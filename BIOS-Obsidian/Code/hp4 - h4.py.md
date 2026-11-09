---
source: BIOS-Obsidian/tools/scripts/hp4/h4.py
handouts: [histopathology-lab4-microtome]
saved: 2026-11-09
tags: [bios, code]
---
# hp4/h4.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#histopathology-lab4-microtome|histopathology-lab4-microtome]]

```python
import sys; sys.path.insert(0, "/tmp/claude-0/-home-user--/67d83c9a-7b0e-5ae5-b52b-cd659ab074ab/scratchpad/imm456")
from ci import *            # c helpers + B INSHORT TERMS balance save(split.fix)
sys.path.insert(0, "/tmp/claude-0/-home-user--/67d83c9a-7b0e-5ae5-b52b-cd659ab074ab/scratchpad"); from bidi import ltr_all; from flowfit import fit

# Histopathology practical, lab 4 (user) — "Microtome for paraffin and frozen sections" (23 slides, 14 pictures, no questions).
# The title slide says "LAB 3" (lab 3 is tissue processing) — numbered 4 as the user said. "By: M.S.C AYA WESMII".
split.ABBR = split.ABBR + ("M.S.C",)
BN = lambda en, ar: N(en, ar, label=["BIOS note", "ملاحظة BIOS"])
O = P

blocks = [
 # ───────────────────────── 1
 SEC("What is Microtomy?", "ما هي المقطعية (القطع الدقيق)؟"),
 N("By: M.S.C AYA WESMII", "إعداد: م.م. آية وسمي", label=["Lab sheet", "ورقة العملي"]),
 BN("The title slide of this file says **\"LAB 3\"**, but lab 3 is *Tissue processing*; this lab (microtome) is numbered **4** as the lab sequence follows.",
    "شريحة العنوان في هذا الملف مكتوب فيها **\"LAB 3\"**، لكن العملي 3 هو *تحضير النسيج*؛ لذلك رُقّم هذا العملي (المشراح) **4** حسب تسلسل العمليات."),
 C(["**Microtomy** is the technique of preparing **extremely thin sections** of biological tissues, plants, or materials using a specialized instrument called a **microtome**.",
    "These thin sections, typically only **a few micrometers thick** (1 µm = 1/1000 of a millimeter), are then mounted on glass slides and stained to be examined under a light or electron microscope."],
   ["**المقطعية (القطع الدقيق)** تقنية تحضير **مقاطع رقيقة جدًا** من الأنسجة الحيوية أو النباتات أو المواد باستعمال جهاز متخصّص يُسمّى **المِشراح (المايكروتوم)**.",
    "وهذه المقاطع الرقيقة، التي يبلغ سمكها عادةً **بضعة مايكرومترات** (`1 µm = 1/1000` من المليمتر)، تُحمَّل بعد ذلك على شرائح زجاجية وتُصبغ لتُفحص تحت المجهر الضوئي أو الإلكتروني."]),
 C("The **primary goal** of microtomy is to **allow light or electrons to pass through the specimen**, making its internal structures visible and enabling detailed histological, pathological, or cytological analysis.",
   "و**الهدف الرئيس** من المقطعية **السماح للضوء أو الإلكترونات بالمرور عبر العيّنة**، فتصبح تراكيبها الداخلية مرئية ويمكن تحليلها نسيجيًا أو مرضيًا أو خلويًا بالتفصيل."),
 L(["**Base & Clamp**: A heavy, stable base to **prevent vibration**, and a clamp to **hold the specimen block** firmly in place.",
    "**Knife Holder**: A mount for the cutting blade (**steel, glass, or diamond**).",
    "**Specimen Feed Mechanism**: An extremely precise mechanism (manual or automatic) that **advances the specimen block** a specific distance (e.g., 4 µm, 5 µm) towards the knife after each cutting stroke. This determines the **thickness of the section**.",
    "**Cutting Window/Arm**: The part that the user moves to perform the cutting stroke."],
   ["**القاعدة والمِلزمة**: قاعدة ثقيلة ثابتة **لمنع الاهتزاز**، ومِلزمة **لتثبيت قالب العيّنة** بإحكام.",
    "**حامل السكّين**: مثبّت لشفرة القطع (**فولاذ أو زجاج أو ماس**).",
    "**آلية تغذية العيّنة**: آلية دقيقة جدًا (يدوية أو آلية) **تُقدّم قالب العيّنة** مسافة محدّدة (مثل 4 أو 5 مايكرومتر) نحو السكّين بعد كل ضربة قطع. وهي التي تحدّد **سُمك المقطع**.",
    "**نافذة/ذراع القطع**: الجزء الذي يحرّكه المستعمل لإجراء ضربة القطع."],
   en=["A microtome is a **precision cutting tool**.", "While designs vary, all microtomes consist of a few **key components**:"],
   ar=["المِشراح **أداة قطع دقيقة**.", "ومع اختلاف تصاميمه، تتكوّن كل المشاريح من بضعة **مكوّنات أساسية**:"]),
 F("microtome-labels.png", "Microtome parts: Block holder, Blade, Stage, Automated microtome setting", "أجزاء المِشراح: حامل القالب، والشفرة، والمنصّة، وضبط المِشراح الآلي", h="48mm"),
 INSHORT([("Microtomy = **very thin sections** (few µm) with a **microtome** → light passes → structures visible.", "المقطعية = **مقاطع رقيقة جدًا** (بضعة مايكرومترات) بالمِشراح ← يمرّ الضوء ← تظهر التراكيب."),
          ("4 parts: **base & clamp, knife holder, specimen feed (sets thickness), cutting arm**.", "4 أجزاء: **القاعدة والمِلزمة، وحامل السكّين، وآلية التغذية (تحدّد السُمك)، وذراع القطع**.")]),

 # ───────────────────────── 2
 SEC("Types of Microtomes", "أنواع المشاريح"),
 C("Different microtomes are used for different types of specimens and embedding media:", "تُستعمل مشاريح مختلفة لأنواع مختلفة من العيّنات وأوساط الطمر:"),
 H2("1. Rotary Microtome", "1. المِشراح الدوّار"),
 C("The **most common type** in histology and pathology labs.", "**النوع الأكثر شيوعًا** في مختبرات الأنسجة والأمراض."),
 L(["**How it works**: The specimen block is **moved vertically past a stationary knife** in a rotary motion of a **handwheel**.",
    "**Best for**: Producing **large numbers of thin, serial sections (2-10 µm)** from **paraffin-embedded** tissues."],
   ["**كيف يعمل**: يتحرّك قالب العيّنة **عموديًا أمام سكّين ثابتة** بحركة دوّارة من **عجلة اليد**.",
    "**الأنسب لـ**: إنتاج **أعداد كبيرة من المقاطع الرقيقة المتسلسلة (2–10 مايكرومتر)** من الأنسجة **المطمورة بالبرافين**."]),
 F("rotary.png", "Rotary Microtome", "المِشراح الدوّار", h="40mm"),
 H2("2- Cryostat (Freezing Microtome)", "2. الكرايوستات (المِشراح التجميدي)"),
 L(["**How it works**: A **rotary microtome housed in a refrigerated chamber** (typically **-15°C to -30°C**).",
    ["**Best for**: Cutting **frozen tissue sections**.", "Tissues are frozen and embedded in a **freezing medium, not paraffin**.", "This is essential for:"]],
   ["**كيف يعمل**: **مِشراح دوّار داخل حجرة مبرّدة** (عادةً **من -15 إلى -30 °م**).",
    ["**الأنسب لـ**: قطع **مقاطع الأنسجة المجمّدة**.", "تُجمّد الأنسجة وتُطمر في **وسط تجميد لا في البرافين**.", "وهذا أساسي لـ:"]]),
 L(["**Rapid intra-operative diagnosis** (e.g., during surgery to determine if a tumor is cancerous).",
    "Demonstrating **lipids or enzymes** that would be **destroyed by hot paraffin** processing.",
    "**Immunohistochemistry** on sensitive antigens."],
   ["**التشخيص السريع أثناء العملية** (مثل تحديد هل الورم سرطاني أثناء الجراحة).",
    "إظهار **الدهون أو الإنزيمات** التي **يُتلفها البرافين الساخن** أثناء التحضير.",
    "**الكيمياء النسيجية المناعية** على المستضدّات الحسّاسة."]),
 FF(("cryostat.png", "Cryostat (Freezing Microtome)", "الكرايوستات (المِشراح التجميدي)", "42mm"), ("cryostat-chamber.png", "Inside the refrigerated chamber of a cryostat", "داخل الحجرة المبرّدة للكرايوستات", "42mm")),
 H2("3- Sledge Microtome", "3. المِشراح المنزلق"),
 L(["**How it works**: The specimen block is mounted on a **\"sledge\"** that **slides past a long, stationary knife**.",
    "**Best for**: Cutting **very large blocks or hard materials**, including **celloidin-embedded** tissues and some rigid plastics."],
   ["**كيف يعمل**: يُثبّت قالب العيّنة على **\"زلّاجة\"** **تنزلق أمام سكّين طويلة ثابتة**.",
    "**الأنسب لـ**: قطع **القوالب الكبيرة جدًا أو المواد الصلبة**، ومنها الأنسجة **المطمورة بالسيلويدين** وبعض البلاستيك الصلب."]),
 F("sledge.png", "Sledge Microtome", "المِشراح المنزلق", h="40mm"),
 H2("4- Ultramicrotome", "4. المِشراح الفائق الدقّة"),
 L(["**How it works**: An extremely precise microtome that uses a **glass or diamond knife** to cut sections in a **fluid-filled trough (a \"boat\")**.",
    ["**Best for**: Preparing **ultra-thin sections (50-100 nanometers)** for **Transmission Electron Microscopy (TEM)**.", "The sections are so thin they must be collected on small **copper grids**."]],
   ["**كيف يعمل**: مِشراح دقيق جدًا يستعمل **سكّينًا زجاجية أو ماسية** لقطع المقاطع في **حوض مملوء بسائل (\"قارب\")**.",
    ["**الأنسب لـ**: تحضير **مقاطع فائقة الرقّة (50–100 نانومتر)** لـ**المجهر الإلكتروني النافذ (`TEM`)**.", "والمقاطع رقيقة جدًا لدرجة أنها تُجمع على **شبكات نحاسية** صغيرة."]]),
 F("ultramicrotome.png", "Ultramicrotome", "المِشراح الفائق الدقّة", h="40mm"),
 H2("5- Vibratome (Vibrating Microtome)", "5. الفايبراتوم (المِشراح الاهتزازي)"),
 L(["**How it works**: Uses a **vibrating blade** to cut through tissue. The tissue is **not frozen or embedded in paraffin**; it is simply **submerged in a buffer solution**.",
    "**Best for**: Cutting **fresh, unfixed, or lightly fixed** tissues. It **preserves cell viability and antigenicity** better than other methods but produces **thicker sections (30-500 µm)**."],
   ["**كيف يعمل**: يستعمل **شفرة مهتزّة** لقطع النسيج. والنسيج **غير مجمّد ولا مطمور بالبرافين**؛ بل **مغمور في محلول دارئ** فقط.",
    "**الأنسب لـ**: قطع الأنسجة **الطازجة أو غير المثبّتة أو المثبّتة تثبيتًا خفيفًا**. وهو **يحافظ على حيوية الخلايا ومستضدّيتها** أفضل من الطرائق الأخرى لكنه يعطي **مقاطع أسمك (30–500 مايكرومتر)**."]),
 F("vibratome.png", "Vibratome (Vibrating Microtome)", "الفايبراتوم (المِشراح الاهتزازي)", h="40mm"),
 T([B("Microtome", "المِشراح"), B("How it cuts", "كيف يقطع"), B("Section thickness", "سُمك المقطع"), B("Best for", "الأنسب لـ")],
   [[B("**Rotary**", "**الدوّار**"), B("block moves vertically past a stationary knife (handwheel)", "القالب يتحرّك عموديًا أمام سكّين ثابتة (عجلة يد)"), B("2–10 µm", "2–10 مايكرومتر"), B("paraffin, serial sections", "البرافين، مقاطع متسلسلة")],
    [B("**Cryostat**", "**الكرايوستات**"), B("rotary microtome in a cold chamber (-15 to -30 °C)", "مِشراح دوّار في حجرة باردة (-15 إلى -30 °م)"), B("frozen sections", "مقاطع مجمّدة"), B("intra-operative diagnosis, lipids, enzymes, IHC", "التشخيص أثناء العملية، والدهون، والإنزيمات، والكيمياء المناعية")],
    [B("**Sledge**", "**المنزلق**"), B("block on a sledge slides past a long stationary knife", "قالب على زلّاجة ينزلق أمام سكّين طويلة ثابتة"), B("—", "—"), B("very large / hard blocks, celloidin", "قوالب كبيرة جدًا / صلبة، السيلويدين")],
    [B("**Ultramicrotome**", "**الفائق الدقّة**"), B("glass or diamond knife, fluid-filled boat", "سكّين زجاجية أو ماسية، قارب سائل"), B("50–100 nm", "50–100 نانومتر"), B("TEM (copper grids)", "المجهر الإلكتروني النافذ (شبكات نحاسية)")],
    [B("**Vibratome**", "**الاهتزازي**"), B("vibrating blade, tissue in buffer", "شفرة مهتزّة، النسيج في دارئ"), B("30–500 µm", "30–500 مايكرومتر"), B("fresh / unfixed tissue, viability, antigenicity", "نسيج طازج / غير مثبّت، الحيوية والمستضدّية")]],
   key_cols=[0], widths=[18, 34, 18, 30], style="summary", label_en="BIOS: the 5 microtomes", label_ar="BIOS: المشاريح الخمسة"),
 INSHORT([("**Rotary** = most common, paraffin, 2–10 µm; **cryostat** = frozen, -15 to -30 °C.", "**الدوّار** = الأشيع، برافين، 2–10 مايكرومتر؛ و**الكرايوستات** = مجمّد، -15 إلى -30 °م."),
          ("**Sledge** = large/hard blocks; **ultramicrotome** = 50–100 nm for TEM; **vibratome** = fresh tissue, 30–500 µm.", "**المنزلق** = قوالب كبيرة/صلبة؛ و**الفائق الدقّة** = 50–100 نانومتر للمجهر الإلكتروني؛ و**الاهتزازي** = نسيج طازج، 30–500 مايكرومتر.")]),

 # ───────────────────────── 3
 SEC("Cutting the sections", "قطع المقاطع"),
 L(["The **block is secured** in the microtome.", "A **sharp microtome knife or disposable blade** is installed.", "The **thickness is set** (e.g., **4-5 µm**).",
    "The user **rotates the handwheel** in a smooth, rhythmic motion.",
    "As sections are cut, the **static electricity** causes them to adhere to each other, forming a continuous **\"ribbon\" of serial sections**."],
   ["**يُثبّت القالب** في المِشراح.", "تُركّب **سكّين مِشراح حادّة أو شفرة تُستعمل مرّة واحدة**.", "**يُضبط السُمك** (مثل **4–5 مايكرومتر**).",
    "يُدير المستعمل **عجلة اليد** بحركة سلسة منتظمة.",
    "ومع قطع المقاطع تجعلها **الكهرباء الساكنة** تلتصق بعضها ببعض فتكوّن **\"شريطًا\" متصلًا من المقاطع المتسلسلة**."]),
 FF(("block-clamp.png", "The block secured in the clamp, facing the blade", "القالب مثبّت في المِلزمة مقابل الشفرة", "40mm"), ("handwheel.png", "The handwheel", "عجلة اليد", "40mm")),
 F("ribbon.png", "A ribbon of serial sections on the blade", "شريط من المقاطع المتسلسلة على الشفرة", h="42mm"),
 INSHORT([("Secure block → install blade → set **4–5 µm** → turn the handwheel → **ribbon** (static electricity).", "تثبيت القالب ← تركيب الشفرة ← ضبط **4–5 مايكرومتر** ← إدارة العجلة ← **شريط** (كهرباء ساكنة).")]),

 # ───────────────────────── 4
 SEC("Float-out, mounting and staining", "التعويم والتحميل والتصبيغ"),
 H2("Float-Out Bath:", "حمّام التعويم:"),
 L(["The ribbon is carefully manipulated with a **brush or forceps** and floated on a **warm water bath** (usually **5-10°C below the melting point of the paraffin**).",
    "The **warmth relaxes the sections**, removing **wrinkles and folds**."],
   ["يُحرَّك الشريط بعناية بـ**فرشاة أو ملقط** ويُعوَّم على **حمّام ماء دافئ** (عادةً **أقل من درجة انصهار البرافين بـ 5–10 °م**).",
    "و**الدفء يُرخي المقاطع** فيزيل **التجاعيد والطيّات**."]),
 F("float-bath.png", "Float-out water bath", "حمّام التعويم المائي", h="40mm"),
 H2("Mounting:", "التحميل:"),
 L(["A glass microscope slide is **submerged under the floating section**.", "The section is carefully **\"fished\" out onto the slide** and positioned.",
    "The slide is **drained and dried in an oven** to firmly adhere the section to the glass."],
   ["تُغمر شريحة مجهرية زجاجية **تحت المقطع العائم**.", "يُ**\"صاد\" المقطع** بعناية على الشريحة ويُعدّل موضعه.",
    "تُصفّى الشريحة **وتُجفّف في الفرن** ليلتصق المقطع بالزجاج بإحكام."]),
 FF(("fishing.png", "Fishing the section onto the slide", "صيد المقطع على الشريحة", "40mm"), ("slide-sections.png", "Sections mounted on the slide", "مقاطع محمّلة على الشريحة", "40mm")),
 C("**Staining**: The slide is then processed through stains (like **Hematoxylin and Eosin - H&E**) to visualize cellular components.",
   "**التصبيغ**: ثم تُمرَّر الشريحة عبر الصبغات (مثل **الهيماتوكسلين والإيوسين – `H&E`**) لإظهار مكوّنات الخلايا."),
 F("he-section.png", "H&E-stained section", "مقطع مصبوغ بـ `H&E`", h="40mm"),
 FLOW([("Ribbon", "الشريط"), ("Warm water bath", "حمّام ماء دافئ"), ("Fish onto slide", "صيد على الشريحة"), ("Drain & oven-dry", "تصفية وتجفيف بالفرن"), ("Stain (H&E)", "تصبيغ (H&E)")],
      en="After cutting", ar="بعد القطع"),
 INSHORT([("Float-out: **warm water 5–10 °C below paraffin melting point** → removes wrinkles.", "التعويم: **ماء دافئ أقل من انصهار البرافين بـ 5–10 °م** ← يزيل التجاعيد."),
          ("Mounting: slide **under** the section → fish out → **drain and oven-dry** → stain (H&E).", "التحميل: الشريحة **تحت** المقطع ← صيده ← **تصفية وتجفيف بالفرن** ← تصبيغ (`H&E`).")]),
] + TERMS([
 ("Microtomy / microtome", "المقطعية (القطع الدقيق) / المِشراح (المايكروتوم)"),
 ("Section", "المقطع"),
 ("Micrometer (µm) / nanometer (nm)", "مايكرومتر / نانومتر"),
 ("Clamp / knife holder", "المِلزمة / حامل السكّين"),
 ("Specimen feed mechanism", "آلية تغذية (تقديم) العيّنة"),
 ("Rotary microtome", "المِشراح الدوّار"),
 ("Handwheel", "عجلة اليد"),
 ("Serial sections / ribbon", "مقاطع متسلسلة / شريط"),
 ("Cryostat (freezing microtome)", "الكرايوستات / المِشراح التجميدي"),
 ("Intra-operative diagnosis", "التشخيص أثناء العملية الجراحية"),
 ("Immunohistochemistry", "الكيمياء النسيجية المناعية"),
 ("Sledge microtome", "المِشراح المنزلق"),
 ("Celloidin", "السيلويدين"),
 ("Ultramicrotome", "المِشراح الفائق الدقّة"),
 ("Transmission electron microscopy (TEM)", "المجهر الإلكتروني النافذ"),
 ("Copper grid", "شبكة نحاسية"),
 ("Vibratome", "الفايبراتوم / المِشراح الاهتزازي"),
 ("Float-out bath", "حمّام التعويم"),
 ("Mounting", "التحميل"),
])

IMG = lambda f, h="34mm": dict(img="assets/" + f, img_h=h)
mcq = [
 {"topic_en": "Microtomy and microtome parts", "topic_ar": "المقطعية وأجزاء المِشراح"},
 Q("Microtomy is the technique of preparing:", "المقطعية تقنية تحضير:", O(("Extremely thin sections with a microtome", "مقاطع رقيقة جدًا بالمِشراح"), ("Thick smears", "مسحات سميكة"), ("Culture media", "أوساط زرعية"), ("Blood films", "مسحات دموية")), "a"),
 Q("1 µm equals:", "المايكرومتر الواحد يساوي:", O(("1/10 mm", "1/10 ملم"), ("1/1000 of a millimeter", "1/1000 من المليمتر"), ("1 mm", "1 ملم"), ("1/100 mm", "1/100 ملم")), "b"),
 Q("The primary goal of microtomy is to:", "الهدف الرئيس من المقطعية:", O(("Kill bacteria", "قتل البكتيريا"), ("Freeze tissue", "تجميد النسيج"), ("Allow light or electrons to pass through the specimen", "السماح للضوء أو الإلكترونات بالمرور عبر العيّنة"), ("Stain the block", "تصبيغ القالب")), "c"),
 Q("The heavy base of the microtome is to:", "القاعدة الثقيلة للمِشراح من أجل:", O(("Heat the block", "تسخين القالب"), ("Cool the knife", "تبريد السكّين"), ("Cut faster", "القطع أسرع"), ("Prevent vibration", "منع الاهتزاز")), "d"),
 Q("The section thickness is determined by the:", "يحدّد سُمك المقطع:", O(("Specimen feed mechanism", "آلية تغذية العيّنة"), ("Base", "القاعدة"), ("Water bath", "حمّام الماء"), ("Oven", "الفرن")), "a"),
 Q("Microtome blades may be made of:", "قد تُصنع شفرات المِشراح من:", O(("Wood", "خشب"), ("Steel, glass or diamond", "فولاذ أو زجاج أو ماس"), ("Plastic only", "بلاستيك فقط"), ("Copper", "نحاس")), "b"),
 {"topic_en": "Types of microtomes", "topic_ar": "أنواع المشاريح"},
 Q("The most common microtome in histology labs is the:", "المِشراح الأكثر شيوعًا في مختبرات الأنسجة:", O(("Sledge", "المنزلق"), ("Ultramicrotome", "الفائق الدقّة"), ("Rotary microtome", "الدوّار"), ("Vibratome", "الاهتزازي")), "c"),
 Q("The rotary microtome produces serial sections of:", "يعطي المِشراح الدوّار مقاطع متسلسلة بسُمك:", O(("50–100 nm", "50–100 نانومتر"), ("30–500 µm", "30–500 مايكرومتر"), ("1 mm", "1 ملم"), ("2–10 µm", "2–10 مايكرومتر")), "d"),
 Q("A cryostat is a rotary microtome in a refrigerated chamber at:", "الكرايوستات مِشراح دوّار في حجرة مبرّدة بدرجة:", O(("-15 to -30 °C", "-15 إلى -30 °م"), ("0 to 4 °C", "0 إلى 4 °م"), ("37 °C", "37 °م"), ("-80 °C", "-80 °م")), "a"),
 Q("Rapid intra-operative diagnosis uses:", "التشخيص السريع أثناء العملية يستعمل:", O(("Ultramicrotome", "الفائق الدقّة"), ("Cryostat", "الكرايوستات"), ("Sledge microtome", "المنزلق"), ("Paraffin processing", "التحضير بالبرافين")), "b"),
 Q("Frozen sections are needed to demonstrate lipids and enzymes because:", "تُحتاج المقاطع المجمّدة لإظهار الدهون والإنزيمات لأن:", O(("They are cheaper", "أرخص"), ("They are thicker", "أسمك"), ("Hot paraffin processing would destroy them", "التحضير بالبرافين الساخن يُتلفها"), ("They need TEM", "تحتاج المجهر الإلكتروني")), "c"),
 Q("Celloidin-embedded tissues and very large hard blocks are cut with the:", "تُقطع الأنسجة المطمورة بالسيلويدين والقوالب الكبيرة الصلبة بـ:", O(("Vibratome", "الاهتزازي"), ("Cryostat", "الكرايوستات"), ("Ultramicrotome", "الفائق الدقّة"), ("Sledge microtome", "المنزلق")), "d"),
 Q("Ultra-thin sections for TEM (50–100 nm) are cut with the:", "المقاطع فائقة الرقّة للمجهر الإلكتروني (50–100 نانومتر) تُقطع بـ:", O(("Ultramicrotome", "الفائق الدقّة"), ("Rotary microtome", "الدوّار"), ("Sledge microtome", "المنزلق"), ("Vibratome", "الاهتزازي")), "a"),
 Q("Ultramicrotome sections are collected on:", "تُجمع مقاطع المِشراح الفائق الدقّة على:", O(("Glass slides", "شرائح زجاجية"), ("Copper grids", "شبكات نحاسية"), ("Filter paper", "ورق ترشيح"), ("Agar", "آغار")), "b"),
 Q("The vibratome cuts tissue that is:", "يقطع الفايبراتوم نسيجًا:", O(("Embedded in paraffin", "مطمورًا بالبرافين"), ("Frozen", "مجمّدًا"), ("Fresh, submerged in buffer", "طازجًا مغمورًا في دارئ"), ("Embedded in plastic", "مطمورًا بالبلاستيك")), "c"),
 Q("Vibratome sections are:", "مقاطع الفايبراتوم:", O(("50–100 nm", "50–100 نانومتر"), ("2–10 µm", "2–10 مايكرومتر"), ("4–5 µm", "4–5 مايكرومتر"), ("30–500 µm (thicker)", "30–500 مايكرومتر (أسمك)")), "d"),
 {"topic_en": "Cutting, float-out and mounting", "topic_ar": "القطع والتعويم والتحميل"},
 Q("The usual section thickness set in the lab is:", "السُمك المعتاد المضبوط في العملي:", O(("4–5 µm", "4–5 مايكرومتر"), ("50 µm", "50 مايكرومتر"), ("1 mm", "1 ملم"), ("100 nm", "100 نانومتر")), "a"),
 Q("Sections stick together into a ribbon because of:", "تلتصق المقاطع ببعضها في شريط بسبب:", O(("Glue", "الصمغ"), ("Static electricity", "الكهرباء الساكنة"), ("Water", "الماء"), ("Heat", "الحرارة")), "b"),
 Q("The float-out water bath temperature is usually:", "درجة حرارة حمّام التعويم عادةً:", O(("Boiling", "غليان"), ("Ice-cold", "مثلّج"), ("5–10 °C below the paraffin melting point", "أقل من انصهار البرافين بـ 5–10 °م"), ("Room temperature only", "حرارة الغرفة فقط")), "c"),
 Q("The warm water bath:", "حمّام الماء الدافئ:", O(("Stains the section", "يصبغ المقطع"), ("Freezes the section", "يجمّد المقطع"), ("Fixes the tissue", "يثبّت النسيج"), ("Relaxes the sections, removing wrinkles and folds", "يُرخي المقاطع ويزيل التجاعيد والطيّات")), "d"),
 Q("To mount a section, the slide is:", "لتحميل المقطع تُ:", O(("Submerged under the floating section and the section fished out", "غمر الشريحة تحت المقطع العائم ويُصاد المقطع"), ("Placed on top of the block", "وضع الشريحة فوق القالب"), ("Heated before cutting", "تسخين الشريحة قبل القطع"), ("Dipped in eosin", "غمس الشريحة في الإيوسين")), "a"),
 Q("After fishing, the slide is drained and:", "بعد الصيد تُصفّى الشريحة و:", O(("Frozen", "تُجمّد"), ("Dried in an oven", "تُجفّف في الفرن"), ("Washed with acid", "تُغسل بالحامض"), ("Cut again", "تُقطع ثانية")), "b"),
 {"topic_en": "Picture questions", "topic_ar": "أسئلة الصور"},
 Q("This instrument is a:", "هذا الجهاز:", O(("Sledge microtome", "مِشراح منزلق"), ("Water bath", "حمّام ماء"), ("Cryostat (freezing microtome)", "كرايوستات (مِشراح تجميدي)"), ("Oven", "فرن")), "c", **IMG("cryostat.png")),
 Q("This picture shows:", "تُظهر هذه الصورة:", O(("A float-out bath", "حمّام تعويم"), ("A handwheel", "عجلة يد"), ("An H&E section", "مقطعًا مصبوغًا بـ H&E"), ("A ribbon of serial sections on the blade", "شريطًا من المقاطع المتسلسلة على الشفرة")), "d", **IMG("ribbon.png")),
]
mcq = balance(mcq, 77)

tf = [
 TF("Microtomy sections are typically a few micrometers thick.", "يبلغ سمك مقاطع المقطعية عادةً بضعة مايكرومترات.", "T"),
 TF("The specimen feed mechanism determines the thickness of the section.", "تحدّد آلية تغذية العيّنة سُمك المقطع.", "T"),
 TF("The rotary microtome moves the knife past a stationary block.", "يحرّك المِشراح الدوّار السكّين أمام قالب ثابت.", "F"),
 TF("The cryostat cuts paraffin-embedded tissues.", "يقطع الكرايوستات الأنسجة المطمورة بالبرافين.", "F"),
 TF("Frozen sections are used for rapid intra-operative diagnosis.", "تُستعمل المقاطع المجمّدة للتشخيص السريع أثناء العملية.", "T"),
 TF("The sledge microtome is best for very large or hard blocks.", "المِشراح المنزلق الأنسب للقوالب الكبيرة جدًا أو الصلبة.", "T"),
 TF("The ultramicrotome uses a glass or diamond knife.", "يستعمل المِشراح الفائق الدقّة سكّينًا زجاجية أو ماسية.", "T"),
 TF("Ultramicrotome sections are 30–500 µm thick.", "سُمك مقاطع المِشراح الفائق الدقّة 30–500 مايكرومتر.", "F"),
 TF("The vibratome preserves cell viability and antigenicity.", "يحافظ الفايبراتوم على حيوية الخلايا ومستضدّيتها.", "T"),
 TF("A ribbon of serial sections forms because of static electricity.", "يتكوّن شريط المقاطع المتسلسلة بسبب الكهرباء الساكنة.", "T"),
 TF("The float-out bath is kept above the melting point of paraffin.", "يُحفظ حمّام التعويم فوق درجة انصهار البرافين.", "F"),
 TF("After mounting, the slide is dried in an oven.", "بعد التحميل تُجفّف الشريحة في الفرن.", "T"),
]

traps = [
 TR("Thickness of each microtome", "سُمك كل مِشراح", "Rotary 2–10 µm (set 4–5 µm); ultramicrotome 50–100 NANOmeters; vibratome 30–500 µm (thickest).", "الدوّار 2–10 مايكرومتر (يُضبط 4–5)؛ والفائق الدقّة 50–100 نانومتر؛ والاهتزازي 30–500 مايكرومتر (الأسمك)."),
 TR("Rotary: what moves?", "الدوّار: ماذا يتحرّك؟", "The BLOCK moves vertically past a STATIONARY knife (handwheel).", "القالب يتحرّك عموديًا أمام سكّين ثابتة (عجلة اليد)."),
 TR("Sledge: what moves?", "المنزلق: ماذا يتحرّك؟", "The block on the SLEDGE slides past a long stationary knife.", "القالب على الزلّاجة ينزلق أمام سكّين طويلة ثابتة."),
 TR("Cryostat vs vibratome", "الكرايوستات مقابل الاهتزازي", "Cryostat: FROZEN tissue in freezing medium. Vibratome: FRESH tissue NOT frozen, NOT paraffin — in buffer.", "الكرايوستات: نسيج مجمّد في وسط تجميد. الاهتزازي: نسيج طازج غير مجمّد ولا برافين — في دارئ."),
 TR("Water bath temperature", "حرارة حمّام الماء", "5–10 °C BELOW the paraffin melting point — not above (the wax would melt).", "أقل من انصهار البرافين بـ 5–10 °م — لا أعلى (وإلا يذوب الشمع)."),
 TR("Slide position when mounting", "موضع الشريحة عند التحميل", "The slide goes UNDER the floating section, then the section is fished out.", "الشريحة توضع تحت المقطع العائم ثم يُصاد المقطع."),
]

important = [
 IM("Define microtomy and state its primary goal.", "عرّف المقطعية واذكر هدفها الرئيس.",
    "The technique of preparing extremely thin sections (a few µm) with a microtome, which are mounted on slides and stained for light or electron microscopy. Goal: allow light or electrons to pass through the specimen so internal structures become visible.",
    "تقنية تحضير مقاطع رقيقة جدًا (بضعة مايكرومترات) بالمِشراح، تُحمّل على شرائح وتُصبغ للفحص بالمجهر الضوئي أو الإلكتروني. هدفها: السماح للضوء أو الإلكترونات بالمرور عبر العيّنة لتظهر تراكيبها الداخلية."),
 IM("List the key components of a microtome.", "عدّد المكوّنات الأساسية للمِشراح.",
    "1. Base & clamp (prevents vibration, holds the block). 2. Knife holder (steel, glass or diamond blade). 3. Specimen feed mechanism (advances the block e.g. 4–5 µm; determines thickness). 4. Cutting window/arm.",
    "1. القاعدة والمِلزمة (تمنع الاهتزاز وتثبّت القالب). 2. حامل السكّين (شفرة فولاذ أو زجاج أو ماس). 3. آلية تغذية العيّنة (تُقدّم القالب مثل 4–5 مايكرومتر؛ وتحدّد السُمك). 4. نافذة/ذراع القطع."),
 IM("Compare the five types of microtomes.", "قارن بين أنواع المشاريح الخمسة.",
    "Rotary: block moves past a stationary knife; 2–10 µm paraffin serial sections; most common. Cryostat: rotary in a -15 to -30 °C chamber; frozen sections (intra-operative diagnosis, lipids, enzymes, IHC). Sledge: block on a sledge past a long knife; large/hard, celloidin. Ultramicrotome: glass/diamond knife in a boat; 50–100 nm for TEM on copper grids. Vibratome: vibrating blade, fresh tissue in buffer; 30–500 µm.",
    "الدوّار: القالب يتحرّك أمام سكّين ثابتة؛ مقاطع برافين متسلسلة 2–10 مايكرومتر؛ الأشيع. الكرايوستات: دوّار في حجرة -15 إلى -30 °م؛ مقاطع مجمّدة (تشخيص أثناء العملية، دهون، إنزيمات، كيمياء مناعية). المنزلق: قالب على زلّاجة أمام سكّين طويلة؛ كبير/صلب، سيلويدين. الفائق الدقّة: سكّين زجاجية/ماسية في قارب؛ 50–100 نانومتر للمجهر الإلكتروني على شبكات نحاسية. الاهتزازي: شفرة مهتزّة، نسيج طازج في دارئ؛ 30–500 مايكرومتر."),
 IM("Why is the cryostat essential? Give three uses.", "لماذا الكرايوستات أساسي؟ اذكر ثلاثة استعمالات.",
    "It cuts frozen sections (tissue in freezing medium, not paraffin): 1. rapid intra-operative diagnosis (is the tumor cancerous?), 2. demonstrating lipids or enzymes destroyed by hot paraffin, 3. immunohistochemistry on sensitive antigens.",
    "يقطع مقاطع مجمّدة (نسيج في وسط تجميد لا برافين): 1. التشخيص السريع أثناء العملية (هل الورم سرطاني؟)، 2. إظهار الدهون أو الإنزيمات التي يُتلفها البرافين الساخن، 3. الكيمياء النسيجية المناعية على المستضدّات الحسّاسة."),
 IM("Describe the steps from cutting to staining.", "صف الخطوات من القطع إلى التصبيغ.",
    "Secure the block; install a sharp knife/disposable blade; set thickness (4–5 µm); turn the handwheel smoothly → ribbon of serial sections (static electricity). Float the ribbon on a warm water bath (5–10 °C below paraffin melting point) to remove wrinkles; submerge a slide under the section, fish it out, drain and dry in an oven; stain (e.g. H&E).",
    "تثبيت القالب؛ تركيب سكّين حادّة/شفرة لمرّة واحدة؛ ضبط السُمك (4–5 مايكرومتر)؛ إدارة العجلة بسلاسة ← شريط مقاطع متسلسلة (كهرباء ساكنة). تعويم الشريط على حمّام ماء دافئ (أقل من انصهار البرافين بـ 5–10 °م) لإزالة التجاعيد؛ غمر شريحة تحت المقطع وصيده وتصفيته وتجفيفه بالفرن؛ ثم التصبيغ (مثل H&E)."),
]

meta = {"subject_en": "Histopathology", "subject_ar": "علم الأمراض النسيجية", "short_ar": "انسجة", "instructor": "م.م. آية وسمي",
        "unit_en": "Lab 4", "unit_ar": "العملي 4", "unit_label": "LAB", "unit_no": "4",
        "title_en": "Microtome for paraffin and frozen sections", "title_ar": "المِشراح للمقاطع البرافينية والمجمّدة",
        "kind": "Laboratories — عملي", "stage": "The third stage — الثالثة"}
blocks, mcq, tf, traps, important = ltr_all(blocks), ltr_all(mcq), ltr_all(tf), ltr_all(traps), ltr_all(important)
save("histopathology-lab4-microtome", meta, blocks, mcq, tf, traps, important)
fit("histopathology-lab4-microtome", min_gap=0.08)   # no big gaps, small ones too

```
