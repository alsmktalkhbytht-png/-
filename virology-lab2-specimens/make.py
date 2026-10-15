import json, os
from collections import Counter

def C(en, ar, **k):  return dict(t="card", en=en, ar=ar, **k)
def R(en, ar):       return dict(t="rule", en=en, ar=ar)
def SEC(en, ar):     return dict(t="section", en=en, ar=ar)
def H2(en, ar):      return dict(t="h2", en=en, ar=ar)
def L(en_items, ar_items, en="", ar="", **k):
    return dict(t="card", en=en, ar=ar, list_en=en_items, list_ar=ar_items, **k)
def N(en, ar, label=None):
    b = dict(t="note", en=en, ar=ar)
    if label: b["label"] = label
    return b
def T(head, rows, **k): return dict(t="table", head=head, rows=rows, **k)
def Q(en, ar, opts, ans, **k):
    return dict(en=en, ar=ar, options=[list(o) for o in opts], answer=ans, **k)
def TF(en, ar, a): return dict(en=en, ar=ar, answer=a)
def TR(en, ar, ae, aa): return dict(en=en, ar=ar, answer_en=ae, answer_ar=aa)
IM = TR

blocks = [
 SEC("1. Specimen Collection", "1. جمع العيّنات"),
 H2("Selection of Specimens", "اختيار العيّنات"),
 C("Choose the appropriate specimen based on the suspected virus and clinical symptoms:",
   "اختر العيّنة المناسبة اعتمادًا على **الفيروس المشتبه به** و**الأعراض السريرية**:", keep=True),
 T(["Virus group", "Specimen", "مجموعة الفيروسات — العيّنة"],
   [["Respiratory viruses:", "Nasopharyngeal or oropharyngeal swabs, sputum, or bronchoalveolar lavage.",
     "**الفيروسات التنفسية**: مسحات بلعومية أنفية أو بلعومية فموية، أو قشع، أو غسيل قصبي سنخي"],
    ["Gastrointestinal viruses:", "Stool or rectal swabs.", "**الفيروسات المعوية**: البراز أو المسحات الشرجية"],
    ["Bloodborne viruses:", "Whole blood, plasma, or serum.", "**الفيروسات المنقولة بالدم**: الدم الكامل أو البلازما أو المصل"],
    ["Cutaneous or mucocutaneous viruses:", "Vesicle swabs, tissue biopsies, or skin scrapings.",
     "**الفيروسات الجلدية أو الجلدية المخاطية**: مسحات الحويصلات، أو خزعات الأنسجة، أو كشط الجلد"],
    ["Neurological viruses:", "Cerebrospinal fluid (CSF).", "**الفيروسات العصبية**: السائل الدماغي الشوكي `(CSF)`"]],
   ar_cols=[2], key_cols=[0], widths=["40mm", "", "68mm"]),

 H2("Aseptic Technique", "التقنية المعقّمة"),
 L(["Collect specimens using sterile tools and containers to prevent contamination.",
    "Use gloves, masks, and other to avoid contamination and protect personnel."],
   ["اجمع العيّنات باستعمال **أدوات وحاويات معقّمة** لمنع التلوّث.",
    "استعمل القفّازات والكمّامات وغيرها لتجنّب التلوّث وحماية العاملين."]),

 H2("Collection Guidelines", "إرشادات الجمع"),
 R(["Swabs: Use synthetic fiber-tipped swabs with plastic shafts (e.g., Dacron or rayon).",
    "Avoid cotton swabs with wooden shafts as they may inhibit virus detection."],
   ["**المسحات:** استعمل مسحات **ذات رأس من ألياف صناعية وساق بلاستيكية** (مثل الداكرون أو الرايون).",
    "وتجنّب **المسحات القطنية ذات الساق الخشبية** لأنها قد **تثبّط الكشف عن الفيروس**."]),
 R("Blood: Collect in anticoagulant-treated or plain tubes, depending on the test.",
   "**الدم:** يُجمع في أنابيب معاملة بمانع تخثّر أو أنابيب عادية، حسب الفحص."),
 R("Urine/Stool: Collect in sterile, leak-proof containers.",
   "**الإدرار/البراز:** يُجمع في حاويات **معقّمة ومحكمة لا تسرّب**."),

 H2("Timing", "التوقيت"),
 L(["Collect specimens as early as possible in the course of illness when viral load is typically highest.",
    "Follow specific timing recommendations for optimal diagnostic accuracy."],
   ["اجمع العيّنات **في أبكر وقت ممكن** من مسار المرض، حين يكون **الحمل الفيروسي** عادةً في أعلى مستوياته.",
    "اتّبع توصيات التوقيت الخاصة للحصول على أفضل دقّة تشخيصية."]),

 SEC("2. Specimen Transport", "2. نقل العيّنات"),
 H2("Transport Medium", "وسط النقل"),
 C("Use appropriate viral transport media (VTM) to maintain virus viability:",
   "استعمل **أوساط نقل فيروسية** `(VTM)` مناسبة للمحافظة على **حيوية الفيروس**:",
   list_en=["**Respiratory or swab samples:** Place in VTM containing stabilizing agents and antimicrobials.",
            "**CSF, blood, or stool:** Transport without medium unless otherwise specified."],
   list_ar=["**العيّنات التنفسية أو المسحات:** توضع في `VTM` يحتوي **عوامل مثبّتة ومضادات ميكروبية**.",
            "**السائل الدماغي الشوكي أو الدم أو البراز:** تُنقل **بدون وسط** ما لم يُحدَّد خلاف ذلك."]),

 H2("Temperature Control", "التحكّم بالحرارة"),
 C("Transport specimens quickly to the laboratory to prevent degradation:",
   "انقل العيّنات إلى المختبر **بسرعة** لمنع تحلّلها:",
   list_en=["Refrigerate at **2–8°C** for short-term transport (<72 hours).",
            "Freeze at **-70°C** for long-term storage or transport if delays are expected."],
   list_ar=["تُبرَّد بدرجة **2 إلى 8 °م** للنقل القصير (أقل من 72 ساعة).",
            "تُجمَّد بدرجة سالب 70 °م للخزن الطويل أو للنقل إذا كان التأخير متوقّعًا."]),

 H2("Packaging", "التغليف"),
 C("Use triple-layer packaging to ensure biosafety:", "استعمل **التغليف ثلاثي الطبقات** لضمان السلامة الحيوية:", keep=True),
 R("**Primary container:** Leak-proof, labeled, and sealed (e.g., screw-cap tubes).",
   "**الحاوية الأولية:** محكمة لا تسرّب، وعليها ملصق، ومغلقة (مثل الأنابيب ذات الغطاء اللولبي)."),
 R("**Secondary container:** A sealed bag or canister to contain the primary container.",
   "**الحاوية الثانوية:** كيس أو علبة محكمة تحتوي الحاوية الأولية."),
 R("**Outer packaging:** A sturdy box with proper labeling (e.g., biohazard symbols, “Infectious Substance” if applicable).",
   "**الغلاف الخارجي:** صندوق متين عليه ملصقات صحيحة (مثل رموز الخطر الحيوي، وعبارة «مادة معدية» عند الحاجة)."),
 dict(t="flow", steps=[{"en": "Primary container", "ar": "الحاوية الأولية"},
                       {"en": "Secondary container", "ar": "الحاوية الثانوية"},
                       {"en": "Outer packaging", "ar": "الغلاف الخارجي"}],
      tail_en="From the inside out (drawn for the handout from the lecture text)",
      tail_ar="من الداخل إلى الخارج (رُسم للملزمة من نص المحاضرة)"),

 SEC("3. Specimen Storage", "3. خزن العيّنات"),
 H2("Short-Term Storage", "الخزن قصير الأمد"),
 L(["Maintain at **2–8°C** for specimens processed within 72 hours.",
    "Avoid repeated freeze-thaw cycles to preserve viral integrity."],
   ["تُحفظ بدرجة **2 إلى 8 °م** للعيّنات التي تُعالَج **خلال 72 ساعة**.",
    "تجنّب **دورات التجميد والإذابة المتكرّرة** للمحافظة على سلامة الفيروس."]),
 H2("Long-Term Storage", "الخزن طويل الأمد"),
 L(["Store at **-70°C or below** for long-term preservation.",
    "Use cryoprotective agents (e.g., glycerol or DMSO) for certain specimen types to prevent freeze damage."],
   ["تُخزَّن بدرجة سالب 70 °م **أو أقل** للحفظ الطويل.",
    "استعمل **عوامل واقية من التجميد** (مثل الغليسرول أو `DMSO`) لبعض أنواع العيّنات لمنع ضرر التجميد."]),
 H2("Special Cases", "حالات خاصة"),
 L(["**RNA viruses:** Store at **-80°C** to reduce degradation risk.",
    "**Formalin-fixed tissues:** Store at room temperature for histological analysis, though nucleic acid-based tests may be affected."],
   ["**فيروسات `RNA`:** تُخزَّن بدرجة سالب 80 °م لتقليل خطر التحلّل.",
    "**الأنسجة المثبّتة بالفورمالين:** تُخزَّن بدرجة حرارة الغرفة للتحليل النسيجي، مع أن الفحوص المعتمدة على **الأحماض النووية** قد تتأثّر."]),
 T(["Condition", "Temperature", "الحالة — الحرارة"],
   [["Short-term transport (<72 hours) / short-term storage", "2–8°C", "النقل والخزن القصير (أقل من 72 ساعة) — من 2 إلى 8 °م"],
    ["Long-term storage or delayed transport", "-70°C (or below)", "الخزن الطويل أو النقل المتأخّر — سالب 70 °م أو أقل"],
    ["RNA viruses", "-80°C", "فيروسات `RNA` — سالب 80 °م"],
    ["Formalin-fixed tissues", "Room temperature", "الأنسجة المثبّتة بالفورمالين — حرارة الغرفة"]],
   ar_cols=[2], key_cols=[0], style="summary", label_en="Temperatures at a glance", label_ar="خلاصة درجات الحرارة"),

 H2("Monitoring and Record-Keeping", "المراقبة وحفظ السجلّات"),
 L(["Use temperature-controlled freezers and monitor continuously with alarms for deviations.",
    "Maintain detailed records of specimen receipt, processing, and storage conditions."],
   ["استعمل **مجمّدات مضبوطة الحرارة** وراقبها باستمرار مع **إنذارات** عند الانحراف.",
    "احتفظ **بسجلّات مفصّلة** عن استلام العيّنات ومعالجتها وظروف خزنها."]),

 H2("Common Errors to Avoid", "أخطاء شائعة يجب تجنّبها"),
 L(["Delayed transport without refrigeration, leading to viral degradation.",
    "Use of inappropriate collection materials (e.g., wooden swabs or unsterilized containers).",
    "Labeling errors or incomplete requisition forms."],
   ["**تأخير النقل بدون تبريد**، ما يؤدّي إلى تحلّل الفيروس.",
    "استعمال **مواد جمع غير مناسبة** (مثل المسحات الخشبية أو الحاويات غير المعقّمة).",
    "**أخطاء الملصقات** أو **استمارات الطلب غير المكتملة**."]),
]

