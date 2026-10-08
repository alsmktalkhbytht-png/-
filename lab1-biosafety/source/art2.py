"""Vector artwork for the BIOS booklet (all hand-built SVG)."""
import math, random

BURG = "#6B1E2A"; BURG_D = "#46121A"; GOLD = "#B38B4D"; GOLD_L = "#D9C08E"; INK = "#2B211F"; IVORY = "#FAF6EE"


def _pt(r, deg, cx=0, cy=0):
    a = math.radians(deg)
    return cx + r * math.cos(a), cy + r * math.sin(a)


# ------------------------------------------------------------------ warning symbols
def biohazard(size="100%", fill=INK, tri="#E2B84C", edge=INK):
    """Biohazard sign: constructed from the standard circle geometry, inside a warning triangle."""
    s = [f'<svg viewBox="-60 -62 120 112" width="{size}" xmlns="http://www.w3.org/2000/svg">']
    s.append(f'<path d="M0 -56 L56 44 L-56 44 Z" fill="{tri}" stroke="{edge}" stroke-width="5" stroke-linejoin="round"/>')
    s.append('<defs><mask id="bhm"><rect x="-60" y="-60" width="120" height="120" fill="black"/>')
    k = 1.0
    cy = 14
    L = (-90, 30, 150)
    for ang in L:   # lobes
        x, y = _pt(11 * k, ang, 0, cy)
        s.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{15 * k:.2f}" fill="white"/>')
    for ang in L:   # hollow of each lobe (opens outward)
        x, y = _pt(16.2 * k, ang, 0, cy)
        s.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{10.5 * k:.2f}" fill="black"/>')
    s.append(f'<circle cx="0" cy="{cy}" r="{12.8 * k:.2f}" fill="none" stroke="white" stroke-width="{3.2 * k:.2f}"/>')
    for ang in L:   # thin separation between ring and lobe edge
        x, y = _pt(16.2 * k, ang, 0, cy)
        s.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{10.5 * k:.2f}" fill="none" stroke="black" stroke-width="{1.6 * k:.2f}"/>')
        x2, y2 = _pt(6.5 * k, ang, 0, cy)
        s.append(f'<line x1="0" y1="{cy}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="black" stroke-width="{1.5 * k:.2f}"/>')
    s.append(f'<circle cx="0" cy="{cy}" r="{3.2 * k:.2f}" fill="black"/>')
    s.append('</mask></defs>')
    s.append(f'<g transform="translate(0 14) scale(1.12) translate(0 -14)"><rect x="-60" y="-60" width="120" height="120" fill="{fill}" mask="url(#bhm)"/></g>')
    s.append('</svg>')
    return "".join(s)


def radiation(size="100%", fill=INK, tri="#E2B84C", edge=INK):
    s = [f'<svg viewBox="-60 -62 120 112" width="{size}" xmlns="http://www.w3.org/2000/svg">']
    s.append(f'<path d="M0 -56 L56 44 L-56 44 Z" fill="{tri}" stroke="{edge}" stroke-width="5" stroke-linejoin="round"/>')
    cx, cy = 0, 14
    r0, r1 = 7.5, 27
    s.append(f'<circle cx="{cx}" cy="{cy}" r="5" fill="{fill}"/>')
    for c in (-150, -30, 90):
        a0, a1 = c - 30, c + 30
        x0, y0 = _pt(r0, a0, cx, cy); x1, y1 = _pt(r1, a0, cx, cy)
        x2, y2 = _pt(r1, a1, cx, cy); x3, y3 = _pt(r0, a1, cx, cy)
        s.append(f'<path d="M{x0:.2f} {y0:.2f} L{x1:.2f} {y1:.2f} A{r1} {r1} 0 0 1 {x2:.2f} {y2:.2f} '
                 f'L{x3:.2f} {y3:.2f} A{r0} {r0} 0 0 0 {x0:.2f} {y0:.2f} Z" fill="{fill}"/>')
    s.append('</svg>')
    return "".join(s)


# ------------------------------------------------------------------ ornaments
def corner(size_mm=14, color=GOLD, rot=0):
    return (f'<svg viewBox="0 0 60 60" style="width:{size_mm}mm;height:{size_mm}mm;transform:rotate({rot}deg)" xmlns="http://www.w3.org/2000/svg">'
            f'<g fill="none" stroke="{color}" stroke-width="1.1">'
            '<path d="M2 58 V2 H58"/><path d="M7 58 V7 H58" stroke-width=".6"/>'
            '<path d="M12 40 V12 H40" stroke-width=".6"/>'
            '<path d="M2 2 L18 18" stroke-width=".7"/>'
            '<path d="M12 22 Q22 22 22 12" stroke-width=".7"/>'
            '</g>'
            f'<path d="M18 14 L22 18 L18 22 L14 18 Z" fill="{color}"/>'
            f'<circle cx="7" cy="7" r="1.6" fill="{color}"/>'
            '</svg>')


