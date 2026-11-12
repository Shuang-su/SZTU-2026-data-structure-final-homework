
import sys, collections
L=collections.defaultdict(dict); F=[]; U=[]
for l in open(sys.argv[1]):
    p=l.split()
    if not p: continue
    if p[0]=='L': L[int(p[1])][int(p[2])]=L[int(p[1])].get(int(p[2]),0)+int(p[3])
    elif p[0]=='FL': F.append((int(p[1]),int(p[2]),int(p[3])))
    elif p[0]=='UP': U.append((int(p[1]),int(p[2])))
allv=sorted(v for x in L for v in L[x].values())
q=lambda p: allv[int(p*(len(allv)-1))]
print('per (machine,tick) log score quantiles 50/90/99/99.9/max', q(.5),q(.9),q(.99),q(.999),allv[-1], 'n',len(allv))
print('fails',len(F))
down=collections.defaultdict(list)
for x,t,_ in F:
    up=min([u for (y,u) in U if y==x and u>t], default=10**9)
    down[x].append((t,up))
    row=[L[x].get(t-k,0) for k in range(12,-1,-1)]
    print('fail m',x,'t',t,'jobs',_,'up',up if up<10**9 else '-','scores t-12..t:',row)
# detector: score at (x,t) >= TH -> predict fail within H ticks
for TH in (20,40,60,100,150,200):
    for H in (5,10,20):
        tp=fp=0; caught=set()
        for x in L:
            for t,v in L[x].items():
                if v<TH: continue
                if any(a<=t<b for a,b in down[x]): continue
                hit=[f for f in F if f[0]==x and t<f[1]<=t+H]
                if hit: tp+=1; caught.add(hit[0][:2])
                else: fp+=1
        print(f'TH {TH} H {H}: alarms tp {tp} fp {fp} fails caught {len(caught)}/{len(F)}')
