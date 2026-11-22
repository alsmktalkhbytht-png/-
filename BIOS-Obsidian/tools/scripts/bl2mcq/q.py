import sys, json, os, shutil
from collections import Counter
WORK = "/home/claude/scratch/work"
sys.path.insert(0, WORK + "/bac"); from bal import balance
sys.path.insert(0, WORK); from bidi import ltr_all

# Diagnostic Microbiology — PRACTICAL Lab 2 (stage 4, د. هبة سامي; slides by MSc. Ammar Hassan & MSc. Ali Thamer):
# Selection, Collection, and Transport of Specimens for Microbiological Examination.
# Source 2026-11-22: the same 11-slide deck as bacteriology-lab2-specimens/, a class-annotated copy (highlights; handwritten
# organisms beside the transport media: Stuart's → Bordetella, Amies → H. influenzae, Cary-Blair → Vibrio cholerae,
# VTM → "SARS-CoV-19"). Same request pattern as Lab 1 ("حتى الصور") → comprehensive bilingual MCQ bank WITH pictures.
# Pictures = the clean copies in bacteriology-lab2-specimens/assets. Correct option first ("a"); fixed= keeps
# "All of the above" last and sets its key after balance().

def Q(en, ar, opts, why_en, why_ar, img=None, h="38mm", fixed=None):
    d = dict(en=en, ar=ar, options=[list(o) for o in opts], note_en=why_en, note_ar=why_ar)
    if fixed: d["_fixed"] = fixed
    else: d["answer"] = "a"
    if img: d.update(img="assets/" + img, img_h=h)
    return d
def T(en, ar): return {"topic_en": en, "topic_ar": ar}
ALL = ("All of the above", "جميع ما سبق")
S = lambda x: f"__{x}__"

