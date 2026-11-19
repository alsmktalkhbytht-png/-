import sys, os, json
WORK = "/tmp/claude-0/-home-user/8d90b83d-8398-5b0c-8a4a-924e1daeb159/scratchpad/work"
sys.path.insert(0, WORK)
from bidi import ltr_all

def Q(en, ar, opts, ans, note=None):
    d = {"en": en, "ar": ar, "options": opts, "answer": ans}
    if note:
        d["note_en"], d["note_ar"] = note
    return d

def T(en, ar):
    return {"topic_en": en, "topic_ar": ar}

def S(latin, ar):
    return ["__%s__" % latin, ar]

ALL  = ["All of the above", "جميع ما سبق"]
ALLt = ["All of them", "جميعها"]
NONE = ["None of the above", "لا شيء مما سبق"]
NONEt = ["None of these", "لا شيء من هذه"]
NONEb = ["None", "لا شيء"]

def GL(): return S("Giardia lamblia", "الجيارديا اللمبلية")
def TV(): return S("Trichomonas vaginalis", "المشعرة المهبلية")

mcq = [
 T("Giardia lamblia", "الجيارديا اللمبلية (Giardia lamblia)"),

 Q("Motility by flagella:", "الحركة بالأسواط:",
   [GL(), S("E. histolytica", "الأميبا الحالّة للنسيج"), S("Entamoeba coli", "الأميبا القولونية"),
    S("Endolimax nana", "الأميبا القزمة"), S("E. gingivalis", "الأميبا اللثوية")], "A"),

 Q("Motility by flagella:", "الحركة بالأسواط:",
   [GL(), S("E. histolytica", "الأميبا الحالّة للنسيج"), S("Taenia solium", "الشريطية المسلّحة"),
    S("Toxoplasma gondii", "المقوّسة الغوندية"), S("Taenia saginata", "الشريطية العزلاء")], "A"),

 Q("Motility by flagella:", "الحركة بالأسواط:",
   [GL(), S("Toxoplasma gondii", "المقوّسة الغوندية"), S("Entamoeba histolytica", "الأميبا الحالّة للنسيج"),
    S("Balantidium coli", "البالانتيدية القولونية"), S("Entamoeba coli", "الأميبا القولونية")], "A"),

 Q("The most common site for Giardia lamblia is:", "الموضع الأكثر شيوعًا للجيارديا اللمبلية هو:",
   [["Rectum", "المستقيم"], ["Duodenum", "الاثنا عشري"], ["Gall bladder", "المرارة"],
    ["Caecum", "الأعور"], ["Blood", "الدم"]], "B"),

 Q("The dwelling of Giardia lamblia is:", "مسكن الجيارديا اللمبلية هو:",
   [["RBCs", "كريات الدم الحمراء"], ["Caecum", "الأعور"], ["Rectum", "المستقيم"],
    ["Duodenum", "الاثنا عشري"], ["Liver", "الكبد"]], "D"),

 Q("Normal reside of Giardia lamblia is:", "المسكن الطبيعي للجيارديا اللمبلية هو:",
   [["Bladder", "المثانة"], ["Colon", "القولون"], ["Urethra", "الإحليل"], ["Caecum", "الأعور"],
    ["Duodenum and upper Jejunum", "الاثنا عشري وأعلى الصائم"]], "E"),

 Q("Giardia lamblia is considered as:", "تُعدّ الجيارديا اللمبلية:",
   [["Intestinal flagellate", "سوطيًّا معويًّا"], ["Genital flagellate", "سوطيًّا تناسليًّا"],
    ["Oral; flagellate", "سوطيًّا فمويًّا"], ["Hemoflagelate", "سوطيًّا دمويًّا"], NONEt], "A"),

 Q("The habitat of Giardia lamblia is:", "موطن الجيارديا اللمبلية هو:",
   [["RBC", "كريات الدم الحمراء"], ["Small intestine", "الأمعاء الدقيقة"], ["WBC", "كريات الدم البيضاء"],
    ["Liver", "الكبد"], ALL], "B"),

 Q("The habitat is the small intestine:", "الموطن هو الأمعاء الدقيقة:",
   [S("Entamoeba coli", "الأميبا القولونية"), GL(), S("Entamoeba histolytica", "الأميبا الحالّة للنسيج"),
    ["A and B", "A و B"], ["A, B and C", "A و B و C"]], "B"),

 Q("Watery diarrhea disease caused by:", "مرض الإسهال المائي يسبّبه:",
   [GL(), S("Toxoplasma gondii", "المقوّسة الغوندية"), S("E. histolytica", "الأميبا الحالّة للنسيج"),
    S("Plasmodium malaria", "متصوّرة الملاريا"), NONE], "A"),

 Q("Watery diarrhea is clinical feature of:", "الإسهال المائي علامة سريرية لـ:",
   [S("E. histolytica", "الأميبا الحالّة للنسيج"), S("Dientamoeba fragilis", "ثنائية الأميبا الهشّة"),
    S("E. gingivalis", "الأميبا اللثوية"), GL(), S("Trichomonas hominis", "المشعرة البشرية")], "D"),

 Q("The following is true of giardiasis… except:", "ما يأتي صحيح عن داء الجيارديا … ما عدا:",
   [["Cause acute watery diarrhea", "تسبّب إسهالًا مائيًّا حادًّا"],
    ["Duodenum and jejunum are the prime sites of dwelling", "الاثنا عشري والصائم هما الموضعان الرئيسان للسكن"],
    ["Cause bloody diarrhea", "تسبّب إسهالًا دمويًّا"],
    ["Cause steatorrhea", "تسبّب الإسهال الدهني"],
    ["Cause foul smelling stool", "تسبّب برازًا كريه الرائحة"]], "C"),

 Q("Giardia lamblia:", "الجيارديا اللمبلية:",
   [["Cause steatorrhea in patients", "تسبّب الإسهال الدهني لدى المرضى"],
    ["Trophozoite with 1 nucleus", "طور متحرّك بنواة واحدة"], ["Blood", "الدم"],
    ["One of symptom is Leuopenia", "من أعراضها قلّة الكريات البيض"], ["Reside in colon", "تسكن القولون"]], "A"),

 Q("Which one of following test is used for diagnosis of Giardia blamblia infections:",
   "أيُّ الفحوص الآتية يُستعمل لتشخيص عدوى الجيارديا اللمبلية:",
   [["Enterotest", "فحص الخيط المعوي (Enterotest)"], ["Cassein's test", "فحص كاسين"],
    ["ParaSight F test", "فحص ParaSight F"], ["Napier's test", "فحص نابير"], ALLt], "A"),

 Q("Each of the following statement concerning Giardia lamblia is correct except:",
   "كل عبارة مما يأتي عن الجيارديا اللمبلية صحيحة ما عدا:",
   [["G. lamblia has both a trophozoite and cyst stage in its life cycle",
     "للجيارديا طوران: المتحرّك والكيس في دورة حياتها"],
    ["G. lamblia is transmitted by the fecal – oral route", "تنتقل الجيارديا بالطريق البرازي – الفموي"],
    ["G. lamblia causes hemolytic anemia", "تسبّب الجيارديا فقر دم انحلالي"],
    ["G. lamblia can be diagnosed by serodiagnosis through enzyme – linked immunosorbent assay",
     "يمكن تشخيص الجيارديا مصليًّا بمقايسة الممتز المناعي المرتبط بالإنزيم (ELISA)"],
    ["G. lamblia infection may lead to steatorrhea", "قد تؤدّي عدوى الجيارديا إلى الإسهال الدهني"]], "C"),

 Q("Which is incorrect in the following statements regarding Giardia lamblia:",
   "أيُّ العبارات الآتية غير صحيح بخصوص الجيارديا اللمبلية:",
   [["Cysts remain viable in soil only for several weeks", "تبقى الأكياس حيّة في التربة فقط لأسابيع عدّة"],
    ["Trophozoite remain viable in soil and water for several months", "يبقى الطور المتحرّك حيًّا في التربة والماء أشهرًا عدّة"],
    ["Cysts remain viable in water only for several months", "تبقى الأكياس حيّة في الماء فقط لأشهر عدّة"],
    ["Cysts remain viable in soil and water for several days", "تبقى الأكياس حيّة في التربة والماء لأيّام عدّة"],
    ["Cysts remain viable in soil and water for several months", "تبقى الأكياس حيّة في التربة والماء لأشهر عدّة"]], "E"),

 Q("Which of the following is correct regarding Giardia lamblia life cycle:",
   "أيُّ ما يأتي صحيح بخصوص دورة حياة الجيارديا اللمبلية:",
   [["Giardia trophozoites only can be found in the stool of infected person and may be observed microscopically to diagnose giardiasis",
     "تُوجد الأطوار المتحرّكة فقط في براز المصاب وتُرى مجهريًّا لتشخيص الداء"],
    ["Giardia cysts and trophozoites can be found in the stool of infected person and may be observed macroscopically to diagnose giardiasis",
     "تُوجد الأكياس والأطوار المتحرّكة في براز المصاب وتُرى عِيانيًّا (بالعين) لتشخيص الداء"],
    ["Giardia cysts and trophozoites can be found in the stool of infected person and may be observed microscopically to diagnose giardiasis",
     "تُوجد الأكياس والأطوار المتحرّكة في براز المصاب وتُرى مجهريًّا لتشخيص الداء"],
    ["Giardia cysts only can be found in the stool of infected person and may be observed microscopically to diagnose giardiasis",
     "تُوجد الأكياس فقط في براز المصاب وتُرى مجهريًّا لتشخيص الداء"],
    ["Giardia cysts and trophozoites can be found in the stool of infected person and may be observed microscopically for giardiasis treatment",
     "تُوجد الأكياس والأطوار المتحرّكة في براز المصاب وتُرى مجهريًّا لعلاج الداء"]], "C"),

 Q("The suitable description for the cyst of Giardia lamblia is:",
   "الوصف المناسب لكيس الجيارديا اللمبلية هو:",
   [["With rigid envelope and four nuclei distributed across the cytoplasm",
     "بغلاف صلب وأربع أنوية موزّعة في السيتوبلازم"],
    ["With membranous envelope and four nuclei grouped at one pole of the cell",
     "بغلاف غشائي وأربع أنوية مجتمعة عند أحد قطبي الخلية"],
    ["With rigid envelope and four nuclei grouped at one pole of the cell",
     "بغلاف صلب وأربع أنوية مجتمعة عند أحد قطبي الخلية"],
    ["With membranous envelope and four nuclei distributed across the cytoplasm",
     "بغلاف غشائي وأربع أنوية موزّعة في السيتوبلازم"],
    ["With rigid envelope and four nuclei each two of them are grouped at one of the poles of the cell",
     "بغلاف صلب وأربع أنوية كل نواتين منها مجتمعتان عند أحد قطبي الخلية"]], "C"),

 Q("Trophozoite of Giardia lamblia has:", "الطور المتحرّك للجيارديا اللمبلية له:",
   [["2 flagella", "سوطان"], ["4 flagella", "أربعة أسواط"], ["6 flagella", "ستة أسواط"],
    ["8 flagella", "ثمانية أسواط"], ["Aflagellate, No flagella", "بلا أسواط"]], "D"),

 Q("Giardia trophozoites contains:", "تحتوي الأطوار المتحرّكة للجيارديا على:",
   [["One nucleus", "نواة واحدة"], ["Two nuclei", "نواتان"], ["Three nuclei", "ثلاث أنوية"],
    ["Four nuclei", "أربع أنوية"], ["8 nuclei", "ثماني أنوية"]], "B"),

 Q("Trophozoite of Giardia lamblia has:", "الطور المتحرّك للجيارديا اللمبلية له:",
   [["1 nucleus", "نواة واحدة"], ["2 nuclei", "نواتان"], ["4 nuclei", "أربع أنوية"],
    ["6 nuclei", "ست أنوية"], ["8 nuclei", "ثماني أنوية"]], "B"),

 Q("Giardia lamblia has:", "الجيارديا اللمبلية لها:",
   [["Promastigote", "طور أمامي السوط (Promastigote)"], ["Pseudopodia", "أقدام كاذبة"],
    ["Amastigote", "طور عديم السوط (Amastigote)"], ["Four pairs of flagella", "أربعة أزواج من الأسواط"],
    ["Cilia", "أهداب"]], "D"),

 Q("Giardia lamblia has:", "الجيارديا اللمبلية لها:",
   [["Four pairs of flagella", "أربعة أزواج من الأسواط"], ["Pseudopodia", "أقدام كاذبة"],
    ["One flagellum", "سوط واحد"], ["Two flagella", "سوطان"], NONEb], "A"),

 Q("The characteristic feature of Giardia lamblia infection in human is:",
   "السمة المميّزة لعدوى الجيارديا اللمبلية في الإنسان هي:",
   [["Urithritis", "التهاب الإحليل"], ["Prostitis", "التهاب البروستات"], ["Steatorrhea", "الإسهال الدهني"],
    ["Cervicitis", "التهاب عنق الرحم"], ["Vaginalis", "التهاب المهبل"]], "C"),

 Q("All of the statement are correct except:", "كل العبارات صحيحة ما عدا:",
   [["Trichomonas vaginalis is with four free flagella", "المشعرة المهبلية لها أربعة أسواط حرّة"],
    ["Dientamoeba fragilis is binucleated and without cyst stage",
     "ثنائية الأميبا الهشّة ثنائية النواة وبلا طور كيسي"],
    ["The cyst of Chilomastix mesnilli is lemon-shaped", "كيس الكيلوماستكس المنيلي ليموني الشكل"],
    ["In giardia infection, the stool contains fat and mucus without blood",
     "في عدوى الجيارديا يحتوي البراز على دهن ومخاط بلا دم"],
    ["Giardia trophozoites multiply and reside in the last part of the small intestine",
     "تتكاثر أطوار الجيارديا المتحرّكة وتسكن في الجزء الأخير من الأمعاء الدقيقة"]], "E"),

 Q("Which of the following is not correctly matched:", "أيُّ ما يأتي غير متطابق بصورة صحيحة:",
   [["Giardia lamblia : Steatorrhea", "الجيارديا اللمبلية: الإسهال الدهني"],
    ["Chilomastix mesnilli : trophozoite with 3 anterior flagella",
     "الكيلوماستكس المنيلي: طور متحرّك بثلاثة أسواط أمامية"],
    ["Dientamoeba fragilis: infection is of low pathogenicity causes gastrointestinal (GI) disease",
     "ثنائية الأميبا الهشّة: العدوى ضعيفة الإمراض تسبّب داءً معديًّا معويًّا"],
    ["Trichomonas vaginalis : parasite’s secretions decrease the pH of vaginal fluid",
     "المشعرة المهبلية: إفرازات الطفيلي تخفض الأس الهيدروجيني لسائل المهبل"],
    ["Trichomonas tenax : the organism with five free anterior flagella",
     "المشعرة الفموية (tenax): الكائن ذو خمسة أسواط أمامية حرّة"]], "E"),

 Q("The mature cyst, is infective stage of:", "الكيس الناضج هو الطور المُعدي لـ:",
   [GL(), S("Leishmania tropica", "الليشمانيا المدارية"), S("Plasmodium malaria", "متصوّرة الملاريا"),
    S("Diphyllobothrium latum", "الشريطية العريضة"), S("Trichinella spiralis", "الشعرينة الحلزونية")], "A",
   ("The trailing “formalin…” text in the source is from a text box of another topic (specimen preservatives) that overlapped this page; it is not part of this question.",
    "النصّ اللاحق «formalin…» في الملف من مربّع نصٍّ لموضوع آخر (حافظات العيّنات) تداخل على الصفحة، وليس جزءًا من هذا السؤال.")),

 # Q28 in the source is a corrupted layout artifact (fragments of a formalin/preservative text box
 # with no stem and no marked answer) — omitted. Reported to the user.

 T("Trichomonas vaginalis", "المشعرة المهبلية (Trichomonas vaginalis)"),

 Q("All of the following lead to bloody diarrhea except:", "كل ما يأتي يؤدّي إلى إسهال دموي ما عدا:",
   [S("Schistosoma japonicum", "البلهارسيا اليابانية"), S("Entamoeba histolytica", "الأميبا الحالّة للنسيج"),
    S("Cryptosporidium", "الخفيّات (Cryptosporidium)"), S("T. Vaginalis", "المشعرة المهبلية"), ALL], "D",
   ("Cryptosporidium (C) also does not cause bloody diarrhea (it causes watery diarrhea); the source marks T. vaginalis (D), which is correct as it is not an intestinal parasite at all.",
    "الخفيّات (C) أيضًا لا تسبّب إسهالًا دمويًّا (تسبّب إسهالًا مائيًّا)؛ والمصدر يحدّد المشعرة المهبلية (D)، وهو جواب سليم لأنها ليست طفيليًّا معويًّا أصلًا.")),

 Q("The specimen for the diagnosis of Trichomonas vaginalis infection in female:",
   "العيّنة لتشخيص عدوى المشعرة المهبلية في الأنثى:",
   [["Blood", "الدم"], ["Vaginal discharge", "الإفراز المهبلي"], ["Stool", "البراز"],
    ["Saliva", "اللعاب"], ["Urine", "الإدرار"]], "B"),

 Q("The specimen for the diagnosis of Trichomonas vaginalis infection in female:",
   "العيّنة لتشخيص عدوى المشعرة المهبلية في الأنثى:",
   [["Prostatic secretions", "إفرازات البروستات"], ["Vaginal discharges", "الإفرازات المهبلية"],
    ["Urine", "الإدرار"], ["B and C", "B و C"], ["A and B", "A و B"]], "D"),

 Q("The specimen for the diagnosis of Trichomonas vaginalis infection in female:",
   "العيّنة لتشخيص عدوى المشعرة المهبلية في الأنثى:",
   [["Blood", "الدم"], ["Vaginal discharge", "الإفراز المهبلي"], ["Stool", "البراز"],
    ["Saliva", "اللعاب"], ["Sputum", "القشع"]], "B"),

 Q("The specimen for the diagnosis of Trichomonas vaginalis infection in women:",
   "العيّنة لتشخيص عدوى المشعرة المهبلية في النساء:",
   [["Gland secretion", "إفراز الغدّة"], ["Vaginal discharge", "الإفراز المهبلي"], ["Stool", "البراز"],
    ["Urine", "الإدرار"], ALLt], "B"),

 Q("The specimen for the diagnosis of Trichomonas vaginalis infection in women:",
   "العيّنة لتشخيص عدوى المشعرة المهبلية في النساء:",
   [["Gland secretion", "إفراز الغدّة"], ["Vaginal discharge", "الإفراز المهبلي"], ["Stool", "البراز"],
    ["Sputum", "القشع"], ALLt], "B"),

 Q("Trichomonas vaginalis is found in:", "تُوجد المشعرة المهبلية في:",
   [["Urethra of male", "إحليل الذكر"], ["Vagina of female", "مهبل الأنثى"], ["Gum", "اللثة"],
    ["Intestine", "الأمعاء"], ["A and B", "A و B"]], "E"),

 Q("Trichomonas vaginalis:", "المشعرة المهبلية:",
   [["Has pseudopodia", "لها أقدام كاذبة"], ["Nonpathogenic protozoa", "أوالٍ غير ممرضة"],
    ["Cause steatorrhea", "تسبّب الإسهال الدهني"], ["Find in human intestine", "تُوجد في أمعاء الإنسان"],
    ["Cause Vaginitis and Urethritis", "تسبّب التهاب المهبل والإحليل"]], "E"),

 Q("A women suffering from cervicitis (“strawberry” cervix), Urethritis, Discomfort during urination, itching, yellow to green discharge, Based on what criteria, Diagnosis is:",
   "امرأة تعاني التهاب عنق الرحم (عنق «الفراولة») والتهاب الإحليل وانزعاجًا أثناء التبوّل وحكّة وإفرازًا أصفر إلى أخضر، بناءً على هذه المعايير، التشخيص هو:",
   [S("Toxoplasma gondii", "المقوّسة الغوندية"), TV(), S("Leishmania donovani", "الليشمانيا الدونوفانية"),
    GL(), S("Leishmania tropica", "الليشمانيا المدارية")], "B"),

 Q("The correct higher classification of flagellates is:", "التصنيف الأعلى الصحيح للسوطيات هو:",
   [["Kingdom Protista. Subkingdom Protozoa, Phylum Sarcomastigophora, Class Mastigophora",
     "مملكة الطلائعيات، تحت مملكة الأوالي، شُعبة Sarcomastigophora، صف Mastigophora"],
    ["Domain Protista, Subkingdom Protozoa, Phylum Sarcomastigophora, Subphylum Mastigophora",
     "نطاق الطلائعيات، تحت مملكة الأوالي، شُعبة Sarcomastigophora، تحت شُعبة Mastigophora"],
    ["Kingdom Protista, Order Protozoa, Phylum Sarcomastigophora, Subphylum Mastigophora",
     "مملكة الطلائعيات، رتبة الأوالي، شُعبة Sarcomastigophora، تحت شُعبة Mastigophora"],
    ["Kingdom Protista, Subkingdom Protozoa, Phylum Sarcomastigophora, Subphylum, Mastigophora",
     "مملكة الطلائعيات، تحت مملكة الأوالي، شُعبة Sarcomastigophora، تحت شُعبة Mastigophora"],
    ["Kingdom Protista, Class Protozoa, Phylum Sarcomastigophora, Subphylum Mastigophora",
     "مملكة الطلائعيات، صف الأوالي، شُعبة Sarcomastigophora، تحت شُعبة Mastigophora"]], "B",
   ("The source marks B, but it says “Domain Protista”; Protista is a kingdom, not a domain. The scientifically correct hierarchy (Kingdom Protista → Subkingdom Protozoa → Phylum Sarcomastigophora → Subphylum Mastigophora) is option D.",
    "المصدر يحدّد B لكنه يقول «نطاق الطلائعيات»؛ والطلائعيات مملكة لا نطاق. والتسلسل الصحيح علميًّا (مملكة الطلائعيات ← تحت مملكة الأوالي ← شُعبة Sarcomastigophora ← تحت شُعبة Mastigophora) هو الخيار D.")),

 Q("Flagellates are characterized by all of the following except:",
   "تتّصف السوطيات بكل ما يأتي ما عدا:",
   [["Presence of flagella that are used for locomotion", "وجود أسواط تُستعمل للحركة"],
    ["Some of them have a single flagellum while others have more", "بعضها بسوط واحد وبعضها بأكثر"],
    ["There is one nucleus per cell in all species of flagellates", "يوجد نواة واحدة لكل خلية في جميع أنواع السوطيات"],
    ["Flagellates do not display sexual reproduction", "لا تُبدي السوطيات تكاثرًا جنسيًّا"],
    ["If there is more than one nucleus, they are all similar", "إن وُجد أكثر من نواة فجميعها متشابهة"]], "C"),

 Q("Choose the correct description for the trophozoite of Giardia lamblia:",
   "اختر الوصف الصحيح للطور المتحرّك للجيارديا اللمبلية:",
   [["Pyriform, binucleated, convex dorsally and concave ventrally with sucking disc helps in attachment to the hepatic mucosa",
     "كمثري الشكل، ثنائي النواة، محدّب ظهريًّا مقعّر بطنيًّا بقرص ماصّ يساعد على الالتصاق بمخاطية الكبد"],
    ["Pyriform, uninucleated, convex dorsally and concave ventrally with sucking disc helps in attachment to the intestinal mucosa",
     "كمثري، وحيد النواة، محدّب ظهريًّا مقعّر بطنيًّا بقرص ماصّ يساعد على الالتصاق بالمخاطية المعوية"],
    ["Pyriform, binucleated, concave dorsally and convex ventrally with sucking disc helps in attachment to the intestinal mucosa",
     "كمثري، ثنائي النواة، مقعّر ظهريًّا محدّب بطنيًّا بقرص ماصّ يساعد على الالتصاق بالمخاطية المعوية"],
    ["Pyriform, binucleated, convex dorsally and concave ventrally with sucking disc helps in attachment to the intestinal submucosa",
     "كمثري، ثنائي النواة، محدّب ظهريًّا مقعّر بطنيًّا بقرص ماصّ يساعد على الالتصاق بتحت المخاطية المعوية"],
    ["Pyriform, binucleated, convex dorsally and concave ventrally with sucking disc helps in attachment to the intestinal mucosa",
     "كمثري، ثنائي النواة، محدّب ظهريًّا مقعّر بطنيًّا بقرص ماصّ يساعد على الالتصاق بالمخاطية المعوية"]], "E"),

 Q("Trophozoite of Giardia lamblia is:", "الطور المتحرّك للجيارديا اللمبلية هو:",
   [["Pyriform, uninucleated, convex dorsally and concave ventrally with sucking disc helps in attachment to the intestinal submucosa",
     "كمثري، وحيد النواة، محدّب ظهريًّا مقعّر بطنيًّا بقرص ماصّ يساعد على الالتصاق بتحت المخاطية المعوية"],
    ["Pyriform, binucleated, convex dorsally and concave ventrally with sucking disc helps in attachment to the intestinal mucosa",
     "كمثري، ثنائي النواة، محدّب ظهريًّا مقعّر بطنيًّا بقرص ماصّ يساعد على الالتصاق بالمخاطية المعوية"],
    ["Pyriform, uninucleatd, convex ventrally and concave dorsally with sucking disc helps in attachment to the intestinal mucosa",
     "كمثري، وحيد النواة، محدّب بطنيًّا مقعّر ظهريًّا بقرص ماصّ يساعد على الالتصاق بالمخاطية المعوية"],
    ["Pyriform, uninucleated, convex dorsally and concave ventrally with sucking disc helps in attachment to the intestinal mucosa",
     "كمثري، وحيد النواة، محدّب ظهريًّا مقعّر بطنيًّا بقرص ماصّ يساعد على الالتصاق بالمخاطية المعوية"],
    ["Pyriform, binucleated, convex dorsally and concave ventrally with sucking disc helps in attachment to the intestinal submucosa",
     "كمثري، ثنائي النواة، محدّب ظهريًّا مقعّر بطنيًّا بقرص ماصّ يساعد على الالتصاق بتحت المخاطية المعوية"]], "B"),

 Q("Which of the following statements is correct:", "أيُّ العبارات الآتية صحيحة:",
   [["Lumen dwelling flagellates: living in the urogenital tract (Giardia) and alimentary tract (Trichomonas).",
     "السوطيات ساكنة اللمعة: تعيش في السبيل البولي التناسلي (الجيارديا) والسبيل الهضمي (المشعرة)"],
    ["Hemoflagellates: Living in blood (Leishmania) and tissue (Trypanosoma)",
     "السوطيات الدموية: تعيش في الدم (الليشمانيا) والنسيج (المثقبيات)"],
    ["Lumen dwelling flagellates: Living in tissues (Leishmania) and blood (Trypanosoma)",
     "السوطيات ساكنة اللمعة: تعيش في الأنسجة (الليشمانيا) والدم (المثقبيات)"],
    ["Hemoflagellates: Living in the alimentary tract (Giardia) and urogenital tract (trichomonas)",
     "السوطيات الدموية: تعيش في السبيل الهضمي (الجيارديا) والسبيل البولي التناسلي (المشعرة)"]], "D",
   ("The source marks D, but it is wrong: hemoflagellates live in blood and tissue (Leishmania, Trypanosoma). The correct statement is B.",
    "المصدر يحدّد D لكنه خطأ: السوطيات الدموية تعيش في الدم والنسيج (الليشمانيا والمثقبيات). والعبارة الصحيحة هي B.")),

 Q("The main complication of Trichomonas vaginalis in women is:",
   "التعقيد الرئيس للمشعرة المهبلية في النساء هو:",
   [["Pruritic ani", "حكّة الشرج"], ["Pruritic vaginitis", "التهاب المهبل الحاكّ"],
    ["Pruritic papules", "حطاطات حاكّة"], ["Pruritic vulvae", "حكّة الفرج"],
    ["Pruritic folliculitis", "التهاب الجريبات الحاكّ"]], "B"),

 Q("Trichomoniasis is a disease caused by:", "داء المشعرات مرض يسبّبه:",
   [S("Trichomonas hominis", "المشعرة البشرية"), TV(), S("Trichomonas tenax", "المشعرة الفموية"),
    ALL, NONE], "B"),

 Q("Trichomoniasis is a disease caused by:", "داء المشعرات مرض يسبّبه:",
   [TV(), S("Entamoeba histolytica", "الأميبا الحالّة للنسيج"), GL(),
    S("Plasmodium malaria", "متصوّرة الملاريا"), S("Toxoplasma gondii", "المقوّسة الغوندية")], "A"),

 Q("The infective form of Trichomonas vaginalis is:", "الطور المُعدي للمشعرة المهبلية هو:",
   [["Epimastigote", "الطور فوق السوطي (Epimastigote)"], ["Promastigote", "الطور أمامي السوط (Promastigote)"],
    ["Trophozoite", "الطور المتحرّك (Trophozoite)"], ["Oocyst", "الكيس البيضي (Oocyst)"],
    ["Sporozoite", "البوغيّة (Sporozoite)"]], "C"),

 Q("The trophozoite is the infective stage in:", "الطور المتحرّك هو الطور المُعدي في:",
   [GL(), S("Entamoeba histolytica", "الأميبا الحالّة للنسيج"), TV(),
    S("Endolimax nana", "الأميبا القزمة"), S("Balantidium coli", "البالانتيدية القولونية")], "C"),

 Q("Motility of Trichomonas hominis is:", "حركة المشعرة البشرية هي:",
   [["Amoeboid", "أميبية"], ["Falling leaf like", "كسقوط الورقة"], ["Stately", "متمهّلة"],
    ["Jerky movement", "حركة ارتجاجية (متشنّجة)"], ["Rotary", "دورانية"]], "D"),

 Q("Clinical signs of cervicitis, urethritis is caused by:",
   "العلامات السريرية لالتهاب عنق الرحم والإحليل يسبّبها:",
   [S("E. histolytica", "الأميبا الحالّة للنسيج"), S("Trichomonas hominis", "المشعرة البشرية"),
    S("T. tenax", "المشعرة الفموية"), S("T. vaginalis", "المشعرة المهبلية"),
    S("E. coli", "الأميبا القولونية")], "D"),

 Q("The parasite that causing bad vaginal smell, burring, and itching sensation is:",
   "الطفيلي المسبّب لرائحة مهبلية كريهة وحُرقة وإحساس بالحكّة هو:",
   [GL(), TV(), S("E. histolytica", "الأميبا الحالّة للنسيج"),
    S("Entamoeba coli", "الأميبا القولونية"), S("E. gingivalis", "الأميبا اللثوية")], "B"),

 Q("Protozoan transmitted sexually is:", "الأوالي المنتقلة جنسيًّا هي:",
   [S("Entamoeba histolytica", "الأميبا الحالّة للنسيج"), GL(), TV(), ALL, NONEb], "C"),

 Q("Each of the following statements concerning Trichomonas vaginalis is correct except:",
   "كل عبارة مما يأتي عن المشعرة المهبلية صحيحة ما عدا:",
   [["T. vaginalis can be diagnosed by visualizing the trophozopite", "تُشخّص المشعرة المهبلية برؤية الطور المتحرّك"],
    ["T. vaginalis is transmitted sexually", "تنتقل المشعرة المهبلية جنسيًّا"],
    ["T. vaginalis causes bloody diarrhea", "تسبّب المشعرة المهبلية إسهالًا دمويًّا"],
    ["T. vaginalis can be treated effectively with metronidazole", "تُعالَج المشعرة المهبلية بفعّالية بالميترونيدازول"],
    NONE], "C"),

 Q("Each of the following statements concerning Trichomonas vaginalis is correct except:",
   "كل عبارة مما يأتي عن المشعرة المهبلية صحيحة ما عدا:",
   [["T. vaginalis is transmitted sexually", "تنتقل المشعرة المهبلية جنسيًّا"],
    ["T. vaginalis can be diagnosed by visualizing the trophozoite", "تُشخّص المشعرة المهبلية برؤية الطور المتحرّك"],
    ["T. vaginalis infection in men can be asymptomatic", "قد تكون عدوى المشعرة المهبلية في الرجال بلا أعراض"],
    ["T. vaginalis causes bloody diarrhea", "تسبّب المشعرة المهبلية إسهالًا دمويًّا"],
    ["T. vaginalis is pyriform shaped with 4 free anterior flagella", "المشعرة المهبلية كمثرية الشكل بأربعة أسواط أمامية حرّة"]], "D"),

 Q("Trichomonas vaginalis cause the following except:", "تسبّب المشعرة المهبلية ما يأتي ما عدا:",
   [["Steatorrhea", "الإسهال الدهني"], ["Prostitis", "التهاب البروستات"], ["Urethritis", "التهاب الإحليل"],
    ["Vaginitis", "التهاب المهبل"], ["Cervicitis", "التهاب عنق الرحم"]], "A"),

 Q("Trichomonas vaginalis:", "المشعرة المهبلية:",
   [["Has Pseudopodia", "لها أقدام كاذبة"], ["Nonpathogenic", "غير ممرضة"],
    ["Cause steatorrhea", "تسبّب الإسهال الدهني"], ["Has five flagella", "لها خمسة أسواط"],
    ["Reside in human intestine", "تسكن أمعاء الإنسان"]], "D"),

 Q("Trichomonas vaginalis is found in following except:", "تُوجد المشعرة المهبلية فيما يأتي ما عدا:",
   [["Male urethra", "إحليل الذكر"], ["Female urethra", "إحليل الأنثى"], ["Prostate", "البروستات"],
    ["Vagina", "المهبل"], ["Duodenum", "الاثنا عشري"]], "E"),

 Q("The diagnostic form of Trichomonas vaginalis is:", "الطور التشخيصي للمشعرة المهبلية هو:",
   [["Promastigote", "الطور أمامي السوط (Promastigote)"], ["Epimastigote", "الطور فوق السوطي (Epimastigote)"],
    ["Tachyzoite", "البوغيّة السريعة (Tachyzoite)"], ["Bradyzoite", "البوغيّة البطيئة (Bradyzoite)"],
    ["Trophozoite (Jerky movement )", "الطور المتحرّك (بحركة ارتجاجية)"]], "E"),

 Q("Trichomonas vaginalis habitat:", "موطن المشعرة المهبلية:",
   [["Brain", "الدماغ"], ["Lung", "الرئة"], ["Eye", "العين"],
    ["Blood , CSF, Lymph", "الدم والسائل الدماغي الشوكي واللمف"],
    ["Urogenital tract", "السبيل البولي التناسلي"]], "E"),
]

