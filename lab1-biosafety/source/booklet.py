from lib import *
from art import emblem, grid

SUBJ_EN = "Diagnostic Microbiology"
SUBJ_AR = "الأحياء المجهرية التشخيصية"
TITLE_EN = "Rules and biosafety levels"
TITLE_AR = "القواعد ومستويات السلامة الحيوية"

COVER_CSS = r"""
.cover{background:var(--van)}
.cv-top{position:absolute;left:0;right:0;top:0;height:158mm;background:var(--van)}
.cv-bot{position:absolute;left:0;right:0;top:158mm;bottom:0;background:var(--moon)}
.grid{position:absolute;inset:0;display:grid}
.gcell{border-right:.3mm solid;border-bottom:.3mm solid;position:relative}
.gcell span{position:absolute;left:2mm;top:1.5mm;font-size:7pt;font-weight:500}
.cv-logo{position:absolute;left:14mm;top:13mm;width:62mm}
.cv-chip{position:absolute;right:14mm;top:19mm;display:flex;align-items:center;gap:2.5mm;font-weight:700;font-size:11pt;color:var(--moon-d)}
.cv-chip .tri{width:0;height:0;border-left:9mm solid var(--moon);border-top:5.5mm solid transparent;border-bottom:5.5mm solid transparent}
.cv-ar{position:absolute;right:16mm;top:56mm;text-align:right;font-weight:900;font-size:44pt;line-height:1.12;color:var(--moon)}
.cv-en{position:absolute;left:16mm;top:118mm;font-weight:700;font-size:21pt;color:var(--moon-dd);line-height:1.15}
.cv-en small{display:block;font-size:11pt;font-weight:600;color:var(--moon-d);letter-spacing:.18em;text-transform:uppercase;margin-bottom:1.5mm}
.cv-badge{position:absolute;left:16mm;top:100mm;display:flex;gap:2mm}
.cv-badge span{font-weight:800;font-size:10.5pt;padding:1.2mm 3.5mm;border-radius:10mm;background:var(--moon);color:var(--cream)}
.cv-badge span.w{background:var(--wis);color:#fff}
.cv-art{position:absolute;right:10mm;top:118mm;width:96mm;height:96mm}
.cv-info{position:absolute;left:16mm;top:172mm;width:92mm;color:var(--van)}
.cv-subj{font-weight:900;font-size:24pt;line-height:1.1;color:var(--van)}
.cv-subj-ar{font-family:AmiriQ,serif;font-size:25pt;line-height:1.75;color:var(--cream);direction:rtl;text-align:left}
.cv-rows{margin-top:5mm;border-top:.4mm solid rgba(255,235,175,.5)}
.cv-row{display:flex;justify-content:space-between;align-items:baseline;padding:2.2mm 0;border-bottom:.4mm solid rgba(255,235,175,.35);font-size:12pt}
.cv-row .k{font-weight:500;color:var(--cream);opacity:.85;font-size:10pt;letter-spacing:.08em;text-transform:uppercase}
.cv-row .v{font-weight:800;color:var(--van)}
.cv-row .va{font-weight:800;color:var(--van);direction:rtl}
.cv-foot{position:absolute;left:16mm;right:16mm;bottom:12mm;display:flex;justify-content:space-between;align-items:center;color:var(--cream);font-weight:700;font-size:10.5pt}
.cv-foot .sw{display:flex;gap:1.6mm}
.cv-foot .sw i{width:6mm;height:6mm;border-radius:50%;display:block;border:.5mm solid rgba(255,255,255,.7)}
.cv-bigar{position:absolute;right:16mm;bottom:22mm;font-weight:900;font-size:30pt;color:var(--van);text-align:right;line-height:1.15}
/* contents page */
.card{border-radius:5mm;overflow:hidden;border:.4mm solid var(--line);margin-bottom:6mm}
.card-h{background:var(--moon);color:var(--cream);font-weight:800;font-size:13pt;padding:2.4mm 5mm;display:flex;justify-content:space-between}
.card-r{display:grid;grid-template-columns:30mm 1fr 1fr;gap:3mm;padding:1.6mm 5mm;border-top:.35mm solid var(--line);align-items:baseline;font-size:13pt}
.card-r:nth-child(odd){background:#FFFCEF}
.card-r .k{font-weight:700;color:var(--moon-d);font-size:11pt}
.card-r .v{font-weight:600}
.card-r .va{font-weight:700;text-align:right;color:var(--ink-ar)}
.toc{list-style:none}
.toc li{display:flex;align-items:center;gap:3mm;padding:1.2mm 0;border-bottom:.35mm dashed var(--line)}
.toc .n{width:8mm;height:8mm;border-radius:50%;background:var(--van);color:var(--moon-dd);font-weight:900;display:flex;align-items:center;justify-content:center;font-size:11pt;flex:none}
.toc .te{font-weight:700;font-size:12pt;color:var(--moon-dd)}
.toc .ta{flex:1;text-align:right;font-weight:700;font-size:12pt;color:var(--ink-ar)}
.toc .p{width:10mm;text-align:center;font-weight:900;color:var(--cream);background:var(--moon);border-radius:3mm;font-size:11pt;flex:none}
"""

