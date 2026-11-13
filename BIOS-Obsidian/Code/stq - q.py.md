---
source: BIOS-Obsidian/tools/scripts/stq/q.py
handouts: []
saved: 2026-11-13
tags: [bios, code]
---
# stq/q.py

Utility script.

```python
import sys, json, os
sys.path.insert(0, "/tmp/claude-0/-home-user-kwmdkm/44452a28-19bf-5ce8-890a-f6919e775f0b/scratchpad/imm456")
from ci import *            # Q TF TR IM P balance
sys.path.insert(0, "/tmp/claude-0/-home-user-kwmdkm/44452a28-19bf-5ce8-890a-f6919e775f0b/scratchpad"); from bidi import ltr_all

# Enzymology practical lecture 4 (stage 4, د. بارق و د. هشام) — Lab Safety and Blood Collecting Tubes.
# Source: the same image-based PDF (7 pages: lab-safety posters + blood tubes) WITH the student's handwritten notes.
# QUESTIONS ONLY — comprehensive MCQ + questions drawn from the student's handwritten annotations.
# answers_inline: answer under each option set + one short line explaining why (note_en/note_ar). (user rule 2026-11-08)
O = P
FOLDER = "enzymology-safety-tubes-mcq"
W = lambda q, en, ar: dict(q, note_en=en, note_ar=ar)      # why this option — one short line

mcq = [
 # ───────────────────────── 1. Lab safety — protective gear & rules
 {"topic_en": "Lab safety: protective gear and rules", "topic_ar": "سلامة المختبر: معدات الحماية والقواعد"},
 W(Q("Which item is part of the “Use Protective Gear” list?", "أيّ عنصر من قائمة «استعمل معدات الحماية»؟",
     O(("Open sandals", "صندل مكشوف"), ("Safety goggles", "نظارات السلامة"), ("Short trousers", "بنطلون قصير"), ("A smartwatch", "ساعة ذكية")), "b"),
   "The gear is goggles, lab coat, gloves, long pants and closed shoes.", "المعدات: نظارات سلامة، صدرية، قفازات، بنطلون طويل، وحذاء مغلق."),
 W(Q("“Proper Supervision” means you should NOT perform lab experiments without:", "«الإشراف المناسب» يعني ألّا تُجري التجارب دون:",
     O(("A phone", "هاتف"), ("Instructor supervision", "إشراف المدرّس"), ("Music", "موسيقى"), ("A partner only", "زميل فقط")), "b",),
   "A lab supervisor/instructor must be present — a point the student also noted by hand.", "يجب حضور مسؤول/مدرّس المختبر — وهي نقطة دوّنها الطالب بخط اليد أيضًا."),
 W(Q("“ID Hazards” instructs you to:", "«تعرّف على المخاطر» يوجّهك إلى:",
     O(("Taste chemicals to identify them", "تذوّق المواد لتعرّفها"), ("Always read labels before using any chemicals", "اقرأ الملصقات دائمًا قبل استعمال أي مواد"), ("Mix all reagents first", "اخلط الكواشف أولًا"), ("Ignore warning signs", "تجاهل علامات التحذير")), "b"),
   "Reading the label first tells you the hazard before you handle the chemical.", "قراءة الملصق أولًا تُعلمك الخطر قبل التعامل مع المادة."),
 W(Q("“Safety First” emphasises knowing the location of:", "«السلامة أولًا» تؤكّد معرفة مكان:",
     O(("The cafeteria", "المقصف"), ("Safety equipment and emergency numbers", "معدات السلامة وأرقام الطوارئ"), ("The library", "المكتبة"), ("The car park", "موقف السيارات")), "b"),
   "You must know where the safety equipment and exits/emergency numbers are.", "يجب أن تعرف مكان معدات السلامة والمخارج وأرقام الطوارئ."),
 W(Q("Under “No Food”, you must never:", "تحت «ممنوع الطعام»، يجب ألّا:",
     O(("Wash your hands", "تغسل يديك"), ("Eat, drink, or taste chemicals in the lab", "تأكل أو تشرب أو تتذوّق المواد في المختبر"), ("Wear gloves", "تلبس قفازات"), ("Label tubes", "تؤشّر الأنابيب")), "b"),
   "Eating, drinking and tasting chemicals are forbidden in the lab.", "الأكل والشرب وتذوّق المواد ممنوعة في المختبر."),
 W(Q("“Be Attentive” warns you NOT to:", "«كن منتبهًا» يحذّرك من:",
     O(("Leave an experiment in progress", "ترك تجربة وهي قيد التنفيذ"), ("Read the protocol", "قراءة البروتوكول"), ("Ask the instructor", "سؤال المدرّس"), ("Record results", "تسجيل النتائج")), "a"),
   "Stay present and do not leave a running experiment unattended.", "ابقَ حاضرًا ولا تترك تجربة شغّالة دون مراقبة."),
 W(Q("“Handle Glassware Carefully” tells you to:", "«تعامل مع الزجاجيات بحذر» يطلب منك:",
     O(("Throw broken glass in the sink", "رمي الزجاج المكسور في الحوض"), ("Properly dispose of anything that breaks", "التخلّص الصحيح من أي شيء ينكسر"), ("Heat glass on an open flame freely", "تسخين الزجاج على اللهب بحرّية"), ("Leave broken glass on the bench", "ترك الزجاج المكسور على الطاولة")), "b"),
   "Dispose of broken glassware the proper way, not in a normal bin or sink.", "تخلّص من الزجاج المكسور بالطريقة الصحيحة، لا في الحوض أو سلّة عادية."),
 W(Q("Under “Clean Up”, after finishing the lab you must:", "تحت «التنظيف»، بعد انتهاء العملي يجب:",
     O(("Leave immediately", "المغادرة فورًا"), ("Clean the workspace and equipment and wash your hands", "تنظيف مكان العمل والأجهزة وغسل اليدين"), ("Keep your gloves on all day", "إبقاء القفازات طوال اليوم"), ("Store food in the fridge", "خزن الطعام في الثلاجة")), "b"),
   "Clean your workspace and equipment, and don’t forget to wash your hands.", "نظّف مكان العمل والأجهزة، ولا تنسَ غسل يديك."),

 # ───────────────────────── 2. Student handwritten safety notes
 {"topic_en": "From the student’s handwritten notes (safety)", "topic_ar": "من ملاحظات الطالب بخط اليد (السلامة)"},
 W(Q("A student note beside “Proper Supervision” states that there must always be:", "ملاحظة الطالب بجانب «الإشراف المناسب» تقول إنه يجب دائمًا وجود:",
     O(("A lab supervisor present", "مسؤول للمختبر حاضر"), ("Two microscopes", "مجهرين"), ("An open window", "نافذة مفتوحة"), ("A fire only", "نار فقط")), "a"),
   "Student note: “there must be a lab supervisor present.”", "ملاحظة الطالب: «لازم موجود مسؤول للمختبر»."),
 W(Q("The student labelled the four hazard symbols. Which set matches them?", "أشّر الطالب رموز الخطر الأربعة. أيّ مجموعة تطابقها؟",
     O(("Explosive, radioactive, flammable, toxic", "متفجّرة، مشعّة، قابلة للاشتعال، سامّة"), ("Acidic, basic, neutral, inert", "حمضية، قاعدية، متعادلة، خاملة"), ("Cold, hot, wet, dry", "باردة، حارّة، رطبة، جافّة"), ("Red, green, blue, yellow", "حمراء، خضراء، زرقاء، صفراء")), "a"),
   "The four pictograms shown are: explosive, radioactive, flammable and toxic (skull).", "الرموز الأربعة المعروضة: متفجّرة، مشعّة، قابلة للاشتعال، وسامّة (الجمجمة)."),
 W(Q("Another student note beside “Safety First” reminds you to know the lab’s:", "ملاحظة أخرى للطالب بجانب «السلامة أولًا» تذكّرك بمعرفة:",
     O(("Doors and exits (emergency routes)", "أبواب المختبر ومخارجه (طرق الطوارئ)"), ("Wi-Fi password", "كلمة مرور الإنترنت"), ("Nearest café", "أقرب مقهى"), ("Staff names", "أسماء الموظّفين")), "a"),
   "Student note: you must know the lab doors/exits — matching “emergency routes accessible.”", "ملاحظة الطالب: لازم تعرف أبواب/مخارج المختبر — وتوافق «طرق الطوارئ متاحة»."),
 W(Q("The student’s note beside “Be Attentive” warns that you must NOT:", "ملاحظة الطالب بجانب «كن منتبهًا» تحذّر من:",
     O(("Expose glassware directly to a flame", "تعريض الزجاجيات مباشرةً للّهب"), ("Wear gloves", "لبس القفازات"), ("Label the tubes", "تأشير الأنابيب"), ("Record the time", "تسجيل الوقت")), "a"),
   "Student note: “glassware must not be exposed to the flame directly.”", "ملاحظة الطالب: «لا يجوز تعريض الزجاج على اللهب مباشرة»."),

 # ───────────────────────── 3. Lab safety poster (page 2)
 {"topic_en": "Lab safety poster rules", "topic_ar": "قواعد بوستر سلامة المختبر"},
 W(Q("According to the poster, who may be in the laboratory?", "حسب البوستر، مَن يُسمح له بالوجود في المختبر؟",
     O(("Anyone", "أي شخص"), ("Authorised persons only", "الأشخاص المخوّلون فقط"), ("Visitors freely", "الزوّار بحرّية"), ("Children", "الأطفال")), "b"),
   "“Authorised persons only in the laboratory.”", "«الأشخاص المخوّلون فقط في المختبر»."),
 W(Q("The poster requires footwear to be:", "يشترط البوستر أن يكون الحذاء:",
     O(("Open sandals", "صندل مكشوف"), ("Sensible, closed (no open shoes)", "مناسبًا مغلقًا (لا حذاء مكشوف)"), ("High heels", "كعب عالٍ"), ("Barefoot allowed", "يُسمح بحفاء القدم")), "b"),
   "“Sensible footwear must be worn — no open shoes.”", "«يجب ارتداء حذاء مناسب — لا أحذية مكشوفة»."),
 W(Q("On the poster, all accidents and dangerous events must be:", "حسب البوستر، كل الحوادث والأحداث الخطيرة يجب:",
     O(("Ignored", "تجاهلها"), ("Reported and recorded", "الإبلاغ عنها وتسجيلها"), ("Hidden", "إخفاؤها"), ("Discussed later only", "مناقشتها لاحقًا فقط")), "b"),
   "“All accidents and dangerous events must be reported and recorded.”", "«كل الحوادث والأحداث الخطيرة يجب الإبلاغ عنها وتسجيلها»."),
 W(Q("The poster states that all work must be carried out in accordance with:", "يذكر البوستر أن كل العمل يجب أن يُجرى وفق:",
     O(("Personal preference", "التفضيل الشخصي"), ("A risk assessment", "تقييم المخاطر"), ("The weather", "الطقس"), ("The budget", "الميزانية")), "b"),
   "“All work must be carried out in accordance with risk assessment.”", "«كل العمل يجب أن يُجرى وفق تقييم المخاطر»."),
 W(Q("Waste, according to the poster, must be:", "حسب البوستر، يجب التخلّص من النفايات:",
     O(("Poured down the sink", "صبّها في الحوض"), ("Disposed of properly, in line with policy", "بشكل صحيح ووفق السياسة"), ("Left on the bench", "تركها على الطاولة"), ("Burned openly", "حرقها في العلن")), "b"),
   "“Dispose of waste properly, in line with policy.”", "«تخلّص من النفايات بشكل صحيح ووفق السياسة»."),

 # ───────────────────────── 4. Blood collecting tubes — introduction & order of draw
 {"topic_en": "Blood collecting tubes: introduction and order of draw", "topic_ar": "أنابيب جمع الدم: المقدمة وترتيب السحب"},
 W(Q("Blood collection tubes are used in hospitals because:", "تُستعمل أنابيب جمع الدم في المستشفيات لأن:",
     O(("Each tube has different functions for various diagnostic tests", "لكل أنبوب وظائف مختلفة لفحوص تشخيصية متنوّعة"), ("They are all identical", "كلها متطابقة"), ("Only one tube exists", "يوجد أنبوب واحد فقط"), ("They store food", "لتخزين الطعام")), "a"),
   "Different tubes have different additives and uses, so each must be used accordingly.", "لكل أنبوب مضاف واستعمال مختلف، فيجب استعمال كلٍّ بحسبه."),
 W(Q("In the order of draw, the FIRST tube (number 1) is the:", "في ترتيب السحب، الأنبوب الأول (رقم 1) هو:",
     O(("Lavender top tube", "البنفسجي"), ("Plain (red top) tube", "السادة (الأحمر)"), ("Grey top tube", "الرمادي"), ("Blue tube", "الأزرق")), "b"),
   "In the lecture table, order 1 is the Plain / Red top tube (no additive).", "في جدول المحاضرة، الترتيب 1 هو الأنبوب السادة/الأحمر (بلا مضاف)."),
 W(Q("Which tube–additive pairing is correct in the lecture table?", "أيّ مزاوجة أنبوب–مضاف صحيحة في جدول المحاضرة؟",
     O(("Lavender = Sodium fluoride", "البنفسجي = فلوريد الصوديوم"), ("Grey = EDTA", "الرمادي = EDTA"), ("Lavender = EDTA", "البنفسجي = EDTA"), ("Green = Thrombin", "الأخضر = الثرومبين")), "c"),
   "Lavender top = EDTA; grey = sodium fluoride; green = sodium heparin; orange = thrombin.", "البنفسجي = EDTA؛ الرمادي = فلوريد الصوديوم؛ الأخضر = هيبارين الصوديوم؛ البرتقالي = ثرومبين."),
 W(Q("In the table, the ESR tube has the stopper colour:", "في الجدول، أنبوب سرعة الترسيب (ESR) لونه:",
     O(("Black", "أسود"), ("Red", "أحمر"), ("Yellow", "أصفر"), ("Green", "أخضر")), "a",),
   "ESR (Westergren sedimentation rate) = Black top tube with sodium citrate.", "ESR (سرعة ترسيب وسترغرين) = الأنبوب الأسود مع سترات الصوديوم."),

 # ───────────────────────── 5. Red tubes
 {"topic_en": "Red tubes", "topic_ar": "الأنابيب الحمراء"},
 W(Q("Red tubes are used for biochemistry tests that require:", "تُستعمل الأنابيب الحمراء لفحوص كيموحيوية تتطلّب:",
     O(("Whole blood", "دم كامل"), ("Serum", "المصل"), ("Plasma only", "بلازما فقط"), ("Urine", "إدرار")), "b"),
   "Red tubes give serum (the blood is allowed to clot).", "الأنابيب الحمراء تعطي المصل (يُترك الدم ليتخثّر)."),
 W(Q("The additive/particles in red tubes act as:", "المادة/الجسيمات في الأنابيب الحمراء تعمل كـ:",
     O(("Anticoagulant", "مانع تخثّر"), ("Clot activators (silica particles)", "منشّطات تخثّر (جزيئات سيليكا)"), ("A dye", "صبغة"), ("A buffer", "محلول منظّم")), "b"),
   "Red tubes contain silica particles that promote clotting (clot activator).", "تحتوي الأنابيب الحمراء على جزيئات سيليكا تعزّز التخثّر (منشّط تخثّر)."),
 W(Q("Which test is a laboratory use of the red tube?", "أيّ فحص من استعمالات الأنبوب الأحمر؟",
     O(("CBC", "تعداد الدم الكامل"), ("Serum glucose, cholesterol, liver enzymes", "سكر المصل، الكوليسترول، إنزيمات الكبد"), ("Coagulation PT/PTT", "التخثّر PT/PTT"), ("Blood film for malaria", "فيلم الملاريا")), "b"),
   "Red (serum) tube: glucose, lipids, cholesterol, enzymes, antibody screening, blood-bank serology, etc.", "الأنبوب الأحمر (المصل): السكر، الدهون، الكوليسترول، الإنزيمات، فحص الأضداد، مصليات بنك الدم، وغيرها."),

 # ───────────────────────── 6. Lavender (EDTA) tubes
 {"topic_en": "Lavender (EDTA) tubes", "topic_ar": "الأنابيب البنفسجية (EDTA)"},
 W(Q("Lavender tubes are mainly used for:", "تُستعمل الأنابيب البنفسجية أساسًا لفحوص:",
     O(("Hematology tests (whole blood)", "أمراض الدم (دم كامل)"), ("Coagulation", "التخثّر"), ("Blood cultures", "زرع الدم"), ("Serum chemistry", "كيمياء المصل")), "a"),
   "Lavender/EDTA tubes are for hematology, where whole blood is needed.", "الأنابيب البنفسجية/EDTA لأمراض الدم حيث يُحتاج دم كامل."),
 W(Q("EDTA prevents clotting by:", "يمنع EDTA التخثّر عن طريق:",
     O(("Activating thrombin", "تنشيط الثرومبين"), ("Removing (binding) calcium", "إزالة (ربط) الكالسيوم"), ("Adding silica", "إضافة السيليكا"), ("Heating the blood", "تسخين الدم")), "b"),
   "EDTA chelates (removes) calcium, so no clot forms.", "يخلب EDTA الكالسيوم (يزيله) فلا يتكوّن تخثّر."),
 W(Q("Which test uses the lavender (EDTA) tube?", "أيّ فحص يستعمل الأنبوب البنفسجي (EDTA)؟",
     O(("CBC, HbA1c, blood film for malaria", "تعداد الدم، HbA1c، فيلم الملاريا"), ("PT/PTT", "PT/PTT"), ("Serum cholesterol", "كوليسترول المصل"), ("Blood culture", "زرع الدم")), "a"),
   "EDTA tube: CBC, HbA1c, blood film (malaria/abnormal cells), reticulocytes, monospot.", "أنبوب EDTA: تعداد الدم، HbA1c، الفيلم الدموي (الملاريا/الخلايا الشاذّة)، الخلايا الشبكية، المونوسبوت."),

 # ───────────────────────── 7. Green (heparin) tubes
 {"topic_en": "Green (heparin) tubes", "topic_ar": "الأنابيب الخضراء (الهيبارين)"},
 W(Q("The additive in green tubes is:", "المادة المضافة في الأنابيب الخضراء هي:",
     O(("EDTA", "EDTA"), ("Heparin (sodium/lithium/ammonium)", "الهيبارين (صوديوم/ليثيوم/أمونيوم)"), ("Sodium fluoride", "فلوريد الصوديوم"), ("Thrombin", "الثرومبين")), "b"),
   "Green tubes contain heparin, which inhibits thrombin to prevent clotting.", "تحتوي الأنابيب الخضراء على الهيبارين الذي يثبّط الثرومبين لمنع التخثّر."),
 W(Q("Heparin prevents blood clotting by:", "يمنع الهيبارين التخثّر عن طريق:",
     O(("Inhibiting the formation of thrombin", "تثبيط تكوّن الثرومبين"), ("Binding calcium like EDTA", "ربط الكالسيوم مثل EDTA"), ("Activating silica", "تنشيط السيليكا"), ("Adding fluoride", "إضافة الفلوريد")), "a"),
   "Heparin works by inhibiting thrombin formation (a different mechanism from citrate/EDTA).", "يعمل الهيبارين بتثبيط تكوّن الثرومبين (آلية تختلف عن السترات/EDTA)."),
 W(Q("A laboratory use of the green tube is:", "من استعمالات الأنبوب الأخضر:",
     O(("Chemistry testing, ammonia, insulin, chromosome screening", "الفحوص الكيميائية، الأمونيا، الأنسولين، فحص الكروموسومات"), ("CBC", "تعداد الدم"), ("Coagulation", "التخثّر"), ("Blood culture", "زرع الدم")), "a"),
   "Green (heparinized plasma): chemistry, ammonia, insulin, chromosome screening, aldosterone, renin.", "الأخضر (بلازما مهبّرنة): الكيمياء، الأمونيا، الأنسولين، فحص الكروموسومات، الألدوستيرون، الرينين."),

 # ───────────────────────── 8. Grey tubes
 {"topic_en": "Grey tubes", "topic_ar": "الأنابيب الرمادية"},
 W(Q("The grey top tube additive is:", "مضاف الأنبوب الرمادي هو:",
     O(("Sodium citrate", "سترات الصوديوم"), ("Sodium fluoride", "فلوريد الصوديوم"), ("EDTA", "EDTA"), ("Thrombin", "الثرومبين")), "b"),
   "Grey = sodium fluoride; it preserves glucose (antiglycolytic).", "الرمادي = فلوريد الصوديوم؛ يحفظ الغلوكوز (مضادّ لتحلّل السكّر)."),
 W(Q("The grey tube is used mainly for:", "يُستعمل الأنبوب الرمادي أساسًا لـ:",
     O(("CBC", "تعداد الدم"), ("Glucose tolerance testing and alcohol level", "اختبار تحمّل الغلوكوز ومستوى الكحول"), ("Coagulation", "التخثّر"), ("Blood culture", "زرع الدم")), "b"),
   "Sodium fluoride stops glycolysis, so glucose stays stable — glucose/alcohol testing.", "فلوريد الصوديوم يوقف تحلّل السكّر فيبقى الغلوكوز ثابتًا — فحص السكّر/الكحول."),

 # ───────────────────────── 9. Light blue tubes
 {"topic_en": "Light blue tubes", "topic_ar": "الأنابيب الزرقاء الفاتحة"},
 W(Q("Light blue tubes are used for:", "تُستعمل الأنابيب الزرقاء الفاتحة لـ:",
     O(("Coagulation (clotting) tests", "فحوص التخثّر"), ("CBC", "تعداد الدم"), ("Serum chemistry", "كيمياء المصل"), ("Cultures", "الزرع")), "a"),
   "Blue tubes are for coagulation tests (PT, PTT, FDP, factor assays).", "الأنابيب الزرقاء لفحوص التخثّر (PT، PTT، FDP، فحوص العوامل)."),
 W(Q("The additive in light blue tubes is sodium citrate, which:", "مضاف الأنابيب الزرقاء هو سترات الصوديوم، الذي:",
     O(("Activates clotting", "ينشّط التخثّر"), ("Binds and removes calcium to prevent clotting", "يربط الكالسيوم ويزيله لمنع التخثّر"), ("Adds glucose", "يضيف الغلوكوز"), ("Inhibits thrombin directly", "يثبّط الثرومبين مباشرةً")), "b"),
   "Sodium citrate binds calcium (reversibly) to stop clotting — ideal for coagulation tests.", "سترات الصوديوم تربط الكالسيوم (عكسيًا) لإيقاف التخثّر — مثالية لفحوص التخثّر."),

 # ───────────────────────── 10. Yellow tubes
 {"topic_en": "Yellow tubes", "topic_ar": "الأنابيب الصفراء"},
 W(Q("Yellow tubes are used for blood and bodily-fluid:", "تُستعمل الأنابيب الصفراء للدم وسوائل الجسم في:",
     O(("Cultures", "الزرع (المزارع)"), ("Coagulation", "التخثّر"), ("Glucose testing", "فحص السكّر"), ("ESR", "سرعة الترسيب")), "a"),
   "Yellow tubes are for cultures; their additive (SPS/ACD) also stabilizes bacterial growth.", "الأنابيب الصفراء للمزارع؛ ومضافها (SPS/ACD) يثبّت أيضًا نموّ البكتيريا."),
 W(Q("The additive in yellow tubes is:", "المادة المضافة في الأنابيب الصفراء هي:",
     O(("SPS and ACD", "SPS وACD"), ("EDTA", "EDTA"), ("Sodium fluoride", "فلوريد الصوديوم"), ("Heparin", "الهيبارين")), "a"),
   "Yellow = SPS (sodium polyanethol sulfonate) and ACD (acid citrate dextrose).", "الأصفر = SPS (سلفونات بولي أنيثول الصوديوم) وACD (ستّرات الحامض والدكستروز)."),
 W(Q("Tubes containing ACD are used for:", "الأنابيب التي تحتوي ACD تُستعمل لـ:",
     O(("Cellular studies, paternity testing, HLA typing", "الدراسات الخلوية، فحص الأبوّة، تنميط HLA"), ("Glucose", "السكّر"), ("ESR", "سرعة الترسيب"), ("PT/PTT", "PT/PTT")), "a"),
   "ACD tubes: cellular studies, paternity (DNA) testing and HLA typing.", "أنابيب ACD: الدراسات الخلوية، فحص الأبوّة (DNA)، وتنميط HLA."),

 # ───────────────────────── 11. From the student’s homework note + comparison
 {"topic_en": "From the student’s note + comparison", "topic_ar": "من ملاحظة الطالب + المقارنة"},
 W(Q("Student homework: why is EDTA preferred over sodium citrate for a complete blood count (CBC)?", "واجب الطالب: لماذا يُفضَّل EDTA على سترات الصوديوم لتعداد الدم الكامل (CBC)؟",
     O(("EDTA best preserves cell morphology and counts and does not dilute the sample", "EDTA يحفظ شكل الخلايا وأعدادها جيّدًا ولا يخفّف العيّنة"), ("Sodium citrate is toxic", "سترات الصوديوم سامّة"), ("EDTA adds calcium", "EDTA يضيف الكالسيوم"), ("They are identical", "هما متطابقان")), "a"),
   "EDTA keeps cells intact for accurate counts; citrate dilutes the sample (liquid additive) and is kept for coagulation. (From the student’s handwritten question.)", "EDTA يحافظ على الخلايا لعدٍّ دقيق؛ أما السترات فتخفّف العيّنة (مضاف سائل) وتُحفظ للتخثّر. (من سؤال الطالب بخط اليد.)"),
 W(Q("Which two additives both work by removing/binding calcium?", "أيّ مضافَين يعملان بإزالة/ربط الكالسيوم؟",
     O(("EDTA and sodium citrate", "EDTA وسترات الصوديوم"), ("Heparin and thrombin", "الهيبارين والثرومبين"), ("Silica and SPS", "السيليكا وSPS"), ("Sodium fluoride and ACD", "فلوريد الصوديوم وACD")), "a"),
   "Both EDTA and sodium citrate chelate calcium; heparin instead inhibits thrombin.", "كلٌّ من EDTA وسترات الصوديوم يخلب الكالسيوم؛ أما الهيبارين فيثبّط الثرومبين."),
 W(Q("Which abbreviation is matched correctly?", "أيّ اختصار مطابق صحيح؟",
     O(("PTT = Prothrombin time", "PTT = زمن البروثرومبين"), ("CBC = Complete blood count", "CBC = تعداد الدم الكامل"), ("ACD = EDTA", "ACD = EDTA"), ("SPS = silica particles", "SPS = جزيئات السيليكا")), "b"),
   "CBC = complete blood count; PT = prothrombin time; PTT = partial thromboplastin time; ACD = acid citrate dextrose; SPS = sodium polyanethol sulfonate.", "CBC = تعداد الدم الكامل؛ PT = زمن البروثرومبين؛ PTT = زمن الثرومبوبلاستين الجزئي؛ ACD = ستّرات الحامض والدكستروز؛ SPS = سلفونات بولي أنيثول الصوديوم."),
]
mcq = balance(mcq, 404)

meta = {"subject_en": "Clinical Enzymology", "subject_ar": "الإنزيمات السريرية", "short_ar": "انزيمات سريرية", "instructor": "د. بارق و د. هشام",
        "unit_en": "Lecture 4", "unit_ar": "المحاضرة 4", "unit_label": "LEC", "unit_no": "4",
        "title_en": "Lab Safety and Blood Collecting Tubes", "title_ar": "السلامة في المختبر وأنابيب جمع الدم",
        "kind": "Laboratories — عملي", "stage": "The fourth stage — الرابعة",
        "file_name": "BIOS - انزيمات سريرية عملي المحاضرة الرابعة - بنك أسئلة شامل"}
important = [
 IM("List the personal protective equipment to be used in the laboratory.", "اذكر معدات الحماية الشخصية التي تُستعمل في المختبر.",
    "Safety goggles, a lab coat, gloves, long pants (trousers) and closed shoes.",
    "نظارات السلامة، والصدرية (المعطف)، والقفازات، والبنطلون الطويل، والحذاء المغلق."),
 IM("State the main laboratory safety rules.", "اذكر قواعد سلامة المختبر الرئيسة.",
    "Proper supervision (no experiment without the instructor); identify hazards (read labels first); know the safety equipment, exits and emergency numbers; no food, drink or tasting chemicals; be attentive and never leave a running experiment; handle and dispose of glassware carefully; clean up and wash hands; authorised persons only; wear a lab coat and closed footwear; report and record all accidents; work according to a risk assessment; dispose of waste properly; no smoking; keep the lab tidy with emergency routes clear.",
    "الإشراف المناسب (لا تجربة دون المدرّس)؛ التعرّف على المخاطر (اقرأ الملصقات أولًا)؛ معرفة معدات السلامة والمخارج وأرقام الطوارئ؛ لا طعام ولا شراب ولا تذوّق للمواد؛ الانتباه وعدم ترك تجربة شغّالة؛ التعامل مع الزجاجيات والتخلّص منها بحذر؛ التنظيف وغسل اليدين؛ الأشخاص المخوّلون فقط؛ ارتداء الصدرية والحذاء المغلق؛ الإبلاغ عن كل الحوادث وتسجيلها؛ العمل وفق تقييم المخاطر؛ التخلّص الصحيح من النفايات؛ ممنوع التدخين؛ إبقاء المختبر مرتّبًا ومخارج الطوارئ متاحة."),
 IM("From the student’s notes: explain the four hazard symbols and the extra safety points the student added.", "من ملاحظات الطالب: اشرح رموز الخطر الأربعة والنقاط الإضافية التي أضافها الطالب.",
    "The four hazard pictograms are: explosive, radioactive, flammable, and toxic (skull). The student also noted: a lab supervisor must always be present; you must know the lab doors/exits (emergency routes); and glassware must NOT be exposed to the flame directly.",
    "الرموز الأربعة: متفجّرة، ومشعّة، وقابلة للاشتعال، وسامّة (الجمجمة). وأضاف الطالب: يجب دائمًا وجود مسؤول للمختبر؛ ويجب معرفة أبواب/مخارج المختبر (طرق الطوارئ)؛ ولا يجوز تعريض الزجاج للّهب مباشرةً."),
 IM("Give the order of draw of blood collection tubes (as in the lecture table).", "اذكر ترتيب سحب أنابيب جمع الدم (كما في جدول المحاضرة).",
    "1) Plain / red top, 2) EDTA / lavender, 3) heparin / green, 4) ESR / black, 5) glucose / grey, 6) PT / blue, 7) serum / yellow, 8) thrombin / orange, 9) serum gel / gel yellow.",
    "1) السادة/الأحمر، 2) EDTA/البنفسجي، 3) الهيبارين/الأخضر، 4) ESR/الأسود، 5) الغلوكوز/الرمادي، 6) PT/الأزرق، 7) المصل/الأصفر، 8) الثرومبين/البرتقالي، 9) الهلامي/الأصفر الهلامي."),
 IM("For each tube colour, give its additive and main laboratory use: red, lavender, green, grey, light blue, yellow.", "لكل لون أنبوب اذكر مضافه واستعماله الرئيس: الأحمر، البنفسجي، الأخضر، الرمادي، الأزرق الفاتح، الأصفر.",
    "Red: no additive (silica clot activator) → serum biochemistry (glucose, lipids, enzymes). Lavender: EDTA → hematology (CBC, HbA1c, blood film). Green: heparin → chemistry, ammonia, insulin. Grey: sodium fluoride → glucose tolerance / alcohol. Light blue: sodium citrate → coagulation (PT, PTT). Yellow: SPS/ACD → cultures and cellular/HLA/paternity studies.",
    "الأحمر: بلا مضاف (سيليكا منشّط تخثّر) ← كيمياء المصل (السكر، الدهون، الإنزيمات). البنفسجي: EDTA ← أمراض الدم (CBC، HbA1c، الفيلم الدموي). الأخضر: الهيبارين ← الكيمياء، الأمونيا، الأنسولين. الرمادي: فلوريد الصوديوم ← تحمّل الغلوكوز/الكحول. الأزرق: سترات الصوديوم ← التخثّر (PT، PTT). الأصفر: SPS/ACD ← المزارع والدراسات الخلوية/HLA/الأبوّة."),
 IM("Explain how EDTA, sodium citrate and heparin each prevent clotting, and how the red tube differs.", "اشرح كيف يمنع كلٌّ من EDTA وسترات الصوديوم والهيبارين التخثّر، وكيف يختلف الأنبوب الأحمر.",
    "EDTA and sodium citrate both bind/remove calcium so no clot forms (citrate is reversible). Heparin instead inhibits the formation of thrombin. The red tube has NO anticoagulant — its silica particles are clot activators, so the blood clots and gives serum.",
    "يربط كلٌّ من EDTA وسترات الصوديوم الكالسيوم ويزيلانه فلا يتكوّن تخثّر (والسترات عكسية). أما الهيبارين فيثبّط تكوّن الثرومبين. والأنبوب الأحمر بلا مانع تخثّر — جزيئات السيليكا فيه منشّطات تخثّر، فيتخثّر الدم ويعطي المصل."),
 IM("Student homework: why is EDTA preferred over sodium citrate for a complete blood count (CBC)?", "واجب الطالب: لماذا يُفضَّل EDTA على سترات الصوديوم لتعداد الدم الكامل (CBC)؟",
    "EDTA best preserves cell morphology and gives accurate cell counts and does not dilute the sample. Sodium citrate is a liquid additive that dilutes the blood (fixed blood-to-additive ratio) and is reserved for coagulation tests, so it is not suitable for a CBC.",
    "EDTA يحفظ شكل الخلايا جيدًا ويعطي عدًّا دقيقًا للخلايا ولا يخفّف العيّنة. أما سترات الصوديوم فمضاف سائل يخفّف الدم (بنسبة ثابتة دم:مضاف) وتُحفظ لفحوص التخثّر، فلا تصلح لتعداد الدم."),
 # ───── more SA tied to the student’s highlighted points
 IM("Marked by the student — red tube: what sample does it give, what is its additive, and give three of its tests.", "مؤشَّر بالطالب — الأنبوب الأحمر: أيّ عيّنة يعطي، وما مضافه، واذكر ثلاثة من فحوصه.",
    "It gives serum (the blood is allowed to clot). It has no anticoagulant; it contains silica particles that act as clot activators. Tests: serum glucose, cholesterol/triglycerides/HDL, liver enzymes/CK, antibody screening, blood-bank serology, RPR, ANA, rheumatoid factor.",
    "يعطي المصل (يُترك الدم ليتخثّر). وبلا مانع تخثّر؛ فيه جزيئات سيليكا تعمل منشّطات تخثّر. الفحوص: سكر المصل، الكوليسترول/الدهون الثلاثية/HDL، إنزيمات الكبد/CK، فحص الأضداد، مصليات بنك الدم، RPR، ANA، العامل الرثوي."),
 IM("Marked by the student — light blue tube: its use, its additive’s mechanism, and its tests.", "مؤشَّر بالطالب — الأنبوب الأزرق الفاتح: استعماله، وآلية مضافه، وفحوصه.",
    "Used for hematology coagulation (clotting) tests that need whole blood. Additive: sodium citrate, which binds and removes calcium to prevent clotting. Tests: coagulation, PT, FDP, APTT/PTT, TT and factor assays.",
    "يُستعمل لفحوص التخثّر (الدم الكامل). المضاف: سترات الصوديوم التي تربط الكالسيوم وتزيله لمنع التخثّر. الفحوص: التخثّر، PT، FDP، APTT/PTT، TT، وفحوص العوامل."),
 IM("Marked by the student — green tube: why is it the most common, its additive and mechanism, and its uses.", "مؤشَّر بالطالب — الأنبوب الأخضر: لماذا هو الأكثر شيوعًا، ومضافه وآليته، واستعمالاته.",
    "It is the most common tube, used mainly for biochemistry tests needing whole blood or heparinized plasma. Additive: heparin (sodium/lithium/ammonium), which inhibits the formation of thrombin to prevent clotting. Uses: chemistry testing, ammonia, insulin, chromosome screening, aldosterone and renin.",
    "هو الأكثر شيوعًا، يُستعمل أساسًا لفحوص الكيمياء الحيوية التي تحتاج دمًا كاملًا أو بلازما مهبّرنة. المضاف: الهيبارين (صوديوم/ليثيوم/أمونيوم) الذي يثبّط تكوّن الثرومبين لمنع التخثّر. الاستعمالات: الفحوص الكيميائية، الأمونيا، الأنسولين، فحص الكروموسومات، الألدوستيرون والرينين."),
 IM("Marked by the student — lavender and yellow tubes: give the additive and main uses of each.", "مؤشَّر بالطالب — الأنبوبان البنفسجي والأصفر: اذكر مضاف واستعمالات كلٍّ منهما.",
    "Lavender: additive EDTA (removes calcium) → hematology; blood film for malaria/abnormal cells, red-cell folate, reticulocytes, parathyroid hormone and monospot. Yellow: additive SPS and ACD (prevent clotting and stabilize bacterial growth) → blood/bodily-fluid cultures; ACD tubes for cellular studies, paternity testing and HLA typing.",
    "البنفسجي: مضافه EDTA (يزيل الكالسيوم) ← أمراض الدم؛ الفيلم الدموي للملاريا/الخلايا الشاذّة، فولات الكريات الحمر، الخلايا الشبكية، هرمون جارات الدرقية، والمونوسبوت. الأصفر: مضافه SPS وACD (يمنعان التخثّر ويثبّتان نموّ البكتيريا) ← مزارع الدم وسوائل الجسم؛ وأنابيب ACD للدراسات الخلوية وفحص الأبوّة وتنميط HLA."),
 IM("Marked by the student — grey tube: its additive, why it is used, and its main tests.", "مؤشَّر بالطالب — الأنبوب الرمادي: مضافه، وسبب استعماله، وفحوصه الرئيسة.",
    "Additive: sodium fluoride, which stops glycolysis (antiglycolytic) so glucose stays stable in the sample. Main uses: glucose tolerance testing and blood alcohol level.",
    "المضاف: فلوريد الصوديوم الذي يوقف تحلّل السكّر (مضادّ لتحلّل السكّر) فيبقى الغلوكوز ثابتًا في العيّنة. الاستعمالات: اختبار تحمّل الغلوكوز ومستوى الكحول في الدم."),
]
Qs = {"title_en": "Lab Safety and Blood Collecting Tubes — Comprehensive Questions (MCQ + SA)", "title_ar": "السلامة في المختبر وأنابيب جمع الدم — أسئلة شاملة (اختيار + مقالية)",
      "answers_inline": True, "mcq": ltr_all(mcq), "tf": [], "traps": [], "important": ltr_all(important)}
d = "/home/user/-/" + FOLDER
os.makedirs(d, exist_ok=True)
json.dump({"meta": meta, "questions": Qs}, open(d + "/lecture.json", "w"), ensure_ascii=False, indent=1)
from collections import Counter
qs = [m for m in mcq if "answer" in m]
print(FOLDER, len(qs), "MCQ", dict(Counter(m["answer"] for m in qs)), "| notes:", sum(1 for m in qs if m.get("note_en")))

```
