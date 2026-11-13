---
source: BIOS-Obsidian/tools/scripts/sheet.py
handouts: []
saved: 2026-11-13
tags: [bios, code]
---
# sheet.py

Side-by-side image of chosen booklet pages: sheet.py <folder> out.png 3,4,5.

```python
import sys, glob
from PIL import Image
d, out, pages = sys.argv[1], sys.argv[2], [int(x) for x in sys.argv[3].split(",")]
ims = [Image.open(f"{d}/.build/booklet-pages/p{n:02d}.png").convert("RGB") for n in pages]
w, h = ims[0].size; s = 0.36
W, Hh = int(w*s), int(h*s)
o = Image.new("RGB", (W*len(ims), Hh), "white")
for i, im in enumerate(ims): o.paste(im.resize((W, Hh)), (i*W, 0))
o.save(out)

```
