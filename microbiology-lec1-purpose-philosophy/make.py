# BIOS — بكتريا نظري المحاضرة الاولى (Purpose and Philosophy) — د. عدنان، المرحلة الرابعة
# المصدر: Diagnostic Microbiology Lecture 1.md + صورتان. كل جملة إنجليزية منقولة حرفيًا ومترجمة؛
# الترجمة العربية الموجودة في المصدر استُعملت كما هي حيث تطابق الجملة (مقسّمة جملةً بجملة).
# لم يُنقل: سطر «Source: ... @hu5ks.pdf» وملاحظة المحرّر عن البند الخامس (ليسا من المحاضرة)،
# والصورة 01 (صورة زخرفية بلا معلومة ولا نص).
import json, os, random
from collections import Counter

def C(en, ar, **k):  return dict(t="card", en=en, ar=ar, **k)
def SEC(en, ar):     return dict(t="section", en=en, ar=ar)
def H2(en, ar):      return dict(t="h2", en=en, ar=ar)
def L(en_items, ar_items, en="", ar="", **k):
    return dict(t="card", en=en, ar=ar, list_en=en_items, list_ar=ar_items, **k)
def T(head, rows, **k): return dict(t="table", head=head, rows=rows, **k)
def F(src, en, ar, **k): return dict(t="figure", src="assets/" + src, en=en, ar=ar, **k)
def TF(en, ar, a): return dict(en=en, ar=ar, answer=a)
def TR(en, ar, ae, aa): return dict(en=en, ar=ar, answer_en=ae, answer_ar=aa)
IM = TR