n = sum(1 for q in mcq if "topic_en" not in q)
from collections import Counter
cnt = Counter(q["answer"] for q in mcq if "answer" in q)
notes = sum(1 for q in mcq if "note_en" in q)
print("questions:", n, "| answer dist:", dict(cnt), "| notes:", notes)

meta = {
 "subject_en": "Diagnostic Parasitology", "subject_ar": "الطفيليات التشخيصية",
 "instructor": "أ.د. نزار الخفاجي",
 "unit_en": "Week 6–7", "unit_ar": "الأسبوعان 6 و7", "unit_label": "WEEK", "unit_no": "6–7",
 "title_en": "Intestinal, Oral & Genital Flagellates (Giardia, Trichomonas)",
 "title_ar": "السوطيات المعوية والفموية والتناسلية (الجيارديا والمشعرات)",
 "department": "قسم التحليلات", "stage": "The fourth stage — الرابعة",
 "kind": "Theory — نظري", "questions_kind": "MCQ — أسئلة اختيار",
 "file_name": "BIOS - طفيليات نظري الأسبوعان السادس والسابع - الأسئلة",
 "short_ar": "طفيليات",
}
questions = {
 "title_en": meta["title_en"], "title_ar": meta["title_ar"],
 "sub": "MCQ",
 "answers_inline": True,
 "mcq_en": "MCQ — 1st semester, weeks 6–7", "mcq_ar": "أسئلة الاختيار — الفصل الأول، الأسبوعان 6 و7",
 "intro_en": ["Q. Select the most correct answer from the followings",
              "The answer under each question is the one marked in the source file, kept as it is; a BIOS note flags any answer that is unsolved, doubtful or wrong."],
 "intro_ar": ["س. اختر الإجابة الأصح مما يأتي",
              "الحل تحت كل سؤال هو المؤشَّر في الملف الأصلي كما هو؛ وملاحظة BIOS تنبّه على أي سؤال غير محلول أو حلّه مشكوك فيه أو خاطئ."],
 "mcq": ltr_all(mcq),
}
out = "/home/user/-/parasitology-week6-7-mcq/lecture.json"
os.makedirs(os.path.dirname(out), exist_ok=True)
json.dump({"meta": meta, "questions": questions}, open(out, "w"), ensure_ascii=False, indent=1)
print("wrote", out)
