import json, os
from collections import Counter

def C(en, ar, **k):  return dict(t="card", en=en, ar=ar, **k)
def SEC(en, ar):     return dict(t="section", en=en, ar=ar)
def H2(en, ar):      return dict(t="h2", en=en, ar=ar)
def L(en_items, ar_items, en="", ar="", **k):
    return dict(t="card", en=en, ar=ar, list_en=en_items, list_ar=ar_items, **k)
def T(head, rows, **k): return dict(t="table", head=head, rows=rows, **k)
def F(src, en, ar, **k): return dict(t="figure", src="assets/" + src, en=en, ar=ar, **k)
def FF(*items):
    return dict(t="figures", items=[dict(src="assets/" + s, en=e, ar=a, h=h, fit="contain") for s, e, a, h in items])
def Q(en, ar, opts, ans, **k):
    return dict(en=en, ar=ar, options=[list(o) for o in opts], answer=ans, **k)
def TF(en, ar, a): return dict(en=en, ar=ar, answer=a)
def TR(en, ar, ae, aa): return dict(en=en, ar=ar, answer_en=ae, answer_ar=aa)
IM = TR

blocks = [
 C("Prepared by: MSc. Ammar hassn — MSc. Ali Thamer", "إعداد: م. عمار حسن — م. علي ثامر (ماجستير)"),

 SEC("Selection, collection, and transportation of specimens for microbiological examination",
     "اختيار العيّنات وجمعها ونقلها للفحص الميكروبيولوجي"),
 C("The role of the laboratory in the diagnosis of infections can be considered a major steps of diagnostic microbiology.",
   "يمكن عدّ دور المختبر في تشخيص الإصابات من الخطوات الرئيسة في الأحياء المجهرية التشخيصية."),
 L(["the type of specimen", "collection of specimen", "time of specimen", "method of its dispatch to the laboratory must be correct."],
   ["نوع العيّنة", "جمع العيّنة", "وقت العيّنة", "وطريقة إرسالها إلى المختبر يجب أن تكون صحيحة."],
   en="If pathogens are to be isolated successfully", ar="إذا أُريد عزل المُمرِضات بنجاح، فإنّ:"),

 L(["Patient details.", "Clinical diagnosis.", "Onset of symptoms", "Sample type.", "Time of collection.",
    "Treatment history and antimicrobial therapy.", "Other health and safety issues.",
    "Supporting clinical information, including travel history and contact with infected individuals, is also important."],
   ["معلومات المريض.", "التشخيص السريري.", "بداية ظهور الأعراض", "نوع العيّنة.", "وقت الجمع.",
    "تاريخ العلاج والعلاج بمضادات الميكروبات.", "قضايا صحية وأمنية أخرى.",
    "والمعلومات السريرية الداعمة، ومنها تاريخ السفر والتماس مع الأفراد المصابين، مهمّة أيضًا."],
   en="A detailed request form that accompanies a clinical sample is pivotal in ensuring the appropriate diagnostic procedures are undertaken; information should include:",
   ar="استمارة الطلب المفصّلة التي ترافق العيّنة السريرية أساسية لضمان إجراء الفحوص التشخيصية المناسبة؛ ويجب أن تتضمّن المعلومات:"),

 SEC("Transport of microbiological specimens", "نقل العيّنات الميكروبيولوجية"),
 L(["Specimen should reach to the laboratory as soon as possible or a suitable preservative or transport medium must be used.",
    "Refrigeration of sample at 4 ºC can help to preserve cells and reduce the multiplication of commensals in unpreserved specimens.",
    "Freezing at -70 ºC or below In the presence of a stabilizing fluid, like glycerol or serum.",
    "Ensure that the specimen container is free from cracks, and the cap is leak proof.",
    "Seal round the container cap with adhesive tape to prevent loosening and leakage during transit.",
    "If the container is glass tube or bottle, use sufficient packaging material to prefect a specimen.",
    "If the specimen is fluid, use sufficient absorbent material to absorb it.",
    "Mark all specimen that may contain highly infectious organism “HIGH RISK”."],
   ["يجب أن تصل العيّنة إلى المختبر بأسرع وقت ممكن، وإلّا وجب استعمال مادة حافظة أو وسط نقل مناسب.",
    "تبريد العيّنة بدرجة 4 °م يساعد على حفظ الخلايا وتقليل تكاثر الكائنات المتعايشة في العيّنات غير المحفوظة.",
    "التجميد بدرجة سالب 70 °م أو أقل بوجود سائل مثبّت مثل الغليسيرول أو المصل.",
    "تأكّد من أنّ وعاء العيّنة خالٍ من الشقوق وأنّ غطاءه محكم لا يسرّب.",
    "أحكم إغلاق محيط غطاء الوعاء بشريط لاصق لمنع ارتخائه وتسرّبه أثناء النقل.",
    "إذا كان الوعاء أنبوبًا أو قنينة زجاجية، فاستعمل مواد تغليف كافية لحماية العيّنة (`prefect`).",
    "إذا كانت العيّنة سائلة، فاستعمل مادة ماصّة كافية لامتصاصها.",
    "علّم كل العيّنات التي قد تحتوي على كائنات شديدة العدوى بعبارة «خطر عالٍ» (`HIGH RISK`)."]),

 SEC("Non-culture techniques", "التقنيات غير الزرعية"),
 C("Following receipt of the sample, the microbiology laboratory may utilize non- culture techniques to provide rapid clinical information, which may benefit patient management.",
   "بعد استلام العيّنة، قد يستعمل مختبر الأحياء المجهرية تقنيات غير زرعية لتوفير معلومات سريرية سريعة قد تفيد في إدارة حالة المريض."),
 L(["Microorganism cannot be readily cultured in vitro;",
    "Microorganism is slow-growing;",
    "Rapid laboratory diagnosis significantly influences clinical management of the patient."],
   ["لا يمكن زرع الكائن المجهري بسهولة خارج الجسم؛",
    "الكائن المجهري بطيء النمو؛",
    "التشخيص المختبري السريع يؤثّر بشكل كبير في الإدارة السريرية للمريض."],
   en="There are several situations where non-culture techniques are of importance:",
   ar="هناك عدّة حالات تكون فيها التقنيات غير الزرعية مهمّة:"),
 C("-Non-culture techniques include: (direct microscopy, immunological methods, serology, and nucleic acid amplification techniques (NAAT).",
   "تشمل التقنيات غير الزرعية: (الفحص المجهري المباشر، والطرائق المناعية، والفحوص المصلية، وتقنيات تضخيم الحمض النووي (`NAAT`)."),

 SEC("Principles of Specimen Collection", "مبادئ جمع العيّنات"),
 L(["Collect from correct site.", "Collect before antibiotics.", "Use aseptic technique.", "Collect sufficient quantity.",
    "Label properly.", "Use sterile containers.", "Transport immediately."],
   ["اجمع من الموقع الصحيح.", "اجمع قبل المضادات الحيوية.", "استعمل التقنية المعقّمة.", "اجمع كمية كافية.",
    "علّم العيّنة بشكل صحيح.", "استعمل أوعية معقّمة.", "انقل العيّنة فورًا."]),

 SEC("Collection Techniques", "تقنيات الجمع"),
 L(["**Blood:** aseptic collection.", "**Urine:** midstream clean-catch.", "**Sputum:** deep cough specimen.",
    "**Swabs:** sterile cotton, avoid normal flora.", "**Stool:** small amount, avoid urine.", "**CSF:** lumbar puncture."],
   ["**الدم:** جمع معقّم.", "**الإدرار:** عيّنة منتصف الإدرار النظيفة.", "**القشع:** عيّنة من سعال عميق.",
    "**المسحات:** قطن معقّم، مع تجنّب النبيت الطبيعي.", "**البراز:** كمية صغيرة، مع تجنّب الإدرار.", "**السائل الدماغي الشوكي** (`CSF`): البزل القطني."]),
 FF(("swabs.jpg", "Image 01: specimen/swab image", "الصورة 01: مسحات جمع العيّنات", "40mm"),
    ("swab-transport.jpg", "Image 02: swab with transport media", "الصورة 02: مسحة مع وسط النقل", "40mm")),
 FF(("sputum-container.jpg", "Image 03: sputum container", "الصورة 03: وعاء القشع", "40mm"),
    ("specimen-container.jpg", "Image 04: specimen container", "الصورة 04: وعاء العيّنة", "40mm")),

 SEC("Common Errors to Avoid", "أخطاء شائعة يجب تجنّبها"),
 L(["✗ Collecting after antibiotics", "✗ Contaminated containers", "✗ Delayed transport", "✗ Missing labels", "✗ Insufficient specimen"],
   ["الجمع بعد المضادات الحيوية", "أوعية ملوّثة", "تأخّر النقل", "غياب العلامات (الملصقات)", "عيّنة غير كافية"]),

 SEC("Selection of Specimens", "اختيار العيّنات"),
 T(["Type of Infection", "Specimen Required", "Notes", "الترجمة"],
   [["Respiratory infection", "Sputum, throat swab, nasopharyngeal swab", "Avoid saliva; collect early morning sputum",
     "**الإصابة التنفسية:** قشع، مسحة حلق، مسحة بلعومية أنفية — تجنّب اللعاب؛ واجمع قشع الصباح الباكر"],
    ["Urinary tract infection", "Midstream urine (MSU(", "Use sterile container, midstream portion",
     "**إصابة المجاري البولية:** إدرار منتصف الدفق (`MSU`) — استعمل وعاءً معقّمًا والجزء الأوسط من الدفق"],
    ["Wound infection", "Swab, pus aspirate, tissue biopsy", "Aspirate preferred over swab",
     "**إصابة الجروح:** مسحة، رشافة القيح، خزعة نسيجية — الرشافة أفضل من المسحة"],
    ["Bloodstream infection", "Blood culture", "Collect before antibiotics",
     "**إصابة مجرى الدم:** زرع الدم — اجمع قبل المضادات الحيوية"],
    ["CSF infection", "Cerebrospinal fluid", "Urgent transport to lab",
     "**إصابة السائل الدماغي الشوكي:** السائل الدماغي الشوكي — نقل عاجل إلى المختبر"]],
   ar_cols=[3], key_cols=[0], widths=["30mm", "36mm", "34mm", ""]),

 SEC("Transport Media Examples", "أمثلة على أوساط النقل"),
 T(["Medium", "Use", "الترجمة"],
   [["Stuart’s medium", "Swabs (throat, wound, genital(", "**وسط ستيوارت:** المسحات (الحلق، الجروح، التناسلية)"],
    ["Amies medium", "Swabs (with or without charcoal(", "**وسط إيميز:** المسحات (مع الفحم أو بدونه)"],
    ["Cary-Blair medium", "Stool specimens", "**وسط كاري-بلير:** عيّنات البراز"],
    ["Viral transport medium (VTM(", "Viral samples (nasal, throat swabs(", "**وسط النقل الفيروسي** (`VTM`): العيّنات الفيروسية (مسحات الأنف والحلق)"]],
   ar_cols=[2], key_cols=[0], widths=["44mm", "52mm", ""]),
 F("collection-infographic.jpg", "Image 05: specimen collection infographic (Arabic in the source)",
   "الصورة 05: لوحة جمع العيّنات (مكتوبة بالعربي في المصدر)", h="150mm", fit="contain"),
]

