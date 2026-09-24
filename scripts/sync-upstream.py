#!/usr/bin/env python3
"""Pull MIT upstream skills listed in skills/REGISTRY.md into vendor/.

Source of truth is the REGISTRY table (not a hardcoded skill list).
Usage:
  python3 scripts/sync-upstream.py                  # all vendor ids
  python3 scripts/sync-upstream.py sci.experimental-design phd.experiment-design
Windows (no python3):  python scripts/sync-upstream.py
Requires git on PATH. Do not rewrite LOCKS.md with PowerShell.
"""
from __future__ import annotations

import datetime
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "skills" / "REGISTRY.md"
LOCK = ROOT / "skills" / "LOCKS.md"
VENDOR = ROOT / "vendor"

# Fallback only if REGISTRY `from` has no parenthetical list.
PPTX_FILES = ("SKILL.md", "content_guidelines.md", "slide_patterns.md", "README.md")


def files_from_dot(frm: str) -> tuple[str, ...]:
    if "(" in frm and ")" in frm:
        inner = frm[frm.find("(") + 1 : frm.rfind(")")]
        names = tuple(x.strip() for x in inner.split(",") if x.strip())
        if names:
            return names
    return PPTX_FILES


def is_sep(line: str) -> bool:
    return line.startswith("|") and set(line) <= set("|-: ") and "-" in line


def md_cells(line: str) -> list[str]:
    if not line.startswith("|"):
        return []
    return [c.strip() for c in line.strip("|").split("|")]


def parse_vendor_rows(text: str) -> list[dict]:
    rows: list[dict] = []
    in_table = False
    for line in text.splitlines():
        parts = md_cells(line)
        if len(parts) >= 2 and parts[0] == "id" and parts[1] == "何时":
            in_table = True
            continue
        if not in_table:
            continue
        if is_sep(line):
            continue
        if not line.startswith("|"):
            break
        if len(parts) < 6 or not parts[0]:
            continue
        rows.append(
            {
                "id": parts[0],
                "when": parts[1],
                "repo": parts[2],
                "frm": parts[3],
                "local": parts[4],
                "license": parts[5],
            }
        )
    return rows


def run_git(args: list[str], cwd: Path | None = None) -> str:
    r = subprocess.run(
        ["git", *args],
        cwd=str(cwd) if cwd else None,
        capture_output=True,
        text=True,
    )
    if r.returncode != 0:
        err = (r.stderr or r.stdout or "").strip() or f"exit {r.returncode}"
        print(f"ERROR: git {' '.join(args)} 失败（exit {r.returncode}）", file=sys.stderr)
        print(err, file=sys.stderr)
        print(
            "常见原因：无网、公司代理/TLS（如 SEC_E_NO_CREDENTIALS）、未登录 git、仓库不存在。",
            file=sys.stderr,
        )
        raise SystemExit(r.returncode)
    return r.stdout.strip()


def copy_license(src: Path, dest: Path) -> None:
    dest.mkdir(parents=True, exist_ok=True)
    for name in ("LICENSE", "LICENSE.md"):
        p = src / name
        if p.is_file():
            shutil.copy2(p, dest / name)
            return
    raise SystemExit(f"ERROR: no LICENSE in {src}")


def license_dir(local: str) -> Path:
    parts = Path(local).parts
    # vendor/pkg/skill → vendor/pkg ; vendor/pkg → vendor/pkg
    if len(parts) >= 3:
        return ROOT.joinpath(*parts[:2])
    return ROOT / local


def install_id(row: dict, clone: Path) -> None:
    local = ROOT / row["local"]
    frm = row["frm"]
    if frm.startswith("."):
        local.mkdir(parents=True, exist_ok=True)
        for f in files_from_dot(frm):
            src = clone / f
            if not src.is_file():
                raise SystemExit(f"ERROR: missing {f} in {row['repo']}")
            shutil.copy2(src, local / f)
        copy_license(clone, local)
        return
    src = clone / frm
    if not src.is_dir():
        raise SystemExit(f"ERROR: path drifted: {frm} in {row['repo']}")
    if local.exists():
        shutil.rmtree(local)
    local.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(src, local)
    copy_license(clone, license_dir(row["local"]))


def lock_row(repo: str, sha: str, note: str) -> None:
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    lines = LOCK.read_text(encoding="utf-8").splitlines() if LOCK.exists() else []
    pre, header, sep, body = [], [], [], []
    for line in lines:
        if line.startswith("| repo"):
            header = [line]
        elif is_sep(line):
            sep = [line]
        elif line.startswith("|"):
            parts = [c.strip() for c in line.strip("|").split("|")]
            if len(parts) >= 4 and parts[0] and parts[0] != repo:
                body.append(parts)
        else:
            pre.append(line)
    if not header:
        header = ["| repo | sha | pulled_at_utc | note |"]
    if not sep:
        sep = ["|------|-----|----------------|------|"]
    body.append([repo, sha, stamp, note])
    while pre and pre[-1] == "":
        pre.pop()
    out = pre + ([""] if pre else []) + header + sep + ["| " + " | ".join(r) + " |" for r in body]
    LOCK.parent.mkdir(parents=True, exist_ok=True)
    LOCK.write_text("\n".join(out) + "\n", encoding="utf-8")


def main(argv: list[str]) -> int:
    if not shutil.which("git"):
        print("ERROR: git not on PATH (Windows: install Git for Windows or use WSL)", file=sys.stderr)
        return 1
    rows = parse_vendor_rows(REGISTRY.read_text(encoding="utf-8"))
    if not rows:
        print("ERROR: REGISTRY.md 没有解析到 vendor 行。", file=sys.stderr)
        print("表头须为 id | 何时 | repo | from | local | license（6 列）。改过列名/删过列会静默变空。", file=sys.stderr)
        return 1
    wanted = set(argv) if argv else {r["id"] for r in rows}
    unknown = wanted - {r["id"] for r in rows}
    if unknown:
        print("ERROR: id not in REGISTRY:", ", ".join(sorted(unknown)), file=sys.stderr)
        return 1
    selected = [r for r in rows if r["id"] in wanted]
    by_repo: dict[str, list[dict]] = {}
    for r in selected:
        by_repo.setdefault(r["repo"], []).append(r)

    VENDOR.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="dga-upstream-") as tmp:
        tmp_path = Path(tmp)
        for i, (repo, group) in enumerate(by_repo.items()):
            dest = tmp_path / f"repo-{i}"
            print(f"== {repo} ==")
            run_git(["clone", "--depth", "1", repo, str(dest)])
            sha = run_git(["rev-parse", "HEAD"], cwd=dest)
            for r in group:
                print(f"  {r['id']}  {r['frm']} -> {r['local']}")
                install_id(r, dest)
            note = ",".join(r["id"] for r in group)
            lock_row(repo, sha, note)
            print(f"  sha {sha}")
    print("Done. SHAs in skills/LOCKS.md")
    if LOCK.exists():
        print(LOCK.read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
