#!/usr/bin/env bash
# Thin wrapper. Logic lives in sync-upstream.py (REGISTRY is the only skill list).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
if command -v python3 >/dev/null 2>&1; then
  PYTHON=python3
elif command -v python >/dev/null 2>&1; then
  PYTHON=python
else
  echo "ERROR: need python3 or python" >&2
  exit 1
fi
exec "$PYTHON" "$ROOT/scripts/sync-upstream.py" "$@"
