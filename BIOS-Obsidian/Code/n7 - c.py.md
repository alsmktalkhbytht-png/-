---
source: BIOS-Obsidian/tools/scripts/n7/c.py
handouts: []
saved: 2026-10-31
tags: [bios, code]
---
# n7/c.py

Short block builders (C, R, SEC, H2, L, N, FLOW, T, Q, TF, TR, IM, F, FF, SIDE) and save().

```python
import sys; sys.path.insert(0, "/tmp/claude-0/-home-user--/8f878068-bae9-502b-96f7-788f221c7cb0/scratchpad/hem3")
from common import C, R, SEC, H2, L, N, FLOW, T, Q, TF, TR
import json, os
from collections import Counter
IM = TR
def F(src, en, ar, **k): return dict(t="figure", src="assets/" + src, en=en, ar=ar, **k)
def FF(*items): return dict(t="figures", items=[dict(src="assets/" + s, en=e, ar=a, h=h, fit="contain") for s, e, a, h in items])
def SIDE(blocks, src, en, ar): return dict(t="side", blocks=blocks, figure=dict(src="assets/" + src, en=en, ar=ar))
def Q5(en, ar, opts, ans, **k): return Q(en, ar, opts, ans, **k)
def save(folder, meta, blocks, mcq, tf, traps, important):
    qs = [q for q in mcq if "answer" in q]
    print(folder, len(qs), dict(Counter(q["answer"] for q in qs)), len(tf), len(traps), len(important))
    d = "/home/user/-/" + folder; os.makedirs(d, exist_ok=True)
    json.dump({"meta": meta, "blocks": blocks, "questions": {"mcq": mcq, "tf": tf, "traps": traps, "important": important}},
              open(d + "/lecture.json", "w"), ensure_ascii=False, indent=1)
HEM = dict(subject_en="Hematology", subject_ar="أمراض الدم", short_ar="امراض الدم", unit_label="LAB",
           kind="Laboratories — عملي", stage="The third stage — الثالثة", instructor="ليندا منجد هادي")

```
