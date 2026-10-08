import json
from lib2 import *
from art2 import biohazard, radiation, medallion, corner, divider, icon

D = json.load(open("data.json"))
SUBJ_EN, SUBJ_AR = "Diagnostic Microbiology", "الأحياء المجهرية التشخيصية"
TITLE_EN, TITLE_AR = "Rules and Biosafety Levels", "القواعد ومستويات السلامة الحيوية"
LECTURER = "د. هبة سامي"

# ================================================================ extra CSS
X = r"""
/* ---------- cover ---------- */
.cover{background:radial-gradient(120% 70% at 50% 18%,#FFFDF8 0,#F7EFE2 55%,#EADCC4 100%)}
.cv-arch{position:absolute;left:-20mm;right:-20mm;top:168mm;bottom:-10mm;background:radial-gradient(90% 80% at 50% 0,#7A2532 0,#5A1822 45%,#3C0E15 100%);border-radius:50% 50% 0 0/22% 22% 0 0}
.cv-arch::before{content:"";position:absolute;inset:3.5mm 18mm auto;height:100%;border-top:.5mm solid var(--gold);border-radius:50% 50% 0 0/22% 22% 0 0;opacity:.8}
.cv-fr{position:absolute;inset:7mm;border:.6mm solid var(--gold);pointer-events:none}
.cv-fr2{position:absolute;inset:9mm;border:.25mm solid var(--gold-l);pointer-events:none}
.cv-cn{position:absolute;width:24mm;height:24mm;line-height:0}
.cv-logo{position:absolute;left:50%;top:13mm;width:66mm;transform:translateX(-50%)}
.cv-tg{position:absolute;right:15mm;top:16mm;display:flex;align-items:center;gap:2mm;border:.4mm solid var(--burg);border-radius:10mm;padding:1mm 3.5mm 1mm 1.2mm;font-weight:600;font-size:10pt;color:var(--burg-d);background:rgba(255,255,255,.5)}
.cv-tg i{width:7mm;height:7mm;border-radius:50%;background:var(--burg);display:flex;align-items:center;justify-content:center}
.cv-ar-brand{position:absolute;left:0;right:0;top:61mm;display:flex;justify-content:center;align-items:center;gap:4mm;font-weight:700;font-size:11pt;color:var(--burg-d)}
.cv-ar-brand .d{width:16mm;border-top:.3mm solid var(--burg);position:relative}
.cv-t0{position:absolute;left:0;right:0;top:68mm;text-align:center;font-family:Cormorant;font-weight:700;font-size:14pt;letter-spacing:.6em;color:var(--gold-d);padding-left:.6em}
.cv-t1{position:absolute;left:0;right:0;top:73mm;text-align:center;font-family:Playfair;font-weight:700;font-size:47pt;line-height:1;color:var(--burg-d);letter-spacing:.01em;transform:scaleY(1.32);transform-origin:top}
.cv-div{position:absolute;left:0;right:0;top:100mm}
.cv-t2{position:absolute;left:0;right:0;top:104mm;text-align:center;font-weight:900;font-size:33pt;line-height:1.25;color:var(--burg)}
.cv-t3{position:absolute;left:0;right:0;top:124.5mm;display:flex;justify-content:center;align-items:center;gap:3mm}
.cv-t3 .ln{width:22mm;border-top:.3mm solid var(--burg)}
.cv-t3 span.e{font-family:Cormorant;font-weight:700;font-size:12pt;letter-spacing:.3em;color:var(--burg-d)}
.cv-t4{position:absolute;left:0;right:0;top:132mm;text-align:center;font-weight:700;font-size:13pt;color:var(--gold-d)}
.cv-med{position:absolute;left:50%;top:142mm;width:104mm;height:104mm;transform:translateX(-50%);filter:drop-shadow(0 3mm 6mm rgba(40,8,12,.45))}
.cv-cards{position:absolute;left:15mm;right:15mm;bottom:17mm;display:flex;gap:5mm;justify-content:center}
.cv-card{flex:1;position:relative;padding:10mm 3mm 4mm;text-align:center;background:linear-gradient(#FFFDF8,#F1E6D3);border:.5mm solid var(--gold);clip-path:polygon(8% 0,92% 0,100% 18%,100% 100%,0 100%,0 18%)}
.cv-card .ic{position:absolute;left:50%;top:-1mm;transform:translate(-50%,-55%);width:15mm;height:15mm;border-radius:50%;background:var(--burg);box-shadow:0 0 0 .7mm #F7EFE2,0 0 0 1.3mm var(--gold);display:flex;align-items:center;justify-content:center}
.cv-card .ic div{width:8.5mm;height:8.5mm}
.cv-card .k{font-family:Cormorant;font-weight:700;font-size:12.5pt;color:var(--ink);letter-spacing:.04em}
.cv-card .v{font-weight:800;font-size:13pt;color:var(--burg-d);margin-top:.5mm}
.cv-card .o{width:20mm;margin:1.4mm auto 0}
.cv-cardwrap{flex:1;position:relative;padding-top:7mm}
/* ---------- lecture card + toc ---------- */
.lc{display:grid;grid-template-columns:1fr 1fr;gap:2.4mm;margin-bottom:5mm}
.lc div{border:.3mm solid var(--line);border-radius:2mm;background:#fff;padding:2mm 3.5mm;display:flex;justify-content:space-between;align-items:center;gap:2mm}
.lc .k{font-family:Cormorant;font-weight:700;font-size:10pt;letter-spacing:.12em;color:var(--gold-d);text-transform:uppercase;line-height:1.1}
.lc .k small{display:block;font-family:Mada;letter-spacing:0;font-size:8pt;color:var(--muted);text-transform:none}
.lc .v{font-weight:700;font-size:12pt;color:var(--burg-d);text-align:right}
.lc .wide{grid-column:1/3;background:linear-gradient(90deg,#FFFBF1,#F6EAD2);border-color:var(--gold-l)}
.lc .wide .v{font-size:15pt;color:var(--burg)}
.toc{list-style:none}
.toc li{display:flex;align-items:baseline;gap:2.5mm;padding:1.5mm 0}
.toc .n{font-family:Playfair;font-style:italic;font-weight:900;font-size:14pt;color:var(--gold);width:9mm}
.toc .te{font-family:Playfair;font-weight:700;font-size:12pt;color:var(--burg)}
.toc .dots{flex:1;border-bottom:.45mm dotted var(--gold-l);transform:translateY(-1mm)}
.toc .ta{font-weight:700;font-size:12pt;color:var(--ink-ar)}
.toc .p{font-family:Playfair;font-weight:700;font-size:12pt;color:#fff;background:var(--burg);border-radius:1.2mm;padding:0 2mm;min-width:8mm;text-align:center}
/* ---------- risk ladder ---------- */
.ladder{display:flex;align-items:flex-end;gap:2.6mm;height:56mm;margin:2mm 0 1mm;padding:0 1mm}
.step{flex:1;border-radius:2.4mm 2.4mm 0 0;position:relative;color:#fff;padding:2.6mm 2.6mm 0;display:flex;flex-direction:column}
.step .num{font-family:Playfair;font-weight:900;font-style:italic;font-size:26pt;line-height:.9}
.step .lv{font-family:Cormorant;font-weight:700;font-size:9pt;letter-spacing:.14em;text-transform:uppercase;margin-top:1mm;opacity:.9}
.step .rk{font-family:Playfair;font-weight:700;font-size:12pt;line-height:1.15}
.step .rka{font-weight:800;font-size:11pt}
.step .bsl{position:absolute;right:2.4mm;top:2.6mm;width:12mm;height:12mm;border-radius:50%;border:.35mm solid currentColor;display:flex;flex-direction:column;align-items:center;justify-content:center;line-height:1;font-size:6.5pt;font-weight:700;letter-spacing:.05em}
.step .bsl b{font-family:Playfair;font-size:12pt;font-weight:900}
.rkw{display:flex;justify-content:space-between;align-items:baseline;gap:1mm}.s1{height:44%;background:linear-gradient(#EFE3C8,#E2CFA6);color:#5A4520}
.s2{height:60%;background:linear-gradient(#D6B47A,#BE9452);color:#3E2A0E}
.s3{height:79%;background:linear-gradient(#A85A55,#8A3B3E)}
.s4{height:100%;background:linear-gradient(#6B1E2A,#3E0F16)}
.ladder-base{height:2.4mm;background:linear-gradient(90deg,#E2CFA6,#BE9452,#8A3B3E,#3E0F16);border-radius:0 0 1.2mm 1.2mm;margin:0 1mm}
.ladder-ax{display:flex;justify-content:space-between;align-items:center;margin:1.4mm 1mm 3.6mm;font-size:9pt;font-weight:700;color:var(--muted)}
.ladder-ax .ar2{font-weight:700}
.ladder-ax .arr{flex:1;margin:0 3mm;height:0;border-top:.35mm solid var(--gold-l);position:relative}
.ladder-ax .arr::after{content:"";position:absolute;right:-1mm;top:-1.25mm;border-left:2.4mm solid var(--gold);border-top:1.1mm solid transparent;border-bottom:1.1mm solid transparent}
.ex{display:flex;gap:2.6mm;margin:0 1mm 4mm}
.ex div{flex:1;font-size:9.5pt;line-height:1.35;color:var(--ink);border-top:.35mm solid var(--line);padding-top:1.2mm}
.ex div b{display:block;font-family:Cormorant;font-weight:700;letter-spacing:.12em;font-size:8pt;color:var(--gold-d);text-transform:uppercase}
.rg{border-radius:2.6mm;overflow:hidden;margin:0 0 3.4mm;background:#fff;border:.3mm solid var(--line);break-inside:avoid}
.rg-h{display:flex;align-items:center;gap:3mm;padding:1.8mm 4mm;color:#fff}
.rg-h .rn{font-family:Playfair;font-style:italic;font-weight:900;font-size:19pt;line-height:1}
.rg-h .rt{flex:1;display:flex;justify-content:space-between;align-items:baseline}
.rg-h .rte{font-family:Playfair;font-weight:700;font-size:12.5pt}
.rg-h .rta{font-weight:800;font-size:12.5pt}
.rg-s{display:flex;justify-content:space-between;padding:1mm 4mm;font-size:9.5pt;font-weight:700;background:var(--ivory);color:var(--gold-d);border-bottom:.3mm solid var(--line)}
.rg .c-en{padding:2mm 4mm 2mm 12mm}
.rg1 .rg-h{background:linear-gradient(90deg,#C9AE78,#DCC596);color:#3E2A0E}
.rg2 .rg-h{background:linear-gradient(90deg,#A9813F,#C9A15E)}
.rg3 .rg-h{background:linear-gradient(90deg,#7F3236,#A3504D)}
.rg4 .rg-h{background:linear-gradient(90deg,#3E0F16,#6B1E2A)}
/* ---------- compare grid ---------- */
.cg{display:grid;grid-template-columns:1fr 1fr;gap:3mm;margin:1mm 0 3.4mm}
.cgc{border:.3mm solid var(--line);border-radius:2.6mm;background:#fff;padding:3mm 3.4mm 2.4mm;position:relative;break-inside:avoid}
.cgc .top{display:flex;align-items:center;gap:2.6mm;margin-bottom:1.6mm}
.cgc .ic{width:10mm;height:10mm;border-radius:50%;background:var(--burg);padding:2.1mm;flex:none}
.cgc .te{font-family:Playfair;font-weight:700;font-size:12.5pt;color:var(--burg);line-height:1.1}
.cgc .ta{font-weight:800;font-size:11pt;color:var(--ink-ar)}
.cgc .row{display:grid;grid-template-columns:17mm 1fr;gap:2mm;border-top:.3mm dashed var(--line);padding:1.1mm 0;font-size:10.5pt;line-height:1.3}
.cgc .row .k{font-family:Cormorant;font-weight:700;letter-spacing:.1em;font-size:8.5pt;color:var(--gold-d);text-transform:uppercase;padding-top:.4mm}
.cgc .row .ka{font-family:Mada;letter-spacing:0;font-size:8.5pt;display:block;text-transform:none;color:var(--muted)}
.cgc .row .va{direction:rtl;text-align:right;color:var(--ink-ar);font-weight:600}
.cgc .meter{position:absolute;right:3.4mm;top:3.6mm;display:flex;gap:.8mm}
.cgc .meter i{width:2.2mm;height:5mm;border-radius:.6mm;background:var(--gold-ll)}
.cgc .meter i.on{background:var(--gold)}
/* ---------- tree (bio risk assessment) ---------- */
.tree{margin:1mm 0 3.4mm;break-inside:avoid}
.tree .root{margin:0 auto;width:96mm;text-align:center;background:var(--burg);color:#F3E3C4;border-radius:2.4mm;padding:2mm 3mm}
.tree .root .e{font-family:Playfair;font-weight:700;font-size:12.5pt}
.tree .root .a{font-weight:800;font-size:11.5pt}
.tree .stem{width:0;height:5mm;border-left:.4mm solid var(--gold);margin:0 auto}
.tree .bar{height:5mm;border:.4mm solid var(--gold);border-bottom:0;margin:0 24%}
.tree .kids{display:grid;grid-template-columns:1fr 1fr;gap:6mm}
.tree .kid{border:.3mm solid var(--gold-l);border-radius:2.4mm;background:#fff;overflow:hidden}
.tree .kid .h{background:var(--ivory);padding:1.6mm 3mm;display:flex;justify-content:space-between;align-items:baseline;border-bottom:.3mm solid var(--line)}
.tree .kid .h .e{font-family:Playfair;font-weight:700;font-size:11.5pt;color:var(--burg)}
.tree .kid .h .a{font-weight:800;font-size:11pt;color:var(--burg)}
.tree .kid .b{padding:1.6mm 3mm 2mm}
.tree .kid .b .en{font-size:12pt;line-height:1.35}
.tree .kid .b .ar{font-size:12.5pt;line-height:1.7}
.chips{display:flex;flex-wrap:wrap;gap:1.2mm;margin-top:1mm}
.chips span{font-size:9.5pt;font-weight:600;border:.3mm solid var(--line2);border-radius:5mm;padding:0 2mm;background:var(--ivory)}
/* ---------- cabinet callouts ---------- */
.cab{position:relative}
.cab img{display:block;width:100%}
.pin{position:absolute;width:6.4mm;height:6.4mm;margin:-3.2mm 0 0 -3.2mm;border-radius:50%;background:var(--burg);color:#fff;font-family:Playfair;font-weight:700;font-size:9pt;display:flex;align-items:center;justify-content:center;border:.5mm solid #fff;box-shadow:0 .6mm 1.6mm rgba(0,0,0,.3)}
.pin.q{background:var(--gold)}
.legend{display:grid;grid-template-columns:1fr 1fr 1fr;gap:1.2mm 4mm;margin:1mm 0 2mm}
.legend div{display:grid;grid-template-columns:6.5mm 1fr;gap:2mm;align-items:start;border-bottom:.3mm dotted var(--line2);padding:.8mm 0 1mm}
.legend .n{width:6mm;height:6mm;border-radius:50%;background:var(--burg);color:#fff;font-family:Playfair;font-weight:700;font-size:8.5pt;display:flex;align-items:center;justify-content:center;margin-top:.5mm}
.legend .n.q{background:var(--gold)}
.legend .e{font-weight:700;font-size:10pt;color:var(--ink);line-height:1.25}
.legend .a{font-family:AmiriQ;font-size:11pt;color:var(--ink-ar);direction:rtl;text-align:right;line-height:1.38}
.legend .a bdi{font-family:Mada}
/* ---------- glossary ---------- */
.gl{column-count:2;column-gap:8mm}
.gl div{break-inside:avoid;display:flex;align-items:baseline;gap:1.6mm;padding:1.05mm 0}
.gl .e{font-weight:700;font-size:10.5pt;color:var(--burg)}
.gl .d{flex:1;border-bottom:.4mm dotted var(--gold-l);transform:translateY(-1mm);min-width:4mm}
.gl .a{font-family:AmiriQ;font-size:12.5pt;color:var(--ink-ar)}
.gl .l{column-span:all;font-family:Playfair;font-style:italic;font-weight:900;color:var(--gold);font-size:13pt;border-bottom:.3mm solid var(--line);margin:1mm 0}
/* ---------- summary ---------- */
.sm{display:grid;grid-template-columns:10mm 1fr;gap:3mm;margin:0 0 3mm;break-inside:avoid}
.sm .n{font-family:Playfair;font-style:italic;font-weight:900;font-size:22pt;color:var(--gold);line-height:1;text-align:right}
.sm .en{font-size:13.5pt}
.sm .ar{font-size:14pt}
.sm .t{border-left:.4mm solid var(--gold-l);padding-left:3mm}
/* ---------- symbols ---------- */
.sym{display:flex;flex-direction:column;align-items:center;justify-content:center;padding:3mm 4mm 1mm}
.sym .s{width:34mm}
.sym .l{font-family:Cormorant;font-weight:700;letter-spacing:.18em;font-size:10.5pt;color:var(--burg);margin-top:1mm}
.sym .la{font-weight:800;font-size:10.5pt;color:var(--ink-ar)}
"""

