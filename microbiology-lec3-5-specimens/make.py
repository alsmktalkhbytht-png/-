# BIOS — بكتريا نظري المحاضرة 3+4+5 (Selection, collection, and transport of specimens) — د. عدنان، المرحلة الرابعة
# المصدر: نص ملصق في الرسالة (source.txt) + لقطة صفحة تبيّن مكان الشكل (1) (source-page-figure1.jpg).
# كل جملة منقولة حرفيًا ومترجمة؛ بلا تصحيح إملائي.
# لم يُنقل: «االختبار القبلً : :Pretest» الذي ظهر وسط جملة (ملصق من الصفحة يقطع الجملة) — أُبلغ المستخدم.
import json, os, random
from collections import Counter

def C(en, ar, **k):  return dict(t="card", en=en, ar=ar, **k)
def SEC(en, ar):     return dict(t="section", en=en, ar=ar)
def L(en_items, ar_items, en="", ar="", **k):
    return dict(t="card", en=en, ar=ar, list_en=en_items, list_ar=ar_items, **k)
def F(src, en, ar, **k): return dict(t="figure", src="assets/" + src, en=en, ar=ar, **k)
def TF(en, ar, a): return dict(en=en, ar=ar, answer=a)
def TR(en, ar, ae, aa): return dict(en=en, ar=ar, answer_en=ae, answer_ar=aa)
IM = TR

