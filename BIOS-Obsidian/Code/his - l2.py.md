---
source: BIOS-Obsidian/tools/scripts/his/l2.py
handouts: [histopathology-lab2-samples]
saved: 2026-10-30
tags: [bios, code]
---
# his/l2.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#histopathology-lab2-samples|histopathology-lab2-samples]]

```python
from l1 import *

def Dfn(t_en, t_ar, en, ar, fig):
    return dict(t="side", blocks=[C(f"**{t_en}** {en}", f"**{t_ar}** {ar}")], figure=dict(src="assets/" + fig[0], en=fig[1], ar=fig[2]))

blocks = [
 SEC("Request of histopathological examination", "طلب الفحص النسيجي المرضي"),
 C("The histopathology lab examines **tissues & organs removed from patients** in order to **identify disease processes, document surgical operations and provide tissue for researches**.",
   "يفحص مختبر الأنسجة **الأنسجة والأعضاء المستأصلة من المرضى** من أجل **تحديد العمليات المرضية، وتوثيق العمليات الجراحية، وتوفير الأنسجة للبحوث**."),
 C("The standard protocols require that a **request** for histopathological examination **must be written** , and the request should contain:",
   "تتطلّب البروتوكولات القياسية أن يكون **طلب** الفحص النسيجي المرضي **مكتوبًا**، ويجب أن يحتوي على:",
   list_en=["Patient identification", "Procedure type & date",
            "Clinical data (type of specimen, purpose of removal, type & location of any lesion if present, previous diagnosis, previous or current treatment..etc)"],
   list_ar=["هوية المريض", "نوع الإجراء وتاريخه",
            "البيانات السريرية (نوع العيّنة، والغرض من الاستئصال، ونوع أي آفة وموقعها إن وُجدت، والتشخيص السابق، والعلاج السابق أو الحالي.. إلخ)"]),
 C(["The pathologist's **interpretation** of a biopsy is critical to identify the diagnosis of a a **benign or malignant** tumor, differentiate between different **types and grades** of cancer, **staging** the extent of malignant disease and assessing **surgical margins**.",
    "Biopsies are also used to diagnose diseases other than cancer, including **inflammatory & infectious** diseases ."],
   ["إن **تفسير** أخصائي الأمراض للخزعة أساسي لتشخيص الورم **الحميد أو الخبيث**، والتمييز بين **أنواع السرطان ودرجاته**، و**تحديد مرحلة** انتشار المرض الخبيث، وتقييم **الحواف الجراحية**.",
    "وتُستخدم الخزعات أيضًا لتشخيص أمراض غير السرطان، ومنها الأمراض **الالتهابية والمعدية**."]),

 SEC("Types of pathology specimens", "أنواع العيّنات المرضية"),
 C("In general pathology specimens can be divided into **two main types**:", "بشكل عام تُقسَّم العيّنات المرضية إلى **نوعين رئيسين**:"),
 R(["**Tissue biopsy:** a biopsy is a small piece of tissue removed primarily for histopathological analysis.",
    "Types of biopsies include : core biopsies , punch biopsy, shave biopsy, endoscopic biopsy, incisional biopsy, excisional biopsy and surgical resection specimens ."],
   ["**الخزعة النسيجية:** الخزعة قطعة صغيرة من النسيج تُستأصل أساسًا للتحليل النسيجي المرضي.",
    "وتشمل أنواع الخزعات: الخزعة اللبّية، والخزعة الثاقبة، والخزعة الكشطية، والخزعة بالمنظار، والخزعة الشقّية، والخزعة الاستئصالية، وعيّنات الاستئصال الجراحي."]),
 R(["**cytology :** in which smears can be made from **cells suspended in a fluid** or individual cells have been **scraped, brushed, or aspirated (sucked)** from a surface or from within an organ .",
    "Cytology smears can be taken by **Fine needle aspiration, pap test or body fluids**."],
   ["**علم الخلايا:** وفيه تُحضَّر المسحات من **خلايا معلّقة في سائل** أو من خلايا مفردة **كُشطت أو فُرشت أو شُفطت (مُصّت)** من سطح أو من داخل عضو.",
    "وتُؤخذ المسحات الخلوية بـ**الشفط بالإبرة الدقيقة، أو مسحة باب، أو من سوائل الجسم**."]),

 H2("Tissue biopsies", "الخزعات النسيجية"),
 C("**core biopsy (tru-cut biopsy):** a **core of tissue (about 2 mm thick)** is taken by using a special **large-bore needle** from specific area or lump, usually done through the skin under the guidance of **radiological techniques** such as ultrasound, CT scan or MRI",
   "**الخزعة اللبّية (`tru-cut`):** يُؤخذ **لبّ من النسيج (بسُمك نحو 2 ملم)** باستخدام **إبرة خاصة واسعة التجويف** من منطقة أو كتلة محدّدة، وتُجرى عادةً عبر الجلد بتوجيه **التقنيات الشعاعية** مثل الموجات فوق الصوتية أو المفراس الحلزوني أو الرنين المغناطيسي"),
 dict(t="figures", items=[dict(src="assets/core-biopsy-principle.jpg", en="Principle of tru-cut biopsy: push, slide, withdraw", ar="مبدأ خزعة `tru-cut`: الدفع، ثم الانزلاق، ثم السحب", h="50mm", fit="contain"),
                          dict(src="assets/core-biopsy-ultrasound.jpg", en="Core biopsy under ultrasound guidance", ar="خزعة لبّية بتوجيه الموجات فوق الصوتية", h="50mm", fit="contain")]),
 C("**Punch biopsy :** where a special surgical instrument is used to remove a **small piece of suspicious area from the top layers** of the tissue for examination (often from the **skin or cervix**).",
   "**الخزعة الثاقبة:** تُستخدم فيها أداة جراحية خاصة لإزالة **قطعة صغيرة من المنطقة المشتبه بها من الطبقات العليا** للنسيج لفحصها (غالبًا من **الجلد أو عنق الرحم**)."),
 dict(t="figures", items=[dict(src="assets/punch-biopsy.jpg", en="Punch biopsy of the skin", ar="الخزعة الثاقبة للجلد", h="46mm", fit="contain"),
                          dict(src="assets/punch-biopsy-photos.jpg", en="Punch biopsy steps", ar="خطوات الخزعة الثاقبة", h="46mm", fit="contain")]),
 C("**Endoscopic biopsy :** A **flexible tube (endoscope)** with a light on the end to see structures inside your body. Special tools are passed with the tube to take a small sample of tissue to be analysed.",
   "**الخزعة بالمنظار:** **أنبوب مرن (منظار)** في نهايته ضوء لرؤية التراكيب داخل الجسم، وتُمرَّر معه أدوات خاصة لأخذ عيّنة صغيرة من النسيج لتحليلها."),
 dict(t="figures", items=[dict(src="assets/endoscopic-biopsy.jpg", en="Endoscopic biopsy", ar="الخزعة بالمنظار", h="46mm", fit="contain"),
                          dict(src="assets/endoscopic-forceps.jpg", en="Endoscopic biopsy forceps", ar="ملقط الخزعة بالمنظار", h="46mm", fit="contain")]),
 C("**Excisional biopsy :** Removal of the **whole lesion with free margins** and re-stitching of the wound margins",
   "**الخزعة الاستئصالية:** إزالة **الآفة كاملة مع حواف سليمة** ثم إعادة خياطة حواف الجرح"),
 C("**Incisional biopsy:** they are done through diagnostic surgical procedures that remove **part of a suspicious lesion** for microscopic examination.",
   "**الخزعة الشقّية:** تُجرى عبر إجراءات جراحية تشخيصية تُزيل **جزءًا من الآفة المشتبه بها** للفحص المجهري."),
 dict(t="figures", items=[dict(src="assets/excisional-biopsy.jpg", en="Excisional biopsy: line of incision around the lesion, then primary closure", ar="الخزعة الاستئصالية: خط الشق حول الآفة ثم الإغلاق الأولي", h="44mm", fit="contain"),
                          dict(src="assets/incisional-excisional.jpg", en="Incisional (part of the lesion) vs excisional (whole lesion) biopsy", ar="الخزعة الشقّية (جزء من الآفة) مقابل الاستئصالية (الآفة كاملة)", h="44mm", fit="contain")]),
 C("**Surgical resection specimens:** **therapeutic** surgical removal of an **entire diseased area or organ** (sometimes even multiple organs).",
   "**عيّنات الاستئصال الجراحي:** إزالة جراحية **علاجية** لـ**منطقة مريضة كاملة أو عضو كامل** (وأحيانًا أعضاء متعدّدة)."),
 dict(t="figures", items=[dict(src="assets/resection-2.jpg", en="Surgical resection specimen", ar="عيّنة استئصال جراحي", h="40mm", fit="contain"),
                          dict(src="assets/resection-3.jpg", en="Surgical resection specimen (bone)", ar="عيّنة استئصال جراحي (عظم)", h="40mm", fit="contain")]),

 H2("Cytology", "علم الخلايا"),
 dict(t="side", blocks=[C("**Fine needle aspiration:** (**FNA**) is the **most frequently used technique in cytology**. It is typically used to sample **'lumps and bumps'** on the body",
   "**الشفط بالإبرة الدقيقة** (`FNA`): هو **أكثر التقنيات استخدامًا في علم الخلايا**، ويُستخدم عادةً لأخذ عيّنات من **«الكتل والنتوءات»** في الجسم")],
   figure=dict(src="assets/fna.jpg", en="Fine needle aspiration of a lump", ar="الشفط بالإبرة الدقيقة من كتلة")),
 C("**Exfoliative cytology:** sometimes by **brushing the lesion** and collect the cells in a **special fixative**", "**علم الخلايا التقشّري:** أحيانًا **بفرش الآفة بفرشاة** وجمع الخلايا في **مثبّت خاص**"),
 dict(t="figures", items=[dict(src="assets/exfoliative-spatula.jpg", en="Cervical sampling with a spatula/brush (cells from endocervix, transformation zone, ectocervix)", ar="أخذ عيّنة من عنق الرحم بالملوق/الفرشاة (خلايا من باطن العنق، ومنطقة التحوّل، وظاهر العنق)", h="46mm", fit="contain"),
                          dict(src="assets/exfoliative-brush.jpg", en="Oral brush cytology", ar="أخذ عيّنة خلوية من الفم بالفرشاة", h="46mm", fit="contain")]),
 T(["Biopsy", "Key point", "الخزعة — النقطة الأساسية"],
   [["Core (tru-cut)", "~2 mm core, large-bore needle, radiological guidance", "**اللبّية**: لبّ نحو 2 ملم، إبرة واسعة، توجيه شعاعي"],
    ["Punch", "Top layers, skin or cervix", "**الثاقبة**: الطبقات العليا، الجلد أو عنق الرحم"],
    ["Endoscopic", "Flexible tube with light", "**بالمنظار**: أنبوب مرن مع ضوء"],
    ["Excisional", "Whole lesion with free margins", "**الاستئصالية**: الآفة كاملة مع حواف سليمة"],
    ["Incisional", "Part of the lesion", "**الشقّية**: جزء من الآفة"],
    ["Surgical resection", "Therapeutic, entire area or organ", "**الاستئصال الجراحي**: علاجي، منطقة أو عضو كامل"],
    ["FNA", "Most used in cytology; lumps and bumps", "**الشفط بالإبرة الدقيقة**: الأكثر استخدامًا في علم الخلايا؛ الكتل"],
    ["Exfoliative", "Brushing; special fixative", "**التقشّري**: بالفرشاة؛ مثبّت خاص"]],
   ar_cols=[2], key_cols=[0], style="summary", label_en="Specimens at a glance", label_ar="العيّنات باختصار"),
]

mcq = [
 {"topic_en": "Request and specimen types", "topic_ar": "الطلب وأنواع العيّنات"},
 Q("The histopathology lab examines tissues and organs to do all EXCEPT:", "يفحص مختبر الأنسجة الأنسجة والأعضاء لكل مما يأتي عدا:", [("Identify disease processes", "تحديد العمليات المرضية"), ("Document surgical operations", "توثيق العمليات الجراحية"), ("Provide tissue for research", "توفير الأنسجة للبحوث"), ("Cross-match blood", "مطابقة الدم")], "d"),
 Q("The request for histopathological examination must be:", "يجب أن يكون طلب الفحص النسيجي:", [("Verbal", "شفهيًا"), ("Written", "مكتوبًا"), ("Optional", "اختياريًا"), ("Sent after the report", "بعد التقرير")], "b"),
 Q("Which is NOT required in the request?", "أي مما يأتي ليس مطلوبًا في الطلب؟", [("Patient identification", "هوية المريض"), ("Procedure type & date", "نوع الإجراء وتاريخه"), ("Patient's salary", "راتب المريض"), ("Clinical data", "البيانات السريرية")], "c"),
 Q("The pathologist's interpretation of a biopsy helps in all EXCEPT:", "يساعد تفسير الخزعة في كل مما يأتي عدا:", [("Benign vs malignant", "حميد أم خبيث"), ("Grading cancer", "درجة السرطان"), ("Assessing surgical margins", "تقييم الحواف الجراحية"), ("Measuring blood glucose", "قياس كلوكوز الدم")], "d"),
 Q("Pathology specimens are divided into two main types:", "تُقسَّم العيّنات المرضية إلى نوعين رئيسين:", [("Tissue biopsy and cytology", "الخزعة النسيجية وعلم الخلايا"), ("Blood and urine", "الدم والبول"), ("Fixed and frozen", "مثبّتة ومجمّدة"), ("Solid and liquid", "صلبة وسائلة")], "a"),
 Q("Cytology smears can be taken by:", "تُؤخذ المسحات الخلوية بـ:", [("Surgical resection", "الاستئصال الجراحي"), ("Punch biopsy", "الخزعة الثاقبة"), ("FNA, pap test or body fluids", "الشفط الدقيق أو مسحة باب أو سوائل الجسم"), ("Core biopsy", "الخزعة اللبّية")], "c"),
 {"topic_en": "Biopsy types", "topic_ar": "أنواع الخزعات"},
 Q("Core (tru-cut) biopsy takes a core of tissue about:", "تأخذ الخزعة اللبّية لبًّا من النسيج بسُمك نحو:", [("2 mm", "2 ملم"), ("2 cm", "2 سم"), ("0.2 mm", "0.2 ملم"), ("10 mm", "10 ملم")], "a"),
 Q("Core biopsy is usually guided by:", "توجَّه الخزعة اللبّية عادةً بـ:", [("Naked eye only", "العين المجرّدة فقط"), ("Radiological techniques (US, CT, MRI)", "التقنيات الشعاعية"), ("Endoscope", "المنظار"), ("Microscope", "المجهر")], "b"),
 Q("Removing a small piece from the top layers of the skin or cervix is a:", "إزالة قطعة صغيرة من الطبقات العليا للجلد أو عنق الرحم تُسمّى:", [("Excisional biopsy", "خزعة استئصالية"), ("Core biopsy", "خزعة لبّية"), ("Resection", "استئصال جراحي"), ("Punch biopsy", "خزعة ثاقبة")], "d"),
 Q("A flexible tube with a light used to take a tissue sample is used in:", "الأنبوب المرن مع الضوء لأخذ عيّنة نسيجية يُستخدم في:", [("Endoscopic biopsy", "الخزعة بالمنظار"), ("FNA", "الشفط الدقيق"), ("Punch biopsy", "الخزعة الثاقبة"), ("Pap test", "مسحة باب")], "a"),
 Q("Removal of the whole lesion with free margins is:", "إزالة الآفة كاملة مع حواف سليمة هي:", [("Incisional biopsy", "خزعة شقّية"), ("Excisional biopsy", "خزعة استئصالية"), ("Core biopsy", "خزعة لبّية"), ("Shave biopsy", "خزعة كشطية")], "b"),
 Q("Removal of part of a suspicious lesion is:", "إزالة جزء من الآفة المشتبه بها هي:", [("Excisional biopsy", "خزعة استئصالية"), ("Surgical resection", "استئصال جراحي"), ("Incisional biopsy", "خزعة شقّية"), ("FNA", "الشفط الدقيق")], "c"),
 Q("Therapeutic removal of an entire diseased organ gives a:", "الإزالة العلاجية لعضو مريض كامل تعطي:", [("Punch biopsy", "خزعة ثاقبة"), ("Cytology smear", "مسحة خلوية"), ("Core biopsy", "خزعة لبّية"), ("Surgical resection specimen", "عيّنة استئصال جراحي")], "d"),
 {"topic_en": "Cytology", "topic_ar": "علم الخلايا"},
 Q("The most frequently used technique in cytology is:", "أكثر التقنيات استخدامًا في علم الخلايا:", [("Fine needle aspiration", "الشفط بالإبرة الدقيقة"), ("Excisional biopsy", "الخزعة الاستئصالية"), ("Resection", "الاستئصال"), ("Punch biopsy", "الخزعة الثاقبة")], "a"),
 Q("FNA is typically used to sample:", "يُستخدم الشفط الدقيق عادةً لأخذ عيّنات من:", [("Bone marrow only", "النخاع فقط"), ("'Lumps and bumps'", "«الكتل والنتوءات»"), ("Blood vessels", "الأوعية الدموية"), ("Whole organs", "الأعضاء الكاملة")], "b"),
 Q("In exfoliative cytology, cells are collected by brushing and placed in:", "في علم الخلايا التقشّري تُجمع الخلايا بالفرشاة وتوضع في:", [("Water", "الماء"), ("Saline only", "المحلول الملحي فقط"), ("A special fixative", "مثبّت خاص"), ("Paraffin", "البرافين")], "c"),
 {"topic_en": "Picture questions", "topic_ar": "أسئلة الصور"},
 Q("This figure shows the push–slide–withdraw principle of which biopsy?", "يُظهر هذا الشكل مبدأ الدفع والانزلاق والسحب لأي خزعة؟", [("Punch biopsy", "الثاقبة"), ("Tru-cut (core) biopsy", "اللبّية (tru-cut)"), ("Excisional biopsy", "الاستئصالية"), ("FNA", "الشفط الدقيق")], "b", img="assets/core-biopsy-principle.jpg", img_h="40mm"),
 Q("The rotating circular blade on the skin in this figure is a:", "الشفرة الدائرية الدوّارة على الجلد في هذا الشكل:", [("Punch biopsy", "خزعة ثاقبة"), ("Endoscopic biopsy", "خزعة بالمنظار"), ("Core biopsy", "خزعة لبّية"), ("Resection", "استئصال")], "a", img="assets/punch-biopsy.jpg", img_h="38mm"),
 Q("In this figure, the biopsy that removes the whole lesion is labelled:", "في هذا الشكل، الخزعة التي تزيل الآفة كاملة مكتوب عليها:", [("Incisional biopsy", "Incisional biopsy"), ("Core biopsy", "Core biopsy"), ("Punch biopsy", "Punch biopsy"), ("Excisional biopsy", "Excisional biopsy")], "d", img="assets/incisional-excisional.jpg", img_h="38mm"),
 Q("The technique shown (a syringe with a fine needle in a lump) is:", "التقنية في الشكل (محقنة بإبرة دقيقة في كتلة):", [("Punch biopsy", "خزعة ثاقبة"), ("Exfoliative cytology", "علم الخلايا التقشّري"), ("Fine needle aspiration", "الشفط بالإبرة الدقيقة"), ("Endoscopic biopsy", "خزعة بالمنظار")], "c", img="assets/fna.jpg", img_h="40mm"),
 Q("Brushing the oral lesion as in this figure is an example of:", "فرش آفة الفم كما في هذا الشكل مثال على:", [("Exfoliative cytology", "علم الخلايا التقشّري"), ("Core biopsy", "الخزعة اللبّية"), ("Resection", "الاستئصال"), ("Excisional biopsy", "الخزعة الاستئصالية")], "a", img="assets/exfoliative-brush.jpg", img_h="38mm"),
]
tf = [
 TF("The request for histopathological examination must be written.", "يجب أن يكون طلب الفحص النسيجي مكتوبًا.", "T"),
 TF("Previous treatment is part of the clinical data in the request.", "العلاج السابق جزء من البيانات السريرية في الطلب.", "T"),
 TF("Biopsies are used only to diagnose cancer.", "تُستخدم الخزعات لتشخيص السرطان فقط.", "F"),
 TF("A biopsy is a small piece of tissue removed for histopathological analysis.", "الخزعة قطعة صغيرة من النسيج تُستأصل للتحليل النسيجي.", "T"),
 TF("Shave biopsy is one of the types of tissue biopsy.", "الخزعة الكشطية من أنواع الخزعة النسيجية.", "T"),
 TF("Core biopsy uses a fine thin needle.", "تستخدم الخزعة اللبّية إبرة دقيقة رفيعة.", "F"),
 TF("Punch biopsy is often taken from the skin or cervix.", "تُؤخذ الخزعة الثاقبة غالبًا من الجلد أو عنق الرحم.", "T"),
 TF("Incisional biopsy removes the whole lesion with free margins.", "تزيل الخزعة الشقّية الآفة كاملة مع حواف سليمة.", "F"),
 TF("Surgical resection may remove multiple organs.", "قد يزيل الاستئصال الجراحي أعضاء متعدّدة.", "T"),
 TF("FNA is the least used technique in cytology.", "الشفط الدقيق أقل التقنيات استخدامًا في علم الخلايا.", "F"),
 TF("The pap test is a cytology technique.", "مسحة باب تقنية من علم الخلايا.", "T"),
]
traps = [
 TR("Excisional vs incisional biopsy", "الخزعة الاستئصالية مقابل الشقّية", "Excisional: the whole lesion with free margins. Incisional: only part of the lesion.", "الاستئصالية: الآفة كاملة مع حواف سليمة. الشقّية: جزء من الآفة فقط."),
 TR("Excisional biopsy vs surgical resection", "الخزعة الاستئصالية مقابل الاستئصال الجراحي", "Excisional: a lesion removed for diagnosis. Resection: therapeutic removal of an entire area or organ (even several organs).", "الاستئصالية: إزالة آفة للتشخيص. الاستئصال الجراحي: إزالة علاجية لمنطقة أو عضو كامل (وأحيانًا عدة أعضاء)."),
 TR("Core biopsy vs FNA — which needle?", "الخزعة اللبّية مقابل الشفط الدقيق — أي إبرة؟", "Core: large-bore needle, a 2 mm tissue core (biopsy). FNA: fine needle, cells (cytology).", "اللبّية: إبرة واسعة ولبّ نسيجي 2 ملم (خزعة). الشفط الدقيق: إبرة دقيقة وخلايا (علم خلايا)."),
 TR("Is FNA a tissue biopsy?", "هل الشفط الدقيق خزعة نسيجية؟", "No — FNA, pap test and body fluids belong to cytology.", "لا — الشفط الدقيق ومسحة باب وسوائل الجسم من علم الخلايا."),
 TR("Punch biopsy depth", "عمق الخزعة الثاقبة", "Only the top layers of the tissue (skin or cervix).", "الطبقات العليا من النسيج فقط (الجلد أو عنق الرحم)."),
]
important = [
 IM("What must the request for histopathological examination contain?", "ماذا يجب أن يحتوي طلب الفحص النسيجي المرضي؟", "It must be written and contain: patient identification; procedure type and date; clinical data (specimen type, purpose of removal, type and location of any lesion, previous diagnosis, previous or current treatment).", "يجب أن يكون مكتوبًا ويحتوي: هوية المريض؛ نوع الإجراء وتاريخه؛ البيانات السريرية (نوع العيّنة، الغرض من الاستئصال، نوع الآفة وموقعها، التشخيص السابق، العلاج السابق أو الحالي)."),
 IM("Why is the pathologist's interpretation of a biopsy important?", "لماذا يُعدّ تفسير أخصائي الأمراض للخزعة مهمًا؟", "To diagnose benign or malignant tumours, differentiate types and grades of cancer, stage malignant disease and assess surgical margins; also to diagnose inflammatory and infectious diseases.", "لتشخيص الأورام الحميدة أو الخبيثة، والتمييز بين أنواع السرطان ودرجاته، وتحديد مرحلة المرض الخبيث، وتقييم الحواف الجراحية؛ ولتشخيص الأمراض الالتهابية والمعدية."),
 IM("Classify pathology specimens.", "صنّف العيّنات المرضية.", "(1) Tissue biopsy: core, punch, shave, endoscopic, incisional, excisional, surgical resection. (2) Cytology: cells in fluid, scraped, brushed or aspirated — FNA, pap test, body fluids.", "(1) الخزعة النسيجية: اللبّية، الثاقبة، الكشطية، بالمنظار، الشقّية، الاستئصالية، الاستئصال الجراحي. (2) علم الخلايا: خلايا في سائل أو مكشوطة أو مفروشة أو مشفوطة — الشفط الدقيق، مسحة باب، سوائل الجسم."),
 IM("Describe core (tru-cut) and punch biopsy.", "صف الخزعة اللبّية والثاقبة.", "Core: a ~2 mm core taken with a large-bore needle from a lump, through the skin under ultrasound/CT/MRI guidance. Punch: a special instrument removes a small piece from the top layers (skin, cervix).", "اللبّية: لبّ نحو 2 ملم بإبرة واسعة من كتلة عبر الجلد بتوجيه الموجات فوق الصوتية/المفراس/الرنين. الثاقبة: أداة خاصة تزيل قطعة صغيرة من الطبقات العليا (الجلد، عنق الرحم)."),
 IM("Compare excisional, incisional and surgical resection specimens.", "قارن بين الخزعة الاستئصالية والشقّية والاستئصال الجراحي.", "Excisional: whole lesion with free margins, wound re-stitched. Incisional: part of a suspicious lesion. Resection: therapeutic removal of an entire diseased area or organ.", "الاستئصالية: الآفة كاملة مع حواف سليمة وخياطة الجرح. الشقّية: جزء من الآفة المشتبه بها. الاستئصال الجراحي: إزالة علاجية لمنطقة مريضة أو عضو كامل."),
 IM("What are FNA and exfoliative cytology?", "ما الشفط بالإبرة الدقيقة وعلم الخلايا التقشّري؟", "FNA: the most used cytology technique, sampling lumps and bumps with a fine needle. Exfoliative cytology: brushing the lesion and collecting cells in a special fixative.", "الشفط الدقيق: أكثر تقنيات علم الخلايا استخدامًا، لأخذ عيّنات من الكتل بإبرة دقيقة. التقشّري: فرش الآفة وجمع الخلايا في مثبّت خاص."),
]
save("histopathology-lab2-samples", 2, "Types of samples & sample handling", "أنواع العيّنات والتعامل معها", blocks, mcq, tf, traps, important)

```
