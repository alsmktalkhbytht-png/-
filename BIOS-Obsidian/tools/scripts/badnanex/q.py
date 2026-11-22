import sys, json, os
from collections import Counter
WORK = "/home/claude/scratch/work"
sys.path.insert(0, WORK); from bidi import ltr_all

# Diagnostic Microbiology THEORY (stage 4) — Prof. Dr. Adnan Neamah Albeidani's past exams, MCQ only (user 2026-11-22:
# "ضيف هل اسئلة مال دكتور عدنان وخلي ملاحظه بالبداية اسئلة دكتور عدنان تبدي من الصفحة الفلانية").
# Sources: (1) 2025 exam with the doctor's answer table (Q2/Q3 essays not used — MCQ only); (2) exam dated 2/12/2023 with the doctor's
# underlined keys; (3) 2022 1st attempt — NO key in the file → answered from the lectures (and from the doctor's own keys where the
# same question appears in 1/2). Original order and A–E options kept, no shuffling; spelling typos fixed. In-exam duplicates asked once
# (2025 Q29 = Q10; 2022 Q29 = Q23). Doctor's keys kept even where doubtful — told the user: 2025 Q5 (chocolate agar = E Differential),
# 2025 Q20 (request form = E only A and C), 2023 Q18 (carbohydrates instead of bile salts), "Traditional methods" (2025 = E, 2023 = D),
# bile esculin (D).

def Q(en, ar, opts, key):
    return dict(en=en, ar=ar, options=[list(o) for o in opts], answer=key)
def T(en, ar): return {"topic_en": en, "topic_ar": ar}
S = lambda x: f"__{x}__"
ALL = ("All of the above", "جميع ما سبق"); NONE = ("None of the above", "لا شيء مما سبق")
ALLT = ("All of them", "جميعها"); NONET = ("None of them", "لا شيء منها")

purpose = Q("The purpose of diagnostic microbiology include:", "يشمل غرض الأحياء الدقيقة التشخيصية:",
   [("Confirm the suspicion of infectious diseases", "تأكيد الاشتباه بالأمراض المعدية"), ("Identify the etiological agent", "تحديد العامل المسبِّب"),
    ("Decision on antimicrobial therapy", "اتخاذ قرار العلاج بمضادات الميكروبات"), ("Elimination of the microbes", "القضاء على الميكروبات"), ALL], "e")
fix = lambda last: Q("……… is the process by which the internal and external structures of cells are preserved and fixed on the slide.",
   "……… هو العملية التي تُحفظ بها التراكيب الداخلية والخارجية للخلايا وتُثبَّت على الشريحة.",
   [("Smear technique", "تقنية المسحة"), ("Fixation technique", "تقنية التثبيت"), ("Staining method", "طريقة الصبغ"), ("Latex agglutination technique", "تقنية التلازن باللاتكس"), last], "b")
enriched = lambda a, b: Q("……… media contain additional nutrients for the isolation of more fastidious bacteria like whole blood (blood agar) or agar containing lysed blood (chocolate agar).",
   "……… أوساط تحتوي مغذّيات إضافية لعزل البكتيريا صعبة النمو مثل الدم الكامل (أجار الدم) أو الأجار الحاوي على دم متحلّل (أجار الشوكولاتة).",
   [("Differential", "التفريقية"), ("Nutrient", "المغذّية"), ("Enriched", "الغنية"), a, b], "c")
trypto = lambda n: Q("Ability of the microorganism to degrade the amino acid tryptophan can be detected by:", "يمكن كشف قدرة الكائن الدقيق على تحليل الحمض الأميني تربتوفان بواسطة:",
   [("Catalase test", "اختبار الكاتاليز"), ("Oxidase test", "اختبار الأوكسيديز"), ("Citrate test", "اختبار السترات"), ("Urease test", "اختبار اليوريز"), n], "e")
indole = lambda a, b: Q("Indole test detects when bacteria produce the enzyme tryptophanase which degrades the amino acid tryptophan into ………, ammonia, and indole.",
   "يكشف اختبار الإندول إنتاج البكتيريا لإنزيم التربتوفانيز الذي يحلّل التربتوفان إلى ……… والأمونيا والإندول.",
   [("pyruvic acid", "حمض البيروفيك"), ("lactic acid", "حمض اللاكتيك"), ("acetic acid", "حمض الخليك"), a, b], "a")
