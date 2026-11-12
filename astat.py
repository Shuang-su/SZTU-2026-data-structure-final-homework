
import sys, collections
W=[l.split()[1:] for l in open(sys.argv[1]) if l.startswith('W ')]
A=[l.split()[1:] for l in open(sys.argv[1]) if l.startswith('A ')]
tmin=int(sys.argv[2]) if len(sys.argv)>2 else 0
b=collections.defaultdict(lambda:[0,0,0.0,0.0])
for wi,now,r1,r2,f,ov,n in A:
    if int(now)<tmin: continue
    w=W[int(wi)]; done=int(w[3])==0
    k=min(int(float(r1)*10),30)
    b[k][0]+=1; b[k][1]+=done; b[k][2]+=int(w[5]); b[k][3]+=int(w[6])
print('ratio(dl-now)/rem: admitted, done, value, cost')
for k in sorted(b): print(k/10, b[k][0], b[k][1], round(b[k][1]/b[k][0],2), int(b[k][2]), int(b[k][3]))
