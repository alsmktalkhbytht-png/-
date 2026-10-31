---
source: BIOS-Obsidian/tools/scripts/iml3/l3q.py
handouts: [immunology-lab3-antigen-preparation]
saved: 2026-10-31
tags: [bios, code]
---
# iml3/l3q.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#immunology-lab3-antigen-preparation|immunology-lab3-antigen-preparation]]

```python
mcq = [
 {"topic_en": "Antigens", "topic_ar": "المستضدات"},
 Q("An antigen is a macromolecule that:", "المستضد جزيء كبير:", O(("Induces formation of antibody that reacts specifically with it", "يحفّز تكوين ضد يتفاعل معه نوعيًا"), ("Kills bacteria directly", "يقتل البكتيريا مباشرةً"), ("Is always a lipid", "يكون دائمًا دهنًا"), ("Is produced by B cells", "تنتجه الخلايا البائية")), "a"),
 Q("The molecular weight of a good antigen is:", "الوزن الجزيئي للمستضد الجيّد:", O(("< 1000 Dalton", "أقل من 1000 دالتون"), ("> 10000 Dalton", "أكبر من 10000 دالتون"), ("Exactly 500 Dalton", "500 دالتون بالضبط"), ("Not important", "غير مهم")), "b"),
 Q("Which is NOT a main characteristic of an antigen?", "أيّ مما يأتي ليس من الصفات الرئيسية للمستضد؟", O(("Foreignness", "الغرابة"), ("Chemical complexity", "التعقيد الكيميائي"), ("Low molecular weight", "الوزن الجزيئي المنخفض"), ("High molecular weight", "الوزن الجزيئي العالي")), "c"),
 Q("Which is a type of antigen prepared commercially?", "أيّ مما يأتي من أنواع المستضدات المحضّرة تجاريًا؟", O(("Antibody", "الضد"), ("Complement", "المتمّم"), ("Formal-saline", "الفورمال-سلاين"), ("Recombinant proteins", "البروتينات المؤشبة")), "d"),
 Q("A vaccine is introduced into the body:", "يُدخل اللقاح إلى الجسم:", O(("Artificially, to produce antibodies", "اصطناعيًا لإنتاج الأضداد"), ("Naturally by infection", "طبيعيًا بالإصابة"), ("To kill the antigen", "لقتل المستضد"), ("Only in animals", "في الحيوانات فقط")), "a"),
 Q("Antigens entering from outside by inhalation, ingestion or injection are:", "المستضدات التي تدخل من الخارج بالاستنشاق أو الابتلاع أو الحقن هي:", O(("Endogenous", "داخلية"), ("Exogenous", "خارجية"), ("Auto antigens", "ذاتية"), ("Haptens", "ناقصة")), "b"),
 Q("Uptake of exogenous antigens by APCs is mainly by:", "التقاط الخلايا المقدّمة للمستضدات الخارجية يكون غالبًا بـ:", O(("Diffusion", "الانتشار"), ("Active transport", "النقل الفعّال"), ("Phagocytosis", "البلعمة"), ("Filtration", "الترشيح")), "c"),
 Q("An example of an endogenous antigen is:", "مثال على المستضد الداخلي:", O(("Bacteria", "البكتيريا"), ("Viruses", "الفيروسات"), ("Fungi", "الفطريات"), ("Blood group antigens and HLA", "مستضدات فصائل الدم وHLA")), "d"),
 Q("Endogenous antigens are processed by macrophages and later accepted by:", "تعالج البلاعم المستضدات الداخلية ثم تستقبلها:", O(("Cytotoxic T – cells", "الخلايا التائية السامّة للخلايا"), ("Neutrophils", "العدلات"), ("Red cells", "الكريات الحمر"), ("Platelets", "الصفيحات")), "a"),
 Q("Auto antigens become immunogenic when:", "تصبح المستضدات الذاتية مولّدة للمناعة عندما:", O(("They are injected", "تُحقن"), ("Immunological tolerance is lost", "يُفقد التحمّل المناعي"), ("They are boiled", "تُغلى"), ("They enter by inhalation", "تدخل بالاستنشاق")), "b"),
 Q("Which is NOT a property of formal-saline?", "أيّ مما يأتي ليس من خصائص الفورمال-سلاين؟", O(("Kills microorganisms", "يقتل الأحياء المجهرية"), ("Fixes the flagella on the cell wall", "يثبّت الأسواط على جدار الخلية"), ("Helps bacteria grow", "يساعد البكتيريا على النمو"), ("Keeps it for a long time", "يحفظه مدّة طويلة")), "c"),
 {"topic_en": "Bacterial antigens", "topic_ar": "المستضدات البكتيرية"},
 Q("The capsule antigen is written as:", "يُكتب مستضد المحفظة:", O(("LPS", "LPS"), ("PGN", "PGN"), ("EPS", "EPS"), ("Vi", "Vi")), "d"),
 Q("The Salmonella somatic (O) antigen is:", "المستضد الجسمي (O) للسالمونيلا:", O(("Stable at 100 °C and in alcohol", "ثابت عند 100 °م وفي الكحول"), ("A flagellar protein", "بروتين سوطي"), ("Inactivated above 60 °C", "يتعطّل فوق 60 °م"), ("Found on the flagella", "يوجد على الأسواط")), "a"),
 Q("The Salmonella H antigen is:", "المستضد H للسالمونيلا:", O(("A lipid complex", "معقّد دهني"), ("A flagellar protein inactivated above 60 °C", "بروتين سوطي يتعطّل فوق 60 °م"), ("Stable at 100 °C", "ثابت عند 100 °م"), ("On the capsule", "على المحفظة")), "b"),
 Q("For O antigen preparation, Salmonella colonies are taken from:", "لتحضير مستضد O تؤخذ مستعمرات السالمونيلا من:", O(("Blood agar", "آجار الدم"), ("MacConkey broth", "مرق ماكونكي"), ("S.S agar", "آجار S.S"), ("Todd-Hewitt broth", "مرق تود-هيويت")), "c"),
 Q("In O antigen preparation the bacteria are killed by:", "في تحضير مستضد O تُقتل البكتيريا بـ:", O(("0.6% formal saline for 5 days", "فورمال-سلاين 0.6% لمدّة 5 أيام"), ("Methiolate", "الميثيولات"), ("Freezing", "التجميد"), ("Boiling water bath for 3.5 hr then 1.5 hr", "حمّام ماء مغلي 3.5 ساعة ثم 1.5 ساعة")), "d"),
 Q("The washed O antigen product has the appearance of:", "مظهر ناتج مستضد O المغسول يشبه:", O(("Skim milk", "الحليب منزوع الدسم"), ("Clear water", "الماء الصافي"), ("Blood", "الدم"), ("Jelly", "الهلام")), "a"),
 Q("O antigen is stored in:", "يُحفظ مستضد O في:", O(("0.6% formal saline at room temperature", "فورمال-سلاين 0.6% بحرارة الغرفة"), ("0.3% formal saline at 4 °C", "فورمال-سلاين 0.3% بدرجة 4 °م"), ("Alsever's solution", "محلول ألسيفر"), ("Methiolate at 37 °C", "ميثيولات بدرجة 37 °م")), "b"),
 Q("For H antigen preparation, the broth culture is treated with:", "لتحضير مستضد H يُعالج مرق المزرعة بـ:", O(("Boiling for 3.5 hr", "الغلي 3.5 ساعة"), ("Alcohol", "الكحول"), ("250 ml of 0.6% formal saline for 5 days", "250 مل فورمال-سلاين 0.6% لمدّة 5 أيام"), ("Cholesterol", "الكوليسترول")), "c"),
 {"topic_en": "Streptolysin O", "topic_ar": "الستربتوليسين O"},
 Q("Streptolysin O is a protein of:", "الستربتوليسين O بروتين وزنه:", O(("10 kDa", "10 كيلو دالتون"), ("150 kDa", "150 كيلو دالتون"), ("1000 kDa", "1000 كيلو دالتون"), ("67 kDa", "67 كيلو دالتون")), "d"),
 Q("Streptolysin O is inhibited by:", "يُثبَّط الستربتوليسين O بـ:", O(("Cholesterol and related sterols", "الكوليسترول والستيرولات المشابهة"), ("Sulfhydryl compounds", "مركّبات السلفهيدريل"), ("Reducing agents", "العوامل المختزلة"), ("Saline", "المحلول الملحي")), "a"),
 Q("For better SLO production the organisms are grown in:", "لإنتاج أفضل للـ SLO تُنمّى الأحياء في:", O(("A fat-rich medium", "وسط غني بالدهون"), ("A fat free, reducing agent containing medium (kalbak broth)", "وسط خالٍ من الدهون ويحتوي عاملًا مختزلًا (مرق كالباك)"), ("S.S agar", "آجار S.S"), ("Blood agar", "آجار الدم")), "b"),
 Q("SLO culture is incubated for:", "تُحضن مزرعة SLO لمدّة:", O(("5 days at room temperature", "5 أيام بحرارة الغرفة"), ("3.5 hours in boiling water", "3.5 ساعة في الماء المغلي"), ("15 hrs at 37 °C", "15 ساعة بدرجة 37 °م"), ("1 month at 4 °C", "شهر بدرجة 4 °م")), "c"),
 Q("SLO is collected from the:", "يُجمع SLO من:", O(("Bacterial cells", "الخلايا البكتيرية"), ("Precipitate", "الراسب"), ("Colonies on agar", "المستعمرات على الآجار"), ("Filtrate after filtration", "الراشح بعد الترشيح")), "d"),
 {"topic_en": "RBC antigens", "topic_ar": "مستضدات الكريات الحمر"},
 Q("ABO blood group antigens are composed of:", "تتكوّن مستضدات فصائل ABO من:", O(("Sugars", "سكريات"), ("Proteins", "بروتينات"), ("Lipids only", "دهون فقط"), ("Nucleic acids", "أحماض نووية")), "a"),
 Q("Rh antigens are composed of:", "تتكوّن مستضدات Rh من:", O(("Sugars", "سكريات"), ("Proteins", "بروتينات"), ("Cholesterol", "كوليسترول"), ("DNA", "DNA")), "b"),
 Q("The purpose of RBC preparation is:", "الغرض من تحضير الكريات الحمر:", O(("To make a vaccine", "صنع لقاح"), ("To grow bacteria", "تنمية البكتيريا"), ("To prepare RBCs suspensions for serologic testing", "تحضير عوالق الكريات الحمر للفحوص المصلية"), ("To measure hemoglobin", "قياس الهيموغلوبين")), "c"),
 Q("The RBC suspension is centrifuged for:", "يُنبذ عالق الكريات الحمر لمدّة:", O(("15 min at 1000 RPM", "15 دقيقة بسرعة 1000"), ("1 hr at 500 RPM", "ساعة بسرعة 500"), ("30 s at 10000 RPM", "30 ثانية بسرعة 10000"), ("5 min at 3000 RPM", "5 دقائق بسرعة 3000")), "d"),
 Q("For long storage, red cells are kept in:", "للحفظ الطويل تُحفظ الكريات الحمر في:", O(("Alsever's solution", "محلول ألسيفر"), ("Normal saline", "المحلول الملحي الطبيعي"), ("Formal-saline 0.6%", "فورمال-سلاين 0.6%"), ("Distilled water", "الماء المقطّر")), "a"),
 Q("The anticoagulant tube used for RBC antigen preparation is:", "أنبوب مانع التخثّر المستعمل لتحضير مستضد الكريات الحمر:", O(("Citrate", "السترات"), ("EDTA", "EDTA"), ("Heparin", "الهيبارين"), ("Plain tube", "أنبوب بلا مانع")), "b"),
 {"topic_en": "Picture question", "topic_ar": "سؤال صورة"},
 Q("In this figure, the coloured shapes that fit on the tips of the Y-shaped molecule are:", "في هذا الشكل، الأشكال الملوّنة التي تركب على أطراف الجزيء الذي يشبه حرف Y هي:", O(("Antibodies", "أضداد"), ("Red cells", "كريات حمر"), ("Antigens", "مستضدات"), ("Flagella", "أسواط")), "c", img="assets/antigen-antibody.png", img_h="42mm"),
]
mcq = balance(mcq, 23)

tf = [
 TF("An antigen must be foreign to the body.", "يجب أن يكون المستضد غريبًا عن الجسم.", "T"),
 TF("Synthetic peptides are a type of commercially prepared antigen.", "الببتيدات المصنّعة نوع من المستضدات المحضّرة تجاريًا.", "T"),
 TF("Exogenous antigens originate from the host's own body.", "المستضدات الخارجية تنشأ من جسم المضيف نفسه.", "F"),
 TF("Auto antigens are immunogenic under normal conditions.", "المستضدات الذاتية مولّدة للمناعة في الظروف الطبيعية.", "F"),
 TF("Formal-saline fixes the flagella on the cell wall.", "يثبّت الفورمال-سلاين الأسواط على جدار الخلية.", "T"),
 TF("Peptidoglycan is one of the cell membrane antigens of bacteria.", "الببتيدوغلايكان أحد مستضدات غشاء الخلية البكتيرية.", "T"),
 TF("The Salmonella H antigen is stable at 100 °C.", "المستضد H للسالمونيلا ثابت عند 100 °م.", "F"),
 TF("O antigen sterility is shown by no turbidity in brain heart infusion broth and no growth on S.S agar.", "تُثبت عقامة مستضد O بعدم العكارة في مرق نقيع الدماغ والقلب وعدم النمو على آجار S.S.", "T"),
 TF("In H antigen preparation the supernatant is kept and the precipitate discarded.", "في تحضير مستضد H يُحتفظ بالطافي ويُرمى الراسب.", "F"),
 TF("Streptolysin O is formed by pyogenic streptococci.", "يتكوّن الستربتوليسين O بواسطة المكوّرات السبحية المقيّحة.", "T"),
 TF("Streptolysin O is activated by sulfhydryl compounds.", "ينشّط الستربتوليسين O بمركّبات السلفهيدريل.", "T"),
 TF("Properly stored SLO loses its potency after one week.", "يفقد SLO المحفوظ جيدًا فعاليته بعد أسبوع.", "F"),
 TF("A proper ratio of plasma to red cells is important for antigen-antibody reactions.", "النسبة الصحيحة بين البلازما والكريات الحمر مهمة لتفاعلات المستضد والضد.", "T"),
 TF("RBCs can be obtained by defibrinating clotted specimens.", "يمكن الحصول على الكريات الحمر بنزع الفايبرين من العيّنات المتخثّرة.", "T"),
]

traps = [
 TR("O vs H — which survives boiling?", "O مقابل H — أيّهما يتحمّل الغلي؟", "O (somatic) is stable at 100 °C and in alcohol, so it is prepared by boiling. H (flagellar) is a protein inactivated above 60 °C, so it is killed with formal saline instead.", "O (الجسمي) ثابت عند 100 °م وفي الكحول، لذلك يُحضَّر بالغلي. أما H (السوطي) فبروتين يتعطّل فوق 60 °م، لذلك يُقتل بالفورمال-سلاين بدل الغلي."),
 TR("0.6% or 0.3% formal saline?", "فورمال-سلاين 0.6% أم 0.3%؟", "0.6% is added to kill the H culture (5 days); 0.3% is the storage solution for both O and H at 4 °C.", "0.6% يُضاف لقتل مزرعة H (5 أيام)؛ و0.3% هو محلول الحفظ لكلا O وH بدرجة 4 °م."),
 TR("SLO: activated vs inhibited", "SLO: ما ينشّطه مقابل ما يثبّطه", "Activated by sulfhydryl compounds; inhibited by cholesterol and related sterols — so it is grown in a fat-free, reducing medium.", "ينشّطه السلفهيدريل؛ ويثبّطه الكوليسترول والستيرولات — لذلك يُنمّى في وسط خالٍ من الدهون ومختزل."),
 TR("1 month or many years?", "شهر أم سنوات؟", "SLO in the filtrate got inactivated after 1 month; but SLO prepared and properly stored keeps constant potency for many years (as the lecture states both).", "الـ SLO في الراشح يتعطّل بعد شهر؛ لكن الـ SLO المحضّر والمحفوظ جيدًا يبقى بفعالية ثابتة لسنوات (المحاضرة تذكر الاثنين)."),
 TR("ABO vs Rh antigens", "مستضدات ABO مقابل Rh", "ABO = sugars; Rh = proteins.", "ABO = سكريات؛ وRh = بروتينات."),
 TR("Saline or Alsever's?", "المحلول الملحي أم ألسيفر؟", "Saline for short time; Alsever's solution for long time.", "المحلول الملحي لمدّة قصيرة؛ ومحلول ألسيفر لمدّة طويلة."),
 TR("Two broths for SLO", "مرقان للـ SLO", "Grow first in Todd-Hewitt broth, then transfer 50 ml to 1000 ml of kalbak's broth.", "يُنمّى أولًا في مرق تود-هيويت، ثم يُنقل 50 مل إلى 1000 مل من مرق كالباك."),
]

important = [
 IM("Define antigen and list its main characteristics.", "عرّف المستضد واذكر صفاته الرئيسية.", "A macromolecule that induces formation of antibody which reacts specifically with it. Characteristics: high molecular weight > 10000 Dalton, foreignness, chemical complexity.", "جزيء كبير يحفّز تكوين ضد يتفاعل معه نوعيًا. الصفات: وزن جزيئي عالٍ > 10000 دالتون، والغرابة، والتعقيد الكيميائي."),
 IM("Classify antigens on the basis of source with examples.", "صنّف المستضدات حسب المصدر مع الأمثلة.", "Exogenous: foreign, enter from outside by inhalation, ingestion or injection, taken by APCs by phagocytosis (bacteria, fungi, viruses). Endogenous: from the host's own body, processed by macrophages and accepted by cytotoxic T cells (blood group antigens, HLA). Auto antigens: normal self proteins recognized in autoimmune disease after loss of tolerance (nucleoproteins, nucleic acids).", "الخارجية: غريبة تدخل من الخارج بالاستنشاق أو الابتلاع أو الحقن وتلتقطها APCs بالبلعمة (البكتيريا، الفطريات، الفيروسات). الداخلية: من جسم المضيف، تعالجها البلاعم وتستقبلها الخلايا التائية السامّة (مستضدات فصائل الدم، HLA). الذاتية: بروتينات ذاتية طبيعية يتعرّف عليها الجهاز المناعي في المرض المناعي الذاتي بعد فقدان التحمّل (البروتينات النووية، الأحماض النووية)."),
 IM("What are the properties of formal-saline?", "ما خصائص الفورمال-سلاين؟", "1. Kills microorganisms; 2. fixes the flagella on the cell wall; 3. keeps the antigen for a long time without deterioration; 4. masks the body of the bacterial cell.", "1. يقتل الأحياء المجهرية؛ 2. يثبّت الأسواط على جدار الخلية؛ 3. يحفظ المستضد مدّة طويلة دون تلف؛ 4. يحجب جسم الخلية البكتيرية."),
 IM("Compare the Salmonella O and H antigens.", "قارن بين مستضدي O وH للسالمونيلا.", "O (somatic): on the cell surface, lipid complex (polysaccharide), stable at 100 °C and in alcohol. H (flagellar): on the flagella, protein, inactivated above 60 °C.", "O (الجسمي): على سطح الخلية، معقّد دهني (عديد سكريد)، ثابت عند 100 °م وفي الكحول. H (السوطي): على الأسواط، بروتين، يتعطّل فوق 60 °م."),
 IM("Describe the preparation of the Salmonella somatic (O) antigen.", "صف تحضير المستضد الجسمي (O) للسالمونيلا.", "Streak Salmonella colonies from S.S agar onto brain heart infusion agar; incubate overnight at 37 °C; harvest with sterile saline; boil 250 ml suspension 3.5 hr, leave overnight, boil again 1.5 hr; wash 3 times with saline (skim-milk look); check sterility (no turbidity in BHI broth, no growth on S.S agar); store in 0.3% formal saline at 4 °C.", "خطّط مستعمرات السالمونيلا من آجار S.S على آجار نقيع الدماغ والقلب؛ احضن ليلة بدرجة 37 °م؛ احصد بمحلول ملحي معقّم؛ اغلِ 250 مل من العالق 3.5 ساعة، واتركه ليلة، ثم اغلِه 1.5 ساعة؛ اغسله 3 مرّات بالمحلول الملحي (مظهر الحليب منزوع الدسم)؛ افحص العقامة (لا عكارة في مرق BHI ولا نمو على S.S)؛ واحفظه في فورمال-سلاين 0.3% بدرجة 4 °م."),
 IM("Describe the preparation of streptolysin O antigen.", "صف تحضير مستضد الستربتوليسين O.", "Grow pyogenic streptococci in Todd-Hewitt broth; transfer 50 ml to 1000 ml kalbak's broth (fat free, reducing); incubate 15 hrs at 37 °C; check for haemolysin; filter off the cells; preserve the filtrate with methiolate; store at 4 °C. Properly stored SLO keeps constant potency for many years.", "نمِّ المكوّرات السبحية المقيّحة في مرق تود-هيويت؛ انقل 50 مل إلى 1000 مل من مرق كالباك (خالٍ من الدهون ومختزل)؛ احضن 15 ساعة بدرجة 37 °م؛ افحص الحالّ للدم؛ افصل الخلايا بالترشيح؛ احفظ الراشح بالميثيولات؛ وخزّنه بدرجة 4 °م. والـ SLO المحفوظ جيدًا يبقى بفعالية ثابتة لسنوات."),
 IM("Give the functions of RBC antigens and the procedure to prepare an RBC antigen.", "اذكر وظائف مستضدات الكريات الحمر وإجراء تحضير مستضد الكريات الحمر.", "Functions: determine blood group; ensure compatibility in transfusion (typing and cross matching); in pregnancy, the mother may form antibodies against fetal RBC antigens. Procedure: venepuncture → EDTA tube → add normal saline → centrifuge 5 min at 3000 RPM → discard supernatant, add saline → repeat → resuspend and standardize → store in saline (short) or Alsever's solution (long).", "الوظائف: تحديد فصيلة الدم؛ ضمان التوافق في نقل الدم (التحديد والمطابقة التصالبية)؛ وفي الحمل قد تكوّن الأم أضدادًا ضد مستضدات كريات الجنين. الإجراء: بزل وريدي ← أنبوب EDTA ← إضافة محلول ملحي ← نبذ 5 دقائق بسرعة 3000 ← التخلّص من الطافي وإضافة محلول ملحي ← التكرار ← إعادة التعليق والتوحيد ← الحفظ في المحلول الملحي (قصيرًا) أو محلول ألسيفر (طويلًا)."),
]

meta = {"subject_en": "Practical Immunology", "subject_ar": "علم المناعة العملي", "short_ar": "مناعة", "instructor": "م.م. جنان خليل",
        "unit_en": "Lab 3", "unit_ar": "العملي 3", "unit_label": "LAB", "unit_no": "3",
        "title_en": "Antigen preparation, bacterial Ag, R.B.Cs Ag, protein Ag", "title_ar": "تحضير المستضدات: المستضد البكتيري، مستضد الكريات الحمر، المستضد البروتيني",
        "department": "تقنيات المختبرات الطبية", "stage": "The third stage — الثالثة", "kind": "Laboratories — عملي"}
save("immunology-lab3-antigen-preparation", meta, blocks, mcq, tf, traps, important)

```
