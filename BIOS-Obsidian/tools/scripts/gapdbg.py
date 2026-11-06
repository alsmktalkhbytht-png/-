"""python3 gapdbg.py <folder>/lecture.json — for each booklet page < 80% full, show what pushed to next page."""
import sys, re, json, html as H
sys.path.insert(0, "/home/user/-/bios-engine")
import bios
orig = bios.paginate
def pag(items, html_path, sub, forced):
    pages = orig(items, html_path, sub, forced)
    Hm = json.loads(bios.node("measure", html_path))
    idx = 0
    for p, pg in enumerate(pages, 1):
        used = sum(Hm[str(idx + k)] for k in range(len(pg)))
        idx += len(pg)
        if idx < len(items) and used / bios.BODY_MM < .8:
            # chain of next
            j, need = idx, 0
            while True:
                need += Hm[str(j)]
                if not items[j][1] or j + 1 >= len(items): break
                j += 1
            txt = re.sub(r"<[^>]+>", " ", items[idx][0]); txt = re.sub(r"\s+", " ", H.unescape(txt))[:70]
            print(f"p{p+1 if False else p}: {used/bios.BODY_MM*100:.0f}%  next#{idx} needs {need:.0f}mm (free {bios.BODY_MM-used:.0f})  {txt}")
    return pages
bios.paginate = pag
bios.build(sys.argv[1], html_only=True)
