---
source: BIOS-Obsidian/tools/scripts/vir4/v4.py
handouts: []
saved: 2026-11-01
tags: [bios, code]
---
# vir4/v4.py

Utility script.

```python
import sys; sys.path.insert(0, "/tmp/claude-0/-home-user-kwmdkm/a0840832-519a-5a9b-84ea-294867ea1189/scratchpad/imm456")
from ci import *            # c helpers + B INSHORT TERMS balance save(split.fix)

BN = lambda en, ar: N(en, ar, label=["BIOS note", "ملاحظة BIOS"])
O = P

blocks = [
 # ───────────────────────── 1
 SEC("Introduction", "المقدمة"),
 H2("Isolation and Cultivation of Viruses", "عزل الفيروسات وزرعها"),
 C(["Viruses are **obligate intracellular parasites**, meaning they **require living host cells to replicate**.", "To study viruses, it is essential to **isolate and cultivate** them in the laboratory.", "This involves providing them with **suitable host cells and conditions** for replication."],
   ["الفيروسات **طفيليات إجبارية داخل الخلايا**، أي أنها **تحتاج إلى خلايا مضيفة حية لتتضاعف**.", "ولدراسة الفيروسات لا بدّ من **عزلها وزرعها** في المختبر.", "ويتضمّن ذلك تزويدها **بخلايا مضيفة وظروف مناسبة** للتضاعف."]),
 H2("Methods of Viral Cultivation", "طرق زرع الفيروسات"),
 R("**Cell Culture:** The **most common method**, involving growing viruses in cultured cells derived from various animal tissues.", "**المزرعة الخلوية:** **الطريقة الأكثر شيوعًا**، وتتضمّن تنمية الفيروسات في خلايا مزروعة مشتقّة من أنسجة حيوانية مختلفة."),
 R("**Primary cell cultures:** Derived **directly from tissues**, have **limited lifespan**.", "**المزارع الخلوية الأولية:** مشتقّة **مباشرةً من الأنسجة**، ولها **عمر محدود**."),
 R("**Continuous cell lines:** **Immortalized (not dying)** cells that can be **propagated indefinitely**.", "**الخطوط الخلوية المستمرة:** خلايا **خالدة (لا تموت)** يمكن **إكثارها إلى ما لا نهاية**."),
 R("**Embryonated Eggs:** Used for cultivating some viruses, such as **influenza and herpes simplex viruses**.", "**البيض المُخصَّب (الحاوي على جنين):** يُستعمل لزرع بعض الفيروسات، مثل **فيروسات الإنفلونزا والحلأ البسيط (الهربس البسيط)**."),
 R("**Animal Inoculation:** Used for viruses that **cannot be grown in cell culture or eggs**, such as **rabies and poliovirus**.", "**حقن الحيوانات:** يُستعمل للفيروسات التي **لا يمكن تنميتها في المزرعة الخلوية أو البيض**، مثل **داء الكلب وفيروس شلل الأطفال**."),
 BN("Items 2 and 3 (primary cultures and continuous lines) are the two kinds of item 1 (cell culture), although the sheet numbers them separately.",
    "البندان 2 و3 (المزارع الأولية والخطوط المستمرة) هما نوعا البند 1 (المزرعة الخلوية)، مع أن الورقة رقّمتهما بشكل مستقل."),
 INSHORT([("Viruses need **living cells** → must be isolated and cultivated in the lab.", "الفيروسات تحتاج **خلايا حية** ← لا بدّ من عزلها وزرعها في المختبر."),
          ("Methods: **cell culture** (primary / continuous), **embryonated eggs** (influenza, HSV), **animal inoculation** (rabies, polio).", "الطرق: **المزرعة الخلوية** (أولية / مستمرة)، **البيض المخصّب** (الإنفلونزا، الهربس)، **حقن الحيوانات** (الكلب، شلل الأطفال).")]),

 # ───────────────────────── 2
 SEC("Steps in Viral Isolation", "خطوات العزل والزرع"),
 H2("Steps in Viral Isolation and Cultivation", "خطوات عزل الفيروسات وزرعها"),
 R("**Sample Collection:** Obtain clinical specimens (e.g., **blood, respiratory secretions, stool**) from infected individuals.", "**جمع العيّنة:** الحصول على عيّنات سريرية (مثل **الدم والإفرازات التنفسية والبراز**) من الأشخاص المصابين."),
 R("**Sample Preparation:** Inactivate or remove interfering substances, such as **antibiotics or bacteria**.", "**تحضير العيّنة:** تثبيط المواد المتداخلة أو إزالتها، مثل **المضادّات الحيوية أو البكتيريا**."),
 R("**Inoculation:** Introduce the prepared sample into the chosen host system (**cell culture, embryonated eggs, or animals**).", "**التلقيح:** إدخال العيّنة المحضّرة في النظام المضيف المختار (**المزرعة الخلوية، أو البيض المخصّب، أو الحيوانات**)."),
 R("**Incubation:** Provide appropriate conditions for viral replication (**temperature, humidity**, etc.).", "**الحضن:** توفير الظروف المناسبة لتضاعف الفيروس (**الحرارة، الرطوبة**، وغيرها)."),
 R("**Observation:** Monitor for signs of viral infection, such as **cytopathic effects (CPE)** in cell cultures or **disease symptoms** in animals.", "**المراقبة:** متابعة علامات الإصابة الفيروسية، مثل **التأثيرات المرضية الخلوية (CPE)** في المزارع الخلوية أو **أعراض المرض** في الحيوانات."),
 R("**Virus Identification:** Use various techniques to identify the isolated virus, such as:", "**تشخيص الفيروس:** استعمال تقنيات مختلفة لتحديد الفيروس المعزول، مثل:"),
 L(["**Electron microscopy:** Visualize viral particles directly.", "**Serological tests:** Detect virus-specific antibodies.", "**Nucleic acid amplification tests (NAATs):** Amplify and detect viral DNA or RNA."],
   ["**المجهر الإلكتروني:** رؤية الجسيمات الفيروسية مباشرةً.", "**الفحوص المصلية:** كشف الأضداد الخاصّة بالفيروس.", "**فحوص تضخيم الحامض النووي (NAATs):** تضخيم DNA أو RNA الفيروسي وكشفه."], alpha=True),
 FLOW([("Collection", "الجمع"), ("Preparation", "التحضير"), ("Inoculation", "التلقيح"), ("Incubation", "الحضن"), ("Observation", "المراقبة"), ("Identification", "التشخيص")], en="Six steps", ar="الخطوات الست"),
 INSHORT([("**Collect → prepare → inoculate → incubate → observe (CPE) → identify**.", "**الجمع ← التحضير ← التلقيح ← الحضن ← المراقبة (CPE) ← التشخيص**."),
          ("Identification: **EM** (particles), **serology** (antibodies), **NAATs** (DNA/RNA).", "التشخيص: **المجهر الإلكتروني** (الجسيمات)، **المصلية** (الأضداد)، **NAATs** (DNA/RNA).")]),

 # ───────────────────────── 3
 SEC("Isolation of Viruses", "عزل الفيروسات"),
 R("Viruses **cannot be grown on an artificial nutrient medium**, viruses require a **living host cell** for replication.", "**لا يمكن تنمية الفيروسات على وسط غذائي اصطناعي**، فالفيروسات تحتاج إلى **خلية مضيفة حية** لتتضاعف."),
 R("Infected host cells (eukaryotic or prokaryotic) can be cultured and grown, and then the **growth medium can be harvested** as a source of virus.", "يمكن زرع الخلايا المضيفة المصابة (حقيقية النواة أو بدائية النواة) وتنميتها، ثم **يُحصد وسط النمو** مصدرًا للفيروس."),
 R("**Virions** (virus particles) in the liquid medium can be separated from the host cells by either **centrifugation or filtration**.", "يمكن فصل **الفيريونات** (الجسيمات الفيروسية) في الوسط السائل عن الخلايا المضيفة إمّا **بالطرد المركزي أو بالترشيح**."),
 R("Filters can physically remove anything present in the solution that is **larger than the virions**; the viruses can then be **collected in the filtrate** (Figure 1).", "تستطيع المرشّحات أن تزيل فيزيائيًا كل ما في المحلول **أكبر من الفيريونات**؛ ثم **تُجمع الفيروسات في الراشح** (الشكل 1)."),
 F("filter-isolation.png", "Figure 6.3.1. Isolation of virus from other cells by Bacterial filter: Membrane filters can be used to remove cells or viruses from a solution. (a) This scanning electron micrograph shows rod-shaped bacterial cells captured on the surface of a membrane filter. Note differences in the comparative size of the membrane pores and bacteria. Viruses will pass through this filter. (b) The size of the pores in the filter determines what is captured on the surface of the filter (animal [red] and bacteria [blue]) and removed from liquid passing through. Note the viruses (green) pass through the finer filter. (credit a: modification of work by U.S. Department of Energy)",
   "الشكل 6.3.1. عزل الفيروس عن الخلايا الأخرى بالمرشّح البكتيري: يمكن استعمال المرشّحات الغشائية لإزالة الخلايا أو الفيروسات من المحلول. (أ) صورة بالمجهر الإلكتروني الماسح تُظهر خلايا بكتيرية عصوية (Bacteria) عالقة على سطح مرشّح غشائي؛ لاحظ الفرق في الحجم بين ثقوب الغشاء (Pore) والبكتيريا، والفيروسات ستمرّ خلال هذا المرشّح. (ب) حجم ثقوب المرشّح (5 مايكرومتر، و200 نانومتر = 0.2 مايكرومتر) يحدّد ما يُحتجز على سطحه (الخلايا الحيوانية [أحمر] والبكتيريا [أزرق]) ويُزال من السائل المارّ؛ لاحظ أن الفيروسات (أخضر) تمرّ خلال المرشّح الأدقّ. (مصدر أ: تعديل عن عمل وزارة الطاقة الأمريكية)", h="64mm"),
 BN("The sheet calls this figure \"Figure 1\" in the text but \"Figure 6.3.1\" in the caption — they are the same figure.",
    "الورقة تسمّي هذا الشكل \"Figure 1\" في النص و\"Figure 6.3.1\" في التعليق — وهما الشكل نفسه."),
 INSHORT([("No artificial media — viruses need **living host cells**; harvest the **growth medium**.", "لا أوساط اصطناعية — الفيروسات تحتاج **خلايا مضيفة حية**؛ ويُحصد **وسط النمو**."),
          ("Separate virions by **centrifugation or filtration**; viruses pass into the **filtrate**.", "تُفصل الفيريونات **بالطرد المركزي أو الترشيح**؛ والفيروسات تمرّ إلى **الراشح**.")]),

 # ───────────────────────── 4
 SEC("Cultivation of Viruses", "زرع الفيروسات"),
 R("Viruses can be grown **in vivo** (within a whole living organism, plant, or animal) or **in vitro** (outside a living organism in cells in an artificial environment, such as a test tube, cell culture flask, or agar plate).",
   "يمكن تنمية الفيروسات **داخل الكائن الحي (in vivo)** (ضمن كائن حي كامل، نبات أو حيوان) أو **خارج الكائن الحي (in vitro)** (في خلايا ضمن بيئة اصطناعية، مثل أنبوب اختبار أو قنينة مزرعة خلوية أو طبق آكار)."),
 R('**Bacteriophages** can be grown in the presence of a dense layer of bacteria (also called a **bacterial lawn**) grown in a **0.7 % soft agar** in a Petri dish or flat (horizontal) flask (Figure 2 a).', 'يمكن تنمية **العاثيات البكتيرية** بوجود طبقة كثيفة من البكتيريا (تُسمّى أيضًا **المرجة أو البساط البكتيري**) منماة في **آكار طري بتركيز 0.7%** في طبق بتري أو قنينة مسطّحة (أفقية) (الشكل 2 أ).'),
 C('The agar concentration is decreased from the **1.5%** usually used in culturing bacteria.', 'ويُخفَّض تركيز الآكار عن **1.5%** المستعمل عادةً في زرع البكتيريا.'),
 C('The soft 0.7% agar allows the bacteriophages to **easily diffuse** through the medium.', 'ويسمح الآكار الطري 0.7% للعاثيات **بالانتشار بسهولة** خلال الوسط.'),
 C('For **lytic bacteriophages**, lysing of the bacterial hosts can then be readily observed when a **clear zone called a plaque** is detected (Figure 2b).', 'وفي **العاثيات المحلِّلة**، يمكن ملاحظة تحلّل البكتيريا المضيفة بسهولة عند ظهور **منطقة صافية تُسمّى اللويحة (البلاك)** (الشكل 2 ب).'),
 C('As the phage kills the bacteria, many plaques are observed among the **cloudy bacterial lawn**.', 'ومع قتل العاثي للبكتيريا تُلاحظ لويحات كثيرة وسط **المرجة البكتيرية العكرة**.'),
 F("flask-plaques.png", "Figure 2. (a) Flasks like this may be used to culture human or animal cells for viral culturing. (b) These plates contain bacteriophage T4 grown on an Escherichia coli lawn. Clear plaques are visible where host bacterial cells have been lysed. Viral titers increase on the plates to the left.",
   "الشكل 2. (أ) قد تُستعمل قناني مثل هذه لزرع الخلايا البشرية أو الحيوانية لزرع الفيروسات. (ب) تحتوي هذه الأطباق على العاثي T4 منمًّى على مرجة من الإشريكية القولونية؛ وتظهر لويحات صافية حيث تحلّلت الخلايا البكتيرية المضيفة. ويزداد العيار الفيروسي في الأطباق باتجاه اليسار.", h="44mm"),
 R("**Animal viruses** require cells within a **host animal** or **tissue-culture cells** derived from an animal.", "تحتاج **الفيروسات الحيوانية** إلى خلايا داخل **حيوان مضيف** أو إلى **خلايا مزرعة نسيجية** مشتقّة من حيوان."),
 L(["**identification and diagnosis** of pathogenic viruses in clinical specimens.", "**production of vaccines**.", "**basic research** studies."],
   ["**تحديد وتشخيص** الفيروسات الممرضة في العيّنات السريرية.", "**إنتاج اللقاحات**.", "**دراسات البحث الأساسي**."], en="Animal virus cultivation is important for:", ar="زرع الفيروسات الحيوانية مهمّ لـ:"),
 H2("A. In vivo", "أ. داخل الكائن الحي"),
 C('**In vivo** host sources can be a developing embryo in an **embryonated bird’s egg** (e.g., chicken, turkey) or a **whole animal**.', 'يمكن أن تكون مصادر المضيف **داخل الكائن الحي** جنينًا نامِيًا في **بيضة طائر مخصّبة** (مثل الدجاج والديك الرومي) أو **حيوانًا كاملًا**.'),
 C('For example, most of the **influenza vaccine** manufactured for annual flu vaccination programs is cultured in **hens’ eggs**.', 'فمثلًا يُزرع معظم **لقاح الإنفلونزا** المصنَّع لبرامج التلقيح السنوية في **بيض الدجاج**.'),
 C('The embryo or host animal serves as an **incubator** for viral replication (Figure 3).', 'ويعمل الجنين أو الحيوان المضيف **حاضنةً** لتضاعف الفيروس (الشكل 3).'),
 F("egg-cultivation.png", "Figure 3. (a) The cells within chicken eggs are used to culture different types of viruses. (b) Viruses can be replicated in various locations within the egg, including the chorioallantoic membrane, the amniotic cavity, and the yolk sac. (Labels: chorioallantoic membrane, amniotic cavity, embryo, albumin, yolk sac, shell)",
   "الشكل 3. (أ) تُستعمل الخلايا داخل بيض الدجاج لزرع أنواع مختلفة من الفيروسات. (ب) يمكن أن تتضاعف الفيروسات في مواقع مختلفة داخل البيضة، منها الغشاء المشيمي السقائي، والجوف الأمنيوسي (السلوي)، وكيس المحّ. (التسميات: الغشاء المشيمي السقائي، الجوف الأمنيوسي، الجنين، الزلال (بياض البيض)، كيس المحّ (الصفار)، القشرة)", h="50mm"),
 H2("B. In vitro", "ب. خارج الكائن الحي"),
 C('For **in vitro** studies, various types of cells can be used to support the growth of viruses.', 'في الدراسات **خارج الكائن الحي** يمكن استعمال أنواع مختلفة من الخلايا لدعم نموّ الفيروسات.'),
 C('A **primary cell culture** is freshly prepared from animal organs or tissues.', 'و**المزرعة الخلوية الأولية** تُحضَّر حديثًا من أعضاء الحيوان أو أنسجته.'),
 C('Cells are extracted from tissues by **mechanical scraping or mincing** to release cells or by an **enzymatic method using trypsin or Collagenase** to break up tissue and release single cells into suspension.', 'وتُستخلص الخلايا من الأنسجة **بالكشط الميكانيكي أو الفرم** لتحرير الخلايا، أو **بطريقة إنزيمية باستعمال التربسين أو الكولاجينيز** لتفكيك النسيج وتحرير خلايا مفردة في معلّق.'),
 C('In contrast to primary cell cultures, **continuous cell lines**, usually derived from **transformed cells or tumors**, are often able to be subcultured many times or even grown indefinitely (in which case they are called **immortal**). (Figure 4).', 'وعلى خلاف المزارع الأولية، فإن **الخطوط الخلوية المستمرة**، المشتقّة عادةً من **خلايا متحوّلة أو أورام**، يمكن غالبًا زرعها ثانويًا مرّات كثيرة أو حتى تنميتها إلى ما لا نهاية (وتُسمّى عندئذٍ **خالدة**). (الشكل 4).'),
 F("cell-cultures.png", "Figure 4. Cells for culture are prepared by separating them from their tissue matrix. (a) Primary cell cultures grow attached to the surface of the culture container. Contact inhibition slows the growth of the cells once they become too dense and begin touching each other. At this point, growth can only be sustained by making a secondary culture. (b) Continuous cell cultures are not affected by contact inhibition. They continue to grow regardless of cell density.",
   "الشكل 4. تُحضَّر الخلايا للزرع بفصلها عن قالبها النسيجي. (أ) المزارع الخلوية الأولية تنمو ملتصقة بسطح وعاء الزرع (نسيج الرئة ← خلايا مفردة معزولة من النسيج ← مزرعة خلوية أولية ← تثبيط التماس ← نقل بعض الخلايا إلى وسط جديد ← مزرعة خلوية ثانوية). ويبطّئ تثبيط التماس نموّ الخلايا عندما تصبح كثيفة جدًا وتبدأ بلمس بعضها؛ وعندها لا يستمر النمو إلا بعمل مزرعة ثانوية. (ب) المزارع الخلوية المستمرة لا تتأثّر بتثبيط التماس (خلايا متحوّلة أو خلايا مفردة معزولة من ورم ← خط خلوي مستمر)، وتستمر بالنمو بغضّ النظر عن كثافة الخلايا.", h="56mm"),
 T([B("", ""), B("Primary cell culture", "المزرعة الأولية"), B("Continuous cell line", "الخط المستمر")],
   [[B("**Source**", "**المصدر**"), B("freshly from animal organs or tissues", "حديثًا من أعضاء الحيوان أو أنسجته"), B("transformed cells or tumors", "خلايا متحوّلة أو أورام")],
    [B("**Lifespan**", "**العمر**"), B("limited", "محدود"), B("indefinite (immortal)", "غير محدود (خالدة)")],
    [B("**Contact inhibition**", "**تثبيط التماس**"), B("yes → secondary culture needed", "نعم ← تحتاج مزرعة ثانوية"), B("not affected", "لا تتأثّر")]],
   key_cols=[0], widths=[24, 38, 38], style="summary", label_en="Primary vs continuous", label_ar="الأولية مقابل المستمرة"),
 INSHORT([("**In vivo** (whole organism, embryonated egg) vs **in vitro** (cells in flasks, plates).", "**داخل الكائن** (كائن كامل، بيض مخصّب) مقابل **خارجه** (خلايا في قناني وأطباق)."),
          ("Phages: **bacterial lawn** in **0.7% soft agar** (not 1.5%) → **plaques** = clear zones of lysis.", "العاثيات: **مرجة بكتيرية** في **آكار طري 0.7%** (لا 1.5%) ← **لويحات** = مناطق تحلّل صافية."),
          ("Eggs: chorioallantoic membrane, amniotic cavity, yolk sac; flu vaccine in **hens’ eggs**.", "البيض: الغشاء المشيمي السقائي، الجوف الأمنيوسي، كيس المحّ؛ ولقاح الإنفلونزا في **بيض الدجاج**.")]),

 # ───────────────────────── 5
 SEC("Detection of a Virus", "الكشف عن الفيروس"),
 C("Regardless of the method of cultivation, once a virus has been introduced into a whole host organism, embryo, or tissue-culture cell, a sample can be prepared from the infected host, embryo, or cell line for further analysis under a **brightfield, electron, or fluorescent microscope**.",
   "بغضّ النظر عن طريقة الزرع، بمجرّد إدخال الفيروس في كائن مضيف كامل أو جنين أو خلية مزرعة نسيجية، يمكن تحضير عيّنة من المضيف أو الجنين أو الخط الخلوي المصاب لتحليلها أكثر تحت **المجهر الضوئي ذي الحقل الساطع أو الإلكتروني أو الفلوري**."),
 C('**Cytopathic effects (CPEs)** are distinct observable cell abnormalities due to viral infection.', '**التأثيرات المرضية الخلوية (CPEs)** شذوذات خلوية مميّزة يمكن ملاحظتها بسبب الإصابة الفيروسية.'),
 C('CPEs can include **loss of adherence** to the surface of the container, changes in cell shape from **flat to round**, **shrinkage of the nucleus**, **vacuoles in the cytoplasm**, **fusion of cytoplasmic membranes** and the formation of **multinucleated syncytia**, **inclusion bodies** in the nucleus or cytoplasm, and **complete cell lysis** (Figure 5).', 'وقد تشمل CPEs: **فقدان الالتصاق** بسطح الوعاء، وتغيّر شكل الخلية من **مسطّح إلى كروي**، و**انكماش النواة**، و**فجوات في السايتوبلازم**، و**اندماج الأغشية السايتوبلازمية** وتكوين **مخلوّات متعدّدة النوى**، و**أجسام اشتمالية** في النواة أو السايتوبلازم، و**التحلّل الكامل للخلية** (الشكل 5).'),
 T([B("Virus", "الفيروس"), B("Cytopathic Effect", "التأثير المرضي الخلوي")],
   [[B("*Paramyxovirus*", "*الفيروس المخاطاني نظير*"), B("Syncytium and faint basophilic cytoplasmic inclusion bodies", "مخلوّ وأجسام اشتمالية سايتوبلازمية قاعدية الصبغ باهتة")],
    [B("*Poxvirus*", "*الفيروس الجدري*"), B("Pink eosinophilic cytoplasmic inclusion bodies (arrows) and cell swelling", "أجسام اشتمالية سايتوبلازمية وردية حمضية الصبغ (الأسهم) وانتفاخ الخلية")],
    [B("*Herpesvirus*", "*الفيروس الحلئي (الهربس)*"), B("Cytoplasmic stranding (arrow) and nuclear inclusion bodies (dashed arrow)", "تخيّط (خيوط) سايتوبلازمي (السهم) وأجسام اشتمالية نووية (السهم المتقطّع)")],
    [B("*Adenovirus*", "*الفيروس الغدّي*"), B("Cell enlargement, rounding, and distinctive “grape-like” clusters", "تضخّم الخلية وتكوّرها وعناقيد مميّزة \"شبيهة بالعنب\"")]],
   key_cols=[0], widths=[30, 70], label_en="Cytopathic Effects of Specific Viruses", label_ar="التأثيرات المرضية الخلوية لفيروسات معيّنة"),
 F("cpe-examples.png", "Figure 5. Cytopathic effects induced by virus infections — Example column, left to right: Paramyxovirus, Poxvirus, Herpesvirus, Adenovirus (ASM MicrobeLibrary.org © Suchman and Blair)",
   "الشكل 5. التأثيرات المرضية الخلوية الناتجة عن الإصابات الفيروسية — عمود الأمثلة من اليسار إلى اليمين: الفيروس المخاطاني نظير، الفيروس الجدري، الفيروس الحلئي، الفيروس الغدّي", h="40mm"),
 BN("Figure 5 in the sheet is a table picture; its text is written above as a bilingual table and its four example photos are shown in one row.",
    "الشكل 5 في الورقة صورة جدول؛ فكُتب نصّه أعلاه جدولًا ثنائي اللغة، وعُرضت صوره الأربع بصفّ واحد."),
 INSHORT([("Detect under **brightfield, electron, or fluorescent** microscope.", "الكشف تحت المجهر **الضوئي الساطع أو الإلكتروني أو الفلوري**."),
          ("**CPEs**: loss of adherence, round cells, nuclear shrinkage, vacuoles, **syncytia**, inclusion bodies, **lysis**.", "**CPEs**: فقدان الالتصاق، تكوّر الخلايا، انكماش النواة، فجوات، **مخلوّات**، أجسام اشتمالية، **تحلّل**."),
          ("Paramyxo → syncytium; pox → pink cytoplasmic inclusions; herpes → stranding + nuclear inclusions; adeno → grape-like clusters.", "المخاطاني نظير ← مخلوّ؛ الجدري ← أجسام سايتوبلازمية وردية؛ الهربس ← تخيّط + أجسام نووية؛ الغدّي ← عناقيد عنبية.")]),

 *TERMS([("Isolation", "العزل"),
         ("Cultivation", "الزرع / الاستنبات"),
         ("Cell culture", "المزرعة الخلوية / زرع الخلايا"),
         ("Primary cell culture", "المزرعة الخلوية الأولية"),
         ("Continuous cell line", "الخط الخلوي المستمر"),
         ("Immortalized / immortal", "خالدة / مُخلَّدة"),
         ("Embryonated egg", "البيض المخصّب / الحاوي على جنين"),
         ("Animal inoculation", "حقن (تلقيح) الحيوانات"),
         ("Inoculation", "التلقيح / الحقن"),
         ("Incubation", "الحضن"),
         ("Filtrate", "الراشح"),
         ("Centrifugation", "الطرد المركزي"),
         ("In vivo / in vitro", "داخل الكائن الحي / خارج الكائن الحي (في الزجاج)"),
         ("Bacterial lawn", "المرجة البكتيرية / البساط البكتيري"),
         ("Soft agar", "الآكار الطري"),
         ("Lytic bacteriophage", "العاثي المحلِّل"),
         ("Plaque", "اللويحة / البلاك / البقعة الصافية"),
         ("Viral titer", "العيار الفيروسي"),
         ("Chorioallantoic membrane", "الغشاء المشيمي السقائي"),
         ("Amniotic cavity", "الجوف الأمنيوسي / السلوي"),
         ("Yolk sac", "كيس المحّ / كيس الصفار"),
         ("Trypsin / Collagenase", "التربسين / الكولاجينيز"),
         ("Contact inhibition", "تثبيط التماس"),
         ("Cytopathic effect (CPE)", "التأثير المرضي الخلوي / الاعتلال الخلوي"),
         ("Syncytium", "المخلوّ / الخلية المندمجة متعدّدة النوى"),
         ("Inclusion bodies", "الأجسام الاشتمالية / المحتواة"),
         ("Cell lysis", "تحلّل الخلية"),
         ("Virion", "الفيريون / الجسيم الفيروسي"),
         ("Serological tests", "الفحوص المصلية"),
         ("NAATs", "فحوص تضخيم الحامض النووي"),
         ("Vaccine", "اللقاح"),
         ("Transformed cells", "الخلايا المتحوّلة"),
         ("Secondary culture", "المزرعة الثانوية"),
         ("Fluorescent microscope", "المجهر الفلوري / مجهر التألّق")]),
]
_t = blocks[-1]; _r = _t["rows"]
blocks[-1:] = [dict(_t, rows=_r[i:i + 6]) for i in range(0, len(_r), 6)]

exec(open(__file__.replace("v4.py", "v4q.py")).read())

```
