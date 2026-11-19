import sys, os, json
WORK = "/tmp/claude-0/-home-user/8d90b83d-8398-5b0c-8a4a-924e1daeb159/scratchpad/work"
sys.path.insert(0, WORK)
from bidi import ltr_all

def Q(en, ar, opts, ans=None, note=None):
    d = {"en": en, "ar": ar, "options": opts}
    if ans:
        d["answer"] = ans
    if note:
        d["note_en"], d["note_ar"] = note
    return d

def T(en, ar):
    return {"topic_en": en, "topic_ar": ar}

def S(latin, ar):
    return ["__%s__" % latin, ar]

ALL  = ["All of the above", "جميع ما سبق"]
NONE = ["None of the above", "لا شيء مما سبق"]
NONEb = ["None", "لا شيء"]

# species
Tc = lambda: S("Trypanosoma cruzi", "المثقبية الكروزية")
Tb = lambda: S("Trypanosoma brucei", "المثقبية البروسية")

mcq = [
 T("Trypanosoma", "المثقبيات (Trypanosoma)"),

 Q("Trypanosoma is spread by:", "تنتشر المثقبيات بـ:",
   [["Bites from infected Tsetse flies", "لسعات ذباب تسي تسي المصاب"],
    ["Fecal – oral contamination", "التلوّث البرازي – الفموي"],
    ["Direct contact from an infected person", "التماس المباشر من شخص مصاب"],
    ["Sexually", "جنسيًّا"], ["Consuming under cooked meat", "تناول لحم غير مطهوّ جيدًا"]], "A"),

 Q("African trypanosomiasis is transmitted by:", "ينتقل داء المثقبيات الإفريقي بـ:",
   [["Stable fly", "الذبابة الثابتة"], ["Black fly", "الذبابة السوداء"], ["Tsetse fly", "ذبابة تسي تسي"],
    ["Sand fly", "ذبابة الرمل"], ["House fly", "الذبابة المنزلية"]], "C"),

 Q("Trypanosoma cruzi is transmitted by:", "تنتقل المثقبية الكروزية بـ:",
   [["Tsetse fly", "ذبابة تسي تسي"], ["Sand fly", "ذبابة الرمل"], ["Reduviid bug", "بقّة الريدوفيد (حشرة التقبيل)"],
    ["House fly", "الذبابة المنزلية"], ["Mosquitoes", "البعوض"]], "C"),

 Q("Biological vector of Chaga’s disease:", "الناقل البيولوجي لداء شاغاس:",
   [["Reduviid bug", "بقّة الريدوفيد (حشرة التقبيل)"], ["Horse fly", "ذبابة الخيل"], ["House fly", "الذبابة المنزلية"],
    ["Mosquito", "البعوض"], NONEb], "A"),

 Q("Vector for Trypanosoma cruzi is:", "ناقل المثقبية الكروزية هو:",
   [["Reduviid bug", "بقّة الريدوفيد (حشرة التقبيل)"], ["Tsetse fly", "ذبابة تسي تسي"], ["Sand fly", "ذبابة الرمل"],
    ["Hard tick", "القُراد الصلب"], ["House fly", "الذبابة المنزلية"]], "A"),

 Q("The intermediate stage of T. cruzi is:", "الطور/العائل الوسطي للمثقبية الكروزية هو:",
   [["Sand flies", "ذباب الرمل"], ["Tsetse", "ذبابة تسي تسي"], ["Reduviid bug", "بقّة الريدوفيد (حشرة التقبيل)"],
    ["Mosquito", "البعوض"], ["Man", "الإنسان"]], "C"),

 Q("The final host of Trypanosoma brucei for human is:", "العائل النهائي للمثقبية البروسية بالنسبة للإنسان هو:",
   [["Man", "الإنسان"], ["Glossina spp. (Tsetse fly)", "جنس Glossina (ذبابة تسي تسي)"], ["Cat", "القطة"],
    ["Dog", "الكلب"], NONE], "B"),

 Q("The African Trypanosomiasis is:", "داء المثقبيات الإفريقي هو:",
   [["Bacterium", "جرثومة"], ["Protozoan", "أوالٍ (بروتوزوا)"], ["Virus", "فيروس"],
    ["Fungus", "فطر"], ["Yeast", "خميرة"]], "B"),

 Q("Tsetse fly is a vector for sleeping sickness, which of the following parasite transmitted the infective stage:",
   "ذبابة تسي تسي ناقلة لداء النوم، فأيُّ الطفيليات الآتية تنقل الطور المُعدي:",
   [S("Leishmania donovani", "الليشمانيا الدونوفانية"), S("Plasmodium falciparum", "المتصوّرة المنجلية"),
    S("Trypanosoma gambiense", "المثقبية الغامبية"), S("Trichomonas vaginalis", "المشعرة المهبلية"),
    S("Diphyllobothrium latum", "الشريطية العريضة")], "C"),

 Q("Each of the following statements concerning sleeping sickness is correct except:",
   "كل عبارة مما يأتي عن داء النوم صحيحة ما عدا:",
   [["Sleeping sickness is caused by trypanosome", "يسبّب داء النوم المثقبيات"],
    ["Sleeping sickness occur primarily in tropical Africa", "يحدث داء النوم أساسًا في إفريقيا المدارية"],
    ["Sleeping sickness can be diagnosed by finding eggs in the stool", "يُشخَّص داء النوم بإيجاد بيوض في البراز"],
    ["Sleeping sickness is transmitted by tsetse flies", "ينتقل داء النوم بذباب تسي تسي"],
    ["All false", "جميعها خاطئة"]], "C"),

 Q("A boy with bloody diarrhea was seen by a physician. The specimen was sent to the laboratory and then stained by modified acid – fast method, which appears the diameter of the objects is approximately 3.3 µm. Based on what criteria diagnosis is:",
   "صبيّ مصاب بإسهال دموي عاينه طبيب، وأُرسلت العيّنة للمختبر وصُبغت بطريقة الصباغ الصامد للحمض المعدّلة، فظهر قطر الأجسام نحو `3.3 µm`. بناءً على هذه المعايير، التشخيص هو:",
   [S("Cryptosporidium parvum", "الخفيّة الصغيرة (Cryptosporidium parvum)"), S("Toxoplasma gondii", "المقوّسة الغوندية"),
    S("Giardia lamblia", "الجيارديا اللمبلية"), S("Trichomonas vaginalis", "المشعرة المهبلية"),
    S("Leishmania donovani", "الليشمانيا الدونوفانية")], "A"),

 Q("Chagas disease that is prevalent in Latin America is caused by:",
   "داء شاغاس المنتشر في أمريكا اللاتينية يسبّبه:",
   [Tc(), S("Trypanosome brucei", "المثقبية البروسية"), S("L. brazilience", "الليشمانيا البرازيلية"),
    S("Toxoplasma", "المقوّسة"), NONE], "A"),

 Q("Trypanosoma cruzi cause ------ in humans:", "تسبّب المثقبية الكروزية ------ في الإنسان:",
   [["Chronic African trypanosomiasis", "داء المثقبيات الإفريقي المزمن"], ["Chagas disease", "داء شاغاس"],
    ["Leishmaniasis", "داء الليشمانيات"], ["Visceral leishmaniasis", "داء الليشمانيات الحشوي"],
    ["East African sleeping sickness", "داء النوم الإفريقي الشرقي"]], "B"),

 Q("Sleeping sickness in Africa is caused by:", "داء النوم في إفريقيا يسبّبه:",
   [S("Leishmania tropica", "الليشمانيا المدارية"), ["Malaria", "الملاريا"],
    S("Trypanosoma gambience", "المثقبية الغامبية"), Tc(), NONE], "C"),

 Q("Which of the following species is not injected through the bite of mouthparts of the insect vector?",
   "أيُّ الأنواع الآتية لا يُحقن عبر لسعة أجزاء فم الحشرة الناقلة؟",
   [Tb(), Tc(), S("Leishmania donovani", "الليشمانيا الدونوفانية"),
    S("Trypanosoma rhodesiense", "المثقبية الروديسية"), S("Trypanosoma evansi", "مثقبية إيفانس")], "B",
   ("T. cruzi is transmitted by the contaminated feces of the reduviid bug rubbed into the bite site, not injected through the bite itself (stercorarian transmission).",
    "تنتقل المثقبية الكروزية عبر براز بقّة الريدوفيد الملوّث الذي يُفرَك في موضع اللسعة، لا بالحقن عبر اللسعة نفسها (انتقال برازي/ستيركوراري).")),

 Q("Which of the following is exclusively an intracellular parasite in the definitive host?",
   "أيُّ ما يأتي طفيلي داخل خلوي حصريًّا في العائل النهائي؟",
   [["Cutaneous leishmaniasis", "داء الليشمانيات الجلدي"], ["African trypanosomiasis", "داء المثقبيات الإفريقي"],
    ["Visceral leishmaniasis", "داء الليشمانيات الحشوي"], ["A, B and C", "A و B و C"], ["A and C", "A و C"]], "E"),

 Q("In Trypanosoma cruzi life cycle:", "في دورة حياة المثقبية الكروزية:",
   [["The parasites differentiate into infective metacyclic epimastigotes in the foregut",
     "تتمايز الطفيليات إلى أطوار فوق سوطية استحالية مُعدية في المعي الأمامي"],
    ["The parasites differentiate into infective metacyclic amastigote in the hindgut",
     "تتمايز الطفيليات إلى طور عديم السوط استحالي مُعدٍ في المعي الخلفي"],
    ["The parasites differentiated into infective metacyclic trypomastigote in the foregut",
     "تتمايز الطفيليات إلى طور مثقبي استحالي مُعدٍ في المعي الأمامي"],
    ["The parasite differentiate into infective metacyclic promastigote in the hindgut",
     "يتمايز الطفيلي إلى طور أمامي السوط استحالي مُعدٍ في المعي الخلفي"],
    ["The parasite differentiated into infective metacyclic trypomastigote in the hind gut",
     "يتمايز الطفيلي إلى طور مثقبي استحالي مُعدٍ في المعي الخلفي"]], "E"),

 Q("Stage I disease of African sleeping sickness includes:", "المرحلة الأولى من داء النوم الإفريقي تشمل:",
   [["Myocarditis and anemia develop infrequently in patients", "التهاب عضلة القلب وفقر الدم يتطوّران نادرًا في المرضى"],
    ["Myocarditis, anemia and profound coma develop frequently in patients",
     "التهاب عضلة القلب وفقر الدم وغيبوبة عميقة تتطوّر كثيرًا في المرضى"],
    ["Myocarditis, anemia, fatigue, headache, muscle aches and day time sleeping in patient",
     "التهاب عضلة القلب وفقر الدم والإعياء والصداع وآلام العضلات والنوم النهاري في المريض"],
    ["Myocarditis and anemia develop frequently in patients", "التهاب عضلة القلب وفقر الدم يتطوّران كثيرًا في المرضى"],
    ["Myocarditis and anemia develop occasionally in patients", "التهاب عضلة القلب وفقر الدم يتطوّران أحيانًا في المرضى"]], "D"),

 Q("The stage II disease of African sleeping sickness:", "المرحلة الثانية من داء النوم الإفريقي:",
   [["In chronic infection, the parasites cross the blood – brain barrier and invade the Central Nervous System (CMS)",
     "في العدوى المزمنة، تعبر الطفيليات الحاجز الدموي الدماغي وتغزو الجهاز العصبي المركزي (CMS)"],
    ["In chronic infection, the parasites cross the blood – brain barrier and invade the Central Nervous System (CNS)",
     "في العدوى المزمنة، تعبر الطفيليات الحاجز الدموي الدماغي وتغزو الجهاز العصبي المركزي (CNS)"],
    ["In acute infection, the parasites cross the blood- brain barrier and invade the Central Nervous System (CMS)",
     "في العدوى الحادّة، تعبر الطفيليات الحاجز الدموي الدماغي وتغزو الجهاز العصبي المركزي (CMS)"],
    ["In acute infection, the parasites cross the blood – brain barrier and invade the Central Nervous System (CNS)",
     "في العدوى الحادّة، تعبر الطفيليات الحاجز الدموي الدماغي وتغزو الجهاز العصبي المركزي (CNS)"],
    ["In chronic infection, the parasites fail to cross the blood -brain barrier and invade the Central Nervous System (CNS)",
     "في العدوى المزمنة، تفشل الطفيليات في عبور الحاجز الدموي الدماغي وغزو الجهاز العصبي المركزي (CNS)"]], "B"),

 Q("Which statement of the following is mismatched:", "أيُّ العبارات الآتية غير متطابقة:",
   [["West African sleeping sickness; Trypanosoma brucei gambiense",
     "داء النوم الإفريقي الغربي؛ المثقبية البروسية الغامبية"],
    ["American trypanosomaisis; Trypanosoma cruzi", "داء المثقبيات الأمريكي؛ المثقبية الكروزية"],
    ["Visceral leishmaniasis; Leishmania donovani", "داء الليشمانيات الحشوي؛ الليشمانيا الدونوفانية"],
    ["East African sleeping sickness; Trypanosoma cruzi rhodesiense",
     "داء النوم الإفريقي الشرقي؛ المثقبية الكروزية الروديسية"],
    ["Mucocutaneous leishmaniasis; Leishmania braziliense", "داء الليشمانيات المخاطي الجلدي؛ الليشمانيا البرازيلية"]], "D",
   ("East African sleeping sickness is caused by Trypanosoma brucei rhodesiense, not “Trypanosoma cruzi rhodesiense”; that is why D is the mismatched (correct) choice.",
    "داء النوم الإفريقي الشرقي تسبّبه المثقبية البروسية الروديسية لا «المثقبية الكروزية الروديسية»؛ لذلك D هو الخيار غير المتطابق (الصحيح).")),

 Q("Choose the correct statement of the following:", "اختر العبارة الصحيحة مما يأتي:",
   [["Tsetse fly (Triatoma) becomes infected with blood stream trypomastigotes when taking a blood meal from infected human",
     "ذبابة تسي تسي (Triatoma) تُصاب بالأطوار المثقبية في مجرى الدم عند أخذها وجبة دم من إنسان مصاب"],
    ["Tsetse fly (Glossina) becomes infected with bloodstream epimastigotes when taking a blood meal from infected human",
     "ذبابة تسي تسي (Glossina) تُصاب بالأطوار فوق السوطية في مجرى الدم عند أخذها وجبة دم من إنسان مصاب"],
    ["Tsetse fly (Phlebotomus) becomes infected with blood stream trypomastigotes when taking a blood meal from infected human",
     "ذبابة تسي تسي (Phlebotomus) تُصاب بالأطوار المثقبية في مجرى الدم عند أخذها وجبة دم من إنسان مصاب"],
    ["Tsetse fly (Glossina) becomes infected with bloodstream promastigotes when taking a blood meal from infected human",
     "ذبابة تسي تسي (Glossina) تُصاب بالأطوار أمامية السوط في مجرى الدم عند أخذها وجبة دم من إنسان مصاب"],
    ["Tsetse fly (Glossina) becomes infected with blood stream trypomastigote when taking a bloodmeal from infected human",
     "ذبابة تسي تسي (Glossina) تُصاب بالأطوار المثقبية في مجرى الدم عند أخذها وجبة دم من إنسان مصاب"]], "E"),

 Q("The infective stage for both of Trypanosoma cruzi and T. brucei is:",
   "الطور المُعدي لكلٍّ من المثقبية الكروزية والمثقبية البروسية هو:",
   [["Metacyclic promastigote", "الطور أمامي السوط الاستحالي"], ["Metacyclic amastigote", "الطور عديم السوط الاستحالي"],
    ["Metacyclic trypomastigotes", "الأطوار المثقبية الاستحالية"], ["Metacyclic epimastigote", "الطور فوق السوطي الاستحالي"],
    ALL], "C"),

 Q("Trypanosoma gambienze:", "المثقبية الغامبية:",
   [["Present in Iraq", "موجودة في العراق"], ["Sand fly is the vector", "ذبابة الرمل هي الناقل"],
    ["Cause ASS", "تسبّب داء النوم الإفريقي (ASS)"], ["Intracellular protozoa", "أوالٍ داخل خلوية"],
    ["Trophozoite contains blood", "الطور المتحرّك يحتوي دمًا"]], "C"),

 Q("Which of the following parasites is the causes of African Sleeping Sickness:",
   "أيُّ الطفيليات الآتية مسبّب لداء النوم الإفريقي:",
   [["Leishmania", "الليشمانيا"], ["Trypanosoma", "المثقبيات"], ["Entamoeba", "الأميبا"],
    ["Trichomonas", "المشعرات"], ["Plasmodium", "المتصوّرات"]], "B"),

 Q("Which of the following parasites is responsible for the cause of African Sleeping Sickness:",
   "أيُّ الطفيليات الآتية مسؤول عن حدوث داء النوم الإفريقي:",
   [["Leishmania", "الليشمانيا"], ["Trypanosoma", "المثقبيات"], ["Entamoeba", "الأميبا"],
    ["Trichomonas", "المشعرات"], ["Plasmodium", "المتصوّرات"]], "B"),

 Q("The final host of Trypanosoma brucei for human is:", "العائل النهائي للمثقبية البروسية بالنسبة للإنسان هو:",
   [["Man", "الإنسان"], ["Glossina spp. (Tsetse fly)", "جنس Glossina (ذبابة تسي تسي)"], ["Cat", "القطة"],
    ["Dog", "الكلب"], NONE], "B"),

 Q("The developing stage of trypanosomatidae that does not have free flagellum is:",
   "الطور النامي من المثقبيات الذي لا يملك سوطًا حرًّا هو:",
   [["Amastigote", "عديم السوط (Amastigote)"], ["Trypomastigote", "المثقبي (Trypomastigote)"],
    ["Epimastigote", "فوق السوطي (Epimastigote)"], ["Promastigote", "أمامي السوط (Promastigote)"], ALL], "A"),

 Q("Among blood flagellates, the stage of development that has an undulating membrane, and a kinetoplast located posterior to the nucleus, is the:",
   "من بين السوطيات الدموية، الطور الذي له غشاء متموّج وكينيتوبلاست خلف النواة هو:",
   [["Trypomastigote", "المثقبي (Trypomastigote)"], ["Epimastigote", "فوق السوطي (Epimastigote)"],
    ["Amastigote", "عديم السوط (Amastigote)"], ["Promastigote", "أمامي السوط (Promastigote)"], NONE], "A"),

 Q("Schuffner’s dot in RBCs are seen in infection with:", "نقاط شوفنر في كريات الدم الحمراء تُرى في العدوى بـ:",
   [S("Plasmodium vivax", "المتصوّرة النشيطة"), S("Plasmodium falciparum", "المتصوّرة المنجلية"),
    S("Plasmodium malariae", "المتصوّرة الوبالية"), S("Plasmodium ovale", "المتصوّرة البيضوية"),
    ["A and D", "A و D"]], "E"),

 Q("Diagnostic stage of Trypanosoma gambiense is:", "الطور التشخيصي للمثقبية الغامبية هو:",
   [["Tachyzoite", "البوغيّة السريعة (Tachyzoite)"], ["Cyst", "الكيس"], ["Amastigote", "عديم السوط (Amastigote)"],
    ["Bradyzoite", "البوغيّة البطيئة (Bradyzoite)"], ["Trypomastigote", "المثقبي (Trypomastigote)"]], "C",
   ("The source marks Amastigote, but T. b. gambiense has no amastigote stage in humans; it circulates in blood, lymph and CSF as the trypomastigote, which is the diagnostic stage (E).",
    "المصدر يحدّد «عديم السوط»، لكن المثقبية الغامبية ليس لها طور عديم السوط في الإنسان؛ فهي تدور في الدم واللمف والسائل الدماغي الشوكي بالطور المثقبي، وهو الطور التشخيصي (E).")),

 Q("Diagnostic stage of cutaneous leishmaniasis:", "الطور التشخيصي لداء الليشمانيات الجلدي:",
   [["Tachyzoit", "البوغيّة السريعة (Tachyzoite)"], ["Cyst", "الكيس"], ["Amastigote", "عديم السوط (Amastigote)"],
    ["Bradyzoite", "البوغيّة البطيئة (Bradyzoite)"], ALL], "C"),

 Q("The sand flies are responsible for transmission of the following disease to humans:",
   "ذباب الرمل مسؤول عن نقل المرض الآتي إلى الإنسان:",
   [["Filariasis", "داء الفيلاريات"], ["Amoebiais", "داء الأميبات"], ["Giardiasis", "داء الجيارديا"],
    ["Leishmaniasis", "داء الليشمانيات"], ["Toxoplasmosis", "داء المقوّسات"]], None,
   ("Not marked in the source file. Scientifically the answer is D: sand flies (Phlebotomus) transmit leishmaniasis.",
    "غير مؤشَّر في الملف الأصلي. والجواب الصحيح علميًّا هو D: ذباب الرمل (Phlebotomus) ينقل داء الليشمانيات.")),

 Q("Glossdina spp. (Tsetse fly) is the vector that transport:", "جنس Glossina (ذبابة تسي تسي) هو الناقل الذي ينقل:",
   [S("Trichomonas vaginalis", "المشعرة المهبلية"), S("Trypanosoma brucei gambiense", "المثقبية البروسية الغامبية"),
    S("Leishmania donovani", "الليشمانيا الدونوفانية"), S("Toxoplasma gondii", "المقوّسة الغوندية"),
    ["Plasmodium spp", "أنواع المتصوّرات (Plasmodium spp)"]], "B"),

 Q("Typical trypanosoma structure:", "البنية النموذجية للمثقبية:",
   [["Elongated -Spindle-Shaped body more or less tapers at both ends",
     "جسم مستطيل مغزلي الشكل يدقّ تقريبًا عند الطرفين"],
    ["A centrally situated nucleus", "نواة تقع مركزيًّا"],
    ["Kinetoplast posterior to nucleus", "كينيتوبلاست خلف النواة"],
    ["Undulating membrane proceding form", "غشاء متموّج ممتدّ"],
    ["Single free flagella at anterior end", "سوط حرّ واحد عند الطرف الأمامي"]], None,
   ("Not marked in the source file. All the listed items are true features of a typical trypanosome, so the intended answer appears to be “all of the above.”",
    "غير مؤشَّر في الملف الأصلي. وكل البنود المذكورة صفات صحيحة للمثقبية النموذجية، فيبدو أن المطلوب «جميع ما سبق».")),

 Q("The developing stage of Trypanosomatidae that does not have free flagellum is:",
   "الطور النامي من المثقبيات الذي لا يملك سوطًا حرًّا هو:",
   [["Trypomastigote", "المثقبي (Trypomastigote)"], ["Epimastiogote", "فوق السوطي (Epimastigote)"],
    ["Promastigote", "أمامي السوط (Promastigote)"], ["Amastigote", "عديم السوط (Amastigote)"],
    ["All of the above with free flagellum", "جميع ما سبق له سوط حرّ"]], "D"),

 Q("Trypanosoma is spread by:", "تنتشر المثقبيات بـ:",
   [["Bites from infected Tsetse flies", "لسعات ذباب تسي تسي المصاب"],
    ["Fecal – oral contamination", "التلوّث البرازي – الفموي"],
    ["Direct contact from an infected person", "التماس المباشر من شخص مصاب"],
    ["Sexually", "جنسيًّا"], ["Consuming under cooked meat", "تناول لحم غير مطهوّ جيدًا"]], "A"),

 Q("The final host of Trypanosoma brucei for human is:", "العائل النهائي للمثقبية البروسية بالنسبة للإنسان هو:",
   [["Man", "الإنسان"], ["Glossina spp. (Tsetse fly)", "جنس Glossina (ذبابة تسي تسي)"], ["Cat", "القطة"],
    ["Dog", "الكلب"], NONE], "B"),

 Q("Sleeping sickness in Africa is caused by:", "داء النوم في إفريقيا يسبّبه:",
   [S("Leishmania tropica", "الليشمانيا المدارية"), ["Malaria", "الملاريا"],
    S("Trypanosoma gambience", "المثقبية الغامبية"), Tc(), NONE], "C"),

 Q("Tsetse fly is a vector for sleeping sickness, which of the following parasite transmitted the infective stage:",
   "ذبابة تسي تسي ناقلة لداء النوم، فأيُّ الطفيليات الآتية تنقل الطور المُعدي:",
   [S("Leishmania donovani", "الليشمانيا الدونوفانية"), S("Plasmodium falciparum", "المتصوّرة المنجلية"),
    S("Trypanosoma gambiense", "المثقبية الغامبية"), S("Trichomonas vaginalis", "المشعرة المهبلية"),
    S("Diphyllobothrium latum", "الشريطية العريضة")], "C"),

 Q("Each of the following statements concerning sleeping sickness is correct except:",
   "كل عبارة مما يأتي عن داء النوم صحيحة ما عدا:",
   [["Sleeping sickness is caused by trypanosome", "يسبّب داء النوم المثقبيات"],
    ["Sleeping sickness occur primarily in tropical Africa", "يحدث داء النوم أساسًا في إفريقيا المدارية"],
    ["Sleeping sickness can be diagnosed by finding eggs in the stool", "يُشخَّص داء النوم بإيجاد بيوض في البراز"],
    ["Sleeping sickness is transmitted by tsetse flies", "ينتقل داء النوم بذباب تسي تسي"],
    ["All false", "جميعها خاطئة"]], "C"),

 Q("Chaga’s disease can be diagnosed by:", "يمكن تشخيص داء شاغاس بـ:",
   [["Xenodiagnosis", "التشخيص بالعائل (Xenodiagnosis)"], ["Thymol turbidity test", "فحص عكارة الثيمول"],
    ["Casoni’s test", "فحص كازوني"], ["Mercuric chloride", "كلوريد الزئبق"], ["Enterotest", "فحص الخيط المعوي (Enterotest)"]], "A"),

 Q("Chagas disease that is prevalent in Latin America is caused by:",
   "داء شاغاس المنتشر في أمريكا اللاتينية يسبّبه:",
   [Tc(), S("Trypanosome brucei", "المثقبية البروسية"), S("L. brazilience", "الليشمانيا البرازيلية"),
    S("Toxoplasma", "المقوّسة"), NONE], "A"),

 Q("Trypasnosoma cruzi cause ------ in humans:", "تسبّب المثقبية الكروزية ------ في الإنسان:",
   [["Chronic African trypanosomiasis", "داء المثقبيات الإفريقي المزمن"], ["Chagas disease", "داء شاغاس"],
    ["Leishmaniasis", "داء الليشمانيات"], ["Visceral leishmaniasis", "داء الليشمانيات الحشوي"],
    ["East African sleeping sickness", "داء النوم الإفريقي الشرقي"]], "B"),

 Q("Which of the following species is not injected through the bite of mouthparts of the insect vector?",
   "أيُّ الأنواع الآتية لا يُحقن عبر لسعة أجزاء فم الحشرة الناقلة؟",
   [Tb(), Tc(), S("Leishmania donovani", "الليشمانيا الدونوفانية"),
    S("Trypanosoma rhodesiense", "المثقبية الروديسية"), S("Trypanosoma evansi", "مثقبية إيفانس")], "B"),

 Q("Peripheral blood smear examination is useful in diagnosis of:",
   "فحص لطاخة الدم المحيطي مفيد في تشخيص:",
   [["Trypanosoma", "المثقبيات"], ["Leishmania", "الليشمانيا"], ["Malaria", "الملاريا"],
    ["All", "جميعها"], ["B and C", "B و C"]], "D"),

 Q("Biological vector of sleeping sickness is:", "الناقل البيولوجي لداء النوم هو:",
   [["Tsetse fly", "ذبابة تسي تسي"], ["Horse fly", "ذبابة الخيل"], ["House fly", "الذبابة المنزلية"],
    ["Mosquitoes", "البعوض"], NONE], "A"),

 Q("Which of the following is exclusively an intracellular parasite in the definitive host?",
   "أيُّ ما يأتي طفيلي داخل خلوي حصريًّا في العائل النهائي؟",
   [["Cutaneous leishmaniasis", "داء الليشمانيات الجلدي"], ["African trypanosomiasis", "داء المثقبيات الإفريقي"],
    ["Visceral leishmaniasis", "داء الليشمانيات الحشوي"], ["A, B and C", "A و B و C"], ["A and C", "A و C"]], "E"),

 Q("In Trypanosoma cruzi life cycle:", "في دورة حياة المثقبية الكروزية:",
   [["The parasites differentiate into infective metacyclic epimastigotes in the foregut",
     "تتمايز الطفيليات إلى أطوار فوق سوطية استحالية مُعدية في المعي الأمامي"],
    ["The parasites differentiate into infective metacyclic amastigote in the hindgut",
     "تتمايز الطفيليات إلى طور عديم السوط استحالي مُعدٍ في المعي الخلفي"],
    ["The parasites differentiated into infective metacyclic trypomastigote in the foregut",
     "تتمايز الطفيليات إلى طور مثقبي استحالي مُعدٍ في المعي الأمامي"],
    ["The parasite differentiated into infective metacyclic promastigote in the hindgut",
     "يتمايز الطفيلي إلى طور أمامي السوط استحالي مُعدٍ في المعي الخلفي"],
    ["The parasite differentiated into infective metacyclic trypomastigote in the hind gut",
     "يتمايز الطفيلي إلى طور مثقبي استحالي مُعدٍ في المعي الخلفي"]], "E"),

 Q("The infective stage for both of Trypanosoma cruzi and T. brucei is:",
   "الطور المُعدي لكلٍّ من المثقبية الكروزية والمثقبية البروسية هو:",
   [["Metacyclic promastigote", "الطور أمامي السوط الاستحالي"], ["Metacyclic amastigote", "الطور عديم السوط الاستحالي"],
    ["Metacyclic trypomastigotes", "الأطوار المثقبية الاستحالية"], ["Metacyclic epimastigote", "الطور فوق السوطي الاستحالي"],
    ALL], "C"),

 Q("Trypanosoma gambienze:", "المثقبية الغامبية:",
   [["Present in Iraq", "موجودة في العراق"], ["Sand fly is the vector", "ذبابة الرمل هي الناقل"],
    ["Cause ASS", "تسبّب داء النوم الإفريقي (ASS)"], ["Intracellular protozoa", "أوالٍ داخل خلوية"],
    ["Trophozoite contains blood", "الطور المتحرّك يحتوي دمًا"]], "C"),

 Q("Glossina spp. (Tsetse fly) is the vector that transport:", "جنس Glossina (ذبابة تسي تسي) هو الناقل الذي ينقل:",
   [S("Trichomonas vaginalis", "المشعرة المهبلية"), S("Trypanosoma brucei gambiense", "المثقبية البروسية الغامبية"),
    S("Leishmania donovani", "الليشمانيا الدونوفانية"), S("Toxoplasma gondii", "المقوّسة الغوندية"),
    ["Plasmodium spp", "أنواع المتصوّرات (Plasmodium spp)"]], "B"),
]

