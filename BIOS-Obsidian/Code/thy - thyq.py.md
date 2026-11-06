---
source: BIOS-Obsidian/tools/scripts/thy/thyq.py
handouts: [endocrine-lab5-thyroid-hormones]
saved: 2026-11-06
tags: [bios, code]
---
# thy/thyq.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#endocrine-lab5-thyroid-hormones|endocrine-lab5-thyroid-hormones]]

```python
mcq = [
 {"topic_en": "Synthesis and iodine", "topic_ar": "التصنيع واليود"},
 Q("Thyroid hormones are stored in the colloid as part of:", "تُخزن هرمونات الدرقية في الغروانية جزءًا من:", O(("Thyroglobulin", "الثايروغلوبيولين"), ("Albumin", "الألبومين"), ("TBG", "TBG"), ("Transthyretin", "الترانسثايريتين")), "a"),
 Q("Iodide is transported into follicular cells by:", "يُنقل اليوديد إلى الخلايا الجريبية بواسطة:", O(("Thyroid peroxidase", "البيروكسيديز الدرقي"), ("Sodium–iodide symporter (NIS)", "الناقل المشترك للصوديوم-اليوديد"), ("Deiodinase", "إنزيم نزع اليود"), ("TSH receptor", "مستقبل TSH")), "b"),
 Q("Iodide is oxidized by TPO using:", "يؤكسد TPO اليوديد مستعملًا:", O(("Oxygen gas", "غاز الأكسجين"), ("NADPH only", "NADPH فقط"), ("Hydrogen peroxide", "بيروكسيد الهيدروجين"), ("Glucose", "الكلوكوز")), "c"),
 Q("MIT + DIT gives:", "MIT + DIT يعطي:", O(("T4", "T4"), ("rT3", "rT3"), ("Thyroglobulin", "الثايروغلوبيولين"), ("T3", "T3")), "d"),
 Q("DIT + DIT gives:", "DIT + DIT يعطي:", O(("T4 (thyroxine)", "T4 (الثايروكسين)"), ("T3", "T3"), ("MIT", "MIT"), ("TSH", "TSH")), "a"),
 Q("The release of T3 and T4 into the blood is stimulated by:", "يحفّز إطلاق T3 وT4 إلى الدم:", O(("Iodine", "اليود"), ("TSH", "TSH"), ("Albumin", "الألبومين"), ("rT3", "rT3")), "b"),
 Q("The thyroid gland secretes predominantly:", "تفرز الغدّة الدرقية بصورة رئيسية:", O(("T3", "T3"), ("rT3", "rT3"), ("T4", "T4"), ("MIT", "MIT")), "c"),
 Q("Recommended adult iodine intake is about:", "المدخول الموصى به من اليود للبالغ نحو:", O(("15 µg/day", "15 مايكروغرام/يوم"), ("1.5 g/day", "1.5 غ/يوم"), ("1500 µg/day", "1500 مايكروغرام/يوم"), ("150 µg/day", "150 مايكروغرام/يوم")), "d"),
 Q("Excess iodine temporarily inhibits hormone synthesis through:", "يثبّط اليود الزائد تصنيع الهرمون مؤقّتًا عبر:", O(("Wolff–Chaikoff effect", "تأثير وولف-تشايكوف"), ("Graves effect", "تأثير غريفز"), ("Coupling", "الاقتران"), ("Peripheral conversion", "التحويل المحيطي")), "a"),
 {"topic_en": "Metabolism and transport", "topic_ar": "الأيض والنقل"},
 Q("Inner-ring deiodination of T4 produces:", "نزع اليود من الحلقة الداخلية لـ T4 ينتج:", O(("T3 (active)", "T3 (فعّال)"), ("Reverse T3 (inactive)", "T3 العكسي (غير فعّال)"), ("Conjugated metabolites", "نواتج مقترنة"), ("DIT", "DIT")), "b"),
 Q("T3 is more active than T4 because it:", "T3 أنشط من T4 لأنه:", O(("Is more abundant", "أكثر وفرة"), ("Binds TBG more strongly", "يرتبط بـ TBG أقوى"), ("Interacts more strongly with thyroid hormone receptors", "يتفاعل أقوى مع مستقبلات هرمون الدرقية"), ("Has more iodine", "فيه يود أكثر")), "c"),
 Q("The percentage of thyroid hormones bound to plasma proteins is:", "نسبة هرمونات الدرقية المرتبطة ببروتينات البلازما:", O(("About 50%", "نحو 50%"), ("About 75%", "نحو 75%"), ("About 1%", "نحو 1%"), ("More than 99%", "أكثر من 99%")), "d"),
 Q("The major high-affinity carrier of thyroid hormones is:", "الناقل الرئيسي عالي الألفة لهرمونات الدرقية:", O(("TBG", "TBG"), ("Albumin", "الألبومين"), ("Transthyretin", "الترانسثايريتين"), ("Thyroglobulin", "الثايروغلوبيولين")), "a"),
 Q("Albumin as a thyroid hormone carrier has:", "الألبومين ناقلًا لهرمون الدرقية له:", O(("High affinity, low capacity", "ألفة عالية وسعة قليلة"), ("Lower affinity but high transport capacity", "ألفة أقل لكن سعة نقل عالية"), ("No binding", "لا ارتباط"), ("The same role as TSH", "دور TSH نفسه")), "b"),
 Q("Transthyretin is also known as:", "يُعرف الترانسثايريتين أيضًا بـ:", O(("Thyroglobulin", "الثايروغلوبيولين"), ("TBG", "TBG"), ("Thyroxine-binding prealbumin", "البري ألبومين الرابط للثايروكسين"), ("Reverse T3", "T3 العكسي")), "c"),
 Q("In pregnancy, changes in binding proteins may cause:", "في الحمل قد تسبّب تغيّرات البروتينات الرابطة:", O(("FT4 change without total T4 change", "تغيّر FT4 دون T4 الكلّي"), ("Graves disease", "داء غريفز"), ("Iodine deficiency", "نقص اليود"), ("Total T4 change without corresponding FT4 change", "تغيّر T4 الكلّي دون تغيّر مقابل في FT4")), "d"),
 {"topic_en": "Actions and TFTs", "topic_ar": "الأفعال وفحوص الوظيفة"},
 Q("Thyroid hormones:", "هرمونات الدرقية:", O(("Increase basal metabolic rate and heat production", "تزيد معدّل الأيض الأساسي وإنتاج الحرارة"), ("Decrease oxygen consumption", "تقلّل استهلاك الأكسجين"), ("Lower glucose turnover", "تخفض تدوير الكلوكوز"), ("Block LDL clearance", "تمنع تصفية LDL")), "a"),
 Q("Hypothyroidism commonly causes:", "يسبّب قصور الدرقية عادةً:", O(("Low cholesterol", "انخفاض الكوليسترول"), ("Increased total cholesterol and LDL-C", "زيادة الكوليسترول الكلّي وLDL-C"), ("Muscle wasting from excess hormone", "هزال العضلات من الهرمون الزائد"), ("Increased BMR", "زيادة الأيض")), "b"),
 Q("Excessive thyroid hormone leads to:", "يؤدّي الهرمون الدرقي الزائد إلى:", O(("Protein synthesis and growth", "تصنيع البروتين والنمو"), ("Reduced heat", "حرارة أقل"), ("Protein breakdown and muscle wasting", "تحطّم البروتين وهزال العضلات"), ("High LDL", "ارتفاع LDL")), "c"),
 Q("The principal tests for thyroid function are:", "الفحوص الرئيسية لوظيفة الدرقية:", O(("Total T3 and rT3", "T3 الكلّي وrT3"), ("Thyroglobulin and albumin", "الثايروغلوبيولين والألبومين"), ("Iodine and TPO", "اليود وTPO"), ("TSH and FT4", "TSH وFT4")), "d"),
 Q("TSH ↑ with FT4 ↓ indicates:", "TSH ↑ مع FT4 ↓ يدلّ على:", O(("Primary hypothyroidism", "قصور الدرقية الأولي"), ("Primary hyperthyroidism", "فرط الدرقية الأولي"), ("Subclinical hyperthyroidism", "فرط تحت سريري"), ("Central hypothyroidism", "قصور مركزي")), "a"),
 Q("TSH ↑ with normal FT4 indicates:", "TSH ↑ مع FT4 طبيعي يدلّ على:", O(("Primary hyperthyroidism", "فرط أولي"), ("Subclinical hypothyroidism", "قصور تحت سريري"), ("Central hypothyroidism", "قصور مركزي"), ("Graves disease", "داء غريفز")), "b"),
 Q("Low or inappropriately normal TSH with low FT4 indicates:", "TSH منخفض أو طبيعي على غير المتوقّع مع FT4 منخفض يدلّ على:", O(("Primary hypothyroidism", "قصور أولي"), ("Subclinical hyperthyroidism", "فرط تحت سريري"), ("Central hypothyroidism", "قصور الدرقية المركزي"), ("Hashimoto thyroiditis", "هاشيموتو")), "c"),
 Q("FT3 is particularly useful when suspecting:", "يفيد FT3 خصوصًا عند الاشتباه بـ:", O(("Iodine deficiency", "نقص اليود"), ("Central hypothyroidism", "القصور المركزي"), ("Hashimoto", "هاشيموتو"), ("T3-predominant thyrotoxicosis", "الانسمام الدرقي الذي يغلب فيه T3")), "d"),
 Q("Thyrotoxicosis means:", "الانسمام الدرقي يعني:", O(("Excessive thyroid hormone action regardless of the source", "زيادة فعل هرمون الدرقية بغضّ النظر عن المصدر"), ("Excess synthesis by the gland only", "زيادة التصنيع من الغدّة فقط"), ("Low thyroid hormone", "انخفاض هرمون الدرقية"), ("Iodine excess only", "زيادة اليود فقط")), "a"),
 {"topic_en": "Disorders and values", "topic_ar": "الاضطرابات والقيم"},
 Q("A cause of hypothyroidism is:", "من أسباب قصور الدرقية:", O(("Graves disease", "داء غريفز"), ("Hashimoto thyroiditis", "التهاب هاشيموتو"), ("Toxic adenoma", "الورم الغدّي السمّي"), ("Toxic multinodular goiter", "الدراق العقدي السمّي")), "b"),
 Q("In Graves disease, antibodies:", "في داء غريفز الأضداد:", O(("Destroy TPO", "تتلف TPO"), ("Block iodide trapping", "تمنع اقتناص اليوديد"), ("Stimulate the TSH receptor", "تحفّز مستقبل TSH"), ("Bind T4", "ترتبط بـ T4")), "c"),
 Q("Anti-TPO antibodies are frequently positive in:", "أضداد TPO موجبة كثيرًا في:", O(("Graves disease", "داء غريفز"), ("Toxic adenoma", "الورم الغدّي السمّي"), ("Iodine deficiency", "نقص اليود"), ("Hashimoto thyroiditis", "التهاب هاشيموتو")), "d"),
 Q("The typical adult reference interval for TSH is:", "المدى المرجعي النموذجي لـ TSH للبالغين:", O(("0.5–4.0 mIU/L", "0.5–4.0 ملي وحدة/لتر"), ("4.5–11.2 mIU/L", "4.5–11.2"), ("60–180 mIU/L", "60–180"), ("10–20 mIU/L", "10–20")), "a"),
 Q("The typical adult reference interval for total T4 is:", "المدى المرجعي النموذجي لـ T4 الكلّي:", O(("60–180 ng/dL", "60–180 نانوغرام/دل"), ("4.5–11.2 µg/dL", "4.5–11.2 مايكروغرام/دل"), ("0.5–4.0 µg/dL", "0.5–4.0"), ("150 µg/dL", "150")), "b"),
]
mcq = balance(mcq, 71)

tf = [
 TF("Thyroid hormones are synthesized by follicular cells.", "تُصنَّع هرمونات الدرقية في الخلايا الجريبية.", "T"),
 TF("DIT contains one iodine atom.", "يحتوي DIT على ذرّة يود واحدة.", "F"),
 TF("MIT and DIT are deiodinated inside the thyroid, allowing iodine recycling.", "يُنزع اليود من MIT وDIT داخل الدرقية فيُعاد تدويره.", "T"),
 TF("Most circulating T3 is generated by peripheral conversion of T4.", "يتولّد معظم T3 الدوّار بالتحويل المحيطي لـ T4.", "T"),
 TF("Chronic iodine deficiency may cause goiter.", "قد يسبّب نقص اليود المزمن الدراق.", "T"),
 TF("Reverse T3 is biologically active.", "T3 العكسي فعّال حيويًا.", "F"),
 TF("Free fractions FT4 and FT3 are available to tissues.", "الأجزاء الحرّة FT4 وFT3 متاحة للأنسجة.", "T"),
 TF("Thyroid hormones promote hepatic LDL clearance.", "تعزّز هرمونات الدرقية تصفية الكبد للـ LDL.", "T"),
 TF("Untreated congenital hypothyroidism always recovers fully.", "يُشفى قصور الدرقية الخلقي غير المعالج دائمًا بالكامل.", "F"),
 TF("In primary hyperthyroidism TSH is high.", "في فرط الدرقية الأولي يكون TSH مرتفعًا.", "F"),
 TF("Thyroiditis can cause thyrotoxicosis without increased hormone synthesis.", "قد يسبّب التهاب الدرقية انسمامًا دون زيادة تصنيع الهرمون.", "T"),
 TF("Toxic adenoma is a cause of hypothyroidism.", "الورم الغدّي السمّي من أسباب قصور الدرقية.", "F"),
 TF("The laboratory's own reference interval should always be used.", "يجب دائمًا استعمال المدى المرجعي الخاصّ بالمختبر.", "T"),
]

traps = [
 TR("T3 or T4 from MIT/DIT?", "T3 أم T4 من MIT/DIT؟", "MIT + DIT = T3 (1 + 2 = 3 iodines); DIT + DIT = T4 (2 + 2 = 4).", "MIT + DIT = T3 (1 + 2 = 3 ذرّات يود)؛ DIT + DIT = T4 (2 + 2 = 4)."),
 TR("Outer vs inner ring", "الحلقة الخارجية مقابل الداخلية", "Outer-ring deiodination → T3 (active); inner-ring → reverse T3 (inactive).", "نزع اليود من الخارجية ← T3 (فعّال)؛ ومن الداخلية ← T3 العكسي (غير فعّال)."),
 TR("Carrier affinity vs capacity", "ألفة الناقل مقابل سعته", "TBG = highest affinity (major); albumin = lowest affinity but highest capacity; TTR = prealbumin.", "TBG = أعلى ألفة (الرئيسي)؛ الألبومين = أقل ألفة لكن أعلى سعة؛ TTR = البري ألبومين."),
 TR("Subclinical", "تحت السريري", "Subclinical = TSH abnormal (↑ hypo, ↓ hyper) with NORMAL FT4.", "تحت السريري = TSH غير طبيعي (↑ قصور، ↓ فرط) مع FT4 طبيعي."),
 TR("Central hypothyroidism", "القصور المركزي", "TSH is low or inappropriately normal (not high) with low FT4 — the problem is in the pituitary/hypothalamus.", "TSH منخفض أو طبيعي على غير المتوقّع (لا مرتفع) مع FT4 منخفض — المشكلة في النخامية/الوطاء."),
 TR("Hyperthyroidism vs thyrotoxicosis", "فرط الدرقية مقابل الانسمام الدرقي", "Hyperthyroidism = the gland overproduces; thyrotoxicosis = too much hormone action from any source (e.g. thyroiditis, taking too many tablets).", "فرط الدرقية = الغدّة تفرط في الإنتاج؛ الانسمام = فعل هرموني زائد من أي مصدر (مثل التهاب الدرقية أو تناول حبوب كثيرة)."),
 TR("Units of the reference values", "وحدات القيم المرجعية", "Total T4 in µg/dL (4.5–11.2), total T3 in ng/dL (60–180), TSH in mIU/L (0.5–4.0).", "T4 الكلّي بالمايكروغرام/دل (4.5–11.2)، T3 الكلّي بالنانوغرام/دل (60–180)، TSH بالملي وحدة/لتر (0.5–4.0)."),
]

important = [
 IM("Describe the steps of thyroid hormone synthesis.", "صف خطوات تصنيع هرمونات الدرقية.", "1. Iodide trapping by NIS into follicular cells. 2. Oxidation of iodide to reactive iodine by TPO using H₂O₂. 3. Organification: iodine binds tyrosine in thyroglobulin → MIT and DIT. 4. Coupling by TPO: MIT + DIT → T3, DIT + DIT → T4. 5. Storage in colloid on thyroglobulin; TSH stimulates endocytosis and lysosomal proteolysis to release T3 and T4; MIT and DIT are deiodinated for iodine recycling.", "1. اقتناص اليوديد بـ NIS إلى الخلايا الجريبية. 2. أكسدة اليوديد إلى يود فعّال بـ TPO مستعملًا H₂O₂. 3. التعضية: يرتبط اليود بالتايروسين في الثايروغلوبيولين ← MIT وDIT. 4. الاقتران بـ TPO: MIT + DIT ← T3، DIT + DIT ← T4. 5. الخزن في الغروانية على الثايروغلوبيولين؛ ويحفّز TSH الإدخال الخلوي والتحلّل الليسوسومي لإطلاق T3 وT4؛ ويُنزع اليود من MIT وDIT لإعادة تدويره."),
 IM("What is the importance of iodine for the thyroid?", "ما أهمية اليود للدرقية؟", "Iodine is essential for T3 and T4 synthesis; adults need about 150 µg/day. Chronic deficiency causes goiter and hypothyroidism; excess iodine temporarily inhibits synthesis (Wolff–Chaikoff effect). Iodine-containing drugs and contrast agents may alter thyroid function in susceptible people.", "اليود أساسي لتصنيع T3 وT4، ويحتاج البالغ نحو 150 مايكروغرام/يوم. ونقصه المزمن يسبّب الدراق وقصور الدرقية؛ وزيادته تثبّط التصنيع مؤقّتًا (تأثير وولف-تشايكوف). وقد تغيّر الأدوية والصبغات المحتوية على اليود وظيفة الدرقية في المهيَّئين."),
 IM("Explain T4 metabolism and transport of thyroid hormones in blood.", "اشرح أيض T4 ونقل هرمونات الدرقية في الدم.", "T4 is a reservoir for active T3. Peripheral deiodinases: outer-ring → T3 (active), inner-ring → reverse T3 (inactive), other pathways → conjugated metabolites for elimination. More than 99% of the hormones are protein bound: TBG (major, high affinity), transthyretin (prealbumin), albumin (low affinity, high capacity). Only the free FT4 and FT3 are available to tissues; pregnancy, estrogen, liver disease and drugs can change total T4 without changing FT4.", "T4 مخزون لـ T3 الفعّال. إنزيمات نزع اليود المحيطية: الحلقة الخارجية ← T3 (فعّال)، والداخلية ← T3 العكسي (غير فعّال)، ومسارات أخرى ← نواتج مقترنة للطرح. وأكثر من 99% من الهرمونات مرتبط بالبروتين: TBG (الرئيسي، ألفة عالية)، والترانسثايريتين (البري ألبومين)، والألبومين (ألفة قليلة، سعة عالية). والحرّ فقط FT4 وFT3 متاح للأنسجة؛ والحمل والإستروجين وأمراض الكبد والأدوية قد تغيّر T4 الكلّي دون FT4."),
 IM("List the physiological actions of thyroid hormones.", "عدّد الأفعال الفسيولوجية لهرمونات الدرقية.", "Metabolic: ↑ BMR, oxygen consumption, heat. Carbohydrate: ↑ glucose turnover. Lipid: ↑ lipid turnover and hepatic LDL clearance (hypothyroidism raises cholesterol and LDL-C). Protein: normal levels → growth and synthesis; excess → breakdown and muscle wasting. Growth: skeletal maturation, childhood growth, brain development (congenital hypothyroidism → irreversible damage). Nervous/reproductive: cognition and reproductive health.", "الأيضي: ↑ معدّل الأيض واستهلاك الأكسجين والحرارة. الكربوهيدرات: ↑ تدوير الكلوكوز. الدهون: ↑ تدوير الدهون وتصفية LDL (القصور يرفع الكوليسترول وLDL-C). البروتين: المستوى الطبيعي ← النمو والتصنيع؛ والزائد ← التحطّم وهزال العضلات. النمو: نضج الهيكل ونموّ الطفولة وتطوّر الدماغ (القصور الخلقي ← ضرر غير قابل للعكس). العصبي/التناسلي: الإدراك والصحّة الإنجابية."),
 IM("Interpret TSH and FT4 in thyroid disorders.", "فسّر TSH وFT4 في اضطرابات الدرقية.", "Primary hypothyroidism: TSH ↑, FT4 ↓. Primary hyperthyroidism: TSH ↓, FT4 ↑. Subclinical hypothyroidism: TSH ↑, FT4 normal. Subclinical hyperthyroidism: TSH ↓, FT4 normal. Central hypothyroidism: TSH low or inappropriately normal, FT4 ↓. FT3 helps in T3-predominant thyrotoxicosis.", "القصور الأولي: TSH ↑ وFT4 ↓. الفرط الأولي: TSH ↓ وFT4 ↑. القصور تحت السريري: TSH ↑ وFT4 طبيعي. الفرط تحت السريري: TSH ↓ وFT4 طبيعي. القصور المركزي: TSH منخفض أو طبيعي على غير المتوقّع وFT4 ↓. ويفيد FT3 في الانسمام الذي يغلب فيه T3."),
 IM("Compare Hashimoto thyroiditis and Graves disease.", "قارن بين التهاب هاشيموتو وداء غريفز.", "Hashimoto: chronic autoimmune damage of thyroid tissue → hypothyroidism; TSH elevated; anti-TPO antibodies often positive. Graves: autoimmune antibodies stimulate the TSH receptor → hyperthyroidism; TSH suppressed, FT4 and/or FT3 elevated, TRAb may be positive.", "هاشيموتو: تلف مناعي ذاتي مزمن لنسيج الدرقية ← قصور؛ TSH مرتفع؛ وأضداد TPO موجبة غالبًا. غريفز: أضداد ذاتية تحفّز مستقبل TSH ← فرط؛ TSH مكبوت، وFT4 و/أو FT3 مرتفع، وقد تكون TRAb موجبة."),
]

meta = {"subject_en": "Practical Endocrinology", "subject_ar": "الغدد الصماء العملي", "short_ar": "غدد صماء", "instructor": "م.م. نور إبراهيم جليل",
        "unit_en": "Lab 5", "unit_ar": "العملي 5", "unit_label": "LAB", "unit_no": "5",
        "title_en": "Thyroid hormones", "title_ar": "هرمونات الغدّة الدرقية",
        "kind": "Laboratories — عملي", "stage": "The third stage — الثالثة"}
sys.path.insert(0, "/tmp/claude-0/-home-user/61936e68-b1f5-523f-9c76-ea02be11c0c4/scratchpad"); from bidi import ltr_all; from flowfit import fit
blocks, mcq, tf, traps, important = ltr_all(blocks), ltr_all(mcq), ltr_all(tf), ltr_all(traps), ltr_all(important)   # formulas inside Arabic stay LTR
save("endocrine-lab5-thyroid-hormones", meta, blocks, mcq, tf, traps, important)
fit("endocrine-lab5-thyroid-hormones", min_gap=0.08)   # no big gaps (2026-11-06 rebuild)

```
