---
source: BIOS-Obsidian/tools/scripts/n2/make2.py
handouts: [enzymology-lec2-kinetics-inhibition]
saved: 2026-10-29
tags: [bios, code]
---
# n2/make2.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#enzymology-lec2-kinetics-inhibition|enzymology-lec2-kinetics-inhibition]]

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
 SEC("Michaelis-Menten equation", "معادلة ميكايلس–منتن"),
 H2("1. Reaction model", "1. نموذج التفاعل"),
 C(["**Michaelis and Menten** proposed a simple model that explains for most of the features of enzyme-catalyzed reactions.",
    "In this model, the enzyme **E** reversibly combines with its substrate **S** to form an **ES complex** that subsequently breaks down to product **P**, regenerating the free enzyme."],
   ["اقترح **ميكايلس ومنتن** نموذجًا بسيطًا يفسّر معظم خصائص التفاعلات المحفَّزة إنزيميًا.",
    "في هذا النموذج يتّحد الإنزيم **`E`** اتحادًا عكسيًا مع ركيزته **`S`** ليكوّن **المعقّد `ES`**، الذي يتفكّك بعد ذلك إلى الناتج **`P`** مع إعادة تكوين الإنزيم الحر."]),
 C("The model, involving one substrate molecule, is represented below:", "ويُمثَّل النموذج، الذي يتضمّن جزيء ركيزة واحدًا، كما يأتي:"),
 EQ("mm-model.jpg", "30mm"),
 C("Where: **k1, k-1 and k2** are **rate constant**.", "حيث: `k1` و`k-1` و`k2` هي **ثوابت السرعة**."),

 H2("2. Deriving the Michaelis-Menten equation", "2. اشتقاق معادلة ميكايلس–منتن"),
 C("The Michaelis-Menten equation describes **how reaction velocity varies with substrate concentration**:",
   "تصف معادلة ميكايلس–منتن **كيف تتغيّر سرعة التفاعل مع تركيز الركيزة**:"),
 EQ("mm-equation.jpg", "20mm"),
 C("When **V0** is plotted against **[S]** in Michaelis-Menten equation, it is give a **hyperbolic curve** as shown in the figure below.",
   "عند رسم `V0` مقابل `[S]` في معادلة ميكايلس–منتن نحصل على **منحنٍ زائدي** كما في الشكل أدناه."),
 F("mm-curve.jpg", "Michaelis-Menten hyperbolic curve: initial velocity V0 against substrate concentration [S]; Km is the [S] at ½Vmax",
   "منحنى ميكايلس–منتن الزائدي: السرعة الابتدائية `V0` مقابل تركيز الركيزة `[S]`؛ و`Km` هو `[S]` عند نصف `Vmax`", h="62mm"),
 C("**The following assumptions are made in deriving the Michaelis-Menten rate equation:**",
   "**تُفترض الافتراضات الآتية عند اشتقاق معادلة سرعة ميكايلس–منتن:**"),
 G("a. Relative concentrations of E and S", "أ. التراكيز النسبية لـ `E` و`S`",
   "**[S] >> [E]**, so that the percentage of total substrate bound to enzyme at any one time is small.",
   "`[S] >> [E]`، بحيث تكون نسبة الركيزة المرتبطة بالإنزيم من مجمل الركيزة في أي وقت صغيرة."),
 G("b. Steady-state assumption", "ب. افتراض الحالة المستقرة",
   ["**[ES] does not change with the time** (the steady-state assumption), that is mean; the rate of formation of ES is equal to that of the breakdown of ES (E + S and E + P).",
    "In general, an intermediate in a series of reactions is said to be in steady-state when its **rate of synthesis is equal to its rate of degradation**."],
   ["**لا يتغيّر `[ES]` مع الزمن** (افتراض الحالة المستقرة)، أي أن سرعة تكوين `ES` تساوي سرعة تفكّكه (إلى `E + S` و`E + P`).",
    "وبشكل عام، يُقال عن مادة وسطية في سلسلة تفاعلات إنها في حالة مستقرة عندما **تساوي سرعة تخليقها سرعة تحلّلها**."]),
 G("c. Initial velocity", "ج. السرعة الابتدائية",
   ["are used in the analysis of enzyme reactions.", "This means, that the rate of the reaction is measured **as soon as enzyme and substrate are mixed**.",
    "At that time, the concentration of product is very small and, therefore, the **rate of the back reaction from P to S can be ignored**."],
   ["تُستخدم في تحليل التفاعلات الإنزيمية.", "وهذا يعني أن سرعة التفاعل تُقاس **حال مزج الإنزيم والركيزة**.",
    "وفي ذلك الوقت يكون تركيز الناتج صغيرًا جدًا، ولذلك **يمكن إهمال سرعة التفاعل العكسي من `P` إلى `S`**."]),
 G("d. Michaelis constant (Km)", "د. ثابت ميكايلس (`Km`)",
   "The Km constant reflects the **affinity of the enzyme for its substrate**; whenever **Km is small** (k1 is large), that is mean the **bigger tendency** of enzyme binding to substrate and vice versa.",
   "يعكس الثابت `Km` **ألفة الإنزيم لركيزته**؛ فكلما **صغر `Km`** (كبر `k1`) كان **ميل الإنزيم للارتباط بالركيزة أكبر**، والعكس صحيح."),

 H2("e. Relationship between V0, [S] and Km constant", "هـ. العلاقة بين `V0` و`[S]` والثابت `Km`"),
 R("**When Km = [S]**: The Michaelis-Menten equation becomes:", "**عندما `Km = [S]`**: تصبح معادلة ميكايلس–منتن:"),
 EQ("eq-km-equal-s.jpg", "13mm"),
 C(["That is mean the initial velocity it’s a **half of maximum velocity**.", "Usually this value involved inside the cell (**in vivo**)."],
   ["أي أن السرعة الابتدائية تساوي **نصف السرعة القصوى**.", "وعادةً ما تكون هذه القيمة داخل الخلية (**في الجسم الحي** `in vivo`)."]),
 R("**When Km >> [S] (Km ≥ 100[S])**: The [S] in the denominator fraction of Michaelis-Menten equation can be ignored, and the Michaelis-Menten equation becomes:",
   "**عندما `Km >> [S]` (`Km ≥ 100[S]`)**: يمكن إهمال `[S]` في مقام معادلة ميكايلس–منتن، فتصبح المعادلة:"),
 EQ("eq-first-order.jpg", "14mm"),
 C(["Since Km and Vmax are constant amount, the V0 can be considering as a **function for substrate**, on the other word, the cell be **sensitive** for any changing in the substrate concentration.",
    "So the rate of the reaction is then said to be **first order** with respect to substrate."],
   ["وبما أن `Km` و`Vmax` مقداران ثابتان، يمكن عدّ `V0` **دالة للركيزة**؛ بعبارة أخرى، تكون الخلية **حسّاسة** لأي تغيّر في تركيز الركيزة.",
    "ولذلك يُقال إن سرعة التفاعل **من الرتبة الأولى** بالنسبة للركيزة."]),
 R("**When Km << [S] (100 Km ≤ [S])**: The Km in the denominator fraction of Michaelis-Menten equation can be ignored, and the Michaelis-Menten equation becomes:",
   "**عندما `Km << [S]` (`100 Km ≤ [S]`)**: يمكن إهمال `Km` في مقام معادلة ميكايلس–منتن، فتصبح المعادلة:"),
 EQ("eq-zero-order.jpg", "13mm"),
 C(["The cell is **not sensitive** for any changing in the substrate concentration.", "So the rate of the reaction is then said to be **zero order** with respect to substrate."],
   ["لا تكون الخلية **حسّاسة** لأي تغيّر في تركيز الركيزة.", "ولذلك يُقال إن سرعة التفاعل **من الرتبة صفر** بالنسبة للركيزة."]),

 SEC("Lineweaver-Burke plot", "مخطط لاينويفر–بيرك"),
 C(["When V0 is plotted against [S] in Michaelis-Menten equation, it is give a hyperbolic curve.", "So it is **not always possible to determine Km precisely**."],
   ["عند رسم `V0` مقابل `[S]` في معادلة ميكايلس–منتن نحصل على منحنٍ زائدي.", "ولذلك **لا يمكن دائمًا تحديد `Km` بدقة**."]),
 C(["Because of the important Km constant, it is necessary to determine it in precisely and convenient way.",
    "Both two scientist **Lineweaver and Burke** converted the Michaelis-Menten equation by **take the reciprocal** of this equation to obtain the **strait linear equation** as shown in the figure below."],
   ["ونظرًا لأهمية الثابت `Km`، من الضروري تحديده بطريقة دقيقة ومناسبة.",
    "فحوّل العالمان **لاينويفر وبيرك** معادلة ميكايلس–منتن **بأخذ مقلوبها** للحصول على **معادلة خط مستقيم** كما في الشكل أدناه."]),
 EQ("lb-equation.jpg", "18mm"),
 F("lb-plot.jpg", "Lineweaver-Burke plot: y-intercept = 1/Vmax, x-intercept = −1/Km, slope = Km/Vmax",
   "مخطط لاينويفر–بيرك: المقطع الصادي = `1/Vmax`، والمقطع السيني = `−1/Km`، والميل = `Km/Vmax`", h="62mm"),
 N("This plot, the **Lineweaver-Burke plot** (also called a **double-reciprocal plot**).", "هذا المخطط هو **مخطط لاينويفر–بيرك** (ويُسمّى أيضًا **مخطط المقلوب المزدوج**).", label=["Name", "التسمية"]),

 SEC("Enzyme inhibitors", "مثبّطات الإنزيمات"),
 G("a. Inhibitors", "أ. المثبّطات",
   "Substances (compounds or ions) making the enzyme **inactive** by interfering with its **ability to react with a substrate** slowing the velocity of enzyme reaction.",
   "مواد (مركّبات أو أيونات) تجعل الإنزيم **غير فعّال** بالتداخل مع **قدرته على التفاعل مع الركيزة**، فتُبطئ سرعة التفاعل الإنزيمي."),
 C("**b. Enzyme inhibitors advantages:** The study of the effect of inhibitors very useful to give:", "**ب. فوائد مثبّطات الإنزيمات:** دراسة تأثير المثبّطات مفيدة جدًا لإعطاء:",
   list_en=["Information of the active site of enzyme.", "Mechanism of action.", "Possible regulation of physiological significance."],
   list_ar=["معلومات عن الموقع الفعّال للإنزيم.", "آلية العمل.", "التنظيم المحتمل ذي الأهمية الفسيولوجية."]),
 C("**c. Inhibitors effects:** Inhibitors effect on one or more of the following factors:", "**ج. تأثيرات المثبّطات:** تؤثّر المثبّطات في واحد أو أكثر من العوامل الآتية:",
   list_en=["The active site of enzyme.", "The protein part of enzyme (Apoenzyme).", "Effect on coenzyme.", "The prosthetic group."],
   list_ar=["الموقع الفعّال للإنزيم.", "الجزء البروتيني للإنزيم (الأبوإنزيم).", "التأثير في المرافق الإنزيمي.", "المجموعة الملحقة."]),
 C("**d. Classification of Inhibition:**", "**د. تصنيف التثبيط:**",
   list_en=["Reversible inhibition:", "Irreversible inhibition:"], list_ar=["التثبيط العكسي:", "التثبيط غير العكسي:"]),
 G("Reversible inhibition", "التثبيط العكسي",
   ["interact with the enzyme through **noncovalent** association/dissociation reactions.",
    "This means that the enzyme **regains activity when the inhibitor dissociates** from the enzyme that occurs with dilution ES complex.",
    "There are three types of reversible inhibition:"],
   ["يتفاعل مع الإنزيم عبر تفاعلات ارتباط/انفصال **غير تساهمية**.",
    "وهذا يعني أن الإنزيم **يستعيد فعاليته عندما ينفصل المثبّط** عنه، وهو ما يحدث بتخفيف المعقّد `ES`.",
    "وهناك ثلاثة أنواع من التثبيط العكسي:"]),

 SEC("a. Competitive Inhibition", "أ. التثبيط التنافسي"),
 C(["It is a **competitive between the inhibitor (I) and the substrate (S) for binding to active site** of enzyme.",
    "The inhibitor may be **substrate derivative** or **basically exist in the cell** or **other substrate** or as a **result of reaction product**."],
   ["هو **تنافس بين المثبّط (`I`) والركيزة (`S`) على الارتباط بالموقع الفعّال** للإنزيم.",
    "وقد يكون المثبّط **مشتقًا من الركيزة**، أو **موجودًا أصلًا في الخلية**، أو **ركيزة أخرى**، أو **ناتجًا عن التفاعل**."]),
 C("The general equation can be represented as follow:", "يمكن تمثيل المعادلة العامة كما يأتي:"),
 F("competitive-scheme.jpg", "Competitive inhibition: I and S compete for the free enzyme (EI forms, no product)", "التثبيط التنافسي: يتنافس `I` و`S` على الإنزيم الحر (يتكوّن `EI` بلا ناتج)", h="44mm"),
 C(["Where **KI**, is the **dissociation constant of enzyme inhibitor**.", "After derivative, the equation it can be obtain"],
   ["حيث `KI` هو **ثابت تفكّك معقّد الإنزيم–المثبّط**.", "وبعد الاشتقاق نحصل على المعادلة:"]),
 EQ("competitive-equation.jpg", "16mm"),
 C("When compare equation above with Michaelis-Menten equation it's conclude that:", "عند مقارنة المعادلة أعلاه بمعادلة ميكايلس–منتن نستنتج أن:",
   list_en=["**Vmax=Vmaxi**, and is **unaffected** by I because the entire enzyme is in the complex form.",
            "**Km < Km app**, because Km is multiply by 1+ [I]/ KI It is known whenever the Km value increase the tendency of binding the enzyme to substrate is decrease."],
   list_ar=["`Vmax = Vmaxi`، و**لا يتأثّر** بـ`I` لأن الإنزيم كله يكون بشكل معقّد.",
            "`Km < Km app`، لأن `Km` يُضرب في `1 + [I]/KI`، ومن المعروف أنه كلما زادت قيمة `Km` **قلّ ميل** الإنزيم للارتباط بالركيزة."]),
 C("The relationship between V and S in the presence and absence the inhibitor can be draw as in the figure below:", "يمكن رسم العلاقة بين `V` و`S` بوجود المثبّط وغيابه كما في الشكل أدناه:"),
 F("competitive-curve.jpg", "Competitive inhibition: the same Vmax, an apparent Km greater than Km", "التثبيط التنافسي: `Vmax` نفسه، و`Km` ظاهري أكبر من `Km`", h="56mm"),
 C("The equation can be draw to obtain linear equation of Lineweaver-Burke by taking 1/ V versus 1/S:", "يمكن رسم المعادلة للحصول على معادلة لاينويفر–بيرك الخطية بأخذ `1/V` مقابل `1/S`:"),
 EQ("competitive-lb-equation.jpg", "20mm"),
 F("competitive-lb-plot.jpg", "Competitive inhibition on a Lineweaver-Burke plot: lines meet at 1/Vmax; the slope increases", "التثبيط التنافسي في مخطط لاينويفر–بيرك: تلتقي الخطوط عند `1/Vmax` ويزداد الميل", h="62mm"),
 G("Succinate Dehydrogenase—A Classic Example of Competitive Inhibition", "سكسينيت ديهيدروجينيز — مثال تقليدي على التثبيط التنافسي",
   "The enzyme **succinate dehydrogenase (SDH)** is **competitively inhibited by malonate** as shown in the following equation.",
   "يُثبَّط إنزيم **سكسينيت ديهيدروجينيز** (`SDH`) **تثبيطًا تنافسيًا بالمالونيت** كما في المعادلة الآتية."),
 F("sdh-malonate.jpg", "Succinate → fumarate by succinate dehydrogenase; malonate is a competitive inhibitor", "السكسينيت ← الفيوماريت بإنزيم سكسينيت ديهيدروجينيز؛ والمالونيت مثبّط تنافسي", h="56mm"),

 SEC("b. Uncompetitive inhibition", "ب. التثبيط اللاتنافسي"),
 C(["The inhibitor I bind reversibly with **enzyme-substrate complex ES only**, but **not free enzyme E**.", "The general equation can be represented as follow:"],
   ["يرتبط المثبّط `I` ارتباطًا عكسيًا **بمعقّد الإنزيم–الركيزة `ES` فقط**، و**ليس بالإنزيم الحر `E`**.", "ويمكن تمثيل المعادلة العامة كما يأتي:"]),
 F("uncompetitive-scheme.jpg", "Uncompetitive inhibition: I binds the ES complex to form ESI", "التثبيط اللاتنافسي: يرتبط `I` بالمعقّد `ES` ليكوّن `ESI`", h="44mm"),
 C("After derivative the equation it can be obtain:", "وبعد الاشتقاق نحصل على المعادلة:"),
 EQ("uncompetitive-equation.jpg", "22mm"),
 C("When compare equation above with Michaelis-Menten equation it's conclude that:", "عند مقارنة المعادلة أعلاه بمعادلة ميكايلس–منتن نستنتج أن:",
   list_en=["**Vmax > Vmax I**, because Vmax I is divided on 1+ [I]/ KI .then the result is product decrease.",
            "**Km > Km app** because Km app is divided on 1+ [I]/ KI. Although Km > Km app, but its observe from the general reaction that ES is form by E+S and ESI as a result of high S tendency to binding with E in any form, but this is not mean that the binding is active that observe by binding ES with I."],
   list_ar=["`Vmax > Vmax I`، لأن `Vmax I` يُقسَم على `1 + [I]/KI`، فتكون النتيجة انخفاض الناتج.",
            "`Km > Km app` لأن `Km app` يُقسَم على `1 + [I]/KI`. ومع أن `Km > Km app`، يُلاحظ من التفاعل العام أن `ES` يتكوّن من `E+S` ومن `ESI` نتيجة الميل العالي لـ`S` للارتباط بـ`E` بأي شكل، لكن هذا لا يعني أن الارتباط فعّال، وهو ما يُلاحظ من ارتباط `ES` بـ`I`."]),
 C("The relationship between V and S in the presence and absence the inhibitor can be draw as in the figure below:", "يمكن رسم العلاقة بين `V` و`S` بوجود المثبّط وغيابه كما في الشكل أدناه:"),
 F("uncompetitive-curve.jpg", "Uncompetitive inhibition: both Vmax and Km decrease (Vmax I, Km app)", "التثبيط اللاتنافسي: ينخفض كلٌّ من `Vmax` و`Km` (`Vmax I`، `Km app`)", h="56mm"),
 C("The equation can be draw to obtain linear equation of Lineweaver-Burke by taking 1/ V versus 1/S.", "يمكن رسم المعادلة للحصول على معادلة لاينويفر–بيرك الخطية بأخذ `1/V` مقابل `1/S`."),
 EQ("uncompetitive-lb-equation.jpg", "13mm"),
]

