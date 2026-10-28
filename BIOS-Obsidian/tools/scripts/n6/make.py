import json
from collections import Counter
def C(en, ar, **k): return dict(t="card", en=en, ar=ar, **k)
def R(en, ar): return dict(t="rule", en=en, ar=ar)
def SEC(en, ar): return dict(t="section", en=en, ar=ar)
def H2(en, ar): return dict(t="h2", en=en, ar=ar)
def L(en_items, ar_items, en="", ar="", **k): return dict(t="card", en=en, ar=ar, list_en=en_items, list_ar=ar_items, **k)
def F(src, en, ar, **k): return dict(t="figure", src="assets/" + src, en=en, ar=ar, **k)
def N(en, ar, label=None):
    b = dict(t="note", en=en, ar=ar)
    if label: b["label"] = label
    return b

blocks = [
 SEC("Introduction", "المقدمة"),
 C(["Eukaryotic cells reproduce in two different ways: **mitosis** and **meiosis**.",
    "It is absolutely essential that you understand and can clearly distinguish between the two.",
    "Without comprehension of these two methods of cell division an understanding of genetics and life cycles is impossible.",
    "Today we will be focusing on regular cell division (**mitosis**) as found in most eukaryotic cells.",
    "We will be examining **meiosis**, a type of cell division involved in **sexual reproduction**, [[cut]]"],
   ["تتكاثر الخلايا حقيقية النواة بطريقتين مختلفتين: **الانقسام الخيطي (المتساوي)** (`mitosis`) و**الانقسام الاختزالي** (`meiosis`).",
    "ومن الضروري جدًا أن تفهمهما وتميّز بينهما بوضوح.",
    "فمن دون فهم هاتين الطريقتين في انقسام الخلية يستحيل فهم علم الوراثة ودورات الحياة.",
    "سنركّز اليوم على الانقسام الخلوي الاعتيادي (**الانقسام الخيطي**) كما يحدث في معظم الخلايا حقيقية النواة.",
    "وسندرس **الانقسام الاختزالي**، وهو نوع من انقسام الخلية يشارك في **التكاثر الجنسي**، [[قطع]]"]),

 SEC("Cell cycle", "دورة الخلية"),
 C(["**Cell cycle** or cell division is a very important process in all living organisms.",
    "Its sequence of event by which, **DNA replication** and **cell growth** also take place and eventually cell divides into **two daughter cells**, all these events are under **genetic control**.",
    "Cell cycle is divided into two periods, **interphase**, **mitotic (M) phase** and followed by cytokines.",
    "For example, through cell cycle, the single-celled fertilized egg develops into a mature organism, as well as by this process,  hair, skin, blood cells, and some internal organs are renewed."],
   ["**دورة الخلية** أو انقسام الخلية عملية مهمة جدًا في جميع الكائنات الحية.",
    "وهي سلسلة أحداث يحدث خلالها **تضاعف الـ`DNA`** و**نمو الخلية**، ثم تنقسم الخلية في النهاية إلى **خليتين بنويتين**، وكل هذه الأحداث تحت **سيطرة وراثية**.",
    "تُقسَّم دورة الخلية إلى فترتين: **الطور البيني** و**طور الانقسام (`M`)**، ويليهما انقسام السايتوبلازم (`cytokinesis`).",
    "فمثلًا، من خلال دورة الخلية تتطوّر البيضة المخصّبة وحيدة الخلية إلى كائن ناضج، وبهذه العملية أيضًا يتجدّد الشعر والجلد وخلايا الدم وبعض الأعضاء الداخلية."]),
 F("cell-cycle.png", "The cell cycle: interphase (G1, S, G2), mitosis, cytokinesis, and G0 (cell cycle arrest)", "دورة الخلية: الطور البيني (`G1`، `S`، `G2`)، والانقسام، وانقسام السايتوبلازم، و`G0` (توقّف دورة الخلية)", h="70mm"),

 SEC("Interphase", "الطور البيني"),
 C(["**Inter phase**: It is note that in the **24 hour** average duration of cell cycle of a human cell, cell division proper lasts for only **about an hour**.",
    "The interphase lasts **more than 95%** of the duration of cell cycle.", "Interphase is divided to:"],
   ["**الطور البيني**: يُلاحَظ أنه في دورة الخلية البشرية التي يبلغ متوسط مدّتها **24 ساعة**، يستغرق الانقسام الفعلي **نحو ساعة واحدة** فقط.",
    "ويستغرق الطور البيني **أكثر من 95%** من مدة دورة الخلية.", "ويُقسَّم الطور البيني إلى:"]),
 R(["**Gap1 (G1)**: in this phase, Cells **increase in size and growth**, but **does not replicate its DNA**,",
    "the **G1 checkpoint** control mechanism ensures that everything is ready for DNA synthesis."],
   ["**الفجوة الأولى (`G1`)**: في هذا الطور **يزداد حجم الخلايا وتنمو**، لكنها **لا تضاعف الـ`DNA`**،",
    "وتضمن آلية السيطرة في **نقطة تفتيش `G1`** أن كل شيء جاهز لتخليق الـ`DNA`."]),
 R(["**Synthesis phase (S phase)**: in this phase, **DNA replication** begins in the nucleus, the **amount of DNA per cell doubles**. and the **centriole duplicates** in the cytoplasm.",
    "Each chromosome now consists of **two sister chromatids**."],
   ["**طور التخليق (`S`)**: في هذا الطور يبدأ **تضاعف الـ`DNA`** في النواة، **فتتضاعف كمية الـ`DNA` في الخلية**، و**يتضاعف الجسيم المركزي** في السايتوبلازم.",
    "ويتكوّن كل كروموسوم الآن من **كروماتيدين شقيقين**."]),
 R("**Gap 2(G2)**:  During this phase, **proteins are synthesized** in preparation for mitosis while cell growth continues.",
   "**الفجوة الثانية (`G2`)**: خلال هذا الطور **تُخلَّق البروتينات** استعدادًا للانقسام الخيطي مع استمرار نمو الخلية."),
 C(["In actively dividing cells, the actual division process may take **1 or 2 hours**, the **G1** phase approximately **8 hours**, the **S** phase about **6 hours** and the **G2** phase about **4 to 5 hours**.",
    "Thus, the total cell cycle (period from one division to the next) in actively dividing cells is quite short, lasting perhaps **20 hours**."],
   ["في الخلايا النشطة الانقسام، قد تستغرق عملية الانقسام الفعلية **ساعة أو ساعتين**، وطور `G1` نحو **8 ساعات**، وطور `S` نحو **6 ساعات**، وطور `G2` نحو **4 إلى 5 ساعات**.",
    "وهكذا تكون دورة الخلية الكاملة (المدة من انقسام إلى الذي يليه) في الخلايا النشطة الانقسام قصيرة نسبيًا، وربما تستمر نحو **20 ساعة**."]),
 dict(t="table", style="summary", label_en="Durations in actively dividing cells", label_ar="المدد في الخلايا النشطة الانقسام",
      head=["Phase", "Duration", "الطور — المدة"], ar_cols=[2], key_cols=[0],
      rows=[["G1", "≈ 8 hours", "`G1` — نحو 8 ساعات"], ["S", "≈ 6 hours", "`S` — نحو 6 ساعات"], ["G2", "4 – 5 hours", "`G2` — 4 إلى 5 ساعات"],
            ["Division (M)", "1 – 2 hours", "الانقسام (`M`) — ساعة إلى ساعتين"], ["Total cycle", "≈ 20 hours", "الدورة الكاملة — نحو 20 ساعة"]]),

 SEC("Mitosis phase (M phase)", "طور الانقسام الخيطي (`M`)"),
 C(["**Mitosis** is **nuclear division plus cytokinesis**, and produces **two identical daughter cells** during prophase, metaphase, anaphase, and telophase.",
    "Mitosis is divided into the following four stages:"],
   ["**الانقسام الخيطي** هو **انقسام النواة مع انقسام السايتوبلازم**، وينتج **خليتين بنويتين متطابقتين** خلال الطور التمهيدي والاستوائي والانفصالي والنهائي.",
    "ويُقسَّم الانقسام الخيطي إلى المراحل الأربع الآتية:"]),
 dict(t="flow", steps=[{"en": "Prophase", "ar": "التمهيدي"}, {"en": "Metaphase", "ar": "الاستوائي"}, {"en": "Anaphase", "ar": "الانفصالي"}, {"en": "Telophase", "ar": "النهائي"}]),
 F("mitosis-stages.jpg", "Stages of mitosis: G2 of interphase, prophase, prometaphase, metaphase, anaphase, telophase and cytokinesis",
   "مراحل الانقسام الخيطي: `G2` من الطور البيني، والتمهيدي، وما قبل الاستوائي، والاستوائي، والانفصالي، والنهائي وانقسام السايتوبلازم", h="110mm"),

 H2("1- Prophase", "1- الطور التمهيدي"),
 C(["Prophase which is the **first stage of mitosis** follows the S and G2 phases of interphase.",
    "Prophase is marked by the **initiation of condensation of chromosomal material**.",
    "The chromosomal material becomes untangled during the process of chromatin condensation"],
   ["الطور التمهيدي هو **المرحلة الأولى من الانقسام الخيطي**، ويأتي بعد طوري `S` و`G2` من الطور البيني.",
    "ويتميّز الطور التمهيدي **ببدء تكثّف المادة الكروموسومية**.",
    "وتنفكّ تشابكات المادة الكروموسومية أثناء عملية تكثّف الكروماتين"]),
 L(["The **centriole**, now begins to move towards **opposite poles** of the cell.",
    "Chromosomes are seen to be composed of **two chromatids** attached together at the **centromere**.",
    "Initiation of the assembly of **mitotic spindle**, the microtubules, the proteinaceous components of the cell cytoplasm help in the process."],
   ["يبدأ **الجسيم المركزي** الآن بالتحرّك نحو **قطبين متقابلين** في الخلية.",
    "تظهر الكروموسومات مكوّنة من **كروماتيدين** متّصلين معًا عند **القطعة المركزية** (`centromere`).",
    "يبدأ تجميع **مغزل الانقسام**، وتساعد في ذلك الأنيبيبات الدقيقة، وهي المكوّنات البروتينية لسايتوبلازم الخلية."]),
 N("Cells at the end of prophase, when viewed under the microscope, **do not show golgi complexes, endoplasmic reticulum, nucleolus and the nuclear envelope**.",
   "الخلايا في نهاية الطور التمهيدي، عند فحصها بالمجهر، **لا تُظهر أجسام كولجي، ولا الشبكة الإندوبلازمية، ولا النوية، ولا الغلاف النووي**.", label=["Important", "مهم"]),

 H2("2- Metaphase", "2- الطور الاستوائي"),
 C(["By this stage, **condensation of chromosomes is completed** and they can be observed clearly under the microscope.",
    "At this stage, metaphase chromosome is made up of **two sister chromatids**, which are held together by the **centromere**.",
    "Small disc-shaped structures at the surface of the centromeres are called **kinetochores**.",
    "These structures serve as the **sites of attachment of spindle fibers** (formed by the spindle fibers) to the chromosomes that are moved into position at the center of the cell.",
    "Hence With the arrival of all the centromeres at the **equatorial plane** (middle) of the cell metaphase begins.",
    "The key features of metaphase are:"],
   ["في هذه المرحلة **يكتمل تكثّف الكروموسومات** ويمكن رؤيتها بوضوح بالمجهر.",
    "ويتكوّن الكروموسوم الاستوائي في هذه المرحلة من **كروماتيدين شقيقين** تربطهما **القطعة المركزية**.",
    "وتُسمّى التراكيب الصغيرة القرصية الشكل على سطح القطع المركزية **الحُبيبات الحركية** (`kinetochores`).",
    "وتعمل هذه التراكيب **مواقع لارتباط خيوط المغزل** بالكروموسومات التي تُحرَّك إلى موضعها في وسط الخلية.",
    "ولذلك يبدأ الطور الاستوائي بوصول جميع القطع المركزية إلى **المستوى الاستوائي** (وسط) الخلية.",
    "والسمات الرئيسة للطور الاستوائي هي:"],
   list_en=["Spindle fibers attach to **kinetochores** of chromosomes.",
            "Chromosomes are moved to spindle equator and get aligned along **metaphase plate** through spindle fibers to both poles."],
   list_ar=["ترتبط خيوط المغزل **بالحُبيبات الحركية** للكروموسومات.",
            "تتحرّك الكروموسومات إلى خط استواء المغزل وتصطف على طول **الصفيحة الاستوائية** بواسطة خيوط المغزل المتّجهة إلى القطبين."]),

 H2("3- Anaphase", "3- الطور الانفصالي"),
 C(["As soon as the **centromeres divide**, the cell is said to be in anaphase.",
    "During anaphase one single-stranded chromosome of each previously double-stranded chromosome moves toward one pole of the cell, and the other single-stranded \"partner\" moves towards the opposite pole.",
    "Therefore, anaphase is the stage of **chromosome migration to the poles**.",
    "This stage ends when the chromosomes reach the poles of the cell.",
    "The separated sister chromatids are now referred to as **daughter chromosomes**."],
   ["حالما **تنقسم القطع المركزية** يُقال إن الخلية في الطور الانفصالي.",
    "وخلال هذا الطور يتحرّك كروموسوم مفرد الشريط من كل كروموسوم كان مزدوج الشريط نحو أحد قطبي الخلية، ويتحرّك «شريكه» المفرد الآخر نحو القطب المقابل.",
    "لذلك فالطور الانفصالي هو مرحلة **هجرة الكروموسومات إلى القطبين**.",
    "وتنتهي هذه المرحلة عندما تصل الكروموسومات إلى قطبي الخلية.",
    "وتُسمّى الكروماتيدات الشقيقة المنفصلة الآن **الكروموسومات البنوية**."]),

 H2("4- Telophase", "4- الطور النهائي"),
 C(["Its **final stage of mitosis** and a **reversal** of many of the processes observed during prophase.",
    "The **nuclear membrane reforms** around the chromosomes grouped at either pole of the cell, the chromosomes **uncoil** and become diffuse, and the **spindle fibres disappear**, nucleolus, Golgi complex and ER reform."],
   ["هو **المرحلة الأخيرة من الانقسام الخيطي**، و**عكس** لكثير من العمليات التي تحدث في الطور التمهيدي.",
    "إذ **يُعاد تكوين الغشاء النووي** حول الكروموسومات المتجمّعة عند كل قطب، و**تنفكّ** الكروموسومات وتصبح منتشرة، و**تختفي خيوط المغزل**، ويُعاد تكوين النوية وجهاز كولجي والشبكة الإندوبلازمية."]),

 SEC("Cytokines", "انقسام السايتوبلازم (`Cytokinesis`)"),
 C(["In this stage the nuclei, cytoplasm, organelles and cell membrane are divided into **two cells** containing **roughly equal shares** of these cellular components.",
    "**Cytokinesis is not a phase of mitosis**; it is a separate process necessary for completing cell division."],
   ["في هذه المرحلة تُقسَّم الأنوية والسايتوبلازم والعضيّات وغشاء الخلية إلى **خليتين** تحتوي كلٌّ منهما على **حصص متساوية تقريبًا** من هذه المكوّنات الخلوية.",
    "**انقسام السايتوبلازم ليس طورًا من أطوار الانقسام الخيطي**؛ بل عملية منفصلة ضرورية لإكمال انقسام الخلية."]),
 dict(t="table", style="summary", label_en="Mitosis at a glance", label_ar="الانقسام الخيطي باختصار",
      head=["Stage", "Key event", "الحدث الرئيس"], ar_cols=[2], key_cols=[0],
      rows=[["Prophase", "Chromosome condensation begins; centrioles move to poles; spindle assembly starts", "**التمهيدي**: يبدأ تكثّف الكروموسومات؛ تتحرّك الجسيمات المركزية إلى القطبين؛ يبدأ تجميع المغزل"],
            ["Metaphase", "Spindle fibers attach to kinetochores; chromosomes align on the metaphase plate", "**الاستوائي**: ترتبط خيوط المغزل بالحُبيبات الحركية؛ تصطف الكروموسومات على الصفيحة الاستوائية"],
            ["Anaphase", "Centromeres divide; daughter chromosomes migrate to the poles", "**الانفصالي**: تنقسم القطع المركزية؛ تهاجر الكروموسومات البنوية إلى القطبين"],
            ["Telophase", "Nuclear membrane reforms; chromosomes uncoil; spindle disappears", "**النهائي**: يُعاد تكوين الغشاء النووي؛ تنفكّ الكروموسومات؛ يختفي المغزل"],
            ["Cytokinesis", "Cytoplasm divides into two cells (not a phase of mitosis)", "**انقسام السايتوبلازم**: ينقسم السايتوبلازم إلى خليتين (ليس طورًا من الانقسام)"]]),
]