blocks = [
 SEC("Introduction", "المقدمة"),
 C(["The role of the laboratory in the diagnosis of infections can be considered a major steps of diagnostic microbiology.",
    "If pathogens are to be isolated successfully, the type of specimen, its collection, time and method of its dispatch to the laboratory must be correct.",
    "(Figure- 1)"],
   ["يمكن عدّ **دور المختبر في تشخيص العدوى** من الخطوات الرئيسة في الأحياء المجهرية التشخيصية.",
    "إذا أُريد **عزل المُمرِضات بنجاح**، فيجب أن يكون **نوع العيّنة**، و**جمعها**، و**وقتها**، و**طريقة إرسالها** إلى المختبر صحيحة.",
    "(الشكل - 1)"]),
 L(["Patient details.", "Clinical diagnosis.", "Onset of symptoms", "Sample type.", "Time of collection.",
    "Treatment history and concurrent antimicrobial therapy.", "Other health and safety issues."],
   ["معلومات المريض.", "التشخيص السريري.", "بداية ظهور الأعراض", "نوع العيّنة.", "وقت الجمع.",
    "تاريخ العلاج والعلاج المتزامن بمضادات الميكروبات.", "قضايا صحية وأمنية أخرى."],
   en="A detailed request form that accompanies a clinical sample is pivotal in ensuring the appropriate diagnostic procedures are undertaken; information should include:",
   ar="**استمارة الطلب المفصّلة** التي ترافق العيّنة السريرية أساسية لضمان إجراء الفحوص التشخيصية المناسبة؛ ويجب أن تتضمّن المعلومات:"),
 C("Supporting clinical information, including travel history and contact with infected individuals, is also important.",
   "و**المعلومات السريرية الداعمة**، ومنها **تاريخ السفر** و**التماس مع الأفراد المصابين**، مهمّة أيضًا."),
 F("diagnostic-pattern.jpg",
   "Figure (1): Laboratory diagnostic pattern. — Clinical request and sample collection · Sample transport · Non-culture techniques · Culture techniques · Identification and sensitivity testing · Additional diagnostic procedures",
   "الشكل (1): نمط التشخيص المختبري. — الطلب السريري وجمع العيّنة · نقل العيّنة · التقنيات غير الزرعية · التقنيات الزرعية · التشخيص وفحص الحساسية · إجراءات تشخيصية إضافية",
   h="80mm", fit="contain", nonum=True),

 SEC("Sample collection", "جمع العيّنات"),
 C("Samples for microbiological investigation require careful collection, without contamination from external sources or the patient’s own flora.",
   "تتطلّب العيّنات المخصّصة للفحص الميكروبيولوجي **جمعًا دقيقًا**، **دون تلوّث** من مصادر خارجية أو من **النبيت الطبيعي للمريض نفسه**."),
 C(["When taking clinical samples, it is important to: use sterile, leak-proof containers; label the specimen correctly; take care whilst obtaining samples through an area containing a normal flora like vein puncture through skin to obtain blood culture in this instance the skin should be decontaminated with an appropriate antiseptic prior to collecting blood.",
    "If possible, specimens for microbiological culture should be taken prior to commencement of antibiotic therapy, to avoid false-negative results."],
   ["عند أخذ العيّنات السريرية من المهم: استعمال **أوعية معقّمة محكمة لا تسرّب**؛ و**وسم العيّنة بشكل صحيح**؛ والحذر عند أخذ العيّنات عبر منطقة فيها نبيت طبيعي، مثل بزل الوريد عبر الجلد للحصول على زرع الدم، ففي هذه الحالة يجب **إزالة تلوّث الجلد بمطهّر مناسب** قبل سحب الدم.",
    "وإن أمكن، يجب أخذ عيّنات الزرع الميكروبيولوجي **قبل بدء العلاج بالمضادات الحيوية**، لتجنّب **النتائج السالبة الكاذبة**."]),

 SEC("Transport of microbiological specimens", "نقل العيّنات الميكروبيولوجية"),
 C(["Rapid transport of samples to the microbiology laboratory is essential, as many fastidious microorganisms, such as __Neisseria gonorrhoeae__ and __Haemophilus influenzae__, die during transit."],
   ["**النقل السريع** للعيّنات إلى مختبر الأحياء المجهرية ضروري، لأن كثيرًا من **الكائنات الدقيقة صعبة النمو** (`fastidious`)، مثل `__Neisseria gonorrhoeae__` و`__Haemophilus influenzae__`، **تموت أثناء النقل**."]),
 C(["Furthermore, overgrowth by contaminating normal flora confusing the pathogen may also occur."],
   ["فضلًا عن ذلك، قد يحدث **فرط نموّ النبيت الطبيعي الملوِّث** فيُربك تشخيص العامل الممرض."]),
 L(["Specimen should reach to the laboratory as soon as possible or a suitable preservative or transport medium must be used.",
    "Refrigeration of sample at 4 ºC can help to preserve cells and reduce the multiplication of commensals in unpreserved specimens.",
    "Freezing at -70 ºC or below in the presence of a stabilizing fluid, like glycerol or serum.",
    "Ensure that the specimen container is free from cracks, and the cap is leak proof.",
    "Seal round the container cap with adhesive tape to prevent loosening and leakage during transit.",
    "If the container is glass tube or bottle, use sufficient packaging material to prefect a specimen.",
    "If the specimen is fluid, use sufficient absorbent material to absorb it.",
    "Mark all specimen that may contain highly infectious organism “HIGH RISK”."],
   ["يجب أن تصل العيّنة إلى المختبر **بأسرع وقت ممكن**، وإلّا وجب استعمال **مادة حافظة أو وسط نقل** مناسب.",
    "**تبريد العيّنة بدرجة 4 °م** يساعد على حفظ الخلايا وتقليل تكاثر **الكائنات المتعايشة** في العيّنات غير المحفوظة.",
    "**التجميد بدرجة سالب 70 °م أو أقل** بوجود سائل مثبّت مثل **الغليسيرول أو المصل**.",
    "تأكّد من أنّ وعاء العيّنة **خالٍ من الشقوق** وأنّ غطاءه محكم لا يسرّب.",
    "أحكم إغلاق محيط غطاء الوعاء **بشريط لاصق** لمنع ارتخائه وتسرّبه أثناء النقل.",
    "إذا كان الوعاء أنبوبًا أو قنينة زجاجية، فاستعمل **مواد تغليف كافية** لحماية العيّنة (`prefect`).",
    "إذا كانت العيّنة سائلة، فاستعمل **مادة ماصّة كافية** لامتصاصها.",
    "علّم كل العيّنات التي قد تحتوي على كائنات شديدة العدوى بعبارة «**خطر عالٍ**» (`HIGH RISK`)."],
   en="To minimize these complications, the microbiology department may adopt several strategies such as:",
   ar="ولتقليل هذه المضاعفات، قد يعتمد قسم الأحياء المجهرية **عدّة استراتيجيات** مثل:"),

 SEC("Non-culture techniques", "التقنيات غير الزرعية"),
 C("Following receipt of the sample, the microbiology laboratory may utilize non-culture techniques to provide rapid clinical information, which may benefit patient management.",
   "بعد استلام العيّنة، قد يستعمل مختبر الأحياء المجهرية **تقنيات غير زرعية** لتوفير **معلومات سريرية سريعة** قد تفيد في إدارة حالة المريض."),
 L(["Microorganism cannot be readily cultured in vitro;",
    "Microorganism is slow-growing;",
    "Rapid laboratory diagnosis significantly influences clinical management of the patient."],
   ["لا يمكن **زرع الكائن المجهري بسهولة** في المختبر (`in vitro`)؛",
    "الكائن المجهري **بطيء النمو**؛",
    "**التشخيص المختبري السريع** يؤثّر بشكل كبير في الإدارة السريرية للمريض."],
   en="There are several situations where non culture techniques are of importance:",
   ar="هناك عدّة حالات تكون فيها **التقنيات غير الزرعية** مهمّة:"),
 C("Non-culture techniques include direct microscopy, immunological methods, serology, and nucleic acid amplification techniques (NAAT).",
   "تشمل التقنيات غير الزرعية: **الفحص المجهري المباشر**، و**الطرائق المناعية**، و**الفحوص المصلية**، و**تقنيات تضخيم الحمض النووي** (`NAAT`)."),
]

