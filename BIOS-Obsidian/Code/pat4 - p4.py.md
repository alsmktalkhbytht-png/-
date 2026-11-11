---
source: BIOS-Obsidian/tools/scripts/pat4/p4.py
handouts: []
saved: 2026-11-11
tags: [bios, code]
---
# pat4/p4.py

Utility script.

```python
import sys, re; sys.path.insert(0, "/tmp/claude-0/-home-user--/67d83c9a-7b0e-5ae5-b52b-cd659ab074ab/scratchpad/imm456")
from ci import *            # c helpers + B INSHORT TERMS balance save(split.fix)
import split
split.ABBR = split.ABBR + ("e.g.,",)

# Pathology — lecture 4 (stage 4) — د. حامد خليل التميمي — Lung Cancer

BN = lambda en, ar: N(en, ar, label=["BIOS note", "ملاحظة BIOS"])
O = P
def TERMS6(terms, n=6):
    head = [B("Term", "المصطلح"), "الترجمات العربية المستعملة"]
    return [SEC("Key terms", "أهم المصطلحات")] + [T(head, [[f"**{e}**", a] for e, a in terms[i:i + n]], ar_cols=[1], widths=[36, 64])
                                                  for i in range(0, len(terms), n)]

blocks = [
 # ───────────────────────── 1. Lung tumors
 SEC("LUNG TUMORS", "أورام الرئة"),
 FF(("lung-tumor.jpg", "Lung cancer", "سرطان الرئة", "50mm"),
    ("lung-diagram.jpg", "Trachea, Right Lung, Left Lung, Tumors, Lymph Nodes, Bronchus", "الرغامى، الرئة اليمنى، الرئة اليسرى، الأورام، العقد اللمفية، القصبة", "50mm")),
 C(["Although lungs frequently are the site of metastases from cancers arising in extra-thoracic organs, primary lung cancer is also a common disease.",
    "Roughly 95% of primary lung tumors are carcinomas; the remaining 5% constitute a miscellaneous group that includes carcinoids, mesenchymal malignancies (e.g., fibrosarcomas, leiomyomas), lymphomas, and a few benign lesions."],
   ["مع أن الرئتين كثيرًا ما تكونان **موقعًا للنقائل** من سرطانات تنشأ في أعضاء خارج الصدر، فإن **سرطان الرئة الأولي** مرض شائع أيضًا.",
    "حوالي **95%** من أورام الرئة الأولية **كارسينومات (سرطانات ظهارية)**؛ والـ**5%** الباقية مجموعة متنوّعة تشمل **الكارسينويدات**، والخباثات المتوسطية (مثل **الساركوما الليفية** و**الأورام العضلية الملساء**)، و**اللمفومات**، وبعض الآفات الحميدة."]),
 BN("“leiomyomas” are benign; the malignant smooth-muscle tumor is **leiomyosarcoma** — written as in the slide.", "“leiomyomas” أورام حميدة؛ والورم الخبيث للعضل الأملس هو **leiomyosarcoma** — كُتبت كما في الشريحة."),
 H2("BENIGN TUMORS OF LUNG", "أورام الرئة الحميدة"),
 C(["The most common benign tumor is a spherical, small (3 to 4 cm), discrete “hamartoma” that often shows up as a so-called coin lesion on chest radiographs.",
    "It consists mainly of mature cartilage, but this is often admixed with fat, fibrous tissue, and blood vessels in various proportions.",
    "Clonal cytogenic abnormalities Also confirm hamartoma."],
   ["أشيع ورم حميد هو **“الورم العابي (hamartoma)”** الكروي الصغير (**3 إلى 4 سم**) المحدّد، الذي يظهر غالبًا بما يسمّى **“آفة العملة النقدية” (coin lesion)** في صور الصدر الشعاعية.",
    "ويتكوّن أساسًا من **غضروف ناضج**، لكنه غالبًا يختلط بالدهن والنسيج الليفي والأوعية الدموية بنسب مختلفة.",
    "و**الشذوذات الوراثية الخلوية النسيلية** تؤكّد أيضًا الورم العابي."]),
 FF(("hamartoma-histology.jpg", "Hamartoma (histology)", "الورم العابي (مقطع نسيجي)", "50mm"),
    ("coin-lesion-cxr.jpg", "Coin lesion on chest radiograph", "آفة العملة النقدية في صورة الصدر الشعاعية", "50mm")),
 BN("“cytogenic” in the slide = **cytogenetic**.", "“cytogenic” في الشريحة أي **cytogenetic** (وراثي خلوي)."),
 INSHORT([("Lungs: common site of **metastases**, but primary lung cancer is common too; **95% carcinomas**, 5% others.", "الرئة: موقع شائع **للنقائل**، لكن السرطان الأولي شائع أيضًا؛ **95% كارسينومات**، و5% أخرى."),
          ("Commonest benign tumor: **hamartoma** — 3–4 cm, **coin lesion** on X-ray, mainly **mature cartilage** (+ fat, fibrous tissue, vessels).", "أشيع ورم حميد: **الورم العابي** — 3–4 سم، **آفة العملة** بالأشعة، أساسًا **غضروف ناضج** (+ دهن، ليف، أوعية).")]),

 # ───────────────────────── 2. Carcinomas
 SEC("CARCINOMAS", "الكارسينومات (سرطانات الرئة)"),
 C(["Carcinoma of the lung (also known as “lung cancer”) is without doubt the single most important cause of cancer-related deaths in industrialized countries.",
    "It has long held this position among males in the United States, accounting for about one third of cancer deaths in men, and has become the leading cause of cancer deaths in women as well."],
   ["**كارسينوما الرئة** (المعروفة بـ“سرطان الرئة”) هي بلا شك **أهم سبب منفرد لوفيات السرطان** في الدول الصناعية.",
    "وقد احتلّت هذه المكانة طويلًا بين الذكور في الولايات المتحدة، إذ تشكّل حوالي **ثلث وفيات السرطان عند الرجال**، وأصبحت **السبب الأول لوفيات السرطان عند النساء** أيضًا."]),
 C(["American Cancer Society estimates for 2011 included approximately 221,100 new cases of lung cancer and 156,900 deaths.",
    "The incidence among males is gradually decreasing, but it continues to increase among females, with more women dying each year from lung cancer than from breast cancers, since 1987."],
   ["تضمّنت تقديرات **جمعية السرطان الأمريكية لعام 2011** حوالي **221,100 حالة جديدة** من سرطان الرئة و**156,900 وفاة**.",
    "والإصابة بين الذكور **تتناقص تدريجيًا**، لكنها **مستمرة بالزيادة بين الإناث**، إذ تموت نساء كل سنة بسرطان الرئة أكثر من سرطانات الثدي، **منذ 1987**."]),
 C(["These statistics undoubtedly reflect the causal relationship of cigarette smoking and lung cancer.", "The peak incidence of lung cancer is in persons in their 50s and 60s."],
   ["وتعكس هذه الإحصائيات بلا شك **العلاقة السببية بين تدخين السجائر وسرطان الرئة**.", "وذروة الإصابة بسرطان الرئة في الأشخاص **في الخمسينات والستينات من العمر**."]),
 L(["Adenocarcinoma,", "Squamous cell carcinoma,", "Small cell carcinoma.", "Large cell carcinoma."],
   ["**الكارسينوما الغدّية**،", "**كارسينوما الخلايا الحرشفية**،", "**كارسينوما الخلايا الصغيرة**.", "**كارسينوما الخلايا الكبيرة**."],
   en="The four major histologic types of carcinomas of the lung are;", ar="الأنواع النسيجية الأربعة الرئيسية لكارسينومات الرئة هي:"),
 INSHORT([("Lung cancer = **most important cause of cancer deaths**; ~**1/3** of male cancer deaths; **leading** in women (more than breast since **1987**).", "سرطان الرئة = **أهم سبب لوفيات السرطان**؛ ~**ثلث** وفيات الذكور؛ **الأول** عند النساء (أكثر من الثدي منذ **1987**)."),
          ("Cause: **cigarette smoking**; peak age **50s–60s**.", "السبب: **تدخين السجائر**؛ ذروة العمر **50–60s**."),
          ("4 types: **adenocarcinoma, squamous, small cell, large cell**.", "4 أنواع: **الغدّية، الحرشفية، الخلايا الصغيرة، الخلايا الكبيرة**.")]),

 # ───────────────────────── 3. SCLC vs NSCLC
 SEC("SCLC and NSCLC", "سرطان الخلايا الصغيرة وغير الصغيرة"),
 L(["Small cell lung cancer (SCLC)", "Non–small cell lung cancer (NSCLC), with the latter including adenocarcinomas and squamous and large cell carcinomas."],
   ["**سرطان الرئة ذو الخلايا الصغيرة (SCLC)**", "**سرطان الرئة ذو الخلايا غير الصغيرة (NSCLC)**، ويشمل الأخير الكارسينومات الغدّية والحرشفية وكارسينومات الخلايا الكبيرة."],
   en="Until recently, carcinomas of the lung were classified into two broad groups:", ar="حتى وقت قريب كانت كارسينومات الرئة تُصنَّف إلى **مجموعتين واسعتين**:"),
 C(["The key reason for this historical distinction was that virtually all SCLCs have metastasized by the time of diagnosis and hence are not curable by surgery.", "Therefore, they are best treated by chemotherapy, with or without radiation therapy."],
   ["والسبب الرئيسي لهذا التمييز التاريخي أن **كل حالات SCLC تقريبًا تكون قد انتشرت عند التشخيص**، لذا **لا تُشفى بالجراحة**.", "ولذلك يكون علاجها الأفضل **بالعلاج الكيميائي**، مع أو بدون **العلاج الإشعاعي**."]),
 C(["By contrast, NSCLCs were more likely to be re-sectable and usually responded poorly to chemotherapy; however, now therapies are available that target specific mutated gene products present in the various subtypes of NSCLC, mainly in adenocarcinomas.",
    "Thus, NSCLC must be sub-classified into histologic and molecular subtypes."],
   ["في المقابل، كانت NSCLC **أكثر قابلية للاستئصال الجراحي** وتستجيب عادةً **بشكل ضعيف للعلاج الكيميائي**؛ لكن تتوفّر الآن **علاجات تستهدف نواتج جينات طافرة محدّدة** في الأنواع الفرعية المختلفة من NSCLC، **خاصةً في الكارسينومات الغدّية**.",
    "لذا يجب **تصنيف NSCLC فرعيًا** إلى أنواع **نسيجية وجزيئية**."]),
 F("subtypes.jpg", "Lung Cancer (LC) sub-types and origin: SCLC (~15%) — neuroendocrine cell; NSCLC (~85%): LUAD — alveolar type II epithelial cell, LUSC — basal epithelial cell, LCC — various epithelial cells",
   "أنواع سرطان الرئة الفرعية ومنشؤها: SCLC (~15%) — خلية صمّاء عصبية؛ NSCLC (~85%): الغدّية (LUAD) — خلية ظهارية سنخية نوع II، الحرشفية (LUSC) — خلية ظهارية قاعدية، الخلايا الكبيرة (LCC) — خلايا ظهارية متنوّعة", h="64mm", fit="contain"),
 T([B("Feature", "الصفة"), B("SCLC", "الخلايا الصغيرة"), B("NSCLC", "غير الصغيرة")],
   [[B("**Share (figure)**", "**النسبة (الشكل)**"), B("~15%", "~15%"), B("~85%", "~85%")],
    [B("**Includes**", "**يشمل**"), B("small cell carcinoma", "كارسينوما الخلايا الصغيرة"), B("adenocarcinoma, squamous, large cell", "الغدّية، الحرشفية، الخلايا الكبيرة")],
    [B("**At diagnosis**", "**عند التشخيص**"), B("virtually all metastasized", "كلها تقريبًا منتشرة"), B("more likely re-sectable", "أكثر قابلية للاستئصال")],
    [B("**Treatment**", "**العلاج**"), B("chemotherapy ± radiation", "كيميائي ± إشعاعي"), B("surgery; targeted therapy (mutated genes, mainly adenocarcinoma)", "جراحة؛ علاج موجّه (جينات طافرة، خاصةً الغدّية)")]],
   key_cols=[0], widths=[24, 34, 42], style="summary", label_en="SCLC vs NSCLC", label_ar="SCLC مقابل NSCLC"),
 INSHORT([("**SCLC**: metastasized at diagnosis → **not surgical** → chemo ± radiation.", "**SCLC**: منتشر عند التشخيص ← **لا جراحة** ← كيميائي ± إشعاعي."),
          ("**NSCLC**: re-sectable, poor chemo response, now **targeted therapy** → must be sub-classified (histologic + molecular).", "**NSCLC**: قابل للاستئصال، استجابة ضعيفة للكيميائي، والآن **علاج موجّه** ← يجب تصنيفه فرعيًا (نسيجيًا + جزيئيًا).")]),

 # ───────────────────────── 4. Histology
 SEC("LUNG CANCER HISTOLOGY", "نسيجية سرطان الرئة"),
 F("histology-chart.jpg", "Lung cancer histology", "نسيجية سرطان الرئة", h="96mm", fit="contain"),
 T([B("Group in the chart", "المجموعة في المخطط"), B("Types written in the chart", "الأنواع المكتوبة في المخطط")],
   [[B("**Small cell carcinoma**", "**كارسينوما الخلايا الصغيرة**"), B("Pure small cell lung carcinoma; Combined small cell/non-small cell lung carcinoma", "كارسينوما رئة صغيرة الخلايا نقية؛ كارسينوما مختلطة صغيرة/غير صغيرة الخلايا")],
    [B("**Carcinoid tumor**", "**الورم الكارسينويدي**"), B("Typical carcinoid; Atypical carcinoid", "كارسينويد نموذجي؛ كارسينويد غير نموذجي")],
    [B("**Carcinomas of salivary gland type**", "**كارسينومات من نوع الغدد اللعابية**"), B("Mucoepidermoid carcinoma; Adenoid cystic carcinoma", "الكارسينوما المخاطية البشروية؛ الكارسينوما الغدّانية الكيسية")],
    [B("**Carcinomas with pleomorphic, sarcomatoid, or sarcomatous elements**", "**كارسينومات بعناصر متعدّدة الأشكال أو شبه ساركومية أو ساركومية**"), B("Sarcomas with spindle and/or giant cells; Spindle cell carcinoma; Giant cell carcinoma; Carcinocarcinoma; Pulmonary blastoma", "ساركومات بخلايا مغزلية و/أو عملاقة؛ كارسينوما الخلايا المغزلية؛ كارسينوما الخلايا العملاقة؛ Carcinocarcinoma؛ الورم الأرومي الرئوي")],
    [B("**Large cell carcinoma**", "**كارسينوما الخلايا الكبيرة**"), B("Several variants", "عدّة أنواع")],
    [B("**Squamous cell carcinoma**", "**كارسينوما الخلايا الحرشفية**"), B("Papillary; Clear cell; Basaloid; Small cell", "حليمي؛ صافي الخلايا؛ شبه قاعدي؛ صغير الخلايا")],
    [B("**Adenocarcinoma**", "**الكارسينوما الغدّية**"), B("Acinar; Papillary; Solid adenocarcinoma with mucin; Bronchioalveolar", "عنبي؛ حليمي؛ كارسينوما غدّية صلبة مع مخاط؛ قصيبي سنخي")]],
   key_cols=[0], widths=[36, 64], style="summary", label_en="Labels in the chart (all non-small cell except the first row)", label_ar="كتابات المخطط (كلها غير صغيرة الخلايا عدا الصف الأول)"),
 BN("“Carcinocarcinoma” in the chart is usually written **carcinosarcoma**.", "“Carcinocarcinoma” في المخطط تُكتب عادةً **carcinosarcoma** (الساركوما الكارسينومية)."),
 INSHORT([("Chart: **small cell** vs **non-small cell** (carcinoid, salivary-type, sarcomatoid, large cell, squamous, adenocarcinoma).", "المخطط: **صغيرة الخلايا** مقابل **غير الصغيرة** (كارسينويد، نوع الغدد اللعابية، شبه ساركومي، خلايا كبيرة، حرشفية، غدّية)."),
          ("Adenocarcinoma subtypes: **acinar, papillary, solid with mucin, bronchioalveolar**.", "أنواع الغدّية: **عنبي، حليمي، صلب مع مخاط، قصيبي سنخي**.")]),

 # ───────────────────────── 5. Etiology and pathogenesis
 SEC("ETIOLOGY AND PATHOGENESIS", "السببيات والإمراضية"),
 C(["Smoking-related carcinomas of the lung arise by a stepwise accumulation of a multitude of genetic abnormalities (estimated to be in the thousands for small cell carcinoma) that result in transformation of benign progenitor cells in the lung into neoplastic cells.",
    "The sequence of molecular changes is not random but follows a predictable sequence that parallels the histologic progression toward cancer."],
   ["تنشأ كارسينومات الرئة المرتبطة بالتدخين **بتراكم تدريجي لعدد كبير من الشذوذات الجينية** (تُقدَّر **بالآلاف** في كارسينوما الخلايا الصغيرة) تؤدّي إلى **تحوّل الخلايا السلفية الحميدة** في الرئة إلى **خلايا ورمية**.",
    "وتسلسل التغيّرات الجزيئية **ليس عشوائيًا** بل يتبع **تسلسلًا متوقّعًا يوازي التطوّر النسيجي** نحو السرطان."]),
 C("Thus, inactivation of the putative tumor suppressor genes located on the short arm of chromosome 3 (3p) is a very early event, whereas TP53mutations or activation of the KRAS oncogene occurs relatively late.",
   "فتعطيل **الجينات الكابتة للورم المفترضة** على **الذراع القصير للكروموسوم 3 (3p)** حدث **مبكر جدًا**، بينما **طفرات TP53** أو **تنشيط الجين الورمي KRAS** تحدث **متأخرة نسبيًا**."),
 FLOW([("3p tumor suppressor loss (very early)", "فقد كابتات 3p (مبكر جدًا)"), ("…accumulating genetic changes…", "…تراكم التغيّرات الجينية…"), ("TP53 mutation / KRAS activation (late)", "طفرة TP53 / تنشيط KRAS (متأخر)"), ("Cancer", "السرطان")]),
 INSHORT([("Stepwise accumulation of **genetic abnormalities** (thousands in SCLC) in a **predictable sequence**.", "تراكم تدريجي **لشذوذات جينية** (بالآلاف في SCLC) **بتسلسل متوقّع**."),
          ("**3p** tumor-suppressor loss = **very early**; **TP53 / KRAS** = **late**.", "فقد كابتات **3p** = **مبكر جدًا**؛ **TP53 / KRAS** = **متأخر**.")]),

 # ───────────────────────── 6. Predisposing factors
 SEC("PREDISPOSING FACTORS", "العوامل المهيّئة"),
 L(["About 90% of lung cancers occur in active smokers or those who stopped recently. A nearly linear correlation has been recognized between the frequency of lung cancer and pack-years of cigarette smoking.",
    "The increased risk becomes 60 times greater among habitual heavy smokers (two packs a day for 20 years) than among non-smokers.",
    "For reasons not entirely clear, women have a higher susceptibility to carcinogens in tobacco than men."],
   ["حوالي **90%** من سرطانات الرئة تحدث عند **المدخّنين الحاليين** أو من أقلعوا حديثًا. وقد عُرفت **علاقة خطية تقريبًا** بين تكرار سرطان الرئة و**سنوات العلبة (pack-years)** من تدخين السجائر.",
    "يصبح الخطر أكبر **60 مرة** عند **المدخّنين الشرهين المعتادين** (**علبتان يوميًا لمدة 20 سنة**) مقارنةً بغير المدخّنين.",
    "ولأسباب غير واضحة تمامًا، **النساء أكثر تأثّرًا** بمسرطنات التبغ من الرجال."]),
 L(["Although cessation of smoking decreases the risk of developing lung cancer over time, it may never return to baseline levels.",
    "In fact, genetic changes that predate lung cancer can persist for many years in the bronchial epithelium of former smokers."],
   ["مع أن **الإقلاع عن التدخين يقلّل الخطر** بمرور الوقت، فقد **لا يعود أبدًا** إلى المستوى الأساسي.",
    "وفي الحقيقة، **التغيّرات الجينية** التي تسبق سرطان الرئة قد **تستمر سنوات طويلة** في ظهارة القصبات عند المدخّنين السابقين."], start=4),
 L(["Passive smoking (proximity to cigarette smokers) increases the risk of developing lung cancer to approximately twice that of non-smokers.",
    "The smoking of pipes and cigars also increases the risk, but only modestly."],
   ["**التدخين السلبي** (القرب من مدخّني السجائر) يزيد خطر سرطان الرئة إلى **ضعفي** خطر غير المدخّنين تقريبًا.",
    "وتدخين **الغليون والسيجار** يزيد الخطر أيضًا، لكن **بشكل متواضع** فقط."], start=6),
 F("pipe-cigarette.jpg", "Pipe and cigarette", "الغليون والسيجارة", h="50mm", fit="contain"),
 C(["**6-** Workers exposed to dusts containing arsenic, chromium, uranium, nickel, vinyl chloride, and mustard gas.", "Exposure to asbestos increases the risk of lung cancer fivefold in non-smokers."],
   ["**6-** **العمّال المعرّضون** لأتربة تحتوي **الزرنيخ والكروم واليورانيوم والنيكل وكلوريد الفاينيل وغاز الخردل**.", "و**التعرّض للأسبستوس** يزيد خطر سرطان الرئة **خمسة أضعاف** عند غير المدخّنين."]),
 BN("The slide numbers two different points as “6-” (pipes and cigars, then occupational dusts) — the handout keeps the slide’s own numbering for the last one.",
    "ترقّم الشريحة نقطتين مختلفتين بـ“6-” (الغليون والسيجار، ثم الأتربة المهنية) — وأبقت الملزمة رقم الشريحة للنقطة الأخيرة."),
 T([B("Factor", "العامل"), B("Risk", "الخطر")],
   [[B("**Active / recent smokers**", "**المدخّنون الحاليون / الحديثو الإقلاع**"), B("about 90% of lung cancers", "حوالي 90% من سرطانات الرئة")],
    [B("**Heavy smokers** (2 packs/day × 20 years)", "**المدخّنون الشرهون** (علبتان/يوم × 20 سنة)"), B("60 times", "60 ضعفًا")],
    [B("**Passive smoking**", "**التدخين السلبي**"), B("about twice", "حوالي الضعف")]],
   key_cols=[0], widths=[50, 50], style="summary", label_en="Numbers to remember", label_ar="أرقام للحفظ"),
 T([B("Factor", "العامل"), B("Risk", "الخطر")],
   [[B("**Pipes and cigars**", "**الغليون والسيجار**"), B("modest increase", "زيادة متواضعة")],
    [B("**Asbestos** (non-smokers)", "**الأسبستوس** (غير المدخّنين)"), B("fivefold", "خمسة أضعاف")],
    [B("**Mutagen sensitivity genotype**", "**النمط الجيني الحسّاس للمطفّرات**"), B("> 10-fold", "أكثر من 10 أضعاف")]],
   key_cols=[0], widths=[50, 50], style="summary", label_en="Numbers to remember (cont.)", label_ar="أرقام للحفظ (تكملة)"),
 INSHORT([("**90%** in smokers; risk ∝ **pack-years**; heavy smokers **×60**; women more susceptible.", "**90%** عند المدخّنين؛ الخطر ∝ **سنوات العلبة**؛ الشرهون **×60**؛ النساء أكثر تأثّرًا."),
          ("Quitting lowers risk but **never to baseline**; passive smoking **×2**; pipes/cigars modest.", "الإقلاع يقلّل الخطر لكن **ليس للمستوى الأساسي**؛ التدخين السلبي **×2**؛ الغليون/السيجار متواضع."),
          ("Occupational: **arsenic, chromium, uranium, nickel, vinyl chloride, mustard gas**; **asbestos ×5** in non-smokers.", "المهني: **الزرنيخ، الكروم، اليورانيوم، النيكل، كلوريد الفاينيل، غاز الخردل**؛ **الأسبستوس ×5** عند غير المدخّنين.")]),

 # ───────────────────────── 7. Chemical substances
 SEC("CHEMICALS SUBSTANCES", "المواد الكيميائية"),
 C("Many chemicals (procarcinogens) require metabolic activation via the P-450 monooxygenase enzyme system for conversion into ultimate carcinogens .",
   "كثير من المواد الكيميائية (**طلائع المسرطنات**) تحتاج **تنشيطًا أيضيًا** عبر **نظام إنزيم P-450 أحادي الأوكسجيناز** لتتحوّل إلى **مسرطنات نهائية**."),
 C(["There is evidence that persons with specific genetic polymorphisms involving the P-450 genes have an increased capacity to metabolize procarcinogens derived from cigarette smoke, and thus conceivably incur the greatest risk for development of lung cancer."],
   ["وهناك دليل على أن الأشخاص ذوي **تعدّدات أشكال جينية محدّدة في جينات P-450** لديهم **قدرة أكبر على استقلاب** طلائع المسرطنات المشتقّة من دخان السجائر، وبالتالي يُحتمل أن يتعرّضوا **لأكبر خطر** للإصابة بسرطان الرئة."]),
 C("Similarly, persons whose peripheral blood lymphocytes undergo chromosomal breakages after exposure to tobacco-related carcinogens (mutagen sensitivity genotype) have a greater than 10-fold risk of developing lung cancer over that of control subjects.",
   "وبالمثل، الأشخاص الذين تتعرّض **لمفاويات دمهم المحيطي لكسور كروموسومية** بعد التعرّض لمسرطنات التبغ (**النمط الجيني الحسّاس للمطفّرات**) لديهم خطر أكبر من **10 أضعاف** للإصابة بسرطان الرئة مقارنةً بالأشخاص الضابطين."),
 C("The sequential changes leading to cancer have been best documented for squamous cell carcinomas, but they also are present in other histologic subtypes",
   "التغيّرات المتسلسلة المؤدّية للسرطان **موثّقة أفضل في كارسينوما الخلايا الحرشفية**، لكنها موجودة أيضًا في الأنواع النسيجية الأخرى"),
 C(["In essence, there is a linear correlation between the intensity of exposure to cigarette smoke and the appearance of ever more worrisome epithelial changes that begin with rather innocuous basal cell hyperplasia and squamous metaplasia and progress to squamous dysplasia and carcinoma in situ, before culminating in invasive cancer."],
   ["وجوهر الأمر وجود **علاقة خطية** بين **شدّة التعرّض لدخان السجائر** وظهور تغيّرات ظهارية متزايدة الخطورة تبدأ **بفرط تنسّج الخلايا القاعدية والحؤول الحرشفي** غير المؤذيين نسبيًا، وتتطوّر إلى **خلل التنسّج الحرشفي** و**الكارسينوما الموضعية**، قبل أن تنتهي **بسرطان غازٍ**."]),
 FLOW([("Basal cell hyperplasia", "فرط تنسّج الخلايا القاعدية"), ("Squamous metaplasia", "الحؤول الحرشفي"), ("Squamous dysplasia", "خلل التنسّج الحرشفي"), ("Carcinoma in situ", "الكارسينوما الموضعية"), ("Invasive cancer", "السرطان الغازي")]),
 C("Among the major histologic subtypes of lung cancer, squamous and small-cell carcinomas show the strongest association with tobacco exposure.",
   "ومن بين الأنواع النسيجية الرئيسية لسرطان الرئة، تُظهر **الكارسينوما الحرشفية وكارسينوما الخلايا الصغيرة أقوى ارتباط** بالتعرّض للتبغ."),
 INSHORT([("**Procarcinogens** → activated by **P-450 monooxygenase** → ultimate carcinogens; P-450 **polymorphisms** ↑ risk.", "**طلائع المسرطنات** ← تُنشَّط بـ**P-450 أحادي الأوكسجيناز** ← مسرطنات نهائية؛ **تعدّد أشكال** P-450 ↑ الخطر."),
          ("**Mutagen sensitivity genotype** (lymphocyte chromosome breaks) → **> 10-fold** risk.", "**النمط الحسّاس للمطفّرات** (كسور كروموسومات اللمفاويات) ← خطر **> 10 أضعاف**."),
          ("Sequence: **basal hyperplasia → squamous metaplasia → dysplasia → CIS → invasive**; strongest tobacco link: **squamous + small cell**.", "التسلسل: **فرط تنسّج قاعدي ← حؤول حرشفي ← خلل تنسّج ← كارسينوما موضعية ← غازٍ**؛ أقوى ارتباط بالتبغ: **الحرشفية + صغيرة الخلايا**.")]),

 *TERMS6([("Metastasis", "النقيلة / الانتشار الثانوي"), ("Carcinoma", "الكارسينوما / السرطان الظهاري"), ("Hamartoma", "الورم العابي / الورم الخلطي"),
          ("Coin lesion", "آفة العملة النقدية / الظلّ الدائري"), ("Carcinoid", "الكارسينويد / الورم شبه السرطاني"), ("Mesenchymal", "متوسطي / لُحمي"),
          ("Adenocarcinoma", "الكارسينوما الغدّية / السرطان الغدّي"), ("Squamous cell carcinoma", "كارسينوما الخلايا الحرشفية"), ("Small cell lung cancer (SCLC)", "سرطان الرئة صغير الخلايا"),
          ("Non-small cell lung cancer (NSCLC)", "سرطان الرئة غير صغير الخلايا"), ("Re-sectable", "قابل للاستئصال الجراحي"), ("Chemotherapy", "العلاج الكيميائي"),
          ("Tumor suppressor gene", "الجين الكابت للورم"), ("Oncogene (KRAS)", "الجين الورمي / الجين المسرطن"), ("Pack-years", "سنوات العلبة"),
          ("Passive smoking", "التدخين السلبي / التدخين القسري"), ("Asbestos", "الأسبستوس / الحرير الصخري"), ("Procarcinogen", "طليعة المسرطن / مسرطن أولي"),
          ("Polymorphism", "تعدّد الأشكال الجيني"), ("Squamous metaplasia", "الحؤول الحرشفي"), ("Dysplasia", "خلل التنسّج"),
          ("Carcinoma in situ", "الكارسينوما الموضعية / السرطان اللابد"), ("Invasive cancer", "السرطان الغازي / المجتاح")]),
]

exec(open(__file__.replace("p4.py", "p4q.py")).read())

```
