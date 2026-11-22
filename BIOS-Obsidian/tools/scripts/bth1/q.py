import sys, json, os
from collections import Counter
WORK = "/home/claude/scratch/work"
sys.path.insert(0, WORK + "/bac"); from bal import balance
sys.path.insert(0, WORK); from bidi import ltr_all

# Diagnostic Microbiology — THEORY Lecture 1 (stage 4, د. عدنان as in lec6/7-9/11): Diagnostic microbiology — purpose and
# philosophy. Source 2026-11-22: phone scan (7 pages, iOS, no text layer) of the department's bilingual handout, annotated
# in class: «سؤال قصير» (short answer), «MCQ», «مهم», «فهم» (understand), «تجربة فهم/ال أثر»; paragraphs crossed ✗ = deleted
# → NOT asked (mitigates microbial load; second approach after growth; empiric treatment; the five-techniques intro sentence;
# "after obtaining specimens"; "as the laboratory staff…"; Figure 1). The five techniques themselves are marked
# «الـ5 نقاط حفظ مختصر» → asked. Pretest/Posttest kept as SA; the handwritten posttest answer lists different five
# techniques (microscopy, culture, staining, biochemical, AST) → BIOS note.
# User: "هسه نبدي نظري اريد شي شامل للماده كلش" → «شامل» bank = MCQ (answers_inline) + SA (important).

def Q(en, ar, opts, why_en, why_ar, fixed=None):
    d = dict(en=en, ar=ar, options=[list(o) for o in opts], note_en=why_en, note_ar=why_ar)
    if fixed: d["_fixed"] = fixed
    else: d["answer"] = "a"
    return d
def T(en, ar): return {"topic_en": en, "topic_ar": ar}
def IM(en, ar, ae, aa): return dict(en=en, ar=ar, answer_en=ae, answer_ar=aa)
ALL = ("All of the above", "جميع ما سبق")
AB = ("Both A and B", "كلاهما أ و ب")

