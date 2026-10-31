---
source: BIOS-Obsidian/tools/scripts/gh/ghq.py
handouts: [clinbiochem-lab3-growth-hormone]
saved: 2026-10-31
tags: [bios, code]
---
# gh/ghq.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#clinbiochem-lab3-growth-hormone|clinbiochem-lab3-growth-hormone]]

```python
mcq = [
 {"topic_en": "Growth hormone", "topic_ar": "هرمون النمو"},
 Q("Growth hormone is a peptide hormone of:", "هرمون النمو هرمون ببتيدي من:", O(("191 amino acids", "191 حمضًا أمينيًا"), ("51 amino acids", "51 حمضًا أمينيًا"), ("9 amino acids", "9 أحماض أمينية"), ("500 amino acids", "500 حمض أميني")), "a"),
 Q("GH is secreted by somatotrophs of the:", "يُفرَز GH من الخلايا المولّدة للنمو في:", O(("Posterior pituitary", "النخامية الخلفية"), ("Anterior pituitary", "النخامية الأمامية"), ("Hypothalamus", "الوطاء"), ("Liver", "الكبد")), "b"),
 Q("GH secretion is stimulated by all EXCEPT:", "يُحفَّز إفراز GH بكل ما يأتي ما عدا:", O(("Exercise", "التمارين"), ("Onset of deep sleep", "بداية النوم العميق"), ("High plasma glucose", "ارتفاع كلوكوز البلازما"), ("Falling plasma glucose after meals", "انخفاض الكلوكوز بعد الوجبات")), "c"),
 Q("In the figure, the hypothalamic hormone that inhibits GH is:", "في الشكل، الهرمون الوطائي الذي يثبّط GH هو:", O(("GHRH", "GHRH"), ("Ghrelin", "الغريلين"), ("IGF-1 stimulation", "تحفيز IGF-1"), ("Somatostatin", "السوماتوستاتين")), "d"),
 Q("GH acts on the liver to produce:", "يعمل GH على الكبد لإنتاج:", O(("IGF-1", "IGF-1"), ("Insulin", "الأنسولين"), ("Glucagon", "الغلوكاغون"), ("Cortisol", "الكورتيزول")), "a"),
 {"topic_en": "Disorders", "topic_ar": "الاضطرابات"},
 Q("Excess GH before epiphyseal plate closure causes:", "زيادة GH قبل انغلاق صفيحة المشاش تسبّب:", O(("Acromegaly", "ضخامة الأطراف"), ("Gigantism", "العملقة"), ("Dwarfism", "القزامة"), ("Diabetes insipidus", "السكري الكاذب")), "b"),
 Q("Acromegaly is excess GH:", "ضخامة الأطراف هي زيادة GH:", O(("In infancy", "في الرضاعة"), ("Before puberty", "قبل البلوغ"), ("After growth plates have closed", "بعد انغلاق صفائح النمو"), ("With low IGF-1", "مع IGF-1 منخفض")), "c"),
 Q("The usual cause of GH excess is:", "السبب المعتاد لزيادة GH:", O(("Liver failure", "فشل الكبد"), ("Hypothalamic dysfunction", "خلل الوطاء"), ("Genetic mutation", "طفرة وراثية"), ("Pituitary adenoma", "ورم غدّي نخامي")), "d"),
 Q("In children, GH deficiency causes:", "عند الأطفال يسبّب نقص GH:", O(("Growth retardation or dwarfism", "تأخّر النمو أو القزامة"), ("Gigantism", "العملقة"), ("Acromegaly", "ضخامة الأطراف"), ("Obesity only", "سمنة فقط")), "a"),
 Q("In adults, GH deficiency may lead to:", "عند البالغين قد يؤدّي نقص GH إلى:", O(("Increased muscle mass", "زيادة الكتلة العضلية"), ("Reduced muscle mass and increased fat deposition", "نقص العضلات وزيادة ترسّب الدهون"), ("Enlarged hands", "تضخّم اليدين"), ("Tall stature", "طول القامة")), "b"),
 {"topic_en": "Diagnostic tests", "topic_ar": "فحوص التشخيص"},
 Q("GH stimulation tests are used to assess:", "تُستعمل فحوص تحفيز GH لتقييم:", O(("GH excess", "زيادة GH"), ("Thyroid function", "وظيفة الدرقية"), ("GH deficiency", "نقص GH"), ("Liver function", "وظيفة الكبد")), "c"),
 Q("GH excess is diagnosed with:", "تُشخَّص زيادة GH بـ:", O(("Insulin tolerance test", "فحص تحمّل الأنسولين"), ("Arginine test", "فحص الأرجنين"), ("Clonidine test", "فحص الكلونيدين"), ("A suppression test (oral glucose tolerance test)", "فحص كبت (تحمّل الكلوكوز الفموي)")), "d"),
 Q("IGF-1 measurement reflects:", "يعكس قياس IGF-1:", O(("Average GH activity", "متوسط نشاط GH"), ("Insulin level", "مستوى الأنسولين"), ("Blood glucose", "سكر الدم"), ("A single GH pulse", "نبضة GH واحدة")), "a"),
 Q("In the ITT, the target blood glucose is:", "في فحص تحمّل الأنسولين يكون كلوكوز الدم المستهدف:", O(("> 200 mg/dL", "أكثر من 200 ملغم/دل"), ("< 40 mg/dL", "أقل من 40 ملغم/دل"), ("100 mg/dL", "100 ملغم/دل"), ("< 70 mg/dL", "أقل من 70 ملغم/دل")), "b"),
 Q("The ITT is contraindicated in patients with:", "يُمنع فحص تحمّل الأنسولين في مرضى:", O(("Obesity", "السمنة"), ("Anemia", "فقر الدم"), ("Seizures or cardiovascular conditions", "الصرع أو أمراض القلب والأوعية"), ("Short stature", "قِصر القامة")), "c"),
 Q("In the arginine test, the dose is:", "في فحص الأرجنين تكون الجرعة:", O(("1 mg IM", "1 ملغم عضليًا"), ("75 g orally", "75 غ فمويًا"), ("0.15 mg/m² orally", "0.15 ملغم/م² فمويًا"), ("0.5 g/kg IV, maximum 30 g", "0.5 غ/كغم وريديًا بحدّ أقصى 30 غ")), "d"),
 Q("Arginine should NOT be given to patients with:", "يجب ألّا يُعطى الأرجنين لمرضى:", O(("Renal, hepatic or acid-base disorders or DM", "اضطرابات الكلى أو الكبد أو الحامضية أو السكري"), ("Short stature", "قِصر القامة"), ("Hypertension only", "ارتفاع الضغط فقط"), ("Anemia", "فقر الدم")), "a"),
 Q("Clonidine is given:", "يُعطى الكلونيدين:", O(("Intravenously 0.5 g/kg", "وريديًا 0.5 غ/كغم"), ("Orally 0.15 mg/m² body surface area", "فمويًا 0.15 ملغم/م² من مساحة سطح الجسم"), ("Intramuscularly 1 mg", "عضليًا 1 ملغم"), ("As 75 g drink", "شرابًا 75 غ")), "b"),
 Q("Side effects of the clonidine test are:", "الآثار الجانبية لفحص الكلونيدين:", O(("Nausea and vomiting", "غثيان وتقيّؤ"), ("Hyperglycemia", "ارتفاع السكر"), ("Drowsiness and hypotension", "النعاس وانخفاض الضغط"), ("Seizures", "الصرع")), "c"),
 Q("Glucagon in the stimulation test is given:", "يُعطى الغلوكاغون في فحص التحفيز:", O(("Orally", "فمويًا"), ("Intravenously as infusion", "وريديًا بالتسريب"), ("Subcutaneously 75 g", "تحت الجلد 75 غ"), ("Intramuscularly", "في العضل")), "d"),
 Q("In the glucagon test, a normal peak GH in adults is:", "في فحص الغلوكاغون تكون ذروة GH الطبيعية عند البالغين:", O(("> 3 ng/mL", "أكثر من 3 نانوغرام/مل"), ("> 10 ng/mL", "أكثر من 10 نانوغرام/مل"), ("< 1 ng/mL", "أقل من 1 نانوغرام/مل"), ("> 50 ng/mL", "أكثر من 50 نانوغرام/مل")), "a"),
 Q("A normal peak GH in children after stimulation is:", "ذروة GH الطبيعية عند الأطفال بعد التحفيز:", O(("< 1 ng/mL", "أقل من 1 نانوغرام/مل"), ("> 10 ng/mL", "أكثر من 10 نانوغرام/مل"), ("0.4 ng/mL", "0.4 نانوغرام/مل"), ("2 ng/mL", "2 نانوغرام/مل")), "b"),
 {"topic_en": "Reference values and GH excess", "topic_ar": "القيم المرجعية وزيادة GH"},
 Q("Basal GH in adults is:", "GH الأساسي عند البالغين:", O(("0-5 ng/mL", "0-5 نانوغرام/مل"), ("10-20 ng/mL", "10-20 نانوغرام/مل"), ("< 1 ng/mL", "أقل من 1 نانوغرام/مل"), ("> 10 ng/mL", "أكثر من 10 نانوغرام/مل")), "c"),
 Q("Newborns have higher basal GH (up to 10-20 ng/mL) because of:", "لحديثي الولادة GH أساسي أعلى (حتى 10-20) بسبب:", O(("Acromegaly", "ضخامة الأطراف"), ("Pituitary adenoma", "ورم نخامي"), ("Feeding", "الرضاعة"), ("Stress during birth", "إجهاد الولادة")), "d"),
 Q("Random GH measurements are often not diagnostic because of:", "قياسات GH العشوائية غالبًا غير تشخيصية بسبب:", O(("Episodic secretion and a short half-life", "الإفراز النوبي وقصر عمر النصف"), ("Long half-life", "طول عمر النصف"), ("Constant secretion", "الإفراز الثابت"), ("Binding to albumin", "الارتباط بالألبومين")), "a"),
 Q("The more sensitive imaging for the pituitary is:", "التصوير الأكثر حساسية للنخامية:", O(("CT", "المقطعي"), ("MRI", "الرنين المغناطيسي"), ("X-ray", "الأشعة السينية"), ("Ultrasound", "الأمواج فوق الصوتية")), "b"),
 Q("A random GH below 0.5 μg/L with normal IGF-1:", "GH عشوائي أقل من 0.5 مايكروغرام/لتر مع IGF-1 طبيعي:", O(("Confirms acromegaly", "يؤكّد ضخامة الأطراف"), ("Means GH deficiency", "يعني نقص GH"), ("Essentially excludes acromegaly", "يستبعد عمليًا ضخامة الأطراف"), ("Needs ITT", "يحتاج فحص الأنسولين")), "c"),
 Q("The ‘gold standard’ for diagnosis of acromegaly is:", "‘المعيار الذهبي’ لتشخيص ضخامة الأطراف:", O(("Random GH", "GH العشوائي"), ("Insulin tolerance test", "فحص تحمّل الأنسولين"), ("CT scan", "التصوير المقطعي"), ("Glucose suppression test", "فحص الكبت بالكلوكوز")), "d"),
 Q("In the glucose suppression test, the glucose load is:", "في فحص الكبت يكون حمل الكلوكوز:", O(("75 g in about 300 mL water", "75 غ في نحو 300 مل ماء"), ("50 g in 100 mL", "50 غ في 100 مل"), ("100 g IV", "100 غ وريديًا"), ("1 mg/kg", "1 ملغم/كغم")), "a"),
 Q("In normal subjects after the glucose load, plasma GH falls to:", "في الطبيعيين بعد حمل الكلوكوز ينخفض GH إلى:", O(("> 10 μg/L", "أكثر من 10 مايكروغرام/لتر"), ("< 0.5 μg/L", "أقل من 0.5 مايكروغرام/لتر"), ("5 μg/L", "5 مايكروغرام/لتر"), ("Zero exactly", "صفر بالضبط")), "b"),
 Q("In acromegaly after a glucose load, GH:", "في ضخامة الأطراف بعد حمل الكلوكوز يكون GH:", O(("Falls below 0.5 μg/L", "ينخفض تحت 0.5"), ("Falls to zero", "ينخفض إلى صفر"), ("Does not fall and may increase in about 30%", "لا ينخفض وقد يرتفع في نحو 30%"), ("Doubles in all patients", "يتضاعف في كل المرضى")), "c"),
 {"topic_en": "Picture questions", "topic_ar": "أسئلة الصور"},
 Q("In this figure, the factor marked (−) that comes from the liver and feeds back on GH is:", "في هذا الشكل، العامل المؤشَّر (−) الآتي من الكبد والذي يعمل تغذية راجعة على GH:", O(("Ghrelin", "الغريلين"), ("GHRH", "GHRH"), ("Glucose uptake", "امتصاص الكلوكوز"), ("IGF-1", "IGF-1")), "d", img="assets/gh-regulation-1.jpg", img_h="46mm"),
 Q("These enlarged hands are typical of:", "هذه اليدان المتضخّمتان نموذجيتان لـ:", O(("Acromegaly", "ضخامة الأطراف"), ("Dwarfism", "القزامة"), ("GH deficiency in adults", "نقص GH عند البالغين"), ("Hypoglycemia", "نقص السكر")), "a", img="assets/acromegaly-hands.jpg", img_h="34mm"),
]
mcq = balance(mcq, 61)

tf = [
 TF("GH stimulates the growth of essentially all tissues including bone.", "يحفّز GH نموّ كل الأنسجة تقريبًا ومنها العظم.", "T"),
 TF("Outside stimulation periods, plasma GH is usually high in children.", "خارج فترات التحفيز يكون GH في البلازما مرتفعًا عادةً عند الأطفال.", "F"),
 TF("Ghrelin stimulates GH secretion.", "يحفّز الغريلين إفراز GH.", "T"),
 TF("Gigantism occurs after growth plates have closed.", "تحدث العملقة بعد انغلاق صفائح النمو.", "F"),
 TF("GH deficiency may be caused by hypothalamic dysfunction.", "قد ينتج نقص GH عن خلل الوطاء.", "T"),
 TF("In the ITT insulin is given orally.", "في فحص تحمّل الأنسولين يُعطى الأنسولين فمويًا.", "F"),
 TF("The ITT requires close monitoring to prevent severe hypoglycemia.", "يحتاج فحص تحمّل الأنسولين مراقبة دقيقة لمنع نقص السكر الشديد.", "T"),
 TF("Clonidine stimulates GH secretion via the hypothalamus.", "يحفّز الكلونيدين إفراز GH عبر الوطاء.", "T"),
 TF("In the glucagon test samples are taken up to 180 minutes.", "في فحص الغلوكاغون تؤخذ العيّنات حتى 180 دقيقة.", "T"),
 TF("Some labs use 4.1-10 ng/mL as the adult cutoff after stimulation.", "بعض المختبرات تستعمل 4.1-10 نانوغرام/مل حدًّا للبالغين بعد التحفيز.", "T"),
 TF("Reference ranges for IGF-1 are the same for all ages.", "المديات المرجعية لـ IGF-1 واحدة لكل الأعمار.", "F"),
 TF("CT is more sensitive than MRI for the pituitary.", "التصوير المقطعي أكثر حساسية من الرنين للنخامية.", "F"),
 TF("In the glucose suppression test basal samples are taken at least 30 min after inserting the cannula.", "في فحص الكبت تؤخذ العيّنات الأساسية بعد 30 دقيقة على الأقل من إدخال الكانيولا.", "T"),
]

traps = [
 TR("Stimulation or suppression?", "تحفيز أم كبت؟", "Deficiency → stimulation tests (insulin, arginine, clonidine, glucagon). Excess → suppression test (glucose).", "النقص ← فحوص التحفيز (الأنسولين، الأرجنين، الكلونيدين، الغلوكاغون). الزيادة ← فحص الكبت (الكلوكوز)."),
 TR("Gigantism vs acromegaly", "العملقة مقابل ضخامة الأطراف", "Same excess GH: gigantism before epiphyseal closure (children), acromegaly after closure (adults).", "زيادة GH نفسها: العملقة قبل انغلاق المشاش (الأطفال)، وضخامة الأطراف بعد الانغلاق (البالغون)."),
 TR("Adult cutoffs differ by test", "حدود البالغين تختلف حسب الفحص", "ITT and arginine: > 5 ng/mL; glucagon: > 3 ng/mL; clonidine: only the child value (> 10) is given.", "الأنسولين والأرجنين: > 5 نانوغرام/مل؛ الغلوكاغون: > 3؛ الكلونيدين: تُذكر قيمة الأطفال فقط (> 10)."),
 TR("Routes and doses", "الطرق والجرعات", "Insulin IV; arginine IV 0.5 g/kg (max 30 g); clonidine oral 0.15 mg/m²; glucagon IM 1 mg (children) or 1-1.5 mg (adults); glucose 75 g oral.", "الأنسولين وريدي؛ الأرجنين وريدي 0.5 غ/كغم (أقصى 30 غ)؛ الكلونيدين فموي 0.15 ملغم/م²؛ الغلوكاغون عضلي 1 ملغم (أطفال) أو 1-1.5 ملغم (بالغون)؛ الكلوكوز 75 غ فمويًا."),
 TR("Which side effects?", "أي آثار جانبية؟", "ITT: severe hypoglycemia (not with seizures, heart disease). Clonidine: drowsiness, hypotension. Glucagon: nausea, vomiting, hypoglycemia. Arginine: avoid in renal, hepatic, acid-base disorders, DM.", "الأنسولين: نقص سكر شديد (ليس مع الصرع وأمراض القلب). الكلونيدين: نعاس وهبوط ضغط. الغلوكاغون: غثيان وتقيّؤ ونقص سكر. الأرجنين: يُتجنّب في أمراض الكلى والكبد والحامضية والسكري."),
 TR("< 1, < 0.5 or < 0.4?", "< 1 أم < 0.5 أم < 0.4؟", "Basal adult and normal suppressed GH: < 1 ng/mL (ideally < 0.4 in some protocols). Random GH < 0.5 μg/L with normal IGF‐1 excludes acromegaly; after glucose load normal GH < 0.5 μg/L.", "GH الأساسي للبالغ والمكبوت الطبيعي: < 1 نانوغرام/مل (ومثاليًا < 0.4 في بعض البروتوكولات). وGH عشوائي < 0.5 مع IGF‐1 طبيعي يستبعد ضخامة الأطراف؛ وبعد حمل الكلوكوز GH الطبيعي < 0.5."),
]

important = [
 IM("What is growth hormone and what stimulates its secretion?", "ما هرمون النمو وما الذي يحفّز إفرازه؟", "A peptide hormone of 191 amino acids made and secreted by somatotrophs of the anterior pituitary; it stimulates growth of essentially all tissues including bone. Secretion is stimulated by exercise, onset of deep sleep and falling plasma glucose about an hour after meals; otherwise plasma GH is very low or undetectable, especially in children.", "هرمون ببتيدي من 191 حمضًا أمينيًا تصنعه وتفرزه الخلايا المولّدة للنمو في النخامية الأمامية، ويحفّز نموّ كل الأنسجة تقريبًا ومنها العظم. ويُحفَّز إفرازه بالتمارين وبداية النوم العميق وانخفاض كلوكوز البلازما بعد نحو ساعة من الوجبات؛ وفي غير ذلك يكون منخفضًا جدًا أو غير قابل للكشف، خصوصًا عند الأطفال."),
 IM("Describe the disorders of GH excess and deficiency.", "صف اضطرابات زيادة هرمون النمو ونقصه.", "Excess: gigantism in children (before epiphyseal plate closure), acromegaly in adults (enlarged hands, feet, facial features after plate closure), usually due to pituitary adenomas. Deficiency: growth retardation or dwarfism in children; reduced muscle mass, increased fat and poor quality of life in adults; caused by genetic mutations, pituitary damage or hypothalamic dysfunction.", "الزيادة: العملقة عند الأطفال (قبل انغلاق المشاش)، وضخامة الأطراف عند البالغين (تضخّم اليدين والقدمين وملامح الوجه بعد الانغلاق)، وغالبًا بسبب أورام غدّية نخامية. النقص: تأخّر النمو أو القزامة عند الأطفال؛ ونقص العضلات وزيادة الدهون وتدنّي جودة الحياة عند البالغين؛ وسببه طفرات وراثية أو تلف النخامية أو خلل الوطاء."),
 IM("Describe the insulin tolerance test.", "صف فحص تحمّل الأنسولين.", "Purpose: GH release in response to hypoglycemia. Overnight fast; baseline glucose and GH; IV insulin to bring glucose below 40 mg/dL; samples at 0, 30, 60, 90 and 120 min for GH. Normal peak GH > 10 ng/mL in children or > 5 ng/mL in adults. Needs close monitoring for severe hypoglycemia; contraindicated in seizures or cardiovascular conditions.", "الغرض: إفراز GH استجابةً لنقص السكر. صيام ليلة؛ كلوكوز وGH أساسيان؛ أنسولين وريدي لخفض الكلوكوز تحت 40 ملغم/دل؛ عيّنات عند 0 و30 و60 و90 و120 دقيقة لقياس GH. الذروة الطبيعية > 10 نانوغرام/مل للأطفال أو > 5 للبالغين. يحتاج مراقبة دقيقة لنقص السكر الشديد؛ وممنوع مع الصرع وأمراض القلب والأوعية."),
 IM("Compare the arginine, clonidine and glucagon stimulation tests.", "قارن بين فحوص التحفيز بالأرجنين والكلونيدين والغلوكاغون.", "Arginine: 0.5 g/kg IV (max 30 g), samples 0-120 min, normal > 10 children / > 5 adults; not in renal, hepatic, acid-base disorders or DM. Clonidine: 0.15 mg/m² orally, acts via hypothalamus, samples 0-120 min, normal > 10 in children; drowsiness and hypotension. Glucagon: IM 1 mg children or 1-1.5 mg adults, samples 0-180 min, normal > 10 children / > 3 adults; watch nausea, vomiting, hypoglycemia.", "الأرجنين: 0.5 غ/كغم وريديًا (أقصى 30 غ)، عيّنات 0-120 دقيقة، الطبيعي > 10 أطفال / > 5 بالغون؛ ليس لمرضى الكلى والكبد والحامضية والسكري. الكلونيدين: 0.15 ملغم/م² فمويًا، يعمل عبر الوطاء، عيّنات 0-120، الطبيعي > 10 للأطفال؛ نعاس وهبوط ضغط. الغلوكاغون: عضلي 1 ملغم أطفال أو 1-1.5 ملغم بالغون، عيّنات 0-180، الطبيعي > 10 أطفال / > 3 بالغون؛ راقب الغثيان والتقيّؤ ونقص السكر."),
 IM("Give the reference values of GH.", "اذكر القيم المرجعية لهرمون النمو.", "Basal: adults < 1 ng/mL (often undetectable in daytime due to pulsatile secretion), children 0-5 ng/mL, newborns up to 10-20 ng/mL (birth stress). After stimulation: children > 10 ng/mL, adults > 5 ng/mL (some labs 4.1-10); below these suggests deficiency. Suppressed: normal < 1 ng/mL (ideally < 0.4).", "الأساسي: البالغون < 1 نانوغرام/مل (غالبًا غير قابل للكشف نهارًا بسبب الإفراز النبضي)، الأطفال 0-5، حديثو الولادة حتى 10-20 (إجهاد الولادة). بعد التحفيز: الأطفال > 10، البالغون > 5 (بعض المختبرات 4.1-10)؛ وما دونها يوحي بالنقص. المكبوت: الطبيعي < 1 (مثاليًا < 0.4)."),
 IM("How is GH excess diagnosed? Describe the glucose suppression test.", "كيف تُشخَّص زيادة هرمون النمو؟ صف فحص الكبت بالكلوكوز.", "Suggested by clinical presentation, biochemical tests and pituitary imaging (MRI more sensitive than CT; CT/MRI may find an ectopic GH or GHRH source). Requires GH and IGF‐1; random GH is variable (episodic, short half-life), but random GH < 0.5 μg/L with normal IGF‐1 essentially excludes acromegaly, while raised IGF‐1 needs a glucose test. Gold standard: overnight fast, IV cannula, after ≥ 30 min basal glucose and GH, drink 75 g glucose in ~300 mL water, sample at 30, 60, 90, 120 min. Normal GH falls below 0.5 μg/L; in acromegaly/gigantism it does not fall and may rise in ~30%.", "يُشتبه بها من الصورة السريرية والفحوص الكيموحيوية وتصوير النخامية (الرنين أكثر حساسية من المقطعي؛ وقد يكشفان مصدرًا هاجرًا لـ GH أو GHRH). وتتطلّب قياس GH وIGF‐1؛ وGH العشوائي متباين (نوبي، عمر نصف قصير)، لكن GH عشوائي < 0.5 مع IGF‐1 طبيعي يستبعد ضخامة الأطراف، وارتفاع IGF‐1 يحتاج فحص الكلوكوز. المعيار الذهبي: صيام ليلة، كانيولا وريدية، بعد ≥ 30 دقيقة كلوكوز وGH أساسيان، شرب 75 غ كلوكوز في ~300 مل ماء، وعيّنات عند 30 و60 و90 و120 دقيقة. في الطبيعي ينخفض GH تحت 0.5؛ وفي ضخامة الأطراف/العملقة لا ينخفض وقد يرتفع في نحو 30%."),
]

meta = {"subject_en": "Clinical Biochemistry", "subject_ar": "الكيمياء السريرية", "short_ar": "كيمياء سريرية", "instructor": "م.م. نور إبراهيم جليل",
        "unit_en": "Lab 3", "unit_ar": "العملي 3", "unit_label": "LAB", "unit_no": "3",
        "title_en": "Growth hormone", "title_ar": "هرمون النمو",
        "kind": "Laboratories — عملي", "stage": "The third stage — الثالثة"}
save("clinbiochem-lab3-growth-hormone", meta, blocks, mcq, tf, traps, important)

```
