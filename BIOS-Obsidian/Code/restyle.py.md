---
source: BIOS-Obsidian/tools/scripts/restyle.py
handouts: []
saved: 2026-10-29
tags: [bios, code]
---
# restyle.py

Utility script.

```python
p = '/home/user/-/bios-engine/style.css'
s = open(p).read()


def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b)


rep("three colours: Black Bean #2e272a · Star White #d7cfbb · Egret #efefe8",
    "knight palette: navy #2c3846 · gold #b08547 / light gold #e2cfa3 · crimson #8e2219 · parchment #f3ead6 · ink #1e1b1c")
rep(""":root{--dark:#2e272a;--star:#d7cfbb;--egret:#efefe8;
--ink:var(--dark);--muted:rgba(46,39,42,.62);--bd:var(--star)}""",
    """:root{--dark:#2c3846;--gold:#b08547;--star:#e2cfa3;--egret:#f3ead6;--red:#8e2219;--paper:#fffcf5;
--ink:#1e1b1c;--muted:rgba(30,27,28,.6);--bd:var(--star)}""")
rep(".page{width:210mm;height:297mm;position:relative;overflow:hidden;background:#fff;",
    ".page{width:210mm;height:297mm;position:relative;overflow:hidden;background:var(--paper);")
rep('.mr::before,.mr::after{content:"";position:absolute;left:-.15mm;width:.3mm;background:var(--star)}',
    '.mr::before,.mr::after{content:"";position:absolute;left:-.15mm;width:.3mm;background:var(--gold)}')
rep(".mr i{position:absolute;left:-1.2mm;width:2.4mm;height:.3mm;background:var(--dark)}",
    ".mr i{position:absolute;left:-1.2mm;width:2.4mm;height:.3mm;background:var(--red)}")
rep(".hl{position:absolute;top:5.2mm;height:0;border-top:.45mm solid var(--star)}",
    ".hl{position:absolute;top:5.2mm;height:0;border-top:.45mm solid var(--gold)}")
rep("border-left:.4mm solid var(--star)}", "border-left:.4mm solid var(--gold)}")
rep("border-top:1.1mm solid var(--star)}", "border-top:1.1mm solid var(--gold)}")
rep(".ftr .fx b{font-weight:800;color:#fff}", ".ftr .fx b{font-weight:800;color:var(--star)}")
rep("border-radius:2mm 2mm 0 0;border:.6mm solid var(--star);border-bottom:0}",
    "border-radius:2mm 2mm 0 0;border:.6mm solid var(--gold);border-bottom:0;background:var(--red)}")
rep('.hp.lab::before{content:"";position:absolute;left:0;top:0;bottom:0;width:4mm;border-radius:6mm 0 0 6mm;background:var(--dark)}',
    '.hp.lab::before{content:"";position:absolute;left:0;top:0;bottom:0;width:4mm;border-radius:6mm 0 0 6mm;background:var(--red)}')
rep(".lt-box{width:17mm;height:100%;background:var(--dark)",
    ".lt-box{width:17mm;height:100%;background:var(--dark);border-right:1mm solid var(--gold)")
rep("border:.5mm solid var(--dark);color:var(--dark);font-weight:800;font-size:9pt;display:flex;align-items:center;justify-content:center;background:var(--star)}",
    "border:.5mm solid var(--gold);color:var(--egret);font-weight:800;font-size:9pt;display:flex;align-items:center;justify-content:center;background:var(--red)}")
rep(".sb{flex:1;height:9mm;border-radius:4.5mm;background:var(--dark);",
    ".sb{flex:1;height:9mm;border-radius:4.5mm;background:var(--dark);box-shadow:inset 0 -.6mm 0 var(--gold);")
rep(".en{font-size:11.6pt;line-height:1.5;color:var(--dark)}", ".en{font-size:11.6pt;line-height:1.5;color:var(--ink)}")
rep(".ar{font-family:AmiriQ,serif;font-size:14pt;line-height:1.72;color:var(--dark);text-align:right}",
    ".ar{font-family:AmiriQ,serif;font-size:13pt;line-height:1.72;color:var(--ink);text-align:right}")
rep("b.t{color:var(--dark);font-weight:800;background:linear-gradient(transparent 45%,var(--star) 45%,var(--star) 95%,transparent 95%);padding:0 .3mm}",
    "b.t{color:var(--red);font-weight:800}")
rep(".cut{display:inline-block;font-family:Mada;font-size:7.4pt;font-weight:800;color:var(--dark);background:var(--star);border:.3mm dashed var(--dark);",
    ".cut{display:inline-block;font-family:Mada;font-size:7.4pt;font-weight:800;color:var(--red);background:var(--egret);border:.3mm dashed var(--red);")
rep(".mark{color:var(--dark);font-weight:800}", ".mark{color:var(--red);font-weight:800}")
rep(".rule .rn{flex:none;width:9mm;height:9mm;border-radius:50%;background:var(--dark);",
    ".rule .rn{flex:none;width:9mm;height:9mm;border-radius:50%;background:var(--red);")
rep("figcaption b{color:var(--dark);font-weight:800}", "figcaption b{color:var(--red);font-weight:800}")
rep(".h2{display:flex;justify-content:space-between;font-weight:800;font-size:10.5pt;color:var(--dark);border-bottom:.35mm solid var(--dark);",
    ".h2{display:flex;justify-content:space-between;font-weight:800;font-size:10.5pt;color:var(--dark);border-bottom:.35mm solid var(--gold);")
rep(".note{background:var(--egret);border-left:3.4mm solid var(--dark);", ".note{background:var(--egret);border-left:3.4mm solid var(--red);")
rep(".note .en{font-size:10.5pt}.note .ar{font-size:13.5pt;line-height:1.7}", ".note .en{font-size:10.5pt}.note .ar{font-size:12.5pt;line-height:1.7}")
rep(".np{display:inline-block;background:var(--dark);", ".np{display:inline-block;background:var(--red);")
rep(".sum{background:var(--egret);border-left:3.4mm solid var(--star);", ".sum{background:var(--egret);border-left:3.4mm solid var(--gold);")
rep("table.tb th{background:var(--dark);color:var(--egret);", "table.tb th{background:var(--dark);color:var(--egret);border-bottom:.6mm solid var(--gold);")
# cover
rep(".cv-c1{position:absolute;left:140mm;top:-30mm;width:115mm;height:115mm;border-radius:50%;background:var(--star);opacity:.55}",
    ".cv-c1{position:absolute;left:140mm;top:-30mm;width:115mm;height:115mm;border-radius:50%;background:var(--dark)}")
rep(".cv-c2{position:absolute;left:130mm;top:-42mm;width:135mm;height:135mm;border-radius:50%;border:.3mm solid var(--star)}",
    ".cv-c2{position:absolute;left:130mm;top:-42mm;width:135mm;height:135mm;border-radius:50%;border:.6mm solid var(--gold)}")
rep(".cv-b1{position:absolute;left:-20mm;top:216mm;width:105mm;height:100mm;border-radius:0 52mm 0 0;background:var(--star);opacity:.55}",
    ".cv-b1{position:absolute;left:-20mm;top:216mm;width:105mm;height:100mm;border-radius:0 52mm 0 0;background:var(--red)}")
rep(".cv-b2{position:absolute;left:-30mm;top:228mm;width:105mm;height:100mm;border-radius:0 40mm 0 0;border:.3mm solid var(--star);",
    ".cv-b2{position:absolute;left:-30mm;top:228mm;width:105mm;height:100mm;border-radius:0 40mm 0 0;border:.6mm solid var(--gold);")
rep(".cv-r{position:absolute;left:22mm;right:22mm;border-top:.35mm solid var(--star)}",
    ".cv-r{position:absolute;left:22mm;right:22mm;border-top:.35mm solid var(--gold)}")
rep(".cv-pill{position:absolute;left:40mm;right:40mm;top:164mm;height:8.6mm;border-radius:4.3mm;background:var(--dark);",
    ".cv-pill{position:absolute;left:40mm;right:40mm;top:164mm;height:8.6mm;border-radius:4.3mm;background:var(--dark);box-shadow:0 0 0 .6mm var(--gold);")
rep(".cv-ins{position:absolute;left:26mm;right:26mm;top:223mm;height:17mm;border:.4mm solid var(--dark);",
    ".cv-ins{position:absolute;left:26mm;right:26mm;top:223mm;height:17mm;border:.5mm solid var(--gold);")
rep(".cv-ins .v{font-weight:900;font-size:19pt;color:var(--dark);border-top:.3mm solid var(--star);border-bottom:.3mm solid var(--star);",
    ".cv-ins .v{font-weight:900;font-size:19pt;color:var(--red);border-top:.3mm solid var(--gold);border-bottom:.3mm solid var(--gold);")
rep(".cv-st{position:absolute;left:50%;transform:translateX(-50%);background:var(--egret);color:var(--dark);",
    ".cv-st{position:absolute;left:50%;transform:translateX(-50%);background:var(--egret);color:var(--gold);")
rep(".cv-band{position:absolute;left:0;right:0;top:272mm;height:2.2mm;background:var(--star)}",
    ".cv-band{position:absolute;left:0;right:0;top:272mm;height:2.2mm;background:var(--gold)}")
rep(".cv-foot .l b{font-family:Playfair;font-style:italic;font-weight:900;font-size:20pt;color:#fff}",
    ".cv-foot .l b{font-family:Playfair;font-style:italic;font-weight:900;font-size:20pt;color:var(--star)}")
rep(".cv-foot .r b{font-weight:800;color:#fff}", ".cv-foot .r b{font-weight:800;color:var(--star)}")
rep(".sym .l1{font-weight:800;font-size:9.5pt;color:var(--dark);", ".sym .l1{font-weight:800;font-size:9.5pt;color:var(--red);")
rep(".qnum{position:absolute;right:4mm;top:3.1mm;font-size:6.4pt;font-weight:800;background:var(--dark);",
    ".qnum{position:absolute;right:4mm;top:3.1mm;font-size:6.4pt;font-weight:800;background:var(--red);")
rep(".akey div span{color:var(--dark);font-weight:800}", ".akey div span{color:var(--red);font-weight:800}")
# old ol.nl rules -> paired list
i = s.index("ol.nl{list-style:none")
j = s.index("/* rule cards */")
s = s[:i] + """.nb{flex:none;width:4.8mm;height:4.8mm;border-radius:50%;background:var(--red);color:var(--egret);font-family:Mada;font-size:6.6pt;font-weight:800;display:flex;align-items:center;justify-content:center}
/* numbered points inside a card: each point followed by its translation */
.c-list{padding:1.6mm 5mm 1.2mm 5mm;border-top:.3mm dashed var(--star)}
ol.pl{list-style:none}
ol.pl li{display:grid;grid-template-columns:4.8mm 1fr;gap:2.6mm;align-items:start;padding:1.1mm 0;border-bottom:.25mm dotted var(--star)}
ol.pl li:last-child{border-bottom:0}
ol.pl .nb{margin-top:1.1mm}
.pr.inline{display:flex;justify-content:space-between;align-items:baseline;gap:4mm}
.pr.stack .ar{margin-top:.2mm}
.pr .en{font-size:11pt;line-height:1.45}
.pr .ar{font-size:12.5pt;line-height:1.6}
""" + s[j:]
# MCQ options
rep(".op{display:grid;grid-template-columns:6mm 1fr 1fr;gap:3mm;align-items:center;",
    ".op{display:grid;grid-template-columns:6mm 1fr;gap:2.4mm;align-items:center;")
rep(".op .en{font-size:10.4pt;line-height:1.3}", ".op .en{font-size:10.4pt;line-height:1.3}.op .pr{padding:.6mm 0}.op .pr.stack .ar{text-align:right}")
rep(".op .ar{font-size:12.5pt;line-height:1.4}", ".op .ar{font-size:11.5pt;line-height:1.4}")
open(p, 'w').write(s)
print("ok")

```
