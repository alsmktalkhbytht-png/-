---
source: BIOS-Obsidian/tools/scripts/fill2.py
handouts: []
saved: 2026-11-10
tags: [bios, code]
---
# fill2.py

Utility script.

```python
"""Page-fill check on lecture pages only.
   python3 fill2.py <folder> [threshold=80]   (after bios.py has built <folder>)
Prints: <folder> <number of lecture pages> <page:fill%> for every lecture page under the threshold.
Skips the cover, the last lecture page (it ends the handout) and the merged question part
(header "· Exam"), which fill.py counted as gaps although they are natural ends."""
import sys, re, glob
from PIL import Image
folder = sys.argv[1]; th = float(sys.argv[2]) if len(sys.argv) > 2 else 80
h = open(folder + "/.build/booklet.html").read()
secs = re.findall(r'<section class="page" data-num="(\d+)">(.*?)(?=<section class="page|\Z)', h, re.S)
lec = [int(n) for n, body in secs if "· Exam" not in body[:3000]]
nlec = max(lec) if lec else 0
out = []
for f in sorted(glob.glob(folder + "/.build/booklet-pages/*.png"))[1:]:
    n = int(re.search(r"p(\d+)", f.split("/")[-1]).group(1))
    if n >= nlec: continue          # last lecture page + question pages
    im = Image.open(f).convert("L"); w, hh = im.size
    top, bot = int(hh * 0.075), int(hh * 0.90); last = top
    for y in range(bot, top, -1):
        if min(im.crop((int(w*.06), y, int(w*.93), y+1)).getdata()) < 200: last = y; break
    pct = (last - top) / (bot - top) * 100
    if pct < th: out.append(f"{n}:{pct:.0f}%")
print(folder, nlec, " ".join(out))

```