# ================================================================ cover
def cover(kind="booklet"):
    cards = [("microscope", "Practical Section", "القسم العملي"), ("clipboard", "Stage 4", "المرحلة الرابعة"), ("person", "Lecturer", LECTURER)]
    cc = "".join(f'<div class="cv-cardwrap"><div class="cv-card"><div class="k">{k}</div><div class="v" dir="rtl">{v}</div>'
                 f'<div class="o">{divider("20mm")}</div></div><div class="ic" style="position:absolute;left:50%;top:7mm;transform:translate(-50%,-50%);width:15mm;height:15mm;border-radius:50%;background:var(--burg);box-shadow:0 0 0 .7mm #F7EFE2,0 0 0 1.3mm var(--gold);display:flex;align-items:center;justify-content:center"><div style="width:8.5mm;height:8.5mm">{icon(i, "#E9D3A6", "100%", 1.5)}</div></div></div>'
                 for i, k, v in cards)
    corners = (f'<div class="cv-cn" style="left:4mm;top:4mm">{corner(24)}</div><div class="cv-cn" style="right:4mm;top:4mm">{corner(24, rot=90)}</div>'
               f'<div class="cv-cn" style="right:4mm;bottom:4mm">{corner(24, rot=180)}</div><div class="cv-cn" style="left:4mm;bottom:4mm">{corner(24, rot=270)}</div>')
    return f'''<section class="page cover">
<div class="cv-arch"></div><div class="cv-fr"></div><div class="cv-fr2"></div>{corners}
<img class="cv-logo" src="assets/logo.png">
<div class="cv-tg"><i><span style="width:4.2mm;height:4.2mm;display:flex">{icon("plane", "#F3E3C4", "100%", 1.8)}</span></i>t.me/BIOS0t</div>
<div class="cv-ar-brand"><span class="d"></span><span>بايوس &nbsp;|&nbsp; ترجمة وتعديل الملازم</span><span class="d"></span></div>
<div class="cv-t0">DIAGNOSTIC</div>
<div class="cv-t1">MICROBIOLOGY</div>
<div class="cv-div">{divider("70mm", "#8C6A33")}</div>
<div class="cv-t2" dir="rtl">{SUBJ_AR}</div>
<div class="cv-t3"><span class="ln"></span><span class="e">LAB 1 · {TITLE_EN.upper()}</span><span class="ln"></span></div>
<div class="cv-t4" dir="rtl">العملي ١ — {TITLE_AR}</div>
<div class="cv-med">{medallion(uid="cvm")}</div>
<div class="cv-cards">{cc}</div>
</section>'''