def divider(width="60mm", color=GOLD):
    return (f'<svg viewBox="0 0 300 16" style="width:{width};height:auto;display:block;margin:0 auto" xmlns="http://www.w3.org/2000/svg">'
            f'<g stroke="{color}" fill="none" stroke-width="1"><path d="M0 8 H118"/><path d="M182 8 H300"/>'
            '<path d="M124 8 Q137 0 150 8 Q163 16 176 8" /></g>'
            f'<path d="M150 2 L156 8 L150 14 L144 8 Z" fill="{color}"/>'
            f'<circle cx="118" cy="8" r="2" fill="{color}"/><circle cx="182" cy="8" r="2" fill="{color}"/></svg>')


# ------------------------------------------------------------------ line icons (24x24, stroke)
_I = {
 "microscope": '<path d="M6 21h12"/><path d="M9 21v-3"/><path d="M10 4l4 2-3.5 7-4-2z"/><path d="M12 5l1-2 2 1-1 2"/><path d="M9.5 12.5l-1 2"/><path d="M14 18a6 6 0 0 0 2-9"/><path d="M8 18h8"/>',
 "clipboard": '<rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4V3h6v1"/><path d="M8 10l1.5 1.5L12 9"/><path d="M14 10.5h3"/><path d="M8 15l1.5 1.5L12 14"/><path d="M14 15.5h3"/>',
 "person": '<circle cx="12" cy="8" r="3.6"/><path d="M5 21v-1.5a7 7 0 0 1 14 0V21"/><path d="M9.5 15.5l2.5 3 2.5-3"/>',
 "coat": '<path d="M8 3l4 3 4-3 3 3-2 4v11H7V10L5 6z"/><path d="M12 6v15"/><path d="M9 14h1.5"/>',
 "gloves": '<path d="M7 21v-5l-3-4 1.5-1.5L8 13V5.5a1.3 1.3 0 0 1 2.6 0V11V4a1.3 1.3 0 0 1 2.6 0v7V5a1.3 1.3 0 0 1 2.6 0v8l1-2a1.3 1.3 0 0 1 2.2 1.3L17 17v4"/>',
 "nofood": '<circle cx="12" cy="12" r="9"/><path d="M5.6 5.6l12.8 12.8"/><path d="M9 7v5m-1.5-5v3a1.5 1.5 0 0 0 3 0V7"/><path d="M15 7c-1 0-1.6 1.6-1.6 3.4 0 1 .6 1.6 1.6 1.6V17"/>',
 "hair": '<path d="M7 11a5 5 0 0 1 10 0v2"/><path d="M7 11c0 4 2 7 5 7s5-3 5-7"/><path d="M17 12c2 2 2 5 1 8"/><path d="M15.5 17.5l2.2 0"/><path d="M8 9c2-2 6-2 8 0"/>',
 "dish": '<ellipse cx="12" cy="13" rx="9" ry="5"/><path d="M3 13v2c0 2.8 4 5 9 5s9-2.2 9-5v-2"/><circle cx="9" cy="12.5" r="1"/><circle cx="13" cy="14" r=".8"/><circle cx="15" cy="12" r="1.1"/>',
 "wash": '<path d="M5 7h7a3 3 0 0 1 3 3"/><path d="M15 10v1"/><path d="M15 13.5l-.8 1.4a.9.9 0 1 0 1.6 0z"/><path d="M4 21c1-3 3-4 6-4h4l3-2 2 1-3 4H8"/><path d="M5 5v4"/>',
 "tools": '<path d="M5 19l6-6"/><path d="M14 4a3 3 0 0 0-3 4l-1 1 4 4 1-1a3 3 0 0 0 4-3l-2 1-2-2 1-2z"/><path d="M15 15l4 4"/><path d="M8 4l-2 2 2 2"/><circle cx="18.5" cy="5.5" r="1.5"/>',
 "waste": '<path d="M5 7h14"/><path d="M9 7V4h6v3"/><path d="M6.5 7l1 14h9l1-14"/><path d="M10 11v6m4-6v6"/>',
 "flame": '<path d="M12 3c1 3 5 5 5 10a5 5 0 0 1-10 0c0-2 1-3.5 2-4.5 0 2 1 3 2 3 0-3-1-5 1-8.5z"/>',
 "spray": '<rect x="7" y="9" width="8" height="12" rx="1.5"/><path d="M9 9V6h4v3"/><path d="M13 6h3l1 1"/><path d="M19 4l1-1m-1 4h1.5m-1.5 3l1 1"/>',
 "hand": '<path d="M7 20c-2-2-3-4-3-7V9a1.3 1.3 0 0 1 2.6 0v3V5.5a1.3 1.3 0 0 1 2.6 0V11V4.5a1.3 1.3 0 0 1 2.6 0V11V5.5a1.3 1.3 0 0 1 2.6 0V13l1.6-2a1.3 1.3 0 0 1 2.1 1.5L16 18c-1 1.5-2.5 2-4 2z"/>',
 "drops": '<path d="M8 4l-3 5a3 3 0 0 0 6 0z"/><path d="M16 9l-3.5 6a3.5 3.5 0 0 0 7 0z"/><path d="M4 20h16"/>',
 "lab": '<path d="M9 3h6"/><path d="M10 3v6l-5 9a2 2 0 0 0 1.8 3h10.4a2 2 0 0 0 1.8-3l-5-9V3"/><path d="M7.5 15h9"/>',
 "risk": '<path d="M12 3l9 16H3z"/><path d="M12 9v5"/><circle cx="12" cy="16.8" r=".6"/>',
 "search": '<circle cx="10.5" cy="10.5" r="6"/><path d="M15 15l5 5"/><path d="M8 10.5h5M10.5 8v5"/>',
 "cabinet": '<rect x="4" y="3" width="16" height="13" rx="1"/><path d="M4 7h16"/><path d="M7 16v5m10-5v5"/><path d="M8 10h8"/>',
 "shield": '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
 "book": '<path d="M4 5c3-1 6-1 8 1 2-2 5-2 8-1v14c-3-1-6-1-8 1-2-2-5-2-8-1z"/><path d="M12 6v14"/>',
 "star": '<path d="M12 3l2.6 5.6 6 .7-4.5 4.1 1.2 6L12 16.4 6.7 19.4l1.2-6L3.4 9.3l6-.7z"/>',
 "check": '<circle cx="12" cy="12" r="9"/><path d="M8 12.5l3 3 5-6"/>',
 "quill": '<path d="M20 4C12 5 7 10 5 19"/><path d="M20 4c-1 5-4 9-9 10"/><path d="M4 21l2-3"/>',
 "plane": '<path d="M21 4L3 11l6 2 2 6 3-4 4 3z"/><path d="M9 13l12-9"/>',
 "bulb": '<path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-3.5 10.9c.7.5 1 1.3 1 2.1h5c0-.8.3-1.6 1-2.1A6 6 0 0 0 12 3z"/>',
 "alert": '<path d="M12 3l9 16H3z"/><path d="M12 9v5"/><circle cx="12" cy="16.8" r=".6"/>',
 "brain": '<path d="M9 4a3 3 0 0 0-3 3 3 3 0 0 0-2 5 3 3 0 0 0 2 5 3 3 0 0 0 3 3h1V4z"/><path d="M15 4a3 3 0 0 1 3 3 3 3 0 0 1 2 5 3 3 0 0 1-2 5 3 3 0 0 1-3 3h-1V4z"/>',
 "scale": '<path d="M12 4v16M7 20h10"/><path d="M5 7h14"/><path d="M5 7l-3 6a3 3 0 0 0 6 0zM19 7l-3 6a3 3 0 0 0 6 0z"/>',
 "key": '<circle cx="8" cy="15" r="4"/><path d="M11 12l8-8M16 7l2 2M14 9l2 2"/>',
}


