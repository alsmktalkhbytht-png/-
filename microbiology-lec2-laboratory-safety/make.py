# BIOS — بكتريا نظري المحاضرة الثانية (Laboratory safety) — د. عدنان، المرحلة الرابعة
# المصدر: نص ملصق في الرسالة (source.txt) + لقطة صفحة تبيّن مكان الشكل (2) (source-page-figure2.jpg).
# كل جملة منقولة حرفيًا ومترجمة؛ بلا تصحيح إملائي (الأصل كما هو).
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
 SEC("Laboratory safety", "السلامة في المختبر"),
 C("Microbiology laboratory include admonitions such as the necessity to (1) wear gloves, (2) wash hands after working with infectious materials, (3) disinfect all instruments immediately after use, (4) use water to moisten specimen labels rather than the tongue, (5) disinfect all contaminated waste before discarding, and (6) report to appropriate personnel all accidents or exposures to infectious agents.",
   "يتضمّن **مختبر الأحياء المجهرية** تحذيرات مثل ضرورة: (1) **ارتداء القفازات**، (2) **غسل اليدين** بعد العمل بالمواد المعدية، (3) **تطهير كل الأدوات** فور استعمالها، (4) استعمال **الماء لترطيب ملصقات العيّنات** بدل اللسان، (5) **تطهير كل النفايات الملوّثة** قبل التخلّص منها، (6) **إبلاغ الأشخاص المختصّين** بكل الحوادث أو حالات التعرّض للعوامل المعدية."),

 SEC("Safety", "السلامة"),
 C("Programs have been expanded to include the proper handling of biologic hazards encountered in processing patient specimens and handling infectious microorganisms; fire and electrical safety; the safe handling, storage, and disposal of chemicals and radioactive substances; and techniques for safely lifting or moving heavy objects.",
   "وُسّعت **البرامج** لتشمل: التعامل الصحيح مع **المخاطر الحيوية** التي تُصادف عند معالجة عيّنات المرضى والتعامل مع الكائنات الدقيقة المعدية؛ و**السلامة من الحريق والكهرباء**؛ والتعامل الآمن مع **المواد الكيميائية والمواد المشعّة** وخزنها والتخلّص منها؛ وتقنيات **رفع الأجسام الثقيلة أو تحريكها** بأمان."),

 SEC("Sterilization, Disinfection, and Decontamination", "التعقيم والتطهير وإزالة التلوّث"),
 C("**Sterilization** is a process that kills all forms of microbial life, including bacterial endospores.",
   "**التعقيم** (`Sterilization`) عملية تقتل **كل أشكال الحياة الميكروبية**، بما فيها **الأبواغ الداخلية البكتيرية**."),
 C(["**Disinfection** is a process that destroys pathogenic organisms, but not necessarily all microorganisms, endospores, or prions.",
    "However, some disinfectants will kill endospores with prolonged exposure times."],
   ["**التطهير** (`Disinfection`) عملية تُتلف **الكائنات المُمرِضة**، ولكن ليس بالضرورة كل الكائنات الدقيقة أو الأبواغ الداخلية أو البريونات.",
    "ومع ذلك، فإن بعض المطهّرات تقتل الأبواغ الداخلية عند **إطالة زمن التعرّض**."]),
 C("**Decontamination** is the removal of pathogenic microorganisms so items are safe to handle or dispose of.",
   "**إزالة التلوّث** (`Decontamination`) هي إزالة الكائنات الدقيقة المُمرِضة بحيث تصبح الأشياء **آمنة للتداول أو التخلّص منها**."),
 C(["Many factors limit the success or degree of sterilization, disinfection, or decontamination in a health care setting, such as organic load (organisms and other contaminating materials such as blood or body fluids), the type of organisms present, the concentration and exposure time to the germicide, the physical and chemical nature of the surface (hinges, cracks, rough or smooth surfaces),temperature, pH, humidity, and presence of a biofilm.",
    "These processes may be accomplished by a variety of physical or chemical methods."],
   ["تحدّ عوامل كثيرة من نجاح التعقيم أو التطهير أو إزالة التلوّث أو من درجته في مرافق الرعاية الصحية، مثل: **الحمل العضوي** (الكائنات والمواد الملوِّثة الأخرى كالدم أو سوائل الجسم)، ونوع الكائنات الموجودة، و**تركيز مبيد الجراثيم وزمن التعرّض له**، والطبيعة الفيزيائية والكيميائية للسطح (المفصّلات، والشقوق، والسطوح الخشنة أو الملساء)، ودرجة الحرارة، والأس الهيدروجيني (`pH`)، والرطوبة، ووجود **غشاء حيوي** (`biofilm`).",
    "ويمكن إنجاز هذه العمليات بطرق **فيزيائية أو كيميائية** متنوّعة."]),

 SEC("Methods of Sterilization", "طرق التعقيم"),
 L(["Incineration", "Moist heat", "Dry heat", "Filtration", "Ionizing (gamma) radiation",
    "Chemicals (ethylene oxide gas, hydrogen peroxide gas plasma, vaporized hydrogen peroxide, and other liquid chemicals)."],
   ["**الحرق**", "**الحرارة الرطبة**", "**الحرارة الجافة**", "**الترشيح**", "**الإشعاع المؤيِّن** (أشعة كاما)",
    "**المواد الكيميائية** (غاز أوكسيد الإثيلين، وبلازما غاز بيروكسيد الهيدروجين، وبيروكسيد الهيدروجين المُبخَّر، والمواد الكيميائية السائلة الأخرى)."],
   en="The physical methods of sterilization include:", ar="تشمل **الطرق الفيزيائية للتعقيم**:"),
 C("Chemical safety of diagnostic microbiologically laboratory should have a chemical hygiene plan that includes guidelines on proper labeling of chemical containers, manufacturers material safety data sheets (MSDSs), and the written chemical safety training and retraining programs.",
   "**السلامة الكيميائية**: يجب أن تكون لمختبر الأحياء المجهرية التشخيصية **خطة للصحة الكيميائية** تتضمّن إرشادات عن الوسم الصحيح لحاويات المواد الكيميائية، و**صحائف بيانات سلامة المواد** من الشركات المصنّعة (`MSDSs`)، وبرامج التدريب وإعادة التدريب المكتوبة على السلامة الكيميائية."),
 C(["Fire safety is an important component of the laboratory safety program.",
    "Each laboratory is required to post fire evacuation plans that are essentially strategies for finding the nearest exit in case of fire."],
   ["**السلامة من الحريق** مكوّن مهم في برنامج السلامة المختبرية.",
    "ويُطلب من كل مختبر أن يعلّق **خطط الإخلاء عند الحريق**، وهي أساسًا استراتيجيات لإيجاد **أقرب مخرج** في حالة الحريق."]),

 SEC("Electrical safety", "السلامة الكهربائية"),
 C(["Electrical cables should be checked regularly for fraying and replaced when necessary.",
    "All plugs should be the three-prong, grounded type.",
    "All sockets should be checked for electrical grounding and leakage at least annually.",
    "No extension cables should be used in the laboratory."],
   ["يجب فحص **الأسلاك الكهربائية** بانتظام للتأكّد من عدم تآكلها، واستبدالها عند الضرورة.",
    "ويجب أن تكون كل القوابس من النوع **ثلاثي الأطراف المؤرَّض**.",
    "ويجب فحص كل المقابس للتأكّد من **التأريض الكهربائي** وعدم التسرّب **مرة واحدة سنويًا على الأقل**.",
    "ولا يجوز استعمال **أسلاك التمديد** في المختبر."]),

 SEC("Handling of compressed gases", "التعامل مع الغازات المضغوطة"),
 C("Compressed gas cylinders (CO2, anaerobic gas mixture) contain pressurized gases and must be properly handled and secured.",
   "تحتوي **أسطوانات الغاز المضغوط** (ثنائي أوكسيد الكربون `CO2`، وخليط الغاز اللاهوائي) على غازات مضغوطة، ويجب التعامل معها بصورة صحيحة **وتثبيتها بإحكام**."),

 SEC("Biosafety", "السلامة الحيوية"),
 C("Individuals are exposed in various ways to laboratory acquired infections in microbiology laboratories, through that risks from a microbiology laboratory may extend to adjacent laboratories and to the families of those who work in the microbiology laboratory.",
   "يتعرّض الأفراد بطرق مختلفة إلى **العدوى المكتسبة من المختبر** في مختبرات الأحياء المجهرية، وقد تمتدّ مخاطر مختبر الأحياء المجهرية إلى **المختبرات المجاورة** وإلى **عائلات العاملين** فيه."),
 L(["Rubbing the eyes or nose with contaminated hands",
    "Inhaling aerosols produced during centrifugation, mixing with a vortex, or spills of liquid cultures",
    "Accidentally ingesting microorganisms by putting pens or fingers in the mouth",
    "Receiving percutaneous inoculation (i.e., through puncture from an accidental needle stick)",
    "Manipulating or opening bacterial cultures in liquid media or on plates, creating potentially hazardous aerosols,outside of a biosafety hood",
    "Failure to wash hands upon leaving the restroom or other public areas before entering the laboratory"],
   ["**فرك العينين أو الأنف** بأيدٍ ملوّثة",
    "**استنشاق الرذاذ** (`aerosols`) الناتج أثناء النبذ المركزي، أو الخلط بجهاز الدوّامة (`vortex`)، أو انسكاب المزارع السائلة",
    "**ابتلاع الكائنات الدقيقة عرضًا** بوضع الأقلام أو الأصابع في الفم",
    "**التلقيح عبر الجلد** (أي من خلال وخزة إبرة عرضية)",
    "التعامل مع المزارع البكتيرية في الأوساط السائلة أو على الأطباق أو فتحها، مما يولّد رذاذًا قد يكون خطرًا، **خارج خزانة السلامة الحيوية**",
    "**عدم غسل اليدين** عند مغادرة دورة المياه أو الأماكن العامة الأخرى قبل دخول المختبر"],
   en="**Individuals are exposed in various ways to health care– associated infections, transporting specimens and in public areas such as elevators or cafeterias, by:**",
   ar="**يتعرّض الأفراد بطرق مختلفة إلى العدوى المرتبطة بالرعاية الصحية، وعند نقل العيّنات، وفي الأماكن العامة مثل المصاعد أو الكافتيريات، وذلك عن طريق:**"),
 F("autoclave-bags.jpg", "Figure (2 ):Autoclave bags.", "الشكل (2): أكياس جهاز التعقيم بالبخار (الأوتوكليف).", h="48mm", fit="contain", nonum=True),
 C(["Microbiologists should wear laboratory coats over their street clothes, and these coats should be removed before leaving the laboratory.",
    "Most exposures to blood-containing fluids occur on the hands or forearms, so gowns with closed wrists or forearm covers and gloves that cover all potentially exposed skin on the arms are most beneficial."],
   ["يجب أن يرتدي العاملون في الأحياء المجهرية **صدريات المختبر** فوق ملابسهم الاعتيادية، وأن يخلعوها **قبل مغادرة المختبر**.",
    "معظم حالات التعرّض للسوائل الحاوية على الدم تحدث على **اليدين أو الساعدين**، لذا فإن الأردية **مغلقة المعصمين** أو أغطية الساعد، والقفازات التي تغطّي كل الجلد المعرّض على الذراعين هي الأكثر فائدة."]),
 C(["If the laboratory protective clothing becomes contaminated with body fluids or potential pathogens, it should be sterilized in an autoclave immediately and cleaned before reusing.",
    "The institution or a uniform agency should clean laboratory coats; it is no longer permissible for microbiologists to launder their own coats.",
    "Alternatively, disposable gowns may be use."],
   ["إذا تلوّثت الملابس الواقية المختبرية بسوائل الجسم أو بمُمرِضات محتملة، فيجب **تعقيمها في جهاز الأوتوكليف فورًا** وتنظيفها قبل إعادة استعمالها.",
    "يجب أن تتولّى **المؤسسة أو جهة مختصّة بالأزياء** تنظيف صدريات المختبر؛ إذ **لم يعد مسموحًا** للعاملين في الأحياء المجهرية أن يغسلوا صدرياتهم بأنفسهم.",
    "وبدلًا من ذلك، يمكن استعمال **أردية تُستعمل لمرة واحدة**."]),
]

