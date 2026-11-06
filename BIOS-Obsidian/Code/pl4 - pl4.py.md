---
source: BIOS-Obsidian/tools/scripts/pl4/pl4.py
handouts: []
saved: 2026-11-06
tags: [bios, code]
---
# pl4/pl4.py

Utility script.

```python
import sys, re; sys.path.insert(0, "/tmp/claude-0/-home-claude/4a281dcf-357b-50ce-b2f4-8802cfcc6472/scratchpad/imm456")
from ci import *            # c helpers + B INSHORT TERMS balance save(split.fix)
import split
split.ABBR = split.ABBR + ("R.F.",)      # "R.F. Carter" is a name, not a sentence end

# Medical Parasitology — Lab 4 (stage 4) — Asst. lec. Nariman Hassan
# Source: 14 phone screenshots of the slides (no text layer) — text copied by reading the images.

BN = lambda en, ar: N(en, ar, label=["BIOS note", "ملاحظة BIOS"])
O = P
def LB(*pairs):
    """Label table: two labels per row, each English label with its Arabic in the same cell."""
    cells = [B(f"**{e}**", a) for e, a in pairs]
    if len(cells) % 2: cells.append(B("", ""))
    return [cells[i:i + 2] for i in range(0, len(cells), 2)]
def LBT(*pairs, en="Labels in the figure", ar="كتابات الشكل"):
    return T([B("Label", "الكتابة"), B("Label", "الكتابة")], LB(*pairs), style="summary", label_en=en, label_ar=ar)
def GI(rows):
    """'General information' slide: label + value, verbatim."""
    return L([f"**{a}** {b}" for a, b, _, _ in rows], [f"**{c}** {d}" for _, _, c, d in rows])

def TERMS6(terms, n=6):
    """Key terms split into small tables so the pages fill (no big empty space before one long table)."""
    head = [B("Term", "المصطلح"), "الترجمات العربية المستعملة"]
    return [SEC("Key terms", "أهم المصطلحات")] + [T(head, [[f"**{e}**", a] for e, a in terms[i:i + n]], ar_cols=[1], widths=[36, 64])
                                                  for i in range(0, len(terms), n)]

blocks = [
 # ───────────────────────── 1. list
 SEC("Non- pathogenic amoebae", "الأميبات غير الممرضة"),
 L(["E. dispar.", "E. hartmanni.", "E. coli.", "E. gingivalis.", "E. nana.", "I. butschlii."],
   ["الأميبا المتباينة.", "أميبا هارتمان.", "الأميبا القولونية.",
    "الأميبا اللثوية.", "الأميبا القزمة (إندوليماكس نانا).", "أميبا بوتشلي اليودية."],
   en="**Non- pathogenic amoebae:**", ar="**الأميبات غير الممرضة:**"),

 # ───────────────────────── 2. E. coli
 SEC("Entamoeba coli", "الأميبا القولونية"),
 H2("INTRODUCTION", "مقدمة"),
 C(["Entamoeba coli is a non-pathogenic amoeba with world wide distribution.",
    "Its life cycle is similar to that of E. histolytica but it does not have an invasive stage and do not ingest [[cut]]"],
   ["الأميبا القولونية أميبا غير ممرضة ذات انتشار عالمي.",
    "دورة حياتها مشابهة لدورة الأميبا الحالّة للنسيج لكنها لا تملك طورًا غازيًا ولا تبتلع [[قطع]]"]),
 BN("The end of this sentence is hidden behind the picture on the slide; from the comparison table below, E. coli does not ingest **red blood cells**.",
    "نهاية هذه الجملة مغطّاة بالصورة في الشريحة؛ ومن جدول المقارنة أدناه: الأميبا القولونية لا تبتلع **كريات الدم الحمر**."),
 F("ecoli-diagram.jpg", "Entamoeba coli trophozoite (drawing) — Pseudopod; Vacuole Containing Bacteria; Eccentric Karyosome; Uneven Peripheral Chromatin; Cytoplasm",
   "الطور المتغذّي للأميبا القولونية (رسم) — القدم الكاذبة؛ فجوة تحتوي بكتيريا؛ جسيم نووي لا مركزي؛ كروماتين محيطي غير منتظم؛ السايتوبلازم", h="44mm", fit="contain"),

 H2("Trophozoite:", "الطور المتغذّي:"),
 L(["The trophozoite is 15- 50 µm, sluggish in movement.",
    "It has a more granular endoplasm containing food vacuoles, ingested bacteria, depress, a narrow ectoplasm and a large karyosome.",
    "Nuclear membrane is thick and is lined by coarse chromatin granules."],
   ["يبلغ الطور المتغذّي **15- 50 مايكرومتر**، وهو بطيء الحركة.",
    "له إندوبلازم أكثر تحبّبًا يحتوي فجوات غذائية وبكتيريا مبتلعة وحطامًا، وإكتوبلازم ضيّق، وجسيم نووي كبير.",
    "الغشاء النووي سميك ومبطّن بحبيبات كروماتين خشنة."]),
 BN("“depress” in the slide is most likely **debris** (حطام).", "كلمة “depress” في الشريحة الأرجح أنها **debris** أي الحطام."),
 FF(("ecoli-troph-stains.jpg", "Entamoeba coli trophozoite: Iron hematoxylin stain (left), Trichrome stain (right)",
     "الطور المتغذّي للأميبا القولونية: صبغة الهيماتوكسيلين الحديدي (يسار)، الصبغة الثلاثية (يمين)", "46mm"),
    ("ecoli-troph-wet.jpg", "E. coli trophozoite in a wet preparation", "الطور المتغذّي للأميبا القولونية في تحضير رطب", "46mm")),

 H2("Cyst:", "الكيس:"),
 L([["The cyst is spherical and usually larger than that of E. histolytica.", "Its size is 10-31 µm and has 8 nuclei"],
    "Chromatoid body is filamentous.",
    "Pre-cyst resemble in shape with that of E. histolytica."],
   [["الكيس كروي وعادةً أكبر من كيس الأميبا الحالّة للنسيج.", "حجمه **10-31 مايكرومتر** وله **8 أنوية**"],
    "الجسم الكروماتيني خيطي.",
    "ما قبل الكيس يشبه في شكله ما قبل كيس الأميبا الحالّة للنسيج."]),
 F("ecoli-cyst-row.jpg", "E. coli cysts (two photographs) and drawing — cyst wall; 8-nuclei",
   "أكياس الأميبا القولونية (صورتان) ورسم — جدار الكيس؛ 8 أنوية", h="46mm", fit="contain"),

 H2("General information", "معلومات عامة"),
 GI([("Definitive Host:", "Humans", "المضيف النهائي:", "الإنسان"),
     ("Intermediate Host:", "None", "المضيف الوسطي:", "لا يوجد"),
     ("Mode of transmission:", "Ingestion of contaminated food and water.", "طريقة الانتقال:", "ابتلاع طعام وماء ملوّثين."),
     ("Location in Definitive host:", "Cecum and large intestine.", "الموقع في المضيف النهائي:", "الأعور والأمعاء الغليظة."),
     ("Pathology and Treatment:", "None", "الإمراضية والعلاج:", "لا يوجد")]),
 L(["Harmless commensal", "Feeds on bacteria, yeast, and wastes in intestines"],
   ["متعايش غير ضار", "يتغذّى على البكتيريا والخمائر والفضلات في الأمعاء"]),
 C("**Diagnosis:** Important to distinguish between it and E. histolytica",
   "**التشخيص:** من المهم التمييز بينها وبين الأميبا الحالّة للنسيج"),
 L(["8 nuclei in cyst vs. 4 in E. histolytica", "Different shape nuclei."],
   ["8 أنوية في الكيس مقابل 4 في الأميبا الحالّة للنسيج", "أنوية مختلفة الشكل."]),

 H2("Life cycle", "دورة الحياة"),
 C("The life cycle is similar to that of E. histolytica except that the trophozoite in this example doesn’t attack the mucosa of the intestine, so that it is described non-pathogenic (commensal) amoeba.",
   "دورة الحياة مشابهة لدورة الأميبا الحالّة للنسيج إلا أن الطور المتغذّي هنا **لا يهاجم الغشاء المخاطي للأمعاء**، ولذلك توصف بأنها أميبا **غير ممرضة (متعايشة)**."),
 C("Its presence is evidence that the host has ingested fecal material.", "ووجودها **دليل على أن المضيف ابتلع مادة برازية**."),

 H2("Laboratory Diagnosis", "التشخيص المختبري"),
 C("Laboratory diagnosis is made by finding the characteristic cysts in an iodine stained, formol-ether concentration method or by detecting the characteristic trophozoites in a wet preparation or a permanent stained preparation.",
   "يتم التشخيص المختبري بإيجاد **الأكياس المميّزة** في تحضير مصبوغ باليود أو بطريقة **التركيز بالفورمول-إيثر**، أو بالكشف عن **الأطوار المتغذّية المميّزة** في تحضير رطب أو تحضير مصبوغ دائم."),
 F("ecoli-drawings.jpg", "E. coli trophozoite and cyst (drawings)", "الطور المتغذّي والكيس للأميبا القولونية (رسوم)", h="30mm", fit="contain", keep=True),
 F("ecoli-photos.jpg", "Entamoeba coli: trophozoite (left) and cyst (right); scale bar 10 µm",
   "الأميبا القولونية: الطور المتغذّي (يسار) والكيس (يمين)؛ مقياس الرسم 10 مايكرومتر", h="44mm", fit="contain"),

 H2("E. histolytica vs E. coli", "الحالّة للنسيج مقابل القولونية"),
 C("It is similar to E. histolytica with exception of the following differences :-",
   "وهي تشبه الأميبا الحالّة للنسيج باستثناء الاختلافات الآتية :-"),
 T([B("Trophozoite", "الطور المتغذّي"), B("E. histolytica", "الحالّة للنسيج"), B("E. coli", "القولونية")],
   [[B("**Disease**", "**المرض**"), B("Amoebiasis(Amoebic dysentery or Amoebic liver abscess)", "داء الأميبات (الزحار الأميبي أو خرّاج الكبد الأميبي)"), B("Non pathogenic", "غير ممرضة")],
    [B("**Motility**", "**الحركة**"), B("Active", "نشطة"), B("Sluggish", "بطيئة")],
    [B("**Size**", "**الحجم**"), B("10-40 mµ", "10-40 مايكرومتر"), B("20-50 mµ", "20-50 مايكرومتر")],
    [B("**Cytoplasm**", "**السايتوبلازم**"), B("Ectoplasm clearly differentiation from endoplasm", "الإكتوبلازم متميّز بوضوح عن الإندوبلازم"), B("Not clearly differentiation from endoplasm", "غير متميّز بوضوح عن الإندوبلازم")],
    [B("**Food vacuole**", "**الفجوة الغذائية**"), B("Contain R.B.C in acute case", "تحتوي كريات حمر في الحالة الحادّة"), B("Contain bacteria,yeast & other particles without RBC", "تحتوي بكتيريا وخمائر ودقائق أخرى بلا كريات حمر")],
    [B("**Karyosome**", "**الجسيم النووي**"), B("Small &central in the nucleus", "صغير ومركزي في النواة"), B("Large & not central eccentric", "كبير وغير مركزي (لا مركزي)")]],
   key_cols=[0], widths=[22, 39, 39]),
 T([B("Cyst", "الكيس"), B("E. histolytica", "الحالّة للنسيج"), B("E. coli", "القولونية")],
   [[B("**Cyst**", "**الكيس**"), B("Have cyst stage", "لها طور كيس"), B("Have cyst stage", "لها طور كيس")],
    [B("**Diameter**", "**القطر**"), B("10-15 mµ", "10-15 مايكرومتر"), B("10-30 mµ", "10-30 مايكرومتر")],
    [B("**Nuclei in mature cyst**", "**أنوية الكيس الناضج**"), B("4 Nuclei", "4 أنوية"), B("8 Nuclei", "8 أنوية")],
    [B("**Chromatin**", "**الكروماتين**"), B("Chromatin bodies from 1-4 &cigar-shape", "أجسام كروماتينية من 1-4 وسيجارية الشكل"), B("Chromatin bodies from 10-15 &splinter shape", "أجسام كروماتينية من 10-15 وشظوية الشكل")]],
   key_cols=[0], widths=[22, 39, 39]),
 BN(["“mµ” in the table means **µm** (micrometre).",
     "The slides give two sizes for E. coli: trophozoite **15- 50 µm** (text) and **20-50 mµ** (table); cyst **10-31 µm** (text) and **10-30 mµ** (table) — both are kept as written."],
    ["“mµ” في الجدول تعني **مايكرومتر**.",
     "تذكر الشرائح حجمين للأميبا القولونية: المتغذّي **15- 50** (النص) و**20-50** (الجدول)؛ والكيس **10-31** (النص) و**10-30** (الجدول) — وأُبقي الاثنان كما كُتبا."]),
 INSHORT([("Non-pathogenic, worldwide; lives in the **cecum and large intestine**; host: **humans**; no intermediate host.", "غير ممرضة وعالمية؛ تعيش في **الأعور والأمعاء الغليظة**؛ المضيف: **الإنسان**؛ بلا مضيف وسطي."),
          ("Trophozoite **15-50 µm**, sluggish, **large eccentric karyosome**, eats bacteria/yeast — **no RBCs**.", "المتغذّي **15-50 مايكرومتر**، بطيء، **جسيم نووي كبير لا مركزي**، يأكل البكتيريا/الخمائر — **بلا كريات حمر**."),
          ("Cyst **10-31 µm** with **8 nuclei** and **splinter / filamentous** chromatoid bodies (E. histolytica: 4 nuclei, cigar-shaped).", "الكيس **10-31 مايكرومتر** بـ**8 أنوية** وأجسام كروماتينية **شظوية / خيطية** (الحالّة للنسيج: 4 أنوية وسيجارية)."),
          ("Its presence = the host **ingested fecal material**; diagnosis: cysts in iodine / formol-ether, trophozoites in wet or permanent stain.", "وجودها = المضيف **ابتلع مادة برازية**؛ التشخيص: الأكياس باليود / الفورمول-إيثر، والمتغذّيات بالتحضير الرطب أو الصبغة الدائمة.")]),

 # ───────────────────────── 3. E. gingivalis
 SEC("Entamoeba gingivalis", "الأميبا اللثوية"),
 L(["The first amoeba of man to described (Gros in 1849).",
    "Only trophozoite stage have been found.",
    "It live in gingival tissue between teeth and gum."],
   ["**أول أميبا** وُصفت في الإنسان (**Gros** عام **1849**).",
    "لم يُعثر إلا على **الطور المتغذّي** فقط.",
    "تعيش في **النسيج اللثوي** بين الأسنان واللثة."],
   en="**E. gingivalis:**", ar="**الأميبا اللثوية:**"),
 L(["It transmitted by oral contact (closely contact like kissing and from contaminated utensils.",
    "Its prevalence rate rang between 10% in person with healthy mouth to 95% in those with diseased teeth and gum.",
    "Also found in the diseased tonsils and in the vaginal and cervical smear from women using intrauterine devices."],
   ["تنتقل **بالتماس الفموي** (التماس القريب مثل **التقبيل** ومن **الأواني الملوّثة**.",
    "يتراوح معدّل انتشارها بين **10%** في الأشخاص ذوي الفم السليم إلى **95%** في المصابين بأمراض الأسنان واللثة.",
    "وتوجد أيضًا في **اللوزتين المريضتين** وفي المسحات المهبلية وعنق الرحم لدى النساء المستعملات **لوسائل منع الحمل داخل الرحم**."], start=4),
 H2("General information", "معلومات عامة"),
 GI([("Definitive Host:", "Humans. Also other primates, dogs, and cats.", "المضيف النهائي:", "الإنسان. وأيضًا الرئيسيات الأخرى والكلاب والقطط."),
     ("Intermediate Host:", "None", "المضيف الوسطي:", "لا يوجد"),
     ("Mode of transmission:", "Direct oral contact (kissing).", "طريقة الانتقال:", "التماس الفموي المباشر (التقبيل).")]),
 H2("Trophozoite:", "الطور المتغذّي:"),
 L(["Measure 5- 25 µm.", "Actively motile by multiple pseudopodia.", "The food vacuole contain leukocyte, epithelial cell and red blood cells.",
    "Nucleus spherical, central karyosome.", "Chromatin granules are closely packed."],
   ["يبلغ **5- 25 مايكرومتر**.", "**نشط الحركة** بأقدام كاذبة متعدّدة.", "تحتوي الفجوة الغذائية **كريات بيض وخلايا ظهارية وكريات دم حمر**.",
    "النواة كروية، والجسيم النووي **مركزي**.", "حبيبات الكروماتين متراصّة."]),
 F("eging-troph.jpg", "E. gingivalis trophozoite — Host leukocytes; Nucleus; Phagocytosed and partly digested host leukocytes",
   "الطور المتغذّي للأميبا اللثوية — كريات بيض المضيف؛ النواة؛ كريات بيض للمضيف مبلعمة ومهضومة جزئيًا", h="42mm", fit="contain"),
 H2("Life Cycle", "دورة الحياة"),
 C(["No cyst stage.", "Never goes out to external environment."], ["لا يوجد طور كيس.", "لا تخرج أبدًا إلى البيئة الخارجية."]),
 F("eging-cycle.jpg", "Life cycle of E. gingivalis — Trophozoites in mouth ⇄ Binary Fission; Direct oral contact passes it to next host",
   "دورة حياة الأميبا اللثوية — أطوار متغذّية في الفم ⇄ الانشطار الثنائي؛ التماس الفموي المباشر ينقلها إلى المضيف التالي", h="34mm", fit="contain"),
 H2("Laboratory Diagnosis", "التشخيص المختبري"),
 C(["Identification of E. gingivalis is usually made by the finding of trophozoites in scrapings of the gums and teeth;", "trophozoites may be seen ingesting white cells and epithelial cell nuclei"],
   ["يتم تشخيص الأميبا اللثوية عادةً بإيجاد **الأطوار المتغذّية في كشط اللثة والأسنان**؛", "وقد تُشاهد الأطوار المتغذّية وهي **تبتلع كريات بيضًا وأنوية خلايا ظهارية**"]),
 INSHORT([("**First amoeba** described in man (Gros, 1849); **trophozoite only — no cyst**; never leaves the host.", "**أول أميبا** وُصفت في الإنسان (Gros، 1849)؛ **طور متغذّي فقط — بلا كيس**؛ لا تغادر المضيف."),
          ("Lives between **teeth and gum**; spread by **kissing / utensils**; 10% healthy mouth → 95% diseased gums.", "تعيش بين **الأسنان واللثة**؛ تنتقل **بالتقبيل / الأواني**؛ 10% بالفم السليم ← 95% باللثة المريضة."),
          ("Troph **5-25 µm**, active, **central karyosome**; eats **leukocytes, epithelial cells and RBCs**.", "المتغذّي **5-25 مايكرومتر**، نشط، **جسيم نووي مركزي**؛ يأكل **كريات بيض وخلايا ظهارية وكريات حمر**."),
          ("Diagnosis: trophozoites in **scrapings of gums and teeth**.", "التشخيص: أطوار متغذّية في **كشط اللثة والأسنان**.")]),

 # ───────────────────────── 4. Endolimax nana
 SEC("Endolimax nana", "الأميبا القزمة (إندوليماكس نانا)"),
 L([["Firstly described by Wenyon and O’Connor.", "It has a prevalence of 10 - 20% throughout the world."],
    "Habitat lumen of large intestine of man, primates and pigs.",
    "It has 3 stages trophozoite, pre-cyst and cyst."],
   [["وصفها أولًا **Wenyon** و**O’Connor**.", "ونسبة انتشارها **10 - 20%** في أنحاء العالم."],
    "موطنها **تجويف الأمعاء الغليظة** للإنسان والرئيسيات والخنازير.",
    "لها **3 أطوار**: الطور المتغذّي، وما قبل الكيس، والكيس."],
   en="**Endolimax. nana:**", ar="**الأميبا القزمة:**"),
 L(["Trophozoite is small in size 6- 15µm in diameter, with a granular, vacuolated cytoplasm , central nucleus and a sluggish movement.",
    "Chromidial pars and glycogen vacuole are absent.",
    "The cyst is oval in shape, ranging from 5- 14 µm in diameter, with 4 indistinct nuclei and no chromatoid bars."],
   ["الطور المتغذّي **صغير الحجم 6- 15 مايكرومتر** في القطر، بسايتوبلازم محبّب مفجّى، ونواة مركزية، و**حركة بطيئة**.",
    "**القضبان الكروماتينية وفجوة الغلايكوجين غائبة**.",
    "الكيس **بيضوي** الشكل، قطره **5- 14 مايكرومتر**، بـ**4 أنوية غير واضحة** وبلا قضبان كروماتينية."], start=4),
 BN("“Chromidial pars” in the slide means **chromatoidal bars**.", "عبارة “Chromidial pars” في الشريحة يُقصد بها **القضبان الكروماتينية**."),
 F("enana-row1.jpg", "Endolimax nana: Trophozoite (left) and Cyst (iodine, then stained)", "الأميبا القزمة: الطور المتغذّي (يسار) والكيس (باليود، ثم مصبوغ)", h="42mm", fit="contain"),
 FF(("enana-photo.jpg", "Endolimax nana trophozoite (trichrome stain)", "الطور المتغذّي للأميبا القزمة (الصبغة الثلاثية)", "62mm"),
    ("enana-diagram.jpg", "Endolimax nana: cyst 6 to 8 µm (range 5 to 10 µm), trophozoite 8 to 10 µm (range 6 to 12 µm)",
     "الأميبا القزمة: الكيس 6 إلى 8 مايكرومتر (المدى 5 إلى 10)، والمتغذّي 8 إلى 10 مايكرومتر (المدى 6 إلى 12)", "62mm")),
 BN("The drawing gives other size ranges (cyst **5 to 10 µm**, trophozoite **6 to 12 µm**) than the text (**5- 14** and **6- 15 µm**); the text is kept as written.",
    "الرسم يعطي أحجامًا أخرى (الكيس **5 إلى 10**، والمتغذّي **6 إلى 12 مايكرومتر**) غير النص (**5- 14** و**6- 15**)؛ وأُبقي النص كما كُتب."),
 F("enana-row2.jpg", "Endolimax nanus cysts and Endolimax nanus trophozoite (drawings); cysts in iodine; unstained wet mount",
   "أكياس الأميبا القزمة وطورها المتغذّي (رسوم)؛ أكياس باليود؛ تحضير رطب غير مصبوغ", h="38mm", fit="contain"),
 F("enana-fig-ab.jpg", "Endolimax nana; A. Vegetative form; B. Quadrinucleate cyst — Food vacuole containing bacteria; Nucleus",
   "الأميبا القزمة؛ A. الطور الخضري؛ B. الكيس رباعي الأنوية — فجوة غذائية تحتوي بكتيريا؛ النواة", h="44mm", fit="contain"),
 INSHORT([("Lumen of the **large intestine** of man, primates and pigs; prevalence **10-20%**; 3 stages: troph, pre-cyst, cyst.", "تجويف **الأمعاء الغليظة** للإنسان والرئيسيات والخنازير؛ الانتشار **10-20%**؛ 3 أطوار: متغذّي، ما قبل الكيس، كيس."),
          ("Troph **6-15 µm**, central nucleus, sluggish; **no chromatoid bars and no glycogen vacuole**.", "المتغذّي **6-15 مايكرومتر**، نواة مركزية، بطيء؛ **بلا قضبان كروماتينية وبلا فجوة غلايكوجين**."),
          ("Cyst **oval, 5-14 µm, 4 indistinct nuclei**.", "الكيس **بيضوي، 5-14 مايكرومتر، 4 أنوية غير واضحة**.")]),

 # ───────────────────────── 5. Iodamoeba
 SEC("Iodamoeba Buetschlii", "أميبا بوتشلي اليودية"),
 L(["This is widely distributed, though less common than E. coli and E. nana."],
   ["وهي واسعة الانتشار، لكنها أقل شيوعًا من الأميبا القولونية والقزمة."]),
 L(["The trophozoite is small, 6–12 µm, with clear nucleus.",
    ["The cyst is oval, uninucleate, and has a prominent iodine staining glycogen mass (**iodophilic body**).", "Hence, the name ‘Iodamoeba’."]],
   ["الطور المتغذّي **صغير، 6–12 مايكرومتر**، بنواة واضحة.",
    ["الكيس **بيضوي أحادي النواة**، وفيه كتلة غلايكوجين بارزة تتصبّغ باليود (**الجسم المحبّ لليود**).", "ومن هنا جاء اسم ‘الأميبا اليودية’."]], start=2),
 FF(("iod-figure.jpg", "Iodamoeba buetschlii: trophozoite (left; Size 6-20 µ, Average 12µ) and cyst (right; Size 5-18µ, Average 10µ) — Food Vacuole; Nucleus; Glycogen Vacuole",
     "أميبا بوتشلي اليودية: الطور المتغذّي (يسار؛ الحجم 6-20، المتوسط 12) والكيس (يمين؛ الحجم 5-18، المتوسط 10 مايكرومتر) — فجوة غذائية؛ النواة؛ فجوة الغلايكوجين", "58mm"),
    ("iod-cyst.jpg", "Iodamoeba butschlii cyst", "كيس أميبا بوتشلي اليودية", "58mm")),
 INSHORT([("Widely distributed but **less common than E. coli and E. nana**.", "واسعة الانتشار لكنها **أقل شيوعًا من القولونية والقزمة**."),
          ("Troph **6-12 µm**, clear nucleus; cyst **oval, uninucleate** with a big **glycogen mass** that stains with iodine.", "المتغذّي **6-12 مايكرومتر** بنواة واضحة؛ الكيس **بيضوي أحادي النواة** فيه **كتلة غلايكوجين** كبيرة تتصبّغ باليود."),
          ("**Iodophilic body** → the name **Iodamoeba**.", "**الجسم المحبّ لليود** ← اسم **الأميبا اليودية**.")]),

 # ───────────────────────── 6. comparison (BIOS)
 SEC("The four amoebae at a glance", "الأميبات الأربع بنظرة واحدة"),
 T([B("Amoeba", "الأميبا"), B("Trophozoite", "الطور المتغذّي"), B("Cyst", "الكيس"), B("Key point", "النقطة المميّزة")],
   [[B("**E. coli**", "القولونية"), B("15- 50 µm, sluggish, large eccentric karyosome", "15-50، بطيء، جسيم نووي كبير لا مركزي"), B("10-31 µm, 8 nuclei", "10-31، 8 أنوية"), B("evidence of fecal ingestion", "دليل ابتلاع مادة برازية")],
    [B("**E. gingivalis**", "اللثوية"), B("5- 25 µm, active, central karyosome", "5-25، نشط، جسيم نووي مركزي"), B("No cyst stage", "لا يوجد كيس"), B("gums and teeth; kissing", "اللثة والأسنان؛ التقبيل")]],
   key_cols=[0], widths=[19, 30, 27, 24], style="summary", label_en="Sizes in µm", label_ar="الأحجام بالمايكرومتر"),
 T([B("Amoeba", "الأميبا"), B("Trophozoite", "الطور المتغذّي"), B("Cyst", "الكيس"), B("Key point", "النقطة المميّزة")],
   [[B("**Endolimax nana**", "القزمة"), B("6- 15µm, sluggish", "6-15، بطيء"), B("5- 14 µm, oval, 4 indistinct nuclei", "5-14، بيضوي، 4 أنوية غير واضحة"), B("no chromatoid bars", "بلا قضبان كروماتينية")],
    [B("**Iodamoeba Buetschlii**", "بوتشلي اليودية"), B("6–12 µm, clear nucleus", "6–12، نواة واضحة"), B("oval, uninucleate", "بيضوي، أحادي النواة"), B("iodophilic body", "الجسم المحبّ لليود")]],
   key_cols=[0], widths=[19, 30, 27, 24], style="summary", label_en="Sizes in µm (cont.)", label_ar="الأحجام بالمايكرومتر (تكملة)"),
 INSHORT([("Nuclei in the cyst: **E. coli 8**, **E. nana 4**, **Iodamoeba 1**, **E. gingivalis — no cyst**.", "أنوية الكيس: **القولونية 8**، **القزمة 4**، **اليودية 1**، **اللثوية — بلا كيس**."),
          ("Only **E. gingivalis** lives in the **mouth**; the others live in the **large intestine**.", "فقط **اللثوية** تعيش في **الفم**؛ والبقية في **الأمعاء الغليظة**.")]),

 # ───────────────────────── 7. Naegleria fowleri
 SEC("Naegleria fowleri", "النيغلرية الفاولرية"),
 C("Naegleria is a freeliving amoeba, typically found in warm fresh water, such as ponds, lakes, rivers and hot springs.",
   "النيغلرية أميبا **حرّة المعيشة**، توجد عادةً في **المياه العذبة الدافئة** مثل البرك والبحيرات والأنهار و**الينابيع الحارّة**."),
 C("It is also found in soil, near warmwater discharges of industrial plants and swimming pools.",
   "وتوجد أيضًا في **التربة**، وقرب تصريفات المياه الدافئة للمنشآت الصناعية، وفي **أحواض السباحة**."),
 C(["Only one species, N. fowleri, is known to cause infection, although two other species, N. australiensis and N. italica, can cause infection in mice N. fowleri (also known as “the braineating amoeba”) is first described by physicians M. Fowler (hence named as fowleri) and R.F. Carter in Australia in 1965."],
   ["نوع واحد فقط هو **النيغلرية الفاولرية** معروف بأنه يسبّب الإصابة، مع أن نوعين آخرين هما **النيغلرية الأسترالية** و**النيغلرية الإيطالية** يمكن أن يسبّبا الإصابة في **الفئران**؛ و**النيغلرية الفاولرية** (المعروفة أيضًا بـ“**الأميبا آكلة الدماغ**”) وصفها أول مرة الطبيبان **فاولر** (ومنه جاء اسم `fowleri`) و**كارتر** في **أستراليا عام 1965**."]),
 H2("Morphology", "الشكل"),
 C("Naegleria fowleri exists in nature as cyst and trophozoite forms", "توجد النيغلرية الفاولرية في الطبيعة بشكلَي **الكيس والطور المتغذّي**"),
 F("naeg-forms.jpg", "Naegleria fowleri: amoeboid trophozoite (Lobopodia; Nucleolus; Nucleus; Karyosome; Food vacuole; Contractile vacuole), flagellated trophozoite (Flagella) and cyst (Thick smooth double layered cyst wall)",
   "النيغلرية الفاولرية: الطور المتغذّي الأميبي (أقدام فصّية؛ النوية؛ النواة؛ الجسيم النووي؛ فجوة غذائية؛ فجوة متقلّصة)، والطور المسوط (الأسواط)، والكيس (جدار كيس سميك أملس ثنائي الطبقة)", h="38mm", fit="contain"),
 *[C(e, a) for e, a in zip(["**Trophozoite Stage:** The trophozoites occur in two forms, amoeboid and flagellated form. Both measure 8–15 µm.",
    "**Amoeboid form:** It is the only recognizable form in humans. It possesses lobate pseudopodia (called as **lobopodia**). Cyto plasm is granular with food vacuoles; nucleus shows central karyosome and no peripheral chromatin. It is the only replicating form and it divides by binary fission (Fig. 3.15 A)",
    "**Flagellated form:** When the amoeboid forms are exposed to a change in ionic concentration such as placement in distilled water at 27–37°C, they transform [[cut]]"],
   ["**طور المتغذّي:** تظهر الأطوار المتغذّية بشكلين، **أميبي ومسوط**. وكلاهما يبلغ **8–15 مايكرومتر**.",
    "**الشكل الأميبي:** هو **الشكل الوحيد الذي يُعرف في الإنسان**. ويملك أقدامًا كاذبة مفصّصة (تسمّى **الأقدام الفصّية**). السايتوبلازم محبّب فيه فجوات غذائية؛ والنواة تُظهر **جسيمًا نوويًا مركزيًا ولا كروماتين محيطي**. وهو **الشكل الوحيد المتكاثر** وينقسم **بالانشطار الثنائي** (الشكل 3.15 A)",
    "**الشكل المسوط:** عندما تتعرّض الأشكال الأميبية لتغيّر في التركيز الأيوني مثل وضعها في **الماء المقطّر بدرجة 27–37°م**، فإنها تتحوّل [[قطع]]"])],
 BN("The slide stops at “they transform”; the next words are missing in the file.", "تتوقّف الشريحة عند “they transform”؛ وبقية الكلام غير موجودة في الملف."),
 H2("Life cycle of Naegleria fowleri", "دورة حياة النيغلرية الفاولرية"),
 F("naeg-cycle.jpg", "Life cycle of Naegleria fowleri", "دورة حياة النيغلرية الفاولرية", h="48mm", fit="contain"),
 T([B("Step", "الخطوة"), B("Step", "الخطوة")],
   LB(("1. Free living amoeboid trophozoites in water", "1. أطوار متغذّية أميبية حرّة المعيشة في الماء"), ("2. Human infection by inhalation (during swimming)", "2. إصابة الإنسان بالاستنشاق (أثناء السباحة)"),
      ("3. Penetration of nasal mucosa", "3. اختراق الغشاء المخاطي للأنف"), ("4. Olfactory nerve infection", "4. إصابة العصب الشمّي"),
      ("5. Brain", "5. الدماغ"), ("6. Primary amoebic meningoencephalitis", "6. التهاب السحايا والدماغ الأميبي الأولي"), ("7. Death", "7. الوفاة")),
   style="summary", label_en="Labels in the figure (in order)", label_ar="كتابات الشكل (بالترتيب)"),

 H2("Laboratory Diagnosis", "التشخيص المختبري"),
 L(["***Cerebrospinal fl uid analysis***",
    "CSF is thick purulent, with polymorphonuclear cells more than 20,000/µl, elevated protein and reduced sugar level (mimic bacterial menin gitis).",
   ],
   ["***تحليل السائل الدماغي الشوكي***",
    "يكون السائل الدماغي الشوكي **سميكًا قيحيًا**، فيه خلايا متعدّدة أشكال النواة **أكثر من 20,000/مايكرولتر**، و**بروتين مرتفع وسكر منخفض** (يحاكي **التهاب السحايا البكتيري**)."]),
 L(["***Microscopy***",
    "**Direct microscopy: Motile amoeboid** trophozoites can be demonstrated in wet mount preparation of CSF made with cover slip (counting chamber is not used as trophozites in CSF mimic leucocytes) Other forms are not seen in CSF"],
   ["***الفحص المجهري***",
    "**الفحص المجهري المباشر:** يمكن إظهار **الأطوار المتغذّية الأميبية المتحرّكة** في تحضير رطب للسائل الدماغي الشوكي مغطّى بغطاء شريحة (لا تُستعمل **حجرة العدّ** لأن الأطوار المتغذّية في السائل **تحاكي كريات البيض**) ولا تُشاهد الأشكال الأخرى في السائل الدماغي الشوكي"], start=3),
 L(["Care should be taken to diff erentiate the trophozoites from leukocytes. Motile trophozoite containing a spherical nucleus with large karyosome is the clue for identifi cation",
    "**Phase contrast microscope yields better** result than light microscope. (Fig. A)",
    "**Histopathological staining (Wright’s or** Giemsa) of CSF or brain biopsied tissue may demonstrate trophozoites with sky blue cytoplasm with a pink nucleus (Fig. B)"],
   ["يجب الحرص على **تمييز الأطوار المتغذّية عن كريات البيض**. و**الطور المتغذّي المتحرّك ذو النواة الكروية والجسيم النووي الكبير** هو مفتاح التشخيص",
    "**مجهر التباين الطوري يعطي نتيجة أفضل** من المجهر الضوئي. (الشكل A)",
    "**الصبغ النسيجي المرضي (رايت أو** كيمزا) للسائل الدماغي الشوكي أو لنسيج خزعة الدماغ قد يُظهر أطوارًا متغذّية **بسايتوبلازم أزرق سماوي ونواة وردية** (الشكل B)"],
   en="Conti…..", ar="تكملة….."),
 L(["Refrigeration is not recommended if there is a delay in examining the CSF  If the parasite load is low then CSF can be centrifuged at low speed (150 rpm for 5 minutes). Trophozoites are not damaged, they only lose their pseudopodia  Trophozoites can also be demonst rated by direct fluorescence anti body staining of centrifuged CSF using monoclonal antibody."],
   ["**لا يُنصح بالتبريد** إذا تأخّر فحص السائل الدماغي الشوكي؛ وإذا كان حمل الطفيلي قليلًا يمكن **نبذ السائل بسرعة منخفضة (150 دورة/دقيقة لمدة 5 دقائق)**. لا تتضرّر الأطوار المتغذّية، بل تفقد أقدامها الكاذبة فقط؛ ويمكن أيضًا إظهار الأطوار المتغذّية **بصبغة الأضداد المتألّقة المباشرة** للسائل المنبوذ باستعمال **ضدّ وحيد النسيلة**."],
   en="Conti……", ar="تكملة……"),
 F("naeg-fig-ab.jpg", "Figs A and B: Naegleria fowleri (A) saline mount (phase contrast microscopy) top—flagellated trophozoite, below—amoeboid trophozoite; (B) arrow shows amoeboid rophozoite (hematoxylin and eosin stain)",
   "الشكلان A وB: النيغلرية الفاولرية (A) تحضير ملحي (مجهر التباين الطوري) في الأعلى طور متغذّي مسوط وفي الأسفل طور متغذّي أميبي؛ (B) يشير السهم إلى طور متغذّي أميبي (صبغة الهيماتوكسيلين والأيوسين)", h="49mm", fit="contain"),
 L([["***Culture:*** CSF sample can be cultivated on **nonnutrient agar (Page’s saline and 1.5% agar), lawn** cultured with bacterial supplement like E. coli.", "Naegleria feeds on bacteria and crawls over the lawn culture of E. coli to produce trails (**Trail sign).**"]],
   [    ["***الزرع:*** يمكن زرع عيّنة السائل الدماغي الشوكي على **أكار غير مغذٍّ (محلول بيج الملحي و1.5% أكار)، مفروش** بمزرعة بكتيرية مضافة مثل **الإشريكية القولونية**.", "تتغذّى النيغلرية على البكتيريا وتزحف فوق المزرعة المفروشة من الإشريكية القولونية فتترك مسارات (**علامة المسار).**"]], start=2),
 BN(["Words split by spaces such as “fl uid”, “menin gitis”, “diff erentiate”, “identifi cation”, “demonst rated” and “anti body” are copied as they appear in the slides (fluid, meningitis, differentiate, identification, demonstrated, antibody).",
     "Here **E. coli** in the culture is the bacterium **Escherichia coli**, not the amoeba Entamoeba coli."],
    ["الكلمات المقطّعة بفراغات مثل “fl uid” و“menin gitis” و“diff erentiate” و“identifi cation” و“demonst rated” و“anti body” منقولة كما في الشرائح (أي: سائل، التهاب السحايا، يميّز، التشخيص، أُظهر، ضدّ).",
     "و**E. coli** هنا في الزرع هي بكتيريا **الإشريكية القولونية** وليست الأميبا القولونية."]),
 INSHORT([("**Free-living** amoeba of **warm fresh water**, soil and swimming pools; “the **brain-eating amoeba**”; described by **Fowler and Carter, Australia 1965**.", "أميبا **حرّة المعيشة** في **المياه العذبة الدافئة** والتربة وأحواض السباحة؛ “**الأميبا آكلة الدماغ**”؛ وصفها **Fowler وCarter في أستراليا 1965**."),
          ("Forms: **cyst + trophozoite** (amoeboid and flagellated, **8-15 µm**); only the **amoeboid** form is seen in humans and replicates (binary fission).", "الأشكال: **كيس + متغذّي** (أميبي ومسوط، **8-15 مايكرومتر**)؛ والشكل **الأميبي** وحده يُرى في الإنسان ويتكاثر (انشطار ثنائي).")]),
 INSHORT([("Infection: **inhalation while swimming** → nasal mucosa → **olfactory nerve** → brain → **PAM** → death.", "الإصابة: **الاستنشاق أثناء السباحة** ← المخاطية الأنفية ← **العصب الشمّي** ← الدماغ ← **التهاب السحايا والدماغ الأميبي الأولي** ← الوفاة."),
          ("CSF: purulent, PMN **> 20,000/µl**, ↑ protein, ↓ sugar; wet mount with cover slip (**no counting chamber**); phase contrast is better.", "السائل الدماغي الشوكي: قيحي، متعدّدة النوى **> 20,000/مايكرولتر**، ↑ البروتين، ↓ السكر؛ تحضير رطب بغطاء شريحة (**بلا حجرة عدّ**)؛ والتباين الطوري أفضل."),
          ("**No refrigeration**; centrifuge at **150 rpm / 5 min**; culture on **nonnutrient agar + E. coli lawn → Trail sign**.", "**لا تبريد**؛ نبذ **150 دورة/دقيقة لمدة 5 دقائق**؛ الزرع على **أكار غير مغذٍّ + مزرعة إشريكية ← علامة المسار**.")], en="In short (cont.)", ar="باختصار (تكملة)"),

 *TERMS6([("Non-pathogenic / Commensal", "غير ممرض / متعايش / مُعايش غير ضار"),
         ("Trophozoite", "الطور المتغذّي / الطور الخضري / الطور النشط"),
         ("Cyst / Pre-cyst", "الكيس / ما قبل الكيس / الطور المتكيّس"),
         ("Karyosome", "الجسيم النووي / الكاريوسوم / النُّوَيّة الكاذبة"),
         ("Eccentric", "لا مركزي / منحرف عن المركز"),
         ("Peripheral chromatin", "الكروماتين المحيطي / كروماتين الحافة"),
         ("Chromatoid body", "الجسم الكروماتيني / القضيب الكروماتيني"),
         ("Splinter shape", "شظوي الشكل / يشبه الشظايا"),
         ("Iodophilic body", "الجسم المحبّ لليود / كتلة الغلايكوجين المتصبّغة باليود"),
         ("Definitive host", "المضيف النهائي / المضيف الأساسي"),
         ("Intermediate host", "المضيف الوسطي / المضيف الثانوي"),
         ("Formol-ether concentration", "التركيز بالفورمول-إيثر / طريقة الفورمالين-إيثر"),
         ("Permanent stained preparation", "تحضير مصبوغ دائم / مسحة مصبوغة دائمة"),
         ("Gingival tissue", "النسيج اللثوي / نسيج اللثة"),
         ("Intrauterine device", "اللولب / وسيلة منع الحمل داخل الرحم"),
         ("Free-living amoeba", "أميبا حرّة المعيشة / أميبا غير متطفّلة"),
         ("Lobopodia", "الأقدام الفصّية / الأقدام الكاذبة المفصّصة"),
         ("Flagellated form", "الشكل المسوط / الطور السوطي"),
         ("Primary amoebic meningoencephalitis (PAM)", "التهاب السحايا والدماغ الأميبي الأولي"),
         ("Olfactory nerve", "العصب الشمّي"),
         ("Purulent CSF", "سائل دماغي شوكي قيحي / صديدي"),
         ("Phase contrast microscope", "مجهر التباين الطوري / المجهر متباين الأطوار"),
         ("Nonnutrient agar", "أكار غير مغذٍّ / وسط أكار فقير"),
         ("Trail sign", "علامة المسار / علامة الأثر")]),
]

# species names in bold italic (English only, never inside a bold run)
SPECIES = re.compile(r"\b(?:(?:Entamoeba|Endolimax\.?|Iodamoeba|Naegleria|E\.|I\.|N\.) (?:coli|histolytica|gingivalis|nana|nanus|dispar|hartmanni|butschlii|buetschlii|Buetschlii|fowleri|australiensis|italica)|Naegleria)\b")
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
    if b.get("t") in ("section",): continue
    for k in ("en", "list_en"):
        if k in b: b[k] = walk_it(b[k])
    if b.get("t") == "table":
        b["rows"] = [[[ital(c[0]), c[1]] if isinstance(c, list) else c for c in r] for r in b["rows"]]

exec(open(__file__.replace("pl4.py", "pl4q.py")).read())

```
