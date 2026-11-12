#!/usr/bin/env python3
"""Offline analysis of a recorded judge stream (REC=file) to understand the workload."""
import sys, collections, statistics as st

toks = open(sys.argv[1]).read().split()
p = 0
def nx():
    global p
    p += 1
    return toks[p - 1]
def ni():
    return int(nx())

T, D, N, R, M, K, L, I, P, W, E = [ni() for _ in range(11)]
Breg, Brack, Bnet, Ureg, Unet = [ni() for _ in range(5)]
price = [ni() for _ in range(D)]
racks = [(ni(), ni(), ni()) for _ in range(R)]
machs = [(ni(), ni(), ni(), ni()) for _ in range(M)]
edges = [(ni(), ni(), ni()) for _ in range(E)]
tens = [(ni(), ni()) for _ in range(K)]
lsz = [ni() for _ in range(L)]
imgs = []
for _ in range(I):
    k = ni(); imgs.append([ni() for _ in range(k)])
freq = [ni() for _ in range(9)]
pats = [(nx(), ni()) for _ in range(P)]
print("T,D,N,R,M,K,L,I,P,W,E", T, D, N, R, M, K, L, I, P, W, E)
print("B", Breg, Brack, Bnet, "U", Ureg, Unet, "price", price)
cap = collections.Counter(); mem = collections.Counter()
for r, c, m, mc in machs:
    cap[racks[r][0]] += c; mem[racks[r][0]] += m
print("cpu per dc", dict(cap), "mem per dc", dict(mem), "total cpu", sum(cap.values()))
print("mach cpu dist", collections.Counter(c for _, c, _, _ in machs))
print("mach mem dist", collections.Counter(m for _, _, m, _ in machs))
print("mcap", min(x[3] for x in machs), max(x[3] for x in machs), "rcap", [x[2] for x in racks])
print("layer size", min(lsz), st.mean(lsz), max(lsz), "img layers", collections.Counter(len(x) for x in imgs))
print("img size mean", st.mean(sum(lsz[l] for l in im) for im in imgs))
print("edge w", min(e[2] for e in edges), st.mean(e[2] for e in edges), max(e[2] for e in edges))
print("quota", sorted(q for _, q in tens)[:10], "...", sorted(q for _, q in tens)[-10:], "root", tens[0])
depth = []
for i in range(K):
    d = 0; a = i
    while tens[a][0] >= 0:
        a = tens[a][0]; d += 1
    depth.append(d)
print("tenant depth", collections.Counter(depth))
pw = collections.Counter(w for _, w in pats)
print("pattern weights (top)", sorted(pw.items())[-12:], "len", collections.Counter(len(s) for s, _ in pats))

flows = []; evc = collections.Counter(); fails = []; logs = collections.Counter()
while p < len(toks):
    assert nx() == "TICK"
    t, ne, nq = ni(), ni(), ni()
    for _ in range(ne):
        e = nx(); evc[e] += 1
        if e == "WF":
            w, o, v, dl, n = ni(), ni(), ni(), ni(), ni()
            js = []
            for _ in range(n):
                j, c, m, ee, im, s, zi, zo, k = [ni() for _ in range(9)]
                pr = [ni() for _ in range(k)]
                js.append((j, c, m, ee, im, s, zi, zo, pr))
            flows.append((t, w, o, v, dl, js))
        elif e == "LOG":
            x = ni(); ni(); nx(); logs[x] += 1
        elif e in ("QUOTA",):
            ni(); ni()
        elif e == "FAIL":
            fails.append((t, ni()))
        else:
            ni()
    for _ in range(nq):
        q = nx(); ni()
        if q == "ROUTE": ni()
print("events", dict(evc))
print("flows", len(flows), "jobs", sum(len(f[5]) for f in flows))
print("n per flow", collections.Counter(len(f[5]) for f in flows).most_common(12))
allj = [j for f in flows for j in f[5]]
print("c", collections.Counter(j[1] for j in allj)); print("m", collections.Counter(j[2] for j in allj))
es = [j[3] for j in allj]
print("e", min(es), st.mean(es), max(es))
print("ext input frac", sum(1 for j in allj if j[5] >= 0) / len(allj), "zin mean", st.mean(j[6] for j in allj if j[5] >= 0), "zout mean", st.mean(j[7] for j in allj))
print("npred", collections.Counter(len(j[8]) for j in allj).most_common(8))
work = sum(j[1] * j[3] for j in allj)
print("total est work core-ticks", work, "capacity core-ticks", sum(cap.values()) * T, "ratio", work / (sum(cap.values()) * T))
print("value", min(f[3] for f in flows), st.mean(f[3] for f in flows), max(f[3] for f in flows), "sum", sum(f[3] for f in flows))
# per-flow: value per core-tick, deadline slack vs critical path
dens = []; slk = []
for t, w, o, v, dl, js in flows:
    idx = {j[0]: i for i, j in enumerate(js)}
    fin = [0] * len(js)
    for i, j in enumerate(js):
        fin[i] = max([fin[idx[q]] for q in j[8]] + [0]) + j[3]
    cp = max(fin); wk = sum(j[1] * j[3] for j in js)
    dens.append(v / wk); slk.append((dl - t) / cp)
