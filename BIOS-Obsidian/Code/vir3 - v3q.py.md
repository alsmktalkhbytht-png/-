---
source: BIOS-Obsidian/tools/scripts/vir3/v3q.py
handouts: [virology-lab3-direct-examination]
saved: 2026-11-11
tags: [bios, code]
---
# vir3/v3q.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#virology-lab3-direct-examination|virology-lab3-direct-examination]]

```python
lab = [
 {"topic_en": "MCQs Lab Three (from the lab sheet)", "topic_ar": "أسئلة العملي الثالث (من ورقة العملي)"},
 Q("What are viruses:", "ما الفيروسات:", O(("They are free-living cellular organisms", "كائنات خلوية حرّة المعيشة"), ("They are acellular, submicroscopic obligate intracellular parasites", "طفيليات لا خلوية دون مجهرية إجبارية داخل الخلايا"), ("They contain both DNA and RNA", "تحتوي DNA وRNA معًا"), ("They reproduce by binary fission", "تتكاثر بالانشطار الثنائي"), ("They synthesize their own proteins", "تصنّع بروتيناتها بنفسها")), "b"),
 Q("A viral particle genome contains:", "يحتوي جينوم الجسيم الفيروسي:", O(("Both DNA and RNA", "DNA وRNA معًا"), ("Only proteins", "بروتينات فقط"), ("Either DNA or RNA", "إمّا DNA أو RNA"), ("Lipids only", "دهونًا فقط"), ("Ribosomes and enzymes", "رايبوسومات وإنزيمات")), "c"),
 Q("The protein coat surrounding a viral genome is called the:", "يُسمّى الغطاء البروتيني المحيط بالجينوم الفيروسي:", O(("Capsid", "الكابسيد"), ("Envelope", "الغلاف"), ("Cell wall", "الجدار الخلوي"), ("Nucleolus", "النوية"), ("Matrix", "المطرس (الماتركس)")), "a"),
 Q("An envelope of an enveloped virus is mainly composed of:", "يتكوّن غلاف الفيروس المغلَّف أساسًا من:", O(("Peptidoglycan", "الببتيدوگلايكان"), ("Cellulose", "السليلوز"), ("Lipid from the infected cell and viral proteins", "دهون من الخلية المصابة وبروتينات فيروسية"), ("Ribosomes and DNA", "رايبوسومات وDNA"), ("Only viral nucleic acid", "حامض نووي فيروسي فقط")), "c"),
 Q("Viruses are considered parasites because they:", "تُعدّ الفيروسات طفيليات لأنها:", O(("Produce excessive ATP", "تنتج ATP بإفراط"), ("Use binary fission for replication", "تستعمل الانشطار الثنائي للتضاعف"), ("Contain mitochondria", "تحتوي مايتوكوندريا"), ("Carry out photosynthesis", "تقوم بالبناء الضوئي"), ("Depend on host cells for energy and metabolic processes", "تعتمد على الخلايا المضيفة في الطاقة والعمليات الأيضية")), "e"),
 Q("Which cellular change may be observed by light microscopy in viral infections:", "أي تغيّر خلوي قد يُلاحظ بالمجهر الضوئي في الإصابات الفيروسية:", O(("Formation of inclusion bodies", "تكوين الأجسام الاشتمالية"), ("Direct visualization of all virions", "رؤية جميع الفيريونات مباشرةً"), ("Bacterial endospore formation", "تكوين الأبواغ البكتيرية الداخلية"), ("Production of fungal hyphae", "إنتاج خيوط فطرية"), ("Formation of erythrocytes", "تكوين كريات الدم الحمر")), "a"),
 Q("Cytopathogenic effects may include:", "قد تشمل التأثيرات المرضية الخلوية:", O(("Production of antibodies", "إنتاج الأضداد"), ("Formation of bacterial capsules", "تكوين محافظ بكتيرية"), ("Cell rounding, swelling, and syncytium formation", "تكوّر الخلية وانتفاخها وتكوين المخلوّ"), ("Cell division into daughter cells", "انقسام الخلية إلى خلايا بنوية"), ("Destruction of viral nucleic acid by ribosomes", "تحطيم الحامض النووي الفيروسي بالرايبوسومات")), "c"),
 Q("Transmission electron microscopy is especially useful for examining:", "المجهر الإلكتروني النافذ مفيد خصوصًا لفحص:", O(("The external surface only", "السطح الخارجي فقط"), ("The internal structure of viruses and infected cells", "التركيب الداخلي للفيروسات والخلايا المصابة"), ("Antibody concentration in serum", "تركيز الأضداد في المصل"), ("Viral genome sequencing", "تسلسل الجينوم الفيروسي"), ("Cell culture nutrient composition", "تركيب مغذّيات المزرعة الخلوية")), "b"),
 Q("Scanning electron microscopy produces images that are useful for studying:", "ينتج المجهر الإلكتروني الماسح صورًا مفيدة لدراسة:", O(("Internal viral nucleic acid", "الحامض النووي الفيروسي الداخلي"), ("Viral external morphology and interactions with cells", "الشكل الخارجي للفيروس وتفاعلاته مع الخلايا"), ("Antiviral antibody production", "إنتاج الأضداد المضادّة للفيروس"), ("Viral protein synthesis in ribosomes", "تصنيع البروتين الفيروسي في الرايبوسومات"), ("Host-cell DNA replication", "تضاعف DNA الخلية المضيفة")), "b"),
 Q("One limitation of direct viral examination is that:", "من قيود الفحص المباشر للفيروسات أنه:", O(("It always identifies every virus species precisely", "يحدّد دائمًا كل نوع فيروسي بدقّة"), ("It does not require specialized equipment", "لا يحتاج أجهزة متخصّصة"), ("It may fail to detect the type of virus", "قد يفشل في كشف نوع الفيروس"), ("It cannot be used with clinical specimens", "لا يمكن استعماله مع العيّنات السريرية"), ("It eliminates the need for other diagnostic tests", "يلغي الحاجة إلى فحوص تشخيصية أخرى")), "c"),
]

mine = [
 {"topic_en": "BIOS questions — viruses and their structure", "topic_ar": "أسئلة BIOS — الفيروسات وتركيبها"},
 Q("Viruses can only be seen with:", "لا تُرى الفيروسات إلا بـ:", O(("A hand lens", "عدسة يدوية"), ("A standard light microscope", "مجهر ضوئي اعتيادي"), ("An electron microscope", "مجهر إلكتروني"), ("The naked eye", "العين المجرّدة")), "c"),
 Q("Viruses that infect bacteria are called:", "الفيروسات التي تصيب البكتيريا تُسمّى:", O(("Bacteriophages", "العاثيات (البكتريوفاج)"), ("Virions", "الفيريونات"), ("Capsomeres", "الكابسوميرات"), ("Syncytia", "المخلوّات")), "a"),
 Q("A complete virus particle is called a:", "يُسمّى الجسيم الفيروسي الكامل:", O(("Capsomere", "كابسومير"), ("Virion", "فيريون"), ("Syncytium", "مخلوّ"), ("Inclusion body", "جسم اشتمالي")), "b"),
 Q("Viruses are described as energy parasites because:", "توصف الفيروسات بأنها طفيليات طاقة لأنه:", O(("They store ATP", "تخزّن ATP"), ("They photosynthesize", "تقوم بالبناء الضوئي"), ("They have mitochondria", "لها مايتوكوندريا"), ("No known virus can generate the energy for all biological processes", "لا يستطيع أي فيروس معروف توليد الطاقة لكل العمليات الحيوية")), "d"),
 Q("A virus made of a genome and a capsid only is a:", "الفيروس المكوّن من جينوم وكابسيد فقط هو:", O(("Naked virus", "فيروس عاري"), ("Enveloped virus", "فيروس مغلَّف"), ("Bacterium", "بكتيريا"), ("Syncytium", "مخلوّ")), "a"),
 Q("The lipid of a viral envelope is taken from:", "تُؤخذ دهون الغلاف الفيروسي من:", O(("The capsid", "الكابسيد"), ("The infected cell", "الخلية المصابة"), ("The viral genome", "الجينوم الفيروسي"), ("Ribosomes", "الرايبوسومات")), "b"),
 Q("The bacteriophage (head and tail) is an example of:", "العاثي (رأس وذيل) مثال على:", O(("Icosahedral symmetry only", "تناظر عشريني فقط"), ("Helical symmetry", "تناظر حلزوني"), ("Complex symmetry", "تناظر معقّد"), ("No symmetry", "لا تناظر")), "c"),
 Q("Viruses lack the genetic information for:", "تفتقر الفيروسات إلى المعلومات الوراثية لـ:", O(("Their capsid proteins", "بروتينات الكابسيد"), ("Their genome", "جينومها"), ("Infecting cells", "إصابة الخلايا"), ("Metabolic energy generation and ribosomes", "توليد الطاقة الأيضية والرايبوسومات")), "d"),
 Q("This figure shows a virus with an outer envelope; it is:", "يُظهر هذا الشكل فيروسًا بغلاف خارجي؛ وهو:", O(("An enveloped virus (lentivirus)", "فيروس مغلَّف (فيروس بطيء)"), ("A naked adenovirus", "فيروس غدّي عاري"), ("A bacteriophage", "عاثي"), ("A helical plant virus", "فيروس نباتي حلزوني")), "a", img="assets/naked-enveloped.png", img_h="40mm"),
 {"topic_en": "BIOS questions — microscopy", "topic_ar": "أسئلة BIOS — الفحص المجهري"},
 Q("Inclusion bodies are aggregates of:", "الأجسام الاشتمالية تجمّعات من:", O(("Lipids and sugars", "دهون وسكريات"), ("Viral proteins or nucleic acids", "بروتينات أو أحماض نووية فيروسية"), ("Bacterial spores", "أبواغ بكتيرية"), ("Red blood cells", "كريات حمر")), "b"),
 Q("A syncytium is:", "المخلوّ هو:", O(("A single virion", "فيريون واحد"), ("A capsid unit", "وحدة كابسيد"), ("Fused cells", "خلايا مندمجة"), ("An antibody", "ضد")), "c"),
 Q("CPE can be observed in:", "يمكن ملاحظة CPE في:", O(("Serum", "المصل"), ("Purified DNA", "DNA منقّى"), ("Culture media without cells", "أوساط زرع بلا خلايا"), ("Cell cultures infected with certain viruses", "المزارع الخلوية المصابة ببعض الفيروسات")), "d"),
 Q("The main advantage of electron microscopy over light microscopy is:", "الميزة الرئيسية للمجهر الإلكتروني على الضوئي:", O(("Significantly higher resolution", "قدرة تمييز أعلى بكثير"), ("Lower cost", "كلفة أقل"), ("No need for trained staff", "لا يحتاج كوادر مدرّبة"), ("Colour images", "صور ملوّنة")), "a"),
 Q("In TEM the electron beam:", "في TEM حزمة الإلكترونات:", O(("Is scanned across the surface", "تمسح السطح"), ("Is transmitted through a thin section", "تنفذ خلال مقطع رقيق"), ("Is reflected by a mirror", "تنعكس بمرآة"), ("Is replaced by light", "تُستبدل بالضوء")), "b"),
 Q("A 3D image of the viral surface is produced by:", "تُنتَج صورة ثلاثية الأبعاد لسطح الفيروس بـ:", O(("TEM", "TEM"), ("Light microscopy", "المجهر الضوئي"), ("SEM", "SEM"), ("NAAT", "NAAT")), "c"),
 Q("This figure shows inclusion bodies seen by light microscopy in rabies-infected nerve cells; they are:", "يُظهر هذا الشكل أجسامًا اشتمالية بالمجهر الضوئي في خلايا عصبية مصابة بداء الكلب؛ وهي:", O(("Guarnieri bodies", "أجسام غوارنيري"), ("Syncytia", "مخلوّات"), ("Capsomeres", "كابسوميرات"), ("Negri bodies", "أجسام نيغري")), "d", img="assets/negri-bodies.png", img_h="36mm"),
 Q("This image of a bacteriophage was obtained by:", "صورة العاثي هذه أُخذت بـ:", O(("TEM", "المجهر الإلكتروني النافذ"), ("SEM", "المجهر الإلكتروني الماسح"), ("Light microscopy", "المجهر الضوئي"), ("Fluorescence", "التألّق")), "a", img="assets/phage-tem.png", img_h="34mm"),
 {"topic_en": "BIOS questions — applications and limitations", "topic_ar": "أسئلة BIOS — التطبيقات والقيود"},
 Q("Clinical specimens for direct viral examination include:", "تشمل العيّنات السريرية للفحص المباشر:", O(("Respiratory secretions, stool, or blood", "الإفرازات التنفسية أو البراز أو الدم"), ("Hair only", "الشعر فقط"), ("Teeth", "الأسنان"), ("Bone only", "العظم فقط")), "a"),
 Q("Similar morphology of related viruses is a problem of:", "تشابه شكل الفيروسات المتقاربة مشكلة في:", O(("Sensitivity", "الحساسية"), ("Specificity", "النوعية"), ("Cost", "الكلفة"), ("Speed", "السرعة")), "b"),
 Q("Failure to detect low levels of virus is a problem of:", "الفشل في كشف المستويات المنخفضة من الفيروس مشكلة في:", O(("Specificity", "النوعية"), ("Technical expertise", "الخبرة التقنية"), ("Sensitivity", "الحساسية"), ("Resolution", "قدرة التمييز")), "c"),
 Q("Direct examination is often combined with:", "كثيرًا ما يُدمج الفحص المباشر مع:", O(("Gram stain only", "صبغة گرام فقط"), ("Blood culture only", "زرع الدم فقط"), ("Urine dipstick", "شريط الإدرار"), ("NAATs and serological tests", "NAATs والفحوص المصلية")), "d"),
]
mcq = lab + balance(mine, 31)

tf = [
 TF("Viruses are submicroscopic obligate intracellular parasites.", "الفيروسات طفيليات دون مجهرية إجبارية داخل الخلايا.", "T"),
 TF("Viruses have a complete cellular structure with ribosomes.", "للفيروسات تركيب خلوي كامل مع رايبوسومات.", "F"),
 TF("A viral genome contains either DNA or RNA.", "يحتوي الجينوم الفيروسي إمّا DNA أو RNA.", "T"),
 TF("The protein coat surrounding the viral genome is called the capsid.", "يُسمّى الغطاء البروتيني المحيط بالجينوم الفيروسي الكابسيد.", "T"),
 TF("Enveloped viruses contain a lipid envelope derived from the infected host cell.", "تحتوي الفيروسات المغلَّفة غلافًا دهنيًا مشتقًّا من الخلية المضيفة المصابة.", "T"),
 TF("Virions grow and divide by binary fission.", "تنمو الفيريونات وتنقسم بالانشطار الثنائي.", "F"),
 TF("Inclusion bodies may be observed in the nucleus or cytoplasm of infected cells.", "قد تُلاحظ الأجسام الاشتمالية في نواة الخلايا المصابة أو سايتوبلازمها.", "T"),
 TF("Light microscopy can directly visualize all viruses clearly.", "يستطيع المجهر الضوئي رؤية جميع الفيروسات بوضوح مباشرةً.", "F"),
 TF("Transmission electron microscopy is useful for examining internal viral structures.", "المجهر الإلكتروني النافذ مفيد لفحص التراكيب الفيروسية الداخلية.", "T"),
 TF("Scanning electron microscopy can produce three-dimensional images of viral surfaces.", "يستطيع المجهر الإلكتروني الماسح إنتاج صور ثلاثية الأبعاد لأسطح الفيروسات.", "T"),
 TF("A virus is a form of life but not a living organism.", "الفيروس شكل من أشكال الحياة لكنه ليس كائنًا حيًا.", "T"),
 TF("Viruses infect only humans and animals.", "تصيب الفيروسات الإنسان والحيوان فقط.", "F"),
 TF("Direct examination can be used to evaluate antiviral drugs.", "يمكن استعمال الفحص المباشر لتقييم الأدوية المضادّة للفيروسات.", "T"),
]

traps = [
 TR("Living form vs living organism", "شكل حياة مقابل كائن حي", "The sheet says a virus is a form of life (living form) but NOT a living organism.", "تقول الورقة إن الفيروس شكل من أشكال الحياة لكنه ليس كائنًا حيًا."),
 TR("DNA and RNA?", "DNA وRNA؟", "A virus has either DNA OR RNA — never both (the option \"both DNA and RNA\" is wrong).", "للفيروس إمّا DNA أو RNA — وليس الاثنين (خيار \"DNA وRNA معًا\" خطأ)."),
 TR("Where does the envelope come from?", "من أين يأتي الغلاف؟", "Envelope = lipid from the infected (host) cell + some virus proteins; the capsid is protein made by the virus.", "الغلاف = دهون من الخلية المصابة (المضيفة) + بعض البروتينات الفيروسية؛ والكابسيد بروتين يصنعه الفيروس."),
 TR("Light microscope sees the virus?", "المجهر الضوئي يرى الفيروس؟", "No — it sees the virus's effects on cells: inclusion bodies and CPE. Only EM shows virions directly.", "لا — يرى تأثيرات الفيروس في الخلايا: الأجسام الاشتمالية وCPE. والمجهر الإلكتروني وحده يُظهر الفيريونات مباشرةً."),
 TR("TEM vs SEM", "النافذ مقابل الماسح", "TEM = Transmitted through a thin section → internal structure. SEM = Scanned across the Surface → 3D external morphology.", "TEM = تنفذ خلال مقطع رقيق ← التركيب الداخلي. SEM = تمسح السطح ← الشكل الخارجي ثلاثي الأبعاد."),
 TR("Sensitivity vs specificity limit", "قيد الحساسية مقابل النوعية", "Sensitivity = may miss low levels of virus; specificity = similar morphology makes related viruses hard to tell apart.", "الحساسية = قد يفوت المستويات المنخفضة من الفيروس؛ النوعية = الشكل المتشابه يصعّب تمييز الفيروسات المتقاربة."),
]

important = [
 IM("How do viruses differ from other microorganisms?", "كيف تختلف الفيروسات عن الأحياء المجهرية الأخرى؟", "1. No cellular structure: only proteins and nucleic acid (DNA or RNA). 2. No metabolic systems of their own; they use the host cell's synthetic mechanism. 3. They infect bacteria (bacteriophages), protozoa, algae, fungi, plants, animals and humans. 4. They are assembled from pre-formed components made by the infected cell. 5. Virions do not grow or divide and lack ribosomes and energy-generating apparatus. 6. They are energy parasites. 7. A form of life but not a living organism.", "1. لا تركيب خلوي: بروتينات وحامض نووي (DNA أو RNA) فقط. 2. لا أنظمة أيضية خاصّة؛ تستعمل آلية التصنيع في الخلية المضيفة. 3. تصيب البكتيريا (العاثيات) والأوالي والطحالب والفطريات والنباتات والحيوانات والإنسان. 4. تُجمَّع من مكوّنات مصنّعة مسبقًا في الخلية المصابة. 5. الفيريونات لا تنمو ولا تنقسم وتفتقر إلى الرايبوسومات وأجهزة توليد الطاقة. 6. طفيليات طاقة. 7. شكل من أشكال الحياة لا كائن حي."),
 IM("Describe the composition of a virus particle.", "صف تركيب الجسيم الفيروسي.", "A genome of DNA or RNA encased by a protein coat (capsid) = naked virus. Some viruses also have an envelope of lipid from the infected cell plus some viral proteins = enveloped virus. Capsid symmetry may be icosahedral, helical or complex.", "جينوم من DNA أو RNA مغلّف بغطاء بروتيني (الكابسيد) = فيروس عاري. ولبعض الفيروسات أيضًا غلاف من دهون الخلية المصابة مع بعض البروتينات الفيروسية = فيروس مغلَّف. وقد يكون تناظر الكابسيد عشريني الأوجه أو حلزونيًا أو معقّدًا."),
 IM("What can light microscopy show in viral infections?", "ماذا يُظهر المجهر الضوئي في الإصابات الفيروسية؟", "Viruses are too small for the light microscope, but it shows characteristic changes in infected cells: 1. inclusion bodies — aggregates of viral proteins or nucleic acids in the nucleus or cytoplasm, indicating specific infections; 2. cytopathogenic effects — rounding, swelling or syncytia (fused cells), seen in infected cell cultures.", "الفيروسات أصغر من المجهر الضوئي، لكنه يُظهر تغيّرات مميّزة في الخلايا المصابة: 1. الأجسام الاشتمالية — تجمّعات بروتينات أو أحماض نووية فيروسية في النواة أو السايتوبلازم تدلّ على إصابات معيّنة؛ 2. التأثيرات المرضية الخلوية — التكوّر أو الانتفاخ أو المخلوّات (خلايا مندمجة)، وتُرى في المزارع الخلوية المصابة."),
 IM("Compare TEM and SEM.", "قارن بين TEM وSEM.", "TEM: electrons are transmitted through a thin section of the sample; useful for the internal structure of viruses and infected cells (e.g. influenza, HIV, bacteriophage). SEM: electrons are scanned across the surface, producing a 3D image; useful for external morphology and virus–cell interactions (e.g. coronavirus, Ebola, adenovirus).", "TEM: تنفذ الإلكترونات خلال مقطع رقيق من العيّنة؛ مفيد للتركيب الداخلي للفيروسات والخلايا المصابة (مثل الإنفلونزا وHIV والعاثي). SEM: تمسح الإلكترونات السطح فتنتج صورة ثلاثية الأبعاد؛ مفيد للشكل الخارجي وتفاعل الفيروس مع الخلية (مثل كورونا وإيبولا والفيروس الغدّي)."),
 IM("List the applications of direct viral examination.", "عدّد تطبيقات الفحص المباشر للفيروسات.", "1. Diagnosis of viral infections in clinical specimens (respiratory secretions, stool, blood). 2. Characterization of new viruses by EM morphology. 3. Monitoring viral replication in infected cells. 4. Evaluation of antiviral therapies.", "1. تشخيص الإصابات الفيروسية في العيّنات السريرية (الإفرازات التنفسية، البراز، الدم). 2. توصيف الفيروسات الجديدة بشكلها في المجهر الإلكتروني. 3. متابعة تضاعف الفيروس في الخلايا المصابة. 4. تقييم العلاجات المضادّة للفيروسات."),
 IM("What are the limitations of direct viral examination?", "ما قيود الفحص المباشر للفيروسات؟", "1. Sensitivity: may not detect low levels of virus. 2. Specificity: similar morphology of related viruses. 3. Technical expertise: specialized equipment and trained personnel. It is therefore often combined with NAATs and serological tests.", "1. الحساسية: قد لا يكشف المستويات المنخفضة. 2. النوعية: تشابه شكل الفيروسات المتقاربة. 3. الخبرة التقنية: أجهزة متخصّصة وكوادر مدرّبة. ولذلك كثيرًا ما يُدمج مع NAATs والفحوص المصلية."),
]

meta = {"subject_en": "Medical Virology", "subject_ar": "الفيروسات الطبية", "short_ar": "فايروسات", "instructor": "د. آية وسمي",
        "unit_en": "Lab 3", "unit_ar": "العملي 3", "unit_label": "LAB", "unit_no": "3",
        "title_en": "Direct viral examination (Light Microscopy, Electron Microscopy Examination)", "title_ar": "الفحص المباشر للفيروسات (المجهر الضوئي والمجهر الإلكتروني)",
        "kind": "Laboratories — عملي", "stage": "The third stage — الثالثة"}
save("virology-lab3-direct-examination", meta, blocks, mcq, tf, traps, important)

```