# ---------------------------------------------------------------- questions (lecture content only)
LET = list("abcd") * 7
random.Random(9).shuffle(LET)
_n = [0]
def Q(en, ar, right, wrong, **k):
    """right = (en, ar); wrong = 3 x (en, ar); the right option goes to the next balanced letter."""
    ans = LET[_n[0]]; _n[0] += 1
    opts = list(wrong); opts.insert("abcd".index(ans), right)
    return dict(en=en, ar=ar, options=[list(o) for o in opts], answer=ans, **k)

mcq = [
 {"topic_en": "Laboratory safety and safety programs", "topic_ar": "السلامة في المختبر وبرامج السلامة"},
 Q("To moisten specimen labels, microbiology laboratory admonitions say to use:", "لترطيب ملصقات العيّنات، تنصّ تحذيرات مختبر الأحياء المجهرية على استعمال:",
   ("Water", "الماء"), [("The tongue", "اللسان"), ("Alcohol", "الكحول"), ("Disinfectant", "المطهّر")]),
 Q("All instruments in the microbiology laboratory should be disinfected:", "يجب تطهير كل الأدوات في مختبر الأحياء المجهرية:",
   ("Immediately after use", "فور استعمالها"), [("Once a week", "مرة أسبوعيًا"), ("Before use only", "قبل الاستعمال فقط"), ("At the end of the month", "في نهاية الشهر")]),
 Q("All accidents or exposures to infectious agents should be:", "كل الحوادث أو حالات التعرّض للعوامل المعدية يجب:",
   ("Reported to appropriate personnel", "إبلاغ الأشخاص المختصّين بها"),
   [("Ignored if minor", "تجاهلها إن كانت بسيطة"), ("Reported to the patient", "إبلاغ المريض بها"), ("Recorded only at the end of the year", "تسجيلها في نهاية السنة فقط")]),
 Q("All contaminated waste should be:", "كل النفايات الملوّثة يجب:",
   ("Disinfected before discarding", "تطهيرها قبل التخلّص منها"),
   [("Discarded directly", "التخلّص منها مباشرة"), ("Stored in the laboratory", "خزنها في المختبر"), ("Washed with water only", "غسلها بالماء فقط")]),
 Q("Safety programs have been expanded to include all of the following EXCEPT:", "وُسّعت برامج السلامة لتشمل كل ما يأتي عدا:",
   ("Choosing the antibiotic for the patient", "اختيار المضاد الحيوي للمريض"),
   [("Fire and electrical safety", "السلامة من الحريق والكهرباء"), ("Safe handling of radioactive substances", "التعامل الآمن مع المواد المشعّة"),
    ("Techniques for safely lifting heavy objects", "تقنيات رفع الأجسام الثقيلة بأمان")]),

 {"topic_en": "Sterilization, disinfection and decontamination", "topic_ar": "التعقيم والتطهير وإزالة التلوّث"},
 Q("A process that kills all forms of microbial life, including bacterial endospores, is:", "العملية التي تقتل كل أشكال الحياة الميكروبية بما فيها الأبواغ الداخلية البكتيرية هي:",
   ("Sterilization", "التعقيم"), [("Disinfection", "التطهير"), ("Decontamination", "إزالة التلوّث"), ("Filtration only", "الترشيح فقط")]),
 Q("Disinfection destroys:", "التطهير يُتلف:",
   ("Pathogenic organisms, but not necessarily all microorganisms, endospores, or prions", "الكائنات المُمرِضة، ولكن ليس بالضرورة كل الكائنات الدقيقة أو الأبواغ أو البريونات"),
   [("All forms of microbial life", "كل أشكال الحياة الميكروبية"), ("Prions only", "البريونات فقط"), ("Endospores only", "الأبواغ الداخلية فقط")]),
 Q("Some disinfectants will kill endospores with:", "بعض المطهّرات تقتل الأبواغ الداخلية عند:",
   ("Prolonged exposure times", "إطالة زمن التعرّض"), [("Short exposure times", "تقصير زمن التعرّض"), ("Low temperature only", "انخفاض الحرارة فقط"), ("Dilution with water", "التخفيف بالماء")]),
 Q("Removal of pathogenic microorganisms so items are safe to handle or dispose of is:", "إزالة الكائنات المُمرِضة بحيث تصبح الأشياء آمنة للتداول أو التخلّص منها هي:",
   ("Decontamination", "إزالة التلوّث"), [("Sterilization", "التعقيم"), ("Incineration", "الحرق"), ("Inoculation", "التلقيح")]),
 Q("Which is NOT listed among the factors limiting the success of sterilization or disinfection?", "أيّ ممّا يأتي لم يُذكر ضمن العوامل التي تحدّ من نجاح التعقيم أو التطهير؟",
   ("Colour of the laboratory walls", "لون جدران المختبر"),
   [("Organic load", "الحمل العضوي"), ("Presence of a biofilm", "وجود غشاء حيوي"), ("Concentration and exposure time to the germicide", "تركيز مبيد الجراثيم وزمن التعرّض له")]),
 Q("Organic load includes organisms and other contaminating materials such as:", "يشمل الحمل العضوي الكائنات والمواد الملوِّثة الأخرى مثل:",
   ("Blood or body fluids", "الدم أو سوائل الجسم"), [("Ethylene oxide gas", "غاز أوكسيد الإثيلين"), ("Autoclave bags", "أكياس الأوتوكليف"), ("Gloves", "القفازات")]),

 {"topic_en": "Methods of sterilization", "topic_ar": "طرق التعقيم"},
 Q("Which of the following is listed among the methods of sterilization?", "أيّ ممّا يأتي ذُكر ضمن طرق التعقيم؟",
   ("Incineration", "الحرق"), [("Vortex mixing", "الخلط بالدوّامة"), ("Centrifugation", "النبذ المركزي"), ("Refrigeration", "التبريد")]),
 Q("Ionizing radiation used for sterilization is:", "الإشعاع المؤيِّن المستعمل في التعقيم هو:",
   ("Gamma radiation", "أشعة كاما"), [("Infrared", "الأشعة تحت الحمراء"), ("Visible light", "الضوء المرئي"), ("Radio waves", "موجات الراديو")]),
 Q("Which of the following is a chemical used for sterilization in the lecture?", "أيّ ممّا يأتي مادة كيميائية للتعقيم مذكورة في المحاضرة؟",
   ("Ethylene oxide gas", "غاز أوكسيد الإثيلين"), [("Carbon dioxide", "ثنائي أوكسيد الكربون"), ("Glycerol", "الغليسيرول"), ("Saline", "المحلول الملحي")]),
 Q("Hydrogen peroxide is used for sterilization as:", "يُستعمل بيروكسيد الهيدروجين في التعقيم على شكل:",
   ("Gas plasma or vaporized hydrogen peroxide", "بلازما غازية أو بيروكسيد هيدروجين مُبخَّر"),
   [("Tablets only", "أقراص فقط"), ("Powder only", "مسحوق فقط"), ("It is not mentioned", "لم يُذكر")]),

 {"topic_en": "Chemical, fire and electrical safety, compressed gases", "topic_ar": "السلامة الكيميائية والحريق والكهرباء والغازات المضغوطة"},
 Q("The chemical hygiene plan includes guidelines on:", "تتضمّن خطة الصحة الكيميائية إرشادات عن:",
   ("Proper labeling of chemical containers and MSDSs", "الوسم الصحيح لحاويات المواد الكيميائية وصحائف بيانات السلامة"),
   [("Fire evacuation plans", "خطط الإخلاء عند الحريق"), ("Three-prong plugs", "القوابس ثلاثية الأطراف"), ("Laundering laboratory coats", "غسل صدريات المختبر")]),
 Q("MSDSs stands for:", "يرمز `MSDSs` إلى:",
   ("Material safety data sheets", "صحائف بيانات سلامة المواد"),
   [("Microbiology safety data systems", "أنظمة بيانات سلامة الأحياء المجهرية"), ("Medical specimen data sheets", "صحائف بيانات العيّنات الطبية"),
    ("Material sterilization data sheets", "صحائف بيانات تعقيم المواد")]),
 Q("Fire evacuation plans are essentially strategies for:", "خطط الإخلاء عند الحريق هي أساسًا استراتيجيات لـ:",
   ("Finding the nearest exit in case of fire", "إيجاد أقرب مخرج في حالة الحريق"),
   [("Extinguishing all fires", "إطفاء كل الحرائق"), ("Storing chemicals", "خزن المواد الكيميائية"), ("Checking sockets", "فحص المقابس")]),
 Q("All plugs in the laboratory should be:", "يجب أن تكون كل القوابس في المختبر:",
   ("The three-prong, grounded type", "من النوع ثلاثي الأطراف المؤرَّض"),
   [("Two-prong type", "ثنائية الأطراف"), ("Connected to extension cables", "موصولة بأسلاك تمديد"), ("Ungrounded", "غير مؤرَّضة")]),
 Q("Sockets should be checked for electrical grounding and leakage at least:", "يجب فحص المقابس للتأريض والتسرّب على الأقل:",
   ("Annually", "سنويًا"), [("Every 10 years", "كل 10 سنوات"), ("Never", "أبدًا"), ("Only when broken", "عند عطلها فقط")]),
 Q("Which of the following should NOT be used in the laboratory?", "أيّ ممّا يأتي لا يجوز استعماله في المختبر؟",
   ("Extension cables", "أسلاك التمديد"), [("Grounded plugs", "القوابس المؤرَّضة"), ("Gloves", "القفازات"), ("Biosafety hood", "خزانة السلامة الحيوية")]),
 Q("Compressed gas cylinders mentioned in the lecture contain:", "أسطوانات الغاز المضغوط المذكورة في المحاضرة تحتوي على:",
   ("CO2 and anaerobic gas mixture", "ثنائي أوكسيد الكربون وخليط الغاز اللاهوائي"),
   [("Ethylene oxide only", "أوكسيد الإثيلين فقط"), ("Hydrogen peroxide", "بيروكسيد الهيدروجين"), ("Oxygen only", "الأوكسجين فقط")]),

 {"topic_en": "Biosafety", "topic_ar": "السلامة الحيوية"},
 Q("Risks from a microbiology laboratory may extend to:", "قد تمتدّ مخاطر مختبر الأحياء المجهرية إلى:",
   ("Adjacent laboratories and the families of those who work in it", "المختبرات المجاورة وعائلات العاملين فيه"),
   [("No one outside the laboratory", "لا أحد خارج المختبر"), ("Patients' blood groups", "فصائل دم المرضى"), ("Fire evacuation plans", "خطط الإخلاء")]),
 Q("Inhaling aerosols may occur during:", "قد يحدث استنشاق الرذاذ أثناء:",
   ("Centrifugation, mixing with a vortex, or spills of liquid cultures", "النبذ المركزي أو الخلط بالدوّامة أو انسكاب المزارع السائلة"),
   [("Washing hands", "غسل اليدين"), ("Wearing gloves", "ارتداء القفازات"), ("Reading MSDSs", "قراءة صحائف بيانات السلامة")]),
 Q("Percutaneous inoculation means exposure through:", "التلقيح عبر الجلد يعني التعرّض من خلال:",
   ("Puncture from an accidental needle stick", "وخزة إبرة عرضية"),
   [("Inhaling aerosols", "استنشاق الرذاذ"), ("Rubbing the eyes", "فرك العينين"), ("Putting pens in the mouth", "وضع الأقلام في الفم")]),
 Q("Most exposures to blood-containing fluids occur on:", "معظم حالات التعرّض للسوائل الحاوية على الدم تحدث على:",
   ("The hands or forearms", "اليدين أو الساعدين"), [("The feet", "القدمين"), ("The back", "الظهر"), ("The hair", "الشعر")]),
 Q("Contaminated laboratory protective clothing should be:", "الملابس الواقية المختبرية الملوّثة يجب:",
   ("Sterilized in an autoclave immediately and cleaned before reusing", "تعقيمها في الأوتوكليف فورًا وتنظيفها قبل إعادة الاستعمال"),
   [("Laundered at home by the microbiologist", "غسلها في البيت من قبل العامل"), ("Worn until the end of the week", "ارتداؤها حتى نهاية الأسبوع"),
    ("Discarded in the street", "رميها خارجًا")]),

 {"topic_en": "Picture questions", "topic_ar": "أسئلة الصور"},
 Q("Figure (2) shows:", "يبيّن الشكل (2):",
   ("Autoclave bags", "أكياس جهاز الأوتوكليف"),
   [("Compressed gas cylinders", "أسطوانات الغاز المضغوط"), ("Biosafety hood", "خزانة السلامة الحيوية"), ("Laboratory coats", "صدريات المختبر")],
   img="assets/autoclave-bags.jpg", img_h="36mm"),
]

