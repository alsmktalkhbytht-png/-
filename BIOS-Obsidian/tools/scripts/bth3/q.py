import sys, json, os
from collections import Counter
WORK = "/home/claude/scratch/work"
sys.path.insert(0, WORK + "/bac"); from bal import balance
sys.path.insert(0, WORK); from bidi import ltr_all

# Diagnostic Microbiology — THEORY Lectures 3+4+5 (stage 4, د. عدنان): Selection, collection, and transport of specimens for
# microbiological examination. Source 2026-11-22: a Kilonotes copy of a student summary («Medical laboratory», Telegram @hu5ks,
# Husein K. J) — 5 pages: cover + 4 pages of bilingual text with highlights (green/pink/yellow) and one handwritten note on
# p.1 ("إذا تأخرت العينة 2h → 4C°; إذا … يومين −20" — partly illegible → NOT asked, told to the user). No crossed-out parts.
# Figures (diagnostic pattern; AI-generated collage with garbled text) are not used. Text-layer typos kept: "a major steps",
# "prefect" (= protect). "Concurrent antimicrobial therapy" here (lab 2 slide said "treatment history and antimicrobial therapy").
# Comprehensive bank (MCQ + SA), same pattern as lectures 1–2.

def Q(en, ar, opts, why_en, why_ar, fixed=None):
    d = dict(en=en, ar=ar, options=[list(o) for o in opts], note_en=why_en, note_ar=why_ar)
    if fixed: d["_fixed"] = fixed
    else: d["answer"] = "a"
    return d
def T(en, ar): return {"topic_en": en, "topic_ar": ar}
def IM(en, ar, ae, aa): return dict(en=en, ar=ar, answer_en=ae, answer_ar=aa)
ALL = ("All of the above", "جميع ما سبق")
S = lambda x: f"__{x}__"