def cover():
    return f'''<section class="page cover">
<div class="cv-top">{grid()}</div>
<div class="cv-bot">{grid(color="rgba(255,235,175,.16)", rows=3, letters="DEF", label_color="rgba(255,235,175,.45)")}</div>
<img class="cv-logo" src="assets/logo.png">
<div class="cv-chip"><span>Lab 1</span><span class="tri"></span></div>
<div class="cv-ar" dir="rtl">القواعد<br>ومستويات<br>السلامة الحيوية</div>
<div class="cv-badge"><span>Practical · عملي</span><span class="w">Lab 1 · المختبر ١</span></div>
<div class="cv-en"><small>Laboratories</small>{TITLE_EN}</div>
<div class="cv-art">{emblem()}</div>
<div class="cv-info">
  <div class="cv-subj">{SUBJ_EN}</div>
  <div class="cv-subj-ar" dir="rtl">{SUBJ_AR}</div>
  <div class="cv-rows">
    <div class="cv-row"><span class="k">Stage</span><span class="v">The fourth stage</span><span class="va">المرحلة الرابعة</span></div>
    <div class="cv-row"><span class="k">Lab</span><span class="v">Lab: 1</span><span class="va">المختبر: ١</span></div>
    <div class="cv-row"><span class="k">Type</span><span class="v">Practical</span><span class="va">عملي</span></div>
  </div>
</div>
<div class="cv-foot"><span>Bilingual Booklet · English + العربية</span>
<span class="sw"><i style="background:#FFEBAF"></i><i style="background:#4C9DB0"></i><i style="background:#C69FD5"></i><i style="background:#FCFDC8"></i></span></div>
</section>'''

HDR = (f'<div class="hdr"><span class="h-en" dir="ltr">{SUBJ_EN}</span>'
       f'<span class="chip">Lab <b>1</b> · Practical · عملي</span>'
       f'<span class="h-ar" dir="rtl">{SUBJ_AR}</span></div>')
FL = "The fourth stage · " + TITLE_EN
FR = "المرحلة الرابعة · " + TITLE_AR

# ---------------------------------------------------------------- content pages
P = []   # list of (toc entry or None, html)

# 1 — Biosafety levels
P.append((("1", "Biosafety levels", "مستويات السلامة الحيوية"),
  sec("1", "Biosafety levels", "مستويات السلامة الحيوية", "🛡️")
  + '<div style="display:flex;gap:6mm;align-items:flex-start"><div style="flex:1">'
  + ul([
      ("**Biosafety levels**: They are principles and application used to protect laboratory workers and the surrounding environment from exposure to danger while working with living organisms.",
       "**مستويات السلامة الحيوية**: هي مبادئ وتطبيقات تُستخدم لحماية العاملين في المختبر والبيئة المحيطة من التعرّض للخطر أثناء العمل مع الكائنات الحية."),
      ("**It aims to**: provide the highest level of protection and the lowest range of exposure.",
       "**تهدف إلى**: توفير أعلى مستوى من الحماية وأدنى مدى من التعرّض."),
    ])
  + '</div>' + fig("assets/labsafety.jpg", "Lab Safety", "سلامة المختبر", w="34mm") + '</div>'
  + box("memory", pair("Highest protection ⬆  +  Lowest exposure ⬇ = the goal of every biosafety level.",
                       "أعلى حماية ⬆ + أقل تعرّض ⬇ = هدف كل مستوى من مستويات السلامة الحيوية."))
))

