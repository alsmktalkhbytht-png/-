---
source: BIOS-Obsidian/tools/scripts/pathcmp.py
handouts: [pathology-comparisons]
saved: 2026-11-15
tags: [bios, code]
---
# pathcmp.py — pathology bilingual comparison-tables handout

```python
import json, os, sys
sys.path.insert(0, "/home/user/bios-repo/BIOS-Obsidian/tools/scripts"); from bidi import ltr_all

FOLDER = "pathology-comparisons"
B = lambda e, a: [e, a]

meta = {
 "subject_en": "Pathology", "subject_ar": "علم الأمراض", "short_ar": "أمراض",
 "instructor": "د. حامد خليل التميمي",
 "unit_en": "Comparisons", "unit_ar": "جداول مقارنة", "unit_label": "PATH", "unit_no": "C",
 "title_en": "Selected Comparisons — Renal Failure, Urinary Findings & Atelectasis",
 "title_ar": "جداول مقارنة مختارة — الفشل الكلوي والموجودات البولية والانخماص",
 "kind": "Theory — نظري", "stage": "The fourth stage — الرابعة",
 "file_name": "BIOS - أمراض نظري - جداول مقارنة (الكلى والانخماص)",
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
  ["**Atelectasis**", "الانخماص / انخماص الرئة"],
  ["**Cicatrization**", "التندّب / التليّف الندبي"],
  ["**Pleural effusion**", "الانصباب الجنبي"],
 ]}

blocks = [
 {"t": "section", "en": "Renal failure — acute vs chronic", "ar": "الفشل الكلوي — الحاد مقابل المزمن"}, t1,
 {"t": "section", "en": "Asymptomatic urinary findings — proteinuria vs haematuria", "ar": "الموجودات البولية اللاعرضية — البيلة البروتينية مقابل الدموية"}, t2,
 {"t": "section", "en": "Types of atelectasis", "ar": "أنواع الانخماص الرئوي"}, t3,
 note,
 {"t": "section", "en": "Key terms", "ar": "أهم المصطلحات"}, terms,
]

blocks = ltr_all(blocks)
d = "/home/user/-/" + FOLDER
os.makedirs(d, exist_ok=True)
json.dump({"meta": meta, "blocks": blocks}, open(d + "/lecture.json", "w"), ensure_ascii=False, indent=1)
print(FOLDER, "written |", len(blocks), "blocks")

```
