---
source: BIOS-Obsidian/tools/scripts/iml4/l4.py
handouts: [immunology-lab4-immunization-heart-puncture]
saved: 2026-11-08
tags: [bios, code]
---
# iml4/l4.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#immunology-lab4-immunization-heart-puncture|immunology-lab4-immunization-heart-puncture]]

```python
import sys; sys.path.insert(0, "/tmp/claude-0/-home-user/ebd718de-5339-5b98-9782-8a5888247f2a/scratchpad/imm456")
from ci import *            # c helpers + B INSHORT TERMS balance save(split.fix)
sys.path.insert(0, "/tmp/claude-0/-home-user/ebd718de-5339-5b98-9782-8a5888247f2a/scratchpad"); from bidi import ltr_all; from flowfit import fit

# Practical Immunology, lab 4 — Immunization of laboratory animals, heart puncture. Source: Lab4.pdf (Word, 4 pages;
# header "Medical Lab. Techniques · Practical Immunology \3rd stage · Assistant Lecturer \ Jinan Khaleel · Lab. No.(4)").
# 7 pictures (the college logo and header bars left out). Third stage → blush, questions merged. No questions in the file.
BN = lambda en, ar: N(en, ar, label=["BIOS note", "ملاحظة BIOS"])
O = P
FOLDER = "immunology-lab4-immunization-heart-puncture"
import split; split.ABBR += ("Lab.",)   # "Medical Lab. Techniques", "Lab. No.(4)" are not sentence ends

blocks = [
 # ───────────────────────── 1 animal inoculation
 SEC("Animal inoculation", "تلقيح الحيوانات"),
 N("Medical Lab. Techniques · Practical Immunology \\3rd stage · Assistant Lecturer \\ Jinan Khaleel · Lab. No.(4)",
   "تقنيات المختبرات الطبية · علم المناعة العملي \\ المرحلة الثالثة · المدرّس المساعد \\ جنان خليل · العملي رقم (4)", label=["Lab sheet", "ورقة العملي"]),
 H2("**Immunization of laboratory, Animal heart puncture**", "**تمنيع حيوانات المختبر، وبزل قلب الحيوان**"),
 C(["**Animal inoculation** : Selection of an animal model is one of the most important step in any of the experimental studies.",
    "Animal model preferred for the study must be producing similar disease profile as in the human."],
   ["**تلقيح الحيوانات (`Animal inoculation`):** اختيار النموذج الحيواني من أهمّ الخطوات في أيّ دراسة تجريبية.",
    "والنموذج الحيواني المفضّل للدراسة يجب أن ينتج صورة مرضية مشابهة لما في الإنسان."]),
 L(["Use of an animal phylogenetically closer to man.",
    "Use of an animal in which the process under investigation is as close as possible to that in man.",
    "The Anatomy, Physiology and Biochemistry are considered to be similar."],
   ["استعمال حيوان أقرب إلى الإنسان من ناحية النشوء والتطوّر.",
    "استعمال حيوان تكون فيه العملية قيد الدراسة أقرب ما يمكن إلى ما في الإنسان.",
    "أن يكون التشريح ووظائف الأعضاء والكيمياء الحيوية متشابهة."],
   en="**Animal model selected should follow three main objectives:**", ar="**النموذج الحيواني المختار يجب أن يحقّق ثلاثة أهداف رئيسية:**"),
 L(["**Rodents** (Mice, Rats, Guinea pigs, Hamster… etc.).", "**Non-rodents** (Rabbit, Dog, Cat, Monkey…. etc.)."],
   ["**القوارض** (الفئران، الجرذان، خنازير غينيا، الهامستر… إلخ).", "**غير القوارض** (الأرنب، الكلب، القطّ، القرد…. إلخ)."],
   en="**Classification of experimental animals:**", ar="**تصنيف حيوانات التجارب:**", start=1),
 BN("The rabbit is NOT a rodent (it is a lagomorph) — that is why the sheet lists it with the non-rodents.",
    "الأرنب ليس من القوارض (هو من الأرنبيات) — ولذلك وضعته الورقة مع غير القوارض."),
 INSHORT([("Animal model = gives a disease profile **similar to man**.", "النموذج الحيواني = يعطي صورة مرضية **مشابهة للإنسان**."),
          ("3 objectives: **phylogenetically close**, **similar process**, **similar anatomy/physiology/biochemistry**.", "3 أهداف: **قريب تطوّريًا**، **عملية مشابهة**، **تشريح/وظائف/كيمياء حيوية متشابهة**."),
          ("Rodents: mice, rats, guinea pigs, hamster; non-rodents: **rabbit**, dog, cat, monkey.", "القوارض: الفئران، الجرذان، خنازير غينيا، الهامستر؛ وغير القوارض: **الأرنب**، الكلب، القطّ، القرد.")]),

 # ───────────────────────── 2 handling
 SEC("Animal handling", "التعامل مع الحيوان"),
 C("Before restrain, first pet or sooth the animal by slow deliberate movements in the body, overcrowding near the animal cage should be, noise should be kept as minimum, don’t hold animal too hard, never agitate the animal, it may become violent for self-protection.",
   "قبل تقييد الحيوان، داعبه أو هدّئه أولًا بحركات بطيئة متأنّية على جسمه، ويجب [تجنّب] الازدحام قرب قفص الحيوان، وإبقاء الضوضاء في حدّها الأدنى، ولا تمسك الحيوان بقوّة شديدة، ولا تهيّجه أبدًا، فقد يصبح عنيفًا دفاعًا عن نفسه."),
 BN("\"overcrowding near the animal cage should be,\" — a word is missing: overcrowding should be **avoided**.",
    "\"overcrowding near the animal cage should be,\" — توجد كلمة ناقصة: يجب **تجنّب (`avoided`)** الازدحام."),
 INSHORT([("Calm the animal first (slow movements), **no crowding, little noise**, don't hold too hard, **never agitate** it.", "هدّئ الحيوان أولًا (حركات بطيئة)، **بلا ازدحام وبضوضاء قليلة**، لا تمسكه بقوّة، و**لا تهيّجه أبدًا**.")]),

 # ───────────────────────── 3 IV
 SEC("Route of injection: intravenous", "طرق الحقن: الحقن الوريدي"),
 C("**1- Intravenous:** This procedure involves direct injection into blood stream of the animal.", "**1- الحقن الوريدي (`Intravenous`):** يتضمّن هذا الإجراء الحقن مباشرةً في مجرى دم الحيوان."),
 C("The ear vein is the most accessible and visible vein in the rabbit. Take the rabbit then:", "وريد الأذن هو أسهل الأوردة وصولًا وأوضحها في الأرنب. خذ الأرنب ثم:"),
 L(["See the vein on the dorsal edge of either ear.", "Shave the hair away from the area.", "Clean the area with disinfectant (70% ethanol).",
    "For the ease injection, the diameter of the vein may be enlarged before injection by heating and by applying pressure over the vein at the base of ear.",
    "Hold the ear with one hand while supporting the ear from below with finger of the same hand.",
    ["With vein clearly visible, insert the needle in the direction of the blood flow (toward the head of the rabbit).",
     "Slowly inject the inoculums (Ag) while watching for signs for dilution of the blood in the vein indicating that the injected material is passing into the vein.",
     "The blunder of the syringe should move down easily and no raised area in the surrounding tissue should be visible."],
    "When injection is complete with draw the needle and made pressure by finger to the injection site to stop bleeding and disinfectant with ethanol 70% the area by place a piece of cotton on site of injection."],
   ["حدّد الوريد على الحافّة الظهرية لأيّ من الأذنين.", "احلق الشعر عن المنطقة.", "نظّف المنطقة بمطهّر (إيثانول 70%).",
    "لتسهيل الحقن، يمكن توسيع قطر الوريد قبل الحقن بالتدفئة وبالضغط على الوريد عند قاعدة الأذن.",
    "أمسك الأذن بيد واحدة مع إسنادها من الأسفل بإصبع من اليد نفسها.",
    ["والوريد ظاهر بوضوح، أدخل الإبرة باتّجاه جريان الدم (نحو رأس الأرنب).",
     "واحقن اللقاح (المستضد `Ag`) ببطء مع مراقبة علامات تخفّف الدم في الوريد، التي تدلّ على أن المادة المحقونة تمرّ إلى الوريد.",
     "ويجب أن يتحرّك مكبس المحقنة إلى الأسفل بسهولة، وألّا تظهر منطقة منتفخة في النسيج المحيط."],
    "عند انتهاء الحقن اسحب الإبرة واضغط بالإصبع على موضع الحقن لإيقاف النزف، وطهّر المنطقة بإيثانول 70% بوضع قطعة قطن على موضع الحقن."]),
 FF(("ear-marginal-vein.png", "Rabbit ear: Marginal vein and Auricular artery", "أذن الأرنب: الوريد الحافّي والشريان الأذيني", "46mm"),
    ("iv-ear-injection.png", "Intravenous injection into the ear vein", "الحقن الوريدي في وريد الأذن", "46mm")),
 BN(["\"blunder of the syringe\" = the **plunger**; \"with draw\" = **withdraw**; \"made pressure\" = **make** pressure.",
     "In the picture the **marginal vein** runs along the edge of the ear and the **auricular artery** runs in the middle — inject into the vein, not the artery."],
    ["\"blunder of the syringe\" = **المكبس (`plunger`)**؛ و\"with draw\" = **اسحب (`withdraw`)**؛ و\"made pressure\" = **اضغط (`make pressure`)**.",
     "في الصورة **الوريد الحافّي** يمتدّ على حافّة الأذن، و**الشريان الأذيني** في الوسط — الحقن يكون في الوريد لا الشريان."]),
 INSHORT([("IV = **directly into the blood stream**; in the rabbit: the **ear vein** (dorsal edge).", "الوريدي = **مباشرةً في مجرى الدم**؛ وفي الأرنب: **وريد الأذن** (الحافّة الظهرية)."),
          ("Shave → 70% ethanol → enlarge the vein (heat, pressure) → needle **toward the head** → inject slowly.", "احلق ← إيثانول 70% ← وسّع الوريد (تدفئة، ضغط) ← الإبرة **نحو الرأس** ← احقن ببطء."),
          ("Correct injection: blood **dilutes**, plunger moves **easily**, **no raised area**.", "الحقن الصحيح: الدم **يتخفّف**، والمكبس يتحرّك **بسهولة**، و**لا انتفاخ**.")]),

 # ───────────────────────── 4 IP
 SEC("Intraperitoneal injection", "الحقن داخل الصفاق"),
 C(["**2- Intraperitoneal (Mouse):** The injection of material into the peritoneal of abdominal cavity of the animal.", "The animal (Rabbit or mouse) should be place on its back ."],
   ["**2- الحقن داخل الصفاق (`Intraperitoneal`) (الفأر):** حقن المادة في الصفاق (البريتون) للتجويف البطني للحيوان.", "ويجب وضع الحيوان (الأرنب أو الفأر) على ظهره."]),
 L(["Anesthesia may be used for this injection .", "Clip the hair away from the injection site and disinfect the site with 70% ethanol.",
    "Grasp the skin and peritoneum with finger.", ["Insert the needle through the skin and peritoneum.", "The needle should be empty from the bubbles."],
    "Inject inoculums (Ag) carefully so as to prevent injection into the animal organs with practice, the procedure is relatively easy.",
    "Remove the needle with disinfect the area once again with alcohol."],
   ["قد يُستعمل التخدير في هذا الحقن.", "قصّ الشعر عن موضع الحقن وطهّره بإيثانول 70%.",
    "أمسك الجلد والصفاق بالإصبع.", ["أدخل الإبرة عبر الجلد والصفاق.", "ويجب أن تكون الإبرة خالية من الفقاعات."],
    "احقن اللقاح (المستضد `Ag`) بحذر لتجنّب الحقن في أعضاء الحيوان؛ ومع التمرين يصبح الإجراء سهلًا نسبيًا.",
    "أخرج الإبرة وطهّر المنطقة مرّة أخرى بالكحول."]),
 FF(("ip-injection-1.png", "Intraperitoneal injection in a mouse", "الحقن داخل الصفاق في فأر", "40mm"),
    ("ip-injection-2.png", "Holding the mouse on its back for intraperitoneal injection", "إمساك الفأر على ظهره للحقن داخل الصفاق", "40mm")),
 INSHORT([("IP = into the **peritoneal (abdominal) cavity**; animal **on its back**; anesthesia may be used.", "داخل الصفاق = في **التجويف البطني (الصفاقي)**؛ الحيوان **على ظهره**؛ وقد يُستعمل التخدير."),
          ("Needle **without bubbles**; inject carefully to **avoid the organs**.", "إبرة **بلا فقاعات**؛ واحقن بحذر **لتجنّب الأعضاء**.")]),

 # ───────────────────────── 5 SC
 SEC("Subcutaneous injection", "الحقن تحت الجلد"),
 C(["**3- Subcutaneous:** This method involves the injection of material under the skin.", "Choose a site (usually the back)."],
   ["**3- الحقن تحت الجلد (`Subcutaneous`):** تتضمّن هذه الطريقة حقن المادة تحت الجلد.", "اختر موضعًا (عادةً الظهر)."]),
 L(["Cline and shave the hair and disinfect the injection site with 70% ethanol.",
    "Load tuberculin syringe and insert the needle almost horizontal to the animal to a depth.",
    "Slowly inject the inoculums and observed the formation of a slightly raised area under the skin.",
    "Remove needle and disinfect the injection site once again with alcohol."],
   ["نظّف واحلق الشعر وطهّر موضع الحقن بإيثانول 70%.",
    "املأ محقنة التوبركلين وأدخل الإبرة بوضع شبه أفقي على الحيوان إلى عمق [مناسب].",
    "احقن اللقاح ببطء ولاحظ تكوّن منطقة مرتفعة قليلًا تحت الجلد.",
    "أخرج الإبرة وطهّر موضع الحقن مرّة أخرى بالكحول."]),
 FF(("sc-injection-1.png", "Subcutaneous injection in the back of a rabbit", "الحقن تحت الجلد في ظهر الأرنب", "40mm"),
    ("sc-injection-2.png", "Subcutaneous injection — skin lifted, needle almost horizontal", "الحقن تحت الجلد — الجلد مرفوع والإبرة شبه أفقية", "40mm")),
 BN("\"Cline\" = **clean**. Note the difference: in IV injection **no raised area** should appear, while in SC injection a **slightly raised area** is the sign of a correct injection.",
    "\"Cline\" = **نظّف (`clean`)**. ولاحظ الفرق: في الحقن الوريدي **لا يجب** أن تظهر منطقة منتفخة، بينما في الحقن تحت الجلد **المنطقة المرتفعة قليلًا** هي علامة الحقن الصحيح."),
 T([B("Route", "الطريق"), B("Where", "أين"), B("Animal / site", "الحيوان / الموضع"), B("Sign of correct injection", "علامة الحقن الصحيح")],
   [[B("**Intravenous**", "**وريدي**"), B("blood stream", "مجرى الدم"), B("rabbit — ear vein", "الأرنب — وريد الأذن"), B("blood dilutes, no raised area", "يتخفّف الدم، بلا انتفاخ")],
    [B("**Intraperitoneal**", "**داخل الصفاق**"), B("peritoneal cavity", "التجويف الصفاقي"), B("mouse/rabbit — on its back", "الفأر/الأرنب — على ظهره"), B("no bubbles, organs avoided", "بلا فقاعات، تجنّب الأعضاء")],
    [B("**Subcutaneous**", "**تحت الجلد**"), B("under the skin", "تحت الجلد"), B("usually the back", "عادةً الظهر"), B("slightly raised area", "منطقة مرتفعة قليلًا")]],
   key_cols=[0], widths=[22, 22, 26, 30], style="summary", label_en="BIOS: the three routes", label_ar="BIOS: طرق الحقن الثلاث"),
 INSHORT([("SC = **under the skin**, usually **the back**; **tuberculin syringe**, needle almost **horizontal**.", "تحت الجلد = **تحت الجلد**، عادةً **الظهر**؛ **محقنة التوبركلين**، والإبرة **شبه أفقية**."),
          ("Sign: a **slightly raised area** under the skin.", "العلامة: **منطقة مرتفعة قليلًا** تحت الجلد.")]),

 # ───────────────────────── 6 blood harvesting
 SEC("Blood harvesting", "جمع الدم"),
 C(["The blood should collected to detect antibody formation against the antigen had been injected (R.B.Cs and Serum of human and rabbit).",
    "There are two main sites to collect blood in rabbit, they are auricular artery (marginal ear vein) and cardiac puncture (heart puncture)."],
   ["يجب جمع الدم للكشف عن تكوّن الأضداد ضدّ المستضد الذي حُقن (كريات الدم الحمر ومصل الإنسان والأرنب).",
    "وهناك موضعان رئيسيان لجمع الدم في الأرنب، هما: الشريان الأذيني (وريد الأذن الحافّي) وبزل القلب."]),
 BN("The **auricular artery** and the **marginal ear vein** are two different vessels (see the ear picture); both can be used to bleed a rabbit.",
    "**الشريان الأذيني** و**وريد الأذن الحافّي** وعاءان مختلفان (انظر صورة الأذن)؛ ويمكن سحب دم الأرنب من كليهما."),
 H2("**Heart puncture (Cardiac puncture)**", "**بزل القلب (`Cardiac puncture`)**"),
 C(["Cardiac puncture is a suitable technique to obtain a single, large, good quality sample from a euthanized animal or a animal under deep terminal anesthesia if coagulation parameters, a separate arterial or venous sample or cardiac histology are not required.",
    "It is appropriate for all strains of rat."],
   ["بزل القلب تقنية مناسبة للحصول على عيّنة واحدة كبيرة وجيّدة النوعية من حيوان قُتل رحيمًا أو حيوان تحت تخدير عميق نهائي، إذا لم تكن مطلوبة معاملات التخثّر أو عيّنة شريانية أو وريدية منفصلة أو نسيج القلب.",
    "وهي مناسبة لكل سلالات الجرذان."]),
 C(["A sample of blood (10 - 15 ml from rat, or 20-60 ml from rabbit) can be obtained depending on the size of the animal and whether the heart is beating.",
    "Blood samples are taken from the heart, preferably the ventricle, which can be accessed either via the left side of the chest, through the diaphragm, or from the top of the sternum.",
    "Blood should be withdrawn slowly to prevent the heart collapsing."],
   ["يمكن الحصول على عيّنة دم (10 - 15 مل من الجرذ، أو 20-60 مل من الأرنب) حسب حجم الحيوان وما إذا كان القلب ينبض.",
    "وتُؤخذ عيّنات الدم من القلب، ويُفضّل البطين، الذي يمكن الوصول إليه إمّا عن طريق الجانب الأيسر من الصدر، أو عبر الحجاب الحاجز، أو من أعلى عظم القصّ.",
    "ويجب سحب الدم ببطء لمنع انخماص القلب."]),
 F("heart-puncture-steps.png", "Heart puncture in a rat — steps 1 to 5", "بزل القلب في جرذ — الخطوات 1 إلى 5", h="70mm"),
 T([B("", ""), B("Rat", "الجرذ"), B("Rabbit", "الأرنب")],
   [[B("**Blood volume** (preferably from the ventricle)", "**حجم الدم** (ويُفضّل من البطين)"), B("10 - 15 ml", "10 - 15 مل"), B("20-60 ml", "20-60 مل")]],
   key_cols=[0], widths=[30, 35, 35], style="summary", label_en="BIOS: cardiac puncture numbers", label_ar="BIOS: أرقام بزل القلب"),
 BN("The 5 pictures have no captions in the sheet; they show the rat on its back and the needle entering the chest towards the heart.",
    "الصور الخمس بلا عناوين في الورقة؛ وتُظهر الجرذ على ظهره والإبرة تدخل الصدر باتّجاه القلب."),
 INSHORT([("Blood is collected to detect **antibody formation** against the injected antigen.", "يُجمع الدم للكشف عن **تكوّن الأضداد** ضدّ المستضد المحقون."),
          ("Rabbit bleeding sites: **ear (auricular artery / marginal vein)** and **cardiac puncture**.", "مواضع سحب دم الأرنب: **الأذن (الشريان الأذيني / الوريد الحافّي)** و**بزل القلب**."),
          ("Cardiac puncture: **single, large sample**, euthanized/deeply anesthetized animal; rat **10–15 ml**, rabbit **20–60 ml**; withdraw **slowly**.", "بزل القلب: **عيّنة واحدة كبيرة**، حيوان مقتول رحيمًا/تحت تخدير عميق؛ الجرذ **10–15 مل**، الأرنب **20–60 مل**؛ اسحب **ببطء**.")]),
] + TERMS([
 ("Immunization", "التمنيع / التحصين"),
 ("Animal inoculation", "تلقيح الحيوان / حقن الحيوان"),
 ("Animal model", "النموذج الحيواني"),
 ("Rodents", "القوارض"),
 ("Inoculum", "اللقاح / المادة المحقونة"),
 ("Intravenous (IV)", "وريدي / في الوريد"),
 ("Intraperitoneal (IP)", "داخل الصفاق / داخل البريتون"),
 ("Subcutaneous (SC)", "تحت الجلد"),
 ("Marginal ear vein", "وريد الأذن الحافّي"),
 ("Auricular artery", "الشريان الأذيني"),
 ("Tuberculin syringe", "محقنة التوبركلين / محقنة 1 مل"),
 ("Plunger", "مكبس المحقنة"),
 ("Anesthesia", "التخدير"),
 ("Cardiac (heart) puncture", "بزل القلب / ثقب القلب"),
 ("Euthanized", "مقتول رحيمًا"),
 ("Ventricle", "البطين"),
])

# ───────────────────────── questions (BIOS — the file has none)
mcq = [
 {"topic_en": "Animal models and handling", "topic_ar": "النماذج الحيوانية والتعامل"},
 Q("The animal model preferred for a study must:", "النموذج الحيواني المفضّل للدراسة يجب أن:", O(("Produce a disease profile similar to that in man", "ينتج صورة مرضية مشابهة للإنسان"), ("Be the cheapest animal", "يكون أرخص حيوان"), ("Be the largest animal", "يكون أكبر حيوان"), ("Never get the disease", "لا يصاب بالمرض أبدًا")), "a"),
 Q("Which is one of the three main objectives of animal model selection?", "أيّ مما يلي من الأهداف الثلاثة لاختيار النموذج الحيواني؟", O(("Use of a wild animal", "استعمال حيوان برّي"), ("Use of an animal phylogenetically closer to man", "استعمال حيوان أقرب تطوّريًا إلى الإنسان"), ("Use of a very young animal only", "استعمال حيوان صغير جدًا فقط"), ("Use of an animal with no immune system", "استعمال حيوان بلا جهاز مناعي")), "b"),
 Q("Which of the following is a rodent?", "أيّ مما يلي من القوارض؟", O(("Rabbit", "الأرنب"), ("Dog", "الكلب"), ("Guinea pig", "خنزير غينيا"), ("Monkey", "القرد")), "c"),
 Q("In the sheet, the rabbit is classified as a:", "في الورقة، صُنّف الأرنب ضمن:", O(("Rodent", "القوارض"), ("Primate", "الرئيسيات"), ("Bird", "الطيور"), ("Non-rodent", "غير القوارض")), "d"),
 Q("When handling an animal you should:", "عند التعامل مع الحيوان يجب:", O(("Calm it with slow deliberate movements and keep noise minimum", "تهدئته بحركات بطيئة متأنّية وإبقاء الضوضاء بالحدّ الأدنى"), ("Hold it as hard as possible", "إمساكه بأقصى قوّة"), ("Agitate it to keep it awake", "تهييجه ليبقى يقظًا"), ("Crowd around the cage", "الازدحام حول القفص")), "a"),
 {"topic_en": "Routes of injection", "topic_ar": "طرق الحقن"},
 Q("The most accessible and visible vein in the rabbit is the:", "أسهل الأوردة وصولًا وأوضحها في الأرنب:", O(("Jugular vein", "الوريد الوداجي"), ("Ear vein", "وريد الأذن"), ("Tail vein", "وريد الذيل"), ("Femoral vein", "الوريد الفخذي")), "b"),
 Q("The ear vein is seen on the:", "يُرى وريد الأذن على:", O(("Ventral surface of the ear", "السطح البطني للأذن"), ("Tip of the ear only", "رأس الأذن فقط"), ("Dorsal edge of either ear", "الحافّة الظهرية لأيّ من الأذنين"), ("Base of the tail", "قاعدة الذيل")), "c"),
 Q("The ear vein may be enlarged before injection by:", "يمكن توسيع وريد الأذن قبل الحقن بـ:", O(("Cooling with ice", "التبريد بالثلج"), ("Applying alcohol only", "وضع الكحول فقط"), ("Shaking the rabbit", "هزّ الأرنب"), ("Heating and pressure over the vein at the base of the ear", "التدفئة والضغط على الوريد عند قاعدة الأذن")), "d"),
 Q("In IV injection the needle is inserted:", "في الحقن الوريدي تُدخل الإبرة:", O(("In the direction of the blood flow (toward the head)", "باتّجاه جريان الدم (نحو الرأس)"), ("Against the blood flow", "عكس جريان الدم"), ("Vertically into the cartilage", "عموديًا في الغضروف"), ("Into the artery", "في الشريان")), "a"),
 Q("A sign of correct intravenous injection is:", "من علامات الحقن الوريدي الصحيح:", O(("A raised area in the tissue", "منطقة منتفخة في النسيج"), ("Dilution of the blood in the vein and an easily moving plunger", "تخفّف الدم في الوريد وسهولة حركة المكبس"), ("Bleeding before injection", "النزف قبل الحقن"), ("Bubbles in the syringe", "فقاعات في المحقنة")), "b"),
 Q("Intraperitoneal injection is the injection of material into the:", "الحقن داخل الصفاق هو حقن المادة في:", O(("Blood stream", "مجرى الدم"), ("Muscle", "العضلة"), ("Peritoneal (abdominal) cavity", "التجويف الصفاقي (البطني)"), ("Skin layers", "طبقات الجلد")), "c"),
 Q("For intraperitoneal injection the animal is placed:", "في الحقن داخل الصفاق يوضع الحيوان:", O(("On its side", "على جانبه"), ("Standing", "واقفًا"), ("Upside down by the tail", "مقلوبًا من الذيل"), ("On its back", "على ظهره")), "d"),
 Q("In IP injection the inoculum is injected carefully to:", "في الحقن داخل الصفاق يُحقن اللقاح بحذر لـ:", O(("Prevent injection into the animal organs", "منع الحقن في أعضاء الحيوان"), ("Make a raised area", "تكوين منطقة منتفخة"), ("Reach the heart", "الوصول إلى القلب"), ("Dilute the blood", "تخفيف الدم")), "a"),
 Q("Subcutaneous injection is usually given in the:", "الحقن تحت الجلد يُعطى عادةً في:", O(("Ear", "الأذن"), ("Back", "الظهر"), ("Heart", "القلب"), ("Tail vein", "وريد الذيل")), "b"),
 Q("The syringe used for subcutaneous injection in the sheet is the:", "المحقنة المستعملة للحقن تحت الجلد في الورقة:", O(("Insulin pen", "قلم الإنسولين"), ("50 ml syringe", "محقنة 50 مل"), ("Tuberculin syringe", "محقنة التوبركلين"), ("Glass pipette", "ماصّة زجاجية")), "c"),
 Q("The sign of a correct subcutaneous injection is:", "علامة الحقن الصحيح تحت الجلد:", O(("No change in the skin", "لا تغيّر في الجلد"), ("Blood in the syringe", "دم في المحقنة"), ("Dilution of blood in a vein", "تخفّف الدم في الوريد"), ("A slightly raised area under the skin", "منطقة مرتفعة قليلًا تحت الجلد")), "d"),
 Q("The disinfectant used before and after injection is:", "المطهّر المستعمل قبل الحقن وبعده:", O(("70% ethanol", "إيثانول 70%"), ("Formalin", "الفورمالين"), ("Hayem’s solution", "محلول هايم"), ("Distilled water", "الماء المقطّر")), "a"),
 {"topic_en": "Blood harvesting", "topic_ar": "جمع الدم"},
 Q("Blood is collected after immunization to:", "يُجمع الدم بعد التمنيع لـ:", O(("Count platelets", "عدّ الصفائح"), ("Detect antibody formation against the injected antigen", "الكشف عن تكوّن الأضداد ضدّ المستضد المحقون"), ("Measure glucose", "قياس السكّر"), ("Grow bacteria", "زرع البكتيريا")), "b"),
 Q("The two main sites to collect blood in the rabbit are:", "الموضعان الرئيسيان لجمع دم الأرنب:", O(("Tail vein and jugular vein", "وريد الذيل والوريد الوداجي"), ("Femoral artery and liver", "الشريان الفخذي والكبد"), ("Auricular artery (marginal ear vein) and cardiac puncture", "الشريان الأذيني (وريد الأذن الحافّي) وبزل القلب"), ("Skin and muscle", "الجلد والعضلة")), "c"),
 Q("Cardiac puncture gives:", "بزل القلب يعطي:", O(("Many small samples over days", "عيّنات صغيرة كثيرة على مدى أيام"), ("A sample for cardiac histology", "عيّنة لنسيج القلب"), ("A separate arterial sample", "عيّنة شريانية منفصلة"), ("A single, large, good quality sample", "عيّنة واحدة كبيرة جيّدة النوعية")), "d"),
 Q("By cardiac puncture, the blood obtained from a rabbit is about:", "بزل القلب في الأرنب يعطي نحو:", O(("20-60 ml", "20-60 مل"), ("1-2 ml", "1-2 مل"), ("10-15 ml", "10-15 مل"), ("200 ml", "200 مل")), "a"),
 Q("In cardiac puncture, blood is preferably taken from the:", "في بزل القلب يُفضّل أخذ الدم من:", O(("Atrium", "الأذين"), ("Ventricle", "البطين"), ("Aorta", "الأبهر"), ("Pericardium", "التامور")), "b"),
 Q("Blood is withdrawn slowly in cardiac puncture to:", "يُسحب الدم ببطء في بزل القلب لـ:", O(("Increase the volume", "زيادة الحجم"), ("Allow clotting", "السماح بالتخثّر"), ("Prevent the heart collapsing", "منع انخماص القلب"), ("Wake the animal", "إيقاظ الحيوان")), "c"),
 {"topic_en": "Picture questions", "topic_ar": "أسئلة الصور"},
 Q("In this picture, the vessel running along the edge of the rabbit ear is the:", "في هذه الصورة، الوعاء الممتدّ على حافّة أذن الأرنب هو:", O(("Auricular artery", "الشريان الأذيني"), ("Jugular vein", "الوريد الوداجي"), ("Carotid artery", "الشريان السباتي"), ("Marginal vein", "الوريد الحافّي")), "d", img="assets/ear-marginal-vein.png", img_h="34mm"),
 Q("This picture shows which route of injection?", "هذه الصورة تُظهر أيّ طريق للحقن؟", O(("Intraperitoneal", "داخل الصفاق"), ("Intravenous (ear)", "وريدي (الأذن)"), ("Subcutaneous", "تحت الجلد"), ("Cardiac", "قلبي")), "a", img="assets/ip-injection-1.png", img_h="32mm"),
 Q("These pictures show:", "هذه الصور تُظهر:", O(("Subcutaneous injection", "الحقن تحت الجلد"), ("Ear vein injection", "الحقن في وريد الأذن"), ("Heart puncture in a rat", "بزل القلب في جرذ"), ("Intraperitoneal injection in a rabbit", "الحقن داخل الصفاق في أرنب")), "c", img="assets/heart-puncture-steps.png", img_h="40mm"),
]
mcq = balance(mcq, 8)
tf = [
 TF("Selection of an animal model is one of the most important steps in experimental studies.", "اختيار النموذج الحيواني من أهمّ الخطوات في الدراسات التجريبية.", "T"),
 TF("Hamsters are non-rodents.", "الهامستر من غير القوارض.", "F"),
 TF("An agitated animal may become violent for self-protection.", "الحيوان المُهيَّج قد يصبح عنيفًا دفاعًا عن نفسه.", "T"),
 TF("Intravenous injection is a direct injection into the blood stream.", "الحقن الوريدي حقن مباشر في مجرى الدم.", "T"),
 TF("In ear vein injection the needle is inserted away from the head of the rabbit.", "في الحقن بوريد الأذن تُدخل الإبرة بعيدًا عن رأس الأرنب.", "F"),
 TF("A raised area around the vein means the IV injection was correct.", "ظهور منطقة منتفخة حول الوريد يعني أن الحقن الوريدي صحيح.", "F"),
 TF("After IV injection, pressure is applied to the site to stop bleeding.", "بعد الحقن الوريدي يُضغط على الموضع لإيقاف النزف.", "T"),
 TF("Anesthesia may be used for intraperitoneal injection.", "قد يُستعمل التخدير في الحقن داخل الصفاق.", "T"),
 TF("The needle for IP injection may contain bubbles.", "يجوز أن تحتوي إبرة الحقن داخل الصفاق على فقاعات.", "F"),
 TF("In subcutaneous injection the needle is inserted almost horizontal.", "في الحقن تحت الجلد تُدخل الإبرة بوضع شبه أفقي.", "T"),
 TF("Cardiac puncture is done on a fully awake, unanesthetized animal.", "يُجرى بزل القلب على حيوان يقظ تمامًا وغير مخدّر.", "F"),
 TF("Cardiac puncture is appropriate for all strains of rat.", "بزل القلب مناسب لكل سلالات الجرذان.", "T"),
 TF("10 - 15 ml of blood can be obtained from a rat by cardiac puncture.", "يمكن الحصول على 10 - 15 مل دم من الجرذ ببزل القلب.", "T"),
 TF("Blood should be withdrawn quickly in cardiac puncture.", "يجب سحب الدم بسرعة في بزل القلب.", "F"),
]
traps = [
 TR("Raised area: good or bad?", "المنطقة المنتفخة: جيّدة أم سيّئة؟", "IV: NO raised area should appear (a bump = the needle is outside the vein). SC: a slightly raised area IS the sign of correct injection.",
    "الوريدي: لا يجب أن تظهر منطقة منتفخة (الانتفاخ = الإبرة خارج الوريد). وتحت الجلد: المنطقة المرتفعة قليلًا هي علامة الحقن الصحيح."),
 TR("Rabbit is not a rodent", "الأرنب ليس من القوارض", "Rodents: mice, rats, guinea pigs, hamster. The rabbit is listed with non-rodents (dog, cat, monkey).",
    "القوارض: الفئران، الجرذان، خنازير غينيا، الهامستر. والأرنب مذكور مع غير القوارض (الكلب، القطّ، القرد)."),
 TR("Direction of the needle", "اتّجاه الإبرة", "Ear vein: insert the needle in the direction of the blood flow — toward the HEAD of the rabbit.",
    "وريد الأذن: أدخل الإبرة باتّجاه جريان الدم — نحو رأس الأرنب."),
 TR("Vein vs artery in the ear", "الوريد مقابل الشريان في الأذن", "Marginal vein = along the edge (used for IV injection); auricular artery = in the middle of the ear.",
    "الوريد الحافّي = على الحافّة (يُستعمل للحقن الوريدي)؛ والشريان الأذيني = في وسط الأذن."),
 TR("Rat vs rabbit volumes", "حجوم الجرذ مقابل الأرنب", "Cardiac puncture: rat 10–15 ml, rabbit 20–60 ml — depending on size and whether the heart is beating.",
    "بزل القلب: الجرذ 10–15 مل، والأرنب 20–60 مل — حسب الحجم وما إذا كان القلب ينبض."),
 TR("Which syringe?", "أيّ محقنة؟", "Subcutaneous injection uses a tuberculin syringe, needle almost horizontal, usually in the back.",
    "الحقن تحت الجلد يستعمل محقنة التوبركلين، والإبرة شبه أفقية، وعادةً في الظهر."),
 TR("Slow, not fast", "ببطء لا بسرعة", "Inject the inoculum slowly (IV, SC) and withdraw heart blood slowly to prevent the heart collapsing.",
    "احقن اللقاح ببطء (الوريدي وتحت الجلد) واسحب دم القلب ببطء لمنع انخماص القلب."),
]
important = [
 IM("What are the three main objectives in selecting an animal model?", "ما الأهداف الثلاثة الرئيسية لاختيار النموذج الحيواني؟",
    "1) An animal phylogenetically closer to man. 2) An animal in which the process under investigation is as close as possible to that in man. 3) Similar anatomy, physiology and biochemistry.",
    "1) حيوان أقرب تطوّريًا إلى الإنسان. 2) حيوان تكون فيه العملية قيد الدراسة أقرب ما يمكن إلى ما في الإنسان. 3) تشريح ووظائف أعضاء وكيمياء حيوية متشابهة."),
 IM("Classify experimental animals with examples.", "صنّف حيوانات التجارب مع أمثلة.",
    "Rodents: mice, rats, guinea pigs, hamster. Non-rodents: rabbit, dog, cat, monkey.", "القوارض: الفئران، الجرذان، خنازير غينيا، الهامستر. وغير القوارض: الأرنب، الكلب، القطّ، القرد."),
 IM("Describe intravenous injection in the rabbit ear vein.", "صف الحقن الوريدي في وريد أذن الأرنب.",
    "Find the vein on the dorsal edge of the ear; shave; disinfect with 70% ethanol; enlarge the vein by heating and pressure at the base of the ear; hold the ear; insert the needle toward the head; inject slowly watching for dilution of blood (plunger moves easily, no raised area); withdraw, press to stop bleeding, disinfect and put cotton.",
    "حدّد الوريد على الحافّة الظهرية للأذن؛ احلق؛ طهّر بإيثانول 70%؛ وسّع الوريد بالتدفئة والضغط عند قاعدة الأذن؛ أمسك الأذن؛ أدخل الإبرة نحو الرأس؛ احقن ببطء مع مراقبة تخفّف الدم (المكبس يتحرّك بسهولة، بلا انتفاخ)؛ اسحب واضغط لإيقاف النزف وطهّر وضع قطنة."),
 IM("Describe intraperitoneal injection.", "صف الحقن داخل الصفاق.",
    "Injection into the peritoneal cavity; animal (rabbit or mouse) on its back, anesthesia may be used; clip hair and disinfect with 70% ethanol; grasp skin and peritoneum; insert a bubble-free needle through skin and peritoneum; inject carefully avoiding the organs; remove needle and disinfect again.",
    "حقن في التجويف الصفاقي؛ الحيوان (أرنب أو فأر) على ظهره، وقد يُستعمل التخدير؛ قصّ الشعر وطهّر بإيثانول 70%؛ أمسك الجلد والصفاق؛ أدخل إبرة خالية من الفقاعات عبر الجلد والصفاق؛ احقن بحذر متجنّبًا الأعضاء؛ أخرج الإبرة وطهّر مجدّدًا."),
 IM("Describe subcutaneous injection.", "صف الحقن تحت الجلد.",
    "Injection under the skin, usually in the back: clean, shave and disinfect with 70% ethanol; load a tuberculin syringe; insert the needle almost horizontal; inject slowly and observe a slightly raised area under the skin; remove needle and disinfect again.",
    "حقن تحت الجلد، عادةً في الظهر: نظّف واحلق وطهّر بإيثانول 70%؛ املأ محقنة التوبركلين؛ أدخل الإبرة شبه أفقية؛ احقن ببطء ولاحظ منطقة مرتفعة قليلًا تحت الجلد؛ أخرج الإبرة وطهّر مجدّدًا."),
 IM("Why is blood harvested after immunization, and from which sites in the rabbit?", "لماذا يُجمع الدم بعد التمنيع، ومن أيّ مواضع في الأرنب؟",
    "To detect antibody formation against the injected antigen (e.g. RBCs and serum of human and rabbit). Sites: the ear (auricular artery / marginal ear vein) and cardiac (heart) puncture.",
    "للكشف عن تكوّن الأضداد ضدّ المستضد المحقون (مثل كريات الدم الحمر ومصل الإنسان والأرنب). والمواضع: الأذن (الشريان الأذيني / وريد الأذن الحافّي) وبزل القلب."),
 IM("Describe cardiac puncture.", "صف بزل القلب.",
    "A technique to get a single, large, good quality blood sample from a euthanized or deeply anesthetized animal (when coagulation tests, separate arterial/venous samples or cardiac histology are not needed). Rat 10–15 ml, rabbit 20–60 ml. Blood is taken from the heart, preferably the ventricle, via the left chest, through the diaphragm or from the top of the sternum, and withdrawn slowly to prevent the heart collapsing.",
    "تقنية للحصول على عيّنة دم واحدة كبيرة جيّدة النوعية من حيوان مقتول رحيمًا أو تحت تخدير عميق (عند عدم الحاجة إلى فحوص التخثّر أو عيّنات شريانية/وريدية منفصلة أو نسيج القلب). الجرذ 10–15 مل، والأرنب 20–60 مل. يُؤخذ الدم من القلب، ويُفضّل البطين، عن طريق الجانب الأيسر للصدر أو عبر الحجاب الحاجز أو من أعلى القصّ، ويُسحب ببطء لمنع انخماص القلب."),
]
meta = dict(subject_en="Practical Immunology", subject_ar="علم المناعة العملي", short_ar="مناعة", instructor="م.م. جنان خليل",
            unit_en="Lab 4", unit_ar="العملي 4", unit_label="LAB", unit_no="4",
            title_en="Immunization of laboratory animals, Animal heart puncture", title_ar="تمنيع حيوانات المختبر وبزل القلب",
            department="تقنيات المختبرات الطبية", stage="The third stage — الثالثة", kind="Laboratories — عملي")
blocks, mcq, tf, traps, important = ltr_all(blocks), ltr_all(mcq), ltr_all(tf), ltr_all(traps), ltr_all(important)
save(FOLDER, meta, blocks, mcq, tf, traps, important)
fit(FOLDER)   # no big gaps (fill2 >= 80%)

```
