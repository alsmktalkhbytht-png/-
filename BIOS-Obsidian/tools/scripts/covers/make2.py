"""Five refined variations of cover 1 (classic framed, centred). Writes covers2.html."""
import importlib.util, sys
spec = importlib.util.spec_from_file_location("m1", "make.py"); m1 = importlib.util.module_from_spec(spec)
sys.argv = ["x"]; spec.loader.exec_module(m1)          # reuse palette, fonts, data (also rewrites covers.html; harmless)
D, M, L, I, BASE = m1.D, m1.M, m1.L, m1.I, m1.BASE


def corners(inset, size, w=".5mm"):
    """Four L-shaped corner ornaments."""
    out = ""
    for v, h in (("top", "left"), ("top", "right"), ("bottom", "left"), ("bottom", "right")):
        out += (f'<i style="position:absolute;{v}:{inset};{h}:{inset};width:{size};height:{size};'
                f'border-{v}:{w} solid {D};border-{h}:{w} solid {D}"></i>')
    return out


def diamond(top, size="3mm"):
    return (f'<div style="position:absolute;left:50%;top:{top};transform:translate(-50%,-50%);display:flex;align-items:center;gap:2.5mm">'
            f'<span style="width:22mm;height:.35mm;background:{M}"></span><span style="width:{size};height:{size};background:{M};rotate:45deg"></span>'
            f'<span style="width:22mm;height:.35mm;background:{M}"></span></div>')


def row3(style=""):
    items = [("النوع · Type", f'{I["kind_ar"]} · {I["kind_en"]}'), (f'{I["unit_ar"]} · {I["unit_en"]}', I["no"]), ("المرحلة · Stage", I["stage_ar"])]
    return "".join(f'<div><small>{a}</small><b>{v}</b></div>' for a, v in items)


CSS = f"""
.v{{background:{L}}}
.v .fr{{position:absolute;inset:11mm;border:.35mm solid {M}}}
.v .logo{{position:absolute;left:50%;transform:translateX(-50%)}}
.v .subj{{position:absolute;left:0;right:0;text-align:center}}
.v .subj .e{{font-weight:800;font-size:25pt}}
.v .subj .a{{font-weight:900;font-size:23pt;margin-top:.5mm;direction:rtl}}
.v .lbl{{font-size:8pt;font-weight:700;letter-spacing:.22em;opacity:.7}}
.v .ins{{position:absolute;left:0;right:0;text-align:center}}
.v .ins b{{display:block;font-size:20pt;font-weight:900;margin-top:1.2mm;direction:rtl}}
.v .foot{{position:absolute;left:0;right:0;bottom:17mm;text-align:center;font-size:8.5pt;font-weight:700;letter-spacing:.06em;opacity:.8}}
.row{{position:absolute;display:flex;justify-content:center;align-items:stretch}}
.row>div{{text-align:center;padding:0 7mm}}
.row>div+div{{border-left:.35mm solid {M}}}
.row small{{display:block;font-size:7.8pt;font-weight:700;opacity:.7}}
.row b{{display:block;font-size:13pt;font-weight:800;margin-top:1mm;direction:rtl}}
"""

# A — corner ornaments, outlined title, divided row
A = f"""<section class="page v"><span class="tag">1A</span><div class="fr"></div>{corners("8mm", "14mm")}
<img class="logo" src="logo_dark.png" style="top:28mm;width:88mm">
{diamond("104mm")}
<div class="subj" style="top:112mm"><div class="e">{I["subject_en"]}</div><div class="a">{I["subject_ar"]}</div></div>
<div style="position:absolute;left:32mm;right:32mm;top:150mm;border:.45mm solid {D};border-radius:3mm;padding:5mm 8mm;text-align:center;background:#fff">
 <div class="lbl">LECTURE TITLE · عنوان المحاضرة</div>
 <div style="font-family:Amiri;font-size:18pt;margin-top:1.5mm;direction:rtl">{I["title_ar"]}</div>
 <div style="font-weight:700;font-size:12.5pt;margin-top:.5mm">{I["title_en"]}</div></div>
<div class="row" style="left:20mm;right:20mm;top:197mm">{row3()}</div>
{diamond("223mm", "2.4mm")}
<div class="ins" style="top:230mm"><div class="lbl">INSTRUCTOR · التدريسي</div><b>{I["instructor"]}</b></div>
<div class="foot">BIOS · Telegram @BIOS0t</div></section>"""