# 2 — Risk groups (table split over two pages)
def rg_row(lvl_en, lvl_ar, title_en, title_ar, cls, d_en, d_ar, n):
    return (f'<tr><td class="lvl" style="font-size:10.5pt;padding:2.4mm 1.5mm"><div dir="ltr">{lvl_en}</div><div dir="rtl" style="font-weight:700;color:var(--ink-ar)">{lvl_ar}</div></td>'
            f'<td><div class="rg-title {cls}" dir="ltr" style="font-size:13.5pt">{md(title_en)}</div>'
            f'<div class="rg-title {cls}" dir="rtl" style="font-size:13.5pt">{md(title_ar)}</div>'
            f'{en(d_en)}{ar(d_ar)}</td><td class="cnum">{n}</td></tr>')

RG_HEAD = ('<table class="t rg"><thead><tr><th style="width:29mm;font-size:9.5pt">The level of biological safety for each group<br>'
           '<span style="color:var(--cream);font-weight:700">مستوى السلامة الحيوية لكل مجموعة</span></th>'
           '<th>Risk groups<br><span style="color:var(--cream);font-weight:700">مجموعات الخطورة</span></th><th style="width:12mm">#</th></tr></thead><tbody>')

R1 = rg_row("Biosafety level 1", "مستوى السلامة الحيوية ١", "(**Minimal** risk) Risk group 1", "(خطورة **ضئيلة**) مجموعة الخطورة 1", "risk1",
   "**Non-pathogenic** factors in healthy people and adults (with little or no risk). *E.coli* , *Bacillus Subtilis*",
   "عوامل **غير مُمرِضة** للأشخاص الأصحّاء والبالغين (ذات خطورة قليلة أو معدومة). `*E.coli*` (الإشريكية القولونية)، `*Bacillus Subtilis*` (العصوية الرقيقة).", 1)
R2 = rg_row("Biosafety level 2", "مستوى السلامة الحيوية ٢", "(**Moderate** risk) Risk group 2", "(خطورة **متوسطة**) مجموعة الخطورة 2", "risk2",
   "Factors related to **human infection** and **treatment is possible** in this case (moderate risk and !!limited!! risk of spread). *E.coli* pathogenic strain , *Brucella spp.* , *Salmonella spp.*",
   "عوامل مرتبطة **بإصابة الإنسان بالعدوى**، و**يكون العلاج ممكنًا** في هذه الحالة (خطورة متوسطة وخطر انتشار !!محدود!!). السلالة المُمرِضة من `*E.coli*`، أنواع البروسيلا `*Brucella spp.*`، أنواع السالمونيلا `*Salmonella spp.*`.", 2)
R3 = rg_row("Biosafety level 3", "مستوى السلامة الحيوية ٣", "(**High** risk) Risk group 3", "(خطورة **عالية**) مجموعة الخطورة 3", "risk3",
   "Factors that cause serious and fatal infections to humans and their **treatment is not easy**, specially for immunosuppressed persons (with a high risk for individuals). *Salmonella typhi*. *Mycobacterium tuberculosis*.",
   "عوامل تسبّب عدوى خطيرة ومميتة للإنسان و**علاجها ليس سهلًا**، خصوصًا للأشخاص المثبَّطة مناعتهم (مع خطورة عالية على الأفراد). السالمونيلا التيفية `*Salmonella typhi*`. المتفطّرة السلّية `*Mycobacterium tuberculosis*`.", 3)
R4 = rg_row("Biosafety level 4", "مستوى السلامة الحيوية ٤", "(**Extreme** risk) Risk group 4", "(خطورة **قصوى**) مجموعة الخطورة 4", "risk4",
   "Factor that are fatal to humans are easily transmitted from …",
   "عوامل مميتة للإنسان وتنتقل بسهولة من …", 4)

