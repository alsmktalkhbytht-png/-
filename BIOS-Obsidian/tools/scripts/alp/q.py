import sys, json, os
sys.path.insert(0, "/tmp/claude-0/-home-user-kwmdkm/44452a28-19bf-5ce8-890a-f6919e775f0b/scratchpad/imm456")
from ci import *            # Q P balance IM
sys.path.insert(0, "/tmp/claude-0/-home-user-kwmdkm/44452a28-19bf-5ce8-890a-f6919e775f0b/scratchpad"); from bidi import ltr_all

# Clinical Enzymology practical — Serum Alkaline Phosphatase (ALP) (stage 4, د. بارق و د. هشام).
# Source: 3-page student notes ("Abdullah Khalid", Advanced clinical Biochemistry practical 2023-2024).
# QUESTIONS ONLY — comprehensive MCQ bank; answers_inline + SA incl. the student's marked points
# ("كل وحدة نحفظ كم سبب" + the T/F storage/handling points).
O = P
FOLDER = "enzymology-alp-mcq"
W = lambda q, en, ar: dict(q, note_en=en, note_ar=ar)

mcq = [
 # ───────────────────────── 1. source & general properties
 {"topic_en": "Source and general properties of ALP", "topic_ar": "مصدر الفوسفاتيز القاعدي وصفاته العامة"},
 W(Q("Alkaline phosphatase (ALP) originates mainly in the:", "ينشأ الفوسفاتيز القاعدي (ALP) أساسًا في:",
     O(("Bone, liver and placenta", "العظم والكبد والمشيمة"), ("Spleen and lungs", "الطحال والرئتين"), ("Brain and skin", "الدماغ والجلد"), ("Red blood cells", "كريات الدم الحمراء")), "a"),
   "ALP originates mainly in bone, liver and placenta, with some activity in the kidney and intestines.", "ينشأ ALP أساسًا في العظم والكبد والمشيمة، مع بعض الفعالية في الكلية والأمعاء."),
 W(Q("Besides its main sources, ALP has some activity in the:", "إضافةً إلى مصادره الرئيسة، للـ ALP بعض الفعالية في:",
     O(("Kidney and intestines", "الكلية والأمعاء"), ("Heart and brain", "القلب والدماغ"), ("Skin and hair", "الجلد والشعر"), ("Thyroid gland", "الغدة الدرقية")), "a"),
   "Some activity exists in the kidney and intestines.", "توجد بعض الفعالية في الكلية والأمعاء."),
 W(Q("ALP is called “alkaline” because it functions best at a pH of:", "يُسمّى ALP «قاعديًا» لأنه يعمل أفضل ما يكون عند أسّ هيدروجيني:",
     O(("9", "9"), ("7", "7"), ("5", "5"), ("2", "2")), "a"),
   "It is called alkaline because it functions best at a pH of 9.", "يُسمّى قاعديًا لأنه يعمل أفضل ما يكون عند أسّ هيدروجيني 9."),
 W(Q("ALP levels are dependent on:", "تعتمد مستويات ALP على:",
     O(("Age and gender", "العمر والجنس"), ("Blood type", "فصيلة الدم"), ("Height only", "الطول فقط"), ("Time of year", "فصل السنة")), "a"),
   "ALP levels are age and gender dependent.", "تعتمد مستويات ALP على العمر والجنس."),
 W(Q("ALP is used (when correlated with other clinical findings) as an index of:", "يُستعمل ALP (عند ربطه بموجودات سريرية أخرى) كدليل على:",
     O(("Liver and bone disease", "أمراض الكبد والعظم"), ("Kidney stones", "حصى الكلى"), ("Lung infection", "عدوى الرئة"), ("Anemia", "فقر الدم")), "a"),
   "ALP is used as an index of liver and bone disease when correlated with other clinical findings.", "يُستعمل ALP دليلًا على أمراض الكبد والعظم عند ربطه بالموجودات السريرية الأخرى."),

 # ───────────────────────── 2. bone vs liver disease
 {"topic_en": "ALP in bone disease vs liver disease", "topic_ar": "ALP في مرض العظم مقابل مرض الكبد"},
 W(Q("In bone disease, the ALP level rises in proportion to:", "في مرض العظم، يرتفع مستوى ALP بتناسب مع:",
     O(("New bone cell production (osteoplastic activity and calcium deposit)", "إنتاج خلايا عظمية جديدة (الفعالية البانية للعظم وترسيب الكالسيوم)"), ("Red cell destruction", "تحطّم الكريات الحمراء"), ("Muscle breakdown", "تحلّل العضلات"), ("Fat storage", "خزن الدهون")), "a"),
   "In bone disease, ALP rises in proportion to new bone cell production from osteoplastic activity and the deposit of calcium in the bones.", "في مرض العظم يرتفع ALP بتناسب مع إنتاج خلايا عظمية جديدة الناتج عن الفعالية البانية للعظم وترسيب الكالسيوم في العظام."),
 W(Q("In liver disease, the blood ALP level rises when:", "في مرض الكبد، يرتفع مستوى ALP في الدم عندما:",
     O(("Excretion of the enzyme is impaired by obstruction in the biliary tract", "يختلّ طرح الإنزيم بسبب انسداد في القناة الصفراوية"), ("The liver stops making bile acids", "يتوقّف الكبد عن صنع الأحماض الصفراوية"), ("Blood glucose falls", "ينخفض سكّر الدم"), ("Red cells increase", "تزداد الكريات الحمراء")), "a"),
   "In liver disease, the blood level rises when excretion of the enzyme is impaired as a result of obstruction in the biliary tract.", "في مرض الكبد يرتفع المستوى في الدم عندما يختلّ طرح الإنزيم نتيجة انسداد في القناة الصفراوية."),
 W(Q("Used alone, alkaline phosphatase may be:", "عند استعماله وحده، قد يكون الفوسفاتيز القاعدي:",
     O(("Misleading", "مضلِّلًا"), ("Always diagnostic", "تشخيصيًا دائمًا"), ("Unmeasurable", "غير قابل للقياس"), ("Specific to the kidney", "نوعيًا للكلية")), "a"),
   "Used alone, alkaline phosphatase may be misleading — it is interpreted with other clinical findings.", "عند استعماله وحده قد يكون مضلِّلًا — ويُفسَّر مع الموجودات السريرية الأخرى."),

 # ───────────────────────── 3. normal values
 {"topic_en": "Normal reference values", "topic_ar": "القيم المرجعية الطبيعية"},
 W(Q("The normal ALP value for FEMALES older than 15 years is:", "القيمة الطبيعية لـ ALP عند الإناث فوق 15 سنة هي:",
     O(("25–100 U/L", "25–100 U/L"), ("<350 U/L", "<350 U/L"), ("<500 U/L", "<500 U/L"), ("5–45 U/L", "5–45 U/L")), "a"),
   "Females >15 years: 25–100 U/L (1–12 years: <350 U/L).", "الإناث فوق 15 سنة: 25–100 U/L (ومن 1–12 سنة: <350 U/L)."),
 W(Q("The normal ALP value for FEMALES aged 1–12 years is:", "القيمة الطبيعية لـ ALP عند الإناث بعمر 1–12 سنة هي:",
     O(("<350 U/L", "<350 U/L"), ("25–100 U/L", "25–100 U/L"), ("<500 U/L", "<500 U/L"), ("13–45 U/L", "13–45 U/L")), "a"),
   "Females 1–12 years: <350 U/L.", "الإناث 1–12 سنة: <350 U/L."),
 W(Q("The normal ALP value for MALES aged 12–14 years is:", "القيمة الطبيعية لـ ALP عند الذكور بعمر 12–14 سنة هي:",
     O(("<500 U/L", "<500 U/L"), ("<350 U/L", "<350 U/L"), ("25–100 U/L", "25–100 U/L"), ("10–40 U/L", "10–40 U/L")), "a"),
   "Males 12–14 years: <500 U/L (1–12 years: <350 U/L; >20 years: 25–100 U/L).", "الذكور 12–14 سنة: <500 U/L (ومن 1–12 سنة: <350 U/L؛ وفوق 20 سنة: 25–100 U/L)."),
 W(Q("The normal ALP value for MALES older than 20 years is:", "القيمة الطبيعية لـ ALP عند الذكور فوق 20 سنة هي:",
     O(("25–100 U/L", "25–100 U/L"), ("<350 U/L", "<350 U/L"), ("<500 U/L", "<500 U/L"), ("7–35 U/L", "7–35 U/L")), "a"),
   "Males >20 years: 25–100 U/L.", "الذكور فوق 20 سنة: 25–100 U/L."),

 # ───────────────────────── 4. increased ALP
 {"topic_en": "Causes of increased ALP", "topic_ar": "أسباب ارتفاع ALP"},
 W(Q("Which LIVER condition causes INCREASED ALP?", "أيّ حالة كبدية تسبّب ارتفاع ALP؟",
     O(("Obstructive jaundice / hepatic carcinoma / hepatitis / infectious mononucleosis", "اليرقان الانسدادي / سرطان الكبد / التهاب الكبد / كثرة الوحيدات العدوائية"), ("Iron-deficiency anemia", "فقر الدم بعوز الحديد"), ("Dehydration", "الجفاف"), ("Vitamin C deficiency", "نقص فيتامين C")), "a"),
   "Increased ALP in liver disease: obstructive jaundice, hepatic carcinoma, hepatocellular cirrhosis, hepatitis, infectious mononucleosis.", "يرتفع ALP في أمراض الكبد: اليرقان الانسدادي، وسرطان الكبد، وتشمّع خلايا الكبد، والتهاب الكبد، وكثرة الوحيدات العدوائية."),
 W(Q("Which BONE condition causes INCREASED ALP?", "أيّ حالة عظمية تسبّب ارتفاع ALP؟",
     O(("Metastatic bone tumor / osteogenic sarcoma / osteomalacia", "ورم العظم النقيلي / الساركومة العظمية المنشأ / تليّن العظام"), ("Osteoporosis only", "هشاشة العظام فقط"), ("Bone bruise", "رضّ العظم"), ("Normal bone growth never", "نمو العظم الطبيعي أبدًا")), "a"),
   "Increased ALP in bone disease: metastatic bone tumor, osteogenic sarcoma, and osteomalacia.", "يرتفع ALP في أمراض العظم: ورم العظم النقيلي، والساركومة العظمية المنشأ، وتليّن العظام."),
 W(Q("Which metabolic condition is listed as INCREASING ALP?", "أيّ حالة استقلابية مذكورة ترفع ALP؟",
     O(("Diabetes mellitus and diabetic hepatic lipidosis", "الداء السكّري والشحام الكبدي السكّري"), ("Hypoglycemia", "نقص سكّر الدم"), ("Dehydration", "الجفاف"), ("Gout", "النقرس")), "a"),
   "Increased ALP: diabetes mellitus and diabetic hepatic lipidosis; also chronic alcohol ingestion.", "يرتفع ALP في: الداء السكّري والشحام الكبدي السكّري؛ وكذلك تناول الكحول المزمن."),
 W(Q("Chronic ___ ingestion is listed as a cause of increased ALP.", "تناول ___ المزمن مذكور سببًا لارتفاع ALP.",
     O(("Alcohol", "الكحول"), ("Caffeine", "الكافيين"), ("Sugar", "السكّر"), ("Iron", "الحديد")), "a"),
   "Chronic alcohol ingestion increases ALP.", "يرفع تناول الكحول المزمن مستوى ALP."),

 # ───────────────────────── 5. decreased ALP
 {"topic_en": "Causes of decreased ALP", "topic_ar": "أسباب انخفاض ALP"},
 W(Q("Which endocrine condition causes DECREASED ALP?", "أيّ حالة صمّاوية تسبّب انخفاض ALP؟",
     O(("Hyperparathyroidism and hyperthyroidism", "فرط نشاط جارات الدرقية وفرط نشاط الدرقية"), ("Hypothyroidism", "قصور الدرقية"), ("Diabetes mellitus", "الداء السكّري"), ("Addison disease", "داء أديسون")), "a"),
   "Decreased ALP: hyperparathyroidism and hyperthyroidism.", "ينخفض ALP في: فرط نشاط جارات الدرقية وفرط نشاط الدرقية."),
 W(Q("Which cardiopulmonary condition is listed as DECREASING ALP?", "أيّ حالة قلبية-رئوية مذكورة تخفض ALP؟",
     O(("Pulmonary and myocardial infarctions", "الاحتشاء الرئوي والاحتشاء القلبي"), ("Myocardial infarction increases it", "الاحتشاء القلبي يرفعه"), ("Hypertension", "ارتفاع الضغط"), ("Anemia", "فقر الدم")), "a"),
   "Decreased ALP: pulmonary and myocardial infarctions.", "ينخفض ALP في: الاحتشاء الرئوي والاحتشاء القلبي."),
 W(Q("A nutritional deficiency of which minerals DECREASES ALP?", "عوز أيّ المعدنين (تغذويًا) يخفض ALP؟",
     O(("Magnesium and zinc", "المغنيسيوم والزنك"), ("Sodium and potassium", "الصوديوم والبوتاسيوم"), ("Iron and copper", "الحديد والنحاس"), ("Calcium and phosphate", "الكالسيوم والفوسفات")), "a"),
   "Decreased ALP: magnesium and zinc deficiency (nutritional).", "ينخفض ALP في: عوز المغنيسيوم والزنك (تغذويًا)."),
 W(Q("Which gastrointestinal condition is listed as DECREASING ALP?", "أيّ حالة هضمية مذكورة تخفض ALP؟",
     O(("Ulcerative colitis and peptic ulcer", "التهاب القولون التقرّحي والقرحة الهضمية"), ("Appendicitis", "التهاب الزائدة"), ("Gastritis only", "التهاب المعدة فقط"), ("Hepatitis", "التهاب الكبد")), "a"),
   "Decreased ALP: ulcerative colitis, peptic ulcer.", "ينخفض ALP في: التهاب القولون التقرّحي والقرحة الهضمية."),
 W(Q("Chronic ___ failure is listed as a cause of DECREASED ALP.", "فشل ___ المزمن مذكور سببًا لانخفاض ALP.",
     O(("Renal", "كلوي"), ("Heart", "قلبي"), ("Respiratory", "تنفّسي"), ("Hepatic", "كبدي")), "a"),
   "Decreased ALP: chronic renal failure (also cancer of lung or pancreas).", "ينخفض ALP في: الفشل الكلوي المزمن (وكذلك سرطان الرئة أو البنكرياس)."),

 # ───────────────────────── 6. sample & stability
 {"topic_en": "Sample and stability (exam T/F points)", "topic_ar": "العيّنة والثبات (نقاط صح/خطأ الامتحانية)"},
 W(Q("The sample used for the ALP test is:", "العيّنة المستعملة لفحص ALP هي:",
     O(("Serum or plasma", "المصل أو البلازما"), ("Whole blood only", "الدم الكامل فقط"), ("Urine", "البول"), ("CSF", "السائل الدماغي الشوكي")), "a"),
   "Sample: serum or plasma.", "العيّنة: المصل أو البلازما."),
 W(Q("At room temperature and in refrigerated storage, ALP levels:", "في حرارة الغرفة وفي الحفظ المبرّد، مستويات ALP:",
     O(("Increase (so testing should be done the same day)", "ترتفع (لذا يجب الفحص في اليوم نفسه)"), ("Decrease", "تنخفض"), ("Stay exactly the same", "تبقى كما هي تمامًا"), ("Become zero", "تصبح صفرًا")), "a"),
   "ALP levels increase at room temperature and in refrigerated storage; testing should be done the same day.", "ترتفع مستويات ALP في حرارة الغرفة وفي الحفظ المبرّد؛ لذا يجب إجراء الفحص في اليوم نفسه."),
 W(Q("If the blood is anticoagulated, the ALP level:", "إذا مُنع تخثّر الدم (مضاد تخثّر)، فإن مستوى ALP:",
     O(("Decreases", "ينخفض"), ("Increases", "يرتفع"), ("Doubles", "يتضاعف"), ("Is unaffected", "لا يتأثّر")), "a"),
   "ALP levels decrease if blood is anticoagulated.", "ينخفض مستوى ALP إذا مُنع تخثّر الدم بمضاد تخثّر."),
 W(Q("After fatty meals, the ALP level:", "بعد الوجبات الدهنية، مستوى ALP:",
     O(("Increases", "يرتفع"), ("Decreases", "ينخفض"), ("Is unaffected", "لا يتأثّر"), ("Falls to zero", "ينزل إلى الصفر")), "a"),
   "ALP levels increase after fatty meals.", "يرتفع مستوى ALP بعد الوجبات الدهنية."),

 # ───────────────────────── 7. principle, procedure, calculation
 {"topic_en": "Principle, procedure and calculation", "topic_ar": "المبدأ والإجراء والحساب"},
 W(Q("In the ALP assay principle, the substrate p-nitrophenylphosphate + H₂O is converted to:", "في مبدأ فحص ALP، تتحوّل المادة p-نيتروفينيل فوسفات + H₂O إلى:",
     O(("Phosphate + p-nitrophenol", "فوسفات + p-نيتروفينول"), ("Pyruvate + lactate", "بيروفات + لاكتات"), ("Oxaloacetate + malate", "أوكسالوأسيتات + مالات"), ("Glucose + water", "غلوكوز + ماء")), "a"),
   "Principle: p-nitrophenylphosphate + H₂O → phosphate + p-nitrophenol.", "المبدأ: p-نيتروفينيل فوسفات + H₂O ← فوسفات + p-نيتروفينول."),
 W(Q("The colored product measured in the ALP reaction is:", "النّاتج المُقاس في تفاعل ALP هو:",
     O(("p-nitrophenol", "p-نيتروفينول"), ("p-nitrophenylphosphate", "p-نيتروفينيل فوسفات"), ("NADH", "NADH"), ("Oxaloacetate", "أوكسالوأسيتات")), "a"),
   "ALP releases p-nitrophenol (plus phosphate) from p-nitrophenylphosphate; p-nitrophenol is followed.", "يُحرّر ALP الـ p-نيتروفينول (مع الفوسفات) من p-نيتروفينيل فوسفات؛ ويُتابَع p-نيتروفينول."),
 W(Q("In the ALP procedure, the volume of SAMPLE is:", "في إجراء ALP، حجم العيّنة هو:",
     O(("20 µL", "20 µL"), ("100 µL", "100 µL"), ("250 µL", "250 µL"), ("1000 µL", "1000 µL")), "a"),
   "Procedure: sample 20 µL, buffer (BUF) 1000 µL, mix and incubate 1 min, then substrate (SUB) 250 µL.", "الإجراء: العيّنة 20 µL، والمحلول المنظّم (BUF) 1000 µL، يُمزج ويُحضَن دقيقة، ثم المادة (SUB) 250 µL."),
 W(Q("In the ALP procedure, the volume of BUFFER (BUF) is:", "في إجراء ALP، حجم المحلول المنظّم (BUF) هو:",
     O(("1000 µL", "1000 µL"), ("20 µL", "20 µL"), ("250 µL", "250 µL"), ("100 µL", "100 µL")), "a"),
   "Buffer (BUF) = 1000 µL.", "المحلول المنظّم (BUF) = 1000 µL."),
 W(Q("In the ALP procedure, the volume of SUBSTRATE (SUB) is:", "في إجراء ALP، حجم المادة (SUB) هو:",
     O(("250 µL", "250 µL"), ("20 µL", "20 µL"), ("1000 µL", "1000 µL"), ("500 µL", "500 µL")), "a"),
   "Substrate (SUB) = 250 µL; after adding it, mix and read the absorbance after 1 min, then again after 1, 2 and 3 min.", "المادة (SUB) = 250 µL؛ وبعد إضافتها يُمزج وتُقرأ الامتصاصية بعد دقيقة، ثم تُعاد القراءة بعد 1 و2 و3 دقائق."),
 W(Q("The ALP activity is calculated as:", "يُحسب نشاط ALP بالعلاقة:",
     O(("U/L = ΔA/min × 3433", "U/L = ΔA/min × 3433"), ("U/L = ΔA/min × 1745", "U/L = ΔA/min × 1745"), ("U/L = ΔA/min × 340", "U/L = ΔA/min × 340"), ("U/L = ΔA/min ÷ 3433", "U/L = ΔA/min ÷ 3433")), "a"),
   "ALP activity: U/L = ΔA/min × 3433 (note: the transaminases ALT/AST use ×1745).", "نشاط ALP: U/L = ΔA/min × 3433 (ملاحظة: ناقلات الأمين ALT/AST تستعمل ×1745)."),
]
mcq = balance(mcq, 343)

