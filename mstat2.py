import sys, collections, math
by=collections.defaultdict(list)
for fn in sys.argv[1:]:
    W=[l.split()[1:] for l in open(fn) if l.startswith('W ')]
    seen=set()
    for l in open(fn):
        if not l.startswith('Y '): continue
        p=l.split(); wi=int(p[1])
        if wi in seen: continue
        seen.add(wi)
        d={p[i]:float(p[i+1]) for i in range(2,len(p)-1,2)}
        w=W[wi]; left=int(w[3]); end=int(w[10]); n=int(d['left'])
        k=0 if n<=1 else 1 if n<=3 else 2 if n<=6 else 3 if n<=12 else 4 if n<=24 else 5
        by[k].append(((end-d['now'])/max(1,d['rem'])) if left==0 else 99)
print('left-bucket: n | notdone% | m quantiles 10 25 50 75 90')
for k in sorted(by):
    v=sorted(by[k]); q=lambda p: v[min(len(v)-1,int(p*len(v)))]
    print(['1','2-3','4-6','7-12','13-24','25+'][k].ljust(6), len(v), f"{100*sum(1 for x in v if x==99)/len(v):.0f}%", ' '.join(f"{q(p):.2f}" for p in (.1,.25,.5,.75,.9)))
