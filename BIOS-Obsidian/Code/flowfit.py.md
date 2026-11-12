---
source: BIOS-Obsidian/tools/scripts/flowfit.py
handouts: []
saved: 2026-11-12
tags: [bios, code]
---
# flowfit.py

Page filler: cuts tall cards/notes/tables at the best piece boundary (measured by the engine) so no page keeps a big gap. fit(folder) after save().

```python
"""flowfit — fill the pages of a BIOS handout without big gaps (rule of 2026-10-31: every page >= 80%).

    python3 flowfit.py <folder> [<folder> …]     # rewrites <folder>/lecture.json; then build with bios.py
    from flowfit import fit; fit("<folder>")     # same, at the end of a generator after save()

Why: the engine never splits a block, so a tall card / note / table that does not fit the space
left on a page jumps whole to the next page and leaves a gap.
How: it runs the engine's own pagination (same measurements, same keep-with-next rules). When a
splittable block would leave a gap bigger than MIN_GAP, the block is cut at the largest piece
boundary whose first part (measured in Chromium) still fits the page; the rest goes on. A block
taller than a page is cut the same way. Repeats until nothing changes.
Pieces: a sentence of a card/note, a point of a card list, a row of a table. A card's heading
stays with its first point. The second part is a list-only card that keeps counting (start=…),
a table with its header again, or a note / summary table labelled "(continued) — (تكملة)".
Figures, sections, rules, flows and one-piece cards are never cut.
Running it again is safe: the parts it made carry "_ff" and are joined back first.
"""
import copy, json, os, sys

ENGINE = "/home/user/-/bios-engine"
sys.path.insert(0, ENGINE)
import bios  # noqa: E402

CONT = (" (continued)", " (تكملة)")
MIN_GAP = 0.12            # split only when the gap would be larger than this share of the page


# ------------------------------------------------------------------ pieces of one block
def _sent(b):
    e, a = b.get("en"), b.get("ar")
    if isinstance(e, list) and e:
        return len(e)
    if isinstance(a, list) and a and not e:
        return len(a)
    return 1 if (e or a) else 0


def pieces(b):
    """piece keys of block b: [[('s', i)], [('l', i)], [('r', i)] …] — None if it cannot be cut."""
    t = b["t"]
    if t == "card":
        ns, nl = _sent(b), len(b.get("list_en") or [])
        keys = [[("s", i)] for i in range(ns)] + [[("l", i)] for i in range(nl)]
        if ns and nl:                                   # the heading never ends a page alone
            keys[ns - 1:ns + 1] = [keys[ns - 1] + keys[ns]]
    elif t == "note":
        keys = [[("s", i)] for i in range(_sent(b))]
    elif t == "table":
        keys = [[("r", i)] for i in range(len(b["rows"]))]
    else:
        return None
    return keys if len(keys) > 1 else None


def join(b, keys, first):
    """the block made of pieces `keys` of block b; first = it is the first part."""
    t = b["t"]
    S = [i for k, i in keys if k == "s"]
    L = [i for k, i in keys if k == "l"]
    R = [i for k, i in keys if k == "r"]
    nb = copy.deepcopy(b)
    if t in ("card", "note"):
        e, a = b.get("en"), b.get("ar")
        if isinstance(e, list) and e:
            nb["en"], nb["ar"] = [e[i] for i in S], [a[i] for i in S]
        elif isinstance(a, list) and a and not e:
            nb["ar"] = [a[i] for i in S]
        elif not S:
            nb["en"], nb["ar"] = "", ""
        if t == "note" and not first:
            lab = b.get("label", ("Note", "ملاحظة"))
            nb["label"] = [lab[0] + CONT[0] if lab[0] else "", lab[1] + CONT[1]]   # Arabic-only notes: no English word
    if t == "card":
        nb.pop("start", None)
        if L:
            nb["list_en"] = [b["list_en"][i] for i in L]
            nb["list_ar"] = [b["list_ar"][i] for i in L]
            st = b.get("start", 1) + L[0]
            if st != 1:
                nb["start"] = st
        else:
            for k in ("list_en", "list_ar", "alpha"):
                nb.pop(k, None)
    if t == "table":
        nb["rows"] = [b["rows"][i] for i in R]
        if not first and b.get("style") == "summary":
            nb["label_en"] = b.get("label_en", "Summary") + CONT[0] if b.get("label_en", "Summary") else ""
            nb["label_ar"] = b.get("label_ar", "خلاصة الجدول") + CONT[1]
    return nb


def cut(b, k):
    """split block b after its first k pieces → (first part, rest)."""
    ks = pieces(b)
    fid = b.get("_ff") or id(b)          # same id for every part of one block
    head = join(b, sum(ks[:k], []), b.get("_first", True))
    tail = join(b, sum(ks[k:], []), False)
    head["_ff"] = tail["_ff"] = fid
    head["_first"], tail["_first"] = b.get("_first", True), False
    head["_orig"] = tail["_orig"] = b.get("_orig", b)
    if b.get("keep"):
        head.pop("keep", None)                          # only the last part keeps with the next block
    tail["keep"] = b.get("keep", False) or None
    if tail["keep"] is None:
        tail.pop("keep")
    return head, tail


# ------------------------------------------------------------------ undo an earlier run
def unfit(blocks):
    out = []
    for b in blocks:
        if b.get("t") == "pagebreak" and b.get("auto"):
            continue
        if b.get("_ff") and out and out[-1].get("_ff") == b["_ff"]:
            p = out[-1]
            if b["t"] == "table":
                p["rows"] += b["rows"]
            else:
                for k in ("en", "ar"):
                    if isinstance(p.get(k), list) and isinstance(b.get(k), list):
                        p[k] += b[k]
                    elif not p.get(k) and b.get(k):
                        p[k] = b[k]
                if b.get("list_en"):
                    if not p.get("list_en") and b.get("start", 1) != 1 and not p.get("en") and not p.get("ar"):
                        p["start"] = b["start"]
                    p["list_en"] = (p.get("list_en") or []) + b["list_en"]
                    p["list_ar"] = (p.get("list_ar") or []) + b["list_ar"]
                    for k in ("alpha",):
                        if b.get(k):
                            p[k] = b[k]
            if b.get("keep"):
                p["keep"] = True
            continue
        out.append(copy.deepcopy(b))
    for b in out:
        b.pop("_ff", None)
    return out


# ------------------------------------------------------------------ measuring with the engine
def _measure(blocks, folder):
    """height in mm of each block, rendered by the engine exactly as in the booklet."""
    base = os.path.relpath(folder, os.path.join(folder, ".build"))
    st = {"sec": 0, "rule": 0, "grp": 0}
    htmls = []
    for b in blocks:                                    # running state: sections after the first get a top gap
        bios.FIG["n"] = 0
        htmls.append(bios.render_block(_clean(b), st, base)[0])
    probe = "".join(f'<div data-m="{i}" style="display:flow-root">{h}</div>' for i, h in enumerate(htmls))
    path = os.path.join(folder, ".build", "flowfit-measure.html")
    open(path, "w").write(bios.doc("measure", [bios.page(probe, 1, bios.M["unit_en"])]))
    H = json.loads(bios.node("measure", path))
    os.remove(path)
    return [H[str(i)] for i in range(len(blocks))]


def _clean(b):
    return {k: v for k, v in b.items() if not k.startswith("_")}


def _prepare(folder, data):
    """the engine's setup (meta, css paths) without building, so render_block/doc work."""
    path = os.path.join(folder, "lecture.json")
    bios.load(path)
    out_dir = os.path.join(folder, ".build")
    os.makedirs(out_dir, exist_ok=True)
    rel = lambda p: os.path.relpath(p, out_dir)
    third = bios.cover_stage() == "المرحلة الثالثة"
    theme = bios.M.get("theme", "blush" if third else "wineoat")
    bios.M["_css"] = rel(os.path.join(ENGINE, "style.css"))
    bios.M["_theme"] = rel(os.path.join(ENGINE, "themes", theme + ".css"))
    bios.M["_assets"] = rel(folder)


# ------------------------------------------------------------------ one pass of the engine's paging
def _pass(blocks, folder):
    """walk the pages like bios.paginate; return the blocks with at most one new cut per page."""
    title = bios.unit_title(bios.M["title_en"], bios.M["title_ar"])
    body = [b for b in blocks if b["t"] != "pagebreak"]
    hs = _measure(body, folder)
    # items as the engine sees them: title (keep) + blocks
    items, forced, bi_of = [(None, True)], set(), [None]
    for b in blocks:
        if b["t"] == "pagebreak":
            forced.add(len(items))
            continue
        items.append((b, b.get("keep", False) or b["t"] in ("section", "h2")))
        bi_of.append(b)
    H = [_measure_html(title, folder)] + hs
    plan, h_cur, cur = None, 0.0, 0
    for i, (b, keep) in enumerate(items):
        need, j = H[i], i
        while keep and j + 1 < len(items):              # heading chain + first real block
            j += 1
            need += H[j]
            if not items[j][1]:
                break
        last, heads = items[j][0], need - H[j]
        if cur and (i in forced or h_cur + need > bios.BODY_MM):
            free = bios.BODY_MM - h_cur
            if (i not in forced and last is not None and pieces(last) and free - heads > MIN_GAP * bios.BODY_MM
                    and free - heads > last.get("_minroom", 0) + 1):
                plan = (last, free - heads)
                break
            h_cur, cur = 0.0, 0
        if not cur and need > bios.BODY_MM and last is not None and pieces(last) \
                and bios.BODY_MM - heads > last.get("_minroom", 0) + 1:
            plan = (last, bios.BODY_MM - heads)         # taller than a page
            break
        cur += 1
        h_cur += H[i]
    if not plan:
        return None
    b, room = plan
    ks = pieces(b)
    cands = [cut(b, k)[0] for k in range(1, len(ks))]
    hs = _measure(cands, folder)
    n = len(ks)
    ok = lambda k: b["t"] != "table" or n < 4 or 2 <= k <= n - 2     # no table row left alone on a page
    best = max((k for k, h in enumerate(hs, 1) if h <= room - 0.5 and ok(k)), default=None)
    if best is None:
        b["_minroom"] = room                            # its first piece needs more room than this
        return blocks
    head, tail = cut(b, best)
    n = next(i for i, x in enumerate(blocks) if x is b)
    return blocks[:n] + [head, tail] + blocks[n + 1:]


_TH = {}


def _measure_html(h, folder):
    if h not in _TH:
        path = os.path.join(folder, ".build", "flowfit-measure.html")
        open(path, "w").write(bios.doc("measure", [bios.page(f'<div data-m="0" style="display:flow-root">{h}</div>', 1, bios.M["unit_en"])]))
        _TH[h] = json.loads(bios.node("measure", path))["0"]
        os.remove(path)
    return _TH[h]


def fit(folder, min_gap=None):
    """min_gap: share of the page a gap must exceed before a block is cut (default MIN_GAP = 0.12;
    0.08 also fills the small gaps left before a section heading)."""
    global MIN_GAP
    if min_gap is not None:
        MIN_GAP = min_gap
    if not os.path.isdir(folder):
        folder = os.path.join("/home/user/-", folder)
    folder = folder.rstrip("/")
    path = os.path.join(folder, "lecture.json")
    data = json.load(open(path))
    _prepare(folder, data)
    blocks = unfit(data["blocks"])
    n_cuts = 0
    for _ in range(400):
        nb = _pass(blocks, folder)
        if nb is None:
            break
        n_cuts += len(nb) > len(blocks)
        blocks = nb
    out, ids = [], {}
    for b in blocks:
        c = _clean(b)
        if b.get("_ff"):
            c["_ff"] = ids.setdefault(b["_ff"], len(ids) + 1)
        out.append(c)
    data["blocks"] = out
    json.dump(data, open(path, "w"), ensure_ascii=False, indent=1)
    print(f"flowfit {os.path.basename(folder)}: {n_cuts} cuts")

```
