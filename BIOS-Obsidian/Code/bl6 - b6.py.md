---
source: BIOS-Obsidian/tools/scripts/bl6/b6.py
handouts: [bacteriology-lab6-biochemical-tests]
saved: 2026-11-11
tags: [bios, code]
---
# bl6/b6.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#bacteriology-lab6-biochemical-tests|bacteriology-lab6-biochemical-tests]]

```python
import sys; sys.path.insert(0, "/tmp/claude-0/-home-user--/67d83c9a-7b0e-5ae5-b52b-cd659ab074ab/scratchpad/imm456")
from ci import *            # c helpers + B INSHORT TERMS balance save(split.fix)
sys.path.insert(0, "/tmp/claude-0/-home-user--/67d83c9a-7b0e-5ae5-b52b-cd659ab074ab/scratchpad"); from bidi import ltr_all; from flowfit import fit

# Diagnostic Microbiology practical, lab 6 — "Biochemical Testing of Microorganisms" (20 slides, 11 pictures, no questions;
# prepared by MSc. Hiba sami · MSc. Ali Thamar). Fourth stage → separate question file.
split.ABBR = split.ABBR + ("MSc.", "spp.", "Staph.")
BN = lambda en, ar: N(en, ar, label=["BIOS note", "ملاحظة BIOS"])
O = P
EQ = lambda src, h="14mm": dict(t="eq", src="assets/" + src, h=h)
def RES(en_lines, ar_lines):
    """result lines (\"X ……. Positive.\") in a one-column table: a cell is never cut into sentences."""
    return T([B("Result", "النتيجة")], [[B(e, a)] for e, a in zip(en_lines, ar_lines)], widths=[100], key_cols=[0])

blocks = [
 # ───────────────────────── 0
 SEC("Biochemical tests", "الفحوص الكيميائية الحيوية"),
 N("Prepared by MSc. Hiba sami · MSc. Ali Thamar", "إعداد: م. هبة سامي · م. علي ثامر", label=["Lab sheet", "ورقة العملي"]),
 C("Because there are many species of bacteria having **similar shape and size**, so we need **biochemical tests** that used for the identification of bacteria species based on the **differences in the biochemical activities**.",
   "لأن أنواعًا كثيرة من البكتيريا لها **شكل وحجم متشابهان**، نحتاج إلى **فحوص كيميائية حيوية** تُستعمل لتشخيص أنواع البكتيريا على أساس **الاختلاف في نشاطاتها الكيميائية الحيوية**."),

 # ───────────────────────── 1 catalase
 SEC("Catalase test", "فحص الكاتاليز"),
 H2("1. Catalase Test:", "1. فحص الكاتاليز:"),
 C("This test is used to identify organisms that produce the enzyme **catalase** breaking **hydrogen peroxide** into **water and oxygen gas** clearly indicate a positive result.",
   "يُستعمل هذا الفحص لتشخيص الكائنات التي تنتج إنزيم **الكاتاليز** الذي يحلّل **بيروكسيد الهيدروجين** إلى **ماء وغاز الأوكسجين**، وهذا يدلّ بوضوح على نتيجة موجبة."),
 EQ("catalase-equation.png", "13mm"),
 L(["transfer bacterial colony by **wooden stick** on the slide.", "then add a **drop of hydrogen peroxide** on them.", "note whether or not **bubbles** from."],
   ["انقل مستعمرة بكتيرية بـ**عود خشبي** إلى الشريحة.", "ثم أضف **قطرة من بيروكسيد الهيدروجين** عليها.", "لاحظ هل تتكوّن **فقاعات** أم لا."],
   en=["**Procedure:**", "The catalase test it done by:"], ar=["**الطريقة:**", "يُجرى فحص الكاتاليز بـ:"]),
 RES(["The __Staphylococcus__ …… **Positive.**", "The __Streptococcus__ ……. **Negative.**"],
   ["`__Staphylococcus__` …… **موجبة.**", "`__Streptococcus__` ……. **سالبة.**"]),
 F("catalase-test.png", "Figure ( 1 ): Catalase test (HYDROGEN PEROXIDE — bubbles on the slide)", "الشكل (1): فحص الكاتاليز (بيروكسيد الهيدروجين — فقاعات على الشريحة)", h="48mm"),
 BN("Use a **wooden stick** (not a metal loop) — iron in a loop can split H₂O₂ and give a false positive.",
    "استعمل **عودًا خشبيًا** (لا عروة معدنية) — لأن الحديد في العروة قد يحلّل `H₂O₂` فيعطي نتيجة موجبة كاذبة."),

 # ───────────────────────── 2 indole
 SEC("Indole test", "فحص الإندول"),
 H2("2- Indole Test:", "2. فحص الإندول:"),
 C(["Is used to determine the ability of the organism to **convert tryptophan into indole**.", "Pyruvic acid and ammonia by **tryptophanase enzyme**.",
    "The presence of indole is detected by addition of **kovac’s reagent**.",
    "kovac’s reagent reacts with the indole, producing a **bright red compound** on the surface of the medium."],
   ["يُستعمل لتحديد قدرة الكائن على **تحويل التربتوفان إلى إندول**.", "وحامض البايروفيك والأمونيا بإنزيم **التربتوفانيز**.",
    "ويُكشف وجود الإندول بإضافة **كاشف كوفاكس**.",
    "ويتفاعل كاشف كوفاكس مع الإندول فينتج **مركّبًا أحمر لامعًا** على سطح الوسط."]),
 F("indole-reaction.png", "Tryptophane amino acids → (Tryptophanase) → Indole + Pyurvic acid + NH3 → Kovac's Reagent → Red color in upper organic layer",
   "الحامض الأميني تربتوفان ← (تربتوفانيز) ← إندول + حامض البايروفيك + `NH3` ← كاشف كوفاكس ← لون أحمر في الطبقة العضوية العليا", h="34mm"),
 L(["Inoculate **peptone water** (is a rich tryptophan) with young bacterial culture.", "incubate **at 37C for 24** hours.", "Add **5 drop of kovac’s reagent** to the broth culture.", "Observe for the presence or absence of **red ring**."],
   ["لقّح **ماء الببتون** (الغني بالتربتوفان) بمزرعة بكتيرية فتية.", "احضن **عند 37°م لمدة 24** ساعة.", "أضف **5 قطرات من كاشف كوفاكس** إلى المزرعة السائلة.", "لاحظ وجود **الحلقة الحمراء** أو غيابها."],
   en="**Procedure:**", ar="**الطريقة:**"),
 RES(["**Positive** ……. __E.coli__.", "**Negative** ……… __Pseudomonas aeruginosa__"], ["**موجب** ……. `__E.coli__`.", "**سالب** ……… `__Pseudomonas aeruginosa__`"]),
 F("indole-tubes.png", "Indole test: red (pink) ring on top = positive (left); no ring = negative (right)", "فحص الإندول: حلقة حمراء (وردية) في الأعلى = موجب (يسار)؛ لا حلقة = سالب (يمين)", h="34mm"),

 # ───────────────────────── 3 coagulase
 SEC("Coagulase test", "فحص التخثّر"),
 H2("3- Coagulase test:", "3. فحص التخثّر (الكواغيوليز):"),
 C("**Coagulase** is an enzyme that **clots plasma**.", "**الكواغيوليز** إنزيم **يُخثّر البلازما**."),
 F("coagulase-reaction.png", "Fibrinogen (Plasma) → Coagulase → Fibrin (Clot)", "الفايبرينوجين (البلازما) ← الكواغيوليز ← الفايبرين (الخثرة)", h="26mm"),
 L(["Place a drop of **distilled water** on a glass slide.", "With a wooden stick, transfer a colony of bacteria and mix it with a drop of water.", "Add a drop of **blood plasma** to the suspension and mix well."],
   ["ضع قطرة من **الماء المقطّر** على شريحة زجاجية.", "انقل بعود خشبي مستعمرة بكتيرية وامزجها بقطرة الماء.", "أضف قطرة من **بلازما الدم** إلى المعلّق وامزج جيدًا."],
   en=["**Procedure:**", "This test is done by **tube coagulase method** or **slid coagulase method**:"],
   ar=["**الطريقة:**", "يُجرى هذا الفحص بـ**طريقة الأنبوب** أو **طريقة الشريحة**:"]),
 RES(["**Agglutination**….. **Positive** like __Staph. Aureus__", "**No agglutination** …… **Negative** like other staphylococcus."],
   ["**تلازن (تكتّل)**….. **موجب** مثل العنقودية الذهبية", "**لا تلازن** …… **سالب** مثل العنقوديات الأخرى."]),
 F("coagulase-slide-tube.png", "Figure ( 1 ): slide coagulase method (clumps = + test, smooth = – test); Figure ( 2 ): tube coagulase method (clot)",
   "الشكل (1): طريقة الشريحة (تكتّلات = موجب، متجانس = سالب)؛ الشكل (2): طريقة الأنبوب (خثرة)", h="52mm"),
 BN("The steps written here are the **slide** method. In the **tube** method the colony is mixed with plasma in a tube and incubated at 37°C (up to 4 h) — a **clot** = positive.",
    "الخطوات المكتوبة هنا لـ**طريقة الشريحة**. وفي **طريقة الأنبوب** تُمزج المستعمرة مع البلازما في أنبوب وتُحضن عند 37°م (حتى 4 ساعات) — و**الخثرة** = موجب."),

 # ───────────────────────── 4 MR
 SEC("Methyl red test", "فحص أحمر المثيل"),
 H2("4- Methyl red test (MR):", "4. فحص أحمر المثيل (MR):"),
 L(["the ability of bacteria to **oxidize glucose** and produce **high concentration of acidic end products**, the acid so produced **decreases the PH 4.5 or below**, which is indicated by a change in the color of methyl red from **yellow to red**.",
    "and to distinguish between the bacterial species that oxidize glucose, some bacterial species have special enzymes that **convert the final acids into neutral substances** and reduce the acidity of the medium (**raise the PH**)."],
   ["قدرة البكتيريا على **أكسدة الكلوكوز** وإنتاج **تركيز عالٍ من النواتج النهائية الحامضية**، فيخفض الحامض الناتج **الأس الهيدروجيني إلى 4.5 أو أقل**، ويُستدلّ على ذلك بتغيّر لون أحمر المثيل من **الأصفر إلى الأحمر**.",
    "وللتفريق بين أنواع البكتيريا التي تؤكسد الكلوكوز، إذ تمتلك بعض الأنواع إنزيمات خاصة **تحوّل الحوامض النهائية إلى مواد متعادلة** وتقلّل حموضة الوسط (**ترفع الأس الهيدروجيني**)."],
   en="This test is used to determine:", ar="يُستعمل هذا الفحص لتحديد:", alpha=True),
 BN("Strictly, MR-positive bacteria **ferment** glucose (mixed-acid fermentation) — \"oxidize\" in the sheet means use/break down glucose.",
    "علميًا البكتيريا الموجبة لـ`MR` **تُخمّر** الكلوكوز (تخمّر الحوامض المختلطة) — وكلمة \"oxidize\" في الورقة تعني استهلاك الكلوكوز وتحليله."),
 L(["Incubate **glucose phosphate peptone water media (MR-VP)** with young bacterial culture for **24-48 h at 37C**.", "Add **2-3 drops methyl red** reagent into the broth."],
   ["احضن **وسط ماء الببتون الفوسفاتي الكلوكوزي (`MR-VP`)** مع مزرعة بكتيرية فتية مدّة **24–48 ساعة عند 37°م**.", "أضف **2–3 قطرات من كاشف أحمر المثيل** إلى المزرعة."],
   en="**Procedure:**", ar="**الطريقة:**"),
 RES(["**Red color solution: Positive** …….. __E.coli__.", "**Yellow: Negative** ……. __Klebsiella__."],
   ["**محلول أحمر: موجب** …….. `__E.coli__`.", "**أصفر: سالب** ……. `__Klebsiella__`."]),
 F("mr-tubes.png", "MR- (yellow) and MR+ (red)", "`MR-` (أصفر) و`MR+` (أحمر)", h="44mm"),

 # ───────────────────────── 5 oxidase
 SEC("Oxidase test", "فحص الأوكسيديز"),
 H2("5- Oxidase Test:", "5. فحص الأوكسيديز:"),
 C("This test is used to identify microorganisms containing the enzyme **cytochrome oxidase**.", "يُستعمل هذا الفحص لتشخيص الأحياء المجهرية التي تحتوي إنزيم **السايتوكروم أوكسيديز**."),
 L(["Wet **filter paper** with the indicator composed of **N,N,N,N tetramethyl- p –phenylenediamine dihydrochloride (TNPD)**.",
    "Use a **wooden stick** to transfer a large mass of pure bacteria to the filter paper.",
    ["Observe the filter membrane for **up to three minutes**.", "If the area of inoculation turns **dark-blue** the result is **positive**.", "If a color change does not occur the result is **negative**."]],
   ["بلّل **ورقة الترشيح** بالكاشف المكوّن من **رباعي مثيل بارا فينيلين ثنائي الأمين ثنائي الهيدروكلوريد (`TNPD`)**.",
    "استعمل **عودًا خشبيًا** لنقل كتلة كبيرة من البكتيريا النقية إلى ورقة الترشيح.",
    ["راقب غشاء الترشيح **مدّة تصل إلى ثلاث دقائق**.", "إذا تحوّلت منطقة التلقيح إلى **أزرق داكن** فالنتيجة **موجبة**.", "وإذا لم يتغيّر اللون فالنتيجة **سالبة**."]],
   en="**Procedure:**", ar="**الطريقة:**"),
 RES(["**Positive** ……...... __Pseudomadacea__.", "**Negative** ……….. __Enterobacteriaceae__."],
   ["**موجب** ……...... `__Pseudomonadaceae__` (العائلة الزائفية).", "**سالب** ……….. `__Enterobacteriaceae__` (العائلة المعوية)."]),
 F("oxidase-test.png", "Figure ( 1 ): Oxidase test (dark-blue spot = positive)", "الشكل (1): فحص الأوكسيديز (بقعة زرقاء داكنة = موجب)", h="46mm"),
 BN("\"Pseudomadacea\" = **Pseudomonadaceae** (e.g. __Pseudomonas__); the reagent is usually written **TMPD** (tetramethyl-p-phenylenediamine).",
    "\"Pseudomadacea\" المقصود **`Pseudomonadaceae`** (مثل `__Pseudomonas__`)؛ والكاشف يُكتب عادةً **`TMPD`**."),

 # ───────────────────────── 6 urease
 SEC("Urease test", "فحص اليوريز"),
 H2("6- Urease Test", "6. فحص اليوريز"),
 C("This test is used to detect if the bacteria a possess the enzyme **Urease** that hydrolyzing **urea** into **ammonia and CO2**.",
   "يُستعمل هذا الفحص لكشف امتلاك البكتيريا إنزيم **اليوريز** الذي يحلّل **اليوريا** إلى **أمونيا و`CO2`**."),
 L(["Inoculate the **urea agar** with the required bacteria.", "Incubate at **37 Cﹾ for 24-48 hrs**."],
   ["لقّح **آغار اليوريا** بالبكتيريا المطلوبة.", "احضن **عند 37°م مدّة 24–48 ساعة**."], en="**Procedure:**", ar="**الطريقة:**"),
 RES(["**Positive Pink color** ………. __Klebsiella, proteus, Helicobacter pylori__.", "**Negative Yellow color** …… __E.coli__"],
   ["**موجب لون وردي** ………. `__Klebsiella__` و`__Proteus__` و`__Helicobacter pylori__`.", "**سالب لون أصفر** …… `__E.coli__`"]),
 F("urease-tubes.png", "Urease test: Negative (yellow) and Positive (pink)", "فحص اليوريز: سالب (أصفر) وموجب (وردي)", h="50mm"),
 BN("Ammonia makes the medium **alkaline**, so the **phenol red** indicator in urea agar turns **pink**.", "الأمونيا تجعل الوسط **قاعديًا**، فيتحوّل كاشف **الفينول الأحمر** في آغار اليوريا إلى **الوردي**."),

 # ───────────────────────── 7 citrate
 SEC("Citrate test", "فحص السترات"),
 H2("7- Citrate Test:", "7. فحص السترات:"),
 C(["**Purpose of the test**: to detect bacteria capable of consuming **citrate as a source of carbon** and **ammonia as a source of nitrogen**.",
    "Bacteria that grow on this medium produce an enzyme **citrate permease**."],
   ["**غرض الفحص**: كشف البكتيريا القادرة على استهلاك **السترات مصدرًا للكربون** و**الأمونيا مصدرًا للنيتروجين**.",
    "والبكتيريا التي تنمو على هذا الوسط تنتج إنزيم **ناقل السترات (`citrate permease`)**."]),
 C(["**Media**: **Simmons Citrate agar**", "**Reagent**: **Bromothymol Blue** indicater.", "**Note**: the reagent is **included in the medium**."],
   ["**الوسط**: **آغار سترات سيمونز**", "**الكاشف**: كاشف **أزرق البروموثايمول**.", "**ملاحظة**: الكاشف **موجود ضمن الوسط**."]),
 L(["The **slant is streaked only** with the required bacteria.", "Incubate at **37 C for 48 hrs**.", "Observed a color change."],
   ["**يُخطّط سطح الوسط المائل فقط** بالبكتيريا المطلوبة.", "احضن **عند 37°م مدّة 48 ساعة**.", "لاحظ تغيّر اللون."], en="**The procedure:**", ar="**الطريقة:**"),
 RES(["**Negative** ………. **Green** like __E.coli__.", "**Positive** ……….. **Blue** like __Pseudomonas spp.__"],
   ["**سالب** ………. **أخضر** مثل `__E.coli__`.", "**موجب** ……….. **أزرق** مثل `__Pseudomonas spp.__`"]),
 F("citrate-tubes.png", "Citrate test: Negative (green) and Positive (blue)", "فحص السترات: سالب (أخضر) وموجب (أزرق)", h="44mm"),

 # ───────────────────────── 8 TSI
 SEC("TSI test", "فحص آغار الحديد ثلاثي السكّر"),
 H2("8- Triple sugar Iron Agar test (TSI):", "8. فحص آغار الحديد ثلاثي السكّر (TSI):"),
 C("The name of the test indicates the name of the medium containing the **3 type of sugar: glucose, sucrose and lactose**. In addition to **ferrous sulfate** compound and **red phenol** reagent.",
   "يدلّ اسم الفحص على اسم الوسط الذي يحتوي **3 أنواع من السكّر: الكلوكوز والسكروز واللاكتوز**. إضافةً إلى مركّب **كبريتات الحديدوز** وكاشف **الفينول الأحمر**."),
 L(["**Fermentation of sugars.**", "**Detection of gases CO2.**", "**Detection of H2S.**"], ["**تخمير السكّريات.**", "**كشف الغازات `CO2`.**", "**كشف `H2S`.**"],
   en="**This test is used to detect**", ar="**يُستعمل هذا الفحص لكشف**", alpha=True),
 L(["If **neither lactose \\ sucrose nor glucose** is fermented, both the **butt and the slant will be red**. (**k\\k**), like __pseudomonas spp.__",
    ["If the **glucose** is fermented, the **butt will be yellow**.", "But the **slant will be red**. (**k\\A**), like: __Slamonella typhi.__"],
    "If **lactose and sucrose** is fermented, the **butt and slant will be yellow**. (**A\\A**), like: __E.coli.__",
    ["if **H2S** is produced, the **black** color of ferrous sulfide is seen.", "Like __Proteus spp.__"],
    "Some organisms generate **gases CO2**, which produces **bubbles or cracks** on the medium."],
   ["إذا لم يُخمَّر **اللاكتوز / السكروز ولا الكلوكوز**، يكون **القاع والسطح المائل أحمرين**. (**`K/K`**)، مثل `__Pseudomonas spp.__`",
    ["إذا خُمِّر **الكلوكوز** يصبح **القاع أصفر**.", "لكن **السطح المائل يبقى أحمر**. (**`K/A`**)، مثل: `__Salmonella typhi__`."],
    "إذا خُمِّر **اللاكتوز والسكروز** يصبح **القاع والسطح المائل أصفرين**. (**`A/A`**)، مثل: `__E.coli__`.",
    ["إذا أُنتج **`H2S`** يُرى اللون **الأسود** لكبريتيد الحديدوز.", "مثل `__Proteus spp.__`"],
    "بعض الكائنات تولّد **غازات `CO2`** فتظهر **فقاعات أو تشقّقات** في الوسط."],
   en="**Interpretation of results:**", ar="**تفسير النتائج:**"),
 C("H2S + Feso4 → Fes↓ + So3 + H2O", "`H2S + FeSO4 → FeS↓ + SO3 + H2O` (كبريتيد الحديدوز الأسود يترسّب)"),
 F("tsi-tubes.png", "Figure ( 2 ): TSI test — K/K Negative, A/A, A/A Gas, A/A Gas H₂S, A/A H₂S, K/A, K/A Gas, K/A H₂S (A: Acidic, K: Alkaline)",
   "الشكل (2): فحص `TSI` — `K/K` سالب، `A/A`، `A/A` غاز، `A/A` غاز و`H₂S`، `A/A` و`H₂S`، `K/A`، `K/A` غاز، `K/A` و`H₂S` (`A`: حامضي، `K`: قاعدي)", h="62mm"),
 T([B("Result (slant/butt)", "النتيجة (السطح/القاع)"), B("Colour", "اللون"), B("Meaning", "المعنى"), B("Example", "مثال")],
   [[B("**K/K**", "**`K/K`**"), B("red / red", "أحمر / أحمر"), B("no sugar fermented", "لا تخمير"), B("__Pseudomonas__", "`__Pseudomonas__`")],
    [B("**K/A**", "**`K/A`**"), B("red / yellow", "أحمر / أصفر"), B("glucose only", "الكلوكوز فقط"), B("__Salmonella typhi__", "`__Salmonella typhi__`")],
    [B("**A/A**", "**`A/A`**"), B("yellow / yellow", "أصفر / أصفر"), B("lactose / sucrose (+ glucose)", "اللاكتوز / السكروز (+ الكلوكوز)"), B("__E. coli__", "`__E. coli__`")],
    [B("**H₂S +**", "**`H₂S` +**"), B("black", "أسود"), B("ferrous sulfide", "كبريتيد الحديدوز"), B("__Proteus__", "`__Proteus__`")],
    [B("**Gas +**", "**غاز +**"), B("bubbles / cracks", "فقاعات / تشقّقات"), B("CO₂ produced", "إنتاج `CO₂`"), B("—", "—")]],
   key_cols=[0], widths=[22, 22, 30, 26], style="summary", label_en="Reading TSI (A = acid, K = alkaline)", label_ar="قراءة `TSI` (`A` = حامضي، `K` = قاعدي)"),
 BN("Results are written **slant/butt**: K/A = alkaline (red) slant over acid (yellow) butt. \"red phenol\" = **phenol red**; \"Slamonella\" = **Salmonella**.",
    "تُكتب النتيجة **السطح/القاع**: `K/A` = سطح قاعدي (أحمر) فوق قاع حامضي (أصفر). و\"red phenol\" = **الفينول الأحمر**؛ و\"Slamonella\" = **`Salmonella`**."),

 # ───────────────────────── summary
 SEC("All tests at a glance", "كل الفحوص بنظرة"),
 T([B("Test", "الفحص"), B("Enzyme / detects", "الإنزيم / يكشف"), B("Positive", "الموجب"), B("Example +", "مثال +"), B("Example −", "مثال −")],
   [[B("**Catalase**", "**الكاتاليز**"), B("catalase (H₂O₂ → H₂O + O₂)", "الكاتاليز (`H₂O₂ → H₂O + O₂`)"), B("bubbles", "فقاعات"), B("__Staphylococcus__", "`__Staphylococcus__`"), B("__Streptococcus__", "`__Streptococcus__`")],
    [B("**Indole**", "**الإندول**"), B("tryptophanase", "التربتوفانيز"), B("red ring (Kovac's)", "حلقة حمراء (كوفاكس)"), B("__E. coli__", "`__E. coli__`"), B("__P. aeruginosa__", "`__P. aeruginosa__`")],
    [B("**Coagulase**", "**التخثّر**"), B("clots plasma", "يخثّر البلازما"), B("agglutination / clot", "تلازن / خثرة"), B("__S. aureus__", "`__S. aureus__`"), B("other staphylococci", "العنقوديات الأخرى")],
    [B("**Methyl red**", "**أحمر المثيل**"), B("acid from glucose (pH ≤ 4.5)", "حامض من الكلوكوز (`pH ≤ 4.5`)"), B("red", "أحمر"), B("__E. coli__", "`__E. coli__`"), B("__Klebsiella__ (yellow)", "`__Klebsiella__` (أصفر)")],
    [B("**Oxidase**", "**الأوكسيديز**"), B("cytochrome oxidase", "السايتوكروم أوكسيديز"), B("dark blue", "أزرق داكن"), B("__Pseudomonas__", "`__Pseudomonas__`"), B("Enterobacteriaceae", "العائلة المعوية")],
    [B("**Urease**", "**اليوريز**"), B("urea → NH₃ + CO₂", "يوريا ← `NH₃ + CO₂`"), B("pink", "وردي"), B("__Klebsiella, Proteus, H. pylori__", "`__Klebsiella__`، `__Proteus__`، `__H. pylori__`"), B("__E. coli__ (yellow)", "`__E. coli__` (أصفر)")],
    [B("**Citrate**", "**السترات**"), B("citrate permease", "ناقل السترات"), B("blue", "أزرق"), B("__Pseudomonas__", "`__Pseudomonas__`"), B("__E. coli__ (green)", "`__E. coli__` (أخضر)")],
    [B("**TSI**", "**`TSI`**"), B("sugars, gas, H₂S", "السكّريات، والغاز، و`H₂S`"), B("yellow / black / bubbles", "أصفر / أسود / فقاعات"), B("__E. coli__ A/A; __Proteus__ H₂S", "`__E. coli__` `A/A`؛ `__Proteus__` `H₂S`"), B("__Pseudomonas__ K/K", "`__Pseudomonas__` `K/K`")]],
   key_cols=[0], widths=[16, 24, 20, 21, 19], style="summary", label_en="The 8 tests", label_ar="الفحوص الثمانية"),
] + TERMS([
 ("Biochemical test", "الفحص الكيميائي الحيوي"),
 ("Catalase", "الكاتاليز (إنزيم تحليل بيروكسيد الهيدروجين)"),
 ("Hydrogen peroxide", "بيروكسيد الهيدروجين / الماء الأوكسجيني"),
 ("Tryptophan / tryptophanase", "التربتوفان / التربتوفانيز"),
 ("Kovac's reagent", "كاشف كوفاكس"),
 ("Peptone water", "ماء الببتون"),
 ("Coagulase", "الكواغيوليز / إنزيم التخثّر"),
 ("Fibrinogen / fibrin", "الفايبرينوجين / الفايبرين"),
 ("Methyl red (MR)", "أحمر المثيل"),
 ("MR-VP medium", "وسط ماء الببتون الفوسفاتي الكلوكوزي"),
 ("Cytochrome oxidase", "السايتوكروم أوكسيديز"),
 ("Urease / urea agar", "اليوريز / آغار اليوريا"),
 ("Simmons citrate agar", "آغار سترات سيمونز"),
 ("Bromothymol blue", "أزرق البروموثايمول"),
 ("Citrate permease", "ناقل السترات (برميز السترات)"),
 ("Triple sugar iron agar (TSI)", "آغار الحديد ثلاثي السكّر"),
 ("Slant / butt", "السطح المائل / القاع"),
 ("Phenol red", "الفينول الأحمر"),
 ("Ferrous sulfate / ferrous sulfide", "كبريتات الحديدوز / كبريتيد الحديدوز"),
 ("Acidic (A) / alkaline (K)", "حامضي / قاعدي"),
])

# ───────────────────────── questions (the slides have none — all BIOS)
IMG = lambda f, h="36mm": dict(img="assets/" + f, img_h=h)
mcq = [
 {"topic_en": "Catalase, indole and coagulase", "topic_ar": "الكاتاليز والإندول والتخثّر"},
 Q("Biochemical tests are needed because many bacteria have:", "نحتاج الفحوص الكيميائية الحيوية لأن بكتيريا كثيرة لها:", O(("Different colours", "ألوان مختلفة"), ("Similar shape and size", "شكل وحجم متشابهان"), ("No enzymes", "لا إنزيمات"), ("No cell wall", "لا جدار خلوي")), "b"),
 Q("Catalase breaks hydrogen peroxide into:", "يحلّل الكاتاليز بيروكسيد الهيدروجين إلى:", O(("Water and oxygen", "ماء وأوكسجين"), ("Indole and ammonia", "إندول وأمونيا"), ("Ammonia and CO₂", "أمونيا وCO₂"), ("Acid and gas", "حامض وغاز")), "a"),
 Q("A positive catalase test shows:", "يُظهر فحص الكاتاليز الموجب:", O(("A red ring", "حلقة حمراء"), ("A clot", "خثرة"), ("Bubbles", "فقاعات"), ("Blue colour", "لونًا أزرق")), "c"),
 Q("Which is catalase negative?", "أيّها سالب الكاتاليز؟", O(("Staphylococcus", "العنقودية"), ("E. coli", "الإشريكية القولونية"), ("Pseudomonas", "الزائفة"), ("Streptococcus", "العقدية")), "d"),
 Q("The indole test detects the ability to convert:", "يكشف فحص الإندول القدرة على تحويل:", O(("Urea to ammonia", "اليوريا إلى أمونيا"), ("Tryptophan to indole", "التربتوفان إلى إندول"), ("Citrate to CO₂", "السترات إلى CO₂"), ("Glucose to acid", "الكلوكوز إلى حامض")), "b"),
 Q("The reagent added in the indole test is:", "الكاشف المضاف في فحص الإندول:", O(("Kovac's reagent", "كاشف كوفاكس"), ("Methyl red", "أحمر المثيل"), ("Hydrogen peroxide", "بيروكسيد الهيدروجين"), ("TNPD", "TNPD")), "a"),
 Q("The medium for the indole test is:", "وسط فحص الإندول:", O(("Urea agar", "آغار اليوريا"), ("Simmons citrate", "سترات سيمونز"), ("Peptone water", "ماء الببتون"), ("TSI", "TSI")), "c"),
 Q("Indole negative organism in the lab:", "الكائن السالب للإندول في العملي:", O(("E. coli", "الإشريكية القولونية"), ("Proteus", "المتقلّبة"), ("Klebsiella", "الكليبسيلا"), ("Pseudomonas aeruginosa", "الزائفة الزنجارية")), "d"),
 Q("Coagulase converts:", "يحوّل الكواغيوليز:", O(("Fibrinogen to fibrin (clot)", "الفايبرينوجين إلى فايبرين (خثرة)"), ("H₂O₂ to water", "H₂O₂ إلى ماء"), ("Urea to ammonia", "اليوريا إلى أمونيا"), ("Tryptophan to indole", "التربتوفان إلى إندول")), "a"),
 Q("A coagulase-positive organism is:", "الكائن الموجب للتخثّر:", O(("Streptococcus", "العقدية"), ("Staph. aureus", "العنقودية الذهبية"), ("E. coli", "الإشريكية القولونية"), ("Pseudomonas", "الزائفة")), "b"),
 {"topic_en": "Methyl red and oxidase", "topic_ar": "أحمر المثيل والأوكسيديز"},
 Q("In the MR test, a positive result is:", "في فحص MR تكون النتيجة الموجبة:", O(("Yellow", "أصفر"), ("Blue", "أزرق"), ("Red", "أحمر"), ("Black", "أسود")), "c"),
 Q("The pH in a positive MR test falls to:", "ينخفض الأس الهيدروجيني في فحص MR الموجب إلى:", O(("7", "7"), ("8.5", "8.5"), ("6", "6"), ("4.5 or below", "4.5 أو أقل")), "d"),
 Q("The medium used for the MR test is:", "الوسط المستعمل لفحص MR:", O(("Glucose phosphate peptone water (MR-VP)", "ماء الببتون الفوسفاتي الكلوكوزي (MR-VP)"), ("Urea agar", "آغار اليوريا"), ("Blood agar", "آغار الدم"), ("Simmons citrate", "سترات سيمونز")), "a"),
 Q("MR negative organism in the lab:", "الكائن السالب لـ MR في العملي:", O(("E. coli", "الإشريكية القولونية"), ("Klebsiella", "الكليبسيلا"), ("Proteus", "المتقلّبة"), ("Staphylococcus", "العنقودية")), "b"),
 Q("The oxidase test identifies the enzyme:", "يشخّص فحص الأوكسيديز إنزيم:", O(("Catalase", "الكاتاليز"), ("Urease", "اليوريز"), ("Cytochrome oxidase", "السايتوكروم أوكسيديز"), ("Coagulase", "الكواغيوليز")), "c"),
 Q("A positive oxidase test turns the filter paper:", "يحوّل فحص الأوكسيديز الموجب ورقة الترشيح إلى:", O(("Pink", "وردي"), ("Yellow", "أصفر"), ("Green", "أخضر"), ("Dark blue", "أزرق داكن")), "d"),
 Q("The oxidase result is read within:", "تُقرأ نتيجة الأوكسيديز خلال:", O(("Three minutes", "ثلاث دقائق"), ("24 hours", "24 ساعة"), ("48 hours", "48 ساعة"), ("One week", "أسبوع")), "a"),
 Q("Oxidase-negative family in the lab:", "العائلة السالبة للأوكسيديز في العملي:", O(("Pseudomonadaceae", "الزائفية"), ("Enterobacteriaceae", "المعوية"), ("Neisseriaceae", "النيسرية"), ("Vibrionaceae", "الضمّية")), "b"),
 {"topic_en": "Urease, citrate and TSI", "topic_ar": "اليوريز والسترات وTSI"},
 Q("Urease hydrolyzes urea into:", "يحلّل اليوريز اليوريا إلى:", O(("Indole", "إندول"), ("Water and oxygen", "ماء وأوكسجين"), ("Ammonia and CO₂", "أمونيا وCO₂"), ("Fibrin", "فايبرين")), "c"),
 Q("A positive urease test colour is:", "لون فحص اليوريز الموجب:", O(("Yellow", "أصفر"), ("Green", "أخضر"), ("Black", "أسود"), ("Pink", "وردي")), "d"),
 Q("Which is urease negative in the lab?", "أيّها سالب اليوريز في العملي؟", O(("E. coli", "الإشريكية القولونية"), ("Proteus", "المتقلّبة"), ("Klebsiella", "الكليبسيلا"), ("Helicobacter pylori", "الملوية البوابية")), "a"),
 Q("In the citrate test bacteria use citrate as a source of:", "في فحص السترات تستعمل البكتيريا السترات مصدرًا لـ:", O(("Nitrogen", "النيتروجين"), ("Carbon", "الكربون"), ("Iron", "الحديد"), ("Sulfur", "الكبريت")), "b"),
 Q("The indicator in Simmons citrate agar is:", "الكاشف في آغار سترات سيمونز:", O(("Phenol red", "الفينول الأحمر"), ("Methyl red", "أحمر المثيل"), ("Bromothymol blue", "أزرق البروموثايمول"), ("Kovac's", "كوفاكس")), "c"),
 Q("A positive citrate test colour is:", "لون فحص السترات الموجب:", O(("Green", "أخضر"), ("Pink", "وردي"), ("Red", "أحمر"), ("Blue", "أزرق")), "d"),
 Q("TSI contains the sugars:", "يحتوي TSI السكّريات:", O(("Glucose, sucrose and lactose", "الكلوكوز والسكروز واللاكتوز"), ("Glucose and maltose", "الكلوكوز والمالتوز"), ("Lactose only", "اللاكتوز فقط"), ("Mannitol and sucrose", "المانيتول والسكروز")), "a"),
 Q("A TSI result K/A means:", "نتيجة TSI ‏K/A تعني:", O(("No fermentation", "لا تخمير"), ("Glucose fermented only (red slant, yellow butt)", "تخمير الكلوكوز فقط (سطح أحمر وقاع أصفر)"), ("All sugars fermented", "تخمير كل السكّريات"), ("H₂S only", "H₂S فقط")), "b"),
 Q("A/A in TSI is given by:", "تعطي ‏A/A في TSI:", O(("Pseudomonas", "الزائفة"), ("Salmonella typhi", "السالمونيلا التيفية"), ("E. coli", "الإشريكية القولونية"), ("Proteus only", "المتقلّبة فقط")), "c"),
 Q("Black colour in TSI indicates:", "اللون الأسود في TSI يدلّ على:", O(("Gas", "غاز"), ("Glucose fermentation", "تخمير الكلوكوز"), ("Alkaline slant", "سطح قاعدي"), ("H₂S production (ferrous sulfide)", "إنتاج H₂S (كبريتيد الحديدوز)")), "d"),
 {"topic_en": "Picture questions", "topic_ar": "أسئلة الصور"},
 Q("This picture shows the result of which test?", "هذه الصورة تُظهر نتيجة أيّ فحص؟", O(("Methyl red", "أحمر المثيل"), ("Citrate", "السترات"), ("Indole", "الإندول"), ("Coagulase", "التخثّر")), "a", **IMG("mr-tubes.png", "34mm")),
 Q("In this urease picture, the pink tube is:", "في صورة اليوريز هذه، الأنبوب الوردي:", O(("Negative", "سالب"), ("Positive", "موجب"), ("Contaminated", "ملوّث"), ("Uninoculated", "غير ملقّح")), "b", **IMG("urease-tubes.png", "34mm")),
 Q("In this oxidase picture, the dark-blue spot means:", "في صورة الأوكسيديز هذه، البقعة الزرقاء الداكنة تعني:", O(("Negative", "سالب"), ("Catalase positive", "موجب الكاتاليز"), ("Positive", "موجب"), ("H₂S", "H₂S")), "c", **IMG("oxidase-test.png", "32mm")),
 Q("In this TSI picture, the blackened tubes show:", "في صورة TSI هذه، الأنابيب السوداء تُظهر:", O(("Gas only", "غازًا فقط"), ("No fermentation", "لا تخمير"), ("Alkaline butt", "قاعًا قاعديًا"), ("H₂S production", "إنتاج H₂S")), "d", **IMG("tsi-tubes.png", "40mm")),
]
mcq = balance(mcq, 96)

tf = [
 TF("Biochemical tests identify bacteria based on differences in biochemical activities.", "تشخّص الفحوص الكيميائية الحيوية البكتيريا على أساس الاختلاف في نشاطاتها الكيميائية الحيوية.", "T"),
 TF("A wooden stick is used to transfer the colony in the catalase test.", "يُستعمل عود خشبي لنقل المستعمرة في فحص الكاتاليز.", "T"),
 TF("Streptococcus is catalase positive.", "العقدية موجبة الكاتاليز.", "F"),
 TF("Kovac's reagent produces a bright red compound with indole.", "ينتج كاشف كوفاكس مركّبًا أحمر لامعًا مع الإندول.", "T"),
 TF("The indole test is incubated at 37°C for 24 hours.", "يُحضن فحص الإندول عند 37°م مدّة 24 ساعة.", "T"),
 TF("Coagulase is an enzyme that dissolves plasma clots.", "الكواغيوليز إنزيم يُذيب خثرات البلازما.", "F"),
 TF("Agglutination in the slide coagulase test is positive, as in Staph. aureus.", "التلازن في فحص التخثّر بالشريحة موجب، كما في العنقودية الذهبية.", "T"),
 TF("In the MR test, yellow colour is positive.", "في فحص MR اللون الأصفر موجب.", "F"),
 TF("Some bacteria convert the final acids into neutral substances and raise the pH.", "بعض البكتيريا تحوّل الحوامض النهائية إلى مواد متعادلة وترفع الأس الهيدروجيني.", "T"),
 TF("Enterobacteriaceae are oxidase positive.", "العائلة المعوية موجبة الأوكسيديز.", "F"),
 TF("Helicobacter pylori is urease positive.", "الملوية البوابية موجبة اليوريز.", "T"),
 TF("The reagent of the citrate test is added after incubation.", "يُضاف كاشف فحص السترات بعد الحضن.", "F"),
 TF("In TSI, K/K means neither lactose, sucrose nor glucose is fermented.", "في TSI تعني K/K عدم تخمير اللاكتوز والسكروز والكلوكوز.", "T"),
 TF("Bubbles or cracks in TSI indicate gas production.", "الفقاعات أو التشقّقات في TSI تدلّ على إنتاج الغاز.", "T"),
]

traps = [
 TR("Same colour, different meaning", "اللون نفسه بمعنى مختلف", "RED = positive in indole (ring) and MR; but RED slant/butt in TSI = alkaline (K, no fermentation). YELLOW = negative in MR and urease, but acid (A) in TSI.", "الأحمر = موجب في الإندول (حلقة) وMR؛ لكن السطح/القاع الأحمر في TSI = قاعدي (K، لا تخمير). والأصفر = سالب في MR واليوريز، لكنه حامضي (A) في TSI."),
 TR("E. coli results", "نتائج الإشريكية القولونية", "E. coli: indole +, MR +, urease −, citrate − (green), TSI A/A.", "الإشريكية القولونية: إندول +، MR +، يوريز −، سترات − (أخضر)، TSI ‏A/A."),
 TR("Klebsiella", "الكليبسيلا", "Klebsiella is MR NEGATIVE (yellow) but urease POSITIVE (pink).", "الكليبسيلا سالبة MR (أصفر) لكنها موجبة اليوريز (وردي)."),
 TR("Pseudomonas", "الزائفة", "Pseudomonas: indole −, oxidase +, citrate + (blue), TSI K/K.", "الزائفة: إندول −، أوكسيديز +، سترات + (أزرق)، TSI ‏K/K."),
 TR("Catalase vs coagulase", "الكاتاليز مقابل التخثّر", "Catalase (H₂O₂ → bubbles) separates Staph from Strep; coagulase (plasma → clot) separates S. aureus from other staphylococci.", "الكاتاليز (H₂O₂ ← فقاعات) يفصل العنقودية عن العقدية؛ والتخثّر (بلازما ← خثرة) يفصل الذهبية عن العنقوديات الأخرى."),
 TR("Reagent inside or added?", "الكاشف داخل الوسط أم يُضاف؟", "Citrate (bromothymol blue), urease and TSI (phenol red): indicator IN the medium. Indole (Kovac's) and MR (methyl red): reagent ADDED after incubation.", "السترات (أزرق البروموثايمول) واليوريز وTSI (الفينول الأحمر): الكاشف داخل الوسط. الإندول (كوفاكس) وMR (أحمر المثيل): الكاشف يُضاف بعد الحضن."),
 TR("Reading K/A", "قراءة K/A", "Write SLANT first, then BUTT: K/A = red (alkaline) slant, yellow (acid) butt = glucose only (e.g. Salmonella typhi).", "يُكتب السطح أولًا ثم القاع: K/A = سطح أحمر (قاعدي) وقاع أصفر (حامضي) = الكلوكوز فقط (مثل السالمونيلا التيفية)."),
]

important = [
 IM("Why are biochemical tests needed? Explain the catalase test.", "لماذا نحتاج الفحوص الكيميائية الحيوية؟ اشرح فحص الكاتاليز.",
    "Many bacteria have similar shape and size, so species are identified by differences in biochemical activities. Catalase breaks H₂O₂ into water and oxygen: transfer a colony with a wooden stick to a slide, add a drop of H₂O₂, look for bubbles. Staphylococcus +, Streptococcus −.",
    "بكتيريا كثيرة متشابهة الشكل والحجم، فتُشخَّص الأنواع باختلاف نشاطاتها الكيميائية الحيوية. الكاتاليز يحلّل H₂O₂ إلى ماء وأوكسجين: انقل مستعمرة بعود خشبي إلى شريحة، وأضف قطرة H₂O₂، وابحث عن الفقاعات. العنقودية +، والعقدية −."),
 IM("Describe the indole test (principle, procedure, result).", "صف فحص الإندول (المبدأ والطريقة والنتيجة).",
    "Tryptophanase converts tryptophan into indole, pyruvic acid and ammonia. Inoculate peptone water, incubate at 37°C for 24 h, add 5 drops of Kovac's reagent: red ring = positive (E. coli); no ring = negative (Pseudomonas aeruginosa).",
    "التربتوفانيز يحوّل التربتوفان إلى إندول وحامض البايروفيك وأمونيا. لقّح ماء الببتون، واحضن عند 37°م مدّة 24 ساعة، وأضف 5 قطرات من كاشف كوفاكس: حلقة حمراء = موجب (الإشريكية القولونية)؛ لا حلقة = سالب (الزائفة الزنجارية)."),
 IM("Describe the slide coagulase test.", "صف فحص التخثّر بالشريحة.",
    "Coagulase clots plasma (fibrinogen → fibrin). Place a drop of distilled water on a slide, mix a colony in it with a wooden stick, add a drop of plasma and mix: agglutination = positive (Staph. aureus); no agglutination = negative (other staphylococci).",
    "الكواغيوليز يخثّر البلازما (فايبرينوجين ← فايبرين). ضع قطرة ماء مقطّر على شريحة، وامزج فيها مستعمرة بعود خشبي، وأضف قطرة بلازما وامزج: تلازن = موجب (العنقودية الذهبية)؛ لا تلازن = سالب (العنقوديات الأخرى)."),
 IM("What does the methyl red test determine and how is it read?", "ماذا يحدّد فحص أحمر المثيل وكيف يُقرأ؟",
    "The ability to produce a high concentration of acid from glucose (pH 4.5 or below) and to distinguish species that neutralize their acids. Incubate MR-VP medium 24–48 h at 37°C, add 2–3 drops of methyl red: red = positive (E. coli); yellow = negative (Klebsiella).",
    "القدرة على إنتاج تركيز عالٍ من الحامض من الكلوكوز (pH ‏4.5 أو أقل)، والتفريق بين الأنواع التي تعادل حوامضها. احضن وسط MR-VP مدّة 24–48 ساعة عند 37°م، وأضف 2–3 قطرات أحمر المثيل: أحمر = موجب (الإشريكية)؛ أصفر = سالب (الكليبسيلا)."),
 IM("Describe the oxidase test.", "صف فحص الأوكسيديز.",
    "Detects cytochrome oxidase. Wet filter paper with TNPD (tetramethyl-p-phenylenediamine), rub a large mass of pure bacteria with a wooden stick, observe up to 3 minutes: dark blue = positive (Pseudomonadaceae); no change = negative (Enterobacteriaceae).",
    "يكشف السايتوكروم أوكسيديز. بلّل ورقة ترشيح بـ TNPD، وافرك عليها كتلة كبيرة من بكتيريا نقية بعود خشبي، وراقب حتى 3 دقائق: أزرق داكن = موجب (الزائفية)؛ لا تغيّر = سالب (المعوية)."),
 IM("Describe the urease and citrate tests.", "صف فحصَي اليوريز والسترات.",
    "Urease: hydrolyzes urea into ammonia and CO₂; inoculate urea agar, 37°C 24–48 h: pink = positive (Klebsiella, Proteus, H. pylori), yellow = negative (E. coli). Citrate: citrate as carbon and ammonia as nitrogen source (citrate permease); Simmons citrate agar with bromothymol blue in the medium; streak the slant, 37°C 48 h: blue = positive (Pseudomonas), green = negative (E. coli).",
    "اليوريز: يحلّل اليوريا إلى أمونيا وCO₂؛ لقّح آغار اليوريا، 37°م ‏24–48 ساعة: وردي = موجب (الكليبسيلا والمتقلّبة والملوية)، أصفر = سالب (الإشريكية). السترات: السترات مصدر كربون والأمونيا مصدر نيتروجين (ناقل السترات)؛ آغار سترات سيمونز وفيه أزرق البروموثايمول؛ خطّط السطح المائل، 37°م ‏48 ساعة: أزرق = موجب (الزائفة)، أخضر = سالب (الإشريكية)."),
 IM("What does TSI contain and detect? Interpret its results.", "ماذا يحتوي TSI وماذا يكشف؟ فسّر نتائجه.",
    "Glucose, sucrose, lactose, ferrous sulfate and phenol red; detects sugar fermentation, gas and H₂S. K/K (red/red): no fermentation (Pseudomonas). K/A (red slant, yellow butt): glucose only (Salmonella typhi). A/A (yellow/yellow): lactose/sucrose fermented (E. coli). Black: H₂S (Proteus). Bubbles/cracks: gas.",
    "الكلوكوز والسكروز واللاكتوز وكبريتات الحديدوز والفينول الأحمر؛ ويكشف تخمير السكّريات والغاز وH₂S. ‏K/K (أحمر/أحمر): لا تخمير (الزائفة). ‏K/A (سطح أحمر وقاع أصفر): الكلوكوز فقط (السالمونيلا التيفية). ‏A/A (أصفر/أصفر): تخمير اللاكتوز/السكروز (الإشريكية). أسود: H₂S (المتقلّبة). فقاعات/تشقّقات: غاز."),
 IM("Name the positive and negative example of each test in this lab.", "اذكر المثال الموجب والسالب لكل فحص في هذا العملي.",
    "Catalase: Staphylococcus / Streptococcus. Indole: E. coli / P. aeruginosa. Coagulase: S. aureus / other staphylococci. MR: E. coli / Klebsiella. Oxidase: Pseudomonadaceae / Enterobacteriaceae. Urease: Klebsiella, Proteus, H. pylori / E. coli. Citrate: Pseudomonas / E. coli. TSI: E. coli A/A, S. typhi K/A, Pseudomonas K/K, Proteus H₂S.",
    "الكاتاليز: العنقودية / العقدية. الإندول: الإشريكية / الزائفة الزنجارية. التخثّر: العنقودية الذهبية / العنقوديات الأخرى. MR: الإشريكية / الكليبسيلا. الأوكسيديز: الزائفية / المعوية. اليوريز: الكليبسيلا والمتقلّبة والملوية / الإشريكية. السترات: الزائفة / الإشريكية. TSI: الإشريكية A/A، والسالمونيلا التيفية K/A، والزائفة K/K، والمتقلّبة H₂S."),
]

meta = {"subject_en": "Diagnostic Microbiology", "subject_ar": "الأحياء المجهرية التشخيصية", "short_ar": "بكتريا", "instructor": "د. هبة سامي",
        "unit_en": "Lab 6", "unit_ar": "العملي 6", "unit_label": "LAB", "unit_no": "6",
        "title_en": "Biochemical Testing of Microorganisms", "title_ar": "الفحوص الكيميائية الحيوية للأحياء المجهرية",
        "department": "قسم التحليلات", "kind": "Laboratories — عملي", "stage": "The fourth stage — الرابعة"}
blocks, mcq, tf, traps, important = ltr_all(blocks), ltr_all(mcq), ltr_all(tf), ltr_all(traps), ltr_all(important)
save("bacteriology-lab6-biochemical-tests", meta, blocks, mcq, tf, traps, important)
fit("bacteriology-lab6-biochemical-tests", min_gap=0.08)   # no big gaps, small ones too

```
