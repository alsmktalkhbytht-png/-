---
source: BIOS-Obsidian/tools/scripts/ha/h3.py
handouts: [nursing-ha-lec3-ear]
saved: 2026-11-08
tags: [bios, code]
---
# ha/h3.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#nursing-ha-lec3-ear|nursing-ha-lec3-ear]]

```python
import sys; sys.path.insert(0, "/tmp/claude-0/-home-user--/67d83c9a-7b0e-5ae5-b52b-cd659ab074ab/scratchpad/ha")
from common_ha import *

def STEPS(en, ar, title_en="**Procedure:**", title_ar="**الإجراء:**"):
    return L(en, ar, en=title_en, ar=title_ar)
def NF(en, ar):
    return T([B("Normal findings", "النتائج الطبيعية")], [[B(e, a)] for e, a in zip(en, ar)], widths=[100])

blocks = [
 SEC("Objectives and preparation", "الأهداف والتحضير"),
 H2("Ear Assessment", "تقييم الأذن"),
 L(["Demonstrate the ability to safely and accurately complete the ear assessment.",
    "Demonstrate the ability to accurately document ear assessment in organized manner."],
   ["إظهار القدرة على إكمال تقييم الأذن بأمان ودقّة.", "إظهار القدرة على توثيق تقييم الأذن بدقّة وبطريقة منظّمة."],
   en="**Objectives: -** At the end of this lab the student will be able to: -", ar="**الأهداف:** في نهاية هذا الدرس سيكون الطالب قادرًا على:"),
 L(["Otoscope with bright light.", "Tunning forks."], ["منظار الأذن بضوء ساطع.", "الشوكات الرنّانة."], en="**Equipment needed: -**", ar="**الأدوات المطلوبة:**"),
 L(["Position the adult sitting up straight with his or her head at your eye level.",
    "If ear canal is obstructed with cerumen, the preferred method for cleaning by softening cerumen with warmed solution of mineral oil hydrogen peroxide.",
],
   ["ضع البالغ جالسًا مستقيمًا ورأسه بمستوى عينيك.",
    "إذا كانت قناة الأذن مسدودة بالصملاخ (شمع الأذن)، فالطريقة المفضّلة للتنظيف هي تليين الصملاخ بمحلول دافئ من الزيت المعدني بيروكسيد الهيدروجين.",
], en="**Preparation: -**", ar="**التحضير:**"),
 L(["Irrigate the canal with warm water", "Do not irrigate if the history or the examination suggests perforation or infection."],
   ["اغسل القناة بماء دافئ", "لا تغسل القناة إذا أشار التاريخ أو الفحص إلى ثقب أو عدوى."], start=3),
 T([B("Subjective data: -", "البيانات الذاتية:"), B("", "")],
   [[B("1. Earaches.", "1. ألم الأذن."), B("2. Hearing loss.", "2. فقدان السمع.")],
    [B("4. Infections.", "4. العدوى (الالتهابات)."), B("5. Environmental noise.", "5. الضوضاء البيئية.")],
    [B("7. Discharges.", "7. الإفرازات."), B("8. Tinnitus.", "8. الطنين.")]], widths=[50, 50]),
 dict(t="figures", keep=True, items=[dict(src="assets/otoscope.jpg", en="Examining the ear canal and eardrum with the otoscope", ar="فحص قناة الأذن وطبلتها بمنظار الأذن", h="40mm", fit="contain"),
   dict(src="assets/otoscope-exam.jpg", en="Otoscopic examination of the ear", ar="فحص الأذن بالمنظار", h="40mm", fit="contain")]),
 LBT(("Ear canal", "قناة الأذن"), ("Eardrum", "طبلة الأذن"), ("Otoscope", "منظار الأذن")),
 INSHORT([("Equipment: **otoscope** with bright light + **tuning forks**.", "الأدوات: **منظار الأذن** بضوء ساطع + **الشوكات الرنّانة**."),
          ("Cerumen is softened with a warmed solution, then the canal is irrigated with **warm water** — **not** if perforation or infection is suspected.", "يُليَّن الصملاخ بمحلول دافئ ثم تُغسل القناة بـ**ماء دافئ** — و**لا** تُغسل عند الشك بثقب أو عدوى.")]),

 SEC("External ear and mastoid", "الأذن الخارجية والناتئ الخشائي"),
 H2("Inspect external ear for the following:-", "افحص الأذن الخارجية بالنظر من حيث ما يلي:"),
 PN([("Size and shape", "الحجم والشكل", "Ears of equal size and similar appearance.", "أذنان متساويتان في الحجم ومتشابهتان في المظهر."),
      ("Position", "الموضع", "Alignment of pinna with corner of eye and within 10 degree angle of vertical position.", "يحاذي الصيوان زاوية العين، وضمن زاوية `10` درجات من الوضع العمودي."),
      ("Lesions and discoloration", "الآفات وتغيّر اللون", "Skin smooth and without nodules, color pink.", "الجلد أملس وبلا عقيدات، ولونه وردي."),
      ("Palpate external ear:-", "جُسّ الأذن الخارجية:", "Non tender auricle, tragus.", "الصيوان والزنمة غير مؤلمين.")]),
 H2("Palpate mastoid process for the following:-", "جُسّ الناتئ الخشائي من حيث ما يلي:"),
 PN([("Tenderness", "الإيلام", "No tender or pain when palpated.", "لا إيلام ولا ألم عند الجسّ."),
      ("Temperature", "الحرارة", "Warm.", "دافئ."),
      ("Edema", "الوذمة", "Mastoid process easily palpated.", "يُجسّ الناتئ الخشائي بسهولة.")]),
 INSHORT([("Ears equal; pinna aligned with the **corner of the eye**, within **10°** of vertical.", "الأذنان متساويتان؛ والصيوان يحاذي **زاوية العين** وضمن **`10°`** من العمودي."),
          ("Auricle and tragus **non-tender**; mastoid warm, non-tender, easily palpated.", "الصيوان والزنمة **غير مؤلمين**؛ والناتئ الخشائي دافئ وغير مؤلم ويُجسّ بسهولة.")]),

 SEC("Otoscopic examination", "الفحص بمنظار الأذن"),
 H2("Inspect auditory canal using otoscope for the following:-", "افحص القناة السمعية بمنظار الأذن من حيث ما يلي:"),
 PN([("Cerumen", "الصملاخ", "**Color**: black, dark red, gray, or brown. **Consistency**: waxy, flaky, soft, or hard. **Odor**: non.",
      "**اللون**: أسود، أو أحمر داكن، أو رمادي، أو بنّي. **القوام**: شمعي، أو متقشّر، أو طري، أو صلب. **الرائحة**: لا توجد."),
      ("Appearance", "المظهر", "Canal walls pink and uniform with tympanic membrane visible.", "جدران القناة وردية ومتجانسة والغشاء الطبلي مرئي."),
      ("Tenderness", "الإيلام", "Little or no discomfort on manipulation of pinna; inner two third of canal very tender if touched with speculum.",
       "انزعاج قليل أو معدوم عند تحريك الصيوان؛ والثلثان الداخليان من القناة مؤلمان جدًا إذا لُمسا بالمنظار.")]),
 H2("Inspect tympanic membrane using otoscope for following:-", "افحص الغشاء الطبلي بمنظار الأذن من حيث ما يلي:"),
 PN([("Color", "اللون", "Pearly gray , shiny, & translucent", "رمادي لؤلؤي، ولامع، وشفّاف"),
      ("Consistency", "القوام", "Intact: - may show movement when swallowing.", "سليم: قد يُظهر حركة عند البلع."),
      ("Landmark", "المعالم", "Cone of light, umbo, handle of malleus & short process of malleus easily visualized.", "يُرى مخروط الضوء، والسُّرّة، ومقبض المطرقة، والناتئ القصير للمطرقة بسهولة.")]),
 INSHORT([("Cerumen: black, dark red, gray or brown; **no odor**.", "الصملاخ: أسود أو أحمر داكن أو رمادي أو بنّي؛ و**بلا رائحة**."),
          ("Tympanic membrane: **pearly gray, shiny, translucent**, intact; landmarks: **cone of light, umbo, handle and short process of malleus**.", "الغشاء الطبلي: **رمادي لؤلؤي، لامع، شفّاف**، وسليم؛ ومعالمه: **مخروط الضوء، والسُّرّة، ومقبض المطرقة وناتئها القصير**.")]),

 SEC("Auditory function", "وظيفة السمع"),
 H2("Assess auditory function for the following :-", "قيّم وظيفة السمع من حيث ما يلي:"),
 STEPS(["Test one ear at a time while masking hearing in the other ear.",
        "Shield your lips so the client cannot compensate for hearing loss by lip reading or using the good ear.",
        "Stand 30 to 60cm (1-2ft) from the client’s ear.",
        "Exhale & whisper slowly some tow syllable words, such as, armchair, baseball.",
        "Ask the client to repeat what you said."],
       ["افحص أذنًا واحدة في كل مرة مع حجب السمع في الأذن الأخرى.",
        "احجب شفتيك حتى لا يعوّض المريض فقدان السمع بقراءة الشفاه أو باستعمال الأذن السليمة.",
        "قف على بُعد `30 to 60cm` (`1-2ft`) من أذن المريض.",
        "ازفر وهمس ببطء بعض الكلمات ذات المقطعين، مثل `armchair` و`baseball`.",
        "اطلب من المريض تكرار ما قلته."], "**a) Voice test**", "**أ) اختبار الصوت (الهمس)**"),
 NF(["The client is able to hear whispered word from 1-2 ft."], ["يستطيع المريض سماع الكلمة المهموسة من `1-2 ft`."]),
 STEPS(["Place a vibrating tuning fork in the middle of the client’s skull.", "Ask if the ton sounds the same in both ears or better in one."],
       ["ضع شوكة رنّانة مهتزّة في منتصف جمجمة المريض.", "اسأله هل النغمة تُسمع متساوية في الأذنين أم أوضح في إحداهما."],
       "**b) Lateralization of sound (weber test):-**", "**ب) تحديد جانب الصوت (اختبار ويبر):**"),
 NF(["Vibration heard equally in both ears."], ["يُسمع الاهتزاز بالتساوي في الأذنين."]),
 F("weber.jpg", "Weber test: vibrating tuning fork in the middle of the skull", "اختبار ويبر: شوكة رنّانة مهتزّة في منتصف الجمجمة", h="48mm", fit="contain"),
 STEPS(["Place the stem of the vibrating tuning fork on the client’s mastoid process.", "Ask him to signal when the sound goes away.",
        "Quickly invert the fork so the vibrating end is near canal.", "Repeat with the other ear."],
       ["ضع ساق الشوكة الرنّانة المهتزّة على الناتئ الخشائي للمريض.", "اطلب منه أن يشير عندما يختفي الصوت.",
        "اقلب الشوكة بسرعة بحيث يكون الطرف المهتزّ قرب القناة.", "كرّر مع الأذن الأخرى."],
       "**c) Comparison of air conduction (AC) to bone conduction (BC) (Rinne test ):-**", "**ج) مقارنة التوصيل الهوائي (`AC`) بالتوصيل العظمي (`BC`) (اختبار رينّي):**"),
 NF(["AC >BC (AC is twice as long as BC)."], ["`AC > BC` (التوصيل الهوائي ضعف مدّة التوصيل العظمي)."]),
 F("bc-ac.jpg", "Rinne test: bone conduction then air conduction", "اختبار رينّي: التوصيل العظمي ثم الهوائي", h="46mm", fit="contain", keep=True),
 LBT(("Bone Conduction (BC)", "التوصيل العظمي"), ("Air Conduction (AC)", "التوصيل الهوائي")),
 INSHORT([("Voice test: stand **30–60 cm**, whisper two-syllable words; normal hears at **1–2 ft**.", "اختبار الهمس: قف على **`30–60 cm`** وهمس بكلمات من مقطعين؛ والطبيعي يسمع من **`1–2 ft`**."),
          ("**Weber**: fork on the middle of the skull → heard **equally** in both ears.", "**ويبر**: الشوكة على منتصف الجمجمة ← تُسمع **بالتساوي** في الأذنين."),
          ("**Rinne**: mastoid then canal → **AC > BC** (AC twice as long).", "**رينّي**: الخشائي ثم القناة ← **`AC > BC`** (الهوائي ضعف المدّة).")]),

 SEC("Equilibrium", "التوازن"),
 STEPS(["Let the client stand with feet together.", "First, with eye opening.", "Then With eyes closed.", "Put your arms around client to prevent fail."],
       ["اجعل المريض يقف وقدماه متلاصقتان.", "أولًا مع فتح العينين.", "ثم مع إغلاق العينين.", "ضع ذراعيك حول المريض لمنع سقوطه."],
       "**Perform (Romberg test) for equilibrium:-**", "**أجرِ (اختبار رومبرغ) للتوازن:**"),
 NF(["Client stands straight with minimal swaying."], ["يقف المريض مستقيمًا مع تمايل قليل."]),
 INSHORT([("**Romberg**: feet together, eyes open then closed → stands straight with **minimal swaying**.", "**رومبرغ**: القدمان متلاصقتان، والعينان مفتوحتان ثم مغلقتان ← يقف مستقيمًا مع **تمايل قليل**.")]),
] + TERMS([
 ("Otoscope", "منظار الأذن"), ("Tuning fork", "الشوكة الرنّانة"), ("Cerumen", "الصملاخ / شمع الأذن"), ("Pinna / auricle", "الصيوان / صيوان الأذن"),
 ("Tragus", "الزنمة / الوتدة"), ("Mastoid process", "الناتئ الخشائي / عظم خلف الأذن"), ("Tympanic membrane", "الغشاء الطبلي / طبلة الأذن"),
 ("Umbo", "السُّرّة (مركز الطبلة)"), ("Malleus", "المطرقة"), ("Cone of light", "مخروط الضوء / المنعكس الضوئي"),
 ("Air conduction (AC)", "التوصيل الهوائي"), ("Bone conduction (BC)", "التوصيل العظمي"), ("Lateralization", "تحديد الجانب / الانحياز الجانبي للصوت"),
 ("Tinnitus", "الطنين / رنين الأذن"), ("Equilibrium", "التوازن"), ("Perforation", "الثقب / الانثقاب"),
])

mcq = [
 {"topic_en": "Preparation and external ear", "topic_ar": "التحضير والأذن الخارجية"},
 Q("The equipment needed for ear assessment is:", "أدوات تقييم الأذن:", [("Otoscope and tuning forks", "منظار الأذن والشوكات الرنّانة"), ("Ophthalmoscope and Snellen chart", "منظار العين ولوحة سنلن"), ("Stethoscope and ruler", "سمّاعة ومسطرة"), ("Tongue blade and gauze", "خافض لسان وشاش")], "a"),
 Q("Cerumen obstructing the canal is cleaned by first:", "يُنظَّف الصملاخ الساد للقناة أولًا بـ:", [("Removing it with forceps", "إزالته بملقط"), ("Softening it with a warmed solution", "تليينه بمحلول دافئ"), ("Cold water irrigation", "الغسل بماء بارد"), ("Cotton swabs", "أعواد القطن")], "b"),
 Q("Irrigation of the ear canal is contraindicated when there is:", "يُمنع غسل قناة الأذن عند وجود:", [("Cerumen", "صملاخ"), ("Tinnitus", "طنين"), ("Perforation or infection", "ثقب أو عدوى"), ("Hearing loss", "فقدان سمع")], "c"),
 Q("The ear canal is irrigated with:", "تُغسل قناة الأذن بـ:", [("Cold water", "ماء بارد"), ("Alcohol", "كحول"), ("Hot oil", "زيت ساخن"), ("Warm water", "ماء دافئ")], "d"),
 Q("The normal pinna is aligned with:", "يحاذي الصيوان الطبيعي:", [("The corner of the eye", "زاوية العين"), ("The tip of the nose", "طرف الأنف"), ("The chin", "الذقن"), ("The eyebrow", "الحاجب")], "a"),
 Q("The pinna normally lies within ___ of the vertical position:", "يقع الصيوان طبيعيًا ضمن ___ من الوضع العمودي:", [("45 degree", "45 درجة"), ("10 degree", "10 درجات"), ("30 degree", "30 درجة"), ("90 degree", "90 درجة")], "b"),
 Q("The normal mastoid process is:", "الناتئ الخشائي الطبيعي:", [("Tender and hot", "مؤلم وساخن"), ("Edematous", "متوذّم"), ("Warm, non-tender, easily palpated", "دافئ وغير مؤلم ويُجسّ بسهولة"), ("Not palpable", "لا يُجسّ")], "c"),
 {"topic_en": "Otoscope", "topic_ar": "منظار الأذن"},
 Q("The normal odor of cerumen is:", "رائحة الصملاخ الطبيعية:", [("Foul", "كريهة"), ("Sweet", "حلوة"), ("Sour", "حامضة"), ("None", "لا توجد")], "d"),
 Q("Which is NOT a normal color of cerumen?", "أيّها ليس لونًا طبيعيًا للصملاخ؟", [("Green", "أخضر"), ("Black", "أسود"), ("Gray", "رمادي"), ("Brown", "بنّي")], "a"),
 Q("The part of the canal that is very tender if touched with the speculum:", "جزء القناة المؤلم جدًا إذا لُمس بالمنظار:", [("Outer one third", "الثلث الخارجي"), ("Inner two third", "الثلثان الداخليان"), ("Tragus", "الزنمة"), ("Pinna", "الصيوان")], "b"),
 Q("The normal tympanic membrane color is:", "لون الغشاء الطبلي الطبيعي:", [("Red and bulging", "أحمر ومنتفخ"), ("Yellow", "أصفر"), ("Pearly gray, shiny & translucent", "رمادي لؤلؤي لامع وشفّاف"), ("White and opaque", "أبيض ومعتم")], "c"),
 Q("The landmarks of the tympanic membrane include all EXCEPT:", "معالم الغشاء الطبلي تشمل كل ما يلي عدا:", [("Cone of light", "مخروط الضوء"), ("Umbo", "السُّرّة"), ("Handle of malleus", "مقبض المطرقة"), ("Tragus", "الزنمة")], "d"),
 Q("The intact tympanic membrane may show movement when:", "قد يُظهر الغشاء الطبلي السليم حركة عند:", [("Swallowing", "البلع"), ("Blinking", "الرمش"), ("Coughing only", "السعال فقط"), ("Standing", "الوقوف")], "a"),
 {"topic_en": "Hearing tests", "topic_ar": "اختبارات السمع"},
 Q("In the voice test, the examiner stands from the client's ear at:", "في اختبار الصوت يقف الفاحص من أذن المريض على بُعد:", [("10 cm", "10 سم"), ("30 to 60 cm (1-2 ft)", "30 إلى 60 سم (1-2 قدم)"), ("20 feet", "20 قدمًا"), ("3 m", "3 م")], "b"),
 Q("The examiner shields the lips during the voice test to prevent:", "يحجب الفاحص شفتيه في اختبار الصوت لمنع:", [("Infection", "العدوى"), ("Loud sound", "الصوت العالي"), ("Lip reading", "قراءة الشفاه"), ("Swallowing", "البلع")], "c"),
 Q("The words whispered in the voice test are:", "الكلمات المهموسة في اختبار الصوت:", [("Numbers only", "أرقام فقط"), ("One-syllable words", "كلمات من مقطع واحد"), ("Long sentences", "جمل طويلة"), ("Two syllable words like armchair, baseball", "كلمات من مقطعين مثل armchair وbaseball")], "d"),
 Q("In the Weber test, the tuning fork is placed:", "في اختبار ويبر توضع الشوكة الرنّانة:", [("In the middle of the client's skull", "في منتصف جمجمة المريض"), ("On the mastoid process", "على الناتئ الخشائي"), ("Near the canal", "قرب القناة"), ("On the chest", "على الصدر")], "a"),
 Q("The normal Weber test result is:", "النتيجة الطبيعية لاختبار ويبر:", [("Heard better in the right ear", "يُسمع أوضح في اليمنى"), ("Vibration heard equally in both ears", "يُسمع الاهتزاز بالتساوي في الأذنين"), ("Not heard", "لا يُسمع"), ("BC > AC", "BC > AC")], "b"),
 Q("The Rinne test compares:", "يقارن اختبار رينّي بين:", [("Right and left ears", "الأذن اليمنى واليسرى"), ("Whisper and voice", "الهمس والصوت"), ("Air conduction and bone conduction", "التوصيل الهوائي والعظمي"), ("Balance and hearing", "التوازن والسمع")], "c"),
 Q("The normal Rinne test result is:", "النتيجة الطبيعية لاختبار رينّي:", [("BC > AC", "BC > AC"), ("AC = BC", "AC = BC"), ("BC twice AC", "BC ضعف AC"), ("AC > BC (AC twice as long as BC)", "AC > BC (الهوائي ضعف العظمي)")], "d"),
 Q("In the Rinne test, the stem of the fork is first placed on the:", "في اختبار رينّي يوضع ساق الشوكة أولًا على:", [("Mastoid process", "الناتئ الخشائي"), ("Forehead", "الجبهة"), ("Tragus", "الزنمة"), ("Middle of the skull", "منتصف الجمجمة")], "a"),
 Q("The Romberg test assesses:", "يقيّم اختبار رومبرغ:", [("Hearing", "السمع"), ("Equilibrium", "التوازن"), ("Cerumen", "الصملاخ"), ("Tympanic membrane", "الغشاء الطبلي")], "b"),
 Q("The normal Romberg result is:", "النتيجة الطبيعية لاختبار رومبرغ:", [("Falls to one side", "يسقط لجانب"), ("Cannot stand with eyes closed", "لا يستطيع الوقوف مغمض العينين"), ("Stands straight with minimal swaying", "يقف مستقيمًا مع تمايل قليل"), ("Marked swaying", "تمايل شديد")], "c"),
 Q("Picture: this test is the:", "صورة: هذا الاختبار هو:", [("Rinne test", "اختبار رينّي"), ("Romberg test", "اختبار رومبرغ"), ("Voice test", "اختبار الصوت"), ("Weber test", "اختبار ويبر")], "d", img="assets/weber.jpg", img_h="36mm"),
 Q("Picture: the two positions shown are used in the:", "صورة: الوضعان الظاهران يُستعملان في:", [("Rinne test (BC and AC)", "اختبار رينّي (العظمي والهوائي)"), ("Weber test", "اختبار ويبر"), ("Romberg test", "اختبار رومبرغ"), ("Otoscopy", "الفحص بالمنظار")], "a", img="assets/bc-ac.jpg", img_h="32mm"),
]
mcq = balance(mcq, 33)
tf = [
 TF("Ears of equal size and similar appearance are normal.", "الأذنان المتساويتان والمتشابهتان طبيعيتان.", "T"),
 TF("The ear canal can be irrigated even if perforation is suspected.", "يمكن غسل قناة الأذن حتى عند الشك بثقب.", "F"),
 TF("The auricle and tragus are normally non-tender.", "الصيوان والزنمة غير مؤلمين طبيعيًا.", "T"),
 TF("Normal cerumen has a foul odor.", "الصملاخ الطبيعي له رائحة كريهة.", "F"),
 TF("The tympanic membrane is normally pearly gray, shiny and translucent.", "الغشاء الطبلي طبيعيًا رمادي لؤلؤي لامع وشفّاف.", "T"),
 TF("In the voice test, both ears are tested together.", "في اختبار الصوت تُفحص الأذنان معًا.", "F"),
 TF("The normal client hears a whispered word from 1-2 ft.", "يسمع المريض الطبيعي الكلمة المهموسة من 1-2 قدم.", "T"),
 TF("In the Weber test, the fork is placed on the mastoid process.", "في اختبار ويبر توضع الشوكة على الناتئ الخشائي.", "F"),
 TF("In a normal Rinne test, AC is twice as long as BC.", "في اختبار رينّي الطبيعي يكون الهوائي ضعف مدّة العظمي.", "T"),
 TF("The Romberg test is done first with eyes open, then with eyes closed.", "يُجرى اختبار رومبرغ أولًا بعينين مفتوحتين ثم مغلقتين.", "T"),
 TF("The outer two third of the canal is very tender to the speculum.", "الثلثان الخارجيان من القناة مؤلمان جدًا للمنظار.", "F"),
 TF("The examiner puts the arms around the client during the Romberg test to prevent falling.", "يضع الفاحص ذراعيه حول المريض في اختبار رومبرغ لمنع سقوطه.", "T"),
]
traps = [
 TR("Weber vs Rinne", "ويبر مقابل رينّي", "Weber: fork in the middle of the skull → heard equally in both ears. Rinne: fork on the mastoid then near the canal → AC > BC.", "ويبر: الشوكة في منتصف الجمجمة ← تُسمع بالتساوي. رينّي: الشوكة على الخشائي ثم قرب القناة ← AC > BC."),
 TR("AC > BC or BC > AC?", "AC > BC أم BC > AC؟", "Normal is AC > BC; AC is twice as long as BC.", "الطبيعي AC > BC؛ والهوائي ضعف مدّة العظمي."),
 TR("Which part of the canal is very tender?", "أي جزء من القناة مؤلم جدًا؟", "The inner two third of the canal when touched with the speculum; pinna manipulation causes little or no discomfort.", "الثلثان الداخليان عند لمسهما بالمنظار؛ أما تحريك الصيوان فيسبّب انزعاجًا قليلًا أو معدومًا."),
 TR("Hearing test vs balance test", "اختبار السمع مقابل التوازن", "Voice, Weber and Rinne test hearing; Romberg tests equilibrium.", "الصوت وويبر ورينّي تفحص السمع؛ ورومبرغ يفحص التوازن."),
 TR("Tympanic membrane landmarks", "معالم الغشاء الطبلي", "Cone of light, umbo, handle of malleus and short process of malleus — not the tragus (part of the external ear).", "مخروط الضوء، والسُّرّة، ومقبض المطرقة وناتئها القصير — وليست الزنمة (جزء من الأذن الخارجية)."),
]
important = [
 IM("Describe the preparation for ear assessment.", "صف التحضير لتقييم الأذن.", "Position the adult sitting up straight with the head at your eye level; if the canal is obstructed with cerumen, soften it with a warmed solution of mineral oil hydrogen peroxide; irrigate with warm water; do not irrigate if history or examination suggests perforation or infection.", "يجلس البالغ مستقيمًا ورأسه بمستوى عينيك؛ وإذا سدّ الصملاخ القناة يُليَّن بمحلول دافئ من الزيت المعدني بيروكسيد الهيدروجين؛ وتُغسل بماء دافئ؛ ولا تُغسل عند الشك بثقب أو عدوى."),
 IM("Give the normal findings of the tympanic membrane.", "اذكر النتائج الطبيعية للغشاء الطبلي.", "Color: pearly gray, shiny & translucent. Consistency: intact, may show movement when swallowing. Landmarks: cone of light, umbo, handle of malleus and short process of malleus easily visualized.", "اللون: رمادي لؤلؤي لامع وشفّاف. القوام: سليم وقد يتحرّك عند البلع. المعالم: مخروط الضوء والسُّرّة ومقبض المطرقة وناتئها القصير تُرى بسهولة."),
 IM("How is the voice test performed?", "كيف يُجرى اختبار الصوت؟", "Test one ear at a time while masking the other; shield your lips; stand 30 to 60 cm (1-2 ft) from the ear; exhale and whisper slowly two-syllable words such as armchair, baseball; ask the client to repeat them. Normal: hears whispered words from 1-2 ft.", "تُفحص أذن واحدة مع حجب الأخرى؛ ويحجب الفاحص شفتيه؛ ويقف على بُعد 30 إلى 60 سم؛ ويزفر ويهمس ببطء كلمات من مقطعين مثل armchair وbaseball؛ ويكرّرها المريض. الطبيعي: يسمعها من 1-2 قدم."),
 IM("Compare the Weber and Rinne tests.", "قارن بين اختباري ويبر ورينّي.", "Weber (lateralization of sound): fork in the middle of the skull; normal = heard equally in both ears. Rinne (AC vs BC): fork on the mastoid until the sound goes away, then near the canal; normal = AC > BC (AC twice as long as BC).", "ويبر (تحديد جانب الصوت): الشوكة في منتصف الجمجمة؛ والطبيعي تُسمع بالتساوي. رينّي (الهوائي مقابل العظمي): على الخشائي حتى يختفي الصوت ثم قرب القناة؛ والطبيعي AC > BC (الهوائي ضعف العظمي)."),
 IM("Describe the Romberg test.", "صف اختبار رومبرغ.", "For equilibrium: the client stands with feet together, first with eyes open then with eyes closed; put your arms around the client to prevent falling. Normal: stands straight with minimal swaying.", "للتوازن: يقف المريض وقدماه متلاصقتان، أولًا بعينين مفتوحتين ثم مغلقتين؛ ويضع الفاحص ذراعيه حوله لمنع السقوط. الطبيعي: يقف مستقيمًا مع تمايل قليل."),
]
meta = HA(3, "Ear Assessment", "تقييم الأذن")
save("nursing-ha-lec3-ear", meta, chunk_lists(blocks, size=10, budget=13), mcq, tf, traps, important)

```
