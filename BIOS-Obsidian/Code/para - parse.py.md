---
source: BIOS-Obsidian/tools/scripts/para/parse.py
handouts: []
saved: 2026-10-29
tags: [bios, code]
---
# para/parse.py

PDF → paragraphs with ⟦bold⟧ and __italic__ markers (pdfplumber).

```python
import pdfplumber, re, json, sys
pdf = pdfplumber.open('src/mcq.pdf')
paras = []
for pi, p in enumerate(pdf.pages):
    ws = p.extract_words(extra_attrs=["fontname", "size"], keep_blank_chars=False, use_text_flow=True)
    lines = []
    for w in ws:
        if w['size'] < 9 and lines and abs(w['top'] - lines[-1]['top']) < 6:   # superscripts (st, th)
            lines[-1]['words'].append(w); continue
        if lines and abs(w['top'] - lines[-1]['top']) < 4:
            lines[-1]['words'].append(w)
        else:
            lines.append({'top': w['top'], 'bottom': w['bottom'], 'words': [w]})
    prev = None
    for ln in lines:
        if prev is None or ln['top'] - prev['bottom'] > 6.5:
            paras.append({'page': pi + 1, 'words': []})
        paras[-1]['words'] += ln['words']; prev = ln
def render(words):
    out = []; cur = None
    for w in words:
        f = w['fontname']; kind = 'b' if 'Bold' in f else ('i' if 'Italic' in f else 'n')
        out.append((kind, w['text']))
    s = ""; last = None
    for kind, t in out:
        if kind != last:
            if last == 'b': s = s.rstrip() + "⟧ "
            if last == 'i': s = s.rstrip() + "__ "
            if kind == 'b': s += "⟦"
            if kind == 'i': s += "__"
        s += t + " "; last = kind
    if last == 'b': s = s.rstrip() + "⟧"
    if last == 'i': s = s.rstrip() + "__"
    return re.sub(r"\s+", " ", s).strip()
res = []
for p in paras:
    t = render(p['words'])
    if t.startswith('Diagnostic Parasitology MCQ') or set(t) <= set('- '): continue
    res.append({'page': p['page'], 'text': t})
json.dump(res, open('paras.json', 'w'), ensure_ascii=False, indent=0)
print(len(res))

```
