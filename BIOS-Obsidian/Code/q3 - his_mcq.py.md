---
source: BIOS-Obsidian/tools/scripts/q3/his_mcq.py
handouts: []
saved: 2026-11-12
tags: [bios, code]
---
# q3/his_mcq.py

Utility script.

```python
"""MCQ-only banks (answer under each question) for Histology practical labs 2, 3, 4 — stage 2, م.م. جنان خليل."""
import sys, json, os
sys.path.insert(0, "/tmp/claude-0/-home-user-kwmdkm/44452a28-19bf-5ce8-890a-f6919e775f0b/scratchpad/bac")
from bal import balance

def Q(en, ar, opts, ans): return dict(en=en, ar=ar, options=[list(o) for o in opts], answer=ans)
def TOP(en, ar): return dict(topic_en=en, topic_ar=ar)

NUM = {2: "الثانية", 3: "الثالثة", 4: "الرابعة"}
def save(no, title_en, title_ar, mcq, seed):
    mcq = balance(mcq, seed)
    for q in mcq:
        if "answer" in q: q["answer"] = q["answer"].upper()
    folder = f"/home/user/-/histology-lab{no}-mcq"; os.makedirs(folder, exist_ok=True)
    data = {"meta": {"subject_en": "Histology", "subject_ar": "علم الأنسجة", "short_ar": "أنسجة", "unit_label": "LAB",
                     "unit_en": f"Lab {no}", "unit_ar": f"العملي {no}", "unit_no": str(no), "title_en": title_en, "title_ar": title_ar,
                     "kind": "Laboratories — عملي", "stage": "The second stage — الثانية", "instructor": "م.م. جنان خليل",
                     "department": "قسم التحليلات", "questions_kind": "MCQ — أسئلة اختيار",
                     "file_name": f"BIOS - أنسجة عملي المحاضرة {NUM[no]} - الأسئلة"},
            "questions": {"title_en": title_en, "title_ar": title_ar, "sub": "MCQ", "answers_inline": True,
                          "mcq_en": f"Comprehensive MCQs — Lab {no}", "mcq_ar": f"أسئلة اختيار شاملة — العملي {no}",
                          "intro_en": ["Choose the correct answer.", "The answer is in the box under each question."],
                          "intro_ar": ["اختر الإجابة الصحيحة.", "الحل في المربع تحت كل سؤال."],
                          "mcq": mcq}}
    json.dump(data, open(folder + "/lecture.json", "w"), ensure_ascii=False, indent=1)
    n = [q for q in mcq if "answer" in q]
    from collections import Counter
    print(folder, len(n), dict(Counter(q["answer"] for q in n)))

# ───────────────────────── Lab 2 — Classification of Epithelial Tissue
L2 = [
 TOP("Groups of epithelia and number of layers", "مجموعات الظهارة وعدد الطبقات"),
 Q("Epithelia are divided into two main groups according to their:", "تُقسَّم الظهارة إلى مجموعتين رئيستين بحسب:", [("Structure and function", "التركيب والوظيفة"), ("Color and size", "اللون والحجم"), ("Blood supply", "التجهيز الدموي"), ("Nerve supply", "التجهيز العصبي")], "a"),
 Q("The two main groups of epithelia are:", "المجموعتان الرئيستان للظهارة:", [("Simple and stratified", "البسيطة والمطبّقة"), ("Covering & lining and glandular", "المغطّية والمبطّنة، والغدّية"), ("Squamous and cuboidal", "الحرشفية والمكعّبة"), ("Ciliated and non-ciliated", "المهدّبة وغير المهدّبة")], "b"),
 Q("Glandular epithelia:", "الظهارة الغدّية:", [("Line the blood vessels", "تبطّن الأوعية الدموية"), ("Form the outer layer of the skin", "تكوّن الطبقة الخارجية للجلد"), ("Form the glands within the body", "تكوّن الغدد داخل الجسم"), ("Cover the ventral body cavity", "تغطّي التجويف البطني")], "c"),
 Q("Covering and lining epithelia are classified according to the number of cellular layers into all EXCEPT:", "تُصنَّف الظهارة المغطّية والمبطّنة بحسب عدد الطبقات إلى كل ما يأتي ما عدا:", [("Simple", "بسيطة"), ("Stratified", "مطبّقة"), ("Pseudostratified", "مطبّقة كاذبة"), ("Glandular", "غدّية")], "d"),
 Q("A simple epithelium is:", "الظهارة البسيطة:", [("One cell layer thick, all cells touch the basement membrane", "طبقة خلوية واحدة وكل الخلايا تلامس الغشاء القاعدي"), ("Two or more layers", "طبقتان أو أكثر"), ("Only the basal cells touch the basement membrane", "الخلايا القاعدية فقط تلامس الغشاء القاعدي"), ("Always keratinized", "متقرّنة دائمًا")], "a"),
 Q("A simple epithelium is found where the primary function is:", "توجد الظهارة البسيطة حيث الوظيفة الأساسية:", [("Protection against abrasion", "الحماية من الاحتكاك"), ("Filtration, absorption or secretion", "الترشيح أو الامتصاص أو الإفراز"), ("Mechanical stress", "تحمّل الإجهاد الميكانيكي"), ("Stretching", "التمدّد")], "b"),
 Q("Which is an example location of simple epithelium?", "أي مما يأتي موقع للظهارة البسيطة؟", [("Skin", "الجلد"), ("Esophagus", "المريء"), ("Air sacs of the lung", "الأكياس الهوائية للرئة"), ("Pharynx", "البلعوم")], "c"),
 Q("In a stratified epithelium, the cells in direct contact with the basement membrane are:", "في الظهارة المطبّقة، الخلايا الملامسة مباشرة للغشاء القاعدي هي:", [("All the cells", "كل الخلايا"), ("The apical cells", "الخلايا القمّية"), ("The middle cells", "الخلايا الوسطى"), ("Only the basal (deepest) layer", "الطبقة القاعدية (الأعمق) فقط")], "d"),
 Q("A stratified epithelium is found in areas subjected to:", "توجد الظهارة المطبّقة في مناطق معرّضة لـ:", [("Abrasive activities or mechanical stress", "الاحتكاك أو الإجهاد الميكانيكي"), ("Filtration", "الترشيح"), ("Gas exchange", "تبادل الغازات"), ("Absorption only", "الامتصاص فقط")], "a"),
 Q("The stratified epithelium is compared to:", "تُشبَّه الظهارة المطبّقة بـ:", [("A honeycomb", "قرص العسل"), ("A brick wall", "جدار من الطابوق"), ("A fishing net", "شبكة صيد"), ("A ladder", "سُلّم")], "b"),
 Q("In stratified epithelium, lost apical cells are replaced by:", "في الظهارة المطبّقة تُعوَّض الخلايا القمّية المفقودة بـ:", [("Goblet cells", "الخلايا الكأسية"), ("Blood cells", "خلايا الدم"), ("Continuous regeneration of basal cells", "التجدّد المستمر للخلايا القاعدية"), ("Fibroblasts", "الأرومات الليفية")], "c"),
 Q("Pseudostratified epithelium looks layered because:", "تبدو الظهارة المطبّقة الكاذبة طبقات لأن:", [("It has many layers", "فيها طبقات كثيرة"), ("Cells are keratinized", "الخلايا متقرّنة"), ("Cells are binucleated", "الخلايا ثنائية النواة"), ("Nuclei lie at different levels", "الأنوية في مستويات مختلفة")], "d"),
 Q("Pseudostratified epithelium is classified as a type of simple epithelium because:", "تُصنَّف الظهارة المطبّقة الكاذبة نوعًا من البسيطة لأن:", [("All cells are attached to the basement membrane", "كل الخلايا مرتبطة بالغشاء القاعدي"), ("All cells reach the apical surface", "كل الخلايا تصل السطح القمّي"), ("It has one nucleus level", "أنويتها في مستوى واحد"), ("It lacks cilia", "تفتقد الأهداب")], "a"),
 TOP("Simple epithelia by cell shape", "الظهارة البسيطة بحسب شكل الخلية"),
 Q("Simple squamous cells are:", "خلايا الظهارة الحرشفية البسيطة:", [("Tall with oval basal nuclei", "طويلة بأنوية بيضوية قاعدية"), ("Flat (scales) with a disk-shaped flattened nucleus", "مسطّحة (حراشف) بنواة قرصية مسطّحة"), ("Square with round central nuclei", "مربّعة بأنوية مستديرة مركزية"), ("Binucleated", "ثنائية النواة")], "b"),
 Q("Simple squamous epithelium is thin enough to allow:", "الظهارة الحرشفية البسيطة رقيقة بما يكفي لـ:", [("Keratin production", "إنتاج الكيراتين"), ("Mucus secretion", "إفراز المخاط"), ("Passive diffusion", "الانتشار المنفعل"), ("Stretching", "التمدّد")], "c"),
 Q("The endothelium lining blood vessels is:", "البطانة التي تبطّن الأوعية الدموية:", [("Simple cuboidal", "مكعّبة بسيطة"), ("Stratified squamous", "حرشفية مطبّقة"), ("Transitional", "انتقالية"), ("Simple squamous", "حرشفية بسيطة")], "d"),
 Q("The mesothelium gets its name from the germ layer:", "يأخذ الميزوثيليوم اسمه من الطبقة الجرثومية:", [("Mesoderm", "الأديم المتوسط"), ("Ectoderm", "الأديم الظاهر"), ("Endoderm", "الأديم الباطن"), ("Neural crest", "العُرف العصبي")], "a"),
 Q("Simple cuboidal cells are:", "خلايا الظهارة المكعّبة البسيطة:", [("Taller than wide", "أطول من عرضها"), ("As tall as they are wide, with large round central nuclei", "طولها يساوي عرضها، بأنوية كبيرة مستديرة مركزية"), ("Flat", "مسطّحة"), ("Without nuclei", "بلا أنوية")], "b"),
 Q("Simple cuboidal epithelium is found in:", "توجد الظهارة المكعّبة البسيطة في:", [("Epidermis", "البشرة"), ("Urinary bladder", "المثانة"), ("Small collecting ducts of kidney, pancreas and salivary glands", "القنوات الجامعة الصغيرة للكلية والبنكرياس والغدد اللعابية"), ("Air sacs", "الأكياس الهوائية")], "c"),
 Q("The important functions of simple cuboidal epithelium are:", "الوظائف المهمة للظهارة المكعّبة البسيطة:", [("Protection", "الحماية"), ("Stretching", "التمدّد"), ("Diffusion only", "الانتشار فقط"), ("Secretion and absorption", "الإفراز والامتصاص")], "d"),
 Q("In simple columnar epithelium, the nucleus is:", "في الظهارة العمودية البسيطة تكون النواة:", [("Oval, close to the basal region", "بيضوية قريبة من المنطقة القاعدية"), ("Disk-shaped, flattened", "قرصية مسطّحة"), ("Absent", "غائبة"), ("Round, central", "مستديرة مركزية")], "a"),
 Q("Simple columnar epithelium lines the:", "تبطّن الظهارة العمودية البسيطة:", [("Esophagus", "المريء"), ("Stomach and uterine cervix", "المعدة وعنق الرحم"), ("Blood vessels", "الأوعية الدموية"), ("Urinary bladder", "المثانة")], "b"),
 Q("Non-ciliated columnar epithelium of the small intestine contains:", "تحتوي الظهارة العمودية غير المهدّبة في الأمعاء الدقيقة على:", [("Keratin", "الكيراتين"), ("Binucleated cells", "خلايا ثنائية النواة"), ("Microvilli and goblet cells", "زغيبات وخلايا كأسية"), ("Stem cells only", "خلايا جذعية فقط")], "c"),
 Q("In pseudostratified columnar epithelium, the shorter cells are:", "في الظهارة العمودية المطبّقة الكاذبة، الخلايا الأقصر هي:", [("Goblet cells", "خلايا كأسية"), ("Dead cells", "خلايا ميّتة"), ("Keratinocytes", "خلايا متقرّنة"), ("Stem cells", "خلايا جذعية")], "d"),
 Q("EM shows that pseudostratified columnar epithelium is 'simple' because:", "يُظهر المجهر الإلكتروني أن الظهارة العمودية المطبّقة الكاذبة 'بسيطة' لأن:", [("All its cells contact the basement membrane", "كل خلاياها تلامس الغشاء القاعدي"), ("It has one layer of nuclei", "فيها طبقة أنوية واحدة"), ("All cells reach the surface", "كل الخلايا تصل السطح"), ("It lacks goblet cells", "تفتقد الخلايا الكأسية")], "a"),
 Q("Pseudostratified ciliated columnar epithelium is found in:", "توجد الظهارة العمودية المطبّقة الكاذبة المهدّبة في:", [("Male urethra", "الإحليل الذكري"), ("Larger air passageways of the respiratory system", "المجاري الهوائية الكبيرة للجهاز التنفسي"), ("Skin", "الجلد"), ("Kidney tubules", "نبيبات الكلية")], "b"),
 Q("Pseudostratified non-ciliated columnar epithelium occurs in:", "توجد الظهارة العمودية المطبّقة الكاذبة غير المهدّبة في:", [("Trachea", "الرغامى"), ("Stomach", "المعدة"), ("Part of the male urethra and epididymis", "جزء من الإحليل الذكري والبربخ"), ("Esophagus", "المريء")], "c"),
 TOP("Stratified epithelia", "الظهارة المطبّقة"),
 Q("Stratified epithelia are classified according to the shape of the cells of the:", "تُصنَّف الظهارة المطبّقة بحسب شكل خلايا:", [("Basal layer", "الطبقة القاعدية"), ("Middle layer", "الطبقة الوسطى"), ("Basement membrane", "الغشاء القاعدي"), ("Superficial layer", "الطبقة السطحية")], "d"),
 Q("In stratified squamous epithelium, the basal cells are:", "في الظهارة الحرشفية المطبّقة تكون الخلايا القاعدية:", [("Cuboidal or polyhedral", "مكعّبة أو متعدّدة الأوجه"), ("Flat", "مسطّحة"), ("Ciliated", "مهدّبة"), ("Dead", "ميّتة")], "a"),
 Q("Non-keratinized stratified squamous epithelium:", "الظهارة الحرشفية المطبّقة غير المتقرّنة:", [("Has dead superficial cells", "خلاياها السطحية ميّتة"), ("Has living cells up to the surface, kept moist", "خلاياها حيّة حتى السطح ومرطّبة"), ("Is filled with keratin", "مملوءة بالكيراتين"), ("Forms the epidermis", "تكوّن البشرة")], "b"),
 Q("Non-keratinized stratified squamous epithelium lines all EXCEPT:", "تبطّن الظهارة الحرشفية المطبّقة غير المتقرّنة كل ما يأتي ما عدا:", [("Oral cavity", "تجويف الفم"), ("Esophagus", "المريء"), ("Epidermis of the skin", "بشرة الجلد"), ("Vagina", "المهبل")], "c"),
 Q("Keratinized stratified squamous epithelium has superficial cells that are:", "خلايا الظهارة الحرشفية المطبّقة المتقرّنة السطحية:", [("Alive and nucleated", "حيّة ومنوّاة"), ("Ciliated", "مهدّبة"), ("Binucleated", "ثنائية النواة"), ("Dead, without nuclei, filled with keratin", "ميّتة بلا أنوية ومملوءة بالكيراتين")], "d"),
 Q("The epidermis of the skin consists of:", "تتكوّن بشرة الجلد من:", [("Keratinized stratified squamous epithelium", "ظهارة حرشفية مطبّقة متقرّنة"), ("Non-keratinized stratified squamous", "حرشفية مطبّقة غير متقرّنة"), ("Transitional", "انتقالية"), ("Simple columnar", "عمودية بسيطة")], "a"),
 Q("Stratified cuboidal epithelium forms the walls of:", "تكوّن الظهارة المكعّبة المطبّقة جدران:", [("Air sacs", "الأكياس الهوائية"), ("Large ducts of exocrine glands such as sweat gland ducts", "القنوات الكبيرة للغدد خارجية الإفراز مثل قنوات الغدد العرقية"), ("Blood vessels", "الأوعية الدموية"), ("Urinary bladder", "المثانة")], "b"),
 Q("Stratified columnar epithelium is:", "الظهارة العمودية المطبّقة:", [("The most common epithelium", "أكثر الظهارات شيوعًا"), ("Found in the skin", "موجودة في الجلد"), ("Relatively rare; in large ducts of salivary glands and membranous male urethra", "نادرة نسبيًا؛ في القنوات الكبيرة للغدد اللعابية والجزء الغشائي للإحليل الذكري"), ("Columnar in all layers", "عمودية في كل الطبقات")], "c"),
 Q("Transitional epithelium is limited to the:", "تقتصر الظهارة الانتقالية على:", [("Respiratory tract", "الجهاز التنفسي"), ("Digestive tract", "الجهاز الهضمي"), ("Skin", "الجلد"), ("Urinary tract", "الجهاز البولي")], "d"),
 Q("In a relaxed state, the apical cells of transitional epithelium are:", "في حالة الارتخاء تكون الخلايا القمّية للظهارة الانتقالية:", [("Large and rounded", "كبيرة ومستديرة"), ("Flat", "مسطّحة"), ("Columnar", "عمودية"), ("Dead", "ميّتة")], "a"),
 Q("A distinguishing feature of transitional epithelium is:", "من الصفات المميّزة للظهارة الانتقالية:", [("Keratin", "الكيراتين"), ("Some binucleated cells", "وجود بعض الخلايا ثنائية النواة"), ("Cilia", "الأهداب"), ("Goblet cells", "الخلايا الكأسية")], "b"),
 Q("When stretched, transitional epithelium may be confused with:", "عند التمدّد قد تختلط الظهارة الانتقالية بـ:", [("Simple cuboidal", "المكعّبة البسيطة"), ("Pseudostratified columnar", "العمودية المطبّقة الكاذبة"), ("Non-keratinized stratified squamous epithelium", "الظهارة الحرشفية المطبّقة غير المتقرّنة"), ("Simple columnar", "العمودية البسيطة")], "c"),
]

# ───────────────────────── Lab 3 — Glandular Epithelial Tissue
L3 = [
 TOP("Glands: general", "الغدد: عام"),
 Q("Glandular epithelium is formed by cells specialized to:", "تتكوّن الظهارة الغدّية من خلايا متخصّصة لـ:", [("Contract", "الانقباض"), ("Produce secretion", "إنتاج الإفراز"), ("Conduct impulses", "توصيل السيالات"), ("Store fat", "خزن الدهون")], "b"),
 Q("Glands arise in the embryo from:", "تنشأ الغدد في الجنين من:", [("Invaginations of epithelium into connective tissue", "انغمادات الظهارة في النسيج الضام"), ("Muscle cells", "الخلايا العضلية"), ("Nerve cells", "الخلايا العصبية"), ("Blood vessels", "الأوعية الدموية")], "a"),
 Q("Glandular secretions include all EXCEPT:", "تشمل الإفرازات الغدّية كل ما يأتي ما عدا:", [("Mucin", "الميوسين"), ("Hormones", "الهرمونات"), ("Enzymes", "الإنزيمات"), ("Collagen fibers", "ألياف الكولاجين")], "d"),
 Q("Glands are classified as endocrine or exocrine depending on:", "تُصنَّف الغدد إلى صمّاء وخارجية الإفراز بحسب:", [("Their size", "حجمها"), ("Their color", "لونها"), ("Whether they have a duct", "وجود قناة"), ("Number of cells", "عدد الخلايا")], "c"),
 Q("Endocrine glands:", "الغدد الصمّاء:", [("Lack ducts and secrete into interstitial fluid and blood", "تفتقد القنوات وتفرز في السائل الخلالي والدم"), ("Have long ducts", "لها قنوات طويلة"), ("Secrete onto the skin", "تفرز على الجلد"), ("Are always unicellular", "أحادية الخلية دائمًا")], "a"),
 Q("The secretions of endocrine glands are called:", "تُسمّى إفرازات الغدد الصمّاء:", [("Enzymes", "الإنزيمات"), ("Hormones", "الهرمونات"), ("Mucins", "الميوسينات"), ("Sebum", "الزهم")], "b"),
 TOP("Exocrine glands", "الغدد خارجية الإفراز"),
 Q("Exocrine glands maintain contact with the epithelial surface by:", "تحافظ الغدد خارجية الإفراز على صلتها بالسطح الظهاري بواسطة:", [("Blood vessels", "الأوعية الدموية"), ("Nerves", "الأعصاب"), ("Hormones", "الهرمونات"), ("A duct", "قناة")], "d"),
 Q("A duct is:", "القناة هي:", [("An epithelium-lined tube that discharges secretions onto the epithelial surface", "أنبوب مبطّن بالظهارة يصبّ الإفرازات على السطح الظهاري"), ("A blood vessel", "وعاء دموي"), ("A nerve", "عصب"), ("A muscle", "عضلة")], "a"),
 Q("Enzymes from the pancreas into the small intestine is an example of secretion onto:", "الإنزيمات من البنكرياس إلى الأمعاء الدقيقة مثال على الإفراز على:", [("The skin surface", "سطح الجلد"), ("An epithelial surface lining an internal passageway", "سطح ظهاري يبطّن ممرًا داخليًا"), ("The blood", "الدم"), ("The interstitial fluid", "السائل الخلالي")], "b"),
 Q("A unicellular exocrine gland:", "الغدة خارجية الإفراز أحادية الخلية:", [("Has a long duct", "لها قناة طويلة"), ("Is deep in connective tissue", "عميقة في النسيج الضام"), ("Usually has no duct and lies close to the epithelial surface", "عادةً بلا قناة وقريبة من السطح الظهاري"), ("Secretes hormones", "تفرز الهرمونات")], "c"),
 Q("The most common unicellular exocrine gland is the:", "أكثر الغدد خارجية الإفراز أحادية الخلية شيوعًا:", [("Sebaceous gland", "الغدة الدهنية"), ("Sweat gland", "الغدة العرقية"), ("Mammary gland", "الغدة الثديية"), ("Goblet cell", "الخلية الكأسية")], "d"),
 Q("Goblet cells are found in the:", "توجد الخلايا الكأسية في:", [("Respiratory tract and intestine", "الجهاز التنفسي والأمعاء"), ("Skin", "الجلد"), ("Bone", "العظم"), ("Blood vessels", "الأوعية الدموية")], "a"),
 Q("Multicellular exocrine glands are classified according to how many criteria?", "تُصنَّف الغدد خارجية الإفراز متعدّدة الخلايا وفق كم معيارًا؟", [("Two", "اثنين"), ("Three", "ثلاثة"), ("Four", "أربعة"), ("Five", "خمسة")], "b"),
 Q("Classification by form and structure (morphology) is considered:", "التصنيف بحسب الشكل والتركيب يُعدّ تصنيفًا:", [("Physiologic", "وظيفيًا"), ("Chemical", "كيميائيًا"), ("Anatomic", "تشريحيًا"), ("Genetic", "وراثيًا")], "c"),
 Q("Classification by type and method of secretion is considered:", "التصنيف بحسب نوع الإفراز وطريقته يُعدّ تصنيفًا:", [("Anatomic", "تشريحيًا"), ("Embryologic", "جنينيًا"), ("Morphologic", "شكليًا"), ("Physiologic", "وظيفيًا")], "d"),
 TOP("Form and structure", "الشكل والتركيب"),
 Q("Simple glands have:", "الغدد البسيطة لها:", [("A single, unbranched duct", "قناة واحدة غير متفرّعة"), ("Ducts that branch repeatedly", "قنوات تتفرّع مرارًا"), ("No duct", "بلا قناة"), ("Two ducts", "قناتان")], "a"),
 Q("Compound glands have:", "الغدد المركّبة لها:", [("A single duct", "قناة واحدة"), ("Ducts that branch repeatedly", "قنوات تتفرّع مرارًا"), ("No secretory portion", "بلا جزء إفرازي"), ("No duct", "بلا قناة")], "b"),
 Q("If the secretory portion and duct have uniform diameter, the gland is:", "إذا كان قطر الجزء الإفرازي والقناة متساويًا فالغدة:", [("Acinar", "عنبية"), ("Alveolar", "سنخية"), ("Tubular", "أنبوبية"), ("Tubuloacinar", "أنبوبية عنبية")], "c"),
 Q("Which is NOT a subtype of simple tubular glands?", "أي مما يأتي ليس من أنواع الغدد الأنبوبية البسيطة؟", [("Simple tubular", "أنبوبية بسيطة"), ("Simple coiled tubular", "أنبوبية ملتفّة بسيطة"), ("Simple branched tubular", "أنبوبية متفرّعة بسيطة"), ("Compound tubuloacinar", "أنبوبية عنبية مركّبة")], "d"),
 Q("If the secretory cells form an expanded sac, the gland is:", "إذا كوّنت الخلايا الإفرازية كيسًا متّسعًا فالغدة:", [("Acinar (alveolar)", "عنبية (سنخية)"), ("Tubular", "أنبوبية"), ("Coiled", "ملتفّة"), ("Endocrine", "صمّاء")], "a"),
 Q("Compound glands consist of:", "تتكوّن الغدد المركّبة من:", [("One cell", "خلية واحدة"), ("Simple glands whose small ducts join into progressively larger ducts", "غدد بسيطة تتّحد قنواتها الصغيرة في قنوات أكبر فأكبر"), ("A single sac", "كيس واحد"), ("Only tubules", "أنابيب فقط")], "b"),
 Q("A compound gland having both secretory tubules and secretory acini is:", "الغدة المركّبة التي فيها أنابيب إفرازية وعنيبات إفرازية معًا:", [("Compound tubular", "أنبوبية مركّبة"), ("Compound acinar", "عنبية مركّبة"), ("Compound tubuloacinar", "أنبوبية عنبية مركّبة"), ("Simple branched acinar", "عنبية متفرّعة بسيطة")], "c"),
 TOP("Types of secretion", "أنواع الإفراز"),
 Q("Serous glands secrete:", "تفرز الغدد المصلية:", [("Thick mucus", "مخاطًا ثخينًا"), ("Oily sebum", "زهمًا زيتيًا"), ("Cell fragments", "شظايا خلوية"), ("A non-viscous watery fluid", "سائلًا مائيًا غير لزج")], "d"),
 Q("Which is a serous secretion?", "أي مما يأتي إفراز مصلي؟", [("Sweat, milk, tears or digestive juices", "العرق أو الحليب أو الدموع أو العصارات الهضمية"), ("Mucus", "المخاط"), ("Sebum", "الزهم"), ("Cerumen only", "الصملاخ فقط")], "a"),
 Q("Mucous glands secrete mucins which form mucus when mixed with:", "تفرز الغدد المخاطية ميوسينات تكوّن المخاط عند مزجها بـ:", [("Blood", "الدم"), ("Water", "الماء"), ("Fat", "الدهن"), ("Air", "الهواء")], "b"),
 Q("Mucous glands are found in the:", "توجد الغدد المخاطية في:", [("Skin", "الجلد"), ("Mammary gland", "الغدة الثديية"), ("Roof of the oral cavity and surface of the tongue", "سقف تجويف الفم وسطح اللسان"), ("Pancreas", "البنكرياس")], "c"),
 Q("Mixed (seromucous) glands, such as the salivary glands inferior to the oral cavity, contain:", "الغدد المختلطة (المصلية المخاطية) مثل الغدد اللعابية أسفل تجويف الفم تحتوي:", [("Serous cells only", "خلايا مصلية فقط"), ("Mucous cells only", "خلايا مخاطية فقط"), ("Goblet cells only", "خلايا كأسية فقط"), ("Both serous and mucous cells", "خلايا مصلية ومخاطية معًا")], "d"),
 TOP("Methods of secretion", "طرق الإفراز"),
 Q("Merocrine glands release secretion by:", "تطلق الغدد الميروكرينية الإفراز بـ:", [("Exocytosis with no loss of cellular material", "الإخراج الخلوي دون فقدان مادة خلوية"), ("Disintegration of the whole cell", "تفكّك الخلية كلها"), ("Pinching off the apical cytoplasm", "انقراص السايتوبلازم القمّي"), ("Diffusion through a duct wall", "الانتشار عبر جدار القناة")], "a"),
 Q("Which is a merocrine gland?", "أي مما يأتي غدة ميروكرينية؟", [("Sebaceous gland", "الغدة الدهنية"), ("Salivary gland", "الغدة اللعابية"), ("Mammary gland", "الغدة الثديية"), ("Ceruminous gland", "الغدة الصملاخية")], "b"),
 Q("In holocrine glands, the secretion is:", "في الغدد الهولوكرينية يكون الإفراز:", [("Packaged in vesicles", "معبّأ في حويصلات"), ("Only the apical portion", "الجزء القمّي فقط"), ("A mixture of cell fragments and product after the whole cell disintegrates", "خليطًا من شظايا الخلية والمنتج بعد تفكّك الخلية كلها"), ("A hormone", "هرمونًا")], "c"),
 Q("The example of holocrine glands is:", "مثال الغدد الهولوكرينية:", [("Lacrimal gland", "الغدة الدمعية"), ("Pancreas", "البنكرياس"), ("Gastric glands", "الغدد المعدية"), ("Sebaceous glands", "الغدد الدهنية")], "d"),
 Q("In holocrine glands, the ruptured dead cells are replaced by:", "في الغدد الهولوكرينية تُعوَّض الخلايا الميّتة بـ:", [("Epithelial cells undergoing mitosis", "خلايا ظهارية تنقسم خيطيًا"), ("Fibroblasts", "أرومات ليفية"), ("Blood cells", "خلايا الدم"), ("Nothing", "لا شيء")], "a"),
 Q("The mode of secretion of apocrine glands is:", "طريقة إفراز الغدد الأبوكرينية:", [("Exocytosis", "الإخراج الخلوي"), ("Decapitation of the apical portion", "قطع الجزء القمّي"), ("Whole cell disintegration", "تفكّك الخلية كلها"), ("Diffusion", "الانتشار")], "b"),
 Q("Which are apocrine glands?", "أي مما يأتي غدد أبوكرينية؟", [("Sebaceous glands", "الغدد الدهنية"), ("Gastric glands", "الغدد المعدية"), ("Mammary and ceruminous glands", "الغدد الثديية والصملاخية"), ("Lacrimal glands", "الغدد الدمعية")], "c"),
]

# ───────────────────────── Lab 4 — Connective Tissues
L4 = [
 TOP("General features and components", "الصفات العامة والمكوّنات"),
 Q("Connective tissue is described as:", "يوصف النسيج الضام بأنه:", [("The least abundant tissue", "أقل الأنسجة وفرة"), ("The most diverse, abundant and widely distributed tissue", "أكثر الأنسجة تنوّعًا ووفرة وانتشارًا"), ("Only found in bone", "موجود في العظم فقط"), ("Avascular lining tissue", "نسيج مبطّن لاوعائي")], "b"),
 Q("Connective tissue is called the 'glue' because it:", "يُسمّى النسيج الضام 'الغراء' لأنه:", [("Binds body structures together", "يربط تراكيب الجسم معًا"), ("Contracts", "ينقبض"), ("Conducts impulses", "يوصل السيالات"), ("Secretes hormones", "يفرز الهرمونات")], "a"),
 Q("Which is NOT listed as a connective tissue?", "أي مما يأتي ليس من النسيج الضام المذكور؟", [("Tendons and ligaments", "الأوتار والأربطة"), ("Body fat", "دهن الجسم"), ("Blood", "الدم"), ("Epidermis", "البشرة")], "d"),
 Q("Structurally, connective tissue is formed by:", "يتكوّن النسيج الضام تركيبيًا من:", [("Cells only", "خلايا فقط"), ("Fibers only", "ألياف فقط"), ("Cells, fibers and ground substance", "الخلايا والألياف والمادة الأساسية"), ("Cells and basement membrane", "الخلايا والغشاء القاعدي")], "c"),
 Q("The major constituent of connective tissue is:", "المكوّن الرئيسي للنسيج الضام:", [("Cells", "الخلايا"), ("The extracellular matrix", "المادة خارج الخلوية"), ("Nerves", "الأعصاب"), ("Blood vessels", "الأوعية الدموية")], "b"),
 Q("The extracellular matrix consists of:", "تتكوّن المادة خارج الخلوية من:", [("Protein fibers and ground substance", "ألياف بروتينية ومادة أساسية"), ("Cells and fibers", "خلايا وألياف"), ("Cells only", "خلايا فقط"), ("Water only", "ماء فقط")], "a"),
 Q("Cartilage contains:", "يحتوي الغضروف على:", [("Osteocytes", "خلايا عظمية"), ("Adipocytes", "خلايا دهنية"), ("Fibroblasts only", "أرومات ليفية فقط"), ("Chondrocytes", "خلايا غضروفية")], "d"),
 Q("Unlike epithelium, connective tissue cells are:", "على خلاف الظهارة، خلايا النسيج الضام:", [("Crowded closely together", "متراصّة"), ("Scattered, not in direct contact with each other", "متناثرة وغير متلامسة"), ("Arranged in layers", "مرتّبة في طبقات"), ("Without matrix", "بلا مادة بينية")], "b"),
 Q("Collagen fibers are:", "ألياف الكولاجين:", [("Flexible and resilient", "مرنة وقابلة للارتداد"), ("Interwoven framework", "إطار متشابك"), ("Strong and stretch resistant", "قوية ومقاومة للمطّ"), ("Absent in connective tissue", "غائبة في النسيج الضام")], "c"),
 Q("Elastic fibers are:", "الألياف المرنة:", [("Strong and stretch resistant", "قوية ومقاومة للمطّ"), ("Flexible and resilient", "مرنة وقابلة للارتداد"), ("An interwoven framework", "إطار متشابك"), ("Made of keratin", "مصنوعة من الكيراتين")], "b"),
 Q("Reticular fibers:", "الألياف الشبكية:", [("Form an interwoven framework", "تكوّن إطارًا متشابكًا"), ("Are stretch resistant", "مقاومة للمطّ"), ("Are flexible", "مرنة"), ("Store fat", "تخزن الدهن")], "a"),
 Q("The ground substance is:", "المادة الأساسية:", [("Living cells", "خلايا حيّة"), ("Protein fibers", "ألياف بروتينية"), ("Blood", "الدم"), ("Nonliving material produced by connective tissue cells", "مادة غير حيّة تنتجها خلايا النسيج الضام")], "d"),
 Q("The ground substance is semisolid in:", "تكون المادة الأساسية شبه صلبة في:", [("Blood", "الدم"), ("Bone", "العظم"), ("Cartilage", "الغضروف"), ("Fat", "الدهن")], "c"),
 TOP("Functions and development", "الوظائف والتكوّن"),
 Q("Fat packed around the kidneys is an example of:", "الدهن المحيط بالكليتين مثال على:", [("Physical protection", "الحماية الفيزيائية"), ("Transport", "النقل"), ("Immune protection", "الحماية المناعية"), ("Binding", "الربط")], "a"),
 Q("Tendons bind:", "تربط الأوتار:", [("Bone to bone", "عظمًا بعظم"), ("Muscle to bone", "عضلة بعظم"), ("Skin to muscle", "جلدًا بعضلة"), ("Organ to organ", "عضوًا بعضو")], "b"),
 Q("Ligaments bind:", "تربط الأربطة:", [("Muscle to bone", "عضلة بعظم"), ("Skin to bone", "جلدًا بعظم"), ("Nerve to muscle", "عصبًا بعضلة"), ("Bone to bone", "عظمًا بعظم")], "d"),
 Q("The major energy reserve in the body is:", "المخزون الرئيسي للطاقة في الجسم:", [("Bone", "العظم"), ("Cartilage", "الغضروف"), ("Fat", "الدهن"), ("Blood", "الدم")], "c"),
 Q("Bone is a large reservoir for:", "العظم مخزن كبير لـ:", [("Calcium and phosphorus", "الكالسيوم والفسفور"), ("Iron and copper", "الحديد والنحاس"), ("Glucose", "الغلوكوز"), ("Vitamins", "الفيتامينات")], "a"),
 Q("The transport function of connective tissue is done by:", "تؤدّي وظيفة النقل في النسيج الضام:", [("Cartilage", "الغضروف"), ("Blood", "الدم"), ("Ligaments", "الأربطة"), ("Fat", "الدهن")], "b"),
 Q("All connective tissues are formed from the germ layer:", "تتكوّن كل الأنسجة الضامة من الطبقة الجرثومية:", [("Ectoderm", "الأديم الظاهر"), ("Endoderm", "الأديم الباطن"), ("Neural crest", "العُرف العصبي"), ("Mesoderm", "الأديم المتوسط")], "d"),
 Q("The first type of connective tissue to emerge is:", "أول نوع من النسيج الضام يظهر:", [("Mucous connective tissue", "النسيج الضام المخاطي"), ("Bone", "العظم"), ("Mesenchyme", "الميزنكيم (اللُّحمة المتوسطة)"), ("Adipose", "الدهني")], "c"),
 Q("Mesenchyme cells are:", "خلايا الميزنكيم:", [("Star-shaped or spindle-shaped in a gel-like ground substance", "نجمية أو مغزلية في مادة أساسية هلامية"), ("Large and flat", "كبيرة ومسطّحة"), ("Filled with fat", "مملوءة بالدهن"), ("Phagocytic", "بلعمية")], "a"),
 Q("The source of all other connective tissues is:", "مصدر كل الأنسجة الضامة الأخرى:", [("Mucous connective tissue", "النسيج الضام المخاطي"), ("Mesenchyme", "الميزنكيم"), ("Fibroblasts", "الأرومات الليفية"), ("Blood", "الدم")], "b"),
 Q("Mucous connective tissue is located:", "يوجد النسيج الضام المخاطي:", [("In the skin of adults", "في جلد البالغين"), ("In bone", "في العظم"), ("Around the kidneys", "حول الكليتين"), ("Within the umbilical cord only", "في الحبل السري فقط")], "d"),
 Q("Connective tissues at birth are classified into all EXCEPT:", "تُصنَّف الأنسجة الضامة عند الولادة إلى كل ما يأتي ما عدا:", [("Connective tissue proper", "النسيج الضام الأصلي"), ("Supporting connective tissue", "النسيج الضام الداعم"), ("Glandular connective tissue", "النسيج الضام الغدّي"), ("Fluid connective tissue", "النسيج الضام السائل")], "c"),
 TOP("Cells of connective tissue proper", "خلايا النسيج الضام الأصلي"),
 Q("Resident cells of connective tissue proper include all EXCEPT:", "تشمل الخلايا المقيمة في النسيج الضام الأصلي كل ما يأتي ما عدا:", [("Fibroblasts", "الأرومات الليفية"), ("Adipocytes", "الخلايا الدهنية"), ("Fixed macrophages", "البلاعم الثابتة"), ("Mast cells", "الخلايا البدينة")], "d"),
 Q("The 4 types of wandering cells are:", "أنواع الخلايا الجوّالة الأربعة:", [("Mast cells, plasma cells, free macrophages and other leukocytes", "الخلايا البدينة والبلازمية والبلاعم الحرّة وكريات بيض أخرى"), ("Fibroblasts, adipocytes, macrophages, mesenchymal cells", "الأرومات الليفية والدهنية والبلاعم والميزنكيمية"), ("Chondrocytes and osteocytes", "الغضروفية والعظمية"), ("Red cells and platelets", "الكريات الحمر والصفيحات")], "a"),
 Q("The most abundant resident cells in connective tissue proper are:", "أكثر الخلايا المقيمة وفرة في النسيج الضام الأصلي:", [("Adipocytes", "الخلايا الدهنية"), ("Fibroblasts", "الأرومات الليفية"), ("Mast cells", "الخلايا البدينة"), ("Plasma cells", "الخلايا البلازمية")], "b"),
 Q("Fibroblasts produce:", "تنتج الأرومات الليفية:", [("Antibodies", "الأضداد"), ("Heparin", "الهيبارين"), ("Fibers and ground substance", "الألياف والمادة الأساسية"), ("Fat", "الدهن")], "c"),
 Q("A large cluster of adipocytes dominating an area forms:", "تجمّع كبير من الخلايا الدهنية يسيطر على منطقة يكوّن:", [("Cartilage", "الغضروف"), ("Bone", "العظم"), ("Mucous tissue", "النسيج المخاطي"), ("Adipose connective tissue", "النسيج الضام الدهني")], "d"),
 Q("Fixed macrophages are derived from:", "تُشتقّ البلاعم الثابتة من:", [("Monocytes", "الوحيدات"), ("Neutrophils", "العدلات"), ("Fibroblasts", "الأرومات الليفية"), ("B lymphocytes", "اللمفاويات B")], "a"),
 Q("When mesenchymal stem cells divide after injury:", "عندما تنقسم الخلايا الجذعية الميزنكيمية بعد الإصابة:", [("Both die", "تموت الاثنتان"), ("One replaces the stem cell and one differentiates into the needed cell", "تعوّض إحداهما الخلية الجذعية وتتمايز الأخرى إلى الخلية المطلوبة"), ("Both become fat cells", "تصبح الاثنتان خلايا دهنية"), ("They become plasma cells", "تصبح خلايا بلازمية")], "b"),
 Q("Mast cells secrete:", "تفرز الخلايا البدينة:", [("Antibodies", "الأضداد"), ("Collagen", "الكولاجين"), ("Heparin and histamine", "الهيبارين والهستامين"), ("Keratin", "الكيراتين")], "c"),
 Q("Histamine from mast cells:", "الهستامين من الخلايا البدينة:", [("Inhibits blood clotting", "يثبّط تخثّر الدم"), ("Produces fibers", "ينتج الألياف"), ("Stores fat", "يخزن الدهن"), ("Dilates blood vessels and increases blood flow", "يوسّع الأوعية ويزيد جريان الدم")], "d"),
 Q("Plasma cells develop from:", "تتطوّر الخلايا البلازمية من:", [("Activated B-lymphocytes", "اللمفاويات B المنشّطة"), ("Monocytes", "الوحيدات"), ("Fibroblasts", "الأرومات الليفية"), ("Neutrophils", "العدلات")], "a"),
 Q("Plasma cells synthesize:", "تصنّع الخلايا البلازمية:", [("Heparin", "الهيبارين"), ("Antibodies", "الأضداد"), ("Collagen", "الكولاجين"), ("Ground substance", "المادة الأساسية")], "b"),
 Q("Plasma cells are usually found in:", "توجد الخلايا البلازمية عادةً في:", [("Bone and cartilage", "العظم والغضروف"), ("Skin epidermis", "بشرة الجلد"), ("Intestinal walls, spleen and lymph nodes", "جدران الأمعاء والطحال والعقد اللمفية"), ("Umbilical cord", "الحبل السري")], "c"),
 Q("Free macrophages are:", "البلاعم الحرّة:", [("Fixed cells derived from fibroblasts", "خلايا ثابتة من الأرومات الليفية"), ("Fat cells", "خلايا دهنية"), ("Antibody-producing cells", "خلايا منتجة للأضداد"), ("Mobile phagocytes formed from monocytes", "خلايا بالعة متحرّكة من الوحيدات")], "d"),
 Q("The majority of other leukocytes in connective tissue are:", "معظم الكريات البيض الأخرى في النسيج الضام:", [("Neutrophils", "العدلات"), ("Eosinophils", "الحمضات"), ("Basophils", "القعدات"), ("Monocytes", "الوحيدات")], "a"),
]

save(2, "Classification of Epithelial Tissue", "تصنيف النسيج الظهاري", L2, 21)
save(3, "Glandular Epithelial Tissue", "النسيج الظهاري الغدّي", L3, 22)
save(4, "Connective Tissues", "الأنسجة الضامة", L4, 23)

```
