import sys, json, os
from collections import Counter
WORK = "/home/claude/scratch/work"
sys.path.insert(0, WORK + "/bac"); from bal import balance
sys.path.insert(0, WORK); from bidi import ltr_all

# Diagnostic Microbiology — THEORY Lecture 2 (stage 4, د. عدنان): Laboratory safety. Source 2026-11-22: phone scan (6 pages,
# iOS, no text layer) of the department's bilingual handout, annotated in class. Marks: «MCQ», «مهم», «مهمات جدًا» (the physical
# methods of sterilization), «سؤال قصير» (factors limiting sterilization; compressed gases), «تعريف أو MCQ» (fire safety),
# «T,F» (no extension cables), «كلهن تجربة فهم» (the six admonitions; the routes of exposure).
# Crossed ✗ → NOT asked: the "Safety programs have been expanded…" paragraph; "These processes may be accomplished by…";
# the Chemical safety paragraph (MSDSs) — note: the 2023 exam asked "MSDSs → chemical safety" (see the 2024 bank);
# "Electrical cables should be checked…"; the first Biosafety paragraph (lab-acquired infections reaching adjacent labs/families).
# Slide content flagged: "Chemicals" listed under PHYSICAL methods of sterilization (they are chemical).

def Q(en, ar, opts, why_en, why_ar, fixed=None):
    d = dict(en=en, ar=ar, options=[list(o) for o in opts], )  # user 2026-11-22: MCQ only, no explanation
    if fixed: d["_fixed"] = fixed
    else: d["answer"] = "a"
    return d
def T(en, ar): return {"topic_en": en, "topic_ar": ar}
def IM(en, ar, ae, aa): return dict(en=en, ar=ar, answer_en=ae, answer_ar=aa)
ALL = ("All of the above", "جميع ما سبق")