mcq = [
 T("The role of the laboratory", "دور المختبر"),
 Q("The role of the laboratory in the diagnosis of infections can be considered:", "يمكن عدّ دور المختبر في تشخيص العدوى:",
   [("A major step of diagnostic microbiology", "خطوة رئيسية في علم الأحياء الدقيقة التشخيصي"), ("A minor step", "خطوة ثانوية"),
    ("An administrative step only", "خطوة إدارية فقط"), ("Unrelated to diagnosis", "غير مرتبط بالتشخيص")],
   "The file writes “a major steps” (sic).", "الملف كتب «a major steps» كما هو."),
 Q("If pathogens are to be isolated successfully, which of the following must be correct?", "لكي تُعزل الممرضات بنجاح، أيّ مما يأتي يجب أن يكون صحيحًا؟",
   [("The type of specimen and its collection", "نوع العيّنة وجمعها"), ("The time of the specimen", "وقت العيّنة"),
    ("The method of its dispatch to the laboratory", "طريقة إرسالها إلى المختبر"), ALL],
   "Four things: type, collection, time, method of dispatch.", "أربعة أشياء: النوع، الجمع، الوقت، طريقة الإرسال.", fixed="d"),

 T("The request form", "نموذج الطلب"),
 Q("A detailed request form that accompanies a clinical sample is pivotal in:", "نموذج الطلب التفصيلي المرافق للعيّنة السريرية محوري في:",
   [("Ensuring the appropriate diagnostic procedures are undertaken", "ضمان إجراء الفحوص التشخيصية المناسبة"), ("Reducing the price", "تقليل السعر"),
    ("Sterilizing the sample", "تعقيم العيّنة"), ("Replacing the culture", "الاستغناء عن الزرع")],
   "Highlighted in the file.", "مظلَّل في الملف."),
 Q("Which of the following should be included in the request form?", "أيّ مما يأتي يجب أن يتضمّنه نموذج الطلب؟",
   [("Patient details", "تفاصيل المريض"), ("Sample type", "نوع العيّنة"), ("Time of collection", "وقت الجمع"), ALL],
   "Seven items; this question was unsolved in the 2024 file (answer: all).", "سبعة بنود؛ وهذا السؤال كان غير محلول في ملف 2024 (الجواب: الكل).", fixed="d"),
 Q("Item 6 of the request form is:", "البند 6 في نموذج الطلب:",
   [("Treatment history and concurrent antimicrobial therapy", "تاريخ العلاج والعلاج المتزامن بمضادات الميكروبات"), ("The patient's blood group", "زمرة دم المريض"),
    ("The cost of the test", "كلفة الفحص"), ("The doctor's phone number", "رقم هاتف الطبيب")],
   "Highlighted.", "مظلَّل."),
 Q("How many items of information should the request form include?", "كم بندًا من المعلومات يجب أن يتضمّن نموذج الطلب؟",
   [("7", "7"), ("4", "4"), ("5", "5"), ("10", "10")],
   "Patient details, clinical diagnosis, onset of symptoms, sample type, time of collection, treatment history, other health and safety issues.",
   "تفاصيل المريض، التشخيص السريري، ظهور الأعراض، نوع العيّنة، وقت الجمع، تاريخ العلاج، قضايا الصحة والسلامة الأخرى."),
 Q("Which of the following is NOT one of the request form items?", "أيّ مما يأتي ليس من بنود نموذج الطلب؟",
   [("The patient's income", "دخل المريض"), ("Clinical diagnosis", "التشخيص السريري"), ("Onset of symptoms", "ظهور الأعراض"), ("Other health and safety issues", "قضايا الصحة والسلامة الأخرى")],
   "Not on the list.", "ليس في القائمة."),
 Q("Supporting clinical information that is also important includes:", "المعلومات السريرية الداعمة المهمة أيضًا تشمل:",
   [("Travel history and contact with infected individuals", "تاريخ السفر والتماس مع أشخاص مصابين"), ("The patient's hobbies", "هوايات المريض"),
    ("The patient's job title only", "وظيفة المريض فقط"), ("The hospital name", "اسم المستشفى")],
   "Last sentence of page 1.", "آخر جملة في الصفحة 1."),

 T("Sample collection", "جمع العيّنات"),
 Q("Samples for microbiological investigation require careful collection without contamination from:", "تتطلّب عيّنات الفحص الميكروبيولوجي جمعًا دقيقًا دون تلوّث من:",
   [("External sources or the patient's own flora", "مصادر خارجية أو فلورا المريض نفسه"), ("Sterile containers", "الحاويات المعقّمة"),
    ("Transport media", "أوساط النقل"), ("Antiseptics", "المطهّرات")],
   "Sample collection, first point.", "جمع العيّنات، النقطة الأولى."),
 Q("When taking clinical samples, it is important to use:", "عند أخذ العيّنات السريرية من المهم استعمال:",
   [("Sterile, leak-proof containers", "حاويات معقّمة مانعة للتسرّب"), ("Any clean cup", "أي كوب نظيف"),
    ("Paper bags", "أكياس ورقية"), ("Reused containers", "حاويات مُعاد استعمالها")],
   "Point 1 (highlighted).", "النقطة 1 (مظلَّلة)."),
 Q("When obtaining blood culture by vein puncture through the skin, the skin should be:", "عند سحب زرع الدم بثقب الوريد عبر الجلد، يجب أن يكون الجلد:",
   [("Decontaminated with an appropriate antiseptic prior to collecting blood", "مطهَّرًا بمطهّر مناسب قبل سحب الدم"), ("Washed with water only", "مغسولًا بالماء فقط"),
    ("Left untreated", "بلا أي معالجة"), ("Heated", "مسخَّنًا")],
   "Because the skin contains a normal flora.", "لأن الجلد يحتوي فلورا طبيعية."),
 Q("Specimens for microbiological culture should be taken prior to antibiotic therapy to avoid:", "يجب أخذ العيّنات للزرع قبل العلاج بالمضادات الحيوية لتجنّب:",
   [("False-negative results", "النتائج السلبية الكاذبة"), ("False-positive results", "النتائج الإيجابية الكاذبة"),
    ("Contamination", "التلوّث"), ("Leakage", "التسرّب")],
   "Point 4; a 2023-exam question.", "النقطة 4؛ ومن أسئلة امتحان 2023."),
 Q("Vein puncture through the skin is an example of obtaining samples through:", "ثقب الوريد عبر الجلد مثال على أخذ العيّنات عبر:",
   [("An area containing a normal flora", "منطقة تحتوي فلورا طبيعية"), ("A sterile body site", "موقع معقّم من الجسم"),
    ("A transport medium", "وسط نقل"), ("A biosafety cabinet", "خزانة سلامة حيوية")],
   "Point 3.", "النقطة 3."),

 T("Transport of microbiological specimens", "نقل العيّنات الميكروبيولوجية"),
 Q("Rapid transport of samples to the microbiology laboratory is essential because:", "النقل السريع للعيّنات إلى المختبر ضروري لأن:",
   [("Many fastidious microorganisms die during transit", "كائنات صعبة النمو كثيرة تموت أثناء النقل"), ("Samples freeze", "العيّنات تتجمّد"),
    ("Labels fall off", "الملصقات تسقط"), ("The cost increases", "الكلفة تزيد")],
   "First transport point.", "أول نقطة في النقل."),
 Q("Examples of fastidious microorganisms that die during transit are:", "أمثلة الكائنات صعبة النمو التي تموت أثناء النقل:",
   [(S("Neisseria gonorrhoeae") + " and " + S("Haemophilus influenzae"), "النيسرية البنية والمستدمية النزلية"),
    (S("E. coli") + " and " + S("Staphylococcus aureus"), "الإشريكية القولونية والعنقودية الذهبية"),
    (S("Klebsiella") + " and " + S("Proteus"), "الكلبسيلة والمتقلّبة"), (S("Bacillus subtilis"), "العصوية الرقيقة")],
   "Underlined and highlighted; a 2023-exam question.", "مسطَّر ومظلَّل؛ ومن أسئلة امتحان 2023."),
 Q("Another problem of delayed transport is:", "مشكلة أخرى للنقل المتأخّر:",
   [("Overgrowth by contaminating normal flora confusing the pathogen", "النمو المفرط للفلورا الطبيعية الملوِّثة مما يربك التعرّف على الممرض"),
    ("The pathogen multiplies too fast to identify", "تكاثر الممرض بسرعة"), ("The container melts", "ذوبان الحاوية"), ("Loss of the request form", "ضياع نموذج الطلب")],
   "Second transport point.", "النقطة الثانية في النقل."),

 T("Strategies to minimize transport complications", "استراتيجيات تقليل مشكلات النقل"),
 Q("If the specimen cannot reach the laboratory as soon as possible:", "إذا لم تصل العيّنة إلى المختبر بأسرع وقت:",
   [("A suitable preservative or transport medium must be used", "يجب استعمال حافظ أو وسط نقل مناسب"), ("It must be discarded", "يجب التخلّص منها"),
    ("It must be heated", "يجب تسخينها"), ("Antibiotics must be added", "يجب إضافة مضادات حيوية")],
   "Strategy 1.", "الاستراتيجية 1."),
 Q("Refrigeration of the sample at `4 ºC` helps to:", "تبريد العيّنة عند `4 ºC` يساعد على:",
   [("Preserve cells and reduce the multiplication of commensals in unpreserved specimens", "حفظ الخلايا وتقليل تكاثر المتعايشات في العيّنات غير المحفوظة"),
    ("Kill all pathogens", "قتل جميع الممرضات"), ("Increase pathogen growth", "زيادة نمو الممرض"), ("Sterilize the specimen", "تعقيم العيّنة")],
   "Strategy 2; a 2023-exam question.", "الاستراتيجية 2؛ ومن أسئلة امتحان 2023."),
 Q("Freezing of specimens is done at:", "يكون تجميد العيّنات عند:",
   [("`-70 ºC` or below with a stabilizing fluid", "`-70 ºC` أو أقل مع سائل مثبِّت"), ("`4 ºC`", "`4 ºC`"), ("`0 ºC`", "`0 ºC`"), ("`-4 ºC`", "`-4 ºC`")],
   "Strategy 3.", "الاستراتيجية 3."),
 Q("The stabilizing fluid used when freezing specimens is:", "السائل المثبِّت المستعمل عند تجميد العيّنات:",
   [("Glycerol or serum", "الغليسرول أو المصل"), ("Alcohol", "الكحول"), ("Phenol", "الفينول"), ("Formalin", "الفورمالين")],
   "Glycerol was the answer in the 2023 exam.", "الغليسرول كان جواب امتحان 2023."),
 Q("To prevent loosening and leakage of the container cap during transit, you should:", "لمنع ارتخاء غطاء الحاوية والتسرّب أثناء النقل:",
   [("Seal round the cap with adhesive tape", "إحكام الغطاء بشريط لاصق"), ("Freeze the container", "تجميد الحاوية"),
    ("Use a paper cap", "استعمال غطاء ورقي"), ("Fill the container to the top", "ملء الحاوية حتى آخرها")],
   "Strategy 5.", "الاستراتيجية 5."),
 Q("If the specimen container is a glass tube or bottle:", "إذا كانت حاوية العيّنة أنبوبًا أو قنينة زجاجية:",
   [("Use sufficient packaging material to protect it", "استعمل مادة تغليف كافية لحمايتها"), ("Use absorbent material only", "استعمل مادة ماصّة فقط"),
    ("Use no packaging", "لا تستعمل أي تغليف"), ("Freeze it", "جمّدها")],
   "The file writes “prefect” — a typo for “protect”.", "الملف كتب «prefect» وصوابها «protect»."),
 Q("If the specimen is fluid:", "إذا كانت العيّنة سائلة:",
   [("Use sufficient absorbent material to absorb it", "استعمل مادة ماصّة كافية لامتصاصها"), ("Use packaging material only", "استعمل مادة تغليف فقط"),
    ("Dry it first", "جفّفها أولًا"), ("Add glycerol", "أضف الغليسرول")],
   "Strategy 7.", "الاستراتيجية 7."),
 Q("All specimens that may contain a highly infectious organism must be marked:", "جميع العيّنات التي قد تحتوي كائنًا شديد العدوى يجب وسمها بـ:",
   [("“HIGH RISK”", "«HIGH RISK» (عالية الخطورة)"), ("“LOW RISK”", "«LOW RISK»"), ("“NO RISK”", "«NO RISK»"), ("“STERILE”", "«STERILE»")],
   "Strategy 8; a 2023-exam question.", "الاستراتيجية 8؛ ومن أسئلة امتحان 2023."),
 Q("How many strategies to minimize transport complications are listed?", "كم استراتيجية لتقليل مشكلات النقل مذكورة؟",
   [("8", "8"), ("4", "4"), ("6", "6"), ("10", "10")],
   "Numbered (1)–(8).", "مرقّمة من (1) إلى (8)."),

 T("Non-culture techniques", "التقنيات غير الزرعية"),
 Q("Following receipt of the sample, the laboratory may use non-culture techniques to:", "بعد استلام العيّنة قد يستعمل المختبر التقنيات غير الزرعية لـ:",
   [("Provide rapid clinical information that may benefit patient management", "تقديم معلومات سريرية سريعة قد تفيد في تدبير المريض"),
    ("Replace the request form", "الاستغناء عن نموذج الطلب"), ("Sterilize the sample", "تعقيم العيّنة"), ("Slow down diagnosis", "إبطاء التشخيص")],
   "Highlighted: “provide rapid clinical information”.", "المظلَّل: «تقديم معلومات سريرية سريعة»."),
 Q("Non-culture techniques are of importance when:", "تكون التقنيات غير الزرعية مهمة عندما:",
   [("The microorganism cannot be readily cultured in vitro", "لا يمكن زرع الكائن بسهولة في المختبر"), ("The microorganism is slow-growing", "يكون الكائن بطيء النمو"),
    ("Rapid diagnosis significantly influences clinical management", "يؤثّر التشخيص السريع كثيرًا في التدبير السريري"), ALL],
   "Three situations; a 2023-exam question.", "ثلاث حالات؛ ومن أسئلة امتحان 2023.", fixed="d"),
 Q("Non-culture techniques include:", "تشمل التقنيات غير الزرعية:",
   [("Direct microscopy and immunological methods", "الفحص المجهري المباشر والطرق المناعية"), ("Serology", "الفحوص المصلية"),
    ("Nucleic acid amplification techniques (NAAT)", "تقنيات تضخيم الحمض النووي (NAAT)"), ALL],
   "Four techniques; a 2023-exam question.", "أربع تقنيات؛ ومن أسئلة امتحان 2023.", fixed="d"),
 Q("Which of the following is NOT a non-culture technique?", "أيّ مما يأتي ليس تقنية غير زرعية؟",
   [("Blood culture on agar", "زرع الدم على الأجار"), ("Serology", "الفحوص المصلية"), ("Direct microscopy", "الفحص المجهري المباشر"), ("NAAT", "NAAT")],
   "Culture is, by definition, not a non-culture technique.", "الزرع بالتعريف ليس تقنية غير زرعية."),
]

