import sys, json, os, shutil
from collections import Counter
WORK = "/home/claude/scratch/work"
sys.path.insert(0, WORK + "/bac"); from bal import balance
sys.path.insert(0, WORK); from bidi import ltr_all

# Diagnostic Microbiology — PRACTICAL Lab 6 (stage 4, د. هبة سامي; slides by MSc. Hiba Sami & MSc. Ali Thamar):
# Biochemical Testing of Microorganisms. Source 2026-11-22: class-annotated (Kilonotes) copy of the same 20-slide deck as
# bacteriology-lab6-biochemical-tests/. Handwritten class notes used as "Class note" questions: catalase — the reagent is
# H2O2, medium nutrient agar, do not take colonies from blood/chocolate agar (RBCs give false bubbles); indole — medium
# tryptone broth, Proteus vulgaris +, P. mirabilis −; oxidase — medium nutrient agar.
# Slide wording flagged: MR says "oxidize glucose" (it is glucose FERMENTATION — mixed-acid); "Pseudomadacea" =
# Pseudomonadaceae; "TNPD" — the reagent's abbreviation is usually TMPD. Pictures = clean copies in the old handout's assets.

def Q(en, ar, opts, why_en, why_ar, img=None, h="38mm", fixed=None):
    d = dict(en=en, ar=ar, options=[list(o) for o in opts], note_en=why_en, note_ar=why_ar)
    if fixed: d["_fixed"] = fixed
    else: d["answer"] = "a"
    if img: d.update(img="assets/" + img, img_h=h)
    return d
def T(en, ar): return {"topic_en": en, "topic_ar": ar}
ALL = ("All of the above", "جميع ما سبق")
S = lambda x: f"__{x}__"