mcq = [
 T("Laboratory safety — admonitions", "السلامة المختبرية — التحذيرات"),
 Q("Microbiology laboratory admonitions include the necessity to:", "تتضمّن تحذيرات مختبر الأحياء الدقيقة ضرورة:",
   [("Wear gloves", "ارتداء القفازات"), ("Wash hands after working with infectious materials", "غسل اليدين بعد العمل بالمواد المعدية"),
    ("Disinfect all instruments immediately after use", "تطهير جميع الأدوات فور الاستعمال"), ALL],
   "Six admonitions («كلهن تجربة فهم»); a 2023-exam question.", "ستة تحذيرات («كلهن فهم»)؛ ومن أسئلة امتحان 2023.", fixed="d"),
 Q("The first admonition in the microbiology laboratory (marked MCQ) is to:", "أول تحذير في مختبر الأحياء الدقيقة (مؤشَّر MCQ):",
   [("Wear gloves", "ارتداء القفازات"), ("Report accidents", "الإبلاغ عن الحوادث"), ("Moisten labels with water", "ترطيب الملصقات بالماء"), ("Disinfect waste", "تطهير النفايات")],
   "(1) wear gloves.", "(1) ارتداء القفازات."),
 Q("Specimen labels should be moistened with:", "يجب ترطيب ملصقات العيّنات بـ:",
   [("Water rather than the tongue", "الماء بدلًا من اللسان"), ("The tongue", "اللسان"), ("Alcohol", "الكحول"), ("Blood", "الدم")],
   "Admonition 4.", "التحذير 4."),
 Q("All contaminated waste should be:", "يجب أن تكون جميع النفايات الملوّثة:",
   [("Disinfected before discarding", "مطهَّرة قبل التخلّص منها"), ("Discarded directly", "يُتخلّص منها مباشرة"),
    ("Kept on the bench", "محفوظة على المنضدة"), ("Washed with water only", "مغسولة بالماء فقط")],
   "Admonition 5.", "التحذير 5."),
 Q("All accidents or exposures to infectious agents should be:", "يجب أن تُعامل جميع الحوادث أو التعرّضات للعوامل المعدية بـ:",
   [("Reported to appropriate personnel", "الإبلاغ عنها للموظفين المختصّين"), ("Hidden", "إخفائها"), ("Ignored if minor", "تجاهلها إن كانت بسيطة"), ("Reported to the patient", "إبلاغ المريض")],
   "Admonition 6.", "التحذير 6."),
 Q("How many admonitions of the microbiology laboratory are listed?", "كم تحذيرًا لمختبر الأحياء الدقيقة مذكورًا؟",
   [("6", "6"), ("4", "4"), ("5", "5"), ("8", "8")],
   "Gloves, hand washing, instruments, labels, waste, reporting.", "القفازات، غسل اليدين، الأدوات، الملصقات، النفايات، الإبلاغ."),

 T("Sterilization, disinfection and decontamination", "التعقيم والتطهير وإزالة التلوّث"),
 Q("A process that kills all forms of microbial life, including bacterial endospores, is:", "العملية التي تقتل جميع أشكال الحياة الميكروبية، بما فيها الأبواغ الداخلية البكتيرية، هي:",
   [("Sterilization", "التعقيم"), ("Disinfection", "التطهير"), ("Decontamination", "إزالة التلوّث"), ("Antisepsis", "التطهير الموضعي")],
   "Starred «مهم جدًا»; a 2023-exam question.", "منجَّم «مهم جدًّا»؛ ومن أسئلة امتحان 2023."),
 Q("A process that destroys pathogenic organisms, but not necessarily all microorganisms, endospores, or prions, is:", "العملية التي تقضي على الكائنات الممرضة، لكن ليس بالضرورة جميع الكائنات الدقيقة أو الأبواغ الداخلية أو البريونات، هي:",
   [("Disinfection", "التطهير"), ("Sterilization", "التعقيم"), ("Incineration", "الحرق"), ("Filtration", "الترشيح")],
   "Marked MCQ.", "مؤشَّر MCQ."),
 Q("Some disinfectants will kill endospores:", "بعض المطهّرات تقتل الأبواغ الداخلية:",
   [("With prolonged exposure times", "مع أوقات تعرّض طويلة"), ("Immediately", "فورًا"), ("Never", "أبدًا لا تقتلها"), ("Only at `4 ºC`", "عند `4 ºC` فقط")],
   "The last sentence of the definition.", "الجملة الأخيرة من التعريف."),
 Q("Decontamination is:", "إزالة التلوّث هي:",
   [("The removal of pathogenic microorganisms so items are safe to handle or dispose of", "إزالة الكائنات الدقيقة الممرضة بحيث تصبح المواد آمنة للتعامل معها أو التخلّص منها"),
    ("Killing all forms of microbial life", "قتل جميع أشكال الحياة الميكروبية"), ("Killing endospores only", "قتل الأبواغ فقط"), ("Heating at `45 ºC`", "التسخين عند `45 ºC`")],
   "Marked «حفظ MCQ».", "مؤشَّر «حفظ MCQ»."),
 Q("Which process does NOT necessarily kill endospores or prions?", "أيّ عملية لا تقتل بالضرورة الأبواغ الداخلية أو البريونات؟",
   [("Disinfection", "التطهير"), ("Sterilization", "التعقيم"), ("Incineration", "الحرق"), ("Moist heat sterilization", "التعقيم بالحرارة الرطبة")],
   "Only sterilization kills all forms.", "التعقيم وحده يقتل كل الأشكال."),
 Q("Factors that limit the success or degree of sterilization, disinfection or decontamination include:", "من العوامل التي تحدّ من نجاح التعقيم أو التطهير أو إزالة التلوّث:",
   [("Organic load (organisms, blood or body fluids)", "الحمل العضوي (الكائنات، الدم أو سوائل الجسم)"), ("The type of organisms present", "نوع الكائنات الموجودة"),
    ("The concentration and exposure time to the germicide", "تركيز المبيد الجرثومي ووقت التعرّض له"), ALL],
   "Marked «سؤال قصير»; a 2023-exam question.", "مؤشَّر «سؤال قصير»؛ ومن أسئلة امتحان 2023.", fixed="d"),
 Q("Which of the following is also a factor that limits sterilization or disinfection?", "أيّ مما يأتي من العوامل التي تحدّ من التعقيم أو التطهير أيضًا؟",
   [("Presence of a biofilm", "وجود غشاء حيوي (biofilm)"), ("Using sterile water", "استعمال الماء المعقّم"), ("Labelling the container", "وسم الحاوية"), ("Wearing gloves", "ارتداء القفازات")],
   "Also: physical/chemical nature of the surface, temperature, pH, humidity.", "وأيضًا: الطبيعة الفيزيائية والكيميائية للسطح، الحرارة، الأس الهيدروجيني، الرطوبة."),
 Q("Hinges, cracks and rough or smooth surfaces are examples of:", "المفصلات والشقوق والأسطح الخشنة أو الملساء أمثلة على:",
   [("The physical and chemical nature of the surface", "الطبيعة الفيزيائية والكيميائية للسطح"), ("Organic load", "الحمل العضوي"),
    ("The type of organisms", "نوع الكائنات"), ("The germicide concentration", "تركيز المبيد")],
   "From the same list.", "من القائمة نفسها."),

 T("Methods of sterilization", "طرق التعقيم"),
 Q("The physical methods of sterilization include:", "تشمل الطرق الفيزيائية للتعقيم:",
   [("Incineration and moist heat", "الحرق والحرارة الرطبة"), ("Dry heat and filtration", "الحرارة الجافة والترشيح"), ("Ionizing (gamma) radiation", "الإشعاع المؤيّن (غاما)"), ALL],
   "Marked «مهمات جدًا»; a 2023-exam question.", "مؤشَّرة «مهمات جدًّا»؛ ومن أسئلة امتحان 2023.", fixed="d"),
 Q("Which of the following is NOT listed among the methods of sterilization?", "أيّ مما يأتي ليس من طرق التعقيم المذكورة؟",
   [("Pasteurization", "البسترة"), ("Filtration", "الترشيح"), ("Dry heat", "الحرارة الجافة"), ("Incineration", "الحرق")],
   "Pasteurization is not sterilization (2023 exam).", "البسترة ليست تعقيمًا (امتحان 2023)."),
 Q("Ethylene oxide gas and hydrogen peroxide gas plasma are examples of sterilization by:", "غاز أكسيد الإثيلين وبلازما غاز بيروكسيد الهيدروجين أمثلة على التعقيم بـ:",
   [("Chemicals", "المواد الكيميائية"), ("Ionizing radiation", "الإشعاع المؤيّن"), ("Dry heat", "الحرارة الجافة"), ("Filtration", "الترشيح")],
   "The lecture lists “Chemicals” under the physical methods heading; they are actually chemical methods.",
   "المحاضرة تذكر «المواد الكيميائية» تحت عنوان الطرق الفيزيائية؛ وهي في الحقيقة طرق كيميائية."),
 Q("The type of radiation used for sterilization in the lecture is:", "نوع الإشعاع المستعمل للتعقيم في المحاضرة:",
   [("Ionizing (gamma) radiation", "الإشعاع المؤيّن (غاما)"), ("Infrared", "الأشعة تحت الحمراء"), ("Visible light", "الضوء المرئي"), ("Radio waves", "موجات الراديو")],
   "Gamma.", "غاما."),

 T("Fire, electrical and gas safety", "السلامة من الحرائق والكهرباء والغازات"),
 Q("Fire safety is:", "السلامة من الحرائق:",
   [("An important component of the laboratory safety program", "عنصر مهم في برنامج السلامة المختبرية"), ("Optional in microbiology labs", "اختيارية في مختبرات الأحياء الدقيقة"),
    ("Related to chemical labels only", "مرتبطة بملصقات المواد الكيميائية فقط"), ("The same as biosafety", "مثل السلامة الحيوية")],
   "Marked «تعريف أو MCQ».", "مؤشَّر «تعريف أو MCQ»."),
 Q("Fire evacuation plans posted in each laboratory are essentially:", "خطط الإخلاء من الحرائق المنشورة في كل مختبر هي في الأساس:",
   [("Strategies for finding the nearest exit in case of fire", "استراتيجيات للعثور على أقرب مخرج عند نشوب حريق"), ("Lists of fire extinguishers", "قوائم بطفايات الحريق"),
    ("Chemical labels", "ملصقات كيميائية"), ("Electrical diagrams", "مخطّطات كهربائية")],
   "Slide text.", "نصّ المحاضرة."),
 Q("All plugs in the laboratory should be:", "يجب أن تكون جميع المقابس في المختبر:",
   [("The three-prong, grounded type", "من النوع المؤرَّض ثلاثي الشُّعب"), ("Two-prong", "ثنائية الشُّعب"), ("Any type", "من أي نوع"), ("Extension cables", "كابلات تمديد")],
   "Marked MCQ.", "مؤشَّر MCQ."),
 Q("All sockets should be checked for electrical grounding and leakage:", "يجب فحص جميع المقابس للتأريض والتسرّب الكهربائي:",
   [("At least annually", "سنويًّا على الأقل"), ("Every 10 years", "كل 10 سنوات"), ("Never", "لا تُفحص"), ("Only after a fire", "بعد الحريق فقط")],
   "Slide text.", "نصّ المحاضرة."),
 Q("True or false: extension cables may be used in the laboratory.", "صح أم خطأ: يمكن استعمال كابلات التمديد في المختبر.",
   [("False — no extension cables should be used in the laboratory", "خطأ — لا ينبغي استعمال أي كابلات تمديد في المختبر"), ("True", "صح"),
    ("True if grounded", "صح إذا كانت مؤرَّضة"), ("True for one day only", "صح ليوم واحد فقط")],
   "Marked «T,F».", "مؤشَّر «T,F»."),
 Q("Compressed gas cylinders such as `CO2` and anaerobic gas mixture:", "أسطوانات الغاز المضغوط مثل `CO2` وخليط الغاز اللاهوائي:",
   [("Contain pressurized gases and must be properly handled and secured", "تحتوي غازات مضغوطة ويجب التعامل معها وتأمينها بشكل صحيح"),
    ("Contain liquid cultures", "تحتوي مزارع سائلة"), ("Are harmless", "غير مؤذية"), ("Can be stored anywhere", "يمكن خزنها في أي مكان")],
   "Marked «سؤال قصير».", "مؤشَّر «سؤال قصير»."),
 Q("Examples of compressed gas cylinders in the lab are:", "أمثلة أسطوانات الغاز المضغوط في المختبر:",
   [("`CO2` and anaerobic gas mixture", "`CO2` وخليط الغاز اللاهوائي"), ("Oxygen and nitrogen only", "الأكسجين والنيتروجين فقط"),
    ("Hydrogen peroxide", "بيروكسيد الهيدروجين"), ("Ethanol", "الإيثانول")],
   "Slide text.", "نصّ المحاضرة."),

 T("Biosafety — routes of exposure", "السلامة الحيوية — طرق التعرّض"),
 Q("Individuals are exposed to health care–associated infections, in transporting specimens and in public areas such as elevators or cafeterias, by:", "يتعرّض الأفراد للعدوى المرتبطة بالرعاية الصحية، وفي نقل العيّنات، وفي الأماكن العامة كالمصاعد والكافيتريات، عن طريق:",
   [("Rubbing the eyes or nose with contaminated hands", "فرك العين أو الأنف بالأيدي الملوّثة"), ("Inhaling aerosols produced during centrifugation, vortex mixing or spills", "استنشاق الهباء الناتج أثناء الطرد المركزي أو الخلط بالدوامة أو الانسكابات"),
    ("Accidentally ingesting microorganisms (pens or fingers in the mouth)", "تناول الكائنات خطأً (وضع الأقلام أو الأصابع في الفم)"), ALL],
   "Routes of exposure («كلّه فهم»).", "طرق التعرّض («كلّه فهم»).", fixed="d"),
 Q("Aerosols may be inhaled when they are produced during:", "قد يُستنشق الهباء الجوي حين يتكوّن أثناء:",
   [("Centrifugation, mixing with a vortex, or spills of liquid cultures", "الطرد المركزي، أو الخلط بالدوامة، أو انسكاب المزارع السائلة"), ("Labelling", "الوسم"),
    ("Hand washing", "غسل اليدين"), ("Reading results", "قراءة النتائج")],
   "Route 2.", "الطريق 2."),
 Q("Percutaneous inoculation means:", "التلقيح عن طريق الجلد يعني:",
   [("Puncture from an accidental needle stick", "الوخز بإبرة عرضيًّا"), ("Inhaling aerosols", "استنشاق الهباء"),
    ("Rubbing the eyes", "فرك العين"), ("Swallowing cultures", "بلع المزارع")],
   "Boxed «مهمة».", "مؤطَّر «مهمة»."),
 Q("Manipulating or opening bacterial cultures outside of a biosafety hood is dangerous because it:", "التعامل مع المزارع البكتيرية أو فتحها خارج غطاء السلامة الحيوية خطر لأنه:",
   [("Creates potentially hazardous aerosols", "يكوّن هباءً قد يكون خطرًا"), ("Kills the bacteria", "يقتل البكتيريا"),
    ("Dries the medium", "يجفّف الوسط"), ("Changes the colour of the medium", "يغيّر لون الوسط")],
   "Route 5.", "الطريق 5."),
 Q("Which of the following is a route of exposure listed in the lecture?", "أيّ مما يأتي من طرق التعرّض المذكورة في المحاضرة؟",
   [("Failure to wash hands upon leaving the restroom or public areas before entering the laboratory", "عدم غسل اليدين عند مغادرة الحمّام أو الأماكن العامة قبل دخول المختبر"),
    ("Wearing gloves", "ارتداء القفازات"), ("Using a biosafety hood", "استعمال غطاء السلامة الحيوية"), ("Disinfecting instruments", "تطهير الأدوات")],
   "Route 6.", "الطريق 6."),
 Q("If laboratory protective clothing becomes contaminated with body fluids or potential pathogens, it should be:", "إذا تلوّثت الملابس الواقية للمختبر بسوائل الجسم أو بمسبّبات محتملة، يجب:",
   [("Sterilized in an autoclave immediately and cleaned before reusing", "تعقيمها في الأوتوكلاف فورًا وتنظيفها قبل إعادة الاستعمال"), ("Washed at home", "غسلها في البيت"),
    ("Discarded in ordinary waste", "رميها مع النفايات العادية"), ("Worn again after drying", "لبسها ثانية بعد التجفيف")],
   "Marked MCQ (autoclave).", "مؤشَّر MCQ (الأوتوكلاف)."),
]

