---
source: BIOS-Obsidian/tools/scripts/atl2/a2.py
handouts: [advtech-lab2-immunochromatography]
saved: 2026-11-11
tags: [bios, code]
---
# atl2/a2.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#advtech-lab2-immunochromatography|advtech-lab2-immunochromatography]]

```python
import sys; sys.path.insert(0, "/tmp/claude-0/-home-user--/67d83c9a-7b0e-5ae5-b52b-cd659ab074ab/scratchpad/imm456")
from ci import *            # c helpers + B INSHORT TERMS balance save(split.fix)
sys.path.insert(0, "/tmp/claude-0/-home-user--/67d83c9a-7b0e-5ae5-b52b-cd659ab074ab/scratchpad"); from bidi import ltr_all; from flowfit import fit

# Advanced Techniques practical, lab 2 — Immunochromatographic Assays (LFIA). Source: Immunochromatographic_Assays_Practical-1.pdf
# (18 slides exported to PDF, "Presented By: Linda Munjed Hadi"). Text from pdfplumber, re-ordered by the slide columns; the small
# footer notes/citations are not in the text layer → read from the page images. 8 pictures (7 photos/diagrams + the strip
# drawing of slide 4 rendered from the page). Template text "IMAGE PLACEHOLDER …" (slide 2, and hidden under the photos of
# slides 4, 10, 14) left out. Slide 18 "Quick Review Questions" → important questions with model answers. Third stage → merged.
BN = lambda en, ar: N(en, ar, label=["BIOS note", "ملاحظة BIOS"])
FN = lambda en, ar: N(en, ar, label=["Slide footnote", "حاشية الشريحة"])
O = P
FOLDER = "advtech-lab2-immunochromatography"
import split; split.ABBR += ("Biochem.", "Chem.")   # journal abbreviations in the citation are not sentence ends


def ROWS(rows, label, widths=(30, 70), head=(("Item", "البند"), ("What the slide says", "ما تقوله الشريحة"))):
    """slide cards (title + text) → bilingual table; rows = [(title_en, title_ar, text_en, text_ar)]"""
    return T([B(*head[0]), B(*head[1])], [[B(f"**{a}**", f"**{b}**"), B(c, d)] for a, b, c, d in rows],
             key_cols=[0], widths=list(widths), label_en=label[0], label_ar=label[1])


blocks = [
 # ───────────────────────── 1 what is it
 SEC("What is immunochromatography?", "ما هو الكروماتوغرافيا المناعية؟"),
 N("Immunochromatographic Assays · Lateral Flow Immunoassays (LFIA) · Practical Laboratory Lecture · Advanced Laboratory Techniques · Presented By: Linda Munjed Hadi",
   "المقايسات الكروماتوغرافية المناعية · مقايسات التدفّق الجانبي المناعية (`LFIA`) · محاضرة مختبرية عملية · التقنيات المختبرية المتقدمة · تقديم: ليندا منجد هادي",
   label=["Lab sheet", "ورقة العملي"]),
 H2("**What Is Immunochromatography?**", "**ما هي الكروماتوغرافيا المناعية؟**"),
 C("**Immunochromatography**, also known as **lateral flow immunoassay (LFIA)** or simply **a rapid test**, is a rapid diagnostic technique used to detect the presence or absence of a target analyte (such as a specific antigen or antibody) in a liquid sample without the need for specialized laboratory equipment.",
   "**الكروماتوغرافيا المناعية (`Immunochromatography`)**، وتُعرف أيضًا بـ**مقايسة التدفّق الجانبي المناعية (`LFIA`)** أو ببساطة **الفحص السريع**، تقنية تشخيص سريعة تُستعمل للكشف عن وجود أو غياب مادّة هدف (مثل مستضدّ أو ضدّ نوعي) في عيّنة سائلة دون الحاجة إلى أجهزة مختبرية متخصّصة."),
 ROWS([("IMMUNO", "المناعي", "Specific antigen–antibody recognition", "تعرّف نوعي بين المستضدّ والضدّ"),
       ("CHROMATOGRAPHY", "الكروماتوغرافي", "Movement through a membrane by capillary flow", "حركة خلال غشاء بالتدفّق الشعري")],
      ("The two halves of the name", "نصفا الاسم"), (32, 68)),
 C("Together → a visible or reader-detected signal at the test region.", "معًا ← إشارة مرئية أو يكشفها جهاز قارئ عند منطقة الفحص."),
 FN("[1] Koczula & Gallotta, Essays Biochem. 2016; [2] Boehringer & O'Farrell, Clin Chem. 2022", "المصدران [1] و[2] (انظر جدول المصادر أدناه)"),
 BN("Slide 2 also has an empty template box (\"IMAGE PLACEHOLDER\") with no picture — left out.",
    "في الشريحة 2 مربّع قالب فارغ (\"IMAGE PLACEHOLDER\") بلا صورة — لم يُنقل."),
 T([B("No.", "الرقم"), B("Source on the slides", "المصدر في الشرائح")],
   [["[1]", B("Koczula & Gallotta, Essays Biochem. 2016", "`Koczula & Gallotta, Essays Biochem. 2016`")],
    ["[2]", B("Boehringer & O'Farrell, Clin Chem. 2022", "`Boehringer & O'Farrell, Clin Chem. 2022`")],
    ["[3]", B("WHO, 2023", "منظمة الصحة العالمية `WHO`، 2023")],
    ["[4]", B("Lateral flow immunoassays for antigens, antibodies and haptens detection, 2023", "مقايسات التدفّق الجانبي المناعية للكشف عن المستضدّات والأضداد والهابتينات، 2023")]],
   widths=[12, 88], label_en="Core sources: Koczula & Gallotta, 2016; WHO, 2023; Boehringer & O'Farrell, 2022", label_ar="المصادر الأساسية المذكورة في تذييل الشرائح"),
 INSHORT([("Immunochromatography = **LFIA** = **rapid test**: detects presence/absence of a target analyte **without special equipment**.", "الكروماتوغرافيا المناعية = **`LFIA`** = **الفحص السريع**: يكشف وجود/غياب الهدف **بلا أجهزة متخصّصة**."),
          ("**Immuno** = Ag–Ab recognition; **chromatography** = capillary flow through a membrane.", "**المناعي** = تعرّف مستضدّ–ضدّ؛ و**الكروماتوغرافي** = تدفّق شعري خلال غشاء.")]),

 # ───────────────────────── 2 principle
 SEC("Basic Principle of Lateral Flow", "المبدأ الأساسي للتدفّق الجانبي"),
 FLOW([("Sample", "العيّنة"), ("Capillary Migration", "الهجرة الشعرية"), ("Target binds labeled reagent", "يرتبط الهدف بالكاشف الموسوم"),
       ("Capture at Test line", "الالتقاط عند خطّ الفحص"), ("Visible Signal", "إشارة مرئية")]),
 L(["The sample moves along the strip.", "It carries the target and labeled particles.", "The target is captured at the test line.", "The control line shows that the test worked correctly."],
   ["تتحرّك العيّنة على طول الشريط.", "وتحمل معها الهدف والجسيمات الموسومة.", "ويُلتقَط الهدف عند خطّ الفحص.", "ويُظهر خطّ السيطرة أن الفحص عمل بصورة صحيحة."],
   en="**Key Idea**", ar="**الفكرة المفتاحية**"),
 FN("[1] Koczula & Gallotta, 2016; [2] Boehringer & O'Farrell, 2022", "المصدران [1] و[2]"),
 INSHORT([("Sample → **capillary migration** → binds **labeled reagent** → captured at **T** → visible signal.", "العيّنة ← **هجرة شعرية** ← ترتبط **بالكاشف الموسوم** ← تُلتقَط عند **T** ← إشارة مرئية."),
          ("**Control line** = proof that the test **worked correctly**.", "**خطّ السيطرة** = دليل على أن الفحص **عمل بصورة صحيحة**.")]),

 # ───────────────────────── 3 anatomy
 SEC("Anatomy of a lateral-flow strip", "تشريح شريط التدفّق الجانبي"),
 H2("**Anatomy of a Lateral-Flow Strip**", "**تشريح شريط التدفّق الجانبي**"),
 F("strip-anatomy.png", "Sample Pad → Conjugate Pad → Nitrocellulose Membrane (T, C) → Absorbent Pad", "وسادة العيّنة ← وسادة المقترن ← غشاء النتروسليلوز (`T`، `C`) ← الوسادة الماصّة", h="22mm"),
 L(["**Sample pad:** receives and conditions the specimen.", "**Conjugate pad:** stores dried labeled antibodies or antigens.",
    "**Nitrocellulose membrane:** contains the Test (T) and Control (C) capture regions.", "**Absorbent pad:** pulls fluid through the strip and collects excess liquid."],
   ["**وسادة العيّنة:** تستقبل العيّنة وتهيّئها.", "**وسادة المقترن:** تخزّن أضدادًا أو مستضدّات موسومة مجفّفة.",
    "**غشاء النتروسليلوز:** يحتوي منطقتَي الالتقاط: الفحص (`T`) والسيطرة (`C`).", "**الوسادة الماصّة:** تسحب السائل عبر الشريط وتجمع السائل الزائد."]),
 FF(("strip-in-hand.png", "A rapid test cassette (SARS-CoV-2 Antigen): sample well S, lines C and T", "كاسيت فحص سريع (مستضدّ `SARS-CoV-2`): حفرة العيّنة `S` والخطّان `C` و`T`", "44mm"),
    ("cassettes-photo.png", "Rapid test cassettes from the laboratory (HEV, HAV, TORCH IgM…)", "كاسيتات فحوص سريعة من المختبر (`HEV`، `HAV`، `TORCH IgM`…)", "44mm")),
 F("lfa-diagram.png", "How a lateral-flow (sandwich) test works", "كيف يعمل فحص التدفّق الجانبي (الساندويتش)", h="64mm"),
 T([B("Figure text", "كتابات الشكل"), B("Arabic", "بالعربي")],
   [[B("**Sample well (S)**", "**حفرة العيّنة (`S`)**"), B("where the sample is dropped", "مكان وضع العيّنة")],
    [B("**Control line (C)** / **Test line (T)**", "**خطّ السيطرة (`C`)** / **خطّ الفحص (`T`)**"), B("the two lines read in the window", "الخطّان اللذان يُقرآن في النافذة")],
    [B("**1. Sample added**", "**1. إضافة العيّنة**"), B("on the sample pad", "على وسادة العيّنة")],
    [B("**2. Antigen binds to labelled antibody**", "**2. يرتبط المستضدّ بالضدّ الموسوم**"), B("in the conjugate pad (gold-labelled antibody)", "في وسادة المقترن (ضدّ موسوم بالذهب)")],
    [B("**3. Complex moves and is captured at Test line (T)**", "**3. يتحرّك المعقّد ويُلتقَط عند خطّ الفحص (`T`)**"), B("Test line (T) (capture antibody)", "خطّ الفحص (`T`) (ضدّ ملتقِط)")],
    [B("**4. Excess label is captured at Control line (C)**", "**4. يُلتقَط الوسم الزائد عند خطّ السيطرة (`C`)**"), B("Control line (C) (capture antibody)", "خطّ السيطرة (`C`) (ضدّ ملتقِط)")],
    [B("**Absorbent pad**", "**الوسادة الماصّة**"), B("end of the strip", "نهاية الشريط")]],
   key_cols=[0], widths=[55, 45], label_en="Figure text", label_ar="كتابات الشكل"),
 BN("Slides 5 and 6 are pictures only (no text); their captions here are by BIOS. The order along the strip is always **S → T → C** (the control line is the last line).",
    "الشريحتان 5 و6 صور فقط (بلا نص)؛ والعناوين هنا من BIOS. والترتيب على الشريط دائمًا **`S → T → C`** (خطّ السيطرة هو الخطّ الأخير)."),
 INSHORT([("Strip: **sample pad → conjugate pad → nitrocellulose (T, C) → absorbent pad**.", "الشريط: **وسادة العيّنة ← وسادة المقترن ← النتروسليلوز (`T`، `C`) ← الوسادة الماصّة**."),
          ("Conjugate pad = **dried labeled** antibodies/antigens; absorbent pad **pulls** the fluid.", "وسادة المقترن = أضداد/مستضدّات **موسومة مجفّفة**؛ والوسادة الماصّة **تسحب** السائل.")]),

 # ───────────────────────── 4 sample & conjugate pads
 SEC("Sample pad and conjugate pad", "وسادة العيّنة ووسادة المقترن"),
 H2("**Sample Pad & Conjugate Pad**", "**وسادة العيّنة ووسادة المقترن**"),
 L(["Receives the specimen", "Helps distribute fluid evenly", "May filter or condition the sample", "Begins capillary migration"],
   ["تستقبل العيّنة", "تساعد على توزيع السائل بانتظام", "قد ترشّح العيّنة أو تهيّئها", "تبدأ الهجرة الشعرية"],
   en="**Sample Pad**", ar="**وسادة العيّنة**"),
 L(["Contains dried labeled detection reagents", "Labels may include colloidal gold or colored/fluorescent particles", "Rehydrates when the sample reaches it", "Target + labeled reagent form a migrating complex"],
   ["تحتوي كواشف كشف موسومة مجفّفة", "قد تشمل الوسوم الذهب الغروي أو جسيمات ملوّنة/متألّقة", "تعود إليها الرطوبة عندما تصلها العيّنة", "يكوّن الهدف + الكاشف الموسوم معقّدًا مهاجرًا"],
   en="**Conjugate Pad**", ar="**وسادة المقترن**", start=1),
 C("**Practical point:** incorrect specimen volume or poor sample preparation can disturb flow before the sample ever reaches the test line.",
   "**نقطة عملية:** حجم العيّنة الخاطئ أو سوء تحضيرها قد يخلّ بالتدفّق قبل أن تصل العيّنة إلى خطّ الفحص أصلًا."),
 FN("[2] Boehringer & O'Farrell, 2022", "المصدر [2]"),
 INSHORT([("Sample pad: receives, distributes, filters, **starts migration**.", "وسادة العيّنة: تستقبل، توزّع، ترشّح، **تبدأ الهجرة**."),
          ("Conjugate pad: **dried labels** (colloidal gold / coloured / fluorescent) → rehydrate → **migrating complex**.", "وسادة المقترن: **وسوم مجفّفة** (ذهب غروي / ملوّنة / متألّقة) ← تترطّب ← **معقّد مهاجر**.")]),

 # ───────────────────────── 5 lines
 SEC("Test line, control line and absorbent pad", "خطّ الفحص وخطّ السيطرة والوسادة الماصّة"),
 H2("**Test Line, Control Line & Absorbent Pad**", "**خطّ الفحص وخطّ السيطرة والوسادة الماصّة**"),
 ROWS([("Test Line (T)", "خطّ الفحص (`T`)", "Captures the target and produces the test signal.", "يلتقط الهدف وينتج إشارة الفحص."),
       ("Control Line (C)", "خطّ السيطرة (`C`)", "Shows that the test worked correctly.", "يُظهر أن الفحص عمل بصورة صحيحة."),
       ("Absorbent Pad", "الوسادة الماصّة", "Helps the sample keep moving and collects excess liquid.", "تساعد العيّنة على الاستمرار بالحركة وتجمع السائل الزائد.")],
      ("Test Line, Control Line & Absorbent Pad", "خطّ الفحص وخطّ السيطرة والوسادة الماصّة"), (30, 70)),
 C("**No control line = Invalid result.**", "**لا خطّ سيطرة = نتيجة باطلة.**"),
 FN("[1] Koczula & Gallotta, 2016; manufacturer instructions must be followed for each kit", "المصدر [1]؛ ويجب اتّباع تعليمات الشركة المصنّعة لكل عُدّة"),
 INSHORT([("**T** captures the target → test signal; **C** proves the test worked.", "**`T`** يلتقط الهدف ← إشارة الفحص؛ و**`C`** يثبت أن الفحص عمل."),
          ("**No C line = invalid**, whatever T shows.", "**لا خطّ `C` = باطلة**، مهما أظهر `T`.")]),

 # ───────────────────────── 6 interpretation
 SEC("Interpreting results", "تفسير النتائج"),
 H2("**Interpreting Results**", "**تفسير النتائج**"),
 C("For a typical qualitative sandwich-format rapid test", "لفحص سريع نوعي نموذجي بصيغة الساندويتش"),
 ROWS([("POSITIVE", "موجب", "Control line appears + Test line appears", "يظهر خطّ السيطرة + يظهر خطّ الفحص"),
       ("NEGATIVE", "سالب", "Control line appears + No Test line", "يظهر خطّ السيطرة + لا يظهر خطّ الفحص"),
       ("INVALID", "باطل", "Control line does not appear", "لا يظهر خطّ السيطرة")],
      ("Interpreting Results", "تفسير النتائج"), (24, 76), (("Result", "النتيجة"), ("Lines", "الخطوط"))),
 FF(("cassettes-hand.png", "Two cassettes: C + T (positive) and C only (negative)", "كاسيتان: `C` + `T` (موجب) و`C` فقط (سالب)", "38mm"),
    ("results-abc.png", "(A) positive · (B) negative · (C) invalid — Control line, Test line, Drop solution, Flow", "(A) موجب · (B) سالب · (C) باطل — خطّ السيطرة، خطّ الفحص، موضع وضع المحلول، اتّجاه التدفّق", "38mm")),
 C("Always interpret the result according to the specific kit instructions and within the stated reading time.", "فسّر النتيجة دائمًا وفق تعليمات العُدّة المحدّدة وضمن وقت القراءة المذكور."),
 BN("The two pictures have no captions on the slide; A/B/C are read by BIOS from the lines (A: C + faint T, B: C only, C: no line). On the slide the picture covers part of the sentence above — its full text is from the file.",
    "الصورتان بلا عناوين في الشريحة؛ وقراءة A/B/C من BIOS حسب الخطوط (A: `C` + `T` خفيف، B: `C` فقط، C: لا خطّ). وفي الشريحة تغطّي الصورة جزءًا من الجملة أعلاه — ونصّها الكامل من الملف."),
 FN("WHO guidance emphasizes correct performance and interpretation of RDTs [3]", "إرشادات منظمة الصحة العالمية تؤكّد الأداء والتفسير الصحيحين للفحوص التشخيصية السريعة (`RDTs`) [3]"),
 INSHORT([("**Positive** = C + T; **negative** = C only; **invalid** = no C.", "**موجب** = `C` + `T`؛ و**سالب** = `C` فقط؛ و**باطل** = لا `C`."),
          ("Follow the **kit instructions** and the **reading time**.", "اتّبع **تعليمات العُدّة** و**وقت القراءة**.")]),

 # ───────────────────────── 7 faint line
 SEC("A faint test line", "خطّ الفحص الخفيف"),
 H2("**What About a Faint Test Line?**", "**ماذا عن خطّ الفحص الخفيف؟**"),
 C("A faint line may still represent a reactive/positive result in many qualitative tests — but only if the manufacturer defines it that way and it appears within the permitted reading time.",
   "قد يمثّل الخطّ الخفيف نتيجة متفاعلة/موجبة في كثير من الفحوص النوعية — ولكن فقط إذا عرّفته الشركة المصنّعة كذلك وظهر ضمن وقت القراءة المسموح."),
 L(["Do not compare line darkness between different brands unless the kit supports that interpretation.", "Do not read the cassette after the stated time window.",
    "Repeat or confirm according to the test algorithm when the result is uncertain."],
   ["لا تقارن غمق الخطّ بين ماركات مختلفة إلا إذا كانت العُدّة تدعم هذا التفسير.", "لا تقرأ الكاسيت بعد نافذة الوقت المذكورة.",
    "أعد الفحص أو أكّده حسب خوارزمية الفحص عندما تكون النتيجة غير مؤكّدة."]),
 F("faint-line.png", "Test line intensity at 0 ng/mL, 1 ng/mL and 2 ng/mL (C, T, S)", "شدّة خطّ الفحص عند `0 ng/mL` و`1 ng/mL` و`2 ng/mL` (`C`، `T`، `S`)", h="56mm"),
 BN("In this picture the T line gets darker as the concentration rises (0 → 1 → 2 ng/mL) while C stays the same — a faint T is still a line.",
    "في هذه الصورة يغمق خطّ `T` كلّما زاد التركيز (`0 → 1 → 2 ng/mL`) بينما يبقى `C` كما هو — فالخطّ `T` الخفيف يبقى خطًّا."),
 FN("Interpretation is kit-specific; follow manufacturer IFU and local testing algorithm", "التفسير خاصّ بكل عُدّة؛ اتّبع تعليمات الاستعمال (`IFU`) للشركة وخوارزمية الفحص المحلّية"),
 INSHORT([("Faint T may be **positive** — only if the **manufacturer** says so and it is **within the reading time**.", "خطّ `T` الخفيف قد يكون **موجبًا** — فقط إذا قالت **الشركة** ذلك وظهر **ضمن وقت القراءة**."),
          ("Don't compare brands; don't read late; **repeat/confirm** when uncertain.", "لا تقارن الماركات؛ لا تقرأ متأخّرًا؛ **أعد/أكّد** عند الشك.")]),

 # ───────────────────────── 8 formats
 SEC("Main assay formats", "الصيغ الرئيسية للفحص"),
 H2("**Main Assay Formats**", "**الصيغ الرئيسية للفحص**"),
 C("**Sandwich Format** · **Competitive Format**", "**صيغة الساندويتش** · **الصيغة التنافسية**"),
 C("Never interpret a rapid test by memory alone — identify the assay format and read the kit instructions.",
   "لا تفسّر الفحص السريع من الذاكرة وحدها أبدًا — حدّد صيغة الفحص واقرأ تعليمات العُدّة."),
 BN("The two format boxes on the slide are empty (titles only). The table below is BIOS: it is the reason the slide warns you to identify the format.",
    "مربّعا الصيغتين في الشريحة فارغان (عنوانان فقط). والجدول أدناه من BIOS: وهو سبب تحذير الشريحة من ضرورة تحديد الصيغة."),
 T([B("", ""), B("Sandwich format", "صيغة الساندويتش"), B("Competitive format", "الصيغة التنافسية")],
   [[B("**Used for**", "**تُستعمل لـ**"), B("large analytes (proteins, hCG, antigens)", "مواد كبيرة (بروتينات، `hCG`، مستضدّات)"), B("small molecules / drugs", "جزيئات صغيرة / أدوية")],
    [B("**At the T line**", "**عند خطّ `T`**"), B("target bridges labeled Ab and capture Ab", "الهدف يربط الضدّ الموسوم بالضدّ الملتقِط"), B("target competes and blocks the labeled reagent", "الهدف ينافس ويمنع ارتباط الكاشف الموسوم")],
    [B("**Positive result**", "**النتيجة الموجبة**"), B("**T line appears**", "**يظهر خطّ `T`**"), B("**T line weaker or absent**", "**خطّ `T` أضعف أو يختفي**")],
    [B("**Control line**", "**خطّ السيطرة**"), B("must appear", "يجب أن يظهر"), B("must appear", "يجب أن يظهر")]],
   key_cols=[0], widths=[24, 38, 38], style="summary", label_en="BIOS: sandwich vs competitive", label_ar="BIOS: الساندويتش مقابل التنافسي"),
 FN("[4] Lateral flow immunoassays for antigens, antibodies and haptens detection, 2023", "المصدر [4]"),
 INSHORT([("Two formats: **sandwich** and **competitive**.", "صيغتان: **الساندويتش** و**التنافسية**."),
          ("Sandwich: T line = positive; competitive: **no/weak T = positive** → always check the format and the kit.", "الساندويتش: خطّ `T` = موجب؛ والتنافسية: **غياب/ضعف `T` = موجب** ← تحقّق دائمًا من الصيغة والعُدّة.")]),

 # ───────────────────────── 9 applications
 SEC("Common clinical applications", "التطبيقات السريرية الشائعة"),
 H2("**Common Clinical Applications**", "**التطبيقات السريرية الشائعة**"),
 ROWS([("Pregnancy", "الحمل", "hCG in urine", "`hCG` في الإدرار"),
       ("Infectious disease", "الأمراض المعدية", "Antigen or antibody detection", "الكشف عن المستضدّ أو الضدّ"),
       ("Cardiac markers", "واسمات القلب", "Selected rapid biomarker tests", "فحوص سريعة مختارة للواسمات الحيوية"),
       ("Drugs / small molecules", "الأدوية / الجزيئات الصغيرة", "Often competitive format", "غالبًا بالصيغة التنافسية"),
       ("Point-of-care testing", "الفحص عند نقطة الرعاية", "Near-patient rapid decisions", "قرارات سريعة قرب المريض"),
       ("Home testing", "الفحص المنزلي", "Some regulated self-tests", "بعض الفحوص الذاتية المنظَّمة")],
      ("Common Clinical Applications", "التطبيقات السريرية الشائعة"), (34, 66)),
 FN("[2] Boehringer & O'Farrell, 2022; [3] WHO, 2023", "المصدران [2] و[3]"),
 INSHORT([("Pregnancy (**hCG in urine**), infections (Ag/Ab), cardiac markers, drugs, point-of-care, home tests.", "الحمل (**`hCG` في الإدرار**)، الأمراض المعدية (مستضدّ/ضدّ)، واسمات القلب، الأدوية، نقطة الرعاية، الفحص المنزلي."),
          ("Drugs / small molecules → often **competitive**.", "الأدوية / الجزيئات الصغيرة ← غالبًا **تنافسي**.")]),

 # ───────────────────────── 10 specimens
 SEC("Specimen types", "أنواع العيّنات"),
 H2("**Specimen Types — Use Only What the Kit Allows**", "**أنواع العيّنات — استعمل فقط ما تسمح به العُدّة**"),
 L(["Whole blood", "Serum", "Plasma", "Urine", "Saliva / oral fluid", "Nasal or nasopharyngeal swab extract", "Other kit-specific specimens"],
   ["الدم الكامل", "المصل", "البلازما", "الإدرار", "اللعاب / سائل الفم", "مستخلص مسحة الأنف أو البلعوم الأنفي", "عيّنات أخرى خاصّة بالعُدّة"]),
 N("A test validated for one specimen type should not automatically be used with another specimen type.", "الفحص المُعتمَد لنوع عيّنة واحد لا يجوز استعماله تلقائيًا مع نوع عيّنة آخر.",
   label=["Critical rule", "قاعدة حاسمة"]),
 FN("Follow the manufacturer's Instructions for Use (IFU) for accepted specimen types", "اتّبع تعليمات الاستعمال (`IFU`) للشركة المصنّعة لأنواع العيّنات المقبولة"),
 INSHORT([("Blood, serum, plasma, urine, saliva, nasal/nasopharyngeal swab…", "دم، مصل، بلازما، إدرار، لعاب، مسحة أنف/بلعوم أنفي…"),
          ("**Critical rule:** use only the specimen the kit is **validated** for.", "**قاعدة حاسمة:** استعمل فقط العيّنة **المُعتمَدة** للعُدّة.")]),

 # ───────────────────────── 11 materials
 SEC("Materials", "المواد"),
 H2("**Materials Needed for the Practical Session**", "**المواد المطلوبة للجلسة العملية**"),
 L(["Rapid test cassette or strip", "Patient specimen", "Kit buffer or extraction solution", "Dropper, capillary tube, or micropipette as specified",
    "Timer", "Disposable gloves and laboratory coat", "Biohazard waste container"],
   ["كاسيت أو شريط الفحص السريع", "عيّنة المريض", "دارئ العُدّة أو محلول الاستخلاص", "قطّارة أو أنبوب شعري أو ماصّة دقيقة حسب المحدّد",
    "مؤقّت", "قفّازات للاستعمال مرّة واحدة وصدرية مختبر", "حاوية نفايات الخطر الحيوي"]),
 F("kit-contents.png", "Rapid test kit contents (box, cassettes, buffer, swab, instructions for use)", "محتويات عُدّة الفحص السريع (العلبة، الكاسيتات، الدارئ، المسحة، تعليمات الاستعمال)", h="58mm"),
 INSHORT([("Cassette/strip, specimen, **kit buffer**, dropper/capillary/micropipette, **timer**, gloves + coat, **biohazard container**.", "كاسيت/شريط، عيّنة، **دارئ العُدّة**، قطّارة/أنبوب شعري/ماصّة، **مؤقّت**، قفّازات + صدرية، **حاوية خطر حيوي**.")]),

 # ───────────────────────── 12 procedure
 SEC("Practical procedure", "الإجراء العملي"),
 H2("**Practical Procedure — General Workflow**", "**الإجراء العملي — خطوات العمل العامة**"),
 L(["Check kit & expiry", "Label cassette", "Prepare specimen", "Add exact sample volume", "Add buffer if required", "Start timer", "Read at specified time", "Record result"],
   ["افحص العُدّة وتاريخ انتهائها", "رقّم الكاسيت", "حضّر العيّنة", "أضف حجم العيّنة المضبوط", "أضف الدارئ إذا لزم", "شغّل المؤقّت", "اقرأ في الوقت المحدّد", "سجّل النتيجة"]),
 C("The exact number of drops, incubation time, and interpretation rules are test-specific.", "العدد الدقيق للقطرات ووقت الحضن وقواعد التفسير خاصّة بكل فحص."),
 FN("WHO: correct test performance and interpretation are essential for reliable RDT use [3]", "منظمة الصحة العالمية: الأداء والتفسير الصحيحان ضروريان للاستعمال الموثوق للفحوص السريعة (`RDT`) [3]"),
 INSHORT([("Check kit/expiry → label → specimen → **exact volume** → buffer → **timer** → read on time → record.", "افحص العُدّة/الانتهاء ← رقّم ← العيّنة ← **الحجم المضبوط** ← الدارئ ← **المؤقّت** ← اقرأ في الوقت ← سجّل."),
          ("Drops, time and rules are **test-specific**.", "القطرات والوقت والقواعد **خاصّة بكل فحص**.")]),

 # ───────────────────────── 13 errors
 SEC("False or invalid results", "النتائج الكاذبة أو الباطلة"),
 H2("**Common Causes of False or Invalid Results**", "**الأسباب الشائعة للنتائج الكاذبة أو الباطلة**"),
 L(["Wrong specimen type", "Poor specimen collection", "Incorrect sample volume", "Wrong buffer volume", "Expired or improperly stored kit", "Cross-contamination"],
   ["نوع عيّنة خاطئ", "سوء جمع العيّنة", "حجم عيّنة غير صحيح", "حجم دارئ خاطئ", "عُدّة منتهية أو مخزونة بصورة غير صحيحة", "تلوّث متبادل"],
   en="**Pre-analytical / User Errors**", ar="**أخطاء ما قبل التحليل / أخطاء المستخدم**"),
 L(["Incorrect timing", "Cassette placed on an unsuitable surface", "Failure of control line", "Misreading faint lines", "Reading after the allowed time", "Ignoring kit-specific interpretation rules"],
   ["توقيت غير صحيح", "وضع الكاسيت على سطح غير مناسب", "فشل خطّ السيطرة", "قراءة خاطئة للخطوط الخفيفة", "القراءة بعد الوقت المسموح", "تجاهل قواعد التفسير الخاصّة بالعُدّة"],
   en="**Analytical / Interpretation Errors**", ar="**أخطاء التحليل / التفسير**", start=1),
 FN("WHO notes that incorrect performance or interpretation can compromise RDT utility [3]", "تشير منظمة الصحة العالمية إلى أن الأداء أو التفسير غير الصحيح قد يُضعف فائدة الفحوص السريعة [3]"),
 INSHORT([("User errors: wrong **specimen**, **volume**, **buffer**, expired kit, contamination.", "أخطاء المستخدم: **عيّنة** أو **حجم** أو **دارئ** خاطئ، عُدّة منتهية، تلوّث."),
          ("Interpretation errors: **timing**, surface, **no control line**, faint lines, **late reading**, ignoring kit rules.", "أخطاء التفسير: **التوقيت**، السطح، **غياب خطّ السيطرة**، الخطوط الخفيفة، **القراءة المتأخّرة**، تجاهل قواعد العُدّة.")]),

 # ───────────────────────── 14 advantages
 SEC("Advantages and limitations", "المزايا والقيود"),
 H2("**Advantages & Limitations**", "**المزايا والقيود**"),
 L(["Fast results", "Easy to use", "Portable", "Needs little equipment", "Useful near the patient", "Can be used outside large laboratories"],
   ["نتائج سريعة", "سهل الاستعمال", "قابل للحمل", "يحتاج أجهزة قليلة", "مفيد قرب المريض", "يمكن استعماله خارج المختبرات الكبيرة"],
   en="**Advantages**", ar="**المزايا**"),
 L(["Accuracy may differ between tests", "Usually gives positive/negative results", "Faint lines can be difficult to read", "May be less sensitive than some laboratory methods",
    "Some results need confirmation by another test"],
   ["قد تختلف الدقّة بين الفحوص", "يعطي عادةً نتائج موجب/سالب", "قد يصعب قراءة الخطوط الخفيفة", "قد يكون أقلّ حساسية من بعض الطرائق المختبرية",
    "بعض النتائج تحتاج تأكيدًا بفحص آخر"],
   en="**Limitations**", ar="**القيود**", start=1),
 FN("[1] Koczula & Gallotta, 2016; [2] Boehringer & O'Farrell, 2022; [3] WHO, 2023", "المصادر [1] و[2] و[3]"),
 INSHORT([("Advantages: **fast, easy, portable**, little equipment, near the patient.", "المزايا: **سريع، سهل، قابل للحمل**، أجهزة قليلة، قرب المريض."),
          ("Limitations: usually **only +/−**, faint lines, **less sensitive**, may need **confirmation**.", "القيود: عادةً **موجب/سالب فقط**، خطوط خفيفة، **أقلّ حساسية**، قد يحتاج **تأكيدًا**.")]),
] + TERMS([
 ("Immunochromatography", "الكروماتوغرافيا المناعية / الاستشراب المناعي"),
 ("Lateral flow immunoassay (LFIA)", "مقايسة التدفّق الجانبي المناعية / الفحص السريع"),
 ("Rapid diagnostic test (RDT)", "الفحص التشخيصي السريع"),
 ("Analyte", "المادّة الهدف / المادّة المقيسة"),
 ("Capillary flow / migration", "التدفّق الشعري / الهجرة الشعرية"),
 ("Sample pad", "وسادة العيّنة"),
 ("Conjugate pad", "وسادة المقترن / وسادة الاقتران"),
 ("Nitrocellulose membrane", "غشاء النتروسليلوز"),
 ("Absorbent pad", "الوسادة الماصّة / وسادة الامتصاص"),
 ("Test line (T)", "خطّ الفحص / خطّ الاختبار"),
 ("Control line (C)", "خطّ السيطرة / خطّ الضبط"),
 ("Colloidal gold", "الذهب الغروي"),
 ("Invalid result", "نتيجة باطلة / غير صالحة"),
 ("Sandwich format", "صيغة الساندويتش / الشطيرة"),
 ("Competitive format", "الصيغة التنافسية"),
 ("Point-of-care testing", "الفحص عند نقطة الرعاية / بجانب المريض"),
 ("Instructions for Use (IFU)", "تعليمات الاستعمال / نشرة العُدّة"),
 ("Cassette", "الكاسيت / الشريحة البلاستيكية للفحص"),
])

