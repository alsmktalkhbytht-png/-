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
ALLt = ["All", "جميعها"]
ALLa = ["All of above", "جميع ما سبق"]
NONE = ["None of the above", "لا شيء مما سبق"]
NONEb = ["None", "لا شيء"]

# species
Ld = lambda: S("Leishmania donovani", "الليشمانيا الدونوفانية")
Lt = lambda: S("Leishmania tropica", "الليشمانيا المدارية")

# common stage options (bilingual)
EPI = ["Epimastigote", "فوق السوطي (Epimastigote)"]
AMA = ["Amastigote", "عديم السوط (Amastigote)"]
TRY = ["Trypomastigote", "المثقبي (Trypomastigote)"]
PRO = ["Promastigote", "أمامي السوط (Promastigote)"]
SAND = ["Sand fly", "ذبابة الرمل"]
SANDs = ["Sand flies", "ذباب الرمل"]

mcq = [
 T("Genus Leishmania", "جنس الليشمانيا (Leishmania)"),
 T("Properties of ideal vaccines, Leishmania vaccine in trial",
   "خصائص اللقاحات المثالية، ولقاح الليشمانيا قيد التجربة"),

 Q("Visceral leishmaniasis is also known as:", "داء الليشمانيات الحشوي يُعرف أيضًا بـ:",
   [["Kala-azar", "الكلازار"], ["Black fever", "الحمّى السوداء"], ["Dum dum fever", "حمّى دمدم"],
    ALLt, NONEb], "D"),

 Q("The causative agent of Kala azar is:", "العامل المسبّب للكلازار هو:",
   [Lt(), S("Leishmania major", "الليشمانيا الكبرى"), Ld(),
    S("Leishmania infantum", "الليشمانيا الطفلية"), S("Leishmania brazilliensis", "الليشمانيا البرازيلية")], "C"),

 Q("Leishmania donovani:", "الليشمانيا الدونوفانية:",
   [["Cause VL", "تسبّب داء الليشمانيات الحشوي (VL)"], ["Cause CL", "تسبّب داء الليشمانيات الجلدي (CL)"],
    ["Mosquito is the vector", "البعوض هو الناقل"], ["Baghdad boil", "حبّة بغداد"],
    ["Less pathogenic than Leishmania tropica", "أقل إمراضًا من الليشمانيا المدارية"]], "A"),

 Q("Leishmania tropica:", "الليشمانيا المدارية:",
   [["More dangerous than L. donovani", "أخطر من الليشمانيا الدونوفانية"],
    ["High spread than L. donovani", "أوسع انتشارًا من الليشمانيا الدونوفانية"],
    ["Enter host orally", "تدخل العائل فمويًّا"], ["Tick is the vector", "القُراد هو الناقل"],
    ["Find in children only", "تُوجد في الأطفال فقط"]], "B"),

 Q("Which of the following is the stage of Leishmania that is transmitted to humans by the vector?",
   "أيُّ ما يأتي هو طور الليشمانيا الذي ينقله الناقل إلى الإنسان؟",
   [EPI, AMA, TRY, PRO, ALL], "D"),

 Q("Among blood flagellates, the stage of development that has an undulating membrane, and a kinetoplast located posterior to the nucleus is the:",
   "من بين السوطيات الدموية، الطور الذي له غشاء متموّج وكينيتوبلاست خلف النواة هو:",
   [TRY, EPI, AMA, PRO, NONE], "A"),

 Q("Which of the following is exclusively an intracellular parasite in the definitive host?",
   "أيُّ ما يأتي طفيلي داخل خلوي حصريًّا في العائل النهائي؟",
   [S("Trypanosoma brucei", "المثقبية البروسية"), Ld(), S("Trichomonas vaginalis", "المشعرة المهبلية"),
    S("Entamoeba histolytica", "الأميبا الحالّة للنسيج"), S("Giardia lamblia", "الجيارديا اللمبلية")], "B"),

 Q("Leishmania sp. is transmitted to humans by the:", "تنتقل الليشمانيا إلى الإنسان بـ:",
   [SAND, ["Mosquito", "البعوض"], ["Kissing bug", "بقّة التقبيل"], ["Tsetse fly", "ذبابة تسي تسي"],
    ["House fly", "الذبابة المنزلية"]], "A"),

 Q("What is the major mode of Black fever transmission to humans?",
   "ما الطريقة الرئيسة لانتقال الحمّى السوداء إلى الإنسان؟",
   [["Bite of both sexes infected sand fly", "لسعة ذبابة الرمل المصابة من كلا الجنسين"],
    ["Bite of male infected mosquito", "لسعة البعوضة الذكر المصابة"],
    ["Bite of male infected sand fly", "لسعة ذبابة الرمل الذكر المصابة"],
    ["Bite of female infected mosquito", "لسعة البعوضة الأنثى المصابة"],
    ["Bite of female infected sand fly", "لسعة ذبابة الرمل الأنثى المصابة"]], "E"),

 Q("Which of the following cause Oriental sore?", "أيُّ ما يأتي يسبّب القرحة الشرقية؟",
   [Lt(), S("Leishmania major", "الليشمانيا الكبرى"), Ld(),
    S("Leishmania aethiopica", "الليشمانيا الحبشية"), S("Leishmania infantum", "الليشمانيا الطفلية")], "A"),

 Q("If someone has been infected with Leishmania tropica, what will you see under the microscope?",
   "إذا أُصيب شخص بالليشمانيا المدارية، فماذا سترى تحت المجهر؟",
   [TRY, AMA, PRO, EPI, ALL], "B"),

 Q("To diagnose cutaneous leishmaniasis:", "لتشخيص داء الليشمانيات الجلدي:",
   [["Vaginal swab", "مسحة مهبلية"], ["Biopsy better taken from underneath of ulcer", "خزعة يُفضّل أخذها من أسفل القرحة"],
    ["Bone marrow aspirates", "رشافات نقي العظم"], ["Stool", "البراز"], ALLa], "B"),

 Q("In which of the following pathogen, we can use skin test to follow-up with the patient?",
   "في أيٍّ من الممرضات الآتية يمكن استعمال الاختبار الجلدي لمتابعة المريض؟",
   [Ld(), S("Trypanosoma brucei", "المثقبية البروسية"), Lt(),
    S("Giardia lamblia", "الجيارديا اللمبلية"), S("Trichomonas tenax", "المشعرة الفموية")], "C"),

 Q("Leishmania sp. is transmitted to humans by:", "تنتقل الليشمانيا إلى الإنسان بـ:",
   [SAND, ["Mosquito", "البعوض"], ["Kissing bug", "بقّة التقبيل"], ["Tsetse fly", "ذبابة تسي تسي"],
    ["House fly", "الذبابة المنزلية"]], "A"),

 Q("Leishmania is transmitted by:", "تنتقل الليشمانيا بـ:",
   [SAND, ["Milk", "الحليب"], ["Sexually", "جنسيًّا"], ["Food and water", "الطعام والماء"], NONE], "A"),

 Q("Leishmania parasites are transmitted to human by:", "تنتقل طفيليات الليشمانيا إلى الإنسان بـ:",
   [["Tsetse", "ذبابة تسي تسي"], SANDs, ["Bug", "البقّة"], ["Mosquito", "البعوض"], ["Unknown", "غير معروف"]], "B"),

 Q("Leishmania parasite transmitted by the bite of:", "ينتقل طفيلي الليشمانيا بلسعة:",
   [["House fly", "الذبابة المنزلية"], ["Tsetse fly", "ذبابة تسي تسي"], SAND, ["Mosquitoes", "البعوض"], NONEb], "C"),

 Q("Leishmaniasis is:", "داء الليشمانيات هو:",
   [["Cutaneous disease", "داء جلدي"], ["Visceral disease", "داء حشوي"], ["Mucocutaneous disease", "داء مخاطي جلدي"],
    ALL, NONE], "D"),

 Q("Habitat for visceral leishmaniasis:", "موطن داء الليشمانيات الحشوي:",
   [["Macrophage of reticuloendothelial system (Spleen, Liver, Bone)",
     "بلاعم الجهاز الشبكي البطاني (الطحال والكبد والعظم)"],
    ["Kidney", "الكلية"], ["Muscle", "العضلة"], ["Skin", "الجلد"], ["Lung", "الرئة"]], "A"),

 Q("Habitat for visceral leishmaniasis:", "موطن داء الليشمانيات الحشوي:",
   [["Bone", "العظم"], ["Macrophage of reticuloendothelial system (spleen, liver)",
     "بلاعم الجهاز الشبكي البطاني (الطحال والكبد)"], ["Kidney", "الكلية"], ["Lung", "الرئة"], ["Bone", "العظم"]], "B"),

 Q("Visceral leishmaniasis is also known as:", "داء الليشمانيات الحشوي يُعرف أيضًا بـ:",
   [["Kala-azar", "الكلازار"], ["Black fever", "الحمّى السوداء"], ["Dumdum fever", "حمّى دمدم"],
    ALLt, NONEb], "D"),

 Q("Intermediate host of Cutaneous leishmaniasis:", "العائل الوسطي لداء الليشمانيات الجلدي:",
   [["Man", "الإنسان"], ["Cow", "البقرة"], ["Cat", "القطة"], ["Dog", "الكلب"],
    ["Female sand fly", "ذبابة الرمل الأنثى"]], "E"),

 Q("The causative agent of Kala-azar is:", "العامل المسبّب للكلازار هو:",
   [Lt(), S("Leishmania major", "الليشمانيا الكبرى"), Ld(),
    S("Leishmania infantum", "الليشمانيا الطفلية"), S("Leishmania brazilliensis", "الليشمانيا البرازيلية")], "C"),

 Q("Leishmania donovani:", "الليشمانيا الدونوفانية:",
   [["Cause VL", "تسبّب داء الليشمانيات الحشوي (VL)"], ["Cause CL", "تسبّب داء الليشمانيات الجلدي (CL)"],
    ["Mosquito is the vector", "البعوض هو الناقل"], ["Baghdad boil", "حبّة بغداد"],
    ["Less pathogenic than Leishmania tropica", "أقل إمراضًا من الليشمانيا المدارية"]], "A"),

 Q("Which of the following is the stage of Leishmania that is transmitted to humans by the vector?",
   "أيُّ ما يأتي هو طور الليشمانيا الذي ينقله الناقل إلى الإنسان؟",
   [EPI, AMA, TRY, PRO, ALL], "D"),

 Q("Among blood flagellates, the stage of development that has an undulating membrane, and a kinetoplast located posterior to the nucleus is the:",
   "من بين السوطيات الدموية، الطور الذي له غشاء متموّج وكينيتوبلاست خلف النواة هو:",
   [TRY, EPI, AMA, PRO, NONE], "A"),

 Q("Which of the following is exclusively an intracellular parasite in the definitive host?",
   "أيُّ ما يأتي طفيلي داخل خلوي حصريًّا في العائل النهائي؟",
   [S("Trypanosoma brucei", "المثقبية البروسية"), Ld(), S("Trichomonas vaginalis", "المشعرة المهبلية"),
    S("Entamoeba histolytica", "الأميبا الحالّة للنسيج"), S("Giardia lamblia", "الجيارديا اللمبلية")], "B"),

 Q("What is the major mode of Black fever transmission to humans?",
   "ما الطريقة الرئيسة لانتقال الحمّى السوداء إلى الإنسان؟",
   [["Bite of both sexes infected sand fly", "لسعة ذبابة الرمل المصابة من كلا الجنسين"],
    ["Bite of male infected mosquito", "لسعة البعوضة الذكر المصابة"],
    ["Bite of male infected sand fly", "لسعة ذبابة الرمل الذكر المصابة"],
    ["Bite of female infected mosquito", "لسعة البعوضة الأنثى المصابة"],
    ["Bite of infected female sand fly", "لسعة ذبابة الرمل الأنثى المصابة"]], "E"),

 Q("Which of the following cause Oriental sore?", "أيُّ ما يأتي يسبّب القرحة الشرقية؟",
   [Lt(), S("Leishmania major", "الليشمانيا الكبرى"), Ld(),
    S("Leishmania aethiopica", "الليشمانيا الحبشية"), S("Leishmania infantum", "الليشمانيا الطفلية")], "A"),

 Q("If someone has been infected with Leishmania tropica, what will you see under the microscope?",
   "إذا أُصيب شخص بالليشمانيا المدارية، فماذا سترى تحت المجهر؟",
   [TRY, AMA, PRO, EPI, ALL], "B"),

 Q("Which of the following is vector of Leishmania?", "أيُّ ما يأتي ناقل الليشمانيا؟",
   [["Human", "الإنسان"], ["Kissing bug", "بقّة التقبيل"], ["Tsetse", "ذبابة تسي تسي"], SAND,
    ["House fly", "الذبابة المنزلية"]], "D"),

 Q("In which of the following pathogen, we can use skin test to follow-up with the patient?",
   "في أيٍّ من الممرضات الآتية يمكن استعمال الاختبار الجلدي لمتابعة المريض؟",
   [Ld(), S("Trypanosoma brucei", "المثقبية البروسية"), Lt(),
    S("Giardia lamblia", "الجيارديا اللمبلية"), S("Trichomonas tenax", "المشعرة الفموية")], "C"),

 Q("The vector of Leishmania tropica in Baghdad area is:", "ناقل الليشمانيا المدارية في منطقة بغداد هو:",
   [S("Phlebotomus papatasi", "فاصدة بابا طاسي (Phlebotomus papatasi)"),
    S("Phlebotomus sergenti", "فاصدة سيرجنت (Phlebotomus sergenti)"),
    S("Phlebotomus alexandri", "فاصدة الإسكندري (Phlebotomus alexandri)"),
    ["A and B", "A و B"], ["A, B, and C", "A و B و C"]], "D"),

 Q("Oriental sore is a parasitic disease caused by:", "القرحة الشرقية داء طفيلي يسبّبه:",
   [S("Giardia lamblia", "الجيارديا اللمبلية"), Lt(), S("Toxoplasma gondii", "المقوّسة الغوندية"),
    S("Entamoeba histolytica", "الأميبا الحالّة للنسيج"), ["Plasmodium spp", "أنواع المتصوّرات (Plasmodium spp)"]], "B"),

 Q("Oriental sore is caused by?", "القرحة الشرقية يسبّبها؟",
   [["Bacterium", "جرثومة"], ["Virus", "فيروس"], ["Protozoan", "أوالٍ (بروتوزوا)"],
    ["Fungus", "فطر"], ["Yeast", "خميرة"]], "C"),

 Q("Choose the parasite species which is considered intracellular:", "اختر نوع الطفيلي الذي يُعدّ داخل خلوي:",
   [Ld(), Lt(), ["Trypomastigote", "المثقبي (Trypomastigote)"], ["A and B", "A و B"], ["A, B, and C", "A و B و C"]], "D"),

 Q("Leishmania tropica:", "الليشمانيا المدارية:",
   [["More dangerous than L. donovani", "أخطر من الليشمانيا الدونوفانية"],
    ["Faster in spread than L. donovani", "أسرع انتشارًا من الليشمانيا الدونوفانية"],
    ["Enter host orally", "تدخل العائل فمويًّا"], ["Tick is the vector", "القُراد هو الناقل"],
    ["Found in children only", "تُوجد في الأطفال فقط"]], "B"),

 Q("Leishmania stage is present in the cells of:", "طور الليشمانيا موجود في خلايا:",
   [["Vertebrate", "الفقاريات"], ["Invertebrate", "اللافقاريات"], ["Arthropods", "المفصليات"],
    ALLt, NONEb], "A"),

 Q("Phlebotomus is the vector of:", "الفاصدة (Phlebotomus) هي ناقل:",
   [S("Toxoplasma gondii", "المقوّسة الغوندية"), S("Entamoeba gingivalis", "الأميبا اللثوية"),
    S("Trypanosoma cruzi", "المثقبية الكروزية"), Lt(), ["Plasmodium spp", "أنواع المتصوّرات (Plasmodium spp)"]], "D"),

 Q("All statements concerning Kala-azar is correct Except:", "كل العبارات عن الكلازار صحيحة ما عدا:",
   [["Kala-azar is caused by Leishmania donovani", "الكلازار تسبّبه الليشمانيا الدونوفانية"],
    ["Kala-azar is transmitted by the bite of sand flies", "ينتقل الكلازار بلسعة ذباب الرمل"],
    ["Kala-azar occurs primarily in rural Latin America", "يحدث الكلازار أساسًا في ريف أمريكا اللاتينية"],
    ["Kala-azar can be diagnosed by finding amastigote in bone marrow", "يُشخَّص الكلازار بإيجاد الطور عديم السوط في نقي العظم"],
    ["Kala-azar can be caused hepatic ulcer", "قد يسبّب الكلازار قرحة كبدية"]], "C"),

 Q("Leishmania tropica cause:", "الليشمانيا المدارية تسبّب:",
   [["Kala-azar", "الكلازار"], ["Dumdum fever", "حمّى دمدم"], ["Baghdad boil", "حبّة بغداد"],
    ["Black fever", "الحمّى السوداء"], ALL], "C"),

 Q("The common name of Leishmania tropica:", "الاسم الشائع لليشمانيا المدارية:",
   [["Kala-azar", "الكلازار"], ["Delhi boils", "حبّة دلهي"], ["Espundia", "الإسپونديا (Espundia)"],
    ["Dumdum fever", "حمّى دمدم"], NONE], "B"),

 Q("Intermediate host of cutaneous leishmaniasis:", "العائل الوسطي لداء الليشمانيات الجلدي:",
   [["Man", "الإنسان"], ["Cow", "البقرة"], ["Cat", "القطة"], ["Dog", "الكلب"],
    ["Female sand fly", "ذبابة الرمل الأنثى"]], "A"),

 Q("Visceral Leishmaniasis caused by:", "داء الليشمانيات الحشوي يسبّبه:",
   [S("Taenia solium", "الشريطية المسلّحة"), S("L. donovani", "الليشمانيا الدونوفانية"),
    S("Echinococcus granulosus", "المشوكة الحبيبية"), ["Plasmodium spp.", "أنواع المتصوّرات"],
    S("Toxoplasma gondii", "المقوّسة الغوندية")], "B"),

 Q("Which of the following parasite can be spread to human by the bite of sand fly:",
   "أيُّ الطفيليات الآتية يمكن أن ينتشر إلى الإنسان بلسعة ذبابة الرمل:",
   [S("Toxoplasma gondii", "المقوّسة الغوندية"), S("E. histolytica", "الأميبا الحالّة للنسيج"),
    S("Trichomonas vaginalis", "المشعرة المهبلية"), S("L. donovani", "الليشمانيا الدونوفانية"), NONEb], "D"),

 Q("Delhi boil is a disease caused by:", "حبّة دلهي داء يسبّبه:",
   [S("Leishmania donovani", "الليشمانيا الدونوفانية"), S("Plasmodium malariae", "المتصوّرة الوبالية"),
    S("Plasmodium vivax", "المتصوّرة النشيطة"), S("Plasmodium ovale", "المتصوّرة البيضوية"), Lt()], "E"),

 Q("Baghdad boil is caused by:", "حبّة بغداد يسبّبها:",
   [Lt(), S("Leishmania donovani", "الليشمانيا الدونوفانية"), S("Trypanosoma cruzi", "المثقبية الكروزية"),
    S("Toxoplasma gondii", "المقوّسة الغوندية"), S("Trichomonas vaginalis", "المشعرة المهبلية")], "A"),

 Q("The incubation period for Kala-azar disease is:", "فترة حضانة داء الكلازار هي:",
   [["24 hours", "24 ساعة"], ["One month", "شهر واحد"], ["7 days", "7 أيام"],
    ["2-4 months", "`2-4` أشهر"], ["Unknown", "غير معروف"]], "D"),

 Q("Human acquire Leishmania spp. infection through:", "يكتسب الإنسان عدوى الليشمانيا عن طريق:",
   [["Fecal – Oral route", "الطريق البرازي – الفموي"], ["Sexual intercourse", "الجماع الجنسي"],
    ["Bite of an infected female sand fly", "لسعة ذبابة الرمل الأنثى المصابة"],
    ["Drinking food", "تناول الطعام"], NONE], "C"),

 Q("Which of the following is vector for cutaneous Leishmaniasis:", "أيُّ ما يأتي ناقل لداء الليشمانيات الجلدي:",
   [S("Phlebotomus", "الفاصدة (Phlebotomus)"), ["Reduviid", "الريدوفيد"], S("Anopheles", "الأنوفيلة (Anopheles)"),
    S("Lutzomyia", "اللوتزومية (Lutzomyia)"), ["A and D", "A و D"]], "E"),

 Q("The causative agent of Kala-azar is:", "العامل المسبّب للكلازار هو:",
   [Lt(), S("Leishmania major", "الليشمانيا الكبرى"), Ld(),
    S("Leishmania infantum", "الليشمانيا الطفلية"), S("Leishmania braziliense", "الليشمانيا البرازيلية")], "C"),

 Q("Kala-azar in human is caused by:", "الكلازار في الإنسان يسبّبه:",
   [S("Toxoplasma gondii", "المقوّسة الغوندية"), S("Taenia solium", "الشريطية المسلّحة"), Ld(),
    S("Balantidium coli", "البالانتيدية القولونية"), S("Giardia lamblia", "الجيارديا اللمبلية")], "C"),

 Q("Which of the following is vector of Leishmania?", "أيُّ ما يأتي ناقل الليشمانيا؟",
   [["Human", "الإنسان"], ["Kissing bug", "بقّة التقبيل"], ["Tsetse", "ذبابة تسي تسي"], SAND,
    ["House fly", "الذبابة المنزلية"]], "D"),

 Q("Which of the following pathogen we can use skin test to follow-up with the patient?",
   "في أيٍّ من الممرضات الآتية يمكن استعمال الاختبار الجلدي لمتابعة المريض؟",
   [Ld(), S("Trypanosoma brucei", "المثقبية البروسية"), Lt(),
    S("Giardia lamblia", "الجيارديا اللمبلية"), S("Trichomonas tenax", "المشعرة الفموية")], "C"),

 Q("The developing stage of Trypanosomatidae that does not have free flagellum is:",
   "الطور النامي من المثقبيات الذي لا يملك سوطًا حرًّا هو:",
   [["Trypomnastigote", "المثقبي (Trypomastigote)"], ["Epimastiogote", "فوق السوطي (Epimastigote)"],
    ["Promastigote", "أمامي السوط (Promastigote)"], ["Amastigote", "عديم السوط (Amastigote)"],
    ["All of the above with free flagellum", "جميع ما سبق له سوط حرّ"]], "D"),

 Q("Leishmania tropica:", "الليشمانيا المدارية:",
   [["More dangerous than L. donovani", "أخطر من الليشمانيا الدونوفانية"],
    ["High spread than L. donovani", "أوسع انتشارًا من الليشمانيا الدونوفانية"],
    ["Enter host orally", "تدخل العائل فمويًّا"], ["Tick is the vector", "القُراد هو الناقل"],
    ["Found in children only", "تُوجد في الأطفال فقط"]], "B"),

 Q("Leishmania parasites are transmitted to human by:", "تنتقل طفيليات الليشمانيا إلى الإنسان بـ:",
   [["Tsetse", "ذبابة تسي تسي"], SANDs, ["Bug", "البقّة"], ["Mosquito", "البعوض"], ["Unknown", "غير معروف"]], "B"),

 Q("Leishmania is transmitted by:", "تنتقل الليشمانيا بـ:",
   [SAND, ["Milk", "الحليب"], ["Sexually", "جنسيًّا"], ["Food and water", "الطعام والماء"], NONE], "A"),

 Q("Leishmania parasite transmitted by the bite of:", "ينتقل طفيلي الليشمانيا بلسعة:",
   [["House fly", "الذبابة المنزلية"], ["Tsetse fly", "ذبابة تسي تسي"], SAND, ["Mosquito", "البعوض"], NONEb], "C"),

 Q("Leishmania stage is present in the cells of:", "طور الليشمانيا موجود في خلايا:",
   [["Vertebrate", "الفقاريات"], ["Invertebrate", "اللافقاريات"], ["Arthropods", "المفصليات"],
    ALLt, NONEb], "A"),

 Q("Phlebotomus is the vector of:", "الفاصدة (Phlebotomus) هي ناقل:",
   [S("Toxoplasma gondii", "المقوّسة الغوندية"), S("Entamoeba gingivalis", "الأميبا اللثوية"),
    S("Trypanosoma cruzi", "المثقبية الكروزية"), Lt(), ["Plasmodium spp", "أنواع المتصوّرات (Plasmodium spp)"]], "D"),

 Q("All statements concerning Kala-azar is correct Except:", "كل العبارات عن الكلازار صحيحة ما عدا:",
   [["Kala-azar is caused by Leishmania donovani", "الكلازار تسبّبه الليشمانيا الدونوفانية"],
    ["Kala-azar is transmitted by the bite of sandflies", "ينتقل الكلازار بلسعة ذباب الرمل"],
    ["Kala-azar occurs primarily in rural Latin America", "يحدث الكلازار أساسًا في ريف أمريكا اللاتينية"],
    ["Kala-azar can be diagnosed by finding amastigote in bone marrow", "يُشخَّص الكلازار بإيجاد الطور عديم السوط في نقي العظم"],
    ["Kala-azar can be cause hepatic ulcer", "قد يسبّب الكلازار قرحة كبدية"]], "C"),

 Q("Leishmaniasis is:", "داء الليشمانيات هو:",
   [["Cutaneous disease", "داء جلدي"], ["Visceral disease", "داء حشوي"], ["Mucocutaneous disease", "داء مخاطي جلدي"],
    ALL, NONE], "D"),

 Q("Leishmania tropica cause:", "الليشمانيا المدارية تسبّب:",
   [["Kala azar", "الكلازار"], ["Dum dum fever", "حمّى دمدم"], ["Baghdad boil", "حبّة بغداد"],
    ["Black fever", "الحمّى السوداء"], ALL], "C"),

 Q("The common name of Leishmania tropica:", "الاسم الشائع لليشمانيا المدارية:",
   [["Kala-azar", "الكلازار"], ["Delhy boils", "حبّة دلهي"], ["Espundia", "الإسپونديا (Espundia)"],
    ["Dumdum fever", "حمّى دمدم"], NONE], "B"),

 Q("The causative agent of Kala-azar is:", "العامل المسبّب للكلازار هو:",
   [S("Leshmania tropica", "الليشمانيا المدارية"), S("Leishmania major", "الليشمانيا الكبرى"), Ld(),
    S("Leishmania infantum", "الليشمانيا الطفلية"), S("Leishmania brazielensis", "الليشمانيا البرازيلية")], "C"),

 Q("Kala azar in humans is caused by:", "الكلازار في الإنسان يسبّبه:",
   [S("Toxoplasma gondii", "المقوّسة الغوندية"), S("Taenia solium", "الشريطية المسلّحة"), Ld(),
    S("Balantidium coli", "البالانتيدية القولونية"), S("Giardia lamblia", "الجيارديا اللمبلية")], "C"),

 Q("Intermediate host of cutaneous leishmaniasis:", "العائل الوسطي لداء الليشمانيات الجلدي:",
   [["Man", "الإنسان"], ["Cow", "البقرة"], ["Cat", "القطة"], ["Dog", "الكلب"],
    ["Female sand fly", "ذبابة الرمل الأنثى"]], "A"),

 Q("Oriental sore is a parasitic disease cause by:", "القرحة الشرقية داء طفيلي يسبّبه:",
   [S("Giardia lamblia", "الجيارديا اللمبلية"), Lt(), S("Toxoplasma gondii", "المقوّسة الغوندية"),
    S("Entamoeba histolytica", "الأميبا الحالّة للنسيج"), ["Plasmodium spp", "أنواع المتصوّرات (Plasmodium spp)"]], "B"),

 Q("Visceral Leishmaniasis caused by:", "داء الليشمانيات الحشوي يسبّبه:",
   [S("Taenia solium", "الشريطية المسلّحة"), S("L. donovani", "الليشمانيا الدونوفانية"),
    S("Echinococcus granulosus", "المشوكة الحبيبية"), ["Plasmodium spp.", "أنواع المتصوّرات"],
    S("Toxoplasma gondii", "المقوّسة الغوندية")], "B"),

 Q("Which of the following parasite can be spread to human by the bite of sand fly:",
   "أيُّ الطفيليات الآتية يمكن أن ينتشر إلى الإنسان بلسعة ذبابة الرمل:",
   [S("Toxoplasma gondii", "المقوّسة الغوندية"), S("E. histolytica", "الأميبا الحالّة للنسيج"),
    S("Trichomonas vaginalis", "المشعرة المهبلية"), S("L. donovani", "الليشمانيا الدونوفانية"), NONEb], "D"),

 Q("Baghdad boil is caused by:", "حبّة بغداد يسبّبها:",
   [Lt(), S("Leishmania donovani", "الليشمانيا الدونوفانية"), S("Trypanosoma cruzi", "المثقبية الكروزية"),
    S("Toxoplasma gondii", "المقوّسة الغوندية"), S("Trichomonas vaginalis", "المشعرة المهبلية")], "A"),

 Q("Habitat for visceral leishmaniasis:", "موطن داء الليشمانيات الحشوي:",
   [["Bone", "العظم"], ["Macrophage of reticuloendothelial system (spleen, liver)",
     "بلاعم الجهاز الشبكي البطاني (الطحال والكبد)"], ["Kidney", "الكلية"], ["Liver", "الكبد"], ["Bone", "العظم"]], "B"),

 Q("The incubation period for Kala-azar disease is:", "فترة حضانة داء الكلازار هي:",
   [["24 hours", "24 ساعة"], ["one month", "شهر واحد"], ["7 days", "7 أيام"],
    ["2-4 months", "`2-4` أشهر"], ["unknown", "غير معروف"]], None,
   ("Not marked in the source file. The identical earlier question is marked D (2-4 months), which is the accepted incubation period for kala-azar.",
    "غير مؤشَّر في الملف الأصلي. والسؤال المطابق السابق مؤشَّر عليه D (`2-4` أشهر)، وهي فترة الحضانة المعتمدة للكلازار.")),

 Q("Human acquire Leishmania spp infection by:", "يكتسب الإنسان عدوى الليشمانيا بـ:",
   [["Fecal – Oral route", "الطريق البرازي – الفموي"], ["Sexual intercourse", "الجماع الجنسي"],
    ["Bite of an infected female sand fly", "لسعة ذبابة الرمل الأنثى المصابة"],
    ["Drinking food", "تناول الطعام"], NONE], "C"),
]

