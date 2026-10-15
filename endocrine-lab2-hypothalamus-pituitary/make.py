import json, os
from collections import Counter

def C(en, ar, **k):  return dict(t="card", en=en, ar=ar, **k)
def SEC(en, ar):     return dict(t="section", en=en, ar=ar)
def H2(en, ar):      return dict(t="h2", en=en, ar=ar)
def N(en, ar, label=None):
    b = dict(t="note", en=en, ar=ar)
    if label: b["label"] = label
    return b
def T(head, rows, **k): return dict(t="table", head=head, rows=rows, **k)
def F(src, en, ar, **k): return dict(t="figure", src="assets/" + src, en=en, ar=ar, **k)
def Q(en, ar, opts, ans, **k):
    return dict(en=en, ar=ar, options=[list(o) for o in opts], answer=ans, **k)
def TF(en, ar, a): return dict(en=en, ar=ar, answer=a)
def TR(en, ar, ae, aa): return dict(en=en, ar=ar, answer_en=ae, answer_ar=aa)
IM = TR

TBL = dict(ar_cols=[2], key_cols=[0], widths=["52mm", "", "62mm"])

blocks = [
 SEC("Introduction", "مقدمة"),
 C(["The hypothalamus and pituitary gland work together to regulate several endocrine functions, including growth, metabolism, reproduction, stress responses, and water balance.",
    "The hypothalamus controls pituitary hormone secretion through releasing and inhibiting hormones, neural connections, and feedback mechanisms.",
    "Pituitary disorders may result in either excessive or deficient hormone secretion."],
   ["يعمل **الوطاء** (تحت المهاد) و**الغدة النخامية** معًا لتنظيم عدّة وظائف صمّاوية، منها النمو والأيض والتكاثر والاستجابة للإجهاد وتوازن الماء.",
    "يتحكّم الوطاء في إفراز هرمونات النخامية عن طريق **الهرمونات المحرِّرة والمثبِّطة**، والاتصالات العصبية، وآليات التغذية الراجعة.",
    "قد تؤدّي اضطرابات الغدة النخامية إلى **زيادة** إفراز الهرمونات أو **نقصه**."]),

 SEC("Hypothalamic–Pituitary Relationship", "العلاقة بين الوطاء والغدة النخامية"),
 C("The pituitary gland consists of two functionally distinct parts:",
   "تتكوّن الغدة النخامية من **جزأين مختلفين وظيفيًا**:"),
 F("hormones.jpg", "Hormones", "الهرمونات: الوطاء والغدة النخامية وأعضاؤها المستهدفة", h="118mm", fit="contain"),
 N("The figure labels adrenocorticotropic hormone as (ACH); the correct abbreviation is ACTH. Vasopressin (ADH) in the figure is the same hormone written ADH/AVP in the tables.",
   "في الشكل كُتب اختصار الهرمون الموجّه لقشرة الكظر `(ACH)` والصحيح `ACTH`. و**الفازوبريسين** `(ADH)` في الشكل هو نفسه الهرمون المكتوب `ADH/AVP` في الجداول.",
   ["BIOS note", "ملاحظة بايوس"]),

 H2("A-Anterior Pituitary (Adenohypophysis)", "أ- النخامية الأمامية (النخامية الغدّية)"),
 C("The hypothalamus regulates the anterior pituitary through releasing and inhibiting hormones transported by the hypothalamic–pituitary portal system.",
   "ينظّم الوطاء النخامية الأمامية عن طريق هرمونات محرِّرة ومثبِّطة تُنقل عبر **الجهاز البابي الوطائي النخامي**."),
 C("**Major anterior pituitary hormones:**", "**أهم هرمونات النخامية الأمامية:**", keep=True),
 T(["Hormone", "Main Function", "الهرمون — الوظيفة الرئيسة"],
   [["Growth Hormone (GH)", "Stimulates body growth and regulates metabolism",
     "**هرمون النمو** `(GH)` — يحفّز نمو الجسم وينظّم الأيض"],
    ["Prolactin (PRL)", "Stimulates milk production",
     "**البرولاكتين** `(PRL)` — يحفّز إنتاج الحليب"],
    ["Adrenocorticotropic-Hormone (ACTH)", "Stimulates cortisol secretion from the adrenal cortex",
     "**الهرمون الموجّه لقشرة الكظر** `(ACTH)` — يحفّز إفراز الكورتيزول من قشرة الكظر"],
    ["Thyroid-Stimulating-Hormone (TSH)", "Stimulates thyroid hormone production",
     "**الهرمون المحفّز للدرقية** `(TSH)` — يحفّز إنتاج هرمونات الغدة الدرقية"],
    ["Follicle-Stimulating-Hormone (FSH)", "Regulates follicular development and spermatogenesis",
     "**الهرمون المحفّز للجريب** `(FSH)` — ينظّم نموّ الجريبات وتكوين النطف"],
    ["Luteinizing Hormone (LH)", "Regulates ovulation and sex hormone production",
     "**الهرمون اللوتيني** `(LH)` — ينظّم الإباضة وإنتاج الهرمونات الجنسية"]], **TBL),

 H2("B. Posterior Pituitary (Neurohypophysis)", "ب. النخامية الخلفية (النخامية العصبية)"),
 C("The posterior pituitary stores and releases hormones synthesized in the hypothalamus.",
   "**تخزّن** النخامية الخلفية **وتحرّر** هرمونات **تُصنَّع في الوطاء**.", keep=True),
 T(["Hormone", "Main Function", "الهرمون — الوظيفة الرئيسة"],
   [["Antidiuretic-Hormone (ADH/AVP)", "Increases water reabsorption in the kidney collecting ducts",
     "**الهرمون المضاد لإدرار البول** `(ADH/AVP)` — يزيد إعادة امتصاص الماء في القنوات الجامعة للكلية"],
    ["Oxytocin", "Promotes milk ejection and uterine contractions",
     "**الأوكسيتوسين** — يعزّز قذف الحليب وتقلّصات الرحم"]], **TBL),

 SEC("Control of Anterior Pituitary Hormones", "التحكّم في هرمونات النخامية الأمامية"),
 C("The hypothalamus regulates anterior pituitary hormone secretion through specific factors:",
   "ينظّم الوطاء إفراز هرمونات النخامية الأمامية عن طريق عوامل محدّدة:", keep=True),
 T(["Hypothalamic Factor", "Effect", "العامل الوطائي — التأثير"],
   [["Growth-Hormone-Releasing-Hormone (GHRH)", "Stimulates GH secretion",
     "**الهرمون المحرِّر لهرمون النمو** `(GHRH)` — يحفّز إفراز `GH`"],
    ["Somatostatin", "Inhibits GH secretion",
     "**السوماتوستاتين** — يثبّط إفراز `GH`"],
    ["Dopamine", "Inhibits prolactin secretion",
     "**الدوبامين** — يثبّط إفراز البرولاكتين"],
    ["Corticotropin-Releasing Hormone (CRH)", "Stimulates ACTH secretion",
     "**الهرمون المحرِّر لموجّهة القشرة** `(CRH)` — يحفّز إفراز `ACTH`"],
    ["Thyrotropin-Releasing Hormone (TRH)", "Stimulates TSH secretion",
     "**الهرمون المحرِّر لموجّهة الدرقية** `(TRH)` — يحفّز إفراز `TSH`"],
    ["Gonadotropin-Releasing Hormone (GnRH)", "Stimulates FSH and LH secretion",
     "**الهرمون المحرِّر لموجّهة الغدد التناسلية** `(GnRH)` — يحفّز إفراز `FSH` و`LH`"]], **TBL),

 SEC("Negative Feedback Mechanism", "آلية التغذية الراجعة السلبية"),
 C("Hormones released by target endocrine glands inhibit further secretion from the hypothalamus and pituitary gland.",
   "الهرمونات التي تحرّرها **الغدد الصمّاء المستهدفة** **تثبّط** استمرار الإفراز من الوطاء والغدة النخامية."),
 N("Increased circulating thyroid hormones (T3 and T4) suppress TRH and TSH secretion.",
   "ارتفاع هرمونات الدرقية الجائلة في الدم (`T3` و`T4`) **يكبح** إفراز `TRH` و`TSH`.",
   ["Example", "مثال"]),
 dict(t="flow", en="Thyroid axis (drawn for the handout from the lecture text)",
      ar="محور الغدة الدرقية (رُسم للملزمة من نص المحاضرة)",
      steps=[{"en": "Hypothalamus → TRH", "ar": "الوطاء ← `TRH`"},
             {"en": "Anterior pituitary → TSH", "ar": "النخامية الأمامية ← `TSH`"},
             {"en": "Thyroid → T3 & T4", "ar": "الدرقية ← `T3` و`T4`"}],
      tail_en="↑ T3 & T4 → suppress TRH and TSH (negative feedback)",
      tail_ar="ارتفاع `T3` و`T4` يكبح `TRH` و`TSH` (تغذية راجعة سلبية)"),
]

