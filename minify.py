#!/usr/bin/env python3
"""Turn the readable sol.cpp into the submission file (< 16384 bytes, ASCII, LF).

Only mechanical transformations are applied, so both files behave identically:
  1. drop the `#ifdef DBG` diagnostics,
  2. replace the tunables `PRM(NAME, value)` by their literal values,
  3. drop comments and unnecessary white space,
  4. rename the program's own identifiers to short names.

usage: python3 minify.py sol.cpp submit.cpp            smallest file (steps 1-4)
       python3 minify.py sol.cpp submit.cpp --names    keep the identifiers (steps 1-3)
       python3 minify.py sol.cpp main.cpp --clean      readable file: step 1 only
"""
import re
import sys
from collections import Counter

LIMIT = 16384
src = open(sys.argv[1]).read()
MODE = sys.argv[3] if len(sys.argv) > 3 else ""

# ---- 1. preprocessor: keep the non-DBG branch -------------------------------------------
out, stack = [], []
for line in src.split("\n"):
    t = line.strip()
    if t.startswith("#ifdef"):
        stack.append(t.split()[1] != "DBG")
    elif t.startswith("#ifndef"):
        stack.append(t.split()[1] == "DBG")
    elif t.startswith("#else"):
        stack[-1] = not stack[-1]
    elif t.startswith("#endif"):
        stack.pop()
    elif all(stack):
        out.append(line)
assert not stack
src = "\n".join(out)
if MODE == "--clean":
    src = re.sub(r"\n{3,}", "\n\n", src)
    assert all(ord(c) < 128 for c in src)
    open(sys.argv[2], "w", newline="\n").write(src)
    print(f"{sys.argv[2]}: {len(src.encode())} bytes (readable version without diagnostics)")
    sys.exit()

# ---- 2. tunables --------------------------------------------------------------------------
prm = {}
def grab(m):
    prm[m.group(1)] = m.group(2).strip()
    return ""
src = re.sub(r"^#define PRM\(.*$", "", src, flags=re.M)
src = re.sub(r"^PRM\((\w+),\s*([^)]+)\);", grab, src, flags=re.M)

# ---- 3. tokenise ----------------------------------------------------------------------------
TOKEN = re.compile(r"""
    (?P<comment>//[^\n]*|/\*.*?\*/)
  | (?P<pp>^[ \t]*\#[^\n]*)
  | (?P<str>"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*')
  | (?P<num>(?:0[xX][0-9a-fA-F]+|\d+\.?\d*(?:[eE][-+]?\d+)?|\.\d+(?:[eE][-+]?\d+)?)[uUlLfF]*)
  | (?P<id>[A-Za-z_]\w*)
  | (?P<ws>\s+)
  | (?P<op><<=|>>=|->|\+\+|--|<<|>>|<=|>=|==|!=|&&|\|\||[-+*/%&|^]=|::|.)
""", re.X | re.M | re.S)

def tokens(text):
    res = []
    for m in TOKEN.finditer(text):
        k = m.lastgroup
        if k in ("comment", "ws"):
            continue
        res.append((k, m.group()))
    return res

KEEP = set("""
alignas auto bool break case char const continue default do double else enum false float for if
int long namespace new operator return short signed sizeof static struct switch true typedef
unsigned using void while define include std main
vector pair string map set first second size begin end clear insert erase push_back pop_back back
front resize assign data empty sort lower_bound upper_bound make_pair max min swap abs to_string
fwrite fflush stdout stdin read memset memcpy clock CLOCKS_PER_SEC log exp sqrt pow floor ceil
reserve find count fill reverse unique atoll atoi array unordered_map
""".split())

toks = []
for k, v in tokens(src):
    if k == "pp":
        if v.strip().startswith("#include"):
            toks.append(("pp", v.strip()))
        else:  # a #define: tokenise its body so that names inside are renamed too
            body = v.strip()[1:]
            toks.append(("ppstart", "#"))
            toks.extend(tokens(body))
            toks.append(("ppend", ""))
    else:
        toks.append((k, v))

# inline tunables
def literal(name):
    v = prm[name]
    f = float(v)
    s = repr(int(f)) + "." if f == int(f) and abs(f) < 1e6 else v
    if s.startswith("0.") and len(s) > 2:
        s = s[1:]
    return s
toks = [("num", literal(v)) if k == "id" and v in prm else (k, v) for k, v in toks]

# ---- 4. rename --------------------------------------------------------------------------------
freq = Counter(v for k, v in toks if k == "id" and v not in KEEP)
def names():
    a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for c in a:
        yield c
    for c in a:
        for d in a + "0123456789":
            yield c + d
gen, ren = names(), {}
for name, _ in freq.most_common() if MODE != "--names" else []:
    n = next(gen)
    while n in KEEP or n in ("do", "if", "or"):
        n = next(gen)
    ren[name] = n
toks = [(k, ren.get(v, v)) if k == "id" else (k, v) for k, v in toks]

# ---- 5. emit ----------------------------------------------------------------------------------
res, line, prev = [], "", None
def wordy(t):
    return t and (t[0] in ("id", "num"))
def flush():
    global line
    if line:
        res.append(line)
    line = ""
i = 0
in_pp = False
for k, v in toks:
    if k == "pp":
        flush(); res.append(v); prev = None
        continue
    if k == "ppstart":
        flush(); line = "#"; prev = None; in_pp = True; pp_count = 0
        continue
    if k == "ppend":
        flush(); prev = None; in_pp = False
        continue
    sep = ""
    if prev:
        if wordy(prev) and wordy((k, v)):
            sep = " "
        elif prev[0] == "op" and k == "op" and (prev[1] + v) in ("++", "--", "+++", "---", "<<", ">>", "&&", "||", "->", "//", "/*", "::", "<:", "<%", "%:", "%>", ":>") :
            sep = " "
        elif prev[0] == "op" and k == "op" and prev[1] in "+-&<>" and v[0] == prev[1][-1]:
            sep = " "
        elif prev[0] == "num" and k == "op" and v[0] == "." or prev[0] == "op" and prev[1] == "." and k == "num":
            sep = " "
    if in_pp:
        pp_count += 1
        # "#define NAME(args) body" / "#define NAME body": keep one blank after the macro head
        if pp_count == 3 and v != "(":
            sep = " "
        if pp_count > 3 and pp_close:
            sep = " "
        pp_close = False
        if pp_count > 2 and v == ")" and pp_depth == 1 and not pp_done:
            pp_close = pp_done = True
        if pp_count == 1:
            pp_depth, pp_done, pp_close = 0, False, False
        if pp_count == 3 and v != "(":
            pp_done = True
        if v == "(":
            pp_depth += 1
        elif v == ")":
            pp_depth -= 1
    # keep lines reasonably short: break after ; { } outside of macros
    line += sep + v
    if not in_pp and k == "op" and v in ";{}" and len(line) > 150:
        flush(); prev = None
        continue
    prev = (k, v)
flush()
text = "\n".join(res) + "\n"
assert all(ord(c) < 128 for c in text) and "\r" not in text
open(sys.argv[2], "w", newline="\n").write(text)
print(f"{sys.argv[2]}: {len(text.encode())} bytes ({'OK' if len(text.encode()) < LIMIT else 'TOO BIG'}, limit {LIMIT}), {len(ren)} identifiers renamed")
