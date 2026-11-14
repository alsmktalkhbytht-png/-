import sys, json, os, random
sys.path.insert(0, "/tmp/claude-0/-home-user/bbbdedfa-3c9f-5150-ab3b-e66c0ade12b5/scratchpad/work/imm456")
from ci import *            # Q P IM
sys.path.insert(0, "/tmp/claude-0/-home-user/bbbdedfa-3c9f-5150-ab3b-e66c0ade12b5/scratchpad/work"); from bidi import ltr_all

# Principles of Research — Lecture 2 "Scientific Method" (stage 4, ليندا منجد هادي).
# Source: the professor's own MCQ file (5 pages, 23 Q, correct answer in bold). QUESTIONS ONLY —
# arranged BIOS-style: every option translated, answer under each (answers_inline), 4 Q per page. No invented SA.
# The professor's double colons ("::") in the stems of Q13/Q20/Q23 are rendered as a single colon; wording kept verbatim.
O = P
FOLDER = "research-lec2-scientific-method-mcq"
W = lambda q, en, ar: dict(q, note_en=en, note_ar=ar)

def balance5(mcq, seed=7):
    rnd = random.Random(seed); L = "abcde"
    qs = [q for q in mcq if "answer" in q]
    seq = []
    while len(seq) < len(qs):
        b = list("abcde"); rnd.shuffle(b); seq += b
    for q, t in zip(qs, seq):
        n = len(q["options"]); i = L.index(q["answer"]); j = min(L.index(t), n - 1)
        q["options"][i], q["options"][j] = q["options"][j], q["options"][i]
        q["answer"] = L[j]
    return mcq