important = [
 IM("List the admonitions of the microbiology laboratory.", "عدّد تحذيرات مختبر الأحياء الدقيقة.",
    "(1) Wear gloves; (2) wash hands after working with infectious materials; (3) disinfect all instruments immediately after use; (4) use water to moisten specimen labels rather than the tongue; (5) disinfect all contaminated waste before discarding; and (6) report to appropriate personnel all accidents or exposures to infectious agents.",
    "(1) ارتداء القفازات؛ (2) غسل اليدين بعد العمل بالمواد المعدية؛ (3) تطهير جميع الأدوات فور الاستعمال؛ (4) استعمال الماء لترطيب ملصقات العيّنات بدلًا من اللسان؛ (5) تطهير جميع النفايات الملوّثة قبل التخلّص منها؛ (6) إبلاغ الموظفين المختصّين بجميع الحوادث أو التعرّضات للعوامل المعدية."),
 IM("Define sterilization, disinfection and decontamination.", "عرّف التعقيم والتطهير وإزالة التلوّث.",
    "Sterilization is a process that kills all forms of microbial life, including bacterial endospores. Disinfection is a process that destroys pathogenic organisms, but not necessarily all microorganisms, endospores, or prions; however, some disinfectants will kill endospores with prolonged exposure times. Decontamination is the removal of pathogenic microorganisms so items are safe to handle or dispose of.",
    "التعقيم: عملية تقتل جميع أشكال الحياة الميكروبية، بما فيها الأبواغ الداخلية البكتيرية. التطهير: عملية تقضي على الكائنات الممرضة، لكن ليس بالضرورة جميع الكائنات الدقيقة أو الأبواغ الداخلية أو البريونات؛ ومع ذلك تقتل بعض المطهّرات الأبواغ مع التعرّض الطويل. إزالة التلوّث: إزالة الكائنات الممرضة بحيث تصبح المواد آمنة للتعامل معها أو التخلّص منها."),
 IM("Short answer: what factors limit the success or degree of sterilization, disinfection, or decontamination in a health care setting?", "سؤال قصير: ما العوامل التي تحدّ من نجاح أو درجة التعقيم أو التطهير أو إزالة التلوّث في أماكن الرعاية الصحية؟",
    "Organic load (organisms and other contaminating materials such as blood or body fluids), the type of organisms present, the concentration and exposure time to the germicide, the physical and chemical nature of the surface (hinges, cracks, rough or smooth surfaces), temperature, pH, humidity, and presence of a biofilm.",
    "الحمل العضوي (الكائنات والمواد الملوِّثة الأخرى كالدم أو سوائل الجسم)، ونوع الكائنات الموجودة، وتركيز المبيد الجرثومي ووقت التعرّض له، والطبيعة الفيزيائية والكيميائية للسطح (المفصلات، الشقوق، الأسطح الخشنة أو الملساء)، والحرارة، والأس الهيدروجيني، والرطوبة، ووجود غشاء حيوي."),
 IM("List the physical methods of sterilization.", "عدّد الطرق الفيزيائية للتعقيم.",
    "Incineration; moist heat; dry heat; filtration; ionizing (gamma) radiation; and chemicals (ethylene oxide gas, hydrogen peroxide gas plasma, vaporized hydrogen peroxide, and other liquid chemicals). BIOS note: the lecture lists chemicals under this heading, although they are chemical, not physical, methods.",
    "الحرق؛ الحرارة الرطبة؛ الحرارة الجافة؛ الترشيح؛ الإشعاع المؤيّن (غاما)؛ والمواد الكيميائية (غاز أكسيد الإثيلين، بلازما غاز بيروكسيد الهيدروجين، بيروكسيد الهيدروجين المتبخّر، وسوائل كيميائية أخرى). ملاحظة BIOS: المحاضرة تذكر المواد الكيميائية تحت هذا العنوان مع أنها طرق كيميائية لا فيزيائية."),
 IM("Define fire safety.", "عرّف السلامة من الحرائق.",
    "Fire safety is an important component of the laboratory safety program. Each laboratory is required to post fire evacuation plans that are essentially strategies for finding the nearest exit in case of fire.",
    "السلامة من الحرائق عنصر مهم في برنامج السلامة المختبرية. ويُطلب من كل مختبر نشر خطط الإخلاء من الحرائق، وهي في الأساس استراتيجيات للعثور على أقرب مخرج عند نشوب حريق."),
 IM("What are the rules of electrical safety in the laboratory?", "ما قواعد السلامة الكهربائية في المختبر؟",
    "All plugs should be the three-prong, grounded type. All sockets should be checked for electrical grounding and leakage at least annually. No extension cables should be used in the laboratory.",
    "يجب أن تكون جميع المقابس من النوع المؤرَّض ثلاثي الشُّعب. ويجب فحص جميع المقابس للتأريض والتسرّب الكهربائي سنويًّا على الأقل. ولا ينبغي استعمال أي كابلات تمديد في المختبر."),
 IM("Short answer: what do compressed gas cylinders contain, and how must they be treated?", "سؤال قصير: ماذا تحتوي أسطوانات الغاز المضغوط، وكيف يجب التعامل معها؟",
    "Compressed gas cylinders (CO2, anaerobic gas mixture) contain pressurized gases and must be properly handled and secured.",
    "تحتوي أسطوانات الغاز المضغوط (CO2، خليط الغاز اللاهوائي) غازات مضغوطة، ويجب التعامل معها وتأمينها بشكل صحيح."),
 IM("How are individuals exposed to health care–associated infections, in transporting specimens and in public areas?", "كيف يتعرّض الأفراد للعدوى المرتبطة بالرعاية الصحية، وفي نقل العيّنات، وفي الأماكن العامة؟",
    "By: rubbing the eyes or nose with contaminated hands; inhaling aerosols produced during centrifugation, mixing with a vortex, or spills of liquid cultures; accidentally ingesting microorganisms by putting pens or fingers in the mouth; receiving percutaneous inoculation (through puncture from an accidental needle stick); manipulating or opening bacterial cultures in liquid media or on plates, creating potentially hazardous aerosols, outside of a biosafety hood; and failure to wash hands upon leaving the restroom or other public areas before entering the laboratory.",
    "عن طريق: فرك العين أو الأنف بالأيدي الملوّثة؛ واستنشاق الهباء الناتج أثناء الطرد المركزي أو الخلط بالدوامة أو انسكاب المزارع السائلة؛ وتناول الكائنات خطأً بوضع الأقلام أو الأصابع في الفم؛ والتلقيح عن طريق الجلد (وخز الإبرة العرضي)؛ والتعامل مع المزارع البكتيرية أو فتحها في الأوساط السائلة أو على الأطباق خارج غطاء السلامة الحيوية مما يكوّن هباءً خطرًا؛ وعدم غسل اليدين عند مغادرة الحمّام أو الأماكن العامة قبل دخول المختبر."),
 IM("What should be done if the laboratory protective clothing becomes contaminated?", "ماذا يجب أن يُفعل إذا تلوّثت الملابس الواقية للمختبر؟",
    "If the laboratory protective clothing becomes contaminated with body fluids or potential pathogens, it should be sterilized in an autoclave immediately and cleaned before reusing.",
    "إذا تلوّثت الملابس الواقية للمختبر بسوائل الجسم أو بمسبّبات محتملة، يجب تعقيمها في الأوتوكلاف فورًا وتنظيفها قبل إعادة استعمالها."),
]

