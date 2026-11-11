---
source: BIOS-Obsidian/tools/scripts/nur/common_nur.py
handouts: []
saved: 2026-11-11
tags: [bios, code]
---
# nur/common_nur.py

Pediatric nursing meta NUR(), BN() BIOS note, chunk_lists() (old; replaced by flowfit).

```python
import sys; sys.path.insert(0, "/tmp/claude-0/-home-user--/67d83c9a-7b0e-5ae5-b52b-cd659ab074ab/scratchpad/imm456")
from ci import *            # c helpers + B INSHORT TERMS balance save(split.fix)

ORD = {1: "الأولى", 2: "الثانية", 3: "الثالثة", 4: "الرابعة"}
def NUR(no, title_en, title_ar):
    return dict(subject_en="Pediatric Nursing", subject_ar="تمريض الأطفال", short_ar="تمريض أطفال", unit_label="LEC",
                kind="Theory — نظري", stage="The third stage — الثالثة", department="كلية التمريض",
                unit_en=f"Lecture {no}", unit_ar=f"المحاضرة {no}", unit_no=str(no), title_en=title_en, title_ar=title_ar)
BN = lambda en, ar: N(en, ar, label=["BIOS note", "ملاحظة BIOS"])

def chunk_lists(blocks, size=8, budget=10):
    """Split long point lists into several cards so no card is taller than a page.
    A card holds at most `size` points and about `budget` sentences."""
    import re
    def weight(x):
        return max(1, len(re.findall(r"[.!?](\s|$)", x))) + len(x) // 260
    out = []
    for b in blocks:
        le, la = b.get("list_en"), b.get("list_ar")
        if b.get("t") == "card" and le:
            groups, cur, w = [], [], 0
            for i, x in enumerate(le):
                if cur and (len(cur) >= size or w + weight(x) > budget):
                    groups.append(cur); cur, w = [], 0
                cur.append(i); w += weight(x)
            groups.append(cur)
            if len(groups) == 1:
                out.append(b); continue
            for g in groups:
                i0 = g[0]
                nb = dict(b, list_en=[le[i] for i in g], list_ar=[la[i] for i in g], start=b.get("start", 1) + i0)
                if i0:
                    e, a_ = b.get("en", ""), b.get("ar", "")
                    nb["en"] = e.rstrip(":* ") + " (continued)**" if e.startswith("**") else e
                    nb["ar"] = a_.rstrip(":* ") + " (تكملة)**" if a_.startswith("**") else a_
                out.append(nb)
        else:
            out.append(b)
    return out

```
