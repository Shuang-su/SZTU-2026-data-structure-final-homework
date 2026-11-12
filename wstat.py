
import sys, collections, statistics as st
rows=[l.split()[1:] for l in open(sys.argv[1]) if l.startswith('W ')]
R=[dict(a=int(a),dl=int(dl),n=int(n),left=int(left),dead=int(dead),v=int(v),c=int(c),cp=float(cp),t=int(t),f=float(f),end=int(e)) for a,dl,n,left,dead,v,c,cp,t,f,e in rows]
def grp(r):
    if r['left']==0: return 'done'
    return 'startedND' if r['c']>0 else 'never'
for lo,hi in ((1,4),(5,9),(10,19),(20,99)):
    sel=[r for r in R if lo<=r['n']<=hi]
    print('n in',lo,hi,'count',len(sel),'value',sum(r['v'] for r in sel))
    for g in ('done','startedND','never'):
        s2=[r for r in sel if grp(r)==g]
        if not s2: continue
        win=sorted((r['dl']-r['a'])/(r['cp']*r['f']) for r in s2)
        line=f"   {g:10s} n={len(s2):4d} value={sum(r['v'] for r in s2):9d} cost={sum(r['c'] for r in s2):8d} window/cp q10,50,90={win[len(win)//10]:.2f},{win[len(win)//2]:.2f},{win[9*len(win)//10]:.2f}"
        if g!='never':
            stz=sorted((r['end']-r['a'])/(r['cp']*r['f']) for r in s2)
            line+=f" elapsed/cp q10,50,90={stz[len(stz)//10]:.2f},{stz[len(stz)//2]:.2f},{stz[9*len(stz)//10]:.2f}"
            if g=='startedND': line+=" fracdone=%.2f"%st.mean(1-r['left']/r['n'] for r in s2)
        print(line)
