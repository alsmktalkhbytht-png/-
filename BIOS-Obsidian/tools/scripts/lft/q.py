import sys, json, os
sys.path.insert(0, "/tmp/claude-0/-home-user-kwmdkm/44452a28-19bf-5ce8-890a-f6919e775f0b/scratchpad/imm456")
from ci import *            # Q P balance IM
sys.path.insert(0, "/tmp/claude-0/-home-user-kwmdkm/44452a28-19bf-5ce8-890a-f6919e775f0b/scratchpad"); from bidi import ltr_all

# Clinical Enzymology practical — Liver Function Tests (LFT): ALT/GPT & AST/GOT (stage 4, د. بارق و د. هشام).
# Source: 7-page student notes ("Abdullah Khalid", Advanced clinical Biochemistry practical 2023-2024).
# QUESTIONS ONLY — comprehensive MCQ bank; answers_inline + SA (important) incl. the student's marked/highlighted points.
O = P
FOLDER = "enzymology-lft-mcq"
W = lambda q, en, ar: dict(q, note_en=en, note_ar=ar)

mcq = [
 # ───────────────────────── 1. LFT overview & liver functions
 {"topic_en": "Liver function tests & functions of the liver", "topic_ar": "فحوصات وظائف الكبد ووظائف الكبد"},
 W(Q("Liver function tests (LFT) are used to:", "تُستعمل فحوصات وظائف الكبد (LFT) لـ:",
     O(("Measure various chemicals in the blood made by the liver", "قياس مواد كيميائية مختلفة في الدم يصنعها الكبد"), ("Measure urine output", "قياس كمية الإدرار"), ("Count blood cells", "عدّ خلايا الدم"), ("Measure blood pressure", "قياس ضغط الدم")), "a"),
   "LFTs measure chemicals in the blood made by the liver; an abnormal result indicates a liver problem and may help identify the cause.", "تقيس فحوصات وظائف الكبد مواد كيميائية في الدم يصنعها الكبد؛ والنتيجة غير الطبيعية تدلّ على مشكلة في الكبد وقد تساعد في معرفة سببها."),
 W(Q("Which is listed as a major function of the liver?", "أيّها مذكور وظيفةً رئيسة للكبد؟",
     O(("Bile production and excretion", "إنتاج العصارة الصفراء وإفرازها"), ("Production of red blood cells only", "إنتاج كريات الدم الحمراء فقط"), ("Filtering urine", "ترشيح البول"), ("Pumping blood", "ضخّ الدم")), "a"),
   "Major functions: bile production/excretion; excretion of bilirubin, cholesterol, hormones and drugs; metabolism of fats, proteins and carbohydrates; enzyme activation; storage of glycogen, vitamins and minerals; synthesis of plasma proteins and clotting factors.", "من وظائف الكبد الرئيسة: إنتاج الصفراء وإفرازها؛ وطرح البيليروبين والكوليسترول والهرمونات والأدوية؛ وأيض الدهون والبروتينات والكربوهيدرات؛ وتنشيط الإنزيمات؛ وخزن الغلايكوجين والفيتامينات والمعادن؛ وتصنيع بروتينات البلازما وعوامل التخثّر."),
 W(Q("The liver synthesizes plasma proteins such as:", "يصنّع الكبد بروتينات البلازما مثل:",
     O(("Albumin and clotting factors", "الألبومين وعوامل التخثّر"), ("Hemoglobin", "الهيموغلوبين"), ("Insulin", "الأنسولين"), ("Keratin", "الكيراتين")), "a"),
   "Function 6: synthesis of plasma proteins, such as albumin, and clotting factors.", "الوظيفة 6: تصنيع بروتينات البلازما، مثل الألبومين، وعوامل التخثّر."),
 W(Q("Which is NOT one of the main tests for liver function listed in the notes?", "أيّها ليس من الفحوصات الرئيسة لوظيفة الكبد المذكورة في الملاحظات؟",
     O(("Blood urea", "يوريا الدم"), ("Serum bilirubin", "البيليروبين المصلي"), ("Alkaline phosphatase (ALP)", "الفوسفاتيز القلوي (ALP)"), ("Albumin and total protein", "الألبومين والبروتين الكلّي")), "a"),
   "The five main LFTs listed: ALT (GPT), AST (GOT), serum bilirubin (total, direct, indirect), alkaline phosphatase (ALP), and albumin/total protein.", "الفحوصات الخمسة الرئيسة المذكورة: ALT (GPT)، وAST (GOT)، والبيليروبين المصلي (الكلّي والمباشر وغير المباشر)، والفوسفاتيز القلوي (ALP)، والألبومين/البروتين الكلّي."),
 W(Q("Serum bilirubin as a liver function test is measured as:", "يُقاس البيليروبين المصلي في فحص وظيفة الكبد بصورة:",
     O(("Total, direct and indirect", "الكلّي والمباشر وغير المباشر"), ("Total only", "الكلّي فقط"), ("Direct only", "المباشر فقط"), ("It is not measured", "لا يُقاس")), "a"),
   "The notes list serum bilirubin as Total, Direct and indirect.", "تذكر الملاحظات البيليروبين المصلي: الكلّي والمباشر وغير المباشر."),

 # ───────────────────────── 2. ALT / GPT — definition & distribution
 {"topic_en": "Alanine aminotransferase (ALT / GPT)", "topic_ar": "ناقلة أمين الألانين (ALT / GPT)"},
 W(Q("Alanine aminotransferase (ALT) is also called:", "ناقلة أمين الألانين (ALT) تُسمّى أيضًا:",
     O(("Glutamic-pyruvic transaminase (GPT)", "ناقلة أمين الغلوتاميك-بيروفيك (GPT)"), ("Glutamic-oxaloacetic transaminase (GOT)", "ناقلة أمين الغلوتاميك-أوكسالوأسيتيك (GOT)"), ("Lactate dehydrogenase (LDH)", "نازعة هيدروجين اللاكتات (LDH)"), ("Alkaline phosphatase (ALP)", "الفوسفاتيز القلوي (ALP)")), "a"),
   "ALT = alanine aminotransferase, also called glutamic-pyruvic transaminase (GPT).", "ALT = ناقلة أمين الألانين، وتُسمّى أيضًا ناقلة أمين الغلوتاميك-بيروفيك (GPT)."),
 W(Q("ALT catalyzes the transfer of an amino group from L-alanine to α-ketoglutarate to produce:", "تحفّز ALT نقل مجموعة أمين من الألانين-L إلى ألفا-كيتوغلوتارات لإنتاج:",
     O(("Pyruvate and L-glutamate", "البيروفات والغلوتامات-L"), ("Oxaloacetate and glutamate", "الأوكسالوأسيتات والغلوتامات"), ("Lactate and NAD", "اللاكتات وNAD"), ("Malate and NAD", "المالات وNAD")), "a"),
   "ALT catalyzes a reversible transamination: L-alanine + α-ketoglutarate → pyruvate + L-glutamate.", "تحفّز ALT نقل أمين عكوسًا: الألانين-L + ألفا-كيتوغلوتارات ← البيروفات + الغلوتامات-L."),
 W(Q("The ALT reaction is described in the notes as a:", "يوصف تفاعل ALT في الملاحظات بأنه:",
     O(("Reversible transamination reaction", "تفاعل نقل أمين عكوس"), ("Irreversible oxidation", "أكسدة غير عكوسة"), ("Hydrolysis reaction", "تفاعل حلمهة"), ("Precipitation reaction", "تفاعل ترسيب")), "a"),
   "The notes call it a reversible transamination reaction.", "تسمّيه الملاحظات تفاعل نقل أمين عكوسًا."),
 W(Q("ALT is found primarily in the:", "توجد ALT بصورة رئيسة في:",
     O(("Liver and kidney", "الكبد والكلية"), ("Lungs and spleen", "الرئتين والطحال"), ("Bone and skin", "العظم والجلد"), ("Brain only", "الدماغ فقط")), "a"),
   "ALT is an enzyme found primarily in the liver and kidney; normally a low level exists in serum.", "ALT إنزيم يوجد بصورة رئيسة في الكبد والكلية؛ وعادةً يوجد مستوى منخفض منه في المصل."),
 W(Q("ALT is most commonly associated with the liver; high concentrations occur in the liver and relatively low concentrations in the:", "ترتبط ALT غالبًا بالكبد؛ وتوجد تراكيز عالية في الكبد وتراكيز منخفضة نسبيًا في:",
     O(("Heart, muscle, and kidney", "القلب والعضلة والكلية"), ("Liver only", "الكبد فقط"), ("Blood only", "الدم فقط"), ("Bile ducts", "القنوات الصفراوية")), "a"),
   "ALT occurs in plasma and tissues but is most associated with the liver; high in liver, relatively low in heart, muscle and kidney.", "توجد ALT في البلازما والأنسجة لكنها أكثر ارتباطًا بالكبد؛ عالية في الكبد ومنخفضة نسبيًا في القلب والعضلة والكلية."),
 W(Q("A normally LOW serum ALT level that rises with liver damage makes ALT useful for:", "كون مستوى ALT في المصل منخفضًا عادةً ويرتفع مع تلف الكبد يجعلها مفيدة لـ:",
     O(("Screening and monitoring liver disease", "فحص ومتابعة أمراض الكبد"), ("Measuring blood glucose", "قياس سكّر الدم"), ("Counting platelets", "عدّ الصفيحات"), ("Testing kidney filtration", "اختبار ترشيح الكلية")), "a"),
   "Normally low ALT exists in serum; the level increases with liver damage and is used for screening and/or monitoring liver disease.", "عادةً يوجد ALT منخفض في المصل؛ ويرتفع مع تلف الكبد ويُستعمل لفحص ومتابعة أمراض الكبد."),
 W(Q("ALT testing is primarily used to:", "يُستعمل فحص ALT بصورة رئيسة لـ:",
     O(("Diagnose liver disease and monitor treatment of hepatitis", "تشخيص أمراض الكبد ومتابعة علاج التهاب الكبد"), ("Diagnose anemia", "تشخيص فقر الدم"), ("Diagnose diabetes", "تشخيص السكّري"), ("Diagnose fractures", "تشخيص الكسور")), "a"),
   "Primarily used to diagnose liver disease and to monitor the course of treatment for hepatitis, active post-necrotic cirrhosis, and the effects of later drug therapy.", "يُستعمل أساسًا لتشخيص أمراض الكبد ومتابعة سير علاج التهاب الكبد، والتشمّع التالي للتنخّر النشط، وتأثيرات العلاج الدوائي اللاحق."),

 # ───────────────────────── 3. ALT vs AST & reference values
 {"topic_en": "ALT vs AST, jaundice, and reference values", "topic_ar": "ALT مقابل AST، واليرقان، والقيم المرجعية"},
 W(Q("Which statement about ALT and AST specificity/sensitivity is correct?", "أيّ عبارة صحيحة عن نوعية/حساسية ALT وAST؟",
     O(("ALT is more specific for liver disease, but AST is more sensitive to alcoholic liver disease", "ALT أكثر نوعية لمرض الكبد، لكن AST أكثر حساسية لمرض الكبد الكحولي"), ("AST is more specific for liver disease than ALT", "AST أكثر نوعية لمرض الكبد من ALT"), ("Both are equally specific", "كلاهما متساويان في النوعية"), ("Neither is related to the liver", "كلاهما لا علاقة له بالكبد")), "a"),
   "ALT is more specific than AST for liver disease, but AST is more sensitive to alcoholic liver disease.", "ALT أكثر نوعية من AST لمرض الكبد، لكن AST أكثر حساسية لمرض الكبد الكحولي."),
 W(Q("ALT helps differentiate between:", "تساعد ALT في التفريق بين:",
     O(("Hemolytic jaundice and jaundice due to liver disease", "اليرقان الانحلالي واليرقان الناتج عن مرض الكبد"), ("Anemia and leukemia", "فقر الدم وابيضاض الدم"), ("Diabetes and gout", "السكّري والنقرس"), ("Two types of fracture", "نوعين من الكسور")), "a"),
   "ALT also differentiates between hemolytic jaundice and jaundice due to liver disease.", "تفرّق ALT أيضًا بين اليرقان الانحلالي واليرقان الناتج عن مرض الكبد."),
 W(Q("The adult ALT reference value for MALES is:", "القيمة المرجعية لـ ALT عند الذكور البالغين هي:",
     O(("10–40 U/L", "10–40 U/L"), ("7–35 U/L", "7–35 U/L"), ("13–45 U/L", "13–45 U/L"), ("5–45 U/L", "5–45 U/L")), "a"),
   "Adults — Males: 10–40 U/L; Females: 7–35 U/L. Newborns: 13–45 U/L.", "البالغون — الذكور: 10–40 U/L؛ الإناث: 7–35 U/L. حديثو الولادة: 13–45 U/L."),
 W(Q("The adult ALT reference value for FEMALES is:", "القيمة المرجعية لـ ALT عند الإناث البالغات هي:",
     O(("7–35 U/L", "7–35 U/L"), ("10–40 U/L", "10–40 U/L"), ("13–45 U/L", "13–45 U/L"), ("5–45 U/L", "5–45 U/L")), "a"),
   "Females: 7–35 U/L (males 10–40 U/L; newborns 13–45 U/L).", "الإناث: 7–35 U/L (الذكور 10–40 U/L؛ حديثو الولادة 13–45 U/L)."),
 W(Q("The ALT reference value for NEWBORNS is:", "القيمة المرجعية لـ ALT عند حديثي الولادة هي:",
     O(("13–45 U/L", "13–45 U/L"), ("10–40 U/L", "10–40 U/L"), ("7–35 U/L", "7–35 U/L"), ("5–45 U/L", "5–45 U/L")), "a"),
   "Newborns: 13–45 U/L.", "حديثو الولادة: 13–45 U/L."),
 W(Q("Which condition is listed as causing INCREASED ALT levels?", "أيّ حالة مذكورة سببًا لارتفاع مستوى ALT؟",
     O(("Hepatocellular disease", "مرض خلايا الكبد"), ("Iron deficiency", "نقص الحديد"), ("Dehydration only", "الجفاف فقط"), ("Vitamin C deficiency", "نقص فيتامين C")), "a"),
   "Increased ALT: hepatocellular disease, alcoholic cirrhosis, obstructive jaundice/biliary obstruction, viral/infectious/toxic hepatitis, myocardial infarction & heart failure, severe burns, and obesity.", "يرتفع ALT في: مرض خلايا الكبد، والتشمّع الكحولي، واليرقان الانسدادي/الانسداد الصفراوي، والتهاب الكبد الفيروسي/الإنتاني/السمّي، واحتشاء العضلة القلبية وفشل القلب، والحروق الشديدة، والسمنة."),

 # ───────────────────────── 4. ALT method (principle, procedure, calculation)
 {"topic_en": "ALT method: principle, procedure, calculation", "topic_ar": "طريقة ALT: المبدأ والإجراء والحساب"},
 W(Q("In the kinetic ALT method, the indicator (second) reaction uses the enzyme:", "في طريقة ALT الحركية، يستعمل التفاعل الكاشف (الثاني) الإنزيم:",
     O(("Lactate dehydrogenase (LDH)", "نازعة هيدروجين اللاكتات (LDH)"), ("Malate dehydrogenase (MDH)", "نازعة هيدروجين المالات (MDH)"), ("Alkaline phosphatase (ALP)", "الفوسفاتيز القلوي (ALP)"), ("Amylase", "الأميليز")), "a"),
   "ALT principle: L-alanine + α-ketoglutarate —ALT→ pyruvate + L-glutamate; then pyruvate + NADH + H⁺ —LDH→ L-lactate + NAD⁺ (LDH = indicator).", "مبدأ ALT: الألانين-L + ألفا-كيتوغلوتارات —ALT← بيروفات + غلوتامات-L؛ ثم بيروفات + NADH + H⁺ —LDH← لاكتات-L + NAD⁺ (LDH = الكاشف)."),
 W(Q("In the ALT indicator reaction, pyruvate + NADH + H⁺ are converted by LDH to:", "في تفاعل ALT الكاشف، يحوّل LDH البيروفات + NADH + H⁺ إلى:",
     O(("L-lactate + NAD⁺", "لاكتات-L + NAD⁺"), ("L-malate + NAD⁺", "مالات-L + NAD⁺"), ("Oxaloacetate + glutamate", "أوكسالوأسيتات + غلوتامات"), ("Pyruvate + glutamate", "بيروفات + غلوتامات")), "a"),
   "LDH converts pyruvate + NADH + H⁺ → L-lactate + NAD⁺; the fall in NADH is what is measured.", "يحوّل LDH البيروفات + NADH + H⁺ ← لاكتات-L + NAD⁺؛ والمقاس هو انخفاض NADH."),
 W(Q("In the ALT procedure, the volumes of work reagent and sample are:", "في إجراء ALT، حجما الكاشف العامل والعيّنة هما:",
     O(("1000 µL reagent and 100 µL sample", "1000 µL كاشف و100 µL عيّنة"), ("100 µL reagent and 1000 µL sample", "100 µL كاشف و1000 µL عيّنة"), ("500 µL reagent and 500 µL sample", "500 µL كاشف و500 µL عيّنة"), ("1000 µL reagent and 1000 µL sample", "1000 µL كاشف و1000 µL عيّنة")), "a"),
   "Procedure: work reagent 1000 µL + sample 100 µL; mix and incubate 1 min at 37°C, then read the change in absorbance every 20 sec during 1 min.", "الإجراء: الكاشف العامل 1000 µL + العيّنة 100 µL؛ يُمزج ويُحضَن دقيقة عند 37°م، ثم يُقرأ تغيّر الامتصاص كل 20 ثانية خلال دقيقة."),
 W(Q("The SGPT (ALT) activity is calculated as:", "يُحسب نشاط SGPT (ALT) بالعلاقة:",
     O(("ΔA/min × 1745", "ΔA/min × 1745"), ("ΔA/min × 340", "ΔA/min × 340"), ("ΔA/min ÷ 1745", "ΔA/min ÷ 1745"), ("ΔA × min × 100", "ΔA × min × 100")), "a"),
   "SGPT activity (U/L) = ΔA/min × 1745.", "نشاط SGPT (U/L) = ΔA/min × 1745."),

 # ───────────────────────── 5. AST / GOT — definition & distribution
 {"topic_en": "Aspartate aminotransferase (AST / GOT)", "topic_ar": "ناقلة أمين الأسبارتات (AST / GOT)"},
 W(Q("Aspartate aminotransferase (AST) is also called:", "ناقلة أمين الأسبارتات (AST) تُسمّى أيضًا:",
     O(("Glutamic-oxaloacetic transaminase (GOT)", "ناقلة أمين الغلوتاميك-أوكسالوأسيتيك (GOT)"), ("Glutamic-pyruvic transaminase (GPT)", "ناقلة أمين الغلوتاميك-بيروفيك (GPT)"), ("Lactate dehydrogenase (LDH)", "نازعة هيدروجين اللاكتات (LDH)"), ("Alkaline phosphatase (ALP)", "الفوسفاتيز القلوي (ALP)")), "a"),
   "AST = aspartate aminotransferase, also called glutamic-oxaloacetic transaminase (GOT).", "AST = ناقلة أمين الأسبارتات، وتُسمّى أيضًا ناقلة أمين الغلوتاميك-أوكسالوأسيتيك (GOT)."),
 W(Q("AST catalyzes the reversible reaction of aspartate and α-ketoglutarate to form:", "تحفّز AST تفاعل الأسبارتات وألفا-كيتوغلوتارات العكوس لتكوين:",
     O(("Oxaloacetate and glutamate", "الأوكسالوأسيتات والغلوتامات"), ("Pyruvate and L-glutamate", "البيروفات والغلوتامات-L"), ("Lactate and NAD", "اللاكتات وNAD"), ("Malate and NAD", "المالات وNAD")), "a"),
   "AST: aspartate + α-ketoglutarate ⇌ oxaloacetate + glutamate (aspartate donates its amino group → oxaloacetate; α-ketoglutarate accepts it → glutamate).", "AST: الأسبارتات + ألفا-كيتوغلوتارات ⇌ أوكسالوأسيتات + غلوتامات (يتبرّع الأسبارتات بمجموعة الأمين ← أوكسالوأسيتات؛ وتقبلها ألفا-كيتوغلوتارات ← غلوتامات)."),
 W(Q("The AST reaction requires the coenzyme:", "يتطلّب تفاعل AST المرافق الإنزيمي:",
     O(("Pyridoxine phosphate (a vitamin B6 derivative)", "فوسفات البيريدوكسين (مشتقّ من فيتامين B6)"), ("Thiamine (vitamin B1)", "الثيامين (فيتامين B1)"), ("Ascorbic acid (vitamin C)", "حمض الأسكوربيك (فيتامين C)"), ("Biotin (vitamin B7)", "البيوتين (فيتامين B7)")), "a"),
   "This reaction requires the coenzyme pyridoxine phosphate (a derivative of vitamin B6).", "يتطلّب هذا التفاعل المرافق الإنزيمي فوسفات البيريدوكسين (مشتقّ من فيتامين B6)."),
 W(Q("GOT is an enzyme present in tissues of:", "GOT إنزيم موجود في أنسجة ذات:",
     O(("High metabolic activity", "نشاط أيضي عالٍ"), ("Low blood supply", "إمداد دموي قليل"), ("No metabolism", "لا أيض فيها"), ("Fat storage only", "خزن دهني فقط")), "a"),
   "GOT is present in tissues of high metabolic activity (heart, liver, skeletal muscle, kidney, brain, pancreas, spleen, lungs).", "GOT موجود في أنسجة ذات نشاط أيضي عالٍ (القلب، الكبد، العضلة الهيكلية، الكلية، الدماغ، البنكرياس، الطحال، الرئتان)."),
 W(Q("GOT (AST) is released into the circulation following:", "يُطلق GOT (AST) إلى الدوران عقب:",
     O(("Injury or death of cells", "إصابة الخلايا أو موتها"), ("Eating a meal", "تناول وجبة"), ("Physical rest", "الراحة الجسدية"), ("Drinking water", "شرب الماء")), "a"),
   "The enzyme is released into the circulation following injury or death of cells; any disease affecting these highly metabolic tissues raises GOT.", "يُطلق الإنزيم إلى الدوران عقب إصابة الخلايا أو موتها؛ وأيّ مرض يصيب هذه الأنسجة عالية الأيض يرفع GOT."),
 W(Q("AST (GOT) testing is used to evaluate:", "يُستعمل فحص AST (GOT) لتقييم:",
     O(("Liver and heart disease", "أمراض الكبد والقلب"), ("Kidney stones", "حصى الكلى"), ("Lung infection only", "عدوى الرئة فقط"), ("Bone density", "كثافة العظم")), "a"),
   "AST is used to evaluate liver and heart disease; GOT is usually ordered along with GPT.", "يُستعمل AST لتقييم أمراض الكبد والقلب؛ وعادةً يُطلب GOT مع GPT."),

 # ───────────────────────── 6. AST reference, significance & method
 {"topic_en": "AST reference, clinical significance & method", "topic_ar": "القيمة المرجعية والأهمية السريرية وطريقة AST"},
 W(Q("The reference value for AST (GOT) is:", "القيمة المرجعية لـ AST (GOT) هي:",
     O(("5–45 U/L", "5–45 U/L"), ("10–40 U/L", "10–40 U/L"), ("7–35 U/L", "7–35 U/L"), ("13–45 U/L", "13–45 U/L")), "a"),
   "AST reference value: 5–45 U/L.", "القيمة المرجعية لـ AST: 5–45 U/L."),
 W(Q("Which is listed as a cause of INCREASED AST levels?", "أيّها مذكور سببًا لارتفاع مستوى AST؟",
     O(("Myocardial infarction (MI)", "احتشاء العضلة القلبية (MI)"), ("Iron-deficiency anemia", "فقر الدم بعوز الحديد"), ("Hyperthyroidism", "فرط نشاط الدرقية"), ("Vitamin D excess", "زيادة فيتامين D")), "a"),
   "Increased AST: myocardial infarction (MI); liver diseases (acute, chronic, alcoholic hepatitis); hypothyroidism; trauma & irradiation of skeletal muscle; hemolytic anemia, exhaustion and heat stroke.", "يرتفع AST في: احتشاء العضلة القلبية (MI)؛ وأمراض الكبد (التهاب الكبد الحاد والمزمن والكحولي)؛ وقصور الدرقية؛ ورضّ العضلة الهيكلية وتشعيعها؛ وفقر الدم الانحلالي والإنهاك وضربة الحرّ."),
 W(Q("In the kinetic AST method, the indicator (second) reaction uses the enzyme:", "في طريقة AST الحركية، يستعمل التفاعل الكاشف (الثاني) الإنزيم:",
     O(("Malate dehydrogenase (MDH)", "نازعة هيدروجين المالات (MDH)"), ("Lactate dehydrogenase (LDH)", "نازعة هيدروجين اللاكتات (LDH)"), ("Alkaline phosphatase (ALP)", "الفوسفاتيز القلوي (ALP)"), ("Lipase", "اللايبيز")), "a"),
   "AST principle: L-aspartate + α-ketoglutarate —AST→ oxaloacetate + L-glutamate; then oxaloacetate + NADH + H⁺ —MDH→ L-malate + NAD⁺ (MDH = indicator).", "مبدأ AST: الأسبارتات-L + ألفا-كيتوغلوتارات —AST← أوكسالوأسيتات + غلوتامات-L؛ ثم أوكسالوأسيتات + NADH + H⁺ —MDH← مالات-L + NAD⁺ (MDH = الكاشف)."),
 W(Q("In the AST indicator reaction, oxaloacetate + NADH + H⁺ are converted by MDH to:", "في تفاعل AST الكاشف، يحوّل MDH الأوكسالوأسيتات + NADH + H⁺ إلى:",
     O(("L-malate + NAD⁺", "مالات-L + NAD⁺"), ("L-lactate + NAD⁺", "لاكتات-L + NAD⁺"), ("Pyruvate + glutamate", "بيروفات + غلوتامات"), ("Aspartate + glutamate", "أسبارتات + غلوتامات")), "a"),
   "MDH converts oxaloacetate + NADH + H⁺ → L-malate + NAD⁺; the fall in NADH is measured.", "يحوّل MDH الأوكسالوأسيتات + NADH + H⁺ ← مالات-L + NAD⁺؛ والمقاس انخفاض NADH."),
 W(Q("The SGOT (AST) activity is calculated as:", "يُحسب نشاط SGOT (AST) بالعلاقة:",
     O(("ΔA/min × 1745", "ΔA/min × 1745"), ("ΔA/min × 340", "ΔA/min × 340"), ("ΔA/min ÷ 1745", "ΔA/min ÷ 1745"), ("ΔA/min × 100", "ΔA/min × 100")), "a"),
   "SGOT activity (U/L) = ΔA/min × 1745 (same calculation form as SGPT).", "نشاط SGOT (U/L) = ΔA/min × 1745 (الصيغة نفسها كـ SGPT)."),
 W(Q("How does the AST reading differ from the ALT reading in the procedure?", "كيف تختلف قراءة AST عن قراءة ALT في الإجراء؟",
     O(("AST reads the change in absorbance per minute during 3 min", "تُقرأ AST بتغيّر الامتصاص كل دقيقة خلال 3 دقائق"), ("AST needs no incubation", "AST لا تحتاج حضنًا"), ("AST uses 10 µL sample", "AST تستعمل 10 µL عيّنة"), ("AST is not read spectrophotometrically", "AST لا تُقرأ طيفيًا")), "a"),
   "AST: mix and incubate 1 min at 37°C, then read ΔA per minute during 3 min (ALT reads per 20 sec during 1 min) — “same film, slight difference.”", "AST: يُمزج ويُحضَن دقيقة عند 37°م، ثم يُقرأ ΔA كل دقيقة خلال 3 دقائق (ALT تُقرأ كل 20 ثانية خلال دقيقة) — «نفس الفيلم باختلاف بسيط»."),
]
mcq = balance(mcq, 745)