blocks = [
 SEC("Manifestations of Infection", "مظاهر العدوى"),
 L(["The clinical presentation of an infectious disease reflects the interaction between the host and the microorganism.",
    "This interaction is affected by the host immune status and microbial virulence factors. Signs and symptoms vary according to the site and severity of infection.",
    "Diagnosis requires a composite of information, including history, physical examination, radiographic findings, and laboratory data."],
   ["يعكس **العرض السريري** لمرض معدٍ التفاعل بين **المضيف** والكائنات الحية الدقيقة.",
    "يتأثر هذا التفاعل **بالحالة المناعية للمضيف** و**عوامل الفوعة الميكروبية**. تختلف العلامات والأعراض وفقًا لموقع العدوى وشدتها.",
    "يتطلب **التشخيص** مجموعة من المعلومات، بما في ذلك التاريخ والفحص البدني والنتائج الإشعاعية والبيانات المختبرية."]),

 SEC("Microbial Causes of Infection", "الأسباب الميكروبية للعدوى"),
 L(["**Exogenous:** acquired from environmental or animal sources or from other persons.",
    "**Endogenous:** from the normal flora."],
   ["**خارجي** (`Exogenous`): مكتسب من مصادر بيئية أو حيوانية أو من أشخاص آخرين.",
    "**داخلي** (`Endogenous`): من النبيت الطبيعي."],
   en=["Infections may be caused by bacteria, viruses, fungi, and parasites.", "The pathogen may be:"],
   ar=["قد تحدث العدوى بسبب البكتيريا والفيروسات والفطريات والطفيليات.", "وقد يكون العامل الممرض:"]),

 SEC("Diagnostic Microbiology", "الأحياء المجهرية التشخيصية"),
 C("Diagnostic microbiology is the tool that makes it possible to identify the exact pathogens of infectious diseases and the most optimal therapy at the level of individual patients.",
   "**الأحياء المجهرية التشخيصية** هي الأداة التي تجعل من الممكن تحديد مسببات الأمراض الدقيقة للأمراض المعدية والعلاج الأمثل على مستوى المرضى الأفراد."),

 SEC("Conventional Methods", "الطرق التقليدية"),
 L(["Conventional methods require time to grow the microbes *in vitro* under specific conditions, and not all microbes can easily be cultured. This is followed by biochemical methods for identification, which further makes the process lengthy.",
    "Transport of the specimens under less than ideal conditions, prior use of antibiotics, and small number of organisms are among the factors that render culture-based methods less reliable."],
   ["تتطلب **الطرق التقليدية** وقتًا لزراعة الميكروبات في المختبر (`in vitro`) في ظل ظروف محددة، ولا يمكن زراعة جميع الميكروبات بسهولة. يتبع ذلك طرق كيميائية حيوية لتحديد الهوية، مما يزيد من إطالة العملية.",
    "يعد نقل العينات في ظل ظروف أقل من المثالية، والاستخدام السابق للمضادات الحيوية، والعدد القليل من الكائنات الحية من بين العوامل التي تجعل **الطرق القائمة على الزرع أقل موثوقية**."]),

 SEC("Newer Methods", "الطرق الأحدث"),
 L(["This mitigates the need for higher microbial load, presence of metabolically active viable organisms, and shortens the time.",
    "These methods can be used to detect antibiotic resistance genes directly from the specimen and help direct targeted therapy with efficacy.",
    "Since these methods will not fulfill all the diagnostic needs, a second approach is being used to shorten the time to identification after the organism has already grown."],
   ["تخفف هذه الطرق من الحاجة إلى **حمل ميكروبي أعلى** ووجود كائنات حية نشطة الأيض، كما **تقصر الوقت**.",
    "يمكن استخدام هذه الطرق للكشف عن **جينات مقاومة المضادات الحيوية** مباشرة من العينة والمساعدة في توجيه العلاج المستهدف بفعالية.",
    "نظرًا لأن هذه الطرق لن تلبي جميع الاحتياجات التشخيصية، يتم استخدام نهج ثانٍ لتقصير الوقت اللازم لتحديد الهوية بعد نمو الكائن الحي بالفعل."],
   en="Newer methods depend on amplification of nucleic acids followed by use of probes for identification.",
   ar="تعتمد **الطرق الأحدث** على **تضخيم الأحماض النووية** ثم استعمال **المجسّات** (`probes`) لتحديد الهوية."),

 SEC("Microbial Colonization", "الاستعمار الميكروبي"),
 L(["**Elimination of the microorganism without affecting the host.**",
    "**Infection** in which the organisms multiply and cause the host to react by making an immune or other type of response.",
    "**A transient or prolonged carrier state.** Infectious disease occurs when the organism causes tissue damage and loss of function of body systems."],
   ["**القضاء على الكائنات الحية الدقيقة دون التأثير على المضيف.**",
    "**العدوى** التي تتكاثر فيها الكائنات الحية وتتسبب في تفاعل المضيف عن طريق إجراء استجابة مناعية أو أي نوع آخر من الاستجابة.",
    "**حالة حاملة عابرة أو طويلة.** يحدث **المرض المعدي** عندما يتسبب الكائن الحي في تلف الأنسجة وفقدان وظيفة أنظمة الجسم."],
   en="Microbial colonization may result in:", ar="قد يؤدّي **الاستعمار الميكروبي** إلى:"),

 SEC("Purpose and Philosophy of Diagnostic Bacteriology", "هدف علم البكتيريا التشخيصي وفلسفته"),
 C("The purpose and philosophy of diagnostic bacteriology depend on identifying the causative microorganism by different laboratory methods, which is usually essential for effective antimicrobial and supportive therapy.",
   "يعتمد الهدف والفلسفة من **علم البكتيريا التشخيصي** على **تحديد الكائن المسبب للعدوى** باستخدام طرق مخبرية مختلفة، وهو أمر ضروري عادةً للعلاج الفعال بمضادات الميكروبات والعلاج الداعم."),
 L(["Through that initial treatment may be empiric, based on the microbiologic epidemiology of the infection and the patient’s symptoms."],
   ["وقد يكون **العلاج الأولي تجريبيًا**، استنادًا إلى علم الأوبئة الميكروبيولوجي للعدوى وأعراض المريض."]),
 L(["**Morphologic identification** of the agent in stains of specimens or sections of tissues (light and electron microscopy).",
    "**Cultivation and identification** of the organisms.",
    "**Detection of microbial antigens** by immunologic assay (latex agglutination, enzyme immunoassay [EIA]).",
    "**Detection of microbial DNA or RNA.**",
    "The source lists obtaining the proper specimens and informing the laboratory of the careful clinical diagnosis; the clinician should begin treatment with drugs aimed at the organism thought to be responsible for the patient’s illness."],
   ["**التعرّف الشكلي** على العامل في صبغات العيّنات أو مقاطع الأنسجة (المجهر الضوئي والإلكتروني).",
    "**الزرع والتشخيص** للكائنات.",
    "**الكشف عن المستضدات الميكروبية** بالفحص المناعي (التلازن بالّلاتكس، والفحص المناعي الإنزيمي `[EIA]`).",
    "**الكشف عن `DNA` أو `RNA` الميكروبي.**",
    "يذكر المصدر الحصول على العيّنات المناسبة وإبلاغ المختبر بالتشخيص السريري الدقيق؛ وعلى الطبيب أن يبدأ العلاج بأدوية موجّهة إلى الكائن الذي يُعتقد أنه المسؤول عن مرض المريض."],
   en="However, definitive microbiologic diagnosis of an infectious disease usually involves one or more of the following five basic laboratory techniques, which guide the physician along a narrowing path of possible causative pathogens:",
   ar="ومع ذلك، يتضمّن **التشخيص الميكروبيولوجي النهائي** للمرض المعدي عادةً واحدة أو أكثر من **التقنيات المختبرية الأساسية الخمس** الآتية، التي توجّه الطبيب في مسار يضيق تدريجيًا بين المُمرِضات المحتملة:"),

 SEC("Laboratory Feedback and Clinical Course", "التغذية الراجعة من المختبر والمسار السريري"),
 C("As the laboratory staff begins to obtain results, they inform health care providers, who can then reevaluate the diagnosis and clinical course of the patient and perhaps make changes in the therapeutic program.",
   "عندما يبدأ موظفو المختبر في الحصول على النتائج، فإنهم يبلغون مقدمي الرعاية الصحية، الذين يمكنهم بعد ذلك **إعادة تقييم التشخيص والمسار السريري** للمريض وربما إجراء تغييرات في البرنامج العلاجي."),
 C("This “feedback” information from the laboratory consists of earliest reports of the results of individual steps in the isolation and identification of the causative agent.",
   "وتتكون معلومات «**التغذية الراجعة**» من المختبر من أقدم التقارير عن نتائج الخطوات الفردية في عزل وتحديد العامل المسبب."),
 F("specimens-diagnosis.jpg", "Figure (1): Represent human specimens collection and diagnoses",
   "الشكل (1): يمثّل جمع العيّنات البشرية والتشخيص", h="150mm", fit="contain"),
 T(["Label", "الترجمة", "Label", "الترجمة"], [
   ["Symptomatic Patient: (localized or systemic)", "مريض ظاهر الأعراض (موضعي أو جهازي)", "Specimen collection", "جمع العيّنات"],
   ["Characteristic signs and symptoms", "العلامات والأعراض المميّزة", "Presumptive clinical diagnosis", "التشخيص السريري المبدئي"],
   ["Sputum", "القشع", "Urine", "الإدرار"],
   ["Blood", "الدم", "Serum", "المصل"],
   ["Swab", "المسحة", "Feces", "البراز"],
   ["Tissue biopsy", "خزعة نسيجية", "Anaerobic sample", "عيّنة لاهوائية"],
   ["Test selection by clinicians", "اختيار الفحص من قبل الأطباء", "Microscopic", "الفحص المجهري"],
   ["Quantitation", "التقدير الكمّي", "Culture", "الزرع"],
   ["Selective and nonselective media", "أوساط انتقائية وغير انتقائية", "Biochemical tests", "الفحوص الكيميائية الحيوية"],
   ["Serologic Tests", "الفحوص المصلية", "Agglutination, complement fixation, ELISA", "التلازن، وتثبيت المتمّم، و`ELISA`"],
   ["Genetic", "الفحوص الجينية", "Hybridization of DNA, RNA", "تهجين `DNA` و`RNA`"],
   ["Definitive diagnosis", "التشخيص النهائي", "Antimicrobial susceptibility testing (or known susceptibility)", "فحص الحساسية لمضادات الميكروبات (أو حساسية معروفة)"],
   ["Treatment", "العلاج", "Asymptomatic patient", "مريض بلا أعراض"],
 ], ar_cols=[1, 3], key_cols=[0, 2], widths=["24%", "26%", "24%", "26%"]),
]