def Q(en, ar, opts, ans, **k):
    return dict(en=en, ar=ar, options=[list(o) for o in opts], answer=ans, **k)

mcq = [
 {"topic_en": "Michaelis-Menten model", "topic_ar": "نموذج ميكايلس–منتن"},
 Q("In the Michaelis-Menten model, the enzyme reversibly combines with substrate to form:", "في نموذج ميكايلس–منتن يتّحد الإنزيم عكسيًا مع الركيزة ليكوّن:", [("EI complex", "المعقّد EI"), ("ES complex", "المعقّد ES"), ("ESI complex", "المعقّد ESI"), ("Product directly", "الناتج مباشرة")], "b"),
 Q("In the model, k1, k-1 and k2 are:", "في النموذج، k1 وk-1 وk2 هي:", [("Rate constants", "ثوابت السرعة"), ("Dissociation constants of inhibitor", "ثوابت تفكّك المثبّط"), ("Concentrations", "تراكيز"), ("Enzyme units", "وحدات إنزيم")], "a"),
 Q("A plot of V0 against [S] gives a:", "رسم V0 مقابل [S] يعطي:", [("Straight line", "خطًا مستقيمًا"), ("Bell-shaped curve", "منحنًى جرسيًا"), ("Hyperbolic curve", "منحنًى زائديًا"), ("Sigmoid curve only", "منحنًى سينيًا فقط")], "c"),
 Q("Which is an assumption in deriving the Michaelis-Menten equation?", "أي مما يأتي من افتراضات اشتقاق معادلة ميكايلس–منتن؟", [("[E] >> [S]", "[E] >> [S]"), ("[S] >> [E]", "[S] >> [E]"), ("[ES] changes rapidly with time", "[ES] يتغيّر بسرعة مع الزمن"), ("The back reaction P → S is large", "التفاعل العكسي P ← S كبير")], "b"),
 Q("The steady-state assumption means that:", "افتراض الحالة المستقرة يعني أن:", [("[S] is constant", "[S] ثابت"), ("[P] is zero", "[P] صفر"), ("Vmax is reached", "تُبلَغ Vmax"), ("[ES] does not change with time", "[ES] لا يتغيّر مع الزمن")], "d"),
 Q("Initial velocities are used because at that time:", "تُستخدم السرعات الابتدائية لأنه في ذلك الوقت:", [("Product concentration is very small, so the back reaction can be ignored", "يكون تركيز الناتج صغيرًا جدًا فيُهمَل التفاعل العكسي"), ("Enzyme is denatured", "يكون الإنزيم ممسوخًا"), ("Substrate is exhausted", "تكون الركيزة قد نفدت"), ("Inhibitor is absent", "يكون المثبّط غائبًا")], "a"),
 Q("A small Km means:", "صغر Km يعني:", [("Low affinity of the enzyme for its substrate", "ألفة منخفضة للإنزيم لركيزته"), ("No binding", "لا ارتباط"), ("High affinity (bigger tendency to bind substrate)", "ألفة عالية (ميل أكبر للارتباط بالركيزة)"), ("High Vmax", "Vmax عالية")], "c"),
 Q("When Km = [S], the initial velocity equals:", "عندما Km = [S] تساوي السرعة الابتدائية:", [("Vmax", "Vmax"), ("2 Vmax", "2 Vmax"), ("Zero", "صفرًا"), ("½ Vmax", "نصف Vmax")], "d"),
 Q("When Km >> [S] (Km ≥ 100[S]), the reaction is:", "عندما Km >> [S] (Km ≥ 100[S]) يكون التفاعل:", [("Zero order", "من الرتبة صفر"), ("First order with respect to substrate", "من الرتبة الأولى بالنسبة للركيزة"), ("Second order", "من الرتبة الثانية"), ("Independent of [S]", "مستقلًا عن [S]")], "b"),
 Q("When Km << [S] (100 Km ≤ [S]), V0 equals:", "عندما Km << [S] (100 Km ≤ [S]) تساوي V0:", [("Vmax", "Vmax"), ("½ Vmax", "نصف Vmax"), ("Vmax[S]/Km", "Vmax[S]/Km"), ("Km/Vmax", "Km/Vmax")], "a"),
 Q("In which condition is the cell NOT sensitive to changes in substrate concentration?", "في أي حالة لا تكون الخلية حسّاسة لتغيّر تركيز الركيزة؟", [("Km >> [S]", "Km >> [S]"), ("Km = [S]", "Km = [S]"), ("Km << [S]", "Km << [S]"), ("[S] = 0", "[S] = 0")], "c"),
 {"topic_en": "Lineweaver-Burke plot", "topic_ar": "مخطط لاينويفر–بيرك"},
 Q("The Lineweaver-Burke plot is obtained by:", "يُحصَل على مخطط لاينويفر–بيرك بـ:", [("Taking the logarithm of the equation", "أخذ لوغاريتم المعادلة"), ("Taking the reciprocal of the Michaelis-Menten equation", "أخذ مقلوب معادلة ميكايلس–منتن"), ("Squaring both sides", "تربيع الطرفين"), ("Plotting V0 against time", "رسم V0 مقابل الزمن")], "b"),
 Q("The Lineweaver-Burke plot is also called:", "يُسمّى مخطط لاينويفر–بيرك أيضًا:", [("Double-reciprocal plot", "مخطط المقلوب المزدوج"), ("Arrhenius plot", "مخطط أرهينيوس"), ("Hill plot", "مخطط هيل"), ("Scatchard plot", "مخطط سكاتشارد")], "a"),
 Q("In the Lineweaver-Burke plot, the slope equals:", "في مخطط لاينويفر–بيرك يساوي الميل:", [("1/Vmax", "1/Vmax"), ("−1/Km", "−1/Km"), ("Vmax/Km", "Vmax/Km"), ("Km/Vmax", "Km/Vmax")], "d"),
 Q("The x-axis intercept of the Lineweaver-Burke plot equals:", "المقطع السيني في مخطط لاينويفر–بيرك يساوي:", [("1/Vmax", "1/Vmax"), ("−1/Km", "−1/Km"), ("Km", "Km"), ("Vmax", "Vmax")], "b"),
 Q("The main reason for using the Lineweaver-Burke plot is that:", "السبب الرئيس لاستخدام مخطط لاينويفر–بيرك هو أن:", [("Km cannot always be determined precisely from the hyperbolic curve", "Km لا يمكن دائمًا تحديده بدقة من المنحني الزائدي"), ("It measures temperature", "يقيس الحرارة"), ("It measures pH", "يقيس الـ pH"), ("It shows enzyme units", "يُظهر وحدات الإنزيم")], "a"),
 {"topic_en": "Enzyme inhibitors", "topic_ar": "مثبّطات الإنزيمات"},
 Q("Studying enzyme inhibitors gives information about all EXCEPT:", "دراسة مثبّطات الإنزيمات تعطي معلومات عن كل مما يأتي عدا:", [("The active site", "الموقع الفعّال"), ("Mechanism of action", "آلية العمل"), ("Physiological regulation", "التنظيم الفسيولوجي"), ("The molecular weight of the substrate", "الوزن الجزيئي للركيزة")], "d"),
 Q("Reversible inhibitors interact with the enzyme through:", "تتفاعل المثبّطات العكسية مع الإنزيم عبر:", [("Covalent bonds", "أواصر تساهمية"), ("Noncovalent association/dissociation", "ارتباط/انفصال غير تساهمي"), ("Peptide bonds", "أواصر ببتيدية"), ("Disulfide bonds", "أواصر ثنائية الكبريت")], "b"),
 Q("In competitive inhibition, the inhibitor competes with the substrate for:", "في التثبيط التنافسي يتنافس المثبّط مع الركيزة على:", [("The ES complex", "المعقّد ES"), ("The coenzyme", "المرافق الإنزيمي"), ("The active site of the enzyme", "الموقع الفعّال للإنزيم"), ("The product", "الناتج")], "c"),
 Q("In competitive inhibition, Vmax:", "في التثبيط التنافسي، Vmax:", [("Is unaffected", "لا تتأثّر"), ("Decreases", "تنخفض"), ("Increases", "تزداد"), ("Becomes zero", "تصبح صفرًا")], "a"),
 Q("In competitive inhibition, the apparent Km:", "في التثبيط التنافسي، Km الظاهري:", [("Decreases", "ينخفض"), ("Is unchanged", "لا يتغيّر"), ("Becomes zero", "يصبح صفرًا"), ("Increases (Km < Km app)", "يزداد (Km < Km app)")], "d"),
 Q("KI is the:", "KI هو:", [("Michaelis constant", "ثابت ميكايلس"), ("Dissociation constant of the enzyme–inhibitor complex", "ثابت تفكّك معقّد الإنزيم–المثبّط"), ("Rate of product formation", "سرعة تكوين الناتج"), ("Turnover number", "رقم التحوّل")], "b"),
 Q("Succinate dehydrogenase is competitively inhibited by:", "يُثبَّط سكسينيت ديهيدروجينيز تنافسيًا بـ:", [("Fumarate", "الفيوماريت"), ("Succinate", "السكسينيت"), ("Malonate", "المالونيت"), ("Malate", "الماليت")], "c"),
 Q("In uncompetitive inhibition, the inhibitor binds:", "في التثبيط اللاتنافسي يرتبط المثبّط بـ:", [("The free enzyme only", "الإنزيم الحر فقط"), ("The ES complex only", "المعقّد ES فقط"), ("The substrate", "الركيزة"), ("The product", "الناتج")], "b"),
 Q("In uncompetitive inhibition:", "في التثبيط اللاتنافسي:", [("Vmax unchanged, Km increases", "Vmax ثابتة وKm يزداد"), ("Vmax increases, Km decreases", "Vmax تزداد وKm ينخفض"), ("Both Vmax and Km decrease", "تنخفض Vmax وKm كلاهما"), ("Both unchanged", "كلاهما ثابت")], "c"),
 Q("On a Lineweaver-Burke plot, competitive inhibition lines intersect at:", "في مخطط لاينويفر–بيرك تتقاطع خطوط التثبيط التنافسي عند:", [("1/Vmax on the y-axis", "1/Vmax على المحور الصادي"), ("−1/Km on the x-axis", "−1/Km على المحور السيني"), ("The origin", "نقطة الأصل"), ("They are parallel", "تكون متوازية")], "a"),
 {"topic_en": "Picture questions", "topic_ar": "أسئلة الصور"},
 Q("In this curve, the point on the [S] axis that gives ½Vmax is:", "في هذا المنحني، النقطة على محور [S] التي تعطي نصف Vmax هي:", [("Vmax", "Vmax"), ("Km", "Km"), ("KI", "KI"), ("k2", "k2")], "b", img="assets/mm-curve.jpg", img_h="44mm"),
 Q("In this plot, the intercept on the y-axis equals:", "في هذا المخطط، المقطع على المحور الصادي يساوي:", [("−1/Km", "−1/Km"), ("Km/Vmax", "Km/Vmax"), ("1/Vmax", "1/Vmax"), ("Km", "Km")], "c", img="assets/lb-plot.jpg", img_h="44mm"),
 Q("The red curve in this figure shows which type of inhibition?", "المنحني الأحمر في هذا الشكل يمثّل أي نوع من التثبيط؟", [("Uncompetitive", "اللاتنافسي"), ("Irreversible", "غير العكسي"), ("No inhibition", "بلا تثبيط"), ("Competitive", "التنافسي")], "d", img="assets/competitive-curve.jpg", img_h="44mm"),
 Q("In this scheme, the inhibitor binds only the ES complex to form ESI. This is:", "في هذا المخطط يرتبط المثبّط بالمعقّد ES فقط ليكوّن ESI. هذا هو:", [("Competitive inhibition", "التثبيط التنافسي"), ("Uncompetitive inhibition", "التثبيط اللاتنافسي"), ("Lineweaver-Burke plot", "مخطط لاينويفر–بيرك"), ("Steady state", "الحالة المستقرة")], "b", img="assets/uncompetitive-scheme.jpg", img_h="36mm"),
 Q("In this figure, malonate inhibits succinate dehydrogenase by:", "في هذا الشكل يثبّط المالونيت سكسينيت ديهيدروجينيز بـ:", [("Competitive inhibition", "التثبيط التنافسي"), ("Uncompetitive inhibition", "التثبيط اللاتنافسي"), ("Denaturation", "المسخ"), ("Covalent binding", "الارتباط التساهمي")], "a", img="assets/sdh-malonate.jpg", img_h="40mm"),
]

