---
source: BIOS-Obsidian/tools/scripts/bt/make2.py
handouts: [bloodbank-lec2-donation-criteria]
saved: 2026-10-31
tags: [bios, code]
---
# bt/make2.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#bloodbank-lec2-donation-criteria|bloodbank-lec2-donation-criteria]]

```python
import json, os
def C(en, ar, **k): return dict(t="card", en=en, ar=ar, **k)
def R(en, ar): return dict(t="rule", en=en, ar=ar)
def SEC(en, ar): return dict(t="section", en=en, ar=ar)
def H2(en, ar): return dict(t="h2", en=en, ar=ar)
def N(en, ar, label=None):
    d = dict(t="note", en=en, ar=ar)
    if label: d["label"] = label
    return d

blocks = [
 SEC("Criteria of blood donation", "معايير التبرع بالدم"),
 C("**Major goal of transfusion medicine** is to reduce the risk of transfusion-transmitted infection to as low a level as possible.",
   "**الهدف الرئيس لطب نقل الدم** هو تقليل خطر العدوى المنتقلة بنقل الدم إلى أدنى مستوى ممكن."),
 C("One method to achieve this is through the use of **appropriate donor selection procedures**.",
   "ومن طرق تحقيق ذلك استعمال **إجراءات مناسبة لاختيار المتبرعين**."),
 C("For infectious diseases for which routine blood donor screening assays are performed (human immunodeficiency virus [HIV], hepatitis B and C), the importance of donor screening procedures relates to their ability to identify potentially infectious donors during the infectious **seronegative window period**.",
   "بالنسبة إلى الأمراض المُعدية التي تُجرى لها فحوص تحرٍّ روتينية لدم المتبرعين (فيروس العوز المناعي البشري `HIV`، والتهاب الكبد B وC)، تكمن أهمية إجراءات تحرّي المتبرعين في قدرتها على كشف المتبرعين الذين قد يكونون مُعدين خلال **فترة النافذة** المُعدية السلبية مصليًا."),

 SEC("What is the Window period?", "ما فترة النافذة؟"),
 C(["The **window period** refers to the interval between the initial exposure to pathogen and the time when test can reliably detect the infection.",
    "( i.e when a person is infected with a pathogen and when the infection can be detected by diagnostic tests) .",
    "This period is also variable and can range from a **few days to several weeks**."],
   ["تشير **فترة النافذة** (`Window period`) إلى المدة بين التعرّض الأول للمُمرِض والوقت الذي يستطيع فيه الفحص كشف العدوى بصورة موثوقة.",
    "(أي بين إصابة الشخص بالمُمرِض وإمكان كشف العدوى بالفحوص التشخيصية).",
    "وهذه المدة متغيّرة أيضًا، وقد تتراوح من **بضعة أيام إلى عدة أسابيع**."]),
 N("during this period, a test may produce a **false negative** results , even though the infection is present.",
   "خلال هذه المدة قد يعطي الفحص نتيجة **سلبية كاذبة** مع أن العدوى موجودة."),

 SEC("Donor selection", "اختيار المتبرع"),
 C(["The physician must determine the suitability of donors.",
    "Donor selection is based on **Medical history** and a **physical examination** done on the day of donation to determine whether giving blood will harm the donor or if transfusion of the unit will harm the recipient."],
   ["يجب أن يحدّد الطبيب مدى ملاءمة المتبرعين.",
    "ويعتمد اختيار المتبرع على **التاريخ المرضي** و**الفحص البدني** في يوم التبرع، لتحديد ما إذا كان إعطاء الدم سيضرّ المتبرع، أو إن كان نقل الوحدة سيضرّ المستلم."]),
 C("Careful donor selection attributes to the safety of both donor and recipient.", "يسهم الاختيار الدقيق للمتبرع في سلامة المتبرع والمستلم كليهما."),
 C("The medical history information and physical examination are designed to answer two questions:", "صُمّمت معلومات التاريخ المرضي والفحص البدني للإجابة عن سؤالين:",
   list_en=["Will a donation of approximately **450 mL** of whole blood be harmful to the donor?", "Could blood drawn from this donor at this time potentially transmit a disease to the recipient?"],
   list_ar=["هل سيكون التبرع بنحو **450 مل** من الدم الكامل ضارًا بالمتبرع؟", "هل يمكن أن ينقل الدم المسحوب من هذا المتبرع في هذا الوقت مرضًا إلى المستلم؟"]),
 C("Before blood donation , the donor should be subjected to:", "قبل التبرع بالدم، يجب أن يخضع المتبرع لما يأتي:",
   list_en=["Detailed medical history (Questionnaire form).", "Limited physical examination"],
   list_ar=["تاريخ مرضي مفصّل (استمارة الاستبيان).", "فحص بدني محدود"]),
 H2("I. Medical history", "أولًا. التاريخ المرضي"),
 C("Before each donation questions should be asked to determine that the donor is in normal health and has not suffered from any serious illness e.g. malignant disease , epilepsy , bronchial asthma , diabetes , excessive menstrual bleeding , cardio - vascular conditions , renal disease , allergic diseases , abnormal bleeding tendency",
   "قبل كل تبرع يجب طرح أسئلة للتأكد من أن المتبرع بصحة طبيعية ولم يُصَب بأي مرض خطير، مثل: الأمراض الخبيثة، والصرع، والربو القصبي، والسكري، ونزف الحيض المفرط، وأمراض القلب والأوعية الدموية، وأمراض الكلى، وأمراض الحساسية، والميل غير الطبيعي للنزف"),
 H2("2. Physical Examination", "2. الفحص البدني"),
 C("**Physical Examination:** A medical officer should certify the donor fit for blood donation.", "**الفحص البدني:** يجب أن يشهد ضابط طبي بأن المتبرع لائق للتبرع بالدم."),

 SEC("Donor selection criteria", "معايير اختيار المتبرع"),
 dict(t="table", head=["Criterion", "Requirement", "المعيار"], ar_cols=[2], key_cols=[0], widths=["32mm", "", "62mm"],
      rows=[["Age", "17–70 years (maximum 65 at first donation)", "العمر: 17–70 سنة (65 حدًا أقصى عند أول تبرع)"],
            ["Weight", "> 50 kg", "الوزن: أكثر من 50 كغم"],
            ["Hb", ">13 g/dL for men, >12 g/dL for women", "الهيموغلوبين: أكثر من 13 غ/دل للرجال، وأكثر من 12 غ/دل للنساء"],
            ["Minimum donation interval", "of 12 weeks (16 weeks advised) and three donations per year maximum", "أقل فاصل بين التبرعات: 12 أسبوعًا (يُنصح بـ 16)، وثلاثة تبرعات في السنة حدًا أقصى"],
            ["Apheresis", "for platelets or plasma up to 24 times in 12 months", "فصادة الصفائح أو البلازما: حتى 24 مرة في 12 شهرًا"]]),
 C("**Pregnant** and **lactating** women excluded because of high iron requirements; donation deferred for **6 months post delivery** and only if the mother is not exclusively breastfeeding and is in good health.",
   "تُستبعد النساء **الحوامل** و**المرضعات** بسبب حاجتهن العالية إلى الحديد؛ ويؤجَّل التبرع **6 أشهر بعد الولادة**، وفقط إذا لم تكن الأم ترضع رضاعة طبيعية حصرية وكانت بصحة جيدة."),

 SEC("Exclusion criteria of Donor selection", "معايير استبعاد المتبرع"),
 R("**Medical illness:** prospective donors with diseases of the heart, liver, or lung or with a history of cancer or abnormal bleeding tendency shall be excluded unless determined to be suitable to donate by a qualified physician",
   "**الأمراض الطبية:** يُستبعد المتبرعون المحتملون المصابون بأمراض القلب أو الكبد أو الرئة، أو الذين لديهم تاريخ سرطان أو ميل غير طبيعي للنزف، ما لم يقرّر طبيب مؤهَّل أنهم مناسبون للتبرع"),
 R("Person with **HBV, HCV, and HIV** infection **Permanently deferred** from donation", "الشخص المصاب بعدوى **HBV وHCV وHIV** **يؤجَّل نهائيًا** عن التبرع"),
 R("History of **syphilis**: accepted **12 months** after completion of therapy.", "تاريخ الإصابة **بالزهري**: يُقبل بعد **12 شهرًا** من إكمال العلاج."),
 R("Confirmed **brucellosis** rejected for at least **two years** following full recovery", "**داء البروسيلات** المؤكَّد: يُرفض **سنتين** على الأقل بعد الشفاء التام"),
 R("**Tuberculosis**: may be accepted **two years** after having been cured.", "**السل**: قد يُقبل بعد **سنتين** من الشفاء."),
 R("**Malaria** - deferred, until the donor is a symptomatic and off treatment for **3 years**.", "**الملاريا**: يؤجَّل حتى يكون المتبرع بلا أعراض ومنقطعًا عن العلاج مدة **3 سنوات**."),
 R("Person **temporary** not suitable for donation", "الشخص غير المناسب للتبرع **مؤقتًا**"),
 dict(t="table", head=["Condition", "Deferral", "الحالة — مدة التأجيل"], ar_cols=[2], key_cols=[0], widths=["52mm", "34mm", ""],
      rows=[["Dental extraction", "→ after one week.", "قلع الأسنان ← بعد أسبوع واحد"],
            ["Diphtheria & typhoid", "after two weeks.", "الخنّاق والتيفوئيد ← بعد أسبوعين"],
            ["Viral disease or Bacterial infection", "after 3 weeks.", "مرض فيروسي أو عدوى بكتيرية ← بعد 3 أسابيع"],
            ["Resident from Africa", "→ 3 months.", "مقيم قادم من أفريقيا ← 3 أشهر"]]),
 R("Donors having history of **jaundice** should be deferred up to **1 year**.", "المتبرعون الذين لديهم تاريخ **يرقان** يؤجَّلون حتى **سنة واحدة**."),
 R("Donors having history of **measles / mumps / chicken pox** should be deferred for **8 weeks**.", "المتبرعون الذين لديهم تاريخ **حصبة / نكاف / جدري الماء** يؤجَّلون **8 أسابيع**."),
 R(["**Immunization** \\Person who have recently received toxoids and **killed** viral, bacterial, are acceptable, if they are symptom free and a febrile.",
    "These include vaccines against (e.g cholera, diphtheria, hepatitis, B, influenza)."],
   ["**التلقيح:** الأشخاص الذين تلقّوا حديثًا ذوفانات أو لقاحات فيروسية أو بكتيرية **مقتولة** يُقبلون إذا كانوا بلا أعراض وبلا حمّى.",
    "ومنها اللقاحات ضد (مثل الكوليرا، والخنّاق، والتهاب الكبد B، والإنفلونزا)."]),
 R("**Pregnancy:** Prospective donor should not be accepted during period of pregnancy ; donation deferred for **6 months post delivery** and only if the mother is not exclusively breastfeeding and is in good health.",
   "**الحمل:** لا يُقبل المتبرع المحتمل في أثناء الحمل؛ ويؤجَّل التبرع **6 أشهر بعد الولادة**، وفقط إذا لم تكن الأم ترضع رضاعة حصرية وكانت بصحة جيدة."),
 R(["Donors who have **abortions** should be deferred till **6 months** after 2nd and 3rd trimester abortion.", "Menstruation in itself should not be a cause for deferral."],
   ["المتبرعات اللواتي تعرّضن **للإجهاض** يؤجَّلن حتى **6 أشهر** بعد الإجهاض في الثلث الثاني والثالث من الحمل.", "أما الحيض بحد ذاته فلا يُعدّ سببًا للتأجيل."]),
 R("**Surgery:** Major operation , Donors should be accepted **one year** after the recovery from **major** operations and **six months** after recovery from **minor operations** including acupuncture, tattooing",
   "**الجراحة:** يُقبل المتبرعون بعد **سنة** من الشفاء من العمليات **الكبرى**، وبعد **ستة أشهر** من الشفاء من **العمليات الصغرى** ومنها الوخز بالإبر والوشم"),
 R("Donors having history of **receiving transfusion** of blood or blood products should be deferred for **12 months**.", "المتبرعون الذين لديهم تاريخ **تلقّي نقل** دم أو منتجاته يؤجَّلون **12 شهرًا**."),
 R("Ingestion of **Aspirin** or any related medicine within **three days** prior to donation should preclude use of donor as a source of **platelet** preparation.",
   "تناول **الأسبرين** أو أي دواء مشابه خلال **ثلاثة أيام** قبل التبرع يمنع استعمال المتبرع مصدرًا لتحضير **الصفائح الدموية**."),
 N("In the source, the numbering of these criteria goes from 14 directly to 16.", "في الملف الأصلي ينتقل ترقيم هذه المعايير من 14 إلى 16 مباشرة.", ["Note", "ملاحظة"]),

 SEC("Practical blood transfusion", "نقل الدم العملي"),
 C("Before blood donation; the donor should be subjected to:", "قبل التبرع بالدم، يجب أن يخضع المتبرع لما يأتي:",
   list_en=["Detailed medical history (Questionnaire form).", "Limited physical examination"], list_ar=["تاريخ مرضي مفصّل (استمارة الاستبيان).", "فحص بدني محدود"]),
 H2("Questionnaire form", "استمارة الاستبيان"),
 C("**Registration:**", "**التسجيل:**",
   list_en=["Name of the donor.", "Date and time of last donation not< 12 weeks", "Address", "Gender"],
   list_ar=["اسم المتبرع.", "تاريخ آخر تبرع ووقته (لا يقل عن 12 أسبوعًا)", "العنوان", "الجنس"]),
 H2("Donor interview", "مقابلة المتبرع"),
 C("Donors are asked questions concerning their sexual activities, their injection drug history, their prior HIV testing history, and their history of selected sexually transmitted diseases.",
   "يُسأل المتبرعون عن نشاطهم الجنسي، وتاريخ تعاطيهم المخدرات بالحقن، وتاريخ فحوص HIV السابقة، وتاريخ إصابتهم ببعض الأمراض المنقولة جنسيًا."),
 H2("Donor Screening", "تحرّي المتبرع"),
 C("", "", list_en=["All blood comes from **volunteer donors**.", "Screening performed to ensure donor is healthy.", "Starts with the donor and first impressions are critical",
                    "Clean facility from waiting room to collection area", "Professional staff who can ask the appropriate questions, observe and interpret the responses."],
   list_ar=["كل الدم يأتي من **متبرعين متطوّعين**.", "يُجرى التحرّي للتأكد من أن المتبرع سليم.", "يبدأ بالمتبرع، والانطباعات الأولى حاسمة",
            "منشأة نظيفة من غرفة الانتظار حتى منطقة الجمع", "كادر محترف يستطيع طرح الأسئلة المناسبة وملاحظة الإجابات وتفسيرها."]),
 H2("Donor Registration", "تسجيل المتبرع"),
 C("**Donor signs** in Written materials are given to the donor which explains high risk activities which may make the donor ineligible",
   "**يوقّع المتبرع** عند الدخول، وتُعطى له مواد مكتوبة تشرح الأنشطة عالية الخطورة التي قد تجعله غير مؤهَّل للتبرع",
   list_en=["The donor **must read** the information presented about testing for diseases", "A nurse takes the donor into a private room where more questions to check the donor.",
            "Donor must be informed and give details information how will be used his or her blood", "Repeat donors may be required to show ID card"],
   list_ar=["يجب أن **يقرأ** المتبرع المعلومات المقدَّمة عن فحص الأمراض", "تأخذ ممرضة المتبرع إلى غرفة خاصة لطرح مزيد من الأسئلة للتحقق منه.",
            "يجب إبلاغ المتبرع وإعطاؤه معلومات مفصّلة عن كيفية استعمال دمه", "قد يُطلب من المتبرعين المتكرّرين إبراز بطاقة الهوية"]),
 H2("Physical Examination", "الفحص البدني"),
 R("**General appearance** (and skin lesions): if the donor looks ill, appears to be under the influence of drugs or alcohol, it is best to defer the donation.",
   "**المظهر العام** (والآفات الجلدية): إذا بدا المتبرع مريضًا أو تحت تأثير المخدرات أو الكحول، فالأفضل تأجيل التبرع."),
 R("**Temp:** must not exceed **37.5 °C (99.5 F)** .", "**الحرارة:** يجب ألّا تتجاوز **37.5 °م (99.5 °ف)**."),
 R("**Pulse:** should exhibit no pathologic irregularity, and the frequency should be between **50 and 100 beats/ minute**.", "**النبض:** يجب ألّا يُظهر عدم انتظام مرضي، وأن يكون معدّله بين **50 و100 نبضة/دقيقة**."),
 R("**Blood pressure:** systolic and diastolic blood pressure “within normal ”", "**ضغط الدم:** الضغط الانقباضي والانبساطي «ضمن الحد الطبيعي»"),
 R("**Weight:** at least **50 Kg**.", "**الوزن:** 50 كغم على الأقل."),
 R("**Hb level:** > **13.0 g/dl** for males and > **12.0 g/dl** (PCV = 38%) for [[cut]]", "**مستوى الهيموغلوبين:** أكثر من **13.0 غ/دل** للذكور وأكثر من **12.0 غ/دل** (PCV = 38%) لـ [[قطع]]"),
]

def M(en, ar, o, a): return {"en": en, "ar": ar, "options": o, "answer": a}
mcq = [
 M("The major goal of transfusion medicine is to:", "الهدف الرئيس لطب نقل الدم هو:", [["Increase the number of transfusions", "زيادة عدد عمليات النقل"], ["Reduce the risk of transfusion-transmitted infection", "تقليل خطر العدوى المنتقلة بنقل الدم"], ["Collect blood from paid donors", "جمع الدم من متبرعين مأجورين"], ["Shorten donation time", "تقصير وقت التبرع"]], "b"),
 M("The window period is the interval between:", "فترة النافذة هي المدة بين:", [["Donation and transfusion", "التبرع والنقل"], ["Two donations", "تبرعين"], ["Initial exposure to a pathogen and reliable detection by a test", "التعرّض الأول للمُمرِض والكشف الموثوق بالفحص"], ["Collection and storage", "الجمع والخزن"]], "c"),
 M("During the window period a test may give:", "خلال فترة النافذة قد يعطي الفحص:", [["A false positive result", "نتيجة موجبة كاذبة"], ["A false negative result", "نتيجة سلبية كاذبة"], ["Always a correct result", "نتيجة صحيحة دائمًا"], ["No result", "لا نتيجة"]], "b"),
 M("The window period can range from:", "قد تتراوح فترة النافذة من:", [["A few days to several weeks", "بضعة أيام إلى عدة أسابيع"], ["Minutes to hours", "دقائق إلى ساعات"], ["5 to 10 years", "5 إلى 10 سنوات"], ["Exactly one month", "شهر واحد بالضبط"]], "a"),
 M("Donor selection is based on:", "يعتمد اختيار المتبرع على:", [["Blood group only", "فصيلة الدم فقط"], ["Age only", "العمر فقط"], ["The donor's wish only", "رغبة المتبرع فقط"], ["Medical history and physical examination on the day of donation", "التاريخ المرضي والفحص البدني في يوم التبرع"]], "d"),
 M("The approximate volume of a whole blood donation is:", "الحجم التقريبي لتبرع الدم الكامل هو:", [["250 mL", "250 مل"], ["450 mL", "450 مل"], ["1000 mL", "1000 مل"], ["100 mL", "100 مل"]], "b"),
 M("The accepted age range for blood donors is:", "مدى العمر المقبول للمتبرعين:", [["17–70 years (maximum 65 at first donation)", "17–70 سنة (65 حدًا أقصى عند أول تبرع)"], ["12–60 years", "12–60 سنة"], ["18–50 years", "18–50 سنة"], ["21–80 years", "21–80 سنة"]], "a"),
 M("The minimum weight for a blood donor is:", "الوزن الأدنى للمتبرع:", [["40 kg", "40 كغم"], ["45 kg", "45 كغم"], ["50 kg", "50 كغم"], ["70 kg", "70 كغم"]], "c"),
 M("The minimum Hb for female donors is:", "الحد الأدنى للهيموغلوبين للمتبرعات:", [["10 g/dL", "10 غ/دل"], ["11 g/dL", "11 غ/دل"], ["13 g/dL", "13 غ/دل"], ["12 g/dL", "12 غ/دل"]], "d"),
 M("The minimum interval between whole blood donations is:", "أقل فاصل بين تبرعات الدم الكامل:", [["4 weeks", "4 أسابيع"], ["12 weeks", "12 أسبوعًا"], ["1 year", "سنة"], ["2 weeks", "أسبوعان"]], "b"),
 M("The maximum number of whole blood donations per year is:", "الحد الأقصى لتبرعات الدم الكامل في السنة:", [["Three", "ثلاثة"], ["Six", "ستة"], ["Twelve", "اثنا عشر"], ["Twenty-four", "أربعة وعشرون"]], "a"),
 M("Apheresis for platelets or plasma is allowed up to:", "يُسمح بفصادة الصفائح أو البلازما حتى:", [["3 times in 12 months", "3 مرات في 12 شهرًا"], ["6 times in 12 months", "6 مرات في 12 شهرًا"], ["24 times in 12 months", "24 مرة في 12 شهرًا"], ["Once a year", "مرة في السنة"]], "c"),
 M("Persons with HBV, HCV or HIV infection are:", "الأشخاص المصابون بعدوى HBV أو HCV أو HIV:", [["Deferred 1 year", "يؤجَّلون سنة"], ["Deferred 6 months", "يؤجَّلون 6 أشهر"], ["Accepted after treatment", "يُقبلون بعد العلاج"], ["Permanently deferred", "يؤجَّلون نهائيًا"]], "d"),
 M("A donor with a history of syphilis is accepted:", "يُقبل المتبرع الذي لديه تاريخ زهري:", [["12 months after completion of therapy", "بعد 12 شهرًا من إكمال العلاج"], ["Immediately", "فورًا"], ["After 2 years", "بعد سنتين"], ["Never", "أبدًا"]], "a"),
 M("Confirmed brucellosis: the donor is rejected for at least:", "داء البروسيلات المؤكَّد: يُرفض المتبرع مدة لا تقل عن:", [["One week", "أسبوع"], ["Two years after full recovery", "سنتين بعد الشفاء التام"], ["Three months", "ثلاثة أشهر"], ["Six months", "ستة أشهر"]], "b"),
 M("Malaria: the donor is deferred until symptom-free and off treatment for:", "الملاريا: يؤجَّل المتبرع حتى يكون بلا أعراض ومنقطعًا عن العلاج مدة:", [["3 weeks", "3 أسابيع"], ["6 months", "6 أشهر"], ["3 years", "3 سنوات"], ["1 year", "سنة"]], "c"),
 M("After dental extraction, a donor can donate after:", "بعد قلع الأسنان، يستطيع المتبرع التبرع بعد:", [["One week", "أسبوع"], ["Two weeks", "أسبوعين"], ["Three weeks", "ثلاثة أسابيع"], ["Three months", "ثلاثة أشهر"]], "a"),
 M("A resident from Africa is deferred for:", "المقيم القادم من أفريقيا يؤجَّل:", [["1 week", "أسبوعًا"], ["2 weeks", "أسبوعين"], ["1 year", "سنة"], ["3 months", "3 أشهر"]], "d"),
 M("A history of jaundice defers the donor up to:", "تاريخ اليرقان يؤجّل المتبرع حتى:", [["8 weeks", "8 أسابيع"], ["1 year", "سنة"], ["3 years", "3 سنوات"], ["Permanently", "نهائيًا"]], "b"),
 M("Measles, mumps or chicken pox: the donor is deferred for:", "الحصبة أو النكاف أو جدري الماء: يؤجَّل المتبرع:", [["1 week", "أسبوعًا"], ["1 year", "سنة"], ["8 weeks", "8 أسابيع"], ["6 months", "6 أشهر"]], "c"),
 M("After a major operation, donors are accepted:", "بعد عملية كبرى، يُقبل المتبرعون:", [["One year after recovery", "بعد سنة من الشفاء"], ["Six months after recovery", "بعد ستة أشهر من الشفاء"], ["One month after recovery", "بعد شهر من الشفاء"], ["Immediately", "فورًا"]], "a"),
 M("Tattooing and acupuncture are treated like minor operations, so the deferral is:", "يُعامل الوشم والوخز بالإبر معاملة العمليات الصغرى، لذا يكون التأجيل:", [["One week", "أسبوعًا"], ["One year", "سنة"], ["Six months", "ستة أشهر"], ["Permanent", "نهائيًا"]], "c"),
 M("A donor who received a blood transfusion is deferred for:", "المتبرع الذي تلقّى نقل دم يؤجَّل:", [["3 days", "3 أيام"], ["12 months", "12 شهرًا"], ["8 weeks", "8 أسابيع"], ["3 years", "3 سنوات"]], "b"),
 M("Aspirin within three days before donation prevents using the donor as a source of:", "تناول الأسبرين خلال ثلاثة أيام قبل التبرع يمنع استعمال المتبرع مصدرًا لـ:", [["Plasma", "البلازما"], ["Red cells", "الكريات الحمر"], ["Whole blood", "الدم الكامل"], ["Platelets", "الصفائح الدموية"]], "d"),
 M("The donor's temperature must not exceed:", "يجب ألّا تتجاوز حرارة المتبرع:", [["37.5 °C", "37.5 °م"], ["38.5 °C", "38.5 °م"], ["36.0 °C", "36.0 °م"], ["39 °C", "39 °م"]], "a"),
 M("The donor's pulse should be between:", "يجب أن يكون نبض المتبرع بين:", [["40 and 60 beats/min", "40 و60 نبضة/دقيقة"], ["50 and 100 beats/min", "50 و100 نبضة/دقيقة"], ["100 and 120 beats/min", "100 و120 نبضة/دقيقة"], ["30 and 50 beats/min", "30 و50 نبضة/دقيقة"]], "b"),
]
tf = [
 {"en": "Appropriate donor selection procedures reduce transfusion-transmitted infection.", "ar": "إجراءات اختيار المتبرع المناسبة تقلّل العدوى المنتقلة بالدم.", "answer": "T"},
 {"en": "During the window period, tests always detect the infection.", "ar": "خلال فترة النافذة تكشف الفحوص العدوى دائمًا.", "answer": "F"},
 {"en": "Donor selection is done on the day of donation.", "ar": "يُجرى اختيار المتبرع في يوم التبرع.", "answer": "T"},
 {"en": "Lactating women are excluded because of high iron requirements.", "ar": "تُستبعد المرضعات بسبب حاجتهن العالية إلى الحديد.", "answer": "T"},
 {"en": "Tuberculosis patients may be accepted two years after cure.", "ar": "قد يُقبل مرضى السل بعد سنتين من الشفاء.", "answer": "T"},
 {"en": "Diphtheria and typhoid require a deferral of three months.", "ar": "يتطلب الخنّاق والتيفوئيد تأجيلًا ثلاثة أشهر.", "answer": "F"},
 {"en": "Persons who received killed vaccines are acceptable if symptom-free and afebrile.", "ar": "يُقبل الأشخاص الذين تلقّوا لقاحات مقتولة إذا كانوا بلا أعراض وبلا حمّى.", "answer": "T"},
 {"en": "Menstruation is a cause for deferral.", "ar": "الحيض سبب للتأجيل.", "answer": "F"},
 {"en": "After a 2nd or 3rd trimester abortion, donation is deferred 6 months.", "ar": "بعد الإجهاض في الثلث الثاني أو الثالث يؤجَّل التبرع 6 أشهر.", "answer": "T"},
 {"en": "Repeat donors may be required to show an ID card.", "ar": "قد يُطلب من المتبرعين المتكرّرين إبراز بطاقة الهوية.", "answer": "T"},
 {"en": "A donor who appears to be under the influence of alcohol should be accepted.", "ar": "يجب قبول المتبرع الذي يبدو تحت تأثير الكحول.", "answer": "F"},
 {"en": "The minimum weight of a donor is 40 kg.", "ar": "الوزن الأدنى للمتبرع 40 كغم.", "answer": "F"},
]
traps = [
 {"en": "Syphilis and brucellosis have the same deferral period. Correct?", "ar": "للزهري وداء البروسيلات مدة التأجيل نفسها. هل هذا صحيح؟", "answer_en": "No. Syphilis → accepted **12 months** after therapy; brucellosis → rejected at least **two years** after recovery.", "answer_ar": "لا. الزهري ← يُقبل بعد **12 شهرًا** من العلاج؛ البروسيلات ← يُرفض **سنتين** على الأقل بعد الشفاء."},
 {"en": "Malaria and tuberculosis are both deferred for two years. Correct?", "ar": "تؤجَّل الملاريا والسل كلاهما سنتين. هل هذا صحيح؟", "answer_en": "No. Tuberculosis → **two years** after cure; malaria → **3 years** symptom-free and off treatment.", "answer_ar": "لا. السل ← **سنتان** بعد الشفاء؛ الملاريا ← **3 سنوات** بلا أعراض ومن دون علاج."},
 {"en": "Jaundice and measles share the same deferral. Correct?", "ar": "لليرقان والحصبة التأجيل نفسه. هل هذا صحيح؟", "answer_en": "No. Jaundice → up to **1 year**; measles / mumps / chicken pox → **8 weeks**.", "answer_ar": "لا. اليرقان ← حتى **سنة**؛ الحصبة/النكاف/جدري الماء ← **8 أسابيع**."},
 {"en": "Major and minor operations both defer the donor for one year. Correct?", "ar": "العمليات الكبرى والصغرى كلتاهما تؤجّل المتبرع سنة. هل هذا صحيح؟", "answer_en": "No. Major → **one year**; minor (including acupuncture, tattooing) → **six months**.", "answer_ar": "لا. الكبرى ← **سنة**؛ الصغرى (ومنها الوخز بالإبر والوشم) ← **ستة أشهر**."},
 {"en": "Aspirin excludes the donor from all blood donation. Correct?", "ar": "الأسبرين يمنع المتبرع من كل أنواع التبرع. هل هذا صحيح؟", "answer_en": "No. It only precludes use of the donor as a source of **platelet** preparation (within three days).", "answer_ar": "لا. يمنع فقط استعمال المتبرع مصدرًا لتحضير **الصفائح** (خلال ثلاثة أيام)."},
 {"en": "The Hb limit is the same for men and women. Correct?", "ar": "حد الهيموغلوبين واحد للرجال والنساء. هل هذا صحيح؟", "answer_en": "No. Men > **13 g/dL**; women > **12 g/dL**.", "answer_ar": "لا. الرجال أكثر من **13 غ/دل**؛ النساء أكثر من **12 غ/دل**."},
]
important = [
 {"en": "Define the window period and explain its importance.", "ar": "عرّف فترة النافذة واشرح أهميتها.", "answer_en": "The interval between initial exposure to a pathogen and the time a test can reliably detect the infection (few days to several weeks). A test may give a false negative result though the infection is present, so donor screening must identify potentially infectious donors in this period.", "answer_ar": "المدة بين التعرّض الأول للمُمرِض ووقت إمكان كشف العدوى بالفحص بصورة موثوقة (من أيام إلى أسابيع). قد يعطي الفحص نتيجة سلبية كاذبة مع وجود العدوى، لذا يجب أن يكشف تحرّي المتبرعين المُعدين المحتملين في هذه المدة."},
 {"en": "What two questions do the medical history and physical examination answer?", "ar": "ما السؤالان اللذان يجيب عنهما التاريخ المرضي والفحص البدني؟", "answer_en": "(1) Will a donation of approximately 450 mL of whole blood be harmful to the donor? (2) Could blood drawn from this donor at this time potentially transmit a disease to the recipient?", "answer_ar": "(1) هل سيضرّ التبرع بنحو 450 مل من الدم الكامل بالمتبرع؟ (2) هل يمكن أن ينقل الدم المسحوب من هذا المتبرع الآن مرضًا إلى المستلم؟"},
 {"en": "List the donor selection criteria (age, weight, Hb, interval).", "ar": "عدّد معايير اختيار المتبرع (العمر، الوزن، الهيموغلوبين، الفاصل).", "answer_en": "Age 17–70 (max 65 at first donation); weight > 50 kg; Hb > 13 g/dL men, > 12 g/dL women; interval 12 weeks (16 advised), max three donations per year; apheresis up to 24 times in 12 months.", "answer_ar": "العمر 17–70 (65 حدًا أقصى أول مرة)؛ الوزن أكثر من 50 كغم؛ الهيموغلوبين أكثر من 13 للرجال و12 للنساء؛ الفاصل 12 أسبوعًا (يُنصح بـ 16)، وثلاثة تبرعات سنويًا حدًا أقصى؛ الفصادة حتى 24 مرة في 12 شهرًا."},
 {"en": "List the temporary deferrals and their periods.", "ar": "عدّد حالات التأجيل المؤقت ومددها.", "answer_en": "Dental extraction 1 week; diphtheria & typhoid 2 weeks; viral or bacterial infection 3 weeks; resident from Africa 3 months; measles/mumps/chicken pox 8 weeks; jaundice up to 1 year; transfusion 12 months; minor surgery 6 months; major surgery 1 year.", "answer_ar": "قلع الأسنان أسبوع؛ الخنّاق والتيفوئيد أسبوعان؛ العدوى الفيروسية أو البكتيرية 3 أسابيع؛ المقيم من أفريقيا 3 أشهر؛ الحصبة/النكاف/جدري الماء 8 أسابيع؛ اليرقان حتى سنة؛ نقل الدم 12 شهرًا؛ الجراحة الصغرى 6 أشهر؛ الكبرى سنة."},
 {"en": "What does the physical examination of the donor include?", "ar": "ماذا يشمل الفحص البدني للمتبرع؟", "answer_en": "General appearance and skin lesions; temperature ≤ 37.5 °C; pulse 50–100 beats/min with no pathologic irregularity; blood pressure within normal; weight ≥ 50 kg; Hb > 13.0 g/dl males and > 12.0 g/dl females.", "answer_ar": "المظهر العام والآفات الجلدية؛ الحرارة لا تتجاوز 37.5 °م؛ النبض 50–100 نبضة/دقيقة بلا عدم انتظام مرضي؛ ضغط الدم طبيعي؛ الوزن 50 كغم على الأقل؛ الهيموغلوبين أكثر من 13.0 للذكور و12.0 للإناث."},
]

data = {"meta": {
  "subject_en": "Blood Transfusion", "subject_ar": "نقل الدم", "short_ar": "نقل الدم",
  "unit_en": "Lecture 2", "unit_ar": "المحاضرة 2", "unit_label": "LEC", "unit_no": "2",
  "title_en": "Criteria of blood donation", "title_ar": "معايير التبرع بالدم",
  "kind": "Theory & Practical — نظري وعملي", "stage": "The fourth stage — الرابعة", "instructor": "د. مازن اللهيبي"},
 "blocks": blocks, "questions": {"mcq": mcq, "tf": tf, "traps": traps, "important": important}}
from collections import Counter
print(len(mcq), Counter(q["answer"] for q in mcq))
os.makedirs("/home/user/-/bloodbank-lec2-donation-criteria", exist_ok=True)
json.dump(data, open("/home/user/-/bloodbank-lec2-donation-criteria/lecture.json", "w"), ensure_ascii=False, indent=1)

```