# ---------------------------------------------------------------- questions (lecture content only)
LET = list("abcd") * 7
random.Random(3).shuffle(LET)
_n = [0]
def Q(en, ar, right, wrong, **k):
    """right = (en, ar); wrong = 3 x (en, ar); the right option goes to the next balanced letter."""
    ans = LET[_n[0]]; _n[0] += 1
    opts = list(wrong); opts.insert("abcd".index(ans), right)
    return dict(en=en, ar=ar, options=[list(o) for o in opts], answer=ans, **k)

mcq = [
 {"topic_en": "Manifestations and causes of infection", "topic_ar": "مظاهر العدوى وأسبابها"},
 Q("The clinical presentation of an infectious disease reflects the interaction between:", "يعكس العرض السريري للمرض المعدي التفاعل بين:",
   ("The host and the microorganism", "المضيف والكائن الحي الدقيق"),
   [("The laboratory and the physician", "المختبر والطبيب"), ("Two antibiotics", "مضادّين حيويين"), ("The specimen and the culture medium", "العيّنة والوسط الزرعي")]),
 Q("The host–microorganism interaction is affected by:", "يتأثر تفاعل المضيف مع الكائن الدقيق بـ:",
   ("Host immune status and microbial virulence factors", "الحالة المناعية للمضيف وعوامل الفوعة الميكروبية"),
   [("Specimen transport only", "نقل العيّنة فقط"), ("Type of culture media", "نوع الأوساط الزرعية"), ("Laboratory feedback", "التغذية الراجعة من المختبر")]),
 Q("Signs and symptoms of infection vary according to:", "تختلف علامات العدوى وأعراضها وفقًا لـ:",
   ("The site and severity of infection", "موقع العدوى وشدتها"),
   [("The colour of the specimen", "لون العيّنة"), ("The laboratory staff", "موظفي المختبر"), ("The biochemical tests used", "الفحوص الكيميائية الحيوية المستعملة")]),
 Q("Diagnosis of infection requires a composite of information including all EXCEPT:", "يتطلب تشخيص العدوى مجموعة معلومات تشمل كل ما يأتي عدا:",
   ("Blood group of the physician", "فصيلة دم الطبيب"),
   [("History", "التاريخ"), ("Physical examination", "الفحص البدني"), ("Radiographic findings and laboratory data", "النتائج الإشعاعية والبيانات المختبرية")]),
 Q("An exogenous pathogen is acquired from:", "العامل الممرض الخارجي يُكتسب من:",
   ("Environmental or animal sources or from other persons", "مصادر بيئية أو حيوانية أو من أشخاص آخرين"),
   [("The normal flora", "النبيت الطبيعي"), ("Antibiotic resistance genes", "جينات مقاومة المضادات الحيوية"), ("Selective media", "الأوساط الانتقائية")]),
 Q("An endogenous pathogen comes from:", "العامل الممرض الداخلي يأتي من:",
   ("The normal flora", "النبيت الطبيعي"),
   [("Animal sources", "مصادر حيوانية"), ("Other persons", "أشخاص آخرين"), ("The environment", "البيئة")]),

 {"topic_en": "Diagnostic microbiology and its methods", "topic_ar": "الأحياء المجهرية التشخيصية وطرقها"},
 Q("Diagnostic microbiology is the tool that makes it possible to identify:", "الأحياء المجهرية التشخيصية هي الأداة التي تمكّن من تحديد:",
   ("The exact pathogens and the most optimal therapy at the level of individual patients", "مسببات الأمراض الدقيقة والعلاج الأمثل على مستوى المرضى الأفراد"),
   [("The blood group of patients", "فصيلة دم المرضى"), ("Only the epidemiology of infections", "علم أوبئة العدوى فقط"),
    ("The radiographic findings only", "النتائج الإشعاعية فقط")]),
 Q("Conventional methods are lengthy because they need:", "الطرق التقليدية طويلة لأنها تحتاج إلى:",
   ("Time to grow microbes in vitro followed by biochemical identification", "وقت لزراعة الميكروبات في المختبر ثم التشخيص الكيميائي الحيوي"),
   [("Amplification of nucleic acids", "تضخيم الأحماض النووية"), ("Use of probes only", "استعمال المجسّات فقط"), ("Detection of resistance genes", "الكشف عن جينات المقاومة")]),
 Q("Which factor renders culture-based methods less reliable?", "أيّ عامل يجعل الطرق القائمة على الزرع أقل موثوقية؟",
   ("Prior use of antibiotics", "الاستخدام السابق للمضادات الحيوية"),
   [("Large number of organisms", "العدد الكبير من الكائنات"), ("Ideal transport conditions", "ظروف النقل المثالية"), ("Use of probes", "استعمال المجسّات")]),
 Q("Newer methods depend on:", "تعتمد الطرق الأحدث على:",
   ("Amplification of nucleic acids followed by use of probes", "تضخيم الأحماض النووية ثم استعمال المجسّات"),
   [("Growing microbes in vitro for days", "زراعة الميكروبات في المختبر لأيام"), ("Biochemical tests only", "الفحوص الكيميائية الحيوية فقط"),
    ("Gram stain only", "صبغة غرام فقط")]),
 Q("An advantage of newer methods is that they:", "من مزايا الطرق الأحدث أنها:",
   ("Shorten the time", "تقصّر الوقت"),
   [("Need a higher microbial load", "تحتاج حملًا ميكروبيًا أعلى"), ("Need metabolically active viable organisms", "تحتاج كائنات حية نشطة الأيض"),
    ("Fulfill all the diagnostic needs", "تلبي كل الاحتياجات التشخيصية")]),
 Q("Newer methods can detect directly from the specimen:", "يمكن للطرق الأحدث أن تكشف مباشرة من العيّنة:",
   ("Antibiotic resistance genes", "جينات مقاومة المضادات الحيوية"),
   [("The patient’s symptoms", "أعراض المريض"), ("The site of infection", "موقع العدوى"), ("Radiographic findings", "النتائج الإشعاعية")]),
 Q("Since newer methods will not fulfill all diagnostic needs, a second approach is used to:", "لأن الطرق الأحدث لا تلبي كل الاحتياجات التشخيصية، يُستعمل نهج ثانٍ لـ:",
   ("Shorten the time to identification after the organism has already grown", "تقصير وقت التشخيص بعد نمو الكائن الحي"),
   [("Avoid specimen collection", "تجنّب جمع العيّنات"), ("Replace treatment", "الاستغناء عن العلاج"), ("Increase the microbial load", "زيادة الحمل الميكروبي")]),

 {"topic_en": "Microbial colonization", "topic_ar": "الاستعمار الميكروبي"},
 Q("Microbial colonization may result in all of the following EXCEPT:", "قد يؤدّي الاستعمار الميكروبي إلى كل ما يأتي عدا:",
   ("Detection of microbial DNA", "الكشف عن `DNA` الميكروبي"),
   [("Elimination of the microorganism without affecting the host", "القضاء على الكائن دون التأثير على المضيف"),
    ("Infection", "العدوى"), ("A transient or prolonged carrier state", "حالة حاملة عابرة أو طويلة")]),
 Q("Infection is the state in which the organisms:", "العدوى هي الحالة التي فيها الكائنات:",
   ("Multiply and cause the host to make an immune or other type of response", "تتكاثر وتجعل المضيف يُحدث استجابة مناعية أو غيرها"),
   [("Are eliminated without affecting the host", "تُزال دون التأثير على المضيف"), ("Never multiply", "لا تتكاثر أبدًا"),
    ("Live only in culture media", "تعيش في الأوساط الزرعية فقط")]),
 Q("Infectious disease occurs when the organism causes:", "يحدث المرض المعدي عندما يسبّب الكائن:",
   ("Tissue damage and loss of function of body systems", "تلف الأنسجة وفقدان وظيفة أنظمة الجسم"),
   [("No response in the host", "لا استجابة في المضيف"), ("A transient carrier state only", "حالة حاملة عابرة فقط"), ("Elimination of itself", "القضاء على نفسه")]),

 {"topic_en": "Purpose and philosophy of diagnostic bacteriology", "topic_ar": "هدف علم البكتيريا التشخيصي وفلسفته"},
 Q("The purpose and philosophy of diagnostic bacteriology depend on:", "يعتمد هدف علم البكتيريا التشخيصي وفلسفته على:",
   ("Identifying the causative microorganism by different laboratory methods", "تحديد الكائن المسبّب بطرق مختبرية مختلفة"),
   [("Radiographic findings only", "النتائج الإشعاعية فقط"), ("Empiric treatment only", "العلاج التجريبي فقط"), ("The patient’s history only", "تاريخ المريض فقط")]),
 Q("Initial treatment may be empiric, based on:", "قد يكون العلاج الأولي تجريبيًا استنادًا إلى:",
   ("The microbiologic epidemiology of the infection and the patient’s symptoms", "علم الأوبئة الميكروبيولوجي للعدوى وأعراض المريض"),
   [("Antimicrobial susceptibility testing", "فحص الحساسية لمضادات الميكروبات"), ("The definitive diagnosis", "التشخيص النهائي"),
    ("Hybridization of DNA", "تهجين `DNA`")]),
 Q("Definitive microbiologic diagnosis usually involves how many basic laboratory techniques?", "يتضمّن التشخيص الميكروبيولوجي النهائي عادةً كم تقنية مختبرية أساسية؟",
   ("Five", "خمس"), [("Two", "اثنتين"), ("Three", "ثلاث"), ("Seven", "سبع")]),
 Q("Morphologic identification of the agent is done in stains of specimens or sections of tissues using:", "يتمّ التعرّف الشكلي على العامل في صبغات العيّنات أو مقاطع الأنسجة باستعمال:",
   ("Light and electron microscopy", "المجهر الضوئي والإلكتروني"),
   [("Latex agglutination", "التلازن باللاتكس"), ("Biochemical tests", "الفحوص الكيميائية الحيوية"), ("Probes", "المجسّات")]),
 Q("Detection of microbial antigens is done by immunologic assay such as:", "يتمّ الكشف عن المستضدات الميكروبية بالفحص المناعي مثل:",
   ("Latex agglutination and enzyme immunoassay (EIA)", "التلازن باللاتكس والفحص المناعي الإنزيمي (`EIA`)"),
   [("Electron microscopy", "المجهر الإلكتروني"), ("Culture on selective media", "الزرع على أوساط انتقائية"), ("Radiography", "التصوير الشعاعي")]),
 Q("Which of the following is one of the basic laboratory techniques of definitive diagnosis?", "أيّ ممّا يأتي من التقنيات المختبرية الأساسية للتشخيص النهائي؟",
   ("Detection of microbial DNA or RNA", "الكشف عن `DNA` أو `RNA` الميكروبي"),
   [("Physical examination", "الفحص البدني"), ("Patient history", "تاريخ المريض"), ("Empiric therapy", "العلاج التجريبي")]),

 {"topic_en": "Laboratory feedback and Figure (1)", "topic_ar": "التغذية الراجعة من المختبر والشكل (1)"},
 Q("As the laboratory staff obtain results, they inform:", "عندما يحصل موظفو المختبر على النتائج يبلغون:",
   ("Health care providers", "مقدمي الرعاية الصحية"),
   [("The patient’s family only", "عائلة المريض فقط"), ("The pharmacy only", "الصيدلية فقط"), ("No one until the final report", "لا أحد حتى التقرير النهائي")]),
 Q("Laboratory “feedback” information consists of:", "تتكوّن معلومات «التغذية الراجعة» من المختبر من:",
   ("Earliest reports of the results of individual steps in isolation and identification", "أقدم التقارير عن نتائج الخطوات الفردية في العزل والتشخيص"),
   [("The final report only", "التقرير النهائي فقط"), ("The patient’s symptoms", "أعراض المريض"), ("Radiographic findings", "النتائج الإشعاعية")]),
 Q("In Figure (1), the specimen obtained from blood for serologic tests is:", "في الشكل (1)، العيّنة المأخوذة من الدم للفحوص المصلية هي:",
   ("Serum", "المصل"), [("Sputum", "القشع"), ("Swab", "المسحة"), ("Feces", "البراز")]),
 Q("In Figure (1), characteristic signs and symptoms lead to:", "في الشكل (1)، تؤدّي العلامات والأعراض المميّزة إلى:",
   ("Presumptive clinical diagnosis", "التشخيص السريري المبدئي"),
   [("Definitive diagnosis", "التشخيص النهائي"), ("Treatment directly", "العلاج مباشرة"), ("Quantitation", "التقدير الكمّي")]),

 {"topic_en": "Picture questions", "topic_ar": "أسئلة الصور"},
 Q("In this part of Figure (1), the hidden test category that ends in hybridization of DNA, RNA is:", "في هذا الجزء من الشكل (1)، فئة الفحص المخفيّة التي تنتهي بتهجين `DNA` و`RNA` هي:",
   ("Genetic", "الفحوص الجينية"),
   [("Serologic Tests", "الفحوص المصلية"), ("Culture", "الزرع"), ("Microscopic", "الفحص المجهري")],
   img="assets/q-genetic.jpg", img_h="40mm"),
 Q("In this part of Figure (1), the hidden step that comes before antimicrobial susceptibility testing is:", "في هذا الجزء من الشكل (1)، الخطوة المخفيّة التي تسبق فحص الحساسية لمضادات الميكروبات هي:",
   ("Definitive diagnosis", "التشخيص النهائي"),
   [("Presumptive clinical diagnosis", "التشخيص السريري المبدئي"), ("Specimen collection", "جمع العيّنات"), ("Treatment", "العلاج")],
   img="assets/q-definitive.jpg", img_h="40mm"),
]

