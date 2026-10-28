"""Five cover concepts, wineoat palette, Immunology Lab 1 data. Writes covers.html (one A4 page each)."""
D, M, L = "#4a2c34", "#c9b4a5", "#f7f1ee"
I = dict(subject_en="Practical Immunology", subject_ar="علم المناعة العملي",
         title_en="Safety, Introduction to Serology", title_ar="السلامة، مقدمة في علم الأمصال",
         kind_en="Practical", kind_ar="عملي", no="1", unit_en="Lab", unit_ar="العملي",
         stage_en="Third stage", stage_ar="المرحلة الثالثة", instructor="م.م. جنان خليل")

FONTS = "".join(f"@font-face{{font-family:Mada;src:url(Mada-{n}.ttf);font-weight:{w}}}" for n, w in
                [("Light", 300), ("Regular", 400), ("Medium", 500), ("SemiBold", 600), ("Bold", 700), ("ExtraBold", 800), ("Black", 900)])
FONTS += "@font-face{font-family:Amiri;src:url(AmiriQuran-Regular.ttf)}"
FONTS += "@font-face{font-family:Playfair;src:url(playfair-display-latin-900-italic.woff2);font-weight:900;font-style:italic}"
FONTS += "@font-face{font-family:PlayfairR;src:url(playfair-display-latin-700-normal.woff2);font-weight:700}"

BASE = FONTS + f"""
*{{box-sizing:border-box;margin:0;padding:0}}
@page{{size:A4;margin:0}}
body{{font-family:Mada;color:{D};-webkit-print-color-adjust:exact;print-color-adjust:exact;background:#ccc}}
.page{{width:210mm;height:297mm;position:relative;overflow:hidden;background:#fff;break-after:page}}
@media screen{{.page{{margin:8mm auto}}}}
.ar{{direction:rtl}}
.tag{{position:absolute;left:0;top:0;background:{D};color:{L};font-weight:800;font-size:9pt;padding:1.5mm 4mm;border-bottom-right-radius:3mm;z-index:9}}
"""


def info_cells(cls=""):
    rows = [("النوع", "Type", f'{I["kind_ar"]} · {I["kind_en"]}'),
            (I["unit_ar"], I["unit_en"], I["no"]),
            ("المرحلة", "Stage", f'{I["stage_ar"]}')]
    return "".join(f'<div class="cell {cls}"><small>{a} · {e}</small><b>{v}</b></div>' for a, e, v in rows)


