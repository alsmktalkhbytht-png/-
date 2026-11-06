---
source: BIOS-Obsidian/tools/scripts/pat5/p5.py
handouts: []
saved: 2026-11-06
tags: [bios, code]
---
# pat5/p5.py

Utility script.

```python
import sys, re; sys.path.insert(0, "/tmp/claude-0/-home-claude/4a281dcf-357b-50ce-b2f4-8802cfcc6472/scratchpad/imm456")
from ci import *            # c helpers + B INSHORT TERMS balance save(split.fix)
import split
split.ABBR = split.ABBR + ("e.g",)

# Pathology — lecture 5 (stage 4) — د. حامد خليل التميمي — Glomerular Diseases
# The PDF text layer splits words ("st ructure"); text taken from the slides as displayed.

BN = lambda en, ar: N(en, ar, label=["BIOS note", "ملاحظة BIOS"])
O = P
def TERMS6(terms, n=6):
    head = [B("Term", "المصطلح"), "الترجمات العربية المستعملة"]
    return [SEC("Key terms", "أهم المصطلحات")] + [T(head, [[f"**{e}**", a] for e, a in terms[i:i + n]], ar_cols=[1], widths=[36, 64])
                                                  for i in range(0, len(terms), n)]

blocks = [
 # ───────────────────────── 1. Kidney
 SEC("FUNCTIONS OF KIDNEYS", "وظائف الكليتين"),
 L(["excreting waste products,", "regulating body fluid and solute balance,", "regulating blood pressure,", "secreting hormones."],
   ["**إخراج الفضلات**،", "**تنظيم توازن سوائل الجسم والمذابات**،", "**تنظيم ضغط الدم**،", "**إفراز الهرمونات**."],
   en="The kidney has an intricate structure that underlies its diverse roles of", ar="للكلية **تركيب معقّد** يقوم عليه دورها المتنوّع في:"),
 F("kidney.jpg", "Kidney — Cortex, Medulla, Renal Pelvis, Renal Artery, Renal Vein, Ureter", "الكلية — القشرة، اللبّ، الحوض الكلوي، الشريان الكلوي، الوريد الكلوي، الحالب", h="56mm", fit="contain"),
 L(["The renal corpuscle: glomerulus and Bowman capsule", "Proximal convoluted tubules (PCT, located in the renal cortex)", "Descending loop of Henle (LOH)",
    "Ascending convoluted tubule limb (which resides in the renal medulla, leading to the thick ascending limb)", "Thick ascending limb", "Distal convoluted tubule",
    "Collecting duct (which opens into the renal papilla)"],
   ["**الجسيم الكلوي**: الكبيبة ومحفظة بومان", "**النبيبات الملتفّة القريبة** (PCT، في قشرة الكلية)", "**الطرف النازل لعروة هنلي** (LOH)",
    "**الطرف الصاعد** (يقع في لبّ الكلية، ويؤدّي إلى الطرف الصاعد الثخين)", "**الطرف الصاعد الثخين**", "**النبيب الملتفّ البعيد**",
    "**القناة الجامعة** (تنفتح في الحليمة الكلوية)"],
   en="**The functional renal unit is the nephron,** which is composed of the following:", ar="**الوحدة الوظيفية للكلية هي النفرون (الكليون)**، ويتكوّن مما يأتي:"),
 BN("“Ascending convoluted tubule limb” on the slide is the **thin ascending limb** of the loop of Henle.", "“Ascending convoluted tubule limb” في الشريحة يقصد بها **الطرف الصاعد الرقيق** لعروة هنلي."),
 FF(("nephron.jpg", "Nephron — Bowman’s Capsule, Glomerulus, Proximal and Distal Convoluted Tubule, Loop of Henle, Vasa Recta, Collecting Duct",
     "النفرون — محفظة بومان، الكبيبة، النبيب الملتفّ القريب والبعيد، عروة هنلي، الأوعية المستقيمة، القناة الجامعة", "62mm"),
    ("renal-corpuscle.jpg", "Renal corpuscle — Bowman’s capsule, Afferent and Efferent arteriole, Proximal tubule",
     "الجسيم الكلوي — محفظة بومان، الشُرَيّن الوارد والصادر، النبيب القريب", "62mm")),
 INSHORT([("Kidney functions: **excretion, fluid/solute balance, blood pressure, hormones**.", "وظائف الكلية: **الإخراج، توازن السوائل/المذابات، ضغط الدم، الهرمونات**."),
          ("Nephron: **renal corpuscle (glomerulus + Bowman capsule) → PCT → loop of Henle → thick ascending limb → DCT → collecting duct**.", "النفرون: **الجسيم الكلوي (كبيبة + محفظة بومان) ← PCT ← عروة هنلي ← الطرف الصاعد الثخين ← DCT ← القناة الجامعة**.")]),

 # ───────────────────────── 2. Glomerular diseases
 SEC("GLOMERULAR DISEASES", "أمراض الكبيبات"),
 C("Glomerular diseases are typically caused by disturbances of structure.", "تنتج أمراض الكبيبات عادةً عن **اضطرابات في التركيب**."),
 L(["Endothelial cells lining the capillary", "Glomerular basement membrane", "Mesangium.",
    ["Epithelial cells or podocytes, which form an outer coating to the capillary.", "These cells are in contact with the outer surface of the basement membrane via a series of foot processes."]],
   ["**الخلايا البطانية** المبطّنة للشعيرة", "**الغشاء القاعدي الكبيبي**", "**المسراق (Mesangium)**.",
    ["**الخلايا الظهارية أو الخلايا القدمية (podocytes)** التي تكوّن غطاءً خارجيًا للشعيرة.", "وتتّصل هذه الخلايا بالسطح الخارجي للغشاء القاعدي عبر سلسلة من **الزوائد القدمية**."]],
   en="**Four significant components of the glomerulus may be damaged:**", ar="**أربعة مكوّنات مهمة للكبيبة قد تتضرّر:**"),
 H2("AETIOLOGY OF GLOMERULAR DISEASES", "سببيات أمراض الكبيبات"),
 L(["Primary (majority)—idiopathic", "Secondary—disease process is secondary to systemic disease", "Hereditary—Alport’s syndrome, Fabry’s syndrome and congenital nephrotic syndrome."],
   ["**أولية (الأغلبية)** — مجهولة السبب", "**ثانوية** — العملية المرضية ثانوية لمرض جهازي", "**وراثية** — متلازمة ألبورت، ومتلازمة فابري، والمتلازمة الكلائية الخلقية."],
   en="**Glomerular diseases may be classified as :**", ar="**يمكن تصنيف أمراض الكبيبات إلى:**"),
 C(["Glomerular diseases encompass a large and clinically significant group of renal diseases.",
    "Glomerulonephritis (GN) or Bright’s disease is the term used for diseases that primarily involve the renal glomeruli."],
   ["تشمل أمراض الكبيبات **مجموعة كبيرة ومهمة سريريًا** من أمراض الكلية.",
    "**التهاب الكبيبات والكلية (GN)** أو **داء برايت** هو المصطلح المستعمل للأمراض التي تصيب **كبيبات الكلية أساسًا**."]),
 L(["Primary glomerular diseases", "Secondary glomerular diseases", "inherited glomerular diseases"],
   ["أمراض الكبيبات **الأولية**", "أمراض الكبيبات **الثانوية**", "أمراض الكبيبات **الموروثة**"],
   en="It is convenient to classify glomerular diseases into 3 broad groups:", ar="من الملائم تصنيف أمراض الكبيبات إلى **3 مجموعات واسعة**:"),
 INSHORT([("Glomerular diseases = disturbances of **structure** of 4 components: **endothelium, GBM, mesangium, podocytes**.", "أمراض الكبيبات = اضطرابات **تركيب** 4 مكوّنات: **البطانة، الغشاء القاعدي، المسراق، الخلايا القدمية**."),
          ("Causes: **primary (majority, idiopathic)**, secondary (systemic), hereditary (Alport, Fabry, congenital nephrotic).", "الأسباب: **أولية (الأغلبية، مجهولة)**، ثانوية (جهازية)، وراثية (ألبورت، فابري، الكلائية الخلقية)."),
          ("GN = **Bright’s disease**.", "التهاب الكبيبات = **داء برايت**.")]),

 # ───────────────────────── 3. Classification
 SEC("Classification of glomerular diseases", "تصنيف أمراض الكبيبات"),
 L(["Acute GN — i) Post-streptococcal, ii) Non-streptococcal", "Rapidly progressive GN", "Minimal change disease", "Membranous GN", "Membrano-proliferative GN",
    "Focal and diffuse proliferative GN", "Focal segmental glomerulosclerosis (FSGS)", "IgA nephropathy", "Chronic glomerulonephritis"],
   ["التهاب الكبيبات الحاد — i) تالٍ للمكوّرات العقدية، ii) غير عقدي", "التهاب الكبيبات **سريع التقدّم**", "**داء التغيّر الأدنى**", "التهاب الكبيبات **الغشائي**", "التهاب الكبيبات **الغشائي التكاثري**",
    "التهاب الكبيبات **التكاثري البؤري والمنتشر**", "**التصلّب الكبيبي البؤري القطعي (FSGS)**", "**اعتلال الكلية بـ IgA**", "التهاب الكبيبات **المزمن**"],
   en="**I. PRIMARY GLOMERULONEPHRITIS**", ar="**I. التهاب الكبيبات والكلية الأولي**"),
 L(["Lupus nephritis (SLE)", "Diabetic nephropathy", "Amyloidosis", "Polyarteritis nodosa", "Wegener’s granulomatosis(inflammation of the blood vessels in kidneys).",
    "Goodpasture’s syndrome(antibodies that attack the kidneys).", "Henoch-Schönlein purpura (also known as IgA vasculitis)",
    "Systemic infectious diseases (bacterial e.g. bacterial endocarditis, syphilis, leprosy; viral e.g. HBV, HCV, HIV; parasitic e.g. falciparum malaria, filariasis)",
    "Idiopathic mixed cryoglobulinaemia"],
   ["**التهاب الكلية الذئبي** (الذئبة الحمامية الجهازية)", "**اعتلال الكلية السكري**", "**الداء النشواني**", "**التهاب الشرايين العقدي المتعدّد**", "**ورام فيغنر الحبيبي** (التهاب الأوعية الدموية في الكلية).",
    "**متلازمة غودباستشر** (أضداد تهاجم الكلية).", "**فرفرية هينوخ-شونلاين** (وتعرف أيضًا بالتهاب الأوعية بـ IgA)",
    "**الأمراض المعدية الجهازية** (بكتيرية مثل التهاب الشغاف البكتيري والزهري والجذام؛ فيروسية مثل HBV وHCV وHIV؛ طفيلية مثل الملاريا المنجلية وداء الخيطيات)",
    "**الغلوبيولين البردي المختلط مجهول السبب**"],
   en="**II. SECONDARY SYSTEMIC GLOMERULAR DISEASES**", ar="**II. أمراض الكبيبات الجهازية الثانوية**"),
 L(["Alport’s syndrome", "Fabry’s disease", "Nail-patella syndrome"], ["**متلازمة ألبورت**", "**داء فابري**", "**متلازمة الظفر-الرضفة**"],
   en="**III. HEREDITARY NEPHRITIS**", ar="**III. التهاب الكلية الوراثي**"),
 INSHORT([("Primary GN: **9** types (acute post-/non-streptococcal, RPGN, minimal change, membranous, MPGN, proliferative, FSGS, **IgA**, chronic).", "الأولي: **9** أنواع (الحاد التالي/غير العقدي، سريع التقدّم، التغيّر الأدنى، الغشائي، الغشائي التكاثري، التكاثري، FSGS، **IgA**، المزمن)."),
          ("Secondary: **SLE, diabetes, amyloidosis**, PAN, Wegener, Goodpasture, HSP, infections, cryoglobulinaemia.", "الثانوي: **الذئبة، السكري، النشواني**، PAN، فيغنر، غودباستشر، HSP، العدوى، الغلوبيولين البردي."),
          ("Hereditary: **Alport, Fabry, nail-patella**.", "الوراثي: **ألبورت، فابري، الظفر-الرضفة**.")]),

 # ───────────────────────── 4. Clinical manifestations + IgA
 SEC("CLINICAL MANIFESTATIONS", "المظاهر السريرية"),
 L(["Proteinuria,", "Haematuria,", "Hypertension", "Disturbed excretory function."],
   ["**البيلة البروتينية**،", "**البيلة الدموية**،", "**ارتفاع ضغط الدم**", "**اضطراب الوظيفة الإخراجية**."],
   en="The clinical presentation of glomerular disease is quite variable but in general four features are present in varying combinations depending upon the underlying condition.",
   ar="يتباين العرض السريري لأمراض الكبيبات كثيرًا، لكن عمومًا توجد **أربع صفات** بتراكيب مختلفة حسب الحالة الأساسية."),
 C("A firm diagnosis, however, can be established by examination of renal biopsy under light, electron and immunofluorescence microscopy.",
   "ومع ذلك، يمكن تأكيد التشخيص **بفحص خزعة الكلية** تحت المجهر **الضوئي والإلكتروني والتألّق المناعي**."),
 H2("IGA NEPHROPATHY (BERGER DISEASE)", "اعتلال الكلية بـ IgA (داء بيرجر)"),
 C(["**Pathogenesis:** The mechanism is unknown.", "There is a possible entrapment of circulating immune complexes with activation of the alternate complement pathway.",
    "There is also a possible genetic predisposition.", "Most common cause of glomerulonephritis in the world"],
   ["**الإمراضية:** الآلية **غير معروفة**.", "هناك احتمال **احتباس معقّدات مناعية دائرة** مع **تنشيط المسار البديل للمتمّمة**.",
    "وهناك أيضًا احتمال **استعداد وراثي**.", "**أشيع سبب لالتهاب الكبيبات في العالم**"]),
 F("iga-nephropathy.jpg", "IgA NEPHROPATHY — abnormal IgA1 + anti-glycan auto-antibody → immune complex deposits in the glomerulus; most common nephropathy; nephritic syndrome",
   "اعتلال الكلية بـ IgA — IgA1 شاذ + ضد ذاتي مضاد للغليكان ← ترسّب المعقّد المناعي في الكبيبة؛ أشيع اعتلال كلوي؛ متلازمة التهاب الكلية", h="56mm", fit="contain"),
 INSHORT([("4 features: **proteinuria, haematuria, hypertension, disturbed excretion**; firm diagnosis by **renal biopsy** (light, EM, IF).", "4 صفات: **بيلة بروتينية، بيلة دموية، ارتفاع الضغط، اضطراب الإخراج**؛ التأكيد **بخزعة الكلية** (ضوئي، إلكتروني، تألّق مناعي)."),
          ("**IgA nephropathy (Berger)**: immune complexes + **alternate complement pathway**, genetic; **most common GN in the world**.", "**اعتلال IgA (بيرجر)**: معقّدات مناعية + **المسار البديل للمتمّمة**، وراثي؛ **أشيع التهاب كبيبات في العالم**.")]),

 # ───────────────────────── 5. Major glomerular syndromes
 SEC("MAJOR GLOMERULAR SYNDROMES", "المتلازمات الكبيبية الرئيسية"),
 C("Following six are commonly found in different glomerular diseases:", "الست الآتية شائعة في أمراض الكبيبات المختلفة:"),
 C(["**I. Acute Nephritic Syndrome** This is the acute onset of microscopic haematuria, mild proteinuria, hypertension, oedema and oliguria .",
    "The underlying causes of acute nephritic syndrome may be primary glomerulonephritic diseases (classically acute glomerulonephritis and rapidly progressive glomerulonephritis) or certain systemic diseases."],
   ["**I. متلازمة التهاب الكلية الحادة** وهي البدء الحاد لـ**بيلة دموية مجهرية، وبيلة بروتينية خفيفة، وارتفاع ضغط، ووذمة، وقلّة بول**.",
    "وقد تكون أسبابها **أمراض التهاب الكبيبات الأولية** (تقليديًا **التهاب الكبيبات الحاد** و**سريع التقدّم**) أو أمراض جهازية معيّنة."]),
 L(["Massive proteinuria,", "Hypoalbuminaemia,", "Oedema,", "Hyperlipidaemia,", "Lipiduria ,", "Hypercoagulability."],
   ["**بيلة بروتينية هائلة**،", "**نقص ألبومين الدم**،", "**الوذمة**،", "**فرط شحوم الدم**،", "**البيلة الدهنية**،", "**فرط التخثّر**."],
   en="**II. NEPHROTIC SYNDROME** — Nephrotic syndrome is a constellation of features in different diseases having varying pathogenesis; it is characterised by findings of;",
   ar="**II. المتلازمة الكلائية** — مجموعة صفات في أمراض مختلفة ذات إمراضية متباينة؛ وتتميّز بـ:"),
 L(["In children, primary glomerulonephritis is the cause in majority of cases of the nephrotic syndrome; most frequent being lipoid nephrosis (65%) .",
    "In adults, on the other hand, systemic diseases (diabetes, amyloidosis and SLE)are more frequent causes of nephrotic syndrome .",
    "The most common primary glomerular disease in adults is membranous glomerulonephritis (40%)."],
   ["في **الأطفال** يكون التهاب الكبيبات الأولي سبب أغلب حالات المتلازمة الكلائية؛ وأشيعها **الكلاء الشحمي (lipoid nephrosis) (65%)**.",
    "أما في **البالغين** فالأمراض الجهازية (**السكري والنشواني والذئبة**) أكثر أسبابها شيوعًا.",
    "وأشيع مرض كبيبي أولي في البالغين هو **التهاب الكبيبات الغشائي (40%)**."]),
 F("membranous.png", "Normal → Membranous glomerulopathy: antibody + antigen → immune complexes along the basement membrane (endothelial cell, basement membrane, epithelial cell)",
   "الطبيعي ← الاعتلال الكبيبي الغشائي: ضد + مستضد ← معقّدات مناعية على الغشاء القاعدي (خلية بطانية، غشاء قاعدي، خلية ظهارية)", h="56mm", fit="contain"),
 T([B("Feature", "الصفة"), B("Nephritic", "التهاب الكلية"), B("Nephrotic", "الكلائية")],
   [[B("**Proteinuria**", "**البيلة البروتينية**"), B("mild", "خفيفة"), B("massive", "هائلة")],
    [B("**Haematuria**", "**البيلة الدموية**"), B("microscopic", "مجهرية"), B("—", "—")],
    [B("**Other**", "**أخرى**"), B("hypertension, oedema, oliguria", "ارتفاع ضغط، وذمة، قلّة بول"), B("hypoalbuminaemia, oedema, hyperlipidaemia, lipiduria, hypercoagulability", "نقص ألبومين، وذمة، فرط شحوم، بيلة دهنية، فرط تخثّر")],
    [B("**Typical cause**", "**السبب النموذجي**"), B("acute GN, RPGN", "التهاب الكبيبات الحاد، سريع التقدّم"), B("children: lipoid nephrosis 65%; adults: membranous 40% / systemic", "الأطفال: الكلاء الشحمي 65%؛ البالغون: الغشائي 40% / جهازية")]],
   key_cols=[0], widths=[22, 36, 42], style="summary", label_en="Nephritic vs nephrotic", label_ar="التهاب الكلية مقابل الكلائية"),
 C("**III. ACUTE RENAL FAILURE** Acute renal failure (ARF) is characterised by rapid decline in renal function. ARF has many causes including glomerular disease, principally rapidly progressive GN and acute diffuse proliferative GN.",
   "**III. الفشل الكلوي الحاد** يتميّز الفشل الكلوي الحاد (ARF) **بتدهور سريع في وظيفة الكلية**. وله أسباب كثيرة منها أمراض الكبيبات، وأهمها **التهاب الكبيبات سريع التقدّم** و**التهاب الكبيبات التكاثري المنتشر الحاد**."),
 C(["**IV. CHRONIC RENAL FAILURE** These cases have advanced renal impairment progressing over years and is detected by significant proteinuria, haematuria, hypertension and azotaemia.",
    "Such patients generally have small contracted kidneys due to chronic glomerulonephritis."],
   ["**IV. الفشل الكلوي المزمن** لهذه الحالات **قصور كلوي متقدّم يتطوّر عبر سنوات**، ويُكشف ببيلة بروتينية واضحة وبيلة دموية وارتفاع ضغط و**آزوتيميا (ارتفاع نواتج النتروجين في الدم)**.",
    "ولدى هؤلاء المرضى عمومًا **كلى صغيرة متقلّصة** بسبب التهاب الكبيبات المزمن."]),
 F("normal-diseased-kidney.jpg", "Normal kidney (glomerulus, collecting tubules) vs Diseased kidney (scar tissue, damaged glomerulus, damaged tubules)",
   "كلية طبيعية (كبيبة، نبيبات جامعة) مقابل كلية مريضة (نسيج ندبي، كبيبة متضرّرة، نبيبات متضرّرة)", h="58mm", fit="contain"),
 C("**V. ASYMPTOMATIC PROTEINURIA** Presence of proteinuria unexpectedly in a patient may be unrelated to renal disease (e.g. exercise - induced, extreme lordosis and orthostatic proteinuria), or may indicate an underlying mild glomerulonephritis.",
   "**V. البيلة البروتينية اللاعرضية** وجود بيلة بروتينية بشكل غير متوقّع قد يكون **غير متعلّق بمرض كلوي** (مثل الناتجة عن **الجهد**، و**التقعّر القطني الشديد**، و**البيلة البروتينية الانتصابية**)، أو قد يدلّ على **التهاب كبيبات خفيف**."),
 L(["Diseases of the glomerulus, Renal interstitium, Calyceal system, Ureter, bladder, prostate, urethra, and underlying bleeding disorder.", "Congenital abnormalities of the kidneys", "Neoplasia."],
   ["أمراض **الكبيبة**، و**النسيج الخلالي الكلوي**، و**الجهاز الكأسي**، و**الحالب** و**المثانة** و**البروستات** و**الإحليل**، و**اضطراب نزفي** أساسي.", "**التشوّهات الخلقية** للكليتين", "**الأورام**."],
   en="**VI. ASYMPTOMATIC HAEMATURIA** Asymptomatic microscopic haematuria is common in children and young adolescents and has many diverse causes such as",
   ar="**VI. البيلة الدموية اللاعرضية** البيلة الدموية المجهرية اللاعرضية **شائعة في الأطفال واليافعين** ولها أسباب متنوّعة مثل"),
 INSHORT([("**Nephritic**: microscopic haematuria, mild proteinuria, hypertension, oedema, oliguria.", "**التهاب الكلية**: بيلة دموية مجهرية، بروتينية خفيفة، ارتفاع ضغط، وذمة، قلّة بول."),
          ("**Nephrotic**: massive proteinuria, hypoalbuminaemia, oedema, hyperlipidaemia, lipiduria, hypercoagulability; children → **lipoid nephrosis 65%**; adults → **membranous 40%** (primary) / systemic.", "**الكلائية**: بروتينية هائلة، نقص ألبومين، وذمة، فرط شحوم، بيلة دهنية، فرط تخثّر؛ الأطفال ← **الكلاء الشحمي 65%**؛ البالغون ← **الغشائي 40%** (أولي) / جهازية."),
          ("ARF: rapid decline (RPGN, acute diffuse proliferative GN); CRF: years, azotaemia, **small contracted kidneys**.", "الحاد: تدهور سريع (سريع التقدّم، التكاثري المنتشر الحاد)؛ المزمن: سنوات، آزوتيميا، **كلى صغيرة متقلّصة**."),
          ("Asymptomatic proteinuria (exercise, lordosis, orthostatic) and haematuria (common in children; many causes).", "البيلة البروتينية اللاعرضية (جهد، تقعّر، انتصابية) والدموية (شائعة في الأطفال؛ أسباب كثيرة).")]),

 *TERMS6([("Nephron", "النفرون / الكليون / الوحدة الكلوية"), ("Glomerulus", "الكبيبة"), ("Bowman capsule", "محفظة بومان"),
          ("Loop of Henle", "عروة هنلي"), ("Podocyte", "الخلية القدمية / الخلية الظهارية الحشوية"), ("Mesangium", "المسراق / النسيج بين الشعيرات"),
          ("Glomerular basement membrane", "الغشاء القاعدي الكبيبي"), ("Glomerulonephritis (GN)", "التهاب الكبيبات والكلية / داء برايت"), ("Idiopathic", "مجهول السبب"),
          ("Minimal change disease", "داء التغيّر الأدنى / الكلاء الشحمي"), ("FSGS", "التصلّب الكبيبي البؤري القطعي"), ("IgA nephropathy (Berger)", "اعتلال الكلية بـ IgA / داء بيرجر"),
          ("Alternate complement pathway", "المسار البديل للمتمّمة"), ("Nephritic syndrome", "متلازمة التهاب الكلية"), ("Nephrotic syndrome", "المتلازمة الكلائية / المتلازمة النفروزية"),
          ("Proteinuria", "البيلة البروتينية / البروتين في البول"), ("Haematuria", "البيلة الدموية / الدم في البول"), ("Oliguria", "قلّة البول"),
          ("Hypoalbuminaemia", "نقص ألبومين الدم"), ("Lipiduria", "البيلة الدهنية"), ("Azotaemia", "الآزوتيميا / ارتفاع اليوريا في الدم"),
          ("Orthostatic proteinuria", "البيلة البروتينية الانتصابية / الوضعية")]),
]

def _chunk(blocks, n=2, minlen=4):
    """Split long numbered lists into cards of n points (numbering continues) so pages fill."""
    out = []
    for b in blocks:
        le = b.get("list_en")
        if b.get("t") == "card" and le and len(le) >= minlen and not b.get("alpha"):
            st = b.get("start", 1)
            for i in range(0, len(le), n):
                d = dict(t="card", en=b["en"] if i == 0 else "", ar=b["ar"] if i == 0 else "",
                         list_en=le[i:i + n], list_ar=b["list_ar"][i:i + n])
                if st + i != 1: d["start"] = st + i
                out.append(d)
        else:
            out.append(b)
    return out
blocks = _chunk(blocks)

exec(open(__file__.replace("p5.py", "p5q.py")).read())

```