tf = [
 TF("The clinical presentation of an infectious disease reflects the interaction between the host and the microorganism.", "يعكس العرض السريري للمرض المعدي التفاعل بين المضيف والكائن الدقيق.", "T"),
 TF("Signs and symptoms are the same whatever the site and severity of infection.", "العلامات والأعراض نفسها مهما كان موقع العدوى وشدتها.", "F"),
 TF("Infections may be caused by bacteria, viruses, fungi, and parasites.", "قد تحدث العدوى بسبب البكتيريا والفيروسات والفطريات والطفيليات.", "T"),
 TF("An endogenous pathogen is acquired from other persons.", "العامل الممرض الداخلي يُكتسب من أشخاص آخرين.", "F"),
 TF("All microbes can easily be cultured.", "يمكن زراعة جميع الميكروبات بسهولة.", "F"),
 TF("Small number of organisms renders culture-based methods less reliable.", "العدد القليل من الكائنات يجعل الطرق القائمة على الزرع أقل موثوقية.", "T"),
 TF("Newer methods need a higher microbial load.", "تحتاج الطرق الأحدث إلى حمل ميكروبي أعلى.", "F"),
 TF("Newer methods can detect antibiotic resistance genes directly from the specimen.", "يمكن للطرق الأحدث الكشف عن جينات مقاومة المضادات الحيوية مباشرة من العيّنة.", "T"),
 TF("Newer methods fulfill all the diagnostic needs.", "تلبي الطرق الأحدث كل الاحتياجات التشخيصية.", "F"),
 TF("Infectious disease occurs when the organism causes tissue damage and loss of function of body systems.", "يحدث المرض المعدي عندما يسبّب الكائن تلف الأنسجة وفقدان وظيفة أنظمة الجسم.", "T"),
 TF("Initial treatment may be empiric.", "قد يكون العلاج الأولي تجريبيًا.", "T"),
 TF("Definitive microbiologic diagnosis involves only one laboratory technique.", "يتضمّن التشخيص الميكروبيولوجي النهائي تقنية مختبرية واحدة فقط.", "F"),
 TF("Laboratory feedback may lead to changes in the therapeutic program.", "قد تؤدّي التغذية الراجعة من المختبر إلى تغييرات في البرنامج العلاجي.", "T"),
 TF("In Figure (1), ELISA is listed under culture.", "في الشكل (1)، ذُكر `ELISA` تحت الزرع.", "F"),
]

