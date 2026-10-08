import re, html

AR_DIGITS = str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩")

def ard(n):
    return str(n).translate(AR_DIGITS)

def md(s):
    """Tiny inline markup.
    `x`   -> isolated LTR run (for Latin inside Arabic)
    **x** -> highlighted term
    *x*   -> italic (scientific names)
    !!x!! -> emphasis (key qualifier)
    """
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r'<b class="term">\1</b>', s)
    s = re.sub(r"!!(.+?)!!", r'<b class="em">\1</b>', s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", s)
    s = re.sub(r"`(.+?)`", r'<bdi dir="ltr" class="lt">\1</bdi>', s)
    return s

def en(s, cls=""):
    return f'<p class="en {cls}" dir="ltr">{md(s)}</p>'

def ar(s, cls=""):
    return f'<p class="ar {cls}" dir="rtl">{md(s)}</p>'

def pair(e, a, cls=""):
    return f'<div class="pair {cls}">{en(e)}{ar(a)}</div>'

def sec(num, e, a, icon=""):
    return (f'<div class="sec"><div class="sec-num">{num}</div>'
            f'<div class="sec-t"><div class="sec-en" dir="ltr">{md(e)}</div>'
            f'<div class="sec-ar" dir="rtl">{md(a)}</div></div>'
            f'<div class="sec-ico">{icon}</div></div>')

def h2(e, a):
    return (f'<div class="h2"><span class="h2-en" dir="ltr">{md(e)}</span>'
            f'<span class="h2-ar" dir="rtl">{md(a)}</span></div>')

def ul(items):
    out = []
    for e, a in items:
        out.append(f'<li><div class="li-en" dir="ltr"><span class="mk"></span>{md(e)}</div>'
                   f'<div class="li-ar" dir="rtl"><span class="mk"></span>{md(a)}</div></li>')
    return '<ul class="bl">' + "".join(out) + "</ul>"

def ol(items, start=1):
    out = []
    for i, (e, a) in enumerate(items, start):
        out.append(f'<li><div class="li-en" dir="ltr"><span class="nb">{i}</span>{md(e)}</div>'
                   f'<div class="li-ar" dir="rtl"><span class="nb">{ard(i)}</span>{md(a)}</div></li>')
    return '<ol class="nl">' + "".join(out) + "</ol>"

BOX = {
    "note":    ("💡", "BIOS Note", "ملاحظة"),
    "alert":   ("⚠️", "Exam Alert", "تنبيه امتحاني"),
    "sci":     ("🔬", "Scientific Note", "ملاحظة علمية"),
    "memory":  ("🧠", "Memory Tip", "طريقة للحفظ"),
    "compare": ("⚖️", "Compare", "مقارنة"),
    "key":     ("🔑", "KEY POINTS", "أهم النقاط"),
}

def box(kind, body, title=None):
    ico, te, ta = BOX[kind]
    if title: te, ta = title
    return (f'<div class="box box-{kind}"><div class="box-h"><span class="box-ico">{ico}</span>'
            f'<span class="box-te" dir="ltr">{te}</span><span class="box-ta" dir="rtl">{ta}</span></div>'
            f'<div class="box-b">{body}</div></div>')

def fig(src, ce, ca, w="120mm", cls=""):
    return (f'<figure class="fig {cls}" style="width:{w}"><div class="fig-frame"><img src="{src}"></div>'
            f'<figcaption><span dir="ltr">{md(ce)}</span><span dir="rtl">{md(ca)}</span></figcaption></figure>')

def figrow(*figs):
    return '<div class="figrow">' + "".join(figs) + "</div>"

FONTS = """
@font-face{font-family:Mada;src:url(fonts/Mada-Light.ttf);font-weight:300}
@font-face{font-family:Mada;src:url(fonts/Mada-Regular.ttf);font-weight:400}
@font-face{font-family:Mada;src:url(fonts/Mada-Medium.ttf);font-weight:500}
@font-face{font-family:Mada;src:url(fonts/Mada-SemiBold.ttf);font-weight:600}
@font-face{font-family:Mada;src:url(fonts/Mada-Bold.ttf);font-weight:700}
@font-face{font-family:Mada;src:url(fonts/Mada-ExtraBold.ttf);font-weight:800}
@font-face{font-family:Mada;src:url(fonts/Mada-Black.ttf);font-weight:900}
@font-face{font-family:AmiriQ;src:url(fonts/AmiriQuran-Regular.ttf)}
"""

CSS = FONTS + r"""
:root{
  --moon:#4C9DB0; --moon-d:#2C6D7D; --moon-dd:#1E4D59;
  --van:#FFEBAF; --cream:#FCFDC8; --wis:#C69FD5; --wis-d:#7A4E8F; --wis-l:#EFE3F4;
  --ink:#1B2B31; --ink-ar:#20414A; --paper:#FFFEF7; --line:#BFDCE3;
  --acc:var(--moon); --acc-d:var(--moon-d);
}
*{box-sizing:border-box;margin:0;padding:0}
@page{size:A4;margin:0}
html,body{background:#d9d4c7}
body{font-family:Mada,sans-serif;color:var(--ink);-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:210mm;height:297mm;position:relative;overflow:hidden;background:var(--paper);
  display:flex;flex-direction:column;page-break-after:always;break-after:page;margin:0 auto}
@media screen{.page{margin:8mm auto;box-shadow:0 4px 24px rgba(0,0,0,.18)}}
/* frame */
.frame{position:absolute;inset:7mm;border:0.35mm solid rgba(76,157,176,.35);border-radius:5mm;pointer-events:none}
.frame::before,.frame::after{content:"";position:absolute;width:2.6mm;height:2.6mm;border-radius:50%;background:var(--wis);top:-1.45mm;left:18mm}
.frame::after{left:auto;right:18mm;top:auto;bottom:-1.45mm;background:var(--moon)}
/* header */
.hdr{height:24mm;padding:11mm 15mm 0;display:flex;align-items:center;justify-content:space-between;gap:4mm}
.hdr .h-en{font-weight:700;font-size:10.5pt;color:var(--acc-d);letter-spacing:.02em}
.hdr .h-ar{font-weight:700;font-size:11pt;color:var(--acc-d)}
.hdr .chip{font-size:9pt;font-weight:700;background:var(--acc);color:var(--cream);border-radius:20mm;padding:1mm 4mm;white-space:nowrap}
.hdr .chip b{color:var(--van)}
.hrule{margin:2.4mm 15mm 0;height:1.4mm;border-radius:2mm;background:linear-gradient(90deg,var(--van) 0 62%,var(--wis) 62% 80%,var(--acc) 80%)}
/* body */
.body{flex:1;display:flex;flex-direction:column;padding:4mm 17mm 0;min-height:0}
.content{flex:0 0 auto}
/* footer */
.ftr{height:21mm;padding:0 15mm 10mm;display:flex;align-items:flex-end;justify-content:space-between;font-size:9pt;color:var(--acc-d);font-weight:600}
.ftr .pg{min-width:11mm;height:7mm;padding:0 2.5mm;border-radius:4mm;background:var(--acc);color:var(--cream);font-weight:800;font-size:10.5pt;display:flex;align-items:center;justify-content:center}
.ftr .f-en,.ftr .f-ar{width:70mm}
.ftr .f-ar{text-align:right}
/* notes */
.notes{flex:1 1 auto;min-height:49mm;margin-top:4mm;display:flex;flex-direction:column;padding-bottom:1mm}
.notes-h{display:flex;align-items:center;gap:2.5mm;font-size:10.5pt;font-weight:700;color:var(--wis-d);margin-bottom:1mm}
.notes-h .ln{flex:1;height:0;border-top:0.35mm dashed var(--wis)}
.notes-lines{flex:1;background:repeating-linear-gradient(to bottom,transparent 0,transparent calc(8.2mm - 0.3mm),rgba(76,157,176,.45) calc(8.2mm - 0.3mm),rgba(76,157,176,.45) 8.2mm);background-size:100% 8.2mm;min-height:41mm}
/* section heading */
.sec{display:flex;align-items:center;gap:4mm;margin:1mm 0 4mm;padding:2.6mm 4mm;border-radius:4mm;
  background:linear-gradient(90deg,var(--van),var(--cream));border-left:2mm solid var(--acc);break-inside:avoid}
.sec-num{width:11mm;height:11mm;flex:none;border-radius:50%;background:var(--acc);color:var(--cream);display:flex;align-items:center;justify-content:center;font-weight:900;font-size:13pt}
.sec-t{flex:1;display:flex;justify-content:space-between;align-items:baseline;gap:4mm}
.sec-en{font-weight:800;font-size:17pt;color:var(--moon-dd);line-height:1.15}
.sec-ar{font-weight:800;font-size:17pt;color:var(--acc-d);line-height:1.3}
.sec-ico{font-size:15pt}
.h2{display:flex;justify-content:space-between;align-items:baseline;border-bottom:0.5mm solid var(--wis);padding-bottom:1mm;margin:4mm 0 3mm}
.h2-en{font-weight:800;font-size:15pt;color:var(--wis-d)}
.h2-ar{font-weight:800;font-size:15pt;color:var(--wis-d)}
/* text */
.en{font-size:14pt;line-height:1.42;font-weight:400;text-align:left}
.ar{font-size:14pt;line-height:1.62;font-weight:500;color:var(--ink-ar);text-align:right}
.pair{margin:0 0 3.4mm;break-inside:avoid}
.pair .ar{margin-top:.6mm}
b.term{font-weight:700;color:var(--moon-dd);background:linear-gradient(transparent 60%,rgba(255,235,175,.95) 60%)}
b.em{font-weight:800;color:var(--wis-d)}
i{font-style:italic}
.ar i{font-style:italic}
bdi.lt{unicode-bidi:isolate;white-space:nowrap}
/* lists */
ul.bl,ol.nl{list-style:none;margin:0 0 2mm}
ul.bl li,ol.nl li{margin:0 0 3.4mm;break-inside:avoid}
.li-en{font-size:14pt;line-height:1.42;position:relative;padding-left:7mm}
.li-ar{font-size:14pt;line-height:1.62;font-weight:500;color:var(--ink-ar);position:relative;padding-right:7mm;margin-top:.6mm}
ul.bl .mk{position:absolute;top:2.3mm;width:2.4mm;height:2.4mm;background:var(--acc);transform:rotate(45deg);border-radius:.4mm}
.li-en .mk{left:1.2mm}.li-ar .mk{right:1.2mm;top:3mm;background:var(--wis)}
ol.nl .nb{position:absolute;top:.9mm;width:5.4mm;height:5.4mm;border-radius:50%;background:var(--acc);color:var(--cream);font-weight:800;font-size:10pt;display:flex;align-items:center;justify-content:center;line-height:1}
.li-en .nb{left:0}.li-ar .nb{right:0;top:1.6mm;background:var(--wis);color:#fff}
/* boxes */
.box{border-radius:4mm;margin:2mm 0 3.6mm;break-inside:avoid;overflow:hidden;border:0.4mm solid var(--line)}
.box-h{display:flex;align-items:center;gap:2.5mm;padding:1.6mm 4mm;font-weight:800;font-size:11.5pt}
.box-h .box-te{flex:1}
.box-b{padding:2.6mm 4.5mm 1.2mm}
.box-b .pair{margin-bottom:2.6mm}
.box-note{background:#FFFBEA;border-color:#F2D78A}.box-note .box-h{background:var(--van);color:#6B5310}
.box-alert{background:#FBF6FD;border-color:var(--wis)}.box-alert .box-h{background:var(--wis);color:#fff}
.box-sci{background:#F3FAFC;border-color:var(--line)}.box-sci .box-h{background:var(--moon);color:#fff}
.box-memory{background:#FEFFE9;border-color:#E6E79A}.box-memory .box-h{background:var(--cream);color:var(--moon-dd)}
.box-compare{background:#fff;border-color:var(--line)}.box-compare .box-h{background:var(--moon-dd);color:var(--van)}
.box-key{background:#F4FAFB;border-color:var(--moon)}.box-key .box-h{background:var(--moon);color:var(--cream)}
/* figures */
.fig{margin:1mm auto 4mm;break-inside:avoid}
.fig-frame{border-radius:4mm;overflow:hidden;border:1.2mm solid #fff;box-shadow:0 0 0 0.35mm var(--line),0 2mm 5mm rgba(30,77,89,.12);background:#fff}
.fig-frame img{display:block;width:100%;height:auto}
figcaption{display:flex;justify-content:space-between;gap:3mm;margin-top:1.6mm;font-size:10.5pt;font-weight:700;color:var(--acc-d)}
.figrow{display:flex;justify-content:space-around;align-items:flex-start;gap:6mm}
.figrow .fig{margin:1mm 0 4mm}
/* tables */
table.t{width:100%;border-collapse:separate;border-spacing:0;margin:1mm 0 4mm;font-size:13pt;break-inside:auto}
table.t th{background:var(--moon-dd);color:var(--van);font-weight:800;padding:2mm 2.5mm;text-align:center;vertical-align:middle;line-height:1.3}
table.t th:first-child{border-top-left-radius:3mm}table.t th:last-child{border-top-right-radius:3mm}
table.t td{padding:2.4mm 3mm;vertical-align:top;border-bottom:0.35mm solid var(--line)}
table.t tr:nth-child(even) td{background:#FFFCEF}
table.t td .en{font-size:13pt;line-height:1.38}
table.t td .ar{font-size:13pt;line-height:1.55}
table.t tr{break-inside:avoid}
.rg-title{font-weight:800;text-align:center}
.lvl{font-weight:800;color:var(--moon-dd);text-align:center}
.cnum{width:12mm;text-align:center;font-weight:900;font-size:16pt;color:var(--acc)}
.risk1{color:#3C8D5A}.risk2{color:#B58A12}.risk3{color:#C0602A}.risk4{color:#A3243B}
/* glossary */
table.g td{font-size:13pt;padding:1.7mm 3mm;border-bottom:0.3mm solid var(--line);vertical-align:middle}
table.g td.ge{font-weight:700;color:var(--moon-dd);width:50%}
table.g td.ga{text-align:right;font-weight:600;color:var(--ink-ar)}
.muted{color:#6b7f85}
"""

def page(content, hdr, ftr_l, ftr_r, num, notes=True, extra=""):
    notes_html = ('<div class="notes"><div class="notes-h"><span dir="ltr">Student Notes</span>'
                  '<span class="ln"></span><span dir="rtl">ملاحظات الطالب</span></div>'
                  '<div class="notes-lines"></div></div>') if notes else ""
    return (f'<section class="page" data-num="{num}"><div class="frame"></div>{extra}{hdr}'
            f'<div class="hrule"></div><div class="body"><div class="content">{content}</div>{notes_html}</div>'
            f'<div class="ftr"><span class="f-en" dir="ltr">{ftr_l}</span><span class="pg">{num}</span>'
            f'<span class="f-ar" dir="rtl">{ftr_r}</span></div></section>')

def doc(title, pages, extra_css=""):
    return (f'<!doctype html><html><head><meta charset="utf-8"><title>{title}</title>'
            f'<style>{CSS}{extra_css}</style></head><body>{"".join(pages)}</body></html>')

CSS += """
table.rg td .en,table.rg td .ar{font-size:12.5pt}
table.rg td{padding:2mm 2.6mm}
.card-r{padding:1.8mm 5mm}
.toc li{padding:1.1mm 0}.toc .te,.toc .ta{font-size:12pt}.toc .n{width:7mm;height:7mm;font-size:10pt}.card-r{font-size:12pt}.card{margin-bottom:4mm}
"""
