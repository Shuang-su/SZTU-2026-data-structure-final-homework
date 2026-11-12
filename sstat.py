
import sys, collections, statistics as st
rows=[list(map(int,l.split()[1:])) for l in open(sys.argv[1]) if l.startswith('S ')]
n=len(rows)
print('starts',n,'mean wait',round(st.mean(r[0] for r in rows),2),'mean tt',round(st.mean(r[1] for r in rows),2),'mean pull',round(st.mean(r[2] for r in rows),2),'mean S',round(st.mean(max(r[1],r[2]) for r in rows),2))
print('coreticks prep', sum(max(r[1],r[2])*r[7] for r in rows), 'wait hist', sorted(collections.Counter(min(r[0]//5,10) for r in rows).items()))
print('tt>0 frac', sum(1 for r in rows if r[1]>0)/n, 'xdc frac', sum(r[6] for r in rows)/n, 'xdc fee', sum(r[3] for r in rows if r[6]), 'intra fee', sum(r[3] for r in rows if not r[6]))
print('qreg>0 frac', sum(1 for r in rows if r[4]>0)/n, 'qrack>0', sum(1 for r in rows if r[5]>0)/n, 'warm', sum(1 for r in rows if r[4]==0 and r[5]==0)/n)
print('ext jobs', sum(r[8] for r in rows)/n, 'ext with tt=0', sum(1 for r in rows if r[8] and r[1]==0)/max(1,sum(r[8] for r in rows)), 'nonext tt>0', sum(1 for r in rows if not r[8] and r[1]>0)/max(1,sum(1 for r in rows if not r[8])))
print('tt hist', sorted(collections.Counter(min(r[1]//5,10) for r in rows).items()))
print('pull hist', sorted(collections.Counter(min(r[2]//3,10) for r in rows).items()))