P.append((("2", "Risk groups", "مجموعات الخطورة"),
  sec("2", "Risk groups", "مجموعات الخطورة", "📊")
  + pair("**Risk groups:** are used to assess risk, determine its source and how to deal with it , includes 4 groups:",
         "**مجموعات الخطورة:** تُستخدم لتقييم الخطر، وتحديد مصدره وكيفية التعامل معه، وتشمل 4 مجموعات:")
  + RG_HEAD + R1 + R2 + "</tbody></table>"
))
P.append((None,
  RG_HEAD + R3 + R4 + "</tbody></table>"
  + box("note",
        pair("Risk group 4 text is cut off in the original slide. WHO reference: these agents usually cause serious disease, spread readily between individuals, and lack effective treatment or prevention.",
             "نص المجموعة 4 مقطوع في الشريحة الأصلية. مرجع منظمة الصحة العالمية: تسبّب هذه العوامل عادةً مرضًا خطيرًا، وتنتشر بسهولة بين الأفراد، ولا يتوفر لها علاج أو وقاية فعّالة عادةً."))
))

# 3 — Biohazard symbol
P.append((("3", "Biohazard symbol", "رمز الخطر الحيوي"),
  sec("3", "Biohazard symbol", "رمز الخطر الحيوي", "☣️")
  + ul([
      ("**Biohazard symbol**: it used to warn people of the potential for the presence dangerous biological materials such as :",
       "**رمز الخطر الحيوي**: يُستخدم لتحذير الأشخاص من احتمال وجود مواد بيولوجية خطرة، مثل:"),
      ("Cultures of pathogens.", "مزارع المُمرِضات (العوامل المسبّبة للأمراض)."),
      ("Human Blood and Tissue.", "دم الإنسان وأنسجته."),
      ("Corridors leading to the laboratories.", "الممرات المؤدية إلى المختبرات."),
    ])
  + figrow(fig("assets/biohazard.jpg", "BIOHAZARD", "الخطر الحيوي", w="42mm"),
           fig("assets/radiation.jpg", "RADIATION HAZARD", "خطر الإشعاع", w="56mm"))
))

# 4 — Laboratory safety considerations
SAFE = [
  ("Wear protective clothing (clean lab. Coat – **Gloves** - **mask** – safety **glasses**).",
   "ارتدِ الملابس الواقية (معطف مختبر نظيف – **قفازات** – **كمامة** – **نظارات** واقية)."),
  ("Avoid touching objects (pencils , cell phones , door handles, e.g.) while wearing gloves. And pencils, labels , or any other materials should never be placed in your mouth.",
   "تجنّب لمس الأشياء (الأقلام، الهواتف المحمولة، مقابض الأبواب، مثلًا) أثناء ارتداء القفازات. ويجب ألّا توضع الأقلام أو الملصقات أو أي مواد أخرى في فمك أبدًا."),
  ("Do not eat food or drink water in the lab. Do not use lab glassware as food or water containers.",
   "لا تأكل الطعام ولا تشرب الماء في المختبر. لا تستخدم الأدوات الزجاجية المختبرية أوعيةً للطعام أو الماء."),
  ("Long hair must be tied back or covered to minimize fire hazard or contamination of experiment.",
   "يجب ربط الشعر الطويل إلى الخلف أو تغطيته لتقليل خطر الحريق أو تلوّث التجربة."),
  ("Do not take any cultures out of the lab for any reason, all cultures should be handled as **potentially pathogenic**.",
   "لا تُخرج أي مزارع من المختبر لأي سبب كان، ويجب التعامل مع جميع المزارع على أنها **يُحتمل أن تكون مُمرِضة**."),
  ("Wash hands after working with infectious materials.", "اغسل يديك بعد العمل مع المواد المُعدية."),
  ("Disinfect all instruments **immediately after use**.", "طهّر جميع الأدوات **فور استخدامها**."),
  ("Disinfect all contaminated waste **before discarding**.", "طهّر جميع النفايات الملوّثة **قبل التخلّص منها**."),
]
P.append((("4", "Laboratory safety considerations", "اعتبارات السلامة في المختبر"),
  sec("4", "Laboratory safety considerations:", "اعتبارات السلامة في المختبر:", "🥽")
  + ol(SAFE[0:1], 1)
  + fig("assets/ppe.jpg", "Protective clothing: mask – safety glasses – gloves", "الملابس الواقية: كمامة – نظارات واقية – قفازات", w="118mm")
  + ol(SAFE[1:2], 2)
))
P.append((None,
  h2("Laboratory safety considerations (continued)", "اعتبارات السلامة (تتمة)")
  + ol(SAFE[2:3], 3)
  + fig("assets/nofood.jpg", "No food or drink in the lab", "ممنوع الأكل والشرب في المختبر", w="62mm")
  + ol(SAFE[3:4], 4)
))
P.append((None,
  h2("Laboratory safety considerations (continued)", "اعتبارات السلامة (تتمة)")
  + ol(SAFE[4:5], 5)
  + fig("assets/cultures.jpg", "Bacterial cultures on agar plates", "مزارع بكتيرية على أطباق الآجار", w="88mm")
  + ol(SAFE[5:6], 6)
  + fig("assets/handwash.jpg", "Hand washing", "غسل اليدين", w="68mm")
))
P.append((None,
  h2("Laboratory safety considerations (continued)", "اعتبارات السلامة (تتمة)")
  + ol(SAFE[6:8], 7)
  + fig("assets/disinfect.jpg", "Disinfection of instruments and work areas", "تطهير الأدوات ومناطق العمل", w="98mm")
  + box("key", ul([("8 rules: protect yourself (1, 4) · keep everything away from your mouth and food (2, 3) · keep cultures inside (5) · clean hands, instruments and waste (6, 7, 8).",
                    "٨ قواعد: احمِ نفسك (1، 4) · أبعِد كل شيء عن فمك وطعامك (2، 3) · أبقِ المزارع داخل المختبر (5) · نظّف اليدين والأدوات والنفايات (6، 7، 8).")]))
))

