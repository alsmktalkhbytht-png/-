---
source: BIOS-Obsidian/tools/scripts/imm456/split.py
handouts: []
saved: 2026-10-31
tags: [bios, code]
---
# imm456/split.py

Sentence splitter + checker: every English sentence must get its own Arabic sentence.

```python
"""Split every paragraph into sentences so each English sentence is followed by its own translation."""
import re

ABBR = ("e.g.", "i.e.", "vs.", "Dr.", "Fig.", "etc.", "approx.", "No.", "spp.", "St.", "incl.")
EN_CUT = re.compile(r'(?<=[.?!])(\**)\s+(?=[A-Z(\[“"*0-9])')
AR_CUT = re.compile(r'(?<=[.؟!])(\**)\s+(?=\S)')


def _cut(s, rx, abbr=()):
    parts, last = [], 0
    for m in rx.finditer(s):
        left = s[last:m.start() + len(m.group(1))]
        tail = left.rstrip("*").strip()
        if re.fullmatch(r"\**\(?(\d{1,2}|[A-Za-z\u0621-\u064A])[.)]", tail.split(" ")[-1]):
            continue                                   # "**1." numbering, not a sentence end
        if tail.endswith(abbr):
            continue
        if re.fullmatch(r"\*\*[^*]{1,25}[.؟]\*\*", left.strip()):
            continue                                   # "**Age.**" run-in label stays with its sentence
        if left.count("**") % 2:                       # never split inside a bold run
            continue
        parts.append(left.strip()); last = m.end()
    parts.append(s[last:].strip())
    return [p for p in parts if p]


def en_sents(s): return _cut(s, EN_CUT, ABBR)
def ar_sents(s): return _cut(s, AR_CUT)


BAD = []


def sp(e, a, where=""):
    if isinstance(e, list) and isinstance(a, list) and len(e) == len(a) and all(e):
        E, A = [], []
        for x, y in zip(e, a):                     # split every sentence-list item further
            x, y = sp(x, y, x[:50])
            E += x if isinstance(x, list) else [x]; A += y if isinstance(y, list) else [y]
        return E, A
    if isinstance(e, list) or not e or not a:
        return e, a
    E, A = en_sents(e), ar_sents(a)
    if len(E) == 1:
        return e, a
    if len(E) != len(A):
        BAD.append((where, E, A))
        return e, a
    return E, A


def walk(blocks):
    for b in blocks:
        t = b.get("t")
        if t in ("card", "rule", "note", "group"):
            b["en"], b["ar"] = sp(b.get("en"), b.get("ar"), (b.get("en") or "")[:50])
            if b.get("list_en"):
                for i, (e, a) in enumerate(zip(b["list_en"], b["list_ar"])):
                    b["list_en"][i], b["list_ar"][i] = sp(e, a, e[:50])
        elif t == "side":
            walk(b["blocks"])


def fix(blocks):
    walk(blocks)
    if BAD:
        for w, E, A in BAD:
            print(f"\n## {w}\n  EN {len(E)}: " + "\n      ".join(E) + f"\n  AR {len(A)}: " + "\n      ".join(A))
        raise SystemExit(f"{len(BAD)} paragraphs need matching sentences")
    return blocks

```
