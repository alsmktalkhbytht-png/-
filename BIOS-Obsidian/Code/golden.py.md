---
source: BIOS-Obsidian/tools/scripts/golden.py
handouts: [pathology-golden-exam]
saved: 2026-11-15
tags: [bios, code]
---
# golden.py — الصمونة الذهبية (solved pathology exam bank)

```python
import sys, json, os
sys.path.insert(0, "/home/user/bios-repo/BIOS-Obsidian/tools/scripts")
sys.path.insert(0, "/tmp/gwork")
from bidi import ltr_all

# helpers (self-contained, keep exam option order; no balance)
def O(*o): return [[e, a] for e, a in o]
def Q(en, ar, opts, ans, **k): return dict(en=en, ar=ar, options=opts, answer=ans, **k)
def IM(en, ar, ae, aa): return dict(en=en, ar=ar, answer_en=ae, answer_ar=aa)
W = lambda q, en, ar: dict(q, note_en=en, note_ar=ar)
FOLDER = "pathology-golden-exam"

mcq = [
 {"topic_en": "Exam 1 — Choose the most suitable answer (Mid-exam)", "topic_ar": "الامتحان الأول — اختر الأنسب (امتحان نصفي)"},
 Q("What is atelectasis also known as?", "الانخماص يُعرف أيضًا بـ؟",
   O(("Lung expansion", "تمدّد الرئة"), ("Lung collapse", "انهيار (انخماص) الرئة"), ("Alveolar repair", "إصلاح سنخي"), ("Hypoxemia", "نقص أكسجة الدم")), "b"),
 Q("Which type of atelectasis results from airway obstruction?", "أيّ نوع من الانخماص ينتج عن انسداد المجرى الهوائي؟",
   O(("Resorption atelectasis", "الانخماص الامتصاصي"), ("Compression atelectasis", "الانخماص الانضغاطي"), ("Contraction atelectasis", "الانخماص التقلّصي"), ("Hypoxic atelectasis", "الانخماص الناقص الأكسجين")), "a"),
 W(Q("Which cells primarily produce pulmonary surfactant?", "أيّ خلايا تنتج الفاعل بالسطح الرئوي بصورة رئيسة؟",
   O(("Type I pneumocytes", "الخلايا الرئوية النوع الأول"), ("Type II pneumocytes", "الخلايا الرئوية النوع الثاني"), ("Alveolar macrophages", "البلاعم السنخية"), ("Goblet cells", "الخلايا الكأسية")), "b"),
   "Type II pneumocytes synthesize surfactant (type I only line the surface for gas exchange).", "الخلايا الرئوية النوع الثاني تصنّع الفاعل بالسطح (النوع الأول مجرّد تبطين للسطح لتبادل الغازات)."),
 Q("Acute Respiratory Distress Syndrome (ARDS) is primarily caused by:", "متلازمة الضائقة التنفسية الحادة (ARDS) سببها الرئيس:",
   O(("Lung infections", "عدوى الرئة"), ("Diffuse alveolar damage", "الأذى السنخي المنتشر"), ("Bronchial obstruction", "انسداد قصبي"), ("Hypoventilation", "نقص التهوية")), "b"),
 Q("The Reid index is used to measure:", "يُستعمل مشعر ريد (Reid) لقياس:",
   O(("Lung volume", "حجم الرئة"), ("Mucous gland size in chronic bronchitis", "حجم الغدد المخاطية في التهاب القصبات المزمن"), ("Airflow rate", "معدّل جريان الهواء"), ("Bronchial diameter", "قطر القصبة")), "b"),
 Q("The main feature of chronic bronchitis is:", "السمة الرئيسة لالتهاب القصبات المزمن:",
   O(("Airway dilation", "توسّع المجرى الهوائي"), ("Mucus hypersecretion", "فرط إفراز المخاط"), ("Decreased airway resistance", "نقص مقاومة المجرى الهوائي"), ("Increased surfactant", "زيادة الفاعل بالسطح")), "b"),
 Q("The most common cause of lung cancer is:", "أشيع سبب لسرطان الرئة:",
   O(("Genetic factors", "عوامل وراثية"), ("Air pollution", "تلوّث الهواء"), ("Cigarette smoking", "تدخين السجائر"), ("Asbestos exposure", "التعرّض للأسبستوس")), "c"),
 W(Q("Which of the following is NOT a type of emphysema?", "أيّها ليس نوعًا من النُّفاخ الرئوي؟",
   O(("Centriacinar", "مركزي العُنيبة"), ("Panacinar", "شامل العُنيبة"), ("Irregular", "غير منتظم"), ("Bronchoacinar", "قصبي عُنيبي")), "d"),
   "The types are centriacinar, panacinar, paraseptal (distal acinar) and irregular; “bronchoacinar” is not a recognised type.", "الأنواع: مركزي وشامل العنيبة وقُربَ الحاجز (بعيد العنيبة) وغير منتظم؛ و«القصبي العنيبي» ليس نوعًا معروفًا."),
 Q("A characteristic feature of emphysema is:", "من السمات المميّزة للنُّفاخ الرئوي:",
   O(("Bronchial obstruction", "انسداد قصبي"), ("Permanent enlargement of airspaces", "توسّع دائم للحيّز الهوائي"), ("Increased mucus production", "زيادة إنتاج المخاط"), ("Reduced alveolar permeability", "نقص نفاذية السنخ")), "b"),
 Q("The histological hallmark of ARDS is:", "العلامة النسيجية المميّزة لـ ARDS:",
   O(("Alveolar hyperplasia", "فرط تنسّج سنخي"), ("Diffuse alveolar damage", "الأذى السنخي المنتشر"), ("Fibrosis of bronchioles", "تليّف القصيبات"), ("Loss of surfactant", "فقدان الفاعل بالسطح")), "b"),
 W(Q("Small cell lung cancer (SCLC) is best treated with:", "سرطان الرئة صغير الخلايا (SCLC) يُعالج أفضل بـ:",
   O(("Surgery", "الجراحة"), ("Chemotherapy", "العلاج الكيميائي"), ("Radiation alone", "الإشعاع وحده"), ("Immunotherapy only", "العلاج المناعي فقط")), "b"),
   "SCLC spreads early and is usually inoperable, so chemotherapy (± radiation) is the mainstay.", "ينتشر SCLC مبكرًا وغالبًا غير قابل للجراحة، فالعلاج الكيميائي (± الإشعاع) هو الأساس."),
 Q("Compression atelectasis is commonly caused by:", "الانخماص الانضغاطي غالبًا سببه:",
   O(("Blood or air in the pleural cavity", "دم أو هواء في التجويف الجنبي"), ("Airway obstruction", "انسداد المجرى الهوائي"), ("Bronchospasm", "تشنّج قصبي"), ("Lung infection", "عدوى الرئة")), "a"),
 Q("A typical feature of chronic bronchitis is:", "من السمات النموذجية لالتهاب القصبات المزمن:",
   O(("Hyperinflated alveoli", "أسناخ مفرطة الانتفاخ"), ("Productive cough for at least 3 months for 2 years", "سعال منتج لا يقلّ عن 3 أشهر خلال سنتين"), ("Alveolar shrinkage", "انكماش سنخي"), ("Absence of mucus production", "غياب إنتاج المخاط")), "b"),
 W(Q("The main histologic types of lung carcinoma include all EXCEPT:", "تشمل الأنواع النسيجية الرئيسة لسرطانة الرئة كلّ ما يلي عدا:",
   O(("Adenocarcinoma", "السرطانة الغدّية"), ("Squamous cell carcinoma", "السرطانة حرشفية الخلايا"), ("Large cell carcinoma", "السرطانة كبيرة الخلايا"), ("Sarcoma", "الساركوما (الورم اللحمي)")), "d"),
   "Lung carcinomas are epithelial (adeno, squamous, large cell, small cell); sarcoma is a mesenchymal tumour, not a carcinoma.", "سرطانات الرئة ظهارية (غدّية، حرشفية، كبيرة الخلايا، صغيرة الخلايا)؛ أما الساركوما فورم لُحمي (متوسّطي) لا سرطانة."),
 Q("Emphysema is more commonly associated with:", "يرتبط النُّفاخ الرئوي أكثر بـ:",
   O(("Persistent cough", "سعال مستمر"), ("Alveolar wall destruction", "تدمير جدار السنخ"), ("Reduced surfactant", "نقص الفاعل بالسطح"), ("Inflammation of large airways", "التهاب المجاري الهوائية الكبيرة")), "b"),
 Q("ARDS may lead to multi-organ failure because of:", "قد يؤدّي ARDS إلى فشل أعضاء متعدّد بسبب:",
   O(("Pulmonary infections", "عدوى رئوية"), ("Systemic hypoxemia", "نقص أكسجة الدم الجهازي"), ("Increased surfactant production", "زيادة إنتاج الفاعل بالسطح"), ("Bronchial hyperresponsiveness", "فرط استجابة القصبات")), "b"),
 Q("Which of the following is a predictor of poor prognosis in ARDS?", "أيّها مؤشّر على سوء الإنذار في ARDS؟",
   O(("Young age", "صغر السن"), ("Presence of sepsis", "وجود الإنتان"), ("Improved oxygen levels", "تحسّن مستويات الأكسجين"), ("Low heart rate", "بطء ضربات القلب")), "b"),
 Q("Lung cancer risk in non-smokers increases due to:", "يزداد خطر سرطان الرئة لدى غير المدخّنين بسبب:",
   O(("Poor diet", "سوء التغذية"), ("Passive smoking", "التدخين السلبي"), ("Low blood pressure", "انخفاض ضغط الدم"), ("High altitude", "الارتفاع العالي")), "b"),
 W(Q("Which lung cancer type has a strong correlation with smoking?", "أيّ نوع من سرطان الرئة له ارتباط قوي بالتدخين؟",
   O(("Adenocarcinoma", "السرطانة الغدّية"), ("Squamous cell carcinoma", "السرطانة حرشفية الخلايا"), ("Mesothelioma", "ورم المتوسّطة"), ("Hamartoma", "الورم العابي")), "b"),
   "Squamous cell (and small cell) carcinoma are strongly smoking-related; adenocarcinoma is the commonest type in non-smokers.", "السرطانة الحرشفية (وصغيرة الخلايا) شديدة الارتباط بالتدخين؛ أما الغدّية فأشيع نوع عند غير المدخّنين."),
 Q("Contraction atelectasis is primarily due to:", "الانخماص التقلّصي سببه الرئيس:",
   O(("Lung infection", "عدوى الرئة"), ("Fibrotic changes", "تغيّرات ليفية"), ("Dehydration", "التجفاف"), ("Mucus obstruction", "انسداد مخاطي")), "b"),
 Q("Chronic bronchitis often leads to:", "كثيرًا ما يؤدّي التهاب القصبات المزمن إلى:",
   O(("Hypocapnia", "نقص ثنائي أكسيد الكربون"), ("Hypercapnia and cyanosis", "فرط ثنائي أكسيد الكربون وازرقاق"), ("Decreased airway mucus", "نقص مخاط المجرى الهوائي"), ("Reduced cough", "نقص السعال")), "b"),
 W(Q("The typical age group affected by lung cancer is:", "الفئة العمرية النموذجية المصابة بسرطان الرئة:",
   O(("20s and 30s", "العشرينات والثلاثينات"), ("40s and 50s", "الأربعينات والخمسينات"), ("50s and 60s", "الخمسينات والستّينات"), ("70s and 80s", "السبعينات والثمانينات")), "c"),
   "The source wrote “blood group”, read here as age group — peak incidence is in the 50s–60s.", "كُتب في الأصل «blood group» والمقصود الفئة العمرية — وذروة الحدوث في الخمسينات والستّينات."),
 W(Q("Which type of emphysema causes airway obstruction?", "أيّ نوع من النُّفاخ يسبّب انسداد المجرى الهوائي؟",
   O(("Panacinar only", "شامل العنيبة فقط"), ("Centriacinar and Panacinar", "مركزي وشامل العنيبة"), ("Distal acinar only", "بعيد العنيبة فقط"), ("Irregular only", "غير المنتظم فقط")), "b"),
   "Centriacinar and panacinar emphysema are the clinically significant forms that cause airflow obstruction.", "النوعان مركزي وشامل العنيبة هما الشكلان المهمّان سريريًا المسبّبان لانسداد الجريان الهوائي."),
 Q("Major inflammatory cells in asthma include:", "تشمل الخلايا الالتهابية الرئيسة في الربو:",
   O(("Eosinophils and neutrophils", "الحمضات والعدلات"), ("Fibroblasts", "الأرومات الليفية"), ("Plasma cells", "الخلايا البلازمية"), ("Erythrocytes", "الكريات الحمر")), "a"),

 {"topic_en": "Exam 2 — Select the single best answer", "topic_ar": "الامتحان الثاني — اختر الإجابة الأفضل الوحيدة"},
 Q("What is the most common benign lung tumor?", "ما أشيع ورم رئوي حميد؟",
   O(("Adenoma", "الورم الغدّي"), ("Hamartoma", "الورم العابي (الهامارتوما)"), ("Leiomyoma", "الورم العضلي الأملس"), ("Lipoma", "الورم الشحمي")), "b"),
 Q("Which histologic type of lung cancer is most strongly associated with smoking?", "أيّ نوع نسيجي من سرطان الرئة الأشدّ ارتباطًا بالتدخين؟",
   O(("Adenocarcinoma", "السرطانة الغدّية"), ("Large cell carcinoma", "السرطانة كبيرة الخلايا"), ("Squamous cell carcinoma", "السرطانة حرشفية الخلايا"), ("Bronchioloalveolar carcinoma", "السرطانة القصيبية السنخية")), "c"),
 Q("The peak incidence of lung cancer is in persons in their:", "ذروة حدوث سرطان الرئة لدى الأشخاص في:",
   O(("30s and 40s", "الثلاثينات والأربعينات"), ("40s and 50s", "الأربعينات والخمسينات"), ("50s and 60s", "الخمسينات والستّينات"), ("70s and 80s", "السبعينات والثمانينات")), "c"),
 Q("What is the most common cause of resorption atelectasis?", "ما أشيع سبب للانخماص الامتصاصي؟",
   O(("Pleural effusion", "الانصباب الجنبي"), ("Mucous or mucopurulent plug", "سدادة مخاطية أو مخاطية قيحية"), ("Pneumothorax", "استرواح الصدر"), ("Tumor invasion", "الغزو الورمي")), "b"),
 Q("Which cell type is responsible for synthesizing pulmonary surfactant?", "أيّ نوع خلوي مسؤول عن تصنيع الفاعل بالسطح الرئوي؟",
   O(("Type I pneumocyte", "الخلية الرئوية النوع الأول"), ("Type II pneumocyte", "الخلية الرئوية النوع الثاني"), ("Alveolar macrophage", "البلعم السنخي"), ("Endothelial cell", "الخلية البطانية")), "b"),
 Q("The histologic manifestation of ARDS in the lungs is known as:", "يُعرف التظاهر النسيجي لـ ARDS في الرئة بـ:",
   O(("Centrilobular necrosis", "التنخّر المركزي الفصيصي"), ("Diffuse alveolar damage (DAD)", "الأذى السنخي المنتشر (DAD)"), ("Bronchial metaplasia", "الحؤول القصبي"), ("Granuloma formation", "تكوّن الورم الحبيبي")), "b"),
 Q("Which of the following is a characteristic feature of chronic bronchitis?", "أيّها سمة مميّزة لالتهاب القصبات المزمن؟",
   O(("Decreased Reid index", "نقص مشعر ريد"), ("Hypertrophy of mucous glands", "تضخّم الغدد المخاطية"), ("Reduced number of goblet cells", "نقص عدد الخلايا الكأسية"), ("Decreased mucus production", "نقص إنتاج المخاط")), "b"),
 W(Q("The most common primary glomerular disease in adults causing nephrotic syndrome is:", "أشيع مرض كبيبي أولي عند البالغين يسبّب المتلازمة الكلائية:",
   O(("Minimal change disease", "داء التغيّر الأدنى"), ("Focal segmental glomerulosclerosis (FSGS)", "التصلّب الكبيبي البؤري القطعي (FSGS)"), ("Membranous glomerulonephritis", "التهاب الكبيبات الغشائي"), ("IgA nephropathy", "اعتلال IgA")), "c"),
   "Per the lecture, membranous GN (~40%) is the commonest cause of nephrotic syndrome in adults (minimal change is commonest in children).", "حسب المحاضرة، التهاب الكبيبات الغشائي (~40%) أشيع سبب للمتلازمة الكلائية عند البالغين (وداء التغيّر الأدنى أشيعها عند الأطفال)."),
 Q("Which cytokine is primarily responsible for activating eosinophils in asthma?", "أيّ سيتوكين مسؤول رئيسيًا عن تنشيط الحمضات في الربو؟",
   O(("IL-4", "إنترلوكين 4"), ("IL-5", "إنترلوكين 5"), ("IL-13", "إنترلوكين 13"), ("IFN-gamma", "إنترفيرون غاما")), "b"),
 Q("Atelectasis that occurs due to generalized fibrotic changes in the lung is called:", "الانخماص الناتج عن تغيّرات ليفية معمّمة في الرئة يُسمّى:",
   O(("Resorption atelectasis", "الانخماص الامتصاصي"), ("Compression atelectasis", "الانخماص الانضغاطي"), ("Contraction atelectasis", "الانخماص التقلّصي"), ("Relaxation atelectasis", "الانخماص الارتخائي")), "c"),
]

important = [
 IM("The functional unit of the kidney is the ______.", "الوحدة الوظيفية للكلية هي ______.", "The nephron.", "النفرون (الوحدة الكلوية)."),
 IM("Atelectasis can be classified into resorption, compression, and ______ atelectasis.", "يُصنّف الانخماص إلى امتصاصي وانضغاطي و______.", "Contraction atelectasis.", "الانخماص التقلّصي."),
 IM("The most common benign lung tumor is ______.", "أشيع ورم رئوي حميد هو ______.", "Hamartoma.", "الورم العابي (الهامارتوما)."),
 IM("In asthma, IL-5 is responsible for activating ______.", "في الربو، الإنترلوكين 5 مسؤول عن تنشيط ______.", "Eosinophils.", "الحمضات (اليوزينوفيلات)."),
 IM("The diagnosis of chronic bronchitis requires a persistent productive cough for at least ______ consecutive months in at least 2 consecutive years.", "يتطلّب تشخيص التهاب القصبات المزمن سعالًا منتجًا مستمرًّا لا يقلّ عن ______ أشهر متتالية في سنتين متتاليتين على الأقل.", "3 (three) months.", "ثلاثة (3) أشهر."),
 IM("The major function of the lung is to replenish ______ and excrete carbon dioxide.", "الوظيفة الرئيسة للرئة هي تجديد ______ وطرح ثنائي أكسيد الكربون.", "Oxygen.", "الأكسجين."),
 IM("The two main phases of an asthma attack are the early phase and the ______ phase.", "الطوران الرئيسان لنوبة الربو هما الطور المبكّر والطور ______.", "The late phase.", "المتأخّر."),
 IM("______ is characterized by abnormal permanent enlargement of the air spaces distal to the terminal bronchioles.", "______ يتميّز بتوسّع دائم غير طبيعي للحيّزات الهوائية البعيدة عن القصيبات الانتهائية.", "Emphysema.", "النُّفاخ الرئوي."),
 IM("The key reason for distinguishing small cell lung cancer from non-small cell lung cancer is that SCLC is often not curable by ______.", "السبب الجوهري للتمييز بين سرطان الرئة صغير الخلايا وغير صغير الخلايا هو أن صغير الخلايا غالبًا غير قابل للشفاء بـ______.", "Surgery.", "الجراحة."),
 IM("The clinical syndrome of Acute Lung Injury requires the absence of clinical evidence of primary ______ heart failure.", "تتطلّب متلازمة الأذى الرئوي الحاد غياب دليل سريري على قصور القلب ______ الأولي.", "Left-sided (left).", "الأيسر."),
]

meta = {"subject_en": "Pathology", "subject_ar": "علم الأمراض", "short_ar": "أمراض", "instructor": "د. حامد خليل التميمي",
        "unit_en": "Golden Exam", "unit_ar": "الصمونة الذهبية", "unit_label": "PATH", "unit_no": "G",
        "title_en": "The Golden Loaf — Solved Pathology Exam", "title_ar": "الصمونة الذهبية — امتحان علم الأمراض محلولًا",
        "kind": "Theory — نظري", "stage": "The fourth stage — الرابعة",
        "file_name": "BIOS - أمراض نظري - الصمونة الذهبية (امتحان محلول)"}

Qs = {"title_en": "The Golden Loaf — Solved Pathology Exam", "title_ar": "الصمونة الذهبية — امتحان علم الأمراض محلولًا",
      "sub": "Solved", "answers_inline": True, "compact": True, "mcq_per_page": 5,
      "mcq_en": "Multiple-choice questions (with answers)", "mcq_ar": "أسئلة الاختيار من متعدّد (مع الحلول)",
      "mcq": ltr_all(mcq), "tf": [], "traps": [], "important": ltr_all(important)}
d = "/home/user/-/" + FOLDER
os.makedirs(d, exist_ok=True)
json.dump({"meta": meta, "questions": Qs}, open(d + "/lecture.json", "w"), ensure_ascii=False, indent=1)
from collections import Counter
qs = [m for m in mcq if "answer" in m]
print(FOLDER, len(qs), "MCQ", dict(sorted(Counter(m["answer"] for m in qs).items())), "| SA:", len(important), "| notes:", sum(1 for m in qs if m.get("note_en")))

```
