---
source: BIOS-Obsidian/tools/scripts/imm456/ci.py
handouts: []
saved: 2026-10-30
tags: [bios, code]
---
# imm456/ci.py

Clinical-immunology meta, B() bilingual cell, END() summary+glossary, INSHORT() per-topic box, TERMS() glossary, save() with split.fix.

```python
import sys; sys.path.insert(0, "/tmp/claude-0/-home-user--/8f878068-bae9-502b-96f7-788f221c7cb0/scratchpad/n7")
sys.path.insert(0, "/tmp/claude-0/-home-user--/8f878068-bae9-502b-96f7-788f221c7cb0/scratchpad/bac")
from c import *
from bal import balance

CI = dict(subject_en="Clinical Immunology", subject_ar="المناعة السريرية", short_ar="مناعة سريرية", unit_label="LEC",
          kind="Theory — نظري", stage="The fourth stage — الرابعة", instructor="د. عبير")
P = lambda *o: [(x, y) for x, y in o]
import split
_save = save
def save(folder, meta, blocks, *rest):
    return _save(folder, meta, split.fix(blocks), *rest)
B = lambda e, a: [e, a]                       # bilingual table cell
def END(points, terms, points_more=None):
    """Closing summary (key points) + key-terms glossary with several Arabic renderings each."""
    out = [SEC("Quick summary & key terms", "الخلاصة السريعة وأهم المصطلحات"),
           H2("In short", "باختصار"),
           *[L([p[0] for p in points[i:i + 4]], [p[1] for p in points[i:i + 4]]) for i in range(0, len(points), 4)]]
    out += [H2("Key terms — more than one translation", "أهم المصطلحات — بأكثر من ترجمة"),
            T([B("Term", "المصطلح"), "الترجمات العربية المستعملة"],
              [[f"**{e}**", a] for e, a in terms], ar_cols=[1], widths=[36, 64])]
    return out
def INSHORT(points, en="In short", ar="باختصار"):
    """Per-topic summary box placed at the end of each section (team rule)."""
    return N([p[0] for p in points], [p[1] for p in points], label=(en, ar))
def TERMS(terms):
    """Closing key-terms glossary only (team rule: no whole-lecture summary at the end)."""
    return [SEC("Key terms", "أهم المصطلحات"),
            T([B("Term", "المصطلح"), "الترجمات العربية المستعملة"], [[f"**{e}**", a] for e, a in terms], ar_cols=[1], widths=[36, 64])]

```