mcq = [
 {"topic_en": "Introduction and request form", "topic_ar": "المقدّمة واستمارة الطلب"},
 Q("For pathogens to be isolated successfully, which must be correct?", "لعزل المُمرِضات بنجاح، أيّ ممّا يأتي يجب أن يكون صحيحًا؟",
   [("The type, collection, time of specimen and method of its dispatch", "نوع العيّنة وجمعها ووقتها وطريقة إرسالها"),
    ("The colour of the container only", "لون الوعاء فقط"), ("The patient's age only", "عمر المريض فقط"), ("The lab temperature only", "حرارة المختبر فقط")], "a"),
 Q("Which of the following should be included in the request form?", "أيّ ممّا يأتي يجب أن تتضمّنه استمارة الطلب؟",
   [("The lab technician's salary", "راتب فنّي المختبر"), ("Treatment history and antimicrobial therapy", "تاريخ العلاج والعلاج بمضادات الميكروبات"),
    ("The colour of the swab", "لون المسحة"), ("The brand of the container", "علامة الوعاء التجارية")], "b"),
 Q("Supporting clinical information in the request form includes:", "تشمل المعلومات السريرية الداعمة في استمارة الطلب:",
   [("Patient's hobbies", "هوايات المريض"), ("Laboratory name only", "اسم المختبر فقط"),
    ("Travel history and contact with infected individuals", "تاريخ السفر والتماس مع المصابين"), ("Price of the test", "سعر الفحص")], "c"),

 {"topic_en": "Transport of specimens", "topic_ar": "نقل العيّنات"},
 Q("If the specimen cannot reach the laboratory as soon as possible, use:", "إذا لم تصل العيّنة إلى المختبر بسرعة، فاستعمل:",
   [("Hot water", "ماءً حارًّا"), ("Direct sunlight", "أشعة الشمس المباشرة"), ("Antibiotics", "المضادات الحيوية"), ("A suitable preservative or transport medium", "مادة حافظة أو وسط نقل مناسب")], "d"),
 Q("Refrigeration of the sample is done at:", "يُبرَّد النموذج بدرجة:",
   [("4 ºC", "4 °م"), ("37 ºC", "37 °م"), ("-20 ºC", "سالب 20 °م"), ("25 ºC", "25 °م")], "a"),
 Q("Refrigeration helps to preserve cells and reduce the multiplication of:", "يساعد التبريد على حفظ الخلايا وتقليل تكاثر:",
   [("Viruses only", "الفيروسات فقط"), ("Commensals in unpreserved specimens", "الكائنات المتعايشة في العيّنات غير المحفوظة"),
    ("Red blood cells", "كريات الدم الحمراء"), ("Antibodies", "الأجسام المضادة")], "b"),
 Q("Freezing is done at -70 ºC or below in the presence of:", "يُجرى التجميد بدرجة سالب 70 °م أو أقل بوجود:",
   [("Formalin", "الفورمالين"), ("Alcohol", "الكحول"), ("A stabilizing fluid like glycerol or serum", "سائل مثبّت مثل الغليسيرول أو المصل"), ("Charcoal", "الفحم")], "c"),
 Q("The container cap is sealed with adhesive tape to prevent:", "يُغلق غطاء الوعاء بشريط لاصق لمنع:",
   [("Freezing", "التجمّد"), ("Labeling", "التعليم"), ("Refrigeration", "التبريد"), ("Loosening and leakage during transit", "الارتخاء والتسرّب أثناء النقل")], "d"),
 Q("Specimens that may contain highly infectious organism are marked:", "تُعلَّم العيّنات التي قد تحتوي على كائنات شديدة العدوى بعبارة:",
   [("HIGH RISK", "خطر عالٍ"), ("FRAGILE", "قابل للكسر"), ("URGENT ONLY", "عاجل فقط"), ("STERILE", "معقّم")], "a"),
 Q("If the specimen is fluid, use:", "إذا كانت العيّنة سائلة، فاستعمل:",
   [("Glass bottle only", "قنينة زجاجية فقط"), ("Sufficient absorbent material", "مادة ماصّة كافية"), ("No packaging", "بلا تغليف"), ("Charcoal", "الفحم")], "b"),

 {"topic_en": "Non-culture techniques", "topic_ar": "التقنيات غير الزرعية"},
 Q("Non-culture techniques are important when:", "تكون التقنيات غير الزرعية مهمّة عندما:",
   [("The microorganism grows very fast", "ينمو الكائن المجهري بسرعة كبيرة"), ("No diagnosis is needed", "لا حاجة إلى التشخيص"),
    ("The microorganism is slow-growing", "يكون الكائن المجهري بطيء النمو"), ("The specimen is frozen", "تكون العيّنة مجمّدة")], "c"),
 Q("Which of the following is a non-culture technique?", "أيّ ممّا يأتي تقنية غير زرعية؟",
   [("Blood culture", "زرع الدم"), ("Cary-Blair medium", "وسط كاري-بلير"), ("Stuart's medium", "وسط ستيوارت"), ("Nucleic acid amplification techniques (NAAT)", "تقنيات تضخيم الحمض النووي")], "d"),
 Q("Non-culture techniques are used to provide:", "تُستعمل التقنيات غير الزرعية لتوفير:",
   [("Rapid clinical information", "معلومات سريرية سريعة"), ("Transport media", "أوساط نقل"), ("Sterile containers", "أوعية معقّمة"), ("Antibiotics", "مضادات حيوية")], "a"),

 {"topic_en": "Principles and techniques of collection", "topic_ar": "مبادئ الجمع وتقنياته"},
 Q("According to the principles of specimen collection, specimens should be collected:", "حسب مبادئ جمع العيّنات، يجب جمع العيّنات:",
   [("After antibiotics", "بعد المضادات الحيوية"), ("Before antibiotics", "قبل المضادات الحيوية"), ("Only at night", "ليلًا فقط"), ("After 24 hours of symptoms only", "بعد 24 ساعة من الأعراض فقط")], "b"),
 Q("Urine is collected as:", "يُجمع الإدرار على شكل:",
   [("First drops only", "القطرات الأولى فقط"), ("24-hour sample only", "عيّنة 24 ساعة فقط"), ("Midstream clean-catch", "عيّنة منتصف الإدرار النظيفة"), ("From the toilet", "من المرحاض")], "c"),
 Q("Sputum is collected as:", "يُجمع القشع على شكل:",
   [("Saliva", "لعاب"), ("Throat swab only", "مسحة حلق فقط"), ("Nasal wash", "غسول أنفي"), ("Deep cough specimen", "عيّنة من سعال عميق")], "d"),
 Q("CSF is collected by:", "يُجمع السائل الدماغي الشوكي بواسطة:",
   [("Lumbar puncture", "البزل القطني"), ("Venipuncture", "بزل الوريد"), ("Swab", "مسحة"), ("Midstream collection", "جمع منتصف الدفق")], "a"),
 Q("When collecting swabs you should:", "عند جمع المسحات يجب:",
   [("Use non-sterile cotton", "استعمال قطن غير معقّم"), ("Use sterile cotton and avoid normal flora", "استعمال قطن معقّم وتجنّب النبيت الطبيعي"),
    ("Touch the normal flora", "لمس النبيت الطبيعي"), ("Add urine", "إضافة الإدرار")], "b"),
 Q("When collecting stool you should:", "عند جمع البراز يجب:",
   [("Collect a large amount with urine", "جمع كمية كبيرة مع الإدرار"), ("Add disinfectant", "إضافة مطهّر"), ("Collect a small amount and avoid urine", "جمع كمية صغيرة وتجنّب الإدرار"), ("Freeze immediately at 4 ºC", "التجميد فورًا بدرجة 4 °م")], "c"),
 Q("Which of the following is a common error to avoid?", "أيّ ممّا يأتي خطأ شائع يجب تجنّبه؟",
   [("Using sterile containers", "استعمال أوعية معقّمة"), ("Proper labeling", "التعليم الصحيح"), ("Immediate transport", "النقل الفوري"), ("Collecting after antibiotics", "الجمع بعد المضادات الحيوية")], "d"),

 {"topic_en": "Selection of specimens and transport media", "topic_ar": "اختيار العيّنات وأوساط النقل"},
 Q("For respiratory infection you should:", "في الإصابة التنفسية يجب:",
   [("Avoid saliva; collect early morning sputum", "تجنّب اللعاب وجمع قشع الصباح الباكر"), ("Collect saliva only", "جمع اللعاب فقط"),
    ("Collect blood culture only", "جمع زرع الدم فقط"), ("Collect evening sputum mixed with saliva", "جمع قشع المساء مع اللعاب")], "a"),
 Q("The specimen required for urinary tract infection is:", "العيّنة المطلوبة لإصابة المجاري البولية هي:",
   [("Sputum", "القشع"), ("Midstream urine (MSU)", "إدرار منتصف الدفق"), ("Blood culture", "زرع الدم"), ("Throat swab", "مسحة الحلق")], "b"),
 Q("In wound infection, which is preferred?", "في إصابة الجروح، أيّهما المفضّل؟",
   [("Swab over aspirate", "المسحة على الرشافة"), ("Saliva", "اللعاب"), ("Aspirate over swab", "الرشافة على المسحة"), ("Urine", "الإدرار")], "c"),
 Q("For CSF infection, the note is:", "الملاحظة الخاصة بإصابة السائل الدماغي الشوكي هي:",
   [("Collect after antibiotics", "الجمع بعد المضادات الحيوية"), ("Refrigerate for 2 days", "التبريد يومين"), ("Avoid saliva", "تجنّب اللعاب"), ("Urgent transport to lab", "النقل العاجل إلى المختبر")], "d"),
 Q("The transport medium used for stool specimens is:", "وسط النقل المستعمل لعيّنات البراز هو:",
   [("Cary-Blair medium", "وسط كاري-بلير"), ("Stuart’s medium", "وسط ستيوارت"), ("Amies medium", "وسط إيميز"), ("VTM", "وسط النقل الفيروسي")], "a"),
 Q("The transport medium that may be used with or without charcoal is:", "وسط النقل الذي قد يُستعمل مع الفحم أو بدونه هو:",
   [("Cary-Blair medium", "وسط كاري-بلير"), ("Amies medium", "وسط إيميز"), ("VTM", "وسط النقل الفيروسي"), ("Stuart’s medium", "وسط ستيوارت")], "b"),
 Q("Viral transport medium (VTM) is used for:", "يُستعمل وسط النقل الفيروسي لـ:",
   [("Stool specimens", "عيّنات البراز"), ("Blood culture", "زرع الدم"), ("Viral samples (nasal, throat swabs)", "العيّنات الفيروسية (مسحات الأنف والحلق)"), ("Tissue biopsy", "الخزعة النسيجية")], "c"),

 {"topic_en": "Picture questions", "topic_ar": "أسئلة الصور"},
 Q("The item in this image is:", "الأداة في هذه الصورة هي:",
   [("Sputum container", "وعاء القشع"), ("Blood culture bottle", "قنينة زرع الدم"), ("Stool container", "وعاء البراز"), ("Swab with transport media", "مسحة مع وسط النقل")], "d",
   img="assets/swab-transport.jpg", img_h="32mm"),
 Q("The specimen in this container should be collected as:", "العيّنة في هذا الوعاء يجب أن تُجمع على شكل:",
   [("Deep cough specimen", "عيّنة من سعال عميق"), ("Midstream clean-catch", "منتصف الإدرار النظيفة"), ("Lumbar puncture", "بزل قطني"), ("Small amount, avoid urine", "كمية صغيرة مع تجنّب الإدرار")], "a",
   img="assets/sputum-container.jpg", img_h="32mm"),
 Q("These items are used for collecting:", "تُستعمل هذه الأدوات لجمع:",
   [("CSF", "السائل الدماغي الشوكي"), ("Swabs (sterile cotton)", "المسحات (قطن معقّم)"), ("Blood", "الدم"), ("Stool", "البراز")], "b",
   img="assets/swabs.jpg", img_h="32mm"),
]

