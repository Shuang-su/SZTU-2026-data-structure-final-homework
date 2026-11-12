#!/usr/bin/env python3
import sys, json, re
a = {r["case"]: r for r in json.load(open(sys.argv[1]))}
b = {r["case"]: r for r in json.load(open(sys.argv[2]))}
def f(m):
    g = lambda k: int(re.search(k + r" ?(-?\d+)", m).group(1))
    return g("收益"), g("运行费"), g("拉取费"), g("传输费"), g("完成"), g("上界 U="), g("工作流")
tot=[0]*8
print("case   ratio |  ref: rev run pull xfer done | cur: rev run pull xfer done | U flows")
for k in sorted(a):
    ra, rb = f(a[k]["msg"]), f(b[k]["msg"])
    print(f"{k[:-3]:5s} {b[k]['profit']/a[k]['profit']:5.2f} | {ra[0]/1e3:7.0f} {ra[1]/1e3:6.0f} {ra[2]/1e3:5.0f} {ra[3]/1e3:5.0f} {ra[4]:5d} | {rb[0]/1e3:7.0f} {rb[1]/1e3:6.0f} {rb[2]/1e3:5.0f} {rb[3]/1e3:5.0f} {rb[4]:5d} | {ra[5]/1e3:6.0f} {ra[6]} P/U ref {a[k]['profit']/ra[5]:.2f} cur {b[k]['profit']/ra[5]:.2f}")
