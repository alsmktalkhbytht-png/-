import math, random

def emblem(c_ring=("#FCFDC8", "#FFEBAF", "#C69FD5", "#2C6D7D"), agar="#FFEBAF",
           streak="#C69FD5", colony="#4C9DB0", bug="#1E4D59", rim="#FFFFFF", label="#1E4D59", seed=7):
    """Petri dish inside four containment rings (BSL-1 → BSL-4)."""
    rnd = random.Random(seed)
    s = ['<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">']
    # containment rings: outer = BSL-1 ... inner = BSL-4 (protection tightens toward the agent)
    radii = [192, 170, 148, 126]
    widths = [5, 7, 9, 11]
    for i, (r, w) in enumerate(zip(radii, widths)):
        dash = "" if i == 3 else f'stroke-dasharray="{[3, 10, 26, 60][i]} {[9, 8, 7, 0][i]}"'
        s.append(f'<circle cx="200" cy="200" r="{r}" fill="none" stroke="{c_ring[i]}" stroke-width="{w}" '
                 f'stroke-linecap="round" {dash}/>')
    # level badges on the right side (angle -28deg)
    for i, r in enumerate(radii):
        a = math.radians(-32 + i * 0)
        x = 200 + r * math.cos(a); y = 200 + r * math.sin(a)
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="12.5" fill="{c_ring[3] if i < 3 else c_ring[1]}" stroke="#fff" stroke-width="2.5"/>')
        s.append(f'<text x="{x:.1f}" y="{y + 5.2:.1f}" text-anchor="middle" font-family="Mada" font-weight="900" '
                 f'font-size="15" fill="{c_ring[1] if i < 3 else c_ring[3]}">{i + 1}</text>')
    # dish
    s.append(f'<circle cx="200" cy="200" r="108" fill="{rim}" opacity=".95"/>')
    s.append(f'<circle cx="200" cy="200" r="99" fill="{agar}"/>')
    s.append('<ellipse cx="168" cy="150" rx="46" ry="20" fill="#fff" opacity=".35" transform="rotate(-35 168 150)"/>')
    # streak plate pattern: three zones
    s.append(f'<g fill="none" stroke="{streak}" stroke-width="3.2" stroke-linecap="round" opacity=".9">')
    s.append('<path d="M128 170 q20 -14 40 0 q20 14 40 0 q16 -12 30 -2"/>')
    s.append('<path d="M120 190 q22 -14 44 0 q22 14 44 0 q18 -12 36 0"/>')
    s.append('<path d="M232 166 q14 22 0 44 q-14 22 0 44"/>')
    s.append('<path d="M252 176 q12 20 0 40 q-12 20 0 40"/>')
    s.append('<path d="M150 262 q16 -14 32 0 q16 14 32 0"/>')
    s.append('</g>')
    # colonies
    for _ in range(26):
        a = rnd.uniform(0, 2 * math.pi); r = rnd.uniform(15, 86)
        x = 200 + r * math.cos(a); y = 200 + r * math.sin(a)
        rr = rnd.choice([3, 3.5, 4.5, 5.5, 7])
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{rr}" fill="{colony}" opacity="{rnd.uniform(.55, .95):.2f}"/>')
    # bacilli and cocci
    for (x, y, rot) in [(176, 222, 30), (196, 232, -20), (214, 214, 65), (160, 236, -50), (226, 240, 10)]:
        s.append(f'<rect x="{x - 11}" y="{y - 4.5}" width="22" height="9" rx="4.5" fill="{bug}" transform="rotate({rot} {x} {y})"/>')
    for (x, y) in [(244, 150), (252, 157), (240, 160), (249, 167), (258, 148)]:
        s.append(f'<circle cx="{x}" cy="{y}" r="4.3" fill="{bug}"/>')
    s.append(f'<circle cx="200" cy="200" r="99" fill="none" stroke="{label}" stroke-opacity=".18" stroke-width="2"/>')
    s.append('</svg>')
    return "".join(s)


def grid(color="rgba(76,157,176,.22)", cols=5, rows=4, letters="ABCD", label_color="rgba(76,157,176,.55)"):
    cells = []
    for r in range(rows):
        for c in range(cols):
            cells.append(f'<div class="gcell" style="border-color:{color}"><span style="color:{label_color}">{letters[r]}{c + 1}</span></div>')
    return f'<div class="grid" style="grid-template-columns:repeat({cols},1fr);grid-template-rows:repeat({rows},1fr)">' + "".join(cells) + "</div>"
