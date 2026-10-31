---
source: BIOS-Obsidian/tools/scripts/lb2/gl2.py
handouts: [genetics-lab2-meiosis]
saved: 2026-10-31
tags: [bios, code]
---
# lb2/gl2.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#genetics-lab2-meiosis|genetics-lab2-meiosis]]

```python
import sys; sys.path.insert(0, "/tmp/claude-0/-home-user--/8f878068-bae9-502b-96f7-788f221c7cb0/scratchpad/imm456")
from ci import *            # c helpers + B INSHORT TERMS balance save(split.fix)

GL = dict(subject_en="Human Genetics", subject_ar="الوراثة البشرية", short_ar="وراثة", unit_label="LAB",
          kind="Laboratories — عملي", stage="The third stage — الثالثة", instructor="م.م. نور م. فاضل")
BN = lambda en, ar: N(en, ar, label=["BIOS note", "ملاحظة BIOS"])

blocks = [
 SEC("Meiosis", "الانقسام الاختزالي"),
 C("Meiosis is the division of a **germ cell (diploid)** involving **two fissions of the nucleus (Meiosis I and Meiosis II)**. and giving rise to **four gametes (haploid sex cells)**, each possessing **half the number of chromosomes** of the original cell.",
   "الانقسام الاختزالي هو انقسام **خلية جرثومية (ثنائية المجموعة)** يتضمّن **انشطارين للنواة (الاختزالي الأول والاختزالي الثاني)**، وينتج عنه **أربعة أمشاج (خلايا جنسية أحادية المجموعة)**، يحمل كل منها **نصف عدد كروموسومات** الخلية الأصلية."),
 L(["Meiosis Is a **Special Type of Cell Division** That Occurs in **Sexually Reproducing Organisms** .",
    "Meiosis of **diploid cells** produces **haploid daughter cells**, which may function as **gametes**.",
    "Gametes undergo **fertilization**, **restoring the diploid number** of chromosomes in the **zygote**"],
   ["الانقسام الاختزالي **نوع خاص من الانقسام الخلوي** يحدث في **الكائنات التي تتكاثر جنسيًا**.",
    "ينتج الانقسام الاختزالي للخلايا **ثنائية المجموعة** **خلايا بنوية أحادية المجموعة** قد تعمل **أمشاجًا**.",
    "وتخضع الأمشاج لـ**الإخصاب** فـ**يُستعاد العدد الثنائي** للكروموسومات في **البيضة المخصّبة (الزايكوت)**"]),
 FLOW([("Diploid germ cell (2n)", "خلية جرثومية ثنائية (2n)"), ("Meiosis I + Meiosis II", "الاختزالي الأول + الثاني"), ("4 haploid gametes (n)", "4 أمشاج أحادية (n)"), ("Fertilization", "الإخصاب"), ("Diploid zygote (2n)", "زايكوت ثنائي (2n)")]),
 H2("The stages of meiosis", "مراحل الانقسام الاختزالي"),
 C("The stages of meiosis can be broken down into **two main stages**,", "يمكن تقسيم مراحل الانقسام الاختزالي إلى **مرحلتين رئيستين**،"),
 T([B("Main stage", "المرحلة الرئيسة"), B("Sub stages", "المراحل الفرعية")],
   [[B("**Meiosis I**", "**الاختزالي الأول**"), B("Prophase I, Metaphase I, Anaphase I and Telophase I", "التمهيدي I، والاستوائي I، والانفصالي I، والنهائي I")],
    [B("**Meiosis II**", "**الاختزالي الثاني**"), B("Prophase II, Metaphase II, Anaphase II and Telophase II", "التمهيدي II، والاستوائي II، والانفصالي II، والنهائي II")]],
   key_cols=[0], widths=[28, 72], style="summary", label_en="4 + 4 sub stages", label_ar="4 + 4 مراحل فرعية"),
 INSHORT([("Meiosis: **1 diploid cell → 4 haploid gametes**.", "الاختزالي: **خلية ثنائية واحدة ← 4 أمشاج أحادية**."),
          ("**Two** nuclear divisions (I and II), each with **4 sub stages**.", "انقسامان **اثنان** للنواة (I وII)، لكل منهما **4 مراحل فرعية**."),
          ("Fertilization brings back **2n** in the zygote.", "الإخصاب يعيد **2n** في الزايكوت.")]),

 SEC("Meiosis I — Prophase I", "الاختزالي الأول — التمهيدي I"),
 C("**Prophase I** - **most of the significant processes** of Meiosis occur during Prophase I", "**التمهيدي I**: تحدث **معظم العمليات المهمة** في الانقسام الاختزالي أثناء التمهيدي I"),
 L(["The **nuclear membrane** begins to dissolve", "The **centrioles** form by dividing and move toward the poles"],
   ["يبدأ **الغشاء النووي** بالذوبان", "تتكوّن **المريكزات** بالانقسام وتتحرّك نحو القطبين"]),
 T([B("Sub stage", "المرحلة الفرعية"), B("Event", "الحدث")],
   [[B("**Leptotene**", "**الطور القلادي (اللبتوتين)**"), B("chromosomes start to condense.", "تبدأ الكروموسومات بالتكثّف.")],
    [B("**Zygotene**", "**الطور التزاوجي (الزايكوتين)**"), B("homologous chromosomes become closely associated (synapsis) to form pairs of chromosomes (bivalents) consisting of four chromatids (tetrads).", "تتقارب الكروموسومات المتماثلة بشدّة (التشابك) لتكوّن أزواجًا (ثنائيات) تتكوّن من أربعة كروماتيدات (رباعيات).")],
    [B("**Pachytene**", "**الطور الضام (الباكيتين)**"), B("crossing over between pairs of homologous chromosomes to form chiasmata (sing. chiasma).", "العبور بين أزواج الكروموسومات المتماثلة لتكوين التصالبات (المفرد: تصالب).")],
    [B("**Diplotene**", "**الطور الانفراجي (الدبلوتين)**"), B("homologous chromosomes start to separate but remain attached by chiasmata.", "تبدأ الكروموسومات المتماثلة بالانفصال لكنها تبقى مرتبطة بالتصالبات.")],
    [B("**Diakinesis**", "**الطور التشتّتي (الدايكاينيسس)**"), B("homologous chromosomes continue to separate, and chiasmata move to the ends of the chromosomes .", "يستمر انفصال الكروموسومات المتماثلة، وتتحرّك التصالبات إلى نهايات الكروموسومات.")]],
   key_cols=[0], widths=[30, 70], style="summary", label_en="5 sub stages of prophase I", label_ar="5 مراحل للتمهيدي I"),
 FLOW([("Leptotene: condense", "اللبتوتين: تكثّف"), ("Zygotene: synapsis", "الزايكوتين: تشابك"), ("Pachytene: crossing over", "الباكيتين: عبور"), ("Diplotene: separate", "الدبلوتين: انفصال"), ("Diakinesis: chiasmata to ends", "الدايكاينيسس: التصالبات للنهايات")]),
 H2("Definitions", "تعريفات"),
 C("**synapsis:** the process, Which the replicated homologous pair of chromosomes comes together In prophase I of meiosis.",
   "**التشابك:** العملية التي يجتمع فيها زوج الكروموسومات المتماثلة المتضاعفة في التمهيدي I من الانقسام الاختزالي."),
 C("**crossing over** : The **reciprocal exchange of genetic material** between **non sister chromatids** during synapsis in meiosis I. the resultant chromosomes are **neither entirely maternal nor entirely paternal**, but contain genes from both parents.",
   "**العبور:** **التبادل المتقابل للمادة الوراثية** بين **الكروماتيدات غير الشقيقة** أثناء التشابك في الاختزالي الأول، فتكون الكروموسومات الناتجة **لا أمّية كليًا ولا أبوية كليًا**، بل تحمل جينات من الأبوين."),
 F("crossing-over.png", "Crossing over during meiosis: non-sister chromatids exchange segments (X, Y, Z / x, y, z)", "العبور أثناء الانقسام الاختزالي: تتبادل الكروماتيدات غير الشقيقة قطعًا (X وY وZ / x وy وz)", h="58mm"),
 H2("The results of Synapsis and crossing over that occur only in meiosis", "نتائج التشابك والعبور التي تحدث في الانقسام الاختزالي فقط"),
 R("Genetic material from the homologous chromosomes is **randomly swapped**", "تُتبادل المادة الوراثية بين الكروموسومات المتماثلة **عشوائيًا**"),
 R("This creates **four unique chromatids**", "وهذا يكوّن **أربعة كروماتيدات فريدة**"),
 R("Since each chromatid is unique, the overall **genetic diversity of the gametes is greatly increased**.", "وبما أن كل كروماتيد فريد، **يزداد التنوّع الوراثي للأمشاج** كثيرًا."),
 INSHORT([("Prophase I = **most important** phase; 5 sub stages: **L-Z-P-D-D**.", "التمهيدي I = **أهم** طور؛ وله 5 مراحل: **L-Z-P-D-D**."),
          ("**Synapsis** (zygotene) → bivalents / **tetrads**.", "**التشابك** (الزايكوتين) ← ثنائيات / **رباعيات**."),
          ("**Crossing over** (pachytene) between **non-sister** chromatids → **chiasmata**.", "**العبور** (الباكيتين) بين كروماتيدات **غير شقيقة** ← **تصالبات**."),
          ("Result: 4 unique chromatids → **genetic diversity ↑**.", "النتيجة: 4 كروماتيدات فريدة ← **↑ التنوّع الوراثي**.")]),

 SEC("Meiosis I — Metaphase I to Telophase I", "الاختزالي الأول — من الاستوائي I إلى النهائي I"),
 H2("Metaphase I", "الاستوائي I"),
 L(["**Microtubules** grow from the centrioles and attach to the centromeres", "The **tetrads line up** along the cell equator ."],
   ["تنمو **الأنيبيبات الدقيقة** من المريكزات وترتبط بالسنتروميرات", "**تصطفّ الرباعيات** على طول خط استواء الخلية."]),
 H2("Anaphase I", "الانفصالي I"),
 L(["The centromeres break and **homologous chromosomes separate** (note that the **sister chromatids are still attached**)", "**Cytokinesis begins** ."],
   ["تنكسر السنتروميرات و**تنفصل الكروموسومات المتماثلة** (لاحظ أن **الكروماتيدات الشقيقة ما زالت مرتبطة**)", "**يبدأ انقسام السايتوبلازم**."]),
 H2("Telophase I", "النهائي I"),
 L(["The chromosomes **may decondense** (depends on species)", "Cytokinesis reaches completion, creating **two haploid daughter cells**."],
   ["**قد تنفكّ** الكروموسومات (بحسب النوع)", "يكتمل انقسام السايتوبلازم مكوّنًا **خليتين بنويتين أحاديتي المجموعة**."]),
 INSHORT([("Metaphase I: **tetrads** on the equator.", "الاستوائي I: **الرباعيات** على خط الاستواء."),
          ("Anaphase I: **homologues** separate; sister chromatids **stay together**.", "الانفصالي I: تنفصل **المتماثلات**؛ والكروماتيدات الشقيقة **تبقى معًا**."),
          ("Telophase I: **2 haploid cells**.", "النهائي I: **خليتان أحاديتان**.")]),

 SEC("Meiosis II", "الاختزالي الثاني"),
 H2("Prophase II", "التمهيدي II"),
 L(["**Centrioles** form and move toward the poles", "The **nuclear membrane dissolves**."], ["تتكوّن **المريكزات** وتتحرّك نحو القطبين", "**يذوب الغشاء النووي**."]),
 H2("Metaphase II", "الاستوائي II"),
 L(["Microtubules grow from the centrioles and attach to the centromeres", "The **sister chromatids line up** along the cell Equator."],
   ["تنمو الأنيبيبات الدقيقة من المريكزات وترتبط بالسنتروميرات", "**تصطفّ الكروماتيدات الشقيقة** على طول خط استواء الخلية."]),
 H2("Anaphase II", "الانفصالي II"),
 L(["The centromeres break and **sister chromatids separate**", "**Cytokinesis begins** ."], ["تنكسر السنتروميرات و**تنفصل الكروماتيدات الشقيقة**", "**يبدأ انقسام السايتوبلازم**."]),
 H2("Telophase II", "النهائي II"),
 L(["The chromosomes may decondense (depends on species)", "Cytokinesis reaches completion creating **four haploid daughter cells** ."],
   ["قد تنفكّ الكروموسومات (بحسب النوع)", "يكتمل انقسام السايتوبلازم مكوّنًا **أربع خلايا بنوية أحادية المجموعة**."]),
 C("The events of Meiosis II are **analogous to those of a mitotic division**, although the **number of chromosomes involved has been halved**.",
   "أحداث الاختزالي الثاني **مشابهة لأحداث الانقسام الخيطي**، مع أن **عدد الكروموسومات المشاركة قد انخفض إلى النصف**."),
 F("meiosis-stages.png", "Meiosis I and meiosis II: from interphase to 4 haploid daughter cells", "الاختزالي الأول والثاني: من الطور البيني إلى 4 خلايا بنوية أحادية", h="110mm"),
 T([B("Label in the figure", "التسمية في الشكل"), B("Arabic", "بالعربي")],
   [["**Prophase I — Synapsis and crossing over occur.**", "التمهيدي I — يحدث التشابك والعبور."],
    ["**Tetrad (paired homologous chromosomes with two chromatids each)**", "رباعي (كروموسومان متماثلان مقترنان لكل منهما كروماتيدان)"],
    ["**Metaphase I — Tetrads line up on the metaphase plate.**", "الاستوائي I — تصطفّ الرباعيات على الصفيحة الاستوائية."],
    ["**Anaphase I — Homologous pairs separate.**", "الانفصالي I — تنفصل الأزواج المتماثلة."],
    ["**Metaphase II — Chromosomes line up on the metaphase plate.**", "الاستوائي II — تصطفّ الكروموسومات على الصفيحة الاستوائية."],
    ["**Anaphase II — Sister chromatids separate.**", "الانفصالي II — تنفصل الكروماتيدات الشقيقة."],
    ["**4 haploid daughter cells are formed, each having only one chromosome of each homologous pair.**", "تتكوّن 4 خلايا بنوية أحادية، لكل منها كروموسوم واحد فقط من كل زوج متماثل."]],
   key_cols=[0], ar_cols=[1], widths=[55, 45], label_en="Figure labels", label_ar="تسميات الشكل"),
 INSHORT([("Meiosis II = **like mitosis** but with **half** the chromosomes.", "الاختزالي الثاني = **مثل الخيطي** لكن بـ**نصف** الكروموسومات."),
          ("Anaphase II: **sister chromatids** separate.", "الانفصالي II: تنفصل **الكروماتيدات الشقيقة**."),
          ("End: **4 haploid cells**.", "النهاية: **4 خلايا أحادية**.")]),

 SEC("Meiosis I vs Meiosis II", "الاختزالي الأول مقابل الثاني"),
 T([B("Compare", "مقارنة"), B("Meiosis I", "الاختزالي الأول"), B("Meiosis II", "الاختزالي الثاني")],
   [[B("**Metaphase: what lines up?**", "**الاستوائي: ماذا يصطفّ؟**"), B("Tetrads", "الرباعيات"), B("Sister chromatids (chromosomes)", "الكروماتيدات الشقيقة (الكروموسومات)")],
    [B("**Anaphase: what separates?**", "**الانفصالي: ماذا ينفصل؟**"), B("Homologous chromosomes", "الكروموسومات المتماثلة"), B("Sister chromatids", "الكروماتيدات الشقيقة")],
    [B("**Synapsis and crossing over**", "**التشابك والعبور**"), B("Yes (prophase I)", "نعم (التمهيدي I)"), B("No", "لا")],
    [B("**Result**", "**الناتج**"), B("2 haploid cells", "خليتان أحاديتان"), B("4 haploid cells", "4 خلايا أحادية")]],
   key_cols=[0], widths=[34, 33, 33], style="summary", label_en="I vs II", label_ar="I مقابل II"),
 BN("This comparison table is put together by BIOS from the lab.", "جدول المقارنة هذا جمعته BIOS من المحاضرة."),
] + TERMS([
 ("Meiosis", "الانقسام الاختزالي / الانقسام المنصّف"),
 ("Germ cell", "خلية جرثومية / خلية جنسية أولية"),
 ("Gamete", "مشيج / كميت / خلية جنسية"),
 ("Fertilization", "الإخصاب / التلقيح"),
 ("Zygote", "الزايكوت / البيضة المخصّبة / اللاقحة"),
 ("Leptotene", "اللبتوتين / الطور القلادي / الخيطي الرفيع"),
 ("Zygotene", "الزايكوتين / الطور التزاوجي"),
 ("Pachytene", "الباكيتين / الطور الضام / الثخين"),
 ("Diplotene", "الدبلوتين / الطور الانفراجي"),
 ("Diakinesis", "الدايكاينيسس / الطور التشتّتي"),
 ("Synapsis", "التشابك / الاقتران"),
 ("Bivalent / Tetrad", "ثنائي (زوج) / رباعي"),
 ("Crossing over", "العبور / التصالب الوراثي / تبادل القطع"),
 ("Chiasma (pl. chiasmata)", "تصالب / نقطة التصالب (تصالبات)"),
 ("Non-sister chromatids", "كروماتيدات غير شقيقة"),
 ("Centrioles", "المريكزات / الجسيمات المركزية"),
 ("Genetic diversity", "التنوّع الوراثي / التباين الوراثي"),
])

O = P
mcq = [
 {"topic_en": "Definition and stages", "topic_ar": "التعريف والمراحل"},
 Q("Meiosis gives rise to:", "ينتج عن الانقسام الاختزالي:", O(("Two diploid cells", "خليتان ثنائيتان"), ("Four haploid gametes", "أربعة أمشاج أحادية"), ("One zygote", "زايكوت واحد"), ("Four diploid cells", "أربع خلايا ثنائية")), "b"),
 Q("Meiosis occurs in:", "يحدث الانقسام الاختزالي في:", O(("Sexually reproducing organisms", "الكائنات التي تتكاثر جنسيًا"), ("Bacteria only", "البكتيريا فقط"), ("All somatic cells", "كل الخلايا الجسمية"), ("Red blood cells", "الكريات الحمر")), "a"),
 Q("The diploid number is restored in the zygote by:", "يُستعاد العدد الثنائي في الزايكوت بواسطة:", O(("Mitosis", "الانقسام الخيطي"), ("Crossing over", "العبور"), ("Fertilization", "الإخصاب"), ("Synapsis", "التشابك")), "c"),
 Q("Meiosis involves how many nuclear fissions?", "كم انشطارًا نوويًا يتضمّن الانقسام الاختزالي؟", O(("One", "واحد"), ("Three", "ثلاثة"), ("Four", "أربعة"), ("Two", "اثنان")), "d"),
 {"topic_en": "Prophase I", "topic_ar": "التمهيدي I"},
 Q("Most of the significant processes of meiosis occur in:", "تحدث معظم العمليات المهمة في الاختزالي في:", O(("Prophase I", "التمهيدي I"), ("Metaphase II", "الاستوائي II"), ("Anaphase I", "الانفصالي I"), ("Telophase II", "النهائي II")), "a"),
 Q("Chromosomes start to condense in:", "تبدأ الكروموسومات بالتكثّف في:", O(("Zygotene", "الزايكوتين"), ("Leptotene", "اللبتوتين"), ("Diplotene", "الدبلوتين"), ("Diakinesis", "الدايكاينيسس")), "b"),
 Q("Synapsis forming bivalents (tetrads) occurs in:", "يحدث التشابك المكوّن للثنائيات (الرباعيات) في:", O(("Leptotene", "اللبتوتين"), ("Pachytene", "الباكيتين"), ("Zygotene", "الزايكوتين"), ("Diakinesis", "الدايكاينيسس")), "c"),
 Q("Crossing over to form chiasmata occurs in:", "يحدث العبور المكوّن للتصالبات في:", O(("Diplotene", "الدبلوتين"), ("Leptotene", "اللبتوتين"), ("Zygotene", "الزايكوتين"), ("Pachytene", "الباكيتين")), "d"),
 Q("Homologous chromosomes start to separate but remain attached by chiasmata in:", "تبدأ المتماثلات بالانفصال وتبقى مرتبطة بالتصالبات في:", O(("Diplotene", "الدبلوتين"), ("Pachytene", "الباكيتين"), ("Leptotene", "اللبتوتين"), ("Metaphase I", "الاستوائي I")), "a"),
 Q("Chiasmata move to the ends of the chromosomes in:", "تتحرّك التصالبات إلى نهايات الكروموسومات في:", O(("Zygotene", "الزايكوتين"), ("Diakinesis", "الدايكاينيسس"), ("Leptotene", "اللبتوتين"), ("Anaphase II", "الانفصالي II")), "b"),
 Q("A tetrad consists of:", "يتكوّن الرباعي من:", O(("Two chromatids", "كروماتيدين"), ("Eight chromatids", "ثمانية كروماتيدات"), ("Four chromatids", "أربعة كروماتيدات"), ("One chromosome", "كروموسوم واحد")), "c"),
 Q("Crossing over is an exchange of genetic material between:", "العبور تبادل للمادة الوراثية بين:", O(("Sister chromatids", "الكروماتيدات الشقيقة"), ("Two gametes", "مشيجين"), ("Mitochondria", "المايتوكوندريا"), ("Non sister chromatids", "الكروماتيدات غير الشقيقة")), "d"),
 Q("After crossing over, the resultant chromosomes are:", "بعد العبور تكون الكروموسومات الناتجة:", O(("Neither entirely maternal nor entirely paternal", "لا أمّية كليًا ولا أبوية كليًا"), ("Entirely maternal", "أمّية كليًا"), ("Entirely paternal", "أبوية كليًا"), ("Identical to the parent cell", "مطابقة للخلية الأم")), "a"),
 Q("The main result of synapsis and crossing over is:", "النتيجة الأساسية للتشابك والعبور:", O(("Fewer gametes", "أمشاج أقل"), ("Increased genetic diversity of gametes", "زيادة التنوّع الوراثي للأمشاج"), ("Diploid gametes", "أمشاج ثنائية"), ("No change", "لا تغيّر")), "b"),
 {"topic_en": "Meiosis I and II", "topic_ar": "الاختزالي الأول والثاني"},
 Q("In metaphase I, the structures that line up on the equator are:", "في الاستوائي I تصطفّ على خط الاستواء:", O(("Single chromatids", "كروماتيدات مفردة"), ("Sister chromatids", "كروماتيدات شقيقة"), ("Tetrads", "الرباعيات"), ("Gametes", "الأمشاج")), "c"),
 Q("In anaphase I:", "في الانفصالي I:", O(("Sister chromatids separate", "تنفصل الكروماتيدات الشقيقة"), ("The nuclear membrane reforms", "يُعاد الغشاء النووي"), ("Synapsis occurs", "يحدث التشابك"), ("Homologous chromosomes separate; sister chromatids stay attached", "تنفصل المتماثلات وتبقى الكروماتيدات الشقيقة مرتبطة")), "d"),
 Q("Telophase I ends with:", "ينتهي النهائي I بـ:", O(("Two haploid daughter cells", "خليتين بنويتين أحاديتين"), ("Four haploid cells", "أربع خلايا أحادية"), ("One diploid cell", "خلية ثنائية واحدة"), ("A zygote", "زايكوت")), "a"),
 Q("In anaphase II:", "في الانفصالي II:", O(("Homologues separate", "تنفصل المتماثلات"), ("Sister chromatids separate", "تنفصل الكروماتيدات الشقيقة"), ("Crossing over occurs", "يحدث العبور"), ("Tetrads form", "تتكوّن الرباعيات")), "b"),
 Q("Meiosis II is analogous to:", "يشبه الاختزالي الثاني:", O(("Fertilization", "الإخصاب"), ("Interphase", "الطور البيني"), ("A mitotic division", "الانقسام الخيطي"), ("Prophase I", "التمهيدي I")), "c"),
 Q("Telophase II ends with:", "ينتهي النهائي II بـ:", O(("Two diploid cells", "خليتين ثنائيتين"), ("One gamete", "مشيج واحد"), ("Two haploid cells", "خليتين أحاديتين"), ("Four haploid daughter cells", "أربع خلايا بنوية أحادية")), "d"),
 {"topic_en": "Picture questions", "topic_ar": "أسئلة الصور"},
 Q("This figure shows:", "يوضّح هذا الشكل:", O(("Crossing over during meiosis", "العبور أثناء الانقسام الاختزالي"), ("Cytokinesis", "انقسام السايتوبلازم"), ("DNA replication", "تضاعف DNA"), ("Fertilization", "الإخصاب")), "a", img="assets/crossing-over.png", img_h="36mm"),
 Q("In this figure, the stage where homologous pairs separate is:", "في هذا الشكل، الطور الذي تنفصل فيه الأزواج المتماثلة:", O(("Anaphase II", "الانفصالي II"), ("Anaphase I", "الانفصالي I"), ("Metaphase II", "الاستوائي II"), ("Telophase II", "النهائي II")), "b", img="assets/meiosis-stages.png", img_h="60mm"),
]
mcq = balance(mcq, 14)
tf = [
 TF("Meiosis is the division of a diploid germ cell.", "الانقسام الاختزالي انقسام لخلية جرثومية ثنائية.", "T"),
 TF("Each gamete has the same number of chromosomes as the original cell.", "يحمل كل مشيج عدد كروموسومات الخلية الأصلية نفسه.", "F"),
 TF("Meiosis I and meiosis II each have four sub stages.", "لكل من الاختزالي الأول والثاني أربع مراحل فرعية.", "T"),
 TF("The centrioles move toward the poles in prophase I.", "تتحرّك المريكزات نحو القطبين في التمهيدي I.", "T"),
 TF("Crossing over occurs in zygotene.", "يحدث العبور في الزايكوتين.", "F"),
 TF("Synapsis and crossing over occur only in meiosis.", "يحدث التشابك والعبور في الانقسام الاختزالي فقط.", "T"),
 TF("Sister chromatids separate in anaphase I.", "تنفصل الكروماتيدات الشقيقة في الانفصالي I.", "F"),
 TF("Cytokinesis begins in anaphase.", "يبدأ انقسام السايتوبلازم في الطور الانفصالي.", "T"),
 TF("Chromosome decondensation in telophase depends on species.", "يعتمد انفكاك الكروموسومات في النهائي على النوع.", "T"),
 TF("Meiosis II involves the full diploid number of chromosomes.", "يتضمّن الاختزالي الثاني العدد الثنائي الكامل للكروموسومات.", "F"),
]
traps = [
 TR("Anaphase I vs anaphase II", "الانفصالي I مقابل الانفصالي II", "Anaphase I: homologous chromosomes separate (sister chromatids still attached). Anaphase II: sister chromatids separate.", "الانفصالي I: تنفصل المتماثلات (والكروماتيدات الشقيقة ما زالت مرتبطة). الانفصالي II: تنفصل الكروماتيدات الشقيقة."),
 TR("Metaphase I vs metaphase II", "الاستوائي I مقابل الاستوائي II", "Metaphase I: tetrads line up. Metaphase II: sister chromatids (single chromosomes) line up.", "الاستوائي I: تصطفّ الرباعيات. الاستوائي II: تصطفّ الكروماتيدات الشقيقة (كروموسومات مفردة)."),
 TR("Zygotene vs pachytene", "الزايكوتين مقابل الباكيتين", "Zygotene = synapsis (bivalents/tetrads). Pachytene = crossing over (chiasmata).", "الزايكوتين = التشابك (ثنائيات/رباعيات). الباكيتين = العبور (تصالبات)."),
 TR("Non-sister, not sister", "غير الشقيقة وليس الشقيقة", "Crossing over is between NON-sister chromatids of homologous chromosomes.", "العبور يكون بين الكروماتيدات غير الشقيقة للكروموسومات المتماثلة."),
 TR("Two cells or four?", "خليتان أم أربع؟", "Telophase I → 2 haploid cells; telophase II → 4 haploid cells.", "النهائي I ← خليتان أحاديتان؛ النهائي II ← 4 خلايا أحادية."),
]
important = [
 IM("Define meiosis and state its importance.", "عرّف الانقسام الاختزالي وبيّن أهميته.", "Division of a diploid germ cell with two nuclear fissions (meiosis I and II) giving four haploid gametes with half the chromosomes; it occurs in sexually reproducing organisms, and fertilization restores the diploid number in the zygote.", "انقسام خلية جرثومية ثنائية بانشطارين نوويين (I وII) ينتج أربعة أمشاج أحادية بنصف الكروموسومات؛ يحدث في الكائنات التي تتكاثر جنسيًا، ويعيد الإخصاب العدد الثنائي في الزايكوت."),
 IM("List the sub stages of prophase I and the event of each.", "عدّد المراحل الفرعية للتمهيدي I وحدث كل منها.", "Leptotene: chromosomes condense; zygotene: synapsis forms bivalents (tetrads); pachytene: crossing over forms chiasmata; diplotene: homologues start to separate, held by chiasmata; diakinesis: separation continues, chiasmata move to the ends.", "اللبتوتين: تكثّف؛ الزايكوتين: تشابك يكوّن ثنائيات (رباعيات)؛ الباكيتين: عبور يكوّن تصالبات؛ الدبلوتين: تبدأ المتماثلات بالانفصال مع بقاء التصالبات؛ الدايكاينيسس: يستمر الانفصال وتتحرّك التصالبات للنهايات."),
 IM("Define synapsis and crossing over.", "عرّف التشابك والعبور.", "Synapsis: the replicated homologous pair comes together in prophase I. Crossing over: reciprocal exchange of genetic material between non-sister chromatids during synapsis, so chromosomes carry genes from both parents.", "التشابك: اجتماع زوج المتماثلات المتضاعفة في التمهيدي I. العبور: تبادل متقابل للمادة الوراثية بين الكروماتيدات غير الشقيقة أثناء التشابك، فتحمل الكروموسومات جينات من الأبوين."),
 IM("What are the results of synapsis and crossing over?", "ما نتائج التشابك والعبور؟", "Genetic material is randomly swapped, four unique chromatids are created, and the genetic diversity of the gametes is greatly increased.", "تُتبادل المادة الوراثية عشوائيًا، وتتكوّن أربعة كروماتيدات فريدة، ويزداد التنوّع الوراثي للأمشاج كثيرًا."),
 IM("Describe metaphase, anaphase and telophase of meiosis I.", "صف الاستوائي والانفصالي والنهائي في الاختزالي الأول.", "Metaphase I: microtubules attach to centromeres and tetrads line up on the equator. Anaphase I: homologues separate (sister chromatids attached) and cytokinesis begins. Telophase I: chromosomes may decondense and two haploid cells form.", "الاستوائي I: ترتبط الأنيبيبات بالسنتروميرات وتصطفّ الرباعيات. الانفصالي I: تنفصل المتماثلات (والشقيقة مرتبطة) ويبدأ انقسام السايتوبلازم. النهائي I: قد تنفكّ الكروموسومات وتتكوّن خليتان أحاديتان."),
 IM("Describe meiosis II and compare it with mitosis.", "صف الاختزالي الثاني وقارنه بالانقسام الخيطي.", "Prophase II: centrioles move to poles, nuclear membrane dissolves; metaphase II: sister chromatids line up; anaphase II: sister chromatids separate; telophase II: four haploid cells. It is like mitosis but with half the chromosomes.", "التمهيدي II: تتحرّك المريكزات ويذوب الغشاء؛ الاستوائي II: تصطفّ الكروماتيدات الشقيقة؛ الانفصالي II: تنفصل الشقيقة؛ النهائي II: أربع خلايا أحادية. وهو مثل الخيطي لكن بنصف الكروموسومات."),
]
meta = dict(GL, unit_en="Lab 2", unit_ar="العملي 2", unit_no="2", title_en="Meiosis", title_ar="الانقسام الاختزالي")
save("genetics-lab2-meiosis", meta, blocks, mcq, tf, traps, important)

```