n = sum(1 for q in mcq if "topic_en" not in q)
from collections import Counter
cnt = Counter(q.get("answer") for q in mcq if "topic_en" not in q)
notes = sum(1 for q in mcq if "note_en" in q)
print("questions:", n, "| answers:", dict(cnt), "| notes:", notes)

meta = {
 "subject_en": "Diagnostic Parasitology", "subject_ar": "الطفيليات التشخيصية",
 "instructor": "أ.د. نزار الخفاجي",
 "unit_en": "Week 8", "unit_ar": "الأسبوع 8", "unit_label": "WEEK", "unit_no": "8",
 "title_en": "Tissue Flagellates: Trypanosoma",
 "title_ar": "السوطيات النسيجية: المثقبيات (Trypanosoma)",
 "department": "قسم التحليلات", "stage": "The fourth stage — الرابعة",
 "kind": "Theory — نظري", "questions_kind": "MCQ — أسئلة اختيار",
 "file_name": "BIOS - طفيليات نظري الأسبوع الثامن - الأسئلة",
 "short_ar": "طفيليات",
}
questions = {
 "title_en": meta["title_en"], "title_ar": meta["title_ar"],
 "sub": "MCQ", "answers_inline": True,
 "mcq_en": "MCQ — 1st semester, week 8", "mcq_ar": "أسئلة الاختيار — الفصل الأول، الأسبوع الثامن",
 "intro_en": ["Q. Select the most correct answer from the followings",
              "The answer under each question is the one marked in the source file, kept as it is; a BIOS note flags any answer that is unsolved, doubtful or wrong."],
 "intro_ar": ["س. اختر الإجابة الأصح مما يأتي",
              "الحل تحت كل سؤال هو المؤشَّر في الملف الأصلي كما هو؛ وملاحظة BIOS تنبّه على أي سؤال غير محلول أو حلّه مشكوك فيه أو خاطئ."],
 "mcq": ltr_all(mcq),
}
out = "/home/user/-/parasitology-week8-mcq/lecture.json"
os.makedirs(os.path.dirname(out), exist_ok=True)
json.dump({"meta": meta, "questions": questions}, open(out, "w"), ensure_ascii=False, indent=1)
print("wrote", out)