tf = [
 TF("The time of the specimen affects successful isolation of pathogens.", "يؤثّر وقت العيّنة في نجاح عزل المُمرِضات.", "T"),
 TF("The request form does not need the time of collection.", "استمارة الطلب لا تحتاج إلى وقت الجمع.", "F"),
 TF("Refrigeration at 4 ºC reduces the multiplication of commensals in unpreserved specimens.", "التبريد بدرجة 4 °م يقلّل تكاثر الكائنات المتعايشة في العيّنات غير المحفوظة.", "T"),
 TF("Freezing of specimens is done at 4 ºC.", "يُجرى تجميد العيّنات بدرجة 4 °م.", "F"),
 TF("The specimen container should be free from cracks and the cap leak proof.", "يجب أن يكون وعاء العيّنة خاليًا من الشقوق وغطاؤه محكمًا.", "T"),
 TF("Non-culture techniques are used when microorganisms grow rapidly in vitro.", "تُستعمل التقنيات غير الزرعية عندما تنمو الكائنات بسرعة خارج الجسم.", "F"),
 TF("Serology is a non-culture technique.", "الفحوص المصلية من التقنيات غير الزرعية.", "T"),
 TF("Specimens should be collected after antibiotics.", "يجب جمع العيّنات بعد المضادات الحيوية.", "F"),
 TF("Blood should be collected aseptically.", "يجب جمع الدم بطريقة معقّمة.", "T"),
 TF("Saliva is the preferred specimen in respiratory infection.", "اللعاب هو العيّنة المفضّلة في الإصابة التنفسية.", "F"),
 TF("Blood culture should be collected before antibiotics.", "يجب جمع زرع الدم قبل المضادات الحيوية.", "T"),
 TF("Cary-Blair medium is used for throat swabs.", "يُستعمل وسط كاري-بلير لمسحات الحلق.", "F"),
]