tf = [
 TF("Specimen labels should be moistened with the tongue.", "يجب ترطيب ملصقات العيّنات باللسان.", "F"),
 TF("Hands should be washed after working with infectious materials.", "يجب غسل اليدين بعد العمل بالمواد المعدية.", "T"),
 TF("Sterilization kills all forms of microbial life, including bacterial endospores.", "التعقيم يقتل كل أشكال الحياة الميكروبية بما فيها الأبواغ الداخلية البكتيرية.", "T"),
 TF("Disinfection always destroys all microorganisms, endospores and prions.", "التطهير يُتلف دائمًا كل الكائنات الدقيقة والأبواغ والبريونات.", "F"),
 TF("Presence of a biofilm limits the success of sterilization and disinfection.", "وجود غشاء حيوي يحدّ من نجاح التعقيم والتطهير.", "T"),
 TF("Refrigeration is listed among the methods of sterilization.", "التبريد من طرق التعقيم المذكورة.", "F"),
 TF("Ethylene oxide is used for sterilization as a liquid only.", "يُستعمل أوكسيد الإثيلين في التعقيم سائلًا فقط.", "F"),
 TF("Extension cables may be used in the laboratory.", "يجوز استعمال أسلاك التمديد في المختبر.", "F"),
 TF("Electrical cables should be checked regularly for fraying.", "يجب فحص الأسلاك الكهربائية بانتظام للتأكّد من عدم تآكلها.", "T"),
 TF("Compressed gas cylinders must be properly handled and secured.", "يجب التعامل مع أسطوانات الغاز المضغوط بصورة صحيحة وتثبيتها.", "T"),
 TF("Laboratory coats may be worn when leaving the laboratory.", "يجوز ارتداء صدريات المختبر عند مغادرته.", "F"),
 TF("Microbiologists are allowed to launder their own coats.", "يُسمح للعاملين في الأحياء المجهرية بغسل صدرياتهم بأنفسهم.", "F"),
 TF("Disposable gowns may be used as an alternative.", "يمكن استعمال أردية لمرة واحدة بديلًا.", "T"),
 TF("Opening bacterial cultures outside a biosafety hood can create hazardous aerosols.", "فتح المزارع البكتيرية خارج خزانة السلامة الحيوية قد يولّد رذاذًا خطرًا.", "T"),
]