# ---------------------------------------------------------------- questions (lecture content only)
LET = list("abcd") * 6
random.Random(4).shuffle(LET)
_n = [0]
def Q(en, ar, right, wrong, **k):
    """right = (en, ar); wrong = 3 x (en, ar); the right option goes to the next balanced letter."""
    ans = LET[_n[0]]; _n[0] += 1
    opts = list(wrong); opts.insert("abcd".index(ans), right)
    return dict(en=en, ar=ar, options=[list(o) for o in opts], answer=ans, **k)

mcq = [
 {"topic_en": "Introduction and request form", "topic_ar": "المقدمة واستمارة الطلب"},
 Q("If pathogens are to be isolated successfully, which must be correct?", "إذا أُريد عزل المُمرِضات بنجاح، فما الذي يجب أن يكون صحيحًا؟",
   ("The type of specimen, its collection, time and method of its dispatch", "نوع العيّنة وجمعها ووقتها وطريقة إرسالها"),
   [("The colour of the container only", "لون الوعاء فقط"), ("The patient's blood group", "فصيلة دم المريض"), ("The laboratory temperature only", "حرارة المختبر فقط")]),
 Q("A detailed request form that accompanies a clinical sample is pivotal in:", "استمارة الطلب المفصّلة المرافقة للعيّنة أساسية في:",
   ("Ensuring the appropriate diagnostic procedures are undertaken", "ضمان إجراء الفحوص التشخيصية المناسبة"),
   [("Sterilizing the sample", "تعقيم العيّنة"), ("Freezing the sample", "تجميد العيّنة"), ("Replacing the transport medium", "الاستغناء عن وسط النقل")]),
 Q("Which of the following is listed in the information of the request form?", "أيّ ممّا يأتي من معلومات استمارة الطلب؟",
   ("Treatment history and concurrent antimicrobial therapy", "تاريخ العلاج والعلاج المتزامن بمضادات الميكروبات"),
   [("Patient's income", "دخل المريض"), ("Name of the transport company", "اسم شركة النقل"), ("Colour of the swab", "لون المسحة")]),
 Q("Supporting clinical information that is also important includes:", "من المعلومات السريرية الداعمة المهمّة أيضًا:",
   ("Travel history and contact with infected individuals", "تاريخ السفر والتماس مع الأفراد المصابين"),
   [("Favourite food", "الطعام المفضّل"), ("Blood group", "فصيلة الدم"), ("Number of siblings", "عدد الإخوة")]),

 {"topic_en": "Laboratory diagnostic pattern (Figure 1)", "topic_ar": "نمط التشخيص المختبري (الشكل 1)"},
 Q("In Figure (1), the first step of the laboratory diagnostic pattern is:", "في الشكل (1)، الخطوة الأولى في نمط التشخيص المختبري هي:",
   ("Clinical request and sample collection", "الطلب السريري وجمع العيّنة"),
   [("Culture techniques", "التقنيات الزرعية"), ("Additional diagnostic procedures", "إجراءات تشخيصية إضافية"), ("Identification and sensitivity testing", "التشخيص وفحص الحساسية")]),
 Q("In Figure (1), the last step is:", "في الشكل (1)، الخطوة الأخيرة هي:",
   ("Additional diagnostic procedures", "إجراءات تشخيصية إضافية"),
   [("Sample transport", "نقل العيّنة"), ("Non-culture techniques", "التقنيات غير الزرعية"), ("Clinical request", "الطلب السريري")]),
 Q("In Figure (1), the step that comes directly after culture techniques is:", "في الشكل (1)، الخطوة التي تأتي مباشرة بعد التقنيات الزرعية هي:",
   ("Identification and sensitivity testing", "التشخيص وفحص الحساسية"),
   [("Sample transport", "نقل العيّنة"), ("Clinical request and sample collection", "الطلب السريري وجمع العيّنة"), ("Non-culture techniques", "التقنيات غير الزرعية")]),

 {"topic_en": "Sample collection", "topic_ar": "جمع العيّنات"},
 Q("Samples for microbiological investigation require careful collection without contamination from:", "تتطلّب عيّنات الفحص الميكروبيولوجي جمعًا دقيقًا دون تلوّث من:",
   ("External sources or the patient’s own flora", "مصادر خارجية أو النبيت الطبيعي للمريض نفسه"),
   [("Transport media", "أوساط النقل"), ("Glycerol", "الغليسيرول"), ("Adhesive tape", "الشريط اللاصق")]),
 Q("Containers for clinical samples should be:", "يجب أن تكون أوعية العيّنات السريرية:",
   ("Sterile and leak-proof", "معقّمة ومحكمة لا تسرّب"),
   [("Open and clean", "مفتوحة ونظيفة"), ("Reused without washing", "مُعاد استعمالها دون غسل"), ("Made of paper", "من الورق")]),
 Q("Before collecting blood for blood culture, the skin should be:", "قبل سحب الدم لزرع الدم يجب:",
   ("Decontaminated with an appropriate antiseptic", "إزالة تلوّث الجلد بمطهّر مناسب"),
   [("Washed with tap water only", "غسل الجلد بماء الحنفية فقط"), ("Left without preparation", "تركه دون تحضير"), ("Covered with glycerol", "تغطيته بالغليسيرول")]),
 Q("Specimens for culture should, if possible, be taken prior to antibiotic therapy to avoid:", "يجب، إن أمكن، أخذ عيّنات الزرع قبل العلاج بالمضادات الحيوية لتجنّب:",
   ("False-negative results", "النتائج السالبة الكاذبة"),
   [("False-positive results only", "النتائج الموجبة الكاذبة فقط"), ("Leakage during transit", "التسرّب أثناء النقل"), ("Freezing of the sample", "تجمّد العيّنة")]),

 {"topic_en": "Transport of microbiological specimens", "topic_ar": "نقل العيّنات الميكروبيولوجية"},
 Q("Rapid transport is essential because many fastidious microorganisms die during transit, such as:", "النقل السريع ضروري لأن كائنات صعبة النمو كثيرة تموت أثناء النقل، مثل:",
   ("Neisseria gonorrhoeae and Haemophilus influenzae", "النيسيرية البنية والمستدمية النزلية"),
   [("Normal flora of the skin", "النبيت الطبيعي للجلد"), ("Commensals in refrigerated samples", "المتعايشات في العيّنات المبرّدة"), ("All bacteria equally", "كل البكتيريا بالتساوي")]),
 Q("Besides death of fastidious organisms, delay in transport may cause:", "إضافة إلى موت الكائنات صعبة النمو، قد يسبّب تأخّر النقل:",
   ("Overgrowth by contaminating normal flora confusing the pathogen", "فرط نموّ النبيت الطبيعي الملوِّث الذي يُربك تشخيص العامل الممرض"),
   [("Sterilization of the sample", "تعقيم العيّنة"), ("Increase of the pathogen only", "زيادة العامل الممرض فقط"), ("Better culture results", "نتائج زرع أفضل")]),
 Q("If the specimen cannot reach the laboratory as soon as possible:", "إذا لم تصل العيّنة إلى المختبر بأسرع وقت ممكن:",
   ("A suitable preservative or transport medium must be used", "يجب استعمال مادة حافظة أو وسط نقل مناسب"),
   [("It should be discarded", "يجب التخلّص منها"), ("It should be left at room temperature for days", "تُترك بحرارة الغرفة لأيام"), ("Nothing is needed", "لا حاجة لشيء")]),
 Q("Refrigeration of the sample is done at:", "يُبرَّد النموذج بدرجة:",
   ("4 ºC", "4 °م"), [("37 ºC", "37 °م"), ("-70 ºC", "سالب 70 °م"), ("25 ºC", "25 °م")]),
 Q("Refrigeration of unpreserved specimens helps to:", "تبريد العيّنات غير المحفوظة يساعد على:",
   ("Preserve cells and reduce the multiplication of commensals", "حفظ الخلايا وتقليل تكاثر المتعايشات"),
   [("Kill all pathogens", "قتل كل المُمرِضات"), ("Increase the multiplication of commensals", "زيادة تكاثر المتعايشات"), ("Replace culture", "الاستغناء عن الزرع")]),
 Q("Freezing at -70 ºC or below is done in the presence of a stabilizing fluid like:", "التجميد بدرجة سالب 70 °م أو أقل يكون بوجود سائل مثبّت مثل:",
   ("Glycerol or serum", "الغليسيرول أو المصل"),
   [("Alcohol", "الكحول"), ("Antiseptic", "المطهّر"), ("Tap water", "ماء الحنفية")]),
 Q("To prevent loosening and leakage during transit, the container cap is sealed with:", "لمنع ارتخاء الغطاء وتسرّبه أثناء النقل يُحكم الغطاء بـ:",
   ("Adhesive tape", "شريط لاصق"), [("Cotton", "قطن"), ("Glycerol", "غليسيرول"), ("Serum", "مصل")]),
 Q("Specimens that may contain highly infectious organisms are marked:", "العيّنات التي قد تحتوي على كائنات شديدة العدوى تُعلَّم بعبارة:",
   ("“HIGH RISK”", "«خطر عالٍ»"), [("“FRAGILE”", "«قابل للكسر»"), ("“KEEP WARM”", "«يُحفظ دافئًا»"), ("“URGENT”", "«عاجل»")]),

 {"topic_en": "Non-culture techniques", "topic_ar": "التقنيات غير الزرعية"},
 Q("Non-culture techniques are used to provide:", "تُستعمل التقنيات غير الزرعية لتوفير:",
   ("Rapid clinical information", "معلومات سريرية سريعة"),
   [("Slower results", "نتائج أبطأ"), ("Sterile containers", "أوعية معقّمة"), ("Transport media", "أوساط نقل")]),
 Q("Non-culture techniques are important when the microorganism:", "تكون التقنيات غير الزرعية مهمّة عندما يكون الكائن المجهري:",
   ("Is slow-growing", "بطيء النمو"),
   [("Grows rapidly on all media", "سريع النمو على كل الأوساط"), ("Is part of normal flora only", "من النبيت الطبيعي فقط"), ("Is frozen", "مجمّدًا")]),
 Q("Which of the following is NOT listed among non-culture techniques?", "أيّ ممّا يأتي لم يُذكر ضمن التقنيات غير الزرعية؟",
   ("Refrigeration at 4 ºC", "التبريد بدرجة 4 °م"),
   [("Direct microscopy", "الفحص المجهري المباشر"), ("Serology", "الفحوص المصلية"), ("Nucleic acid amplification techniques (NAAT)", "تقنيات تضخيم الحمض النووي (`NAAT`)")]),

 {"topic_en": "Picture questions", "topic_ar": "أسئلة الصور"},
 Q("The hidden (orange) step in this laboratory diagnostic pattern is:", "الخطوة المخفيّة (البرتقالية) في نمط التشخيص المختبري هذا هي:",
   ("Sample transport", "نقل العيّنة"),
   [("Culture techniques", "التقنيات الزرعية"), ("Additional diagnostic procedures", "إجراءات تشخيصية إضافية"), ("Identification and sensitivity testing", "التشخيص وفحص الحساسية")],
   img="assets/q-sample-transport.jpg", img_h="36mm"),
]

