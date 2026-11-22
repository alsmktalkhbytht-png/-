import sys, json, os
from collections import Counter
WORK = "/home/claude/scratch/work"
sys.path.insert(0, WORK + "/bac"); from bal import balance
sys.path.insert(0, WORK); from bidi import ltr_all

# Diagnostic Microbiology — THEORY Lecture 6 (stage 4, د. عدنان): Cultivation and Isolation of Viable Pathogen.
# Source 2026-11-22: iOS scan of a student summary (prepared by «سراج حيدر الكلابي», Instagram med_analyst1) — 10 pages, highlighted,
# with ministerial («سؤال وزاري») MCQs on pp.3–8 and a tutorial/ministerial set on pp.9–10 (keys circled/highlighted).
# User rule (2026-11-22): theory banks = MCQ only, no explanations, no SA.
# Past questions kept with their original option order (fixed=), spelling typos fixed (E.colli, partem, piting, Comple, conatin, supressing).
# Duplicate "Antibiotics added to media for" asked once. p.7 highlight on «supporting the growth» is wrong — key = suppressing (as p.9).
# Handwritten "10%" near NaCl and the "Abdullah Khalid" signature are not asked.

def Q(en, ar, opts, fixed=None):
    d = dict(en=en, ar=ar, options=[list(o) for o in opts])
    if fixed: d["_fixed"] = fixed
    else: d["answer"] = "a"
    return d
def T(en, ar): return {"topic_en": en, "topic_ar": ar}
ALL = ("All of the above", "جميع ما سبق")
S = lambda x: f"__{x}__"

