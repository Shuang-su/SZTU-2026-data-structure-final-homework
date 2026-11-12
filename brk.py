#!/usr/bin/env python3
"""usage: brk.py result.json ... : revenue / cost breakdown summed over all cases of each result file."""
import sys, json, re
g = lambda m, k: int(re.search(k + r" ?(-?\d+)", m).group(1))
for fn in sys.argv[1:]:
    A = {}
    for r in json.load(open(fn)):
        m = r["msg"]; wf = re.search(r"工作流 (\d+) 个，完成 (\d+)（按时 (\d+)，逾期 (\d+)", m)
        for k, v in dict(profit=g(m, "利润"), rev=g(m, "收益"), run=g(m, "运行费"), intr=g(m, "被中断浪费"), pull=g(m, "拉取费"), tr=g(m, "传输费"), U=g(m, "上界 U="), n=int(wf[1]), done=int(wf[2]), late=int(wf[4])).items():
            A[k] = A.get(k, 0) + v
    R = A["rev"]
    print(f"{fn}: profit {A['profit']/1e6:.1f}M rev {R/1e6:.1f}M | of rev: profit {A['profit']/R:.3f} run {A['run']/R:.3f} (interrupted {A['intr']/R:.3f}) pull {A['pull']/R:.3f} transfer {A['tr']/R:.3f} | profit/U {A['profit']/A['U']:.3f} done {A['done']/A['n']:.3f} late/done {A['late']/A['done']:.3f}")