mcq = [
 T("Introduction", "مقدّمة"),
 Q("The role of the laboratory in the diagnosis of infections can be considered:", "يمكن عدّ دور المختبر في تشخيص العدوى:",
   [("A major step of diagnostic microbiology", "خطوة رئيسية من خطوات الأحياء المجهرية التشخيصية"), ("A minor step that can be skipped", "خطوة ثانوية يمكن تجاوزها"),
    ("Only an administrative step", "خطوة إدارية فقط"), ("Unrelated to diagnosis", "غير مرتبط بالتشخيص")],
   "Slide 2 (highlighted).", "الشريحة 2 (مظلَّلة)."),
 Q("If pathogens are to be isolated successfully, which must be correct?", "لكي تُعزل الممرضات بنجاح، أيّ مما يأتي يجب أن يكون صحيحًا؟",
   [("The type of specimen", "نوع العيّنة"), ("Collection of the specimen", "جمع العيّنة"), ("Time of the specimen and method of its dispatch to the laboratory", "وقت العيّنة وطريقة إرسالها إلى المختبر"), ALL],
   "Four things must be correct: type, collection, time, and method of dispatch.", "أربعة أشياء يجب أن تكون صحيحة: النوع، الجمع، الوقت، وطريقة الإرسال.", fixed="d"),
 Q("How many conditions must be correct for successful isolation of pathogens?", "كم شرطًا يجب أن يكون صحيحًا لعزل الممرضات بنجاح؟",
   [("4", "4"), ("2", "2"), ("3", "3"), ("6", "6")],
   "Type, collection, time, method of dispatch.", "النوع، الجمع، الوقت، طريقة الإرسال."),

 T("The request form", "نموذج الطلب"),
 Q("A detailed request form that accompanies a clinical sample is pivotal in:", "نموذج الطلب التفصيلي المرافق للعيّنة السريرية محوري في:",
   [("Ensuring the appropriate diagnostic procedures are undertaken", "ضمان إجراء الفحوص التشخيصية المناسبة"), ("Reducing the cost of the test", "تقليل كلفة الفحص"),
    ("Sterilizing the specimen", "تعقيم العيّنة"), ("Replacing the culture", "الاستغناء عن الزرع")],
   "Slide 3 opening sentence.", "الجملة الأولى في الشريحة 3."),
 Q("Which of the following should be included in the request form?", "أيّ مما يأتي يجب أن يتضمّنه نموذج الطلب؟",
   [("Patient details and clinical diagnosis", "بيانات المريض والتشخيص السريري"), ("The patient's salary", "راتب المريض"),
    ("The colour of the specimen container only", "لون حاوية العيّنة فقط"), ("The name of the culture medium manufacturer", "اسم الشركة المصنّعة للوسط الزرعي")],
   "The list: patient details, clinical diagnosis, onset of symptoms, sample type, time of collection, treatment history and antimicrobial therapy, other health and safety issues.",
   "القائمة: بيانات المريض، التشخيص السريري، بداية الأعراض، نوع العيّنة، وقت الجمع، تاريخ العلاج والعلاج بمضادات الميكروبات، قضايا الصحة والسلامة الأخرى."),
 Q("“Treatment history and antimicrobial therapy” in the request form is important because:", "«تاريخ العلاج والعلاج بمضادات الميكروبات» في نموذج الطلب مهم لأن:",
   [("Prior antibiotics can affect culture results", "المضادات الحيوية السابقة قد تؤثّر في نتائج الزرع"), ("It decides the price", "يحدّد السعر"),
    ("It replaces the clinical diagnosis", "يغني عن التشخيص السريري"), ("It is needed for the label colour", "مطلوب للون الملصق")],
   "Collecting after antibiotics is listed as a common error — antibiotics can make the culture falsely negative.",
   "الجمع بعد المضادات الحيوية مذكور خطأً شائعًا — فالمضادات قد تجعل الزرع سلبيًّا كاذبًا."),
 Q("Which of the following is NOT listed in the request form information?", "أيّ مما يأتي ليس من معلومات نموذج الطلب المذكورة؟",
   [("The patient's blood group", "زمرة دم المريض"), ("Onset of symptoms", "بداية الأعراض"), ("Sample type", "نوع العيّنة"), ("Time of collection", "وقت الجمع")],
   "Blood group is not on the slide's list.", "زمرة الدم ليست في قائمة الشريحة."),
 Q("Supporting clinical information that is also important includes:", "المعلومات السريرية الداعمة المهمة أيضًا تشمل:",
   [("Travel history and contact with infected individuals", "تاريخ السفر والتماس مع أشخاص مصابين"), ("The patient's hobbies", "هوايات المريض"),
    ("The patient's education", "تعليم المريض"), ("The hospital's address", "عنوان المستشفى")],
   "Last line of slide 3.", "آخر سطر في الشريحة 3."),
 Q("The tube shown is a:", "الأنبوب المعروض هو:",
   [("Swab with transport medium", "مسحة مع وسط نقل"), ("Blood culture bottle", "قنينة زرع دم"), ("Urine container", "حاوية إدرار"), ("Petri dish", "طبق بتري")],
   "The picture is labelled “Swab with transport media” (Amies transport medium tube).", "الصورة معنونة «مسحة مع وسط نقل» (أنبوب وسط نقل Amies).", img="swab-transport.png", h="34mm"),
 Q("The container in the image is labelled for:", "الحاوية في الصورة معنونة لـ:",
   [("Sputum culture and sensitivity (C/S)", "زرع القشع وفحص الحساسية (C/S)"), ("Stool culture", "زرع البراز"), ("Blood culture", "زرع الدم"), ("CSF analysis", "تحليل السائل الشوكي")],
   "C/S = culture and sensitivity.", "C/S = الزرع والحساسية.", img="sputum-container.png", h="34mm"),

 T("Transport of microbiological specimens", "نقل العيّنات الميكروبيولوجية"),
 Q("A specimen should reach the laboratory:", "يجب أن تصل العيّنة إلى المختبر:",
   [("As soon as possible, or a suitable preservative or transport medium must be used", "بأسرع وقت ممكن، أو يُستعمل حافظ أو وسط نقل مناسب"), ("After 48 hours", "بعد 48 ساعة"),
    ("At the end of the day", "في نهاية اليوم"), ("Only when frozen", "مجمّدة فقط")],
   "First transport rule.", "أول قاعدة من قواعد النقل."),
 Q("Refrigeration of the sample is done at:", "يكون تبريد العيّنة عند:",
   [("`4 ºC`", "`4 ºC`"), ("`37 ºC`", "`37 ºC`"), ("`-70 ºC`", "`-70 ºC`"), ("`25 ºC`", "`25 ºC`")],
   "4 ºC = refrigeration; −70 ºC = freezing.", "4 درجات = تبريد؛ −70 = تجميد."),
 Q("Refrigeration at 4 ºC helps to:", "التبريد عند 4 درجات يساعد على:",
   [("Preserve cells and reduce the multiplication of commensals in unpreserved specimens", "حفظ الخلايا وتقليل تكاثر المتعايشات في العيّنات غير المحفوظة"),
    ("Kill all pathogens", "قتل جميع الممرضات"), ("Increase the growth of pathogens", "زيادة نمو الممرضات"), ("Sterilize the specimen", "تعقيم العيّنة")],
   "Highlighted in class.", "مظلَّلة بالمحاضرة."),
 Q("Freezing of specimens is done at:", "يكون تجميد العيّنات عند:",
   [("`-70 ºC` or below, with a stabilizing fluid", "`-70 ºC` أو أقل، مع سائل مثبِّت"), ("`4 ºC`", "`4 ºC`"), ("`0 ºC` without any fluid", "`0 ºC` بلا أي سائل"), ("`-4 ºC`", "`-4 ºC`")],
   "−70 ºC or below in the presence of a stabilizing fluid.", "−70 أو أقل بوجود سائل مثبِّت."),
 Q("Examples of the stabilizing fluid used for freezing are:", "أمثلة السائل المثبِّت المستعمل للتجميد:",
   [("Glycerol or serum", "الغليسرول أو المصل"), ("Alcohol or phenol", "الكحول أو الفينول"), ("Formalin", "الفورمالين"), ("Distilled water only", "الماء المقطّر فقط")],
   "Glycerol or serum (highlighted).", "الغليسرول أو المصل (مظلَّلة)."),
 Q("The specimen container must be:", "يجب أن تكون حاوية العيّنة:",
   [("Free from cracks with a leak-proof cap", "خالية من الشقوق وغطاؤها مانع للتسرّب"), ("Made of paper", "من الورق"),
    ("Open to allow air", "مفتوحة لدخول الهواء"), ("Reused without washing", "مُعاد استعمالها بلا غسل")],
   "Transport rule 4.", "قاعدة النقل 4."),
 Q("Sealing round the container cap with adhesive tape prevents:", "إحكام الغطاء بشريط لاصق يمنع:",
   [("Loosening and leakage during transit", "ارتخاء الغطاء والتسرّب أثناء النقل"), ("Growth of bacteria", "نمو البكتيريا"),
    ("Freezing of the specimen", "تجمّد العيّنة"), ("Labelling errors", "أخطاء الوسم")],
   "Transport rule 5.", "قاعدة النقل 5."),
 Q("If the container is a glass tube or bottle, you should:", "إذا كانت الحاوية أنبوبًا أو قنينة زجاجية، يجب:",
   [("Use sufficient packaging material to protect the specimen", "استعمال مادة تغليف كافية لحماية العيّنة"), ("Use absorbent material only", "استعمال مادة ماصّة فقط"),
    ("Freeze it immediately", "تجميدها فورًا"), ("Avoid labelling it", "تجنّب وسمها")],
   "The slide says “prefect” — a typo for “protect”.", "الشريحة كتبت «prefect» وهو خطأ طباعي صوابه «protect» (يحمي)."),
 Q("If the specimen is fluid, you should use:", "إذا كانت العيّنة سائلة، يجب استعمال:",
   [("Sufficient absorbent material to absorb it", "مادة ماصّة كافية لامتصاصها"), ("Packaging material only", "مادة تغليف فقط"),
    ("A paper envelope", "ظرف ورقي"), ("A larger glass bottle", "قنينة زجاجية أكبر")],
   "Glass → packaging material; fluid → absorbent material.", "زجاج ← مادة تغليف؛ سائل ← مادة ماصّة."),
 Q("Specimens that may contain highly infectious organisms must be marked:", "العيّنات التي قد تحتوي على كائنات شديدة العدوى يجب وسمها بـ:",
   [("“HIGH RISK”", "«HIGH RISK» (خطورة عالية)"), ("“LOW RISK”", "«LOW RISK»"), ("“STERILE”", "«STERILE»"), ("“URGENT ONLY”", "«URGENT ONLY»")],
   "Last transport rule.", "آخر قاعدة من قواعد النقل."),

 T("Non-culture techniques", "التقنيات غير الزرعية"),
 Q("Non-culture techniques are used after receipt of the sample to:", "تُستعمل التقنيات غير الزرعية بعد استلام العيّنة لـ:",
   [("Provide rapid clinical information that may benefit patient management", "تقديم معلومات سريرية سريعة قد تفيد في تدبير المريض"),
    ("Replace the request form", "الاستغناء عن نموذج الطلب"), ("Sterilize the specimen", "تعقيم العيّنة"), ("Transport the specimen", "نقل العيّنة")],
   "Key word: rapid.", "الكلمة المفتاحية: سريعة."),
 Q("Non-culture techniques are of importance when:", "تكون التقنيات غير الزرعية مهمة عندما:",
   [("The microorganism cannot be readily cultured in vitro", "لا يمكن زرع الكائن بسهولة في المختبر"), ("The microorganism is slow-growing", "يكون الكائن بطيء النمو"),
    ("Rapid laboratory diagnosis significantly influences clinical management", "يؤثّر التشخيص المختبري السريع كثيرًا في التدبير السريري"), ALL],
   "Three situations, all highlighted in class.", "ثلاث حالات، كلها مظلَّلة بالمحاضرة.", fixed="d"),
 Q("Which of the following is NOT a non-culture technique?", "أيّ مما يأتي ليس تقنية غير زرعية؟",
   [("Blood culture", "زرع الدم"), ("Direct microscopy", "الفحص المجهري المباشر"), ("Serology", "الفحوص المصلية"), ("Nucleic acid amplification techniques (NAAT)", "تقنيات تضخيم الحمض النووي (NAAT)")],
   "Non-culture: direct microscopy, immunological methods, serology, NAAT.", "غير الزرعية: المجهر المباشر، الطرق المناعية، المصلية، NAAT."),
 Q("NAAT stands for:", "NAAT اختصار لـ:",
   [("Nucleic acid amplification techniques", "تقنيات تضخيم الحمض النووي"), ("Natural antibody assay test", "فحص الأجسام المضادة الطبيعية"),
    ("Non-aseptic transport technique", "تقنية النقل غير المعقّم"), ("Nutrient agar test", "اختبار الأجار المغذّي")],
   "NAAT = nucleic acid amplification techniques (e.g. PCR).", "NAAT = تقنيات تضخيم الحمض النووي (مثل PCR)."),

 T("Principles of specimen collection", "مبادئ جمع العيّنات"),
 Q("Which of the following is a principle of specimen collection?", "أيّ مما يأتي من مبادئ جمع العيّنات؟",
   [("Collect before antibiotics", "الجمع قبل المضادات الحيوية"), ("Collect after antibiotics", "الجمع بعد المضادات الحيوية"),
    ("Use non-sterile containers", "استعمال حاويات غير معقّمة"), ("Delay transport", "تأخير النقل")],
   "The seven principles: correct site, before antibiotics, aseptic technique, sufficient quantity, label properly, sterile containers, transport immediately.",
   "المبادئ السبعة: الموقع الصحيح، قبل المضادات، تقنية معقّمة، كمية كافية، وسم صحيح، حاويات معقّمة، نقل فوري."),
 Q("Which of the following is NOT a principle of specimen collection?", "أيّ مما يأتي ليس من مبادئ جمع العيّنات؟",
   [("Collect the smallest possible quantity", "جمع أقل كمية ممكنة"), ("Collect from the correct site", "الجمع من الموقع الصحيح"),
    ("Use aseptic technique", "استعمال تقنية معقّمة"), ("Label properly", "الوسم الصحيح")],
   "The principle is “collect sufficient quantity”.", "المبدأ هو «جمع كمية كافية»."),
 Q("The number of principles of specimen collection on the slide is:", "عدد مبادئ جمع العيّنات في الشريحة:",
   [("7", "7"), ("5", "5"), ("6", "6"), ("4", "4")],
   "Seven principles.", "سبعة مبادئ."),

 T("Collection techniques", "تقنيات الجمع"),
 Q("Urine is collected as:", "يُجمع الإدرار بطريقة:",
   [("Midstream clean-catch", "منتصف الجريان مع التنظيف (clean-catch)"), ("The first drops only", "القطرات الأولى فقط"),
    ("A 24-hour sample in an open container", "عيّنة 24 ساعة في حاوية مفتوحة"), ("Lumbar puncture", "البزل القطني")],
   "Urine: midstream clean-catch.", "الإدرار: منتصف الجريان مع التنظيف."),
 Q("The container in the image is suitable for collecting:", "الحاوية في الصورة مناسبة لجمع:",
   [("Urine (midstream) in a sterile container", "الإدرار (منتصف الجريان) في حاوية معقّمة"), ("Blood culture", "زرع الدم"),
    ("CSF by lumbar puncture", "السائل الشوكي بالبزل القطني"), ("Throat swab", "مسحة البلعوم")],
   "A sterile screw-cap specimen container, used for urine (and sputum/stool).", "حاوية عيّنات معقّمة بغطاء لولبي، تُستعمل للإدرار (وللقشع والبراز).", img="urine-container.png", h="34mm"),
 Q("Sputum should be:", "يجب أن يكون القشع:",
   [("A deep cough specimen", "عيّنة سعال عميق"), ("Saliva", "لعابًا"), ("Collected at night after meals", "مجموعًا ليلًا بعد الأكل"), ("Mixed with urine", "ممزوجًا بالإدرار")],
   "Sputum: deep cough specimen; avoid saliva.", "القشع: عيّنة سعال عميق؛ وتجنّب اللعاب."),
 Q("Swabs should be:", "يجب أن تكون المسحات:",
   [("Sterile cotton, avoiding normal flora", "قطنية معقّمة، مع تجنّب الفلورا الطبيعية"), ("Non-sterile, from any site", "غير معقّمة، من أي موقع"),
    ("Dry and reused", "جافّة ومُعاد استعمالها"), ("Taken after antibiotics", "مأخوذة بعد المضادات")],
   "Swabs: sterile cotton, avoid normal flora.", "المسحات: قطن معقّم، تجنّب الفلورا الطبيعية.", img="swabs.png", h="34mm"),
 Q("Stool specimens should be:", "يجب أن تكون عيّنات البراز:",
   [("A small amount, avoiding urine", "كمية صغيرة، مع تجنّب الإدرار"), ("A large amount mixed with urine", "كمية كبيرة ممزوجة بالإدرار"),
    ("Collected by lumbar puncture", "مجموعة بالبزل القطني"), ("Frozen without fluid", "مجمّدة بلا سائل")],
   "Stool: small amount, avoid urine.", "البراز: كمية صغيرة، تجنّب الإدرار."),
 Q("CSF is collected by:", "يُجمع السائل الشوكي (CSF) بـ:",
   [("Lumbar puncture", "البزل القطني"), ("Midstream clean-catch", "منتصف الجريان"), ("Deep cough", "السعال العميق"), ("Throat swab", "مسحة البلعوم")],
   "CSF: lumbar puncture.", "السائل الشوكي: البزل القطني."),
 Q("Blood is collected by:", "يُجمع الدم بـ:",
   [("Aseptic collection", "الجمع المعقّم"), ("Clean-catch", "الالتقاط النظيف"), ("Deep cough", "السعال العميق"), ("Cotton swab", "المسحة القطنية")],
   "Blood: aseptic collection.", "الدم: جمع معقّم."),

 T("Common errors to avoid", "أخطاء شائعة يجب تجنّبها"),
 Q("Which of the following is a common error to avoid?", "أيّ مما يأتي من الأخطاء الشائعة التي يجب تجنّبها؟",
   [("Collecting after antibiotics", "الجمع بعد المضادات الحيوية"), ("Contaminated containers", "الحاويات الملوّثة"),
    ("Delayed transport, missing labels and insufficient specimen", "تأخير النقل، الملصقات المفقودة، والعيّنة غير الكافية"), ALL],
   "Five errors listed: after antibiotics, contaminated containers, delayed transport, missing labels, insufficient specimen.",
   "خمسة أخطاء: بعد المضادات، الحاويات الملوّثة، تأخير النقل، فقدان الملصقات، العيّنة غير الكافية.", fixed="d"),
 Q("Which of the following is NOT one of the common errors listed?", "أيّ مما يأتي ليس من الأخطاء الشائعة المذكورة؟",
   [("Using sterile containers", "استعمال حاويات معقّمة"), ("Delayed transport", "تأخير النقل"), ("Missing labels", "فقدان الملصقات"), ("Insufficient specimen", "العيّنة غير الكافية")],
   "Sterile containers is a principle, not an error.", "الحاويات المعقّمة مبدأ لا خطأ."),

 T("Selection of specimens", "اختيار العيّنات"),
 Q("For respiratory infection, the note on the specimen is:", "في عدوى الجهاز التنفّسي، الملاحظة على العيّنة:",
   [("Avoid saliva; collect early morning sputum", "تجنّب اللعاب؛ واجمع قشع الصباح الباكر"), ("Aspirate preferred over swab", "الرشافة أفضل من المسحة"),
    ("Urgent transport to lab", "نقل عاجل إلى المختبر"), ("Use midstream portion", "استعمل منتصف الجريان")],
   "Respiratory: sputum, throat swab, nasopharyngeal swab.", "التنفّسي: القشع، مسحة البلعوم، مسحة البلعوم الأنفي."),
 Q("The specimen required for urinary tract infection is:", "العيّنة المطلوبة لعدوى المسالك البولية:",
   [("Midstream urine (MSU)", "إدرار منتصف الجريان (MSU)"), ("Blood culture", "زرع الدم"), ("Sputum", "القشع"), ("Pus aspirate", "رشافة القيح")],
   "Note: sterile container, midstream portion.", "الملاحظة: حاوية معقّمة، منتصف الجريان."),
 Q("In wound infection:", "في عدوى الجروح:",
   [("Aspirate is preferred over swab", "الرشافة مفضّلة على المسحة"), ("Swab is preferred over aspirate", "المسحة مفضّلة على الرشافة"),
    ("Only blood culture is used", "يُستعمل زرع الدم فقط"), ("Saliva is collected", "يُجمع اللعاب")],
   "Wound specimens: swab, pus aspirate, tissue biopsy.", "عيّنات الجرح: مسحة، رشافة قيح، خزعة نسيج."),
 Q("For bloodstream infection, blood culture should be collected:", "في عدوى مجرى الدم، يجب جمع زرع الدم:",
   [("Before antibiotics", "قبل المضادات الحيوية"), ("After antibiotics", "بعد المضادات الحيوية"), ("Only at night", "ليلًا فقط"), ("After 3 days of treatment", "بعد 3 أيام من العلاج")],
   "Bloodstream infection note.", "ملاحظة عدوى مجرى الدم."),
 Q("CSF infection requires:", "عدوى السائل الشوكي تتطلّب:",
   [("Urgent transport to the lab", "نقلًا عاجلًا إلى المختبر"), ("Refrigeration for 24 hours", "تبريدًا 24 ساعة"),
    ("Collecting early morning", "الجمع صباحًا باكرًا"), ("Avoiding saliva", "تجنّب اللعاب")],
   "CSF note: urgent transport.", "ملاحظة السائل الشوكي: نقل عاجل."),

 T("Transport media", "أوساط النقل"),
 Q("Stuart's medium is used for:", "يُستعمل وسط ستيوارت لـ:",
   [("Swabs (throat, wound, genital)", "المسحات (البلعوم، الجروح، التناسلية)"), ("Stool specimens", "عيّنات البراز"),
    ("Viral samples", "العيّنات الفيروسية"), ("Blood culture", "زرع الدم")],
   "Stuart's → swabs (throat, wound, genital).", "ستيوارت ← المسحات (البلعوم، الجروح، التناسلية)."),
 Q("Amies medium is used for:", "يُستعمل وسط أميس لـ:",
   [("Swabs, with or without charcoal", "المسحات، مع الفحم أو بدونه"), ("Stool specimens", "عيّنات البراز"), ("CSF", "السائل الشوكي"), ("Urine", "الإدرار")],
   "Amies → swabs (with or without charcoal).", "أميس ← المسحات (مع الفحم أو بدونه)."),
 Q("Cary-Blair medium is used for:", "يُستعمل وسط كاري-بلير لـ:",
   [("Stool specimens", "عيّنات البراز"), ("Throat swabs", "مسحات البلعوم"), ("Viral samples", "العيّنات الفيروسية"), ("Sputum", "القشع")],
   "Cary-Blair → stool.", "كاري-بلير ← البراز."),
 Q("Viral transport medium (VTM) is used for:", "يُستعمل وسط النقل الفيروسي (VTM) لـ:",
   [("Viral samples (nasal, throat swabs)", "العيّنات الفيروسية (مسحات الأنف والبلعوم)"), ("Stool specimens", "عيّنات البراز"),
    ("Wound swabs only", "مسحات الجروح فقط"), ("Blood culture", "زرع الدم")],
   "VTM → viral nasal and throat swabs.", "VTM ← المسحات الفيروسية من الأنف والبلعوم."),
 Q("Class note: which organism was written beside Cary-Blair medium?", "ملاحظة المحاضرة: أيّ كائن كُتب بجانب وسط كاري-بلير؟",
   [(S("Vibrio cholerae"), "ضمّة الكوليرا"), (S("Bordetella"), "البورديتيلا"), (S("Haemophilus influenzae"), "المستدمية النزلية"), ("SARS-CoV-2", "فيروس SARS-CoV-2")],
   "Handwritten in class: Stuart's → Bordetella, Amies → H. influenzae, Cary-Blair → Vibrio cholerae, VTM → SARS-CoV.",
   "مكتوب بخط اليد بالمحاضرة: ستيوارت ← البورديتيلا، أميس ← المستدمية النزلية، كاري-بلير ← ضمّة الكوليرا، VTM ← فيروس كورونا."),
 Q("Class note: the organism written beside the viral transport medium (VTM) is:", "ملاحظة المحاضرة: الكائن المكتوب بجانب وسط النقل الفيروسي (VTM):",
   [("SARS-CoV-2 (the COVID-19 virus)", "فيروس SARS-CoV-2 (فيروس كوفيد-19)"), (S("Vibrio cholerae"), "ضمّة الكوليرا"), (S("Bordetella"), "البورديتيلا"), (S("Haemophilus influenzae"), "المستدمية النزلية")],
   "The note reads “SARS-CoV-19”; the virus's name is SARS-CoV-2 and the disease is COVID-19.",
   "الملاحظة مكتوبة «SARS-CoV-19»؛ واسم الفيروس الصحيح SARS-CoV-2 والمرض COVID-19."),
 Q("Class note: the organism written beside Amies medium is:", "ملاحظة المحاضرة: الكائن المكتوب بجانب وسط أميس:",
   [(S("Haemophilus influenzae"), "المستدمية النزلية"), (S("Vibrio cholerae"), "ضمّة الكوليرا"), ("SARS-CoV-2", "فيروس SARS-CoV-2"), (S("Salmonella typhi"), "السالمونيلا التيفية")],
   "Amies → H. influenzae; Stuart's → Bordetella.", "أميس ← المستدمية النزلية؛ ستيوارت ← البورديتيلا."),
]

