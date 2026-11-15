---
source: BIOS-Obsidian/tools/scripts/pathcmp.py
handouts: [pathology-comparisons]
saved: 2026-11-15
tags: [bios, code]
---
# pathcmp.py — pathology bilingual comparisons + enumerations handout

```python
import json, os, sys
sys.path.insert(0, "/home/user/bios-repo/BIOS-Obsidian/tools/scripts"); from bidi import ltr_all

FOLDER = "pathology-comparisons"
B = lambda e, a: [e, a]

meta = {
 "subject_en": "Pathology", "subject_ar": "علم الأمراض", "short_ar": "أمراض",
 "instructor": "د. حامد خليل التميمي",
 "unit_en": "Selections", "unit_ar": "مختارات", "unit_label": "PATH", "unit_no": "S",
 "title_en": "Selected Comparisons & Key Lists — Renal & Lung",
 "title_ar": "مقارنات وتعدادات مختارة — الكلى والرئة",
 "kind": "Theory — نظري", "stage": "The fourth stage — الرابعة",
 "file_name": "BIOS - أمراض نظري - مقارنات وتعدادات مختارة",
}

t1 = {"t": "table", "style": "summary",
 "label_en": "Acute vs chronic renal failure", "label_ar": "الفشل الكلوي الحاد مقابل المزمن",
 "key_cols": [0], "widths": [16, 42, 42],
 "head": [B("Feature", "الصفة"), B("Acute renal failure (ARF)", "الفشل الكلوي الحاد (ARF)"), B("Chronic renal failure (CRF)", "الفشل الكلوي المزمن (CRF)")],
 "rows": [
  [B("**Course**", "**المسار**"), B("Rapid decline in renal function", "تدهور سريع في وظيفة الكلية"), B("Advanced renal impairment progressing over years", "قصور كلوي متقدّم يتطوّر عبر سنوات")],
  [B("**Causes**", "**الأسباب**"), B("Many causes, including glomerular disease, principally rapidly progressive GN and acute diffuse proliferative GN", "أسباب كثيرة منها أمراض الكبيبات، وأهمها التهاب الكبيبات سريع التقدّم والتهاب الكبيبات التكاثري المنتشر الحاد"), B("Chronic glomerulonephritis", "التهاب الكبيبات المزمن")],
  [B("**Features**", "**العلامات المميّزة**"), B("Rising urea and creatinine, often with reduced urine output ⁺", "ارتفاع اليوريا والكرياتينين، وغالبًا مع نقص إدرار البول ⁺"), B("Detected by significant proteinuria, haematuria, hypertension and azotaemia", "تُكشف ببيلة بروتينية واضحة وبيلة دموية وارتفاع ضغط وآزوتيميا")],
  [B("**Kidney size**", "**حجم الكلية**"), B("Usually normal or enlarged ⁺", "عادةً طبيعي أو متضخّم ⁺"), B("Small contracted kidneys", "كلى صغيرة متقلّصة")],
 ]}

t2 = {"t": "table", "style": "summary",
 "label_en": "Asymptomatic proteinuria vs haematuria", "label_ar": "البيلة البروتينية مقابل الدموية اللاعرضية",
 "key_cols": [0], "widths": [16, 42, 42],
 "head": [B("Feature", "الصفة"), B("Asymptomatic proteinuria", "البيلة البروتينية اللاعرضية"), B("Asymptomatic haematuria", "البيلة الدموية اللاعرضية")],
 "rows": [
  [B("**Definition**", "**التعريف**"), B("Presence of proteinuria unexpectedly in a patient", "وجود بيلة بروتينية بشكل غير متوقّع في مريض"), B("Asymptomatic microscopic haematuria", "بيلة دموية مجهرية لا عرضية")],
  [B("**Relation to renal disease**", "**العلاقة بمرض الكلية**"), B("May be unrelated to renal disease, or may indicate underlying mild glomerulonephritis", "قد تكون غير متعلّقة بمرض كلوي، أو قد تدلّ على التهاب كبيبات خفيف أساسي"), B("Has many diverse causes", "لها أسباب متنوّعة كثيرة")],
  [B("**Examples of causes**", "**أمثلة الأسباب**"), B("Exercise-induced, extreme lordosis, orthostatic proteinuria (non-renal causes)", "الناتجة عن الجهد، والتقعّر القطني الشديد، والبيلة البروتينية الانتصابية (أسباب غير كلوية)"), B("Urinary tract infection, hypercalciuria, IgA nephropathy, Alport syndrome, thin basement membrane disease, renal stones ⁺", "عدوى المسالك البولية، فرط كالسيوم البول، اعتلال IgA، متلازمة ألبورت، مرض الغشاء القاعدي الرقيق، حصى الكلية ⁺")],
  [B("**Age group**", "**الفئة العمرية**"), B("Commonly seen in children and adolescents, especially the orthostatic type ⁺", "شائعة في الأطفال واليافعين، خصوصًا النوع الانتصابي ⁺"), B("Common in children and young adolescents", "شائعة في الأطفال واليافعين الصغار")],
 ]}

glom = {"t": "card",
 "en": "Four significant components of the glomerulus may be damaged:",
 "ar": "قد تتضرر أربعة مكوّنات مهمة من الكبيبة:",
 "list_en": [
  "Endothelial cells lining the capillary.",
  "Glomerular basement membrane.",
  "Mesangium.",
  "Epithelial cells or podocytes, which form an outer coating to the capillary. These cells are in contact with the outer surface of the basement membrane via a series of foot processes.",
 ],
 "list_ar": [
  "الخلايا البطانية المبطّنة للشعيرة الدموية.",
  "الغشاء القاعدي الكبيبي.",
  "الميزانجيوم (النسيج المسراقي).",
  "الخلايا الظهارية أو الخلايا القدمية (podocytes)، التي تشكّل غطاءً خارجيًا للشعيرة. وهذه الخلايا تلامس السطح الخارجي للغشاء القاعدي عبر سلسلة من النواتئ القدمية (foot processes).",
 ]}

glom_note = {"t": "note",
 "en": ["These four components make up the glomerular filtration barrier. The three layers that actually separate the blood from the filtrate (primary urine) are: the fenestrated capillary endothelium, the glomerular basement membrane, and the podocyte foot processes with their slit diaphragms."],
 "ar": ["هذه المكوّنات الأربعة تُشكّل حاجز الترشيح الكبيبي. والطبقات الثلاث التي تفصل فعليًا بين الدم والمُرشَّح (البول الأولي) هي: بطانة الشعيرة المنخرَبة، والغشاء القاعدي الكبيبي، والنواتئ القدمية للخلايا القدمية بأغشيتها الشقّية."],
 "label": ["BIOS note — what separates blood from the filtrate", "ملاحظة BIOS — ما يفصل الدم عن المُرشَّح"]}

t3 = {"t": "table", "style": "summary",
 "label_en": "Types of atelectasis", "label_ar": "أنواع الانخماص الرئوي",
 "key_cols": [0], "widths": [16, 28, 28, 28],
 "head": [B("Feature", "الصفة"), B("Resorption", "الامتصاصي"), B("Compression", "الانضغاطي"), B("Contraction", "التقلّصي")],
 "rows": [
  [B("**Mechanism**", "**الآلية**"),
   B("Obstruction prevents air from reaching distal airways; trapped air is gradually absorbed, then alveolar collapse follows", "يمنع الانسداد وصول الهواء إلى المجاري الهوائية البعيدة؛ فيُمتصّ الهواء المحتبس تدريجيًا، ثم يتبعه انهيار الأسناخ"),
   B("Fluid, blood or air accumulates in the pleural cavity and mechanically collapses the adjacent lung", "يتجمّع سائل أو دم أو هواء في التجويف الجنبي فيُسبّب انهيارًا ميكانيكيًا للرئة المجاورة"),
   B("Local or generalized fibrotic changes in the lung or pleura hamper expansion and increase elastic recoil during expiration", "تغيّرات ليفية موضعية أو معمّمة في الرئة أو الجنبة تعيق التمدّد وتزيد الارتداد المرن أثناء الزفير")],
  [B("**Main cause(s)**", "**السبب الرئيس**"),
   B("Mucous or mucopurulent plug in a bronchus", "سدادة مخاطية أو مخاطية قيحية في القصبة"),
   B("Pleural effusion (most commonly from CHF), pneumothorax, basal atelectasis from elevated diaphragm", "الانصباب الجنبي (غالبًا من عجز القلب الاحتقاني CHF)، استرواح الصدر، انخماص قاعدي من ارتفاع الحجاب الحاجز"),
   B("Fibrosis", "التليّف")],
  [B("**Associated conditions**", "**الحالات المرافقة**"),
   B("Postoperative state, bronchial asthma, bronchiectasis, chronic bronchitis, tumor, foreign body aspiration (especially children)", "ما بعد الجراحة، الربو القصبي، توسّع القصبات، التهاب القصبات المزمن، الورم، استنشاق جسم غريب (خصوصًا الأطفال)"),
   B("Bedridden patients, ascites, during and after surgery", "المرضى طريحو الفراش، الحبن (الاستسقاء)، أثناء الجراحة وبعدها"),
   B("—", "—")],
  [B("**Also called**", "**ويُسمّى أيضًا**"),
   B("—", "—"),
   B("Passive or relaxation atelectasis", "الانخماص المنفعل أو الارتخائي"),
   B("Cicatrization atelectasis", "الانخماص الندبي (التندّبي)")],
  [B("**Extent / note**", "**الامتداد / ملاحظة**"),
   B("Entire lung, a complete lobe, or one or more segments", "رئة كاملة، أو فص كامل، أو قطعة واحدة أو أكثر"),
   B("—", "—"),
   B("Most serious type — it causes fibrosis", "النوع الأخطر — لأنه يسبّب التليّف")],
 ]}

alv = {"t": "card",
 "en": "The microscopic structure of the alveolar walls (or alveolar septa) consists of the following components, proceeding from blood to air:",
 "ar": "يتكوّن التركيب المجهري لجدران الأسناخ (أو الحواجز السنخية) من المكوّنات التالية، متدرّجًا من الدم إلى الهواء:",
 "list_en": [
  "The capillary endothelium and basement membrane.",
  "The pulmonary interstitium is composed of fine elastic fibers, small bundles of collagen, a few fibroblast-like cells, smooth muscle cells, mast cells, and rare mono-nuclear cells. It is most prominent in thicker portions of the alveolar septum.",
  "Alveolar epithelium contains a continuous layer of two principal cell types: flattened, platelike type I pneumocytes covering 95% of the alveolar surface and rounded type II pneumocytes. The latter synthesize pulmonary surfactant and are the main cell type involved in repair of alveolar epithelium after damage to type I pneumocytes. The alveolar walls are not solid but are perforated by numerous pores of Kohn, which permit passage of air, bacteria, and exudates between adjacent alveoli.",
  "A few alveolar macrophages usually lie free within the alveolar space. In the adult, these macrophages often contain phagocytosed carbon particles.",
 ],
 "list_ar": [
  "بطانة الشعيرة الدموية والغشاء القاعدي.",
  "النسيج الخلالي الرئوي (pulmonary interstitium) يتألّف من ألياف مرنة دقيقة، وحُزَم صغيرة من الكولاجين (collagen)، وقليل من الخلايا الشبيهة بالأرومات الليفية (fibroblast-like)، وخلايا عضلية ملساء، وخلايا بدينة (mast cells)، وخلايا وحيدة النواة نادرة. وهو أبرز ما يكون في الأجزاء الأسمك من الحاجز السنخي.",
  "الظهارة السنخية تحتوي طبقة متّصلة من نوعين رئيسيين من الخلايا: خلايا رئوية من النوع الأول (type I) مفلطحة شبيهة بالصفيحة تغطّي 95% من السطح السنخي، وخلايا رئوية من النوع الثاني (type II) مستديرة. والأخيرة تصنّع الفاعل بالسطح الرئوي (surfactant) وهي الخلية الرئيسة في إصلاح الظهارة السنخية بعد تضرّر خلايا النوع الأول. وجدران الأسناخ ليست مصمتة بل مثقوبة بثقوب كون (pores of Kohn) العديدة التي تسمح بمرور الهواء والبكتيريا والرشحات بين الأسناخ المتجاورة.",
  "توجد عادةً بضع بلاعم سنخية (alveolar macrophages) حرّة داخل الحيّز السنخي. وفي البالغ، كثيرًا ما تحتوي هذه البلاعم على جُسيمات كربون مبتلَعة.",
 ]}

alv_note = {"t": "note",
 "en": ["Common exam question (“mention”): list the components of the alveolar wall / septum from blood to air."],
 "ar": ["سؤال امتحاني شائع (mention): عدّد مكوّنات جدار السنخ (الحاجز السنخي) من الدم إلى الهواء."],
 "label": ["BIOS note — exam", "ملاحظة BIOS — امتحاني"]}

note = {"t": "note",
 "en": ["⁺ These points are added to complete the comparison; they are general-knowledge items, not taken from the original lecture text."],
 "ar": ["⁺ هذه البنود أُضيفت لتكملة المقارنة؛ وهي من المعرفة العامة لا من نصّ المحاضرة الأصلي."],
 "label": ["BIOS note", "ملاحظة BIOS"]}

terms = {"t": "table", "ar_cols": [1], "widths": [34, 66],
 "head": [B("Term", "المصطلح"), "الترجمات العربية المستعملة"],
 "rows": [
  ["**GN (glomerulonephritis)**", "التهاب الكبيبات (والكلية)"],
  ["**Rapidly progressive GN (RPGN)**", "التهاب الكبيبات سريع التقدّم"],
  ["**Azotaemia**", "الآزوتيميا / ارتفاع نواتج النتروجين (اليوريا) في الدم"],
  ["**Orthostatic proteinuria**", "البيلة البروتينية الانتصابية / الوضعية"],
  ["**Podocyte / foot processes**", "الخلية القدمية / النواتئ القدمية"],
  ["**Mesangium**", "الميزانجيوم / النسيج المسراقي"],
  ["**Pneumocyte (type I / II)**", "الخلية الرئوية (النوع الأول / الثاني)"],
  ["**Surfactant**", "الفاعل بالسطح الرئوي"],
  ["**Pores of Kohn**", "ثقوب كون"],
  ["**Atelectasis**", "الانخماص / انخماص الرئة"],
  ["**Cicatrization**", "التندّب / التليّف الندبي"],
  ["**Pleural effusion**", "الانصباب الجنبي"],
 ]}

blocks = [
 {"t": "section", "en": "Renal failure — acute vs chronic", "ar": "الفشل الكلوي — الحاد مقابل المزمن"}, t1,
 {"t": "section", "en": "Asymptomatic urinary findings — proteinuria vs haematuria", "ar": "الموجودات البولية اللاعرضية — البيلة البروتينية مقابل الدموية"}, t2,
 {"t": "section", "en": "Components of the glomerulus that may be damaged", "ar": "مكوّنات الكبيبة التي قد تتضرر"}, glom, glom_note,
 {"t": "section", "en": "Types of atelectasis", "ar": "أنواع الانخماص الرئوي"}, t3,
 {"t": "section", "en": "Alveolar wall structure", "ar": "تركيب جدار السنخ (الحاجز السنخي)"}, alv, alv_note,
 note,
 {"t": "section", "en": "Key terms", "ar": "أهم المصطلحات"}, terms,
]

blocks = ltr_all(blocks)
d = "/home/user/-/" + FOLDER
os.makedirs(d, exist_ok=True)
json.dump({"meta": meta, "blocks": blocks}, open(d + "/lecture.json", "w"), ensure_ascii=False, indent=1)
print(FOLDER, "written |", len(blocks), "blocks")

```