# ---------------------------------------------------------------- 1 Classic centred
C1 = f"""
.c1{{background:{L}}}
.c1 .frame{{position:absolute;inset:10mm;border:.4mm solid {M};border-radius:4mm}}
.c1 .frame2{{position:absolute;inset:12.5mm;border:.25mm solid {M};border-radius:3mm;opacity:.7}}
.c1 .logo{{position:absolute;left:50%;top:26mm;transform:translateX(-50%);width:92mm}}
.c1 .rule{{position:absolute;left:50%;transform:translateX(-50%);width:110mm;border-top:.35mm solid {M}}}
.c1 .dot{{position:absolute;left:50%;transform:translate(-50%,-50%);width:3mm;height:3mm;background:{M};rotate:45deg}}
.c1 .subj{{position:absolute;left:0;right:0;top:112mm;text-align:center}}
.c1 .subj .e{{font-weight:800;font-size:26pt;letter-spacing:.01em}}
.c1 .subj .a{{font-weight:900;font-size:24pt;margin-top:1mm}}
.c1 .ttl{{position:absolute;left:30mm;right:30mm;top:152mm;background:{D};color:{L};border-radius:6mm;padding:4.5mm 8mm;text-align:center}}
.c1 .ttl .e{{font-weight:700;font-size:13pt}}
.c1 .ttl .a{{font-family:Amiri;font-size:16pt;margin-top:.5mm}}
.c1 .cells{{position:absolute;left:24mm;right:24mm;top:191mm;display:grid;grid-template-columns:1fr .7fr 1fr;gap:4mm}}
.cell{{background:#fff;border:.35mm solid {M};border-radius:3mm;padding:3mm 3mm;text-align:center}}
.cell small{{display:block;font-size:7.5pt;font-weight:600;opacity:.75}}
.cell b{{display:block;font-size:12.5pt;font-weight:800;margin-top:.8mm;direction:rtl}}
.c1 .ins{{position:absolute;left:0;right:0;top:226mm;text-align:center}}
.c1 .ins small{{font-size:8.5pt;font-weight:700;letter-spacing:.2em;opacity:.7}}
.c1 .ins b{{display:block;font-size:20pt;font-weight:900;margin-top:1mm;direction:rtl}}
.c1 .foot{{position:absolute;left:0;right:0;bottom:16mm;text-align:center;font-size:8.5pt;font-weight:700;letter-spacing:.08em;opacity:.8}}
"""
P1 = f"""<section class="page c1"><span class="tag">1</span><div class="frame"></div><div class="frame2"></div>
<img class="logo" src="logo_dark.png">
<div class="rule" style="top:104mm"></div><div class="dot" style="top:104mm"></div>
<div class="subj"><div class="e">{I["subject_en"]}</div><div class="a ar">{I["subject_ar"]}</div></div>
<div class="ttl"><div class="e">{I["title_en"]}</div><div class="a ar">{I["title_ar"]}</div></div>
<div class="cells">{info_cells()}</div>
<div class="rule" style="top:220mm;width:60mm"></div>
<div class="ins"><small>INSTRUCTOR · التدريسي</small><b>{I["instructor"]}</b></div>
<div class="foot">BIOS · Telegram @BIOS0t</div></section>"""

# ---------------------------------------------------------------- 2 Split panel
C2 = f"""
.c2 .side{{position:absolute;left:0;top:0;bottom:0;width:78mm;background:{D};color:{L}}}
.c2 .side .logo{{position:absolute;left:9mm;top:22mm;width:60mm}}
.c2 .side .num{{position:absolute;left:0;right:0;top:92mm;text-align:center}}
.c2 .side .num small{{display:block;font-size:10pt;font-weight:700;letter-spacing:.3em;color:{M}}}
.c2 .side .num b{{display:block;font-family:PlayfairR;font-size:120pt;line-height:1;color:{L}}}
.c2 .side .num i{{display:block;font-style:normal;font-size:13pt;font-weight:800;color:{M}}}
.c2 .side .kind{{position:absolute;left:14mm;right:14mm;top:186mm;border:.4mm solid {M};border-radius:20mm;text-align:center;padding:3mm;font-weight:800;font-size:12pt}}
.c2 .side .tg{{position:absolute;left:0;right:0;bottom:16mm;text-align:center;font-size:8.5pt;font-weight:700;color:{M}}}
.c2 .main{{position:absolute;left:78mm;right:0;top:0;bottom:0;background:{L};padding:30mm 16mm 0 16mm}}
.c2 .bar{{width:22mm;height:1.6mm;background:{M};border-radius:1mm;margin-bottom:7mm}}
.c2 .se{{font-size:10pt;font-weight:700;letter-spacing:.18em;opacity:.75}}
.c2 .s{{font-weight:900;font-size:25pt;line-height:1.15;margin-top:2mm}}
.c2 .sa{{font-weight:900;font-size:23pt;margin-top:1mm}}
.c2 .t{{margin-top:34mm;border-right:1.6mm solid {M};padding-right:5mm;text-align:right}}
.c2 .t .a{{font-family:Amiri;font-size:21pt;line-height:1.5}}
.c2 .t .e{{font-size:13.5pt;font-weight:700;margin-top:2mm;direction:ltr}}
.c2 .meta{{position:absolute;left:16mm;right:16mm;top:150mm}}
.c2 .wm{{position:absolute;left:16mm;right:16mm;bottom:22mm;width:calc(100% - 32mm);opacity:.09}}
.c2 .meta div{{display:flex;justify-content:space-between;align-items:baseline;border-bottom:.3mm solid {M};padding:3.2mm 0}}
.c2 .meta small{{font-size:8.5pt;font-weight:700;opacity:.7}}
.c2 .meta b{{font-size:13pt;font-weight:800;direction:rtl}}
"""
P2 = f"""<section class="page c2"><span class="tag">2</span>
<div class="side"><img class="logo" src="logo_light.png">
<div class="num"><small>{I["unit_en"].upper()}</small><b>0{I["no"]}</b><i class="ar">{I["unit_ar"]} {I["no"]}</i></div>
<div class="kind ar">{I["kind_ar"]} · {I["kind_en"]}</div><div class="tg">Telegram @BIOS0t</div></div>
<div class="main"><div class="bar"></div><div class="se">SUBJECT · المادة</div>
<div class="s">{I["subject_en"]}</div><div class="sa ar">{I["subject_ar"]}</div>
<div class="t"><div class="a ar">{I["title_ar"]}</div><div class="e">{I["title_en"]}</div></div>
<div class="meta"><div><small>Stage · المرحلة</small><b>{I["stage_ar"]}</b></div>
<div><small>Instructor · التدريسي</small><b>{I["instructor"]}</b></div></div>
<img class="wm" src="logo_dark.png"></div></section>"""

