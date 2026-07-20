# -*- coding: utf-8 -*-
"""Audit: list every multiple-choice sub-question in the source PDFs and report
which ones are not represented in the concept deck."""
import fitz, re, sys, io, importlib.util, difflib

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
D = "C:/Users/furga/Downloads/"
FILES = [
    ("Bonus test 1 (paper)", "assignment 1.pdf"),
    ("Bonus test 2 (paper)", "assignment 2 (1).pdf"),
    ("Bonus Test 1 (sol)", "solutions/test 1.pdf"),
    ("Bonus Test 2 (sol)", "solutions/test 2.pdf"),
    ("Bonus Test 3 (sol)", "solutions/test 3.pdf"),
    ("Bonus Test 4 (sol)", "solutions/test 4.pdf"),
    ("Final Exam", "Final Exam Paper.pdf"),
    ("Short test 5", "short_test_5_reconstruction.pdf"),
]

# option tokens that mark a line as belonging to a multiple-choice box
OPTBITS = re.compile(
    r"^(True|False|Yes|No|D&C|DP|Greedy|Divide|Incremental|Other|Preorder|Postorder|Inorder|"
    r"None of the|MergeSort|HeapSort|InsertionSort|BubbleSort|Case \d|<|>|\?|Θ\(|O\(|≥|"
    r"2h|2n|n$|⌊)"
)
SUB = re.compile(r"^([a-r])\)\s*(.*)$")
PROB = re.compile(r"^Problem\s+(\d+)")


def items(path):
    doc = fitz.open(path)
    lines = []
    for pi in range(len(doc)):
        for ln in doc[pi].get_text().split("\n"):
            lines.append(ln.strip())
    out, prob, cur = [], None, None
    for i, ln in enumerate(lines):
        m = PROB.match(ln)
        if m:
            prob = m.group(1)
            continue
        m = SUB.match(ln)
        if m:
            if cur:
                out.append(cur)
            cur = [prob, m.group(1), m.group(2), 0]
            continue
        if cur:
            if OPTBITS.match(ln):
                cur[3] += 1
            elif len(cur[2]) < 220 and ln and not ln.startswith(("–", "CIT-", "250", "Page", "✂")):
                cur[2] += " " + ln
    if cur:
        out.append(cur)
    return [o for o in out if o[3] >= 2]        # >=2 option boxes -> multiple choice


def norm(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return " ".join(s.split())


spec = importlib.util.spec_from_file_location("g", "_gen_concepts.py")
g = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)
deck = []
for name, opts, its in g.T:
    for (q, a, why, src, ov, fig) in its:
        deck.append((norm(q), src, q))
decknorm = [d[0] for d in deck]

missing = []
for label, f in FILES:
    print("\n########## %s  (%s)" % (label, f))
    for prob, sub, text, nb in items(D + f):
        t = norm(text)[:150]
        best = difflib.get_close_matches(t, decknorm, n=1, cutoff=0.62)
        # also accept substring containment either way
        hit = bool(best)
        if not hit and t:
            for dn in decknorm:
                if len(t) > 25 and (t[:60] in dn or dn[:60] in t):
                    hit = True
                    break
        flag = "   " if hit else ">>>"
        print("%s P%s%s [%d] %s" % (flag, prob, sub, nb, text[:130]))
        if not hit:
            missing.append((label, "P%s%s" % (prob, sub), text[:160]))

print("\n\n===== NOT FOUND IN DECK (%d) =====" % len(missing))
for m in missing:
    print("%-22s %-6s %s" % m)