mcq = [
 T("Introduction", "مقدّمة"),
 Q("Biochemical tests are needed for the identification of bacterial species because:", "نحتاج الاختبارات الكيميائية الحيوية لتشخيص أنواع البكتيريا لأن:",
   [("Many species have similar shape and size, so they are identified by differences in biochemical activities", "أنواعًا كثيرة متشابهة في الشكل والحجم، فتُشخَّص بالفروق في نشاطاتها الكيميائية الحيوية"),
    ("Bacteria cannot be stained", "البكتيريا لا تُصبغ"), ("Culture is impossible", "الزرع مستحيل"), ("They are cheaper than microscopy", "أرخص من المجهر")],
   "Slide 2.", "الشريحة 2."),

 T("1. Catalase test", "1. اختبار الكاتاليز"),
 Q("The catalase enzyme breaks hydrogen peroxide into:", "يحلّل إنزيم الكاتاليز بيروكسيد الهيدروجين إلى:",
   [("Water and oxygen gas", "ماء وغاز أكسجين"), ("Water and carbon dioxide", "ماء وثاني أكسيد الكربون"), ("Ammonia and CO2", "أمونيا وCO2"), ("Indole and pyruvic acid", "إندول وحمض البيروفيك")],
   "`2H2O2 → 2H2O + O2`.", "`2H2O2 → 2H2O + O2`."),
 Q("A positive catalase test is indicated by:", "تدلّ على نتيجة كاتاليز موجبة:",
   [("Bubbles (oxygen gas)", "الفقاعات (غاز الأكسجين)"), ("A red ring", "حلقة حمراء"), ("Dark-blue colour", "لون أزرق داكن"), ("Agglutination", "التلازن")],
   "Step 3: note whether or not bubbles form.", "الخطوة 3: لاحظ تكوّن الفقاعات أو عدمه."),
 Q("In the catalase test, the colony is transferred to the slide using:", "في اختبار الكاتاليز تُنقل المستعمرة إلى الشريحة بـ:",
   [("A wooden stick", "عود خشبي"), ("A metal loop", "عروة معدنية"), ("A pipette", "ماصّة"), ("A swab", "مسحة")],
   "Step 1 (a wooden stick, not a metal loop).", "الخطوة 1 (عود خشبي لا عروة معدنية)."),
 Q("Catalase-positive and catalase-negative genera on the slide are:", "الجنسان موجب وسالب الكاتاليز في الشريحة:",
   [(S("Staphylococcus") + " positive, " + S("Streptococcus") + " negative", "العنقودية موجبة، العقدية سالبة"),
    (S("Streptococcus") + " positive, " + S("Staphylococcus") + " negative", "العقدية موجبة، العنقودية سالبة"),
    ("Both positive", "كلاهما موجب"), ("Both negative", "كلاهما سالب")],
   "Circled in class.", "مؤطَّرة بالمحاضرة."),
 Q("The image shows the catalase test. The reagent in the bottle is:", "تبيّن الصورة اختبار الكاتاليز. الكاشف في القنينة:",
   [("Hydrogen peroxide (`H2O2`)", "بيروكسيد الهيدروجين (`H2O2`)"), ("Kovac's reagent", "كاشف كوفاك"), ("Methyl red", "المثيل الأحمر"), ("Blood plasma", "بلازما الدم")],
   "Class note: the reagent is H2O2.", "ملاحظة المحاضرة: الكاشف هو H2O2.", img="catalase-test.png", h="36mm"),
 Q("Class note: colonies for the catalase test should NOT be taken from blood or chocolate agar because:", "ملاحظة المحاضرة: لا تؤخذ مستعمرات اختبار الكاتاليز من أجار الدم أو الشوكولاتة لأن:",
   [("The red blood cells contain catalase and give false bubbles", "الكريات الحمر تحتوي الكاتاليز وتعطي فقاعات كاذبة"), ("The colonies are too small", "المستعمرات صغيرة جدًّا"),
    ("Blood inhibits catalase", "الدم يثبّط الكاتاليز"), ("The colour hides the result", "اللون يخفي النتيجة")],
   "Handwritten: use nutrient agar; RBCs give a false (positive) result.", "مكتوب بخط اليد: استعمل الأجار المغذّي؛ الكريات الحمر تعطي نتيجة (موجبة) كاذبة."),

 T("2. Indole test", "2. اختبار الإندول"),
 Q("The indole test determines the ability of the organism to convert tryptophan into:", "يحدّد اختبار الإندول قدرة الكائن على تحويل التربتوفان إلى:",
   [("Indole, pyruvic acid and ammonia", "إندول وحمض البيروفيك وأمونيا"), ("Water and oxygen", "ماء وأكسجين"), ("Ammonia and CO2 only", "أمونيا وCO2 فقط"), ("Fibrin", "فيبرين")],
   "By the enzyme tryptophanase.", "بإنزيم التربتوفانيز."),
 Q("The enzyme responsible for the indole test is:", "الإنزيم المسؤول عن اختبار الإندول:",
   [("Tryptophanase", "التربتوفانيز"), ("Catalase", "الكاتاليز"), ("Urease", "اليورييز"), ("Citrate permease", "ناقل السترات")],
   "Slide 5.", "الشريحة 5."),
 Q("Indole is detected by adding:", "يُكشف الإندول بإضافة:",
   [("Kovac's reagent", "كاشف كوفاك"), ("Methyl red", "المثيل الأحمر"), ("Hydrogen peroxide", "بيروكسيد الهيدروجين"), ("Bromothymol blue", "أزرق البروموثيمول")],
   "5 drops of Kovac's reagent.", "5 قطرات من كاشف كوفاك."),
 Q("A positive indole test appears as:", "تظهر نتيجة الإندول الموجبة كـ:",
   [("A bright red ring on the surface of the medium", "حلقة حمراء زاهية على سطح الوسط"), ("Bubbles", "فقاعات"), ("A blue slant", "سطح مائل أزرق"), ("A black precipitate", "راسب أسود")],
   "Red colour in the upper organic layer.", "لون أحمر في الطبقة العضوية العليا."),
 Q("The medium inoculated for the indole test is:", "الوسط الذي يُلقَّح لاختبار الإندول:",
   [("Peptone water (rich in tryptophan)", "ماء الببتون (غني بالتربتوفان)"), ("Simmons citrate agar", "أجار سيمونز سترات"), ("Urea agar", "أجار اليوريا"), ("MR-VP broth", "مرق MR-VP")],
   "Incubated at 37 °C for 24 hours. (Class note: tryptone broth.)", "يُحضن عند 37 درجة لمدّة 24 ساعة. (ملاحظة المحاضرة: مرق التربتون.)"),
 Q("Indole-positive and indole-negative examples on the slide are:", "مثالا موجب وسالب الإندول في الشريحة:",
   [(S("E. coli") + " positive, " + S("Pseudomonas aeruginosa") + " negative", "الإشريكية موجبة، الزائفة الزنجارية سالبة"),
    (S("Pseudomonas aeruginosa") + " positive, " + S("E. coli") + " negative", "الزائفة موجبة، الإشريكية سالبة"),
    (S("Klebsiella") + " positive, " + S("E. coli") + " negative", "الكلبسيلة موجبة، الإشريكية سالبة"), (S("Staphylococcus") + " positive", "العنقودية موجبة")],
   "Slide 6.", "الشريحة 6."),
 Q("In the image of the indole test, the tube on the left with a red ring at the top is:", "في صورة اختبار الإندول، الأنبوب الأيسر ذو الحلقة الحمراء في الأعلى:",
   [("Indole positive", "موجب الإندول"), ("Indole negative", "سالب الإندول"), ("Catalase positive", "موجب الكاتاليز"), ("Uninoculated", "غير ملقَّح")],
   "Red ring = positive (e.g. E. coli); yellow = negative.", "الحلقة الحمراء = موجب (مثل الإشريكية)؛ الأصفر = سالب.", img="indole-tubes.png", h="36mm"),
 Q("Class note: the indole result of " + S("Proteus vulgaris") + " and " + S("Proteus mirabilis") + " is:", "ملاحظة المحاضرة: نتيجة الإندول للمتقلّبة الشائعة والمتقلّبة الرائعة:",
   [(S("P. vulgaris") + " positive, " + S("P. mirabilis") + " negative", "الشائعة موجبة، الرائعة سالبة"),
    (S("P. vulgaris") + " negative, " + S("P. mirabilis") + " positive", "الشائعة سالبة، الرائعة موجبة"), ("Both positive", "كلاهما موجب"), ("Both negative", "كلاهما سالب")],
   "Handwritten in class: vulgaris +, mirabilis −.", "مكتوب بخط اليد: vulgaris +، mirabilis −."),

 T("3. Coagulase test", "3. اختبار الكواغيوليز"),
 Q("Coagulase is an enzyme that:", "الكواغيوليز إنزيم:",
   [("Clots plasma (fibrinogen → fibrin)", "يخثّر البلازما (فيبرينوجين ← فيبرين)"), ("Breaks hydrogen peroxide", "يحلّل بيروكسيد الهيدروجين"), ("Hydrolyzes urea", "يحلّل اليوريا"), ("Ferments lactose", "يخمّر اللاكتوز")],
   "Fibrinogen (plasma) → fibrin (clot).", "الفيبرينوجين (البلازما) ← الفيبرين (الخثرة)."),
 Q("The coagulase test can be done by:", "يمكن إجراء اختبار الكواغيوليز بطريقة:",
   [("The tube method or the slide method", "الأنبوب أو الشريحة"), ("The disk method only", "القرص فقط"), ("Filter paper", "ورق الترشيح"), ("Slant streaking", "تخطيط السطح المائل")],
   "Slide 8.", "الشريحة 8."),
 Q("In the slide coagulase method, the reagent added to the bacterial suspension is:", "في طريقة الشريحة، الكاشف المضاف إلى المعلّق البكتيري:",
   [("A drop of blood plasma", "قطرة من بلازما الدم"), ("Hydrogen peroxide", "بيروكسيد الهيدروجين"), ("Kovac's reagent", "كاشف كوفاك"), ("Methyl red", "المثيل الأحمر")],
   "Step 3.", "الخطوة 3."),
 Q("A positive slide coagulase test shows:", "تظهر نتيجة الكواغيوليز الموجبة بطريقة الشريحة كـ:",
   [("Agglutination — like " + S("Staph. aureus"), "تلازن — مثل العنقودية الذهبية"), ("No agglutination", "عدم التلازن"), ("Bubbles", "فقاعات"), ("A red ring", "حلقة حمراء")],
   "No agglutination = negative, like other staphylococci.", "عدم التلازن = سالب، مثل باقي العنقوديات."),
 Q("The image shows coagulase test results. On the slide (top), the granular clumping on the left side indicates:", "تبيّن الصورة نتائج الكواغيوليز. على الشريحة (الأعلى) التكتّل الحبيبي في الجهة اليسرى يدلّ على:",
   [("A positive coagulase result", "نتيجة كواغيوليز موجبة"), ("A negative result", "نتيجة سالبة"), ("Catalase activity", "نشاط الكاتاليز"), ("Contamination", "تلوّث")],
   "Agglutination = positive (S. aureus).", "التلازن = موجب (العنقودية الذهبية).", img="coagulase-slide-tube.png", h="42mm"),

 T("4. Methyl red (MR) test", "4. اختبار المثيل الأحمر (MR)"),
 Q("In the MR test, the acid produced decreases the pH to:", "في اختبار MR يخفّض الحامض المنتَج الأس الهيدروجيني إلى:",
   [("4.5 or below", "4.5 أو أقل"), ("7", "7"), ("9", "9"), ("6.5 or above", "6.5 أو أكثر")],
   "pH ≤ 4.5 turns methyl red from yellow to red.", "الأس ≤ 4.5 يحوّل المثيل الأحمر من الأصفر إلى الأحمر."),
 Q("In a positive MR test, methyl red changes from:", "في اختبار MR الموجب يتغيّر المثيل الأحمر من:",
   [("Yellow to red", "الأصفر إلى الأحمر"), ("Red to yellow", "الأحمر إلى الأصفر"), ("Green to blue", "الأخضر إلى الأزرق"), ("Yellow to pink", "الأصفر إلى الوردي")],
   "Red = positive; yellow = negative.", "الأحمر = موجب؛ الأصفر = سالب."),
 Q("The medium used for the MR test is:", "الوسط المستعمل لاختبار MR:",
   [("Glucose phosphate peptone water (MR-VP)", "ماء الببتون الفوسفاتي بالغلوكوز (MR-VP)"), ("Peptone water", "ماء الببتون"), ("Urea agar", "أجار اليوريا"), ("Simmons citrate", "سيمونز سترات")],
   "Incubated 24–48 h at 37 °C, then 2–3 drops of methyl red.", "يُحضن 24–48 ساعة عند 37 درجة، ثم 2–3 قطرات مثيل أحمر."),
 Q("MR-positive and MR-negative examples on the slide are:", "مثالا موجب وسالب MR في الشريحة:",
   [(S("E. coli") + " positive (red), " + S("Klebsiella") + " negative (yellow)", "الإشريكية موجبة (أحمر)، الكلبسيلة سالبة (أصفر)"),
    (S("Klebsiella") + " positive, " + S("E. coli") + " negative", "الكلبسيلة موجبة، الإشريكية سالبة"), ("Both positive", "كلاهما موجب"), (S("Proteus") + " negative", "المتقلّبة سالبة")],
   "Slide 11.", "الشريحة 11."),
 Q("Some bacteria are MR-negative because they:", "بعض البكتيريا سالبة MR لأنها:",
   [("Have special enzymes that convert the final acids into neutral substances and raise the pH", "تمتلك إنزيمات خاصة تحوّل الأحماض النهائية إلى مواد متعادلة وترفع الأس الهيدروجيني"),
    ("Cannot grow in the medium", "لا تنمو في الوسط"), ("Produce strong acids", "تنتج أحماضًا قوية"), ("Lack tryptophanase", "تفتقر إلى التربتوفانيز")],
   "The slide says bacteria “oxidize glucose”; strictly, the MR test detects glucose fermentation (mixed acids).",
   "الشريحة تقول «تؤكسد الغلوكوز»؛ والأدقّ أن اختبار MR يكشف تخمير الغلوكوز (أحماض مختلطة)."),

 T("5. Oxidase test", "5. اختبار الأوكسيديز"),
 Q("The oxidase test identifies microorganisms containing the enzyme:", "يشخّص اختبار الأوكسيديز الكائنات التي تحتوي إنزيم:",
   [("Cytochrome oxidase", "السايتوكروم أوكسيديز"), ("Catalase", "الكاتاليز"), ("Coagulase", "الكواغيوليز"), ("Urease", "اليورييز")],
   "Slide 12.", "الشريحة 12."),
 Q("In the oxidase test, a positive result is:", "في اختبار الأوكسيديز تكون النتيجة الموجبة:",
   [("Dark-blue colour within three minutes", "لون أزرق داكن خلال ثلاث دقائق"), ("Bubbles", "فقاعات"), ("Red ring", "حلقة حمراء"), ("Pink slant", "سطح مائل وردي")],
   "No colour change = negative.", "عدم تغيّر اللون = سالب."),
 Q("Oxidase-positive and oxidase-negative groups on the slide are:", "مجموعتا موجب وسالب الأوكسيديز في الشريحة:",
   [("Pseudomonadaceae positive, Enterobacteriaceae negative", "الزائفيات موجبة، البكتيريا المعوية سالبة"),
    ("Enterobacteriaceae positive, Pseudomonadaceae negative", "المعوية موجبة، الزائفيات سالبة"), ("Both positive", "كلاهما موجب"), ("Both negative", "كلاهما سالب")],
   "The slide spells “Pseudomadacea”.", "الشريحة كتبت «Pseudomadacea» وصوابها Pseudomonadaceae."),
 Q("In this oxidase test image, the right half of the filter paper is:", "في صورة اختبار الأوكسيديز هذه، النصف الأيمن من ورق الترشيح:",
   [("Positive — dark-blue/purple colour", "موجب — لون أزرق/بنفسجي داكن"), ("Negative — no colour", "سالب — بلا لون"), ("Catalase positive", "موجب الكاتاليز"), ("Uninoculated", "غير ملقَّح")],
   "Figure (1): the + side turned dark blue.", "الشكل (1): الجهة + تحوّلت إلى أزرق داكن.", img="oxidase-test.png", h="36mm"),
 Q("In the oxidase test, the bacteria are transferred to the filter paper using:", "في اختبار الأوكسيديز تُنقل البكتيريا إلى ورق الترشيح بـ:",
   [("A wooden stick", "عود خشبي"), ("A nichrome loop", "عروة نيكروم"), ("A swab dipped in alcohol", "مسحة مغموسة بالكحول"), ("A pipette", "ماصّة")],
   "Step 2: a large mass of pure bacteria with a wooden stick.", "الخطوة 2: كتلة كبيرة من بكتيريا نقية بعود خشبي."),

 T("6. Urease test", "6. اختبار اليورييز"),
 Q("Urease hydrolyzes urea into:", "يحلّل اليورييز اليوريا إلى:",
   [("Ammonia and `CO2`", "أمونيا و`CO2`"), ("Water and oxygen", "ماء وأكسجين"), ("Indole and pyruvic acid", "إندول وحمض البيروفيك"), ("Fibrin", "فيبرين")],
   "Slide 14.", "الشريحة 14."),
 Q("A positive urease test on urea agar is:", "نتيجة اليورييز الموجبة على أجار اليوريا:",
   [("Pink colour", "لون وردي"), ("Yellow colour", "لون أصفر"), ("Blue colour", "لون أزرق"), ("Black colour", "لون أسود")],
   "Ammonia raises the pH → pink; yellow = negative.", "الأمونيا ترفع الأس ← وردي؛ الأصفر = سالب."),
 Q("Urease-positive organisms on the slide include:", "الكائنات موجبة اليورييز في الشريحة تشمل:",
   [(S("Klebsiella") + ", " + S("Proteus") + " and " + S("Helicobacter pylori"), "الكلبسيلة والمتقلّبة والملوية البوابية"), (S("E. coli"), "الإشريكية القولونية"),
    (S("Pseudomonas") + " only", "الزائفة فقط"), (S("Streptococcus"), "العقدية")],
   "E. coli is urease negative (yellow).", "الإشريكية سالبة اليورييز (أصفر)."),

 T("7. Citrate test", "7. اختبار السترات"),
 Q("The citrate test detects bacteria able to use:", "يكشف اختبار السترات البكتيريا القادرة على استعمال:",
   [("Citrate as a carbon source and ammonia as a nitrogen source", "السترات مصدرًا للكربون والأمونيا مصدرًا للنيتروجين"), ("Urea as a carbon source", "اليوريا مصدرًا للكربون"),
    ("Tryptophan as a nitrogen source", "التربتوفان مصدرًا للنيتروجين"), ("Lactose only", "اللاكتوز فقط")],
   "Purpose of the test.", "غرض الاختبار."),
 Q("Bacteria that grow on citrate medium produce the enzyme:", "البكتيريا التي تنمو على وسط السترات تنتج إنزيم:",
   [("Citrate permease", "ناقل السترات (citrate permease)"), ("Tryptophanase", "التربتوفانيز"), ("Urease", "اليورييز"), ("Coagulase", "الكواغيوليز")],
   "Slide 16.", "الشريحة 16."),
 Q("The medium and indicator of the citrate test are:", "وسط اختبار السترات ومؤشّره:",
   [("Simmons citrate agar with bromothymol blue (included in the medium)", "أجار سيمونز سترات مع أزرق البروموثيمول (ضمن الوسط)"),
    ("Urea agar with phenol red", "أجار اليوريا مع الفينول الأحمر"), ("Peptone water with Kovac's", "ماء الببتون مع كوفاك"), ("MR-VP with methyl red", "MR-VP مع المثيل الأحمر")],
   "Note: the reagent is included in the medium.", "ملاحظة: الكاشف ضمن الوسط."),
 Q("In this citrate test image, the blue tube on the right is:", "في صورة اختبار السترات هذه، الأنبوب الأزرق على اليمين:",
   [("Positive — like " + S("Pseudomonas") + " spp.", "موجب — مثل الزائفة"), ("Negative — like " + S("E. coli"), "سالب — مثل الإشريكية"), ("Uninoculated", "غير ملقَّح"), ("Contaminated", "ملوَّث")],
   "Green = negative (E. coli); blue = positive (Pseudomonas spp.).", "أخضر = سالب (الإشريكية)؛ أزرق = موجب (الزائفة).", img="citrate-tubes.png", h="36mm"),
 Q("The citrate slant is incubated at 37 °C for:", "يُحضن السطح المائل للسترات عند 37 درجة لمدّة:",
   [("48 hrs", "48 ساعة"), ("3 minutes", "3 دقائق"), ("15 seconds", "15 ثانية"), ("7 days", "7 أيام")],
   "Streaked only, incubated 48 h, then observe the colour.", "يُخطَّط فقط، ويُحضن 48 ساعة، ثم يُلاحظ اللون."),

 T("8. Triple sugar iron (TSI) agar test", "8. اختبار أجار الحديد ثلاثي السكّر (TSI)"),
 Q("TSI medium contains three sugars:", "يحتوي وسط TSI على ثلاثة سكّريات:",
   [("Glucose, sucrose and lactose", "الغلوكوز والسكروز واللاكتوز"), ("Glucose, maltose and mannitol", "الغلوكوز والمالتوز والمانيتول"),
    ("Lactose, galactose and fructose", "اللاكتوز والغالاكتوز والفركتوز"), ("Sucrose, starch and dextrin", "السكروز والنشا والدكسترين")],
   "Plus ferrous sulfate and phenol red.", "بالإضافة إلى كبريتات الحديدوز والفينول الأحمر."),
 Q("TSI is used to detect:", "يُستعمل TSI للكشف عن:",
   [("Fermentation of sugars", "تخمير السكّريات"), ("Gas (`CO2`) production", "إنتاج الغاز (`CO2`)"), ("`H2S` production", "إنتاج `H2S`"), ALL],
   "Three uses.", "ثلاثة استعمالات.", fixed="d"),
 Q("If neither lactose/sucrose nor glucose is fermented, the TSI tube shows:", "إذا لم يُخمَّر اللاكتوز/السكروز ولا الغلوكوز، يظهر أنبوب TSI:",
   [("Red butt and red slant (K/K), like " + S("Pseudomonas") + " spp.", "قاع أحمر وسطح أحمر (K/K)، مثل الزائفة"),
    ("Yellow butt, red slant (K/A)", "قاع أصفر وسطح أحمر (K/A)"), ("Yellow butt and slant (A/A)", "قاع وسطح أصفران (A/A)"), ("Black butt", "قاع أسود")],
   "K = alkaline (red).", "K = قاعدي (أحمر)."),
 Q("If only glucose is fermented, the TSI result is:", "إذا خُمِّر الغلوكوز فقط تكون نتيجة TSI:",
   [("Yellow butt, red slant (K/A), like " + S("Salmonella typhi"), "قاع أصفر وسطح أحمر (K/A)، مثل السالمونيلا التيفية"),
    ("Red butt and slant (K/K)", "قاع وسطح أحمران (K/K)"), ("Yellow butt and slant (A/A)", "قاع وسطح أصفران (A/A)"), ("Blue slant", "سطح أزرق")],
   "Slant/butt: K/A. The slide spells “Slamonella”.", "السطح/القاع: K/A. والشريحة كتبت «Slamonella»."),
 Q("If lactose and sucrose are fermented, the TSI result is:", "إذا خُمِّر اللاكتوز والسكروز تكون نتيجة TSI:",
   [("Yellow butt and slant (A/A), like " + S("E. coli"), "قاع وسطح أصفران (A/A)، مثل الإشريكية"), ("K/K", "K/K"), ("K/A", "K/A"), ("Black precipitate only", "راسب أسود فقط")],
   "A = acid (yellow).", "A = حامضي (أصفر)."),
 Q("The black colour in TSI indicates:", "اللون الأسود في TSI يدلّ على:",
   [("`H2S` production (ferrous sulfide), like " + S("Proteus") + " spp.", "إنتاج `H2S` (كبريتيد الحديدوز)، مثل المتقلّبة"), ("Gas production", "إنتاج غاز"),
    ("Lactose fermentation", "تخمير اللاكتوز"), ("No fermentation", "عدم التخمير")],
   "`H2S + FeSO4 → FeS` (black).", "`H2S + FeSO4 → FeS` (أسود)."),
 Q("Gas (`CO2`) production in TSI appears as:", "يظهر إنتاج الغاز (`CO2`) في TSI كـ:",
   [("Bubbles or cracks in the medium", "فقاعات أو تشقّقات في الوسط"), ("A black colour", "لون أسود"), ("A red ring", "حلقة حمراء"), ("A blue slant", "سطح مائل أزرق")],
   "Slide 19.", "الشريحة 19."),
 Q("In TSI reading, the letters K and A mean:", "في قراءة TSI يعني الحرفان K وA:",
   [("K = alkaline (red), A = acidic (yellow)", "K = قاعدي (أحمر)، A = حامضي (أصفر)"), ("K = acidic, A = alkaline", "K = حامضي، A = قاعدي"),
    ("K = potassium, A = agar", "K = البوتاسيوم، A = الأجار"), ("K = negative, A = gas", "K = سالب، A = غاز")],
   "Figure (2) legend.", "مفتاح الشكل (2)."),
]

