import json,re,sys
for f in sys.argv[1:]:
    r=json.load(open(f))
    g=lambda m,k:int(re.search(k+r" ?(-?\d+)",m).group(1))
    print(f, 'profit',sum(x['profit'] for x in r),'waste',sum(g(x['msg'],'中断浪费') for x in r),'run',sum(g(x['msg'],'运行费') for x in r))
