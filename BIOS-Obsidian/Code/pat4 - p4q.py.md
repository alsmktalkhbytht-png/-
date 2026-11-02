---
source: BIOS-Obsidian/tools/scripts/pat4/p4q.py
handouts: [pathology-lec4-lung-cancer]
saved: 2026-11-02
tags: [bios, code]
---
# pat4/p4q.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#pathology-lec4-lung-cancer|pathology-lec4-lung-cancer]]

```python
A = lambda f: "assets/" + f
mcq = [
 {"topic_en": "Lung tumors and carcinomas", "topic_ar": "أورام الرئة والكارسينومات"},
 Q("Roughly what percentage of primary lung tumors are carcinomas?", "تقريبًا كم نسبة أورام الرئة الأولية التي هي كارسينومات؟", O(("95%", "95%"), ("50%", "50%"), ("5%", "5%"), ("15%", "15%")), "a"),
 Q("The most common benign tumor of the lung is:", "أشيع ورم حميد في الرئة:", O(("Carcinoid", "الكارسينويد"), ("Hamartoma", "الورم العابي"), ("Fibrosarcoma", "الساركوما الليفية"), ("Lymphoma", "اللمفوما")), "b"),
 Q("A hamartoma consists mainly of:", "يتكوّن الورم العابي أساسًا من:", O(("Smooth muscle", "عضل أملس"), ("Lymphoid tissue", "نسيج لمفي"), ("Mature cartilage", "غضروف ناضج"), ("Squamous epithelium", "ظهارة حرشفية")), "c"),
 Q("On chest radiographs a hamartoma appears as:", "يظهر الورم العابي في صورة الصدر الشعاعية كـ:", O(("Cavity", "تجويف"), ("Pleural effusion", "انصباب جنبي"), ("Ground-glass opacity", "عتامة زجاجية"), ("Coin lesion", "آفة العملة النقدية")), "d"),
 Q("The size of a hamartoma is about:", "حجم الورم العابي حوالي:", O(("3 to 4 cm", "3 إلى 4 سم"), ("10 to 15 cm", "10 إلى 15 سم"), ("< 1 mm", "أقل من 1 ملم"), ("20 cm", "20 سم")), "a"),
 Q("Lung cancer accounts for about what fraction of cancer deaths in US men?", "يشكّل سرطان الرئة حوالي أيّ جزء من وفيات السرطان عند الرجال في أمريكا؟", O(("One half", "النصف"), ("One third", "الثلث"), ("One tenth", "العُشر"), ("Two thirds", "الثلثين")), "b"),
 Q("Since 1987, more women die each year from lung cancer than from:", "منذ 1987 تموت نساء بسرطان الرئة أكثر من:", O(("Colon cancer", "سرطان القولون"), ("Leukemia", "الابيضاض"), ("Breast cancers", "سرطانات الثدي"), ("Ovarian cancer", "سرطان المبيض")), "c"),
 Q("The peak incidence of lung cancer is in persons in their:", "ذروة الإصابة بسرطان الرئة في الأعمار:", O(("20s and 30s", "العشرينات والثلاثينات"), ("Childhood", "الطفولة"), ("80s and 90s", "الثمانينات والتسعينات"), ("50s and 60s", "الخمسينات والستينات")), "d"),
 Q("Which is NOT one of the four major histologic types of lung carcinoma?", "أيّ مما يأتي ليس من الأنواع النسيجية الأربعة الرئيسية؟", O(("Hamartoma", "الورم العابي"), ("Adenocarcinoma", "الكارسينوما الغدّية"), ("Squamous cell carcinoma", "الحرشفية"), ("Large cell carcinoma", "الخلايا الكبيرة")), "a"),
 {"topic_en": "SCLC and NSCLC", "topic_ar": "SCLC وNSCLC"},
 Q("NSCLC includes:", "يشمل NSCLC:", O(("Small cell carcinoma only", "الخلايا الصغيرة فقط"), ("Adenocarcinoma, squamous and large cell carcinomas", "الغدّية والحرشفية والخلايا الكبيرة"), ("Hamartoma", "الورم العابي"), ("Lymphomas", "اللمفومات")), "b"),
 Q("SCLC is not curable by surgery because:", "لا يُشفى SCLC بالجراحة لأن:", O(("It is benign", "حميد"), ("It is radioresistant", "مقاوم للإشعاع"), ("Virtually all have metastasized by the time of diagnosis", "كله تقريبًا منتشر عند التشخيص"), ("It is too small", "صغير جدًا")), "c"),
 Q("SCLC is best treated by:", "أفضل علاج لـ SCLC:", O(("Surgery alone", "الجراحة وحدها"), ("Antibiotics", "المضادات الحيوية"), ("Observation", "المراقبة"), ("Chemotherapy, with or without radiation", "العلاج الكيميائي مع أو بدون إشعاع")), "d"),
 Q("Targeted therapies for mutated gene products are available mainly in:", "تتوفّر العلاجات الموجّهة لنواتج الجينات الطافرة خاصةً في:", O(("Adenocarcinomas", "الكارسينومات الغدّية"), ("Small cell carcinoma", "الخلايا الصغيرة"), ("Hamartomas", "الأورام العابية"), ("Carcinoids", "الكارسينويدات")), "a"),
 Q("According to the subtype figure, SCLC arises from:", "حسب شكل الأنواع، ينشأ SCLC من:", O(("Alveolar type II cell", "خلية سنخية نوع II"), ("Neuroendocrine cell", "خلية صمّاء عصبية"), ("Basal epithelial cell", "خلية ظهارية قاعدية"), ("Fibroblast", "أرومة ليفية")), "b"),
 Q("In the figure, NSCLC represents about:", "في الشكل يمثّل NSCLC حوالي:", O(("15%", "15%"), ("50%", "50%"), ("85%", "85%"), ("5%", "5%")), "c"),
 {"topic_en": "Pathogenesis and predisposing factors", "topic_ar": "الإمراضية والعوامل المهيّئة"},
 Q("A very early molecular event in smoking-related lung cancer is:", "حدث جزيئي مبكر جدًا في سرطان الرئة المرتبط بالتدخين:", O(("KRAS activation", "تنشيط KRAS"), ("TP53 mutation", "طفرة TP53"), ("P-450 induction", "تحفيز P-450"), ("Inactivation of tumor suppressor genes on 3p", "تعطيل الجينات الكابتة على 3p")), "d"),
 Q("TP53 mutations and KRAS activation occur:", "طفرات TP53 وتنشيط KRAS تحدث:", O(("Relatively late", "متأخرة نسبيًا"), ("First", "أولًا"), ("Never in smokers", "أبدًا عند المدخّنين"), ("Only in hamartoma", "فقط في الورم العابي")), "a"),
 Q("About what percentage of lung cancers occur in active or recent smokers?", "حوالي كم نسبة سرطانات الرئة عند المدخّنين الحاليين أو الحديثي الإقلاع؟", O(("50%", "50%"), ("90%", "90%"), ("30%", "30%"), ("10%", "10%")), "b"),
 Q("Habitual heavy smokers (two packs a day for 20 years) have a risk greater by:", "خطر المدخّنين الشرهين (علبتان يوميًا لمدة 20 سنة) أكبر بـ:", O(("2 times", "مرّتين"), ("5 times", "5 مرات"), ("60 times", "60 مرة"), ("10 times", "10 مرات")), "c"),
 Q("Passive smoking increases the risk of lung cancer to about:", "يزيد التدخين السلبي خطر سرطان الرئة إلى حوالي:", O(("60 times", "60 ضعفًا"), ("Ten times", "عشرة أضعاف"), ("No change", "لا تغيير"), ("Twice that of non-smokers", "ضعف غير المدخّنين")), "d"),
 Q("Exposure to asbestos increases the risk of lung cancer in non-smokers:", "التعرّض للأسبستوس يزيد خطر سرطان الرئة عند غير المدخّنين:", O(("Fivefold", "خمسة أضعاف"), ("Twofold", "ضعفين"), ("Sixtyfold", "ستين ضعفًا"), ("Not at all", "لا يزيد")), "a"),
 Q("After cessation of smoking, the risk:", "بعد الإقلاع عن التدخين، الخطر:", O(("Disappears immediately", "يختفي فورًا"), ("Decreases but may never return to baseline", "يقلّ لكن قد لا يعود للمستوى الأساسي"), ("Increases", "يزداد"), ("Is unchanged", "لا يتغيّر")), "b"),
 Q("Which of the following is an occupational dust linked to lung cancer?", "أيّ مما يأتي غبار مهني مرتبط بسرطان الرئة؟", O(("Calcium", "الكالسيوم"), ("Sodium", "الصوديوم"), ("Arsenic", "الزرنيخ"), ("Iron", "الحديد")), "c"),
 {"topic_en": "Chemicals and sequential changes", "topic_ar": "المواد الكيميائية والتغيّرات المتسلسلة"},
 Q("Procarcinogens are activated to ultimate carcinogens by:", "تُنشَّط طلائع المسرطنات إلى مسرطنات نهائية بواسطة:", O(("Lipase", "الليبيز"), ("Amylase", "الأميليز"), ("Trypsin", "التربسين"), ("P-450 monooxygenase system", "نظام P-450 أحادي الأوكسجيناز")), "d"),
 Q("Persons with the mutagen sensitivity genotype have a lung cancer risk of:", "الأشخاص ذوو النمط الحسّاس للمطفّرات لديهم خطر سرطان رئة:", O(("Greater than 10-fold", "أكثر من 10 أضعاف"), ("Half", "النصف"), ("Twice", "ضعفين"), ("Same as controls", "مثل الضابطين")), "a"),
 Q("The sequential changes leading to cancer are best documented for:", "التغيّرات المتسلسلة نحو السرطان موثّقة أفضل في:", O(("Adenocarcinoma", "الغدّية"), ("Squamous cell carcinoma", "الحرشفية"), ("Hamartoma", "الورم العابي"), ("Carcinoid", "الكارسينويد")), "b"),
 Q("The first change in the epithelial sequence is:", "أول تغيّر في التسلسل الظهاري:", O(("Carcinoma in situ", "الكارسينوما الموضعية"), ("Invasive cancer", "السرطان الغازي"), ("Basal cell hyperplasia", "فرط تنسّج الخلايا القاعدية"), ("Squamous dysplasia", "خلل التنسّج الحرشفي")), "c"),
 Q("The subtypes with the strongest association with tobacco are:", "الأنواع الأقوى ارتباطًا بالتبغ:", O(("Adenocarcinoma and carcinoid", "الغدّية والكارسينويد"), ("Large cell and hamartoma", "الخلايا الكبيرة والورم العابي"), ("Lymphoma and sarcoma", "اللمفوما والساركوما"), ("Squamous and small-cell carcinomas", "الحرشفية وصغيرة الخلايا")), "d"),
 {"topic_en": "Picture questions", "topic_ar": "أسئلة الصور"},
 Q("This chest radiograph lesion is typical of:", "هذه الآفة في صورة الصدر نموذجية لـ:", O(("Hamartoma (coin lesion)", "الورم العابي (آفة العملة)"), ("Pneumonia", "ذات الرئة"), ("Asthma", "الربو"), ("Emphysema", "انتفاخ الرئة")), "a", img=A("coin-lesion-cxr.jpg"), img_h="44mm"),
 Q("In this figure, LUSC arises from:", "في هذا الشكل، ينشأ LUSC من:", O(("Neuroendocrine cell", "خلية صمّاء عصبية"), ("Basal epithelial cell", "خلية ظهارية قاعدية"), ("Alveolar type II cell", "خلية سنخية نوع II"), ("Various epithelial cells", "خلايا ظهارية متنوّعة")), "b", img=A("subtypes.jpg"), img_h="44mm"),
 Q("In this chart, “Acinar, Papillary, Bronchioalveolar” are subtypes of:", "في هذا المخطط “عنبي، حليمي، قصيبي سنخي” أنواع فرعية لـ:", O(("Small cell carcinoma", "الخلايا الصغيرة"), ("Carcinoid tumor", "الكارسينويد"), ("Adenocarcinoma", "الكارسينوما الغدّية"), ("Large cell carcinoma", "الخلايا الكبيرة")), "c", img=A("histology-chart.jpg"), img_h="52mm"),
]

tf = [
 TF("Lungs are frequently the site of metastases from extra-thoracic cancers.", "الرئتان موقع متكرّر للنقائل من سرطانات خارج الصدر.", "T"),
 TF("Lymphomas are part of the 95% carcinomas of the lung.", "اللمفومات جزء من الـ95% كارسينومات الرئة.", "F"),
 TF("A hamartoma may contain fat, fibrous tissue and blood vessels.", "قد يحتوي الورم العابي دهنًا ونسيجًا ليفيًا وأوعية دموية.", "T"),
 TF("The incidence of lung cancer is increasing among males.", "الإصابة بسرطان الرئة تزداد بين الذكور.", "F"),
 TF("Lung cancer statistics reflect the causal relationship of smoking and lung cancer.", "إحصائيات سرطان الرئة تعكس العلاقة السببية بين التدخين وسرطان الرئة.", "T"),
 TF("NSCLC usually responds well to chemotherapy.", "يستجيب NSCLC عادةً جيدًا للعلاج الكيميائي.", "F"),
 TF("NSCLC must be sub-classified into histologic and molecular subtypes.", "يجب تصنيف NSCLC فرعيًا إلى أنواع نسيجية وجزيئية.", "T"),
 TF("The sequence of molecular changes in lung cancer is random.", "تسلسل التغيّرات الجزيئية في سرطان الرئة عشوائي.", "F"),
 TF("Women have a higher susceptibility to tobacco carcinogens than men.", "النساء أكثر تأثّرًا بمسرطنات التبغ من الرجال.", "T"),
 TF("Genetic changes may persist for years in the bronchial epithelium of former smokers.", "قد تستمر التغيّرات الجينية سنوات في ظهارة القصبات عند المدخّنين السابقين.", "T"),
 TF("Smoking pipes and cigars greatly increases the risk, more than cigarettes.", "تدخين الغليون والسيجار يزيد الخطر كثيرًا أكثر من السجائر.", "F"),
 TF("There is a nearly linear correlation between lung cancer and pack-years of smoking.", "توجد علاقة خطية تقريبًا بين سرطان الرئة وسنوات العلبة.", "T"),
 TF("Squamous metaplasia comes after carcinoma in situ.", "يأتي الحؤول الحرشفي بعد الكارسينوما الموضعية.", "F"),
 TF("Persons with certain P-450 polymorphisms may have the greatest risk of lung cancer.", "قد يكون لأصحاب تعدّدات أشكال P-450 معيّنة أكبر خطر لسرطان الرئة.", "T"),
]

traps = [
 TR("Hamartoma — benign or malignant?", "الورم العابي — حميد أم خبيث؟",
    "Benign — the commonest benign lung tumor (coin lesion, mainly mature cartilage).", "حميد — أشيع ورم حميد في الرئة (آفة العملة، أساسًا غضروف ناضج)."),
 TR("SCLC or NSCLC — which is treated by surgery?", "SCLC أم NSCLC — أيّهما يُعالج جراحيًا؟",
    "NSCLC (more likely re-sectable); SCLC has metastasized at diagnosis → chemotherapy ± radiation.", "NSCLC (أكثر قابلية للاستئصال)؛ أما SCLC فمنتشر عند التشخيص ← كيميائي ± إشعاعي."),
 TR("3p loss or KRAS — which is early?", "فقد 3p أم KRAS — أيّهما مبكر؟",
    "3p tumor-suppressor inactivation is very early; TP53 mutation and KRAS activation are late.", "تعطيل كابتات 3p مبكر جدًا؛ وطفرة TP53 وتنشيط KRAS متأخران."),
 TR("×2, ×5, ×10, ×60 — which is which?", "×2، ×5، ×10، ×60 — أيّها لأيّ عامل؟",
    "Passive smoking ×2; asbestos in non-smokers ×5; mutagen sensitivity genotype > ×10; heavy smokers ×60.", "التدخين السلبي ×2؛ الأسبستوس عند غير المدخّنين ×5؛ النمط الحسّاس للمطفّرات > ×10؛ المدخّنون الشرهون ×60."),
 TR("Which subtype has the targeted therapies?", "أيّ نوع لديه العلاجات الموجّهة؟",
    "NSCLC, mainly adenocarcinomas; but the strongest link to tobacco is squamous and small-cell carcinoma.", "NSCLC، خاصةً الغدّية؛ لكن أقوى ارتباط بالتبغ للحرشفية وصغيرة الخلايا."),
 TR("Does quitting smoking return the risk to normal?", "هل يعيد الإقلاع عن التدخين الخطر للطبيعي؟",
    "No — it decreases over time but may never return to baseline.", "لا — يقلّ مع الوقت لكن قد لا يعود أبدًا للمستوى الأساسي."),
]

important = [
 IM("Write about the hamartoma of the lung.", "اكتب عن الورم العابي في الرئة.",
    "The most common benign lung tumor: spherical, small (3–4 cm), discrete; appears as a coin lesion on chest radiographs; consists mainly of mature cartilage admixed with fat, fibrous tissue and blood vessels; clonal cytogenetic abnormalities confirm it.",
    "أشيع ورم حميد في الرئة: كروي صغير (3–4 سم) محدّد؛ يظهر كآفة العملة في صورة الصدر؛ يتكوّن أساسًا من غضروف ناضج مختلط بالدهن والنسيج الليفي والأوعية؛ وتؤكّده الشذوذات الوراثية الخلوية النسيلية."),
 IM("List the four major histologic types of lung carcinoma and the two broad groups.", "عدّد الأنواع النسيجية الأربعة الرئيسية لكارسينوما الرئة والمجموعتين الواسعتين.",
    "Adenocarcinoma, squamous cell carcinoma, small cell carcinoma and large cell carcinoma. Groups: small cell lung cancer (SCLC) and non-small cell lung cancer (NSCLC: adenocarcinoma, squamous and large cell carcinomas).",
    "الكارسينوما الغدّية، كارسينوما الخلايا الحرشفية، كارسينوما الخلايا الصغيرة، كارسينوما الخلايا الكبيرة. المجموعتان: سرطان الرئة صغير الخلايا (SCLC) وغير صغير الخلايا (NSCLC: الغدّية والحرشفية والخلايا الكبيرة)."),
 IM("Why are lung carcinomas divided into SCLC and NSCLC?", "لماذا تُقسم كارسينومات الرئة إلى SCLC وNSCLC؟",
    "Virtually all SCLCs have metastasized by diagnosis, so are not curable by surgery and are treated by chemotherapy ± radiation. NSCLCs are more likely re-sectable and respond poorly to chemotherapy, but targeted therapies now exist for mutated genes (mainly adenocarcinoma), so NSCLC must be sub-classified histologically and molecularly.",
    "كل SCLC تقريبًا منتشر عند التشخيص فلا يُشفى بالجراحة ويُعالج بالكيميائي ± الإشعاعي. أما NSCLC فأكثر قابلية للاستئصال واستجابته للكيميائي ضعيفة، لكن توجد الآن علاجات موجّهة للجينات الطافرة (خاصةً الغدّية)، لذا يجب تصنيفه فرعيًا نسيجيًا وجزيئيًا."),
 IM("Explain the pathogenesis of smoking-related lung carcinoma.", "اشرح إمراضية كارسينوما الرئة المرتبطة بالتدخين.",
    "Stepwise accumulation of many genetic abnormalities (thousands in SCLC) transforms benign progenitor cells into neoplastic cells, in a predictable sequence paralleling histologic progression: 3p tumor-suppressor inactivation very early, TP53 mutation / KRAS activation late. Epithelial sequence: basal cell hyperplasia → squamous metaplasia → squamous dysplasia → carcinoma in situ → invasive cancer.",
    "تراكم تدريجي لشذوذات جينية كثيرة (بالآلاف في SCLC) يحوّل الخلايا السلفية الحميدة إلى ورمية، بتسلسل متوقّع يوازي التطوّر النسيجي: تعطيل كابتات 3p مبكر جدًا، وطفرة TP53 / تنشيط KRAS متأخر. التسلسل الظهاري: فرط تنسّج قاعدي ← حؤول حرشفي ← خلل تنسّج حرشفي ← كارسينوما موضعية ← سرطان غازٍ."),
 IM("List the predisposing factors of lung cancer.", "عدّد العوامل المهيّئة لسرطان الرئة.",
    "Active/recent smoking (90%; linear with pack-years); heavy smoking ×60; women more susceptible; risk stays above baseline after quitting; passive smoking ×2; pipes and cigars (modest); occupational dusts (arsenic, chromium, uranium, nickel, vinyl chloride, mustard gas); asbestos ×5 in non-smokers; P-450 polymorphisms; mutagen sensitivity genotype > ×10.",
    "التدخين الحالي/الحديث (90%؛ خطي مع سنوات العلبة)؛ التدخين الشره ×60؛ النساء أكثر تأثّرًا؛ يبقى الخطر فوق الأساسي بعد الإقلاع؛ التدخين السلبي ×2؛ الغليون والسيجار (متواضع)؛ الأتربة المهنية (الزرنيخ، الكروم، اليورانيوم، النيكل، كلوريد الفاينيل، غاز الخردل)؛ الأسبستوس ×5 عند غير المدخّنين؛ تعدّد أشكال P-450؛ النمط الحسّاس للمطفّرات > ×10."),
 IM("How do chemical substances cause lung cancer?", "كيف تسبّب المواد الكيميائية سرطان الرئة؟",
    "Procarcinogens need metabolic activation by the P-450 monooxygenase system into ultimate carcinogens; persons with P-450 gene polymorphisms metabolize smoke procarcinogens more and have the greatest risk; persons whose lymphocytes show chromosomal breaks after tobacco carcinogens (mutagen sensitivity genotype) have > 10-fold risk.",
    "طلائع المسرطنات تحتاج تنشيطًا أيضيًا بنظام P-450 أحادي الأوكسجيناز إلى مسرطنات نهائية؛ وأصحاب تعدّد أشكال جينات P-450 يستقلبون طلائع مسرطنات الدخان أكثر فيكون خطرهم الأكبر؛ ومن تتعرّض لمفاوياتهم لكسور كروموسومية بعد مسرطنات التبغ (النمط الحسّاس للمطفّرات) خطرهم > 10 أضعاف."),
]

meta = dict(subject_en="Pathology", subject_ar="علم الأمراض", short_ar="أمراض",
            unit_en="Lecture 4", unit_ar="المحاضرة 4", unit_label="LEC", unit_no="4",
            title_en="Lung Cancer", title_ar="سرطان الرئة",
            kind="Theory — نظري", stage="The fourth stage — الرابعة", instructor="د. حامد خليل التميمي")
save("pathology-lec4-lung-cancer", meta, blocks, balance(mcq, 17), tf, traps, important)

```
