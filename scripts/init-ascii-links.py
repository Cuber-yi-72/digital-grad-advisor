#!/usr/bin/env python3
"""Create ASCII directory aliases next to the Chinese folders.

Zip/Windows 部分工具链读 `00-核心` 会乱码。解压后在本包根目录跑：
  python scripts/init-ascii-links.py

Creates (does not copy files):
  00-core        -> 00-核心
  01-config      -> 01-配置
  03-templates   -> 03-模板
  04-examples    -> 04-示例

Agent 与文档仍以中文路径为准。链接只给不会中文路径的工具用。
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAP = {
    "00-core": "00-核心",
    "01-config": "01-配置",
    "03-templates": "03-模板",
    "04-examples": "04-示例",
}


def link(dst: Path, src: Path) -> None:
    if dst.exists() or dst.is_symlink():
        print(f"skip exists: {dst.name}")
        return
    if not src.is_dir():
        raise SystemExit(f"ERROR: missing {src}")
    try:
        os.symlink(src.name, dst, target_is_directory=True)
        print(f"symlink {dst.name} -> {src.name}")
        return
    except OSError:
        pass
    if os.name == "nt":
        import subprocess

        r = subprocess.run(["cmd", "/c", "mklink", "/J", str(dst), str(src)], capture_output=True, text=True)
        if r.returncode == 0:
            print(f"junction {dst.name} -> {src.name}")
            return
        print(r.stderr or r.stdout, file=sys.stderr)
    raise SystemExit(f"ERROR: cannot link {dst.name} (Windows 可先开开发者模式或用 Git Bash)")


def main() -> int:
    os.chdir(ROOT)
    for ascii_name, cn in MAP.items():
        link(ROOT / ascii_name, ROOT / cn)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
