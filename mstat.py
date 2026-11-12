import sys, collections
W=[l.split()[1:] for l in open(sys.argv[1]) if l.startswith('W ')]
A=[l.split()[1:] for l in open(sys.argv[1]) if l.startswith('A ')]
by=collections.defaultdict(list); nd=collections.Counter(); tot=collections.Counter()
seen=set()
for a in A:
    wi,now,r1=int(a[0]),int(a[1]),float(a[2]); n=int(a[6])
    if wi in seen: continue
    seen.add(wi)
    w=W[wi]; dl=int(w[1]); left=int(w[3]); end=int(w[10])
    k=0 if n<5 else 1 if n<10 else 2 if n<20 else 3
    tot[k]+=1
    if left: nd[k]+=1; continue
    by[k].append((end-now)*r1/max(1,dl-now))
for k in sorted(by):
    v=sorted(by[k]); q=lambda p: v[min(len(v)-1,int(p*len(v)))]
    print(f"n-bucket {k}: admitted {tot[k]} notdone {nd[k]} m q10 {q(.1):.2f} q30 {q(.3):.2f} q50 {q(.5):.2f} q70 {q(.7):.2f} q90 {q(.9):.2f} q97 {q(.97):.2f}")