mcq = [
 Q("What is definition of the scientific method:", "ما تعريف المنهج العلمي:",
   O(("A systematic, evidence-based approach to investigate questions and develop conclusions from measurable data", "منهج منظّم قائم على الأدلّة للتحرّي عن الأسئلة وتطوير الاستنتاجات من بيانات قابلة للقياس"),
     ("A fixed set of rules used only in laboratory experiments", "مجموعة قواعد ثابتة تُستعمل فقط في التجارب المختبرية"),
     ("A method for confirming existing beliefs through selected observations", "طريقة لتأكيد المعتقدات القائمة عبر ملاحظات منتقاة"),
     ("A statistical technique used to prove that a hypothesis is true", "تقنية إحصائية تُستعمل لإثبات أن الفرضية صحيحة"),
     ("A process that relies primarily on expert opinion", "عملية تعتمد أساسًا على رأي الخبير")), "a"),
 Q("Which feature means that scientific conclusions depend on collected observations or measurements:", "أيّ صفة تعني أن الاستنتاجات العلمية تعتمد على ملاحظات أو قياسات مجموعة:",
   O(("Empirical", "تجريبي (قائم على المشاهدة)"),
     ("Objective", "موضوعي"),
     ("Reproducible", "قابل للتكرار"),
     ("Transparent", "شفّاف"),
     ("Self-correcting", "ذاتي التصحيح")), "a"),
 Q("Why is a scientific approach useful when investigating a laboratory problem:", "لماذا يكون المنهج العلمي مفيدًا عند التحرّي عن مشكلة مختبرية:",
   O(("It helps define questions and procedures so evidence and conclusions can be evaluated by others", "يساعد على تحديد الأسئلة والإجراءات كي يتمكّن الآخرون من تقييم الأدلّة والاستنتاجات"),
     ("It removes the need to define variables", "يُلغي الحاجة إلى تعريف المتغيّرات"),
     ("It guarantees that every result will be statistically significant", "يضمن أن تكون كل نتيجة ذات دلالة إحصائية"),
     ("It makes results independent of measurement procedures", "يجعل النتائج مستقلّة عن إجراءات القياس"),
     ("It prevents new evidence from changing earlier explanations", "يمنع الأدلّة الجديدة من تغيير التفسيرات السابقة")), "a"),
 Q("Which characteristic of scientific investigation aims to minimize personal bias:", "أيّ خاصّية من خصائص التحرّي العلمي تهدف إلى تقليل التحيّز الشخصي:",
   O(("Objective", "موضوعي"),
     ("Empirical", "تجريبي (قائم على المشاهدة)"),
     ("Testable", "قابل للاختبار"),
     ("Controlled", "مضبوط (محكوم)"),
     ("Reproducible", "قابل للتكرار")), "a"),
 Q("Which sequence best represents the major steps of the scientific method:", "أيّ تسلسل يمثّل أفضل الخطوات الرئيسة للمنهج العلمي:",
   O(("Observation/problem, research question, background research, hypothesis, design, data collection, analysis, conclusion, communication", "الملاحظة/المشكلة، سؤال البحث، البحث الخلفي، الفرضية، التصميم، جمع البيانات، التحليل، الاستنتاج، التواصل"),
     ("Hypothesis, conclusion, observation, communication, data collection", "الفرضية، الاستنتاج، الملاحظة، التواصل، جمع البيانات"),
     ("Research question, data collection, hypothesis, observation, conclusion, study design", "سؤال البحث، جمع البيانات، الفرضية، الملاحظة، الاستنتاج، تصميم الدراسة"),
     ("Study design, communication, observation, background research, analysis, hypothesis", "تصميم الدراسة، التواصل، الملاحظة، البحث الخلفي، التحليل، الفرضية"),
     ("Observation, statistical test, publication, hypothesis, research question", "الملاحظة، الاختبار الإحصائي، النشر، الفرضية، سؤال البحث")), "a"),
 Q("A laboratory finds that delayed plasma samples have lower glucose readings. What is the observation:", "يجد مختبر أن عيّنات البلازما المتأخّرة تعطي قراءات غلوكوز أقل. ما الملاحظة:",
   O(("A directly recorded finding that delayed samples give lower glucose readings", "نتيجة مسجَّلة مباشرةً مفادها أن العيّنات المتأخّرة تعطي قراءات غلوكوز أقل"),
     ("The effect of delay is uncertain", "تأثير التأخير غير مؤكّد"),
     ("A defined issue requiring investigation", "مشكلة محدّدة تتطلّب تحرّيًا"),
     ("The hypothesis that delay decreases glucose", "الفرضية القائلة إن التأخير يخفض الغلوكوز"),
     ("The conclusion that all glucose samples must be processed immediately", "الاستنتاج القائل إن كل عيّنات الغلوكوز يجب معالجتها فورًا")), "a"),
 Q("Which research question is most clearly measurable and focused:", "أيّ سؤال بحثي هو الأوضح قابليةً للقياس والأكثر تركيزًا:",
   O(("Does a 2-hour delay before plasma separation change measured glucose concentration?", "هل يغيّر تأخيرٌ مدّته ساعتان قبل فصل البلازما تركيزَ الغلوكوز المقاس؟"),
     ("Why is glucose important?", "لماذا الغلوكوز مهمّ؟"),
     ("Do laboratory delays cause problems?", "هل تسبّب تأخيرات المختبر مشكلات؟"),
     ("What happens to samples over time?", "ماذا يحدث للعيّنات مع مرور الوقت؟"),
     ("Are delayed samples worse than other samples?", "هل العيّنات المتأخّرة أسوأ من العيّنات الأخرى؟")), "a"),
 Q("What is a key purpose of conducting a literature review before a study:", "ما الغرض الأساس من إجراء مراجعة الأدبيات قبل الدراسة:",
   O(("To avoid unnecessary duplication and identify gaps or limitations in prior evidence", "لتجنّب التكرار غير الضروري وتحديد الفجوات أو حدود الأدلّة السابقة"),
     ("To guarantee the study will confirm its hypothesis", "لضمان أن تؤكّد الدراسة فرضيتها"),
     ("To replace the need for an experimental design", "للاستغناء عن الحاجة إلى تصميم تجريبي"),
     ("To select only sources that support the expected result", "لانتقاء المصادر التي تدعم النتيجة المتوقّعة فقط"),
     ("To determine the final conclusion before collecting data", "لتحديد الاستنتاج النهائي قبل جمع البيانات")), "a"),
 Q("Which statement best describes a hypothesis:", "أيّ عبارة تصف الفرضية أفضل وصف:",
   O(("A specific, testable statement about an expected relationship or difference between variables", "عبارة محدّدة قابلة للاختبار حول علاقة أو فرق متوقَّع بين المتغيّرات"),
     ("A broad topic area chosen for investigation", "مجال موضوعي واسع يُختار للتحرّي"),
     ("A summary of the results after statistical analysis", "ملخّص للنتائج بعد التحليل الإحصائي"),
     ("A procedure for controlling laboratory quality", "إجراء لضبط جودة المختبر"),
     ("A statement that cannot be changed by new evidence", "عبارة لا يمكن تغييرها بأدلّة جديدة")), "a"),
 Q("In a study of processing delay and glucose concentration, which is the independent variable:", "في دراسة عن تأخير المعالجة وتركيز الغلوكوز، أيّها المتغيّر المستقل:",
   O(("Processing delay", "تأخير المعالجة"),
     ("Glucose concentration", "تركيز الغلوكوز"),
     ("Tube type", "نوع الأنبوب"),
     ("Analyser", "جهاز التحليل"),
     ("Temperature", "درجة الحرارة")), "a"),
 Q("In the same study, which is the dependent variable:", "في الدراسة نفسها، أيّها المتغيّر التابع:",
   O(("Glucose concentration", "تركيز الغلوكوز"),
     ("Processing delay", "تأخير المعالجة"),
     ("Tube type", "نوع الأنبوب"),
     ("Temperature", "درجة الحرارة"),
     ("Sample identifier", "معرّف العيّنة")), "a"),
 Q("How does a study design relate to the scientific method:", "كيف يرتبط تصميم الدراسة بالمنهج العلمي:",
   O(("The scientific method guides the investigation, while study design specifies how evidence will be obtained", "المنهج العلمي يوجّه التحرّي، بينما يحدّد تصميم الدراسة كيف ستُجمع الأدلّة"),
     ("The study design is the broad framework for reasoning, while the scientific method is the specific evidence collection plan", "تصميم الدراسة هو الإطار العام للاستدلال، بينما المنهج العلمي هو خطة جمع الأدلّة المحدّدة"),
     ("They are identical terms for statistical analysis", "هما مصطلحان متطابقان للتحليل الإحصائي"),
     ("Study design is used only after a conclusion is reached", "لا يُستعمل تصميم الدراسة إلا بعد الوصول إلى استنتاج"),
     ("The scientific method applies only to experimental studies", "ينطبق المنهج العلمي على الدراسات التجريبية فقط")), "a"),
 Q("Which practice supports reliable data collection:", "أيّ ممارسة تدعم جمع بيانات موثوق:",
   O(("Use standardized procedures, defined units, and record missing data or protocol deviations", "استعمال إجراءات موحّدة ووحدات محدّدة، وتسجيل البيانات الناقصة أو انحرافات البروتوكول"),
     ("Use different procedures for each sample to explore variation", "استعمال إجراءات مختلفة لكل عيّنة لاستكشاف التباين"),
     ("Record only results that match the hypothesis", "تسجيل النتائج التي تطابق الفرضية فقط"),
     ("Avoid coded identifiers so samples are easier to recognize", "تجنّب المعرّفات المرمّزة كي يسهل التعرّف على العيّنات"),
     ("Skip calibration if the analyzer has recently been serviced", "تخطّي المعايرة إذا كان جهاز التحليل قد صيِّن حديثًا")), "a"),
 Q("What is the difference between data analysis and interpretation:", "ما الفرق بين تحليل البيانات وتفسيرها:",
   O(("Analysis organises and summarises data; interpretation relates findings to the question and considers relevance and limitations", "التحليل ينظّم البيانات ويلخّصها؛ أما التفسير فيربط النتائج بالسؤال ويراعي الصلة والحدود"),
     ("Analysis assesses clinical relevance; interpretation calculates raw measurements only", "التحليل يقيّم الصلة السريرية؛ والتفسير يحسب القياسات الخام فقط"),
     ("Analysis and interpretation are unrelated steps", "التحليل والتفسير خطوتان غير مترابطتين"),
     ("Interpretation must occur before data are collected", "يجب أن يحدث التفسير قبل جمع البيانات"),
     ("Analysis proves whether a hypothesis is true", "التحليل يثبت ما إذا كانت الفرضية صحيحة")), "a"),
 Q("Which conclusion is scientifically appropriate:", "أيّ استنتاج هو المناسب علميًا:",
   O(("A conclusion that matches the strength and scope of the evidence and reports important limitations", "استنتاج يتناسب مع قوّة الأدلّة ونطاقها ويذكر الحدود المهمّة"),
     ("A conclusion that generalizes to every population regardless of the study sample", "استنتاج يُعمَّم على كل المجتمعات بغضّ النظر عن عيّنة الدراسة"),
     ("A conclusion that omits alternative explanations", "استنتاج يُغفل التفسيرات البديلة"),
     ("A conclusion that states the hypothesis was proven", "استنتاج يذكر أن الفرضية قد أُثبِتت"),
     ("A conclusion based only on expected results", "استنتاج مبني على النتائج المتوقّعة فقط")), "a"),
 Q("Why should researchers report unexpected or negative findings:", "لماذا ينبغي للباحثين الإبلاغ عن النتائج غير المتوقّعة أو السلبية:",
   O(("They help provide a complete, transparent record that others can evaluate and reproduce", "لأنها تساعد على تقديم سجلّ كامل وشفّاف يمكن للآخرين تقييمه وإعادة إنتاجه"),
     ("They should be reported only when they support the hypothesis", "ينبغي الإبلاغ عنها فقط حين تدعم الفرضية"),
     ("They make further analysis unnecessary", "لأنها تجعل المزيد من التحليل غير ضروري"),
     ("They prove that the study design was invalid", "لأنها تثبت أن تصميم الدراسة كان غير صحيح"),
     ("They are relevant only to commercial studies", "لأنها ذات صلة بالدراسات التجارية فقط")), "a"),
 Q("Which statement about good study design and statistical analysis is correct:", "أيّ عبارة صحيحة عن تصميم الدراسة الجيّد والتحليل الإحصائي:",
   O(("Good design reduces avoidable error, and analysis cannot repair every design problem", "التصميم الجيّد يقلّل الخطأ القابل للتجنّب، والتحليل لا يمكنه إصلاح كل مشكلة تصميم"),
     ("Statistical analysis can repair every design problem", "يمكن للتحليل الإحصائي إصلاح كل مشكلة تصميم"),
     ("Confounding is irrelevant when sample size is large", "الإرباك (التشويش) غير ذي صلة عندما يكون حجم العيّنة كبيرًا"),
     ("Random error is eliminated by transparent reporting", "يُزال الخطأ العشوائي بالإبلاغ الشفّاف"),
     ("Study design has no effect on validity", "تصميم الدراسة لا أثر له في الصدقية (الصحّة)")), "a"),
 Q("In an ELISA wash-step study, what should be evaluated:", "في دراسة لخطوة الغسل في إليزا (ELISA)، ما الذي ينبغي تقييمه:",
   O(("Both background or negative-control absorbance and the expected positive signal against predefined criteria", "امتصاص الخلفية أو الشاهد السالب والإشارة الموجبة المتوقّعة معًا، مقابل معايير محدّدة سلفًا"),
     ("Only whether background absorbance decreases", "ما إذا كان امتصاص الخلفية ينخفض فقط"),
     ("Only whether the positive signal increases", "ما إذا كانت الإشارة الموجبة تزداد فقط"),
     ("Whether the hypothesis is accepted before collecting data", "ما إذا كانت الفرضية مقبولة قبل جمع البيانات"),
     ("Whether all controls can be removed", "ما إذا كان يمكن إزالة كل الشواهد")), "a"),
 Q("Which action best protects scientific integrity:", "أيّ إجراء يحمي النزاهة العلمية أفضل حماية:",
   O(("Report protocol deviations and limitations transparently and do not alter or selectively remove data", "الإبلاغ الشفّاف عن انحرافات البروتوكول والحدود، وعدم تغيير البيانات أو إزالتها انتقائيًا"),
     ("Remove data points that weaken the hypothesis without explanation", "إزالة نقاط بيانات تُضعف الفرضية دون تفسير"),
     ("Report only statistically significant outcomes", "الإبلاغ عن النتائج ذات الدلالة الإحصائية فقط"),
     ("Fabricate missing values to complete the dataset", "اختلاق قيم مفقودة لإكمال مجموعة البيانات"),
     ("Keep methods confidential so others cannot challenge the findings", "إبقاء الطرائق سرّية كي لا يتمكّن الآخرون من الطعن في النتائج")), "a"),
 Q("Which is an appropriate role for AI in scientific research:", "أيّها دور مناسب للذكاء الاصطناعي في البحث العلمي:",
   O(("It can support tasks such as literature organisation or code assistance, while researchers verify sources, data, assumptions, and claims", "يمكنه دعم مهام مثل تنظيم الأدبيات أو المساعدة البرمجية، بينما يتحقّق الباحثون من المصادر والبيانات والافتراضات والادّعاءات"),
     ("Its output can serve as scientific evidence without validation", "يمكن أن تُستعمل مُخرَجاته دليلًا علميًا دون تحقّق"),
     ("It removes researcher responsibility for confidentiality", "يُلغي مسؤولية الباحث عن السرّية"),
     ("It should independently determine whether results are valid", "ينبغي أن يحدّد باستقلالية ما إذا كانت النتائج صحيحة"),
     ("It makes ethical review unnecessary", "يجعل المراجعة الأخلاقية غير ضرورية")), "a"),
 Q("How should an AI system intended to flag blood-smear images for expert review be evaluated:", "كيف ينبغي تقييم نظام ذكاء اصطناعي مُعدّ لتأشير صور لطاخة الدم لمراجعة الخبير:",
   O(("Compare it with an expert reference on separate patients and assess appropriate performance measures and errors", "مقارنته بمرجع خبير على مرضى منفصلين، وتقييم مقاييس الأداء المناسبة والأخطاء"),
     ("Test it only on the training data and report accuracy", "اختباره على بيانات التدريب فقط والإبلاغ عن الدقّة"),
     ("Ask the AI system whether its predictions are reliable", "سؤال نظام الذكاء الاصطناعي عمّا إذا كانت تنبّؤاته موثوقة"),
     ("Use only images that were correctly classified previously", "استعمال الصور التي صُنِّفت سابقًا تصنيفًا صحيحًا فقط"),
     ("Evaluate writing quality instead of diagnostic performance", "تقييم جودة الكتابة بدلًا من الأداء التشخيصي")), "a"),
 Q("Which performance measures may be relevant when evaluating an AI tool for blood-smear review:", "أيّ مقاييس أداء قد تكون ذات صلة عند تقييم أداة ذكاء اصطناعي لمراجعة لطاخة الدم:",
   O(("Sensitivity, specificity, missed cases, calibration, and review time, depending on intended use", "الحساسية والنوعية والحالات الفائتة والمعايرة وزمن المراجعة، تبعًا للاستعمال المقصود"),
     ("Only the number of images processed", "عدد الصور المعالَجة فقط"),
     ("Only statistical significance of the training results", "الدلالة الإحصائية لنتائج التدريب فقط"),
     ("The number of keywords suggested by the model", "عدد الكلمات المفتاحية التي يقترحها النموذج"),
     ("Only agreement with its own previous output", "التوافق مع مُخرَجاته السابقة فقط")), "a"),
 Q("Which statement best summarizes the scientific conclusions:", "أيّ عبارة تلخّص الاستنتاجات العلمية أفضل تلخيص:",
   O(("A conclusion should answer the question using evidence while acknowledging uncertainty, limitations, and scope", "ينبغي أن يجيب الاستنتاج عن السؤال بالاستناد إلى الأدلّة، مع الإقرار بعدم اليقين والحدود والنطاق"),
     ("Conclusions should go beyond the data to maximize impact", "ينبغي أن تتجاوز الاستنتاجات البيانات لتعظيم الأثر"),
     ("A strong hypothesis is sufficient to establish causation", "الفرضية القوية كافية لإثبات السببية"),
     ("A well-designed study does not need transparent reporting", "الدراسة جيّدة التصميم لا تحتاج إلى إبلاغ شفّاف"),
     ("AI-generated conclusions do not require verification", "الاستنتاجات المولّدة بالذكاء الاصطناعي لا تحتاج إلى تحقّق")), "a"),
]
mcq = balance5(mcq, 222)