traps = [
 TR("Refrigeration vs freezing temperatures.", "درجة التبريد مقابل درجة التجميد.",
    "Refrigeration: 4 ºC. Freezing: -70 ºC or below in the presence of a stabilizing fluid (glycerol or serum).",
    "التبريد: 4 °م. التجميد: سالب 70 °م أو أقل بوجود سائل مثبّت (غليسيرول أو مصل)."),
 TR("Wound infection — swab or aspirate?", "إصابة الجروح — مسحة أم رشافة؟",
    "Aspirate preferred over swab.", "الرشافة أفضل من المسحة."),
 TR("Respiratory specimen — sputum or saliva?", "العيّنة التنفسية — قشع أم لعاب؟",
    "Sputum (deep cough, early morning); avoid saliva.", "القشع (سعال عميق، الصباح الباكر)؛ وتجنّب اللعاب."),
 TR("Stuart’s vs Cary-Blair medium.", "وسط ستيوارت مقابل وسط كاري-بلير.",
    "Stuart’s: swabs (throat, wound, genital). Cary-Blair: stool specimens.",
    "ستيوارت: المسحات (الحلق، الجروح، التناسلية). كاري-بلير: عيّنات البراز."),
 TR("Glass container vs fluid specimen packaging.", "تغليف الوعاء الزجاجي مقابل العيّنة السائلة.",
    "Glass tube or bottle: sufficient packaging material. Fluid specimen: sufficient absorbent material.",
    "الأنبوب أو القنينة الزجاجية: مواد تغليف كافية. العيّنة السائلة: مادة ماصّة كافية."),
 TR("Urine vs stool collection — the word “urine” appears in both.", "جمع الإدرار مقابل البراز — كلمة «الإدرار» تظهر في الاثنين.",
    "Urine: midstream clean-catch. Stool: small amount, avoid urine.",
    "الإدرار: عيّنة منتصف الإدرار النظيفة. البراز: كمية صغيرة مع تجنّب الإدرار."),
]

