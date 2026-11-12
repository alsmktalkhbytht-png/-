---
source: BIOS-Obsidian/tools/scripts/enzq/q.py
handouts: []
saved: 2026-11-12
tags: [bios, code]
---
# enzq/q.py

Utility script.

```python
import sys, json, os
sys.path.insert(0, "/tmp/claude-0/-home-user-kwmdkm/44452a28-19bf-5ce8-890a-f6919e775f0b/scratchpad/imm456")
from ci import *            # Q P balance
sys.path.insert(0, "/tmp/claude-0/-home-user-kwmdkm/44452a28-19bf-5ce8-890a-f6919e775f0b/scratchpad"); from bidi import ltr_all

# Clinical Enzymology practical — Introduction of Enzymes (stage 4, د. بارق و د. هشام, user-confirmed).
# Source: 3-page student notes ("Abdullah Khalid"): definition, properties, sources, chemical composition, factors, blood enzymes.
# QUESTIONS ONLY — comprehensive MCQ bank; answers_inline (answer under the options + one short note line).
O = P
FOLDER = "enzymology-enzymes-intro-mcq"
W = lambda q, en, ar: dict(q, note_en=en, note_ar=ar)

mcq = [
 # ───────────────────────── 1. definition & functions
 {"topic_en": "Definition and functions", "topic_ar": "التعريف والوظائف"},
 W(Q("Enzymes are best defined as:", "تُعرَّف الإنزيمات بأنها:",
     O(("Biological catalysts that bring about chemical reactions in the living cell", "محفّزات حيوية تُحدث التفاعلات الكيميائية في الخلية الحيّة"), ("Structural proteins only", "بروتينات بنيوية فقط"), ("Energy molecules", "جزيئات طاقة"), ("Genetic material", "مادة وراثية")), "a"),
   "An enzyme is a biological catalyst that speeds up a reaction in the living cell.", "الإنزيم محفّز حيوي يسرّع التفاعل في الخلية الحيّة."),
 W(Q("Which is listed as a function of enzymes?", "أيّها مذكور وظيفةً للإنزيمات؟",
     O(("Digestion, respiration, and synthesis/breakdown of carbohydrates, proteins and fats", "الهضم والتنفّس وبناء/تحليل الكربوهيدرات والبروتينات والدهون"), ("Carrying oxygen only", "نقل الأكسجين فقط"), ("Storing genetic information", "خزن المعلومات الوراثية"), ("Forming the cell wall", "تكوين جدار الخلية")), "a"),
   "The notes list digestion, breathing, and synthesis/breakdown of CHO, proteins and fats.", "الملاحظات تذكر الهضم والتنفّس وبناء/تحليل الكربوهيدرات والبروتينات والدهون."),

 # ───────────────────────── 2. general properties
 {"topic_en": "General properties of enzymes", "topic_ar": "الصفات العامة للإنزيمات"},
 W(Q("According to the notes, all enzymes are chemically:", "حسب الملاحظات، كل الإنزيمات كيميائيًا:",
     O(("Lipids", "دهون"), ("Proteins", "بروتينات"), ("Carbohydrates", "كربوهيدرات"), ("Nucleic acids", "أحماض نووية")), "b"),
   "Property 1: all enzymes are proteins.", "الصفة 1: كل الإنزيمات بروتينات."),
 W(Q("Enzymes accelerate a reaction but do NOT:", "تُسرّع الإنزيمات التفاعل لكنها لا:",
     O(("Alter the reaction equilibrium", "تغيّر اتّزان التفاعل"), ("Speed up the reaction", "تسرّع التفاعل"), ("Lower activation energy", "تخفض طاقة التنشيط"), ("Act on substrates", "تؤثّر في المواد"), ), "a"),
   "They don’t change the equilibrium, aren’t consumed, and are needed in very small amounts.", "لا تغيّر الاتّزان، ولا تُستهلك، وتُحتاج بكميات صغيرة جدًا."),
 W(Q("Enzymes are required in the reaction in:", "تُحتاج الإنزيمات في التفاعل بكميات:",
     O(("Large quantities", "كبيرة"), ("Very small quantities", "صغيرة جدًا"), ("Equal amounts to the substrate", "مساوية للمادة"), ("No quantity", "معدومة")), "b"),
   "Enzymes are catalysts, so very small quantities are enough and they aren’t consumed.", "الإنزيمات محفّزات، فكميات صغيرة جدًا تكفي ولا تُستهلك."),
 W(Q("Enzymes are described as highly ___ for their substrate.", "تُوصف الإنزيمات بأنها عالية الـ ___ تجاه مادتها.",
     O(("Specific", "نوعية (تخصّصية)"), ("Random", "عشوائية"), ("Unstable", "عدم ثبات"), ("Soluble", "ذوبان")), "a"),
   "Property 3: enzymes are highly specific for their substrate.", "الصفة 3: الإنزيمات عالية النوعية تجاه مادتها."),
 W(Q("The part of the enzyme where it interacts with the substrate is the:", "الجزء من الإنزيم الذي يتفاعل فيه مع المادة هو:",
     O(("Prosthetic group", "المجموعة الاصطناعية"), ("Active site", "الموقع الفعّال"), ("Coenzyme", "المرافق الإنزيمي"), ("Apoenzyme", "الإنزيم الناقص")), "b"),
   "Property 4: enzymes possess an active site where interaction with the substrate takes place.", "الصفة 4: للإنزيم موقع فعّال يحدث فيه التفاعل مع المادة."),

 # ───────────────────────── 3. sources
 {"topic_en": "Sources of enzymes", "topic_ar": "مصادر الإنزيمات"},
 W(Q("Enzymes that function inside the cell are called:", "الإنزيمات التي تعمل داخل الخلية تُسمّى:",
     O(("Exoenzymes", "الإنزيمات الخارجية"), ("Endoenzymes", "الإنزيمات الداخلية"), ("Coenzymes", "المرافقات الإنزيمية"), ("Zymogens", "الطلائع (زيموجين)")), "b"),
   "Endoenzymes act within cells (most enzymes), e.g. metabolic oxidase.", "الإنزيمات الداخلية تعمل داخل الخلايا (معظم الإنزيمات)، مثل الأوكسيديز الأيضي."),
 W(Q("Digestive enzymes such as amylase, lipase and protease are examples of:", "الإنزيمات الهضمية مثل الأميليز واللايبيز والبروتييز أمثلة على:",
     O(("Endoenzymes", "الإنزيمات الداخلية"), ("Exoenzymes", "الإنزيمات الخارجية"), ("Coenzymes", "المرافقات الإنزيمية"), ("Apoenzymes", "الإنزيمات الناقصة")), "b"),
   "Exoenzymes are liberated by cells and catalyze reactions outside the cell (digestive enzymes).", "الإنزيمات الخارجية تُطلقها الخلايا وتحفّز تفاعلات خارج الخلية (الإنزيمات الهضمية)."),
 W(Q("“Metabolic oxidase” is given as an example of:", "«الأوكسيديز الأيضي» مذكور مثالًا على:",
     O(("An endoenzyme", "إنزيم داخلي"), ("An exoenzyme", "إنزيم خارجي"), ("A coenzyme", "مرافق إنزيمي"), ("A prosthetic group", "مجموعة اصطناعية")), "a"),
   "Metabolic oxidase works inside the cell → endoenzyme.", "الأوكسيديز الأيضي يعمل داخل الخلية ← إنزيم داخلي."),

 # ───────────────────────── 4. chemical composition
 {"topic_en": "Chemical composition", "topic_ar": "التركيب الكيميائي"},
 W(Q("Pepsin and trypsin are examples of enzymes that consist of:", "البيبسين والتربسين أمثلة على إنزيمات تتكوّن من:",
     O(("Protein only", "بروتين فقط"), ("Protein + coenzyme", "بروتين + مرافق إنزيمي"), ("Protein + prosthetic group", "بروتين + مجموعة اصطناعية"), ("Lipid only", "دهن فقط")), "a"),
   "Some enzymes are only protein (amino acids joined by peptide bonds), e.g. pepsin, trypsin.", "بعض الإنزيمات بروتين فقط (أحماض أمينية بروابط ببتيدية)، مثل البيبسين والتربسين."),
 W(Q("Protein (enzyme) + coenzyme together form a:", "البروتين (الإنزيم) + المرافق الإنزيمي يكوّنان:",
     O(("Holoenzyme", "الإنزيم الكامل (الهولوإنزيم)"), ("Apoenzyme", "الإنزيم الناقص"), ("Zymogen", "الطليعة (زيموجين)"), ("Substrate", "المادة")), "a"),
   "The complete, active enzyme = apoenzyme (protein) + its cofactor/coenzyme = holoenzyme.", "الإنزيم الكامل الفعّال = الإنزيم الناقص (البروتين) + مرافقه = الهولوإنزيم."),
 W(Q("The protein part of an enzyme (inactive alone) is the:", "الجزء البروتيني من الإنزيم (الخامل وحده) هو:",
     O(("Holoenzyme", "الهولوإنزيم"), ("Apoenzyme", "الإنزيم الناقص (الأبوإنزيم)"), ("Coenzyme", "المرافق الإنزيمي"), ("Cofactor", "العامل المرافق")), "b"),
   "Apoenzyme = the protein part; it is inactive until it binds its cofactor.", "الإنزيم الناقص = الجزء البروتيني؛ وهو خامل حتى يرتبط بعامله المرافق."),
 W(Q("A holoenzyme is made of:", "يتكوّن الهولوإنزيم من:",
     O(("Apoenzyme + prosthetic group (cofactor)", "إنزيم ناقص + مجموعة اصطناعية (عامل مرافق)"), ("Two substrates", "مادتين"), ("Protein + lipid", "بروتين + دهن"), ("Active site only", "موقع فعّال فقط")), "a"),
   "Holoenzyme (whole, active) = apoenzyme (protein) + prosthetic group / cofactor.", "الهولوإنزيم (الكامل الفعّال) = الإنزيم الناقص (البروتين) + المجموعة الاصطناعية/العامل المرافق."),
 W(Q("Coenzymes are typically:", "المرافقات الإنزيمية عادةً:",
     O(("Metal ions", "أيونات معدنية"), ("Organic molecules that help enzymes catalyse reactions", "جزيئات عضوية تساعد الإنزيمات على التحفيز"), ("Parts of the protein chain", "أجزاء من السلسلة البروتينية"), ("Substrates", "مواد تفاعل")), "b"),
   "Coenzymes are organic molecules with functionalities not found in proteins; they help catalysis.", "المرافقات الإنزيمية جزيئات عضوية فيها خصائص غير موجودة في البروتين؛ وتساعد في التحفيز."),
 W(Q("Cofactors are described in the notes as catalytically essential molecules or ions that are:", "تصف الملاحظات العوامل المرافقة بأنها جزيئات أو أيونات ضرورية للتحفيز:",
     O(("Covalently bound to the enzyme", "مرتبطة تساهميًا بالإنزيم"), ("Never bound to the enzyme", "غير مرتبطة بالإنزيم أبدًا"), ("Made of DNA", "مكوّنة من DNA"), ("The same as the substrate", "هي نفسها المادة")), "a"),
   "Per the notes, cofactors are catalytically essential and covalently bound to the enzyme.", "حسب الملاحظات، العوامل المرافقة ضرورية للتحفيز ومرتبطة تساهميًا بالإنزيم."),
 W(Q("In the diagram, the non-protein part that activates the apoenzyme is the:", "في الشكل، الجزء غير البروتيني الذي ينشّط الإنزيم الناقص هو:",
     O(("Substrate", "المادة"), ("Cofactor/coenzyme", "العامل المرافق/المرافق الإنزيمي"), ("Active site", "الموقع الفعّال"), ("Peptide bond", "الرابطة الببتيدية")), "b"),
   "Diagram: apoenzyme (protein, inactive) + cofactor (nonprotein, activator) → holoenzyme (active).", "الشكل: الإنزيم الناقص (بروتين خامل) + العامل المرافق (غير بروتيني، منشّط) ← الهولوإنزيم (الفعّال)."),

 # ───────────────────────── 5. active site & zymogen
 {"topic_en": "Active site and zymogen", "topic_ar": "الموقع الفعّال والطليعة"},
 W(Q("The active site of an enzyme is:", "الموقع الفعّال للإنزيم هو:",
     O(("The point where the enzyme interacts with the substrate", "النقطة التي يتفاعل فيها الإنزيم مع المادة"), ("The non-protein part", "الجزء غير البروتيني"), ("The whole enzyme", "الإنزيم كله"), ("A digestive enzyme", "إنزيم هضمي")), "a"),
   "The active site is the point at which interaction with the substrate occurs.", "الموقع الفعّال هو النقطة التي يحدث عندها التفاعل مع المادة."),
 W(Q("A zymogen (proenzyme) is correctly described as the ___ form of an enzyme.", "الطليعة الإنزيمية (زيموجين) تُوصف صحيحًا بأنها الصورة ___ للإنزيم.",
     O(("Active", "الفعّالة"), ("Inactive (precursor)", "غير الفعّالة (السليفة)"), ("Digestive", "الهضمية"), ("Protein-free", "الخالية من البروتين")), "b"),
   "⚠ The notes say zymogen is the “active” form, but a zymogen is the INACTIVE precursor that is later activated.", "⚠ تقول الملاحظات إن الزيموجين «الصورة الفعّالة»، والصحيح أنه السليفة غير الفعّالة التي تُنشَّط لاحقًا."),

 # ───────────────────────── 6. factors affecting enzyme activity
 {"topic_en": "Factors affecting enzyme activity", "topic_ar": "العوامل المؤثّرة في نشاط الإنزيم"},
 W(Q("If the amount of enzyme is doubled (substrate in excess), the reaction rate:", "إذا تضاعفت كمية الإنزيم (والمادة بوفرة)، فإن معدّل التفاعل:",
     O(("Is doubled", "يتضاعف"), ("Is halved", "ينتصف"), ("Stops", "يتوقّف"), ("Does not change", "لا يتغيّر")), "a"),
   "Rate is proportional to enzyme concentration — double the enzyme, double the rate.", "المعدّل يتناسب مع تركيز الإنزيم — مضاعفة الإنزيم تضاعف المعدّل."),
 W(Q("The rate of reaction is directly proportional to:", "معدّل التفاعل يتناسب طرديًا مع:",
     O(("The available substrate concentration", "تركيز المادة المتاح"), ("The temperature only", "درجة الحرارة فقط"), ("The pH only", "الأس الهيدروجيني فقط"), ("The colour of the tube", "لون الأنبوب")), "a"),
   "With more available substrate, the reaction rate rises (until the enzyme is saturated).", "بزيادة المادة المتاحة يرتفع المعدّل (حتى يتشبّع الإنزيم)."),
 W(Q("The optimum temperature for enzyme activity, as given in the notes, is:", "درجة الحرارة المثلى لنشاط الإنزيم كما في الملاحظات هي:",
     O(("0°C", "0°م"), ("37°C", "37°م"), ("60°C", "60°م"), ("100°C", "100°م")), "b"),
   "Rate rises with temperature up to a limit; the optimum is about 37°C.", "يرتفع المعدّل مع الحرارة حتى حدٍّ معيّن؛ والمثلى نحو 37°م."),
 W(Q("Which is listed as a factor affecting enzyme activity?", "أيّها مذكور عاملًا يؤثّر في نشاط الإنزيم؟",
     O(("Tube colour", "لون الأنبوب"), ("pH value", "قيمة الأس الهيدروجيني"), ("Patient age", "عمر المريض"), ("Light", "الضوء")), "b"),
   "The four factors: enzyme concentration, substrate concentration, temperature and pH value.", "العوامل الأربعة: تركيز الإنزيم، وتركيز المادة، ودرجة الحرارة، وقيمة الأس الهيدروجيني."),

 # ───────────────────────── 7. enzymes in blood
 {"topic_en": "Examples of enzymes in blood", "topic_ar": "أمثلة إنزيمات الدم"},
 W(Q("“AST” stands for:", "«AST» تعني:",
     O(("Aspartate aminotransferase", "ناقلة أمين الأسبارتات"), ("Alanine aminotransferase", "ناقلة أمين الألانين"), ("Alkaline phosphatase", "الفوسفاتيز القلوي"), ("Lactate dehydrogenase", "نازعة هيدروجين اللاكتات")), "a"),
   "AST = aspartate aminotransferase; ALT = alanine aminotransferase.", "AST = ناقلة أمين الأسبارتات؛ وALT = ناقلة أمين الألانين."),
 W(Q("“LDH” among the blood enzymes stands for:", "«LDH» من إنزيمات الدم تعني:",
     O(("Lactate dehydrogenase", "نازعة هيدروجين اللاكتات"), ("Liver dehydrogenase", "نازعة هيدروجين الكبد"), ("Lipase", "اللايبيز"), ("Alkaline phosphatase", "الفوسفاتيز القلوي")), "a"),
   "LDH = lactate dehydrogenase (a blood diagnostic enzyme).", "LDH = نازعة هيدروجين اللاكتات (إنزيم تشخيصي بالدم)."),
 W(Q("Which pair of digestive/pancreatic enzymes is listed among the blood enzyme examples?", "أيّ زوج من الإنزيمات الهضمية/البنكرياسية مذكور ضمن أمثلة إنزيمات الدم؟",
     O(("Amylase and lipase", "الأميليز واللايبيز"), ("Pepsin and trypsin", "البيبسين والتربسين"), ("AST and ALT", "AST وALT"), ("Oxidase and catalase", "الأوكسيديز والكاتاليز")), "a"),
   "The listed blood enzymes are AST, ALT, LDH, ALP, amylase and lipase.", "إنزيمات الدم المذكورة: AST وALT وLDH وALP والأميليز واللايبيز."),
 W(Q("“ALP / ALK” in the list refers to:", "«ALP / ALK» في القائمة تشير إلى:",
     O(("Alanine aminotransferase", "ناقلة أمين الألانين"), ("Alkaline phosphatase", "الفوسفاتيز القلوي"), ("Amylase", "الأميليز"), ("Lactate dehydrogenase", "نازعة هيدروجين اللاكتات")), "b"),
   "ALK/ALP = alkaline phosphatase.", "ALK/ALP = الفوسفاتيز القلوي."),
]
mcq = balance(mcq, 606)

meta = {"subject_en": "Clinical Enzymology", "subject_ar": "الإنزيمات السريرية", "short_ar": "انزيمات سريرية", "instructor": "د. بارق و د. هشام",
        "unit_en": "Introduction", "unit_ar": "مقدمة", "unit_label": "LAB", "unit_no": "",
        "title_en": "Introduction of Enzymes", "title_ar": "مقدمة في الإنزيمات",
        "kind": "Laboratories — عملي", "stage": "The fourth stage — الرابعة",
        "file_name": "BIOS - انزيمات سريرية عملي - مقدمة في الإنزيمات - بنك أسئلة شامل"}
important = [
 IM("Define an enzyme and state its main functions.", "عرّف الإنزيم واذكر وظائفه الرئيسة.",
    "An enzyme is a biological (protein) catalyst that brings about chemical reactions in the living cell. Functions: digestion, respiration (breathing), and the synthesis and breakdown of carbohydrates, proteins and fats.",
    "الإنزيم محفّز حيوي (بروتيني) يُحدث التفاعلات الكيميائية في الخلية الحيّة. ووظائفه: الهضم، والتنفّس، وبناء وتحليل الكربوهيدرات والبروتينات والدهون."),
 IM("List the general properties of enzymes.", "عدّد الصفات العامة للإنزيمات.",
    "1) All enzymes are proteins. 2) They accelerate the reaction but do not alter its equilibrium, are not consumed, and are needed in very small quantities. 3) They are highly specific for their substrate. 4) They possess an active site where interaction with the substrate takes place.",
    "1) كل الإنزيمات بروتينات. 2) تُسرّع التفاعل لكنها لا تغيّر اتّزانه، ولا تُستهلك، وتُحتاج بكميات صغيرة جدًا. 3) عالية النوعية تجاه مادتها. 4) لها موقع فعّال يحدث فيه التفاعل مع المادة."),
 IM("Differentiate between endoenzymes and exoenzymes, with an example of each.", "فرّق بين الإنزيمات الداخلية والخارجية مع مثال لكل منهما.",
    "Endoenzymes function within the cell (most enzymes), e.g. metabolic oxidase. Exoenzymes are liberated by cells and catalyze reactions outside the cell, e.g. digestive enzymes (amylase, lipase, protease).",
    "الإنزيمات الداخلية تعمل داخل الخلية (معظم الإنزيمات)، مثل الأوكسيديز الأيضي. والإنزيمات الخارجية تُطلقها الخلايا وتحفّز تفاعلات خارج الخلية، مثل الإنزيمات الهضمية (الأميليز، اللايبيز، البروتييز)."),
 IM("Classify enzymes according to their chemical composition.", "صنّف الإنزيمات حسب تركيبها الكيميائي.",
    "1) Enzymes made of protein only (e.g. pepsin, trypsin — amino acids joined by peptide bonds). 2) Protein (enzyme) + coenzyme = holoenzyme (protein part = apoenzyme). 3) Protein (enzyme) + prosthetic group (cofactor) = holoenzyme.",
    "1) إنزيمات من بروتين فقط (مثل البيبسين والتربسين — أحماض أمينية بروابط ببتيدية). 2) بروتين (إنزيم) + مرافق إنزيمي = هولوإنزيم (الجزء البروتيني = أبوإنزيم). 3) بروتين (إنزيم) + مجموعة اصطناعية (عامل مرافق) = هولوإنزيم."),
 IM("Define: holoenzyme, apoenzyme, coenzyme, cofactor, active site, and zymogen.", "عرّف: الهولوإنزيم، الأبوإنزيم، المرافق الإنزيمي، العامل المرافق، الموقع الفعّال، والزيموجين.",
    "Holoenzyme = the whole active enzyme (apoenzyme + prosthetic group). Apoenzyme = the protein part (inactive alone). Coenzyme = an organic molecule that helps catalysis. Cofactor = a catalytically essential molecule/ion bound to the enzyme. Active site = the point where the enzyme interacts with the substrate. Zymogen = the INACTIVE precursor of an enzyme (⚠ the source wrongly calls it the “active” form).",
    "الهولوإنزيم = الإنزيم الكامل الفعّال (أبوإنزيم + مجموعة اصطناعية). الأبوإنزيم = الجزء البروتيني (خامل وحده). المرافق الإنزيمي = جزيء عضوي يساعد في التحفيز. العامل المرافق = جزيء/أيون ضروري للتحفيز مرتبط بالإنزيم. الموقع الفعّال = النقطة التي يتفاعل فيها الإنزيم مع المادة. الزيموجين = السليفة غير الفعّالة للإنزيم (⚠ الملف يسمّيها خطأً «الصورة الفعّالة»)."),
 IM("List the factors affecting enzyme activity and the effect of each.", "عدّد العوامل المؤثّرة في نشاط الإنزيم وأثر كلٍّ منها.",
    "1) Enzyme concentration: doubling the enzyme doubles the reaction rate. 2) Substrate concentration: the rate is directly proportional to the available substrate. 3) Temperature: the rate rises with temperature up to a limit (optimum ≈ 37°C). 4) pH value.",
    "1) تركيز الإنزيم: مضاعفة الإنزيم تضاعف معدّل التفاعل. 2) تركيز المادة: المعدّل يتناسب طرديًا مع المادة المتاحة. 3) درجة الحرارة: يرتفع المعدّل مع الحرارة حتى حدٍّ معيّن (المثلى نحو 37°م). 4) قيمة الأس الهيدروجيني."),
 IM("Give examples of enzymes found in blood with their abbreviations.", "اذكر أمثلة على الإنزيمات الموجودة في الدم مع اختصاراتها.",
    "AST (aspartate aminotransferase), ALT (alanine aminotransferase), LDH (lactate dehydrogenase), ALP/ALK (alkaline phosphatase), amylase and lipase.",
    "AST (ناقلة أمين الأسبارتات)، ALT (ناقلة أمين الألانين)، LDH (نازعة هيدروجين اللاكتات)، ALP/ALK (الفوسفاتيز القلوي)، والأميليز واللايبيز."),
 IM("Using the diagram, explain how an inactive apoenzyme becomes an active holoenzyme.", "باستعمال الشكل، اشرح كيف يصبح الأبوإنزيم الخامل هولوإنزيمًا فعّالًا.",
    "The apoenzyme is the protein part and is inactive on its own. When it binds its cofactor (the nonprotein part / activator), it becomes the holoenzyme — the whole, active enzyme that can then bind the substrate at its active site.",
    "الأبوإنزيم هو الجزء البروتيني وهو خامل وحده. وعندما يرتبط بعامله المرافق (الجزء غير البروتيني/المنشّط) يصبح هولوإنزيمًا — الإنزيم الكامل الفعّال الذي يرتبط بعدها بالمادة في موقعه الفعّال."),
 # ───── more SA tied to the student’s highlighted points
 IM("Marked by the student: what is meant by “enzymes are not consumed and do not alter the equilibrium”?", "مؤشَّر بالطالب: ما المقصود بأن الإنزيمات «لا تُستهلك ولا تغيّر الاتّزان»؟",
    "As catalysts, enzymes speed up a reaction without being used up, so the same enzyme molecule works repeatedly and only very small amounts are needed. They lower the time to reach equilibrium but do not change the position of the equilibrium itself.",
    "بوصفها محفّزات، تُسرّع الإنزيمات التفاعل دون أن تُستهلك، فيعمل الجزيء نفسه مرارًا وتكفي كميات صغيرة جدًا. وهي تقصّر زمن بلوغ الاتّزان لكنها لا تغيّر موضع الاتّزان نفسه."),
 IM("Marked by the student: explain the effect of enzyme concentration and substrate concentration on the reaction rate.", "مؤشَّر بالطالب: اشرح أثر تركيز الإنزيم وتركيز المادة في معدّل التفاعل.",
    "Enzyme concentration: if the enzyme amount is doubled (substrate in excess), the reaction rate is doubled — the rate is proportional to enzyme concentration. Substrate concentration: the rate is directly proportional to the available substrate (until the enzyme becomes saturated).",
    "تركيز الإنزيم: إذا تضاعفت كمية الإنزيم (والمادة بوفرة) تضاعف المعدّل — فالمعدّل يتناسب مع تركيز الإنزيم. تركيز المادة: المعدّل يتناسب طرديًا مع المادة المتاحة (حتى يتشبّع الإنزيم)."),
 IM("Marked by the student: how does temperature affect enzyme activity, and what is the optimum?", "مؤشَّر بالطالب: كيف تؤثّر درجة الحرارة في نشاط الإنزيم، وما الدرجة المثلى؟",
    "The rate increases as temperature rises, but only up to a certain limit; beyond it the enzyme (a protein) denatures and activity falls. The optimum temperature is about 37°C.",
    "يزداد المعدّل بارتفاع الحرارة لكن حتى حدٍّ معيّن؛ وبعده يتمسّخ الإنزيم (وهو بروتين) ويقلّ نشاطه. والدرجة المثلى نحو 37°م."),
 IM("Marked by the student: differentiate between a coenzyme and a cofactor.", "مؤشَّر بالطالب: فرّق بين المرافق الإنزيمي والعامل المرافق.",
    "A coenzyme is typically an organic molecule that helps the enzyme catalyse the reaction and has functionalities not found in proteins. A cofactor is a catalytically essential molecule or ion that is bound to the enzyme (the notes say covalently bound). Both are the non-protein part that activates the apoenzyme.",
    "المرافق الإنزيمي عادةً جزيء عضوي يساعد الإنزيم على التحفيز وفيه خصائص غير موجودة في البروتين. والعامل المرافق جزيء أو أيون ضروري للتحفيز مرتبط بالإنزيم (الملاحظات تقول تساهميًا). وكلاهما الجزء غير البروتيني الذي ينشّط الأبوإنزيم."),
]
Qs = {"title_en": "Introduction of Enzymes — Comprehensive Questions (MCQ + SA)", "title_ar": "مقدمة في الإنزيمات — أسئلة شاملة (اختيار + مقالية)",
      "answers_inline": True, "mcq": ltr_all(mcq), "tf": [], "traps": [], "important": ltr_all(important)}
d = "/home/user/-/" + FOLDER
os.makedirs(d, exist_ok=True)
json.dump({"meta": meta, "questions": Qs}, open(d + "/lecture.json", "w"), ensure_ascii=False, indent=1)
from collections import Counter
qs = [m for m in mcq if "answer" in m]
print(FOLDER, len(qs), "MCQ", dict(Counter(m["answer"] for m in qs)), "| notes:", sum(1 for m in qs if m.get("note_en")))

```