meta = {"subject_en": "Principles of Research", "subject_ar": "مبادئ البحث العلمي", "short_ar": "مبادئ البحث", "instructor": "ليندا منجد هادي",
        "unit_en": "Lecture 2", "unit_ar": "المحاضرة 2", "unit_label": "LEC", "unit_no": "2",
        "title_en": "Scientific Method", "title_ar": "المنهج العلمي",
        "kind": "Theory — نظري", "stage": "The fourth stage — الرابعة",
        "file_name": "BIOS - مبادئ البحث نظري المحاضرة الثانية - الأسئلة"}

Qs = {"title_en": "Scientific Method (Lecture 2) — MCQs", "title_ar": "المنهج العلمي (المحاضرة الثانية) — أسئلة اختيار من متعدّد",
      "sub": "MCQs", "answers_inline": True, "mcq_per_page": 4, "compact": True,
      "mcq_en": "Multiple-choice questions", "mcq_ar": "أسئلة الاختيار من متعدّد",
      "mcq": ltr_all(mcq), "tf": [], "traps": [], "important": []}
d = "/home/user/-/" + FOLDER
os.makedirs(d, exist_ok=True)
json.dump({"meta": meta, "questions": Qs}, open(d + "/lecture.json", "w"), ensure_ascii=False, indent=1)
from collections import Counter
qs = [m for m in mcq if "answer" in m]
print(FOLDER, len(qs), "MCQ", dict(sorted(Counter(m["answer"] for m in qs).items())), "| notes:", sum(1 for m in qs if m.get("note_en")))
