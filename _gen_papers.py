# -*- coding: utf-8 -*-
"""Crop open-ended (non multiple-choice) problems from Short test 5, the Final
Exam and the Retake into card images.

  Retake  : scanned + solved -> front = colour-stripped (question only), back = full solution
  Final   : question paper only            -> single-face question card
  Test 5  : reconstruction (Q + source notes) -> single-face card
"""
import fitz, os, glob
import numpy as np
from PIL import Image

SRC = "C:/Users/furga/Downloads"
OUT = "C:/Users/furga/Downloads/exam-trainer/img"
os.makedirs(OUT, exist_ok=True)
for f in glob.glob(OUT + "/p[567]-*.png"):
    os.remove(f)

X0, X1, TOP, BOT = 40, 560, 38, 800


def strip_ink(img):
    """Whiten every non-grey pixel: printed question text is black/grey,
    the solution ink and the watermark are blue."""
    a = np.array(img).astype(int)
    spread = a.max(axis=2) - a.min(axis=2)
    a[spread > 18] = [255, 255, 255]
    return Image.fromarray(a.astype("uint8"))


def page_img(doc, pg, zoom):
    px = doc[pg - 1].get_pixmap(matrix=fitz.Matrix(zoom, zoom))
    return Image.frombytes("RGB", [px.width, px.height], px.samples)


def content_bottom(doc, pg, top, bot):
    m = top
    for b in doc[pg - 1].get_text("dict")["blocks"]:
        for l in b.get("lines", []):
            if top <= l["bbox"][3] <= bot:
                m = max(m, l["bbox"][3])
    for d in doc[pg - 1].get_drawings():
        r = d["rect"]
        if top <= r.y1 <= bot and 3 < (r.x1 - r.x0) < 430:
            m = max(m, r.y1)
    return m


def crop_text_pdf(doc, segs, zoom=2.3, trim=True):
    """segs = [(startPage, y0, endPage, y1)] in PDF points, stitched vertically."""
    sl = []
    for (sp, sy, ep, ey) in segs:
        for pg in range(sp, ep + 1):
            top = sy if pg == sp else TOP
            bot = ey if pg == ep else BOT
            if trim and pg == ep:
                bot = min(bot, content_bottom(doc, pg, top, bot) + 16)
            if bot - top < 6:
                continue
            im = page_img(doc, pg, zoom)
            sl.append(im.crop((int(X0 * zoom), int(top * zoom), int(X1 * zoom), int(bot * zoom))))
    if not sl:
        return None
    W = max(s.width for s in sl); H = sum(s.height for s in sl) + (len(sl) - 1) * 6
    out = Image.new("RGB", (W, H), "white"); y = 0
    for s in sl:
        out.paste(s, (0, y)); y += s.height + 6
    return out


# ---------------------------------------------------------------- Retake (scanned)
# no text layer -> regions given as (page, y0, y1) in *rendered* pixels at zoom 2.6
RZ = 2.6
RETAKE = [
    ("2",  3,  120, 1290, "Recurrence Relations"),
    ("3",  3, 1290, 2400, "Mystery Algorithm"),
    ("5",  4, 1230, 2400, "Identifying Graph Properties"),
    ("6",  5,  120, 1540, "PageRank Algorithm"),
    ("7",  5, 1540, 2400, "DFS Theorem"),
    ("8",  6,  120, 2400, "Kruskal's and Bellman-Ford"),
    ("11", 9,  120, 1690, "Strongly Connected Components"),
    ("12", 9, 1730, 2400, "Hash Tables"),
    ("13", 10, 120, 2400, "Rotations and Binary Search Trees"),
    ("14", 11, 120, 2400, "Room Scheduling for Profit"),
]

rdoc = fitz.open(f"{SRC}/Retake_Exam_Oct2025_Solutions.pdf")
made = []
for prob, pg, y0, y1, title in RETAKE:
    full = page_img(rdoc, pg, RZ).crop((int(X0 * RZ), y0, int(X1 * RZ), y1))
    q = strip_ink(full)
    full.save(f"{OUT}/p7-p{prob}-a.png")
    q.save(f"{OUT}/p7-p{prob}-q.png")
    made.append(("retake", prob, title, full.size))

# ---------------------------------------------------------------- Final Exam (questions only)
fdoc = fitz.open(f"{SRC}/Final Exam Paper.pdf")
FHEAD = []
for pi in range(len(fdoc)):
    for b in fdoc[pi].get_text("dict")["blocks"]:
        for l in b.get("lines", []):
            t = "".join(s["text"] for s in l["spans"]).strip()
            if t.startswith("Problem ") and len(t) < 18:
                FHEAD.append((int(t.split()[1]), pi + 1, l["spans"][0]["bbox"][1]))
FHEAD.sort(key=lambda x: (x[1], x[2]))
FINAL_OPEN = {1: "Complexity of Pseudocode", 2: "Recurrences", 3: "Sorting", 4: "Heaps",
              5: "Greedy", 6: "Dynamic Programming", 8: "Identifying Graph Properties",
              9: "PageRank Algorithm", 11: "Graph Algorithms", 12: "Hashing",
              14: "Topological Sort"}
for i, (p, pg, y) in enumerate(FHEAD):
    if p not in FINAL_OPEN:
        continue
    ep, ey = (FHEAD[i + 1][1], FHEAD[i + 1][2]) if i + 1 < len(FHEAD) else (len(fdoc), 900)
    im = crop_text_pdf(fdoc, [(pg, y, min(ep, len(fdoc)), ey)])
    if im:
        im.save(f"{OUT}/p6-p{p}-q.png")
        made.append(("final", p, FINAL_OPEN[p], im.size))

# ---------------------------------------------------------------- Short test 5 (reconstruction)
sdoc = fitz.open(f"{SRC}/short_test_5_reconstruction.pdf")
import re
SHEAD = []
pat = re.compile(r"^Problems?\s+(\d+)")
for pi in range(len(sdoc)):
    for b in sdoc[pi].get_text("dict")["blocks"]:
        for l in b.get("lines", []):
            t = "".join(s["text"] for s in l["spans"]).strip()
            m = pat.match(t)
            if m:
                SHEAD.append((int(m.group(1)), pi + 1, l["spans"][0]["bbox"][1], t))
# first occurrence of each number, in page order; every heading acts as a boundary
seen, S = set(), []
SHEAD.sort(key=lambda x: (x[1], x[2]))
for n, pg, y, t in SHEAD:
    if n not in seen:
        seen.add(n); S.append((n, pg, y, t))
for i, (n, pg, y, t) in enumerate(S):
    if n > 7:          # 8-9 are the MCQ/True-False block, already in the MC deck
        continue
    ep, ey = (S[i + 1][1], S[i + 1][2]) if i + 1 < len(S) else (len(sdoc), 900)
    im = crop_text_pdf(sdoc, [(pg, y, min(ep, len(sdoc)), ey)])
    if im:
        im.save(f"{OUT}/p5-p{n}-q.png")
        made.append(("test5", n, t[:52], im.size))

for m in made:
    print(m)
print("total images:", len(made))
