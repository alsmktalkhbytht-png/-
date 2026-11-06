---
source: BIOS-Obsidian/tools/scripts/pat6/p6q.py
handouts: [pathology-lec6-nephrotic-renal-tumors]
saved: 2026-11-06
tags: [bios, code]
---
# pat6/p6q.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#pathology-lec6-nephrotic-renal-tumors|pathology-lec6-nephrotic-renal-tumors]]

```python
A = lambda f: "assets/" + f
mcq = [
 {"topic_en": "Nephrotic syndrome", "topic_ar": "المتلازمة الكلائية"},
 Q("Nephrotic syndrome is characterized by increased permeability of the:", "تتميّز المتلازمة الكلائية بزيادة نفاذية:", O(("Basement membrane", "الغشاء القاعدي"), ("Collecting duct", "القناة الجامعة"), ("Ureter", "الحالب"), ("Renal capsule", "محفظة الكلية")), "a"),
 Q("The protein mainly lost in nephrotic syndrome is:", "البروتين المفقود أساسًا في المتلازمة الكلائية:", O(("Fibrinogen", "الفايبرينوجين"), ("Albumin", "الألبومين"), ("IgM", "IgM"), ("Haemoglobin", "الهيموغلوبين")), "b"),
 Q("Massive proteinuria in nephrotic syndrome is excretion of more than:", "البيلة البروتينية الهائلة في المتلازمة الكلائية إخراج أكثر من:", O(("150 mg/day", "150 ملغ/يوم"), ("1 g/day", "1 غ/يوم"), ("4 g/day", "4 غ/يوم"), ("40 g/day", "40 غ/يوم")), "c"),
 Q("In nephrotic syndrome, serum albumin is often less than:", "في المتلازمة الكلائية يكون ألبومين المصل غالبًا أقل من:", O(("10 g/100 mL", "10 غ/100 مل"), ("6 g/100 mL", "6 غ/100 مل"), ("5 g/100 mL", "5 غ/100 مل"), ("3 g/100 mL", "3 غ/100 مل")), "d"),
 Q("Generalized edema in nephrotic syndrome results from:", "تنتج الوذمة المعمّمة في المتلازمة الكلائية عن:", O(("Decreased plasma colloid oncotic pressure", "انخفاض الضغط الغرواني للبلازما"), ("Heart failure", "عجز القلب"), ("Increased albumin", "زيادة الألبومين"), ("Haematuria", "البيلة الدموية")), "a"),
 Q("Hyperlipidemia in nephrotic syndrome is caused by:", "سبب فرط شحوم الدم في المتلازمة الكلائية:", O(("Fatty diet only", "الغذاء الدسم فقط"), ("Increased hepatic lipoprotein synthesis", "زيادة تخليق البروتينات الدهنية في الكبد"), ("Renal fat production", "إنتاج الكلية للدهن"), ("Lipiduria", "البيلة الدهنية")), "b"),
 Q("Proteinuria in nephrotic syndrome is:", "البيلة البروتينية في المتلازمة الكلائية:", O(("Accompanied by many red cells", "يرافقها كريات حمر كثيرة"), ("Accompanied by many white cells", "يرافقها كريات بيض كثيرة"), ("Unaccompanied by increased urinary red or white cells", "لا يرافقها زيادة الكريات الحمر أو البيض"), ("Always bloody", "دموية دائمًا")), "c"),
 Q("According to Table 13–2, the most common cause of nephrotic syndrome in children is:", "حسب جدول 13–2، أشيع سبب للمتلازمة الكلائية في الأطفال:", O(("Membranous nephropathy", "الاعتلال الغشائي"), ("FSGS", "FSGS"), ("IgA nephropathy", "اعتلال IgA"), ("Minimal-change disease (65%)", "داء التغيّر الأدنى (65%)")), "d"),
 Q("According to Table 13–2, the most common primary cause in adults is:", "حسب جدول 13–2، أشيع سبب أولي في البالغين:", O(("Focal segmental glomerulosclerosis (35%)", "التصلّب الكبيبي البؤري القطعي (35%)"), ("Minimal change (10%)", "التغيّر الأدنى (10%)"), ("MPGN (10%)", "الغشائي التكاثري (10%)"), ("IgA (15%)", "IgA (15%)")), "a"),
 Q("Systemic disease causes about what percentage of nephrotic syndrome in adults?", "تسبّب الأمراض الجهازية حوالي كم نسبة من المتلازمة الكلائية في البالغين؟", O(("5%", "5%"), ("40%", "40%"), ("95%", "95%"), ("60%", "60%")), "b"),
 {"topic_en": "IgA nephropathy", "topic_ar": "اعتلال IgA"},
 Q("IgA nephropathy is defined by deposition of IgA in the:", "يُعرَّف اعتلال IgA بترسّب IgA في:", O(("Tubules", "النبيبات"), ("Bowman capsule", "محفظة بومان"), ("Mesangium", "المسراق"), ("Renal pelvis", "الحوض الكلوي")), "c"),
 Q("The most common glomerular disease revealed by renal biopsy worldwide is:", "أشيع مرض كبيبي تكشفه خزعة الكلية عالميًا:", O(("Lupus nephritis", "الذئبي"), ("Amyloidosis", "النشواني"), ("Minimal change", "التغيّر الأدنى"), ("IgA nephropathy", "اعتلال IgA")), "d"),
 Q("IgA nephropathy begins with gross hematuria within 1–2 days of:", "يبدأ اعتلال IgA ببيلة دموية عيانية خلال 1–2 يوم من:", O(("A nonspecific upper respiratory tract infection", "عدوى غير نوعية في الجهاز التنفسي العلوي"), ("A fatty meal", "وجبة دسمة"), ("Trauma", "إصابة"), ("Bee sting", "لسعة نحلة")), "a"),
 Q("Henoch-Schönlein purpura differs from IgA nephropathy in that it is:", "تختلف فرفرية هينوخ-شونلاين عن اعتلال IgA بأنها:", O(("Purely renal", "كلوية بحتة"), ("A systemic syndrome (skin, GIT, joints, kidneys)", "متلازمة جهازية (جلد، هضم، مفاصل، كلى)"), ("Without IgA deposits", "بلا ترسّبات IgA"), ("Only in adults", "في البالغين فقط")), "b"),
 Q("Slow progression of IgA nephropathy to chronic renal failure occurs in:", "يحدث تطوّر اعتلال IgA البطيء للفشل المزمن في:", O(("100% within 1 year", "100% خلال سنة"), ("5% over 5 years", "5% خلال 5 سنوات"), ("25% to 50% over 20 years", "25% إلى 50% خلال 20 سنة"), ("None", "لا أحد")), "c"),
 Q("A biopsy finding that indicates worse prognosis in IgA nephropathy is:", "من موجودات الخزعة الدالّة على إنذار أسوأ في اعتلال IgA:", O(("Normal glomeruli", "كبيبات طبيعية"), ("Minimal change", "تغيّر أدنى"), ("No deposits", "لا ترسّبات"), ("Tubulointerstitial fibrosis", "التليّف الخلالي النبيبي")), "d"),
 {"topic_en": "Kidney tumors", "topic_ar": "أورام الكلية"},
 Q("Urothelial carcinoma arises from:", "تنشأ الكارسينوما الظهارية البولية من:", O(("The epithelium of the renal pelvis", "ظهارة الحوض الكلوي"), ("Renal tubules", "النبيبات الكلوية"), ("Embryonic tissue", "النسيج الجنيني"), ("Mesenchymal tissue", "النسيج المتوسطي")), "a"),
 Q("Wilms’ tumor arises from:", "ينشأ ورم ويلمز من:", O(("Renal pelvis", "الحوض الكلوي"), ("Embryonic (primitive metanephric) tissue", "النسيج الجنيني (التالي البدائي)"), ("Mature tubules", "النبيبات الناضجة"), ("Fat", "الدهن")), "b"),
 Q("A renal adenoma is:", "الورم الغدّي الكلوي:", O(("Large and painful", "كبير ومؤلم"), ("Derived from the renal pelvis", "مشتق من الحوض الكلوي"), ("Small, asymptomatic, from renal tubules", "صغير لا عرضي من النبيبات"), ("Malignant", "خبيث")), "c"),
 Q("Angiomyolipoma consists of:", "يتكوّن الورم الوعائي العضلي الشحمي من:", O(("Cartilage and bone", "غضروف وعظم"), ("Epithelial cells only", "خلايا ظهارية فقط"), ("Lymphocytes", "خلايا لمفية"), ("Fat, smooth muscle, and blood vessels", "دهن وعضل أملس وأوعية دموية")), "d"),
 Q("Angiomyolipoma is often associated with:", "يرتبط الورم الوعائي العضلي الشحمي غالبًا بـ:", O(("Tuberous sclerosis", "التصلّب الحدبي"), ("Von Hippel-Lindau", "فون هيبل-لينداو"), ("Smoking", "التدخين"), ("IgA nephropathy", "اعتلال IgA")), "a"),
 Q("Oncocytoma cells have cytoplasm replete with:", "سايتوبلازم خلايا الورم الخلوي الحمضي مملوء بـ:", O(("Glycogen", "الغلايكوجين"), ("Mitochondria", "المايتوكوندريا"), ("Fat", "الدهن"), ("Mucin", "المخاط")), "b"),
 Q("The most common renal malignancy is:", "أشيع خباثة كلوية:", O(("Wilms tumor", "ورم ويلمز"), ("Oncocytoma", "الورم الخلوي الحمضي"), ("Renal cell carcinoma", "كارسينوما الخلايا الكلوية"), ("Adenoma", "الورم الغدّي")), "c"),
 Q("Renal cell carcinoma is associated with deletions in chromosome:", "ترتبط كارسينوما الخلايا الكلوية بحذف في الكروموسوم:", O(("11", "11"), ("21", "21"), ("X", "X"), ("3", "3")), "d"),
 Q("Which is an etiological factor of RCC in women?", "أيّ مما يأتي عامل مسبّب لـ RCC في النساء؟", O(("Obesity and oestrogen therapy", "السمنة والعلاج بالإستروجين"), ("Bee sting", "لسعة النحل"), ("Pregnancy", "الحمل"), ("Breastfeeding", "الرضاعة")), "a"),
 Q("Wilms tumor incidence peaks at:", "تبلغ ذروة ورم ويلمز بعمر:", O(("50–70 years", "50–70 سنة"), ("2–4 years", "2–4 سنوات"), ("Newborn only", "حديث الولادة فقط"), ("20–30 years", "20–30 سنة")), "b"),
 Q("The most common presenting feature of Wilms tumor is:", "أشيع علامة أولى لورم ويلمز:", O(("Purpuric rash", "طفح فرفري"), ("Hypertension only", "ارتفاع الضغط فقط"), ("Palpable flank mass (often huge)", "كتلة خاصرة محسوسة (غالبًا ضخمة)"), ("Jaundice", "اليرقان")), "c"),
 {"topic_en": "Picture questions", "topic_ar": "أسئلة الصور"},
 Q("This rash is typical of:", "هذا الطفح نموذجي لـ:", O(("Wilms tumor", "ورم ويلمز"), ("Nephrotic syndrome", "المتلازمة الكلائية"), ("Oncocytoma", "الورم الخلوي الحمضي"), ("Henoch-Schönlein purpura", "فرفرية هينوخ-شونلاين")), "d", img=A("hsp-rash.jpg"), img_h="36mm"),
 Q("This tumor with vessels, fat and spindle cells is:", "هذا الورم ذو الأوعية والدهن والخلايا المغزلية هو:", O(("Angiomyolipoma", "الورم الوعائي العضلي الشحمي"), ("Adenoma", "الورم الغدّي"), ("Oncocytoma", "الورم الخلوي الحمضي"), ("Urothelial carcinoma", "الكارسينوما الظهارية البولية")), "a", img=A("angiomyolipoma.jpg"), img_h="40mm"),
 Q("This karyotype shows the deletion associated with:", "يُظهر هذا النمط النووي الحذف المرتبط بـ:", O(("Renal cell carcinoma (chromosome 3)", "كارسينوما الخلايا الكلوية (الكروموسوم 3)"), ("Wilms tumor (short arm of chromosome 11)", "ورم ويلمز (الذراع القصير للكروموسوم 11)"), ("Down syndrome", "متلازمة داون"), ("IgA nephropathy", "اعتلال IgA")), "b", img=A("karyotype-del11p.jpg"), img_h="32mm"),
]

tf = [
 TF("In nephrotic syndrome, edema is usually severe according to the definition slide.", "حسب شريحة التعريف، الوذمة في المتلازمة الكلائية عادةً شديدة.", "F"),
 TF("All causes of nephrotic syndrome share a derangement in the glomerular capillary walls.", "تشترك كل أسباب المتلازمة الكلائية في خلل جدران الشعيرات الكبيبية.", "T"),
 TF("Long-standing heavy proteinuria causes a drop in plasma colloid osmotic pressure.", "البيلة البروتينية الشديدة الطويلة تسبّب انخفاض الضغط التناضحي الغرواني للبلازما.", "T"),
 TF("Primary glomerular disease causes about 95% of nephrotic syndrome in children.", "يسبّب المرض الكبيبي الأولي حوالي 95% من المتلازمة الكلائية في الأطفال.", "T"),
 TF("Bee sting allergy is listed as a miscellaneous cause of nephrotic syndrome.", "حساسية لسعة النحل مذكورة سببًا متفرّقًا للمتلازمة الكلائية.", "T"),
 TF("IgA nephropathy usually affects the elderly.", "يصيب اعتلال IgA عادةً كبار السن.", "F"),
 TF("Many patients with IgA nephropathy maintain normal renal function for decades.", "كثير من مرضى اعتلال IgA يحتفظون بوظيفة كلوية طبيعية لعقود.", "T"),
 TF("Henoch-Schönlein purpura is characterized by IgA deposition in the mesangium.", "تتميّز فرفرية هينوخ-شونلاين بترسّب IgA في المسراق.", "T"),
 TF("Angiomyolipoma is a malignant epithelial tumor.", "الورم الوعائي العضلي الشحمي ورم ظهاري خبيث.", "F"),
 TF("Renal cell carcinoma is more common in women.", "كارسينوما الخلايا الكلوية أشيع في النساء.", "F"),
 TF("RCC has a higher incidence in cigarette smokers.", "إصابة RCC أعلى في مدخّني السجائر.", "T"),
 TF("Von Hippel-Lindau disease is caused by alterations in a gene on chromosome 3.", "ينتج داء فون هيبل-لينداو عن تغيّرات في جين على الكروموسوم 3.", "T"),
 TF("Analgesic nephropathy is a risk factor for RCC.", "اعتلال الكلية بالمسكّنات عامل خطورة لـ RCC.", "T"),
 TF("Wilms tumor is the most common renal malignancy of adults.", "ورم ويلمز أشيع خباثة كلوية في البالغين.", "F"),
]

traps = [
 TR("Minimal change or membranous — which leads in children?", "التغيّر الأدنى أم الغشائي — أيّهما الأول في الأطفال؟",
    "Children: minimal-change disease 65% (membranous only 5%); adults: FSGS 35%, membranous 30%.", "الأطفال: التغيّر الأدنى 65% (الغشائي 5% فقط)؛ البالغون: FSGS 35%، الغشائي 30%."),
 TR("Nephrotic urine — red cells or not?", "بول المتلازمة الكلائية — فيه كريات حمر أم لا؟",
    "No — the proteinuria is unaccompanied by increased red or white cells.", "لا — البيلة البروتينية لا يرافقها زيادة الكريات الحمر أو البيض."),
 TR("IgA nephropathy vs HSP?", "اعتلال IgA مقابل HSP؟",
    "Both have mesangial IgA; IgA nephropathy is purely renal, HSP is systemic (skin rash, abdominal pain, arthritis, kidneys).", "كلاهما فيه IgA مسراقي؛ اعتلال IgA كلوي بحت، وHSP جهازي (طفح، ألم بطن، التهاب مفاصل، كلى)."),
 TR("Chromosome 3 or 11?", "الكروموسوم 3 أم 11؟",
    "Chromosome 3 → RCC and von Hippel-Lindau; short arm of chromosome 11 → Wilms tumor.", "الكروموسوم 3 ← RCC وفون هيبل-لينداو؛ الذراع القصير للكروموسوم 11 ← ورم ويلمز."),
 TR("Tuberous sclerosis — which tumors?", "التصلّب الحدبي — أيّ الأورام؟",
    "Angiomyolipoma (benign hamartoma) and it is also a risk factor for RCC.", "الورم الوعائي العضلي الشحمي (عابي حميد)، وهو أيضًا عامل خطورة لـ RCC."),
 TR("Which renal malignancy in a 3-year-old with a huge flank mass?", "أيّ خباثة كلوية في طفل عمره 3 سنوات بكتلة خاصرة ضخمة؟",
    "Wilms tumor (nephroblastoma), peak 2–4 years; RCC is in men aged 50–70.", "ورم ويلمز (الورم الأرومي الكلوي)، الذروة 2–4 سنوات؛ أما RCC ففي الرجال 50–70 سنة."),
]

important = [
 IM("Define nephrotic syndrome and explain its pathophysiology.", "عرّف المتلازمة الكلائية واشرح فسلجتها المرضية.",
    "A group of conditions with increased basement membrane permeability allowing urinary loss of plasma proteins, particularly low-weight proteins like albumin; edema usually mild. All causes share a derangement of glomerular capillary walls; structural or physicochemical GBM changes let protein escape into the filtrate; long-standing heavy proteinuria lowers serum albumin → hypoalbuminemia and a drop in plasma colloid osmotic pressure.",
    "مجموعة حالات بزيادة نفاذية الغشاء القاعدي تسمح بفقد بروتينات البلازما في البول، خاصةً منخفضة الوزن كالألبومين؛ والوذمة عادةً خفيفة. تشترك كل الأسباب في خلل جدران الشعيرات الكبيبية؛ والتغيّرات التركيبية أو الفيزيوكيميائية في الغشاء القاعدي تسمح بتسرّب البروتين للراشح؛ والبيلة البروتينية الشديدة الطويلة تخفض الألبومين ← نقص ألبومين الدم وانخفاض الضغط الغرواني."),
 IM("List the clinical manifestations of nephrotic syndrome.", "عدّد المظاهر السريرية للمتلازمة الكلائية.",
    "1. Massive proteinuria (> 4 g/day) without increased urinary red or white cells. 2. Hypoalbuminemia (< 3 g/100 mL). 3. Generalized edema from decreased plasma colloid oncotic pressure. 4. Hyperlipidemia and hypercholesterolemia from increased hepatic lipoprotein synthesis.",
    "1. بيلة بروتينية هائلة (> 4 غ/يوم) بلا زيادة كريات حمر أو بيض. 2. نقص ألبومين الدم (< 3 غ/100 مل). 3. وذمة معمّمة من انخفاض الضغط الغرواني. 4. فرط شحوم وكوليسترول الدم من زيادة تخليق البروتينات الدهنية في الكبد."),
 IM("Write the causes of nephrotic syndrome (Table 13–2).", "اكتب أسباب المتلازمة الكلائية (جدول 13–2).",
    "Primary (children/adults %): membranous 5/30, minimal change 65/10, FSGS 10/35, MPGN 10/10, IgA and others 10/15. Systemic: diabetes, amyloidosis, SLE, drugs (gold, penicillamine, street heroin), infections (malaria, syphilis, hepatitis B, HIV), malignancy (carcinoma, melanoma), miscellaneous (bee sting allergy, hereditary nephritis). Primary disease ≈ 95% in children, 60% in adults; systemic ≈ 5% and 40%.",
    "الأولية (أطفال/بالغون %): الغشائي 5/30، التغيّر الأدنى 65/10، FSGS 10/35، الغشائي التكاثري 10/10، IgA وغيره 10/15. الجهازية: السكري، النشواني، الذئبة، الأدوية (الذهب، البنسيلامين، هيروين الشارع)، العدوى (الملاريا، الزهري، التهاب الكبد B، HIV)، الخباثة (الكارسينوما، الميلانوما)، متفرّقة (لسعة النحل، التهاب الكلية الوراثي). الأولي ≈ 95% في الأطفال و60% في البالغين؛ الجهازي ≈ 5% و40%."),
 IM("Write about IgA nephropathy and its clinical course.", "اكتب عن اعتلال IgA وسيره السريري.",
    "Berger disease: IgA deposition in the mesangium; common cause of recurrent microscopic or gross hematuria and the commonest glomerular disease on renal biopsy worldwide; affects children and young adults; gross hematuria 1–2 days after a nonspecific URTI; possibly a localized variant of HSP (which is systemic). Course: > half present with gross haematuria after infection; many keep normal function for decades; 25–50% progress to CRF over 20 years; worse prognosis with diffuse mesangial proliferation, segmental sclerosis, endocapillary proliferation or tubulointerstitial fibrosis.",
    "داء بيرجر: ترسّب IgA في المسراق؛ سبب شائع للبيلة الدموية المتكرّرة وأشيع مرض كبيبي بالخزعة عالميًا؛ يصيب الأطفال والشباب؛ بيلة دموية عيانية بعد 1–2 يوم من عدوى تنفسية علوية؛ وربما نوع موضعي من HSP (الجهازية). السير: أكثر من النصف ببيلة عيانية بعد عدوى؛ كثيرون بوظيفة طبيعية لعقود؛ 25–50% يتطوّرون لفشل مزمن خلال 20 سنة؛ والإنذار أسوأ مع التكاثر المسراقي المنتشر والتصلّب القطعي والتكاثر داخل الشعيرات والتليّف الخلالي."),
 IM("Classify kidney tumors by origin and describe the benign tumors.", "صنّف أورام الكلية حسب المنشأ وصف الأورام الحميدة.",
    "Origin: renal tubules (adenoma, adenocarcinoma), embryonic tissue (mesoblastic nephroma, Wilms’ tumor), mesenchymal tissue (angiomyolipoma, medullary interstitial tumor), renal pelvis epithelium (urothelial carcinoma). Benign: adenoma — small, asymptomatic, from tubules; angiomyolipoma — hamartoma of fat, smooth muscle and vessels, with tuberous sclerosis; oncocytoma — cells with abundant granular acidophilic cytoplasm full of mitochondria.",
    "المنشأ: النبيبات (الورم الغدّي، الكارسينوما الغدّية)، النسيج الجنيني (الورم الكلوي الأرومي المتوسط، ويلمز)، المتوسطي (الوعائي العضلي الشحمي، الخلالي اللبّي)، ظهارة الحوض (الظهارية البولية). الحميدة: الغدّي — صغير لا عرضي من النبيبات؛ الوعائي العضلي الشحمي — عابي من دهن وعضل أملس وأوعية، مع التصلّب الحدبي؛ الخلوي الحمضي — خلايا بسايتوبلازم حبيبي حمضي مملوء بالمايتوكوندريا."),
 IM("Compare renal cell carcinoma and Wilms tumor.", "قارن بين كارسينوما الخلايا الكلوية وورم ويلمز.",
    "RCC: most common renal malignancy; men, 50–70 years, smokers; chromosome 3 deletions, von Hippel-Lindau; etiology: tobacco, genetic factors, cystic kidney disease, asbestos/heavy metals/petrochemicals, obesity and oestrogen in women, analgesic nephropathy, tuberous sclerosis. Wilms (nephroblastoma): most common renal malignancy of early childhood; peak 2–4 years; from primitive metanephric tissue; palpable (often huge) flank mass; deletion of short arm of chromosome 11.",
    "RCC: أشيع خباثة كلوية؛ الرجال 50–70 سنة، المدخّنون؛ حذف في الكروموسوم 3، فون هيبل-لينداو؛ الأسباب: التبغ، الوراثة، الأمراض الكيسية، الأسبستوس/المعادن الثقيلة/البتروكيميائيات، السمنة والإستروجين في النساء، اعتلال المسكّنات، التصلّب الحدبي. ويلمز: أشيع خباثة كلوية في الطفولة المبكرة؛ الذروة 2–4 سنوات؛ من نسيج كلوي تالي بدائي؛ كتلة خاصرة محسوسة (غالبًا ضخمة)؛ حذف الذراع القصير للكروموسوم 11."),
]

meta = dict(subject_en="Pathology", subject_ar="علم الأمراض", short_ar="أمراض",
            unit_en="Lecture 6", unit_ar="المحاضرة 6", unit_label="LEC", unit_no="6",
            title_en="Nephrotic Syndrome + Renal Tumors", title_ar="المتلازمة الكلائية وأورام الكلية",
            kind="Theory — نظري", stage="The fourth stage — الرابعة", instructor="د. حامد خليل التميمي")
save("pathology-lec6-nephrotic-renal-tumors", meta, blocks, balance(mcq, 29), tf, traps, important)

```
