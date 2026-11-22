import sys, json, os, shutil
from collections import Counter
WORK = "/home/claude/scratch/work"
sys.path.insert(0, WORK + "/bac"); from bal import balance
sys.path.insert(0, WORK); from bidi import ltr_all

# Diagnostic Microbiology — PRACTICAL Lab 1 (stage 4, د. هبة سامي): Rules and biosafety levels.
# Source 2026-11-22: the same 12-slide deck as lab1-biosafety/, a copy annotated in class (Abdullah Khalid's marks:
# «مهم», «MCQ / T.F», «كلش مهم» on the risk-group table and the four definitions; slide 11 — Biological laboratory /
# Bio risk / Bio risk assessment — crossed out «حذف» → NOT asked). User chose: comprehensive MCQ bank WITH pictures.
# Pictures = the clean copies already in lab1-biosafety/assets (the new scan carries handwriting).
# Correct option written first ("a"), then balance() spreads the keys.

def Q(en, ar, opts, why_en, why_ar, img=None, h="40mm", fixed=None):
    # fixed: the key is set after balance() and the options stay in place ("All of the above" must stay last)
    d = dict(en=en, ar=ar, options=[list(o) for o in opts], note_en=why_en, note_ar=why_ar)
    if fixed: d["_fixed"] = fixed
    else: d["answer"] = "a"
    if img: d.update(img="assets/" + img, img_h=h)
    return d
def T(en, ar): return {"topic_en": en, "topic_ar": ar}
ALL = ("All of the above", "جميع ما سبق")
S = lambda x: f"__{x}__"

