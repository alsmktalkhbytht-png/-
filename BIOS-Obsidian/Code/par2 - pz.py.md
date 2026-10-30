---
source: BIOS-Obsidian/tools/scripts/par2/pz.py
handouts: []
saved: 2026-10-30
tags: [bios, code]
---
# par2/pz.py

Parasitology theory meta + SAVE() for handouts without questions.

```python
import sys, json, os
sys.path.insert(0, "/tmp/claude-0/-home-user--/8f878068-bae9-502b-96f7-788f221c7cb0/scratchpad/imm456")
from ci import C, R, SEC, H2, L, N, FLOW, T, F, FF, B, END, split
ORD = {2: "الثاني", 3: "الثالث", 4: "الرابع", 5: "الخامس"}
def META(w, title_en, title_ar):
    return {"subject_en": "Diagnostic Parasitology", "subject_ar": "الطفيليات التشخيصية", "short_ar": "طفيليات", "instructor": "أ.د. نزار الخفاجي",
            "unit_en": f"Week {w}", "unit_ar": f"الأسبوع {w}", "unit_label": "WEEK", "unit_no": str(w), "title_en": title_en, "title_ar": title_ar,
            "department": "قسم التحليلات", "stage": "The fourth stage — الرابعة", "kind": "Theory — نظري"}
def SAVE(w, meta, blocks):
    d = f"/home/user/-/parasitology-week{w}-theory"; os.makedirs(d + "/assets", exist_ok=True)
    json.dump({"meta": meta, "blocks": split.fix(blocks)}, open(d + "/lecture.json", "w"), ensure_ascii=False, indent=1)
    print(d, len(blocks))
BN = lambda en, ar: N(en, ar, label=("BIOS note", "ملاحظة BIOS"))

```
