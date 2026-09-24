#!/usr/bin/env python3
"""Truncate USAGE.md but keep the last row for every id. Never drop an id's only record.

Read/write UTF-8 (no BOM). Only this script should rewrite USAGE.md —
do not pipe it through PowerShell Get-Content/Set-Content (encoding will break).
Windows: `python scripts/compact-usage.py` if `python3` is missing.
"""
from pathlib import Path


def is_sep(line: str) -> bool:
    # Distinguish `|---` separator from empty placeholder `|  |  |` (no dashes).
    return line.startswith("|") and set(line) <= set("|-: ") and "-" in line


p = Path(__file__).resolve().parents[1] / "skills" / "USAGE.md"
text = p.read_text(encoding="utf-8")
lines = text.splitlines()
pre, table = [], []
seen_header = False
for line in lines:
    if line.startswith("| 日期") or (seen_header and line.startswith("|")):
        seen_header = True
        table.append(line)
    elif not seen_header:
        pre.append(line)

header, sep, rows = [], [], []
for line in table:
    if line.startswith("| 日期"):
        header = [line]
    elif is_sep(line):
        sep = [line]
    elif line.startswith("|"):
        rows.append(line)

if not sep:
    sep = ["|------|------------------------------|------------|"]

last = {}
order = []
for row in rows:
    cols = [c.strip() for c in row.strip("|").split("|")]
    if len(cols) < 2 or not cols[1]:
        continue
    key = cols[1]
    if key not in last:
        order.append(key)
    last[key] = row

out = pre + ([""] if pre and pre[-1] != "" else []) + header + sep + [last[k] for k in order]
p.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")
print(f"compact-usage: {len(rows)} rows -> {len(last)} ids")
