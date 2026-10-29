---
source: BIOS-Obsidian/tools/scripts/tb/turb.py
handouts: [hematology-practical-turbidimetry]
saved: 2026-10-29
tags: [bios, code]
---
# tb/turb.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#hematology-practical-turbidimetry|hematology-practical-turbidimetry]]

```python
import sys; sys.path.insert(0, "/tmp/claude-0/-home-user--/8f878068-bae9-502b-96f7-788f221c7cb0/scratchpad/imm456")
from ci import *            # c helpers + B INSHORT TERMS balance save(split.fix)

blocks = [
 SEC("What is Turbidimetry?", "ما هو قياس العكارة؟"),
 SIDE([L(["Turbidimetry measures the **cloudiness of a liquid sample**.", "Cloudiness is caused by **particles suspended** in the sample.",
          "The instrument measures **how much light passes through** the sample."],
         ["يقيس قياسُ العكارة **تعكّرَ العيّنة السائلة**.", "ينتج التعكّر عن **جسيمات عالقة** في العيّنة.",
          "ويقيس الجهاز **كمية الضوء التي تنفذ خلال** العيّنة."])],
      "turbidimeter-kit.jpg", "A portable turbidimeter kit", "جهاز قياس العكارة المحمول"),
 INSHORT([("Turbidimetry = measuring **cloudiness**.", "قياس العكارة = قياس **التعكّر**."),
          ("Cloudiness comes from **suspended particles**.", "يأتي التعكّر من **الجسيمات العالقة**."),
          ("The instrument reads the light that **passes through**.", "يقرأ الجهاز الضوء الذي **ينفذ خلال** العيّنة.")]),

 SEC("Principle", "المبدأ"),
 L(["A **beam of light** passes through the sample.", "**Suspended particles reduce** the amount of light that passes straight through.",
    "The **detector** measures the **transmitted light**.", "**More turbidity → less transmitted light.**"],
   ["تمرّ **حزمة ضوئية** خلال العيّنة.", "**تقلّل الجسيمات العالقة** كمية الضوء التي تنفذ بشكل مستقيم.",
    "ويقيس **الكاشف** **الضوء النافذ**.", "**عكارة أكثر ← ضوء نافذ أقل.**"]),
 FLOW([("Light source", "مصدر الضوء"), ("Sample", "العيّنة"), ("Transmitted light (measured)", "الضوء النافذ (يُقاس)"), ("Detector", "الكاشف")]),
 F("turbidimeter-diagram.png", "Turbidimeter: visible light → filter → sample cell → photocell detector → read out device",
   "جهاز قياس العكارة: ضوء مرئي ← مرشّح ← خلية العيّنة ← كاشف خلية ضوئية ← جهاز عرض القراءة", h="62mm"),
 T([B("Label in the figure", "التسمية في الشكل"), B("Meaning", "المعنى")],
   [[B("**Visible light**", "**ضوء مرئي**"), B("The light source of the instrument", "مصدر الضوء في الجهاز")],
    [B("**Filter**", "**مرشّح**"), B("Selects the light that reaches the sample", "يختار الضوء الذي يصل إلى العيّنة")],
    [B("**Sample Cell**", "**خلية العيّنة**"), B("Holds the cloudy sample (cuvette)", "تحمل العيّنة العكرة (الكيوفيت)")],
    [B("**Photocell Detector**", "**كاشف الخلية الضوئية**"), B("Measures the transmitted light", "يقيس الضوء النافذ")],
    [B("**Read Out Device**", "**جهاز عرض القراءة**"), B("Shows the result", "يعرض النتيجة")]],
   key_cols=[0], widths=[38, 62], label_en="Figure labels", label_ar="تسميات الشكل"),
 N("The meanings of the figure labels are explained by BIOS; the slide shows only the labels.",
   "معاني تسميات الشكل شرحٌ من BIOS؛ والشريحة تعرض التسميات فقط.", label=["BIOS note", "ملاحظة BIOS"]),
 INSHORT([("Light → sample → detector, in a **straight line**.", "الضوء ← العيّنة ← الكاشف، في **خط مستقيم**."),
          ("The detector reads **transmitted** light.", "يقرأ الكاشف الضوء **النافذ**."),
          ("**More turbidity = less transmitted light.**", "**عكارة أكثر = ضوء نافذ أقل.**")]),

 SEC("Clinical Immunoturbidimetry", "قياس العكارة المناعي السريري"),
 H2("Medical laboratory use", "الاستعمال في المختبر الطبي"),
 L(["In many clinical tests, an **antigen** reacts with a **specific antibody**.", "This reaction forms small **immune complexes**.",
    "The complexes make the sample **more turbid**.", "The analyzer measures this change to **estimate the amount of the analyte**."],
   ["في كثير من الفحوص السريرية يتفاعل **مستضد** مع **ضد نوعي**.", "يكوّن هذا التفاعل **معقّدات مناعية** صغيرة.",
    "وتجعل هذه المعقّدات العيّنة **أكثر عكارة**.", "ويقيس المحلّل هذا التغيّر **لتقدير كمية المادة المقاسة**."]),
 FLOW([("Antigen + Antibody", "مستضد + ضد"), ("immune complexes", "معقّدات مناعية"), ("turbidity increases", "تزداد العكارة")]),
 INSHORT([("Antigen + specific antibody → **immune complexes**.", "مستضد + ضد نوعي ← **معقّدات مناعية**."),
          ("Complexes → **more turbidity** → the analyzer estimates the analyte.", "المعقّدات ← **عكارة أكثر** ← يقدّر المحلّل كمية المادة المقاسة.")]),

 SEC("Instrument", "الجهاز"),
 T([B("Turbidimetry can be measured using:", "يمكن قياس العكارة باستعمال:"), B("Main parts", "الأجزاء الرئيسة")],
   [[B("**Spectrophotometer**", "**مطياف ضوئي**"), B("**Light source**", "**مصدر الضوء**")],
    [B("**Automated chemistry analyzer**", "**محلّل كيميائي آلي**"), B("**Sample cell / cuvette**", "**خلية العيّنة / الكيوفيت**")],
    [B("**Turbidimetric analyzer**", "**محلّل العكارة**"), B("**Detector**", "**الكاشف**")],
    ["", B("**Display or computer**", "**شاشة عرض أو حاسوب**")]],
   widths=[50, 50]),
 FF(("instrument-cuvette.jpg", "Placing the cuvette in the instrument", "وضع الكيوفيت في الجهاز", "44mm"),
    ("instrument-analyzer.jpg", "A turbidimetric analyzer with samples", "محلّل عكارة مع العيّنات", "44mm")),
 INSHORT([("3 instruments: **spectrophotometer, automated chemistry analyzer, turbidimetric analyzer**.", "3 أجهزة: **المطياف الضوئي، والمحلّل الكيميائي الآلي، ومحلّل العكارة**."),
          ("4 parts: **light source → cuvette → detector → display**.", "4 أجزاء: **مصدر الضوء ← الكيوفيت ← الكاشف ← الشاشة**.")]),

 SEC("Clinical Applications", "التطبيقات السريرية"),
 T([B("Measured by turbidimetry", "ما يُقاس بالعكارة"), B("Examples", "أمثلة")],
   [[B("**C-reactive protein (CRP)**", "**البروتين المتفاعل C**"), "CRP"],
    [B("**Immunoglobulins**", "**الغلوبولينات المناعية**"), B("such as IgG, IgA, and IgM", "مثل IgG وIgA وIgM")],
    [B("**Complement proteins**", "**بروتينات المتمّمة**"), B("such as C3 and C4", "مثل C3 وC4")],
    [B("**Transferrin and other specific proteins**", "**الترانسفيرين وبروتينات نوعية أخرى**"), "Transferrin"],
    [B("**Some urine protein measurements**", "**بعض قياسات بروتين الإدرار**"), B("urine protein", "بروتين الإدرار")]],
   key_cols=[0], widths=[55, 45], style="summary", label_en="Applications", label_ar="التطبيقات"),
 INSHORT([("Remember **CRP**, **IgG/IgA/IgM**, **C3/C4**, **transferrin**, **urine protein**.", "تذكّر **CRP**، و**IgG/IgA/IgM**، و**C3/C4**، و**الترانسفيرين**، و**بروتين الإدرار**."),
          ("All are **specific proteins** measured by antigen–antibody turbidity.", "كلها **بروتينات نوعية** تُقاس بعكارة تفاعل المستضد والضد.")]),

 SEC("Basic Practical Steps", "الخطوات العملية الأساسية"),
 R("**Prepare** the sample and reagent", "**حضّر** العيّنة والكاشف"),
 R("**Mix** them correctly", "**امزجهما** بشكل صحيح"),
 R("Allow the reaction to **develop**", "اترك التفاعل **ليكتمل**"),
 R("Place the **cuvette** in the instrument", "ضع **الكيوفيت** في الجهاز"),
 R("**Measure** the turbidity / absorbance", "**قِس** العكارة / الامتصاص"),
 R("**Record** the result", "**سجّل** النتيجة"),
 FLOW([("Prepare", "حضّر"), ("Mix", "امزج"), ("React", "تفاعل"), ("Cuvette", "الكيوفيت"), ("Measure", "قِس"), ("Record", "سجّل")]),
 INSHORT([("6 steps: **prepare → mix → react → cuvette → measure → record**.", "6 خطوات: **حضّر ← امزج ← تفاعل ← الكيوفيت ← قِس ← سجّل**.")]),

 SEC("Turbidimetry vs Nephelometry", "قياس العكارة مقابل قياس التشتّت"),
 T([B("Turbidimetry", "قياس العكارة"), B("Nephelometry", "قياس التشتّت (النفلومتري)")],
   [[B("1. Measures **transmitted light**.", "1. يقيس **الضوء النافذ**."), B("1. Measures **scattered light**.", "1. يقيس **الضوء المتشتّت**.")],
    [B("2. Detector is **in line with the light beam**.", "2. الكاشف **على خط الحزمة الضوئية**."), B("2. The detector is placed **at an angle, commonly 90°**.", "2. يوضع الكاشف **بزاوية، غالبًا 90°**.")],
    [B("3. More turbidity → **less transmitted light**.", "3. عكارة أكثر ← **ضوء نافذ أقل**."), B("3. More particles → **more scattered light**.", "3. جسيمات أكثر ← **ضوء متشتّت أكثر**.")]],
   widths=[50, 50], style="summary", label_en="Comparison", label_ar="مقارنة"),
 F("turbid-vs-nephelo.png", "Turbidimetry: detector in line with the beam; nephelometry: detector at an angle to read scattered light",
   "قياس العكارة: الكاشف على خط الحزمة؛ قياس التشتّت: الكاشف بزاوية ليقرأ الضوء المتشتّت", h="48mm"),
 T([B("Label in the figure", "التسمية في الشكل"), B("Arabic", "بالعربي")],
   [["**Light source**", "مصدر الضوء"], ["**Lens**", "عدسة"], ["**Sample**", "العيّنة"], ["**Scattered light**", "الضوء المتشتّت"], ["**Detector and readout**", "الكاشف والقراءة"]],
   key_cols=[0], ar_cols=[1], widths=[45, 55], label_en="Figure labels", label_ar="تسميات الشكل"),
 INSHORT([("**Turbidimetry** = transmitted light, detector **straight** (180°).", "**قياس العكارة** = ضوء نافذ، والكاشف **مستقيم** (180°)."),
          ("**Nephelometry** = scattered light, detector **at 90°**.", "**قياس التشتّت** = ضوء متشتّت، والكاشف **بزاوية 90°**."),
          ("Particles ↑ → transmitted ↓ but scattered ↑.", "الجسيمات ↑ ← النافذ ↓ لكن المتشتّت ↑.")]),

 SEC("Common Sources of Error", "مصادر الخطأ الشائعة"),
 SIDE([L(["**Air bubbles** in the cuvette", "**Dirty or scratched** cuvette", "**Incorrect** sample or reagent **volume**", "**Poor mixing**",
          "Very **lipemic samples** may interfere with some assays", "Using the **wrong wavelength** or assay settings"],
         ["**فقاعات هواء** في الكيوفيت", "كيوفيت **متّسخ أو مخدوش**", "**حجم غير صحيح** للعيّنة أو الكاشف", "**مزج ضعيف**",
          "قد تتداخل **العيّنات الدهنية جدًا** مع بعض الفحوص", "استعمال **طول موجي خاطئ** أو إعدادات فحص خاطئة"])],
      "turbidity-standards.png", "Pure water cuvette and turbidity reference solutions", "كيوفيت ماء نقي ومحاليل العكارة المرجعية"),
 INSHORT([("Cuvette errors: **bubbles, dirt, scratches**.", "أخطاء الكيوفيت: **الفقاعات، والاتّساخ، والخدوش**."),
          ("Method errors: **wrong volume, poor mixing, wrong wavelength**.", "أخطاء الطريقة: **حجم خاطئ، ومزج ضعيف، وطول موجي خاطئ**."),
          ("Sample error: **very lipemic** sample.", "خطأ العيّنة: عيّنة **دهنية جدًا**.")]),

 SEC("Advantages", "المزايا"),
 L(["**Simple and fast**", "Can be **automated**", "Useful for **quantitative** measurements", "Suitable for **routine clinical laboratories**", "Can measure **several specific proteins**"],
   ["**بسيط وسريع**", "يمكن **أتمتته**", "مفيد في القياسات **الكمّية**", "مناسب **للمختبرات السريرية الروتينية**", "يمكنه قياس **عدّة بروتينات نوعية**"]),
 INSHORT([("**Simple, fast, automated, quantitative, routine.**", "**بسيط، وسريع، وآلي، وكمّي، وروتيني.**")]),

 SEC("Quick Summary", "خلاصة سريعة"),
 T([B("Term", "المصطلح"), B("Key idea", "الفكرة الأساسية")],
   [[B("**Turbidimetry**", "**قياس العكارة**"), B("Measures transmitted light through a cloudy sample. It does not directly measure scattered light.", "يقيس الضوء النافذ خلال عيّنة عكرة. ولا يقيس الضوء المتشتّت مباشرة.")],
    [B("**Immunoturbidimetry**", "**قياس العكارة المناعي**"), B("Uses antigen–antibody complexes to create turbidity.", "يستعمل معقّدات المستضد والضد لتكوين العكارة.")],
    [B("**Nephelometry**", "**قياس التشتّت**"), B("Measures scattered light, commonly at 90°.", "يقيس الضوء المتشتّت، غالبًا بزاوية 90°.")]],
   key_cols=[0], widths=[30, 70], style="summary", label_en="Quick summary", label_ar="خلاصة سريعة"),
 N("**More particles → more turbidity → less transmitted light.**", "**جسيمات أكثر ← عكارة أكثر ← ضوء نافذ أقل.**", label=["Remember", "تذكّر"]),
] + TERMS([
 ("Turbidimetry", "قياس العكارة / القياس العكري / التوربيديمتري"),
 ("Turbidity / Cloudiness", "العكارة / التعكّر / الغباشة"),
 ("Suspended particles", "جسيمات عالقة / دقائق معلّقة"),
 ("Transmitted light", "الضوء النافذ / الضوء المار / الضوء المنقول"),
 ("Scattered light", "الضوء المتشتّت / الضوء المبعثر"),
 ("Detector", "الكاشف / المتحسّس / المستقبِل"),
 ("Cuvette / Sample cell", "الكيوفيت / خلية العيّنة / أنبوب القياس"),
 ("Immunoturbidimetry", "قياس العكارة المناعي / التوربيديمتري المناعي"),
 ("Immune complex", "معقّد مناعي / مركّب مستضد–ضد"),
 ("Analyte", "المادة المقاسة / المادة المحلَّلة / المحلول المستهدف"),
 ("Nephelometry", "قياس التشتّت / قياس الكدرة / النفلومتري"),
 ("Spectrophotometer", "مطياف ضوئي / جهاز المطياف / السبكتروفوتوميتر"),
 ("Absorbance", "الامتصاص / الامتصاصية / الكثافة الضوئية"),
 ("Wavelength", "الطول الموجي / طول الموجة"),
 ("Lipemic sample", "عيّنة دهنية / مصل شحمي / عيّنة عكرة بالدهون"),
 ("C-reactive protein (CRP)", "البروتين المتفاعل C / بروتين سي التفاعلي"),
 ("Complement (C3, C4)", "المتمّمة / بروتينات المتمّم / الكومبلمنت"),
])

O = P
mcq = [
 {"topic_en": "Definition and principle", "topic_ar": "التعريف والمبدأ"},
 Q("Turbidimetry measures:", "يقيس قياس العكارة:", O(("The colour of a sample", "لون العيّنة"), ("The cloudiness of a liquid sample", "تعكّر العيّنة السائلة"), ("The pH of a sample", "الأس الهيدروجيني للعيّنة"), ("The temperature of a sample", "درجة حرارة العيّنة")), "b"),
 Q("Cloudiness of a sample is caused by:", "ينتج تعكّر العيّنة عن:", O(("Dissolved salts", "الأملاح الذائبة"), ("Water", "الماء"), ("Particles suspended in the sample", "جسيمات عالقة في العيّنة"), ("Light", "الضوء")), "c"),
 Q("In turbidimetry, the detector measures:", "في قياس العكارة يقيس الكاشف:", O(("Transmitted light", "الضوء النافذ"), ("Scattered light", "الضوء المتشتّت"), ("Emitted fluorescence", "الفلورة المنبعثة"), ("Radioactivity", "النشاط الإشعاعي")), "a"),
 Q("More turbidity means:", "العكارة الأكثر تعني:", O(("More transmitted light", "ضوءًا نافذًا أكثر"), ("No change in light", "لا تغيّر في الضوء"), ("More absorbed colour", "لونًا ممتصًا أكثر"), ("Less transmitted light", "ضوءًا نافذًا أقل")), "d"),
 Q("The correct order in the principle is:", "الترتيب الصحيح في المبدأ:", O(("Detector → sample → light source", "الكاشف ← العيّنة ← مصدر الضوء"), ("Light source → sample → transmitted light → detector", "مصدر الضوء ← العيّنة ← الضوء النافذ ← الكاشف"), ("Sample → light source → detector", "العيّنة ← مصدر الضوء ← الكاشف"), ("Light source → detector → sample", "مصدر الضوء ← الكاشف ← العيّنة")), "b"),
 Q("Suspended particles in the sample:", "الجسيمات العالقة في العيّنة:", O(("Increase the light that passes straight through", "تزيد الضوء النافذ بشكل مستقيم"), ("Have no effect on light", "ليس لها تأثير على الضوء"), ("Reduce the light that passes straight through", "تقلّل الضوء النافذ بشكل مستقيم"), ("Produce light", "تُنتج ضوءًا")), "c"),
 {"topic_en": "Immunoturbidimetry and applications", "topic_ar": "قياس العكارة المناعي والتطبيقات"},
 Q("In immunoturbidimetry, turbidity is produced by:", "في قياس العكارة المناعي تنتج العكارة عن:", O(("Immune complexes of antigen and antibody", "معقّدات مناعية من المستضد والضد"), ("Red blood cells", "الكريات الحمر"), ("Air bubbles", "فقاعات الهواء"), ("Lipids only", "الدهون فقط")), "a"),
 Q("The analyzer measures the change in turbidity to:", "يقيس المحلّل تغيّر العكارة من أجل:", O(("Count cells", "عدّ الخلايا"), ("Measure pH", "قياس الأس الهيدروجيني"), ("Identify bacteria", "تشخيص البكتيريا"), ("Estimate the amount of the analyte", "تقدير كمية المادة المقاسة")), "d"),
 Q("Which is a clinical application of turbidimetry?", "أي مما يأتي تطبيق سريري لقياس العكارة؟", O(("Blood film staining", "صبغ المسحة الدموية"), ("C-reactive protein (CRP)", "البروتين المتفاعل C"), ("Gram stain", "صبغة غرام"), ("Blood grouping", "تحديد فصيلة الدم")), "b"),
 Q("Complement proteins measured by turbidimetry include:", "من بروتينات المتمّمة التي تُقاس بالعكارة:", O(("C3 and C4", "C3 وC4"), ("IgE and IgD", "IgE وIgD"), ("Albumin and globulin", "الألبومين والغلوبولين"), ("Hb and MCV", "Hb وMCV")), "a"),
 Q("The immunoglobulins listed in the lecture are:", "الغلوبولينات المناعية المذكورة في المحاضرة:", O(("IgE only", "IgE فقط"), ("IgD and IgE", "IgD وIgE"), ("IgG, IgA, and IgM", "IgG وIgA وIgM"), ("None", "لا شيء")), "c"),
 {"topic_en": "Instrument, steps, errors", "topic_ar": "الجهاز والخطوات والأخطاء"},
 Q("Which is NOT listed as an instrument for turbidimetry?", "أي مما يأتي ليس من أجهزة قياس العكارة المذكورة؟", O(("Spectrophotometer", "المطياف الضوئي"), ("Automated chemistry analyzer", "المحلّل الكيميائي الآلي"), ("Turbidimetric analyzer", "محلّل العكارة"), ("Centrifuge", "جهاز الطرد المركزي")), "d"),
 Q("The sample is placed in the:", "توضع العيّنة في:", O(("Detector", "الكاشف"), ("Sample cell / cuvette", "خلية العيّنة / الكيوفيت"), ("Light source", "مصدر الضوء"), ("Display", "الشاشة")), "b"),
 Q("After mixing sample and reagent, the next step is:", "بعد مزج العيّنة والكاشف تكون الخطوة التالية:", O(("Record the result", "تسجيل النتيجة"), ("Measure immediately", "القياس مباشرة"), ("Allow the reaction to develop", "ترك التفاعل ليكتمل"), ("Discard the cuvette", "التخلّص من الكيوفيت")), "c"),
 Q("Which is a common source of error?", "أي مما يأتي من مصادر الخطأ الشائعة؟", O(("Air bubbles in the cuvette", "فقاعات هواء في الكيوفيت"), ("Clean cuvette", "كيوفيت نظيف"), ("Correct wavelength", "طول موجي صحيح"), ("Good mixing", "مزج جيد")), "a"),
 Q("Very lipemic samples:", "العيّنات الدهنية جدًا:", O(("Improve accuracy", "تحسّن الدقّة"), ("Have no effect", "ليس لها تأثير"), ("Are required for the test", "مطلوبة للفحص"), ("May interfere with some assays", "قد تتداخل مع بعض الفحوص")), "d"),
 Q("Which is an advantage of turbidimetry?", "أي مما يأتي من مزايا قياس العكارة؟", O(("Very slow", "بطيء جدًا"), ("Can be automated", "يمكن أتمتته"), ("Qualitative only", "نوعي فقط"), ("Measures one protein only", "يقيس بروتينًا واحدًا فقط")), "b"),
 {"topic_en": "Turbidimetry vs nephelometry", "topic_ar": "العكارة مقابل التشتّت"},
 Q("Nephelometry measures:", "يقيس قياس التشتّت:", O(("Transmitted light", "الضوء النافذ"), ("Absorbed colour", "اللون الممتص"), ("Scattered light", "الضوء المتشتّت"), ("Electrical current", "التيار الكهربائي")), "c"),
 Q("In nephelometry, the detector is commonly placed at:", "في قياس التشتّت يوضع الكاشف غالبًا بزاوية:", O(("90°", "90°"), ("0° behind the light source", "0° خلف مصدر الضوء"), ("45° only", "45° فقط"), ("In line with the light beam", "على خط الحزمة الضوئية")), "a"),
 Q("In turbidimetry, the detector is:", "في قياس العكارة يكون الكاشف:", O(("At 90°", "بزاوية 90°"), ("Above the sample", "فوق العيّنة"), ("Inside the light source", "داخل مصدر الضوء"), ("In line with the light beam", "على خط الحزمة الضوئية")), "d"),
 Q("In nephelometry, more particles give:", "في قياس التشتّت تعطي الجسيمات الأكثر:", O(("Less scattered light", "ضوءًا متشتّتًا أقل"), ("More scattered light", "ضوءًا متشتّتًا أكثر"), ("No light", "لا ضوء"), ("More transmitted light", "ضوءًا نافذًا أكثر")), "b"),
 {"topic_en": "Picture questions", "topic_ar": "أسئلة الصور"},
 Q("In this turbidimeter, the part that holds the sample is the:", "في جهاز قياس العكارة هذا، الجزء الذي يحمل العيّنة هو:", O(("Filter", "المرشّح"), ("Read out device", "جهاز عرض القراءة"), ("Sample cell", "خلية العيّنة"), ("Visible light", "الضوء المرئي")), "c", img="assets/turbidimeter-diagram.png", img_h="38mm"),
 Q("In the lower diagram (nephelometry), the detector reads:", "في المخطط السفلي (قياس التشتّت) يقرأ الكاشف:", O(("Scattered light", "الضوء المتشتّت"), ("Transmitted light", "الضوء النافذ"), ("Reflected colour", "اللون المنعكس"), ("Heat", "الحرارة")), "a", img="assets/turbid-vs-nephelo.png", img_h="38mm"),
 Q("The cuvettes in this picture show:", "تُظهر الكيوفيتات في هذه الصورة:", O(("Blood groups", "فصائل الدم"), ("Stained cells", "خلايا مصبوغة"), ("Different pH values", "قيم أس هيدروجيني مختلفة"), ("Pure water and turbidity reference solutions", "ماءً نقيًا ومحاليل عكارة مرجعية")), "d", img="assets/turbidity-standards.png", img_h="38mm"),
]
mcq = balance(mcq, 11)
tf = [
 TF("Turbidimetry measures the cloudiness of a liquid sample.", "يقيس قياس العكارة تعكّر العيّنة السائلة.", "T"),
 TF("In turbidimetry, more turbidity gives more transmitted light.", "في قياس العكارة تعطي العكارة الأكثر ضوءًا نافذًا أكثر.", "F"),
 TF("The detector in turbidimetry measures the transmitted light.", "يقيس الكاشف في قياس العكارة الضوء النافذ.", "T"),
 TF("Immune complexes make the sample less turbid.", "تجعل المعقّدات المناعية العيّنة أقل عكارة.", "F"),
 TF("CRP can be measured by turbidimetry.", "يمكن قياس CRP بقياس العكارة.", "T"),
 TF("Nephelometry measures transmitted light.", "يقيس قياس التشتّت الضوء النافذ.", "F"),
 TF("In nephelometry the detector is commonly at 90°.", "في قياس التشتّت يكون الكاشف غالبًا بزاوية 90°.", "T"),
 TF("A scratched cuvette is a source of error.", "الكيوفيت المخدوش مصدر من مصادر الخطأ.", "T"),
 TF("Turbidimetry cannot be automated.", "لا يمكن أتمتة قياس العكارة.", "F"),
 TF("Turbidimetry directly measures scattered light.", "يقيس قياس العكارة الضوء المتشتّت مباشرة.", "F"),
]
traps = [
 TR("Turbidimetry vs nephelometry", "العكارة مقابل التشتّت", "Turbidimetry: transmitted light, detector in line. Nephelometry: scattered light, detector at an angle (commonly 90°).", "العكارة: ضوء نافذ، والكاشف على الخط. التشتّت: ضوء متشتّت، والكاشف بزاوية (غالبًا 90°)."),
 TR("Turbidity and transmitted light", "العكارة والضوء النافذ", "They move in opposite directions: more turbidity → less transmitted light.", "يتحرّكان باتجاهين متعاكسين: عكارة أكثر ← ضوء نافذ أقل."),
 TR("Particles in nephelometry", "الجسيمات في قياس التشتّت", "More particles → MORE scattered light (not less).", "جسيمات أكثر ← ضوء متشتّت أكثر (وليس أقل)."),
 TR("Turbidimetry vs immunoturbidimetry", "العكارة مقابل العكارة المناعية", "Immunoturbidimetry is turbidimetry where the turbidity comes from antigen–antibody complexes.", "العكارة المناعية هي قياس عكارة تنتج فيه العكارة عن معقّدات المستضد والضد."),
 TR("Reaction time", "زمن التفاعل", "Do not measure right after mixing: allow the reaction to develop first.", "لا تقِس مباشرة بعد المزج: اترك التفاعل ليكتمل أولًا."),
]
important = [
 IM("Define turbidimetry and state what causes turbidity.", "عرّف قياس العكارة، وما سبب العكارة؟", "Turbidimetry measures the cloudiness of a liquid sample; cloudiness is caused by particles suspended in the sample.", "يقيس قياس العكارة تعكّر العيّنة السائلة، وينتج التعكّر عن جسيمات عالقة في العيّنة."),
 IM("Explain the principle of turbidimetry.", "اشرح مبدأ قياس العكارة.", "A beam of light passes through the sample; suspended particles reduce the light passing straight through; the detector measures the transmitted light; more turbidity → less transmitted light.", "تمرّ حزمة ضوئية خلال العيّنة، فتقلّل الجسيمات العالقة الضوء النافذ المستقيم، ويقيس الكاشف الضوء النافذ؛ عكارة أكثر ← ضوء نافذ أقل."),
 IM("How does immunoturbidimetry work?", "كيف يعمل قياس العكارة المناعي؟", "Antigen + specific antibody → small immune complexes → turbidity increases → the analyzer measures the change to estimate the analyte.", "مستضد + ضد نوعي ← معقّدات مناعية صغيرة ← تزداد العكارة ← يقيس المحلّل التغيّر لتقدير المادة المقاسة."),
 IM("List the clinical applications of turbidimetry.", "عدّد التطبيقات السريرية لقياس العكارة.", "CRP; immunoglobulins IgG, IgA, IgM; complement C3 and C4; transferrin and other specific proteins; some urine protein measurements.", "CRP؛ الغلوبولينات المناعية IgG وIgA وIgM؛ المتمّمة C3 وC4؛ الترانسفيرين وبروتينات نوعية أخرى؛ بعض قياسات بروتين الإدرار."),
 IM("Compare turbidimetry with nephelometry.", "قارن بين قياس العكارة وقياس التشتّت.", "Turbidimetry: transmitted light, detector in line, more turbidity → less transmitted light. Nephelometry: scattered light, detector at an angle (commonly 90°), more particles → more scattered light.", "العكارة: ضوء نافذ، والكاشف على الخط، وعكارة أكثر ← ضوء نافذ أقل. التشتّت: ضوء متشتّت، والكاشف بزاوية (غالبًا 90°)، وجسيمات أكثر ← ضوء متشتّت أكثر."),
 IM("List the common sources of error in turbidimetry.", "عدّد مصادر الخطأ الشائعة في قياس العكارة.", "Air bubbles; dirty or scratched cuvette; incorrect sample or reagent volume; poor mixing; very lipemic samples; wrong wavelength or assay settings.", "فقاعات الهواء؛ كيوفيت متّسخ أو مخدوش؛ حجم غير صحيح للعيّنة أو الكاشف؛ مزج ضعيف؛ عيّنات دهنية جدًا؛ طول موجي أو إعدادات خاطئة."),
]
meta = dict(HEM, unit_en="Lab 4", unit_ar="العملي 4", unit_no="4", title_en="Turbidimetry", title_ar="قياس العكارة")
save("hematology-practical-turbidimetry", meta, blocks, mcq, tf, traps, important)

```
