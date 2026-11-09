---
source: BIOS-Obsidian/tools/scripts/bidi.py
handouts: []
saved: 2026-11-09
tags: [bios, code]
---
# bidi.py

ltr_all(obj): wraps Latin runs and formulas (TT × tt, 3 : 1) inside Arabic strings in backticks so they are not reversed.

```python
"""bidi — keep Latin runs and formulas the right way round inside Arabic text.

    from bidi import ltr_all
    blocks = ltr_all(blocks); mcq = ltr_all(mcq); ...      # before save()

Inside an Arabic (RTL) line, "TT × tt", "1 RR : 2 Rr : 1 rr", "P: BBRR × bbrr" or "3 : 1" get their parts
reversed by the browser. ltr_all() wraps every such run in `backticks` (the engine's LTR run) in all
Arabic strings: "ar", "answer_ar", "list_ar", the Arabic half of ["en", "ar"] table cells and options.
Runs already inside backticks are left alone. Plain single numbers are not wrapped.
"""
import re

_SUP = "⁰¹²³⁴⁵⁶⁷⁸⁹⁻"                                 # powers of ten: 10⁵, 10⁻³ must stay LTR too
_RUN = re.compile(r"[A-Za-z0-9½¼¾(][A-Za-z0-9½¼¾%s ×:/=+_.()%%,'-]*[A-Za-z0-9½¼¾%s)%%]|[A-Za-z]" % (_SUP, _SUP))
_NEEDS = re.compile(r"[A-Za-z×=:/%s]" % _SUP)


def _wrap(seg):
    def rep(m):
        s = m.group(0)
        if s.count("(") != s.count(")"):                # do not cut a bracket in half
            s2 = s.strip("()")
            if not s2:
                return s
            i = s.index(s2)
            return s[:i] + (f"`{s2}`" if _NEEDS.search(s2) else s2) + s[i + len(s2):]
        return f"`{s}`" if _NEEDS.search(s) else s
    return _RUN.sub(rep, seg)


def ltr(s):
    if not isinstance(s, str):
        return s
    if not re.search(r"[؀-ۿ]", s):                    # Arabic side with no Arabic letters ("1 TT : 2 Tt", "½ T + ½ t", "3 : 1"):
        if "`" not in s and re.search(r"\S\s+\S|[×=:/+½¼¾]", s):   # an RTL paragraph would move the leading number to the end
            return f"`{s}`"
        return s
    parts = s.split("`")
    return "`".join(p if i % 2 else _wrap(p) for i, p in enumerate(parts))


def _pair(x):
    return isinstance(x, list) and len(x) == 2 and all(isinstance(y, str) for y in x)


def ltr_all(obj):
    if isinstance(obj, list):
        if _pair(obj):
            return [obj[0], ltr(obj[1])]
        return [ltr_all(x) for x in obj]
    if isinstance(obj, dict):
        out = {}
        for k, v in obj.items():
            if k == "label" or k.endswith("en"):         # labels and English fields are never wrapped
                out[k] = v                               # (a 2-sentence English list is not an [en, ar] pair)
            elif k in ("ar", "answer_ar", "title_ar", "label_ar", "text_ar", "tail_ar", "sub_ar"):
                out[k] = [ltr(x) for x in v] if isinstance(v, list) else ltr(v)
            elif k == "list_ar":
                out[k] = [[ltr(y) for y in x] if isinstance(x, list) else ltr(x) for x in v]
            else:
                out[k] = ltr_all(v)
        return out
    return obj


if __name__ == "__main__":
    for t in ["P: **TT × tt** ← أمشاج T وt ← الجيل F1 كله **Tt (طويل)**.", "نسبة **3 : 1** والتراكيب 1 RR : 2 Rr : 1 rr",
              "**التركيب (`Genotype`)** – شيء", "الاحتمال = **1/2 = 50%**.", "أمشاج RT وrT"]:
        print(ltr(t))

```