mcq = [
 T("Manifestations of infection", "مظاهر العدوى"),
 Q("The clinical presentation of an infectious disease reflects:", "يعكس العرض السريري للمرض المعدي:",
   [("The interaction between the host and the microorganism", "التفاعل بين المضيف والكائن الحي الدقيق"), ("The microorganism alone", "الكائن الدقيق وحده"),
    ("The host alone", "المضيف وحده"), ("The type of culture medium", "نوع الوسط الزرعي")],
   "Marked «سؤال قصير أو MCQ».", "مؤشَّر «سؤال قصير أو MCQ»."),
 Q("The interaction between the host and the microorganism is affected by:", "يتأثّر التفاعل بين المضيف والكائن الدقيق بـ:",
   [("The host immune status", "الحالة المناعية للمضيف"), ("Microbial virulence factors", "عوامل الضراوة الميكروبية"), AB, ("The patient's age only", "عمر المريض فقط")],
   "Two factors (numbered ① ② in class); also a 2023 exam question.", "عاملان (مرقّمان ① ② بالمحاضرة)؛ وهو أيضًا من أسئلة امتحان 2023.", fixed="c"),
 Q("Signs and symptoms of infection vary according to:", "تختلف علامات العدوى وأعراضها حسب:",
   [("The site and severity of infection", "موقع الإصابة وشدّتها"), ("The colour of the specimen", "لون العيّنة"),
    ("The laboratory method", "الطريقة المختبرية"), ("The time of day", "وقت اليوم")],
   "Marked MCQ.", "مؤشَّر MCQ."),
 Q("Diagnosis of infection requires a composite of information, including:", "يتطلّب تشخيص العدوى مجموعة من المعلومات، منها:",
   [("History and physical examination", "التاريخ المرضي والفحص البدني"), ("Radiographic findings", "نتائج التصوير الشعاعي"), ("Laboratory data", "البيانات المختبرية"), ALL],
   "Four sources of information (marked «فهم»).", "أربعة مصادر للمعلومات (مؤشَّرة «فهم»).", fixed="d"),

 T("Microbial causes of infection", "الأسباب الميكروبية للعدوى"),
 Q("Infections may be caused by:", "قد تُسبَّب العدوى بـ:",
   [("Bacteria, viruses, fungi and parasites", "البكتيريا والفيروسات والفطريات والطفيليات"), ("Bacteria only", "البكتيريا فقط"),
    ("Bacteria and viruses only", "البكتيريا والفيروسات فقط"), ("Fungi and parasites only", "الفطريات والطفيليات فقط")],
   "Four causes (numbered ①–④ in class).", "أربعة مسبّبات (مرقّمة ①–④ بالمحاضرة)."),
 Q("An exogenous pathogen is acquired from:", "العامل الممرض الخارجي (exogenous) يُكتسب من:",
   [("Environmental or animal sources or from other persons", "مصادر بيئية أو حيوانية أو من أشخاص آخرين"), ("The normal flora", "الفلورا الطبيعية"),
    ("The patient's own blood", "دم المريض نفسه"), ("Culture media", "الأوساط الزرعية")],
   "Marked «مهم MCQ».", "مؤشَّر «مهم MCQ»."),
 Q("An endogenous pathogen comes from:", "العامل الممرض الداخلي (endogenous) يأتي من:",
   [("The normal flora", "الفلورا الطبيعية"), ("Animal sources", "المصادر الحيوانية"), ("Other persons", "أشخاص آخرين"), ("The environment", "البيئة")],
   "Endogenous = from the normal flora.", "الداخلي = من الفلورا الطبيعية."),
 Q("A pathogen acquired from another person is described as:", "العامل الممرض المكتسب من شخص آخر يوصف بأنه:",
   [("Exogenous", "خارجي (exogenous)"), ("Endogenous", "داخلي (endogenous)"), ("Commensal", "متعايش"), ("Normal flora", "فلورا طبيعية")],
   "Other persons → exogenous.", "أشخاص آخرون ← خارجي."),

 T("Diagnostic microbiology — the tool", "علم الأحياء الدقيقة التشخيصي — الأداة"),
 Q("The tool that makes it possible to identify the exact pathogens of infectious diseases and the most optimal therapy at the level of individual patients is:",
   "الأداة التي تتيح التعرّف الدقيق على مسبّبات الأمراض المعدية والعلاج الأمثل على مستوى المرضى الأفراد هي:",
   [("Diagnostic microbiology", "علم الأحياء الدقيقة التشخيصي"), ("Virology", "علم الفيروسات"), ("Epidemiology", "علم الوبائيات"), ("Immunology", "علم المناعة")],
   "Boxed and starred in class; the same question came in the 2024 file.", "مؤطَّر ومنجَّم بالمحاضرة؛ والسؤال نفسه ورد في ملف 2024."),
 Q("Diagnostic microbiology identifies the most optimal therapy at the level of:", "يحدّد علم الأحياء الدقيقة التشخيصي العلاج الأمثل على مستوى:",
   [("Individual patients", "المرضى الأفراد"), ("The whole population", "السكان كلهم"), ("The hospital only", "المستشفى فقط"), ("The laboratory staff", "كادر المختبر")],
   "“…at the level of individual patients”.", "«…على مستوى المرضى الأفراد»."),

 T("Conventional and newer methods", "الطرق التقليدية والحديثة"),
 Q("Conventional methods require:", "تتطلّب الطرق التقليدية:",
   [("Time to grow the microbes in vitro under specific conditions", "وقتًا لإنماء الميكروبات في المختبر تحت ظروف محدّدة"), ("Amplification of nucleic acids", "تضخيم الأحماض النووية"),
    ("Probes for identification only", "مسابير للتعرّف فقط"), ("No culture at all", "عدم الزرع إطلاقًا")],
   "Starred; marked «سؤال قصير».", "منجَّم؛ مؤشَّر «سؤال قصير»."),
 Q("A limitation of conventional methods is that:", "من عيوب الطرق التقليدية أن:",
   [("Not all microbes can easily be cultured", "ليس كل الميكروبات تُزرع بسهولة"), ("They need no time", "لا تحتاج وقتًا"),
    ("They detect resistance genes directly", "تكشف جينات المقاومة مباشرة"), ("They do not need specific conditions", "لا تحتاج ظروفًا محدّدة")],
   "Slide text.", "نصّ المحاضرة."),
 Q("In conventional methods, culture is followed by biochemical methods for identification, which:", "في الطرق التقليدية يتبع الزرعَ طرقٌ كيميائية حيوية للتعرّف:",
   [("Further makes the process lengthy", "تجعل العملية أطول"), ("Shortens the process", "تختصر العملية"),
    ("Replaces culture", "تغني عن الزرع"), ("Needs no incubation", "لا تحتاج حضنًا")],
   "Marked «سؤال قصير».", "مؤشَّر «سؤال قصير»."),
 Q("Which of the following factors render culture-based methods less reliable?", "أيّ العوامل الآتية تجعل الطرق القائمة على الزرع أقل موثوقية؟",
   [("Transport of the specimens under less than ideal conditions", "نقل العيّنات في ظروف أقل من المثالية"), ("Prior use of antibiotics", "الاستعمال المسبق للمضادات الحيوية"),
    ("Small number of organisms", "قلّة عدد الكائنات"), ALL],
   "Three factors (marked «تجربة فهم»); a 2024-file question.", "ثلاثة عوامل (مؤشَّرة «فهم»)؛ ومن أسئلة ملف 2024.", fixed="d"),
 Q("Newer methods depend on:", "تعتمد الطرق الأحدث على:",
   [("Amplification of nucleic acids followed by use of probes for identification", "تضخيم الأحماض النووية متبوعًا باستعمال المسابير للتعرّف"),
    ("Growing microbes in vitro for days", "إنماء الميكروبات في المختبر لأيام"), ("Biochemical tests only", "الاختبارات الكيميائية الحيوية فقط"), ("Staining only", "التصبيغ فقط")],
   "“Amplification of nucleic acids” is boxed «سؤال قصير».", "«تضخيم الأحماض النووية» مؤطَّر «سؤال قصير»."),
 Q("Newer (molecular) methods can be used to:", "يمكن استعمال الطرق الأحدث (الجزيئية) لـ:",
   [("Detect antibiotic resistance genes directly from the specimen", "الكشف عن جينات مقاومة المضادات الحيوية مباشرة من العيّنة"),
    ("Grow the organism faster", "إنماء الكائن أسرع"), ("Stain the bacteria", "تصبيغ البكتيريا"), ("Replace the request form", "الاستغناء عن نموذج الطلب")],
   "Marked «سؤال قصير أو MCQ».", "مؤشَّر «سؤال قصير أو MCQ»."),
 Q("Detecting antibiotic resistance genes directly from the specimen helps to:", "الكشف عن جينات المقاومة مباشرة من العيّنة يساعد على:",
   [("Direct targeted therapy with efficacy", "توجيه العلاج المستهدف بفعالية"), ("Delay treatment", "تأخير العلاج"),
    ("Increase the microbial load", "زيادة الحمل الميكروبي"), ("Avoid laboratory tests", "تجنّب الفحوص المختبرية")],
   "Second half of the same sentence.", "النصف الثاني من الجملة نفسها."),

 T("Microbial colonization", "الاستعمار الميكروبي"),
 Q("Microbial colonization may result in:", "قد يؤدّي الاستعمار الميكروبي إلى:",
   [("Elimination of the microorganism without affecting the host", "التخلّص من الكائن الدقيق دون التأثير في المضيف"),
    ("Infection in which the organisms multiply and cause the host to react", "عدوى تتكاثر فيها الكائنات وتجعل المضيف يستجيب"),
    ("A transient or prolonged carrier state", "حالة حمل عابرة أو مطوّلة"), ALL],
   "Three outcomes (starred, «تجربة فهم»); a 2024-file question.", "ثلاث نتائج (منجَّمة، «فهم»)؛ ومن أسئلة ملف 2024.", fixed="d"),
 Q("In the infection outcome of colonization, the organisms multiply and the host reacts by making:", "في نتيجة العدوى من الاستعمار تتكاثر الكائنات ويستجيب المضيف بـ:",
   [("An immune or other type of response", "استجابة مناعية أو نوع آخر من الاستجابة"), ("No response", "لا استجابة"),
    ("Only fever", "الحمّى فقط"), ("Antibiotics", "مضادات حيوية")],
   "Outcome 2.", "النتيجة 2."),
 Q("Elimination of the microorganism after colonization occurs:", "التخلّص من الكائن الدقيق بعد الاستعمار يحدث:",
   [("Without affecting the host", "دون التأثير في المضيف"), ("With tissue damage", "مع تلف الأنسجة"),
    ("With loss of function of body systems", "مع فقدان وظائف أجهزة الجسم"), ("Only after antibiotic therapy", "بعد العلاج بالمضادات فقط")],
   "Outcome 1.", "النتيجة 1."),
 Q("Infectious disease occurs when the organism causes:", "يحدث المرض المعدي عندما يسبّب الكائن:",
   [("Tissue damage", "تلف الأنسجة"), ("Loss of function of body systems", "فقدان وظائف أجهزة الجسم"), AB, ("A carrier state only", "حالة حمل فقط")],
   "Both are highlighted (marked MCQ); asked in the 2023 exams.", "كلاهما مظلَّل (مؤشَّر MCQ)؛ وسُئل في امتحانات 2023.", fixed="c"),
 Q("Which outcome of colonization means the person carries the organism for a short or long time?", "أيّ نتائج الاستعمار تعني أن الشخص يحمل الكائن مدة قصيرة أو طويلة؟",
   [("A transient or prolonged carrier state", "حالة الحمل العابرة أو المطوّلة"), ("Elimination", "التخلّص"), ("Infection", "العدوى"), ("Sterilization", "التعقيم")],
   "Outcome 3.", "النتيجة 3."),

 T("Purpose and philosophy of diagnostic bacteriology", "غرض وفلسفة علم الجراثيم التشخيصي"),
 Q("The purpose and the philosophy of diagnostic bacteriology depend on:", "يعتمد غرض وفلسفة علم الجراثيم التشخيصي على:",
   [("Identifying the causative microorganism by different laboratory methods", "تحديد الكائن المسبّب بطرق مختبرية مختلفة"),
    ("Identifying the causative microorganism by the same laboratory method", "تحديد الكائن المسبّب بالطريقة المختبرية نفسها"),
    ("Treating the patient without tests", "علاج المريض دون فحوص"), ("Culturing normal flora", "زرع الفلورا الطبيعية")],
   "Marked MCQ; the same question in the 2023 exam (“different”, not “same”).", "مؤشَّر MCQ؛ والسؤال نفسه في امتحان 2023 («مختلفة» لا «نفسها»)."),
 Q("Identifying the causative microorganism is usually essential for:", "تحديد الكائن المسبّب ضروري عادةً لـ:",
   [("Effective antimicrobial and supportive therapy", "العلاج الفعّال بمضادات الميكروبات والعلاج الداعم"), ("Making the patient a carrier", "جعل المريض حاملًا"),
    ("Increasing the microbial load", "زيادة الحمل الميكروبي"), ("Avoiding diagnosis", "تجنّب التشخيص")],
   "The arrow (MCQ) points to “effective antimicrobial…”.", "السهم (MCQ) يشير إلى «العلاج الفعّال بمضادات الميكروبات…»."),

 T("The five basic laboratory techniques", "التقنيات المختبرية الأساسية الخمس"),
 Q("Morphologic identification of the agent in stains of specimens or sections of tissues uses:", "التحديد الشكلي للعامل في صبغات العيّنات أو مقاطع الأنسجة يستعمل:",
   [("Light and electron microscopy", "المجهر الضوئي والإلكتروني"), ("PCR", "PCR"), ("Latex agglutination", "التلازن باللاتكس"), ("Culture media", "الأوساط الزرعية")],
   "Technique 1.", "التقنية 1."),
 Q("Detection of microbial antigens is done by immunologic assay such as:", "يُكشف عن المستضدّات الميكروبية بالمقايسة المناعية مثل:",
   [("Latex agglutination and enzyme immunoassay (EIA)", "التلازن باللاتكس والمقايسة المناعية الإنزيمية (EIA)"), ("Electron microscopy", "المجهر الإلكتروني"),
    ("Biochemical tests", "الاختبارات الكيميائية الحيوية"), ("Gram stain", "صبغة غرام")],
   "Technique 3.", "التقنية 3."),
 Q("Which of the following is one of the five basic laboratory techniques of definitive diagnosis?", "أيّ مما يأتي من التقنيات المختبرية الأساسية الخمس للتشخيص النهائي؟",
   [("Detection of microbial DNA or RNA", "الكشف عن الـ DNA أو الـ RNA الميكروبي"), ("Empiric treatment", "العلاج التجريبي"),
    ("Radiographic findings", "نتائج التصوير الشعاعي"), ("Physical examination", "الفحص البدني")],
   "Technique 4.", "التقنية 4."),
 Q("The fifth basic laboratory technique is:", "التقنية المختبرية الأساسية الخامسة:",
   [("Detection of an inflammatory or host immune response to the pathogenic agents", "الكشف عن استجابة التهابية أو مناعية للمضيف تجاه العوامل الممرضة"),
    ("Cultivation and identification of the organisms", "زرع الكائنات والتعرّف عليها"), ("Detection of microbial antigens", "الكشف عن المستضدّات الميكروبية"),
    ("Morphologic identification", "التحديد الشكلي")],
   "Order: morphology → cultivation → antigens → DNA/RNA → host response.", "الترتيب: الشكل ← الزرع ← المستضدّات ← DNA/RNA ← استجابة المضيف."),
 Q("Definitive microbiologic diagnosis involves which of the following?", "يتضمّن التشخيص الميكروبيولوجي النهائي أيًّا مما يأتي؟",
   [("Morphologic identification and cultivation of the organisms", "التحديد الشكلي وزرع الكائنات"), ("Detection of microbial antigens", "الكشف عن المستضدّات الميكروبية"),
    ("Detection of microbial nucleic acids or host response", "الكشف عن الأحماض النووية الميكروبية أو استجابة المضيف"), ALL],
   "All five techniques (marked «الـ5 نقاط حفظ مختصر»); a 2024-file question.", "التقنيات الخمس كلها (مؤشَّرة «الـ5 نقاط حفظ مختصر»)؛ ومن أسئلة ملف 2024.", fixed="d"),

 T("Laboratory feedback", "التغذية الراجعة من المختبر"),
 Q("The “feedback” information from the laboratory consists of:", "تتكوّن معلومات «التغذية الراجعة» من المختبر من:",
   [("Earliest reports of the results of individual steps in the isolation and identification of the causative agent", "التقارير الأولية عن نتائج الخطوات الفردية في عزل العامل المسبّب وتحديده"),
    ("The final bill of the tests", "الفاتورة النهائية للفحوص"), ("The patient's complaints", "شكاوى المريض"), ("The request form only", "نموذج الطلب فقط")],
   "“feedback” is marked MCQ.", "«feedback» مؤشَّرة MCQ."),
 Q("The term for the earliest reports of results of individual steps in isolating and identifying the causative agent is:", "المصطلح الدالّ على التقارير الأولية لنتائج الخطوات الفردية في عزل العامل المسبّب وتحديده:",
   [("Feedback", "التغذية الراجعة (Feedback)"), ("Colonization", "الاستعمار"), ("Carrier state", "حالة الحمل"), ("Empiric therapy", "العلاج التجريبي")],
   "Reverse of the previous question.", "عكس السؤال السابق."),
]

