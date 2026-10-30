---
source: BIOS-Obsidian/tools/scripts/bac/lab2.py
handouts: [bacteriology-lab2-specimens]
saved: 2026-10-30
tags: [bios, code]
---
# bac/lab2.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#bacteriology-lab2-specimens|bacteriology-lab2-specimens]]

```python
import sys; sys.path.insert(0, "/tmp/claude-0/-home-user--/8f878068-bae9-502b-96f7-788f221c7cb0/scratchpad/n7")
sys.path.insert(0, "/tmp/claude-0/-home-user--/8f878068-bae9-502b-96f7-788f221c7cb0/scratchpad/bac")
from c import *

BAC = dict(subject_en="Diagnostic Microbiology", subject_ar="الأحياء المجهرية التشخيصية", short_ar="بكتريا", unit_label="LAB", department="قسم التحليلات",
           kind="Laboratories — عملي", stage="The fourth stage — الرابعة", instructor="د. هبة سامي")

blocks = [
 SEC("Introduction", "مقدّمة"),
 H2("Selection, collection, and transportation of specimens for microbiological examination",
    "اختيار العيّنات وجمعها ونقلها للفحص الميكروبيولوجي"),
 C("The role of the laboratory in the diagnosis of infections can be considered a major steps of diagnostic microbiology.",
   "يمكن عدّ دور المختبر في تشخيص العدوى من الخطوات الرئيسة في الأحياء المجهرية التشخيصية."),
 L(["**the type of specimen**", "**collection of specimen**", "**time of specimen**", "**method of its dispatch to the laboratory must be correct.**"],
   ["**نوع العيّنة**", "**جمع العيّنة**", "**وقت أخذ العيّنة**", "**طريقة إرسالها إلى المختبر يجب أن تكون صحيحة.**"],
   en="If pathogens are to be isolated successfully", ar="إذا أُريد عزل الممرضات بنجاح فإن:"),

 L(["Patient details.", "Clinical diagnosis.", "Onset of symptoms", "Sample type."],
   ["تفاصيل المريض.", "التشخيص السريري.", "بداية ظهور الأعراض", "نوع العيّنة."],
   en="**A detailed** request form that accompanies a clinical sample is pivotal in ensuring the appropriate diagnostic procedures are undertaken; information should include:",
   ar="استمارة الطلب **المفصّلة** المرافقة للعيّنة السريرية أساسية لضمان إجراء الفحوص التشخيصية المناسبة؛ ويجب أن تتضمّن المعلومات:"),
 FF(("swab-transport.png", "Swab with transport media", "مسحة مع وسط نقل", "30mm"),
    ("swabs.png", "Sterile swabs", "مسحات معقّمة", "30mm")),
 L(["Time of collection.", "Treatment history and antimicrobial therapy.", "Other health and safety issues.",
    "Supporting clinical information, including travel history and contact with infected individuals, is also important."],
   ["وقت الجمع.", "تاريخ العلاج والعلاج بمضادات الميكروبات.", "أمور الصحة والسلامة الأخرى.",
    "المعلومات السريرية الداعمة، ومنها تاريخ السفر والاختلاط بأشخاص مصابين، مهمة أيضًا."]),
 FF(("urine-container.png", "Specimen container", "حاوية عيّنة", "30mm"),
    ("sputum-container.png", "Sputum C/S container", "حاوية عيّنة القشع (زرع وحساسية)", "30mm")),
 F("collection-infographic.jpg", "Specimen Collection", "جمع العيّنات", h="125mm", fit="contain"),

 SEC("Transport of microbiological specimens", "نقل العيّنات الميكروبيولوجية"),
 C("**Specimen should reach to the laboratory as soon as possible** or a suitable preservative or transport medium must be used.",
   "**يجب أن تصل العيّنة إلى المختبر بأسرع وقت ممكن** وإلا وجب استخدام مادة حافظة أو وسط نقل مناسب."),
 C("**Refrigeration of sample at 4 ºC** can help to preserve cells and reduce the multiplication of commensals in unpreserved specimens.",
   "**تبريد العيّنة بدرجة 4 مْ** يساعد على حفظ الخلايا وتقليل تكاثر الكائنات المتعايشة في العيّنات غير المحفوظة."),
 C("**Freezing at -70 ºC or below** In the presence of a stabilizing fluid, like glycerol or serum.",
   "**التجميد بدرجة 70- مْ أو أقل** بوجود سائل مثبّت مثل الكليسيرول أو المصل."),
 C("**Ensure that the specimen container is free from cracks**, and the cap is leak proof.",
   "**تأكّد من خلوّ حاوية العيّنة من الشقوق**، وأن الغطاء لا يسرّب."),
 C("**Seal round the container cap with adhesive tape** to prevent loosening and leakage during transit.",
   "**أحكِم الغلق حول غطاء الحاوية بشريط لاصق** لمنع ارتخائه والتسرّب أثناء النقل."),
 C("**If the container is glass tube or bottle, use sufficient packaging material** to prefect a specimen.",
   "**إذا كانت الحاوية أنبوبًا أو قنينة زجاجية فاستخدم مواد تغليف كافية** لحماية العيّنة."),
 C("**If the specimen is fluid,** use sufficient absorbent material to absorb it.",
   "**إذا كانت العيّنة سائلة،** فاستخدم مادة ماصّة كافية لامتصاصها."),
 C("Mark all specimen that may contain **highly infectious organism “HIGH RISK”**.",
   "ضع علامة **«خطورة عالية» (`HIGH RISK`)** على كل عيّنة قد تحتوي **كائنًا شديد العدوى**."),

 SEC("Non-culture techniques", "التقنيات غير الزرعية"),
 C("Following receipt of the sample, the microbiology laboratory may utilize **non- culture techniques** to provide rapid clinical information, which may benefit patient management.",
   "بعد استلام العيّنة قد يستخدم مختبر الأحياء المجهرية **تقنيات غير زرعية** لتقديم معلومات سريرية سريعة قد تفيد في تدبير حالة المريض."),
 L(["Microorganism cannot be readily cultured in vitro;", "Microorganism is slow-growing;",
    "Rapid laboratory diagnosis significantly influences clinical management of the patient."],
   ["لا يمكن زرع الكائن المجهري بسهولة خارج الجسم (في المختبر)؛", "الكائن المجهري بطيء النمو؛",
    "التشخيص المختبري السريع يؤثّر كثيرًا في التدبير السريري للمريض."],
   en="There are several situations where non-culture techniques are of importance:",
   ar="هناك عدة حالات تكون فيها التقنيات غير الزرعية مهمة:"),
 L(["direct microscopy", "immunological methods", "serology", "nucleic acid amplification techniques (NAAT)."],
   ["الفحص المجهري المباشر", "الطرائق المناعية", "الفحوص المصلية", "تقنيات تضخيم الأحماض النووية (`NAAT`)."],
   en="**Non-culture techniques include:**", ar="**تشمل التقنيات غير الزرعية:**"),

 SEC("Principles of Specimen Collection", "مبادئ جمع العيّنات"),
 L(["Collect from correct site.", "Collect before antibiotics.", "Use aseptic technique.", "Collect sufficient quantity.",
    "Label properly.", "Use sterile containers.", "Transport immediately."],
   ["اجمعها من الموقع الصحيح.", "اجمعها قبل المضادات الحيوية.", "استخدم التقنية المعقّمة.", "اجمع كمية كافية.",
    "ضع الملصق بصورة صحيحة.", "استخدم حاويات معقّمة.", "انقلها فورًا."]),

 SEC("Collection Techniques", "تقنيات الجمع"),
 T(["Specimen", "Collection", "الترجمة"],
   [["Blood", "aseptic collection.", "**الدم**: جمع معقّم."],
    ["Urine", "midstream clean-catch.", "**الإدرار**: عيّنة منتصف الإدرار النظيفة."],
    ["Sputum", "deep cough specimen.", "**القشع**: عيّنة سعال عميق."],
    ["Swabs", "sterile cotton, avoid normal flora.", "**المسحات**: قطن معقّم، وتجنّب الفلورا الطبيعية."],
    ["Stool", "small amount, avoid urine.", "**البراز**: كمية قليلة، وتجنّب خلطه بالإدرار."],
    ["CSF", "lumbar puncture.", "**السائل الدماغي الشوكي**: البزل القطني."]],
   ar_cols=[2], key_cols=[0]),

 SEC("Common Errors to Avoid", "أخطاء شائعة يجب تجنّبها"),
 L(["✗ Collecting after antibiotics", "✗ Contaminated containers", "✗ Delayed transport", "✗ Missing labels", "✗ Insufficient specimen"],
   ["✗ الجمع بعد المضادات الحيوية", "✗ حاويات ملوّثة", "✗ تأخّر النقل", "✗ غياب الملصقات", "✗ عيّنة غير كافية"]),

 SEC("Selection of Specimens", "اختيار العيّنات"),
 T(["Type of Infection", "Specimen Required", "Notes", "الترجمة"],
   [["Respiratory infection", "Sputum, throat swab, nasopharyngeal swab", "Avoid saliva; collect early morning sputum",
     "**عدوى الجهاز التنفسي**: قشع، مسحة بلعوم، مسحة أنفية بلعومية — تجنّب اللعاب؛ واجمع قشع الصباح الباكر"],
    ["Urinary tract infection", "Midstream urine (MSU)", "Use sterile container, midstream portion",
     "**عدوى المسالك البولية**: عيّنة منتصف الإدرار — استخدم حاوية معقّمة والجزء الأوسط من الإدرار"],
    ["Wound infection", "Swab, pus aspirate, tissue biopsy", "Aspirate preferred over swab",
     "**عدوى الجروح**: مسحة، رشافة قيح، خزعة نسيجية — الرشافة مفضّلة على المسحة"],
    ["Bloodstream infection", "Blood culture", "Collect before antibiotics",
     "**عدوى مجرى الدم**: زرع الدم — اجمعها قبل المضادات الحيوية"],
    ["CSF infection", "Cerebrospinal fluid", "Urgent transport to lab",
     "**عدوى السائل الدماغي الشوكي**: السائل الدماغي الشوكي — نقل عاجل إلى المختبر"]],
   ar_cols=[3], key_cols=[0], widths=[18, 22, 22, 38]),

 SEC("Transport Media Examples", "أمثلة على أوساط النقل"),
 T(["Medium", "Use", "الترجمة"],
   [["Stuart’s medium", "Swabs (throat, wound, genital)", "**وسط ستيوارت**: المسحات (البلعوم، الجروح، التناسلية)"],
    ["Amies medium", "Swabs (with or without charcoal)", "**وسط آميز**: المسحات (مع الفحم أو بدونه)"],
    ["Cary-Blair medium", "Stool specimens", "**وسط كاري-بلير**: عيّنات البراز"],
    ["Viral transport medium (VTM)", "Viral samples (nasal, throat swabs)", "**وسط النقل الفيروسي**: العيّنات الفيروسية (مسحات الأنف والبلعوم)"]],
   ar_cols=[2], key_cols=[0]),
]

P = lambda *o: [(x, y) for x, y in o]
mcq = [
 {"topic_en": "Specimen selection and the request form", "topic_ar": "اختيار العيّنة واستمارة الطلب"},
 Q("For pathogens to be isolated successfully, all of the following must be correct EXCEPT:", "لعزل الممرضات بنجاح يجب أن يكون كل ما يأتي صحيحًا عدا:",
   P(("The type of specimen", "نوع العيّنة"), ("Collection of specimen", "جمع العيّنة"), ("Time of specimen", "وقت العيّنة"), ("The colour of the container", "لون الحاوية"), ("Method of its dispatch to the laboratory", "طريقة إرسالها إلى المختبر")), "d"),
 Q("Which of the following is NOT listed as information in the request form:", "أي مما يأتي لم يُذكر ضمن معلومات استمارة الطلب:",
   P(("Clinical diagnosis", "التشخيص السريري"), ("Onset of symptoms", "بداية الأعراض"), ("Patient's blood group", "فصيلة دم المريض"), ("Treatment history and antimicrobial therapy", "تاريخ العلاج والعلاج بالمضادات"), ("Travel history", "تاريخ السفر")), "c"),
 Q("A detailed request form is pivotal because it ensures:", "استمارة الطلب المفصّلة أساسية لأنها تضمن:",
   P(("Lower cost of the test", "كلفة أقل للفحص"), ("The appropriate diagnostic procedures are undertaken", "إجراء الفحوص التشخيصية المناسبة"), ("Faster transport", "نقلًا أسرع"), ("Sterility of the container", "تعقيم الحاوية")), "b"),

 {"topic_en": "Transport of specimens", "topic_ar": "نقل العيّنات"},
 Q("If the specimen cannot reach the laboratory as soon as possible:", "إذا لم تصل العيّنة إلى المختبر بأسرع وقت:",
   P(("It is discarded", "تُتلف"), ("A suitable preservative or transport medium must be used", "يجب استخدام مادة حافظة أو وسط نقل مناسب"), ("It is heated to 37 ºC", "تُسخّن إلى 37 مْ"), ("It is diluted with water", "تُخفّف بالماء")), "b"),
 Q("Refrigeration of an unpreserved sample is done at:", "يُبرَّد النموذج غير المحفوظ بدرجة:",
   P(("37 ºC", "37 مْ"), ("25 ºC", "25 مْ"), ("4 ºC", "4 مْ"), ("-20 ºC", "20- مْ"), ("-70 ºC", "70- مْ")), "c"),
 Q("Refrigeration at 4 ºC helps to:", "يساعد التبريد بدرجة 4 مْ على:",
   P(("Kill all pathogens", "قتل جميع الممرضات"), ("Preserve cells and reduce multiplication of commensals", "حفظ الخلايا وتقليل تكاثر المتعايشات"), ("Increase growth of pathogens", "زيادة نمو الممرضات"), ("Lyse red blood cells", "تحليل كريات الدم الحمر")), "b"),
 Q("Freezing of specimens is done at -70 ºC or below in the presence of:", "يُجرى تجميد العيّنات بدرجة 70- مْ أو أقل بوجود:",
   P(("Formalin", "الفورمالين"), ("Glycerol or serum", "الكليسيرول أو المصل"), ("Ethanol", "الإيثانول"), ("Charcoal", "الفحم"), ("Saline only", "المحلول الملحي فقط")), "b"),
 Q("The container cap is sealed with adhesive tape to:", "يُغلق غطاء الحاوية بشريط لاصق لـ:",
   P(("Label the specimen", "تعليم العيّنة"), ("Prevent loosening and leakage during transit", "منع الارتخاء والتسرّب أثناء النقل"), ("Keep it cold", "إبقائها باردة"), ("Absorb fluids", "امتصاص السوائل")), "b"),
 Q("A specimen that may contain a highly infectious organism is marked:", "تُعلَّم العيّنة التي قد تحتوي كائنًا شديد العدوى بعبارة:",
   P(("URGENT", "عاجل"), ("STERILE", "معقّم"), ("HIGH RISK", "خطورة عالية"), ("FRAGILE", "قابل للكسر")), "c"),

 {"topic_en": "Non-culture techniques", "topic_ar": "التقنيات غير الزرعية"},
 Q("Non-culture techniques are important in all of the following situations EXCEPT:", "تكون التقنيات غير الزرعية مهمة في كل الحالات الآتية عدا:",
   P(("Microorganism cannot be readily cultured in vitro", "لا يمكن زرع الكائن بسهولة في المختبر"), ("Microorganism is slow-growing", "الكائن بطيء النمو"), ("Microorganism grows rapidly on simple media", "الكائن ينمو سريعًا على الأوساط البسيطة"), ("Rapid diagnosis influences clinical management", "التشخيص السريع يؤثّر في التدبير السريري")), "c"),
 Q("Which of the following is NOT a non-culture technique:", "أي مما يأتي ليس تقنية غير زرعية:",
   P(("Direct microscopy", "الفحص المجهري المباشر"), ("Serology", "الفحوص المصلية"), ("NAAT", "تقنيات تضخيم الأحماض النووية"), ("Culture on blood agar", "الزرع على أكار الدم"), ("Immunological methods", "الطرائق المناعية")), "d"),
 Q("NAAT stands for:", "يرمز `NAAT` إلى:",
   P(("Nucleic acid amplification techniques", "تقنيات تضخيم الأحماض النووية"), ("Nutrient agar antibiotic test", "فحص المضادات على الأكار المغذّي"), ("Non-aseptic transport", "النقل غير المعقّم"), ("Normal antibody agglutination test", "فحص تلازن الأضداد الطبيعي")), "a"),

 {"topic_en": "Principles, techniques and errors", "topic_ar": "المبادئ والتقنيات والأخطاء"},
 Q("Specimens for culture should be collected:", "يجب جمع عيّنات الزرع:",
   P(("After the first dose of antibiotics", "بعد أول جرعة من المضاد"), ("Before antibiotics", "قبل المضادات الحيوية"), ("After completing treatment", "بعد إكمال العلاج"), ("At any time", "في أي وقت")), "b"),
 Q("The correct urine specimen for culture is:", "عيّنة الإدرار الصحيحة للزرع هي:",
   P(("First drops of urine", "القطرات الأولى من الإدرار"), ("Midstream clean-catch", "منتصف الإدرار النظيفة"), ("24-hour urine", "إدرار 24 ساعة"), ("Last drops of urine", "القطرات الأخيرة")), "b"),
 Q("Sputum is collected as:", "يُجمع القشع على شكل:",
   P(("Saliva", "لعاب"), ("Deep cough specimen", "عيّنة سعال عميق"), ("Throat wash", "غسول بلعوم"), ("Nasal swab", "مسحة أنفية")), "b"),
 Q("CSF is collected by:", "يُجمع السائل الدماغي الشوكي بـ:",
   P(("Venipuncture", "بزل الوريد"), ("Lumbar puncture", "البزل القطني"), ("Swab", "مسحة"), ("Midstream catch", "عيّنة منتصف التيار")), "b"),
 Q("When collecting stool, you should:", "عند جمع البراز يجب:",
   P(("Collect a large amount mixed with urine", "جمع كمية كبيرة مع الإدرار"), ("Collect a small amount and avoid urine", "جمع كمية قليلة وتجنّب الإدرار"), ("Use a swab only", "استخدام المسحة فقط"), ("Freeze it immediately", "تجميده فورًا")), "b"),
 Q("All of the following are common errors to avoid EXCEPT:", "كل ما يأتي أخطاء شائعة يجب تجنّبها عدا:",
   P(("Collecting after antibiotics", "الجمع بعد المضادات"), ("Delayed transport", "تأخّر النقل"), ("Missing labels", "غياب الملصقات"), ("Using sterile containers", "استخدام حاويات معقّمة"), ("Insufficient specimen", "عيّنة غير كافية")), "d"),

 {"topic_en": "Selection of specimens & transport media", "topic_ar": "اختيار العيّنات وأوساط النقل"},
 Q("In respiratory infection, the note for sputum collection is:", "في عدوى الجهاز التنفسي تكون ملاحظة جمع القشع:",
   P(("Collect at night", "اجمعه ليلًا"), ("Avoid saliva; collect early morning sputum", "تجنّب اللعاب واجمع قشع الصباح الباكر"), ("Mix with saliva", "اخلطه باللعاب"), ("Collect after antibiotics", "اجمعه بعد المضادات")), "b"),
 Q("In wound infection, which is preferred:", "في عدوى الجروح أيهما مفضّل:",
   P(("Swab over aspirate", "المسحة على الرشافة"), ("Aspirate over swab", "الرشافة على المسحة"), ("Blood culture", "زرع الدم"), ("Urine", "الإدرار")), "b"),
 Q("The specimen required for bloodstream infection is:", "العيّنة المطلوبة لعدوى مجرى الدم هي:",
   P(("Sputum", "القشع"), ("Blood culture", "زرع الدم"), ("CSF", "السائل الدماغي الشوكي"), ("Stool", "البراز")), "b"),
 Q("CSF infection specimens require:", "تتطلّب عيّنات عدوى السائل الدماغي الشوكي:",
   P(("Refrigeration for 24 h", "تبريدًا لمدة 24 ساعة"), ("Urgent transport to lab", "نقلًا عاجلًا إلى المختبر"), ("Freezing at -70 ºC", "تجميدًا بدرجة 70- مْ"), ("Cary-Blair medium", "وسط كاري-بلير")), "b"),
 Q("Cary-Blair medium is used for:", "يُستخدم وسط كاري-بلير لـ:",
   P(("Throat swabs", "مسحات البلعوم"), ("Stool specimens", "عيّنات البراز"), ("Viral samples", "العيّنات الفيروسية"), ("Blood culture", "زرع الدم")), "b"),
 Q("Amies medium is used for:", "يُستخدم وسط آميز لـ:",
   P(("Stool specimens", "عيّنات البراز"), ("Swabs (with or without charcoal)", "المسحات (مع الفحم أو بدونه)"), ("CSF", "السائل الدماغي الشوكي"), ("Urine", "الإدرار")), "b"),
 Q("Stuart’s medium is used for:", "يُستخدم وسط ستيوارت لـ:",
   P(("Swabs (throat, wound, genital)", "المسحات (البلعوم، الجروح، التناسلية)"), ("Stool specimens", "عيّنات البراز"), ("Viral samples", "العيّنات الفيروسية"), ("Blood", "الدم")), "a"),
 Q("Nasal and throat swabs for viruses are placed in:", "توضع مسحات الأنف والبلعوم الفيروسية في:",
   P(("Cary-Blair medium", "وسط كاري-بلير"), ("Stuart’s medium", "وسط ستيوارت"), ("Viral transport medium (VTM)", "وسط النقل الفيروسي"), ("Blood culture bottle", "قنينة زرع الدم")), "c"),

 {"topic_en": "Picture questions", "topic_ar": "أسئلة الصور"},
 Q("The item in the picture is:", "الأداة في الصورة هي:",
   P(("Blood culture bottle", "قنينة زرع دم"), ("Swab with transport medium", "مسحة مع وسط نقل"), ("Urine container", "حاوية إدرار"), ("Lumbar puncture needle", "إبرة بزل قطني")), "b",
   img="assets/swab-transport.png", img_h="34mm"),
 Q("This container is labelled for:", "هذه الحاوية معلَّمة لـ:",
   P(("Stool C/S", "زرع البراز"), ("Sputum C/S", "زرع القشع وحساسيته"), ("CSF", "السائل الدماغي الشوكي"), ("Blood culture", "زرع الدم")), "b",
   img="assets/sputum-container.png", img_h="34mm"),
]

tf = [
 TF("The time of specimen collection affects successful isolation of pathogens.", "يؤثّر وقت جمع العيّنة في نجاح عزل الممرضات.", "T"),
 TF("Travel history is part of the supporting clinical information.", "تاريخ السفر جزء من المعلومات السريرية الداعمة.", "T"),
 TF("Refrigeration at 4 ºC increases the multiplication of commensals.", "التبريد بدرجة 4 مْ يزيد تكاثر المتعايشات.", "F"),
 TF("Freezing at -70 ºC is done in the presence of glycerol or serum.", "يُجرى التجميد بدرجة 70- مْ بوجود الكليسيرول أو المصل.", "T"),
 TF("Fluid specimens need sufficient absorbent material.", "تحتاج العيّنات السائلة مادة ماصّة كافية.", "T"),
 TF("Non-culture techniques are useful when the microorganism is slow-growing.", "التقنيات غير الزرعية مفيدة عندما يكون الكائن بطيء النمو.", "T"),
 TF("Specimens should be collected after antibiotics.", "يجب جمع العيّنات بعد المضادات الحيوية.", "F"),
 TF("Urine for culture is a midstream clean-catch specimen.", "عيّنة الإدرار للزرع هي عيّنة منتصف الإدرار النظيفة.", "T"),
 TF("Swabs should include normal flora.", "يجب أن تشمل المسحات الفلورا الطبيعية.", "F"),
 TF("In wound infection, a swab is preferred over an aspirate.", "في عدوى الجروح تُفضَّل المسحة على الرشافة.", "F"),
 TF("Cary-Blair medium is used for stool specimens.", "يُستخدم وسط كاري-بلير لعيّنات البراز.", "T"),
 TF("CSF specimens can wait in the refrigerator before transport.", "يمكن أن تنتظر عيّنات السائل الدماغي الشوكي في الثلاجة قبل النقل.", "F"),
]
traps = [
 TR("Refrigerate or freeze?", "تبريد أم تجميد؟", "Refrigeration is at 4 ºC (preserves cells, reduces commensals); freezing is at -70 ºC or below with glycerol or serum.", "التبريد بدرجة 4 مْ (يحفظ الخلايا ويقلّل المتعايشات)؛ والتجميد بدرجة 70- مْ أو أقل مع الكليسيرول أو المصل."),
 TR("Aspirate or swab in wounds?", "رشافة أم مسحة في الجروح؟", "The aspirate is preferred over the swab.", "الرشافة مفضّلة على المسحة."),
 TR("Which transport medium for stool?", "أي وسط نقل للبراز؟", "Cary-Blair — Stuart’s and Amies are for swabs, VTM for viral samples.", "كاري-بلير — أما ستيوارت وآميز فللمسحات، ووسط النقل الفيروسي للعيّنات الفيروسية."),
 TR("Sputum or saliva?", "قشع أم لعاب؟", "Deep cough sputum, early morning; saliva must be avoided.", "قشع سعال عميق في الصباح الباكر؛ ويجب تجنّب اللعاب."),
 TR("Is serology a culture technique?", "هل الفحص المصلي تقنية زرعية؟", "No — direct microscopy, immunological methods, serology and NAAT are non-culture techniques.", "لا — الفحص المجهري المباشر والطرائق المناعية والفحوص المصلية وتقنيات تضخيم الأحماض النووية كلها تقنيات غير زرعية."),
]
important = [
 IM("What must be correct for pathogens to be isolated successfully?", "ما الذي يجب أن يكون صحيحًا لعزل الممرضات بنجاح؟", "The type of specimen, collection of specimen, time of specimen and method of its dispatch to the laboratory.", "نوع العيّنة، وجمعها، ووقتها، وطريقة إرسالها إلى المختبر."),
 IM("List the information included in the request form.", "عدّد المعلومات التي تتضمّنها استمارة الطلب.", "Patient details, clinical diagnosis, onset of symptoms, sample type, time of collection, treatment history and antimicrobial therapy, other health and safety issues, and supporting clinical information (travel history, contact with infected individuals).", "تفاصيل المريض، التشخيص السريري، بداية الأعراض، نوع العيّنة، وقت الجمع، تاريخ العلاج والعلاج بالمضادات، أمور الصحة والسلامة الأخرى، والمعلومات السريرية الداعمة (تاريخ السفر والاختلاط بالمصابين)."),
 IM("List the rules for transport of microbiological specimens.", "عدّد قواعد نقل العيّنات الميكروبيولوجية.", "Reach the lab as soon as possible or use a preservative/transport medium; refrigerate at 4 ºC or freeze at -70 ºC with glycerol or serum; crack-free leak-proof container; seal the cap with adhesive tape; packaging for glass; absorbent material for fluids; mark highly infectious specimens “HIGH RISK”.", "الوصول إلى المختبر بأسرع وقت أو استخدام حافظة/وسط نقل؛ التبريد بدرجة 4 مْ أو التجميد بدرجة 70- مْ مع الكليسيرول أو المصل؛ حاوية بلا شقوق وغطاء لا يسرّب؛ إحكام الغطاء بشريط لاصق؛ مواد تغليف للزجاج؛ مادة ماصّة للسوائل؛ تعليم العيّنات شديدة العدوى «خطورة عالية»."),
 IM("When are non-culture techniques important? Give examples.", "متى تكون التقنيات غير الزرعية مهمة؟ أعطِ أمثلة.", "When the microorganism cannot be readily cultured in vitro, is slow-growing, or when rapid diagnosis influences management; e.g., direct microscopy, immunological methods, serology, NAAT.", "عندما لا يمكن زرع الكائن بسهولة، أو يكون بطيء النمو، أو عندما يؤثّر التشخيص السريع في التدبير؛ مثل الفحص المجهري المباشر والطرائق المناعية والفحوص المصلية وتقنيات تضخيم الأحماض النووية."),
 IM("List the principles of specimen collection.", "عدّد مبادئ جمع العيّنات.", "Correct site, before antibiotics, aseptic technique, sufficient quantity, proper labelling, sterile containers, immediate transport.", "الموقع الصحيح، قبل المضادات، تقنية معقّمة، كمية كافية، ملصق صحيح، حاويات معقّمة، نقل فوري."),
 IM("Match each transport medium with its use.", "طابق كل وسط نقل مع استخدامه.", "Stuart’s: swabs (throat, wound, genital); Amies: swabs with or without charcoal; Cary-Blair: stool; VTM: viral samples (nasal, throat swabs).", "ستيوارت: المسحات (البلعوم، الجروح، التناسلية)؛ آميز: المسحات مع الفحم أو بدونه؛ كاري-بلير: البراز؛ وسط النقل الفيروسي: العيّنات الفيروسية (مسحات الأنف والبلعوم)."),
]
meta = dict(BAC, unit_en="Lab 2", unit_ar="العملي 2", unit_no="2",
            title_en="Selection, Collection, and Transport of Specimens for Microbiological Examination",
            title_ar="اختيار العيّنات وجمعها ونقلها للفحص الميكروبيولوجي")
from bal import balance
save("bacteriology-lab2-specimens", meta, blocks, balance(mcq), tf, traps, important)

```