important = [
 IM("What must be correct for pathogens to be isolated successfully?", "ما الذي يجب أن يكون صحيحًا لعزل المُمرِضات بنجاح؟",
    "1- The type of specimen, 2- collection of specimen, 3- time of specimen, 4- method of its dispatch to the laboratory.",
    "1- نوع العيّنة، 2- جمعها، 3- وقتها، 4- طريقة إرسالها إلى المختبر."),
 IM("List the information that the request form should include.", "عدّد المعلومات التي يجب أن تتضمّنها استمارة الطلب.",
    "Patient details; clinical diagnosis; onset of symptoms; sample type; time of collection; treatment history and antimicrobial therapy; other health and safety issues; supporting clinical information.",
    "معلومات المريض؛ التشخيص السريري؛ بداية الأعراض؛ نوع العيّنة؛ وقت الجمع؛ تاريخ العلاج ومضادات الميكروبات؛ قضايا صحية وأمنية أخرى؛ معلومات سريرية داعمة."),
 IM("Mention the rules of transport of microbiological specimens.", "اذكر قواعد نقل العيّنات الميكروبيولوجية.",
    "Reach the lab as soon as possible or use a preservative/transport medium; refrigerate at 4 ºC; freeze at -70 ºC with a stabilizing fluid; container free from cracks with leak-proof cap; seal the cap with adhesive tape; packaging material for glass; absorbent material for fluid; mark highly infectious specimens “HIGH RISK”.",
    "الوصول بسرعة أو استعمال حافظ/وسط نقل؛ التبريد بدرجة 4 °م؛ التجميد بدرجة سالب 70 °م مع سائل مثبّت؛ وعاء بلا شقوق وغطاء محكم؛ إغلاق الغطاء بشريط لاصق؛ تغليف كافٍ للزجاج؛ مادة ماصّة للسوائل؛ وتعليم العيّنات شديدة العدوى «خطر عالٍ»."),
 IM("When are non-culture techniques important? Give examples.", "متى تكون التقنيات غير الزرعية مهمّة؟ اذكر أمثلة.",
    "When the microorganism cannot be readily cultured in vitro, is slow-growing, or rapid diagnosis significantly influences management. Examples: direct microscopy, immunological methods, serology, NAAT.",
    "عندما لا يمكن زرع الكائن بسهولة، أو يكون بطيء النمو، أو يؤثّر التشخيص السريع كثيرًا في الإدارة. أمثلة: الفحص المجهري المباشر، الطرائق المناعية، الفحوص المصلية، تضخيم الحمض النووي."),
 IM("Mention the principles of specimen collection.", "اذكر مبادئ جمع العيّنات.",
    "Collect from correct site; before antibiotics; aseptic technique; sufficient quantity; label properly; sterile containers; transport immediately.",
    "الجمع من الموقع الصحيح؛ قبل المضادات الحيوية؛ بتقنية معقّمة؛ كمية كافية؛ تعليم صحيح؛ أوعية معقّمة؛ نقل فوري."),
 IM("Mention the common errors to avoid in specimen collection.", "اذكر الأخطاء الشائعة الواجب تجنّبها في جمع العيّنات.",
    "Collecting after antibiotics; contaminated containers; delayed transport; missing labels; insufficient specimen.",
    "الجمع بعد المضادات الحيوية؛ أوعية ملوّثة؛ تأخّر النقل؛ غياب العلامات؛ عيّنة غير كافية."),
 IM("Give examples of transport media and their uses.", "اذكر أمثلة على أوساط النقل واستعمالاتها.",
    "Stuart’s: swabs (throat, wound, genital); Amies: swabs (with or without charcoal); Cary-Blair: stool specimens; VTM: viral samples (nasal, throat swabs).",
    "ستيوارت: المسحات (الحلق، الجروح، التناسلية)؛ إيميز: المسحات (مع الفحم أو بدونه)؛ كاري-بلير: عيّنات البراز؛ الوسط الفيروسي: العيّنات الفيروسية (مسحات الأنف والحلق)."),
]

meta = dict(subject_en="Diagnostic Microbiology", subject_ar="الأحياء المجهرية التشخيصية", short_ar="بكتريا",
            unit_en="Lab 2", unit_ar="العملي 2", unit_label="LAB", unit_no="2",
            title_en="Selection, Collection, and Transport of Specimens", title_ar="اختيار العيّنات وجمعها ونقلها",
            kind="Laboratories — عملي", stage="The fourth stage — الرابعة", instructor="د. هبة سامي",
            file_name="بكتريا عملي المحاضرة الثانية", questions_suffix=" اسئلة")   # user-chosen file names

folder = "microbiology-lab2-specimens"
qs = [q for q in mcq if "answer" in q]
print(folder, len(qs), dict(Counter(q["answer"] for q in qs)), len(tf),
      dict(Counter(t["answer"] for t in tf)), len(traps), len(important))
d = os.path.dirname(os.path.abspath(__file__))
json.dump({"meta": meta, "blocks": blocks,
           "questions": {"mcq": mcq, "tf": tf, "traps": traps, "important": important}},
          open(os.path.join(d, "lecture.json"), "w"), ensure_ascii=False, indent=1)