HDR = (f'<div class="hdr"><div class="brand"><span class="bw">BIOS</span><span class="ba">بايوس</span></div>'
       f'<div class="hc"><div class="t1">{SUBJ_EN}</div><div class="t2" dir="rtl">{SUBJ_AR}</div></div>'
       f'<div class="hr"><span class="lab">Lab 1</span><span class="sep"></span><span dir="rtl">العملي ١</span></div></div>')

# ================================================================ components
def rg_card(n, cls, te, ta, de, da):
    return (f'<div class="rg {cls}"><div class="rg-h"><span class="rn">{n}</span><div class="rt">'
            f'<span class="rte" dir="ltr">{md(te)}</span><span class="rta" dir="rtl">{md(ta)}</span></div></div>'
            f'<div class="rg-s"><span dir="ltr">Biosafety level {n}</span><span dir="rtl">مستوى السلامة الحيوية {ard(n)}</span></div>'
            f'<div class="c-en"><span class="tag">EN</span>{en(de)}</div><div class="c-ar"><span class="tag tag-ar">ع</span>{ar(da)}</div></div>')

RG = [
 (1, "rg1", "Risk group 1 — (Minimal risk)", "مجموعة الخطورة 1 — (خطورة ضئيلة)",
  "**Non-pathogenic** factors in healthy people and adults (with little or no risk). *E.coli* , *Bacillus Subtilis*",
  "عوامل **غير مُمرِضة** للأشخاص الأصحّاء والبالغين (ذات خطورة قليلة أو معدومة). `*E.coli*`، `*Bacillus Subtilis*`."),
 (2, "rg2", "Risk group 2 — (Moderate risk)", "مجموعة الخطورة 2 — (خطورة متوسطة)",
  "Factors related to **human infection** and **treatment is possible** in this case (moderate risk and !!limited!! risk of spread). *E.coli* pathogenic strain , *Brucella spp.* , *Salmonella spp.*",
  "عوامل مرتبطة **بإصابة الإنسان بالعدوى**، و**يكون العلاج ممكنًا** في هذه الحالة (خطورة متوسطة وخطر انتشار !!محدود!!). السلالة المُمرِضة من `*E.coli*`، و`*Brucella spp.*`، و`*Salmonella spp.*`."),
 (3, "rg3", "Risk group 3 — (High risk)", "مجموعة الخطورة 3 — (خطورة عالية)",
  "Factors that cause serious and fatal infections to humans and their **treatment is not easy**, specially for immunosuppressed persons (with a high risk for individuals). *Salmonella typhi*. *Mycobacterium tuberculosis*.",
  "عوامل تسبّب عدوى خطيرة ومميتة للإنسان و**علاجها ليس سهلًا**، خصوصًا للأشخاص المثبَّطة مناعتهم (مع خطورة عالية على الأفراد). `*Salmonella typhi*`. `*Mycobacterium tuberculosis*`."),
 (4, "rg4", "Risk group 4 — (Extreme risk)", "مجموعة الخطورة 4 — (خطورة قصوى)",
  "Factor that are fatal to humans are easily transmitted from … [[cut]]",
  "عوامل مميتة للإنسان وتنتقل بسهولة من … [[قطع]]"),
]

