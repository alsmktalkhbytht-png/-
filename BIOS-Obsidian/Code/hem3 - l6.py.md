---
source: BIOS-Obsidian/tools/scripts/hem3/l6.py
handouts: [hematology-lec6-iron-deficiency]
saved: 2026-10-30
tags: [bios, code]
---
# hem3/l6.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#hematology-lec6-iron-deficiency|hematology-lec6-iron-deficiency]]

```python
from common import *

blocks = [
 SEC("Microcytic hypochromic anaemia", "فقر الدم صغير الكريات ناقص الصباغ"),
 C("It results from **defect in hemoglobin synthesis**.", "ينتج عن **خلل في تخليق الهيموغلوبين**."),
 T(["Component", "Defect leads to", "المكوّن — الخلل يؤدي إلى"],
   [["Iron", "Iron deficiency Anaemia, chronic Inflammation or Malignancy.", "**الحديد**: فقر الدم بنقص الحديد، الالتهاب المزمن أو الخباثة."],
    ["Protoporphyrin", "(defect in protoporphyrin synthesis)", "**البروتوبورفيرين**: (خلل في تخليق البروتوبورفيرين)"],
    ["Iron + Protoporphyrin → Haem", "", "**الحديد + البروتوبورفيرين ← الهيم**"],
    ["Goblin (globin)", "Thalassemias (alpha or Beta)", "**الكلوبين**: الثلاسيميا (ألفا أو بيتا)"],
    ["Haem + Goblin → Hemoglobin", "", "**الهيم + الكلوبين ← الهيموغلوبين**"]],
   ar_cols=[2], key_cols=[0]),
 C("So the defect could be either in **iron** or in **goblin chain synthesis** or in **Protoporphyrin Synthesis**, all these defects lead to **microcytic hypochromic anaemia**.",
   "لذلك قد يكون الخلل في **الحديد** أو في **تخليق سلاسل الكلوبين** أو في **تخليق البروتوبورفيرين**، وكل هذه الأخطاء تؤدي إلى **فقر دم صغير الكريات ناقص الصباغ**."),

 SEC("Iron deficiency anemia (IDA)", "فقر الدم بنقص الحديد"),
 L(["**The commonest anaemia.**",
    "It results from failure of production of adequate number of red blood cells due to **lack of iron** which is essential for hemoglobin synthesis.",
    "In normal adult, about **2/3 of body iron** is in form of **circulating hemoglobin**.",
    "**Total body iron is about 3-5 gm.**",
    "The remaining **1/3** of iron is present in form of certain enzyme like **Cytochromes, Catalase ,Peroxides** and some are present in the body stored in **reticuloendothelial system** especially macrophage of bone marrow and liver.",
    "The form of iron present in store is **ferritin and haemosidrin**. The **haemosidrin is the stainable iron** in the tissues.",
    "Normal **daily intake** of iron is **10 mg** in average diet from which only **5-10%** is absorbed.",
    "Normal **daily loss** of iron is **1 mg**, the loss usually occurs through GIT mucosa, urinary system, sweating, nail and hair."],
   ["**أكثر أنواع فقر الدم شيوعًا.**",
    "ينتج عن الفشل في إنتاج عدد كافٍ من الكريات الحمر بسبب **نقص الحديد** الضروري لتخليق الهيموغلوبين.",
    "عند البالغ الطبيعي يكون نحو **ثلثي حديد الجسم** بشكل **هيموغلوبين دائر**.",
    "**الحديد الكلي في الجسم نحو 3–5 غم.**",
    "ويوجد **الثلث** المتبقي بشكل إنزيمات مثل **السايتوكرومات والكاتاليز والبيروكسيديز**، وبعضه مخزون في **الجهاز الشبكي البطاني** ولا سيما بلاعم نخاع العظم والكبد.",
    "وشكل الحديد المخزون هو **الفيريتين والهيموسيدرين**. و**الهيموسيدرين هو الحديد القابل للتصبيغ** في الأنسجة.",
    "**المدخول اليومي** الطبيعي من الحديد **10 ملغم** في الغذاء المعتاد، يُمتص منه **5–10%** فقط.",
    "**الفقدان اليومي** الطبيعي **1 ملغم**، ويحدث عادةً عبر مخاطية القناة الهضمية، والجهاز البولي، والتعرّق، والأظافر، والشعر."]),

 SEC("Iron Absorption and metabolism", "امتصاص الحديد واستقلابه"),
 L(["Normal western diet contains **10-15 mg** of iron from which only **5-10 %** is normally absorbed.",
    "The proportion can be increased to **20-30 %** in **iron deficiency or pregnancy**.",
    "Iron absorption occurs through the **duodenum** and less through jejunum."],
   ["يحتوي الغذاء الغربي الطبيعي على **10–15 ملغم** حديد يُمتص منه عادةً **5–10%** فقط.",
    "ويمكن أن ترتفع النسبة إلى **20–30%** في **نقص الحديد أو الحمل**.",
    "ويحدث امتصاص الحديد في **الاثني عشري** وبدرجة أقل في الصائم."], en="**Absorption of iron:**", ar="**امتصاص الحديد:**"),
 T(["Factors favoring absorption", "Factors reducing absorption", "الترجمة (يزيد ← يقلّل)"],
   [["1. Ferrous form (Fe +2)", "1. Ferric form (Fe+3)", "الحديدوز `Fe²⁺` ← الحديديك `Fe³⁺`"],
    ["2. Inorganic iron.", "2. Organic irons.", "الحديد غير العضوي ← الحديد العضوي"],
    ["3. Acids, vitamin C.", "3. Antacids, alkali.", "الحوامض وفيتامين `C` ← مضادات الحموضة والقلويات"],
    ["4. Iron deficiency.", "4. Iron excess.", "نقص الحديد ← زيادة الحديد"],
    ["5. Pregnancy.", "5. Infection.", "الحمل ← العدوى"],
    ["6. Primary haemchromatosis.", "6. Tea.", "داء ترسّب الأصبغة الدموية الأولي ← الشاي"]],
   ar_cols=[2]),

 SEC("Causes of iron deficiency anaemia", "أسباب فقر الدم بنقص الحديد"),
 R("**Chronic blood loss** (GIT, uterine, urinary, etc).", "**الفقدان المزمن للدم** (القناة الهضمية، الرحم، الجهاز البولي، إلخ)."),
 R("**Increase physiological demand** (growth period, pregnancy, lactation, menstruation).", "**زيادة الحاجة الفسيولوجية** (فترة النمو، الحمل، الإرضاع، الحيض)."),
 R("**Impaired absorption** of iron e.g. lesion in GIT like gastrectomy.", "**ضعف امتصاص** الحديد مثل آفة في القناة الهضمية كاستئصال المعدة."),
 R("**Inadequate intake** of iron (poor diet).", "**عدم كفاية المدخول** من الحديد (غذاء فقير)."),

 SEC("Clinical features", "المظاهر السريرية"),
 L(["Signs and symptoms of anaemia.", "Painless **glossities**, **angular stomatitis**, brittle and ridged or **spoon nails (koilonychias)**,",
    "**Dysphagia** due to **pharyngeal webs** (**Paterson-Kelly or Plummer-Vinson syndrome**) And unusual dietary cravings (**pica**)."],
   ["علامات فقر الدم وأعراضه.", "**التهاب اللسان** غير المؤلم، و**التهاب زاوية الفم**، والأظافر الهشّة المحزّزة أو **الملعقية (تقعّر الأظافر)**،",
    "**عسر البلع** بسبب **الأغشية البلعومية** (**متلازمة باترسون–كيلي أو بلامر–فينسون**)، والرغبات الغذائية غير المعتادة (**القَطَا** `pica`)."]),

 SEC("Laboratory findings", "النتائج المختبرية"),
 L(["**Decrease** Hb, PCV, RBCs, MCV, MCH, MCHC.", "Blood film will show: **Hypochromic microcytic** anaemia.",
    "**Anisocytosis** (i.e. differences in size of cells)", "**Poikilocytosis** (i.e. differences in shape of cells)",
    "**Target cells and pencil shaped cells.**", "WBC is variable.", "**Platelets usually increase.**"],
   ["**انخفاض** `Hb` و`PCV` و`RBC` و`MCV` و`MCH` و`MCHC`.", "تُظهر المسحة: فقر دم **ناقص الصباغ صغير الكريات**.",
    "**تفاوت حجم الكريات** (أي اختلاف أحجام الخلايا)", "**تشوّه شكل الكريات** (أي اختلاف أشكال الخلايا)",
    "**الخلايا الهدفية والخلايا قلمية الشكل.**", "الكريات البيض متغيّرة.", "**الصفيحات تزداد عادةً.**"], en="**1. Red cell indices and blood film:**", ar="**1. مؤشّرات الكريات والمسحة الدموية:**"),
 L(["**Erythrocytic hyperplasia** with **micronormoblastic** maturation.", "**Depleted iron store** usually there is **complete absences of iron** from stores."],
   ["**فرط تنسّج الخط الحمري** مع نضج **بأرومات سوية صغيرة**.", "**نفاد مخزون الحديد**، وعادةً **يغيب الحديد كليًا** من المخازن."],
   en="**2. Bone marrow aspirates and iron storage:**", ar="**2. رشافة نخاع العظم ومخزون الحديد:**"),
 R("**Serum iron and total iron binding capacity:** Usually there is **decrease serum iron** and **increase total iron binding capacity**.",
   "**حديد المصل والسعة الكلية لربط الحديد:** عادةً **ينخفض حديد المصل** و**ترتفع السعة الكلية لربط الحديد**."),
 R("**Serum ferritin is decrease.**", "**ينخفض فيريتين المصل.**"),
 R("**Serum transferrine receptors:** The level of these receptors is **increased in iron deficiency anaemia** but **not in anaemia of chronic diseases or thalassemia trait**.",
   "**مستقبلات الترانسفيرين في المصل:** يرتفع مستواها **في فقر الدم بنقص الحديد** لكن **ليس في فقر دم الأمراض المزمنة ولا في سمة الثلاسيميا**."),
 T(["Test", "In IDA", "الفحص — في نقص الحديد"],
   [["Serum iron", "↓", "حديد المصل ↓"], ["TIBC", "↑", "السعة الكلية لربط الحديد ↑"], ["Serum ferritin", "↓", "الفيريتين ↓"],
    ["Serum transferrin receptors", "↑", "مستقبلات الترانسفيرين ↑"], ["Marrow iron stores", "Absent", "مخزون حديد النخاع: غائب"], ["Platelets", "Usually ↑", "الصفيحات: ترتفع عادةً"]],
   ar_cols=[2], key_cols=[0], style="summary", label_en="IDA at a glance", label_ar="نقص الحديد باختصار"),
]

mcq = [
 {"topic_en": "Iron and its body stores", "topic_ar": "الحديد ومخازنه في الجسم"},
 Q("The commonest anaemia is:", "أكثر أنواع فقر الدم شيوعًا:", [("Thalassaemia", "الثلاسيميا"), ("Iron deficiency anaemia", "فقر الدم بنقص الحديد"), ("Aplastic anaemia", "اللاتنسّجي"), ("Sideroblastic anaemia", "الحديدي الأرومات")], "b"),
 Q("Total body iron is about:", "الحديد الكلي في الجسم نحو:", [("3–5 g", "3–5 غم"), ("10–15 g", "10–15 غم"), ("300–500 mg", "300–500 ملغم"), ("1 g", "1 غم")], "a"),
 Q("About two-thirds of body iron is in the form of:", "نحو ثلثي حديد الجسم بشكل:", [("Ferritin", "الفيريتين"), ("Cytochromes", "السايتوكرومات"), ("Circulating haemoglobin", "الهيموغلوبين الدائر"), ("Myoglobin", "المايوغلوبين")], "c"),
 Q("The stainable iron in the tissues is:", "الحديد القابل للتصبيغ في الأنسجة هو:", [("Ferritin", "الفيريتين"), ("Transferrin", "الترانسفيرين"), ("Haem", "الهيم"), ("Haemosiderin", "الهيموسيدرين")], "d"),
 Q("The normal daily loss of iron is:", "الفقدان اليومي الطبيعي من الحديد:", [("1 mg", "1 ملغم"), ("10 mg", "10 ملغم"), ("5 mg", "5 ملغم"), ("0.1 mg", "0.1 ملغم")], "a"),
 Q("Of the dietary iron, normally only this proportion is absorbed:", "يُمتص عادةً من حديد الغذاء نسبة:", [("50%", "50%"), ("5–10%", "5–10%"), ("80%", "80%"), ("1%", "1%")], "b"),
 Q("In iron deficiency or pregnancy, absorption can increase to:", "في نقص الحديد أو الحمل يمكن أن يرتفع الامتصاص إلى:", [("5–10%", "5–10%"), ("50–60%", "50–60%"), ("20–30%", "20–30%"), ("90%", "90%")], "c"),
 Q("Iron is mainly absorbed in the:", "يُمتص الحديد أساسًا في:", [("Stomach", "المعدة"), ("Ileum", "اللفائفي"), ("Colon", "القولون"), ("Duodenum", "الاثني عشري")], "d"),
 {"topic_en": "Absorption factors and causes", "topic_ar": "عوامل الامتصاص والأسباب"},
 Q("Which factor favours iron absorption?", "أي عامل يزيد امتصاص الحديد؟", [("Ferric form", "الحديديك"), ("Tea", "الشاي"), ("Vitamin C", "فيتامين C"), ("Antacids", "مضادات الحموضة")], "c"),
 Q("Which factor reduces iron absorption?", "أي عامل يقلّل امتصاص الحديد؟", [("Tea", "الشاي"), ("Pregnancy", "الحمل"), ("Ferrous form", "الحديدوز"), ("Iron deficiency", "نقص الحديد")], "a"),
 Q("The best absorbed form of iron is:", "أفضل أشكال الحديد امتصاصًا:", [("Ferric (Fe³⁺)", "الحديديك (Fe³⁺)"), ("Ferrous (Fe²⁺)", "الحديدوز (Fe²⁺)"), ("Organic iron", "الحديد العضوي"), ("Haemosiderin", "الهيموسيدرين")], "b"),
 Q("The most common cause of IDA in the list is:", "أول أسباب فقر الدم بنقص الحديد في القائمة:", [("Chronic blood loss", "الفقدان المزمن للدم"), ("Excess intake", "زيادة المدخول"), ("Infection", "العدوى"), ("Haemolysis", "الانحلال")], "a"),
 Q("Gastrectomy causes iron deficiency by:", "يسبّب استئصال المعدة نقص الحديد بسبب:", [("Increased demand", "زيادة الحاجة"), ("Blood loss", "فقدان الدم"), ("Impaired absorption", "ضعف الامتصاص"), ("Poor diet", "سوء الغذاء")], "c"),
 {"topic_en": "Clinical and laboratory findings", "topic_ar": "النتائج السريرية والمختبرية"},
 Q("Dysphagia due to pharyngeal webs in IDA is called:", "عسر البلع بسبب الأغشية البلعومية في نقص الحديد يُسمّى:", [("Zollinger–Ellison", "زولنجر–إليسون"), ("Cushing syndrome", "متلازمة كوشينغ"), ("Pica", "القَطَا"), ("Plummer–Vinson (Paterson–Kelly) syndrome", "متلازمة بلامر–فينسون (باترسون–كيلي)")], "d"),
 Q("Unusual dietary cravings in IDA are called:", "الرغبات الغذائية غير المعتادة في نقص الحديد تُسمّى:", [("Pica", "القَطَا (pica)"), ("Glossitis", "التهاب اللسان"), ("Koilonychia", "تقعّر الأظافر"), ("Stomatitis", "التهاب الفم")], "a"),
 Q("Differences in the shape of red cells are called:", "اختلاف أشكال الكريات الحمر يُسمّى:", [("Anisocytosis", "تفاوت الحجم"), ("Poikilocytosis", "تشوّه الشكل"), ("Polychromasia", "تعدّد الصباغ"), ("Spherocytosis", "كثرة الكريات الكروية")], "b"),
 Q("In IDA, platelets are usually:", "في نقص الحديد تكون الصفيحات عادةً:", [("Decreased", "منخفضة"), ("Absent", "غائبة"), ("Increased", "مرتفعة"), ("Giant", "عملاقة")], "c"),
 Q("In IDA, serum iron and TIBC are:", "في نقص الحديد يكون حديد المصل وTIBC:", [("Both increased", "كلاهما مرتفع"), ("Both decreased", "كلاهما منخفض"), ("Iron increased, TIBC decreased", "الحديد مرتفع وTIBC منخفض"), ("Iron decreased, TIBC increased", "الحديد منخفض وTIBC مرتفع")], "d"),
 Q("Serum ferritin in IDA is:", "فيريتين المصل في نقص الحديد:", [("Decreased", "منخفض"), ("Increased", "مرتفع"), ("Normal", "طبيعي"), ("Variable", "متغيّر")], "a"),
 Q("Serum transferrin receptors are increased in:", "ترتفع مستقبلات الترانسفيرين في المصل في:", [("Anaemia of chronic disease", "فقر دم الأمراض المزمنة"), ("Thalassaemia trait", "سمة الثلاسيميا"), ("Iron deficiency anaemia", "فقر الدم بنقص الحديد"), ("All anaemias", "كل أنواع فقر الدم")], "c"),
 Q("Bone marrow in IDA shows:", "يُظهر نخاع العظم في نقص الحديد:", [("Increased iron stores", "زيادة مخزون الحديد"), ("Ringed sideroblasts", "أرومات حديدية حلقية"), ("Megaloblasts", "أرومات ضخمة"), ("Erythroid hyperplasia with micronormoblasts and absent iron stores", "فرط تنسّج حمري بأرومات صغيرة وغياب مخزون الحديد")], "d"),
 Q("Target cells and pencil cells in the blood film suggest:", "الخلايا الهدفية والقلمية في المسحة توحي بـ:", [("Iron deficiency anaemia", "فقر الدم بنقص الحديد"), ("Megaloblastic anaemia", "الأرومي الضخم"), ("Aplastic anaemia", "اللاتنسّجي"), ("Acute blood loss", "النزف الحاد")], "a"),
]
tf = [
 TF("Microcytic hypochromic anaemia results from a defect in haemoglobin synthesis.", "ينتج فقر الدم صغير الكريات ناقص الصباغ عن خلل في تخليق الهيموغلوبين.", "T"),
 TF("A defect in protoporphyrin synthesis gives a macrocytic anaemia.", "يعطي خلل تخليق البروتوبورفيرين فقر دم كبير الكريات.", "F"),
 TF("Ferritin and haemosiderin are storage forms of iron.", "الفيريتين والهيموسيدرين شكلا خزن الحديد.", "T"),
 TF("Iron stores are found mainly in macrophages of the bone marrow and liver.", "توجد مخازن الحديد أساسًا في بلاعم نخاع العظم والكبد.", "T"),
 TF("Average daily intake of iron is about 100 mg.", "متوسط المدخول اليومي من الحديد نحو 100 ملغم.", "F"),
 TF("Pregnancy increases iron absorption.", "يزيد الحمل امتصاص الحديد.", "T"),
 TF("Organic iron is absorbed better than inorganic iron.", "يُمتص الحديد العضوي أفضل من غير العضوي.", "F"),
 TF("Menstruation increases physiological iron demand.", "يزيد الحيض الحاجة الفسيولوجية للحديد.", "T"),
 TF("Koilonychia is a feature of iron deficiency.", "تقعّر الأظافر من مظاهر نقص الحديد.", "T"),
 TF("In IDA, MCHC is increased.", "في نقص الحديد يرتفع MCHC.", "F"),
 TF("Serum transferrin receptors are increased in thalassaemia trait.", "ترتفع مستقبلات الترانسفيرين في سمة الثلاسيميا.", "F"),
 TF("Iron stores are usually completely absent in IDA.", "يغيب مخزون الحديد عادةً كليًا في نقص الحديد.", "T"),
]
traps = [
 TR("Ferrous vs ferric for absorption", "الحديدوز مقابل الحديديك في الامتصاص", "Ferrous (Fe²⁺) favours absorption; ferric (Fe³⁺) reduces it. (Inorganic > organic in this lecture.)", "الحديدوز (Fe²⁺) يزيد الامتصاص؛ والحديديك (Fe³⁺) يقلّله. (غير العضوي > العضوي في هذه المحاضرة.)"),
 TR("Intake vs absorption vs loss", "المدخول مقابل الامتصاص مقابل الفقدان", "Intake 10 mg/day (western diet 10–15 mg), absorbed 5–10% (20–30% in deficiency/pregnancy), loss 1 mg/day.", "المدخول 10 ملغم/يوم (الغربي 10–15)، يُمتص 5–10% (20–30% في النقص/الحمل)، الفقدان 1 ملغم/يوم."),
 TR("Serum iron and TIBC move in opposite directions in IDA", "حديد المصل وTIBC يتحرّكان بعكس بعضهما في نقص الحديد", "Serum iron ↓, TIBC ↑, ferritin ↓, transferrin receptors ↑.", "حديد المصل ↓، TIBC ↑، الفيريتين ↓، مستقبلات الترانسفيرين ↑."),
 TR("Transferrin receptors — IDA vs chronic disease vs thalassaemia trait", "مستقبلات الترانسفيرين — نقص الحديد مقابل المزمن مقابل سمة الثلاسيميا", "Increased only in IDA, not in anaemia of chronic disease or thalassaemia trait.", "ترتفع في نقص الحديد فقط، لا في فقر دم الأمراض المزمنة ولا سمة الثلاسيميا."),
 TR("Anisocytosis vs poikilocytosis", "تفاوت الحجم مقابل تشوّه الشكل", "Anisocytosis = different sizes; poikilocytosis = different shapes.", "تفاوت الحجم = أحجام مختلفة؛ تشوّه الشكل = أشكال مختلفة."),
]
important = [
 IM("Explain why defects in iron, protoporphyrin or globin cause microcytic hypochromic anaemia.", "وضّح لماذا يسبّب خلل الحديد أو البروتوبورفيرين أو الكلوبين فقر دم صغير الكريات ناقص الصباغ.", "Haem = iron + protoporphyrin, and haemoglobin = haem + globin; a defect in any (iron deficiency/chronic inflammation/malignancy, protoporphyrin synthesis, or thalassaemia) impairs haemoglobin synthesis.", "الهيم = حديد + بروتوبورفيرين، والهيموغلوبين = هيم + كلوبين؛ وخلل أي منها (نقص الحديد/الالتهاب المزمن/الخباثة، تخليق البروتوبورفيرين، الثلاسيميا) يضعف تخليق الهيموغلوبين."),
 IM("Describe body iron distribution and balance.", "صف توزيع الحديد في الجسم وتوازنه.", "Total 3–5 g; 2/3 in circulating Hb; 1/3 in enzymes (cytochromes, catalase, peroxidase) and stores (ferritin, haemosiderin) in RES macrophages of marrow and liver. Intake 10 mg/day, 5–10% absorbed; loss 1 mg/day through GIT, urine, sweat, nails and hair.", "الكلي 3–5 غم؛ الثلثان في Hb الدائر؛ والثلث في الإنزيمات (السايتوكرومات، الكاتاليز، البيروكسيديز) والمخازن (الفيريتين، الهيموسيدرين) في بلاعم النخاع والكبد. المدخول 10 ملغم/يوم يُمتص 5–10%؛ والفقدان 1 ملغم/يوم عبر الهضمي والبول والعرق والأظافر والشعر."),
 IM("List the factors that favour and reduce iron absorption.", "عدّد العوامل التي تزيد امتصاص الحديد والتي تقلّله.", "Favour: ferrous form, inorganic iron, acids/vitamin C, iron deficiency, pregnancy, primary haemochromatosis. Reduce: ferric form, organic iron, antacids/alkali, iron excess, infection, tea.", "تزيد: الحديدوز، الحديد غير العضوي، الحوامض/فيتامين C، نقص الحديد، الحمل، داء ترسّب الأصبغة الأولي. تقلّل: الحديديك، العضوي، مضادات الحموضة/القلويات، زيادة الحديد، العدوى، الشاي."),
 IM("List the causes and clinical features of IDA.", "عدّد أسباب نقص الحديد ومظاهره السريرية.", "Causes: chronic blood loss, increased demand (growth, pregnancy, lactation, menstruation), impaired absorption (gastrectomy), poor intake. Features: anaemia, painless glossitis, angular stomatitis, koilonychia, dysphagia with pharyngeal webs (Plummer–Vinson), pica.", "الأسباب: الفقدان المزمن للدم، زيادة الحاجة (النمو، الحمل، الإرضاع، الحيض)، ضعف الامتصاص (استئصال المعدة)، قلّة المدخول. المظاهر: فقر الدم، التهاب اللسان، التهاب زاوية الفم، تقعّر الأظافر، عسر البلع مع الأغشية البلعومية (بلامر–فينسون)، القَطَا."),
 IM("Give the laboratory findings of IDA.", "اذكر النتائج المختبرية لنقص الحديد.", "Low Hb, PCV, RBC, MCV, MCH, MCHC; hypochromic microcytic film with anisocytosis, poikilocytosis, target and pencil cells; variable WBC; platelets usually up; marrow erythroid hyperplasia with micronormoblasts and absent iron; serum iron ↓, TIBC ↑, ferritin ↓, transferrin receptors ↑.", "انخفاض Hb وPCV وRBC وMCV وMCH وMCHC؛ مسحة ناقصة الصباغ صغيرة الكريات مع تفاوت الحجم والشكل وخلايا هدفية وقلمية؛ كريات بيض متغيّرة؛ الصفيحات ترتفع عادةً؛ النخاع فرط تنسّج حمري بأرومات صغيرة وغياب الحديد؛ حديد المصل ↓، TIBC ↑، الفيريتين ↓، مستقبلات الترانسفيرين ↑."),
]
save("hematology-lec6-iron-deficiency", 6, "Iron Deficiency anemia (IDA)", "فقر الدم بنقص الحديد", blocks, mcq, tf, traps, important)

```
