---
source: BIOS-Obsidian/tools/scripts/lb3/gl3.py
handouts: [genetics-lab3-medical-genetics]
saved: 2026-10-31
tags: [bios, code]
---
# lb3/gl3.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#genetics-lab3-medical-genetics|genetics-lab3-medical-genetics]]

```python
import sys; sys.path.insert(0, "/tmp/claude-0/-home-user--/8f878068-bae9-502b-96f7-788f221c7cb0/scratchpad/imm456")
from ci import *            # c helpers + B INSHORT TERMS balance save(split.fix)

GL = dict(subject_en="Human Genetics", subject_ar="الوراثة البشرية", short_ar="وراثة", unit_label="LAB",
          kind="Laboratories — عملي", stage="The third stage — الثالثة", instructor="م.م. نور م. فاضل")
BN = lambda en, ar: N(en, ar, label=["BIOS note", "ملاحظة BIOS"])

blocks = [
 SEC("Medical genetics", "الوراثة الطبية"),
 C("**medical genetics** : it involves **any application of genetics to medical practice** it includes ;", "**الوراثة الطبية:** تشمل **أي تطبيق لعلم الوراثة في الممارسة الطبية**، وتتضمّن:"),
 R("Studies of the **inheritance of disease in families** .", "دراسة **توارث الأمراض في العائلات**."),
 R("The **mapping of disease genes** to specific locations on chromosomes .", "**تحديد مواقع جينات الأمراض** في أماكن معيّنة على الكروموسومات."),
 R("Analysis of the **molecular mechanisms** through which genes cause disease .", "تحليل **الآليات الجزيئية** التي تسبّب بها الجينات المرض."),
 N("The knowledge of medical genetics is **important for health care** .. Because … Genetics disease make up a **large proportion of the total disease burden** in both **paediatric and adult** populations ..",
   "معرفة الوراثة الطبية **مهمّة للرعاية الصحية**. لأن الأمراض الوراثية تشكّل **نسبة كبيرة من العبء الكلي للأمراض** عند **الأطفال والبالغين** على حدّ سواء.", label=["Why it matters", "لماذا هي مهمّة"]),
 INSHORT([("Medical genetics = genetics **applied to medicine**.", "الوراثة الطبية = الوراثة **مطبَّقة في الطب**."),
          ("3 parts: **family inheritance, gene mapping, molecular mechanisms**.", "3 محاور: **التوارث العائلي، وتحديد مواقع الجينات، والآليات الجزيئية**.")]),

 SEC("Types of genetic disease", "أنواع الأمراض الوراثية"),
 T([B("Type", "النوع"), B("Description", "الوصف"), B("Examples", "أمثلة")],
   [[B("**1- chromosomal disorder**", "**1. الاضطراب الكروموسومي**"), B("when large segment or the whole chromosome is missing , duplicated or altered", "حين تكون قطعة كبيرة أو الكروموسوم كله مفقودًا أو مضاعفًا أو متغيّرًا"), B("Down syndrome and turner syndrome", "متلازمة داون ومتلازمة تيرنر")],
    [B("**2- disorder in which single genes are altered** (mendelian) / single Gene disorder", "**2. اضطراب يتغيّر فيه جين واحد** (مندلي) / اضطراب الجين المفرد"), B("single genes are altered", "يتغيّر فيه جين مفرد"), B("cystic fibrosis, sickle cell disease and haemophilia", "التليّف الكيسي، وفقر الدم المنجلي، والهيموفيليا (الناعور)")],
    [B("**3- multifactor disorder**", "**3. الاضطراب متعدّد العوامل**"), B("due to combination of multiple genetic as well as environmental causes", "ينتج عن مزيج من أسباب وراثية متعدّدة وأسباب بيئية"), B("Many birth defect: cleft lip or cleft palate, heart disease and diabetes", "كثير من التشوّهات الخلقية: الشفة المشقوقة أو شقّ الحنك، وأمراض القلب، والسكري")],
    [B("**4- mitochondrial disorder**", "**4. الاضطراب المايتوكوندري**"), B("small number of disease caused by alterations in the small cytoplasmic mitochondrial chromosomes", "عدد قليل من الأمراض سببه تغيّرات في الكروموسومات المايتوكوندرية الصغيرة في السايتوبلازم"), "—"]],
   key_cols=[0], widths=[28, 40, 32], style="summary", label_en="4 types", label_ar="4 أنواع"),
 T([B("Term", "المصطلح"), B("Definition", "التعريف")],
   [[B("**Autosomal chromosomes**", "**الكروموسومات الجسمية**"), B("any chromosomes other than sex chromosomes", "أي كروموسومات غير الكروموسومات الجنسية")],
    [B("**Sex chromosomes**", "**الكروموسومات الجنسية**"), B("X & Y chromosomes which differ in male and female ( XX in the female XY in male ) these chromosomes are responsible for sex determination", "الكروموسومان X وY ويختلفان بين الذكر والأنثى (XX في الأنثى وXY في الذكر)، وهما المسؤولان عن تحديد الجنس")]],
   key_cols=[0], widths=[30, 70]),
 INSHORT([("4 types: **chromosomal, single gene, multifactorial, mitochondrial**.", "4 أنواع: **كروموسومي، وجين مفرد، ومتعدّد العوامل، ومايتوكوندري**."),
          ("Down/Turner = **chromosomal**; CF, sickle cell, haemophilia = **single gene**.", "داون/تيرنر = **كروموسومي**؛ والتليّف الكيسي والمنجلي والهيموفيليا = **جين مفرد**."),
          ("Cleft lip, heart disease, diabetes = **multifactorial** (genes + environment).", "الشفة المشقوقة وأمراض القلب والسكري = **متعدّد العوامل** (جينات + بيئة)."),
          ("Female **XX**, male **XY**.", "الأنثى **XX**، والذكر **XY**.")]),

 SEC("The classification of chromosomes", "تصنيف الكروموسومات"),
 H2("1- Based on the number of the centromers", "1. بحسب عدد السنتروميرات"),
 T([B("Type", "النوع"), B("Centromeres", "السنتروميرات")],
   [[B("**Acrocentric**", "**أكروسنتري (عديم السنترومير)**"), B("absence of centromere and this type is not found in human", "غياب السنترومير، وهذا النوع لا يوجد في الإنسان")],
    [B("**Monocentric**", "**أحادي السنترومير**"), B("only one centromere found and this type found in human", "يوجد سنترومير واحد فقط، وهذا النوع يوجد في الإنسان")],
    [B("**Dicentric**", "**ثنائي السنترومير**"), B("two centromeres are found within the chromosomes.", "يوجد سنتروميران في الكروموسوم.")],
    [B("**Polycentric**", "**متعدّد السنتروميرات**"), B("more than two centromeres are Found .", "يوجد أكثر من سنتروميرين.")]],
   key_cols=[0], widths=[32, 68], style="summary", label_en="By number", label_ar="بحسب العدد"),
 BN("In the number-based list, the chromosome **without a centromere** is called **acentric**; \"Acrocentric\" here is a slip — acrocentric belongs to the location-based list below.",
    "في التصنيف بحسب العدد، الكروموسوم **الخالي من السنترومير** يُسمّى **acentric (عديم السنترومير)**؛ وكلمة \"Acrocentric\" هنا سهو، لأن الأكروسنتري من التصنيف بحسب الموقع في الأسفل."),
 H2("2- Based on the location of the centromers", "2. بحسب موقع السنترومير"),
 T([B("Type", "النوع"), B("Location of centromere", "موقع السنترومير")],
   [[B("**Telocentric**", "**طرفي السنترومير**"), B("located at one end of the chromosome; not found in human but in mouse .", "في أحد طرفي الكروموسوم؛ لا يوجد في الإنسان بل في الفأر.")],
    [B("**Acrocentric**", "**قريب الطرف (أكروسنتري)**"), B("located near one end of the chromosome being sub terminal in Position", "قريب من أحد الطرفين، أي في موقع تحت طرفي")],
    [B("**Sub metacentric**", "**تحت الوسطي**"), B("located in the upper arm .", "في الذراع العلوي.")],
    [B("**Metacentric**", "**وسطي السنترومير**"), B("located in the middle of the chromosome .", "في منتصف الكروموسوم.")]],
   key_cols=[0], widths=[32, 68], style="summary", label_en="By location", label_ar="بحسب الموقع"),
 BN("In a **submetacentric** chromosome the centromere is **a little off the middle**, so one arm is shorter (short arm, p) and one longer (long arm, q).",
    "في الكروموسوم **تحت الوسطي** يكون السنترومير **بعيدًا قليلًا عن المنتصف**، فيصبح ذراع أقصر (الذراع القصير p) وذراع أطول (الذراع الطويل q)."),
 F("chromosome-types.png", "Types of chromosomes: telocentric, acrocentric, submetacentric, metacentric", "أنواع الكروموسومات: طرفي، وقريب الطرف، وتحت الوسطي، ووسطي", h="52mm"),
 T([B("Label in the figure", "التسمية في الشكل"), B("Arabic", "بالعربي")],
   [["**Centromere**", "السنترومير"], ["**Satellite**", "التابع (القمر)"], ["**Stalk**", "السويقة"], ["**Short arm**", "الذراع القصير"], ["**Long arm**", "الذراع الطويل"]],
   key_cols=[0], ar_cols=[1], widths=[45, 55], label_en="Figure labels", label_ar="تسميات الشكل"),
 FLOW([("Telocentric: at the end", "طرفي: في الطرف"), ("Acrocentric: near the end", "قريب الطرف: قرب الطرف"), ("Submetacentric: off centre", "تحت الوسطي: بعيد عن المركز قليلًا"), ("Metacentric: middle", "وسطي: في المنتصف")],
      en="From the end to the middle", ar="من الطرف إلى المنتصف"),
 INSHORT([("By number: **acentric (0), monocentric (1, human), dicentric (2), polycentric (> 2)**.", "بحسب العدد: **عديم (0)، وأحادي (1، في الإنسان)، وثنائي (2)، ومتعدّد (> 2)**."),
          ("By location: **telocentric (mouse), acrocentric, submetacentric, metacentric**.", "بحسب الموقع: **طرفي (الفأر)، وقريب الطرف، وتحت الوسطي، ووسطي**."),
          ("Telocentric is **not found in human**.", "الطرفي **لا يوجد في الإنسان**.")]),

 SEC("3- Based on the location of the centromere and the length", "3. بحسب موقع السنترومير والطول"),
 C("Based on the location of the centromere and the length of the chromosomes is type of classification which is now depend on :", "التصنيف بحسب موقع السنترومير وطول الكروموسومات هو النوع المعتمد حاليًا:"),
 T([B("Group", "المجموعة"), B("Chromosomes", "الكروموسومات"), B("Length", "الطول"), B("Centromere", "السنترومير")],
   [[B("**A**", "**A**"), "**1, 2, 3**", B("the longest", "الأطول"), B("metacentric", "وسطي")],
    [B("**B**", "**B**"), "**4, 5**", B("long", "طويلة"), B("off – center sub metacentric", "بعيد عن المركز، تحت الوسطي")],
    [B("**C**", "**C**"), "**6–12 and X**", B("long", "طويلة"), B("sub metacentric", "تحت الوسطي")],
    [B("**D**", "**D**"), "**13, 14, 15**", B("short", "قصيرة"), B("acrocentric", "قريب الطرف")],
    [B("**E**", "**E**"), "**16, 17, 18**", B("short", "قصيرة"), B("sub metacentric", "تحت الوسطي")],
    [B("**F**", "**F**"), "**19, 20**", B("short", "قصيرة"), B("metacentric", "وسطي")],
    [B("**G**", "**G**"), "**21, 22 and Y**", B("the shortest", "الأقصر"), B("acrocentric", "قريب الطرف")]],
   key_cols=[0], widths=[14, 24, 24, 38], style="summary", label_en="Groups A–G", label_ar="المجموعات A–G"),
 F("karyotype.png", "Normal human karyotype: chromosome pairs 1–22, X and Y", "النمط النووي البشري الطبيعي: أزواج الكروموسومات 1–22 وX وY", h="70mm"),
 INSHORT([("**A (1–3)** longest metacentric; **G (21, 22, Y)** shortest acrocentric.", "**A (1–3)** الأطول والوسطية؛ و**G (21، 22، Y)** الأقصر وقريبة الطرف."),
          ("**X is in group C**; **Y is in group G**.", "**X في المجموعة C**؛ و**Y في المجموعة G**."),
          ("Acrocentric groups: **D and G**; metacentric groups: **A and F**.", "مجموعات قريبة الطرف: **D وG**؛ والوسطية: **A وF**.")]),

 SEC("The structure and function of genes and chromosomes", "تركيب الجينات والكروموسومات ووظيفتها"),
 L(["somatic cell are **diploid** having **22 pairs of autosomal chromosomes** and **one pair of sex chromosomes** ..",
    "Gametes are **haploid** and having **23 chromosomes** ..",
    "The diploid number of chromosomes is maintained in successive generations of somatic cells by the process of **mitosis** while the haploid number is maintained through **meiosis** ."],
   ["الخلايا الجسمية **ثنائية المجموعة**، فيها **22 زوجًا من الكروموسومات الجسمية** و**زوج واحد من الكروموسومات الجنسية**.",
    "والأمشاج **أحادية المجموعة**، فيها **23 كروموسومًا**.",
    "ويُحافَظ على العدد الثنائي في الأجيال المتعاقبة من الخلايا الجسمية بعملية **الانقسام الخيطي**، بينما يُحافَظ على العدد الأحادي عبر **الانقسام الاختزالي**."]),
 C(["**Genes** : the **unit of inheritance** , are located on the chromosomes of gametes , as well as somatic cells .",
    "They passed from parents to progeny through successive generation after **fertilization** .",
    "The human is estimated to have **5000 to 10000 structural gene** ( that code an error or mutation in one of these genes often leads to a **recognizable genetic disease** ."],
   ["**الجينات**: **وحدة الوراثة**، وتوجد على كروموسومات الأمشاج وكذلك الخلايا الجسمية.",
    "وتنتقل من الآباء إلى الأبناء عبر الأجيال المتعاقبة بعد **الإخصاب**.",
    "ويُقدَّر أن لدى الإنسان **5000 إلى 10000 جين تركيبي**، وأي خطأ أو طفرة في أحد هذه الجينات يؤدي غالبًا إلى **مرض وراثي واضح**."]),
 BN("The gene number is written as **5000 to 10000** in the lab sheet; older textbooks gave **50 000–100 000**, and today the human genome is known to have about **20 000 protein-coding genes**. Use the lecturer's number in her exam.",
    "عدد الجينات مكتوب في الملزمة **5000 إلى 10000**؛ وكانت الكتب القديمة تذكر **50 000–100 000**، والمعروف اليوم أن المجين البشري فيه نحو **20 000 جين مشفّر للبروتين**. اعتمد رقم المدرّسة في امتحانها."),
 T([B("Cell", "الخلية"), B("Chromosomes", "الكروموسومات"), B("Kept by", "يُحافَظ عليه بـ")],
   [[B("**Somatic (2n)**", "**الجسمية (2n)**"), B("46 = 22 pairs autosomes + 1 pair sex chromosomes", "46 = 22 زوجًا جسميًا + زوج جنسي"), B("Mitosis", "الانقسام الخيطي")],
    [B("**Gamete (n)**", "**المشيج (n)**"), "23", B("Meiosis", "الانقسام الاختزالي")]],
   key_cols=[0], widths=[24, 46, 30], style="summary", label_en="2n vs n", label_ar="2n مقابل n"),
 INSHORT([("Somatic = **46 (2n)** kept by **mitosis**; gamete = **23 (n)** made by **meiosis**.", "الجسمية = **46 (2n)** بالانقسام **الخيطي**؛ والمشيج = **23 (n)** بالانقسام **الاختزالي**."),
          ("A **mutation** in one gene → a recognizable genetic disease.", "**طفرة** في جين واحد ← مرض وراثي واضح.")]),
] + TERMS([
 ("Medical genetics", "الوراثة الطبية / علم الوراثة الطبي"),
 ("Gene mapping", "تحديد مواقع الجينات / رسم الخرائط الجينية"),
 ("Chromosomal disorder", "اضطراب كروموسومي / شذوذ صبغي"),
 ("Single gene (mendelian) disorder", "اضطراب الجين المفرد / مرض مندلي"),
 ("Multifactorial disorder", "اضطراب متعدّد العوامل"),
 ("Mitochondrial disorder", "اضطراب مايتوكوندري / مرض المتقدّرات"),
 ("Down syndrome / Turner syndrome", "متلازمة داون (المنغولية) / متلازمة تيرنر"),
 ("Cystic fibrosis", "التليّف الكيسي / المرض الليفي الكيسي"),
 ("Haemophilia", "الهيموفيليا / الناعور / نزف الدم الوراثي"),
 ("Cleft lip / cleft palate", "الشفة المشقوقة (الأرنبية) / شقّ الحنك"),
 ("Autosomes", "الكروموسومات الجسمية / الصبغيات الجسدية"),
 ("Sex chromosomes", "الكروموسومات الجنسية / صبغيات تحديد الجنس"),
 ("Acentric / Monocentric / Dicentric / Polycentric", "عديم / أحادي / ثنائي / متعدّد السنترومير"),
 ("Telocentric", "طرفي السنترومير"),
 ("Acrocentric", "قريب الطرف / أكروسنتري"),
 ("Submetacentric", "تحت الوسطي / شبه وسطي"),
 ("Metacentric", "وسطي السنترومير / متوسّط"),
 ("Karyotype", "النمط النووي / الطراز الكروموسومي"),
 ("Mutation", "طفرة / تغيّر وراثي"),
])

O = P
mcq = [
 {"topic_en": "Medical genetics and disease types", "topic_ar": "الوراثة الطبية وأنواع الأمراض"},
 Q("Medical genetics involves:", "تشمل الوراثة الطبية:", O(("Plant breeding only", "تربية النبات فقط"), ("Any application of genetics to medical practice", "أي تطبيق للوراثة في الممارسة الطبية"), ("Only blood transfusion", "نقل الدم فقط"), ("Only surgery", "الجراحة فقط")), "b"),
 Q("Down syndrome is an example of a:", "متلازمة داون مثال على:", O(("Chromosomal disorder", "اضطراب كروموسومي"), ("Single gene disorder", "اضطراب جين مفرد"), ("Mitochondrial disorder", "اضطراب مايتوكوندري"), ("Infection", "عدوى")), "a"),
 Q("Cystic fibrosis, sickle cell disease and haemophilia are:", "التليّف الكيسي والمنجلي والهيموفيليا:", O(("Chromosomal disorders", "اضطرابات كروموسومية"), ("Multifactorial disorders", "اضطرابات متعدّدة العوامل"), ("Single gene (mendelian) disorders", "اضطرابات جين مفرد (مندلية)"), ("Mitochondrial disorders", "اضطرابات مايتوكوندرية")), "c"),
 Q("Cleft lip, heart disease and diabetes are examples of:", "الشفة المشقوقة وأمراض القلب والسكري أمثلة على:", O(("Mitochondrial disorders", "اضطرابات مايتوكوندرية"), ("Chromosomal disorders", "اضطرابات كروموسومية"), ("Single gene disorders", "اضطرابات جين مفرد"), ("Multifactor disorders", "اضطرابات متعدّدة العوامل")), "d"),
 Q("Multifactor disorders are due to:", "تنتج الاضطرابات متعدّدة العوامل عن:", O(("Multiple genetic as well as environmental causes", "أسباب وراثية متعدّدة وبيئية"), ("One gene only", "جين واحد فقط"), ("Missing chromosome only", "كروموسوم مفقود فقط"), ("Mitochondria only", "المايتوكوندريا فقط")), "a"),
 Q("Mitochondrial disorders are caused by alterations in:", "تنتج الاضطرابات المايتوكوندرية عن تغيّرات في:", O(("Sex chromosomes", "الكروموسومات الجنسية"), ("Small cytoplasmic mitochondrial chromosomes", "الكروموسومات المايتوكوندرية الصغيرة في السايتوبلازم"), ("Autosomes only", "الكروموسومات الجسمية فقط"), ("Ribosomes", "الرايبوسومات")), "b"),
 Q("The sex chromosomes of a normal male are:", "الكروموسومات الجنسية للذكر الطبيعي:", O(("XX", "XX"), ("XO", "XO"), ("XY", "XY"), ("YY", "YY")), "c"),
 {"topic_en": "Classification of chromosomes", "topic_ar": "تصنيف الكروموسومات"},
 Q("The chromosome type found in human (by number of centromeres) is:", "نوع الكروموسوم الموجود في الإنسان (بحسب عدد السنتروميرات):", O(("Acentric", "عديم السنترومير"), ("Dicentric", "ثنائي السنترومير"), ("Polycentric", "متعدّد السنتروميرات"), ("Monocentric", "أحادي السنترومير")), "d"),
 Q("A chromosome with two centromeres is:", "الكروموسوم ذو السنتروميرين:", O(("Dicentric", "ثنائي السنترومير"), ("Monocentric", "أحادي السنترومير"), ("Telocentric", "طرفي"), ("Metacentric", "وسطي")), "a"),
 Q("The centromere at one end of the chromosome (found in mouse, not human) is:", "السنترومير في أحد طرفي الكروموسوم (في الفأر لا الإنسان):", O(("Metacentric", "وسطي"), ("Telocentric", "طرفي"), ("Acrocentric", "قريب الطرف"), ("Submetacentric", "تحت الوسطي")), "b"),
 Q("A chromosome with the centromere near one end (sub terminal) is:", "الكروموسوم ذو السنترومير القريب من أحد الطرفين (تحت طرفي):", O(("Metacentric", "وسطي"), ("Telocentric", "طرفي"), ("Acrocentric", "قريب الطرف"), ("Polycentric", "متعدّد")), "c"),
 Q("A metacentric chromosome has its centromere:", "الكروموسوم الوسطي يكون سنتروميره:", O(("At one end", "في أحد الطرفين"), ("Near one end", "قرب أحد الطرفين"), ("Absent", "غائبًا"), ("In the middle", "في المنتصف")), "d"),
 Q("Group A chromosomes are:", "كروموسومات المجموعة A:", O(("1, 2, 3 — longest, metacentric", "1، 2، 3 — الأطول والوسطية"), ("21, 22, Y — shortest", "21، 22، Y — الأقصر"), ("4, 5 — submetacentric", "4، 5 — تحت الوسطية"), ("19, 20 — short metacentric", "19، 20 — قصيرة وسطية")), "a"),
 Q("The X chromosome belongs to group:", "ينتمي الكروموسوم X إلى المجموعة:", O(("A", "A"), ("C", "C"), ("E", "E"), ("G", "G")), "b"),
 Q("Group D chromosomes (13, 14, 15) are:", "كروموسومات المجموعة D (13، 14، 15):", O(("Long metacentric", "طويلة وسطية"), ("Short submetacentric", "قصيرة تحت وسطية"), ("Short acrocentric", "قصيرة قريبة الطرف"), ("Longest", "الأطول")), "c"),
 Q("The Y chromosome belongs to group:", "ينتمي الكروموسوم Y إلى المجموعة:", O(("A", "A"), ("C", "C"), ("F", "F"), ("G", "G")), "d"),
 Q("Group F chromosomes are:", "كروموسومات المجموعة F:", O(("19, 20 — short and metacentric", "19، 20 — قصيرة ووسطية"), ("16, 17, 18", "16، 17، 18"), ("1, 2, 3", "1، 2، 3"), ("21, 22", "21، 22")), "a"),
 Q("Group E chromosomes (16, 17, 18) are:", "كروموسومات المجموعة E (16، 17، 18):", O(("Long acrocentric", "طويلة قريبة الطرف"), ("Short submetacentric", "قصيرة تحت وسطية"), ("Short metacentric", "قصيرة وسطية"), ("Longest", "الأطول")), "b"),
 {"topic_en": "Genes and chromosome number", "topic_ar": "الجينات وعدد الكروموسومات"},
 Q("Somatic cells contain:", "تحتوي الخلايا الجسمية على:", O(("23 chromosomes", "23 كروموسومًا"), ("22 chromosomes", "22 كروموسومًا"), ("22 pairs of autosomes and one pair of sex chromosomes", "22 زوجًا جسميًا وزوجًا جنسيًا"), ("23 pairs of sex chromosomes", "23 زوجًا جنسيًا")), "c"),
 Q("The haploid number in gametes is maintained through:", "يُحافَظ على العدد الأحادي في الأمشاج عبر:", O(("Mitosis", "الانقسام الخيطي"), ("Fertilization", "الإخصاب"), ("Crossing over", "العبور"), ("Meiosis", "الانقسام الاختزالي")), "d"),
 Q("The unit of inheritance is the:", "وحدة الوراثة هي:", O(("Gene", "الجين"), ("Centromere", "السنترومير"), ("Ribosome", "الرايبوسوم"), ("Gamete", "المشيج")), "a"),
 {"topic_en": "Picture questions", "topic_ar": "أسئلة الصور"},
 Q("In this figure, the chromosome with satellites and a stalk is:", "في هذا الشكل، الكروموسوم ذو التوابع والسويقة:", O(("Telocentric", "طرفي"), ("Acrocentric", "قريب الطرف"), ("Metacentric", "وسطي"), ("Submetacentric", "تحت الوسطي")), "b", img="assets/chromosome-types.png", img_h="36mm"),
 Q("This picture of chromosome pairs 1–22, X and Y is called a:", "تُسمّى صورة أزواج الكروموسومات 1–22 وX وY هذه:", O(("Pedigree", "شجرة العائلة"), ("Blood film", "مسحة دموية"), ("Karyotype", "نمط نووي"), ("Gel", "هلام")), "c", img="assets/karyotype.png", img_h="40mm"),
]
mcq = balance(mcq, 15)
tf = [
 TF("Mapping disease genes to chromosomes is part of medical genetics.", "تحديد مواقع جينات الأمراض على الكروموسومات جزء من الوراثة الطبية.", "T"),
 TF("Genetic diseases are a small part of the disease burden.", "الأمراض الوراثية جزء صغير من عبء الأمراض.", "F"),
 TF("Turner syndrome is a chromosomal disorder.", "متلازمة تيرنر اضطراب كروموسومي.", "T"),
 TF("Haemophilia is a multifactorial disorder.", "الهيموفيليا اضطراب متعدّد العوامل.", "F"),
 TF("Autosomes are all chromosomes other than sex chromosomes.", "الكروموسومات الجسمية هي كل الكروموسومات غير الجنسية.", "T"),
 TF("Telocentric chromosomes are found in human.", "توجد الكروموسومات الطرفية في الإنسان.", "F"),
 TF("Group G contains the shortest acrocentric chromosomes.", "تحتوي المجموعة G على أقصر الكروموسومات قريبة الطرف.", "T"),
 TF("Group B chromosomes are 4 and 5.", "كروموسومات المجموعة B هي 4 و5.", "T"),
 TF("Gametes are diploid with 46 chromosomes.", "الأمشاج ثنائية المجموعة وفيها 46 كروموسومًا.", "F"),
 TF("The diploid number in somatic cells is maintained by mitosis.", "يُحافَظ على العدد الثنائي في الخلايا الجسمية بالانقسام الخيطي.", "T"),
 TF("A mutation in a structural gene often leads to a recognizable genetic disease.", "تؤدي الطفرة في جين تركيبي غالبًا إلى مرض وراثي واضح.", "T"),
]
traps = [
 TR("Acentric vs acrocentric", "عديم السنترومير مقابل قريب الطرف", "No centromere = acentric (not in human). Acrocentric = centromere NEAR one end (groups D and G).", "بلا سنترومير = acentric (لا يوجد في الإنسان). وacrocentric = سنترومير قرب أحد الطرفين (المجموعتان D وG)."),
 TR("Telocentric vs acrocentric", "الطرفي مقابل قريب الطرف", "Telocentric: AT the end (mouse, not human). Acrocentric: NEAR the end (human).", "الطرفي: في الطرف نفسه (الفأر لا الإنسان). قريب الطرف: قرب الطرف (الإنسان)."),
 TR("Where are X and Y?", "أين X وY؟", "X is in group C (long submetacentric); Y is in group G (shortest acrocentric).", "X في المجموعة C (طويلة تحت وسطية)؛ وY في المجموعة G (الأقصر وقريبة الطرف)."),
 TR("Metacentric groups", "المجموعات الوسطية", "A (1–3, longest) and F (19, 20, short) are metacentric.", "A (1–3، الأطول) وF (19، 20، قصيرة) وسطية."),
 TR("Single gene vs multifactorial", "الجين المفرد مقابل متعدّد العوامل", "Single gene: one altered gene (CF, sickle cell, haemophilia). Multifactorial: many genes + environment (cleft lip/palate, heart disease, diabetes).", "الجين المفرد: جين واحد متغيّر (التليّف الكيسي، المنجلي، الهيموفيليا). متعدّد العوامل: جينات عدّة + بيئة (الشفة/الحنك المشقوق، القلب، السكري)."),
]
important = [
 IM("Define medical genetics and list what it includes.", "عرّف الوراثة الطبية واذكر ما تتضمّنه.", "Any application of genetics to medical practice; it includes studies of the inheritance of disease in families, mapping of disease genes to chromosome locations, and analysis of the molecular mechanisms by which genes cause disease.", "أي تطبيق للوراثة في الممارسة الطبية؛ وتتضمّن دراسة توارث الأمراض في العائلات، وتحديد مواقع جينات الأمراض على الكروموسومات، وتحليل الآليات الجزيئية التي تسبّب بها الجينات المرض."),
 IM("List the types of genetic disease with an example of each.", "عدّد أنواع الأمراض الوراثية مع مثال لكل منها.", "Chromosomal (Down, Turner); single gene/mendelian (cystic fibrosis, sickle cell disease, haemophilia); multifactorial (cleft lip/palate, heart disease, diabetes); mitochondrial (alterations of the mitochondrial chromosome).", "كروموسومي (داون، تيرنر)؛ جين مفرد/مندلي (التليّف الكيسي، المنجلي، الهيموفيليا)؛ متعدّد العوامل (الشفة/الحنك المشقوق، القلب، السكري)؛ مايتوكوندري (تغيّرات كروموسوم المايتوكوندريا)."),
 IM("Classify chromosomes according to the number of centromeres.", "صنّف الكروموسومات بحسب عدد السنتروميرات.", "No centromere (acentric; written acrocentric in the sheet) — not in human; monocentric (one, in human); dicentric (two); polycentric (more than two).", "بلا سنترومير (acentric؛ مكتوب acrocentric في الملزمة) — لا يوجد في الإنسان؛ أحادي (واحد، في الإنسان)؛ ثنائي (اثنان)؛ متعدّد (أكثر من اثنين)."),
 IM("Classify chromosomes according to the location of the centromere.", "صنّف الكروموسومات بحسب موقع السنترومير.", "Telocentric: at one end (mouse, not human); acrocentric: near one end (sub-terminal); submetacentric: in the upper arm (off centre); metacentric: in the middle.", "طرفي: في أحد الطرفين (الفأر لا الإنسان)؛ قريب الطرف: قرب أحد الطرفين؛ تحت الوسطي: في الذراع العلوي (بعيد عن المركز)؛ وسطي: في المنتصف."),
 IM("Give the groups A–G of human chromosomes.", "اذكر مجموعات الكروموسومات البشرية A–G.", "A: 1–3 longest metacentric; B: 4–5 long submetacentric; C: 6–12 + X long submetacentric; D: 13–15 short acrocentric; E: 16–18 short submetacentric; F: 19–20 short metacentric; G: 21, 22, Y shortest acrocentric.", "A: 1–3 الأطول ووسطية؛ B: 4–5 طويلة تحت وسطية؛ C: 6–12 + X طويلة تحت وسطية؛ D: 13–15 قصيرة قريبة الطرف؛ E: 16–18 قصيرة تحت وسطية؛ F: 19–20 قصيرة وسطية؛ G: 21، 22، Y الأقصر وقريبة الطرف."),
 IM("Compare somatic cells and gametes in chromosome number.", "قارن بين الخلايا الجسمية والأمشاج في عدد الكروموسومات.", "Somatic cells are diploid (22 pairs of autosomes + 1 pair of sex chromosomes = 46), kept by mitosis; gametes are haploid (23), kept through meiosis.", "الخلايا الجسمية ثنائية (22 زوجًا جسميًا + زوج جنسي = 46) ويُحافَظ عليها بالخيطي؛ والأمشاج أحادية (23) ويُحافَظ عليها بالاختزالي."),
]
meta = dict(GL, unit_en="Lab 3", unit_ar="العملي 3", unit_no="3", title_en="Medical genetics", title_ar="الوراثة الطبية")
save("genetics-lab3-medical-genetics", meta, blocks, mcq, tf, traps, important)

```
