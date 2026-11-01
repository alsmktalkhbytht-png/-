---
source: BIOS-Obsidian/tools/scripts/hl3x/t3.py
handouts: []
saved: 2026-11-01
tags: [bios, code]
---
# hl3x/t3.py

Utility script.

```python
import sys; sys.path.insert(0, "/tmp/claude-0/-home-claude/ff420988-e3a4-58e4-8344-8f014438cb53/scratchpad/imm456")
from ci import *            # c helpers + B INSHORT TERMS balance save(split.fix)
import split; split.ABBR = split.ABBR + ("**clean**.",)

BN = lambda en, ar: N(en, ar, label=["BIOS note", "ملاحظة BIOS"])
O = P

blocks = [
 # ───────────────────────── 1
 SEC("Tissue processing", "تحضير (معالجة) النسيج"),
 C("Tissue processing describes the steps required to take animal or human tissue **from fixation** to the state where it is **completely infiltrated with a suitable histological wax** and can be **embedded** ready for section cutting on the **microtome**.",
   "تحضير النسيج يصف الخطوات اللازمة لنقل النسيج الحيواني أو البشري **من التثبيت** إلى الحالة التي يكون فيها **مُشرَّبًا بالكامل بشمع نسيجي مناسب** ويمكن **طمره** جاهزًا لقطع المقاطع على **المشراح (المايكروتوم)**."),
 C("types : **manually** or **automated**", "أنواعه: **يدوي** أو **آلي**"),
 H2("Tissue processing steps", "خطوات تحضير النسيج"),
 L(["**Fixation.**", "**Sectioning**", "**Dehydration.**", "**Clearing** (or de-alcohlisation).", "**Impregnation in wax** ( Wax infiltration).", "**Embedding in paraffin block.**", "**sectioning and slide preparation**", "**staining**", "**mounting**"],
   ["**التثبيت.**", "**التقطيع (فتح العيّنة)**", "**نزع الماء (التجفيف).**", "**الترويق** (أو إزالة الكحول).", "**التشريب بالشمع** (تخلّل الشمع).", "**الطمر في قالب برافين.**", "**التقطيع وتحضير الشريحة**", "**الصبغ**", "**التحميل (التغطية)**"]),
 BN("Step 2 \"Sectioning\" here means cutting (grossing) the received specimen into pieces before processing; step 7 is cutting thin sections on the microtome. The sheet writes \"de-alcohlisation\" (de-alcoholisation).",
    "الخطوة 2 \"Sectioning\" هنا تعني تقطيع العيّنة المستلمة (الفحص العياني والتقطيع) قبل التحضير؛ أمّا الخطوة 7 فهي قطع مقاطع رقيقة بالمايكروتوم. والورقة تكتب \"de-alcohlisation\" والصحيح \"de-alcoholisation\"."),
 FLOW([("Fixation", "التثبيت"), ("Sectioning", "التقطيع"), ("Dehydration", "نزع الماء"), ("Clearing", "الترويق"), ("Wax impregnation", "التشريب بالشمع"), ("Embedding", "الطمر"), ("Microtomy", "التقطيع الدقيق"), ("Staining", "الصبغ"), ("Mounting", "التحميل")], en="Nine steps", ar="تسع خطوات"),
 INSHORT([("Tissue processing: from **fixation** → tissue fully **infiltrated with wax** → **embedded** for the **microtome**.", "تحضير النسيج: من **التثبيت** ← نسيج **مُشرَّب بالشمع** بالكامل ← **مطمور** للمايكروتوم."),
          ("Done **manually** or **automated**; nine steps from fixation to mounting.", "يتم **يدويًا** أو **آليًا**؛ وتسع خطوات من التثبيت إلى التحميل.")]),

 # ───────────────────────── 2
 SEC("Fixation", "التثبيت"),
 C("Aiming to **preserve** a sample of biological materials ( tissues or cells) **as close to its natural state as possible** in the process of preparing tissue for examination.",
   "يهدف إلى **حفظ** عيّنة المواد الحيوية (الأنسجة أو الخلايا) **أقرب ما يمكن إلى حالتها الطبيعية** أثناء تحضير النسيج للفحص."),
 C("**Factors affecting fixation:** PH , temperature, volume ,Time interval", "**العوامل المؤثّرة في التثبيت:** الأس الهيدروجيني (pH)، ودرجة الحرارة، والحجم، والفترة الزمنية"),
 INSHORT([("Fixation preserves tissue **close to its natural state**.", "التثبيت يحفظ النسيج **قريبًا من حالته الطبيعية**."),
          ("Factors: **pH, temperature, volume, time**.", "العوامل: **pH، الحرارة، الحجم، الوقت**.")]),

 # ───────────────────────── 3
 SEC("Sectioning", "التقطيع (فتح العيّنة)"),
 R("Each organ or tissue has a **special procedure** in sectioning.", "لكل عضو أو نسيج **إجراء خاص** في التقطيع."),
 F("grossing.png", "Sectioning a received specimen", "تقطيع عيّنة مستلمة", h="44mm"),
 R("The details are **recorded in a register** including patient information and sample type and all the accompanying documents are carefully checked.", "تُسجَّل التفاصيل **في سجلّ** تشمل معلومات المريض ونوع العيّنة، وتُفحص كل الوثائق المرافقة بعناية."),
 F("register.png", "Recording the details in the register", "تسجيل التفاصيل في السجلّ", h="44mm"),
 R("The sample and request form are **labeled**", "تُوسَم (تُلصق عليها البطاقة) العيّنة واستمارة الطلب"),
 R("Specimens are usually **received in fixative**", "تُستلم العيّنات عادةً **في مادة مثبّتة**"),
 FF(("labelling.png", "The sample and request form are labeled", "وسم العيّنة واستمارة الطلب", "40mm"),
    ("fixative-received.png", "Specimen received in fixative", "عيّنة مستلمة في مادة مثبّتة", "40mm")),
 INSHORT([("Each tissue has its **own procedure**; details go in a **register**; sample and form are **labeled**; specimens arrive **in fixative**.", "لكل نسيج **إجراؤه**؛ وتُسجَّل التفاصيل في **سجلّ**؛ وتُوسَم العيّنة والاستمارة؛ وتصل العيّنات **في مثبّت**.")]),

 # ───────────────────────── 4
 SEC("Dehydration", "نزع الماء (التجفيف)"),
 L(["This process must be carried out so that the **embedding medium can infiltrate properly**.", "**Alcohol in various dilutions** is usually used.", "water from the tissues should be removed because **water is not miscible with wax**", "prevent tissue shrinking."],
   ["يجب إجراء هذه العملية حتى **يتخلّل وسط الطمر النسيج بشكل صحيح**.", "يُستعمل عادةً **الكحول بتخافيف مختلفة (تراكيز متدرّجة)**.", "يجب إزالة الماء من الأنسجة لأن **الماء لا يمتزج بالشمع**", "منع انكماش النسيج."]),
 F("dehydration.png", "Dehydration: 30% (3 min) → 50% (3 min) → 70% (3 min) → 70% (overnight) → 90% → Ab Alcohol (1 hr in each grade). Remove fixative and water from the tissues and replacing with dehydrating fluid.",
   "نزع الماء: 30% (3 دقائق) ← 50% (3 دقائق) ← 70% (3 دقائق) ← 70% (طوال الليل) ← 90% ← الكحول المطلق (ساعة في كل درجة). إزالة المثبّت والماء من الأنسجة واستبدالهما بسائل نازع للماء.", h="56mm"),
 H2("Automatic sample preparation system", "نظام تحضير العيّنات الآلي"),
 F("auto-processor.png", "Automatic sample (tissue) preparation system", "نظام تحضير العيّنات (الأنسجة) الآلي", h="48mm"),
 INSHORT([("Dehydration = removing water with **graded alcohols**, because **water does not mix with wax**.", "نزع الماء = إزالة الماء **بكحولات متدرّجة**، لأن **الماء لا يمتزج بالشمع**."),
          ("Lets the embedding medium infiltrate; prevents shrinking.", "يسمح بتخلّل وسط الطمر؛ ويمنع الانكماش.")]),

 # ───────────────────────── 5
 SEC("Clearing", "الترويق"),
 C("As **paraffin wax is insoluble in alcohol**, it must be replaced by a fluid that is **miscible with or is a solvent of paraffin wax**, to get rid of alcohol & make the tissue **more translucent**.",
   "لأن **شمع البرافين لا يذوب في الكحول**، يجب استبدال الكحول بسائل **يمتزج بشمع البرافين أو يذيبه**، للتخلّص من الكحول وجعل النسيج **أكثر شفافية**."),
 C("**Xylol:** cheap and rapid in action, though tends to **harden tissue on prolonged application**",
   "**الزايلول (الزايلين):** رخيص وسريع المفعول، لكنه يميل إلى **تقسية النسيج عند الاستعمال المطوّل**"),
 FF(("xylene-bottle.png", "p-Xylene", "الزايلين (بارا-زايلين)", "46mm"),
    ("xylene-clearing.png", "Clearing the tissue in xylene", "ترويق النسيج في الزايلين", "46mm")),
 INSHORT([("Clearing replaces **alcohol** with a **wax solvent** → tissue becomes **translucent**.", "الترويق يستبدل **الكحول** بـ**مذيب للشمع** ← يصبح النسيج **شفّافًا**."),
          ("**Xylol**: cheap, fast, but **hardens** tissue if left long.", "**الزايلول**: رخيص وسريع، لكنه **يقسّي** النسيج إذا طال.")]),

 # ───────────────────────── 6
 SEC("Impregnation (Wax infiltration)", "التشريب (تخلّل الشمع)"),
 C("Tissues are impregnated in wax for **two reasons**:", "تُشرَّب الأنسجة بالشمع **لسببين**:"),
 L(["To surround tissue with some plastic substances to **support it on all sides without injury**.", "To enable **natural cavities** of tissue to be filled with wax, thus **preserving their relationship** to each other."],
   ["لإحاطة النسيج بمادة لدنة **تدعمه من كل الجهات دون أذى**.", "لتمكين **التجاويف الطبيعية** للنسيج من الامتلاء بالشمع، فـ**يُحفظ ترابطها** بعضها مع بعض."]),
 C("**Paraffin wax** used for routine work", "يُستعمل **شمع البرافين** في العمل الروتيني"),
 C(["Tissue may be impregnated with paraffin wax using: ▪ **56 C° oven** or ▪ **Vacuum embedding**.", "Paraffin for impregnation must be **clean**. (i.e. filtered)."],
   ["يمكن تشريب النسيج بشمع البرافين باستعمال: ▪ **فرن بحرارة 56°م** أو ▪ **الطمر بالتفريغ (الفراغ الهوائي)**.", "ويجب أن يكون البرافين المستعمل للتشريب **نظيفًا** (أي مُرشَّحًا)."]),
 C("Tissues which benefits most from **vacuum embedding** are:- **Lung, bone, fatty tissue, all tissues from CNS and lymph nodes**.",
   "الأنسجة الأكثر استفادة من **الطمر بالتفريغ** هي: **الرئة، والعظم، والنسيج الدهني، وكل أنسجة الجهاز العصبي المركزي، والعقد اللمفاوية**."),
 F("wax-impregnation.png", "Tissue in molten paraffin wax for impregnation", "نسيج في شمع برافين منصهر للتشريب", h="52mm"),
 INSHORT([("Wax **supports** tissue on all sides and **fills natural cavities**.", "الشمع **يدعم** النسيج من كل الجهات و**يملأ التجاويف الطبيعية**."),
          ("Paraffin (clean, filtered) in a **56°C oven** or by **vacuum** — vacuum best for lung, bone, fat, CNS, lymph nodes.", "برافين (نظيف مُرشَّح) في **فرن 56°م** أو **بالتفريغ** — والتفريغ الأفضل للرئة والعظم والدهن والجهاز العصبي المركزي والعقد اللمفاوية.")]),

 # ───────────────────────── 7
 SEC("Embedding", "الطمر"),
 C("Process by which tissues are surrounded by a **medium wax** which when solidifies will provide **sufficient external support during sectioning**.",
   "عملية تُحاط فيها الأنسجة **بوسط من الشمع** يوفّر عند تصلّبه **دعمًا خارجيًا كافيًا أثناء التقطيع**."),
 C("Impregnated tissue transferred from **wax bath** to a **mould filled with molten wax** to get a block of wax with the tissue specimen **at the center** with the **cutting surface facing the base** of the block",
   "يُنقل النسيج المُشرَّب من **حمّام الشمع** إلى **قالب مملوء بشمع منصهر** للحصول على قالب شمعي فيه العيّنة النسيجية **في المركز** و**سطح القطع مواجه لقاعدة** القالب"),
 L(["**L-shaped brass boxes.**", "**Embedding cassette**"], ["**صناديق نحاسية على شكل حرف L.**", "**كاسيت (شريط) الطمر**"], en="This may be done using :", ar="ويمكن إجراء ذلك باستعمال:"),
 F("embedding.png", "Embedding (panels A–D): A. embedding centre; B. placing the tissue in the mould; C. labelled cassette; D. the finished paraffin block", "الطمر (اللوحات أ–د): أ. جهاز الطمر؛ ب. وضع النسيج في القالب؛ ج. كاسيت موسوم؛ د. قالب البرافين الجاهز", h="84mm"),
 BN("The A–D panels of the embedding figure have no labels in the sheet; the short descriptions in the caption are BIOS's reading of the pictures.",
    "لوحات شكل الطمر (أ–د) بلا تسميات في الورقة؛ والوصف المختصر في التعليق قراءة BIOS للصور."),
 INSHORT([("Embedding: tissue moved from **wax bath** to a **mould of molten wax** → block with tissue **centred**, cutting surface toward the **base**.", "الطمر: يُنقل النسيج من **حمّام الشمع** إلى **قالب شمع منصهر** ← قالب فيه النسيج **في المركز** وسطح القطع نحو **القاعدة**."),
          ("Tools: **L-shaped brass boxes** or **embedding cassettes**.", "الأدوات: **صناديق نحاسية L** أو **كاسيتات الطمر**.")]),

 *TERMS([("Tissue processing", "تحضير (معالجة) النسيج"),
         ("Fixation", "التثبيت"),
         ("Sectioning", "التقطيع / عمل المقاطع"),
         ("Dehydration", "نزع الماء / التجفيف"),
         ("Clearing", "الترويق / التنقية"),
         ("De-alcoholisation", "إزالة الكحول"),
         ("Impregnation (infiltration)", "التشريب / التخلّل"),
         ("Embedding", "الطمر / القولبة"),
         ("Paraffin wax", "شمع البرافين"),
         ("Microtome", "المايكروتوم / المشراح"),
         ("Staining", "الصبغ / التلوين"),
         ("Mounting", "التحميل / التغطية / التثبيت على الشريحة"),
         ("Fixative", "المثبّت / المادة المثبّتة"),
         ("Miscible", "قابل للامتزاج"),
         ("Translucent", "شفّاف / نصف شفّاف"),
         ("Xylol (xylene)", "الزايلول / الزايلين"),
         ("Vacuum embedding", "الطمر بالتفريغ (بالفراغ الهوائي)"),
         ("Mould", "القالب"),
         ("Embedding cassette", "كاسيت الطمر"),
         ("Register", "السجلّ"),
         ("Shrinking", "الانكماش")]),
]
_t = blocks[-1]; _r = _t["rows"]
blocks[-1:] = [dict(_t, rows=_r[i:i + 7]) for i in range(0, len(_r), 7)]

exec(open(__file__.replace("t3.py", "t3q.py")).read())

```