tf = [
 TF("The type of specimen and time of its dispatch must be correct for pathogens to be isolated successfully.", "يجب أن يكون نوع العيّنة ووقت إرسالها صحيحين لعزل المُمرِضات بنجاح.", "T"),
 TF("Onset of symptoms is not needed in the request form.", "بداية ظهور الأعراض غير مطلوبة في استمارة الطلب.", "F"),
 TF("Travel history is supporting clinical information that is also important.", "تاريخ السفر من المعلومات السريرية الداعمة المهمّة أيضًا.", "T"),
 TF("Samples may be contaminated from the patient’s own flora.", "قد تتلوّث العيّنات من النبيت الطبيعي للمريض نفسه.", "T"),
 TF("Specimens for culture should be taken after starting antibiotic therapy.", "يجب أخذ عيّنات الزرع بعد بدء العلاج بالمضادات الحيوية.", "F"),
 TF("Neisseria gonorrhoeae is a fastidious microorganism that may die during transit.", "النيسيرية البنية كائن صعب النمو قد يموت أثناء النقل.", "T"),
 TF("Refrigeration at 4 ºC increases the multiplication of commensals.", "التبريد بدرجة 4 °م يزيد تكاثر المتعايشات.", "F"),
 TF("Freezing is done at -20 ºC without any stabilizing fluid.", "يتمّ التجميد بدرجة سالب 20 °م دون أي سائل مثبّت.", "F"),
 TF("If the specimen is fluid, sufficient absorbent material should be used.", "إذا كانت العيّنة سائلة يجب استعمال مادة ماصّة كافية.", "T"),
 TF("Small cracks in the specimen container are acceptable if the cap is tight.", "الشقوق الصغيرة في وعاء العيّنة مقبولة إذا كان الغطاء محكمًا.", "F"),
 TF("Non-culture techniques are useful when the microorganism cannot be readily cultured in vitro.", "التقنيات غير الزرعية مفيدة عندما لا يمكن زرع الكائن بسهولة في المختبر.", "T"),
 TF("Culture techniques come before sample transport in Figure (1).", "تأتي التقنيات الزرعية قبل نقل العيّنة في الشكل (1).", "F"),
]

