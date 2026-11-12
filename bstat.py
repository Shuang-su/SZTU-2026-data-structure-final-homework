import sys, collections
# 2-D table of realised profit of admitted flows: rows = number of jobs, cols = (deadline window)/(remaining estimate) at admission
B=collections.defaultdict(lambda:[0,0.0,0.0,0.0,0])
nb=[1,3,6,12,24,48,999]; sb=[1.0,1.15,1.3,1.5,1.8,2.3,3,99]
mode=sys.argv[1]
for fn in sys.argv[2:]:
    W=[l.split()[1:] for l in open(fn) if l.startswith('W ')]
    seen=set()
    for l in open(fn):
        if not l.startswith('Y '): continue
        p=l.split(); wi=int(p[1])
        if wi in seen: continue
        seen.add(wi)
        d={p[i]:float(p[i+1]) for i in range(2,len(p)-1,2)}
        w=W[wi]; arr,dl,n,left,dead,v,cost=map(int,w[:7]); end=int(w[10])
        g=max(5,(dl-arr)//3)
        rev=0 if left else (v if end<=dl else max(0,v*(dl+g-end)//g))
        a=next(i for i,x in enumerate(nb) if n<=x)
        if mode=='slack': s=(dl-d['now'])/max(1,d['rem'])
        else: s=1+(d['rev']-d['cost'])/max(1,d['cost'])/2
        b=next(i for i,x in enumerate(sb) if s<=x)
        e=B[(a,b)]; e[0]+=1; e[1]+=rev; e[2]+=cost; e[3]+=d['rev']-d['cost']; e[4]+=(left==0)
print('rows: n<=',nb,' cols:',mode,'<=',sb)
for title,fn in (('count',lambda e:f"{e[0]:7d}"),('real profit K',lambda e:f"{(e[1]-e[2])/1e3:7.0f}"),('real cost K',lambda e:f"{e[2]/1e3:7.0f}"),('done %',lambda e:f"{100*e[4]/max(1,e[0]):7.0f}"),('real/pred profit',lambda e:f"{(e[1]-e[2])/max(1,e[3]):7.2f}")):
    print(title)
    for a in range(len(nb)):
        print(f"{nb[a]:4d} "+' '.join(fn(B[(a,b)]) for b in range(len(sb))))