LADDER = ('<div class="ladder">' + "".join(
    f'<div class="step s{n}"><span class="bsl"><span>BSL</span><b>{n}</b></span><span class="num">{n}</span>'
    f'<span class="lv">Risk group</span><span class="rkw"><span class="rk">{rk}</span><span class="rka" dir="rtl">{rka}</span></span></div>'
    for n, rk, rka in [(1, "Minimal", "ضئيلة"), (2, "Moderate", "متوسطة"), (3, "High", "عالية"), (4, "Extreme", "قصوى")])
    + '</div><div class="ladder-base"></div>'
    '<div class="ladder-ax"><span dir="ltr">Risk increases</span><span class="arr"></span><span class="ar2" dir="rtl">الخطورة تزداد</span></div>'
    '<div class="ex">'
    '<div><b>Examples</b><i>E.coli</i>, <i>Bacillus Subtilis</i></div>'
    '<div><b>Examples</b><i>E.coli</i> pathogenic strain, <i>Brucella spp.</i>, <i>Salmonella spp.</i></div>'
    '<div><b>Examples</b><i>Salmonella typhi</i>, <i>Mycobacterium tuberculosis</i></div>'
    '<div><b>Examples</b><span class="muted">— not given (text cut off)</span></div></div>')

def cmp_card(ic, te, ta, rows, meter):
    m = "".join(f'<i class="{"on" if k < meter else ""}"></i>' for k in range(4))
    r = "".join(f'<div class="row"><span class="k">{k}<span class="ka">{ka}</span></span><div>{en(ve) if ve else ""}<div class="va">{md(va)}</div></div></div>'
                for k, ka, ve, va in rows)
    return (f'<div class="cgc"><div class="meter">{m}</div><div class="top"><div class="ic">{icon(ic, "#EBD6A9", "100%", 1.6)}</div>'
            f'<div><div class="te">{te}</div><div class="ta" dir="rtl">{ta}</div></div></div>{r}</div>')