traps = [
 TR("Specimens for culture can be taken at any time during antibiotic therapy.", "يمكن أخذ عيّنات الزرع في أي وقت أثناء العلاج بالمضادات الحيوية.",
    "No — if possible they should be taken prior to commencement of antibiotic therapy, to avoid false-negative results.",
    "لا — يجب، إن أمكن، أخذها قبل بدء العلاج بالمضادات الحيوية، لتجنّب النتائج السالبة الكاذبة."),
 TR("Refrigeration at 4 ºC and freezing at -70 ºC are the same procedure.", "التبريد بدرجة 4 °م والتجميد بدرجة سالب 70 °م إجراء واحد.",
    "No — refrigeration at 4 ºC preserves cells and reduces commensals; freezing is at -70 ºC or below in a stabilizing fluid like glycerol or serum.",
    "لا — التبريد بدرجة 4 °م يحفظ الخلايا ويقلّل المتعايشات؛ أمّا التجميد فبدرجة سالب 70 °م أو أقل بوجود سائل مثبّت مثل الغليسيرول أو المصل."),
 TR("Rapid transport matters only because the pathogen may die.", "النقل السريع مهم فقط لأن العامل الممرض قد يموت.",
    "No — also because overgrowth by contaminating normal flora confusing the pathogen may occur.",
    "لا — وأيضًا لأن فرط نموّ النبيت الطبيعي الملوِّث قد يحدث فيُربك تشخيص العامل الممرض."),
 TR("Blood for culture can be drawn without preparing the skin.", "يمكن سحب دم الزرع دون تحضير الجلد.",
    "No — the skin should be decontaminated with an appropriate antiseptic prior to collecting blood, because the needle passes through an area containing normal flora.",
    "لا — يجب إزالة تلوّث الجلد بمطهّر مناسب قبل سحب الدم، لأن الإبرة تمرّ عبر منطقة فيها نبيت طبيعي."),
 TR("Non-culture techniques are used only after the organism has grown.", "تُستعمل التقنيات غير الزرعية فقط بعد نمو الكائن.",
    "No — they are used following receipt of the sample to provide rapid clinical information (e.g., when the organism cannot be cultured or is slow-growing).",
    "لا — تُستعمل بعد استلام العيّنة لتوفير معلومات سريرية سريعة (مثلًا عندما لا يمكن زرع الكائن أو يكون بطيء النمو)."),
 TR("Glass containers need no special packaging.", "الأوعية الزجاجية لا تحتاج تغليفًا خاصًا.",
    "No — if the container is a glass tube or bottle, sufficient packaging material should be used.",
    "لا — إذا كان الوعاء أنبوبًا أو قنينة زجاجية، يجب استعمال مواد تغليف كافية."),
]

