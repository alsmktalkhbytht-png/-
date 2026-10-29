---
source: BIOS-Obsidian/tools/scripts/hem3/l3.py
handouts: [hematology-lec3-blood-elements]
saved: 2026-10-29
tags: [bios, code]
---
# hem3/l3.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#hematology-lec3-blood-elements|hematology-lec3-blood-elements]]

```python
from common import *

blocks = [
 SEC("Erythrocyte production (Erythropoiesis)", "إنتاج الكريات الحمر (تكوين الكريات الحمر)"),
 FLOW([("Pronormoblast", "أرومة سوية أولية"), ("Normoblast (erythroblast)", "أرومة سوية (أرومة حمراء)"), ("Early erythroblast (basophilic)", "أرومة حمراء مبكرة (قاعدية)"),
       ("Intermediate erythroblast (polychromatic)", "أرومة حمراء وسطية (متعدّدة الألوان)"), ("Late erythroblast (pyknotic)", "أرومة حمراء متأخرة (متغلّظة النواة)"),
       ("Reticulocytes", "الخلايا الشبكية"), ("Red cells", "الكريات الحمر")]),
 C("During these developing stages, the erythrocytes passes through successive changes that involve:", "خلال مراحل النمو هذه، تمرّ الكريات الحمر بتغيّرات متتابعة تشمل:",
   list_en=["Progressive **diminution in cell size**.", "Progressive **reduction in nuclear size** with **condensation of the nuclear chromatin**.",
            "Progressive **loss of basophilic RNA** of the cytoplasm and concurrent **production of hemoglobin**."],
   list_ar=["**تناقص تدريجي في حجم الخلية**.", "**تناقص تدريجي في حجم النواة** مع **تكثّف الكروماتين النووي**.",
            "**فقدان تدريجي للـ`RNA` القاعدي** في السايتوبلازم مع **إنتاج الهيموغلوبين** في الوقت نفسه."]),
 C(["The **reticulocytes** is slightly larger than mature red cell and spend **1-2 days in bone marrow** then it released to the circulation after maturation to erythrocytes after **1-2 days**, when **RNA is lost in the spleen**.",
    "in normal blood the reticulocytes content is **0.2-2.0%**."],
   ["**الخلية الشبكية** أكبر قليلًا من الكرية الحمراء الناضجة، وتقضي **1–2 يوم في نخاع العظم** ثم تُطلق إلى الدوران وتنضج إلى كرية حمراء بعد **1–2 يوم**، عندما **تفقد الـ`RNA` في الطحال**.",
    "ونسبة الخلايا الشبكية في الدم الطبيعي **0.2–2.0%**."]),

 SEC("Red blood cells (Erythrocytes)", "كريات الدم الحمر"),
 C(["The normal mature red blood cells is a **flexible biconcave disc**, measuring about **6-8 µm** in diameter.",
    "The red cells in order to carry hemoglobin into closed contact with the tissues and for successful gaseous exchange, must be able to pass repeatedly through the **microcirculation whose minimum diameter is 3.5 µm**, to maintain hemoglobin in a **reduced (ferrous) state** and to maintain **osmotic equilibrium** despite the high concentration of protein (hemoglobin) in the cell."],
   ["الكرية الحمراء الناضجة الطبيعية **قرص مرن مقعّر الوجهين**، قطره نحو **6–8 مايكرومتر**.",
    "ولكي تنقل الكريات الحمر الهيموغلوبين إلى تماس قريب مع الأنسجة ولنجاح تبادل الغازات، يجب أن تستطيع المرور مرارًا عبر **الدوران الدقيق الذي يبلغ أصغر قطر فيه 3.5 مايكرومتر**، وأن تحافظ على الهيموغلوبين في **الحالة المختزلة (الحديدوزية)**، وأن تحافظ على **التوازن الأوزموزي** رغم التركيز العالي للبروتين (الهيموغلوبين) فيها."]),
 C(["Its total journey throughout its **120-day lifespan** that estimated to be **480 km. (300 miles)**.",
    "To fulfil these functions, the red cell is a flexible, biconcave disc with an ability to generate energy as **ATP by the anaerobic glycolytic pathway (Embden Meyerhof pathway)** and to generate reducing power as nicotinamide dihydroxylase (**NADH**) by this pathway and to reduced nicotinamide adenine dinucleotide phosphate (**NADPH**) by **hexose monophosphate shunt**. ."],
   ["وتُقدَّر رحلتها الكلية خلال **عمرها البالغ 120 يومًا** بنحو **480 كم (300 ميل)**.",
    "ولتؤدي هذه الوظائف، فالكرية الحمراء قرص مرن مقعّر الوجهين قادر على توليد الطاقة بشكل **`ATP` عبر مسار التحلّل السكري اللاهوائي (مسار إمبدن–مايرهوف)**، وتوليد قدرة اختزالية بشكل **`NADH`** عبر هذا المسار، و**`NADPH`** عبر **تحويلة الهكسوز أحادي الفوسفات**."]),
 C(["Normally only **late reticulocytes and mature erythrocytes** appear in the peripheral blood but in states of **erythropoietin induced increase** in red cells productions, **early reticulocytes and even normoblast** may enter the circulation.",
    "After release from the marrow, the normal red cells survives for about **120 days**, at the end of this time, the cell is **phagocytized by macrophage of reticule-endothelial system**."],
   ["في الحالة الطبيعية تظهر في الدم المحيطي **الخلايا الشبكية المتأخرة والكريات الحمر الناضجة** فقط، لكن في حالات **زيادة إنتاج الكريات الحمر بتحفيز الإريثروبويتين** قد تدخل الدوران **الخلايا الشبكية المبكرة بل والأرومات السوية**.",
    "وبعد إطلاقها من النخاع تعيش الكرية الحمراء الطبيعية نحو **120 يومًا**، وفي نهايتها **تبتلعها بلاعم الجهاز الشبكي البطاني**."]),

 SEC("Red Blood Cell Membrane", "غشاء الكرية الحمراء"),
 C(["Red cell blood membrane compromise of a **lipid bilayer, integral membrane proteins and membrane skeleton**.",
    "About **50%** of the membrane is **protein**, **40%** is **fat** and up to **10%** is **carbohydrate**."],
   ["يتكوّن غشاء الكرية الحمراء من **طبقة دهنية مزدوجة، وبروتينات غشائية مدمجة، وهيكل غشائي**.",
    "ونحو **50%** من الغشاء **بروتين**، و**40%** **دهن**، وحتى **10%** **كاربوهيدرات**."]),
 C(["The **membrane skeleton** formed by structural protein that include **spectrin, Ankyrin, protein 4.1 and actin**.",
    "These proteins formed the **horizontal network** on the internal side of the red cell membrane and are important to **maintain the biconcave shape** of red cell.",
    "Defect of the protein may explain some of the abnormalities of the shape of the red cell membrane e.g. **hereditary spherocytosis and elliptocytosis**."],
   ["يتكوّن **الهيكل الغشائي** من بروتينات بنائية تشمل **السبكترين، والأنكيرين، والبروتين 4.1، والأكتين**.",
    "وتكوّن هذه البروتينات **شبكة أفقية** على الجانب الداخلي لغشاء الكرية الحمراء، وهي مهمة **للمحافظة على الشكل المقعّر الوجهين**.",
    "وقد يفسّر خلل هذه البروتينات بعض تشوّهات شكل الكرية الحمراء، مثل **كثرة الكريات الكروية الوراثية وكثرة الكريات الإهليلجية**."]),

 SEC("Substances required for Erythropoiesis", "المواد اللازمة لتكوين الكريات الحمر"),
 C("Because of the very great number of new red cells that produced each day, the marrow requires many precursors to synthesize the new cells and the large amounts of hemoglobin. The following groups of substances needed:",
   "بسبب العدد الكبير جدًا من الكريات الحمر الجديدة التي تُنتج يوميًا، يحتاج النخاع إلى مواد أولية كثيرة لتخليق الخلايا الجديدة والكميات الكبيرة من الهيموغلوبين. والمجموعات اللازمة هي:"),
 T(["Group", "Substances", "المجموعة — المواد"],
   [["1. Metals", "Iron, Manganese and Cobalt.", "**الفلزات**: الحديد، المنغنيز، الكوبلت."],
    ["2. Vitamins", "Vitamin B12, B6, C, E and Folate.", "**الفيتامينات**: `B12` و`B6` و`C` و`E` وحمض الفوليك."],
    ["3. Amino acid", "—", "**الأحماض الأمينية**"],
    ["4. Hormones", "Erythropoietin, Androgen and Thyroxin.", "**الهرمونات**: الإريثروبويتين، الأندروجين، الثايروكسين."]],
   ar_cols=[2], key_cols=[0], widths=["28mm", "", ""]),

 SEC("Regulation of Erythropoiesis", "تنظيم تكوين الكريات الحمر"),
 C("The progressive differentiation and proliferation appear to be under the control of **erythropoietin** which is produce mainly in the **kidney (90%)** and possibly **10% in liver** and other organs.",
   "يبدو أن التمايز والتكاثر المتدرّجين تحت سيطرة **الإريثروبويتين** الذي يُنتج أساسًا في **الكلية (90%)** وربما **10% في الكبد** وأعضاء أخرى."),
 C(["When erythropoietin production acutely stimulated by **hypoxia** from any cause including **anaemia and hemorrhage**, there is a resultant **increase in the red cells**.",
    "Production in the other hand, **increased O2 supply** to the tissues because of increased red cell mass or because Hb ability to released O2 more readily than normal will **reduce the erythropoietin production**."],
   ["عندما يُحفَّز إنتاج الإريثروبويتين تحفيزًا حادًا بـ**نقص الأكسجة** لأي سبب ومنه **فقر الدم والنزف**، ينتج عن ذلك **زيادة في الكريات الحمر**.",
    "ومن ناحية أخرى، فإن **زيادة إمداد الأنسجة بالأوكسجين** بسبب زيادة كتلة الكريات الحمر أو لأن الهيموغلوبين يُطلق الأوكسجين بسهولة أكبر من الطبيعي **تُقلّل إنتاج الإريثروبويتين**."]),
 FLOW([("Hypoxia (anaemia, hemorrhage)", "نقص الأكسجة (فقر دم، نزف)"), ("↑ Erythropoietin", "↑ الإريثروبويتين"), ("↑ Red cells", "↑ الكريات الحمر")]),

 SEC("Tests of erythropoiesis", "فحوص تكوين الكريات الحمر"),
 C("We do many tests on peripheral blood to know if we have normal erythropoiesis or not. These tests include:",
   "نجري فحوصًا كثيرة على الدم المحيطي لنعرف إن كان تكوين الكريات الحمر طبيعيًا أم لا. وتشمل هذه الفحوص:"),
 T(["Test", "Male", "Female", "الفحص"],
   [["1. Hemoglobin level (Hb.)", "13.5-17.5 g/dl", "11.5-15.5 g/dl", "مستوى الهيموغلوبين"],
    ["2. Red blood cell count", "4.5-6.5 ×10¹²/L", "3.9-5.6 ×10¹²/L", "عدد الكريات الحمر"],
    ["3. Packed cell volume (pcv)", "40-52%", "36-48%", "حجم الخلايا المرصوصة (الهيماتوكريت)"]],
   ar_cols=[3], key_cols=[0]),
 C("The above three test results will help in calculation of **red blood cell indices** that include:", "تساعد نتائج الفحوص الثلاثة أعلاه في حساب **مؤشّرات الكريات الحمر**، وتشمل:"),
 T(["Index", "Normal", "المؤشّر"],
   [["1. MCV (Mean corpuscular volume)", "80-95 fl.", "متوسط حجم الكرية"],
    ["2. MCH (Mean corpuscular hemoglobin)", "27-34 pg.", "متوسط هيموغلوبين الكرية"],
    ["3. MCHC (Mean corpuscular hemoglobin concentration)", "20-35 g/dl.", "متوسط تركيز هيموغلوبين الكرية"]],
   ar_cols=[2], key_cols=[0]),
 C("Other tests you should do are the **blood film examination** to see the **RBC morphology**.", "ومن الفحوص الأخرى الواجب إجراؤها **فحص المسحة الدموية** لرؤية **شكل الكريات الحمر**."),
 N("The lecture gives MCHC as **20-35 g/dl**; most references give **30-35 g/dl**. Learn the lecture value for the exam and check with the doctor.",
   "تذكر المحاضرة `MCHC` بقيمة **20–35 غ/دل**؛ ومعظم المراجع تذكر **30–35 غ/دل**. احفظ قيمة المحاضرة للامتحان وتأكّد من الدكتور.", label=["BIOS note", "ملاحظة بايوس"]),
]

mcq = [
 {"topic_en": "Erythropoiesis and reticulocytes", "topic_ar": "تكوين الكريات الحمر والخلايا الشبكية"},
 Q("During erythroid maturation, cell size:", "أثناء نضج الخط الحمري، حجم الخلية:", [("Increases", "يزداد"), ("Progressively diminishes", "يتناقص تدريجيًا"), ("Stays the same", "يبقى ثابتًا"), ("Doubles", "يتضاعف")], "b"),
 Q("During maturation, the cytoplasm progressively loses:", "أثناء النضج يفقد السايتوبلازم تدريجيًا:", [("Haemoglobin", "الهيموغلوبين"), ("Iron", "الحديد"), ("Basophilic RNA", "الـ RNA القاعدي"), ("Membrane", "الغشاء")], "c"),
 Q("The reticulocyte loses its RNA in the:", "تفقد الخلية الشبكية الـ RNA في:", [("Liver", "الكبد"), ("Kidney", "الكلية"), ("Lymph nodes", "العقد اللمفاوية"), ("Spleen", "الطحال")], "d"),
 Q("The normal reticulocyte count in blood is:", "النسبة الطبيعية للخلايا الشبكية في الدم:", [("0.2–2.0%", "0.2–2.0%"), ("5–10%", "5–10%"), ("10–20%", "10–20%"), ("0%", "0%")], "a"),
 Q("The reticulocyte spends in the bone marrow about:", "تقضي الخلية الشبكية في النخاع نحو:", [("1–2 hours", "1–2 ساعة"), ("1–2 days", "1–2 يوم"), ("1–2 weeks", "1–2 أسبوع"), ("120 days", "120 يومًا")], "b"),
 {"topic_en": "The red cell", "topic_ar": "الكرية الحمراء"},
 Q("The diameter of a normal mature red cell is about:", "قطر الكرية الحمراء الناضجة الطبيعية نحو:", [("3.5 µm", "3.5 مايكرومتر"), ("12–15 µm", "12–15 مايكرومتر"), ("6–8 µm", "6–8 مايكرومتر"), ("20 µm", "20 مايكرومتر")], "c"),
 Q("The minimum diameter of the microcirculation is:", "أصغر قطر في الدوران الدقيق:", [("3.5 µm", "3.5 مايكرومتر"), ("6 µm", "6 مايكرومتر"), ("8 µm", "8 مايكرومتر"), ("1 µm", "1 مايكرومتر")], "a"),
 Q("The red cell lifespan is about:", "عمر الكرية الحمراء نحو:", [("7–10 days", "7–10 أيام"), ("30 days", "30 يومًا"), ("60 days", "60 يومًا"), ("120 days", "120 يومًا")], "d"),
 Q("The total journey of a red cell over its lifespan is estimated at:", "تُقدَّر رحلة الكرية الحمراء طوال عمرها بنحو:", [("48 km", "48 كم"), ("480 km (300 miles)", "480 كم (300 ميل)"), ("4800 km", "4800 كم"), ("100 km", "100 كم")], "b"),
 Q("The red cell generates ATP by:", "تولّد الكرية الحمراء الـ ATP عبر:", [("Oxidative phosphorylation", "الفسفرة التأكسدية"), ("The Krebs cycle", "دورة كريبس"), ("Anaerobic glycolysis (Embden–Meyerhof pathway)", "التحلّل السكري اللاهوائي (مسار إمبدن–مايرهوف)"), ("Beta-oxidation", "أكسدة بيتا")], "c"),
 Q("NADPH in the red cell is generated by the:", "يُولَّد الـ NADPH في الكرية الحمراء عبر:", [("Hexose monophosphate shunt", "تحويلة الهكسوز أحادي الفوسفات"), ("Embden–Meyerhof pathway", "مسار إمبدن–مايرهوف"), ("Urea cycle", "دورة اليوريا"), ("Mitochondria", "المايتوكوندريا")], "a"),
 Q("At the end of their life, red cells are phagocytized by:", "في نهاية عمرها تُبتلع الكريات الحمر بواسطة:", [("Neutrophils", "العدلات"), ("Platelets", "الصفيحات"), ("Lymphocytes", "اللمفاويات"), ("Macrophages of the reticuloendothelial system", "بلاعم الجهاز الشبكي البطاني")], "d"),
 Q("The red cell membrane is composed of about:", "يتكوّن غشاء الكرية الحمراء من نحو:", [("50% protein, 40% fat, up to 10% carbohydrate", "50% بروتين، 40% دهن، حتى 10% كاربوهيدرات"), ("80% fat, 20% protein", "80% دهن، 20% بروتين"), ("50% carbohydrate", "50% كاربوهيدرات"), ("100% protein", "100% بروتين")], "a"),
 Q("Which is NOT a membrane skeleton protein?", "أي مما يأتي ليس من بروتينات الهيكل الغشائي؟", [("Spectrin", "السبكترين"), ("Ankyrin", "الأنكيرين"), ("Haemoglobin", "الهيموغلوبين"), ("Actin", "الأكتين")], "c"),
 Q("Defects of membrane skeleton proteins explain:", "يفسّر خلل بروتينات الهيكل الغشائي:", [("Iron deficiency", "نقص الحديد"), ("Hereditary spherocytosis and elliptocytosis", "كثرة الكريات الكروية والإهليلجية الوراثية"), ("Thalassaemia", "الثلاسيميا"), ("Lead poisoning", "التسمّم بالرصاص")], "b"),
 {"topic_en": "Requirements, regulation and tests", "topic_ar": "المتطلّبات والتنظيم والفحوص"},
 Q("Which metal is NOT listed as required for erythropoiesis?", "أي فلز ليس من الفلزات اللازمة لتكوين الكريات الحمر؟", [("Iron", "الحديد"), ("Cobalt", "الكوبلت"), ("Manganese", "المنغنيز"), ("Lead", "الرصاص")], "d"),
 Q("Hormones required for erythropoiesis include:", "من الهرمونات اللازمة لتكوين الكريات الحمر:", [("Insulin and glucagon", "الإنسولين والكلوكاكون"), ("Erythropoietin, androgen and thyroxin", "الإريثروبويتين والأندروجين والثايروكسين"), ("Cortisol only", "الكورتيزول فقط"), ("Oestrogen only", "الإستروجين فقط")], "b"),
 Q("Erythropoietin production is stimulated by:", "يُحفَّز إنتاج الإريثروبويتين بـ:", [("Increased O2 supply", "زيادة إمداد الأوكسجين"), ("Increased red cell mass", "زيادة كتلة الكريات الحمر"), ("Hypoxia (anaemia, haemorrhage)", "نقص الأكسجة (فقر الدم، النزف)"), ("High altitude only", "الارتفاعات العالية فقط")], "c"),
 Q("The normal haemoglobin in females according to the lecture is:", "الهيموغلوبين الطبيعي عند الإناث بحسب المحاضرة:", [("11.5–15.5 g/dl", "11.5–15.5 غ/دل"), ("13.5–17.5 g/dl", "13.5–17.5 غ/دل"), ("8–10 g/dl", "8–10 غ/دل"), ("18–20 g/dl", "18–20 غ/دل")], "a"),
 Q("The normal PCV in males is:", "الـ PCV الطبيعي عند الذكور:", [("36–48%", "36–48%"), ("20–30%", "20–30%"), ("60–70%", "60–70%"), ("40–52%", "40–52%")], "d"),
 Q("The normal MCV is:", "الـ MCV الطبيعي:", [("27–34 fl", "27–34 fl"), ("80–95 fl", "80–95 fl"), ("100–120 fl", "100–120 fl"), ("50–60 fl", "50–60 fl")], "b"),
 Q("MCH normal range is:", "المدى الطبيعي لـ MCH:", [("80–95 pg", "80–95 pg"), ("10–15 pg", "10–15 pg"), ("27–34 pg", "27–34 pg"), ("40–50 pg", "40–50 pg")], "c"),
]
tf = [
 TF("The reticulocyte is slightly smaller than the mature red cell.", "الخلية الشبكية أصغر قليلًا من الكرية الحمراء الناضجة.", "F"),
 TF("Haemoglobin production increases as the erythroblast matures.", "يزداد إنتاج الهيموغلوبين مع نضج الأرومة الحمراء.", "T"),
 TF("The red cell must keep haemoglobin in the ferrous (reduced) state.", "يجب أن تحافظ الكرية الحمراء على الهيموغلوبين في الحالة الحديدوزية (المختزلة).", "T"),
 TF("Normoblasts may enter the circulation when erythropoietin drives production.", "قد تدخل الأرومات السوية الدوران عندما يحفّز الإريثروبويتين الإنتاج.", "T"),
 TF("Red cells live about 7–10 days.", "تعيش الكريات الحمر نحو 7–10 أيام.", "F"),
 TF("The membrane skeleton lies on the external side of the red cell membrane.", "يقع الهيكل الغشائي على الجانب الخارجي لغشاء الكرية الحمراء.", "F"),
 TF("Spectrin helps maintain the biconcave shape of the red cell.", "يساعد السبكترين في المحافظة على الشكل المقعّر الوجهين.", "T"),
 TF("Vitamin B12 and folate are needed for erythropoiesis.", "يحتاج تكوين الكريات الحمر إلى فيتامين B12 والفولات.", "T"),
 TF("Increased O2 supply to tissues increases erythropoietin production.", "زيادة إمداد الأنسجة بالأوكسجين تزيد إنتاج الإريثروبويتين.", "F"),
 TF("RBC indices are calculated from Hb, RBC count and PCV.", "تُحسب مؤشّرات الكريات الحمر من Hb وعدد الكريات وPCV.", "T"),
 TF("The blood film is used to see RBC morphology.", "تُستخدم المسحة الدموية لرؤية شكل الكريات الحمر.", "T"),
]
traps = [
 TR("Where does the reticulocyte lose RNA, and how long does it take?", "أين تفقد الخلية الشبكية الـ RNA وكم يستغرق ذلك؟", "1–2 days in the marrow, then 1–2 days in the circulation; RNA is lost in the spleen. Normal count 0.2–2.0%.", "1–2 يوم في النخاع ثم 1–2 يوم في الدوران؛ وتفقد الـ RNA في الطحال. النسبة الطبيعية 0.2–2.0%."),
 TR("Red cell diameter vs capillary diameter", "قطر الكرية مقابل قطر الشعيرة", "Red cell 6–8 µm; minimum microcirculation diameter 3.5 µm — hence the need for flexibility.", "الكرية 6–8 مايكرومتر؛ أصغر قطر في الدوران الدقيق 3.5 — ولذلك تحتاج إلى المرونة."),
 TR("NADH vs NADPH", "NADH مقابل NADPH", "NADH (and ATP) from the Embden–Meyerhof pathway; NADPH from the hexose monophosphate shunt.", "NADH (والـ ATP) من مسار إمبدن–مايرهوف؛ وNADPH من تحويلة الهكسوز أحادي الفوسفات."),
 TR("Membrane composition", "تركيب الغشاء", "Protein 50%, fat 40%, carbohydrate up to 10%; skeleton: spectrin, ankyrin, protein 4.1, actin.", "بروتين 50%، دهن 40%، كاربوهيدرات حتى 10%؛ الهيكل: سبكترين، أنكيرين، بروتين 4.1، أكتين."),
 TR("Male vs female normal values", "القيم الطبيعية للذكور مقابل الإناث", "Hb 13.5–17.5 vs 11.5–15.5 g/dl; RBC 4.5–6.5 vs 3.9–5.6 ×10¹²/L; PCV 40–52 vs 36–48%.", "Hb 13.5–17.5 مقابل 11.5–15.5؛ RBC 4.5–6.5 مقابل 3.9–5.6 ×10¹²/L؛ PCV 40–52 مقابل 36–48%."),
]
important = [
 IM("What changes occur during erythroid maturation?", "ما التغيّرات التي تحدث أثناء نضج الخط الحمري؟", "Progressive decrease in cell size; decrease in nuclear size with chromatin condensation; loss of basophilic RNA with production of haemoglobin.", "تناقص حجم الخلية؛ تناقص حجم النواة مع تكثّف الكروماتين؛ فقدان الـ RNA القاعدي مع إنتاج الهيموغلوبين."),
 IM("Describe the normal red cell and how it fulfils its functions.", "صف الكرية الحمراء الطبيعية وكيف تؤدي وظائفها.", "A flexible biconcave disc 6–8 µm, passing through 3.5 µm capillaries, keeping Hb ferrous and osmotic balance; lives 120 days (480 km); makes ATP and NADH by the Embden–Meyerhof pathway and NADPH by the HMP shunt; removed by RES macrophages.", "قرص مرن مقعّر الوجهين 6–8 مايكرومتر، يمرّ في شعيرات 3.5، ويحافظ على Hb حديدوزيًا وعلى التوازن الأوزموزي؛ يعيش 120 يومًا (480 كم)؛ ينتج ATP وNADH بمسار إمبدن–مايرهوف وNADPH بتحويلة HMP؛ وتزيله بلاعم الجهاز الشبكي البطاني."),
 IM("Describe the red cell membrane.", "صف غشاء الكرية الحمراء.", "Lipid bilayer, integral proteins and membrane skeleton; 50% protein, 40% fat, up to 10% carbohydrate; skeleton of spectrin, ankyrin, protein 4.1 and actin forms a horizontal network maintaining the biconcave shape; defects cause hereditary spherocytosis and elliptocytosis.", "طبقة دهنية مزدوجة وبروتينات مدمجة وهيكل غشائي؛ 50% بروتين، 40% دهن، حتى 10% كاربوهيدرات؛ هيكل من السبكترين والأنكيرين والبروتين 4.1 والأكتين يكوّن شبكة أفقية تحفظ الشكل؛ وخلله يسبّب كثرة الكريات الكروية والإهليلجية الوراثية."),
 IM("List the substances required for erythropoiesis.", "عدّد المواد اللازمة لتكوين الكريات الحمر.", "Metals (iron, manganese, cobalt); vitamins (B12, B6, C, E, folate); amino acids; hormones (erythropoietin, androgen, thyroxin).", "الفلزات (حديد، منغنيز، كوبلت)؛ الفيتامينات (B12، B6، C، E، فولات)؛ الأحماض الأمينية؛ الهرمونات (إريثروبويتين، أندروجين، ثايروكسين)."),
 IM("How is erythropoiesis regulated and assessed?", "كيف يُنظَّم تكوين الكريات الحمر وكيف يُقيَّم؟", "Erythropoietin (kidney 90%) rises with hypoxia (anaemia, haemorrhage) and falls with increased O2 supply. Assessed by Hb, RBC count, PCV, indices (MCV 80–95 fl, MCH 27–34 pg, MCHC) and the blood film.", "يرتفع الإريثروبويتين (الكلية 90%) مع نقص الأكسجة (فقر دم، نزف) وينخفض مع زيادة الأوكسجين. ويُقيَّم بـ Hb وعدد الكريات وPCV والمؤشّرات (MCV 80–95، MCH 27–34، MCHC) والمسحة الدموية."),
]
save("hematology-lec3-blood-elements", 3, "Blood elements production", "إنتاج عناصر الدم", blocks, mcq, tf, traps, important)

```