traps = [
 TR("Sterilization and disinfection mean the same thing.", "التعقيم والتطهير يعنيان الشيء نفسه.",
    "No — sterilization kills all forms of microbial life including endospores; disinfection destroys pathogenic organisms but not necessarily all microorganisms, endospores, or prions.",
    "لا — التعقيم يقتل كل أشكال الحياة الميكروبية بما فيها الأبواغ، أمّا التطهير فيُتلف الكائنات المُمرِضة وليس بالضرورة كل الكائنات أو الأبواغ أو البريونات."),
 TR("No disinfectant can ever kill endospores.", "لا يوجد مطهّر يمكنه قتل الأبواغ الداخلية.",
    "No — some disinfectants will kill endospores with prolonged exposure times.",
    "لا — بعض المطهّرات تقتل الأبواغ الداخلية عند إطالة زمن التعرّض."),
 TR("Decontamination kills all microbial life.", "إزالة التلوّث تقتل كل الحياة الميكروبية.",
    "No — it is the removal of pathogenic microorganisms so items are safe to handle or dispose of.",
    "لا — هي إزالة الكائنات الدقيقة المُمرِضة بحيث تصبح الأشياء آمنة للتداول أو التخلّص منها."),
 TR("Contaminated lab coats can be taken home to be washed.", "يمكن أخذ الصدريات الملوّثة إلى البيت لغسلها.",
    "No — they are sterilized in an autoclave immediately; the institution or a uniform agency cleans lab coats; laundering your own coat is no longer permissible.",
    "لا — تُعقّم فورًا في الأوتوكليف، وتتولّى المؤسسة أو جهة مختصّة تنظيف الصدريات؛ ولم يعد مسموحًا أن يغسلها العامل بنفسه."),
 TR("Two-prong plugs and extension cables are acceptable in the laboratory.", "القوابس ثنائية الأطراف وأسلاك التمديد مقبولة في المختبر.",
    "No — all plugs should be the three-prong, grounded type, and no extension cables should be used.",
    "لا — يجب أن تكون كل القوابس ثلاثية الأطراف مؤرَّضة، ولا تُستعمل أسلاك التمديد."),
 TR("Lab-acquired infection risks stay inside the microbiology laboratory.", "مخاطر العدوى المكتسبة من المختبر تبقى داخل مختبر الأحياء المجهرية.",
    "No — they may extend to adjacent laboratories and to the families of those who work there.",
    "لا — قد تمتدّ إلى المختبرات المجاورة وإلى عائلات العاملين فيه."),
 TR("Sockets need to be checked for grounding only when they break.", "تُفحص المقابس للتأريض عند عطلها فقط.",
    "No — at least annually, for electrical grounding and leakage.",
    "لا — مرة سنويًا على الأقل، للتأريض الكهربائي والتسرّب."),
]