mcq = [
 T("Biosafety levels", "مستويات السلامة الحيوية"),
 Q("Biosafety levels are principles and application used to protect:", "مستويات السلامة الحيوية مبادئ وتطبيقات تُستعمل لحماية:",
   [("Laboratory workers and the surrounding environment from exposure to danger while working with living organisms", "العاملين في المختبر والبيئة المحيطة من التعرّض للخطر أثناء العمل مع الكائنات الحيّة"),
    ("Laboratory equipment from damage", "أجهزة المختبر من التلف"), ("Culture media from drying", "الأوساط الزرعية من الجفاف"),
    ("Patients' records from loss", "سجلات المرضى من الضياع")],
   "Definition on the slide: workers + surrounding environment, while working with living organisms.",
   "التعريف في الشريحة: العاملون + البيئة المحيطة، أثناء العمل مع الكائنات الحيّة."),
 Q("Biosafety levels aim to provide:", "تهدف مستويات السلامة الحيوية إلى توفير:",
   [("The highest level of protection and the lowest range of exposure", "أعلى مستوى من الحماية وأدنى مدى من التعرّض"),
    ("The lowest level of protection and the highest range of exposure", "أدنى مستوى من الحماية وأعلى مدى من التعرّض"),
    ("The fastest laboratory results", "أسرع النتائج المختبرية"), ("The cheapest laboratory work", "أرخص عمل مختبري")],
   "Marked “T.F / MCQ” in class: highest protection, lowest exposure.",
   "مؤشَّر عليها «T.F / MCQ» بالمحاضرة: أعلى حماية وأقل تعرّض."),

 T("Risk groups", "مجموعات الخطورة"),
 Q("Risk groups are used to:", "تُستعمل مجموعات الخطورة لـ:",
   [("Assess risk, determine its source and how to deal with it", "تقييم الخطر وتحديد مصدره وكيفية التعامل معه"),
    ("Classify culture media", "تصنيف الأوساط الزرعية"), ("Stain bacteria", "تصبيغ البكتيريا"), ("Sterilize instruments", "تعقيم الأدوات")],
   "Slide 3: assess the risk, its source, and how to deal with it.", "الشريحة 3: تقييم الخطر ومصدره وكيفية التعامل معه."),
 Q("The number of risk groups is:", "عدد مجموعات الخطورة:",
   [("4", "4"), ("3", "3"), ("2", "2"), ("5", "5")],
   "Four groups, each matched to a biosafety level 1–4.", "أربع مجموعات، كل واحدة تقابل مستوى سلامة حيوية من 1 إلى 4."),
 Q("Risk group 1 is described as:", "توصف مجموعة الخطورة 1 بأنها:",
   [("Minimal risk", "خطورة ضئيلة"), ("Moderate risk", "خطورة متوسطة"), ("High risk", "خطورة عالية"), ("Extreme risk", "خطورة قصوى")],
   "1 Minimal · 2 Moderate · 3 High · 4 Extreme.", "1 ضئيلة · 2 متوسطة · 3 عالية · 4 قصوى."),
 Q("Non-pathogenic factors in healthy people and adults (with little or no risk) belong to:", "العوامل غير الممرضة للأشخاص الأصحاء والبالغين (خطورتها قليلة أو معدومة) تنتمي إلى:",
   [("Risk group 1 — Biosafety level 1", "مجموعة الخطورة 1 — مستوى السلامة الحيوية 1"), ("Risk group 2 — Biosafety level 2", "مجموعة الخطورة 2 — مستوى السلامة الحيوية 2"),
    ("Risk group 3 — Biosafety level 3", "مجموعة الخطورة 3 — مستوى السلامة الحيوية 3"), ("Risk group 4 — Biosafety level 4", "مجموعة الخطورة 4 — مستوى السلامة الحيوية 4")],
   "Group 1 = non-pathogenic, little or no risk.", "المجموعة 1 = غير ممرضة، خطورة قليلة أو معدومة."),
 Q("Examples of risk group 1 organisms are:", "أمثلة كائنات مجموعة الخطورة 1:",
   [(S("E. coli") + ", " + S("Bacillus subtilis"), "الإشريكية القولونية، العصوية الرقيقة"),
    (S("Salmonella typhi") + ", " + S("Mycobacterium tuberculosis"), "السالمونيلا التيفية، المتفطّرة السلية"),
    (S("Brucella") + " spp., " + S("Salmonella") + " spp.", "البروسيلا، السالمونيلا"),
    ("Pathogenic " + S("E. coli") + " strain", "السلالة الممرضة من الإشريكية القولونية")],
   "Group 1: E. coli (non-pathogenic) and Bacillus subtilis.", "المجموعة 1: الإشريكية القولونية (غير الممرضة) والعصوية الرقيقة."),
 Q("Factors related to human infection whose treatment is possible (moderate risk and limited risk of spread) belong to:",
   "العوامل المرتبطة بعدوى الإنسان والتي علاجها ممكن (خطورة متوسطة وخطر انتشار محدود) تنتمي إلى:",
   [("Risk group 2", "مجموعة الخطورة 2"), ("Risk group 1", "مجموعة الخطورة 1"), ("Risk group 3", "مجموعة الخطورة 3"), ("Risk group 4", "مجموعة الخطورة 4")],
   "Group 2 key words: treatment is possible + limited spread.", "كلمات المجموعة 2 المفتاحية: العلاج ممكن + انتشار محدود."),
 Q("The pathogenic strain of " + S("E. coli") + ", " + S("Brucella") + " spp. and " + S("Salmonella") + " spp. are examples of:",
   "السلالة الممرضة من الإشريكية القولونية والبروسيلا والسالمونيلا أمثلة على:",
   [("Risk group 2 (moderate risk)", "مجموعة الخطورة 2 (متوسطة)"), ("Risk group 1 (minimal risk)", "مجموعة الخطورة 1 (ضئيلة)"),
    ("Risk group 3 (high risk)", "مجموعة الخطورة 3 (عالية)"), ("Risk group 4 (extreme risk)", "مجموعة الخطورة 4 (قصوى)")],
   "Note: non-pathogenic E. coli is group 1, but its pathogenic strain is group 2.", "انتبه: الإشريكية القولونية غير الممرضة من المجموعة 1، أمّا سلالتها الممرضة فمن المجموعة 2."),
 Q(S("E. coli") + " appears in two risk groups on the slide:", "تظهر الإشريكية القولونية في مجموعتين من مجموعات الخطورة في الشريحة:",
   [("Group 1 (non-pathogenic) and group 2 (pathogenic strain)", "المجموعة 1 (غير الممرضة) والمجموعة 2 (السلالة الممرضة)"),
    ("Group 1 and group 3", "المجموعة 1 والمجموعة 3"), ("Group 2 and group 4", "المجموعة 2 والمجموعة 4"), ("Group 3 and group 4", "المجموعة 3 والمجموعة 4")],
   "The strain decides the group: ordinary E. coli → 1, pathogenic strain → 2.", "السلالة هي التي تحدّد المجموعة: الاعتيادية ← 1، والممرضة ← 2."),
 Q("Factors that cause serious and fatal infections to humans, whose treatment is not easy, especially for immunosuppressed persons, belong to:",
   "العوامل التي تسبّب عدوى خطيرة ومميتة للإنسان وعلاجها ليس سهلًا، ولا سيما لدى المثبَّطين مناعيًّا، تنتمي إلى:",
   [("Risk group 3 (high risk)", "مجموعة الخطورة 3 (عالية)"), ("Risk group 2 (moderate risk)", "مجموعة الخطورة 2 (متوسطة)"),
    ("Risk group 1 (minimal risk)", "مجموعة الخطورة 1 (ضئيلة)"), ("Risk group 4 (extreme risk)", "مجموعة الخطورة 4 (قصوى)")],
   "Group 3 key words: treatment is not easy + immunosuppressed + high risk for individuals.", "كلمات المجموعة 3: العلاج ليس سهلًا + المثبَّطون مناعيًّا + خطورة عالية على الأفراد."),
 Q("Examples of risk group 3 organisms are:", "أمثلة كائنات مجموعة الخطورة 3:",
   [(S("Salmonella typhi") + " and " + S("Mycobacterium tuberculosis"), "السالمونيلا التيفية والمتفطّرة السلية"),
    (S("E. coli") + " and " + S("Bacillus subtilis"), "الإشريكية القولونية والعصوية الرقيقة"),
    (S("Brucella") + " spp. and " + S("Salmonella") + " spp.", "البروسيلا والسالمونيلا"),
    ("Non-pathogenic " + S("E. coli"), "الإشريكية القولونية غير الممرضة")],
   "Group 3: S. typhi and M. tuberculosis.", "المجموعة 3: السالمونيلا التيفية والمتفطّرة السلية."),
 Q("In risk group 3, the risk is described as high for:", "في مجموعة الخطورة 3، توصف الخطورة بأنها عالية على:",
   [("Individuals", "الأفراد"), ("The community only", "المجتمع فقط"), ("Animals only", "الحيوانات فقط"), ("No one", "لا أحد")],
   "Slide: “with a high risk for individuals”.", "الشريحة: «خطورة عالية على الأفراد»."),
 Q("Factors that are fatal to humans and are easily transmitted belong to:", "العوامل المميتة للإنسان وسهلة الانتقال تنتمي إلى:",
   [("Risk group 4 (extreme risk)", "مجموعة الخطورة 4 (قصوى)"), ("Risk group 3 (high risk)", "مجموعة الخطورة 3 (عالية)"),
    ("Risk group 2 (moderate risk)", "مجموعة الخطورة 2 (متوسطة)"), ("Risk group 1 (minimal risk)", "مجموعة الخطورة 1 (ضئيلة)")],
   "The group-4 row is cut off at the bottom of the slide; the class note beside it says “no treatment”.",
   "سطر المجموعة 4 مقطوع أسفل الشريحة، والملاحظة المكتوبة بالمحاضرة يمّه تقول «no treatment» (لا علاج)."),
 Q("Which biosafety level is matched to risk group 3?", "أيّ مستوى سلامة حيوية يقابل مجموعة الخطورة 3؟",
   [("Biosafety level 3", "مستوى السلامة الحيوية 3"), ("Biosafety level 1", "مستوى السلامة الحيوية 1"), ("Biosafety level 2", "مستوى السلامة الحيوية 2"), ("Biosafety level 4", "مستوى السلامة الحيوية 4")],
   "Each risk group has the biosafety level of the same number.", "كل مجموعة خطورة تقابل مستوى السلامة الحيوية بالرقم نفسه."),
 Q("As the risk group number increases from 1 to 4:", "كلّما ازداد رقم مجموعة الخطورة من 1 إلى 4:",
   [("The risk increases and treatment becomes harder", "تزداد الخطورة ويصعب العلاج"), ("The risk decreases", "تقلّ الخطورة"),
    ("Treatment becomes easier", "يصبح العلاج أسهل"), ("The risk stays the same", "تبقى الخطورة نفسها")],
   "Minimal → moderate (treatable) → high (treatment not easy) → extreme (fatal, easily transmitted).",
   "ضئيلة ← متوسطة (العلاج ممكن) ← عالية (العلاج ليس سهلًا) ← قصوى (مميتة وسهلة الانتقال)."),

 T("Biohazard symbol", "رمز الخطر البيولوجي"),
 Q("This symbol is the:", "هذا الرمز هو:",
   [("Biohazard symbol", "رمز الخطر البيولوجي"), ("Radiation hazard symbol", "رمز خطر الإشعاع"), ("Fire hazard symbol", "رمز خطر الحريق"), ("Toxic chemical symbol", "رمز المادة الكيميائية السامّة")],
   "Three interlocking crescents on yellow = biohazard.", "ثلاثة أهلّة متداخلة على أصفر = خطر بيولوجي.", img="biohazard.jpg", h="34mm"),
 Q("This symbol warns of:", "هذا الرمز يحذّر من:",
   [("Radiation hazard", "خطر الإشعاع"), ("Biological hazard", "الخطر البيولوجي"), ("Electrical hazard", "الخطر الكهربائي"), ("Slippery floor", "الأرضية الزلقة")],
   "The trefoil (three blades around a dot) is the radiation hazard sign shown next to the biohazard sign.",
   "رمز الأوراق الثلاث حول نقطة هو علامة خطر الإشعاع المعروضة بجانب رمز الخطر البيولوجي.", img="radiation.jpg", h="34mm"),
 Q("The biohazard symbol is used to:", "يُستعمل رمز الخطر البيولوجي لـ:",
   [("Warn people of the potential presence of dangerous biological materials", "تحذير الناس من احتمال وجود مواد بيولوجية خطرة"),
    ("Mark radioactive materials", "تمييز المواد المشعّة"), ("Mark fire exits", "تمييز مخارج الحريق"), ("Label sterile media", "وسم الأوساط المعقّمة")],
   "Slide 4 definition.", "تعريف الشريحة 4."),
 Q("The biohazard symbol is placed on:", "يوضع رمز الخطر البيولوجي على:",
   [("Cultures of pathogens", "مزارع الممرضات"), ("Human blood and tissue", "دم الإنسان وأنسجته"), ("Corridors leading to the laboratories", "الممرّات المؤدّية إلى المختبرات"), ALL],
   "All three examples are listed on the slide.", "الأمثلة الثلاثة كلها مذكورة في الشريحة.", fixed="d"),
 Q("Which of the following is NOT one of the examples given for the biohazard symbol?", "أيّ مما يأتي ليس من الأمثلة المذكورة لرمز الخطر البيولوجي؟",
   [("Sterile distilled water", "الماء المقطّر المعقّم"), ("Cultures of pathogens", "مزارع الممرضات"), ("Human blood and tissue", "دم الإنسان وأنسجته"), ("Corridors leading to the laboratories", "الممرّات المؤدّية إلى المختبرات")],
   "Sterile water is not a dangerous biological material.", "الماء المعقّم ليس مادة بيولوجية خطرة."),

 T("Laboratory safety considerations", "اعتبارات السلامة في المختبر"),
 Q("The image illustrates which laboratory safety rule?", "توضّح الصورة أيّ قاعدة من قواعد السلامة المختبرية؟",
   [("Wear protective clothing (clean lab coat – gloves – mask – safety glasses)", "ارتدِ الملابس الواقية (صدرية نظيفة – قفازات – كمّامة – نظارات سلامة)"),
    ("Do not eat or drink in the lab", "لا تأكل ولا تشرب في المختبر"), ("Wash hands after work", "اغسل يديك بعد العمل"), ("Tie back long hair", "اربط الشعر الطويل")],
   "Rule 1 with its picture (protective clothing).", "القاعدة 1 مع صورتها (الملابس الواقية).", img="ppe.jpg", h="38mm"),
 Q("Protective clothing in the microbiology lab includes:", "تشمل الملابس الواقية في مختبر الأحياء المجهرية:",
   [("Clean lab coat, gloves, mask and safety glasses", "صدرية مختبر نظيفة، قفازات، كمّامة، نظارات سلامة"), ("Lab coat only", "الصدرية فقط"),
    ("Gloves only", "القفازات فقط"), ("Safety glasses only", "نظارات السلامة فقط")],
   "Rule 1 lists four items.", "القاعدة 1 تعدّد أربعة أشياء."),
 Q("While wearing gloves, you should avoid touching:", "أثناء لبس القفازات يجب تجنّب لمس:",
   [("Pencils, cell phones and door handles", "الأقلام والهواتف ومقابض الأبواب"), ("Culture plates", "أطباق المزارع"),
    ("Specimen containers", "حاويات العيّنات"), ("Microscope slides", "شرائح المجهر")],
   "Rule 2: gloves contaminate everyday objects.", "القاعدة 2: القفازات تلوّث الأشياء اليومية."),
 Q("Pencils, labels or any other materials should:", "الأقلام والملصقات وأيّ مواد أخرى يجب:",
   [("Never be placed in your mouth", "ألّا توضع في الفم أبدًا"), ("Be moistened with saliva", "أن تُرطَّب باللعاب"),
    ("Be shared between students", "أن تُتبادل بين الطلبة"), ("Be left on the bench", "أن تُترك على المنضدة")],
   "Rule 2, second part.", "القاعدة 2، الجزء الثاني."),
 Q("The sign in the image means:", "العلامة في الصورة تعني:",
   [("Do not eat food or drink water in the lab", "لا تتناول الطعام ولا تشرب الماء في المختبر"), ("Food can be stored in the lab fridge", "يمكن حفظ الطعام في ثلاجة المختبر"),
    ("Use lab glassware as cups", "استعمل الزجاجيات المختبرية أكوابًا"), ("Drinking is allowed at the bench", "الشرب مسموح عند المنضدة")],
   "Rule 3 with its picture.", "القاعدة 3 مع صورتها.", img="nofood.jpg", h="34mm"),
 Q("Laboratory glassware:", "الزجاجيات المختبرية:",
   [("Must not be used as food or water containers", "يجب ألّا تُستعمل أوعيةً للطعام أو الماء"), ("May be used for drinking water after washing", "يمكن استعمالها للشرب بعد غسلها"),
    ("May be used for food if sterilized", "يمكن استعمالها للطعام إذا عُقّمت"), ("Can be taken home", "يمكن أخذها إلى البيت")],
   "Rule 3, second part — no exception.", "القاعدة 3، الجزء الثاني — بلا استثناء."),
 Q("Long hair must be tied back or covered to minimize:", "يجب ربط الشعر الطويل أو تغطيته لتقليل:",
   [("Fire hazard or contamination of the experiment", "خطر الحريق أو تلوّث التجربة"), ("Hair loss", "تساقط الشعر"),
    ("Electric shock", "الصدمة الكهربائية"), ("Noise in the lab", "الضوضاء في المختبر")],
   "Rule 4: two reasons — fire and contamination.", "القاعدة 4: سببان — الحريق والتلوّث."),
 Q("Cultures like those in the image must:", "المزارع مثل التي في الصورة يجب:",
   [("Never be taken out of the lab, and be handled as potentially pathogenic", "ألّا تُخرج من المختبر أبدًا، وأن تُعامل على أنها ممرضة محتملة"),
    ("Be taken home for study if covered", "أن تؤخذ إلى البيت للدراسة إذا كانت مغطّاة"), ("Be handled as harmless", "أن تُعامل على أنها غير مؤذية"),
    ("Be discarded without disinfection", "أن يُتخلّص منها دون تطهير")],
   "Rule 5 (marked in class): no culture leaves the lab for any reason.", "القاعدة 5 (مؤشَّرة بالمحاضرة): لا تخرج أي مزرعة من المختبر لأي سبب.", img="cultures.jpg", h="36mm"),
 Q("All cultures in the laboratory should be handled as:", "يجب التعامل مع جميع المزارع في المختبر على أنها:",
   [("Potentially pathogenic", "ممرضة محتملة"), ("Non-pathogenic", "غير ممرضة"), ("Sterile", "معقّمة"), ("Risk group 1 only", "من مجموعة الخطورة 1 فقط")],
   "Rule 5.", "القاعدة 5."),
 Q("Hands must be washed:", "يجب غسل اليدين:",
   [("After working with infectious materials", "بعد العمل مع المواد المعدية"), ("Only before entering the lab", "قبل دخول المختبر فقط"),
    ("Only if gloves were not worn", "فقط إذا لم تُلبس القفازات"), ("Once a day", "مرّة واحدة في اليوم")],
   "Rule 6.", "القاعدة 6.", img="handwash.jpg", h="34mm"),
 Q("All instruments should be disinfected:", "يجب تطهير جميع الأدوات:",
   [("Immediately after use", "فور الانتهاء من استعمالها"), ("At the end of the week", "في نهاية الأسبوع"),
    ("Only when visibly dirty", "فقط عندما تبدو متّسخة"), ("Before use only", "قبل الاستعمال فقط")],
   "Rule 7.", "القاعدة 7."),
 Q("Contaminated waste must be:", "يجب أن تكون النفايات الملوّثة:",
   [("Disinfected before discarding", "مطهَّرة قبل التخلّص منها"), ("Discarded directly with ordinary waste", "تُرمى مباشرةً مع النفايات العادية"),
    ("Stored on the bench", "مخزَّنة على المنضدة"), ("Taken out of the lab", "مُخرَجة من المختبر")],
   "Rule 8 (the picture shows disinfecting instruments and surfaces).", "القاعدة 8 (الصورة تبيّن تطهير الأدوات والأسطح).", img="disinfect.jpg", h="36mm"),
 Q("The number of laboratory safety considerations listed in the lab is:", "عدد اعتبارات السلامة المختبرية المذكورة في العملي:",
   [("8", "8"), ("6", "6"), ("10", "10"), ("4", "4")],
   "Rules 1–8.", "القواعد من 1 إلى 8."),

 T("Sterilization, disinfection, antiseptics, decontamination", "التعقيم والتطهير والمطهرات الموضعية وإزالة التلوّث"),
 Q("The complete killing or removal of all living organisms, such as cell spores, viruses and fungi, is:", "القتل أو الإزالة الكاملة لجميع الكائنات الحيّة، مثل الأبواغ والفيروسات والفطريات، هو:",
   [("Sterilization", "التعقيم"), ("Disinfection", "التطهير"), ("Antiseptics", "المطهرات الموضعية"), ("Decontamination", "إزالة التلوّث")],
   "Sterilization = complete (everything, including spores).", "التعقيم = كامل (كل شيء، حتى الأبواغ)."),
 Q("Disinfection is the destruction or removal of pathogens:", "التطهير هو إتلاف الممرضات أو إزالتها:",
   [("But not bacterial spores", "ولكن ليس الأبواغ البكتيرية"), ("Including bacterial spores", "بما فيها الأبواغ البكتيرية"),
    ("On body surfaces only", "على سطوح الجسم فقط"), ("By washing only", "بالغسل فقط")],
   "The key difference from sterilization (boxed in class): spores survive disinfection.", "الفرق المفتاحي عن التعقيم (مؤطَّر بالمحاضرة): الأبواغ تنجو من التطهير."),
 Q("Disinfection is usually used only on:", "يُستعمل التطهير عادةً على:",
   [("Inanimate objects", "الأجسام غير الحيّة فقط"), ("Body surfaces", "سطوح الجسم"), ("Open wounds", "الجروح المفتوحة"), ("Living tissues", "الأنسجة الحيّة")],
   "Disinfection → objects; antiseptics → body surfaces.", "التطهير ← الأجسام؛ المطهرات الموضعية ← سطوح الجسم."),
 Q("Chemicals applied to body surfaces to destroy or inhibit pathogens are called:", "المواد الكيميائية التي توضع على سطوح الجسم لإتلاف الممرضات أو تثبيطها تُسمّى:",
   [("Antiseptics", "المطهرات الموضعية"), ("Disinfectants", "المطهرات"), ("Sterilants", "المعقِّمات"), ("Decontaminants", "مزيلات التلوّث")],
   "Antiseptics = body surfaces.", "المطهرات الموضعية = سطوح الجسم."),
 Q("The mechanical removal of most microbes by using washing, heat or disinfectants is:", "الإزالة الميكانيكية لمعظم الميكروبات باستعمال الغسل أو الحرارة أو المطهرات هي:",
   [("Decontamination", "إزالة التلوّث"), ("Sterilization", "التعقيم"), ("Antisepsis", "التطهير الموضعي"), ("Disinfection", "التطهير")],
   "Decontamination = mechanical removal of most microbes.", "إزالة التلوّث = إزالة ميكانيكية لمعظم الميكروبات."),
 Q("Decontamination can be done by:", "يمكن إجراء إزالة التلوّث بـ:",
   [("Washing, heat or disinfectants", "الغسل أو الحرارة أو المطهرات"), ("Antibiotics only", "المضادات الحيوية فقط"),
    ("Staining", "التصبيغ"), ("Cooling", "التبريد")],
   "Three means on the slide.", "ثلاث وسائل في الشريحة."),
 Q("Which process kills bacterial spores?", "أيّ عملية تقتل الأبواغ البكتيرية؟",
   [("Sterilization", "التعقيم"), ("Disinfection", "التطهير"), ("Antiseptics", "المطهرات الموضعية"), ("Washing", "الغسل")],
   "Only sterilization kills all life including spores.", "التعقيم وحده يقتل كل أشكال الحياة بما فيها الأبواغ."),

 T("Biosafety cabinet", "خزانة السلامة الحيوية"),
 Q("The last slide shows several types of equipment under the title:", "تعرض الشريحة الأخيرة عدة أنواع من الأجهزة تحت عنوان:",
   [("Biosafety cabinet", "خزانة السلامة الحيوية"), ("Incubator", "الحاضنة"), ("Autoclave", "المؤصدة"), ("Centrifuge", "جهاز الطرد المركزي")],
   "The slide's labels include Class I, II and III biosafety cabinets (an autoclave and incubator also appear in the picture).",
   "تسميات الشريحة تشمل خزانات السلامة الحيوية من الأصناف I وII وIII (وتظهر في الصورة أيضًا مؤصدة وحاضنة).", img="cabinets.jpg", h="50mm"),
]