n = sum(1 for q in mcq if "topic_en" not in q)
from collections import Counter
cnt = Counter(q.get("answer") for q in mcq if "topic_en" not in q)
notes = sum(1 for q in mcq if "note_en" in q)
print("questions:", n, "| answers:", dict(cnt), "| notes:", notes)

meta = {
 "subject_en": "Diagnostic Parasitology", "subject_ar": "الطفيليات التشخيصية",
 "instructor": "أ.د. نزار الخفاجي",
 "unit_en": "Week 9", "unit_ar": "الأسبوع 9", "unit_label": "WEEK", "unit_no": "9",
 "title_en": "Genus Leishmania",
 "title_ar": "جنس الليشمانيا (Leishmania)",
 "department": "قسم التحليلات", "stage": "The fourth stage — الرابعة",
 "kind": "Theory — نظري", "questions_kind": "MCQ — أسئلة اختيار",
 "file_name": "BIOS - طفيليات نظري الأسبوع التاسع - الأسئلة",
 "short_ar": "طفيليات",
}
questions = {
 "title_en": meta["title_en"], "title_ar": meta["title_ar"],
 "sub": "MCQ", "answers_inline": True,
 "mcq_en": "MCQ — 1st semester, week 9", "mcq_ar": "أسئلة الاختيار — الفصل الأول، الأسبوع التاسع",
 "intro_en": ["Q. Select the most correct answer from the followings",
              "The answer under each question is the one marked in the source file, kept as it is; a BIOS note flags any answer that is unsolved, doubtful or wrong."],
 "intro_ar": ["س. اختر الإجابة الأصح مما يأتي",
              "الحل تحت كل سؤال هو المؤشَّر في الملف الأصلي كما هو؛ وملاحظة BIOS تنبّه على أي سؤال غير محلول أو حلّه مشكوك فيه أو خاطئ."],
 "mcq": ltr_all(mcq),
}
out = "/home/user/-/parasitology-week9-mcq/lecture.json"
os.makedirs(os.path.dirname(out), exist_ok=True)
json.dump({"meta": meta, "questions": questions}, open(out, "w"), ensure_ascii=False, indent=1)
print("wrote", out)
