#!/usr/bin/env python3
"""Sanity-check the toolkit. No network.

  python3 scripts/validate.py
  python  scripts/validate.py
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_sync():
    spec = importlib.util.spec_from_file_location("sync", ROOT / "scripts" / "sync-upstream.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> int:
    errors: list[str] = []

    def err(msg: str) -> None:
        errors.append(msg)
        print("FAIL:", msg)

    for d in sorted(p for p in (ROOT / "skills").iterdir() if p.is_dir()):
        sk = d / "SKILL.md"
        if not sk.is_file():
            err(f"{d.name}: missing SKILL.md")
            continue
        text = sk.read_text(encoding="utf-8")
        if not text.startswith("---"):
            err(f"{d.name}: no YAML frontmatter")
            continue
        name = None
        for line in text.split("---", 2)[1].splitlines():
            if line.startswith("name:"):
                name = line.split(":", 1)[1].strip()
        if name != d.name:
            err(f"{d.name}: YAML name={name!r} != folder")
        if "\n# |" in text or text.lstrip().startswith("# |"):
            err(f"{d.name}: table row starts with '# |' (would render as h1)")

    sync = load_sync()
    rows = sync.parse_vendor_rows((ROOT / "skills" / "REGISTRY.md").read_text(encoding="utf-8"))
    if not rows:
        err("REGISTRY.md parsed 0 vendor rows (表头可能被改过)")
    else:
        print(f"ok REGISTRY {len(rows)} ids")

    for rel in ("00-核心/SYSTEM.md", "LICENSE", "AGENTS.md", "03-模板/中期考核.md"):
        if not (ROOT / rel).is_file():
            err(f"missing {rel}")

    if errors:
        print(f"{len(errors)} error(s)")
        return 1
    print("validate ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
