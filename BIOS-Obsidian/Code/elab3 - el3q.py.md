---
source: BIOS-Obsidian/tools/scripts/elab3/el3q.py
handouts: [enzymology-lab3-alkaline-phosphatase]
saved: 2026-11-09
tags: [bios, code]
---
# elab3/el3q.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#enzymology-lab3-alkaline-phosphatase|enzymology-lab3-alkaline-phosphatase]]

```python
mcq = [
 {"topic_en": "The enzyme", "topic_ar": "الإنزيم"},
 Q("ALP originates mainly from:", "يأتي ALP أساسًا من:", O(("Bone, liver and placenta", "العظم والكبد والمشيمة"), ("Heart and skeletal muscle", "القلب والعضلات الهيكلية"), ("Pancreas only", "البنكرياس فقط"), ("Red blood cells", "كريات الدم الحمر")), "a"),
 Q("ALP is called alkaline because it works best at pH:", "سُمّي ALP قاعديًا لأنه يعمل أفضل عند pH:", O(("5", "5"), ("9", "9"), ("7.4", "7.4"), ("2", "2")), "b"),
 Q("ALP levels depend on:", "تعتمد مستويات ALP على:", O(("Blood group", "فصيلة الدم"), ("Time of day only", "وقت اليوم فقط"), ("Age and gender", "العمر والجنس"), ("Height", "الطول")), "c"),
 Q("ALP is used as an index of:", "يُستعمل ALP مؤشّرًا لـ:", O(("Heart and kidney disease", "أمراض القلب والكلية"), ("Muscle disease", "أمراض العضلات"), ("Lung disease", "أمراض الرئة"), ("Liver and bone disease", "أمراض الكبد والعظم")), "d"),
 Q("In bone disease, ALP rises in proportion to:", "في أمراض العظم يرتفع ALP بالتناسب مع:", O(("New bone cell production (osteoblastic activity)", "إنتاج خلايا عظمية جديدة (نشاط بانيات العظم)"), ("Bone marrow failure", "فشل نخاع العظم"), ("Muscle mass", "كتلة العضلات"), ("Red cell destruction", "تكسّر الكريات الحمر")), "a"),
 Q("In liver disease, ALP rises because of:", "في أمراض الكبد يرتفع ALP بسبب:", O(("Increased bone formation", "زيادة تكوين العظم"), ("Obstruction in the biliary tract", "انسداد القناة الصفراوية"), ("Kidney failure", "الفشل الكلوي"), ("Low pH", "انخفاض pH")), "b"),
 {"topic_en": "Normal values", "topic_ar": "القيم الطبيعية"},
 Q("The normal ALP of an adult (female > 15 y or male > 20 y) is:", "القيمة الطبيعية لـ ALP للبالغ (أنثى > 15 أو ذكر > 20 سنة):", O(("< 350 U/L", "أقل من 350"), ("< 500 U/L", "أقل من 500"), ("25–100 U/L", "25–100"), ("0–10 U/L", "0–10")), "c"),
 Q("The normal ALP for children 1–12 years is:", "القيمة الطبيعية لـ ALP للأطفال 1–12 سنة:", O(("25–100 U/L", "25–100"), ("< 500 U/L", "أقل من 500"), ("> 1000 U/L", "أكثر من 1000"), ("< 350 U/L", "أقل من 350")), "d"),
 Q("The highest upper limit (< 500 U/L) is for:", "أعلى حدّ أعلى (أقل من 500) يكون لـ:", O(("Males 12–14 years", "الذكور 12–14 سنة"), ("Females > 15 years", "الإناث > 15 سنة"), ("Males > 20 years", "الذكور > 20 سنة"), ("Females 1–12 years", "الإناث 1–12 سنة")), "a"),
 {"topic_en": "Clinical significance", "topic_ar": "الأهمية السريرية"},
 Q("ALP is increased in:", "يرتفع ALP في:", O(("Magnesium deficiency", "نقص المغنيسيوم"), ("Obstructive jaundice", "اليرقان الانسدادي"), ("Chronic renal failure", "الفشل الكلوي المزمن"), ("Peptic ulcer", "القرحة الهضمية")), "b"),
 Q("Which bone disease increases ALP?", "أيّ مرض عظمي يرفع ALP؟", O(("Peptic ulcer", "القرحة الهضمية"), ("Myocardial infarction", "احتشاء القلب"), ("Osteomalacia", "تليّن العظام"), ("Zinc deficiency", "نقص الزنك")), "c"),
 Q("According to the sheet, ALP is decreased in:", "حسب الورقة، ينخفض ALP في:", O(("Hepatitis", "التهاب الكبد"), ("Osteogenic sarcoma", "الساركوما العظمية"), ("Chronic alcohol ingestion", "تناول الكحول المزمن"), ("Chronic renal failure", "الفشل الكلوي المزمن")), "d"),
 Q("Nutritional deficiency that decreases ALP:", "النقص الغذائي الذي يخفض ALP:", O(("Magnesium and zinc", "المغنيسيوم والزنك"), ("Iron", "الحديد"), ("Vitamin C", "فيتامين C"), ("Sodium", "الصوديوم")), "a"),
 Q("Which of the following increases ALP?", "أيّ مما يأتي يرفع ALP؟", O(("Ulcerative colitis", "التهاب القولون التقرّحي"), ("Diabetes mellitus", "داء السكري"), ("Cancer of the pancreas", "سرطان البنكرياس"), ("Pulmonary infarction", "احتشاء الرئة")), "b"),
 Q("Infectious mononucleosis affects ALP as a:", "داء كثرة الوحيدات العدوائي يؤثّر على ALP كـ:", O(("Bone disease that decreases it", "مرض عظمي يخفضه"), ("Nutritional cause of decrease", "سبب غذائي للانخفاض"), ("Liver disease that increases it", "مرض كبدي يرفعه"), ("No effect", "لا تأثير")), "c"),
 {"topic_en": "Sample and interference", "topic_ar": "العيّنة والتداخلات"},
 Q("The sample for ALP is:", "عيّنة ALP هي:", O(("Urine", "الإدرار"), ("CSF", "السائل الدماغي الشوكي"), ("Whole blood only", "دم كامل فقط"), ("Serum or plasma", "مصل أو بلازما")), "d"),
 Q("ALP should be tested the same day because:", "يجب فحص ALP في اليوم نفسه لأن:", O(("It increases at room temperature and in refrigerated storage", "يرتفع بدرجة الغرفة وفي الخزن المبرّد"), ("It disappears in 1 hour", "يختفي خلال ساعة"), ("It clots", "يتخثّر"), ("It turns yellow", "يصفرّ")), "a"),
 Q("Anticoagulated blood causes ALP to:", "الدم المضاف إليه مانع تخثّر يجعل ALP:", O(("Increase", "يرتفع"), ("Decrease", "ينخفض"), ("Stay the same", "يبقى نفسه"), ("Double", "يتضاعف")), "b"),
 Q("A fatty meal before sampling:", "الوجبة الدسمة قبل سحب العيّنة:", O(("Decreases ALP", "تخفض ALP"), ("Has no effect", "لا تأثير لها"), ("Increases ALP", "ترفع ALP"), ("Stops the reaction", "توقف التفاعل")), "c"),
 {"topic_en": "Principle, procedure and calculation", "topic_ar": "المبدأ وطريقة العمل والحساب"},
 Q("The substrate used in the ALP method is:", "المادة الأساس في طريقة ALP:", O(("Glucose", "الغلوكوز"), ("Urea", "اليوريا"), ("ATP", "ATP"), ("p-Nitrophenylphosphate", "بارا-نايتروفينيل فوسفات")), "d"),
 Q("The coloured product measured is:", "الناتج الملوّن الذي يُقاس:", O(("p-Nitrophenol", "بارا-نايتروفينول"), ("Phosphate", "الفوسفات"), ("Water", "الماء"), ("NADH", "NADH")), "a"),
 Q("The volume of sample in the procedure is:", "حجم العيّنة في طريقة العمل:", O(("250 microL", "250 مايكرولتر"), ("20 microL", "20 مايكرولتر"), ("1000 microL", "1000 مايكرولتر"), ("100 microL", "100 مايكرولتر")), "b"),
 Q("The starter reagent (added last) is:", "كاشف البدء (يُضاف أخيرًا) هو:", O(("The buffer (BUF)", "المحلول المنظّم"), ("The sample", "العيّنة"), ("The substrate (SUB)", "المادة الأساس"), ("Water", "الماء")), "c"),
 Q("ALP activity is calculated as:", "تُحسب فعالية ALP:", O(("U/L = ΔA/min ÷ 3433", "U/L = ΔA/min ÷ 3433"), ("U/L = A × 100", "U/L = A × 100"), ("U/L = 3433 ÷ ΔA", "U/L = 3433 ÷ ΔA"), ("U/L = ΔA/min × 3433", "U/L = ΔA/min × 3433")), "d"),
 Q("If ΔA/min = 0.020, ALP activity is about:", "إذا كانت ΔA/min = 0.020 فإن فعالية ALP تقريبًا:", O(("69 U/L", "69 وحدة/لتر"), ("172 U/L", "172 وحدة/لتر"), ("343 U/L", "343 وحدة/لتر"), ("20 U/L", "20 وحدة/لتر")), "a"),
]

tf = [
 TF("ALP has some activity in the kidney and intestines.", "لـ ALP بعض الفعالية في الكلية والأمعاء.", "T"),
 TF("ALP functions best at pH 7.", "يعمل ALP أفضل عند pH 7.", "F"),
 TF("Used alone, alkaline phosphatase may be misleading.", "إذا استُعمل ALP وحده فقد يكون مضلّلًا.", "T"),
 TF("Children have lower ALP than adults.", "ALP عند الأطفال أقل من البالغين.", "F"),
 TF("Hepatic carcinoma increases ALP.", "سرطان الكبد يرفع ALP.", "T"),
 TF("Chronic alcohol ingestion decreases ALP.", "تناول الكحول المزمن يخفض ALP.", "F"),
 TF("Peptic ulcer is listed among the causes of decreased ALP.", "القرحة الهضمية مذكورة ضمن أسباب انخفاض ALP.", "T"),
 TF("Refrigerated storage keeps ALP unchanged for days.", "الخزن المبرّد يبقي ALP دون تغيير لأيام.", "F"),
 TF("ALP can be measured in serum or plasma.", "يمكن قياس ALP في المصل أو البلازما.", "T"),
 TF("In the procedure, the sample is incubated with the buffer for 1 min before adding the substrate.", "في طريقة العمل تُحضَّن العيّنة مع المنظّم دقيقة قبل إضافة المادة الأساس.", "T"),
 TF("The absorbance is read only once.", "يُقرأ الامتصاص مرّة واحدة فقط.", "F"),
 TF("The factor in the calculation is 3433.", "المعامل في الحساب هو 3433.", "T"),
]

traps = [
 TR("Bone vs liver — why does ALP rise in each?", "العظم مقابل الكبد — لماذا يرتفع ALP في كلٍّ منهما؟",
    "Bone: more new bone cell production (osteoblastic activity); liver: impaired excretion due to biliary obstruction.", "العظم: زيادة إنتاج خلايا عظمية جديدة (بانيات العظم)؛ الكبد: تعطّل الإخراج بسبب انسداد القناة الصفراوية."),
 TR("High ALP in a 13-year-old boy — disease?", "ALP مرتفع عند ولد عمره 13 سنة — مرض؟",
    "Not necessarily — males 12–14 years have normal values up to < 500 U/L (growth).", "ليس بالضرورة — الطبيعي للذكور 12–14 سنة حتى أقل من 500 وحدة/لتر (النمو)."),
 TR("Storage: up or down?", "الخزن: يرفع أم يخفض؟",
    "Up — ALP increases at room temperature and in the fridge; test the same day.", "يرفع — يزداد ALP بدرجة الغرفة وفي الثلاجة؛ افحص في نفس اليوم."),
 TR("Anticoagulant vs fatty meal?", "مانع التخثّر مقابل الوجبة الدسمة؟",
    "Anticoagulated blood decreases ALP; a fatty meal increases it.", "الدم مع مانع التخثّر يخفض ALP؛ والوجبة الدسمة ترفعه."),
 TR("BUF or SUB — which starts the reaction?", "BUF أم SUB — أيّهما يبدأ التفاعل؟",
    "SUB (substrate, p-nitrophenylphosphate) — the starter reagent, added after 1 min incubation of sample + buffer.", "SUB (المادة الأساس، بارا-نايتروفينيل فوسفات) — كاشف البدء، يُضاف بعد تحضين العيّنة مع المنظّم دقيقة."),
 TR("Multiply or divide by 3433?", "نضرب أم نقسم على 3433؟",
    "Multiply: U/L = ΔA/min × 3433.", "نضرب: U/L = ΔA/min × 3433."),
]

important = [
 IM("What is ALP and why is it called alkaline?", "ما هو ALP ولماذا سُمّي قاعديًا؟",
    "An enzyme originating mainly in bone, liver and placenta, with some activity in kidney and intestines; called alkaline because it works best at pH 9; its levels depend on age and gender; it is an index of liver and bone disease when correlated with other clinical findings.",
    "إنزيم يأتي أساسًا من العظم والكبد والمشيمة مع بعض الفعالية في الكلية والأمعاء؛ سُمّي قاعديًا لأنه يعمل أفضل عند pH 9؛ مستوياته تعتمد على العمر والجنس؛ وهو مؤشّر لأمراض الكبد والعظم عند ربطه بالنتائج السريرية الأخرى."),
 IM("Write the normal values of ALP.", "اكتب القيم الطبيعية لـ ALP.",
    "Females: 1–12 y < 350 U/L, > 15 y 25–100 U/L. Males: 1–12 y < 350 U/L, 12–14 y < 500 U/L, > 20 y 25–100 U/L.",
    "الإناث: 1–12 سنة أقل من 350، وأكثر من 15 سنة 25–100 وحدة/لتر. الذكور: 1–12 سنة أقل من 350، و12–14 سنة أقل من 500، وأكثر من 20 سنة 25–100 وحدة/لتر."),
 IM("List the causes of increased ALP.", "عدّد أسباب ارتفاع ALP.",
    "Liver disease (obstructive jaundice, hepatic carcinoma, hepatocellular cirrhosis, hepatitis, infectious mononucleosis); diabetes mellitus and diabetic hepatic lipidosis; chronic alcohol ingestion; bone disease (metastatic bone tumor, osteogenic sarcoma, osteomalacia).",
    "أمراض الكبد (اليرقان الانسدادي، سرطان الكبد، تليّف الكبد، التهاب الكبد، داء كثرة الوحيدات العدوائي)؛ السكري والتشحّم الكبدي السكري؛ الكحول المزمن؛ أمراض العظم (ورم العظم النقيلي، الساركوما العظمية، تليّن العظام)."),
 IM("List the causes of decreased ALP (as in the sheet).", "عدّد أسباب انخفاض ALP (كما في الورقة).",
    "Hyperparathyroidism and hyperthyroidism; pulmonary and myocardial infarctions; cancer of lung or pancreas; ulcerative colitis, peptic ulcer; chronic renal failure; magnesium and zinc deficiency (nutritional).",
    "فرط جارات الدرقية وفرط الدرقية؛ احتشاء الرئة والقلب؛ سرطان الرئة أو البنكرياس؛ التهاب القولون التقرّحي والقرحة الهضمية؛ الفشل الكلوي المزمن؛ نقص المغنيسيوم والزنك (غذائي)."),
 IM("What factors affect the ALP result?", "ما العوامل المؤثّرة في نتيجة ALP؟",
    "ALP increases at room temperature and in refrigerated storage (test the same day), decreases if blood is anticoagulated, and increases after fatty meals. Sample: serum or plasma.",
    "يرتفع ALP بدرجة الغرفة وفي الخزن المبرّد (افحص في نفس اليوم)، وينخفض إذا أُضيف مانع تخثّر، ويرتفع بعد الوجبات الدسمة. العيّنة: مصل أو بلازما."),
 IM("Write the principle, procedure and calculation of ALP.", "اكتب مبدأ فحص ALP وطريقته وحسابه.",
    "Principle: p-nitrophenylphosphate + H2O → phosphate + p-nitrophenol (yellow). Procedure: 20 µL sample + 1000 µL BUF, mix and incubate 1 min, add 250 µL SUB, mix and read Abs after 1 min then again after 1, 2 and 3 min. Calculation: U/L = ΔA/min × 3433.",
    "المبدأ: بارا-نايتروفينيل فوسفات + ماء ← فوسفات + بارا-نايتروفينول (أصفر). الطريقة: 20 مايكرولتر عيّنة + 1000 منظّم، امزج وحضّن دقيقة، أضف 250 مادة أساس، امزج واقرأ الامتصاص بعد دقيقة ثم بعد 1 و2 و3 دقائق. الحساب: `U/L = ΔA/min × 3433`."),
]

import re as _re
_RUN = _re.compile(r"[A-Za-z0-9Δ(][A-Za-z0-9Δ/×÷=.()· ]*[A-Za-z0-9)]")
def _ltr(s):
    return _RUN.sub(lambda m: "`" + m.group(0) + "`" if "=" in m.group(0) else m.group(0), s)
for _q in mcq:
    if "ar" in _q:
        _q["ar"] = _ltr(_q["ar"]); _q["options"] = [[o[0], _ltr(o[1])] for o in _q["options"]]
for _q in traps:
    _q["answer_ar"] = _ltr(_q["answer_ar"])

meta = {"subject_en": "Clinical Enzymology", "subject_ar": "الإنزيمات السريرية", "short_ar": "انزيمات سريرية", "instructor": "د. بارق و د. هشام",
        "unit_en": "Lab 3", "unit_ar": "العملي 3", "unit_label": "LAB", "unit_no": "3",
        "title_en": "Serum Alkaline Phosphatase (ALP)", "title_ar": "الفوسفاتيز القاعدي في المصل",
        "kind": "Laboratories — عملي", "stage": "The fourth stage — الرابعة"}
save("enzymology-lab3-alkaline-phosphatase", meta, blocks, balance(mcq, 13), tf, traps, important)

```