# 5 — Sterilization / Disinfection / Antiseptics / Decontamination
DEFS = [
  ("**Sterilization:** is the complete killing or removal of all living organism such as cell spore , viruses , fungi, ….",
   "**التعقيم:** هو القتل أو الإزالة الكاملة لجميع الكائنات الحية، مثل الخلايا والأبواغ والفيروسات والفطريات، …."),
  ("**Disinfection:** the destruction or removal of pathogens !!but not bacterial spores!! , usually used only on inanimate object.",
   "**التطهير:** تدمير المُمرِضات أو إزالتها !!ولكن ليس الأبواغ البكتيرية!!، ويُستخدم عادةً على الأجسام غير الحيّة فقط."),
  ("**Antiseptics:** chemicals applied to !!body surfaces!! to destroy or inhibit pathogens.",
   "**المطهِّرات الموضعية** `(Antiseptics)`: مواد كيميائية تُطبَّق على !!أسطح الجسم!! لتدمير المُمرِضات أو تثبيطها."),
  ("**Decontamination:** the mechanical removal of most microbes by using washing , heat or disinfectants.",
   "**إزالة التلوّث:** الإزالة الميكانيكية لمعظم الميكروبات باستخدام الغسل أو الحرارة أو المطهِّرات."),
]
P.append((("5", "Sterilization & related terms", "التعقيم والمصطلحات المرتبطة"),
  sec("5", "Sterilization & related terms", "التعقيم والمصطلحات المرتبطة", "🧪")
  + ul(DEFS)

))

CMP = ('<table class="t"><thead><tr><th>Term · المصطلح</th><th>What it does · ماذا يفعل</th><th>Applied on · يُطبَّق على</th></tr></thead><tbody>'
  + "".join(f'<tr><td><b class="term">{a}</b><div dir="rtl" style="font-weight:700;color:var(--ink-ar)">{b}</div></td>'
            f'<td>{en(c)}{ar(d)}</td><td>{(en(e)+ar(f)) if e!="—" else '<p class="en" style="text-align:center">—</p>'}</td></tr>' for a, b, c, d, e, f in [
    ("Sterilization", "التعقيم", "Complete killing or removal of **all** living organisms", "قتل أو إزالة **جميع** الكائنات الحية كليًا", "—", "—"),
    ("Disinfection", "التطهير", "Destroys/removes pathogens, **not bacterial spores**", "يدمّر/يزيل المُمرِضات، **لا الأبواغ البكتيرية**", "Inanimate objects", "الأجسام غير الحيّة"),
    ("Antiseptics", "المطهّرات الموضعية", "Chemicals that destroy or inhibit pathogens", "مواد كيميائية تدمّر المُمرِضات أو تثبّطها", "Body surfaces", "أسطح الجسم"),
    ("Decontamination", "إزالة التلوّث", "Mechanical removal of **most** microbes (washing, heat, disinfectants)", "إزالة ميكانيكية **لمعظم** الميكروبات (غسل، حرارة، مطهّرات)", "—", "—"),
  ]) + "</tbody></table>")
