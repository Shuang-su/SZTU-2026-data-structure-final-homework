
import sys, collections
W=[l.split()[1:] for l in open(sys.argv[1]) if l.startswith('W ')]
A=[l.split()[1:] for l in open(sys.argv[1]) if l.startswith('A ')]
tot=[0,0]; byn=collections.defaultdict(lambda:[0,0,0])
for wi,now,r1,r2,f,ov,n,c0 in A:
    w=W[int(wi)]
    if int(w[3])!=0 or int(now)<60: continue
    tot[0]+=float(c0); tot[1]+=int(w[6])
    k=min(int(n)//10,3); byn[k][0]+=float(c0); byn[k][1]+=int(w[6]); byn[k][2]+=1
print('done flows: predicted cost', int(tot[0]), 'actual', tot[1], 'ratio', round(tot[1]/tot[0],3), {k:(v[2],round(v[1]/v[0],2)) for k,v in sorted(byn.items())})