H = ("Growth Hormone (GH)", "هرمون النمو"); P = ("Prolactin (PRL)", "البرولاكتين")
A = ("ACTH", "ACTH"); TS = ("TSH", "TSH"); FS = ("FSH", "FSH"); L = ("LH", "LH")
O = ("Oxytocin", "الأوكسيتوسين"); AD = ("ADH", "ADH")

mcq = [
 {"topic_en": "Introduction & relationship", "topic_ar": "المقدمة والعلاقة بين الوطاء والنخامية"},
 Q("The hypothalamus and pituitary gland regulate all of the following EXCEPT:",
   "ينظّم الوطاء والغدة النخامية كل ما يلي عدا:",
   [("Growth", "النمو"), ("Water balance", "توازن الماء"), ("Digestion of food", "هضم الطعام"), ("Stress responses", "الاستجابة للإجهاد")], "c"),
 Q("The hypothalamus controls pituitary hormone secretion through:",
   "يتحكّم الوطاء في إفراز هرمونات النخامية عن طريق:",
   [("Releasing and inhibiting hormones only", "الهرمونات المحرِّرة والمثبِّطة فقط"), ("Neural connections only", "الاتصالات العصبية فقط"),
    ("Feedback mechanisms only", "آليات التغذية الراجعة فقط"), ("All of the above", "كل ما سبق")], "d"),
 Q("Pituitary disorders may result in:", "قد تؤدّي اضطرابات الغدة النخامية إلى:",
   [("Either excessive or deficient hormone secretion", "زيادة إفراز الهرمونات أو نقصه"), ("Excessive secretion only", "زيادة الإفراز فقط"),
    ("Deficient secretion only", "نقص الإفراز فقط"), ("No change in secretion", "لا تغيّر في الإفراز")], "a"),
 Q("The anterior pituitary is also called:", "تُسمّى النخامية الأمامية أيضًا:",
   [("Neurohypophysis", "النخامية العصبية"), ("Adenohypophysis", "النخامية الغدّية"), ("Pineal gland", "الغدة الصنوبرية"), ("Hypothalamus", "الوطاء")], "b"),
 Q("The posterior pituitary is also called:", "تُسمّى النخامية الخلفية أيضًا:",
   [("Adenohypophysis", "النخامية الغدّية"), ("Adrenal medulla", "لبّ الكظر"), ("Neurohypophysis", "النخامية العصبية"), ("Thyroid gland", "الغدة الدرقية")], "c"),
 Q("Hypothalamic releasing and inhibiting hormones reach the anterior pituitary through the:",
   "تصل الهرمونات الوطائية المحرِّرة والمثبِّطة إلى النخامية الأمامية عبر:",
   [("Lymphatic vessels", "الأوعية اللمفاوية"), ("Cerebrospinal fluid", "السائل الدماغي الشوكي"),
    ("Kidney collecting ducts", "القنوات الجامعة للكلية"), ("Hypothalamic–pituitary portal system", "الجهاز البابي الوطائي النخامي")], "d"),

 {"topic_en": "Anterior pituitary hormones", "topic_ar": "هرمونات النخامية الأمامية"},
 Q("The hormone that stimulates body growth and regulates metabolism is:", "الهرمون الذي يحفّز نمو الجسم وينظّم الأيض هو:",
   [H, P, ("TSH", "TSH"), ("Oxytocin", "الأوكسيتوسين")], "a"),
 Q("Prolactin (PRL) stimulates:", "يحفّز البرولاكتين `(PRL)`:",
   [("Milk ejection", "قذف الحليب"), ("Milk production", "إنتاج الحليب"), ("Uterine contractions", "تقلّصات الرحم"), ("Ovulation", "الإباضة")], "b"),
 Q("Cortisol secretion from the adrenal cortex is stimulated by:", "يُحفَّز إفراز الكورتيزول من قشرة الكظر بواسطة:",
   [TS, L, A, AD], "c"),
 Q("Follicular development and spermatogenesis are regulated by:", "يُنظَّم نموّ الجريبات وتكوين النطف بواسطة:",
   [L, P, H, FS], "d"),
 Q("Ovulation and sex hormone production are regulated by:", "تُنظَّم الإباضة وإنتاج الهرمونات الجنسية بواسطة:",
   [L, FS, TS, A], "a"),
 Q("Which of the following is NOT an anterior pituitary hormone?", "أيّ مما يلي ليس من هرمونات النخامية الأمامية؟",
   [TS, O, FS, H], "b"),

 {"topic_en": "Posterior pituitary hormones", "topic_ar": "هرمونات النخامية الخلفية"},
 Q("The posterior pituitary:", "النخامية الخلفية:",
   [("Synthesizes ADH and oxytocin", "تصنّع `ADH` والأوكسيتوسين"), ("Secretes GH and PRL", "تفرز `GH` و`PRL`"),
    ("Stores and releases hormones synthesized in the hypothalamus", "تخزّن وتحرّر هرمونات مصنّعة في الوطاء"),
    ("Is controlled by the portal system", "يتحكّم بها الجهاز البابي")], "c"),
 Q("ADH increases water reabsorption in the:", "يزيد `ADH` إعادة امتصاص الماء في:",
   [("Proximal tubule", "النُبيب القريب"), ("Urinary bladder", "المثانة"), ("Glomerulus", "الكُبيبة"), ("Kidney collecting ducts", "القنوات الجامعة للكلية")], "d"),
 Q("Milk ejection and uterine contractions are promoted by:", "يعزّز قذف الحليب وتقلّصات الرحم:",
   [O, P, AD, L], "a"),
 Q("Antidiuretic hormone is also written as:", "يُكتب الهرمون المضاد لإدرار البول أيضًا:",
   [("ACTH", "ACTH"), ("AVP", "AVP"), ("GHRH", "GHRH"), ("CRH", "CRH")], "b"),

 {"topic_en": "Control of anterior pituitary hormones", "topic_ar": "التحكّم في هرمونات النخامية الأمامية"},
 Q("GH secretion is inhibited by:", "يُثبَّط إفراز `GH` بواسطة:",
   [("GHRH", "GHRH"), ("Dopamine", "الدوبامين"), ("Somatostatin", "السوماتوستاتين"), ("TRH", "TRH")], "c"),
 Q("Prolactin secretion is inhibited by:", "يُثبَّط إفراز البرولاكتين بواسطة:",
   [("Somatostatin", "السوماتوستاتين"), ("CRH", "CRH"), ("GnRH", "GnRH"), ("Dopamine", "الدوبامين")], "d"),
 Q("Corticotropin-releasing hormone (CRH) stimulates the secretion of:", "يحفّز الهرمون المحرِّر لموجّهة القشرة `(CRH)` إفراز:",
   [A, TS, H, P], "a"),
 Q("Thyrotropin-releasing hormone (TRH) stimulates the secretion of:", "يحفّز الهرمون المحرِّر لموجّهة الدرقية `(TRH)` إفراز:",
   [A, TS, FS, ("T3 and T4 directly", "T3 و T4 مباشرة")], "b"),
 Q("GnRH stimulates the secretion of:", "يحفّز `GnRH` إفراز:",
   [("GH", "GH"), ("ACTH", "ACTH"), ("FSH and LH", "FSH و LH"), ("Prolactin", "البرولاكتين")], "c"),
 Q("The hypothalamic factor that stimulates GH secretion is:", "العامل الوطائي الذي يحفّز إفراز `GH` هو:",
   [("Somatostatin", "السوماتوستاتين"), ("Dopamine", "الدوبامين"), ("CRH", "CRH"), ("GHRH", "GHRH")], "d"),

 {"topic_en": "Negative feedback", "topic_ar": "التغذية الراجعة السلبية"},
 Q("In negative feedback, hormones released by target endocrine glands:", "في التغذية الراجعة السلبية، الهرمونات التي تحرّرها الغدد المستهدفة:",
   [("Inhibit further secretion from the hypothalamus and pituitary", "تثبّط استمرار الإفراز من الوطاء والنخامية"),
    ("Stimulate further secretion from the hypothalamus", "تحفّز استمرار إفراز الوطاء"),
    ("Have no effect on the pituitary", "لا تأثير لها في النخامية"), ("Are stored in the posterior pituitary", "تُخزَّن في النخامية الخلفية")], "a"),
 Q("Increased circulating T3 and T4 suppress:", "ارتفاع `T3` و`T4` في الدم يكبح:",
   [("GHRH and GH", "GHRH و GH"), ("TRH and TSH", "TRH و TSH"), ("CRH and ACTH", "CRH و ACTH"), ("GnRH and LH", "GnRH و LH")], "b"),

 {"topic_en": "Picture questions", "topic_ar": "أسئلة الصور"},
 Q("The gland shown secretes cortisol when stimulated by which pituitary hormone?", "تفرز الغدة الظاهرة في الصورة الكورتيزول بتحفيز من أيّ هرمون نخامي؟",
   [TS, A, L, AD], "b", img="assets/q-adrenal.jpg", img_h="32mm"),
 Q("Production of the hormones shown is stimulated by:", "يُحفَّز إنتاج الهرمونات الظاهرة في الصورة بواسطة:",
   [A, FS, TS, P], "c", img="assets/q-thyroid.jpg", img_h="32mm"),
 Q("The anterior pituitary hormone that stimulates milk production in the organ shown is:", "هرمون النخامية الأمامية الذي يحفّز إنتاج الحليب في العضو الظاهر هو:",
   [O, L, AD, P], "d", img="assets/q-breast.jpg", img_h="32mm"),
 Q("The posterior pituitary hormone that promotes contractions of the organ shown (uterus) is:", "هرمون النخامية الخلفية الذي يعزّز تقلّصات العضو الظاهر (الرحم) هو:",
   [O, P, FS, H], "a", img="assets/q-uterus.jpg", img_h="32mm"),
 Q("The hormone that increases water reabsorption in the collecting ducts of the organ shown is:", "الهرمون الذي يزيد إعادة امتصاص الماء في القنوات الجامعة للعضو الظاهر هو:",
   [A, TS, AD, O], "c", img="assets/q-kidneys.jpg", img_h="32mm"),
]

