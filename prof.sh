#!/bin/sh
# usage: prof.sh case...  -- records the judge's stream with the current DBG binary, then replays it offline
for c in "$@"; do
  REC=$PWD/w/$c.rec python3 run.py bin/sol cases/$c.in >/dev/null 2>&1
  echo "== $c"
  ./bin/sol < w/$c.rec 2>&1 >/dev/null | grep -E "PERF (net|total)"
done
