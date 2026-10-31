---
source: BIOS-Obsidian/tools/scripts/hl3/norm3.py
handouts: [hematology-practical-normal-values]
saved: 2026-10-31
tags: [bios, code]
---
# hl3/norm3.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#hematology-practical-normal-values|hematology-practical-normal-values]]

```python
import sys; sys.path.insert(0, "/tmp/claude-0/-home-user--/8f878068-bae9-502b-96f7-788f221c7cb0/scratchpad/imm456")
from ci import *            # c helpers + B INSHORT TERMS save(split.fix)

blocks = [
 SEC("Definition and Why Age Matters", "التعريف ولماذا يهمّ العمر"),
 L(["A **normal value (reference range)** is the **expected range in healthy people**.", "Normal values **change with age**, and sometimes with **sex**.",
    "The same result may be **normal in one age group and abnormal in another**."],
   ["**القيمة الطبيعية (المدى المرجعي)** هي **المدى المتوقّع عند الأشخاص الأصحاء**.", "تتغيّر القيم الطبيعية **مع العمر**، وأحيانًا مع **الجنس**.",
    "والنتيجة نفسها قد تكون **طبيعية في فئة عمرية وغير طبيعية في أخرى**."]),
 FLOW([("Healthy people", "الأشخاص الأصحاء"), ("Expected range", "المدى المتوقّع"), ("Normal value", "القيمة الطبيعية")]),
 INSHORT([("Normal value = reference range of healthy people.", "القيمة الطبيعية = المدى المرجعي للأصحاء."),
          ("It depends on **age** (and sometimes **sex**).", "تعتمد على **العمر** (وأحيانًا **الجنس**)."),
          ("So the same number can be normal or abnormal.", "لذلك قد يكون الرقم نفسه طبيعيًا أو غير طبيعي.")]),

 SEC("Key Age Groups", "الفئات العمرية الرئيسة"),
 T([B("Age group", "الفئة العمرية"), B("Main point", "النقطة الرئيسة")],
   [[B("**Newborn**", "**حديث الولادة**"), B("Higher hemoglobin, higher white blood cell count, higher reticulocytes", "هيموغلوبين أعلى، وعدد كريات بيض أعلى، وخلايا شبكية أعلى")],
    [B("**Child**", "**الطفل**"), B("Values gradually move toward the adult range", "تقترب القيم تدريجيًا من مدى البالغين")],
    [B("**Adult**", "**البالغ**"), B("Stable adult range; sex differences become clearer", "مدى ثابت للبالغين؛ وتتّضح الفروق بين الجنسين")]],
   key_cols=[0], widths=[26, 74]),
 F("age-overview.jpg", "Newborn → child → adult; platelets are relatively stable across ages", "حديث الولادة ← الطفل ← البالغ؛ والصفيحات ثابتة نسبيًا عبر الأعمار", h="34mm"),
 INSHORT([("**Newborn:** everything high (Hb, WBC, reticulocytes).", "**حديث الولادة:** كل شيء مرتفع (الهيموغلوبين والكريات البيض والخلايا الشبكية)."),
          ("**Child:** moving toward adult values.", "**الطفل:** يقترب من قيم البالغين."),
          ("**Adult:** stable values; male ≠ female.", "**البالغ:** قيم ثابتة؛ والذكر يختلف عن الأنثى.")]),

 SEC("Hemoglobin According to Age", "الهيموغلوبين بحسب العمر"),
 SIDE([T([B("Age", "العمر"), B("Hemoglobin", "الهيموغلوبين")],
         [[B("**Newborn**", "**حديث الولادة**"), "**14–24** g/dL"], [B("**Child**", "**الطفل**"), "**11–14** g/dL"],
          [B("**Adult male**", "**الذكر البالغ**"), "**13.5–17.5** g/dL"], [B("**Adult female**", "**الأنثى البالغة**"), "**12.0–16.0** g/dL"]],
         key_cols=[0], widths=[50, 50])],
      "hb-by-age.jpg", "Hemoglobin reference values by age", "قيم الهيموغلوبين المرجعية بحسب العمر"),
 INSHORT([("Highest Hb in the **newborn** (14–24), lowest in the **child** (11–14).", "أعلى هيموغلوبين عند **حديث الولادة** (14–24)، وأقلّه عند **الطفل** (11–14)."),
          ("Adult male (13.5–17.5) is higher than adult female (12–16).", "الذكر البالغ (13.5–17.5) أعلى من الأنثى البالغة (12–16).")]),

 SEC("White Blood Cell Count", "عدد الكريات البيض"),
 SIDE([T([B("Age", "العمر"), B("White blood cell count", "عدد الكريات البيض")],
         [[B("**Newborn**", "**حديث الولادة**"), "**9,000–30,000** /µL"], [B("**Child**", "**الطفل**"), "**6,000–17,000** /µL"],
          [B("**Adult**", "**البالغ**"), "**4,000–11,000** /µL"]],
         key_cols=[0], widths=[45, 55])],
      "wbc-by-age.jpg", "White blood cell count reference values by age", "قيم الكريات البيض المرجعية بحسب العمر"),
 H2("Adult White Blood Cell Differential Count", "العدّ التفريقي للكريات البيض عند البالغين"),
 T([B("Cell", "الخلية"), B("Normal %", "النسبة الطبيعية")],
   [[B("**Neutrophils**", "**العدلات**"), "**40–75%**"], [B("**Lymphocytes**", "**اللمفاويات**"), "**20–45%**"], [B("**Monocytes**", "**الوحيدات**"), "**2–10%**"],
    [B("**Eosinophils**", "**الحمضات**"), "**1–6%**"], [B("**Basophils**", "**القعدات**"), "**0–1%**"]],
   key_cols=[0], widths=[55, 45], style="summary", label_en="Differential", label_ar="العدّ التفريقي"),
 F("neutrophil-lymphocyte.jpg", "Blood film: a neutrophil and a lymphocyte among red cells", "مسحة دموية: عدلة ولمفاوية بين الكريات الحمر", h="54mm"),
 INSHORT([("WBC count falls with age: 9,000–30,000 → 6,000–17,000 → 4,000–11,000.", "يقلّ عدد الكريات البيض مع العمر: 9,000–30,000 ← 6,000–17,000 ← 4,000–11,000."),
          ("Order in adults: **neutrophils > lymphocytes > monocytes > eosinophils > basophils**.", "الترتيب عند البالغين: **العدلات > اللمفاويات > الوحيدات > الحمضات > القعدات**.")]),

 SEC("Platelets and Reticulocytes", "الصفيحات والخلايا الشبكية"),
 T([B("Parameter", "المعيار"), B("Normal value", "القيمة الطبيعية")],
   [[B("**Platelets**", "**الصفيحات**"), "**150,000–450,000** /µL"],
    [B("**Reticulocytes in newborns**", "**الخلايا الشبكية عند حديثي الولادة**"), "**2.5–6.0%**"],
    [B("**Reticulocytes in adults**", "**الخلايا الشبكية عند البالغين**"), "**0.5–1.5%**"]],
   key_cols=[0], widths=[60, 40]),
 FF(("platelets.jpg", "Platelets (arrows) in a blood film", "الصفيحات (الأسهم) في مسحة دموية", "48mm"), ("reticulocytes.jpg", "Reticulocytes (supravital stain)", "الخلايا الشبكية (صبغة فوق حيوية)", "48mm")),
 INSHORT([("Platelets: **150,000–450,000 /µL** at every age.", "الصفيحات: **150,000–450,000 /مايكرولتر** في كل الأعمار."),
          ("Reticulocytes: newborn **2.5–6.0%** > adult **0.5–1.5%**.", "الخلايا الشبكية: حديث الولادة **2.5–6.0%** أعلى من البالغ **0.5–1.5%**.")]),

 SEC("Red Blood Cell Count and Red Blood Cell Indices", "عدد الكريات الحمر ومؤشّراتها"),
 T([B("Adult", "البالغ"), B("Red blood cell count", "عدد الكريات الحمر")],
   [[B("**Adult male**", "**الذكر البالغ**"), "**4.7–6.1** ×10⁶/µL"], [B("**Adult female**", "**الأنثى البالغة**"), "**4.2–5.4** ×10⁶/µL"]],
   key_cols=[0], widths=[45, 55]),
 H2("Important red blood cell indices", "مؤشّرات الكريات الحمر المهمّة"),
 T([B("Parameter", "المعيار"), B("Normal", "الطبيعي"), B("Meaning", "المعنى")],
   [[B("**Mean Corpuscular Volume (MCV)**", "**متوسط حجم الكرية**"), "**80–100** fL", B("Average red blood cell size", "متوسط حجم الكرية الحمراء")],
    [B("**Mean Corpuscular Hemoglobin (MCH)**", "**متوسط هيموغلوبين الكرية**"), "**27–33** pg", B("Average hemoglobin amount per red blood cell", "متوسط كمية الهيموغلوبين في الكرية الحمراء الواحدة")],
    [B("**Mean Corpuscular Hemoglobin Concentration (MCHC)**", "**متوسط تركيز هيموغلوبين الكرية**"), "**32–36** g/dL", B("Average hemoglobin concentration in red blood cells", "متوسط تركيز الهيموغلوبين في الكريات الحمر")]],
   key_cols=[0], widths=[38, 18, 44], style="summary", label_en="RBC indices", label_ar="مؤشّرات الكريات الحمر"),
 N("These practical values (MCV 80–100, MCHC 32–36) differ slightly from the theory lectures of Dr. Mazin (MCV 80–95, MCHC 20–35) — use each lecturer's values in their exam.",
   "تختلف هذه القيم العملية (`MCV 80–100`، `MCHC 32–36`) قليلًا عن محاضرات النظري لدكتور مازن (`MCV 80–95`، `MCHC 20–35`)، فاعتمد قيم كل تدريسي في امتحانه.", label=["BIOS note", "ملاحظة BIOS"]),
 INSHORT([("RBC count: male **4.7–6.1** > female **4.2–5.4** ×10⁶/µL.", "عدد الكريات الحمر: الذكر **4.7–6.1** أعلى من الأنثى **4.2–5.4** ×10⁶/مايكرولتر."),
          ("**MCV** = size (fL), **MCH** = amount (pg), **MCHC** = concentration (g/dL).", "**MCV** = الحجم (fL)، و**MCH** = الكمية (pg)، و**MCHC** = التركيز (g/dL).")]),

 SEC("Quick Comparison by Age", "مقارنة سريعة بحسب العمر"),
 T([B("Parameter", "المعيار"), B("Newborn", "حديث الولادة"), B("Child", "الطفل"), B("Adult", "البالغ")],
   [[B("**Hemoglobin** (g/dL)", "**الهيموغلوبين**"), "14–24", "11–14", B("Male: 13.5–17.5 · Female: 12–16", "الذكر: 13.5–17.5 · الأنثى: 12–16")],
    [B("**White Blood Cell Count** (/µL)", "**عدد الكريات البيض**"), "9,000–30,000", "6,000–17,000", "4,000–11,000"],
    [B("**Platelets** (/µL)", "**الصفيحات**"), "150,000–450,000", "150,000–450,000", "150,000–450,000"],
    [B("**Reticulocytes**", "**الخلايا الشبكية**"), "2.5–6.0%", "—", "0.5–1.5%"]],
   key_cols=[0], widths=[28, 20, 20, 32], style="summary", label_en="Quick comparison", label_ar="مقارنة سريعة"),
 N(["Newborns usually have **higher hemoglobin and white blood cell counts**.", "Children **gradually approach** adult reference ranges.",
    "Adult males and females differ mainly in **hemoglobin and red blood cell count**.", "**Platelets are relatively stable** across age groups.", "**Always interpret results using the patient’s age.**"],
   ["لدى حديثي الولادة عادةً **هيموغلوبين وكريات بيض أعلى**.", "يقترب الأطفال **تدريجيًا** من مديات البالغين المرجعية.",
    "يختلف الذكور والإناث البالغون أساسًا في **الهيموغلوبين وعدد الكريات الحمر**.", "**الصفيحات ثابتة نسبيًا** عبر الفئات العمرية.", "**فسّر النتائج دائمًا بحسب عمر المريض.**"],
   label=["Keep in mind", "تذكّر"]),
] + TERMS([
 ("Normal value / Reference range", "القيمة الطبيعية / المدى المرجعي / المعدّل الطبيعي"),
 ("Newborn", "حديث الولادة / الوليد / المولود الجديد"),
 ("Hemoglobin (Hb)", "الهيموغلوبين / خضاب الدم / اليحمور"),
 ("White blood cell (WBC)", "كرية بيضاء / خلية دم بيضاء / كرية دم بيضاء"),
 ("Differential count", "العدّ التفريقي / العدّ النوعي / صيغة الدم"),
 ("Neutrophil", "عدلة / متعادلة / خلية متعادلة"),
 ("Lymphocyte", "لمفاوية / خلية لمفية / لمفية"),
 ("Monocyte", "وحيدة / وحيدة النواة / خلية وحيدة"),
 ("Eosinophil", "حمضة / يوزينية / محبّة للحمض"),
 ("Basophil", "قعدة / محبّة للقاعدة / قاعدية"),
 ("Platelet", "صفيحة / صفيحة دموية / خلية التخثّر"),
 ("Reticulocyte", "خلية شبكية / كرية شبكية / كرية حمراء فتيّة"),
 ("Red blood cell indices", "مؤشّرات الكريات الحمر / ثوابت الكريات الحمر / معاملات الكرية"),
 ("MCV", "متوسط حجم الكرية / الحجم الكروي الوسطي"),
 ("MCH", "متوسط هيموغلوبين الكرية / الخضاب الكروي الوسطي"),
 ("MCHC", "متوسط تركيز هيموغلوبين الكرية / تركيز الخضاب الكروي الوسطي"),
])

mcq = [
 {"topic_en": "Reference ranges and age", "topic_ar": "المديات المرجعية والعمر"},
 Q("A normal value (reference range) is:", "القيمة الطبيعية (المدى المرجعي) هي:", [("The highest value ever measured", "أعلى قيمة قيست"), ("The expected range in healthy people", "المدى المتوقّع عند الأصحاء"), ("The value in sick people", "القيمة عند المرضى"), ("A fixed number for all ages", "رقم ثابت لكل الأعمار")], "b"),
 Q("Normal values change with:", "تتغيّر القيم الطبيعية مع:", [("Age and sometimes sex", "العمر وأحيانًا الجنس"), ("Weather", "الطقس"), ("Blood group only", "فصيلة الدم فقط"), ("Nothing", "لا شيء")], "a"),
 Q("Which age group has higher Hb, WBC and reticulocytes?", "أي فئة عمرية لديها Hb وكريات بيض وخلايا شبكية أعلى؟", [("Child", "الطفل"), ("Adult", "البالغ"), ("Newborn", "حديث الولادة"), ("Elderly", "كبير السن")], "c"),
 Q("In which group do sex differences become clearer?", "في أي فئة تتّضح الفروق بين الجنسين؟", [("Newborn", "حديث الولادة"), ("Infant", "الرضيع"), ("Child", "الطفل"), ("Adult", "البالغ")], "d"),
 {"topic_en": "Values", "topic_ar": "القيم"},
 Q("Normal haemoglobin of a newborn is:", "الهيموغلوبين الطبيعي لحديث الولادة:", [("11–14 g/dL", "11–14"), ("14–24 g/dL", "14–24"), ("12–16 g/dL", "12–16"), ("8–10 g/dL", "8–10")], "b"),
 Q("Normal haemoglobin of a child is:", "الهيموغلوبين الطبيعي للطفل:", [("11–14 g/dL", "11–14"), ("14–24 g/dL", "14–24"), ("13.5–17.5 g/dL", "13.5–17.5"), ("18–22 g/dL", "18–22")], "a"),
 Q("Normal haemoglobin of an adult female (this lecture) is:", "الهيموغلوبين الطبيعي للأنثى البالغة (هذه المحاضرة):", [("11–14 g/dL", "11–14"), ("13.5–17.5 g/dL", "13.5–17.5"), ("12.0–16.0 g/dL", "12.0–16.0"), ("14–24 g/dL", "14–24")], "c"),
 Q("The normal WBC count of a newborn is:", "عدد الكريات البيض الطبيعي لحديث الولادة:", [("4,000–11,000", "4,000–11,000"), ("6,000–17,000", "6,000–17,000"), ("1,000–3,000", "1,000–3,000"), ("9,000–30,000", "9,000–30,000")], "d"),
 Q("The normal adult WBC count is:", "عدد الكريات البيض الطبيعي للبالغ:", [("4,000–11,000 /µL", "4,000–11,000"), ("9,000–30,000 /µL", "9,000–30,000"), ("150,000–450,000 /µL", "150,000–450,000"), ("6,000–17,000 /µL", "6,000–17,000")], "a"),
 Q("The most numerous white cells in adults are:", "أكثر الكريات البيض عددًا عند البالغين:", [("Lymphocytes", "اللمفاويات"), ("Neutrophils (40–75%)", "العدلات (40–75%)"), ("Monocytes", "الوحيدات"), ("Eosinophils", "الحمضات")], "b"),
 Q("Normal basophils in adults are:", "النسبة الطبيعية للقعدات عند البالغين:", [("2–10%", "2–10%"), ("1–6%", "1–6%"), ("0–1%", "0–1%"), ("20–45%", "20–45%")], "c"),
 Q("Normal lymphocytes in adults are:", "النسبة الطبيعية للمفاويات عند البالغين:", [("20–45%", "20–45%"), ("40–75%", "40–75%"), ("0–1%", "0–1%"), ("2–10%", "2–10%")], "a"),
 Q("The normal platelet count is:", "العدد الطبيعي للصفيحات:", [("4,000–11,000 /µL", "4,000–11,000"), ("1–2 million /µL", "1–2 مليون"), ("50,000–100,000 /µL", "50,000–100,000"), ("150,000–450,000 /µL", "150,000–450,000")], "d"),
 Q("Reticulocytes in adults are:", "الخلايا الشبكية عند البالغين:", [("2.5–6.0%", "2.5–6.0%"), ("0.5–1.5%", "0.5–1.5%"), ("10%", "10%"), ("0%", "0%")], "b"),
 Q("The adult male red cell count (this lecture) is:", "عدد الكريات الحمر للذكر البالغ (هذه المحاضرة):", [("4.2–5.4 ×10⁶/µL", "4.2–5.4"), ("3.0–4.0 ×10⁶/µL", "3.0–4.0"), ("4.7–6.1 ×10⁶/µL", "4.7–6.1"), ("7–8 ×10⁶/µL", "7–8")], "c"),
 Q("MCV reflects:", "يعكس MCV:", [("Average red blood cell size", "متوسط حجم الكرية الحمراء"), ("Average Hb concentration", "متوسط تركيز Hb"), ("Platelet count", "عدد الصفيحات"), ("WBC count", "عدد الكريات البيض")], "a"),
 Q("The normal MCHC (this lecture) is:", "الـ MCHC الطبيعي (هذه المحاضرة):", [("80–100 g/dL", "80–100"), ("27–33 g/dL", "27–33"), ("12–16 g/dL", "12–16"), ("32–36 g/dL", "32–36")], "d"),
 Q("Which parameter is relatively stable across ages?", "أي معيار ثابت نسبيًا عبر الأعمار؟", [("Haemoglobin", "الهيموغلوبين"), ("Platelets", "الصفيحات"), ("WBC count", "عدد الكريات البيض"), ("Reticulocytes", "الخلايا الشبكية")], "b"),
 {"topic_en": "Picture questions", "topic_ar": "أسئلة الصور"},
 Q("In this chart, the age group with the widest WBC range is:", "في هذا المخطط، الفئة العمرية ذات أوسع مدى للكريات البيض:", [("Adult", "البالغ"), ("Child", "الطفل"), ("Newborn", "حديث الولادة"), ("All equal", "متساوية")], "c", img="assets/wbc-by-age.jpg", img_h="40mm"),
 Q("The small fragments marked by arrows in this blood film are:", "القطع الصغيرة المؤشّرة بالأسهم في هذه المسحة:", [("Reticulocytes", "خلايا شبكية"), ("Lymphocytes", "لمفاويات"), ("Platelets", "صفيحات"), ("Neutrophils", "عدلات")], "c", img="assets/platelets.jpg", img_h="40mm"),
 Q("The cell with the multilobed nucleus in this film is a:", "الخلية ذات النواة متعدّدة الفصوص في هذه المسحة:", [("Neutrophil", "عدلة"), ("Lymphocyte", "لمفاوية"), ("Platelet", "صفيحة"), ("Reticulocyte", "خلية شبكية")], "a", img="assets/neutrophil-lymphocyte.jpg", img_h="40mm"),
]
tf = [
 TF("The same result may be normal in one age group and abnormal in another.", "قد تكون النتيجة نفسها طبيعية في فئة عمرية وغير طبيعية في أخرى.", "T"),
 TF("Children have higher haemoglobin than newborns.", "لدى الأطفال هيموغلوبين أعلى من حديثي الولادة.", "F"),
 TF("Children's values gradually move toward the adult range.", "تقترب قيم الأطفال تدريجيًا من مدى البالغين.", "T"),
 TF("Newborns have the highest WBC count.", "لدى حديثي الولادة أعلى عدد للكريات البيض.", "T"),
 TF("Monocytes are 40–75% of adult WBC.", "تشكّل الوحيدات 40–75% من كريات البالغين البيض.", "F"),
 TF("Eosinophils are 1–6% in adults.", "تشكّل الحمضات 1–6% عند البالغين.", "T"),
 TF("Reticulocytes are higher in newborns than adults.", "الخلايا الشبكية أعلى عند حديثي الولادة منها عند البالغين.", "T"),
 TF("Platelet reference ranges differ greatly between newborns and adults.", "تختلف مديات الصفيحات كثيرًا بين حديثي الولادة والبالغين.", "F"),
 TF("Adult males and females differ mainly in Hb and RBC count.", "يختلف الذكور والإناث البالغون أساسًا في Hb وعدد الكريات الحمر.", "T"),
 TF("MCH means average haemoglobin concentration in red cells.", "يعني MCH متوسط تركيز الهيموغلوبين في الكريات الحمر.", "F"),
 TF("Results should always be interpreted using the patient’s age.", "يجب تفسير النتائج دائمًا بحسب عمر المريض.", "T"),
]
traps = [
 TR("MCH vs MCHC", "MCH مقابل MCHC", "MCH: average Hb amount per cell (27–33 pg). MCHC: average Hb concentration in red cells (32–36 g/dL).", "MCH: متوسط كمية Hb في الكرية (27–33 pg). MCHC: متوسط تركيز Hb في الكريات (32–36 g/dL)."),
 TR("Highest Hb vs highest WBC", "أعلى Hb مقابل أعلى كريات بيض", "Both are highest in newborns (Hb 14–24; WBC 9,000–30,000).", "كلاهما الأعلى عند حديثي الولادة (Hb 14–24؛ الكريات البيض 9,000–30,000)."),
 TR("Reticulocytes: newborn vs adult", "الخلايا الشبكية: حديث الولادة مقابل البالغ", "Newborn 2.5–6.0%; adult 0.5–1.5%.", "حديث الولادة 2.5–6.0%؛ البالغ 0.5–1.5%."),
 TR("Differential percentages", "نسب العدّ التفريقي", "Neutrophils 40–75, lymphocytes 20–45, monocytes 2–10, eosinophils 1–6, basophils 0–1.", "العدلات 40–75، اللمفاويات 20–45، الوحيدات 2–10، الحمضات 1–6، القعدات 0–1."),
 TR("Practical vs theory values", "قيم العملي مقابل النظري", "This lecture: female Hb 12–16, MCV 80–100, MCHC 32–36. Dr. Mazin's theory: female Hb 11.5–15.5, MCV 80–95, MCHC 20–35.", "هذه المحاضرة: Hb الأنثى 12–16، MCV 80–100، MCHC 32–36. نظري د. مازن: Hb الأنثى 11.5–15.5، MCV 80–95، MCHC 20–35."),
]
important = [  # the lecturer's quiz (slide 11)
 IM("What is meant by a normal (reference) value?", "ما المقصود بالقيمة الطبيعية (المرجعية)؟", "The expected range in healthy people.", "المدى المتوقّع عند الأشخاص الأصحاء."),
 IM("Why is age important in hematology?", "لماذا يهمّ العمر في أمراض الدم؟", "Normal values change with age (and sometimes sex), so the same result may be normal in one age group and abnormal in another.", "لأن القيم الطبيعية تتغيّر مع العمر (وأحيانًا الجنس)، فقد تكون النتيجة نفسها طبيعية في فئة وغير طبيعية في أخرى."),
 IM("Which age group usually has the highest white blood cell count?", "أي فئة عمرية لديها عادةً أعلى عدد للكريات البيض؟", "Newborns (9,000–30,000 /µL).", "حديثو الولادة (9,000–30,000 /مايكرولتر)."),
 IM("What is the normal platelet range?", "ما المدى الطبيعي للصفيحات؟", "150,000–450,000 /µL, relatively stable across ages.", "150,000–450,000 /مايكرولتر، وهو ثابت نسبيًا عبر الأعمار."),
 IM("What is the hemoglobin range in adult males and females?", "ما مدى الهيموغلوبين عند الذكور والإناث البالغين؟", "Males 13.5–17.5 g/dL; females 12.0–16.0 g/dL.", "الذكور 13.5–17.5 غ/دل؛ الإناث 12.0–16.0 غ/دل."),
 IM("Why are reticulocytes higher in newborns?", "لماذا تكون الخلايا الشبكية أعلى عند حديثي الولادة؟", "Newborns show higher values (2.5–6.0% vs 0.5–1.5% in adults) because red cell production is very active at birth, with high haemoglobin.", "لأن لديهم قيمًا أعلى (2.5–6.0% مقابل 0.5–1.5% عند البالغين) بسبب نشاط إنتاج الكريات الحمر العالي عند الولادة مع ارتفاع الهيموغلوبين."),
]
meta = dict(HEM, unit_en="Lab 3", unit_ar="العملي 3", unit_no="3", title_en="Normal Values of Blood Components According to Age", title_ar="القيم الطبيعية لمكوّنات الدم بحسب العمر")
save("hematology-practical-normal-values", meta, blocks, mcq, tf, traps, important)

```
