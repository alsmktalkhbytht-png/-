---
source: BIOS-Obsidian/tools/scripts/heal2/h4q.py
handouts: [histopathology-lec4-healing-regeneration]
saved: 2026-11-11
tags: [bios, code]
---
# heal2/h4q.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#histopathology-lec4-healing-regeneration|histopathology-lec4-healing-regeneration]]

```python
mcq = [
 {"topic_en": "Repair: regeneration and scar", "topic_ar": "الإصلاح: التجدّد والندبة"},
 Q("Repair (healing) refers to:", "يشير الإصلاح (الالتئام) إلى:",
   P(("Restoration of tissue architecture and function after an injury", "استعادة بنية النسيج ووظيفته بعد الإصابة"), ("Death of injured cells", "موت الخلايا المصابة"), ("Acute inflammation only", "الالتهاب الحاد فقط"), ("Formation of tumors", "تكوّن الأورام")), "a"),
 Q("Repair occurs by:", "يحدث الإصلاح بـ:",
   P(("Regeneration only", "التجدّد فقط"), ("Scar formation only", "تكوّن الندبة فقط"), ("Regeneration and scar formation", "التجدّد وتكوّن الندبة"), ("Apoptosis and necrosis", "الاستماتة والنخر")), "c"),
 Q("Regeneration is the typical response to injury in all of the following EXCEPT:", "التجدّد هو الاستجابة النموذجية للإصابة في كل ما يأتي عدا:",
   P(("Skin epithelium", "ظهارة الجلد"), ("Intestinal epithelium", "ظهارة الأمعاء"), ("Liver", "الكبد"), ("Cardiac muscle", "عضلة القلب")), "d"),
 Q("Regeneration occurs by:", "يحدث التجدّد بـ:",
   P(("Deposition of collagen", "ترسيب الكولاجين"), ("Proliferation of residual cells and replacement from tissue stem cells", "تكاثر الخلايا المتبقية والتعويض من الخلايا الجذعية النسيجية"), ("Fibroblast migration only", "هجرة الخلايا الليفية فقط"), ("Granulation tissue", "النسيج الحبيبي")), "b"),
 Q("Repair occurs by scar formation when:", "يحدث الإصلاح بتكوّن الندبة عندما:",
   P(("The tissue is capable of regeneration", "يكون النسيج قادرًا على التجدّد"), ("The supporting structures of the tissue are severely damaged", "تتضرّر البنى الداعمة للنسيج بشدة"), ("Injury is mild and superficial", "تكون الإصابة خفيفة وسطحية"), ("Stem cells are preserved", "يكون مخزون الخلايا الجذعية محفوظًا")), "b"),
 Q("The fibrous scar:", "الندبة الليفية:",
   P(("Performs the function of lost parenchymal cells", "تؤدي وظيفة الخلايا المتنية المفقودة"), ("Provides structural stability", "توفّر ثباتًا بنيويًا"), ("Regenerates neurons", "تجدّد الخلايا العصبية"), ("Is made of epithelial cells", "تتكوّن من خلايا ظهارية")), "b"),

 {"topic_en": "Scar formation and granulation tissue", "topic_ar": "تكوّن الندبة والنسيج الحبيبي"},
 Q("The first step in scar formation is:", "الخطوة الأولى في تكوّن الندبة هي:",
   P(("Remodeling", "إعادة التشكيل"), ("Angiogenesis", "تكوّن الأوعية"), ("Collagen deposition", "ترسيب الكولاجين"), ("Scab formation", "تكوّن القشرة")), "b"),
 Q("Maturation and reorganization of the fibrous tissue is called:", "نضج النسيج الليفي وإعادة تنظيمه يُسمّى:",
   P(("Angiogenesis", "تكوّن الأوعية"), ("Remodeling", "إعادة التشكيل"), ("Regeneration", "التجدّد"), ("Apoptosis", "الاستماتة")), "b"),
 Q("Repair begins within:", "يبدأ الإصلاح خلال:",
   P(("1 hour", "ساعة واحدة"), ("24 hours", "24 ساعة"), ("3 to 5 days", "3 إلى 5 أيام"), ("2 weeks", "أسبوعين")), "b"),
 Q("Granulation tissue becomes apparent by:", "يظهر النسيج الحبيبي بحلول:",
   P(("6 hours", "6 ساعات"), ("24 hours", "24 ساعة"), ("3 to 5 days", "3 إلى 5 أيام"), ("1 month", "شهر")), "c"),
 Q("Granulation tissue has a pink, granular appearance due to:", "للنسيج الحبيبي مظهر وردي حبيبي بسبب:",
   P(("Fibroblasts, connective tissue, abundant vessels and leukocytes", "الخلايا الليفية والنسيج الضام والأوعية الوفيرة والكريات البيض"), ("Epithelial cells only", "الخلايا الظهارية فقط"), ("Red blood cells only", "كريات الدم الحمر فقط"), ("Calcium deposits", "ترسّبات الكالسيوم")), "a"),
 Q("The main inflammatory cells in granulation tissue are:", "الخلايا الالتهابية الرئيسة في النسيج الحبيبي هي:",
   P(("Neutrophils", "العدلات"), ("Eosinophils", "الحمضات"), ("Macrophages", "البلاعم"), ("Mast cells", "الخلايا البدينة")), "c"),
 Q("The term granulation tissue derives from its:", "اشتُقّ مصطلح النسيج الحبيبي من:",
   P(("Gross appearance", "مظهره العياني"), ("Microscopic granules", "حبيبات مجهرية"), ("Chemical composition", "تركيبه الكيميائي"), ("Location in bone", "موقعه في العظم")), "a"),

 {"topic_en": "Cell proliferation", "topic_ar": "تكاثر الخلايا"},
 Q("Vascular endothelial cells proliferate during repair to:", "تتكاثر الخلايا البطانية الوعائية أثناء الإصلاح لـ:",
   P(("Form the scar", "تكوين الندبة"), ("Create new vessels that provide nutrients", "تكوين أوعية جديدة توفّر المغذّيات"), ("Restore normal structure", "استعادة البنية الطبيعية"), ("Kill microbes", "قتل الميكروبات")), "b"),
 Q("The source of the fibrous tissue that forms the scar is:", "مصدر النسيج الليفي الذي يكوّن الندبة هو:",
   P(("Endothelial cells", "الخلايا البطانية"), ("Fibroblasts", "الخلايا الليفية"), ("Macrophages", "البلاعم"), ("Neurons", "الخلايا العصبية")), "b"),
 Q("The proliferation of cells during repair is driven by:", "يُحفَّز تكاثر الخلايا أثناء الإصلاح بـ:",
   P(("Growth factors", "عوامل النمو"), ("Antibodies", "الأضداد"), ("Complement", "المتمّمة"), ("Hemoglobin", "الهيموغلوبين")), "a"),
 Q("The normal size of cell populations is determined by a balance among all EXCEPT:", "يتحدّد الحجم الطبيعي للتجمّعات الخلوية بالتوازن بين كل ما يأتي عدا:",
   P(("Cell proliferation", "تكاثر الخلايا"), ("Cell death by apoptosis", "موت الخلايا بالاستماتة"), ("Emergence of differentiated cells from stem cells", "ظهور خلايا متمايزة من الخلايا الجذعية"), ("Collagen deposition", "ترسيب الكولاجين")), "d"),
 Q("The key processes in the proliferation of cells are:", "العمليتان الأساسيتان في تكاثر الخلايا هما:",
   P(("DNA replication and mitosis", "تضاعف الـDNA والانقسام الخيطي"), ("Apoptosis and necrosis", "الاستماتة والنخر"), ("Transcription and translation", "النسخ والترجمة"), ("Phagocytosis and chemotaxis", "البلعمة والانجذاب الكيميائي")), "a"),

 {"topic_en": "Proliferative capacities of tissues", "topic_ar": "القدرات التكاثرية للأنسجة"},
 Q("Hematopoietic cells in the bone marrow are:", "الخلايا المكوّنة للدم في نقي العظم:",
   P(("Labile cells", "خلايا متقلّبة"), ("Stable cells", "خلايا مستقرة"), ("Permanent cells", "خلايا دائمة"), ("Terminally differentiated", "متمايزة نهائيًا")), "a"),
 Q("Liver, kidney and pancreas parenchyma are:", "متن الكبد والكلية والبنكرياس:",
   P(("Labile", "متقلّب"), ("Stable", "مستقر"), ("Permanent", "دائم"), ("Embryonic", "جنيني")), "b"),
 Q("Which tissue is permanent:", "أي نسيج دائم:",
   P(("Skin epithelium", "ظهارة الجلد"), ("Liver", "الكبد"), ("Cardiac muscle", "عضلة القلب"), ("Bone marrow", "نقي العظم")), "c"),
 Q("Stable cells in their normal state are:", "الخلايا المستقرة في حالتها الطبيعية:",
   P(("Continuously dividing", "دائمة الانقسام"), ("Quiescent with minimal replicative activity", "ساكنة ونشاطها التضاعفي ضئيل"), ("Unable to divide ever", "عاجزة عن الانقسام أبدًا"), ("Undifferentiated", "غير متمايزة")), "b"),
 Q("Injury to the brain or heart results in:", "تنتهي إصابة الدماغ أو القلب بـ:",
   P(("Complete regeneration", "تجدّد كامل"), ("A scar", "ندبة"), ("Hyperplasia", "فرط تنسّج"), ("No change", "لا تغيير")), "b"),
 Q("Labile tissues can readily regenerate as long as:", "تتجدّد الأنسجة المتقلّبة بسهولة ما دام:",
   P(("The pool of stem cells is preserved", "مخزون الخلايا الجذعية محفوظًا"), ("Collagen is deposited", "الكولاجين مترسّبًا"), ("Infection is present", "العدوى موجودة"), ("Steroids are given", "الستيرويدات معطاة")), "a"),

 {"topic_en": "Factors that influence repair", "topic_ar": "العوامل المؤثّرة في الإصلاح"},
 Q("Clinically the most important cause of delay in healing is:", "أهم سبب سريري لتأخّر الالتئام هو:",
   P(("Foreign bodies", "الأجسام الغريبة"), ("Infection", "العدوى"), ("Diabetes", "السكري"), ("Vitamin C deficiency", "نقص فيتامين C")), "b"),
 Q("Vitamin C deficiency retards healing by inhibiting:", "يؤخّر نقص فيتامين C الالتئام بتثبيط:",
   P(("Angiogenesis", "تكوّن الأوعية"), ("Collagen synthesis", "تخليق الكولاجين"), ("Mitosis", "الانقسام"), ("Apoptosis", "الاستماتة")), "b"),
 Q("Glucocorticoids may result in weakness of the scar because of inhibition of:", "قد تسبّب القشرانيات السكرية ضعف الندبة بسبب تثبيط:",
   P(("TGF-β production", "إنتاج TGF-β"), ("Vitamin C", "فيتامين C"), ("Hemoglobin", "الهيموغلوبين"), ("Stem cells", "الخلايا الجذعية")), "a"),
 Q("Poor perfusion that impairs healing may be due to all EXCEPT:", "قد يكون ضعف التروية المعيق للالتئام بسبب كل ما يأتي عدا:",
   P(("Arteriosclerosis", "تصلّب الشرايين"), ("Diabetes", "السكري"), ("Varicose veins", "دوالي الأوردة"), ("Protein-rich diet", "غذاء غني بالبروتين")), "d"),
 Q("An example of an extrinsic factor that modifies healing is:", "مثال على عامل خارجي يعدّل الالتئام:",
   P(("Infection", "العدوى"), ("Stem cells", "الخلايا الجذعية"), ("Growth factors", "عوامل النمو"), ("Fibroblasts", "الخلايا الليفية")), "a"),

 {"topic_en": "Stem cells", "topic_ar": "الخلايا الجذعية"},
 Q("Stem cells are characterized by:", "تتميّز الخلايا الجذعية بـ:",
   P(("Self-renewal and asymmetric replication", "التجدّد الذاتي والتضاعف غير المتناظر"), ("Terminal differentiation", "التمايز النهائي"), ("Short life", "قصر العمر"), ("Inability to divide", "العجز عن الانقسام")), "a"),
 Q("In asymmetric replication:", "في التضاعف غير المتناظر:",
   P(("Both daughter cells differentiate", "تتمايز الخليتان البنتان"), ("Both remain stem cells", "تبقى الخليتان جذعيتين"), ("One differentiates and the other remains a stem cell", "تتمايز إحداهما وتبقى الأخرى خلية جذعية"), ("The cell dies", "تموت الخلية")), "c"),
 Q("In the skin and GI tract, stem cells live near:", "في الجلد والقناة الهضمية تعيش الخلايا الجذعية قرب:",
   P(("The surface", "السطح"), ("The basal layer of the epithelium", "الطبقة القاعدية للظهارة"), ("The blood vessels", "الأوعية الدموية"), ("The lumen", "التجويف")), "b"),
 Q("Embryonic stem cells are present in:", "توجد الخلايا الجذعية الجنينية في:",
   P(("Bone marrow", "نقي العظم"), ("The inner cell mass of the blastocyst", "كتلة الخلايا الداخلية للكيسة الأريمية"), ("The liver", "الكبد"), ("The basal layer of the skin", "الطبقة القاعدية للجلد")), "b"),
 Q("ES cells can be maintained in culture without differentiating for:", "يمكن إبقاء الخلايا الجنينية في المزرعة دون تمايز:",
   P(("A few hours", "بضع ساعات"), ("One week", "أسبوعًا"), ("Over a year", "أكثر من سنة"), ("Never", "أبدًا")), "c"),
 Q("Compared with ES cells, adult stem cells have:", "مقارنةً بالخلايا الجنينية، للخلايا الجذعية البالغة:",
   P(("Wider lineage potential", "قدرة سلالية أوسع"), ("More limited self-renewal", "تجدّد ذاتي محدود أكثر"), ("Ability to form all three germ layers", "قدرة على تكوين الطبقات الثلاث"), ("No self-renewal", "لا تجدّد ذاتي")), "b"),

 {"topic_en": "Picture questions", "topic_ar": "أسئلة الصور"},
 Q("In this figure, the outcome after severe injury is:", "في هذا الشكل تكون النتيجة بعد الإصابة الشديدة:",
   P(("Regeneration", "التجدّد"), ("Scar formation", "تكوّن الندبة"), ("Normal epithelium", "ظهارة طبيعية"), ("Hyperplasia", "فرط التنسّج")), "b", img="assets/regeneration-vs-scar.jpg", img_h="42mm"),
 Q("The phase labelled S in this cycle is:", "الطور المعلَّم S في هذه الدورة هو:",
   P(("Growth", "النمو"), ("DNA synthesis", "تخليق الـDNA"), ("Mitosis", "الانقسام"), ("Preparation for mitosis", "التحضير للانقسام")), "b", img="assets/cell-cycle.jpg", img_h="40mm"),
 Q("This diagram shows a stem cell property called:", "يوضّح هذا المخطط خاصية للخلية الجذعية تُسمّى:",
   P(("Asymmetric replication", "التضاعف غير المتناظر"), ("Apoptosis", "الاستماتة"), ("Terminal differentiation", "التمايز النهائي"), ("Angiogenesis", "تكوّن الأوعية")), "a", img="assets/stem-cell-division.png", img_h="36mm"),
]

tf = [
 TF("Repair occurs by regeneration and scar formation.", "يحدث الإصلاح بالتجدّد وتكوّن الندبة.", "T"),
 TF("The fibrous scar can perform the function of lost parenchymal cells.", "تستطيع الندبة الليفية أداء وظيفة الخلايا المتنية المفقودة.", "F"),
 TF("The liver is a parenchymal organ that can regenerate.", "الكبد عضو متني قادر على التجدّد.", "T"),
 TF("Repair begins within 24 hours of injury.", "يبدأ الإصلاح خلال 24 ساعة من الإصابة.", "T"),
 TF("Granulation tissue is apparent within 6 hours.", "يظهر النسيج الحبيبي خلال 6 ساعات.", "F"),
 TF("The main inflammatory cells in granulation tissue are macrophages.", "الخلايا الالتهابية الرئيسة في النسيج الحبيبي هي البلاعم.", "T"),
 TF("Fibroblasts are the source of the fibrous tissue of the scar.", "الخلايا الليفية مصدر النسيج الليفي للندبة.", "T"),
 TF("Neurons are stable cells.", "الخلايا العصبية خلايا مستقرة.", "F"),
 TF("Stable cells can proliferate in response to injury.", "تستطيع الخلايا المستقرة التكاثر استجابةً للإصابة.", "T"),
 TF("Infection is clinically the most important cause of delay in healing.", "العدوى سريريًا أهم سبب لتأخّر الالتئام.", "T"),
 TF("Glucocorticoids strengthen the scar.", "القشرانيات السكرية تقوّي الندبة.", "F"),
 TF("Embryonic stem cells are the most undifferentiated stem cells.", "الخلايا الجذعية الجنينية أقل الخلايا الجذعية تمايزًا.", "T"),
 TF("Adult stem cells can form cells of all three germ layers.", "تستطيع الخلايا الجذعية البالغة تكوين خلايا الطبقات الجرثومية الثلاث.", "F"),
 TF("Foreign bodies impede healing.", "تعيق الأجسام الغريبة الالتئام.", "T"),
]
traps = [
 TR("24 hours or 3 to 5 days?", "24 ساعة أم 3 إلى 5 أيام؟", "Repair begins within 24 hours; granulation tissue is apparent by 3 to 5 days.", "يبدأ الإصلاح خلال 24 ساعة؛ ويظهر النسيج الحبيبي بحلول 3 إلى 5 أيام."),
 TR("Labile, stable or permanent?", "متقلّب أم مستقر أم دائم؟", "Labile: bone marrow, surface epithelia. Stable: liver, kidney, pancreas. Permanent: neurons, cardiac muscle.", "المتقلّب: نقي العظم والظهارات السطحية. المستقر: الكبد والكلية والبنكرياس. الدائم: الخلايا العصبية وعضلة القلب."),
 TR("Which inflammatory cell dominates granulation tissue?", "أي خلية التهابية تغلب على النسيج الحبيبي؟", "Macrophages — not neutrophils.", "البلاعم — وليس العدلات."),
 TR("Why do steroids weaken the scar?", "لماذا تُضعف الستيرويدات الندبة؟", "They inhibit TGF-β production and diminish fibrosis.", "لأنها تثبّط إنتاج TGF-β وتقلّل التليّف."),
 TR("ES or adult stem cells — which is more limited?", "الجنينية أم البالغة — أيها أكثر محدودية؟", "Adult (tissue) stem cells: more limited self-renewal and restricted lineage potential.", "البالغة (النسيجية): تجدّد ذاتي أكثر محدودية وقدرة سلالية مقتصرة."),
 TR("Most important cause of delayed healing?", "أهم سبب لتأخّر الالتئام؟", "Infection (extrinsic) — not nutrition or foreign bodies.", "العدوى (عامل خارجي) — وليس التغذية أو الأجسام الغريبة."),
]
important = [
 IM("Define repair and mention its two types of reactions.", "عرّف الإصلاح واذكر نوعي تفاعلاته.", "Repair (healing) is the restoration of tissue architecture and function after an injury; it occurs by regeneration of the injured tissue and by scar formation (deposition of connective tissue).", "الإصلاح (الالتئام) هو استعادة بنية النسيج ووظيفته بعد الإصابة؛ ويحدث بتجدّد النسيج المصاب وبتكوّن الندبة (ترسيب النسيج الضام)."),
 IM("Define regeneration and how it occurs.", "عرّف التجدّد وكيف يحدث.", "Replacement of damaged cells with return to a normal state; occurs by proliferation of residual uninjured cells and replacement from tissue stem cells (skin, intestines, liver).", "تعويض الخلايا التالفة مع العودة إلى الحالة الطبيعية؛ ويحدث بتكاثر الخلايا المتبقية غير المصابة والتعويض من الخلايا الجذعية النسيجية (الجلد، الأمعاء، الكبد)."),
 IM("List the steps in scar formation.", "عدّد خطوات تكوّن الندبة.", "1) Angiogenesis; 2) migration and proliferation of fibroblasts and deposition of connective tissue (granulation tissue); 3) maturation and reorganization (remodeling) into a stable fibrous scar.", "1) تكوّن الأوعية؛ 2) هجرة الخلايا الليفية وتكاثرها وترسيب النسيج الضام (النسيج الحبيبي)؛ 3) النضج وإعادة التشكيل إلى ندبة ليفية مستقرة."),
 IM("Describe granulation tissue.", "صف النسيج الحبيبي.", "Named from its gross appearance beneath a scab; histologically: proliferating fibroblasts and new thin-walled capillaries in a loose ECM with inflammatory cells (mainly macrophages); fibroblasts lay down collagen forming a scar.", "سُمّي من مظهره العياني تحت القشرة؛ نسيجيًا: خلايا ليفية متكاثرة وشعيرات جديدة رقيقة الجدار في مادة خارج خلوية رخوة مع خلايا التهابية (أهمها البلاعم)؛ وترسّب الخلايا الليفية الكولاجين فتتكوّن الندبة."),
 IM("Classify tissues according to their proliferative capacity with examples.", "صنّف الأنسجة بحسب قدرتها التكاثرية مع أمثلة.", "Labile (continuously dividing): bone marrow, surface epithelia. Stable (quiescent, divide after injury): liver, kidney, pancreas. Permanent (non-proliferative): neurons, cardiac muscle — repair by scar.", "المتقلّبة (دائمة الانقسام): نقي العظم والظهارات السطحية. المستقرة (ساكنة وتنقسم بعد الإصابة): الكبد والكلية والبنكرياس. الدائمة (غير متكاثرة): الخلايا العصبية وعضلة القلب — يكون الإصلاح بندبة."),
 IM("List the factors that influence tissue repair.", "عدّد العوامل المؤثّرة في إصلاح النسيج.", "Infection, nutrition (protein and vitamin C deficiency), glucocorticoids, poor perfusion (arteriosclerosis, diabetes, varicose veins), foreign bodies.", "العدوى، التغذية (نقص البروتين وفيتامين C)، القشرانيات السكرية، ضعف التروية (تصلّب الشرايين، السكري، دوالي الأوردة)، الأجسام الغريبة."),
 IM("What are the properties of stem cells? Explain asymmetric replication.", "ما خصائص الخلايا الجذعية؟ اشرح التضاعف غير المتناظر.", "Self-renewal capacity and asymmetric replication: on division one daughter cell differentiates into mature cells while the other remains an undifferentiated stem cell.", "القدرة على التجدّد الذاتي والتضاعف غير المتناظر: عند الانقسام تتمايز إحدى الخليتين البنتين إلى خلايا ناضجة وتبقى الأخرى خلية جذعية غير متمايزة."),
 IM("Compare embryonic and adult stem cells.", "قارن بين الخلايا الجذعية الجنينية والبالغة.", "ES: most undifferentiated, inner cell mass of blastocyst, extensive renewal, all three germ layers. Adult: less undifferentiated, among differentiated cells of an organ, limited renewal, lineage restricted to its tissue.", "الجنينية: الأقل تمايزًا، في كتلة الخلايا الداخلية للكيسة الأريمية، تجدّد واسع، الطبقات الثلاث. البالغة: أكثر تمايزًا، بين خلايا العضو المتمايزة، تجدّد محدود، وقدرة سلالية مقتصرة على نسيجها."),
]
mcq = balance(mcq, 5)
meta = dict(subject_en="Histopathology", subject_ar="علم الأمراض النسيجية", short_ar="انسجة",
            unit_en="Lecture 4", unit_ar="المحاضرة 4", unit_label="LEC", unit_no="4",
            title_en="Healing and Regeneration", title_ar="الالتئام والتجدّد",
            kind="Theory — نظري", stage="The third stage — الثالثة", instructor="د. حامد خليل التميمي")
save("histopathology-lec4-healing-regeneration", meta, blocks, mcq, tf, traps, important)

```