tf = [
 dict(en="In the Michaelis-Menten model, the free enzyme is regenerated after product formation.", ar="في نموذج ميكايلس–منتن يُعاد تكوين الإنزيم الحر بعد تكوين الناتج.", answer="T"),
 dict(en="The Michaelis-Menten plot of V0 against [S] is a straight line.", ar="رسم ميكايلس–منتن لـ V0 مقابل [S] خط مستقيم.", answer="F"),
 dict(en="In deriving the equation it is assumed that [S] >> [E].", ar="عند اشتقاق المعادلة يُفترض أن [S] >> [E].", answer="T"),
 dict(en="A large Km means a high affinity of the enzyme for its substrate.", ar="Km الكبير يعني ألفة عالية للإنزيم لركيزته.", answer="F"),
 dict(en="When Km = [S], V0 = ½ Vmax.", ar="عندما Km = [S] تكون V0 = نصف Vmax.", answer="T"),
 dict(en="When Km >> [S], the reaction is zero order with respect to substrate.", ar="عندما Km >> [S] يكون التفاعل من الرتبة صفر بالنسبة للركيزة.", answer="F"),
 dict(en="When Km << [S], V0 ≈ Vmax and the cell is not sensitive to [S].", ar="عندما Km << [S] تكون V0 ≈ Vmax ولا تكون الخلية حسّاسة لـ [S].", answer="T"),
 dict(en="Lineweaver and Burke took the reciprocal of the Michaelis-Menten equation.", ar="أخذ لاينويفر وبيرك مقلوب معادلة ميكايلس–منتن.", answer="T"),
 dict(en="In reversible inhibition, the enzyme regains activity when the inhibitor dissociates.", ar="في التثبيط العكسي يستعيد الإنزيم فعاليته عند انفصال المثبّط.", answer="T"),
 dict(en="Competitive inhibition decreases Vmax.", ar="يُنقص التثبيط التنافسي Vmax.", answer="F"),
 dict(en="A competitive inhibitor may be a substrate derivative or a reaction product.", ar="قد يكون المثبّط التنافسي مشتقًا من الركيزة أو ناتجًا للتفاعل.", answer="T"),
 dict(en="Malonate is a competitive inhibitor of succinate dehydrogenase.", ar="المالونيت مثبّط تنافسي لسكسينيت ديهيدروجينيز.", answer="T"),
 dict(en="An uncompetitive inhibitor binds the free enzyme E.", ar="يرتبط المثبّط اللاتنافسي بالإنزيم الحر E.", answer="F"),
 dict(en="In uncompetitive inhibition, Vmax I is lower than Vmax.", ar="في التثبيط اللاتنافسي تكون Vmax I أقل من Vmax.", answer="T"),
]

