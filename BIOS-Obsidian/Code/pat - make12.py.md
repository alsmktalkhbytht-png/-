---
source: BIOS-Obsidian/tools/scripts/pat/make12.py
handouts: [pathology-lec1-2-atelectasis]
saved: 2026-10-29
tags: [bios, code]
---
# pat/make12.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#pathology-lec1-2-atelectasis|pathology-lec1-2-atelectasis]]

```python
import json, os
from collections import Counter
def C(en, ar, **k): return dict(t="card", en=en, ar=ar, **k)
def R(en, ar): return dict(t="rule", en=en, ar=ar)
def SEC(en, ar): return dict(t="section", en=en, ar=ar)
def H2(en, ar): return dict(t="h2", en=en, ar=ar)
def F(src, en, ar, **k): return dict(t="figure", src="assets/" + src, en=en, ar=ar, **k)
def N(en, ar, label=None):
    b = dict(t="note", en=en, ar=ar)
    if label: b["label"] = label
    return b

blocks = [
 SEC("Atelectasis (collapse)", "انخماص الرئة (الانهيار)"),
 C(["The major function of the lung is to replenish oxygen and excrete carbon dioxide from blood.",
    "The right lung bud eventually divides into three main bronchi, and the left into two main bronchi, thus giving rise to three lobes on the right and two on the left."],
   ["الوظيفة الرئيسة للرئة هي **تجديد الأوكسجين** في الدم و**طرح ثاني أوكسيد الكاربون** منه.",
    "يتفرّع برعم الرئة اليمنى في النهاية إلى **ثلاث قصبات رئيسة**، واليسرى إلى **قصبتين رئيستين**، فينشأ بذلك **ثلاثة فصوص في اليمين وفصّان في اليسار**."]),
 F("respiratory-system.jpg", "The upper and lower respiratory tract", "الجهاز التنفسي العلوي والسفلي", h="70mm"),

 SEC("Alveolar wall structure", "تركيب جدار الأسناخ"),
 C("The microscopic structure of the alveolar walls (or alveolar septa) consists of the following components, proceeding from blood to air ;",
   "يتكوّن التركيب المجهري لجدران الأسناخ (أو **الحواجز السنخية** `alveolar septa`) من المكوّنات الآتية، بدءًا من الدم باتجاه الهواء؛"),
 R("The **capillary endothelium** and **basement membrane**.", "**بطانة الشعيرات الدموية** و**الغشاء القاعدي**."),
 R(["The **pulmonary interstitium** is composed of fine elastic fibers, small bundles of collagen, a few fibroblast-like cells, smooth muscle cells, mast cells, and rare mono-nuclear cells.",
    "It is most prominent in thicker portions of the alveolar septum."],
   ["يتكوّن **النسيج الخلالي الرئوي** من ألياف مرنة دقيقة، وحزم صغيرة من الكولاجين، وقليل من الخلايا الشبيهة بالأرومات الليفية، وخلايا عضلية ملساء، وخلايا بدينة، وخلايا وحيدة النواة نادرة.",
    "ويكون أوضح ما يكون في الأجزاء الأسمك من الحاجز السنخي."]),
 R(["**Alveolar epithelium** contains a continuous layer of two principal cell types: flattened, platelike **type I pneumocytes** covering **95%** of the alveolar surface and rounded **type II pneumocytes**.",
    "The latter **synthesize pulmonary surfactant** and are the main cell type involved in **repair** of alveolar epithelium after damage to type I pneumocytes."],
   ["تحتوي **ظهارة الأسناخ** على طبقة متصلة من نوعين رئيسين من الخلايا: **الخلايا الرئوية من النوع الأول** المسطّحة الصفيحية التي تغطي **95%** من سطح الأسناخ، و**الخلايا الرئوية من النوع الثاني** المستديرة.",
    "وهذه الأخيرة **تصنع المادة الفاعلة بالسطح الرئوية** (`surfactant`)، وهي النوع الرئيس من الخلايا المسؤول عن **إصلاح** ظهارة الأسناخ بعد تضرّر خلايا النوع الأول."]),
 C(["The alveolar walls are not solid but are perforated by numerous **pores of Kohn**, which permit passage of air, bacteria, and exudates between adjacent alveoli."],
   ["وجدران الأسناخ ليست مصمتة، بل تثقبها **مسامات كون** (`pores of Kohn`) العديدة، التي تسمح بمرور الهواء والبكتريا والنضحات بين الأسناخ المتجاورة."]),
 R(["A few **alveolar macrophages** usually lie free within the alveolar space.",
    "In the adult, these macrophages often contain phagocytosed **carbon particles**."],
   ["تقع عادةً بضع **بلاعم سنخية** حرّة داخل الفراغ السنخي.",
    "وفي البالغ، غالبًا ما تحتوي هذه البلاعم على **دقائق كاربون** مبلوعة."]),

 SEC("Primary lung diseases", "أمراض الرئة الأولية"),
 C("There are multiple primary lung diseases that can broadly be divided into those primarily affecting",
   "توجد أمراض رئوية أولية متعددة يمكن تقسيمها بشكل عام إلى تلك التي تصيب أساسًا",
   list_en=["The airways,", "The interstitium, and", "The pulmonary vascular system."],
   list_ar=["المجاري الهوائية،", "النسيج الخلالي، و", "الجهاز الوعائي الرئوي."]),
 dict(t="figures", items=[
   dict(src="assets/alveolar-wall.jpg", en="Microscopic structure of the alveolar wall", ar="التركيب المجهري لجدار السنخ", h="62mm", fit="contain"),
   dict(src="assets/lung-alveoli.jpg", en="Trachea, bronchial tubes and the alveoli with their capillary network", ar="الرغامى والأنابيب القصبية والأسناخ مع شبكتها الشعرية", h="62mm", fit="contain")]),

 SEC("Atelectasis (collapse)", "انخماص الرئة (الانهيار)"),
 C(["**Atelectasis**, also known as **collapse**, is **loss of lung volume** caused by **inadequate expansion of air spaces**.",
    "It results in **shunting** of inadequately oxygenated blood from pulmonary arteries into veins, thus giving rise to a **ventilation-perfusion imbalance** and **hypoxia**."],
   ["**انخماص الرئة** (`Atelectasis`)، ويُعرف أيضًا بـ**الانهيار** (`collapse`)، هو **فقدان حجم الرئة** الناتج عن **عدم كفاية تمدّد الفراغات الهوائية**.",
    "ويؤدي إلى **تحويلة** (`shunting`) للدم غير المؤكسج بشكل كافٍ من الشرايين الرئوية إلى الأوردة، فينشأ بذلك **عدم توازن بين التهوية والتروية** و**نقص الأكسجة** (`hypoxia`)."]),
 dict(t="figures", items=[
   dict(src="assets/collapsed-lung.jpg", en="Collapsed lung", ar="رئة منخمصة (منهارة)", h="64mm", fit="contain"),
   dict(src="assets/atelectasis-forms.jpg", en="Various forms of acquired atelectasis: resorption, compression and contraction", ar="الأشكال المختلفة لانخماص الرئة المكتسب: الامتصاصي والانضغاطي والتقلّصي", h="64mm", fit="contain")]),
 C("**On the basis of the underlying mechanism or the distribution of alveolar collapse, atelectasis is classified into three forms.**",
   "**على أساس الآلية المسبِّبة أو توزيع انهيار الأسناخ، يُصنَّف انخماص الرئة إلى ثلاثة أشكال.**"),

 dict(t="side", blocks=[dict(t="group", title_en="1- Resorption atelectasis", title_ar="1- الانخماص الامتصاصي",
   en=["Resorption atelectasis occurs when an **obstruction** prevents air from reaching distal airways.",
       "The air already present gradually becomes **absorbed**, and alveolar collapse follows.",
       "Depending on the level of airway obstruction, an entire lung, a complete lobe, or one or more segments may be involved."],
   ar=["يحدث الانخماص الامتصاصي عندما يمنع **انسداد** وصول الهواء إلى المجاري الهوائية البعيدة.",
       "فيُ**متصّ** الهواء الموجود أصلًا تدريجيًا، ثم يتبعه انهيار الأسناخ.",
       "وبحسب مستوى انسداد المجرى الهوائي، قد تصاب رئة كاملة، أو فص كامل، أو قطعة واحدة أو أكثر."])],
   figure=dict(src="assets/resorption.jpg", en="Resorption", ar="امتصاصي")),
 C(["The most common cause of resorption collapse is **obstruction of a bronchus by a mucous or mucopurulent plug**.",
    "This frequently occurs **postoperatively** but also may complicate bronchial asthma, bronchiectasis, chronic bronchitis, tumor, or **foreign body aspiration, particularly in children**."],
   ["السبب الأكثر شيوعًا للانهيار الامتصاصي هو **انسداد قصبة بسدادة مخاطية أو مخاطية قيحية**.",
    "ويحدث هذا كثيرًا **بعد العمليات الجراحية**، ولكنه قد يكون أيضًا من مضاعفات الربو القصبي، وتوسّع القصبات، والتهاب القصبات المزمن، والأورام، أو **استنشاق جسم غريب، ولا سيما عند الأطفال**."]),

 dict(t="side", blocks=[dict(t="group", title_en="2- Compression atelectasis", title_ar="2- الانخماص الانضغاطي",
   en=["Compression atelectasis (some-times called **passive** or **relaxation** atelectasis) is usually associated with accumulation of **fluid, blood, or air within the pleural cavity**, which mechanically collapses the adjacent lung.",
       "This is a frequent occurrence with **pleural effusion**, caused most commonly by **congestive heart failure (CHF)**."],
   ar=["الانخماص الانضغاطي (ويُسمّى أحيانًا الانخماص **المنفعل** أو **الارتخائي**) يرتبط عادةً بتجمّع **سائل أو دم أو هواء داخل التجويف الجنبي**، فيُسبّب انهيارًا ميكانيكيًا للرئة المجاورة.",
       "ويحدث هذا كثيرًا مع **الانصباب الجنبي** (`pleural effusion`)، الناجم في الغالب عن **عجز القلب الاحتقاني** (`CHF`)."])],
   figure=dict(src="assets/compression.jpg", en="Compression", ar="انضغاطي")),
 C(["Leakage of air into the pleural cavity (**pneumothorax**) also leads to compression atelectasis.",
    "**Basal atelectasis** resulting from the elevated position of the diaphragm commonly occurs in **bedridden patients**, in patients with **ascites**, and **during and after surgery**."],
   ["كما يؤدي تسرّب الهواء إلى التجويف الجنبي (**استرواح الصدر** `pneumothorax`) إلى الانخماص الانضغاطي.",
    "ويحدث **الانخماص القاعدي** الناتج عن ارتفاع موضع الحجاب الحاجز عادةً عند **المرضى طريحي الفراش**، والمصابين بـ**الحبن** (`ascites`)، و**أثناء الجراحة وبعدها**."]),

 dict(t="side", blocks=[dict(t="group", title_en="3- Contraction atelectasis", title_ar="3- الانخماص التقلّصي",
   en="Contraction (or **cicatrization**) atelectasis occurs when either local or generalized **fibrotic changes** in the lung or pleura hamper expansion and increase elastic recoil during expiration.",
   ar="يحدث الانخماص التقلّصي (أو **التندّبي** `cicatrization`) عندما تعيق **تغيّرات تليّفية** موضعية أو معمّمة في الرئة أو الجنبة التمدّدَ، وتزيد الارتداد المرن أثناء الزفير.")],
   figure=dict(src="assets/contraction.jpg", en="Contraction", ar="تقلّصي")),
 N("Atelectasis (**except when caused by contraction**) is **potentially reversible** and should be treated promptly to prevent **hypoxemia** and **superimposed infection** of the collapsed lung.",
   "انخماص الرئة (**إلا إذا كان سببه التقلّص**) **قابل للعكس** في الغالب، ويجب علاجه بسرعة لمنع **نقص أكسجة الدم** و**العدوى المُضافة** في الرئة المنهارة.",
   label=["Important", "مهم"]),

 SEC("Acute lung injury", "إصابة الرئة الحادة"),
 C("The term **acute lung injury** encompasses a spectrum of **bilateral pulmonary damage** (endothelial and epithelial), which can be initiated by numerous conditions.",
   "يشمل مصطلح **إصابة الرئة الحادة** (`acute lung injury`) طيفًا من **الأذى الرئوي الثنائي الجانب** (البطاني والظهاري)، الذي يمكن أن تبدأه حالات عديدة."),
 C("**Clinically, acute lung injury manifests as**", "**سريريًا، تظهر إصابة الرئة الحادة بـ**",
   list_en=["Acute onset of **dyspnea**,", "Decreased arterial oxygen pressure (**hypoxemia**),",
            "Development of **bilateral pulmonary infiltrates** on the chest radiograph, all in the absence of clinical evidence of primary left-sided heart failure."],
   list_ar=["بداية حادة لـ**ضيق التنفس**،", "انخفاض ضغط الأوكسجين الشرياني (**نقص أكسجة الدم**)،",
            "ظهور **ارتشاحات رئوية ثنائية الجانب** في صورة الصدر الشعاعية، وكل ذلك مع غياب الدليل السريري على عجز القلب الأيسر الأولي."]),
 C("Since the pulmonary infiltrates in acute lung injury are usually caused by **damage to the alveolar capillary membrane**, rather than by left-sided heart failure , such accumulations constitute an example of **non-cardiogenic pulmonary edema**.",
   "لأن الارتشاحات الرئوية في إصابة الرئة الحادة تنتج عادةً عن **تضرّر الغشاء الشعري السنخي** وليس عن عجز القلب الأيسر، فإن هذه التجمّعات تمثّل مثالًا على **الوذمة الرئوية غير القلبية المنشأ**."),
 C("Acute lung injury can progress to the more severe **acute respiratory distress syndrome**.",
   "ويمكن أن تتطوّر إصابة الرئة الحادة إلى الحالة الأشد: **متلازمة الضائقة التنفسية الحادة**."),
 F("acute-lung-injury.jpg", "Normal alveolus (left) compared with the injured alveolus in acute lung injury (right)", "السنخ الطبيعي (يسارًا) مقارنةً بالسنخ المتضرّر في إصابة الرئة الحادة (يمينًا)", h="62mm"),

 SEC("Acute Respiratory Distress Syndrome", "متلازمة الضائقة التنفسية الحادة"),
 F("ards.jpg", "Acute Respiratory Distress Syndrome (ARDS)", "متلازمة الضائقة التنفسية الحادة (`ARDS`)", h="52mm", fit="contain"),
 C("**Acute respiratory distress syndrome (ARDS)** is a clinical syndrome caused by **diffuse alveolar capillary and epithelial damage**. The usual course is characterized by;",
   "**متلازمة الضائقة التنفسية الحادة** (`ARDS`) متلازمة سريرية سببها **تضرّر منتشر في الشعيرات والظهارة السنخية**. ويتميّز سيرها المعتاد بـ؛",
   list_en=["Rapid onset of life-threatening respiratory insufficiency", "Cyanosis.",
            "Severe arterial hypoxemia that is **refractory to oxygen therapy** and may progress to **multisystem organ failure**."],
   list_ar=["بداية سريعة لقصور تنفسي مهدِّد للحياة", "الزُّراق (`Cyanosis`).",
            "نقص شديد في أكسجة الدم الشرياني **لا يستجيب للعلاج بالأوكسجين**، وقد يتطوّر إلى **فشل أعضاء متعددة**."]),
 C(["The histologic manifestation of ARDS in the lungs is known as **diffuse alveolar damage(DAD)**.",
    "ARDS can occur in a multitude of clinical settings and is associated with either **direct injury** to the lung or **indirect injury** in the setting of a systemic process."],
   ["يُعرف المظهر النسيجي لـ`ARDS` في الرئتين بـ**الأذى السنخي المنتشر** (`DAD`).",
    "ويمكن أن تحدث `ARDS` في حالات سريرية كثيرة، وترتبط إما بـ**أذى مباشر** للرئة أو **أذى غير مباشر** ضمن عملية جهازية."]),
 H2("Table 12-1 Clinical Disorders Associated with the Development of Acute Lung Injury/Acute Respiratory Distress Syndrome",
    "جدول `12-1` الاضطرابات السريرية المرتبطة بحدوث إصابة الرئة الحادة / متلازمة الضائقة التنفسية الحادة"),
 dict(t="table", head=["Direct Lung Injury", "الأذى الرئوي المباشر", "Indirect Lung Injury", "الأذى الرئوي غير المباشر"],
      ar_cols=[1, 3], key_cols=[0, 2],
      rows=[["^^Common Causes^^", "^^أسباب شائعة^^", "", ""],
            ["Pneumonia", "ذات الرئة", "Sepsis", "الإنتان"],
            ["Aspiration of gastric contents", "استنشاق محتويات المعدة", "Severe trauma with shock", "رضّ شديد مع صدمة"],
            ["^^Uncommon Causes^^", "^^أسباب غير شائعة^^", "", ""],
            ["Pulmonary contusion", "كدمة رئوية", "Cardiopulmonary bypass", "المجازة القلبية الرئوية"],
            ["Fat embolism", "الانصمام الدهني", "Acute pancreatitis", "التهاب البنكرياس الحاد"],
            ["Near-drowning", "شبه الغرق", "Drug overdose", "جرعة دوائية مفرطة"],
            ["Inhalational injury", "أذى الاستنشاق", "Transfusion of blood products", "نقل منتجات الدم"],
            ["Reperfusion injury after lung transplantation", "أذى إعادة التروية بعد زرع الرئة", "Uremia", "اليوريمية"]]),
 N("It should be recalled that **respiratory distress syndrome of the new born** is pathogenetically distinct; it is caused by a **primary deficiency of surfactant**.",
   "ينبغي التذكّر أن **متلازمة الضائقة التنفسية عند حديثي الولادة** مختلفة من حيث الإمراض؛ إذ سببها **نقص أولي في المادة الفاعلة بالسطح** (`surfactant`).",
   label=["Remember", "تذكّر"]),

 SEC("Clinical Features", "المظاهر السريرية"),
 C("Approximately **85%** of patients develop the clinical syndrome of acute lung injury or ARDS **within 72 hours** of the initiating insult.",
   "يصاب نحو **85%** من المرضى بالمتلازمة السريرية لإصابة الرئة الحادة أو `ARDS` **خلال 72 ساعة** من الأذى المُحدِث."),
 C("With improvements in supportive therapy, the mortality rate for the 190,000 ARDS cases occurring yearly has decreased **from 60% to 40%** in the last decade.",
   "ومع تحسّن العلاج الداعم، انخفض معدل الوفيات لحالات `ARDS` البالغة 190,000 حالة سنويًا **من 60% إلى 40%** في العقد الأخير."),
 C("**Predictors of poor prognosis include**", "**من مؤشّرات سوء الإنذار**",
   list_en=["Advanced age,", "Underlying bacteremia (sepsis),", "The development of multisystem (especially cardiac, renal, or hepatic) failure."],
   list_ar=["التقدّم في العمر،", "تجرثم الدم الكامن (الإنتان)،", "حدوث فشل أجهزة متعددة (ولا سيما القلب أو الكلية أو الكبد)."]),
 C("However, in most patients who survive the acute insult and are spared the chronic sequelae, normal respiratory function returns **within 6 to 12 months**.",
   "ومع ذلك، فإن معظم المرضى الذين ينجون من الأذى الحاد ويسلمون من العواقب المزمنة تعود لديهم الوظيفة التنفسية الطبيعية **خلال 6 إلى 12 شهرًا**."),

 SEC("Emphysema", "النُّفاخ الرئوي"),
 C("**Emphysema** is characterized by **abnormal permanent enlargement of the air spaces distal to the terminal bronchioles**, accompanied by **destruction of their wall** **without significant fibrosis**.",
   "يتميّز **النُّفاخ** (`Emphysema`) بـ**تضخّم دائم غير طبيعي في الفراغات الهوائية البعيدة عن القصيبات الانتهائية**، مصحوبًا بـ**تخرّب جدرانها** **من دون تليّف ملحوظ**."),

 SEC("Types of Emphysema", "أنواع النُّفاخ"),
 C(["Emphysema is classified according to its **anatomic distribution within the lobule**, the **acinus** is the structure distal to terminal bronchioles, and a cluster of **three to five acini** is called a **lobule**."],
   ["يُصنَّف النُّفاخ بحسب **توزيعه التشريحي داخل الفُصيص**؛ و**العُنيبة** (`acinus`) هي البنية الواقعة بعد القصيبات الانتهائية، ومجموعة من **ثلاث إلى خمس عُنيبات** تُسمّى **فُصيصًا** (`lobule`)."]),
 C("**There are four major types of emphysema:**", "**هناك أربعة أنواع رئيسة للنُّفاخ:**",
   list_en=["Centri-acinar,", "Pan-acinar,", "Distal acinar, and", "Irregular."],
   list_ar=["مركزي العُنيبة،", "شامل العُنيبة،", "قاصي العُنيبة، و", "غير منتظم."]),
 C("Only the **first two types** cause clinically significant airway obstruction, with **centriacinar** emphysema being about **20 times more common** than panacinar disease.",
   "**النوعان الأولان فقط** يسبّبان انسدادًا ذا أهمية سريرية في المجاري الهوائية، والنُّفاخ **مركزي العُنيبة** أكثر شيوعًا بنحو **20 مرة** من النوع شامل العُنيبة."),
 dict(t="figures", items=[
   dict(src="assets/emphysema-patterns.jpg", en="Major patterns of emphysema: A, normal acinus; B, centriacinar; C, panacinar", ar="الأنماط الرئيسة للنُّفاخ: A العُنيبة الطبيعية، B مركزي العُنيبة، C شامل العُنيبة", h="74mm", fit="contain"),
   dict(src="assets/alveolar-sac.jpg", en="Respiratory bronchiole, alveolar duct and alveolar sac", ar="القصيبة التنفسية والقناة السنخية والكيس السنخي", h="74mm", fit="contain")]),

 SEC("Clinical Features", "المظاهر السريرية"),
 R("**Dyspnea** usually is the **first symptom**; it begins insidiously but is steadily progressive.",
   "**ضيق التنفس** هو عادةً **العرض الأول**؛ يبدأ خفيًا لكنه يتقدّم باطّراد."),
 R("In patients with underlying chronic bronchitis or chronic asthmatic bronchitis, **cough and wheezing** may be the initial complaints.",
   "عند المرضى المصابين أصلًا بالتهاب القصبات المزمن أو التهاب القصبات الربوي المزمن، قد يكون **السعال والأزيز** هما الشكويين الأوليين."),
 R("**Weight loss** is common and may be so severe as to suggest a hidden malignant tumor.",
   "**فقدان الوزن** شائع، وقد يكون شديدًا إلى حدّ يوحي بوجود ورم خبيث مخفي."),
 R(["Pulmonary function tests reveal **reduced FEV1**(Forced expiratory volume in 1 second )with **normal or near-normal FVC**(Forced Vital Capacity).",
    "Hence, the **ratio of FEV1to FVC is reduced**."],
   ["تكشف اختبارات وظائف الرئة عن **انخفاض** `FEV1` (حجم الزفير القسري في الثانية الأولى) مع **سعة حيوية قسرية** `FVC` **طبيعية أو قريبة من الطبيعية**.",
    "ولذلك **تنخفض نسبة** `FEV1` **إلى** `FVC`."]),
]

def Q(en, ar, opts, ans, **k):
    return dict(en=en, ar=ar, options=[list(o) for o in opts], answer=ans, **k)

mcq = [
 {"topic_en": "Lung structure", "topic_ar": "تركيب الرئة"},
 Q("The right lung has how many lobes?", "كم فصًّا في الرئة اليمنى؟", [("Two", "اثنان"), ("Three", "ثلاثة"), ("Four", "أربعة"), ("Five", "خمسة")], "b"),
 Q("Type I pneumocytes cover about what percentage of the alveolar surface?", "تغطي الخلايا الرئوية من النوع الأول نحو أي نسبة من سطح الأسناخ؟", [("50%", "50%"), ("75%", "75%"), ("85%", "85%"), ("95%", "95%")], "d"),
 Q("Which cells synthesize pulmonary surfactant?", "أي الخلايا تصنع المادة الفاعلة بالسطح الرئوية؟", [("Type II pneumocytes", "الخلايا الرئوية من النوع الثاني"), ("Type I pneumocytes", "الخلايا الرئوية من النوع الأول"), ("Alveolar macrophages", "البلاعم السنخية"), ("Mast cells", "الخلايا البدينة")], "a"),
 Q("The main cell type involved in repair of alveolar epithelium after damage to type I pneumocytes is:", "النوع الرئيس من الخلايا المسؤول عن إصلاح ظهارة الأسناخ بعد تضرّر خلايا النوع الأول هو:", [("Fibroblast-like cells", "الخلايا الشبيهة بالأرومات الليفية"), ("Endothelial cells", "خلايا البطانة"), ("Type II pneumocytes", "الخلايا الرئوية من النوع الثاني"), ("Alveolar macrophages", "البلاعم السنخية")], "c"),
 Q("The pores that permit passage of air, bacteria and exudates between adjacent alveoli are:", "المسامات التي تسمح بمرور الهواء والبكتريا والنضحات بين الأسناخ المتجاورة هي:", [("Pores of Kohn", "مسامات كون"), ("Canals of Lambert", "قنوات لامبرت"), ("Stomata", "الثغور"), ("Fenestrae", "النوافذ")], "a"),
 Q("In the adult, alveolar macrophages often contain phagocytosed:", "في البالغ، غالبًا ما تحتوي البلاعم السنخية على مبلوعات من:", [("Iron particles", "دقائق الحديد"), ("Carbon particles", "دقائق الكاربون"), ("Bacteria only", "البكتريا فقط"), ("Surfactant", "المادة الفاعلة بالسطح")], "b"),
 Q("Primary lung diseases are broadly divided into those affecting all of the following EXCEPT:", "تُقسَّم أمراض الرئة الأولية إلى ما يصيب كل مما يأتي عدا:", [("The airways", "المجاري الهوائية"), ("The interstitium", "النسيج الخلالي"), ("The pleura only", "الجنبة فقط"), ("The pulmonary vascular system", "الجهاز الوعائي الرئوي")], "c"),
 {"topic_en": "Atelectasis", "topic_ar": "انخماص الرئة"},
 Q("Atelectasis is best defined as:", "أفضل تعريف لانخماص الرئة هو:", [("Permanent enlargement of air spaces", "تضخّم دائم في الفراغات الهوائية"), ("Loss of lung volume caused by inadequate expansion of air spaces", "فقدان حجم الرئة بسبب عدم كفاية تمدّد الفراغات الهوائية"), ("Accumulation of fluid in the alveoli", "تجمّع السائل في الأسناخ"), ("Inflammation of the bronchi", "التهاب القصبات")], "b"),
 Q("Atelectasis gives rise to hypoxia mainly through:", "يؤدي انخماص الرئة إلى نقص الأكسجة أساسًا عن طريق:", [("Ventilation-perfusion imbalance", "عدم توازن التهوية والتروية"), ("Increased surfactant", "زيادة المادة الفاعلة بالسطح"), ("Increased FVC", "زيادة السعة الحيوية القسرية"), ("Pulmonary fibrosis", "تليّف الرئة")], "a"),
 Q("The most common cause of resorption collapse is:", "السبب الأكثر شيوعًا للانهيار الامتصاصي هو:", [("Pleural effusion", "الانصباب الجنبي"), ("Pneumothorax", "استرواح الصدر"), ("Obstruction of a bronchus by a mucous or mucopurulent plug", "انسداد قصبة بسدادة مخاطية أو مخاطية قيحية"), ("Pulmonary fibrosis", "تليّف الرئة")], "c"),
 Q("Foreign body aspiration, particularly in children, causes which form of atelectasis?", "استنشاق جسم غريب، ولا سيما عند الأطفال، يسبّب أي شكل من الانخماص؟", [("Compression", "الانضغاطي"), ("Contraction", "التقلّصي"), ("Basal", "القاعدي"), ("Resorption", "الامتصاصي")], "d"),
 Q("Compression atelectasis is also called:", "يُسمّى الانخماص الانضغاطي أيضًا:", [("Cicatrization atelectasis", "الانخماص التندّبي"), ("Passive or relaxation atelectasis", "الانخماص المنفعل أو الارتخائي"), ("Obstructive atelectasis", "الانخماص الانسدادي"), ("Absorption atelectasis", "الانخماص الامتصاصي")], "b"),
 Q("Pleural effusion causing compression atelectasis is most commonly due to:", "الانصباب الجنبي المسبّب للانخماص الانضغاطي يكون غالبًا بسبب:", [("Pneumonia", "ذات الرئة"), ("Tumor", "ورم"), ("Asthma", "الربو"), ("Congestive heart failure (CHF)", "عجز القلب الاحتقاني")], "d"),
 Q("Leakage of air into the pleural cavity (pneumothorax) leads to:", "تسرّب الهواء إلى التجويف الجنبي (استرواح الصدر) يؤدي إلى:", [("Compression atelectasis", "الانخماص الانضغاطي"), ("Resorption atelectasis", "الانخماص الامتصاصي"), ("Contraction atelectasis", "الانخماص التقلّصي"), ("Emphysema", "النُّفاخ")], "a"),
 Q("Contraction atelectasis is also called:", "يُسمّى الانخماص التقلّصي أيضًا:", [("Relaxation atelectasis", "الانخماص الارتخائي"), ("Passive atelectasis", "الانخماص المنفعل"), ("Cicatrization atelectasis", "الانخماص التندّبي"), ("Basal atelectasis", "الانخماص القاعدي")], "c"),
 Q("Which form of atelectasis is NOT potentially reversible?", "أي شكل من الانخماص غير قابل للعكس؟", [("Resorption", "الامتصاصي"), ("Compression", "الانضغاطي"), ("Basal", "القاعدي"), ("Contraction", "التقلّصي")], "d"),
 {"topic_en": "Acute lung injury and ARDS", "topic_ar": "إصابة الرئة الحادة ومتلازمة الضائقة التنفسية"},
 Q("Clinically, acute lung injury manifests by all of the following EXCEPT:", "سريريًا، تظهر إصابة الرئة الحادة بكل مما يأتي عدا:", [("Acute onset of dyspnea", "بداية حادة لضيق التنفس"), ("Hypoxemia", "نقص أكسجة الدم"), ("Primary left-sided heart failure", "عجز القلب الأيسر الأولي"), ("Bilateral pulmonary infiltrates", "ارتشاحات رئوية ثنائية الجانب")], "c"),
 Q("The pulmonary infiltrates of acute lung injury are an example of:", "الارتشاحات الرئوية في إصابة الرئة الحادة مثال على:", [("Cardiogenic pulmonary edema", "الوذمة الرئوية القلبية المنشأ"), ("Non-cardiogenic pulmonary edema", "الوذمة الرئوية غير القلبية المنشأ"), ("Emphysema", "النُّفاخ"), ("Pleural effusion", "الانصباب الجنبي")], "b"),
 Q("The histologic manifestation of ARDS in the lungs is known as:", "يُعرف المظهر النسيجي لـ ARDS في الرئتين بـ:", [("Diffuse alveolar damage (DAD)", "الأذى السنخي المنتشر"), ("Bronchiolitis obliterans", "التهاب القصيبات المسدّ"), ("Centriacinar emphysema", "النُّفاخ مركزي العُنيبة"), ("Pores of Kohn", "مسامات كون")], "a"),
 Q("The arterial hypoxemia of ARDS is:", "نقص أكسجة الدم الشرياني في ARDS:", [("Mild and transient", "خفيف وعابر"), ("Corrected easily by oxygen", "يُصحَّح بسهولة بالأوكسجين"), ("Refractory to oxygen therapy", "لا يستجيب للعلاج بالأوكسجين"), ("Absent", "غائب")], "c"),
 Q("Respiratory distress syndrome of the newborn is caused by:", "متلازمة الضائقة التنفسية عند حديثي الولادة سببها:", [("Sepsis", "الإنتان"), ("Aspiration of gastric contents", "استنشاق محتويات المعدة"), ("Primary deficiency of surfactant", "نقص أولي في المادة الفاعلة بالسطح"), ("Pneumothorax", "استرواح الصدر")], "c"),
 Q("Which is a common cause of DIRECT lung injury leading to ARDS?", "أي مما يأتي سبب شائع للأذى الرئوي المباشر المؤدي إلى ARDS؟", [("Sepsis", "الإنتان"), ("Pneumonia", "ذات الرئة"), ("Acute pancreatitis", "التهاب البنكرياس الحاد"), ("Uremia", "اليوريمية")], "b"),
 Q("Which is a common cause of INDIRECT lung injury leading to ARDS?", "أي مما يأتي سبب شائع للأذى الرئوي غير المباشر المؤدي إلى ARDS؟", [("Sepsis", "الإنتان"), ("Fat embolism", "الانصمام الدهني"), ("Near-drowning", "شبه الغرق"), ("Pulmonary contusion", "كدمة رئوية")], "a"),
 Q("Approximately 85% of patients develop acute lung injury or ARDS within:", "يصاب نحو 85% من المرضى بإصابة الرئة الحادة أو ARDS خلال:", [("24 hours", "24 ساعة"), ("72 hours", "72 ساعة"), ("1 week", "أسبوع"), ("1 month", "شهر")], "b"),
 Q("With improved supportive therapy, ARDS mortality has decreased:", "مع تحسّن العلاج الداعم انخفضت وفيات ARDS:", [("From 60% to 40%", "من 60% إلى 40%"), ("From 85% to 60%", "من 85% إلى 60%"), ("From 40% to 20%", "من 40% إلى 20%"), ("From 95% to 85%", "من 95% إلى 85%")], "a"),
 Q("All are predictors of poor prognosis in ARDS EXCEPT:", "كل مما يأتي من مؤشّرات سوء الإنذار في ARDS عدا:", [("Advanced age", "التقدّم في العمر"), ("Underlying bacteremia (sepsis)", "تجرثم الدم (الإنتان)"), ("Multisystem failure", "فشل أجهزة متعددة"), ("Young age", "صغر العمر")], "d"),
 Q("In most survivors of ARDS, normal respiratory function returns within:", "عند معظم الناجين من ARDS تعود الوظيفة التنفسية الطبيعية خلال:", [("1 to 2 weeks", "1 إلى 2 أسبوع"), ("1 to 3 months", "1 إلى 3 أشهر"), ("6 to 12 months", "6 إلى 12 شهرًا"), ("5 years", "5 سنوات")], "c"),
 {"topic_en": "Emphysema", "topic_ar": "النُّفاخ"},
 Q("Emphysema is characterized by permanent enlargement of air spaces distal to the terminal bronchioles with wall destruction:", "يتميّز النُّفاخ بتضخّم دائم في الفراغات الهوائية بعد القصيبات الانتهائية مع تخرّب الجدار:", [("With marked fibrosis", "مع تليّف واضح"), ("Without significant fibrosis", "من دون تليّف ملحوظ"), ("With granulomas", "مع أورام حبيبية"), ("With mucus plugs only", "مع سدادات مخاطية فقط")], "b"),
 Q("A cluster of three to five acini is called a:", "مجموعة من ثلاث إلى خمس عُنيبات تُسمّى:", [("Lobe", "فصًّا"), ("Segment", "قطعة"), ("Lobule", "فُصيصًا"), ("Alveolar sac", "كيسًا سنخيًا")], "c"),
 Q("Which type of emphysema is about 20 times more common than panacinar?", "أي نوع من النُّفاخ أكثر شيوعًا بنحو 20 مرة من النوع شامل العُنيبة؟", [("Distal acinar", "قاصي العُنيبة"), ("Irregular", "غير المنتظم"), ("Paraseptal", "جانب الحاجز"), ("Centriacinar", "مركزي العُنيبة")], "d"),
 Q("The usual first symptom of emphysema is:", "العرض الأول المعتاد للنُّفاخ هو:", [("Dyspnea", "ضيق التنفس"), ("Weight loss", "فقدان الوزن"), ("Cyanosis", "الزُّراق"), ("Hemoptysis", "نفث الدم")], "a"),
 Q("Pulmonary function tests in emphysema show:", "تُظهر اختبارات وظائف الرئة في النُّفاخ:", [("Increased FEV1 and reduced FVC", "زيادة FEV1 ونقص FVC"), ("Normal FEV1/FVC ratio", "نسبة FEV1/FVC طبيعية"), ("Reduced FEV1 with normal or near-normal FVC", "نقص FEV1 مع FVC طبيعية أو قريبة منها"), ("Reduced FVC only", "نقص FVC فقط")], "c"),
 {"topic_en": "Picture questions", "topic_ar": "أسئلة الصور"},
 Q("The cell labelled “Type II pneumocyte” in this figure is responsible for:", "الخلية المؤشَّرة “Type II pneumocyte” في هذا الشكل مسؤولة عن:", [("Covering 95% of the alveolar surface", "تغطية 95% من سطح الأسناخ"), ("Synthesizing surfactant and repairing alveolar epithelium", "صنع المادة الفاعلة بالسطح وإصلاح ظهارة الأسناخ"), ("Phagocytosis of carbon particles", "بلعمة دقائق الكاربون"), ("Gas exchange only", "تبادل الغازات فقط")], "b", img="assets/alveolar-wall.jpg", img_h="44mm"),
 Q("The black area in this figure (fluid in the pleural cavity) shows which form of atelectasis?", "المنطقة السوداء في هذا الشكل (سائل في التجويف الجنبي) تمثّل أي شكل من الانخماص؟", [("Resorption", "الامتصاصي"), ("Contraction", "التقلّصي"), ("Compression", "الانضغاطي"), ("Emphysema", "النُّفاخ")], "c", img="assets/compression.jpg", img_h="36mm"),
 Q("The figure shows a plug in a bronchus with collapse of the distal lung. This is:", "يُظهر الشكل سدادة في قصبة مع انهيار الرئة البعيدة. هذا هو:", [("Resorption atelectasis", "الانخماص الامتصاصي"), ("Compression atelectasis", "الانخماص الانضغاطي"), ("Contraction atelectasis", "الانخماص التقلّصي"), ("Pneumothorax", "استرواح الصدر")], "a", img="assets/resorption.jpg", img_h="36mm"),
 Q("The shrunken, scarred lung in this figure represents which form?", "الرئة المنكمشة المتندّبة في هذا الشكل تمثّل أي شكل؟", [("Compression", "الانضغاطي"), ("Resorption", "الامتصاصي"), ("Basal", "القاعدي"), ("Contraction (cicatrization)", "التقلّصي (التندّبي)")], "d", img="assets/contraction.jpg", img_h="40mm"),
 Q("The right half of this figure (sloughed epithelium, edema fluid, hyaline membrane) represents:", "النصف الأيمن من هذا الشكل (ظهارة متقشّرة، سائل وذمي، غشاء زجاجي) يمثّل:", [("Normal alveolus", "سنخًا طبيعيًا"), ("Acute lung injury", "إصابة الرئة الحادة"), ("Emphysema", "النُّفاخ"), ("Chronic bronchitis", "التهاب القصبات المزمن")], "b", img="assets/acute-lung-injury.jpg", img_h="46mm"),
 Q("In this figure, panel B (dilation that initially affects the respiratory bronchioles) is:", "في هذا الشكل، اللوحة B (توسّع يصيب القصيبات التنفسية أولًا) هي:", [("Panacinar emphysema", "النُّفاخ شامل العُنيبة"), ("Normal acinus", "عُنيبة طبيعية"), ("Centriacinar emphysema", "النُّفاخ مركزي العُنيبة"), ("Irregular emphysema", "النُّفاخ غير المنتظم")], "c", img="assets/emphysema-patterns.jpg", img_h="46mm"),
]

tf = [
 dict(en="The left lung has three lobes.", ar="في الرئة اليسرى ثلاثة فصوص.", answer="F"),
 dict(en="Type I pneumocytes cover 95% of the alveolar surface.", ar="تغطي الخلايا الرئوية من النوع الأول 95% من سطح الأسناخ.", answer="T"),
 dict(en="Type I pneumocytes synthesize pulmonary surfactant.", ar="تصنع الخلايا الرئوية من النوع الأول المادة الفاعلة بالسطح.", answer="F"),
 dict(en="The alveolar walls are solid and not perforated.", ar="جدران الأسناخ مصمتة وغير مثقّبة.", answer="F"),
 dict(en="Atelectasis causes a ventilation-perfusion imbalance and hypoxia.", ar="يسبّب انخماص الرئة عدم توازن التهوية والتروية ونقص الأكسجة.", answer="T"),
 dict(en="Resorption atelectasis frequently occurs postoperatively.", ar="يحدث الانخماص الامتصاصي كثيرًا بعد العمليات الجراحية.", answer="T"),
 dict(en="Basal atelectasis results from a lowered position of the diaphragm.", ar="ينتج الانخماص القاعدي عن انخفاض موضع الحجاب الحاجز.", answer="F"),
 dict(en="Contraction atelectasis is potentially reversible.", ar="الانخماص التقلّصي قابل للعكس.", answer="F"),
 dict(en="Acute lung injury involves bilateral endothelial and epithelial damage.", ar="تتضمّن إصابة الرئة الحادة أذى بطانيًا وظهاريًا ثنائي الجانب.", answer="T"),
 dict(en="Acute lung injury can progress to ARDS.", ar="يمكن أن تتطوّر إصابة الرئة الحادة إلى ARDS.", answer="T"),
 dict(en="Respiratory distress syndrome of the newborn has the same pathogenesis as adult ARDS.", ar="لمتلازمة الضائقة التنفسية عند حديثي الولادة الإمراض نفسه لـ ARDS عند البالغين.", answer="F"),
 dict(en="Emphysema is accompanied by significant fibrosis.", ar="يرافق النُّفاخَ تليّفٌ ملحوظ.", answer="F"),
 dict(en="Only centriacinar and panacinar emphysema cause clinically significant airway obstruction.", ar="النُّفاخ مركزي العُنيبة وشامل العُنيبة فقط يسبّبان انسدادًا ذا أهمية سريرية.", answer="T"),
 dict(en="In emphysema the ratio of FEV1 to FVC is reduced.", ar="في النُّفاخ تنخفض نسبة FEV1 إلى FVC.", answer="T"),
]

traps = [
 dict(en="Type I vs type II pneumocytes", ar="الخلايا الرئوية من النوع الأول مقابل الثاني",
      answer_en="Type I: flattened, platelike, cover 95% of the surface. Type II: rounded, synthesize surfactant and repair the epithelium.",
      answer_ar="النوع الأول: مسطّحة صفيحية تغطي 95% من السطح. النوع الثاني: مستديرة، تصنع المادة الفاعلة بالسطح وتصلح الظهارة."),
 dict(en="Compression atelectasis — other names", ar="الانخماص الانضغاطي — أسماؤه الأخرى",
      answer_en="Passive or relaxation atelectasis. Cicatrization is the other name of contraction atelectasis.",
      answer_ar="الانخماص المنفعل أو الارتخائي. أما التندّبي فهو اسم الانخماص التقلّصي."),
 dict(en="Which atelectasis is not reversible?", ar="أي انخماص غير قابل للعكس؟",
      answer_en="Contraction (cicatrization) atelectasis — because it is due to fibrosis. The others are potentially reversible.",
      answer_ar="الانخماص التقلّصي (التندّبي) — لأن سببه التليّف. أما البقية فقابلة للعكس."),
 dict(en="Acute lung injury edema — cardiogenic or not?", ar="وذمة إصابة الرئة الحادة — قلبية المنشأ أم لا؟",
      answer_en="Non-cardiogenic: caused by damage to the alveolar capillary membrane, not by left-sided heart failure.",
      answer_ar="غير قلبية المنشأ: سببها تضرّر الغشاء الشعري السنخي، لا عجز القلب الأيسر."),
 dict(en="Newborn RDS vs adult ARDS", ar="متلازمة الضائقة عند حديثي الولادة مقابل ARDS",
      answer_en="Newborn RDS is caused by a primary deficiency of surfactant; ARDS by diffuse alveolar capillary and epithelial damage.",
      answer_ar="متلازمة حديثي الولادة سببها نقص أولي في المادة الفاعلة بالسطح؛ أما ARDS فسببها تضرّر منتشر في الشعيرات والظهارة السنخية."),
 dict(en="Acinus vs lobule", ar="العُنيبة مقابل الفُصيص",
      answer_en="Acinus: the structure distal to terminal bronchioles. Lobule: a cluster of three to five acini.",
      answer_ar="العُنيبة: البنية بعد القصيبات الانتهائية. الفُصيص: مجموعة من ثلاث إلى خمس عُنيبات."),
 dict(en="FEV1 and FVC in emphysema", ar="FEV1 وFVC في النُّفاخ",
      answer_en="FEV1 is reduced, FVC is normal or near-normal, so the FEV1/FVC ratio is reduced.",
      answer_ar="ينخفض FEV1 وتبقى FVC طبيعية أو قريبة منها، فتنخفض نسبة FEV1/FVC."),
]

important = [
 dict(en="List the components of the alveolar wall from blood to air.", ar="عدّد مكوّنات جدار السنخ من الدم إلى الهواء.",
      answer_en="(1) Capillary endothelium and basement membrane; (2) pulmonary interstitium; (3) alveolar epithelium (type I and type II pneumocytes); (4) a few free alveolar macrophages.",
      answer_ar="(1) بطانة الشعيرات والغشاء القاعدي؛ (2) النسيج الخلالي الرئوي؛ (3) ظهارة الأسناخ (الخلايا الرئوية من النوع الأول والثاني)؛ (4) بضع بلاعم سنخية حرّة."),
 dict(en="Define atelectasis and explain how it causes hypoxia.", ar="عرّف انخماص الرئة ووضّح كيف يسبّب نقص الأكسجة.",
      answer_en="Loss of lung volume caused by inadequate expansion of air spaces. Poorly oxygenated blood is shunted from pulmonary arteries into veins, giving a ventilation-perfusion imbalance and hypoxia.",
      answer_ar="فقدان حجم الرئة بسبب عدم كفاية تمدّد الفراغات الهوائية. يتحوّل الدم ضعيف الأكسجة من الشرايين الرئوية إلى الأوردة، فيحدث عدم توازن التهوية والتروية ونقص الأكسجة."),
 dict(en="Compare the three forms of atelectasis.", ar="قارن بين أشكال انخماص الرئة الثلاثة.",
      answer_en="Resorption: obstruction (mucous plug) — air absorbed distally. Compression: fluid, blood or air in the pleural cavity (effusion from CHF, pneumothorax, basal). Contraction: local or generalized fibrosis hampers expansion — not reversible.",
      answer_ar="الامتصاصي: انسداد (سدادة مخاطية) فيُمتصّ الهواء البعيد. الانضغاطي: سائل أو دم أو هواء في التجويف الجنبي (انصباب بسبب عجز القلب، استرواح الصدر، القاعدي). التقلّصي: تليّف موضعي أو معمّم يعيق التمدّد — غير قابل للعكس."),
 dict(en="What are the clinical manifestations of acute lung injury?", ar="ما المظاهر السريرية لإصابة الرئة الحادة؟",
      answer_en="Acute onset of dyspnea, hypoxemia, and bilateral pulmonary infiltrates on chest radiograph, without evidence of primary left-sided heart failure.",
      answer_ar="بداية حادة لضيق التنفس، ونقص أكسجة الدم، وارتشاحات رئوية ثنائية في صورة الصدر، من دون دليل على عجز القلب الأيسر الأولي."),
 dict(en="Define ARDS and give its usual course.", ar="عرّف ARDS واذكر سيرها المعتاد.",
      answer_en="A clinical syndrome caused by diffuse alveolar capillary and epithelial damage: rapid onset of life-threatening respiratory insufficiency, cyanosis, and severe hypoxemia refractory to oxygen that may progress to multisystem organ failure.",
      answer_ar="متلازمة سريرية سببها تضرّر منتشر في الشعيرات والظهارة السنخية: بداية سريعة لقصور تنفسي مهدِّد للحياة، وزُراق، ونقص أكسجة شديد لا يستجيب للأوكسجين وقد يتطوّر إلى فشل أعضاء متعددة."),
 dict(en="List the predictors of poor prognosis in ARDS.", ar="عدّد مؤشّرات سوء الإنذار في ARDS.",
      answer_en="Advanced age, underlying bacteremia (sepsis), and the development of multisystem (especially cardiac, renal or hepatic) failure.",
      answer_ar="التقدّم في العمر، وتجرثم الدم (الإنتان)، وحدوث فشل أجهزة متعددة (ولا سيما القلب أو الكلية أو الكبد)."),
 dict(en="Define emphysema and list its types.", ar="عرّف النُّفاخ وعدّد أنواعه.",
      answer_en="Abnormal permanent enlargement of air spaces distal to the terminal bronchioles with destruction of their wall without significant fibrosis. Types: centriacinar, panacinar, distal acinar, irregular.",
      answer_ar="تضخّم دائم غير طبيعي في الفراغات الهوائية بعد القصيبات الانتهائية مع تخرّب جدرانها من دون تليّف ملحوظ. أنواعه: مركزي العُنيبة، شامل العُنيبة، قاصي العُنيبة، غير المنتظم."),
 dict(en="Write the clinical features of emphysema.", ar="اكتب المظاهر السريرية للنُّفاخ.",
      answer_en="Dyspnea (first, insidious, progressive); cough and wheezing if chronic bronchitis coexists; weight loss; reduced FEV1 with normal FVC so the FEV1/FVC ratio is reduced.",
      answer_ar="ضيق التنفس (أولًا، خفي ومتقدّم)؛ سعال وأزيز عند وجود التهاب قصبات مزمن؛ فقدان الوزن؛ نقص FEV1 مع FVC طبيعية فتنخفض نسبة FEV1/FVC."),
]

data = {"meta": {
  "subject_en": "Pathology", "subject_ar": "علم الأمراض", "short_ar": "أمراض",
  "unit_en": "Lecture 1+2", "unit_ar": "المحاضرتان 1 و2", "unit_label": "LEC", "unit_no": "1+2",
  "title_en": "Atelectasis, ARDS & Emphysema", "title_ar": "انخماص الرئة ومتلازمة الضائقة التنفسية والنُّفاخ",
  "kind": "Theory — نظري", "stage": "The fourth stage — الرابعة", "instructor": "د. حامد خليل التميمي",
  "file_name": "BIOS - أمراض نظري المحاضرة الأولى والثانية"},
 "blocks": blocks, "questions": {"mcq": mcq, "tf": tf, "traps": traps, "important": important}}
qs = [q for q in mcq if "answer" in q]
print(len(qs), Counter(q["answer"] for q in qs))
json.dump(data, open("/home/user/-/pathology-lec1-2-atelectasis/lecture.json", "w"), ensure_ascii=False, indent=1)

```
