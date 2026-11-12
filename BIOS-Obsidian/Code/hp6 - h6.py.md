---
source: BIOS-Obsidian/tools/scripts/hp6/h6.py
handouts: [histopathology-lab6-he-stain]
saved: 2026-11-12
tags: [bios, code]
---
# hp6/h6.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#histopathology-lab6-he-stain|histopathology-lab6-he-stain]]

```python
import sys; sys.path.insert(0, "/tmp/claude-0/-home-user-kwmdkm/a7dd109e-db53-5fd3-8234-9dab3a530e24/scratchpad/imm456")
from ci import *            # c helpers + B INSHORT TERMS balance save(split.fix)
sys.path.insert(0, "/tmp/claude-0/-home-user-kwmdkm/a7dd109e-db53-5fd3-8234-9dab3a530e24/scratchpad"); from bidi import ltr_all; from flowfit import fit

# Histopathology practical, lab 6 — "The hematoxylins and eosin" (17 slides, 22 pictures = 19 distinct, no questions;
# "By: M.S.C AYA WESMII"). Third stage → blush, questions merged.
split.ABBR = split.ABBR + ("M.S.C",)
BN = lambda en, ar: N(en, ar, label=["BIOS note", "ملاحظة BIOS"])
O = P

blocks = [
 # ───────────────────────── 1
 SEC("H&E staining", "التصبيغ بالهيماتوكسلين والإيوسين"),
 N("By: M.S.C AYA WESMII", "إعداد: م.م. آية وسمي", label=["Lab sheet", "ورقة العملي"]),
 H2("Why We Stain?", "لماذا نصبغ؟"),
 C(["The full term is **Hematoxylin and Eosin (H&E) staining**.", "It is the **gold standard** for histological examination, used to visualize tissue structure under a microscope.",
    "**Over 80%** of all tissue diagnostics start with an H&E stain."],
   ["الاسم الكامل هو **التصبيغ بالهيماتوكسلين والإيوسين (`H&E`)**.", "وهو **المعيار الذهبي** للفحص النسيجي، ويُستعمل لإظهار بنية النسيج تحت المجهر.",
    "و**أكثر من 80%** من كل التشخيصات النسيجية تبدأ بصبغة `H&E`."]),
 F("stain-collage.png", "Tissues stained with H&E", "أنسجة مصبوغة بـ `H&E`", h="38mm"),

 # ───────────────────────── 2
 SEC("A. Hematoxylin", "أ. الهيماتوكسلين"),
 C(["A **basic dye** derived from the **logwood tree** (__Haematoxylum campechianum__).", "**What it stains**: Acidic (acidophilic) structures.", "**Color**: Stains them a **bluish-purple or dark blue**."],
   ["**صبغة قاعدية** مستخلصة من **شجرة البقّم (خشب الكامبيش)** (`__Haematoxylum campechianum__`).", "**ماذا تصبغ**: التراكيب الحامضية (المحبّة للحامض).", "**اللون**: تصبغها **بنفسجيًا مزرقًّا أو أزرق داكنًا**."]),
 FF(("hematoxylin-bottle.png", "Hematoxylin stain bottle", "قنينة صبغة الهيماتوكسلين", "40mm"), ("hematoxylin-section.png", "Nuclei stained blue-purple by hematoxylin", "أنوية مصبوغة بنفسجيًا مزرقًّا بالهيماتوكسلين", "40mm")),
 L(["**Cell Nucleus** (because DNA/RNA is acidic)", "**Rough Endoplasmic Reticulum**", "**Cartilage**"],
   ["**نواة الخلية** (لأن `DNA/RNA` حامضي)", "**الشبكة الإندوبلازمية الخشنة**", "**الغضروف**"], en="**Targets:**", ar="**الأهداف:**"),
 FF(("rer.png", "Rough Endoplasmic Reticulum with ribosomes", "الشبكة الإندوبلازمية الخشنة مع الرايبوسومات", "36mm"), ("knee-cartilage.png", "KNEE JOINT — Articular Cartilage", "مفصل الركبة — الغضروف المفصلي", "36mm")),
 BN("Hematoxylin stains **acidic** structures, but these are called **basophilic** (they love the **basic** dye) — not \"acidophilic\" as written on the slide. Likewise eosin stains **basic** structures, which are called **acidophilic / eosinophilic** — not \"basophilic\".",
    "الهيماتوكسلين يصبغ التراكيب **الحامضية**، لكنها تُسمّى **محبّة للقاعدة `(basophilic)`** (لأنها تحبّ الصبغة **القاعدية**) — لا \"acidophilic\" كما كُتب في الشريحة. وبالمثل الإيوسين يصبغ التراكيب **القاعدية** التي تُسمّى **محبّة للحامض/للإيوسين `(acidophilic / eosinophilic)`** — لا \"basophilic\"."),
 INSHORT([("Hematoxylin = **basic dye** from the **logwood tree**; colour **blue-purple / dark blue**.", "الهيماتوكسلين = **صبغة قاعدية** من **شجرة البقّم**؛ لونها **بنفسجي مزرق / أزرق داكن**."),
          ("Targets: **nucleus** (acidic DNA/RNA), **RER**, **cartilage**.", "أهدافه: **النواة** (`DNA/RNA` حامضي)، و**الشبكة الإندوبلازمية الخشنة**، و**الغضروف**.")]),

 # ───────────────────────── 3
 SEC("2. Eosin", "2. الإيوسين"),
 C(["**What it stains**: Basic (basophilic) structures.", "**Color**: Stains them shades of **pink, red, or orange**."],
   ["**ماذا يصبغ**: التراكيب القاعدية (المحبّة للقاعدة).", "**اللون**: يصبغها بدرجات من **الوردي أو الأحمر أو البرتقالي**."]),
 FF(("eosin-bottle.png", "Eosin Y stain bottle", "قنينة صبغة الإيوسين `Y`", "40mm"), ("eosin-section.png", "Cytoplasm stained pink by eosin", "سايتوبلازم مصبوغ بالوردي بالإيوسين", "40mm")),
 L(["**Cytoplasm**", "**Muscle fibers**", "**Collagen**", "**Red blood cells**", "**Keratin**"],
   ["**السايتوبلازم**", "**الألياف العضلية**", "**الكولاجين**", "**كريات الدم الحمر**", "**الكيراتين**"], en="**Targets:**", ar="**الأهداف:**"),
 FF(("cytoplasm-cells.png", "Cytoplasm — Plant Cell and Animal Cell", "السايتوبلازم — خلية نباتية وخلية حيوانية", "34mm"), ("muscle-bundle.png", "Muscle fibers", "الألياف العضلية", "34mm")),
 FF(("collagen.png", "Collagen (triple helix and fibrils)", "الكولاجين (اللولب الثلاثي والليفات)", "34mm"), ("rbc.png", "Red blood cells", "كريات الدم الحمر", "34mm")),
 F("keratin-hair.png", "Keratin (hair)", "الكيراتين (الشعر)", h="34mm"),
 T([B("Point", "وجه المقارنة"), B("Hematoxylin", "الهيماتوكسلين"), B("Eosin", "الإيوسين")],
   [[B("**Dye type**", "**نوع الصبغة**"), B("basic (from logwood tree)", "قاعدية (من شجرة البقّم)"), B("acidic", "حامضية")],
    [B("**Stains**", "**تصبغ**"), B("acidic structures (basophilic)", "التراكيب الحامضية (محبّة للقاعدة)"), B("basic structures (acidophilic)", "التراكيب القاعدية (محبّة للحامض)")],
    [B("**Colour**", "**اللون**"), B("bluish-purple / dark blue", "بنفسجي مزرق / أزرق داكن"), B("pink / red / orange", "وردي / أحمر / برتقالي")],
    [B("**Targets**", "**الأهداف**"), B("nucleus, RER, cartilage", "النواة، والشبكة الإندوبلازمية الخشنة، والغضروف"), B("cytoplasm, muscle, collagen, RBCs, keratin", "السايتوبلازم، والعضلات، والكولاجين، وكريات الدم الحمر، والكيراتين")]],
   key_cols=[0], widths=[22, 39, 39], style="summary", label_en="BIOS: hematoxylin vs eosin", label_ar="BIOS: الهيماتوكسلين مقابل الإيوسين"),
 INSHORT([("Eosin colours **pink, red or orange**.", "الإيوسين يلوّن **وردي أو أحمر أو برتقالي**."),
          ("Targets: **cytoplasm, muscle fibers, collagen, RBCs, keratin**.", "أهدافه: **السايتوبلازم، والألياف العضلية، والكولاجين، وكريات الدم الحمر، والكيراتين**.")]),

 # ───────────────────────── 4
 SEC("The Staining Process", "خطوات التصبيغ"),
 C("**1- Tissue Preparation**: A thin slice of tissue (a \"section\") is mounted on a glass slide.", "**1. تحضير النسيج**: توضع شريحة رقيقة من النسيج (\"مقطع\") على شريحة زجاجية."),
 F("section-on-slide.png", "A tissue section is placed on the glass slide", "وضع المقطع النسيجي على الشريحة الزجاجية", h="38mm"),
 C("**2- Hematoxylin**: The slide is immersed in hematoxylin, which stains the **nuclei dark blue**.", "**2. الهيماتوكسلين**: تُغمر الشريحة في الهيماتوكسلين الذي يصبغ **الأنوية بالأزرق الداكن**."),
 F("hematoxylin-immersion.png", "Slides immersed in the staining dish", "غمر الشرائح في وعاء الصبغة", h="40mm"),
 C("**3- Rinsing**: Excess dye is washed off.", "**3. الشطف**: تُغسل الصبغة الزائدة."),
 F("rinsing-scheme.png", "Scheme of picking up sections, staining and washing with distilled water", "مخطّط التقاط المقاطع وتصبيغها وغسلها بالماء المقطّر", h="50mm"),
 C(["**4- \"Bluing\"**: The section is placed in a **weak alkaline solution** (like **ammonia water** or **Scott's tap water**) to turn the hematoxylin a **permanent, crisp blue** color."],
   ["**4. \"التزريق\" (الإزراق)**: يوضع المقطع في **محلول قاعدي ضعيف** (مثل **ماء الأمونيا** أو **ماء سكوت**) لتحويل الهيماتوكسلين إلى لون **أزرق واضح ودائم**."]),
 F("nuclei-blue.png", "After bluing: nuclei crisp blue (arrow)", "بعد الإزراق: الأنوية زرقاء واضحة (السهم)", h="40mm"),
 C("**B. Eosin**: The slide is then immersed in **eosin**, which stains the **cytoplasmic and extracellular components pink**.", "**ب. الإيوسين**: ثم تُغمر الشريحة في **الإيوسين** الذي يصبغ **المكوّنات السايتوبلازمية وخارج الخلوية بالوردي**."),
 F("eosin-glomerulus.png", "After eosin: cytoplasm and connective tissue pink (kidney glomerulus)", "بعد الإيوسين: السايتوبلازم والنسيج الضامّ وردي (كبيبة الكلية)", h="40mm"),
 C("**Dehydration & Mounting**: The slide is **dehydrated through alcohols**, **cleared**, and **sealed with a coverslip** for preservation.", "**نزع الماء والتحميل**: تُنزع المياه من الشريحة **بسلسلة من الكحولات**، ثم **تُروَّق**، و**تُغطّى بساترة** للحفظ."),
 F("coverslip.png", "Mounting with a coverslip", "التحميل بالساترة", h="36mm"),
 FLOW([("Section on slide", "مقطع على الشريحة"), ("Hematoxylin", "الهيماتوكسلين"), ("Rinse", "شطف"), ("Bluing (alkaline)", "إزراق (قاعدي)"), ("Eosin", "الإيوسين"), ("Dehydrate, clear, mount", "نزع الماء، ترويق، تحميل")],
      en="H&E in order", ar="H&E بالترتيب"),
 BN("Clearing is usually done with **xylene**, and the coverslip is fixed with a mounting medium (e.g. DPX); in many labs a quick **acid-alcohol differentiation** removes excess hematoxylin before bluing.",
    "يُجرى الترويق عادةً بـ**الزايلين**، وتُثبّت الساترة بوسط تحميل (مثل `DPX`)؛ وفي مختبرات كثيرة يُستعمل **تمييز سريع بالكحول الحامضي** لإزالة الهيماتوكسلين الزائد قبل الإزراق."),
 INSHORT([("Order: **section → hematoxylin → rinse → bluing → eosin → dehydrate, clear, mount**.", "الترتيب: **مقطع ← هيماتوكسلين ← شطف ← إزراق ← إيوسين ← نزع الماء والترويق والتحميل**."),
          ("**Bluing** = weak alkali (**ammonia water / Scott's tap water**) → permanent crisp blue.", "**الإزراق** = قاعدي ضعيف (**ماء الأمونيا / ماء سكوت**) ← أزرق دائم واضح.")]),

 # ───────────────────────── 5
 SEC("The Final Result", "النتيجة النهائية"),
 C(["**The Final Result: A Diagnostic Picture**", "Under the microscope, an H&E-stained slide provides a classic and highly informative **color contrast**:"],
   ["**النتيجة النهائية: صورة تشخيصية**", "تحت المجهر تعطي الشريحة المصبوغة بـ `H&E` **تباينًا لونيًا** تقليديًا وغنيًا بالمعلومات:"]),
 L(["**Nuclei**: Dark Blue/Purple", "**Cytoplasm & Connective Tissue**: Pink", "**Muscle Fibers**: Deeper Pink", "**Red Blood Cells**: Bright Orange/Red"],
   ["**الأنوية**: أزرق داكن/بنفسجي", "**السايتوبلازم والنسيج الضامّ**: وردي", "**الألياف العضلية**: وردي أغمق", "**كريات الدم الحمر**: برتقالي/أحمر لامع"]),
 F("muscle-pink.png", "Muscle Fibers: Deeper Pink", "الألياف العضلية: وردي أغمق", h="40mm"),
 BN("The pictures on the result slides are the same ones shown above: nuclei (after bluing), cytoplasm & connective tissue (kidney glomerulus), and red blood cells.",
    "صور شرائح النتيجة هي نفسها المعروضة أعلاه: الأنوية (بعد الإزراق)، والسايتوبلازم والنسيج الضامّ (كبيبة الكلية)، وكريات الدم الحمر."),
 T([B("Structure", "التركيب"), B("H&E colour", "اللون في H&E")],
   [[B("**Nuclei**", "**الأنوية**"), B("dark blue / purple", "أزرق داكن / بنفسجي")],
    [B("**Cytoplasm & connective tissue**", "**السايتوبلازم والنسيج الضامّ**"), B("pink", "وردي")],
    [B("**Muscle fibers**", "**الألياف العضلية**"), B("deeper pink", "وردي أغمق")],
    [B("**Red blood cells**", "**كريات الدم الحمر**"), B("bright orange / red", "برتقالي / أحمر لامع")]],
   key_cols=[0], widths=[50, 50], style="summary", label_en="Colours to remember", label_ar="ألوان للحفظ"),
] + TERMS([
 ("Hematoxylin and eosin (H&E)", "الهيماتوكسلين والإيوسين"),
 ("Gold standard", "المعيار الذهبي"),
 ("Logwood tree (Haematoxylum campechianum)", "شجرة البقّم / خشب الكامبيش"),
 ("Basic dye / acidic dye", "صبغة قاعدية / صبغة حامضية"),
 ("Basophilic / acidophilic (eosinophilic)", "محبّ للقاعدة / محبّ للحامض (للإيوسين)"),
 ("Rough endoplasmic reticulum", "الشبكة الإندوبلازمية الخشنة"),
 ("Cartilage", "الغضروف"),
 ("Keratin", "الكيراتين"),
 ("Section", "المقطع النسيجي"),
 ("Rinsing", "الشطف / الغسل"),
 ("Bluing", "الإزراق / التزريق"),
 ("Scott's tap water", "ماء سكوت (محلول الإزراق)"),
 ("Dehydration", "نزع الماء"),
 ("Clearing", "الترويق"),
 ("Mounting / coverslip", "التحميل / الساترة (غطاء الشريحة)"),
])

IMG = lambda f, h="34mm": dict(img="assets/" + f, img_h=h)
mcq = [
 {"topic_en": "H&E, hematoxylin and eosin", "topic_ar": "H&E والهيماتوكسلين والإيوسين"},
 Q("H&E staining is described as:", "يُوصف التصبيغ بـ H&E بأنه:", O(("The gold standard for histological examination", "المعيار الذهبي للفحص النسيجي"), ("A special stain for fat", "صبغة خاصة للدهون"), ("A stain for bacteria only", "صبغة للبكتيريا فقط"), ("A rarely used stain", "صبغة نادرة الاستعمال")), "a"),
 Q("What percentage of tissue diagnostics start with an H&E stain?", "ما نسبة التشخيصات النسيجية التي تبدأ بـ H&E؟", O(("Under 20%", "أقل من 20%"), ("Over 80%", "أكثر من 80%"), ("About 50%", "نحو 50%"), ("10%", "10%")), "b"),
 Q("Hematoxylin is derived from:", "يُستخلص الهيماتوكسلين من:", O(("Sea water", "ماء البحر"), ("Bacteria", "البكتيريا"), ("The logwood tree", "شجرة البقّم"), ("Petroleum", "النفط")), "c"),
 Q("Hematoxylin is a:", "الهيماتوكسلين:", O(("Acidic dye", "صبغة حامضية"), ("Metal salt", "ملح معدني"), ("Fixative", "مثبّت نسيجي"), ("Basic dye", "صبغة قاعدية")), "d"),
 Q("Hematoxylin colours its targets:", "يلوّن الهيماتوكسلين أهدافه بـ:", O(("Bluish-purple or dark blue", "بنفسجي مزرق أو أزرق داكن"), ("Pink", "وردي"), ("Orange", "برتقالي"), ("Yellow", "أصفر")), "a"),
 Q("Which is a target of hematoxylin?", "أيّها من أهداف الهيماتوكسلين؟", O(("Keratin", "الكيراتين"), ("Cartilage", "الغضروف"), ("Collagen", "الكولاجين"), ("Red blood cells", "كريات الدم الحمر")), "b"),
 Q("The nucleus takes hematoxylin because:", "تأخذ النواة الهيماتوكسلين لأن:", O(("It has keratin", "فيها كيراتين"), ("It is basic", "قاعدية"), ("DNA/RNA is acidic", "DNA/RNA حامضي"), ("It has collagen", "فيها كولاجين")), "c"),
 Q("Eosin colours its targets:", "يلوّن الإيوسين أهدافه بـ:", O(("Dark blue", "أزرق داكن"), ("Black", "أسود"), ("Green", "أخضر"), ("Pink, red or orange", "وردي أو أحمر أو برتقالي")), "d"),
 Q("Which is NOT a target of eosin?", "أيّها ليس من أهداف الإيوسين؟", O(("Cell nucleus", "نواة الخلية"), ("Cytoplasm", "السايتوبلازم"), ("Collagen", "الكولاجين"), ("Keratin", "الكيراتين")), "a"),
 Q("Structures that take the basic dye hematoxylin are correctly called:", "التراكيب التي تأخذ الصبغة القاعدية (الهيماتوكسلين) تُسمّى صحيحًا:", O(("Acidophilic", "محبّة للحامض"), ("Basophilic", "محبّة للقاعدة"), ("Eosinophilic", "محبّة للإيوسين"), ("Neutrophilic", "متعادلة")), "b"),
 {"topic_en": "The staining process", "topic_ar": "خطوات التصبيغ"},
 Q("The first step of the H&E process is:", "الخطوة الأولى في H&E:", O(("Eosin", "الإيوسين"), ("Bluing", "الإزراق"), ("Tissue preparation (section on a glass slide)", "تحضير النسيج (مقطع على شريحة)"), ("Mounting", "التحميل")), "c"),
 Q("After hematoxylin, excess dye is removed by:", "بعد الهيماتوكسلين تُزال الصبغة الزائدة بـ:", O(("Eosin", "الإيوسين"), ("Bluing", "الإزراق"), ("Mounting", "التحميل"), ("Rinsing", "الشطف")), "d"),
 Q("Bluing uses:", "يستعمل الإزراق:", O(("A weak alkaline solution", "محلولًا قاعديًا ضعيفًا"), ("A strong acid", "حامضًا قويًا"), ("Eosin", "الإيوسين"), ("Xylene only", "الزايلين فقط")), "a"),
 Q("An example of a bluing solution is:", "مثال على محلول الإزراق:", O(("Picric acid", "حامض البكريك"), ("Scott's tap water", "ماء سكوت"), ("Formalin", "الفورمالين"), ("Eosin Y", "الإيوسين Y")), "b"),
 Q("Bluing turns hematoxylin:", "يحوّل الإزراق الهيماتوكسلين إلى:", O(("Pink", "وردي"), ("Colorless", "عديم اللون"), ("A permanent, crisp blue", "أزرق دائم واضح"), ("Red", "أحمر")), "c"),
 Q("Eosin stains the cytoplasmic and extracellular components:", "يصبغ الإيوسين المكوّنات السايتوبلازمية وخارج الخلوية بالـ:", O(("Blue", "أزرق"), ("Black", "أسود"), ("Purple", "بنفسجي"), ("Pink", "وردي")), "d"),
 Q("Before sealing with a coverslip, the slide is:", "قبل تغطيتها بالساترة تُ:", O(("Dehydrated through alcohols and cleared", "نُزع منها الماء بالكحولات وتُروَّق"), ("Boiled", "تُغلى"), ("Frozen", "تُجمّد"), ("Stained with Gram", "تُصبغ بغرام")), "a"),
 Q("The correct order is:", "الترتيب الصحيح:", O(("Eosin → hematoxylin → bluing", "إيوسين ← هيماتوكسلين ← إزراق"), ("Hematoxylin → rinse → bluing → eosin", "هيماتوكسلين ← شطف ← إزراق ← إيوسين"), ("Bluing → hematoxylin → eosin", "إزراق ← هيماتوكسلين ← إيوسين"), ("Mounting → hematoxylin → eosin", "تحميل ← هيماتوكسلين ← إيوسين")), "b"),
 {"topic_en": "The final result", "topic_ar": "النتيجة النهائية"},
 Q("In H&E, nuclei appear:", "في H&E تظهر الأنوية:", O(("Pink", "وردية"), ("Orange", "برتقالية"), ("Dark blue/purple", "زرقاء داكنة/بنفسجية"), ("Yellow", "صفراء")), "c"),
 Q("In H&E, muscle fibers appear:", "في H&E تظهر الألياف العضلية:", O(("Dark blue", "زرقاء داكنة"), ("Colorless", "عديمة اللون"), ("Black", "سوداء"), ("Deeper pink", "وردية أغمق")), "d"),
 Q("In H&E, red blood cells appear:", "في H&E تظهر كريات الدم الحمر:", O(("Bright orange/red", "برتقالية/حمراء لامعة"), ("Blue", "زرقاء"), ("Purple", "بنفسجية"), ("Green", "خضراء")), "a"),
 Q("Cytoplasm and connective tissue in H&E are:", "السايتوبلازم والنسيج الضامّ في H&E:", O(("Dark blue", "أزرق داكن"), ("Pink", "وردي"), ("Black", "أسود"), ("Magenta", "أرجواني")), "b"),
 {"topic_en": "Picture questions", "topic_ar": "أسئلة الصور"},
 Q("This picture shows which hematoxylin target?", "تُظهر هذه الصورة أيّ هدف للهيماتوكسلين؟", O(("Keratin", "الكيراتين"), ("Red blood cells", "كريات الدم الحمر"), ("Articular cartilage", "الغضروف المفصلي"), ("Collagen", "الكولاجين")), "c", **IMG("knee-cartilage.png")),
 Q("The pink colour of this kidney section is given by:", "اللون الوردي في مقطع الكلية هذا تعطيه:", O(("Hematoxylin", "الهيماتوكسلين"), ("Scott's tap water", "ماء سكوت"), ("Silver", "الفضّة"), ("Eosin", "الإيوسين")), "d", **IMG("eosin-glomerulus.png")),
]
mcq = balance(mcq, 66)

tf = [
 TF("H&E is the gold standard for histological examination.", "H&E هي المعيار الذهبي للفحص النسيجي.", "T"),
 TF("Hematoxylin is an acidic dye.", "الهيماتوكسلين صبغة حامضية.", "F"),
 TF("Hematoxylin is derived from the logwood tree.", "يُستخلص الهيماتوكسلين من شجرة البقّم.", "T"),
 TF("Rough endoplasmic reticulum is a target of hematoxylin.", "الشبكة الإندوبلازمية الخشنة من أهداف الهيماتوكسلين.", "T"),
 TF("Eosin stains the nucleus dark blue.", "يصبغ الإيوسين النواة بالأزرق الداكن.", "F"),
 TF("Keratin is a target of eosin.", "الكيراتين من أهداف الإيوسين.", "T"),
 TF("Bluing uses a weak alkaline solution such as ammonia water.", "يستعمل الإزراق محلولًا قاعديًا ضعيفًا مثل ماء الأمونيا.", "T"),
 TF("Bluing is done after eosin.", "يُجرى الإزراق بعد الإيوسين.", "F"),
 TF("Rinsing washes off excess dye.", "يغسل الشطف الصبغة الزائدة.", "T"),
 TF("The slide is dehydrated through alcohols, cleared and sealed with a coverslip.", "تُنزع المياه من الشريحة بالكحولات وتُروَّق وتُغطّى بساترة.", "T"),
 TF("In H&E, red blood cells appear dark blue.", "في H&E تظهر كريات الدم الحمر زرقاء داكنة.", "F"),
 TF("Muscle fibers appear deeper pink than cytoplasm.", "تظهر الألياف العضلية وردية أغمق من السايتوبلازم.", "T"),
]

traps = [
 TR("Basophilic vs acidophilic (the slide's wording)", "محبّ للقاعدة مقابل محبّ للحامض (صياغة الشريحة)", "Hematoxylin (basic) stains ACIDIC structures → called BASOPHILIC; eosin (acidic) stains BASIC structures → called ACIDOPHILIC/eosinophilic. The slides write the opposite words in brackets.", "الهيماتوكسلين (قاعدي) يصبغ التراكيب الحامضية ← تُسمّى محبّة للقاعدة؛ والإيوسين (حامضي) يصبغ التراكيب القاعدية ← تُسمّى محبّة للحامض/للإيوسين. والشرائح كتبت الكلمتين بالعكس بين القوسين."),
 TR("Bluing comes before eosin", "الإزراق قبل الإيوسين", "Order: hematoxylin → rinse → BLUING → eosin → dehydrate/clear/mount.", "الترتيب: هيماتوكسلين ← شطف ← إزراق ← إيوسين ← نزع الماء/ترويق/تحميل."),
 TR("Bluing solution is alkaline", "محلول الإزراق قاعدي", "Bluing = WEAK ALKALINE (ammonia water, Scott's tap water) — not acid.", "الإزراق = قاعدي ضعيف (ماء الأمونيا، ماء سكوت) — لا حامض."),
 TR("Cartilage colour", "لون الغضروف", "Cartilage matrix is a HEMATOXYLIN target (blue), while collagen is an EOSIN target (pink).", "حشوة الغضروف من أهداف الهيماتوكسلين (أزرق)، بينما الكولاجين من أهداف الإيوسين (وردي)."),
 TR("Two shades of pink", "درجتان من الوردي", "Cytoplasm & connective tissue = pink; muscle fibers = DEEPER pink; RBCs = bright orange/red.", "السايتوبلازم والنسيج الضامّ = وردي؛ والألياف العضلية = وردي أغمق؛ وكريات الدم الحمر = برتقالي/أحمر لامع."),
 TR("RER is blue", "الشبكة الإندوبلازمية الخشنة زرقاء", "RER (ribosomes, RNA) is a hematoxylin target, even though it is in the cytoplasm.", "الشبكة الإندوبلازمية الخشنة (رايبوسومات، RNA) من أهداف الهيماتوكسلين مع أنها في السايتوبلازم."),
]

important = [
 IM("What is H&E staining and why is it important?", "ما التصبيغ بـ H&E ولماذا هو مهم؟",
    "Hematoxylin and Eosin staining — the gold standard for histological examination, used to visualize tissue structure under a microscope; over 80% of all tissue diagnostics start with an H&E stain.",
    "التصبيغ بالهيماتوكسلين والإيوسين — المعيار الذهبي للفحص النسيجي، ويُستعمل لإظهار بنية النسيج تحت المجهر؛ وأكثر من 80% من التشخيصات النسيجية تبدأ به."),
 IM("Compare hematoxylin and eosin (type, what they stain, colour, targets).", "قارن بين الهيماتوكسلين والإيوسين (النوع، وما تصبغ، واللون، والأهداف).",
    "Hematoxylin: basic dye from the logwood tree; stains acidic structures bluish-purple/dark blue; targets nucleus (acidic DNA/RNA), RER, cartilage. Eosin: acidic dye; stains basic structures pink/red/orange; targets cytoplasm, muscle fibers, collagen, RBCs, keratin.",
    "الهيماتوكسلين: صبغة قاعدية من شجرة البقّم؛ تصبغ التراكيب الحامضية بنفسجيًا مزرقًّا/أزرق داكنًا؛ أهدافها النواة (DNA/RNA حامضي) والشبكة الإندوبلازمية الخشنة والغضروف. الإيوسين: صبغة حامضية؛ تصبغ التراكيب القاعدية وردي/أحمر/برتقالي؛ أهدافها السايتوبلازم والألياف العضلية والكولاجين وكريات الدم الحمر والكيراتين."),
 IM("Describe the H&E staining process.", "صف خطوات التصبيغ بـ H&E.",
    "1. Tissue preparation: thin section mounted on a glass slide. 2. Hematoxylin: nuclei dark blue. 3. Rinsing: excess dye washed off. 4. Bluing: weak alkaline solution (ammonia water or Scott's tap water) → permanent crisp blue. Eosin: cytoplasmic and extracellular components pink. Dehydration through alcohols, clearing and mounting with a coverslip.",
    "1. تحضير النسيج: مقطع رقيق على شريحة زجاجية. 2. الهيماتوكسلين: الأنوية زرقاء داكنة. 3. الشطف: غسل الصبغة الزائدة. 4. الإزراق: محلول قاعدي ضعيف (ماء الأمونيا أو ماء سكوت) ← أزرق دائم واضح. الإيوسين: المكوّنات السايتوبلازمية وخارج الخلوية وردية. نزع الماء بالكحولات والترويق والتحميل بالساترة."),
 IM("What is bluing and why is it done?", "ما الإزراق ولماذا يُجرى؟",
    "Placing the section in a weak alkaline solution (ammonia water or Scott's tap water) after hematoxylin and rinsing, to turn the hematoxylin a permanent, crisp blue colour.",
    "وضع المقطع في محلول قاعدي ضعيف (ماء الأمونيا أو ماء سكوت) بعد الهيماتوكسلين والشطف، لتحويل الهيماتوكسلين إلى لون أزرق دائم واضح."),
 IM("Give the colour of each structure in an H&E-stained slide.", "اذكر لون كل تركيب في شريحة مصبوغة بـ H&E.",
    "Nuclei: dark blue/purple. Cytoplasm & connective tissue: pink. Muscle fibers: deeper pink. Red blood cells: bright orange/red.",
    "الأنوية: أزرق داكن/بنفسجي. السايتوبلازم والنسيج الضامّ: وردي. الألياف العضلية: وردي أغمق. كريات الدم الحمر: برتقالي/أحمر لامع."),
]

meta = {"subject_en": "Histopathology", "subject_ar": "علم الأمراض النسيجية", "short_ar": "انسجة", "instructor": "م.م. آية وسمي",
        "unit_en": "Lab 6", "unit_ar": "العملي 6", "unit_label": "LAB", "unit_no": "6",
        "title_en": "The hematoxylins and eosin", "title_ar": "الهيماتوكسلين والإيوسين",
        "kind": "Laboratories — عملي", "stage": "The third stage — الثالثة"}
blocks, mcq, tf, traps, important = ltr_all(blocks), ltr_all(mcq), ltr_all(tf), ltr_all(traps), ltr_all(important)
save("histopathology-lab6-he-stain", meta, blocks, mcq, tf, traps, important)
fit("histopathology-lab6-he-stain", min_gap=0.08)   # no big gaps, small ones too

```
