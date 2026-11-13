---
source: BIOS-Obsidian/tools/scripts/ha/h4.py
handouts: [nursing-ha-lec4-lung-thorax]
saved: 2026-11-13
tags: [bios, code]
---
# ha/h4.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#nursing-ha-lec4-lung-thorax|nursing-ha-lec4-lung-thorax]]

```python
import sys; sys.path.insert(0, "/tmp/claude-0/-home-user-kwmdkm/44452a28-19bf-5ce8-890a-f6919e775f0b/scratchpad/ha")
from common_ha import *

def STEPS(en, ar, title_en="**Procedure:**", title_ar="**الإجراء:**", **k):
    return L(en, ar, en=title_en, ar=title_ar, **k)
def NF(en, ar):
    return T([B("Normal findings", "النتائج الطبيعية")], [[B(e, a)] for e, a in zip(en, ar)], widths=[100])
def FP(a, b, h="46mm", keep=False):
    d = dict(t="figures", items=[dict(src="assets/" + s, en=e, ar=r, h=h, fit="contain") for s, e, r in (a, b)])
    if keep: d["keep"] = True
    return d

blocks = [
 SEC("Objectives and preparation", "الأهداف والتحضير"),
 H2("Lung and Thorax Assessment", "تقييم الرئتين والصدر"),
 L(["Demonstrate the ability to safely and accurately complete the lung and thorax assessment.",
    "Demonstrate the ability to accurately document thorax and lung assessment in organized manner."],
   ["إظهار القدرة على إكمال تقييم الرئتين والصدر بأمان ودقّة.", "إظهار القدرة على توثيق تقييم الصدر والرئتين بدقّة وبطريقة منظّمة."],
   en="**Objectives: -** At the end of this lab the student will be able to:", ar="**الأهداف:** في نهاية هذا الدرس سيكون الطالب قادرًا على:"),
 L(["Stethoscope.", "Small ruler.", "Marking pen.", "Alcohol swab."], ["السمّاعة الطبية.", "مسطرة صغيرة.", "قلم تعليم.", "مسحة كحول."],
   en="**Equipment needed: -**", ar="**الأدوات المطلوبة:**"),
 L(["Ask the client to sit upright & the male to uncover to the waist.", "For female, leave the gown on & open at the back.",
    "When examining the anterior chest, lift up the gown & drape it on her shoulders than removing it completely.",
    "For further comfort: a warm room, a warm diaphragm end piece.", "Private examination time with no interruption."],
   ["اطلب من المريض الجلوس منتصبًا، ومن الذكر كشف جسمه حتى الخصر.", "للأنثى اترك الرداء عليها مفتوحًا من الخلف.",
    "عند فحص الصدر الأمامي ارفع الرداء وضعه على كتفيها بدلًا من نزعه بالكامل.",
    "ولمزيد من الراحة: غرفة دافئة، وقطعة غشاء (حجاب) دافئة للسمّاعة.", "وقت فحص خاص بلا مقاطعة."],
   en="**Preparation:-**", ar="**التحضير:**"),
 L(["Cough.", "Smoking history.", "Past history of respiratory infections.", "Chest pain with breathing.", "Self-behaviors", "Environmental exposure", "Shortness of breath."],
   ["السعال.", "تاريخ التدخين.", "التاريخ السابق لعدوى الجهاز التنفّسي.", "ألم الصدر مع التنفّس.", "السلوكيات الذاتية", "التعرّض البيئي", "ضيق النفس."],
   en="**Subjective data:**", ar="**البيانات الذاتية:**"),
 INSHORT([("Equipment: **stethoscope, small ruler, marking pen, alcohol swab**.", "الأدوات: **سمّاعة، ومسطرة صغيرة، وقلم تعليم، ومسحة كحول**."),
          ("Client sits upright; female gown **open at the back**, draped on the shoulders for the anterior chest; warm room and warm diaphragm.", "يجلس المريض منتصبًا؛ ورداء الأنثى **مفتوح من الخلف** ويوضع على الكتفين للصدر الأمامي؛ وغرفة دافئة وغشاء دافئ.")]),

 SEC("Inspection and respiratory landmarks", "الفحص بالنظر والمعالم التنفّسية"),
 H2("Inspect, anterior, posterior & lateral thorax for the following: -", "افحص الصدر الأمامي والخلفي والجانبي بالنظر من حيث ما يلي:"),
 PN([("Color", "اللون", "Pink", "وردي"),
      ("Intercostal spaces", "المسافات الوربية (بين الأضلاع)", "Even & relaxed", "منتظمة ومرتخية"),
      ("Chest symmetry", "تناظر الصدر", "Equal", "متساوٍ"),
      ("Rib slope", "ميل الأضلاع", "Less than 90 degrees downward", "أقل من `90` درجة نحو الأسفل"),
      ("Respiration (rate, depth, rhythm).", "التنفّس (المعدّل، والعمق، والإيقاع).", "Even: - 12-20/ min, unlabored", "منتظم: `12-20/ min`، بلا جهد"),
      ("Anterior-posterior to lateral diameter.", "القطر الأمامي الخلفي إلى القطر الجانبي.", "1: 2 ratios", "نسبة `1: 2`"),
      ("Shape & position of sternum", "شكل القصّ وموضعه", "Level with ribs", "بمستوى الأضلاع"),
      ("Position of trachea", "موضع الرغامى", "Midline", "في خط الوسط")]),
 F("resp-landmarks.jpg", "Respiratory Land marks", "المعالم التنفّسية", h="58mm", fit="contain", keep=True),
 LBT(("Midclavical line", "خط منتصف الترقوة"), ("Midsternal line", "خط منتصف القصّ"), ("Anterior axillary line", "الخط الإبطي الأمامي"),
     ("Midaxillary line", "الخط الإبطي المتوسط"), ("Posterior axillary line", "الخط الإبطي الخلفي"), ("Left scapular line", "خط الكتف الأيسر"),
     ("Right scapular line", "خط الكتف الأيمن"), ("Midspinal line", "خط منتصف العمود الفقري")),
 INSHORT([("Respiration **12–20/min**, even, unlabored; AP : lateral diameter **1 : 2**.", "التنفّس **`12–20/min`** منتظم وبلا جهد؛ والقطر الأمامي الخلفي : الجانبي **`1 : 2`**."),
          ("Rib slope **< 90°** downward; sternum level with ribs; trachea **midline**.", "ميل الأضلاع **أقل من `90°`** للأسفل؛ والقصّ بمستوى الأضلاع؛ والرغامى **في الوسط**.")]),

 SEC("Palpation", "الجسّ"),
 H2("Palpate thorax three levels for the following: -", "جُسّ الصدر على ثلاثة مستويات من حيث ما يلي:"),
 PN([("Sensation", "الإحساس", "No pain or tenderness.", "لا ألم ولا إيلام."),
      ("Vocal fremitus as client says \"99”", "الرجفان الصوتي عندما يقول المريض \"99\"", "Vibration decreases over periphery of lungs & increased over major airways.", "يقلّ الاهتزاز على محيط الرئتين ويزداد على المجاري الهوائية الرئيسة.")]),
 STEPS(["Use either the palm base (the ball) of fingers, or the ulnar edge of one hand.", "Touch the client's chest.",
        "Ask the client to repeat a resonant phrase that generate strong vibration like 99.", "Start over the lung apices & palpate from side to another.",
        "Avoid palpating over the scapulae."],
       ["استعمل إمّا قاعدة الراحة (كرة الأصابع)، أو الحافة الزندية ليد واحدة.", "المس صدر المريض.",
        "اطلب من المريض تكرار عبارة رنّانة تولّد اهتزازًا قويًا مثل `99`.", "ابدأ فوق قمّتي الرئتين وجُسّ من جانب إلى آخر.",
        "تجنّب الجسّ فوق لوحي الكتف."], "**Vocal fremitus:**", "**الرجفان الصوتي:**"),
 FP(("fremitus-ant.jpg", "Tactile fremitus ( Anterior )", "الرجفان اللمسي (أمامي)"), ("fremitus-post.jpg", "Tactile fremitus ( posterior )", "الرجفان اللمسي (خلفي)"), h="44mm"),
 H2("Palpate thorax for thoracic expansion by the using following methods: -", "جُسّ الصدر لتقييم التمدّد الصدري بالطرق التالية:"),
 STEPS(["Placing your warmed hand on the poster lateral chest wall.", "The thumbs should be at level of T9 to T10.",
        "Slide your hands medially to pinch up a small fold between your thumbs.", "Ask the client to take deep breath.", "Your thumb should move with respiration."],
       ["ضع يدك الدافئة على جدار الصدر الخلفي الجانبي.", "يجب أن يكون الإبهامان بمستوى `T9` إلى `T10`.",
        "حرّك يديك نحو الوسط لتجمع طيّة صغيرة بين إبهاميك.", "اطلب من المريض أخذ نفس عميق.", "يجب أن يتحرّك إبهامك مع التنفّس."],
       "**Posteriorly: -**", "**من الخلف:**"),
 STEPS(["Placing your warmed hand on the anterolateral wall.", "Thumbs should be a long the costal margins &pointing toward the xiphoid process.",
        "Ask the client to take deep breath.", "Watch your thumbs move with respiration."],
       ["ضع يدك الدافئة على الجدار الأمامي الجانبي.", "يجب أن يكون الإبهامان على طول الحافتين الضلعيتين ومتّجهين نحو الناتئ الرهابي.",
        "اطلب من المريض أخذ نفس عميق.", "راقب إبهاميك يتحرّكان مع التنفّس."],
       "**Anteriority:-**", "**من الأمام:**"),
 NF(["2 to 3 –inch symmetrical thoracic expansion.", "Symmetrical expansion (thumbs move apart equal distance in both directions).",
     "Symmetrical expansion ( thumbs move apart equal distance in both directions )"],
    ["تمدّد صدري متناظر بمقدار `2 to 3 inch`.", "تمدّد متناظر (يتباعد الإبهامان مسافة متساوية في الاتجاهين).",
     "تمدّد متناظر (يتباعد الإبهامان مسافة متساوية في الاتجاهين)"]),
 FP(("ant-expansion.jpg", "Anterior chest expansion", "تمدّد الصدر الأمامي"), ("post-expansion.jpg", "Posterior chest expansion", "تمدّد الصدر الخلفي"), h="46mm"),
 INSHORT([("Palpation: no pain; **vocal fremitus (\"99\")** decreases at the periphery, increases over major airways; avoid the scapulae.", "الجسّ: لا ألم؛ و**الرجفان الصوتي (\"99\")** يقلّ في المحيط ويزداد على المجاري الرئيسة؛ وتجنّب لوحي الكتف."),
          ("Expansion: thumbs at **T9–T10** (posterior) or along the **costal margins** (anterior) → **2–3 inch symmetrical**.", "التمدّد: الإبهامان عند **`T9–T10`** (خلفيًا) أو على **الحافتين الضلعيتين** (أماميًا) ← **`2–3 inch` متناظر**.")]),

 SEC("Percussion", "القرع"),
 H2("Percuss thorax to determine the following: -", "اقرع الصدر لتحديد ما يلي:"),
 STEPS(["Start at the tops.", "Percuss across the tops of both shoulders.", "Percuss in the interspaces.",
        "Make side to side comparison all the way to lung region.", "Avoid the damping effect of the scapulae & ribs."],
       ["ابدأ من الأعلى.", "اقرع عبر قمّتي الكتفين.", "اقرع في المسافات الوربية.",
        "قارن جانبًا بجانب على طول منطقة الرئة.", "تجنّب التأثير المخمِّد للوحي الكتف والأضلاع."],
       "**Lung Field Posteriorly: -**", "**الحقل الرئوي من الخلف:**"),
 STEPS(["Begin percussing the apices in the supraclavicular areas.", "Then, percussing the interspaces.", "Compare one side to the other.",
        "Move down to the anterior chest.", "Do not do percussion directly over female breast.", "Shift the breast over slightly, using the edge of your stationary hand."],
       ["ابدأ بقرع القمّتين في المنطقتين فوق الترقوة.", "ثم اقرع المسافات الوربية.", "قارن جانبًا بالآخر.",
        "انزل إلى الصدر الأمامي.", "لا تقرع مباشرةً فوق ثدي الأنثى.", "أزح الثدي قليلًا باستعمال حافة يدك الثابتة."],
       "**Lung Field Anteriorly: -**", "**الحقل الرئوي من الأمام:**"),
 NF(["Resonance predominates in healthy lung tissue.", "Cardiac dullness normally found of the anterior chest."],
    ["يسود الرنين في نسيج الرئة السليم.", "تُوجد الأصمّية القلبية طبيعيًا في الصدر الأمامي."]),
 F("post-percussion.jpg", "Posterior respiratory percussion", "القرع التنفّسي الخلفي", h="50mm", fit="contain"),
 STEPS(["Ask the client to exhale & hold it.", "Percuss down the scapular line until the sound changes form resonant to dull each side.",
        "Mark the level where the sound changed to dull.", "Ask the client to take deep breath & hold it.", "Continue percussing form the mark down ward.",
        "Mark the level the sound changed to dull on deep inspiration.", "Measure the difference."],
       ["اطلب من المريض الزفير وحبس النفس.", "اقرع نزولًا على خط الكتف حتى يتغيّر الصوت من رنّان إلى أصمّ في كل جانب.",
        "علّم المستوى الذي تغيّر عنده الصوت إلى أصمّ.", "اطلب من المريض أخذ نفس عميق وحبسه.", "تابع القرع من العلامة نزولًا.",
        "علّم المستوى الذي تغيّر عنده الصوت إلى أصمّ عند الشهيق العميق.", "قِس الفرق."],
       "**Diaphragmatic Excursion Posteriorly: -**", "**مدى حركة الحجاب الحاجز من الخلف:**"),
 NF(["It should be equal bilaterally & measure about 3-5 cm in adult, although it may be up to 7-8cm."],
    ["يجب أن يكون متساويًا في الجانبين ويبلغ نحو `3-5 cm` عند البالغ، مع أنه قد يصل إلى `7-8cm`."]),
 F("diaph-excursion.jpg", "Diaphragmatic excursion", "مدى حركة الحجاب الحاجز", h="50mm", fit="contain", keep=True),
 LBT(("Resonant over lungs", "رنّان فوق الرئتين"), ("Dull over diaphragm", "أصمّ فوق الحجاب الحاجز")),
 INSHORT([("Percuss **interspaces**, side to side; avoid scapulae, ribs and the female breast.", "اقرع **المسافات الوربية** جانبًا بجانب؛ وتجنّب لوحي الكتف والأضلاع والثدي."),
          ("Healthy lung = **resonance**; anterior chest has **cardiac dullness**.", "الرئة السليمة = **رنين**؛ وفي الصدر الأمامي **أصمّية قلبية**."),
          ("Diaphragmatic excursion: exhale-mark vs deep-inspiration-mark → **3–5 cm** (up to 7–8 cm), equal both sides.", "حركة الحجاب: علامة الزفير مقابل علامة الشهيق العميق ← **`3–5 cm`** (حتى `7–8 cm`)، ومتساوية في الجانبين.")]),

 SEC("Auscultation", "الإصغاء (التسمّع)"),
 STEPS(["Put the client in sitting position, leaning forward slightly, with arms resting across the lab.", "Instruct the client to breathe through the mouth.",
        "The breath should be deeper than usual.", "Monitor the breathing through the examination.", "Use the diaphragm of the stethoscope.",
        "Hold the diaphragm firmly on the client’s chest wall.", "Listen at least to one full respiration in each location.",
        "Side to side comparison is most important.", "Do not confuse background noise with lung sounds."],
       ["ضع المريض جالسًا مائلًا إلى الأمام قليلًا وذراعاه مستريحتان على الحِجر.", "وجّه المريض للتنفّس من الفم.",
        "يجب أن يكون النفس أعمق من المعتاد.", "راقب التنفّس طوال الفحص.", "استعمل غشاء (حجاب) السمّاعة.",
        "ثبّت الغشاء بإحكام على جدار صدر المريض.", "استمع إلى دورة تنفّس كاملة واحدة على الأقل في كل موضع.",
        "المقارنة جانبًا بجانب هي الأهم.", "لا تخلط بين ضوضاء الخلفية وأصوات الرئة."],
       "**Auscultate the thorax posteriorly:-**", "**أصغِ إلى الصدر من الخلف:**"),
 T([B("Sound", "الصوت"), B("Normal findings", "النتائج الطبيعية")],
   [[B("**Bronchial breath sounds**", "**أصوات التنفّس القصبية**"), B("heard over trachea, it is loud; expiration longer than inspiration; short silence between inspiration & expiration.", "تُسمع فوق الرغامى، وهي عالية؛ والزفير أطول من الشهيق؛ وصمت قصير بين الشهيق والزفير.")],
    [B("**Broncho-vesicular sounds**", "**الأصوات القصبية الحويصلية**"), B("heard over main stem bronchi; below clavicles & between scapulae; inspiration equal to expiration.", "تُسمع فوق القصبتين الرئيستين؛ تحت الترقوتين وبين لوحي الكتف؛ والشهيق يساوي الزفير.")],
    [B("**Vesicular sounds**", "**الأصوات الحويصلية**"), B("low; soft; heard over lung periphery: inspiration longer than expiration.", "منخفضة؛ ناعمة؛ تُسمع فوق محيط الرئة: والشهيق أطول من الزفير.")]],
   key_cols=[0], widths=[32, 68]),
 F("post-auscultation.jpg", "Posterior respiratory auscultation", "الإصغاء التنفّسي الخلفي", h="48mm", fit="contain"),
 STEPS(["Auscultate from the apices in the supraclavicular areas down to the sixth rib.", "Progress from side to side as you move dawn ward.",
        "Do not use the stethoscope directly over the female breast.", "Displace the breast & listen directly over the chest wall."],
       ["أصغِ من القمّتين في المنطقتين فوق الترقوة نزولًا إلى الضلع السادس.", "تقدّم من جانب إلى جانب وأنت تنزل للأسفل.",
        "لا تستعمل السمّاعة مباشرةً فوق ثدي الأنثى.", "أزح الثدي واستمع مباشرةً فوق جدار الصدر."],
       "**Auscultate the thorax Anteriorly: -**", "**أصغِ إلى الصدر من الأمام:**"),
 FP(("ant-resp-exam.jpg", "Anterior respiratory examination", "الفحص التنفّسي الأمامي"), ("post-resp-exam.jpg", "Posterior respiratory examination", "الفحص التنفّسي الخلفي"), h="50mm"),
 INSHORT([("Use the **diaphragm**, firmly; client breathes deeper through the mouth; **side-to-side comparison** is most important.", "استعمل **الغشاء** بإحكام؛ ويتنفّس المريض أعمق من الفم؛ و**المقارنة جانبًا بجانب** هي الأهم."),
          ("**Bronchial**: trachea, expiration > inspiration. **Bronchovesicular**: main bronchi, inspiration = expiration. **Vesicular**: periphery, inspiration > expiration.", "**القصبي**: الرغامى، الزفير > الشهيق. **القصبي الحويصلي**: القصبتان الرئيستان، الشهيق = الزفير. **الحويصلي**: المحيط، الشهيق > الزفير."),
          ("Anteriorly: from the apices down to the **sixth rib**.", "أماميًا: من القمّتين نزولًا إلى **الضلع السادس**.")]),
] + TERMS([
 ("Intercostal spaces (ICS)", "المسافات الوربية / المسافات بين الأضلاع"), ("Midclavicular line", "خط منتصف الترقوة"), ("Midaxillary line", "الخط الإبطي المتوسط"),
 ("Scapular line", "خط الكتف / خط لوح الكتف"), ("Vocal (tactile) fremitus", "الرجفان الصوتي / الرجفان اللمسي"), ("Thoracic expansion", "التمدّد الصدري / اتساع الصدر"),
 ("Costal margin", "الحافة الضلعية"), ("Xiphoid process", "الناتئ الرهابي / الناتئ الخنجري"), ("Percussion", "القرع / الطَّرق"),
 ("Resonance", "الرنين / الصوت الرنّان"), ("Dullness", "الأصمّية / الصوت الأصمّ"), ("Diaphragmatic excursion", "مدى حركة الحجاب الحاجز / انزياح الحجاب"),
 ("Auscultation", "الإصغاء / التسمّع"), ("Bronchial sounds", "الأصوات القصبية"), ("Bronchovesicular sounds", "الأصوات القصبية الحويصلية"), ("Vesicular sounds", "الأصوات الحويصلية"),
])

mcq = [
 {"topic_en": "Preparation and inspection", "topic_ar": "التحضير والفحص بالنظر"},
 Q("For a female client, the gown is:", "بالنسبة للأنثى يكون الرداء:", [("Left on & open at the back", "متروكًا عليها ومفتوحًا من الخلف"), ("Removed completely", "منزوعًا بالكامل"), ("Open at the front", "مفتوحًا من الأمام"), ("Not used", "غير مستعمل")], "a"),
 Q("The normal respiratory rate in the lecture is:", "معدّل التنفّس الطبيعي في المحاضرة:", [("8-10/min", "8-10/د"), ("12-20/min", "12-20/د"), ("20-30/min", "20-30/د"), ("30-40/min", "30-40/د")], "b"),
 Q("The normal anterior-posterior to lateral diameter ratio is:", "النسبة الطبيعية للقطر الأمامي الخلفي إلى الجانبي:", [("1:1", "1:1"), ("2:1", "2:1"), ("1:2", "1:2"), ("1:3", "1:3")], "c"),
 Q("The normal rib slope is:", "ميل الأضلاع الطبيعي:", [("More than 90 degrees upward", "أكثر من 90 درجة للأعلى"), ("Horizontal", "أفقي"), ("Exactly 90 degrees", "90 درجة تمامًا"), ("Less than 90 degrees downward", "أقل من 90 درجة للأسفل")], "d"),
 Q("The normal sternum is:", "القصّ الطبيعي:", [("Level with ribs", "بمستوى الأضلاع"), ("Depressed", "منخفض"), ("Protruding", "بارز"), ("Deviated", "منحرف")], "a"),
 {"topic_en": "Palpation", "topic_ar": "الجسّ"},
 Q("Vocal fremitus is assessed while the client says:", "يُقيَّم الرجفان الصوتي بينما يقول المريض:", [("Ahh", "آه"), ("99", "99"), ("Ee", "إي"), ("1-2-3", "1-2-3")], "b"),
 Q("Normal vocal fremitus is:", "الرجفان الصوتي الطبيعي:", [("Equal everywhere", "متساوٍ في كل مكان"), ("Increased at the periphery", "يزداد في المحيط"), ("Decreased at the periphery, increased over major airways", "يقلّ في المحيط ويزداد فوق المجاري الرئيسة"), ("Absent", "غائب")], "c"),
 Q("During fremitus palpation, avoid palpating over the:", "عند جسّ الرجفان تجنّب الجسّ فوق:", [("Apices", "القمّتين"), ("Interspaces", "المسافات الوربية"), ("Trachea", "الرغامى"), ("Scapulae", "لوحي الكتف")], "d"),
 Q("For posterior thoracic expansion, the thumbs are placed at the level of:", "لتقييم التمدّد الخلفي يوضع الإبهامان بمستوى:", [("T9 to T10", "T9 إلى T10"), ("T1 to T2", "T1 إلى T2"), ("L1 to L2", "L1 إلى L2"), ("C7", "C7")], "a"),
 Q("For anterior thoracic expansion, the thumbs point toward the:", "لتقييم التمدّد الأمامي يتّجه الإبهامان نحو:", [("Clavicles", "الترقوتين"), ("Xiphoid process", "الناتئ الرهابي"), ("Axilla", "الإبط"), ("Umbilicus", "السُّرّة")], "b"),
 Q("Normal thoracic expansion is:", "التمدّد الصدري الطبيعي:", [("Asymmetrical", "غير متناظر"), ("1 inch", "بوصة واحدة"), ("2 to 3 inch symmetrical", "2 إلى 3 بوصة ومتناظر"), ("5 inch", "5 بوصات")], "c"),
 {"topic_en": "Percussion", "topic_ar": "القرع"},
 Q("Which sound predominates in healthy lung tissue?", "أي صوت يسود في نسيج الرئة السليم؟", [("Dullness", "الأصمّية"), ("Flatness", "الصوت المسطّح"), ("Tympany", "الطبلي"), ("Resonance", "الرنين")], "d"),
 Q("Cardiac dullness is normally found on the:", "توجد الأصمّية القلبية طبيعيًا في:", [("Anterior chest", "الصدر الأمامي"), ("Posterior chest", "الصدر الخلفي"), ("Lung apices", "قمّتي الرئتين"), ("Scapulae", "لوحي الكتف")], "a"),
 Q("Percussion of the lung fields is done in the:", "يُجرى قرع الحقول الرئوية في:", [("Ribs", "الأضلاع"), ("Interspaces", "المسافات الوربية"), ("Scapulae", "لوحي الكتف"), ("Breast", "الثدي")], "b"),
 Q("Diaphragmatic excursion is percussed down the:", "تُقرع حركة الحجاب الحاجز نزولًا على:", [("Midsternal line", "خط منتصف القصّ"), ("Midaxillary line", "الخط الإبطي المتوسط"), ("Scapular line", "خط الكتف"), ("Midclavicular line", "خط منتصف الترقوة")], "c"),
 Q("Normal diaphragmatic excursion in adults is about:", "حركة الحجاب الطبيعية عند البالغ نحو:", [("1 cm", "1 سم"), ("10-12 cm", "10-12 سم"), ("0.5 cm", "0.5 سم"), ("3-5 cm", "3-5 سم")], "d"),
 Q("Diaphragmatic excursion may normally be up to:", "قد تصل حركة الحجاب طبيعيًا إلى:", [("7-8 cm", "7-8 سم"), ("12 cm", "12 سم"), ("15 cm", "15 سم"), ("2 cm", "2 سم")], "a"),
 {"topic_en": "Auscultation", "topic_ar": "الإصغاء"},
 Q("Lung auscultation is done with the:", "يُجرى إصغاء الرئة بـ:", [("Bell lightly applied", "الجرس بلطف"), ("Diaphragm held firmly", "الغشاء بإحكام"), ("Palm of the hand", "راحة اليد"), ("Ulnar edge", "الحافة الزندية")], "b"),
 Q("The most important point in lung auscultation is:", "أهم نقطة في إصغاء الرئة:", [("Listening fast", "الاستماع بسرعة"), ("Using the bell", "استعمال الجرس"), ("Side to side comparison", "المقارنة جانبًا بجانب"), ("Shallow breathing", "التنفّس السطحي")], "c"),
 Q("Bronchial breath sounds are heard over the:", "تُسمع أصوات التنفّس القصبية فوق:", [("Lung periphery", "محيط الرئة"), ("Main stem bronchi", "القصبتين الرئيستين"), ("Diaphragm", "الحجاب الحاجز"), ("Trachea", "الرغامى")], "d"),
 Q("In bronchovesicular sounds:", "في الأصوات القصبية الحويصلية:", [("Inspiration equals expiration", "الشهيق يساوي الزفير"), ("Expiration is longer", "الزفير أطول"), ("Inspiration is longer", "الشهيق أطول"), ("No expiration", "لا زفير")], "a"),
 Q("Vesicular sounds are:", "الأصوات الحويصلية:", [("Loud, over trachea", "عالية فوق الرغامى"), ("Low, soft, over lung periphery; inspiration longer than expiration", "منخفضة ناعمة فوق المحيط؛ الشهيق أطول من الزفير"), ("Heard between scapulae; I = E", "بين لوحي الكتف؛ الشهيق = الزفير"), ("Absent normally", "غائبة طبيعيًا")], "b"),
 Q("Anterior auscultation extends from the apices down to the:", "يمتد الإصغاء الأمامي من القمّتين نزولًا إلى:", [("Second rib", "الضلع الثاني"), ("Fourth rib", "الضلع الرابع"), ("Sixth rib", "الضلع السادس"), ("Tenth rib", "الضلع العاشر")], "c"),
 Q("Picture: this figure shows:", "صورة: يوضّح هذا الشكل:", [("Lung lobes", "فصوص الرئة"), ("Auscultation sites", "مواقع الإصغاء"), ("Heart areas", "مناطق القلب"), ("Respiratory landmarks (imaginary lines)", "المعالم التنفّسية (الخطوط الوهمية)")], "d", img="assets/resp-landmarks.jpg", img_h="34mm"),
 Q("Picture: the examiner is assessing:", "صورة: الفاحص يقيّم:", [("Diaphragmatic excursion", "حركة الحجاب الحاجز"), ("Vocal fremitus", "الرجفان الصوتي"), ("Thoracic expansion", "التمدّد الصدري"), ("Tracheal position", "موضع الرغامى")], "a", img="assets/diaph-excursion.jpg", img_h="38mm"),
]
mcq = balance(mcq, 44)
tf = [
 TF("The male client uncovers to the waist.", "يكشف المريض الذكر جسمه حتى الخصر.", "T"),
 TF("Normal intercostal spaces are retracted.", "المسافات الوربية الطبيعية منسحبة.", "F"),
 TF("The trachea is normally in the midline.", "الرغامى طبيعيًا في خط الوسط.", "T"),
 TF("Vocal fremitus increases at the periphery of the lungs.", "يزداد الرجفان الصوتي في محيط الرئتين.", "F"),
 TF("Fremitus can be palpated with the ulnar edge of one hand.", "يمكن جسّ الرجفان بالحافة الزندية ليد واحدة.", "T"),
 TF("Percussion is done directly over the female breast.", "يُجرى القرع مباشرةً فوق ثدي الأنثى.", "F"),
 TF("Diaphragmatic excursion should be equal bilaterally.", "يجب أن تكون حركة الحجاب متساوية في الجانبين.", "T"),
 TF("The client breathes through the nose during lung auscultation.", "يتنفّس المريض من الأنف أثناء إصغاء الرئة.", "F"),
 TF("Listen to at least one full respiration in each location.", "استمع إلى دورة تنفّس كاملة واحدة على الأقل في كل موضع.", "T"),
 TF("In bronchial sounds, expiration is longer than inspiration.", "في الأصوات القصبية الزفير أطول من الشهيق.", "T"),
 TF("Bronchovesicular sounds are heard over the lung periphery.", "تُسمع الأصوات القصبية الحويصلية فوق محيط الرئة.", "F"),
 TF("Posterior auscultation is done with the client leaning forward slightly.", "يُجرى الإصغاء الخلفي والمريض مائل للأمام قليلًا.", "T"),
]
traps = [
 TR("Bronchial vs bronchovesicular vs vesicular", "القصبي مقابل القصبي الحويصلي مقابل الحويصلي", "Bronchial: over trachea, loud, E > I. Bronchovesicular: over main stem bronchi, below clavicles and between scapulae, I = E. Vesicular: periphery, low and soft, I > E.", "القصبي: فوق الرغامى، عالٍ، الزفير > الشهيق. القصبي الحويصلي: فوق القصبتين الرئيستين، تحت الترقوتين وبين لوحي الكتف، الشهيق = الزفير. الحويصلي: المحيط، منخفض وناعم، الشهيق > الزفير."),
 TR("Fremitus: periphery vs airways", "الرجفان: المحيط مقابل المجاري", "Vibration decreases over the periphery and increases over the major airways.", "يقلّ الاهتزاز فوق المحيط ويزداد فوق المجاري الرئيسة."),
 TR("Posterior vs anterior expansion", "التمدّد الخلفي مقابل الأمامي", "Posterior: thumbs at T9 to T10. Anterior: thumbs along the costal margins pointing toward the xiphoid process.", "الخلفي: الإبهامان عند T9 إلى T10. الأمامي: الإبهامان على الحافتين الضلعيتين باتجاه الناتئ الرهابي."),
 TR("Resonance vs dullness", "الرنين مقابل الأصمّية", "Resonance predominates in healthy lung; cardiac dullness is normal on the anterior chest and over the diaphragm.", "يسود الرنين في الرئة السليمة؛ والأصمّية طبيعية فوق القلب في الصدر الأمامي وفوق الحجاب."),
 TR("Diaphragm or bell for the lungs?", "الغشاء أم الجرس للرئتين؟", "The diaphragm of the stethoscope, held firmly on the chest wall.", "غشاء السمّاعة، مثبّتًا بإحكام على جدار الصدر."),
]
important = [
 IM("List the normal findings of thorax inspection.", "عدّد النتائج الطبيعية لفحص الصدر بالنظر.", "Color pink; intercostal spaces even & relaxed; chest symmetry equal; rib slope less than 90 degrees downward; respiration even 12-20/min, unlabored; AP to lateral diameter 1:2; sternum level with ribs; trachea midline.", "اللون وردي؛ والمسافات الوربية منتظمة ومرتخية؛ والصدر متناظر؛ وميل الأضلاع أقل من 90 درجة للأسفل؛ والتنفّس منتظم 12-20/د بلا جهد؛ والقطر الأمامي الخلفي إلى الجانبي 1:2؛ والقصّ بمستوى الأضلاع؛ والرغامى في الوسط."),
 IM("How is vocal fremitus assessed?", "كيف يُقيَّم الرجفان الصوتي؟", "Use the palm base (ball) of the fingers or the ulnar edge of one hand; touch the chest; ask the client to repeat 99; start over the apices and palpate side to side; avoid the scapulae. Normal: vibration decreases over the periphery and increases over major airways.", "تُستعمل قاعدة الراحة أو الحافة الزندية؛ ويُلمس الصدر؛ ويكرّر المريض 99؛ ويُبدأ من القمّتين جانبًا بجانب؛ وتُتجنّب لوحا الكتف. الطبيعي: يقلّ الاهتزاز في المحيط ويزداد فوق المجاري الرئيسة."),
 IM("Describe the measurement of diaphragmatic excursion.", "صف قياس حركة الحجاب الحاجز.", "The client exhales and holds; percuss down the scapular line until resonance changes to dullness and mark it; the client takes a deep breath and holds; percuss down from the mark and mark the new level; measure the difference. Normal: equal bilaterally, about 3-5 cm in adults, may be up to 7-8 cm.", "يزفر المريض ويحبس؛ ويُقرع نزولًا على خط الكتف حتى يتغيّر الرنين إلى أصمّية ويُعلَّم؛ ثم يأخذ نفسًا عميقًا ويحبسه؛ ويُقرع من العلامة نزولًا ويُعلَّم المستوى الجديد؛ ويُقاس الفرق. الطبيعي: متساوٍ في الجانبين ونحو 3-5 سم وقد يصل 7-8 سم."),
 IM("Compare the three normal breath sounds.", "قارن بين أصوات التنفّس الطبيعية الثلاثة.", "Bronchial: over trachea, loud, expiration longer than inspiration, short silence between them. Bronchovesicular: over main stem bronchi, below clavicles and between scapulae, inspiration equal to expiration. Vesicular: low, soft, over lung periphery, inspiration longer than expiration.", "القصبي: فوق الرغامى، عالٍ، والزفير أطول مع صمت قصير بينهما. القصبي الحويصلي: فوق القصبتين الرئيستين، تحت الترقوتين وبين لوحي الكتف، والشهيق = الزفير. الحويصلي: منخفض ناعم فوق المحيط، والشهيق أطول."),
 IM("Give the steps of posterior auscultation of the thorax.", "اذكر خطوات الإصغاء الخلفي للصدر.", "Client sitting, leaning forward slightly with arms resting; breathe through the mouth, deeper than usual; monitor breathing; use the diaphragm held firmly on the chest wall; listen to at least one full respiration in each location; compare side to side; do not confuse background noise with lung sounds.", "يجلس المريض مائلًا للأمام وذراعاه مستريحتان؛ ويتنفّس من الفم أعمق من المعتاد؛ ويُراقب التنفّس؛ ويُستعمل الغشاء بإحكام؛ ويُستمع لدورة تنفّس كاملة على الأقل في كل موضع؛ وتُقارن الجهتان؛ ولا تُخلط ضوضاء الخلفية بأصوات الرئة."),
]
meta = HA(4, "Lung and Thorax Assessment", "تقييم الرئتين والصدر")
save("nursing-ha-lec4-lung-thorax", meta, chunk_lists(blocks, size=10, budget=13), mcq, tf, traps, important)

```
