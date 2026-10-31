---
source: BIOS-Obsidian/tools/scripts/iml3/l3.py
handouts: []
saved: 2026-10-31
tags: [bios, code]
---
# iml3/l3.py

Utility script.

```python
import sys, re; sys.path.insert(0, "/tmp/claude-0/-home-claude/ff420988-e3a4-58e4-8344-8f014438cb53/scratchpad/imm456")
from ci import *            # c helpers + B INSHORT TERMS balance save(split.fix)
import split
split.ABBR = split.ABBR + ("E.g.", "e. g.", "5min.", "mol.")   # not sentence ends

BN = lambda en, ar: N(en, ar, label=["BIOS note", "ملاحظة BIOS"])
O = P

blocks = [
 # ───────────────────────── 1. antigen
 SEC("Antigen (Ag)", "المستضد"),
 SIDE([C("**Antigen (Ag):** is **macromolecule** that induced to **formation of antibody (Ab)**, which **react specifically** with the Ag",
         "**المستضد (`Antigen`):** **جزيء كبير** يحفّز **تكوين الضد (`Antibody`)** الذي **يتفاعل نوعيًا** مع المستضد")],
      "antigen-antibody.png", "Antigens and an antibody (antigen-binding site)", "مستضدات وضد (موقع ارتباط المستضد)"),
 T([B("Label", "الكتابة"), B("Label", "الكتابة")],
   [[B("**Antigens**", "المستضدات"), B("**Antigen**", "المستضد")], [B("**Antigen-binding site**", "موقع ارتباط المستضد"), B("**Antibody**", "الضد")]],
   style="summary", label_en="Labels in the figure", label_ar="كتابات الشكل"),
 L(["**High molecular weight** > **10000 Dalton** .", "**Foreignness**", "**Chemical complexity**"],
   ["**وزن جزيئي عالٍ** > **10000 دالتون**.", "**الغرابة (أن يكون غريبًا عن الجسم)**", "**التعقيد الكيميائي**"],
   en="Main characteristics of the antigen:", ar="الصفات الرئيسية للمستضد:"),
 L(["Whole culture extract", "Native protein antigen", "Specific carbohydrate antigen", "Synthetic peptides", "Recombinant proteins"],
   ["مستخلص المزرعة الكاملة", "المستضد البروتيني الطبيعي", "المستضد الكربوهيدراتي النوعي", "الببتيدات المصنّعة", "البروتينات المؤشبة (المعاد تركيبها)"],
   en="**Types of antigens prepared commercially**", ar="**أنواع المستضدات المحضّرة تجاريًا**"),
 C("**Vaccine**: any substance when introduce **artificially** to human or animal body produces an immune resulting **Ab**",
   "**اللقاح**: أي مادة إذا أُدخلت **اصطناعيًا** إلى جسم الإنسان أو الحيوان أنتجت استجابة مناعية ينتج عنها **أضداد**"),
 INSHORT([("Antigen = macromolecule → **antibody** that reacts **specifically** with it.", "المستضد = جزيء كبير ← **ضد** يتفاعل معه **نوعيًا**."),
          ("Characteristics: **MW > 10000 Da**, **foreignness**, **chemical complexity**.", "الصفات: **وزن جزيئي > 10000 دالتون**، **الغرابة**، **التعقيد الكيميائي**."),
          ("Commercial antigens: whole culture extract, native protein, specific carbohydrate, synthetic peptides, recombinant proteins.", "المستضدات التجارية: مستخلص مزرعة كاملة، بروتين طبيعي، كربوهيدرات نوعي، ببتيدات مصنّعة، بروتينات مؤشبة.")]),

 # ───────────────────────── 2. classification
 SEC("Classification on basis of Source/Origin", "التصنيف حسب المصدر/المنشأ"),
 C("**The Antigens classification on basis of Source/Origin**", "**تصنيف المستضدات على أساس المصدر/المنشأ**"),
 R(["**Exogenous antigens**: These are antigens which are **foreign to host body** hence are also called **foreign antigens**.",
    "These are antigens that enters the body of the organism **from the outside**, e.g. through **inhalation, ingestion, or injection**.",
    "The uptakes of these exogenous antigens by **APCs** are mainly mediated by the **phagocytosis**.",
    "E.g. **Bacteria, Fungi, Viruses** etc."],
   ["**المستضدات الخارجية (`Exogenous`)**: مستضدات **غريبة عن جسم المضيف**، ولذلك تُسمّى أيضًا **المستضدات الغريبة**.",
    "وهي مستضدات تدخل جسم الكائن **من الخارج**، مثلًا عن طريق **الاستنشاق أو الابتلاع أو الحقن**.",
    "ويتمّ التقاط هذه المستضدات الخارجية بواسطة **الخلايا المقدّمة للمستضد (`APCs`)** بصورة رئيسية **بالبلعمة**.",
    "مثل **البكتيريا والفطريات والفيروسات** وغيرها."]),
 R(["**Endogenous antigens**: These are antigens which **originate from own body** of host organisms.",
    "The endogenous antigens are processed by the **macrophages** which are later accepted by the **cytotoxic T – cells**.",
    "E.g. **Blood group antigens, HLA** (Histocompatibility Leukocyte antigens) etc."],
   ["**المستضدات الداخلية (`Endogenous`)**: مستضدات **تنشأ من جسم الكائن المضيف نفسه**.",
    "وتُعالَج المستضدات الداخلية بواسطة **البلاعم**، ثم تستقبلها لاحقًا **الخلايا التائية السامّة للخلايا**.",
    "مثل **مستضدات فصائل الدم، ومستضدات HLA** (مستضدات توافق النسيج الكريّات البيض) وغيرها."]),
 R(["**Auto antigens**: These are usually a **normal protein or protein complex** (and sometimes DNA or RNA) that is recognized by the immune system of patients suffering from a specific **autoimmune disease**.",
    "These are **not immunogenic under normal condition** however due to genetic and environmental changes or factors **immunological tolerance is lost** and immune response is generated.",
    "E.g. **Nucleoproteins, Nucleic acids**, etc."],
   ["**المستضدات الذاتية (`Auto antigens`)**: عادةً **بروتين طبيعي أو معقّد بروتيني** (وأحيانًا DNA أو RNA) يتعرّف عليه الجهاز المناعي لمرضى مصابين **بمرض مناعي ذاتي** معيّن.",
    "وهي **غير مولّدة للمناعة في الظروف الطبيعية**، لكن بسبب تغيّرات أو عوامل وراثية وبيئية **يُفقد التحمّل المناعي** وتتولّد استجابة مناعية.",
    "مثل **البروتينات النووية والأحماض النووية** وغيرها."]),
 T([B("Type", "النوع"), B("Origin", "المنشأ"), B("Examples", "أمثلة")],
   [[B("**Exogenous**", "**خارجية**"), B("from outside (inhalation, ingestion, injection); taken by APCs by phagocytosis", "من الخارج (استنشاق، ابتلاع، حقن)؛ تلتقطها APCs بالبلعمة"), B("bacteria, fungi, viruses", "البكتيريا، الفطريات، الفيروسات")],
    [B("**Endogenous**", "**داخلية**"), B("own body; processed by macrophages → cytotoxic T – cells", "جسم المضيف؛ تعالجها البلاعم ← الخلايا التائية السامّة"), B("blood group antigens, HLA", "مستضدات فصائل الدم، HLA")],
    [B("**Auto antigens**", "**ذاتية**"), B("normal self proteins; tolerance lost in autoimmune disease", "بروتينات ذاتية طبيعية؛ يُفقد التحمّل في المرض المناعي الذاتي"), B("nucleoproteins, nucleic acids", "البروتينات النووية، الأحماض النووية")]],
   key_cols=[0], widths=[20, 48, 32], style="summary", label_en="Antigens by origin", label_ar="المستضدات حسب المنشأ"),
 L(["**Kill** microorganisms .", "**Fix the flagella** on the cell wall .", "**Keep it for a long time** without deterioration .", "**Mask** the body bacterial cell"],
   ["**يقتل** الأحياء المجهرية.", "**يثبّت الأسواط** على جدار الخلية.", "**يحفظه مدّة طويلة** دون تلف.", "**يحجب (يغطّي)** جسم الخلية البكتيرية"],
   en="The properties of **formal-saline** (formaldehyde + saline) :", ar="خصائص **الفورمال-سلاين** (فورمالديهايد + محلول ملحي):"),
 INSHORT([("**Exogenous** = from outside (bacteria, fungi, viruses); **endogenous** = own body (blood group, HLA); **auto** = self proteins in autoimmune disease.", "**الخارجية** = من الخارج (بكتيريا، فطريات، فيروسات)؛ **الداخلية** = من الجسم (فصائل الدم، HLA)؛ **الذاتية** = بروتينات ذاتية في المرض المناعي الذاتي."),
          ("Formal-saline: **kills**, **fixes flagella**, **keeps long**, **masks** the body cell.", "الفورمال-سلاين: **يقتل**، **يثبّت الأسواط**، **يحفظ طويلًا**، **يحجب** جسم الخلية.")]),

 # ───────────────────────── 3. bacterial antigens
 SEC("Bacterial antigens", "المستضدات البكتيرية"),
 L(["Whole bacterial cells.", "Appendixes (e.g., **flagella, cilia, and fimbria**).", "Cell membrane (CM) which include:"],
   ["الخلايا البكتيرية الكاملة.", "الزوائد (مثل **الأسواط والأهداب والخمل**).", "غشاء الخلية (CM) ويشمل:"],
   en="Different types of antigens are located onto bacterial surfaces which are includes:", ar="توجد أنواع مختلفة من المستضدات على أسطح البكتيريا، وتشمل:"),
 L(["**Lipopolysaccharides (LPS).**", "**Peptidoglycan (PGN).**", "**Exo-polysaccharides (EPS).**", "**Capsule (Vi).**"],
   ["**عديدات السكريد الدهنية (LPS).**", "**الببتيدوغلايكان (PGN).**", "**عديدات السكريد الخارجية (EPS).**", "**المحفظة (Vi).**"], alpha=True),
 C("4. **Toxin.**", "4. **الذيفان (السم).**"),
 L(["**Flagellar (H) antigen:**", "**somatic (O) antigen**"], ["**المستضد السوطي (H):**", "**المستضد الجسمي (O)**"],
   en="Example of bacterial Ag (Salmonella Ags)", ar="مثال على المستضد البكتيري (مستضدات السالمونيلا)"),
 H2("Salmonella antigen", "مستضد السالمونيلا"),
 T([B("Somatic (O) antigen", "المستضد الجسمي (O)"), B("Somatic ( H) antigen", "المستضد (H)")],
   [[B("1- Found on the surface of the cell", "1- يوجد على سطح الخلية"), B("1 -Flagella", "1- الأسواط")],
    [B("2 -Lipid complex (it is polysaccharide)", "2- معقّد دهني (وهو عديد سكريد)"), B("2 -Protein", "2- بروتين")],
    [B("3- -Stable at 100 °C and in alcohol", "3- ثابت عند 100 °م وفي الكحول"), B("3 -Inactivated at more than 60 °C", "3- يتعطّل عند أكثر من 60 °م")]]),
 BN("The second column is the **Flagellar (H)** antigen (the header says “Somatic ( H)”). The degree signs (°) did not show in the lecture file (“100 C”, “37 C”).",
    "العمود الثاني هو المستضد **السوطي (H)** (العنوان مكتوب “Somatic ( H)”). وعلامات الدرجة (°) ما ظهرت بملف المحاضرة (“100 C”، “37 C”)."),
 INSHORT([("Bacterial surface antigens: whole cells, appendixes (flagella, cilia, fimbria), cell membrane (**LPS, PGN, EPS, capsule Vi**), toxin.", "مستضدات سطح البكتيريا: الخلايا الكاملة، الزوائد (أسواط، أهداب، خمل)، غشاء الخلية (**LPS، PGN، EPS، المحفظة Vi**)، الذيفان."),
          ("Salmonella **O** = cell surface, lipid-polysaccharide, **stable at 100 °C** and alcohol; **H** = flagella, protein, **inactivated > 60 °C**.", "السالمونيلا **O** = سطح الخلية، دهني-سكريد، **ثابت عند 100 °م** والكحول؛ و**H** = الأسواط، بروتين، **يتعطّل فوق 60 °م**.")]),

 # ───────────────────────── 4. method
 SEC("Method", "الطريقة"),
 H2("Somatic (O) antigen preparation", "تحضير المستضد الجسمي (O)"),
 R("Streaking a few typical **Salmonella colonies** from the **Salmonella-Shigella agar (S.S agar)** plate onto **brain heart infusion agar** plates using a sterile cotton swab",
   "تخطيط بضع مستعمرات **سالمونيلا** نموذجية من طبق **آجار السالمونيلا-الشيكلا (S.S agar)** على أطباق **آجار نقيع الدماغ والقلب** باستعمال مسحة قطنية معقّمة"),
 R("Plates were incubated **overnight at 37 °C**.", "حُضنت الأطباق **ليلة كاملة بدرجة 37 °م**."),
 R("Sterile normal saline was used to **harvest the lawns** and a bottle containing **250 ml** of bacterial suspension was immersed in a **boiling water bath for 3.5 hr**.",
   "استُعمل محلول ملحي طبيعي معقّم **لحصاد النمو** وغُمرت قنينة فيها **250 مل** من العالق البكتيري في **حمّام ماء مغلي لمدّة 3.5 ساعة**."),
 R("It was left to stand at room temperature overnight and again immersed in boiling water for an **additional 1.5 hr.** on the next day.",
   "تُرك بحرارة الغرفة ليلة كاملة، ثم غُمر مرّة ثانية في الماء المغلي **لمدّة 1.5 ساعة إضافية** في اليوم التالي."),
 R("The now killed bacteria were **washed 3 times** with normal saline.", "غُسلت البكتيريا المقتولة **3 مرّات** بالمحلول الملحي الطبيعي."),
 R("The resulting product had the appearance of **skim milk**.", "كان مظهر الناتج مثل **الحليب منزوع الدسم**."),
 R("It was judged **sterile** by its failure to cause **turbidity in brain heart infusion broth** tubes after prolonged incubation at 37 °C, and its failure to produce **growth on S.S agar** plates.",
   "عُدّ **معقّمًا** لعدم إحداثه **عكارة في أنابيب مرق نقيع الدماغ والقلب** بعد حضن طويل بدرجة 37 °م، ولعدم إعطائه **نموًّا على أطباق آجار S.S**."),
 R("Storage was in **0.3% formal saline at 4 °C**", "كان الحفظ في **فورمال-سلاين 0.3% بدرجة 4 °م**"),
 H2("Flagellar (H) antigen preparation", "تحضير المستضد السوطي (H)"),
 R("Inoculated a few typical Salmonella colonies from the (S.S agar) plate onto a **250 ml brain heart infusion broth**.",
   "لُقّحت بضع مستعمرات سالمونيلا نموذجية من طبق (S.S agar) في **250 مل من مرق نقيع الدماغ والقلب**."),
 R("Broth was incubated **overnight at 37 °C**.", "حُضن المرق **ليلة كاملة بدرجة 37 °م**."),
 R("Then, **250 ml of 0.6% formal saline** was added and the mixture was allowed to stand at room temperature for **5 d.** sterility test were performed.",
   "ثم أُضيف **250 مل من فورمال-سلاين 0.6%**، وتُرك الخليط بحرارة الغرفة **5 أيام**، وأُجري فحص العقامة."),
 R("Washing killed bacteria and **discard the supernatant**.", "غسل البكتيريا المقتولة **والتخلّص من الطافي**."),
 R("Re-suspend the precipitate with **0.3% formal saline** and storage at **4 °C**.", "إعادة تعليق الراسب **بفورمال-سلاين 0.3%** والحفظ بدرجة **4 °م**."),
 T([B("Step", "الخطوة"), B("Somatic (O)", "الجسمي (O)"), B("Flagellar (H)", "السوطي (H)")],
   [[B("**Growth**", "**التنمية**"), B("brain heart infusion agar plates, overnight 37 °C", "أطباق آجار نقيع الدماغ والقلب، ليلة 37 °م"), B("250 ml brain heart infusion broth, overnight 37 °C", "250 مل مرق نقيع الدماغ والقلب، ليلة 37 °م")],
    [B("**Killing**", "**القتل**"), B("boiling water bath 3.5 hr + 1.5 hr next day", "حمّام ماء مغلي 3.5 ساعة + 1.5 ساعة اليوم التالي"), B("250 ml of 0.6% formal saline, 5 days at room temperature", "250 مل فورمال-سلاين 0.6%، 5 أيام بحرارة الغرفة")],
    [B("**Washing**", "**الغسل**"), B("3 times with normal saline (looks like skim milk)", "3 مرّات بالمحلول الملحي (يشبه الحليب منزوع الدسم)"), B("wash, discard supernatant", "غسل والتخلّص من الطافي")],
    [B("**Storage**", "**الحفظ**"), B("0.3% formal saline at 4 °C", "فورمال-سلاين 0.3% بدرجة 4 °م"), B("0.3% formal saline at 4 °C", "فورمال-سلاين 0.3% بدرجة 4 °م")]],
   key_cols=[0], widths=[16, 42, 42], style="summary", label_en="O vs H preparation", label_ar="تحضير O مقابل H"),
 INSHORT([("**O antigen**: killed by **boiling** (3.5 h + 1.5 h) — fits a heat-stable antigen.", "**مستضد O**: يُقتل **بالغلي** (3.5 ساعة + 1.5 ساعة) — يناسب مستضدًا ثابتًا بالحرارة."),
          ("**H antigen**: killed by **0.6% formal saline** for 5 days (flagella kept, not boiled).", "**مستضد H**: يُقتل **بفورمال-سلاين 0.6%** لمدّة 5 أيام (تبقى الأسواط، دون غلي)."),
          ("Both stored in **0.3% formal saline at 4 °C**; sterility checked before use.", "كلاهما يُحفظ في **فورمال-سلاين 0.3% بدرجة 4 °م**؛ ويُفحص العقامة قبل الاستعمال.")]),

 # ───────────────────────── 5. SLO
 SEC("Streptolysin O antigen Preparation", "تحضير مستضد الستربتوليسين O"),
 L(["Family of lysine a **protein of 67 k Da** mol. Wt formed by **pyogenic streptococci**.",
    "**Activated by sulfhydro compound** and **inhibited by cholesterol** and related sterols.",
    "For better production, thus organisms should be grown in the **fat free and reducing agent containing medium (kalbak broth).**"],
   ["من عائلة الحالّات (lysine)، وهو **بروتين وزنه الجزيئي 67 كيلو دالتون** تكوّنه **المكوّرات السبحية المقيّحة**.",
    "**ينشّطه مركّب السلفهيدريل** و**يثبّطه الكوليسترول** والستيرولات المشابهة.",
    "ولإنتاج أفضل، يجب تنمية هذه الأحياء في **وسط خالٍ من الدهون ويحتوي عاملًا مختزلًا (مرق كالباك).**"]),
 H2("Procedure", "الإجراء"),
 R("Grow organisms in **Todd-Hewitt broth**.", "نمِّ الأحياء في **مرق تود-هيويت**."),
 R("Transfer **50 ml** culture broth to **1000 ml of kalbak's broth**.", "انقل **50 مل** من مرق المزرعة إلى **1000 مل من مرق كالباك**."),
 R("Incubate for **15 hrs at 37 degree C**.", "احضن **15 ساعة بدرجة 37 °م**."),
 R("Check the culture for **haemolysin**.", "افحص المزرعة عن **الهيمولايسين (الحالّ للدم)**."),
 R("Separate microbial cell by **filtration**.", "افصل الخلايا المجهرية **بالترشيح**."),
 R("Preserve the filtrate by adding **methiolate**.", "احفظ الراشح بإضافة **الميثيولات (الميرثيولات)**."),
 R("Store at **4 degree C**.", "احفظه بدرجة **4 °م**."),
 R("Streptolysin O present in filtrate got **inactivated after 1 month** of preparation.", "الستربتوليسين O الموجود في الراشح **يتعطّل بعد شهر واحد** من التحضير."),
 R("Thus prepared SLO retains **constant potency for many years** if properly stored", "والـ SLO المحضّر بهذه الطريقة **يحتفظ بفعالية ثابتة لسنوات كثيرة** إذا حُفظ جيدًا"),
 BN("“Family of lysine” means a family of **lysins** (cell-lysing toxins), “sulfhydro” is **sulfhydryl (–SH)**, and “methiolate” is **merthiolate (thiomersal)**.",
    "“Family of lysine” يُقصد بها عائلة **الحالّات (lysins)** أي الذيفانات المحلّلة للخلايا، و“sulfhydro” هي **السلفهيدريل (–SH)**، و“methiolate” هي **الميرثيولات (الثايومرسال)**."),
 FLOW([("Todd-Hewitt broth", "مرق تود-هيويت"), ("50 ml → 1000 ml kalbak's broth", "50 مل ← 1000 مل مرق كالباك"), ("15 hrs at 37 °C", "15 ساعة بدرجة 37 °م"), ("Check haemolysin", "فحص الحالّ للدم"), ("Filtration", "الترشيح"), ("Filtrate + methiolate, 4 °C", "الراشح + ميثيولات، 4 °م")],
      en="SLO in steps", ar="الستربتوليسين O بالخطوات"),
 INSHORT([("SLO = **67 kDa protein** of **pyogenic streptococci**; **activated by sulfhydryl**, **inhibited by cholesterol**.", "SLO = **بروتين 67 كيلو دالتون** من **المكوّرات السبحية المقيّحة**؛ **ينشّطه السلفهيدريل** و**يثبّطه الكوليسترول**."),
          ("Grown in **fat-free reducing medium** (kalbak broth) **15 h at 37 °C**; SLO is in the **filtrate**, preserved with methiolate at 4 °C.", "يُنمّى في **وسط خالٍ من الدهون ومختزل** (مرق كالباك) **15 ساعة بدرجة 37 °م**؛ والـ SLO في **الراشح** ويُحفظ بالميثيولات بدرجة 4 °م.")]),

 # ───────────────────────── 6. RBC antigens
 SEC("Red blood cell antigens", "مستضدات كريات الدم الحمر"),
 C("**Methods of the preparation of antigens:**", "**طرق تحضير المستضدات:**"),
 C("Red blood cell antigens:", "مستضدات كريات الدم الحمر:"),
 C("❖ **Blood group antigens** are one of RBCs components and composed either **sugars** (e.g., **ABO** blood group Ags) or **proteins** (e. g. **Rh** antigen groups).",
   "❖ **مستضدات فصائل الدم** أحد مكوّنات كريات الدم الحمر، وتتكوّن إمّا من **سكريات** (مثل مستضدات فصائل **ABO**) أو **بروتينات** (مثل مجموعات مستضد **Rh**)."),
 L(["Determine of an **individual's blood group**.",
    "Ensure of **immune compatibility** (typed and cross matched) through **blood transfusion** from donate to recipient patients.",
    "In **pregnancy**, the risk of the mother's immune system attacking the foreign antigens present on her fetus' RBCs and forming antibodies to cover fetal RBCs antigens."],
   ["تحديد **فصيلة دم الفرد**.",
    "ضمان **التوافق المناعي** (التحديد والمطابقة التصالبية) عند **نقل الدم** من المتبرّع إلى المرضى المستلمين.",
    "في **الحمل**، خطر مهاجمة الجهاز المناعي للأم المستضدات الغريبة الموجودة على كريات الجنين الحمر وتكوين أضداد تغطّي مستضدات كريات الجنين الحمر."],
   en="Function of RBCs Ags:", ar="وظيفة مستضدات كريات الدم الحمر:"),
 H2("Preparation of Red Blood Cell (RBCs)", "تحضير كريات الدم الحمر"),
 C("**Purpose:** To prepare **RBCs suspensions** used for **serologic testing**", "**الغرض:** تحضير **عوالق كريات الدم الحمر** المستعملة في **الفحوص المصلية**"),
 C("**Principle:** A **proper ratio of plasma to red cells** is important for accuracy in antigen antibody reactions.",
   "**المبدأ:** **النسبة الصحيحة بين البلازما والكريات الحمر** مهمة لدقّة تفاعلات المستضد والضد."),
 C("**Specimen:** Blood sample and RBCs can be obtained by **\"defibrinating\" (mashing)** clotted specimens.",
   "**العيّنة:** عيّنة دم، ويمكن الحصول على الكريات الحمر **بنزع الفايبرين \"defibrinating\" (الهرس)** من العيّنات المتخثّرة."),
 C("**Procedure to prepare RBCs Ag:**", "**إجراء تحضير مستضد كريات الدم الحمر:**"),
 R("Collected blood by **vein puncture** method.", "اجمع الدم بطريقة **البزل الوريدي**."),
 R("Added blood into **anticoagulant tube (EDTA-tube)** and then mixed.", "أضف الدم إلى **أنبوب مانع التخثّر (أنبوب EDTA)** ثم امزجه."),
 R("Added **isotonic solution such as normal saline** to the mixture.", "أضف **محلولًا متساوي التوتّر مثل المحلول الملحي الطبيعي** إلى الخليط."),
 R("centrifugation the RBCs suspension for **5min. at 3000 RPM**.", "انبذ عالق الكريات الحمر **5 دقائق بسرعة 3000 دورة/دقيقة**."),
 R("**Discard the supernatant** and again add saline to precipitate.", "**تخلّص من الطافي** وأضف المحلول الملحي مرّة ثانية إلى الراسب."),
 R("Mixed the precipitate and **repeat steps 4 and 5**.", "امزج الراسب **وكرّر الخطوتين 4 و5**."),
 R("Re-suspended the precipitate again with saline **standardized** it.", "أعد تعليق الراسب بالمحلول الملحي **ووحّد تركيزه**."),
 R("Preserve the blood in **saline for short time**, and in **AL severs solution for long time**.", "احفظ الدم في **المحلول الملحي لمدّة قصيرة**، وفي **محلول ألسيفر لمدّة طويلة**."),
 BN("“AL severs solution” is **Alsever's solution**, used to store red cells for a long time.", "“AL severs solution” هو **محلول ألسيفر (Alsever's)** المستعمل لحفظ الكريات الحمر مدّة طويلة."),
 FLOW([("Vein puncture", "البزل الوريدي"), ("EDTA tube", "أنبوب EDTA"), ("+ normal saline", "+ محلول ملحي"), ("Centrifuge 5 min, 3000 RPM", "نبذ 5 دقائق، 3000 دورة"), ("Discard supernatant, wash again", "التخلّص من الطافي، غسل ثانٍ"), ("Resuspend & standardize", "إعادة التعليق والتوحيد")],
      en="RBC antigen in steps", ar="مستضد الكريات الحمر بالخطوات"),
 INSHORT([("Blood group antigens: **sugars (ABO)** or **proteins (Rh)**.", "مستضدات فصائل الدم: **سكريات (ABO)** أو **بروتينات (Rh)**."),
          ("Functions: **blood group**, **transfusion compatibility**, **pregnancy** (mother vs fetal RBCs).", "الوظائف: **فصيلة الدم**، **توافق نقل الدم**، **الحمل** (الأم مقابل كريات الجنين)."),
          ("RBC suspension: EDTA → saline washes (**5 min, 3000 RPM**) → standardize; store in saline (short) or **Alsever's** (long).", "عالق الكريات: EDTA ← غسل بالمحلول الملحي (**5 دقائق، 3000 دورة**) ← توحيد؛ ويُحفظ بالمحلول الملحي (قصيرًا) أو **ألسيفر** (طويلًا).")]),

 *TERMS([("Antigen (Ag)", "المستضد / مولّد الضد / الأنتجين"),
         ("Antibody (Ab)", "الضد / الجسم المضاد / الأنتيبودي"),
         ("Macromolecule", "جزيء كبير / جزيء ضخم"),
         ("Foreignness", "الغرابة / كونه غريبًا عن الجسم"),
         ("Recombinant proteins", "البروتينات المؤشبة / المعاد تركيبها وراثيًا"),
         ("Vaccine", "اللقاح / المطعوم"),
         ("Exogenous / Endogenous antigens", "المستضدات الخارجية / الداخلية"),
         ("Auto antigens", "المستضدات الذاتية"),
         ("Antigen-presenting cells (APCs)", "الخلايا المقدّمة للمستضد / العارضة للمستضد"),
         ("Immunological tolerance", "التحمّل المناعي / التسامح المناعي"),
         ("Formal-saline", "الفورمال-سلاين / المحلول الملحي الفورماليني"),
         ("Lipopolysaccharide (LPS)", "عديد السكريد الدهني / السكريات الدهنية المتعدّدة"),
         ("Peptidoglycan", "الببتيدوغلايكان / الغلايكان الببتيدي"),
         ("Somatic (O) antigen", "المستضد الجسمي O"),
         ("Flagellar (H) antigen", "المستضد السوطي H"),
         ("Brain heart infusion", "نقيع الدماغ والقلب"),
         ("Supernatant / Precipitate", "الطافي / الراسب"),
         ("Streptolysin O (SLO)", "الستربتوليسين O / الحالّ السبحي O"),
         ("Haemolysin", "الحالّ للدم / الهيمولايسين"),
         ("Filtrate", "الراشح / الناتج المرشّح"),
         ("Cross matching", "المطابقة التصالبية / فحص التوافق"),
         ("Defibrination", "نزع الفايبرين / إزالة الليفين"),
         ("Isotonic solution", "محلول متساوي التوتّر / محلول متعادل الضغط"),
         ("Alsever's solution", "محلول ألسيفر")]),
]

SPECIES = re.compile(r"Salmonella(?=[ -])(?! antigen| colonies| Ags| Ag)|Shigella")
def ital(s):
    out, i = [], 0
    for m in SPECIES.finditer(s):
        if s[:m.start()].count("**") % 2: continue
        out.append(s[i:m.start()]); out.append(f"__{m.group(0)}__"); i = m.end()
    out.append(s[i:]); return "".join(out)

exec(open(__file__.replace("l3.py", "l3q.py")).read())

```
