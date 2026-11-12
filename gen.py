#!/usr/bin/env python3
"""Generate varied practice parameter files (the judge builds the world from them)."""
import random, sys, os
n = int(sys.argv[1]); prefix = sys.argv[2]; base = int(sys.argv[3]) if len(sys.argv) > 3 else 1000
os.makedirs(os.path.dirname(prefix) or ".", exist_ok=True)
for i in range(n):
    rnd = random.Random(base + i)
    D = rnd.randint(2, 5)
    rpd = rnd.randint(3, min(6, 30 // D))
    lo = rnd.randint(4, 8); hi = rnd.randint(lo + 2, 14)
    while D * rpd * hi > 360: hi -= 1
    p = dict(seed=rnd.randint(1, 10**9), T=rnd.randint(400, 600), D=D, nodes_per_dc=rnd.randint(40, 600 // D if 600 // D < 120 else 120),
             racks_per_dc=rpd, mach_per_rack_lo=lo, mach_per_rack_hi=max(hi, lo), NT=rnd.randint(30, 200), NL=rnd.randint(150, 400),
             NI=rnd.randint(40, 120), p_noise=rnd.randint(3000, 10000), p_signal=rnd.randint(20, 60), W=rnd.randint(20, 60),
             load=round(rnd.uniform(0.6, 1.2), 2), sigma=round(rnd.uniform(0.2, 0.5), 2), bias_lo=round(rnd.uniform(0.6, 0.9), 2),
             bias_hi=round(rnd.uniform(1.3, 2.2), 2), fail_frac=round(rnd.uniform(0.05, 0.3), 2), precursor_frac=round(rnd.uniform(0.4, 0.9), 2),
             falsealarm_frac=round(rnd.uniform(0, 0.3), 2), blackswan=rnd.randint(0, 1), link_events=rnd.randint(50, 400),
             quota_events=rnd.randint(20, 120), log_rate=round(rnd.uniform(0.1, 0.25), 2), straggler_p=round(rnd.uniform(0.03, 0.12), 2),
             audit_rate=round(rnd.uniform(2, 5.5), 1))
    with open(f"{prefix}{i:02d}.in", "w") as f:
        for k, v in p.items(): f.write(f"{k} {v}\n")