mcq = [
 {"topic_en": "MCQs Lab Two (from the lecture)", "topic_ar": "أسئلة المحاضرة (من التدريسية)"},
 Q("Which specimen is most appropriate for the diagnosis of neurological viral infections:", "أيّ عيّنة هي الأنسب لتشخيص العداوى الفيروسية العصبية:",
   [("Stool", "البراز"), ("Serum", "المصل"), ("Cerebrospinal fluid (CSF)", "السائل الدماغي الشوكي"), ("Skin scraping", "كشط الجلد"), ("Sputum", "القشع")], "c"),
 Q("Which type of swab is recommended for viral specimen collection:", "أيّ نوع من المسحات يُوصى به لجمع العيّنات الفيروسية:",
   [("Cotton-tipped swab with a wooden shaft", "مسحة قطنية بساق خشبية"), ("Synthetic fiber-tipped swab with a plastic shaft", "مسحة بألياف صناعية وساق بلاستيكية"),
    ("Metal-tipped swab", "مسحة برأس معدني"), ("Cotton swab with a paper shaft", "مسحة قطنية بساق ورقية"), ("Glass-tipped swab", "مسحة برأس زجاجي")], "b"),
 Q("When should specimens ideally be collected during viral infection:", "متى يُفضَّل جمع العيّنات أثناء العدوى الفيروسية:",
   [("At the end of illness", "في نهاية المرض"), ("After symptoms disappear", "بعد اختفاء الأعراض"), ("As early as possible during the course of illness", "في أبكر وقت ممكن من مسار المرض"),
    ("Only after antibiotic treatment", "بعد العلاج بالمضادات الحيوية فقط"), ("One month after infection", "بعد شهر من العدوى")], "c"),
 Q("What is the recommended temperature for short-term transport of viral specimens for less than 72 hours:", "ما درجة الحرارة الموصى بها للنقل القصير للعيّنات الفيروسية لأقل من 72 ساعة:",
   [("25°C", "25 °م"), ("15°C", "15 °م"), ("10°C", "10 °م"), ("2–8°C", "من 2 إلى 8 °م"), ("−70°C", "سالب 70 °م")], "d"),
 Q("What temperature is recommended for long-term storage of viral specimens:", "ما درجة الحرارة الموصى بها للخزن الطويل للعيّنات الفيروسية:",
   [("37°C", "37 °م"), ("25°C", "25 °م"), ("2–8°C", "من 2 إلى 8 °م"), ("−20°C", "سالب 20 °م"), ("−70°C or below", "سالب 70 °م أو أقل")], "e"),
 Q("Which specimen is commonly used for gastrointestinal viral infections:", "أيّ عيّنة تُستعمل عادةً للعداوى الفيروسية المعوية:",
   [("Cerebrospinal fluid", "السائل الدماغي الشوكي"), ("Stool or rectal swab", "البراز أو المسحة الشرجية"), ("Vesicle fluid only", "سائل الحويصلات فقط"), ("Sputum", "القشع"), ("Skin biopsy", "خزعة الجلد")], "b"),
 Q("What is the main purpose of viral transport medium:", "ما الغرض الرئيس من وسط النقل الفيروسي:",
   [("To kill contaminating viruses", "قتل الفيروسات الملوِّثة"), ("To increase bacterial growth", "زيادة نمو البكتيريا"), ("To maintain virus viability during transport", "المحافظة على حيوية الفيروس أثناء النقل"),
    ("To fix tissues permanently", "تثبيت الأنسجة بشكل دائم"), ("To destroy viral nucleic acids", "تدمير الأحماض النووية الفيروسية")], "c"),
 Q("Why should repeated freeze-thaw cycles be avoided:", "لماذا يجب تجنّب دورات التجميد والإذابة المتكرّرة:",
   [("They increase bacterial growth", "تزيد نمو البكتيريا"), ("They may damage viral integrity", "قد تضرّ بسلامة الفيروس"), ("They increase specimen volume", "تزيد حجم العيّنة"),
    ("They sterilize the specimen", "تعقّم العيّنة"), ("They improve viral detection", "تحسّن الكشف عن الفيروس")], "b"),
 Q("Which of the following is a common error in viral specimen handling:", "أيّ مما يلي خطأ شائع في التعامل مع العيّنات الفيروسية:",
   [("Early specimen collection", "الجمع المبكر للعيّنة"), ("Using sterile containers", "استعمال حاويات معقّمة"), ("Proper labeling", "الملصقات الصحيحة"),
    ("Delayed transport without refrigeration", "تأخير النقل بدون تبريد"), ("Maintaining appropriate temperature", "المحافظة على الحرارة المناسبة")], "d"),

 {"topic_en": "Specimen collection", "topic_ar": "جمع العيّنات"},
 Q("Bronchoalveolar lavage is a specimen for:", "الغسيل القصبي السنخي عيّنة لـ:",
   [("Respiratory viruses", "الفيروسات التنفسية"), ("Gastrointestinal viruses", "الفيروسات المعوية"), ("Neurological viruses", "الفيروسات العصبية"), ("Bloodborne viruses", "الفيروسات المنقولة بالدم")], "a"),
 Q("Vesicle swabs and skin scrapings are used for:", "تُستعمل مسحات الحويصلات وكشط الجلد لـ:",
   [("Bloodborne viruses", "الفيروسات المنقولة بالدم"), ("Respiratory viruses", "الفيروسات التنفسية"), ("Gastrointestinal viruses", "الفيروسات المعوية"), ("Cutaneous or mucocutaneous viruses", "الفيروسات الجلدية أو الجلدية المخاطية")], "d"),
 Q("Whole blood, plasma, or serum are specimens for:", "الدم الكامل أو البلازما أو المصل عيّنات لـ:",
   [("Bloodborne viruses", "الفيروسات المنقولة بالدم"), ("Neurological viruses", "الفيروسات العصبية"), ("Respiratory viruses", "الفيروسات التنفسية"), ("Cutaneous viruses", "الفيروسات الجلدية")], "a"),
 Q("Examples of synthetic swab tips mentioned in the lecture are:", "من أمثلة رؤوس المسحات الصناعية المذكورة في المحاضرة:",
   [("Cotton and wool", "القطن والصوف"), ("Glass and metal", "الزجاج والمعدن"), ("Paper and wood", "الورق والخشب"), ("Dacron or rayon", "الداكرون أو الرايون")], "d"),
 Q("Cotton swabs with wooden shafts should be avoided because they:", "يجب تجنّب المسحات القطنية ذات الساق الخشبية لأنها:",
   [("May inhibit virus detection", "قد تثبّط الكشف عن الفيروس"), ("Are too expensive", "غالية جدًا"), ("Increase viral load", "تزيد الحمل الفيروسي"), ("Contain antimicrobials", "تحتوي مضادات ميكروبية")], "a"),
 Q("Urine and stool should be collected in:", "يُجمع الإدرار والبراز في:",
   [("Anticoagulant tubes", "أنابيب مانع التخثّر"), ("VTM tubes only", "أنابيب VTM فقط"), ("Open cups", "أكواب مفتوحة"), ("Sterile, leak-proof containers", "حاويات معقّمة محكمة لا تسرّب")], "d"),

 {"topic_en": "Transport", "topic_ar": "النقل"},
 Q("Respiratory or swab samples are placed in VTM containing:", "توضع العيّنات التنفسية أو المسحات في `VTM` يحتوي:",
   [("Stabilizing agents and antimicrobials", "عوامل مثبّتة ومضادات ميكروبية"), ("Formalin", "الفورمالين"), ("Anticoagulants only", "مانعات التخثّر فقط"), ("Glycerol only", "الغليسرول فقط")], "a"),
 Q("CSF, blood, or stool are transported:", "تُنقل عيّنات السائل الدماغي الشوكي والدم والبراز:",
   [("Always in VTM", "دائمًا في VTM"), ("In formalin", "في الفورمالين"), ("Without medium unless otherwise specified", "بدون وسط ما لم يُحدَّد خلاف ذلك"), ("Frozen at −20°C", "مجمّدة بدرجة سالب 20 °م")], "c"),
 Q("The packaging layer that contains the primary container is the:", "طبقة التغليف التي تحتوي الحاوية الأولية هي:",
   [("Outer packaging", "الغلاف الخارجي"), ("Secondary container", "الحاوية الثانوية"), ("Screw-cap tube", "الأنبوب ذو الغطاء اللولبي"), ("Requisition form", "استمارة الطلب")], "b"),
 Q("Biohazard symbols and “Infectious Substance” labels are placed on the:", "توضع رموز الخطر الحيوي وعبارة «مادة معدية» على:",
   [("Outer packaging", "الغلاف الخارجي"), ("Primary container", "الحاوية الأولية"), ("Secondary container", "الحاوية الثانوية"), ("Swab shaft", "ساق المسحة")], "a"),
 Q("A screw-cap tube is an example of the:", "الأنبوب ذو الغطاء اللولبي مثال على:",
   [("Outer packaging", "الغلاف الخارجي"), ("Secondary container", "الحاوية الثانوية"), ("Transport medium", "وسط النقل"), ("Primary container", "الحاوية الأولية")], "d"),

 {"topic_en": "Storage", "topic_ar": "الخزن"},
 Q("RNA viruses should be stored at:", "تُخزَّن فيروسات `RNA` بدرجة:",
   [("2–8°C", "من 2 إلى 8 °م"), ("Room temperature", "حرارة الغرفة"), ("−80°C", "سالب 80 °م"), ("−20°C", "سالب 20 °م")], "c"),
 Q("An example of a cryoprotective agent is:", "من أمثلة العوامل الواقية من التجميد:",
   [("Formalin", "الفورمالين"), ("Glycerol", "الغليسرول"), ("EDTA", "EDTA"), ("Saline", "المحلول الملحي")], "b"),
 Q("Formalin-fixed tissues are stored at:", "تُخزَّن الأنسجة المثبّتة بالفورمالين بدرجة:",
   [("Room temperature", "حرارة الغرفة"), ("−70°C", "سالب 70 °م"), ("2–8°C", "من 2 إلى 8 °م"), ("−80°C", "سالب 80 °م")], "a"),
 Q("Freezers used for specimen storage should be:", "يجب أن تكون المجمّدات المستعملة لخزن العيّنات:",
   [("Opened frequently", "تُفتح كثيرًا"), ("Kept at room temperature", "بحرارة الغرفة"), ("Used without records", "تُستعمل بلا سجلّات"), ("Temperature-controlled with alarms for deviations", "مضبوطة الحرارة مع إنذارات للانحراف")], "d"),
]