negst = lambda c: Q("……… is very useful in the demonstration of bacterial/yeast capsules which do not take up simple stains.", "……… مفيدة جدًّا لإظهار محافظ البكتيريا والخمائر التي لا تأخذ الصبغات البسيطة.",
   [("Microscopy", "الفحص المجهري"), ("Negative stain", "الصبغة السالبة"), c, ALL if c[0] == "Serology" else ("alcohol", "الكحول"), NONE], "b")
tradit = lambda key: Q("Traditional methods for identification of pathogens or their products include:", "تشمل الطرق التقليدية لتشخيص الممرضات أو نواتجها:",
   [("Molecular testing", "التحاليل الجزيئية"), ("Saliva based testing", "تحاليل اللعاب"), ("Chromogenic testing", "تحاليل الكروموجين"), ALL, NONE], key)
catal = lambda a, b: Q("Catalase test is key to the identification scheme of many ……… organisms.", "اختبار الكاتاليز أساسي في مخطط تشخيص كثير من الكائنات ………",
   [("Gram-negative", "سالبة غرام"), ("Gram-positive", "موجبة غرام"), ("Virus", "الفيروسات"), a, b], "b")
msa = lambda a, b: Q("Mannitol salt agar which contains increased ……… for the recovery of staphylococci.", "أجار المانيتول الملحي يحتوي تركيزًا عاليًا من ……… لاستعادة العنقوديات.",
   [("Antibiotics", "المضادات الحيوية"), ("NaCl", "NaCl"), ("Thioglycollate", "الثايوكلايكوليت"), a, b], "b")
abx = lambda a, b: Q("Some antibiotics are additive in media in order to make ………", "تُضاف بعض المضادات الحيوية إلى الأوساط لجعلها ………",
   [("Enrich media", "أوساطًا غنية"), ("Simple media", "أوساطًا بسيطة"), ("Selective media", "أوساطًا انتقائية"), ("Basal media", "أوساطًا أساسية"), ("Transport media", "أوساط نقل")], "c")
urea = lambda n: Q("Bacteria able of hydrolyzing urea to make ammonia and carbon dioxide by:", "البكتيريا القادرة على تحليل اليوريا لإنتاج الأمونيا وثاني أوكسيد الكربون تفعل ذلك بواسطة:",
   [("Catalase enzyme", "إنزيم الكاتاليز"), ("Coagulase enzyme", "إنزيم التخثّر"), ("Oxidase enzyme", "إنزيم الأوكسيديز"), ("Urease enzyme", "إنزيم اليوريز"), n], "d")
bileesc = lambda: Q("Bile esculin test is used to differentiate between:", "يُستعمل اختبار bile esculin للتفريق بين:",
   [(S("Staph. saprophyticus") + " from " + S("Staph. aureus"), "Staph. saprophyticus وStaph. aureus"), (S("Staph. saprophyticus") + " from " + S("Staph. epidermidis"), "Staph. saprophyticus وStaph. epidermidis"),
    (S("Strep. pyogenes") + " from " + S("Strep. agalactiae"), "Strep. pyogenes وStrep. agalactiae"), (S("Strep. pneumoniae") + " from " + S("Strep. mutans"), "Strep. pneumoniae وStrep. mutans"),
    (S("Staph. aureus") + " from " + S("Enterococcus faecium"), "Staph. aureus وEnterococcus faecium")], "d")
pyog = lambda: Q(S("Streptococcus pyogenes") + " growing on a blood agar plate shows which of the following?", "Streptococcus pyogenes النامية على أجار الدم تُظهر أيًّا مما يأتي؟",
   [("Alpha hemolysis, a clear zone surrounding the colonies", "تحلّل ألفا، منطقة صافية حول المستعمرات"), ("Alpha hemolysis, a green zone surrounding the colonies", "تحلّل ألفا، منطقة خضراء حول المستعمرات"),
    ("Beta-hemolysis, a clear zone surrounding the colonies", "تحلّل بيتا، منطقة صافية حول المستعمرات"), ("Beta-hemolysis, a green zone surrounding the colonies", "تحلّل بيتا، منطقة خضراء حول المستعمرات"),
    ("Gamma-hemolysis, a clear zone surrounding the colonies", "تحلّل كاما، منطقة صافية حول المستعمرات")], "c")
choc = lambda: Q("Chocolate agar also called:", "أجار الشوكولاتة يُسمّى أيضًا:",
   [("Blood agar", "أجار الدم"), ("Lysed blood agar", "أجار الدم المتحلّل"), ("Heated blood agar", "أجار الدم المسخَّن"), ("Enriched media", "وسط غني"), ("Differential media", "وسط تفريقي")], "e")