traps = [
 TR("Exogenous and endogenous pathogens: which one comes from the normal flora?", "العامل الممرض الخارجي والداخلي: أيّهما يأتي من النبيت الطبيعي؟",
    "Endogenous — from the normal flora. Exogenous is acquired from environmental or animal sources or from other persons.",
    "الداخلي — من النبيت الطبيعي. أمّا الخارجي فيُكتسب من مصادر بيئية أو حيوانية أو من أشخاص آخرين."),
 TR("Newer methods need metabolically active viable organisms.", "تحتاج الطرق الأحدث إلى كائنات حية نشطة الأيض.",
    "No — they mitigate the need for higher microbial load and for metabolically active viable organisms, and shorten the time.",
    "لا — فهي تخفّف الحاجة إلى حمل ميكروبي أعلى وإلى كائنات حية نشطة الأيض، وتقصّر الوقت."),
 TR("Every microbial colonization ends in infectious disease.", "كل استعمار ميكروبي ينتهي بمرض معدٍ.",
    "No — it may end in elimination without affecting the host, infection, or a transient or prolonged carrier state; disease occurs only when the organism causes tissue damage and loss of function.",
    "لا — قد ينتهي بالقضاء على الكائن دون التأثير على المضيف، أو بالعدوى، أو بحالة حاملة عابرة أو طويلة؛ والمرض يحدث فقط عندما يسبّب الكائن تلف الأنسجة وفقدان الوظيفة."),
 TR("Empiric treatment is based on laboratory results.", "العلاج التجريبي مبنيّ على نتائج المختبر.",
    "No — it is based on the microbiologic epidemiology of the infection and the patient’s symptoms.",
    "لا — مبنيّ على علم الأوبئة الميكروبيولوجي للعدوى وأعراض المريض."),
 TR("Latex agglutination is a morphologic identification method.", "التلازن باللاتكس طريقة تعرّف شكلي.",
    "No — it is an immunologic assay for detection of microbial antigens; morphologic identification uses light and electron microscopy.",
    "لا — هو فحص مناعي للكشف عن المستضدات الميكروبية؛ أمّا التعرّف الشكلي فيستعمل المجهر الضوئي والإلكتروني."),
 TR("Presumptive and definitive diagnosis are the same step in Figure (1).", "التشخيص المبدئي والنهائي خطوة واحدة في الشكل (1).",
    "No — presumptive clinical diagnosis comes from characteristic signs and symptoms; definitive diagnosis comes after the laboratory tests.",
    "لا — التشخيص السريري المبدئي يأتي من العلامات والأعراض المميّزة، والتشخيص النهائي يأتي بعد الفحوص المختبرية."),
 TR("Feedback information is the final laboratory report only.", "معلومات التغذية الراجعة هي التقرير النهائي للمختبر فقط.",
    "No — it consists of earliest reports of the results of individual steps in the isolation and identification of the causative agent.",
    "لا — تتكوّن من أقدم التقارير عن نتائج الخطوات الفردية في عزل العامل المسبّب وتحديده."),
]

