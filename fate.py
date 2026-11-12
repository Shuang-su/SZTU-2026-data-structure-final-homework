#!/usr/bin/env python3
"""usage: fate.py <keep-dir> case...  : classify every workflow of a DBG run by its fate (from the W lines)."""
import sys, re, collections
d = sys.argv[1]
for c in sys.argv[2:]:
    err = open(f"{d}/{c}.err").read()
    cat = collections.defaultdict(lambda: [0, 0, 0, 0.0, 0.0])
    T = max(int(l.split()[2]) for l in err.split("\n") if l.startswith("W "))
    for l in err.split("\n"):
        if not l.startswith("W "): continue
        a, dl, n, left, dead, v, cost, cp, ten, f, endT = l.split()[1:]
        a, dl, n, left, dead, v, cost, endT = map(int, (a, dl, n, left, dead, v, cost, endT)); cp = float(cp); f = float(f)
        if left == 0: k = "done"
        elif cost > 0 and dead: k = "killed"
        elif cost > 0: k = "started,unfinished"
        elif dead: k = "never started,dead"
        else: k = "never started,waiting"
        x = cat[k]; x[0] += 1; x[1] += v; x[2] += cost; x[3] += (dl - a) / max(1, cp * f); x[4] += n
    tv = sum(x[1] for x in cat.values())
    print(c, re.search(r"BLK.*", err).group(0))
    for k, x in sorted(cat.items()):
        print(f"  {k:24s} n {x[0]:5d} v {x[1]/tv:.3f} cost/v {x[2]/max(1,x[1]):.3f} window/(cp*f) {x[3]/x[0]:.2f} jobs/flow {x[4]/x[0]:.1f}")
