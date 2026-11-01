---
source: BIOS-Obsidian/tools/scripts/vir4/v4q.py
handouts: [virology-lab4-isolation-cultivation]
saved: 2026-11-01
tags: [bios, code]
---
# vir4/v4q.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#virology-lab4-isolation-cultivation|virology-lab4-isolation-cultivation]]

```python
lab = [
 {"topic_en": "MCQs Lab Four (from the lab sheet)", "topic_ar": "أسئلة العملي الرابع (من ورقة العملي)"},
 Q("Why must viruses be cultivated in living cells:", "لماذا يجب زرع الفيروسات في خلايا حية:", O(("They synthesize their own proteins", "تصنّع بروتيناتها بنفسها"), ("They require host cells to replicate", "تحتاج خلايا مضيفة لتتضاعف"), ("They grow on artificial nutrient media", "تنمو على أوساط غذائية اصطناعية"), ("They divide by binary fission", "تنقسم بالانشطار الثنائي"), ("They produce ATP independently", "تنتج ATP بشكل مستقل")), "b"),
 Q("Which method uses immortalized cells that can be propagated indefinitely:", "أي طريقة تستعمل خلايا خالدة يمكن إكثارها إلى ما لا نهاية:", O(("Primary cell culture", "المزرعة الخلوية الأولية"), ("Embryonated egg culture", "الزرع في البيض المخصّب"), ("Continuous cell line", "الخط الخلوي المستمر"), ("Animal inoculation", "حقن الحيوانات"), ("Bacterial lawn culture", "زرع المرجة البكتيرية")), "c"),
 Q("Which is an example of a clinical specimen collected for viral isolation:", "أيّها مثال على عيّنة سريرية تُجمع لعزل الفيروس:", O(("Distilled water", "الماء المقطّر"), ("Blood", "الدم"), ("Agar powder", "مسحوق الآكار"), ("Culture flask", "قنينة الزرع"), ("Filter paper", "ورق الترشيح")), "b"),
 Q("During viral isolation, virions can be separated from host cells by:", "أثناء عزل الفيروس يمكن فصل الفيريونات عن الخلايا المضيفة بـ:", O(("Gram staining", "صبغة گرام"), ("Autoclaving", "التعقيم بالموصدة"), ("Centrifugation or filtration", "الطرد المركزي أو الترشيح"), ("Freezing only", "التجميد فقط"), ("Incubation in nutrient broth", "الحضن في مرق مغذٍّ")), "c"),
 Q("What happens to most viruses when a suitable membrane filter removes larger cells and bacteria:", "ماذا يحدث لمعظم الفيروسات عندما يزيل مرشّح غشائي مناسب الخلايا الأكبر والبكتيريا:", O(("They are retained on the filter surface", "تُحتجز على سطح المرشّح"), ("They pass into the filtrate", "تمرّ إلى الراشح"), ("They are destroyed immediately", "تتحطّم فورًا"), ("They become bacteria", "تصبح بكتيريا"), ("They form spores", "تكوّن أبواغًا")), "b"),
 Q("In bacteriophage cultivation, a clear zone in a bacterial lawn is called a:", "في زرع العاثيات تُسمّى المنطقة الصافية في المرجة البكتيرية:", O(("Colony", "مستعمرة"), ("Capsule", "محفظة"), ("Spore", "بوغ"), ("Plaque", "لويحة (بلاك)"), ("Biofilm", "غشاء حيوي")), "d"),
 Q("Why is 0.7% soft agar used for growing bacteriophages:", "لماذا يُستعمل الآكار الطري 0.7% لتنمية العاثيات:", O(("It kills host bacteria", "يقتل البكتيريا المضيفة"), ("It allows bacteriophages to diffuse easily", "يسمح للعاثيات بالانتشار بسهولة"), ("It prevents plaque formation", "يمنع تكوّن اللويحات"), ("It replaces the bacterial lawn", "يحلّ محلّ المرجة البكتيرية"), ("It inactivates viral particles", "يثبّط الجسيمات الفيروسية")), "b"),
 Q("Which of the following is an important purpose of animal-virus cultivation:", "أيّ ممّا يلي غرض مهمّ لزرع الفيروسات الحيوانية:", O(("Production of antibiotics", "إنتاج المضادّات الحيوية"), ("Identification and diagnosis of pathogenic viruses", "تحديد وتشخيص الفيروسات الممرضة"), ("Detection of fungal spores", "كشف الأبواغ الفطرية"), ("Preparation of bacterial stains", "تحضير الصبغات البكتيرية"), ("Production of artificial nutrient media", "إنتاج أوساط غذائية اصطناعية")), "b"),
 Q("Which method can directly visualize viral particles:", "أي طريقة تستطيع رؤية الجسيمات الفيروسية مباشرةً:", O(("Electron microscopy", "المجهر الإلكتروني"), ("Serological testing", "الفحص المصلي"), ("Gram staining", "صبغة گرام"), ("Bacterial culture", "الزرع البكتيري"), ("Antibiotic sensitivity testing", "فحص الحساسية للمضادّات")), "a"),
 Q("Which finding is considered a cytopathic effect of viral infection:", "أيّ نتيجة تُعدّ تأثيرًا مرضيًا خلويًا للإصابة الفيروسية:", O(("Formation of multinucleated syncytia", "تكوين مخلوّات متعدّدة النوى"), ("Production of bacterial endospores", "إنتاج أبواغ بكتيرية داخلية"), ("Increased cell adherence", "زيادة التصاق الخلايا"), ("Normal cell division", "انقسام خلوي طبيعي"), ("Formation of fungal hyphae", "تكوين خيوط فطرية")), "a"),
]

mine = [
 {"topic_en": "BIOS questions — methods and steps", "topic_ar": "أسئلة BIOS — الطرق والخطوات"},
 Q("The most common method of viral cultivation is:", "أكثر طرق زرع الفيروسات شيوعًا:", O(("Cell culture", "المزرعة الخلوية"), ("Animal inoculation", "حقن الحيوانات"), ("Embryonated eggs", "البيض المخصّب"), ("Artificial media", "الأوساط الاصطناعية")), "a"),
 Q("Primary cell cultures:", "المزارع الخلوية الأولية:", O(("Are immortal", "خالدة"), ("Have a limited lifespan", "لها عمر محدود"), ("Come from tumors", "تأتي من الأورام"), ("Are not affected by contact inhibition", "لا تتأثّر بتثبيط التماس")), "b"),
 Q("Rabies and poliovirus are cultivated by:", "يُزرع داء الكلب وفيروس شلل الأطفال بـ:", O(("Embryonated eggs", "البيض المخصّب"), ("Bacterial lawn", "المرجة البكتيرية"), ("Animal inoculation", "حقن الحيوانات"), ("Soft agar", "الآكار الطري")), "c"),
 Q("Influenza and herpes simplex viruses can be cultivated in:", "يمكن زرع فيروسات الإنفلونزا والهربس البسيط في:", O(("Artificial media", "الأوساط الاصطناعية"), ("1.5% agar", "آكار 1.5%"), ("Filter paper", "ورق الترشيح"), ("Embryonated eggs", "البيض المخصّب")), "d"),
 Q("Removing antibiotics or bacteria from a specimen is the step of:", "إزالة المضادّات الحيوية أو البكتيريا من العيّنة هي خطوة:", O(("Sample preparation", "تحضير العيّنة"), ("Inoculation", "التلقيح"), ("Incubation", "الحضن"), ("Identification", "التشخيص")), "a"),
 Q("Detecting virus-specific antibodies is done by:", "يتم كشف الأضداد الخاصّة بالفيروس بـ:", O(("Electron microscopy", "المجهر الإلكتروني"), ("Serological tests", "الفحوص المصلية"), ("NAATs", "NAATs"), ("Filtration", "الترشيح")), "b"),
 {"topic_en": "BIOS questions — isolation and cultivation", "topic_ar": "أسئلة BIOS — العزل والزرع"},
 Q("Growing viruses in a test tube or cell culture flask is:", "تنمية الفيروسات في أنبوب اختبار أو قنينة مزرعة خلوية هي:", O(("In vivo", "داخل الكائن الحي"), ("Animal inoculation", "حقن الحيوانات"), ("In vitro", "خارج الكائن الحي"), ("Egg culture", "زرع البيض")), "c"),
 Q("The agar concentration usually used in culturing bacteria is:", "تركيز الآكار المستعمل عادةً في زرع البكتيريا:", O(("0.7%", "0.7%"), ("0.2%", "0.2%"), ("5%", "5%"), ("1.5%", "1.5%")), "d"),
 Q("In this figure, the clear spots on the E. coli lawn are:", "في هذا الشكل، البقع الصافية على مرجة الإشريكية القولونية هي:", O(("Plaques where host bacteria were lysed", "لويحات حيث تحلّلت البكتيريا المضيفة"), ("Bacterial colonies", "مستعمرات بكتيرية"), ("Fungal spores", "أبواغ فطرية"), ("Air bubbles", "فقاعات هواء")), "a", img="assets/flask-plaques.png", img_h="34mm"),
 Q("Most of the annual influenza vaccine is cultured in:", "يُزرع معظم لقاح الإنفلونزا السنوي في:", O(("Tumour cell lines", "خطوط خلايا الأورام"), ("Hens’ eggs", "بيض الدجاج"), ("Bacterial lawns", "المرجات البكتيرية"), ("Soft agar", "الآكار الطري")), "b"),
 Q("This figure shows sites in the egg where viruses can replicate; they include:", "يوضّح الشكل مواقع في البيضة يمكن أن تتضاعف فيها الفيروسات؛ منها:", O(("The shell only", "القشرة فقط"), ("The albumin only", "الزلال فقط"), ("The chorioallantoic membrane, amniotic cavity and yolk sac", "الغشاء المشيمي السقائي والجوف الأمنيوسي وكيس المحّ"), ("The air cell only", "الحجيرة الهوائية فقط")), "c", img="assets/egg-cultivation.png", img_h="34mm"),
 Q("Cells are released from tissue enzymatically using:", "تُحرَّر الخلايا من النسيج إنزيميًا باستعمال:", O(("Lysozyme", "اللايسوزايم"), ("Amylase", "الأميليز"), ("Lipase", "اللايبيز"), ("Trypsin or collagenase", "التربسين أو الكولاجينيز")), "d"),
 Q("Continuous cell lines are usually derived from:", "تُشتقّ الخطوط الخلوية المستمرة عادةً من:", O(("Transformed cells or tumors", "خلايا متحوّلة أو أورام"), ("Red blood cells", "كريات الدم الحمر"), ("Bacteria", "البكتيريا"), ("Egg albumin", "زلال البيض")), "a"),
 Q("Growth of primary cultures slows when cells touch each other because of:", "يتباطأ نموّ المزارع الأولية عند تلامس الخلايا بسبب:", O(("Lysis", "التحلّل"), ("Contact inhibition", "تثبيط التماس"), ("Plaque formation", "تكوّن اللويحات"), ("Filtration", "الترشيح")), "b"),
 {"topic_en": "BIOS questions — detection", "topic_ar": "أسئلة BIOS — الكشف"},
 Q("Virus-infected samples can be examined under:", "يمكن فحص العيّنات المصابة تحت:", O(("Brightfield microscope only", "المجهر الضوئي الساطع فقط"), ("Hand lens", "العدسة اليدوية"), ("Brightfield, electron, or fluorescent microscope", "المجهر الضوئي الساطع أو الإلكتروني أو الفلوري"), ("No microscope", "دون مجهر")), "c"),
 Q("A change of cell shape in CPE is from:", "تغيّر شكل الخلية في CPE يكون من:", O(("Round to flat", "كروي إلى مسطّح"), ("Rod to coccus", "عصوي إلى كروي بكتيري"), ("Round to spiral", "كروي إلى حلزوني"), ("Flat to round", "مسطّح إلى كروي")), "d"),
 Q("Pink eosinophilic cytoplasmic inclusion bodies and cell swelling are the CPE of:", "الأجسام الاشتمالية السايتوبلازمية الوردية الحمضية وانتفاخ الخلية هي CPE لـ:", O(("Poxvirus", "الفيروس الجدري"), ("Adenovirus", "الفيروس الغدّي"), ("Paramyxovirus", "المخاطاني نظير"), ("Herpesvirus", "الهربس")), "a"),
 Q("Cytoplasmic stranding with nuclear inclusion bodies is the CPE of:", "التخيّط السايتوبلازمي مع أجسام اشتمالية نووية هو CPE لـ:", O(("Poxvirus", "الفيروس الجدري"), ("Herpesvirus", "الفيروس الحلئي"), ("Adenovirus", "الفيروس الغدّي"), ("Paramyxovirus", "المخاطاني نظير")), "b"),
 Q("Distinctive “grape-like” clusters are the CPE of:", "العناقيد المميّزة \"الشبيهة بالعنب\" هي CPE لـ:", O(("Herpesvirus", "الهربس"), ("Poxvirus", "الجدري"), ("Adenovirus", "الفيروس الغدّي"), ("Paramyxovirus", "المخاطاني نظير")), "c"),
 Q("Syncytium with faint basophilic cytoplasmic inclusions is the CPE of:", "المخلوّ مع أجسام اشتمالية سايتوبلازمية قاعدية باهتة هو CPE لـ:", O(("Adenovirus", "الفيروس الغدّي"), ("Poxvirus", "الجدري"), ("Herpesvirus", "الهربس"), ("Paramyxovirus", "المخاطاني نظير")), "d"),
]
mcq = lab + balance(mine, 41)

tf = [
 TF("Viruses are obligate intracellular parasites that require living host cells for replication.", "الفيروسات طفيليات إجبارية داخل الخلايا تحتاج خلايا مضيفة حية للتضاعف.", "T"),
 TF("Viruses can be grown on artificial nutrient media without host cells.", "يمكن تنمية الفيروسات على أوساط غذائية اصطناعية دون خلايا مضيفة.", "F"),
 TF("Continuous cell lines can be propagated indefinitely.", "يمكن إكثار الخطوط الخلوية المستمرة إلى ما لا نهاية.", "T"),
 TF("Embryonated eggs can be used to cultivate influenza viruses.", "يمكن استعمال البيض المخصّب لزرع فيروسات الإنفلونزا.", "T"),
 TF("Virions can be separated from host cells by centrifugation or filtration.", "يمكن فصل الفيريونات عن الخلايا المضيفة بالطرد المركزي أو الترشيح.", "T"),
 TF("During filtration, viruses are usually collected in the filtrate after larger cells are removed.", "أثناء الترشيح تُجمع الفيروسات عادةً في الراشح بعد إزالة الخلايا الأكبر.", "T"),
 TF("A clear zone produced by lytic bacteriophages in a bacterial lawn is called a plaque.", "تُسمّى المنطقة الصافية التي تنتجها العاثيات المحلِّلة في المرجة البكتيرية لويحة.", "T"),
 TF("Bacteriophages are grown in 1.5% hard agar to allow easy diffusion.", "تُنمّى العاثيات في آكار صلب 1.5% للسماح بالانتشار السهل.", "F"),
 TF("Electron microscopy can be used to visualize viral particles directly.", "يمكن استعمال المجهر الإلكتروني لرؤية الجسيمات الفيروسية مباشرةً.", "T"),
 TF("Formation of multinucleated syncytia is a cytopathic effect of viral infection.", "تكوين مخلوّات متعدّدة النوى تأثير مرضي خلوي للإصابة الفيروسية.", "T"),
 TF("Continuous cell cultures stop growing because of contact inhibition.", "تتوقّف المزارع الخلوية المستمرة عن النمو بسبب تثبيط التماس.", "F"),
 TF("Animal virus cultivation is important for vaccine production.", "زرع الفيروسات الحيوانية مهمّ لإنتاج اللقاحات.", "T"),
 TF("Viral titers in Figure 2b increase on the plates to the right.", "في الشكل 2 ب يزداد العيار الفيروسي في الأطباق باتجاه اليمين.", "F"),
]

traps = [
 TR("0.7% vs 1.5% agar", "آكار 0.7% مقابل 1.5%", "Phages use 0.7% SOFT agar so they diffuse easily; 1.5% is the usual concentration for culturing bacteria.", "العاثيات تستعمل آكارًا طريًا 0.7% لتنتشر بسهولة؛ و1.5% هو التركيز المعتاد لزرع البكتيريا."),
 TR("Filtrate or filter?", "الراشح أم المرشّح؟", "Cells and bacteria stay ON the filter; viruses pass THROUGH into the filtrate.", "الخلايا والبكتيريا تبقى على المرشّح؛ والفيروسات تمرّ خلاله إلى الراشح."),
 TR("Primary vs continuous", "الأولية مقابل المستمرة", "Primary: fresh from tissue, limited lifespan, contact inhibition. Continuous: from transformed cells/tumours, immortal, no contact inhibition.", "الأولية: حديثة من النسيج، عمر محدود، تثبيط التماس. المستمرة: من خلايا متحوّلة/أورام، خالدة، بلا تثبيط تماس."),
 TR("Eggs vs animals", "البيض مقابل الحيوانات", "Eggs: influenza, herpes simplex. Animal inoculation: viruses that cannot grow in cell culture or eggs — rabies, poliovirus.", "البيض: الإنفلونزا والهربس البسيط. حقن الحيوانات: الفيروسات التي لا تنمو في المزرعة أو البيض — داء الكلب وشلل الأطفال."),
 TR("In vivo vs in vitro", "داخل الكائن مقابل خارجه", "In vivo = whole organism or embryonated egg; in vitro = cells in a test tube, flask, or agar plate.", "داخل الكائن = كائن كامل أو بيضة مخصّبة؛ خارجه = خلايا في أنبوب أو قنينة أو طبق آكار."),
 TR("Which virus, which CPE?", "أي فيروس، أي CPE؟", "Paramyxo = syncytium; pox = pink cytoplasmic inclusions + swelling; herpes = stranding + NUCLEAR inclusions; adeno = grape-like clusters.", "المخاطاني نظير = مخلوّ؛ الجدري = أجسام سايتوبلازمية وردية + انتفاخ؛ الهربس = تخيّط + أجسام نووية؛ الغدّي = عناقيد عنبية."),
 TR("Identification methods", "طرق التشخيص", "EM sees particles; serology detects ANTIBODIES; NAATs amplify DNA/RNA.", "المجهر الإلكتروني يرى الجسيمات؛ والمصلية تكشف الأضداد؛ وNAATs تضخّم DNA/RNA."),
]

important = [
 IM("List the methods of viral cultivation.", "عدّد طرق زرع الفيروسات.", "1. Cell culture (most common): viruses grown in cultured animal cells — primary cell cultures (directly from tissues, limited lifespan) and continuous cell lines (immortalized, propagated indefinitely). 2. Embryonated eggs: e.g. influenza and herpes simplex viruses. 3. Animal inoculation: for viruses that cannot grow in cell culture or eggs, e.g. rabies and poliovirus.", "1. المزرعة الخلوية (الأكثر شيوعًا): تنمية الفيروسات في خلايا حيوانية مزروعة — المزارع الأولية (مباشرةً من الأنسجة، عمر محدود) والخطوط المستمرة (خالدة، تُكثَّر بلا نهاية). 2. البيض المخصّب: مثل الإنفلونزا والهربس البسيط. 3. حقن الحيوانات: للفيروسات التي لا تنمو في المزرعة أو البيض، مثل داء الكلب وشلل الأطفال."),
 IM("Describe the steps in viral isolation and cultivation.", "صف خطوات عزل الفيروسات وزرعها.", "1. Sample collection (blood, respiratory secretions, stool). 2. Sample preparation: remove or inactivate antibiotics or bacteria. 3. Inoculation into cell culture, eggs or animals. 4. Incubation (temperature, humidity). 5. Observation for CPE or disease symptoms. 6. Virus identification by electron microscopy, serological tests or NAATs.", "1. جمع العيّنة (دم، إفرازات تنفسية، براز). 2. تحضير العيّنة: إزالة المضادّات أو البكتيريا أو تثبيطها. 3. التلقيح في المزرعة أو البيض أو الحيوانات. 4. الحضن (حرارة، رطوبة). 5. مراقبة CPE أو أعراض المرض. 6. تشخيص الفيروس بالمجهر الإلكتروني أو الفحوص المصلية أو NAATs."),
 IM("How are viruses isolated from host cells?", "كيف تُعزل الفيروسات عن الخلايا المضيفة؟", "Viruses cannot grow on artificial media, so infected host cells are cultured and the growth medium is harvested. Virions are separated from cells by centrifugation or filtration; membrane filters retain cells and bacteria (larger than virions) while viruses pass into the filtrate.", "لا تنمو الفيروسات على أوساط اصطناعية، فتُزرع الخلايا المضيفة المصابة ويُحصد وسط النمو. وتُفصل الفيريونات عن الخلايا بالطرد المركزي أو الترشيح؛ إذ تحتجز المرشّحات الغشائية الخلايا والبكتيريا (الأكبر من الفيريونات) وتمرّ الفيروسات إلى الراشح."),
 IM("How are bacteriophages cultivated and detected?", "كيف تُزرع العاثيات البكتيرية وتُكشف؟", "They are grown on a dense bacterial lawn in 0.7% soft agar (lower than the usual 1.5%) in a Petri dish or flat flask, so phages diffuse easily. Lytic phages lyse the bacteria, producing clear zones called plaques among the cloudy lawn.", "تُنمّى على مرجة بكتيرية كثيفة في آكار طري 0.7% (أقل من 1.5% المعتاد) في طبق بتري أو قنينة مسطّحة لتنتشر العاثيات بسهولة. والعاثيات المحلِّلة تحلّل البكتيريا فتنتج مناطق صافية تُسمّى اللويحات وسط المرجة العكرة."),
 IM("Compare in vivo and in vitro cultivation of animal viruses.", "قارن بين زرع الفيروسات الحيوانية داخل الكائن الحي وخارجه.", "In vivo: a developing embryo in an embryonated bird's egg (chorioallantoic membrane, amniotic cavity, yolk sac) or a whole animal acts as an incubator; e.g. influenza vaccine in hens' eggs. In vitro: primary cell cultures freshly prepared from tissues (by scraping/mincing or trypsin/collagenase), limited by contact inhibition; continuous cell lines from transformed cells or tumours that grow indefinitely (immortal).", "داخل الكائن: جنين نامٍ في بيضة طائر مخصّبة (الغشاء المشيمي السقائي، الجوف الأمنيوسي، كيس المحّ) أو حيوان كامل يعمل حاضنة؛ مثل لقاح الإنفلونزا في بيض الدجاج. خارج الكائن: مزارع أولية تُحضّر حديثًا من الأنسجة (بالكشط/الفرم أو التربسين/الكولاجينيز) ويحدّها تثبيط التماس؛ وخطوط مستمرة من خلايا متحوّلة أو أورام تنمو بلا نهاية (خالدة)."),
 IM("What are cytopathic effects? Give examples.", "ما التأثيرات المرضية الخلوية؟ أعطِ أمثلة.", "Distinct observable cell abnormalities due to viral infection: loss of adherence, flat-to-round shape change, nuclear shrinkage, cytoplasmic vacuoles, membrane fusion with multinucleated syncytia, nuclear or cytoplasmic inclusion bodies, and complete lysis. Paramyxovirus: syncytium; poxvirus: pink cytoplasmic inclusions and swelling; herpesvirus: cytoplasmic stranding and nuclear inclusions; adenovirus: enlargement, rounding, grape-like clusters.", "شذوذات خلوية مميّزة تُلاحظ بسبب الإصابة الفيروسية: فقدان الالتصاق، تغيّر الشكل من مسطّح إلى كروي، انكماش النواة، فجوات سايتوبلازمية، اندماج الأغشية مع مخلوّات متعدّدة النوى، أجسام اشتمالية نووية أو سايتوبلازمية، والتحلّل الكامل. المخاطاني نظير: مخلوّ؛ الجدري: أجسام سايتوبلازمية وردية وانتفاخ؛ الهربس: تخيّط سايتوبلازمي وأجسام نووية؛ الغدّي: تضخّم وتكوّر وعناقيد عنبية."),
]

meta = {"subject_en": "Medical Virology", "subject_ar": "الفيروسات الطبية", "short_ar": "فايروسات", "instructor": "د. آية وسمي",
        "unit_en": "Lab 4", "unit_ar": "العملي 4", "unit_label": "LAB", "unit_no": "4",
        "title_en": "Isolation and Cultivation of Viruses", "title_ar": "عزل الفيروسات وزرعها",
        "kind": "Laboratories — عملي", "stage": "The third stage — الثالثة"}
save("virology-lab4-isolation-cultivation", meta, blocks, mcq, tf, traps, important)

```
