---
source: BIOS-Obsidian/tools/scripts/fill.py
handouts: []
saved: 2026-10-31
tags: [bios, code]
---
# fill.py

Utility script.

```python
"""Report how full each page is (last content row above the footer)."""
import sys, glob
from PIL import Image
for f in sorted(glob.glob(sys.argv[1] + "/*.png"))[1:]:
    im = Image.open(f).convert("L"); w, h = im.size
    top, bot = int(h * 0.075), int(h * 0.90)          # body area between header and footer
    last = top
    for y in range(bot, top, -1):
        row = im.crop((int(w * 0.06), y, int(w * 0.93), y + 1))
        if min(row.getdata()) < 200: last = y; break
    pct = (last - top) / (bot - top) * 100
    print(f.split("/")[-1], f"{pct:5.1f}%", "  <-- gap" if pct < 82 else "")

```