CMP = ('<div class="cg">'
  + cmp_card("flame", "Sterilization", "التعقيم", [("Removes", "يزيل", "**All** living organisms (incl. spores)", "**جميع** الكائنات الحية (ومنها الأبواغ)"), ("Method", "الطريقة", "Complete killing or removal", "قتل أو إزالة كاملة")], 4)
  + cmp_card("spray", "Disinfection", "التطهير", [("Removes", "يزيل", "Pathogens — **not bacterial spores**", "المُمرِضات — **لا الأبواغ البكتيرية**"), ("Used on", "يُطبَّق على", "Inanimate objects", "الأجسام غير الحيّة")], 3)
  + cmp_card("hand", "Antiseptics", "المطهّرات الموضعية", [("Action", "العمل", "Destroy or inhibit pathogens", "تدمير المُمرِضات أو تثبيطها"), ("Used on", "يُطبَّق على", "**Body surfaces**", "**أسطح الجسم**")], 2)
  + cmp_card("drops", "Decontamination", "إزالة التلوّث", [("Removes", "يزيل", "**Most** microbes (mechanical)", "**معظم** الميكروبات (إزالة ميكانيكية)"), ("Using", "باستخدام", "Washing, heat or disinfectants", "الغسل أو الحرارة أو المطهّرات")], 2)
  + '</div>')