mcq = balance(mcq, 6606)
for q in mcq:
    if "_fixed" in q: q["answer"] = q.pop("_fixed")

meta = {"subject_en": "Diagnostic Microbiology", "subject_ar": "الأحياء المجهرية التشخيصية", "short_ar": "بكتريا",
        "instructor": "د. هبة سامي", "unit_en": "Lab 6", "unit_ar": "العملي 6", "unit_label": "LAB", "unit_no": "6",
        "title_en": "Biochemical Testing of Microorganisms", "title_ar": "الفحوص الكيميائية الحيوية للأحياء المجهرية",
        "department": "قسم التحليلات", "kind": "Laboratories — عملي", "questions_kind": "MCQ — أسئلة اختيار",
        "stage": "The fourth stage — الرابعة",
        "file_name": "BIOS - بكتريا عملي المحاضرة السادسة - بنك أسئلة شامل بالصور"}
Qs = {"title_en": "Biochemical Testing of Microorganisms — Comprehensive MCQs (with figures)",
      "title_ar": "الفحوص الكيميائية الحيوية — أسئلة اختيار شاملة (مع الصور)",
      "sub": "MCQ", "answers_inline": True, "compact": True, "mcq_per_page": 4,
      "mcq_en": "Comprehensive MCQs — Lab 6", "mcq_ar": "أسئلة اختيار شاملة — العملي السادس",
      "intro_en": ["Q. Select the most correct answer from the followings",
                   "These MCQs cover the whole lab with its own pictures; the answer and a short reason sit under each question. Questions marked “Class note” come from the handwritten notes on the slides."],
      "intro_ar": ["س. اختر الإجابة الأصح مما يأتي",
                   "هذه الأسئلة تغطّي العملي كاملًا بصوره نفسها؛ والحل وسطر سبب مختصر تحت كل سؤال. الأسئلة المعلَّمة «ملاحظة المحاضرة» مأخوذة من الملاحظات المكتوبة بخط اليد على الشرائح."],
      "mcq": ltr_all(mcq), "tf": [], "traps": [], "important": []}

d = "/home/user/-/bacteriology-lab6-mcq"
os.makedirs(d + "/assets", exist_ok=True)
for q in mcq:
    if q.get("img"):
        shutil.copy("/home/user/-/bacteriology-lab6-biochemical-tests/" + q["img"], d + "/" + q["img"])
json.dump({"meta": meta, "questions": Qs}, open(d + "/lecture.json", "w"), ensure_ascii=False, indent=1)
qs = [m for m in mcq if "answer" in m]
print("MCQ:", len(qs), "| dist:", dict(Counter(m["answer"] for m in qs)), "| images:", sum(1 for m in qs if m.get("img")))
for i, q in enumerate(qs, 1):
    print(i, q["answer"], q["options"]["abcd".index(q["answer"])][0][:60])
