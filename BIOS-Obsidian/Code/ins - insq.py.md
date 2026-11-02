---
source: BIOS-Obsidian/tools/scripts/ins/insq.py
handouts: [endocrine-lab4-insulin]
saved: 2026-11-02
tags: [bios, code]
---
# ins/insq.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#endocrine-lab4-insulin|endocrine-lab4-insulin]]

```python
mcq = [
 {"topic_en": "Insulin", "topic_ar": "الأنسولين"},
 Q("Insulin is produced by:", "يُنتج الأنسولين من:", O(("Beta cells of the pancreas", "خلايا بيتا في البنكرياس"), ("Alpha cells of the pancreas", "خلايا ألفا في البنكرياس"), ("The anterior pituitary", "النخامية الأمامية"), ("The adrenal medulla", "لبّ الكظر")), "a"),
 Q("Chemically, insulin is a:", "كيميائيًا الأنسولين:", O(("Steroid hormone", "هرمون ستيرويدي"), ("Peptide hormone", "هرمون ببتيدي"), ("Amine hormone", "هرمون أميني"), ("Lipid", "دهن")), "b"),
 Q("Which is NOT a function of insulin shown in the figure?", "أيّ مما يأتي ليس من وظائف الأنسولين في الشكل؟", O(("Facilitates glucose uptake", "يسهّل امتصاص الكلوكوز"), ("Promotes glycogen synthesis", "يعزّز تصنيع الغلايكوجين"), ("Stimulates glucose production", "يحفّز إنتاج الكلوكوز"), ("Enhances fat storage", "يعزّز خزن الدهون")), "c"),
 Q("Insulin estimation is important in diagnosing:", "تقدير الأنسولين مهم في تشخيص:", O(("Anemia", "فقر الدم"), ("Hepatitis", "التهاب الكبد"), ("Gout", "النقرس"), ("Diabetes mellitus type 1 and type 2", "داء السكري النوع 1 والنوع 2")), "d"),
 Q("Insulin estimation helps in assessing all EXCEPT:", "يساعد تقدير الأنسولين في تقييم كل ما يأتي ما عدا:", O(("Thyroid function", "وظيفة الدرقية"), ("Insulin resistance", "مقاومة الأنسولين"), ("Hyperinsulinemia", "فرط أنسولين الدم"), ("Pancreatic function", "وظيفة البنكرياس")), "a"),
 Q("Which is listed in the lecture as a symptom of insulin deficiency?", "أيّ مما يأتي مذكور في المحاضرة عرضًا لنقص الأنسولين؟", O(("Weight gain", "زيادة الوزن"), ("Shakiness", "الارتجاف"), ("Slow heartbeat", "بطء القلب"), ("High blood pressure", "ارتفاع الضغط")), "b"),
 Q("When insulin increases, it increases the risk of:", "عندما يزداد الأنسولين يزيد خطر:", O(("Type 1 diabetes", "السكري النوع 1"), ("Anemia", "فقر الدم"), ("Obesity and type 2 diabetes", "السمنة والسكري النوع 2"), ("Hypothyroidism", "قصور الدرقية")), "c"),
 Q("High insulin also:", "زيادة الأنسولين أيضًا:", O(("Increases life expectancy", "تزيد العمر المتوقّع"), ("Prevents cardiovascular disease", "تمنع أمراض القلب"), ("Lowers fat storage", "تقلّل خزن الدهون"), ("Decreases health span", "تقلّل مدّة الصحّة")), "d"),
 {"topic_en": "Estimation methods", "topic_ar": "طرق التقدير"},
 Q("Which is NOT one of the insulin estimation methods in the lecture?", "أيّ مما يأتي ليس من طرق تقدير الأنسولين في المحاضرة؟", O(("Sahli’s method", "طريقة سالي"), ("ELISA", "الإليزا"), ("HPLC", "HPLC"), ("Mass spectrometry", "مطيافية الكتلة")), "a"),
 Q("The principle of ELISA couples an antigen-antibody reaction with:", "يقرن مبدأ الإليزا تفاعل المستضد-الضد بـ:", O(("Radioactive counting", "عدّ إشعاعي"), ("An enzyme-catalyzed color change", "تغيّر لوني يحفّزه إنزيم"), ("Agglutination", "التلازن"), ("Precipitation in gel", "الترسيب في الهلام")), "b"),
 Q("In insulin ELISA, the microplate is first coated with:", "في إليزا الأنسولين تُغلّف الصفيحة أولًا بـ:", O(("Substrate", "الركيزة"), ("Serum", "المصل"), ("Insulin-specific antibodies", "أضداد خاصّة بالأنسولين"), ("Wash buffer", "محلول الغسل")), "c"),
 Q("The substrate in ELISA is converted by the enzyme into:", "تتحوّل الركيزة في الإليزا بالإنزيم إلى:", O(("Insulin", "أنسولين"), ("An antibody", "ضد"), ("A radioactive label", "وسم إشعاعي"), ("A colored product", "ناتج ملوّن")), "d"),
 Q("An advantage of ELISA is:", "من مزايا الإليزا:", O(("No radiation, safer, widely available", "بلا إشعاع، أكثر أمانًا، متوفّرة"), ("Higher sensitivity than RIA", "حساسية أعلى من RIA"), ("No antibodies needed", "لا تحتاج أضدادًا"), ("No equipment needed", "لا تحتاج أجهزة")), "a"),
 Q("A disadvantage of ELISA compared to RIA is:", "من عيوب الإليزا مقارنةً بـ RIA:", O(("Radiation hazard", "خطر الإشعاع"), ("Moderate sensitivity", "حساسية متوسّطة"), ("Not available", "غير متوفّرة"), ("Needs live cells", "تحتاج خلايا حيّة")), "b"),
 {"topic_en": "Normal range and procedure", "topic_ar": "المدى الطبيعي والطريقة"},
 Q("The normal fasting insulin range is:", "المدى الطبيعي للأنسولين الصيامي:", O(("10 - 50 μU/mL", "10 - 50 مايكرووحدة/مل"), ("< 2.6 μU/mL", "أقل من 2.6"), ("2.6 - 24.9 μU/mL", "2.6 - 24.9 مايكرووحدة/مل"), ("> 24.9 μU/mL", "أكثر من 24.9")), "c"),
 Q("Fasting insulin of 18 - 174 pmol/L corresponds to:", "الأنسولين الصيامي 18 - 174 بيكومول/لتر يقابل:", O(("Insulin resistance", "مقاومة الأنسولين"), ("Low insulin", "أنسولين منخفض"), ("Hyperinsulinemia", "فرط الأنسولين"), ("The normal range", "المدى الطبيعي")), "d"),
 Q("Insulin above 24.9 μU/mL indicates:", "الأنسولين فوق 24.9 مايكرووحدة/مل يدلّ على:", O(("Insulin resistance and hyperinsulinemia", "مقاومة الأنسولين وفرط أنسولين الدم"), ("Normal level", "مستوى طبيعي"), ("Low insulin", "أنسولين منخفض"), ("Lab error only", "خطأ مختبري فقط")), "a"),
 Q("Low insulin level is:", "مستوى الأنسولين المنخفض:", O(("> 174 pmol/L", "أكثر من 174 بيكومول/لتر"), ("< 2.6 μU/mL (< 18 pmol/L)", "أقل من 2.6 مايكرووحدة/مل (أقل من 18 بيكومول/لتر)"), ("2.6 - 24.9 μU/mL", "2.6 - 24.9"), ("Exactly 18 μU/mL", "18 بالضبط")), "b"),
 Q("The incubation in the insulin ELISA lab is typically:", "الحضن في عملي إليزا الأنسولين عادةً:", O(("10 min at 37 °C", "10 دقائق بدرجة 37"), ("Overnight at 4 °C", "ليلة بدرجة 4"), ("1 hour at room temperature", "ساعة بحرارة الغرفة"), ("5 min boiling", "5 دقائق غليان")), "c"),
 Q("Unbound substances are removed using:", "تُزال المواد غير المرتبطة باستعمال:", O(("Substrate", "الركيزة"), ("Serum", "المصل"), ("Distilled water only", "الماء المقطّر فقط"), ("A wash buffer", "محلول الغسل المنظِّم")), "d"),
 Q("Optical density in insulin ELISA is usually read at:", "تُقرأ الكثافة الضوئية في إليزا الأنسولين عادةً عند:", O(("450 nm", "450 نانومتر"), ("540 nm", "540 نانومتر"), ("340 nm", "340 نانومتر"), ("620 nm", "620 نانومتر")), "a"),
 Q("The instrument used to read the plate is:", "الجهاز المستعمل لقراءة الصفيحة:", O(("Centrifuge", "جهاز الطرد"), ("Microplate reader", "قارئ الصفائح الدقيقة"), ("Microscope", "المجهر"), ("pH meter", "مقياس الحموضة")), "b"),
 Q("Insulin concentration is calculated using:", "يُحسب تركيز الأنسولين باستعمال:", O(("A conversion factor only", "معامل تحويل فقط"), ("The lowest detectable value", "أقل قيمة قابلة للكشف"), ("A standard curve", "منحنى قياسي"), ("Visual comparison", "مقارنة بصرية")), "c"),
 Q("Replicate tests are done to ensure:", "تُجرى الفحوص المكرّرة لضمان:", O(("Calibration", "المعايرة"), ("Sensitivity", "الحساسية"), ("Color change", "تغيّر اللون"), ("Accuracy and precision", "الدقّة والضبط")), "d"),
 {"topic_en": "Picture questions", "topic_ar": "أسئلة الصور"},
 Q("In this figure, insulin and glucagon come from the:", "في هذا الشكل يأتي الأنسولين والغلوكاغون من:", O(("Pancreas", "البنكرياس"), ("Adrenal medulla", "لبّ الكظر"), ("Thyroid", "الدرقية"), ("Posterior pituitary", "النخامية الخلفية")), "a", img="assets/endocrine-axis.jpg", img_h="58mm"),
 Q("According to this figure, insulin:", "حسب هذا الشكل، الأنسولين:", O(("Inhibits glycogen synthesis", "يثبّط تصنيع الغلايكوجين"), ("Inhibits glucose production", "يثبّط إنتاج الكلوكوز"), ("Blocks amino acid absorption", "يمنع امتصاص الأحماض الأمينية"), ("Decreases fat storage", "يقلّل خزن الدهون")), "b", img="assets/insulin-function.jpg", img_h="38mm"),
]
mcq = balance(mcq, 67)

tf = [
 TF("Insulin regulates glucose metabolism.", "ينظّم الأنسولين أيض الكلوكوز.", "T"),
 TF("Insulin is produced by alpha cells of the pancreas.", "يُنتج الأنسولين من خلايا ألفا في البنكرياس.", "F"),
 TF("Insulin supports amino acid absorption.", "يدعم الأنسولين امتصاص الأحماض الأمينية.", "T"),
 TF("Sweating is listed as a symptom in the lecture.", "التعرّق مذكور عرضًا في المحاضرة.", "T"),
 TF("Increased insulin decreases the risk of obesity.", "زيادة الأنسولين تقلّل خطر السمنة.", "F"),
 TF("HPLC is one of the insulin estimation methods.", "HPLC إحدى طرق تقدير الأنسولين.", "T"),
 TF("ELISA uses radioactive labels.", "تستعمل الإليزا وسومًا إشعاعية.", "F"),
 TF("ELISA is more sensitive than RIA.", "الإليزا أكثر حساسية من RIA.", "F"),
 TF("In ELISA insulin in the serum binds to the coated antibody.", "في الإليزا يرتبط أنسولين المصل بالضد المغلِّف.", "T"),
 TF("Fasting insulin above 24.9 μU/mL is normal.", "الأنسولين الصيامي فوق 24.9 مايكرووحدة/مل طبيعي.", "F"),
 TF("Standard insulin solutions are used to generate a standard curve.", "تُستعمل محاليل الأنسولين القياسية لإنشاء منحنى قياسي.", "T"),
 TF("Sensitivity means checking the lowest detectable concentration of insulin.", "الحساسية تعني التحقّق من أقل تركيز قابل للكشف من الأنسولين.", "T"),
]

traps = [
 TR("Beta or alpha cells?", "خلايا بيتا أم ألفا؟", "Insulin = beta cells of the pancreas (glucagon is from alpha cells).", "الأنسولين = خلايا بيتا في البنكرياس (والغلوكاغون من خلايا ألفا)."),
 TR("“Insulin deficiency” symptoms", "أعراض “نقص الأنسولين”", "The lecture lists pallor, shakiness, dizziness, sweating, hunger/nausea, fast heartbeat, fatigue under insulin deficiency — answer with this list if asked “according to the lecture”; physiologically they are hypoglycaemia symptoms.", "المحاضرة تذكر الشحوب والارتجاف والدوخة والتعرّق والجوع/الغثيان وتسارع القلب والإعياء تحت نقص الأنسولين — أجب بهذه القائمة إذا قيل “حسب المحاضرة”؛ وفسيولوجيًا هي أعراض نقص السكر."),
 TR("Two units for the same range", "وحدتان للمدى نفسه", "2.6 - 24.9 μU/mL = 18 - 174 pmol/L. Do not mix them: > 24.9 μU/mL (> 174 pmol/L) high; < 2.6 μU/mL (< 18 pmol/L) low.", "2.6 - 24.9 مايكرووحدة/مل = 18 - 174 بيكومول/لتر. لا تخلط بينهما: > 24.9 (> 174) مرتفع؛ < 2.6 (< 18) منخفض."),
 TR("ELISA vs RIA", "الإليزا مقابل RIA", "ELISA: no radiation, safer, available — but only moderate sensitivity compared to RIA.", "الإليزا: بلا إشعاع، أكثر أمانًا، متوفّرة — لكن حساسيتها متوسّطة مقارنةً بـ RIA."),
 TR("Which wavelength?", "أي طول موجي؟", "Insulin ELISA: usually 450 nm on a microplate reader (Drabkin's Hb was 540 nm on a spectrophotometer).", "إليزا الأنسولين: عادةً 450 نانومتر بقارئ الصفائح (وهيموغلوبين درابكن كان 540 نانومتر بالمطياف)."),
 TR("Calibration vs accuracy", "المعايرة مقابل الدقّة", "Calibration = standard solutions → standard curve; accuracy and precision = replicate tests; sensitivity = lowest detectable concentration.", "المعايرة = محاليل قياسية ← منحنى قياسي؛ الدقّة والضبط = فحوص مكرّرة؛ الحساسية = أقل تركيز قابل للكشف."),
]

important = [
 IM("Define insulin and state why it is estimated.", "عرّف الأنسولين واذكر لماذا يُقدَّر.", "A peptide hormone produced by the beta cells of the pancreas that regulates glucose metabolism and maintains blood sugar levels. It is estimated to diagnose diabetes mellitus (type 1 and type 2) and other metabolic disorders, and to assess insulin resistance, hyperinsulinemia and pancreatic function.", "هرمون ببتيدي تنتجه خلايا بيتا في البنكرياس، ينظّم أيض الكلوكوز ويحافظ على مستويات سكر الدم. ويُقدَّر لتشخيص داء السكري (النوع 1 و2) واضطرابات أيضية أخرى، ولتقييم مقاومة الأنسولين وفرط أنسولين الدم ووظيفة البنكرياس."),
 IM("List the functions of insulin shown in the figure.", "عدّد وظائف الأنسولين المبيّنة في الشكل.", "Inhibits glucose production; facilitates glucose uptake; enhances fat storage; regulates blood sugar levels; supports amino acid absorption; promotes glycogen synthesis.", "يثبّط إنتاج الكلوكوز؛ يسهّل امتصاص الكلوكوز؛ يعزّز خزن الدهون؛ ينظّم مستويات سكر الدم؛ يدعم امتصاص الأحماض الأمينية؛ يعزّز تصنيع الغلايكوجين."),
 IM("What happens when insulin increases?", "ماذا يحدث عندما يزداد الأنسولين؟", "It increases the risk of obesity, type 2 diabetes and cardiovascular disease, and decreases health span and life expectancy.", "يزيد خطر السمنة والسكري النوع 2 وأمراض القلب والأوعية، ويقلّل مدّة الصحّة ومتوسّط العمر المتوقّع."),
 IM("Explain the principle and procedure of insulin ELISA.", "اشرح مبدأ إليزا الأنسولين وطريقتها.", "Principle: an antigen-antibody reaction coupled with an enzyme-catalyzed color change. Procedure: coat microplate with insulin-specific antibodies; add serum (insulin binds); add enzyme-conjugated secondary antibody; add substrate → colored product; measure color with a spectrophotometer. Advantages: no radiation, safer, widely available; disadvantage: moderate sensitivity compared to RIA.", "المبدأ: تفاعل مستضد-ضد مقرون بتغيّر لوني يحفّزه إنزيم. الطريقة: غلّف الصفيحة بأضداد خاصّة بالأنسولين؛ أضف المصل (يرتبط الأنسولين)؛ أضف ضدًّا ثانويًا مقترنًا بإنزيم؛ أضف الركيزة ← ناتج ملوّن؛ قِس اللون بالمطياف. المزايا: بلا إشعاع، أكثر أمانًا، متوفّرة؛ والعيب: حساسية متوسّطة مقارنةً بـ RIA."),
 IM("Give the normal range of insulin and its interpretation.", "اذكر المدى الطبيعي للأنسولين وتفسيره.", "Fasting normal: 2.6 - 24.9 μU/mL (18 - 174 pmol/L). Elevated > 24.9 μU/mL (> 174 pmol/L): insulin resistance and hyperinsulinemia. Low < 2.6 μU/mL (< 18 pmol/L).", "الصيامي الطبيعي: 2.6 - 24.9 مايكرووحدة/مل (18 - 174 بيكومول/لتر). المرتفع > 24.9 (> 174): مقاومة الأنسولين وفرط أنسولين الدم. المنخفض < 2.6 (< 18)."),
 IM("Describe the laboratory steps of estimating insulin by ELISA and its quality control.", "صف خطوات تقدير الأنسولين بالإليزا في المختبر وضبط جودتها.", "Materials: insulin ELISA kit, microplate reader, serum samples or standards, distilled water, pipettes and tips. Steps: prepare reagents; coat wells with antibodies; add serum or standards; incubate 1 h at room temperature; wash with wash buffer; add enzyme-labeled secondary antibody; add substrate; read optical density at ~450 nm; calculate from a standard curve. QC: calibration with standards, sensitivity (lowest detectable concentration), accuracy and precision by replicate tests.", "المواد: عدّة إليزا للأنسولين، قارئ الصفائح، عيّنات مصل أو معايير، ماء مقطّر، ماصّات ورؤوسها. الخطوات: حضّر الكواشف؛ غلّف الحفر بالأضداد؛ أضف المصل أو المعايير؛ احضن ساعة بحرارة الغرفة؛ اغسل بمحلول الغسل؛ أضف الضد الثانوي الموسوم بالإنزيم؛ أضف الركيزة؛ اقرأ الكثافة الضوئية عند ~450 نانومتر؛ احسب من المنحنى القياسي. ضبط الجودة: المعايرة بالمعايير، الحساسية (أقل تركيز قابل للكشف)، الدقّة والضبط بالفحوص المكرّرة."),
]

meta = {"subject_en": "Practical Endocrinology", "subject_ar": "الغدد الصماء العملي", "short_ar": "غدد صماء", "instructor": "م.م. نور إبراهيم جليل",
        "unit_en": "Lab 4", "unit_ar": "العملي 4", "unit_label": "LAB", "unit_no": "4",
        "title_en": "Insulin", "title_ar": "الأنسولين",
        "kind": "Laboratories — عملي", "stage": "The third stage — الثالثة"}
save("endocrine-lab4-insulin", meta, blocks, mcq, tf, traps, important)

```