traps = [
 dict(en="Small Km = high or low affinity?", ar="Km صغير = ألفة عالية أم منخفضة؟", answer_en="High affinity: a small Km (large k1) means a bigger tendency of the enzyme to bind its substrate.", answer_ar="ألفة عالية: Km الصغير (k1 الكبير) يعني ميلًا أكبر للإنزيم للارتباط بركيزته."),
 dict(en="First order vs zero order", ar="الرتبة الأولى مقابل الرتبة صفر", answer_en="Km >> [S]: V0 = Vmax[S]/Km → first order, the cell is sensitive to [S]. Km << [S]: V0 = Vmax → zero order, not sensitive.", answer_ar="Km >> [S]: V0 = Vmax[S]/Km ← رتبة أولى والخلية حسّاسة لـ [S]. Km << [S]: V0 = Vmax ← رتبة صفر وغير حسّاسة."),
 dict(en="Lineweaver-Burke intercepts", ar="مقاطع مخطط لاينويفر–بيرك", answer_en="y-intercept = 1/Vmax; x-intercept = −1/Km; slope = Km/Vmax.", answer_ar="المقطع الصادي = 1/Vmax؛ المقطع السيني = −1/Km؛ الميل = Km/Vmax."),
 dict(en="Competitive inhibition: what changes?", ar="التثبيط التنافسي: ما الذي يتغيّر؟", answer_en="Vmax is unchanged; apparent Km increases (Km < Km app). On the double-reciprocal plot the lines meet at 1/Vmax and the slope increases.", answer_ar="Vmax ثابتة؛ Km الظاهري يزداد (Km < Km app). وفي مخطط المقلوب المزدوج تلتقي الخطوط عند 1/Vmax ويزداد الميل."),
 dict(en="Uncompetitive inhibition: what changes?", ar="التثبيط اللاتنافسي: ما الذي يتغيّر؟", answer_en="Both decrease: Vmax > Vmax I and Km > Km app (both divided by 1 + [I]/KI).", answer_ar="كلاهما ينخفض: Vmax > Vmax I وKm > Km app (كلاهما يُقسَم على 1 + [I]/KI)."),
 dict(en="Where does each inhibitor bind?", ar="بماذا يرتبط كل مثبّط؟", answer_en="Competitive: the free enzyme's active site (forms EI). Uncompetitive: the ES complex only (forms ESI).", answer_ar="التنافسي: بالموقع الفعّال للإنزيم الحر (يكوّن EI). اللاتنافسي: بالمعقّد ES فقط (يكوّن ESI)."),
 dict(en="Malonate vs fumarate in the SDH reaction", ar="المالونيت مقابل الفيوماريت في تفاعل SDH", answer_en="Succinate → fumarate is the reaction; malonate is the competitive inhibitor.", answer_ar="السكسينيت ← الفيوماريت هو التفاعل؛ والمالونيت هو المثبّط التنافسي."),
]