# B — number badge on the title box, filled title, chips
B = f"""<section class="page v"><span class="tag">1B</span><div class="fr"></div><div class="fr" style="inset:13.5mm;opacity:.6"></div>
<img class="logo" src="logo_dark.png" style="top:26mm;width:90mm">
<div class="subj" style="top:106mm"><div class="e">{I["subject_en"]}</div><div class="a">{I["subject_ar"]}</div></div>
<div style="position:absolute;left:30mm;right:30mm;top:150mm;background:{D};color:{L};border-radius:4mm;padding:9mm 8mm 6mm;text-align:center">
 <div style="font-family:Amiri;font-size:19pt;direction:rtl">{I["title_ar"]}</div>
 <div style="font-weight:700;font-size:12.5pt;margin-top:.5mm;color:{M}">{I["title_en"]}</div></div>
<div style="position:absolute;left:50%;top:150mm;transform:translate(-50%,-50%);background:{M};color:{D};border:1mm solid {L};border-radius:10mm;padding:1.5mm 7mm;font-weight:900;font-size:12pt;white-space:nowrap">
 {I["unit_en"].upper()} {I["no"]} · <span style="direction:rtl">{I["unit_ar"]} {I["no"]}</span></div>
<div style="position:absolute;left:0;right:0;top:193mm;display:flex;justify-content:center;gap:5mm">
 <div style="border:.35mm solid {M};background:#fff;border-radius:10mm;padding:2.4mm 7mm;font-weight:800;font-size:12pt;direction:rtl">{I["kind_ar"]} · {I["kind_en"]}</div>
 <div style="border:.35mm solid {M};background:#fff;border-radius:10mm;padding:2.4mm 7mm;font-weight:800;font-size:12pt;direction:rtl">{I["stage_ar"]}</div></div>
<div style="position:absolute;left:60mm;right:60mm;top:216mm;border-top:.35mm solid {M}"></div>
<div class="ins" style="top:222mm"><div class="lbl">INSTRUCTOR · التدريسي</div><b>{I["instructor"]}</b></div>
<div class="foot">BIOS · Telegram @BIOS0t</div></section>"""

# C — logo medallion, ornamental rules around the title, details table
C = f"""<section class="page v"><span class="tag">1C</span><div class="fr"></div>{corners("8mm", "10mm", ".4mm")}
<div style="position:absolute;left:50%;top:22mm;transform:translateX(-50%);width:104mm;height:76mm;border-radius:50%;background:#fff;border:.35mm solid {M}"></div>
<img class="logo" src="logo_dark.png" style="top:31mm;width:80mm">
<div class="subj" style="top:110mm"><div class="lbl">SUBJECT · المادة</div><div class="e" style="margin-top:1.5mm">{I["subject_en"]}</div><div class="a">{I["subject_ar"]}</div></div>
{diamond("151mm", "2.6mm")}
<div style="position:absolute;left:0;right:0;top:157mm;text-align:center">
 <div style="font-family:Amiri;font-size:20pt;direction:rtl">{I["title_ar"]}</div>
 <div style="font-weight:700;font-size:13pt;margin-top:.5mm">{I["title_en"]}</div></div>
{diamond("188mm", "2.6mm")}
<table style="position:absolute;left:30mm;right:30mm;top:198mm;width:calc(100% - 60mm);border-collapse:collapse;background:#fff;border:.35mm solid {M}">
 {"".join(f'<tr><td style="padding:2.6mm 5mm;font-size:8.5pt;font-weight:700;opacity:.75;border-top:.35mm solid {M}">{a}</td><td style="padding:2.6mm 5mm;text-align:right;font-weight:800;font-size:12.5pt;direction:rtl;border-top:.35mm solid {M}">{v}</td></tr>' for a, v in [("Type · النوع", f'{I["kind_ar"]} · {I["kind_en"]}'), (f'{I["unit_en"]} · {I["unit_ar"]}', I["no"]), ("Stage · المرحلة", I["stage_ar"]), ("Instructor · التدريسي", I["instructor"])])}
</table>
<div class="foot">BIOS · Telegram @BIOS0t</div></section>"""