def Q(en, ar, opts, ans, **k):
    return dict(en=en, ar=ar, options=[list(o) for o in opts], answer=ans, **k)

mcq = [
 {"topic_en": "Cell cycle and interphase", "topic_ar": "دورة الخلية والطور البيني"},
 Q("Eukaryotic cells reproduce by:", "تتكاثر الخلايا حقيقية النواة بـ:", [("Binary fission only", "الانشطار الثنائي فقط"), ("Mitosis and meiosis", "الانقسام الخيطي والاختزالي"), ("Budding only", "التبرعم فقط"), ("Meiosis only", "الانقسام الاختزالي فقط")], "b"),
 Q("The type of cell division involved in sexual reproduction is:", "نوع انقسام الخلية المشارك في التكاثر الجنسي هو:", [("Mitosis", "الخيطي"), ("Cytokinesis", "انقسام السايتوبلازم"), ("Meiosis", "الاختزالي"), ("Interphase", "الطور البيني")], "c"),
 Q("The average duration of the cell cycle of a human cell is:", "متوسط مدة دورة الخلية البشرية:", [("1 hour", "ساعة واحدة"), ("6 hours", "6 ساعات"), ("12 hours", "12 ساعة"), ("24 hours", "24 ساعة")], "d"),
 Q("Interphase lasts:", "يستغرق الطور البيني:", [("More than 95% of the cell cycle", "أكثر من 95% من دورة الخلية"), ("About 50%", "نحو 50%"), ("Less than 5%", "أقل من 5%"), ("Exactly one hour", "ساعة واحدة بالضبط")], "a"),
 Q("In which phase does the cell grow but NOT replicate its DNA?", "في أي طور تنمو الخلية لكنها لا تضاعف الـ DNA؟", [("S", "S"), ("G1", "G1"), ("M", "M"), ("Anaphase", "الانفصالي")], "b"),
 Q("The checkpoint that ensures everything is ready for DNA synthesis is the:", "نقطة التفتيش التي تضمن الجاهزية لتخليق الـ DNA هي:", [("G2 checkpoint", "نقطة G2"), ("M checkpoint", "نقطة M"), ("G1 checkpoint", "نقطة G1"), ("S checkpoint", "نقطة S")], "c"),
 Q("DNA replication and centriole duplication occur in the:", "يحدث تضاعف الـ DNA والجسيم المركزي في طور:", [("G1 phase", "G1"), ("G2 phase", "G2"), ("Telophase", "النهائي"), ("S phase", "S")], "d"),
 Q("At the end of the S phase, each chromosome consists of:", "في نهاية طور S يتكوّن كل كروموسوم من:", [("Two sister chromatids", "كروماتيدين شقيقين"), ("One chromatid", "كروماتيد واحد"), ("Four chromatids", "أربعة كروماتيدات"), ("No centromere", "بلا قطعة مركزية")], "a"),
 Q("In G2, the cell mainly:", "في طور G2 تقوم الخلية أساسًا بـ:", [("Replicates DNA", "مضاعفة الـ DNA"), ("Synthesizes proteins in preparation for mitosis", "تخليق البروتينات استعدادًا للانقسام"), ("Divides its cytoplasm", "تقسيم السايتوبلازم"), ("Aligns chromosomes", "رصف الكروموسومات")], "b"),
 Q("In actively dividing cells, the S phase lasts about:", "في الخلايا النشطة الانقسام يستغرق طور S نحو:", [("1 hour", "ساعة"), ("4 hours", "4 ساعات"), ("6 hours", "6 ساعات"), ("8 hours", "8 ساعات")], "c"),
 Q("In actively dividing cells, the total cell cycle lasts perhaps:", "في الخلايا النشطة الانقسام تستمر الدورة الكاملة ربما:", [("5 hours", "5 ساعات"), ("10 hours", "10 ساعات"), ("48 hours", "48 ساعة"), ("20 hours", "20 ساعة")], "d"),
 {"topic_en": "Stages of mitosis", "topic_ar": "مراحل الانقسام الخيطي"},
 Q("Mitosis produces:", "ينتج الانقسام الخيطي:", [("Two identical daughter cells", "خليتين بنويتين متطابقتين"), ("Four different cells", "أربع خلايا مختلفة"), ("Gametes", "أمشاجًا"), ("One cell", "خلية واحدة")], "a"),
 Q("The first stage of mitosis is:", "المرحلة الأولى من الانقسام الخيطي:", [("Metaphase", "الاستوائي"), ("Prophase", "التمهيدي"), ("Anaphase", "الانفصالي"), ("Telophase", "النهائي")], "b"),
 Q("Prophase is marked by:", "يتميّز الطور التمهيدي بـ:", [("Division of centromeres", "انقسام القطع المركزية"), ("Reformation of the nuclear membrane", "إعادة تكوين الغشاء النووي"), ("Initiation of chromosome condensation", "بدء تكثّف الكروموسومات"), ("Alignment on the metaphase plate", "الاصطفاف على الصفيحة الاستوائية")], "c"),
 Q("At the end of prophase, the cell does NOT show:", "في نهاية الطور التمهيدي لا تُظهر الخلية:", [("Chromosomes", "الكروموسومات"), ("Centrioles", "الجسيمات المركزية"), ("Microtubules", "الأنيبيبات الدقيقة"), ("Golgi, ER, nucleolus and nuclear envelope", "كولجي والشبكة والنوية والغلاف النووي")], "d"),
 Q("The sister chromatids are held together by the:", "يربط الكروماتيدين الشقيقين:", [("Centromere", "القطعة المركزية"), ("Centriole", "الجسيم المركزي"), ("Nucleolus", "النوية"), ("Golgi", "كولجي")], "a"),
 Q("Kinetochores are:", "الحُبيبات الحركية (kinetochores) هي:", [("Pole bodies", "أجسام قطبية"), ("Small disc-shaped structures on the centromeres where spindle fibers attach", "تراكيب قرصية صغيرة على القطع المركزية ترتبط بها خيوط المغزل"), ("Parts of the nucleolus", "أجزاء من النوية"), ("Cytoplasmic granules", "حبيبات سايتوبلازمية")], "b"),
 Q("Chromosomes align on the metaphase plate during:", "تصطف الكروموسومات على الصفيحة الاستوائية خلال:", [("Prophase", "التمهيدي"), ("Anaphase", "الانفصالي"), ("Metaphase", "الاستوائي"), ("Telophase", "النهائي")], "c"),
 Q("Condensation of chromosomes is completed in:", "يكتمل تكثّف الكروموسومات في:", [("Metaphase", "الاستوائي"), ("G1", "G1"), ("Telophase", "النهائي"), ("S phase", "S")], "a"),
 Q("Anaphase begins as soon as:", "يبدأ الطور الانفصالي حالما:", [("The nuclear membrane reforms", "يُعاد تكوين الغشاء النووي"), ("The centromeres divide", "تنقسم القطع المركزية"), ("DNA replicates", "يتضاعف الـ DNA"), ("The cytoplasm divides", "ينقسم السايتوبلازم")], "b"),
 Q("The separated sister chromatids are called:", "تُسمّى الكروماتيدات الشقيقة المنفصلة:", [("Homologous chromosomes", "الكروموسومات المتماثلة"), ("Kinetochores", "الحُبيبات الحركية"), ("Centrosomes", "الأجسام المركزية"), ("Daughter chromosomes", "الكروموسومات البنوية")], "d"),
 Q("The stage of chromosome migration to the poles is:", "مرحلة هجرة الكروموسومات إلى القطبين هي:", [("Prophase", "التمهيدي"), ("Metaphase", "الاستوائي"), ("Anaphase", "الانفصالي"), ("Interphase", "البيني")], "c"),
 Q("Telophase is a reversal of the processes of:", "الطور النهائي عكس لعمليات:", [("Prophase", "الطور التمهيدي"), ("Anaphase", "الطور الانفصالي"), ("S phase", "طور S"), ("Metaphase", "الطور الاستوائي")], "a"),
 Q("In telophase:", "في الطور النهائي:", [("The spindle forms", "يتكوّن المغزل"), ("Centromeres divide", "تنقسم القطع المركزية"), ("Chromosomes condense", "تتكثّف الكروموسومات"), ("The nuclear membrane reforms and the chromosomes uncoil", "يُعاد تكوين الغشاء النووي وتنفكّ الكروموسومات")], "d"),
 Q("Cytokinesis is:", "انقسام السايتوبلازم هو:", [("The first phase of mitosis", "الطور الأول من الانقسام"), ("A separate process, not a phase of mitosis", "عملية منفصلة وليس طورًا من الانقسام"), ("Part of G1", "جزء من G1"), ("DNA replication", "تضاعف الـ DNA")], "b"),
 {"topic_en": "Picture questions", "topic_ar": "أسئلة الصور"},
 Q("In this cell-cycle figure, the phase in which “each of the 46 chromosomes is duplicated” is:", "في شكل دورة الخلية هذا، الطور الذي «يتضاعف فيه كل كروموسوم من الـ 46» هو:", [("G1", "G1"), ("G2", "G2"), ("S", "S"), ("G0", "G0")], "c", img="assets/cell-cycle.png", img_h="48mm"),
 Q("Which stage of mitosis is shown (chromosomes lined up on a plate in the middle of the spindle)?", "أي مرحلة من الانقسام في الشكل (كروموسومات مصطفّة على صفيحة في وسط المغزل)؟", [("Prophase", "التمهيدي"), ("Metaphase", "الاستوائي"), ("Anaphase", "الانفصالي"), ("Telophase", "النهائي")], "b", img="assets/stage-metaphase.jpg", img_h="44mm"),
 Q("Which stage of mitosis is shown (daughter chromosomes moving to opposite poles)?", "أي مرحلة من الانقسام في الشكل (كروموسومات بنوية تتحرّك إلى قطبين متقابلين)؟", [("Metaphase", "الاستوائي"), ("Prophase", "التمهيدي"), ("Telophase", "النهائي"), ("Anaphase", "الانفصالي")], "d", img="assets/stage-anaphase.jpg", img_h="44mm"),
 Q("Which stage is shown (cleavage furrow, nuclear envelope and nucleolus forming)?", "أي مرحلة في الشكل (ثلم انشطار، وتكوّن الغلاف النووي والنوية)؟", [("Telophase and cytokinesis", "النهائي وانقسام السايتوبلازم"), ("Prophase", "التمهيدي"), ("Metaphase", "الاستوائي"), ("G2 of interphase", "G2 من الطور البيني")], "a", img="assets/stage-telophase-cytokinesis.jpg", img_h="44mm"),
 Q("Which stage is shown (early mitotic spindle and aster; chromosome of two sister chromatids inside the nucleus)?", "أي مرحلة في الشكل (مغزل انقسام مبكر ونجمة؛ كروموسوم من كروماتيدين داخل النواة)؟", [("Anaphase", "الانفصالي"), ("Telophase", "النهائي"), ("Prophase", "التمهيدي"), ("Metaphase", "الاستوائي")], "c", img="assets/stage-prophase.jpg", img_h="44mm"),
]