tf = [
 TF("CSF is the specimen of choice for neurological viruses.", "السائل الدماغي الشوكي هو العيّنة المختارة للفيروسات العصبية.", "T"),
 TF("Cotton swabs with wooden shafts are recommended for virus detection.", "يُوصى بالمسحات القطنية ذات الساق الخشبية للكشف عن الفيروسات.", "F"),
 TF("Specimens should be collected as early as possible, when viral load is typically highest.", "تُجمع العيّنات في أبكر وقت ممكن حين يكون الحمل الفيروسي عادةً في أعلاه.", "T"),
 TF("Blood is always collected in plain tubes only.", "يُجمع الدم دائمًا في أنابيب عادية فقط.", "F"),
 TF("CSF, blood and stool are usually transported in VTM.", "تُنقل عيّنات السائل الدماغي الشوكي والدم والبراز عادةً في `VTM`.", "F"),
 TF("Specimens transported for less than 72 hours are refrigerated at 2–8°C.", "تُبرَّد العيّنات المنقولة لأقل من 72 ساعة بدرجة 2 إلى 8 °م.", "T"),
 TF("Triple-layer packaging consists of primary, secondary and outer packaging.", "يتكوّن التغليف الثلاثي من حاوية أولية وثانوية وغلاف خارجي.", "T"),
 TF("Repeated freeze-thaw cycles preserve viral integrity.", "تحافظ دورات التجميد والإذابة المتكرّرة على سلامة الفيروس.", "F"),
 TF("RNA viruses are stored at −80°C to reduce degradation risk.", "تُخزَّن فيروسات `RNA` بدرجة سالب 80 °م لتقليل خطر التحلّل.", "T"),
 TF("Formalin-fixed tissues are ideal for nucleic acid-based tests.", "الأنسجة المثبّتة بالفورمالين مثالية لفحوص الأحماض النووية.", "F"),
 TF("Glycerol and DMSO are cryoprotective agents.", "الغليسرول و`DMSO` عوامل واقية من التجميد.", "T"),
 TF("Incomplete requisition forms are a common error to avoid.", "استمارات الطلب غير المكتملة من الأخطاء الشائعة الواجب تجنّبها.", "T"),
]

