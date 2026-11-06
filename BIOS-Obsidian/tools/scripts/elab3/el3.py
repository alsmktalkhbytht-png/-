import sys, re; sys.path.insert(0, "/tmp/claude-0/-home-claude/4a281dcf-357b-50ce-b2f4-8802cfcc6472/scratchpad/imm456")
from ci import *            # c helpers + B INSHORT TERMS balance save(split.fix)

# Clinical Enzymology — practical lab 3 (stage 4) — د. بارق & د. هشام — Serum Alkaline Phosphatase (ALP)
# Source: 3-page Word PDF headed "Advanced clinical Biochemistry (practical) 4th stage 2023-2024".

BN = lambda en, ar: N(en, ar, label=["BIOS note", "ملاحظة BIOS"])
O = P
def TERMS5(terms, n=5):
    head = [B("Term", "المصطلح"), "الترجمات العربية المستعملة"]
    return [SEC("Key terms", "أهم المصطلحات")] + [T(head, [[f"**{e}**", a] for e, a in terms[i:i + n]], ar_cols=[1], widths=[36, 64])
                                                  for i in range(0, len(terms), n)]

blocks = [
 # ───────────────────────── 1. ALP
 SEC("Serum Alkaline Phosphatase ALP", "الفوسفاتيز القاعدي في المصل"),
 C("**Alkaline Phosphatase (ALP)** is an enzyme originating mainly in: The bone, Liver, Placenta With some activity in the kidney and Intestines.",
   "**الفوسفاتيز القاعدي (ALP)** إنزيم يأتي أساسًا من: **العظم، والكبد، والمشيمة**، مع بعض الفعالية في **الكلية والأمعاء**."),
 L(["It is called alkaline because it functions best at a pH of 9.", "ALP levels are age and gender dependent.",
    "Alkaline Phosphatase is used as an index of liver and bone disease when correlated with other clinical findings."],
   ["سُمّي **قاعديًا** لأنه يعمل بأفضل شكل عند **pH = 9**.", "مستويات ALP **تعتمد على العمر والجنس**.",
    "يُستعمل الفوسفاتيز القاعدي **مؤشّرًا لأمراض الكبد والعظم** عند ربطه بالنتائج السريرية الأخرى."]),
 L(["In bone disease, the enzyme level rises in proportion to new bone cell production resulting from osteoplastic activity and the deposit of calcium in the bones.",
    ["In liver disease, the blood level rises when excretion of this enzyme is impaired as a result of obstruction in the biliary tract.", "Used alone, alkaline Phosphatase may be misleading."]],
   ["في **أمراض العظم** يرتفع مستوى الإنزيم **بالتناسب مع إنتاج خلايا عظمية جديدة** الناتج عن **نشاط بانيات العظم** وترسّب الكالسيوم في العظام.",
    ["في **أمراض الكبد** يرتفع مستواه في الدم عندما **يتعطّل إخراج هذا الإنزيم** نتيجة **انسداد القناة الصفراوية**.", "وإذا استُعمل الفوسفاتيز القاعدي **وحده** فقد يكون **مضلّلًا**."]],
   start=4),
 BN("“osteoplastic” in the sheet means **osteoblastic** (bone-forming cells).", "“osteoplastic” في الورقة يقصد بها **osteoblastic** أي نشاط **بانيات العظم**."),
 INSHORT([("Sources: **bone, liver, placenta** (+ some kidney and intestine).", "المصادر: **العظم، الكبد، المشيمة** (+ قليل من الكلية والأمعاء)."),
          ("Works best at **pH 9** → “alkaline”; levels depend on **age and sex**.", "يعمل أفضل عند **pH 9** ← “قاعدي”؛ ومستوياته تعتمد على **العمر والجنس**."),
          ("Bone: rises with **new bone formation**; liver: rises with **biliary obstruction**; alone it may mislead.", "العظم: يرتفع مع **تكوين عظم جديد**؛ الكبد: يرتفع مع **انسداد القناة الصفراوية**؛ ووحده قد يضلّل.")]),

 # ───────────────────────── 2. Normal value
 SEC("Normal Value", "القيم الطبيعية"),
 T([B("Sex", "الجنس"), B("Age", "العمر"), B("Normal Value", "القيمة الطبيعية")],
   [[B("**Females**", "**الإناث**"), B("1–12 years", "1–12 سنة"), B("<350 U/L", "أقل من 350 وحدة/لتر")],
    [B("", ""), B(">15 years", "أكثر من 15 سنة"), B("25–100 U/L", "25–100 وحدة/لتر")],
    [B("**Males**", "**الذكور**"), B("1–12 years", "1–12 سنة"), B("<350 U/L", "أقل من 350 وحدة/لتر")],
    [B("", ""), B("12–14 years", "12–14 سنة"), B("<500 U/L", "أقل من 500 وحدة/لتر")],
    [B("", ""), B(">20 years", "أكثر من 20 سنة"), B("25–100 U/L", "25–100 وحدة/لتر")]],
   key_cols=[0], widths=[24, 34, 42]),
 INSHORT([("Adults: **25–100 U/L**; children: **< 350 U/L** (growing bones); boys 12–14 y: **< 500 U/L** (growth spurt).", "البالغون: **25–100 وحدة/لتر**؛ الأطفال: **أقل من 350** (عظام تنمو)؛ الذكور 12–14 سنة: **أقل من 500** (طفرة النمو).")]),

 # ───────────────────────── 3. Clinical significance
 SEC("Clinical significance", "الأهمية السريرية"),
 L(["Liver disease (obstructive jaundice, hepatic carcinoma, Hepatocellular cirrhosis, Hepatitis, infectious mononucleosis)",
    "Diabetes mellitus and diabetic hepatic lipidosis.", "Chronic alcohol ingestion.", "Bone disease (Metastatic bone tumor, osteogenic sarcoma, and osteomalacia)"],
   ["**أمراض الكبد** (اليرقان الانسدادي، سرطان الكبد، تليّف الكبد الخلوي، التهاب الكبد، داء كثرة الوحيدات العدوائي)",
    "**داء السكري** والتشحّم الكبدي السكري.", "**تناول الكحول المزمن**.", "**أمراض العظم** (ورم العظم النقيلي، الساركوما العظمية، تليّن العظام)"],
   en="**Increased levels of ALP in:**", ar="**يرتفع ALP في:**", alpha=True),
 L(["Hyperparathyroidism and hyperthyroidism.", "Pulmonary and myocardial infarctions.", "Cancer of lung or pancreas."],
   ["فرط نشاط جارات الدرقية وفرط نشاط الدرقية.", "احتشاء الرئة واحتشاء عضلة القلب.", "سرطان الرئة أو البنكرياس."],
   en="**Decreased levels of ALP in:**", ar="**ينخفض ALP في:**", alpha=True),
 L(["Ulcerative colitis, peptic ulcer.", "Chronic renal failure.", "Magnesium and zinc deficiency (nutritional) and etc."],
   ["التهاب القولون التقرّحي، القرحة الهضمية.", "الفشل الكلوي المزمن.", "نقص المغنيسيوم والزنك (غذائي) وغيرها."], alpha=True, start=4),
 BN("Many textbooks list **hyperparathyroidism and hyperthyroidism** among the causes of **increased** ALP (high bone turnover), and **hypo**thyroidism / **hypo**parathyroidism among the decreased ones — the sheet is copied as written; follow your instructor in the exam.",
    "كثير من الكتب تذكر **فرط جارات الدرقية وفرط الدرقية** ضمن أسباب **ارتفاع** ALP (زيادة تجدّد العظم)، و**قصور** الدرقية / جارات الدرقية ضمن أسباب الانخفاض — نقلنا الورقة كما هي؛ واتّبع أستاذك في الامتحان."),
 T([B("↑ ALP", "ارتفاع ALP"), B("↓ ALP", "انخفاض ALP")],
   [[B("liver disease (obstructive jaundice…)", "أمراض الكبد (اليرقان الانسدادي…)"), B("hyperparathyroidism, hyperthyroidism (sheet)", "فرط جارات الدرقية وفرط الدرقية (الورقة)")],
    [B("diabetes mellitus, hepatic lipidosis", "السكري، التشحّم الكبدي"), B("pulmonary / myocardial infarction", "احتشاء الرئة / القلب")],
    [B("chronic alcohol", "الكحول المزمن"), B("cancer of lung or pancreas", "سرطان الرئة أو البنكرياس")],
    [B("bone disease (metastases, osteogenic sarcoma, osteomalacia)", "أمراض العظم (النقائل، الساركوما العظمية، تليّن العظام)"), B("ulcerative colitis, peptic ulcer, chronic renal failure, Mg & Zn deficiency", "التهاب القولون التقرّحي، القرحة، الفشل الكلوي المزمن، نقص Mg وZn")]],
   widths=[50, 50], style="summary", label_en="Up or down", label_ar="ارتفاع أم انخفاض"),
 INSHORT([("**↑** mainly in **liver (obstructive jaundice)** and **bone** disease, also diabetes and chronic alcohol.", "**يرتفع** أساسًا في أمراض **الكبد (اليرقان الانسدادي)** و**العظم**، وأيضًا السكري والكحول المزمن."),
          ("**↓** in the sheet: hyperpara- / hyperthyroidism, infarctions, lung/pancreas cancer, ulcerative colitis, renal failure, **Mg and Zn deficiency**.", "**ينخفض** حسب الورقة: فرط جارات الدرقية/الدرقية، الاحتشاءات، سرطان الرئة/البنكرياس، التهاب القولون التقرّحي، الفشل الكلوي، **نقص Mg وZn**.")]),

 # ───────────────────────── 4. Sample and interfering factors
 SEC("Sample", "العيّنة"),
 L([["ALP levels increase at room temperature and in refrigerated storage.", "Testing should be done the same day."],
    "ALP levels decrease if blood is anticoagulated.", "ALP levels increase after fatty meals."],
   [["ترتفع مستويات ALP **بدرجة حرارة الغرفة وفي الخزن المبرّد**.", "لذا يجب إجراء الفحص **في اليوم نفسه**."],
    "تنخفض مستويات ALP إذا **أُضيف مانع تخثّر للدم**.", "ترتفع مستويات ALP **بعد الوجبات الدسمة**."]),
 C("**Sample:** serum or plasma", "**العيّنة:** مصل أو بلازما"),
 INSHORT([("Test **the same day**; storage (room or fridge) **raises** ALP; anticoagulant **lowers** it; fatty meal **raises** it.", "افحص **في نفس اليوم**؛ الخزن (غرفة أو ثلاجة) **يرفع** ALP؛ مانع التخثّر **يخفضه**؛ الوجبة الدسمة **ترفعه**."),
          ("Sample: **serum or plasma**.", "العيّنة: **مصل أو بلازما**.")]),

 # ───────────────────────── 5. Principle, procedure, calculation
 SEC("The principle", "مبدأ الفحص"),
 C("**The principle:** p-Nitrophenylphosphate + H2O → phosphate + p-Nitrophenol", "**المبدأ:** `p-Nitrophenylphosphate + H2O → phosphate + p-Nitrophenol`"),
 BN(["ALP splits the colourless substrate **p-nitrophenylphosphate** into phosphate and **p-nitrophenol**, which is **yellow** in alkaline buffer.", "The rate of increase in absorbance per minute is proportional to the ALP activity."],
    ["يحلّل ALP المادة الأساس عديمة اللون **بارا-نايتروفينيل فوسفات** إلى فوسفات و**بارا-نايتروفينول** الذي يكون **أصفر** في المحلول القاعدي.", "ومعدّل زيادة الامتصاص في الدقيقة يتناسب مع فعالية ALP."]),
 H2("Procedure: with starter reagent", "طريقة العمل: باستعمال كاشف البدء"),
 T([B("Step", "الخطوة"), B("Volume", "الحجم")],
   [[B("**sample**", "**العيّنة**"), B("20 microL", "20 مايكرولتر")],
    [B("**BUF**", "**المحلول المنظّم (BUF)**"), B("1000 microL", "1000 مايكرولتر")],
    [B("Mix, incubate for 1 min", "امزج، وحضّن لمدة دقيقة"), B("—", "—")],
    [B("**SUB**", "**المادة الأساس (SUB)**"), B("250 microL", "250 مايكرولتر")],
    [B("Mix, read the Abs after 1 min, and the same time read the Abs again after 1,2 and 3 min", "امزج، واقرأ الامتصاص بعد دقيقة، ثم اقرأه مرّة أخرى بعد 1 و2 و3 دقائق"), B("—", "—")]],
   key_cols=[0], widths=[70, 30]),
 BN("BUF = **buffer**, SUB = **substrate** (p-nitrophenylphosphate); the substrate is the **starter reagent** — it is added last to start the reaction.",
    "BUF = **المحلول المنظّم**، وSUB = **المادة الأساس** (بارا-نايتروفينيل فوسفات)؛ والمادة الأساس هي **كاشف البدء** — تُضاف أخيرًا لتبدأ التفاعل."),
 FLOW([("sample 20 µL", "العيّنة 20"), ("+ BUF 1000 µL", "+ المنظّم 1000"), ("mix, 1 min", "مزج، دقيقة"), ("+ SUB 250 µL", "+ المادة الأساس 250"), ("read Abs at 1, 2, 3 min", "اقرأ عند 1، 2، 3 دقائق")]),
 H2("CALCULATION", "الحساب"),
 C("**U\\I = A\\min x 3433**", "**`U/L = ΔA/min × 3433`**"),
 BN(["“U\\I” means **U/L** and “A\\min” means the **mean change in absorbance per minute (ΔA/min)**.", "Example: ΔA/min = 0.030 → 0.030 × 3433 ≈ **103 U/L** (just above the adult range 25–100)."],
    ["“U\\I” يقصد بها **U/L** و“A\\min” تعني **متوسّط التغيّر في الامتصاص لكل دقيقة (ΔA/min)**.", "مثال: `ΔA/min = 0.030 → 0.030 × 3433 ≈ 103 U/L` (أعلى بقليل من مدى البالغين 25–100)."]),
 INSHORT([("**pNPP + H2O → phosphate + p-nitrophenol** (yellow); kinetic reading of absorbance.", "**pNPP + H2O → فوسفات + بارا-نايتروفينول** (أصفر)؛ قراءة حركية للامتصاص."),
          ("**20 µL sample + 1000 µL BUF**, 1 min, then **250 µL SUB** (starter); read at 1, 2, 3 min.", "**20 مايكرولتر عيّنة + 1000 منظّم**، دقيقة، ثم **250 مادة أساس** (كاشف البدء)؛ اقرأ عند 1 و2 و3 دقائق."),
          ("Activity: **U/L = ΔA/min × 3433**.", "الفعالية: **U/L = ΔA/min × 3433**.")]),

 *TERMS5([("Alkaline phosphatase (ALP)", "الفوسفاتيز القاعدي / الفوسفاتاز القلوي"), ("Osteoblastic activity", "نشاط بانيات العظم / النشاط العظمي البنّاء"),
          ("Biliary obstruction", "انسداد القناة الصفراوية / انسداد مجرى الصفراء"), ("Obstructive jaundice", "اليرقان الانسدادي / الصفار الانسدادي"),
          ("Infectious mononucleosis", "داء كثرة الوحيدات العدوائي / حمّى الغدد"), ("Osteogenic sarcoma", "الساركوما العظمية / ورم العظم الخبيث"),
          ("Osteomalacia", "تليّن العظام"), ("Hepatic lipidosis", "التشحّم الكبدي / الكبد الدهني"),
          ("Myocardial infarction", "احتشاء عضلة القلب / الجلطة القلبية"), ("Ulcerative colitis", "التهاب القولون التقرّحي"),
          ("Anticoagulated blood", "دم مضاف إليه مانع تخثّر"), ("p-Nitrophenylphosphate (pNPP)", "بارا-نايتروفينيل فوسفات"),
          ("p-Nitrophenol", "بارا-نايتروفينول"), ("Buffer (BUF)", "المحلول المنظّم / الدارئ"),
          ("Substrate (SUB) / starter reagent", "المادة الأساس / كاشف البدء"), ("Absorbance (Abs)", "الامتصاص / الامتصاصية")]),
]

exec(open(__file__.replace("el3.py", "el3q.py")).read())