tf = [
 dict(en="Cell cycle events are under genetic control.", ar="أحداث دورة الخلية تحت سيطرة وراثية.", answer="T"),
 dict(en="In a 24-hour human cell cycle, cell division proper lasts about 12 hours.", ar="في دورة الخلية البشرية البالغة 24 ساعة يستغرق الانقسام الفعلي نحو 12 ساعة.", answer="F"),
 dict(en="DNA is replicated during G1.", ar="يتضاعف الـ DNA خلال G1.", answer="F"),
 dict(en="The amount of DNA per cell doubles in the S phase.", ar="تتضاعف كمية الـ DNA في الخلية في طور S.", answer="T"),
 dict(en="Proteins are synthesized in G2 in preparation for mitosis.", ar="تُخلَّق البروتينات في G2 استعدادًا للانقسام.", answer="T"),
 dict(en="The G1 phase lasts about 8 hours in actively dividing cells.", ar="يستغرق طور G1 نحو 8 ساعات في الخلايا النشطة الانقسام.", answer="T"),
 dict(en="Mitosis produces two genetically different daughter cells.", ar="ينتج الانقسام الخيطي خليتين بنويتين مختلفتين وراثيًا.", answer="F"),
 dict(en="Centrioles move towards opposite poles during prophase.", ar="تتحرّك الجسيمات المركزية نحو القطبين خلال الطور التمهيدي.", answer="T"),
 dict(en="Kinetochores are sites of attachment of spindle fibers.", ar="الحُبيبات الحركية مواقع لارتباط خيوط المغزل.", answer="T"),
 dict(en="Chromosomes reach the poles at the beginning of anaphase.", ar="تصل الكروموسومات إلى القطبين في بداية الطور الانفصالي.", answer="F"),
 dict(en="In telophase the spindle fibres disappear.", ar="في الطور النهائي تختفي خيوط المغزل.", answer="T"),
 dict(en="Cytokinesis is the fifth phase of mitosis.", ar="انقسام السايتوبلازم هو الطور الخامس من الانقسام الخيطي.", answer="F"),
 dict(en="The nucleolus and nuclear envelope are visible at the end of prophase.", ar="تظهر النوية والغلاف النووي في نهاية الطور التمهيدي.", answer="F"),
 dict(en="Interphase lasts more than 95% of the cell cycle.", ar="يستغرق الطور البيني أكثر من 95% من دورة الخلية.", answer="T"),
]

