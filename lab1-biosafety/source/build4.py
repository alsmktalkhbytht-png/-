"""BIOS bilingual booklet — Lab 1 (academic edition).

python3 build4.py  →  booklet4.html   (then: node render4.js booklet4.html out.pdf shots/)
Pagination is done in the browser (see PAGINATE): blocks flow onto A4 pages, headings and
lead-in lines stay with what follows, table rows carry a repeated header, and a notes area is
added only where a page ends at a section boundary with real space left.
"""
import re, html
from content4 import META as M, B, LABELS, MARKS

# ------------------------------------------------------------------ inline markup
def md(s):
    s = html.escape(s, quote=False)
    s = s.replace("[[cut]]", '<span class="cut">[text cut off in the original file]</span>')
    s = s.replace("[[قطع]]", '<span class="cut">[النص مقطوع في الملف الأصلي]</span>')
    s = s.replace("[[rev]]", '<span class="flag">!</span>')
    s = re.sub(r"==(.+?)==", r'<b class="em1">\1</b>', s)
    s = re.sub(r"\+\+(.+?)\+\+", r'<b class="em2">\1</b>', s)
    s = re.sub(r"\*\*(.+?)\*\*", r'<b class="term">\1</b>', s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", s)
    s = re.sub(r"`(.+?)`", r'<bdi dir="ltr" class="lat">\1</bdi>', s)
    return s

def en(s, cls=""): return f'<p class="en {cls}" dir="ltr">{md(s)}</p>'
def ar(s, cls=""): return f'<p class="ar {cls}" dir="rtl">{md(s)}</p>'
def blk(inner, cls="", attrs=""): return f'<div class="blk {cls}" {attrs}>{inner}</div>'

FIG = {"n": 0}
def figcap(e, a):
    FIG["n"] += 1; n = FIG["n"]
    return (f'<figcaption><span class="ce" dir="ltr"><b>Figure {n}.</b> {md(e)}</span>'
            f'<span class="ca" dir="rtl"><b>الشكل {n}.</b> {md(a)}</span></figcaption>')

# ------------------------------------------------------------------ cover art
def trefoil(color, op):
    """Biohazard trefoil outline used only as a faint decorative watermark on the cover."""
    import math
    parts = []
    for a in (-90, 30, 150):
        r = math.radians(a)
        cx, cy = 50 + 15 * math.cos(r), 50 + 15 * math.sin(r)
        hx, hy = 50 + 21 * math.cos(r), 50 + 21 * math.sin(r)
        parts.append(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="20" />')
        parts.append(f'<circle cx="{hx:.2f}" cy="{hy:.2f}" r="13.5" />')
    return (f'<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><g fill="none" stroke="{color}" '
            f'stroke-width=".55" opacity="{op}">{"".join(parts)}<circle cx="50" cy="50" r="17" stroke-width="2.4"/>'
            f'<circle cx="50" cy="50" r="5.5"/></g></svg>')

def cabinet_art():
    c, g, s = "#6E1F2A", "#B08A3E", "#56605A"
    arrows = "".join(f'<path d="M{x} 40 v20 m-3.2 -4.6 l3.2 4.6 l3.2 -4.6" stroke="{g}" stroke-width="1.4" fill="none" stroke-linecap="round"/>'
                     for x in (62, 82, 102, 122, 142))
    return f'''<svg viewBox="0 0 204 190" xmlns="http://www.w3.org/2000/svg" fill="none" stroke-linejoin="round">
<rect x="40" y="14" width="124" height="26" rx="3" stroke="{s}" stroke-width="1.6"/>
<g stroke="{s}" stroke-width=".8" opacity=".7">{"".join(f'<line x1="{x}" y1="20" x2="{x}" y2="34"/>' for x in range(50, 158, 6))}</g>
<rect x="36" y="40" width="132" height="92" rx="4" stroke="{c}" stroke-width="2"/>
<path d="M46 50 h112 v52 h-112 z" stroke="{c}" stroke-width="1.2" fill="#fff" fill-opacity=".55"/>
{arrows}
<line x1="46" y1="102" x2="158" y2="102" stroke="{c}" stroke-width="1.2"/>
<rect x="46" y="108" width="112" height="16" rx="2" stroke="{s}" stroke-width="1.1"/>
<g stroke="{s}" stroke-width=".9">{"".join(f'<line x1="{x}" y1="112" x2="{x}" y2="120"/>' for x in range(52, 156, 5))}</g>
<ellipse cx="80" cy="99" rx="11" ry="2.6" stroke="{c}" stroke-width="1.1"/><ellipse cx="80" cy="97.6" rx="11" ry="2.6" stroke="{c}" stroke-width=".8"/>
<path d="M112 99 v-15 h9 v15 z M110.5 84 h12" stroke="{s}" stroke-width="1.1"/><path d="M112 93 h9" stroke="{g}" stroke-width="2"/>
<path d="M134 99 l6 -22 l3 1 l-5 21" stroke="{c}" stroke-width="1.1"/>
<line x1="50" y1="132" x2="50" y2="176" stroke="{s}" stroke-width="2"/><line x1="154" y1="132" x2="154" y2="176" stroke="{s}" stroke-width="2"/>
<line x1="50" y1="160" x2="154" y2="160" stroke="{s}" stroke-width="1.1"/>
<line x1="40" y1="176" x2="60" y2="176" stroke="{s}" stroke-width="2"/><line x1="144" y1="176" x2="164" y2="176" stroke="{s}" stroke-width="2"/>
</svg>'''

def ladder():
    cols = ["#8C9A8E", "#B08A3E", "#9A4A3A", "#6E1F2A"]
    out = ['<div class="ladder">']
    for i, col in enumerate(cols, 1):
        out.append(f'<div class="step" style="height:{8 + i * 6}mm;background:{col}"><b>{i}</b></div>')
    out.append('</div><div class="ladder-cap"><span dir="ltr">Risk groups 1 → 4</span><span dir="rtl">مجموعات الخطورة 1–4</span></div>')
    return "".join(out)

def cover():
    info = [("Instructor", "التدريسي", "", M["doctor_ar"]),
            ("Stage", "المرحلة", M["stage_en"], M["stage_ar"]),
            ("Subject", "المادة", M["subject_en"], M["subject_ar"]),
            ("Lecture", "رقم المحاضرة", M["lab_en"], M["lab_ar"]),
            ("Type", "النوع", M["type_en"], M["type_ar"])]
    cards = "".join(f'<div class="ic"><div class="ik"><span dir="ltr">{k}</span><span dir="rtl">{ka}</span></div>'
                    f'<div class="iv">{f"<span dir=ltr>{v}</span>" if v else ""}<span dir="rtl">{va}</span></div></div>' for k, ka, v, va in info)
    return f'''<section class="page cover">
<div class="cv-wm">{trefoil("#6E1F2A", .07)}</div>
<div class="cv-top"><img src="assets2/logo_full.jpg" class="cv-logo"></div>
<div class="cv-mid">
  <div class="cv-eyebrow"><span dir="ltr">{M["subject_en"]}</span><span class="dot">·</span><span dir="rtl">{M["subject_ar"]}</span></div>
  <h1 class="cv-t-en" dir="ltr">{M["title_en"]}</h1>
  <h1 class="cv-t-ar" dir="rtl">{M["title_ar"]}</h1>
  <div class="cv-badges"><span class="bd b1"><span dir="ltr">LAB 1</span><i>·</i><span dir="rtl">المختبر 1</span></span><span class="bd b2"><span dir="ltr">Practical</span><i>·</i><span dir="rtl">عملي</span></span></div>
</div>
<div class="cv-art"><div class="cv-cab">{cabinet_art()}</div><div class="cv-lad">{ladder()}</div></div>
<div class="cv-info">{cards}</div>
<div class="cv-foot"><span class="w">BIOS</span><span dir="rtl">بايوس · ترجمة وتعديل الملازم</span><span class="sp"></span><span dir="ltr">Telegram: <b>BIOS0t</b></span></div>
</section>'''

# ------------------------------------------------------------------ block renderers
def r_labtitle(_):
    return blk(f'''<div class="opener"><div class="op-l"><div class="op-eb" dir="ltr">{M["subject_en"]} · {M["stage_en"]} · Laboratories</div>
<div class="op-eb ar" dir="rtl">{M["subject_ar"]} · {M["stage_ar"]} · المختبرات</div>
<h1 class="op-en" dir="ltr">{M["title_en"]}</h1><h1 class="op-ar" dir="rtl">{M["title_ar"]}</h1></div>
<div class="op-r"><small>LAB</small><b>1</b><small dir="rtl">المختبر</small></div></div>''', "")

def r_section(k):
    tag = ('<span class="edit" dir="rtl">عنوان تنظيمي</span>' if k.get("editorial") else "")
    return blk(f'<div class="sec"><div class="sn">{k["n"]}</div><div class="st"><div class="se" dir="ltr">{md(k["en"])}{tag}</div>'
               f'<div class="sa" dir="rtl">{md(k["ar"])}</div></div></div>', "keep clr")

def r_h2(k):
    return blk(f'<div class="h2"><div class="h2e" dir="ltr">{md(k["en"])}</div><div class="h2a" dir="rtl">{md(k["ar"])}</div></div>', "keep clr")

def r_p(k):
    return blk(f'<div class="pair">{en(k["en"])}{ar(k["ar"])}</div>', "keep" if k.get("keep") else "")

def bul(e, a):
    return f'<div class="pair bl">{en(e)}{ar(a)}</div>'

def r_side(k):
    items = "".join(bul(e, a) for e, a in k["items"])
    return blk(f'<div class="side" style="grid-template-columns:1fr {k["w"]}mm"><div>{items}</div>'
               f'<figure class="fig sm"><img src="assets2/{k["img"]}">{figcap(k["cap_en"], k["cap_ar"])}</figure></div>')

def r_rgtable(k):
    h = k["head"]
    cols = '<colgroup><col style="width:39mm"><col><col style="width:11mm"></colgroup>'
    head = (f'<table class="rg">{cols}<thead><tr>' + "".join(
        f'<th><span class="te" dir="ltr">{md(e)}</span><span class="ta" dir="rtl">{md(a)}</span></th>' if e else '<th class="nc">#</th>' for e, a in h)
        + '</tr></thead></table>')
    out = [blk(head, "keep thead", 'data-tbl="rg"')]
    for i, (lv, lva, t, ta, d, da, n) in enumerate(k["rows"], 1):
        row = (f'<table class="rg">{cols}<tbody><tr class="r{i}">'
               f'<td class="lv"><span class="te" dir="ltr">{md(lv)}</span><span class="ta" dir="rtl">{md(lva)}</span></td>'
               f'<td class="ds"><div class="rt" dir="ltr">{md(t)}</div><div class="rta" dir="rtl">{md(ta)}</div>'
               f'{en(d, "tc")}{ar(da, "tc")}</td><td class="nc">{n}</td></tr></tbody></table>')
        out.append(blk(row, "trow", 'data-tbl="rg"'))
    return "".join(out)

def r_clarify(k):
    return blk(f'<div class="clar"><div class="cl-h"><span dir="ltr">Clarification</span><span dir="rtl">توضيح — إضافة من BIOS وليست من نص المحاضرة</span></div>'
               f'{en(k["en"])}{ar(k["ar"])}</div>')

def r_short(k):
    rows = "".join(f'<div class="sr"><div class="se2" dir="ltr">{md(e)}</div><div class="sa2" dir="rtl">{md(a)}</div></div>' for e, a in k["items"])
    return blk(f'<div class="short">{rows}</div>')

def r_symbols(_):
    cells = "".join(f'<div class="sym"><div class="sl" dir="ltr">{e}</div><div class="sla" dir="rtl">{a}</div><img src="assets2/{f}"></div>'
                    for e, a, f in [("BIOHAZARD", "خطر بيولوجي", "biohazard.jpg"), ("RADIATION HAZARD", "خطر إشعاعي", "radiation.jpg")])
    return blk(f'<figure class="fig"><div class="syms">{cells}</div>{figcap("BIOHAZARD and RADIATION HAZARD (labels as in the original slide).", "خطر بيولوجي وخطر إشعاعي (التسميتان كما في الشريحة الأصلية).")}</figure>')

def r_rules(k):
    nums = k["nums"]
    ce = f'Rule{"s" if len(nums) > 1 else ""} {" & ".join(map(str, nums))}'
    ca = f'{"القاعدتان" if len(nums) > 1 else "القاعدة"} {" و".join(map(str, nums))}'
    fig = (f'<figure class="fig fl"><img src="assets2/{k["img"]}">'
           f'<figcaption class="tag"><span dir="ltr">{ce}</span><span dir="rtl">{ca}</span></figcaption></figure>')
    out = []
    for j, (n, (e, a)) in enumerate(zip(nums, k["items"])):
        rule = f'<div class="rule"><span class="rn">{n}</span><div>{en(e)}{ar(a)}</div></div>'
        last = j == len(nums) - 1  # picture sits with the last rule of its slide (it shows that rule's subject)
        out.append(blk((fig if last else "") + rule, "rgrp" if j == 0 else ""))
    return "".join(out)

def r_def(k):
    note = ""
    if k.get("note_en"):
        note = (f'<div class="hid dn"><span dir="ltr"><span class="flag">!</span> {md(k["note_en"])}</span>'
                f'<span dir="rtl"><span class="flag">!</span> {md(k["note_ar"])}</span></div>')
    return blk(f'<div class="pair df">{en("**" + k["term_en"] + "** " + k["en"])}{ar("**" + k["term_ar"] + "** " + k["ar"])}{note}</div>')

def r_cabinet(_):
    marks = "".join(f'<span class="mk" style="left:{x}%;top:{y}%">{i}</span>' for i, (x, y) in enumerate(MARKS, 1))
    fig = (f'<figure class="fig"><div class="cab" style="width:84%;margin:0 auto"><img src="assets2/cabinets.jpg">{marks}</div>'
              f'{figcap("Biosafety Cabinet — numbers added by BIOS; labels translated in the table below.", "خزانة السلامة الحيوية — الأرقام مضافة من BIOS، وترجمة التسميات في الجدول أدناه.")}</figure>')
    def half(rng, he, ha):
        trs = "".join(f'<tr><td class="n">{i}</td><td><span class="le" dir="ltr">{md(LABELS[i-1][0])}{"<span class=flag>!</span>" if LABELS[i-1][2] else ""}</span>'
                      f'<span class="la" dir="rtl">{md(LABELS[i-1][1])}</span></td></tr>' for i in rng)
        return (f'<table class="lab"><thead><tr><th class="n">#</th><th><span dir="ltr">{he}</span><span dir="rtl" class="a">{ha}</span></th></tr></thead>'
                f'<tbody>{trs}</tbody></table>')
    tbl = (f'<div class="labs">{half(range(1, 7), "Top row of the picture", "الصف العلوي من الصورة")}{half(range(7, 12), "Bottom row of the picture", "الصف السفلي من الصورة")}</div>'
              f'<div class="hid"><span dir="ltr"><span class="flag">!</span> Labels 2–5 are partly hidden by the watermark in the original picture; only the readable parts are shown.</span>'
              f'<span dir="rtl"><span class="flag">!</span> التسميات 2–5 محجوبة جزئيًا بالعلامة المائية في الصورة الأصلية؛ لذا كُتب الجزء المقروء منها فقط.</span></div>')
    return blk(fig + tbl, "")

def r_review(_):
    items = [("Risk group 4: the description is cut off in the original slide after “transmitted from”.",
              "مجموعة الخطورة 4: الوصف مقطوع في الشريحة الأصلية بعد عبارة «transmitted from»."),
             ("Sterilization: “cell spore” is kept as written; it was translated as “cells and spores” — please confirm with the lecturer.",
              "التعقيم: أُبقيت عبارة «cell spore» كما وردت، وتُرجمت «الخلايا والأبواغ» — يُرجى التأكد من المحاضر."),
             ("Biosafety Cabinet: labels 2–5 in the picture are partly hidden by a watermark.",
              "خزانة السلامة الحيوية: التسميات 2–5 في الصورة محجوبة جزئيًا بعلامة مائية.")]
    lis = "".join(f'<li>{en(e)}{ar(a)}</li>' for e, a in items)
    return blk(f'<div class="review"><div class="rv-h"><span dir="ltr"><sup class="flag">⚑</sup> Points for review</span><span dir="rtl">مواضع تحتاج إلى مراجعة</span></div><ol>{lis}</ol></div>', "endnote")

R = {k[2:]: v for k, v in globals().items() if k.startswith("r_")}

# ------------------------------------------------------------------ CSS
CSS = open("fonts3/fonts.css").read() + r"""
:root{--burg:#6E1F2A;--burg-d:#4B141C;--burg-l:#F6EDEC;--sage:#56605A;--sage-d:#3E4741;--sage-l:#EEF1ED;--gold:#B08A3E;--gold-l:#F5EEDC;
--ink:#1E1E1E;--ink-ar:#262B28;--rule:#D8D3CA;--muted:#6F716E;
--en:'Source Serif 4',serif;--ar:'IBM Plex Sans Arabic',sans-serif;--hen:'Inter',sans-serif;--har:'Noto Kufi Arabic',sans-serif}
*{box-sizing:border-box;margin:0;padding:0}
@page{size:A4;margin:0}
html,body{background:#bbb}
body{-webkit-print-color-adjust:exact;print-color-adjust:exact;color:var(--ink)}
.page{width:210mm;height:297mm;position:relative;overflow:hidden;background:#fff;break-after:page}
@media screen{.page{margin:6mm auto}}
#flow{position:absolute;left:-9999px;top:0;width:174mm}
/* --- running head / foot */
.rh{position:absolute;left:18mm;right:18mm;top:10mm;height:9mm;display:flex;align-items:flex-end;justify-content:space-between;border-bottom:.3mm solid var(--rule);padding-bottom:1.6mm}
.rh::after{content:"";position:absolute;left:0;bottom:-.45mm;width:22mm;height:.6mm;background:var(--burg)}
.rh .l{font:600 7.6pt var(--hen);color:var(--sage);letter-spacing:.04em;text-transform:uppercase}
.rh .l b{color:var(--burg);font-weight:700}
.rh .r{font:600 8pt var(--har);color:var(--sage)}
.rf{position:absolute;left:18mm;right:18mm;bottom:9mm;height:7mm;display:flex;align-items:center;justify-content:space-between;border-top:.3mm solid var(--rule);padding-top:1.4mm}
.rf .l{font:600 7.2pt var(--hen);color:var(--muted)} .rf .l b{font:italic 800 9pt var(--en);color:var(--burg);margin-right:1.5mm}
.rf .r{font:500 7.6pt var(--har);color:var(--muted)}
.rf .pn{position:absolute;left:50%;transform:translateX(-50%);top:1.2mm;min-width:9mm;height:6mm;padding:0 2mm;border-radius:3mm;background:var(--burg);color:#fff;font:700 8.5pt var(--hen);display:flex;align-items:center;justify-content:center}
.body{position:absolute;left:18mm;right:18mm;top:24mm;height:252mm;overflow:hidden}
.inner{display:flow-root}
/* --- text */
p.en{font:400 12pt/1.42 var(--en);text-align:justify;hyphens:auto;-webkit-hyphens:auto}
p.ar{font:400 11pt/1.68 var(--ar);color:var(--ink-ar);text-align:justify;margin-top:.8mm;padding-right:3mm;border-right:.7mm solid var(--gold-l)}
p.ar b{font-weight:700}
.pair{margin-bottom:3.2mm;break-inside:avoid}
b.em1{color:var(--burg);font-weight:700}
b.em2{color:var(--burg-d);font-weight:700;background:var(--gold-l);padding:0 .6mm;border-radius:.6mm;box-decoration-break:clone;-webkit-box-decoration-break:clone}
b.term{color:var(--burg);font-weight:700}
i{font-style:italic}
bdi.lat{font-family:var(--en);font-size:1.0em}
.cut{font:italic 500 .82em var(--hen);color:#8A5A00;background:#FFF3D6;border:.25mm dashed #C99A3B;border-radius:1mm;padding:0 1mm;white-space:nowrap}
p.ar .cut{font-family:var(--har);font-style:normal}
span.flag{display:inline-flex;align-items:center;justify-content:center;width:1.25em;height:1.25em;border-radius:50%;background:#C9822B;color:#fff;font:800 .62em/1 var(--hen);vertical-align:.35em;margin:0 .5mm}
/* bullets */
.bl p.en{padding-left:5.5mm;position:relative}
.bl p.en::before{content:"";position:absolute;left:.6mm;top:2.15mm;width:1.9mm;height:1.9mm;background:var(--burg);border-radius:.3mm}
.bl p.ar{margin-left:5.5mm}
.df p.en{padding-left:5.5mm;position:relative}
.df p.en::before{content:"";position:absolute;left:.6mm;top:2.1mm;width:2mm;height:2mm;border:.45mm solid var(--burg);border-radius:50%}
.df p.ar{margin-left:5.5mm}
/* --- opener */
.opener{display:flex;align-items:stretch;gap:5mm;margin:1mm 0 7mm;padding-bottom:4.5mm;border-bottom:.5mm solid var(--burg)}
.op-l{flex:1}
.op-eb{font:600 8.2pt var(--hen);color:var(--sage);letter-spacing:.05em;text-transform:uppercase}
.op-eb.ar{font:600 8.4pt var(--har);text-transform:none;letter-spacing:0;margin-top:.6mm}
.op-en{font:700 22pt/1.15 var(--hen);color:var(--burg-d);margin-top:3mm;letter-spacing:-.01em}
.op-ar{font:700 20pt/1.5 var(--har);color:var(--burg-d);margin-top:1mm}
.op-r{width:24mm;background:var(--burg);color:#fff;border-radius:2mm;display:flex;flex-direction:column;align-items:center;justify-content:center;line-height:1}
.op-r small{font:600 7pt var(--hen);letter-spacing:.16em;opacity:.85}.op-r small[dir=rtl]{font:500 7.5pt var(--har);letter-spacing:0;margin-top:1.4mm}
.op-r b{font:800 30pt var(--hen);margin:1.2mm 0 0}
/* --- headings */
.sec{display:flex;gap:3.2mm;align-items:stretch;margin:4mm 0 3.4mm;padding-bottom:2mm;border-bottom:.3mm solid var(--rule)}
.sn{width:10mm;flex:none;border-radius:1.6mm;background:var(--burg);color:#fff;font:800 14pt var(--hen);display:flex;align-items:center;justify-content:center}
.st{flex:1}
.se{font:700 16pt/1.25 var(--hen);color:var(--burg-d)}
.sa{font:700 14pt/1.6 var(--har);color:var(--sage-d);text-align:right}
.edit{font:500 7pt var(--har);color:var(--muted);border:.25mm solid var(--rule);border-radius:1mm;padding:.2mm 1.4mm;margin-left:3mm;vertical-align:middle}
.h2{margin:4.5mm 0 3mm;padding-left:3.4mm;border-left:1.2mm solid var(--gold)}
.h2e{font:700 14pt/1.25 var(--hen);color:var(--sage-d)}
.h2a{font:600 12pt/1.6 var(--har);color:var(--sage);text-align:right}
/* --- side layout */
.side{display:grid;gap:6mm;align-items:start;margin-bottom:2mm}
.fig{break-inside:avoid;margin:1mm 0 4mm}
.fig img{width:100%;display:block;border-radius:1.4mm;border:.3mm solid var(--rule)}
.fig.sm{margin-top:1mm}
figcaption{margin-top:1.6mm;display:flex;flex-direction:column;gap:.4mm}
figcaption .ce{font:400 10pt/1.3 var(--en);color:var(--muted)} figcaption .ce b{font-family:var(--hen);font-size:9pt;color:var(--burg);font-weight:700}
figcaption .ca{font:400 9pt/1.6 var(--ar);color:var(--muted);text-align:right} figcaption .ca b{color:var(--burg)}
/* --- risk-group table */
table.rg{width:100%;border-collapse:collapse;table-layout:fixed}
table.rg th{background:var(--burg);color:#fff;padding:2.2mm 2.4mm;vertical-align:middle;text-align:left}
table.rg th .te{display:block;font:700 10.5pt/1.25 var(--hen)} table.rg th .ta{display:block;font:600 10pt/1.6 var(--har);text-align:right;margin-top:.6mm;opacity:.95}
table.rg th.nc{text-align:center;font:700 10.5pt var(--hen)}
.thead.cont table.rg th{background:var(--sage)}
table.rg td{border-bottom:.3mm solid var(--rule);padding:2.6mm 2.4mm 2.8mm;vertical-align:top}
table.rg td.lv{background:var(--sage-l)}
table.rg td.lv .te{display:block;font:600 10.5pt/1.3 var(--en)} table.rg td.lv .ta{display:block;white-space:nowrap;font:500 10pt/1.6 var(--ar);text-align:right;margin-top:1mm;color:var(--ink-ar)}
table.rg td.nc{text-align:center;font:800 13pt var(--hen);color:var(--burg)}
.rt{font:600 10.5pt var(--en);color:var(--burg-d);text-align:center}
.rta{font:600 10pt/1.6 var(--ar);color:var(--burg-d);text-align:center;margin-bottom:1.4mm}
.rt b.em1{font-size:1.15em}
p.tc{font-size:10.5pt;line-height:1.38}
p.ar.tc{font-size:10pt;line-height:1.7}
.trow:last-of-type td{border-bottom:.5mm solid var(--burg)}
.thead+.trow td,.trow td{}
/* --- clarification */
.clar{margin:4mm 0 4mm;padding:2.6mm 3.6mm 2.6mm;background:#FBF8F1;border:.3mm dashed var(--gold);border-radius:1.6mm}
.cl-h{display:flex;justify-content:space-between;margin-bottom:1.4mm}
.cl-h [dir=ltr]{font:700 8pt var(--hen);color:var(--gold);letter-spacing:.08em;text-transform:uppercase}
.cl-h [dir=rtl]{font:600 8pt var(--har);color:#8A6A2A}
.clar p.en{font-size:10.5pt}.clar p.ar{font-size:10pt;border-right-color:#EBDDB8}
/* --- short list */
.short{margin:0 0 4mm;border-top:.3mm solid var(--rule)}
.sr{display:grid;grid-template-columns:1fr 1fr;gap:6mm;padding:1.3mm 0;border-bottom:.3mm solid var(--rule);align-items:center}
.se2{font:400 12pt/1.4 var(--en);padding-left:5.5mm;position:relative}
.se2::before{content:"";position:absolute;left:.6mm;top:2.2mm;width:1.9mm;height:1.9mm;background:var(--burg);border-radius:.3mm}
.sa2{font:400 11pt/1.7 var(--ar);color:var(--ink-ar);padding-right:5.5mm;position:relative}
.sa2::before{content:"";position:absolute;right:.6mm;top:2.9mm;width:1.9mm;height:1.9mm;background:var(--gold);border-radius:.3mm}
/* --- symbols */
.syms{display:grid;grid-template-columns:1fr 1fr;gap:10mm;padding:2.4mm 10mm;background:var(--sage-l);border-radius:2mm}
.sym{text-align:center}.sym img{width:auto;height:27mm;margin:1.6mm auto 0;border:none;border-radius:0}
.sl{font:800 10.5pt var(--hen);color:#B01C1C;letter-spacing:.04em}.sla{font:700 10pt var(--har);color:var(--ink-ar)}
/* --- rules */
.rule{display:grid;grid-template-columns:8mm 1fr;gap:2.4mm;margin-bottom:3.2mm}
.rn{width:7.2mm;height:7.2mm;border-radius:50%;border:.45mm solid var(--burg);color:var(--burg);font:800 10pt var(--hen);display:flex;align-items:center;justify-content:center;margin-top:.4mm}
.rule p.en,.side p.en{text-align:left}
.clr{clear:both}
.rgrp{clear:both;padding-top:2.6mm;border-top:.3mm dotted var(--rule)}
.fig.fl figcaption.tag{position:absolute;left:1.4mm;bottom:1.4mm;display:flex;flex-direction:row;gap:1.6mm;margin:0;background:rgba(110,31,42,.92);color:#fff;border-radius:1mm;padding:.5mm 1.8mm;font:700 7.2pt/1.5 var(--hen)}
.fig.fl figcaption.tag [dir=rtl]{font:600 7.2pt/1.5 var(--har)}
.fig.fl{position:relative;float:right;width:46mm;margin:.6mm 0 3mm 6mm}
/* --- cabinet */
.cab{position:relative}
.mk{position:absolute;transform:translate(-50%,-50%);width:5mm;height:5mm;border-radius:50%;background:var(--burg);color:#fff;font:800 7.6pt var(--hen);display:flex;align-items:center;justify-content:center;border:.4mm solid #fff;box-shadow:0 0 0 .2mm var(--burg)}
.labs{display:grid;grid-template-columns:1fr 1fr;gap:5mm;align-items:start}
table.lab{width:100%;border-collapse:collapse;table-layout:fixed}
table.lab th{color:#fff;background:var(--sage);padding:1.5mm 2.2mm;text-align:left}
table.lab th span{display:block;font:700 10.5pt var(--hen)} table.lab th span.a{font:600 10pt/1.5 var(--har);text-align:right}
table.lab td{padding:1.1mm 2.2mm;border-bottom:.3mm solid var(--rule);vertical-align:top}
table.lab .le{display:block;font:600 10.5pt/1.3 var(--en)}
table.lab .la{display:block;font:400 10pt/1.5 var(--ar);text-align:right;color:var(--ink-ar)}
table.lab .n{width:8mm;text-align:center;font:800 10pt var(--hen);color:var(--burg);vertical-align:middle}
table.lab tbody tr:nth-child(even) td{background:#FAFAF8}
.hid.dn{margin:1.4mm 0 0 5.5mm}
.hid{display:flex;flex-direction:column;gap:.6mm;margin-top:2mm}
.hid [dir=ltr]{font:italic 400 9.5pt/1.35 var(--en);color:var(--muted)}.hid [dir=rtl]{font:400 9pt/1.6 var(--ar);color:var(--muted)}
/* --- review box */
.review{margin-top:6mm;border:.35mm solid #E2C9A0;background:#FFFBF3;border-radius:1.6mm;padding:3mm 4mm 1mm}
.rv-h{display:flex;justify-content:space-between;margin-bottom:2mm}
.rv-h [dir=ltr]{font:700 9pt var(--hen);color:#8A5A00;text-transform:uppercase;letter-spacing:.06em}.rv-h [dir=rtl]{font:700 9.5pt var(--har);color:#8A5A00}
.review ol{list-style:none;counter-reset:r}
.review li{counter-increment:r;position:relative;padding-left:6mm;margin-bottom:2.2mm}
.review li::before{content:counter(r);position:absolute;left:0;top:.6mm;font:800 9pt var(--hen);color:#8A5A00}
.review p.en{font-size:10.5pt}.review p.ar{font-size:10pt;border-right-color:#EBDDB8}
/* --- notes */
.notes{position:absolute;left:0;right:0;bottom:0;border-top:.3mm solid var(--rule);padding-top:2mm}
.notes .nh{display:flex;justify-content:space-between;font:700 8pt var(--hen);color:var(--sage);letter-spacing:.08em;text-transform:uppercase}
.notes .nh span[dir=rtl]{font:600 8.5pt var(--har);letter-spacing:0;text-transform:none}
.notes .ln{height:8mm;border-bottom:.25mm dashed #CFCAC0}
/* --- cover */
.cover{background:linear-gradient(180deg,#EAE0D4 0%,#EAE0D4 34%,#EEE7DD 62%,#E8DED1 100%)}
.cv-wm{position:absolute;right:-52mm;top:128mm;width:150mm;height:150mm}
.cv-top{position:absolute;left:0;right:0;top:12mm;text-align:center}
.cv-logo{width:84mm;-webkit-mask-image:radial-gradient(closest-side,#000 70%,transparent 100%);mask-image:radial-gradient(closest-side,#000 70%,transparent 100%)}
.cv-mid{position:absolute;left:20mm;right:20mm;top:96mm;text-align:center}
.cv-eyebrow{display:flex;justify-content:center;gap:3mm;align-items:center;font:700 10pt var(--hen);color:var(--sage);letter-spacing:.12em;text-transform:uppercase}
.cv-eyebrow [dir=rtl]{font:700 11pt var(--har);letter-spacing:0}
.cv-eyebrow .dot{color:var(--gold)}
.cv-t-en{font:800 30pt/1.1 var(--hen);color:var(--burg-d);margin-top:6mm;letter-spacing:-.015em}
.cv-t-ar{font:800 26pt/1.5 var(--har);color:var(--burg);margin-top:2mm}
.cv-badges{display:flex;justify-content:center;gap:3mm;margin-top:5mm}
.bd{font:700 9.5pt var(--hen);padding:1.4mm 4.5mm;border-radius:5mm;display:inline-flex;gap:2mm;align-items:center;direction:ltr}.bd i{font-style:normal;opacity:.7}.bd [dir=rtl]{font-family:var(--har)}
.bd.b1{background:var(--burg);color:#fff}.bd.b2{border:.4mm solid var(--sage);color:var(--sage-d)}
.cv-art{position:absolute;left:30mm;right:30mm;top:160mm;height:56mm;display:flex;align-items:flex-end;justify-content:center;gap:16mm}
.cv-cab svg{width:58mm;display:block}
.ladder{display:flex;align-items:flex-end;gap:2mm;height:34mm}
.step{width:10mm;border-radius:1.2mm 1.2mm 0 0;display:flex;align-items:flex-start;justify-content:center;padding-top:1.4mm}
.step b{font:800 10pt var(--hen);color:#fff}
.ladder-cap{display:flex;flex-direction:column;align-items:center;margin-top:1.6mm;font:600 7.5pt var(--hen);color:var(--sage)}
.ladder-cap [dir=rtl]{font:600 7.8pt var(--har)}
.cv-lad{display:flex;flex-direction:column;align-items:center;padding-bottom:2mm}
.cv-info{position:absolute;left:18mm;right:18mm;top:229mm;display:grid;grid-template-columns:repeat(5,1fr);gap:2.4mm}
.ic{background:rgba(255,255,255,.62);border:.3mm solid #DCCFBC;border-top:.9mm solid var(--burg);border-radius:1.4mm;padding:2mm 2.2mm;min-height:19mm}
.ik{display:flex;flex-direction:column;gap:.3mm;font:700 6.8pt var(--hen);color:var(--muted);text-transform:uppercase;letter-spacing:.06em}
.ik [dir=rtl]{font:600 7.4pt var(--har);text-transform:none;letter-spacing:0;text-align:right}
.iv{margin-top:1.6mm;display:flex;flex-direction:column;gap:.3mm}
.iv [dir=ltr]{font:600 8.6pt/1.25 var(--en);color:var(--ink)}
.iv [dir=rtl]{font:700 9pt/1.5 var(--har);color:var(--burg-d);text-align:right}
.cv-foot{position:absolute;left:0;right:0;bottom:0;height:13mm;background:var(--burg);display:flex;align-items:center;gap:3mm;padding:0 18mm;color:#fff;font:500 8.6pt var(--har)}
.cv-foot .w{font:italic 800 14pt var(--en);letter-spacing:.03em}.cv-foot .sp{flex:1}
.cv-foot [dir=ltr]{font:500 8.6pt var(--hen)}
"""

PAGINATE = r"""
function mkPage(n){
  const s=document.createElement('section');s.className='page';
  s.innerHTML=`<div class="rh"><span class="l"><b>BIOS</b> · Diagnostic Microbiology · Lab 1</span><span class="r" dir="rtl">الأحياء المجهرية التشخيصية · المختبر 1</span></div>
  <div class="body"><div class="inner"></div></div>
  <div class="rf"><span class="l"><b>BIOS</b>Rules and biosafety levels</span><span class="pn">${n}</span><span class="r" dir="rtl">ترجمة وتعديل الملازم · Telegram: BIOS0t</span></div>`;
  document.getElementById('pages').appendChild(s);return s;}
function fits(p){const b=p.querySelector('.body'),i=p.querySelector('.inner');return i.getBoundingClientRect().height<=b.clientHeight+0.5;}
function paginate(){
  const flow=document.getElementById('flow');const blocks=[...flow.children];
  const head=flow.querySelector('.thead');
  let n=1,p=mkPage(n),inner=p.querySelector('.inner');const log=[];
  for(const b of blocks){
    inner.appendChild(b);
    if(fits(p))continue;
    inner.removeChild(b);const carry=[b];
    while(inner.lastElementChild&&inner.lastElementChild.classList.contains('keep')){carry.unshift(inner.lastElementChild);inner.removeChild(inner.lastElementChild);}
    if(!inner.children.length){carry.slice(0,-1).forEach(x=>inner.appendChild(x));carry.splice(0,carry.length-1);}
    p=mkPage(++n);inner=p.querySelector('.inner');
    if(carry[0].classList.contains('trow')){const h=head.cloneNode(true);h.classList.add('cont');inner.appendChild(h);}
    carry.forEach(x=>inner.appendChild(x));
    if(!fits(p))log.push('OVERFLOW on page '+n);
  }
  // notes area: only where a page ends at a section boundary (or the end) with real space left
  const pages=[...document.querySelectorAll('#pages .page')];
  pages.forEach((pg,i)=>{
    const body=pg.querySelector('.body'),inr=pg.querySelector('.inner');
    const free=body.clientHeight-inr.getBoundingClientRect().height;
    const nxt=pages[i+1]?pages[i+1].querySelector('.inner').firstElementChild:null;
    const boundary=!nxt||nxt.querySelector('.sec,.h2');
    const mm=free*25.4/96;
    log.push(`page ${i+1}: free ${mm.toFixed(1)}mm${boundary?' (boundary)':''}`);
    if(boundary&&mm>=30){
      const lines=Math.min(14,Math.floor((mm-12)/8));
      const d=document.createElement('div');d.className='notes';
      d.innerHTML='<div class="nh"><span>Notes</span><span dir="rtl">ملاحظات</span></div>'+'<div class="ln"></div>'.repeat(lines);
      body.appendChild(d);
    }
  });
  window.__log=log;window.__done=true;
}
document.fonts.ready.then(()=>Promise.all([...document.images].map(i=>i.complete?1:new Promise(r=>{i.onload=i.onerror=r})))).then(()=>setTimeout(paginate,50));
"""

def build():
    blocks = "".join(R[k](kw) for k, kw in B)
    doc = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>BIOS · Diagnostic Microbiology · Lab 1</title>'
           f'<style>{CSS}</style></head><body>{cover()}<div id="pages"></div><div id="flow">{blocks}</div>'
           f'<script>{PAGINATE}</script></body></html>')
    open("booklet4.html", "w").write(doc)
    print("figures:", FIG["n"], "blocks:", len(B))

if __name__ == "__main__":
    build()