mcq = [
 T("Laboratory media", "الأوساط الزراعية"),
 Q("Culture media are required to:", "الأوساط الزراعية ضرورية لـ:",
   [("Isolate the bacteria from the clinical specimens", "عزل البكتيريا من العيّنات السريرية"), ("Sterilize the specimens", "تعقيم العيّنات"),
    ("Kill the causative agent", "قتل المسبِّب"), ("Replace the biochemical tests", "الاستغناء عن الفحوص الكيميائية الحيوية")]),
 Q("Needed as source of nutrients for the growth of the microbes:", "تُستعمل مصدرًا للمغذّيات لنمو الميكروبات:",
   [("reagent", "الكاشف"), ("media", "الأوساط"), ("bacteria", "البكتيريا"), ("alcohol", "الكحول")], fixed="b"),
 Q("The isolated organism is identified from blood culture by:", "يُشخَّص الكائن المعزول من زرع الدم بواسطة:",
   [("colony morphology", "شكل المستعمرة"), ("Gram staining", "صبغة غرام"), ("Biochemical reactions", "التفاعلات الكيميائية الحيوية"), ALL], fixed="d"),

 T("Constituents of culture media", "مكوّنات الأوساط الزراعية"),
 Q("The constituents of culture media are:", "مكوّنات الأوساط الزراعية هي:",
   [("Water", "الماء"), ("Electrolyte", "الإلكتروليت"), ("Peptone", "الببتون"), ALL], fixed="d"),
 Q("The water used for media preparation is:", "الماء المستعمل لتحضير الأوساط:",
   [("Distilled water or potable water with low mineral content", "ماء مقطّر أو ماء صالح للشرب قليل المعادن"), ("Sea water", "ماء البحر"),
    ("Water with high mineral content", "ماء غني بالمعادن"), ("Saline only", "محلول ملحي فقط")]),
 Q("An example of the electrolytes used in culture media is:", "من أمثلة الإلكتروليتات المستعملة في الأوساط الزراعية:",
   [("Sodium chloride", "كلوريد الصوديوم"), ("Glucose", "الكلوكوز"), ("Agar", "الأجار"), ("Peptone", "الببتون")]),
 Q("Peptone is:", "الببتون هو:",
   [("A complex mixture of partially digested proteins", "خليط معقّد من بروتينات مهضومة جزئيًّا"), ("A polysaccharide from seaweeds", "سكّر متعدّد من الطحالب البحرية"),
    ("A pure chemical substance", "مادة كيميائية نقية"), ("A pH indicator", "مؤشّر pH")]),
 Q("Peptone is usually obtained by digestion of protein material with proteolytic enzymes, such as:", "يُحصل على الببتون عادةً بهضم المواد البروتينية بإنزيمات محلّلة للبروتين مثل:",
   [("Pepsin", "الببسين"), ("Amylase", "الأميليز"), ("Lipase", "الليبيز"), ("Lactase", "اللاكتيز")]),
 Q("Sources of peptone include:", "من مصادر الببتون:",
   [("Lean meat, heart muscle, casein, fibrin or soya flour", "اللحم الخالي من الدهون، عضلة القلب، الكازين، الفيبرين أو دقيق الصويا"),
    ("Red algae", "الطحالب الحمراء"), ("Baker's yeast", "خميرة الخبّاز"), ("Sheep blood", "دم الخراف")]),
 Q("Accessory growth factors contained in peptone are:", "عوامل النمو الإضافية الموجودة في الببتون:",
   [("Nicotinic acid and riboflavin", "حمض النيكوتينيك والريبوفلافين"), ("Glucose and starch", "الكلوكوز والنشا"),
    ("Bile salts and crystal violet", "أملاح الصفراء والبنفسج البلوري"), ("Agar and gelatin", "الأجار والجيلاتين")]),
 Q("Agar is used in culture media for:", "يُستعمل الأجار في الأوساط الزراعية لـ:",
   [("Sterilization the culture media", "تعقيم الوسط الزراعي"), ("Solidifying the culture media", "تصليب الوسط الزراعي"),
    ("Neutralization the pH", "معادلة الـ pH"), ("Supporting the growth of bacteria", "دعم نمو البكتيريا")], fixed="b"),
 Q("One of the following is used for solidifying the culture media:", "واحد مما يأتي يُستعمل لتصليب الوسط الزراعي:",
   [("Peptone", "الببتون"), ("Electrolyte", "الإلكتروليت"), ("Carbohydrate", "الكربوهيدرات"), ("None of the above", "لا شيء مما سبق")], fixed="d"),
 Q("Agar ('agar-agar') is prepared from the cell wall of:", "يُحضَّر الأجار («أجار-أجار») من جدران خلايا:",
   [("Seaweeds (red algae of species " + S("Gelidium") + " and " + S("Gracilaria") + ")", "الطحالب البحرية (الطحالب الحمراء من نوعي Gelidium وGracilaria)"),
    ("Baker's yeast", "خميرة الخبّاز"), ("Beef", "لحم البقر"), ("Soya beans", "فول الصويا")]),
 Q("Agar powder:", "مسحوق الأجار:",
   [("Melts in water after boiling and jellifies after cooling", "يذوب في الماء بعد الغليان ويتجلّد بعد التبريد"), ("Melts at room temperature", "يذوب بدرجة حرارة الغرفة"),
    ("Never dissolves in water", "لا يذوب في الماء أبدًا"), ("Jellifies only after boiling", "يتجلّد بعد الغليان فقط")]),
 Q("Molten agar is poured into the Petri dishes when its temperature comes down to:", "يُصبّ الأجار المذاب في أطباق بتري عندما تنخفض حرارته إلى:",
   [("`45 ºC`", "`45 ºC`"), ("`100 ºC`", "`100 ºC`"), ("`121 ºC`", "`121 ºC`"), ("`4 ºC`", "`4 ºC`")]),
 Q("After pouring into Petri dishes, agar medium is allowed to set for:", "بعد الصبّ في أطباق بتري يُترك وسط الأجار ليتصلّب مدة:",
   [("20 minutes", "20 دقيقة"), ("2 minutes", "دقيقتين"), ("2 hours", "ساعتين"), ("24 hours", "24 ساعة")]),
 Q("The dissolved agar mixture is sterilized by:", "يُعقَّم خليط الأجار المذاب بواسطة:",
   [("Autoclave", "الأوتوكلاف"), ("Filtration", "الترشيح"), ("Alcohol", "الكحول"), ("Freezing", "التجميد")]),
 Q("Meat extract is usually made from:", "يُصنع مستخلص اللحم عادةً من:",
   [("Beef", "لحم البقر"), ("Fish", "السمك"), ("Chicken", "الدجاج"), ("Soya", "الصويا")]),
 Q("Malt extract agar consists of maltose (about 50%) and ………", "يتكوّن أجار مستخلص الشعير من المالتوز (حوالي 50%) و………",
   [("starch", "النشا"), ("Dextrin", "الدكسترين"), ("Glucose", "الكلوكوز"), ALL], fixed="d"),
 Q("Malt extract media contains different components like:", "يحتوي وسط مستخلص الشعير مكوّنات مختلفة مثل:",
   [("Blood", "الدم"), ("Inorganic salts", "الأملاح غير العضوية"), ("Growth factors", "عوامل النمو"), ("None of the above", "لا شيء مما سبق")], fixed="b"),
 Q("Yeast extract is prepared commercially from:", "يُحضَّر مستخلص الخميرة تجاريًّا من:",
   [("Washed cells of Baker's yeast", "خلايا مغسولة من خميرة الخبّاز"), ("Red algae", "الطحالب الحمراء"), ("Lean meat", "اللحم الخالي من الدهون"), ("Casein", "الكازين")]),
 Q("Blood and serum are important components of:", "الدم والمصل مكوّنان مهمّان في:",
   [("Enriched media, providing extra nutrition to fastidious bacteria", "الأوساط الغنية، إذ يوفّران تغذية إضافية للبكتيريا صعبة النمو"),
    ("Synthetic media", "الأوساط الاصطناعية"), ("Simple media", "الأوساط البسيطة"), ("Transport media only", "أوساط النقل فقط")]),
 Q("The percentage of sheep blood usually used in enriched media is:", "نسبة دم الخراف المستعملة عادةً في الأوساط الغنية:",
   [("5–10%", "5–10%"), ("1%", "1%"), ("20–30%", "20–30%"), ("50%", "50%")]),

 T("Types of culture media", "أنواع الأوساط الزراعية"),
 Q("Types of culture media based on consistency are:", "أنواع الأوساط الزراعية حسب القوام:",
   [("Liquid media (or broth)", "أوساط سائلة (أو مرق)"), ("Semisolid media", "أوساط شبه صلبة"), ("Solid media", "أوساط صلبة"), ALL], fixed="d"),
 Q("Media that prepared from pure chemical substances known as:", "الأوساط المحضَّرة من مواد كيميائية نقية تُعرف بـ:",
   [("Routine laboratory media", "الأوساط المختبرية الروتينية"), ("synthetic", "الاصطناعية"), ("defined media", "الأوساط المعرَّفة"), ("both B and C", "B وC معًا")], fixed="d"),
 Q("Defined (synthetic) media are either:", "الأوساط المعرَّفة (الاصطناعية) تكون إمّا:",
   [("Simple synthetic or complex synthetic media", "اصطناعية بسيطة أو اصطناعية معقّدة"), ("Liquid or solid only", "سائلة أو صلبة فقط"),
    ("Selective or differential", "انتقائية أو تفريقية"), ("Aerobic or anaerobic", "هوائية أو لاهوائية")]),
 Q("Routine laboratory media are prepared from:", "تُحضَّر الأوساط المختبرية الروتينية من:",
   [("Nutrients, such as aqueous extract of meat and peptone", "مغذّيات مثل مستخلص اللحم المائي والببتون"), ("Pure chemical substances", "مواد كيميائية نقية"),
    ("Antibiotics only", "مضادات حيوية فقط"), ("Distilled water only", "ماء مقطّر فقط")]),
 Q("MacConkey agar is used for growth only gram negative bacteria, which one of the following media:", "أجار ماكونكي يُستعمل لنمو البكتيريا سالبة غرام فقط، فهو أيّ من الأوساط الآتية:",
   [("Semisolid media", "وسط شبه صلب"), ("Simple media", "وسط بسيط"), ("Enriched media", "وسط غني"), ("Selective media", "وسط انتقائي")], fixed="d"),

 T("Simple and enriched media", "الأوساط البسيطة والغنية"),
 Q("An example of simple media is:", "مثال على الأوساط البسيطة:",
   [("Nutrient broth / nutrient agar", "مرق المغذّي / أجار المغذّي"), ("Blood agar", "أجار الدم"), ("Chocolate agar", "أجار الشوكولاتة"), ("MacConkey agar", "أجار ماكونكي")]),
 Q("Nutrient agar contains ‘peptone’ and:", "يحتوي أجار المغذّي على «الببتون» و:",
   [("‘Meat extract’", "«مستخلص اللحم»"), ("Whole blood", "دم كامل"), ("Bile salts", "أملاح الصفراء"), ("Antibiotics", "مضادات حيوية")]),
 Q("……… Media contain additional nutrients for the isolation of more fastidious bacteria like whole blood (blood agar) or agar containing lysed blood (Chocolate agar).",
   "……… أوساط تحتوي مغذّيات إضافية لعزل البكتيريا صعبة النمو، مثل الدم الكامل (أجار الدم) أو الأجار الحاوي على دم متحلّل (أجار الشوكولاتة).",
   [("Differential", "التفريقية"), ("Nutrient", "المغذّية"), ("Enriched", "الغنية"), ALL], fixed="c"),
 Q("Chocolate agar is agar containing:", "أجار الشوكولاتة هو أجار يحتوي على:",
   [("Lysed blood", "دم متحلّل"), ("Whole blood", "دم كامل"), ("Chocolate", "شوكولاتة"), ("Bile salts", "أملاح الصفراء")]),
 Q("Example of non-enriched media is:", "مثال على وسط غير غني:",
   [("Blood agar", "أجار الدم"), ("Chocolate agar", "أجار الشوكولاتة"), ("Mannitol salt agar", "أجار المانيتول الملحي"), ("A and B", "A وB")], fixed="c"),
 Q("Fastidious microorganisms:", "الكائنات الدقيقة صعبة النمو:",
   [(S("E. coli"), "الإشريكية القولونية"), (S("A. hydrophila"), "الإيروموناس المحبّة للماء"), ("Staphylococci", "العنقوديات"), (S("M. tuberculosis"), "المتفطّرة السلية")], fixed="d"),

 T("Selective media", "الأوساط الانتقائية"),
 Q("The ……… media are designed to facilitate growth of some bacteria while suppressing the growth of others.", "الأوساط ……… مصمَّمة لتسهيل نمو بعض البكتيريا مع تثبيط نمو غيرها.",
   [("Simple", "البسيطة"), ("Enriched", "الغنية"), ("Selective", "الانتقائية"), ("Complex", "المعقّدة")], fixed="c"),
 Q("Mannitol salt agar which contains increased in substance for the recovery of Staphylococci:", "أجار المانيتول الملحي يحتوي تركيزًا عاليًا من مادة لاستعادة العنقوديات:",
   [("Antibiotics", "المضادات الحيوية"), ("NaCl", "NaCl"), ("Thioglycollate", "الثايوكلايكوليت"), ALL], fixed="b"),
 Q("Mannitol salt agar contain increased concentration of NaCl used as selective media for:", "أجار المانيتول الملحي يحتوي تركيزًا عاليًا من NaCl ويُستعمل وسطًا انتقائيًّا لـ:",
   [(S("Pseudomonas"), "الزائفة"), ("staphylococcus", "العنقودية"), ("streptococci", "العقديات"), (S("E. coli"), "الإشريكية القولونية")], fixed="b"),
 Q("MacConkey agar is selective because it contains:", "أجار ماكونكي انتقائي لأنه يحتوي على:",
   [("Bile salt, allowing the growth of bile-tolerant bacteria only", "أملاح الصفراء، فيسمح بنمو البكتيريا المتحمّلة للصفراء فقط"), ("Increased NaCl", "تركيزًا عاليًا من NaCl"),
    ("Whole blood", "دمًا كاملًا"), ("Lysed blood", "دمًا متحلّلًا")]),
 Q("Antibiotics added to media for ………", "تُضاف المضادات الحيوية إلى الأوساط لـ………",
   [("supporting the growth", "دعم النمو"), ("as color indicator", "مؤشّر لوني"), ("suppressing the growth", "تثبيط النمو"), ("growth factor", "عامل نمو")], fixed="c"),
 Q("Some antibiotics are additive in media in order to make ………", "تُضاف بعض المضادات الحيوية إلى الأوساط لجعلها ………",
   [("Enrich media", "أوساطًا غنية"), ("Simple media", "أوساطًا بسيطة"), ("Selective media", "أوساطًا انتقائية"), ("Basal media", "أوساطًا أساسية")], fixed="c"),

 T("Indicator media", "الأوساط المؤشِّرة"),
 Q("Indicator media are designed to:", "الأوساط المؤشِّرة مصمَّمة لـ:",
   [("Aid the detection and recognition of particular pathogens", "المساعدة في كشف ممرضات معيّنة والتعرّف عليها"), ("Kill all pathogens", "قتل جميع الممرضات"),
    ("Transport specimens", "نقل العيّنات"), ("Solidify the media", "تصليب الأوساط")]),
 Q("Indicator media are often based on:", "تعتمد الأوساط المؤشِّرة غالبًا على:",
   [("Sugar fermentation reactions producing acid and a color change of a pH indicator", "تفاعلات تخمير السكريات المنتجة للحمض وتغيّر لون مؤشّر الـ pH"),
    ("Hemolysis only", "التحلّل الدموي فقط"), ("Antibiotic resistance", "مقاومة المضادات الحيوية"), ("Gram staining", "صبغة غرام")]),
 Q("MacConkey agar contains lactose and a pH indicator (neutral red); used for detection of ……", "أجار ماكونكي يحتوي اللاكتوز ومؤشّر pH (الأحمر المتعادل)؛ ويُستعمل لكشف ……",
   [("Salts tolerant bacteria", "البكتيريا المتحمّلة للأملاح"), ("Lactose-fermenting bacteria", "البكتيريا المخمِّرة للاكتوز"),
    ("Lactose-fermenting yeasts", "الخمائر المخمِّرة للاكتوز"), ALL], fixed="b"),
 Q("The pH indicator in MacConkey agar is:", "مؤشّر الـ pH في أجار ماكونكي هو:",
   [("Neutral red", "الأحمر المتعادل"), ("Phenol red", "أحمر الفينول"), ("Crystal violet", "البنفسج البلوري"), ("Methylene blue", "أزرق المثيلين")]),
 Q("On MacConkey agar, lactose-fermenting bacteria (like " + S("Escherichia coli") + "):", "على أجار ماكونكي، البكتيريا المخمِّرة للاكتوز (مثل الإشريكية القولونية):",
   [("Produce acid and form pink colonies", "تنتج حمضًا وتكوّن مستعمرات وردية"), ("Form pale yellow colonies", "تكوّن مستعمرات صفراء باهتة"),
    ("Do not grow", "لا تنمو"), ("Form black colonies", "تكوّن مستعمرات سوداء")]),
 Q("On MacConkey agar, non-lactose fermenting bacteria (like " + S("Salmonella") + " spp.):", "على أجار ماكونكي، البكتيريا غير المخمِّرة للاكتوز (مثل السالمونيلا):",
   [("Do not produce acid and form pale yellow colonies", "لا تنتج حمضًا وتكوّن مستعمرات صفراء باهتة"), ("Produce acid and form pink colonies", "تنتج حمضًا وتكوّن مستعمرات وردية"),
    ("Form green colonies", "تكوّن مستعمرات خضراء"), ("Lyse the blood", "تحلّل الدم")]),
 Q("Which of the following media can differentiate between lactose and non-lactose fermenting gram-negative bacteria?", "أيّ الأوساط الآتية يفرّق بين البكتيريا سالبة غرام المخمِّرة وغير المخمِّرة للاكتوز؟",
   [("Chocolate agar", "أجار الشوكولاتة"), ("MacConkey agar", "أجار ماكونكي"), ("Modified Thayer-Martin agar", "أجار ثاير-مارتن المعدَّل"), ("Blood agar", "أجار الدم")], fixed="b"),
 Q("Which of the following organisms is lactose fermenting ……", "أيّ الكائنات الآتية مخمِّر للاكتوز ……",
   [(S("Klebsiella"), "الكلبسيلة"), (S("Salmonella"), "السالمونيلا"), (S("Shigella"), "الشيغيلا"), ("Both B and C", "B وC معًا")], fixed="a"),
 Q("Substances added to indicator media to suppress the growth of most Gram-positive microorganisms include:", "من المواد المضافة للأوساط المؤشِّرة لتثبيط نمو معظم موجبات غرام:",
   [("Bile salts and crystal violet", "أملاح الصفراء والبنفسج البلوري"), ("Peptone and meat extract", "الببتون ومستخلص اللحم"),
    ("Blood and serum", "الدم والمصل"), ("Glucose and starch", "الكلوكوز والنشا")]),
 Q("MacConkey agar is therefore:", "لذلك يُعدّ أجار ماكونكي:",
   [("Both a selective medium and an indicator medium", "وسطًا انتقائيًّا ومؤشِّرًا معًا"), ("An enriched medium only", "وسطًا غنيًّا فقط"),
    ("A simple medium", "وسطًا بسيطًا"), ("A synthetic medium", "وسطًا اصطناعيًّا")]),
 Q("Changes in agar media resulting from bacterial growth indicate as:", "التغيّرات في أوساط الأجار الناتجة عن نمو البكتيريا تظهر على شكل:",
   [("hemolytic pattern on blood agar", "نمط التحلّل الدموي على أجار الدم"), ("changes in color of pH indicators", "تغيّر لون مؤشّرات الـ pH"),
    ("pitting of the agar surface", "تنقّر سطح الأجار"), ("All of them", "جميعها")], fixed="d"),
 Q("In gram positive, cells retain the ……… stain and remain purple to dark blue.", "في موجبات غرام تحتفظ الخلايا بصبغة ……… وتبقى بنفسجية إلى زرقاء داكنة.",
   [("Crystal violet", "البنفسج البلوري"), ("Decolorizing", "مزيل اللون"), ("Safranin", "السفرانين"), ("Iodine solution", "محلول اليود")], fixed="a"),
]