tf = [
 TF("The hypothalamus and pituitary gland regulate water balance.", "ينظّم الوطاء والغدة النخامية توازن الماء.", "T"),
 TF("The pituitary gland consists of three functionally distinct parts.", "تتكوّن الغدة النخامية من ثلاثة أجزاء مختلفة وظيفيًا.", "F"),
 TF("The posterior pituitary synthesizes ADH and oxytocin.", "تصنّع النخامية الخلفية `ADH` والأوكسيتوسين.", "F"),
 TF("The anterior pituitary is regulated by hormones transported by the hypothalamic–pituitary portal system.", "تُنظَّم النخامية الأمامية بهرمونات ينقلها الجهاز البابي الوطائي النخامي.", "T"),
 TF("Prolactin promotes milk ejection.", "يعزّز البرولاكتين قذف الحليب.", "F"),
 TF("ACTH stimulates cortisol secretion from the adrenal cortex.", "يحفّز `ACTH` إفراز الكورتيزول من قشرة الكظر.", "T"),
 TF("FSH regulates ovulation and sex hormone production.", "ينظّم `FSH` الإباضة وإنتاج الهرمونات الجنسية.", "F"),
 TF("Somatostatin stimulates GH secretion.", "يحفّز السوماتوستاتين إفراز `GH`.", "F"),
 TF("Dopamine inhibits prolactin secretion.", "يثبّط الدوبامين إفراز البرولاكتين.", "T"),
 TF("GnRH stimulates both FSH and LH secretion.", "يحفّز `GnRH` إفراز `FSH` و`LH` كليهما.", "T"),
 TF("In negative feedback, target-gland hormones stimulate further secretion from the hypothalamus.", "في التغذية الراجعة السلبية تحفّز هرمونات الغدد المستهدفة استمرار إفراز الوطاء.", "F"),
 TF("Increased circulating T3 and T4 suppress TRH and TSH secretion.", "ارتفاع `T3` و`T4` الجائلة يكبح إفراز `TRH` و`TSH`.", "T"),
]

