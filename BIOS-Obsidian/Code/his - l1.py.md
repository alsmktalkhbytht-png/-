---
source: BIOS-Obsidian/tools/scripts/his/l1.py
handouts: [histopathology-lab1-lab-safety]
saved: 2026-10-28
tags: [bios, code]
---
# his/l1.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#histopathology-lab1-lab-safety|histopathology-lab1-lab-safety]]

```python
import sys; sys.path.insert(0, "/tmp/claude-0/-home-user--/8f878068-bae9-502b-96f7-788f221c7cb0/scratchpad/hem3")
from common import C, R, SEC, H2, L, N, FLOW, T, Q, TF, TR
import json, os
from collections import Counter
IM = TR
def F(src, en, ar, **k): return dict(t="figure", src="assets/" + src, en=en, ar=ar, **k)
def FF(*items): return dict(t="figures", items=[dict(src="assets/" + s, en=e, ar=a, h=h, fit="contain") for s, e, a, h in items])

def save(folder, no, title_en, title_ar, blocks, mcq, tf, traps, important):
    data = {"meta": {
        "subject_en": "Histopathology", "subject_ar": "علم الأمراض النسيجية", "short_ar": "انسجة",
        "unit_en": f"Lab {no}", "unit_ar": f"العملي {no}", "unit_label": "LAB", "unit_no": str(no),
        "title_en": title_en, "title_ar": title_ar,
        "kind": "Laboratories — عملي", "stage": "The third stage — الثالثة", "instructor": "م.م. آية وسمي"},
        "blocks": blocks, "questions": {"mcq": mcq, "tf": tf, "traps": traps, "important": important}}
    qs = [q for q in mcq if "answer" in q]
    print(folder, len(qs), dict(Counter(q["answer"] for q in qs)), len(tf), len(traps), len(important))
    d = "/home/user/-/" + folder; os.makedirs(d, exist_ok=True)
    json.dump(data, open(d + "/lecture.json", "w"), ensure_ascii=False, indent=1)

if __name__ == "__main__":
  blocks = [
   SEC("HISTOPATHOLOGY — Definition", "علم الأمراض النسيجية — التعريف"),
   L(["**Histo** : Tissue", "**Histology** : Study of anatomy of normal cell or tissue.", "**Histopathology** : Study of diseased tissue at microscopic level.",
      "**Histotechniques** : Processing of tissue in such a manner that it enables the satisfactory study of tissue."],
     ["**`Histo`**: نسيج", "**علم الأنسجة** (`Histology`): دراسة تشريح الخلية أو النسيج الطبيعي.", "**علم الأمراض النسيجية** (`Histopathology`): دراسة النسيج المريض على المستوى المجهري.",
      "**التقنيات النسيجية** (`Histotechniques`): معالجة النسيج بطريقة تتيح دراسته دراسة مُرضية."]),
   H2("What is Histopathology", "ما علم الأمراض النسيجية"),
   L(["Histopathology is the **diagnosis and study of diseases of the tissue**, and involves examining tissue and/or cell **under a microscope**.",
      "**Histopathologist** are responsible for making **tissue diagnoses** and helping clinicians manage a patient's care."],
     ["علم الأمراض النسيجية هو **تشخيص أمراض النسيج ودراستها**، ويتضمّن فحص النسيج و/أو الخلية **بالمجهر**.",
      "**أخصائيو علم الأمراض النسيجية** مسؤولون عن **التشخيص النسيجي** ومساعدة الأطباء السريريين في إدارة رعاية المريض."]),
   H2("What is Histopathology Laboratory", "ما مختبر علم الأمراض النسيجية"),
   L(["Histopathology Laboratory is specially designed to undergo histopathological diagnosis like studying the **malignant or benign condition** of tissue",
      "In this Laboratory we also study **morphology of tissues**",
      "In **Immunohistochemistry** section presence of **specific antigen or special molecules** on tissue is detected. We detect the presence of **tumor marker** to indentify different types cancer"],
     ["مختبر علم الأمراض النسيجية مصمّم خصيصًا لإجراء التشخيص النسيجي المرضي، مثل دراسة **الحالة الخبيثة أو الحميدة** للنسيج",
      "وفي هذا المختبر ندرس أيضًا **شكل الأنسجة**",
      "وفي قسم **الكيمياء النسيجية المناعية** يُكشف عن وجود **مستضد معيّن أو جزيئات خاصة** على النسيج. ونكشف عن وجود **الواسم الورمي** لتحديد أنواع السرطان المختلفة"]),

   SEC("Laboratory Management & Chemical Safety in the Lab", "إدارة المختبر والسلامة الكيميائية فيه"),
   L(["Personal Protective Equipment (PPE)", "Safe Chemical Handling", "Proper Chemical Storage", "Chemical Waste Disposal", "Emergency Procedures", "Laboratory Hygiene", "Accident Prevention"],
     ["معدّات الوقاية الشخصية (`PPE`)", "التعامل الآمن مع المواد الكيميائية", "الخزن السليم للمواد الكيميائية", "التخلّص من النفايات الكيميائية", "إجراءات الطوارئ", "نظافة المختبر", "منع الحوادث"]),
   H2("Chemicals & Reagents", "المواد الكيميائية والكواشف"),
   L(["Fixative", "Decalcifying Agents", "Dehydrating Agents", "Clearing Agents", "Embedding Agents", "Staining Chemicals", "Mounting Medium"],
     ["المثبّت", "عوامل إزالة الكلس", "عوامل نزع الماء", "عوامل الترويق (التصفية)", "عوامل الطمر", "مواد التصبيغ", "وسط التحميل (التركيب)"]),
   dict(t="side", blocks=[L(["Laboratory Construction", "Proper Laboratory Layout", "Good Ventilation", "Adequate Lighting", "Safe Electrical Systems", "Emergency Exits", "Fire Safety Equipment", "Safe Workspaces"],
     ["بناء المختبر", "تخطيط سليم للمختبر", "تهوية جيدة", "إضاءة كافية", "أنظمة كهربائية آمنة", "مخارج طوارئ", "معدّات السلامة من الحريق", "أماكن عمل آمنة"],
     en="**Laboratory construction**", ar="**بناء المختبر**")],
     figure=dict(src="assets/lab-construction.jpg", en="Laboratory", ar="المختبر")),
   dict(t="side", blocks=[L(["Laboratory Staff", "Qualified Staff", "Proper Training", "Safety Awareness", "Good Communication", "Teamwork", "Following Safety Rules"],
     ["كادر المختبر", "كادر مؤهّل", "تدريب مناسب", "وعي بالسلامة", "تواصل جيد", "العمل بروح الفريق", "اتّباع قواعد السلامة"],
     en="**Laboratory staff**", ar="**كادر المختبر**")],
     figure=dict(src="assets/lab-staff.jpg", en="Laboratory staff", ar="كادر المختبر")),

   SEC("Safety in pathology lab", "السلامة في مختبر الأمراض"),
   C("The histopathology department is **rich in hazards** including :", "قسم علم الأمراض النسيجية **غني بالمخاطر**، ومنها:",
     list_en=["**Biological or infectious hazard** (HBV, HCV, HIV, T.B…etc)", "**Physical hazard** (burn, injury by sharp instruments, electrical injury…etc)", "**Chemical hazard**"],
     list_ar=["**الخطر الحيوي أو المعدي** (`HBV`، `HCV`، `HIV`، التدرّن… إلخ)", "**الخطر الفيزيائي** (الحروق، الإصابة بالأدوات الحادة، الصدمة الكهربائية… إلخ)", "**الخطر الكيميائي**"]),
   FF(("biohazard.jpg", "Caution — Biohazard", "تحذير — خطر حيوي", "46mm"), ("danger-formaldehyde.jpg", "Danger — Formaldehyde: irritant and potential cancer hazard", "خطر — الفورمالديهايد: مهيّج وخطر سرطاني محتمل", "46mm")),

   SEC("Universal precautions", "الاحتياطات العامة (الشاملة)"),
   C("To prevent the transmission of infective agents with serious health hazards: **hepatitis B, hepatitis C and HIV**",
     "لمنع انتقال العوامل المعدية ذات المخاطر الصحية الخطيرة: **التهاب الكبد `B`، والتهاب الكبد `C`، و`HIV`**"),
   C("**Body fluids that need universal precautions:** blood, peritoneal and pleural fluid, CSF, semen, vaginal secretions, synovial effusion and faecal material",
     "**سوائل الجسم التي تحتاج إلى الاحتياطات العامة:** الدم، والسائل البريتوني والجنبي، والسائل الدماغي الشوكي، والسائل المنوي، والإفرازات المهبلية، والانصباب الزليلي، والمواد البرازية"),
   dict(t="side", blocks=[L(["hand wash", "gloves", "Mask", "Goggles", "Aprons or gowns", "Take care of sharp objects", "Proper disposal of waste."],
     ["غسل اليدين", "القفّازات", "الكمّامة", "النظّارات الواقية", "المآزر أو الأردية", "الحذر من الأدوات الحادة", "التخلّص السليم من النفايات."], en="**Measure:**", ar="**الإجراءات:**")],
     figure=dict(src="assets/universal-precautions.jpg", en="Universal precautionary measures in laboratory", ar="إجراءات الاحتياطات العامة في المختبر")),

   SEC("Needle stick injury", "إصابة وخز الإبرة"),
   C("The most important pathogens that can be transmitted through needlestick injury are :", "أهم الممرضات التي يمكن أن تنتقل بإصابة وخز الإبرة:",
     list_en=["Hepatitis B virus", "Hepatitis C virus", "HIV"], list_ar=["فيروس التهاب الكبد `B`", "فيروس التهاب الكبد `C`", "فيروس `HIV`"]),
   dict(t="side", blocks=[L(["Immediately **report** to your employer", "**Rinse** the area with running water for **15 minutes**.",
     "Gently **squeeze the wound** to encourage it to bleed (ideally while holding it under running water)", "Take appropriate **post-exposure prophylaxis** if available."],
     ["**أبلغ** صاحب العمل فورًا", "**اغسل** المنطقة بماء جارٍ لمدة **15 دقيقة**.", "**اعصر الجرح** بلطف لتشجيع نزفه (ويُفضّل أثناء وضعه تحت الماء الجاري)", "خذ **الوقاية الدوائية بعد التعرّض** المناسبة إن توفّرت."],
     en="**What to do in case of needle prick?**", ar="**ماذا تفعل عند وخز الإبرة؟**")],
     figure=dict(src="assets/needle-stick.jpg", en="Needle stick injury", ar="إصابة وخز الإبرة")),
   T(["", "Standard first-aid treatment", "الإسعاف الأولي القياسي"],
     [["Eye contact", "Rinse immediately with plenty of water for at least 15 minutes. Obtain medical attention.", "**تماس العين**: اغسلها فورًا بكمية وفيرة من الماء 15 دقيقة على الأقل، واطلب الرعاية الطبية."],
      ["Skin contact", "Remove any contaminated clothing. Wash off immediately with plenty of water for at least 15 minutes. Obtain medical attention.", "**تماس الجلد**: انزع الملابس الملوّثة، واغسل فورًا بكمية وفيرة من الماء 15 دقيقة على الأقل، واطلب الرعاية الطبية."],
      ["Inhalation", "Move to fresh air. If breathing is difficult, give oxygen. If not breathing, give artificial respiration. Obtain medical attention.", "**الاستنشاق**: انتقل إلى هواء نقي؛ وإذا صعب التنفّس أعطِ أوكسجين، وإذا توقّف أعطِ تنفّسًا صناعيًا، واطلب الرعاية الطبية."],
      ["Ingestion", "Do not induce vomiting. Obtain medical attention.", "**البلع**: لا تُحفّز التقيّؤ، واطلب الرعاية الطبية."]],
     ar_cols=[2], key_cols=[0], style="summary", label_en="Table 2.5 Standard first-aid treatment", label_ar="جدول 2.5 الإسعاف الأولي القياسي"),

   SEC("Proper disposal of laboratory Waste", "التخلّص السليم من نفايات المختبر"),
   L(["Store waste only in a **closed container** with no chance of puncture in case of sharp material.",
      "**Do not keep incompatible chemicals in a same container** such as **acid and alkali** should not be kept together."],
     ["خزّن النفايات في **وعاء مغلق** فقط لا يمكن ثقبه في حالة المواد الحادة.",
      "**لا تحفظ المواد الكيميائية غير المتوافقة في الوعاء نفسه**، فمثلًا **الحامض والقاعدة** لا يُحفظان معًا."],
     en="**Basic rules to Dispose the Waste Material are:**", ar="**القواعد الأساسية للتخلّص من النفايات:**"),
   T(["Colour", "Waste", "اللون — النفايات"],
     [["Red", "Infectious / contaminated waste", "**الأحمر**: النفايات المعدية / الملوّثة"], ["Yellow", "Biohazardous waste", "**الأصفر**: النفايات الخطرة حيويًا"],
      ["Purple", "Cytotoxic waste", "**البنفسجي**: النفايات السامّة للخلايا"], ["Black", "General waste", "**الأسود**: النفايات العامة"],
      ["Blue", "Glass waste", "**الأزرق**: نفايات الزجاج"], ["Brown", "Chemical waste", "**البنّي**: النفايات الكيميائية"]],
     ar_cols=[2], key_cols=[0], style="summary", label_en="Waste Color Coding", label_ar="ترميز النفايات بالألوان"),
   F("waste-disposal.jpg", "Waste disposal in healthcare laboratory — colour-coded bins", "التخلّص من النفايات في المختبر الصحي — حاويات بألوان مختلفة", h="56mm"),

   SEC("Histopathology lab equipment", "أجهزة مختبر الأنسجة"),
   FF(("embedding-station.jpg", "Embedding Station", "محطة الطمر", "50mm"), ("microtome.jpg", "Microtome", "المِقطاع (الميكروتوم)", "50mm")),
   FF(("water-bath.jpg", "Water bath", "الحمّام المائي", "44mm"), ("staining-racks.jpg", "Microscopic Slide staining Racks", "حوامل تصبيغ الشرائح المجهرية", "44mm")),
   FF(("staining-jars.jpg", "Slide Staining Dishes/ Jars", "أحواض / جِرار تصبيغ الشرائح", "44mm"), ("automated-stainer.jpg", "Automated slide stainer", "جهاز التصبيغ الآلي للشرائح", "44mm")),
   FF(("microscope.jpg", "Microscope", "المجهر", "48mm"), ("microwave.jpg", "Microwave", "المايكروويف", "48mm")),
   FF(("slide-storage.jpg", "Storage for Stained Slides", "خزانة حفظ الشرائح المصبوغة", "46mm"), ("slide-storage-2.jpg", "Storage for Stained Slides", "خزانة حفظ الشرائح المصبوغة", "46mm")),
  ]

  mcq = [
   {"topic_en": "Definitions", "topic_ar": "التعريفات"},
   Q("“Histo” means:", "كلمة “Histo” تعني:", [("Cell", "الخلية"), ("Tissue", "النسيج"), ("Disease", "المرض"), ("Organ", "العضو")], "b"),
   Q("Histology is the study of:", "علم الأنسجة هو دراسة:", [("Diseased tissue", "النسيج المريض"), ("Anatomy of normal cell or tissue", "تشريح الخلية أو النسيج الطبيعي"), ("Microbes", "الأحياء المجهرية"), ("Blood only", "الدم فقط")], "b"),
   Q("Histopathology is the study of:", "علم الأمراض النسيجية هو دراسة:", [("Diseased tissue at microscopic level", "النسيج المريض على المستوى المجهري"), ("Normal tissue", "النسيج الطبيعي"), ("Body fluids", "سوائل الجسم"), ("Genes", "الجينات")], "a"),
   Q("Processing of tissue to enable its satisfactory study is called:", "معالجة النسيج بطريقة تتيح دراسته دراسة مُرضية تُسمّى:", [("Histology", "علم الأنسجة"), ("Cytology", "علم الخلايا"), ("Histotechniques", "التقنيات النسيجية"), ("Immunology", "علم المناعة")], "c"),
   Q("Detecting tumour markers on tissue is done in which section?", "يُكشف عن الواسمات الورمية على النسيج في أي قسم؟", [("Haematology", "أمراض الدم"), ("Microbiology", "الأحياء المجهرية"), ("Blood bank", "مصرف الدم"), ("Immunohistochemistry", "الكيمياء النسيجية المناعية")], "d"),
   {"topic_en": "Management, chemicals and hazards", "topic_ar": "الإدارة والمواد والمخاطر"},
   Q("Which is NOT one of the chemicals & reagents of the histopathology lab?", "أي مما يأتي ليس من مواد وكواشف مختبر الأنسجة؟", [("Fixative", "المثبّت"), ("Clearing agents", "عوامل الترويق"), ("Antibiotic discs", "أقراص المضادات الحيوية"), ("Mounting medium", "وسط التحميل")], "c"),
   Q("Which is part of good laboratory construction?", "أي مما يأتي من البناء الجيد للمختبر؟", [("Poor lighting", "إضاءة ضعيفة"), ("Good ventilation", "تهوية جيدة"), ("No emergency exits", "بلا مخارج طوارئ"), ("Closed windows only", "نوافذ مغلقة فقط")], "b"),
   Q("Burns and injury by sharp instruments are:", "الحروق والإصابة بالأدوات الحادة:", [("Physical hazards", "مخاطر فيزيائية"), ("Biological hazards", "مخاطر حيوية"), ("Chemical hazards", "مخاطر كيميائية"), ("Not hazards", "ليست مخاطر")], "a"),
   Q("HBV, HCV, HIV and TB represent:", "تمثّل HBV وHCV وHIV والتدرّن:", [("Chemical hazard", "خطرًا كيميائيًا"), ("Physical hazard", "خطرًا فيزيائيًا"), ("Electrical hazard", "خطرًا كهربائيًا"), ("Biological or infectious hazard", "خطرًا حيويًا أو معديًا")], "d"),
   {"topic_en": "Universal precautions and needle stick", "topic_ar": "الاحتياطات العامة ووخز الإبرة"},
   Q("Universal precautions mainly prevent transmission of:", "تمنع الاحتياطات العامة أساسًا انتقال:", [("Influenza", "الإنفلونزا"), ("Hepatitis B, hepatitis C and HIV", "التهاب الكبد B وC وHIV"), ("Malaria", "الملاريا"), ("Food poisoning", "التسمّم الغذائي")], "b"),
   Q("Which body fluid is NOT listed as needing universal precautions?", "أي سائل لم يُذكر ضمن ما يحتاج احتياطات عامة؟", [("CSF", "السائل الدماغي الشوكي"), ("Pleural fluid", "السائل الجنبي"), ("Semen", "السائل المنوي"), ("Tears", "الدموع")], "d"),
   Q("All are measures of universal precautions EXCEPT:", "كل مما يأتي من إجراءات الاحتياطات العامة عدا:", [("Hand wash", "غسل اليدين"), ("Goggles", "النظّارات الواقية"), ("Recapping needles by hand", "إعادة غطاء الإبرة باليد"), ("Proper disposal of waste", "التخلّص السليم من النفايات")], "c"),
   Q("After a needle prick, rinse the area with running water for:", "بعد وخز الإبرة اغسل المنطقة بماء جارٍ لمدة:", [("1 minute", "دقيقة"), ("5 minutes", "5 دقائق"), ("15 minutes", "15 دقيقة"), ("1 hour", "ساعة")], "c"),
   Q("After a needle prick, the wound should be:", "بعد وخز الإبرة يجب أن يكون الجرح:", [("Gently squeezed to encourage bleeding", "معصورًا بلطف لتشجيع النزف"), ("Sucked by mouth", "ممصوصًا بالفم"), ("Covered without washing", "مغطّى دون غسل"), ("Burned with alcohol flame", "محروقًا بلهب الكحول")], "a"),
   Q("The first step after a needle prick is to:", "الخطوة الأولى بعد وخز الإبرة:", [("Go home", "الذهاب إلى البيت"), ("Immediately report to your employer", "الإبلاغ الفوري لصاحب العمل"), ("Wait for symptoms", "انتظار الأعراض"), ("Ignore it", "تجاهله")], "b"),
   Q("For ingestion of a chemical, first aid is:", "الإسعاف الأولي لبلع مادة كيميائية:", [("Induce vomiting", "تحفيز التقيّؤ"), ("Give oxygen", "إعطاء الأوكسجين"), ("Do not induce vomiting; obtain medical attention", "عدم تحفيز التقيّؤ وطلب الرعاية الطبية"), ("Wash the skin", "غسل الجلد")], "c"),
   Q("For inhalation of a chemical, the first step is to:", "عند استنشاق مادة كيميائية الخطوة الأولى:", [("Move to fresh air", "الانتقال إلى هواء نقي"), ("Drink water", "شرب الماء"), ("Induce vomiting", "تحفيز التقيّؤ"), ("Remove clothing only", "نزع الملابس فقط")], "a"),
   {"topic_en": "Waste", "topic_ar": "النفايات"},
   Q("Acid and alkali waste should be:", "يجب أن تكون نفايات الحامض والقاعدة:", [("Kept in the same container", "في الوعاء نفسه"), ("Kept in separate containers", "في وعاءين منفصلين"), ("Poured in the sink together", "مسكوبة معًا في المغسلة"), ("Burned", "محروقة")], "b"),
   Q("Cytotoxic waste is placed in the colour:", "تُوضع النفايات السامّة للخلايا في اللون:", [("Black", "الأسود"), ("Blue", "الأزرق"), ("Brown", "البنّي"), ("Purple", "البنفسجي")], "d"),
   Q("Glass waste is placed in the colour:", "تُوضع نفايات الزجاج في اللون:", [("Blue", "الأزرق"), ("Red", "الأحمر"), ("Yellow", "الأصفر"), ("Black", "الأسود")], "a"),
   Q("Chemical waste is placed in the colour:", "تُوضع النفايات الكيميائية في اللون:", [("Purple", "البنفسجي"), ("Brown", "البنّي"), ("Black", "الأسود"), ("Blue", "الأزرق")], "b"),
   Q("General waste is placed in the colour:", "تُوضع النفايات العامة في اللون:", [("Yellow", "الأصفر"), ("Red", "الأحمر"), ("Black", "الأسود"), ("Purple", "البنفسجي")], "c"),
   {"topic_en": "Picture questions", "topic_ar": "أسئلة الصور"},
   Q("The instrument shown is used to cut thin tissue sections. It is the:", "الجهاز في الشكل يُستخدم لقطع مقاطع نسيجية رقيقة. هو:", [("Water bath", "الحمّام المائي"), ("Microtome", "المِقطاع (الميكروتوم)"), ("Microwave", "المايكروويف"), ("Embedding station", "محطة الطمر")], "b", img="assets/q-microtome.jpg", img_h="36mm"),
   Q("Identify the instrument shown:", "تعرّف على الجهاز في الشكل:", [("Automated slide stainer", "جهاز التصبيغ الآلي"), ("Microtome", "المِقطاع"), ("Water bath", "الحمّام المائي"), ("Microscope", "المجهر")], "c", img="assets/q-water-bath.jpg", img_h="32mm"),
   Q("Identify the equipment shown:", "تعرّف على الجهاز في الشكل:", [("Embedding station", "محطة الطمر"), ("Microwave", "المايكروويف"), ("Slide storage", "خزانة الشرائح"), ("Microtome", "المِقطاع")], "a", img="assets/q-embedding-station.jpg", img_h="36mm"),
   Q("The sign in this figure warns of a:", "تحذّر العلامة في هذا الشكل من:", [("Chemical hazard", "خطر كيميائي"), ("Electrical hazard", "خطر كهربائي"), ("Fire hazard", "خطر حريق"), ("Biohazard", "خطر حيوي")], "d", img="assets/biohazard.jpg", img_h="36mm"),
   Q("According to the sign, formaldehyde is:", "بحسب العلامة، الفورمالديهايد:", [("Safe for everyone", "آمن للجميع"), ("Irritant and potential cancer hazard", "مهيّج وخطر سرطاني محتمل"), ("Radioactive", "مشعّ"), ("A biohazard", "خطر حيوي")], "b", img="assets/danger-formaldehyde.jpg", img_h="30mm"),
  ]
  tf = [
   TF("Histopathology studies diseased tissue at the microscopic level.", "يدرس علم الأمراض النسيجية النسيج المريض على المستوى المجهري.", "T"),
   TF("Histology is the study of diseased tissue.", "علم الأنسجة دراسة النسيج المريض.", "F"),
   TF("Histopathologists help clinicians manage a patient's care.", "يساعد أخصائيو الأمراض النسيجية الأطباء في إدارة رعاية المريض.", "T"),
   TF("The histopathology lab studies only malignant tissue.", "يدرس مختبر الأنسجة النسيج الخبيث فقط.", "F"),
   TF("Decalcifying agents are among the chemicals of the histopathology lab.", "عوامل إزالة الكلس من مواد مختبر الأنسجة.", "T"),
   TF("Electrical injury is a chemical hazard.", "الصدمة الكهربائية خطر كيميائي.", "F"),
   TF("Synovial effusion needs universal precautions.", "يحتاج الانصباب الزليلي إلى الاحتياطات العامة.", "T"),
   TF("After a needle prick, the area should be rinsed with running water for 15 minutes.", "بعد وخز الإبرة تُغسل المنطقة بماء جارٍ 15 دقيقة.", "T"),
   TF("Post-exposure prophylaxis should be taken if available.", "يجب أخذ الوقاية بعد التعرّض إن توفّرت.", "T"),
   TF("For eye contact with a chemical, rinse for at least 1 minute.", "عند تماس العين مع مادة كيميائية تُغسل دقيقة واحدة على الأقل.", "F"),
   TF("Yellow bins are for biohazardous waste.", "الحاويات الصفراء للنفايات الخطرة حيويًا.", "T"),
   TF("Red bins are for glass waste.", "الحاويات الحمراء لنفايات الزجاج.", "F"),
  ]
  traps = [
   TR("Histology vs histopathology vs histotechniques", "علم الأنسجة مقابل الأمراض النسيجية مقابل التقنيات النسيجية", "Histology: normal cell/tissue. Histopathology: diseased tissue at microscopic level. Histotechniques: processing tissue for satisfactory study.", "علم الأنسجة: الخلية/النسيج الطبيعي. الأمراض النسيجية: النسيج المريض مجهريًا. التقنيات النسيجية: معالجة النسيج لدراسته."),
   TR("Which hazard type?", "أي نوع من المخاطر؟", "Biological: HBV, HCV, HIV, TB. Physical: burns, sharps, electrical injury. Chemical: chemicals such as formaldehyde.", "حيوي: HBV، HCV، HIV، التدرّن. فيزيائي: الحروق، الأدوات الحادة، الكهرباء. كيميائي: المواد مثل الفورمالديهايد."),
   TR("Red vs yellow bins", "الحاوية الحمراء مقابل الصفراء", "Red: infectious/contaminated waste. Yellow: biohazardous waste.", "الحمراء: النفايات المعدية/الملوّثة. الصفراء: النفايات الخطرة حيويًا."),
   TR("Purple vs brown bins", "الحاوية البنفسجية مقابل البنّية", "Purple: cytotoxic waste. Brown: chemical waste.", "البنفسجية: النفايات السامّة للخلايا. البنّية: النفايات الكيميائية."),
   TR("Ingestion first aid", "الإسعاف عند البلع", "Do NOT induce vomiting; obtain medical attention.", "لا تُحفّز التقيّؤ؛ اطلب الرعاية الطبية."),
   TR("Squeeze or not after a needle prick?", "تعصر أم لا بعد وخز الإبرة؟", "Gently squeeze to encourage bleeding, ideally under running water, after reporting and rinsing for 15 minutes.", "اعصر بلطف لتشجيع النزف، ويُفضّل تحت الماء الجاري، بعد الإبلاغ والغسل 15 دقيقة."),
  ]
  important = [
   IM("Define histology, histopathology and histotechniques.", "عرّف علم الأنسجة والأمراض النسيجية والتقنيات النسيجية.", "Histology: study of anatomy of normal cell or tissue. Histopathology: study of diseased tissue at microscopic level. Histotechniques: processing tissue so it can be studied satisfactorily.", "علم الأنسجة: دراسة تشريح الخلية أو النسيج الطبيعي. الأمراض النسيجية: دراسة النسيج المريض مجهريًا. التقنيات النسيجية: معالجة النسيج لتمكين دراسته."),
   IM("What is studied in the histopathology laboratory?", "ماذا يُدرس في مختبر الأمراض النسيجية؟", "Histopathological diagnosis (malignant or benign condition of tissue), morphology of tissues, and in immunohistochemistry the presence of specific antigens or molecules such as tumour markers to identify cancer types.", "التشخيص النسيجي المرضي (الحالة الخبيثة أو الحميدة)، وشكل الأنسجة، وفي الكيمياء النسيجية المناعية وجود مستضدات أو جزيئات معيّنة كالواسمات الورمية لتحديد أنواع السرطان."),
   IM("List the hazards of the histopathology department.", "عدّد مخاطر قسم الأمراض النسيجية.", "Biological/infectious (HBV, HCV, HIV, TB); physical (burns, sharp instruments, electrical injury); chemical.", "حيوية/معدية (HBV، HCV، HIV، التدرّن)؛ فيزيائية (الحروق، الأدوات الحادة، الكهرباء)؛ كيميائية."),
   IM("What are universal precautions and their measures?", "ما الاحتياطات العامة وما إجراءاتها؟", "Precautions to prevent transmission of HBV, HCV and HIV from blood, peritoneal/pleural fluid, CSF, semen, vaginal secretions, synovial effusion and faeces. Measures: hand wash, gloves, mask, goggles, aprons/gowns, care with sharps, proper waste disposal.", "احتياطات لمنع انتقال HBV وHCV وHIV من الدم والسوائل البريتونية/الجنبية والدماغي الشوكي والمني والإفرازات المهبلية والزليلي والبراز. الإجراءات: غسل اليدين، القفّازات، الكمّامة، النظّارات، المآزر، الحذر من الأدوات الحادة، التخلّص السليم من النفايات."),
   IM("What should be done in case of a needle prick?", "ماذا يجب فعله عند وخز الإبرة؟", "Report immediately; rinse under running water for 15 minutes; gently squeeze to encourage bleeding; take post-exposure prophylaxis if available.", "الإبلاغ فورًا؛ الغسل بماء جارٍ 15 دقيقة؛ العصر بلطف لتشجيع النزف؛ أخذ الوقاية بعد التعرّض إن توفّرت."),
   IM("Give the rules and colour coding of laboratory waste disposal.", "اذكر قواعد التخلّص من نفايات المختبر وترميزها اللوني.", "Store waste in closed puncture-proof containers; don't keep incompatible chemicals (acid and alkali) together. Red infectious, yellow biohazardous, purple cytotoxic, black general, blue glass, brown chemical.", "خزن النفايات في أوعية مغلقة لا تُثقب؛ وعدم جمع المواد غير المتوافقة (حامض وقاعدة). الأحمر معدية، الأصفر خطرة حيويًا، البنفسجي سامّة للخلايا، الأسود عامة، الأزرق زجاج، البنّي كيميائية."),
  ]
  save("histopathology-lab1-lab-safety", 1, "Laboratory management & Chemical safety in the lab", "إدارة المختبر والسلامة الكيميائية فيه", blocks, mcq, tf, traps, important)

```
