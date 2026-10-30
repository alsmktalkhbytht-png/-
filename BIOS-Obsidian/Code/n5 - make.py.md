---
source: BIOS-Obsidian/tools/scripts/n5/make.py
handouts: [hematology-lab1-blood-collection]
saved: 2026-10-30
tags: [bios, code]
---
# n5/make.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#hematology-lab1-blood-collection|hematology-lab1-blood-collection]]

```python
import json
from collections import Counter
def C(en, ar, **k): return dict(t="card", en=en, ar=ar, **k)
def R(en, ar): return dict(t="rule", en=en, ar=ar)
def SEC(en, ar): return dict(t="section", en=en, ar=ar)
def H2(en, ar): return dict(t="h2", en=en, ar=ar)
def L(en_items, ar_items, en="", ar="", **k): return dict(t="card", en=en, ar=ar, list_en=en_items, list_ar=ar_items, **k)
def F(src, en, ar, **k): return dict(t="figure", src="assets/" + src, en=en, ar=ar, **k)
def FF(*items): return dict(t="figures", items=[dict(src="assets/" + s, en=e, ar=a, h=h, fit="contain") for s, e, a, h in items])
def N(en, ar, label=None):
    b = dict(t="note", en=en, ar=ar)
    if label: b["label"] = label
    return b
def FLOW(pairs, **k): return dict(t="flow", steps=[{"en": e, "ar": a} for e, a in pairs], **k)

blocks = [
 SEC("Blood Collection", "جمع الدم"),
 C("**Blood collection** is the process of obtaining a blood sample for **laboratory testing, diagnosis, and monitoring**.",
   "**جمع الدم** هو عملية الحصول على عيّنة دم لأغراض **الفحص المختبري والتشخيص والمتابعة**."),
 L(["**Laboratory testing** – such as hematological, biochemical, serological, immunological, and microbiological tests.",
    "**Blood donation** – to provide blood and blood components for transfusion.",
    "**Monitoring** – to follow the patient’s condition and response to treatment."],
   ["**الفحص المختبري** – مثل الفحوص الدموية، والكيميائية الحيوية، والمصلية، والمناعية، والأحياء المجهرية.",
    "**التبرّع بالدم** – لتوفير الدم ومكوّناته لنقلها للمرضى.",
    "**المتابعة** – لمتابعة حالة المريض واستجابته للعلاج."],
   en="**Purposes of Blood Collection** — Blood is collected mainly for:", ar="**أغراض جمع الدم** — يُجمع الدم أساسًا من أجل:"),

 SEC("Types of blood collection", "أنواع جمع الدم"),
 L(["Most commonly used specimen.", "Suitable for most routine laboratory tests.", "Provides a relatively large volume of blood."],
   ["العيّنة الأكثر استخدامًا.", "مناسبة لمعظم الفحوص المختبرية الروتينية.", "توفّر حجمًا كبيرًا نسبيًا من الدم."],
   en="**1. Venous Blood**", ar="**1. الدم الوريدي**"),
 L(["Obtained by **skin puncture**.", "Used when a **small volume** is required.", "Common in **infants** and **point-of-care testing**."],
   ["يُحصل عليه **بوخز الجلد**.", "يُستخدم عندما يكون المطلوب **حجمًا صغيرًا**.", "شائع عند **الرضّع** وفي **الفحوص بجانب المريض**."],
   en="**2. Capillary Blood**", ar="**2. الدم الشعيري**"),
 L(["Obtained directly from an **artery**.", "Mainly used for **Arterial Blood Gas (ABG)** analysis.", "Provides information about **respiratory and acid–base status**."],
   ["يُحصل عليه مباشرة من **شريان**.", "يُستخدم أساسًا لتحليل **غازات الدم الشرياني** (`ABG`).", "يعطي معلومات عن **الحالة التنفسية والتوازن الحامضي–القاعدي**."],
   en="**3. Arterial Blood**", ar="**3. الدم الشرياني**"),
 F("types-of-collection.jpg", "Types of blood collection: venous, capillary and arterial", "أنواع جمع الدم: الوريدي والشعيري والشرياني", h="80mm"),

 SEC("Materials and tools", "المواد والأدوات"),
 dict(t="table", head=["Tool (from the slide)", "الأداة"], ar_cols=[1], key_cols=[0], numbered=False,
      rows=[["Syringes & needles", "المحاقن والإبر"], ["Tourniquet", "الرباط الضاغط (التورنيكه)"], ["Test-tubes", "أنابيب الفحص"],
            ["70% isopropanol", "كحول الأيزوبروبانول 70%"], ["Cotton", "القطن"], ["Marker pen", "قلم التأشير"], ["Gloves", "القفّازات"]]),
 F("materials-and-tools.jpg", "Materials and tools for blood collection", "المواد والأدوات المستخدمة في جمع الدم", h="62mm"),
 F("venipuncture-systems.jpg", "Venipuncture systems: vacuum (evacuated tube system), butterfly (winged) and disposable syringe",
   "أنظمة سحب الدم الوريدي: النظام المفرَّغ (أنابيب مفرّغة من الهواء)، والفراشة (المجنّحة)، والمحقنة ذات الاستعمال الواحد", h="74mm"),

 SEC("Venipuncture: Equipment & Sites", "سحب الدم الوريدي: الأدوات والمواقع"),
 C("**Venous Blood Collection** — Most common method of blood collection.", "**جمع الدم الوريدي** — الطريقة الأكثر شيوعًا لجمع الدم."),
 L(["**Median cubital vein → preferred**", "Cephalic vein", "Basilic vein."],
   ["**الوريد المرفقي الناصف ← المفضّل**", "الوريد الرأسي", "الوريد القاعدي."],
   en="**Common Venipuncture Sites**", ar="**مواقع سحب الدم الوريدي الشائعة**"),
 FF(("antecubital-veins.jpg", "Antecubital veins: cephalic (lateral), median cubital (preferred), basilic (medial)", "أوردة الحفرة المرفقية: الرأسي (الجانبي)، والمرفقي الناصف (المفضّل)، والقاعدي (الإنسي)", "60mm"),
    ("venous-sites.jpg", "Common venous blood collection sites (including dorsal hand and saphenous veins)", "مواقع جمع الدم الوريدي الشائعة (ومنها أوردة ظهر اليد والأوردة الصافنة)", "60mm")),
 C("**Basic steps:**", "**الخطوات الأساسية:**"),
 FLOW([("Patient identification", "تعريف المريض"), ("Tourniquet", "الرباط الضاغط"), ("Disinfection (70% alcohol)", "التعقيم (كحول 70%)"),
       ("Blood collection", "سحب الدم"), ("Pressure", "الضغط"), ("Labeling", "وضع الملصق")]),

 SEC("Arterial Blood Collection", "جمع الدم الشرياني"),
 C("Blood is collected directly from an **artery**, mainly for **Arterial Blood Gas (ABG)** analysis.",
   "يُجمع الدم مباشرة من **شريان**، أساسًا لتحليل **غازات الدم الشرياني** (`ABG`)."),
 L(["**Radial artery → preferred**", "Brachial artery", "Femoral artery"], ["**الشريان الكعبري ← المفضّل**", "الشريان العضدي", "الشريان الفخذي"],
   en="**Sites:**", ar="**المواقع:**"),
 C("**ABG measures:** pH – PaO₂ – PaCO₂ – HCO₃⁻ – O₂ saturation", "**يقيس تحليل غازات الدم:** `pH – PaO₂ – PaCO₂ – HCO₃⁻` – تشبّع الأوكسجين"),
 C("It evaluates **oxygenation, ventilation, and acid–base balance**.", "وهو يقيّم **الأكسجة والتهوية والتوازن الحامضي–القاعدي**."),
 FF(("arterial-sampling.jpg", "Arterial blood sampling (radial artery, with the Allen test)", "سحب الدم الشرياني (الشريان الكعبري، مع اختبار ألن)", "56mm"),
    ("arterial-sites.jpg", "Common arterial blood sampling sites", "مواقع سحب الدم الشرياني الشائعة", "56mm")),
 L(["Use a **heparinized syringe**.", "Clean the puncture site.", "Collect arterial blood.", "**Remove air bubbles.**", "Apply **firm pressure** after collection.", "Send the sample **promptly** for analysis."],
   ["استخدم **محقنة مُهَبرنة** (تحتوي هيبارين).", "نظّف موقع الوخز.", "اسحب الدم الشرياني.", "**أزل فقاعات الهواء.**", "اضغط **ضغطًا قويًا** بعد السحب.", "أرسل العيّنة للتحليل **فورًا**."],
   en="**Arterial Blood Collection: Basic Steps**", ar="**جمع الدم الشرياني: الخطوات الأساسية**"),

 SEC("Capillary Blood Collection", "جمع الدم الشعيري"),
 C("Capillary blood is obtained by **skin puncture** using a **sterile lancet**.", "يُحصل على الدم الشعيري **بوخز الجلد** باستخدام **مِشرط وخز معقّم** (`lancet`)."),
 L(["**Adults/older children** → side of the middle or ring finger , earlobe .", "**Infants** → medial or lateral plantar surface of the heel."],
   ["**البالغون/الأطفال الأكبر** ← جانب الإصبع الوسطى أو البنصر، وشحمة الأذن.", "**الرضّع** ← السطح الأخمصي الإنسي أو الوحشي للكعب."],
   en="**Collection Sites**", ar="**مواقع الجمع**"),
 FF(("capillary-sites.jpg", "Capillary blood collection sites: earlobe, heel, fingertip", "مواقع جمع الدم الشعيري: شحمة الأذن، الكعب، طرف الإصبع", "50mm"),
    ("capillary-collection.jpg", "Preferred sites on the heel and finger — avoid the central area", "المواقع المفضّلة على الكعب والإصبع — تجنّب المنطقة الوسطى", "50mm")),
 L(["Allow alcohol to dry.", "**Wipe away the first drop.**", "Avoid excessive squeezing.", "Allow blood to flow freely."],
   ["اترك الكحول ليجفّ.", "**امسح القطرة الأولى.**", "تجنّب العصر المفرط.", "دع الدم ينساب بحرّية."],
   en="**Precautions**", ar="**الاحتياطات**"),
 N("Excessive squeezing may cause **hemolysis** and **contamination with tissue fluid**.", "قد يسبّب العصر المفرط **تحلّل الدم** و**التلوّث بسائل الأنسجة**.", label=["Why", "لماذا"]),

 SEC("Blood Collection Tubes", "أنابيب جمع الدم"),
 dict(t="table", head=["Additive", "Main Use", "المادة المضافة — الاستخدام الرئيس"], ar_cols=[2], key_cols=[0],
      rows=[["EDTA", "CBC, blood film", "`EDTA` — صورة الدم الكاملة (`CBC`) والمسحة الدموية"],
            ["Sodium citrate", "Coagulation tests", "سترات الصوديوم — فحوص التخثّر"],
            ["Heparin", "Blood gases / some chemistry tests", "الهيبارين — غازات الدم / بعض الفحوص الكيميائية"],
            ["Fluoride/Oxalate", "Glucose", "الفلورايد/الأوكزالات — الكلوكوز"],
            ["Plain tube", "Serum", "الأنبوب العادي — المصل"]]),
 F("collection-tubes.jpg", "Blood collection tubes: EDTA, sodium citrate, plain, SST, heparin, fluoride/oxalate", "أنابيب جمع الدم: EDTA، سترات الصوديوم، العادي، أنبوب فصل المصل، الهيبارين، الفلورايد/الأوكزالات", h="70mm"),

 SEC("Serum vs. Plasma", "المصل مقابل البلازما"),
 dict(t="table", head=["", "Plasma", "Serum", "الترجمة"], ar_cols=[3], key_cols=[0],
      rows=[["Source", "From anticoagulated blood.", "Obtained after blood clotting.", "**البلازما**: من دم مُضاف إليه مانع تخثّر. **المصل**: بعد تخثّر الدم."],
            ["Fibrinogen", "Contains fibrinogen.", "Does not contain fibrinogen.", "**البلازما** تحتوي الفايبرينوجين، و**المصل** لا يحتويه."]]),
 FLOW([("Blood + anticoagulant", "دم + مانع تخثّر"), ("Plasma", "بلازما")]),
 FLOW([("Blood + clotting", "دم + تخثّر"), ("Serum", "مصل")]),
 F("serum-vs-plasma.jpg", "Serum and plasma: how each is obtained and what it contains", "المصل والبلازما: كيف يُحصل على كلٍّ منهما وما يحتويه", h="76mm"),

 SEC("Hemolysis", "تحلّل الدم"),
 C("**Hemolysis:** rupture of RBCs with release of **hemoglobin and intracellular contents** into serum/plasma.",
   "**تحلّل الدم** (`Hemolysis`): تمزّق كريات الدم الحمر مع تحرّر **الهيموغلوبين والمحتويات داخل الخلوية** إلى المصل/البلازما."),
 L(["Small needle", "Forceful aspiration", "Vigorous shaking"], ["الإبرة الصغيرة", "السحب بقوة", "الرجّ العنيف"], en="**Common causes:**", ar="**الأسباب الشائعة:**"),
 C(["Hemolyzed samples may appear **pink or red**.", "Hemolysis may cause **incorrect laboratory results**."],
   ["قد تظهر العيّنات المتحلّلة **وردية أو حمراء**.", "قد يسبّب تحلّل الدم **نتائج مختبرية غير صحيحة**."]),
 L(["Use appropriate needle size.", "Avoid forceful aspiration.", "Handle and mix tubes gently."],
   ["استخدم إبرة بحجم مناسب.", "تجنّب السحب بقوة.", "تعامل مع الأنابيب واخلطها بلطف."], en="**Prevention:**", ar="**الوقاية:**"),
 dict(t="side", blocks=[
   dict(t="table", head=["Tube", "Serum (from the figure)", "المصل"], ar_cols=[2], key_cols=[0],
        rows=[["1, 4 and 7", "Normal serum", "مصل طبيعي"], ["2 and 3", "Icteric serum (Hyperbilirubinemia)", "مصل يرقاني (فرط البيليروبين)"],
              ["5", "Lipemic serum", "مصل دهني"], ["6", "Hemolyzed serum", "مصل متحلّل"]])],
   figure=dict(src="assets/normal-vs-pathology-serum.jpg", en="Normal vs. pathology serum", ar="المصل الطبيعي مقابل المرضي")),

 SEC("Important Precautions", "احتياطات مهمة"),
 dict(t="table", head=["", "Precaution (from the slide)", "الاحتياط"], ar_cols=[2], key_cols=[1], numbered=True, widths=["10mm", "", ""],
      rows=[["1", "Hand hygiene", "نظافة اليدين"], ["2", "Use PPE", "ارتداء معدّات الوقاية الشخصية"], ["3", "Check patient identification", "التحقّق من هوية المريض"],
            ["4", "Explain the procedure and obtain consent", "شرح الإجراء وأخذ الموافقة"], ["5", "Use the correct collection site", "استخدام موقع الجمع الصحيح"],
            ["6", "Use appropriate equipment", "استخدام الأدوات المناسبة"], ["7", "Avoid prolonged tourniquet time (< 1 minute)", "تجنّب إطالة وقت الرباط الضاغط (أقل من دقيقة)"],
            ["8", "Avoid hemolysis", "تجنّب تحلّل الدم"], ["9", "Order of draw", "ترتيب سحب الأنابيب"], ["10", "Proper disposal of sharps", "التخلّص السليم من الأدوات الحادة"],
            ["11", "Apply pressure and bandage", "الضغط ووضع الضمادة"], ["12", "Dispose of contaminated materials properly", "التخلّص السليم من المواد الملوّثة"]]),
 F("important-precautions.jpg", "Important precautions during blood collection", "احتياطات مهمة أثناء جمع الدم", h="84mm"),
 N("**Remember:** Proper collection → Reliable laboratory results", "**تذكّر:** الجمع السليم ← نتائج مختبرية موثوقة", label=["Remember", "تذكّر"]),
]

def Q(en, ar, opts, ans, **k):
    return dict(en=en, ar=ar, options=[list(o) for o in opts], answer=ans, **k)

mcq = [
 {"topic_en": "Purposes and types", "topic_ar": "الأغراض والأنواع"},
 Q("Blood is collected mainly for all of the following EXCEPT:", "يُجمع الدم أساسًا لكل مما يأتي عدا:", [("Laboratory testing", "الفحص المختبري"), ("Blood donation", "التبرّع بالدم"), ("Monitoring", "المتابعة"), ("Sterilization", "التعقيم")], "d"),
 Q("The most commonly used blood specimen is:", "العيّنة الدموية الأكثر استخدامًا هي:", [("Venous blood", "الدم الوريدي"), ("Capillary blood", "الدم الشعيري"), ("Arterial blood", "الدم الشرياني"), ("Cord blood", "دم الحبل السري")], "a"),
 Q("Capillary blood is obtained by:", "يُحصل على الدم الشعيري بـ:", [("Venipuncture", "بزل الوريد"), ("Skin puncture", "وخز الجلد"), ("Arterial puncture", "بزل الشريان"), ("Catheter", "قسطرة")], "b"),
 Q("Capillary blood is common in:", "الدم الشعيري شائع عند:", [("Blood donors", "المتبرّعين بالدم"), ("ABG analysis", "تحليل غازات الدم"), ("Infants and point-of-care testing", "الرضّع والفحوص بجانب المريض"), ("Coagulation studies only", "دراسات التخثّر فقط")], "c"),
 Q("Arterial blood is mainly used for:", "يُستخدم الدم الشرياني أساسًا لـ:", [("CBC", "صورة الدم الكاملة"), ("Blood film", "المسحة الدموية"), ("Glucose", "الكلوكوز"), ("Arterial blood gas (ABG) analysis", "تحليل غازات الدم الشرياني")], "d"),
 {"topic_en": "Venous, arterial and capillary collection", "topic_ar": "الجمع الوريدي والشرياني والشعيري"},
 Q("The preferred vein for venipuncture is the:", "الوريد المفضّل لسحب الدم هو:", [("Cephalic vein", "الوريد الرأسي"), ("Median cubital vein", "الوريد المرفقي الناصف"), ("Basilic vein", "الوريد القاعدي"), ("Femoral vein", "الوريد الفخذي")], "b"),
 Q("Disinfection before venipuncture uses:", "يُستخدم في التعقيم قبل سحب الدم الوريدي:", [("70% alcohol", "كحول 70%"), ("Distilled water", "الماء المقطّر"), ("Saline", "المحلول الملحي"), ("EDTA", "EDTA")], "a"),
 Q("The last basic step of venous collection is:", "الخطوة الأساسية الأخيرة في الجمع الوريدي هي:", [("Tourniquet", "الرباط الضاغط"), ("Disinfection", "التعقيم"), ("Labeling", "وضع الملصق"), ("Patient identification", "تعريف المريض")], "c"),
 Q("The preferred artery for ABG sampling is the:", "الشريان المفضّل لسحب غازات الدم هو:", [("Femoral artery", "الشريان الفخذي"), ("Brachial artery", "الشريان العضدي"), ("Carotid artery", "الشريان السباتي"), ("Radial artery", "الشريان الكعبري")], "d"),
 Q("Which is NOT measured by ABG analysis?", "أي مما يأتي لا يقيسه تحليل غازات الدم؟", [("pH", "pH"), ("PaO₂", "PaO₂"), ("Hemoglobin electrophoresis", "الترحيل الكهربائي للهيموغلوبين"), ("HCO₃⁻", "HCO₃⁻")], "c"),
 Q("ABG evaluates oxygenation, ventilation and:", "يقيّم تحليل غازات الدم الأكسجة والتهوية و:", [("Acid–base balance", "التوازن الحامضي–القاعدي"), ("Coagulation", "التخثّر"), ("Blood groups", "فصائل الدم"), ("Glucose level", "مستوى الكلوكوز")], "a"),
 Q("Arterial blood is collected using a:", "يُجمع الدم الشرياني باستخدام:", [("EDTA tube", "أنبوب EDTA"), ("Heparinized syringe", "محقنة مُهَبرنة"), ("Plain tube", "أنبوب عادي"), ("Citrate tube", "أنبوب سترات")], "b"),
 Q("After collecting arterial blood you should:", "بعد سحب الدم الشرياني يجب:", [("Shake the syringe vigorously", "رجّ المحقنة بقوة"), ("Leave air bubbles", "ترك فقاعات الهواء"), ("Remove air bubbles and send promptly", "إزالة فقاعات الهواء والإرسال فورًا"), ("Store it for a day", "حفظها يومًا")], "c"),
 Q("In infants, capillary blood is collected from the:", "عند الرضّع يُجمع الدم الشعيري من:", [("Earlobe", "شحمة الأذن"), ("Middle finger", "الإصبع الوسطى"), ("Center of the heel", "وسط الكعب"), ("Medial or lateral plantar surface of the heel", "السطح الأخمصي الإنسي أو الوحشي للكعب")], "d"),
 Q("In adults, capillary blood is taken from the:", "عند البالغين يُؤخذ الدم الشعيري من:", [("Side of the middle or ring finger, earlobe", "جانب الإصبع الوسطى أو البنصر، وشحمة الأذن"), ("Thumb nail", "ظفر الإبهام"), ("Heel", "الكعب"), ("Radial artery", "الشريان الكعبري")], "a"),
 Q("During capillary collection, the first drop should be:", "أثناء الجمع الشعيري يجب أن تكون القطرة الأولى:", [("Collected for CBC", "مجموعة لصورة الدم"), ("Wiped away", "ممسوحة"), ("Squeezed out strongly", "معصورة بقوة"), ("Mixed with alcohol", "ممزوجة بالكحول")], "b"),
 Q("Excessive squeezing during capillary collection may cause:", "قد يسبّب العصر المفرط أثناء الجمع الشعيري:", [("Clotting only", "التخثّر فقط"), ("Lipemia", "الدهنية"), ("Hemolysis and contamination with tissue fluid", "تحلّل الدم والتلوّث بسائل الأنسجة"), ("Icterus", "اليرقان")], "c"),
 {"topic_en": "Tubes, serum and plasma, hemolysis", "topic_ar": "الأنابيب والمصل والبلازما وتحلّل الدم"},
 Q("The tube used for CBC and blood film contains:", "الأنبوب المستخدم لصورة الدم والمسحة يحتوي على:", [("Sodium citrate", "سترات الصوديوم"), ("EDTA", "EDTA"), ("Heparin", "الهيبارين"), ("Fluoride", "الفلورايد")], "b"),
 Q("Coagulation tests use a tube containing:", "تستخدم فحوص التخثّر أنبوبًا يحتوي على:", [("Sodium citrate", "سترات الصوديوم"), ("EDTA", "EDTA"), ("Fluoride/oxalate", "الفلورايد/الأوكزالات"), ("Nothing", "لا شيء")], "a"),
 Q("Fluoride/oxalate tubes are used for:", "تُستخدم أنابيب الفلورايد/الأوكزالات لـ:", [("Serum", "المصل"), ("CBC", "صورة الدم"), ("Blood gases", "غازات الدم"), ("Glucose", "الكلوكوز")], "d"),
 Q("A plain tube is used to obtain:", "يُستخدم الأنبوب العادي للحصول على:", [("Plasma", "البلازما"), ("Whole blood", "الدم الكامل"), ("Serum", "المصل"), ("Buffy coat", "الطبقة البيضاء")], "c"),
 Q("The main difference between serum and plasma is that serum:", "الفرق الرئيس بين المصل والبلازما أن المصل:", [("Contains fibrinogen", "يحتوي الفايبرينوجين"), ("Does not contain fibrinogen", "لا يحتوي الفايبرينوجين"), ("Comes from anticoagulated blood", "يأتي من دم مضاف إليه مانع تخثّر"), ("Contains RBCs", "يحتوي كريات حمراء")], "b"),
 Q("Blood + anticoagulant gives:", "دم + مانع تخثّر يعطي:", [("Plasma", "البلازما"), ("Serum", "المصل"), ("Clot only", "خثرة فقط"), ("Hemolysate", "محلّل دموي")], "a"),
 Q("Hemolysis is the rupture of RBCs with release of:", "تحلّل الدم هو تمزّق الكريات الحمر مع تحرّر:", [("Fibrinogen", "الفايبرينوجين"), ("Bilirubin only", "البيليروبين فقط"), ("Lipids", "الدهون"), ("Hemoglobin and intracellular contents", "الهيموغلوبين والمحتويات داخل الخلوية")], "d"),
 Q("A common cause of hemolysis is:", "من الأسباب الشائعة لتحلّل الدم:", [("Large needle", "الإبرة الكبيرة"), ("Gentle mixing", "الخلط اللطيف"), ("Forceful aspiration", "السحب بقوة"), ("Allowing alcohol to dry", "ترك الكحول يجفّ")], "c"),
 Q("The tourniquet should not be left on for more than:", "يجب ألّا يُترك الرباط الضاغط أكثر من:", [("1 minute", "دقيقة واحدة"), ("5 minutes", "5 دقائق"), ("10 minutes", "10 دقائق"), ("30 minutes", "30 دقيقة")], "a"),
 {"topic_en": "Picture questions", "topic_ar": "أسئلة الصور"},
 Q("In this figure, the vein marked as preferred (most common) for venipuncture is the:", "في هذا الشكل، الوريد المؤشَّر بأنه المفضّل لسحب الدم هو:", [("Basilic vein", "الوريد القاعدي"), ("Median cubital vein", "الوريد المرفقي الناصف"), ("Cephalic vein", "الوريد الرأسي"), ("Dorsal hand vein", "وريد ظهر اليد")], "b", img="assets/antecubital-veins.jpg", img_h="44mm"),
 Q("In this figure of an infant’s heel, where should the puncture be made?", "في شكل كعب الرضيع هذا، أين يجب أن يكون الوخز؟", [("The central area of the heel", "المنطقة الوسطى من الكعب"), ("The toes", "أصابع القدم"), ("The medial or lateral plantar surface", "السطح الأخمصي الإنسي أو الوحشي"), ("The back of the heel", "مؤخّرة الكعب")], "c", img="assets/capillary-collection.jpg", img_h="42mm"),
 Q("In this figure, tube number 6 (red serum) is:", "في هذا الشكل، الأنبوب رقم 6 (مصل أحمر) هو:", [("Normal serum", "مصل طبيعي"), ("Icteric serum", "مصل يرقاني"), ("Lipemic serum", "مصل دهني"), ("Hemolyzed serum", "مصل متحلّل")], "d", img="assets/normal-vs-pathology-serum.jpg", img_h="48mm"),
 Q("In this figure, tube number 5 (milky serum) is:", "في هذا الشكل، الأنبوب رقم 5 (مصل حليبي) هو:", [("Lipemic serum", "مصل دهني"), ("Hemolyzed serum", "مصل متحلّل"), ("Normal serum", "مصل طبيعي"), ("Icteric serum", "مصل يرقاني")], "a", img="assets/normal-vs-pathology-serum.jpg", img_h="48mm"),
 Q("The lavender (purple) tube in this figure contains EDTA and is used for:", "الأنبوب البنفسجي في هذا الشكل يحتوي EDTA ويُستخدم لـ:", [("Glucose", "الكلوكوز"), ("CBC, blood film", "صورة الدم والمسحة"), ("Coagulation tests", "فحوص التخثّر"), ("Blood gases", "غازات الدم")], "b", img="assets/collection-tubes.jpg", img_h="46mm"),
 Q("The system shown on the left of this figure, using evacuated tubes, is the:", "النظام المعروض يسار هذا الشكل، الذي يستخدم أنابيب مفرّغة، هو:", [("Butterfly (winged) system", "نظام الفراشة (المجنّح)"), ("Disposable syringe", "المحقنة ذات الاستعمال الواحد"), ("Vacuum (evacuated tube) system", "النظام المفرَّغ (الأنابيب المفرّغة)"), ("Lancet", "مِشرط الوخز")], "c", img="assets/venipuncture-systems.jpg", img_h="46mm"),
]

tf = [
 dict(en="Blood collection is used for laboratory testing, diagnosis and monitoring.", ar="يُستخدم جمع الدم للفحص المختبري والتشخيص والمتابعة.", answer="T"),
 dict(en="Capillary blood provides a relatively large volume of blood.", ar="يوفّر الدم الشعيري حجمًا كبيرًا نسبيًا من الدم.", answer="F"),
 dict(en="The median cubital vein is the preferred site for venipuncture.", ar="الوريد المرفقي الناصف هو الموقع المفضّل لسحب الدم الوريدي.", answer="T"),
 dict(en="Patient identification is the first basic step of venous collection.", ar="تعريف المريض هو الخطوة الأساسية الأولى في الجمع الوريدي.", answer="T"),
 dict(en="The brachial artery is the preferred artery for ABG.", ar="الشريان العضدي هو الشريان المفضّل لغازات الدم.", answer="F"),
 dict(en="Air bubbles should be removed from an arterial sample.", ar="يجب إزالة فقاعات الهواء من العيّنة الشريانية.", answer="T"),
 dict(en="Firm pressure is applied after arterial collection.", ar="يُطبَّق ضغط قوي بعد سحب الدم الشرياني.", answer="T"),
 dict(en="In capillary collection, the alcohol should not be allowed to dry.", ar="في الجمع الشعيري لا يجب ترك الكحول يجفّ.", answer="F"),
 dict(en="Sodium citrate tubes are used for coagulation tests.", ar="تُستخدم أنابيب سترات الصوديوم لفحوص التخثّر.", answer="T"),
 dict(en="Heparin tubes are used for glucose.", ar="تُستخدم أنابيب الهيبارين للكلوكوز.", answer="F"),
 dict(en="Plasma contains fibrinogen.", ar="تحتوي البلازما على الفايبرينوجين.", answer="T"),
 dict(en="Serum is obtained from anticoagulated blood.", ar="يُحصل على المصل من دم مضاف إليه مانع تخثّر.", answer="F"),
 dict(en="Hemolyzed samples may appear pink or red.", ar="قد تظهر العيّنات المتحلّلة وردية أو حمراء.", answer="T"),
 dict(en="Vigorous shaking of tubes prevents hemolysis.", ar="رجّ الأنابيب بعنف يمنع تحلّل الدم.", answer="F"),
]

traps = [
 dict(en="Preferred vein vs preferred artery", ar="الوريد المفضّل مقابل الشريان المفضّل", answer_en="Vein: median cubital. Artery (ABG): radial.", answer_ar="الوريد: المرفقي الناصف. الشريان (غازات الدم): الكعبري."),
 dict(en="Capillary sites: adults vs infants", ar="مواقع الدم الشعيري: البالغون مقابل الرضّع", answer_en="Adults/older children: side of the middle or ring finger, earlobe. Infants: medial or lateral plantar surface of the heel (avoid the central heel).", answer_ar="البالغون/الأطفال الأكبر: جانب الوسطى أو البنصر، وشحمة الأذن. الرضّع: السطح الأخمصي الإنسي أو الوحشي للكعب (تجنّب وسط الكعب)."),
 dict(en="Which tube for which test?", ar="أي أنبوب لأي فحص؟", answer_en="EDTA → CBC, blood film; sodium citrate → coagulation; heparin → blood gases/some chemistry; fluoride/oxalate → glucose; plain → serum.", answer_ar="EDTA ← صورة الدم والمسحة؛ سترات الصوديوم ← التخثّر؛ الهيبارين ← غازات الدم/بعض الكيمياء؛ الفلورايد/الأوكزالات ← الكلوكوز؛ العادي ← المصل."),
 dict(en="Serum vs plasma — which has fibrinogen?", ar="المصل مقابل البلازما — أيهما فيه الفايبرينوجين؟", answer_en="Plasma (anticoagulated blood) contains fibrinogen; serum (after clotting) does not.", answer_ar="البلازما (دم مع مانع تخثّر) تحتوي الفايبرينوجين؛ والمصل (بعد التخثّر) لا يحتويه."),
 dict(en="Small or large needle for hemolysis?", ar="إبرة صغيرة أم كبيرة وتحلّل الدم؟", answer_en="A small needle causes hemolysis; use an appropriate needle size.", answer_ar="الإبرة الصغيرة تسبّب تحلّل الدم؛ استخدم إبرة بحجم مناسب."),
 dict(en="Why wipe the first drop?", ar="لماذا تُمسح القطرة الأولى؟", answer_en="It is part of capillary precautions (with letting alcohol dry and avoiding squeezing) — squeezing causes hemolysis and tissue-fluid contamination.", answer_ar="من احتياطات الجمع الشعيري (مع ترك الكحول يجفّ وتجنّب العصر) — فالعصر يسبّب التحلّل والتلوّث بسائل الأنسجة."),
 dict(en="Colours of serum in the figure", ar="ألوان المصل في الشكل", answer_en="Normal: clear yellow; icteric (hyperbilirubinemia): dark yellow; lipemic: milky; hemolyzed: red.", answer_ar="الطبيعي: أصفر صافٍ؛ اليرقاني (فرط البيليروبين): أصفر داكن؛ الدهني: حليبي؛ المتحلّل: أحمر."),
]

important = [  # the lecturer's own review questions (slide 15), with model answers from the lecture
 dict(en="What is blood collection, and what are its main purposes?", ar="ما جمع الدم، وما أغراضه الرئيسة؟", answer_en="Obtaining a blood sample for laboratory testing, diagnosis and monitoring. Purposes: laboratory testing, blood donation, monitoring.", answer_ar="الحصول على عيّنة دم للفحص المختبري والتشخيص والمتابعة. أغراضه: الفحص المختبري، التبرّع بالدم، المتابعة."),
 dict(en="What are the three main types of blood collection?", ar="ما الأنواع الثلاثة الرئيسة لجمع الدم؟", answer_en="Venous, capillary and arterial.", answer_ar="الوريدي، والشعيري، والشرياني."),
 dict(en="What is the preferred vein for venipuncture?", ar="ما الوريد المفضّل لسحب الدم الوريدي؟", answer_en="The median cubital vein.", answer_ar="الوريد المرفقي الناصف."),
 dict(en="What are the basic steps of venous blood collection?", ar="ما الخطوات الأساسية لجمع الدم الوريدي؟", answer_en="Patient identification → tourniquet → disinfection (70% alcohol) → blood collection → pressure → labeling.", answer_ar="تعريف المريض ← الرباط الضاغط ← التعقيم (كحول 70%) ← سحب الدم ← الضغط ← وضع الملصق."),
 dict(en="What is the main purpose of arterial blood collection?", ar="ما الغرض الرئيس من جمع الدم الشرياني؟", answer_en="Arterial blood gas (ABG) analysis.", answer_ar="تحليل غازات الدم الشرياني (ABG)."),
 dict(en="What is the preferred artery for ABG sampling?", ar="ما الشريان المفضّل لسحب غازات الدم؟", answer_en="The radial artery.", answer_ar="الشريان الكعبري."),
 dict(en="What parameters are measured in ABG analysis?", ar="ما المعايير التي يقيسها تحليل غازات الدم؟", answer_en="pH, PaO₂, PaCO₂, HCO₃⁻ and O₂ saturation.", answer_ar="pH، وPaO₂، وPaCO₂، وHCO₃⁻، وتشبّع الأوكسجين."),
 dict(en="What are the common sites for capillary blood collection in adults and infants?", ar="ما المواقع الشائعة للجمع الشعيري عند البالغين والرضّع؟", answer_en="Adults/older children: side of the middle or ring finger, earlobe. Infants: medial or lateral plantar surface of the heel.", answer_ar="البالغون/الأطفال الأكبر: جانب الوسطى أو البنصر، وشحمة الأذن. الرضّع: السطح الأخمصي الإنسي أو الوحشي للكعب."),
 dict(en="Why should excessive squeezing be avoided during capillary collection?", ar="لماذا يجب تجنّب العصر المفرط أثناء الجمع الشعيري؟", answer_en="It may cause hemolysis and contamination with tissue fluid.", answer_ar="لأنه قد يسبّب تحلّل الدم والتلوّث بسائل الأنسجة."),
 dict(en="What is the main difference between serum and plasma?", ar="ما الفرق الرئيس بين المصل والبلازما؟", answer_en="Plasma comes from anticoagulated blood and contains fibrinogen; serum is obtained after clotting and does not contain fibrinogen.", answer_ar="البلازما من دم مع مانع تخثّر وتحتوي الفايبرينوجين؛ والمصل بعد التخثّر ولا يحتويه."),
 dict(en="What is hemolysis? Mention two common causes.", ar="ما تحلّل الدم؟ اذكر سببين شائعين.", answer_en="Rupture of RBCs with release of hemoglobin and intracellular contents into serum/plasma. Causes: small needle, forceful aspiration, vigorous shaking.", answer_ar="تمزّق الكريات الحمر مع تحرّر الهيموغلوبين والمحتويات داخل الخلوية إلى المصل/البلازما. أسبابه: الإبرة الصغيرة، السحب بقوة، الرجّ العنيف."),
 dict(en="How can hemolysis be prevented during blood collection?", ar="كيف يمكن منع تحلّل الدم أثناء الجمع؟", answer_en="Use an appropriate needle size, avoid forceful aspiration, and handle and mix tubes gently.", answer_ar="استخدام إبرة بحجم مناسب، وتجنّب السحب بقوة، والتعامل مع الأنابيب وخلطها بلطف."),
]

data = {"meta": {
  "subject_en": "Hematology", "subject_ar": "أمراض الدم", "short_ar": "امراض الدم",
  "unit_en": "Lab 1", "unit_ar": "العملي 1", "unit_label": "LAB", "unit_no": "1",
  "title_en": "Blood Collection", "title_ar": "جمع الدم",
  "kind": "Laboratories — عملي", "stage": "The third stage — الثالثة", "instructor": "ليندا منجد هادي"},
 "blocks": blocks, "questions": {"mcq": mcq, "tf": tf, "traps": traps, "important": important}}
qs = [q for q in mcq if "answer" in q]
print(len(qs), Counter(q["answer"] for q in qs))
json.dump(data, open("/home/user/-/hematology-lab1-blood-collection/lecture.json", "w"), ensure_ascii=False, indent=1)

```
