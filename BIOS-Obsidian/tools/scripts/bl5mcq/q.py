import sys, json, os, shutil
from collections import Counter
WORK = "/home/claude/scratch/work"
sys.path.insert(0, WORK + "/bac"); from bal import balance
sys.path.insert(0, WORK); from bidi import ltr_all

# Diagnostic Microbiology — PRACTICAL Lab 5 (stage 4, د. هبة سامي; slides by MSc. Ali Thamer & MSc. Hiba Sami):
# Specimen Processing and Staining. Source 2026-11-22: class-annotated (Kilonotes) copy of the same 20-slide deck as
# bacteriology-lab5-staining/. Slide 2 (basic procedures) marked «كلاوات» → not asked. Handwritten beside the simple-stain
# picture: flagella → silver salt, capsule → India ink (slide 9 lists special stains; used as a class-note question).
# Pictures = clean copies in bacteriology-lab5-staining/assets; picture questions chosen so the answer is not printed in
# the picture. Slide errors flagged: acid-fast text says "acid-resistant bacteria are easy to remove" (should be
# NON-acid-fast); "the work of a bacterial membrane" = making a bacterial smear. Correct option first; fixed= for ALL.

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
 T("Microscopy and magnification", "المجهرية والتكبير"),
 Q("Microscopy is defined as:", "تُعرَّف المجهرية بأنها:",
   [("The use of a microscope to magnify objects too small to be visualized with the naked eye", "استعمال المجهر لتكبير الأجسام الصغيرة جدًّا التي لا تُرى بالعين المجرّدة"),
    ("Growing bacteria on media", "إنماء البكتيريا على الأوساط"), ("Staining bacteria only", "تصبيغ البكتيريا فقط"), ("Testing antibiotic sensitivity", "اختبار الحساسية للمضادات")],
   "Slide 3.", "الشريحة 3."),
 Q("Microscopy plays an important role in the laboratory because:", "تؤدّي المجهرية دورًا مهمًّا في المختبر لأن:",
   [("Most infectious agents cannot be detected with the unaided eye", "معظم العوامل المعدية لا تُكشف بالعين المجرّدة"), ("It is cheaper than culture", "أرخص من الزرع"),
    ("It replaces all other tests", "تغني عن كل الفحوص الأخرى"), ("It kills bacteria", "تقتل البكتيريا")],
   "Slide 3.", "الشريحة 3."),
 Q("The ocular lens of our microscope is:", "العدسة العينية في مجهرنا:",
   [("`10x`", "`10x`"), ("`4x`", "`4x`"), ("`40x`", "`40x`"), ("`100x`", "`100x`")],
   "Oculars 10x; objectives 4x, 10x, 40x, 100x.", "العينية 10x؛ الشيئية 4x و10x و40x و100x."),
 Q("The overall magnification of a light microscope equals:", "التكبير الكلّي للمجهر الضوئي يساوي:",
   [("Power of the oculars × power of the objectives", "قوّة العدسة العينية × قوّة العدسة الشيئية"), ("Power of the oculars + power of the objectives", "قوّة العينية + قوّة الشيئية"),
    ("Power of the objectives only", "قوّة الشيئية فقط"), ("Power of the oculars ÷ power of the objectives", "قوّة العينية ÷ قوّة الشيئية")],
   "Multiplied — highlighted.", "حاصل الضرب — مظلَّلة."),
 Q("With a `10x` ocular and a `40x` objective, the overall magnification is:", "بعدسة عينية `10x` وشيئية `40x` يكون التكبير الكلّي:",
   [("`400x`", "`400x`"), ("`50x`", "`50x`"), ("`40x`", "`40x`"), ("`4000x`", "`4000x`")],
   "10 × 40 = 400.", "10 × 40 = 400."),
 Q("The overall magnification with the `100x` objective is:", "التكبير الكلّي بالعدسة الشيئية `100x`:",
   [("`1000x`", "`1000x`"), ("`100x`", "`100x`"), ("`110x`", "`110x`"), ("`400x`", "`400x`")],
   "10 × 100 = 1000 (oil immersion).", "10 × 100 = 1000 (الغمر بالزيت)."),
 Q("To achieve the desired resolution at `1000x`:", "لتحقيق قوّة التمييز المطلوبة عند `1000x`:",
   [("Oil immersion must be used", "يجب استعمال الغمر بالزيت"), ("Water must be added to the slide", "يجب إضافة الماء إلى الشريحة"),
    ("The slide must be heated", "يجب تسخين الشريحة"), ("The 4x objective must be used", "يجب استعمال الشيئية 4x")],
   "Slide 5.", "الشريحة 5."),
 Q("Immersion oil fills the space between:", "يملأ زيت الغمر الفراغ بين:",
   [("The objective lens and the glass slide", "العدسة الشيئية والشريحة الزجاجية"), ("The ocular and the objective", "العينية والشيئية"),
    ("The light source and the stage", "مصدر الضوء والمنصّة"), ("The eye and the ocular", "العين والعينية")],
   "Slide 5.", "الشريحة 5."),
 Q("In the sequence of using the objectives, the drop of oil is added:", "في تسلسل استعمال العدسات الشيئية، تُضاف قطرة الزيت:",
   [("After `40x` and before `100x`", "بعد `40x` وقبل `100x`"), ("Before `4x`", "قبل `4x`"), ("After `100x`", "بعد `100x`"), ("Between `4x` and `10x`", "بين `4x` و`10x`")],
   "4x (coarse & fine) → 10x → 40x → add oil → 100x (fine focus only).", "4x (خشن ودقيق) ← 10x ← 40x ← إضافة الزيت ← 100x (ضبط دقيق فقط)."),

 T("Bacterial staining and smear preparation", "تصبيغ البكتيريا وتحضير المسحة"),
 Q("Living bacteria are generally:", "البكتيريا الحيّة عمومًا:",
   [("Colorless and difficult to view with bright-field microscopes", "عديمة اللون وصعبة الرؤية بالمجهر ذي الحقل المضيء"), ("Brightly colored", "ملوّنة بوضوح"),
    ("Visible to the naked eye", "مرئية بالعين المجرّدة"), ("Always purple", "بنفسجية دائمًا")],
   "That is why staining is needed.", "لهذا يلزم التصبيغ."),
 Q("Staining is necessary in order to:", "التصبيغ ضروري لـ:",
   [("Make bacteria visible for intracellular structures and overall morphology", "جعل البكتيريا مرئية لمشاهدة التراكيب داخل الخلية والشكل العام"), ("Kill bacteria only", "قتل البكتيريا فقط"),
    ("Grow bacteria", "إنماء البكتيريا"), ("Test sensitivity", "اختبار الحساسية")],
   "Two reasons on slide 6.", "سببان في الشريحة 6."),
 Q("A bacterial smear is:", "المسحة البكتيرية هي:",
   [("A dried preparation of bacterial cells on a glass slide", "مستحضر مجفَّف من الخلايا البكتيرية على شريحة زجاجية"), ("A liquid culture", "مزرعة سائلة"),
    ("A colony on agar", "مستعمرة على أجار"), ("A stain", "صبغة")],
   "Used to prepare a specimen for staining.", "تُستعمل لتحضير العيّنة للتصبيغ."),
 Q("In the bacterial smear procedure, the first step is:", "في إجراء المسحة البكتيرية، الخطوة الأولى:",
   [("Draw a circle on the bottom of the slide", "رسم دائرة على أسفل الشريحة"), ("Pass the slide over the flame", "تمرير الشريحة فوق اللهب"),
    ("Let it air dry", "تركها تجفّ بالهواء"), ("Add crystal violet", "إضافة البنفسج البلّوري")],
   "Circle → spread in a drop of water → air dry → flame three times.", "دائرة ← نشر بقطرة ماء ← تجفيف بالهواء ← لهب ثلاث مرّات."),
 Q("To fix the organisms, the slide is passed over the flame:", "لتثبيت الكائنات، تُمرَّر الشريحة فوق اللهب:",
   [("Three times", "ثلاث مرّات"), ("Once", "مرّة واحدة"), ("Ten times", "عشر مرّات"), ("For 5 minutes", "لمدّة 5 دقائق")],
   "Step 4.", "الخطوة 4."),
 Q("Fixation causes the specimen to:", "يؤدّي التثبيت إلى:",
   [("Adhere to the glass", "التصاق العيّنة بالزجاج"), ("Kill the microorganisms", "قتل الكائنات الدقيقة"), ("Generally preserve their shape and size", "الحفاظ عمومًا على شكلها وحجمها"), ALL],
   "Three effects of fixation.", "ثلاثة تأثيرات للتثبيت.", fixed="d"),
 Q("The figure shows the procedure for making a bacterial smear. Before heat fixing, the smear must be:", "يبيّن الشكل إجراء عمل المسحة البكتيرية. قبل التثبيت الحراري يجب أن تكون المسحة:",
   [("Air dried", "مجفَّفة بالهواء"), ("Stained with safranin", "مصبوغة بالسفرانين"), ("Covered with oil", "مغطّاة بالزيت"), ("Washed with alcohol", "مغسولة بالكحول")],
   "Smear → air dry → heat fix → stain → look.", "مسحة ← تجفيف بالهواء ← تثبيت حراري ← تصبيغ ← فحص.", img="smear-procedure.png", h="40mm"),

 T("Types of stains", "أنواع الصبغات"),
 Q("Simple stains are:", "الصبغات البسيطة هي:",
   [("Basic dyes that react with acidic substances in the cell", "أصباغ قاعدية تتفاعل مع المواد الحامضية في الخلية"), ("Acidic dyes that react with basic substances", "أصباغ حامضية تتفاعل مع المواد القاعدية"),
    ("Compound dyes using more than one dye", "أصباغ مركّبة تستعمل أكثر من صبغة"), ("Stains for capsules only", "صبغات للمحافظ فقط")],
   "Basic dye + acidic cell components.", "صبغة قاعدية + مكوّنات خلوية حامضية."),
 Q("Examples of simple stains are:", "أمثلة الصبغات البسيطة:",
   [("Carbol fuchsin, safranin and methylene blue", "الكاربول فوكسين، السفرانين، أزرق المثيلين"), ("Gram stain and acid-fast stain", "صبغة غرام وصبغة الصمود للحمض"),
    ("India ink and nigrosin", "الحبر الهندي والنيغروسين"), ("Silver salts", "أملاح الفضة")],
   "Slide 9.", "الشريحة 9."),
 Q("Differential staining:", "التصبيغ التفريقي:",
   [("Uses more than one dye and is known as the compound dye", "يستعمل أكثر من صبغة ويُعرف بالصبغة المركّبة"), ("Uses one basic dye", "يستعمل صبغة قاعدية واحدة"),
    ("Uses no dye", "لا يستعمل صبغة"), ("Stains only the background", "يصبغ الخلفية فقط")],
   "Includes Gram stain and acid-fast stain.", "يشمل صبغة غرام وصبغة الصمود للحمض."),
 Q("Which of the following is a differential stain?", "أيّ مما يأتي صبغة تفريقية؟",
   [("Gram stain", "صبغة غرام"), ("Methylene blue alone", "أزرق المثيلين وحده"), ("Safranin alone", "السفرانين وحده"), ("Nigrosin", "النيغروسين")],
   "Gram and acid-fast are differential.", "غرام والصمود للحمض تفريقيتان."),
 Q("Simple stains have an important role in recognizing:", "للصبغات البسيطة دور مهم في التعرّف على:",
   [("The shape, size and arrangement of bacteria", "شكل البكتيريا وحجمها وترتيبها"), ("Gram reaction", "تفاعل غرام"),
    ("Acid-fastness", "الصمود للحمض"), ("Capsules", "المحافظ")],
   "Helps the initial diagnosis.", "يساعد في التشخيص الأولي."),
 Q("Class note: the special stain written for flagella was:", "ملاحظة المحاضرة: الصبغة الخاصة المكتوبة للأسواط:",
   [("Silver salt", "ملح الفضة"), ("India ink", "الحبر الهندي"), ("Crystal violet", "البنفسج البلّوري"), ("Carbol fuchsin", "الكاربول فوكسين")],
   "Handwritten in class: flagella → silver salt; capsule → India ink.", "مكتوب بخط اليد بالمحاضرة: الأسواط ← ملح الفضة؛ المحفظة ← الحبر الهندي."),

 T("Gram stain", "صبغة غرام"),
 Q("The importance of the Gram stain is that it:", "أهمية صبغة غرام أنها:",
   [("Divides bacteria into Gram-negative and Gram-positive and is used for classification and differentiation", "تقسم البكتيريا إلى سالبة وموجبة غرام وتُستعمل للتصنيف والتمييز"),
    ("Detects capsules", "تكشف المحافظ"), ("Detects tuberculosis only", "تكشف السل فقط"), ("Measures magnification", "تقيس التكبير")],
   "Slide 11.", "الشريحة 11."),
 Q("In the image, the purple bacteria on the right are:", "في الصورة، البكتيريا البنفسجية على اليمين:",
   [("Gram-positive", "موجبة غرام"), ("Gram-negative", "سالبة غرام"), ("Acid-fast", "صامدة للحمض"), ("Capsulated", "ذات محافظ")],
   "Gram + = purple; Gram − = pink/red.", "موجبة = بنفسجية؛ سالبة = وردية/حمراء.", img="gram-neg-pos.png", h="36mm"),
 Q("The primary stain in the Gram stain is:", "الصبغة الأولية في صبغة غرام:",
   [("Crystal violet", "البنفسج البلّوري"), ("Safranin", "السفرانين"), ("Gram's iodine", "يود غرام"), ("Methylene blue", "أزرق المثيلين")],
   "Its function is to stain cells.", "وظيفتها صبغ الخلايا."),
 Q("Gram's iodine acts as a:", "يعمل يود غرام كـ:",
   [("Mordant that increases the cell's affinity for the stain (CV-I complex)", "مثبِّت (مرسِّخ) يزيد ألفة الخلية للصبغة (معقّد CV-I)"), ("Decolorizer", "مزيل لون"),
    ("Counterstain", "صبغة مضادّة"), ("Primary stain", "صبغة أوّلية")],
   "Mordant → crystal violet–iodine complex.", "المرسِّخ ← معقّد البنفسج البلّوري–اليود."),
 Q("The decolorizer in the Gram stain is:", "مزيل اللون في صبغة غرام:",
   [("Ethyl alcohol `95%`", "الكحول الإثيلي `95%`"), ("Acid alcohol", "الكحول الحامضي"), ("Water", "الماء"), ("Safranin", "السفرانين")],
   "Serves as a lipid solvent.", "يعمل مذيبًا للدهون."),
 Q("The action of the decolorizer is determined by:", "يتحدّد عمل مزيل اللون بـ:",
   [("The concentration of lipids and the thickness of the bacterial cell wall", "تركيز الدهون وسُمك جدار الخلية البكتيرية"), ("The temperature of the room", "حرارة الغرفة"),
    ("The colour of the stain", "لون الصبغة"), ("The size of the slide", "حجم الشريحة")],
   "Two factors (highlighted).", "عاملان (مظلَّلان)."),
 Q("The counterstain in the Gram stain is:", "الصبغة المضادّة في صبغة غرام:",
   [("Safranin", "السفرانين"), ("Crystal violet", "البنفسج البلّوري"), ("Methylene blue", "أزرق المثيلين"), ("Iodine", "اليود")],
   "Step 7: safranin for 1 min.", "الخطوة 7: السفرانين لمدّة دقيقة."),
 Q("In the Gram stain procedure, crystal violet is applied for:", "في إجراء صبغة غرام، يوضع البنفسج البلّوري لمدّة:",
   [("1 min", "دقيقة واحدة"), ("5–15 sec", "5–15 ثانية"), ("3–5 min with heat", "3–5 دقائق مع التسخين"), ("10 min", "10 دقائق")],
   "Crystal violet 1 min, iodine 1 min, alcohol 5–15 sec, safranin 1 min.", "البنفسج دقيقة، اليود دقيقة، الكحول 5–15 ثانية، السفرانين دقيقة."),
 Q("Decolorization in the Gram stain takes:", "يستغرق إزالة اللون في صبغة غرام:",
   [("5 to 15 sec with `95%` ethyl alcohol", "5 إلى 15 ثانية بالكحول الإثيلي `95%`"), ("1 min with acid alcohol", "دقيقة بالكحول الحامضي"),
    ("3–5 min", "3–5 دقائق"), ("30 min", "30 دقيقة")],
   "Step 5.", "الخطوة 5."),
 Q("The correct order of the Gram stain reagents is:", "الترتيب الصحيح لكواشف صبغة غرام:",
   [("Crystal violet → iodine → alcohol → safranin", "البنفسج البلّوري ← اليود ← الكحول ← السفرانين"), ("Safranin → alcohol → iodine → crystal violet", "السفرانين ← الكحول ← اليود ← البنفسج"),
    ("Iodine → crystal violet → safranin → alcohol", "اليود ← البنفسج ← السفرانين ← الكحول"), ("Crystal violet → alcohol → iodine → safranin", "البنفسج ← الكحول ← اليود ← السفرانين")],
   "Washing with tap water between each step.", "مع الغسل بماء الحنفية بين كل خطوة."),
 Q("After the Gram stain, the slide is examined under:", "بعد صبغة غرام تُفحص الشريحة تحت:",
   [("Oil immersion", "الغمر بالزيت"), ("The `4x` objective only", "الشيئية `4x` فقط"), ("UV light", "الأشعة فوق البنفسجية"), ("The naked eye", "العين المجرّدة")],
   "Step 9.", "الخطوة 9."),
 Q("The figure shows the four steps of the Gram stain. After the alcohol wash (step 3), Gram-negative cells appear:", "يبيّن الشكل خطوات صبغة غرام الأربع. بعد الغسل بالكحول (الخطوة 3) تظهر الخلايا سالبة غرام:",
   [("Colorless", "عديمة اللون"), ("Purple", "بنفسجية"), ("Pink", "وردية"), ("Brown", "بنّية")],
   "Alcohol removes the CV-I from Gram-negatives; they turn pink only after safranin.", "الكحول يزيل معقّد CV-I من السالبة؛ ولا تصير وردية إلّا بعد السفرانين.", img="gram-steps.png", h="42mm"),

 T("Acid-fast stain", "صبغة الصمود للحمض"),
 Q("Acid-fast (acid-resistant) bacteria are difficult to decolorize even with alcohol because they have:", "يصعب إزالة لون البكتيريا الصامدة للحمض حتى بالكحول لأنها تحتوي على:",
   [("A high content of fatty substances", "محتوى عالٍ من المواد الدهنية"), ("No cell wall", "لا جدار خلوي"), ("A capsule", "محفظة"), ("Flagella", "أسواطًا")],
   "e.g. tuberculosis bacteria.", "مثل بكتيريا السل."),
 Q("An example of acid-fast bacteria is:", "مثال على البكتيريا الصامدة للحمض:",
   [("Tuberculosis bacteria (" + S("Mycobacterium") + ")", "بكتيريا السل (المتفطّرة)"), (S("E. coli"), "الإشريكية القولونية"),
    (S("Staphylococcus"), "المكوّرات العنقودية"), (S("Cryptococcus"), "المستخفية")],
   "Slide 16.", "الشريحة 16."),
 Q("The primary dye in the acid-fast stain is:", "الصبغة الأولية في صبغة الصمود للحمض:",
   [("Basic fuchsin (carbol fuchsin)", "الفوكسين القاعدي (الكاربول فوكسين)"), ("Crystal violet", "البنفسج البلّوري"), ("Safranin", "السفرانين"), ("India ink", "الحبر الهندي")],
   "Then acid alcohol, then methylene blue.", "ثم الكحول الحامضي، ثم أزرق المثيلين."),
 Q("Heat is used in the acid-fast stain to:", "يُستعمل التسخين في صبغة الصمود للحمض لـ:",
   [("Facilitate the permeability of the dye into the cell wall", "تسهيل نفاذ الصبغة إلى الجدار الخلوي"), ("Kill the bacteria only", "قتل البكتيريا فقط"),
    ("Decolorize the cells", "إزالة لون الخلايا"), ("Dry the slide", "تجفيف الشريحة")],
   "Basic fuchsin is heated for 3–5 minutes.", "يُسخَّن الفوكسين القاعدي 3–5 دقائق."),
 Q("The decolorizer in the acid-fast stain is:", "مزيل اللون في صبغة الصمود للحمض:",
   [("Acid alcohol", "الكحول الحامضي"), ("`95%` ethyl alcohol", "الكحول الإثيلي `95%`"), ("Water", "الماء"), ("Iodine", "اليود")],
   "Added with the slide tilted.", "يُضاف والشريحة مائلة."),
 Q("The counterstain in the acid-fast stain is:", "الصبغة المضادّة في صبغة الصمود للحمض:",
   [("Methylene blue (1 min)", "أزرق المثيلين (دقيقة)"), ("Safranin", "السفرانين"), ("Crystal violet", "البنفسج البلّوري"), ("Nigrosin", "النيغروسين")],
   "Step 5.", "الخطوة 5."),
 Q("After the acid-fast stain:", "بعد صبغة الصمود للحمض:",
   [("Acid-fast cells are red and non-acid-fast cells are blue", "الخلايا الصامدة حمراء وغير الصامدة زرقاء"), ("Acid-fast cells are blue and non-acid-fast red", "الصامدة زرقاء وغير الصامدة حمراء"),
    ("All cells are purple", "كل الخلايا بنفسجية"), ("All cells are colorless", "كل الخلايا عديمة اللون")],
   "The slide text says “the acid-resistant bacteria are easy to remove and take methylene blue” — it should read NON-acid-resistant.",
   "نصّ الشريحة يقول «البكتيريا الصامدة للحمض سهلة الإزالة وتأخذ لون أزرق المثيلين» — والصواب: غير الصامدة."),
 Q("The red rods in this image of " + S("Mycobacterium leprae") + " are red because they are:", "العصيّات الحمراء في صورة المتفطّرة الجذامية حمراء لأنها:",
   [("Acid-fast — they retained carbol fuchsin", "صامدة للحمض — احتفظت بالكاربول فوكسين"), ("Gram-negative", "سالبة غرام"),
    ("Stained with safranin", "مصبوغة بالسفرانين"), ("Capsulated", "ذات محافظ")],
   "Mycobacteria are acid-fast.", "المتفطّرات صامدة للحمض.", img="m-leprae.png", h="36mm"),
 Q("In the acid-fast work steps, “the work of a bacterial membrane” (step 1) means:", "في خطوات صبغة الصمود للحمض، «the work of a bacterial membrane» (الخطوة 1) تعني:",
   [("Making a bacterial smear", "عمل مسحة بكتيرية"), ("Removing the cell membrane", "إزالة الغشاء الخلوي"), ("Staining the membrane", "صبغ الغشاء"), ("Culturing the bacteria", "زرع البكتيريا")],
   "A literal translation of «عمل مسحة بكتيرية».", "ترجمة حرفية لـ «عمل مسحة بكتيرية»."),

 T("Capsule stain", "صبغة المحفظة"),
 Q("In the capsule staining technique, the first step is mixing a loopful of bacterial suspension with:", "في تقنية صبغ المحفظة، الخطوة الأولى خلط ملء العروة من المعلّق البكتيري بـ:",
   [("A drop of India ink or nigrosin", "قطرة من الحبر الهندي أو النيغروسين"), ("Crystal violet", "البنفسج البلّوري"), ("Safranin", "السفرانين"), ("Acid alcohol", "الكحول الحامضي")],
   "Step 1.", "الخطوة 1."),
 Q("In capsule staining, the slide is flooded with:", "في صبغ المحفظة، تُغمر الشريحة بـ:",
   [("Crystal violet for 1 min", "البنفسج البلّوري لمدّة دقيقة"), ("Safranin for 1 min", "السفرانين لمدّة دقيقة"), ("Methylene blue", "أزرق المثيلين"), ("Basic fuchsin with heat", "الفوكسين القاعدي مع التسخين")],
   "Step 3.", "الخطوة 3."),
 Q("After rinsing, the capsule smear is left to air dry and NOT blot dried because blotting:", "بعد الشطف تُترك مسحة المحفظة تجفّ بالهواء ولا تُنشَّف بالورق لأن التنشيف:",
   [("Distorts the capsules", "يشوّه المحافظ"), ("Adds color", "يضيف لونًا"), ("Kills the bacteria", "يقتل البكتيريا"), ("Is too slow", "بطيء جدًّا")],
   "Step 3 note.", "ملاحظة الخطوة 3."),
 Q("In this capsule stain, the clear halo around the cells is:", "في صبغة المحفظة هذه، الهالة الصافية حول الخلايا هي:",
   [("The capsule", "المحفظة"), ("The cell wall", "الجدار الخلوي"), ("A spore", "بوغ"), ("The flagellum", "السوط")],
   "Dark background, violet bacteria, halo = capsule (Cryptococcus neoformans in India ink on the right).",
   "خلفية داكنة، بكتيريا بنفسجية، والهالة = المحفظة (المستخفية المورّمة بالحبر الهندي على اليمين).", img="capsule-microscopy.png", h="38mm"),
 Q("In capsule staining, the background appears:", "في صبغ المحفظة تظهر الخلفية:",
   [("Black or grey", "سوداء أو رمادية"), ("Pink", "وردية"), ("Colorless", "عديمة اللون"), ("Blue", "زرقاء")],
   "India ink/nigrosin colour the background (negative staining).", "الحبر الهندي/النيغروسين يلوّنان الخلفية (تصبيغ سلبي)."),
]