traps = [
 TR("Milk production vs milk ejection", "إنتاج الحليب مقابل قذف الحليب",
    "Prolactin (anterior pituitary) stimulates milk production; oxytocin (posterior pituitary) promotes milk ejection.",
    "البرولاكتين (النخامية الأمامية) يحفّز **إنتاج** الحليب، والأوكسيتوسين (النخامية الخلفية) يعزّز **قذفه**."),
 TR("Does the posterior pituitary make its own hormones?", "هل تصنّع النخامية الخلفية هرموناتها؟",
    "No — it stores and releases hormones synthesized in the hypothalamus (ADH and oxytocin).",
    "لا، هي **تخزّن وتحرّر** هرمونات **مصنّعة في الوطاء** (`ADH` والأوكسيتوسين)."),
 TR("FSH vs LH", "`FSH` مقابل `LH`",
    "FSH: follicular development and spermatogenesis. LH: ovulation and sex hormone production.",
    "ينظّم `FSH` نموّ الجريبات وتكوين النطف، أمّا `LH` فينظّم الإباضة وإنتاج الهرمونات الجنسية."),
 TR("GHRH vs somatostatin", "`GHRH` مقابل السوماتوستاتين",
    "Both act on GH: GHRH stimulates GH secretion, somatostatin inhibits it.",
    "كلاهما يؤثّر في `GH`، إذ **يحفّز** `GHRH` إفرازه، و**يثبّطه** السوماتوستاتين."),
 TR("Which factor inhibits prolactin?", "أيّ عامل يثبّط البرولاكتين؟",
    "Dopamine — not somatostatin (somatostatin inhibits GH).",
    "**الدوبامين**، وليس السوماتوستاتين (فالسوماتوستاتين يثبّط `GH`)."),
 TR("ADH, AVP and vasopressin", "`ADH` و`AVP` والفازوبريسين",
    "They are the same posterior pituitary hormone; it acts on the kidney collecting ducts.",
    "كلها **هرمون واحد** من النخامية الخلفية، يعمل على القنوات الجامعة في الكلية."),
]

