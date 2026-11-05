---
source: BIOS-Obsidian/tools/scripts/gen2/g2q.py
handouts: [genetics-lec2-mitosis]
saved: 2026-11-05
tags: [bios, code]
---
# gen2/g2q.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#genetics-lec2-mitosis|genetics-lec2-mitosis]]

```python
mcq = [
 {"topic_en": "Definitions and chromosome structure", "topic_ar": "التعاريف وتركيب الكروموسوم"},
 Q("The basic unit of heredity that codes for a specific trait is the:", "الوحدة الأساسية للوراثة التي تشفّر لصفة معيّنة هي:", O(("Gene", "الجين"), ("Genome", "الجينوم"), ("Chromatid", "الكروماتيد"), ("Centromere", "السنترومير")), "a"),
 Q("The total hereditary endowment of DNA of a cell or organism is the:", "مجموع الموروث الوراثي من DNA لخلية أو كائن هو:", O(("Gene", "الجين"), ("Genome", "الجينوم"), ("Gamete", "المشيج"), ("Kinetochore", "الكاينيتوكور")), "b"),
 Q("Somatic cells are:", "الخلايا الجسمية هي:", O(("Sperm and eggs only", "النطف والبيوض فقط"), ("Haploid cells", "خلايا أحادية"), ("All body cells except reproductive cells", "جميع خلايا الجسم عدا التكاثرية"), ("Zygotes only", "الزايكوتات فقط")), "c"),
 Q("A diploid (2n) cell has each chromosome type represented by:", "في الخلية الثنائية (2n) يُمثَّل كل نوع كروموسومي بـ:", O(("One chromosome", "كروموسوم واحد"), ("Three chromosomes", "ثلاثة كروموسومات"), ("Four chromatids only", "أربعة كروماتيدات فقط"), ("Two homologous chromosomes", "كروموسومين متماثلين")), "d"),
 Q("Homologous chromosomes are chromosomes of the same size and shape that carry:", "الكروموسومات المتماثلة بالحجم والشكل نفسيهما وتحمل:", O(("The same type of genes", "النوع نفسه من الجينات"), ("Different types of genes", "أنواعًا مختلفة من الجينات"), ("No genes", "لا جينات"), ("Only histones", "هستونات فقط")), "a"),
 Q("The region of the chromosome where microtubules attach during mitosis and meiosis is the:", "منطقة الكروموسوم التي ترتبط بها الأنيبيبات الدقيقة أثناء الانقسامين:", O(("Chromatid", "الكروماتيد"), ("Centromere", "السنترومير"), ("Telomere", "التيلومير"), ("Cell plate", "الصفيحة الخلوية")), "b"),
 Q("A chromosome is composed of:", "يتكوّن الكروموسوم من:", O(("RNA and lipid", "RNA ودهون"), ("DNA only", "DNA فقط"), ("DNA and protein (histones)", "DNA وبروتين (هستونات)"), ("Protein only", "بروتين فقط")), "c"),
 Q("In an organism with 2n = 4, chromosomes 1 & 3 came from:", "في كائن 2n = 4، الكروموسومان 1 و3 جاءا من:", O(("The father", "الأب"), ("Both parents", "الأبوين"), ("Mitosis", "الانقسام الخيطي"), ("The mother", "الأم")), "d"),
 Q("This figure shows the two halves of a duplicated chromosome joined at the centromere; each half is a:", "يوضّح هذا الشكل نصفي كروموسوم مضاعَف متّصلين عند السنترومير؛ كل نصف هو:", O(("Chromatid", "كروماتيد"), ("Gene", "جين"), ("Kinetochore", "كاينيتوكور"), ("Spindle fibre", "خيط مغزل")), "a", img="assets/chromosome-structure.png", img_h="34mm"),
 {"topic_en": "Cell cycle", "topic_ar": "دورة الخلية"},
 Q("DNA is replicated during:", "يتضاعف DNA أثناء:", O(("G1 phase", "طور G1"), ("S phase", "طور S"), ("G2 phase", "طور G2"), ("M phase", "طور M")), "b"),
 Q("Metabolic changes that assemble the cytoplasmic materials for mitosis and cytokinesis occur in:", "التغيّرات الأيضية التي تجمع المواد السايتوبلازمية للانقسام تحدث في:", O(("G1", "G1"), ("S", "S"), ("G2", "G2"), ("G0", "G0")), "c"),
 Q("Interphase consists of:", "يتكوّن الطور البيني من:", O(("Prophase and metaphase", "التمهيدي والاستوائي"), ("M phase only", "طور M فقط"), ("Mitosis and cytokinesis", "الخيطي وانقسام السايتوبلازم"), ("G1, S and G2", "G1 وS وG2")), "d"),
 Q("The M phase is:", "طور M هو:", O(("Nuclear division followed by cell division", "انقسام نووي يتبعه انقسام خلوي"), ("DNA synthesis", "تصنيع DNA"), ("Cell cycle arrest", "توقّف دورة الخلية"), ("A gap phase", "طور فاصل")), "a"),
 Q("In this figure, the phase labelled G0 means:", "في هذا الشكل، الطور المؤشّر G0 يعني:", O(("DNA replication", "تضاعف DNA"), ("Cell cycle arrest", "توقّف دورة الخلية"), ("Cytokinesis", "انقسام السايتوبلازم"), ("Double-checking chromosomes", "التحقّق من الكروموسومات")), "b", img="assets/cell-cycle.png", img_h="46mm"),
 {"topic_en": "Mitosis and its phases", "topic_ar": "الانقسام الخيطي ومراحله"},
 Q("Mitosis produces:", "ينتج الانقسام الخيطي:", O(("Four haploid cells", "أربع خلايا أحادية"), ("Two genetically different cells", "خليتين مختلفتين وراثيًا"), ("Two genetically identical daughter cells", "خليتين بنويتين متطابقتين وراثيًا"), ("One zygote", "زايكوتًا واحدًا")), "c"),
 Q("The division of the nucleus is called:", "يُسمّى انقسام النواة:", O(("Cytokinesis", "انقسام السايتوبلازم"), ("Interphase", "الطور البيني"), ("Regeneration", "التجدّد"), ("Karyokinesis", "انقسام النواة")), "d"),
 Q("Mitosis is conventionally divided into how many stages?", "يُقسَّم الانقسام الخيطي اصطلاحًا إلى كم مرحلة؟", O(("Five", "خمس"), ("Four", "أربع"), ("Three", "ثلاث"), ("Six", "ست")), "a"),
 Q("The stage that occupies over half of mitosis is:", "المرحلة التي تشغل أكثر من نصف الانقسام الخيطي:", O(("Anaphase", "الانفصالي"), ("Prophase", "التمهيدي"), ("Metaphase", "الاستوائي"), ("Telophase", "النهائي")), "b"),
 Q("The nuclear envelope fragments during:", "يتفتّت الغلاف النووي أثناء:", O(("Telophase", "النهائي"), ("Anaphase", "الانفصالي"), ("Prometaphase", "ما قبل الاستوائي"), ("Interphase", "الطور البيني")), "c"),
 Q("Spindle fibres attach to the centre of each chromosome at the:", "ترتبط خيوط المغزل بمركز كل كروموسوم عند:", O(("Telomere", "التيلومير"), ("Cell plate", "الصفيحة الخلوية"), ("Histone", "الهستون"), ("Kinetochore", "الكاينيتوكور")), "d"),
 Q("Chromosomes align along the metaphase plate during:", "تصطفّ الكروموسومات على الصفيحة الاستوائية أثناء:", O(("Metaphase", "الاستوائي"), ("Prophase", "التمهيدي"), ("Telophase", "النهائي"), ("G2", "G2")), "a"),
 Q("The shortest stage of mitosis is:", "أقصر مرحلة في الانقسام الخيطي:", O(("Prophase", "التمهيدي"), ("Anaphase", "الانفصالي"), ("Prometaphase", "ما قبل الاستوائي"), ("Metaphase", "الاستوائي")), "b"),
 Q("The separated sister chromatids are referred to as:", "تُسمّى الكروماتيدات الشقيقة المنفصلة:", O(("Homologous chromosomes", "كروموسومات متماثلة"), ("Isochromosomes", "كروموسومات متساوية الذراعين"), ("Daughter chromosomes", "كروموسومات بنوية"), ("Bivalents", "ثنائيات")), "c"),
 Q("The stage that is a reversal of many processes of prophase is:", "المرحلة التي تعكس كثيرًا من عمليات التمهيدي:", O(("Metaphase", "الاستوائي"), ("Anaphase", "الانفصالي"), ("Prometaphase", "ما قبل الاستوائي"), ("Telophase", "النهائي")), "d"),
 Q("In plants, cytokinesis occurs by:", "في النبات يحدث انقسام السايتوبلازم بـ:", O(("Formation of a cell plate", "تكوين صفيحة خلوية"), ("Constriction of the cytoplasm", "تخصّر السايتوبلازم"), ("Crossing over", "العبور"), ("Budding", "التبرعم")), "a"),
 Q("In this figure, \"centromeres divide; sister chromatids move to opposite poles\" labels:", "في هذا الشكل، \"انقسام السنتروميرات؛ تحرّك الكروماتيدات إلى القطبين\" يؤشّر:", O(("Metaphase", "الاستوائي"), ("Anaphase", "الانفصالي"), ("Telophase", "النهائي"), ("Prophase", "التمهيدي")), "b", img="assets/mitosis-phases.png", img_h="52mm"),
 {"topic_en": "Uses and errors", "topic_ar": "الاستعمالات والأخطاء"},
 Q("Starfish regenerate lost arms through:", "يجدّد نجم البحر أذرعه المفقودة بـ:", O(("Meiosis", "الانقسام الاختزالي"), ("Fertilization", "الإخصاب"), ("Mitosis", "الانقسام الخيطي"), ("Crossing over", "العبور")), "c"),
 Q("Skin and digestive tract cells are constantly sloughed off and replaced; this use of mitosis is:", "خلايا الجلد والقناة الهضمية تتساقط وتُستبدل باستمرار؛ هذا الاستعمال هو:", O(("Regeneration", "التجدّد"), ("Asexual reproduction", "التكاثر اللاجنسي"), ("Development", "التطوّر"), ("Cell replacement", "استبدال الخلايا")), "d"),
 Q("Transversal cleavage of the centromere forms:", "الانشطار المستعرض للسنترومير يكوّن:", O(("Isochromosomes", "كروموسومات متساوية الذراعين"), ("Normal daughter chromosomes", "كروموسومات بنوية طبيعية"), ("Bivalents", "ثنائيات"), ("Polar bodies", "أجسامًا قطبية")), "a"),
 Q("An isochromosome shows:", "يُظهر الكروموسوم متساوي الذراعين:", O(("Two normal arms", "ذراعين طبيعيتين"), ("Deletion of one arm and duplication of the other", "حذف ذراع وتضاعف الأخرى"), ("Loss of the centromere only", "فقد السنترومير فقط"), ("Four chromatids", "أربعة كروماتيدات")), "b"),
 Q("An individual with two or more cell populations with different chromosomal makeup shows:", "فرد لديه مجموعتان أو أكثر من الخلايا بتركيب كروموسومي مختلف يُظهر:", O(("Isochromosome", "كروموسومًا متساوي الذراعين"), ("Haploidy", "أحادية"), ("Chromosome mosaics", "موزاييكًا كروموسوميًا"), ("Homology", "تماثلًا")), "c"),
]
mcq = balance(mcq, 23)

tf = [
 TF("Eukaryotic cells divide in two ways: mitosis and meiosis.", "تنقسم الخلايا حقيقية النواة بطريقتين: الخيطي والاختزالي.", "T"),
 TF("Gametes are somatic cells.", "الأمشاج خلايا جسمية.", "F"),
 TF("A haploid cell has one chromosome of each type.", "الخلية الأحادية فيها كروموسوم واحد من كل نوع.", "T"),
 TF("Duplicated chromosomes are connected by a centromere.", "ترتبط الكروموسومات المضاعَفة بالسنترومير.", "T"),
 TF("After S phase each chromosome consists of two sister chromatids.", "بعد طور S يتكوّن كل كروموسوم من كروماتيدين شقيقين.", "T"),
 TF("Interphase includes the M phase.", "يشمل الطور البيني طور M.", "F"),
 TF("Mitosis is used by single-celled organisms to reproduce.", "تستعمل الكائنات وحيدة الخلية الانقسام الخيطي للتكاثر.", "T"),
 TF("Mitosis is a series of separate, non-continuous steps.", "الانقسام الخيطي خطوات منفصلة غير مستمرة.", "F"),
 TF("The mitotic spindle begins to form in prophase.", "يبدأ مغزل الانقسام بالتكوّن في التمهيدي.", "T"),
 TF("Anaphase is the longest stage of mitosis.", "الانفصالي أطول مراحل الانقسام الخيطي.", "F"),
 TF("In telophase the spindle fibers disappear.", "في النهائي تختفي خيوط المغزل.", "T"),
 TF("In animals cytokinesis is by a cell plate.", "في الحيوان يتم انقسام السايتوبلازم بصفيحة خلوية.", "F"),
 TF("Chromosome mosaics can affect blood, egg and sperm, and skin cells.", "قد يصيب الموزاييك الكروموسومي خلايا الدم والبيوض والنطف والجلد.", "T"),
]

traps = [
 TR("Chromatid vs chromosome", "الكروماتيد مقابل الكروموسوم", "A chromatid is one of the two duplicated copies joined at the centromere; after they separate in anaphase each one is called a daughter chromosome.", "الكروماتيد نسخة من النسختين المضاعفتين المتّصلتين عند السنترومير؛ وبعد انفصالهما في الانفصالي تُسمّى كل واحدة كروموسومًا بنويًا."),
 TR("Centromere vs kinetochore", "السنترومير مقابل الكاينيتوكور", "The centromere is the region joining sister chromatids; the kinetochore is where spindle fibres attach at the centre of each chromosome (prometaphase).", "السنترومير منطقة ربط الكروماتيدين الشقيقين؛ والكاينيتوكور مكان ارتباط خيوط المغزل بمركز كل كروموسوم (ما قبل الاستوائي)."),
 TR("Longest vs shortest stage", "أطول وأقصر مرحلة", "Prophase is the longest (over half of mitosis); anaphase is the shortest.", "التمهيدي الأطول (أكثر من نصف الانقسام)؛ والانفصالي الأقصر."),
 TR("Where does the nuclear envelope break?", "متى يتفتّت الغلاف النووي؟", "In this lecture the nuclear envelope fragments in prometaphase (the figure shows its breakdown starting in prophase); it reforms in telophase.", "في هذه المحاضرة يتفتّت الغلاف النووي في ما قبل الاستوائي (والشكل يُظهر بدء تحطّمه في التمهيدي)؛ ويعود في النهائي."),
 TR("Interphase is not a phase of mitosis", "الطور البيني ليس من مراحل الخيطي", "Interphase = G1 + S + G2, between divisions; the five mitotic stages are prophase, prometaphase, metaphase, anaphase, telophase.", "الطور البيني = G1 + S + G2 بين الانقسامات؛ ومراحل الخيطي الخمس: التمهيدي، ما قبل الاستوائي، الاستوائي، الانفصالي، النهائي."),
 TR("Cytokinesis in plants vs animals", "انقسام السايتوبلازم في النبات مقابل الحيوان", "Plants: cell plate along the metaphase plate line; animals: constriction of the cytoplasm.", "النبات: صفيحة خلوية على خط الصفيحة الاستوائية؛ الحيوان: تخصّر السايتوبلازم."),
 TR("i p and i q", "i p وi q", "Isochromosome i p = two short arms (q lost); i q = two long arms (p lost); each is a deletion of one arm plus duplication of the other.", "i p = ذراعان قصيرتان (فُقدت q)؛ i q = ذراعان طويلتان (فُقدت p)؛ وكل منهما حذف ذراع مع تضاعف الأخرى."),
]

important = [
 IM("Define: gene, genome, somatic cell, gamete, diploid, haploid, homologous chromosome, chromatid, centromere.", "عرّف: الجين، الجينوم، الخلية الجسمية، المشيج، الثنائي، الأحادي، الكروموسوم المتماثل، الكروماتيد، السنترومير.", "Gene: basic unit of heredity coding for a trait. Genome: total hereditary DNA of a cell or organism. Somatic cell: all body cells except reproductive cells. Gamete: reproductive cell (sperm, egg). Diploid (2n): each chromosome type represented by two homologues. Haploid (n): by only one. Homologous chromosomes: same size and shape, same type of genes. Chromatid: one of two duplicated chromosomes joined at the centromere. Centromere: region where microtubules attach during mitosis and meiosis.", "الجين: الوحدة الأساسية للوراثة يشفّر لصفة. الجينوم: مجموع DNA الوراثي للخلية أو الكائن. الخلية الجسمية: كل خلايا الجسم عدا التكاثرية. المشيج: خلية تكاثرية (نطفة، بيضة). الثنائي (2n): كل نوع ممثَّل بمتماثلين. الأحادي (n): بواحد فقط. المتماثلة: بالحجم والشكل نفسيهما وتحمل النوع نفسه من الجينات. الكروماتيد: أحد كروموسومين مضاعفين متّصلين بالسنترومير. السنترومير: منطقة ارتباط الأنيبيبات الدقيقة أثناء الانقسامين."),
 IM("Describe the phases of the cell cycle.", "صف أطوار دورة الخلية.", "G1: metabolic changes prepare the cell for division. S: DNA synthesis replicates the genetic material, so each chromosome has two sister chromatids. G2: metabolic changes assemble the cytoplasmic materials for mitosis and cytokinesis. M: nuclear division (mitosis) followed by cell division (cytokinesis). G1, S and G2 together = interphase.", "G1: تغيّرات أيضية تهيّئ الخلية للانقسام. S: تصنيع DNA يضاعف المادة الوراثية فيصبح لكل كروموسوم كروماتيدان شقيقان. G2: تغيّرات أيضية تجمع المواد السايتوبلازمية للانقسام. M: انقسام نووي (خيطي) يتبعه انقسام خلوي (السايتوبلازم). وG1 وS وG2 معًا = الطور البيني."),
 IM("Describe the phases of mitosis.", "صف مراحل الانقسام الخيطي.", "Prophase (over half of mitosis): chromosomes condense and thicken, each appears as two sister chromatids, spindle begins to form. Prometaphase: nuclear envelope fragments, spindle fibres attach at the kinetochore, condensation continues. Metaphase: chromosomes align on the metaphase plate. Anaphase (shortest): centromeres divide, sister chromatids move to opposite poles as daughter chromosomes. Telophase: nuclear membrane reforms, chromosomes uncoil, spindle disappears.", "التمهيدي (أكثر من النصف): تتكثّف الكروموسومات وتثخن ويظهر كل منها كروماتيدين، ويبدأ المغزل. ما قبل الاستوائي: يتفتّت الغلاف النووي وترتبط الخيوط بالكاينيتوكور ويستمر التكثّف. الاستوائي: الاصطفاف على الصفيحة الاستوائية. الانفصالي (الأقصر): تنقسم السنتروميرات وتتحرّك الكروماتيدات إلى القطبين كروموسومات بنوية. النهائي: يعود الغشاء النووي وتنفكّ الكروموسومات ويختفي المغزل."),
 IM("Compare cytokinesis in plant and animal cells.", "قارن انقسام السايتوبلازم في الخلايا النباتية والحيوانية.", "Cytokinesis is the final cellular division forming two new cells. In plants a cell plate forms along the line of the metaphase plate; in animals there is a constriction of the cytoplasm.", "انقسام السايتوبلازم هو الانقسام الخلوي الأخير الذي يكوّن خليتين جديدتين. في النبات تتكوّن صفيحة خلوية على خط الصفيحة الاستوائية؛ وفي الحيوان يحدث تخصّر في السايتوبلازم."),
 IM("In which circumstances does mitosis occur?", "في أي الحالات يحدث الانقسام الخيطي؟", "1. Development and growth: cell number increases. 2. Cell replacement: e.g. skin and digestive tract. 3. Regeneration: e.g. starfish regrow lost arms. 4. Asexual reproduction: e.g. vegetative propagation in plants.", "1. التطوّر والنمو: يزداد عدد الخلايا. 2. استبدال الخلايا: مثل الجلد والقناة الهضمية. 3. التجدّد: مثل نجم البحر يجدّد أذرعه. 4. التكاثر اللاجنسي: مثل التكاثر الخضري في النبات."),
 IM("Explain transversal cleavage of the centromere and its results.", "اشرح الانشطار المستعرض للسنترومير ونتائجه.", "It is an anaphase accident that disturbs distribution of genetic material. It forms isochromosomes made of only the two short arms (i p) or the two long arms (i q), so each has a deletion of one arm and a duplication of the other. It leads to chromosome mosaics: two or more cell populations with different chromosomal makeup, which can affect blood cells, egg and sperm cells, and skin cells.", "هو حادث في الطور الانفصالي يخلّ بتوزيع المادة الوراثية. يكوّن كروموسومات متساوية الذراعين من الذراعين القصيرين فقط (i p) أو الطويلين (i q)، فيكون في كل منها حذف ذراع وتضاعف الأخرى. ويؤدّي إلى الموزاييك الكروموسومي: مجموعتان أو أكثر من الخلايا بتركيب كروموسومي مختلف، وقد يصيب خلايا الدم والبيوض والنطف والجلد."),
]

meta = dict(GT, unit_en="Lecture 2", unit_ar="المحاضرة 2", unit_no="2", title_en="Mitosis", title_ar="الانقسام الخيطي")
save("genetics-lec2-mitosis", meta, blocks, mcq, tf, traps, important)

```