important = [
 IM("What must be correct if pathogens are to be isolated successfully?", "ما الذي يجب أن يكون صحيحًا لعزل الممرضات بنجاح؟",
    "The type of specimen, its collection, time and method of its dispatch to the laboratory must be correct.",
    "يجب أن يكون نوع العيّنة وجمعها ووقتها وطريقة إرسالها إلى المختبر صحيحة."),
 IM("List the information that the request form accompanying a clinical sample should include.", "عدّد المعلومات التي يجب أن يتضمّنها نموذج الطلب المرافق للعيّنة السريرية.",
    "1) Patient details. 2) Clinical diagnosis. 3) Onset of symptoms. 4) Sample type. 5) Time of collection. 6) Treatment history and concurrent antimicrobial therapy. 7) Other health and safety issues. Supporting clinical information, including travel history and contact with infected individuals, is also important.",
    "1) تفاصيل المريض. 2) التشخيص السريري. 3) ظهور الأعراض. 4) نوع العيّنة. 5) وقت الجمع. 6) تاريخ العلاج والعلاج المتزامن بمضادات الميكروبات. 7) قضايا الصحة والسلامة الأخرى. والمعلومات السريرية الداعمة، كتاريخ السفر والتماس مع المصابين، مهمة أيضًا."),
 IM("When taking clinical samples, what is it important to do?", "عند أخذ العيّنات السريرية، ما الذي من المهم القيام به؟",
    "1) Use sterile, leak-proof containers. 2) Label the specimen correctly. 3) Take care whilst obtaining samples through an area containing a normal flora — e.g. vein puncture through the skin for blood culture, where the skin should be decontaminated with an appropriate antiseptic prior to collecting blood. 4) If possible, take specimens for microbiological culture prior to antibiotic therapy, to avoid false-negative results.",
    "1) استعمال حاويات معقّمة مانعة للتسرّب. 2) وسم العيّنة بشكل صحيح. 3) الحذر عند أخذ العيّنات عبر منطقة فيها فلورا طبيعية — مثل ثقب الوريد عبر الجلد لزرع الدم، إذ يجب تطهير الجلد بمطهّر مناسب قبل سحب الدم. 4) أخذ عيّنات الزرع قبل العلاج بالمضادات الحيوية إن أمكن، لتجنّب النتائج السلبية الكاذبة."),
 IM("Why is rapid transport of samples to the microbiology laboratory essential?", "لماذا يُعدّ النقل السريع للعيّنات إلى مختبر الأحياء الدقيقة ضروريًّا؟",
    "Because many fastidious microorganisms, such as Neisseria gonorrhoeae and Haemophilus influenzae, die during transit. Furthermore, overgrowth by contaminating normal flora confusing the pathogen may also occur.",
    "لأن كائنات صعبة النمو كثيرة، مثل النيسرية البنية والمستدمية النزلية، تموت أثناء النقل. وفوق ذلك قد يحدث نمو مفرط للفلورا الطبيعية الملوِّثة يربك التعرّف على الممرض."),
 IM("List the strategies that the microbiology department may adopt to minimize transport complications.", "عدّد الاستراتيجيات التي قد يتّبعها قسم الأحياء الدقيقة لتقليل مشكلات النقل.",
    "(1) The specimen should reach the laboratory as soon as possible, or a suitable preservative or transport medium must be used. (2) Refrigeration at 4 °C to preserve cells and reduce the multiplication of commensals. (3) Freezing at −70 °C or below with a stabilizing fluid such as glycerol or serum. (4) Ensure the container is free from cracks and the cap is leak-proof. (5) Seal round the cap with adhesive tape. (6) For a glass tube or bottle, use sufficient packaging material to protect the specimen. (7) For a fluid specimen, use sufficient absorbent material. (8) Mark all specimens that may contain a highly infectious organism “HIGH RISK”.",
    "(1) وصول العيّنة إلى المختبر بأسرع وقت، أو استعمال حافظ أو وسط نقل مناسب. (2) التبريد عند 4 درجات لحفظ الخلايا وتقليل تكاثر المتعايشات. (3) التجميد عند −70 درجة أو أقل مع سائل مثبِّت كالغليسرول أو المصل. (4) التأكّد من خلوّ الحاوية من الشقوق وأن الغطاء مانع للتسرّب. (5) إحكام الغطاء بشريط لاصق. (6) للأنبوب أو القنينة الزجاجية: مادة تغليف كافية لحماية العيّنة. (7) للعيّنة السائلة: مادة ماصّة كافية. (8) وسم كل عيّنة قد تحتوي كائنًا شديد العدوى بـ«HIGH RISK»."),
 IM("When are non-culture techniques important, and what do they include?", "متى تكون التقنيات غير الزرعية مهمة، وماذا تشمل؟",
    "They provide rapid clinical information that may benefit patient management. They are important when: the microorganism cannot be readily cultured in vitro; the microorganism is slow-growing; or rapid laboratory diagnosis significantly influences clinical management of the patient. They include: 1) direct microscopy, 2) immunological methods, 3) serology, 4) nucleic acid amplification techniques (NAAT).",
    "تقدّم معلومات سريرية سريعة قد تفيد في تدبير المريض. وتكون مهمة عندما: لا يمكن زرع الكائن بسهولة في المختبر؛ أو يكون بطيء النمو؛ أو يؤثّر التشخيص المختبري السريع كثيرًا في التدبير السريري للمريض. وتشمل: 1) الفحص المجهري المباشر، 2) الطرق المناعية، 3) الفحوص المصلية، 4) تقنيات تضخيم الحمض النووي (NAAT)."),
]

