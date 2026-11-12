#!/usr/bin/env python3
"""usage: ev.py <binary> cfg1 cfg2 ...   (cfg = "A=1 B=2", "" = defaults)
Runs every case of the sets tune (a,b,p), c and d and prints, per set, the profit relative to the
reference program (REF json) and, paired case by case, relative to the v1 program (BASE json).
SETS=abp,c,d selects sets; SAVE=file keeps the last result json."""
import sys, os, json, glob, subprocess, tempfile, math
binp = sys.argv[1]
ref = {r["case"]: r["profit"] for r in json.load(open(os.environ.get("REF", "w/refall2.json")))}
base = {r["case"]: r["profit"] for r in json.load(open(os.environ.get("BASE", "w/v1_all.json")))}
sets = os.environ.get("SETS", "abp,c,d").split(",")
cases = sorted(c for s in sets for ch in s for c in glob.glob(f"cases/{ch}*.in"))
for cfg in sys.argv[2:]:
    env = dict(os.environ)
    for kv in cfg.split():
        k, v = kv.split("="); env[k] = v
    out = os.environ.get("SAVE") or tempfile.mktemp(suffix=".json")
    subprocess.run([sys.executable, "run.py", binp, *cases, "-j", "10", "-o", out], env=env, stdout=subprocess.DEVNULL)
    res = json.load(open(out))
    if not os.environ.get("SAVE"): os.unlink(out)
    line = f"{cfg or 'default':28s}"
    bad = sum(1 for r in res if r["profit"] is None or "对账错误 0/" not in r["msg"] or "非法指令 0，" not in r["msg"])
    for s in sets + ["all", "weak", "rest"]:  # weak: cases where v1 earned less than the reference
        rs = [r for r in res if r["profit"] is not None and (s == "all" or (s == "weak" and base[r["case"]] < ref[r["case"]]) or (s == "rest" and base[r["case"]] >= ref[r["case"]]) or r["case"][0] in s)]
        if os.environ.get("BRIEF") and s not in ("all", "weak", "rest"): continue
        rat = sorted(r["profit"] / ref[r["case"]] for r in rs)
        pb = [r["profit"] / base[r["case"]] for r in rs if base[r["case"]] > 0]
        tot = sum(r["profit"] for r in rs) / sum(base[r["case"]] for r in rs)
        gm = math.exp(sum(math.log(max(x, 1e-9)) for x in pb) / len(pb))
        worse = sum(1 for x in pb if x < 0.98); better = sum(1 for x in pb if x > 1.02)
        if os.environ.get("BRIEF"): line += f" | {s}: med {rat[len(rat)//2]:.3f} <1:{sum(1 for x in rat if x<1):2d} v1 tot {tot:.4f} gm {gm:.4f} +{better}/-{worse}"
        else: line += f" | {s}: ref med {rat[len(rat)//2]:.3f} q10 {rat[len(rat)//10]:.3f} min {rat[0]:.3f} <1:{sum(1 for x in rat if x<1):2d}  v1 tot {tot:.4f} gm {gm:.4f} +{better}/-{worse}"
    print(line + f" | bad {bad} maxcpu {max(r['cpu'] for r in res):.2f}", flush=True)
