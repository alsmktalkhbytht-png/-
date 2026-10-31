---
source: BIOS-Obsidian/tools/scripts/bt/make3.py
handouts: [bloodbank-lec3-services]
saved: 2026-10-31
tags: [bios, code]
---
# bt/make3.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#bloodbank-lec3-services|bloodbank-lec3-services]]

```python
import json, os
def C(en, ar, **k): return dict(t="card", en=en, ar=ar, **k)
def R(en, ar): return dict(t="rule", en=en, ar=ar)
def SEC(en, ar): return dict(t="section", en=en, ar=ar)
def H2(en, ar): return dict(t="h2", en=en, ar=ar)

blocks = [
 SEC("Blood bank services", "خدمات بنك الدم"),
 C("**Includes:**", "**تشمل:**",
   list_en=["Blood grouping and typing", "Blood cross matching", "Coombs test", "Tests for uncommon blood cell antigens and antibodies", "Antibody titer",
            "Screening tests for: Hepatitis B and Hepatitis C, HIV, Venereal diseases, Malaria, Microfilaria.", "Blood bank services collect, [[cut]]"],
   list_ar=["تحديد فصيلة الدم ونوعه", "اختبار التوافق (المطابقة) الدموي", "اختبار كومبس (`Coombs test`)", "فحوص مستضدات وأضداد خلايا الدم غير الشائعة", "معايرة الأجسام المضادة (`Antibody titer`)",
            "فحوص التحرّي عن: التهاب الكبد B وC، وHIV، والأمراض الزهرية (التناسلية)، والملاريا، والفيلاريا الدقيقة.", "تجمع خدمات بنك الدم… [[قطع]]"]),
 C("**Unnecessary transfusions** specially **unsafe transfusion** practices, expose patients to the risk of serious adverse **transfusion reactions** and **transfusion-transmissible infections**.",
   "إن **عمليات النقل غير الضرورية**، ولا سيما ممارسات **النقل غير الآمن**، تعرّض المرضى لخطر **تفاعلات نقل الدم** الضارة الخطيرة و**العدوى المنتقلة بنقل الدم**."),
 C("**Unnecessary transfusions** also **reduce** the **availability** of blood products for patients who are in need.",
   "كما أن **عمليات النقل غير الضرورية** **تقلّل توافر** منتجات الدم للمرضى المحتاجين إليها."),
 C(["The fundamental **purpose** of a blood bank is to ensure a **safe** and **adequate supply** of blood for various medical interventions.",
    "This includes transfusions for patients undergoing surgeries, individuals with medical conditions such as anemia or leukemia, and those who [[cut]]"],
   ["**الغاية** الأساسية لبنك الدم هي ضمان **إمداد آمن وكافٍ** من الدم لمختلف التدخلات الطبية.",
    "ويشمل ذلك نقل الدم للمرضى الذين يخضعون للعمليات الجراحية، والمصابين بحالات طبية مثل فقر الدم أو ابيضاض الدم (اللوكيميا)، ومن… [[قطع]]"]),

 SEC("Blood banks have four major function areas", "لبنوك الدم أربع مناطق وظيفية رئيسة"),
 R("**receiving room** ; consisting of entrance, reception, registration, waiting, medical examination, bleeding, refreshment/recovery/rest room, and apheresis room.",
   "**غرفة الاستقبال**؛ وتتكوّن من المدخل، والاستقبال، والتسجيل، والانتظار، والفحص الطبي، وسحب الدم، وغرفة المرطّبات/التعافي/الاستراحة، وغرفة الفصادة."),
 R("**Testing room** ; consisting of serology lab and transferable disease lab.", "**غرفة الفحص**؛ وتتكوّن من مختبر المصليات ومختبر الأمراض المنتقلة."),
 R("**Storage area** with blood component room.", "**منطقة الخزن** مع غرفة مكوّنات الدم."),
 R("**Distribution area.**", "**منطقة التوزيع.**"),

 SEC("Blood and blood product storage", "خزن الدم ومنتجاته"),
 C(["Normally blood products is stored in one of two ways: either in **refrigerator** or **freezer cabinets**.", "Choosing one of these two methods depend in type of blood products which stored."],
   ["تُخزَّن منتجات الدم عادةً بإحدى طريقتين: إما في **الثلاجات** أو في **خزانات التجميد (المجمّدات)**.", "ويعتمد اختيار إحدى هاتين الطريقتين على نوع منتج الدم المخزَّن."]),

 SEC("The blood bank and phlebotomy", "بنك الدم وسحب الدم"),
 C("**What is the purpose of a blood bank, and how does it relate to phlebotomy?**", "**ما غاية بنك الدم، وما علاقته بسحب الدم (`Phlebotomy`)؟**"),
 C("The blood bank playing important role in the **collection, processing, storage, and distribution** of blood and blood products for medical treatments and emergencies.",
   "يؤدي بنك الدم دورًا مهمًا في **جمع** الدم ومنتجاته و**معالجتها وخزنها وتوزيعها** للعلاجات الطبية والطوارئ."),
 C("**Phlebotomy**, the practice of **drawing blood from patients**, is closely intertwined with the functions of a blood bank, as it serves as the primary source for the acquisition of donor blood.",
   "**سحب الدم** (`Phlebotomy`)، أي ممارسة **سحب الدم من المرضى**، مرتبط ارتباطًا وثيقًا بوظائف بنك الدم، لأنه المصدر الرئيس للحصول على دم المتبرعين."),

 SEC("Blood Bank Equipment", "أجهزة بنك الدم"),
 C("The Blood bank should identify the equipment that is critical to the provision of blood, blood components, and/or services with calibration, maintenance, and monitoring of equipment",
   "يجب أن يحدّد بنك الدم الأجهزة الحاسمة لتوفير الدم أو مكوّناته و/أو الخدمات، مع معايرة الأجهزة وصيانتها ومراقبتها"),
 C(["**Selection of Equipment** : a process to define the selection criteria for equipment according to qualification of Equipment for its intended use.",
    "Equipment repairs and upgrades shall be evaluated based on the facility’s policies and manufacturer recommendations."],
   ["**اختيار الأجهزة:** عملية لتحديد معايير اختيار الأجهزة وفق تأهيل الجهاز للاستعمال المقصود منه.",
    "وتُقيَّم إصلاحات الأجهزة وتحديثاتها بناءً على سياسات المنشأة وتوصيات الشركة المصنّعة."]),

 SEC("Quality Control", "ضبط الجودة"),
 C("A program of **quality control** shall be established that is sufficiently comprehensive to ensure that reagents, equipment, and methods perform as expected.",
   "يجب وضع برنامج **لضبط الجودة** شامل بما يكفي لضمان أن الكواشف والأجهزة والطرق تعمل كما هو متوقَّع."),
 C("**Use of Materials** : All materials (including containers and solutions used for collection, processing, preservation, and storage of blood and blood components, and all reagents used for tests) should be stored and used in accordance with the manufacturer’s written instructions and should meet specified requirements.",
   "**استعمال المواد:** يجب خزن جميع المواد (ومنها الأوعية والمحاليل المستعملة في جمع الدم ومكوّناته ومعالجتها وحفظها وخزنها، وجميع الكواشف المستعملة في الفحوص) واستعمالها وفق التعليمات المكتوبة للشركة المصنّعة، ويجب أن تستوفي المتطلبات المحدّدة."),

 SEC("Practical Blood Transfusion 3 — Standard Conditions For Blood Bags Storage.", "نقل الدم العملي 3 — الشروط القياسية لخزن أكياس الدم"),
 C("Blood component storage devices should be carefully selected and validated to ensure that they are capable of maintaining the FDA-regulated storage temperatures.",
   "يجب اختيار أجهزة خزن مكوّنات الدم بعناية والتحقق منها لضمان قدرتها على الحفاظ على درجات حرارة الخزن التي تنظّمها إدارة الغذاء والدواء (`FDA`)."),
 C("**Temperatures** must be continuously **monitored**, **recorded** at **least every 4 hours**", "يجب **مراقبة** درجات الحرارة باستمرار و**تسجيلها** **كل 4 ساعات على الأقل**"),
 C("The **device** should **alert** the user **if an unacceptable temperature** condition occurs.", "يجب أن **ينبّه الجهاز** المستعمل **إذا حدثت حالة حرارة غير مقبولة**."),
 C("The **room** in which platelets are **stored** is constantly monitored and maintained at **20° to 24°C** , sometimes need environmental device to [[cut]]",
   "تُراقَب **الغرفة** التي **تُخزَّن** فيها الصفائح الدموية باستمرار ويُحافَظ عليها عند **20° إلى 24 °م**، وأحيانًا تحتاج إلى جهاز بيئي لـ… [[قطع]]"),

 SEC("Storage Devices & storage conditions", "أجهزة الخزن وشروطه"),
 C("**Storage devices include**", "**تشمل أجهزة الخزن:**", list_en=["refrigerators", "freezers", "platelet agitators"], list_ar=["الثلاجات", "المجمّدات", "هزّازات (محرّكات) الصفائح الدموية"]),
 C("**Benefit of Cold temperature :**", "**فائدة درجة الحرارة الباردة:**", list_en=["Inhibits bacterial growth", "Slows glycolytic activity"], list_ar=["تثبّط نمو البكتيريا", "تبطّئ نشاط تحلّل الكلوكوز"]),
 H2("Whole blood, or RBC packed storage conditions :", "شروط خزن الدم الكامل أو الكريات الحمر المكدّسة:"),
 C("**whole blood** & **packed red cells** must be stored at **1° to 6°C**, and the shelf life is dependent on the anticoagulant/preservative substances used",
   "يجب خزن **الدم الكامل** و**الكريات الحمر المكدّسة** عند **1° إلى 6 °م**، ويعتمد العمر التخزيني على المواد المانعة للتخثّر/الحافظة المستعملة"),
 C(["Whole blood collected in acid-citrate-dextrose (**ACD**), citrate-phosphate dextrose (**CPD**) has a shelf life of **21 days**.",
    "Whole blood collected in citrate-phosphate-dextrose-adenine (**CPDA-1**) has a shelf life of **35 days**."],
   ["الدم الكامل المجموع في سترات الحامض والدكستروز (`ACD`) أو سترات الفوسفات والدكستروز (`CPD`) عمره التخزيني **21 يومًا**.",
    "أما الدم الكامل المجموع في سترات الفوسفات والدكستروز والأدينين (`CPDA-1`) فعمره التخزيني **35 يومًا**."]),
 C("If **additive solution** like saline-adenine-glucose-mannitol(**SAGM**) is added to RBCs, the shelf life can extended to **42 days**.",
   "إذا أُضيف **محلول مضاف** مثل المحلول الملحي-الأدينين-الكلوكوز-المانيتول (`SAGM`) إلى الكريات الحمر، يمكن أن يمتد العمر التخزيني إلى **42 يومًا**."),
 dict(t="table", style="summary", label_en="Summary", label_ar="خلاصة", head=["Anticoagulant / additive", "Shelf life", "المادة — العمر التخزيني"], ar_cols=[2], key_cols=[0],
      rows=[["ACD, CPD", "21 days", "`ACD` و`CPD` ← 21 يومًا"], ["CPDA-1", "35 days", "`CPDA-1` ← 35 يومًا"], ["SAGM (added to RBCs)", "42 days", "`SAGM` (يُضاف إلى الكريات الحمر) ← 42 يومًا"]]),

 SEC("Platelets storage", "خزن الصفائح الدموية"),
 C("**Platelets** are stored at **20° to 24°C** with **constant agitation**, and therefore they are the blood component that is **most likely** to **grow bacteria** if inadvertently contaminated.",
   "تُخزَّن **الصفائح الدموية** عند **20° إلى 24 °م** مع **تحريك مستمر**، ولذلك فهي مكوّن الدم **الأكثر عرضة** **لنمو البكتيريا** إذا تلوّثت عن غير قصد."),
 C("**Bacteria** may be introduced into a platelet product either by **ineffective skin cleaning** prior to phlebotomy **or** a **low-level donor bacteremia** that is not identified during health history review or physical examination of the donor",
   "قد تدخل **البكتيريا** إلى منتج الصفائح إما بسبب **تنظيف الجلد غير الفعّال** قبل سحب الدم، **أو** بسبب **تجرثم دم خفيف لدى المتبرع** لم يُكشف في أثناء مراجعة التاريخ الصحي أو الفحص البدني للمتبرع"),

 SEC("Plasma storage", "خزن البلازما"),
 C("**Frozen plasma** is stored at **–18°C** or colder for **1 year** or at **–65°C** or below for **7 years** with FDA approval.",
   "تُخزَّن **البلازما المجمّدة** عند **−18 °م** أو أبرد مدة **سنة**، أو عند **−65 °م** أو أقل مدة **7 سنوات** بموافقة `FDA`."),
 C(["Plasma from whole blood donations may also remain in a liquid state, stored at **1° to 6°C**, and be labeled as **liquid plasma (LP)**.",
    "LP expires **5** days after the whole blood shelf life from which it was collected.",
    "For example, CPD whole blood has a 21-day shelf life, therefore CPD LP has a shelf life of 26 days"],
   ["يمكن أيضًا أن تبقى البلازما المأخوذة من تبرعات الدم الكامل بحالة سائلة، مخزَّنة عند **1° إلى 6 °م**، وتُوسم **بالبلازما السائلة** (`LP`).",
    "تنتهي صلاحية البلازما السائلة بعد **5** أيام من انتهاء العمر التخزيني للدم الكامل الذي جُمعت منه.",
    "فمثلًا: الدم الكامل في CPD عمره 21 يومًا، لذا فإن عمر البلازما السائلة منه 26 يومًا"]),
 C(["Once **thawing** is complete for **frozen plasma** , the product may be stored at 1° to 6°C for up to **24** hours.",
    "If not transfused within the initial 24-hour period, the thawed plasma may be stored for up to **5** days, but the product label must be changed to “**thawed plasma**” *because it can not maintain therapeutic levels of the labile clotting Factor V and Factor VIII*."],
   ["بعد اكتمال **إذابة** **البلازما المجمّدة**، يمكن خزن المنتج عند 1° إلى 6 °م مدة تصل إلى **24** ساعة.",
    "وإذا لم يُنقل خلال الـ 24 ساعة الأولى، يمكن خزن البلازما المذابة مدة تصل إلى **5** أيام، لكن يجب تغيير ملصق المنتج إلى «**بلازما مذابة**» *لأنها لا تستطيع الحفاظ على المستويات العلاجية لعاملَي التخثّر غير المستقرَّين V وVIII*."]),
]

def M(en, ar, o, a): return {"en": en, "ar": ar, "options": o, "answer": a}
mcq = [
 M("Which of the following is NOT listed among blood bank services?", "أيٌّ مما يأتي ليس من خدمات بنك الدم المذكورة؟", [["Blood grouping and typing", "تحديد فصيلة الدم"], ["Coombs test", "اختبار كومبس"], ["Liver biopsy", "خزعة الكبد"], ["Antibody titer", "معايرة الأجسام المضادة"]], "c"),
 M("Blood bank screening tests include all EXCEPT:", "تشمل فحوص التحرّي في بنك الدم كل ما يأتي ما عدا:", [["Hepatitis B and C", "التهاب الكبد B وC"], ["HIV", "HIV"], ["Malaria", "الملاريا"], ["Diabetes", "السكري"]], "d"),
 M("Unnecessary transfusions:", "عمليات النقل غير الضرورية:", [["Expose patients to adverse reactions and reduce blood availability", "تعرّض المرضى لتفاعلات ضارة وتقلّل توافر الدم"], ["Have no risk", "لا خطر فيها"], ["Increase blood availability", "تزيد توافر الدم"], ["Are recommended before surgery", "يُوصى بها قبل الجراحة"]], "a"),
 M("The fundamental purpose of a blood bank is to:", "الغاية الأساسية لبنك الدم هي:", [["Sell blood", "بيع الدم"], ["Ensure a safe and adequate supply of blood", "ضمان إمداد آمن وكافٍ من الدم"], ["Perform surgeries", "إجراء العمليات"], ["Diagnose leukemia", "تشخيص اللوكيميا"]], "b"),
 M("How many major function areas does a blood bank have?", "كم منطقة وظيفية رئيسة لبنك الدم؟", [["Two", "اثنتان"], ["Three", "ثلاث"], ["Four", "أربع"], ["Six", "ست"]], "c"),
 M("The apheresis room belongs to the:", "تنتمي غرفة الفصادة إلى:", [["Receiving room", "غرفة الاستقبال"], ["Testing room", "غرفة الفحص"], ["Storage area", "منطقة الخزن"], ["Distribution area", "منطقة التوزيع"]], "a"),
 M("The serology lab and transferable disease lab are in the:", "يقع مختبر المصليات ومختبر الأمراض المنتقلة في:", [["Receiving room", "غرفة الاستقبال"], ["Distribution area", "منطقة التوزيع"], ["Storage area", "منطقة الخزن"], ["Testing room", "غرفة الفحص"]], "d"),
 M("Blood products are normally stored in:", "تُخزَّن منتجات الدم عادةً في:", [["Incubators or ovens", "حاضنات أو أفران"], ["Refrigerator or freezer cabinets", "ثلاجات أو خزانات تجميد"], ["Room shelves only", "رفوف الغرفة فقط"], ["Water baths", "حمّامات مائية"]], "b"),
 M("Phlebotomy is:", "سحب الدم (Phlebotomy) هو:", [["Blood grouping", "تحديد الفصيلة"], ["Storage of plasma", "خزن البلازما"], ["The practice of drawing blood from patients", "ممارسة سحب الدم من المرضى"], ["Cross matching", "المطابقة"]], "c"),
 M("Phlebotomy relates to the blood bank because it is:", "يرتبط سحب الدم ببنك الدم لأنه:", [["The primary source for acquiring donor blood", "المصدر الرئيس للحصول على دم المتبرعين"], ["A storage method", "طريقة خزن"], ["A quality control test", "فحص لضبط الجودة"], ["A type of equipment", "نوع من الأجهزة"]], "a"),
 M("Equipment repairs and upgrades are evaluated based on:", "تُقيَّم إصلاحات الأجهزة وتحديثاتها بناءً على:", [["The donor's opinion", "رأي المتبرع"], ["The cheapest option", "الخيار الأرخص"], ["The facility's policies and manufacturer recommendations", "سياسات المنشأة وتوصيات المصنّع"], ["The patient's request", "طلب المريض"]], "c"),
 M("A quality control program ensures that:", "يضمن برنامج ضبط الجودة أن:", [["Reagents, equipment, and methods perform as expected", "الكواشف والأجهزة والطرق تعمل كما هو متوقَّع"], ["Donors are paid", "المتبرعين يتقاضون أجرًا"], ["Blood is free", "الدم مجاني"], ["Storage is unlimited", "الخزن غير محدود"]], "a"),
 M("Storage temperatures must be recorded at least every:", "يجب تسجيل درجات حرارة الخزن مرة على الأقل كل:", [["24 hours", "24 ساعة"], ["4 hours", "4 ساعات"], ["Week", "أسبوع"], ["12 hours", "12 ساعة"]], "b"),
 M("Which of the following is NOT a storage device mentioned in the lecture?", "أيٌّ مما يأتي ليس من أجهزة الخزن المذكورة؟", [["Refrigerators", "الثلاجات"], ["Freezers", "المجمّدات"], ["Platelet agitators", "هزّازات الصفائح"], ["Centrifuges", "أجهزة الطرد المركزي"]], "d"),
 M("Cold temperature benefits stored blood by:", "تفيد درجة الحرارة الباردة الدم المخزَّن بـ:", [["Activating platelets", "تنشيط الصفائح"], ["Inhibiting bacterial growth and slowing glycolytic activity", "تثبيط نمو البكتيريا وإبطاء تحلّل الكلوكوز"], ["Increasing glycolysis", "زيادة تحلّل الكلوكوز"], ["Thawing plasma", "إذابة البلازما"]], "b"),
 M("Whole blood and packed red cells are stored at:", "يُخزَّن الدم الكامل والكريات الحمر المكدّسة عند:", [["20° to 24°C", "20° إلى 24 °م"], ["–18°C", "−18 °م"], ["1° to 6°C", "1° إلى 6 °م"], ["–65°C", "−65 °م"]], "c"),
 M("Whole blood in CPD has a shelf life of:", "العمر التخزيني للدم الكامل في CPD:", [["21 days", "21 يومًا"], ["35 days", "35 يومًا"], ["42 days", "42 يومًا"], ["5 days", "5 أيام"]], "a"),
 M("Whole blood in CPDA-1 has a shelf life of:", "العمر التخزيني للدم الكامل في CPDA-1:", [["21 days", "21 يومًا"], ["26 days", "26 يومًا"], ["42 days", "42 يومًا"], ["35 days", "35 يومًا"]], "d"),
 M("Adding SAGM to RBCs extends the shelf life to:", "إضافة SAGM إلى الكريات الحمر تمدّد العمر التخزيني إلى:", [["35 days", "35 يومًا"], ["42 days", "42 يومًا"], ["1 year", "سنة"], ["7 years", "7 سنوات"]], "b"),
 M("Platelets are stored at:", "تُخزَّن الصفائح الدموية عند:", [["20° to 24°C with constant agitation", "20° إلى 24 °م مع تحريك مستمر"], ["1° to 6°C without agitation", "1° إلى 6 °م بلا تحريك"], ["–18°C", "−18 °م"], ["–65°C", "−65 °م"]], "a"),
 M("The blood component most likely to grow bacteria if contaminated is:", "مكوّن الدم الأكثر عرضة لنمو البكتيريا إذا تلوّث:", [["Frozen plasma", "البلازما المجمّدة"], ["Packed red cells", "الكريات الحمر المكدّسة"], ["Platelets", "الصفائح الدموية"], ["Whole blood at 4 °C", "الدم الكامل عند 4 °م"]], "c"),
 M("Frozen plasma stored at –65°C or below lasts (with FDA approval):", "البلازما المجمّدة المخزَّنة عند −65 °م أو أقل تدوم (بموافقة FDA):", [["1 year", "سنة"], ["5 days", "5 أيام"], ["7 years", "7 سنوات"], ["24 hours", "24 ساعة"]], "c"),
 M("Liquid plasma (LP) from CPD whole blood has a shelf life of:", "العمر التخزيني للبلازما السائلة من دم CPD:", [["21 days", "21 يومًا"], ["26 days", "26 يومًا"], ["35 days", "35 يومًا"], ["5 days", "5 أيام"]], "b"),
 M("Thawed plasma not transfused within 24 hours can be stored up to 5 days but relabeled because it cannot maintain levels of:", "البلازما المذابة التي لم تُنقل خلال 24 ساعة يمكن خزنها حتى 5 أيام مع تغيير ملصقها لأنها لا تحافظ على مستويات:", [["Factors V and VIII", "العاملَين V وVIII"], ["Albumin", "الألبومين"], ["Glucose", "الكلوكوز"], ["Platelets", "الصفائح"]], "a"),
]
tf = [
 {"en": "Coombs test is one of the blood bank services.", "ar": "اختبار كومبس من خدمات بنك الدم.", "answer": "T"},
 {"en": "Unnecessary transfusions increase the availability of blood for patients in need.", "ar": "عمليات النقل غير الضرورية تزيد توافر الدم للمرضى المحتاجين.", "answer": "F"},
 {"en": "The distribution area is one of the four major function areas of a blood bank.", "ar": "منطقة التوزيع إحدى المناطق الوظيفية الأربع لبنك الدم.", "answer": "T"},
 {"en": "The choice between refrigerator and freezer depends on the type of blood product.", "ar": "يعتمد الاختيار بين الثلاجة والمجمّدة على نوع منتج الدم.", "answer": "T"},
 {"en": "Storage devices should alert the user when an unacceptable temperature occurs.", "ar": "يجب أن تنبّه أجهزة الخزن المستعمل عند حدوث حرارة غير مقبولة.", "answer": "T"},
 {"en": "Cold temperature speeds up glycolytic activity.", "ar": "الحرارة الباردة تسرّع نشاط تحلّل الكلوكوز.", "answer": "F"},
 {"en": "The shelf life of whole blood depends on the anticoagulant/preservative used.", "ar": "يعتمد العمر التخزيني للدم الكامل على مانع التخثّر/الحافظ المستعمل.", "answer": "T"},
 {"en": "Platelets are stored in the refrigerator at 1° to 6°C.", "ar": "تُخزَّن الصفائح في الثلاجة عند 1° إلى 6 °م.", "answer": "F"},
 {"en": "Ineffective skin cleaning before phlebotomy can contaminate platelets with bacteria.", "ar": "التنظيف غير الفعّال للجلد قبل سحب الدم قد يلوّث الصفائح بالبكتيريا.", "answer": "T"},
 {"en": "Frozen plasma at –18°C or colder can be stored for 1 year.", "ar": "البلازما المجمّدة عند −18 °م أو أبرد يمكن خزنها سنة.", "answer": "T"},
 {"en": "Liquid plasma expires 5 days before the whole blood it came from.", "ar": "تنتهي صلاحية البلازما السائلة قبل الدم الكامل الذي أُخذت منه بـ 5 أيام.", "answer": "F"},
 {"en": "Thawed frozen plasma may be stored at 1° to 6°C for up to 24 hours.", "ar": "يمكن خزن البلازما المجمّدة بعد إذابتها عند 1° إلى 6 °م حتى 24 ساعة.", "answer": "T"},
]
traps = [
 {"en": "Whole blood in CPD and CPDA-1 has the same shelf life. Correct?", "ar": "للدم الكامل في CPD وCPDA-1 العمر التخزيني نفسه. هل هذا صحيح؟", "answer_en": "No. ACD/CPD → **21 days**; CPDA-1 → **35 days**; with SAGM → **42 days**.", "answer_ar": "لا. ACD/CPD ← **21 يومًا**؛ CPDA-1 ← **35 يومًا**؛ مع SAGM ← **42 يومًا**."},
 {"en": "Platelets are the safest component against bacteria because they are kept cold. Correct?", "ar": "الصفائح أكثر المكوّنات أمانًا من البكتيريا لأنها تُحفظ باردة. هل هذا صحيح؟", "answer_en": "No. Platelets are kept at **20–24 °C** with agitation, so they are the component **most likely** to grow bacteria.", "answer_ar": "لا. تُحفظ الصفائح عند **20–24 °م** مع التحريك، لذا فهي المكوّن **الأكثر عرضة** لنمو البكتيريا."},
 {"en": "Frozen plasma at –18°C can be stored for 7 years. Correct?", "ar": "يمكن خزن البلازما المجمّدة عند −18 °م مدة 7 سنوات. هل هذا صحيح؟", "answer_en": "No. –18°C or colder → **1 year**; –65°C or below → **7 years** (with FDA approval).", "answer_ar": "لا. −18 °م أو أبرد ← **سنة**؛ −65 °م أو أقل ← **7 سنوات** (بموافقة FDA)."},
 {"en": "Liquid plasma from CPD whole blood lasts 21 days. Correct?", "ar": "البلازما السائلة من دم CPD تدوم 21 يومًا. هل هذا صحيح؟", "answer_en": "No. LP expires **5 days after** the whole blood shelf life: 21 + 5 = **26 days**.", "answer_ar": "لا. تنتهي البلازما السائلة **بعد 5 أيام** من عمر الدم الكامل: 21 + 5 = **26 يومًا**."},
 {"en": "Thawed plasma kept 5 days keeps the same label. Correct?", "ar": "البلازما المذابة المحفوظة 5 أيام تبقى بالملصق نفسه. هل هذا صحيح؟", "answer_en": "No. After 24 hours the label must change to **“thawed plasma”** — it cannot maintain Factor V and Factor VIII.", "answer_ar": "لا. بعد 24 ساعة يجب تغيير الملصق إلى **«بلازما مذابة»** — لأنها لا تحافظ على العاملين V وVIII."},
 {"en": "Temperatures in storage devices are recorded once a day. Correct?", "ar": "تُسجَّل درجات الحرارة في أجهزة الخزن مرة في اليوم. هل هذا صحيح؟", "answer_en": "No. They must be continuously monitored and recorded **at least every 4 hours**.", "answer_ar": "لا. يجب مراقبتها باستمرار وتسجيلها **كل 4 ساعات على الأقل**."},
]
important = [
 {"en": "List the blood bank services.", "ar": "عدّد خدمات بنك الدم.", "answer_en": "Blood grouping and typing; cross matching; Coombs test; tests for uncommon blood cell antigens and antibodies; antibody titer; screening for hepatitis B and C, HIV, venereal diseases, malaria, microfilaria.", "answer_ar": "تحديد الفصيلة؛ المطابقة؛ اختبار كومبس؛ فحوص المستضدات والأضداد غير الشائعة؛ معايرة الأجسام المضادة؛ التحرّي عن التهاب الكبد B وC وHIV والأمراض الزهرية والملاريا والفيلاريا الدقيقة."},
 {"en": "What are the four major function areas of a blood bank?", "ar": "ما المناطق الوظيفية الأربع لبنك الدم؟", "answer_en": "(1) Receiving room (entrance, reception, registration, waiting, medical examination, bleeding, refreshment/rest, apheresis); (2) testing room (serology and transferable disease labs); (3) storage area with blood component room; (4) distribution area.", "answer_ar": "(1) غرفة الاستقبال (المدخل، الاستقبال، التسجيل، الانتظار، الفحص الطبي، السحب، الاستراحة، الفصادة)؛ (2) غرفة الفحص (مختبر المصليات والأمراض المنتقلة)؛ (3) منطقة الخزن مع غرفة المكوّنات؛ (4) منطقة التوزيع."},
 {"en": "What is the purpose of a blood bank, and how does it relate to phlebotomy?", "ar": "ما غاية بنك الدم وما علاقته بسحب الدم؟", "answer_en": "It collects, processes, stores and distributes blood and blood products for treatments and emergencies. Phlebotomy (drawing blood) is the primary source for acquiring donor blood.", "answer_ar": "يجمع الدم ومنتجاته ويعالجها ويخزّنها ويوزّعها للعلاجات والطوارئ. وسحب الدم هو المصدر الرئيس للحصول على دم المتبرعين."},
 {"en": "Write the standard conditions for blood bag storage.", "ar": "اكتب الشروط القياسية لخزن أكياس الدم.", "answer_en": "Validated devices that keep FDA-regulated temperatures; temperatures monitored continuously and recorded at least every 4 hours; the device alerts on unacceptable temperature; platelet room kept at 20–24 °C.", "answer_ar": "أجهزة مُتحقَّق منها تحافظ على حرارة FDA؛ مراقبة الحرارة باستمرار وتسجيلها كل 4 ساعات على الأقل؛ تنبيه الجهاز عند حرارة غير مقبولة؛ غرفة الصفائح عند 20–24 °م."},
 {"en": "Compare the storage of whole blood/RBCs, platelets and plasma.", "ar": "قارن بين خزن الدم الكامل/الكريات الحمر والصفائح والبلازما.", "answer_en": "Whole blood/RBCs: 1–6 °C; 21 days (ACD, CPD), 35 days (CPDA-1), 42 days (SAGM). Platelets: 20–24 °C with constant agitation. Plasma: frozen –18 °C 1 year or –65 °C 7 years; liquid plasma 1–6 °C (whole blood life + 5 days); thawed 24 h, up to 5 days as “thawed plasma”.", "answer_ar": "الدم الكامل/الكريات الحمر: 1–6 °م؛ 21 يومًا (ACD، CPD)، 35 (CPDA-1)، 42 (SAGM). الصفائح: 20–24 °م مع تحريك مستمر. البلازما: مجمّدة −18 °م سنة أو −65 °م 7 سنوات؛ سائلة 1–6 °م (عمر الدم + 5 أيام)؛ المذابة 24 ساعة، وحتى 5 أيام باسم «بلازما مذابة»."},
]

data = {"meta": {
  "subject_en": "Blood Transfusion", "subject_ar": "نقل الدم", "short_ar": "نقل الدم",
  "unit_en": "Lecture 3", "unit_ar": "المحاضرة 3", "unit_label": "LEC", "unit_no": "3",
  "title_en": "Blood bank services", "title_ar": "خدمات بنك الدم",
  "kind": "Theory & Practical — نظري وعملي", "stage": "The fourth stage — الرابعة", "instructor": "د. مازن اللهيبي"},
 "blocks": blocks, "questions": {"mcq": mcq, "tf": tf, "traps": traps, "important": important}}
from collections import Counter
print(len(mcq), Counter(q["answer"] for q in mcq))
os.makedirs("/home/user/-/bloodbank-lec3-services", exist_ok=True)
json.dump(data, open("/home/user/-/bloodbank-lec3-services/lecture.json", "w"), ensure_ascii=False, indent=1)

```
