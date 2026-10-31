---
source: BIOS-Obsidian/tools/scripts/hem3/common.py
handouts: []
saved: 2026-10-31
tags: [bios, code]
---
# hem3/common.py

Base helpers used by c.py.

```python
import json, os
from collections import Counter
def C(en, ar, **k): return dict(t="card", en=en, ar=ar, **k)
def R(en, ar): return dict(t="rule", en=en, ar=ar)
def SEC(en, ar): return dict(t="section", en=en, ar=ar)
def H2(en, ar): return dict(t="h2", en=en, ar=ar)
def L(en_items, ar_items, en="", ar="", **k): return dict(t="card", en=en, ar=ar, list_en=en_items, list_ar=ar_items, **k)
def N(en, ar, label=None):
    b = dict(t="note", en=en, ar=ar)
    if label: b["label"] = label
    return b
def FLOW(pairs, **k): return dict(t="flow", steps=[{"en": e, "ar": a} for e, a in pairs], **k)
def T(head, rows, **k): return dict(t="table", head=head, rows=rows, **k)
def Q(en, ar, opts, ans, **k): return dict(en=en, ar=ar, options=[list(o) for o in opts], answer=ans, **k)
def TF(en, ar, a): return dict(en=en, ar=ar, answer=a)
def TR(en, ar, ae, aa): return dict(en=en, ar=ar, answer_en=ae, answer_ar=aa)
IM = TR
def save(folder, no, title_en, title_ar, blocks, mcq, tf, traps, important):
    data = {"meta": {
        "subject_en": "Hematology", "subject_ar": "أمراض الدم", "short_ar": "امراض الدم",
        "unit_en": f"Lecture {no}", "unit_ar": f"المحاضرة {no}", "unit_label": "LEC", "unit_no": str(no),
        "title_en": title_en, "title_ar": title_ar,
        "kind": "Theory — نظري", "stage": "The third stage — الثالثة", "instructor": "د. مازن اللهيبي"},
        "blocks": blocks, "questions": {"mcq": mcq, "tf": tf, "traps": traps, "important": important}}
    qs = [q for q in mcq if "answer" in q]
    print(folder, len(qs), dict(Counter(q["answer"] for q in qs)), len(tf), len(traps), len(important))
    d = "/home/user/-/" + folder
    os.makedirs(d, exist_ok=True)
    json.dump(data, open(d + "/lecture.json", "w"), ensure_ascii=False, indent=1)
def VALUES(label=True):
    k = dict(style="summary", label_en="Normal adult red cell value", label_ar="القيم الطبيعية لكريات البالغين الحمر") if label else {}
    return T(["", "Male", "Female", "الترجمة"],
       [["Hemoglobin (Hb.) (g/dl)", "13.5-17.5", "11.5-15.5", "الهيموغلوبين (غ/دل)"],
        ["Hematocrit (pcv) (%)", "40-52", "36-48", "الهيماتوكريت (%)"],
        ["Red cell count (x10¹²/l)", "4.5- 6.5", "3.9-5.6", "عدد الكريات الحمر (×10¹²/لتر)"],
        ["MCV (fl)", "80-95", "80-95", "متوسط حجم الكرية"],
        ["MCH (pg)", "27-34", "27-34", "متوسط هيموغلوبين الكرية"],
        ["MCHC (g/dl)", "20-35", "20-35", "متوسط تركيز الهيموغلوبين"]],
       ar_cols=[3], key_cols=[0], **k)

```
