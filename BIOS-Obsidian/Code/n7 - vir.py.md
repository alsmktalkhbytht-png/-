---
source: BIOS-Obsidian/tools/scripts/n7/vir.py
handouts: [virology-lab1-safety]
saved: 2026-10-29
tags: [bios, code]
---
# n7/vir.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#virology-lab1-safety|virology-lab1-safety]]

```python
from c import *

blocks = [
 SEC("Laboratory Safety Guidelines", "إرشادات السلامة في المختبر"),
 R("**Personal Protective Equipment:** Wear lab coat, gloves, lab coats.", "**معدّات الوقاية الشخصية:** ارتدِ صدرية المختبر والقفّازات."),
 R(["**Safe Handling of Pathogens:** Handle infectious agents within a **biological safety cabinet (Hood)** to contain aerosols and splashes.",
    "Use **sealed tubes and secondary containment** when transporting specimens."],
   ["**التعامل الآمن مع الممرضات:** تعامل مع العوامل المعدية داخل **كابينة السلامة الحيوية (الهود)** لاحتواء الرذاذ والتناثر.",
    "واستخدم **أنابيب محكمة الغلق مع حاوية ثانوية** عند نقل العيّنات."]),
 R(["**Waste Management:** Decontaminate biohazard waste using **autoclaves or chemical disinfectants** before disposal.",
    "Follow regulations for disposal of sharps and infectious materials."],
   ["**إدارة النفايات:** أزِل تلوّث النفايات الخطرة حيويًا باستخدام **المؤصدة (الأوتوكليف) أو المطهّرات الكيميائية** قبل التخلّص منها.",
    "واتّبع الأنظمة الخاصة بالتخلّص من الأدوات الحادة والمواد المعدية."]),

 SEC("Aseptic Techniques", "التقنيات المعقّمة (اللاتلوّثية)"),
 C("Aseptic techniques **minimize contamination risk** and **ensure sample integrity** during virological work.",
   "تقلّل التقنيات المعقّمة **خطر التلوّث** و**تضمن سلامة العيّنة** أثناء العمل الفيروسي."),
 R(["**Workstation Preparation:** Disinfect the work area with an appropriate agent (e.g., **70% ethanol or sodium hypochlorite**).",
    "Organize tools and materials to minimize unnecessary movement."],
   ["**تهيئة مكان العمل:** طهّر منطقة العمل بمادة مناسبة (مثل **الإيثانول 70% أو هايبوكلورايت الصوديوم**).",
    "ونظّم الأدوات والمواد لتقليل الحركة غير الضرورية."]),
 R(["**Specimen Collection and Handling:** Use **sterile equipment** for specimen collection.",
    "**Avoid touching sterile surfaces with bare hands** or non-sterile objects."],
   ["**جمع العيّنات والتعامل معها:** استخدم **أدوات معقّمة** لجمع العيّنات.",
    "و**تجنّب لمس الأسطح المعقّمة باليد المجرّدة** أو بأدوات غير معقّمة."]),
 R(["**Hand Hygiene:** Wash hands thoroughly **before and after** procedures.", "Use **alcohol-based hand sanitizers** as an additional measure."],
   ["**نظافة اليدين:** اغسل يديك جيدًا **قبل الإجراءات وبعدها**.", "واستخدم **معقّمات اليدين الكحولية** إجراءً إضافيًا."]),
 R(["**Use of Sterile Supplies:** Employ **single-use sterile** pipette tips, tubes, and culture plates.", "Open sterile packaging carefully to maintain sterility."],
   ["**استخدام المستلزمات المعقّمة:** استخدم رؤوس ماصّات وأنابيب وأطباق زرع **معقّمة ذات استعمال واحد**.", "وافتح العبوات المعقّمة بحذر للمحافظة على تعقيمها."]),
 R(["**Minimizing Aerosols:** Perform procedures **gently** to avoid splashing or aerosol generation.", "Centrifuge samples in **sealed containers** with appropriate rotors."],
   ["**تقليل الرذاذ:** نفّذ الإجراءات **بلطف** لتجنّب التناثر أو توليد الرذاذ.", "وضع العيّنات في جهاز الطرد المركزي داخل **حاويات محكمة الغلق** مع دوّارات مناسبة."]),
 R(["**Flame Sterilization:** Sterilize reusable instruments (e.g., **inoculation loops**) using a **Bunsen burner** or a sterilizer.", "**Avoid reaching over the flame** to prevent contamination."],
   ["**التعقيم باللهب:** عقّم الأدوات القابلة لإعادة الاستعمال (مثل **عروة التلقيح**) باستخدام **مصباح بنزن** أو جهاز تعقيم.", "و**تجنّب مدّ اليد فوق اللهب** لمنع التلوّث."]),
 R("**Environmental Monitoring:** Regularly test the work environment for contamination using **swabs and microbial culture** techniques.",
   "**مراقبة البيئة:** افحص بيئة العمل بانتظام بحثًا عن التلوّث باستخدام **المسحات وتقنيات الزرع الميكروبي**."),
 T(["Situation", "Use", "الحالة — الاستخدام"],
   [["Infectious agents", "Biological safety cabinet (Hood)", "**العوامل المعدية**: كابينة السلامة الحيوية"],
    ["Transport", "Sealed tubes + secondary containment", "**النقل**: أنابيب محكمة + حاوية ثانوية"],
    ["Biohazard waste", "Autoclave or chemical disinfectants", "**النفايات الخطرة حيويًا**: المؤصدة أو المطهّرات"],
    ["Work area", "70% ethanol or sodium hypochlorite", "**منطقة العمل**: إيثانول 70% أو هايبوكلورايت الصوديوم"],
    ["Centrifugation", "Sealed containers, appropriate rotors", "**الطرد المركزي**: حاويات محكمة ودوّارات مناسبة"],
    ["Inoculation loops", "Bunsen burner or sterilizer", "**عروة التلقيح**: مصباح بنزن أو جهاز تعقيم"]],
   ar_cols=[2], key_cols=[0], style="summary", label_en="At a glance", label_ar="باختصار"),
]

P = lambda *o: [(x, y) for x, y in o]
mcq = [
 {"topic_en": "Lecturer's MCQs (Medical Virology Lab One)", "topic_ar": "أسئلة المحاضرة (من ملف التدريسي)"},
 Q("What is the main purpose of aseptic techniques in virology laboratory work:", "ما الغرض الرئيس من التقنيات المعقّمة في العمل المختبري الفيروسي:",
   P(("Increase viral growth", "زيادة نمو الفيروس"), ("Minimize contamination risk and ensure sample integrity", "تقليل خطر التلوّث وضمان سلامة العيّنة"), ("Increase aerosol production", "زيادة إنتاج الرذاذ"), ("Destroy laboratory equipment", "إتلاف الأدوات المختبرية"), ("Increase specimen volume", "زيادة حجم العيّنة")), "b"),
 Q("Infectious agents should be handled within a:", "يجب التعامل مع العوامل المعدية داخل:",
   P(("Centrifuge", "جهاز الطرد المركزي"), ("Water bath", "الحمّام المائي"), ("Biological safety cabinet", "كابينة السلامة الحيوية"), ("Refrigerator", "الثلاجة"), ("Incubator", "الحاضنة")), "c"),
 Q("When transporting specimens, which should be used:", "عند نقل العيّنات يجب استخدام:",
   P(("Open tubes", "أنابيب مفتوحة"), ("Sealed tubes and secondary containment", "أنابيب محكمة مع حاوية ثانوية"), ("Paper bags", "أكياس ورقية"), ("Open Petri dishes", "أطباق بتري مفتوحة"), ("Uncovered containers", "حاويات مكشوفة")), "b"),
 Q("Which agent can be used to disinfect the laboratory work area:", "أي مادة يمكن استخدامها لتطهير منطقة العمل:",
   P(("Normal saline", "المحلول الملحي"), ("Distilled water", "الماء المقطّر"), ("70% ethanol", "إيثانول 70%"), ("Culture medium", "الوسط الزرعي"), ("Glucose solution", "محلول الكلوكوز")), "c"),
 Q("Specimens should be collected using:", "يجب جمع العيّنات باستخدام:",
   P(("Contaminated equipment", "أدوات ملوّثة"), ("Bare hands", "اليد المجرّدة"), ("Sterile equipment", "أدوات معقّمة"), ("Used pipettes", "ماصّات مستعملة"), ("Non-sterile tubes", "أنابيب غير معقّمة")), "c"),
 Q("Which practice should be avoided during aseptic procedures:", "أي ممارسة يجب تجنّبها أثناء الإجراءات المعقّمة:",
   P(("Touching sterile surfaces with bare hands", "لمس الأسطح المعقّمة باليد المجرّدة"), ("Washing hands", "غسل اليدين"), ("Using sterile equipment", "استخدام الأدوات المعقّمة"), ("Using sterile pipette tips", "استخدام رؤوس ماصّات معقّمة"), ("Disinfecting the work area", "تطهير منطقة العمل")), "a"),
 Q("Samples should be centrifuged in:", "يجب وضع العيّنات في الطرد المركزي داخل:",
   P(("Open containers", "حاويات مفتوحة"), ("Sealed containers with appropriate rotors", "حاويات محكمة مع دوّارات مناسبة"), ("Paper containers", "حاويات ورقية"), ("Open Petri dishes", "أطباق بتري مفتوحة"), ("Uncovered tubes", "أنابيب مكشوفة")), "b"),
 Q("Biohazard waste should be decontaminated using:", "يجب إزالة تلوّث النفايات الخطرة حيويًا باستخدام:",
   P(("Distilled water", "الماء المقطّر"), ("Culture media", "الأوساط الزرعية"), ("Normal saline", "المحلول الملحي"), ("Autoclaves or chemical disinfectants", "المؤصدة أو المطهّرات الكيميائية"), ("Refrigeration", "التبريد")), "d"),
 Q("Which of the following is used as a sterile, single-use laboratory supply:", "أي مما يأتي يُستخدم مستلزمًا معقّمًا ذا استعمال واحد:",
   P(("Pipette tips", "رؤوس الماصّات"), ("Bunsen burner", "مصباح بنزن"), ("Microscope", "المجهر"), ("Centrifuge", "جهاز الطرد المركزي"), ("Incubator", "الحاضنة")), "a"),
 Q("Laboratory procedures should be performed gently to:", "يجب تنفيذ الإجراءات المختبرية بلطف من أجل:",
   P(("Increase splashing", "زيادة التناثر"), ("Generate aerosols", "توليد الرذاذ"), ("Avoid splashing and aerosol generation", "تجنّب التناثر وتوليد الرذاذ"), ("Increase contamination", "زيادة التلوّث"), ("Increase specimen evaporation", "زيادة تبخّر العيّنة")), "c"),
 {"topic_en": "More practice", "topic_ar": "تدريب إضافي"},
 Q("Besides 70% ethanol, the work area can be disinfected with:", "إضافة إلى إيثانول 70% يمكن تطهير منطقة العمل بـ:", P(("Sodium hypochlorite", "هايبوكلورايت الصوديوم"), ("Glucose", "الكلوكوز"), ("Saline", "المحلول الملحي"), ("Distilled water", "الماء المقطّر")), "a"),
 Q("Reusable inoculation loops are sterilized by:", "تُعقَّم عروة التلقيح القابلة لإعادة الاستعمال بـ:", P(("Washing with water", "الغسل بالماء"), ("A Bunsen burner or a sterilizer", "مصباح بنزن أو جهاز تعقيم"), ("Refrigeration", "التبريد"), ("Saline", "المحلول الملحي")), "b"),
 Q("During flame sterilization you should avoid:", "أثناء التعقيم باللهب يجب تجنّب:", P(("Using a Bunsen burner", "استخدام مصباح بنزن"), ("Sterilizing loops", "تعقيم العروات"), ("Reaching over the flame", "مدّ اليد فوق اللهب"), ("Wearing gloves", "ارتداء القفّازات")), "c"),
 Q("The work environment is tested for contamination using:", "تُفحص بيئة العمل بحثًا عن التلوّث باستخدام:", P(("Thermometers", "محارير"), ("pH paper", "ورق الأس الهيدروجيني"), ("Microscopes only", "المجاهر فقط"), ("Swabs and microbial culture", "المسحات والزرع الميكروبي")), "d"),
 Q("Hands should be washed:", "يجب غسل اليدين:", P(("Before and after procedures", "قبل الإجراءات وبعدها"), ("Only after work", "بعد العمل فقط"), ("Only before work", "قبل العمل فقط"), ("Never", "أبدًا")), "a"),
 Q("Organizing tools and materials on the workstation aims to:", "يهدف تنظيم الأدوات والمواد في مكان العمل إلى:", P(("Increase contamination", "زيادة التلوّث"), ("Minimize unnecessary movement", "تقليل الحركة غير الضرورية"), ("Speed up aerosols", "تسريع الرذاذ"), ("Avoid disinfection", "تجنّب التطهير")), "b"),
 Q("Sterile packaging should be:", "يجب أن تُفتح العبوات المعقّمة:", P(("Torn open quickly", "بسرعة وتمزيق"), ("Opened with bare teeth", "بالأسنان"), ("Opened carefully to maintain sterility", "بحذر للمحافظة على التعقيم"), ("Left open overnight", "وتُترك مفتوحة طوال الليل")), "c"),
]
tf = [
 TF("Infectious agents should be handled on an open bench.", "يُتعامل مع العوامل المعدية على منضدة مفتوحة.", "F"),
 TF("A biological safety cabinet contains aerosols and splashes.", "تحتوي كابينة السلامة الحيوية الرذاذ والتناثر.", "T"),
 TF("Biohazard waste can be thrown away without decontamination.", "يمكن رمي النفايات الخطرة حيويًا دون إزالة تلوّثها.", "F"),
 TF("Aseptic techniques ensure sample integrity.", "تضمن التقنيات المعقّمة سلامة العيّنة.", "T"),
 TF("Alcohol-based hand sanitizers replace hand washing.", "تحلّ معقّمات اليدين الكحولية محلّ غسل اليدين.", "F"),
 TF("Pipette tips, tubes and culture plates should be single-use and sterile.", "يجب أن تكون رؤوس الماصّات والأنابيب وأطباق الزرع معقّمة وذات استعمال واحد.", "T"),
 TF("Samples may be centrifuged in open tubes.", "يمكن وضع العيّنات في الطرد المركزي بأنابيب مفتوحة.", "F"),
 TF("Reaching over the flame may cause contamination.", "قد يسبّب مدّ اليد فوق اللهب التلوّث.", "T"),
 TF("Environmental monitoring is done regularly.", "تُجرى مراقبة البيئة بانتظام.", "T"),
 TF("Sodium hypochlorite is used to disinfect the work area.", "يُستخدم هايبوكلورايت الصوديوم لتطهير منطقة العمل.", "T"),
]
traps = [
 TR("Where are infectious agents handled?", "أين يُتعامل مع العوامل المعدية؟", "Inside a biological safety cabinet (hood) — not a centrifuge, incubator or open bench.", "داخل كابينة السلامة الحيوية (الهود) — لا الطرد المركزي ولا الحاضنة ولا المنضدة المفتوحة."),
 TR("Disinfectant vs diluent", "المطهّر مقابل المخفّف", "70% ethanol or sodium hypochlorite disinfect; saline and distilled water do not.", "الإيثانول 70% وهايبوكلورايت الصوديوم يطهّران؛ أما المحلول الملحي والماء المقطّر فلا."),
 TR("Single-use supply or equipment?", "مستلزم ذو استعمال واحد أم جهاز؟", "Pipette tips, tubes, culture plates are single-use; Bunsen burner, microscope, centrifuge, incubator are equipment.", "رؤوس الماصّات والأنابيب وأطباق الزرع ذات استعمال واحد؛ ومصباح بنزن والمجهر والطرد المركزي والحاضنة أجهزة."),
 TR("Hand sanitizer — main or additional?", "معقّم اليدين — رئيس أم إضافي؟", "Additional measure; hands are washed thoroughly before and after procedures.", "إجراء إضافي؛ وتُغسل اليدان جيدًا قبل الإجراءات وبعدها."),
 TR("How is biohazard waste decontaminated?", "كيف تُزال تلوّث النفايات الخطرة حيويًا؟", "Autoclave or chemical disinfectants before disposal.", "بالمؤصدة أو المطهّرات الكيميائية قبل التخلّص منها."),
]
important = [
 IM("List the laboratory safety guidelines in virology.", "عدّد إرشادات السلامة في مختبر الفيروسات.", "PPE (lab coat, gloves); handle pathogens in a biological safety cabinet and transport them in sealed tubes with secondary containment; decontaminate biohazard waste by autoclave or chemicals and follow sharps regulations.", "معدّات الوقاية (صدرية، قفّازات)؛ التعامل مع الممرضات في كابينة السلامة الحيوية ونقلها بأنابيب محكمة وحاوية ثانوية؛ إزالة تلوّث النفايات بالمؤصدة أو الكيميائيات واتّباع أنظمة الأدوات الحادة."),
 IM("Define aseptic techniques and list them.", "عرّف التقنيات المعقّمة وعدّدها.", "Techniques that minimize contamination risk and ensure sample integrity: workstation preparation, specimen collection and handling, hand hygiene, sterile supplies, minimizing aerosols, flame sterilization, environmental monitoring.", "تقنيات تقلّل خطر التلوّث وتضمن سلامة العيّنة: تهيئة مكان العمل، جمع العيّنات والتعامل معها، نظافة اليدين، المستلزمات المعقّمة، تقليل الرذاذ، التعقيم باللهب، مراقبة البيئة."),
 IM("How is the workstation prepared?", "كيف يُهيّأ مكان العمل؟", "Disinfect with 70% ethanol or sodium hypochlorite and organize tools to minimize unnecessary movement.", "يُطهّر بالإيثانول 70% أو هايبوكلورايت الصوديوم وتُنظّم الأدوات لتقليل الحركة غير الضرورية."),
 IM("How are aerosols minimized?", "كيف يُقلَّل الرذاذ؟", "Perform procedures gently to avoid splashing and centrifuge in sealed containers with appropriate rotors.", "بتنفيذ الإجراءات بلطف لتجنّب التناثر، والطرد المركزي في حاويات محكمة مع دوّارات مناسبة."),
 IM("Describe flame sterilization and environmental monitoring.", "صف التعقيم باللهب ومراقبة البيئة.", "Reusable instruments such as inoculation loops are sterilized with a Bunsen burner or sterilizer without reaching over the flame; the environment is tested regularly with swabs and microbial culture.", "تُعقَّم الأدوات القابلة لإعادة الاستعمال كعروة التلقيح بمصباح بنزن أو جهاز تعقيم دون مدّ اليد فوق اللهب؛ وتُفحص البيئة بانتظام بالمسحات والزرع الميكروبي."),
]
meta = dict(subject_en="Medical Virology", subject_ar="الفيروسات الطبية", short_ar="فايروسات", unit_en="Lab 1", unit_ar="العملي 1", unit_label="LAB", unit_no="1",
            title_en="Laboratory Safety Guidelines & Aseptic Techniques", title_ar="إرشادات السلامة في المختبر والتقنيات المعقّمة",
            kind="Laboratories — عملي", stage="The third stage — الثالثة", instructor="م.م. آية وسمي")
save("virology-lab1-safety", meta, blocks, mcq, tf, traps, important)

```
