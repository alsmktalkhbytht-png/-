---
source: BIOS-Obsidian/tools/scripts/pat5/p5q.py
handouts: [pathology-lec5-glomerular-diseases]
saved: 2026-11-13
tags: [bios, code]
---
# pat5/p5q.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#pathology-lec5-glomerular-diseases|pathology-lec5-glomerular-diseases]]

```python
A = lambda f: "assets/" + f
mcq = [
 {"topic_en": "Kidney and glomerulus", "topic_ar": "الكلية والكبيبة"},
 Q("The functional renal unit is the:", "الوحدة الوظيفية للكلية هي:", O(("Nephron", "النفرون"), ("Ureter", "الحالب"), ("Renal pelvis", "الحوض الكلوي"), ("Medulla", "اللبّ")), "a"),
 Q("The renal corpuscle consists of:", "يتكوّن الجسيم الكلوي من:", O(("Loop of Henle and collecting duct", "عروة هنلي والقناة الجامعة"), ("Glomerulus and Bowman capsule", "الكبيبة ومحفظة بومان"), ("PCT and DCT", "النبيب القريب والبعيد"), ("Cortex and medulla", "القشرة واللبّ")), "b"),
 Q("The collecting duct opens into the:", "تنفتح القناة الجامعة في:", O(("Bowman capsule", "محفظة بومان"), ("Renal cortex", "قشرة الكلية"), ("Renal papilla", "الحليمة الكلوية"), ("Renal artery", "الشريان الكلوي")), "c"),
 Q("Which is NOT one of the four glomerular components that may be damaged?", "أيّ مما يأتي ليس من مكوّنات الكبيبة الأربعة؟", O(("Endothelial cells", "الخلايا البطانية"), ("Basement membrane", "الغشاء القاعدي"), ("Mesangium", "المسراق"), ("Collecting duct", "القناة الجامعة")), "d"),
 Q("Podocytes contact the basement membrane via:", "تتّصل الخلايا القدمية بالغشاء القاعدي عبر:", O(("Foot processes", "الزوائد القدمية"), ("Cilia", "الأهداب"), ("Microvilli", "الزغيبات"), ("Tight junctions only", "الوصلات المحكمة فقط")), "a"),
 Q("The majority of glomerular diseases are:", "أغلب أمراض الكبيبات:", O(("Hereditary", "وراثية"), ("Primary (idiopathic)", "أولية (مجهولة السبب)"), ("Secondary to infection", "ثانوية للعدوى"), ("Drug-induced", "دوائية")), "b"),
 Q("Bright’s disease is another name for:", "داء برايت اسم آخر لـ:", O(("Renal stones", "حصى الكلية"), ("Pyelonephritis", "التهاب الحويضة والكلية"), ("Glomerulonephritis", "التهاب الكبيبات والكلية"), ("Polycystic kidney", "الكلية متعدّدة الأكياس")), "c"),
 {"topic_en": "Classification", "topic_ar": "التصنيف"},
 Q("Which is a hereditary nephritis?", "أيّ مما يأتي التهاب كلية وراثي؟", O(("Lupus nephritis", "التهاب الكلية الذئبي"), ("Diabetic nephropathy", "اعتلال الكلية السكري"), ("Amyloidosis", "الداء النشواني"), ("Alport’s syndrome", "متلازمة ألبورت")), "d"),
 Q("Diabetic nephropathy is classified as:", "يُصنَّف اعتلال الكلية السكري كـ:", O(("Secondary systemic glomerular disease", "مرض كبيبي جهازي ثانوي"), ("Primary GN", "التهاب كبيبات أولي"), ("Hereditary nephritis", "التهاب كلية وراثي"), ("Normal variant", "تغيّر طبيعي")), "a"),
 Q("Goodpasture’s syndrome involves:", "تتضمّن متلازمة غودباستشر:", O(("Kidney stones", "حصى الكلية"), ("Antibodies that attack the kidneys", "أضدادًا تهاجم الكلية"), ("Bacterial infection only", "عدوى بكتيرية فقط"), ("Congenital absence of kidney", "غياب خلقي للكلية")), "b"),
 Q("Henoch-Schönlein purpura is also known as:", "تعرف فرفرية هينوخ-شونلاين أيضًا بـ:", O(("Wegener’s granulomatosis", "ورام فيغنر"), ("Fabry’s disease", "داء فابري"), ("IgA vasculitis", "التهاب الأوعية بـ IgA"), ("Lupus", "الذئبة")), "c"),
 Q("FSGS stands for:", "FSGS تعني:", O(("Fast streptococcal GN syndrome", "متلازمة التهاب الكبيبات العقدي السريع"), ("Familial secondary GN", "التهاب كبيبات ثانوي عائلي"), ("Fibrous systemic glomerular scar", "ندبة كبيبية جهازية ليفية"), ("Focal segmental glomerulosclerosis", "التصلّب الكبيبي البؤري القطعي")), "d"),
 {"topic_en": "Clinical features and IgA nephropathy", "topic_ar": "المظاهر السريرية واعتلال IgA"},
 Q("A firm diagnosis of glomerular disease is established by:", "يُؤكَّد تشخيص أمراض الكبيبات بـ:", O(("Renal biopsy under light, electron and immunofluorescence microscopy", "خزعة الكلية بالمجهر الضوئي والإلكتروني والتألّق المناعي"), ("Urine culture", "زرع البول"), ("Chest X-ray", "أشعة الصدر"), ("Blood glucose", "سكر الدم")), "a"),
 Q("The most common cause of glomerulonephritis in the world is:", "أشيع سبب لالتهاب الكبيبات في العالم:", O(("Membranous GN", "الغشائي"), ("IgA nephropathy", "اعتلال IgA"), ("Lupus nephritis", "الذئبي"), ("Alport’s syndrome", "ألبورت")), "b"),
 Q("IgA nephropathy is also called:", "يُسمّى اعتلال IgA أيضًا:", O(("Bright’s disease", "داء برايت"), ("Fabry disease", "داء فابري"), ("Berger disease", "داء بيرجر"), ("Lipoid nephrosis", "الكلاء الشحمي")), "c"),
 Q("In IgA nephropathy, immune complexes activate:", "في اعتلال IgA تنشّط المعقّدات المناعية:", O(("Coagulation cascade", "سلسلة التخثّر"), ("Classical pathway only", "المسار الكلاسيكي فقط"), ("Lectin pathway only", "مسار اللكتين فقط"), ("Alternate complement pathway", "المسار البديل للمتمّمة")), "d"),
 {"topic_en": "Major glomerular syndromes", "topic_ar": "المتلازمات الكبيبية الرئيسية"},
 Q("Acute nephritic syndrome includes:", "تشمل متلازمة التهاب الكلية الحادة:", O(("Microscopic haematuria, mild proteinuria, hypertension, oedema and oliguria", "بيلة دموية مجهرية، بروتينية خفيفة، ارتفاع ضغط، وذمة، قلّة بول"), ("Massive proteinuria only", "بروتينية هائلة فقط"), ("Lipiduria and hypercoagulability", "بيلة دهنية وفرط تخثّر"), ("No urinary findings", "لا موجودات بولية")), "a"),
 Q("Which is a feature of nephrotic syndrome?", "أيّ مما يأتي صفة للمتلازمة الكلائية؟", O(("Mild proteinuria", "بروتينية خفيفة"), ("Hypoalbuminaemia", "نقص ألبومين الدم"), ("Hypocoagulability", "نقص التخثّر"), ("Hypolipidaemia", "نقص الشحوم")), "b"),
 Q("The most frequent cause of nephrotic syndrome in children is:", "أشيع سبب للمتلازمة الكلائية في الأطفال:", O(("Diabetes", "السكري"), ("Membranous GN", "الغشائي"), ("Lipoid nephrosis (65%)", "الكلاء الشحمي (65%)"), ("Amyloidosis", "النشواني")), "c"),
 Q("The most common primary glomerular disease causing nephrotic syndrome in adults is:", "أشيع مرض كبيبي أولي في البالغين:", O(("IgA nephropathy", "اعتلال IgA"), ("Minimal change", "التغيّر الأدنى"), ("Alport", "ألبورت"), ("Membranous glomerulonephritis (40%)", "التهاب الكبيبات الغشائي (40%)")), "d"),
 Q("In adults, the more frequent causes of nephrotic syndrome are:", "في البالغين الأسباب الأكثر شيوعًا للمتلازمة الكلائية:", O(("Systemic diseases (diabetes, amyloidosis, SLE)", "الأمراض الجهازية (السكري، النشواني، الذئبة)"), ("Lipoid nephrosis", "الكلاء الشحمي"), ("Exercise", "الجهد"), ("Lordosis", "التقعّر القطني")), "a"),
 Q("Glomerular causes of acute renal failure are principally:", "الأسباب الكبيبية للفشل الكلوي الحاد أساسًا:", O(("IgA nephropathy and Alport", "اعتلال IgA وألبورت"), ("Rapidly progressive GN and acute diffuse proliferative GN", "سريع التقدّم والتكاثري المنتشر الحاد"), ("Minimal change and FSGS", "التغيّر الأدنى وFSGS"), ("Membranous GN only", "الغشائي فقط")), "b"),
 Q("Chronic renal failure patients generally have:", "لدى مرضى الفشل الكلوي المزمن عمومًا:", O(("Enlarged kidneys", "كلى متضخّمة"), ("Normal kidneys", "كلى طبيعية"), ("Small contracted kidneys", "كلى صغيرة متقلّصة"), ("Polycystic kidneys", "كلى متعدّدة الأكياس")), "c"),
 Q("Which proteinuria may be unrelated to renal disease?", "أيّ بيلة بروتينية قد لا تتعلّق بمرض كلوي؟", O(("Massive nephrotic", "الكلائية الهائلة"), ("Diabetic", "السكرية"), ("Lupus", "الذئبية"), ("Orthostatic", "الانتصابية")), "d"),
 Q("Asymptomatic microscopic haematuria is common in:", "البيلة الدموية المجهرية اللاعرضية شائعة في:", O(("Children and young adolescents", "الأطفال واليافعين"), ("The elderly only", "كبار السن فقط"), ("Pregnant women only", "الحوامل فقط"), ("Newborns only", "حديثي الولادة فقط")), "a"),
 {"topic_en": "Picture questions", "topic_ar": "أسئلة الصور"},
 Q("In this figure, the glomerulus is enclosed by:", "في هذا الشكل، الكبيبة محاطة بـ:", O(("Collecting duct", "القناة الجامعة"), ("Bowman’s capsule", "محفظة بومان"), ("Vasa recta", "الأوعية المستقيمة"), ("Ureter", "الحالب")), "b", img=A("renal-corpuscle.jpg"), img_h="34mm"),
 Q("This figure shows the deposition of immune complexes in:", "يُظهر هذا الشكل ترسّب المعقّدات المناعية في:", O(("IgA nephropathy", "اعتلال IgA"), ("Alport’s syndrome", "ألبورت"), ("Membranous glomerulopathy", "الاعتلال الكبيبي الغشائي"), ("Normal kidney", "الكلية الطبيعية")), "c", img=A("membranous.png"), img_h="40mm"),
 Q("The diseased kidney in this figure shows:", "الكلية المريضة في هذا الشكل تُظهر:", O(("Normal glomeruli", "كبيبات طبيعية"), ("Enlarged smooth surface", "سطحًا أملس متضخّمًا"), ("Stones only", "حصى فقط"), ("Scar tissue, damaged glomerulus and tubules", "نسيجًا ندبيًا وكبيبة ونبيبات متضرّرة")), "d", img=A("normal-diseased-kidney.jpg"), img_h="42mm"),
]

tf = [
 TF("The kidney secretes hormones.", "تفرز الكلية الهرمونات.", "T"),
 TF("The proximal convoluted tubule is located in the renal medulla.", "يقع النبيب الملتفّ القريب في لبّ الكلية.", "F"),
 TF("Glomerular diseases are typically caused by disturbances of structure.", "تنتج أمراض الكبيبات عادةً عن اضطرابات التركيب.", "T"),
 TF("Fabry’s disease is a secondary systemic glomerular disease.", "داء فابري مرض كبيبي جهازي ثانوي.", "F"),
 TF("Systemic infections such as HBV, HCV and HIV can cause secondary glomerular disease.", "قد تسبّب العدوى الجهازية مثل HBV وHCV وHIV مرضًا كبيبيًا ثانويًا.", "T"),
 TF("Haematuria is one of the four clinical features of glomerular disease.", "البيلة الدموية من الصفات السريرية الأربع لأمراض الكبيبات.", "T"),
 TF("The mechanism of IgA nephropathy is fully known.", "آلية اعتلال IgA معروفة بالكامل.", "F"),
 TF("Nephrotic syndrome includes hyperlipidaemia and lipiduria.", "تشمل المتلازمة الكلائية فرط شحوم الدم والبيلة الدهنية.", "T"),
 TF("Massive proteinuria is a feature of acute nephritic syndrome.", "البيلة البروتينية الهائلة صفة لمتلازمة التهاب الكلية الحادة.", "F"),
 TF("In children, primary GN causes most cases of nephrotic syndrome.", "في الأطفال يسبّب التهاب الكبيبات الأولي أغلب حالات المتلازمة الكلائية.", "T"),
 TF("Chronic renal failure develops over days.", "يتطوّر الفشل الكلوي المزمن خلال أيام.", "F"),
 TF("Azotaemia is a finding in chronic renal failure.", "الآزوتيميا من موجودات الفشل الكلوي المزمن.", "T"),
 TF("Neoplasia can cause asymptomatic haematuria.", "قد تسبّب الأورام بيلة دموية لاعرضية.", "T"),
 TF("Exercise-induced proteinuria always indicates glomerulonephritis.", "البيلة البروتينية الناتجة عن الجهد تدلّ دائمًا على التهاب الكبيبات.", "F"),
]

traps = [
 TR("Nephritic or nephrotic — which has massive proteinuria?", "التهاب الكلية أم الكلائية — أيّهما ببروتينية هائلة؟",
    "Nephrotic (massive proteinuria, hypoalbuminaemia, oedema, hyperlipidaemia); nephritic has mild proteinuria with haematuria, hypertension and oliguria.", "الكلائية (بروتينية هائلة، نقص ألبومين، وذمة، فرط شحوم)؛ أما التهاب الكلية فبروتينية خفيفة مع بيلة دموية وارتفاع ضغط وقلّة بول."),
 TR("65% or 40%?", "65% أم 40%؟",
    "65% = lipoid nephrosis in children; 40% = membranous GN in adults (most common primary).", "65% = الكلاء الشحمي في الأطفال؛ 40% = التهاب الكبيبات الغشائي في البالغين (أشيع أولي)."),
 TR("Most common GN in the world vs most common primary nephrotic cause in adults?", "أشيع التهاب كبيبات في العالم مقابل أشيع سبب أولي للكلائية في البالغين؟",
    "World: IgA nephropathy (Berger); adults' nephrotic (primary): membranous GN.", "العالم: اعتلال IgA (بيرجر)؛ الكلائية الأولية في البالغين: الغشائي."),
 TR("Alport and Fabry — secondary or hereditary?", "ألبورت وفابري — ثانوي أم وراثي؟",
    "Hereditary (with nail-patella syndrome and congenital nephrotic syndrome).", "وراثي (مع متلازمة الظفر-الرضفة والكلائية الخلقية)."),
 TR("ARF vs CRF?", "الحاد مقابل المزمن؟",
    "ARF: rapid decline (RPGN, acute diffuse proliferative GN); CRF: over years, azotaemia, small contracted kidneys.", "الحاد: تدهور سريع (سريع التقدّم، التكاثري المنتشر الحاد)؛ المزمن: عبر سنوات، آزوتيميا، كلى صغيرة متقلّصة."),
 TR("Is all proteinuria renal disease?", "هل كل بيلة بروتينية مرض كلوي؟",
    "No — exercise-induced, extreme lordosis and orthostatic proteinuria may be unrelated to renal disease.", "لا — الناتجة عن الجهد والتقعّر الشديد والانتصابية قد لا تتعلّق بمرض كلوي."),
]

important = [
 IM("List the functions of the kidney and the parts of the nephron.", "عدّد وظائف الكلية وأجزاء النفرون.",
    "Functions: excreting waste products, regulating body fluid and solute balance, regulating blood pressure, secreting hormones. Nephron: renal corpuscle (glomerulus and Bowman capsule), PCT, descending loop of Henle, ascending limb, thick ascending limb, DCT, collecting duct.",
    "الوظائف: إخراج الفضلات، تنظيم توازن السوائل والمذابات، تنظيم ضغط الدم، إفراز الهرمونات. النفرون: الجسيم الكلوي (الكبيبة ومحفظة بومان)، PCT، الطرف النازل لعروة هنلي، الطرف الصاعد، الطرف الصاعد الثخين، DCT، القناة الجامعة."),
 IM("What are the glomerular components that may be damaged, and the aetiology of glomerular diseases?", "ما مكوّنات الكبيبة التي قد تتضرّر، وما سببيات أمراض الكبيبات؟",
    "Components: endothelial cells, glomerular basement membrane, mesangium, epithelial cells (podocytes with foot processes). Aetiology: primary (majority, idiopathic), secondary to systemic disease, hereditary (Alport, Fabry, congenital nephrotic syndrome).",
    "المكوّنات: الخلايا البطانية، الغشاء القاعدي الكبيبي، المسراق، الخلايا الظهارية (الخلايا القدمية بزوائدها). السببيات: أولية (الأغلبية، مجهولة)، ثانوية لمرض جهازي، وراثية (ألبورت، فابري، الكلائية الخلقية)."),
 IM("Classify glomerular diseases with examples.", "صنّف أمراض الكبيبات مع الأمثلة.",
    "I. Primary GN: acute (post-/non-streptococcal), RPGN, minimal change, membranous, membrano-proliferative, focal and diffuse proliferative, FSGS, IgA nephropathy, chronic GN. II. Secondary: lupus nephritis, diabetic nephropathy, amyloidosis, PAN, Wegener’s, Goodpasture’s, HSP, systemic infections, mixed cryoglobulinaemia. III. Hereditary: Alport’s, Fabry’s, nail-patella.",
    "I. الأولي: الحاد (التالي/غير العقدي)، سريع التقدّم، التغيّر الأدنى، الغشائي، الغشائي التكاثري، التكاثري البؤري والمنتشر، FSGS، اعتلال IgA، المزمن. II. الثانوي: الذئبي، السكري، النشواني، PAN، فيغنر، غودباستشر، HSP، العدوى الجهازية، الغلوبيولين البردي. III. الوراثي: ألبورت، فابري، الظفر-الرضفة."),
 IM("Write about IgA nephropathy.", "اكتب عن اعتلال الكلية بـ IgA.",
    "Berger disease; mechanism unknown — possible entrapment of circulating immune complexes (abnormal IgA1 + anti-glycan autoantibody) with activation of the alternate complement pathway, and possible genetic predisposition; the most common cause of glomerulonephritis in the world (nephritic syndrome).",
    "داء بيرجر؛ الآلية غير معروفة — احتمال احتباس معقّدات مناعية دائرة (IgA1 شاذ + ضد ذاتي مضاد للغليكان) مع تنشيط المسار البديل للمتمّمة، واحتمال استعداد وراثي؛ وهو أشيع سبب لالتهاب الكبيبات في العالم (متلازمة التهاب الكلية)."),
 IM("Compare the acute nephritic syndrome and the nephrotic syndrome.", "قارن بين متلازمة التهاب الكلية الحادة والمتلازمة الكلائية.",
    "Nephritic: acute microscopic haematuria, mild proteinuria, hypertension, oedema, oliguria; causes acute GN, RPGN or systemic disease. Nephrotic: massive proteinuria, hypoalbuminaemia, oedema, hyperlipidaemia, lipiduria, hypercoagulability; children — primary GN, lipoid nephrosis 65%; adults — systemic diseases (diabetes, amyloidosis, SLE), primary membranous GN 40%.",
    "التهاب الكلية: بيلة دموية مجهرية حادة، بروتينية خفيفة، ارتفاع ضغط، وذمة، قلّة بول؛ أسبابه التهاب الكبيبات الحاد وسريع التقدّم أو مرض جهازي. الكلائية: بروتينية هائلة، نقص ألبومين، وذمة، فرط شحوم، بيلة دهنية، فرط تخثّر؛ الأطفال — أولي، الكلاء الشحمي 65%؛ البالغون — جهازية (سكري، نشواني، ذئبة)، الغشائي الأولي 40%."),
 IM("Describe acute and chronic renal failure, asymptomatic proteinuria and asymptomatic haematuria.", "صف الفشل الكلوي الحاد والمزمن، والبيلة البروتينية والدموية اللاعرضيتين.",
    "ARF: rapid decline in renal function (glomerular causes: RPGN, acute diffuse proliferative GN). CRF: advanced impairment over years with proteinuria, haematuria, hypertension and azotaemia; small contracted kidneys from chronic GN. Asymptomatic proteinuria: may be unrelated (exercise, extreme lordosis, orthostatic) or mild GN. Asymptomatic microscopic haematuria: common in children and adolescents; causes — glomerulus, interstitium, calyces, ureter, bladder, prostate, urethra, bleeding disorders, congenital abnormalities, neoplasia.",
    "الحاد: تدهور سريع في وظيفة الكلية (أسباب كبيبية: سريع التقدّم، التكاثري المنتشر الحاد). المزمن: قصور متقدّم عبر سنوات مع بروتينية ودموية وارتفاع ضغط وآزوتيميا؛ كلى صغيرة متقلّصة من التهاب الكبيبات المزمن. البروتينية اللاعرضية: قد لا تتعلّق بمرض (جهد، تقعّر، انتصابية) أو التهاب كبيبات خفيف. الدموية المجهرية اللاعرضية: شائعة في الأطفال واليافعين؛ أسبابها الكبيبة والنسيج الخلالي والكؤوس والحالب والمثانة والبروستات والإحليل واضطرابات النزف والتشوّهات الخلقية والأورام."),
]

meta = dict(subject_en="Pathology", subject_ar="علم الأمراض", short_ar="أمراض",
            unit_en="Lecture 5", unit_ar="المحاضرة 5", unit_label="LEC", unit_no="5",
            title_en="Glomerular Diseases", title_ar="أمراض الكبيبات",
            kind="Theory — نظري", stage="The fourth stage — الرابعة", instructor="د. حامد خليل التميمي")
save("pathology-lec5-glomerular-diseases", meta, blocks, balance(mcq, 23), tf, traps, important)

```
