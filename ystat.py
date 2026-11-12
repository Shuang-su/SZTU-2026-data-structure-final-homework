import sys, collections
B=collections.defaultdict(lambda:[0,0.0,0.0,0.0,0.0,0])
for fn in sys.argv[1:]:
    W=[l.split()[1:] for l in open(fn) if l.startswith('W ')]
    seen=set()
    for l in open(fn):
        if not l.startswith('Y '): continue
        p=l.split(); wi=int(p[1])
        if wi in seen: continue
        seen.add(wi)
        d={p[i]:float(p[i+1]) for i in range(2,len(p)-1,2)}
        w=W[wi]; arr,dl,n,left,dead,v,cost=int(w[0]),int(w[1]),int(w[2]),int(w[3]),int(w[4]),int(w[5]),int(w[6]); end=int(w[10])
        g=max(5,(dl-arr)//3)
        rev=0 if left else (v if end<=dl else max(0,v*(dl+g-end)//g))
        m=(d['rev']-d['cost'])/max(1,d['cost'])
        k=min(int(m*4),12) if m<3 else 12+min(int(m-3)//2+1,4)
        b=B[k]; b[0]+=1; b[1]+=d['rev']; b[2]+=d['cost']; b[3]+=rev; b[4]+=cost; b[5]+= (left==0)
print('margin bucket: n | pred rev, pred cost, pred profit | real rev, real cost, real profit | done%')
for k in sorted(B):
    b=B[k]; lab = f"{k/4:.2f}" if k<=12 else f">{3+(k-13)*2}"
    print(f"{lab:6s} {b[0]:5d} | {b[1]/1e3:8.0f} {b[2]/1e3:8.0f} {(b[1]-b[2])/1e3:8.0f} | {b[3]/1e3:8.0f} {b[4]/1e3:8.0f} {(b[3]-b[4])/1e3:8.0f} | {100*b[5]/b[0]:.0f}%")