def icon(name, color=BURG, size="100%", sw=1.5):
    return (f'<svg viewBox="0 0 24 24" width="{size}" height="{size}" fill="none" stroke="{color}" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg">{_I[name]}</svg>')


# ------------------------------------------------------------------ cover medallion (bacteria field)
def medallion(seed=3, uid="m"):
    rnd = random.Random(seed)
    W = 400
    s = [f'<svg viewBox="0 0 {W} {W}" xmlns="http://www.w3.org/2000/svg"><defs>']
    s.append(f'<clipPath id="{uid}c"><circle cx="200" cy="200" r="184"/></clipPath>')
    s.append(f'<radialGradient id="{uid}bg" cx="45%" cy="40%" r="70%"><stop offset="0" stop-color="#5A2230"/>'
             '<stop offset=".6" stop-color="#3A1219"/><stop offset="1" stop-color="#1E080C"/></radialGradient>')
    palettes = {
        "rose": ("#E7A9A3", "#B9585A", "#5E1A24"),
        "plum": ("#C9A2D6", "#7E4A93", "#331A40"),
        "slate": ("#A9B9DD", "#55679C", "#1F2848"),
        "wine": ("#E59B8F", "#A23B3E", "#4A0F16"),
    }
    for k, (a, b, c) in palettes.items():
        s.append(f'<radialGradient id="{uid}{k}" cx="35%" cy="30%" r="80%"><stop offset="0" stop-color="{a}"/>'
                 f'<stop offset=".55" stop-color="{b}"/><stop offset="1" stop-color="{c}"/></radialGradient>')
    s.append(f'<pattern id="{uid}tx" width="7" height="7" patternUnits="userSpaceOnUse">'
             '<circle cx="2" cy="2" r="1.1" fill="#000" opacity=".22"/><circle cx="5.5" cy="5" r=".8" fill="#fff" opacity=".18"/></pattern>')
    s.append(f'<filter id="{uid}blur"><feGaussianBlur stdDeviation="3.2"/></filter>')
    s.append('</defs>')
    s.append(f'<g clip-path="url(#{uid}c)"><rect width="{W}" height="{W}" fill="url(#{uid}bg)"/>')

    def bacillus(cx, cy, L, Wd, rot, pal, blur=False, flag=0):
        g = [f'<g transform="rotate({rot} {cx} {cy})"' + (f' filter="url(#{uid}blur)" opacity=".75"' if blur else "") + '>']
        for _ in range(flag):
            y0 = cy + rnd.uniform(-Wd / 2, Wd / 2)
            side = rnd.choice([-1, 1])
            x0 = cx + side * L / 2
            d = f"M{x0:.1f} {y0:.1f}"
            x, y = x0, y0
            for _k in range(4):
                nx = x + side * rnd.uniform(10, 16); ny = y + rnd.uniform(-9, 9)
                d += f" Q{(x + nx) / 2 + rnd.uniform(-6, 6):.1f} {(y + ny) / 2 + rnd.uniform(-8, 8):.1f} {nx:.1f} {ny:.1f}"
                x, y = nx, ny
            g.append(f'<path d="{d}" fill="none" stroke="#C98A86" stroke-width=".8" opacity=".55"/>')
        g.append(f'<rect x="{cx - L / 2}" y="{cy - Wd / 2}" width="{L}" height="{Wd}" rx="{Wd / 2}" fill="url(#{uid}{pal})"/>')
        g.append(f'<rect x="{cx - L / 2}" y="{cy - Wd / 2}" width="{L}" height="{Wd}" rx="{Wd / 2}" fill="url(#{uid}tx)"/>')
        g.append(f'<rect x="{cx - L / 2 + Wd * .25}" y="{cy - Wd * .38}" width="{L * .55}" height="{Wd * .18}" rx="{Wd * .09}" fill="#fff" opacity=".18"/>')
        g.append('</g>')
        return "".join(g)

    def coccus(cx, cy, r, pal, blur=False):
        b = f' filter="url(#{uid}blur)" opacity=".7"' if blur else ""
        return (f'<g{b}><circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#{uid}{pal})"/>'
                f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#{uid}tx)"/></g>')

    # background (blurred, depth)
    s.append(bacillus(80, 90, 120, 44, 25, "wine", blur=True))
    s.append(bacillus(330, 300, 130, 46, -35, "plum", blur=True))
    s.append(coccus(320, 95, 26, "rose", blur=True))
    s.append(coccus(70, 300, 22, "slate", blur=True))
    # mid layer
    s.append(bacillus(285, 120, 120, 40, 18, "slate"))
    s.append(bacillus(95, 210, 120, 42, -28, "plum"))
    # streptococcus chain
    x, y = 300, 170
    for i in range(7):
        s.append(coccus(x, y, 15 - i * .4, "slate"))
        x += rnd.uniform(-3, 4); y += 24
    # staph cluster
    for (dx, dy) in [(0, 0), (22, 6), (8, 22), (30, 26), (-12, 20)]:
        s.append(coccus(110 + dx, 300 + dy, 13, "rose"))
    # hero bacillus
    s.append(bacillus(200, 215, 190, 66, -38, "rose", flag=26))
    s.append('</g>')
    # rings
    s.append(f'<circle cx="200" cy="200" r="186" fill="none" stroke="{GOLD}" stroke-width="5"/>')
    s.append(f'<circle cx="200" cy="200" r="195" fill="none" stroke="{GOLD_L}" stroke-width="1.2"/>')
    for a in range(0, 360, 10):
        x1, y1 = _pt(190, a, 200, 200); x2, y2 = _pt(195 if a % 30 else 199, a, 200, 200)
        s.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{GOLD}" stroke-width="1"/>')
    s.append('</svg>')
    return "".join(s)
