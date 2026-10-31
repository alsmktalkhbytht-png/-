---
source: BIOS-Obsidian/tools/scripts/at5/a5.py
handouts: []
saved: 2026-10-31
tags: [bios, code]
---
# at5/a5.py

Utility script.

```python
import sys, re; sys.path.insert(0, "/tmp/claude-0/-home-claude/ff420988-e3a4-58e4-8344-8f014438cb53/scratchpad/imm456")
from ci import *            # c helpers + B INSHORT TERMS balance save(split.fix)

BN = lambda en, ar: N(en, ar, label=["BIOS note", "ملاحظة BIOS"])
O = P
def LAB(*pairs, en="Labels in the figure", ar="كتابات الشكل"):
    cells = [B(f"**{e}**", a) for e, a in pairs]
    if len(cells) % 2: cells.append(B("", ""))
    return T([B("Label", "الكتابة"), B("Label", "الكتابة")], [cells[i:i + 2] for i in range(0, len(cells), 2)],
             style="summary", label_en=en, label_ar=ar)
def FG(src, en, ar, h, **k): return F(src, en, ar, h=h, fit="contain", **k)

blocks = [
 SEC("Polymerase Chain Reaction", "تفاعل البلمرة المتسلسل"),
 FG("dna-helix.png", "DNA double helix", "اللولب المزدوج للـ DNA", "40mm"),
 BN("All the slides of this lecture are pictures of text; the English below is copied word for word from those pictures.", "كل شرائح هذه المحاضرة صور لنصوص؛ والإنكليزي أدناه منقول حرفيًا من تلك الصور."),

 SEC("What is PCR?", "ما هو PCR؟"),
 C("**Polymerase Chain Reaction** is an *in vitro* technique for the **amplification** of a **specific sequence of DNA** Which is used for further testing.",
   "**تفاعل البلمرة المتسلسل** تقنية **خارج الجسم الحي (في المختبر)** **لتضخيم** **تسلسل محدّد من الـ DNA** يُستعمل في فحوص لاحقة."),
 FG("pcr-machine.png", "PCR machine (thermal cycler)", "جهاز PCR (المدوّر الحراري)", "44mm"),
 C(["PCR or Polymerase Chain Reaction is a technique used in **molecular biology** to create **several copies of a certain DNA segment**.",
    "This technique was developed in **1983** by **Kary Mullis**, an American biochemist.",
    "PCR has made it possible to generate **millions of copies** of a small segment of DNA.",
    "This tool is commonly used in the molecular biology and biotechnology labs."],
   ["الـ PCR أو تفاعل البلمرة المتسلسل تقنية تُستعمل في **البيولوجيا الجزيئية** لصنع **نسخ عديدة من قطعة DNA معيّنة**.",
    "طُوّرت هذه التقنية عام **1983** على يد **كاري موليس**، عالم الكيمياء الحيوية الأمريكي.",
    "وقد جعل الـ PCR من الممكن توليد **ملايين النسخ** من قطعة صغيرة من الـ DNA.",
    "وتُستعمل هذه الأداة عادةً في مختبرات البيولوجيا الجزيئية والتقانة الحيوية."]),
 INSHORT([("PCR = **in vitro amplification** of a **specific DNA sequence** → millions of copies.", "PCR = **تضخيم في المختبر** **لتسلسل DNA محدّد** ← ملايين النسخ."),
          ("Developed in **1983** by **Kary Mullis**.", "طُوّر عام **1983** على يد **كاري موليس**.")]),

 SEC("Principle of PCR", "مبدأ PCR"),
 C(["The principle of PCR is based on the **enzymatic replication of nucleic acids**.", "PCR involves the use of **primer mediated enzymes** for the amplification of DNA."],
   ["يقوم مبدأ PCR على **التضاعف الإنزيمي للأحماض النووية**.", "ويتضمّن PCR استعمال **إنزيمات تعمل بوساطة البادئات** لتضخيم الـ DNA."]),
 C(["**DNA Polymerase** synthesises new strands of DNA **complementary to the template DNA**.", "The DNA polymerase can add a nucleotide to the **pre-existing 3’-OH group only**.",
    "Therefore, a **primer is required**.", "Thus, more nucleotides are added to the 3’ prime end of the DNA polymerase."],
   ["يصنّع **إنزيم بلمرة الـ DNA** سلاسل DNA جديدة **مكمّلة لـ DNA القالب**.", "ولا يستطيع إنزيم البلمرة إضافة نيوكليوتيد إلا إلى **مجموعة 3’-OH موجودة مسبقًا**.",
    "لذلك **يلزم وجود بادئ**.", "وهكذا تُضاف نيوكليوتيدات أخرى إلى الطرف 3’ (عبر إنزيم البلمرة)."]),
 BN("“added to the 3’ prime end of the DNA polymerase” means added to the **3’ end of the primer (the growing strand)** by the DNA polymerase.",
    "“added to the 3’ prime end of the DNA polymerase” يُقصد بها تُضاف إلى **الطرف 3’ للبادئ (السلسلة النامية)** بواسطة إنزيم البلمرة."),
 FG("primer-extension.png", "DNA polymerase extends primers from their 3’ ends", "إنزيم البلمرة يمدّ البادئات من أطرافها 3’", "26mm"),
 BN("The labels in this figure are only the strand ends 5’ and 3’.", "كتابات هذا الشكل هي أطراف السلاسل فقط: 5’ و3’."),
 INSHORT([("Enzymatic replication of DNA using **primers**.", "تضاعف إنزيمي للـ DNA باستعمال **البادئات**."),
          ("Polymerase adds nucleotides only to a **free 3’-OH** → that is why a **primer is required**.", "إنزيم البلمرة يضيف النيوكليوتيدات فقط إلى **3’-OH حرّة** ← ولهذا **يلزم البادئ**.")]),

 SEC("Components of the reaction mixture", "مكوّنات خليط التفاعل"),
 L(["Template DNA.", "Primers (forward and reverse)", "dNTPs", "*Taq* DNA Polymerase", "Buffer solution", "Divalent cations", "Sterile deionized water"],
   ["DNA القالب.", "البادئات (الأمامي والعكسي)", "ثلاثيات فوسفات النيوكليوتيدات منقوصة الأكسجين (dNTPs)", "إنزيم بلمرة الـ DNA من *Taq*", "المحلول المنظِّم", "الأيونات الموجبة ثنائية التكافؤ", "ماء معقّم منزوع الأيونات"]),
 FG("reaction-tube.png", "Components inside the PCR tube", "المكوّنات داخل أنبوب PCR", "56mm", keep=True),
 LAB(("Primer", "البادئ"), ("Nucleotides", "النيوكليوتيدات"), ("Taq polymerase", "إنزيم بلمرة Taq"), ("DNA", "الـ DNA")),
 C("**Components of PCR constitutes the following:**", "**تتكوّن مكوّنات PCR ممّا يأتي:**"),
]
blocks += [
 dict(t="group", title_en="DNA Template", title_ar="DNA القالب", en="the DNA of interest from the sample.", ar="الـ DNA المطلوب من العيّنة."),
 dict(t="group", title_en="DNA Polymerase", title_ar="إنزيم بلمرة الـ DNA",
      en=["**Taq Polymerase** is used.", "It is the rmostable and **does not denature at very high temperatures**."],
      ar=["يُستعمل **إنزيم بلمرة Taq**.", "وهو مقاوم للحرارة و**لا يتمسّخ عند درجات الحرارة العالية جدًا**."]),
 dict(t="group", title_en="Oligonucleotide Primers", title_ar="البادئات قليلة النيوكليوتيدات",
      en="These are the **short stretches of single-stranded DNA** complementary to the **3’ ends of sense and anti-sense strands**.",
      ar="قطع **قصيرة من DNA أحادي السلسلة** مكمّلة **للأطراف 3’ للسلسلتين المعنوية والمضادة للمعنى**."),
 dict(t="group", title_en="Deoxyribo-nucleotide triphosphate", title_ar="ثلاثيات فوسفات النيوكليوتيدات منقوصة الأكسجين",
      en=["These provide **energy for polymerization** and are the **building blocks** for the synthesis of DNA.", "These are single units of bases."],
      ar=["توفّر **الطاقة للبلمرة** وهي **وحدات البناء** لتصنيع الـ DNA.", "وهي وحدات مفردة من القواعد."]),
 dict(t="group", title_en="Buffer System", title_ar="النظام المنظِّم (الدارئ)",
      en=["**Magnesium and Potassium** provide optimum conditions for DNA denaturation and re-naturation.", "It is also important for **fidelity, polymerase activity, and stability**."],
      ar=["يوفّر **المغنيسيوم والبوتاسيوم** الظروف المثلى لتمسّخ الـ DNA وإعادة تكوّنه.", "وهو مهم أيضًا **لدقّة النسخ ونشاط إنزيم البلمرة وثباته**."]),
 BN("“the rmostable” is **thermostable** (heat-stable). The divalent cation in the mix is **Mg²⁺** (magnesium).", "“the rmostable” هي **thermostable** أي مقاوم للحرارة. والأيون ثنائي التكافؤ في الخليط هو **Mg²⁺** (المغنيسيوم)."),
 FG("dna-replication.png", "DNA REPLICATION", "تضاعف الـ DNA", "58mm", keep=True),
 LAB(("Chromosome", "الكروموسوم"), ("Free nucleotides", "النيوكليوتيدات الحرّة"), ("DNA polymerase", "إنزيم بلمرة الـ DNA"), ("Leading strand", "السلسلة القائدة"),
     ("Original DNA", "الـ DNA الأصلي"), ("Helicase", "الهيليكيز (فاكّ اللولب)"), ("Lagging strand", "السلسلة المتأخّرة"), ("Replication fork", "شوكة التضاعف"),
     ("Original DNA strand", "سلسلة الـ DNA الأصلية"), ("Adenine / Thymine / Cytosine / Guanine", "الأدينين / الثايمين / السايتوسين / الغوانين")),
 FG("initial-mix.png", "Initial Mix (room temperature, + Mg)", "الخليط الأوّلي (حرارة الغرفة، + مغنيسيوم)", "50mm", keep=True),
 LAB(("Initial Mix", "الخليط الأوّلي"), ("Room Temperature", "حرارة الغرفة"), ("+Mg", "+ مغنيسيوم"), ("Forward Primer", "البادئ الأمامي"),
     ("Reverse Primer", "البادئ العكسي"), ("A G C T Deoxynucleotides", "النيوكليوتيدات منقوصة الأكسجين A G C T")),
 T([B("Component", "المكوّن"), B("Role", "الدور")],
   [[B("**Template DNA**", "**DNA القالب**"), B("the DNA of interest from the sample", "الـ DNA المطلوب من العيّنة")],
    [B("**Primers (forward and reverse)**", "**البادئات (أمامي وعكسي)**"), B("short single-stranded DNA complementary to the 3’ ends; starting point", "DNA قصير أحادي السلسلة مكمّل للأطراف 3’؛ نقطة البداية")],
    [B("**dNTPs**", "**dNTPs**"), B("energy for polymerization + building blocks", "طاقة للبلمرة + وحدات البناء")],
    [B("**Taq DNA Polymerase**", "**بلمرة Taq**"), B("thermostable; adds bases to the 3’ end", "مقاوم للحرارة؛ يضيف القواعد إلى الطرف 3’")],
    [B("**Buffer (Mg, K) / divalent cations**", "**المنظِّم (Mg، K) / أيونات ثنائية التكافؤ**"), B("optimum conditions; fidelity, activity, stability", "الظروف المثلى؛ الدقّة والنشاط والثبات")],
    [B("**Sterile deionized water**", "**ماء معقّم منزوع الأيونات**"), B("makes up the volume (BIOS addition)", "يكمل الحجم (إضافة BIOS)")]],
   key_cols=[0], widths=[34, 66], style="summary", label_en="Components at a glance", label_ar="المكوّنات بنظرة"),
 INSHORT([("Mix = **template, 2 primers, dNTPs, Taq, buffer, Mg²⁺, water**.", "الخليط = **قالب، بادئان، dNTPs، Taq، منظِّم، Mg²⁺، ماء**."),
          ("**Taq** = thermostable polymerase; **dNTPs** = energy + building blocks.", "**Taq** = إنزيم بلمرة مقاوم للحرارة؛ **dNTPs** = طاقة + وحدات بناء.")]),

 SEC("PCR Steps", "خطوات PCR"),
 C("The PCR involves **three major cyclic reactions:**", "يتضمّن PCR **ثلاثة تفاعلات دورية رئيسية:**"),
 H2("Denaturation", "التمسّخ (الفصل)"),
 C(["Denaturation occurs when the reaction mixture is heated to **94°C** for about **15-30 minutes**.", "This **breaks the hydrogen bonds** between the two strands of DNA and converts it into a **single-stranded DNA**."],
   ["يحدث التمسّخ عند تسخين خليط التفاعل إلى **94°م** لمدّة نحو **15-30 دقيقة**.", "وهذا **يكسر الروابط الهيدروجينية** بين سلسلتي الـ DNA ويحوّله إلى **DNA أحادي السلسلة**."]),
 C(["The single strands now act as a **template** for the production of new strands of DNA.", "The temperature should be provided for a longer time to ensure the separation of the two strands."],
   ["تعمل السلاسل المفردة الآن **قالبًا** لإنتاج سلاسل DNA جديدة.", "ويجب توفير الحرارة مدّة أطول لضمان انفصال السلسلتين."]),
 BN("In each cycle denaturation usually takes **15–30 seconds** (the figure of the cycle says **1 minute at 94 °C**); a longer initial step of a few minutes is used only at the start. “15-30 minutes” is kept as written.",
    "التمسّخ في كل دورة يستغرق عادةً **15–30 ثانية** (وشكل الدورة يذكر **دقيقة واحدة بدرجة 94 °م**)؛ وخطوة أولى أطول ببضع دقائق تُستعمل في البداية فقط. وأُبقيت “15-30 minutes” كما كُتبت."),
 FG("denaturation.png", "Native (double helix) → Denatured (random coil)", "الأصلي (لولب مزدوج) ← المتمسّخ (التفاف عشوائي)", "40mm"),
 H2("Annealing", "الالتحام (التلدين)"),
 C(["The reaction temperature is lowered to **54-60°C** for around **20-40 seconds**.", "Here, the **primers bind to their complementary sequences** on the template DNA."],
   ["تُخفّض حرارة التفاعل إلى **54-60°م** لمدّة نحو **20-40 ثانية**.", "وهنا **ترتبط البادئات بتسلسلاتها المكمّلة** على DNA القالب."]),
 C("Primers are **single strand sequences of DNA or RNA** around **20 to 30 bases** in length.", "البادئات **تسلسلات أحادية السلسلة من DNA أو RNA** طولها نحو **20 إلى 30 قاعدة**."),
 C("They serve as the **starting point** for the synthesis of DNA.", "وهي تعمل **نقطة بداية** لتصنيع الـ DNA."),
 C("The two separated strands run in the **opposite direction** and consequently there are two primers- a **forward primer** and a **reverse primer**.",
   "تسير السلسلتان المنفصلتان **باتّجاهين متعاكسين**، ولذلك يوجد بادئان: **بادئ أمامي** و**بادئ عكسي**."),
 FG("annealing.png", "Primers annealing to the target sequence", "التحام البادئات بالتسلسل الهدف", "44mm", keep=True),
 LAB(("Target Sequence", "التسلسل الهدف"), ("Primer 1 / Primer 2", "البادئ 1 / البادئ 2"), ("Biotin", "البايوتين"), ("5’ / 3’", "أطراف السلاسل")),
 H2("Elongation", "الاستطالة (الامتداد)"),
 C(["At this step, the temperature is raised to **72-80°C**.", "The bases are added to the **3’ end of the primer** by the **Taq polymerase** enzyme."],
   ["في هذه الخطوة تُرفع الحرارة إلى **72-80°م**.", "وتُضاف القواعد إلى **الطرف 3’ للبادئ** بواسطة إنزيم **بلمرة Taq**."]),
 C(["This elongates the DNA in the **5’ to 3’ direction**.", "The DNA polymerase adds about **1000bp/minute** under optimum conditions."],
   ["وهذا يطيل الـ DNA **باتّجاه 5’ إلى 3’**.", "ويضيف إنزيم البلمرة نحو **1000 زوج قاعدي/دقيقة** في الظروف المثلى."]),
 C(["Taq Polymerase can **tolerate very high temperatures**.", "It attaches to the primer and adds DNA bases to the single strand.", "As a result, a **double-stranded DNA** molecule is obtained."],
   ["يتحمّل إنزيم بلمرة Taq **درجات الحرارة العالية جدًا**.", "يرتبط بالبادئ ويضيف قواعد الـ DNA إلى السلسلة المفردة.", "ونتيجةً لذلك نحصل على جزيء **DNA ثنائي السلسلة**."]),
 C("These three steps are **repeated 20-40 times** in order to obtain a number of sequences of DNA of interest in a very short time period.",
   "تُكرَّر هذه الخطوات الثلاث **20-40 مرّة** للحصول على عدد من تسلسلات الـ DNA المطلوبة في مدّة قصيرة جدًا."),
 FG("elongation.png", "72 °C (extension of the primers)", "72 °م (امتداد البادئات)", "26mm"),
 T([B("Step", "الخطوة"), B("Temperature", "الحرارة"), B("Time", "الوقت"), B("What happens", "ماذا يحدث")],
   [[B("**1. Denaturation**", "**1. التمسّخ**"), B("94°C", "94°م"), B("15-30 min (text) / 1 min (figure)", "15-30 دقيقة (النص) / دقيقة (الشكل)"), B("H-bonds break → single strands", "تنكسر الروابط الهيدروجينية ← سلاسل مفردة")],
    [B("**2. Annealing**", "**2. الالتحام**"), B("54-60°C", "54-60°م"), B("20-40 s (figure: 45 s at 54 °C)", "20-40 ثانية (الشكل: 45 ثانية بدرجة 54 °م)"), B("primers bind complementary sequences", "ترتبط البادئات بالتسلسلات المكمّلة")],
    [B("**3. Elongation**", "**3. الاستطالة**"), B("72-80°C", "72-80°م"), B("figure: 2 min at 72 °C", "الشكل: دقيقتان بدرجة 72 °م"), B("Taq adds bases to 3’ end, 5’→3’, ~1000 bp/min", "Taq يضيف القواعد للطرف 3’، 5’←3’، نحو 1000 زوج/دقيقة")]],
   key_cols=[0], widths=[20, 16, 28, 36], style="summary", label_en="The three steps", label_ar="الخطوات الثلاث"),
 FLOW([("Denaturation 94°C", "التمسّخ 94°م"), ("Annealing 54-60°C", "الالتحام 54-60°م"), ("Elongation 72-80°C", "الاستطالة 72-80°م"), ("Repeat 20-40 times", "التكرار 20-40 مرّة")], en="One PCR cycle", ar="دورة PCR واحدة"),
 FG("pcr-amplification.png", "PCR amplification — exponential amplification", "تضخيم PCR — تضخيم أسّي", "52mm", keep=True),
 LAB(("wanted gene", "الجين المطلوب"), ("template DNA", "DNA القالب"), ("1st / 2nd / 3th / 4th cycle", "الدورة الأولى / الثانية / الثالثة / الرابعة"), ("Exponential amplification", "تضخيم أسّي"),
     ("2² = 4 copies, 2³ = 8 copies, 16, 32 copies", "2² = 4 نسخ، 2³ = 8 نسخ، 16، 32 نسخة"), ("35th cycle: 2³⁶ = 68 billion copies", "الدورة 35: 2³⁶ = 68 مليار نسخة")),
 FG("pcr-cycle.png", "PCR : Polymerase Chain Reaction — 30 - 40 cycles of 3 steps", "PCR: تفاعل البلمرة المتسلسل — 30 - 40 دورة من 3 خطوات", "72mm", keep=True),
 LAB(("Step 1 : denaturation — 1 minut 94 °C", "الخطوة 1: التمسّخ — دقيقة واحدة 94 °م"), ("Step 2 : annealing — 45 seconds 54 °C", "الخطوة 2: الالتحام — 45 ثانية 54 °م"),
     ("forward and reverse primers !!!", "البادئان الأمامي والعكسي!!!"), ("Step 3 : extension — 2 minutes 72 °C", "الخطوة 3: الامتداد — دقيقتان 72 °م"),
     ("only dNTP's", "dNTPs فقط"), ("30 - 40 cycles of 3 steps", "30 - 40 دورة من 3 خطوات")),
 BN("The figures give **30–40** cycles and the text gives **20–40**; both are kept. “3th cycle” = 3rd cycle, “1 minut” = 1 minute.", "الأشكال تذكر **30–40** دورة والنص يذكر **20–40**؛ وأُبقي الاثنان. و“3th cycle” = الدورة الثالثة، و“1 minut” = دقيقة واحدة."),
 INSHORT([("**Denaturation 94°C** → **annealing 54-60°C** (primers 20-30 bases) → **elongation 72-80°C** (Taq, 5’→3’, ~1000 bp/min).", "**التمسّخ 94°م** ← **الالتحام 54-60°م** (بادئات 20-30 قاعدة) ← **الاستطالة 72-80°م** (Taq، 5’←3’، نحو 1000 زوج/دقيقة)."),
          ("Repeated **20-40 times**; copies double each cycle (**exponential**): 2ⁿ.", "تُكرَّر **20-40 مرّة**؛ وتتضاعف النسخ كل دورة (**أسّيًا**): 2ⁿ.")]),

 SEC("Application of PCR", "تطبيقات PCR"),
 L(["Cloning a Gene encoding a known protein", "Amplification of old DNA", "Amplifying cloned DNA from Vectors", "Rapid Amplification of cDNA ends", "Detecting Bacterial or Viral Infection"],
   ["استنساخ جين يرمّز بروتينًا معروفًا", "تضخيم الـ DNA القديم", "تضخيم الـ DNA المستنسخ من النواقل", "التضخيم السريع لأطراف الـ cDNA", "كشف الإصابات البكتيرية أو الفيروسية"]),
 L(["**AIDS infection**", "**Tuberculosis** (*Mycobacterium tuberculosis*)"], ["**إصابة الإيدز**", "**التدرّن** (*المتفطّرة السلّية*)"], alpha=True),
 C("**Genetics Diagnosis**", "**التشخيص الوراثي**"),
 L(["Diagnosing inherited disorders"], ["تشخيص الاضطرابات الوراثية"]),
 L(["Cystic fibrosis", "Muscular dystrophy", "Haemophilia A and B", "Sickle cell anaemia"], ["التليّف الكيسي", "الحثل العضلي", "الهيموفيليا A وB", "فقر الدم المنجلي"], alpha=True),
 L(["Diagnosing cancer", "Blood group typing."], ["تشخيص السرطان", "تحديد فصائل الدم."]),
 C("**Forensic Science**", "**علم الأدلّة الجنائية**"),
 L(["Used as a tool in **genetic fingerprinting**.", "Identifying the criminal from millions of people.", "Paternity tests"],
   ["يُستعمل أداةً في **البصمة الوراثية**.", "تحديد المجرم من بين ملايين الناس.", "فحوص الأبوّة"]),
 INSHORT([("Research: cloning, old DNA, vectors, cDNA ends; infection: **AIDS, TB**.", "البحث: الاستنساخ، الـ DNA القديم، النواقل، أطراف cDNA؛ الإصابات: **الإيدز، التدرّن**."),
          ("Genetics: cystic fibrosis, muscular dystrophy, haemophilia A/B, sickle cell, cancer, blood groups; forensic: **fingerprinting, criminals, paternity**.", "الوراثة: التليّف الكيسي، الحثل العضلي، الهيموفيليا، المنجلي، السرطان، فصائل الدم؛ الجنائي: **البصمة الوراثية، المجرمين، الأبوّة**.")]),

 *TERMS([("Polymerase Chain Reaction (PCR)", "تفاعل البلمرة المتسلسل / التفاعل التسلسلي للبوليميريز"),
         ("In vitro", "خارج الجسم الحي / في المختبر / في الزجاج"),
         ("Amplification", "التضخيم / المضاعفة"),
         ("Template DNA", "DNA القالب / الـ DNA الهدف"),
         ("Primer (forward / reverse)", "البادئ (الأمامي / العكسي) / البرايمر"),
         ("dNTPs", "ثلاثيات فوسفات النيوكليوتيدات منقوصة الأكسجين / النيوكليوتيدات الحرّة"),
         ("Taq polymerase", "إنزيم بلمرة Taq / البوليميريز المقاوم للحرارة"),
         ("Thermostable", "مقاوم للحرارة / ثابت حراريًا"),
         ("Divalent cations", "أيونات موجبة ثنائية التكافؤ"),
         ("Denaturation", "التمسّخ / الفصل / فكّ السلسلتين"),
         ("Annealing", "الالتحام / التلدين / الارتباط"),
         ("Elongation (extension)", "الاستطالة / الامتداد / التطويل"),
         ("Fidelity", "الدقّة / أمانة النسخ"),
         ("Exponential amplification", "التضخيم الأسّي"),
         ("Thermal cycler", "المدوّر الحراري / جهاز PCR"),
         ("Helicase", "الهيليكيز / فاكّ اللولب"),
         ("Replication fork", "شوكة التضاعف"),
         ("Leading / Lagging strand", "السلسلة القائدة / المتأخّرة"),
         ("cDNA", "الـ DNA المكمّل / المتمّم"),
         ("Genetic fingerprinting", "البصمة الوراثية / بصمة الـ DNA")]),
]

exec(open(__file__.replace("a5.py", "a5q.py")).read())

```
