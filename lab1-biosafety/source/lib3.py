"""BIOS reference template (cream · burgundy · sage · gold), rebuilt to match the BIOS Lab 1 booklet."""
import re, html

AR_DIGITS = str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩")
def ard(n): return str(n).translate(AR_DIGITS)

SUBJ_EN, SUBJ_AR = "Diagnostic Microbiology", "الأحياء المجهرية التشخيصية"
TITLE_EN, TITLE_AR = "Rules and Biosafety Levels", "القواعد ومستويات السلامة الحيوية"
DOCTOR = "د. ذهب"

def md(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r'<b class="t">\1</b>', s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", s)
    s = re.sub(r"`(.+?)`", r'<bdi dir="ltr" class="lt">\1</bdi>', s)
    s = s.replace("[[cut]]", '<span class="cut" dir="ltr">[text cut off in the original file]</span>')
    s = s.replace("[[قطع]]", '<span class="cut" dir="rtl">[النص مقطوع في الملف الأصلي]</span>')
    return s

def en(s): return f'<p class="en" dir="ltr">{md(s)}</p>'
def ar(s): return f'<p class="ar" dir="rtl">{md(s)}</p>'

def card(e, a, e_extra="", a_extra="", cls=""):
    return (f'<div class="card {cls}"><div class="c-en"><span class="chip">EN</span>{en(e) if e else ""}{e_extra}</div>'
            f'<div class="c-ar"><span class="chip chip-ar">AR</span>{ar(a) if a else ""}{a_extra}</div></div>')

def nlist(items, rtl=False):
    d = "rtl" if rtl else "ltr"
    cls = "ar" if rtl else "en"
    return f'<ol class="nl {cls}" dir="{d}">' + "".join(f'<li><span class="nb">{i}</span><span>{md(t)}</span></li>' for i, t in enumerate(items, 1)) + "</ol>"

def sec(n, e, a):
    return (f'<div class="sec"><span class="sn">{n}</span><div class="sb"><span dir="ltr">{e}</span><span dir="rtl">{a}</span></div></div>')

def labtitle():
    return (f'<div class="lt-band"><div class="lt-box"><small>LAB</small><b>1</b></div>'
            f'<span class="lt-en" dir="ltr">{TITLE_EN}</span><span class="lt-ar" dir="rtl">{TITLE_AR}</span></div>')

def rule(n, e, a):
    return f'<div class="rule"><span class="rn">{n}</span>{card(e, a)}</div>'

def rg(n, col, te, ta, e, a):
    return (f'<div class="rg card"><div class="rg-h" style="background:{col}"><span dir="ltr">{te}</span><span dir="rtl">{ta}</span></div>'
            f'<div class="rg-s"><span dir="ltr">Biosafety level {n}</span><span dir="rtl">مستوى السلامة الحيوية {n}</span></div>'
            f'<div class="c-en"><span class="chip">EN</span>{en(e)}</div><div class="c-ar"><span class="chip chip-ar">AR</span>{ar(a)}</div></div>')

FIG = {"n": 0}
def fig(src, ce, ca, h=None, inner=None, fit="contain"):
    FIG["n"] += 1; n = FIG["n"]
    st = f"height:{h};object-fit:{fit};object-position:center 40%;width:100%" if h else "width:100%"
    body = inner if inner is not None else f'<img src="{src}" style="{st}">'
    return (f'<figure class="fig"><div class="fig-c">{body}</div><figcaption><span dir="ltr"><b>Figure {n}.</b> {ce}</span>'
            f'<span dir="rtl"><b>الشكل {n}.</b> {ca}</span></figcaption></figure>')

def h2(e, a): return f'<div class="h2"><span dir="ltr">{e}</span><span dir="rtl">{a}</span></div>'

def note(e, a, label=("Note", "ملاحظة")):
    return (f'<div class="note"><span class="np">{label[0]} &nbsp; <span dir="rtl">{label[1]}</span></span>'
            f'{en(e)}{ar(a)}</div>')

FONTS = "".join(f"@font-face{{font-family:Mada;src:url(fonts/Mada-{n}.ttf);font-weight:{w}}}" for n, w in
                [("Light", 300), ("Regular", 400), ("Medium", 500), ("SemiBold", 600), ("Bold", 700), ("ExtraBold", 800), ("Black", 900)])
FONTS += "@font-face{font-family:AmiriQ;src:url(fonts/AmiriQuran-Regular.ttf)}"
FONTS += "@font-face{font-family:Playfair;src:url(fonts/playfair-display-latin-900-italic.woff2);font-weight:900;font-style:italic}"
FONTS += "@font-face{font-family:Playfair;src:url(fonts/playfair-display-latin-700-italic.woff2);font-weight:700;font-style:italic}"

CSS = FONTS + r"""
:root{--burg:#6E1F2A;--burg-d:#4A131B;--sage:#56605A;--sage-m:#8C968D;--sage-l:#EDF0EC;--sage-ll:#D5DBD4;--beige:#F7F2E9;--pink:#F4E8E7;
--gold:#B08A3E;--gold-l:#F2E7CB;--gold-t:#7A5A00;--ink:#2B2B2B;--muted:#7D7D7D;--bd:#E2DDD5;--cream:#F6F1E8}
*{box-sizing:border-box;margin:0;padding:0}
@page{size:A4;margin:0}
html,body{background:#ccc}
body{font-family:Mada,sans-serif;color:var(--ink);-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:210mm;height:297mm;position:relative;overflow:hidden;background:#fff;break-after:page}
@media screen{.page{margin:8mm auto}}
/* margin guides */
.vg{position:absolute;top:30mm;bottom:22mm;width:0;border-left:.25mm dotted #9a9a9a}
.vg.l{left:9mm}.vg.r{right:9mm}
.vd{position:absolute;width:1.9mm;height:1.9mm;border-radius:50%;margin-left:-.95mm;border:.3mm solid #8a8a8a;background:#fff}
.vd.f{background:var(--burg);border-color:var(--burg)}
.vt{position:absolute;width:.6mm;height:4mm;background:var(--burg);margin-left:-.3mm}
/* header */
.hdr{position:absolute;left:9mm;right:9mm;top:12mm;height:13mm}
.hp{position:absolute;top:0;height:10.5mm;border-radius:6mm;display:flex;align-items:center}
.hp.lab{background:var(--sage-l);padding:0 4mm 0 7mm;font-size:7.8pt;font-weight:700;color:#444;line-height:1.25;flex-direction:column;justify-content:center;align-items:flex-start}
.hp.lab::before{content:"";position:absolute;left:0;top:0;bottom:0;width:4mm;border-radius:6mm 0 0 6mm;background:var(--sage)}
.hp.lab span:first-child{font-weight:600;color:#555}
.hp.bios{background:var(--pink);padding:0 8mm 0 4.5mm;gap:3mm}
.hp.bios::after{content:"";position:absolute;right:0;top:0;bottom:0;width:4mm;border-radius:0 6mm 6mm 0;background:var(--burg)}
.hp.bios .bw{font-family:Playfair;font-style:italic;font-weight:900;font-size:17pt;color:var(--burg);letter-spacing:.02em}
.hp.bios .bt{font-size:7.2pt;font-weight:700;color:var(--burg-d);line-height:1.2;border-right:.3mm solid #c9a9ad;padding-right:3mm;max-width:19mm;text-align:right}
.hc{position:absolute;left:50%;transform:translateX(-50%);top:-1mm;text-align:center;width:80mm}
.hc .e{font-weight:700;font-size:10pt;color:#333}
.hc .a{font-weight:600;font-size:8.6pt;color:#666}
.hc .dr{display:inline-block;margin-top:.8mm;background:linear-gradient(#c9a35a,#9c7a33);color:#fff;font-weight:800;font-size:7.4pt;border-radius:3mm;padding:.2mm 3.4mm}
.hl{position:absolute;top:5.2mm;height:0;border-top:.45mm solid var(--sage-m)}
.hl::before,.hl::after{content:"";position:absolute;top:-1.1mm;height:2.2mm;border-left:.4mm solid var(--sage-m)}
.hl::before{left:0}.hl::after{right:0}
/* body */
.body{position:absolute;left:17mm;right:17mm;top:31mm;bottom:24mm}
/* footer */
.ftr{position:absolute;left:0;right:0;bottom:6mm;height:6mm;background:var(--sage);border-bottom:1.1mm solid var(--burg)}
.ftr .fx{position:absolute;top:0;bottom:0;display:flex;align-items:center;gap:2.6mm;font-size:7.4pt;color:#fff;font-weight:600}
.ftr .fx b{font-family:Playfair;font-style:italic;font-weight:900;font-size:10pt}
.ftr .fx .s{opacity:.7}
.tab{position:absolute;bottom:4.9mm;width:18mm;height:10.5mm;background:var(--burg);color:#fff;font-weight:800;font-size:12pt;display:flex;align-items:center;justify-content:center}
.tab.r{right:14mm;clip-path:polygon(0 0,100% 0,85% 100%,15% 100%);clip-path:polygon(0 0,100% 0,100% 100%,12% 100%)}
.tab.l{left:14mm;clip-path:polygon(0 0,100% 0,88% 100%,0 100%)}
/* title band */
.lt-band{display:flex;align-items:center;gap:5mm;height:13.5mm;background:var(--pink);border:.3mm solid #EBD7D7;border-radius:2.5mm;overflow:hidden;margin-bottom:5mm}
.lt-box{width:17mm;height:100%;background:var(--burg);color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;line-height:1}
.lt-box small{font-size:6pt;letter-spacing:.12em;opacity:.85;margin-bottom:1mm}
.lt-box b{font-size:17pt;font-weight:800}
.lt-en{font-weight:700;font-size:15pt;color:var(--burg-d)}
.lt-ar{margin-left:auto;margin-right:5mm;font-weight:800;font-size:15pt;color:var(--burg-d)}
/* section bar */
.sec{display:flex;align-items:center;gap:2.6mm;margin:0 0 3.6mm;break-inside:avoid}
.sn{width:8.4mm;height:8.4mm;flex:none;border-radius:50%;border:.5mm solid var(--burg);color:var(--burg);font-weight:800;font-size:9pt;display:flex;align-items:center;justify-content:center;background:#fff}
.sb{flex:1;height:9mm;border-radius:4.5mm;background:linear-gradient(90deg,var(--sage),var(--sage-m));display:flex;align-items:center;justify-content:space-between;padding:0 5mm;color:#fff;font-weight:800;font-size:11.5pt}
.sb [dir=rtl]{font-size:12pt}
/* cards */
.card{border:.3mm solid var(--bd);border-radius:2.6mm;overflow:hidden;background:#fff;margin:0 0 3mm;break-inside:avoid}
.c-en{position:relative;padding:2.3mm 5mm 2.3mm 13.4mm}
.c-ar{position:relative;padding:1.6mm 13.4mm 1.8mm 5mm;background:var(--beige);border-top:.3mm dashed #DDD3C2}
.chip{position:absolute;left:4mm;top:3.3mm;font-size:6.4pt;font-weight:800;background:var(--sage-l);color:var(--sage);border-radius:1mm;padding:.5mm 1.3mm;line-height:1}
.chip-ar{left:auto;right:4mm;top:3.2mm;background:var(--pink);color:var(--burg)}
.en{font-size:11.6pt;line-height:1.5;color:#2f2f2f}
.ar{font-family:AmiriQ,serif;font-size:14pt;line-height:1.72;color:#222;text-align:right}
b.t{color:var(--burg);font-weight:700}
.ar b.t{font-weight:700}
.ar b.t bdi,.ar bdi.lt{font-family:Mada;font-size:.86em}
.en i{font-style:italic}
.en b.t i,.en i{font-weight:inherit}
.ar i{font-family:Mada;font-weight:700;font-style:italic;font-size:.86em}
bdi.lt{unicode-bidi:isolate}
.cut{display:inline-block;font-family:Mada;font-size:7.4pt;font-weight:800;color:var(--gold-t);background:#FFF4C8;border:.3mm dashed #D8B24C;border-radius:1mm;padding:.2mm 1.4mm;margin:0 1mm;vertical-align:middle;line-height:1.45;font-style:normal}
/* numbered list inside cards */
ol.nl{list-style:none;margin:2mm 0 .4mm}
ol.nl li{display:flex;align-items:flex-start;gap:2.6mm;margin:0 0 1.6mm}
ol.nl.en li{padding-left:1mm}
ol.nl .nb{flex:none;width:4.8mm;height:4.8mm;border-radius:50%;background:var(--burg);color:#fff;font-family:Mada;font-size:6.6pt;font-weight:800;display:flex;align-items:center;justify-content:center;margin-top:1.1mm}
ol.nl.ar li{margin-right:-8mm}
ol.nl.ar .nb{margin-top:2.6mm}
/* rule cards */
.rule{display:flex;gap:3.6mm;align-items:flex-start;break-inside:avoid}
.rule .rn{flex:none;width:9mm;height:9mm;border-radius:50%;background:var(--burg);color:#fff;font-weight:800;font-size:11pt;display:flex;align-items:center;justify-content:center;margin-top:2.4mm}
.rule .card{flex:1}
/* risk group */
.rg-h{display:flex;justify-content:space-between;align-items:center;padding:0 4mm;height:8.6mm;color:#fff;font-weight:800;font-size:10.5pt}
.rg-h [dir=rtl]{font-size:11pt}
.rg-s{display:flex;justify-content:space-between;padding:1.4mm 4mm;font-size:7.6pt;font-weight:700;color:#666;border-bottom:.3mm dashed #DDD3C2}
/* figures */
.fig{margin:0 0 3.6mm;break-inside:avoid}
.fig-c{border:.3mm solid var(--bd);border-radius:2.6mm;padding:2.2mm;background:#fff}
.fig-c img{display:block;border-radius:1.6mm}
figcaption{display:flex;justify-content:space-between;gap:3mm;margin-top:1.4mm;font-size:8pt;color:var(--muted)}
figcaption b{color:var(--burg);font-weight:800}
.fig2{display:grid;grid-template-columns:1fr 1fr;gap:5mm}
/* summary table */
.sum{background:var(--sage-l);border-left:3.4mm solid var(--sage-ll);border-radius:2.6mm;padding:3mm 4mm 4mm;margin:0 0 3.6mm;break-inside:avoid}
.pillh{display:inline-flex;gap:3mm;align-items:center;background:var(--sage);color:#fff;font-weight:800;font-size:7.6pt;border-radius:4mm;padding:.8mm 3.6mm;margin-bottom:2.4mm}
.pillh.b{background:var(--burg)}
table.tb{width:100%;border-collapse:separate;border-spacing:0;border:.3mm solid #9AA39B;border-radius:2.4mm;overflow:hidden;background:#fff}
table.tb th{background:var(--sage);color:#fff;font-weight:700;font-size:9pt;padding:2mm 3mm;text-align:center}
table.tb td{font-size:9pt;padding:1.3mm 3mm;border-top:.3mm solid #E3E6E2}
table.tb tr:nth-child(even) td{background:#F4F6F3}
table.tb td.a{direction:rtl;text-align:right;font-weight:600}
table.tb td.k{font-weight:700}
table.tb th + th{border-left:.3mm solid rgba(255,255,255,.35)}
/* h2 */
.h2{display:flex;justify-content:space-between;font-weight:800;font-size:10.5pt;color:var(--burg);border-bottom:.35mm solid var(--burg);padding-bottom:1mm;margin:1mm 0 3mm}
/* note */
.note{background:#F6EBEA;border-left:3.4mm solid var(--burg);border-radius:2.6mm;padding:2.6mm 5mm 2.6mm;margin:0 0 3.6mm;break-inside:avoid}
.note .en{font-size:10.5pt}.note .ar{font-size:13.5pt;line-height:1.7}
.np{display:inline-block;background:var(--burg);color:#fff;font-weight:800;font-size:7.4pt;border-radius:3mm;padding:.5mm 3mm;margin-bottom:1.2mm}
"""

def guides(seed):
    import random
    r = random.Random(seed)
    out = '<div class="vg l"></div><div class="vg r"></div>'
    for side, x in (("l", "9mm"), ("r", "calc(100% - 9mm)")):
        out += f'<span class="vd {"f" if (side == "r") == (seed % 2 == 1) else ""}" style="left:{x};top:29.5mm"></span>'
        out += f'<span class="vd {"" if (side == "r") == (seed % 2 == 1) else "f"}" style="left:{x};bottom:21.5mm"></span>'
        for y in (80, 155, 230):
            out += f'<span class="vd" style="left:{x};top:{y + r.uniform(-8, 8):.0f}mm;width:1.5mm;height:1.5mm;margin-left:-.75mm"></span>'
        out += f'<span class="vt" style="left:{x};top:{r.uniform(110, 200):.0f}mm"></span>'
    return out

def header(n, sub=("Lab 1", "العملي 1")):
    lab = f'<div class="hp lab" style="{{pos}}"><span>{sub[0]}</span><span dir="rtl">{sub[1]}</span></div>'
    bios = '<div class="hp bios" style="{pos}"><span class="bt" dir="rtl">ترجمة وتعديل الملازم</span><span class="bw">BIOS</span></div>'
    if n % 2:  # odd: lab left, bios right
        left = lab.replace("{pos}", "left:0"); right = bios.replace("{pos}", "right:0")
    else:
        left = bios.replace("{pos}", "left:0").replace('class="hp bios"', 'class="hp bios flip"'); right = lab.replace("{pos}", "right:0").replace('class="hp lab"', 'class="hp lab flip"')
    return (f'<div class="hdr">{left}<span class="hl" style="left:28%;width:16%"></span>'
            f'<div class="hc"><div class="e">{SUBJ_EN}</div><div class="a" dir="rtl">{SUBJ_AR}</div><span class="dr">✦ {DOCTOR} ✦</span></div>'
            f'<span class="hl" style="right:28%;width:16%"></span>{right}</div>')

FLIP = r"""
.hp.bios.flip{padding:0 4.5mm 0 8mm;flex-direction:row-reverse}
.hp.bios.flip::after{left:0;right:auto;border-radius:6mm 0 0 6mm}
.hp.bios.flip .bt{border-right:0;border-left:.3mm solid #c9a9ad;padding:0 0 0 3mm;text-align:left}
.hp.lab.flip{padding:0 7mm 0 4mm;align-items:flex-end}
.hp.lab.flip::before{left:auto;right:0;border-radius:0 6mm 6mm 0}
"""

def footer(n):
    txt_l = '<b>BIOS</b><span>|بايوس</span><span class="s">|</span><span>Telegram: BIOS0t</span><span class="s">|</span><span>ترجمة وتعديل الملازم</span>'
    txt_r = '<span>ترجمة وتعديل الملازم</span><span class="s">|</span><span>Telegram: BIOS0t</span><span class="s">|</span><span>بايوس|</span><b>BIOS</b>'
    if n % 2:
        return f'<div class="ftr"><div class="fx" style="left:13mm">{txt_l}</div></div><div class="tab r">{n}</div>'
    return f'<div class="ftr"><div class="fx" style="right:13mm">{txt_r}</div></div><div class="tab l">{n}</div>'

def page(content, n, sub=("Lab 1", "العملي 1")):
    return (f'<section class="page" data-num="{n}">{guides(n)}{header(n, sub)}'
            f'<div class="body"><div class="content">{content}</div></div>{footer(n)}</section>')

COVER_CSS = r"""
.cover{background:var(--cream)}
.cv-c1{position:absolute;left:140mm;top:-30mm;width:115mm;height:115mm;border-radius:50%;background:#E9EBE5}
.cv-c2{position:absolute;left:130mm;top:-42mm;width:135mm;height:135mm;border-radius:50%;border:.3mm solid #CFCAC1}
.cv-b1{position:absolute;left:-20mm;top:216mm;width:105mm;height:100mm;border-radius:0 52mm 0 0;background:#EFE3DF}
.cv-b2{position:absolute;left:-30mm;top:228mm;width:105mm;height:100mm;border-radius:0 40mm 0 0;border:.3mm solid #D9BFC0;border-left:0;border-bottom:0}
.cv-vg{position:absolute;top:18mm;bottom:27mm;border-left:.25mm dotted #9a9a9a}
.cv-logo{position:absolute;left:57mm;top:22mm;width:96mm;height:96mm;border-radius:50%;
  -webkit-mask-image:radial-gradient(circle,#000 52%,rgba(0,0,0,.6) 62%,transparent 71%);mask-image:radial-gradient(circle,#000 52%,rgba(0,0,0,.6) 62%,transparent 71%)}
.cv-logo img{width:100%;height:100%;object-fit:cover}
.cv-ln{position:absolute;left:62mm;width:86mm;top:110mm;border-top:.3mm solid #D7CFC4}
.cv-ln.b{top:110.6mm;left:118mm;width:30mm;border-color:var(--burg)}
.cv-tr{position:absolute;left:0;right:0;top:111.5mm;text-align:center;font-weight:800;font-size:11pt;color:#555}
.cv-tre{position:absolute;left:0;right:0;top:118mm;text-align:center;font-size:7.6pt;letter-spacing:.3em;color:#666}
.cv-r{position:absolute;left:22mm;right:22mm;border-top:.35mm solid #B79A9B}
.cv-t1{position:absolute;left:0;right:0;top:138mm;text-align:center;font-weight:800;font-size:25pt;color:var(--burg-d)}
.cv-t2{position:absolute;left:0;right:0;top:149mm;text-align:center;font-weight:900;font-size:22pt;color:#2b2b2b}
.cv-pill{position:absolute;left:40mm;right:40mm;top:164mm;height:8.6mm;border-radius:4.3mm;background:#742833;color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 7mm;font-weight:700;font-size:9.2pt}
.cv-cards{position:absolute;left:26mm;right:26mm;top:191mm;display:grid;grid-template-columns:1fr 1fr;gap:3.2mm 6mm}
.cv-card{height:12.4mm;background:#fff;border:.3mm solid #DDD8CF;border-radius:2.6mm;display:flex;align-items:center;justify-content:space-between;padding:0 4mm;box-shadow:0 .4mm 1.2mm rgba(0,0,0,.04)}
.cv-card .k{font-size:7.4pt;color:#666;line-height:1.3}
.cv-card .k small{display:block;font-size:6.4pt;color:#888;text-align:right}
.cv-card .v{font-weight:800;font-size:10.5pt;color:#2b2b2b}
.cv-ins{position:absolute;left:26mm;right:26mm;top:223mm;height:17mm;border:.4mm solid var(--gold);border-radius:2.6mm;background:#FFFDF6;display:flex;align-items:center;justify-content:space-between;padding:0 6mm;box-shadow:0 .8mm 2.4mm rgba(176,138,62,.18)}
.cv-ins .k{font-size:7.6pt;font-weight:700;color:var(--gold-t);line-height:1.35}
.cv-ins .v{font-weight:900;font-size:19pt;color:var(--gold);border-top:.3mm solid var(--gold);border-bottom:.3mm solid var(--gold);padding:0 1mm;line-height:1.5}
.cv-st{position:absolute;left:50%;transform:translateX(-50%);background:var(--cream);color:var(--gold);font-size:8pt;letter-spacing:3.5mm;padding:0 2mm 0 5.5mm}
.cv-sage{position:absolute;left:0;right:0;top:272mm;height:2.2mm;background:var(--sage)}
.cv-foot{position:absolute;left:0;right:0;top:274.2mm;bottom:0;background:var(--burg);color:#fff}
.cv-foot .l{position:absolute;left:18mm;top:9mm;display:flex;align-items:center;gap:3mm}
.cv-foot .l b{font-family:Playfair;font-style:italic;font-weight:900;font-size:20pt}
.cv-foot .l span{font-size:9pt;font-weight:700;border-left:.3mm solid #fff;padding-left:2mm}
.cv-foot .r{position:absolute;right:18mm;top:6.5mm;text-align:right;font-size:8.6pt;line-height:1.6}
.cv-foot .r b{font-weight:800}
"""

def cover(pill_l, pill_r, cards, ins=("Instructor", "تدريسية المادة", DOCTOR)):
    cc = "".join(f'<div class="cv-card"><span class="k">{k}<small dir="rtl">{ka}</small></span><span class="v" dir="rtl">{v}</span></div>' for k, ka, v in cards)
    return f'''<section class="page cover">
<div class="cv-c1"></div><div class="cv-c2"></div><div class="cv-b1"></div><div class="cv-b2"></div>
<div class="cv-vg" style="left:10mm"></div><div class="cv-vg" style="right:10mm"></div>
<div class="cv-logo"><img src="assets/logo_full.jpg"></div>
<div class="cv-ln"></div>
<div class="cv-tr" dir="rtl">ترجمة وتعديل الملازم</div>
<div class="cv-tre">LECTURE TRANSLATION &amp; EDITING</div>
<div class="cv-r" style="top:130mm"></div>
<div class="cv-t1">{SUBJ_EN}</div>
<div class="cv-t2" dir="rtl">{SUBJ_AR}</div>
<div class="cv-pill"><span dir="ltr">{pill_l}</span><span dir="rtl">{pill_r}</span></div>
<div class="cv-r" style="top:181mm"></div>
<div class="cv-cards">{cc}</div>
<div class="cv-ins"><span class="k">{ins[0]}<br><span dir="rtl">{ins[1]}</span></span><span class="v" dir="rtl">{ins[2]}</span></div>
<span class="cv-st" style="top:221.2mm">✦ ✦ ✦</span><span class="cv-st" style="top:238.6mm;letter-spacing:0;padding:0 3mm">✦</span>
<div class="cv-sage"></div>
<div class="cv-foot"><div class="l"><b>BIOS</b><span>بايوس</span></div><div class="r">Telegram: <b>BIOS0t</b><br><span dir="rtl" style="font-weight:700">ترجمة وتعديل الملازم</span></div></div>
</section>'''

def doc(title, pages, extra=""):
    return (f'<!doctype html><html><head><meta charset="utf-8"><title>{title}</title>'
            f'<style>{CSS}{FLIP}{COVER_CSS}{extra}</style></head><body>{"".join(pages)}</body></html>')