mcq = balance(mcq, 7303)
for q in mcq:
    if "_fixed" in q: q["answer"] = q.pop("_fixed")

meta = {"subject_en": "Diagnostic Microbiology", "subject_ar": "الأحياء المجهرية التشخيصية", "short_ar": "بكتريا",
        "instructor": "د. عدنان", "unit_en": "Lectures 3–5", "unit_ar": "المحاضرات 3–5", "unit_label": "LEC", "unit_no": "3-5",
        "title_en": "Selection, Collection, and Transport of Specimens", "title_ar": "اختيار العيّنات وجمعها ونقلها",
        "department": "قسم التحليلات", "kind": "Theory — نظري", "questions_kind": "MCQ + SA — اختيار ومقالية",
        "stage": "The fourth stage — الرابعة",
        "file_name": "BIOS - بكتريا نظري المحاضرات 3 و4 و5 - بنك أسئلة شامل"}
Qs = {"title_en": "Specimens (Lectures 3–5) — Comprehensive Questions (MCQ + SA)",
      "title_ar": "العيّنات (المحاضرات 3–5) — أسئلة شاملة (اختيار + مقالية)",
      "answers_inline": True, "compact": True, "mcq_per_page": 4,
      "mcq_en": "Comprehensive MCQs — Lectures 3–5", "mcq_ar": "أسئلة اختيار شاملة — المحاضرات 3 و4 و5",
      "intro_en": ["Q. Select the most correct answer from the followings",
                   "These questions cover the whole lecture; the answer and a short reason sit under each MCQ, and the model answer under each essay question. Questions that came in the 2023 exams are noted."],
      "intro_ar": ["س. اختر الإجابة الأصح مما يأتي",
                   "هذه الأسئلة تغطّي المحاضرة كاملة؛ والحل وسطر سبب مختصر تحت كل سؤال اختيار، والجواب النموذجي تحت كل سؤال مقالي. والأسئلة التي جاءت في امتحانات 2023 مذكورة."],
      "mcq": ltr_all(mcq), "tf": [], "traps": [], "important": ltr_all(important)}

d = "/home/user/-/bacteriology-lec3-5-mcq"
os.makedirs(d, exist_ok=True)
json.dump({"meta": meta, "questions": Qs}, open(d + "/lecture.json", "w"), ensure_ascii=False, indent=1)
qs = [m for m in mcq if "answer" in m]
print("MCQ:", len(qs), "| SA:", len(important), "| dist:", dict(Counter(m["answer"] for m in qs)))
for i, q in enumerate(qs, 1):
    print(i, q["answer"], q["options"]["abcd".index(q["answer"])][0][:60])
