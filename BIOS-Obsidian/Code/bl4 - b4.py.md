---
source: BIOS-Obsidian/tools/scripts/bl4/b4.py
handouts: [bacteriology-lab4-identification]
saved: 2026-11-12
tags: [bios, code]
---
# bl4/b4.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#bacteriology-lab4-identification|bacteriology-lab4-identification]]

```python
import sys; sys.path.insert(0, "/tmp/claude-0/-home-user-kwmdkm/a7dd109e-db53-5fd3-8234-9dab3a530e24/scratchpad/imm456")
from ci import *            # c helpers + B INSHORT TERMS balance save(split.fix)
sys.path.insert(0, "/tmp/claude-0/-home-user-kwmdkm/a7dd109e-db53-5fd3-8234-9dab3a530e24/scratchpad"); from bidi import ltr_all; from flowfit import fit

# Diagnostic Microbiology practical, lab 4 — slides "Microbiological Methods for Identification Lab 4" (15 slides, no figures,
# no questions; prepared by MSc. Ali Thamer kamil and MSc. haba sami). Fourth stage → wineoat + separate question file.
split.ABBR = split.ABBR + ("MSc.",)          # "MSc. Ali" is not a sentence end
BN = lambda en, ar: N(en, ar, label=["BIOS note", "ملاحظة BIOS"])
HL = lambda en, ar: N(en, ar, label=["Highlighted in the slides", "مُظلَّل في الشرائح"])
O = P

blocks = [
 # ───────────────────────── 1
 SEC("Introduction", "المقدّمة"),
 N("Prepared by MSc. Ali Thamer kamil · MSc. haba sami", "إعداد: م. علي ثامر كامل · م. هبة سامي", label=["Lab sheet", "ورقة العملي"]),
 L(["Microbiological identification determines the type, **genus**, or **species** of **microorganisms**.",
    "It is essential for **disease diagnosis**, **antimicrobial selection**, food safety, and **microbial research**.",
    "Combines **classical** (phenotypic) and **modern** (molecular) methods for accuracy."],
   ["يحدّد التشخيص (التعريف) الميكروبي نوع **الأحياء المجهرية** أو **جنسها** أو **نوعها**.",
    "وهو أساسي لـ**تشخيص المرض**، و**اختيار المضادّ الميكروبي**، وسلامة الغذاء، و**البحث الميكروبي**.",
    "ويجمع بين الطرائق **التقليدية** (المظهرية) و**الحديثة** (الجزيئية) لتحقيق الدقّة."]),
 H2("Objectives of Microbial Identification", "أهداف التشخيص الميكروبي"),
 L(["**Determine** etiologic agents of infection", "**Understand** microbial **diversity** and **taxonomy**", "Guide **therapy** and **infection control**", "Trace outbreaks and perform surveillance"],
   ["**تحديد** العوامل المسبّبة للعدوى", "**فهم** **التنوّع** الميكروبي و**التصنيف**", "توجيه **العلاج** و**مكافحة العدوى**", "تتبّع الفاشيات (التفشّيات) وإجراء الترصّد"]),
 H2("General Steps in Identification", "الخطوات العامة في التشخيص"),
 L(["**Sample Collection** – Aseptic techniques to avoid contamination", "**Microscopic Examination** – Morphology and staining", "**Cultivation** – Selective and differential media",
    "**Biochemical Characterization** – Metabolic profiling", "**Serological Testing** – Antigen or antibody detection", "**Molecular Identification** – DNA/RNA based methods"],
   ["**جمع العيّنة** – تقنيات معقّمة لتجنّب التلوّث", "**الفحص المجهري** – الشكل والتصبيغ", "**الزرع** – أوساط انتقائية وتفريقية",
    "**التوصيف الكيميائي الحيوي** – التنميط الأيضي", "**الفحص المصلي** – كشف المستضدّ أو الضدّ", "**التشخيص الجزيئي** – طرائق مبنية على `DNA/RNA`"]),
 FLOW([("Sample", "العيّنة"), ("Microscopy", "المجهر"), ("Culture", "الزرع"), ("Biochemical", "الكيميائية الحيوية"), ("Serological", "المصلية"), ("Molecular", "الجزيئية")],
      en="6 general steps", ar="الخطوات العامة الست"),
 INSHORT([("Identification = **type, genus or species** of the microorganism.", "التشخيص = **نوع الميكروب أو جنسه أو نوعه**."),
          ("Uses: **diagnosis, antimicrobial selection**, food safety, research.", "الاستعمالات: **التشخيص، واختيار المضادّ**، وسلامة الغذاء، والبحث."),
          ("6 steps: **sample → microscopy → culture → biochemical → serological → molecular**.", "6 خطوات: **عيّنة ← مجهر ← زرع ← كيميائية حيوية ← مصلية ← جزيئية**.")]),

 # ───────────────────────── 2
 SEC("Microscopy and culture", "الفحص المجهري والزرع"),
 H2("Classical (Phenotypic) Methods: Microscopic Examination", "الطرائق التقليدية (المظهرية): الفحص المجهري"),
 HL("This slide title is highlighted in the original — microscopic examination is important for the exam.", "عنوان هذه الشريحة مُظلَّل في الأصل — الفحص المجهري مهم للامتحان."),
 L(["**Gram Stain**: Differentiates Gram-positive (**purple**) and Gram-negative (**pink**)", "**Acid-Fast Stain**: Detects **Mycobacterium**",
    "**Special Stains**: Endospore, Capsule, and Flagella for structure identification"],
   ["**صبغة غرام**: تفرّق بين موجبة غرام (**بنفسجية**) وسالبة غرام (**وردية**)", "**الصبغة الصامدة للحامض**: تكشف **المتفطّرة (`Mycobacterium`)**",
    "**الصبغات الخاصة**: للأبواغ الداخلية والمحفظة والأسواط، لتحديد التراكيب"]),
 H2("Cultural Characteristics", "الصفات الزرعية"),
 L(["**Colony morphology**: size, color, texture, elevation", "**Growth conditions**: aerobic, anaerobic, microaerophilic",
    "**Hemolysis patterns on blood agar**: α, β, γ", "Pigment and odor production"],
   ["**شكل المستعمرة**: الحجم واللون والقوام والارتفاع", "**ظروف النموّ**: هوائي، ولاهوائي، ومحبّ للهواء القليل",
    "**أنماط تحلّل الدم على آغار الدم**: `α` و`β` و`γ`", "إنتاج الصبغة والرائحة"]),
 T([B("Hemolysis", "تحلّل الدم"), B("What is seen on blood agar", "ما يُرى على آغار الدم"), B("Example", "مثال")],
   [[B("**α (alpha)**", "**ألفا**"), B("partial — greenish zone", "جزئي — منطقة مخضرّة"), B("__Streptococcus pneumoniae__", "`__Streptococcus pneumoniae__`")],
    [B("**β (beta)**", "**بيتا**"), B("complete — clear zone", "كامل — منطقة شفّافة"), B("__Streptococcus pyogenes__", "`__Streptococcus pyogenes__`")],
    [B("**γ (gamma)**", "**غاما**"), B("none — no change", "لا تحلّل — لا تغيّر"), B("__Enterococcus__", "`__Enterococcus__`")]],
   key_cols=[0], widths=[22, 42, 36], style="summary", label_en="BIOS: the three hemolysis patterns", label_ar="BIOS: أنماط تحلّل الدم الثلاثة"),
 INSHORT([("Gram: positive **purple**, negative **pink**; acid-fast → **Mycobacterium**.", "غرام: الموجبة **بنفسجية** والسالبة **وردية**؛ والصامدة للحامض ← **المتفطّرة**."),
          ("Special stains: **endospore, capsule, flagella**.", "الصبغات الخاصة: **الأبواغ والمحفظة والأسواط**."),
          ("Culture: colony morphology, O₂ needs, **α / β / γ hemolysis**, pigment and odor.", "الزرع: شكل المستعمرة، والحاجة للأوكسجين، وتحلّل **`α / β / γ`**، والصبغة والرائحة.")]),

 # ───────────────────────── 3
 SEC("Biochemical identification", "التشخيص الكيميائي الحيوي"),
 HL("The whole list of biochemical tests is highlighted in the original slides — learn each test with its example.", "قائمة الفحوص الكيميائية الحيوية كلها مُظلَّلة في الشرائح الأصلية — احفظ كل فحص مع مثاله."),
 L(["**Catalase**: EX __Staphylococcus__ (+) vs. __Streptococcus__ (–)", "**Oxidase**:EX __Pseudomonas__ (+), __Neisseria__ (+)", "**Indole**: EX __E. coli__ (+)",
    "**Urease**: __Proteus__ (+)", "**Citrate**:EX __Enterobacter__ (+)", "**TSI Agar**: EX Sugar fermentation and H₂S production", "**Coagulase**:EX __S. aureus__ (+)"],
   ["**الكاتاليز**: مثال `__Staphylococcus__` (+) مقابل `__Streptococcus__` (–)", "**الأوكسيديز**: مثال `__Pseudomonas__` (+)، و`__Neisseria__` (+)", "**الإندول**: مثال `__E. coli__` (+)",
    "**اليوريز**: `__Proteus__` (+)", "**السترات**: مثال `__Enterobacter__` (+)", "**آغار `TSI`**: مثال تخمير السكّر وإنتاج `H₂S`", "**التخثّر (الكواغيوليز)**: مثال `__S. aureus__` (+)"],
   en="Biochemical tests determine **bacterial metabolism**:", ar="تحدّد الفحوص الكيميائية الحيوية **أيض البكتيريا**:"),
 H2("Common Biochemical Tests", "الفحوص الكيميائية الحيوية الشائعة"),
 T([B("Test", "الفحص"), B("Purpose", "الغرض"), B("Example", "مثال")],
   [[B("**Catalase**", "**الكاتاليز**"), B("Detects catalase enzyme", "يكشف إنزيم الكاتاليز"), B("__Staphylococcus__ (+)", "`__Staphylococcus__` (+)")],
    [B("**Oxidase**", "**الأوكسيديز**"), B("Detects cytochrome oxidase", "يكشف السايتوكروم أوكسيديز"), B("__Pseudomonas__ (+)", "`__Pseudomonas__` (+)")],
    [B("**Urease**", "**اليوريز**"), B("Detects urea hydrolysis", "يكشف تحلّل اليوريا"), B("__Proteus__ (+)", "`__Proteus__` (+)")]],
   key_cols=[0], widths=[22, 44, 34]),
 T([B("Test", "الفحص"), B("Positive example", "مثال موجب"), B("How it reads (BIOS)", "كيف يُقرأ (BIOS)")],
   [[B("**Catalase**", "**الكاتاليز**"), B("__Staphylococcus__ (+); __Streptococcus__ (–)", "`__Staphylococcus__` (+)؛ `__Streptococcus__` (–)"), B("bubbles with H₂O₂", "فقاعات مع `H₂O₂`")],
    [B("**Oxidase**", "**الأوكسيديز**"), B("__Pseudomonas__, __Neisseria__", "`__Pseudomonas__`، `__Neisseria__`"), B("purple colour on the reagent", "لون بنفسجي على الكاشف")],
    [B("**Indole**", "**الإندول**"), B("__E. coli__", "`__E. coli__`"), B("red ring with Kovac's reagent", "حلقة حمراء مع كاشف كوفاكس")],
    [B("**Urease**", "**اليوريز**"), B("__Proteus__", "`__Proteus__`"), B("pink medium (urea → ammonia)", "وسط وردي (يوريا ← أمونيا)")],
    [B("**Citrate**", "**السترات**"), B("__Enterobacter__", "`__Enterobacter__`"), B("green → blue (Simmons citrate)", "أخضر ← أزرق (سترات سيمونز)")],
    [B("**TSI**", "**`TSI`**"), B("sugar fermentation, H₂S (e.g. __Salmonella__ H₂S +)", "تخمير السكّر و`H₂S` (مثل `__Salmonella__` موجبة `H₂S`)"), B("yellow = acid, black = H₂S", "أصفر = حامض، أسود = `H₂S`")],
    [B("**Coagulase**", "**التخثّر**"), B("__S. aureus__", "`__S. aureus__`"), B("plasma clots", "تخثّر البلازما")]],
   key_cols=[0], widths=[18, 44, 38], style="summary", label_en="BIOS: all 7 tests with the result to look for", label_ar="BIOS: الفحوص السبعة مع النتيجة المطلوبة"),
 BN("For **TSI** the slide gives \"EX\" without an organism; a common example is __Salmonella__ (H₂S positive, black butt).",
    "في **`TSI`** كتبت الشريحة \"EX\" بلا كائن؛ ومثال شائع `__Salmonella__` (موجبة `H₂S`، قاع أسود)."),
 INSHORT([("**Catalase**: Staph + / Strep –; **coagulase**: S. aureus +.", "**الكاتاليز**: العنقودية + / العقدية –؛ و**التخثّر**: `S. aureus` +."),
          ("**Oxidase**: Pseudomonas, Neisseria +; **indole**: E. coli +.", "**الأوكسيديز**: الزائفة والنيسرية +؛ و**الإندول**: `E. coli` +."),
          ("**Urease**: Proteus +; **citrate**: Enterobacter +; **TSI**: sugars + H₂S.", "**اليوريز**: المتقلّبة +؛ و**السترات**: الأمعائية +؛ و**`TSI`**: السكّريات + `H₂S`.")]),

 # ───────────────────────── 4
 SEC("Serological and molecular", "المصلية والجزيئية"),
 H2("Serological Identification", "التشخيص المصلي"),
 L(["**Agglutination tests**: __Salmonella__, __Shigella__ typing", "**Latex agglutination**: __Streptococcus__ grouping",
    "**ELISA**: Detects bacterial toxins/antigens", "**Western Blot**: Confirms microbial proteins"],
   ["**فحوص التلازن**: تنميط `__Salmonella__` و`__Shigella__`", "**تلازن اللاتكس**: تصنيف `__Streptococcus__` إلى مجاميع",
    "**الإليزا**: تكشف السموم/المستضدّات البكتيرية", "**اللطخة الغربية**: تؤكّد البروتينات الميكروبية"]),
 C("**Advantages**: Rapid, specific, sensitive.", "**المزايا**: سريع ونوعي وحسّاس."),
 H2("Molecular Identification Methods", "طرائق التشخيص الجزيئي"),
 L(["**PCR**: Amplifies specific DNA sequences", "**DNA Hybridization**: Uses complementary DNA probes", "**Microarrays**: Identify multiple pathogens simultaneously"],
   ["**`PCR`**: يضاعف تسلسلات `DNA` محدّدة", "**تهجين `DNA`**: يستعمل مجسّات `DNA` متمّمة", "**المصفوفات الدقيقة**: تشخّص مُمْرِضات متعدّدة في آنٍ واحد"]),
 T([B("Method", "الطريقة"), B("What it detects / does", "ماذا يكشف / يعمل"), B("Example use", "مثال الاستعمال")],
   [[B("**Agglutination**", "**التلازن**"), B("antigen + specific antiserum → clumps", "مستضدّ + مصل مضاد نوعي ← تكتّلات"), B("__Salmonella__, __Shigella__ typing", "تنميط `__Salmonella__` و`__Shigella__`")],
    [B("**Latex agglutination**", "**تلازن اللاتكس**"), B("antibody-coated latex beads", "حبيبات لاتكس مغلّفة بالأضداد"), B("__Streptococcus__ grouping", "تصنيف `__Streptococcus__`")],
    [B("**ELISA**", "**الإليزا**"), B("toxins / antigens (enzyme colour)", "سموم / مستضدّات (لون إنزيمي)"), B("bacterial toxins", "السموم البكتيرية")],
    [B("**Western blot**", "**اللطخة الغربية**"), B("specific proteins", "بروتينات محدّدة"), B("confirmation", "التأكيد")],
    [B("**PCR**", "**`PCR`**"), B("amplifies a DNA sequence", "يضاعف تسلسل `DNA`"), B("one target", "هدف واحد")],
    [B("**Microarray**", "**المصفوفة الدقيقة**"), B("many probes at once", "مجسّات كثيرة دفعة واحدة"), B("multiple pathogens", "مُمْرِضات متعدّدة")]],
   key_cols=[0], widths=[24, 42, 34], style="summary", label_en="Serological vs molecular", label_ar="المصلية مقابل الجزيئية"),
 INSHORT([("Serological: **agglutination, latex, ELISA, Western blot** — rapid, specific, sensitive.", "المصلية: **التلازن، واللاتكس، والإليزا، واللطخة الغربية** — سريعة ونوعية وحسّاسة."),
          ("Molecular: **PCR** (amplify), **hybridization** (probes), **microarrays** (many pathogens).", "الجزيئية: **`PCR`** (مضاعفة)، و**التهجين** (مجسّات)، و**المصفوفات** (مُمْرِضات كثيرة).")]),

 # ───────────────────────── 5
 SEC("Automation and AST", "الأنظمة الآلية وفحص الحساسية"),
 H2("Automated Identification Systems", "أنظمة التشخيص الآلية"),
 L(["VITEK 2", "BD Phoenix", "MicroScan WalkAway", "MALDI-TOF MS"], ["`VITEK 2`", "`BD Phoenix`", "`MicroScan WalkAway`", "`MALDI-TOF MS` (مطيافية الكتلة)"],
   en="Modern systems for rapid identification:", ar="أنظمة حديثة للتشخيص السريع:"),
 C("Combine **accuracy, speed**, and **antimicrobial susceptibility testing**.", "تجمع بين **الدقّة والسرعة** و**فحص الحساسية للمضادّات الميكروبية**."),
 BN("**MALDI-TOF MS** identifies a colony in minutes from its **protein mass spectrum** (a \"fingerprint\" compared with a database).",
    "**`MALDI-TOF MS`** يشخّص المستعمرة خلال دقائق من **طيف كتلة بروتيناتها** (\"بصمة\" تُقارن بقاعدة بيانات)."),
 H2("Antimicrobial Susceptibility Testing (AST)", "فحص الحساسية للمضادّات الميكروبية (AST)"),
 L(["**Kirby-Bauer Disk Diffusion**", "**Minimum Inhibitory Concentration (MIC)**", "**E-test strips**", "Automated systems (VITEK, Phoenix)"],
   ["**الانتشار بالأقراص (كيربي-باور)**", "**أدنى تركيز مثبّط (`MIC`)**", "**شرائط `E-test`**", "الأنظمة الآلية (`VITEK` و`Phoenix`)"]),
 C("Determine **resistance profiles** for **treatment decisions**.", "تحدّد **أنماط المقاومة** لاتّخاذ **قرارات العلاج**."),
 BN("**MIC** = the **lowest** concentration of an antibiotic that **inhibits visible growth**; Kirby-Bauer reads the **zone of inhibition** around a disk; the E-test strip reads the MIC where the ellipse meets the strip.",
    "**`MIC`** = **أدنى** تركيز من المضادّ الحيوي **يثبّط النموّ المرئي**؛ وكيربي-باور يقرأ **منطقة التثبيط** حول القرص؛ وشريط `E-test` يقرأ `MIC` حيث يلتقي القطع الناقص بالشريط."),
 INSHORT([("Automated ID: **VITEK 2, BD Phoenix, MicroScan WalkAway, MALDI-TOF MS**.", "التشخيص الآلي: **`VITEK 2` و`BD Phoenix` و`MicroScan WalkAway` و`MALDI-TOF MS`**."),
          ("AST: **disk diffusion, MIC, E-test, automated** → resistance profile → treatment.", "فحص الحساسية: **الأقراص، و`MIC`، و`E-test`، والآلي** ← نمط المقاومة ← العلاج.")]),

 # ───────────────────────── 6
 SEC("Advantages and limitations", "المزايا والقيود"),
 HL("This table is highlighted in the original slides.", "هذا الجدول مُظلَّل في الشرائح الأصلية."),
 T([B("Method", "الطريقة"), B("Advantages", "المزايا"), B("Limitations", "القيود")],
   [[B("**Microscopy**", "**الفحص المجهري**"), B("Rapid, simple", "سريع وبسيط"), B("Low specificity", "نوعية منخفضة")],
    [B("**Culture**", "**الزرع**"), B("Reliable", "موثوق"), B("Time-consuming", "يستغرق وقتًا")],
    [B("**Biochemical**", "**الكيميائية الحيوية**"), B("Cost-effective", "اقتصادي (فعّال الكلفة)"), B("May misidentify atypical strains", "قد يخطئ تشخيص السلالات غير النمطية")],
    [B("**Serological**", "**المصلية**"), B("Specific", "نوعي"), B("Requires known antigens", "يحتاج مستضدّات معروفة")],
    [B("**Molecular**", "**الجزيئية**"), B("Fast, accurate", "سريع ودقيق"), B("Expensive, needs expertise", "مكلف ويحتاج خبرة")]],
   key_cols=[0], widths=[26, 34, 40], style="summary", label_en="Method | Advantages | Limitations", label_ar="الطريقة | المزايا | القيود"),
 H2("Conclusion", "الخلاصة"),
 L(["Microbiological identification **integrates classical and molecular methods**.",
    "Combining phenotypic, biochemical, serological, and molecular techniques ensures **accurate and fast diagnostics**.",
    "**Automation and sequencing** are the future of microbial identification."],
   ["يدمج التشخيص الميكروبي **الطرائق التقليدية والجزيئية**.",
    "والجمع بين التقنيات المظهرية والكيميائية الحيوية والمصلية والجزيئية يضمن **تشخيصًا دقيقًا وسريعًا**.",
    "و**الأتمتة والتسلسل (السَّلسَلة الجينية)** هما مستقبل التشخيص الميكروبي."]),
 H2("References", "المصادر"),
 T([B("Reference", "المصدر"), B("In Arabic", "بالعربي")],
   [[B("1. Tille, P. M. (2021). Bailey & Scott’s Diagnostic Microbiology. Elsevier.", "تيل (2021): كتاب بيلي وسكوت للأحياء المجهرية التشخيصية")],
    [B("2. Murray, P. R. et al. (2021). Manual of Clinical Microbiology. ASM Press.", "موراي وآخرون (2021): دليل الأحياء المجهرية السريرية")],
    [B("3. Forbes, B. A., Sahm, D. F. & Weissfeld, A. S. (2020). Bailey & Scott’s Diagnostic Microbiology.", "فوربس وساهم ووايسفيلد (2020): كتاب بيلي وسكوت للأحياء المجهرية التشخيصية")],
    [B("4. Cheesbrough, M. (2019). District Laboratory Practice in Tropical Countries.", "تشيزبرو (2019): الممارسة المختبرية في المناطق الحارّة")]],
   widths=[62, 38]),
 INSHORT([("Fastest + most accurate = **molecular** (but expensive); cheapest = **biochemical**; most reliable = **culture** (but slow).", "الأسرع والأدقّ = **الجزيئية** (لكنها مكلفة)؛ والأرخص = **الكيميائية الحيوية**؛ والأوثق = **الزرع** (لكنه بطيء)."),
          ("Future: **automation and sequencing**.", "المستقبل: **الأتمتة والسَّلسَلة**.")]),
] + TERMS([
 ("Microbiological identification", "التشخيص الميكروبي / تعريف الأحياء المجهرية"),
 ("Etiologic agent", "العامل المسبّب / المُسبِّب المرضي"),
 ("Taxonomy", "علم التصنيف / التصنيف"),
 ("Surveillance / outbreak", "الترصّد / الفاشية (التفشّي)"),
 ("Phenotypic methods", "الطرائق المظهرية / النمطية الظاهرية"),
 ("Aseptic technique", "تقنية معقّمة / عمل لا تلوّثي"),
 ("Selective / differential media", "أوساط انتقائية / تفريقية"),
 ("Acid-fast stain", "الصبغة الصامدة للحامض / صبغة زيل-نيلسن"),
 ("Colony morphology", "شكل المستعمرة / الصفات الشكلية للمستعمرة"),
 ("Microaerophilic", "محبّ للهواء القليل / قليل الهواء"),
 ("Hemolysis", "تحلّل الدم / انحلال الدم"),
 ("Catalase / oxidase / urease", "الكاتاليز / الأوكسيديز / اليوريز"),
 ("Coagulase", "التخثّر / الكواغيوليز (إنزيم التخثير)"),
 ("Agglutination", "التلازن / التراصّ"),
 ("Hybridization / probe", "التهجين / المجسّ"),
 ("Microarray", "المصفوفة الدقيقة"),
 ("Antimicrobial susceptibility testing (AST)", "فحص الحساسية للمضادّات / اختبار الحساسية الدوائية"),
 ("Minimum inhibitory concentration (MIC)", "أدنى تركيز مثبّط"),
 ("Disk diffusion", "الانتشار بالأقراص"),
 ("Atypical strain", "سلالة غير نمطية"),
])

# ───────────────────────── questions (the slides have none — all BIOS, from the slide text)
mcq = [
 {"topic_en": "Introduction and general steps", "topic_ar": "المقدّمة والخطوات العامة"},
 Q("Microbiological identification determines the:", "يحدّد التشخيص الميكروبي:", O(("Type, genus or species of microorganisms", "نوع الأحياء المجهرية أو جنسها أو نوعها"), ("Price of antibiotics", "سعر المضادّات"), ("Blood group", "فصيلة الدم"), ("Patient's age", "عمر المريض")), "a"),
 Q("Microbiological identification combines:", "يجمع التشخيص الميكروبي بين:", O(("Only microscopy and culture", "المجهر والزرع فقط"), ("Classical (phenotypic) and modern (molecular) methods", "الطرائق التقليدية (المظهرية) والحديثة (الجزيئية)"), ("Only serology", "المصلية فقط"), ("Only automation", "الأتمتة فقط")), "b"),
 Q("Which is NOT an objective of microbial identification?", "أيّها ليس من أهداف التشخيص الميكروبي؟", O(("Determine etiologic agents", "تحديد العوامل المسبّبة"), ("Guide therapy and infection control", "توجيه العلاج ومكافحة العدوى"), ("Trace outbreaks", "تتبّع الفاشيات"), ("Determine the patient's blood group", "تحديد فصيلة دم المريض")), "d"),
 Q("The first general step in identification is:", "الخطوة العامة الأولى في التشخيص:", O(("Sample collection", "جمع العيّنة"), ("PCR", "PCR"), ("Serological testing", "الفحص المصلي"), ("Biochemical tests", "الفحوص الكيميائية الحيوية")), "a"),
 Q("Aseptic techniques during sample collection are used to:", "تُستعمل التقنيات المعقّمة أثناء جمع العيّنة لـ:", O(("Stain the bacteria", "تصبيغ البكتيريا"), ("Speed up growth", "تسريع النموّ"), ("Avoid contamination", "تجنّب التلوّث"), ("Detect antibodies", "كشف الأضداد")), "c"),
 Q("Cultivation in identification uses:", "يستعمل الزرع في التشخيص:", O(("DNA probes", "مجسّات DNA"), ("Latex beads", "حبيبات اللاتكس"), ("Antibiotic disks only", "أقراص المضادّات فقط"), ("Selective and differential media", "أوساطًا انتقائية وتفريقية")), "d"),
 {"topic_en": "Microscopy and culture", "topic_ar": "المجهر والزرع"},
 Q("In the Gram stain, Gram-negative bacteria appear:", "في صبغة غرام تظهر البكتيريا السالبة:", O(("Purple", "بنفسجية"), ("Pink", "وردية"), ("Green", "خضراء"), ("Black", "سوداء")), "b"),
 Q("The acid-fast stain detects:", "تكشف الصبغة الصامدة للحامض:", O(("Mycobacterium", "المتفطّرة"), ("Streptococcus", "العقدية"), ("E. coli", "الإشريكية القولونية"), ("Proteus", "المتقلّبة")), "a"),
 Q("Special stains are used for:", "تُستعمل الصبغات الخاصة لـ:", O(("Blood typing", "تحديد فصائل الدم"), ("DNA amplification", "مضاعفة DNA"), ("Endospore, capsule and flagella", "الأبواغ الداخلية والمحفظة والأسواط"), ("Measuring MIC", "قياس MIC")), "c"),
 Q("Hemolysis patterns are read on:", "تُقرأ أنماط تحلّل الدم على:", O(("MacConkey agar", "آغار ماكونكي"), ("Simmons citrate", "سترات سيمونز"), ("TSI agar", "آغار TSI"), ("Blood agar", "آغار الدم")), "d"),
 Q("Which is a cultural characteristic?", "أيّها من الصفات الزرعية؟", O(("Colony size, color, texture and elevation", "حجم المستعمرة ولونها وقوامها وارتفاعها"), ("DNA sequence", "تسلسل DNA"), ("Antibody titer", "عيار الأضداد"), ("Protein band", "شريط بروتيني")), "a"),
 {"topic_en": "Biochemical tests", "topic_ar": "الفحوص الكيميائية الحيوية"},
 Q("The catalase test differentiates:", "يفرّق فحص الكاتاليز بين:", O(("E. coli and Proteus", "الإشريكية والمتقلّبة"), ("Staphylococcus (+) and Streptococcus (–)", "العنقودية (+) والعقدية (–)"), ("Salmonella and Shigella", "السالمونيلا والشيغيلا"), ("Neisseria and Pseudomonas", "النيسرية والزائفة")), "b"),
 Q("Which organisms are oxidase positive in the slides?", "أيّ الكائنات موجبة الأوكسيديز في الشرائح؟", O(("E. coli and Enterobacter", "الإشريكية والأمعائية"), ("S. aureus", "العنقودية الذهبية"), ("Pseudomonas and Neisseria", "الزائفة والنيسرية"), ("Proteus only", "المتقلّبة فقط")), "c"),
 Q("The indole test example in the slides is:", "مثال فحص الإندول في الشرائح:", O(("Proteus", "المتقلّبة"), ("Enterobacter", "الأمعائية"), ("Neisseria", "النيسرية"), ("E. coli (+)", "الإشريكية القولونية (+)")), "d"),
 Q("Urease positive organism in the slides:", "الكائن الموجب لليوريز في الشرائح:", O(("Proteus", "المتقلّبة"), ("Streptococcus", "العقدية"), ("E. coli", "الإشريكية القولونية"), ("Mycobacterium", "المتفطّرة")), "a"),
 Q("Citrate positive example in the slides:", "مثال موجب السترات في الشرائح:", O(("Staphylococcus", "العنقودية"), ("Enterobacter", "الأمعائية"), ("Neisseria", "النيسرية"), ("Streptococcus", "العقدية")), "b"),
 Q("TSI agar detects:", "يكشف آغار TSI:", O(("Catalase enzyme", "إنزيم الكاتاليز"), ("Capsule", "المحفظة"), ("Sugar fermentation and H₂S production", "تخمير السكّر وإنتاج H₂S"), ("DNA sequences", "تسلسلات DNA")), "c"),
 Q("The coagulase test example is:", "مثال فحص التخثّر:", O(("Streptococcus", "العقدية"), ("Proteus", "المتقلّبة"), ("Enterobacter", "الأمعائية"), ("S. aureus (+)", "العنقودية الذهبية (+)")), "d"),
 Q("The oxidase test detects:", "يكشف فحص الأوكسيديز:", O(("Cytochrome oxidase", "السايتوكروم أوكسيديز"), ("Urea hydrolysis", "تحلّل اليوريا"), ("Catalase enzyme", "إنزيم الكاتاليز"), ("Toxins", "السموم")), "a"),
 Q("Biochemical tests determine bacterial:", "تحدّد الفحوص الكيميائية الحيوية لدى البكتيريا:", O(("Size only", "الحجم فقط"), ("Metabolism", "الأيض"), ("DNA sequence", "تسلسل DNA"), ("Antibodies", "الأضداد")), "b"),
 {"topic_en": "Serological, molecular, automated and AST", "topic_ar": "المصلية والجزيئية والآلية وفحص الحساسية"},
 Q("Latex agglutination is used for:", "يُستعمل تلازن اللاتكس لـ:", O(("Salmonella typing", "تنميط السالمونيلا"), ("Detecting toxins", "كشف السموم"), ("Streptococcus grouping", "تصنيف العقدية"), ("DNA amplification", "مضاعفة DNA")), "c"),
 Q("Salmonella and Shigella typing uses:", "يستعمل تنميط السالمونيلا والشيغيلا:", O(("Western blot", "اللطخة الغربية"), ("Microarrays", "المصفوفات الدقيقة"), ("E-test", "E-test"), ("Agglutination tests", "فحوص التلازن")), "d"),
 Q("ELISA detects:", "تكشف الإليزا:", O(("Bacterial toxins/antigens", "السموم/المستضدّات البكتيرية"), ("Colony elevation", "ارتفاع المستعمرة"), ("Hemolysis", "تحلّل الدم"), ("Flagella", "الأسواط")), "a"),
 Q("Western blot:", "اللطخة الغربية:", O(("Amplifies DNA", "تضاعف DNA"), ("Confirms microbial proteins", "تؤكّد البروتينات الميكروبية"), ("Measures MIC", "تقيس MIC"), ("Stains capsules", "تصبغ المحافظ")), "b"),
 Q("PCR:", "تفاعل PCR:", O(("Uses latex beads", "يستعمل حبيبات اللاتكس"), ("Detects catalase", "يكشف الكاتاليز"), ("Amplifies specific DNA sequences", "يضاعف تسلسلات DNA محدّدة"), ("Reads hemolysis", "يقرأ تحلّل الدم")), "c"),
 Q("Microarrays can:", "تستطيع المصفوفات الدقيقة:", O(("Identify only one pathogen", "تشخيص مُمْرِض واحد فقط"), ("Replace sample collection", "الاستغناء عن جمع العيّنة"), ("Stain bacteria", "تصبيغ البكتيريا"), ("Identify multiple pathogens simultaneously", "تشخيص مُمْرِضات متعدّدة في آنٍ واحد")), "d"),
 Q("Which is NOT an automated identification system in the slides?", "أيّها ليس من أنظمة التشخيص الآلية في الشرائح؟", O(("Gram stain", "صبغة غرام"), ("VITEK 2", "VITEK 2"), ("BD Phoenix", "BD Phoenix"), ("MALDI-TOF MS", "MALDI-TOF MS")), "a"),
 Q("Kirby-Bauer is a method of:", "كيربي-باور طريقة لـ:", O(("Molecular identification", "التشخيص الجزيئي"), ("Antimicrobial susceptibility testing (disk diffusion)", "فحص الحساسية للمضادّات (الانتشار بالأقراص)"), ("Serological typing", "التنميط المصلي"), ("Staining", "التصبيغ")), "b"),
 Q("The main limitation of molecular methods is that they are:", "القيد الرئيس للطرائق الجزيئية أنها:", O(("Slow", "بطيئة"), ("Low specificity", "منخفضة النوعية"), ("Expensive and need expertise", "مكلفة وتحتاج خبرة"), ("Need known antigens", "تحتاج مستضدّات معروفة")), "c"),
 Q("Which method is cost-effective but may misidentify atypical strains?", "أيّ طريقة اقتصادية لكنها قد تخطئ في السلالات غير النمطية؟", O(("Molecular", "الجزيئية"), ("Serological", "المصلية"), ("Microscopy", "المجهرية"), ("Biochemical", "الكيميائية الحيوية")), "d"),
 Q("Serological methods require:", "تحتاج الطرائق المصلية إلى:", O(("Known antigens", "مستضدّات معروفة"), ("Sequencing", "سَلسَلة"), ("Blood agar", "آغار الدم"), ("Kovac's reagent", "كاشف كوفاكس")), "a"),
]
mcq = balance(mcq, 74)

tf = [
 TF("Microbiological identification is essential for antimicrobial selection.", "التشخيص الميكروبي أساسي لاختيار المضادّ الميكروبي.", "T"),
 TF("Serological testing in identification is based on DNA/RNA.", "يعتمد الفحص المصلي في التشخيص على DNA/RNA.", "F"),
 TF("Gram-positive bacteria appear purple.", "تظهر البكتيريا الموجبة لغرام بنفسجية.", "T"),
 TF("The acid-fast stain is used to detect Mycobacterium.", "تُستعمل الصبغة الصامدة للحامض لكشف المتفطّرة.", "T"),
 TF("Streptococcus is catalase positive.", "العقدية موجبة الكاتاليز.", "F"),
 TF("Neisseria is oxidase positive.", "النيسرية موجبة الأوكسيديز.", "T"),
 TF("Proteus is urease positive.", "المتقلّبة موجبة اليوريز.", "T"),
 TF("Coagulase is used to identify S. aureus.", "يُستعمل التخثّر لتشخيص العنقودية الذهبية.", "T"),
 TF("ELISA confirms microbial proteins by blotting.", "تؤكّد الإليزا البروتينات الميكروبية بالتلطيخ.", "F"),
 TF("Microarrays identify multiple pathogens simultaneously.", "تشخّص المصفوفات الدقيقة مُمْرِضات متعدّدة في آنٍ واحد.", "T"),
 TF("MALDI-TOF MS is an automated identification system.", "MALDI-TOF MS نظام تشخيص آلي.", "T"),
 TF("E-test strips are used for antimicrobial susceptibility testing.", "تُستعمل شرائط E-test لفحص الحساسية للمضادّات.", "T"),
 TF("Culture is rapid but has low specificity.", "الزرع سريع لكنه منخفض النوعية.", "F"),
 TF("Automation and sequencing are described as the future of microbial identification.", "تُوصف الأتمتة والسَّلسَلة بأنهما مستقبل التشخيص الميكروبي.", "T"),
]

traps = [
 TR("Catalase vs coagulase", "الكاتاليز مقابل التخثّر", "Catalase separates Staphylococcus (+) from Streptococcus (–). Coagulase then identifies S. aureus (+) among staphylococci.", "الكاتاليز يفصل العنقودية (+) عن العقدية (–). ثم التخثّر يشخّص العنقودية الذهبية (+) بين العنقوديات."),
 TR("Which organism goes with which test", "أيّ كائن مع أيّ فحص", "Oxidase: Pseudomonas, Neisseria · Indole: E. coli · Urease: Proteus · Citrate: Enterobacter · Coagulase: S. aureus.", "الأوكسيديز: الزائفة والنيسرية · الإندول: الإشريكية القولونية · اليوريز: المتقلّبة · السترات: الأمعائية · التخثّر: العنقودية الذهبية."),
 TR("Gram colours", "ألوان غرام", "Positive = PURPLE, negative = PINK — do not swap them.", "الموجبة = بنفسجية، والسالبة = وردية — لا تقلبها."),
 TR("Agglutination vs latex agglutination", "التلازن مقابل تلازن اللاتكس", "Agglutination tests → Salmonella, Shigella typing. Latex agglutination → Streptococcus grouping.", "فحوص التلازن ← تنميط السالمونيلا والشيغيلا. تلازن اللاتكس ← تصنيف العقدية إلى مجاميع."),
 TR("ELISA vs Western blot", "الإليزا مقابل اللطخة الغربية", "ELISA detects toxins/antigens; Western blot CONFIRMS microbial proteins.", "الإليزا تكشف السموم/المستضدّات؛ واللطخة الغربية تؤكّد البروتينات الميكروبية."),
 TR("Advantages table", "جدول المزايا", "Culture = reliable but time-consuming; microscopy = rapid but low specificity; molecular = fast and accurate but expensive.", "الزرع = موثوق لكن بطيء؛ والمجهر = سريع لكن منخفض النوعية؛ والجزيئي = سريع ودقيق لكن مكلف."),
 TR("Automated systems do two jobs", "الأنظمة الآلية تعمل عملين", "VITEK and Phoenix appear under identification AND under AST — they combine identification with susceptibility testing.", "VITEK وPhoenix مذكوران تحت التشخيص وتحت فحص الحساسية — فهما يجمعان التشخيص مع فحص الحساسية."),
]

important = [
 IM("Define microbiological identification and give its importance.", "عرّف التشخيص الميكروبي واذكر أهميته.",
    "It determines the type, genus or species of microorganisms. It is essential for disease diagnosis, antimicrobial selection, food safety and microbial research, and combines classical (phenotypic) and modern (molecular) methods.",
    "يحدّد نوع الأحياء المجهرية أو جنسها أو نوعها. وهو أساسي لتشخيص المرض، واختيار المضادّ، وسلامة الغذاء، والبحث الميكروبي، ويجمع بين الطرائق التقليدية (المظهرية) والحديثة (الجزيئية)."),
 IM("List the objectives of microbial identification.", "عدّد أهداف التشخيص الميكروبي.",
    "1. Determine etiologic agents of infection 2. Understand microbial diversity and taxonomy 3. Guide therapy and infection control 4. Trace outbreaks and perform surveillance.",
    "1. تحديد العوامل المسبّبة للعدوى 2. فهم التنوّع والتصنيف الميكروبي 3. توجيه العلاج ومكافحة العدوى 4. تتبّع الفاشيات وإجراء الترصّد."),
 IM("List the general steps in identification.", "عدّد الخطوات العامة في التشخيص.",
    "1. Sample collection (aseptic) 2. Microscopic examination (morphology, staining) 3. Cultivation (selective and differential media) 4. Biochemical characterization (metabolic profiling) 5. Serological testing (antigen/antibody) 6. Molecular identification (DNA/RNA).",
    "1. جمع العيّنة (معقّم) 2. الفحص المجهري (الشكل والتصبيغ) 3. الزرع (أوساط انتقائية وتفريقية) 4. التوصيف الكيميائي الحيوي (التنميط الأيضي) 5. الفحص المصلي (مستضدّ/ضدّ) 6. التشخيص الجزيئي (DNA/RNA)."),
 IM("Name the biochemical tests in the lab with an example of each.", "اذكر الفحوص الكيميائية الحيوية في العملي مع مثال لكل منها.",
    "Catalase: Staphylococcus (+) vs Streptococcus (–); Oxidase: Pseudomonas (+), Neisseria (+); Indole: E. coli (+); Urease: Proteus (+); Citrate: Enterobacter (+); TSI agar: sugar fermentation and H₂S production; Coagulase: S. aureus (+).",
    "الكاتاليز: العنقودية (+) مقابل العقدية (–)؛ الأوكسيديز: الزائفة (+) والنيسرية (+)؛ الإندول: الإشريكية القولونية (+)؛ اليوريز: المتقلّبة (+)؛ السترات: الأمعائية (+)؛ آغار TSI: تخمير السكّر وإنتاج H₂S؛ التخثّر: العنقودية الذهبية (+)."),
 IM("What are the cultural characteristics used in identification?", "ما الصفات الزرعية المستعملة في التشخيص؟",
    "Colony morphology (size, color, texture, elevation); growth conditions (aerobic, anaerobic, microaerophilic); hemolysis patterns on blood agar (α, β, γ); pigment and odor production.",
    "شكل المستعمرة (الحجم واللون والقوام والارتفاع)؛ وظروف النموّ (هوائي، لاهوائي، محبّ للهواء القليل)؛ وأنماط تحلّل الدم على آغار الدم (α وβ وγ)؛ وإنتاج الصبغة والرائحة."),
 IM("Compare serological and molecular identification methods.", "قارن بين طرائق التشخيص المصلية والجزيئية.",
    "Serological: agglutination (Salmonella, Shigella typing), latex agglutination (Streptococcus grouping), ELISA (toxins/antigens), Western blot (proteins) — rapid, specific, sensitive but need known antigens. Molecular: PCR (amplifies DNA), DNA hybridization (probes), microarrays (multiple pathogens) — fast, accurate but expensive and need expertise.",
    "المصلية: التلازن (تنميط السالمونيلا والشيغيلا)، وتلازن اللاتكس (تصنيف العقدية)، والإليزا (السموم/المستضدّات)، واللطخة الغربية (البروتينات) — سريعة ونوعية وحسّاسة لكنها تحتاج مستضدّات معروفة. الجزيئية: PCR (يضاعف DNA)، والتهجين (مجسّات)، والمصفوفات (مُمْرِضات متعدّدة) — سريعة ودقيقة لكنها مكلفة وتحتاج خبرة."),
 IM("Name the automated identification systems and the AST methods.", "اذكر أنظمة التشخيص الآلية وطرائق فحص الحساسية.",
    "Automated: VITEK 2, BD Phoenix, MicroScan WalkAway, MALDI-TOF MS (accuracy, speed, AST). AST: Kirby-Bauer disk diffusion, minimum inhibitory concentration (MIC), E-test strips, automated systems (VITEK, Phoenix) — they determine resistance profiles for treatment decisions.",
    "الآلية: VITEK 2 وBD Phoenix وMicroScan WalkAway وMALDI-TOF MS (دقّة وسرعة وفحص حساسية). فحص الحساسية: الانتشار بالأقراص (كيربي-باور)، وأدنى تركيز مثبّط (MIC)، وشرائط E-test، والأنظمة الآلية (VITEK وPhoenix) — وتحدّد أنماط المقاومة لقرارات العلاج."),
 IM("Give the advantages and limitations of each identification method.", "اذكر مزايا كل طريقة تشخيص وقيودها.",
    "Microscopy: rapid, simple / low specificity. Culture: reliable / time-consuming. Biochemical: cost-effective / may misidentify atypical strains. Serological: specific / requires known antigens. Molecular: fast, accurate / expensive, needs expertise.",
    "المجهر: سريع وبسيط / نوعية منخفضة. الزرع: موثوق / يستغرق وقتًا. الكيميائية الحيوية: اقتصادية / قد تخطئ في السلالات غير النمطية. المصلية: نوعية / تحتاج مستضدّات معروفة. الجزيئية: سريعة ودقيقة / مكلفة وتحتاج خبرة."),
]

meta = {"subject_en": "Diagnostic Microbiology", "subject_ar": "الأحياء المجهرية التشخيصية", "short_ar": "بكتريا", "instructor": "د. هبة سامي",
        "unit_en": "Lab 4", "unit_ar": "العملي 4", "unit_label": "LAB", "unit_no": "4",
        "title_en": "Microbiological Methods for Identification", "title_ar": "الطرائق الميكروبية للتشخيص",
        "department": "قسم التحليلات", "kind": "Laboratories — عملي", "stage": "The fourth stage — الرابعة"}
blocks, mcq, tf, traps, important = ltr_all(blocks), ltr_all(mcq), ltr_all(tf), ltr_all(traps), ltr_all(important)
save("bacteriology-lab4-identification", meta, blocks, mcq, tf, traps, important)
fit("bacteriology-lab4-identification", min_gap=0.08)   # no big gaps, small ones too

```
