---
source: BIOS-Obsidian/tools/scripts/hem3/l2.py
handouts: [hematology-lec2-blood-cell-formation]
saved: 2026-10-29
tags: [bios, code]
---
# hem3/l2.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#hematology-lec2-blood-cell-formation|hematology-lec2-blood-cell-formation]]

```python
from common import *

blocks = [
 SEC("Haemopoiesis", "تكوين الدم"),
 C("**Haemopoiesis:** It is the **production and maintenance of blood cells** (i.e. Red cells, White cells and platelets) at the **normal physiological level**.",
   "**تكوين الدم** (`Haemopoiesis`): هو **إنتاج خلايا الدم والمحافظة عليها** (أي الكريات الحمر والكريات البيض والصفيحات) عند **المستوى الفسيولوجي الطبيعي**."),

 SEC("Site of haemopoiesis", "مواقع تكوين الدم"),
 T(["Age", "Site", "العمر — الموقع"],
   [["Fetus 0-2 months", "yolk sac.", "**الجنين 0–2 شهر**: كيس المح."],
    ["Fetus 2-7 months", "liver, spleen.", "**الجنين 2–7 أشهر**: الكبد والطحال."],
    ["Fetus 5-9 months", "bone marrow (B.M).", "**الجنين 5–9 أشهر**: نخاع العظم."],
    ["Infants", "Bone marrow (B.M) practically all bones.", "**الرضّع**: نخاع العظم في جميع العظام تقريبًا."],
    ["Adults", "vertebrae, ribs, sternum, skull, sacrum, pelvic and proximal ends of femur.", "**البالغون**: الفقرات، الأضلاع، عظم القص، الجمجمة، العجز، الحوض، والنهايات القريبة لعظم الفخذ."]],
   ar_cols=[2], key_cols=[0], widths=["32mm", "", ""]),
 C(["The **bone marrow** represented approximately **3.5-6 %** of total body weight, average around **1500 gm.** in adults,",
    "and consist of haemopoeitic cells, fat, osteoblast, osteoclast and stroma."],
   ["يمثّل **نخاع العظم** نحو **3.5–6%** من وزن الجسم الكلي، بمعدل **1500 غم** تقريبًا عند البالغين،",
    "ويتكوّن من الخلايا المكوّنة للدم، والدهن، والخلايا البانية للعظم، والخلايا الكاسرة للعظم، والسدى (النسيج الداعم)."]),
 L(["**Yellow marrow**(inactive)composed of **fat tissues**", "**RED marrow** (active) contain **all the three cell types**."],
   ["**النخاع الأصفر** (غير فعّال) يتكوّن من **أنسجة دهنية**", "**النخاع الأحمر** (فعّال) يحتوي على **أنواع الخلايا الثلاثة كلها**."],
   en="**Types of marrow:**", ar="**أنواع النخاع:**"),

 SEC("Type's haemopoiesis", "أنواع تكوين الدم"),
 R("**Medullary Haemopoiesis** (Intramedullary haemopoiesis): This is the formation of blood cells **from B.M.**",
   "**تكوين الدم النخاعي** (داخل النخاع): هو تكوين خلايا الدم **من نخاع العظم**."),
 R("**Extra-medullary Haemopoiesis**: This is the formation of blood cells **outside the B.M** (e.g. liver, spleen).",
   "**تكوين الدم خارج النخاع**: هو تكوين خلايا الدم **خارج نخاع العظم** (مثل الكبد والطحال)."),
 C("This type of haemopoiesis (extra-medullary) occurs when either:", "يحدث هذا النوع (خارج النخاع) في إحدى الحالتين:", alpha=True,
   list_en=["B.M **fails** to produce blood cells like in **myelofibrosis** or when B.M **infiltrated** by non-haemopoeitic elements like any **tumors**. Or",
            "When there is **no B.M failure** but B.M **cannot produce enough** blood cells specially the red cells and this usually occur in **hemolytic anemia**."],
   list_ar=["**يفشل** نخاع العظم في إنتاج خلايا الدم كما في **تليّف النخاع**، أو عندما **يرتشح** النخاع بعناصر غير مكوّنة للدم مثل أي **أورام**. أو",
            "عندما **لا يوجد فشل** في النخاع لكنه **لا يستطيع إنتاج ما يكفي** من خلايا الدم ولا سيما الحمر، ويحدث هذا عادةً في **فقر الدم الانحلالي**."]),

 SEC("Origin of blood cells", "منشأ خلايا الدم"),
 C("All the blood cells arise from **\"Hematopoietic stem cells”** or **“Pluripotent stem cell”**.",
   "تنشأ جميع خلايا الدم من **«الخلايا الجذعية المكوّنة للدم»** أو **«الخلية الجذعية متعدّدة القدرات»**."),
 C("The common pluripotent stem cell give rise to a series of progenitor cells after a number a number of cell divisions and differentiations , these series of progenitor cells can gives rise after a number of cell divisions and differentiation steps to a series of progenitor cells for **three main marrow cell lines**:",
   "تعطي الخلية الجذعية متعدّدة القدرات المشتركة سلسلة من الخلايا السلفية بعد عدد من الانقسامات والتمايزات، وتعطي هذه الخلايا السلفية بعد عدد من خطوات الانقسام والتمايز سلسلة من الخلايا السلفية لـ**ثلاثة خطوط خلوية نخاعية رئيسة**:",
   alpha=True,
   list_en=["Erythroid", "Granulocytic and monocytic", "Megakaryocytic as well as to a **common lymphoid stem cell**."],
   list_ar=["الخط الحمري", "الخط المحبّب والوحيدي", "الخط النوّائي (المكوّن للصفيحات)، إضافة إلى **خلية جذعية لمفاوية مشتركة**."]),
 C(["HSC is **rare** , perhaps **1 in every 20 million** nucleated cells in bone marrow .",
    "The stem cells also has the capability of **self-renewal, proliferation and differentiation** so that the BM is the main site of new cell productions, its overall **cellularity remains constant** in a normal healthy steady state."],
   ["الخلايا الجذعية المكوّنة للدم (`HSC`) **نادرة**، ربما **واحدة في كل 20 مليون** خلية منوّاة في نخاع العظم.",
    "ولها القدرة على **التجدّد الذاتي والتكاثر والتمايز**، بحيث يكون نخاع العظم الموقع الرئيس لإنتاج الخلايا الجديدة، و**تبقى خلويّته الكلية ثابتة** في الحالة الصحية الطبيعية المستقرة."]),
 C(["The **precursor cells** are however capable of responding to various stimuli and hormonal messages with increased productions of one or other cell line **according to the body need**.",
    "These stimuli include **haematopoeitic growth factors, hormones and interleukins**."],
   ["غير أن **الخلايا الأولية** قادرة على الاستجابة لمحفّزات ورسائل هرمونية مختلفة بزيادة إنتاج خط خلوي أو آخر **بحسب حاجة الجسم**.",
    "وتشمل هذه المحفّزات **عوامل النمو المكوّنة للدم، والهرمونات، والإنترلوكينات**."]),

 SEC("Regulation of blood elements production", "تنظيم إنتاج عناصر الدم"),
 C(["The production of these blood elements are under control of **haemopoietic growth factors** which include **IL1,IL3,IL5,IL6,TNF,SCF,G.CSF,Erythropietin and thrombopoietin**.",
    "All these factors regulate the **proliferation and differentiation** of haemopoietic progenitor's cells and the **function of mature blood cells**."],
   ["يخضع إنتاج عناصر الدم هذه لسيطرة **عوامل النمو المكوّنة للدم**، ومنها `IL1` و`IL3` و`IL5` و`IL6` و`TNF` و`SCF` و`G-CSF` و**الإريثروبويتين والثرومبوبويتين**.",
    "وتنظّم جميع هذه العوامل **تكاثر وتمايز** الخلايا السلفية المكوّنة للدم و**وظيفة خلايا الدم الناضجة**."]),

 H2("1. Erythrocyte production (Erythropoiesis)", "1. إنتاج الكريات الحمر (تكوين الكريات الحمر)"),
 FLOW([("Pronormoblast", "أرومة سوية أولية"), ("Normoblast (erythroblast)", "أرومة سوية (أرومة حمراء)"), ("Early erythroblast (basophilic)", "أرومة حمراء مبكرة (قاعدية)"),
       ("Intermediate erythroblast (polychromatic)", "أرومة حمراء وسطية (متعدّدة الألوان)"), ("Late erythroblast (pyknotic)", "أرومة حمراء متأخرة (متغلّظة النواة)"),
       ("Reticulocytes", "الخلايا الشبكية"), ("Red cells", "الكريات الحمر")]),
 C("The progressive differentiation and proliferation appear to be under the control of **erythropoietin** which is produce mainly in the **kidney (90%)** and possibly **10% in liver** and other organs",
   "يبدو أن التمايز والتكاثر المتدرّجين تحت سيطرة **الإريثروبويتين** الذي يُنتج أساسًا في **الكلية (90%)** وربما **10% في الكبد** وأعضاء أخرى"),
 H2("2. Granulocyte production (Granulopoiesis)", "2. إنتاج الخلايا المحبّبة"),
 FLOW([("Myeloblast", "أرومة نقوية"), ("Promyelocyte", "خلية نقوية أولية"), ("Myelocytes", "خلايا نقوية"), ("Metamyelocytes", "خلايا نقوية بعدية"), ("Band form", "الشكل الشريطي")]),
 L(["Neutrophils", "Eosinophils", "Basophiles"], ["العدلات", "الحمضات", "القعدات"], en="**Band form →**", ar="**الشكل الشريطي ←**"),
 C("The production of these granulocytes are under control of haemopoietic growth factors which include **IL1, IL3, IL5, IL6, TNF, SCF, G.CSF**.",
   "يخضع إنتاج هذه الخلايا المحبّبة لسيطرة عوامل النمو المكوّنة للدم، ومنها `IL1` و`IL3` و`IL5` و`IL6` و`TNF` و`SCF` و`G-CSF`."),
 H2("3. Platelets production (Megakaryopoiesis)", "3. إنتاج الصفيحات"),
 FLOW([("Megakaryoblast", "أرومة نوّائية"), ("Megakaryocytes", "الخلايا النوّائية (المكوّنة للصفيحات)"), ("Platelets", "الصفيحات")]),
 L(["Platelets production is under control of humeral agents knows as **Thrombopoietin**, made largely in the **liver**.", "The normal platelets lifespan is **7-10 days**."],
   ["يخضع إنتاج الصفيحات لسيطرة عوامل خِلطية تُعرف بـ**الثرومبوبويتين**، الذي يُصنع غالبًا في **الكبد**.", "العمر الطبيعي للصفيحات **7–10 أيام**."]),
]

mcq = [
 {"topic_en": "Haemopoiesis and its sites", "topic_ar": "تكوين الدم ومواقعه"},
 Q("Haemopoiesis is the production and maintenance of:", "تكوين الدم هو إنتاج والمحافظة على:", [("Plasma proteins", "بروتينات البلازما"), ("Blood cells", "خلايا الدم"), ("Bone tissue", "النسيج العظمي"), ("Lymph", "اللمف")], "b"),
 Q("In the fetus 0–2 months, haemopoiesis occurs in the:", "في الجنين 0–2 شهر يحدث تكوين الدم في:", [("Yolk sac", "كيس المح"), ("Liver", "الكبد"), ("Bone marrow", "نخاع العظم"), ("Spleen", "الطحال")], "a"),
 Q("In the fetus 2–7 months, the main sites are:", "في الجنين 2–7 أشهر تكون المواقع الرئيسة:", [("Yolk sac", "كيس المح"), ("Vertebrae", "الفقرات"), ("Liver and spleen", "الكبد والطحال"), ("Lymph nodes", "العقد اللمفاوية")], "c"),
 Q("Bone marrow starts haemopoiesis in the fetus at:", "يبدأ نخاع العظم تكوين الدم في الجنين عند:", [("0–2 months", "0–2 شهر"), ("1–3 months", "1–3 أشهر"), ("2–4 months", "2–4 أشهر"), ("5–9 months", "5–9 أشهر")], "d"),
 Q("In adults, haemopoiesis occurs in all of the following EXCEPT:", "عند البالغين يحدث تكوين الدم في كل مما يأتي عدا:", [("Vertebrae", "الفقرات"), ("Sternum", "عظم القص"), ("Distal ends of the tibia", "النهايات البعيدة لعظم الظنبوب"), ("Pelvis", "الحوض")], "c"),
 Q("The bone marrow in adults weighs on average about:", "يزن نخاع العظم عند البالغين بالمعدّل نحو:", [("500 g", "500 غم"), ("1500 g", "1500 غم"), ("3000 g", "3000 غم"), ("150 g", "150 غم")], "b"),
 Q("Bone marrow represents about what percentage of body weight?", "يمثّل نخاع العظم نحو أي نسبة من وزن الجسم؟", [("3.5–6%", "3.5–6%"), ("10–15%", "10–15%"), ("0.5–1%", "0.5–1%"), ("20%", "20%")], "a"),
 Q("Yellow marrow is:", "النخاع الأصفر:", [("Active and contains all three cell lines", "فعّال ويحتوي الخطوط الثلاثة"), ("Composed of lymphocytes", "يتكوّن من اللمفاويات"), ("Found only in the fetus", "يوجد في الجنين فقط"), ("Inactive and composed of fat tissue", "غير فعّال ويتكوّن من نسيج دهني")], "d"),
 Q("Extramedullary haemopoiesis means formation of blood cells:", "تكوين الدم خارج النخاع يعني تكوين خلايا الدم:", [("Outside the bone marrow (e.g. liver, spleen)", "خارج النخاع (مثل الكبد والطحال)"), ("Inside the bone marrow", "داخل النخاع"), ("In the kidney only", "في الكلية فقط"), ("In lymph only", "في اللمف فقط")], "a"),
 Q("Extramedullary haemopoiesis without bone marrow failure usually occurs in:", "يحدث تكوين الدم خارج النخاع دون فشل النخاع عادةً في:", [("Myelofibrosis", "تليّف النخاع"), ("Tumour infiltration", "ارتشاح الأورام"), ("Hemolytic anemia", "فقر الدم الانحلالي"), ("Aplastic anaemia", "فقر الدم اللاتنسّجي")], "c"),
 {"topic_en": "Stem cells and regulation", "topic_ar": "الخلايا الجذعية والتنظيم"},
 Q("All blood cells arise from:", "تنشأ جميع خلايا الدم من:", [("Erythroblasts", "الأرومات الحمر"), ("Pluripotent haematopoietic stem cells", "الخلايا الجذعية المكوّنة للدم متعدّدة القدرات"), ("Megakaryocytes", "الخلايا النوّائية"), ("Lymphocytes", "اللمفاويات")], "b"),
 Q("The frequency of HSC in bone marrow is perhaps:", "نسبة الخلايا الجذعية المكوّنة للدم في النخاع ربما:", [("1 in 100 cells", "1 في 100 خلية"), ("1 in 1000 cells", "1 في 1000 خلية"), ("1 in 1 million", "1 في مليون"), ("1 in 20 million nucleated cells", "1 في 20 مليون خلية منوّاة")], "d"),
 Q("Stem cells are capable of all EXCEPT:", "الخلايا الجذعية قادرة على كل مما يأتي عدا:", [("Self-renewal", "التجدّد الذاتي"), ("Proliferation", "التكاثر"), ("Differentiation", "التمايز"), ("Producing haemoglobin themselves", "إنتاج الهيموغلوبين بنفسها")], "d"),
 Q("Erythropoietin is produced mainly in the:", "يُنتج الإريثروبويتين أساسًا في:", [("Liver", "الكبد"), ("Spleen", "الطحال"), ("Kidney (90%)", "الكلية (90%)"), ("Bone marrow", "نخاع العظم")], "c"),
 Q("Thrombopoietin is made largely in the:", "يُصنع الثرومبوبويتين غالبًا في:", [("Liver", "الكبد"), ("Kidney", "الكلية"), ("Spleen", "الطحال"), ("Lungs", "الرئتين")], "a"),
 Q("The normal platelet lifespan is:", "العمر الطبيعي للصفيحات:", [("1–2 days", "1–2 يوم"), ("7–10 days", "7–10 أيام"), ("30 days", "30 يومًا"), ("120 days", "120 يومًا")], "b"),
 Q("The cell that directly precedes red cells in erythropoiesis is the:", "الخلية التي تسبق الكرية الحمراء مباشرة في تكوين الكريات الحمر هي:", [("Pronormoblast", "الأرومة السوية الأولية"), ("Late erythroblast", "الأرومة الحمراء المتأخرة"), ("Reticulocyte", "الخلية الشبكية"), ("Myeloblast", "الأرومة النقوية")], "c"),
 Q("The first cell of granulopoiesis is the:", "الخلية الأولى في تكوين المحبّبات هي:", [("Myeloblast", "الأرومة النقوية"), ("Promyelocyte", "الخلية النقوية الأولية"), ("Metamyelocyte", "الخلية النقوية البعدية"), ("Band form", "الشكل الشريطي")], "a"),
 Q("Platelets are produced from:", "تُنتج الصفيحات من:", [("Myelocytes", "الخلايا النقوية"), ("Reticulocytes", "الخلايا الشبكية"), ("Monocytes", "الوحيدات"), ("Megakaryocytes", "الخلايا النوّائية")], "d"),
 Q("The intermediate erythroblast is described as:", "توصف الأرومة الحمراء الوسطية بأنها:", [("Basophilic", "قاعدية"), ("Polychromatic", "متعدّدة الألوان"), ("Pyknotic", "متغلّظة النواة"), ("Granular", "محبّبة")], "b"),
]
tf = [
 TF("The spleen is a site of haemopoiesis in the fetus 2–7 months.", "الطحال موقع لتكوين الدم في الجنين 2–7 أشهر.", "T"),
 TF("In infants, haemopoiesis occurs in practically all bones.", "عند الرضّع يحدث تكوين الدم في جميع العظام تقريبًا.", "T"),
 TF("Yellow marrow contains all three cell types.", "النخاع الأصفر يحتوي أنواع الخلايا الثلاثة.", "F"),
 TF("Myelofibrosis can lead to extramedullary haemopoiesis.", "قد يؤدي تليّف النخاع إلى تكوين الدم خارج النخاع.", "T"),
 TF("Haematopoietic stem cells are very common in the marrow.", "الخلايا الجذعية المكوّنة للدم شائعة جدًا في النخاع.", "F"),
 TF("Bone marrow cellularity remains constant in a healthy steady state.", "تبقى خلويّة النخاع ثابتة في الحالة الصحية المستقرة.", "T"),
 TF("Erythropoietin is produced mainly in the liver.", "يُنتج الإريثروبويتين أساسًا في الكبد.", "F"),
 TF("Granulopoiesis is controlled by growth factors such as G-CSF and IL3.", "يخضع تكوين المحبّبات لعوامل نمو مثل G-CSF وIL3.", "T"),
 TF("The band form gives rise to neutrophils, eosinophils and basophils.", "يعطي الشكل الشريطي العدلات والحمضات والقعدات.", "T"),
 TF("Platelets live about 120 days.", "تعيش الصفيحات نحو 120 يومًا.", "F"),
 TF("A common lymphoid stem cell arises from the pluripotent stem cell.", "تنشأ خلية جذعية لمفاوية مشتركة من الخلية الجذعية متعدّدة القدرات.", "T"),
]
traps = [
 TR("Fetal sites — order and months", "مواقع الجنين — الترتيب والأشهر", "Yolk sac 0–2 m → liver and spleen 2–7 m → bone marrow 5–9 m (overlapping).", "كيس المح 0–2 شهر ← الكبد والطحال 2–7 ← نخاع العظم 5–9 (مع تداخل)."),
 TR("Yellow vs red marrow", "النخاع الأصفر مقابل الأحمر", "Yellow: inactive, fat. Red: active, contains all three cell types.", "الأصفر: غير فعّال، دهني. الأحمر: فعّال، يحتوي الأنواع الثلاثة."),
 TR("Two causes of extramedullary haemopoiesis", "سببا تكوين الدم خارج النخاع", "(A) Marrow failure or infiltration (myelofibrosis, tumours); (B) no failure but not enough production — haemolytic anaemia.", "(أ) فشل النخاع أو ارتشاحه (تليّف، أورام)؛ (ب) لا فشل لكن إنتاج غير كافٍ — فقر الدم الانحلالي."),
 TR("Erythropoietin vs thrombopoietin — where made?", "الإريثروبويتين مقابل الثرومبوبويتين — أين يُصنعان؟", "Erythropoietin: kidney 90% (liver ~10%). Thrombopoietin: mainly liver.", "الإريثروبويتين: الكلية 90% (الكبد نحو 10%). الثرومبوبويتين: الكبد أساسًا."),
 TR("Erythroblast stages", "مراحل الأرومة الحمراء", "Early = basophilic; intermediate = polychromatic; late = pyknotic.", "المبكرة = قاعدية؛ الوسطية = متعدّدة الألوان؛ المتأخرة = متغلّظة النواة."),
]
important = [
 IM("Define haemopoiesis and list its sites by age.", "عرّف تكوين الدم وعدّد مواقعه بحسب العمر.", "Production and maintenance of red cells, white cells and platelets at the normal level. Fetus: yolk sac 0–2 m, liver and spleen 2–7 m, bone marrow 5–9 m; infants: marrow of practically all bones; adults: vertebrae, ribs, sternum, skull, sacrum, pelvis, proximal femur.", "إنتاج الكريات الحمر والبيض والصفيحات والمحافظة عليها بالمستوى الطبيعي. الجنين: كيس المح 0–2، الكبد والطحال 2–7، النخاع 5–9؛ الرضّع: نخاع جميع العظام تقريبًا؛ البالغون: الفقرات، الأضلاع، القص، الجمجمة، العجز، الحوض، نهاية الفخذ القريبة."),
 IM("What is extramedullary haemopoiesis and when does it occur?", "ما تكوين الدم خارج النخاع ومتى يحدث؟", "Blood cell formation outside the marrow (liver, spleen); occurs when the marrow fails (myelofibrosis) or is infiltrated (tumours), or when it cannot produce enough red cells as in haemolytic anaemia.", "تكوين خلايا الدم خارج النخاع (الكبد، الطحال)؛ يحدث عند فشل النخاع (التليّف) أو ارتشاحه (الأورام)، أو عندما لا يكفي إنتاجه للكريات الحمر كما في فقر الدم الانحلالي."),
 IM("Describe the origin of blood cells from stem cells.", "صف منشأ خلايا الدم من الخلايا الجذعية.", "The pluripotent stem cell gives progenitors for erythroid, granulocytic/monocytic and megakaryocytic lines and a common lymphoid stem cell. HSCs are rare (1 in 20 million), capable of self-renewal, proliferation and differentiation; precursors respond to growth factors, hormones and interleukins.", "تعطي الخلية الجذعية متعدّدة القدرات خلايا سلفية للخطوط الحمري، والمحبّب/الوحيدي، والنوّائي، وخلية جذعية لمفاوية مشتركة. الخلايا الجذعية نادرة (1 في 20 مليون) وقادرة على التجدّد والتكاثر والتمايز؛ وتستجيب الأوليات لعوامل النمو والهرمونات والإنترلوكينات."),
 IM("Write the stages of erythropoiesis and its regulation.", "اكتب مراحل تكوين الكريات الحمر وتنظيمه.", "Pronormoblast → normoblast: early (basophilic), intermediate (polychromatic), late (pyknotic) → reticulocyte → red cell; controlled by erythropoietin (kidney 90%, liver ~10%).", "أرومة سوية أولية ← أرومة سوية: مبكرة (قاعدية)، وسطية (متعدّدة الألوان)، متأخرة (متغلّظة) ← خلية شبكية ← كرية حمراء؛ ويتحكّم بها الإريثروبويتين (الكلية 90%، الكبد نحو 10%)."),
 IM("Write the stages of granulopoiesis and megakaryopoiesis.", "اكتب مراحل تكوين المحبّبات والصفيحات.", "Myeloblast → promyelocyte → myelocyte → metamyelocyte → band → neutrophil/eosinophil/basophil (IL1, IL3, IL5, IL6, TNF, SCF, G-CSF). Megakaryoblast → megakaryocyte → platelets (thrombopoietin, liver; lifespan 7–10 days).", "أرومة نقوية ← نقوية أولية ← نقوية ← نقوية بعدية ← شريطية ← عدلة/حمضة/قعدة (IL1، IL3، IL5، IL6، TNF، SCF، G-CSF). أرومة نوّائية ← خلية نوّائية ← صفيحات (الثرومبوبويتين، الكبد؛ عمرها 7–10 أيام)."),
]
save("hematology-lec2-blood-cell-formation", 2, "Blood cell formation", "تكوين خلايا الدم", blocks, mcq, tf, traps, important)

```