mcq = balance(mcq, 7202)
for q in mcq:
    if "_fixed" in q: q["answer"] = q.pop("_fixed")

meta = {"subject_en": "Diagnostic Microbiology", "subject_ar": "الأحياء المجهرية التشخيصية", "short_ar": "بكتريا",
        "instructor": "د. عدنان", "unit_en": "Lecture 2", "unit_ar": "المحاضرة 2", "unit_label": "LEC", "unit_no": "2",
        "title_en": "Laboratory Safety", "title_ar": "السلامة المختبرية",
        "department": "قسم التحليلات", "kind": "Theory — نظري", "questions_kind": "MCQ — اختيار من متعدد",
        "stage": "The fourth stage — الرابعة",
        "file_name": "BIOS - بكتريا نظري المحاضرة الثانية - أسئلة MCQ"}
Qs = {"title_en": "Laboratory Safety (Lecture 2) — MCQ",
      "title_ar": "السلامة المختبرية (المحاضرة 2) — أسئلة اختيار",
      "answers_inline": True, "compact": True, "mcq_per_page": 5,
      "mcq_en": "Comprehensive MCQs — Lecture 2", "mcq_ar": "أسئلة اختيار شاملة — المحاضرة الثانية",
      "intro_en": ["Q. Select the most correct answer from the followings",
                   "These questions cover the whole lecture; the answer sits under each question. Paragraphs crossed out (✗) in class are not asked."],
      "intro_ar": ["س. اختر الإجابة الأصح مما يأتي",
                   "هذه الأسئلة تغطّي المحاضرة كاملة؛ والحل تحت كل سؤال. الفقرات المشطوبة (✗) بالمحاضرة لم تُسأل."],
      "mcq": ltr_all(mcq), "tf": [], "traps": [], "important": []}

d = "/home/user/-/bacteriology-lec2-mcq"
os.makedirs(d, exist_ok=True)
json.dump({"meta": meta, "questions": Qs}, open(d + "/lecture.json", "w"), ensure_ascii=False, indent=1)
qs = [m for m in mcq if "answer" in m]
print("MCQ:", len(qs), "| dist:", dict(Counter(m["answer"] for m in qs)))
for i, q in enumerate(qs, 1):
    print(i, q["answer"], q["options"]["abcd".index(q["answer"])][0][:60])
