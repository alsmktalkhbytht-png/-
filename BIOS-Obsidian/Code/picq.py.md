---
source: BIOS-Obsidian/tools/scripts/picq.py
handouts: [bloodbank-lec1-introduction, immunology-lab1-serology, lab1-biosafety]
saved: 2026-10-31
tags: [bios, code]
---
# picq.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#bloodbank-lec1-introduction|bloodbank-lec1-introduction]] · [[06 فهرس الملازم#immunology-lab1-serology|immunology-lab1-serology]] · [[06 فهرس الملازم#lab1-biosafety|lab1-biosafety]]

```python
import json

TOPIC = {"topic_en": "Picture questions", "topic_ar": "أسئلة الصور"}


def Q(img, en, ar, opts, ans, h="40mm"):
    return {"img": img, "img_h": h, "en": en, "ar": ar, "options": opts, "answer": ans}


PICS = {
 "lab1-biosafety": [
  Q("assets/biohazard.jpg", "What does this warning symbol indicate?", "ماذا تعني علامة التحذير هذه؟",
    [["Radiation hazard", "خطر إشعاعي"], ["Potential presence of dangerous biological materials", "احتمال وجود مواد بيولوجية خطرة"],
     ["Fire hazard", "خطر الحريق"], ["Electrical hazard", "خطر كهربائي"]], "b", "34mm"),
  Q("assets/radiation.jpg", "This warning symbol is the:", "علامة التحذير هذه هي:",
    [["Biohazard symbol", "رمز الخطر البيولوجي"], ["Laser warning", "تحذير الليزر"], ["Radiation hazard symbol", "رمز الخطر الإشعاعي"], ["Toxic chemical symbol", "رمز المواد الكيميائية السامة"]], "c", "30mm"),
  Q("assets/ppe.jpg", "The worker in the picture is wearing:", "الشخص في الصورة يرتدي:",
    [["Personal protective equipment (gown – mask – safety glasses – gloves)", "معدات الحماية الشخصية (رداء – كمامة – نظارات السلامة – قفازات)"],
     ["Ordinary clothes", "ملابس عادية"], ["Radiation suit only", "بدلة إشعاع فقط"], ["Surgical cap only", "قبعة جراحية فقط"]], "a", "30mm"),
  Q("assets/nofood.jpg", "In the laboratory, this sign means:", "تعني هذه العلامة في المختبر:",
    [["Wash your hands", "اغسل يديك"], ["Use lab glassware for drinks", "استعمل الأواني المختبرية للشرب"],
     ["Store food in the lab refrigerator", "خزّن الطعام في ثلاجة المختبر"], ["Do not eat food or drink water in the lab", "لا تأكل ولا تشرب في المختبر"]], "d", "36mm"),
  Q("assets/cultures.jpg", "All cultures like those in the picture should be handled as:", "يجب التعامل مع جميع المزارع مثل التي في الصورة على أنها:",
    [["Potentially pathogenic", "ممرضة محتملة"], ["Non-pathogenic", "غير ممرضة"], ["Safe to take home", "آمنة لأخذها إلى البيت"], ["Sterile", "معقّمة"]], "a"),
  Q("assets/handwash.jpg", "According to the safety rules, hands are washed:", "وفق تعليمات السلامة، تُغسل اليدان:",
    [["Only before entering the lab", "قبل دخول المختبر فقط"], ["After working with infectious materials", "بعد العمل مع المواد المُعدية"],
     ["Only once a day", "مرة واحدة في اليوم فقط"], ["Never while wearing gloves", "لا تُغسل أبدًا في أثناء ارتداء القفازات"]], "b"),
  Q("assets/disinfect.jpg", "Instruments and contaminated waste should be disinfected:", "يجب تطهير الأدوات والنفايات الملوّثة:",
    [["At the end of the week", "في نهاية الأسبوع"], ["Only if visibly dirty", "فقط إذا بدت متّسخة"],
     ["Immediately after use / before discarding", "فور الاستخدام / قبل التخلّص منها"], ["Never", "أبدًا"]], "c"),
  Q("assets/cabinets.jpg", "In this picture of laboratory equipment, which device sterilizes by pressurized steam?", "في صورة الأجهزة المختبرية هذه، أي جهاز يعقّم بالبخار المضغوط؟",
    [["PCR cabinet", "خزانة PCR"], ["Incubator", "الحاضنة"], ["Laminar flow cabinet", "خزانة التدفق الصفائحي"], ["Autoclave", "جهاز التعقيم بالبخار (الأوتوكليف)"]], "d", "52mm"),
 ],
 "immunology-lab1-serology": [
  Q("assets/plasma-tube.jpg", "In this tube of blood with anticoagulant, the upper yellowish layer is:", "في أنبوب الدم هذا الممزوج بمانع التخثّر، الطبقة العليا المائلة إلى الصفرة هي:",
    [["Serum", "المصل"], ["Plasma", "البلازما"], ["Red cells", "الخلايا الحمر"], ["Saline", "المحلول الملحي"]], "b", "44mm"),
  Q("assets/plasma-serum-tubes.jpg", "The right tube shows serum over clotted blood. Serum differs from plasma because it does not include:", "يُظهر الأنبوب الأيمن المصل فوق الدم المتخثّر. يختلف المصل عن البلازما لأنه لا يحتوي:",
    [["Albumin", "الألبومين"], ["Antibodies", "الأجسام المضادة"], ["Fibrinogens", "الفايبرينوجين"], ["Hormones", "الهرمونات"]], "c", "40mm"),
  Q("assets/rbcs.jpg", "To prepare the cells shown, the suspension is washed by centrifugation for:", "لتحضير الخلايا المبيّنة، يُغسل المعلّق بالطرد المركزي مدة:",
    [["5 min. at 3000 rpm", "5 دقائق بسرعة 3000 دورة/دقيقة"], ["1 min. at 500 rpm", "دقيقة واحدة بسرعة 500 دورة/دقيقة"],
     ["30 min. at 300 rpm", "30 دقيقة بسرعة 300 دورة/دقيقة"], ["10 min. at 10000 rpm", "10 دقائق بسرعة 10000 دورة/دقيقة"]], "a", "36mm"),
  Q("assets/tourniquet.jpg", "The tourniquet in the picture is placed above the venipuncture site by about:", "يوضع الرباط الضاغط في الصورة فوق موضع سحب الدم بنحو:",
    [["1 finger", "إصبع واحد"], ["10 fingers", "10 أصابع"], ["Directly on the site", "على الموضع مباشرة"], ["3-4 fingers", "3–4 أصابع"]], "d", "40mm"),
  Q("assets/hematoma.jpg", "The collection of blood under the skin shown in the picture is called:", "تجمّع الدم تحت الجلد المبيّن في الصورة يُسمّى:",
    [["Hematoma", "ورم دموي (Hematoma)"], ["Abscess", "خرّاج"], ["Rash", "طفح جلدي"], ["Burn", "حرق"]], "a", "32mm"),
  Q("assets/chain-of-infection.jpg", "According to the figure, which of the following is a prevention measure?", "وفق الشكل، أيٌّ مما يأتي من إجراءات الوقاية؟",
    [["Leaving wastes in the lab", "ترك النفايات في المختبر"], ["Sharing gloves", "مشاركة القفازات"], ["Hand washing", "غسل اليدين"], ["Removing sample labels", "إزالة ملصقات العيّنات"]], "c", "58mm"),
 ],
 "bloodbank-lec1-introduction": [
  Q("assets/russian-syringe.jpg", "This World War II Russian device was used for:", "استُعمل هذا الجهاز الروسي من الحرب العالمية الثانية لـ:",
    [["Direct inter-human blood transfusion", "نقل الدم المباشر بين شخصين"], ["Plasma freezing", "تجميد البلازما"], ["Blood grouping", "تحديد فصيلة الدم"], ["Platelet storage", "خزن الصفائح الدموية"]], "a", "40mm"),
  Q("assets/agote-1914.jpg", "Luis Agote (in the picture) oversaw one of the first safe transfusions in 1914. In the same year, transfusion became safer because Hustin reported:", "أشرف لويس أغوتي (في الصورة) على إحدى أولى عمليات النقل الآمنة عام 1914. وفي العام نفسه أصبح نقل الدم أكثر أمانًا لأن هوستن أعلن عن:",
    [["The ABO blood groups", "فصائل الدم ABO"], ["Sodium citrate as an anticoagulant", "سترات الصوديوم مانعًا للتخثّر"], ["The plastic blood bag", "كيس الدم البلاستيكي"], ["Blood circulation", "الدورة الدموية"]], "b", "40mm"),
  Q("assets/blood-bag.jpg", "Breakable glass bottles like the one in the picture were replaced in 1950 by:", "استُبدلت القناني الزجاجية القابلة للكسر مثل التي في الصورة عام 1950 بـ:",
    [["Metal containers", "أوعية معدنية"], ["Rubber bags", "أكياس مطاطية"], ["Durable plastic bags", "أكياس بلاستيكية متينة"], ["Direct syringes", "محاقن مباشرة"]], "c", "48mm"),
 ],
}

for folder, qs in PICS.items():
    p = f"/home/user/-/{folder}/lecture.json"
    d = json.load(open(p))
    mcq = [q for q in d["questions"]["mcq"] if "img" not in q and q.get("topic_en") != "Picture questions"]
    d["questions"]["mcq"] = mcq + [TOPIC] + qs
    json.dump(d, open(p, "w"), ensure_ascii=False, indent=1)
    print(folder, len(qs))

```
