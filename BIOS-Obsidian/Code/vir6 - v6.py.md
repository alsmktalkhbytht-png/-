---
source: BIOS-Obsidian/tools/scripts/vir6/v6.py
handouts: [virology-lab6-neutralization]
saved: 2026-11-08
tags: [bios, code]
---
# vir6/v6.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#virology-lab6-neutralization|virology-lab6-neutralization]]

```python
import sys; sys.path.insert(0, "/tmp/claude-0/-home-user--/67d83c9a-7b0e-5ae5-b52b-cd659ab074ab/scratchpad/imm456")
from ci import *            # c helpers + B INSHORT TERMS balance save(split.fix)
sys.path.insert(0, "/tmp/claude-0/-home-user--/67d83c9a-7b0e-5ae5-b52b-cd659ab074ab/scratchpad"); from bidi import ltr_all; from flowfit import fit

# Medical Virology practical, lab 6 — Virology_Lab_6_1.pdf (6 pages, 1 figure, 10 MCQ + 10 TF); د. آية وسمي, third stage
BN = lambda en, ar: N(en, ar, label=["BIOS note", "ملاحظة BIOS"])
O = P

blocks = [
 # ───────────────────────── 1
 SEC("Virus Neutralization Test (VNT)", "اختبار تعادل الفيروس (VNT)"),
 C(["**Neutralization of viruses by antibodies** is a phenomenon of fundamental medical and biological importance.",
    "Importance in virology (e.g., measuring **protective immunity**, **vaccine efficacy**, and **virus identification**)"],
   ["**تعادل (تحييد) الفيروسات بالأضداد** ظاهرة ذات أهمية طبية وحيوية أساسية.",
    "أهميتها في علم الفيروسات (مثل قياس **المناعة الواقية**، و**كفاءة اللقاح**، و**تشخيص (تحديد هوية) الفيروس**)"]),
 L(["Antibodies can **neutralize (decrease the replication of)** viruses by **blocking attachment to the host cell**, **preventing penetration** of the host cell membrane, or prevent with **uncoating** of the virus within the cell.",
    "Neutralizing antibodies typically recognize **proteins or glycoproteins on the virion surface**.",
    ["Some antibodies that bind to virion surface proteins or glycoproteins are **not neutralizing**.", "In some cases, such antibodies may **contribute to immunity**, whereas in others, they may **enhance infection**."],
    "The magnitude of neutralization mediated by a given antibody **may vary with the host cell** used for the measurement.",
    "**Neutralization in vitro** is usually related to **protection in vivo**, but these two properties are **not always perfectly correlated**."],
   ["تستطيع الأضداد **تعادل الفيروسات (أي تقليل تضاعفها)** عن طريق **منع الالتصاق بالخلية المضيفة**، أو **منع اختراق** غشاء الخلية المضيفة، أو منع **إزالة غلاف** الفيروس داخل الخلية.",
    "تتعرّف الأضداد المعادِلة عادةً على **البروتينات أو البروتينات السكرية على سطح الفيريون**.",
    ["بعض الأضداد التي ترتبط ببروتينات سطح الفيريون أو بروتيناته السكرية **ليست معادِلة**.", "وفي بعض الحالات قد **تُسهم هذه الأضداد في المناعة**، بينما في حالات أخرى قد **تُعزّز العدوى**."],
    "مقدار التعادل الذي يحقّقه ضدّ معيّن **قد يختلف باختلاف الخلية المضيفة** المستعملة في القياس.",
    "**التعادل في المختبر (`in vitro`)** يرتبط عادةً **بالحماية في الجسم الحي (`in vivo`)**، لكن هاتين الخاصيتين **لا تترابطان دائمًا ترابطًا تامًّا**."]),
 FLOW([("Blocks attachment", "منع الالتصاق"), ("Prevents penetration", "منع الاختراق"), ("Prevents uncoating", "منع إزالة الغلاف")],
      en="Three ways antibodies neutralize a virus", ar="ثلاث طرق تعادل بها الأضداد الفيروس"),
 BN("\"or prevent with uncoating\" means \"or **interfering with** uncoating\" — the antibody stops the virus from releasing its genome inside the cell.",
    "عبارة \"or prevent with uncoating\" تعني \"أو **التداخل مع** إزالة الغلاف\" — أي أن الضدّ يمنع الفيروس من تحرير مادّته الوراثية داخل الخلية."),
 INSHORT([("Neutralization = antibodies **decrease virus replication**.", "التعادل = الأضداد **تقلّل تضاعف الفيروس**."),
          ("Used to measure **protective immunity, vaccine efficacy** and to **identify viruses**.", "يُستعمل لقياس **المناعة الواقية وكفاءة اللقاح** ولـ**تحديد هوية الفيروسات**."),
          ("Targets: **surface proteins / glycoproteins** of the virion; not every binding antibody neutralizes.", "الهدف: **بروتينات / بروتينات سكرية سطحية** للفيريون؛ وليس كل ضدّ يرتبط يكون معادِلًا."),
          ("In vitro ≈ in vivo, but **not always perfectly**.", "التعادل في المختبر ≈ الحماية في الجسم، لكن **ليس دائمًا تمامًا**.")]),

 # ───────────────────────── 2
 SEC("Methodology principles", "مبادئ الطريقة"),
 C(["The VNT involves mixing **serial dilutions of the serum sample** with **a known amount of virus**.",
    "The mixture is then incubated with **susceptible cells**.",
    "If **neutralizing antibodies** are present, they will bind to the virus and **prevent it from infecting the cells**.",
    "The **highest dilution** of serum that **completely inhibits viral infection** is considered the **neutralization titer**."],
   ["يتضمّن `VNT` مزج **تخافيف متسلسلة من عيّنة المصل** مع **كمية معروفة من الفيروس**.",
    "ثم يُحضن المزيج مع **خلايا قابلة للإصابة (حسّاسة للفيروس)**.",
    "فإذا وُجدت **أضداد معادِلة** فإنها ترتبط بالفيروس و**تمنعه من إصابة الخلايا**.",
    "و**أعلى تخفيف** للمصل **يثبّط الإصابة الفيروسية تثبيطًا كاملًا** يُعدّ **عيار التعادل**."]),
 FLOW([("Serum serial dilutions", "تخافيف متسلسلة للمصل"), ("+ known amount of virus", "+ كمية معروفة من الفيروس"), ("+ susceptible cells", "+ خلايا حسّاسة"), ("Highest protecting dilution = titer", "أعلى تخفيف يحمي = العيار")],
      en="VNT in one line", ar="الاختبار بسطر واحد"),
 INSHORT([("Serum (diluted) + **virus** → + **cells** → look for infection.", "مصل (مخفّف) + **فيروس** ← + **خلايا** ← نبحث عن الإصابة."),
          ("**Titer** = the **highest** dilution that **completely** inhibits infection.", "**العيار** = **أعلى** تخفيف يثبّط الإصابة **تثبيطًا كاملًا**.")]),

 # ───────────────────────── 3
 SEC("Methods", "خطوات العمل"),
 R(["**Sample Preparation:** The sample, usually **blood serum**, is diluted to create **a series of dilutions**.", "This is done to determine the **highest dilution** at which antibodies can still neutralize the virus"],
   ["**تحضير العيّنة:** تُخفَّف العيّنة، وهي عادةً **مصل الدم**، لعمل **سلسلة من التخافيف**.", "ويُجرى ذلك لتحديد **أعلى تخفيف** تبقى فيه الأضداد قادرة على تعادل الفيروس"]),
 R(["**Virus Incubation:** A **known quantity of the virus** is mixed with **each dilution** of the sample.", "This mixture is incubated, allowing any neutralizing antibodies in the sample to **bind to the virus**."],
   ["**حضن الفيروس:** تُمزج **كمية معروفة من الفيروس** مع **كل تخفيف** من العيّنة.", "ويُحضن هذا المزيج للسماح لأي أضداد معادِلة في العيّنة بـ**الارتباط بالفيروس**."]),
 R(["**Cell Culture:** **Cells susceptible to the virus** are added to the virus-antibody mixture.", "If neutralizing antibodies are present, they will **prevent the virus from infecting the cells**."],
   ["**مزرعة الخلايا:** تُضاف **خلايا قابلة للإصابة بالفيروس** إلى مزيج الفيروس والضدّ.", "فإذا وُجدت أضداد معادِلة فإنها **تمنع الفيروس من إصابة الخلايا**."]),
 R(["**Observation:** The cell culture is monitored for **signs of viral infection**.", "If the cells **remain healthy**, it indicates that the antibodies in the sample **neutralized the virus** at that dilution."],
   ["**المراقبة:** تُراقَب مزرعة الخلايا بحثًا عن **علامات الإصابة الفيروسية**.", "فإذا **بقيت الخلايا سليمة** دلّ ذلك على أن الأضداد في العيّنة **عادلت الفيروس** عند ذلك التخفيف."]),
 R(["**Titer Determination:** The **highest dilution** of the sample that still **prevents viral infection** is the **antibody titer**.", "This titer indicates the **level of neutralizing antibodies** present in the sample."],
   ["**تحديد العيار:** **أعلى تخفيف** للعيّنة لا يزال **يمنع الإصابة الفيروسية** هو **عيار الأضداد**.", "ويدلّ هذا العيار على **مستوى الأضداد المعادِلة** الموجودة في العيّنة."]),
 T([B("Step", "الخطوة"), B("What is done", "ماذا يُعمل"), B("Why", "لماذا")],
   [[B("**1. Sample preparation**", "**1. تحضير العيّنة**"), B("serial dilutions of serum", "تخافيف متسلسلة للمصل"), B("find the highest neutralizing dilution", "إيجاد أعلى تخفيف معادِل")],
    [B("**2. Virus incubation**", "**2. حضن الفيروس**"), B("known quantity of virus + each dilution", "كمية معروفة من الفيروس + كل تخفيف"), B("antibodies bind the virus", "ترتبط الأضداد بالفيروس")],
    [B("**3. Cell culture**", "**3. مزرعة الخلايا**"), B("add susceptible cells", "إضافة خلايا حسّاسة"), B("unneutralized virus infects them", "الفيروس غير المعادَل يصيبها")],
    [B("**4. Observation**", "**4. المراقبة**"), B("look for signs of infection", "البحث عن علامات الإصابة"), B("healthy cells = neutralized", "خلايا سليمة = تعادل")],
    [B("**5. Titer**", "**5. العيار**"), B("highest dilution still protecting", "أعلى تخفيف لا يزال يحمي"), B("= level of neutralizing antibodies", "= مستوى الأضداد المعادِلة")]],
   key_cols=[0], widths=[28, 38, 34], style="summary", label_en="5 steps at a glance", label_ar="الخطوات الخمس بنظرة"),
 INSHORT([("Order: **dilute → add virus → add cells → observe → titer**.", "الترتيب: **تخفيف ← إضافة فيروس ← إضافة خلايا ← مراقبة ← عيار**."),
          ("**Healthy cells** = virus neutralized at that dilution.", "**خلايا سليمة** = الفيروس تعادل عند ذلك التخفيف.")]),

 # ───────────────────────── 4
 SEC("Applications", "الاستعمالات"),
 L(["**Vaccine development:** To assess the **efficacy of vaccines** by measuring the levels of neutralizing antibodies induced by vaccination.",
    "**Diagnosis of viral infections:** To detect the presence of neutralizing antibodies in patients suspected of having a viral infection.",
    "**Epidemiological studies:** To determine the **prevalence** of neutralizing antibodies in a population."],
   ["**تطوير اللقاحات:** لتقييم **كفاءة اللقاحات** بقياس مستويات الأضداد المعادِلة التي يحفّزها التلقيح.",
    "**تشخيص الإصابات الفيروسية:** للكشف عن وجود أضداد معادِلة لدى المرضى المشتبه بإصابتهم بعدوى فيروسية.",
    "**الدراسات الوبائية:** لتحديد **مدى انتشار** الأضداد المعادِلة في مجتمع ما."],
   en="The VNT is used in a variety of applications, including:", ar="يُستعمل `VNT` في تطبيقات متنوّعة، منها:"),
 F("vnt.jpg", "Virus Neutralization Test. (dr. A (Astrid) de Greeff. Virus neutralization tests against SARS-CoV-2 variants)",
   "اختبار تعادل الفيروس (المصدر: د. أ. (أسترِد) دي غريف — اختبارات تعادل الفيروس ضدّ متحوّرات `SARS-CoV-2`)", width="100%"),
 T([B("Figure text", "كتابات الشكل"), B("Meaning", "المعنى")],
   [[B("**1. Dilute (neutralizing) antibodies** — serial dilutions →", "**1. خفّف الأضداد (المعادِلة)** — تخافيف متسلسلة ←"), B("samples 1–6, pos. contr., neg. contr. in a 96-well plate", "العيّنات 1–6 والسيطرة الموجبة والسالبة في صفيحة 96 حفرة")],
    [B("**2. Add SARS-CoV-2 variant (and incubate 1-2 hr)**", "**2. أضف متحوّر `SARS-CoV-2` (واحضن 1–2 ساعة)**"), B("virus + antibody", "فيروس + ضدّ")],
    [B("**3. Add cells (and incubate 3-7d)**", "**3. أضف الخلايا (واحضن 3–7 أيام)**"), B("susceptible cells", "خلايا حسّاسة")],
    [B("**4. Detection of virus infected cells** — wash, Detect", "**4. كشف الخلايا المصابة بالفيروس** — غسل، ثم كشف"), B("read the VNT titer of each sample (e.g. 4, 6, 4, 6, 8, 5; pos. contr. 8; neg. contr. 0)", "قراءة عيار كل عيّنة (مثل 4، 6، 4، 6، 8، 5؛ السيطرة الموجبة 8؛ السالبة 0)")],
    [B("**Neutralizing antibodies** — e.g. positive control", "**أضداد معادِلة** — مثل السيطرة الموجبة"), B("**uninfected cells**", "**خلايا غير مصابة**")],
    [B("**Non-neutralizing antibodies** — e.g. negative control", "**أضداد غير معادِلة** — مثل السيطرة السالبة"), B("**virus infected cells**", "**خلايا مصابة بالفيروس**")]],
   key_cols=[0], widths=[52, 48], label_en="Figure text", label_ar="كتابات الشكل"),
 N("https://www.wur.nl/en/research-results/research-institutes/bioveterinary-research/cro/cro-services/virus-neutralization-tests.htm",
   "رابط مصدر الشكل كما ورد في ورقة العملي.", label=["Figure source", "مصدر الشكل"]),
 INSHORT([("Uses: **vaccine efficacy, diagnosis, epidemiology (prevalence)**.", "الاستعمالات: **كفاءة اللقاح، والتشخيص، والوبائيات (الانتشار)**."),
          ("Figure: neutralizing Ab → **uninfected** cells; non-neutralizing Ab → **infected** cells.", "الشكل: ضدّ معادِل ← خلايا **غير مصابة**؛ ضدّ غير معادِل ← خلايا **مصابة**.")]),

 # ───────────────────────── 5
 SEC("Interpretation and limitations", "تفسير النتائج والقيود"),
 H2("Interpretation of Results", "تفسير النتائج"),
 C(["The results of the VNT are typically expressed as a **titer**, which is the **highest dilution of serum that completely inhibits viral infection**.",
    "A **higher titer** indicates a **higher level of neutralizing antibodies**."],
   ["تُعبَّر نتائج `VNT` عادةً بصورة **عيار**، وهو **أعلى تخفيف للمصل يثبّط الإصابة الفيروسية تثبيطًا كاملًا**.",
    "و**العيار الأعلى** يدلّ على **مستوى أعلى من الأضداد المعادِلة**."]),
 H2("Limitations", "القيود (السلبيات)"),
 C(["The VNT is a **complex and time-consuming** assay.", "It requires **specialized equipment and expertise**.", "It can also be **difficult to standardize** the assay across different laboratories."],
   ["`VNT` اختبار **معقّد ويستغرق وقتًا طويلًا**.", "ويحتاج **أجهزة متخصّصة وخبرة**.", "ومن **الصعب أيضًا توحيده (تقييسه)** بين المختبرات المختلفة."]),
 BN("Example: a serum that still protects the cells at **1:320** but not at 1:640 has a titer of **320** — higher than a serum with titer 40, so it has **more** neutralizing antibodies.",
    "مثال: مصل يحمي الخلايا عند **1:320** ولا يحميها عند 1:640 عياره **320** — وهو أعلى من مصل عياره 40، أي فيه أضداد معادِلة **أكثر**."),
 INSHORT([("Result = **titer**; higher titer = **more** neutralizing antibodies.", "النتيجة = **عيار**؛ والعيار الأعلى = أضداد معادِلة **أكثر**."),
          ("Limits: **complex, slow, needs equipment and expertise, hard to standardize**.", "القيود: **معقّد، وبطيء، ويحتاج أجهزة وخبرة، وصعب التوحيد**.")]),
] + TERMS([
 ("Virus Neutralization Test (VNT)", "اختبار تعادل الفيروس / اختبار التحييد الفيروسي"),
 ("Neutralization", "التعادل / التحييد / الإبطال"),
 ("Neutralizing antibodies", "الأضداد المعادِلة / الأجسام المضادة المحيِّدة"),
 ("Virion", "الفيريون / الجسيم الفيروسي الكامل"),
 ("Glycoprotein", "بروتين سكري / غليكوبروتين"),
 ("Attachment / penetration / uncoating", "الالتصاق / الاختراق / إزالة الغلاف (التعرية)"),
 ("Serial dilutions", "تخافيف متسلسلة / تخفيف تسلسلي"),
 ("Titer", "العيار / المعيار"),
 ("Susceptible cells", "خلايا قابلة للإصابة / حسّاسة"),
 ("In vitro / in vivo", "في المختبر (خارج الجسم) / في الجسم الحي"),
 ("Vaccine efficacy", "كفاءة اللقاح / فعالية اللقاح"),
 ("Prevalence", "الانتشار / معدّل الانتشار"),
 ("Epidemiological studies", "الدراسات الوبائية"),
 ("Positive / negative control", "السيطرة (الشاهد) الموجبة / السالبة"),
])

# ───────────────────────── questions
KEY = "1-B, 2-B, 3-A, 4-B, 5-A, 6-B, 7-B, 8-B, 9-B, 10-C"
def kn(q, line, bold, why_en, why_ar):
    q["note_en"] = f"The sheet's \"Answer key\" line ({KEY}) gives **{line}** here, but the answer printed in **bold** in the sheet is **{bold}**, which matches the lab text ({why_en}). We use {bold}."
    q["note_ar"] = f"سطر \"Answer key\" في الورقة (`{KEY}`) يعطي **{line}** هنا، لكن الجواب المكتوب **بالخط الغامق** في الورقة **{bold}**، وهو المطابق لنص العملي ({why_ar}). اعتمدنا {bold}."
    return q

lab = [
 {"topic_en": "MCQs Lab Six (from the lab sheet)", "topic_ar": "أسئلة العملي السادس (من ورقة العملي)"},
 Q("The Virus Neutralization Test (VNT) is primarily used to detect:", "يُستعمل اختبار تعادل الفيروس (VNT) أساسًا للكشف عن:",
   O(("Viral DNA directly", "الدنا الفيروسي مباشرة"), ("Neutralizing antibodies", "الأضداد المعادِلة"), ("Bacterial toxins", "السموم البكتيرية"), ("Red blood cell antigens", "مستضدّات كريات الدم الحمر"), ("Fungal spores", "الأبواغ الفطرية")), "b"),
 kn(Q("Neutralizing antibodies can decrease viral replication by:", "تستطيع الأضداد المعادِلة تقليل تضاعف الفيروس عن طريق:",
   O(("Promoting viral attachment to cells", "تعزيز التصاق الفيروس بالخلايا"), ("Destroying host-cell nuclei", "تحطيم أنوية الخلايا المضيفة"), ("Increasing viral uncoating", "زيادة إزالة غلاف الفيروس"), ("Blocking attachment to host cells", "منع الالتصاق بالخلايا المضيفة"), ("Producing viral enzymes", "إنتاج إنزيمات فيروسية")), "d"),
   "B", "D", "blocking attachment to the host cell", "منع الالتصاق بالخلية المضيفة"),
 Q("Neutralizing antibodies typically recognize:", "تتعرّف الأضداد المعادِلة عادةً على:",
   O(("Proteins or glycoproteins on the virion surface", "البروتينات أو البروتينات السكرية على سطح الفيريون"), ("Host-cell ribosomes", "رايبوسومات الخلية المضيفة"), ("Viral nucleic acid only", "الحامض النووي الفيروسي فقط"), ("Bacterial cell walls", "جدران الخلايا البكتيرية"), ("Red blood cell membranes only", "أغشية كريات الدم الحمر فقط")), "a"),
 kn(Q("In the VNT, serum samples are prepared as:", "في VNT تُحضَّر عيّنات المصل بصورة:",
   O(("A single undiluted sample only", "عيّنة واحدة غير مخفّفة فقط"), ("Heat-fixed bacterial cultures", "مزارع بكتيرية مثبّتة بالحرارة"), ("Serial dilutions", "تخافيف متسلسلة"), ("Agar plates", "أطباق آغار"), ("Stained blood films", "مسحات دم مصبوغة")), "c"),
   "B", "C", "serial dilutions of the serum sample", "تخافيف متسلسلة لعيّنة المصل"),
 kn(Q("In a VNT, each serum dilution is mixed with:", "في VNT يُمزج كل تخفيف للمصل مع:",
   O(("Bacterial colonies", "مستعمرات بكتيرية"), ("Antibiotics only", "مضادّات حيوية فقط"), ("Sheep red blood cells", "كريات دم حمر للأغنام"), ("Complement proteins", "بروتينات المتمّم"), ("A known quantity of virus", "كمية معروفة من الفيروس")), "e"),
   "A", "E", "a known quantity of the virus is mixed with each dilution", "تُمزج كمية معروفة من الفيروس مع كل تخفيف"),
 Q("After serum and virus are incubated, which cells are added:", "بعد حضن المصل والفيروس، أيّ خلايا تُضاف:",
   O(("Nonliving artificial cells", "خلايا صناعية غير حيّة"), ("Cells susceptible to the virus", "خلايا قابلة للإصابة بالفيروس"), ("Fungal cells", "خلايا فطرية"), ("Bacterial spores", "أبواغ بكتيرية"), ("Platelets", "صفائح دموية")), "b"),
 kn(Q("If cells remain healthy during the VNT, this indicates that:", "إذا بقيت الخلايا سليمة أثناء VNT فهذا يدلّ على أن:",
   O(("The virus infected the cells", "الفيروس أصاب الخلايا"), ("No antibodies were present", "لم توجد أضداد"), ("The serum contained bacteria", "المصل احتوى بكتيريا"), ("Neutralizing antibodies prevented infection", "الأضداد المعادِلة منعت الإصابة"), ("Viral replication increased", "تضاعف الفيروس ازداد")), "d"),
   "B", "D", "healthy cells mean the antibodies neutralized the virus", "الخلايا السليمة تعني أن الأضداد عادلت الفيروس"),
 Q("The neutralization titer is defined as:", "يُعرَّف عيار التعادل بأنه:",
   O(("The lowest dilution causing cell death", "أدنى تخفيف يسبّب موت الخلايا"), ("The highest dilution that completely inhibits viral infection", "أعلى تخفيف يثبّط الإصابة الفيروسية تثبيطًا كاملًا"), ("The total number of viruses in serum", "العدد الكلي للفيروسات في المصل"), ("The amount of complement in serum", "كمية المتمّم في المصل"), ("The number of cells in culture", "عدد الخلايا في المزرعة")), "b"),
 Q("A higher VNT titer generally indicates:", "العيار الأعلى في VNT يدلّ عمومًا على:",
   O(("A lower level of neutralizing antibodies", "مستوى أقل من الأضداد المعادِلة"), ("A higher level of neutralizing antibodies", "مستوى أعلى من الأضداد المعادِلة"), ("Absence of viral exposure", "عدم التعرّض للفيروس"), ("Increased bacterial infection", "زيادة العدوى البكتيرية"), ("Failure of the vaccine", "فشل اللقاح")), "b"),
 Q("Which is a limitation of the Virus Neutralization Test:", "أيّها من قيود اختبار تعادل الفيروس:",
   O(("It requires no specialized equipment", "لا يحتاج أجهزة متخصّصة"), ("It is rapid and simple to standardize", "سريع وسهل التوحيد"), ("It is complex and time-consuming", "معقّد ويستغرق وقتًا"), ("It cannot measure neutralizing antibodies", "لا يستطيع قياس الأضداد المعادِلة"), ("It does not require susceptible cells", "لا يحتاج خلايا حسّاسة")), "c"),
]

mine = [
 {"topic_en": "BIOS questions", "topic_ar": "أسئلة BIOS"},
 Q("Neutralizing antibodies may prevent the virus from:", "قد تمنع الأضداد المعادِلة الفيروس من:",
   O(("Uncoating within the cell", "إزالة غلافه داخل الخلية"), ("Being diluted", "التخفيف"), ("Binding complement", "ربط المتمّم"), ("Agglutinating RBCs", "تلزين كريات الدم الحمر")), "a"),
 Q("Some antibodies that bind virion surface proteins are not neutralizing; in some cases they may:", "بعض الأضداد التي ترتبط ببروتينات سطح الفيريون ليست معادِلة؛ وفي بعض الحالات قد:",
   O(("Destroy the host cell nucleus", "تحطّم نواة الخلية المضيفة"), ("Enhance infection", "تعزّز العدوى"), ("Become complement", "تتحوّل إلى متمّم"), ("Replicate the virus", "تضاعف الفيروس")), "b"),
 Q("The magnitude of neutralization by a given antibody may vary with:", "قد يختلف مقدار التعادل بضدّ معيّن باختلاف:",
   O(("The colour of the serum", "لون المصل"), ("The day of the week", "يوم الأسبوع"), ("The host cell used for the measurement", "الخلية المضيفة المستعملة في القياس"), ("The size of the plate only", "حجم الصفيحة فقط")), "c"),
 Q("Neutralization in vitro and protection in vivo are:", "التعادل في المختبر والحماية في الجسم الحي:",
   O(("Always identical", "متطابقان دائمًا"), ("Never related", "غير مترابطين أبدًا"), ("Unrelated to antibodies", "لا علاقة لهما بالأضداد"), ("Usually related but not always perfectly correlated", "مترابطان عادةً لكن ليس دائمًا تمامًا")), "d"),
 Q("The VNT is important for measuring all of these EXCEPT:", "يُعدّ VNT مهمًا لقياس كل ما يلي عدا:",
   O(("Blood glucose", "سكر الدم"), ("Protective immunity", "المناعة الواقية"), ("Vaccine efficacy", "كفاءة اللقاح"), ("Virus identification", "تحديد هوية الفيروس")), "a"),
 Q("In the observation step, healthy cells at a dilution mean:", "في خطوة المراقبة، الخلايا السليمة عند تخفيف معيّن تعني:",
   O(("The virus was not added", "لم يُضف الفيروس"), ("Antibodies neutralized the virus at that dilution", "الأضداد عادلت الفيروس عند ذلك التخفيف"), ("The cells were not susceptible", "الخلايا غير حسّاسة"), ("The titer is zero", "العيار صفر")), "b"),
 Q("The VNT titer indicates:", "يدلّ عيار VNT على:",
   O(("The number of cells", "عدد الخلايا"), ("The amount of complement", "كمية المتمّم"), ("The level of neutralizing antibodies in the sample", "مستوى الأضداد المعادِلة في العيّنة"), ("The virus genome size", "حجم جينوم الفيروس")), "c"),
 Q("Measuring neutralizing antibodies induced by vaccination is used in:", "قياس الأضداد المعادِلة التي يحفّزها التلقيح يُستعمل في:",
   O(("Epidemiological prevalence only", "انتشار وبائي فقط"), ("Blood grouping", "تحديد فصائل الدم"), ("Bacterial culture", "الزرع البكتيري"), ("Vaccine development", "تطوير اللقاحات")), "d"),
 Q("Determining the prevalence of neutralizing antibodies in a population is a:", "تحديد انتشار الأضداد المعادِلة في مجتمع ما يُعدّ:",
   O(("Epidemiological study", "دراسة وبائية"), ("Vaccine failure", "فشل لقاح"), ("Cell culture step", "خطوة زرع خلايا"), ("Titer determination step", "خطوة تحديد عيار")), "a"),
 Q("Which is NOT a limitation of the VNT?", "أيّها ليس من قيود VNT؟",
   O(("Complex", "معقّد"), ("It needs susceptible cells and a known amount of virus", "يحتاج خلايا حسّاسة وكمية معروفة من فيروس"), ("Time-consuming", "يستغرق وقتًا"), ("Difficult to standardize across laboratories", "صعب التوحيد بين المختبرات")), "b"),
 {"topic_en": "Picture questions", "topic_ar": "أسئلة الصور"},
 Q("In this figure, the wells with non-neutralizing antibodies (negative control) end with:", "في هذا الشكل، الحفر التي فيها أضداد غير معادِلة (السيطرة السالبة) تنتهي بـ:",
   O(("Uninfected cells", "خلايا غير مصابة"), ("No cells", "لا خلايا"), ("Virus infected cells", "خلايا مصابة بالفيروس"), ("Complement fixation", "تثبيت المتمّم")), "c", img="assets/vnt.jpg", img_h="40mm"),
 Q("In this figure, after adding the cells the plate is incubated for:", "في هذا الشكل، بعد إضافة الخلايا تُحضن الصفيحة مدّة:",
   O(("1–2 hours", "1–2 ساعة"), ("30 minutes", "30 دقيقة"), ("3–7 days", "3–7 أيام"), ("24 weeks", "24 أسبوعًا")), "c", img="assets/vnt.jpg", img_h="40mm"),
]
mcq = lab + balance(mine, 61)

tf = [
 TF("Neutralizing antibodies can prevent a virus from attaching to host cells.", "تستطيع الأضداد المعادِلة منع الفيروس من الالتصاق بالخلايا المضيفة.", "T"),
 TF("All antibodies that bind to viral surface proteins are neutralizing antibodies.", "كل الأضداد التي ترتبط ببروتينات سطح الفيروس أضداد معادِلة.", "F"),
 TF("In VNT, serum is commonly tested using serial dilutions.", "في VNT يُفحص المصل عادةً باستعمال تخافيف متسلسلة.", "T"),
 TF("The VNT titer is the lowest serum dilution that inhibits viral infection.", "عيار VNT هو أدنى تخفيف للمصل يثبّط الإصابة الفيروسية.", "F"),
 TF("Healthy cells after incubation may indicate viral neutralization by antibodies.", "الخلايا السليمة بعد الحضن قد تدلّ على تعادل الفيروس بالأضداد.", "T"),
 TF("A higher neutralization titer indicates a higher level of neutralizing antibodies.", "عيار التعادل الأعلى يدلّ على مستوى أعلى من الأضداد المعادِلة.", "T"),
 TF("VNT may be used to assess vaccine efficacy.", "قد يُستعمل VNT لتقييم كفاءة اللقاح.", "T"),
 TF("Neutralization measured in vitro is always perfectly correlated with protection in vivo.", "التعادل المقيس في المختبر يرتبط دائمًا ارتباطًا تامًّا بالحماية في الجسم الحي.", "F"),
 TF("VNT can be used in epidemiological studies to determine antibody prevalence in a population.", "يمكن استعمال VNT في الدراسات الوبائية لتحديد انتشار الأضداد في مجتمع ما.", "T"),
 TF("VNT is a simple assay that requires no specialized equipment or expertise.", "VNT اختبار بسيط لا يحتاج أجهزة متخصّصة أو خبرة.", "F"),
 TF("Neutralizing antibodies typically recognize proteins or glycoproteins on the virion surface.", "تتعرّف الأضداد المعادِلة عادةً على البروتينات أو البروتينات السكرية على سطح الفيريون.", "T"),
 TF("In the VNT, susceptible cells are added before the virus is mixed with the serum.", "في VNT تُضاف الخلايا الحسّاسة قبل مزج الفيروس مع المصل.", "F"),
]

traps = [
 TR("Highest, not lowest", "الأعلى لا الأدنى", "The titer is the HIGHEST dilution of serum that COMPLETELY inhibits infection — not the lowest dilution.", "العيار هو أعلى تخفيف للمصل يثبّط الإصابة تثبيطًا كاملًا — وليس أدنى تخفيف."),
 TR("Higher titer", "العيار الأعلى", "A higher titer = MORE neutralizing antibodies (the serum still works when diluted more).", "العيار الأعلى = أضداد معادِلة أكثر (المصل يعمل حتى بعد تخفيف أكبر)."),
 TR("Healthy cells", "الخلايا السليمة", "Healthy cells = the virus was NEUTRALIZED (antibody present) — not 'no antibodies'.", "الخلايا السليمة = الفيروس تعادل (الضدّ موجود) — وليس 'لا أضداد'."),
 TR("Binding ≠ neutralizing", "الارتباط ≠ التعادل", "Some antibodies bind surface proteins but do not neutralize; some may even enhance infection.", "بعض الأضداد ترتبط بالبروتينات السطحية لكنها لا تعادل؛ وبعضها قد يعزّز العدوى."),
 TR("Order of the steps", "ترتيب الخطوات", "Serum dilutions + virus FIRST (incubate), THEN add susceptible cells.", "تخافيف المصل + الفيروس أولًا (حضن)، ثم تُضاف الخلايا الحسّاسة."),
 TR("VNT vs CFT (lab 5)", "VNT مقابل CFT (العملي 5)", "VNT uses virus + susceptible cells and reads infection; CFT uses complement + sheep RBCs and reads hemolysis.", "VNT يستعمل فيروسًا + خلايا حسّاسة ويقرأ الإصابة؛ وCFT يستعمل المتمّم + كريات أغنام ويقرأ تحلّل الدم."),
 TR("The sheet's answer-key line", "سطر مفتاح الأجوبة في الورقة", "The line 'Answer key: 1-B, 2-B, 3-A, 4-B, 5-A, 6-B, 7-B, 8-B, 9-B, 10-C' does not match questions 2, 4, 5 and 7 — follow the bold answers (D, C, E, D).", "سطر 'Answer key' لا يطابق الأسئلة 2 و4 و5 و7 — اعتمد الأجوبة الغامقة (D وC وE وD)."),
]

important = [
 IM("What is virus neutralization and why is it important in virology?", "ما تعادل الفيروس ولماذا هو مهم في علم الفيروسات؟",
    "Antibodies decrease the replication of viruses (neutralize them). It is important for measuring protective immunity, vaccine efficacy and virus identification.",
    "الأضداد تقلّل تضاعف الفيروسات (تعادلها). وهو مهم لقياس المناعة الواقية وكفاءة اللقاح وتحديد هوية الفيروس."),
 IM("How can antibodies neutralize viruses?", "كيف تعادل الأضداد الفيروسات؟",
    "By blocking attachment to the host cell, preventing penetration of the host cell membrane, or interfering with uncoating of the virus within the cell; they usually recognize proteins or glycoproteins on the virion surface.",
    "بمنع الالتصاق بالخلية المضيفة، أو منع اختراق غشائها، أو التداخل مع إزالة غلاف الفيروس داخل الخلية؛ وتتعرّف عادةً على البروتينات أو البروتينات السكرية على سطح الفيريون."),
 IM("Explain the principle of the VNT.", "اشرح مبدأ VNT.",
    "Serial dilutions of serum are mixed with a known amount of virus, then incubated with susceptible cells. Neutralizing antibodies bind the virus and prevent infection of the cells. The highest dilution that completely inhibits infection is the neutralization titer.",
    "تُمزج تخافيف متسلسلة من المصل مع كمية معروفة من الفيروس، ثم تُحضن مع خلايا حسّاسة. ترتبط الأضداد المعادِلة بالفيروس وتمنع إصابة الخلايا. وأعلى تخفيف يثبّط الإصابة تثبيطًا كاملًا هو عيار التعادل."),
 IM("List the methods (steps) of the VNT.", "عدّد خطوات VNT.",
    "1. Sample preparation (serial dilutions of serum). 2. Virus incubation (known quantity of virus + each dilution). 3. Cell culture (add susceptible cells). 4. Observation (signs of infection; healthy cells = neutralized). 5. Titer determination (highest dilution still preventing infection).",
    "1. تحضير العيّنة (تخافيف متسلسلة للمصل). 2. حضن الفيروس (كمية معروفة + كل تخفيف). 3. مزرعة الخلايا (إضافة خلايا حسّاسة). 4. المراقبة (علامات الإصابة؛ خلايا سليمة = تعادل). 5. تحديد العيار (أعلى تخفيف لا يزال يمنع الإصابة)."),
 IM("Give the applications and the limitations of the VNT.", "اذكر استعمالات VNT وقيوده.",
    "Applications: vaccine development (efficacy), diagnosis of viral infections, epidemiological studies (prevalence). Limitations: complex and time-consuming, needs specialized equipment and expertise, difficult to standardize across laboratories.",
    "الاستعمالات: تطوير اللقاحات (الكفاءة)، وتشخيص الإصابات الفيروسية، والدراسات الوبائية (الانتشار). القيود: معقّد ويستغرق وقتًا، ويحتاج أجهزة متخصّصة وخبرة، وصعب التوحيد بين المختبرات."),
 IM("How are VNT results interpreted?", "كيف تُفسَّر نتائج VNT؟",
    "As a titer — the highest dilution of serum that completely inhibits viral infection; a higher titer means a higher level of neutralizing antibodies.",
    "بصورة عيار — أعلى تخفيف للمصل يثبّط الإصابة الفيروسية تثبيطًا كاملًا؛ والعيار الأعلى يعني مستوى أعلى من الأضداد المعادِلة."),
]

meta = {"subject_en": "Medical Virology", "subject_ar": "الفيروسات الطبية", "short_ar": "فايروسات", "instructor": "د. آية وسمي",
        "unit_en": "Lab 6", "unit_ar": "العملي 6", "unit_label": "LAB", "unit_no": "6",
        "title_en": "Virus Neutralization Test (VNT)", "title_ar": "اختبار تعادل الفيروس",
        "kind": "Laboratories — عملي", "stage": "The third stage — الثالثة"}
blocks, mcq, tf, traps, important = ltr_all(blocks), ltr_all(mcq), ltr_all(tf), ltr_all(traps), ltr_all(important)   # formulas inside Arabic stay LTR
save("virology-lab6-neutralization", meta, blocks, mcq, tf, traps, important)
fit("virology-lab6-neutralization")   # no big gaps

```