TREE = ('<div class="tree"><div class="root"><div class="e">Bio risk assessment</div><div class="a" dir="rtl">تقييم الخطر البيولوجي</div></div>'
        '<div class="stem"></div><div class="bar"></div><div class="kids">'
        '<div class="kid"><div class="h"><span class="e">Biosafety risks</span><span class="a" dir="rtl">مخاطر السلامة الحيوية</span></div>'
        f'<div class="b">{en("Risks of **accidental infection**.")}{ar("مخاطر **العدوى العَرَضية**.")}</div></div>'
        '<div class="kid"><div class="h"><span class="e">Laboratory biosecurity risks</span><span class="a" dir="rtl">مخاطر الأمن الحيوي</span></div>'
        '<div class="b"><div class="chips" dir="ltr"><span>unauthorized access</span><span>loss</span><span>theft</span><span>misuse</span><span>diversion</span><span>intentional release</span></div>'
        '<div class="chips" dir="rtl" style="margin-top:1.4mm"><span>الوصول غير المصرَّح به</span><span>الفقدان</span><span>السرقة</span><span>إساءة الاستخدام</span><span>التحويل</span><span>الإطلاق المتعمَّد</span></div></div></div>'
        '</div></div>')

# cabinet labels: (n, en, ar, x%, y%, partial)
CAB = [
 (1, "Class I biosafety cabinet", "كابينة السلامة الحيوية من الفئة الأولى", 8.5, 34, False),
 (2, "Mini Biosafety cabinet", "كابينة سلامة حيوية مصغّرة", 25.5, 34, False),
 (3, "[Class] II Biosafety cabinet *", "كابينة السلامة الحيوية من الفئة الثانية *", 40.5, 34, True),
 (4, "[…] Bio Cabinet *", "كابينة سلامة حيوية *", 56, 34, True),
 (5, "[…]F Biosafety cabinet *", "كابينة سلامة حيوية *", 71.5, 34, True),
 (6, "Class III Biosafety Cabinet", "كابينة السلامة الحيوية من الفئة الثالثة", 89, 34, False),
 (7, "Ducted and Ductless Fume Hood", "خزانة الأبخرة ذات القناة وعديمة القناة", 15, 87, False),
 (8, "Laminar flow Cabinet", "كابينة التدفّق الصفائحي", 40, 87, False),
 (9, "PCR Cabinet", "كابينة تفاعل البلمرة المتسلسل `(PCR)`", 58, 87, False),
 (10, "Autoclave", "جهاز التعقيم بالبخار المضغوط (الأوتوكليف)", 73.5, 87, False),
 (11, "Incubator", "الحاضنة", 88.5, 87, False),
]
CAB_IMG = ('<div class="cab"><img src="assets/cabinets.jpg">' + "".join(
    f'<span class="pin{" q" if q else ""}" style="left:{x}%;top:{y}%">{n}</span>' for n, e, a, x, y, q in CAB) + "</div>")
CAB_LEG = ('<div class="legend">' + "".join(
    f'<div><span class="n{" q" if q else ""}">{n}</span><span><span class="e" dir="ltr">{md(e)}</span><span class="a" style="display:block">{md(a)}</span></span></div>'
    for n, e, a, x, y, q in CAB)
    + '<div style="border:0;display:block;font-size:8pt;color:var(--muted);line-height:1.35"><span dir="ltr" style="display:block">* Labels 3–5 are partly hidden by a watermark in the original image; only the readable parts are shown.</span>'
    '<span dir="rtl" style="display:block;text-align:right">* التسميات 3–5 مغطّاة جزئيًا بعلامة مائية في الصورة الأصلية، فكُتب الجزء المقروء منها فقط.</span></div>' + "</div>")

SAFE_ICONS = ["coat", "gloves", "nofood", "hair", "dish", "wash", "tools", "waste"]