# D — dark header inside the frame with number and type, very clean body
Dv = f"""<section class="page v"><span class="tag">1D</span><div class="fr"></div>
<div style="position:absolute;left:11mm;right:11mm;top:11mm;height:15mm;background:{D};color:{L};display:flex;justify-content:space-between;align-items:center;padding:0 9mm;font-weight:800;font-size:11pt">
 <span>{I["unit_en"].upper()} {I["no"]}</span><span style="color:{M};font-family:Playfair;font-style:italic;font-size:14pt">BIOS</span><span style="direction:rtl">{I["unit_ar"]} {I["no"]}</span></div>
<img class="logo" src="logo_dark.png" style="top:40mm;width:86mm">
{diamond("112mm")}
<div class="subj" style="top:120mm"><div class="e">{I["subject_en"]}</div><div class="a">{I["subject_ar"]}</div></div>
<div style="position:absolute;left:34mm;right:34mm;top:158mm;text-align:center;border-top:.35mm solid {M};border-bottom:.35mm solid {M};padding:5mm 0">
 <div style="font-family:Amiri;font-size:19pt;direction:rtl">{I["title_ar"]}</div>
 <div style="font-weight:700;font-size:12.5pt;margin-top:.5mm">{I["title_en"]}</div></div>
<div class="row" style="left:20mm;right:20mm;top:200mm">
 <div><small>النوع · Type</small><b>{I["kind_ar"]} · {I["kind_en"]}</b></div><div><small>المرحلة · Stage</small><b>{I["stage_ar"]}</b></div></div>
<div class="ins" style="top:226mm"><div class="lbl">INSTRUCTOR · التدريسي</div><b>{I["instructor"]}</b></div>
<div style="position:absolute;left:11mm;right:11mm;bottom:11mm;height:11mm;background:{D};color:{L};display:flex;justify-content:center;align-items:center;font-size:8.5pt;font-weight:700;letter-spacing:.06em">Telegram @BIOS0t</div>
</section>"""

# E — serif elegance: Playfair English subject, generous spacing, soft white inner panel
E = f"""<section class="page v"><span class="tag">1E</span>
<div style="position:absolute;inset:11mm;background:#fff;border:.35mm solid {M};border-radius:2mm"></div>{corners("14.5mm", "8mm", ".35mm")}
<img class="logo" src="logo_dark.png" style="top:27mm;width:84mm">
<div style="position:absolute;left:0;right:0;top:100mm;text-align:center;font-size:9pt;font-weight:800;letter-spacing:.35em;color:{D};opacity:.75">{I["unit_en"].upper()} {I["no"]} · {I["kind_en"].upper()}</div>
<div class="subj" style="top:110mm"><div style="font-family:PlayfairR;font-size:28pt">{I["subject_en"]}</div><div class="a">{I["subject_ar"]}</div></div>
{diamond("150mm", "2.4mm")}
<div style="position:absolute;left:0;right:0;top:157mm;text-align:center">
 <div style="font-family:Amiri;font-size:20pt;direction:rtl">{I["title_ar"]}</div>
 <div style="font-family:PlayfairR;font-size:13pt;margin-top:1mm">{I["title_en"]}</div></div>
<div class="row" style="left:20mm;right:20mm;top:194mm">{row3()}</div>
<div class="ins" style="top:224mm"><div style="display:inline-block;background:{L};border:.35mm solid {M};border-radius:3mm;padding:4mm 14mm">
 <div class="lbl">INSTRUCTOR · التدريسي</div><b>{I["instructor"]}</b></div></div>
<div class="foot">BIOS · Telegram @BIOS0t</div></section>"""

open("covers2.html", "w").write(f"<!doctype html><meta charset=utf-8><style>{BASE}{m1.C1}{CSS}</style>{m1.P1.replace('class=\"tag\">1<', 'class=\"tag\">1 (السابق)<')}{A}{B}{C}{Dv}{E}")
print("ok")
