---
source: BIOS-Obsidian/tools/scripts/hem/make.py
handouts: [enzymology-lab1-safety-tubes]
saved: 2026-10-29
tags: [bios, code]
---
# hem/make.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#enzymology-lab1-safety-tubes|enzymology-lab1-safety-tubes]]

```python
import json, os

def C(en, ar, **k): return dict(t="card", en=en, ar=ar, **k)
def R(en, ar): return dict(t="rule", en=en, ar=ar)
def SEC(en, ar): return dict(t="section", en=en, ar=ar)
def H2(en, ar): return dict(t="h2", en=en, ar=ar)

def tube_section(name_en, name_ar, img, en_list, ar_list):
    """Heading + first sentence beside the tube drawing, then additive and uses as separate cards."""
    add = next(i for i, x in enumerate(en_list) if x.startswith("**Additive"))
    use = next(i for i, x in enumerate(en_list) if x.startswith("**Laboratory"))
    out = [H2(name_en, name_ar),
           dict(t="side", blocks=[C(en_list[:add], ar_list[:add])],
                figure=dict(src=f"assets/{img}", en=name_en, ar=name_ar, h="30mm", fit="contain"))]
    out.append(C(en_list[add:use], ar_list[add:use]))
    out.append(C(en_list[use:], ar_list[use:]))
    return out

blocks = [
 SEC("LAB SAFETY PROTOCOLS", "بروتوكولات السلامة في المختبر"),
 C("**Use Protective Gear**", "**استعمل معدات الحماية**",
   list_en=["Safety Goggles", "Lab Coat", "Gloves", "Long Pants", "Closed Shoes"],
   list_ar=["نظارات السلامة", "صدرية (معطف) المختبر", "القفازات", "بنطلون طويل", "حذاء مغلق"]),
 R(["**Proper Supervision**", "Don't perform lab experiments without instructure supervision."],
   ["**الإشراف المناسب**", "لا تُجرِ تجارب المختبر من دون إشراف المدرّس."]),
 R(["**ID Hazards**", "Always read labels before using any chemicals."],
   ["**تعرّف على المخاطر**", "اقرأ الملصقات دائمًا قبل استعمال أي مواد كيميائية."]),
 R(["**Safety First**", "Known location of safety equipment and emergency numbers."],
   ["**السلامة أولًا**", "معرفة مكان معدات السلامة وأرقام الطوارئ."]),
 R(["**No Food**", "Don't eat or drink in the lab and never taste chemicals."],
   ["**ممنوع الطعام**", "لا تأكل ولا تشرب في المختبر، ولا تتذوّق المواد الكيميائية أبدًا."]),
 R(["**Be Attentive**", "Be attentive while in the lab.", "Don't leave an experiment in progress."],
   ["**كن منتبهًا**", "كن منتبهًا ما دمت في المختبر.", "لا تترك تجربة وهي قيد التنفيذ."]),
 R(["**Handle Glassware Carefully**", "Properly dispose of anything that breaks."],
   ["**تعامل مع الزجاجيات بحذر**", "تخلّص بطريقة صحيحة من أي شيء ينكسر."]),
 R(["**Clean Up**", "After completing the lab, carefully clean your workspace and the equipment.", "Don't forget to wash your hands."],
   ["**التنظيف**", "بعد إكمال العمل في المختبر، نظّف مكان عملك والأجهزة بعناية.", "لا تنسَ غسل يديك."]),

 SEC("Lab Safety", "السلامة في المختبر"),
 C("It is our joint responsibility to keep the lab clean and safe!", "إنها مسؤوليتنا المشتركة أن نحافظ على المختبر نظيفًا وآمنًا!",
   list_en=["Authorised persons only in the laboratory", "Lab coats must be worn", "Sensible footwear must be worn –no open shoes",
            "All accidents and dangerous events must be reported and recorded", "No smoking, of any kind", "Do not store or consume food or drink in the lab",
            "All work must be carried out in accordance with risk assessment", "Dispose of waste properly, in line with policy",
            "Keep the lab tidy, and emergency routes accessible"],
   list_ar=["الأشخاص المخوَّلون فقط في المختبر", "يجب ارتداء صدرية المختبر", "يجب ارتداء حذاء مناسب — لا أحذية مفتوحة",
            "يجب الإبلاغ عن جميع الحوادث والأحداث الخطرة وتسجيلها", "ممنوع التدخين بكل أنواعه", "لا تخزّن الطعام أو الشراب ولا تتناوله في المختبر",
            "يجب أن يُنفَّذ كل عمل وفق تقييم المخاطر", "تخلّص من النفايات بطريقة صحيحة، وفق السياسة المعتمدة",
            "حافظ على ترتيب المختبر، واجعل طرق الطوارئ سالكة"]),
 dict(t="figure", src="assets/lab-safety-rules.jpg", en="Lab safety rules", ar="قواعد السلامة في المختبر", width="104mm"),
 dict(t="note", en="If anything is out of order, please notify: [[cut]]", ar="إذا كان أي شيء غير سليم، يُرجى الإبلاغ: [[قطع]]"),

 SEC("Common types of blood collecting test tubes", "الأنواع الشائعة لأنابيب جمع الدم"),
 C("There are different types of blood collection tubes used in hospital for various diagnostic tests.",
   "توجد أنواع مختلفة من أنابيب جمع الدم تُستعمل في المستشفى لمختلف الفحوص التشخيصية."),
 C("Each tube has different functions and must be used accordingly in collecting blood samples.",
   "لكل أنبوب وظائف مختلفة، ويجب استعماله وفقًا لها عند جمع عيّنات الدم."),

 SEC("Order of draw", "ترتيب السحب"),
 dict(t="figure", src="assets/tubes-order.svg", en="Tube stopper colours in the order of draw (redrawn)", ar="ألوان أغطية الأنابيب حسب ترتيب السحب (أُعيد رسمها)", width="140mm", keep=True),
 dict(t="table", head=["#", "Tube", "Stopper color", "Additives", "Laboratory Use"], widths=["8mm", "28mm", "36mm", "38mm", ""], numbered=True, key_cols=[2],
      rows=[["1", "Plain Tube", "Red Top Tube", "no additive", "Drug … blood … [[cut]]"],
            ["2", "EDTA Tube", "Lavender Top Tube", "EDTA\\*", "CBC\\*, HbA1c"],
            ["3", "Heparin Tube", "Green Top Tube", "Sodium Heparin", "Plasma chemistry, ammonia level"],
            ["4", "ESR Tube", "Black Top Tube", "Sodium citrate", "Westergren sedimentation rate"],
            ["5", "Glucose Tube", "Grey Top Tube", "Sodium fluoride", "glucose tolerance testing, alcohol level"],
            ["6", "PT Tube", "Blue Tube", "Sodium citrate", "PT\\*, PTT\\*"],
            ["7", "Serum Tube", "Yellow Top Tube", "ACD\\*, SPS\\*", "Whole blood determination"],
            ["8", "Thrombin Tube", "Orange Top Tube", "Thrombin", "Chemical testing"],
            ["9", "Gel Yellow tube", "Serum Gel Tube", "contains a clot activator and serum gel separator", "various laboratory tests"]]),
 dict(t="note", label=["Abbreviations", "الاختصارات"],
      en="EDTA=Ethylene diamine tetraacetic acid, ACD= Acid citrate dextrose, CBC=Complete blood count, PT=Prothrombin times, PTT=Partial thrombinplastin times, SPS=sodium polyanethol sulfonate",
      ar="EDTA = حامض الإثيلين ثنائي الأمين رباعي الخليك، ACD = سترات الحامض والدكستروز، CBC = تعداد الدم الكامل، PT = زمن البروثرومبين، PTT = زمن الثرومبوبلاستين الجزئي، SPS = سلفونات بولي أنيثول الصوديوم"),

 SEC("Tube colours in detail", "تفاصيل ألوان الأنابيب"),
 *tube_section("Red lab tubes", "الأنابيب الحمراء", "tube-red.svg",
   ["The red tubes are used for a series of biochemistry tests that require serum.",
    "**Additives**- Red tubes contain silica particles, which are going to act as the clot activators.",
    "The clot activator is responsible for promoting blood clot with silica or glass particles.",
    "Usually no additive present.",
    "**Laboratory uses**- serum testing (glucose, triglycerides, cholesterol, HDL, potassium amylase, BUN, alkaline phosphatase, liver enzymes, or CK), antibody screening, blood bank serology, prototyping of red cell, DAT, monospot, RPR, ANA, and rheumatoid factor."],
   ["تُستعمل الأنابيب الحمراء لسلسلة من الفحوص الكيموحيوية التي تتطلب المصل.",
    "**المضافات** — تحتوي الأنابيب الحمراء على جزيئات السيليكا، التي تعمل منشّطاتٍ للتخثّر.",
    "منشّط التخثّر مسؤول عن تعزيز تخثّر الدم بجزيئات السيليكا أو الزجاج.",
    "وعادةً لا توجد مادة مضافة.",
    "**الاستعمالات المختبرية** — فحوص المصل (الكلوكوز، الدهون الثلاثية، الكوليسترول، HDL، البوتاسيوم، الأميليز، BUN، الفوسفاتيز القلوي، إنزيمات الكبد، أو CK)، وتحرّي الأجسام المضادة، ومصليات بنك الدم، وتحديد أنماط الخلايا الحمر، وDAT، وmonospot، وRPR، وANA، والعامل الرثوي."]),
 *tube_section("Yellow lab tubes", "الأنابيب الصفراء", "tube-yellow.svg",
   ["These tubes are used for blood as well as bodily fluid cultures",
    "**Additive**- Anticoagulant SPS (Sodium Polyanethol Sulfonate) & ACD (acid citrate dextrose).",
    "The additive prevents the clotting of the blood and stabilizes the growth of bacteria.",
    "**Laboratory uses**- bodily fluid cultures (Paternity, HLA, and DNA).",
    "Tubes that have ACD are used for cellular studies, paternity testing, and HLA typing."],
   ["تُستعمل هذه الأنابيب لمزارع الدم وكذلك سوائل الجسم",
    "**المادة المضافة** — مانع التخثّر SPS (سلفونات بولي أنيثول الصوديوم) وACD (سترات الحامض والدكستروز).",
    "تمنع المادة المضافة تخثّر الدم وتُثبّت نمو البكتيريا.",
    "**الاستعمالات المختبرية** — مزارع سوائل الجسم (الأبوّة، HLA، وDNA).",
    "وتُستعمل الأنابيب التي تحتوي ACD للدراسات الخلوية، وفحص الأبوّة، وتنميط HLA."]),
 *tube_section("Light blue tubes", "الأنابيب الزرقاء الفاتحة", "tube-blue.svg",
   ["The blue bottles are used for the hematology tests, which involve the system of clotting and require whole blood, which is inactivated, for the analysis.",
    "**Additive**- Sodium citrate.",
    "It helps in binding and removing calcium in order to prevent the blood from clotting.",
    "**Laboratory uses**- Coagulation, PT, FDP, APTT/PTT, TT, and factor assays."],
   ["تُستعمل القناني الزرقاء لفحوص أمراض الدم التي تخص نظام التخثّر وتتطلب دمًا كاملًا مُعطَّلًا للتحليل.",
    "**المادة المضافة** — سترات الصوديوم.",
    "تساعد على ربط الكالسيوم وإزالته لمنع الدم من التخثّر.",
    "**الاستعمالات المختبرية** — التخثّر، PT، FDP، APTT/PTT، TT، ومقايسات العوامل."]),
 *tube_section("Green lab tubes", "الأنابيب الخضراء", "tube-green.svg",
   ["The green tubes are the most common bottles, used primarily for the biochemistry tests, which are known to require whole blood or heparinized plasma.",
    "**Additive**- Heparin (Sodium/lithium/ammonium).",
    "It inhibits the formation of thrombin in order to prevent blood clotting.",
    "**Laboratory uses**- Chemistry testing, ammonia, insulin, chromosome screening, aldosterone, renin, and insulin."],
   ["الأنابيب الخضراء هي القناني الأكثر شيوعًا، وتُستعمل أساسًا للفحوص الكيموحيوية التي تتطلب دمًا كاملًا أو بلازما مُهبرَنة.",
    "**المادة المضافة** — الهيبارين (صوديوم/ليثيوم/أمونيوم).",
    "يثبّط تكوّن الثرومبين لمنع تخثّر الدم.",
    "**الاستعمالات المختبرية** — الفحوص الكيميائية، الأمونيا، الأنسولين، تحرّي الكروموسومات، الألدوستيرون، الرينين، والأنسولين."]),
 *tube_section("Lavender lab tubes", "الأنابيب البنفسجية (الخزامية)", "tube-lavender.svg",
   ["These bottles are used for the hematology tests, where normally whole blood is needed for analysis.",
    "**Additive**- EDTA.",
    "It helps in removing calcium, thereby preventing a blood clot.",
    "**Laboratory usage**- Hematology testing, blood film for malaria parasites or abnormal cells, red cell folate, reticulocytes, parathyroid hormone, and monospot test."],
   ["تُستعمل هذه القناني لفحوص أمراض الدم، حيث يُحتاج عادةً إلى الدم الكامل للتحليل.",
    "**المادة المضافة** — EDTA.",
    "يساعد على إزالة الكالسيوم، فيمنع بذلك تخثّر الدم.",
    "**الاستعمال المختبري** — فحوص أمراض الدم، والمسحة الدموية لطفيليات الملاريا أو الخلايا غير الطبيعية، وفولات الخلايا الحمر، والخلايا الشبكية، وهرمون جار الدرقية، وفحص monospot."]),
 *tube_section("Grey lab tubes", "الأنابيب الرمادية", "tube-grey.svg",
   ["These tubes are also common and are used for the collection of blood.",
    "**Additive**- Sodium fluoride and potassium oxalate.",
    "The sodium fluoride is responsible for acting as the antiglycolytic agent, which ensures that, there is no further breakdown of glucose after the sample has been collected.",
    "Potassium oxalate is responsible for removing calcium and it is also known to act as the anticoagulant.",
    "**Laboratory uses**- Chemistry testing, mostly lactate and glucose and glucose tolerance test."],
   ["هذه الأنابيب شائعة أيضًا، وتُستعمل لجمع الدم.",
    "**المادة المضافة** — فلوريد الصوديوم وأوكزالات البوتاسيوم.",
    "فلوريد الصوديوم مسؤول عن العمل عاملًا مضادًا لتحلّل الكلوكوز، مما يضمن عدم استمرار تكسّر الكلوكوز بعد جمع العيّنة.",
    "أما أوكزالات البوتاسيوم فمسؤولة عن إزالة الكالسيوم، وتُعرف أيضًا بأنها تعمل مانعًا للتخثّر.",
    "**الاستعمالات المختبرية** — الفحوص الكيميائية، ولا سيما اللاكتات والكلوكوز وفحص تحمّل الكلوكوز."]),
]

def M(en, ar, o, a, img=None, h="38mm"):
    d = {"en": en, "ar": ar, "options": o, "answer": a}
    if img: d.update(img=img, img_h=h)
    return d
mcq = [
 M("Which of the following is part of the protective gear?", "أيٌّ مما يأتي من معدات الحماية؟", [["Sandals", "صندل"], ["Safety goggles", "نظارات السلامة"], ["Short pants", "بنطلون قصير"], ["Open shoes", "حذاء مفتوح"]], "b"),
 M("“Always read labels before using any chemicals” is the rule of:", "«اقرأ الملصقات دائمًا قبل استعمال أي مواد كيميائية» هي قاعدة:", [["Clean up", "التنظيف"], ["No food", "ممنوع الطعام"], ["ID hazards", "تعرّف على المخاطر"], ["Proper supervision", "الإشراف المناسب"]], "c"),
 M("“Known location of safety equipment and emergency numbers” is the rule of:", "«معرفة مكان معدات السلامة وأرقام الطوارئ» هي قاعدة:", [["Safety first", "السلامة أولًا"], ["Be attentive", "كن منتبهًا"], ["Handle glassware carefully", "التعامل مع الزجاجيات بحذر"], ["ID hazards", "تعرّف على المخاطر"]], "a"),
 M("According to the “Be Attentive” rule, you should not:", "وفق قاعدة «كن منتبهًا»، يجب ألّا:", [["Wear gloves", "ترتدي القفازات"], ["Wash your hands", "تغسل يديك"], ["Read labels", "تقرأ الملصقات"], ["Leave an experiment in progress", "تترك تجربة قيد التنفيذ"]], "d"),
 M("What should be done with glassware that breaks?", "ماذا يجب أن نفعل بالزجاجيات التي تنكسر؟", [["Leave it on the bench", "نتركها على المنضدة"], ["Properly dispose of it", "نتخلّص منها بطريقة صحيحة"], ["Hide it", "نخفيها"], ["Reuse it", "نعيد استعمالها"]], "b"),
 M("All accidents and dangerous events in the lab must be:", "يجب أن تكون جميع الحوادث والأحداث الخطرة في المختبر:", [["Ignored", "مُهمَلة"], ["Cleaned only", "منظَّفة فقط"], ["Reported and recorded", "مُبلَّغًا عنها ومسجَّلة"], ["Kept secret", "سرّية"]], "c"),
 M("How many types of blood collection tubes are listed in the order of draw table?", "كم نوعًا من أنابيب جمع الدم ورد في جدول ترتيب السحب؟", [["4", "4"], ["6", "6"], ["9", "9"], ["12", "12"]], "c"),
 M("The first tube in the order of draw is the:", "الأنبوب الأول في ترتيب السحب هو:", [["Red top (plain) tube", "الأنبوب ذو الغطاء الأحمر (العادي)"], ["Lavender top tube", "الأنبوب البنفسجي"], ["Grey top tube", "الأنبوب الرمادي"], ["Blue tube", "الأنبوب الأزرق"]], "a"),
 M("The additive in the lavender top tube is:", "المادة المضافة في الأنبوب البنفسجي هي:", [["Sodium heparin", "هيبارين الصوديوم"], ["Sodium fluoride", "فلوريد الصوديوم"], ["Thrombin", "الثرومبين"], ["EDTA", "EDTA"]], "d"),
 M("CBC and HbA1c are done using the:", "يُجرى فحصا CBC وHbA1c بواسطة:", [["EDTA (lavender) tube", "أنبوب EDTA (البنفسجي)"], ["Heparin (green) tube", "أنبوب الهيبارين (الأخضر)"], ["Thrombin (orange) tube", "أنبوب الثرومبين (البرتقالي)"], ["Plain (red) tube", "الأنبوب العادي (الأحمر)"]], "a"),
 M("The ESR (Westergren sedimentation rate) tube has a ___ top.", "أنبوب ESR (سرعة ترسيب ويسترغرين) غطاؤه:", [["Blue", "أزرق"], ["Black", "أسود"], ["Green", "أخضر"], ["Yellow", "أصفر"]], "b"),
 M("Glucose tolerance testing and alcohol level use the:", "يُستعمل لفحص تحمّل الكلوكوز ومستوى الكحول:", [["Red top tube", "الأنبوب الأحمر"], ["Blue tube", "الأنبوب الأزرق"], ["Grey top tube", "الأنبوب الرمادي"], ["Orange top tube", "الأنبوب البرتقالي"]], "c"),
 M("PT and PTT are measured using the:", "يُقاس PT وPTT بواسطة:", [["Blue tube (sodium citrate)", "الأنبوب الأزرق (سترات الصوديوم)"], ["Green tube (heparin)", "الأنبوب الأخضر (الهيبارين)"], ["Lavender tube (EDTA)", "الأنبوب البنفسجي (EDTA)"], ["Grey tube (fluoride)", "الأنبوب الرمادي (الفلوريد)"]], "a"),
 M("The orange top tube contains:", "يحتوي الأنبوب البرتقالي على:", [["EDTA", "EDTA"], ["Sodium citrate", "سترات الصوديوم"], ["Thrombin", "الثرومبين"], ["No additive", "لا مادة مضافة"]], "c"),
 M("The serum gel tube contains:", "يحتوي أنبوب الهلام للمصل على:", [["Heparin only", "الهيبارين فقط"], ["A clot activator and serum gel separator", "منشّط تخثّر وفاصل هلامي للمصل"], ["Sodium fluoride", "فلوريد الصوديوم"], ["ACD and SPS", "ACD وSPS"]], "b"),
 M("In red tubes, the clot activators are:", "في الأنابيب الحمراء، منشّطات التخثّر هي:", [["EDTA", "EDTA"], ["Heparin", "الهيبارين"], ["Silica particles", "جزيئات السيليكا"], ["Potassium oxalate", "أوكزالات البوتاسيوم"]], "c"),
 M("Red tubes are used for biochemistry tests that require:", "تُستعمل الأنابيب الحمراء للفحوص الكيموحيوية التي تتطلب:", [["Plasma", "البلازما"], ["Whole blood", "الدم الكامل"], ["Urine", "الإدرار"], ["Serum", "المصل"]], "d"),
 M("Yellow tubes contain:", "تحتوي الأنابيب الصفراء على:", [["SPS and ACD", "SPS وACD"], ["EDTA", "EDTA"], ["Sodium fluoride", "فلوريد الصوديوم"], ["Thrombin", "الثرومبين"]], "a"),
 M("Tubes that have ACD are used for:", "تُستعمل الأنابيب التي تحتوي ACD لـ:", [["Glucose tolerance test", "فحص تحمّل الكلوكوز"], ["Cellular studies, paternity testing, and HLA typing", "الدراسات الخلوية وفحص الأبوّة وتنميط HLA"], ["ESR", "ESR"], ["Liver enzymes", "إنزيمات الكبد"]], "b"),
 M("Sodium citrate in light blue tubes prevents clotting by:", "تمنع سترات الصوديوم في الأنابيب الزرقاء التخثّر عن طريق:", [["Inhibiting thrombin formation", "تثبيط تكوّن الثرومبين"], ["Activating platelets", "تنشيط الصفائح"], ["Binding and removing calcium", "ربط الكالسيوم وإزالته"], ["Breaking down glucose", "تكسير الكلوكوز"]], "c"),
 M("Heparin in green tubes prevents clotting by:", "يمنع الهيبارين في الأنابيب الخضراء التخثّر عن طريق:", [["Inhibiting the formation of thrombin", "تثبيط تكوّن الثرومبين"], ["Removing calcium", "إزالة الكالسيوم"], ["Activating silica", "تنشيط السيليكا"], ["Stopping glycolysis", "إيقاف تحلّل الكلوكوز"]], "a"),
 M("The most common bottles, used primarily for biochemistry tests on whole blood or heparinized plasma, are the:", "القناني الأكثر شيوعًا، وتُستعمل أساسًا للفحوص الكيموحيوية على الدم الكامل أو البلازما المهبرنة، هي:", [["Red tubes", "الحمراء"], ["Grey tubes", "الرمادية"], ["Green tubes", "الخضراء"], ["Yellow tubes", "الصفراء"]], "c"),
 M("A blood film for malaria parasites is prepared from the:", "تُحضَّر المسحة الدموية لطفيليات الملاريا من:", [["Lavender tube", "الأنبوب البنفسجي"], ["Grey tube", "الأنبوب الرمادي"], ["Red tube", "الأنبوب الأحمر"], ["Orange tube", "الأنبوب البرتقالي"]], "a"),
 M("In grey tubes, the antiglycolytic agent is:", "في الأنابيب الرمادية، العامل المضاد لتحلّل الكلوكوز هو:", [["Potassium oxalate", "أوكزالات البوتاسيوم"], ["EDTA", "EDTA"], ["Heparin", "الهيبارين"], ["Sodium fluoride", "فلوريد الصوديوم"]], "d"),
 M("In grey tubes, potassium oxalate acts as:", "في الأنابيب الرمادية، تعمل أوكزالات البوتاسيوم بوصفها:", [["A clot activator", "منشّطًا للتخثّر"], ["An anticoagulant that removes calcium", "مانعًا للتخثّر يزيل الكالسيوم"], ["An antiglycolytic agent", "عاملًا مضادًا لتحلّل الكلوكوز"], ["A gel separator", "فاصلًا هلاميًا"]], "b"),
 dict(topic_en="Picture questions", topic_ar="أسئلة الصور"),
 M("This tube is used for CBC and blood films. Its additive is:", "يُستعمل هذا الأنبوب لـ CBC والمسحات الدموية. مادته المضافة هي:", [["EDTA", "EDTA"], ["Sodium citrate", "سترات الصوديوم"], ["Thrombin", "الثرومبين"], ["Sodium fluoride", "فلوريد الصوديوم"]], "a", "assets/tube-lavender.svg"),
 M("Which test is done with the tube shown?", "أي فحص يُجرى بالأنبوب المبيّن؟", [["Glucose tolerance test", "فحص تحمّل الكلوكوز"], ["PT and PTT (coagulation)", "PT وPTT (التخثّر)"], ["Blood culture", "زرع الدم"], ["CBC", "CBC"]], "b", "assets/tube-blue.svg"),
 M("The tube shown contains sodium fluoride and potassium oxalate. It is the:", "الأنبوب المبيّن يحتوي فلوريد الصوديوم وأوكزالات البوتاسيوم. إنه:", [["Grey top tube", "الأنبوب الرمادي"], ["Black top tube", "الأنبوب الأسود"], ["Green top tube", "الأنبوب الأخضر"], ["Red top tube", "الأنبوب الأحمر"]], "a", "assets/tube-grey.svg"),
 M("The additive in the tube shown is:", "المادة المضافة في الأنبوب المبيّن هي:", [["EDTA", "EDTA"], ["Sodium citrate", "سترات الصوديوم"], ["Heparin (sodium/lithium/ammonium)", "الهيبارين (صوديوم/ليثيوم/أمونيوم)"], ["SPS and ACD", "SPS وACD"]], "c", "assets/tube-green.svg"),
 M("The tube shown (plain tube) is used for:", "يُستعمل الأنبوب المبيّن (الأنبوب العادي) لـ:", [["Biochemistry tests that require serum", "الفحوص الكيموحيوية التي تتطلب المصل"], ["ESR", "ESR"], ["Blood film", "المسحة الدموية"], ["Coagulation factor assays", "مقايسات عوامل التخثّر"]], "a", "assets/tube-red.svg"),
 M("In the order of draw shown, which tube comes second?", "في ترتيب السحب المبيّن، أي أنبوب يأتي ثانيًا؟", [["Green (heparin)", "الأخضر (الهيبارين)"], ["Lavender (EDTA)", "البنفسجي (EDTA)"], ["Black (ESR)", "الأسود (ESR)"], ["Blue (PT)", "الأزرق (PT)"]], "b", "assets/tubes-order.svg", "30mm"),
]
tf = [
 {"en": "Lab experiments may be performed without instructor supervision.", "ar": "يمكن إجراء تجارب المختبر من دون إشراف المدرّس.", "answer": "F"},
 {"en": "Closed shoes are part of the protective gear.", "ar": "الحذاء المغلق جزء من معدات الحماية.", "answer": "T"},
 {"en": "Tasting chemicals in the lab is allowed if they are diluted.", "ar": "يُسمح بتذوّق المواد الكيميائية في المختبر إذا كانت مخفّفة.", "answer": "F"},
 {"en": "Emergency routes in the lab must be kept accessible.", "ar": "يجب أن تبقى طرق الطوارئ في المختبر سالكة.", "answer": "T"},
 {"en": "Each blood collection tube has a different function.", "ar": "لكل أنبوب لجمع الدم وظيفة مختلفة.", "answer": "T"},
 {"en": "The red top tube contains EDTA.", "ar": "يحتوي الأنبوب الأحمر على EDTA.", "answer": "F"},
 {"en": "Both the black (ESR) and blue (PT) tubes contain sodium citrate.", "ar": "يحتوي كلٌّ من الأنبوب الأسود (ESR) والأزرق (PT) على سترات الصوديوم.", "answer": "T"},
 {"en": "The yellow tube additive stabilizes the growth of bacteria.", "ar": "المادة المضافة في الأنبوب الأصفر تُثبّت نمو البكتيريا.", "answer": "T"},
 {"en": "Heparin works by removing calcium.", "ar": "يعمل الهيبارين بإزالة الكالسيوم.", "answer": "F"},
 {"en": "EDTA prevents clotting by removing calcium.", "ar": "يمنع EDTA التخثّر بإزالة الكالسيوم.", "answer": "T"},
 {"en": "Sodium fluoride allows glucose to keep breaking down after collection.", "ar": "يسمح فلوريد الصوديوم باستمرار تكسّر الكلوكوز بعد الجمع.", "answer": "F"},
 {"en": "The serum gel tube contains a clot activator and a serum gel separator.", "ar": "يحتوي أنبوب الهلام على منشّط تخثّر وفاصل هلامي للمصل.", "answer": "T"},
]
traps = [
 {"en": "The black and blue tubes contain different anticoagulants. Correct?", "ar": "الأنبوبان الأسود والأزرق يحتويان مانعَي تخثّر مختلفين. هل هذا صحيح؟", "answer_en": "No. Both contain **sodium citrate**: black → ESR (Westergren), blue → PT/PTT and coagulation.", "answer_ar": "لا. كلاهما يحتوي **سترات الصوديوم**: الأسود ← ESR (ويسترغرين)، والأزرق ← PT/PTT والتخثّر."},
 {"en": "Heparin and EDTA prevent clotting in the same way. Correct?", "ar": "يمنع الهيبارين وEDTA التخثّر بالطريقة نفسها. هل هذا صحيح؟", "answer_en": "No. **Heparin** inhibits thrombin formation; **EDTA** (and citrate, oxalate) remove calcium.", "answer_ar": "لا. **الهيبارين** يثبّط تكوّن الثرومبين؛ أما **EDTA** (والسترات والأوكزالات) فتزيل الكالسيوم."},
 {"en": "In the grey tube, sodium fluoride is the anticoagulant. Correct?", "ar": "في الأنبوب الرمادي، فلوريد الصوديوم هو مانع التخثّر. هل هذا صحيح؟", "answer_en": "No. Sodium fluoride is the **antiglycolytic** agent; potassium oxalate is the anticoagulant.", "answer_ar": "لا. فلوريد الصوديوم هو العامل **المضاد لتحلّل الكلوكوز**؛ أما أوكزالات البوتاسيوم فهي مانع التخثّر."},
 {"en": "Red tubes contain an anticoagulant. Correct?", "ar": "تحتوي الأنابيب الحمراء على مانع تخثّر. هل هذا صحيح؟", "answer_en": "No. They contain silica particles that act as **clot activators** — the tube gives serum.", "answer_ar": "لا. تحتوي جزيئات السيليكا التي تعمل **منشّطات للتخثّر** — فالأنبوب يعطي المصل."},
 {"en": "Yellow tubes and the serum gel tube contain the same additive. Correct?", "ar": "تحتوي الأنابيب الصفراء وأنبوب هلام المصل المادة المضافة نفسها. هل هذا صحيح؟", "answer_en": "No. Yellow top → ACD/SPS (cultures, HLA, paternity); serum gel tube → clot activator + gel separator.", "answer_ar": "لا. الأصفر ← ACD/SPS (المزارع، HLA، الأبوّة)؛ أنبوب هلام المصل ← منشّط تخثّر + فاصل هلامي."},
 {"en": "The green tube is used for hematology tests like CBC. Correct?", "ar": "يُستعمل الأنبوب الأخضر لفحوص الدم مثل CBC. هل هذا صحيح؟", "answer_en": "No. Green (heparin) → biochemistry/chemistry tests; CBC → lavender (EDTA).", "answer_ar": "لا. الأخضر (الهيبارين) ← الفحوص الكيموحيوية؛ أما CBC ← البنفسجي (EDTA)."},
]
important = [
 {"en": "List the lab safety protocols.", "ar": "عدّد بروتوكولات السلامة في المختبر.", "answer_en": "Use protective gear (goggles, lab coat, gloves, long pants, closed shoes); proper supervision; ID hazards; safety first; no food; be attentive; handle glassware carefully; clean up and wash hands.", "answer_ar": "استعمال معدات الحماية (نظارات، صدرية، قفازات، بنطلون طويل، حذاء مغلق)؛ الإشراف المناسب؛ التعرّف على المخاطر؛ السلامة أولًا؛ ممنوع الطعام؛ الانتباه؛ التعامل مع الزجاجيات بحذر؛ التنظيف وغسل اليدين."},
 {"en": "Write the order of draw with the stopper colour of each tube.", "ar": "اكتب ترتيب السحب مع لون غطاء كل أنبوب.", "answer_en": "1 Plain (red), 2 EDTA (lavender), 3 Heparin (green), 4 ESR (black), 5 Glucose (grey), 6 PT (blue), 7 Serum (yellow), 8 Thrombin (orange), 9 Gel yellow (serum gel tube).", "answer_ar": "1 العادي (أحمر)، 2 EDTA (بنفسجي)، 3 الهيبارين (أخضر)، 4 ESR (أسود)، 5 الكلوكوز (رمادي)، 6 PT (أزرق)، 7 المصل (أصفر)، 8 الثرومبين (برتقالي)، 9 الهلام الأصفر (أنبوب هلام المصل)."},
 {"en": "Compare the mechanism of the anticoagulants EDTA, sodium citrate, heparin and potassium oxalate.", "ar": "قارن آلية عمل موانع التخثّر: EDTA، سترات الصوديوم، الهيبارين، وأوكزالات البوتاسيوم.", "answer_en": "EDTA, sodium citrate and potassium oxalate remove (bind) calcium; heparin inhibits the formation of thrombin.", "answer_ar": "EDTA وسترات الصوديوم وأوكزالات البوتاسيوم تزيل الكالسيوم (تربطه)؛ أما الهيبارين فيثبّط تكوّن الثرومبين."},
 {"en": "What is the role of sodium fluoride in the grey tube, and what tests use it?", "ar": "ما دور فلوريد الصوديوم في الأنبوب الرمادي، وما الفحوص التي تستعمله؟", "answer_en": "It is an antiglycolytic agent: no further breakdown of glucose after collection. Used for lactate, glucose and glucose tolerance test (and alcohol level).", "answer_ar": "عامل مضاد لتحلّل الكلوكوز: يمنع استمرار تكسّر الكلوكوز بعد الجمع. يُستعمل للاكتات والكلوكوز وفحص تحمّل الكلوكوز (ومستوى الكحول)."},
 {"en": "Give the additive and two uses of the red, lavender and light blue tubes.", "ar": "اذكر المادة المضافة واستعمالين لكل من الأنبوب الأحمر والبنفسجي والأزرق الفاتح.", "answer_en": "Red: silica clot activator (usually no additive) — serum biochemistry, blood bank serology. Lavender: EDTA — CBC, blood film for malaria. Light blue: sodium citrate — PT, APTT/PTT.", "answer_ar": "الأحمر: منشّط تخثّر من السيليكا (عادةً بلا مادة مضافة) — كيمياء المصل، مصليات بنك الدم. البنفسجي: EDTA — CBC، المسحة الدموية للملاريا. الأزرق الفاتح: سترات الصوديوم — PT، APTT/PTT."},
]

data = {"meta": {
  "subject_en": "Clinical Enzymology", "subject_ar": "الإنزيمات السريرية", "short_ar": "انزيمات سريرية",
  "unit_en": "Lab 1", "unit_ar": "العملي 1", "unit_label": "LAB", "unit_no": "1",
  "title_en": "Lab Safety and Blood Collecting Tubes", "title_ar": "السلامة في المختبر وأنابيب جمع الدم",
  "kind": "Laboratories — عملي", "stage": "The fourth stage — الرابعة", "instructor": "د. هشام"},
 "blocks": blocks, "questions": {"mcq": mcq, "tf": tf, "traps": traps, "important": important}}
from collections import Counter
print(sum(1 for q in mcq if "answer" in q), Counter(q["answer"] for q in mcq if "answer" in q))
json.dump(data, open("/home/user/-/enzymology-lab1-safety-tubes/lecture.json", "w"), ensure_ascii=False, indent=1)

```
