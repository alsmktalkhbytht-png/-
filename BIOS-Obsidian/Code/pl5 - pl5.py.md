---
source: BIOS-Obsidian/tools/scripts/pl5/pl5.py
handouts: []
saved: 2026-11-05
tags: [bios, code]
---
# pl5/pl5.py

Utility script.

```python
import sys, re; sys.path.insert(0, "/tmp/claude-0/-home-user/a0840832-519a-5a9b-84ea-294867ea1189/scratchpad/imm456")
from ci import *            # c helpers + B INSHORT TERMS balance save(split.fix)
import split

# Medical Parasitology — Lab 5 (stage 4) — Asst. lec. Nariman Hassan — Flagellates / Giardia lamblia
# Source: 30-slide PDF, most slides are pictures — text copied by reading the slides.

BN = lambda en, ar: N(en, ar, label=["BIOS note", "ملاحظة BIOS"])
O = P
def LB(*pairs):
    cells = [B(f"**{e}**", a) for e, a in pairs]
    if len(cells) % 2: cells.append(B("", ""))
    return [cells[i:i + 2] for i in range(0, len(cells), 2)]
def LBT(*pairs, en="Labels in the figure", ar="كتابات الشكل"):
    return T([B("Label", "الكتابة"), B("Label", "الكتابة")], LB(*pairs), style="summary", label_en=en, label_ar=ar)
def TERMS6(terms, n=4):
    head = [B("Term", "المصطلح"), "الترجمات العربية المستعملة"]
    return [SEC("Key terms", "أهم المصطلحات")] + [T(head, [[f"**{e}**", a] for e, a in terms[i:i + n]], ar_cols=[1], widths=[36, 64])
                                                  for i in range(0, len(terms), n)]

blocks = [
 # ───────────────────────── 1. Flagellates
 SEC("Flagellates", "السوطيات"),
 H2("Introduction:", "مقدمة:"),
 L([["Theflagellates belong to the Magistophora and possess more than one flagellum.", "Beating these flagella enable them to move.",
     "A cytosome may be present which helps in the identification of the species.",
     "Intestinal parasites are parasites that can infect the gastro-intestinal tract (GIT) of humans and other animals."],
    ["They can live throughout the body, but most prefer the intestinal wall.",
     "Means of exposure include ingestion of undercooked meat, drinking infected water, and skin absorption."],
    ["There are pathogenic and commensal species of flagellates.",
     "The flagellates which are encountered in the intestinal tract are: Giardia lamblia, Dientamoeba fragilis, Chilomastix mesnili, Trichomonas hominis, Retortamonas intestinalis and Enteromonas hominis (the latter 2 being less common)."]],
   [["تنتمي السوطيات إلى **السوطيات (Mastigophora)** وتملك **أكثر من سوط واحد**.", "وضرب هذه الأسواط يمكّنها من الحركة.",
     "وقد يوجد **فم خلوي (cytosome)** يساعد في تشخيص النوع.",
     "الطفيليات المعوية هي طفيليات يمكن أن تصيب **القناة الهضمية** للإنسان والحيوانات الأخرى."],
    ["يمكنها العيش في كل أنحاء الجسم، لكن معظمها يفضّل **جدار الأمعاء**.",
     "وطرق التعرّض تشمل تناول **اللحم غير المطبوخ جيدًا**، وشرب **الماء الملوّث**، و**الامتصاص عبر الجلد**."],
    ["توجد أنواع **ممرضة** وأنواع **متعايشة** من السوطيات.",
     "والسوطيات التي تُصادف في القناة المعوية هي: **الجيارديا اللمبلية**، والأميبا الهشّة ثنائية النواة، والكيلوماستكس المسنيلية، والمشعّرة البشرية، والريتورتاموناس المعوية، والإنتيروموناس البشرية (والأخيرتان أقل شيوعًا)."]]),
 BN("“Theflagellates” = The flagellates, and “Magistophora” = **Mastigophora** (the flagellates) — written as in the slide.",
    "“Theflagellates” أي The flagellates، و“Magistophora” صحيحها **Mastigophora** (السوطيات) — كُتبت كما في الشريحة."),
 H2("Classification", "التصنيف"),
 T([B("Rank", "المرتبة"), B("Name", "الاسم")],
   [[B("**Kingdom**", "**المملكة**"), B("Anemalia", "الحيوانية")],
    [B("**Subkingdom**", "**تحت المملكة**"), B("Protozoa", "الأوالي (الحيوانات الأولية)")],
    [B("**Phylum**", "**الشعبة**"), B("Sarcomastigophora", "اللحميات السوطية")],
    [B("**Class**", "**الصف**"), B("Mastigophora (flagellates)", "السوطيات")]],
   key_cols=[0], widths=[30, 70]),
 L(["**Luminal Flagellates** — Giardia lambelia,Chilomastic mesnili",
    "**Hem flagellates** — Trypanosoma Spp. , Leishmania Spp.",
    "**Genital flagellates** — Trichomonas Spp."],
   ["**سوطيات التجويف (المعوية)** — الجيارديا اللمبلية، والكيلوماستكس المسنيلية",
    "**السوطيات الدموية** — أنواع المثقبيات، وأنواع الليشمانيا",
    "**السوطيات التناسلية** — أنواع المشعّرات"],
   en="There are three group of flagellates according to there habitat", ar="توجد ثلاث مجاميع من السوطيات حسب موطنها"),
 BN("Spelling in the slide: “Anemalia” = Animalia, “Hem flagellates” = haemoflagellates, “lambelia” = lamblia, “Chilomastic” = Chilomastix.",
    "إملاء الشريحة: “Anemalia” أي Animalia، و“Hem flagellates” أي السوطيات الدموية، و“lambelia” أي lamblia، و“Chilomastic” أي Chilomastix."),
 H2("Giardia Lambelia", "الجيارديا اللمبلية"),
 L(["**Disease :** Giardiasis, G. intestinalis,G.doudenalis)", "**Habitat :** Small intestine (Doudenum,Jejunum)", "**Morphology :** G. lambelia have two stages, Trophozoite,Cyst"],
   ["**المرض:** داء الجيارديات (وتسمّى أيضًا الجيارديا المعوية والجيارديا الاثني عشرية)", "**الموطن:** الأمعاء الدقيقة (الاثنا عشري، الصائم)", "**الشكل:** للجيارديا اللمبلية طوران، الطور المتغذّي والكيس"]),
 INSHORT([("Flagellates move by **more than one flagellum**; class **Mastigophora**, phylum **Sarcomastigophora**.", "السوطيات تتحرّك **بأكثر من سوط**؛ الصف **السوطيات**، والشعبة **اللحميات السوطية**."),
          ("3 groups by habitat: **luminal** (Giardia, Chilomastix), **blood** (Trypanosoma, Leishmania), **genital** (Trichomonas).", "3 مجاميع حسب الموطن: **التجويف** (الجيارديا، الكيلوماستكس)، **الدم** (المثقبيات، الليشمانيا)، **التناسلية** (المشعّرات)."),
          ("Giardia → **giardiasis**; small intestine; **two stages**: trophozoite and cyst.", "الجيارديا ← **داء الجيارديات**؛ الأمعاء الدقيقة؛ **طوران**: المتغذّي والكيس.")]),

 # ───────────────────────── 2. Lumen-dwelling flagellates
 SEC("LUMEN-DEWLLING FLAGELLATES", "السوطيات المستوطنة للتجويف"),
 T([B("GENUS", "الجنس"), B("PARASITE", "الطفيلي"), B("HABITAT", "الموطن")],
   [[B("Giardia", "الجيارديا"), B("G. lamblia", "الجيارديا اللمبلية"), B("Duodenum", "الاثنا عشري")],
    [B("Chilomastix", "الكيلوماستكس"), B("G. mesnili", "المسنيلية"), B("Caecum", "الأعور")],
    [B("Enteromonas", "الإنتيروموناس"), B("E. hominis", "البشرية"), B("Colon", "القولون")]], key_cols=[0], widths=[28, 32, 40]),
 T([B("GENUS", "الجنس"), B("PARASITE", "الطفيلي"), B("HABITAT", "الموطن")],
   [[B("Retromonas", "الريتورتاموناس"), B("R. intestinalis", "المعوية"), B("Colon", "القولون")],
    [B("Pentatrichomonas", "خماسية المشعّرات"), B("P. hominis", "البشرية"), B("Ileocaecal region", "المنطقة اللفائفية الأعورية")],
    [B("Trichomonas", "المشعّرات"), B("T. Vaginalis / T. tenax", "المهبلية / الفموية"), B("Vagina &Urethra / Teeth & Gums", "المهبل والإحليل / الأسنان واللثة")],
    [B("Dientamoeba", "الأميبا ثنائية النواة"), B("D. fragilis", "الهشّة"), B("Colonic mucosal crypts", "خبايا مخاطية القولون")]],
   key_cols=[0], widths=[28, 32, 40]),
 BN("In the table “G. mesnili” is **Chilomastix (C.) mesnili**, “Retromonas” is **Retortamonas**, and “DEWLLING” = DWELLING.",
    "في الجدول “G. mesnili” هي **Chilomastix (C.) mesnili**، و“Retromonas” هي **Retortamonas**، و“DEWLLING” أي DWELLING."),
 INSHORT([("Only **Giardia** lives in the **duodenum**; Chilomastix → caecum; Enteromonas and Retortamonas → colon.", "**الجيارديا** وحدها تعيش في **الاثني عشري**؛ الكيلوماستكس ← الأعور؛ الإنتيروموناس والريتورتاموناس ← القولون."),
          ("T. vaginalis → **vagina & urethra**; T. tenax → **teeth & gums**; D. fragilis → colonic crypts.", "المشعّرة المهبلية ← **المهبل والإحليل**؛ المشعّرة الفموية ← **الأسنان واللثة**؛ الهشّة ← خبايا القولون.")]),

 # ───────────────────────── 3. Giardia lamblia
 SEC("Giardia lamblia", "الجيارديا اللمبلية"),
 L(["Also known as – G. intestinalis / Lamblia intestinalis.", "**HISTORY** :", "First seen by Antonie Von Leeuwenhoek by examining his own stool."],
   ["تُعرف أيضًا بـ – **الجيارديا المعوية / اللمبلية المعوية**.", "**التاريخ** :", "شوهدت أول مرة من قِبَل **أنطوني فان ليفينهوك** بفحص برازه هو."]),
 F("giardia-name.jpg", "Giardia lamblia — Prof. Giard of Paris (Giardia) and Prof. Lamble of Prague (lamblia)",
   "الجيارديا اللمبلية — البروفيسور جيارد من باريس (Giardia) والبروفيسور لامبل من براغ (lamblia)", h="34mm", fit="contain"),
 H2("GEOGRAPHICAL SPREAD & EPIDEMICS", "الانتشار الجغرافي والأوبئة"),
 L(["**GEOGRAPHICAL DISTRIBUTION :** m/c protozoan pathogen, worldwide distributed.",
    "**EPIDEMIOLOGY :** Areas with poor sanitation , especially tropics & subtropics.",
    "Common in younger age group.",
    "Traveller’s diarrhea is common among visitors caused by giardiasis through contaminated water."],
   ["**التوزيع الجغرافي:** أشيع (m/c = most common) ممرض أوالي، منتشر عالميًا.",
    "**الوبائيات:** المناطق ذات **الصرف الصحي الرديء**، خاصةً المناطق **الاستوائية وشبه الاستوائية**.",
    "شائع في **الفئات العمرية الأصغر**.",
    "**إسهال المسافرين** شائع بين الزائرين، ويسبّبه داء الجيارديات عن طريق **الماء الملوّث**."]),
 H2("HABITAT", "الموطن"),
 L(["Duodenum & the upper part of the jejunum.", "THE ONLY PROTOZOAN PARASITE FOUND IN THE LUMEN OF HUMAN SMALL INTESTINE."],
   ["**الاثنا عشري والجزء العلوي من الصائم**.", "**الطفيلي الأوالي الوحيد** الموجود في **تجويف الأمعاء الدقيقة** للإنسان."]),
 F("habitat.jpg", "Habitat of Giardia — Duodenum; Jejunum", "موطن الجيارديا — الاثنا عشري؛ الصائم", h="46mm", fit="contain"),
 INSHORT([("Also called **G. intestinalis / Lamblia intestinalis**; first seen by **Leeuwenhoek** in his own stool.", "وتسمّى **الجيارديا المعوية / اللمبلية المعوية**؛ رآها أول مرة **ليفينهوك** في برازه."),
          ("Named after **Prof. Giard (Paris)** and **Prof. Lamble (Prague)**.", "سمّيت نسبةً إلى **البروفيسور جيارد (باريس)** و**البروفيسور لامبل (براغ)**."),
          ("Most common protozoan pathogen, worldwide; poor sanitation; young age; **traveller’s diarrhea**.", "أشيع ممرض أوالي، عالمي؛ الصرف الرديء؛ الأعمار الصغيرة؛ **إسهال المسافرين**."),
          ("Habitat: **duodenum + upper jejunum** — the only protozoan in the lumen of the small intestine.", "الموطن: **الاثنا عشري + أعلى الصائم** — الأوالي الوحيد في تجويف الأمعاء الدقيقة.")]),

 # ───────────────────────── 4. Morphology
 SEC("MORPHOLOGY", "الشكل"),
 L(["Trophozoit (Vegetative form)", "Cyst (Infective form)"], ["الطور المتغذّي (الشكل الخضري)", "الكيس (الشكل المُعدي)"], en="It exists in two forms –", ar="توجد بشكلين –"),
 H2("TROPHOZOITE", "الطور المتغذّي"),
 L(["Tennis racket or heart shaped or pyriform shaped.", "Dorsal surface – convex", "Ventral surface – concave & having sucking disk (for attachment)",
    "14 µm x 7µm x 4µm", "Anterior end – broad & rounded", "Posterior end – tappers to a sharp point"],
   ["يشبه **مضرب التنس** أو **القلب** أو **الكمثرى**.", "السطح الظهري – **محدّب**", "السطح البطني – **مقعّر** وفيه **قرص ماصّ** (للالتصاق)",
    "**14 × 7 × 4 مايكرومتر**", "النهاية الأمامية – عريضة ومستديرة", "النهاية الخلفية – تستدقّ إلى نقطة حادّة"]),
 L(["Nuclei – 1 pair", "Flagella with blepharoblast – 4 pair", "Axostyle – 1 pair (along the midline)",
    "Parabasal / Median body – 1 pair ( transverse & posterior to sucking disc)"],
   ["الأنوية – **زوج واحد**", "الأسواط مع الجسيمات القاعدية – **4 أزواج**", "القضيب المحوري – **زوج واحد** (على طول الخط الوسطي)",
    "الجسم جار القاعدي / الوسطي – **زوج واحد** (مستعرض وخلف القرص الماصّ)"],
   en="Bilaterally symmetrical :", ar="متناظر ثنائيًا :"),
 SIDE([C("Falling leaf motility around its long axis.", "حركة **الورقة المتساقطة** حول محوره الطويل.")], "falling-leaf.jpg", "Falling leaves (slide picture)", "أوراق متساقطة (صورة الشريحة)"),
 F("troph-diagram.jpg", "Trophozoite of Giardia (drawing)", "الطور المتغذّي للجيارديا (رسم)", h="70mm", fit="contain"),
 LBT(("Nucleus", "النواة"), ("Basal bodies", "الأجسام القاعدية"), ("Lateral crest", "العرف الجانبي"), ("Ventrolateral flagella", "الأسواط البطنية الجانبية"),
     ("Anterolateral flagella", "الأسواط الأمامية الجانبية"), ("Ventral disc", "القرص البطني"), ("Median bodies", "الأجسام الوسطية"), ("Posterolateral flagella", "الأسواط الخلفية الجانبية"),
     ("Ventral flagella", "الأسواط البطنية"), ("Caudal flagella", "الأسواط الذيلية")),
 F("troph-photos.jpg", "Giardia trophozoites — Sucking disc; Axostyle; Parapasal body", "أطوار الجيارديا المتغذّية — القرص الماصّ؛ القضيب المحوري؛ الجسم جار القاعدي", h="80mm", fit="contain"),
 F("troph-stains.jpg", "Fig : A, B, C: three trophozoites of Giardia intestinalis. Stained with trichrome (A) and stained with iron hematoxyline (B and C) each cell has two nuclei with a large, central karyosome. ( duodenal aspiration smear )",
   "الشكل: A وB وC: ثلاثة أطوار متغذّية للجيارديا المعوية، مصبوغة بالصبغة الثلاثية (A) وبالهيماتوكسيلين الحديدي (B وC)، ولكل خلية نواتان بجسيم نووي كبير مركزي. (مسحة رشافة الاثني عشري)", h="46mm", fit="contain"),
 BN("“Parapasal body” in the figure = **parabasal body**.", "“Parapasal body” في الشكل أي **الجسم جار القاعدي (parabasal body)**."),

 H2("CYST", "الكيس"),
 L(["Round or oval in shape.", "Surrounded by hyaline cyst wall.", "12µm x 7µm.", "Axostyle – diagonally placed, form a deviding line within cyst.",
    "4 nuclei – clustered at one end or at opposite poles (each pairs).", "Remnants of flagella and margins of the sucking disc may be seen inside the cytoplasm of a young cyst.",
    "An acid environment often causes the parasite to encyst."],
   ["**مستدير أو بيضوي** الشكل.", "محاط بجدار كيس **شفّاف (زجاجي)**.", "**12 × 7 مايكرومتر**.", "القضيب المحوري – **موضوع قطريًا**، ويكوّن خطًا فاصلًا داخل الكيس.",
    "**4 أنوية** – متجمّعة في نهاية واحدة أو عند قطبين متقابلين (كل زوج).", "قد تُشاهد **بقايا الأسواط وحواف القرص الماصّ** داخل سايتوبلازم الكيس الفتي.",
    "**البيئة الحامضية** غالبًا تجعل الطفيلي يتكيّس."]),
 F("cyst-diagram.jpg", "Cyst of Giardia (drawing) — Space; Nucleus; Median bodies; Axostyles", "كيس الجيارديا (رسم) — فراغ؛ النواة؛ الأجسام الوسطية؛ القضبان المحورية", h="44mm", fit="contain"),
 H2("Cyst of Giardia lamblia", "كيس الجيارديا اللمبلية"),
 L(["oval in shape", "They have smooth well defined wall", "Contains four nuclei", "Contain parabasal bodies and flagellates"],
   ["بيضوي الشكل", "له جدار أملس واضح الحدود", "يحتوي **أربع أنوية**", "يحتوي أجسامًا جار قاعدية وأسواطًا"]),
 F("cyst-photo.jpg", "Cyst of Giardia lamblia", "كيس الجيارديا اللمبلية", h="56mm", fit="contain"),
 BN("“flagellates” in point 4 means **flagella**; “deviding” = dividing; “tappers” = tapers.", "“flagellates” في النقطة 4 يقصد بها **الأسواط**؛ و“deviding” أي dividing؛ و“tappers” أي tapers."),
 T([B("Feature", "الصفة"), B("Trophozoite", "الطور المتغذّي"), B("Cyst", "الكيس")],
   [[B("**Form**", "**الشكل**"), B("Vegetative form", "الشكل الخضري"), B("Infective form", "الشكل المُعدي")],
    [B("**Shape**", "**الهيئة**"), B("tennis racket / heart / pyriform", "مضرب تنس / قلب / كمثرى"), B("round or oval", "مستدير أو بيضوي")],
    [B("**Size**", "**الحجم**"), B("14 µm x 7µm x 4µm", "14 × 7 × 4 مايكرومتر"), B("12µm x 7µm", "12 × 7 مايكرومتر")],
    [B("**Nuclei**", "**الأنوية**"), B("1 pair", "زوج واحد"), B("4", "4")],
    [B("**Other**", "**أخرى**"), B("4 pairs flagella, sucking disc, falling leaf motility", "4 أزواج أسواط، قرص ماصّ، حركة الورقة المتساقطة"), B("axostyle diagonal, remnants of flagella", "قضيب محوري قطري، بقايا أسواط")]],
   key_cols=[0], widths=[18, 42, 40], style="summary", label_en="Trophozoite vs cyst", label_ar="المتغذّي مقابل الكيس"),
 INSHORT([("Two forms: **trophozoite = vegetative**, **cyst = infective**.", "شكلان: **المتغذّي = خضري**، **الكيس = مُعدي**."),
          ("Trophozoite: **pear / tennis racket**, convex back, concave belly with **sucking disc**; 2 nuclei, **4 pairs of flagella**, 1 pair axostyle, 1 pair median bodies.", "المتغذّي: **كمثري / مضرب تنس**، ظهر محدّب وبطن مقعّر فيه **قرص ماصّ**؛ نواتان، **4 أزواج أسواط**، زوج قضيب محوري، زوج أجسام وسطية."),
          ("Motility: **falling leaf**.", "الحركة: **الورقة المتساقطة**."),
          ("Cyst: oval, **12 × 7 µm**, **4 nuclei**, diagonal axostyle; acid environment → encystment.", "الكيس: بيضوي، **12 × 7 مايكرومتر**، **4 أنوية**، قضيب محوري قطري؛ البيئة الحامضية ← التكيّس.")]),

 # ───────────────────────── 5. Immunity, transmission, life cycle
 SEC("IMMUNITY & RISK FACTORS", "المناعة وعوامل الخطورة"),
 L(["Common in younger age & uncommon in adult, suggesting that an efficient immunity has developed."],
   ["شائع في الأعمار الصغيرة وغير شائع في البالغين، مما يشير إلى **تكوّن مناعة فعّالة**."]),
 L(["Both humoral & cell mediated immunity are important."], ["المناعتان **الخلطية والخلوية** كلتاهما مهمّتان."], start=2),
 L(['IgA deficient person (hypo- or agammaglobulinaemia)', 'Blood group A', 'Achlorhydria', 'Malnutrition'], ['الشخص المصاب **بنقص IgA** (نقص أو انعدام الغلوبيولين المناعي)', '**فصيلة الدم A**', '**انعدام حامض المعدة**', 'سوء التغذية'], en='**RISK FACTORS :**', ar='**عوامل الخطورة:**'),
 L(['Use of cannabis', 'Chronic pancreatitis', 'Immune defects (19A deficiency)'], ['تعاطي القنّب', 'التهاب البنكرياس المزمن', 'العيوب المناعية (نقص IgA)'], start=5),
 BN("“19A deficiency” in the slide is **IgA deficiency**.", "“19A deficiency” في الشريحة يقصد بها **نقص IgA**."),
 H2("MODE OF TRANSMISSION", "طريقة الانتقال"),
 L(["Infection is occured by ingestion of cyst in contaminated food & water.", "Direct transmission from person to person may occure in children, male homosexuals, mentally ill persons."],
   ["تحدث الإصابة **بابتلاع الكيس** في الطعام والماء الملوّثين.", "قد يحدث **انتقال مباشر من شخص لآخر** في الأطفال، والمثليين الذكور، والمرضى العقليين."]),
 H2("LIFE CYCLE", "دورة الحياة"),
 L(["Giardia passes its life cycle through **one host**.", "Infective form – mature cyst (10 to 100 cysts are enough to infection)."],
   ["تُكمل الجيارديا دورة حياتها في **مضيف واحد**.", "الشكل المُعدي – **الكيس الناضج** (**10 إلى 100 كيس** تكفي للإصابة)."]),
 L(["Ingestion of the cyst via food or drink.", "Within 30 min of ingestion, the cyst hatches out into two trophozoites.",
    "They multiply in enormous numbers by binary fission & colonise in duodenum.", "They live in the duodenum & upper part of the jejunum, feeding by pinocytosis.",
    ["During unfavourable condition, encystment occurs usually in the colon.", "A thick resistant wall is secreted by the parasite."],
    "The cystic cell is then divided into two within the cyst wall.", "Cysts are passed in stool (may be 200,000) & remain viable in soil & water for several weeks."],
   ["ابتلاع الكيس مع الطعام أو الشراب.", "خلال **30 دقيقة** من الابتلاع يفقس الكيس إلى **طورين متغذّيين**.",
    "تتكاثر بأعداد هائلة **بالانشطار الثنائي** وتستعمر الاثني عشري.", "تعيش في الاثني عشري والجزء العلوي من الصائم، وتتغذّى **بالاحتساء الخلوي (pinocytosis)**.",
    ["في الظروف غير الملائمة يحدث **التكيّس عادةً في القولون**.", "ويفرز الطفيلي جدارًا سميكًا مقاومًا."],
    "ثم تنقسم الخلية الكيسية إلى اثنتين داخل جدار الكيس.", "تخرج الأكياس مع البراز (قد تصل إلى **200,000**) وتبقى **حيّة في التربة والماء لعدّة أسابيع**."]),
 F("cdc-cycle.jpg", "Life cycle of Giardia (CDC)", "دورة حياة الجيارديا (CDC)", h="54mm", fit="contain"),
 LBT(("Contamination of water, food, or hands/fomites with infective cysts.", "تلوّث الماء أو الطعام أو الأيدي/الأدوات بالأكياس المُعدية."),
     ("Trophozoites are also passed in stool but they do not survive in the environment.", "تخرج الأطوار المتغذّية أيضًا مع البراز لكنها لا تعيش في البيئة."),
     ("i = Infective Stage", "i = الطور المُعدي"), ("d = Diagnostic Stage", "d = الطور التشخيصي"), ("Cyst", "الكيس"), ("Trophozoites", "الأطوار المتغذّية")),
 INSHORT([("Risk: **IgA deficiency**, **blood group A**, achlorhydria, malnutrition, cannabis, chronic pancreatitis.", "الخطورة: **نقص IgA**، **فصيلة الدم A**، انعدام حامض المعدة، سوء التغذية، القنّب، التهاب البنكرياس المزمن."),
          ("Transmission: **cysts in food & water**; person to person in children, male homosexuals, mentally ill.", "الانتقال: **الأكياس في الطعام والماء**؛ ومن شخص لآخر في الأطفال والمثليين الذكور والمرضى العقليين."),
          ("**One host**; **10-100 cysts** infect; cyst hatches in **30 min** → 2 trophozoites → binary fission in duodenum.", "**مضيف واحد**؛ **10-100 كيس** تكفي؛ يفقس الكيس خلال **30 دقيقة** ← طوران متغذّيان ← انشطار ثنائي في الاثني عشري."),
          ("Encystment in the **colon**; up to **200,000 cysts** in stool, viable for weeks.", "التكيّس في **القولون**؛ حتى **200,000 كيس** في البراز، تبقى حيّة أسابيع.")]),

 # ───────────────────────── 6. Pathogenesis & clinical
 SEC("PATHOGENESIS", "الإمراضية"),
 L(['With the help of sucking disc they adhere to the convex surface of epithelial cells & crypts of intestinal mucosa.', 'It doesn’t invade the tissues.'], ['بمساعدة **القرص الماصّ** تلتصق بالسطح المحدّب للخلايا الظهارية وخبايا الغشاء المخاطي المعوي.', '**لا تغزو الأنسجة**.']),
 L(['May cause abnormalities of villous architecture by apoptosis.', 'Capable of producing harm by the toxic effect (VSSP- Variant Specific Surface Proteins), irritative effect & spoliative action (by diverting the nutriments).', 'To avoid the high acidity of proximal duodenum, Giardia often localizes in the biliary tract (gall bladder).'], ['قد تسبّب **تشوّهات في بنية الزغابات** عن طريق **الموت الخلوي المبرمج**.', 'قادرة على إحداث الضرر **بالتأثير السمّي** (**بروتينات السطح المتغيّرة النوعية VSSP**)، و**التأثير المهيّج**، و**الفعل السالب** (بتحويل المغذّيات).', 'لتجنّب **الحموضة العالية** للاثني عشري القريب، غالبًا ما تتمركز الجيارديا في **القناة الصفراوية (المرارة)**.'], start=3),
 H2("CLINICAL FEATURES", "المظاهر السريرية"),
 C("**1.** Silent cases without any symptoms.", "**1.** حالات صامتة **بلا أي أعراض**."),
 L(['Malabsorption syndrome (Steatorrhoea)', 'Mucus diarrhea', 'Dull epigastric pain'], ['متلازمة **سوء الامتصاص** (**الإسهال الدهني**)', 'إسهال مخاطي', 'ألم شرسوفي كليل'], en='**2.** Intestinal :', ar='**2.** معوية :'),
 L(['Flatulence', 'Chronic enteritis', 'Acute enterocolitis'], ['انتفاخ (غازات)', 'التهاب الأمعاء المزمن', 'التهاب الأمعاء والقولون الحاد'], start=4),
 L(["Fever", "Anaemia", "Weight loss", "Allergic manifestations."], ["حمّى", "فقر الدم", "نقص الوزن", "مظاهر تحسّسية."], en="**3.** General :", ar="**3.** عامة :"),
 C(["**4.** Chronic cholecystopathy.", "**Incubation period : about 2 weeks**"], ["**4.** اعتلال المرارة المزمن.", "**فترة الحضانة: حوالي أسبوعين**"]),
 INSHORT([("Attaches by the **sucking disc**; **does not invade** tissues; villous damage by apoptosis.", "تلتصق **بالقرص الماصّ**؛ **لا تغزو** الأنسجة؛ تلف الزغابات بالموت المبرمج."),
          ("Harm: toxic (**VSSP**), irritative, spoliative (steals nutrients); may hide in the **gall bladder**.", "الضرر: سمّي (**VSSP**)، مهيّج، سالب (يسرق المغذّيات)؛ وقد تختبئ في **المرارة**."),
          ("Clinical: silent cases; **malabsorption / steatorrhoea**, mucus diarrhea, epigastric pain; fever, anaemia, weight loss; incubation **≈ 2 weeks**.", "سريريًا: حالات صامتة؛ **سوء امتصاص / إسهال دهني**، إسهال مخاطي، ألم شرسوفي؛ حمّى، فقر دم، نقص وزن؛ الحضانة **≈ أسبوعان**.")]),

 # ───────────────────────── 7. Laboratory diagnosis
 SEC("LABORATORY DIAGNOSIS", "التشخيص المختبري"),
 T([B("Method", "الطريقة"), B("Method", "الطريقة")],
   [[B("**Stool examination** — Macroscopic / Microscopic", "**فحص البراز** — العياني / المجهري"), B("**Enterotest (String test)**", "**الاختبار المعوي (اختبار الخيط)**")],
    [B("**Serological test** — Antigen detection / Antibody detection", "**الاختبار المصلي** — كشف المستضد / كشف الضد"), B("**Molecular diagnosis** — DNA probe / PCR", "**التشخيص الجزيئي** — مسبار الدنا / تفاعل البلمرة المتسلسل")]],
   widths=[50, 50], style="summary", label_en="Chart in the slide", label_ar="مخطط الشريحة"),
 H2("STOOL EXAMINATION", "فحص البراز"),
 L(['Identification of cysts in formed stool and trophozoites & cysts in diarrhoeic stool or after a purgative.', 'In asymptomatic carriers only cysts are seen.'], ['تشخيص **الأكياس في البراز المتماسك**، و**الأطوار المتغذّية والأكياس في البراز الإسهالي** أو بعد مسهّل.', 'في **الحاملين بلا أعراض** تُرى **الأكياس فقط**.']),
 L(['Macroscopy : offensive odour, pale coloured & fatty stool.', 'Microscopy : salaine & iodine wet preparations.', 'Multiple specimens need to be examined.', 'Concentration techniques like formal ether or zinc acetate are used.'], ['الفحص العياني: براز **كريه الرائحة، شاحب اللون ودهني**.', 'الفحص المجهري: تحضيرات رطبة **بالمحلول الملحي واليود**.', 'يجب فحص **عيّنات متعدّدة**.', 'تُستعمل **تقنيات التركيز** مثل الفورمول-إيثر أو أسيتات الزنك.'], start=3),
 H2("ENTEROTEST (STRING TEST)", "الاختبار المعوي (اختبار الخيط)"),
 C("Method for obtaining duodenal specimen (upper part of small intestine)", "طريقة للحصول على **عيّنة من الاثني عشري** (الجزء العلوي من الأمعاء الدقيقة)"),
 L(['A coiled string with a small weighted gelatin capsule is swallowed by the patient & the free end of the string is attached to the side of the patient’s face.', 'The capsule dissolves in the stomach & the string which is weighted at its distal end, passes into the duodenum.'], ['يبلع المريض **خيطًا ملفوفًا داخل كبسولة جيلاتينية صغيرة مثقّلة**، ويُثبّت الطرف الحرّ من الخيط على جانب وجه المريض.', 'تذوب الكبسولة في المعدة، ويمرّ الخيط المثقّل في نهايته البعيدة إلى **الاثني عشري**.'], en='Procedure :', ar='الطريقة :'),
 L(['After 2-4 hrs the string is withdrawn & placed in a saline with mechanical shaking.', 'The centrifuged deposit of saline is examined by wet mount technique to detect the presence of motility of the organism or specific morphological forms of trophozoites of Giardia (and larvae of Strongyloides stercoralis).'], ['بعد **2-4 ساعات** يُسحب الخيط ويوضع في محلول ملحي مع **رجّ ميكانيكي**.', 'يُفحص راسب المحلول الملحي المنبوذ **بطريقة التحضير الرطب** للكشف عن حركة الكائن أو الأشكال المميّزة للأطوار المتغذّية للجيارديا (ويرقات **الأسطوانية البرازية**).'], start=3),
 H2("When the test should performed", "متى يُجرى الاختبار"),
 L(["Entero-test is performed when a physician suspects a parasitic infection, but no parasites were found in stool sample.",
    "As its sensitivity is comparable to duodenal aspirate, it eliminates the need of duodenal intubation."],
   ["يُجرى الاختبار المعوي عندما **يشكّ الطبيب بإصابة طفيلية ولكن لم يُعثر على طفيليات في عيّنة البراز**.",
    "ولأن حساسيته **مماثلة لرشافة الاثني عشري**، فإنه يُغني عن **التنبيب الاثني عشري**."]),
 F("string-test.jpg", "Enterotest (string test): the capsule with the coiled string, and the string being withdrawn", "الاختبار المعوي (اختبار الخيط): الكبسولة مع الخيط الملفوف، وسحب الخيط", h="60mm", fit="contain"),
 H2("SERODIAGNOSIS", "التشخيص المصلي"),
 L(["ELISA", "IIF (Indirect immunofluroscent tests)", "Immuno-chromatographic strip test"],
   ["الإليزا", "الفلورة المناعية غير المباشرة", "اختبار الشريط الكروماتوغرافي المناعي"], en="**Antigen detection in feces –**", ar="**كشف المستضد في البراز –**"),
 L(["Antigen present – active infection.", "Giardia specific Ag 65 (GSA 65) detection by ELISA kits.", "Sensitivity - 95%", "Specificity – 100% compared to microscopy.",
    "Tests are not for routine purpose.", "It is for epidemiological & control purposes."],
   ["وجود المستضد – **إصابة فعّالة**.", "كشف **المستضد النوعي للجيارديا 65 (GSA 65)** بعُدد الإليزا.", "الحساسية - **95%**", "النوعية – **100%** مقارنةً بالفحص المجهري.",
    "الاختبارات **ليست للاستعمال الروتيني**.", "إنها لأغراض **وبائية ورقابية**."], start=4),
 L(["IIF", "ELISA"], ["الفلورة المناعية غير المباشرة", "الإليزا"], en="**Antibody detection –**", ar="**كشف الضد –**"),
 L(["Tests can’t differentiates between recent & past infection.", "Lack sensitivity & specificity.",
    "Antibody detection (anti Giardia IgG Ab) is useful for epidemiological & pathophysiological studies.",
    "The presence of anti Giardia secretory IgA Ab in breast milk protects breast fed infants from giardiasis."],
   ["الاختبارات **لا تميّز بين الإصابة الحديثة والسابقة**.", "تفتقر إلى الحساسية والنوعية.",
    "كشف الضد (**ضدّ IgG المضاد للجيارديا**) مفيد للدراسات الوبائية والفسلجية المرضية.",
    "وجود **ضدّ IgA الإفرازي المضاد للجيارديا في حليب الأم** يحمي الرضّع من داء الجيارديات."], start=3),
 H2("MOLECULAR METHOD", "الطريقة الجزيئية"),
 L(["DNA based techniques are available now.", "They are used to demonstrate the genome of the parasite.", "PCR", "DNA probe"],
   ["التقنيات المعتمدة على الدنا متوفّرة الآن.", "تُستعمل لإظهار **جينوم الطفيلي**.", "تفاعل البلمرة المتسلسل", "مسبار الدنا"]),
 INSHORT([("Stool: cysts in formed stool; trophozoites + cysts in diarrhoea; carriers → **cysts only**; stool **offensive, pale, fatty**.", "البراز: الأكياس في المتماسك؛ المتغذّيات + الأكياس في الإسهالي؛ الحاملون ← **أكياس فقط**؛ البراز **كريه، شاحب، دهني**."),
          ("Saline & iodine wet mounts; **multiple specimens**; concentration: formol-ether / zinc acetate.", "تحضيرات رطبة ملحية ويودية؛ **عيّنات متعدّدة**؛ التركيز: فورمول-إيثر / أسيتات الزنك."),
          ("**String test**: swallowed capsule → duodenum → withdrawn after **2-4 h** → saline → centrifuge → wet mount; used when stool is negative.", "**اختبار الخيط**: كبسولة تُبلع ← الاثني عشري ← تُسحب بعد **2-4 ساعات** ← ملحي ← نبذ ← تحضير رطب؛ يُستعمل عندما يكون البراز سالبًا."),
          ("Antigen (GSA 65, ELISA): sensitivity **95%**, specificity **100%** = active infection; antibodies can’t tell recent from past.", "المستضد (GSA 65، إليزا): الحساسية **95%**، النوعية **100%** = إصابة فعّالة؛ والأضداد لا تميّز الحديثة من السابقة.")]),

 # ───────────────────────── 8. Treatment & prophylaxis
 SEC("TREATMENT", "العلاج"),
 T([B("Drug", "الدواء"), B("Dose / use", "الجرعة / الاستعمال")],
   [[B("**Metronidazole**", "**الميترونيدازول**"), B("250mg x 3 times daily x 5 days. **(Cure rate -95%)**", "250 ملغ × 3 مرات يوميًا × 5 أيام. **(نسبة الشفاء 95%)**")],
    [B("**Tinidazole**", "**التينيدازول**"), B("2 gm single dose. **(More effective)**", "2 غم جرعة واحدة. **(أكثر فعالية)**")]],
   key_cols=[0], widths=[32, 68]),
 T([B("Drug", "الدواء"), B("Dose / use", "الجرعة / الاستعمال")],
   [[B("**Furazolidone**", "**الفيورازوليدون**"), B("Children (less adverse effects)", "الأطفال (آثار جانبية أقل)")],
    [B("**Nitazoxamide**", "**النيتازوكسانيد**"), B("Children (less adverse effects)", "الأطفال (آثار جانبية أقل)")],
    [B("**Parmomycin**", "**الباروموميسين**"), B("Pregnant female", "المرأة الحامل")]],
   key_cols=[0], widths=[32, 68]),
 BN("“Nitazoxamide” = **Nitazoxanide** and “Parmomycin” = **Paromomycin** (spelling in the slide).", "“Nitazoxamide” أي **Nitazoxanide**، و“Parmomycin” أي **Paromomycin** (إملاء الشريحة)."),
 H2("PROPHYLAXIS", "الوقاية"),
 L(["Proper disposal of the waste water & feces.", "Maintain personal hygiene like hand washing before eating & proper disposal of diapers.",
    "Prevention of food & water contamination.", "Boiling of water and filtration by membrane filters are required.", "Chlorination of water is not effective against cysts."],
   ["التخلّص السليم من **مياه الصرف والبراز**.", "الحفاظ على النظافة الشخصية مثل **غسل اليدين قبل الأكل** والتخلّص السليم من الحفّاظات.",
    "منع تلوّث الطعام والماء.", "**غلي الماء والترشيح بالمرشّحات الغشائية** مطلوبان.", "**تعقيم الماء بالكلور غير فعّال ضد الأكياس**."]),
 INSHORT([("**Metronidazole** 250 mg × 3 daily × 5 days (cure 95%); **Tinidazole** 2 g single dose (more effective).", "**الميترونيدازول** 250 ملغ × 3 يوميًا × 5 أيام (شفاء 95%)؛ **التينيدازول** 2 غم جرعة واحدة (أكثر فعالية)."),
          ("Children → **Furazolidone / Nitazoxanide**; pregnant → **Paromomycin**.", "الأطفال ← **الفيورازوليدون / النيتازوكسانيد**؛ الحامل ← **الباروموميسين**."),
          ("Prevention: boil and filter water — **chlorine does not kill the cysts**.", "الوقاية: اغلِ الماء ورشّحه — **الكلور لا يقتل الأكياس**.")]),

 *TERMS6([("Flagellates (Mastigophora)", "السوطيات / الأوالي السوطية"),
          ("Flagellum", "السوط / الهدب السوطي"),
          ("Cytosome", "الفم الخلوي / الثغر الخلوي"),
          ("Giardiasis", "داء الجيارديات / الجيارديا / اللمبليا"),
          ("Trophozoite (vegetative form)", "الطور المتغذّي / الشكل الخضري"),
          ("Cyst (infective form)", "الكيس / الشكل المُعدي / الطور المتكيّس"),
          ("Sucking disc (ventral disc)", "القرص الماصّ / القرص البطني / قرص الالتصاق"),
          ("Axostyle", "القضيب المحوري / الخيط المحوري"),
          ("Median / parabasal body", "الجسم الوسطي / الجسم جار القاعدي"),
          ("Blepharoblast (basal body)", "الجسيم القاعدي / الحُبيبة القاعدية"),
          ("Pyriform", "كمثري الشكل / إجاصي"),
          ("Falling leaf motility", "حركة الورقة المتساقطة"),
          ("Encystment", "التكيّس / تكوين الكيس"),
          ("Binary fission", "الانشطار الثنائي"),
          ("Pinocytosis", "الاحتساء الخلوي / الشرب الخلوي"),
          ("Achlorhydria", "انعدام حامض المعدة / فقد الحامض المعدي"),
          ("Malabsorption syndrome", "متلازمة سوء الامتصاص"),
          ("Steatorrhoea", "الإسهال الدهني / البراز الدهني"),
          ("Apoptosis", "الموت الخلوي المبرمج / الاستماتة"),
          ("Enterotest (string test)", "الاختبار المعوي / اختبار الخيط"),
          ("Duodenal aspirate", "رشافة الاثني عشري / شفط الاثني عشري"),
          ("Purgative", "مسهّل / مليّن"),
          ("Traveller’s diarrhea", "إسهال المسافرين"),
          ("Prophylaxis", "الوقاية / الاتقاء")]),
]

SPECIES = re.compile(r"\b(?:(?:Giardia|Dientamoeba|Chilomastix|Chilomastic|Trichomonas|Retortamonas|Enteromonas|Lamblia|Strongyloides|G\.|E\.|R\.|P\.|T\.|D\.) "
                     r"(?:lamblia|lambelia|Lambelia|intestinalis|fragilis|mesnili|hominis|stercoralis|Vaginalis|tenax)|G\.doudenalis|Giardia|Trypanosoma|Leishmania)\b")
def ital(s):
    out, i = [], 0
    for m in SPECIES.finditer(s):
        if s[:m.start()].count("**") % 2 or s[:m.start()].endswith("__"):
            continue
        out.append(s[i:m.start()]); out.append(f"__{m.group(0)}__"); i = m.end()
    out.append(s[i:]); return "".join(out)
def walk_it(x):
    if isinstance(x, str): return ital(x)
    if isinstance(x, list): return [walk_it(y) for y in x]
    return x
for b in blocks:
    if b.get("t") == "section": continue
    for k in ("en", "list_en"):
        if k in b: b[k] = walk_it(b[k])
    if b.get("t") == "table":
        b["rows"] = [[[ital(c[0]), c[1]] if isinstance(c, list) else c for c in r] for r in b["rows"]]

exec(open(__file__.replace("pl5.py", "pl5q.py")).read())

```