meta = {"subject_en": "Clinical Enzymology", "subject_ar": "الإنزيمات السريرية", "short_ar": "انزيمات سريرية", "instructor": "د. بارق و د. هشام",
        "unit_en": "Lab 3", "unit_ar": "العملي 3", "unit_label": "LAB", "unit_no": "3",
        "title_en": "Serum Alkaline Phosphatase (ALP)", "title_ar": "الفوسفاتيز القاعدي في المصل",
        "kind": "Laboratories — عملي", "stage": "The fourth stage — الرابعة",
        "file_name": "BIOS - انزيمات سريرية عملي - الفوسفاتيز القاعدي - بنك أسئلة شامل"}

important = [
 IM("State the origin of ALP, why it is called “alkaline”, and what it is used to index.", "اذكر مصدر ALP، ولماذا يُسمّى «قاعديًا»، وعلامَ يُستعمل دليلًا.",
    "Alkaline phosphatase originates mainly in bone, liver and placenta, with some activity in the kidney and intestines. It is called alkaline because it functions best at a pH of 9. Its levels are age and gender dependent, and it is used as an index of liver and bone disease when correlated with other clinical findings.",
    "ينشأ الفوسفاتيز القاعدي أساسًا في العظم والكبد والمشيمة، مع بعض الفعالية في الكلية والأمعاء. ويُسمّى قاعديًا لأنه يعمل أفضل ما يكون عند أسّ هيدروجيني 9. ومستوياته تعتمد على العمر والجنس، ويُستعمل دليلًا على أمراض الكبد والعظم عند ربطه بالموجودات السريرية الأخرى."),
 IM("Explain the behaviour of ALP in bone disease versus liver disease.", "اشرح سلوك ALP في مرض العظم مقابل مرض الكبد.",
    "In bone disease, the enzyme level rises in proportion to new bone cell production resulting from osteoplastic activity and the deposit of calcium in the bones. In liver disease, the blood level rises when excretion of the enzyme is impaired as a result of obstruction in the biliary tract. Used alone, alkaline phosphatase may be misleading.",
    "في مرض العظم يرتفع مستوى الإنزيم بتناسب مع إنتاج خلايا عظمية جديدة الناتج عن الفعالية البانية للعظم وترسيب الكالسيوم في العظام. وفي مرض الكبد يرتفع المستوى في الدم عندما يختلّ طرح الإنزيم نتيجة انسداد في القناة الصفراوية. وعند استعماله وحده قد يكون مضلِّلًا."),
 IM("Give the normal ALP reference values for females and males by age.", "اذكر القيم المرجعية الطبيعية لـ ALP للإناث والذكور حسب العمر.",
    "Females — 1–12 years: <350 U/L; >15 years: 25–100 U/L. Males — 1–12 years: <350 U/L; 12–14 years: <500 U/L; >20 years: 25–100 U/L.",
    "الإناث — 1–12 سنة: <350 U/L؛ وفوق 15 سنة: 25–100 U/L. الذكور — 1–12 سنة: <350 U/L؛ و12–14 سنة: <500 U/L؛ وفوق 20 سنة: 25–100 U/L."),
 IM("Marked by the student (“memorize how many causes for each”): list the causes of INCREASED ALP and group them.", "مؤشَّر بالطالب («كل وحدة نحفظ كم سبب»): عدّد أسباب ارتفاع ALP وصنّفها.",
    "Increased ALP (4 groups): (a) Liver disease — obstructive jaundice, hepatic carcinoma, hepatocellular cirrhosis, hepatitis, infectious mononucleosis; (b) Diabetes mellitus and diabetic hepatic lipidosis; (c) Chronic alcohol ingestion; (d) Bone disease — metastatic bone tumor, osteogenic sarcoma, and osteomalacia.",
    "يرتفع ALP (4 مجموعات): (أ) أمراض الكبد — اليرقان الانسدادي، وسرطان الكبد، وتشمّع خلايا الكبد، والتهاب الكبد، وكثرة الوحيدات العدوائية؛ (ب) الداء السكّري والشحام الكبدي السكّري؛ (ج) تناول الكحول المزمن؛ (د) أمراض العظم — ورم العظم النقيلي، والساركومة العظمية المنشأ، وتليّن العظام."),
 IM("Marked by the student (“memorize how many causes for each”): list the causes of DECREASED ALP.", "مؤشَّر بالطالب («كل وحدة نحفظ كم سبب»): عدّد أسباب انخفاض ALP.",
    "Decreased ALP: (a) hyperparathyroidism and hyperthyroidism; (b) pulmonary and myocardial infarctions; (c) cancer of lung or pancreas; (d) ulcerative colitis and peptic ulcer; (e) chronic renal failure; (f) magnesium and zinc deficiency (nutritional), and others.",
    "ينخفض ALP في: (أ) فرط نشاط جارات الدرقية وفرط نشاط الدرقية؛ (ب) الاحتشاء الرئوي والاحتشاء القلبي؛ (ج) سرطان الرئة أو البنكرياس؛ (د) التهاب القولون التقرّحي والقرحة الهضمية؛ (هـ) الفشل الكلوي المزمن؛ (و) عوز المغنيسيوم والزنك (تغذويًا) وغيرها."),
 IM("Marked by the student (T/F points): how do storage/temperature, anticoagulant, and fatty meals affect ALP, and what does this mean for testing?", "مؤشَّر بالطالب (نقاط صح/خطأ): كيف تؤثّر الحفظ/الحرارة ومضاد التخثّر والوجبات الدهنية في ALP، وماذا يعني ذلك للفحص؟",
    "ALP levels INCREASE at room temperature and in refrigerated storage, so testing should be done the same day. ALP levels DECREASE if the blood is anticoagulated. ALP levels INCREASE after fatty meals. Therefore use a fresh serum/plasma sample, avoid anticoagulant interference, and consider recent fatty meals when interpreting the result.",
    "ترتفع مستويات ALP في حرارة الغرفة وفي الحفظ المبرّد، لذا يجب إجراء الفحص في اليوم نفسه. وتنخفض إذا مُنع تخثّر الدم بمضاد تخثّر. وترتفع بعد الوجبات الدهنية. لذا تُستعمل عيّنة مصل/بلازما طازجة، ويُتجنّب تداخل مضاد التخثّر، ويُراعى تناول وجبة دهنية حديثة عند تفسير النتيجة."),
 IM("State the sample used and write the principle reaction of the ALP assay.", "اذكر العيّنة المستعملة واكتب تفاعل مبدأ فحص ALP.",
    "Sample: serum or plasma. Principle: p-nitrophenylphosphate + H₂O → phosphate + p-nitrophenol (ALP releases p-nitrophenol, which is followed spectrophotometrically).",
    "العيّنة: المصل أو البلازما. المبدأ: p-نيتروفينيل فوسفات + H₂O ← فوسفات + p-نيتروفينول (يُحرّر ALP الـ p-نيتروفينول الذي يُتابَع طيفيًا)."),
 IM("Describe the ALP procedure (volumes and reading) and its calculation.", "صِف إجراء ALP (الأحجام والقراءة) وطريقة حسابه.",
    "Procedure (with starter reagent): sample 20 µL + buffer (BUF) 1000 µL, mix and incubate 1 min; then add substrate (SUB) 250 µL, mix, read the absorbance after 1 min and again after 1, 2 and 3 min. Calculation: ALP activity (U/L) = ΔA/min × 3433.",
    "الإجراء (بكاشف بادئ): العيّنة 20 µL + المحلول المنظّم (BUF) 1000 µL، يُمزج ويُحضَن دقيقة؛ ثم تُضاف المادة (SUB) 250 µL، يُمزج، وتُقرأ الامتصاصية بعد دقيقة ثم بعد 1 و2 و3 دقائق. والحساب: نشاط ALP (U/L) = ΔA/min × 3433."),
 IM("Why may alkaline phosphatase be misleading when used alone, and what improves its diagnostic value?", "لماذا قد يكون الفوسفاتيز القاعدي مضلِّلًا عند استعماله وحده، وما الذي يحسّن قيمته التشخيصية؟",
    "ALP rises in both liver and bone disease (and in pregnancy/growth because of placental and bone sources), so a high value alone does not localize the problem. It becomes useful when correlated with other clinical findings and tests (e.g. other liver enzymes, bilirubin, calcium/phosphate, clinical picture).",
    "يرتفع ALP في مرض الكبد ومرض العظم معًا (وفي الحمل/النمو بسبب المصدرين المشيمي والعظمي)، فالقيمة المرتفعة وحدها لا تحدّد موضع المشكلة. ويصبح مفيدًا عند ربطه بالموجودات والفحوص السريرية الأخرى (مثل إنزيمات الكبد الأخرى، والبيليروبين، والكالسيوم/الفوسفات، والصورة السريرية)."),
 IM("Marked by the student: why does the ALP calculation use ×3433 while the transaminases use ×1745?", "مؤشَّر بالطالب: لماذا يستعمل حساب ALP ×3433 بينما تستعمل ناقلات الأمين ×1745؟",
    "The multiplication factor is a method/assay-specific constant that converts the measured change in absorbance per minute (ΔA/min) into enzyme activity in U/L; it depends on the molar absorptivity of the product followed, the wavelength, the light path and the sample/reagent volumes. ALP (following p-nitrophenol) uses ×3433, whereas the NADH-coupled transaminase methods (ALT/AST) use ×1745.",
    "معامل الضرب ثابت خاص بالطريقة/الفحص يحوّل التغيّر المقاس في الامتصاصية بالدقيقة (ΔA/min) إلى نشاط إنزيمي بوحدة U/L؛ ويعتمد على الامتصاصية المولارية للناتج المتابَع، والطول الموجي، ومسار الضوء، وأحجام العيّنة والكاشف. فـ ALP (بمتابعة p-نيتروفينول) يستعمل ×3433، بينما طرائق ناقلات الأمين المقترنة بـ NADH (ALT/AST) تستعمل ×1745."),
]

Qs = {"title_en": "Serum Alkaline Phosphatase (ALP) — Comprehensive Questions (MCQ + SA)",
      "title_ar": "الفوسفاتيز القاعدي في المصل (ALP) — أسئلة شاملة (اختيار + مقالية)",
      "answers_inline": True, "mcq": ltr_all(mcq), "tf": [], "traps": [], "important": ltr_all(important)}
d = "/home/user/-/" + FOLDER
os.makedirs(d, exist_ok=True)
json.dump({"meta": meta, "questions": Qs}, open(d + "/lecture.json", "w"), ensure_ascii=False, indent=1)
from collections import Counter
qs = [m for m in mcq if "answer" in m]
print(FOLDER, len(qs), "MCQ", dict(Counter(m["answer"] for m in qs)), "| SA:", len(important), "| notes:", sum(1 for m in qs if m.get("note_en")))
