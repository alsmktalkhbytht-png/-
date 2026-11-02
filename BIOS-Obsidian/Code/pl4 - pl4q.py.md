---
source: BIOS-Obsidian/tools/scripts/pl4/pl4q.py
handouts: [parasitology-lab4-nonpathogenic-amoebae]
saved: 2026-11-02
tags: [bios, code]
---
# pl4/pl4q.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#parasitology-lab4-nonpathogenic-amoebae|parasitology-lab4-nonpathogenic-amoebae]]

```python
A = lambda f: "assets/" + f
mcq = [
 {"topic_en": "Entamoeba coli", "topic_ar": "الأميبا القولونية"},
 Q("Which of the following is a non-pathogenic amoeba?", "أيّ مما يأتي أميبا غير ممرضة؟", O(("E. coli", "الأميبا القولونية"), ("E. histolytica", "الأميبا الحالّة للنسيج"), ("Naegleria fowleri", "النيغلرية الفاولرية"), ("None of them", "لا شيء منها")), "a"),
 Q("The trophozoite of E. coli measures:", "يبلغ الطور المتغذّي للأميبا القولونية:", O(("5- 25 µm", "5- 25 مايكرومتر"), ("15- 50 µm", "15- 50 مايكرومتر"), ("6–12 µm", "6–12 مايكرومتر"), ("8–15 µm", "8–15 مايكرومتر")), "b"),
 Q("The karyosome of the E. coli trophozoite is:", "الجسيم النووي للطور المتغذّي للأميبا القولونية:", O(("Small & central", "صغير ومركزي"), ("Absent", "غائب"), ("Large & eccentric", "كبير ولا مركزي"), ("Half the nucleus (bull's eye)", "بنصف النواة (عين الثور)")), "c"),
 Q("The mature cyst of E. coli has:", "للكيس الناضج للأميبا القولونية:", O(("1 nucleus", "نواة واحدة"), ("2 nuclei", "نواتان"), ("4 nuclei", "4 أنوية"), ("8 nuclei", "8 أنوية")), "d"),
 Q("The chromatoid body of E. coli is:", "الجسم الكروماتيني للأميبا القولونية:", O(("Filamentous / splinter shape", "خيطي / شظوي"), ("Cigar-shaped", "سيجاري"), ("Absent", "غائب"), ("Iodophilic", "محبّ لليود")), "a"),
 Q("The location of E. coli in the definitive host is:", "موقع الأميبا القولونية في المضيف النهائي:", O(("The liver", "الكبد"), ("Cecum and large intestine", "الأعور والأمعاء الغليظة"), ("The mouth", "الفم"), ("The brain", "الدماغ")), "b"),
 Q("The food vacuoles of E. coli contain:", "تحتوي الفجوات الغذائية للأميبا القولونية:", O(("RBCs in acute cases", "كريات حمر في الحالات الحادّة"), ("Leukocytes and epithelial cells", "كريات بيض وخلايا ظهارية"), ("Bacteria, yeast & other particles without RBC", "بكتيريا وخمائر ودقائق أخرى بلا كريات حمر"), ("Nothing", "لا شيء")), "c"),
 Q("The presence of E. coli in stool is evidence that the host:", "وجود الأميبا القولونية في البراز دليل على أن المضيف:", O(("Has amoebic dysentery", "مصاب بالزحار الأميبي"), ("Has a liver abscess", "مصاب بخرّاج الكبد"), ("Swam in warm water", "سبح في ماء دافئ"), ("Has ingested fecal material", "ابتلع مادة برازية")), "d"),
 Q("E. coli cysts are found in the laboratory by:", "يُعثر على أكياس الأميبا القولونية في المختبر بـ:", O(("Iodine stained, formol-ether concentration method", "التحضير المصبوغ باليود وطريقة التركيز بالفورمول-إيثر"), ("CSF wet mount", "تحضير رطب للسائل الدماغي الشوكي"), ("Gum scrapings", "كشط اللثة"), ("Culture on nonnutrient agar", "الزرع على أكار غير مغذٍّ")), "a"),
 Q("In the comparison table, the cyst diameter of E. histolytica is:", "في جدول المقارنة، قطر كيس الأميبا الحالّة للنسيج:", O(("10-30 mµ", "10-30"), ("10-15 mµ", "10-15"), ("20-50 mµ", "20-50"), ("5- 14 µm", "5- 14")), "b"),
 Q("Ectoplasm clearly differentiated from endoplasm is a feature of:", "الإكتوبلازم المتميّز بوضوح عن الإندوبلازم صفة لـ:", O(("E. coli", "الأميبا القولونية"), ("Endolimax nana", "الأميبا القزمة"), ("E. histolytica", "الأميبا الحالّة للنسيج"), ("Iodamoeba", "الأميبا اليودية")), "c"),
 {"topic_en": "Entamoeba gingivalis", "topic_ar": "الأميبا اللثوية"},
 Q("The first amoeba of man to be described was:", "أول أميبا وُصفت في الإنسان هي:", O(("E. coli", "الأميبا القولونية"), ("Endolimax nana", "الأميبا القزمة"), ("Naegleria fowleri", "النيغلرية الفاولرية"), ("E. gingivalis", "الأميبا اللثوية")), "d"),
 Q("Which stage of E. gingivalis has been found?", "أيّ طور من الأميبا اللثوية عُثر عليه؟", O(("Only the trophozoite", "الطور المتغذّي فقط"), ("Only the cyst", "الكيس فقط"), ("Trophozoite and cyst", "المتغذّي والكيس"), ("Pre-cyst and cyst", "ما قبل الكيس والكيس")), "a"),
 Q("E. gingivalis is transmitted by:", "تنتقل الأميبا اللثوية بـ:", O(("Contaminated water", "الماء الملوّث"), ("Direct oral contact (kissing)", "التماس الفموي المباشر (التقبيل)"), ("Inhalation during swimming", "الاستنشاق أثناء السباحة"), ("Insect bite", "لدغة حشرة")), "b"),
 Q("The prevalence of E. gingivalis in those with diseased teeth and gum reaches:", "تصل نسبة انتشار الأميبا اللثوية في المصابين بأمراض الأسنان واللثة إلى:", O(("10%", "10%"), ("20%", "20%"), ("95%", "95%"), ("50%", "50%")), "c"),
 Q("The food vacuoles of E. gingivalis contain:", "تحتوي الفجوات الغذائية للأميبا اللثوية:", O(("Bacteria only", "بكتيريا فقط"), ("Glycogen", "غلايكوجين"), ("Yeast only", "خمائر فقط"), ("Leukocytes, epithelial cells and red blood cells", "كريات بيض وخلايا ظهارية وكريات حمر")), "d"),
 Q("E. gingivalis is diagnosed by finding trophozoites in:", "تُشخَّص الأميبا اللثوية بإيجاد الأطوار المتغذّية في:", O(("Scrapings of the gums and teeth", "كشط اللثة والأسنان"), ("Stool concentration", "تركيز البراز"), ("CSF", "السائل الدماغي الشوكي"), ("Blood film", "مسحة الدم")), "a"),
 {"topic_en": "Endolimax nana and Iodamoeba", "topic_ar": "الأميبا القزمة والأميبا اليودية"},
 Q("The habitat of Endolimax nana is:", "موطن الأميبا القزمة:", O(("Gingival tissue", "النسيج اللثوي"), ("Lumen of large intestine", "تجويف الأمعاء الغليظة"), ("Brain", "الدماغ"), ("Liver", "الكبد")), "b"),
 Q("The cyst of Endolimax nana is:", "كيس الأميبا القزمة:", O(("Spherical with 8 nuclei", "كروي بـ8 أنوية"), ("Oval with 1 nucleus", "بيضوي بنواة واحدة"), ("Oval, 5- 14 µm, with 4 indistinct nuclei", "بيضوي، 5- 14 مايكرومتر، بـ4 أنوية غير واضحة"), ("Absent", "غائب")), "c"),
 Q("In Endolimax nana, which are absent?", "في الأميبا القزمة، أيّها غائب؟", O(("Nucleus", "النواة"), ("Cytoplasm", "السايتوبلازم"), ("Pseudopodia", "الأقدام الكاذبة"), ("Chromatoid bars and glycogen vacuole", "القضبان الكروماتينية وفجوة الغلايكوجين")), "d"),
 Q("Endolimax nana has how many stages?", "كم طورًا للأميبا القزمة؟", O(("3: trophozoite, pre-cyst and cyst", "3: المتغذّي وما قبل الكيس والكيس"), ("1: trophozoite only", "1: المتغذّي فقط"), ("2: amoeboid and flagellated", "2: الأميبي والمسوط"), ("4", "4")), "a"),
 Q("The name ‘Iodamoeba’ comes from:", "اسم ‘الأميبا اليودية’ جاء من:", O(("Its iodine requirement", "حاجتها لليود"), ("A glycogen mass that stains with iodine (iodophilic body)", "كتلة غلايكوجين تتصبّغ باليود (الجسم المحبّ لليود)"), ("Its discoverer", "مكتشفها"), ("Its 8 nuclei", "أنويتها الثماني")), "b"),
 Q("The cyst of Iodamoeba buetschlii is:", "كيس أميبا بوتشلي اليودية:", O(("Spherical with 8 nuclei", "كروي بـ8 أنوية"), ("Oval with 4 indistinct nuclei", "بيضوي بـ4 أنوية غير واضحة"), ("Oval and uninucleate", "بيضوي أحادي النواة"), ("Absent", "غائب")), "c"),
 {"topic_en": "Naegleria fowleri", "topic_ar": "النيغلرية الفاولرية"},
 Q("Naegleria fowleri is typically found in:", "توجد النيغلرية الفاولرية عادةً في:", O(("Sea water", "ماء البحر"), ("The human mouth", "فم الإنسان"), ("Cold water only", "الماء البارد فقط"), ("Warm fresh water", "المياه العذبة الدافئة")), "d"),
 Q("N. fowleri is also known as:", "تُعرف النيغلرية الفاولرية أيضًا بـ:", O(("The brain-eating amoeba", "الأميبا آكلة الدماغ"), ("The gum amoeba", "أميبا اللثة"), ("The iodine amoeba", "الأميبا اليودية"), ("The dwarf amoeba", "الأميبا القزمة")), "a"),
 Q("The only recognizable form of N. fowleri in humans is:", "الشكل الوحيد المعروف للنيغلرية الفاولرية في الإنسان:", O(("The cyst", "الكيس"), ("The amoeboid form", "الشكل الأميبي"), ("The flagellated form", "الشكل المسوط"), ("The pre-cyst", "ما قبل الكيس")), "b"),
 Q("The amoeboid and flagellated trophozoites of N. fowleri measure:", "تبلغ الأطوار المتغذّية الأميبية والمسوطة للنيغلرية:", O(("15- 50 µm", "15- 50 مايكرومتر"), ("5- 14 µm", "5- 14 مايكرومتر"), ("8–15 µm", "8–15 مايكرومتر"), ("20-50 µm", "20-50 مايكرومتر")), "c"),
 Q("Humans are infected with N. fowleri by:", "يُصاب الإنسان بالنيغلرية الفاولرية عن طريق:", O(("Eating contaminated food", "أكل طعام ملوّث"), ("Kissing", "التقبيل"), ("Mosquito bite", "لدغة البعوض"), ("Inhalation during swimming", "الاستنشاق أثناء السباحة")), "d"),
 Q("The CSF in N. fowleri infection shows:", "يُظهر السائل الدماغي الشوكي في إصابة النيغلرية:", O(("Thick purulent CSF, PMN > 20,000/µl, ↑ protein, ↓ sugar", "سائل قيحي سميك، متعدّدة النوى > 20,000، ↑ البروتين، ↓ السكر"), ("Clear CSF with normal sugar", "سائل صافٍ وسكر طبيعي"), ("Lymphocytes only", "خلايا لمفية فقط"), ("Blood only", "دم فقط")), "a"),
 Q("A counting chamber is not used for N. fowleri in CSF because:", "لا تُستعمل حجرة العدّ للنيغلرية في السائل الدماغي الشوكي لأن:", O(("They are too large", "حجمها كبير جدًا"), ("Trophozoites in CSF mimic leucocytes", "الأطوار المتغذّية في السائل تحاكي كريات البيض"), ("They die in the chamber", "تموت في الحجرة"), ("They are flagellated", "مسوطة")), "b"),
 Q("If the parasite load in CSF is low, the CSF is:", "إذا كان حمل الطفيلي في السائل قليلًا فإن السائل:", O(("Refrigerated", "يُبرَّد"), ("Discarded", "يُهمل"), ("Centrifuged at low speed (150 rpm for 5 minutes)", "يُنبذ بسرعة منخفضة (150 دورة/دقيقة لمدة 5 دقائق)"), ("Frozen", "يُجمَّد")), "c"),
 Q("The culture of N. fowleri on nonnutrient agar with an E. coli lawn gives:", "زرع النيغلرية على أكار غير مغذٍّ مع مزرعة إشريكية مفروشة يعطي:", O(("Bull's eye sign", "علامة عين الثور"), ("Colonies with metallic sheen", "مستعمرات ببريق معدني"), ("No growth", "لا نمو"), ("Trail sign", "علامة المسار")), "d"),
 {"topic_en": "Picture questions", "topic_ar": "أسئلة الصور"},
 Q("This cyst with 8 nuclei belongs to:", "هذا الكيس ذو الأنوية الثماني يعود إلى:", O(("Entamoeba coli", "الأميبا القولونية"), ("Endolimax nana", "الأميبا القزمة"), ("Iodamoeba buetschlii", "أميبا بوتشلي اليودية"), ("E. histolytica", "الأميبا الحالّة للنسيج")), "a", img=A("ecoli-cyst-diagram.jpg"), img_h="36mm"),
 Q("This trophozoite with phagocytosed host leukocytes, from the mouth, is:", "هذا الطور المتغذّي المبتلع لكريات بيض المضيف، من الفم، هو:", O(("E. coli", "الأميبا القولونية"), ("E. gingivalis", "الأميبا اللثوية"), ("Naegleria fowleri", "النيغلرية الفاولرية"), ("Endolimax nana", "الأميبا القزمة")), "b", img=A("eging-troph.jpg"), img_h="38mm"),
 Q("The large glycogen vacuole in this uninucleate cyst identifies:", "فجوة الغلايكوجين الكبيرة في هذا الكيس أحادي النواة تدلّ على:", O(("E. coli", "الأميبا القولونية"), ("Endolimax nana", "الأميبا القزمة"), ("Iodamoeba buetschlii", "أميبا بوتشلي اليودية"), ("E. gingivalis", "الأميبا اللثوية")), "c", img=A("iod-figure.jpg"), img_h="40mm"),
 Q("This figure shows (A) the vegetative form and (B) the quadrinucleate cyst of:", "يُظهر الشكل (A) الطور الخضري و(B) الكيس رباعي الأنوية لـ:", O(("E. coli", "الأميبا القولونية"), ("Iodamoeba", "الأميبا اليودية"), ("E. gingivalis", "الأميبا اللثوية"), ("Endolimax nana", "الأميبا القزمة")), "d", img=A("enana-fig-ab.jpg"), img_h="36mm"),
 Q("This diagram shows the life cycle of:", "يُظهر هذا المخطط دورة حياة:", O(("Naegleria fowleri", "النيغلرية الفاولرية"), ("E. coli", "الأميبا القولونية"), ("E. gingivalis", "الأميبا اللثوية"), ("Endolimax nana", "الأميبا القزمة")), "a", img=A("naeg-cycle.jpg"), img_h="48mm"),
 Q("The three forms in this figure (amoeboid, flagellated, cyst) belong to:", "الأشكال الثلاثة في هذا الشكل (أميبي، مسوط، كيس) تعود إلى:", O(("Iodamoeba", "الأميبا اليودية"), ("Naegleria fowleri", "النيغلرية الفاولرية"), ("E. coli", "الأميبا القولونية"), ("E. gingivalis", "الأميبا اللثوية")), "b", img=A("naeg-forms.jpg"), img_h="30mm"),
]

tf = [
 TF("E. coli has an invasive stage.", "للأميبا القولونية طور غازٍ.", "F"),
 TF("The cyst of E. coli is usually larger than that of E. histolytica.", "كيس الأميبا القولونية عادةً أكبر من كيس الأميبا الحالّة للنسيج.", "T"),
 TF("E. coli has an intermediate host.", "للأميبا القولونية مضيف وسطي.", "F"),
 TF("The trophozoite of E. coli does not attack the intestinal mucosa.", "الطور المتغذّي للأميبا القولونية لا يهاجم الغشاء المخاطي للأمعاء.", "T"),
 TF("The chromatin bodies of E. histolytica are splinter shaped.", "الأجسام الكروماتينية للأميبا الحالّة للنسيج شظوية الشكل.", "F"),
 TF("E. gingivalis never goes out to the external environment.", "الأميبا اللثوية لا تخرج أبدًا إلى البيئة الخارجية.", "T"),
 TF("E. gingivalis has a central karyosome.", "للأميبا اللثوية جسيم نووي مركزي.", "T"),
 TF("E. gingivalis may be found in cervical smears from women using intrauterine devices.", "قد توجد الأميبا اللثوية في مسحات عنق الرحم للنساء المستعملات لوسائل منع الحمل داخل الرحم.", "T"),
 TF("Endolimax nana has chromatoid bars in its cyst.", "لكيس الأميبا القزمة قضبان كروماتينية.", "F"),
 TF("Iodamoeba buetschlii is more common than E. coli.", "أميبا بوتشلي اليودية أكثر شيوعًا من الأميبا القولونية.", "F"),
 TF("The cyst of Iodamoeba is uninucleate.", "كيس الأميبا اليودية أحادي النواة.", "T"),
 TF("Only N. fowleri among Naegleria species is known to cause infection in man.", "النيغلرية الفاولرية وحدها من أنواع النيغلرية معروفة بأنها تسبّب الإصابة في الإنسان.", "T"),
 TF("The flagellated form of N. fowleri is the only replicating form.", "الشكل المسوط للنيغلرية هو الشكل الوحيد المتكاثر.", "F"),
 TF("Refrigeration of CSF is recommended if examination is delayed.", "يُنصح بتبريد السائل الدماغي الشوكي إذا تأخّر فحصه.", "F"),
 TF("Phase contrast microscope gives better results than light microscope for N. fowleri.", "مجهر التباين الطوري يعطي نتائج أفضل من المجهر الضوئي للنيغلرية.", "T"),
 TF("In Wright's or Giemsa stain, N. fowleri trophozoites show sky blue cytoplasm with a pink nucleus.", "في صبغة رايت أو كيمزا تُظهر أطوار النيغلرية سايتوبلازم أزرق سماوي ونواة وردية.", "T"),
]

traps = [
 TR("E. coli cyst vs E. histolytica cyst — how many nuclei?", "كيس القولونية مقابل كيس الحالّة للنسيج — كم نواة؟",
    "E. coli: 8 nuclei; E. histolytica: 4 nuclei.", "القولونية: 8 أنوية؛ الحالّة للنسيج: 4 أنوية."),
 TR("Chromatoid bodies: cigar or splinter?", "الأجسام الكروماتينية: سيجارية أم شظوية؟",
    "E. histolytica: 1-4, cigar-shape; E. coli: 10-15, splinter shape (filamentous).", "الحالّة للنسيج: 1-4 سيجارية؛ القولونية: 10-15 شظوية (خيطية)."),
 TR("Karyosome: E. coli vs E. gingivalis?", "الجسيم النووي: القولونية مقابل اللثوية؟",
    "E. coli: large & eccentric; E. gingivalis: central.", "القولونية: كبير ولا مركزي؛ اللثوية: مركزي."),
 TR("Which amoeba eats RBCs besides E. histolytica in this lab?", "أيّ أميبا تأكل كريات حمرًا غير الحالّة للنسيج في هذا العملي؟",
    "E. gingivalis (leukocytes, epithelial cells and red blood cells); E. coli does not ingest RBCs.", "الأميبا اللثوية (كريات بيض وخلايا ظهارية وكريات حمر)؛ أما القولونية فلا تبتلع الكريات الحمر."),
 TR("Endolimax nana cyst vs Iodamoeba cyst?", "كيس القزمة مقابل كيس اليودية؟",
    "E. nana: oval, 4 indistinct nuclei, no glycogen vacuole; Iodamoeba: oval, 1 nucleus, big iodophilic glycogen mass.", "القزمة: بيضوي، 4 أنوية غير واضحة، بلا فجوة غلايكوجين؛ اليودية: بيضوي، نواة واحدة، كتلة غلايكوجين كبيرة محبّة لليود."),
 TR("E. coli in the Naegleria culture — the amoeba?", "الـ E. coli في زرع النيغلرية — هل هي الأميبا؟",
    "No — it is the bacterium (Escherichia coli) used as a lawn for Naegleria to feed on.", "لا — هي البكتيريا (الإشريكية القولونية) المفروشة لتتغذّى عليها النيغلرية."),
 TR("Which form of N. fowleri is seen in CSF?", "أيّ شكل من النيغلرية يُرى في السائل الدماغي الشوكي؟",
    "Only the motile amoeboid trophozoite; other forms are not seen in CSF.", "الطور المتغذّي الأميبي المتحرّك فقط؛ والأشكال الأخرى لا تُرى في السائل."),
]

important = [
 IM("Compare E. histolytica and E. coli.", "قارن بين الأميبا الحالّة للنسيج والأميبا القولونية.",
    "Disease: amoebiasis vs non pathogenic. Motility: active vs sluggish. Size: 10-40 vs 20-50 µm. Cytoplasm: ectoplasm clearly vs not clearly differentiated. Food vacuole: RBCs in acute cases vs bacteria, yeast without RBCs. Karyosome: small & central vs large & eccentric. Cyst: 10-15 vs 10-30 µm; 4 vs 8 nuclei; chromatin bodies 1-4 cigar-shape vs 10-15 splinter shape.",
    "المرض: داء الأميبات مقابل غير ممرضة. الحركة: نشطة مقابل بطيئة. الحجم: 10-40 مقابل 20-50 مايكرومتر. السايتوبلازم: الإكتوبلازم متميّز بوضوح مقابل غير متميّز. الفجوة الغذائية: كريات حمر في الحالات الحادّة مقابل بكتيريا وخمائر بلا كريات حمر. الجسيم النووي: صغير مركزي مقابل كبير لا مركزي. الكيس: 10-15 مقابل 10-30 مايكرومتر؛ 4 مقابل 8 أنوية؛ أجسام كروماتينية 1-4 سيجارية مقابل 10-15 شظوية."),
 IM("Write the general information of Entamoeba coli.", "اكتب المعلومات العامة عن الأميبا القولونية.",
    "Definitive host: humans; intermediate host: none; transmission: ingestion of contaminated food and water; location: cecum and large intestine; pathology and treatment: none — harmless commensal feeding on bacteria, yeast and wastes; diagnosis: distinguish it from E. histolytica (8 nuclei in cyst vs 4, different shape nuclei).",
    "المضيف النهائي: الإنسان؛ المضيف الوسطي: لا يوجد؛ الانتقال: ابتلاع طعام وماء ملوّثين؛ الموقع: الأعور والأمعاء الغليظة؛ الإمراضية والعلاج: لا يوجد — متعايش غير ضار يتغذّى على البكتيريا والخمائر والفضلات؛ التشخيص: تمييزها عن الحالّة للنسيج (8 أنوية في الكيس مقابل 4، وأنوية مختلفة الشكل)."),
 IM("How is E. coli diagnosed in the laboratory?", "كيف تُشخَّص الأميبا القولونية في المختبر؟",
    "By finding the characteristic cysts in an iodine stained, formol-ether concentration method, or by detecting the characteristic trophozoites in a wet preparation or a permanent stained preparation.",
    "بإيجاد الأكياس المميّزة في تحضير مصبوغ باليود أو بطريقة التركيز بالفورمول-إيثر، أو بالكشف عن الأطوار المتغذّية المميّزة في تحضير رطب أو تحضير مصبوغ دائم."),
 IM("Write short notes on Entamoeba gingivalis.", "اكتب ملاحظات قصيرة عن الأميبا اللثوية.",
    "First amoeba of man described (Gros, 1849); only the trophozoite (5-25 µm, actively motile, central karyosome, food vacuoles with leukocytes, epithelial cells and RBCs); lives in gingival tissue between teeth and gum; transmitted by direct oral contact (kissing) and contaminated utensils; prevalence 10% in healthy mouths to 95% with diseased teeth and gum; also in diseased tonsils and vaginal/cervical smears of IUD users; diagnosis: trophozoites in scrapings of gums and teeth.",
    "أول أميبا وُصفت في الإنسان (Gros، 1849)؛ طور متغذّي فقط (5-25 مايكرومتر، نشط الحركة، جسيم نووي مركزي، فجوات غذائية فيها كريات بيض وخلايا ظهارية وكريات حمر)؛ تعيش في النسيج اللثوي بين الأسنان واللثة؛ تنتقل بالتماس الفموي المباشر (التقبيل) والأواني الملوّثة؛ الانتشار 10% بالفم السليم إلى 95% مع أمراض الأسنان واللثة؛ وأيضًا في اللوزتين المريضتين ومسحات المهبل وعنق الرحم لمستعملات اللولب؛ التشخيص: أطوار متغذّية في كشط اللثة والأسنان."),
 IM("Describe Endolimax nana and Iodamoeba buetschlii.", "صف الأميبا القزمة وأميبا بوتشلي اليودية.",
    "Endolimax nana: lumen of large intestine of man, primates and pigs; prevalence 10-20%; 3 stages; trophozoite 6-15 µm, granular vacuolated cytoplasm, central nucleus, sluggish; no chromatoid bars or glycogen vacuole; cyst oval 5-14 µm with 4 indistinct nuclei. Iodamoeba: widely distributed but less common; trophozoite 6-12 µm with clear nucleus; cyst oval, uninucleate with an iodine-staining glycogen mass (iodophilic body) — hence the name.",
    "الأميبا القزمة: تجويف الأمعاء الغليظة للإنسان والرئيسيات والخنازير؛ الانتشار 10-20%؛ 3 أطوار؛ المتغذّي 6-15 مايكرومتر بسايتوبلازم محبّب مفجّى ونواة مركزية وحركة بطيئة؛ بلا قضبان كروماتينية ولا فجوة غلايكوجين؛ الكيس بيضوي 5-14 مايكرومتر بـ4 أنوية غير واضحة. اليودية: واسعة الانتشار لكنها أقل شيوعًا؛ المتغذّي 6-12 مايكرومتر بنواة واضحة؛ الكيس بيضوي أحادي النواة فيه كتلة غلايكوجين تتصبّغ باليود (الجسم المحبّ لليود) — ومنه الاسم."),
 IM("Describe the forms and life cycle of Naegleria fowleri.", "صف أشكال النيغلرية الفاولرية ودورة حياتها.",
    "Exists as cyst and trophozoite; trophozoites are amoeboid and flagellated (8-15 µm). The amoeboid form has lobopodia, granular cytoplasm with food vacuoles, central karyosome and no peripheral chromatin; it is the only form recognized in humans and the only replicating form (binary fission). The amoeboid form transforms into the flagellated form in distilled water at 27-37 °C. Cycle: free-living trophozoites in water → inhalation while swimming → nasal mucosa → olfactory nerve → brain → primary amoebic meningoencephalitis → death.",
    "توجد بشكل كيس وطور متغذّي؛ والأطوار المتغذّية أميبية ومسوطة (8-15 مايكرومتر). للشكل الأميبي أقدام فصّية وسايتوبلازم محبّب فيه فجوات غذائية وجسيم نووي مركزي بلا كروماتين محيطي؛ وهو الشكل الوحيد المعروف في الإنسان والوحيد المتكاثر (انشطار ثنائي). ويتحوّل الشكل الأميبي إلى المسوط في الماء المقطّر بدرجة 27-37 °م. الدورة: أطوار حرّة في الماء ← استنشاق أثناء السباحة ← المخاطية الأنفية ← العصب الشمّي ← الدماغ ← التهاب السحايا والدماغ الأميبي الأولي ← الوفاة."),
 IM("Describe the laboratory diagnosis of Naegleria fowleri.", "صف التشخيص المختبري للنيغلرية الفاولرية.",
    "CSF analysis: thick purulent, PMN > 20,000/µl, elevated protein, reduced sugar (mimics bacterial meningitis). Direct microscopy: motile amoeboid trophozoites in a wet mount with cover slip (no counting chamber — they mimic leucocytes); spherical nucleus with large karyosome is the clue; phase contrast is better. Wright's or Giemsa stain: sky blue cytoplasm, pink nucleus. No refrigeration; low parasite load → centrifuge at 150 rpm for 5 min; direct fluorescent antibody with monoclonal antibody. Culture on nonnutrient agar with E. coli lawn → trail sign.",
    "تحليل السائل الدماغي الشوكي: قيحي سميك، متعدّدة النوى > 20,000/مايكرولتر، بروتين مرتفع، سكر منخفض (يحاكي التهاب السحايا البكتيري). الفحص المباشر: أطوار متغذّية أميبية متحرّكة في تحضير رطب بغطاء شريحة (بلا حجرة عدّ لأنها تحاكي كريات البيض)؛ النواة الكروية بجسيم نووي كبير هي المفتاح؛ والتباين الطوري أفضل. صبغة رايت أو كيمزا: سايتوبلازم أزرق سماوي ونواة وردية. لا تبريد؛ الحمل القليل ← نبذ 150 دورة/دقيقة لمدة 5 دقائق؛ أضداد متألّقة مباشرة بضدّ وحيد النسيلة. الزرع على أكار غير مغذٍّ مع مزرعة إشريكية ← علامة المسار."),
]

meta = {"subject_en": "Medical Parasitology", "subject_ar": "الطفيليات الطبية", "short_ar": "طفيليات", "instructor": "م.م. نريمان حسن",
        "unit_en": "Lab 4", "unit_ar": "العملي 4", "unit_label": "LAB", "unit_no": "4",
        "title_en": "Non-pathogenic Amoebae & Naegleria fowleri", "title_ar": "الأميبات غير الممرضة والنيغلرية الفاولرية",
        "department": "قسم التحليلات", "stage": "The fourth stage — الرابعة", "kind": "Laboratories — عملي"}
save("parasitology-lab4-nonpathogenic-amoebae", meta, blocks, balance(mcq, 11), tf, traps, important)

```