traps = [
 dict(en="G1 vs S vs G2", ar="G1 مقابل S مقابل G2", answer_en="G1: growth, no DNA replication, G1 checkpoint. S: DNA replication, DNA doubles, centriole duplicates. G2: protein synthesis for mitosis.", answer_ar="G1: نمو بلا تضاعف DNA ونقطة تفتيش G1. S: تضاعف الـ DNA والجسيم المركزي. G2: تخليق البروتينات للانقسام."),
 dict(en="Centromere vs centriole vs kinetochore", ar="القطعة المركزية مقابل الجسيم المركزي مقابل الحُبيبة الحركية", answer_en="Centromere: holds sister chromatids together. Centriole: moves to the poles, organizes the spindle. Kinetochore: disc on the centromere where spindle fibers attach.", answer_ar="القطعة المركزية: تربط الكروماتيدين. الجسيم المركزي: يتحرّك إلى القطبين وينظّم المغزل. الحُبيبة الحركية: قرص على القطعة المركزية ترتبط به خيوط المغزل."),
 dict(en="When does condensation start and finish?", ar="متى يبدأ التكثّف ومتى يكتمل؟", answer_en="It starts in prophase and is completed in metaphase.", answer_ar="يبدأ في الطور التمهيدي ويكتمل في الطور الاستوائي."),
 dict(en="What marks the start of anaphase?", ar="ما الذي يحدّد بداية الطور الانفصالي؟", answer_en="Division of the centromeres — not the arrival at the poles (which ends anaphase).", answer_ar="انقسام القطع المركزية — لا الوصول إلى القطبين (الذي يُنهي الطور)."),
 dict(en="Is cytokinesis part of mitosis?", ar="هل انقسام السايتوبلازم جزء من الانقسام الخيطي؟", answer_en="No — it is a separate process needed to complete cell division (the lecture also writes it as “cytokines”).", answer_ar="لا — هو عملية منفصلة ضرورية لإكمال الانقسام (وتكتبه المحاضرة أيضًا “cytokines”)."),
 dict(en="Interphase vs division time", ar="مدة الطور البيني مقابل الانقسام", answer_en="Human cell cycle ≈ 24 h: division ≈ 1 h; interphase > 95%. Actively dividing cells: total ≈ 20 h (G1 8, S 6, G2 4–5, M 1–2).", answer_ar="دورة الخلية البشرية ≈ 24 ساعة: الانقسام ≈ ساعة؛ البيني > 95%. الخلايا النشطة: الدورة ≈ 20 ساعة (G1 8، S 6، G2 4–5، M 1–2)."),
]