meta = {"subject_en": "Clinical Enzymology", "subject_ar": "الإنزيمات السريرية", "short_ar": "انزيمات سريرية", "instructor": "د. بارق و د. هشام",
        "unit_en": "Lab 4", "unit_ar": "العملي 4", "unit_label": "LAB", "unit_no": "4",
        "title_en": "Liver Function Tests (LFT)", "title_ar": "فحوصات وظائف الكبد",
        "kind": "Laboratories — عملي", "stage": "The fourth stage — الرابعة",
        "file_name": "BIOS - انزيمات سريرية عملي - فحوصات وظائف الكبد - بنك أسئلة شامل"}

important = [
 IM("Define liver function tests (LFT) and list the major functions of the liver.", "عرّف فحوصات وظائف الكبد (LFT) واذكر وظائف الكبد الرئيسة.",
    "LFTs measure various chemicals in the blood made by the liver; an abnormal result indicates a liver problem and may help identify the cause. Major functions: 1) bile production and excretion; 2) excretion of bilirubin, cholesterol, hormones and drugs; 3) metabolism of fats, proteins and carbohydrates; 4) enzyme activation; 5) storage of glycogen, vitamins and minerals; 6) synthesis of plasma proteins (such as albumin) and clotting factors.",
    "تقيس فحوصات وظائف الكبد مواد كيميائية مختلفة في الدم يصنعها الكبد؛ والنتيجة غير الطبيعية تدلّ على مشكلة في الكبد وقد تساعد في معرفة السبب. ووظائف الكبد الرئيسة: 1) إنتاج الصفراء وإفرازها؛ 2) طرح البيليروبين والكوليسترول والهرمونات والأدوية؛ 3) أيض الدهون والبروتينات والكربوهيدرات؛ 4) تنشيط الإنزيمات؛ 5) خزن الغلايكوجين والفيتامينات والمعادن؛ 6) تصنيع بروتينات البلازما (مثل الألبومين) وعوامل التخثّر."),
 IM("List the five main tests used for liver function.", "عدّد الفحوصات الخمسة الرئيسة المستعملة لوظيفة الكبد.",
    "1) Alanine aminotransferase (ALT), also called glutamic-pyruvic transaminase (GPT). 2) Aspartate aminotransferase (AST), also called glutamic-oxaloacetic transaminase (GOT). 3) Serum bilirubin (total, direct and indirect). 4) Alkaline phosphatase (ALP). 5) Albumin, total protein, and others.",
    "1) ناقلة أمين الألانين (ALT) وتُسمّى ناقلة أمين الغلوتاميك-بيروفيك (GPT). 2) ناقلة أمين الأسبارتات (AST) وتُسمّى ناقلة أمين الغلوتاميك-أوكسالوأسيتيك (GOT). 3) البيليروبين المصلي (الكلّي والمباشر وغير المباشر). 4) الفوسفاتيز القلوي (ALP). 5) الألبومين والبروتين الكلّي وغيرها."),
 IM("Write the reaction catalyzed by ALT and state its other name.", "اكتب التفاعل الذي تحفّزه ALT واذكر اسمها الآخر.",
    "ALT (also called GPT) catalyzes a reversible transamination: it transfers an amino group from L-alanine to α-ketoglutarate to produce pyruvate and L-glutamate.",
    "تحفّز ALT (وتُسمّى GPT) نقل أمين عكوسًا: تنقل مجموعة أمين من الألانين-L إلى ألفا-كيتوغلوتارات لإنتاج البيروفات والغلوتامات-L."),
 IM("State the clinical significance (causes of increase) and reference values of ALT.", "اذكر الأهمية السريرية (أسباب الارتفاع) والقيم المرجعية لـ ALT.",
    "Increased ALT occurs in: hepatocellular disease, alcoholic cirrhosis, obstructive jaundice or biliary obstruction, viral/infectious/toxic hepatitis, myocardial infarction and heart failure, severe burns, and obesity. Reference values — Adults: males 10–40 U/L, females 7–35 U/L; newborns 13–45 U/L.",
    "يرتفع ALT في: مرض خلايا الكبد، والتشمّع الكحولي، واليرقان الانسدادي أو الانسداد الصفراوي، والتهاب الكبد الفيروسي/الإنتاني/السمّي، واحتشاء العضلة القلبية وفشل القلب، والحروق الشديدة، والسمنة. والقيم المرجعية — البالغون: الذكور 10–40 U/L، الإناث 7–35 U/L؛ وحديثو الولادة 13–45 U/L."),
 IM("Compare ALT and AST in specificity, sensitivity, and jaundice differentiation.", "قارن بين ALT وAST في النوعية والحساسية والتفريق بين أنواع اليرقان.",
    "ALT is more specific than AST for liver disease, but AST is more sensitive to alcoholic liver disease. ALT also helps differentiate between hemolytic jaundice and jaundice due to liver disease.",
    "ALT أكثر نوعية من AST لمرض الكبد، لكن AST أكثر حساسية لمرض الكبد الكحولي. وتساعد ALT أيضًا في التفريق بين اليرقان الانحلالي واليرقان الناتج عن مرض الكبد."),
 IM("Write the reaction catalyzed by AST, its required coenzyme, and its other name.", "اكتب التفاعل الذي تحفّزه AST، ومرافقها الإنزيمي اللازم، واسمها الآخر.",
    "AST (also called GOT) catalyzes the reversible conversion of aspartate and α-ketoglutarate to oxaloacetate and glutamate (aspartate donates its amino group to form oxaloacetate; α-ketoglutarate accepts the amino group to form glutamate). The reaction requires the coenzyme pyridoxine phosphate (a derivative of vitamin B6).",
    "تحفّز AST (وتُسمّى GOT) التحويل العكوس للأسبارتات وألفا-كيتوغلوتارات إلى أوكسالوأسيتات وغلوتامات (يتبرّع الأسبارتات بمجموعة الأمين فيتكوّن الأوكسالوأسيتات؛ وتقبلها ألفا-كيتوغلوتارات فيتكوّن الغلوتامات). ويتطلّب التفاعل المرافق الإنزيمي فوسفات البيريدوكسين (مشتقّ من فيتامين B6)."),
 IM("State the tissue distribution of GOT, its reference value, and the causes of its increase.", "اذكر توزيع GOT في الأنسجة، وقيمته المرجعية، وأسباب ارتفاعه.",
    "GOT is present in tissues of high metabolic activity: heart, liver, skeletal muscle, kidney, brain, pancreas, spleen and lungs; it is released into the circulation following injury or death of cells. Reference value: 5–45 U/L. Increased AST occurs in: myocardial infarction, liver diseases (acute, chronic, alcoholic hepatitis), hypothyroidism, trauma and irradiation of skeletal muscle, and hemolytic anemia, exhaustion and heat stroke.",
    "GOT موجود في أنسجة ذات نشاط أيضي عالٍ: القلب، والكبد، والعضلة الهيكلية، والكلية، والدماغ، والبنكرياس، والطحال، والرئتين؛ ويُطلق إلى الدوران عقب إصابة الخلايا أو موتها. وقيمته المرجعية: 5–45 U/L. ويرتفع AST في: احتشاء العضلة القلبية، وأمراض الكبد (التهاب الكبد الحاد والمزمن والكحولي)، وقصور الدرقية، ورضّ العضلة الهيكلية وتشعيعها، وفقر الدم الانحلالي والإنهاك وضربة الحرّ."),
 # ───── SA tied to the student's highlighted / pen-marked points
 IM("Marked by the student: explain the principle of the kinetic ALT (SGPT) determination (both reactions) and its calculation.", "مؤشَّر بالطالب: اشرح مبدأ تقدير ALT (SGPT) الحركي (التفاعلين) وطريقة حسابه.",
    "First reaction (ALT): L-alanine + α-ketoglutarate → pyruvate + L-glutamate. Second (indicator) reaction (LDH): pyruvate + NADH + H⁺ → L-lactate + NAD⁺. Procedure: 1000 µL work reagent + 100 µL sample, incubate 1 min at 37°C, then read ΔA every 20 sec for 1 min. Calculation: SGPT activity (U/L) = ΔA/min × 1745.",
    "التفاعل الأول (ALT): الألانين-L + ألفا-كيتوغلوتارات ← بيروفات + غلوتامات-L. والتفاعل الثاني (الكاشف، LDH): بيروفات + NADH + H⁺ ← لاكتات-L + NAD⁺. الإجراء: 1000 µL كاشف عامل + 100 µL عيّنة، يُحضَن دقيقة عند 37°م، ثم يُقرأ ΔA كل 20 ثانية لمدة دقيقة. والحساب: نشاط SGPT (U/L) = ΔA/min × 1745."),
 IM("Marked by the student: why is a second (indicator) reaction used instead of measuring pyruvate directly?", "مؤشَّر بالطالب: لماذا يُستعمل تفاعل ثانٍ (كاشف) بدلًا من قياس البيروفات مباشرةً؟",
    "Pyruvate is produced in direct proportion to the amount and activity of ALT, but measuring pyruvate itself is difficult. So a second (indicator) reaction is coupled: LDH consumes the NADH (converting it to NAD⁺) as it reduces pyruvate to lactate. The fall in NADH absorbance is easy to read spectrophotometrically and is proportional to ALT activity.",
    "يُنتَج البيروفات بتناسب طردي مع كمية ALT ونشاطها، لكن قياس البيروفات نفسه صعب. لذا يُقرَن تفاعل ثانٍ (كاشف): يستهلك LDH الـ NADH (محوّلًا إيّاه إلى NAD⁺) وهو يختزل البيروفات إلى لاكتات. وانخفاض امتصاص NADH سهل القراءة طيفيًا ويتناسب مع نشاط ALT."),
 IM("Marked by the student: explain the principle of the kinetic AST (SGOT) determination and how it differs from ALT.", "مؤشَّر بالطالب: اشرح مبدأ تقدير AST (SGOT) الحركي وكيف يختلف عن ALT.",
    "First reaction (AST): L-aspartate + α-ketoglutarate → oxaloacetate + L-glutamate. Second (indicator) reaction (MDH): oxaloacetate + NADH + H⁺ → L-malate + NAD⁺. It is essentially the “same film” as ALT with a slight difference: ALT couples to LDH (pyruvate → lactate) while AST couples to MDH (oxaloacetate → malate); and AST reads ΔA per minute during 3 min (ALT per 20 sec during 1 min). Calculation: SGOT activity (U/L) = ΔA/min × 1745.",
    "التفاعل الأول (AST): الأسبارتات-L + ألفا-كيتوغلوتارات ← أوكسالوأسيتات + غلوتامات-L. والتفاعل الثاني (الكاشف، MDH): أوكسالوأسيتات + NADH + H⁺ ← مالات-L + NAD⁺. وهو «نفس الفيلم» كـ ALT باختلاف بسيط: ALT يقترن بـ LDH (بيروفات ← لاكتات) بينما AST يقترن بـ MDH (أوكسالوأسيتات ← مالات)؛ وتُقرأ AST بتغيّر الامتصاص كل دقيقة خلال 3 دقائق (وALT كل 20 ثانية خلال دقيقة). والحساب: نشاط SGOT (U/L) = ΔA/min × 1745."),
 IM("Marked by the student: what does a low normal serum ALT level, rising with liver damage, make the enzyme useful for?", "مؤشَّر بالطالب: مستوى ALT المصلي المنخفض عادةً والذي يرتفع مع تلف الكبد — لأيّ غرض يجعل الإنزيم مفيدًا؟",
    "Normally only a low level of ALT exists in the serum. Because the level increases with liver damage, measuring it is used for screening and/or monitoring liver disease, and for monitoring the course of treatment for hepatitis and the effects of later drug therapy.",
    "عادةً لا يوجد في المصل إلا مستوى منخفض من ALT. ولأن المستوى يرتفع مع تلف الكبد، يُستعمل قياسه لفحص ومتابعة أمراض الكبد، ولمتابعة سير علاج التهاب الكبد وتأثيرات العلاج الدوائي اللاحق."),
 IM("Marked by the student: for which organs/diseases are ALT and AST ordered, and why are they often requested together?", "مؤشَّر بالطالب: لأيّ أعضاء/أمراض يُطلب ALT وAST، ولماذا يُطلبان معًا غالبًا؟",
    "ALT is most associated with the liver (more specific for liver disease), while AST (GOT) evaluates both liver and heart disease and is more sensitive to alcoholic liver disease. GOT is usually ordered along with GPT so that the pattern of the two enzymes helps localize and characterize the damage (e.g. hepatic vs cardiac/muscle).",
    "ترتبط ALT غالبًا بالكبد (أكثر نوعية لمرض الكبد)، بينما يقيّم AST (GOT) أمراض الكبد والقلب معًا وهو أكثر حساسية لمرض الكبد الكحولي. وعادةً يُطلب GOT مع GPT حتى يساعد نمط الإنزيمين على تحديد موضع الضرر وتوصيفه (كبدي أم قلبي/عضلي)."),
]

Qs = {"title_en": "Liver Function Tests (ALT/GPT & AST/GOT) — Comprehensive Questions (MCQ + SA)",
      "title_ar": "فحوصات وظائف الكبد (ALT/GPT وAST/GOT) — أسئلة شاملة (اختيار + مقالية)",
      "answers_inline": True, "mcq": ltr_all(mcq), "tf": [], "traps": [], "important": ltr_all(important)}
d = "/home/user/-/" + FOLDER
os.makedirs(d, exist_ok=True)
json.dump({"meta": meta, "questions": Qs}, open(d + "/lecture.json", "w"), ensure_ascii=False, indent=1)
from collections import Counter
qs = [m for m in mcq if "answer" in m]
print(FOLDER, len(qs), "MCQ", dict(Counter(m["answer"] for m in qs)), "| SA:", len(important), "| notes:", sum(1 for m in qs if m.get("note_en")))
