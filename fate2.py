#!/usr/bin/env python3
"""usage: fate2.py <keep-dir> : fate of all workflows over all cases, by size bucket (share of total value)."""
import sys, glob, collections
def bucket(n): return '01-03' if n <= 3 else '04-08' if n <= 8 else '09-20' if n <= 20 else '21-40' if n <= 40 else '41+'
C = collections.defaultdict(lambda: collections.defaultdict(float)); tv = 0; tcost = 0; nd = 0; rev = 0
for fn in glob.glob(sys.argv[1] + '/*.err'):
    for l in open(fn):
        if not l.startswith('W '): continue
        a, dl, n, left, dead, v, cost, cp, ten, f, endT = l.split()[1:]
        a, dl, n, left, dead, v, cost, endT = map(int, (a, dl, n, left, dead, v, cost, endT))
        k = 'done' if left == 0 else 'killed' if cost > 0 and dead else 'unfinished' if cost > 0 else 'dead-unstarted' if dead else 'waiting'
        b = C[bucket(n)]; b[k] += v; b['v'] += v; b['cost_' + ('d' if left == 0 else 'nd')] += cost; tv += v; tcost += cost
        if left == 0:
            G = max(5, (dl - a) // 3); rv = v if endT <= dl else 0 if endT >= dl + G else v * (dl + G - endT) // G
            b['rev'] += rv; rev += rv
        else: nd += cost
print(f"total value {tv/1e6:.0f}M revenue {rev/1e6:.0f}M cost {tcost/1e6:.0f}M costNotDone {nd/1e6:.0f}M ({nd/rev:.3f} of revenue)")
print("bucket  value-share | done killed unfinished dead-unstarted waiting (share of bucket value) | profit M | costNotDone M")
for k in sorted(C):
    b = C[k]
    print(f"{k}   {b['v']/tv:.3f} | {b['done']/b['v']:.2f} {b['killed']/b['v']:.2f} {b['unfinished']/b['v']:.2f} {b['dead-unstarted']/b['v']:.2f} {b['waiting']/b['v']:.2f} | {(b['rev']-b['cost_d']-b['cost_nd'])/1e6:.0f} | {b['cost_nd']/1e6:.0f}")
