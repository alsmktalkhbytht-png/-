---
source: BIOS-Obsidian/tools/scripts/at4/a4.py
handouts: []
saved: 2026-10-31
tags: [bios, code]
---
# at4/a4.py

Utility script.

```python
import sys, re; sys.path.insert(0, "/tmp/claude-0/-home-claude/ff420988-e3a4-58e4-8344-8f014438cb53/scratchpad/imm456")
from ci import *            # c helpers + B INSHORT TERMS balance save(split.fix)

BN = lambda en, ar: N(en, ar, label=["BIOS note", "ملاحظة BIOS"])
O = P
def G(te, ta, en, ar): return dict(t="group", title_en=te, title_ar=ta, en=en, ar=ar)

blocks = [
 # ───────────────────────── 1
 SEC("Introduction", "المقدّمة"),
 C(["Proteins are fundamental biomolecules that perform diverse functions within the human body.",
    "They serve as **enzymes, hormones, transporters, antibodies, and structural components**.",
    "In biological fluids such as **plasma and urine**, the **concentration and composition** of proteins provide crucial **diagnostic information** about physiological and pathological states."],
   ["البروتينات جزيئات حيوية أساسية تؤدّي وظائف متنوّعة داخل جسم الإنسان.",
    "فهي تعمل **إنزيمات وهرمونات ونواقل وأضدادًا ومكوّنات بنائية**.",
    "وفي السوائل الحيوية مثل **البلازما والإدرار** يقدّم **تركيز البروتينات وتركيبها** **معلومات تشخيصية** حاسمة عن الحالات الفسيولوجية والمرضية."]),
 INSHORT([("Proteins = enzymes, hormones, transporters, antibodies, structure.", "البروتينات = إنزيمات، هرمونات، نواقل، أضداد، بناء."),
          ("Their **amount and type in plasma and urine** help diagnosis.", "**كمّيتها ونوعها في البلازما والإدرار** تساعد في التشخيص.")]),

 # ───────────────────────── 2
 SEC("Proteins in Plasma", "البروتينات في البلازما"),
 H2("2.1 Overview", "2.1 نظرة عامة"),
 C(["Plasma proteins constitute approximately **6–8 g/dL** of plasma.",
    "They are synthesized mainly in the **liver** (e.g., albumin, clotting factors) and in the **immune system** (e.g., immunoglobulins)."],
   ["تشكّل بروتينات البلازما نحو **6–8 غ/دل** من البلازما.",
    "وتُصنَّع بصورة رئيسية في **الكبد** (مثل الألبومين وعوامل التخثّر) وفي **الجهاز المناعي** (مثل الغلوبيولينات المناعية)."]),
 C("**Major classes:**", "**الأصناف الرئيسية:**"),
 L(["Maintains **colloid osmotic pressure (oncotic pressure)**", "Serves as a **carrier protein** for hormones, fatty acids, bilirubin, and drugs", "Acts as an **antioxidant**"],
   ["يحافظ على **الضغط التناضحي الغرواني (الضغط الورمي)**", "يعمل **بروتينًا ناقلًا** للهرمونات والأحماض الدهنية والبيليروبين والأدوية", "يعمل **مضادًا للأكسدة**"],
   en="1. **Albumin (~60% of total plasma protein)**", ar="1. **الألبومين (نحو 60% من بروتين البلازما الكلّي)**"),
 L(["**α1-Globulins:** α1-antitrypsin, α1-acid glycoprotein", "**α2-Globulins:** Haptoglobin, ceruloplasmin, α2-macroglobulin",
    "**β-Globulins:** Transferrin, complement proteins, lipoproteins", "**γ-Globulins:** Immunoglobulins (antibodies)"],
   ["**غلوبيولينات ألفا 1:** مضاد التربسين ألفا 1، والبروتين السكري الحامضي ألفا 1", "**غلوبيولينات ألفا 2:** الهابتوغلوبين، والسيرولوبلازمين، والغلوبيولين الكبروي ألفا 2",
    "**غلوبيولينات بيتا:** الترانسفيرين، وبروتينات المتمّم، والبروتينات الدهنية", "**غلوبيولينات غاما:** الغلوبيولينات المناعية (الأضداد)"],
   en="2. **Globulins (~35%)**", ar="2. **الغلوبيولينات (نحو 35%)**"),
 L(["A key **clotting factor** converted to **fibrin** during coagulation."], ["عامل **تخثّر** أساسي يتحوّل إلى **الفايبرين** أثناء التخثّر."],
   en="3. **Fibrinogen (~4%)**", ar="3. **الفايبرينوجين (نحو 4%)**"),
 T([B("Class", "الصنف"), B("Share", "النسبة"), B("Main points", "أهم النقاط")],
   [[B("**Albumin**", "**الألبومين**"), B("~60%", "نحو 60%"), B("oncotic pressure; carrier (hormones, fatty acids, bilirubin, drugs); antioxidant", "الضغط الورمي؛ ناقل (هرمونات، أحماض دهنية، بيليروبين، أدوية)؛ مضاد للأكسدة")],
    [B("**Globulins**", "**الغلوبيولينات**"), B("~35%", "نحو 35%"), B("α1, α2, β, γ (γ = immunoglobulins)", "ألفا 1، ألفا 2، بيتا، غاما (غاما = الغلوبيولينات المناعية)")],
    [B("**Fibrinogen**", "**الفايبرينوجين**"), B("~4%", "نحو 4%"), B("clotting factor → fibrin", "عامل تخثّر ← فايبرين")]],
   key_cols=[0], widths=[22, 16, 62], style="summary", label_en="Plasma protein classes", label_ar="أصناف بروتينات البلازما"),
 H2("2.2 Functions of Plasma Proteins", "2.2 وظائف بروتينات البلازما"),
 L(["Maintenance of **osmotic balance**", "**Transport** (e.g., albumin and transferrin)", "**Buffering capacity** (regulating blood pH)", "**Immune defense** (immunoglobulins, complement)", "**Coagulation** (clotting factors)", "**Nutrient reservoir**"],
   ["الحفاظ على **التوازن التناضحي**", "**النقل** (مثل الألبومين والترانسفيرين)", "**القدرة التنظيمية (الدارئة)** (تنظيم الأس الهيدروجيني للدم)", "**الدفاع المناعي** (الغلوبيولينات المناعية، المتمّم)", "**التخثّر** (عوامل التخثّر)", "**مخزون غذائي**"]),
 H2("2.3 Clinical Significance", "2.3 الأهمية السريرية"),
 L(["**Hypoproteinemia:** Due to **liver disease, malnutrition, nephrotic syndrome, or protein-losing enteropathy**",
    "**Hyperproteinemia:** Often caused by **dehydration** or **monoclonal gammopathies** (e.g., multiple myeloma)"],
   ["**نقص بروتينات الدم:** بسبب **أمراض الكبد، أو سوء التغذية، أو المتلازمة الكلوية، أو اعتلال الأمعاء المفقد للبروتين**",
    "**زيادة بروتينات الدم:** غالبًا بسبب **الجفاف** أو **اعتلالات الغاما وحيدة النسيلة** (مثل الورم النقوي المتعدّد)"]),
 L(["**Serum protein electrophoresis (SPEP)** separates plasma proteins into characteristic bands (**albumin, α1, α2, β, γ**)."],
   ["**الترحيل الكهربائي لبروتينات المصل (SPEP)** يفصل بروتينات البلازما إلى حزم مميّزة (**الألبومين، ألفا 1، ألفا 2، بيتا، غاما**)."],
   en="**Diagnostic tool:**", ar="**أداة التشخيص:**"),
 C("Abnormal patterns help diagnose diseases like **multiple myeloma** or **liver cirrhosis**.", "تساعد الأنماط غير الطبيعية في تشخيص أمراض مثل **الورم النقوي المتعدّد** أو **تشمّع الكبد**."),
 FLOW([("Albumin", "الألبومين"), ("α1", "ألفا 1"), ("α2", "ألفا 2"), ("β", "بيتا"), ("γ", "غاما")], en="SPEP bands", ar="حزم SPEP"),
 INSHORT([("Plasma protein **6–8 g/dL**: albumin **~60%**, globulins **~35%**, fibrinogen **~4%**; made in **liver** and **immune system**.", "بروتين البلازما **6–8 غ/دل**: ألبومين **نحو 60%**، غلوبيولينات **نحو 35%**، فايبرينوجين **نحو 4%**؛ يُصنع في **الكبد** و**الجهاز المناعي**."),
          ("Albumin = **oncotic pressure + carrier + antioxidant**; γ-globulins = **antibodies**.", "الألبومين = **ضغط ورمي + ناقل + مضاد أكسدة**؛ وغلوبيولينات غاما = **الأضداد**."),
          ("**Low** protein: liver disease, malnutrition, nephrotic syndrome, protein-losing enteropathy; **high**: dehydration, myeloma → **SPEP**.", "**نقص** البروتين: أمراض الكبد، سوء التغذية، المتلازمة الكلوية، اعتلال الأمعاء؛ **زيادته**: الجفاف، الورم النقوي ← **SPEP**.")]),

 # ───────────────────────── 3
 SEC("Proteins in Urine", "البروتينات في الإدرار"),
 H2("3.1 Normal Protein Excretion", "3.1 الإطراح الطبيعي للبروتين"),
 C("In healthy individuals, **<150 mg/day** of protein is excreted in urine.", "في الأشخاص الأصحّاء يُطرح **أقل من 150 ملغم/يوم** من البروتين في الإدرار."),
 L(["**Filtered plasma proteins** (mainly albumin, small peptides)", "**Secreted proteins from the renal tubules** (e.g., Tamm-Horsfall protein or uromodulin)"],
   ["**بروتينات البلازما المرشّحة** (غالبًا الألبومين والببتيدات الصغيرة)", "**بروتينات تفرزها النبيبات الكلوية** (مثل بروتين تام-هورسفول أو اليوروموديولين)"],
   en="**Origin:**", ar="**المنشأ:**"),
 L(["Produced by tubular cells of the **thick ascending limb of Henle’s loop**", "The **most abundant protein in normal urine**", "Plays roles in **defense against urinary tract infections** and **prevention of kidney stones.**"],
   ["تنتجه الخلايا النبيبية في **الطرف الصاعد السميك لعروة هنلي**", "**أكثر البروتينات وفرةً في الإدرار الطبيعي**", "له دور في **الدفاع ضد التهابات المسالك البولية** و**منع حصى الكلى.**"],
   en="**Tamm-Horsfall protein (uromodulin):**", ar="**بروتين تام-هورسفول (اليوروموديولين):**"),
 H2("3.2 Mechanisms Controlling Protein Filtration", "3.2 الآليات التي تتحكّم بترشيح البروتين"),
 R("**Glomerular barrier:** Prevents passage of **large or negatively charged** proteins like albumin.", "**الحاجز الكبيبي:** يمنع مرور البروتينات **الكبيرة أو السالبة الشحنة** مثل الألبومين."),
 R("**Tubular reabsorption:** **Low molecular weight** proteins filtered at the glomerulus are **reabsorbed by proximal tubules**.", "**إعادة الامتصاص النبيبي:** البروتينات **منخفضة الوزن الجزيئي** المرشّحة في الكبيبة **تعيد امتصاصها النبيبات القريبة**."),
 R("**Tubular secretion:** Adds specific proteins into urine (e.g., **uromodulin**).", "**الإفراز النبيبي:** يضيف بروتينات معيّنة إلى الإدرار (مثل **اليوروموديولين**)."),
 H2("3.3 Proteinuria (Abnormal Urinary Proteins)", "3.3 البيلة البروتينية (بروتينات الإدرار غير الطبيعية)"),
 C("Excessive urinary protein loss (**>150 mg/day**) indicates **renal or systemic disease**.", "فقدان البروتين المفرط في الإدرار (**أكثر من 150 ملغم/يوم**) يدلّ على **مرض كلوي أو جهازي**."),
 C("**Types of Proteinuria:**", "**أنواع البيلة البروتينية:**"),
 G("1. Glomerular Proteinuria", "1. البيلة البروتينية الكبيبية",
   ["Increased **glomerular permeability** (e.g., nephrotic syndrome, glomerulonephritis)", "Predominantly **albumin**"],
   ["زيادة **نفاذية الكبيبة** (مثل المتلازمة الكلوية، والتهاب كبيبات الكلى)", "غالبًا **الألبومين**"]),
 G("2. Tubular Proteinuria", "2. البيلة البروتينية النبيبية",
   ["**Defective tubular reabsorption** (e.g., interstitial nephritis)", "Presence of **low molecular weight** proteins (**β2-microglobulin**)"],
   ["**خلل إعادة الامتصاص النبيبي** (مثل التهاب الكلية الخلالي)", "وجود بروتينات **منخفضة الوزن الجزيئي** (**الغلوبيولين الصغير بيتا 2**)"]),
 G("3. Overflow Proteinuria", "3. البيلة البروتينية الفائضة",
   ["Excess plasma protein load **exceeds reabsorptive capacity**", "Example: **Bence Jones proteins (light chains)** in **multiple myeloma**"],
   ["حمل بروتين البلازما الزائد **يتجاوز قدرة إعادة الامتصاص**", "مثال: **بروتينات بنس جونز (السلاسل الخفيفة)** في **الورم النقوي المتعدّد**"]),
 G("4. Postrenal Proteinuria", "4. البيلة البروتينية بعد الكلوية",
   "Originates from **urinary tract** (infection, bleeding)", "تنشأ من **المسالك البولية** (التهاب، نزف)"),
 T([B("Type", "النوع"), B("Cause", "السبب"), B("Protein / example", "البروتين / مثال")],
   [[B("**Glomerular**", "**كبيبية**"), B("increased glomerular permeability", "زيادة نفاذية الكبيبة"), B("mainly albumin — nephrotic syndrome, glomerulonephritis", "ألبومين غالبًا — المتلازمة الكلوية، التهاب الكبيبات")],
    [B("**Tubular**", "**نبيبية**"), B("defective tubular reabsorption", "خلل إعادة الامتصاص النبيبي"), B("β2-microglobulin — interstitial nephritis", "بيتا 2 مايكروغلوبيولين — التهاب الكلية الخلالي")],
    [B("**Overflow**", "**فائضة**"), B("load exceeds reabsorptive capacity", "الحمل يتجاوز قدرة إعادة الامتصاص"), B("Bence Jones light chains — multiple myeloma", "سلاسل بنس جونز الخفيفة — الورم النقوي")],
    [B("**Postrenal**", "**بعد كلوية**"), B("urinary tract", "المسالك البولية"), B("infection, bleeding", "التهاب، نزف")]],
   key_cols=[0], widths=[18, 38, 44], style="summary", label_en="Types of proteinuria", label_ar="أنواع البيلة البروتينية"),
 H2("3.4 Diagnostic Assessment", "3.4 التقييم التشخيصي"),
 L(["**Dipstick test:** Detects **mainly albumin** (semi-quantitative)", "**24-hour urine protein estimation:** **Gold standard**",
    "**Spot urine protein-to-creatinine ratio:** Convenient alternative", "**Electrophoresis & Immunofixation:** Identify specific proteins (e.g., **monoclonal light chains**)"],
   ["**فحص الشريط:** يكشف **الألبومين غالبًا** (شبه كمّي)", "**تقدير بروتين إدرار 24 ساعة:** **المعيار الذهبي**",
    "**نسبة البروتين إلى الكرياتينين في عيّنة إدرار عشوائية:** بديل مريح", "**الترحيل الكهربائي والتثبيت المناعي:** تحديد بروتينات معيّنة (مثل **السلاسل الخفيفة وحيدة النسيلة**)"]),
 INSHORT([("Normal urine protein **< 150 mg/day**; most abundant = **Tamm-Horsfall (uromodulin)** from the thick ascending limb of Henle.", "بروتين الإدرار الطبيعي **أقل من 150 ملغم/يوم**؛ وأكثره وفرةً = **تام-هورسفول (اليوروموديولين)** من الطرف الصاعد السميك لعروة هنلي."),
          ("Glomerular → **albumin**; tubular → **β2-microglobulin**; overflow → **Bence Jones** (myeloma); postrenal → infection, bleeding.", "الكبيبية ← **ألبومين**؛ النبيبية ← **بيتا 2 مايكروغلوبيولين**؛ الفائضة ← **بنس جونز** (الورم النقوي)؛ بعد الكلوية ← التهاب، نزف."),
          ("**24-hour urine = gold standard**; dipstick = mainly albumin; protein/creatinine ratio = convenient.", "**إدرار 24 ساعة = المعيار الذهبي**؛ الشريط = ألبومين غالبًا؛ نسبة البروتين/الكرياتينين = بديل مريح.")]),

 # ───────────────────────── 4
 SEC("Comparison Summary", "خلاصة المقارنة"),
 T([B("Parameter", "المعيار"), B("Plasma Proteins", "بروتينات البلازما"), B("Urine Proteins", "بروتينات الإدرار")],
   [[B("Normal concentration", "التركيز الطبيعي"), B("6–8 g/dL", "6–8 غ/دل"), B("<150 mg/day", "أقل من 150 ملغم/يوم")],
    [B("Main proteins", "البروتينات الرئيسية"), B("Albumin, globulins, fibrinogen", "الألبومين، الغلوبيولينات، الفايبرينوجين"), B("Uromodulin, trace albumin", "اليوروموديولين، آثار من الألبومين")],
    [B("Origin", "المنشأ"), B("Liver, immune cells", "الكبد، الخلايا المناعية"), B("Plasma filtration, tubular secretion", "ترشيح البلازما، الإفراز النبيبي")],
    [B("Clinical value", "القيمة السريرية"), B("Nutritional, hepatic, and immune status", "الحالة الغذائية والكبدية والمناعية"), B("Renal function assessment", "تقييم وظيفة الكلى")]],
   key_cols=[0], widths=[26, 37, 37]),

 # ───────────────────────── 5
 SEC("Conclusion", "الخاتمة"),
 C("Proteins in plasma and urine provide essential insights into **body homeostasis and disease**.", "تقدّم البروتينات في البلازما والإدرار رؤى أساسية عن **توازن الجسم والمرض**."),
 L(["Plasma proteins reflect **liver function, nutritional state, and immune activity**.", "Urinary proteins serve as sensitive indicators of **kidney health and systemic disorders**."],
   ["تعكس بروتينات البلازما **وظيفة الكبد والحالة الغذائية والنشاط المناعي**.", "وتعمل بروتينات الإدرار مؤشّرات حسّاسة على **صحّة الكلى والاضطرابات الجهازية**."]),
 C("Modern diagnostic techniques, including **electrophoresis and immunoassays**, continue to enhance our ability to detect and monitor protein abnormalities for **early disease intervention**.",
   "تواصل تقنيات التشخيص الحديثة، ومنها **الترحيل الكهربائي والمقايسات المناعية**، تعزيز قدرتنا على كشف اضطرابات البروتين ومتابعتها **للتدخّل المبكر في المرض**."),
 INSHORT([("Plasma proteins → **liver, nutrition, immunity**; urine proteins → **kidney** and systemic disease.", "بروتينات البلازما ← **الكبد والتغذية والمناعة**؛ وبروتينات الإدرار ← **الكلى** والأمراض الجهازية."),
          ("Tools: **electrophoresis and immunoassays**.", "الأدوات: **الترحيل الكهربائي والمقايسات المناعية**.")]),

 *TERMS([("Plasma proteins", "بروتينات البلازما / بروتينات الدم"),
         ("Albumin", "الألبومين / الزلال"),
         ("Globulins", "الغلوبيولينات / الكريّنات"),
         ("Fibrinogen / Fibrin", "مولّد الليفين (الفايبرينوجين) / الليفين (الفايبرين)"),
         ("Oncotic (colloid osmotic) pressure", "الضغط الورمي / الضغط التناضحي الغرواني"),
         ("Haptoglobin", "الهابتوغلوبين / رابط الهيموغلوبين"),
         ("Ceruloplasmin", "السيرولوبلازمين / حامل النحاس"),
         ("Transferrin", "الترانسفيرين / ناقل الحديد"),
         ("Immunoglobulins", "الغلوبيولينات المناعية / الأضداد"),
         ("Hypoproteinemia / Hyperproteinemia", "نقص / زيادة بروتينات الدم"),
         ("Nephrotic syndrome", "المتلازمة الكلوية / المتلازمة النفروزية"),
         ("Protein-losing enteropathy", "اعتلال الأمعاء المفقد للبروتين"),
         ("Monoclonal gammopathy", "اعتلال الغاما وحيد النسيلة"),
         ("Multiple myeloma", "الورم النقوي المتعدّد / المايلوما"),
         ("Serum protein electrophoresis (SPEP)", "الترحيل الكهربائي لبروتينات المصل"),
         ("Tamm-Horsfall protein (uromodulin)", "بروتين تام-هورسفول / اليوروموديولين"),
         ("Proteinuria", "البيلة البروتينية / بروتين في الإدرار"),
         ("Glomerular barrier", "الحاجز الكبيبي / حاجز الترشيح"),
         ("β2-microglobulin", "الغلوبيولين الصغير بيتا 2 / بيتا 2 مايكروغلوبيولين"),
         ("Bence Jones proteins", "بروتينات بنس جونز / السلاسل الخفيفة الحرّة"),
         ("Dipstick", "الشريط / شريط الغمس"),
         ("Protein-to-creatinine ratio", "نسبة البروتين إلى الكرياتينين"),
         ("Immunofixation", "التثبيت المناعي")]),
]

exec(open(__file__.replace("a4.py", "a4q.py")).read())

```