important = [
 IM("What does the clinical presentation of an infectious disease reflect, and what affects it?", "علامَ يدلّ العرض السريري للمرض المعدي، وما الذي يؤثّر فيه؟",
    "It reflects the interaction between the host and the microorganism; this interaction is affected by the host immune status and microbial virulence factors. Signs and symptoms vary according to the site and severity of infection.",
    "يعكس التفاعل بين المضيف والكائن الدقيق، ويتأثر هذا التفاعل بالحالة المناعية للمضيف وعوامل الفوعة الميكروبية. وتختلف العلامات والأعراض حسب موقع العدوى وشدتها."),
 IM("Define diagnostic microbiology.", "عرّف الأحياء المجهرية التشخيصية.",
    "It is the tool that makes it possible to identify the exact pathogens of infectious diseases and the most optimal therapy at the level of individual patients.",
    "هي الأداة التي تمكّن من تحديد مسببات الأمراض الدقيقة للأمراض المعدية والعلاج الأمثل على مستوى المرضى الأفراد."),
 IM("Why are conventional methods lengthy and less reliable?", "لماذا تكون الطرق التقليدية طويلة وأقل موثوقية؟",
    "They require time to grow microbes in vitro under specific conditions (not all microbes can be cultured), followed by biochemical identification. Transport under less than ideal conditions, prior use of antibiotics and small number of organisms make them less reliable.",
    "لأنها تتطلب وقتًا لزراعة الميكروبات في المختبر في ظروف محددة (ولا يمكن زراعة كل الميكروبات)، ثم التشخيص الكيميائي الحيوي. والنقل في ظروف غير مثالية، والاستخدام السابق للمضادات الحيوية، وقلّة عدد الكائنات تجعلها أقل موثوقية."),
 IM("What do newer methods depend on, and what are their advantages?", "على ماذا تعتمد الطرق الأحدث، وما مزاياها؟",
    "Amplification of nucleic acids followed by probes. They mitigate the need for higher microbial load and viable organisms, shorten the time, and detect antibiotic resistance genes directly from the specimen.",
    "على تضخيم الأحماض النووية ثم المجسّات. وتخفّف الحاجة إلى حمل ميكروبي أعلى وكائنات حية، وتقصّر الوقت، وتكشف عن جينات مقاومة المضادات الحيوية مباشرة من العيّنة."),
 IM("What may microbial colonization result in?", "إلامَ قد يؤدّي الاستعمار الميكروبي؟",
    "1. Elimination of the microorganism without affecting the host. 2. Infection. 3. A transient or prolonged carrier state.",
    "1. القضاء على الكائن الدقيق دون التأثير على المضيف. 2. العدوى. 3. حالة حاملة عابرة أو طويلة."),
 IM("List the five basic laboratory techniques of definitive microbiologic diagnosis.", "عدّد التقنيات المختبرية الأساسية الخمس للتشخيص الميكروبيولوجي النهائي.",
    "1. Morphologic identification (light and electron microscopy). 2. Cultivation and identification. 3. Detection of microbial antigens (latex agglutination, EIA). 4. Detection of microbial DNA or RNA. 5. Obtaining the proper specimens and informing the laboratory of the careful clinical diagnosis.",
    "1. التعرّف الشكلي (المجهر الضوئي والإلكتروني). 2. الزرع والتشخيص. 3. الكشف عن المستضدات الميكروبية (التلازن باللاتكس، `EIA`). 4. الكشف عن `DNA` أو `RNA` الميكروبي. 5. الحصول على العيّنات المناسبة وإبلاغ المختبر بالتشخيص السريري الدقيق."),
 IM("What is laboratory “feedback” information and why is it important?", "ما معلومات «التغذية الراجعة» من المختبر ولماذا هي مهمة؟",
    "Earliest reports of the results of individual steps in isolation and identification of the causative agent; health care providers use them to reevaluate the diagnosis and clinical course and perhaps change the therapeutic program.",
    "هي أقدم التقارير عن نتائج الخطوات الفردية في عزل العامل المسبّب وتحديده؛ ويستعملها مقدمو الرعاية الصحية لإعادة تقييم التشخيص والمسار السريري وربما تغيير البرنامج العلاجي."),
]

meta = dict(subject_en="Diagnostic Microbiology", subject_ar="الأحياء المجهرية التشخيصية", short_ar="بكتريا",
            unit_en="Lecture 1", unit_ar="المحاضرة 1", unit_label="LEC", unit_no="1",
            title_en="Purpose and Philosophy — Manifestations of Infection", title_ar="الهدف والفلسفة ومظاهر العدوى",
            kind="Theory — نظري", stage="The fourth stage — الرابعة", instructor="د. عدنان",
            file_name="بكتريا نظري المحاضرة الاولى", questions_suffix=" اسئلة")   # user-chosen file names

folder = "microbiology-lec1-purpose-philosophy"
qs = [q for q in mcq if "answer" in q]
print(folder, len(qs), dict(Counter(q["answer"] for q in qs)), len(tf),
      dict(Counter(t["answer"] for t in tf)), len(traps), len(important))
d = os.path.dirname(os.path.abspath(__file__))
json.dump({"meta": meta, "blocks": blocks,
           "questions": {"mcq": mcq, "tf": tf, "traps": traps, "important": important}},
          open(os.path.join(d, "lecture.json"), "w"), ensure_ascii=False, indent=1)
