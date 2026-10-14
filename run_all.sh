#!/bin/sh
# Runs every program in code/ and regenerates the figures in figures/
cd "$(dirname "$0")/code" || exit 1
for f in Task_*.py; do
  echo "=== $f"
  python3 "$f"
done
