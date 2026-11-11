---
source: BIOS-Obsidian/tools/scripts/elab4/el4.py
handouts: [enzymology-lab4-amylase-lipase]
saved: 2026-11-11
tags: [bios, code]
---
# elab4/el4.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#enzymology-lab4-amylase-lipase|enzymology-lab4-amylase-lipase]]

```python
import sys; sys.path.insert(0, "/tmp/claude-0/-home-user--/67d83c9a-7b0e-5ae5-b52b-cd659ab074ab/scratchpad/imm456")
from ci import *            # c helpers + B INSHORT TERMS balance save(split.fix)
sys.path.insert(0, "/tmp/claude-0/-home-user--/67d83c9a-7b0e-5ae5-b52b-cd659ab074ab/scratchpad"); from bidi import ltr_all; from flowfit import fit

# Clinical Enzymology — practical lab 4 (stage 4) — د. بارق & د. هشام — Serum Amylase and Serum Lipase.
# Source: amylase_and_Lipase.pdf (Word → ilovepdf, 4 pages). 3 pictures: carbohydrate digestion figure, lipase reaction and the
# lipase formula (the last two are pictures of text → "eq" blocks + text). Stage 4 → wineoat + separate question file.
BN = lambda en, ar: N(en, ar, label=["BIOS note", "ملاحظة BIOS"])
O = P
FOLDER = "enzymology-lab4-amylase-lipase"
EQ = lambda src, h="14mm": dict(t="eq", src="assets/" + src, h=h)

blocks = [
 # ───────────────────────── 1 amylase
 SEC("Serum Amylase", "الأميليز في المصل"),
 C("**Amylase** is an **enzyme** that catalyses the hydrolysis of starch into sugars.", "**الأميليز (`Amylase`)** **إنزيم** يحفّز تحلّل النشا مائيًا إلى سكّريات."),
 L(["Salivary glands.", "Pancreas.", "Liver."], ["الغدد اللعابية.", "البنكرياس.", "الكبد."], en="This enzyme produced by:", ar="يُنتَج هذا الإنزيم من:"),
 F("carbohydrate-digestion.png", "Carbohydrates Digestion", "هضم الكربوهيدرات", h="40mm"),
 T([B("Figure text", "كتابات الشكل"), B("Arabic", "بالعربي")],
   [[B("**Starch molecule (Polysaccharide)**", "**جزيء النشا (سكّر متعدّد)**"), B("broken by Amylase →", "يكسره الأميليز ←")],
    [B("**Maltose molecules (Disaccharide)**", "**جزيئات المالتوز (سكّر ثنائي)**"), B("broken by Maltase →", "يكسرها المالتيز ←")],
    [B("**Glucose molecules (Monosaccharide)**", "**جزيئات الغلوكوز (سكّر أحادي)**"), B("end product", "الناتج النهائي")]],
   key_cols=[0], widths=[55, 45], label_en="Figure text", label_ar="كتابات الشكل"),
 L(["Much lower activities are present in the ovaries, intestines, and skeletal muscle.",
    "If there is an inflammation of the above (pancreas or salivary glands) much amylase enters the blood."],
   ["توجد فعاليات أقلّ بكثير في المبيضين والأمعاء والعضلات الهيكلية.",
    "إذا حدث التهاب فيما ذُكر أعلاه (البنكرياس أو الغدد اللعابية) يدخل الدم كثير من الأميليز."], alpha=True),
 L(["α- amylase \" animal and human tissue \" .", "ᵝ- amylase “plant and bacterial organism\"."],
   ["`α`- أميليز «أنسجة الحيوان والإنسان».", "`β`- أميليز «النبات والكائنات البكتيرية»."], en="**Types of amylase:**", ar="**أنواع الأميليز:**"),
 C("**Normal value:** The normal range is 40 to 140 units per liter (U/L)", "**القيمة الطبيعية:** المدى الطبيعي 40 إلى 140 وحدة لكل لتر (`U/L`)"),
 INSHORT([("Amylase: **starch → sugars**; from **salivary glands, pancreas, liver**.", "الأميليز: **نشا ← سكّريات**؛ من **الغدد اللعابية، البنكرياس، الكبد**."),
          ("Inflamed pancreas / salivary glands → **much amylase in blood**.", "التهاب البنكرياس / الغدد اللعابية ← **أميليز كثير في الدم**."),
          ("**α**-amylase = animal/human; **β**-amylase = plant/bacteria; normal **40–140 U/L**.", "**`α`**-أميليز = حيوان/إنسان؛ **`β`**-أميليز = نبات/بكتيريا؛ الطبيعي **40–140 `U/L`**.")]),

 # ───────────────────────── 2 clinical, unit, principle
 SEC("Amylase: clinical use and principle", "الأميليز: الأهمية السريرية والمبدأ"),
 L(["Acute pancreatitis", "Carcinoma of head of the pancreas", "Peptic ulcers.", "Salivary gland disorder", "Tumor of salivary glands", "Intestinal obstruction and etc"],
   ["التهاب البنكرياس الحادّ", "سرطان رأس البنكرياس", "القرحة الهضمية.", "اضطراب الغدد اللعابية", "ورم الغدد اللعابية", "انسداد الأمعاء وغيرها"],
   en="**Clinical significance:**", ar="**الأهمية السريرية:**"),
 C("**Somogyi unit**: it’s a unit of amylase activity defined as the amount of enzyme that is able to liberate sugars with a reducing value equivalent to 1 gm of glucose in the course of a 30 min reaction at 37C and PH =7.",
   "**وحدة سوموجي (`Somogyi unit`)**: وحدة لفعالية الأميليز تُعرَّف بأنها كمّية الإنزيم القادرة على تحرير سكّريات قيمتها الاختزالية تعادل 1 غم من الغلوكوز خلال تفاعل مدّته 30 دقيقة عند `37°C` و`pH = 7`."),
 BN("In textbooks the Somogyi unit is the amount of enzyme that liberates reducing sugar equivalent to **1 mg** of glucose (per 100 mL of serum) — not 1 gm.",
    "في الكتب وحدة سوموجي هي كمّية الإنزيم التي تحرّر سكّرًا مختزلًا يعادل **1 ملغم** من الغلوكوز (لكل 100 مل مصل) — وليس 1 غم."),
 H2("**The principle:**", "**المبدأ:**"),
 C("Amylase · Triolein + 2H2O ------------------→ Monoglyceride + Oleic Acid", "الأميليز · `Triolein + 2H2O → Monoglyceride + Oleic Acid` (ترايولين + ماء ← أحادي الغليسيريد + حامض الأوليك)"),
 BN(["⚠ This equation is the **lipase** reaction (triolein is a fat), but in the sheet it is written under amylase with \"Amylase\" over the arrow.",
     "The amylase principle is the hydrolysis of **starch** to sugars (maltose, glucose), as in the figure above."],
    ["⚠ هذه المعادلة هي تفاعل **اللايبيز** (الترايولين دهن)، لكنها مكتوبة في الورقة تحت الأميليز وفوق السهم كلمة \"Amylase\".",
     "ومبدأ الأميليز هو تحلّل **النشا** مائيًا إلى سكّريات (مالتوز، غلوكوز)، كما في الشكل أعلاه."]),
 H2("**The procedure:**", "**طريقة العمل:**"),
 C("**READ THE PROCEDURE IN KIT**", "**اقرأ طريقة العمل في العُدّة (`KIT`)**"),
 INSHORT([("Amylase rises in **acute pancreatitis**, pancreatic head carcinoma, peptic ulcer, salivary gland disorders/tumors, intestinal obstruction.", "يرتفع الأميليز في **التهاب البنكرياس الحادّ**، سرطان رأس البنكرياس، القرحة الهضمية، اضطرابات/أورام الغدد اللعابية، انسداد الأمعاء."),
          ("Somogyi unit: sugar ≡ glucose in **30 min at 37 °C, pH 7**.", "وحدة سوموجي: سكّر يعادل الغلوكوز خلال **30 دقيقة عند `37°C` و`pH 7`**."),
          ("Procedure: **from the kit**.", "طريقة العمل: **من العُدّة**.")]),

 # ───────────────────────── 3 lipase
 SEC("Serum Lipase", "اللايبيز في المصل"),
 C("**Lipase** is an enzyme the body uses to break down fats in food into fatty acids and glycerol so they can be absorbed in the intestines.",
   "**اللايبيز (`Lipase`)** إنزيم يستعمله الجسم لتكسير دهون الطعام إلى أحماض دهنية وغليسيرول حتى تُمتصّ في الأمعاء."),
 EQ("lipase-reaction.png", "13mm"),
 C("lipase · Fats → Fatty acids + Glycerol", "اللايبيز · الدهون ← أحماض دهنية + غليسيرول"),
 C(["Lipase is produced in the pancreas, mouth, and stomach.",
    "Most people produce enough pancreatic lipase, but people with cystic fibrosis, Crohn disease, and celiac disease may not have enough lipase to get the nutrition they need from food."],
   ["يُنتَج اللايبيز في البنكرياس والفم والمعدة.",
    "ومعظم الناس ينتجون ما يكفي من لايبيز البنكرياس، لكن المصابين بالتليّف الكيسي وداء كرون والداء البطني (السيلياك) قد لا يملكون ما يكفي من اللايبيز للحصول على حاجتهم الغذائية من الطعام."]),
 C(["Lipase appears in the blood following pancreatic damage at the same time amylase appears (or slightly later) but remains elevated much longer than amylase (7 to 10 days).",
    "Amylase and lipase tests are used to diagnose and monitor treatment of acute pancreatitis and to differentiate pancreatitis from other acute abdominal disorders."],
   ["يظهر اللايبيز في الدم بعد تضرّر البنكرياس في الوقت نفسه الذي يظهر فيه الأميليز (أو بعده بقليل)، لكنه يبقى مرتفعًا مدّة أطول بكثير من الأميليز (7 إلى 10 أيام).",
    "وتُستعمل فحوص الأميليز واللايبيز لتشخيص التهاب البنكرياس الحادّ ومتابعة علاجه، وللتمييز بينه وبين الاضطرابات البطنية الحادّة الأخرى."]),
 L(["80% of patients with acute pancreatitis will have elevated amylase and lipase levels but lipase remains elevated longer than amylase.",
    "Lipase assay provides better sensitivity and specificity and is best used with amylase determination."],
   ["80% من مرضى التهاب البنكرياس الحادّ ترتفع لديهم مستويات الأميليز واللايبيز، لكن اللايبيز يبقى مرتفعًا مدّة أطول من الأميليز.",
    "وفحص اللايبيز يعطي حساسية ونوعية أفضل، ويُستعمل أفضل استعمال مع قياس الأميليز."], alpha=True),
 H2("**Normal value:**", "**القيمة الطبيعية:**"),
 T([B("Adults:", "البالغون:"), B("Elderly persons (>60 years):", "كبار السنّ (>60 سنة):")],
   [[B("10–140 U/L", "10–140 `U/L`"), B("18–180 U/L", "18–180 `U/L`")]], widths=[50, 50], label_en="Normal value:", label_ar="القيمة الطبيعية:"),
 T([B("", ""), B("Amylase", "الأميليز"), B("Lipase", "اللايبيز")],
   [[B("**Substrate**", "**الركيزة**"), B("starch → sugars", "النشا ← سكّريات"), B("fats (triolein) → fatty acids + glycerol", "الدهون (ترايولين) ← أحماض دهنية + غليسيرول")],
    [B("**Sources**", "**المصادر**"), B("salivary glands, pancreas, liver", "الغدد اللعابية، البنكرياس، الكبد"), B("pancreas, mouth, stomach", "البنكرياس، الفم، المعدة")],
    [B("**In pancreatitis**", "**في التهاب البنكرياس**"), B("rises early", "يرتفع مبكرًا"), B("same time or slightly later, stays **7–10 days**", "معه أو بعده بقليل، ويبقى **7–10 أيام**")],
    [B("**Sensitivity / specificity**", "**الحساسية / النوعية**"), B("lower", "أقلّ"), B("**better**", "**أفضل**")],
    [B("**Normal value**", "**القيمة الطبيعية**"), B("40–140 U/L", "40–140 `U/L`"), B("10–140 U/L (elderly 18–180)", "10–140 `U/L` (كبار السنّ 18–180)")]],
   key_cols=[0], widths=[26, 34, 40], style="summary", label_en="BIOS: amylase vs lipase", label_ar="BIOS: الأميليز مقابل اللايبيز"),
 INSHORT([("Lipase: **fats → fatty acids + glycerol**; from pancreas, mouth, stomach.", "اللايبيز: **دهون ← أحماض دهنية + غليسيرول**؛ من البنكرياس والفم والمعدة."),
          ("Low lipase in **cystic fibrosis, Crohn, celiac** disease.", "نقص اللايبيز في **التليّف الكيسي، كرون، السيلياك**."),
          ("Pancreatitis: lipase stays high **7–10 days**, **better sensitivity & specificity**; 80% have both elevated.", "التهاب البنكرياس: اللايبيز يبقى مرتفعًا **7–10 أيام**، و**حساسيته ونوعيته أفضل**؛ و80% يرتفع لديهم الاثنان.")]),

 # ───────────────────────── 4 lipase method
 SEC("Lipase: principle, procedure and calculation", "اللايبيز: المبدأ وطريقة العمل والحساب"),
 C("**The principle:** Pancreatic lipase catalyses the hydrolysis of Triolein to form monoglycerides and fatty acids.",
   "**المبدأ:** يحفّز لايبيز البنكرياس التحلّل المائي للترايولين (`Triolein`) فيكوّن أحادي الغليسيريدات وأحماضًا دهنية."),
 C("**The sample:** must be serum free form hemolysis.", "**العيّنة:** يجب أن تكون مصلًا خاليًا من تحلّل الدم."),
 BN(["\"free form hemolysis\" = free **from** hemolysis.", "C = calibrator tube, T = test tube; the example numbers are BIOS, the calibrator value is printed on the kit."],
    ["\"free form hemolysis\" = free **from** hemolysis (خالٍ من تحلّل الدم).", "`C` = أنبوب المعايِر، و`T` = أنبوب الفحص؛ وأرقام المثال من BIOS، وقيمة المعايِر مكتوبة على العُدّة."]),
 H2("**The procedure:**", "**طريقة العمل:**"),
 T(["", B("C", "C (المعايِر)"), B("T", "T (الفحص)")],
   [[B("**Reagent**", "**الكاشف**"), "1 ml", "1 ml"], [B("**Calibrator**", "**المعايِر**"), "0.04 ml", "--------"], [B("**Sample**", "**العيّنة**"), "---------", "0.04 ml"]],
   key_cols=[0], widths=[40, 30, 30], label_en="The procedure", label_ar="طريقة العمل"),
 L(["Mix well and incubate at room temperature for 4min and read A1", "Read A2 after 5 min."],
   ["اخلط جيدًا واحضن بحرارة الغرفة لمدّة 4 دقائق واقرأ `A1`", "اقرأ `A2` بعد 5 دقائق."]),
 H2("**Calculations:**", "**الحسابات:**"),
 EQ("lipase-formula.png", "12mm"),
 C("Lipase U/L= ΔAt/ ΔAc * conc", "اللايبيز (`U/L`) = `ΔAt / ΔAc × conc`"),
 T([B("Symbol", "الرمز"), B("Meaning", "المعنى")],
   [["**ΔAt**", B("A2 − A1 of the test (sample)", "`A2 − A1` للفحص (العيّنة)")],
    ["**ΔAc**", B("A2 − A1 of the calibrator", "`A2 − A1` للمعايِر")],
    ["**conc**", B("lipase activity of the calibrator (U/L, from the kit)", "فعالية اللايبيز في المعايِر (`U/L`، من العُدّة)")],
    [B("**Example**", "**مثال**"), B("ΔAt = 0.030, ΔAc = 0.060, conc = 120 U/L → 0.030/0.060 × 120 = 60 U/L (normal)", "`ΔAt = 0.030`، `ΔAc = 0.060`، `conc = 120 U/L` ← `0.030/0.060 × 120 = 60 U/L` (طبيعي)")]],
   key_cols=[0], widths=[22, 78], style="summary", label_en="BIOS: reading the formula", label_ar="BIOS: قراءة المعادلة"),
 INSHORT([("Principle: **triolein → monoglycerides + fatty acids** (pancreatic lipase).", "المبدأ: **ترايولين ← أحادي الغليسيريدات + أحماض دهنية** (لايبيز البنكرياس)."),
          ("Sample: **non-hemolysed serum**; 1 ml reagent + **0.04 ml**; 4 min → A1, 5 min later → A2.", "العيّنة: **مصل غير متحلّل**؛ 1 مل كاشف + **0.04 مل**؛ 4 دقائق ← `A1`، وبعد 5 دقائق ← `A2`."),
          ("Lipase U/L = **ΔAt / ΔAc × conc**.", "اللايبيز `U/L` = **`ΔAt / ΔAc × conc`**.")]),
] + TERMS([
 ("Amylase", "الأميليز / إنزيم النشا"),
 ("Lipase", "اللايبيز / الليباز / إنزيم الدهون"),
 ("Hydrolysis", "التحلّل المائي / الحلمأة"),
 ("Starch", "النشا"),
 ("Maltase", "المالتيز"),
 ("Acute pancreatitis", "التهاب البنكرياس الحادّ"),
 ("Peptic ulcer", "القرحة الهضمية"),
 ("Somogyi unit", "وحدة سوموجي"),
 ("Triolein", "الترايولين / ثلاثي أوليات الغليسيرول"),
 ("Monoglyceride", "أحادي الغليسيريد"),
 ("Calibrator", "المعايِر / محلول المعايرة"),
 ("Hemolysis", "تحلّل الدم / انحلال الكريات الحمر"),
 ("Sensitivity / specificity", "الحساسية / النوعية"),
 ("Cystic fibrosis", "التليّف الكيسي"),
])

# ───────────────────────── questions (BIOS — the file has none)
mcq = [
 {"topic_en": "Amylase", "topic_ar": "الأميليز"},
 Q("Amylase catalyses the hydrolysis of:", "يحفّز الأميليز التحلّل المائي لـ:", O(("Starch into sugars", "النشا إلى سكّريات"), ("Fats into fatty acids", "الدهون إلى أحماض دهنية"), ("Proteins into amino acids", "البروتينات إلى أحماض أمينية"), ("Phosphate esters", "إسترات الفوسفات")), "a"),
 Q("Which is NOT listed as a main source of amylase?", "أيّ مما يلي ليس من المصادر الرئيسية للأميليز؟", O(("Salivary glands", "الغدد اللعابية"), ("Kidney", "الكلية"), ("Pancreas", "البنكرياس"), ("Liver", "الكبد")), "b"),
 Q("Much lower amylase activities are present in:", "توجد فعاليات أقلّ بكثير للأميليز في:", O(("Pancreas", "البنكرياس"), ("Salivary glands", "الغدد اللعابية"), ("Ovaries, intestines and skeletal muscle", "المبيضين والأمعاء والعضلات الهيكلية"), ("Liver only", "الكبد فقط")), "c"),
 Q("α-amylase is found in:", "يوجد `α`-أميليز في:", O(("Plants only", "النبات فقط"), ("Bacteria only", "البكتيريا فقط"), ("Fungi", "الفطريات"), ("Animal and human tissue", "أنسجة الحيوان والإنسان")), "d"),
 Q("The normal range of serum amylase in the sheet is:", "المدى الطبيعي لأميليز المصل في الورقة:", O(("40 to 140 U/L", "40 إلى 140 `U/L`"), ("10 to 40 U/L", "10 إلى 40 `U/L`"), ("200 to 400 U/L", "200 إلى 400 `U/L`"), ("18 to 180 U/L", "18 إلى 180 `U/L`")), "a"),
 Q("Which condition is listed as clinically significant for amylase?", "أيّ حالة مذكورة ضمن الأهمية السريرية للأميليز؟", O(("Myocardial infarction", "احتشاء القلب"), ("Acute pancreatitis", "التهاب البنكرياس الحادّ"), ("Osteoporosis", "هشاشة العظام"), ("Anemia", "فقر الدم")), "b"),
 Q("The Somogyi unit is measured over a reaction of:", "تُقاس وحدة سوموجي خلال تفاعل مدّته:", O(("5 min at 25 °C", "5 دقائق عند 25 °م"), ("60 min at 4 °C", "60 دقيقة عند 4 °م"), ("30 min at 37 °C and pH 7", "30 دقيقة عند 37 °م و`pH 7`"), ("10 min at pH 9", "10 دقائق عند `pH 9`")), "c"),
 Q("For the amylase procedure, the sheet says:", "بخصوص طريقة عمل الأميليز تقول الورقة:", O(("Use 1 ml reagent and 0.04 ml sample", "استعمل 1 مل كاشف و0.04 مل عيّنة"), ("Incubate for 30 min", "احضن 30 دقيقة"), ("No procedure is needed", "لا حاجة لطريقة عمل"), ("Read the procedure in the kit", "اقرأ طريقة العمل في العُدّة")), "d"),
 {"topic_en": "Lipase", "topic_ar": "اللايبيز"},
 Q("Lipase breaks down fats into:", "يكسر اللايبيز الدهون إلى:", O(("Fatty acids and glycerol", "أحماض دهنية وغليسيرول"), ("Glucose", "غلوكوز"), ("Amino acids", "أحماض أمينية"), ("Maltose", "مالتوز")), "a"),
 Q("Lipase is produced in the:", "يُنتَج اللايبيز في:", O(("Kidney, bone and placenta", "الكلية والعظم والمشيمة"), ("Pancreas, mouth and stomach", "البنكرياس والفم والمعدة"), ("Liver only", "الكبد فقط"), ("Skeletal muscle", "العضلات الهيكلية")), "b"),
 Q("People who may not have enough lipase include those with:", "من قد لا يملكون ما يكفي من اللايبيز المصابون بـ:", O(("Hypertension", "ارتفاع ضغط الدم"), ("Diabetes insipidus", "السكّري الكاذب"), ("Cystic fibrosis, Crohn disease and celiac disease", "التليّف الكيسي وداء كرون والسيلياك"), ("Gout", "النقرس")), "c"),
 Q("After pancreatic damage, lipase remains elevated for:", "بعد تضرّر البنكرياس يبقى اللايبيز مرتفعًا لمدّة:", O(("A few hours", "بضع ساعات"), ("1 day", "يوم واحد"), ("3 months", "3 أشهر"), ("7 to 10 days", "7 إلى 10 أيام")), "d"),
 Q("Compared with amylase, the lipase assay provides:", "مقارنةً بالأميليز، يعطي فحص اللايبيز:", O(("Better sensitivity and specificity", "حساسية ونوعية أفضل"), ("Lower specificity", "نوعية أقلّ"), ("No diagnostic value", "لا قيمة تشخيصية"), ("Results only in children", "نتائج عند الأطفال فقط")), "a"),
 Q("The percentage of acute pancreatitis patients with elevated amylase and lipase is:", "نسبة مرضى التهاب البنكرياس الحادّ الذين يرتفع لديهم الأميليز واللايبيز:", O(("10%", "10%"), ("80%", "80%"), ("50%", "50%"), ("100%", "100%")), "b"),
 Q("The normal lipase in elderly persons (>60 years) is:", "اللايبيز الطبيعي عند كبار السنّ (>60 سنة):", O(("10–140 U/L", "10–140 `U/L`"), ("40–140 U/L", "40–140 `U/L`"), ("18–180 U/L", "18–180 `U/L`"), ("0–10 U/L", "0–10 `U/L`")), "c"),
 Q("The substrate in the lipase method is:", "الركيزة في طريقة اللايبيز:", O(("Starch", "النشا"), ("p-nitrophenyl phosphate", "بارا-نيتروفينيل فوسفات"), ("Glucose", "الغلوكوز"), ("Triolein", "الترايولين")), "d"),
 Q("The sample for lipase must be:", "عيّنة اللايبيز يجب أن تكون:", O(("Serum free from hemolysis", "مصلًا خاليًا من تحلّل الدم"), ("Whole blood with EDTA", "دمًا كاملًا بـ`EDTA`"), ("Urine", "إدرارًا"), ("Hemolysed plasma", "بلازما متحلّلة")), "a"),
 Q("In the lipase procedure, the volume of sample added is:", "في طريقة اللايبيز، حجم العيّنة المضاف:", O(("1 ml", "1 مل"), ("0.04 ml", "0.04 مل"), ("0.4 ml", "0.4 مل"), ("2 ml", "2 مل")), "b"),
 Q("After mixing, the tubes are incubated at room temperature for:", "بعد الخلط تُحضن الأنابيب بحرارة الغرفة لمدّة:", O(("30 min", "30 دقيقة"), ("1 min", "دقيقة واحدة"), ("4 min, then read A1", "4 دقائق ثم اقرأ `A1`"), ("60 min", "60 دقيقة")), "c"),
 Q("Lipase (U/L) is calculated as:", "يُحسب اللايبيز (`U/L`) بـ:", O(("ΔAc / ΔAt × conc", "`ΔAc / ΔAt × conc`"), ("At × Ac", "`At × Ac`"), ("conc / ΔAt", "`conc / ΔAt`"), ("ΔAt / ΔAc × conc", "`ΔAt / ΔAc × conc`")), "d"),
 {"topic_en": "Picture questions", "topic_ar": "أسئلة الصور"},
 Q("In this figure, the enzyme that converts starch to maltose is:", "في هذا الشكل، الإنزيم الذي يحوّل النشا إلى مالتوز هو:", O(("Amylase", "الأميليز"), ("Maltase", "المالتيز"), ("Lipase", "اللايبيز"), ("ALP", "`ALP`")), "a", img="assets/carbohydrate-digestion.png", img_h="30mm"),
 Q("The end product in this figure is:", "الناتج النهائي في هذا الشكل:", O(("Starch (polysaccharide)", "النشا (سكّر متعدّد)"), ("Glucose (monosaccharide)", "الغلوكوز (سكّر أحادي)"), ("Maltose (disaccharide)", "المالتوز (سكّر ثنائي)"), ("Fatty acids", "أحماض دهنية")), "b", img="assets/carbohydrate-digestion.png", img_h="30mm"),
]
mcq = balance(mcq, 14)
tf = [
 TF("Amylase is produced by the salivary glands, pancreas and liver.", "يُنتَج الأميليز من الغدد اللعابية والبنكرياس والكبد.", "T"),
 TF("Inflammation of the pancreas or salivary glands lowers blood amylase.", "التهاب البنكرياس أو الغدد اللعابية يخفض أميليز الدم.", "F"),
 TF("β-amylase is found in plants and bacteria.", "يوجد `β`-أميليز في النبات والبكتيريا.", "T"),
 TF("Carcinoma of the head of the pancreas is a clinical significance of amylase.", "سرطان رأس البنكرياس من الأهمية السريرية للأميليز.", "T"),
 TF("The triolein reaction in the sheet is the true principle of amylase.", "تفاعل الترايولين في الورقة هو المبدأ الحقيقي للأميليز.", "F"),
 TF("Lipase helps absorb fats in the intestines.", "يساعد اللايبيز على امتصاص الدهون في الأمعاء.", "T"),
 TF("Lipase disappears from the blood before amylase.", "يختفي اللايبيز من الدم قبل الأميليز.", "F"),
 TF("Amylase and lipase help differentiate pancreatitis from other acute abdominal disorders.", "يساعد الأميليز واللايبيز على تمييز التهاب البنكرياس عن الاضطرابات البطنية الحادّة الأخرى.", "T"),
 TF("Lipase is best used alone without amylase.", "يُستعمل اللايبيز أفضل استعمال وحده دون الأميليز.", "F"),
 TF("Hemolysed serum is acceptable for the lipase test.", "المصل المتحلّل مقبول لفحص اللايبيز.", "F"),
 TF("In the lipase method, the calibrator tube receives 0.04 ml calibrator.", "في طريقة اللايبيز يُضاف 0.04 مل معايِر إلى أنبوب المعايِر.", "T"),
 TF("A2 is read 5 min after A1.", "يُقرأ `A2` بعد 5 دقائق من `A1`.", "T"),
]
traps = [
 TR("Amylase or lipase reaction?", "تفاعل الأميليز أم اللايبيز؟", "Amylase: starch → sugars. Lipase: fats/triolein → fatty acids + glycerol (monoglycerides). The triolein equation under 'amylase' in the sheet is really the lipase reaction.",
    "الأميليز: نشا ← سكّريات. واللايبيز: دهون/ترايولين ← أحماض دهنية + غليسيرول (أحادي الغليسيريدات). ومعادلة الترايولين تحت «الأميليز» في الورقة هي فعليًا تفاعل اللايبيز."),
 TR("Which stays high longer?", "أيّهما يبقى مرتفعًا أطول؟", "Lipase appears with (or slightly after) amylase but stays elevated much longer — 7 to 10 days.",
    "اللايبيز يظهر مع الأميليز (أو بعده بقليل) لكنه يبقى مرتفعًا مدّة أطول بكثير — 7 إلى 10 أيام."),
 TR("α or β?", "`α` أم `β`؟", "α-amylase = animal and human tissue; β-amylase = plant and bacteria.",
    "`α`-أميليز = أنسجة الحيوان والإنسان؛ و`β`-أميليز = النبات والبكتيريا."),
 TR("Normal values", "القيم الطبيعية", "Amylase 40–140 U/L; lipase adults 10–140 U/L, elderly (>60) 18–180 U/L.",
    "الأميليز 40–140 `U/L`؛ واللايبيز للبالغين 10–140 `U/L`، ولكبار السنّ (>60) 18–180 `U/L`."),
 TR("Sources", "المصادر", "Amylase: salivary glands, pancreas, liver. Lipase: pancreas, mouth, stomach.",
    "الأميليز: الغدد اللعابية، البنكرياس، الكبد. واللايبيز: البنكرياس، الفم، المعدة."),
 TR("ΔAt / ΔAc, not the reverse", "`ΔAt / ΔAc` وليس العكس", "Lipase U/L = ΔAt (test) ÷ ΔAc (calibrator) × calibrator concentration.",
    "اللايبيز `U/L` = `ΔAt` (الفحص) ÷ `ΔAc` (المعايِر) × تركيز المعايِر."),
]
important = [
 IM("Define amylase and give its sources and types.", "عرّف الأميليز واذكر مصادره وأنواعه.",
    "An enzyme that catalyses the hydrolysis of starch into sugars; produced by the salivary glands, pancreas and liver (much lower in ovaries, intestines, skeletal muscle). Types: α-amylase (animal and human tissue) and β-amylase (plant and bacteria).",
    "إنزيم يحفّز تحلّل النشا مائيًا إلى سكّريات؛ يُنتَج من الغدد اللعابية والبنكرياس والكبد (وأقلّ بكثير في المبيضين والأمعاء والعضلات الهيكلية). أنواعه: `α`-أميليز (أنسجة الحيوان والإنسان) و`β`-أميليز (النبات والبكتيريا)."),
 IM("List the clinical significance of serum amylase.", "عدّد الأهمية السريرية لأميليز المصل.",
    "Acute pancreatitis; carcinoma of the head of the pancreas; peptic ulcers; salivary gland disorder; tumor of salivary glands; intestinal obstruction.",
    "التهاب البنكرياس الحادّ؛ سرطان رأس البنكرياس؛ القرحة الهضمية؛ اضطراب الغدد اللعابية؛ ورم الغدد اللعابية؛ انسداد الأمعاء."),
 IM("Define the Somogyi unit.", "عرّف وحدة سوموجي.",
    "A unit of amylase activity: the amount of enzyme able to liberate sugars with a reducing value equivalent to 1 g (textbooks: 1 mg) of glucose in a 30 min reaction at 37 °C and pH 7.",
    "وحدة لفعالية الأميليز: كمّية الإنزيم القادرة على تحرير سكّريات قيمتها الاختزالية تعادل 1 غم (في الكتب: 1 ملغم) من الغلوكوز خلال تفاعل 30 دقيقة عند 37 °م و`pH 7`."),
 IM("Compare amylase and lipase in acute pancreatitis.", "قارن بين الأميليز واللايبيز في التهاب البنكرياس الحادّ.",
    "Both rise in about 80% of patients; lipase appears at the same time or slightly later but remains elevated much longer (7–10 days) and has better sensitivity and specificity; it is best used together with amylase.",
    "يرتفع الاثنان في نحو 80% من المرضى؛ ويظهر اللايبيز في الوقت نفسه أو بعده بقليل لكنه يبقى مرتفعًا مدّة أطول بكثير (7–10 أيام)، وحساسيته ونوعيته أفضل؛ ويُستعمل أفضل استعمال مع الأميليز."),
 IM("Give the principle, sample and procedure of the serum lipase test.", "اذكر مبدأ فحص اللايبيز في المصل وعيّنته وطريقة عمله.",
    "Principle: pancreatic lipase hydrolyses triolein to monoglycerides and fatty acids. Sample: non-hemolysed serum. Procedure: C = 1 ml reagent + 0.04 ml calibrator; T = 1 ml reagent + 0.04 ml sample; mix, incubate 4 min at room temperature, read A1, read A2 after 5 min.",
    "المبدأ: لايبيز البنكرياس يحلّل الترايولين مائيًا إلى أحادي الغليسيريدات وأحماض دهنية. العيّنة: مصل غير متحلّل. الطريقة: `C` = 1 مل كاشف + 0.04 مل معايِر؛ `T` = 1 مل كاشف + 0.04 مل عيّنة؛ اخلط واحضن 4 دقائق بحرارة الغرفة واقرأ `A1`، ثم اقرأ `A2` بعد 5 دقائق."),
 IM("How is serum lipase calculated? Solve: ΔAt = 0.045, ΔAc = 0.090, calibrator = 160 U/L.", "كيف يُحسب اللايبيز في المصل؟ حلّ: `ΔAt = 0.045`، `ΔAc = 0.090`، المعايِر = 160 `U/L`.",
    "Lipase U/L = ΔAt / ΔAc × conc = 0.045 / 0.090 × 160 = 0.5 × 160 = 80 U/L (within the adult normal range 10–140 U/L).",
    "اللايبيز `U/L` = `ΔAt / ΔAc × conc` = `0.045 / 0.090 × 160 = 0.5 × 160 = 80 U/L` (ضمن المدى الطبيعي للبالغين 10–140 `U/L`)."),
]
meta = {"subject_en": "Clinical Enzymology", "subject_ar": "الإنزيمات السريرية", "short_ar": "انزيمات سريرية", "instructor": "د. بارق و د. هشام",
        "unit_en": "Lab 4", "unit_ar": "العملي 4", "unit_label": "LAB", "unit_no": "4", "title_en": "Serum Amylase and Serum Lipase",
        "title_ar": "الأميليز واللايبيز في المصل", "kind": "Laboratories — عملي", "stage": "The fourth stage — الرابعة"}
blocks, mcq, tf, traps, important = ltr_all(blocks), ltr_all(mcq), ltr_all(tf), ltr_all(traps), ltr_all(important)
save(FOLDER, meta, blocks, mcq, tf, traps, important)
fit(FOLDER, min_gap=0.08)   # no gaps (fill2 >= 80%), incl. small ones before a heading

```