important = [
 IM("Short answer: what does the clinical presentation of an infectious disease reflect, and what affects this interaction?",
    "سؤال قصير: ماذا يعكس العرض السريري للمرض المعدي، وما الذي يؤثّر في هذا التفاعل؟",
    "It reflects the interaction between the host and the microorganism. This interaction is affected by (1) the host immune status and (2) microbial virulence factors.",
    "يعكس التفاعل بين المضيف والكائن الحي الدقيق. ويتأثّر هذا التفاعل بـ (1) الحالة المناعية للمضيف و(2) عوامل الضراوة الميكروبية."),
 IM("Define diagnostic microbiology.", "عرّف علم الأحياء الدقيقة التشخيصي.",
    "Diagnostic microbiology is the tool that makes it possible to identify the exact pathogens of infectious diseases and the most optimal therapy at the level of individual patients.",
    "علم الأحياء الدقيقة التشخيصي هو الأداة التي تتيح التعرّف الدقيق على مسبّبات الأمراض المعدية والعلاج الأمثل على مستوى المرضى الأفراد."),
 IM("Short answer: compare exogenous and endogenous pathogens.", "سؤال قصير: قارن بين العامل الممرض الخارجي والداخلي.",
    "Exogenous: acquired from environmental or animal sources or from other persons. Endogenous: from the normal flora.",
    "الخارجي: يُكتسب من مصادر بيئية أو حيوانية أو من أشخاص آخرين. والداخلي: من الفلورا الطبيعية."),
 IM("Short answer: what do conventional methods require, and why is the process lengthy?", "سؤال قصير: ماذا تتطلّب الطرق التقليدية، ولماذا تكون العملية طويلة؟",
    "Conventional methods require time to grow the microbes in vitro under specific conditions, and not all microbes can easily be cultured. This is followed by biochemical methods for identification, which further makes the process lengthy.",
    "تتطلّب الطرق التقليدية وقتًا لإنماء الميكروبات في المختبر تحت ظروف محدّدة، وليس كل الميكروبات تُزرع بسهولة. ويلي ذلك طرق كيميائية حيوية للتعرّف، مما يجعل العملية أطول."),
 IM("List the factors that render culture-based methods less reliable.", "عدّد العوامل التي تجعل الطرق القائمة على الزرع أقل موثوقية.",
    "1) Transport of the specimens under less than ideal conditions. 2) Prior use of antibiotics. 3) Small number of organisms.",
    "1) نقل العيّنات في ظروف أقل من المثالية. 2) الاستعمال المسبق للمضادات الحيوية. 3) قلّة عدد الكائنات."),
 IM("Short answer: on what do newer methods depend, and what can they detect directly from the specimen?", "سؤال قصير: على ماذا تعتمد الطرق الأحدث، وماذا يمكنها أن تكشف مباشرة من العيّنة؟",
    "Newer methods depend on amplification of nucleic acids followed by use of probes for identification. They can be used to detect antibiotic resistance genes directly from the specimen and help direct targeted therapy with efficacy.",
    "تعتمد الطرق الأحدث على تضخيم الأحماض النووية متبوعًا باستعمال المسابير للتعرّف. ويمكن استعمالها للكشف عن جينات مقاومة المضادات الحيوية مباشرة من العيّنة، والمساعدة في توجيه العلاج المستهدف بفعالية."),
 IM("What may microbial colonization result in? When does infectious disease occur?", "إلامَ قد يؤدّي الاستعمار الميكروبي؟ ومتى يحدث المرض المعدي؟",
    "1) Elimination of the microorganism without affecting the host. 2) Infection in which the organisms multiply and cause the host to react by making an immune or other type of response. 3) A transient or prolonged carrier state. Infectious disease occurs when the organism causes tissue damage and loss of function of body systems.",
    "1) التخلّص من الكائن الدقيق دون التأثير في المضيف. 2) عدوى تتكاثر فيها الكائنات وتجعل المضيف يستجيب باستجابة مناعية أو نوع آخر من الاستجابة. 3) حالة حمل عابرة أو مطوّلة. ويحدث المرض المعدي عندما يسبّب الكائن تلف الأنسجة وفقدان وظائف أجهزة الجسم."),
 IM("Pretest: give the purpose of studying diagnostic bacteria.", "الاختبار القبلي: اذكر الغرض من دراسة البكتيريا التشخيصية.",
    "To identify the disease-causing bacteria and select the proper treatment (the answer written in class). In the lecture's words: the purpose and philosophy of diagnostic bacteriology depend on identifying the causative microorganism by different laboratory methods, which is usually essential for effective antimicrobial and supportive therapy.",
    "تحديد البكتيريا المسبّبة للمرض واختيار العلاج المناسب (الجواب المكتوب بالمحاضرة). وبعبارة المحاضرة: يعتمد غرض وفلسفة علم الجراثيم التشخيصي على تحديد الكائن المسبّب بطرق مختبرية مختلفة، وهو ضروري عادةً للعلاج الفعّال بمضادات الميكروبات والعلاج الداعم."),
 IM("Posttest: what are the five basic laboratory techniques?", "الاختبار البعدي: ما التقنيات المختبرية الأساسية الخمس؟",
    "From the lecture text: 1) Morphologic identification of the agent in stains of specimens or sections of tissues (light and electron microscopy). 2) Cultivation and identification of the organisms. 3) Detection of microbial antigens by immunologic assay (latex agglutination, enzyme immunoassay [EIA]). 4) Detection of microbial DNA or RNA. 5) Detection of an inflammatory or host immune response to the pathogenic agents. BIOS note: the answer handwritten in class (microscopy, culture, staining, biochemical test, antimicrobial susceptibility testing) differs from the lecture's list — study the lecture's five and confirm with the doctor which list he wants.",
    "من نصّ المحاضرة: 1) التحديد الشكلي للعامل في صبغات العيّنات أو مقاطع الأنسجة (المجهر الضوئي والإلكتروني). 2) زرع الكائنات والتعرّف عليها. 3) الكشف عن المستضدّات الميكروبية بالمقايسة المناعية (التلازن باللاتكس، المقايسة المناعية الإنزيمية EIA). 4) الكشف عن الـ DNA أو الـ RNA الميكروبي. 5) الكشف عن استجابة التهابية أو مناعية للمضيف تجاه العوامل الممرضة. ملاحظة BIOS: الجواب المكتوب بخط اليد بالمحاضرة (المجهر، الزرع، التصبيغ، الاختبارات الكيميائية الحيوية، اختبار الحساسية للمضادات) يختلف عن قائمة المحاضرة — احفظ الخمس الواردة في المحاضرة وتأكّد من الدكتور أيّ القائمتين يريد."),
 IM("Define the laboratory “feedback” information.", "عرّف معلومات «التغذية الراجعة» من المختبر.",
    "The “feedback” information from the laboratory consists of the earliest reports of the results of individual steps in the isolation and identification of the causative agent.",
    "تتكوّن معلومات «التغذية الراجعة» من المختبر من التقارير الأولية عن نتائج الخطوات الفردية في عزل العامل المسبّب وتحديده."),
]