mcq = balance(mcq, 1101)
for q in mcq:
    if "_fixed" in q: q["answer"] = q.pop("_fixed")

meta = {"subject_en": "Diagnostic Microbiology", "subject_ar": "الأحياء المجهرية التشخيصية", "short_ar": "بكتريا",
        "instructor": "د. هبة سامي", "unit_en": "Lab 1", "unit_ar": "العملي 1", "unit_label": "LAB", "unit_no": "1",
        "title_en": "Rules and Biosafety Levels", "title_ar": "القواعد ومستويات السلامة الحيوية",
        "department": "قسم التحليلات", "kind": "Laboratories — عملي", "questions_kind": "MCQ — أسئلة اختيار",
        "stage": "The fourth stage — الرابعة",
        "file_name": "BIOS - بكتريا عملي المحاضرة الأولى - بنك أسئلة شامل بالصور"}
Qs = {"title_en": "Rules and Biosafety Levels — Comprehensive MCQs (with figures)",
      "title_ar": "القواعد ومستويات السلامة الحيوية — أسئلة اختيار شاملة (مع الصور)",
      "sub": "MCQ", "answers_inline": True, "compact": True, "mcq_per_page": 4,
      "mcq_en": "Comprehensive MCQs — Lab 1", "mcq_ar": "أسئلة اختيار شاملة — العملي الأول",
      "intro_en": ["Q. Select the most correct answer from the followings",
                   "These MCQs cover the whole lab with its own pictures; the answer and a short reason sit under each question. Slide 11 (biological laboratory, bio risk, bio risk assessment) was deleted in class and is not asked."],
      "intro_ar": ["س. اختر الإجابة الأصح مما يأتي",
                   "هذه الأسئلة تغطّي العملي كاملًا بصوره نفسها؛ والحل وسطر سبب مختصر تحت كل سؤال. الشريحة 11 (المختبر البيولوجي، الخطر البيولوجي، تقييم الخطر البيولوجي) حُذفت بالمحاضرة فلم تُسأل."],
      "mcq": ltr_all(mcq), "tf": [], "traps": [], "important": []}

d = "/home/user/-/bacteriology-lab1-mcq"
os.makedirs(d + "/assets", exist_ok=True)
for q in mcq:
    if q.get("img"):
        shutil.copy("/home/user/-/lab1-biosafety/" + q["img"], d + "/" + q["img"])
json.dump({"meta": meta, "questions": Qs}, open(d + "/lecture.json", "w"), ensure_ascii=False, indent=1)
qs = [m for m in mcq if "answer" in m]
print("MCQ:", len(qs), "| dist:", dict(Counter(m["answer"] for m in qs)), "| images:", sum(1 for m in qs if m.get("img")))
