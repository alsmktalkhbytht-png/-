---
source: BIOS-Obsidian/tools/scripts/enz4/e4q.py
handouts: [enzymology-lec4-bioenergetics]
saved: 2026-11-05
tags: [bios, code]
---
# enz4/e4q.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#enzymology-lec4-bioenergetics|enzymology-lec4-bioenergetics]]

```python
A = lambda f: "assets/" + f
mcq = [
 {"topic_en": "Metabolism", "topic_ar": "الأيض"},
 Q("Metabolism represents:", "يمثّل الأيض:", O(("The sum of all the chemical changes occurring in a cell, a tissue, or the body", "مجموع كل التغيّرات الكيميائية في الخلية أو النسيج أو الجسم"), ("Only the breakdown of glucose", "تكسير الغلوكوز فقط"), ("Only protein synthesis", "بناء البروتين فقط"), ("The energy of sunlight", "طاقة ضوء الشمس")), "a"),
 Q("In a metabolic pathway:", "في المسار الأيضي:", O(("Each reaction is independent", "كل تفاعل مستقل"), ("The product of one reaction serves as the substrate of the next", "ناتج التفاعل مادة أساس للتفاعل التالي"), ("No enzymes are needed", "لا حاجة للإنزيمات"), ("Only one step occurs", "تحدث خطوة واحدة فقط")), "b"),
 Q("Catabolic pathways are:", "مسارات الهدم:", O(("Endergonic and synthetic", "ماصّة للطاقة وبنائية"), ("Links between pathways", "روابط بين المسارات"), ("Exergonic and degradative", "طاردة للطاقة وتكسيرية"), ("Always reversible", "عكوسة دائمًا")), "c"),
 Q("The synthesis of glycogen from glucose is an example of:", "بناء الغلايكوجين من الغلوكوز مثال على:", O(("Catabolism", "الهدم"), ("An amphibolic pathway", "مسار مزدوج"), ("Oxidative phosphorylation", "الفسفرة التأكسدية"), ("Anabolism", "البناء")), "d"),
 Q("The citric acid cycle is an example of:", "دورة حامض الستريك مثال على:", O(("Amphibolic pathway", "مسار مزدوج"), ("Pure anabolism", "بناء فقط"), ("Pure catabolism", "هدم فقط"), ("Photosynthesis", "البناء الضوئي")), "a"),
 Q("In stage II of energy generation, building blocks are degraded to:", "في المرحلة الثانية من توليد الطاقة تتحلّل الوحدات البنائية إلى:", O(("CO2 and water", "CO2 والماء"), ("Acetyl-CoA", "الأسيتيل-CoA"), ("Glycogen", "الغلايكوجين"), ("Amino acids", "الأحماض الأمينية")), "b"),
 {"topic_en": "Bioenergetics and thermodynamics", "topic_ar": "الطاقة الحيوية والديناميكا الحرارية"},
 Q("Bioenergetics is the study of:", "الطاقة الحيوية هي دراسة:", O(("Enzyme structure", "تركيب الإنزيمات"), ("Cell division", "انقسام الخلية"), ("The energy changes accompanying biochemical reactions", "تغيّرات الطاقة المرافقة للتفاعلات الكيموحيوية"), ("Blood groups", "فصائل الدم")), "c"),
 Q("Biologic systems are essentially:", "الأنظمة الحيوية أساسًا:", O(("Using heat to do work", "تستعمل الحرارة لإنجاز الشغل"), ("Without energy", "بلا طاقة"), ("Always at 100 °C", "دائمًا بدرجة 100 °م"), ("Iso-thermic, using chemical energy", "متساوية الحرارة وتستعمل الطاقة الكيميائية")), "d"),
 Q("Malnutrition with energy imbalance is called:", "سوء التغذية مع اختلال توازن الطاقة يسمّى:", O(("Marasmus", "الهزال (marasmus)"), ("Obesity", "السمنة"), ("Hyperthyroidism", "فرط الدرقية"), ("Diabetes", "السكري")), "a"),
 Q("The rate of energy release (metabolic rate) is controlled by:", "يتحكّم بمعدّل تحرّر الطاقة (معدّل الأيض):", O(("Insulin only", "الأنسولين فقط"), ("Thyroid hormones", "هرمونات الدرقية"), ("Vitamin C", "فيتامين C"), ("Hemoglobin", "الهيموغلوبين")), "b"),
 Q("The first law of thermodynamics states that:", "ينصّ القانون الأول للديناميكا الحرارية على أن:", O(("Entropy always decreases", "الإنتروبيا تتناقص دائمًا"), ("Energy is lost in every change", "الطاقة تُفقد في كل تغيّر"), ("The total energy of a system and its surroundings remains constant", "الطاقة الكلية للنظام ومحيطه تبقى ثابتة"), ("ΔG is always zero", "ΔG دائمًا صفر")), "c"),
 Q("For a process to occur spontaneously, the total entropy must:", "لكي تحدث عملية تلقائيًا يجب أن تكون الإنتروبيا الكلية:", O(("Decrease", "تتناقص"), ("Stay zero", "تبقى صفرًا"), ("Be negative", "سالبة"), ("Increase", "تزداد")), "d"),
 Q("Entropy is:", "الإنتروبيا هي:", O(("The extent of disorder or randomness of a system", "درجة الفوضى أو العشوائية في النظام"), ("The heat content", "المحتوى الحراري"), ("The useful energy", "الطاقة المفيدة"), ("The absolute temperature", "درجة الحرارة المطلقة")), "a"),
 Q("∆H in the Gibbs equation is:", "∆H في معادلة جبس هو:", O(("Entropy change", "تغيّر الإنتروبيا"), ("Change in enthalpy (heat content)", "التغيّر في الإنثالبي (المحتوى الحراري)"), ("Free energy change", "تغيّر الطاقة الحرّة"), ("Temperature", "درجة الحرارة")), "b"),
 Q("In biochemical reactions, the Gibbs relationship is written as:", "في التفاعلات الكيموحيوية تُكتب علاقة جبس:", O(("∆G = ∆S − T∆E", "∆G = ∆S − T∆E"), ("∆G = T∆S", "∆G = T∆S"), ("∆G = ∆E − T∆S", "∆G = ∆E − T∆S"), ("∆G = ∆H + ∆S", "∆G = ∆H + ∆S")), "c"),
 {"topic_en": "Free energy change", "topic_ar": "تغيّر الطاقة الحرّة"},
 Q("If ΔG is negative, the reaction is:", "إذا كانت ΔG سالبة فالتفاعل:", O(("Endergonic, not spontaneous", "ماصّ للطاقة، غير تلقائي"), ("At equilibrium", "في حالة توازن"), ("Impossible", "مستحيل"), ("Exergonic and spontaneous", "طارد للطاقة وتلقائي")), "d"),
 Q("If ΔG is positive:", "إذا كانت ΔG موجبة:", O(("Energy must be added for the reaction to go", "يجب إضافة طاقة لسير التفاعل"), ("The reaction is spontaneous", "التفاعل تلقائي"), ("The system is at equilibrium", "النظام في توازن"), ("Heat is released", "تتحرّر حرارة")), "a"),
 Q("If ΔG is zero, the system is:", "إذا كانت ΔG صفرًا فالنظام:", O(("Exergonic", "طارد للطاقة"), ("At equilibrium with no net change", "في توازن بلا تغيّر صافٍ"), ("Endergonic", "ماصّ للطاقة"), ("Irreversible", "غير عكوس")), "b"),
 Q("A large negative ∆G means the reaction is:", "∆G سالبة كبيرة تعني أن التفاعل:", O(("At equilibrium", "في توازن"), ("Stable with no tendency to react", "مستقر بلا ميل للتفاعل"), ("Virtually complete and essentially irreversible", "يكتمل تقريبًا وغير عكوس أساسًا"), ("Endergonic", "ماصّ للطاقة")), "c"),
 Q("An enzyme:", "الإنزيم:", O(("Changes the final equilibrium concentrations", "يغيّر تراكيز التوازن النهائية"), ("Changes ΔG of the reaction", "يغيّر ΔG للتفاعل"), ("Makes endergonic reactions exergonic", "يجعل التفاعل الماصّ طاردًا"), ("Only speeds up the attainment of equilibrium", "يسرّع الوصول إلى التوازن فقط")), "d"),
 {"topic_en": "Energy coupling and ATP", "topic_ar": "اقتران الطاقة وATP"},
 Q("Exergonic and endergonic refer to loss or gain of:", "يشير طارد وماصّ للطاقة إلى فقدان أو اكتساب:", O(("Free energy in any form", "الطاقة الحرّة بأي شكل"), ("Heat only", "الحرارة فقط"), ("Water", "الماء"), ("Electrons only", "الإلكترونات فقط")), "a"),
 Q("A common obligatory intermediate (I) provides the basis for:", "يوفّر المركّب الوسطي الإلزامي المشترك (I) أساسًا لـ:", O(("Photosynthesis", "البناء الضوئي"), ("Respiratory control", "التحكّم التنفّسي"), ("Muscle contraction", "تقلّص العضلات"), ("Glycogen storage", "خزن الغلايكوجين")), "b"),
 Q("The principal high-energy carrier compound (∼E) in the living cell is:", "المركّب الناقل الرئيسي عالي الطاقة (∼E) في الخلية الحية:", O(("Glucose", "الغلوكوز"), ("NADH only", "NADH فقط"), ("ATP", "ATP"), ("AMP", "AMP")), "c"),
 Q("Glucose + Pi → Glucose 6-phosphate has ∆G0′ of:", "التفاعل `Glucose + Pi → Glucose 6-phosphate` له ∆G0′:", O(("−30.5 kJ/mol", "−30.5"), ("−13.8 kJ/mol", "−13.8"), ("−61.9 kJ/mol", "−61.9"), ("+13.8 kJ/mol", "+13.8")), "d"),
 Q("The enzyme coupling glucose phosphorylation with ATP hydrolysis is:", "الإنزيم الذي يقرن فسفرة الغلوكوز بتحلّل ATP:", O(("Hexokinase", "الهكسوكاينيز"), ("Adenylyl kinase", "الأدينيليل كاينيز"), ("Pyrophosphatase", "البايروفوسفاتيز"), ("Acyl-CoA synthetase", "أسيل-CoA سنثيتيز")), "a"),
 Q("The ∆G0′ of hydrolysis of ATP → ADP + Pi is:", "∆G0′ لتحلّل ATP → ADP + Pi:", O(("−61.9 kJ/mol", "−61.9"), ("−30.5 kJ/mol", "−30.5"), ("−13.8 kJ/mol", "−13.8"), ("+30.5 kJ/mol", "+30.5")), "b"),
 Q("The compound with the highest free energy of hydrolysis in the table is:", "المركّب ذو أعلى طاقة حرّة للتحلّل في الجدول:", O(("Creatine phosphate", "كرياتين فوسفات"), ("ATP", "ATP"), ("Phosphoenolpyruvate", "فوسفو إينول بايروفيت"), ("Glucose 6-phosphate", "غلوكوز 6-فوسفات")), "c"),
 Q("ATP contains:", "يحتوي ATP:", O(("Guanine, deoxyribose and two phosphates", "غوانين ورايبوز منقوص الأوكسجين وفوسفاتين"), ("Adenine, glucose and one phosphate", "أدينين وغلوكوز وفوسفات واحدة"), ("Cytosine and ribose", "سايتوسين ورايبوز"), ("Adenine, ribose and three phosphate groups", "أدينين ورايبوز وثلاث مجاميع فوسفات")), "d"),
 Q("In the cell, ATP functions as a complex with:", "في الخلية يعمل ATP على شكل معقّد مع:", O(("Mg²⁺", "Mg²⁺"), ("Fe²⁺", "Fe²⁺"), ("Na⁺", "Na⁺"), ("Cl⁻", "Cl⁻")), "a"),
 Q("The total ATP/ADP pool can maintain an active tissue for:", "يكفي مخزون ATP/ADP الكلي لإدامة نسيج نشط:", O(("Several days", "عدّة أيام"), ("Only a few seconds", "بضع ثوانٍ فقط"), ("One hour", "ساعة واحدة"), ("A week", "أسبوعًا")), "b"),
 Q("Organisms that obtain energy from sunlight or Fe²⁺ → Fe³⁺ are:", "الكائنات التي تحصل على الطاقة من الشمس أو Fe²⁺ → Fe³⁺ هي:", O(("Heterotrophic", "غيرية التغذية"), ("Parasitic", "متطفّلة"), ("Autotrophic", "ذاتية التغذية"), ("Anaerobic only", "لاهوائية فقط")), "c"),
 {"topic_en": "Picture questions", "topic_ar": "أسئلة الصور"},
 Q("In panel A of this figure, ΔG is:", "في اللوحة A من هذا الشكل، ΔG:", O(("Positive", "موجبة"), ("Zero", "صفر"), ("Not shown", "غير موضّحة"), ("Negative", "سالبة")), "d", img=A("dg-panels.png"), img_h="34mm"),
 Q("This figure (A + C → B + D + Heat) shows:", "يُظهر هذا الشكل (A + C → B + D + حرارة):", O(("Coupling of an exergonic to an endergonic reaction", "اقتران تفاعل طارد بتفاعل ماصّ للطاقة"), ("Enzyme inhibition", "تثبيط الإنزيم"), ("Michaelis-Menten kinetics", "حركيات ميكالس-منتن"), ("ATP structure", "تركيب ATP")), "a", img=A("coupling.png"), img_h="44mm"),
 Q("In this figure, the enzyme (catalysed reaction) lowers:", "في هذا الشكل، الإنزيم (التفاعل المحفَّز) يخفض:", O(("ΔG of the reaction", "ΔG للتفاعل"), ("The activation barrier (ΔG‡)", "حاجز التنشيط (ΔG‡)"), ("The energy of the products", "طاقة النواتج"), ("The equilibrium concentration", "تركيز التوازن")), "b", img=A("activation-barrier.png"), img_h="40mm"),
 Q("This structure is:", "هذا التركيب هو:", O(("ADP", "ADP"), ("AMP", "AMP"), ("MgATP²⁻", "MgATP²⁻"), ("Creatine phosphate", "كرياتين فوسفات")), "c", img=A("atp-structure.png"), img_h="22mm"),
]

tf = [
 TF("Anabolic reactions are endergonic.", "تفاعلات البناء ماصّة للطاقة.", "T"),
 TF("Catabolism forms complex end products from simple precursors.", "الهدم يكوّن نواتج معقّدة من سلائف بسيطة.", "F"),
 TF("Starvation causes death because animals obtain fuel from their food.", "التجويع يسبّب الموت لأن الحيوان يحصل على وقوده من غذائه.", "T"),
 TF("Excess storage of surplus energy causes obesity.", "الخزن الزائد للطاقة الفائضة يسبّب السمنة.", "T"),
 TF("According to the first law, energy is lost during chemical changes.", "حسب القانون الأول تُفقد الطاقة أثناء التغيّرات الكيميائية.", "F"),
 TF("Entropy becomes maximum as equilibrium is approached.", "تصل الإنتروبيا أقصاها عند الاقتراب من التوازن.", "T"),
 TF("T in the Gibbs equation is the temperature in °C.", "T في معادلة جبس هي درجة الحرارة بالمئوي.", "F"),
 TF("A positive ΔG reaction of great magnitude is stable with little tendency to react.", "التفاعل ذو ΔG موجبة كبيرة مستقر وميله للتفاعل قليل.", "T"),
 TF("An enzyme alters the final concentrations at equilibrium.", "الإنزيم يغيّر التراكيز النهائية عند التوازن.", "F"),
 TF("The ∼E compound must be structurally related to A, B, C or D.", "يجب أن يرتبط المركّب ∼E تركيبيًا بـ A أو B أو C أو D.", "F"),
 TF("Phosphorylation of glucose alone is highly endergonic.", "فسفرة الغلوكوز وحدها ماصّة للطاقة بشدّة.", "T"),
 TF("ATP can donate high-energy phosphate to compounds below it in the table.", "يستطيع ATP منح الفوسفات عالية الطاقة للمركّبات التي تحته في الجدول.", "T"),
 TF("The high free energy of ATP hydrolysis is partly due to relief of charge repulsion.", "الطاقة الحرّة العالية لتحلّل ATP تعود جزئيًا لزوال تنافر الشحنات.", "T"),
 TF("Heterotrophic organisms use sunlight directly.", "الكائنات غيرية التغذية تستعمل ضوء الشمس مباشرةً.", "F"),
]

traps = [
 TR("Exergonic vs exothermic — same thing?", "طارد للطاقة مقابل طارد للحرارة — نفس الشيء؟",
    "No — exergonic/endergonic refer to free energy in any form, not necessarily heat.", "لا — exergonic/endergonic تعني الطاقة الحرّة بأي شكل، وليس بالضرورة حرارة."),
 TR("Does an enzyme change ΔG?", "هل يغيّر الإنزيم ΔG؟",
    "No — it lowers the activation barrier and speeds reaching equilibrium; ΔG and the equilibrium concentrations stay the same.", "لا — يخفض حاجز التنشيط ويسرّع الوصول للتوازن؛ وتبقى ΔG وتراكيز التوازن نفسها."),
 TR("Negative ΔG large vs positive ΔG large?", "ΔG سالبة كبيرة مقابل موجبة كبيرة؟",
    "Large negative → goes to completion, irreversible; large positive → stable, little or no tendency to react.", "سالبة كبيرة ← يكتمل وغير عكوس؛ موجبة كبيرة ← مستقر وميله قليل أو معدوم."),
 TR("Is ATP the compound with the highest energy of hydrolysis?", "هل ATP صاحب أعلى طاقة تحلّل؟",
    "No — it is intermediate (−30.5 kJ/mol); PEP (−61.9) and creatine phosphate (−43.1) are higher.", "لا — هو وسطي (−30.5)؛ وPEP (−61.9) وكرياتين فوسفات (−43.1) أعلى منه."),
 TR("Common intermediate (I) vs ∼E?", "المركّب الوسطي (I) مقابل ∼E؟",
    "I takes part in both reactions (respiratory control); ∼E (ATP) need not be structurally related to the reactants, so it links many reactions.", "I يشترك في التفاعلين (التحكّم التنفّسي)؛ و∼E (ATP) لا يلزم أن يرتبط تركيبيًا بالمتفاعلات فيربط تفاعلات كثيرة."),
 TR("Catabolism and anabolism — which is exergonic?", "الهدم والبناء — أيّهما طارد للطاقة؟",
    "Catabolism is exergonic (degradative); anabolism is endergonic (synthetic).", "الهدم طارد للطاقة (تكسيري)؛ والبناء ماصّ للطاقة (تركيبي)."),
]

important = [
 IM("Define metabolism, pathways and metabolites.", "عرّف الأيض والمسارات والمستقلبات.",
    "Metabolism: the collective of different intersecting pathways forming an integrated network of chemical reactions — the sum of all chemical changes in a cell, tissue or body. Pathways: multistep sequences of enzymatic reactions in which the product of one reaction is the substrate of the next. Metabolites: the series of intermediates through which a precursor is converted into a product.",
    "الأيض: مجموع المسارات المتقاطعة المكوّنة لشبكة متكاملة من التفاعلات الكيميائية — مجموع كل التغيّرات الكيميائية في الخلية أو النسيج أو الجسم. المسارات: سلاسل متعدّدة الخطوات من التفاعلات الإنزيمية يكون فيها ناتج التفاعل مادة أساس للتالي. المستقلبات: سلسلة المركّبات الوسطية التي تتحوّل عبرها السليفة إلى ناتج."),
 IM("Classify metabolism with examples.", "صنّف الأيض مع الأمثلة.",
    "Catabolism (degradative, exergonic): breaks complex molecules (polysaccharides, lipids, proteins) to CO2, NH3 and water. Anabolism (synthetic, endergonic): forms complex products from simple precursors, e.g. glycogen from glucose. Amphibolic pathways: at the crossroads, linking both, e.g. the citric acid cycle.",
    "الهدم (تكسيري، طارد للطاقة): يكسّر الجزيئات المعقّدة إلى CO2 وNH3 والماء. البناء (تركيبي، ماصّ للطاقة): يكوّن نواتج معقّدة من سلائف بسيطة، مثل الغلايكوجين من الغلوكوز. المسارات المزدوجة: عند مفترق الطرق وتربط الاثنين، مثل دورة حامض الستريك."),
 IM("State the two laws of thermodynamics and the Gibbs equation.", "اذكر قانوني الديناميكا الحرارية ومعادلة جبس.",
    "First law: the total energy of a system and its surroundings remains constant (not lost or gained). Second law: total entropy must increase for a spontaneous process; entropy = disorder, maximal at equilibrium. Gibbs: ∆G = ∆H − T∆S (∆H enthalpy, T absolute temperature = °C + 273); in biochemistry ∆G = ∆E − T∆S.",
    "القانون الأول: الطاقة الكلية للنظام ومحيطه ثابتة (لا تُفقد ولا تُكتسب). القانون الثاني: يجب أن تزداد الإنتروبيا الكلية لكي تحدث العملية تلقائيًا؛ والإنتروبيا = الفوضى وأقصاها عند التوازن. جبس: ∆G = ∆H − T∆S (∆H الإنثالبي، T الحرارة المطلقة = °م + 273)؛ وفي الكيمياء الحيوية ∆G = ∆E − T∆S."),
 IM("How does the sign of ΔG predict the direction of a reaction?", "كيف تتنبّأ إشارة ΔG باتجاه التفاعل؟",
    "Negative ΔG: net loss of energy, spontaneous A → B, exergonic; if large, goes to completion and irreversible. Positive ΔG: net gain, not spontaneous, endergonic, energy must be added; if large, the system is stable. ΔG = 0: equilibrium, no net change. An enzyme only speeds reaching equilibrium.",
    "ΔG سالبة: فقدان صافٍ للطاقة، تفاعل تلقائي `A → B` طارد للطاقة؛ وإذا كانت كبيرة يكتمل ويكون غير عكوس. ΔG موجبة: اكتساب صافٍ، غير تلقائي، ماصّ للطاقة، يلزم إضافة طاقة؛ وإذا كانت كبيرة يكون النظام مستقرًا. ΔG = 0: توازن بلا تغيّر صافٍ. والإنزيم يسرّع الوصول للتوازن فقط."),
 IM("Explain the two mechanisms of energy coupling with examples.", "اشرح آليتي اقتران الطاقة مع الأمثلة.",
    "1. Common obligatory intermediate (I): A + C → I → B + D; controls the rate of oxidation (respiratory control); e.g. dehydrogenation coupled to hydrogenation by a carrier. 2. A high-energy compound (∼E = ATP) made in the exergonic reaction and used in the endergonic one; not structurally related to the reactants, so it links many reactions (biosynthesis, muscle contraction, nerve excitation, active transport). Example: glucose + Pi → G6P (+13.8 kJ/mol) coupled with ATP → ADP + Pi (−30.5) by hexokinase → irreversible.",
    "1. المركّب الوسطي الإلزامي المشترك (I): A + C → I → B + D؛ يتحكّم بسرعة الأكسدة (التحكّم التنفّسي)؛ مثل نزع الهيدروجين المقترن بالهدرجة عبر ناقل. 2. مركّب عالي الطاقة (∼E = ATP) يُصنع في التفاعل الطارد ويُستعمل في الماصّ؛ لا يرتبط تركيبيًا بالمتفاعلات فيربط تفاعلات كثيرة (البناء الحيوي، تقلّص العضلات، التهيّج العصبي، النقل الفعّال). مثال: `Glucose + Pi → G6P (+13.8)` مقترنًا بتحلّل `ATP → ADP + Pi (−30.5)` بواسطة الهكسوكاينيز ← غير عكوس."),
 IM("Write about ATP: its role, composition and high free energy.", "اكتب عن ATP: دوره وتركيبه وطاقته الحرّة العالية.",
    "ATP is the principal high-energy carrier; energy from the sun or nutrient oxidation is converted to ATP. Its hydrolysis (−30.5 kJ/mol) is intermediate in the table, so it donates phosphate to compounds below it and receives from those above (ATP/ADP cycle). It is a nucleoside triphosphate (adenine, ribose, three phosphates) acting as the Mg²⁺ complex. Its high free energy comes from relief of charge repulsion and resonance stabilization of the products. The ATP/ADP pool lasts only a few seconds, so it turns over very rapidly.",
    "ATP هو الناقل الرئيسي عالي الطاقة؛ وتتحوّل طاقة الشمس أو أكسدة الغذاء إلى ATP. تحلّله (−30.5) وسطي في الجدول، فيمنح الفوسفات لما تحته ويستقبل ممّا فوقه (دورة ATP/ADP). وهو نيوكليوسيد ثلاثي الفوسفات (أدينين، رايبوز، ثلاث فوسفات) يعمل كمعقّد مع Mg²⁺. وطاقته العالية من زوال تنافر الشحنات واستقرار النواتج بالرنين. ومخزون ATP/ADP يكفي ثوانٍ فقط فيتجدّد بسرعة كبيرة."),
]

import re as _re
_RUN = _re.compile(r"[A-Za-z0-9\[₀-₉⁰-⁹¹²³∆Δ∼(+−][A-Za-z0-9\[\]₀-₉⁰-⁹¹²³⁺⁻∆Δ∼′‡×−+/=.()·→⇄ ]*[A-Za-z0-9\]₀-₉⁰-⁹¹²³⁺⁻′‡)]")
def _ltr(s):
    """Formulas (with = or an arrow) inside Arabic text go in LTR runs."""
    return _RUN.sub(lambda m: "`" + m.group(0) + "`" if _re.search(r"[=→⇄]", m.group(0)) else m.group(0), s)
for _q in mcq:
    if "ar" in _q:
        _q["ar"] = _ltr(_q["ar"]); _q["options"] = [[o[0], _ltr(o[1])] for o in _q["options"]]
for _q in tf + traps:
    _q["ar"] = _ltr(_q["ar"])
for _q in traps + important:
    _q["answer_ar"] = _ltr(_q["answer_ar"])

meta = {"subject_en": "Clinical Enzymology", "subject_ar": "الإنزيمات السريرية", "short_ar": "انزيمات سريرية", "instructor": "د. وليد مجيد",
        "unit_en": "Lecture 4", "unit_ar": "المحاضرة 4", "unit_label": "LEC", "unit_no": "4",
        "title_en": "Enzyme Bioenergetics", "title_ar": "الطاقة الحيوية للإنزيمات",
        "department": "قسم التحليلات", "stage": "The fourth stage — الرابعة", "kind": "Theory — نظري"}
save("enzymology-lec4-bioenergetics", meta, blocks, balance(mcq, 9), tf, traps, important)

```