mcq = balance(mcq, 7101)
for q in mcq:
    if "_fixed" in q: q["answer"] = q.pop("_fixed")

meta = {"subject_en": "Diagnostic Microbiology", "subject_ar": "الأحياء المجهرية التشخيصية", "short_ar": "بكتريا",
        "instructor": "د. عدنان", "unit_en": "Lecture 1", "unit_ar": "المحاضرة 1", "unit_label": "LEC", "unit_no": "1",
        "title_en": "Diagnostic Microbiology: Purpose and Philosophy", "title_ar": "علم الأحياء الدقيقة التشخيصي: الغرض والفلسفة",
        "department": "قسم التحليلات", "kind": "Theory — نظري", "questions_kind": "MCQ + SA — اختيار ومقالية",
        "stage": "The fourth stage — الرابعة",
        "file_name": "BIOS - بكتريا نظري المحاضرة الأولى - بنك أسئلة شامل"}
Qs = {"title_en": "Purpose and Philosophy (Lecture 1) — Comprehensive Questions (MCQ + SA)",
      "title_ar": "الغرض والفلسفة (المحاضرة 1) — أسئلة شاملة (اختيار + مقالية)",
      "answers_inline": True, "compact": True, "mcq_per_page": 4,
      "mcq_en": "Comprehensive MCQs — Lecture 1", "mcq_ar": "أسئلة اختيار شاملة — المحاضرة الأولى",
      "intro_en": ["Q. Select the most correct answer from the followings",
                   "These questions cover the whole lecture; the answer and a short reason sit under each MCQ, and the model answer under each essay question. Paragraphs crossed out (✗) in class are not asked; the parts marked “short answer” come as essay questions."],
      "intro_ar": ["س. اختر الإجابة الأصح مما يأتي",
                   "هذه الأسئلة تغطّي المحاضرة كاملة؛ والحل وسطر سبب مختصر تحت كل سؤال اختيار، والجواب النموذجي تحت كل سؤال مقالي. الفقرات المشطوبة (✗) بالمحاضرة لم تُسأل، والأجزاء المؤشَّرة «سؤال قصير» جاءت أسئلةً مقالية."],
      "mcq": ltr_all(mcq), "tf": [], "traps": [], "important": ltr_all(important)}

d = "/home/user/-/bacteriology-lec1-mcq"
os.makedirs(d, exist_ok=True)
json.dump({"meta": meta, "questions": Qs}, open(d + "/lecture.json", "w"), ensure_ascii=False, indent=1)
qs = [m for m in mcq if "answer" in m]
print("MCQ:", len(qs), "| SA:", len(important), "| dist:", dict(Counter(m["answer"] for m in qs)))
for i, q in enumerate(qs, 1):
    print(i, q["answer"], q["options"]["abcd".index(q["answer"])][0][:60])
