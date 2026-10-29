---
source: BIOS-Obsidian/tools/scripts/hem3/l7.py
handouts: [hematology-lec7-chronic-sideroblastic]
saved: 2026-10-29
tags: [bios, code]
---
# hem3/l7.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#hematology-lec7-chronic-sideroblastic|hematology-lec7-chronic-sideroblastic]]

```python
from common import *

blocks = [
 SEC("Anaemia of chronic disorders", "فقر دم الاضطرابات المزمنة"),
 C(["**One of the most common anaemias** occurs in patients with a variety of chronic illnesses, e.g. **infections, inflammation and malignancy**.",
    "The pathogenesis of this type of anaemia appears to be related to **decreased release of iron from macrophages to plasma**, **reduced red cell lifespan** and an **inadequate erythropoietin response** to anaemia.",
    "This type of anaemia is **only corrected by successful treatment of underlying diseases** and **dose not response to iron therapy**."],
   ["**من أكثر أنواع فقر الدم شيوعًا**، ويحدث عند مرضى أمراض مزمنة متنوّعة، مثل **العدوى والالتهاب والخباثة**.",
    "ويبدو أن إمراضيته مرتبطة بـ**انخفاض تحرير الحديد من البلاعم إلى البلازما**، و**قِصَر عمر الكريات الحمر**، و**عدم كفاية استجابة الإريثروبويتين** لفقر الدم.",
    "ولا **يُصحَّح هذا النوع إلا بنجاح علاج المرض الأساسي**، و**لا يستجيب للعلاج بالحديد**."]),
 C("**Causes:**", "**الأسباب:**",
   list_en=["**Chronic inflammatory diseases:** A. **Infections** e.g. pulmonary abscess, tuberculosis and osteomyelitis. B. **Non-infectious**: e.g. Rheumatoid arthritis, SLE, and other connective tissues disorders.",
            "**Malignant diseases:** e.g. carcinoma, sarcoma and lymphoma."],
   list_ar=["**الأمراض الالتهابية المزمنة:** أ. **العدوى** مثل خرّاج الرئة والتدرّن والتهاب العظم والنقي. ب. **غير المعدية**: مثل التهاب المفاصل الرثياني، والذئبة الحمراء الجهازية (`SLE`)، واضطرابات النسيج الضام الأخرى.",
            "**الأمراض الخبيثة:** مثل السرطانة، والساركوما، واللمفوما."]),
 C("**The characteristic features are:**", "**السمات المميِّزة:**",
   list_en=["**Normochromic normocytic** or mildly hypochromic.", "**Mild and non-progressive** anaemia (haemoglobin **rarely less than 9.0 g/dl**- the severity being related to the severity of disease.",
            "Both **serum iron and TIBC are reduced** while the **sTfR receptors are normal**.", "The **serum Ferritin is normal or raised**.",
            "**Bone marrow iron storage is normal** but **erythroblast iron is reduced**."],
   list_ar=["**سوي الصباغ سوي الكريات** أو ناقص الصباغ قليلًا.", "فقر دم **خفيف وغير متقدّم** (الهيموغلوبين **نادرًا ما يقل عن 9.0 غ/دل**) — وتتعلّق شدّته بشدّة المرض.",
            "**ينخفض حديد المصل و`TIBC` كلاهما** بينما تكون **مستقبلات الترانسفيرين الذائبة (`sTfR`) طبيعية**.", "**فيريتين المصل طبيعي أو مرتفع**.",
            "**مخزون حديد النخاع طبيعي** لكن **حديد الأرومات الحمر منخفض**."]),
 C("**Mechanism:** Several mechanism founded explain the occurrences of this type of anemia:", "**الآلية:** وُجدت آليات عدة تفسّر حدوث هذا النوع من فقر الدم:"),
 R("Response to inflammatory cytokines predominately **IL6**, the liver also produce increased amount of **hepcidin** which in turn **stop ferroportin from releasing iron stores**.",
   "استجابةً للسيتوكينات الالتهابية ولا سيما **`IL6`**، ينتج الكبد كمية متزايدة من **الهبسيدين** الذي **يمنع الفيروبورتين من تحرير مخازن الحديد**."),
 R("Inflammatory cytokines promotes the productions of **more WBC** and this will cause **fewer stem cell to differentiate to red cells**.",
   "تعزّز السيتوكينات الالتهابية إنتاج **مزيد من الكريات البيض**، فيؤدي ذلك إلى **تمايز عدد أقل من الخلايا الجذعية إلى كريات حمر**."),
 R("In **renal failure** anemia may develop due to **decrease productions of erythropoietin**.", "في **الفشل الكلوي** قد يحدث فقر الدم بسبب **انخفاض إنتاج الإريثروبويتين**."),
 R("Some **drugs** used in different chronic disorders may **inhibit erythropoiesis**.", "قد **تثبّط** بعض **الأدوية** المستخدمة في الاضطرابات المزمنة المختلفة **تكوين الكريات الحمر**."),

 SEC("Sideroblastic anemia", "فقر الدم الحديدي الأرومات"),
 C(["The Sideroblastic anemia are a heterogeneous group of disorders that lead to **abnormal haem synthesis (ineffective erythropoiesis)** , so in this type of anemia the body has **adequate iron but cannot incorporate it** into hemoglobin synthesis,",
    "the iron enter the developing erythrocytes but **accumulated in the perinuclear mitochondria of normoblast**."],
   ["فقر الدم الحديدي الأرومات مجموعة غير متجانسة من الاضطرابات تؤدي إلى **تخليق هيم غير طبيعي (تكوين كريات غير فعّال)**، ففي هذا النوع يكون لدى الجسم **حديد كافٍ لكنه لا يستطيع إدخاله** في تخليق الهيموغلوبين،",
    "فيدخل الحديد الكريات النامية لكنه **يتراكم في المايتوكوندريا المحيطة بالنواة في الأرومة السوية**."]),
 C(["So it’s regarded as a **refractory anemia** with **hypochromic cells** in the peripheral blood and **increase marrow iron** .",
    "It is defined by the presence of many pathological **rings Sidroblast** in the B.M.",
    "The anemia is classified into different types, there's probably always a **defect in haem synthesis**."],
   ["لذلك يُعدّ **فقر دم معنّدًا** مع **خلايا ناقصة الصباغ** في الدم المحيطي و**زيادة حديد النخاع**.",
    "ويُعرَّف بوجود كثير من **الأرومات الحديدية الحلقية** المرضية في نخاع العظم.",
    "ويُصنَّف إلى أنواع مختلفة، وفيها جميعًا على الأرجح **خلل في تخليق الهيم**."]),
 T(["Type", "Details", "النوع — التفاصيل"],
   [["1. Hereditary (Genetic)", "occur due to congenital enzyme defect of haem synthesis. And could be either A: X-Linked B: Autosomal dominant (AD) or Autosomal Recessive (AR).",
     "**الوراثي**: بسبب خلل إنزيمي خلقي في تخليق الهيم، وقد يكون مرتبطًا بالكروموسوم `X`، أو جسميًا سائدًا (`AD`) أو جسميًا متنحّيًا (`AR`)."],
    ["2. Aquired — Primary", "Associated with Myelodysplasia type 2.", "**المكتسب الأولي**: مرتبط بخلل التنسّج النقوي النوع 2."],
    ["2. Aquired — Secondary", "Associated with other malignant diseases of marrow(e.g. lymphoma and multiple myeloma), Drugs like anti-TB, Lead poising, Alcoholism.",
     "**المكتسب الثانوي**: مرتبط بأمراض النخاع الخبيثة الأخرى (مثل اللمفوما والورم النقوي المتعدّد)، والأدوية مثل مضادات التدرّن، والتسمّم بالرصاص، وإدمان الكحول."]],
   ar_cols=[2], key_cols=[0], widths=["32mm", "", ""]),
 C(["**Clinical Manifestation :** Patient have the usual symptoms of anemia including **skin pallor, fatigue, dizziness, and hepatosplenomegaly** (enlarge liver and spleen).",
    "Complication of **iron accumulation** may lead to **heart, liver, kidney and endocrine organ diseases**."],
   ["**المظاهر السريرية:** لدى المريض أعراض فقر الدم المعتادة ومنها **شحوب الجلد، والتعب، والدوخة، وتضخّم الكبد والطحال**.",
    "وقد تؤدي مضاعفات **تراكم الحديد** إلى **أمراض القلب والكبد والكلية والغدد الصمّاء**."]),
 L(["**Mild to moderate anemia** with Hb level ranging from **4-10 mg/dl**.", "Blood film show **hypochromic** blood pictures and sometime **basophilic stippling**.",
    "**Serum iron, serum ferritin are increased.**", "**TIBC is normal or decrease.**",
    "BM show **Erythroid hyperplasia** and staining of the BM smears with **Prussian blue stain** show **ringed sideroblast** in the erythroblast.",
    "Usually Sideroblastic anemia is usually diagnosed when **15% or more** of marrow erythroblast show sideroblast."],
   ["**فقر دم خفيف إلى متوسط** مع مستوى `Hb` بين **4–10** (مكتوبة في الأصل `mg/dl`).", "تُظهر المسحة صورة دم **ناقصة الصباغ** وأحيانًا **تنقّطًا قاعديًا**.",
    "**يرتفع حديد المصل وفيريتين المصل.**", "**`TIBC` طبيعي أو منخفض.**",
    "يُظهر النخاع **فرط تنسّج حمري**، ويُظهر تصبيغ مسحات النخاع بصبغة **أزرق بروسيا** **أرومات حديدية حلقية** في الأرومات الحمر.",
    "ويُشخَّص فقر الدم الحديدي الأرومات عادةً عندما تُظهر **15% أو أكثر** من أرومات النخاع الحمر أرومات حديدية."],
   en="**Laboratory findings:**", ar="**النتائج المختبرية:**"),
 N("The lecture writes the Hb range as **4-10 mg/dl**; haemoglobin is measured in **g/dl**.", "تكتب المحاضرة مدى الهيموغلوبين **4–10 mg/dl**؛ والهيموغلوبين يُقاس بـ **g/dl**.", label=["BIOS note", "ملاحظة بايوس"]),

 SEC("Lead poisoning", "التسمّم بالرصاص"),
 C(["**Lead inhibits both haem and globin synthesis** at a number of points,",
    "in addition it interferes with **breakdown of RNA** by inhibiting the enzymes **pyrimidine 5 nucleotidase** , causing **accumulation of denatured RNA** in the red cells."],
   ["**يثبّط الرصاص تخليق الهيم والكلوبين كليهما** في عدد من النقاط،",
    "إضافةً إلى أنه يتداخل مع **تحلّل الـ`RNA`** بتثبيط إنزيم **بيريميدين 5-نيوكليوتيديز**، مسبّبًا **تراكم `RNA` متغيّر الطبيعة** في الكريات الحمر."]),

 T(["", "Iron deficiency", "Chronic disorders", "Sideroblastic"],
   [["Serum iron", "↓", "↓", "↑"], ["TIBC", "↑", "↓", "Normal or ↓"], ["Serum ferritin", "↓", "Normal or ↑", "↑"],
    ["sTfR", "↑", "Normal", "—"], ["Marrow iron", "Absent", "Normal (erythroblast iron ↓)", "↑ with ringed sideroblasts"]],
   key_cols=[0], style="summary", label_en="Compare (lectures 6–7)", label_ar="مقارنة (المحاضرتان 6–7)"),
]

mcq = [
 {"topic_en": "Anaemia of chronic disorders", "topic_ar": "فقر دم الاضطرابات المزمنة"},
 Q("Anaemia of chronic disorders occurs with:", "يحدث فقر دم الاضطرابات المزمنة مع:", [("Acute bleeding", "النزف الحاد"), ("Chronic infections, inflammation and malignancy", "العدوى والالتهاب والخباثة المزمنة"), ("Vitamin B12 deficiency", "نقص B12"), ("Pregnancy only", "الحمل فقط")], "b"),
 Q("Anaemia of chronic disorders is corrected by:", "يُصحَّح فقر دم الاضطرابات المزمنة بـ:", [("Iron therapy", "العلاج بالحديد"), ("Vitamin B12", "فيتامين B12"), ("Successful treatment of the underlying disease", "علاج المرض الأساسي بنجاح"), ("Blood transfusion only", "نقل الدم فقط")], "c"),
 Q("A non-infectious cause of anaemia of chronic disorders is:", "سبب غير معدٍ لفقر دم الاضطرابات المزمنة:", [("Tuberculosis", "التدرّن"), ("Osteomyelitis", "التهاب العظم والنقي"), ("Pulmonary abscess", "خرّاج الرئة"), ("Rheumatoid arthritis", "التهاب المفاصل الرثياني")], "d"),
 Q("In anaemia of chronic disorders, haemoglobin is rarely less than:", "في فقر دم الاضطرابات المزمنة نادرًا ما يقل الهيموغلوبين عن:", [("9.0 g/dl", "9.0 غ/دل"), ("12 g/dl", "12 غ/دل"), ("4 g/dl", "4 غ/دل"), ("6 g/dl", "6 غ/دل")], "a"),
 Q("In anaemia of chronic disorders, serum iron and TIBC are:", "في فقر دم الاضطرابات المزمنة يكون حديد المصل وTIBC:", [("Both raised", "كلاهما مرتفع"), ("Both reduced", "كلاهما منخفض"), ("Iron low, TIBC high", "الحديد منخفض وTIBC مرتفع"), ("Both normal", "كلاهما طبيعي")], "b"),
 Q("Serum ferritin in anaemia of chronic disorders is:", "فيريتين المصل في فقر دم الاضطرابات المزمنة:", [("Absent", "غائب"), ("Decreased", "منخفض"), ("Normal or raised", "طبيعي أو مرتفع"), ("Very low", "منخفض جدًا")], "c"),
 Q("In anaemia of chronic disorders, bone marrow shows:", "في فقر دم الاضطرابات المزمنة يُظهر النخاع:", [("Absent iron stores", "غياب مخزون الحديد"), ("Ringed sideroblasts", "أرومات حديدية حلقية"), ("Megaloblasts", "أرومات ضخمة"), ("Normal iron stores but reduced erythroblast iron", "مخزونًا طبيعيًا لكن حديد الأرومات منخفض")], "d"),
 Q("The cytokine that raises hepcidin in anaemia of chronic disorders is mainly:", "السيتوكين الذي يرفع الهبسيدين في فقر دم الاضطرابات المزمنة أساسًا:", [("IL6", "IL6"), ("IL2", "IL2"), ("IL4", "IL4"), ("IL10", "IL10")], "a"),
 Q("Hepcidin causes anaemia by:", "يسبّب الهبسيدين فقر الدم عن طريق:", [("Destroying red cells", "تحطيم الكريات الحمر"), ("Blocking B12 absorption", "منع امتصاص B12"), ("Stopping ferroportin from releasing iron stores", "منع الفيروبورتين من تحرير مخازن الحديد"), ("Increasing erythropoietin", "زيادة الإريثروبويتين")], "c"),
 Q("Anaemia in renal failure is mainly due to:", "فقر الدم في الفشل الكلوي يعود أساسًا إلى:", [("Iron excess", "زيادة الحديد"), ("Decreased erythropoietin production", "انخفاض إنتاج الإريثروبويتين"), ("Haemolysis", "الانحلال"), ("Folate deficiency", "نقص الفولات")], "b"),
 {"topic_en": "Sideroblastic anaemia and lead", "topic_ar": "فقر الدم الحديدي الأرومات والرصاص"},
 Q("In sideroblastic anaemia, iron accumulates in the:", "في فقر الدم الحديدي الأرومات يتراكم الحديد في:", [("Nucleus", "النواة"), ("Plasma", "البلازما"), ("Liver only", "الكبد فقط"), ("Perinuclear mitochondria of normoblasts", "المايتوكوندريا المحيطة بنواة الأرومة السوية")], "d"),
 Q("Sideroblastic anaemia is defined by the presence of:", "يُعرَّف فقر الدم الحديدي الأرومات بوجود:", [("Ringed sideroblasts in the bone marrow", "أرومات حديدية حلقية في النخاع"), ("Target cells", "خلايا هدفية"), ("Spherocytes", "كريات كروية"), ("Hypersegmented neutrophils", "عدلات مفرطة التفصّص")], "a"),
 Q("Primary acquired sideroblastic anaemia is associated with:", "يرتبط فقر الدم الحديدي الأرومات المكتسب الأولي بـ:", [("Alcoholism", "الكحول"), ("Anti-TB drugs", "مضادات التدرّن"), ("Myelodysplasia type 2", "خلل التنسّج النقوي النوع 2"), ("Lead poisoning", "التسمّم بالرصاص")], "c"),
 Q("A secondary cause of sideroblastic anaemia is:", "سبب ثانوي لفقر الدم الحديدي الأرومات:", [("Lead poisoning", "التسمّم بالرصاص"), ("Iron deficiency", "نقص الحديد"), ("Vitamin C", "فيتامين C"), ("Pregnancy", "الحمل")], "a"),
 Q("Hereditary sideroblastic anaemia may be inherited as:", "قد يورَّث فقر الدم الحديدي الأرومات الوراثي بشكل:", [("Y-linked only", "مرتبط بـ Y فقط"), ("Mitochondrial only", "مايتوكوندري فقط"), ("X-linked, AD or AR", "مرتبط بـ X، أو جسمي سائد أو متنحٍّ"), ("Not inherited", "غير وراثي")], "c"),
 Q("In sideroblastic anaemia, serum iron and ferritin are:", "في فقر الدم الحديدي الأرومات يكون حديد المصل والفيريتين:", [("Decreased", "منخفضين"), ("Increased", "مرتفعين"), ("Absent", "غائبين"), ("Normal", "طبيعيين")], "b"),
 Q("Ringed sideroblasts are shown with which stain?", "تُظهر الأرومات الحديدية الحلقية بأي صبغة؟", [("Giemsa", "كيمزا"), ("Gram", "كرام"), ("Ziehl–Neelsen", "زيل–نيلسن"), ("Prussian blue", "أزرق بروسيا")], "d"),
 Q("Sideroblastic anaemia is diagnosed when ringed sideroblasts are at least:", "يُشخَّص فقر الدم الحديدي الأرومات عندما تكون الأرومات الحلقية على الأقل:", [("15% of marrow erythroblasts", "15% من أرومات النخاع الحمر"), ("1%", "1%"), ("50%", "50%"), ("90%", "90%")], "a"),
 Q("The blood film in sideroblastic anaemia may show:", "قد تُظهر المسحة في فقر الدم الحديدي الأرومات:", [("Macrocytes only", "كريات كبيرة فقط"), ("Normal cells", "خلايا طبيعية"), ("Hypochromic cells and basophilic stippling", "خلايا ناقصة الصباغ وتنقّطًا قاعديًا"), ("Sickle cells", "خلايا منجلية")], "c"),
 Q("Lead inhibits which enzyme causing accumulation of denatured RNA?", "يثبّط الرصاص أي إنزيم مسبّبًا تراكم RNA متغيّر الطبيعة؟", [("ALA synthase", "ALA synthase"), ("Pyrimidine 5′-nucleotidase", "بيريميدين 5-نيوكليوتيديز"), ("G6PD", "G6PD"), ("Catalase", "الكاتاليز")], "b"),
 Q("Lead inhibits:", "يثبّط الرصاص:", [("Haem synthesis only", "تخليق الهيم فقط"), ("Globin synthesis only", "تخليق الكلوبين فقط"), ("Iron absorption only", "امتصاص الحديد فقط"), ("Both haem and globin synthesis", "تخليق الهيم والكلوبين كليهما")], "d"),
]
tf = [
 TF("Anaemia of chronic disorders responds well to iron therapy.", "يستجيب فقر دم الاضطرابات المزمنة جيدًا للعلاج بالحديد.", "F"),
 TF("Reduced red cell lifespan contributes to anaemia of chronic disorders.", "يسهم قِصَر عمر الكريات في فقر دم الاضطرابات المزمنة.", "T"),
 TF("Lymphoma can cause anaemia of chronic disorders.", "قد تسبّب اللمفوما فقر دم الاضطرابات المزمنة.", "T"),
 TF("In anaemia of chronic disorders, sTfR receptors are increased.", "في فقر دم الاضطرابات المزمنة ترتفع مستقبلات sTfR.", "F"),
 TF("Inflammatory cytokines cause fewer stem cells to differentiate to red cells.", "تجعل السيتوكينات الالتهابية عددًا أقل من الخلايا الجذعية يتمايز إلى كريات حمر.", "T"),
 TF("In sideroblastic anaemia the body lacks iron.", "في فقر الدم الحديدي الأرومات يفتقر الجسم إلى الحديد.", "F"),
 TF("Sideroblastic anaemia is a refractory anaemia with increased marrow iron.", "فقر الدم الحديدي الأرومات معنّد مع زيادة حديد النخاع.", "T"),
 TF("Hepatosplenomegaly may occur in sideroblastic anaemia.", "قد يحدث تضخّم الكبد والطحال في فقر الدم الحديدي الأرومات.", "T"),
 TF("Iron accumulation may damage the heart, liver, kidney and endocrine organs.", "قد يضرّ تراكم الحديد بالقلب والكبد والكلية والغدد الصمّاء.", "T"),
 TF("In sideroblastic anaemia, TIBC is markedly increased.", "في فقر الدم الحديدي الأرومات يرتفع TIBC بشدّة.", "F"),
 TF("Anti-TB drugs may cause secondary sideroblastic anaemia.", "قد تسبّب أدوية مضادات التدرّن فقر دم حديدي أرومات ثانويًا.", "T"),
 TF("Lead interferes with breakdown of RNA in red cells.", "يتداخل الرصاص مع تحلّل الـ RNA في الكريات الحمر.", "T"),
]
traps = [
 TR("Chronic disorders vs iron deficiency — TIBC and ferritin", "الاضطرابات المزمنة مقابل نقص الحديد — TIBC والفيريتين", "Chronic disorders: iron ↓, TIBC ↓, ferritin normal/↑, sTfR normal. IDA: iron ↓, TIBC ↑, ferritin ↓, sTfR ↑.", "المزمنة: الحديد ↓، TIBC ↓، الفيريتين طبيعي/↑، sTfR طبيعي. نقص الحديد: الحديد ↓، TIBC ↑، الفيريتين ↓، sTfR ↑."),
 TR("Marrow iron in the three anaemias", "حديد النخاع في أنواع فقر الدم الثلاثة", "IDA: absent. Chronic disorders: normal stores, erythroblast iron reduced. Sideroblastic: increased with ringed sideroblasts.", "نقص الحديد: غائب. المزمنة: مخزون طبيعي وحديد الأرومات منخفض. الحديدي الأرومات: مرتفع مع أرومات حلقية."),
 TR("Primary vs secondary acquired sideroblastic", "المكتسب الأولي مقابل الثانوي (الحديدي الأرومات)", "Primary: myelodysplasia type 2. Secondary: marrow malignancy (lymphoma, myeloma), anti-TB drugs, lead, alcohol.", "الأولي: خلل التنسّج النقوي 2. الثانوي: خباثات النخاع (لمفوما، ورم نقوي)، مضادات التدرّن، الرصاص، الكحول."),
 TR("Hepcidin and ferroportin", "الهبسيدين والفيروبورتين", "IL6 → liver makes hepcidin → hepcidin stops ferroportin releasing iron from stores.", "IL6 ← يصنع الكبد الهبسيدين ← يمنع الهبسيدين الفيروبورتين من تحرير الحديد المخزون."),
 TR("What does lead do?", "ماذا يفعل الرصاص؟", "Inhibits haem AND globin synthesis, and pyrimidine 5′-nucleotidase → denatured RNA accumulates (basophilic stippling).", "يثبّط تخليق الهيم والكلوبين، وإنزيم بيريميدين 5-نيوكليوتيديز ← تراكم RNA متغيّر (التنقّط القاعدي)."),
]
important = [
 IM("Describe the pathogenesis and causes of anaemia of chronic disorders.", "صف إمراضية فقر دم الاضطرابات المزمنة وأسبابه.", "Decreased release of iron from macrophages, reduced red cell lifespan and inadequate erythropoietin response; corrected only by treating the disease, no response to iron. Causes: chronic infections (lung abscess, TB, osteomyelitis), non-infectious inflammation (RA, SLE), malignancy (carcinoma, sarcoma, lymphoma).", "انخفاض تحرير الحديد من البلاعم، وقِصَر عمر الكريات، وضعف استجابة الإريثروبويتين؛ ولا يُصحَّح إلا بعلاج المرض، ولا يستجيب للحديد. أسبابه: العدوى المزمنة (خرّاج الرئة، التدرّن، التهاب العظم)، الالتهاب غير المعدي (الرثياني، الذئبة)، الخباثات (السرطانة، الساركوما، اللمفوما)."),
 IM("List the characteristic features of anaemia of chronic disorders.", "عدّد السمات المميِّزة لفقر دم الاضطرابات المزمنة.", "Normochromic normocytic or mildly hypochromic; mild non-progressive (Hb rarely < 9 g/dl); serum iron and TIBC reduced, sTfR normal; ferritin normal or raised; marrow stores normal but erythroblast iron reduced.", "سوي الصباغ سوي الكريات أو ناقص الصباغ قليلًا؛ خفيف غير متقدّم (Hb نادرًا < 9)؛ حديد المصل وTIBC منخفضان وsTfR طبيعي؛ الفيريتين طبيعي أو مرتفع؛ مخزون النخاع طبيعي وحديد الأرومات منخفض."),
 IM("Explain the mechanisms of anaemia of chronic disorders.", "اشرح آليات فقر دم الاضطرابات المزمنة.", "(1) IL6 → hepcidin → ferroportin blocked, iron stays in stores; (2) cytokines favour WBC so fewer stem cells become red cells; (3) renal failure lowers erythropoietin; (4) some drugs inhibit erythropoiesis.", "(1) IL6 ← الهبسيدين ← يُحجب الفيروبورتين فيبقى الحديد مخزونًا؛ (2) تفضّل السيتوكينات الكريات البيض فيقل تمايز الجذعية إلى حمر؛ (3) الفشل الكلوي يُنقص الإريثروبويتين؛ (4) بعض الأدوية تثبّط التكوين."),
 IM("Define sideroblastic anaemia and give its classification.", "عرّف فقر الدم الحديدي الأرومات واذكر تصنيفه.", "A heterogeneous group with abnormal haem synthesis: adequate iron that cannot be incorporated, accumulating in perinuclear mitochondria (ringed sideroblasts). Hereditary (X-linked, AD, AR); acquired primary (myelodysplasia type 2) or secondary (marrow malignancy, anti-TB drugs, lead, alcohol).", "مجموعة غير متجانسة بتخليق هيم غير طبيعي: حديد كافٍ لا يدخل الهيموغلوبين فيتراكم في المايتوكوندريا حول النواة (أرومات حلقية). وراثي (مرتبط بـ X، سائد، متنحٍّ)؛ مكتسب أولي (خلل التنسّج 2) أو ثانوي (خباثات النخاع، مضادات التدرّن، الرصاص، الكحول)."),
 IM("Give the laboratory findings of sideroblastic anaemia.", "اذكر النتائج المختبرية لفقر الدم الحديدي الأرومات.", "Mild–moderate anaemia (Hb 4–10); hypochromic film, sometimes basophilic stippling; serum iron and ferritin increased; TIBC normal or decreased; marrow erythroid hyperplasia; Prussian blue shows ringed sideroblasts; diagnosed when ≥ 15% of erythroblasts are ringed sideroblasts.", "فقر دم خفيف–متوسط (Hb 4–10)؛ مسحة ناقصة الصباغ وأحيانًا تنقّط قاعدي؛ ارتفاع حديد المصل والفيريتين؛ TIBC طبيعي أو منخفض؛ فرط تنسّج حمري؛ أزرق بروسيا يُظهر الأرومات الحلقية؛ ويُشخَّص عند ≥ 15% من الأرومات."),
]
save("hematology-lec7-chronic-sideroblastic", 7, "Anaemia of chronic disorders, Sideroblastic anemia and Lead poisoning", "فقر دم الأمراض المزمنة وفقر الدم الحديدي الأرومات والتسمّم بالرصاص", blocks, mcq, tf, traps, important)

```