mcq = balance(mcq, 5505)
for q in mcq:
    if "_fixed" in q: q["answer"] = q.pop("_fixed")

meta = {"subject_en": "Diagnostic Microbiology", "subject_ar": "الأحياء المجهرية التشخيصية", "short_ar": "بكتريا",
        "instructor": "د. هبة سامي", "unit_en": "Lab 5", "unit_ar": "العملي 5", "unit_label": "LAB", "unit_no": "5",
        "title_en": "Specimen Processing and Staining", "title_ar": "معالجة العيّنات والتصبيغ",
        "department": "قسم التحليلات", "kind": "Laboratories — عملي", "questions_kind": "MCQ — أسئلة اختيار",
        "stage": "The fourth stage — الرابعة",
        "file_name": "BIOS - بكتريا عملي المحاضرة الخامسة - بنك أسئلة شامل بالصور"}
Qs = {"title_en": "Specimen Processing and Staining — Comprehensive MCQs (with figures)",
      "title_ar": "معالجة العيّنات والتصبيغ — أسئلة اختيار شاملة (مع الصور)",
      "sub": "MCQ", "answers_inline": True, "compact": True, "mcq_per_page": 4,
      "mcq_en": "Comprehensive MCQs — Lab 5", "mcq_ar": "أسئلة اختيار شاملة — العملي الخامس",
      "intro_en": ["Q. Select the most correct answer from the followings",
                   "These MCQs cover the whole lab with its own pictures; the answer and a short reason sit under each question. Slide 2 (basic procedures) was marked as not required in class and is not asked. A BIOS note points out a slide error in the acid-fast stain."],
      "intro_ar": ["س. اختر الإجابة الأصح مما يأتي",
                   "هذه الأسئلة تغطّي العملي كاملًا بصوره نفسها؛ والحل وسطر سبب مختصر تحت كل سؤال. الشريحة 2 (الإجراءات الأساسية) أُشّر عليها بالمحاضرة أنها غير مطلوبة فلم تُسأل. وملاحظة BIOS تنبّه على خطأ في شريحة صبغة الصمود للحمض."],
      "mcq": ltr_all(mcq), "tf": [], "traps": [], "important": []}

d = "/home/user/-/bacteriology-lab5-mcq"
os.makedirs(d + "/assets", exist_ok=True)
for q in mcq:
    if q.get("img"):
        shutil.copy("/home/user/-/bacteriology-lab5-staining/" + q["img"], d + "/" + q["img"])
json.dump({"meta": meta, "questions": Qs}, open(d + "/lecture.json", "w"), ensure_ascii=False, indent=1)
qs = [m for m in mcq if "answer" in m]
print("MCQ:", len(qs), "| dist:", dict(Counter(m["answer"] for m in qs)), "| images:", sum(1 for m in qs if m.get("img")))
for i, q in enumerate(qs, 1):
    print(i, q["answer"], q["options"]["abcd".index(q["answer"])][0][:60])
