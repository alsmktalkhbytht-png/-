---
source: BIOS-Obsidian/tools/scripts/pat7/p7q.py
handouts: [pathology-lec7-oral-tumors]
saved: 2026-11-06
tags: [bios, code]
---
# pat7/p7q.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#pathology-lec7-oral-tumors|pathology-lec7-oral-tumors]]

```python
A = lambda f: "assets/" + f
mcq = [
 {"topic_en": "Benign salivary tumors", "topic_ar": "أورام الغدد اللعابية الحميدة"},
 Q("The most common benign tumor of the salivary glands is:", "أشيع ورم حميد في الغدد اللعابية:", O(("Pleomorphic adenoma", "الورم الغدّي متعدّد الأشكال"), ("Warthin tumor", "ورم وارثين"), ("Mucoepidermoid carcinoma", "المخاطية البشروية"), ("Oncocytoma", "الخلوي الحمضي")), "a"),
 Q("Pleomorphic adenoma is also called:", "يسمّى الورم الغدّي متعدّد الأشكال أيضًا:", O(("Adenolymphoma", "الورم الغدّي اللمفاوي"), ("Mixed tumor", "الورم المختلط"), ("Hamartoma", "الورم العابي"), ("Cystadenoma", "الورم الغدّي الكيسي")), "b"),
 Q("In pleomorphic adenoma, “pleomorphic” refers to:", "في الورم الغدّي متعدّد الأشكال، “متعدّد الأشكال” يشير إلى:", O(("Nuclear atypia", "لانموذجية الأنوية"), ("Many mitoses", "انقسامات كثيرة"), ("Variable cell types", "تنوّع أنواع الخلايا"), ("Malignancy", "الخباثة")), "c"),
 Q("Pleomorphic adenoma is most frequent in:", "الورم الغدّي متعدّد الأشكال أكثر شيوعًا في:", O(("Children", "الأطفال"), ("Elderly males", "الذكور المسنّين"), ("Smokers", "المدخّنين"), ("Females, 3rd–5th decade", "الإناث، العقد 3–5")), "d"),
 Q("Pleomorphic adenoma constitutes about what percentage of parotid tumors?", "يشكّل الورم الغدّي متعدّد الأشكال حوالي كم نسبة من أورام النكفية؟", O(("60%", "60%"), ("15%", "15%"), ("80%", "80%"), ("5%", "5%")), "a"),
 Q("A known risk factor for pleomorphic adenoma is:", "عامل خطورة معروف للورم الغدّي متعدّد الأشكال:", O(("Smoking", "التدخين"), ("Radiation exposure", "التعرّض للإشعاع"), ("Alcohol", "الكحول"), ("HPV", "فيروس الورم الحليمي")), "b"),
 Q("Warthin tumor is the:", "ورم وارثين هو:", O(("Most common malignant salivary tumor", "أشيع ورم لعابي خبيث"), ("Most common benign tumor", "أشيع ورم حميد"), ("Second most common salivary gland neoplasm", "ثاني أشيع ورم في الغدد اللعابية"), ("Rarest salivary tumor", "أندر ورم لعابي")), "c"),
 Q("Warthin tumor almost exclusively arises in the:", "ينشأ ورم وارثين حصرًا تقريبًا في:", O(("Sublingual gland", "الغدة تحت اللسان"), ("Submandibular gland", "الغدة تحت الفكية"), ("Minor salivary glands", "الغدد الصغيرة"), ("Parotid gland", "الغدة النكفية")), "d"),
 Q("The only salivary gland tumor more common in males is:", "الورم اللعابي الوحيد الأشيع في الذكور:", O(("Warthin tumor", "ورم وارثين"), ("Pleomorphic adenoma", "متعدّد الأشكال"), ("Mucoepidermoid carcinoma", "المخاطية البشروية"), ("Adenoid cystic carcinoma", "الغدّانية الكيسية")), "a"),
 Q("Smokers have what risk of Warthin tumor compared to nonsmokers?", "ما خطر ورم وارثين عند المدخّنين مقارنةً بغيرهم؟", O(("Twice", "الضعف"), ("Eight times", "ثمانية أضعاف"), ("Sixty times", "ستون ضعفًا"), ("Same", "نفسه")), "b"),
 {"topic_en": "Malignant oral tumors", "topic_ar": "الأورام الفموية الخبيثة"},
 Q("The majority of oral cancers are:", "أغلب سرطانات الفم:", O(("Adenocarcinomas", "كارسينومات غدّية"), ("Lymphomas", "لمفومات"), ("Squamous cell carcinomas", "كارسينومات حرشفية"), ("Sarcomas", "ساركومات")), "c"),
 Q("Oral SCC is usually seen in:", "تُرى SCC الفموية عادةً في:", O(("Children", "الأطفال"), ("Young women", "الشابات"), ("Infants", "الرضّع"), ("Middle-aged men", "رجال منتصف العمر")), "d"),
 Q("Inactivation of which gene occurs in about 80% of oral SCC?", "تعطيل أيّ جين يحدث في حوالي 80% من SCC الفموية؟", O(("p16", "p16"), ("KRAS", "KRAS"), ("BRCA1", "BRCA1"), ("RB only", "RB فقط")), "a"),
 Q("p53 mutation in oral SCC is associated with progression of:", "ترتبط طفرة p53 في SCC الفموية بتطوّر:", O(("Dysplasia to normal", "خلل التنسّج للطبيعي"), ("Hyperplasia/hyperkeratosis to dysplasia", "فرط التنسّج/التقرّن إلى خلل التنسّج"), ("Cancer to benign", "السرطان للحميد"), ("Metastasis only", "النقيلة فقط")), "b"),
 Q("Amplification of cyclin D1 in oral SCC:", "تضخيم cyclin D1 في SCC الفموية:", O(("Stops the cell cycle", "يوقف دورة الخلية"), ("Inactivates p16", "يعطّل p16"), ("Constitutively activates cell cycle progression", "ينشّط تقدّم دورة الخلية دائمًا"), ("Causes apoptosis", "يسبّب الموت المبرمج")), "c"),
 Q("The more anterior the oral tumor, the more it spreads to the:", "كلما كان الورم الفموي أماميًا أكثر زاد انتشاره إلى:", O(("Liver", "الكبد"), ("Retropharyngeal nodes", "العقد خلف البلعوم"), ("Bones", "العظام"), ("Cervical nodes", "العقد العنقية")), "d"),
 Q("Carcinomas of the base of the tongue metastasize to the:", "تنتقل كارسينومات قاعدة اللسان إلى:", O(("Deep retropharyngeal lymph nodes", "العقد خلف البلعوم العميقة"), ("Axillary nodes", "العقد الإبطية"), ("Inguinal nodes", "العقد الأربية"), ("Brain only", "الدماغ فقط")), "a"),
 Q("Blood spread of oral SCC is to:", "الانتشار الدموي لـ SCC الفموية إلى:", O(("Kidney and spleen", "الكلية والطحال"), ("Lungs, liver, and bones", "الرئتين والكبد والعظام"), ("Skin only", "الجلد فقط"), ("Heart", "القلب")), "b"),
 Q("The most common primary malignant tumor of the salivary glands is:", "أشيع ورم خبيث أولي في الغدد اللعابية:", O(("Warthin tumor", "ورم وارثين"), ("Pleomorphic adenoma", "متعدّد الأشكال"), ("Mucoepidermoid carcinoma", "الكارسينوما المخاطية البشروية"), ("SCC", "SCC")), "c"),
 Q("Mucoepidermoid carcinoma constitutes about what percentage of salivary gland tumors?", "تشكّل المخاطية البشروية حوالي كم نسبة من أورام الغدد اللعابية؟", O(("60%", "60%"), ("80%", "80%"), ("5%", "5%"), ("15%", "15%")), "d"),
 {"topic_en": "Reflux esophagitis", "topic_ar": "التهاب المريء الارتجاعي"},
 Q("The esophageal squamous epithelium is sensitive to:", "الظهارة الحرشفية للمريء حسّاسة لـ:", O(("Acid", "الحامض"), ("Food abrasion", "احتكاك الطعام"), ("Bicarbonate", "البيكاربونات"), ("Mucin", "المخاط")), "a"),
 Q("The most frequent cause of esophagitis is:", "أشيع سبب لالتهاب المريء:", O(("Candida", "المبيضّات"), ("Reflux of gastric contents (GERD)", "ارتجاع محتويات المعدة (GERD)"), ("Herpes virus", "فيروس الهربس"), ("Radiation", "الإشعاع")), "b"),
 Q("With more significant GERD, the first cells recruited into the mucosa are:", "مع GERD الأشد، أول خلايا تُستدعى للمخاطية:", O(("Lymphocytes", "اللمفاويات"), ("Neutrophils", "العدلات"), ("Eosinophils", "الحمضات"), ("Plasma cells", "خلايا البلازما")), "c"),
 Q("Basal zone hyperplasia in GERD exceeds what proportion of epithelial thickness?", "يتجاوز فرط تنسّج المنطقة القاعدية في GERD أيّ نسبة من سمك الظهارة؟", O(("5%", "5%"), ("50%", "50%"), ("80%", "80%"), ("20%", "20%")), "d"),
 Q("GERD is most common in adults older than:", "GERD أشيع في البالغين فوق:", O(("40 years", "40 سنة"), ("20 years", "20 سنة"), ("70 years", "70 سنة"), ("10 years", "10 سنوات")), "a"),
 Q("Symptomatic relief of GERD is typically provided by:", "يخفّف أعراض GERD عادةً:", O(("Antibiotics", "المضادات الحيوية"), ("Proton pump inhibitors", "مثبّطات مضخّة البروتون"), ("Steroids", "الستيرويدات"), ("Surgery always", "الجراحة دائمًا")), "b"),
 Q("Which is a complication of reflux esophagitis?", "أيّ مما يأتي من مضاعفات التهاب المريء الارتجاعي؟", O(("Warthin tumor", "ورم وارثين"), ("Pleomorphic adenoma", "متعدّد الأشكال"), ("Barrett esophagus", "مريء باريت"), ("Wilms tumor", "ورم ويلمز")), "c"),
 {"topic_en": "Picture questions", "topic_ar": "أسئلة الصور"},
 Q("This parotid swelling with MRI (A, B) is most likely:", "تورّم النكفية هذا مع الرنين (A، B) على الأرجح:", O(("Reflux esophagitis", "التهاب المريء الارتجاعي"), ("Oral SCC of the tongue", "SCC اللسان"), ("Wilms tumor", "ورم ويلمز"), ("Pleomorphic adenoma", "الورم الغدّي متعدّد الأشكال")), "d", img=A("pleomorphic-patient-mri.jpg"), img_h="40mm"),
 Q("This intraoral swelling of the right maxilla with this histology is:", "هذا التورّم داخل الفم في الفك العلوي الأيمن مع هذا النسيج:", O(("Mucoepidermoid carcinoma", "الكارسينوما المخاطية البشروية"), ("Warthin tumor", "ورم وارثين"), ("Hamartoma", "الورم العابي"), ("Barrett esophagus", "مريء باريت")), "a", img=A("mucoepidermoid-clinical.jpg"), img_h="38mm"),
]

tf = [
 TF("Pleomorphic adenoma contains epithelial and stromal elements.", "يحتوي الورم الغدّي متعدّد الأشكال عناصر ظهارية وسدوية.", "T"),
 TF("Pleomorphic adenoma usually arises in the deep lobe of the parotid.", "ينشأ الورم الغدّي متعدّد الأشكال عادةً في الفص العميق للنكفية.", "F"),
 TF("Pleomorphic adenoma is very rare in the sublingual gland.", "الورم الغدّي متعدّد الأشكال نادر جدًا في الغدة تحت اللسان.", "T"),
 TF("Warthin tumor is malignant.", "ورم وارثين خبيث.", "F"),
 TF("Warthin tumor usually occurs between the 5th and 7th decades.", "يحدث ورم وارثين عادةً بين العقد الخامس والسابع.", "T"),
 TF("Oral SCC is a multifactorial disease.", "SCC الفموية مرض متعدّد العوامل.", "T"),
 TF("The development of SCC is a single-step process.", "نشوء SCC عملية من خطوة واحدة.", "F"),
 TF("Mucoepidermoid carcinoma accounts for a major fraction of minor salivary gland tumors.", "تشكّل المخاطية البشروية جزءًا كبيرًا من أورام الغدد اللعابية الصغيرة.", "T"),
 TF("Mucoepidermoid carcinoma occurs mainly in the submandibular gland.", "تحدث المخاطية البشروية أساسًا في الغدة تحت الفكية.", "F"),
 TF("Submucosal esophageal glands secrete mucin and bicarbonate.", "تفرز الغدد المريئية تحت المخاطية المخاط والبيكاربونات.", "T"),
 TF("In mild GERD the mucosal histology is often unremarkable.", "في GERD الخفيف يكون النسيج المخاطي غالبًا غير لافت.", "T"),
 TF("GERD never occurs in infants.", "لا يحدث GERD أبدًا في الرضّع.", "F"),
 TF("Severity of GERD symptoms is closely related to the degree of histologic damage.", "ترتبط شدّة أعراض GERD بشدّة بدرجة الضرر النسيجي.", "F"),
 TF("Chronic GERD chest pain may be mistaken for heart disease.", "قد يُخلط ألم الصدر في GERD المزمن بمرض القلب.", "T"),
]

traps = [
 TR("Most common benign vs most common malignant salivary tumor?", "أشيع حميد مقابل أشيع خبيث لعابي؟",
    "Benign: pleomorphic adenoma (Warthin is 2nd); malignant: mucoepidermoid carcinoma.", "الحميد: الورم الغدّي متعدّد الأشكال (ووارثين الثاني)؛ الخبيث: الكارسينوما المخاطية البشروية."),
 TR("Female or male?", "أنثى أم ذكر؟",
    "Pleomorphic adenoma → females; Warthin tumor → the only salivary tumor commoner in males; oral SCC → middle-aged men.", "متعدّد الأشكال ← الإناث؛ وارثين ← الوحيد الأشيع في الذكور؛ SCC الفموية ← رجال منتصف العمر."),
 TR("Radiation or smoking?", "الإشعاع أم التدخين؟",
    "Radiation ↑ risk of pleomorphic adenoma; smoking ×8 risk of Warthin tumor.", "الإشعاع ↑ خطر متعدّد الأشكال؛ والتدخين ×8 خطر وارثين."),
 TR("“Pleomorphic” — nuclear atypia?", "“متعدّد الأشكال” — لانموذجية الأنوية؟",
    "No — in pleomorphic adenoma it means variable cell types (the general pathology meaning is nuclear variation).", "لا — في هذا الورم يعني تنوّع أنواع الخلايا (والمعنى العام بعلم الأمراض تباين الأنوية)."),
 TR("p16, p53, cyclin D1 — which does what?", "p16 وp53 وcyclin D1 — أيّها يفعل ماذا؟",
    "p16 inactivation in ~80%; p53 mutation → hyperplasia/hyperkeratosis to dysplasia; cyclin D1 amplification → constant cell-cycle activation.", "تعطيل p16 في ~80%؛ طفرة p53 ← فرط تنسّج/تقرّن إلى خلل تنسّج؛ تضخيم cyclin D1 ← تنشيط دائم لدورة الخلية."),
 TR("Eosinophils or neutrophils first in GERD?", "الحمضات أم العدلات أولًا في GERD؟",
    "Eosinophils first; neutrophils follow and indicate more severe injury.", "الحمضات أولًا؛ ثم العدلات وتدل على أذى أشد."),
]

important = [
 IM("Write about pleomorphic adenoma.", "اكتب عن الورم الغدّي متعدّد الأشكال.",
    "The most common benign salivary gland tumor, an admixture of epithelial and stromal elements (mixed tumor); named for its variable cell types. Age 3rd–5th decade; more frequent in females. Site: parotid (~60% of parotid tumors, superficial lobe), less in submandibular, very rare in sublingual; minor glands relatively rare. Etiology unknown; radiation increases risk.",
    "أشيع ورم حميد في الغدد اللعابية، خليط من عناصر ظهارية وسدوية (ورم مختلط)؛ سُمّي لتنوّع خلاياه. العمر العقد 3–5؛ أشيع في الإناث. الموقع: النكفية (~60% من أورامها، الفص السطحي)، أقل في تحت الفكية، نادر جدًا في تحت اللسان؛ والغدد الصغيرة نادرة نسبيًا. السبب غير معروف؛ والإشعاع يزيد الخطر."),
 IM("Write about Warthin tumor.", "اكتب عن ورم وارثين.",
    "Papillary cystadenoma lymphomatosum (adenolymphoma); benign, second most common salivary neoplasm; almost exclusively in the parotid; the only salivary tumor commoner in males; 5th–7th decade; smokers have eight times the risk.",
    "الورم الغدّي الكيسي الحليمي اللمفاوي (الورم الغدّي اللمفاوي)؛ حميد، ثاني أشيع ورم لعابي؛ حصرًا تقريبًا في النكفية؛ الوحيد الأشيع في الذكور؛ العقد 5–7؛ وللمدخّنين ثمانية أضعاف الخطر."),
 IM("Explain the pathogenesis of oral squamous cell carcinoma.", "اشرح إمراضية كارسينوما الخلايا الحرشفية الفموية.",
    "A multistep process of sequential activation of oncogenes and inactivation of tumor suppressor genes in a clonal population: p16 inactivation (~80%); p53 mutation with progression of hyperplasia/hyperkeratosis to dysplasia; amplification and overexpression of cyclin D1 constitutively activating the cell cycle.",
    "عملية متعدّدة الخطوات من تنشيط متسلسل للجينات الورمية وتعطيل للكابتة في مجموعة نسيلية: تعطيل p16 (~80%)؛ طفرة p53 مع تطوّر فرط التنسّج/التقرّن إلى خلل التنسّج؛ تضخيم cyclin D1 وفرط التعبير عنه ينشّط دورة الخلية دائمًا."),
 IM("Describe the methods of spread of oral SCC.", "صف طرق انتشار SCC الفموية.",
    "Local: depends on the primary site. Lymph node: depends on tumor location — the more anterior, the more cervical node spread; base of tongue and oropharynx → deep retropharyngeal nodes. Blood: lungs, liver and bones.",
    "الموضعي: يعتمد على الموقع الأولي. العقد: تعتمد على موقع الورم — كلما كان أماميًا زاد انتشاره للعقد العنقية؛ قاعدة اللسان والبلعوم الفموي ← العقد خلف البلعوم العميقة. الدموي: الرئتان والكبد والعظام."),
 IM("Write about mucoepidermoid carcinoma.", "اكتب عن الكارسينوما المخاطية البشروية.",
    "The most common primary malignant tumor of the salivary glands; about 15% of all salivary gland tumors; mainly (60–70%) in the parotids; a major fraction of minor salivary gland tumors.",
    "أشيع ورم خبيث أولي في الغدد اللعابية؛ حوالي 15% من كل أورامها؛ أساسًا (60–70%) في النكفيتين؛ وجزء كبير من أورام الغدد اللعابية الصغيرة."),
 IM("Describe reflux esophagitis: morphology and clinical features.", "صف التهاب المريء الارتجاعي: الشكل النسيجي والمظاهر السريرية.",
    "Gastric reflux is the commonest cause of esophagitis (GERD). Morphology: hyperemia; often unremarkable in mild cases; eosinophils then neutrophils with more severe disease; basal zone hyperplasia > 20% of thickness and lamina propria papillae reaching the upper third. Clinical: adults > 40 (also infants, children); heartburn, dysphagia, sour regurgitation; rarely severe chest pain mimicking heart disease; PPIs relieve symptoms; damage increases with duration; complications: ulceration, hematemesis, melena, stricture, Barrett esophagus.",
    "ارتجاع المعدة أشيع سبب لالتهاب المريء (GERD). النسيج: احتقان؛ غالبًا غير لافت في الخفيف؛ حمضات ثم عدلات مع المرض الأشد؛ فرط تنسّج قاعدي > 20% وحليمات الصفيحة المخصوصة تصل الثلث العلوي. السريري: بالغون > 40 (وأيضًا رضّع وأطفال)؛ حرقة، عسر بلع، ارتجاع حامض؛ نادرًا ألم صدري شديد يشبه القلب؛ مثبّطات مضخّة البروتون تخفّف الأعراض؛ الضرر يزيد مع المدّة؛ المضاعفات: تقرّح، قيء دم، melena، تضيّق، مريء باريت."),
]

meta = dict(subject_en="Pathology", subject_ar="علم الأمراض", short_ar="أمراض",
            unit_en="Lecture 7", unit_ar="المحاضرة 7", unit_label="LEC", unit_no="7",
            title_en="Oral Cavity Tumors", title_ar="أورام التجويف الفموي",
            kind="Theory — نظري", stage="The fourth stage — الرابعة", instructor="د. حامد خليل التميمي")
save("pathology-lec7-oral-tumors", meta, blocks, balance(mcq, 31), tf, traps, important)

```