important = [
 IM("What information should the request form include?", "ما المعلومات التي يجب أن تتضمّنها استمارة الطلب؟",
    "1. Patient details. 2. Clinical diagnosis. 3. Onset of symptoms. 4. Sample type. 5. Time of collection. 6. Treatment history and concurrent antimicrobial therapy. 7. Other health and safety issues. Supporting clinical information (travel history, contact with infected individuals) is also important.",
    "1. معلومات المريض. 2. التشخيص السريري. 3. بداية ظهور الأعراض. 4. نوع العيّنة. 5. وقت الجمع. 6. تاريخ العلاج والعلاج المتزامن بمضادات الميكروبات. 7. قضايا صحية وأمنية أخرى. والمعلومات السريرية الداعمة (تاريخ السفر، والتماس مع المصابين) مهمّة أيضًا."),
 IM("List the steps of the laboratory diagnostic pattern (Figure 1).", "عدّد خطوات نمط التشخيص المختبري (الشكل 1).",
    "Clinical request and sample collection → Sample transport → Non-culture techniques → Culture techniques → Identification and sensitivity testing → Additional diagnostic procedures.",
    "الطلب السريري وجمع العيّنة ← نقل العيّنة ← التقنيات غير الزرعية ← التقنيات الزرعية ← التشخيص وفحص الحساسية ← إجراءات تشخيصية إضافية."),
 IM("What is important when taking clinical samples?", "ما المهم عند أخذ العيّنات السريرية؟",
    "Use sterile, leak-proof containers; label the specimen correctly; take care when sampling through an area containing normal flora (decontaminate the skin with an antiseptic before collecting blood); take specimens before antibiotic therapy if possible, to avoid false-negative results.",
    "استعمال أوعية معقّمة محكمة؛ ووسم العيّنة بشكل صحيح؛ والحذر عند الجمع عبر منطقة فيها نبيت طبيعي (إزالة تلوّث الجلد بمطهّر قبل سحب الدم)؛ وأخذ العيّنات قبل العلاج بالمضادات الحيوية إن أمكن لتجنّب النتائج السالبة الكاذبة."),
 IM("Why is rapid transport of samples essential?", "لماذا يكون النقل السريع للعيّنات ضروريًا؟",
    "Because many fastidious microorganisms, such as Neisseria gonorrhoeae and Haemophilus influenzae, die during transit, and overgrowth by contaminating normal flora confusing the pathogen may occur.",
    "لأن كثيرًا من الكائنات صعبة النمو مثل النيسيرية البنية والمستدمية النزلية تموت أثناء النقل، وقد يحدث فرط نموّ للنبيت الطبيعي الملوِّث يُربك تشخيص العامل الممرض."),
 IM("List the strategies the microbiology department may adopt during transport.", "عدّد الاستراتيجيات التي قد يعتمدها قسم الأحياء المجهرية في النقل.",
    "Reach the lab as soon as possible or use a preservative/transport medium; refrigerate at 4 ºC; freeze at -70 ºC or below with glycerol or serum; crack-free container with leak-proof cap; seal the cap with adhesive tape; packaging material for glass; absorbent material for fluids; mark highly infectious specimens “HIGH RISK”.",
    "الوصول إلى المختبر بأسرع وقت أو استعمال مادة حافظة/وسط نقل؛ التبريد بدرجة 4 °م؛ التجميد بدرجة سالب 70 °م أو أقل مع الغليسيرول أو المصل؛ وعاء بلا شقوق وغطاء محكم؛ إحكام الغطاء بشريط لاصق؛ مواد تغليف للزجاج؛ مادة ماصّة للسوائل؛ تعليم العيّنات شديدة العدوى بعبارة «خطر عالٍ»."),
 IM("When are non-culture techniques important, and what do they include?", "متى تكون التقنيات غير الزرعية مهمّة، وماذا تشمل؟",
    "When the microorganism cannot be readily cultured in vitro, is slow-growing, or when rapid laboratory diagnosis significantly influences clinical management. They include direct microscopy, immunological methods, serology, and NAAT.",
    "عندما لا يمكن زرع الكائن بسهولة في المختبر، أو يكون بطيء النمو، أو عندما يؤثّر التشخيص السريع بشكل كبير في الإدارة السريرية. وتشمل الفحص المجهري المباشر، والطرائق المناعية، والفحوص المصلية، و`NAAT`."),
]

