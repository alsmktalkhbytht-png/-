---
source: BIOS-Obsidian/tools/scripts/atl3/c3.py
handouts: [advtech-lab3-cie]
saved: 2026-11-13
tags: [bios, code]
---
# atl3/c3.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#advtech-lab3-cie|advtech-lab3-cie]]

```python
import sys; sys.path.insert(0, "/tmp/claude-0/-home-user-kwmdkm/44452a28-19bf-5ce8-890a-f6919e775f0b/scratchpad/imm456")
from ci import *            # c helpers + B INSHORT TERMS balance save(split.fix)
sys.path.insert(0, "/tmp/claude-0/-home-user-kwmdkm/44452a28-19bf-5ce8-890a-f6919e775f0b/scratchpad"); from bidi import ltr_all; from flowfit import fit

# Advanced Techniques practical, lab 3 — Counter Immunoelectrophoresis (CIE), pptx (15 slides, 10 pictures = 6 distinct;
# "Presented By : Linda Munjed Hadi"). Third stage → blush, questions merged. Slide 8 template text "Add image here" left out.
BN = lambda en, ar: N(en, ar, label=["BIOS note", "ملاحظة BIOS"])
O = P

blocks = [
 # ───────────────────────── 1
 SEC("What is CIE?", "ما هو CIE؟"),
 N("Practical Laboratory Lecture · Presented By : Linda Munjed Hadi", "محاضرة مختبرية عملية · تقديم: ليندا منجد هادي", label=["Lab sheet", "ورقة العملي"]),
 L(["CIE is a **rapid immunological test**.", "It detects a **specific antigen or antibody**.",
    "The test uses an **electric current** to move antigen and antibody **toward each other**.", "A **visible precipitation line** means a reaction occurred."],
   ["`CIE` **فحص مناعي سريع**.", "يكشف **مستضدًّا أو ضدًّا نوعيًا**.",
    "يستعمل الفحص **تيارًا كهربائيًا** لتحريك المستضدّ والضدّ **نحو بعضهما**.", "و**خطّ الترسيب المرئي** يعني حدوث التفاعل."]),
 F("cie-scheme.png", "COUNTER IMMUNOELECTROPHORESIS: Ag moves from the CATHODE side and Ab from the ANODE side toward each other",
   "الرحلان الكهربائي المناعي المعاكس: يتحرّك المستضدّ `(Ag)` من جهة **المهبط** والضدّ `(Ab)` من جهة **المصعد** نحو بعضهما", h="44mm"),
 INSHORT([("CIE = **rapid** immunological test for a **specific antigen or antibody**.", "`CIE` = فحص مناعي **سريع** لـ**مستضدّ أو ضدّ نوعي**."),
          ("**Electric current** moves Ag and Ab **toward each other**; a **line** = reaction.", "**التيار الكهربائي** يحرّك المستضدّ والضدّ **نحو بعضهما**؛ و**الخطّ** = تفاعل.")]),

 # ───────────────────────── 2
 SEC("Basic idea and principle", "الفكرة الأساسية والمبدأ"),
 FLOW([("Antigen", "المستضدّ"), ("Electric field", "المجال الكهربائي"), ("Antibody", "الضدّ"), ("Meet in gel", "يلتقيان في الهلام"), ("Precipitation line", "خطّ الترسيب")],
      en="Basic Idea", ar="الفكرة الأساسية"),
 C("**Key idea:** electricity makes the reaction **faster than simple diffusion**.", "**الفكرة المفتاحية:** الكهرباء تجعل التفاعل **أسرع من الانتشار البسيط**."),
 H2("Principle of CIE", "مبدأ CIE"),
 L(["Antigen and antibody are placed in **separate wells** in an **agarose gel**.", "An **electric field** is applied.", "They **move toward each other**.",
    "When they meet at the **right proportion**, a **precipitin line** forms."],
   ["يوضع المستضدّ والضدّ في **حُفَر منفصلة** في **هلام الآغاروز**.", "يُطبَّق **مجال كهربائي**.", "**يتحرّكان نحو بعضهما**.",
    "وعندما يلتقيان **بالنسبة الصحيحة** يتكوّن **خطّ الترسيب**."]),
 F("cie-principle.png", "Counter immunoelectrophoresis principle: Cathode, Electric current →, Anode; Agarose; Wells containing antigen and antibody; Precipitin line; Slide",
   "مبدأ الرحلان الكهربائي المناعي المعاكس: المهبط، التيار الكهربائي ←، المصعد؛ الآغاروز؛ حُفَر فيها المستضدّ والضدّ؛ خطّ الترسيب؛ الشريحة", h="44mm"),
 BN("Why do they move in **opposite** directions? At the alkaline buffer pH the **antigen** is negatively charged and runs to the **anode**, while the **antibody** (IgG) is carried back toward the **cathode** by electro-endosmosis — so the antigen is put in the **cathode** well and the antibody in the **anode** well.",
    "لماذا يتحرّكان باتّجاهين **متعاكسين**؟ عند `pH` الدارئ القاعدي يكون **المستضدّ** سالب الشحنة فيتّجه إلى **المصعد**، بينما يُسحب **الضدّ** (`IgG`) نحو **المهبط** بالتناضح الكهربائي — لذلك يوضع المستضدّ في حفرة **المهبط** والضدّ في حفرة **المصعد**."),
 INSHORT([("Electricity → reaction **faster than simple diffusion**.", "الكهرباء ← تفاعل **أسرع من الانتشار البسيط**."),
          ("Separate wells in **agarose** → electric field → they meet → at the **right proportion** a **precipitin line** forms.", "حُفَر منفصلة في **الآغاروز** ← مجال كهربائي ← يلتقيان ← وعند **النسبة الصحيحة** يتكوّن **خطّ الترسيب**.")]),

 # ───────────────────────── 3
 SEC("Materials and gel set-up", "المواد وتجهيز الهلام"),
 L(["Agarose gel", "Glass slide or gel plate", "Electrophoresis chamber and power supply", "Buffer solution", "Antigen sample", "Specific antibody", "Micropipette and tips"],
   ["هلام الآغاروز", "شريحة زجاجية أو صفيحة هلام", "حجرة الرحلان الكهربائي ومجهّز القدرة", "محلول دارئ", "عيّنة المستضدّ", "الضدّ النوعي", "ماصّة دقيقة ورؤوسها"],
   en="**Materials Needed**", ar="**المواد المطلوبة**"),
 F("cie-apparatus.png", "CIE set-up: gel slide with antigen and antiserum wells in an electrophoresis tank connected to a DC power supply",
   "تجهيز `CIE`: شريحة هلام فيها حُفَر المستضدّ والمصل المضاد في حوض الرحلان الكهربائي موصولة بمجهّز تيار مستمر", h="78mm"),
 T([B("Figure text", "كتابات الشكل"), B("Arabic", "بالعربي")],
   [[B("**Cathode (–)** / **Anode (+)**", "**المهبط (–)** / **المصعد (+)**"), B("negative / positive electrode", "القطب السالب / الموجب")],
    [B("**Antigen wells** / **Antiserum wells**", "**حُفَر المستضدّ** / **حُفَر المصل المضاد**"), B("antigen near the cathode, antiserum near the anode", "المستضدّ قرب المهبط، والمصل المضاد قرب المصعد")],
    [B("**Top view of gel slide (well arrangement)**", "**منظر علوي لشريحة الهلام (ترتيب الحُفَر)**"), B("two rows of wells facing each other", "صفّان من الحُفَر متقابلان")],
    [B("**Electrode buffer reservoir (running buffer)**", "**خزّان دارئ القطب (دارئ التشغيل)**"), B("buffer on each side", "دارئ على كل جهة")],
    [B("**Filter paper wick (moistened with buffer)**", "**فتيل ورق ترشيح (مبلّل بالدارئ)**"), B("connects the buffer to the gel", "يوصل الدارئ بالهلام")],
    [B("**Agarose gel (on glass slide)**", "**هلام الآغاروز (على شريحة زجاجية)**"), B("medium in which Ag and Ab move", "الوسط الذي يتحرّك فيه المستضدّ والضدّ")],
    [B("**Electrophoresis bridge (slide support)**", "**جسر الرحلان (حامل الشريحة)**"), B("holds the slide", "يحمل الشريحة")],
    [B("**DC POWER SUPPLY**", "**مجهّز تيار مستمر**"), B("gives the electric field", "يعطي المجال الكهربائي")]],
   key_cols=[0], widths=[55, 45], label_en="Figure text", label_ar="كتابات الشكل"),
 F("cie-plate.png", "Electrophoresis plate used for CIE: corresponding wells 3 mm in diameter; distance between the two wells 3 mm",
   "صفيحة الرحلان المستعملة في `CIE`: حُفَر متقابلة قطرها 3 ملم؛ والمسافة بين الحفرتين 3 ملم", h="56mm"),
 C("Image adapted from the reference slides provided for this lecture.", "الصورة مقتبسة من الشرائح المرجعية المقدّمة لهذه المحاضرة."),
 H2("Gel Setup", "تجهيز الهلام"),
 L(["Two **small wells** are made in the agarose gel.", "One well receives the **antigen**.", "The other well receives the **antibody**.",
    "The wells are placed **close enough** for the reaction to occur."],
   ["تُعمل **حفرتان صغيرتان** في هلام الآغاروز.", "تستقبل إحدى الحفرتين **المستضدّ**.", "وتستقبل الأخرى **الضدّ**.",
    "وتوضع الحفرتان **قريبتين بما يكفي** لحدوث التفاعل."]),
 INSHORT([("Materials: **agarose, slide/plate, chamber + power supply, buffer, antigen, specific antibody, micropipette**.", "المواد: **آغاروز، شريحة/صفيحة، حجرة + مجهّز قدرة، دارئ، مستضدّ، ضدّ نوعي، ماصّة دقيقة**."),
          ("Two small wells, **close enough** (in the plate: wells 3 mm, 3 mm apart).", "حفرتان صغيرتان **قريبتان** (في الصفيحة: قطر 3 ملم ومسافة 3 ملم).")]),

 # ───────────────────────── 4
 SEC("Procedure and results", "خطوات العمل والنتائج"),
 L(["Prepare the **agarose gel**.", "Make **two wells** in the gel.", "Add **antigen** to one well and **antibody** to the other.", "Place the gel in the **electrophoresis chamber**.",
    "Apply the **electric current** for the required time.", "Observe the gel for a **precipitation line**."],
   ["حضّر **هلام الآغاروز**.", "اعمل **حفرتين** في الهلام.", "أضف **المستضدّ** إلى إحدى الحفرتين و**الضدّ** إلى الأخرى.", "ضع الهلام في **حجرة الرحلان الكهربائي**.",
    "طبّق **التيار الكهربائي** للمدّة المطلوبة.", "افحص الهلام بحثًا عن **خطّ الترسيب**."],
   en="**Practical Procedure**", ar="**خطوات العمل**"),
 FLOW([("Prepare gel", "تحضير الهلام"), ("2 wells", "حفرتان"), ("Ag + Ab", "مستضدّ + ضدّ"), ("Chamber", "الحجرة"), ("Current", "التيار"), ("Look for line", "البحث عن الخطّ")],
      en="6 steps", ar="6 خطوات"),
 H2("Positive Result", "النتيجة الموجبة"),
 C(["A **visible precipitin line** appears between the wells.", "This means the antigen **reacted with its specific antibody**."],
   ["يظهر **خطّ ترسيب مرئي** بين الحفرتين.", "وهذا يعني أن المستضدّ **تفاعل مع ضدّه النوعي**."]),
 H2("Negative Result", "النتيجة السالبة"),
 C(["**No precipitin line** appears between the wells.", "This means **no visible antigen–antibody precipitation** was detected."],
   ["**لا يظهر خطّ ترسيب** بين الحفرتين.", "وهذا يعني أنه **لم يُكشف ترسيب مرئي بين المستضدّ والضدّ**."]),
 FF(("precipitin-line.png", "Positive: a precipitin line between the two wells", "موجب: خطّ ترسيب بين الحفرتين", "38mm"),
    ("precipitin-examples.png", "Examples of precipitin lines (Dils. A–H; SERA / ANTIGEN)", "أمثلة لخطوط الترسيب (التخافيف A–H؛ الأمصال / المستضدّ)", "38mm")),
 INSHORT([("Procedure: **gel → 2 wells → Ag + Ab → chamber → current → look for a line**.", "الخطوات: **هلام ← حفرتان ← مستضدّ + ضدّ ← الحجرة ← التيار ← البحث عن الخطّ**."),
          ("**Line = positive** (Ag reacted with its specific Ab); **no line = negative**.", "**الخطّ = موجب** (تفاعل المستضدّ مع ضدّه)؛ **لا خطّ = سالب**.")]),

 # ───────────────────────── 5
 SEC("Why a line forms and what affects it", "سبب تكوّن الخطّ وما يؤثّر فيه"),
 L(["Antigen **binds to its specific antibody**.", "Many antigen–antibody **complexes join together**.", "The complexes become **large enough to be seen as a white line**."],
   ["يرتبط المستضدّ **بضدّه النوعي**.", "تتّحد **معقّدات** مستضدّ–ضدّ كثيرة معًا.", "وتصبح المعقّدات **كبيرة بما يكفي لتُرى خطًّا أبيض**."],
   en="**Why Does a Line Form?**", ar="**لماذا يتكوّن الخطّ؟**"),
 L(["Correct **antigen and antibody concentration**", "Correct **well distance**", "Proper **buffer and pH**", "Correct **voltage and running time**", "Good **gel preparation**"],
   ["التركيز الصحيح **للمستضدّ والضدّ**", "**المسافة** الصحيحة بين الحُفَر", "**الدارئ والأس الهيدروجيني** المناسبان", "**الفولتية ومدّة التشغيل** الصحيحتان", "**تحضير جيد للهلام**"],
   en="**Factors That Affect the Result**", ar="**العوامل المؤثّرة في النتيجة**"),
 BN("A line needs the **zone of equivalence**: with too much antigen or too much antibody the complexes stay small and soluble, so a false negative can occur — this is why the **right proportion / concentration** matters.",
    "يحتاج الخطّ إلى **منطقة التكافؤ**: فمع زيادة المستضدّ أو زيادة الضدّ تبقى المعقّدات صغيرة وذائبة، فقد تظهر نتيجة سالبة كاذبة — ولهذا تهمّ **النسبة / التركيز الصحيح**."),
 INSHORT([("Line = **many Ag–Ab complexes** joined → big enough to see (white line).", "الخطّ = **معقّدات مستضدّ–ضدّ كثيرة** متّحدة ← كبيرة بما يكفي لتُرى (خطّ أبيض)."),
          ("5 factors: **concentration, well distance, buffer/pH, voltage/time, gel**.", "5 عوامل: **التركيز، والمسافة، والدارئ/الأس الهيدروجيني، والفولتية/الوقت، والهلام**.")]),

 # ───────────────────────── 6
 SEC("Advantages, limitations and summary", "المزايا والقيود والخلاصة"),
 L(["Simple technique", "Faster than passive diffusion methods", "Low-cost equipment", "Visible result", "Useful for teaching antigen–antibody reactions"],
   ["تقنية بسيطة", "أسرع من طرائق الانتشار المنفعل", "أجهزة قليلة الكلفة", "نتيجة مرئية", "مفيدة لتعليم تفاعلات المستضدّ–الضدّ"],
   en="**Advantages**", ar="**المزايا**"),
 L(["Less sensitive than many modern immunoassays", "Usually gives a qualitative result", "Needs an electrophoresis setup", "Weak lines may be difficult to see", "Correct test conditions are important"],
   ["أقل حساسية من كثير من الفحوص المناعية الحديثة", "تعطي غالبًا نتيجة نوعية (وصفية)", "تحتاج تجهيز رحلان كهربائي", "الخطوط الضعيفة قد يصعب رؤيتها", "ظروف الفحص الصحيحة مهمّة"],
   en="**Limitations**", ar="**القيود**"),
 L(["CIE combines **immunology with electrophoresis**.", "Antigen and antibody **move toward each other** in agarose gel.", "A **precipitin line** indicates a **positive** reaction.",
    "The method is **simple, fast, and mainly qualitative**."],
   ["يجمع `CIE` بين **علم المناعة والرحلان الكهربائي**.", "يتحرّك المستضدّ والضدّ **نحو بعضهما** في هلام الآغاروز.", "و**خطّ الترسيب** يدلّ على تفاعل **موجب**.",
    "والطريقة **بسيطة وسريعة ونوعية أساسًا**."],
   en="**Summary**", ar="**الخلاصة**"),
] + TERMS([
 ("Counter immunoelectrophoresis (CIE)", "الرحلان الكهربائي المناعي المعاكس / الهجرة الكهربائية المناعية المتعاكسة"),
 ("Electrophoresis", "الرحلان الكهربائي / الهجرة الكهربائية"),
 ("Antigen / antibody", "المستضدّ / الضدّ (الجسم المضاد)"),
 ("Antiserum", "المصل المضاد"),
 ("Agarose gel", "هلام الآغاروز"),
 ("Precipitin (precipitation) line", "خطّ الترسيب"),
 ("Cathode / anode", "المهبط (القطب السالب) / المصعد (القطب الموجب)"),
 ("Electric field / current", "المجال الكهربائي / التيار الكهربائي"),
 ("Simple (passive) diffusion", "الانتشار البسيط (المنفعل)"),
 ("Buffer", "المحلول الدارئ / المنظّم"),
 ("Wells", "الحُفَر / الآبار"),
 ("Qualitative", "نوعي / وصفي (لا كمّي)"),
 ("Immunoassay", "فحص مناعي / مقايسة مناعية"),
])

# ───────────────────────── questions
mcq = [
 {"topic_en": "What is CIE and its principle", "topic_ar": "ما هو CIE ومبدؤه"},
 Q("CIE stands for:", "اختصار CIE يعني:", O(("Counter immunoelectrophoresis", "الرحلان الكهربائي المناعي المعاكس"), ("Cellular immune electrophoresis", "الرحلان المناعي الخلوي"), ("Complement immune enzyme", "إنزيم المتمّم المناعي"), ("Capillary immuno-ELISA", "إليزا شعرية")), "a"),
 Q("CIE detects:", "يكشف CIE:", O(("Glucose", "الكلوكوز"), ("A specific antigen or antibody", "مستضدًّا أو ضدًّا نوعيًا"), ("DNA sequences", "تسلسلات DNA"), ("Blood cells", "خلايا الدم")), "b"),
 Q("In CIE, antigen and antibody are moved toward each other by:", "في CIE يتحرّك المستضدّ والضدّ نحو بعضهما بفعل:", O(("Gravity", "الجاذبية"), ("Centrifugation", "الطرد المركزي"), ("An electric current", "تيار كهربائي"), ("Heating", "التسخين")), "c"),
 Q("A visible precipitation line in CIE means:", "خطّ الترسيب المرئي في CIE يعني:", O(("The gel is broken", "الهلام مكسور"), ("No reaction", "لا تفاعل"), ("Too much current", "تيار زائد"), ("A reaction occurred", "حدث تفاعل")), "d"),
 Q("Electricity in CIE makes the reaction:", "الكهرباء في CIE تجعل التفاعل:", O(("Faster than simple diffusion", "أسرع من الانتشار البسيط"), ("Slower", "أبطأ"), ("Quantitative", "كمّيًا"), ("Invisible", "غير مرئي")), "a"),
 Q("In CIE, antigen and antibody are placed in:", "في CIE يوضع المستضدّ والضدّ في:", O(("The same well", "الحفرة نفسها"), ("Separate wells in an agarose gel", "حُفَر منفصلة في هلام الآغاروز"), ("A test tube", "أنبوب اختبار"), ("Blood agar", "آغار الدم")), "b"),
 Q("The precipitin line forms when antigen and antibody meet:", "يتكوّن خطّ الترسيب عندما يلتقي المستضدّ والضدّ:", O(("In any amount", "بأي كمية"), ("Without an electric field", "بلا مجال كهربائي"), ("At the right proportion", "بالنسبة الصحيحة"), ("At the cathode only", "عند المهبط فقط")), "c"),
 {"topic_en": "Materials, procedure and results", "topic_ar": "المواد والخطوات والنتائج"},
 Q("Which is NOT among the materials needed for CIE?", "أيّها ليس من المواد المطلوبة لـ CIE؟", O(("Agarose gel", "هلام الآغاروز"), ("Buffer solution", "محلول دارئ"), ("Specific antibody", "ضدّ نوعي"), ("Blood agar plate", "طبق آغار الدم")), "d"),
 Q("How many wells are made in the gel?", "كم حفرة تُعمل في الهلام؟", O(("Two", "اثنتان"), ("One", "واحدة"), ("Five", "خمس"), ("None", "ولا واحدة")), "a"),
 Q("The wells must be placed:", "يجب أن توضع الحُفَر:", O(("At the ends of the gel", "عند طرفي الهلام"), ("Close enough for the reaction to occur", "قريبة بما يكفي لحدوث التفاعل"), ("Outside the gel", "خارج الهلام"), ("In different gels", "في هلامين مختلفين")), "b"),
 Q("The first step of the practical procedure is:", "الخطوة الأولى في العمل:", O(("Apply the current", "تطبيق التيار"), ("Observe the line", "ملاحظة الخطّ"), ("Prepare the agarose gel", "تحضير هلام الآغاروز"), ("Add the antibody", "إضافة الضدّ")), "c"),
 Q("The last step of the practical procedure is:", "الخطوة الأخيرة في العمل:", O(("Make two wells", "عمل حفرتين"), ("Prepare the gel", "تحضير الهلام"), ("Add antigen", "إضافة المستضدّ"), ("Observe the gel for a precipitation line", "فحص الهلام بحثًا عن خطّ الترسيب")), "d"),
 Q("A negative CIE result is:", "نتيجة CIE السالبة:", O(("No precipitin line between the wells", "لا خطّ ترسيب بين الحفرتين"), ("Two lines", "خطّان"), ("A red colour", "لون أحمر"), ("Bubbles", "فقاعات")), "a"),
 Q("A positive CIE result means the antigen:", "نتيجة CIE الموجبة تعني أن المستضدّ:", O(("Was destroyed", "تحطّم"), ("Reacted with its specific antibody", "تفاعل مع ضدّه النوعي"), ("Did not move", "لم يتحرّك"), ("Reached the anode only", "وصل المصعد فقط")), "b"),
 {"topic_en": "Line formation, factors, advantages and limitations", "topic_ar": "تكوّن الخطّ والعوامل والمزايا والقيود"},
 Q("The line becomes visible because:", "يصبح الخطّ مرئيًا لأن:", O(("The gel melts", "الهلام يذوب"), ("The buffer changes colour", "الدارئ يتغيّر لونه"), ("Many antigen–antibody complexes join and become large enough to be seen", "معقّدات مستضدّ–ضدّ كثيرة تتّحد وتكبر بما يكفي لتُرى"), ("Electricity burns the gel", "الكهرباء تحرق الهلام")), "c"),
 Q("The precipitin line appears as a:", "يظهر خطّ الترسيب كخطّ:", O(("Red line", "أحمر"), ("Blue line", "أزرق"), ("Black line", "أسود"), ("White line", "أبيض")), "d"),
 Q("Which is NOT a factor affecting the CIE result?", "أيّها ليس من العوامل المؤثّرة في نتيجة CIE؟", O(("Colour of the slide box", "لون علبة الشرائح"), ("Well distance", "المسافة بين الحُفَر"), ("Buffer and pH", "الدارئ والأس الهيدروجيني"), ("Voltage and running time", "الفولتية ومدّة التشغيل")), "a"),
 Q("An advantage of CIE is that it is:", "من مزايا CIE أنه:", O(("Highly quantitative", "كمّي جدًا"), ("Faster than passive diffusion methods", "أسرع من طرائق الانتشار المنفعل"), ("More sensitive than modern immunoassays", "أكثر حساسية من الفحوص الحديثة"), ("Without equipment", "بلا أجهزة")), "b"),
 Q("A limitation of CIE is that it:", "من قيود CIE أنه:", O(("Gives an invisible result", "يعطي نتيجة غير مرئية"), ("Is very expensive", "مكلف جدًا"), ("Usually gives a qualitative result", "يعطي غالبًا نتيجة نوعية"), ("Needs no electrophoresis setup", "لا يحتاج تجهيز رحلان")), "c"),
 Q("Compared with many modern immunoassays, CIE is:", "مقارنة بكثير من الفحوص المناعية الحديثة، يكون CIE:", O(("More sensitive", "أكثر حساسية"), ("Fully automated", "مؤتمتًا بالكامل"), ("Quantitative", "كمّيًا"), ("Less sensitive", "أقل حساسية")), "d"),
 Q("CIE combines immunology with:", "يجمع CIE بين علم المناعة و:", O(("Electrophoresis", "الرحلان الكهربائي"), ("Microscopy", "المجهرية"), ("Culture", "الزرع"), ("Spectrophotometry", "قياس الطيف الضوئي")), "a"),
 {"topic_en": "Picture questions", "topic_ar": "أسئلة الصور"},
 Q("In this figure, the antigen well is on the side of the:", "في هذا الشكل، حفرة المستضدّ تقع جهة:", O(("Anode", "المصعد"), ("Cathode", "المهبط"), ("Power supply", "مجهّز القدرة"), ("Buffer only", "الدارئ فقط")), "b", img="assets/cie-principle.png", img_h="34mm"),
 Q("In this picture, the dark line between the two wells is:", "في هذه الصورة، الخطّ الداكن بين الحفرتين:", O(("A crack in the gel", "شقّ في الهلام"), ("Dye", "صبغة"), ("A precipitin line (positive)", "خطّ ترسيب (موجب)"), ("The electrode", "القطب")), "c", img="assets/precipitin-line.png", img_h="28mm"),
 Q("In this plate, the distance between the two wells is:", "في هذه الصفيحة، المسافة بين الحفرتين:", O(("1 cm", "1 سم"), ("10 mm", "10 ملم"), ("30 mm", "30 ملم"), ("3 mm", "3 ملم")), "d", img="assets/cie-plate.png", img_h="36mm"),
]
mcq = balance(mcq, 33)

tf = [
 TF("CIE is a rapid immunological test.", "CIE فحص مناعي سريع.", "T"),
 TF("CIE uses gravity to move antigen and antibody.", "يستعمل CIE الجاذبية لتحريك المستضدّ والضدّ.", "F"),
 TF("In CIE, antigen and antibody move toward each other.", "في CIE يتحرّك المستضدّ والضدّ نحو بعضهما.", "T"),
 TF("CIE is slower than simple diffusion.", "CIE أبطأ من الانتشار البسيط.", "F"),
 TF("Antigen and antibody are placed in the same well.", "يوضع المستضدّ والضدّ في الحفرة نفسها.", "F"),
 TF("A precipitin line forms when antigen and antibody meet at the right proportion.", "يتكوّن خطّ الترسيب عندما يلتقي المستضدّ والضدّ بالنسبة الصحيحة.", "T"),
 TF("A buffer solution is one of the materials needed.", "المحلول الدارئ من المواد المطلوبة.", "T"),
 TF("No precipitin line between the wells is a positive result.", "عدم ظهور خطّ ترسيب بين الحفرتين نتيجة موجبة.", "F"),
 TF("The line forms when many antigen–antibody complexes join together.", "يتكوّن الخطّ عندما تتّحد معقّدات مستضدّ–ضدّ كثيرة معًا.", "T"),
 TF("Well distance does not affect the result.", "المسافة بين الحُفَر لا تؤثّر في النتيجة.", "F"),
 TF("CIE needs low-cost equipment.", "يحتاج CIE أجهزة قليلة الكلفة.", "T"),
 TF("CIE usually gives a quantitative result.", "يعطي CIE غالبًا نتيجة كمّية.", "F"),
 TF("Weak lines may be difficult to see.", "قد يصعب رؤية الخطوط الضعيفة.", "T"),
]

traps = [
 TR("Faster than what?", "أسرع من ماذا؟", "CIE is faster than simple (passive) DIFFUSION methods — but it is LESS sensitive than many modern immunoassays.", "CIE أسرع من طرائق الانتشار البسيط (المنفعل) — لكنه أقل حساسية من كثير من الفحوص المناعية الحديثة."),
 TR("Same well or separate wells?", "حفرة واحدة أم حفرتان؟", "SEPARATE wells: antigen in one, antibody in the other; they move toward each other.", "حفرتان منفصلتان: المستضدّ في واحدة والضدّ في الأخرى؛ ويتحرّكان نحو بعضهما."),
 TR("Line = positive", "الخطّ = موجب", "A precipitin line = POSITIVE (Ag reacted with its specific Ab); no line = negative.", "خطّ الترسيب = موجب (تفاعل المستضدّ مع ضدّه)؛ ولا خطّ = سالب."),
 TR("Any amount gives a line?", "أي كمية تعطي خطًّا؟", "No — only the RIGHT PROPORTION (correct concentration) forms a visible line.", "لا — فقط النسبة الصحيحة (التركيز الصحيح) تكوّن خطًّا مرئيًا."),
 TR("Qualitative or quantitative?", "نوعي أم كمّي؟", "CIE is mainly QUALITATIVE (present / absent), not a measurement of amount.", "CIE نوعي أساسًا (موجود / غير موجود)، لا يقيس الكمية."),
 TR("Colour of the line", "لون الخطّ", "The precipitin line is seen as a WHITE line in the gel (stained gels may show it dark).", "يُرى خطّ الترسيب خطًّا أبيض في الهلام (وفي الهلام المصبوغ قد يظهر داكنًا)."),
]

important = [
 IM("What does CIE stand for?", "ماذا يعني اختصار CIE؟",
    "Counter Immunoelectrophoresis — a rapid immunological test that detects a specific antigen or antibody using an electric current.",
    "الرحلان الكهربائي المناعي المعاكس — فحص مناعي سريع يكشف مستضدًّا أو ضدًّا نوعيًا باستعمال تيار كهربائي."),
 IM("What is the role of the electric field?", "ما دور المجال الكهربائي؟",
    "It moves the antigen and antibody toward each other in the agarose gel, so they meet and react faster than by simple diffusion.",
    "يحرّك المستضدّ والضدّ نحو بعضهما في هلام الآغاروز، فيلتقيان ويتفاعلان أسرع من الانتشار البسيط."),
 IM("Where are antigen and antibody placed?", "أين يوضع المستضدّ والضدّ؟",
    "In two separate small wells made in the agarose gel, close enough for the reaction to occur — antigen in one well, antibody in the other.",
    "في حفرتين صغيرتين منفصلتين في هلام الآغاروز، قريبتين بما يكفي لحدوث التفاعل — المستضدّ في حفرة والضدّ في الأخرى."),
 IM("What does a precipitin line mean?", "ماذا يعني خطّ الترسيب؟",
    "A positive result: the antigen reacted with its specific antibody; many Ag–Ab complexes joined and became large enough to be seen as a white line.",
    "نتيجة موجبة: تفاعل المستضدّ مع ضدّه النوعي؛ واتّحدت معقّدات مستضدّ–ضدّ كثيرة وكبرت بما يكفي لتُرى خطًّا أبيض."),
 IM("List the steps of the CIE practical procedure.", "عدّد خطوات عمل CIE.",
    "1. Prepare the agarose gel. 2. Make two wells. 3. Add antigen to one well and antibody to the other. 4. Place the gel in the electrophoresis chamber. 5. Apply the current for the required time. 6. Observe for a precipitation line.",
    "1. تحضير هلام الآغاروز. 2. عمل حفرتين. 3. إضافة المستضدّ إلى حفرة والضدّ إلى الأخرى. 4. وضع الهلام في حجرة الرحلان. 5. تطبيق التيار للمدّة المطلوبة. 6. البحث عن خطّ الترسيب."),
 IM("What factors affect the CIE result? Give its advantages and limitations.", "ما العوامل المؤثّرة في نتيجة CIE؟ واذكر مزاياه وقيوده.",
    "Factors: antigen/antibody concentration, well distance, buffer and pH, voltage and running time, gel preparation. Advantages: simple, faster than passive diffusion, low-cost, visible result, good for teaching. Limitations: less sensitive than modern immunoassays, qualitative, needs electrophoresis setup, weak lines hard to see, conditions must be correct.",
    "العوامل: تركيز المستضدّ/الضدّ، والمسافة بين الحُفَر، والدارئ والأس الهيدروجيني، والفولتية والوقت، وتحضير الهلام. المزايا: بسيط، وأسرع من الانتشار المنفعل، وقليل الكلفة، ونتيجة مرئية، ومفيد للتعليم. القيود: أقل حساسية من الفحوص الحديثة، ونوعي، ويحتاج تجهيز رحلان، والخطوط الضعيفة صعبة الرؤية، والظروف يجب أن تكون صحيحة."),
]

meta = {"subject_en": "Advanced Techniques (Practical)", "subject_ar": "التقنيات المتقدمة العملي", "short_ar": "تقنيات متقدمة", "instructor": "ليندا منجد هادي",
        "unit_en": "Lab 3", "unit_ar": "العملي 3", "unit_label": "LAB", "unit_no": "3",
        "title_en": "Counter Immunoelectrophoresis (CIE)", "title_ar": "الرحلان الكهربائي المناعي المعاكس",
        "department": "قسم التحليلات", "kind": "Laboratories — عملي", "stage": "The third stage — الثالثة"}
blocks, mcq, tf, traps, important = ltr_all(blocks), ltr_all(mcq), ltr_all(tf), ltr_all(traps), ltr_all(important)
save("advtech-lab3-cie", meta, blocks, mcq, tf, traps, important)
fit("advtech-lab3-cie", min_gap=0.08)   # no big gaps, small ones too

```
