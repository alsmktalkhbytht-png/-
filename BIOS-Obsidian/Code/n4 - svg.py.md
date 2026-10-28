---
source: BIOS-Obsidian/tools/scripts/n4/svg.py
handouts: [advtech-lec1-elisa]
saved: 2026-10-28
tags: [bios, code]
---
# n4/svg.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#advtech-lec1-elisa|advtech-lec1-elisa]]

```python
INK="#4a2a30"; CORAL="#f2808f"; PINK="#eebcc2"; BEIGE="#e8d6d0"; LIGHT="#f9e9ef"
def ab(x, y_tip, up, col, w=4.2):
    """Antibody Y. up=True: stem below, arms open upward (tips at y_tip). up=False: arms open downward."""
    s = -1 if up else 1   # direction from tips to junction
    jy = y_tip + s*(-14) if False else (y_tip + 14 if up else y_tip - 14)
    sy = jy + 18 if up else jy - 18
    return (f'<path d="M{x-10},{y_tip} L{x},{jy} L{x+10},{y_tip} M{x},{jy} L{x},{sy}" stroke="{col}" stroke-width="{w}" '
            f'fill="none" stroke-linecap="round" stroke-linejoin="round"/>'), sy
def ag(x, y, r=8): return f'<path d="M{x},{y-r} L{x+r},{y} L{x},{y+r} L{x-r},{y} Z" fill="{PINK}" stroke="{INK}" stroke-width="1.6"/>'
def enz(x, y):
    import math
    pts = " ".join(f"{x+ (8 if i%2==0 else 3.6)*math.cos(math.pi/2+i*math.pi/5):.1f},{y- (8 if i%2==0 else 3.6)*math.sin(math.pi/2+i*math.pi/5):.1f}" for i in range(10))
    return f'<polygon points="{pts}" fill="{CORAL}" stroke="{INK}" stroke-width="1.3"/>'
PLATE = lambda: f'<rect x="10" y="190" width="180" height="12" rx="2" fill="{BEIGE}" stroke="{INK}" stroke-width="1"/>'
def panel(kind):
    g = [PLATE()]
    if kind == "direct":
        g.append(ag(100, 182))
        p, top = ab(100, 172, False, CORAL); g.append(p); g.append(enz(100, top - 8))
    if kind == "indirect":
        g.append(ag(100, 182))
        p, top = ab(100, 172, False, INK); g.append(p)
        p2, top2 = ab(100, top - 4, False, CORAL); g.append(p2); g.append(enz(100, top2 - 8))
    if kind == "sandwich":
        p, top = ab(100, 158, True, INK)   # capture: stem on the plate
        g.append(f'<path d="M90,158 L100,172 L110,158 M100,172 L100,190" stroke="{INK}" stroke-width="4.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
        g.append(ag(100, 150))
        p2, top2 = ab(100, 140, False, CORAL); g.append(p2); g.append(enz(100, top2 - 8))
    if kind == "competitive":
        for x in (60, 140):
            g.append(f'<path d="M{x-10},158 L{x},172 L{x+10},158 M{x},172 L{x},190" stroke="{INK}" stroke-width="4.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
        g.append(ag(60, 150))                       # sample antigen
        g.append(ag(140, 150)); g.append(enz(140, 132))   # labelled antigen
        g.append(ag(95, 95)); g.append(ag(118, 110)); g.append(enz(118, 92))   # free, competing in solution
    return "".join(g)
NAMES = {"direct": ("Direct", "مباشر"), "indirect": ("Indirect", "غير مباشر"), "sandwich": ("Sandwich", "الساندويتش"), "competitive": ("Competitive", "التنافسي")}
def svg(body, w, h, y0=70): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 {y0} {w} {h-y0}" width="{w*2}" height="{(h-y0)*2}" font-family="Arial, sans-serif">{body}</svg>'
out = "/home/user/-/advtech-lec1-elisa/assets/"
for k in NAMES:
    open(out + f"elisa-{k}.svg", "w").write(svg(f'<rect width="200" height="215" fill="#fff"/>' + panel(k), 200, 215))
# combined figure with labels and legend
body = '<rect width="820" height="300" fill="#fff"/>'
for i, k in enumerate(NAMES):
    body += f'<g transform="translate({i*205},0)">{panel(k)}<text x="100" y="228" text-anchor="middle" font-size="15" font-weight="bold" fill="{INK}">{NAMES[k][0]}</text></g>'
leg = [(ag(30, 268), "Antigen"), (f'<path d="M190,262 L198,272 L206,262 M198,272 L198,282" stroke="{INK}" stroke-width="3.5" fill="none" stroke-linecap="round"/>', "Primary / capture antibody"),
       (f'<path d="M420,262 L428,272 L436,262 M428,272 L428,282" stroke="{CORAL}" stroke-width="3.5" fill="none" stroke-linecap="round"/>', "Enzyme-linked (labelled) antibody"),
       (enz(720, 270), "Enzyme")]
xs = [45, 214, 444, 735]
for (shape, lab), x in zip(leg, xs):
    body += shape + f'<text x="{x}" y="275" font-size="12" fill="{INK}">{lab}</text>'
body += f'<rect x="10" y="252" width="800" height="36" rx="6" fill="none" stroke="{PINK}"/>'
open(out + "elisa-types.svg", "w").write(svg(body, 820, 300))

```
