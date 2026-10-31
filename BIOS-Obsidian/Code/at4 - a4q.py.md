---
source: BIOS-Obsidian/tools/scripts/at4/a4q.py
handouts: [advtech-lec4-plasma-urine-proteins]
saved: 2026-10-31
tags: [bios, code]
---
# at4/a4q.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#advtech-lec4-plasma-urine-proteins|advtech-lec4-plasma-urine-proteins]]

```python
mcq = [
 {"topic_en": "Plasma proteins", "topic_ar": "بروتينات البلازما"},
 Q("Total plasma protein is approximately:", "يبلغ بروتين البلازما الكلّي نحو:", O(("6–8 g/dL", "6–8 غ/دل"), ("1–2 g/dL", "1–2 غ/دل"), ("15–20 g/dL", "15–20 غ/دل"), ("< 150 mg/dL", "أقل من 150 ملغم/دل")), "a"),
 Q("Most plasma proteins such as albumin and clotting factors are synthesized in the:", "تُصنَّع معظم بروتينات البلازما مثل الألبومين وعوامل التخثّر في:", O(("Kidney", "الكلية"), ("Liver", "الكبد"), ("Spleen", "الطحال"), ("Bone marrow", "نقي العظم")), "b"),
 Q("Albumin makes up about ___ of total plasma protein:", "يشكّل الألبومين نحو ___ من بروتين البلازما الكلّي:", O(("4%", "4%"), ("35%", "35%"), ("60%", "60%"), ("90%", "90%")), "c"),
 Q("The main protein maintaining oncotic pressure is:", "البروتين الرئيسي الذي يحافظ على الضغط الورمي:", O(("Fibrinogen", "الفايبرينوجين"), ("Transferrin", "الترانسفيرين"), ("Immunoglobulin", "الغلوبيولين المناعي"), ("Albumin", "الألبومين")), "d"),
 Q("Haptoglobin and ceruloplasmin belong to:", "ينتمي الهابتوغلوبين والسيرولوبلازمين إلى:", O(("α2-Globulins", "غلوبيولينات ألفا 2"), ("α1-Globulins", "غلوبيولينات ألفا 1"), ("β-Globulins", "غلوبيولينات بيتا"), ("γ-Globulins", "غلوبيولينات غاما")), "a"),
 Q("α1-antitrypsin is an:", "مضاد التربسين ألفا 1 هو:", O(("α2-Globulin", "غلوبيولين ألفا 2"), ("α1-Globulin", "غلوبيولين ألفا 1"), ("β-Globulin", "غلوبيولين بيتا"), ("γ-Globulin", "غلوبيولين غاما")), "b"),
 Q("Transferrin, complement proteins and lipoproteins are:", "الترانسفيرين وبروتينات المتمّم والبروتينات الدهنية هي:", O(("α1-Globulins", "غلوبيولينات ألفا 1"), ("γ-Globulins", "غلوبيولينات غاما"), ("β-Globulins", "غلوبيولينات بيتا"), ("Albumins", "ألبومينات")), "c"),
 Q("Immunoglobulins (antibodies) are:", "الغلوبيولينات المناعية (الأضداد) هي:", O(("α1-Globulins", "غلوبيولينات ألفا 1"), ("α2-Globulins", "غلوبيولينات ألفا 2"), ("β-Globulins", "غلوبيولينات بيتا"), ("γ-Globulins", "غلوبيولينات غاما")), "d"),
 Q("Fibrinogen forms about ___ of plasma protein:", "يشكّل الفايبرينوجين نحو ___ من بروتين البلازما:", O(("4%", "4%"), ("35%", "35%"), ("60%", "60%"), ("20%", "20%")), "a"),
 Q("Which is NOT a function of plasma proteins?", "أيّ مما يأتي ليس من وظائف بروتينات البلازما؟", O(("Buffering capacity", "القدرة الدارئة"), ("Oxygen production", "إنتاج الأكسجين"), ("Coagulation", "التخثّر"), ("Nutrient reservoir", "مخزون غذائي")), "b"),
 Q("Hypoproteinemia may be caused by all EXCEPT:", "قد ينتج نقص بروتينات الدم عن كل ما يأتي ما عدا:", O(("Liver disease", "أمراض الكبد"), ("Nephrotic syndrome", "المتلازمة الكلوية"), ("Dehydration", "الجفاف"), ("Malnutrition", "سوء التغذية")), "c"),
 Q("Hyperproteinemia is often caused by:", "زيادة بروتينات الدم سببها غالبًا:", O(("Protein-losing enteropathy", "اعتلال الأمعاء المفقد للبروتين"), ("Liver cirrhosis", "تشمّع الكبد"), ("Malnutrition", "سوء التغذية"), ("Dehydration or multiple myeloma", "الجفاف أو الورم النقوي المتعدّد")), "d"),
 Q("SPEP separates plasma proteins into the bands:", "يفصل SPEP بروتينات البلازما إلى الحزم:", O(("Albumin, α1, α2, β, γ", "الألبومين، ألفا 1، ألفا 2، بيتا، غاما"), ("A, B, AB, O", "A، B، AB، O"), ("IgA, IgG, IgM only", "IgA، IgG، IgM فقط"), ("Fibrin and plasmin", "الفايبرين والبلازمين")), "a"),
 {"topic_en": "Urine proteins and proteinuria", "topic_ar": "بروتينات الإدرار والبيلة البروتينية"},
 Q("Normal daily urinary protein excretion is:", "الإطراح اليومي الطبيعي لبروتين الإدرار:", O(("> 3 g/day", "أكثر من 3 غ/يوم"), ("< 150 mg/day", "أقل من 150 ملغم/يوم"), ("6–8 g/dL", "6–8 غ/دل"), ("Zero", "صفر")), "b"),
 Q("The most abundant protein in normal urine is:", "أكثر البروتينات وفرةً في الإدرار الطبيعي:", O(("Albumin", "الألبومين"), ("β2-microglobulin", "بيتا 2 مايكروغلوبيولين"), ("Tamm-Horsfall protein (uromodulin)", "بروتين تام-هورسفول (اليوروموديولين)"), ("Bence Jones protein", "بروتين بنس جونز")), "c"),
 Q("Uromodulin is produced by tubular cells of the:", "يُنتج اليوروموديولين من الخلايا النبيبية في:", O(("Proximal tubule", "النبيب القريب"), ("Collecting duct", "القناة الجامعة"), ("Glomerulus", "الكبيبة"), ("Thick ascending limb of Henle’s loop", "الطرف الصاعد السميك لعروة هنلي")), "d"),
 Q("Uromodulin plays a role in:", "لليوروموديولين دور في:", O(("Defense against UTIs and prevention of kidney stones", "الدفاع ضد التهابات المسالك البولية ومنع حصى الكلى"), ("Blood clotting", "تخثّر الدم"), ("Oxygen transport", "نقل الأكسجين"), ("Iron storage", "خزن الحديد")), "a"),
 Q("The glomerular barrier prevents passage of:", "يمنع الحاجز الكبيبي مرور:", O(("Water", "الماء"), ("Large or negatively charged proteins like albumin", "البروتينات الكبيرة أو السالبة الشحنة مثل الألبومين"), ("Glucose", "الكلوكوز"), ("Small peptides", "الببتيدات الصغيرة")), "b"),
 Q("Low molecular weight filtered proteins are reabsorbed by the:", "تُعاد امتصاص البروتينات المرشّحة منخفضة الوزن الجزيئي بواسطة:", O(("Bladder", "المثانة"), ("Glomerulus", "الكبيبة"), ("Proximal tubules", "النبيبات القريبة"), ("Ureter", "الحالب")), "c"),
 Q("Proteinuria is urinary protein loss of more than:", "البيلة البروتينية هي فقدان بروتين في الإدرار أكثر من:", O(("15 mg/day", "15 ملغم/يوم"), ("1 g/dL", "1 غ/دل"), ("6 g/day", "6 غ/يوم"), ("150 mg/day", "150 ملغم/يوم")), "d"),
 Q("Glomerular proteinuria is predominantly:", "البيلة البروتينية الكبيبية غالبًا:", O(("Albumin", "ألبومين"), ("β2-microglobulin", "بيتا 2 مايكروغلوبيولين"), ("Bence Jones protein", "بروتين بنس جونز"), ("Uromodulin", "يوروموديولين")), "a"),
 Q("β2-microglobulin in urine suggests:", "وجود بيتا 2 مايكروغلوبيولين في الإدرار يوحي بـ:", O(("Glomerular proteinuria", "بيلة بروتينية كبيبية"), ("Tubular proteinuria", "بيلة بروتينية نبيبية"), ("Postrenal proteinuria", "بيلة بروتينية بعد كلوية"), ("Normal urine", "إدرار طبيعي")), "b"),
 Q("Bence Jones proteins in multiple myeloma cause:", "تسبّب بروتينات بنس جونز في الورم النقوي المتعدّد:", O(("Glomerular proteinuria", "بيلة بروتينية كبيبية"), ("Tubular proteinuria", "بيلة بروتينية نبيبية"), ("Overflow proteinuria", "بيلة بروتينية فائضة"), ("Postrenal proteinuria", "بيلة بروتينية بعد كلوية")), "c"),
 Q("Proteinuria from urinary tract infection or bleeding is:", "البيلة البروتينية الناتجة عن التهاب أو نزف في المسالك البولية:", O(("Glomerular", "كبيبية"), ("Tubular", "نبيبية"), ("Overflow", "فائضة"), ("Postrenal", "بعد كلوية")), "d"),
 Q("The gold standard for measuring urine protein is:", "المعيار الذهبي لقياس بروتين الإدرار:", O(("24-hour urine protein estimation", "تقدير بروتين إدرار 24 ساعة"), ("Dipstick", "الشريط"), ("Spot protein/creatinine ratio", "نسبة البروتين/الكرياتينين العشوائية"), ("Microscopy", "الفحص المجهري")), "a"),
 Q("The urine dipstick detects mainly:", "يكشف شريط الإدرار غالبًا:", O(("Light chains", "السلاسل الخفيفة"), ("Albumin", "الألبومين"), ("β2-microglobulin", "بيتا 2 مايكروغلوبيولين"), ("Uromodulin", "اليوروموديولين")), "b"),
 Q("Monoclonal light chains in urine are identified by:", "تُحدَّد السلاسل الخفيفة وحيدة النسيلة في الإدرار بـ:", O(("Dipstick", "الشريط"), ("24-hour volume", "حجم 24 ساعة"), ("Electrophoresis & immunofixation", "الترحيل الكهربائي والتثبيت المناعي"), ("Creatinine ratio", "نسبة الكرياتينين")), "c"),
]
mcq = balance(mcq, 29)

tf = [
 TF("Immunoglobulins are synthesized mainly in the liver.", "تُصنَّع الغلوبيولينات المناعية بصورة رئيسية في الكبد.", "F"),
 TF("Albumin carries hormones, fatty acids, bilirubin and drugs.", "ينقل الألبومين الهرمونات والأحماض الدهنية والبيليروبين والأدوية.", "T"),
 TF("Albumin acts as an antioxidant.", "يعمل الألبومين مضادًا للأكسدة.", "T"),
 TF("Fibrinogen is converted to fibrin during coagulation.", "يتحوّل الفايبرينوجين إلى فايبرين أثناء التخثّر.", "T"),
 TF("Globulins form about 60% of plasma protein.", "تشكّل الغلوبيولينات نحو 60% من بروتين البلازما.", "F"),
 TF("Plasma proteins help regulate blood pH.", "تساعد بروتينات البلازما في تنظيم الأس الهيدروجيني للدم.", "T"),
 TF("Abnormal SPEP patterns help diagnose liver cirrhosis.", "تساعد أنماط SPEP غير الطبيعية في تشخيص تشمّع الكبد.", "T"),
 TF("Normal urine contains no protein at all.", "لا يحتوي الإدرار الطبيعي على أي بروتين.", "F"),
 TF("Tubular secretion adds uromodulin to urine.", "يضيف الإفراز النبيبي اليوروموديولين إلى الإدرار.", "T"),
 TF("Tubular proteinuria is caused by increased glomerular permeability.", "تنتج البيلة البروتينية النبيبية عن زيادة نفاذية الكبيبة.", "F"),
 TF("In overflow proteinuria the protein load exceeds the reabsorptive capacity.", "في البيلة البروتينية الفائضة يتجاوز حمل البروتين قدرة إعادة الامتصاص.", "T"),
 TF("The dipstick test is fully quantitative.", "فحص الشريط كمّي بالكامل.", "F"),
 TF("Plasma proteins reflect liver function, nutritional state and immune activity.", "تعكس بروتينات البلازما وظيفة الكبد والحالة الغذائية والنشاط المناعي.", "T"),
]

traps = [
 TR("Units: g/dL vs mg/day", "الوحدات: غ/دل مقابل ملغم/يوم", "Plasma protein is a concentration (6–8 g/dL); urine protein is a daily amount (< 150 mg/day).", "بروتين البلازما تركيز (6–8 غ/دل)؛ وبروتين الإدرار كمية يومية (أقل من 150 ملغم/يوم)."),
 TR("Most abundant protein — plasma vs urine", "أكثر البروتينات وفرةً — البلازما مقابل الإدرار", "Plasma: albumin (~60%). Normal urine: Tamm-Horsfall protein (uromodulin), with only trace albumin.", "البلازما: الألبومين (نحو 60%). الإدرار الطبيعي: بروتين تام-هورسفول (اليوروموديولين) مع آثار فقط من الألبومين."),
 TR("Which globulin?", "أي غلوبيولين؟", "α1: α1-antitrypsin, α1-acid glycoprotein. α2: haptoglobin, ceruloplasmin, α2-macroglobulin. β: transferrin, complement, lipoproteins. γ: immunoglobulins.", "ألفا 1: مضاد التربسين ألفا 1، البروتين السكري الحامضي. ألفا 2: الهابتوغلوبين، السيرولوبلازمين، الغلوبيولين الكبروي. بيتا: الترانسفيرين، المتمّم، البروتينات الدهنية. غاما: الغلوبيولينات المناعية."),
 TR("Nephrotic syndrome appears twice", "المتلازمة الكلوية تظهر مرّتين", "It causes hypoproteinemia in plasma and glomerular proteinuria (albumin) in urine — the same protein lost.", "تسبّب نقص بروتينات البلازما وبيلة بروتينية كبيبية (ألبومين) في الإدرار — البروتين نفسه يُفقد."),
 TR("Multiple myeloma appears twice", "الورم النقوي يظهر مرّتين", "Plasma: hyperproteinemia (monoclonal gammopathy). Urine: overflow proteinuria with Bence Jones light chains.", "البلازما: زيادة البروتين (اعتلال غاما وحيد النسيلة). الإدرار: بيلة بروتينية فائضة بسلاسل بنس جونز الخفيفة."),
 TR("Gold standard vs convenient", "المعيار الذهبي مقابل البديل المريح", "24-hour urine protein = gold standard; spot protein-to-creatinine ratio = convenient alternative; dipstick = mainly albumin, semi-quantitative.", "إدرار 24 ساعة = المعيار الذهبي؛ نسبة البروتين/الكرياتينين العشوائية = بديل مريح؛ الشريط = ألبومين غالبًا، شبه كمّي."),
]

important = [
 IM("List the major classes of plasma proteins with their percentages and examples.", "عدّد الأصناف الرئيسية لبروتينات البلازما مع نسبها وأمثلتها.", "Albumin (~60%): oncotic pressure, carrier, antioxidant. Globulins (~35%): α1 (α1-antitrypsin, α1-acid glycoprotein), α2 (haptoglobin, ceruloplasmin, α2-macroglobulin), β (transferrin, complement, lipoproteins), γ (immunoglobulins). Fibrinogen (~4%): clotting factor converted to fibrin.", "الألبومين (نحو 60%): ضغط ورمي، ناقل، مضاد أكسدة. الغلوبيولينات (نحو 35%): ألفا 1 (مضاد التربسين، البروتين السكري الحامضي)، ألفا 2 (الهابتوغلوبين، السيرولوبلازمين، الغلوبيولين الكبروي)، بيتا (الترانسفيرين، المتمّم، البروتينات الدهنية)، غاما (الغلوبيولينات المناعية). الفايبرينوجين (نحو 4%): عامل تخثّر يتحوّل إلى فايبرين."),
 IM("What are the functions of plasma proteins?", "ما وظائف بروتينات البلازما؟", "Maintenance of osmotic balance; transport (albumin, transferrin); buffering (blood pH); immune defense (immunoglobulins, complement); coagulation (clotting factors); nutrient reservoir.", "الحفاظ على التوازن التناضحي؛ النقل (الألبومين، الترانسفيرين)؛ الدارئة (الأس الهيدروجيني للدم)؛ الدفاع المناعي (الغلوبيولينات المناعية، المتمّم)؛ التخثّر (عوامل التخثّر)؛ مخزون غذائي."),
 IM("Give the causes of hypo- and hyperproteinemia and the diagnostic tool.", "اذكر أسباب نقص وزيادة بروتينات الدم وأداة التشخيص.", "Hypoproteinemia: liver disease, malnutrition, nephrotic syndrome, protein-losing enteropathy. Hyperproteinemia: dehydration, monoclonal gammopathies (multiple myeloma). Tool: serum protein electrophoresis (albumin, α1, α2, β, γ bands); abnormal patterns help diagnose multiple myeloma or liver cirrhosis.", "النقص: أمراض الكبد، سوء التغذية، المتلازمة الكلوية، اعتلال الأمعاء المفقد للبروتين. الزيادة: الجفاف، اعتلالات الغاما وحيدة النسيلة (الورم النقوي). الأداة: الترحيل الكهربائي لبروتينات المصل (حزم الألبومين وألفا 1 وألفا 2 وبيتا وغاما)؛ والأنماط غير الطبيعية تساعد في تشخيص الورم النقوي أو تشمّع الكبد."),
 IM("Write short notes on Tamm-Horsfall protein.", "اكتب ملاحظات قصيرة عن بروتين تام-هورسفول.", "Also called uromodulin; secreted by tubular cells of the thick ascending limb of Henle’s loop; the most abundant protein in normal urine; defends against urinary tract infections and prevents kidney stones.", "يُسمّى أيضًا اليوروموديولين؛ تفرزه الخلايا النبيبية في الطرف الصاعد السميك لعروة هنلي؛ أكثر البروتينات وفرةً في الإدرار الطبيعي؛ يدافع ضد التهابات المسالك البولية ويمنع حصى الكلى."),
 IM("Explain the mechanisms controlling protein filtration in the kidney.", "اشرح الآليات التي تتحكّم بترشيح البروتين في الكلية.", "Glomerular barrier: blocks large or negatively charged proteins like albumin. Tubular reabsorption: proximal tubules reabsorb filtered low molecular weight proteins. Tubular secretion: adds specific proteins such as uromodulin.", "الحاجز الكبيبي: يمنع البروتينات الكبيرة أو السالبة الشحنة مثل الألبومين. إعادة الامتصاص النبيبي: تعيد النبيبات القريبة امتصاص البروتينات المرشّحة منخفضة الوزن الجزيئي. الإفراز النبيبي: يضيف بروتينات معيّنة مثل اليوروموديولين."),
 IM("Classify proteinuria and describe how it is assessed.", "صنّف البيلة البروتينية وصف كيف تُقيَّم.", "Glomerular (increased permeability, mainly albumin — nephrotic syndrome, glomerulonephritis); tubular (defective reabsorption, β2-microglobulin — interstitial nephritis); overflow (load exceeds reabsorption — Bence Jones light chains in multiple myeloma); postrenal (urinary tract infection, bleeding). Assessment: dipstick (mainly albumin, semi-quantitative), 24-hour urine protein (gold standard), spot protein-to-creatinine ratio (convenient), electrophoresis and immunofixation (specific proteins such as monoclonal light chains).", "كبيبية (زيادة النفاذية، ألبومين غالبًا — المتلازمة الكلوية، التهاب الكبيبات)؛ نبيبية (خلل إعادة الامتصاص، بيتا 2 مايكروغلوبيولين — التهاب الكلية الخلالي)؛ فائضة (الحمل يتجاوز إعادة الامتصاص — سلاسل بنس جونز في الورم النقوي)؛ بعد كلوية (التهاب أو نزف في المسالك). التقييم: الشريط (ألبومين غالبًا، شبه كمّي)، بروتين إدرار 24 ساعة (المعيار الذهبي)، نسبة البروتين/الكرياتينين العشوائية (بديل مريح)، الترحيل الكهربائي والتثبيت المناعي (بروتينات معيّنة مثل السلاسل الخفيفة وحيدة النسيلة)."),
]

meta = {"subject_en": "Advanced Techniques", "subject_ar": "التقنيات المتقدمة", "short_ar": "تقنيات متقدمة", "instructor": "د. مصطفى محمود مصطفى",
        "unit_en": "Lecture 4", "unit_ar": "المحاضرة 4", "unit_label": "LEC", "unit_no": "4",
        "title_en": "Proteins in Plasma and Urine", "title_ar": "البروتينات في البلازما والإدرار",
        "kind": "Theory — نظري", "stage": "The third stage — الثالثة"}
save("advtech-lec4-plasma-urine-proteins", meta, blocks, mcq, tf, traps, important)

```