# ---------------------------------------------------------------- 3 Arch window
C3 = f"""
.c3{{background:#fff}}
.c3 .arch{{position:absolute;left:28mm;right:28mm;top:18mm;height:170mm;background:{L};border:.5mm solid {M};border-radius:77mm 77mm 4mm 4mm}}
.c3 .arch2{{position:absolute;left:33mm;right:33mm;top:23mm;height:160mm;border:.3mm solid {M};border-radius:72mm 72mm 3mm 3mm;opacity:.6}}
.c3 .logo{{position:absolute;left:50%;top:40mm;transform:translateX(-50%);width:84mm}}
.c3 .lec{{position:absolute;left:0;right:0;top:100mm;text-align:center;font-size:10pt;font-weight:800;letter-spacing:.25em;color:{D};opacity:.8}}
.c3 .subj{{position:absolute;left:0;right:0;top:111mm;text-align:center}}
.c3 .subj .e{{font-weight:900;font-size:24pt}}
.c3 .subj .a{{font-weight:900;font-size:22pt}}
.c3 .tt{{position:absolute;left:40mm;right:40mm;top:145mm;text-align:center;border-top:.35mm solid {M};padding-top:5mm}}
.c3 .tt .a{{font-family:Amiri;font-size:17pt}}
.c3 .tt .e{{font-weight:700;font-size:12pt;margin-top:1mm}}
.c3 .cells{{position:absolute;left:28mm;right:28mm;top:198mm;display:grid;grid-template-columns:1fr 1fr 1fr;gap:0;border:.35mm solid {M};border-radius:3mm;overflow:hidden}}
.c3 .cells .cell{{border:0;border-radius:0;border-left:.35mm solid {M}}}
.c3 .cells .cell:first-child{{border-left:0}}
.c3 .ins{{position:absolute;left:28mm;right:28mm;top:228mm;background:{D};color:{L};border-radius:3mm;padding:5mm 7mm;display:flex;justify-content:space-between;align-items:center}}
.c3 .ins small{{font-size:8.5pt;font-weight:700;color:{M}}}
.c3 .ins b{{font-size:18pt;font-weight:900;direction:rtl}}
.c3 .foot{{position:absolute;left:0;right:0;bottom:14mm;text-align:center;font-size:8.5pt;font-weight:700;opacity:.8}}
"""
P3 = f"""<section class="page c3"><span class="tag">3</span><div class="arch"></div><div class="arch2"></div>
<img class="logo" src="logo_dark.png">
<div class="lec">{I["unit_en"].upper()} {I["no"]} · {I["unit_ar"]} {I["no"]}</div>
<div class="subj"><div class="e">{I["subject_en"]}</div><div class="a ar">{I["subject_ar"]}</div></div>
<div class="tt"><div class="a ar">{I["title_ar"]}</div><div class="e">{I["title_en"]}</div></div>
<div class="cells">{info_cells()}</div>
<div class="ins"><small>Instructor<br>التدريسي</small><b>{I["instructor"]}</b></div>
<div class="foot">BIOS · Telegram @BIOS0t</div></section>"""