dens.sort(); slk.sort()
q = lambda a, f: a[int(f * (len(a) - 1))]
print("value/coretick quantiles", [round(q(dens, f), 2) for f in (0, .1, .25, .5, .75, .9, 1)])
print("(dl-arrive)/critpath quantiles", [round(q(slk, f), 2) for f in (0, .1, .25, .5, .75, .9, 1)])
arr = collections.Counter(f[0] // 50 for f in flows)
print("arrivals per 50 ticks", sorted(arr.items()))
print("tenants of flows", len(set(f[2] for f in flows)))
print("fails", len(fails), "fail ticks sample", fails[:20])

print("=== extra ===")
# quota pressure: subtree work vs quota*T
sub = collections.Counter(); subv = collections.Counter()
for t, w, o, v, dl, js in flows:
    wk = sum(j[1] * j[3] for j in js)
    a = o
    while a >= 0:
        sub[a] += wk; subv[a] += v; a = tens[a][0]
rows = sorted(((sub[a] / (tens[a][1] * T), a, tens[a][1], sub[a], depth[a]) for a in sub), reverse=True)
print("quota load (work/(quota*T)) top:", [(round(x, 2), a, q, d) for x, a, q, wk, d in rows[:25]])
print("num tenants with load>0.5:", sum(1 for r in rows if r[0] > .5), "of", len(rows))
leaf = set(f[2] for f in flows)
print("leaf tenant quota", sorted(tens[a][1] for a in leaf))
# image sharing
lc = collections.Counter(l for im in imgs for l in im)
print("layer usage count", collections.Counter(lc.values()), "unused layers", L - len(lc))
print("images sample", imgs[:6])
# image popularity
ic = collections.Counter(j[4] for j in allj)
print("image popularity", sorted(ic.values()))
# images per flow
print("distinct images per flow", collections.Counter(len(set(j[4] for j in f[5])) for f in flows).most_common(10))
# rack distances
import heapq
adj = collections.defaultdict(list)
for u, v, w in edges:
    adj[u].append((v, w)); adj[v].append((u, w))
def dij(s):
    d = {s: 0}; pq = [(0, s)]
    while pq:
        x, u = heapq.heappop(pq)
        if x > d[u]: continue
        for v, w in adj[u]:
            if x + w < d.get(v, 1e9): d[v] = x + w; heapq.heappush(pq, (d[v], v))
    return d
dm = []
for r in range(R):
    d = dij(racks[r][1]); dm.append([d.get(racks[b][1], -1) for b in range(R)])
for r in range(R): print(racks[r][0], dm[r])
# ext input rack vs flows
print("ext racks per flow", collections.Counter(len(set(j[5] for j in f[5] if j[5] >= 0)) for f in flows).most_common(6))
print("zin dist", collections.Counter(min(j[6] // 10, 9) for j in allj if j[5] >= 0), "zout", collections.Counter(j[7] // 5 for j in allj))
# deadlines beyond T
print("flows with dl>T", sum(1 for f in flows if f[4] > T), "value", sum(f[3] for f in flows if f[4] > T))
print("dl-arrive quantiles", sorted(f[4] - f[0] for f in flows)[::len(flows) // 10])
print("value by size bucket", [(k, round(st.mean(f[3] for f in flows if len(f[5]) // 5 == k))) for k in range(8) if any(len(f[5]) // 5 == k for f in flows)])
print("=== extra2 ===")
print("distinct DCs of ext inputs per flow", collections.Counter(len(set(racks[j[5]][0] for j in f[5] if j[5] >= 0)) for f in flows).most_common(6))
print("root job has ext", sum(1 for f in flows if f[5][0][5] >= 0) / len(flows))
cnt = collections.Counter()
for f in flows:
    rs = [j[5] for j in f[5] if j[5] >= 0]
    if len(rs) >= 2:
        cnt[len(set(rs)) == 1] += 1
print("multi-ext flows: all same rack?", cnt)
for f in flows[:14]:
    print(f[0], f[2], f[3], f[4], [(j[1], j[2], j[3], j[4], j[5], j[6], j[7], [next(i for i, q in enumerate(f[5]) if q[0] == p) for p in j[8]]) for j in f[5]])
tw = collections.Counter(); tv = collections.Counter(); tn = collections.Counter()
for f in flows:
    tw[f[2]] += sum(j[1] * j[3] for j in f[5]); tv[f[2]] += f[3]; tn[f[2]] += 1
print("per leaf tenant: n, value density", sorted((round(tv[a] / tw[a], 1), tn[a], a) for a in tw))