important = [
 IM("How does the hypothalamus control pituitary hormone secretion?", "كيف يتحكّم الوطاء في إفراز هرمونات النخامية؟",
    "Through releasing and inhibiting hormones, neural connections, and feedback mechanisms.",
    "عن طريق الهرمونات المحرِّرة والمثبِّطة، والاتصالات العصبية، وآليات التغذية الراجعة."),
 IM("Compare the anterior and posterior pituitary.", "قارن بين النخامية الأمامية والخلفية.",
    "Anterior (adenohypophysis): regulated by hypothalamic releasing/inhibiting hormones carried by the hypothalamic–pituitary portal system; secretes GH, PRL, ACTH, TSH, FSH, LH. Posterior (neurohypophysis): stores and releases hormones synthesized in the hypothalamus — ADH/AVP and oxytocin.",
    "الأمامية (الغدّية): ينظّمها الوطاء بهرمونات محرِّرة ومثبِّطة ينقلها الجهاز البابي، وتفرز `GH` و`PRL` و`ACTH` و`TSH` و`FSH` و`LH`. الخلفية (العصبية): تخزّن وتحرّر هرمونات مصنّعة في الوطاء، وهي `ADH/AVP` والأوكسيتوسين."),
 IM("List the major anterior pituitary hormones and their main functions.", "عدّد أهم هرمونات النخامية الأمامية ووظائفها الرئيسة.",
    "GH: body growth and metabolism; PRL: milk production; ACTH: cortisol secretion from the adrenal cortex; TSH: thyroid hormone production; FSH: follicular development and spermatogenesis; LH: ovulation and sex hormone production.",
    "هرمون النمو `(GH)` لنمو الجسم والأيض، والبرولاكتين `(PRL)` لإنتاج الحليب، والهرمون الموجّه لقشرة الكظر `(ACTH)` لإفراز الكورتيزول، والهرمون المحفّز للدرقية `(TSH)` لإنتاج هرمونات الدرقية، والهرمون المحفّز للجريب `(FSH)` لنموّ الجريبات وتكوين النطف، والهرمون اللوتيني `(LH)` للإباضة وإنتاج الهرمونات الجنسية."),
 IM("Name the posterior pituitary hormones and their functions.", "اذكر هرمونات النخامية الخلفية ووظائفها.",
    "ADH/AVP: increases water reabsorption in the kidney collecting ducts. Oxytocin: promotes milk ejection and uterine contractions.",
    "الهرمون المضاد لإدرار البول `(ADH/AVP)` يزيد إعادة امتصاص الماء في القنوات الجامعة للكلية، والأوكسيتوسين يعزّز قذف الحليب وتقلّصات الرحم."),
 IM("List the hypothalamic factors that control anterior pituitary hormones and their effects.", "عدّد العوامل الوطائية التي تتحكّم في هرمونات النخامية الأمامية وتأثيراتها.",
    "GHRH stimulates GH; somatostatin inhibits GH; dopamine inhibits prolactin; CRH stimulates ACTH; TRH stimulates TSH; GnRH stimulates FSH and LH.",
    "يحفّز `GHRH` إفراز `GH` ويثبّطه السوماتوستاتين، ويثبّط الدوبامين إفراز البرولاكتين، ويحفّز `CRH` إفراز `ACTH`، ويحفّز `TRH` إفراز `TSH`، ويحفّز `GnRH` إفراز `FSH` و`LH`."),
 IM("Explain the negative feedback mechanism with an example.", "اشرح آلية التغذية الراجعة السلبية مع مثال.",
    "Hormones released by target endocrine glands inhibit further secretion from the hypothalamus and pituitary. Example: increased circulating T3 and T4 suppress TRH and TSH secretion.",
    "الهرمونات التي تحرّرها الغدد الصمّاء المستهدفة تثبّط استمرار الإفراز من الوطاء والنخامية. مثال: ارتفاع `T3` و`T4` الجائلة يكبح إفراز `TRH` و`TSH`."),
]

meta = dict(subject_en="Endocrine", subject_ar="الغدد الصمّاء",
            short_ar="غدد",
            unit_en="Lab 2", unit_ar="العملي 2", unit_label="LAB", unit_no="2",
            title_en="Hypothalamus and Pituitary Gland", title_ar="الوطاء والغدة النخامية",
            kind="Laboratories — عملي", stage="The third stage — الثالثة",
            instructor="م.م. نور إبراهيم")

folder = "endocrine-lab2-hypothalamus-pituitary"
qs = [q for q in mcq if "answer" in q]
print(folder, len(qs), dict(Counter(q["answer"] for q in qs)), len(tf), dict(Counter(t["answer"] for t in tf)), len(traps), len(important))
d = "/home/user/-/" + folder
os.makedirs(d, exist_ok=True)
json.dump({"meta": meta, "blocks": blocks,
           "questions": {"mcq": mcq, "tf": tf, "traps": traps, "important": important}},
          open(d + "/lecture.json", "w"), ensure_ascii=False, indent=1)