# ================================================================ pages
P = []
P.append((("1", "Biosafety Levels", "مستويات السلامة الحيوية"),
  sec("1", "Biosafety Levels", "مستويات السلامة الحيوية", "shield")
  + '<div style="display:flex;gap:5mm;align-items:flex-start"><div style="flex:1">'
  + card("**Biosafety levels**: They are principles and application used to protect laboratory workers and the surrounding environment from exposure to danger while working with living organisms.",
         "**مستويات السلامة الحيوية**: هي مبادئ وتطبيقات تُستخدم لحماية العاملين في المختبر والبيئة المحيطة من التعرّض للخطر أثناء العمل مع الكائنات الحية.")
  + card("**It aims to**: provide the highest level of protection and the lowest range of exposure.",
         "**تهدف إلى**: توفير أعلى مستوى من الحماية وأدنى مدى من التعرّض.")
  + '</div>' + fig("assets/labsafety.jpg", "Lab safety", "سلامة المختبر", w="36mm") + '</div>'
))
P.append((("2", "Risk Groups", "مجموعات الخطورة"),
  sec("2", "Risk Groups", "مجموعات الخطورة", "risk")
  + card("**Risk groups:** are used to assess risk, determine its source and how to deal with it , includes 4 groups:",
         "**مجموعات الخطورة:** تُستخدم لتقييم الخطر، وتحديد مصدره وكيفية التعامل معه، وتشمل 4 مجموعات:")
  + h2("The risk ladder at a glance", "سُلَّم الخطورة بنظرة واحدة") + LADDER
  + box("memory", pair("Risk group number = Biosafety level number (RG 1 → BSL 1 … RG 4 → BSL 4).",
                       "رقم مجموعة الخطورة = رقم مستوى السلامة الحيوية (المجموعة 1 ← المستوى 1 … المجموعة 4 ← المستوى 4)."))
))
P.append((None, rg_card(*RG[0]) + rg_card(*RG[1])))
P.append((None, rg_card(*RG[2]) + rg_card(*RG[3])
  + box("note", pair("The rest of the Risk group 4 description is cut off in the original slide. For reference, the WHO *Laboratory Biosafety Manual* describes Risk Group 4 agents as usually causing serious disease, readily transmitted from one individual to another, with effective treatment and preventive measures not usually available.",
                     "بقية وصف مجموعة الخطورة 4 مقطوعة في الشريحة الأصلية. وللاستئناس: يصف دليل السلامة الحيوية المختبرية لمنظمة الصحة العالمية عوامل المجموعة 4 بأنها تسبّب عادةً مرضًا خطيرًا، وتنتقل بسهولة من فرد إلى آخر، ولا تتوفر لها عادةً علاجات أو وسائل وقائية فعّالة."))
))
P.append((("3", "Biohazard Symbol", "رمز الخطر الحيوي"),
  sec("3", "Biohazard Symbol", "رمز الخطر الحيوي", "alert")
  + card("**Biohazard symbol**: it used to warn people of the potential for the presence dangerous biological materials such as :",
         "**رمز الخطر الحيوي**: يُستخدم لتحذير الأشخاص من احتمال وجود مواد بيولوجية خطرة، مثل:")
  + plain([("Cultures of pathogens.", "مزارع المُمرِضات (العوامل المسبّبة للأمراض)."),
           ("Human Blood and Tissue.", "دم الإنسان وأنسجته."),
           ("Corridors leading to the laboratories.", "الممرات المؤدية إلى المختبرات.")])
  + fig(None, "Warning symbols (redrawn in high resolution)", "رموز التحذير (أُعيد رسمها بدقة عالية)", w="150mm",
        inner='<div style="display:flex;justify-content:space-around">'
              f'<div class="sym"><div class="s">{biohazard()}</div><div class="l">BIOHAZARD</div><div class="la">الخطر الحيوي</div></div>'
              f'<div class="sym"><div class="s">{radiation()}</div><div class="l">RADIATION HAZARD</div><div class="la">خطر الإشعاع</div></div></div>')
))
SAFE = [tuple(x) for x in D["SAFE"]]
P.append((("4", "Laboratory Safety Considerations", "اعتبارات السلامة في المختبر"),
  sec("4", "Laboratory Safety Considerations", "اعتبارات السلامة في المختبر", "coat")
  + rules(SAFE[0:1], 1, SAFE_ICONS[0:1])
  + fig("assets/ppe.jpg", "Personal protective equipment", "معدّات الحماية الشخصية", w="106mm")
  + rules(SAFE[1:2], 2, SAFE_ICONS[1:2])
))
P.append((None,
  rules(SAFE[2:5], 3, SAFE_ICONS[2:5])
  + figrow(fig("assets/nofood.jpg", "No food or drink", "ممنوع الطعام والشراب", w="58mm"),
           fig("assets/cultures.jpg", "Bacterial cultures", "مزارع بكتيرية", w="80mm"))
))
P.append((None,
  rules(SAFE[5:8], 6, SAFE_ICONS[5:8])
  + figrow(fig("assets/handwash.jpg", "Hand washing", "غسل اليدين", w="82mm"),
           fig("assets/disinfect.jpg", "Disinfecting instruments and surfaces", "تطهير الأدوات والأسطح", w="82mm"))
))
DEFS = [tuple(x) for x in D["DEFS"]]
P.append((("5", "Sterilization & Related Terms", "التعقيم والمصطلحات المرتبطة"),
  sec("5", "Sterilization & Related Terms", "التعقيم والمصطلحات المرتبطة", "flame")
  + cards(DEFS)
))
P.append((None,
  h2("Four terms — one comparison", "أربعة مصطلحات — مقارنة واحدة") + CMP
  + box("memory", pair("**Anti**septics → on the **skin** (body surfaces); **Dis**infection → on **things** (inanimate objects). The bars show how much each one removes.",
                       "المطهّرات الموضعية `(Antiseptics)` ← على **الجلد** (أسطح الجسم)؛ التطهير `(Disinfection)` ← على **الأشياء** (الأجسام غير الحيّة). وتُظهر الأشرطة مقدار ما يزيله كلٌّ منها."))
))
P.append((("6", "Biological Laboratory & Bio Risk", "المختبر البيولوجي والخطر البيولوجي"),
  sec("6", "Biological Laboratory & Bio Risk", "المختبر البيولوجي والخطر البيولوجي", "lab")
  + cards([
    ("**Biological laboratory** :A facility within which microorganisms, their components or their derivatives are collected handled and/or stored.",
     "**المختبر البيولوجي**: منشأة تُجمَع فيها الكائنات الحية الدقيقة أو مكوّناتها أو مشتقّاتها، ويُتعامَل معها و/أو تُخزَّن."),
    ("**Bio risk** :The probability or chance that a particular adverse event :accidental infection or loss, theft, misuse, diversion or intentional release), possibly leading to harm.",
     "**الخطر البيولوجي**: احتمال أو فرصة وقوع حدث ضار معيّن (عدوى عَرَضية، أو فقدان، أو سرقة، أو إساءة استخدام، أو تحويل، أو إطلاق متعمَّد)، قد يؤدي إلى الضرر."),
  ])
))
P.append((None,
  cards([("**Bio risk assessment** : The process to identify acceptable and unacceptable risks (embracing **biosafety risks** (risks of accidental infection) and **laboratory biosecurity risks** (risks of unauthorized access, loss, theft, misuse, diversion or intentional release)) and their potential consequences.",
          "**تقييم الخطر البيولوجي**: عملية تحديد المخاطر المقبولة وغير المقبولة (وتشمل **مخاطر السلامة الحيوية** (مخاطر العدوى العَرَضية) و**مخاطر الأمن الحيوي المختبري** (مخاطر الوصول غير المصرَّح به، أو الفقدان، أو السرقة، أو إساءة الاستخدام، أو التحويل، أو الإطلاق المتعمَّد))، وعواقبها المحتملة.")])
  + h2("The definition as a diagram", "التعريف على شكل مخطط") + TREE
))
P.append((("7", "Biosafety Cabinet", "كابينة السلامة الحيوية"),
  sec("7", "Biosafety Cabinet", "كابينة السلامة الحيوية", "cabinet")
  + fig(None, "Biosafety cabinets and laboratory equipment", "كابينات السلامة الحيوية وأجهزة مختبرية", w="118mm", inner=CAB_IMG)
  + CAB_LEG
))
TERMS = [tuple(x) for x in D["TERMS"]]
GL = '<div class="gl">' + "".join(f'<div><span class="e" dir="ltr">{e}</span><span class="d"></span><span class="a" dir="rtl">{a}</span></div>' for e, a in sorted(TERMS)) + "</div>"
P.append((("★", "Key Terms", "أهم المصطلحات"), sec("★", "Key Terms", "أهم المصطلحات", "book", ("GLOSSARY", "المسرد")) + GL))
SUMMARY = [tuple(x) for x in D["SUMMARY"]]
def sm(items, start):
    return "".join(f'<div class="sm"><span class="n">{i}</span><div class="t">{en(e)}{ar(a)}</div></div>' for i, (e, a) in enumerate(items, start))