traps = [
 TR("Short-term vs long-term temperatures", "حرارة المدى القصير مقابل الطويل",
    "Short-term (<72 hours): 2–8°C. Long-term: −70°C or below. RNA viruses: −80°C.",
    "القصير (أقل من 72 ساعة): من 2 إلى 8 °م. الطويل: سالب 70 °م أو أقل. فيروسات `RNA`: سالب 80 °م."),
 TR("Which samples go in VTM?", "أيّ العيّنات توضع في `VTM`؟",
    "Respiratory or swab samples go in VTM; CSF, blood and stool are transported without medium unless otherwise specified.",
    "العيّنات **التنفسية والمسحات** في `VTM`، أمّا السائل الدماغي الشوكي والدم والبراز فتُنقل **بدون وسط** ما لم يُحدَّد خلاف ذلك."),
 TR("Swab material", "مادة المسحة",
    "Synthetic fiber tip (Dacron or rayon) with a plastic shaft — not cotton with a wooden shaft.",
    "رأس من **ألياف صناعية** (داكرون أو رايون) بساق **بلاستيكية**، لا قطن بساق خشبية."),
 TR("Formalin-fixed tissue storage", "خزن الأنسجة المثبّتة بالفورمالين",
    "Room temperature (not frozen); good for histology but nucleic acid-based tests may be affected.",
    "بحرارة **الغرفة** لا بالتجميد؛ مناسبة للنسيج لكن فحوص الأحماض النووية قد تتأثّر."),
 TR("Order of triple packaging", "ترتيب التغليف الثلاثي",
    "Inside out: primary container (leak-proof, labeled, sealed) → secondary container (sealed bag or canister) → outer packaging (sturdy labeled box).",
    "من الداخل للخارج: **الأولية** (محكمة وعليها ملصق ومغلقة)، ثم **الثانوية** (كيس أو علبة محكمة)، ثم **الغلاف الخارجي** (صندوق متين عليه ملصقات)."),
 TR("Specimen for gastrointestinal viruses", "عيّنة الفيروسات المعوية",
    "Stool or rectal swabs — not CSF or sputum.",
    "**البراز أو المسحة الشرجية**، لا السائل الدماغي الشوكي ولا القشع."),
]