solid = lambda n: Q("One of the following is used for solidifying the culture media:", "واحد مما يأتي يُستعمل لتصليب الوسط الزراعي:",
   [("Peptone", "الببتون"), ("Electrolyte", "الإلكتروليت"), ("NaCl", "NaCl"), ("Carbohydrate", "الكربوهيدرات"), n], "e")
macsel = lambda: Q("MacConkey agar is used for growth only gram negative bacteria, which one of the following media:", "أجار ماكونكي يُستعمل لنمو سالبات غرام فقط، فهو أيّ من الأوساط الآتية:",
   [("Semisolid media", "وسط شبه صلب"), ("Simple media", "وسط بسيط"), ("Enriched media", "وسط غني"), ("Selective media", "وسط انتقائي"), ("Differential media", "وسط تفريقي")], "d")
blood = lambda n: Q("The isolated organism is identified from blood culture by:", "يُشخَّص الكائن المعزول من زرع الدم بواسطة:",
   [("colony morphology", "شكل المستعمرة"), ("Gram staining", "صبغة غرام"), ("Biochemical reactions", "التفاعلات الكيميائية الحيوية"), ALL if n is NONE else ALLT, n], "d")

mcq = [
 T("Exam 2025 — Prof. Dr. Adnan (doctor's answer key)", "امتحان 2025 — أ.د. عدنان (بمفتاح الدكتور)"),
 Q("The principle of sterilization work in an autoclave depends on:", "يعتمد مبدأ عمل التعقيم في الأوتوكلاف على:",
   [("Steam with moist heat", "البخار مع الحرارة الرطبة"), ("Steam with dry heat", "البخار مع الحرارة الجافة"), ("Pressure with moist heat", "الضغط مع الحرارة الرطبة"),
    ("Pressure with dry heat", "الضغط مع الحرارة الجافة"), ("A and C", "A وC")], "e"),
 Q("Refrigeration of sample at ……… can help to preserve cells and reduce the multiplication of commensals in unpreserved specimens.", "تبريد العيّنة عند ……… يساعد على حفظ الخلايا وتقليل تكاثر المتعايشات في العيّنات غير المحفوظة.",
   [("`45 ºC`", "`45 ºC`"), ("`37 ºC`", "`37 ºC`"), ("`4 ºC`", "`4 ºC`"), ALL, NONE], "c"),
 trypto(NONE),
 Q("In gram positive, cells retain the ……… stain and remain purple to dark blue.", "في موجبات غرام تحتفظ الخلايا بصبغة ……… وتبقى بنفسجية إلى زرقاء داكنة.",
   [("Crystal violet", "البنفسج البلوري"), ("Decolorizing", "مزيل اللون"), ("Safranin", "السفرانين"), ("Iodine solution", "محلول اليود"), NONE], "a"),
 choc(),
 tradit("e"),
 enriched(ALL, NONE),
 solid(NONE),
 fix(ALL),
 purpose,
 macsel(),
 blood(NONE),
 catal(("A & B", "A وB"), NONE),
 Q("One of these methods does not destroy bacteria:", "إحدى هذه الطرق لا تُتلف البكتيريا:",
   [("Disinfection", "التطهير"), ("Filtration", "الترشيح"), ("Boiling", "الغلي"), ("Sterilization", "التعقيم"), NONE], "b"),
 Q("Bactericidal means:", "معنى قاتل للبكتيريا (bactericidal):",
   [("Inhibition of bacterial growth", "تثبيط نمو البكتيريا"), ("Different antibiotic used", "استعمال مضاد حيوي مختلف"), ("Killed all bacterial life", "قتل كل الحياة البكتيرية"),
    ("Stops bacterial growth", "إيقاف نمو البكتيريا"), ("Used toxin", "استعمال سمّ")], "c"),
 Q("To identify the exact pathogens of infectious diseases use:", "لتحديد الممرضات الدقيقة للأمراض المعدية يُستعمل:",
   [("Diagnostic microbiology", "الأحياء الدقيقة التشخيصية"), ("Diagnostic virology", "الفيروسات التشخيصية"), ("Diagnostic parasitology", "الطفيليات التشخيصية"),
    ("Diagnostic mycology", "الفطريات التشخيصية"), NONET], "a"),
 Q("Manufacturers' material safety data sheets (MSDSs) refer to:", "صحائف بيانات سلامة المواد (MSDSs) من المصنّعين تخصّ:",
   [("Physical methods", "الطرق الفيزيائية"), ("Biohazard waste", "النفايات الخطرة حيويًّا"), ("Chemical materials", "المواد الكيميائية"), ("Both A and B", "A وB معًا"), ("All of the above", "جميع ما سبق")], "c"),
 Q("Diagnosis of an infectious disease usually involves:", "يتضمّن تشخيص المرض المعدي عادةً:",
   [("Morphologic identification of the agent", "التحديد الشكلي للعامل"), ("Cultivation of the organisms", "زرع الكائنات"), ("Detection of microbial antigens by immunologic assay", "كشف المستضدات الميكروبية بالمقايسة المناعية"),
    ("Detection of microbial DNA or RNA", "كشف DNA أو RNA الميكروبي"), ALL], "e"),
 Q("Which of the following organisms is fastidious?", "أيّ الكائنات الآتية صعب النمو؟",
   [(S("Neisseria gonorrhoeae"), "النيسرية البنية"), (S("Haemophilus influenzae"), "المستدمية النزلية"), (S("Staph. aureus"), "العنقودية الذهبية"),
    (S("Klebsiella pneumoniae"), "الكلبسيلة الرئوية"), ("Both A and B", "A وB معًا")], "e"),
 Q("A detailed request form that accompanies a clinical sample includes:", "يتضمّن نموذج الطلب التفصيلي المرافق للعيّنة السريرية:",
   [("Patient details", "تفاصيل المريض"), ("Sample type", "نوع العيّنة"), ("Time of collection", "وقت الجمع"), ALL, ("Only A and C", "A وC فقط")], "e"),
 Q("All specimens that may contain highly infectious organism must be marked as:", "كل العيّنات التي قد تحتوي كائنًا شديد العدوى يجب وسمها بـ:",
   [("HIGH RISK", "HIGH RISK"), ("LOW RISK", "LOW RISK"), ("NO RISK", "NO RISK"), ("Unsafe", "غير آمنة"), NONE], "a"),
 Q("Microbiological laboratory uses non-culture techniques for diagnosis such as:", "يستعمل مختبر الأحياء الدقيقة تقنيات غير زرعية للتشخيص مثل:",
   [("Direct microscopy", "الفحص المجهري المباشر"), ("Immunological methods", "الطرق المناعية"), ("Serology", "الفحوص المصلية"), ("Nucleic acid amplification techniques (NAAT)", "تقنيات تضخيم الحمض النووي (NAAT)"), ALL], "e"),
 Q("Pathogen when acquired from normal flora is called:", "الممرض المكتسَب من الفلورا الطبيعية يُسمّى:",
   [("exogenous", "خارجي المنشأ"), ("external pathogen", "ممرض خارجي"), ("endogenous", "داخلي المنشأ"), ("non pathogen", "غير ممرض"), NONE], "c"),
 Q("Antibiotics added to media for:", "تُضاف المضادات الحيوية إلى الأوساط لـ:",
   [("supporting the growth", "دعم النمو"), ("as color indicator", "مؤشّر لوني"), ("suppressing the growth", "تثبيط النمو"), ("Growth factor", "عامل نمو"), NONE], "c"),
 Q("It is possible to see living cells without staining them by using:", "يمكن رؤية الخلايا الحيّة دون صبغها باستعمال:",
   [("SEM microscope", "مجهر SEM"), ("phase-contrast microscope", "مجهر تباين الطور"), ("DIC microscope", "مجهر DIC"), ("Dark-field", "الحقل المظلم"), NONE], "b"),
 indole(ALL, NONE),
 negst(("crystal violet", "البنفسج البلوري")),
 Q("The most frequently medium used in antimicrobial susceptibility test is:", "أكثر وسط يُستعمل في اختبار الحساسية للمضادات الميكروبية:",
   [("Blood agar", "أجار الدم"), ("Chocolate agar", "أجار الشوكولاتة"), ("Mannitol salt agar", "أجار المانيتول الملحي"), ("Thayer-Martin agar", "أجار ثاير-مارتن"), ("Mueller-Hinton agar", "أجار مولر-هنتون")], "e"),
 Q("Common cases of eye infections:", "من حالات التهابات العين الشائعة:",
   [("Conjunctivitis", "التهاب الملتحمة"), ("Keratitis", "التهاب القرنية"), ("A & B", "A وB"), ("Pneumonia", "ذات الرئة"), ALL], "c"),

 T("Exam 2/12/2023 — Prof. Dr. Adnan (doctor's answer key)", "امتحان 2/12/2023 — أ.د. عدنان (بمفتاح الدكتور)"),
 Q(S("Staphylococcus aureus") + " can cross the synovial membrane of a joint to initiate:", "يمكن للعنقودية الذهبية عبور الغشاء الزلالي للمفصل لتبدأ:",
   [("gastritis", "التهاب المعدة"), ("septic arthritis", "التهاب المفصل الإنتاني"), ("tonsillitis", "التهاب اللوزتين"), ALL, NONE], "b"),
 Q("Antimicrobial agents are ……… antimicrobial therapeutic agents.", "مضادات الميكروبات عوامل علاجية ……… مضادة للميكروبات.",
   [("poison", "سامّة"), ("toxic", "مؤذية"), ("non-toxic", "غير سامّة"), ALL, NONE], "c"),
 Q("Novobiocin susceptibility test (NST) is used to differentiate between:", "يُستعمل اختبار الحساسية للنوفوبيوسين (NST) للتفريق بين:",
   [(S("Staph. saprophyticus") + " and " + S("Staph. epidermidis"), "Staph. saprophyticus وStaph. epidermidis"), (S("Staph. aureus") + " and " + S("Staph. saprophyticus"), "Staph. aureus وStaph. saprophyticus"),
    (S("Staph. aureus") + " and " + S("Staph. epidermidis"), "Staph. aureus وStaph. epidermidis"), (S("Staph. saprophyticus") + " and " + S("Strep. pyogenes"), "Staph. saprophyticus وStrep. pyogenes"), NONE], "a"),
 Q("Both pneumococci and " + S("Neisseria meningitidis") + " are:", "كلٌّ من المكوّرات الرئوية والنيسرية السحائية:",
   [("Gram-negative", "سالبة غرام"), ("Bacilli", "عصيات"), ("Diplococci", "مكوّرات مزدوجة"), ALL, NONE], "c"),
 trypto(NONE),
 Q("Skin should be decontaminated with an appropriate ……… prior to collecting blood.", "يجب تطهير الجلد بـ……… مناسب قبل سحب الدم.",
   [("antiseptic", "مطهّر"), ("saline", "محلول ملحي"), ("buffer", "محلول منظِّم"), ("B & C", "B وC"), ("Only C", "C فقط")], "a"),
 bileesc(),
 Q("Mueller Hinton agar (MHA) is commonly used for the routine susceptibility testing because of:", "يُستعمل أجار مولر-هنتون (MHA) عادةً لفحص الحساسية الروتيني لأنه:",
   [("non-selective", "غير انتقائي"), ("non-differential medium", "وسط غير تفريقي"), ("all organisms grow on", "تنمو عليه كل الكائنات"), ALL, NONE], "c"),
 Q(S("Neisseria meningitidis") + " causes:", "تسبّب النيسرية السحائية:",
   [("T.B. disease", "مرض التدرّن"), ("Pneumonia", "ذات الرئة"), ("Arthritis", "التهاب المفاصل"), ("Gonorrhea", "السيلان"), NONE], "b"),
 pyog(),
 Q("In clinical laboratories, susceptibility testing is usually performed by a disk diffusion or/and:", "في المختبرات السريرية يُجرى فحص الحساسية عادةً بانتشار الأقراص و/أو:",
   [("MIC", "MIC"), ("Catalase", "الكاتاليز"), ("Oxidase", "الأوكسيديز"), ALL, NONE], "e"),
 Q("Specimen should reach the laboratory as soon as possible or a suitable ……… medium must be used.", "يجب أن تصل العيّنة إلى المختبر بأسرع وقت أو يُستعمل وسط ……… مناسب.",
   [("selective", "انتقائي"), ("preservative", "حافظ"), ("transport", "نقل"), ("B & C", "B وC"), NONET], "d"),
 urea(("None of the above", "لا شيء مما سبق")),
 msa(ALL, NONE),
 Q("Susceptibility to optochin and solubility in bile are used for identification of:", "الحساسية للأوبتوشين والذوبان في الصفراء يُستعملان لتشخيص:",
   [(S("Strep. pneumoniae"), "Strep. pneumoniae"), (S("Staph. aureus"), "Staph. aureus"), (S("Pseudomonas aeruginosa"), "Pseudomonas aeruginosa"), ALL, NONE], "a"),
 abx(None, None),
 Q("Ability to hydrolyze esculin in the presence of bile is used for identification of ……… species in combination with NaCl.", "القدرة على تحليل الإسكولين بوجود الصفراء تُستعمل لتشخيص أنواع ……… مع NaCl.",
   [("Lactococci", "Lactococci"), ("Pseudococci", "Pseudococci"), ("Enterococci", "Enterococci"), ALL, NONE], "c"),
 Q("Indicator media may also contain selective agents including antibiotics or substances such as ……… and crystal violet to suppress growth of most Gram-positive microorganisms.",
   "قد تحتوي الأوساط المؤشِّرة أيضًا عوامل انتقائية كالمضادات الحيوية أو مواد مثل ……… والبنفسج البلوري لتثبيط نمو معظم موجبات غرام.",
   [("NaCl salts", "أملاح NaCl"), ("bile salts", "أملاح الصفراء"), ("Phosphate", "الفوسفات"), ("Carbohydrates", "الكربوهيدرات"), ("Potassium", "البوتاسيوم")], "d"),
 negst(("Serology", "الفحوص المصلية")),
 Q("Gram stain of a sputum specimen revealing WBCs and gram-positive diplococci is indicative of:", "صبغة غرام لعيّنة قشع تُظهر كريات بيضاء ومكوّرات مزدوجة موجبة غرام تدلّ على:",
   [(S("Staph. aureus"), "Staph. aureus"), (S("Strep. pyogenes"), "Strep. pyogenes"), (S("Strep. pneumoniae"), "Strep. pneumoniae"), ALL, NONE], "c"),
 indole(ALL, NONE),
 fix(ALL),
 purpose,
 enriched(ALL, NONE),
 Q("Gram stains for " + S("N. gonorrhoeae") + " on specimens from the vagina and anal crypts are not recommended because these sites contain other ……… with same morphology.",
   "لا يُنصح بصبغة غرام لـ N. gonorrhoeae في عيّنات المهبل والخبايا الشرجية لأن هذه المواقع تحتوي ……… أخرى بالشكل نفسه.",
   [("fungus", "فطريات"), ("parasite", "طفيليات"), ("bacteria", "بكتيريا"), ALL, NONE], "c"),
 tradit("d"),
 Q("The useful test for differentiating pneumococci from other streptococci is:", "الاختبار المفيد للتفريق بين المكوّرات الرئوية والعقديات الأخرى:",
   [("Inulin fermentation", "تخمير الإينولين"), ("Bile solubility test", "اختبار الذوبان في الصفراء"), ("Both A & B", "A وB معًا"), ("Lactose fermentation", "تخمير اللاكتوز"), NONE], "b"),
 Q("A transient bacteremia can arise from a pneumococcal pneumonia, or pyelonephritis caused by:", "قد ينشأ تجرثم دم عابر من ذات رئة بالمكوّرات الرئوية أو من التهاب حوض الكلية الذي تسبّبه:",
   [(S("Streptococcus sanguinis"), "Streptococcus sanguinis"), (S("Shigella sonnei"), "Shigella sonnei"), (S("Escherichia coli"), "الإشريكية القولونية"), ALL, NONE], "c"),
 Q("The term ……… has been traditionally reserved for compounds that are naturally produced by living microorganisms, such as bacteria and fungi.", "خُصّص مصطلح ……… تقليديًّا للمركّبات التي تنتجها الكائنات الحيّة طبيعيًّا كالبكتيريا والفطريات.",
   [("Antibiotic", "المضاد الحيوي"), ("Antisera", "الأمصال المضادة"), ("Antibiogram", "المخطط الحيوي للمضادات"), ALL, NONE], "a"),
 catal(("A & B", "A وB"), NONE),

 T("Exam 2022 (1st attempt) — Prof. Dr. Adnan (no key in the file; answered from the lectures)", "امتحان 2022 (الدور الأول) — أ.د. عدنان (بلا مفتاح بالملف؛ الحل من المحاضرات)"),
 Q("Which of the following is considered supplemental or enrichment broth?", "أيّ مما يأتي يُعدّ مرقًا داعمًا أو مُغنيًا؟",
   [("BHIB", "BHIB"), ("TSA", "TSA"), ("TSB", "TSB"), ("Both A & C", "A وC معًا"), ALLT], "d"),
 Q("The enzyme that converts soluble fibrinogen protein to insoluble fibrin protein is:", "الإنزيم الذي يحوّل بروتين الفيبرينوجين الذائب إلى فيبرين غير ذائب:",
   [("Catalase enzyme", "إنزيم الكاتاليز"), ("Coagulase enzyme", "إنزيم التخثّر"), ("Oxidase enzyme", "إنزيم الأوكسيديز"), ("Urease enzyme", "إنزيم اليوريز"), NONET], "b"),
 Q("IMViC includes tests:", "يشمل IMViC الاختبارات:",
   [("Indole & urease, MR-VP", "الإندول واليوريز، MR-VP"), ("MR-VP & indole-oxidase", "MR-VP والإندول-أوكسيديز"), ("MR-VP & catalase", "MR-VP والكاتاليز"), ALLT, NONET], "e"),
 Q("Gram stain steps include:", "تشمل خطوات صبغة غرام:",
   [("Crystal violet, iodine, alcohol and safranin", "البنفسج البلوري، اليود، الكحول، السفرانين"), ("Crystal violet, alcohol, iodine and safranin", "البنفسج البلوري، الكحول، اليود، السفرانين"),
    ("Alcohol, iodine, safranin and crystal violet", "الكحول، اليود، السفرانين، البنفسج البلوري"), ("Iodine, safranin and crystal violet", "اليود، السفرانين، البنفسج البلوري"), NONET], "a"),
 Q("The colonies produced by " + S("Pseudomonas") + " on MacConkey's medium are:", "مستعمرات Pseudomonas على وسط ماكونكي تكون:",
   [("Purple colored", "بنفسجية"), ("Pink colored", "وردية"), ("Pale colored", "باهتة"), ("Green colored", "خضراء"), ("Red colored", "حمراء")], "c"),
 Q("Which of the following stains is differential stain?", "أيّ الصبغات الآتية صبغة تفريقية؟",
   [("Negative stain", "الصبغة السالبة"), ("Gram stain", "صبغة غرام"), ("Simple stain", "الصبغة البسيطة"), ("Acid fast stain", "الصبغة المقاومة للحامض"), ("Both B and D", "B وD معًا")], "e"),
 Q("MacConkey agar is:", "أجار ماكونكي:",
   [("Selective media", "وسط انتقائي"), ("Differential media", "وسط تفريقي"), ("Basal media", "وسط أساسي"), ("Both A & B", "A وB معًا"), ALLT], "d"),
 Q("Which of the following media is the selective-differential for " + S("Staph. aureus") + "?", "أيّ الأوساط الآتية انتقائي-تفريقي لـ Staph. aureus؟",
   [("Columbia agar", "أجار كولومبيا"), ("TCBS agar", "أجار TCBS"), ("MacConkey agar", "أجار ماكونكي"), ("Nutrient agar", "أجار المغذّي"), ("Mannitol salt agar", "أجار المانيتول الملحي")], "e"),
 Q("Oxidase test is initially used for differentiating between groups of ……… bacteria.", "يُستعمل اختبار الأوكسيديز أساسًا للتفريق بين مجموعات البكتيريا ………",
   [("Virus", "الفيروسات"), ("Gram negative", "سالبة غرام"), ("Gram-positive", "موجبة غرام"), ALLT, NONET], "b"),
 Q("The morphologic identification of a microorganism involves:", "التشخيص الشكلي للكائن الدقيق يشمل:",
   [("Staining", "الصبغ"), ("Culture", "الزرع"), ("Microscopic examination", "الفحص المجهري"), ("Both A and C", "A وC معًا"), NONET], "d"),
 Q("The ……… media are designed to facilitate growth of some bacteria while suppressing the growth of others.", "الأوساط ……… مصمَّمة لتسهيل نمو بعض البكتيريا مع تثبيط نمو غيرها.",
   [("Simple", "البسيطة"), ("Enriched", "الغنية"), ("Selective", "الانتقائية"), ("Complex", "المعقّدة"), NONET], "c"),
 Q("Which of the following media can differentiate between lactose and non-lactose fermenting gram-negative bacteria?", "أيّ الأوساط الآتية يفرّق بين سالبات غرام المخمِّرة وغير المخمِّرة للاكتوز؟",
   [("Chocolate agar", "أجار الشوكولاتة"), ("MacConkey agar", "أجار ماكونكي"), ("Modified Thayer-Martin agar", "أجار ثاير-مارتن المعدَّل"), ("Blood agar", "أجار الدم"), ("Mannitol salt agar", "أجار المانيتول الملحي")], "b"),
 Q("The enzyme catalase catalyzes the release of water and oxygen from:", "يحفّز إنزيم الكاتاليز تحرير الماء والأوكسجين من:",
   [("Hydrogen peroxide", "بيروكسيد الهيدروجين"), ("Phosphoric acid", "حمض الفسفوريك"), ("Hydrochloric acid", "حمض الهيدروكلوريك"), ("Sulfuric acid", "حمض الكبريتيك"), NONET], "a"),
 Q("During negative staining, bacterial suspension is mixed with dyes, such as:", "في الصبغ السالب يُخلط المعلّق البكتيري بصبغات مثل:",
   [("India ink", "حبر الهند"), ("Nigrosine", "النيكروسين"), ("Carbol fuchsin", "الكاربول فوكسين"), ("Both A & B", "A وB معًا"), ALLT], "d"),
 Q("Changes in agar media resulting from bacterial growth such as:", "تغيّرات أوساط الأجار الناتجة عن نمو البكتيريا مثل:",
   [("Hemolytic pattern on blood agar", "نمط التحلّل الدموي على أجار الدم"), ("Changes in color of pH indicators", "تغيّر لون مؤشّرات الـ pH"), ("Pitting of the agar surface", "تنقّر سطح الأجار"), ALLT, NONET], "d"),
 msa(ALLT, NONET),
 abx(None, None),
 blood(NONET),
 Q("Gram stain consists of:", "تتكوّن صبغة غرام من:",
   [("Four reagents", "أربعة كواشف"), ("Three reagents", "ثلاثة كواشف"), ("Two reagents", "كاشفين"), ("Five reagents", "خمسة كواشف"), ("One reagent", "كاشف واحد")], "a"),
 Q("Malt extract agar consists of maltose (about 50%) and ………", "يتكوّن أجار مستخلص الشعير من المالتوز (حوالي 50%) و………",
   [("starch", "النشا"), ("Dextrin", "الدكسترين"), ("Glucose", "الكلوكوز"), ALLT, NONET], "d"),
 macsel(),
 fix(ALLT),
 enriched(ALLT, NONET),
 solid(NONET),
 bileesc(),
 choc(),
 pyog(),
 urea(NONET),
]