important = [
 IM("List the admonitions of the microbiology laboratory.", "عدّد تحذيرات مختبر الأحياء المجهرية.",
    "(1) wear gloves, (2) wash hands after working with infectious materials, (3) disinfect all instruments immediately after use, (4) use water to moisten specimen labels rather than the tongue, (5) disinfect all contaminated waste before discarding, (6) report to appropriate personnel all accidents or exposures to infectious agents.",
    "(1) ارتداء القفازات، (2) غسل اليدين بعد العمل بالمواد المعدية، (3) تطهير كل الأدوات فور استعمالها، (4) استعمال الماء لترطيب ملصقات العيّنات بدل اللسان، (5) تطهير كل النفايات الملوّثة قبل التخلّص منها، (6) إبلاغ المختصّين بكل الحوادث أو حالات التعرّض."),
 IM("Define sterilization, disinfection and decontamination.", "عرّف التعقيم والتطهير وإزالة التلوّث.",
    "Sterilization kills all forms of microbial life, including bacterial endospores. Disinfection destroys pathogenic organisms, but not necessarily all microorganisms, endospores, or prions. Decontamination is the removal of pathogenic microorganisms so items are safe to handle or dispose of.",
    "التعقيم يقتل كل أشكال الحياة الميكروبية بما فيها الأبواغ الداخلية البكتيرية. التطهير يُتلف الكائنات المُمرِضة وليس بالضرورة كل الكائنات الدقيقة أو الأبواغ أو البريونات. إزالة التلوّث هي إزالة الكائنات المُمرِضة بحيث تصبح الأشياء آمنة للتداول أو التخلّص منها."),
 IM("Mention the factors that limit the success of sterilization, disinfection, or decontamination.", "اذكر العوامل التي تحدّ من نجاح التعقيم أو التطهير أو إزالة التلوّث.",
    "Organic load, the type of organisms present, the concentration and exposure time to the germicide, the physical and chemical nature of the surface, temperature, pH, humidity, and presence of a biofilm.",
    "الحمل العضوي، ونوع الكائنات الموجودة، وتركيز مبيد الجراثيم وزمن التعرّض له، والطبيعة الفيزيائية والكيميائية للسطح، ودرجة الحرارة، والأس الهيدروجيني، والرطوبة، ووجود غشاء حيوي."),
 IM("List the methods of sterilization.", "عدّد طرق التعقيم.",
    "Incineration, moist heat, dry heat, filtration, ionizing (gamma) radiation, chemicals (ethylene oxide gas, hydrogen peroxide gas plasma, vaporized hydrogen peroxide, and other liquid chemicals).",
    "الحرق، والحرارة الرطبة، والحرارة الجافة، والترشيح، والإشعاع المؤيِّن (أشعة كاما)، والمواد الكيميائية (غاز أوكسيد الإثيلين، وبلازما غاز بيروكسيد الهيدروجين، وبيروكسيد الهيدروجين المُبخَّر، والمواد الكيميائية السائلة الأخرى)."),
 IM("What are the rules of electrical safety in the laboratory?", "ما قواعد السلامة الكهربائية في المختبر؟",
    "Check cables regularly for fraying and replace when necessary; all plugs three-prong, grounded; check sockets for grounding and leakage at least annually; no extension cables.",
    "فحص الأسلاك بانتظام واستبدالها عند الحاجة؛ كل القوابس ثلاثية الأطراف مؤرَّضة؛ فحص المقابس للتأريض والتسرّب سنويًا على الأقل؛ عدم استعمال أسلاك التمديد."),
 IM("How are individuals exposed to infections in the laboratory?", "كيف يتعرّض الأفراد للعدوى في المختبر؟",
    "Rubbing the eyes or nose with contaminated hands; inhaling aerosols (centrifugation, vortex, spills); accidentally ingesting microorganisms (pens or fingers in the mouth); percutaneous inoculation (needle stick); manipulating or opening cultures outside a biosafety hood; failure to wash hands before entering the laboratory.",
    "فرك العينين أو الأنف بأيدٍ ملوّثة؛ استنشاق الرذاذ (النبذ المركزي، الدوّامة، الانسكاب)؛ ابتلاع الكائنات عرضًا (الأقلام أو الأصابع في الفم)؛ التلقيح عبر الجلد (وخزة إبرة)؛ التعامل مع المزارع أو فتحها خارج خزانة السلامة الحيوية؛ عدم غسل اليدين قبل دخول المختبر."),
 IM("What are the rules for laboratory coats and protective clothing?", "ما قواعد صدريات المختبر والملابس الواقية؟",
    "Wear coats over street clothes and remove them before leaving; gowns with closed wrists or forearm covers and gloves covering exposed skin; contaminated clothing is sterilized in an autoclave immediately and cleaned before reuse; the institution or a uniform agency cleans coats; disposable gowns may be used.",
    "تُرتدى الصدريات فوق الملابس وتُخلع قبل المغادرة؛ أردية مغلقة المعصمين أو أغطية ساعد وقفازات تغطّي الجلد المعرّض؛ الملابس الملوّثة تُعقّم فورًا في الأوتوكليف وتُنظّف قبل إعادة استعمالها؛ المؤسسة أو جهة مختصّة تنظّف الصدريات؛ ويمكن استعمال أردية لمرة واحدة."),
]

meta = dict(subject_en="Diagnostic Microbiology", subject_ar="الأحياء المجهرية التشخيصية", short_ar="بكتريا",
            unit_en="Lecture 2", unit_ar="المحاضرة 2", unit_label="LEC", unit_no="2",
            title_en="Laboratory Safety", title_ar="السلامة في المختبر",
            kind="Theory — نظري", stage="The fourth stage — الرابعة", instructor="د. عدنان",
            file_name="بكتريا نظري المحاضرة الثانية", questions_suffix=" اسئلة")   # user-chosen file names

folder = "microbiology-lec2-laboratory-safety"
qs = [q for q in mcq if "answer" in q]
print(folder, len(qs), dict(Counter(q["answer"] for q in qs)), len(tf),
      dict(Counter(t["answer"] for t in tf)), len(traps), len(important))
d = os.path.dirname(os.path.abspath(__file__))
json.dump({"meta": meta, "blocks": blocks,
           "questions": {"mcq": mcq, "tf": tf, "traps": traps, "important": important}},
          open(os.path.join(d, "lecture.json"), "w"), ensure_ascii=False, indent=1)
