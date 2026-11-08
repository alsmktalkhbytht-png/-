import sys, re; sys.path.insert(0, "/tmp/claude-0/-home-user--/67d83c9a-7b0e-5ae5-b52b-cd659ab074ab/scratchpad/imm456")
from ci import *            # c helpers + B INSHORT TERMS balance save(split.fix)
import split
split.ABBR = split.ABBR + ("a.", "b.", "c.", "d.", "e.")

# Pathology — lecture 6 (stage 4) — د. حامد خليل التميمي — Nephrotic Syndrome + Renal Tumors
# The PDF text layer splits words; text taken from the slides as displayed.

BN = lambda en, ar: N(en, ar, label=["BIOS note", "ملاحظة BIOS"])
O = P
def TERMS6(terms, n=6):
    head = [B("Term", "المصطلح"), "الترجمات العربية المستعملة"]
    return [SEC("Key terms", "أهم المصطلحات")] + [T(head, [[f"**{e}**", a] for e, a in terms[i:i + n]], ar_cols=[1], widths=[36, 64])
                                                  for i in range(0, len(terms), n)]

blocks = [
 # ───────────────────────── 1. Nephrotic syndrome
 SEC("NEPHROTIC SYNDROME", "المتلازمة الكلائية"),
 C("Nephrotic syndrome includes a group of conditions characterized by increased basement membrane permeability, permitting the urinary loss of plasma proteins, particularly low weight proteins, such as albumin and edema may be present but usually are mild.",
   "تشمل المتلازمة الكلائية مجموعة حالات تتميّز **بزيادة نفاذية الغشاء القاعدي**، مما يسمح **بفقدان بروتينات البلازما في البول**، خاصةً **البروتينات منخفضة الوزن مثل الألبومين**، وقد توجد **وذمة** لكنها عادةً **خفيفة**."),
 F("nephrotic-diagram.jpg", "Normal vs Nephrotic syndrome — Kidney, Ureter, Bladder, Glomerulus (filter), Blood & waste, Filtered blood, Low levels of protein, Protein leaks into urine",
   "الطبيعي مقابل المتلازمة الكلائية — الكلية، الحالب، المثانة، الكبيبة (المرشّح)، دم وفضلات، دم مُرشَّح، مستوى بروتين منخفض، تسرّب البروتين إلى البول", h="96mm", fit="contain"),
 H2("CAUSES OF NEPHROTIC SYNDROME", "أسباب المتلازمة الكلائية"),
 C(["The nephrotic syndrome has diverse causes that share a common pathophysiology.",
    "In all there is a derangement in the capillary walls of the glomeruli that results in increased permeability to plasma proteins."],
   ["للمتلازمة الكلائية **أسباب متنوّعة** تشترك في **فسلجة مرضية واحدة**.",
    "ففيها كلها **خلل في جدران شعيرات الكبيبات** ينتج عنه **زيادة النفاذية لبروتينات البلازما**."]),
 C(["Any increased permeability resulting from either structural or physicochemical alterations in the GBM allows protein to escape from the plasma into the glomerular filtrate.",
    "With long-standing or extremely heavy proteinuria, serum albumin is decreased, resulting in hypoalbuminemia and a drop in plasma colloid osmotic pressure."],
   ["وأي زيادة في النفاذية ناتجة عن **تغيّرات تركيبية أو فيزيوكيميائية في الغشاء القاعدي الكبيبي (GBM)** تسمح للبروتين بالتسرّب من البلازما إلى **الراشح الكبيبي**.",
    "ومع البيلة البروتينية **الطويلة الأمد أو الشديدة جدًا** ينخفض ألبومين المصل، فيحدث **نقص ألبومين الدم** و**انخفاض الضغط التناضحي الغرواني للبلازما**."]),
 F("glomerulus-histology.jpg", "Glomerulus (histology, arrows)", "كبيبة (مقطع نسيجي، الأسهم)", h="46mm", fit="contain"),
 T([B("Cause", "السبب"), B("Children %", "الأطفال %"), B("Adults %", "البالغون %")],
   [[B("**Membranous nephropathy**", "**اعتلال الكلية الغشائي**"), "5", "30"],
    [B("**Minimal-change disease**", "**داء التغيّر الأدنى**"), "65", "10"],
    [B("**Focal segmental glomerulosclerosis**", "**التصلّب الكبيبي البؤري القطعي**"), "10", "35"],
    [B("**Membranoproliferative glomerulonephritis**", "**التهاب الكبيبات الغشائي التكاثري**"), "10", "10"],
    [B("**IgA nephropathy and others**", "**اعتلال IgA وغيره**"), "10", "15"]],
   key_cols=[0], widths=[60, 20, 20], style="summary", label_en="Table 13–2 Causes of Nephrotic Syndrome — Primary Glomerular Disease (prevalence %)", label_ar="جدول 13–2 أسباب المتلازمة الكلائية — مرض كبيبي أولي (النسبة %)"),
 T([B("Systemic Diseases with Renal Manifestations", "أمراض جهازية بمظاهر كلوية"), B("Systemic Diseases with Renal Manifestations", "أمراض جهازية بمظاهر كلوية")],
   [[B("Diabetes mellitus", "داء السكري"), B("Amyloidosis", "الداء النشواني")],
    [B("Systemic lupus erythematosus", "الذئبة الحمامية الجهازية"), B("Ingestion of drugs (gold, penicillamine, “street heroin”)", "تناول أدوية (الذهب، البنسيلامين، “هيروين الشارع”)")],
    [B("Infections (malaria, syphilis, hepatitis B, HIV infection)", "العدوى (الملاريا، الزهري، التهاب الكبد B، عدوى HIV)"), B("Malignancy (carcinoma, melanoma)", "الخباثة (الكارسينوما، الورم الميلانيني)")],
    [B("Miscellaneous (bee sting allergy, hereditary nephritis)", "متفرّقة (حساسية لسعة النحل، التهاب الكلية الوراثي)"), B("", "")]],
   widths=[50, 50], style="summary", label_en="Table 13–2 (cont.) — Systemic Diseases with Renal Manifestations", label_ar="جدول 13–2 (تكملة) — أمراض جهازية بمظاهر كلوية"),
 C(["*Approximate prevalence of primary disease is 95% of the cases in children, 60% in adults.", "Approximate prevalence of systemic disease is 5% of the cases in children, 40% in adults.", "HIV, human immunodeficiency virus."],
   ["*النسبة التقريبية للمرض الأولي **95%** من الحالات في الأطفال، و**60%** في البالغين.", "والنسبة التقريبية للمرض الجهازي **5%** في الأطفال، و**40%** في البالغين.", "HIV: فيروس العوز المناعي البشري."]),
 BN("These percentages (from the table on the slide) differ from lecture 5 (membranous 40% in adults); here FSGS is 35% and membranous 30%.", "هذه النسب (من جدول الشريحة) تختلف عن المحاضرة 5 (الغشائي 40% في البالغين)؛ فهنا FSGS 35% والغشائي 30%."),
 H2("CLINICAL MANIFESTATIONS", "المظاهر السريرية"),
 L([["**Massive proteinuria** is generally characterized by excretion of more than 4 grams of protein per day.", "proteinuria in the nephrotic syndrome is unaccompanied by increased urinary red cells or white cells."],
    "**Hypoalbuminemia** results from proteinuria and is oftenmarked by a serum concentration of less than 3 g/100 mL."],
   [["**البيلة البروتينية الهائلة** تتميّز عمومًا **بإخراج أكثر من 4 غرامات بروتين يوميًا**.", "والبيلة البروتينية في المتلازمة الكلائية **لا يرافقها زيادة الكريات الحمر أو البيض في البول**."],
    "**نقص ألبومين الدم** ينتج عن البيلة البروتينية، ويتميّز غالبًا **بتركيز مصلي أقل من 3 غ/100 مل**."]),
 L(["**Generalized edema** results from decreased plasma colloidoncotic pressure.", "**Hyperlipidemia and hypercholesterolemia** are caused by increased hepatic lipoprotein synthesis"],
   ["**الوذمة المعمّمة** تنتج عن **انخفاض الضغط الغرواني الجاذب للبلازما**.", "**فرط شحوم الدم وفرط كوليسترول الدم** سببهما **زيادة تخليق البروتينات الدهنية في الكبد**"], start=3),
 INSHORT([("Nephrotic = ↑ **GBM permeability** → loss of plasma proteins (mainly **albumin**); edema usually mild.", "الكلائية = ↑ **نفاذية الغشاء القاعدي** ← فقد بروتينات البلازما (خاصةً **الألبومين**)؛ الوذمة عادةً خفيفة."),
          ("**> 4 g protein/day**, no RBCs/WBCs in urine; albumin **< 3 g/100 mL**; edema from ↓ oncotic pressure; ↑ lipids from liver.", "**> 4 غ بروتين/يوم** بلا كريات في البول؛ ألبومين **< 3 غ/100 مل**؛ وذمة من ↓ الضغط الغرواني؛ ↑ الشحوم من الكبد."),
          ("Children: **minimal change 65%**, primary 95%; adults: **FSGS 35%, membranous 30%**, systemic 40%.", "الأطفال: **التغيّر الأدنى 65%**، الأولي 95%؛ البالغون: **FSGS 35%، الغشائي 30%**، الجهازي 40%.")]),

 # ───────────────────────── 2. IgA nephropathy
 SEC("IGA NEPHROPATHY (BERGER DISEASE)", "اعتلال الكلية بـ IgA (داء بيرجر)"),
 C(["**IgA nephropathy (Berger disease) :-** is an extremely common entity defined by deposition of IgA in the mesangium.",
    "IgA nephropathy is one of the most common causes of recurrent microscopic or gross hematuria and is the most common glomerular disease revealed by renal biopsy worldwide."],
   ["**اعتلال الكلية بـ IgA (داء بيرجر):** كيان **شائع جدًا** يُعرَّف **بترسّب IgA في المسراق**.",
    "وهو من **أشيع أسباب البيلة الدموية المتكرّرة المجهرية أو العيانية**، و**أشيع مرض كبيبي تكشفه خزعة الكلية في العالم**."]),
 C("This condition usually affects children and young adults and begins as an episode of gross hematuria that occurs within 1 or 2 days of a nonspecific upper respiratory tract infection.",
   "تصيب هذه الحالة عادةً **الأطفال والشباب**، وتبدأ **بنوبة بيلة دموية عيانية** تحدث **خلال يوم أو يومين** من **عدوى غير نوعية في الجهاز التنفسي العلوي**."),
 C(["Some workers have considered IgA nephropathy to be a localized variant of Henoch-Schönlein purpura, also characterized by IgA deposition in the mesangium .",
    "In contrast with IgA nephropathy, which is purely a renal disorder, Henoch-Schönlein purpura is a systemic syndrome involving the skin (purpuric rash), gastrointestinal tract (abdominal pain), joints (arthritis), and kidneys."],
   ["عدّ بعض الباحثين اعتلال IgA **نوعًا موضعيًا من فرفرية هينوخ-شونلاين** التي تتميّز أيضًا بترسّب IgA في المسراق.",
    "وبخلاف اعتلال IgA الذي هو **اضطراب كلوي بحت**، فإن فرفرية هينوخ-شونلاين **متلازمة جهازية** تصيب **الجلد (طفح فرفري)** و**القناة الهضمية (ألم البطن)** و**المفاصل (التهاب المفاصل)** و**الكليتين**."]),
 F("hsp-rash.jpg", "Purpuric rash (Henoch-Schönlein purpura)", "طفح فرفري (فرفرية هينوخ-شونلاين)", h="54mm", fit="contain"),
 H2("CLINICAL COURSE", "السير السريري"),
 L(["The disease most often affects children and young adults.",
    "More than half of those with IgA nephropathy present with gross haematuria after an infection of the respiratory or, less commonly, gastrointestinal or urinary tract;",
    ["Many patients maintain normal renal function for decades.", "Slow progression to chronic renal failure occurs in 25% to 50% of cases over a period of 20 years."],
    "Renal biopsy findings may help identify those with worse prognosis, as indicated by diffuse mesangial proliferation, segmental sclerosis, endocapillary proliferation, or tubulointerstitial fibrosis."],
   ["يصيب المرض **غالبًا الأطفال والشباب**.",
    "**أكثر من نصف** المصابين يأتون **ببيلة دموية عيانية بعد عدوى تنفسية**، أو بشكل أقل عدوى هضمية أو بولية؛",
    ["كثير من المرضى **يحتفظون بوظيفة كلوية طبيعية لعقود**.", "ويحدث **تطوّر بطيء إلى الفشل الكلوي المزمن** في **25% إلى 50%** من الحالات **خلال 20 سنة**."],
    "قد تساعد **خزعة الكلية** في تحديد ذوي **الإنذار الأسوأ**، كما يدل عليه **التكاثر المسراقي المنتشر**، و**التصلّب القطعي**، و**التكاثر داخل الشعيرات**، أو **التليّف الخلالي النبيبي**."]),
 T([B("Feature", "الصفة"), B("IgA nephropathy", "اعتلال IgA"), B("Henoch-Schönlein purpura", "فرفرية هينوخ-شونلاين")],
   [[B("**IgA in mesangium**", "**IgA في المسراق**"), B("yes", "نعم"), B("yes", "نعم")],
    [B("**Extent**", "**الامتداد**"), B("purely renal", "كلوي بحت"), B("systemic: skin, GIT, joints, kidneys", "جهازي: جلد، هضم، مفاصل، كلى")],
    [B("**Presentation**", "**العرض**"), B("gross haematuria 1–2 days after URTI", "بيلة دموية عيانية بعد 1–2 يوم من عدوى تنفسية علوية"), B("purpuric rash, abdominal pain, arthritis", "طفح فرفري، ألم بطن، التهاب مفاصل")]],
   key_cols=[0], widths=[24, 36, 40], style="summary", label_en="IgA nephropathy vs HSP", label_ar="اعتلال IgA مقابل HSP"),
 INSHORT([("IgA nephropathy = **IgA in mesangium**; commonest GN on **renal biopsy** worldwide; recurrent haematuria.", "اعتلال IgA = **IgA في المسراق**؛ أشيع التهاب كبيبات **بخزعة الكلية** عالميًا؛ بيلة دموية متكرّرة."),
          ("Children/young adults; **gross haematuria 1–2 days after URTI**; HSP = its systemic counterpart.", "الأطفال/الشباب؛ **بيلة دموية عيانية بعد 1–2 يوم من عدوى تنفسية علوية**؛ وHSP نظيره الجهازي."),
          ("Course: normal function for decades; **25–50% → CRF over 20 years**; worse prognosis on biopsy: diffuse mesangial proliferation, sclerosis, endocapillary proliferation, fibrosis.", "السير: وظيفة طبيعية لعقود؛ **25–50% ← فشل مزمن خلال 20 سنة**؛ الإنذار الأسوأ بالخزعة: تكاثر مسراقي منتشر، تصلّب، تكاثر داخل الشعيرات، تليّف.")]),

 # ───────────────────────── 3. Tumors of the kidney
 SEC("TUMORS OF THE KIDNEY", "أورام الكلية"),
 F("kidney-cancer.jpg", "Kidney Cancer — healthy kidneys vs kidneys with tumors", "سرطان الكلية — كلى سليمة مقابل كلى بأورام", h="38mm", fit="contain"),
 C(["Both benign and malignant tumors occur in the kidney.",
    "These may arise from renal tubules (adenoma, adenocarcinoma), embryonic tissue (mesoblastic nephroma, Wilms’ tumor), mesenchymal tissue (angiomyolipoma, medullary interstitial tumor) and from the epithelium of the renal pelvis (urothelial carcinoma)."],
   ["تحدث في الكلية **أورام حميدة وخبيثة**.",
    "وقد تنشأ من **النبيبات الكلوية** (الورم الغدّي، الكارسينوما الغدّية)، أو **النسيج الجنيني** (الورم الكلوي الأرومي المتوسط، ورم ويلمز)، أو **النسيج المتوسطي** (الورم الوعائي العضلي الشحمي، الورم الخلالي اللبّي)، أو من **ظهارة الحوض الكلوي** (الكارسينوما الظهارية البولية)."]),
 T([B("Origin", "المنشأ"), B("Tumors", "الأورام")],
   [[B("**Renal tubules**", "**النبيبات الكلوية**"), B("adenoma, adenocarcinoma", "الورم الغدّي، الكارسينوما الغدّية")],
    [B("**Embryonic tissue**", "**النسيج الجنيني**"), B("mesoblastic nephroma, Wilms’ tumor", "الورم الكلوي الأرومي المتوسط، ورم ويلمز")],
    [B("**Mesenchymal tissue**", "**النسيج المتوسطي**"), B("angiomyolipoma, medullary interstitial tumor", "الورم الوعائي العضلي الشحمي، الورم الخلالي اللبّي")],
    [B("**Renal pelvis epithelium**", "**ظهارة الحوض الكلوي**"), B("urothelial carcinoma", "الكارسينوما الظهارية البولية")]],
   key_cols=[0], widths=[34, 66], style="summary", label_en="Origin of kidney tumors", label_ar="منشأ أورام الكلية"),
 H2("A. BENIGN TUMORS OF THE KIDNEY", "أ. أورام الكلية الحميدة"),
 C(["**1. Adenoma** This tumor is most often small and asymptomatic.", "It is derived from renal tubules."],
   ["**1. الورم الغدّي** غالبًا **صغير ولا عرضي**.", "وهو **مشتق من النبيبات الكلوية**."]),
 F("adenoma.jpg", "Adenoma (histology)", "الورم الغدّي (مقطع نسيجي)", h="44mm", fit="contain"),
 C(["**2. Angiomyolipoma** This tumor is a hamartoma consisting of fat, smooth muscle, and blood vessels.", "It is often associated with the tuberous sclerosis syndrome."],
   ["**2. الورم الوعائي العضلي الشحمي** ورم **عابي** يتكوّن من **الدهن والعضل الأملس والأوعية الدموية**.", "ويرتبط غالبًا **بمتلازمة التصلّب الحدبي**."]),
 F("angiomyolipoma.jpg", "Angiomyolipoma (B) — Vessels, Fat, Spindle cells, Thick hyalinized vessels with eccentric lumen", "الورم الوعائي العضلي الشحمي (B) — أوعية، دهن، خلايا مغزلية، أوعية سميكة متزجّجة ذات تجويف لا مركزي", h="54mm", fit="contain"),
 C("**3. ONCOCYTOMA** This tumor is comprised of cells with abundant granular acidophilic cytoplasm replete with mitochondria, as is the case in oncocytomas elsewhere in the body.",
   "**3. الورم الخلوي الحمضي (Oncocytoma)** يتكوّن من خلايا ذات **سايتوبلازم حبيبي حمضي وفير مملوء بالمتقدّرات (المايتوكوندريا)**، كما في الأورام الخلوية الحمضية في أماكن أخرى من الجسم."),
 F("oncocytoma.jpg", "Oncocytoma (histology)", "الورم الخلوي الحمضي (مقطع نسيجي)", h="50mm", fit="contain"),
 INSHORT([("Kidney tumors arise from **tubules, embryonic tissue, mesenchyme, renal pelvis epithelium**.", "تنشأ أورام الكلية من **النبيبات، النسيج الجنيني، المتوسطي، ظهارة الحوض**."),
          ("Benign: **adenoma** (small, tubules), **angiomyolipoma** (hamartoma: fat + smooth muscle + vessels; **tuberous sclerosis**), **oncocytoma** (granular acidophilic cytoplasm full of **mitochondria**).", "الحميدة: **الورم الغدّي** (صغير، نبيبات)، **الوعائي العضلي الشحمي** (عابي: دهن + عضل أملس + أوعية؛ **التصلّب الحدبي**)، **الخلوي الحمضي** (سايتوبلازم حبيبي حمضي مملوء **بالمايتوكوندريا**).")]),

 # ───────────────────────── 4. Malignant tumors
 SEC("B. MALIGNANT TUMORS OF THE KIDNEY", "ب. أورام الكلية الخبيثة"),
 L(["This cancer is the most common renal malignancy.",
    "It is more common in men, occurs most often from 50 to 70years of age, and has a higher incidence in cigarette smokers.",
    ["In some instances, it is associated with gene deletions in chromosome 3; renal cell carcinoma can also be associated with von Hippel-Lindau disease, which is caused by alterations in a gene localized to chromosome 3."]],
   ["هذا السرطان هو **أشيع خباثة كلوية**.",
    "وهو **أشيع في الرجال**، ويحدث غالبًا **بين 50 و70 سنة**، وإصابته **أعلى في مدخّني السجائر**.",
    ["وفي بعض الحالات يرتبط **بحذف جينات في الكروموسوم 3**؛ ويمكن أن ترتبط كارسينوما الخلايا الكلوية أيضًا **بداء فون هيبل-لينداو** الذي ينتج عن تغيّرات في جين يقع على **الكروموسوم 3**."]],
   en="**1. Renal cell carcinoma (RCC)**", ar="**1. كارسينوما الخلايا الكلوية (RCC)**", alpha=True),
 L(["Tobacco.", "Genetic factors.", "Cystic diseases of the kidneys."], ["**التبغ**.", "**العوامل الوراثية**.", "**الأمراض الكيسية** للكليتين."],
   en="**ETIOLOGY FACTORS.** Various etiologic factors implicated in the etiology of RCC are as follows:", ar="**العوامل المسبّبة.** العوامل المسبّبة المتّهمة في نشوء RCC هي:"),
 L(["Exposure to asbestos, heavy metals and petrochemical products.", "In women, obesity and oestrogen therapy.", "Analgesic nephropathy.", "Tuberous sclerosis."],
   ["التعرّض **للأسبستوس والمعادن الثقيلة والمنتجات البتروكيميائية**.", "في النساء، **السمنة والعلاج بالإستروجين**.", "**اعتلال الكلية بالمسكّنات**.", "**التصلّب الحدبي**."],
   en="**4. Other risk factors.** Besides above, following other factors are associated with higher incidence of RCC:", ar="**4. عوامل خطورة أخرى.** إضافةً لما سبق، ترتبط العوامل الآتية بزيادة الإصابة بـ RCC:", alpha=True),
 H2("2. WILMS TUMOR (NEPHROBLASTOMA)", "2. ورم ويلمز (الورم الأرومي الكلوي)"),
 L(["This cancer is the most common renal malignancy of early childhood.", "Incidence peaks in children 2 to 4 years of age.", "Wilms tumor originates from primitive metanephric tissue.",
    "Most often, the presenting feature is a palpable flank mass (often huge).", "Wilms tumor is often associated with deletions of the short arm of chromosome11."],
   ["هذا السرطان هو **أشيع خباثة كلوية في الطفولة المبكرة**.", "تبلغ الإصابة **ذروتها في الأطفال بعمر 2 إلى 4 سنوات**.", "ينشأ ورم ويلمز من **النسيج الكلوي التالي البدائي (metanephric)**.",
    "غالبًا تكون العلامة الأولى **كتلة خاصرة محسوسة** (غالبًا **ضخمة**).", "ويرتبط ورم ويلمز غالبًا **بحذف الذراع القصير للكروموسوم 11**."], alpha=True),
 FF(("wilms-baby.jpg", "Right kidney with Wilms’ tumor", "الكلية اليمنى مع ورم ويلمز", "48mm"),
    ("karyotype-del11p.jpg", "Karyotype: normal 11 and del(11)(p11.2p13)", "النمط النووي: الكروموسوم 11 الطبيعي وحذف del(11)(p11.2p13)", "48mm")),
 T([B("Feature", "الصفة"), B("Renal cell carcinoma", "كارسينوما الخلايا الكلوية"), B("Wilms tumor", "ورم ويلمز")],
   [[B("**Who**", "**من**"), B("men, 50–70 years; smokers", "الرجال، 50–70 سنة؛ المدخّنون"), B("children 2–4 years", "الأطفال 2–4 سنوات")],
    [B("**Rank**", "**المرتبة**"), B("most common renal malignancy", "أشيع خباثة كلوية"), B("most common renal malignancy of early childhood", "أشيع خباثة كلوية في الطفولة المبكرة")],
    [B("**Chromosome**", "**الكروموسوم**"), B("3 (deletions; von Hippel-Lindau)", "3 (حذف؛ فون هيبل-لينداو)"), B("11 short arm deletion", "حذف الذراع القصير لـ 11")],
    [B("**Origin / sign**", "**المنشأ / العلامة**"), B("—", "—"), B("primitive metanephric tissue; huge flank mass", "نسيج تالي بدائي؛ كتلة خاصرة ضخمة")]],
   key_cols=[0], widths=[22, 38, 40], style="summary", label_en="RCC vs Wilms tumor", label_ar="RCC مقابل ورم ويلمز"),
 INSHORT([("**RCC**: most common renal malignancy; men **50–70**, smokers; **chromosome 3**, **von Hippel-Lindau**.", "**RCC**: أشيع خباثة كلوية؛ رجال **50–70**، مدخّنون؛ **الكروموسوم 3**، **فون هيبل-لينداو**."),
          ("RCC risk: tobacco, genetics, cystic disease, asbestos / heavy metals / petrochemicals, obesity + oestrogen (women), analgesic nephropathy, tuberous sclerosis.", "خطورة RCC: التبغ، الوراثة، الأمراض الكيسية، الأسبستوس / المعادن الثقيلة / البتروكيميائيات، السمنة + الإستروجين (النساء)، اعتلال المسكّنات، التصلّب الحدبي."),
          ("**Wilms**: early childhood (**2–4 y**), metanephric tissue, **huge flank mass**, **11p deletion**.", "**ويلمز**: الطفولة المبكرة (**2–4 سنوات**)، نسيج تالي، **كتلة خاصرة ضخمة**، **حذف 11p**.")]),

 *TERMS6([("Nephrotic syndrome", "المتلازمة الكلائية / المتلازمة النفروزية"), ("Permeability", "النفاذية"), ("Glomerular filtrate", "الراشح الكبيبي"),
          ("Colloid osmotic (oncotic) pressure", "الضغط التناضحي الغرواني / الضغط الجاذب"), ("Hypoalbuminemia", "نقص ألبومين الدم"), ("Hypercholesterolemia", "فرط كوليسترول الدم"),
          ("Minimal-change disease", "داء التغيّر الأدنى"), ("Mesangium", "المسراق"), ("IgA nephropathy (Berger)", "اعتلال الكلية بـ IgA / داء بيرجر"),
          ("Henoch-Schönlein purpura", "فرفرية هينوخ-شونلاين / التهاب الأوعية بـ IgA"), ("Gross haematuria", "بيلة دموية عيانية"), ("Prognosis", "الإنذار / مآل المرض"),
          ("Adenoma", "الورم الغدّي"), ("Angiomyolipoma", "الورم الوعائي العضلي الشحمي"), ("Tuberous sclerosis", "التصلّب الحدبي / التصلّب الدرني"),
          ("Oncocytoma", "الورم الخلوي الحمضي / الورم الأونكوسيتي"), ("Renal cell carcinoma (RCC)", "كارسينوما الخلايا الكلوية"), ("von Hippel-Lindau disease", "داء فون هيبل-لينداو"),
          ("Wilms tumor (nephroblastoma)", "ورم ويلمز / الورم الأرومي الكلوي"), ("Metanephric tissue", "النسيج الكلوي التالي / ما بعد الكلوي"), ("Flank mass", "كتلة الخاصرة"),
          ("Urothelial carcinoma", "الكارسينوما الظهارية البولية")]),
]

def _chunk(blocks, n=2, minlen=4):
    out = []
    for b in blocks:
        le = b.get("list_en")
        if b.get("t") == "card" and le and len(le) >= minlen:
            st = b.get("start", 1)
            for i in range(0, len(le), n):
                d = dict(t="card", en=b["en"] if i == 0 else "", ar=b["ar"] if i == 0 else "",
                         list_en=le[i:i + n], list_ar=b["list_ar"][i:i + n])
                if b.get("alpha"): d["alpha"] = True
                if st + i != 1: d["start"] = st + i
                out.append(d)
        else:
            out.append(b)
    return out
blocks = _chunk(blocks)

exec(open(__file__.replace("p6.py", "p6q.py")).read())
