---
source: BIOS-Obsidian/tools/scripts/par/make.py
handouts: [parasitology-week1-mcq]
saved: 2026-10-31
tags: [bios, code]
---
# par/make.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#parasitology-week1-mcq|parasitology-week1-mcq]]

```python
import json, os

ALL = ["All of the above", "جميع ما سبق"]
NONE = ["None of the above", "لا شيء مما سبق"]


def Q(en, ar, opts, ans, note=None):
    d = {"en": en, "ar": ar, "options": opts, "answer": ans}
    if note:
        d["note_en"], d["note_ar"] = note
    return d


def T(en, ar):
    return {"topic_en": en, "topic_ar": ar}


REL = [["Symbiosis", "التعايش (Symbiosis)"], ["Parasitism", "التطفّل (Parasitism)"], ["Commensalism", "المعايشة (Commensalism)"],
       ["Mutualism", "التقايض/المنفعة المتبادلة (Mutualism)"], ["None of above", "لا شيء مما سبق"]]

mcq = [
 T("General terms and classification", "مصطلحات عامة وتصنيف"),
 Q("Recent parasitic supergroups classification include … except:", "يشمل التصنيف الحديث للمجموعات الكبرى للطفيليات … ما عدا:",
   [["Excavate", "Excavate"], ["Amoebozoa", "Amoebozoa"], ["SAR", "SAR"], ["Chromista", "Chromista"], ["Mastigophora", "Mastigophora"]], "E"),
 Q("Recent parasitic supergroups classification include….except:", "يشمل التصنيف الحديث للمجموعات الكبرى للطفيليات … ما عدا:",
   [["Excavate", "Excavate"], ["Opisthokonta", "Opisthokonta"], ["SAR", "SAR"], ["Amoebozoa", "Amoebozoa"], ["Ciliophora", "Ciliophora"]], "E"),
 Q("Which of the following is mismatched:", "أيٌّ مما يأتي غير متطابق:",
   [["Excavate: Parasitic flagellates", "Excavate: السوطيات الطفيلية"], ["Amoebozoa: Non- flagellated parasitic amoebae", "Amoebozoa: الأميبات الطفيلية غير السوطية"],
    ["SAR: Apicomplexa", "SAR: معقّدات القمة (Apicomplexa)"], ["Excavate: Apicomplexa", "Excavate: معقّدات القمة (Apicomplexa)"],
    ["Opisthokonta: Parasitic helminthes", "Opisthokonta: الديدان الطفيلية"]], "D"),
 Q("Which of the following is mismatched:", "أيٌّ مما يأتي غير متطابق:",
   [["Chromista: Ciliates", "Chromista: الهدبيات"], ["Amoebozoa: Non- flagellated parasitic amoebae", "Amoebozoa: الأميبات الطفيلية غير السوطية"],
    ["SAR: Apicomplexa", "SAR: معقّدات القمة (Apicomplexa)"], ["Excavate: Apicomplexa", "Excavate: معقّدات القمة (Apicomplexa)"],
    ["Opisthokonta: Parasitic helminthes", "Opisthokonta: الديدان الطفيلية"]], "D"),
 Q("Medical Parasitology includes:", "يشمل علم الطفيليات الطبية:",
   [["Medical Entomology", "علم الحشرات الطبية"], ["Medical Protozoology", "علم الأوالي (الابتدائيات) الطبية"], ["Medical Helminthology", "علم الديدان الطبية"],
    ["B and C", "B و C"], ["A, B and C", "A و B و C"]], "E"),
 Q("The immunity system component that kills extracellular and intracellular forms protozoa and helminthes is:",
   "مكوّن الجهاز المناعي الذي يقتل الأطوار خارج الخلوية وداخل الخلوية للأوالي والديدان هو:",
   [["Macrophages", "البلاعم الكبيرة"], ["Neutrophils", "العدلات"], ["Natural killer NK cells", "الخلايا القاتلة الطبيعية NK"], ["Eosinophils", "الحمضات"], ["All", "جميعها"]], "E"),
 Q("The major immune response to protozoan is:", "الاستجابة المناعية الرئيسة تجاه الأوالي هي:",
   [["Pinocytosis", "الاحتساء الخلوي"], ["Phagocytosis", "البلعمة"], ["Plasmosis", "Plasmosis"], ["Saprozoic", "رمّي التغذية"], ALL], "B"),
 Q("Some parasites resist phagocytosis and may even replicate within macrophages, for example:",
   "بعض الطفيليات تقاوم البلعمة بل قد تتكاثر داخل البلاعم، ومثالها:",
   [["*Leishmania donovani*", "*Leishmania donovani*"], ["*Toxoplasma gondii*", "*Toxoplasma gondii*"], ["*Trichomonas vaginalis*", "*Trichomonas vaginalis*"],
    ["*Giardia lamblia*", "*Giardia lamblia*"], ["A and B", "A و B"]], "E"),
 Q("In immune evasion, the parasites get rid of plasma membrane in a process:", "في التهرّب المناعي، تتخلّص الطفيليات من الغشاء البلازمي في عملية تُسمّى:",
   [["Antigenic variation", "التغاير المستضدي"], ["Antigenic shedding", "الانسلاخ (الطرح) المستضدي"], ["Antigenic mimicry", "المحاكاة المستضدية"], ALL, NONE], "A",
   ("The source marks A. In standard references, getting rid of the surface membrane (and the antibodies bound to it) is antigenic shedding (B); antigenic variation means changing the surface antigens.",
    "المصدر يحدّد A. في المراجع المعتمدة، التخلّص من الغشاء السطحي (والأجسام المضادة المرتبطة به) يُسمّى الانسلاخ المستضدي (B)، أما التغاير المستضدي فهو تبديل المستضدات السطحية.")),
 Q("Protista mean … except:", "الطلائعيات (Protista) تعني … ما عدا:",
   [["Microorganism", "كائن مجهري"], ["Prokaryotic", "بدائي النواة"], ["Single cell", "وحيد الخلية"], ["Eukaryotic", "حقيقي النواة"], ["Protozoa", "الأوالي"]], "B"),
 Q("Animalia is … except:", "المملكة الحيوانية (Animalia) هي … ما عدا:",
   [["Macroorganism", "كائن كبير (مرئي)"], ["Protozoa", "الأوالي"], ["Metazoa", "متعددات الخلايا (Metazoa)"],
    ["Possessing well differentiated tissue and complex organ", "تمتلك أنسجة متمايزة جيدًا وأعضاء معقّدة"], ["Multicellular worm", "دودة متعددة الخلايا"]], "B"),
 Q("Subkingdom Protozoa include the following phyla---except:", "تضم تحت مملكة الأوالي الشُّعب الآتية — ما عدا:",
   [["Sarcomastigophora", "Sarcomastigophora"], ["Ciliophora", "Ciliophora"], ["Cestoda", "Cestoda"], ["Microsporidia", "Microsporidia"], ["Apicomplexa", "Apicomplexa"]], "C"),

 T("Parasite — types of relationship", "الطفيلي — أنواع العلاقة"),
 Q("Eating at the same table would be an appropriate description of:", "عبارة «الأكل على المائدة نفسها» وصف مناسب لـ:",
   [["Parasitism", "التطفّل"], ["Mutualism", "المنفعة المتبادلة"], ["Symbiosis", "التعايش"], ["Commensalism", "المعايشة"], ["All of above", "جميع ما سبق"]], "C",
   ("The source marks C. The word commensalism itself comes from Latin com mensa, “at the same table”, so most references give D.",
    "المصدر يحدّد C. كلمة المعايشة (Commensalism) مشتقة أصلًا من اللاتينية com mensa أي «على المائدة نفسها»، لذلك تعطي أغلب المراجع D.")),
 Q("The symbiosis in Parasitology, the relationships between two organisms it may be", "التعايش في علم الطفيليات، أي العلاقة بين كائنين، قد يكون",
   [["Mutualism", "منفعة متبادلة"], ["Commensalism", "معايشة"], ["Parasitism", "تطفّلًا"], ["All", "جميعها"], ["No one", "ولا واحد"]], "D"),
 Q("Mutualism refers to:", "تشير المنفعة المتبادلة إلى:",
   [["Each member benefits the other", "كل طرف ينفع الآخر"], ["One member benefits, while other does not", "طرف يستفيد والآخر لا يستفيد"],
    ["Both are harmed", "كلاهما يتضرّر"], ["All", "جميعها"], ["None", "لا شيء"]], "A"),
 Q("Mutualism:", "المنفعة المتبادلة:",
   [["Both benefit", "كلاهما يستفيد"], ["Harm to host only", "ضرر للمضيف فقط"], ["Harm to parasite only", "ضرر للطفيلي فقط"],
    ["No effect at all", "لا تأثير إطلاقًا"], ["Worst relationship", "أسوأ علاقة"]], "A"),
 Q("Commensalism mean:", "المعايشة تعني:",
   [["Both benefit, host and parasite", "يستفيد كلاهما، المضيف والطفيلي"], ["Harm to host only", "ضرر للمضيف فقط"], ["No effect", "لا تأثير"],
    ["Harm to parasite only", "ضرر للطفيلي فقط"], ["Worst relation", "أسوأ علاقة"]], "C"),
 Q("Commensalism:", "المعايشة:",
   [["Both benefit", "كلاهما يستفيد"], ["Worst relationship", "أسوأ علاقة"], ["One benefit, the other is not", "أحدهما يستفيد والآخر لا"],
    ["No benefit", "لا فائدة"], ["Free living phenomena", "ظاهرة المعيشة الحرة"]], "C"),
 Q("Parasite (not harm host just it benefits) is:", "الطفيلي (لا يضر المضيف وإنما يستفيد فقط) هو:",
   [["Parasitic", "متطفّل"], ["Commensal", "متعايش (Commensal)"], ["Mutual", "متبادل المنفعة"], ["Symbiosis", "تعايش"], ["None of these", "لا شيء مما ذُكر"]], "B"),
 Q("Parasite (not harm host just it benefits) relation mean:", "علاقة الطفيلي (لا يضر المضيف وإنما يستفيد فقط) تعني:",
   [["Phoresis", "الحَمْل (Phoresis)"], ["Symbiosis", "التعايش"], ["Parasite", "طفيلي"], ["Commensal", "متعايش (Commensal)"], ["None of above", "لا شيء مما سبق"]], "D"),
 Q("Commensalism:", "المعايشة:",
   [["Both are dependent upon each other that one cannot live without other", "كلاهما يعتمد على الآخر بحيث لا يعيش أحدهما من دون الآخر"],
    ["Worst relationship", "أسوأ علاقة"], ["Parasite only is deriving benefits without causing injury to host", "الطفيلي وحده يستفيد من دون أن يسبب أذى للمضيف"],
    ["No benefit", "لا فائدة"], ["Free living phenomena", "ظاهرة المعيشة الحرة"]], "C"),
 Q("Parasitism:", "التطفّل:",
   [["Host and parasite are benefit", "المضيف والطفيلي يستفيدان"], ["Worst relationship", "أسوأ علاقة"], ["Parasite and host are not benefit", "الطفيلي والمضيف لا يستفيدان"],
    ["Best relationship", "أفضل علاقة"], ["No effect occurs", "لا يحدث أي تأثير"]], "B"),
 Q("The most dangerous relationship for the host, with another organism is:", "أخطر علاقة على المضيف مع كائن آخر هي:", REL, "B"),
 Q("Parasitism mean:", "التطفّل يعني:",
   [["Host take benefit only", "المضيف وحده يستفيد"], ["Sexual stage", "الطور الجنسي"], ["Asexual stage", "الطور اللاجنسي"],
    ["One partner gets benefit and other injured", "طرف يستفيد والآخر يتضرّر"], ["Both partner get benefit.", "يستفيد الطرفان."]], "D"),
 Q("Parasitism is:", "التطفّل هو:",
   [["Host and Parasite both are benefit", "المضيف والطفيلي كلاهما يستفيد"], ["Worst relationship and cause injury for host", "أسوأ علاقة ويسبب أذى للمضيف"],
    ["Parasite and host are not benefit", "الطفيلي والمضيف لا يستفيدان"], ["Best relationship", "أفضل علاقة"], ["No effect occurs", "لا يحدث أي تأثير"]], "B"),
 Q("Terms for association of Parasites (Parasitism) mean:", "مصطلح ارتباط الطفيليات (التطفّل) يعني:",
   [["No association with host", "لا ارتباط بالمضيف"], ["Host take benefits only", "المضيف وحده يستفيد"],
    ["An association in which the parasite derives benefit and the host gets nothing in return but always suffers some injury",
     "ارتباط يستفيد فيه الطفيلي ولا يحصل المضيف على شيء في المقابل، بل يعاني دائمًا من بعض الأذى"],
    ["Sexual stage", "الطور الجنسي"], ["Asexual stage", "الطور اللاجنسي"]], "C"),
 Q("For the host, the most dangerous relationship with another organism is:", "بالنسبة إلى المضيف، أخطر علاقة مع كائن آخر هي:", REL, "B"),

 T("Parasite — types of parasites", "الطفيلي — أنواع الطفيليات"),
 Q("The typical characteristics of a parasite include:", "تشمل الصفات النموذجية للطفيلي:",
   [["Smaller than their host", "أصغر من مضيفه"], ["Outnumber the host", "يفوق المضيف عددًا"], ["Shorter life span than their host", "عمره أقصر من عمر مضيفه"],
    ["Have greater reproductive potential than their host", "قدرته التكاثرية أكبر من قدرة مضيفه"], ALL], "E"),
 Q("A parasite organism that lives on the outer surface of its host:", "كائن طفيلي يعيش على السطح الخارجي لمضيفه:",
   [["Ectoparasite", "طفيلي خارجي"], ["Endoparasite", "طفيلي داخلي"], ["Erratic Parasite", "طفيلي تائه (Erratic)"], ["A and B", "A و B"], ["None of above", "لا شيء مما سبق"]], "A"),
 Q("The parasites live on the external surface of the host called:", "الطفيليات التي تعيش على السطح الخارجي للمضيف تُسمّى:",
   [["Endoparasites", "طفيليات داخلية"], ["Ectoparasites", "طفيليات خارجية"], ["Obligate parasites", "طفيليات إجبارية"], ["Facultative parasites", "طفيليات اختيارية"], ["None", "لا شيء"]], "B"),
 Q("Ectoparasite:", "الطفيلي الخارجي:",
   [["Pin worm", "الدودة الدبوسية"], ["Tick, lice, fleas", "القراد، القمل، البراغيث"], ["Plasmodium spp.", "أنواع Plasmodium"],
    ["Lives inside the body", "يعيش داخل الجسم"], ["*Entamoeba histolytica*", "*Entamoeba histolytica*"]], "B"),
 Q("Endoparasite:", "الطفيلي الداخلي:",
   [["*Giardia lamblia*", "*Giardia lamblia*"], ["Found outside the body", "يوجد خارج الجسم"], ["Mite", "العث (الحلَم)"], ["Tick", "القراد"], ["Flea", "البرغوث"]], "A"),
 Q("Ectoparasite:", "الطفيلي الخارجي:",
   [["Pinworm", "الدودة الدبوسية"], ["Tick", "القراد"], ["Plasmodium spp.", "أنواع Plasmodium"], ["Lives inside the body", "يعيش داخل الجسم"],
    ["*Entamoeba histolytica*", "*Entamoeba histolytica*"]], "B"),
 Q("Endoparasite mean:", "الطفيلي الداخلي يعني:",
   [["Internal parasites; which live inside the body", "طفيليات داخلية؛ تعيش داخل الجسم"], ["Found in water", "يوجد في الماء"],
    ["Which live on the outside of the body", "تعيش على خارج الجسم"], ["Found on skin.", "يوجد على الجلد."], ["Found in soil", "يوجد في التربة"]], "A"),
 Q("The parasite which cannot exist without a host is:", "الطفيلي الذي لا يمكنه العيش من دون مضيف هو:",
   [["Erratic parasite", "طفيلي تائه"], ["Paratenic parasite", "طفيلي ناقل (Paratenic)"], ["Obligatory parasite", "طفيلي إجباري"],
    ["Facultative parasite", "طفيلي اختياري"], ["Accidental parasite", "طفيلي عرضي"]], "C"),
 Q("An obligatory parasite is that:", "الطفيلي الإجباري هو الذي:",
   [["Affects an unusual host", "يصيب مضيفًا غير معتاد"], ["Live in or on its host without leaving it", "يعيش في مضيفه أو عليه من دون أن يغادره"],
    ["Harbors the adult or sexually mature stages of the parasite", "يحمل الأطوار البالغة أو الناضجة جنسيًا للطفيلي"],
    ["Completely dependent on its host and can’t survive without it.", "يعتمد كليًا على مضيفه ولا يستطيع البقاء من دونه."], ["None of above", "لا شيء مما سبق"]], "D"),
 Q("The parasite which cannot exist without a host is call:", "الطفيلي الذي لا يمكنه العيش من دون مضيف يُسمّى:",
   [["Ectoparasite", "طفيلي خارجي"], ["Facultative parasite", "طفيلي اختياري"], ["Accidental parasite", "طفيلي عرضي"], ["Obligate parasite", "طفيلي إجباري"], ALL], "D"),
 Q("The facultative parasite is that:", "الطفيلي الاختياري هو الذي:",
   [["Affects An unusual host", "يصيب مضيفًا غير معتاد"], ["Visit the host only", "يزور المضيف فقط"],
    ["Can change its life cycle between free living and parasitic", "يستطيع تبديل دورة حياته بين المعيشة الحرة والتطفّل"],
    ["Completely dependent on its host", "يعتمد كليًا على مضيفه"], ["None of these", "لا شيء مما ذُكر"]], "C"),
 Q("The facultative parasite is:", "الطفيلي الاختياري هو:",
   [["Normally not a parasite, but will become parasite, if opportunity arises", "ليس طفيليًا في العادة، لكنه يصبح طفيليًا إذا سنحت الفرصة"],
    ["Cannot survive outside of a host", "لا يستطيع البقاء خارج المضيف"], ["Parasites an organism other than the usual host", "يتطفّل على كائن غير مضيفه المعتاد"],
    ["Established in or on the exterior surface of a host.", "يستقر في السطح الخارجي للمضيف أو عليه."], ["Established inside of a host", "يستقر داخل المضيف"]], "A"),
 Q("A pathogenic parasite is:", "الطفيلي الممرض هو:",
   [["A parasite which demonstrates the ability to cause disease", "طفيلي يُظهر القدرة على إحداث المرض"],
    ["A parasite which has the ability to reproduce inside man", "طفيلي له القدرة على التكاثر داخل الإنسان"],
    ["A parasite that could cause abscess", "طفيلي قد يسبب خرّاجًا"], ["A parasite which causes no harm to its host", "طفيلي لا يسبب أي ضرر لمضيفه"],
    ["A parasite with the ability to spore formation", "طفيلي له القدرة على تكوين الأبواغ"]], "A"),
 Q("In regard to protozoans, which of the following is incorrect?", "فيما يخص الأوالي، أيٌّ مما يأتي غير صحيح؟",
   [["The protozoal cell performs all functions", "خلية الأوالي تؤدي جميع الوظائف"],
    ["They are single celled prokaryotic microorganisms belong to kingdom Protista", "هي كائنات مجهرية وحيدة الخلية بدائية النواة تنتمي إلى مملكة الطلائعيات"],
    ["With no cell walls and therefore can assume an infinitive variety of shapes", "ليس لها جدار خلوي، لذلك تتخذ أشكالًا متنوعة بلا حدود"],
    ["Most of them are free living.", "أغلبها حرّة المعيشة."], ["Very small part of them cause diseases", "جزء صغير جدًا منها يسبب الأمراض"]], "B"),
 Q("Individual single celled microorganism are:", "الكائنات المجهرية المفردة وحيدة الخلية هي:",
   [["Protozoa", "الأوالي"], ["Helminthes", "الديدان"], ["Metazoan", "متعددات الخلايا"], ["Trematoda", "المثقوبات"], ["Cestoda", "الشريطيات"]], "A"),
 Q("Amoebiasis is transmitted by:", "ينتقل داء الأميبات عن طريق:",
   [["Skin pentration", "اختراق الجلد"], ["Insect vector", "حشرة ناقلة"], ["Oral- fecal contamination", "التلوث الفموي-البرازي"], ["Blood", "الدم"], ["Sexual intercourse", "الاتصال الجنسي"]], "C"),
 Q("If we Consider (+) as benefit ; and (-) as loss, and (0) as neutral, how could you describe parasitism?",
   "إذا عددنا (+) فائدة، و(-) خسارة، و(0) حيادًا، فكيف تصف التطفّل؟",
   [["++", "++"], ["+-", "+-"], ["00", "00"], ["0+", "0+"], ["0-", "0-"]], "B"),

 T("Host", "المضيف"),
 Q("Intermediate host:", "المضيف الوسطي:",
   [["Whom sexual reproduction occurs", "الذي يحدث فيه التكاثر الجنسي"], ["Asexual reproduction of the parasite occur", "يحدث فيه التكاثر اللاجنسي للطفيلي"],
    ["Harbor the adult parasite", "يحمل الطفيلي البالغ"], ["Found in direct life cycle", "يوجد في دورة الحياة المباشرة"], ["None of these", "لا شيء مما ذُكر"]], "B"),
 Q("Intermediate host:", "المضيف الوسطي:",
   [["Whom sexual reproduction occurs", "الذي يحدث فيه التكاثر الجنسي"], ["That harbors the adult", "الذي يحمل الطور البالغ"],
    ["Harbors the larval or asexual stages of the parasite", "يحمل الأطوار اليرقية أو اللاجنسية للطفيلي"], ["Found in direct life cycle", "يوجد في دورة الحياة المباشرة"], NONE], "C"),
 Q("A host that harbors the larval or asexual stage of a parasite is known as:", "المضيف الذي يحمل الطور اليرقي أو اللاجنسي للطفيلي يُعرف بـ:",
   [["Intermediate host", "المضيف الوسطي"], ["Reservoir host", "المضيف الخازن"], ["Accidental host", "المضيف العرضي"], ["Definitive host", "المضيف النهائي"], NONE], "A"),
 Q("A definitive host is that:", "المضيف النهائي هو الذي:",
   [["Visits the host only for feeding", "يزور المضيف للتغذية فقط"], ["Is completely dependent on its host", "يعتمد كليًا على مضيفه"], ["Affects an unusual host", "يصيب مضيفًا غير معتاد"],
    ["Harbors the adult or sexually mature stages of the parasite", "يحمل الأطوار البالغة أو الناضجة جنسيًا للطفيلي"],
    ["Is the developmental stage of a pathogenic organism.", "هو الطور التطوري لكائن ممرض."]], "D"),
 Q("The host in which the adult parasite lives and undergoes sexual reproduction is called:", "المضيف الذي يعيش فيه الطفيلي البالغ ويتكاثر جنسيًا يُسمّى:",
   [["Definitive host", "المضيف النهائي"], ["Accidental host", "المضيف العرضي"], ["Intermediate host", "المضيف الوسطي"], ["Vector", "الناقل"], ["None of these", "لا شيء مما ذُكر"]], "A"),
 Q("When the parasite remains viable without further development the host called:", "عندما يبقى الطفيلي حيًا من دون تطوّر إضافي، يُسمّى المضيف:",
   [["Paratenic host", "المضيف الناقل (Paratenic)"], ["Reservoir host", "المضيف الخازن"], ["Accidental host", "المضيف العرضي"], ["Facultative host", "المضيف الاختياري"], ["Final host", "المضيف النهائي"]], "A"),
 Q("Host that serves as a temporary refuge and vehicle for reaching an obligatory host, it is not necessary for the parasites life cycle:",
   "مضيف يعمل ملجأً مؤقتًا ووسيلةً للوصول إلى المضيف الإجباري، وليس ضروريًا لدورة حياة الطفيلي:",
   [["Paratenic host", "المضيف الناقل (Paratenic)"], ["Reservoir host", "المضيف الخازن"], ["Natural host", "المضيف الطبيعي"], ["Accidental host", "المضيف العرضي"], ["Facultative host", "المضيف الاختياري"]], "B",
   ("The source marks B. The wording “temporary refuge … not necessary for the life cycle” is the standard definition of a paratenic host (A), as in the question before it.",
    "المصدر يحدّد B. عبارة «ملجأ مؤقت … ليس ضروريًا لدورة الحياة» هي التعريف المعتمد للمضيف الناقل Paratenic (A)، كما في السؤال الذي قبله.")),
 Q("In the reservoir host:", "في المضيف الخازن:",
   [["The host neither develops nor causes any disease", "المضيف لا يتطوّر ولا يسبب أي مرض"], ["The parasite undergoes sexual reproduction", "يتكاثر الطفيلي جنسيًا"],
    ["The parasite neither develops nor causes any disease", "الطفيلي لا يتطوّر ولا يسبب أي مرض"], ["The parasite undergoes asexual reproduction", "يتكاثر الطفيلي لاجنسيًا"],
    ["The parasite has no chance to develop and unable to leave again the host", "لا فرصة للطفيلي للتطوّر ولا يستطيع مغادرة المضيف مرة أخرى"]], "C"),
 Q("The Vector is:", "الناقل هو:",
   [["A host keep the infective stages of a parasite", "مضيف يحتفظ بالأطوار المُعدية للطفيلي"], ["A host in which parasites have no chance to develop", "مضيف لا فرصة للطفيليات فيه للتطوّر"],
    ["A host that harbors the adult stage of a parasite", "مضيف يحمل الطور البالغ للطفيلي"], ["A host that harbors the immature stages of a parasite", "مضيف يحمل الأطوار غير الناضجة للطفيلي"],
    ["An arthropod that transfers an infection agent from one host to another", "مفصلي ينقل العامل المُعدي من مضيف إلى آخر"]], "E"),
 Q("The Vector is:", "الناقل هو:",
   [["A host keep the infective stages of a parasite in its body when the main host is not available", "مضيف يحتفظ بالأطوار المُعدية للطفيلي في جسمه عندما لا يتوفر المضيف الرئيس"],
    ["A host in which parasites have no chance to develop and unable to leave again this host", "مضيف لا فرصة للطفيليات فيه للتطوّر ولا تستطيع مغادرته مرة أخرى"],
    ["A host that harbors the adult stage of a parasite or a host in which the parasite undergoes sexual reproduction", "مضيف يحمل الطور البالغ للطفيلي، أو مضيف يتكاثر فيه الطفيلي جنسيًا"],
    ["A host that harbors the immature stages of a parasite or a host in which the parasite undergoes asexual reproduction", "مضيف يحمل الأطوار غير الناضجة للطفيلي، أو مضيف يتكاثر فيه الطفيلي لاجنسيًا"],
    ["An arthropod that transfers an infection agent from one host to another", "مفصلي ينقل العامل المُعدي من مضيف إلى آخر"]], "E"),

 T("Stages and life cycle", "الأطوار ودورة الحياة"),
 Q("A parasite which can enter the host and continue development is:", "الطفيلي الذي يستطيع دخول المضيف ومواصلة التطوّر هو:",
   [["Diagnostic stage", "الطور التشخيصي"], ["Accidental parasite", "طفيلي عرضي"], ["Infective stage", "الطور المُعدي"], ["Obligatory parasite.", "طفيلي إجباري."], ["Facultative Parasite", "طفيلي اختياري"]], "C"),
 Q("Invasion of the body by any pathogenic organism (Endoparasite, Protozoa or helminthes):", "غزو الجسم بأي كائن ممرض (طفيلي داخلي، أوالي أو ديدان):",
   [["Infective stage", "الطور المُعدي"], ["Diagnostic stage", "الطور التشخيصي"], ["Pathogenesis", "الإمراضية"], ["Parasitic infection", "الإصابة الطفيلية"], ["None of above", "لا شيء مما سبق"]], "A",
   ("The source marks A. The definition “invasion of the body by a pathogenic organism” describes parasitic infection (D); the infective stage is the stage able to enter the host (see the question before).",
    "المصدر يحدّد A. تعريف «غزو الجسم بكائن ممرض» يصف الإصابة الطفيلية (D)، أما الطور المُعدي فهو الطور القادر على دخول المضيف (انظر السؤال السابق).")),
 Q("Diagnostic stage is mean:", "الطور التشخيصي يعني:",
   [["The stage of parasite at which it is capable of entering the host.", "طور الطفيلي الذي يكون فيه قادرًا على دخول المضيف."],
    ["A developmental stage of a pathogenic organism that can be detected in stool, blood, urine , sputum ,CSF", "طور تطوري لكائن ممرض يمكن الكشف عنه في البراز أو الدم أو الإدرار أو القشع أو السائل الدماغي الشوكي"],
    ["Invasion of the body by any pathogenic organism", "غزو الجسم بأي كائن ممرض"], ["Infection stage", "طور الإصابة"], NONE], "B"),
 Q("Direct life cycle:", "دورة الحياة المباشرة:",
   [["Has two hosts", "لها مضيفان"], ["Has 3 hosts", "لها 3 مضيفات"], ["Found in intermediate host", "توجد في المضيف الوسطي"], ["Has one host", "لها مضيف واحد"], ALL], "D"),
 Q("Direct life cycle:", "دورة الحياة المباشرة:",
   [["Has two hosts", "لها مضيفان"], ["Enter host directly", "تدخل المضيف مباشرة"], ["Has one host", "لها مضيف واحد"],
    ["*Diphyllobothrium latum*", "*Diphyllobothrium latum*"], ["Plasmodium spp", "أنواع Plasmodium"]], "C"),
 Q("Indirect life cycle:", "دورة الحياة غير المباشرة:",
   [["Enter host indirectly", "تدخل المضيف بصورة غير مباشرة"], ["Plasmodium spp.", "أنواع Plasmodium"], ["*Endolemax nana*", "*Endolemax nana*"],
    ["*Giardia lamblia*", "*Giardia lamblia*"], ["Enter host di [[cut]]", "تدخل المضيف … [[قطع]]"]], "B"),
]

n = sum(1 for q in mcq if "topic_en" not in q)
print("questions:", n)
from collections import Counter
print(Counter(q["answer"] for q in mcq if "answer" in q))

data = {
 "meta": {
  "theme": "plum",
  "subject_en": "Diagnostic Parasitology", "subject_ar": "الطفيليات التشخيصية",
  "instructor": "أ.د. نزار الخفاجي",
  "unit_en": "Week 1", "unit_ar": "الأسبوع 1", "unit_label": "WEEK", "unit_no": "1",
  "title_en": "Terms used in Parasitology", "title_ar": "المصطلحات المستعملة في علم الطفيليات",
  "department": "قسم التحليلات", "stage": "The fourth stage — الرابعة",
  "kind": "Theory — نظري", "questions_kind": "MCQ — أسئلة اختيار", "translator": "محمد حامد",
  "file_name": "BIOS - Diagnostic Parasitology - Week 1 - MCQ"
 },
 "questions": {
  "title_en": "Terms used in Parasitology", "title_ar": "المصطلحات المستعملة في علم الطفيليات",
  "sub": "MCQ",
  "mcq_en": "MCQ — 1st semester, week 1", "mcq_ar": "أسئلة الاختيار — الفصل الأول، الأسبوع الأول",
  "intro_en": "Q. Select the most correct answer from the followings",
  "intro_ar": "س. اختر الإجابة الأصح مما يأتي",
  "mcq": mcq
 }
}
out = "/home/user/-/parasitology-week1-mcq/lecture.json"
os.makedirs(os.path.dirname(out), exist_ok=True)
json.dump(data, open(out, "w"), ensure_ascii=False, indent=1)

```