important = [
 dict(en="Define the cell cycle and give its importance.", ar="عرّف دورة الخلية واذكر أهميتها.", answer_en="A sequence of events in which DNA replication and cell growth take place and the cell divides into two daughter cells, under genetic control. Through it the fertilized egg develops into a mature organism, and hair, skin, blood cells and some internal organs are renewed.", answer_ar="سلسلة أحداث يحدث فيها تضاعف الـ DNA ونمو الخلية ثم تنقسم إلى خليتين بنويتين تحت سيطرة وراثية. وبها تتطوّر البيضة المخصّبة إلى كائن ناضج، ويتجدّد الشعر والجلد وخلايا الدم وبعض الأعضاء."),
 dict(en="Describe the phases of interphase.", ar="صف أطوار الطور البيني.", answer_en="G1: the cell grows but does not replicate DNA; G1 checkpoint. S: DNA replication, DNA doubles, centriole duplicates; each chromosome has two sister chromatids. G2: proteins synthesized for mitosis while growth continues.", answer_ar="G1: تنمو الخلية دون مضاعفة الـ DNA؛ نقطة تفتيش G1. S: تضاعف الـ DNA والجسيم المركزي؛ كل كروموسوم من كروماتيدين. G2: تخليق البروتينات للانقسام مع استمرار النمو."),
 dict(en="Give the durations of the cell-cycle phases in actively dividing cells.", ar="اذكر مدد أطوار دورة الخلية في الخلايا النشطة الانقسام.", answer_en="Division 1–2 h, G1 ≈ 8 h, S ≈ 6 h, G2 4–5 h; total ≈ 20 h.", answer_ar="الانقسام 1–2 ساعة، G1 ≈ 8، S ≈ 6، G2 4–5؛ المجموع ≈ 20 ساعة."),
 dict(en="Describe the events of prophase.", ar="صف أحداث الطور التمهيدي.", answer_en="Chromosome condensation begins; centrioles move to opposite poles; chromosomes appear as two chromatids joined at the centromere; the mitotic spindle starts to assemble; by its end the Golgi, ER, nucleolus and nuclear envelope are not seen.", answer_ar="يبدأ تكثّف الكروموسومات؛ تتحرّك الجسيمات المركزية إلى القطبين؛ يظهر الكروموسوم كروماتيدين عند القطعة المركزية؛ يبدأ تجميع المغزل؛ وفي نهايته لا تظهر كولجي والشبكة والنوية والغلاف النووي."),
 dict(en="Describe metaphase and define kinetochores.", ar="صف الطور الاستوائي وعرّف الحُبيبات الحركية.", answer_en="Condensation is completed; each chromosome has two sister chromatids held by the centromere; spindle fibers attach to kinetochores (small discs on the centromeres) and the chromosomes align on the metaphase plate.", answer_ar="يكتمل التكثّف؛ لكل كروموسوم كروماتيدان تربطهما القطعة المركزية؛ ترتبط خيوط المغزل بالحُبيبات الحركية (أقراص صغيرة على القطع المركزية) وتصطف الكروموسومات على الصفيحة الاستوائية."),
 dict(en="Compare anaphase and telophase.", ar="قارن بين الطور الانفصالي والنهائي.", answer_en="Anaphase: centromeres divide and daughter chromosomes migrate to opposite poles. Telophase: reversal of prophase — the nuclear membrane reforms, chromosomes uncoil, the spindle disappears, nucleolus, Golgi and ER reform.", answer_ar="الانفصالي: تنقسم القطع المركزية وتهاجر الكروموسومات البنوية إلى القطبين. النهائي: عكس التمهيدي — يُعاد تكوين الغشاء النووي، وتنفكّ الكروموسومات، ويختفي المغزل، وتعود النوية وكولجي والشبكة."),
 dict(en="What is cytokinesis?", ar="ما انقسام السايتوبلازم؟", answer_en="The division of nuclei, cytoplasm, organelles and cell membrane into two cells with roughly equal shares; it is not a phase of mitosis but a separate process that completes cell division.", answer_ar="تقسيم الأنوية والسايتوبلازم والعضيّات والغشاء إلى خليتين بحصص متساوية تقريبًا؛ وهو ليس طورًا من الانقسام بل عملية منفصلة تُكمل انقسام الخلية."),
]

data = {"meta": {
  "subject_en": "Genetics", "subject_ar": "علم الوراثة", "short_ar": "وراثة",
  "unit_en": "Lecture 1", "unit_ar": "المحاضرة 1", "unit_label": "LEC", "unit_no": "1",
  "title_en": "Cell cycle mitosis in animal cell and plant cell", "title_ar": "دورة الخلية والانقسام الخيطي في الخلية الحيوانية والنباتية",
  "kind": "Theory — نظري", "stage": "The third stage — الثالثة", "instructor": "د. عبد سلطان"},
 "blocks": blocks, "questions": {"mcq": mcq, "tf": tf, "traps": traps, "important": important}}
qs = [q for q in mcq if "answer" in q]
print(len(qs), Counter(q["answer"] for q in qs))
json.dump(data, open("/home/user/-/genetics-lec1-cell-cycle-mitosis/lecture.json", "w"), ensure_ascii=False, indent=1)