# ---------------------------------------------------------------- 4 Big number editorial
C4 = f"""
.c4{{background:{L}}}
.c4 .top{{position:absolute;left:0;right:0;top:0;height:16mm;background:{D}}}
.c4 .logo{{position:absolute;right:16mm;top:24mm;width:62mm}}
.c4 .kind{{position:absolute;left:16mm;top:30mm;background:{D};color:{L};font-weight:800;font-size:11pt;border-radius:10mm;padding:2mm 6mm}}
.c4 .stage{{position:absolute;left:16mm;top:43mm;font-weight:800;font-size:11pt;border:.4mm solid {M};border-radius:10mm;padding:1.6mm 6mm}}
.c4 .big{{position:absolute;left:10mm;top:62mm;font-family:PlayfairR;font-size:230pt;line-height:1;color:transparent;-webkit-text-stroke:.8mm {M}}}
.c4 .bigl{{position:absolute;left:18mm;top:150mm;font-size:12pt;font-weight:800;letter-spacing:.3em}}
.c4 .blk{{position:absolute;left:16mm;right:16mm;top:166mm;background:#fff;border-radius:4mm;padding:9mm 10mm;box-shadow:0 .6mm 0 {M}}}
.c4 .blk .se{{font-size:9pt;font-weight:700;letter-spacing:.15em;opacity:.7}}
.c4 .blk .s{{display:flex;justify-content:space-between;align-items:baseline;font-weight:900;font-size:21pt;margin-top:1.5mm}}
.c4 .blk hr{{border:0;border-top:.35mm solid {M};margin:5mm 0}}
.c4 .blk .t{{display:flex;justify-content:space-between;align-items:baseline;gap:6mm}}
.c4 .blk .t .e{{font-weight:700;font-size:13pt}}
.c4 .blk .t .a{{font-family:Amiri;font-size:17pt}}
.c4 .ins{{position:absolute;left:16mm;right:16mm;top:238mm;display:flex;justify-content:space-between;align-items:center;border-top:.35mm solid {M};padding-top:5mm}}
.c4 .ins small{{font-size:9pt;font-weight:700;opacity:.75}}
.c4 .ins b{{font-size:19pt;font-weight:900;direction:rtl}}
.c4 .bot{{position:absolute;left:0;right:0;bottom:0;height:14mm;background:{D};color:{L};display:flex;align-items:center;justify-content:space-between;padding:0 16mm;font-size:9pt;font-weight:700}}
.c4 .bot b{{font-family:Playfair;font-style:italic;font-weight:900;font-size:15pt;color:{M}}}
"""
P4 = f"""<section class="page c4"><span class="tag">4</span><div class="top"></div>
<img class="logo" src="logo_dark.png">
<div class="kind ar">{I["kind_ar"]} · {I["kind_en"]}</div><div class="stage ar">{I["stage_ar"]}</div>
<div class="big">0{I["no"]}</div><div class="bigl">{I["unit_en"].upper()} · <span class="ar">{I["unit_ar"]}</span></div>
<div class="blk"><div class="se">SUBJECT · المادة</div><div class="s"><span>{I["subject_en"]}</span><span class="ar">{I["subject_ar"]}</span></div>
<hr><div class="t"><span class="e">{I["title_en"]}</span><span class="a ar">{I["title_ar"]}</span></div></div>
<div class="ins"><small>Instructor · التدريسي</small><b>{I["instructor"]}</b></div>
<div class="bot"><b>BIOS</b><span>Telegram @BIOS0t</span></div></section>"""