P.append((None,
  h2("Compare at a glance", "مقارنة سريعة")
  + box("compare", CMP.replace('class="t"','class="t" style="font-size:12pt"'))
))

# 6 — Biological laboratory / Bio risk / assessment
P.append((("6", "Biological laboratory & Bio risk", "المختبر البيولوجي والخطر البيولوجي"),
  sec("6", "Biological laboratory & Bio risk", "المختبر البيولوجي والخطر البيولوجي", "🧫")
  + ul([
    ("**Biological laboratory** :A facility within which microorganisms, their components or their derivatives are collected handled and/or stored.",
     "**المختبر البيولوجي**: منشأة تُجمَع فيها الكائنات الحية الدقيقة أو مكوّناتها أو مشتقّاتها، ويُتعامَل معها و/أو تُخزَّن."),
    ("**Bio risk** :The probability or chance that a particular adverse event :accidental infection or loss, theft, misuse, diversion or intentional release), possibly leading to harm.",
     "**الخطر البيولوجي**: احتمال أو فرصة وقوع حدث ضار معيّن (عدوى عَرَضية، أو فقدان، أو سرقة، أو إساءة استخدام، أو تحويل، أو إطلاق متعمَّد)، قد يؤدي إلى الضرر."),
    ("**Bio risk assessment** : The process to identify acceptable and unacceptable risks (embracing **biosafety risks** (risks of accidental infection) and **laboratory biosecurity risks** (risks of unauthorized access, loss, theft, misuse, diversion or intentional release)) and their potential consequences.",
     "**تقييم الخطر البيولوجي**: عملية تحديد المخاطر المقبولة وغير المقبولة (وتشمل **مخاطر السلامة الحيوية** (مخاطر العدوى العَرَضية) و**مخاطر الأمن الحيوي المختبري** (مخاطر الوصول غير المصرَّح به، أو الفقدان، أو السرقة، أو إساءة الاستخدام، أو التحويل، أو الإطلاق المتعمَّد))، وعواقبها المحتملة."),
  ])
))

# 7 — Biosafety cabinet
LABELS = [("Class I biosafety cabinet", "كابينة السلامة الحيوية من الفئة الأولى"),
          ("Mini Biosafety cabinet", "كابينة سلامة حيوية مصغّرة"),
          ("Class III Biosafety Cabinet", "كابينة السلامة الحيوية من الفئة الثالثة"),
          ("Ducted and Ductless Fume Hood", "خزانة الأبخرة ذات القناة وعديمة القناة"),
          ("Laminar flow Cabinet", "كابينة التدفّق الصفائحي"),
          ("PCR Cabinet", "كابينة تفاعل البلمرة المتسلسل `(PCR)`"),
          ("Autoclave", "جهاز التعقيم بالبخار المضغوط (الأوتوكليف)"),
          ("Incubator", "الحاضنة")]
def _gl(rows): return '<table class="t g" style="margin:0"><tbody>' + "".join(
    f'<tr><td class="ge" dir="ltr" style="font-size:11.5pt">{e}</td><td class="ga" dir="rtl" style="font-size:11.5pt">{md(a)}</td></tr>' for e, a in rows) + "</tbody></table>"
GLAB = '<div style="display:flex;gap:4mm;margin-bottom:3mm"><div style="flex:1">' + _gl(LABELS[:4]) + '</div><div style="flex:1">' + _gl(LABELS[4:]) + '</div></div>'
P.append((("7", "Biosafety Cabinet", "كابينة السلامة الحيوية"),
  sec("7", "Biosafety Cabinet", "كابينة السلامة الحيوية", "🏭")
  + fig("assets/cabinets.jpg", "Biosafety cabinets and related equipment", "كابينات السلامة الحيوية والأجهزة المرتبطة بها", w="112mm")
  + h2("Labels in the image", "التسميات في الصورة") + GLAB
  + '<p class="muted" style="font-size:10pt;margin-top:-2mm" dir="ltr">BIOS Note: three labels in the top row of the original image are hidden by a watermark and could not be read reliably.</p>'
  + '<p class="muted" style="font-size:10pt" dir="rtl">ملاحظة: ثلاث تسميات في الصف العلوي من الصورة الأصلية مغطّاة بعلامة مائية ولم يمكن قراءتها بدقة.</p>'
))

