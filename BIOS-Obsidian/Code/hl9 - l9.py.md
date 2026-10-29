---
source: BIOS-Obsidian/tools/scripts/hl9/l9.py
handouts: [hematology-lec9-hemolytic]
saved: 2026-10-29
tags: [bios, code]
---
# hl9/l9.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#hematology-lec9-hemolytic|hematology-lec9-hemolytic]]

```python
import sys; sys.path.insert(0, "/tmp/claude-0/-home-user--/8f878068-bae9-502b-96f7-788f221c7cb0/scratchpad/imm456")
from ci import *            # c helpers + B INSHORT TERMS balance save(split.fix)

HT = dict(subject_en="Hematology", subject_ar="أمراض الدم", short_ar="امراض الدم", unit_label="LEC",
          kind="Theory — نظري", stage="The third stage — الثالثة", instructor="د. مازن اللهيبي")
BN = lambda en, ar: N(en, ar, label=["BIOS note", "ملاحظة BIOS"])

blocks = [
 SEC("Hemolytic anemia", "فقر الدم الانحلالي"),
 C("haemolytic anemia can be defined as \"those anaemia which results from **increase in the rate of red cells destruction**\" and this destruction occurs either **intravascular or extra vascular**.",
   "يمكن تعريف فقر الدم الانحلالي بأنه \"فقر الدم الناتج عن **زيادة معدّل تحطّم الكريات الحمر**\"، ويحدث هذا التحطّم إمّا **داخل الأوعية أو خارجها**."),
 C("Red cell destruction usually occurs after a **mean lifespan of 120 days** when the red cells are removed extravascular by the **macrophages of reticulo-endothelial system**, especially in the **marrow** but also in the liver and spleen.",
   "يحدث تحطّم الكريات الحمر عادةً بعد **متوسط عمر 120 يومًا**، حين تُزال خارج الأوعية بواسطة **بلاعم الجهاز الشبكي البطاني**، ولا سيما في **النخاع** وكذلك في الكبد والطحال."),
 T([B("Site of destruction", "مكان التحطّم"), B("Details", "التفاصيل")],
   [[B("**Extra vascular**", "**خارج الأوعية**"), B("occurs in the spleen, liver, bone marrow.", "يحدث في الطحال والكبد ونخاع العظم.")],
    [B("**Intravascular**", "**داخل الأوعية**"), B("Certain types of hemolytic anemia result in intravascular destruction.", "تؤدي بعض أنواع فقر الدم الانحلالي إلى تحطّم داخل الأوعية.")],
    [B("**Both**", "**كلاهما**"), B("Some types of haemolysis lead to both (i.e. intra and extra vascular destruction).", "تؤدي بعض أنواع الانحلال إلى الاثنين (أي تحطّم داخل الأوعية وخارجها).")]],
   key_cols=[0], widths=[28, 72], style="summary", label_en="Where?", label_ar="أين؟"),
 C(["In conditions where the rate of red cell break down is increased, the body initially **compensated by producing marrow red cell**, however if the **breakdown exceed the rate of the body production**, the anemia will be develop and the **bilirubin** which is the breakdown product of hemoglobin can accumulated in the blood causing **jaundice** and be excreted in the urine causing the urine to become a **dark brown** in colour."],
   ["في الحالات التي يزداد فيها معدّل تحطّم الكريات الحمر، **يعوّض الجسم أولًا بإنتاج كريات حمر في النخاع**، لكن إذا **تجاوز التحطّم معدّل إنتاج الجسم** يحدث فقر الدم، ويتراكم **البيليروبين** (ناتج تحلّل الهيموغلوبين) في الدم مسبّبًا **اليرقان**، ويُطرح في الإدرار فيصبح لونه **بنيًا غامقًا**."]),
 FLOW([("↑ Red cell destruction", "↑ تحطّم الكريات"), ("Marrow compensates", "النخاع يعوّض"), ("Breakdown > production", "التحطّم > الإنتاج"), ("Anaemia + ↑ bilirubin", "فقر دم + ↑ البيليروبين"), ("Jaundice, dark brown urine", "يرقان، وإدرار بني غامق")]),
 L(["**Reticulocytosis** (erythroidal hyperplasia).", "**Jaundice.**"], ["**كثرة الخلايا الشبكية** (فرط تنسّج الخط الحمري).", "**اليرقان.**"],
   en="Usually hemolytic anemia associated with:", ar="يرافق فقرَ الدم الانحلالي عادةً:"),
 INSHORT([("Haemolytic = **red cells destroyed faster** than normal (normal life **120 days**).", "الانحلالي = **تحطّم الكريات أسرع** من الطبيعي (العمر الطبيعي **120 يومًا**)."),
          ("Destruction: **extravascular** (spleen, liver, marrow), **intravascular**, or both.", "التحطّم: **خارج الأوعية** (الطحال والكبد والنخاع)، أو **داخلها**، أو الاثنان."),
          ("Two signs: **reticulocytosis + jaundice**.", "علامتان: **كثرة الشبكيات + اليرقان**.")]),

 SEC("Classification", "التصنيف"),
 C("Either: 1. **Hereditary** or 2. **Aquired**.", "إمّا: 1. **وراثي** أو 2. **مكتسب**."),
 H2("1. Hereditary", "1. الوراثي"),
 C("Its usually result of **intrinsic red cell defects** (i.e. **intra corpuscular defect**), the defect either in:",
   "ينتج عادةً عن **عيوب داخلية في الكرية الحمراء** (أي **عيب داخل الكرية**)، ويكون العيب في:"),
 T([B("Defect", "العيب"), B("Examples", "أمثلة")],
   [[B("**A. Membrane defect**", "**أ. عيب الغشاء**"), B("e.g. hereditary spherocytosis and hereditary elliptocytosis.", "مثل كثرة الكريات الكروية الوراثية وكثرة الكريات الإهليلجية الوراثية.")],
    [B("**B. Metabolic defect** i.e. enzymopathy", "**ب. عيب استقلابي** أي اعتلال إنزيمي"), B("like G6PD deficiency, Pyruvate kinas deficiency.", "مثل نقص G6PD، ونقص البيروفيت كاينيز.")],
    [B("**C. Hemoglobin defect**", "**ج. عيب الهيموغلوبين**"), B("e.g. Hb. S, Hb. C, unstable Hb.", "مثل Hb S، وHb C، والهيموغلوبين غير المستقر.")]],
   key_cols=[0], widths=[36, 64], style="summary", label_en="Intra-corpuscular", label_ar="داخل الكرية"),
 H2("2. Acquired", "2. المكتسب"),
 C("Its usually occur due to **extra corpuscular defect except PNH**, it include:", "يحدث عادةً بسبب **عيب خارج الكرية ما عدا PNH**، ويشمل:"),
 T([B("Acquired cause", "السبب المكتسب"), B("Acquired cause", "السبب المكتسب")],
   [[B("**A. Immune** either autoimmune or alloimmune.", "**أ. مناعي** إمّا ذاتي أو خيفي."), B("**E. Infection** e.g. malaria.", "**هـ. العدوى** مثل الملاريا.")],
    [B("**B. Drugs.**", "**ب. الأدوية.**"), B("**F. Chemicals and physicals agents.**", "**و. العوامل الكيميائية والفيزيائية.**")],
    [B("**C. Red cells fragmentation syndrome.**", "**ج. متلازمة تشظّي الكريات الحمر.**"), B("**G. Secondary** e.g. renal diseases and liver diseases.", "**ز. ثانوي** مثل أمراض الكلية والكبد.")],
    [B("**D. March haemoglobinuria.**", "**د. بيلة الهيموغلوبين المسيرية.**"), B("**H. Paroxysmal nocturnal haemoglobinuria (PNH)**", "**ح. بيلة الهيموغلوبين الليلية الانتيابية (PNH)**")]],
   widths=[50, 50], style="summary", label_en="Extra-corpuscular (except PNH)", label_ar="خارج الكرية (ما عدا PNH)"),
 BN("PNH is acquired but the defect is **inside** the red cell (intra-corpuscular) — that is why it is the exception.",
    "PNH مكتسب لكن عيبه **داخل** الكرية الحمراء، ولهذا هو الاستثناء."),
 INSHORT([("**Hereditary = inside the cell**: membrane, enzyme (metabolism), haemoglobin.", "**الوراثي = داخل الكرية**: الغشاء، والإنزيم (الاستقلاب)، والهيموغلوبين."),
          ("**Acquired = outside the cell**, except **PNH**.", "**المكتسب = خارج الكرية**، ما عدا **PNH**."),
          ("Acquired A–H: **immune, drugs, fragmentation, march, infection, chemical/physical, secondary, PNH**.", "المكتسب أ–ح: **المناعي، والأدوية، والتشظّي، والمسيري، والعدوى، والكيميائي/الفيزيائي، والثانوي، وPNH**.")]),

 SEC("Classification of hemolytic anemia's", "جدول تصنيف فقر الدم الانحلالي"),
 T([B("Hereditary", "الوراثي"), B("Acquired", "المكتسب")],
   [[B("**1. Membrane** e.g. Hereditary spherocytosis, Hereditary elliptocytosis.", "**1. الغشاء** مثل كثرة الكريات الكروية الوراثية، وكثرة الكريات الإهليلجية الوراثية."),
     B("**1. Immune:** Autoimmune (Warm type, Cold type); Alloimmune (Haemolytic transfusion reaction, Haemolytic diseases of newborn, Allograft especially marrow transplantation); Drug associated.",
       "**1. مناعي:** ذاتي (النوع الدافئ، النوع البارد)؛ خيفي (تفاعل نقل الدم الانحلالي، وداء انحلال الوليد، والطُّعم الخيفي ولا سيما زرع النخاع)؛ ومرتبط بالأدوية.")],
    [B("**2. Metabolism** e.g. G6PD deficiency, pyruvate kinase deficiency.", "**2. الاستقلاب** مثل نقص G6PD، ونقص البيروفيت كاينيز."),
     B("**2. Red cells fragmentation syndromes:** Arterial grafts cardiac valves; Microangipathic haemolytic anaemias (Thrombotic thrombocytopenic purpura, Haemolytic uremic syndrome, Meningococcal sepsis, Pre-eclampsia, Disseminated intravascular coagulation).",
       "**2. متلازمات تشظّي الكريات:** الطعوم الشريانية وصمامات القلب؛ وفقر الدم الانحلالي باعتلال الأوعية الدقيقة (فرفرية قلّة الصفيحات الخثارية، ومتلازمة انحلال الدم اليوريمية، وإنتان المكوّرات السحائية، وما قبل الارتعاج، والتخثّر المنتثر داخل الأوعية).")],
    [B("**3. Haemoglobin** e.g. Abnormal Haemoglobin (Hb.S, Hb.C)", "**3. الهيموغلوبين** مثل الهيموغلوبين الشاذ (Hb S، Hb C)"),
     B("**3. March haemoglobinuria. 4. Infections:** e.g. Malaria. **5. Chemical and physical agents:** Especially drugs, burn. **6. Secondary:** e.g. Liver and renal disease. **7. Paroxysmal nocturnal haemoglobinuria.**",
       "**3. بيلة الهيموغلوبين المسيرية. 4. العدوى:** مثل الملاريا. **5. العوامل الكيميائية والفيزيائية:** ولا سيما الأدوية والحروق. **6. الثانوي:** مثل أمراض الكبد والكلية. **7. بيلة الهيموغلوبين الليلية الانتيابية.**")]],
   widths=[38, 62], style="summary", label_en="Lecture table", label_ar="جدول المحاضرة"),
 H2("Immune haemolysis at a glance", "الانحلال المناعي بنظرة"),
 FLOW([("Immune", "مناعي"), ("Autoimmune: warm / cold", "ذاتي: دافئ / بارد"), ("Alloimmune: transfusion, newborn, allograft", "خيفي: نقل الدم، الوليد، الطُّعم"), ("Drug associated", "مرتبط بالأدوية")]),
 BN("\"Microangipathic\" in the lecture is **microangiopathic**; march haemoglobinuria follows long marching or running.",
    "كلمة \"Microangipathic\" في المحاضرة هي **microangiopathic**؛ وبيلة الهيموغلوبين المسيرية تحدث بعد المشي أو الركض الطويل."),
 INSHORT([("Left column (hereditary): **membrane, metabolism, haemoglobin** — 3 groups.", "العمود الأيسر (الوراثي): **الغشاء، والاستقلاب، والهيموغلوبين** — 3 مجموعات."),
          ("Right column (acquired): **7 groups**, immune and fragmentation have the most examples.", "العمود الأيمن (المكتسب): **7 مجموعات**، وأكثرها أمثلة المناعي والتشظّي."),
          ("Microangiopathic: **TTP, HUS, meningococcal sepsis, pre-eclampsia, DIC**.", "اعتلال الأوعية الدقيقة: **TTP، وHUS، وإنتان المكوّرات السحائية، وما قبل الارتعاج، وDIC**.")]),

 SEC("Clinical features of hemolytic anemia's", "المظاهر السريرية لفقر الدم الانحلالي"),
 C("The clinical evidences of hemolytic anemia are:", "الأدلّة السريرية على فقر الدم الانحلالي هي:"),
 R("**Anaemia.**", "**فقر الدم.**"),
 R("**Jaundice.**", "**اليرقان.**"),
 R("**Crises** (a plastic or hemolytic crisis).", "**النوبات** (نوبة لاتنسّجية أو نوبة انحلالية)."),
 R("**Splenomegaly.**", "**تضخّم الطحال.**"),
 R("**Gall stones.**", "**حصى المرارة.**"),
 R("**Leg ulceration.**", "**تقرّح الساق.**"),
 BN("\"a plastic crisis\" in the lecture means **aplastic crisis**.", "عبارة \"a plastic crisis\" في المحاضرة تعني **النوبة اللاتنسّجية (aplastic crisis)**."),
 INSHORT([("6 features: **anaemia, jaundice, crises, splenomegaly, gall stones, leg ulcers**.", "6 مظاهر: **فقر الدم، واليرقان، والنوبات، وتضخّم الطحال، وحصى المرارة، وتقرّح الساق**."),
          ("Gall stones come from the **extra bilirubin**.", "حصى المرارة تأتي من **البيليروبين الزائد**.")]),

 SEC("Laboratory finding of hemolytic anemia's", "النتائج المختبرية لفقر الدم الانحلالي"),
 L(["**Anemia is usual.**", "**Normal blood indices.**", "**Reticulocytosis** .", "**Increased unconjugated bilirubin.**",
    "**Increased urine urobilinogen** and **fecal stercobilinogen**.", "**Decreased serum Haptoglobin.**", "**Increased serum LDH.**",
    "Blood film will show **microspherocytes** , **fragmented red cells** , **nucleated red cells**.", "Bone marrow will show **Erythroid hyperplasia**."],
   ["**فقر الدم معتاد.**", "**مؤشّرات الدم طبيعية.**", "**كثرة الخلايا الشبكية**.", "**ارتفاع البيليروبين غير المقترن.**",
    "**ارتفاع اليوروبيلينوجين في الإدرار** و**الستيركوبيلينوجين في البراز**.", "**انخفاض الهابتوغلوبين في المصل.**", "**ارتفاع LDH في المصل.**",
    "تُظهر المسحة **كريات كروية صغيرة**، و**كريات حمر متشظّية**، و**كريات حمر منوّاة**.", "يُظهر نخاع العظم **فرط تنسّج حمري**."]),
 T([B("Test", "الفحص"), B("In haemolysis", "في الانحلال")],
   [[B("**Blood indices**", "**مؤشّرات الدم**"), B("Normal", "طبيعية")], [B("**Reticulocytes**", "**الخلايا الشبكية**"), "↑"],
    [B("**Unconjugated bilirubin**", "**البيليروبين غير المقترن**"), "↑"], [B("**Urine urobilinogen / fecal stercobilinogen**", "**يوروبيلينوجين الإدرار / ستيركوبيلينوجين البراز**"), "↑"],
    [B("**Serum haptoglobin**", "**هابتوغلوبين المصل**"), "**↓**"], [B("**Serum LDH**", "**LDH المصل**"), "↑"],
    [B("**Bone marrow**", "**نخاع العظم**"), B("Erythroid hyperplasia", "فرط تنسّج حمري")]],
   key_cols=[0], widths=[60, 40], style="summary", label_en="At a glance", label_ar="بنظرة"),
 H2("Special tests", "الفحوص الخاصة"),
 R("**Commbs test (Antihuman globulin test)** is usually **positive in immune mediated** hemolytic anemia.", "**اختبار كومبس (اختبار الغلوبولين المضاد للإنسان)** يكون عادةً **موجبًا في فقر الدم الانحلالي المناعي**."),
 R("**Osmotic fragility test:** show **increased osmotic fragility**.", "**اختبار الهشاشة التناضحية:** يُظهر **زيادة الهشاشة التناضحية**."),
 R("**Auto-haemolysis test:** show increase auto-haemolysis which is **corrected by glucose**.", "**اختبار الانحلال الذاتي:** يُظهر زيادة الانحلال الذاتي التي **تُصحَّح بالغلوكوز**."),
 R("**Chromium-51 studies** used to document the dominates **splenic destruction**.", "تُستعمل **دراسات الكروم-51** لتوثيق **التحطّم الطحالي** السائد."),
 BN("\"Commbs\" is the **Coombs** test; \"dominates splenic destruction\" means the **predominant (main) splenic destruction**.",
    "كلمة \"Commbs\" هي اختبار **Coombs**؛ وعبارة \"dominates splenic destruction\" تعني **التحطّم الطحالي السائد (الرئيسي)**."),
 INSHORT([("Everything **↑** (retics, bilirubin, urobilinogen, LDH) except **haptoglobin ↓**; indices **normal**.", "كل شيء **↑** (الشبكيات، والبيليروبين، واليوروبيلينوجين، وLDH) ما عدا **الهابتوغلوبين ↓**؛ والمؤشّرات **طبيعية**."),
          ("Film: **microspherocytes, fragments, nucleated red cells**.", "المسحة: **كريات كروية صغيرة، وشظايا، وكريات منوّاة**."),
          ("Coombs = **immune**; osmotic fragility ↑; autohaemolysis corrected by **glucose**; **Cr-51** = spleen.", "كومبس = **مناعي**؛ والهشاشة التناضحية ↑؛ والانحلال الذاتي يُصحَّح **بالغلوكوز**؛ و**Cr-51** = الطحال.")]),
] + TERMS([
 ("Haemolytic anaemia", "فقر الدم الانحلالي / فقر الدم التحلّلي"),
 ("Intravascular / Extravascular", "داخل الأوعية / خارج الأوعية"),
 ("Intra-corpuscular / Extra-corpuscular", "داخل الكرية / خارج الكرية"),
 ("Hereditary spherocytosis", "كثرة الكريات الكروية الوراثية / داء الكريات الكروية"),
 ("Hereditary elliptocytosis", "كثرة الكريات الإهليلجية الوراثية / داء الكريات البيضوية"),
 ("Enzymopathy", "اعتلال إنزيمي / عيب إنزيمي"),
 ("G6PD deficiency", "نقص إنزيم G6PD / داء الفوال"),
 ("Pyruvate kinase deficiency", "نقص البيروفيت كاينيز"),
 ("Autoimmune / Alloimmune", "مناعي ذاتي / مناعي خيفي"),
 ("Microangiopathic haemolytic anaemia", "فقر الدم الانحلالي باعتلال الأوعية الدقيقة"),
 ("March haemoglobinuria", "بيلة الهيموغلوبين المسيرية / بيلة هيموغلوبين الجهد"),
 ("PNH", "بيلة الهيموغلوبين الليلية الانتيابية"),
 ("Aplastic crisis", "نوبة لاتنسّجية / نوبة توقّف النخاع"),
 ("Haptoglobin", "الهابتوغلوبين / بروتين رابط الهيموغلوبين"),
 ("Urobilinogen / Stercobilinogen", "اليوروبيلينوجين / الستيركوبيلينوجين"),
 ("Coombs test", "اختبار كومبس / اختبار الغلوبولين المضاد للإنسان"),
 ("Osmotic fragility test", "اختبار الهشاشة التناضحية / اختبار الهشاشة الأسموزية"),
 ("Autohaemolysis test", "اختبار الانحلال الذاتي"),
])

O = P
mcq = [
 {"topic_en": "Definition and mechanism", "topic_ar": "التعريف والآلية"},
 Q("Haemolytic anaemia results from:", "ينتج فقر الدم الانحلالي عن:", O(("Decreased red cell production", "نقص إنتاج الكريات الحمر"), ("Increased rate of red cell destruction", "زيادة معدّل تحطّم الكريات الحمر"), ("Iron deficiency", "نقص الحديد"), ("B12 deficiency", "نقص B12")), "b"),
 Q("The mean normal red cell lifespan is:", "متوسط عمر الكرية الحمراء الطبيعي:", O(("30 days", "30 يومًا"), ("60 days", "60 يومًا"), ("120 days", "120 يومًا"), ("365 days", "365 يومًا")), "c"),
 Q("Normal red cells are removed mainly by:", "تُزال الكريات الحمر الطبيعية أساسًا بواسطة:", O(("Macrophages of the reticulo-endothelial system", "بلاعم الجهاز الشبكي البطاني"), ("Neutrophils", "العدلات"), ("Kidneys", "الكليتين"), ("Platelets", "الصفيحات")), "a"),
 Q("Extravascular destruction occurs in the:", "يحدث التحطّم خارج الأوعية في:", O(("Lungs and heart", "الرئتين والقلب"), ("Kidney only", "الكلية فقط"), ("Blood vessels", "الأوعية الدموية"), ("Spleen, liver, bone marrow", "الطحال والكبد ونخاع العظم")), "d"),
 Q("Dark brown urine in haemolysis is due to:", "الإدرار البني الغامق في الانحلال سببه:", O(("Blood loss", "فقدان الدم"), ("Excreted bilirubin breakdown products", "نواتج البيليروبين المطروحة"), ("Glucose", "الغلوكوز"), ("Protein", "البروتين")), "b"),
 Q("Haemolytic anaemia is usually associated with:", "يرافق فقرَ الدم الانحلالي عادةً:", O(("Reticulopenia", "قلّة الشبكيات"), ("Thrombocytosis only", "كثرة الصفيحات فقط"), ("Reticulocytosis and jaundice", "كثرة الشبكيات واليرقان"), ("Leucopenia", "قلّة الكريات البيض")), "c"),
 {"topic_en": "Classification", "topic_ar": "التصنيف"},
 Q("Hereditary haemolytic anaemias are usually due to:", "يعود فقر الدم الانحلالي الوراثي عادةً إلى:", O(("Intra-corpuscular defects", "عيوب داخل الكرية"), ("Extra-corpuscular defects", "عيوب خارج الكرية"), ("Infections", "العدوى"), ("Drugs", "الأدوية")), "a"),
 Q("Hereditary spherocytosis is a defect of the:", "كثرة الكريات الكروية الوراثية عيب في:", O(("Enzyme", "الإنزيم"), ("Haemoglobin", "الهيموغلوبين"), ("Plasma", "البلازما"), ("Membrane", "الغشاء")), "d"),
 Q("G6PD deficiency is an example of:", "نقص G6PD مثال على:", O(("Membrane defect", "عيب الغشاء"), ("Metabolic defect (enzymopathy)", "عيب استقلابي (اعتلال إنزيمي)"), ("Immune haemolysis", "انحلال مناعي"), ("Fragmentation syndrome", "متلازمة التشظّي")), "b"),
 Q("Hb S and Hb C are examples of:", "Hb S وHb C مثالان على:", O(("Membrane defects", "عيوب الغشاء"), ("Enzymopathies", "اعتلالات إنزيمية"), ("Haemoglobin defects", "عيوب الهيموغلوبين"), ("Acquired causes", "أسباب مكتسبة")), "c"),
 Q("The acquired haemolytic anaemia with an intra-corpuscular defect is:", "فقر الدم الانحلالي المكتسب ذو العيب داخل الكرية هو:", O(("Malaria", "الملاريا"), ("March haemoglobinuria", "بيلة الهيموغلوبين المسيرية"), ("Autoimmune haemolysis", "الانحلال المناعي الذاتي"), ("PNH", "PNH")), "d"),
 Q("Haemolytic disease of the newborn is classified as:", "يُصنَّف داء انحلال الوليد بأنه:", O(("Alloimmune", "مناعي خيفي"), ("Autoimmune warm type", "مناعي ذاتي دافئ"), ("Membrane defect", "عيب غشاء"), ("Infection", "عدوى")), "a"),
 Q("Which is a microangiopathic haemolytic anaemia?", "أي مما يأتي فقر دم انحلالي باعتلال الأوعية الدقيقة؟", O(("G6PD deficiency", "نقص G6PD"), ("Haemolytic uremic syndrome", "متلازمة انحلال الدم اليوريمية"), ("Hereditary elliptocytosis", "كثرة الكريات الإهليلجية"), ("Hb C", "Hb C")), "b"),
 Q("Arterial grafts and cardiac valves cause haemolysis by:", "تسبّب الطعوم الشريانية وصمامات القلب الانحلال عن طريق:", O(("Antibodies", "الأضداد"), ("Enzyme deficiency", "نقص الإنزيم"), ("Red cell fragmentation", "تشظّي الكريات الحمر"), ("Infection", "العدوى")), "c"),
 Q("An infectious cause of haemolytic anaemia is:", "سبب معدٍ لفقر الدم الانحلالي:", O(("Tuberculosis", "التدرّن"), ("Hepatitis A only", "التهاب الكبد A فقط"), ("Influenza", "الإنفلونزا"), ("Malaria", "الملاريا")), "d"),
 Q("Autoimmune haemolytic anaemia is divided into:", "يُقسَّم فقر الدم الانحلالي المناعي الذاتي إلى:", O(("Warm and cold types", "النوع الدافئ والبارد"), ("Acute and chronic", "حاد ومزمن"), ("Primary and tertiary", "أولي وثالثي"), ("Membrane and enzyme", "غشائي وإنزيمي")), "a"),
 {"topic_en": "Clinical and laboratory", "topic_ar": "السريري والمختبري"},
 Q("Which is a clinical feature of haemolytic anaemia?", "أي مما يأتي من المظاهر السريرية لفقر الدم الانحلالي؟", O(("Koilonychia", "تقعّر الأظافر"), ("Gall stones", "حصى المرارة"), ("Pica", "القَطَا"), ("Glossitis only", "التهاب اللسان فقط")), "b"),
 Q("In haemolytic anaemia, blood indices are usually:", "في فقر الدم الانحلالي تكون مؤشّرات الدم عادةً:", O(("Microcytic", "صغيرة الكريات"), ("Macrocytic", "كبيرة الكريات"), ("Normal", "طبيعية"), ("Hypochromic", "ناقصة الصباغ")), "c"),
 Q("Serum haptoglobin in haemolysis is:", "الهابتوغلوبين في المصل عند الانحلال:", O(("Increased", "مرتفع"), ("Normal", "طبيعي"), ("Very high", "مرتفع جدًا"), ("Decreased", "منخفض")), "d"),
 Q("The bilirubin raised in haemolysis is:", "البيليروبين المرتفع في الانحلال:", O(("Unconjugated", "غير المقترن"), ("Conjugated only", "المقترن فقط"), ("Neither", "لا هذا ولا ذاك"), ("Urinary only", "البولي فقط")), "a"),
 Q("The Coombs (antihuman globulin) test is usually positive in:", "يكون اختبار كومبس عادةً موجبًا في:", O(("G6PD deficiency", "نقص G6PD"), ("Immune mediated haemolytic anaemia", "فقر الدم الانحلالي المناعي"), ("Thalassaemia", "الثلاسيميا"), ("Iron deficiency", "نقص الحديد")), "b"),
 Q("The osmotic fragility test in haemolysis (as in the lecture) shows:", "يُظهر اختبار الهشاشة التناضحية في الانحلال (كما في المحاضرة):", O(("Decreased fragility", "نقص الهشاشة"), ("No change", "لا تغيّر"), ("Increased osmotic fragility", "زيادة الهشاشة التناضحية"), ("Absent haemolysis", "غياب الانحلال")), "c"),
 Q("Increased autohaemolysis is corrected by:", "تُصحَّح زيادة الانحلال الذاتي بـ:", O(("Iron", "الحديد"), ("Vitamin B12", "فيتامين B12"), ("Folate", "الفولات"), ("Glucose", "الغلوكوز")), "d"),
 Q("Chromium-51 studies are used to document:", "تُستعمل دراسات الكروم-51 لتوثيق:", O(("Splenic destruction", "التحطّم الطحالي"), ("Iron absorption", "امتصاص الحديد"), ("B12 absorption", "امتصاص B12"), ("Platelet function", "وظيفة الصفيحات")), "a"),
]
mcq = balance(mcq, 9)
tf = [
 TF("Red cell destruction may be intravascular, extravascular or both.", "قد يكون تحطّم الكريات داخل الأوعية أو خارجها أو كليهما.", "T"),
 TF("The body first compensates for haemolysis by increasing marrow red cell production.", "يعوّض الجسم الانحلال أولًا بزيادة إنتاج النخاع للكريات الحمر.", "T"),
 TF("Anaemia develops as soon as red cell breakdown increases.", "يحدث فقر الدم بمجرد زيادة تحطّم الكريات.", "F"),
 TF("Hereditary haemolytic anaemias are usually extra-corpuscular.", "فقر الدم الانحلالي الوراثي عادةً خارج الكرية.", "F"),
 TF("Pyruvate kinase deficiency is a metabolic defect.", "نقص البيروفيت كاينيز عيب استقلابي.", "T"),
 TF("Haemolytic transfusion reaction is an alloimmune haemolysis.", "تفاعل نقل الدم الانحلالي انحلال مناعي خيفي.", "T"),
 TF("DIC is a cause of microangiopathic haemolytic anaemia.", "التخثّر المنتثر داخل الأوعية سبب لفقر الدم الانحلالي باعتلال الأوعية الدقيقة.", "T"),
 TF("Splenomegaly is not a feature of haemolytic anaemia.", "تضخّم الطحال ليس من مظاهر فقر الدم الانحلالي.", "F"),
 TF("Serum LDH is decreased in haemolysis.", "ينخفض LDH في المصل عند الانحلال.", "F"),
 TF("Urine urobilinogen and fecal stercobilinogen are increased in haemolysis.", "يرتفع يوروبيلينوجين الإدرار وستيركوبيلينوجين البراز في الانحلال.", "T"),
 TF("Nucleated red cells may appear in the blood film.", "قد تظهر كريات حمر منوّاة في المسحة.", "T"),
 TF("The bone marrow in haemolysis shows erythroid hypoplasia.", "يُظهر النخاع في الانحلال نقص تنسّج حمري.", "F"),
]
traps = [
 TR("Hereditary vs acquired — the PNH exception", "الوراثي مقابل المكتسب — استثناء PNH", "Hereditary = intra-corpuscular; acquired = extra-corpuscular, EXCEPT PNH (acquired but intra-corpuscular).", "الوراثي = داخل الكرية؛ والمكتسب = خارج الكرية، ما عدا PNH (مكتسب لكن داخل الكرية)."),
 TR("Haptoglobin goes DOWN", "الهابتوغلوبين ينزل", "In haemolysis almost everything rises (retics, bilirubin, urobilinogen, LDH) but haptoglobin falls.", "في الانحلال يرتفع كل شيء تقريبًا (الشبكيات، والبيليروبين، واليوروبيلينوجين، وLDH) لكن الهابتوغلوبين ينخفض."),
 TR("Indices in haemolysis", "المؤشّرات في الانحلال", "Blood indices are NORMAL (normocytic normochromic), unlike IDA (microcytic) or megaloblastic (macrocytic).", "مؤشّرات الدم طبيعية، على خلاف نقص الحديد (صغيرة) والأرومي الضخم (كبيرة)."),
 TR("Autoimmune vs alloimmune", "الذاتي مقابل الخيفي", "Autoimmune: own antibodies (warm, cold). Alloimmune: antibodies to another's cells (transfusion reaction, HDN, allograft).", "الذاتي: أضداد الشخص نفسه (دافئ، بارد). الخيفي: أضداد لخلايا شخص آخر (تفاعل النقل، داء انحلال الوليد، الطُّعم)."),
 TR("Which test for what?", "أي فحص لأي شيء؟", "Coombs → immune; osmotic fragility → increased; autohaemolysis → corrected by glucose; Cr-51 → splenic destruction.", "كومبس ← المناعي؛ الهشاشة التناضحية ← زيادة؛ الانحلال الذاتي ← يُصحَّح بالغلوكوز؛ Cr-51 ← التحطّم الطحالي."),
]
important = [
 IM("Define haemolytic anaemia and explain how jaundice and dark urine develop.", "عرّف فقر الدم الانحلالي ووضّح كيف يحدث اليرقان والإدرار الغامق.", "Anaemia from increased rate of red cell destruction (intra- or extravascular). The marrow compensates first; when breakdown exceeds production, anaemia develops and bilirubin from haemoglobin breakdown accumulates (jaundice) and is excreted in urine (dark brown).", "فقر دم ناتج عن زيادة معدّل تحطّم الكريات (داخل الأوعية أو خارجها). يعوّض النخاع أولًا، وحين يتجاوز التحطّم الإنتاج يحدث فقر الدم ويتراكم البيليروبين (يرقان) ويُطرح في الإدرار (بني غامق)."),
 IM("Classify hereditary haemolytic anaemias with examples.", "صنّف فقر الدم الانحلالي الوراثي مع أمثلة.", "Intra-corpuscular: membrane (hereditary spherocytosis, elliptocytosis); metabolic/enzymopathy (G6PD, pyruvate kinase deficiency); haemoglobin (Hb S, Hb C, unstable Hb).", "داخل الكرية: الغشاء (الكريات الكروية والإهليلجية الوراثية)؛ الاستقلاب/الإنزيم (نقص G6PD والبيروفيت كاينيز)؛ الهيموغلوبين (Hb S، Hb C، غير المستقر)."),
 IM("List the acquired causes of haemolytic anaemia.", "عدّد الأسباب المكتسبة لفقر الدم الانحلالي.", "Immune (autoimmune warm/cold; alloimmune: transfusion reaction, HDN, allograft; drug), red cell fragmentation (cardiac valves, arterial grafts, microangiopathic: TTP, HUS, meningococcal sepsis, pre-eclampsia, DIC), march haemoglobinuria, infection (malaria), chemical/physical (drugs, burns), secondary (liver, renal), PNH.", "مناعي (ذاتي دافئ/بارد؛ خيفي: تفاعل النقل، داء الوليد، الطُّعم؛ دوائي)، تشظّي الكريات (الصمامات، الطعوم، اعتلال الأوعية الدقيقة: TTP، HUS، إنتان المكوّرات، ما قبل الارتعاج، DIC)، البيلة المسيرية، العدوى (الملاريا)، الكيميائي/الفيزيائي (الأدوية، الحروق)، الثانوي (الكبد، الكلية)، PNH."),
 IM("Give the clinical features of haemolytic anaemia.", "اذكر المظاهر السريرية لفقر الدم الانحلالي.", "Anaemia, jaundice, crises (aplastic or haemolytic), splenomegaly, gall stones, leg ulceration.", "فقر الدم، واليرقان، والنوبات (لاتنسّجية أو انحلالية)، وتضخّم الطحال، وحصى المرارة، وتقرّح الساق."),
 IM("Give the laboratory findings of haemolytic anaemia.", "اذكر النتائج المختبرية لفقر الدم الانحلالي.", "Anaemia with normal indices; reticulocytosis; ↑ unconjugated bilirubin; ↑ urine urobilinogen and fecal stercobilinogen; ↓ haptoglobin; ↑ LDH; film: microspherocytes, fragments, nucleated red cells; marrow erythroid hyperplasia.", "فقر دم بمؤشّرات طبيعية؛ كثرة الشبكيات؛ ارتفاع البيليروبين غير المقترن؛ ارتفاع يوروبيلينوجين الإدرار وستيركوبيلينوجين البراز؛ انخفاض الهابتوغلوبين؛ ارتفاع LDH؛ المسحة: كريات كروية صغيرة وشظايا وكريات منوّاة؛ فرط تنسّج حمري."),
 IM("List the special tests used in haemolytic anaemia and what each shows.", "عدّد الفحوص الخاصة في فقر الدم الانحلالي وما يُظهره كل منها.", "Coombs test: positive in immune haemolysis; osmotic fragility: increased; autohaemolysis: increased, corrected by glucose; chromium-51 studies: document splenic destruction.", "اختبار كومبس: موجب في الانحلال المناعي؛ الهشاشة التناضحية: مرتفعة؛ الانحلال الذاتي: مرتفع ويُصحَّح بالغلوكوز؛ دراسات الكروم-51: توثّق التحطّم الطحالي."),
]
meta = dict(HT, unit_en="Lecture 9", unit_ar="المحاضرة 9", unit_no="9", title_en="Hemolytic anemia", title_ar="فقر الدم الانحلالي")
save("hematology-lec9-hemolytic", meta, blocks, mcq, tf, traps, important)

```
