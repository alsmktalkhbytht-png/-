---
source: BIOS-Obsidian/tools/scripts/n2/make1.py
handouts: [enzymology-lec1-introduction]
saved: 2026-10-29
tags: [bios, code]
---
# n2/make1.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#enzymology-lec1-introduction|enzymology-lec1-introduction]]

```python
import json
from collections import Counter
def C(en, ar, **k): return dict(t="card", en=en, ar=ar, **k)
def R(en, ar): return dict(t="rule", en=en, ar=ar)
def SEC(en, ar): return dict(t="section", en=en, ar=ar)
def H2(en, ar): return dict(t="h2", en=en, ar=ar)
def G(te, ta, en, ar, **k): return dict(t="group", title_en=te, title_ar=ta, en=en, ar=ar, **k)
def F(src, en, ar, **k): return dict(t="figure", src="assets/" + src, en=en, ar=ar, **k)
def FF(*items): return dict(t="figures", items=[dict(src="assets/" + s, en=e, ar=a, h=h, fit="contain") for s, e, a, h in items])
def EQ(src, h="14mm"): return dict(t="eq", src=["assets/" + s for s in src] if isinstance(src, list) else "assets/" + src, h=h)
def N(en, ar, label=None):
    b = dict(t="note", en=en, ar=ar)
    if label: b["label"] = label
    return b

blocks = [
 SEC("Enzymes", "الإنزيمات"),
 C(["**Enzymes**: are **protein catalysts** (and occasionally **RNA called ribozymes**) similar to chemical catalyst such as Pt or Fe+2, that **increases the rate of reactions without itself being consumed**.",
    "Enzymes has a molecular weight in the range of **12,000 1,000,000**."],
   ["**الإنزيمات** (`Enzymes`): هي **عوامل مساعدة (محفّزات) بروتينية** (وأحيانًا **`RNA` يُسمّى الرايبوزايمات** `ribozymes`) تشبه المحفّزات الكيميائية مثل البلاتين `Pt` أو الحديد `Fe+2`، و**تزيد سرعة التفاعلات من دون أن تُستهلك هي نفسها**.",
    "ويتراوح الوزن الجزيئي للإنزيمات بين **12,000 و1,000,000**."]),
 C(["Enzymes act with **high specificity** on one or a class of particular substances called **substrates**.",
    "Enzymes differ from chemical catalyst in their following properties:"],
   ["تعمل الإنزيمات **بتخصّص عالٍ** على مادة واحدة أو صنف من مواد معيّنة تُسمّى **المواد الأساس (الركائز)** `substrates`.",
    "وتختلف الإنزيمات عن المحفّزات الكيميائية في الخصائص الآتية:"],
   alpha=True,
   list_en=["They have a **high degree of specificity** for their substrates; therefore **no side reaction** occurs, so no wasteful by-products are produced.",
            "They **accelerate chemical reactions tremendously**,",
            "They function in aqueous solutions under **very mild conditions** of pressure, temperature and pH, and this rare in non biological catalysts."],
   list_ar=["لها **درجة عالية من التخصّص** لركائزها؛ لذلك **لا تحدث تفاعلات جانبية**، فلا تُنتَج نواتج ثانوية مهدورة.",
            "**تُسرّع التفاعلات الكيميائية تسريعًا هائلًا**،",
            "تعمل في المحاليل المائية تحت **ظروف معتدلة جدًا** من الضغط والحرارة والأس الهيدروجيني، وهذا نادر في المحفّزات غير الحيوية."]),

 SEC("Nomenclature and Classification of Enzymes", "تسمية الإنزيمات وتصنيفها"),
 C("Each enzyme is assigned two names, **recommended name** and **systematic name**.",
   "يُعطى كل إنزيم اسمين: **الاسم الموصى به** و**الاسم النظامي**."),
 G("a. Recommended name", "أ. الاسم الموصى به",
   ["Enzyme are names related to the **substrate** that act on it with adding the suffix **\"-ase\"** (for example, glucosidase urease, sucrase), or names according to the **nature of enzymatic reaction** (for example, lactate dehydrogenase and adenylyl cyclase).",
    "There are some difficulties were appeared for this name, because some enzymes take names which not indicate on their acts, for example, **trypsin and pepsin**, for this reason a systematic name is suggested."],
   ["تُسمّى الإنزيمات نسبةً إلى **الركيزة** التي تعمل عليها مع إضافة اللاحقة **`-ase`** (مثل `glucosidase` و`urease` و`sucrase`)، أو بحسب **طبيعة التفاعل الإنزيمي** (مثل `lactate dehydrogenase` و`adenylyl cyclase`).",
    "وظهرت بعض الصعوبات في هذه التسمية، لأن بعض الإنزيمات تحمل أسماء لا تدل على عملها، مثل **التربسين والببسين**، ولهذا اقتُرح الاسم النظامي."]),
 G("b. Systematic name", "ب. الاسم النظامي",
   "Developed by the **International Union of Biochemistry and Molecular Biology (IUBMB)**. The most important of this system was followed:",
   "وضعه **الاتحاد الدولي للكيمياء الحيوية والبيولوجيا الجزيئية** (`IUBMB`). وأهم ما يتّبعه هذا النظام:"),
 R(["Enzymes are divided into **six major classes**, as shown in the table below.", "Within each class are **subclasses**, and under each subclass are **sub-subclasses**."],
   ["تُقسَّم الإنزيمات إلى **ستة أصناف رئيسة**، كما في الجدول أدناه.", "وداخل كل صنف **أصناف فرعية**، وتحت كل صنف فرعي **أصناف فرعية ثانوية**."]),
 R("Enzyme name consist of **two part**, the first refer to the **substrate (s)**, and the second refer to the **nature of enzymatic reaction** end with the suffix **(-ase)**.",
   "يتكوّن اسم الإنزيم من **جزأين**: الأول يشير إلى **الركيزة (أو الركائز)**، والثاني يشير إلى **طبيعة التفاعل الإنزيمي** وينتهي باللاحقة **(`-ase`)**."),
 R("If additional information requires for clarifying the nature of reaction, the previous information was followed and put it in **parentheses**. **For example:**",
   "إذا تطلّب الأمر معلومات إضافية لتوضيح طبيعة التفاعل، تُتبَع المعلومات السابقة وتوضع بين **قوسين**. **مثال:**"),
 FF(("malic-enzyme.jpg", "Recommended enzyme name: Malic enzyme (L-Malate → pyruvate)", "الاسم الموصى به: الإنزيم الماليكي (`L-Malate` ← `pyruvate`)", "34mm"),
    ("malic-systematic.jpg", "Systematic enzyme name: L-Malate: NAD oxidoreductase (decarboxylating) — substrate · reaction nature · reaction occure by removing carboxyle group as CO2", "الاسم النظامي: الركيزة · طبيعة التفاعل · التفاعل يحدث بإزالة مجموعة الكاربوكسيل بشكل `CO2`", "34mm")),
 R("For each enzyme there is a **systematic code number** consist of **four numbers** and a sign **E.C. (Enzyme Code)**.",
   "لكل إنزيم **رقم رمزي نظامي** يتكوّن من **أربعة أرقام** والعلامة **`E.C.`** (رمز الإنزيم)."),
 C("", "", list_en=["**First number** represents the **major class** of enzyme, which clarifies the nature of reaction.",
                    "**Second number** represents the **subclass** of enzyme which specifies the group or bond related for catalyst.",
                    "**Third number** represents the **sub-subclass** of enzyme which refers for example to the compound that accepted the electrons in oxidoreductase reactions.",
                    "**Fourth number** represents the **serial listing** of the enzyme in its sub-sub classes, which give randomly."],
   list_ar=["**الرقم الأول** يمثّل **الصنف الرئيس** للإنزيم، ويوضّح طبيعة التفاعل.",
            "**الرقم الثاني** يمثّل **الصنف الفرعي** للإنزيم، ويحدّد المجموعة أو الآصرة المتعلّقة بالتحفيز.",
            "**الرقم الثالث** يمثّل **الصنف الفرعي الثانوي**، ويشير مثلًا إلى المركّب الذي يستقبل الإلكترونات في تفاعلات الأكسدة والاختزال.",
            "**الرقم الرابع** يمثّل **الترتيب التسلسلي** للإنزيم ضمن صنفه الفرعي الثانوي، ويُعطى عشوائيًا."]),

 SEC("The six major classes", "الأصناف الرئيسة الستة"),
 F("ec-classes-1.jpg", "Systematic Classification of Enzymes According to the Enzyme Commission (classes 1–2)", "التصنيف النظامي للإنزيمات بحسب لجنة الإنزيمات (الصنفان 1–2)", h="96mm"),
 F("ec-classes-2.jpg", "Systematic classification (classes 3–6)", "التصنيف النظامي (الأصناف 3–6)", h="96mm"),
 dict(t="table", head=["E.C.", "Class", "الصنف", "Example (from the slides)"], ar_cols=[2], key_cols=[1], widths=["12mm", "", "", ""], numbered=True,
      rows=[["1", "Oxidoreductases", "إنزيمات الأكسدة والاختزال", "Pyruvate → L-Lactate (lactate dehydrogenase)"],
            ["2", "Transferases", "الإنزيمات الناقلة", "Glucose → Glucose 6-phosphate (hexokinase)"],
            ["3", "Hydrolases", "إنزيمات التحلّل المائي", "Maltose → Glucose + Glucose (maltase)"],
            ["4", "Lyases", "الإنزيمات المحلِّلة (الفاصلة)", "Fumarate → L-malate (fumarase)"],
            ["5", "Isomerases", "إنزيمات المماكبة", "3-phosphoglycerate ⇌ 2-phosphoglycerate (phosphoglyceromutase)"],
            ["6", "Ligases", "الإنزيمات الرابطة", "Pyruvate → Oxaloacetate (pyruvate carboxylase)"]]),
 FF(("oxidoreductase.jpg", "1. Oxidoreductases", "1. إنزيمات الأكسدة والاختزال", "36mm"),
    ("transferase.jpg", "2. Transferases", "2. الإنزيمات الناقلة", "36mm")),
 FF(("hydrolase.jpg", "3. Hydrolases", "3. إنزيمات التحلّل المائي", "32mm"),
    ("lyase.jpg", "4. Lyases", "4. الإنزيمات المحلِّلة", "32mm")),
 FF(("isomerase.jpg", "5. Isomerases", "5. إنزيمات المماكبة", "30mm"),
    ("ligase.jpg", "6. Ligases", "6. الإنزيمات الرابطة", "30mm")),

 SEC("Properties of enzymes", "خصائص الإنزيمات"),
 H2("a. Active sites", "أ. المواقع الفعّالة"),
 C(["Enzyme molecules contain a **specific pocket or cleft** of amino acid side chains that create a **three-dimensional surface complementary to the substrate** as shown in the figure below:",
    "Two major hypotheses suggested explaining the active site function."],
   ["تحتوي جزيئات الإنزيم على **جيب أو شقّ خاص** من السلاسل الجانبية للأحماض الأمينية يكوّن **سطحًا ثلاثي الأبعاد مكمّلًا للركيزة** كما في الشكل أدناه:",
    "واقتُرحت فرضيتان رئيستان لتفسير عمل الموقع الفعّال."]),
 G("Lock and key hypothesis", "فرضية القفل والمفتاح",
   "Proposed by **Fischer** that is the active site of the enzyme it is **complementary in shape** to that at the substrate.",
   "اقترحها **فيشر** (`Fischer`)، ومفادها أن الموقع الفعّال للإنزيم **مكمّل في شكله** لشكل الركيزة."),
 G("Induced- Fit Hypothesis", "فرضية التلاؤم المستحث",
   ["Proposes by **Koshland**:", "a. The enzymes **change shape** upon binding substrate.", "b. The active site has a shape complementary to that of the substrate **only after the substrate is bound**."],
   ["اقترحها **كوشلاند** (`Koshland`):", "أ. **يتغيّر شكل** الإنزيمات عند ارتباطها بالركيزة.", "ب. يصبح للموقع الفعّال شكل مكمّل لشكل الركيزة **فقط بعد ارتباط الركيزة**."]),
 FF(("lock-and-key.jpg", "Lock and key hypothesis (Fischer)", "فرضية القفل والمفتاح (فيشر)", "42mm"),
    ("induced-fit.jpg", "Induced-fit hypothesis (Koshland)", "فرضية التلاؤم المستحث (كوشلاند)", "42mm")),
 H2("b. Catalytic efficiency", "ب. الكفاءة التحفيزية"),
 C("", "", list_en=["Most enzyme-catalyzed reactions are **highly efficient**, proceeding from **103 to 108 times faster** than uncatalyzed reactions.",
                    "Each enzyme molecule is capable of transforming **100 to 1000 substrate molecules** into product **each second**."],
   list_ar=["معظم التفاعلات التي تحفّزها الإنزيمات **عالية الكفاءة**، إذ تجري **أسرع بـ 10³ إلى 10⁸ مرة** من التفاعلات غير المحفَّزة.",
            "كل جزيء إنزيم قادر على تحويل **100 إلى 1000 جزيء ركيزة** إلى ناتج **في كل ثانية**."]),
 H2("C. Specificity", "ج. التخصّص"),
 C("Enzymes are highly specific, interacting either with **one substrate (absolute specificity)** like **urease** enzyme which is the hydrolyze urea only, or act on a **specified mode of groups or bonds (group specificity)** like **trypsin** enzyme which is catalyzing of the peptide bonds hydrolysis on the carboxyl side of lysine and arginine residues only.",
   "الإنزيمات عالية التخصّص؛ فهي إما تتفاعل مع **ركيزة واحدة (تخصّص مطلق)** مثل إنزيم **اليوريز** الذي يحلّل اليوريا فقط، أو تعمل على **نوع محدّد من المجاميع أو الأواصر (تخصّص مجموعي)** مثل إنزيم **التربسين** الذي يحفّز تحلّل الأواصر الببتيدية من جهة الكاربوكسيل لبقايا اللايسين والأرجنين فقط."),
 H2("d. Regulation", "د. التنظيم"),
 C("Enzyme activity can be regulated, that is, enzymes can be **activated or inhibited**, so that the rate of product formation responds to the needs of the cell.",
   "يمكن تنظيم فعالية الإنزيم، أي يمكن **تنشيط الإنزيمات أو تثبيطها**، بحيث تستجيب سرعة تكوين الناتج لحاجات الخلية."),
 H2("e. Cofactors", "هـ. العوامل المساعدة"),
 C("Some enzymes associate with a **nonprotein cofactor** that is needed for enzymatic activity. Commonly encountered cofactors include:",
   "ترتبط بعض الإنزيمات بـ**عامل مساعد غير بروتيني** ضروري للفعالية الإنزيمية. ومن العوامل المساعدة الشائعة:"),
 G("1. Organic molecules,", "1. الجزيئات العضوية،",
   ["a. **Coenzymes:** are often **derivatives of vitamins** that are **weakly bind** to the active site of enzyme.",
    "**For example**, the coenzyme **NAD+ contains niacin**, **FAD contains riboflavin**, and **coenzyme A contains pantothenic acid**.",
    "b. **Prosthetic groups:** Is **tightly bound coenzyme** that does not dissociate from the enzyme. For example, the **biotin**."],
   ["أ. **المرافقات الإنزيمية** (`Coenzymes`): غالبًا ما تكون **مشتقّات فيتامينات** **ترتبط ارتباطًا ضعيفًا** بالموقع الفعّال للإنزيم.",
    "**مثلًا**، يحتوي المرافق `NAD+` على **النياسين**، و`FAD` على **الرايبوفلافين**، والمرافق `A` على **حمض البانتوثينيك**.",
    "ب. **المجاميع الملحقة (التعويضية)** (`Prosthetic groups`): مرافق إنزيمي **مرتبط بإحكام** لا ينفصل عن الإنزيم. مثل **البايوتين**."]),
 G("2. Metal ions:", "2. الأيونات الفلزية:",
   "such as **Zn+2 or Fe+2**. These ions may be act in different mechanism such as:",
   "مثل `Zn+2` أو `Fe+2`. وقد تعمل هذه الأيونات بآليات مختلفة مثل:"),
 C("", "", list_en=["**Essential components** of enzyme active site.", "May be act as a **bridge** connects the substrate to enzyme to form coordinate complexes.",
                    "Can be **stabilized the enzyme conformation** by interact its charge with the opposite charge of enzyme."],
   list_ar=["**مكوّنات أساسية** في الموقع الفعّال للإنزيم.", "قد تعمل **جسرًا** يربط الركيزة بالإنزيم لتكوين معقّدات تناسقية.",
            "يمكن أن **تُثبّت الشكل الفراغي للإنزيم** بتفاعل شحنتها مع الشحنة المعاكسة في الإنزيم."]),
 C("", "", list_en=["**Holoenzyme** refers to the enzyme with its cofactor.", "**Apoenzyme** refers to the protein portion of the holoenzyme."],
   list_ar=["**الإنزيم الكامل** (`Holoenzyme`) هو الإنزيم مع عامله المساعد.", "**الإنزيم البروتيني (الأبوإنزيم)** (`Apoenzyme`) هو الجزء البروتيني من الإنزيم الكامل."]),
 C("In the absence of the appropriate cofactor, the apoenzyme typically **does not show biologic activity**.",
   "في غياب العامل المساعد المناسب، **لا يُظهر** الأبوإنزيم عادةً **فعالية حيوية**."),
 N("**Holoenzyme = Apoenzyme + Cofactor**", "**الإنزيم الكامل = الأبوإنزيم + العامل المساعد**", label=["Rule", "قاعدة"]),

 SEC("Enzyme Units", "وحدات الإنزيم"),
 G("a. International Unit (IU)", "أ. الوحدة الدولية (`IU`)",
   "The amount of enzyme required to catalyze the conversion of **one micromole of substrate per minute** under optimum condition.",
   "كمية الإنزيم اللازمة لتحفيز تحويل **مايكرومول واحد من الركيزة في الدقيقة** تحت الظروف المثلى."),
 G("b. Turnover number", "ب. رقم التحوّل",
   "The number of substrate molecules converted to product **per second by single enzyme molecule**.",
   "عدد جزيئات الركيزة التي تتحوّل إلى ناتج **في الثانية بواسطة جزيء إنزيم واحد**."),
 G("c. Specific Activity", "ج. الفعالية النوعية",
   "The number of international units of enzyme present in **1 mg of protein**.",
   "عدد الوحدات الدولية من الإنزيم الموجودة في **1 ملغم من البروتين**."),
 G("d. Katal (kat)", "د. الكاتال (`kat`)",
   ["The amount of enzymatic activity that converts **one mole of substrate per second**.", "The katal (kat) is related to an enzyme unit (U) by the relation **1 kat = 6 x 1O7 U**."],
   ["مقدار الفعالية الإنزيمية الذي يحوّل **مولًا واحدًا من الركيزة في الثانية**.", "ويرتبط الكاتال بوحدة الإنزيم (`U`) بالعلاقة **`1 kat = 6 × 10⁷ U`**."]),

 SEC("Enzyme Kinetics", "حركيات الإنزيمات"),
 C(["I s a branch of enzymology study the **factors that effecting on the enzymatic reaction velocity**.", "The most important factors are:"],
   ["هي فرع من علم الإنزيمات يدرس **العوامل المؤثّرة في سرعة التفاعل الإنزيمي**.", "وأهم هذه العوامل:"], alpha=True,
   list_en=["Temperature.", "pH.", "Enzyme concentration.", "Substrate concentration."],
   list_ar=["درجة الحرارة.", "الأس الهيدروجيني `pH`.", "تركيز الإنزيم.", "تركيز الركيزة."]),
 H2("1. Effect of temperature", "1. تأثير درجة الحرارة"),
 C("The rate of an enzyme-catalyzed reaction **increases** when the temperature increased to **limited degree** as a result of **increasing kinetic energy** of reaction molecules then **decrease** when the temperature increasing over this degree as a result of there **denaturation**, as shown in the figure below.",
   "تزداد سرعة التفاعل المحفَّز إنزيميًا عند رفع درجة الحرارة **إلى حدّ معيّن** نتيجة **زيادة الطاقة الحركية** لجزيئات التفاعل، ثم **تنخفض** عند تجاوز هذه الدرجة نتيجة **مسخ (تغيّر طبيعة)** الإنزيم، كما في الشكل."),
 H2("2. Effect of pH", "2. تأثير الأس الهيدروجيني"),
 C(["The pH at which maximal enzyme activity is achieved that **differs for different enzymes** as shown in figure below.",
    "Each of these curves distinguished by **optimum pH** in which the enzyme activity reach to maximum."],
   ["الأس الهيدروجيني الذي تبلغ عنده فعالية الإنزيم أقصاها **يختلف باختلاف الإنزيمات** كما في الشكل.",
    "ويتميّز كل منحنٍ بـ**الأس الهيدروجيني الأمثل** الذي تصل عنده فعالية الإنزيم إلى أقصاها."]),
 FF(("temperature.jpg", "Effect of temperature: heat inactivation of enzyme", "تأثير الحرارة: التعطيل الحراري للإنزيم", "56mm"),
    ("ph.jpg", "Optimum pH: pepsin, trypsin, alkaline phosphatase", "الـ`pH` الأمثل: الببسين، التربسين، الفوسفاتيز القاعدي", "56mm")),
 C("**Decreasing enzyme activity on both side of pH can be explained by:**", "**يمكن تفسير انخفاض فعالية الإنزيم على جانبي الـ`pH` الأمثل بـ:**",
   list_en=["**denaturation of the enzyme**, because the **structure** of the catalytically active protein molecule depends on the ionic character of the amino acid side chains, therefore the enzyme loss its activity.",
            "The catalytic process usually requires that the enzyme and substrate have **specific chemical groups** either an ionized or non ionized state in order to interact, or this not happen only in limited pH."],
   list_ar=["**مسخ الإنزيم**، لأن **تركيب** جزيء البروتين الفعّال تحفيزيًا يعتمد على الصفة الأيونية للسلاسل الجانبية للأحماض الأمينية، فيفقد الإنزيم فعاليته.",
            "تتطلّب عملية التحفيز عادةً أن يمتلك الإنزيم والركيزة **مجاميع كيميائية محدّدة** في حالة متأيّنة أو غير متأيّنة لكي يتفاعلا، وهذا لا يحدث إلا ضمن مدى محدود من الـ`pH`."]),
 H2("3. Enzyme concentration", "3. تركيز الإنزيم"),
 C("The rate of an enzyme-catalyzed reaction **increases with the enzyme concentration**, but **not more than substrate concentration**.",
   "تزداد سرعة التفاعل المحفَّز إنزيميًا **بزيادة تركيز الإنزيم**، ولكن **ليس بما يتجاوز تركيز الركيزة**."),
 H2("4. Substrate concentration", "4. تركيز الركيزة"),
 C(["The rate of an enzyme-catalyzed reaction increases with substrate concentration increased until a **maximal velocity** is reached as shown in figure below.",
    "The more increasing of substrate concentrations not effect on the reaction rate of enzyme, which is reflects the **saturation** with substrate of all available binding sites on the enzyme molecules present."],
   ["تزداد سرعة التفاعل المحفَّز إنزيميًا بزيادة تركيز الركيزة حتى تُبلَغ **السرعة القصوى** كما في الشكل.",
    "والزيادة الأكبر في تركيز الركيزة لا تؤثّر في سرعة التفاعل، وهذا يعكس **تشبّع** جميع مواقع الارتباط المتاحة على جزيئات الإنزيم الموجودة بالركيزة."]),
 F("substrate-concentration.jpg", "Effect of substrate concentration: the rate approaches Vmax as the active sites become saturated", "تأثير تركيز الركيزة: تقترب السرعة من `Vmax` مع تشبّع المواقع الفعّالة", h="58mm"),
]

def Q(en, ar, opts, ans, **k):
    return dict(en=en, ar=ar, options=[list(o) for o in opts], answer=ans, **k)

mcq = [
 {"topic_en": "Enzymes and nomenclature", "topic_ar": "الإنزيمات وتسميتها"},
 Q("Enzymes are protein catalysts, and occasionally catalytic RNA called:", "الإنزيمات محفّزات بروتينية، وأحيانًا RNA محفّز يُسمّى:", [("Ribosomes", "الرايبوسومات"), ("Ribozymes", "الرايبوزايمات"), ("Coenzymes", "المرافقات الإنزيمية"), ("Isozymes", "الإنزيمات المتماثلة")], "b"),
 Q("Enzymes increase the rate of reactions:", "تزيد الإنزيمات سرعة التفاعلات:", [("And are consumed in the reaction", "وتُستهلك في التفاعل"), ("Only at high temperature", "فقط في الحرارة العالية"), ("Without being consumed", "من دون أن تُستهلك"), ("By producing by-products", "بإنتاج نواتج ثانوية")], "c"),
 Q("The molecular weight range of enzymes is:", "مدى الوزن الجزيئي للإنزيمات هو:", [("100 – 1,000", "100 – 1,000"), ("1,000 – 10,000", "1,000 – 10,000"), ("12,000 – 1,000,000", "12,000 – 1,000,000"), ("Above 10,000,000", "أكثر من 10,000,000")], "c"),
 Q("Enzymes differ from chemical catalysts in all of the following EXCEPT:", "تختلف الإنزيمات عن المحفّزات الكيميائية في كل مما يأتي عدا:", [("High specificity", "التخصّص العالي"), ("Work under mild conditions", "العمل في ظروف معتدلة"), ("Tremendous acceleration", "التسريع الهائل"), ("Producing wasteful by-products", "إنتاج نواتج ثانوية مهدورة")], "d"),
 Q("Which enzyme name does NOT indicate its action (a problem of recommended names)?", "أي اسم إنزيم لا يدل على عمله (مشكلة الأسماء الموصى بها)؟", [("Trypsin", "التربسين"), ("Urease", "اليوريز"), ("Sucrase", "السكريز"), ("Lactate dehydrogenase", "لاكتيت ديهيدروجينيز")], "a"),
 Q("The systematic naming of enzymes was developed by:", "وضع التسمية النظامية للإنزيمات:", [("WHO", "منظمة الصحة العالمية"), ("IUBMB", "IUBMB"), ("FDA", "FDA"), ("IUPAC only", "IUPAC فقط")], "b"),
 Q("A systematic enzyme name consists of:", "يتكوّن الاسم النظامي للإنزيم من:", [("Substrate + nature of reaction ending with -ase", "الركيزة + طبيعة التفاعل منتهيًا بـ -ase"), ("Discoverer name + -in", "اسم المكتشف + -in"), ("Organ + -ase", "العضو + -ase"), ("Product only", "الناتج فقط")], "a"),
 Q("In the E.C. number, the FIRST number represents:", "في رقم E.C. يمثّل الرقم الأول:", [("The serial listing", "الترتيب التسلسلي"), ("The sub-subclass", "الصنف الفرعي الثانوي"), ("The major class", "الصنف الرئيس"), ("The subclass", "الصنف الفرعي")], "c"),
 Q("The FOURTH number of the E.C. code represents:", "يمثّل الرقم الرابع في رمز E.C.:", [("The major class", "الصنف الرئيس"), ("The group or bond", "المجموعة أو الآصرة"), ("The electron acceptor", "مستقبل الإلكترونات"), ("The serial listing, given randomly", "الترتيب التسلسلي، ويُعطى عشوائيًا")], "d"),
 Q("Enzymes are divided into how many major classes?", "تُقسَّم الإنزيمات إلى كم صنفًا رئيسًا؟", [("Four", "أربعة"), ("Five", "خمسة"), ("Six", "ستة"), ("Seven", "سبعة")], "c"),
 Q("Lactate dehydrogenase (pyruvate → L-lactate) belongs to:", "ينتمي لاكتيت ديهيدروجينيز (البيروفيت ← اللاكتيت) إلى:", [("Oxidoreductases", "إنزيمات الأكسدة والاختزال"), ("Transferases", "الناقلة"), ("Hydrolases", "التحلّل المائي"), ("Ligases", "الرابطة")], "a"),
 Q("Hexokinase (glucose → glucose 6-phosphate) is a:", "الهكسوكاينيز (الكلوكوز ← كلوكوز 6-فوسفات) هو:", [("Lyase", "محلِّل"), ("Transferase", "ناقل"), ("Isomerase", "مماكب"), ("Hydrolase", "إنزيم تحلّل مائي")], "b"),
 Q("Maltase (maltose + H2O → glucose + glucose) is a:", "المالتيز (المالتوز + الماء ← كلوكوز + كلوكوز) هو:", [("Ligase", "رابط"), ("Isomerase", "مماكب"), ("Hydrolase", "إنزيم تحلّل مائي"), ("Oxidoreductase", "أكسدة واختزال")], "c"),
 Q("Phosphoglyceromutase (3-phosphoglycerate ⇌ 2-phosphoglycerate) is an:", "الفوسفوكليسيروميوتيز (3-فوسفوكليسيريت ⇌ 2-فوسفوكليسيريت) هو:", [("Isomerase", "مماكب"), ("Oxidoreductase", "أكسدة واختزال"), ("Lyase", "محلِّل"), ("Transferase", "ناقل")], "a"),
 Q("Ligases are characterized by:", "تتميّز الإنزيمات الرابطة بـ:", [("Addition to double bonds", "الإضافة إلى الأواصر المزدوجة"), ("ATP-dependent bond formation", "تكوين أواصر معتمد على ATP"), ("Hydrolysis", "التحلّل المائي"), ("Isomerization", "المماكبة")], "b"),
 {"topic_en": "Properties of enzymes", "topic_ar": "خصائص الإنزيمات"},
 Q("The lock and key hypothesis was proposed by:", "اقترح فرضية القفل والمفتاح:", [("Koshland", "كوشلاند"), ("Michaelis", "ميكايلس"), ("Fischer", "فيشر"), ("Menten", "منتن")], "c"),
 Q("According to the induced-fit hypothesis:", "وفق فرضية التلاؤم المستحث:", [("The active site is rigid", "الموقع الفعّال صلب"), ("The enzyme changes shape upon binding substrate", "يتغيّر شكل الإنزيم عند ارتباط الركيزة"), ("Substrate changes the enzyme permanently", "تغيّر الركيزة الإنزيم بشكل دائم"), ("No active site exists", "لا يوجد موقع فعّال")], "b"),
 Q("Enzyme-catalyzed reactions proceed faster than uncatalyzed reactions by:", "تجري التفاعلات المحفَّزة إنزيميًا أسرع من غير المحفَّزة بـ:", [("2 to 10 times", "2 إلى 10 مرات"), ("10³ to 10⁸ times", "10³ إلى 10⁸ مرة"), ("10¹² to 10²⁰ times", "10¹² إلى 10²⁰ مرة"), ("No difference", "لا فرق")], "b"),
 Q("Each enzyme molecule transforms how many substrate molecules per second?", "كم جزيء ركيزة يحوّل جزيء الإنزيم الواحد في الثانية؟", [("1 to 10", "1 إلى 10"), ("10 to 50", "10 إلى 50"), ("100 to 1000", "100 إلى 1000"), ("10⁶", "10⁶")], "c"),
 Q("Urease, which hydrolyzes urea only, is an example of:", "اليوريز الذي يحلّل اليوريا فقط مثال على:", [("Group specificity", "التخصّص المجموعي"), ("Absolute specificity", "التخصّص المطلق"), ("Regulation", "التنظيم"), ("Cofactor", "العامل المساعد")], "b"),
 Q("Trypsin hydrolyzes peptide bonds on the carboxyl side of:", "يحلّل التربسين الأواصر الببتيدية من جهة الكاربوكسيل لـ:", [("Glycine and alanine", "الكلايسين والألانين"), ("Proline only", "البرولين فقط"), ("Phenylalanine", "الفنيل ألانين"), ("Lysine and arginine", "اللايسين والأرجنين")], "d"),
 Q("Coenzymes are often derivatives of:", "المرافقات الإنزيمية غالبًا مشتقّات من:", [("Vitamins", "الفيتامينات"), ("Lipids", "الدهون"), ("Nucleic acids", "الأحماض النووية"), ("Hormones", "الهرمونات")], "a"),
 Q("FAD contains:", "يحتوي FAD على:", [("Niacin", "النياسين"), ("Pantothenic acid", "حمض البانتوثينيك"), ("Riboflavin", "الرايبوفلافين"), ("Biotin", "البايوتين")], "c"),
 Q("A tightly bound coenzyme that does not dissociate from the enzyme (e.g., biotin) is a:", "المرافق المرتبط بإحكام ولا ينفصل عن الإنزيم (مثل البايوتين) هو:", [("Apoenzyme", "أبوإنزيم"), ("Prosthetic group", "مجموعة ملحقة"), ("Substrate", "ركيزة"), ("Holoenzyme", "إنزيم كامل")], "b"),
 Q("Holoenzyme equals:", "الإنزيم الكامل يساوي:", [("Apoenzyme + Cofactor", "أبوإنزيم + عامل مساعد"), ("Apoenzyme − Cofactor", "أبوإنزيم − عامل مساعد"), ("Substrate + Product", "ركيزة + ناتج"), ("Coenzyme only", "مرافق إنزيمي فقط")], "a"),
 {"topic_en": "Units and kinetics", "topic_ar": "الوحدات والحركيات"},
 Q("The International Unit (IU) converts one micromole of substrate per:", "الوحدة الدولية (IU) تحوّل مايكرومولًا واحدًا من الركيزة في:", [("Second", "الثانية"), ("Hour", "الساعة"), ("Minute", "الدقيقة"), ("Day", "اليوم")], "c"),
 Q("The number of substrate molecules converted per second by a single enzyme molecule is the:", "عدد جزيئات الركيزة المحوَّلة في الثانية بواسطة جزيء إنزيم واحد هو:", [("Specific activity", "الفعالية النوعية"), ("Katal", "الكاتال"), ("International unit", "الوحدة الدولية"), ("Turnover number", "رقم التحوّل")], "d"),
 Q("Specific activity is the number of IU of enzyme present in:", "الفعالية النوعية هي عدد وحدات IU من الإنزيم في:", [("1 mg of protein", "1 ملغم من البروتين"), ("1 L of serum", "1 لتر من المصل"), ("1 mole of substrate", "1 مول من الركيزة"), ("1 cell", "خلية واحدة")], "a"),
 Q("One katal converts:", "الكاتال الواحد يحوّل:", [("One micromole per minute", "مايكرومولًا في الدقيقة"), ("One mole of substrate per second", "مولًا من الركيزة في الثانية"), ("One mg per hour", "ملغم في الساعة"), ("One molecule per second", "جزيئًا في الثانية")], "b"),
 Q("At high temperatures enzyme activity decreases because of:", "تنخفض فعالية الإنزيم في الحرارة العالية بسبب:", [("Increased kinetic energy", "زيادة الطاقة الحركية"), ("Substrate saturation", "تشبّع الركيزة"), ("Denaturation", "المسخ"), ("Cofactor binding", "ارتباط العامل المساعد")], "c"),
 Q("Increasing substrate concentration beyond a certain point does not increase the rate because of:", "زيادة تركيز الركيزة بعد حدّ معيّن لا تزيد السرعة بسبب:", [("Denaturation", "المسخ"), ("Saturation of all binding sites", "تشبّع جميع مواقع الارتباط"), ("Low pH", "انخفاض الـ pH"), ("Enzyme inhibition", "تثبيط الإنزيم")], "b"),
 {"topic_en": "Picture questions", "topic_ar": "أسئلة الصور"},
 Q("The reaction in this figure (fumarate + H2O → L-malate by fumarase) is catalyzed by which class?", "التفاعل في هذا الشكل (الفيوماريت + الماء ← L-malate بالفيوماريز) يحفّزه أي صنف؟", [("Hydrolases", "التحلّل المائي"), ("Ligases", "الرابطة"), ("Isomerases", "المماكبة"), ("Lyases", "المحلِّلة")], "d", img="assets/lyase.jpg", img_h="30mm"),
 Q("The reaction in this figure (pyruvate + CO2 + ATP → oxaloacetate) is catalyzed by a:", "التفاعل في هذا الشكل (البيروفيت + CO2 + ATP ← أوكزالوأسيتيت) يحفّزه:", [("Ligase", "إنزيم رابط"), ("Transferase", "ناقل"), ("Lyase", "محلِّل"), ("Oxidoreductase", "أكسدة واختزال")], "a", img="assets/ligase.jpg", img_h="30mm"),
 Q("This figure illustrates which hypothesis of active site function?", "يوضّح هذا الشكل أي فرضية لعمل الموقع الفعّال؟", [("Induced fit (Koshland)", "التلاؤم المستحث (كوشلاند)"), ("Lock and key (Fischer)", "القفل والمفتاح (فيشر)"), ("Michaelis-Menten", "ميكايلس–منتن"), ("Steady state", "الحالة المستقرة")], "b", img="assets/lock-and-key.jpg", img_h="34mm"),
 Q("In this figure, the falling part of the curve (above ~50 °C) is due to:", "في هذا الشكل، الجزء الهابط من المنحني (فوق نحو 50 °م) سببه:", [("Increased kinetic energy", "زيادة الطاقة الحركية"), ("Substrate saturation", "تشبّع الركيزة"), ("Heat inactivation (denaturation) of enzyme", "التعطيل الحراري (مسخ) الإنزيم"), ("Cofactor loss", "فقدان العامل المساعد")], "c", img="assets/temperature.jpg", img_h="40mm"),
 Q("In this figure, the enzyme with the LOWEST optimum pH is:", "في هذا الشكل، الإنزيم ذو الـ pH الأمثل الأقل هو:", [("Trypsin", "التربسين"), ("Alkaline phosphatase", "الفوسفاتيز القاعدي"), ("All are equal", "جميعها متساوية"), ("Pepsin", "الببسين")], "d", img="assets/ph.jpg", img_h="40mm"),
]

tf = [
 dict(en="Enzymes are consumed during the reactions they catalyze.", ar="تُستهلك الإنزيمات أثناء التفاعلات التي تحفّزها.", answer="F"),
 dict(en="Enzymes function in aqueous solutions under very mild conditions.", ar="تعمل الإنزيمات في المحاليل المائية تحت ظروف معتدلة جدًا.", answer="T"),
 dict(en="Each enzyme has two names: recommended and systematic.", ar="لكل إنزيم اسمان: موصى به ونظامي.", answer="T"),
 dict(en="Trypsin and pepsin are names that clearly indicate the enzyme action.", ar="التربسين والببسين اسمان يدلّان بوضوح على عمل الإنزيم.", answer="F"),
 dict(en="The E.C. code consists of three numbers.", ar="يتكوّن رمز E.C. من ثلاثة أرقام.", answer="F"),
 dict(en="The second E.C. number represents the subclass.", ar="يمثّل الرقم الثاني في E.C. الصنف الفرعي.", answer="T"),
 dict(en="In the induced-fit hypothesis, the active site is complementary to the substrate only after the substrate is bound.", ar="في فرضية التلاؤم المستحث يصبح الموقع الفعّال مكمّلًا للركيزة فقط بعد ارتباطها.", answer="T"),
 dict(en="Trypsin shows absolute specificity.", ar="يُظهر التربسين تخصّصًا مطلقًا.", answer="F"),
 dict(en="Enzymes can be activated or inhibited according to the needs of the cell.", ar="يمكن تنشيط الإنزيمات أو تثبيطها وفق حاجات الخلية.", answer="T"),
 dict(en="Coenzymes bind tightly and never dissociate from the enzyme.", ar="ترتبط المرافقات الإنزيمية بإحكام ولا تنفصل أبدًا عن الإنزيم.", answer="F"),
 dict(en="The apoenzyme alone typically shows no biologic activity.", ar="لا يُظهر الأبوإنزيم وحده عادةً فعالية حيوية.", answer="T"),
 dict(en="The katal converts one micromole of substrate per minute.", ar="يحوّل الكاتال مايكرومولًا واحدًا من الركيزة في الدقيقة.", answer="F"),
 dict(en="All enzymes have the same optimum pH.", ar="لجميع الإنزيمات الـ pH الأمثل نفسه.", answer="F"),
 dict(en="Enzyme reaction rate increases with substrate concentration until a maximal velocity is reached.", ar="تزداد سرعة التفاعل الإنزيمي بزيادة تركيز الركيزة حتى تُبلَغ السرعة القصوى.", answer="T"),
]

traps = [
 dict(en="Fischer vs Koshland", ar="فيشر مقابل كوشلاند", answer_en="Fischer: lock and key (rigid complementary shape). Koshland: induced fit (enzyme changes shape after binding).", answer_ar="فيشر: القفل والمفتاح (شكل مكمّل ثابت). كوشلاند: التلاؤم المستحث (يتغيّر شكل الإنزيم بعد الارتباط)."),
 dict(en="Absolute vs group specificity", ar="التخصّص المطلق مقابل المجموعي", answer_en="Absolute: one substrate (urease → urea). Group: a type of bond/group (trypsin → peptide bonds after lysine and arginine).", answer_ar="المطلق: ركيزة واحدة (اليوريز ← اليوريا). المجموعي: نوع من الأواصر/المجاميع (التربسين ← الأواصر الببتيدية بعد اللايسين والأرجنين)."),
 dict(en="Coenzyme vs prosthetic group", ar="المرافق الإنزيمي مقابل المجموعة الملحقة", answer_en="Coenzyme: weakly bound vitamin derivative (NAD+, FAD, CoA). Prosthetic group: tightly bound, does not dissociate (biotin).", answer_ar="المرافق: مشتقّ فيتامين مرتبط بضعف (NAD+، FAD، CoA). المجموعة الملحقة: مرتبطة بإحكام ولا تنفصل (البايوتين)."),
 dict(en="Holoenzyme vs apoenzyme", ar="الإنزيم الكامل مقابل الأبوإنزيم", answer_en="Holoenzyme = apoenzyme (protein part) + cofactor. The apoenzyme alone is usually inactive.", answer_ar="الإنزيم الكامل = الأبوإنزيم (الجزء البروتيني) + العامل المساعد. والأبوإنزيم وحده غير فعّال عادةً."),
 dict(en="IU vs katal", ar="الوحدة الدولية مقابل الكاتال", answer_en="IU: 1 µmol substrate per minute. Katal: 1 mol substrate per second (1 kat = 6 × 10⁷ U).", answer_ar="IU: مايكرومول من الركيزة في الدقيقة. الكاتال: مول في الثانية (1 kat = 6 × 10⁷ U)."),
 dict(en="Turnover number vs specific activity", ar="رقم التحوّل مقابل الفعالية النوعية", answer_en="Turnover number: molecules converted per second by ONE enzyme molecule. Specific activity: IU per 1 mg of protein.", answer_ar="رقم التحوّل: الجزيئات المحوَّلة في الثانية بجزيء إنزيم واحد. الفعالية النوعية: وحدات IU لكل 1 ملغم بروتين."),
 dict(en="Why activity falls at high temperature", ar="لماذا تنخفض الفعالية في الحرارة العالية", answer_en="Denaturation of the enzyme — not a lack of kinetic energy (kinetic energy explains the rising part).", answer_ar="بسبب مسخ الإنزيم — لا نقص الطاقة الحركية (الطاقة الحركية تفسّر الجزء الصاعد)."),
]

important = [
 dict(en="Define enzymes and list how they differ from chemical catalysts.", ar="عرّف الإنزيمات واذكر كيف تختلف عن المحفّزات الكيميائية.", answer_en="Protein catalysts (occasionally RNA ribozymes) that increase the rate of reactions without being consumed. They differ by: high specificity (no side reactions or by-products), tremendous acceleration, and working in aqueous solutions under mild pressure, temperature and pH.", answer_ar="محفّزات بروتينية (وأحيانًا RNA رايبوزايمات) تزيد سرعة التفاعلات دون أن تُستهلك. وتختلف بـ: التخصّص العالي (لا تفاعلات جانبية ولا نواتج ثانوية)، والتسريع الهائل، والعمل في محاليل مائية تحت ظروف معتدلة من الضغط والحرارة والـ pH."),
 dict(en="Explain the systematic naming of enzymes (IUBMB).", ar="اشرح التسمية النظامية للإنزيمات (IUBMB).", answer_en="(1) Six major classes, each with subclasses and sub-subclasses; (2) name of two parts: substrate(s) + nature of reaction ending in -ase; (3) extra information in parentheses, e.g. L-Malate: NAD oxidoreductase (decarboxylating); (4) a four-number E.C. code.", answer_ar="(1) ستة أصناف رئيسة لكل منها أصناف فرعية وفرعية ثانوية؛ (2) اسم من جزأين: الركيزة + طبيعة التفاعل منتهيًا بـ -ase؛ (3) المعلومات الإضافية بين قوسين، مثل L-Malate: NAD oxidoreductase (decarboxylating)؛ (4) رمز E.C. من أربعة أرقام."),
 dict(en="What do the four numbers of the E.C. code represent?", ar="ماذا تمثّل الأرقام الأربعة في رمز E.C.؟", answer_en="1st: major class (nature of reaction); 2nd: subclass (group or bond); 3rd: sub-subclass (e.g. electron acceptor); 4th: serial listing, given randomly.", answer_ar="الأول: الصنف الرئيس (طبيعة التفاعل)؛ الثاني: الصنف الفرعي (المجموعة أو الآصرة)؛ الثالث: الصنف الفرعي الثانوي (مثل مستقبل الإلكترونات)؛ الرابع: الترتيب التسلسلي ويُعطى عشوائيًا."),
 dict(en="List the six major classes of enzymes with an example of each.", ar="عدّد الأصناف الستة للإنزيمات مع مثال لكل منها.", answer_en="Oxidoreductases (lactate dehydrogenase), transferases (hexokinase), hydrolases (maltase), lyases (fumarase), isomerases (phosphoglyceromutase), ligases (pyruvate carboxylase).", answer_ar="الأكسدة والاختزال (لاكتيت ديهيدروجينيز)، الناقلة (الهكسوكاينيز)، التحلّل المائي (المالتيز)، المحلِّلة (الفيوماريز)، المماكبة (الفوسفوكليسيروميوتيز)، الرابطة (بيروفيت كاربوكسيليز)."),
 dict(en="Compare the lock and key and induced-fit hypotheses.", ar="قارن بين فرضيتي القفل والمفتاح والتلاؤم المستحث.", answer_en="Lock and key (Fischer): the active site is complementary in shape to the substrate. Induced fit (Koshland): the enzyme changes shape on binding; the active site becomes complementary only after the substrate is bound.", answer_ar="القفل والمفتاح (فيشر): الموقع الفعّال مكمّل لشكل الركيزة. التلاؤم المستحث (كوشلاند): يتغيّر شكل الإنزيم عند الارتباط، ويصبح الموقع الفعّال مكمّلًا فقط بعد ارتباط الركيزة."),
 dict(en="Classify enzyme cofactors and give the roles of metal ions.", ar="صنّف العوامل المساعدة للإنزيمات واذكر أدوار الأيونات الفلزية.", answer_en="Organic molecules: coenzymes (vitamin derivatives, weakly bound: NAD+ niacin, FAD riboflavin, CoA pantothenic acid) and prosthetic groups (tightly bound: biotin). Metal ions (Zn+2, Fe+2): essential components of the active site; a bridge linking substrate to enzyme; stabilize the enzyme conformation.", answer_ar="جزيئات عضوية: المرافقات (مشتقّات فيتامينات مرتبطة بضعف: NAD+ نياسين، FAD رايبوفلافين، CoA حمض البانتوثينيك) والمجاميع الملحقة (مرتبطة بإحكام: البايوتين). أيونات فلزية (Zn+2، Fe+2): مكوّنات أساسية في الموقع الفعّال؛ جسر يربط الركيزة بالإنزيم؛ تثبيت الشكل الفراغي للإنزيم."),
 dict(en="Define the enzyme units.", ar="عرّف وحدات الإنزيم.", answer_en="IU: enzyme converting 1 µmol substrate/min under optimum conditions. Turnover number: substrate molecules converted per second by one enzyme molecule. Specific activity: IU per mg protein. Katal: converts 1 mol substrate/second (1 kat = 6 × 10⁷ U).", answer_ar="IU: إنزيم يحوّل 1 مايكرومول ركيزة/دقيقة تحت الظروف المثلى. رقم التحوّل: جزيئات الركيزة المحوَّلة في الثانية بجزيء إنزيم واحد. الفعالية النوعية: IU لكل ملغم بروتين. الكاتال: يحوّل 1 مول/ثانية (1 kat = 6 × 10⁷ U)."),
 dict(en="Explain the effect of temperature and pH on enzyme activity.", ar="اشرح تأثير الحرارة والـ pH في فعالية الإنزيم.", answer_en="Temperature: rate rises to a limited degree (more kinetic energy) then falls (denaturation). pH: each enzyme has an optimum pH; activity falls on both sides because of denaturation and because the needed ionized/non-ionized chemical groups exist only in a limited pH range.", answer_ar="الحرارة: تزداد السرعة إلى حدّ معيّن (طاقة حركية أكبر) ثم تنخفض (المسخ). الـ pH: لكل إنزيم pH أمثل؛ وتنخفض الفعالية على الجانبين بسبب المسخ ولأن المجاميع الكيميائية المتأيّنة/غير المتأيّنة اللازمة لا توجد إلا ضمن مدى محدود من الـ pH."),
]

data = {"meta": {
  "subject_en": "Clinical Enzymology", "subject_ar": "الإنزيمات السريرية", "short_ar": "انزيمات سريرية",
  "unit_en": "Lecture 1", "unit_ar": "المحاضرة 1", "unit_label": "LEC", "unit_no": "1",
  "title_en": "Introduction to Enzymes", "title_ar": "مقدمة في الإنزيمات",
  "kind": "Theory — نظري", "stage": "The fourth stage — الرابعة", "instructor": "د. وليد مجيد"},
 "blocks": blocks, "questions": {"mcq": mcq, "tf": tf, "traps": traps, "important": important}}
qs = [q for q in mcq if "answer" in q]
print(len(qs), Counter(q["answer"] for q in qs))
json.dump(data, open("/home/user/-/enzymology-lec1-introduction/lecture.json", "w"), ensure_ascii=False, indent=1)

```
