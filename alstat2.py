import sys, collections
for fn in sys.argv[1:]:
    L=collections.defaultdict(dict); F=[]; U=[]
    for l in open(fn):
        p=l.split()
        if not p: continue
        if p[0]=='L': L[int(p[1])][int(p[2])]=L[int(p[1])].get(int(p[2]),0)+int(p[3])
        elif p[0]=='FL': F.append((int(p[1]),int(p[2]),int(p[3])))
        elif p[0]=='UP': U.append((int(p[1]),int(p[2])))
    allv=sorted(v for x in L for v in L[x].values())
    h=collections.Counter(min(v//20,15) for v in allv)
    print(fn.split('/')[-1], 'hist/20:', [h[i] for i in range(16)])
    cnt=collections.Counter(t for _,t,_ in F); mass={t for t,c in cnt.items() if c>=4}
    ind=[f for f in F if f[1] not in mass]
    for TH in (60,80,100,130):
        lead=[]; miss=0
        for x,t,_ in ind:
            ts=[u for u,v in L[x].items() if v>=TH and t-40<=u<t]
            if ts: lead.append((t-min(ts), t-max(ts), len(ts)))
            else: miss+=1
        # false episodes: signal ticks not within 40 before a failure
        fp=collections.defaultdict(list)
        for x in L:
            for u,v in L[x].items():
                if v>=TH and not any(y==x and 0<t-u<=40 for y,t,_ in F): fp[x].append(u)
        nfp=sum(len(v) for v in fp.values())
        # count episodes (gaps>15)
        ep=0; eplen=[]
        for x,v in fp.items():
            v.sort(); s=v[0]; p=v[0]
            for u in v[1:]:
                if u-p>15: ep+=1; eplen.append(p-s+1); s=u
                p=u
            ep+=1; eplen.append(p-s+1)
        lead.sort()
        print(f'  TH {TH}: indiv fails {len(ind)} missed {miss}; first-signal lead med {lead[len(lead)//2][0] if lead else 0} min {lead[0][0] if lead else 0}; last-signal gap med {sorted(l[1] for l in lead)[len(lead)//2] if lead else 0}; signals/fail med {sorted(l[2] for l in lead)[len(lead)//2] if lead else 0}; false signal ticks {nfp} episodes {ep} len med {sorted(eplen)[len(eplen)//2] if eplen else 0} max {max(eplen) if eplen else 0}')