import copy; mcq = [copy.deepcopy(x) for x in mcq]
d = "/home/user/-/bacteriology-adnan-exams-mcq"
os.makedirs(d, exist_ok=True)
meta = {"subject_en": "Diagnostic Microbiology", "subject_ar": "الأحياء المجهرية التشخيصية", "short_ar": "بكتريا",
        "instructor": "د. عدنان", "unit_en": "Past Exams", "unit_ar": "أسئلة سنوات سابقة", "unit_label": "EXAM", "unit_no": "22-25",
        "title_en": "Prof. Dr. Adnan's Exam Questions (2022–2025)", "title_ar": "أسئلة امتحانات د. عدنان (2022–2025)",
        "department": "قسم التحليلات", "kind": "Theory — نظري", "questions_kind": "MCQ — اختيار من متعدد",
        "stage": "The fourth stage — الرابعة",
        "file_name": "BIOS - بكتريا نظري - أسئلة امتحانات د. عدنان MCQ"}
Qs = {"title_en": "Prof. Dr. Adnan's Exams — MCQ", "title_ar": "امتحانات د. عدنان — أسئلة اختيار",
      "answers_inline": True, "compact": True, "mcq_per_page": 5,
      "mcq_en": "Past exam MCQs — Prof. Dr. Adnan", "mcq_ar": "أسئلة امتحانات سابقة — د. عدنان",
      "intro_en": ["Q. Choose the correct answer of the following",
                   "Three of Prof. Dr. Adnan's exams (2025, 2/12/2023, 2022 1st attempt) in their original order; the answer sits under each question."],
      "intro_ar": ["س. اختر الإجابة الصحيحة مما يأتي",
                   "ثلاثة امتحانات للدكتور عدنان (2025، 2/12/2023، 2022 الدور الأول) بترتيبها الأصلي؛ والحل تحت كل سؤال."],
      "mcq": ltr_all(mcq), "tf": [], "traps": [], "important": []}
json.dump({"meta": meta, "questions": Qs}, open(d + "/lecture.json", "w"), ensure_ascii=False, indent=1)
qs = [m for m in mcq if "answer" in m]
print("MCQ:", len(qs), "| dist:", dict(Counter(m["answer"] for m in qs)))
for i, q in enumerate(qs, 1):
    print(i, q["answer"], q["options"]["abcde".index(q["answer"])][0][:55])