# ───────────────────────── questions
mcq = [
 {"topic_en": "Basics and principle", "topic_ar": "الأساسيات والمبدأ"},
 Q("Immunochromatography is also known as:", "تُعرف الكروماتوغرافيا المناعية أيضًا بـ:", O(("Lateral flow immunoassay (LFIA) or rapid test", "مقايسة التدفّق الجانبي المناعية (`LFIA`) أو الفحص السريع"), ("ELISA", "الإليزا"), ("Gel electrophoresis", "الرحلان الكهربائي الهلامي"), ("Radioimmunoassay", "المقايسة المناعية الإشعاعية")), "a"),
 Q("A main feature of immunochromatography is that it works:", "من أهم صفات الكروماتوغرافيا المناعية أنها تعمل:", O(("Only with a microplate reader", "بقارئ صفائح فقط"), ("Without the need for specialized laboratory equipment", "دون الحاجة إلى أجهزة مختبرية متخصّصة"), ("Only on solid samples", "على العيّنات الصلبة فقط"), ("Only in large laboratories", "في المختبرات الكبيرة فقط")), "b"),
 Q("The \"chromatography\" part of the name refers to:", "جزء «الكروماتوغرافي» من الاسم يشير إلى:", O(("Antigen–antibody recognition", "تعرّف المستضدّ–الضدّ"), ("Colour of the label", "لون الوسم"), ("Movement through a membrane by capillary flow", "الحركة خلال غشاء بالتدفّق الشعري"), ("An electric field", "مجال كهربائي")), "c"),
 Q("What causes the sample to move across the strip?", "ما الذي يحرّك العيّنة عبر الشريط؟", O(("Gravity only", "الجاذبية فقط"), ("An electric current", "تيار كهربائي"), ("A pump", "مضخّة"), ("Capillary flow (pulled by the absorbent pad)", "التدفّق الشعري (تسحبه الوسادة الماصّة)")), "d"),
 Q("The target is captured at the:", "يُلتقَط الهدف عند:", O(("Test line", "خطّ الفحص"), ("Sample pad", "وسادة العيّنة"), ("Absorbent pad", "الوسادة الماصّة"), ("Sample well", "حفرة العيّنة")), "a"),
 {"topic_en": "Anatomy of the strip", "topic_ar": "تشريح الشريط"},
 Q("Dried labeled antibodies or antigens are stored in the:", "تُخزَّن الأضداد أو المستضدّات الموسومة المجفّفة في:", O(("Sample pad", "وسادة العيّنة"), ("Conjugate pad", "وسادة المقترن"), ("Absorbent pad", "الوسادة الماصّة"), ("Plastic cassette", "الكاسيت البلاستيكي")), "b"),
 Q("The Test (T) and Control (C) capture regions are on the:", "منطقتا الالتقاط `T` و`C` موجودتان على:", O(("Sample pad", "وسادة العيّنة"), ("Conjugate pad", "وسادة المقترن"), ("Nitrocellulose membrane", "غشاء النتروسليلوز"), ("Absorbent pad", "الوسادة الماصّة")), "c"),
 Q("The pad that pulls fluid through the strip and collects excess liquid is the:", "الوسادة التي تسحب السائل عبر الشريط وتجمع الزائد هي:", O(("Sample pad", "وسادة العيّنة"), ("Conjugate pad", "وسادة المقترن"), ("Membrane", "الغشاء"), ("Absorbent pad", "الوسادة الماصّة")), "d"),
 Q("Labels in the conjugate pad may include:", "قد تشمل الوسوم في وسادة المقترن:", O(("Colloidal gold or colored/fluorescent particles", "الذهب الغروي أو جسيمات ملوّنة/متألّقة"), ("Radioactive iodine only", "اليود المشعّ فقط"), ("TMB substrate", "ركيزة `TMB`"), ("Agarose", "الآغاروز")), "a"),
 Q("The correct order along the strip is:", "الترتيب الصحيح على طول الشريط:", O(("Absorbent pad → membrane → conjugate pad → sample pad", "الوسادة الماصّة ← الغشاء ← وسادة المقترن ← وسادة العيّنة"), ("Sample pad → conjugate pad → nitrocellulose membrane → absorbent pad", "وسادة العيّنة ← وسادة المقترن ← غشاء النتروسليلوز ← الوسادة الماصّة"),
   ("Conjugate pad → sample pad → absorbent pad → membrane", "وسادة المقترن ← وسادة العيّنة ← الوسادة الماصّة ← الغشاء"), ("Membrane → sample pad → conjugate pad → absorbent pad", "الغشاء ← وسادة العيّنة ← وسادة المقترن ← الوسادة الماصّة")), "b"),
 Q("The sample pad:", "وسادة العيّنة:", O(("Produces the test signal", "تنتج إشارة الفحص"), ("Stores colloidal gold", "تخزّن الذهب الغروي"), ("Receives the specimen and begins capillary migration", "تستقبل العيّنة وتبدأ الهجرة الشعرية"), ("Shows that the test worked", "تُظهر أن الفحص عمل")), "c"),
 {"topic_en": "Lines and interpretation", "topic_ar": "الخطوط والتفسير"},
 Q("The control line:", "خطّ السيطرة:", O(("Captures the target", "يلتقط الهدف"), ("Collects excess liquid", "يجمع السائل الزائد"), ("Rehydrates the label", "يرطّب الوسم"), ("Shows that the test worked correctly", "يُظهر أن الفحص عمل بصورة صحيحة")), "d"),
 Q("In a sandwich-format rapid test, control line appears + test line appears means:", "في فحص سريع بصيغة الساندويتش، ظهور خطّ السيطرة + خطّ الفحص يعني:", O(("Positive", "موجب"), ("Negative", "سالب"), ("Invalid", "باطل"), ("Repeat with another brand", "أعد بماركة أخرى")), "a"),
 Q("Control line appears + no test line means:", "ظهور خطّ السيطرة + عدم ظهور خطّ الفحص يعني:", O(("Positive", "موجب"), ("Negative", "سالب"), ("Invalid", "باطل"), ("Faint positive", "موجب خفيف")), "b"),
 Q("A rapid test is invalid when:", "يكون الفحص السريع باطلًا عندما:", O(("Only the control line appears", "يظهر خطّ السيطرة فقط"), ("Both lines appear", "يظهر الخطّان"), ("The control line does not appear", "لا يظهر خطّ السيطرة"), ("The test line is faint", "يكون خطّ الفحص خفيفًا")), "c"),
 Q("A faint test line may be read as positive only if:", "يُقرأ خطّ الفحص الخفيف موجبًا فقط إذا:", O(("It is darker than another brand", "كان أغمق من ماركة أخرى"), ("It appears after the reading time", "ظهر بعد وقت القراءة"), ("The control line is absent", "غاب خطّ السيطرة"), ("The manufacturer defines it so and it appears within the permitted reading time", "عرّفته الشركة كذلك وظهر ضمن وقت القراءة المسموح")), "d"),
 Q("When the result is uncertain you should:", "عندما تكون النتيجة غير مؤكّدة يجب:", O(("Repeat or confirm according to the test algorithm", "الإعادة أو التأكيد حسب خوارزمية الفحص"), ("Read it again the next day", "قراءتها مجدّدًا في اليوم التالي"), ("Compare it with another brand", "مقارنتها بماركة أخرى"), ("Report it as negative", "تسجيلها سالبة")), "a"),
 {"topic_en": "Formats, applications and specimens", "topic_ar": "الصيغ والتطبيقات والعيّنات"},
 Q("The two main assay formats are:", "الصيغتان الرئيسيتان للفحص:", O(("Direct and indirect", "المباشرة وغير المباشرة"), ("Sandwich and competitive", "الساندويتش والتنافسية"), ("Qualitative and quantitative", "النوعية والكمّية"), ("Wet and dry", "الرطبة والجافّة")), "b"),
 Q("Drugs / small molecules are often tested by the:", "الأدوية / الجزيئات الصغيرة تُفحص غالبًا بالصيغة:", O(("Sandwich format", "الساندويتش"), ("Direct format", "المباشرة"), ("Competitive format", "التنافسية"), ("ELISA format", "الإليزا")), "c"),
 Q("The pregnancy rapid test detects:", "فحص الحمل السريع يكشف:", O(("Glucose in urine", "السكّر في الإدرار"), ("Protein in blood", "البروتين في الدم"), ("Antibodies in saliva", "الأضداد في اللعاب"), ("hCG in urine", "`hCG` في الإدرار")), "d"),
 Q("A test validated for one specimen type:", "الفحص المُعتمَد لنوع عيّنة واحد:", O(("Should not automatically be used with another specimen type", "لا يجوز استعماله تلقائيًا مع نوع عيّنة آخر"), ("Can be used with any specimen", "يمكن استعماله مع أي عيّنة"), ("Works better with urine", "يعمل أفضل مع الإدرار"), ("Needs no buffer", "لا يحتاج دارئًا")), "a"),
 {"topic_en": "Procedure and errors", "topic_ar": "الإجراء والأخطاء"},
 Q("The first step of the general workflow is:", "أوّل خطوة في خطوات العمل العامة:", O(("Start timer", "شغّل المؤقّت"), ("Check kit & expiry", "افحص العُدّة وتاريخ انتهائها"), ("Record result", "سجّل النتيجة"), ("Add buffer", "أضف الدارئ")), "b"),
 Q("Which is a pre-analytical / user error?", "أيّ مما يلي خطأ ما قبل التحليل / خطأ المستخدم؟", O(("Misreading faint lines", "قراءة خاطئة للخطوط الخفيفة"), ("Reading after the allowed time", "القراءة بعد الوقت المسموح"), ("Wrong buffer volume", "حجم دارئ خاطئ"), ("Failure of control line", "فشل خطّ السيطرة")), "c"),
 Q("Which is an analytical / interpretation error?", "أيّ مما يلي خطأ تحليل / تفسير؟", O(("Wrong specimen type", "نوع عيّنة خاطئ"), ("Cross-contamination", "تلوّث متبادل"), ("Expired kit", "عُدّة منتهية"), ("Cassette placed on an unsuitable surface", "وضع الكاسيت على سطح غير مناسب")), "d"),
 Q("Incorrect specimen volume can:", "حجم العيّنة الخاطئ قد:", O(("Disturb flow before the sample reaches the test line", "يخلّ بالتدفّق قبل أن تصل العيّنة إلى خطّ الفحص"), ("Make the kit validated for other specimens", "يجعل العُدّة صالحة لعيّنات أخرى"), ("Change the control line into a test line", "يحوّل خطّ السيطرة إلى خطّ فحص"), ("Have no effect", "لا يؤثّر")), "a"),
 Q("Which is a limitation of lateral-flow tests?", "أيّ مما يلي من قيود فحوص التدفّق الجانبي؟", O(("Fast results", "نتائج سريعة"), ("May be less sensitive than some laboratory methods", "قد تكون أقلّ حساسية من بعض الطرائق المختبرية"), ("Portable", "قابلة للحمل"), ("Useful near the patient", "مفيدة قرب المريض")), "b"),
 {"topic_en": "Picture questions", "topic_ar": "أسئلة الصور"},
 Q("In this picture, cassette (C) with no line at all is:", "في هذه الصورة، الكاسيت (C) الذي لا يظهر فيه أيّ خطّ:", O(("Positive", "موجب"), ("Negative", "سالب"), ("Invalid", "باطل"), ("Faint positive", "موجب خفيف")), "c", img="assets/results-abc.png", img_h="40mm"),
 Q("In this diagram, the gold-labelled antibody is stored in the:", "في هذا المخطّط، يُخزَّن الضدّ الموسوم بالذهب في:", O(("Sample pad", "وسادة العيّنة"), ("Absorbent pad", "الوسادة الماصّة"), ("Control line", "خطّ السيطرة"), ("Conjugate pad", "وسادة المقترن")), "d", img="assets/lfa-diagram.png", img_h="40mm"),
 Q("In this picture, what changes as the concentration rises (0 → 2 ng/mL)?", "في هذه الصورة، ما الذي يتغيّر كلّما زاد التركيز (`0 → 2 ng/mL`)؟", O(("The test line gets darker", "يغمق خطّ الفحص"), ("The control line disappears", "يختفي خطّ السيطرة"), ("The sample well changes colour", "يتغيّر لون حفرة العيّنة"), ("Nothing", "لا شيء")), "a", img="assets/faint-line.png", img_h="40mm"),
 Q("In this cassette, the letter S marks the:", "في هذا الكاسيت، الحرف `S` يشير إلى:", O(("Test line", "خطّ الفحص"), ("Sample well", "حفرة العيّنة"), ("Control line", "خطّ السيطرة"), ("Absorbent pad", "الوسادة الماصّة")), "b", img="assets/strip-in-hand.png", img_h="40mm"),
]
mcq = balance(mcq, 6)
tf = [
 TF("Immunochromatography needs specialized laboratory equipment.", "تحتاج الكروماتوغرافيا المناعية أجهزة مختبرية متخصّصة.", "F"),
 TF("The sample moves along the strip by capillary flow.", "تتحرّك العيّنة على طول الشريط بالتدفّق الشعري.", "T"),
 TF("The conjugate pad stores dried labeled antibodies or antigens.", "تخزّن وسادة المقترن أضدادًا أو مستضدّات موسومة مجفّفة.", "T"),
 TF("The test line shows that the test worked correctly.", "يُظهر خطّ الفحص أن الفحص عمل بصورة صحيحة.", "F"),
 TF("No control line means an invalid result.", "غياب خطّ السيطرة يعني نتيجة باطلة.", "T"),
 TF("Control line + no test line in a sandwich test is positive.", "خطّ السيطرة + عدم وجود خطّ الفحص في فحص الساندويتش نتيجة موجبة.", "F"),
 TF("A faint test line is always negative.", "خطّ الفحص الخفيف سالب دائمًا.", "F"),
 TF("You may read the cassette after the stated time window if the line is clearer.", "يجوز قراءة الكاسيت بعد نافذة الوقت إذا كان الخطّ أوضح.", "F"),
 TF("Line darkness should not be compared between different brands unless the kit supports it.", "لا يجوز مقارنة غمق الخطّ بين ماركات مختلفة إلا إذا دعمت العُدّة ذلك.", "T"),
 TF("Drugs and small molecules are often tested by the competitive format.", "الأدوية والجزيئات الصغيرة تُفحص غالبًا بالصيغة التنافسية.", "T"),
 TF("A test validated for serum can automatically be used with saliva.", "الفحص المُعتمَد للمصل يمكن استعماله تلقائيًا مع اللعاب.", "F"),
 TF("The exact number of drops and incubation time are test-specific.", "عدد القطرات الدقيق ووقت الحضن خاصّان بكل فحص.", "T"),
 TF("Lateral-flow tests usually give positive/negative results.", "تعطي فحوص التدفّق الجانبي عادةً نتائج موجب/سالب.", "T"),
 TF("Lateral-flow results never need confirmation by another test.", "نتائج التدفّق الجانبي لا تحتاج أبدًا تأكيدًا بفحص آخر.", "F"),
]
traps = [
 TR("Test line vs control line", "خطّ الفحص مقابل خطّ السيطرة", "T captures the target and gives the test signal; C only shows that the test worked. No C = invalid even if T appears.",
    "`T` يلتقط الهدف ويعطي إشارة الفحص؛ و`C` يُظهر فقط أن الفحص عمل. لا `C` = باطلة حتى لو ظهر `T`."),
 TR("Negative vs invalid", "السالب مقابل الباطل", "Negative = C appears, no T. Invalid = C does not appear (repeat the test).",
    "السالب = يظهر `C` ولا يظهر `T`. والباطل = لا يظهر `C` (أعد الفحص)."),
 TR("Faint line", "الخطّ الخفيف", "A faint T may be positive — but only if the manufacturer defines it so AND it appears within the reading time.",
    "خطّ `T` الخفيف قد يكون موجبًا — لكن فقط إذا عرّفته الشركة كذلك وظهر ضمن وقت القراءة."),
 TR("Sandwich vs competitive", "الساندويتش مقابل التنافسي", "Sandwich: T line = positive. Competitive (drugs/small molecules): weaker or absent T = positive. Identify the format before reading.",
    "الساندويتش: خطّ `T` = موجب. والتنافسي (الأدوية/الجزيئات الصغيرة): `T` أضعف أو غائب = موجب. حدّد الصيغة قبل القراءة."),
 TR("Conjugate pad vs sample pad", "وسادة المقترن مقابل وسادة العيّنة", "Sample pad receives/conditions the specimen; conjugate pad stores the dried labeled reagent (colloidal gold…).",
    "وسادة العيّنة تستقبل العيّنة وتهيّئها؛ ووسادة المقترن تخزّن الكاشف الموسوم المجفّف (الذهب الغروي…)."),
 TR("Reading time", "وقت القراءة", "Reading too early or after the allowed time is an interpretation error — always use the timer and the kit time window.",
    "القراءة المبكّرة أو بعد الوقت المسموح خطأ تفسير — استعمل المؤقّت ونافذة وقت العُدّة دائمًا."),
 TR("User error or interpretation error?", "خطأ مستخدم أم خطأ تفسير؟", "Specimen type, collection, sample/buffer volume, expired kit, contamination = pre-analytical/user. Timing, surface, control failure, faint lines, late reading, ignoring rules = analytical/interpretation.",
    "نوع العيّنة، الجمع، حجم العيّنة/الدارئ، العُدّة المنتهية، التلوّث = ما قبل التحليل/المستخدم. والتوقيت، السطح، فشل السيطرة، الخطوط الخفيفة، القراءة المتأخّرة، تجاهل القواعد = تحليل/تفسير."),
]
important = [
 IM("Quick Review 1: What causes the sample to move across the strip?", "سؤال المراجعة 1: ما الذي يحرّك العيّنة عبر الشريط؟",
    "Capillary flow (capillary migration) through the membrane; the absorbent pad pulls the fluid through the strip.",
    "التدفّق الشعري (الهجرة الشعرية) خلال الغشاء؛ والوسادة الماصّة تسحب السائل عبر الشريط."),
 IM("Quick Review 2: What is stored in the conjugate pad?", "سؤال المراجعة 2: ماذا يُخزَّن في وسادة المقترن؟",
    "Dried labeled detection reagents (labeled antibodies or antigens); labels may be colloidal gold or colored/fluorescent particles. They rehydrate when the sample arrives and form a migrating complex with the target.",
    "كواشف كشف موسومة مجفّفة (أضداد أو مستضدّات موسومة)؛ والوسوم قد تكون ذهبًا غرويًا أو جسيمات ملوّنة/متألّقة. تترطّب عند وصول العيّنة وتكوّن مع الهدف معقّدًا مهاجرًا."),
 IM("Quick Review 3: What is the function of the test line?", "سؤال المراجعة 3: ما وظيفة خطّ الفحص؟",
    "It captures the target and produces the test signal.", "يلتقط الهدف وينتج إشارة الفحص."),
 IM("Quick Review 4: When is a rapid test considered invalid?", "سؤال المراجعة 4: متى يُعدّ الفحص السريع باطلًا؟",
    "When the control line does not appear (no control line = invalid result), whatever the test line shows; the test must be repeated.",
    "عندما لا يظهر خطّ السيطرة (لا خطّ سيطرة = نتيجة باطلة)، مهما أظهر خطّ الفحص؛ ويجب إعادة الفحص."),
 IM("Quick Review 5: Why must the result be read at the correct time?", "سؤال المراجعة 5: لماذا يجب قراءة النتيجة في الوقت الصحيح؟",
    "A line (even faint) counts only if it appears within the permitted reading time; reading too early or after the stated time window gives false or unreliable results.",
    "الخطّ (حتى الخفيف) لا يُحتسب إلا إذا ظهر ضمن وقت القراءة المسموح؛ والقراءة المبكّرة أو بعد نافذة الوقت تعطي نتائج كاذبة أو غير موثوقة."),
 IM("Quick Review 6: What is the difference between sandwich and competitive formats?", "سؤال المراجعة 6: ما الفرق بين صيغتَي الساندويتش والتنافسية؟",
    "Sandwich: the target is held between the labeled antibody and the capture antibody at the T line, so a T line = positive (large analytes such as hCG). Competitive: the target competes with/blocks the labeled reagent, so a weaker or absent T line = positive (drugs, small molecules).",
    "الساندويتش: يُمسَك الهدف بين الضدّ الموسوم والضدّ الملتقِط عند خطّ `T`، فظهور `T` = موجب (مواد كبيرة مثل `hCG`). والتنافسية: الهدف ينافس الكاشف الموسوم أو يمنعه، فضعف أو غياب `T` = موجب (أدوية، جزيئات صغيرة)."),
 IM("Quick Review 7: Why can wrong sample volume affect the result?", "سؤال المراجعة 7: لماذا يؤثّر حجم العيّنة الخاطئ في النتيجة؟",
    "Incorrect specimen volume can disturb the flow before the sample reaches the test line (too little → no proper migration; too much → flooding), giving false or invalid results.",
    "حجم العيّنة الخاطئ قد يخلّ بالتدفّق قبل أن تصل العيّنة إلى خطّ الفحص (قليل جدًا ← هجرة غير كافية؛ كثير جدًا ← إغراق)، فتنتج نتائج كاذبة أو باطلة."),
 IM("Quick Review 8: Give two advantages of lateral-flow tests.", "سؤال المراجعة 8: اذكر ميزتين لفحوص التدفّق الجانبي.",
    "Any two of: fast results, easy to use, portable, needs little equipment, useful near the patient, can be used outside large laboratories.",
    "أيّ اثنتين من: نتائج سريعة، سهل الاستعمال، قابل للحمل، يحتاج أجهزة قليلة، مفيد قرب المريض، يمكن استعماله خارج المختبرات الكبيرة."),
]
meta = dict(subject_en="Advanced Techniques (Practical)", subject_ar="التقنيات المتقدمة العملي", short_ar="تقنيات متقدمة", instructor="ليندا منجد هادي",
            unit_en="Lab 2", unit_ar="العملي 2", unit_label="LAB", unit_no="2", title_en="Immunochromatographic Assays — Lateral Flow Immunoassays (LFIA)",
            title_ar="المقايسات الكروماتوغرافية المناعية — فحوص التدفّق الجانبي", department="قسم التحليلات", kind="Laboratories — عملي", stage="The third stage — الثالثة")
blocks, mcq, tf, traps, important = ltr_all(blocks), ltr_all(mcq), ltr_all(tf), ltr_all(traps), ltr_all(important)
save(FOLDER, meta, blocks, mcq, tf, traps, important)
fit(FOLDER)   # no big gaps (fill2 >= 80%)

```
