---
source: BIOS-Obsidian/tools/scripts/n4/make.py
handouts: [advtech-lec1-elisa]
saved: 2026-10-29
tags: [bios, code]
---
# n4/make.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#advtech-lec1-elisa|advtech-lec1-elisa]]

```python
import json
from collections import Counter
def C(en, ar, **k): return dict(t="card", en=en, ar=ar, **k)
def R(en, ar): return dict(t="rule", en=en, ar=ar)
def SEC(en, ar): return dict(t="section", en=en, ar=ar)
def H2(en, ar): return dict(t="h2", en=en, ar=ar)
def G(te, ta, en, ar, **k): return dict(t="group", title_en=te, title_ar=ta, en=en, ar=ar, **k)
def L(en_items, ar_items, en="", ar="", **k): return dict(t="card", en=en, ar=ar, list_en=en_items, list_ar=ar_items, **k)
def N(en, ar, label=None):
    b = dict(t="note", en=en, ar=ar)
    if label: b["label"] = label
    return b

blocks = [
 SEC("1. Introduction", "1. المقدمة"),
 G("Definition", "التعريف",
   "**ELISA**, or **Enzyme-Linked Immunosorbent Assay**, is an **immunological technique** used to **detect and quantify antigens** (proteins, peptides, hormones, etc.) **or antibodies** in a sample.",
   "**الإليزا** (`ELISA`)، أي **المقايسة الامتصاصية المناعية المرتبطة بالإنزيم**، هي **تقنية مناعية** تُستخدم **للكشف عن المستضدات** (البروتينات، الببتيدات، الهرمونات، إلخ) **أو الأجسام المضادة وقياس كمّيتها** في العيّنة."),
 L(["Developed in the **early 1970s** as a safer alternative to **radioimmunoassay (RIA)**.",
    "Uses **enzymes instead of radioactive labels** to generate measurable signals."],
   ["طُوّرت في **أوائل السبعينيات** بديلًا أكثر أمانًا من **المقايسة المناعية الإشعاعية** (`RIA`).",
    "تستخدم **الإنزيمات بدلًا من الواسمات المشعّة** لتوليد إشارات قابلة للقياس."],
   en="**Historical Background**", ar="**الخلفية التاريخية**"),
 L(["**Antigen–antibody specificity**", "**Enzyme-mediated signal amplification**"],
   ["**تخصّص المستضد–الجسم المضاد**", "**تضخيم الإشارة بواسطة الإنزيم**"],
   en="**Basic Principle** — ELISA works on the principle of:", ar="**المبدأ الأساسي** — تعمل الإليزا على مبدأ:"),
 C("When an **enzyme-linked antibody** binds its antigen, a **substrate** is added that the enzyme converts into a **colored product**, measurable by **spectrophotometry**.",
   "عندما يرتبط **الجسم المضاد المرتبط بالإنزيم** بمستضده، تُضاف **مادة أساس (ركيزة)** يحوّلها الإنزيم إلى **ناتج ملوّن** يمكن قياسه بـ**المطيافية الضوئية**."),

 SEC("2. Key Components", "2. المكوّنات الرئيسة"),
 dict(t="table", head=["Component", "Function.", "المكوّن ووظيفته"], ar_cols=[2], key_cols=[0], widths=["44mm", "", ""],
      rows=[["Antigen or antibody", "the molecule being detected or used for capture", "**المستضد أو الجسم المضاد**: الجزيء المراد كشفه أو المستخدم للاصطياد (الالتقاط)"],
            ["Solid phase (microtiter plate)", "Provides a surface for immobilization", "**الطور الصلب (صفيحة المعايرة الدقيقة)**: يوفّر سطحًا للتثبيت"],
            ["Enzyme-labeled antibody", "Enables detection via enzyme reaction", "**الجسم المضاد الموسوم بالإنزيم**: يتيح الكشف عبر التفاعل الإنزيمي"],
            ["Substrate (chromogenic)", "Produces measurable color change", "**الركيزة (المولّدة للون)**: تُحدث تغيّرًا لونيًا قابلًا للقياس"],
            ["Detector (spectrophotometer/plate reader)", "Measures absorbance at a specific wavelength", "**الكاشف (مقياس الطيف الضوئي/قارئ الصفائح)**: يقيس الامتصاص عند طول موجي محدّد"]]),
 L(["**Horseradish peroxidase (HRP)**", "**Alkaline phosphatase (AP)**"], ["**بيروكسيديز الفجل الحار** (`HRP`)", "**الفوسفاتيز القاعدي** (`AP`)"],
   en="**Common enzymes used:**", ar="**الإنزيمات الشائعة الاستخدام:**"),
 L(["**TMB** (3,3′,5,5′-Tetramethylbenzidine) for **HRP** (blue → yellow to acid stop)", "**pNPP** (para-nitrophenyl phosphate) for **AP** (yellow product)"],
   ["**`TMB`** (رباعي ميثيل البنزيدين) لإنزيم **`HRP`** (أزرق ← أصفر عند الإيقاف بالحامض)", "**`pNPP`** (بارا-نايتروفينيل فوسفات) لإنزيم **`AP`** (ناتج أصفر)"],
   en="**Common substrates:**", ar="**الركائز الشائعة:**"),

 SEC("3. Types of ELISA", "3. أنواع الإليزا"),
 dict(t="figure", src="assets/elisa-types.svg", en="The four types of ELISA (diagram drawn for this handout from the lecture text)", ar="أنواع الإليزا الأربعة (مخطّط رُسم لهذه الملزمة من نص المحاضرة)", width="100%", keep=True),
 L(["Antigen is immobilized on plate.", "Enzyme-labeled antibody binds **directly** to antigen.", "**Simple but less sensitive.**", "**Applications:** detecting **high antigen concentrations**."],
   ["يُثبَّت المستضد على الصفيحة.", "يرتبط الجسم المضاد الموسوم بالإنزيم **مباشرةً** بالمستضد.", "**بسيطة لكنها أقل حساسية.**", "**التطبيقات:** الكشف عن **التراكيز العالية من المستضد**."], en="**a) Direct ELISA**", ar="**أ) الإليزا المباشرة**"),
 L(["Antigen immobilized.", "**Primary antibody** binds antigen.", "Enzyme-linked **secondary antibody** binds to primary antibody.", "**Higher sensitivity and flexibility.**",
    "**Applications:** detecting **antibodies in serum** (e.g., HIV, Hepatitis B tests)."],
   ["يُثبَّت المستضد.", "يرتبط **الجسم المضاد الأولي** بالمستضد.", "يرتبط **الجسم المضاد الثانوي** المرتبط بالإنزيم بالجسم المضاد الأولي.", "**حساسية ومرونة أعلى.**",
    "**التطبيقات:** الكشف عن **الأجسام المضادة في المصل** (مثل فحوص `HIV` والتهاب الكبد `B`)."], en="**b) Indirect ELISA**", ar="**ب) الإليزا غير المباشرة**"),
 L(["**Capture antibody** immobilized.", "Sample antigen binds.", "Second enzyme-linked antibody (**detection antibody**) binds to antigen.", "**Highly specific and sensitive.**",
    "**Applications:** cytokine quantification, diagnostic kits (e.g., COVID-19 antigen tests)."],
   ["يُثبَّت **الجسم المضاد الملتقِط** (`capture antibody`).", "يرتبط مستضد العيّنة.", "يرتبط جسم مضاد ثانٍ مرتبط بالإنزيم (**الجسم المضاد الكاشف**) بالمستضد.", "**عالية التخصّص والحساسية.**",
    "**التطبيقات:** قياس كمّية السيتوكينات، وعُدد التشخيص (مثل فحوص مستضد `COVID-19`)."], en="**c) Sandwich ELISA**", ar="**ج) إليزا الساندويتش**"),
 L(["Sample antigen **competes with labeled antigen** for limited antibody binding sites.", "Signal **inversely proportional** to antigen concentration.",
    "Useful for **small antigens** (e.g., hormones, drugs)."],
   ["يتنافس مستضد العيّنة **مع المستضد الموسوم** على عدد محدود من مواقع الارتباط في الجسم المضاد.", "تتناسب الإشارة **تناسبًا عكسيًا** مع تركيز المستضد.",
    "مفيدة لـ**المستضدات الصغيرة** (مثل الهرمونات والأدوية)."], en="**d) Competitive ELISA**", ar="**د) الإليزا التنافسية**"),

 SEC("4. ELISA Procedure (General Steps)", "4. خطوات الإليزا (الخطوات العامة)"),
 R("**Coating:** Immobilize antigen or antibody on microplate.", "**التغليف (الطلاء):** تثبيت المستضد أو الجسم المضاد على الصفيحة الدقيقة."),
 R("**Blocking:** Add a blocking buffer (e.g., BSA, casein) to prevent nonspecific binding.", "**الحجب:** إضافة محلول حجب (مثل `BSA` أو الكازين) لمنع الارتباط غير النوعي."),
 R("**Sample Incubation:** Add sample containing target antigen or antibody.", "**حضن العيّنة:** إضافة العيّنة التي تحتوي على المستضد أو الجسم المضاد المستهدف."),
 R("**Detection:** Add enzyme-linked antibody.", "**الكشف:** إضافة الجسم المضاد المرتبط بالإنزيم."),
 R("**Substrate Reaction:** Add substrate → enzyme converts to colored product.", "**تفاعل الركيزة:** إضافة الركيزة ← يحوّلها الإنزيم إلى ناتج ملوّن."),
 R("**Measurement:** Read absorbance using an ELISA reader (usually at **450 nm**).", "**القياس:** قراءة الامتصاص بجهاز قارئ الإليزا (عادةً عند **450 نانومتر**)."),
 dict(t="flow", steps=[{"en": "Coating", "ar": "التغليف"}, {"en": "Blocking", "ar": "الحجب"}, {"en": "Sample", "ar": "العيّنة"},
                       {"en": "Detection", "ar": "الكشف"}, {"en": "Substrate", "ar": "الركيزة"}, {"en": "Measurement", "ar": "القياس"}]),

 SEC("5. Data Analysis", "5. تحليل البيانات"),
 L(["Construct a **standard curve** using known concentrations.", "Measure **optical density (OD)** of unknowns.",
    "Determine concentrations by **comparing OD values to the standard curve**."],
   ["إنشاء **منحنى قياسي** باستخدام تراكيز معلومة.", "قياس **الكثافة الضوئية** (`OD`) للعيّنات المجهولة.",
    "تحديد التراكيز **بمقارنة قيم `OD` بالمنحنى القياسي**."]),

 SEC("6. Applications of ELISA", "6. تطبيقات الإليزا"),
 dict(t="table", head=["Field", "Examples", "المجال والأمثلة"], ar_cols=[2], key_cols=[0], widths=["34mm", "", ""],
      rows=[["Clinical diagnostics", "Detection of HIV, Hepatitis, COVID-19, hormones (HCG, insulin)", "**التشخيص السريري**: كشف `HIV` والتهاب الكبد و`COVID-19` والهرمونات (`HCG`، الإنسولين)"],
            ["Food industry", "Allergen detection, GMO monitoring", "**الصناعات الغذائية**: كشف مسبّبات الحساسية، ومراقبة الكائنات المعدّلة وراثيًا (`GMO`)"],
            ["Pharmaceuticals", "Drug screening, vaccine development", "**الصناعات الدوائية**: تحرّي الأدوية، وتطوير اللقاحات"],
            ["Research", "Quantification of cytokines, antibodies, or signaling molecules", "**البحث العلمي**: قياس كمّية السيتوكينات أو الأجسام المضادة أو جزيئات الإشارة"]]),

 SEC("7. Advantages", "7. المزايا"),
 L(["High sensitivity and specificity", "Quantitative results", "Cost-effective and scalable", "Compatible with large sample numbers"],
   ["حساسية وتخصّص عاليان", "نتائج كمّية", "قليلة الكلفة وقابلة للتوسّع", "تلائم الأعداد الكبيرة من العيّنات"]),
 SEC("8. Limitations", "8. القيود"),
 L(["Requires careful optimization (blocking, washing, incubation times)", "Risk of false positives/negatives",
    "Only semi-quantitative without precise standard curves", "Enzyme/substrate instability"],
   ["تتطلّب ضبطًا دقيقًا (الحجب، الغسل، أوقات الحضن)", "خطر النتائج الموجبة/السالبة الكاذبة",
    "شبه كمّية فقط من دون منحنيات قياسية دقيقة", "عدم ثبات الإنزيم/الركيزة"]),
 SEC("9. Recent Advances", "9. التطوّرات الحديثة"),
 L(["**Multiplex ELISA** (detects multiple analytes in one assay)", "**Electrochemical ELISA** (faster and more sensitive)",
    "**Portable ELISA kits** (for field diagnostics)", "**Automation** using robotic liquid handlers"],
   ["**الإليزا المتعدّدة** (تكشف عدة مواد في فحص واحد)", "**الإليزا الكهروكيميائية** (أسرع وأكثر حساسية)",
    "**عُدد الإليزا المحمولة** (للتشخيص الميداني)", "**الأتمتة** باستخدام أجهزة روبوتية لمناولة السوائل"]),

 SEC("10. Conclusion", "10. الخاتمة"),
 C(["ELISA remains a **cornerstone of immunodiagnostics**, offering a balance of **accuracy, sensitivity, and practicality**.",
    "From infectious disease detection to research applications, it continues to evolve with technology — now integrating **microfluidics and nanotechnology** for rapid, **point-of-care testing**."],
   ["تبقى الإليزا **حجر الأساس في التشخيص المناعي**، إذ توفّر توازنًا بين **الدقة والحساسية والعملية**.",
    "ومن الكشف عن الأمراض المعدية إلى التطبيقات البحثية، تستمر في التطوّر مع التقنية — وهي الآن تدمج **الموائع الدقيقة وتقنية النانو** لإجراء **فحوص سريعة بجانب المريض**."]),
]

def Q(en, ar, opts, ans, **k):
    return dict(en=en, ar=ar, options=[list(o) for o in opts], answer=ans, **k)

mcq = [
 {"topic_en": "Principle and components", "topic_ar": "المبدأ والمكوّنات"},
 Q("ELISA stands for:", "الإليزا (ELISA) اختصار لـ:", [("Enzyme-Linked Immunosorbent Assay", "المقايسة الامتصاصية المناعية المرتبطة بالإنزيم"), ("Electro-Linked Immune Serum Assay", "مقايسة المصل المناعي الكهربائية"), ("Enzyme-Labeled Isotope Assay", "مقايسة النظير الموسوم بالإنزيم"), ("Endogenous Lipid Immune Assay", "مقايسة الدهون المناعية الداخلية")], "a"),
 Q("ELISA was developed in the early 1970s as a safer alternative to:", "طُوّرت الإليزا في أوائل السبعينيات بديلًا أكثر أمانًا من:", [("PCR", "PCR"), ("Radioimmunoassay (RIA)", "المقايسة المناعية الإشعاعية (RIA)"), ("Western blot", "اللطخة الغربية"), ("Flow cytometry", "قياس التدفّق الخلوي")], "b"),
 Q("ELISA uses which label to generate a measurable signal?", "ما الواسم الذي تستخدمه الإليزا لتوليد إشارة قابلة للقياس؟", [("Radioactive isotopes", "النظائر المشعّة"), ("Fluorescent dyes only", "الأصباغ المتألّقة فقط"), ("Enzymes", "الإنزيمات"), ("Gold particles", "جسيمات الذهب")], "c"),
 Q("ELISA works on the principle of antigen–antibody specificity and:", "تعمل الإليزا على مبدأ تخصّص المستضد–الجسم المضاد و:", [("Gene amplification", "تضخيم الجينات"), ("Enzyme-mediated signal amplification", "تضخيم الإشارة بواسطة الإنزيم"), ("Radioactive decay", "التحلّل الإشعاعي"), ("Cell lysis", "تحلّل الخلايا")], "b"),
 Q("The colored product in ELISA is measured by:", "يُقاس الناتج الملوّن في الإليزا بـ:", [("Microscopy", "المجهر"), ("Centrifugation", "الطرد المركزي"), ("Electrophoresis", "الترحيل الكهربائي"), ("Spectrophotometry", "المطيافية الضوئية")], "d"),
 Q("The microtiter plate in ELISA is the:", "صفيحة المعايرة الدقيقة في الإليزا هي:", [("Solid phase providing a surface for immobilization", "الطور الصلب الذي يوفّر سطحًا للتثبيت"), ("Substrate", "الركيزة"), ("Detector", "الكاشف"), ("Blocking buffer", "محلول الحجب")], "a"),
 Q("Which enzymes are commonly used in ELISA?", "ما الإنزيمات الشائعة الاستخدام في الإليزا؟", [("Trypsin and pepsin", "التربسين والببسين"), ("HRP and alkaline phosphatase", "HRP والفوسفاتيز القاعدي"), ("Amylase and lipase", "الأميليز واللايبيز"), ("DNA polymerase", "بوليميريز الـ DNA")], "b"),
 Q("TMB is the substrate for:", "TMB ركيزة لإنزيم:", [("AP", "AP"), ("Urease", "اليوريز"), ("HRP", "HRP"), ("Lactate dehydrogenase", "لاكتيت ديهيدروجينيز")], "c"),
 Q("With HRP, TMB gives a blue color that turns ____ after acid stop:", "مع HRP يعطي TMB لونًا أزرق يتحوّل إلى ____ بعد الإيقاف بالحامض:", [("Red", "الأحمر"), ("Green", "الأخضر"), ("Colorless", "عديم اللون"), ("Yellow", "الأصفر")], "d"),
 Q("pNPP is the substrate for alkaline phosphatase and gives a:", "pNPP ركيزة للفوسفاتيز القاعدي ويعطي ناتجًا:", [("Yellow product", "أصفر"), ("Blue product", "أزرق"), ("Red product", "أحمر"), ("Green product", "أخضر")], "a"),
 {"topic_en": "Types of ELISA", "topic_ar": "أنواع الإليزا"},
 Q("In direct ELISA, the enzyme-labeled antibody binds:", "في الإليزا المباشرة يرتبط الجسم المضاد الموسوم بالإنزيم بـ:", [("A secondary antibody", "جسم مضاد ثانوي"), ("Directly to the antigen", "المستضد مباشرة"), ("A capture antibody", "جسم مضاد ملتقِط"), ("The blocking buffer", "محلول الحجب")], "b"),
 Q("Direct ELISA is:", "الإليزا المباشرة:", [("Simple but less sensitive", "بسيطة لكنها أقل حساسية"), ("The most sensitive type", "أكثر الأنواع حساسية"), ("Used for small antigens", "تُستخدم للمستضدات الصغيرة"), ("Signal inversely proportional", "إشارتها عكسية التناسب")], "a"),
 Q("Detecting antibodies in serum (e.g., HIV, hepatitis B) is an application of:", "الكشف عن الأجسام المضادة في المصل (مثل HIV والتهاب الكبد B) تطبيق لـ:", [("Direct ELISA", "الإليزا المباشرة"), ("Competitive ELISA", "الإليزا التنافسية"), ("Indirect ELISA", "الإليزا غير المباشرة"), ("None", "لا شيء")], "c"),
 Q("In indirect ELISA, the enzyme is linked to the:", "في الإليزا غير المباشرة يرتبط الإنزيم بـ:", [("Antigen", "المستضد"), ("Primary antibody", "الجسم المضاد الأولي"), ("Plate", "الصفيحة"), ("Secondary antibody", "الجسم المضاد الثانوي")], "d"),
 Q("In sandwich ELISA, the antibody immobilized on the plate is the:", "في إليزا الساندويتش، الجسم المضاد المثبّت على الصفيحة هو:", [("Capture antibody", "الجسم المضاد الملتقِط"), ("Detection antibody", "الجسم المضاد الكاشف"), ("Secondary antibody", "الجسم المضاد الثانوي"), ("Labeled antigen", "المستضد الموسوم")], "a"),
 Q("COVID-19 antigen diagnostic kits and cytokine quantification use:", "عُدد تشخيص مستضد COVID-19 وقياس السيتوكينات تستخدم:", [("Direct ELISA", "الإليزا المباشرة"), ("Sandwich ELISA", "إليزا الساندويتش"), ("Competitive ELISA", "الإليزا التنافسية"), ("RIA", "RIA")], "b"),
 Q("In competitive ELISA, the signal is:", "في الإليزا التنافسية تكون الإشارة:", [("Directly proportional to antigen concentration", "متناسبة طرديًا مع تركيز المستضد"), ("Independent of antigen", "مستقلة عن المستضد"), ("Inversely proportional to antigen concentration", "متناسبة عكسيًا مع تركيز المستضد"), ("Always zero", "صفرًا دائمًا")], "c"),
 Q("Competitive ELISA is useful for:", "الإليزا التنافسية مفيدة لـ:", [("Large viruses", "الفيروسات الكبيرة"), ("Whole cells", "الخلايا الكاملة"), ("High antigen concentrations", "التراكيز العالية من المستضد"), ("Small antigens (hormones, drugs)", "المستضدات الصغيرة (الهرمونات، الأدوية)")], "d"),
 {"topic_en": "Procedure and data", "topic_ar": "الخطوات والبيانات"},
 Q("The first step of the ELISA procedure is:", "الخطوة الأولى في الإليزا هي:", [("Coating", "التغليف"), ("Blocking", "الحجب"), ("Detection", "الكشف"), ("Measurement", "القياس")], "a"),
 Q("The blocking step uses BSA or casein to:", "تستخدم خطوة الحجب BSA أو الكازين لـ:", [("Produce color", "إنتاج اللون"), ("Prevent nonspecific binding", "منع الارتباط غير النوعي"), ("Stop the reaction", "إيقاف التفاعل"), ("Measure absorbance", "قياس الامتصاص")], "b"),
 Q("ELISA absorbance is usually read at:", "يُقرأ امتصاص الإليزا عادةً عند:", [("260 nm", "260 نانومتر"), ("340 nm", "340 نانومتر"), ("450 nm", "450 نانومتر"), ("600 nm", "600 نانومتر")], "c"),
 Q("Concentrations of unknowns are determined by comparing their OD with:", "تُحدَّد تراكيز العيّنات المجهولة بمقارنة OD بـ:", [("The blank only", "الفراغ فقط"), ("The substrate", "الركيزة"), ("The wavelength", "الطول الموجي"), ("A standard curve", "المنحنى القياسي")], "d"),
 {"topic_en": "Applications, advantages and limitations", "topic_ar": "التطبيقات والمزايا والقيود"},
 Q("Allergen detection and GMO monitoring are ELISA applications in:", "كشف مسبّبات الحساسية ومراقبة GMO من تطبيقات الإليزا في:", [("Clinical diagnostics", "التشخيص السريري"), ("Food industry", "الصناعات الغذائية"), ("Pharmaceuticals", "الصناعات الدوائية"), ("Research", "البحث")], "b"),
 Q("Which is NOT an advantage of ELISA?", "أي مما يأتي ليس من مزايا الإليزا؟", [("High sensitivity and specificity", "حساسية وتخصّص عاليان"), ("Quantitative results", "نتائج كمّية"), ("Enzyme/substrate instability", "عدم ثبات الإنزيم/الركيزة"), ("Compatible with large sample numbers", "تلائم الأعداد الكبيرة من العيّنات")], "c"),
 Q("Without precise standard curves, ELISA is:", "من دون منحنيات قياسية دقيقة تكون الإليزا:", [("Fully quantitative", "كمّية بالكامل"), ("Only semi-quantitative", "شبه كمّية فقط"), ("Qualitative only for antibodies", "نوعية فقط للأجسام المضادة"), ("Not usable", "غير قابلة للاستخدام")], "b"),
 Q("ELISA that detects multiple analytes in one assay is:", "الإليزا التي تكشف عدة مواد في فحص واحد هي:", [("Electrochemical ELISA", "الإليزا الكهروكيميائية"), ("Portable ELISA", "الإليزا المحمولة"), ("Direct ELISA", "الإليزا المباشرة"), ("Multiplex ELISA", "الإليزا المتعدّدة")], "d"),
 Q("ELISA is now integrating microfluidics and nanotechnology for:", "تدمج الإليزا الآن الموائع الدقيقة وتقنية النانو من أجل:", [("Rapid point-of-care testing", "فحوص سريعة بجانب المريض"), ("Radioactive labeling", "الوسم الإشعاعي"), ("DNA sequencing", "تحديد تسلسل DNA"), ("Blood transfusion", "نقل الدم")], "a"),
 {"topic_en": "Picture questions", "topic_ar": "أسئلة الصور"},
 Q("Which type of ELISA is shown (antigen on the plate, enzyme-labeled antibody bound directly)?", "أي نوع من الإليزا في الشكل (المستضد على الصفيحة، والجسم المضاد الموسوم مرتبط به مباشرة)؟", [("Indirect", "غير المباشرة"), ("Direct", "المباشرة"), ("Sandwich", "الساندويتش"), ("Competitive", "التنافسية")], "b", img="assets/elisa-direct.svg", img_h="30mm"),
 Q("Which type of ELISA is shown (antigen between a capture antibody and a detection antibody)?", "أي نوع من الإليزا في الشكل (المستضد بين جسم مضاد ملتقِط وجسم مضاد كاشف)؟", [("Direct", "المباشرة"), ("Indirect", "غير المباشرة"), ("Sandwich", "الساندويتش"), ("Competitive", "التنافسية")], "c", img="assets/elisa-sandwich.svg", img_h="30mm"),
 Q("Which type of ELISA is shown (primary antibody on the antigen, enzyme-linked secondary antibody on top)?", "أي نوع من الإليزا في الشكل (جسم مضاد أولي على المستضد، وفوقه جسم مضاد ثانوي مرتبط بالإنزيم)؟", [("Indirect", "غير المباشرة"), ("Direct", "المباشرة"), ("Competitive", "التنافسية"), ("Sandwich", "الساندويتش")], "a", img="assets/elisa-indirect.svg", img_h="30mm"),
 Q("In this type (sample antigen and labeled antigen compete for antibody sites), a HIGH antigen concentration gives:", "في هذا النوع (يتنافس مستضد العيّنة والمستضد الموسوم على مواقع الجسم المضاد)، التركيز العالي للمستضد يعطي:", [("A high signal", "إشارة عالية"), ("No change", "لا تغيير"), ("A blue color only", "لونًا أزرق فقط"), ("A low signal", "إشارة منخفضة")], "d", img="assets/elisa-competitive.svg", img_h="30mm"),
]

tf = [
 dict(en="ELISA can detect and quantify both antigens and antibodies.", ar="يمكن للإليزا الكشف عن المستضدات والأجسام المضادة وقياس كمّيتها.", answer="T"),
 dict(en="ELISA uses radioactive labels to generate signals.", ar="تستخدم الإليزا واسمات مشعّة لتوليد الإشارات.", answer="F"),
 dict(en="The substrate is converted by the enzyme into a colored product.", ar="يحوّل الإنزيم الركيزة إلى ناتج ملوّن.", answer="T"),
 dict(en="pNPP is the substrate of HRP.", ar="pNPP ركيزة لإنزيم HRP.", answer="F"),
 dict(en="Direct ELISA is more sensitive than indirect ELISA.", ar="الإليزا المباشرة أكثر حساسية من غير المباشرة.", answer="F"),
 dict(en="In indirect ELISA a secondary enzyme-linked antibody binds the primary antibody.", ar="في الإليزا غير المباشرة يرتبط جسم مضاد ثانوي مرتبط بالإنزيم بالجسم المضاد الأولي.", answer="T"),
 dict(en="Sandwich ELISA is highly specific and sensitive.", ar="إليزا الساندويتش عالية التخصّص والحساسية.", answer="T"),
 dict(en="In competitive ELISA the signal increases as antigen concentration increases.", ar="في الإليزا التنافسية تزداد الإشارة بزيادة تركيز المستضد.", answer="F"),
 dict(en="Blocking prevents nonspecific binding.", ar="يمنع الحجبُ الارتباطَ غير النوعي.", answer="T"),
 dict(en="ELISA absorbance is usually measured at 450 nm.", ar="يُقاس امتصاص الإليزا عادةً عند 450 نانومتر.", answer="T"),
 dict(en="A standard curve is constructed using unknown concentrations.", ar="يُنشأ المنحنى القياسي باستخدام تراكيز مجهولة.", answer="F"),
 dict(en="ELISA is cost-effective and compatible with large sample numbers.", ar="الإليزا قليلة الكلفة وتلائم الأعداد الكبيرة من العيّنات.", answer="T"),
 dict(en="ELISA has no risk of false positive or false negative results.", ar="لا يوجد في الإليزا خطر نتائج موجبة أو سالبة كاذبة.", answer="F"),
 dict(en="Electrochemical ELISA is faster and more sensitive.", ar="الإليزا الكهروكيميائية أسرع وأكثر حساسية.", answer="T"),
]

traps = [
 dict(en="Which substrate goes with which enzyme?", ar="أي ركيزة لأي إنزيم؟", answer_en="TMB → HRP (blue, yellow after acid stop). pNPP → AP (yellow product).", answer_ar="TMB ← HRP (أزرق، ثم أصفر بعد الإيقاف بالحامض). pNPP ← AP (ناتج أصفر)."),
 dict(en="Direct vs indirect ELISA", ar="الإليزا المباشرة مقابل غير المباشرة", answer_en="Direct: one enzyme-labeled antibody on the antigen — simple, less sensitive. Indirect: primary antibody + enzyme-linked secondary — more sensitive; detects serum antibodies.", answer_ar="المباشرة: جسم مضاد واحد موسوم على المستضد — بسيطة وأقل حساسية. غير المباشرة: أولي + ثانوي مرتبط بالإنزيم — أكثر حساسية؛ تكشف أجسام المصل المضادة."),
 dict(en="What is immobilized first in sandwich ELISA?", ar="ما الذي يُثبَّت أولًا في إليزا الساندويتش؟", answer_en="The capture antibody — not the antigen. The antigen is held between the capture and the detection antibody.", answer_ar="الجسم المضاد الملتقِط — لا المستضد. ويُحصر المستضد بين الملتقِط والكاشف."),
 dict(en="Signal in competitive ELISA", ar="الإشارة في الإليزا التنافسية", answer_en="Inversely proportional to antigen: more sample antigen → less labeled antigen bound → lower signal.", answer_ar="عكسية التناسب مع المستضد: مستضد عيّنة أكثر ← ارتباط أقل للمستضد الموسوم ← إشارة أقل."),
 dict(en="Purpose of blocking", ar="الغرض من الحجب", answer_en="To prevent nonspecific binding (BSA, casein) — it does not stop the color reaction.", answer_ar="منع الارتباط غير النوعي (BSA، الكازين) — وليس إيقاف التفاعل اللوني."),
 dict(en="Quantitative or semi-quantitative?", ar="كمّية أم شبه كمّية؟", answer_en="Quantitative with a precise standard curve; only semi-quantitative without one.", answer_ar="كمّية مع منحنى قياسي دقيق؛ وشبه كمّية فقط من دونه."),
]

important = [
 dict(en="Define ELISA and state its basic principle.", ar="عرّف الإليزا واذكر مبدأها الأساسي.", answer_en="An immunological technique to detect and quantify antigens or antibodies in a sample. Principle: antigen–antibody specificity and enzyme-mediated signal amplification — the enzyme-linked antibody binds its antigen and converts an added substrate into a colored product measured by spectrophotometry.", answer_ar="تقنية مناعية للكشف عن المستضدات أو الأجسام المضادة وقياس كمّيتها. المبدأ: تخصّص المستضد–الجسم المضاد وتضخيم الإشارة بالإنزيم — يرتبط الجسم المضاد المرتبط بالإنزيم بمستضده ويحوّل الركيزة إلى ناتج ملوّن يُقاس بالمطيافية."),
 dict(en="List the key components of ELISA and their functions.", ar="عدّد المكوّنات الرئيسة للإليزا ووظائفها.", answer_en="Antigen/antibody (detected or capture); solid phase microtiter plate (immobilization); enzyme-labeled antibody (detection); chromogenic substrate (color change); detector/plate reader (absorbance at a specific wavelength).", answer_ar="المستضد/الجسم المضاد (المكشوف أو الملتقِط)؛ الطور الصلب صفيحة المعايرة (التثبيت)؛ الجسم المضاد الموسوم بالإنزيم (الكشف)؛ الركيزة المولّدة للون (تغيّر لوني)؛ الكاشف/قارئ الصفائح (الامتصاص عند طول موجي محدّد)."),
 dict(en="Compare the four types of ELISA.", ar="قارن بين أنواع الإليزا الأربعة.", answer_en="Direct: labeled antibody on immobilized antigen; simple, less sensitive; high antigen levels. Indirect: primary + enzyme-linked secondary; higher sensitivity; serum antibodies (HIV, HBV). Sandwich: capture antibody, antigen, detection antibody; highly specific and sensitive; cytokines, COVID-19 antigen kits. Competitive: sample vs labeled antigen; signal inversely proportional; small antigens.", answer_ar="المباشرة: جسم مضاد موسوم على مستضد مثبّت؛ بسيطة وأقل حساسية؛ للتراكيز العالية. غير المباشرة: أولي + ثانوي مرتبط بالإنزيم؛ حساسية أعلى؛ أجسام المصل المضادة (HIV، HBV). الساندويتش: ملتقِط، مستضد، كاشف؛ عالية التخصّص والحساسية؛ السيتوكينات وعُدد COVID-19. التنافسية: مستضد العيّنة مقابل الموسوم؛ إشارة عكسية؛ للمستضدات الصغيرة."),
 dict(en="Write the general steps of the ELISA procedure.", ar="اكتب الخطوات العامة للإليزا.", answer_en="(1) Coating; (2) blocking (BSA, casein); (3) sample incubation; (4) detection with enzyme-linked antibody; (5) substrate reaction → colored product; (6) measurement of absorbance (usually 450 nm).", answer_ar="(1) التغليف؛ (2) الحجب (BSA، الكازين)؛ (3) حضن العيّنة؛ (4) الكشف بالجسم المضاد المرتبط بالإنزيم؛ (5) تفاعل الركيزة ← ناتج ملوّن؛ (6) قياس الامتصاص (عادةً 450 نانومتر)."),
 dict(en="How are ELISA data analysed?", ar="كيف تُحلَّل بيانات الإليزا؟", answer_en="Construct a standard curve from known concentrations, measure the OD of unknowns, and determine their concentrations by comparing OD values to the standard curve.", answer_ar="إنشاء منحنى قياسي من تراكيز معلومة، وقياس OD للعيّنات المجهولة، وتحديد تراكيزها بمقارنة قيم OD بالمنحنى القياسي."),
 dict(en="List the advantages and limitations of ELISA.", ar="عدّد مزايا الإليزا وقيودها.", answer_en="Advantages: high sensitivity and specificity, quantitative, cost-effective and scalable, many samples. Limitations: careful optimization needed, false positives/negatives, semi-quantitative without precise standard curves, enzyme/substrate instability.", answer_ar="المزايا: حساسية وتخصّص عاليان، كمّية، قليلة الكلفة وقابلة للتوسّع، عيّنات كثيرة. القيود: تحتاج ضبطًا دقيقًا، نتائج كاذبة، شبه كمّية دون منحنيات دقيقة، عدم ثبات الإنزيم/الركيزة."),
]

data = {"meta": {
  "subject_en": "Advanced Techniques", "subject_ar": "التقنيات المتقدمة", "short_ar": "تقنيات متقدمة",
  "unit_en": "Lecture 1", "unit_ar": "المحاضرة 1", "unit_label": "LEC", "unit_no": "1",
  "title_en": "Enzyme-Linked Immunosorbent Assay (ELISA) Technology", "title_ar": "تقنية الإليزا",
  "kind": "Theory — نظري", "stage": "The third stage — الثالثة", "instructor": "د. مصطفى م. مصطفى"},
 "blocks": blocks, "questions": {"mcq": mcq, "tf": tf, "traps": traps, "important": important}}
qs = [q for q in mcq if "answer" in q]
print(len(qs), Counter(q["answer"] for q in qs))
json.dump(data, open("/home/user/-/advtech-lec1-elisa/lecture.json", "w"), ensure_ascii=False, indent=1)

```
