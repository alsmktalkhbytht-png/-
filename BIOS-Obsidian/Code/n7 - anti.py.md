---
source: BIOS-Obsidian/tools/scripts/n7/anti.py
handouts: [hematology-practical-anticoagulants]
saved: 2026-10-30
tags: [bios, code]
---
# n7/anti.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#hematology-practical-anticoagulants|hematology-practical-anticoagulants]]

```python
from c import *

blocks = [
 SEC("What Are Anticoagulants?", "ما مانعات التخثّر؟"),
 C("**Substances that prevent or reduce blood clotting.**", "**مواد تمنع تخثّر الدم أو تقلّله.**",
   list_en=["Prevent clot formation in collected blood.", "Preserve blood cells for laboratory analysis.", "Allow plasma to be obtained for appropriate tests.", "Examples: **EDTA, heparin, sodium citrate**."],
   list_ar=["تمنع تكوّن الخثرة في الدم المجموع.", "تحافظ على خلايا الدم للتحليل المختبري.", "تتيح الحصول على البلازما للفحوص المناسبة.", "أمثلة: **`EDTA`، الهيبارين، سترات الصوديوم**."]),
 FF(("clotted-vs-anticoagulated.jpg", "Clotted blood vs. anticoagulated blood", "دم متخثّر مقابل دم مضاف إليه مانع تخثّر", "62mm"), ("clot-in-tube.jpg", "A clot in a tube without anticoagulant", "خثرة في أنبوب بلا مانع تخثّر", "62mm")),
 F("types-of-anticoagulants.jpg", "Types of anticoagulants: laboratory (in-vitro), clinical (in-vivo) and natural (in the body)", "أنواع مانعات التخثّر: المختبرية (خارج الجسم)، والسريرية (داخل الجسم)، والطبيعية (في الجسم)", h="118mm"),
 T(["Group (from the figure)", "Examples", "المجموعة — الأمثلة"],
   [["I. Laboratory (In-Vitro)", "EDTA (lavender), sodium citrate (light blue), heparin (green), oxalate fluoride (grey)", "**المختبرية (خارج الجسم)**: `EDTA` (بنفسجي)، سترات الصوديوم (أزرق فاتح)، الهيبارين (أخضر)، أوكزالات الفلورايد (رمادي)"],
    ["II. Clinical (In-Vivo)", "Heparin, LMWH (enoxaparin, dalteparin), warfarin (vitamin K antagonist), DOACs (dabigatran, rivaroxaban)", "**السريرية (داخل الجسم)**: الهيبارين، الهيبارين منخفض الوزن الجزيئي (إينوكسابارين، دالتيبارين)، الوارفارين (مضاد فيتامين `K`)، مانعات التخثّر الفموية المباشرة (دابيغاتران، ريفاروكسابان)"],
    ["III. Natural (In the Body)", "Antithrombin III (inhibits thrombin), protein C & S (inactivate clotting factors), heparan sulfate (enhances antithrombin)", "**الطبيعية (في الجسم)**: مضاد الثرومبين الثالث (يثبّط الثرومبين)، البروتين `C` و`S` (يعطّلان عوامل التخثّر)، كبريتات الهيباران (تعزّز مضاد الثرومبين)"]],
   ar_cols=[2], key_cols=[0], widths=["30mm", "", ""]),

 SEC("Properties of a Good Anticoagulant", "خصائص مانع التخثّر الجيد"),
 L(["Prevents blood clotting effectively.", "Does **not cause hemolysis**.", "Does **not alter blood composition**.", "**Preserves normal cell size and shape.**", "Does **not interfere with test results**."],
   ["يمنع تخثّر الدم بفعالية.", "**لا يسبّب تحلّل الدم**.", "**لا يغيّر تركيب الدم**.", "**يحافظ على حجم الخلايا وشكلها الطبيعيين.**", "**لا يتداخل مع نتائج الفحوص**."]),
 F("edta-blood-film.jpg", "Normal red cells in a blood film (normal size and shape, central pallor)", "كريات حمر طبيعية في مسحة دموية (حجم وشكل طبيعيان، وشحوب مركزي)", h="56mm"),

 SEC("Main Types of Anticoagulants", "الأنواع الرئيسة لمانعات التخثّر"),
 T(["Anticoagulant", "Tube colour", "Main use", "الترجمة"],
   [["EDTA", "Purple / Lavender", "CBC • Blood film", "`EDTA` — بنفسجي — صورة الدم الكاملة، المسحة الدموية"],
    ["Heparin", "Green", "Plasma chemistry • Blood gas", "الهيبارين — أخضر — كيمياء البلازما، غازات الدم"],
    ["Sodium Citrate", "Light Blue", "PT • aPTT", "سترات الصوديوم — أزرق فاتح — `PT` و`aPTT`"],
    ["Fluoride + Oxalate", "Gray", "Glucose testing", "الفلورايد + الأوكزالات — رمادي — فحص الكلوكوز"]],
   ar_cols=[3], key_cols=[0]),

 H2("EDTA — Ethylenediaminetetraacetic Acid", "`EDTA` — إيثيلين ثنائي الأمين رباعي حمض الخليك"),
 SIDE([L(["**Mechanism:** binds **calcium ions** and prevents coagulation.", "**Main uses:** CBC, blood film, hemoglobin measurement, cell counting.",
          "**Tube color:** Purple / Lavender.", "**Preferred in hematology** because it **preserves cell morphology** relatively well."],
         ["**الآلية:** يرتبط **بأيونات الكالسيوم** فيمنع التخثّر.", "**الاستخدامات الرئيسة:** صورة الدم الكاملة، المسحة الدموية، قياس الهيموغلوبين، عدّ الخلايا.",
          "**لون الأنبوب:** بنفسجي / ليلكي.", "**مفضّل في أمراض الدم** لأنه **يحافظ على شكل الخلايا** جيدًا نسبيًا."])],
      "edta-tubes.jpg", "EDTA tubes (purple)", "أنابيب `EDTA` (بنفسجية)"),
 FLOW([("EDTA + Ca²⁺", "`EDTA` + كالسيوم"), ("EDTA–Ca complex", "معقّد `EDTA`–كالسيوم"), ("No coagulation", "لا تخثّر")]),

 H2("Heparin", "الهيبارين"),
 SIDE([L(["**Mechanism:** enhances the activity of **Antithrombin III**.", "This inhibits coagulation factors and reduces fibrin clot formation.",
          "**Main uses:** plasma chemistry and blood gas analysis.", "**Forms:** lithium, sodium, and ammonium heparin.", "**Tube color:** Green."],
         ["**الآلية:** يعزّز فعالية **مضاد الثرومبين الثالث**.", "وهذا يثبّط عوامل التخثّر ويقلّل تكوّن خثرة الفايبرين.",
          "**الاستخدامات الرئيسة:** كيمياء البلازما وتحليل غازات الدم.", "**الأشكال:** هيبارين الليثيوم، والصوديوم، والأمونيوم.", "**لون الأنبوب:** أخضر."])],
      "heparin-tubes.jpg", "Heparin tubes (green)", "أنابيب الهيبارين (خضراء)"),
 FLOW([("Heparin", "الهيبارين"), ("Antithrombin III", "مضاد الثرومبين الثالث"), ("↓ Thrombin", "↓ الثرومبين"), ("↓ Fibrin", "↓ الفايبرين")]),

 H2("Sodium Citrate", "سترات الصوديوم"),
 SIDE([L(["**Mechanism:** binds **calcium ions** and prevents coagulation.", "**Main uses:** **PT, aPTT**, and other coagulation tests.", "**Tube color:** Light Blue.",
          "**Blood : Citrate = 9 : 1**", "**Correct filling is essential** for reliable coagulation results."],
         ["**الآلية:** ترتبط **بأيونات الكالسيوم** فتمنع التخثّر.", "**الاستخدامات الرئيسة:** `PT` و`aPTT` وفحوص التخثّر الأخرى.", "**لون الأنبوب:** أزرق فاتح.",
          "**الدم : السترات = 9 : 1**", "**الملء الصحيح ضروري** لنتائج تخثّر موثوقة."])],
      "citrate-fill-line.jpg", "3.2% sodium citrate tube with fill line", "أنبوب سترات الصوديوم 3.2% مع خط الملء"),
 T(["Citrate tube", "Mixing ratio (citrate : blood)", "الترجمة"],
   [["3.2 %", "1 : 9", "أنبوب 3.2%: جزء سترات لكل 9 أجزاء دم"], ["3.8 %", "1 : 4", "أنبوب 3.8%: جزء سترات لكل 4 أجزاء دم"]],
   ar_cols=[2], key_cols=[0], style="summary", label_en="Mixing ratio", label_ar="نسبة الخلط"),

 H2("Potassium Oxalate + Sodium Fluoride", "أوكزالات البوتاسيوم + فلورايد الصوديوم"),
 T(["", "Role", "الدور"],
   [["Potassium Oxalate", "Anticoagulant — removes / precipitates calcium", "**أوكزالات البوتاسيوم**: مانع تخثّر — يزيل / يرسّب الكالسيوم"],
    ["Sodium Fluoride", "Antiglycolytic agent — helps preserve glucose concentration", "**فلورايد الصوديوم**: مانع للتحلّل السكري — يساعد في المحافظة على تركيز الكلوكوز"]],
   ar_cols=[2], key_cols=[0]),
 C("**Main use:** Blood glucose testing", "**الاستخدام الرئيس:** فحص كلوكوز الدم"),
 FF(("grey-tube.jpg", "Grey-top (fluoride/oxalate) tube", "أنبوب ذو غطاء رمادي (فلورايد/أوكزالات)", "40mm"),
    ("fluoride-glycolysis.jpg", "Sodium fluoride inhibits enolase and glycolysis", "فلورايد الصوديوم يثبّط إنزيم الإينوليز والتحلّل السكري", "40mm")),

 SEC("Anticoagulant Tubes and Their Uses", "أنابيب مانعات التخثّر واستخداماتها"),
 T(["Tube Color", "Additive", "Main Use", "الترجمة"],
   [["Purple / Lavender", "EDTA", "CBC, Blood Film", "بنفسجي — `EDTA` — صورة الدم، المسحة"], ["Light Blue", "Sodium Citrate", "PT, aPTT", "أزرق فاتح — سترات الصوديوم — `PT`، `aPTT`"],
    ["Green", "Heparin", "Plasma Chemistry, Blood Gas", "أخضر — الهيبارين — كيمياء البلازما، غازات الدم"], ["Gray", "Fluoride + Oxalate", "Glucose", "رمادي — فلورايد + أوكزالات — الكلوكوز"]],
   ar_cols=[3], key_cols=[0], style="summary", label_en="Tubes summary", label_ar="خلاصة الأنابيب"),
 F("tube-summary.jpg", "EDTA, sodium citrate, heparin and oxalate fluoride tubes", "أنابيب `EDTA` وسترات الصوديوم والهيبارين وأوكزالات الفلورايد", h="62mm"),

 SEC("Whole Blood Clotting Test (WBCT)", "اختبار تخثّر الدم الكامل"),
 R("Collection of **2 mL of venous blood** that is transferred directly into a **clean and dry glass tube**. It must be maintained upright, open, undisturbed for **20 and/or 30 minutes** at room temperature.",
   "يُجمع **2 مل من الدم الوريدي** ويُنقل مباشرة إلى **أنبوب زجاجي نظيف وجاف**، ويُترك قائمًا مفتوحًا دون تحريك مدة **20 و/أو 30 دقيقة** بدرجة حرارة الغرفة."),
 R("After exactly **20 minutes**, the tube must be **inverted**. If a **solid clot is retained**, the test indicates **normal coagulation**.",
   "بعد **20 دقيقة** بالضبط **يُقلب** الأنبوب. فإذا **بقيت خثرة صلبة**، دلّ الاختبار على **تخثّر طبيعي**."),
 R("If the **clot breaks down quickly** upon inversion of the tube or if there is **no clot**, the test indicates a **coagulopathy**. A friable clot is pictured below.",
   "وإذا **تفكّكت الخثرة بسرعة** عند قلب الأنبوب أو **لم تتكوّن خثرة**، دلّ الاختبار على **اعتلال التخثّر**. والصورة أدناه لخثرة هشّة."),
 F("wbct.jpg", "WBCT — Normal: solid clot retained at 20 or 30 minutes (Grade 0). Abnormal: friable clot (Grade 1) or no clot (Grade 2)",
   "اختبار `WBCT` — الطبيعي: بقاء خثرة صلبة عند 20 أو 30 دقيقة (الدرجة 0). غير الطبيعي: خثرة هشّة (الدرجة 1) أو لا خثرة (الدرجة 2)", h="60mm"),

 SEC("Proper Sample Handling", "التعامل السليم مع العيّنة"),
 SIDE([L(["Fill the tube to the **correct level**.", "**Gently invert** the tube several times.", "**Do not shake vigorously.**", "Check the sample for **clots**.", "**Label** the sample correctly."],
         ["املأ الأنبوب إلى **المستوى الصحيح**.", "**اقلب** الأنبوب **بلطف** عدة مرات.", "**لا ترجّه بقوة.**", "افحص العيّنة بحثًا عن **خثرات**.", "**ضع الملصق** على العيّنة بشكل صحيح."])],
      "inversion.jpg", "Gentle inversion of the tube", "قلب الأنبوب بلطف"),
 N("Incorrect handling → **unreliable laboratory results**", "التعامل الخاطئ ← **نتائج مختبرية غير موثوقة**", label=["Remember", "تذكّر"]),

 SEC("Common Errors", "الأخطاء الشائعة"),
 T(["Error", "Result", "الخطأ ← النتيجة"],
   [["Underfilled citrate tube", "Incorrect coagulation results", "أنبوب سترات ناقص الملء ← نتائج تخثّر غير صحيحة"],
    ["Clotted EDTA sample", "Unreliable CBC results", "عيّنة `EDTA` متخثّرة ← نتائج صورة دم غير موثوقة"],
    ["Vigorous shaking", "May cause hemolysis", "الرجّ العنيف ← قد يسبّب تحلّل الدم"],
    ["Wrong anticoagulant", "May interfere with test results", "مانع تخثّر خاطئ ← قد يتداخل مع نتائج الفحص"]],
   ar_cols=[2], key_cols=[0]),
 FF(("clotted-edta.jpg", "Clotted EDTA sample", "عيّنة `EDTA` متخثّرة", "50mm"), ("underfilling.jpg", "Underfilling vs overfilling", "نقص الملء مقابل زيادته", "50mm")),
]

mcq = [
 {"topic_en": "Anticoagulants", "topic_ar": "مانعات التخثّر"},
 Q("Anticoagulants are substances that:", "مانعات التخثّر مواد:", [("Cause clotting", "تسبّب التخثّر"), ("Prevent or reduce blood clotting", "تمنع تخثّر الدم أو تقلّله"), ("Destroy red cells", "تحطّم الكريات الحمر"), ("Increase platelets", "تزيد الصفيحات")], "b"),
 Q("A good anticoagulant should:", "يجب أن يكون مانع التخثّر الجيد:", [("Cause haemolysis", "مسبّبًا لتحلّل الدم"), ("Alter blood composition", "مغيّرًا لتركيب الدم"), ("Preserve normal cell size and shape", "محافظًا على حجم الخلايا وشكلها"), ("Interfere with results", "متداخلًا مع النتائج")], "c"),
 Q("Which is a natural anticoagulant in the body?", "أي مما يأتي مانع تخثّر طبيعي في الجسم؟", [("Warfarin", "الوارفارين"), ("EDTA", "EDTA"), ("Sodium citrate", "سترات الصوديوم"), ("Antithrombin III", "مضاد الثرومبين الثالث")], "d"),
 Q("Warfarin acts as a:", "يعمل الوارفارين بوصفه:", [("Vitamin K antagonist", "مضادًا لفيتامين K"), ("Calcium chelator", "رابطًا للكالسيوم"), ("Antiglycolytic agent", "مانعًا للتحلّل السكري"), ("Antithrombin enhancer", "معزّزًا لمضاد الثرومبين")], "a"),
 {"topic_en": "EDTA and heparin", "topic_ar": "EDTA والهيبارين"},
 Q("EDTA prevents coagulation by:", "يمنع EDTA التخثّر عن طريق:", [("Enhancing antithrombin III", "تعزيز مضاد الثرومبين"), ("Binding calcium ions", "الارتباط بأيونات الكالسيوم"), ("Inhibiting glycolysis", "تثبيط التحلّل السكري"), ("Lysing platelets", "تحليل الصفيحات")], "b"),
 Q("The tube colour of EDTA is:", "لون أنبوب EDTA:", [("Green", "أخضر"), ("Light blue", "أزرق فاتح"), ("Purple / lavender", "بنفسجي / ليلكي"), ("Grey", "رمادي")], "c"),
 Q("EDTA is preferred in haematology because it:", "يُفضّل EDTA في أمراض الدم لأنه:", [("Preserves cell morphology relatively well", "يحافظ على شكل الخلايا جيدًا نسبيًا"), ("Preserves glucose", "يحافظ على الكلوكوز"), ("Activates clotting", "ينشّط التخثّر"), ("Is cheapest", "أرخص")], "a"),
 Q("Heparin works by enhancing the activity of:", "يعمل الهيبارين بتعزيز فعالية:", [("Vitamin K", "فيتامين K"), ("Thrombin", "الثرومبين"), ("Calcium", "الكالسيوم"), ("Antithrombin III", "مضاد الثرومبين الثالث")], "d"),
 Q("The green-top tube contains:", "يحتوي الأنبوب ذو الغطاء الأخضر على:", [("EDTA", "EDTA"), ("Heparin", "الهيبارين"), ("Sodium citrate", "سترات الصوديوم"), ("Fluoride", "الفلورايد")], "b"),
 Q("Heparin tubes are mainly used for:", "تُستخدم أنابيب الهيبارين أساسًا لـ:", [("Plasma chemistry and blood gas", "كيمياء البلازما وغازات الدم"), ("CBC", "صورة الدم"), ("PT and aPTT", "PT وaPTT"), ("Glucose", "الكلوكوز")], "a"),
 Q("Which is NOT a form of heparin listed?", "أي مما يأتي ليس من أشكال الهيبارين المذكورة؟", [("Lithium heparin", "هيبارين الليثيوم"), ("Sodium heparin", "هيبارين الصوديوم"), ("Ammonium heparin", "هيبارين الأمونيوم"), ("Potassium heparin", "هيبارين البوتاسيوم")], "d"),
 {"topic_en": "Citrate and fluoride/oxalate", "topic_ar": "السترات والفلورايد/الأوكزالات"},
 Q("The tube used for PT and aPTT is:", "الأنبوب المستخدم لـ PT وaPTT:", [("Purple", "البنفسجي"), ("Green", "الأخضر"), ("Light blue (sodium citrate)", "الأزرق الفاتح (سترات الصوديوم)"), ("Grey", "الرمادي")], "c"),
 Q("The blood-to-citrate ratio in a 3.2% citrate tube is:", "نسبة الدم إلى السترات في أنبوب 3.2%:", [("1 : 1", "1 : 1"), ("4 : 1", "4 : 1"), ("9 : 1", "9 : 1"), ("1 : 9", "1 : 9")], "c"),
 Q("For a 3.8% citrate tube, the mixing ratio is 1 part citrate to:", "في أنبوب سترات 3.8% نسبة الخلط جزء سترات إلى:", [("4 parts blood", "4 أجزاء دم"), ("9 parts blood", "9 أجزاء دم"), ("2 parts blood", "جزأين دم"), ("10 parts blood", "10 أجزاء دم")], "a"),
 Q("Sodium fluoride in the grey tube acts as:", "يعمل فلورايد الصوديوم في الأنبوب الرمادي بوصفه:", [("Anticoagulant only", "مانع تخثّر فقط"), ("Antiglycolytic agent", "مانعًا للتحلّل السكري"), ("Clot activator", "منشّطًا للتخثّر"), ("Antithrombin enhancer", "معزّزًا لمضاد الثرومبين")], "b"),
 Q("The anticoagulant in the grey tube that precipitates calcium is:", "مانع التخثّر في الأنبوب الرمادي الذي يرسّب الكالسيوم:", [("Sodium fluoride", "فلورايد الصوديوم"), ("Heparin", "الهيبارين"), ("EDTA", "EDTA"), ("Potassium oxalate", "أوكزالات البوتاسيوم")], "d"),
 Q("The anticoagulant used for glucose testing is:", "مانع التخثّر المستخدم لفحص الكلوكوز:", [("Fluoride + oxalate", "فلورايد + أوكزالات"), ("EDTA", "EDTA"), ("Citrate", "السترات"), ("Heparin", "الهيبارين")], "a"),
 {"topic_en": "Handling, errors and WBCT", "topic_ar": "التعامل والأخطاء واختبار WBCT"},
 Q("Blood tubes should be:", "يجب التعامل مع أنابيب الدم بـ:", [("Shaken vigorously", "الرجّ بقوة"), ("Left unmixed", "تركها دون خلط"), ("Gently inverted several times", "قلبها بلطف عدة مرات"), ("Frozen immediately", "تجميدها فورًا")], "c"),
 Q("An underfilled citrate tube gives:", "أنبوب السترات ناقص الملء يعطي:", [("Incorrect coagulation results", "نتائج تخثّر غير صحيحة"), ("Hemolysis only", "تحلّل الدم فقط"), ("High glucose", "كلوكوز مرتفع"), ("No effect", "لا تأثير")], "a"),
 Q("A clotted EDTA sample gives:", "عيّنة EDTA المتخثّرة تعطي:", [("Reliable CBC", "صورة دم موثوقة"), ("Unreliable CBC results", "نتائج صورة دم غير موثوقة"), ("Better morphology", "شكلًا أفضل"), ("Higher glucose", "كلوكوزًا أعلى")], "b"),
 Q("In WBCT, the tube is inverted after exactly:", "في اختبار WBCT يُقلب الأنبوب بعد:", [("5 minutes", "5 دقائق"), ("10 minutes", "10 دقائق"), ("20 minutes", "20 دقيقة"), ("60 minutes", "60 دقيقة")], "c"),
 Q("In WBCT, no clot or a rapidly breaking clot indicates:", "في اختبار WBCT عدم تكوّن خثرة أو تفكّكها سريعًا يدل على:", [("Normal coagulation", "تخثّر طبيعي"), ("Polycythaemia", "كثرة الكريات الحمر"), ("Anaemia", "فقر الدم"), ("Coagulopathy", "اعتلال التخثّر")], "d"),
 {"topic_en": "Picture questions", "topic_ar": "أسئلة الصور"},
 Q("In this figure, the tube on the left (separated plasma over cells) contains:", "في هذا الشكل، الأنبوب الأيسر (بلازما منفصلة فوق الخلايا) يحتوي على:", [("Anticoagulated blood", "دم مع مانع تخثّر"), ("Clotted blood", "دم متخثّر"), ("Serum only", "مصل فقط"), ("Water", "ماء")], "a", img="assets/clotted-vs-anticoagulated.jpg", img_h="46mm"),
 Q("The tube shown (green top) is used for:", "الأنبوب في الشكل (غطاء أخضر) يُستخدم لـ:", [("CBC", "صورة الدم"), ("PT", "PT"), ("Plasma chemistry and blood gas", "كيمياء البلازما وغازات الدم"), ("Glucose", "الكلوكوز")], "c", img="assets/heparin-tubes.jpg", img_h="36mm"),
 Q("The line marked “FILL LINE” on this light-blue tube shows that:", "يبيّن «خط الملء» على هذا الأنبوب الأزرق الفاتح أن:", [("Filling is not important", "الملء غير مهم"), ("The tube must be filled correctly (9:1)", "يجب ملء الأنبوب بشكل صحيح (9:1)"), ("Only serum is collected", "يُجمع المصل فقط"), ("Glucose is preserved", "يُحفظ الكلوكوز")], "b", img="assets/citrate-fill-line.jpg", img_h="42mm"),
 Q("In this figure (WBCT), the middle tube with a solid clot after inversion means:", "في هذا الشكل (WBCT)، الأنبوب الأوسط مع خثرة صلبة بعد القلب يعني:", [("Coagulopathy (Grade 2)", "اعتلال تخثّر (الدرجة 2)"), ("Friable clot (Grade 1)", "خثرة هشّة (الدرجة 1)"), ("Haemolysis", "تحلّل الدم"), ("Normal coagulation (Grade 0)", "تخثّر طبيعي (الدرجة 0)")], "d", img="assets/wbct.jpg", img_h="34mm"),
]
tf = [
 TF("Anticoagulants allow plasma to be obtained.", "تتيح مانعات التخثّر الحصول على البلازما.", "T"),
 TF("A good anticoagulant may cause haemolysis.", "قد يسبّب مانع التخثّر الجيد تحلّل الدم.", "F"),
 TF("EDTA and sodium citrate both bind calcium ions.", "يرتبط كلٌّ من EDTA وسترات الصوديوم بأيونات الكالسيوم.", "T"),
 TF("Heparin binds calcium ions.", "يرتبط الهيبارين بأيونات الكالسيوم.", "F"),
 TF("EDTA is used for haemoglobin measurement and cell counting.", "يُستخدم EDTA لقياس الهيموغلوبين وعدّ الخلايا.", "T"),
 TF("The light-blue tube is used for CBC.", "يُستخدم الأنبوب الأزرق الفاتح لصورة الدم.", "F"),
 TF("Correct filling of citrate tubes is essential.", "الملء الصحيح لأنابيب السترات ضروري.", "T"),
 TF("Sodium fluoride preserves glucose concentration.", "يحافظ فلورايد الصوديوم على تركيز الكلوكوز.", "T"),
 TF("Vigorous shaking may cause haemolysis.", "قد يسبّب الرجّ العنيف تحلّل الدم.", "T"),
 TF("Using the wrong anticoagulant does not affect results.", "لا يؤثّر استخدام مانع تخثّر خاطئ في النتائج.", "F"),
 TF("WBCT uses a clean, dry glass tube.", "يستخدم اختبار WBCT أنبوبًا زجاجيًا نظيفًا وجافًا.", "T"),
 TF("Enoxaparin is a low molecular weight heparin.", "الإينوكسابارين هيبارين منخفض الوزن الجزيئي.", "T"),
]
traps = [
 TR("Which anticoagulants bind calcium?", "أي مانعات التخثّر ترتبط بالكالسيوم؟", "EDTA and sodium citrate bind calcium (oxalate precipitates it); heparin does NOT — it enhances antithrombin III.", "EDTA وسترات الصوديوم يرتبطان بالكالسيوم (والأوكزالات ترسّبه)؛ أما الهيبارين فلا — بل يعزّز مضاد الثرومبين الثالث."),
 TR("Citrate ratio — which tube?", "نسبة السترات — أي أنبوب؟", "3.2% tube: 1 citrate : 9 blood. 3.8% tube: 1 citrate : 4 blood.", "أنبوب 3.2%: 1 سترات : 9 دم. أنبوب 3.8%: 1 سترات : 4 دم."),
 TR("Grey tube — two additives, two jobs", "الأنبوب الرمادي — مادتان ووظيفتان", "Potassium oxalate = anticoagulant; sodium fluoride = antiglycolytic (preserves glucose).", "أوكزالات البوتاسيوم = مانع تخثّر؛ فلورايد الصوديوم = مانع للتحلّل السكري (يحفظ الكلوكوز)."),
 TR("Tube colours", "ألوان الأنابيب", "Purple EDTA (CBC); light blue citrate (PT, aPTT); green heparin (chemistry, blood gas); grey fluoride/oxalate (glucose).", "البنفسجي EDTA (صورة الدم)؛ الأزرق الفاتح سترات (PT، aPTT)؛ الأخضر هيبارين (كيمياء، غازات)؛ الرمادي فلورايد/أوكزالات (كلوكوز)."),
 TR("Shake or invert?", "رجّ أم قلب؟", "Gently invert several times; vigorous shaking may cause haemolysis.", "يُقلب بلطف عدة مرات؛ والرجّ العنيف قد يسبّب تحلّل الدم."),
 TR("WBCT grades", "درجات اختبار WBCT", "Grade 0: solid clot (normal). Grade 1: friable clot. Grade 2: no clot.", "الدرجة 0: خثرة صلبة (طبيعي). الدرجة 1: خثرة هشّة. الدرجة 2: لا خثرة."),
]
important = [  # the lecturer's quiz (slide 14) with model answers
 IM("What is an anticoagulant?", "ما مانع التخثّر؟", "A substance that prevents or reduces blood clotting, preserving blood cells and allowing plasma to be obtained (e.g. EDTA, heparin, sodium citrate).", "مادة تمنع تخثّر الدم أو تقلّله، فتحافظ على خلايا الدم وتتيح الحصول على البلازما (مثل EDTA والهيبارين وسترات الصوديوم)."),
 IM("Why is EDTA used for CBC?", "لماذا يُستخدم EDTA لصورة الدم؟", "It binds calcium to prevent clotting and preserves cell morphology relatively well.", "لأنه يرتبط بالكالسيوم فيمنع التخثّر، ويحافظ على شكل الخلايا جيدًا نسبيًا."),
 IM("Which tube is used for PT and aPTT?", "أي أنبوب يُستخدم لـ PT وaPTT؟", "The light-blue sodium citrate tube.", "أنبوب سترات الصوديوم الأزرق الفاتح."),
 IM("What is the blood-to-citrate ratio?", "ما نسبة الدم إلى السترات؟", "Blood : citrate = 9 : 1 (3.2% tube); 1 citrate : 4 blood for the 3.8% tube.", "الدم : السترات = 9 : 1 (أنبوب 3.2%)؛ و1 سترات : 4 دم في أنبوب 3.8%."),
 IM("Which anticoagulant is used for glucose testing?", "أي مانع تخثّر يُستخدم لفحص الكلوكوز؟", "Fluoride + oxalate (grey tube): oxalate anticoagulates, fluoride stops glycolysis.", "الفلورايد + الأوكزالات (الأنبوب الرمادي): الأوكزالات تمنع التخثّر والفلورايد يوقف التحلّل السكري."),
 IM("What is the mechanism of action of heparin?", "ما آلية عمل الهيبارين؟", "It enhances antithrombin III, which inhibits coagulation factors (↓ thrombin → ↓ fibrin).", "يعزّز مضاد الثرومبين الثالث الذي يثبّط عوامل التخثّر (↓ الثرومبين ← ↓ الفايبرين)."),
 IM("Why should blood tubes be gently inverted?", "لماذا تُقلب أنابيب الدم بلطف؟", "To mix blood with the anticoagulant without causing haemolysis (vigorous shaking may cause haemolysis).", "لخلط الدم مع مانع التخثّر دون إحداث تحلّل الدم (فالرجّ العنيف قد يسبّبه)."),
 IM("What may happen if an EDTA sample contains a clot?", "ماذا قد يحدث إذا احتوت عيّنة EDTA على خثرة؟", "Unreliable CBC results.", "نتائج صورة دم غير موثوقة."),
]
meta = dict(HEM, unit_en="Lab 1", unit_ar="العملي 1", unit_no="1", title_en="Anticoagulants", title_ar="مانعات التخثّر")
save("hematology-practical-anticoagulants", meta, blocks, mcq, tf, traps, important)

```
