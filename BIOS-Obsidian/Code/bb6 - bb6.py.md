---
source: BIOS-Obsidian/tools/scripts/bb6/bb6.py
handouts: []
saved: 2026-11-06
tags: [bios, code]
---
# bb6/bb6.py

Utility script.

```python
import sys, re; sys.path.insert(0, "/tmp/claude-0/-home-claude/4a281dcf-357b-50ce-b2f4-8802cfcc6472/scratchpad/imm456")
from ci import *            # c helpers + B INSHORT TERMS balance save(split.fix)
import split
split.ABBR = split.ABBR + ("e.g",)

# Blood Transfusion — lecture 6 (stage 4) — د. مازن اللهيبي — ABO Typing Discrepancies + Practical 6 (antibody screening)

BN = lambda en, ar: N(en, ar, label=["BIOS note", "ملاحظة BIOS"])
O = P
def TERMS6(terms, n=6):
    head = [B("Term", "المصطلح"), "الترجمات العربية المستعملة"]
    return [SEC("Key terms", "أهم المصطلحات")] + [T(head, [[f"**{e}**", a] for e, a in terms[i:i + n]], ar_cols=[1], widths=[36, 64])
                                                  for i in range(0, len(terms), n)]

blocks = [
 # ───────────────────────── 1. ABO discrepancies
 SEC("ABO Typing Discrepancies", "اختلافات تحديد فصيلة ABO"),
 L(["ABO discrepancies refer to situations where there is a mismatch between the forward( cell) and reverse (serum) grouping results during ABO blood typing",
    "ABO discrepancies occurs when forward and reverse grouping do not agree or results are unexpected or are weaker."],
   ["**اختلافات ABO** هي الحالات التي يحدث فيها **عدم تطابق بين نتائج التصنيف المباشر (الكريات) والعكسي (المصل)** أثناء تحديد فصيلة ABO",
    "تحدث اختلافات ABO عندما **لا يتّفق التصنيف المباشر والعكسي** أو تكون النتائج **غير متوقّعة** أو **أضعف**."]),
 L(["problems with the patient’s RBCs (forward grouping), or", "problems with the patient’s serum (reverse grouping),", "problems with both the serum and red blood cells."],
   ["مشاكل في **كريات المريض الحمر** (التصنيف المباشر)، أو", "مشاكل في **مصل المريض** (التصنيف العكسي)،", "مشاكل في **المصل والكريات كليهما**."],
   en="These can be due to either :", ar="وقد تكون بسبب:"),
 L(["The unexpected reaction(s) may be due to an extra positive reaction or a weak or missing reaction in the forward and reverse grouping.",
    "All ABO discrepancies must be resolved prior to reporting a patient or donor ABO group."],
   ["قد يكون التفاعل غير المتوقّع بسبب **تفاعل موجب إضافي** أو **تفاعل ضعيف أو مفقود** في التصنيف المباشر والعكسي.",
    "**يجب حلّ كل اختلافات ABO قبل إصدار فصيلة ABO** للمريض أو المتبرّع."]),
 INSHORT([("Discrepancy = **forward (cells) ≠ reverse (serum)**, or results unexpected / weaker.", "الاختلاف = **المباشر (الكريات) ≠ العكسي (المصل)**، أو نتائج غير متوقّعة / أضعف."),
          ("Source: patient’s **RBCs**, **serum**, or **both**; extra positive or weak / missing reaction.", "المصدر: **كريات** المريض أو **مصله** أو **كلاهما**؛ تفاعل موجب إضافي أو ضعيف / مفقود."),
          ("**Resolve every discrepancy before reporting** the ABO group.", "**احلّ كل اختلاف قبل إصدار** الفصيلة.")]),

 # ───────────────────────── 2. Technical errors
 SEC("Technical Errors", "الأخطاء الفنية"),
 C("**Technical Errors** are actually one of the most common causes of apparent ABO discrepancies in the blood bank, Before assuming a patient has an unusual results :",
   "**الأخطاء الفنية** في الحقيقة من **أشيع أسباب** اختلافات ABO الظاهرية في بنك الدم، قبل افتراض أن لدى المريض نتائج غير اعتيادية:"),
 L(["**sample collections errors :** Examples wrong patient sample, incorrect anticoagulant , hemolysis or contaminated specimen .",
    "**Clerical or labeling Errors :** Example include mislabeling of tubes or slides, transcription error ."],
   ["**أخطاء جمع العيّنة:** مثل عيّنة مريض خاطئ، أو مانع تخثّر غير صحيح، أو **انحلال الدم** أو عيّنة ملوّثة.",
    "**الأخطاء الكتابية أو أخطاء التعليم:** مثل التعليم الخاطئ للأنابيب أو الشرائح، و**خطأ النقل (التدوين)**."],
   en="Technical errors includes:", ar="تشمل الأخطاء الفنية:"),
 N(["Results must be recorded immediately after obtaining them to avoid transcription errors",
    "Always examine reagent vials concurrently while performing ABO testing and quality control testing for possible contamination."],
   ["يجب **تسجيل النتائج فور الحصول عليها** لتجنّب أخطاء النقل",
    "افحص دائمًا **قناني الكواشف** في الوقت نفسه أثناء فحص ABO وفحص ضبط الجودة لاحتمال **التلوّث**."],
   label=("Note:", "ملاحظة:")),
 N(["A mix-up in samples may be a source of error.", "Over-centrifugation or under-centrifugation"],
   ["قد يكون **اختلاط العيّنات** مصدرًا للخطأ.", "**زيادة النبذ أو نقصه**"],
   label=("Note:", "ملاحظة:")),
 INSHORT([("Technical errors = **most common** cause of apparent discrepancies: **sample collection** and **clerical / labeling** errors.", "الأخطاء الفنية = **أشيع** سبب للاختلافات الظاهرية: أخطاء **جمع العيّنة** و**الكتابة / التعليم**."),
          ("Record at once, check reagent vials, avoid sample mix-up and **over- / under-centrifugation**.", "سجّل فورًا، افحص قناني الكواشف، تجنّب خلط العيّنات و**زيادة / نقص النبذ**.")]),

 # ───────────────────────── 3. Group I
 SEC("Group I Discrepancies", "اختلافات المجموعة الأولى"),
 C("ABO discrepancies divided into four major categories: group I, group II, group III, and group IV discrepancies.",
   "تُقسم اختلافات ABO إلى **أربع فئات رئيسية**: اختلافات المجموعة الأولى والثانية والثالثة والرابعة."),
 C("**Group I Discrepancies –Weak or missing antibodies (Reverse grouping problem)** are associated with unexpected reactions in the reverse grouping due to weakly reacting or missing antibodies.",
   "**اختلافات المجموعة الأولى – أضداد ضعيفة أو مفقودة (مشكلة في التصنيف العكسي)** ترتبط بتفاعلات غير متوقّعة في التصنيف العكسي بسبب **أضداد ضعيفة التفاعل أو مفقودة**."),
 C(["When a reaction in the serum grouping is weak or missing, a group I discrepancy should be suspected because, normally, RBC and serum grouping reactions are very strong (4+)."],
   ["عندما يكون التفاعل في تصنيف المصل **ضعيفًا أو مفقودًا** يجب الشك باختلاف من المجموعة الأولى، لأن تفاعلات تصنيف الكريات والمصل تكون طبيعيًا **قوية جدًا (4+)**."]),
 L(['Newborns (ABO antibody production is not detectable until 3 to 6 months of age).'], ['**حديثو الولادة** (إنتاج أضداد ABO لا يُكشف حتى عمر **3 إلى 6 أشهر**).'], en='**Causes :** Weak or Missing ABO antibodies in the serum. Examples in:', ar='**الأسباب:** أضداد ABO ضعيفة أو مفقودة في المصل. أمثلة في:'),
 L(['Elderly patients', 'Immunodeficiency or hypogammaglobinemia.', 'Bone marrow transplant or Leukemia', 'Patients whose existing ABO antibodies may have been diluted by plasma transfusion or exchange transfusion .'], ['**كبار السن**', '**نقص المناعة** أو **نقص غاما غلوبيولين الدم**.', '**زرع نخاع العظم** أو **ابيضاض الدم**', 'المرضى الذين **خُفّفت** أضداد ABO لديهم بـ**نقل البلازما** أو **النقل التبادلي**.'], start=2),
 H2("Resolution of Group I discrepancy", "حلّ اختلاف المجموعة الأولى"),
 L(["incubating the patient serum with reagent A1 and B cells at room temperature for approximately 15 to 30 minutes.",
    "If there is still no reaction after centrifugation, the serum-cell mixtures can be incubated at 4°C for 15 to 30 minutes."],
   ["**حضن مصل المريض مع كريات الكاشف A1 وB بدرجة حرارة الغرفة** لمدة **15 إلى 30 دقيقة** تقريبًا.",
    "وإذا لم يحدث تفاعل بعد النبذ، يمكن حضن خليط المصل والكريات **بدرجة 4°م لمدة 15 إلى 30 دقيقة**."],
   en="The best way to resolve this discrepancy is to enhance the weak or missing reaction in the serum by", ar="أفضل طريقة لحلّ هذا الاختلاف هي **تعزيز التفاعل الضعيف أو المفقود في المصل** بـ:"),
 BN("“hypogammaglobinemia” in the slide = hypogammaglobulinemia.", "“hypogammaglobinemia” في الشريحة أي hypogammaglobulinemia (نقص غاما غلوبيولين الدم)."),
 INSHORT([("Group I = **weak / missing antibodies** → **reverse grouping** problem (normal reactions are **4+**).", "المجموعة الأولى = **أضداد ضعيفة / مفقودة** ← مشكلة **التصنيف العكسي** (التفاعل الطبيعي **4+**)."),
          ("Causes: **newborns (< 3–6 months)**, elderly, immunodeficiency, BMT / leukemia, dilution by plasma or exchange transfusion.", "الأسباب: **حديثو الولادة (< 3–6 أشهر)**، كبار السن، نقص المناعة، زرع النخاع / الابيضاض، التخفيف بنقل البلازما أو التبادلي."),
          ("Fix: serum + A1 and B cells at **RT 15–30 min**, then **4°C 15–30 min**.", "الحل: المصل + كريات A1 وB **بحرارة الغرفة 15–30 دقيقة**، ثم **4°م 15–30 دقيقة**.")]),

 # ───────────────────────── 4. Group II
 SEC("Group II Discrepancies", "اختلافات المجموعة الثانية"),
 C(["**Group II Discrepancies –Weak or missing antigens (Forward grouping problem)** associated with unexpected reactions in the forward grouping due to weakly reacting or missing antigens.",
    "This group of discrepancies is probably the least frequently encountered."],
   ["**اختلافات المجموعة الثانية – مستضدات ضعيفة أو مفقودة (مشكلة في التصنيف المباشر)** ترتبط بتفاعلات غير متوقّعة في التصنيف المباشر بسبب **مستضدات ضعيفة التفاعل أو مفقودة**.",
    "وهذه المجموعة من الاختلافات هي **على الأرجح الأقل مصادفةً**."]),
 L(['Subgroups of A ( A3, AX , AM ) or B may be present'], ['قد توجد **تحت مجاميع A** (A3 وAX وAM) أو B'], en='**Causes :** Weak A or B antigen expression on RBCS . Examples in:', ar='**الأسباب:** ضعف التعبير عن مستضد A أو B على الكريات الحمر. أمثلة في:'),
 L(["Leukemia's , Hodgkin's disease, carcinoma may yield weakened A or B antigens", 'The “acquired B” phenomenon will show weak reactions with anti-B antisera and is most often associated with diseases of the digestive tract (e.g., cancer of the colon)'], ['**ابيضاض الدم** و**داء هودجكن** و**السرطان** قد تُضعف مستضدات A أو B', 'ظاهرة “**B المكتسب**” تُظهر تفاعلات ضعيفة مع مصل ضد B، وترتبط غالبًا **بأمراض القناة الهضمية** (مثل **سرطان القولون**)'], start=2),
 H2("Resolution of Common Group II Discrepancies", "حلّ اختلافات المجموعة الثانية الشائعة"),
 L([["by incubating the test mixture at room temperature for up to 30 minutes to increase the association of the antibody with the RBC antigen.", "If the reaction is still negative, incubate the text mixture at 4°C for 15 to 30min."],
    "RBCs can also be pretreated with enzymes and retested with reagent antisera."],
   [["**بحضن خليط الفحص بدرجة حرارة الغرفة حتى 30 دقيقة** لزيادة ارتباط الضد بمستضد الكريات.", "وإذا بقي التفاعل سالبًا، يُحضن الخليط **بدرجة 4°م لمدة 15 إلى 30 دقيقة**."],
    "ويمكن أيضًا **معاملة الكريات مسبقًا بالإنزيمات** ثم إعادة فحصها بالأمصال الكاشفة."]),
 BN("“text mixture” in the slide = **test** mixture.", "“text mixture” في الشريحة أي **test** mixture (خليط الفحص)."),
 INSHORT([("Group II = **weak / missing antigens** → **forward grouping** problem; the **least frequent** group.", "المجموعة الثانية = **مستضدات ضعيفة / مفقودة** ← مشكلة **التصنيف المباشر**؛ **الأقل** مصادفة."),
          ("Causes: **A subgroups (A3, Ax, Am)**, leukemia / Hodgkin / carcinoma, **acquired B** (colon cancer).", "الأسباب: **تحت مجاميع A (A3، Ax، Am)**، الابيضاض / هودجكن / السرطان، **B المكتسب** (سرطان القولون)."),
          ("Fix: **RT up to 30 min → 4°C 15–30 min**, or **enzyme-treated RBCs**.", "الحل: **حرارة الغرفة حتى 30 دقيقة ← 4°م 15–30 دقيقة**، أو **كريات معاملة بالإنزيمات**.")]),

 # ───────────────────────── 5. Group III
 SEC("Group III Discrepancies", "اختلافات المجموعة الثالثة"),
 C("**Group III Discrepancies –Protein or plasma abnormalities .**", "**اختلافات المجموعة الثالثة – شذوذات البروتين أو البلازما.**"),
 L(["Multiple Myeloma in which there is elevated levels of globulin.", "Elevated fibrinogen .", "Plasma expander such as dextran."],
   ["**الورم النقوي المتعدّد** الذي ترتفع فيه مستويات **الغلوبيولين**.", "**ارتفاع الفايبرينوجين**.", "**موسّعات البلازما** مثل **الدكستران**."],
   en="**Causes :** Rouleaux formation or excess plasma proteins interfering with reactions . Examples in:", ar="**الأسباب:** **تكوّن الرصّات (Rouleaux)** أو زيادة بروتينات البلازما التي تتداخل مع التفاعلات. أمثلة في:"),
 C("These will associated with discrepancies between forward and reverse groupings are caused by protein or plasma abnormalities",
   "وتسبّب هذه اختلافات بين التصنيف المباشر والعكسي ناتجة عن **شذوذات البروتين أو البلازما**"),
 H2("Resolution of Common Group III Discrepancies", "حلّ اختلافات المجموعة الثالثة الشائعة"),
 L(["by washing the patient’s RBCs several times with saline to remove excess proteins.",
    ["Performing a saline replacement technique .", "In this procedure, serum is removed and replaced by an equal volume of saline.", "In true agglutination, RBC clumping will still remain after washing."]],
   ["**بغسل كريات المريض عدّة مرات بالمحلول الملحي** لإزالة البروتينات الزائدة.",
    ["إجراء **تقنية استبدال المحلول الملحي**.", "وفيها يُزال المصل ويُستبدل **بحجم مساوٍ من المحلول الملحي**.", "وفي **التلازن الحقيقي** يبقى تكتّل الكريات بعد الغسل."]]),
 INSHORT([("Group III = **protein / plasma abnormalities** → **rouleaux** (false agglutination).", "المجموعة الثالثة = **شذوذات البروتين / البلازما** ← **رصّات** (تلازن كاذب)."),
          ("Causes: **multiple myeloma** (↑ globulin), **↑ fibrinogen**, **dextran**.", "الأسباب: **الورم النقوي المتعدّد** (↑ غلوبيولين)، **↑ فايبرينوجين**، **الدكستران**."),
          ("Fix: **wash RBCs with saline** + **saline replacement** — true agglutination stays, rouleaux disperse.", "الحل: **غسل الكريات بالملحي** + **استبدال المصل بالملحي** — التلازن الحقيقي يبقى والرصّات تتفرّق.")]),

 # ───────────────────────── 6. Group IV
 SEC("Group IV Discrepancies (miscellaneous problems)", "اختلافات المجموعة الرابعة (مشاكل متفرّقة)"),
 C("**Causes :** Mixed-field agglutination or rare conditions .", "**الأسباب:** **التلازن مختلط الحقل** أو حالات نادرة."),
 L(['Mixed cells population that results from Circulating RBCs of more than one ABO group due to RBC transfusion or marrow/stem cell transplant'], ['**مجتمع كريات مختلط** ناتج عن دوران كريات من **أكثر من فصيلة ABO** بسبب **نقل الكريات** أو **زرع النخاع / الخلايا الجذعية**'], en='These discrepancies between forward and reverse groupings are due to miscellaneous problems Examples in:', ar='هذه الاختلافات بين التصنيف المباشر والعكسي سببها **مشاكل متفرّقة**، أمثلة في:'),
 L(['Chimerism ( e.g in twin pregnancy)', 'Cold reactive autoantibodies in which RBCs are so heavily coated with antibody that they spontaneously agglutinate', 'Unexpected non-ABO alloantibodies.'], ['**الخيمرية** (مثلًا في **الحمل التوأمي**)', '**الأضداد الذاتية الباردة** التي تُغطّي الكريات بالضد بكثافة حتى **تتلازن تلقائيًا**', '**أضداد خيفية غير ABO غير متوقّعة**.'], start=2),
 H2("Resolution of Common Group IV Discrepancies", "حلّ اختلافات المجموعة الرابعة الشائعة"),
 L(["Review transfusion and transplant history.", "Perform antibody screen", "Run DAT (direct antiglobulin test) and auto control",
    "Used fresh sample if needed.", "Wash patient cells with warm saline and retest."],
   ["**مراجعة تاريخ النقل والزرع**.", "إجراء **تحرّي الأضداد**", "إجراء **اختبار مضاد الغلوبيولين المباشر (DAT)** و**الشاهد الذاتي**",
    "استعمال **عيّنة طازجة** عند الحاجة.", "**غسل كريات المريض بمحلول ملحي دافئ** وإعادة الفحص."]),
 T([B("Group", "المجموعة"), B("Problem", "المشكلة"), B("Examples", "أمثلة"), B("Resolution", "الحل")],
   [[B("**I**", "**الأولى**"), B("weak / missing **antibodies** (reverse)", "أضداد ضعيفة / مفقودة (العكسي)"), B("newborns, elderly, immunodeficiency", "الرضّع، المسنّون، نقص المناعة"), B("RT 15–30 min → 4°C", "حرارة الغرفة 15–30 ← 4°م")],
    [B("**II**", "**الثانية**"), B("weak / missing **antigens** (forward)", "مستضدات ضعيفة / مفقودة (المباشر)"), B("A subgroups, leukemia, acquired B", "تحت مجاميع A، الابيضاض، B المكتسب"), B("RT 30 min → 4°C; enzymes", "حرارة الغرفة 30 ← 4°م؛ إنزيمات")]],
   key_cols=[0], widths=[12, 28, 30, 30], style="summary", label_en="The four groups at a glance", label_ar="المجاميع الأربع بنظرة"),
 T([B("Group", "المجموعة"), B("Problem", "المشكلة"), B("Examples", "أمثلة"), B("Resolution", "الحل")],
   [[B("**III**", "**الثالثة**"), B("**protein / plasma** abnormalities", "شذوذات البروتين / البلازما"), B("myeloma, fibrinogen, dextran", "الورم النقوي، الفايبرينوجين، الدكستران"), B("saline wash / replacement", "غسل / استبدال ملحي")],
    [B("**IV**", "**الرابعة**"), B("**miscellaneous** (mixed field)", "متفرّقة (مختلط الحقل)"), B("transfusion / transplant, chimerism, cold autoantibodies", "نقل / زرع، خيمرية، أضداد ذاتية باردة"), B("history, antibody screen, DAT, warm wash", "التاريخ، تحرّي الأضداد، DAT، غسل دافئ")]],
   key_cols=[0], widths=[12, 28, 30, 30], style="summary", label_en="The four groups (cont.)", label_ar="المجاميع الأربع (تكملة)"),
 INSHORT([("Group IV = **miscellaneous / mixed-field**: transfusion or transplant, **chimerism**, **cold autoantibodies**, non-ABO alloantibodies.", "المجموعة الرابعة = **متفرّقة / مختلط الحقل**: نقل أو زرع، **خيمرية**، **أضداد ذاتية باردة**، أضداد خيفية غير ABO."),
          ("Fix: history, **antibody screen**, **DAT + auto control**, fresh sample, **warm saline wash**.", "الحل: التاريخ، **تحرّي الأضداد**، **DAT + الشاهد الذاتي**، عيّنة طازجة، **غسل بملحي دافئ**.")]),

 # ───────────────────────── 7. Practical 6
 SEC("Practical Blood Transfusion 6 — Antibody screening", "نقل الدم العملي 6 — تحرّي الأضداد"),
 C("**Practical Blood Transfusion 6** — ABO Blood and Rh Grouping (Part 2 )", "**نقل الدم العملي 6** — تحديد فصائل ABO وRh (الجزء 2)"),
 F("tubes-anti-abd.jpg", "Tubes labelled Anti-A, Anti-B and Anti-D", "أنابيب مُعلَّمة ضد A وضد B وضد D", h="56mm", fit="contain"),
 H2("Antibody screening ( Practical )", "تحرّي الأضداد (عملي)"),
 L(['The detection of antibodies directed against red blood cell antigens is critical in pre-transfusion compatibility testing.'], ['كشف الأضداد الموجّهة ضد مستضدات الكريات الحمر **حاسم في فحص التوافق قبل النقل**.']),
 L(['The focus of antibody screening methods is on clinically significant, unexpected antibodies, as the expected can be detected in other easier methods.'], ['تركّز طرق تحرّي الأضداد على **الأضداد غير المتوقّعة المهمة سريريًا**، لأن الأضداد المتوقّعة يمكن كشفها بطرق أسهل.'], start=2),
 L(['The unexpected antibodies of primary importance are the immune alloantibodies, which are produced in response to red blood cell (RBC) stimulation through transfusion, transplantation,or pregnancy.'], ['والأضداد غير المتوقّعة الأهم هي **الأضداد الخيفية المناعية** التي تُنتج استجابةً لتحفيز الكريات الحمر عبر **النقل أو الزرع أو الحمل**.'], start=3),
 L([['Clinically significant antibodies are those that cause decreased survival of RBCs possessing the target antigen.', 'These antibodies are typically IgG antibodies that react at 37°C or that react in the antihuman globulin (AHG) phase of the indirect antiglobulin test.']], [['**الأضداد المهمة سريريًا** هي التي **تقلّل بقاء الكريات** الحاملة للمستضد الهدف.', 'وهي عادةً **أضداد IgG تتفاعل بدرجة 37°م** أو في **طور مضاد الغلوبيولين البشري (AHG)** من **اختبار مضاد الغلوبيولين غير المباشر**.']], start=4),
 L(['To detect clinically significant antibodies in both the blood donor and the intended recipient as part of pre-transfusion compatibility testing.'], ['كشف الأضداد المهمة سريريًا **عند المتبرّع والمتلقّي** كجزء من فحص التوافق قبل النقل.'], en='**The standard use of an antibody screen are the following:**', ar='**الاستعمالات القياسية لتحرّي الأضداد:**'),
 L(['An antibody screen may be included when evaluating the compatibility of hematopoietic progenitor cell (HPC) and bone marrow donors with the intended transplant recipient.'], ['قد يُضمَّن تحرّي الأضداد عند تقييم توافق متبرّعي **الخلايا السلفية المكوّنة للدم (HPC)** و**نخاع العظم** مع متلقّي الزرع.'], start=2),
 L(['An antibody screen is included in standard prenatal testing for obstetric patients to evaluate the risk of HDFN in the fetus and to assess the mother’s candidacy for Rh-immune globulin (RHIG) prophylaxis.'], ['يُضمَّن تحرّي الأضداد في **فحوص ما قبل الولادة** للحوامل لتقييم خطر **داء انحلال الدم عند الجنين والوليد (HDFN)** ولتقييم أهلية الأم **للوقاية بالغلوبيولين المناعي Rh (RHIG)**.'], start=3),
 C("**** The main significance of test in blood banking is the use of test in pre-transfusion testing**", "**** الأهمية الرئيسية للفحص في بنك الدم هي استعماله في فحوص ما قبل النقل**"),
 L(["Tube Method", "Gel card method", "Solid phase adherence method"], ["طريقة الأنبوب", "طريقة بطاقة الهلام (Gel card)", "طريقة الالتصاق بالطور الصلب"],
   en="**Methods**", ar="**الطرق**"),
 C("Gel and solid phase adherence methods are alternatives to tube testing.", "طريقتا الهلام والالتصاق بالطور الصلب **بديلتان لفحص الأنبوب**."),
 H2("Tube Method", "طريقة الأنبوب"),
 C("The traditional method for detecting antibodies is an indirect antiglobulin test performed in a test tube", "الطريقة التقليدية لكشف الأضداد هي **اختبار مضاد الغلوبيولين غير المباشر** في أنبوب اختبار"),
 L([['**RBC reagents;** The RBC reagents used in the antibody screen come from group O individuals who have been typed for the most common, and the most significant, RBC antigens.', 'Group O cells are used so that anti-A and anti-B will not interfere in the detection of antibodies to other blood group systems.']], [['**كواشف الكريات الحمر:** تأتي من أفراد **فصيلة O** تم تحديد أشيع مستضدات الكريات وأهمها لديهم.', 'وتُستعمل **كريات O** حتى **لا يتداخل ضد A وضد B** في كشف أضداد أنظمة الفصائل الأخرى.']], en='**Requirement**', ar='**المستلزمات**'),
 L([['**Enhancement reagents;** various enhancement reagents, or potentiates, such as LISS( low ionic strength solution ) and PEG ( Polyethylene Glycol) may be added to the cell/serum mixture before the 37°C incubation phase to increase the sensitivity of the test system by promoting antigen-antibody binding or agglutination.', 'These reagents may also allow for a shortened incubation time.']], [['**الكواشف المعزّزة:** كواشف معزّزة أو مقوّيات مختلفة مثل **LISS (محلول منخفض القوة الأيونية)** و**PEG (البولي إثيلين غلايكول)** قد تُضاف لخليط الكريات/المصل **قبل طور الحضن بدرجة 37°م** لزيادة حساسية الفحص بتعزيز ارتباط المستضد بالضد أو التلازن.', 'وقد تسمح هذه الكواشف أيضًا **بتقصير زمن الحضن**.']], start=2),
 L(['**AHG reagents;** used to sensitize the reagent RBCs with the patient’s antibodies.'], ['**كواشف AHG:** تُستعمل **لتحسيس** كريات الكاشف بأضداد المريض.'], start=3),
 H2("Method overview", "نظرة عامة على الطريقة"),
 F("antibody-screen-tube.png", "Steps for performing the tube antibody screen test", "خطوات إجراء فحص تحرّي الأضداد بالأنبوب", h="56mm", fit="contain"),
 T([B("Phase", "الطور"), B("Text in the figure", "النص في الشكل")],
   [[B("**Immediate Spin phase** (optional)", "**طور النبذ الفوري** (اختياري)"), B("2 drops patient’s plasma + 1 drop screen cell reagent; Centrifuge; Observe for hemolysis and agglutination", "قطرتان من بلازما المريض + قطرة كاشف كريات التحرّي؛ نبذ؛ لاحظ الانحلال والتلازن")],
    [B("**37°C phase**", "**طور 37°م**"), B("Add enhancement reagent (optional); Incubate at 37°C — if antibodies present, RBC sensitization occurs; Centrifuge; Observe for hemolysis and agglutination", "أضف الكاشف المعزّز (اختياري)؛ احضن بدرجة 37°م — إذا وُجدت أضداد يحدث تحسيس الكريات؛ نبذ؛ لاحظ الانحلال والتلازن")]],
   key_cols=[0], widths=[26, 74], style="summary", label_en="Labels in the figure", label_ar="كتابات الشكل"),
 T([B("Phase", "الطور"), B("Text in the figure", "النص في الشكل")],
   [[B("**Wash**", "**الغسل**"), B("Wash 3 to 4 times with normal saline — unbound antibodies removed", "اغسل 3 إلى 4 مرات بالملحي الفسيولوجي — تُزال الأضداد غير المرتبطة")],
    [B("**AHG phase**", "**طور AHG**"), B("Add 2 drops AHG reagent — sensitized RBCs cross-linked by antibodies in AHG; Centrifuge; Observe for hemolysis and agglutination", "أضف قطرتين من كاشف AHG — ترتبط الكريات المحسَّسة تصالبيًا بأضداد AHG؛ نبذ؛ لاحظ الانحلال والتلازن")],
    [B("**Control**", "**الشاهد**"), B("Confirm negative reactions with Coombs control cells", "أكّد التفاعلات السالبة بكريات شاهد كومبس")]],
   key_cols=[0], widths=[26, 74], style="summary", label_en="Labels in the figure", label_ar="كتابات الشكل"),
 L(["The result expressed as agglutination, that could be graded according to its strength from 4+ to weak +",
    "The purpose of the antibody screen is to detect unexpected antibodies.",
    "Conclusive antibody identification is achieved when the serum containing the antibody is reactive, after the Ab has been identified, it should be tittered (Ab titration)"],
   ["تُعبَّر النتيجة **كتلازن** يمكن تدريجه حسب قوّته **من 4+ إلى + ضعيف**",
    "غرض تحرّي الأضداد هو **كشف الأضداد غير المتوقّعة**.",
    "يتحقّق **التحديد النهائي للضد** عندما يكون المصل الحاوي للضد متفاعلًا، وبعد تحديد الضد **يجب معايرته (معايرة الضد)**"]),
 L(["Cell-to-serum ratio", "Temperature", "Length of incubation", "PH."], ["نسبة الكريات إلى المصل", "درجة الحرارة", "مدّة الحضن", "الأس الهيدروجيني."],
   en=["**Limitations** — Several factors may influence the sensitivity of the antibody screen.", "These include:"], ar=["**المحدّدات** — عدّة عوامل قد تؤثّر في حساسية تحرّي الأضداد.", "وتشمل:"]),
 BN("“tittered” in the slide = **titered** (titration).", "“tittered” في الشريحة أي **titered** (معايرة)."),
 INSHORT([("Antibody screen detects **unexpected, clinically significant** antibodies — usually **IgG**, reacting at **37°C / AHG phase** (IAT).", "تحرّي الأضداد يكشف الأضداد **غير المتوقّعة المهمة سريريًا** — عادةً **IgG** تتفاعل **بدرجة 37°م / طور AHG** (اختبار غير مباشر)."),
          ("Uses: **pre-transfusion** (main), **HPC / marrow** transplant, **prenatal** (HDFN risk, RhIG).", "الاستعمالات: **قبل النقل** (الرئيسي)، زرع **HPC / النخاع**، **ما قبل الولادة** (خطر HDFN، RhIG)."),
          ("Methods: **tube** (traditional IAT), **gel card**, **solid phase**; screen cells are **group O**; enhancers **LISS / PEG**.", "الطرق: **الأنبوب** (IAT التقليدي)، **بطاقة الهلام**، **الطور الصلب**؛ كريات التحرّي **فصيلة O**؛ المعزّزات **LISS / PEG**."),
          ("Phases: immediate spin → **37°C** → wash ×3–4 → **AHG** → Coombs control cells; grade **4+ → weak +**.", "الأطوار: نبذ فوري ← **37°م** ← غسل 3–4 ← **AHG** ← كريات شاهد كومبس؛ التدريج **4+ ← + ضعيف**.")]),

 *TERMS6([("ABO discrepancy", "اختلاف (تعارض) فصيلة ABO / عدم تطابق التصنيف"),
          ("Forward (cell) grouping", "التصنيف المباشر / تصنيف الكريات"),
          ("Reverse (serum) grouping", "التصنيف العكسي / تصنيف المصل"),
          ("Transcription error", "خطأ النقل / خطأ التدوين"),
          ("Hypogammaglobulinemia", "نقص غاما غلوبيولين الدم"),
          ("Subgroups of A", "تحت مجاميع A / الفصائل الفرعية لـ A"),
          ("Acquired B", "B المكتسب"),
          ("Rouleaux formation", "تكوّن الرصّات / تراصّ الكريات كالعملات"),
          ("Multiple myeloma", "الورم النقوي المتعدّد"),
          ("Plasma expander (dextran)", "موسّع البلازما (الدكستران)"),
          ("Saline replacement technique", "تقنية الاستبدال بالمحلول الملحي"),
          ("Mixed-field agglutination", "التلازن مختلط الحقل"),
          ("Chimerism", "الخيمرية / الكيميرية"),
          ("Cold autoantibodies", "الأضداد الذاتية الباردة"),
          ("Direct antiglobulin test (DAT)", "اختبار مضاد الغلوبيولين المباشر / كومبس المباشر"),
          ("Antibody screening", "تحرّي الأضداد / مسح الأضداد"),
          ("Clinically significant antibody", "ضد مهم سريريًا"),
          ("Indirect antiglobulin test (IAT)", "اختبار مضاد الغلوبيولين غير المباشر / كومبس غير المباشر"),
          ("Enhancement reagent (LISS, PEG)", "كاشف معزّز / مقوٍّ"),
          ("Coombs control cells", "كريات شاهد كومبس / الكريات المحسَّسة بـ IgG"),
          ("HDFN", "داء انحلال الدم عند الجنين والوليد"),
          ("Antibody titration", "معايرة الضد / تعيين عيار الضد")]),
]

exec(open(__file__.replace("bb6.py", "bb6q.py")).read())

```
