---
source: BIOS-Obsidian/tools/scripts/imm456/ci5.py
handouts: [clinimm-lec5-behcet]
saved: 2026-10-28
tags: [bios, code]
---
# imm456/ci5.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#clinimm-lec5-behcet|clinimm-lec5-behcet]]

```python
import sys; sys.path.insert(0, "/tmp/claude-0/-home-user--/8f878068-bae9-502b-96f7-788f221c7cb0/scratchpad/imm456")
from ci import *

blocks = [
 SEC("Behcet's Disease", "داء بهجت"),
 C("Behcet's disease is a **rare, chronic, lifelong disorder** that involves **inflammation of blood vessels** throughout the body. It is a form of **vasculitis** that can lead to ulceration and other lesions, slightly affecting **more men than woman**.",
   "داء بهجت **اضطراب نادر مزمن يدوم مدى الحياة** يتضمّن **التهاب الأوعية الدموية** في أنحاء الجسم. وهو شكل من **التهاب الأوعية** قد يؤدي إلى تقرّحات وآفات أخرى، ويصيب **الرجال أكثر قليلًا من النساء**."),
 FLOW([("**aphthous ulceration of the oral mucous membranes**", "**تقرّح قلاعي للأغشية المخاطية الفموية**"), ("**and genitalia**", "**والأعضاء التناسلية**"), ("**and uveitis**", "**والتهاب العنبية**")],
      en="It is characterized by a **triad of symptoms**, including", ar="ويتميّز بـ**ثالوث من الأعراض** يشمل:"),
 C("**Rare manifestations** include **oligoarthritis** of the lower extremities, **vasculitis of the pulmonary vessels**, **cerebrovascular symptoms**.",
   "ومن **المظاهر النادرة**: **التهاب قلّة المفاصل** في الأطراف السفلية، و**التهاب الأوعية الرئوية**، و**أعراض وعائية دماغية**."),
 C("The etiology of the Behcet's disease is **unkown**. It is believed to be **partly genetic**, an association with **HLA-B51** has been found.",
   "سبب داء بهجت **مجهول**. ويُعتقد أنه **وراثي جزئيًا**، وقد وُجد ارتباط بـ**HLA-B51**."),
 F("behcet-pathogenesis.jpg", "Pathogencity of Behcet's disease", "إمراضية داء بهجت", h="62mm", fit="contain"),
 T([B("Label (from the figure)", "التسمية في الشكل"), B("Meaning", "المعنى")],
   [[B("Genetic Susceptibility", "الاستعداد الوراثي"), B("+ Epigenetic Changes", "+ تغيّرات فوق جينية")],
    [B("Immune System", "الجهاز المناعي"), B("Nonspecific Inflammation; Self-reactive autoinflammation", "التهاب غير نوعي؛ التهاب ذاتي متفاعل مع الذات")],
    [B("Inflammatory cytokines", "السيتوكينات الالتهابية"), B("Secretion of inflammatory cytokines (IL8, TNF-α)", "إفراز السيتوكينات الالتهابية (IL8 وTNF-α)")],
    [B("T and B cells", "الخلايا التائية والبائية"), B("Activation of cytotoxic T-Cells; Production of autoantibodies from B-Cells", "تنشيط الخلايا التائية السامّة؛ إنتاج أضداد ذاتية من الخلايا البائية")],
    [B("Result", "النتيجة"), B("Vasculitis/tissue damage \"Behcet's syndrome\"", "التهاب الأوعية/تلف الأنسجة «متلازمة بهجت»")],
    [B("Sign and Symptoms", "العلامات والأعراض"), B("inflamed eyes, mouth ulcers, genital ulcers, joint pain, skin problems", "التهاب العينين، تقرّحات الفم، تقرّحات تناسلية، ألم المفاصل، مشكلات جلدية")]],
   key_cols=[0], widths=[30, 70]),

 SEC("Risk factors", "عوامل الخطورة"),
 R("**Age.** Behcet's disease most commonly affects men and women in their **20s, 30s and 40s**, though children and older adults also can develop the condition. When the condition occurs at an **earlier age**, it tends to be **more severe**.",
   "**العمر.** يصيب داء بهجت غالبًا الرجال والنساء في **العشرينيات والثلاثينيات والأربعينيات**، وقد يصيب الأطفال وكبار السن أيضًا. وعندما يحدث **في سن مبكرة** يميل إلى أن يكون **أشد**."),
 R("**Geography.** Although the disease occurs worldwide, people from countries in the **Middle East and Asia**, including **Turkey, Iran, Iraq, Japan and China**, are more likely to develop Behcet's.",
   "**الجغرافيا.** مع أن المرض يحدث في أنحاء العالم، فإن سكان بلدان **الشرق الأوسط وآسيا**، ومنها **تركيا وإيران والعراق واليابان والصين**، أكثر عرضة للإصابة به."),
 R("**Sex.** While Behcet's disease occurs in both men and women, the disease is usually **more severe in men**.",
   "**الجنس.** يحدث داء بهجت لدى الرجال والنساء، لكنه عادةً **أشد عند الرجال**."),
 R("**Genes.** Having certain genes **HLA-B51** is associated with a higher risk of developing Behcet's.",
   "**الجينات.** امتلاك جينات معيّنة **HLA-B51** يرتبط بخطر أعلى للإصابة بداء بهجت."),
 T([B("Risk factor", "عامل الخطورة"), B("Remember", "للحفظ")],
   [[B("Age", "العمر"), B("20s–40s; earlier age = more severe", "العشرينيات إلى الأربعينيات؛ كلما كان أبكر كان أشد")],
    [B("Geography", "الجغرافيا"), B("Middle East and Asia (Turkey, Iran, Iraq, Japan, China)", "الشرق الأوسط وآسيا (تركيا، إيران، العراق، اليابان، الصين)")],
    [B("Sex", "الجنس"), B("Both; more severe in men", "الجنسان؛ أشد عند الرجال")],
    [B("Genes", "الجينات"), B("HLA-B51", "HLA-B51")]],
   key_cols=[0], widths=[30, 70], style="summary", label_en="Risk factors at a glance", label_ar="عوامل الخطورة باختصار"),

 SEC("Clinical features", "المظاهر السريرية"),
 T([B("Site", "الموضع"), B("Feature", "المظهر")],
   [[B("Mouth", "الفم"), B("Painful mouth sores, identical to canker sores, are the most common sign of Behcet's disease. Sores begin as raised, round lesions in the mouth that quickly turn into painful ulcers. The sores heal usually in seven to 21 days, though they do recur.",
     "قرح فموية مؤلمة مطابقة لقرح القلاع، وهي أكثر علامات داء بهجت شيوعًا. تبدأ القرح آفاتٍ مرتفعة مستديرة في الفم تتحوّل سريعًا إلى قرح مؤلمة. وتلتئم عادةً خلال 7 إلى 21 يومًا لكنها تتكرّر.")],
    [B("Skin", "الجلد"), B("Skin lesions may occur. Skin problems can vary. Some people may develop acne-like sores on their bodies. Others may develop nodules on the lower legs.",
     "قد تحدث آفات جلدية. وتتنوّع المشكلات الجلدية. فقد يصاب بعضهم بقرح شبيهة بحب الشباب على الجسم. ويصاب آخرون بعقيدات على الساقين.")],
    [B("Genitals", "الأعضاء التناسلية"), B("Sores on the genitals, most commonly on the scrotum or the vulva.", "قرح على الأعضاء التناسلية، أكثرها على الصفن أو الفرج.")],
    [B("Eyes", "العينان"), B("Inflammation in the eye — uveitis — causes redness, pain and blurred vision in one or both eyes.", "التهاب العين — التهاب العنبية — يسبّب الاحمرار والألم وتشوّش الرؤية في عين واحدة أو كلتيهما.")],
    [B("Joints", "المفاصل"), B("Joint swelling and pain most commonly affect the knee.", "تورّم المفاصل وألمها يصيبان الركبة غالبًا.")],
    [B("Vascular system", "الجهاز الوعائي"), B("Inflammation in veins and large arteries, causing redness, pain and swelling in the arms or legs when a blood clot results.", "التهاب الأوردة والشرايين الكبيرة، يسبّب احمرار الذراعين أو الساقين وألمهما وتورّمهما عند تكوّن خثرة دموية.")],
    [B("Digestive system", "الجهاز الهضمي"), B("Abdominal pain, diarrhea or bleeding.", "ألم بطني أو إسهال أو نزف.")],
    [B("Brain", "الدماغ"), B("Inflammation in the brain and nervous system that leads to headache, fever, disorientation, poor balance or stroke.", "التهاب الدماغ والجهاز العصبي يؤدي إلى الصداع والحمّى والتوهان وضعف التوازن أو السكتة الدماغية.")]],
   key_cols=[0], widths=[20, 80]),

 SEC("Diagnosis", "التشخيص"),
 C("There is **no diagnostic test** and the diagnosis is **entirely clinical**. Laboratory findings are **nonspecific** and reflect the inflammatory state, **C-reactive protein** levels, **erythrocyte sedimentation rate (ESR)**, **leukocyte count**, **complement components**, and **acute-phase reactants** may all be **elevated during an acute attack**. Internationally accepted diagnosis criteria have been published recently.",
   "**لا يوجد فحص تشخيصي**، والتشخيص **سريري بالكامل**. والموجودات المختبرية **غير نوعية** وتعكس الحالة الالتهابية؛ فقد ترتفع **مستويات CRP** و**سرعة ترسيب الكريات الحمر (ESR)** و**عدد الكريات البيض** و**مكوّنات المتمّمة** و**متفاعلات الطور الحاد** جميعها **خلال النوبة الحادة**. ونُشرت حديثًا معايير تشخيص مقبولة دوليًا."),
 H2("International Clinical Criteria for Behcet's Disease", "المعايير السريرية الدولية لداء بهجت"),
 C("An international group of physicians has established a set of guidelines to aid in the classification of Behcet's patients. The International Clinical Criteria for Behcet's Disease classification states patients must present with:",
   "وضعت مجموعة دولية من الأطباء مجموعة إرشادات للمساعدة في تصنيف مرضى بهجت. وتنص المعايير السريرية الدولية لتصنيف داء بهجت على أن المرضى يجب أن يُظهروا:"),
 C("**Recurrent oral ulcerations** (apthous or herpetiform) **at least three times in one year**.",
   "**تقرّحات فموية متكرّرة** (قلاعية أو شبيهة بالهربس) **ثلاث مرات على الأقل في السنة**."),
 L(["**Recurrent genital ulcerations.**",
    "**Eye lesions** (uveitis or retinal vasculitis) observed by an ophthalmologist.",
    "**Skin lesions** (a variety of rashes or acne-like sores) may be caused by Behcet's disease. Positive",
    "**Positive pathergy test**, your doctor inserts a **sterile needle** into your skin and then examines the area **two days later**. If the pathergy test is positive, a **small red bump** forms under your skin where the needle was inserted. This indicates your immune system is **overreacting to the minor injury**."],
   ["**تقرّحات تناسلية متكرّرة.**",
    "**آفات عينية** (التهاب العنبية أو التهاب أوعية الشبكية) يلاحظها طبيب العيون.",
    "**آفات جلدية** (طفوح متنوعة أو قرح شبيهة بحب الشباب) قد يسبّبها داء بهجت. [كلمة «Positive» مكرّرة في المصدر]",
    "**اختبار الباثيرجي (فرط التفاعل) الموجب:** يُدخل الطبيب **إبرة معقّمة** في الجلد ثم يفحص المنطقة **بعد يومين**. فإذا كان الاختبار موجبًا تتكوّن **نتوءة حمراء صغيرة** تحت الجلد مكان الإبرة. وهذا يدل على أن الجهاز المناعي **يبالغ في التفاعل مع إصابة بسيطة**."],
   en="**Additionally, patients must present any two of the following:**", ar="**إضافةً إلى ذلك يجب أن يُظهر المريض اثنين من الآتي:**"),
 T([B("Criterion", "المعيار"), B("Required", "المطلوب")],
   [[B("Recurrent oral ulcers ≥ 3 times/year", "قرح فموية متكرّرة 3 مرات على الأقل في السنة"), B("**Must** (1 major)", "**إلزامي** (معيار رئيس واحد)")],
    [B("Genital ulcers · Eye lesions · Skin lesions · Positive pathergy test", "قرح تناسلية · آفات عينية · آفات جلدية · اختبار باثيرجي موجب"), B("**Any 2**", "**أي اثنين**")]],
   key_cols=[0], widths=[66, 34], style="summary", label_en="Diagnosis = 1 + 2", label_ar="التشخيص = 1 + 2"),
] + END(
 [("Behcet's = rare, chronic, lifelong **vasculitis**; slightly **more men**.", "داء بهجت = **التهاب أوعية** نادر مزمن مدى الحياة؛ **الرجال أكثر قليلًا**."),
  ("**Triad:** oral aphthous ulcers + genital ulcers + uveitis.", "**الثالوث:** قرح فموية قلاعية + قرح تناسلية + التهاب العنبية."),
  ("Cause unknown, partly genetic: **HLA-B51**.", "السبب مجهول ووراثي جزئيًا: **HLA-B51**."),
  ("Risk: **20s–40s** (earlier = more severe), **Middle East & Asia** (incl. Iraq), **more severe in men**.", "الخطورة: **العشرينيات–الأربعينيات** (الأبكر أشد)، **الشرق الأوسط وآسيا** (ومنها العراق)، **أشد عند الرجال**."),
  ("Mouth sores = **most common sign**; heal in **7–21 days** and recur.", "قرح الفم = **أشيع علامة**؛ تلتئم خلال **7–21 يومًا** وتتكرّر."),
  ("**No diagnostic test** — diagnosis is **clinical**; CRP, ESR, WBC, complement rise in attacks (nonspecific).", "**لا فحص تشخيصي** — التشخيص **سريري**؛ ترتفع CRP وESR والبيض والمتمّمة في النوبات (غير نوعية)."),
  ("Criteria: **oral ulcers ≥ 3/year + any 2** of genital ulcers, eye lesions, skin lesions, positive pathergy.", "المعايير: **قرح فموية 3 مرات سنويًا على الأقل + أي اثنين** من القرح التناسلية والآفات العينية والجلدية والباثيرجي الموجب."),
  ("**Pathergy test:** sterile needle → read after **2 days** → small red bump = positive.", "**اختبار الباثيرجي:** إبرة معقّمة ← يُقرأ بعد **يومين** ← نتوءة حمراء صغيرة = موجب.")],
 [("Behcet's disease", "داء بهجت / مرض بهجت / متلازمة بهجت"),
  ("Vasculitis", "التهاب الأوعية الدموية / التهاب وعائي"),
  ("Aphthous ulcer", "قرحة قلاعية / قلاع / تقرّح فموي"),
  ("Canker sore", "قرحة الفم / القلاع البسيط / الحويصلة الفموية"),
  ("Uveitis", "التهاب العنبية / التهاب القزحية والجسم الهدبي"),
  ("Oligoarthritis", "التهاب قلّة المفاصل / التهاب مفاصل قليلة العدد"),
  ("Pathergy test", "اختبار الباثيرجي / اختبار فرط التفاعل الجلدي / اختبار الوخز"),
  ("Lesion", "آفة / إصابة / تلف موضعي"),
  ("Nodule", "عقيدة / عقدة صغيرة"),
  ("Scrotum", "الصفن / كيس الخصية"),
  ("Vulva", "الفرج / الأعضاء التناسلية الخارجية الأنثوية"),
  ("Acute-phase reactants", "متفاعلات الطور الحاد / بروتينات المرحلة الحادة"),
  ("Complement", "المتمّمة / المتمّم / النظام المكمّل"),
  ("Epigenetic", "فوق جيني / فوق وراثي / لا جيني"),
  ("Cytokine", "سيتوكين / حركي خلوي"),
  ("Disorientation", "التوهان / فقدان التوجّه / التشوّش")])


mcq = [
 {"topic_en": "Definition and etiology", "topic_ar": "التعريف والسببيات"},
 Q("Behcet's disease is a form of:", "داء بهجت شكل من:",
   P(("Vasculitis", "التهاب الأوعية"), ("Arthritis only", "التهاب المفاصل فقط"), ("Nephritis", "التهاب الكلية"), ("Hepatitis", "التهاب الكبد")), "a"),
 Q("The triad of Behcet's disease includes all EXCEPT:", "يشمل ثالوث داء بهجت كل ما يأتي عدا:",
   P(("Oral aphthous ulcers", "قرح فموية قلاعية"), ("Genital ulcers", "قرح تناسلية"), ("Uveitis", "التهاب العنبية"), ("Dry mouth", "جفاف الفم")), "d"),
 Q("Behcet's disease is associated with:", "يرتبط داء بهجت بـ:",
   P(("HLA-B27", "HLA-B27"), ("HLA-B51", "HLA-B51"), ("HLA-DR4", "HLA-DR4"), ("HLA-DQ2", "HLA-DQ2")), "b"),
 Q("A rare manifestation of Behcet's disease is:", "من المظاهر النادرة لداء بهجت:",
   P(("Oral ulcers", "قرح الفم"), ("Vasculitis of the pulmonary vessels", "التهاب الأوعية الرئوية"), ("Genital ulcers", "القرح التناسلية"), ("Uveitis", "التهاب العنبية")), "b"),
 Q("In the pathogenesis figure, the inflammatory cytokines secreted are:", "في شكل الإمراضية تكون السيتوكينات الالتهابية المفرزة:",
   P(("IL-4 and IL-5", "IL-4 وIL-5"), ("IL8 and TNF-α", "IL8 وTNF-α"), ("IL-10 and TGF-β", "IL-10 وTGF-β"), ("IFN-α", "IFN-α")), "b"),

 {"topic_en": "Risk factors", "topic_ar": "عوامل الخطورة"},
 Q("Behcet's disease most commonly affects people in their:", "يصيب داء بهجت غالبًا من هم في:",
   P(("Childhood", "الطفولة"), ("20s, 30s and 40s", "العشرينيات والثلاثينيات والأربعينيات"), ("60s and 70s", "الستينيات والسبعينيات"), ("Infancy", "الرضاعة")), "b"),
 Q("When Behcet's occurs at an earlier age, it tends to be:", "عندما يحدث بهجت في سن مبكرة يميل إلى أن يكون:",
   P(("Milder", "أخف"), ("More severe", "أشد"), ("Asymptomatic", "بلا أعراض"), ("Self-limited", "محدودًا ذاتيًا")), "b"),
 Q("Behcet's disease is usually more severe in:", "داء بهجت عادةً أشد عند:",
   P(("Women", "النساء"), ("Men", "الرجال"), ("Children", "الأطفال"), ("Elderly women", "المسنّات")), "b"),
 Q("Which country is mentioned among those with higher risk:", "أي بلد ذُكر ضمن الأعلى خطورة:",
   P(("Iraq", "العراق"), ("Brazil", "البرازيل"), ("Canada", "كندا"), ("Australia", "أستراليا")), "a"),

 {"topic_en": "Clinical features", "topic_ar": "المظاهر السريرية"},
 Q("The most common sign of Behcet's disease is:", "أكثر علامات داء بهجت شيوعًا:",
   P(("Painful mouth sores", "قرح فموية مؤلمة"), ("Uveitis", "التهاب العنبية"), ("Knee swelling", "تورّم الركبة"), ("Stroke", "السكتة")), "a"),
 Q("Mouth sores in Behcet's usually heal in:", "تلتئم قرح الفم في بهجت عادةً خلال:",
   P(("1–2 days", "1–2 يوم"), ("7 to 21 days", "7 إلى 21 يومًا"), ("2 months", "شهرين"), ("They never heal", "لا تلتئم")), "b"),
 Q("Skin lesions in Behcet's may include:", "قد تشمل الآفات الجلدية في بهجت:",
   P(("Acne-like sores and nodules on the lower legs", "قرحًا شبيهة بحب الشباب وعقيدات على الساقين"), ("Butterfly rash", "طفحًا فراشيًا"), ("Psoriatic plaques", "لويحات صدفية"), ("Vitiligo", "البهاق")), "a"),
 Q("Genital sores in Behcet's most commonly occur on:", "تحدث القرح التناسلية في بهجت غالبًا على:",
   P(("The scrotum or the vulva", "الصفن أو الفرج"), ("The penis shaft", "جسم القضيب"), ("The cervix", "عنق الرحم"), ("The urethra", "الإحليل")), "a"),
 Q("The eye involvement in Behcet's disease is called:", "إصابة العين في داء بهجت تُسمّى:",
   P(("Keratitis", "التهاب القرنية"), ("Uveitis", "التهاب العنبية"), ("Cataract", "الساد"), ("Glaucoma", "الزرق")), "b"),
 Q("The joint most commonly affected in Behcet's disease is the:", "المفصل الأكثر إصابة في داء بهجت:",
   P(("Hip", "الورك"), ("Knee", "الركبة"), ("Shoulder", "الكتف"), ("Wrist", "الرسغ")), "b"),

 {"topic_en": "Diagnosis", "topic_ar": "التشخيص"},
 Q("The diagnosis of Behcet's disease is:", "تشخيص داء بهجت:",
   P(("By a specific serological test", "بفحص مصلي نوعي"), ("Entirely clinical", "سريري بالكامل"), ("By biopsy only", "بالخزعة فقط"), ("By HLA typing only", "بتحديد HLA فقط")), "b"),
 Q("During an acute attack, all of the following may be elevated EXCEPT:", "خلال النوبة الحادة قد يرتفع كل ما يأتي عدا:",
   P(("CRP", "CRP"), ("ESR", "ESR"), ("Leukocyte count", "عدد الكريات البيض"), ("A specific Behcet autoantibody", "ضد ذاتي نوعي لبهجت")), "d"),
 Q("The required major criterion is recurrent oral ulceration at least:", "المعيار الرئيس المطلوب تقرّح فموي متكرّر على الأقل:",
   P(("Once a year", "مرة في السنة"), ("Three times in one year", "ثلاث مرات في السنة"), ("Monthly", "شهريًا"), ("Twice in a lifetime", "مرتين في العمر")), "b"),
 Q("In addition to oral ulcers, patients must present:", "إضافةً إلى قرح الفم يجب أن يُظهر المريض:",
   P(("Any one criterion", "معيارًا واحدًا"), ("Any two of the other criteria", "اثنين من المعايير الأخرى"), ("All other criteria", "كل المعايير الأخرى"), ("A positive ANA", "ANA موجبًا")), "b"),
 Q("The pathergy test is read:", "يُقرأ اختبار الباثيرجي:",
   P(("Immediately", "فورًا"), ("After 2 hours", "بعد ساعتين"), ("Two days later", "بعد يومين"), ("After one week", "بعد أسبوع")), "c"),
 Q("A positive pathergy test shows:", "يُظهر اختبار الباثيرجي الموجب:",
   P(("A small red bump where the needle was inserted", "نتوءة حمراء صغيرة مكان الإبرة"), ("No change", "لا تغيير"), ("Bleeding", "نزفًا"), ("A blister far from the site", "فقاعة بعيدة عن الموضع")), "a"),
 Q("Eye lesions as a criterion must be observed by:", "يجب أن يلاحظ الآفات العينية بوصفها معيارًا:",
   P(("The patient", "المريض"), ("An ophthalmologist", "طبيب العيون"), ("A dermatologist", "طبيب الجلدية"), ("A nurse", "ممرض")), "b"),
]
tf = [
 TF("Behcet's disease is a rare, chronic, lifelong disorder.", "داء بهجت اضطراب نادر مزمن يدوم مدى الحياة.", "T"),
 TF("Behcet's disease affects women slightly more than men.", "يصيب داء بهجت النساء أكثر قليلًا من الرجال.", "F"),
 TF("The etiology of Behcet's disease is well known.", "سبب داء بهجت معروف جيدًا.", "F"),
 TF("HLA-B51 is associated with a higher risk of Behcet's.", "يرتبط HLA-B51 بخطر أعلى لداء بهجت.", "T"),
 TF("Children and older adults cannot develop Behcet's disease.", "لا يمكن أن يصاب الأطفال وكبار السن بداء بهجت.", "F"),
 TF("Mouth sores in Behcet's recur.", "تتكرّر قرح الفم في بهجت.", "T"),
 TF("Uveitis may cause redness, pain and blurred vision.", "قد يسبّب التهاب العنبية الاحمرار والألم وتشوّش الرؤية.", "T"),
 TF("Behcet's disease may cause stroke.", "قد يسبّب داء بهجت السكتة الدماغية.", "T"),
 TF("There is a specific diagnostic laboratory test for Behcet's disease.", "يوجد فحص مختبري تشخيصي نوعي لداء بهجت.", "F"),
 TF("Laboratory findings in Behcet's are nonspecific.", "الموجودات المختبرية في بهجت غير نوعية.", "T"),
 TF("A positive pathergy test indicates an immune overreaction to minor injury.", "يدل اختبار الباثيرجي الموجب على فرط تفاعل مناعي مع إصابة بسيطة.", "T"),
 TF("Recurrent genital ulceration is the mandatory major criterion.", "التقرّح التناسلي المتكرّر هو المعيار الرئيس الإلزامي.", "F"),
]
traps = [
 TR("Which criterion is mandatory?", "أي معيار إلزامي؟", "Recurrent oral ulceration at least 3 times in one year — plus any two of: genital ulcers, eye lesions, skin lesions, positive pathergy test.", "التقرّح الفموي المتكرّر 3 مرات على الأقل في السنة — مع أي اثنين من: القرح التناسلية، الآفات العينية، الآفات الجلدية، الباثيرجي الموجب."),
 TR("More common or more severe in men?", "أكثر شيوعًا أم أشد عند الرجال؟", "Both in this lecture: slightly more men are affected, and the disease is usually more severe in men.", "كلاهما في المحاضرة: يصيب الرجال أكثر قليلًا، وهو عادةً أشد عندهم."),
 TR("Earlier age — milder or more severe?", "سن مبكرة — أخف أم أشد؟", "More severe.", "أشد."),
 TR("HLA-B51 or HLA-B27?", "HLA-B51 أم HLA-B27؟", "Behcet's disease is associated with HLA-B51.", "يرتبط داء بهجت بـHLA-B51."),
 TR("When is the pathergy test read?", "متى يُقرأ اختبار الباثيرجي؟", "Two days after inserting a sterile needle; a small red bump = positive.", "بعد يومين من إدخال إبرة معقّمة؛ والنتوءة الحمراء الصغيرة = موجب."),
]
important = [
 IM("Define Behcet's disease and its triad of symptoms.", "عرّف داء بهجت وثالوث أعراضه.", "A rare, chronic, lifelong vasculitis with inflammation of blood vessels throughout the body; triad: aphthous ulceration of the oral mucous membranes and genitalia, and uveitis; associated with HLA-B51.", "التهاب أوعية نادر مزمن مدى الحياة يصيب الأوعية في أنحاء الجسم؛ ثالوثه: تقرّح قلاعي للمخاطية الفموية والأعضاء التناسلية والتهاب العنبية؛ ويرتبط بـHLA-B51."),
 IM("List the risk factors for Behcet's disease.", "عدّد عوامل خطورة داء بهجت.", "Age (20s–40s; earlier onset is more severe), geography (Middle East and Asia: Turkey, Iran, Iraq, Japan, China), sex (more severe in men), genes (HLA-B51).", "العمر (20–40؛ البدء المبكر أشد)، الجغرافيا (الشرق الأوسط وآسيا: تركيا وإيران والعراق واليابان والصين)، الجنس (أشد عند الرجال)، الجينات (HLA-B51)."),
 IM("List the clinical features of Behcet's disease.", "عدّد المظاهر السريرية لداء بهجت.", "Mouth (painful sores, most common, heal in 7–21 days and recur), skin (acne-like sores, leg nodules), genitals (scrotum, vulva), eyes (uveitis), joints (knee), vascular (veins and large arteries, clots), digestive (pain, diarrhea, bleeding), brain (headache, fever, disorientation, poor balance, stroke).", "الفم (قرح مؤلمة، الأكثر شيوعًا)، الجلد، الأعضاء التناسلية، العينان (التهاب العنبية)، المفاصل (الركبة)، الأوعية (خثرات)، الجهاز الهضمي، الدماغ (صداع، حمّى، توهان، سكتة)."),
 IM("State the International Clinical Criteria for Behcet's disease.", "اذكر المعايير السريرية الدولية لداء بهجت.", "Recurrent oral ulcerations (aphthous or herpetiform) at least three times in one year, plus any two of: recurrent genital ulcerations, eye lesions (uveitis or retinal vasculitis) seen by an ophthalmologist, skin lesions, positive pathergy test.", "تقرّحات فموية متكرّرة (قلاعية أو شبيهة بالهربس) 3 مرات على الأقل في السنة، مع أي اثنين من: تقرّحات تناسلية متكرّرة، آفات عينية يلاحظها طبيب العيون، آفات جلدية، اختبار باثيرجي موجب."),
 IM("Describe the pathergy test.", "صف اختبار الباثيرجي.", "A sterile needle is inserted into the skin and the area is examined two days later; a small red bump at the site is positive, indicating an immune overreaction to minor injury.", "تُدخل إبرة معقّمة في الجلد وتُفحص المنطقة بعد يومين؛ والنتوءة الحمراء الصغيرة موجبة، وتدل على فرط تفاعل مناعي مع إصابة بسيطة."),
]
meta = dict(CI, unit_en="Lecture 5", unit_ar="المحاضرة 5", unit_no="5", title_en="Behcet's Disease", title_ar="داء بهجت")
save("clinimm-lec5-behcet", meta, blocks, balance(mcq, 65), tf, traps, important)

```
