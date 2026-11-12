#!/usr/bin/env python3
import sys, json, math
a = {r["case"]: r for r in json.load(open(sys.argv[1]))}
b = {r["case"]: r for r in json.load(open(sys.argv[2]))}
rat = []
for k in sorted(a):
    if k in b and a[k]["profit"] and b[k]["profit"] is not None:
        rat.append((b[k]["profit"] / a[k]["profit"], k))
if "-v" in sys.argv:
    print(" ".join(f"{k[:-3]}:{r:.2f}" for r, k in rat))
print(f"mean ratio {sum(r for r, _ in rat) / len(rat):.4f}  min {min(rat)[0]:.3f} ({min(rat)[1]})  max {max(rat)[0]:.3f}  wins {sum(1 for r, _ in rat if r > 1)}/{len(rat)}  maxcpu {max(r['cpu'] for r in b.values()):.3f}")