meta = dict(subject_en="Diagnostic Microbiology", subject_ar="الأحياء المجهرية التشخيصية", short_ar="بكتريا",
            unit_en="Lecture 3+4+5", unit_ar="المحاضرات \u20663+4+5\u2069", unit_label="LEC", unit_no="3+4+5",
            title_en="Selection, collection, and transport of specimens for microbiological examination",
            title_ar="اختيار العيّنات وجمعها ونقلها للفحص الميكروبيولوجي",
            kind="Theory — نظري", stage="The fourth stage — الرابعة", instructor="د. عدنان",
            file_name="بكتريا نظري المحاضرة الثالثة والرابعة والخامسة", questions_suffix=" اسئلة")   # user-chosen file names

folder = "microbiology-lec3-5-specimens"
qs = [q for q in mcq if "answer" in q]
print(folder, len(qs), dict(Counter(q["answer"] for q in qs)), len(tf),
      dict(Counter(t["answer"] for t in tf)), len(traps), len(important))
d = os.path.dirname(os.path.abspath(__file__))
json.dump({"meta": meta, "blocks": blocks,
           "questions": {"mcq": mcq, "tf": tf, "traps": traps, "important": important}},
          open(os.path.join(d, "lecture.json"), "w"), ensure_ascii=False, indent=1)
