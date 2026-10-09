"""Lab 1 content, in the order of the original slides.

Markup:  **x** term · ==x== lecturer's red emphasis · ++x++ lecturer's blue emphasis
         *x* scientific name (italic) · `x` Latin run inside Arabic
         [[cut]] / [[قطع]] text cut off in the original file · [[?]] unreadable in the original
"""

META = {
    "subject_en": "Diagnostic Microbiology", "subject_ar": "الأحياء المجهرية التشخيصية",
    "stage_en": "The fourth stage", "stage_ar": "المرحلة الرابعة",
    "type_en": "Practical (Laboratories)", "type_ar": "عملي (المختبرات)",
    "lab_en": "Lab: 1", "lab_ar": "المختبر 1",
    "title_en": "Rules and biosafety levels", "title_ar": "القواعد ومستويات السلامة الحيوية",
    "doctor_ar": "د. ذهب",
}

# Each block: (kind, payload). Kinds are rendered by build4.py.
B = []
add = lambda k, **kw: B.append((k, kw))

# ---------------------------------------------------------------- slide 1
add("labtitle")

# ---------------------------------------------------------------- slide 2
add("section", n=1, en="Biosafety levels", ar="مستويات السلامة الحيوية", slide=2)
add("side", img="labsafety.jpg", w=40, cap_en="“Lab Safety”", cap_ar="«سلامة المختبر»", items=[
    ("==Biosafety levels==: They are principles and application used to protect laboratory workers and the surrounding environment from exposure to danger while working with living organisms.",
     "==مستويات السلامة الحيوية==: هي مبادئ وتطبيقات تُستخدم لحماية العاملين في المختبر والبيئة المحيطة من التعرّض للخطر في أثناء العمل مع الكائنات الحية."),
    ("==It aims to==: provide the highest level of protection and the lowest range of exposure.",
     "==وتهدف إلى==: توفير أعلى مستوى من الحماية وأدنى مدى من التعرّض."),
])

# ---------------------------------------------------------------- slide 3
add("h2", en="Risk groups", ar="مجموعات الخطورة", slide=3)
add("p", en="==Risk groups:== are used to assess risk, determine its source and how to deal with it, includes 4 groups:",
    ar="==مجموعات الخطورة:== تُستخدم لتقييم الخطر وتحديد مصدره وكيفية التعامل معه، وتشمل 4 مجموعات:", keep=True)
add("rgtable",
    head=[("The level of biological safety for each group", "مستوى السلامة الحيوية لكل مجموعة"),
          ("Risk groups", "مجموعات الخطورة"), ("", "")],
    rows=[
        ("Biosafety level 1", "مستوى السلامة الحيوية 1",
         "(==Minimal== risk) Risk group 1", "مجموعة الخطورة 1 (خطورة ==ضئيلة==)",
         "==Non-pathogenic== factors in healthy people and adults (with little or no risk). *E. coli*, *Bacillus subtilis*",
         "عوامل ==غير مُمرِضة== للأشخاص الأصحاء والبالغين (خطورتها قليلة أو معدومة). `*E. coli*`، `*Bacillus subtilis*`", "1"),
        ("Biosafety level 2", "مستوى السلامة الحيوية 2",
         "(==Moderate== risk) Risk group 2", "مجموعة الخطورة 2 (خطورة ==متوسطة==)",
         "Factors related to ==human infection== and ==treatment is possible== in this case (moderate risk and ==limited== risk of spread). *E. coli* pathogenic strain, *Brucella* spp., *Salmonella* spp.",
         "عوامل مرتبطة ==بإصابة الإنسان بالعدوى==، و==العلاج ممكن== في هذه الحالة (خطورة متوسطة وخطر انتشار ==محدود==). السلالة المُمرِضة من `*E. coli*`، و`*Brucella* spp.`، و`*Salmonella* spp.`", "2"),
        ("Biosafety level 3", "مستوى السلامة الحيوية 3",
         "(==High== risk) Risk group 3", "مجموعة الخطورة 3 (خطورة ==عالية==)",
         "Factors that cause serious and fatal infections to humans and their ==treatment is not easy==, especially for immunosuppressed persons (with a high risk for individuals). *Salmonella typhi*. *Mycobacterium tuberculosis*.",
         "عوامل تسبّب للإنسان أنواع عدوى خطيرة ومميتة، و==علاجها ليس سهلًا==، ولا سيّما لدى الأشخاص المثبَّطين مناعيًا (خطورة عالية على الأفراد). `*Salmonella typhi*`. `*Mycobacterium tuberculosis*`.", "3"),
        ("Biosafety level 4", "مستوى السلامة الحيوية 4",
         "(==Extreme== risk) Risk group 4", "مجموعة الخطورة 4 (خطورة ==قصوى==)",
         "Factors that are fatal to humans are easily transmitted from … [[cut]]",
         "عوامل مميتة للإنسان، وتنتقل بسهولة من … [[قطع]]", "4"),
    ])
