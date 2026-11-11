---
source: BIOS-Obsidian/tools/scripts/im5/q5.py
handouts: [immunology-lec5-mcq]
saved: 2026-11-11
tags: [bios, code]
---
# im5/q5.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#immunology-lec5-mcq|immunology-lec5-mcq]]

```python
import sys, json, os
sys.path.insert(0, "/tmp/claude-0/-home-user-kwmdkm/44452a28-19bf-5ce8-890a-f6919e775f0b/scratchpad/imm456")
from ci import *            # Q TF TR IM P balance
sys.path.insert(0, "/tmp/claude-0/-home-user-kwmdkm/44452a28-19bf-5ce8-890a-f6919e775f0b/scratchpad"); from bidi import ltr_all

# Immunology theory lecture 5 (stage 3) — Generation of antibody diversity. Source: Lec._5_antibodydiversity.ppt
# (26 slides; "Bilad Al Rafidain University · Immunology · Class 3rd · Lec. Dr. Ahmed D. A. · Lec : 5").
# QUESTIONS ONLY (user's choice 2026-11-08), answer under every question (answers_inline, user rule 2026-11-08).
# Figures cropped from the rendered slides (the slide pictures are low-resolution WMF). Slide-text quirks flagged in note_en:
# "105"/"1015"/"10-3"/"10-8" = superscripts lost (10⁵, 10¹⁵, 10⁻³, 10⁻⁸); slide 16 "is not," = is not precise.
O = P
FOLDER = "immunology-lec5-mcq"
NB = lambda q, en, ar: dict(q, note_en=en, note_ar=ar)

mcq = [
 {"topic_en": "Introduction and theories", "topic_ar": "المقدمة والنظريات"},
 NB(Q("The human genome contains fewer than about ___ genes:", "يحتوي الجينوم البشري أقلّ من نحو ___ جين:",
      O(("10⁵", "`10⁵`"), ("10¹⁵", "`10¹⁵`"), ("10²", "`10²`"), ("10⁹", "`10⁹`")), "a"),
    "The slide prints \"105\" and \"1015\" — the superscripts were lost: 10⁵ genes and 10¹⁵ antibodies.",
    "الشريحة تكتب \"`105`\" و\"`1015`\" — ضاعت الأسس: `10⁵` جين و`10¹⁵` ضدّ."),
 Q("A human can make at least ___ different types of antibodies:", "يستطيع الإنسان صنع ___ نوع مختلف من الأضداد على الأقلّ:",
   O(("10³", "`10³`"), ("10¹⁵", "`10¹⁵`"), ("10⁵", "`10⁵`"), ("10⁸", "`10⁸`")), "b"),
 Q("The theory stating that the genome of germ cells contains a large repertoire of Ig genes is the:", "النظرية القائلة إن جينوم الخلايا الجنسية يحتوي ذخيرة كبيرة من جينات الغلوبيولين هي:",
   O(("Somatic variation theory", "نظرية التغاير الجسدي"), ("Clonal selection theory", "نظرية الانتقاء النسيلي"), ("Germ line theory", "نظرية الخط الجنسي (الجرثومي)"), ("Side-chain theory", "نظرية السلاسل الجانبية")), "c"),
 Q("The weakness of the germ line theory was that it:", "نقطة ضعف نظرية الخط الجنسي أنها:",
   O(("Denied the existence of antibodies", "أنكرت وجود الأضداد"), ("Needed mutations", "احتاجت الطفرات"), ("Was proved by Tonegawa", "أثبتها توناغاوا"), ("Could not explain the genetic mechanism of antibody diversity", "لم تفسّر الآلية الوراثية لتنوّع الأضداد")), "d"),
 Q("According to the somatic variation theory, a large number of specificities is generated from a small number of Ig genes by:", "حسب نظرية التغاير الجسدي يتولّد عدد كبير من النوعيات من عدد قليل من جينات الغلوبيولين بـ:",
   O(("Mutation or recombination", "الطفرة أو إعادة الاتحاد"), ("Translation errors", "أخطاء الترجمة"), ("Gene duplication in germ cells", "تضاعف الجينات في الخلايا الجنسية"), ("Viral infection", "العدوى الفيروسية")), "a"),
 Q("The scientist who showed that immunoglobulin genes rearrange is:", "العالم الذي أثبت أن جينات الغلوبيولين المناعي تعيد ترتيبها هو:",
   O(("Pasteur", "باستور"), ("Tonegawa", "توناغاوا"), ("Jenner", "جينر"), ("Koch", "كوخ")), "b"),
 Q("How many means of antibody diversification have been identified in mice and humans?", "كم وسيلة لتنويع الأضداد حُدّدت في الفئران والإنسان؟",
   O(("Three", "ثلاث"), ("Five", "خمس"), ("Seven", "سبع"), ("Ten", "عشر")), "c"),
 {"topic_en": "Light and heavy chain genes", "topic_ar": "جينات السلاسل الخفيفة والثقيلة"},
 Q("In humans, the number of Vκ gene segments is:", "عدد قطع الجينات Vκ في الإنسان:", O(("51", "51"), ("31", "31"), ("27", "27"), ("40", "40")), "d"),
 Q("In humans, the κ light chain has how many Jκ and Cκ segments?", "كم قطعة Jκ وCκ للسلسلة الخفيفة κ في الإنسان؟",
   O(("5 Jκ and 1 Cκ", "5 Jκ و1 Cκ"), ("4 Jκ and 7 Cκ", "4 Jκ و7 Cκ"), ("6 Jκ and 1 Cκ", "6 Jκ و1 Cκ"), ("27 Jκ and 5 Cκ", "27 Jκ و5 Cκ")), "a"),
 Q("The λ light chain genes are on chromosome:", "جينات السلسلة الخفيفة λ على الكروموسوم:", O(("2", "2"), ("22", "22"), ("14", "14"), ("6", "6")), "b"),
 Q("The number of Cλ gene segments in humans is:", "عدد قطع الجينات Cλ في الإنسان:", O(("1", "1"), ("4", "4"), ("7", "7"), ("31", "31")), "c"),
 Q("The human heavy chain locus (chromosome 14) has:", "موقع السلسلة الثقيلة البشري (الكروموسوم 14) فيه:",
   O(("40 V and 5 J", "40 V و5 J"), ("31 V, 4 J and 7 C", "31 V و4 J و7 C"), ("51 V only", "51 V فقط"), ("51 VH, 27 DH, 6 JH and a series of C segments", "51 VH و27 DH و6 JH وسلسلة من قطع C")), "d"),
 Q("The variable region of the light chain is coded by:", "تُشفَّر المنطقة المتغيّرة للسلسلة الخفيفة بـ:",
   O(("V and J genes", "جينات V وJ"), ("V, D and J genes", "جينات V وD وJ"), ("C gene only", "جين C فقط"), ("D gene only", "جين D فقط")), "a"),
 Q("The V, J and C light chain genes are:", "جينات V وJ وC للسلسلة الخفيفة:",
   O(("On different chromosomes", "على كروموسومات مختلفة"), ("On the same chromosome but distantly located from each other", "على الكروموسوم نفسه لكنها متباعدة"), ("Adjacent in germ line DNA", "متجاورة في دنا الخط الجنسي"), ("In mitochondria", "في المايتوكوندريا")), "b"),
 Q("V-J joining of the κ chain happens during:", "يحدث ربط V-J للسلسلة κ أثناء:",
   O(("Plasma cell secretion", "إفراز خلية البلازما"), ("Antigen presentation", "تقديم المستضد"), ("B cell maturation", "نضج الخلية البائية"), ("Class switching", "تبديل الصنف")), "c"),
 Q("Heavy chains are encoded by how many kinds of gene segments?", "تُشفَّر السلاسل الثقيلة بكم نوعًا من قطع الجينات؟", O(("2: V and C", "2: V وC"), ("3: V, J and C", "3: V وJ وC"), ("5", "5"), ("4: V, D, J and C", "4: V وD وJ وC")), "d"),
 Q("In heavy chain gene rearrangement the first joining is:", "في إعادة ترتيب جينات السلسلة الثقيلة يكون أول ربط:",
   O(("D-J joining", "ربط D-J"), ("V-D joining", "ربط V-D"), ("V-C joining", "ربط V-C"), ("J-C joining", "ربط J-C")), "a"),
 Q("After D-J joining, the next step in the heavy chain is:", "بعد ربط D-J تكون الخطوة التالية في السلسلة الثقيلة:",
   O(("Class switching", "تبديل الصنف"), ("Joining of a V gene to the D-J segment (V-D-J)", "ربط جين V بقطعة D-J (V-D-J)"), ("Somatic hypermutation", "الطفرة الجسدية المفرطة"), ("Allelic exclusion", "الإقصاء الأليلي")), "b"),
 {"topic_en": "Recombination and junctional diversity", "topic_ar": "إعادة الاتحاد وتنوّع نقاط الوصل"},
 Q("Recombination signal sequences (RSSs) contain a heptamer and a nonamer separated by a spacer of:", "تحتوي متسلسلات إشارة إعادة الاتحاد (RSS) سباعيًا وتساعيًا يفصلهما فاصل طوله:",
   O(("5 or 10 bp", "5 أو 10 أزواج"), ("100 bp", "100 زوج"), ("12 or 23 bp", "12 أو 23 زوجًا"), ("1 bp", "زوج واحد")), "c"),
 Q("In the recombination model, the RSSs are recognized and cut by:", "في نموذج إعادة الاتحاد تتعرّف على الـ RSS وتقطعها:",
   O(("TdT", "`TdT`"), ("DNA ligase only", "الليغاز فقط"), ("Reverse transcriptase", "المنتسخة العكسية"), ("RAG-1/2", "`RAG-1/2`")), "d"),
 NB(Q("Junctional diversity results from:", "ينتج تنوّع نقاط الوصل عن:",
      O(("Imprecise joining of the V and J (or V, D and J) segments", "الربط غير الدقيق لقطع V وJ (أو V وD وJ)"), ("Class switching", "تبديل الصنف"), ("Allelic exclusion", "الإقصاء الأليلي"), ("Light-chain pairing", "اقتران السلاسل الخفيفة")), "a"),
    "Slide 16 reads \"…are fused together is not,\" — a word is missing: the joining position is **not precise**.",
    "الشريحة 16 تقول \"…are fused together is not,\" — كلمة ناقصة: موقع الربط **غير دقيق**."),
 Q("In the junctional flexibility figure, rearrangements that create a stop codon are:", "في شكل مرونة الوصل، إعادات الترتيب التي تكوّن رامزة توقّف هي:",
   O(("Productive", "منتِجة"), ("Nonproductive", "غير منتِجة"), ("Allelic", "أليلية"), ("Switch", "تبديلية")), "b"),
 Q("P-nucleotides are added after:", "تُضاف نيوكليوتيدات P بعد:",
   O(("Translation", "الترجمة"), ("TdT activity", "نشاط TdT"), ("Cleavage of the hairpin at the coding joint", "قطع دبّوس الشعر عند وصلة الترميز"), ("Class switching", "تبديل الصنف")), "c"),
 Q("P-nucleotides form:", "تكوّن نيوكليوتيدات P:",
   O(("A random sequence", "متسلسلة عشوائية"), ("A stop codon always", "رامزة توقّف دائمًا"), ("RSS heptamers", "سباعيات RSS"), ("A palindromic sequence in the coding joint", "متسلسلة متناظرة (باليندرومية) في وصلة الترميز")), "d"),
 Q("The enzyme that adds N-nucleotides is:", "الإنزيم الذي يضيف نيوكليوتيدات N:",
   O(("Terminal deoxynucleotidyl transferase (TdT)", "الترانسفيريز الطرفي للديوكسي نيوكليوتيد (TdT)"), ("RAG-1", "`RAG-1`"), ("DNA polymerase III", "بوليميريز الدنا III"), ("Reverse transcriptase", "المنتسخة العكسية")), "a"),
 Q("Up to how many N-nucleotides can be added at each heavy-chain joint?", "حتى كم نيوكليوتيد N يمكن إضافته عند كل وصلة في السلسلة الثقيلة؟",
   O(("3", "3"), ("15", "15"), ("50", "50"), ("100", "100")), "b"),
 Q("A complete heavy chain variable region is encoded by:", "تُشفَّر المنطقة المتغيّرة الكاملة للسلسلة الثقيلة بالوحدة:",
   O(("VJ", "`VJ`"), ("VDJC", "`VDJC`"), ("VHNDHNJH", "`VHNDHNJH`"), ("VC", "`VC`")), "c"),
 {"topic_en": "Allelic exclusion and somatic hypermutation", "topic_ar": "الإقصاء الأليلي والطفرة الجسدية المفرطة"},
 Q("Allelic exclusion means that a B cell expresses:", "الإقصاء الأليلي يعني أن الخلية البائية تعبّر عن:",
   O(("Both maternal and paternal heavy chains", "السلسلتين الثقيلتين الأمّية والأبوية"), ("Only λ chains", "سلاسل λ فقط"), ("No light chain", "لا سلسلة خفيفة"), ("Rearranged heavy and light chain genes from only one chromosome each", "جينات السلسلة الثقيلة والخفيفة المُعاد ترتيبها من كروموسوم واحد فقط لكل منهما")), "d"),
 Q("Allelic exclusion is essential because expression of both alleles would make the B cell:", "الإقصاء الأليلي ضروري لأن التعبير عن الأليلين يجعل الخلية البائية:",
   O(("Multi-specific", "متعدّدة النوعية"), ("Haploid", "أحادية المجموعة"), ("Unable to divide", "عاجزة عن الانقسام"), ("A T cell", "خلية تائية")), "a"),
 Q("In the Yancopoulos and Alt model, a productive μ heavy chain:", "في نموذج يانكوبولوس وألت، السلسلة الثقيلة μ المنتِجة:",
   O(("Causes cell death", "تسبّب موت الخلية"), ("Inhibits rearrangement of the second μ allele and induces κ rearrangement", "تثبّط إعادة ترتيب أليل μ الثاني وتحفّز إعادة ترتيب κ"), ("Induces λ rearrangement first", "تحفّز إعادة ترتيب λ أولًا"), ("Has no effect", "لا تأثير لها")), "b"),
 Q("In the allelic exclusion model, λ rearrangement occurs when:", "في نموذج الإقصاء الأليلي تحدث إعادة ترتيب λ عندما:",
   O(("μ is nonproductive", "تكون μ غير منتِجة"), ("The cell is a plasma cell", "تكون الخلية خلية بلازما"), ("Both κ alleles are nonproductive", "يكون أليلا κ غير منتِجين"), ("IgG is made", "يُصنع IgG")), "c"),
 NB(Q("Somatic hypermutation occurs at a frequency of about:", "تحدث الطفرة الجسدية المفرطة بتكرار نحو:",
      O(("10⁻⁸ per bp per generation", "`10⁻⁸` لكل زوج قاعدي لكل جيل"), ("10⁻¹ per bp", "`10⁻¹` لكل زوج"), ("1 per gene", "1 لكل جين"), ("10⁻³ per bp per generation", "`10⁻³` لكل زوج قاعدي لكل جيل")), "d"),
    "The slide prints \"10-3\" and \"10-8\" — these are 10⁻³ and 10⁻⁸.", "الشريحة تكتب \"`10-3`\" و\"`10-8`\" — والمقصود `10⁻³` و`10⁻⁸`."),
 Q("Somatic hypermutation is higher than the spontaneous mutation rate by at least:", "الطفرة الجسدية المفرطة أعلى من معدّل الطفرة التلقائية بما لا يقلّ عن:",
   O(("A hundred thousand fold", "مئة ألف ضعف"), ("Two fold", "ضعفين"), ("Ten fold", "عشرة أضعاف"), ("A hundred fold", "مئة ضعف")), "a"),
 Q("Somatic hypermutation generates additional diversity in:", "تولّد الطفرة الجسدية المفرطة تنوّعًا إضافيًا في:",
   O(("The constant region genes", "جينات المنطقة الثابتة"), ("Rearranged variable region gene units", "وحدات جينات المنطقة المتغيّرة المُعاد ترتيبها"), ("MHC genes", "جينات MHC"), ("Germ cells", "الخلايا الجنسية")), "b"),
 {"topic_en": "Class switching", "topic_ar": "تبديل الصنف"},
 Q("VJ and VDJ rearrangements occur:", "تحدث إعادات ترتيب VJ وVDJ:",
   O(("Only after antigen stimulation", "بعد التحفيز بالمستضد فقط"), ("In plasma cells", "في خلايا البلازما"), ("In the absence of antigen in the early stages of B cell maturation", "في غياب المستضد في المراحل المبكّرة لنضج الخلية البائية"), ("During class switching", "أثناء تبديل الصنف")), "c"),
 Q("During class switching the B cell:", "أثناء تبديل الصنف الخلية البائية:",
   O(("Changes its antigen specificity", "تغيّر نوعيتها للمستضد"), ("Stops making antibodies", "تتوقّف عن صنع الأضداد"), ("Changes its light chain", "تغيّر سلسلتها الخفيفة"), ("Makes a different class of antibody with the same antigenic specificity", "تصنع صنفًا مختلفًا من الأضداد بنفس النوعية المستضدية")), "d"),
 Q("Class switching depends on:", "يعتمد تبديل الصنف على:",
   O(("Antigenic stimulation and cytokines released by T cells", "التحفيز بالمستضد والسيتوكينات التي تحرّرها الخلايا التائية"), ("Allelic exclusion", "الإقصاء الأليلي"), ("TdT", "`TdT`"), ("The germ line theory", "نظرية الخط الجنسي")), "a"),
 Q("In the presence of interferon-gamma, the B cell switches to:", "بوجود الإنترفيرون-غاما تتحوّل الخلية البائية إلى:",
   O(("IgE", "`IgE`"), ("IgG2", "`IgG2`"), ("IgA", "`IgA`"), ("IgM", "`IgM`")), "b"),
 Q("In the presence of IL-4, the B cell switches to:", "بوجود IL-4 تتحوّل الخلية البائية إلى:",
   O(("IgM or IgD", "`IgM` أو `IgD`"), ("IgG2 only", "`IgG2` فقط"), ("IgG4 or IgE", "`IgG4` أو `IgE`"), ("IgA only", "`IgA` فقط")), "c"),
 Q("In the class switching figure, the DNA between two switch regions is:", "في شكل تبديل الصنف، الدنا الواقع بين منطقتي تبديل:",
   O(("Translated", "يُترجَم"), ("Duplicated", "يتضاعف"), ("Moved to another chromosome", "ينتقل إلى كروموسوم آخر"), ("Looped out and deleted as a circle", "يلتفّ ويُحذف على شكل دائرة")), "d"),
 {"topic_en": "Picture questions", "topic_ar": "أسئلة الصور"},
 Q("Which of these is NOT one of the seven means of antibody diversification in this list?", "أيّ مما يلي ليس من وسائل تنويع الأضداد السبع في هذه القائمة؟",
   O(("Allelic exclusion", "الإقصاء الأليلي"), ("Somatic hypermutation", "الطفرة الجسدية المفرطة"), ("Junctional flexibility", "مرونة الوصل"), ("N-region nucleotide addition", "إضافة نيوكليوتيدات المنطقة N")), "a", img="assets/seven-means.png", img_h="72mm"),
 Q("From this table, the number of possible heavy-chain V-D-J combinations is:", "من هذا الجدول، عدد تراكيب V-D-J الممكنة للسلسلة الثقيلة:",
   O(("200", "200"), ("8262", "8262"), ("120", "120"), ("2.64 × 10⁶", "`2.64 × 10⁶`")), "b", img="assets/combinatorial-table.png", img_h="70mm"),
 Q("In this figure, the one-turn RSS has a spacer of:", "في هذا الشكل، الـ RSS أحادي اللفّة فيه فاصل طوله:",
   O(("23 bp", "23 زوجًا"), ("7 bp", "7 أزواج"), ("12 bp", "12 زوجًا"), ("9 bp", "9 أزواج")), "c", img="assets/rss.png", img_h="95mm"),
 Q("In this figure, the step that differs in N-nucleotide addition is:", "في هذا الشكل، الخطوة التي تختلف في إضافة نيوكليوتيدات N هي:",
   O(("Hairpin formation", "تكوّن دبّوس الشعر"), ("Cleavage of the hairpin", "قطع دبّوس الشعر"), ("Repair enzymes", "إنزيمات الإصلاح"), ("TdT adds N-nucleotides", "يضيف TdT نيوكليوتيدات N")), "d", img="assets/p-n-addition.png", img_h="95mm"),
 Q("This figure shows that each B cell expresses:", "يوضّح هذا الشكل أن كل خلية بائية تعبّر عن:",
   O(("One H chain and one light chain from one parent's chromosome each (allelic exclusion)", "سلسلة ثقيلة وسلسلة خفيفة واحدة من كروموسوم أحد الأبوين لكل منهما (الإقصاء الأليلي)"), ("Both maternal and paternal H chains", "السلسلتين الثقيلتين الأمّية والأبوية"), ("κ and λ together", "κ وλ معًا"), ("No receptors", "لا مستقبلات")), "a", img="assets/allelic-exclusion.png", img_h="95mm"),
 Q("This figure shows the rearrangement of the:", "يوضّح هذا الشكل إعادة ترتيب:",
   O(("Heavy chain (V-D-J)", "السلسلة الثقيلة (V-D-J)"), ("κ light chain (V-J joining)", "السلسلة الخفيفة κ (ربط V-J)"), ("Switch regions", "مناطق التبديل"), ("TCR genes", "جينات TCR")), "b", img="assets/light-chain-recombination.png", img_h="95mm"),
 Q("This figure illustrates:", "يوضّح هذا الشكل:",
   O(("Allelic exclusion", "الإقصاء الأليلي"), ("Junctional diversity", "تنوّع نقاط الوصل"), ("Class switching by DNA looping and recombination at switch regions", "تبديل الصنف بالتفاف الدنا وإعادة الاتحاد عند مناطق التبديل"), ("P-addition", "إضافة P")), "c", img="assets/class-switching.png", img_h="85mm"),
]
mcq = balance(mcq, 51)
tf = [
 TF("A human can make at least 10¹⁵ different antibodies although the genome has fewer than 10⁵ genes.", "يستطيع الإنسان صنع `10¹⁵` ضدًّا مختلفًا على الأقلّ رغم أن الجينوم فيه أقلّ من `10⁵` جين.", "T"),
 TF("Germ line proponents explained the genetic mechanism of antibody diversity.", "فسّر أنصار نظرية الخط الجنسي الآلية الوراثية لتنوّع الأضداد.", "F"),
 TF("The somatic variation theory says somatic cells contain a relatively small number of Ig genes.", "تقول نظرية التغاير الجسدي إن الخلايا الجسدية تحتوي عددًا قليلًا نسبيًا من جينات الغلوبيولين.", "T"),
 TF("The κ light chain genes are on chromosome 2.", "جينات السلسلة الخفيفة κ على الكروموسوم 2.", "T"),
 TF("There are 7 Cκ gene segments in humans.", "توجد 7 قطع جينات Cκ في الإنسان.", "F"),
 TF("Light chains contain a D gene segment.", "تحتوي السلاسل الخفيفة على قطعة جين D.", "F"),
 TF("In the heavy chain, V-D joining occurs before D-J joining.", "في السلسلة الثقيلة يحدث ربط V-D قبل ربط D-J.", "F"),
 TF("Imprecise DNA recombination at the junctions can change amino acids.", "قد يغيّر الربط غير الدقيق للدنا عند نقاط الوصل الأحماض الأمينية.", "T"),
 TF("N-nucleotides are added by RAG-1/2.", "يضيف RAG-1/2 نيوكليوتيدات N.", "F"),
 TF("Up to 15 N-nucleotides can be added to the DH-JH and VH-DHJH joints.", "يمكن إضافة حتى 15 نيوكليوتيد N إلى وصلتي DH-JH وVH-DHJH.", "T"),
 TF("B cells are haploid, so they express one allele only.", "الخلايا البائية أحادية المجموعة لذا تعبّر عن أليل واحد فقط.", "F"),
 TF("Somatic hypermutation occurs in rearranged variable region genes.", "تحدث الطفرة الجسدية المفرطة في جينات المنطقة المتغيّرة المُعاد ترتيبها.", "T"),
 TF("Spontaneous mutation rate is about 10⁻⁸ per bp per generation.", "معدّل الطفرة التلقائية نحو `10⁻⁸` لكل زوج قاعدي لكل جيل.", "T"),
 TF("Class switching changes the antigenic specificity of the antibody.", "يغيّر تبديل الصنف النوعية المستضدية للضدّ.", "F"),
 TF("A single B cell with a unique specificity can make antibodies of all classes.", "تستطيع خلية بائية واحدة ذات نوعية فريدة صنع أضداد من كل الأصناف.", "T"),
 TF("IL-4 induces a switch to IgG2.", "يحفّز IL-4 التحوّل إلى `IgG2`.", "F"),
]
traps = [
 TR("Germ line vs somatic variation", "الخط الجنسي مقابل التغاير الجسدي", "Germ line: a LARGE repertoire of Ig genes in germ cells (could not explain the mechanism). Somatic variation: a SMALL number of genes + mutation/recombination.",
    "الخط الجنسي: ذخيرة كبيرة من جينات الغلوبيولين في الخلايا الجنسية (لم تفسّر الآلية). والتغاير الجسدي: عدد قليل من الجينات + طفرة/إعادة اتحاد."),
 TR("Segment numbers", "أعداد القطع", "κ: 40 V, 5 J, 1 C (chr 2). λ: 31 V, 4 J, 7 C (chr 22). Heavy: 51 V, 27 D, 6 J (chr 14). (The combinatorial table uses 30 Vλ.)",
    "κ: 40 V و5 J و1 C (كروموسوم 2). وλ: 31 V و4 J و7 C (كروموسوم 22). والثقيلة: 51 V و27 D و6 J (كروموسوم 14). (جدول التراكيب يستعمل 30 Vλ.)"),
 TR("Order of heavy-chain joining", "ترتيب ربط السلسلة الثقيلة", "D-J first, then V to DJ → VDJ, then a C gene. Light chain: V-J then C.",
    "D-J أولًا، ثم V إلى DJ ← VDJ، ثم جين C. والسلسلة الخفيفة: V-J ثم C."),
 TR("P vs N nucleotides", "نيوكليوتيدات P مقابل N", "P-nucleotides: from asymmetric hairpin cleavage, filled by repair enzymes → palindromic. N-nucleotides: added randomly by TdT (up to 15), heavy chain joints.",
    "نيوكليوتيدات P: من القطع غير المتناظر لدبّوس الشعر وتملؤها إنزيمات الإصلاح ← متناظرة. ونيوكليوتيدات N: يضيفها TdT عشوائيًا (حتى 15)، في وصلات السلسلة الثقيلة."),
 TR("RAG vs TdT", "RAG مقابل TdT", "RAG-1/2 recognize and cut at the RSSs (12/23 bp spacers); TdT adds N-nucleotides.",
    "RAG-1/2 يتعرّفان على الـ RSS ويقطعان عندها (فاصل 12/23 زوجًا)؛ وTdT يضيف نيوكليوتيدات N."),
 TR("10⁻³ vs 10⁻⁸", "`10⁻³` مقابل `10⁻⁸`", "Somatic hypermutation 10⁻³ /bp/generation; spontaneous 10⁻⁸ — at least 100,000-fold higher.",
    "الطفرة الجسدية المفرطة `10⁻³`/زوج/جيل؛ والتلقائية `10⁻⁸` — أعلى بما لا يقلّ عن 100,000 ضعف."),
 TR("Which cytokine → which class?", "أيّ سيتوكين ← أيّ صنف؟", "IFN-γ → IgG2. IL-4 → IgG4 or IgE. Specificity stays the same.",
    "`IFN-γ` ← `IgG2`. و`IL-4` ← `IgG4` أو `IgE`. والنوعية تبقى نفسها."),
 TR("With or without antigen?", "بوجود المستضد أم بدونه؟", "VJ/VDJ rearrangement happens WITHOUT antigen (early B cell maturation); class switching NEEDS antigen and T-cell cytokines.",
    "إعادة ترتيب VJ/VDJ تحدث بدون مستضد (في النضج المبكّر للخلية البائية)؛ وتبديل الصنف يحتاج المستضد وسيتوكينات الخلايا التائية."),
]
important = [
 IM("Compare the germ line theory and the somatic variation theory.", "قارن بين نظرية الخط الجنسي ونظرية التغاير الجسدي.",
    "Germ line theory: all antibodies are coded by genes of germ line cells; the germ-cell genome contains a large repertoire of Ig genes — but it could not explain the genetic mechanism of diversity. Somatic variation theory: somatic cells contain a relatively small number of Ig genes from which a large number of specificities is generated by mutation or recombination.",
    "نظرية الخط الجنسي: كل الأضداد تشفّرها جينات خلايا الخط الجنسي؛ وجينوم الخلايا الجنسية يحتوي ذخيرة كبيرة من جينات الغلوبيولين — لكنها لم تفسّر الآلية الوراثية للتنوّع. ونظرية التغاير الجسدي: الخلايا الجسدية تحتوي عددًا قليلًا نسبيًا من جينات الغلوبيولين يتولّد منها عدد كبير من النوعيات بالطفرة أو إعادة الاتحاد."),
 IM("List the seven means of antibody diversification.", "عدّد الوسائل السبع لتنويع الأضداد.",
    "1) Multiple germ-line gene segments; 2) combinatorial V-(D)-J joining; 3) junctional flexibility; 4) P-region nucleotide addition; 5) N-region nucleotide addition; 6) somatic hypermutation; 7) combinatorial association of light and heavy chains.",
    "1) قطع جينات متعدّدة في الخط الجنسي؛ 2) الربط التوافقي V-(D)-J؛ 3) مرونة الوصل؛ 4) إضافة نيوكليوتيدات المنطقة P؛ 5) إضافة نيوكليوتيدات المنطقة N؛ 6) الطفرة الجسدية المفرطة؛ 7) الاقتران التوافقي للسلاسل الخفيفة والثقيلة."),
 IM("Describe the recombination of the κ light chain genes.", "صف إعادة اتحاد جينات السلسلة الخفيفة κ.",
    "V and J genes code for the variable region and C for the constant region; they are on the same chromosome (chr 2) but far apart. During B cell maturation any one of 40 Vκ joins any one of 5 Jκ (V-J joining), then Cκ is joined to form a V-J-C gene, which is transcribed and translated into a functional κ light chain.",
    "تشفّر جينات V وJ المنطقة المتغيّرة وC المنطقة الثابتة؛ وهي على الكروموسوم نفسه (2) لكنها متباعدة. وأثناء نضج الخلية البائية تتّحد أيّ واحدة من 40 Vκ مع أيّ واحدة من 5 Jκ (ربط V-J)، ثم يُربط Cκ لتكوين جين V-J-C يُنسخ ويُترجَم إلى سلسلة κ خفيفة وظيفية."),
 IM("Describe the recombination of the heavy chain genes.", "صف إعادة اتحاد جينات السلسلة الثقيلة.",
    "Encoded by 4 segments V, D, J and C (51 VH, 27 DH, 6 JH on chr 14). D-J joining occurs first, then V joins DJ to form VDJ, which combines with a C gene segment, is transcribed, processed post-transcriptionally and translated into a functional heavy chain. 51 × 27 × 6 = 8262 possible VDJ combinations.",
    "تُشفَّر بأربع قطع V وD وJ وC (51 VH و27 DH و6 JH على الكروموسوم 14). يحدث ربط D-J أولًا، ثم يرتبط V بـ DJ ليكوّن VDJ، الذي يتّحد مع قطعة جين C، ثم يُنسخ ويُعدَّل بعد النسخ ويُترجَم إلى سلسلة ثقيلة وظيفية. و`51 × 27 × 6 = 8262` تركيبًا ممكنًا لـ VDJ."),
 IM("Explain junctional diversity, P-addition and N-addition.", "اشرح تنوّع نقاط الوصل وإضافة P وإضافة N.",
    "Junctional diversity: the exact position at which V-J or V-D-J are fused is not precise, so imprecise recombination changes amino acids at the junctions (productive or nonproductive rearrangements). P-addition: after the hairpin at the coding end is cleaved asymmetrically, repair enzymes fill the single strand → palindromic P-nucleotides. N-addition: TdT adds up to 15 random N-nucleotides at the DH-JH and VH-DHJH joints, so the heavy chain variable region is VH-N-DH-N-JH.",
    "تنوّع نقاط الوصل: الموقع الدقيق لدمج V-J أو V-D-J غير ثابت، فالربط غير الدقيق يغيّر الأحماض الأمينية عند نقاط الوصل (إعادات ترتيب منتِجة أو غير منتِجة). وإضافة P: بعد قطع دبّوس الشعر عند نهاية الترميز قطعًا غير متناظر تملأ إنزيمات الإصلاح الشريط المفرد ← نيوكليوتيدات P متناظرة. وإضافة N: يضيف TdT حتى 15 نيوكليوتيدًا عشوائيًا عند وصلتي DH-JH وVH-DHJH، فتصبح المنطقة المتغيّرة للسلسلة الثقيلة VH-N-DH-N-JH."),
 IM("What is allelic exclusion and why is it important?", "ما الإقصاء الأليلي ولماذا هو مهم؟",
    "B cells are diploid (maternal and paternal chromosomes), yet each expresses the rearranged heavy chain genes from only one chromosome and the rearranged light chain genes from only one chromosome. This keeps one antigenic specificity per B cell; expressing both alleles would make it multi-specific. In the Yancopoulos–Alt model a productive μ chain inhibits rearrangement of the second μ allele and induces κ rearrangement; μ + κ inhibit λ; λ rearranges only if both κ alleles are nonproductive.",
    "الخلايا البائية ثنائية المجموعة (كروموسومات أمّية وأبوية)، لكن كل خلية تعبّر عن جينات السلسلة الثقيلة المُعاد ترتيبها من كروموسوم واحد فقط، والخفيفة من كروموسوم واحد فقط. وهذا يحفظ نوعية مستضدية واحدة لكل خلية؛ فالتعبير عن الأليلين يجعلها متعدّدة النوعية. وفي نموذج يانكوبولوس–ألت تثبّط سلسلة μ المنتِجة إعادة ترتيب أليل μ الثاني وتحفّز إعادة ترتيب κ؛ وμ + κ تثبّطان λ؛ وλ تُعاد ترتيبها فقط إذا كان أليلا κ غير منتِجين."),
 IM("Describe class switching.", "صف تبديل الصنف.",
    "A B cell's specificity is fixed by its VJ and VDJ rearrangements (made without antigen early in maturation). Later it can switch to make IgG, IgE or IgA with the same specificity. Switching needs antigenic stimulation and T-cell cytokines, which decide the CH gene: IFN-γ → IgG2; IL-4 → IgG4 or IgE. The DNA between switch regions loops out and is deleted. So a single B cell can make antibodies of all classes.",
    "نوعية الخلية البائية ثابتة بإعادات ترتيب VJ وVDJ (تحدث بلا مستضد في النضج المبكّر). ولاحقًا تستطيع التحوّل إلى صنع IgG أو IgE أو IgA بالنوعية نفسها. ويحتاج التبديل التحفيز بالمستضد وسيتوكينات الخلايا التائية التي تحدّد جين CH: `IFN-γ` ← `IgG2`؛ و`IL-4` ← `IgG4` أو `IgE`. والدنا بين مناطق التبديل يلتفّ ويُحذف. فخلية بائية واحدة تستطيع صنع أضداد من كل الأصناف."),
 IM("Calculate the combinatorial diversity from the table of segments.", "احسب التنوّع التوافقي من جدول القطع.",
    "Heavy chain: 51 V × 27 D × 6 J = 8262. κ: 40 V × 5 J = 200. λ: 30 V × 4 J = 120. Heavy–light associations: 8262 × (200 + 120) = 2.64 × 10⁶.",
    "السلسلة الثقيلة: `51 × 27 × 6 = 8262`. وκ: `40 × 5 = 200`. وλ: `30 × 4 = 120`. واقتران الثقيلة بالخفيفة: `8262 × (200 + 120) = 2.64 × 10⁶`."),
]
meta = {"subject_en": "Immunology", "subject_ar": "علم المناعة", "short_ar": "مناعة", "instructor": "د. أحمد داود",
        "unit_en": "Lecture 5", "unit_ar": "المحاضرة 5", "unit_label": "LEC", "unit_no": "5",
        "title_en": "Generation of antibody diversity", "title_ar": "توليد تنوّع الأضداد",
        "kind": "Theory — نظري", "stage": "The third stage — الثالثة",
        "file_name": "BIOS - مناعة نظري المحاضرة الخامسة - الأسئلة"}
Qs = {"title_en": "Generation of antibody diversity — Comprehensive Questions", "title_ar": "توليد تنوّع الأضداد — أسئلة شاملة",
      "answers_inline": True,
      "mcq": ltr_all(mcq), "tf": ltr_all(tf), "traps": ltr_all(traps), "important": ltr_all(important)}
d = "/home/user/-/" + FOLDER
os.makedirs(d, exist_ok=True)
json.dump({"meta": meta, "questions": Qs}, open(d + "/lecture.json", "w"), ensure_ascii=False, indent=1)
from collections import Counter
qs = [m for m in mcq if "answer" in m]
print(FOLDER, len(qs), dict(Counter(m["answer"] for m in qs)), len(tf), len(traps), len(important))

```