important = [
 IM("List the appropriate specimens for each group of viruses.", "عدّد العيّنات المناسبة لكل مجموعة من الفيروسات.",
    "Respiratory: nasopharyngeal or oropharyngeal swabs, sputum, bronchoalveolar lavage. Gastrointestinal: stool or rectal swabs. Bloodborne: whole blood, plasma, serum. Cutaneous/mucocutaneous: vesicle swabs, tissue biopsies, skin scrapings. Neurological: CSF.",
    "التنفسية: مسحات بلعومية أنفية أو فموية، قشع، غسيل قصبي سنخي. المعوية: البراز أو المسحات الشرجية. المنقولة بالدم: الدم الكامل أو البلازما أو المصل. الجلدية والجلدية المخاطية: مسحات الحويصلات، خزعات الأنسجة، كشط الجلد. العصبية: السائل الدماغي الشوكي."),
 IM("What are the collection guidelines for swabs, blood and urine/stool?", "ما إرشادات جمع المسحات والدم والإدرار والبراز؟",
    "Swabs: synthetic fiber-tipped with plastic shafts (Dacron or rayon), avoid cotton with wooden shafts. Blood: anticoagulant-treated or plain tubes depending on the test. Urine/stool: sterile, leak-proof containers.",
    "المسحات: رأس ألياف صناعية وساق بلاستيكية (داكرون أو رايون) وتجنّب القطنية ذات الساق الخشبية. الدم: أنابيب بمانع تخثّر أو عادية حسب الفحص. الإدرار والبراز: حاويات معقّمة محكمة لا تسرّب."),
 IM("Explain temperature control during specimen transport.", "اشرح التحكّم بالحرارة أثناء نقل العيّنات.",
    "Transport quickly to prevent degradation; refrigerate at 2–8°C for short-term transport (<72 hours); freeze at −70°C for long-term storage or if delays are expected.",
    "تُنقل بسرعة لمنع التحلّل، وتُبرَّد بدرجة 2 إلى 8 °م للنقل القصير (أقل من 72 ساعة)، وتُجمَّد بدرجة سالب 70 °م للخزن الطويل أو عند توقّع التأخير."),
 IM("Describe triple-layer packaging.", "صف التغليف ثلاثي الطبقات.",
    "Primary container: leak-proof, labeled, sealed (e.g., screw-cap tubes). Secondary container: sealed bag or canister containing the primary. Outer packaging: sturdy box with proper labeling (biohazard symbols, “Infectious Substance”).",
    "الحاوية الأولية: محكمة لا تسرّب وعليها ملصق ومغلقة (مثل الأنابيب ذات الغطاء اللولبي). الثانوية: كيس أو علبة محكمة تحتوي الأولية. الغلاف الخارجي: صندوق متين بملصقات صحيحة (رموز الخطر الحيوي و«مادة معدية»)."),
 IM("Compare short-term and long-term storage of viral specimens, including special cases.", "قارن بين الخزن القصير والطويل للعيّنات الفيروسية مع الحالات الخاصة.",
    "Short-term: 2–8°C for specimens processed within 72 hours, avoiding repeated freeze-thaw cycles. Long-term: −70°C or below, with cryoprotective agents (glycerol, DMSO) for some specimens. RNA viruses: −80°C. Formalin-fixed tissues: room temperature.",
    "القصير: من 2 إلى 8 °م للعيّنات المعالَجة خلال 72 ساعة مع تجنّب التجميد والإذابة المتكرّرة. الطويل: سالب 70 °م أو أقل مع عوامل واقية من التجميد (الغليسرول و`DMSO`) لبعض العيّنات. فيروسات `RNA`: سالب 80 °م. الأنسجة المثبّتة بالفورمالين: حرارة الغرفة."),
 IM("List common errors to avoid in viral specimen handling.", "عدّد الأخطاء الشائعة الواجب تجنّبها في التعامل مع العيّنات الفيروسية.",
    "Delayed transport without refrigeration (viral degradation); inappropriate collection materials (wooden swabs, unsterilized containers); labeling errors or incomplete requisition forms.",
    "تأخير النقل بدون تبريد (تحلّل الفيروس)، واستعمال مواد جمع غير مناسبة (مسحات خشبية، حاويات غير معقّمة)، وأخطاء الملصقات أو استمارات الطلب غير المكتملة."),
]

meta = dict(subject_en="Medical Virology", subject_ar="الفيروسات الطبية", short_ar="فايروسات",
            unit_en="Lab 2", unit_ar="العملي 2", unit_label="LAB", unit_no="2",
            title_en="Specimen Collection, Transport and Storage", title_ar="جمع العيّنات ونقلها وخزنها",
            kind="Laboratories — عملي", stage="The third stage — الثالثة", instructor="م.م. آية وسمي")

folder = "virology-lab2-specimens"
qs = [q for q in mcq if "answer" in q]
print(folder, len(qs), dict(Counter(q["answer"] for q in qs)), len(tf), dict(Counter(t["answer"] for t in tf)), len(traps), len(important))
d = "/home/user/-/" + folder
os.makedirs(d, exist_ok=True)
json.dump({"meta": meta, "blocks": blocks,
           "questions": {"mcq": mcq, "tf": tf, "traps": traps, "important": important}},
          open(d + "/lecture.json", "w"), ensure_ascii=False, indent=1)