add("clarify",
    en="*spp.* is the abbreviation of “species” (plural): it refers to several species within the same genus.",
    ar="`spp.` اختصار لكلمة `species` بصيغة الجمع، ويعني عدة أنواع تابعة للجنس نفسه، مثل `*Salmonella* spp.` أي أنواع السالمونيلا.")

# ---------------------------------------------------------------- slide 4
add("section", n=2, en="Biohazard symbol", ar="رمز الخطر البيولوجي", slide=4)
add("p", en="==Biohazard symbol==: it is used to warn people of the potential for the presence of dangerous biological materials such as:",
    ar="==رمز الخطر البيولوجي==: يُستخدم لتحذير الناس من احتمال وجود مواد بيولوجية خطرة، مثل:", keep=True)
add("short", items=[
    ("Cultures of pathogens.", "مزارع المُمرِضات."),
    ("Human Blood and Tissue.", "دم الإنسان وأنسجته."),
    ("Corridors leading to the laboratories.", "الممرات المؤدية إلى المختبرات."),
])
add("symbols")

# ---------------------------------------------------------------- slides 5–9
add("section", n=3, en="Laboratory safety considerations", ar="اعتبارات السلامة في المختبر", slide=5)
RULES = [
    ("Wear protective clothing (clean lab coat – ==Gloves== - ==mask== – safety ==glasses==).",
     "ارتدِ الملابس الواقية (معطف مختبر نظيف – ==القفازات== – ==الكمامة== – ==نظارات== السلامة)."),
    ("Avoid touching objects (pencils, cell phones, door handles, e.g.) while wearing gloves. And pencils, labels, or any other materials should never be placed in your mouth.",
     "تجنّب لمس الأشياء (مثل الأقلام والهواتف المحمولة ومقابض الأبواب) في أثناء ارتداء القفازات. ولا يجوز أبدًا وضع الأقلام أو الملصقات أو أي مواد أخرى في فمك."),
    ("Do not eat food or drink water in the lab. Do not use lab glassware as food or water containers.",
     "لا تأكل الطعام ولا تشرب الماء في المختبر. ولا تستخدم الأدوات الزجاجية المختبرية أوعيةً للطعام أو الماء."),
    ("Long hair must be tied back or covered to minimize fire hazard or contamination of experiment.",
     "يجب ربط الشعر الطويل إلى الخلف أو تغطيته لتقليل خطر الحريق أو تلوّث التجربة."),
    ("Do not take any cultures out of the lab for any reason, all cultures should be handled as potentially pathogenic.",
     "لا تُخرج أي مزارع من المختبر لأي سبب كان؛ إذ يجب التعامل مع جميع المزارع على أنها يُحتمل أن تكون مُمرِضة."),
    ("Wash hands after working with infectious materials.",
     "اغسل يديك بعد العمل بالمواد المُعدية."),
    ("Disinfect all instruments immediately after use.",
     "طهّر جميع الأدوات فور استخدامها."),
    ("Disinfect all contaminated waste before discarding.",
     "طهّر جميع النفايات الملوّثة قبل التخلّص منها."),
]
# rules grouped exactly as on the slides, each group with the slide's own picture
for nums, img, slide in [((1,), "ppe.jpg", 5), ((2, 3), "nofood.jpg", 6), ((4, 5), "cultures.jpg", 7),
                         ((6,), "handwash.jpg", 8), ((7, 8), "disinfect.jpg", 9)]:
    add("rules", nums=nums, img=img, slide=slide, items=[RULES[n - 1] for n in nums])

