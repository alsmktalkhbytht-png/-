---
source: BIOS-Obsidian/tools/scripts/hem3/l4.py
handouts: [hematology-lec4-hemoglobin]
saved: 2026-10-28
tags: [bios, code]
---
# hem3/l4.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#hematology-lec4-hemoglobin|hematology-lec4-hemoglobin]]

```python
from common import *

blocks = [
 SEC("Hemoglobin", "الهيموغلوبين"),
 C(["The main function of red cells is to **carry O2 to the tissues** and to **return carbon dioxide (CO2)** from the tissues to the lungs.",
    "In orders to achieve the gaseous exchange, they contain the specialized protein called **hemoglobin**."],
   ["الوظيفة الرئيسة للكريات الحمر هي **نقل الأوكسجين إلى الأنسجة** و**إعادة ثاني أوكسيد الكاربون** من الأنسجة إلى الرئتين.",
    "ولتحقيق تبادل الغازات تحتوي على بروتين متخصّص يُسمّى **الهيموغلوبين**."]),
 C("Each red cell contains approximately **640 million** hemoglobin molecules.", "تحتوي كل كرية حمراء على نحو **640 مليون** جزيء هيموغلوبين."),
 C("Each molecules of normal adult hemoglobin (**Hb.A**) which is the dominant hemoglobin in blood **after the age of 3-6 months** consist **four polypeptide chains (2 alpha and 2 beta)** chains and each chain contains **haem** molecule in the center.",
   "يتكوّن كل جزيء من هيموغلوبين البالغين الطبيعي (**`Hb.A`**)، وهو الهيموغلوبين السائد في الدم **بعد عمر 3–6 أشهر**، من **أربع سلاسل ببتيدية متعدّدة (2 ألفا و2 بيتا)**، وتحتوي كل سلسلة على جزيء **هيم** في مركزها."),
 C(["Normal adult blood also contains small quantities of two other hemoglobin, **Hb.F** and **Hb.A2**.",
    "These also contain **α Chains** but with **γ and δ chains** respectively, Instead of β .",
    "Different between two chains is in the **number and sequences of amino acid**."],
   ["ويحتوي دم البالغين الطبيعي أيضًا على كميات صغيرة من نوعين آخرين من الهيموغلوبين: **`Hb.F`** و**`Hb.A2`**.",
    "وهما يحتويان أيضًا على **سلاسل ألفا** لكن مع **سلاسل غاما ودلتا** على التوالي، بدلًا من بيتا.",
    "والفرق بين السلسلتين في **عدد الأحماض الأمينية وتسلسلها**."]),
 C("In normal adults, we have three type of hemoglobin:", "لدى البالغين الطبيعيين ثلاثة أنواع من الهيموغلوبين:"),
 T(["Types of Hb.", "Hb.A", "Hb.F", "Hb.A2"],
   [["Structure", "α2 β2", "α2 γ2", "α2 δ2"], ["Normal %", "96-98%", "0.5-0.8%", "1.5-3.2%"],
    ["البنية بالعربي", "سلسلتا ألفا + سلسلتا بيتا", "سلسلتا ألفا + سلسلتا غاما", "سلسلتا ألفا + سلسلتا دلتا"]],
   key_cols=[0]),
 C("The major **switch from fetal to adult hemoglobin** occurs **3-6 months after birth** when **β. chain synthesis** started.",
   "يحدث **التحوّل الرئيس من الهيموغلوبين الجنيني إلى هيموغلوبين البالغين** بعد **3–6 أشهر من الولادة** عندما يبدأ **تخليق سلسلة بيتا**."),
 C("Hemoglobin abnormalities could result from either:", "قد تنتج تشوّهات الهيموغلوبين عن:",
   list_en=["Synthesis of **abnormal hemoglobin**.", "**Reduced rate of synthesis** of normal α- or β- globin's chains."],
   list_ar=["تخليق **هيموغلوبين غير طبيعي**.", "**انخفاض سرعة تخليق** سلاسل الكلوبين ألفا أو بيتا الطبيعية."]),

 SEC("Haem synthesis", "تخليق الهيم"),
 C(["Haem synthesis occurs largely in the **mitochondria** by a series of biochemical reactions under action of enzymes **δ- amino levulinic acid (ALA) synthase** and **vit.B6** as a coenzyme.",
    "Ultimately, **protoporhyrin combines with iron in the ferrous state** to form haem."],
   ["يحدث تخليق الهيم غالبًا في **المايتوكوندريا** عبر سلسلة تفاعلات كيميائية حيوية بفعل إنزيم **مُخلِّق حمض دلتا-أمينوليفولينيك (`ALA synthase`)** وبوجود **فيتامين `B6`** مرافقًا إنزيميًا.",
    "وفي النهاية **يتّحد البروتوبورفيرين مع الحديد بحالته الحديدوزية** ليكوّن الهيم."]),
 FLOW([("Protoporphyrin", "البروتوبورفيرين"), ("+ Iron (Fe²⁺)", "+ حديد (`Fe²⁺`)"), ("Haem", "الهيم"), ("+ Globin chains", "+ سلاسل الكلوبين"), ("Hemoglobin", "الهيموغلوبين")]),
 VALUES(),
]

mcq = [
 Q("The main function of red cells is to:", "الوظيفة الرئيسة للكريات الحمر:", [("Fight infection", "مقاومة العدوى"), ("Carry O2 to tissues and return CO2 to the lungs", "نقل الأوكسجين للأنسجة وإعادة CO2 للرئتين"), ("Clot blood", "تخثير الدم"), ("Produce antibodies", "إنتاج الأجسام المضادة")], "b"),
 Q("Each red cell contains approximately how many haemoglobin molecules?", "كم جزيء هيموغلوبين في كل كرية حمراء تقريبًا؟", [("640 thousand", "640 ألف"), ("6.4 million", "6.4 مليون"), ("640 million", "640 مليون"), ("64 billion", "64 مليار")], "c"),
 Q("Normal adult haemoglobin (Hb A) consists of:", "يتكوّن هيموغلوبين البالغين (Hb A) من:", [("2 alpha and 2 beta chains", "سلسلتي ألفا وسلسلتي بيتا"), ("2 alpha and 2 gamma chains", "سلسلتي ألفا وسلسلتي غاما"), ("4 beta chains", "أربع سلاسل بيتا"), ("2 alpha and 2 delta chains", "سلسلتي ألفا وسلسلتي دلتا")], "a"),
 Q("Hb F is composed of:", "يتكوّن Hb F من:", [("α2 β2", "α2 β2"), ("α2 δ2", "α2 δ2"), ("β4", "β4"), ("α2 γ2", "α2 γ2")], "d"),
 Q("Hb A2 contains alpha chains with:", "يحتوي Hb A2 على سلاسل ألفا مع:", [("Beta chains", "سلاسل بيتا"), ("Delta chains", "سلاسل دلتا"), ("Gamma chains", "سلاسل غاما"), ("Epsilon chains", "سلاسل إبسيلون")], "b"),
 Q("The normal percentage of Hb A in adults is:", "النسبة الطبيعية لـ Hb A عند البالغين:", [("50–60%", "50–60%"), ("1.5–3.2%", "1.5–3.2%"), ("96–98%", "96–98%"), ("0.5–0.8%", "0.5–0.8%")], "c"),
 Q("The normal percentage of Hb F in adults is:", "النسبة الطبيعية لـ Hb F عند البالغين:", [("0.5–0.8%", "0.5–0.8%"), ("5–10%", "5–10%"), ("96–98%", "96–98%"), ("1.5–3.2%", "1.5–3.2%")], "a"),
 Q("The normal percentage of Hb A2 in adults is:", "النسبة الطبيعية لـ Hb A2 عند البالغين:", [("0.5–0.8%", "0.5–0.8%"), ("10%", "10%"), ("50%", "50%"), ("1.5–3.2%", "1.5–3.2%")], "d"),
 Q("The switch from fetal to adult haemoglobin occurs:", "يحدث التحوّل من الهيموغلوبين الجنيني إلى البالغ:", [("At birth", "عند الولادة"), ("3–6 months after birth", "بعد 3–6 أشهر من الولادة"), ("At puberty", "عند البلوغ"), ("At 2 years", "عند عمر سنتين")], "b"),
 Q("The switch to adult Hb happens when synthesis starts of the:", "يحدث التحوّل إلى Hb البالغين عند بدء تخليق سلسلة:", [("Alpha chain", "ألفا"), ("Gamma chain", "غاما"), ("Beta chain", "بيتا"), ("Delta chain", "دلتا")], "c"),
 Q("The difference between globin chains is in the:", "الفرق بين سلاسل الكلوبين في:", [("Number and sequence of amino acids", "عدد الأحماض الأمينية وتسلسلها"), ("Iron content", "محتوى الحديد"), ("Haem structure", "بنية الهيم"), ("Carbohydrate content", "محتوى الكاربوهيدرات")], "a"),
 Q("Haemoglobin abnormalities result from abnormal Hb synthesis or:", "تنتج تشوّهات الهيموغلوبين عن تخليق Hb غير طبيعي أو:", [("Excess iron", "زيادة الحديد"), ("Increased haem", "زيادة الهيم"), ("Reduced rate of synthesis of normal α or β chains", "انخفاض سرعة تخليق سلاسل ألفا أو بيتا الطبيعية"), ("Low oxygen", "قلّة الأوكسجين")], "c"),
 Q("Haem synthesis occurs largely in the:", "يحدث تخليق الهيم غالبًا في:", [("Nucleus", "النواة"), ("Ribosomes", "الرايبوسومات"), ("Golgi", "جهاز كولجي"), ("Mitochondria", "المايتوكوندريا")], "d"),
 Q("The coenzyme of ALA synthase in haem synthesis is:", "المرافق الإنزيمي لإنزيم ALA synthase في تخليق الهيم:", [("Vitamin B12", "فيتامين B12"), ("Vitamin B6", "فيتامين B6"), ("Folate", "الفولات"), ("Vitamin C", "فيتامين C")], "b"),
 Q("Haem is formed when protoporphyrin combines with:", "يتكوّن الهيم عندما يتّحد البروتوبورفيرين مع:", [("Iron in the ferrous state", "الحديد بالحالة الحديدوزية"), ("Iron in the ferric state", "الحديد بالحالة الحديدية"), ("Copper", "النحاس"), ("Zinc", "الزنك")], "a"),
 Q("The normal red cell count in males is:", "عدد الكريات الحمر الطبيعي عند الذكور:", [("3.9–5.6 ×10¹²/L", "3.9–5.6"), ("2–3 ×10¹²/L", "2–3"), ("4.5–6.5 ×10¹²/L", "4.5–6.5"), ("8–10 ×10¹²/L", "8–10")], "c"),
 Q("The normal haematocrit in females is:", "الهيماتوكريت الطبيعي عند الإناث:", [("36–48%", "36–48%"), ("40–52%", "40–52%"), ("20–30%", "20–30%"), ("55–65%", "55–65%")], "a"),
 Q("Hb A becomes the dominant haemoglobin after the age of:", "يصبح Hb A الهيموغلوبين السائد بعد عمر:", [("1 week", "أسبوع"), ("1 month", "شهر"), ("10 years", "10 سنوات"), ("3–6 months", "3–6 أشهر")], "d"),
]
tf = [
 TF("Each haemoglobin chain contains a haem molecule in its centre.", "تحتوي كل سلسلة هيموغلوبين على جزيء هيم في مركزها.", "T"),
 TF("Hb A is a tetramer of four polypeptide chains.", "Hb A رباعي من أربع سلاسل ببتيدية.", "T"),
 TF("Hb F contains beta chains.", "يحتوي Hb F على سلاسل بيتا.", "F"),
 TF("All adult haemoglobins contain alpha chains.", "جميع أنواع هيموغلوبين البالغين تحتوي سلاسل ألفا.", "T"),
 TF("Hb A2 is the main haemoglobin of adults.", "Hb A2 هو الهيموغلوبين الرئيس للبالغين.", "F"),
 TF("Beta-chain synthesis starts 3–6 months after birth.", "يبدأ تخليق سلسلة بيتا بعد 3–6 أشهر من الولادة.", "T"),
 TF("Haem synthesis occurs mainly in the cytoplasm.", "يحدث تخليق الهيم أساسًا في السايتوبلازم.", "F"),
 TF("Vitamin B6 is a coenzyme for ALA synthase.", "فيتامين B6 مرافق إنزيمي لـ ALA synthase.", "T"),
 TF("Haem contains iron in the ferric state.", "يحتوي الهيم على الحديد بالحالة الحديدية (Fe³⁺).", "F"),
 TF("Reduced synthesis of normal globin chains can cause a haemoglobin abnormality.", "قد يسبّب انخفاض تخليق سلاسل الكلوبين الطبيعية تشوّهًا في الهيموغلوبين.", "T"),
]
traps = [
 TR("Which chains in each haemoglobin?", "أي السلاسل في كل هيموغلوبين؟", "Hb A α2β2; Hb F α2γ2; Hb A2 α2δ2 — all share alpha chains.", "Hb A α2β2؛ Hb F α2γ2؛ Hb A2 α2δ2 — وكلها تشترك في سلاسل ألفا."),
 TR("Hb F % vs Hb A2 % in adults", "نسبة Hb F مقابل Hb A2 عند البالغين", "Hb F 0.5–0.8% (smaller); Hb A2 1.5–3.2%; Hb A 96–98%.", "Hb F 0.5–0.8% (الأصغر)؛ Hb A2 1.5–3.2%؛ Hb A 96–98%."),
 TR("Ferrous or ferric iron in haem?", "حديد حديدوزي أم حديدي في الهيم؟", "Ferrous (Fe²⁺) iron combines with protoporphyrin.", "الحديد الحديدوزي (Fe²⁺) هو الذي يتّحد مع البروتوبورفيرين."),
 TR("Vitamin for haem synthesis", "الفيتامين اللازم لتخليق الهيم", "Vitamin B6 (coenzyme of ALA synthase) — not B12.", "فيتامين B6 (مرافق ALA synthase) — لا B12."),
 TR("Two causes of haemoglobin abnormality", "سببا تشوّه الهيموغلوبين", "(1) Synthesis of an abnormal haemoglobin; (2) reduced rate of synthesis of normal α or β chains.", "(1) تخليق هيموغلوبين غير طبيعي؛ (2) انخفاض سرعة تخليق سلاسل ألفا أو بيتا الطبيعية."),
]
important = [
 IM("Describe the structure of adult haemoglobin.", "صف بنية هيموغلوبين البالغين.", "Hb A (dominant after 3–6 months) has four polypeptide chains — 2 alpha and 2 beta — each with a haem molecule in its centre; each red cell holds about 640 million Hb molecules.", "يتكوّن Hb A (السائد بعد 3–6 أشهر) من أربع سلاسل — 2 ألفا و2 بيتا — في مركز كل منها جزيء هيم؛ وتحمل كل كرية نحو 640 مليون جزيء."),
 IM("Compare the three normal adult haemoglobins.", "قارن بين أنواع الهيموغلوبين الطبيعية الثلاثة عند البالغين.", "Hb A: α2β2, 96–98%. Hb F: α2γ2, 0.5–0.8%. Hb A2: α2δ2, 1.5–3.2%. Chains differ in the number and sequence of amino acids.", "Hb A: α2β2، 96–98%. Hb F: α2γ2، 0.5–0.8%. Hb A2: α2δ2، 1.5–3.2%. وتختلف السلاسل في عدد الأحماض الأمينية وتسلسلها."),
 IM("Describe haem synthesis.", "صف تخليق الهيم.", "Mostly in the mitochondria through reactions driven by ALA synthase with vitamin B6 as coenzyme; finally protoporphyrin combines with ferrous iron to form haem.", "يحدث غالبًا في المايتوكوندريا بتفاعلات يقودها ALA synthase مع فيتامين B6 مرافقًا؛ وفي النهاية يتّحد البروتوبورفيرين مع الحديد الحديدوزي ليكوّن الهيم."),
 IM("When does the fetal-to-adult switch occur and why?", "متى يحدث التحوّل من الجنيني إلى البالغ ولماذا؟", "3–6 months after birth, when beta-chain synthesis starts.", "بعد 3–6 أشهر من الولادة، عندما يبدأ تخليق سلسلة بيتا."),
 IM("Write the normal adult red cell values.", "اكتب القيم الطبيعية لكريات البالغين الحمر.", "Hb 13.5–17.5 (M) / 11.5–15.5 (F) g/dl; PCV 40–52 / 36–48%; RBC 4.5–6.5 / 3.9–5.6 ×10¹²/L; MCV 80–95 fl; MCH 27–34 pg; MCHC 20–35 g/dl (as in the lecture).", "Hb 13.5–17.5 (ذ) / 11.5–15.5 (إ) غ/دل؛ PCV 40–52 / 36–48%؛ RBC 4.5–6.5 / 3.9–5.6 ×10¹²/L؛ MCV 80–95؛ MCH 27–34؛ MCHC 20–35 (كما في المحاضرة)."),
]
save("hematology-lec4-hemoglobin", 4, "Hemoglobin", "الهيموغلوبين", blocks, mcq, tf, traps, important)

```