important = [
 dict(en="Describe the Michaelis-Menten reaction model and equation.", ar="صف نموذج ومعادلة ميكايلس–منتن.", answer_en="E combines reversibly with S to form ES (k1, k-1), which breaks down to P (k2), regenerating free E. V0 = Vmax[S]/(Km + [S]), where V0 = initial velocity, Vmax = maximal velocity, Km = (k-1 + k2)/k1, [S] = substrate concentration. The V0–[S] plot is hyperbolic.", answer_ar="يتّحد E عكسيًا مع S ليكوّن ES (k1، k-1) الذي يتفكّك إلى P (k2) مع إعادة تكوين E الحر. V0 = Vmax[S]/(Km + [S])، حيث V0 السرعة الابتدائية، وVmax السرعة القصوى، وKm = (k-1 + k2)/k1، و[S] تركيز الركيزة. ورسم V0–[S] زائدي."),
 dict(en="List the assumptions made in deriving the Michaelis-Menten equation.", ar="عدّد افتراضات اشتقاق معادلة ميكايلس–منتن.", answer_en="(a) [S] >> [E]; (b) steady state: [ES] does not change with time; (c) initial velocities are used, so the back reaction P → S is ignored; (d) Km reflects the affinity of the enzyme for its substrate.", answer_ar="(أ) [S] >> [E]؛ (ب) الحالة المستقرة: [ES] لا يتغيّر مع الزمن؛ (ج) تُستخدم السرعات الابتدائية فيُهمَل التفاعل العكسي P ← S؛ (د) Km يعكس ألفة الإنزيم لركيزته."),
 dict(en="Explain the relationship between V0, [S] and Km in three cases.", ar="اشرح العلاقة بين V0 و[S] وKm في ثلاث حالات.", answer_en="Km = [S]: V0 = ½Vmax (in vivo). Km >> [S]: V0 = Vmax[S]/Km — first order, the cell is sensitive to [S]. Km << [S]: V0 = Vmax — zero order, not sensitive.", answer_ar="Km = [S]: V0 = نصف Vmax (في الجسم الحي). Km >> [S]: V0 = Vmax[S]/Km — رتبة أولى والخلية حسّاسة لـ [S]. Km << [S]: V0 = Vmax — رتبة صفر وغير حسّاسة."),
 dict(en="Why is the Lineweaver-Burke plot used? Give its equation.", ar="لماذا يُستخدم مخطط لاينويفر–بيرك؟ اكتب معادلته.", answer_en="The hyperbolic curve does not always allow precise Km determination; taking the reciprocal gives a straight line: 1/V0 = (Km/Vmax)(1/[S]) + 1/Vmax (double-reciprocal plot).", answer_ar="لأن المنحني الزائدي لا يسمح دائمًا بتحديد Km بدقة؛ وأخذ المقلوب يعطي خطًا مستقيمًا: 1/V0 = (Km/Vmax)(1/[S]) + 1/Vmax (مخطط المقلوب المزدوج)."),
 dict(en="Define enzyme inhibitors and give the advantages of studying them.", ar="عرّف مثبّطات الإنزيمات واذكر فوائد دراستها.", answer_en="Substances (compounds or ions) making the enzyme inactive by interfering with its ability to react with a substrate. Their study gives information on the active site, the mechanism of action, and possible physiological regulation.", answer_ar="مواد (مركّبات أو أيونات) تجعل الإنزيم غير فعّال بالتداخل مع قدرته على التفاعل مع الركيزة. ودراستها تعطي معلومات عن الموقع الفعّال، وآلية العمل، والتنظيم الفسيولوجي المحتمل."),
 dict(en="Compare competitive and uncompetitive inhibition.", ar="قارن بين التثبيط التنافسي واللاتنافسي.", answer_en="Competitive: I competes with S for the active site of free E; Vmax unchanged; Km app increased; LB lines meet at 1/Vmax. Uncompetitive: I binds ES only; Vmax and Km both decrease (divided by 1 + [I]/KI).", answer_ar="التنافسي: يتنافس I مع S على الموقع الفعّال للإنزيم الحر؛ Vmax ثابتة؛ Km الظاهري يزداد؛ وتلتقي خطوط LB عند 1/Vmax. اللاتنافسي: يرتبط I بـ ES فقط؛ وتنخفض Vmax وKm كلاهما (يُقسَمان على 1 + [I]/KI)."),
 dict(en="Give a classic example of competitive inhibition.", ar="اذكر مثالًا تقليديًا على التثبيط التنافسي.", answer_en="Succinate dehydrogenase (succinate → fumarate) is competitively inhibited by malonate.", answer_ar="يُثبَّط سكسينيت ديهيدروجينيز (السكسينيت ← الفيوماريت) تنافسيًا بالمالونيت."),
]

data = {"meta": {
  "subject_en": "Clinical Enzymology", "subject_ar": "الإنزيمات السريرية", "short_ar": "انزيمات سريرية",
  "unit_en": "Lecture 2", "unit_ar": "المحاضرة 2", "unit_label": "LEC", "unit_no": "2",
  "title_en": "Enzyme Kinetics and Inhibition", "title_ar": "حركيات الإنزيمات وتثبيطها",
  "kind": "Theory — نظري", "stage": "The fourth stage — الرابعة", "instructor": "د. حسين محمود"},
 "blocks": blocks, "questions": {"mcq": mcq, "tf": tf, "traps": traps, "important": important}}
qs = [q for q in mcq if "answer" in q]
print(len(qs), Counter(q["answer"] for q in qs))
json.dump(data, open("/home/user/-/enzymology-lec2-kinetics-inhibition/lecture.json", "w"), ensure_ascii=False, indent=1)

```