P.append((("★", "Lecture Summary", "ملخص المحاضرة"), sec("★", "Lecture Summary", "ملخص المحاضرة", "star", ("SUMMARY", "الخلاصة")) + sm(SUMMARY[:4], 1)))
P.append((None, h2("Lecture Summary (continued)", "ملخص المحاضرة (تتمة)") + sm(SUMMARY[4:], 5)))

# ================================================================ assemble
def build():
    pages = [cover()]
    num = 1
    body, toc = [], []
    for t, h in P:
        num += 1
        if t: toc.append((t, num + 1))
        body.append(page(h, HDR, num + 1))
    info = ('<div class="lc">'
            f'<div class="wide"><span class="k">Subject<small>المادة</small></span><span class="v"><span dir="ltr">{SUBJ_EN}</span><br><span dir="rtl" style="font-size:13pt">{SUBJ_AR}</span></span></div>'
            f'<div><span class="k">Stage<small>المرحلة</small></span><span class="v">The fourth stage · الرابعة</span></div>'
            f'<div><span class="k">Type<small>النوع</small></span><span class="v">Practical · عملي</span></div>'
            f'<div><span class="k">Lab no.<small>رقم العملي</small></span><span class="v">Lab 1 · العملي ١</span></div>'
            f'<div><span class="k">Lecturer<small>تدريسية المادة</small></span><span class="v">{LECTURER}</span></div>'
            f'<div class="wide"><span class="k">Title<small>العنوان</small></span><span class="v"><span dir="ltr">{TITLE_EN}</span><br><span dir="rtl" style="font-size:13pt">{TITLE_AR}</span></span></div>'
            '</div>')
    tl = ('<ul class="toc">' + "".join(
        f'<li><span class="n">{n if n != "★" else "✦"}</span><span class="te" dir="ltr">{e}</span><span class="dots"></span>'
        f'<span class="ta" dir="rtl">{a}</span><span class="p">{p}</span></li>' for (n, e, a), p in toc) + "</ul>")
    pages.append(page(sec("★", "Lecture Card", "بطاقة المحاضرة", "book", ("BIOS BOOKLET", "ملزمة بايوس")) + info + h2("Contents", "المحتويات") + tl, HDR, 2))
    pages += body
    return pages

if __name__ == "__main__":
    pages = build()
    open("booklet.html", "w").write(doc("Biosafety Booklet", pages, X))
    print("pages", len(pages))