# Key terms
TERMS = [("Biosafety levels", "مستويات السلامة الحيوية"), ("Risk groups", "مجموعات الخطورة"),
         ("Non-pathogenic", "غير مُمرِض"), ("Pathogenic strain", "سلالة مُمرِضة"),
         ("Immunosuppressed persons", "الأشخاص المثبَّطة مناعتهم"), ("Biohazard symbol", "رمز الخطر الحيوي"),
         ("Radiation hazard", "خطر الإشعاع"), ("Cultures of pathogens", "مزارع المُمرِضات"),
         ("Protective clothing", "الملابس الواقية"), ("Lab glassware", "الأدوات الزجاجية المختبرية"),
         ("Infectious materials", "المواد المُعدية"), ("Contaminated waste", "النفايات الملوّثة"),
         ("Sterilization", "التعقيم"), ("Disinfection", "التطهير"), ("Bacterial spores", "الأبواغ البكتيرية"),
         ("Inanimate object", "جسم غير حيّ"), ("Antiseptics", "المطهّرات الموضعية"),
         ("Decontamination", "إزالة التلوّث"), ("Biological laboratory", "المختبر البيولوجي"),
         ("Bio risk", "الخطر البيولوجي"), ("Bio risk assessment", "تقييم الخطر البيولوجي"),
         ("Biosafety risks", "مخاطر السلامة الحيوية"), ("Laboratory biosecurity risks", "مخاطر الأمن الحيوي المختبري"),
         ("Biosafety Cabinet", "كابينة السلامة الحيوية")]
half = (len(TERMS) + 1) // 2
def gt(rows):
    return '<table class="t g"><tbody>' + "".join(
        f'<tr><td class="ge" dir="ltr">{e}</td><td class="ga" dir="rtl">{a}</td></tr>' for e, a in rows) + "</tbody></table>"
P.append((("★", "Key Terms", "أهم المصطلحات"),
  sec("★", "KEY TERMS", "أهم المصطلحات", "📘")
  + '<div style="display:flex;gap:5mm"><div style="flex:1">' + gt(TERMS[:half]) + '</div><div style="flex:1">' + gt(TERMS[half:]) + "</div></div>"
))