mcq = balance(mcq, 7606)
for q in mcq:
    if "_fixed" in q: q["answer"] = q.pop("_fixed")

meta = {"subject_en": "Diagnostic Microbiology", "subject_ar": "الأحياء المجهرية التشخيصية", "short_ar": "بكتريا",
        "instructor": "د. عدنان", "unit_en": "Lecture 6", "unit_ar": "المحاضرة 6", "unit_label": "LEC", "unit_no": "6",
        "title_en": "Cultivation and Isolation of Viable Pathogen", "title_ar": "زراعة مسبّبات الأمراض الحيّة وعزلها",
        "department": "قسم التحليلات", "kind": "Theory — نظري", "questions_kind": "MCQ — اختيار من متعدد",
        "stage": "The fourth stage — الرابعة",
        "file_name": "BIOS - بكتريا نظري المحاضرة السادسة - أسئلة MCQ"}
Qs = {"title_en": "Culture Media (Lecture 6) — MCQ",
      "title_ar": "الأوساط الزراعية (المحاضرة 6) — أسئلة اختيار",
      "answers_inline": True, "compact": True, "mcq_per_page": 5,
      "mcq_en": "Comprehensive MCQs — Lecture 6", "mcq_ar": "أسئلة اختيار شاملة — المحاضرة 6",
      "intro_en": ["Q. Select the most correct answer from the followings",
                   "These questions cover the whole lecture, including the ministerial and tutorial questions; the answer sits under each question."],
      "intro_ar": ["س. اختر الإجابة الأصح مما يأتي",
                   "هذه الأسئلة تغطّي المحاضرة كاملة ومعها الأسئلة الوزارية والتدريبية؛ والحل تحت كل سؤال."],
      "mcq": ltr_all(mcq), "tf": [], "traps": [], "important": []}

d = "/home/user/-/bacteriology-lec6-mcq"
os.makedirs(d, exist_ok=True)
json.dump({"meta": meta, "questions": Qs}, open(d + "/lecture.json", "w"), ensure_ascii=False, indent=1)
qs = [m for m in mcq if "answer" in m]
print("MCQ:", len(qs), "| dist:", dict(Counter(m["answer"] for m in qs)))
for i, q in enumerate(qs, 1):
    print(i, q["answer"], q["options"]["abcd".index(q["answer"])][0][:60])