# ---------------------------------------------------------------- slides 10–11
add("section", n=4, en="Definitions", ar="تعريفات", slide=10, editorial=True)
DEFS = [
    ("Sterilization:", "التعقيم:",
     "is the complete killing or removal of all living organisms such as cell spore [[rev]], viruses, fungi, ….",
     "هو القتل أو الإزالة الكاملة لجميع الكائنات الحية، مثل الخلايا والأبواغ [[rev]]، والفيروسات، والفطريات، …."),
    ("Disinfection:", "التطهير:",
     "the destruction or removal of pathogens ++but not bacterial spores++, usually used only on inanimate objects.",
     "تدمير المُمرِضات أو إزالتها ++ولكن ليس الأبواغ البكتيرية++، ويُستخدم عادةً على الأجسام غير الحيّة فقط."),
    ("Antiseptics:", "المطهِّرات الموضعية:",
     "chemicals applied to ++body surfaces++ to destroy or inhibit pathogens.",
     "مواد كيميائية تُطبَّق على ++أسطح الجسم++ لتدمير المُمرِضات أو تثبيطها."),
    ("Decontamination:", "إزالة التلوّث:",
     "the mechanical removal of most microbes by using washing, heat or disinfectants.",
     "الإزالة الميكانيكية لمعظم الميكروبات باستخدام الغسل أو الحرارة أو المطهِّرات."),
    ("Biological laboratory:", "المختبر البيولوجي:",
     "A facility within which microorganisms, their components or their derivatives are collected, handled and/or stored.",
     "منشأة تُجمَع فيها الكائنات الحية الدقيقة أو مكوّناتها أو مشتقّاتها، ويُتعامَل معها و/أو تُخزَّن."),
    ("Bio risk:", "الخطر البيولوجي:",
     "The probability or chance that a particular adverse event (accidental infection or loss, theft, misuse, diversion or intentional release), possibly leading to harm.",
     "احتمال أو فرصة وقوع حدث ضارّ معيّن (عدوى عرضية، أو فقدان، أو سرقة، أو سوء استخدام، أو تحويل، أو إطلاق متعمَّد)، قد يؤدي إلى الضرر."),
    ("Bio risk assessment:", "تقييم الخطر البيولوجي:",
     "The process to identify acceptable and unacceptable risks (embracing biosafety risks (risks of accidental infection) and laboratory biosecurity risks (risks of unauthorized access, loss, theft, misuse, diversion or intentional release)) and their potential consequences.",
     "عملية تحديد المخاطر المقبولة وغير المقبولة (وتشمل مخاطر السلامة الحيوية (مخاطر العدوى العرضية) ومخاطر الأمن الحيوي المختبري (مخاطر الوصول غير المصرَّح به، أو الفقدان، أو السرقة، أو سوء الاستخدام، أو التحويل، أو الإطلاق المتعمَّد))، وعواقبها المحتملة."),
]
NOTES = {0: ("Review: “cell spore” is kept as written in the original slide; the Arabic reads it as “cells and spores” — to be confirmed with the lecturer.",
              "للمراجعة: أُبقيت عبارة `cell spore` كما وردت في الشريحة الأصلية، وتُرجمت «الخلايا والأبواغ» — يُرجى التأكد من المحاضر.")}
for i, d in enumerate(DEFS):
    n = NOTES.get(i, ("", ""))
    add("def", term_en=d[0], term_ar=d[1], en=d[2], ar=d[3], slide=10 if i < 4 else 11, note_en=n[0], note_ar=n[1])

# ---------------------------------------------------------------- slide 12
add("section", n=5, en="Biosafety Cabinet", ar="خزانة السلامة الحيوية", slide=12)
add("cabinet")
LABELS = [  # left→right, top row then bottom row; (en, ar, partly_hidden)
    ("Class I biosafety cabinet", "خزانة السلامة الحيوية من الصنف الأول", False),
    ("Mini B[…] cabinet", "خزانة […] مصغّرة", True),
    ("[…] Biosafety cabinet", "خزانة سلامة حيوية […]", True),
    ("[…] Cabinet", "خزانة […]", True),
    ("[…]SF Biosafety Cabinet", "خزانة سلامة حيوية […]", True),
    ("Class III Biosafety Cabinet", "خزانة السلامة الحيوية من الصنف الثالث", False),
    ("Ducted and Ductless Fume Hood", "خزانة سحب الأبخرة ذات المجرى وعديمة المجرى", False),
    ("Laminar flow Cabinet", "خزانة التدفّق الصفائحي", False),
    ("PCR Cabinet", "خزانة `PCR` (تفاعل البلمرة المتسلسل)", False),
    ("Autoclave", "جهاز التعقيم بالبخار المضغوط (الأوتوكليف)", False),
    ("Incubator", "الحاضنة", False),
]
# marker positions on the cropped picture, as % of width / height
MARKS = [(9, 44), (26.7, 44), (40.7, 44), (56, 44), (71.3, 44), (90.7, 44),
         (17, 97.6), (42, 97.6), (57.3, 97.6), (73.7, 97.6), (88.3, 97.6)]