mcq = balance(mcq, 2202)
for q in mcq:
    if "_fixed" in q: q["answer"] = q.pop("_fixed")

meta = {"subject_en": "Diagnostic Microbiology", "subject_ar": "الأحياء المجهرية التشخيصية", "short_ar": "بكتريا",
        "instructor": "د. هبة سامي", "unit_en": "Lab 2", "unit_ar": "العملي 2", "unit_label": "LAB", "unit_no": "2",
        "title_en": "Selection, Collection, and Transport of Specimens", "title_ar": "اختيار العيّنات وجمعها ونقلها",
        "department": "قسم التحليلات", "kind": "Laboratories — عملي", "questions_kind": "MCQ — أسئلة اختيار",
        "stage": "The fourth stage — الرابعة",
        "file_name": "BIOS - بكتريا عملي المحاضرة الثانية - بنك أسئلة شامل بالصور"}
Qs = {"title_en": "Selection, Collection, and Transport of Specimens — Comprehensive MCQs (with figures)",
      "title_ar": "اختيار العيّنات وجمعها ونقلها — أسئلة اختيار شاملة (مع الصور)",
      "sub": "MCQ", "answers_inline": True, "compact": True, "mcq_per_page": 4,
      "mcq_en": "Comprehensive MCQs — Lab 2", "mcq_ar": "أسئلة اختيار شاملة — العملي الثاني",
      "intro_en": ["Q. Select the most correct answer from the followings",
                   "These MCQs cover the whole lab with its own pictures; the answer and a short reason sit under each question. Questions marked “Class note” come from the organisms handwritten beside the transport media in class."],
      "intro_ar": ["س. اختر الإجابة الأصح مما يأتي",
                   "هذه الأسئلة تغطّي العملي كاملًا بصوره نفسها؛ والحل وسطر سبب مختصر تحت كل سؤال. الأسئلة المعلَّمة «ملاحظة المحاضرة» مأخوذة من الكائنات المكتوبة بخط اليد بجانب أوساط النقل بالمحاضرة."],
      "mcq": ltr_all(mcq), "tf": [], "traps": [], "important": []}

d = "/home/user/-/bacteriology-lab2-mcq"
os.makedirs(d + "/assets", exist_ok=True)
for q in mcq:
    if q.get("img"):
        shutil.copy("/home/user/-/bacteriology-lab2-specimens/" + q["img"], d + "/" + q["img"])
json.dump({"meta": meta, "questions": Qs}, open(d + "/lecture.json", "w"), ensure_ascii=False, indent=1)
qs = [m for m in mcq if "answer" in m]
print("MCQ:", len(qs), "| dist:", dict(Counter(m["answer"] for m in qs)), "| images:", sum(1 for m in qs if m.get("img")))
for i, q in enumerate(qs, 1):
    print(i, q["answer"], q["options"]["abcd".index(q["answer"])][0][:60])
