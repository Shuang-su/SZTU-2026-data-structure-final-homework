#!/usr/bin/env python3
"""Local harness: run a solution binary against the official judge (tpj_win.exe via CrossOver wine).

usage: run.py <solution-binary> <case.in> [more cases...] [-j N] [-v]
Prints one line per case: name profit status cpu_seconds, then a total.
"""
import os, sys, subprocess, re, resource, tempfile, time, json
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
WINE = "/Applications/CrossOver.app/Contents/SharedSupport/CrossOver/bin/wine"
TPJ = os.path.join(HERE, "kit", "tpj_win.exe")


def run_case(sol, case, keep=None):
    case = os.path.abspath(case)
    d = tempfile.mkdtemp(prefix="tpj_")
    out = os.path.join(d, "out.txt")
    ans = os.path.join(d, "ans.txt")
    open(ans, "w").close()
    r1, w1 = os.pipe()  # judge -> sol
    r2, w2 = os.pipe()  # sol -> judge
    env = dict(os.environ)
    env["WINEDEBUG"] = "-all"
    errf = open(os.path.join(d, "err.txt"), "wb")
    solerr = open(os.path.join(d, "solerr.txt"), "wb")
    judge = subprocess.Popen([WINE, "--bottle", "starring_tpj", TPJ, case, out, ans],
                             stdin=r2, stdout=w1, stderr=errf, env=env, cwd=d)
    solp = subprocess.Popen([sol], stdin=r1, stdout=w2, stderr=solerr)
    for fd in (r1, w1, r2, w2):
        os.close(fd)
    t0 = time.time()
    _, st, ru = os.wait4(solp.pid, 0)
    solp.returncode = st
    cpu = ru.ru_utime + ru.ru_stime
    try:
        judge.wait(timeout=60)
    except subprocess.TimeoutExpired:
        judge.kill()
    errf.close(); solerr.close()
    msg = open(os.path.join(d, "err.txt"), "rb").read().decode("utf8", "replace").strip()
    serr = open(os.path.join(d, "solerr.txt"), "rb").read().decode("utf8", "replace")
    kd = os.environ.get("KEEP")
    if kd:
        os.makedirs(kd, exist_ok=True)
        with open(os.path.join(kd, os.path.basename(case) + ".err"), "w") as f:
            f.write(serr)
    msg = msg.split("\n")[0]
    m = re.search(r"利润 (-?\d+)", msg)
    profit = int(m.group(1)) if m else None
    import shutil
    shutil.rmtree(d, ignore_errors=True)
    return dict(case=os.path.basename(case), profit=profit, msg=msg, cpu=cpu, st=st, wall=time.time() - t0)


def main():
    args = sys.argv[1:]
    jobs = 12
    verbose = False
    if "-v" in args:
        verbose = True; args.remove("-v")
    if "-j" in args:
        i = args.index("-j"); jobs = int(args[i + 1]); del args[i:i + 2]
    outjson = None
    if "-o" in args:
        i = args.index("-o"); outjson = args[i + 1]; del args[i:i + 2]
    sol = os.path.abspath(args[0])
    cases = args[1:]
    with ThreadPoolExecutor(jobs) as ex:
        res = list(ex.map(lambda c: run_case(sol, c), cases))
    tot = 0; bad = 0; mx = 0
    for r in res:
        ok = r["profit"] is not None and "对账错误 0/" in r["msg"] and "非法指令 0，" in r["msg"] and r["st"] == 0
        if verbose or not ok:
            print(f'{r["case"]:>14} cpu={r["cpu"]:.3f} st={r["st"]} {r["msg"][:300]}')
        if r["profit"] is not None:
            tot += r["profit"]
        if not ok:
            bad += 1
        mx = max(mx, r["cpu"])
    print(f"TOTAL profit={tot} cases={len(res)} bad={bad} maxcpu={mx:.3f}")
    if outjson:
        json.dump(res, open(outjson, "w"))


if __name__ == "__main__":
    main()
