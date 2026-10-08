import re, html
from art2 import icon, corner, divider

AR_DIGITS = str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩")
def ard(n): return str(n).translate(AR_DIGITS)

def md(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r'<b class="term">\1</b>', s)
    s = re.sub(r"!!(.+?)!!", r'<b class="em">\1</b>', s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", s)
    s = re.sub(r"`(.+?)`", r'<bdi dir="ltr" class="lt">\1</bdi>', s)
    s = s.replace("[[cut]]", '<span class="cut" dir="ltr">text cut off in the original file</span>')
    s = s.replace("[[قطع]]", '<span class="cut">النص مقطوع في الملف الأصلي</span>')
    return s

def en(s, cls=""): return f'<p class="en {cls}" dir="ltr">{md(s)}</p>'
def ar(s, cls=""): return f'<p class="ar {cls}" dir="rtl">{md(s)}</p>'

def card(e, a, cls=""):
    """English on paper, Arabic on parchment band directly underneath."""
    return (f'<div class="card {cls}"><div class="c-en"><span class="tag">EN</span>{en(e)}</div>'
            f'<div class="c-ar"><span class="tag tag-ar">ع</span>{ar(a)}</div></div>')

def pair(e, a, cls=""):
    return f'<div class="pair {cls}">{en(e)}{ar(a)}</div>'

def cards(items): return "".join(card(e, a) for e, a in items)

NUMW = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
NUMA = ["الأول", "الثاني", "الثالث", "الرابع", "الخامس", "السادس", "السابع", "الثامن", "التاسع"]

def sec(num, e, a, ico="lab", eyebrow=None):
    if eyebrow is None:
        eyebrow = (f"SECTION {NUMW[int(num) - 1]}", f"القسم {NUMA[int(num) - 1]}") if str(num).isdigit() else ("REVIEW", "مراجعة")
    n = f"{int(num):02d}" if str(num).isdigit() else num
    return (f'<div class="sec"><div class="sec-n">{n}</div><div class="sec-b">'
            f'<div class="sec-eb"><span dir="ltr">{eyebrow[0]}</span><span class="dot">✦</span><span dir="rtl">{eyebrow[1]}</span></div>'
            f'<div class="sec-t"><span class="sec-en" dir="ltr">{md(e)}</span><span class="sec-ar" dir="rtl">{md(a)}</span></div>'
            f'</div><div class="sec-ic">{icon(ico, "#B38B4D", "100%", 1.4)}</div></div>')

def h2(e, a):
    return (f'<div class="h2"><span class="h2-en" dir="ltr">{md(e)}</span><span class="h2-line"></span>'
            f'<span class="h2-ar" dir="rtl">{md(a)}</span></div>')

def plain(items):
    out = "".join(f'<li><div class="p-en" dir="ltr"><span class="mk">◆</span>{md(e)}</div>'
                  f'<div class="p-ar" dir="rtl"><span class="mk">◆</span>{md(a)}</div></li>' for e, a in items)
    return f'<ul class="plain">{out}</ul>'

def rules(items, start=1, icons=None):
    out = []
    for i, (e, a) in enumerate(items, start):
        ic = icon(icons[i - start], "#F3E6CC", "100%", 1.5) if icons else ""
        out.append(f'<div class="rule"><div class="r-med"><div class="r-ic">{ic}</div><span class="r-n">{i}</span></div>{card(e, a)}</div>')
    return "".join(out)

BOX = {
    "note":    ("bulb",  "BIOS Note", "ملاحظة بايوس"),
    "alert":   ("alert", "Exam Alert", "تنبيه امتحاني"),
    "sci":     ("search", "Scientific Note", "ملاحظة علمية"),
    "memory":  ("brain", "Memory Tip", "طريقة للحفظ"),
    "compare": ("scale", "Compare", "مقارنة"),
    "key":     ("key",   "Key Points", "أهم النقاط"),
}

def box(kind, body, title=None):
    ico, te, ta = BOX[kind]
    if title: te, ta = title
    return (f'<div class="box box-{kind}"><div class="box-h"><span class="box-ic">{icon(ico, "currentColor", "100%", 1.6)}</span>'
            f'<span class="box-te" dir="ltr">{te}</span><span class="box-ln"></span><span class="box-ta" dir="rtl">{ta}</span></div>'
            f'<div class="box-b">{body}</div></div>')

FIG = {"n": 0}
def fig(src, ce, ca, w="120mm", inner=None, cls=""):
    FIG["n"] += 1
    n = FIG["n"]
    body = inner if inner is not None else f'<img src="{src}">'
    return (f'<figure class="fig {cls}" style="width:{w}"><div class="fig-fr">{body}</div>'
            f'<figcaption><span dir="ltr"><b>Figure {n}.</b> {md(ce)}</span><span dir="rtl"><b>الشكل {ard(n)}.</b> {md(ca)}</span></figcaption></figure>')

def figrow(*f): return '<div class="figrow">' + "".join(f) + "</div>"

FONTS = """
@font-face{font-family:Mada;src:url(fonts/Mada-Light.ttf);font-weight:300}
@font-face{font-family:Mada;src:url(fonts/Mada-Regular.ttf);font-weight:400}
@font-face{font-family:Mada;src:url(fonts/Mada-Medium.ttf);font-weight:500}
@font-face{font-family:Mada;src:url(fonts/Mada-SemiBold.ttf);font-weight:600}
@font-face{font-family:Mada;src:url(fonts/Mada-Bold.ttf);font-weight:700}
@font-face{font-family:Mada;src:url(fonts/Mada-ExtraBold.ttf);font-weight:800}
@font-face{font-family:Mada;src:url(fonts/Mada-Black.ttf);font-weight:900}
@font-face{font-family:AmiriQ;src:url(fonts/AmiriQuran-Regular.ttf)}
@font-face{font-family:Playfair;src:url(fonts/playfair-display-latin-400-normal.woff2);font-weight:400}
@font-face{font-family:Playfair;src:url(fonts/playfair-display-latin-400-italic.woff2);font-weight:400;font-style:italic}
@font-face{font-family:Playfair;src:url(fonts/playfair-display-latin-700-normal.woff2);font-weight:700}
@font-face{font-family:Playfair;src:url(fonts/playfair-display-latin-700-italic.woff2);font-weight:700;font-style:italic}
@font-face{font-family:Playfair;src:url(fonts/playfair-display-latin-900-normal.woff2);font-weight:900}
@font-face{font-family:Playfair;src:url(fonts/playfair-display-latin-900-italic.woff2);font-weight:900;font-style:italic}
@font-face{font-family:Cormorant;src:url(fonts/cormorant-garamond-latin-500-normal.woff2);font-weight:500}
@font-face{font-family:Cormorant;src:url(fonts/cormorant-garamond-latin-500-italic.woff2);font-weight:500;font-style:italic}
@font-face{font-family:Cormorant;src:url(fonts/cormorant-garamond-latin-600-normal.woff2);font-weight:600}
@font-face{font-family:Cormorant;src:url(fonts/cormorant-garamond-latin-600-italic.woff2);font-weight:600;font-style:italic}
@font-face{font-family:Cormorant;src:url(fonts/cormorant-garamond-latin-700-normal.woff2);font-weight:700}
"""

CSS = FONTS + r"""
:root{
  --paper:#FBF8F2; --ivory:#F6EFE3; --parch:#F2E8D8; --line:#E4D6BD; --line2:#D8C39E;
  --burg:#6B1E2A; --burg-d:#4A131B; --wine:#8E3341; --rose:#F5E6E4;
  --gold:#B38B4D; --gold-d:#8C6A33; --gold-l:#D9C08E; --gold-ll:#EFE3C8;
  --ink:#2A201E; --ink-ar:#3B2723; --muted:#8C7D72;
}
*{box-sizing:border-box;margin:0;padding:0}
@page{size:A4;margin:0}
html,body{background:#cfc6b8}
body{font-variant-numeric:lining-nums;font-family:Mada,sans-serif;color:var(--ink);-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:210mm;height:297mm;position:relative;overflow:hidden;background:var(--paper);display:flex;flex-direction:column;break-after:page}
@media screen{.page{margin:8mm auto;box-shadow:0 4px 24px rgba(0,0,0,.18)}}
/* frame */
.fr1{position:absolute;inset:6.5mm;border:.35mm solid var(--gold-l);pointer-events:none}
.fr2{position:absolute;inset:7.6mm;border:.15mm solid var(--gold-ll);pointer-events:none}
.cn{position:absolute;width:11mm;height:11mm;line-height:0}
.cn.tl{left:5mm;top:5mm}.cn.tr{right:5mm;top:5mm}.cn.bl{left:5mm;bottom:5mm}.cn.br{right:5mm;bottom:5mm}
/* header */
.hdr{height:25mm;padding:11.5mm 15mm 0;display:grid;grid-template-columns:1fr auto 1fr;align-items:center;gap:4mm}
.brand{display:flex;align-items:baseline;gap:2mm}
.brand .bw{font-family:Playfair;font-weight:900;font-style:italic;font-size:15pt;color:var(--burg);letter-spacing:.01em}
.brand .ba{font-weight:700;font-size:9pt;color:var(--gold-d);border-left:.3mm solid var(--gold-l);padding-left:2mm}
.hc{text-align:center;line-height:1.15}
.hc .t1{font-family:Cormorant;font-weight:700;font-size:10pt;letter-spacing:.22em;color:var(--burg);text-transform:uppercase}
.hc .t2{font-weight:600;font-size:8.6pt;color:var(--gold-d)}
.hr{justify-self:end;display:flex;align-items:center;gap:2mm;font-size:8.6pt;font-weight:700;color:var(--burg)}
.hr .lab{font-family:Playfair;font-style:italic;font-weight:700;font-size:10.5pt}
.hr .sep{width:1.6mm;height:1.6mm;background:var(--gold);transform:rotate(45deg)}
.orn{padding:1.4mm 15mm 0;display:flex;align-items:center;gap:0}.orn .ol{flex:1;border-top:.3mm solid var(--gold-l)}.orn svg{margin:0 2mm!important;width:30mm}
/* body + footer */
.body{flex:1;display:flex;flex-direction:column;padding:3.5mm 16mm 0;min-height:0}
.content{flex:0 0 auto}
.ftr{height:21mm;padding:0 15mm 9.5mm;display:grid;grid-template-columns:1fr auto 1fr;align-items:end;font-size:8.4pt;color:var(--muted);font-weight:600}
.ftr .fl{display:flex;gap:2mm;align-items:center}
.ftr .fl b{font-family:Playfair;font-style:italic;font-weight:900;color:var(--burg);font-size:10pt}
.ftr .fr{justify-self:end;display:flex;gap:1.5mm;align-items:center}
.ftr .fr b{color:var(--burg)}
.ftr .pg{width:11mm;height:11mm;position:relative;display:flex;align-items:center;justify-content:center;margin-bottom:-2mm}
.ftr .pg::before{content:"";position:absolute;inset:1.6mm;border:.35mm solid var(--gold);transform:rotate(45deg);background:var(--burg)}
.ftr .pg span{position:relative;font-family:Playfair;font-weight:700;font-size:10.5pt;color:#F6EAD2}
/* section opener */
.sec{display:flex;align-items:center;gap:4mm;margin:.5mm 0 3.4mm;padding-bottom:2.4mm;border-bottom:.35mm solid var(--gold-l);position:relative}
.sec::after{content:"";position:absolute;left:0;bottom:-.9mm;width:28mm;height:1.5mm;background:var(--burg)}
.sec-n{font-family:Playfair;font-weight:900;font-style:italic;font-size:34pt;line-height:.9;color:var(--gold)}
.sec-b{flex:1}
.sec-eb{display:flex;gap:2mm;align-items:center;font-family:Cormorant;font-weight:700;font-size:8.5pt;letter-spacing:.28em;color:var(--gold-d)}
.sec-eb [dir=rtl]{font-family:Mada;letter-spacing:0;font-size:8.5pt}
.sec-eb .dot{font-size:7pt;color:var(--gold)}
.sec-t{display:flex;justify-content:space-between;align-items:baseline;gap:4mm;margin-top:.6mm}
.sec-en{font-family:Playfair;font-weight:700;font-size:19pt;color:var(--burg);line-height:1.1}
.sec-ar{font-weight:800;font-size:18pt;color:var(--burg-d);line-height:1.3}
.sec-ic{width:10mm;height:10mm;flex:none}
.h2{display:flex;align-items:center;gap:3mm;margin:3mm 0 3mm}
.h2-en{font-family:Playfair;font-style:italic;font-weight:700;font-size:13.5pt;color:var(--burg)}
.h2-ar{font-weight:800;font-size:13pt;color:var(--burg)}
.h2-line{flex:1;height:0;border-top:.3mm dashed var(--gold-l)}
/* text */
.en{font-size:14pt;line-height:1.45;text-align:left}
.ar{font-family:AmiriQ,serif;font-size:14pt;line-height:1.8;color:var(--ink-ar);text-align:right}
b.term{font-weight:700;color:var(--burg)}
.ar b.term,.ar b.em{font-family:Mada;font-weight:700;font-size:.95em}
b.em{font-weight:800;color:var(--wine);text-decoration:underline;text-decoration-color:var(--gold-l);text-underline-offset:1mm}
i{font-style:italic}
.ar i,.ar bdi{font-family:Mada}
bdi.lt{unicode-bidi:isolate;white-space:nowrap}
.cut{display:inline-block;font-family:Mada;font-size:8.5pt;font-weight:700;color:var(--gold-d);border:.3mm dashed var(--gold);background:#FFF9EA;border-radius:1.2mm;padding:0 1.6mm;margin:0 1mm;vertical-align:middle;line-height:1.6}
/* card */
.card{border:.3mm solid var(--line);border-radius:2.4mm;overflow:hidden;margin:0 0 3mm;background:#fff;break-inside:avoid}
.c-en{position:relative;padding:2mm 4mm 1.8mm 12mm}
.c-ar{position:relative;padding:1mm 12mm 1.2mm 4mm;background:var(--parch);border-top:.3mm dashed var(--line2)}
.tag{position:absolute;left:3.2mm;top:2.9mm;font-family:Cormorant;font-weight:700;font-size:7.5pt;letter-spacing:.12em;color:var(--gold-d);border:.3mm solid var(--gold-l);border-radius:1mm;padding:0 1mm;line-height:1.5}
.tag-ar{left:auto;right:3.4mm;top:2.6mm;font-family:Mada;letter-spacing:0;font-size:8pt;padding:0 1.4mm}
.pair{margin:0 0 3mm}
/* plain list */
ul.plain{list-style:none;margin:0 0 2mm}
ul.plain li{margin:0 0 2mm;break-inside:avoid}
.p-en{font-size:14pt;line-height:1.45;padding-left:6.5mm;position:relative}
.p-ar{font-family:AmiriQ;font-size:14pt;line-height:1.85;color:var(--ink-ar);padding-right:6.5mm;position:relative}
.mk{position:absolute;font-size:8pt;color:var(--gold);top:1.6mm}
.p-en .mk{left:1mm}.p-ar .mk{right:1mm;top:2.6mm;color:var(--burg)}
/* numbered rules */
.rule{display:flex;gap:3.5mm;align-items:flex-start;break-inside:avoid}
.rule .card{flex:1}
.r-med{flex:none;width:13mm;height:13mm;border-radius:50%;background:var(--burg);position:relative;box-shadow:0 0 0 .5mm var(--paper),0 0 0 .85mm var(--gold);margin-top:1mm}
.r-ic{position:absolute;inset:2.8mm}
.r-n{position:absolute;right:-1.6mm;bottom:-1.4mm;width:5.6mm;height:5.6mm;border-radius:50%;background:var(--gold);color:#fff;font-family:Playfair;font-weight:700;font-size:9pt;display:flex;align-items:center;justify-content:center;border:.4mm solid var(--paper)}
/* boxes */
.box{border-radius:2.4mm;margin:1mm 0 3.4mm;break-inside:avoid;border:.3mm solid var(--line);background:#fff;overflow:hidden}
.box-h{display:flex;align-items:center;gap:2mm;padding:1.6mm 4mm;font-size:9.5pt;font-weight:800;letter-spacing:.06em}
.box-h .box-te{font-family:Cormorant;font-weight:700;font-size:10.5pt;letter-spacing:.16em;text-transform:uppercase}
.box-ic{width:4.6mm;height:4.6mm;display:inline-flex}
.box-ln{flex:1;border-top:.3mm dotted currentColor;opacity:.45}
.box-b{padding:1.4mm 4.5mm .6mm}
.box-b .pair{margin-bottom:2.2mm}
.box-note{background:#FFFBF1;border-color:var(--gold-l)}.box-note .box-h{color:var(--gold-d)}
.box-alert{background:#FCF4F3;border-color:#E6C4C3}.box-alert .box-h{color:var(--wine)}
.box-memory{background:#FBF7EE;border:.35mm dashed var(--gold-l)}.box-memory .box-h{color:var(--gold-d)}
.box-compare,.box-key{background:#fff;border-color:var(--gold-l)}
.box-compare .box-h,.box-key .box-h{background:var(--burg);color:#F3E3C4}
.box-sci{background:#F8F5EF}.box-sci .box-h{color:var(--burg)}
/* figures */
.fig{margin:1mm auto 3.6mm;break-inside:avoid}
.fig-fr{background:#fff;padding:1.6mm;border:.3mm solid var(--gold-l);border-radius:1.6mm;box-shadow:0 1.6mm 4mm rgba(74,19,27,.08);position:relative}
.fig-fr img{display:block;width:100%;height:auto;border-radius:.8mm}
figcaption{display:flex;justify-content:space-between;gap:4mm;margin-top:1.4mm;font-size:9.5pt;color:var(--muted);font-weight:500}
figcaption [dir=ltr]{font-family:Cormorant;font-style:italic;font-size:11pt;font-weight:600}
figcaption b{color:var(--burg);font-style:normal;font-weight:700}
figcaption [dir=ltr] b{font-family:Playfair;font-style:italic;font-size:9.5pt}
.figrow{display:flex;justify-content:space-around;align-items:flex-start;gap:5mm}
.figrow .fig{margin:1mm 0 3.6mm}
/* notes */
.notes{flex:1 1 auto;min-height:50mm;margin-top:3mm;display:flex;flex-direction:column;padding-bottom:.5mm}
.notes-h{display:flex;align-items:center;gap:2.5mm;margin-bottom:.6mm}
.notes-h .ne{font-family:Playfair;font-style:italic;font-weight:700;font-size:11pt;color:var(--burg)}
.notes-h .na{font-weight:700;font-size:10pt;color:var(--burg)}
.notes-h .ln{flex:1;border-top:.3mm solid var(--gold-l)}
.notes-h .qi{width:4.5mm;height:4.5mm}
.notes-lines{flex:1;min-height:41mm;background:repeating-linear-gradient(to bottom,transparent 0,transparent calc(8.2mm - .25mm),#DCCBAA calc(8.2mm - .25mm),#DCCBAA 8.2mm);background-size:100% 8.2mm}
.muted{color:var(--muted)}
"""

CORNERS = (f'<div class="cn tl">{corner(11)}</div><div class="cn tr">{corner(11, rot=90)}</div>'
           f'<div class="cn br">{corner(11, rot=180)}</div><div class="cn bl">{corner(11, rot=270)}</div>')

def page(content, hdr, num, notes=True, cls=""):
    notes_html = ('<div class="notes"><div class="notes-h">'
                  f'<span class="qi">{icon("quill", "#B38B4D", "100%", 1.5)}</span><span class="ne" dir="ltr">Student Notes</span>'
                  '<span class="ln"></span><span class="na" dir="rtl">ملاحظات الطالب</span></div>'
                  '<div class="notes-lines"></div></div>') if notes else ""
    ftr = ('<div class="ftr"><div class="fl"><b>BIOS</b><span>|</span><span>بايوس</span><span>·</span><span>ترجمة وتعديل الملازم</span></div>'
           f'<div class="pg"><span>{num}</span></div>'
           f'<div class="fr"><span class="pl" style="width:3.6mm;height:3.6mm;display:inline-flex">{icon("plane", "#8C7D72", "100%", 1.6)}</span>'
           '<span>Telegram:</span><b>BIOS0t</b></div></div>')
    return (f'<section class="page {cls}" data-num="{num}"><div class="fr1"></div><div class="fr2"></div>{CORNERS}{hdr}'
            f'<div class="orn"><span class="ol"></span>{divider("30mm")}<span class="ol"></span></div><div class="body"><div class="content">{content}</div>{notes_html}</div>{ftr}</section>')

def doc(title, pages, extra_css=""):
    return (f'<!doctype html><html><head><meta charset="utf-8"><title>{title}</title>'
            f'<style>{CSS}{extra_css}</style></head><body>{"".join(pages)}</body></html>')