# Lecture summary
SUMMARY = [
    ("Biosafety levels protect laboratory workers and the surrounding environment; they aim for the highest protection and the lowest exposure.",
     "تحمي مستويات السلامة الحيوية العاملين في المختبر والبيئة المحيطة، وتهدف إلى أعلى حماية وأدنى تعرّض."),
    ("There are 4 risk groups, each matched with a biosafety level: minimal (1), moderate (2), high (3) and extreme (4) risk.",
     "توجد 4 مجموعات خطورة، تقابل كلٌّ منها مستوى سلامة حيوية: خطورة ضئيلة (1)، متوسطة (2)، عالية (3)، وقصوى (4)."),
    ("Examples: RG1 – *E.coli*, *Bacillus Subtilis*; RG2 – *E.coli* pathogenic strain, *Brucella spp.*, *Salmonella spp.*; RG3 – *Salmonella typhi*, *Mycobacterium tuberculosis*.",
     "أمثلة: المجموعة 1 – `*E.coli*`، `*Bacillus Subtilis*`؛ المجموعة 2 – السلالة المُمرِضة من `*E.coli*`، `*Brucella spp.*`، `*Salmonella spp.*`؛ المجموعة 3 – `*Salmonella typhi*`، `*Mycobacterium tuberculosis*`."),
    ("The biohazard symbol warns of dangerous biological materials: cultures of pathogens, human blood and tissue, and corridors leading to the laboratories.",
     "يحذّر رمز الخطر الحيوي من المواد البيولوجية الخطرة: مزارع المُمرِضات، ودم الإنسان وأنسجته، والممرات المؤدية إلى المختبرات."),
    ("Eight laboratory safety rules: protective clothing, no touching objects with gloves or placing items in the mouth, no food or drink, tie long hair, keep cultures in the lab, wash hands, disinfect instruments and waste.",
     "ثماني قواعد للسلامة: الملابس الواقية، عدم لمس الأشياء بالقفازات أو وضع أي شيء في الفم، عدم الأكل والشرب، ربط الشعر الطويل، إبقاء المزارع داخل المختبر، غسل اليدين، تطهير الأدوات والنفايات."),
    ("Sterilization kills all living organisms; disinfection does not kill bacterial spores; antiseptics are for body surfaces; decontamination is a mechanical removal of most microbes.",
     "التعقيم يقتل جميع الكائنات الحية؛ التطهير لا يقتل الأبواغ البكتيرية؛ المطهّرات الموضعية لأسطح الجسم؛ إزالة التلوّث إزالة ميكانيكية لمعظم الميكروبات."),
    ("Bio risk assessment identifies acceptable and unacceptable risks — biosafety risks and laboratory biosecurity risks — and their potential consequences.",
     "يحدّد تقييم الخطر البيولوجي المخاطر المقبولة وغير المقبولة — مخاطر السلامة الحيوية ومخاطر الأمن الحيوي المختبري — وعواقبها المحتملة."),
]
P.append((("★", "Lecture Summary", "ملخص المحاضرة"),
  sec("★", "Lecture Summary", "ملخص المحاضرة", "📝")
  + ol(SUMMARY[:4])
))
P.append((None,
  h2("Lecture Summary (continued)", "ملخص المحاضرة (تتمة)")
  + ol(SUMMARY[4:], 5)
))
P.append((("★", "Quick Review", "مراجعة سريعة"),
  sec("★", "QUICK REVIEW", "مراجعة سريعة", "🔁")
  + box("memory", ul([
      ("Risk group number = Biosafety level number (RG 1 → BSL 1 … RG 4 → BSL 4); risk rises: Minimal → Moderate → High → Extreme.",
       "رقم مجموعة الخطورة = رقم مستوى السلامة الحيوية (المجموعة 1 ← المستوى 1 … المجموعة 4 ← المستوى 4)؛ وتتصاعد الخطورة: ضئيلة ← متوسطة ← عالية ← قصوى."),
      ("**Anti**septics → on the **skin** (body surfaces); **Dis**infection → on **things** (inanimate objects).",
       "المطهّرات الموضعية `(Antiseptics)` ← على **الجلد** (أسطح الجسم)؛ التطهير `(Disinfection)` ← على **الأشياء** (الأجسام غير الحيّة)."),
    ]), title=("Memory Tips", "طرق للحفظ"))
  + box("compare", ul([
      ("**Biosafety** risks = risks of **accidental infection**.", "مخاطر **السلامة الحيوية** = مخاطر **العدوى العَرَضية**."),
      ("**Biosecurity** risks = unauthorized access, loss, theft, misuse, diversion or intentional release.", "مخاطر **الأمن الحيوي** = الوصول غير المصرَّح به، الفقدان، السرقة، إساءة الاستخدام، التحويل أو الإطلاق المتعمَّد."),
    ]), title=("Biosafety vs Biosecurity", "السلامة الحيوية مقابل الأمن الحيوي"))
))

# ---------------------------------------------------------------- assemble
pages = [cover()]
toc_entries = []
num = 2
body_pages = []
for i, (toc, html_) in enumerate(P):
    num += 1  # page 2 is the info/contents page
    if toc: toc_entries.append((toc, num))
    body_pages.append(page(html_, HDR, FL, FR, num))

info = ('<div class="card"><div class="card-h"><span dir="ltr">Lecture card</span><span dir="rtl">بطاقة المحاضرة</span></div>'
  + "".join(f'<div class="card-r"><span class="k">{k}</span><span class="v" dir="ltr">{v}</span><span class="va" dir="rtl">{a}</span></div>' for k, v, a in [
      ("Subject", SUBJ_EN, SUBJ_AR), ("Stage", "The fourth stage", "المرحلة الرابعة"),
      ("Lab no.", "Lab: 1", "المختبر: ١"), ("Title", TITLE_EN, TITLE_AR), ("Type", "Practical (Laboratories)", "عملي (المختبرات)")])
  + "</div>")
toc = ('<div class="h2"><span class="h2-en">Contents</span><span class="h2-ar" dir="rtl">المحتويات</span></div><ul class="toc">'
  + "".join(f'<li><span class="n">{n}</span><span class="te" dir="ltr">{e}</span><span class="ta" dir="rtl">{a}</span><span class="p">{p}</span></li>'
            for (n, e, a), p in toc_entries) + "</ul>")
pages.append(page(info + toc, HDR, FL, FR, 2))
pages += body_pages

open("booklet.html", "w").write(doc("Biosafety Booklet", pages, COVER_CSS))
print("pages", len(pages))
