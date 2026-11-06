---
source: BIOS-Obsidian/tools/scripts/bac6/b6q.py
handouts: [bacteriology-lec6-culture-media]
saved: 2026-11-06
tags: [bios, code]
---
# bac6/b6q.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#bacteriology-lec6-culture-media|bacteriology-lec6-culture-media]]

```python
A = lambda f: "assets/" + f
mcq = [
 {"topic_en": "Constituents of culture media", "topic_ar": "مكوّنات الأوساط الزرعية"},
 Q("Culture media are required to:", "الأوساط الزرعية مطلوبة لـ:", O(("Isolate the bacteria from the clinical specimens", "عزل البكتيريا من العيّنات السريرية"), ("Stain the bacteria", "صبغ البكتيريا"), ("Kill the bacteria", "قتل البكتيريا"), ("Count red blood cells", "عدّ الكريات الحمر")), "a"),
 Q("Peptone is:", "الببتون هو:", O(("A solidifying agent", "عامل تصليب"), ("A complex mixture of partially digested proteins", "خليط معقّد من بروتينات مهضومة جزئيًا"), ("A pH indicator", "دليل pH"), ("An antibiotic", "مضاد حيوي")), "b"),
 Q("Peptone is usually prepared by digestion with:", "يُحضَّر الببتون عادةً بالهضم بواسطة:", O(("Amylase", "الأميليز"), ("Lipase", "الليبيز"), ("Pepsin", "البيبسين"), ("DNase", "الدي إن إيز")), "c"),
 Q("Agar is used for:", "يُستعمل الأكار لـ:", O(("Providing nitrogen", "توفير النتروجين"), ("Killing contaminants", "قتل الملوّثات"), ("Changing colour", "تغيير اللون"), ("Solidifying the culture media", "تصليب الأوساط الزرعية")), "d"),
 Q("Agar is prepared from:", "يُحضَّر الأكار من:", O(("Red algae (Gelidium and Gracilaria)", "الطحالب الحمراء (Gelidium وGracilaria)"), ("Beef", "لحم البقر"), ("Baker's yeast", "خميرة الخبّاز"), ("Sheep blood", "دم الأغنام")), "a"),
 Q("Molten agar is poured into Petri dishes when its temperature comes down to:", "يُصبّ الأكار المنصهر في أطباق بتري عندما تنخفض حرارته إلى:", O(("100°C", "100°م"), ("45°C", "45°م"), ("4°C", "4°م"), ("121°C", "121°م")), "b"),
 Q("After pouring, agar plates are allowed to set for:", "بعد الصبّ تُترك أطباق الأكار لتتصلّب:", O(("2 minutes", "دقيقتين"), ("24 hours", "24 ساعة"), ("20 minutes", "20 دقيقة"), ("1 week", "أسبوعًا")), "c"),
 Q("Malt extract consists of about 50%:", "يتكوّن مستخلص الشعير من حوالي 50%:", O(("Glucose", "غلوكوز"), ("Protein", "بروتين"), ("Starch", "نشا"), ("Maltose", "مالتوز")), "d"),
 Q("The blood most commonly used in enriched media is:", "الدم الأكثر استعمالًا في الأوساط المُغناة:", O(("Sheep blood", "دم الأغنام"), ("Fish blood", "دم الأسماك"), ("Chicken blood", "دم الدجاج"), ("Snake blood", "دم الأفاعي")), "a"),
 Q("Yeast extract is prepared from:", "يُحضَّر مستخلص الخميرة من:", O(("Red algae", "الطحالب الحمراء"), ("Washed cells of Baker's yeast", "خلايا خميرة الخبّاز المغسولة"), ("Beef", "لحم البقر"), ("Soya flour", "طحين الصويا")), "b"),
 {"topic_en": "Types of culture media", "topic_ar": "أنواع الأوساط الزرعية"},
 Q("Based on consistency, culture media are:", "حسب القوام تكون الأوساط الزرعية:", O(("Selective and differential", "انتقائية وتفريقية"), ("Simple and complex", "بسيطة ومعقّدة"), ("Liquid, semisolid and solid", "سائلة وشبه صلبة وصلبة"), ("Aerobic and anaerobic", "هوائية ولاهوائية")), "c"),
 Q("Media prepared from pure chemical substances with exact known composition are:", "الأوساط المحضّرة من مواد كيميائية نقية بتركيب معروف بدقّة هي:", O(("Enriched media", "المُغناة"), ("Transport media", "أوساط النقل"), ("Routine media", "الروتينية"), ("Defined or synthetic media", "المحدّدة أو الصناعية")), "d"),
 Q("Nutrient broth / nutrient agar is an example of:", "المرق / الأكار المغذّي مثال على:", O(("Simple media", "الأوساط البسيطة"), ("Selective media", "الأوساط الانتقائية"), ("Indicator media", "الأوساط الدالّة"), ("Synthetic media", "الأوساط الصناعية")), "a"),
 Q("Chocolate agar contains:", "يحتوي أكار الشوكولاتة:", O(("Whole blood", "دمًا كاملًا"), ("Lysed blood", "دمًا متحلّلًا"), ("Bile salts", "أملاح الصفراء"), ("High salt", "ملحًا عاليًا")), "b"),
 Q("Enriched media are used for:", "تُستعمل الأوساط المُغناة لـ:", O(("Suppressing all bacteria", "تثبيط كل البكتيريا"), ("Transporting specimens", "نقل العيّنات"), ("Isolation of fastidious bacteria", "عزل البكتيريا صعبة النمو"), ("Staining", "الصبغ")), "c"),
 {"topic_en": "Selective and indicator media", "topic_ar": "الأوساط الانتقائية والدالّة"},
 Q("Mannitol salt agar is used for the recovery of:", "يُستعمل أكار الملح والمانيتول لاستعادة:", O(("Salmonella", "السالمونيلا"), ("E. coli", "الإشريكية القولونية"), ("Streptococci", "المكوّرات العقدية"), ("Staphylococci", "المكوّرات العنقودية")), "d"),
 Q("MacConkey agar contains bile salts to allow growth of:", "يحتوي أكار ماكونكي أملاح الصفراء للسماح بنمو:", O(("Bile-tolerant bacteria only", "البكتيريا المتحمّلة للصفراء فقط"), ("Gram-positive cocci", "المكوّرات الموجبة لغرام"), ("Fungi", "الفطريات"), ("All bacteria", "كل البكتيريا")), "a"),
 Q("The pH indicator in MacConkey agar is:", "دليل pH في أكار ماكونكي هو:", O(("Phenol red", "الأحمر الفينولي"), ("Neutral red", "الأحمر المتعادل"), ("Bromothymol blue", "أزرق البروموثايمول"), ("Crystal violet", "البنفسجي البلّوري")), "b"),
 Q("On MacConkey agar, E. coli forms:", "على أكار ماكونكي تكوّن الإشريكية القولونية:", O(("Pale yellow colonies", "مستعمرات صفراء شاحبة"), ("Black colonies", "مستعمرات سوداء"), ("Pink colonies", "مستعمرات وردية"), ("No colonies", "لا مستعمرات")), "c"),
 Q("Non-lactose fermenting Salmonella on MacConkey forms:", "السالمونيلا غير المخمّرة للاكتوز على ماكونكي تكوّن:", O(("Pink colonies", "مستعمرات وردية"), ("Green colonies", "مستعمرات خضراء"), ("Red colonies with halo", "مستعمرات حمراء بهالة"), ("Pale yellow colonies", "مستعمرات صفراء شاحبة")), "d"),
 Q("MacConkey agar is:", "أكار ماكونكي:", O(("Both a selective medium and an indicator medium", "وسط انتقائي ودالّ معًا"), ("A simple medium only", "وسط بسيط فقط"), ("A transport medium", "وسط نقل"), ("An enriched medium for fastidious bacteria", "وسط مُغنى للبكتيريا صعبة النمو")), "a"),
 Q("Bile salts and crystal violet in indicator media suppress:", "أملاح الصفراء والبنفسجي البلّوري في الأوساط الدالّة تثبّط:", O(("Gram-negative bacilli", "العصيات السالبة لغرام"), ("Most Gram-positive microorganisms", "معظم الأحياء الموجبة لغرام"), ("Salmonella", "السالمونيلا"), ("Lactose fermenters", "مخمّرات اللاكتوز")), "b"),
 {"topic_en": "Picture questions", "topic_ar": "أسئلة الصور"},
 Q("In this figure, plate C (red) is:", "في هذا الشكل، الطبق C (الأحمر) هو:", O(("Nutrient agar", "الأكار المغذّي"), ("Chocolate agar", "أكار الشوكولاتة"), ("Blood agar", "أكار الدم"), ("Peptone water", "ماء الببتون")), "c", img=A("media-fig1.png"), img_h="30mm"),
 Q("In this figure, D (brown plate) is:", "في هذا الشكل، D (الطبق البنّي) هو:", O(("Blood agar", "أكار الدم"), ("Nutrient agar", "الأكار المغذّي"), ("MacConkey agar", "أكار ماكونكي"), ("Chocolate agar", "أكار الشوكولاتة")), "d", img=A("media-fig1.png"), img_h="30mm"),
 Q("Bottle B in this figure (broth over agar) is a:", "القنينة B في هذا الشكل (مرق فوق أكار) هي:", O(("Biphasic medium", "وسط ثنائي الطور"), ("Monophasic medium", "وسط أحادي الطور"), ("Thioglycollate broth", "مرق الثايوغلايكوليت"), ("Robertson's cooked meat medium", "وسط روبرتسون للحم المطبوخ")), "a", img=A("media-fig2.png"), img_h="36mm"),
]

tf = [
 TF("Distilled water or low-mineral potable water is suitable for media preparation.", "الماء المقطّر أو ماء الشرب قليل المعادن مناسب لتحضير الأوساط.", "T"),
 TF("Agar provides the main nutrition for bacteria.", "الأكار يوفّر التغذية الرئيسية للبكتيريا.", "F"),
 TF("Agar melts after boiling and jellifies after cooling.", "يذوب الأكار بعد الغليان ويتهلّم بعد التبريد.", "T"),
 TF("Agar media are sterilized in an autoclave.", "تُعقَّم أوساط الأكار في المؤصدة.", "T"),
 TF("Meat extract is usually made from beef.", "يُصنع مستخلص اللحم عادةً من لحم البقر.", "T"),
 TF("Horse, ox or human blood can also be used in enriched media.", "يمكن استعمال دم الحصان أو الثور أو الإنسان أيضًا في الأوساط المُغناة.", "T"),
 TF("Blood agar contains lysed blood.", "يحتوي أكار الدم دمًا متحلّلًا.", "F"),
 TF("Transport media and anaerobic media are types of routine laboratory media.", "أوساط النقل والأوساط اللاهوائية من أنواع الأوساط المختبرية الروتينية.", "T"),
 TF("Selective media facilitate growth of all bacteria equally.", "الأوساط الانتقائية تسهّل نمو كل البكتيريا بالتساوي.", "F"),
 TF("Mannitol salt agar contains a high NaCl concentration.", "يحتوي أكار الملح والمانيتول تركيزًا عاليًا من NaCl.", "T"),
 TF("Lactose-fermenting bacteria produce acid on MacConkey agar.", "البكتيريا المخمّرة للاكتوز تنتج حامضًا على أكار ماكونكي.", "T"),
 TF("Salmonella forms pink colonies on MacConkey agar.", "تكوّن السالمونيلا مستعمرات وردية على أكار ماكونكي.", "F"),
]

traps = [
 TR("Blood agar vs chocolate agar?", "أكار الدم مقابل أكار الشوكولاتة؟",
    "Blood agar contains whole blood; chocolate agar contains lysed blood — both are enriched media.", "أكار الدم فيه دم كامل؛ وأكار الشوكولاتة فيه دم متحلّل — وكلاهما وسط مُغنى."),
 TR("Is MacConkey only selective?", "هل ماكونكي انتقائي فقط؟",
    "No — bile salts make it selective and lactose + neutral red make it an indicator; it is both.", "لا — أملاح الصفراء تجعله انتقائيًا واللاكتوز مع الأحمر المتعادل يجعله دالًّا؛ فهو الاثنان."),
 TR("Pink or pale colonies — which is E. coli?", "مستعمرات وردية أم شاحبة — أيّها الإشريكية؟",
    "E. coli (lactose fermenter) → pink; Salmonella (non-lactose fermenter) → pale yellow.", "الإشريكية (مخمّرة للاكتوز) ← وردية؛ السالمونيلا (غير مخمّرة) ← صفراء شاحبة."),
 TR("Agar: nutrient or solidifier?", "الأكار: مغذٍّ أم مصلِّب؟",
    "Solidifier — nutrients come from peptone, extracts, blood and serum.", "مصلِّب — والمغذّيات تأتي من الببتون والمستخلصات والدم والمصل."),
 TR("Pour molten agar at boiling point?", "هل يُصبّ الأكار المنصهر وهو يغلي؟",
    "No — wait until it cools to 45°C, then pour and let it set 20 minutes.", "لا — انتظر حتى يبرد إلى 45°م ثم اصبب واتركه يتصلّب 20 دقيقة."),
 TR("Routine media vs synthetic media?", "الأوساط الروتينية مقابل الصناعية؟",
    "Routine: from nutrients such as meat extract and peptone; synthetic: from pure chemicals with exactly known composition.", "الروتينية: من مغذّيات مثل مستخلص اللحم والببتون؛ الصناعية: من مواد كيميائية نقية بتركيب معروف بدقّة."),
]

important = [
 IM("Pretest: How can you cultivate the bacteria in the lab?", "الاختبار القبلي: كيف تزرع البكتيريا في المختبر؟",
    "By inoculating the clinical specimen onto suitable culture media (prepared from water, electrolytes, peptone, agar, extracts and blood or serum and sterilized in an autoclave), choosing simple, enriched, selective or indicator media according to the expected pathogen; the isolated colonies are then identified by biochemical tests.",
    "بزرع العيّنة السريرية على أوساط زرعية مناسبة (محضّرة من الماء والإلكتروليتات والببتون والأكار والمستخلصات والدم أو المصل ومعقّمة بالمؤصدة)، واختيار وسط بسيط أو مُغنى أو انتقائي أو دالّ حسب الممرض المتوقّع؛ ثم تُشخَّص المستعمرات المعزولة بالفحوص الكيموحيوية."),
 IM("Posttest 1: What are the constituents of culture media?", "الاختبار البعدي 1: ما مكوّنات الأوساط الزرعية؟",
    "Water, electrolyte (NaCl), peptone, agar, meat extract, yeast extract, malt extract, and blood and serum.",
    "الماء، الإلكتروليت (NaCl)، الببتون، الأكار، مستخلص اللحم، مستخلص الخميرة، مستخلص الشعير، والدم والمصل."),
 IM("Posttest 2: Which are the common pathogenic bacteria isolated from the urinary tract?", "الاختبار البعدي 2: ما البكتيريا الممرضة الشائعة المعزولة من المجاري البولية؟",
    "BIOS answer (not in the sheet): mostly Gram-negative bacilli — Escherichia coli (the commonest), Klebsiella, Proteus, Pseudomonas aeruginosa — and Gram-positive cocci such as Enterococcus faecalis, Staphylococcus saprophyticus and Staphylococcus aureus. They are cultured on blood agar and MacConkey agar.",
    "جواب BIOS (غير موجود في الورقة): أغلبها عصيات سالبة لغرام — الإشريكية القولونية (الأشيع)، الكليبسيلا، المتقلّبة، الزائفة الزنجارية — ومكوّرات موجبة لغرام مثل المكوّرات المعوية البرازية والعنقودية الرمّية والعنقودية الذهبية. وتُزرع على أكار الدم وأكار ماكونكي."),
 IM("Describe agar and how agar media are prepared.", "صف الأكار وكيف تُحضَّر أوساط الأكار.",
    "Agar solidifies culture media; it is a powder that melts in water after boiling and jellifies after cooling, prepared from the cell wall of red algae (Gelidium, Gracilaria). Preparation: add agar powder to water, dissolve, sterilize in an autoclave, cool to 45°C, pour into Petri dishes and let it set for 20 minutes.",
    "الأكار يصلّب الأوساط الزرعية؛ مسحوق يذوب في الماء بعد الغليان ويتهلّم بعد التبريد، يُحضَّر من جدار خلايا الطحالب الحمراء (Gelidium وGracilaria). التحضير: أضف المسحوق للماء وأذبه، وعقّمه بالمؤصدة، وبرّده إلى 45°م، واصببه في أطباق بتري واتركه يتصلّب 20 دقيقة."),
 IM("Classify culture media.", "صنّف الأوساط الزرعية.",
    "A. By consistency: liquid (broth), semisolid, solid. B. By growth requirements: 1. routine laboratory media (simple/basal, enriched, enrichment broth, selective, differential, transport, anaerobic); 2. defined or synthetic media (simple and complex synthetic) from pure chemicals with exact composition.",
    "أ. حسب القوام: سائلة (مرق)، شبه صلبة، صلبة. ب. حسب متطلّبات النمو: 1. أوساط مختبرية روتينية (بسيطة/أساسية، مُغناة، مرق إغناء، انتقائية، تفريقية، نقل، لاهوائية)؛ 2. أوساط محدّدة أو صناعية (بسيطة ومعقّدة) من مواد نقية بتركيب دقيق."),
 IM("Explain selective and indicator media with MacConkey agar as an example.", "اشرح الأوساط الانتقائية والدالّة مع أكار ماكونكي مثالًا.",
    "Selective media favour some bacteria and suppress others (mannitol salt agar for staphylococci, MacConkey with bile salts for bile-tolerant bacteria, antibiotics). Indicator media detect pathogens by sugar fermentation → acid → pH indicator colour change: MacConkey has lactose and neutral red; E. coli ferments lactose → pink colonies, Salmonella does not → pale yellow. Bile salts and crystal violet suppress Gram-positives, so MacConkey is both selective and indicator.",
    "الأوساط الانتقائية تسهّل نمو بعض البكتيريا وتثبّط غيرها (أكار الملح والمانيتول للعنقودية، ماكونكي بأملاح الصفراء للمتحمّلة للصفراء، المضادات الحيوية). والأوساط الدالّة تكشف الممرضات بتخمّر السكر ← حامض ← تغيّر لون دليل pH: ماكونكي فيه لاكتوز وأحمر متعادل؛ الإشريكية تخمّر اللاكتوز ← مستعمرات وردية، والسالمونيلا لا تخمّره ← صفراء شاحبة. وأملاح الصفراء والبنفسجي البلّوري تثبّط الموجبة لغرام، فماكونكي انتقائي ودالّ معًا."),
]

meta = {"subject_en": "Diagnostic Microbiology", "subject_ar": "الأحياء المجهرية التشخيصية", "short_ar": "بكتريا", "instructor": "د. عدنان",
        "unit_en": "Lecture 6", "unit_ar": "المحاضرة 6", "unit_label": "LEC", "unit_no": "6",
        "title_en": "Cultivation and Isolation of Viable Pathogen", "title_ar": "زرع الممرضات الحيّة وعزلها",
        "department": "قسم التحليلات", "kind": "Theory — نظري", "stage": "The fourth stage — الرابعة"}
save("bacteriology-lec6-culture-media", meta, blocks, balance(mcq, 6), tf, traps, important)

```