# ---------------------------------------------------------------- 5 Minimal band
C5 = f"""
.c5{{background:#fff}}
.c5 .band{{position:absolute;left:0;right:0;top:0;height:118mm;background:{D}}}
.c5 .band .logo{{position:absolute;left:50%;top:18mm;transform:translateX(-50%);width:96mm}}
.c5 .wave{{position:absolute;left:-10mm;right:-10mm;top:104mm;height:28mm;background:{L};border-radius:50% 50% 0 0/100% 100% 0 0}}
.c5 .pill{{position:absolute;left:50%;top:111mm;transform:translateX(-50%);background:{M};color:{D};font-weight:800;font-size:11pt;border-radius:10mm;padding:2.2mm 8mm;white-space:nowrap}}
.c5 .body{{position:absolute;left:0;right:0;top:117mm;bottom:0;background:{L}}}
.c5 .subj{{position:absolute;left:0;right:0;top:142mm;text-align:center}}
.c5 .subj .e{{font-weight:900;font-size:25pt}}
.c5 .subj .a{{font-weight:900;font-size:23pt}}
.c5 .tt{{position:absolute;left:0;right:0;top:182mm;text-align:center}}
.c5 .tt .a{{font-family:Amiri;font-size:19pt}}
.c5 .tt .e{{font-weight:700;font-size:13pt;opacity:.9}}
.c5 .orn{{position:absolute;left:50%;top:175mm;transform:translateX(-50%);display:flex;gap:2mm;align-items:center}}
.c5 .orn i{{width:16mm;height:.35mm;background:{M}}}.c5 .orn s{{width:2.4mm;height:2.4mm;background:{M};rotate:45deg}}
.c5 .cells{{position:absolute;left:22mm;right:22mm;top:216mm;display:grid;grid-template-columns:1fr 1fr;gap:4mm}}
.c5 .cells .cell{{text-align:right;display:flex;justify-content:space-between;align-items:center;padding:3.5mm 5mm}}
.c5 .cells .cell b{{margin:0}}
.c5 .foot{{position:absolute;left:0;right:0;bottom:13mm;text-align:center;font-size:8.5pt;font-weight:700;opacity:.8}}
"""
cells5 = (f'<div class="cell"><small>المادة النوع · Type</small><b>{I["kind_ar"]} · {I["kind_en"]}</b></div>'
          f'<div class="cell"><small>المرحلة · Stage</small><b>{I["stage_ar"]}</b></div>'
          f'<div class="cell" style="grid-column:1/-1"><small>التدريسي · Instructor</small><b style="font-size:16pt">{I["instructor"]}</b></div>')
cells5 = cells5.replace("المادة النوع", "النوع")
P5 = f"""<section class="page c5"><span class="tag">5</span><div class="band"><img class="logo" src="logo_light.png"></div>
<div class="body"></div><div class="wave"></div>
<div class="pill">{I["unit_en"]} {I["no"]} · <span class="ar">{I["unit_ar"]} {I["no"]}</span></div>
<div class="subj"><div class="e">{I["subject_en"]}</div><div class="a ar">{I["subject_ar"]}</div></div>
<div class="orn"><i></i><s></s><i></i></div>
<div class="tt"><div class="a ar">{I["title_ar"]}</div><div class="e">{I["title_en"]}</div></div>
<div class="cells">{cells5}</div>
<div class="foot">BIOS · Telegram @BIOS0t</div></section>"""

open("covers.html", "w").write(f"<!doctype html><meta charset=utf-8><style>{BASE}{C1}{C2}{C3}{C4}{C5}</style>{P1}{P2}{P3}{P4}{P5}")
print("ok")
