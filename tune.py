#!/usr/bin/env python3
"""usage: tune.py <binary> <case-glob-prefix> cfg1 cfg2 ...   (cfg = "A=1 B=2"); prints mean profit ratio vs reference json."""
import sys, os, json, glob, subprocess, tempfile
binp, pat = sys.argv[1], sys.argv[2]
cases = sorted(glob.glob(pat))
ref = {r["case"]: r for r in json.load(open(os.environ.get("REF", "w/ref.json")))}
for cfg in sys.argv[3:]:
    env = dict(os.environ)
    for kv in cfg.split():
        k, v = kv.split("="); env[k] = v
    out = tempfile.mktemp(suffix=".json")
    subprocess.run([sys.executable, "run.py", binp, *cases, "-j", "14", "-o", out], env=env, stdout=subprocess.DEVNULL)
    res = json.load(open(out)); os.unlink(out)
    rat = []; bad = 0
    for r in res:
        if r["profit"] is None or "对账错误 0/" not in r["msg"] or "非法指令 0，" not in r["msg"]:
            bad += 1; continue
        rat.append(r["profit"] / ref[r["case"]]["profit"])
    rat.sort()
    tr = rat[len(rat)//10: len(rat) - len(rat)//10]
    print(f"{cfg:40s} trim {sum(tr)/len(tr):.4f} med {rat[len(rat)//2]:.3f} q10 {rat[len(rat)//10]:.3f} min {rat[0]:.3f} <.9:{sum(1 for x in rat if x<.9)} >1.1:{sum(1 for x in rat if x>1.1)}/{len(rat)} bad {bad} maxcpu {max(r['cpu'] for r in res):.2f}", flush=True)
