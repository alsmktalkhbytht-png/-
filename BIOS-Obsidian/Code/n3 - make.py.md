---
source: BIOS-Obsidian/tools/scripts/n3/make.py
handouts: [research-lec2-scientific-method]
saved: 2026-10-29
tags: [bios, code]
---
# n3/make.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#research-lec2-scientific-method|research-lec2-scientific-method]]

```python
import json
from collections import Counter
def C(en, ar, **k): return dict(t="card", en=en, ar=ar, **k)
def SEC(en, ar): return dict(t="section", en=en, ar=ar)
def H2(en, ar): return dict(t="h2", en=en, ar=ar)
def G(te, ta, en, ar, **k): return dict(t="group", title_en=te, title_ar=ta, en=en, ar=ar, **k)
def L(en_items, ar_items, en="", ar="", **k): return dict(t="card", en=en, ar=ar, list_en=en_items, list_ar=ar_items, **k)
def N(en, ar, label=None):
    b = dict(t="note", en=en, ar=ar)
    if label: b["label"] = label
    return b

blocks = [
 SEC("Learning Outcomes", "مخرجات التعلّم"),
 L(["Define the scientific method and explain its importance.",
    "Describe the major characteristics and steps of scientific investigation.",
    "Differentiate research questions, hypotheses, variables, and controls.",
    "Explain how data are collected, analysed, interpreted, and communicated.",
    "Apply the scientific method to common medical laboratory problems.",
    "Recognise the role and limitations of artificial intelligence in scientific research."],
   ["تعريف المنهج العلمي وشرح أهميته.",
    "وصف الخصائص والخطوات الرئيسة للاستقصاء العلمي.",
    "التمييز بين أسئلة البحث والفرضيات والمتغيّرات والضوابط.",
    "شرح كيفية جمع البيانات وتحليلها وتفسيرها ونشرها.",
    "تطبيق المنهج العلمي على المشكلات الشائعة في المختبرات الطبية.",
    "إدراك دور الذكاء الاصطناعي وحدوده في البحث العلمي."]),

 SEC("Definition of the Scientific Method", "تعريف المنهج العلمي"),
 C("**The scientific method is a systematic and evidence-based approach used to investigate scientific questions, test hypotheses, and develop conclusions from observable and measurable data.**",
   "**المنهج العلمي نهج منظّم قائم على الأدلة، يُستخدم لاستقصاء الأسئلة العلمية واختبار الفرضيات والوصول إلى استنتاجات من بيانات قابلة للملاحظة والقياس.**"),
 L(["**Systematic**: follows an organised process.", "**Evidence-based**: conclusions depend on collected data.",
    "**Testable**: proposed explanations can be examined.", "**Self-correcting**: new evidence may modify previous explanations."],
   ["**منظّم**: يتّبع عملية مرتّبة.", "**قائم على الأدلة**: تعتمد الاستنتاجات على البيانات المجموعة.",
    "**قابل للاختبار**: يمكن فحص التفسيرات المقترحة.", "**ذاتي التصحيح**: قد تعدّل الأدلة الجديدة التفسيرات السابقة."]),

 SEC("Why Is the Scientific Method Important?", "لماذا المنهج العلمي مهم؟"),
 L(["Observations may be interpreted subjectively.", "Confounding factors may be ignored.", "Results may be difficult to verify or reproduce."],
   ["قد تُفسَّر الملاحظات تفسيرًا ذاتيًا.", "قد تُهمَل العوامل المربكة (المتداخلة).", "قد يصعب التحقّق من النتائج أو تكرارها."], en="**Without a scientific approach**", ar="**من دون نهج علمي**"),
 L(["Questions are defined clearly.", "Variables and procedures are specified.", "Evidence is collected systematically.", "Conclusions can be evaluated by others."],
   ["تُحدَّد الأسئلة بوضوح.", "تُحدَّد المتغيّرات والإجراءات.", "تُجمع الأدلة بشكل منظّم.", "يمكن للآخرين تقييم الاستنتاجات."], en="**With a scientific approach**", ar="**مع النهج العلمي**"),

 SEC("Characteristics of Scientific Investigation", "خصائص الاستقصاء العلمي"),
 L(["**Objective** — aims to minimise personal bias.", "**Empirical** — based on observation or measurement.",
    "**Testable** — hypotheses can be examined using evidence.", "**Controlled** — relevant conditions are managed when possible.",
    "**Reproducible** — methods are described sufficiently for independent repetition.", "**Transparent** — methods, results, and limitations are reported clearly."],
   ["**موضوعي** — يهدف إلى تقليل التحيّز الشخصي.", "**تجريبي (إمبريقي)** — يقوم على الملاحظة أو القياس.",
    "**قابل للاختبار** — يمكن فحص الفرضيات باستخدام الأدلة.", "**مضبوط** — تُدار الظروف ذات الصلة متى أمكن.",
    "**قابل للتكرار** — تُوصف الطرائق بما يكفي لتكرارها بشكل مستقل.", "**شفّاف** — تُعرض الطرائق والنتائج والقيود بوضوح."]),

 SEC("Major Steps of the Scientific Method", "الخطوات الرئيسة للمنهج العلمي"),
 dict(t="table", head=["", "Step", "الخطوة"], ar_cols=[2], key_cols=[1], numbered=True, widths=["12mm", "", ""],
      rows=[["1", "Observation / Problem", "الملاحظة / المشكلة"], ["2", "Research Question", "سؤال البحث"], ["3", "Background Research", "البحث في الخلفية العلمية"],
            ["4", "Hypothesis", "الفرضية"], ["5", "Study / Experiment Design", "تصميم الدراسة / التجربة"], ["6", "Data Collection", "جمع البيانات"],
            ["7", "Analysis & Interpretation", "التحليل والتفسير"], ["8", "Conclusion", "الاستنتاج"], ["9", "Communication", "النشر (التواصل)"]]),
 N("*The process is iterative: findings may generate new questions or require revision of earlier steps.*",
   "*العملية تكرارية: قد تولّد النتائج أسئلة جديدة أو تتطلّب مراجعة خطوات سابقة.*", label=["Note", "ملاحظة"]),

 SEC("1. Observation and Problem Identification", "1. الملاحظة وتحديد المشكلة"),
 G("Observation", "الملاحظة",
   ["A directly recorded or measured finding.", "Example: A delayed plasma sample gives a lower glucose result than a promptly processed sample."],
   ["نتيجة تُسجَّل أو تُقاس مباشرة.", "مثال: عيّنة بلازما متأخّرة تعطي نتيجة كلوكوز أقل من عيّنة عولجت فورًا."]),
 G("Scientific Problem", "المشكلة العلمية",
   ["A defined issue that requires explanation or investigation.", "Example: The effect of processing delay on measured glucose is uncertain."],
   ["قضية محدّدة تتطلّب تفسيرًا أو استقصاءً.", "مثال: تأثير التأخير في المعالجة على الكلوكوز المقاس غير مؤكّد."]),

 SEC("2. Formulating the Research Question", "2. صياغة سؤال البحث"),
 C("**A research question converts a broad problem into a specific question that can be investigated.**",
   "**يحوّل سؤال البحث مشكلة واسعة إلى سؤال محدّد يمكن استقصاؤه.**"),
 L(["**Clear** — uses precise scientific terms.", "**Focused** — addresses a defined problem or relationship.",
    "**Measurable** — includes outcomes that can be observed or quantified.", "**Feasible** — can be studied with available participants, samples, time, and methods."],
   ["**واضح** — يستخدم مصطلحات علمية دقيقة.", "**مركّز** — يعالج مشكلة أو علاقة محدّدة.",
    "**قابل للقياس** — يتضمّن نتائج يمكن ملاحظتها أو قياسها كمّيًا.", "**ممكن التنفيذ** — يمكن دراسته بالمشاركين والعيّنات والوقت والطرائق المتاحة."]),
 N("Example: Does a 2-hour delay before plasma separation change measured glucose concentration?",
   "مثال: هل يغيّر التأخير ساعتين قبل فصل البلازما تركيزَ الكلوكوز المقاس؟", label=["Example", "مثال"]),

 SEC("3. Background Research and Literature Review", "3. البحث في الخلفية ومراجعة الأدبيات"),
 L(["Determine what is already known about the problem.", "Identify gaps, disagreements, and limitations in previous evidence.",
    "Refine the research question and select appropriate methods.", "Avoid unnecessary duplication of previous work.", "Provide a scientific basis for the hypothesis."],
   ["تحديد ما هو معروف مسبقًا عن المشكلة.", "تحديد الفجوات والاختلافات والقيود في الأدلة السابقة.",
    "تنقيح سؤال البحث واختيار الطرائق المناسبة.", "تجنّب التكرار غير الضروري للأعمال السابقة.", "توفير أساس علمي للفرضية."]),
 N("**Sources may include peer-reviewed articles, guidelines, validated laboratory procedures, and manufacturer instructions when relevant.**",
   "**قد تشمل المصادر المقالات المحكّمة، والإرشادات (الأدلّة الإرشادية)، والإجراءات المختبرية المصادق عليها، وتعليمات الشركة المصنّعة عند الحاجة.**", label=["Sources", "المصادر"]),

 SEC("4. Formulating a Hypothesis", "4. صياغة الفرضية"),
 L(["Clear", "Specific", "Testable", "Consistent with existing knowledge", "Related to measurable variables"],
   ["واضحة", "محدّدة", "قابلة للاختبار", "متّسقة مع المعرفة الموجودة", "مرتبطة بمتغيّرات قابلة للقياس"], en="**A good hypothesis should be**", ar="**يجب أن تكون الفرضية الجيدة**"),
 G("Laboratory example", "مثال مختبري",
   ["Hypothesis: A 2-hour delay before plasma separation decreases measured glucose concentration.",
    "Prediction: Delayed samples will show lower glucose than promptly processed samples."],
   ["الفرضية: التأخير ساعتين قبل فصل البلازما يُنقص تركيز الكلوكوز المقاس.",
    "التنبّؤ: ستُظهر العيّنات المتأخّرة كلوكوزًا أقل من العيّنات المعالجة فورًا."]),

 SEC("Null and Alternative Hypotheses", "الفرضية الصفرية والفرضية البديلة"),
 G("Null Hypothesis (H0)", "الفرضية الصفرية (`H0`)",
   ["States that there is **no difference, association, or effect** in the population.",
    "Example: There is no difference in mean glucose concentration between promptly processed and delayed samples."],
   ["تنصّ على **عدم وجود فرق أو ارتباط أو تأثير** في المجتمع.",
    "مثال: لا يوجد فرق في متوسط تركيز الكلوكوز بين العيّنات المعالجة فورًا والعيّنات المتأخّرة."]),
 G("Alternative Hypothesis (H1)", "الفرضية البديلة (`H1`)",
   ["States that **a difference, association, or effect exists**.",
    "Example: Mean glucose concentration differs between promptly processed and delayed samples."],
   ["تنصّ على **وجود فرق أو ارتباط أو تأثير**.",
    "مثال: يختلف متوسط تركيز الكلوكوز بين العيّنات المعالجة فورًا والعيّنات المتأخّرة."]),
 N("*Statistical analysis evaluates how compatible the observed data are with a specified null model; it does not “prove” a hypothesis with certainty.*",
   "*يقيّم التحليل الإحصائي مدى توافق البيانات المشاهدة مع نموذج صفري محدّد؛ وهو لا «يُثبت» الفرضية بيقين.*", label=["Important", "مهم"]),

 SEC("5. Variables in Scientific Research", "5. المتغيّرات في البحث العلمي"),
 C("**A variable is a characteristic, factor, exposure, or outcome that can take different values.**",
   "**المتغيّر هو صفة أو عامل أو تعرّض أو نتيجة يمكن أن تأخذ قيمًا مختلفة.**"),
 dict(t="table", head=["Type", "Definition", "Laboratory example", "الشرح"], ar_cols=[3], key_cols=[0],
      rows=[["Independent", "Factor investigated or manipulated", "Processing delay", "**المستقل**: العامل الذي يُدرس أو يُتحكَّم به — مثال: تأخير المعالجة"],
            ["Dependent", "Outcome measured", "Glucose concentration", "**التابع**: النتيجة المقاسة — مثال: تركيز الكلوكوز"],
            ["Controlled", "Conditions kept similar", "Tube, temperature, analyser", "**المضبوط**: ظروف تُبقى متشابهة — مثال: الأنبوب، الحرارة، جهاز التحليل"]]),
 N("*In observational studies, the “independent” variable may be an exposure that is observed rather than manipulated.*",
   "*في الدراسات الرصدية قد يكون المتغيّر «المستقل» تعرّضًا يُلاحَظ بدلًا من أن يُتحكَّم به.*"),

 SEC("6. Study Design and Experimental Planning", "6. تصميم الدراسة والتخطيط التجريبي"),
 L(["Select a design that matches the research question.", "Define the study population, samples, comparison groups, and eligibility criteria.",
    "Standardise specimen collection, processing, and measurement procedures.", "Plan sample size and statistical analysis before examining the final results.",
    "Identify potential sources of bias and confounding.", "Include appropriate research comparisons and laboratory quality controls."],
   ["اختيار تصميم يتلاءم مع سؤال البحث.", "تحديد مجتمع الدراسة والعيّنات ومجموعات المقارنة ومعايير الأهلية.",
    "توحيد إجراءات جمع العيّنات ومعالجتها وقياسها.", "التخطيط لحجم العيّنة والتحليل الإحصائي قبل فحص النتائج النهائية.",
    "تحديد المصادر المحتملة للتحيّز والتداخل (الإرباك).", "تضمين مقارنات بحثية مناسبة وضوابط جودة مختبرية."]),

 SEC("Scientific Method vs. Study Design", "المنهج العلمي مقابل تصميم الدراسة"),
 G("Scientific Method", "المنهج العلمي", "The broad framework for scientific reasoning.", "الإطار العام للتفكير العلمي."),
 dict(t="flow", steps=[{"en": "Problem", "ar": "مشكلة"}, {"en": "Question", "ar": "سؤال"}, {"en": "Hypothesis", "ar": "فرضية"},
                       {"en": "Evidence", "ar": "دليل"}, {"en": "Interpretation", "ar": "تفسير"}, {"en": "Conclusion", "ar": "استنتاج"}]),
 G("Study Design", "تصميم الدراسة",
   ["The specific plan used to obtain evidence.", "Examples: Experimental, Observational, Diagnostic accuracy, Cross-sectional, Case-control"],
   ["الخطة المحدّدة المستخدمة للحصول على الأدلة.", "أمثلة: تجريبي، رصدي، دقة التشخيص، مقطعي (عرضي)، حالة–شاهد"]),
 N("**The scientific method guides the investigation; the study design determines how the evidence will be collected.**",
   "**المنهج العلمي يوجّه الاستقصاء؛ وتصميم الدراسة يحدّد كيفية جمع الأدلة.**", label=["Key point", "نقطة مهمة"]),

 SEC("Research Comparison vs. Laboratory Quality Control", "المقارنة البحثية مقابل ضبط الجودة المختبري"),
 G("Research Comparison", "المقارنة البحثية",
   ["Designed to answer the research question.", "Example: Prompt processing compared with a defined processing delay.", "Purpose: Estimate a difference or association."],
   ["مصمّمة للإجابة عن سؤال البحث.", "مثال: المعالجة الفورية مقارنةً بتأخير محدّد في المعالجة.", "الغرض: تقدير فرق أو ارتباط."]),
 G("Laboratory Quality Control", "ضبط الجودة المختبري",
   ["Designed to verify analytical performance.", "Example: Control material with an expected acceptable range.", "Purpose: Assess whether the analytical run is acceptable."],
   ["مصمّم للتحقّق من الأداء التحليلي.", "مثال: مادة ضبط (كونترول) لها مدى مقبول متوقّع.", "الغرض: تقييم ما إذا كانت الدفعة التحليلية مقبولة."], style="light"),

 SEC("7. Data Collection and Measurement", "7. جمع البيانات والقياس"),
 L(["Use standardised procedures and clearly defined measurement units.", "Assign coded identifiers to samples and participants.",
    "Record raw data, missing observations, and protocol deviations.", "Use calibrated equipment and validated analytical methods when applicable.",
    "Distinguish biological replicates from repeated technical measurements.", "Protect data integrity, confidentiality, and traceability."],
   ["استخدام إجراءات موحّدة ووحدات قياس محدّدة بوضوح.", "إعطاء رموز تعريفية مشفّرة للعيّنات والمشاركين.",
    "تسجيل البيانات الخام والملاحظات المفقودة والانحرافات عن البروتوكول.", "استخدام أجهزة معايَرة وطرائق تحليلية مصادق عليها عند الاقتضاء.",
    "التمييز بين المكرّرات الحيوية والقياسات التقنية المكرّرة.", "حماية سلامة البيانات وسرّيتها وإمكانية تتبّعها."]),

 SEC("8. Data Analysis and Interpretation", "8. تحليل البيانات وتفسيرها"),
 L(["Organise and summarise data.", "Describe distributions and variability.", "Select statistical methods appropriate to the design and data.", "Estimate effect sizes and uncertainty."],
   ["تنظيم البيانات وتلخيصها.", "وصف التوزيعات والتباين.", "اختيار طرائق إحصائية ملائمة للتصميم والبيانات.", "تقدير حجم التأثير وعدم اليقين."], en="**Data Analysis**", ar="**تحليل البيانات**"),
 L(["Relate findings to the research question.", "Consider biological or clinical relevance.", "Assess bias, confounding, and limitations.", "Compare findings with existing evidence."],
   ["ربط النتائج بسؤال البحث.", "مراعاة الأهمية الحيوية أو السريرية.", "تقييم التحيّز والتداخل والقيود.", "مقارنة النتائج بالأدلة الموجودة."], en="**Interpretation**", ar="**التفسير**"),
 N("**Statistical significance and practical importance are not the same concept.**", "**الدلالة الإحصائية والأهمية العملية ليستا المفهوم نفسه.**", label=["Important", "مهم"]),

 SEC("9. Drawing a Scientific Conclusion", "9. الوصول إلى استنتاج علمي"),
 L(["Answer the research question using the collected evidence.", "State whether the findings are consistent with the proposed hypothesis.",
    "Avoid conclusions that extend beyond the population, methods, or conditions studied.", "Report important limitations and alternative explanations.",
    "Identify questions that require further investigation."],
   ["الإجابة عن سؤال البحث باستخدام الأدلة المجموعة.", "بيان ما إذا كانت النتائج متّسقة مع الفرضية المقترحة.",
    "تجنّب الاستنتاجات التي تتجاوز المجتمع أو الطرائق أو الظروف المدروسة.", "عرض القيود المهمة والتفسيرات البديلة.",
    "تحديد الأسئلة التي تتطلّب مزيدًا من الاستقصاء."]),
 N("**A conclusion should match the strength and scope of the evidence.**", "**يجب أن يتناسب الاستنتاج مع قوة الأدلة ونطاقها.**", label=["Rule", "قاعدة"]),

 SEC("10. Communication and Reproducibility", "10. النشر وقابلية التكرار"),
 L(["Describe methods sufficiently for evaluation and repetition.", "Report complete results, including unexpected or negative findings.",
    "Use appropriate tables, figures, and statistical reporting.", "Discuss limitations transparently.",
    "Allow findings to be examined, challenged, and reproduced by the scientific community."],
   ["وصف الطرائق بما يكفي لتقييمها وتكرارها.", "عرض النتائج كاملة، بما فيها النتائج غير المتوقّعة أو السلبية.",
    "استخدام الجداول والأشكال والتقارير الإحصائية المناسبة.", "مناقشة القيود بشفافية.",
    "إتاحة النتائج للفحص والنقد والتكرار من قبل المجتمع العلمي."]),

 SEC("Bias, Confounding, and Sources of Error", "التحيّز والتداخل ومصادر الخطأ"),
 G("Bias", "التحيّز", "A systematic process that can distort an estimate or interpretation.", "عملية منهجية (منتظمة) يمكن أن تشوّه التقدير أو التفسير."),
 G("Confounding", "التداخل (الإرباك)", "A third factor related to both the exposure and outcome that can distort their observed relationship.",
   "عامل ثالث مرتبط بكلٍّ من التعرّض والنتيجة، يمكن أن يشوّه العلاقة المشاهدة بينهما."),
 G("Random Error", "الخطأ العشوائي", "Variation due to chance, sampling, or measurement variability.", "تباين ناتج عن الصدفة أو أخذ العيّنات أو تباين القياس.", style="light"),
 N("**Good design reduces avoidable error; statistical analysis cannot repair every design problem.**",
   "**التصميم الجيد يقلّل الخطأ الممكن تجنّبه؛ والتحليل الإحصائي لا يستطيع إصلاح كل مشكلة في التصميم.**", label=["Key point", "نقطة مهمة"]),

 SEC("Application 1 — Pre-analytical Laboratory Question", "التطبيق 1 — سؤال مختبري في مرحلة ما قبل التحليل"),
 C("**Research question: Does a defined delay before plasma separation alter measured glucose concentration?**",
   "**سؤال البحث: هل يغيّر تأخير محدّد قبل فصل البلازما تركيزَ الكلوكوز المقاس؟**"),
 dict(t="table", head=["Element", "Content", "العنصر والمحتوى"], ar_cols=[2], key_cols=[0],
      rows=[["Hypothesis", "Delay changes glucose", "**الفرضية**: التأخير يغيّر الكلوكوز"],
            ["Design", "Paired samples from each donor", "**التصميم**: عيّنات مزدوجة من كل متبرّع"],
            ["Independent variable", "Processing delay", "**المتغيّر المستقل**: تأخير المعالجة"],
            ["Dependent variable", "Glucose concentration", "**المتغيّر التابع**: تركيز الكلوكوز"],
            ["Controls", "Tube, temperature, assay", "**الضوابط**: الأنبوب، الحرارة، طريقة الفحص"],
            ["Analysis", "Compare paired differences", "**التحليل**: مقارنة الفروق المزدوجة"],
            ["Conclusion", "Limited to tested conditions", "**الاستنتاج**: مقتصر على الظروف المختبَرة"]]),

 SEC("Application 2 — ELISA Validation Question", "التطبيق 2 — سؤال التحقّق من فحص الإليزا"),
 G("Research Question", "سؤال البحث",
   ["Does an additional wash step reduce background absorbance without compromising expected positive signal?",
    "Independent variable: Wash procedure", "Outcomes: Blank/negative-control OD and positive signal"],
   ["هل تقلّل خطوة غسل إضافية الامتصاص الخلفي دون الإضرار بالإشارة الموجبة المتوقّعة؟",
    "المتغيّر المستقل: إجراء الغسل", "النتائج: الكثافة الضوئية (`OD`) للفراغ/الضابط السالب، والإشارة الموجبة"]),
 L(["Compare defined procedures under otherwise similar conditions.", "Use appropriate assay controls.",
    "Evaluate both background and expected signal.", "Interpret results against predefined performance criteria."],
   ["مقارنة إجراءات محدّدة تحت ظروف متشابهة في ما عدا ذلك.", "استخدام ضوابط فحص مناسبة.",
    "تقييم الخلفية والإشارة المتوقّعة كلتيهما.", "تفسير النتائج مقابل معايير أداء محدّدة مسبقًا."], en="**Scientific Approach**", ar="**النهج العلمي**"),

 SEC("Artificial Intelligence as a Research Tool", "الذكاء الاصطناعي أداةً بحثية"),
 dict(t="table", head=["Research stage", "Possible AI support", "Researcher responsibility", "الترجمة"], ar_cols=[3], key_cols=[0],
      rows=[["Literature search", "Suggest keywords / organise sources", "Verify original sources", "**البحث في الأدبيات**: اقتراح كلمات مفتاحية / تنظيم المصادر — **مسؤولية الباحث**: التحقّق من المصادر الأصلية"],
            ["Analysis", "Assist with code / pattern exploration", "Check data, assumptions, and code", "**التحليل**: المساعدة في الشيفرة / استكشاف الأنماط — **الباحث**: فحص البيانات والافتراضات والشيفرة"],
            ["Writing", "Improve structure and clarity", "Verify every scientific claim", "**الكتابة**: تحسين البنية والوضوح — **الباحث**: التحقّق من كل ادعاء علمي"],
            ["Data handling", "Automate selected tasks", "Protect privacy and governance", "**التعامل مع البيانات**: أتمتة مهام مختارة — **الباحث**: حماية الخصوصية والحوكمة"]]),
 N("**AI output is not scientific evidence by itself; it must be verified against reliable data and sources.**",
   "**مخرجات الذكاء الاصطناعي ليست دليلًا علميًا بحدّ ذاتها؛ ويجب التحقّق منها بمقارنتها ببيانات ومصادر موثوقة.**", label=["Important", "مهم"]),

 SEC("Evaluating AI with the Scientific Method", "تقييم الذكاء الاصطناعي بالمنهج العلمي"),
 C("**Example question: Can an AI system identify blood-smear images that require expert review?**",
   "**سؤال مثال: هل يستطيع نظام ذكاء اصطناعي تحديد صور مسحات الدم التي تتطلّب مراجعة خبير؟**"),
 dict(t="flow", steps=[
   {"en": "Define target outcome", "ar": "تحديد النتيجة المستهدفة"},
   {"en": "Develop / train on appropriate data", "ar": "التطوير / التدريب على بيانات مناسبة"},
   {"en": "Test on new, separate patients", "ar": "الاختبار على مرضى جدد منفصلين"},
   {"en": "Compare with expert reference", "ar": "المقارنة مع مرجع الخبير"},
   {"en": "Evaluate performance and errors", "ar": "تقييم الأداء والأخطاء"}]),
 C("Relevant measures may include **sensitivity, specificity, missed cases, calibration, and review time** — depending on the intended use.",
   "قد تشمل المقاييس ذات الصلة **الحساسية، والنوعية، والحالات المفقودة، والمعايرة، ووقت المراجعة** — بحسب الاستخدام المقصود."),

 SEC("Scientific Integrity and Ethics", "النزاهة العلمية والأخلاقيات"),
 L(["Obtain appropriate ethical review and informed consent or an approved waiver when required.",
    "Protect participant identity and confidential laboratory information.",
    "Do not alter routine patient care merely to create a research condition without appropriate approval.",
    "Do not fabricate, falsify, or selectively remove data.",
    "Report conflicts of interest, protocol deviations, and important limitations transparently."],
   ["الحصول على المراجعة الأخلاقية المناسبة والموافقة المستنيرة أو إعفاء معتمد عند الحاجة.",
    "حماية هوية المشاركين والمعلومات المختبرية السرّية.",
    "عدم تغيير الرعاية الروتينية للمريض لمجرد خلق ظرف بحثي من دون موافقة مناسبة.",
    "عدم اختلاق البيانات أو تزويرها أو حذفها انتقائيًا.",
    "الإبلاغ بشفافية عن تضارب المصالح والانحرافات عن البروتوكول والقيود المهمة."]),

 SEC("Summary", "الخلاصة"),
 dict(t="table", style="summary", label_en="Key messages", label_ar="الرسائل الرئيسة", head=["", "Key message", "الرسالة"], ar_cols=[2], key_cols=[0],
      rows=[["Scientific Method", "A systematic framework for answering scientific questions with evidence.", "إطار منظّم للإجابة عن الأسئلة العلمية بالأدلة."],
            ["Good Research", "Requires clear questions, testable hypotheses, appropriate design, and reliable measurement.", "يتطلّب أسئلة واضحة، وفرضيات قابلة للاختبار، وتصميمًا مناسبًا، وقياسًا موثوقًا."],
            ["Interpretation", "Must consider effect size, uncertainty, bias, confounding, and limitations.", "يجب أن يراعي حجم التأثير، وعدم اليقين، والتحيّز، والتداخل، والقيود."],
            ["Laboratory Science", "Applies to pre-analytical, analytical, and diagnostic questions.", "يُطبَّق على أسئلة ما قبل التحليل والتحليل والتشخيص."],
            ["AI", "Can support research and can itself be evaluated scientifically.", "يمكن أن يدعم البحث، ويمكن تقييمه هو نفسه علميًا."]]),
]

def Q(en, ar, opts, ans, **k):
    return dict(en=en, ar=ar, options=[list(o) for o in opts], answer=ans, **k)

mcq = [
 {"topic_en": "Definition and characteristics", "topic_ar": "التعريف والخصائص"},
 Q("The scientific method is best defined as:", "أفضل تعريف للمنهج العلمي هو:", [("A personal opinion based on experience", "رأي شخصي قائم على الخبرة"), ("A systematic and evidence-based approach to investigate questions, test hypotheses and develop conclusions", "نهج منظّم قائم على الأدلة لاستقصاء الأسئلة واختبار الفرضيات والوصول إلى استنتاجات"), ("A statistical test", "اختبار إحصائي"), ("A laboratory quality-control procedure", "إجراء لضبط الجودة المختبري")], "b"),
 Q("“New evidence may modify previous explanations” describes the scientific method as:", "«قد تعدّل الأدلة الجديدة التفسيرات السابقة» يصف المنهج العلمي بأنه:", [("Systematic", "منظّم"), ("Testable", "قابل للاختبار"), ("Self-correcting", "ذاتي التصحيح"), ("Empirical", "تجريبي")], "c"),
 Q("Without a scientific approach, all of the following may happen EXCEPT:", "من دون نهج علمي قد يحدث كل مما يأتي عدا:", [("Subjective interpretation", "التفسير الذاتي"), ("Ignoring confounding factors", "إهمال العوامل المربكة"), ("Results difficult to reproduce", "صعوبة تكرار النتائج"), ("Conclusions evaluated by others", "تقييم الآخرين للاستنتاجات")], "d"),
 Q("A characteristic that “aims to minimise personal bias” is:", "الخاصية التي «تهدف إلى تقليل التحيّز الشخصي» هي:", [("Objective", "الموضوعية"), ("Reproducible", "قابلية التكرار"), ("Transparent", "الشفافية"), ("Controlled", "الضبط")], "a"),
 Q("“Methods are described sufficiently for independent repetition” describes:", "«تُوصف الطرائق بما يكفي لتكرارها بشكل مستقل» يصف خاصية:", [("Empirical", "التجريبية"), ("Objective", "الموضوعية"), ("Testable", "قابلية الاختبار"), ("Reproducible", "قابلية التكرار")], "d"),
 Q("How many major steps of the scientific method are listed in the lecture?", "كم خطوة رئيسة للمنهج العلمي ذُكرت في المحاضرة؟", [("Five", "خمس"), ("Seven", "سبع"), ("Nine", "تسع"), ("Twelve", "اثنتا عشرة")], "c"),
 Q("The scientific method process is described as:", "توصف عملية المنهج العلمي بأنها:", [("Linear and final", "خطّية ونهائية"), ("Iterative", "تكرارية"), ("Random", "عشوائية"), ("Optional", "اختيارية")], "b"),
 {"topic_en": "Question, hypothesis and variables", "topic_ar": "السؤال والفرضية والمتغيّرات"},
 Q("“A delayed plasma sample gives a lower glucose result than a promptly processed sample” is an example of:", "«عيّنة بلازما متأخّرة تعطي كلوكوزًا أقل من عيّنة عولجت فورًا» مثال على:", [("Observation", "الملاحظة"), ("Hypothesis", "الفرضية"), ("Conclusion", "الاستنتاج"), ("Quality control", "ضبط الجودة")], "a"),
 Q("A research question that “can be studied with available participants, samples, time, and methods” is:", "سؤال البحث الذي «يمكن دراسته بالمشاركين والعيّنات والوقت والطرائق المتاحة» يكون:", [("Clear", "واضحًا"), ("Focused", "مركّزًا"), ("Feasible", "ممكن التنفيذ"), ("Measurable", "قابلًا للقياس")], "c"),
 Q("Which is NOT a purpose of background research and literature review?", "أي مما يأتي ليس من أغراض مراجعة الأدبيات؟", [("Identify gaps in previous evidence", "تحديد الفجوات في الأدلة السابقة"), ("Avoid unnecessary duplication", "تجنّب التكرار غير الضروري"), ("Provide a basis for the hypothesis", "توفير أساس للفرضية"), ("Fabricate missing data", "اختلاق البيانات المفقودة")], "d"),
 Q("A good hypothesis should be all of the following EXCEPT:", "يجب أن تكون الفرضية الجيدة كل مما يأتي عدا:", [("Clear", "واضحة"), ("Testable", "قابلة للاختبار"), ("Vague", "غامضة"), ("Related to measurable variables", "مرتبطة بمتغيّرات قابلة للقياس")], "c"),
 Q("The null hypothesis (H0) states that:", "تنصّ الفرضية الصفرية (H0) على:", [("A difference exists", "وجود فرق"), ("There is no difference, association, or effect", "عدم وجود فرق أو ارتباط أو تأثير"), ("The hypothesis is proven", "إثبات الفرضية"), ("Data are invalid", "عدم صحة البيانات")], "b"),
 Q("Statistical analysis:", "التحليل الإحصائي:", [("Proves a hypothesis with certainty", "يُثبت الفرضية بيقين"), ("Evaluates how compatible the data are with a null model", "يقيّم مدى توافق البيانات مع النموذج الصفري"), ("Replaces study design", "يحلّ محلّ تصميم الدراسة"), ("Is not needed", "غير ضروري")], "b"),
 Q("In the glucose example, the independent variable is:", "في مثال الكلوكوز، المتغيّر المستقل هو:", [("Processing delay", "تأخير المعالجة"), ("Glucose concentration", "تركيز الكلوكوز"), ("Analyser", "جهاز التحليل"), ("Temperature", "الحرارة")], "a"),
 Q("In the glucose example, glucose concentration is the:", "في مثال الكلوكوز، تركيز الكلوكوز هو المتغيّر:", [("Independent variable", "المستقل"), ("Controlled variable", "المضبوط"), ("Dependent variable", "التابع"), ("Confounder", "المربك")], "c"),
 Q("Tube, temperature and analyser kept similar are:", "الأنبوب والحرارة وجهاز التحليل التي تُبقى متشابهة هي متغيّرات:", [("Dependent", "تابعة"), ("Controlled", "مضبوطة"), ("Independent", "مستقلة"), ("Random", "عشوائية")], "b"),
 {"topic_en": "Design, data and conclusion", "topic_ar": "التصميم والبيانات والاستنتاج"},
 Q("Sample size and statistical analysis should be planned:", "يجب التخطيط لحجم العيّنة والتحليل الإحصائي:", [("After seeing the final results", "بعد رؤية النتائج النهائية"), ("Before examining the final results", "قبل فحص النتائج النهائية"), ("Only if results are significant", "فقط إذا كانت النتائج دالّة"), ("Never", "أبدًا")], "b"),
 Q("The scientific method differs from study design in that the study design is:", "يختلف المنهج العلمي عن تصميم الدراسة في أن تصميم الدراسة هو:", [("The broad framework for reasoning", "الإطار العام للتفكير"), ("The specific plan used to obtain evidence", "الخطة المحدّدة للحصول على الأدلة"), ("A conclusion", "استنتاج"), ("A hypothesis", "فرضية")], "b"),
 Q("Which is NOT a study design example in the lecture?", "أي مما يأتي ليس مثالًا على تصميم الدراسة في المحاضرة؟", [("Case-control", "حالة–شاهد"), ("Cross-sectional", "مقطعي"), ("Diagnostic accuracy", "دقة التشخيص"), ("Self-correcting", "ذاتي التصحيح")], "d"),
 Q("Laboratory quality control is designed to:", "يُصمَّم ضبط الجودة المختبري لـ:", [("Answer the research question", "الإجابة عن سؤال البحث"), ("Estimate an association", "تقدير ارتباط"), ("Verify analytical performance", "التحقّق من الأداء التحليلي"), ("Recruit participants", "تجنيد المشاركين")], "c"),
 Q("Distinguishing biological replicates from repeated technical measurements belongs to:", "التمييز بين المكرّرات الحيوية والقياسات التقنية المكرّرة يتبع خطوة:", [("Data collection and measurement", "جمع البيانات والقياس"), ("Literature review", "مراجعة الأدبيات"), ("Communication", "النشر"), ("Formulating the question", "صياغة السؤال")], "a"),
 Q("“Estimate effect sizes and uncertainty” is part of:", "«تقدير حجم التأثير وعدم اليقين» جزء من:", [("Interpretation", "التفسير"), ("Data analysis", "تحليل البيانات"), ("Observation", "الملاحظة"), ("Ethics", "الأخلاقيات")], "b"),
 Q("Statistical significance and practical importance are:", "الدلالة الإحصائية والأهمية العملية:", [("The same concept", "المفهوم نفسه"), ("Always equal", "متساويتان دائمًا"), ("Not the same concept", "ليستا المفهوم نفسه"), ("Unrelated to research", "لا علاقة لهما بالبحث")], "c"),
 Q("A conclusion should:", "يجب أن يكون الاستنتاج:", [("Extend beyond the population studied", "متجاوزًا للمجتمع المدروس"), ("Match the strength and scope of the evidence", "متناسبًا مع قوة الأدلة ونطاقها"), ("Ignore limitations", "متجاهلًا للقيود"), ("Hide negative findings", "مخفيًا للنتائج السلبية")], "b"),
 {"topic_en": "Error, AI and ethics", "topic_ar": "الخطأ والذكاء الاصطناعي والأخلاقيات"},
 Q("A third factor related to both exposure and outcome that distorts their relationship is:", "العامل الثالث المرتبط بالتعرّض والنتيجة معًا والذي يشوّه علاقتهما هو:", [("Bias", "التحيّز"), ("Random error", "الخطأ العشوائي"), ("Confounding", "التداخل (الإرباك)"), ("Calibration", "المعايرة")], "c"),
 Q("Variation due to chance, sampling, or measurement variability is:", "التباين الناتج عن الصدفة أو أخذ العيّنات أو تباين القياس هو:", [("Random error", "الخطأ العشوائي"), ("Bias", "التحيّز"), ("Confounding", "التداخل"), ("Fabrication", "الاختلاق")], "a"),
 Q("In Application 1, the design used is:", "في التطبيق 1، التصميم المستخدم هو:", [("Case-control", "حالة–شاهد"), ("Paired samples from each donor", "عيّنات مزدوجة من كل متبرّع"), ("Cross-sectional survey", "مسح مقطعي"), ("Animal experiment", "تجربة حيوانية")], "b"),
 Q("In the ELISA application, the independent variable is:", "في تطبيق الإليزا، المتغيّر المستقل هو:", [("Background absorbance", "الامتصاص الخلفي"), ("Positive signal", "الإشارة الموجبة"), ("Wash procedure", "إجراء الغسل"), ("OD of blank", "الكثافة الضوئية للفراغ")], "c"),
 Q("When AI is used for literature search, the researcher must:", "عند استخدام الذكاء الاصطناعي في البحث عن الأدبيات يجب على الباحث:", [("Accept its output", "قبول مخرجاته"), ("Verify original sources", "التحقّق من المصادر الأصلية"), ("Stop reading", "التوقّف عن القراءة"), ("Remove references", "حذف المراجع")], "b"),
 Q("AI output is:", "مخرجات الذكاء الاصطناعي:", [("Scientific evidence by itself", "دليل علمي بحدّ ذاتها"), ("Always correct", "صحيحة دائمًا"), ("Not scientific evidence by itself; must be verified", "ليست دليلًا علميًا بذاتها؛ ويجب التحقّق منها"), ("Forbidden in research", "ممنوعة في البحث")], "c"),
 Q("When evaluating an AI system, it should be tested on:", "عند تقييم نظام ذكاء اصطناعي يجب اختباره على:", [("The same training data", "بيانات التدريب نفسها"), ("New, separate patients", "مرضى جدد منفصلين"), ("Only easy cases", "الحالات السهلة فقط"), ("No patients", "لا مرضى")], "b"),
 Q("Which is a violation of scientific integrity?", "أي مما يأتي يُعدّ انتهاكًا للنزاهة العلمية؟", [("Reporting limitations", "عرض القيود"), ("Obtaining informed consent", "الحصول على الموافقة المستنيرة"), ("Protecting participant identity", "حماية هوية المشاركين"), ("Selectively removing data", "حذف البيانات انتقائيًا")], "d"),
]

tf = [
 dict(en="The scientific method is systematic and evidence-based.", ar="المنهج العلمي منظّم وقائم على الأدلة.", answer="T"),
 dict(en="Empirical means based on personal opinion.", ar="التجريبي (الإمبريقي) يعني القائم على الرأي الشخصي.", answer="F"),
 dict(en="The scientific method is iterative; findings may generate new questions.", ar="المنهج العلمي تكراري؛ قد تولّد النتائج أسئلة جديدة.", answer="T"),
 dict(en="A research question converts a specific question into a broad problem.", ar="يحوّل سؤال البحث سؤالًا محدّدًا إلى مشكلة واسعة.", answer="F"),
 dict(en="Literature review helps avoid unnecessary duplication of previous work.", ar="تساعد مراجعة الأدبيات على تجنّب التكرار غير الضروري للأعمال السابقة.", answer="T"),
 dict(en="The alternative hypothesis states that no difference exists.", ar="تنصّ الفرضية البديلة على عدم وجود فرق.", answer="F"),
 dict(en="Statistical analysis proves a hypothesis with certainty.", ar="يُثبت التحليل الإحصائي الفرضية بيقين.", answer="F"),
 dict(en="In observational studies, the independent variable may be an observed exposure.", ar="في الدراسات الرصدية قد يكون المتغيّر المستقل تعرّضًا مُلاحَظًا.", answer="T"),
 dict(en="Laboratory quality control is designed to answer the research question.", ar="يُصمَّم ضبط الجودة المختبري للإجابة عن سؤال البحث.", answer="F"),
 dict(en="Raw data, missing observations and protocol deviations should be recorded.", ar="يجب تسجيل البيانات الخام والملاحظات المفقودة والانحرافات عن البروتوكول.", answer="T"),
 dict(en="Unexpected or negative findings should not be reported.", ar="لا ينبغي عرض النتائج غير المتوقّعة أو السلبية.", answer="F"),
 dict(en="Statistical analysis can repair every design problem.", ar="يستطيع التحليل الإحصائي إصلاح كل مشكلة في التصميم.", answer="F"),
 dict(en="Bias is a systematic process that can distort an estimate.", ar="التحيّز عملية منهجية يمكن أن تشوّه التقدير.", answer="T"),
 dict(en="AI can itself be evaluated scientifically.", ar="يمكن تقييم الذكاء الاصطناعي نفسه علميًا.", answer="T"),
]

traps = [
 dict(en="Observation vs scientific problem", ar="الملاحظة مقابل المشكلة العلمية", answer_en="Observation: a directly recorded/measured finding (lower glucose in a delayed sample). Problem: a defined issue needing investigation (the effect of delay is uncertain).", answer_ar="الملاحظة: نتيجة مسجّلة/مقاسة مباشرة (كلوكوز أقل في عيّنة متأخّرة). المشكلة: قضية محدّدة تحتاج استقصاء (تأثير التأخير غير مؤكّد)."),
 dict(en="Hypothesis vs prediction", ar="الفرضية مقابل التنبّؤ", answer_en="Hypothesis: a 2-hour delay decreases measured glucose. Prediction: delayed samples will show lower glucose than prompt ones.", answer_ar="الفرضية: التأخير ساعتين يُنقص الكلوكوز المقاس. التنبّؤ: ستُظهر العيّنات المتأخّرة كلوكوزًا أقل من الفورية."),
 dict(en="H0 vs H1", ar="H0 مقابل H1", answer_en="H0: no difference, association or effect. H1: a difference, association or effect exists.", answer_ar="H0: لا فرق ولا ارتباط ولا تأثير. H1: يوجد فرق أو ارتباط أو تأثير."),
 dict(en="Scientific method vs study design", ar="المنهج العلمي مقابل تصميم الدراسة", answer_en="Method: the broad framework (problem → … → conclusion) that guides the investigation. Design: the specific plan that determines how evidence is collected.", answer_ar="المنهج: الإطار العام (مشكلة ← … ← استنتاج) الذي يوجّه الاستقصاء. التصميم: الخطة المحدّدة التي تحدّد كيفية جمع الأدلة."),
 dict(en="Research comparison vs laboratory QC", ar="المقارنة البحثية مقابل ضبط الجودة", answer_en="Research comparison answers the research question (estimate a difference). QC verifies analytical performance (is the run acceptable).", answer_ar="المقارنة البحثية تجيب عن سؤال البحث (تقدير فرق). ضبط الجودة يتحقّق من الأداء التحليلي (هل الدفعة مقبولة)."),
 dict(en="Bias vs confounding vs random error", ar="التحيّز مقابل التداخل مقابل الخطأ العشوائي", answer_en="Bias: systematic distortion. Confounding: a third factor linked to exposure and outcome. Random error: chance, sampling or measurement variability.", answer_ar="التحيّز: تشويه منهجي. التداخل: عامل ثالث مرتبط بالتعرّض والنتيجة. الخطأ العشوائي: الصدفة أو أخذ العيّنات أو تباين القياس."),
 dict(en="Data analysis vs interpretation", ar="تحليل البيانات مقابل التفسير", answer_en="Analysis: organise, describe variability, choose statistics, estimate effect sizes. Interpretation: relate to the question, clinical relevance, bias and limitations, compare with evidence.", answer_ar="التحليل: تنظيم، وصف التباين، اختيار الإحصاء، تقدير حجم التأثير. التفسير: الربط بالسؤال، الأهمية السريرية، التحيّز والقيود، المقارنة بالأدلة."),
]

important = [
 dict(en="Define the scientific method and list its features.", ar="عرّف المنهج العلمي وعدّد سماته.", answer_en="A systematic and evidence-based approach used to investigate scientific questions, test hypotheses and develop conclusions from observable and measurable data. Features: systematic, evidence-based, testable, self-correcting.", answer_ar="نهج منظّم قائم على الأدلة لاستقصاء الأسئلة العلمية واختبار الفرضيات والوصول إلى استنتاجات من بيانات قابلة للملاحظة والقياس. سماته: منظّم، قائم على الأدلة، قابل للاختبار، ذاتي التصحيح."),
 dict(en="List the characteristics of scientific investigation.", ar="عدّد خصائص الاستقصاء العلمي.", answer_en="Objective, empirical, testable, controlled, reproducible, transparent.", answer_ar="موضوعي، تجريبي، قابل للاختبار، مضبوط، قابل للتكرار، شفّاف."),
 dict(en="List the major steps of the scientific method.", ar="عدّد الخطوات الرئيسة للمنهج العلمي.", answer_en="Observation/problem, research question, background research, hypothesis, study/experiment design, data collection, analysis and interpretation, conclusion, communication — an iterative process.", answer_ar="الملاحظة/المشكلة، سؤال البحث، البحث في الخلفية، الفرضية، تصميم الدراسة/التجربة، جمع البيانات، التحليل والتفسير، الاستنتاج، النشر — وهي عملية تكرارية."),
 dict(en="What are the features of a good research question? Give an example.", ar="ما سمات سؤال البحث الجيد؟ أعطِ مثالًا.", answer_en="Clear, focused, measurable, feasible. Example: Does a 2-hour delay before plasma separation change measured glucose concentration?", answer_ar="واضح، مركّز، قابل للقياس، ممكن التنفيذ. مثال: هل يغيّر التأخير ساعتين قبل فصل البلازما تركيز الكلوكوز المقاس؟"),
 dict(en="Define a variable and explain its types with laboratory examples.", ar="عرّف المتغيّر واشرح أنواعه مع أمثلة مختبرية.", answer_en="A characteristic, factor, exposure or outcome that can take different values. Independent: factor investigated or manipulated (processing delay). Dependent: outcome measured (glucose). Controlled: conditions kept similar (tube, temperature, analyser).", answer_ar="صفة أو عامل أو تعرّض أو نتيجة تأخذ قيمًا مختلفة. المستقل: العامل المدروس أو المتحكَّم به (تأخير المعالجة). التابع: النتيجة المقاسة (الكلوكوز). المضبوط: ظروف تُبقى متشابهة (الأنبوب، الحرارة، الجهاز)."),
 dict(en="Define bias, confounding and random error.", ar="عرّف التحيّز والتداخل والخطأ العشوائي.", answer_en="Bias: a systematic process that can distort an estimate or interpretation. Confounding: a third factor related to both exposure and outcome that distorts their relationship. Random error: variation due to chance, sampling or measurement variability.", answer_ar="التحيّز: عملية منهجية قد تشوّه التقدير أو التفسير. التداخل: عامل ثالث مرتبط بالتعرّض والنتيجة يشوّه علاقتهما. الخطأ العشوائي: تباين بسبب الصدفة أو أخذ العيّنات أو تباين القياس."),
 dict(en="Explain the role and limits of AI in research.", ar="اشرح دور الذكاء الاصطناعي وحدوده في البحث.", answer_en="AI can suggest keywords and organise sources, assist with code and patterns, improve writing, and automate tasks; the researcher must verify sources, check data and code, verify every claim, and protect privacy. AI output is not evidence by itself and AI can be evaluated scientifically (test on new patients, compare with experts, measure sensitivity, specificity…).", answer_ar="يمكن للذكاء الاصطناعي اقتراح الكلمات المفتاحية وتنظيم المصادر، والمساعدة في الشيفرة والأنماط، وتحسين الكتابة، وأتمتة المهام؛ وعلى الباحث التحقّق من المصادر، وفحص البيانات والشيفرة، والتحقّق من كل ادعاء، وحماية الخصوصية. ومخرجاته ليست دليلًا بذاتها، ويمكن تقييمه علميًا (اختبار على مرضى جدد، مقارنة بالخبراء، قياس الحساسية والنوعية…)."),
 dict(en="List the rules of scientific integrity and ethics.", ar="عدّد قواعد النزاهة العلمية والأخلاقيات.", answer_en="Ethical review and informed consent (or approved waiver); protect participant identity and confidential information; do not alter routine care without approval; do not fabricate, falsify or selectively remove data; report conflicts of interest, deviations and limitations transparently.", answer_ar="المراجعة الأخلاقية والموافقة المستنيرة (أو إعفاء معتمد)؛ حماية هوية المشاركين والمعلومات السرّية؛ عدم تغيير الرعاية الروتينية دون موافقة؛ عدم اختلاق البيانات أو تزويرها أو حذفها انتقائيًا؛ الإبلاغ بشفافية عن تضارب المصالح والانحرافات والقيود."),
]

data = {"meta": {
  "subject_en": "Principles of Research", "subject_ar": "مبادئ البحث العلمي", "short_ar": "مبادئ البحث",
  "unit_en": "Lecture 2", "unit_ar": "المحاضرة 2", "unit_label": "LEC", "unit_no": "2",
  "title_en": "Scientific Method", "title_ar": "المنهج العلمي",
  "kind": "Theory — نظري", "stage": "The fourth stage — الرابعة", "instructor": "ليندا منجد هادي"},
 "blocks": blocks, "questions": {"mcq": mcq, "tf": tf, "traps": traps, "important": important}}
qs = [q for q in mcq if "answer" in q]
print(len(qs), Counter(q["answer"] for q in qs))
import os
os.makedirs("/home/user/-/research-lec2-scientific-method", exist_ok=True)
json.dump(data, open("/home/user/-/research-lec2-scientific-method/lecture.json", "w"), ensure_ascii=False, indent=1)

```
