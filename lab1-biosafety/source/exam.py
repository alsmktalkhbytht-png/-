import sys
from lib import *
from art import emblem, grid
from booklet import SUBJ_EN, SUBJ_AR, TITLE_EN, TITLE_AR, COVER_CSS

EXAM_CSS = r"""
.exam{--acc:#9C6FB3;--acc-d:#6E4483}
.exam .sec{background:linear-gradient(90deg,var(--wis-l),var(--cream))}
.exam .hrule{background:linear-gradient(90deg,var(--wis) 0 62%,var(--van) 62% 80%,var(--moon) 80%)}
.q{margin:0 0 2.6mm;break-inside:avoid;border-bottom:.35mm dashed var(--line);padding-bottom:2.4mm}
.q:last-child{border-bottom:0}
.qh{display:flex;gap:3mm;align-items:flex-start}
.qn{flex:none;min-width:11mm;height:7mm;border-radius:3.5mm;background:var(--acc);color:#fff;font-weight:800;font-size:10.5pt;display:flex;align-items:center;justify-content:center;margin-top:.8mm}
.qt{flex:1}
.qt .en{font-weight:600;line-height:1.3}.qt .ar{line-height:1.45}
.opts{display:flex;flex-direction:column;gap:.9mm;margin:1.6mm 0 0 14mm}
.opt{display:grid;grid-template-columns:7mm 1fr 1fr;gap:3mm;align-items:start;background:#FCFAFD;border:.3mm solid var(--wis-l);border-radius:2.5mm;padding:.5mm 3mm}
.opt .l{flex:none;width:5.6mm;height:5.6mm;border-radius:50%;border:.45mm solid var(--acc);color:var(--acc-d);font-weight:800;font-size:10pt;display:flex;align-items:center;justify-content:center;margin-top:.6mm}
.opt .en{font-size:12.5pt;line-height:1.25}
.opt .ar{font-size:12.5pt;line-height:1.3;margin-top:0}
.tf{display:flex;gap:3mm;align-items:flex-start;margin:0 0 3.6mm;break-inside:avoid;border-bottom:.35mm dashed var(--line);padding-bottom:2.4mm}
.tf .qt .en{font-weight:500}
.tfbox{flex:none;display:flex;gap:1.5mm;margin-top:.8mm}
.tfbox span{width:15mm;height:7mm;gap:1.4mm;white-space:nowrap;border:.45mm solid var(--acc);border-radius:2mm;font-weight:800;font-size:10pt;color:var(--acc-d);display:flex;align-items:center;justify-content:center}
.tfbox em{font-style:normal;font-weight:700;font-size:9.5pt}.ans-lines{height:24mm;margin:2mm 0 0 14mm;background:repeating-linear-gradient(to bottom,transparent 0,transparent 7.7mm,rgba(156,111,179,.4) 7.7mm,rgba(156,111,179,.4) 8mm)}
.key{display:grid;grid-template-columns:repeat(6,1fr);gap:2mm;margin-bottom:4mm}
.key div{border:.35mm solid var(--line);border-radius:2.5mm;padding:1.4mm 0;text-align:center;font-weight:800;font-size:12pt;background:#fff}
.key div b{color:var(--acc-d);margin-right:1.2mm}
.key div span{color:var(--moon-dd)}
.ka{margin:0 0 2.6mm;display:grid;grid-template-columns:9mm 1fr;gap:2mm;break-inside:avoid}.ka .kn{font-weight:900;color:#fff;background:var(--acc);border-radius:2.5mm;height:6.5mm;display:flex;align-items:center;justify-content:center;font-size:10pt;margin-top:1mm}.ka .en,.ka .ar{font-size:13pt}.kq2{font-weight:800;color:var(--acc-d);font-size:12pt}
.ka .kq{font-weight:800;color:var(--acc-d);font-size:12pt}
/* exam cover */
.cv2 .cv-top{background:var(--wis)}
.cv2 .cv-bot{background:var(--cream)}
.cv2 .cv-ar{color:var(--cream)}
.cv2 .cv-en{color:#fff}.cv2 .cv-en small{color:var(--cream)}
.cv2 .cv-chip{color:var(--cream)}.cv2 .cv-chip .tri{border-left-color:var(--cream)}
.cv2 .cv-badge span{background:var(--cream);color:var(--wis-d)}.cv2 .cv-badge span.w{background:var(--moon);color:#fff}
.cv2 .cv-info{color:var(--wis-d)}
.cv2 .cv-subj{color:var(--wis-d)}.cv2 .cv-subj-ar{color:var(--moon-d)}
.cv2 .cv-rows{border-top-color:rgba(122,78,143,.35)}
.cv2 .cv-row{border-bottom-color:rgba(122,78,143,.25)}
.cv2 .cv-row .k{color:var(--wis-d)}.cv2 .cv-row .v,.cv2 .cv-row .va{color:var(--moon-dd)}
.cv2 .cv-foot{color:var(--wis-d)}
.cv2 .cv-logo-badge{position:absolute;left:12mm;top:11mm;width:68mm;padding:3mm 4mm;background:var(--van);border-radius:6mm}
.cv2 .cv-logo-badge img{width:100%;display:block}
"""

# ---------------------------------------------------------------- questions
# (q_en, q_ar, [(opt_en, opt_ar) x4], answer_letter)
MCQ = [
 ("Biosafety levels are principles and application used to protect:", "مستويات السلامة الحيوية مبادئ وتطبيقات تُستخدم لحماية:",
  [("Only the patients", "المرضى فقط"), ("Only laboratory equipment", "الأجهزة المختبرية فقط"),
   ("Laboratory workers and the surrounding environment", "العاملين في المختبر والبيئة المحيطة"), ("Only the cultures", "المزارع فقط")], "c"),
 ("Biosafety levels aim to provide:", "تهدف مستويات السلامة الحيوية إلى توفير:",
  [("The highest level of protection and the lowest range of exposure", "أعلى مستوى من الحماية وأدنى مدى من التعرّض"),
   ("The lowest level of protection and the highest range of exposure", "أدنى مستوى من الحماية وأعلى مدى من التعرّض"),
   ("Moderate protection and moderate exposure", "حماية متوسطة وتعرّض متوسط"),
   ("Protection of cultures only", "حماية المزارع فقط")], "a"),
 ("Risk groups are used to:", "تُستخدم مجموعات الخطورة من أجل:",
  [("Sterilize instruments", "تعقيم الأدوات"), ("Assess risk, determine its source and how to deal with it", "تقييم الخطر وتحديد مصدره وكيفية التعامل معه"),
   ("Destroy bacterial spores", "تدمير الأبواغ البكتيرية"), ("Classify lab glassware", "تصنيف الأدوات الزجاجية المختبرية")], "b"),
 ("How many risk groups are described in the lecture?", "كم عدد مجموعات الخطورة الموصوفة في المحاضرة؟",
  [("2", "2"), ("3", "3"), ("5", "5"), ("4", "4")], "d"),
 ("*Bacillus Subtilis* belongs to:", "تنتمي `*Bacillus Subtilis*` إلى:",
  [("Risk group 1", "مجموعة الخطورة 1"), ("Risk group 2", "مجموعة الخطورة 2"), ("Risk group 3", "مجموعة الخطورة 3"), ("Risk group 4", "مجموعة الخطورة 4")], "a"),
 ("Risk group 1 includes:", "تضم مجموعة الخطورة 1:",
  [("Factors that are fatal to humans", "عوامل مميتة للإنسان"), ("Non-pathogenic factors in healthy people and adults", "عوامل غير مُمرِضة للأشخاص الأصحّاء والبالغين"),
   ("Factors whose treatment is not easy", "عوامل علاجها ليس سهلًا"), ("Factors related to human infection only", "عوامل مرتبطة بعدوى الإنسان فقط")], "b"),
 ("Which statement describes Risk group 2?", "أيّ عبارة تصف مجموعة الخطورة 2؟",
  [("Minimal risk; non-pathogenic", "خطورة ضئيلة؛ غير مُمرِضة"), ("High risk; treatment is not easy", "خطورة عالية؛ العلاج ليس سهلًا"),
   ("Moderate risk; treatment is possible; limited risk of spread", "خطورة متوسطة؛ العلاج ممكن؛ خطر انتشار محدود"), ("Extreme risk", "خطورة قصوى")], "c"),
 ("*Brucella spp.* is an example of:", "تُعدّ `*Brucella spp.*` مثالًا على:",
  [("Risk group 1", "مجموعة الخطورة 1"), ("Risk group 3", "مجموعة الخطورة 3"), ("Risk group 4", "مجموعة الخطورة 4"), ("Risk group 2", "مجموعة الخطورة 2")], "d"),
 ("The pathogenic strain of *E.coli* is classified in:", "تُصنَّف السلالة المُمرِضة من `*E.coli*` ضمن:",
  [("Risk group 2", "مجموعة الخطورة 2"), ("Risk group 1", "مجموعة الخطورة 1"), ("Risk group 3", "مجموعة الخطورة 3"), ("Risk group 4", "مجموعة الخطورة 4")], "a"),
 ("*Mycobacterium tuberculosis* belongs to:", "تنتمي `*Mycobacterium tuberculosis*` إلى:",
  [("Risk group 1", "مجموعة الخطورة 1"), ("Risk group 2", "مجموعة الخطورة 2"), ("Risk group 3", "مجموعة الخطورة 3"), ("Risk group 4", "مجموعة الخطورة 4")], "c"),
 ("*Salmonella typhi* is classified in:", "تُصنَّف `*Salmonella typhi*` ضمن:",
  [("Risk group 1", "مجموعة الخطورة 1"), ("Risk group 3", "مجموعة الخطورة 3"), ("Risk group 2", "مجموعة الخطورة 2"), ("Risk group 4", "مجموعة الخطورة 4")], "b"),
 ("Risk group 3 agents are especially dangerous for:", "عوامل مجموعة الخطورة 3 خطيرة بشكل خاص على:",
  [("Immunosuppressed persons", "الأشخاص المثبَّطة مناعتهم"), ("Laboratory equipment", "الأجهزة المختبرية"),
   ("Inanimate objects", "الأجسام غير الحيّة"), ("Lab glassware", "الأدوات الزجاجية المختبرية")], "a"),
 ("The biosafety level that corresponds to Risk group 3 is:", "مستوى السلامة الحيوية المقابل لمجموعة الخطورة 3 هو:",
  [("Biosafety level 1", "مستوى السلامة الحيوية 1"), ("Biosafety level 2", "مستوى السلامة الحيوية 2"),
   ("Biosafety level 4", "مستوى السلامة الحيوية 4"), ("Biosafety level 3", "مستوى السلامة الحيوية 3")], "d"),
 ("Risk group 4 is described as:", "توصف مجموعة الخطورة 4 بأنها:",
  [("Minimal risk", "خطورة ضئيلة"), ("Extreme risk", "خطورة قصوى"), ("Moderate risk", "خطورة متوسطة"), ("High risk", "خطورة عالية")], "b"),
 ("The biohazard symbol is used to:", "يُستخدم رمز الخطر الحيوي من أجل:",
  [("Warn people of the potential presence of dangerous biological materials", "تحذير الأشخاص من احتمال وجود مواد بيولوجية خطرة"),
   ("Mark sterile instruments", "تمييز الأدوات المعقّمة"), ("Indicate radiation sources only", "الإشارة إلى مصادر الإشعاع فقط"),
   ("Label food containers", "وسم أوعية الطعام")], "a"),
 ("Which of the following is NOT listed as an example for using the biohazard symbol?", "أيّ مما يلي لم يُذكر مثالًا لاستخدام رمز الخطر الحيوي؟",
  [("Cultures of pathogens", "مزارع المُمرِضات"), ("Human blood and tissue", "دم الإنسان وأنسجته"),
   ("Corridors leading to the laboratories", "الممرات المؤدية إلى المختبرات"), ("Office stationery", "القرطاسية المكتبية")], "d"),
 ("Protective clothing in the lab includes all of the following EXCEPT:", "تشمل الملابس الواقية في المختبر جميع ما يلي ما عدا:",
  [("Clean lab coat", "معطف مختبر نظيف"), ("Lab glassware", "الأدوات الزجاجية المختبرية"), ("Mask", "الكمامة"), ("Safety glasses", "النظارات الواقية")], "b"),
 ("While wearing gloves, you should avoid touching:", "أثناء ارتداء القفازات يجب تجنّب لمس:",
  [("Pencils", "الأقلام"), ("Cell phones", "الهواتف المحمولة"), ("Door handles", "مقابض الأبواب"), ("All of the above", "جميع ما سبق")], "d"),
 ("Long hair must be tied back or covered to minimize:", "يجب ربط الشعر الطويل أو تغطيته لتقليل:",
  [("Fire hazard or contamination of experiment", "خطر الحريق أو تلوّث التجربة"), ("Noise in the lab", "الضوضاء في المختبر"),
   ("Breakage of glassware", "كسر الأدوات الزجاجية"), ("Radiation hazard", "خطر الإشعاع")], "a"),
 ("All cultures should be handled as:", "يجب التعامل مع جميع المزارع على أنها:",
  [("Non-pathogenic", "غير مُمرِضة"), ("Sterile", "معقّمة"), ("Potentially pathogenic", "يُحتمل أن تكون مُمرِضة"), ("Harmless outside the lab", "غير ضارة خارج المختبر")], "c"),
 ("Laboratory instruments should be disinfected:", "يجب تطهير أدوات المختبر:",
  [("Once a week", "مرة في الأسبوع"), ("Immediately after use", "فور استخدامها"), ("Only before use", "قبل الاستخدام فقط"), ("Only if visibly dirty", "فقط إذا بدت متّسخة")], "b"),
 ("Contaminated waste must be:", "يجب أن تُعامَل النفايات الملوّثة بـ:",
  [("Discarded directly", "التخلّص منها مباشرة"), ("Taken out of the lab", "إخراجها من المختبر"),
   ("Disinfected before discarding", "تطهيرها قبل التخلّص منها"), ("Kept in food containers", "حفظها في أوعية الطعام")], "c"),
 ("The complete killing or removal of all living organisms is called:", "يُسمّى القتل أو الإزالة الكاملة لجميع الكائنات الحية:",
  [("Disinfection", "التطهير"), ("Antiseptics", "المطهّرات الموضعية"), ("Decontamination", "إزالة التلوّث"), ("Sterilization", "التعقيم")], "d"),
 ("The destruction or removal of pathogens but not bacterial spores is:", "تدمير المُمرِضات أو إزالتها ولكن ليس الأبواغ البكتيرية هو:",
  [("Disinfection", "التطهير"), ("Sterilization", "التعقيم"), ("Antiseptics", "المطهّرات الموضعية"), ("Bio risk", "الخطر البيولوجي")], "a"),
 ("Disinfection is usually used only on:", "يُستخدم التطهير عادةً على:",
  [("Body surfaces", "أسطح الجسم"), ("Inanimate objects", "الأجسام غير الحيّة فقط"), ("Wounds", "الجروح"), ("Food", "الطعام")], "b"),
 ("Chemicals applied to body surfaces to destroy or inhibit pathogens are:", "المواد الكيميائية التي تُطبَّق على أسطح الجسم لتدمير المُمرِضات أو تثبيطها هي:",
  [("Disinfectants of instruments", "مطهّرات الأدوات"), ("Sterilizers", "المعقِّمات"), ("Antiseptics", "المطهّرات الموضعية"), ("Cultures", "المزارع")], "c"),
 ("The mechanical removal of most microbes by using washing, heat or disinfectants is:", "الإزالة الميكانيكية لمعظم الميكروبات باستخدام الغسل أو الحرارة أو المطهّرات هي:",
  [("Sterilization", "التعقيم"), ("Decontamination", "إزالة التلوّث"), ("Bio risk assessment", "تقييم الخطر البيولوجي"), ("Antiseptics", "المطهّرات الموضعية")], "b"),
 ("A facility within which microorganisms, their components or their derivatives are collected, handled and/or stored is:", "المنشأة التي تُجمَع فيها الكائنات الحية الدقيقة أو مكوّناتها أو مشتقّاتها ويُتعامل معها و/أو تُخزَّن هي:",
  [("Biosafety cabinet", "كابينة السلامة الحيوية"), ("Incubator", "الحاضنة"), ("Corridor", "الممر"), ("Biological laboratory", "المختبر البيولوجي")], "d"),
 ("The probability or chance that a particular adverse event possibly leads to harm is:", "احتمال أو فرصة أن يؤدي حدث ضار معيّن إلى الضرر هو:",
  [("Bio risk", "الخطر البيولوجي"), ("Biohazard symbol", "رمز الخطر الحيوي"), ("Sterilization", "التعقيم"), ("Risk group 1", "مجموعة الخطورة 1")], "a"),
 ("The process to identify acceptable and unacceptable risks and their potential consequences is:", "عملية تحديد المخاطر المقبولة وغير المقبولة وعواقبها المحتملة هي:",
  [("Decontamination", "إزالة التلوّث"), ("Bio risk assessment", "تقييم الخطر البيولوجي"), ("Disinfection", "التطهير"), ("Biosafety level 1", "مستوى السلامة الحيوية 1")], "b"),
 ("Which of the following is a laboratory biosecurity risk?", "أيّ مما يلي من مخاطر الأمن الحيوي المختبري؟",
  [("Accidental infection", "العدوى العَرَضية"), ("Loss of bacterial spores during sterilization", "فقدان الأبواغ البكتيرية أثناء التعقيم"),
   ("Washing with heat", "الغسل بالحرارة"), ("Unauthorized access, theft or misuse", "الوصول غير المصرَّح به أو السرقة أو إساءة الاستخدام")], "d"),
]

TF = [
 ("Biosafety levels protect only laboratory workers, not the surrounding environment.", "تحمي مستويات السلامة الحيوية العاملين في المختبر فقط، وليس البيئة المحيطة.", "F"),
 ("Risk groups include 4 groups.", "تشمل مجموعات الخطورة 4 مجموعات.", "T"),
 ("*E.coli* and *Bacillus Subtilis* are given as examples of Risk group 1.", "ذُكرت `*E.coli*` و`*Bacillus Subtilis*` مثالين على مجموعة الخطورة 1.", "T"),
 ("In Risk group 2, treatment is not possible.", "في مجموعة الخطورة 2 لا يكون العلاج ممكنًا.", "F"),
 ("Risk group 3 agents cause serious and fatal infections and their treatment is not easy.", "تسبّب عوامل مجموعة الخطورة 3 عدوى خطيرة ومميتة وعلاجها ليس سهلًا.", "T"),
 ("*Salmonella spp.* belongs to Risk group 3.", "تنتمي `*Salmonella spp.*` إلى مجموعة الخطورة 3.", "F"),
 ("Biosafety level 4 corresponds to Risk group 4 (Extreme risk).", "يقابل مستوى السلامة الحيوية 4 مجموعة الخطورة 4 (خطورة قصوى).", "T"),
 ("The biohazard symbol is used on corridors leading to the laboratories.", "يُستخدم رمز الخطر الحيوي على الممرات المؤدية إلى المختبرات.", "T"),
 ("Pencils and labels may be placed in the mouth after removing the gloves.", "يجوز وضع الأقلام والملصقات في الفم بعد خلع القفازات.", "F"),
 ("Lab glassware can be used as food or water containers if it is clean.", "يمكن استخدام الأدوات الزجاجية المختبرية أوعيةً للطعام أو الماء إذا كانت نظيفة.", "F"),
 ("Cultures may be taken out of the lab if there is a good reason.", "يجوز إخراج المزارع من المختبر إذا وُجد سبب وجيه.", "F"),
 ("Hands should be washed after working with infectious materials.", "يجب غسل اليدين بعد العمل مع المواد المُعدية.", "T"),
 ("Disinfection destroys bacterial spores.", "التطهير يدمّر الأبواغ البكتيرية.", "F"),
 ("Antiseptics are chemicals applied to body surfaces.", "المطهّرات الموضعية مواد كيميائية تُطبَّق على أسطح الجسم.", "T"),
 ("Decontamination is the complete killing of all living organisms.", "إزالة التلوّث هي القتل الكامل لجميع الكائنات الحية.", "F"),
 ("Bio risk assessment embraces biosafety risks and laboratory biosecurity risks.", "يشمل تقييم الخطر البيولوجي مخاطر السلامة الحيوية ومخاطر الأمن الحيوي المختبري.", "T"),
]

TRAPS = [
 ("*Salmonella spp.* and *Salmonella typhi* belong to the same risk group. Correct?", "تنتمي `*Salmonella spp.*` و`*Salmonella typhi*` إلى مجموعة الخطورة نفسها. هل هذا صحيح؟",
  "No. *Salmonella spp.* → Risk group 2; *Salmonella typhi* → Risk group 3.", "لا. `*Salmonella spp.*` ← المجموعة 2؛ `*Salmonella typhi*` ← المجموعة 3."),
 ("*E.coli* appears in two risk groups. Which ones, and why?", "تظهر `*E.coli*` في مجموعتَي خطورة. ما هما، ولماذا؟",
  "*E.coli* → Risk group 1; *E.coli* **pathogenic strain** → Risk group 2.", "`*E.coli*` ← المجموعة 1؛ **السلالة المُمرِضة** من `*E.coli*` ← المجموعة 2."),
 ("Disinfection and sterilization both kill bacterial spores. Correct?", "التطهير والتعقيم كلاهما يقتلان الأبواغ البكتيرية. هل هذا صحيح؟",
  "No. Sterilization kills **all** living organisms; disinfection does **not** kill bacterial spores.", "لا. التعقيم يقتل **جميع** الكائنات الحية؛ أما التطهير فلا يقتل الأبواغ البكتيرية."),
 ("Antiseptics are applied to lab benches and instruments. Correct?", "تُطبَّق المطهّرات الموضعية على طاولات المختبر والأدوات. هل هذا صحيح؟",
  "No. Antiseptics → **body surfaces**; disinfection → inanimate objects.", "لا. المطهّرات الموضعية ← **أسطح الجسم**؛ التطهير ← الأجسام غير الحيّة."),
 ("Decontamination removes all microbes. Correct?", "إزالة التلوّث تزيل جميع الميكروبات. هل هذا صحيح؟",
  "No. It is the mechanical removal of **most** microbes (washing, heat or disinfectants).", "لا. هي الإزالة الميكانيكية **لمعظم** الميكروبات (الغسل أو الحرارة أو المطهّرات)."),
 ("Biosafety levels aim to provide the highest exposure and the lowest protection. Correct?", "تهدف مستويات السلامة الحيوية إلى توفير أعلى تعرّض وأدنى حماية. هل هذا صحيح؟",
  "No — reversed. The aim is the **highest protection** and the **lowest exposure**.", "لا — العبارة معكوسة. الهدف **أعلى حماية** و**أدنى تعرّض**."),
 ("Theft and misuse are biosafety risks. Correct?", "السرقة وإساءة الاستخدام من مخاطر السلامة الحيوية. هل هذا صحيح؟",
  "No. They are **laboratory biosecurity** risks; biosafety risks are risks of accidental infection.", "لا. هي من مخاطر **الأمن الحيوي المختبري**؛ أما مخاطر السلامة الحيوية فهي مخاطر العدوى العَرَضية."),
 ("Contaminated waste is discarded first and then disinfected. Correct?", "تُرمى النفايات الملوّثة أولًا ثم تُطهَّر. هل هذا صحيح؟",
  "No. Waste is disinfected **before discarding**; instruments are disinfected **immediately after use**.", "لا. تُطهَّر النفايات **قبل التخلّص منها**؛ وتُطهَّر الأدوات **فور استخدامها**."),
]

IMPQ = [
 ("Define biosafety levels and state their aim.", "عرّف مستويات السلامة الحيوية واذكر هدفها.",
  "Principles and application used to protect laboratory workers and the surrounding environment from exposure to danger while working with living organisms. Aim: the highest level of protection and the lowest range of exposure.",
  "مبادئ وتطبيقات لحماية العاملين في المختبر والبيئة المحيطة من التعرّض للخطر أثناء العمل مع الكائنات الحية. الهدف: أعلى مستوى من الحماية وأدنى مدى من التعرّض."),
 ("What are risk groups? List the four groups with their examples.", "ما مجموعات الخطورة؟ عدّد المجموعات الأربع مع أمثلتها.",
  "Used to assess risk, determine its source and how to deal with it. RG1 minimal (*E.coli*, *Bacillus Subtilis*); RG2 moderate (*E.coli* pathogenic strain, *Brucella spp.*, *Salmonella spp.*); RG3 high (*Salmonella typhi*, *Mycobacterium tuberculosis*); RG4 extreme.",
  "تُستخدم لتقييم الخطر وتحديد مصدره وكيفية التعامل معه. المجموعة 1 ضئيلة؛ المجموعة 2 متوسطة؛ المجموعة 3 عالية؛ المجموعة 4 قصوى (مع الأمثلة المذكورة)."),
 ("Compare Risk group 2 and Risk group 3.", "قارن بين مجموعة الخطورة 2 ومجموعة الخطورة 3.",
  "RG2: moderate risk, related to human infection, treatment is possible, limited risk of spread. RG3: high risk, serious and fatal infections, treatment is not easy, especially for immunosuppressed persons.",
  "المجموعة 2: خطورة متوسطة، عدوى للإنسان، العلاج ممكن، انتشار محدود. المجموعة 3: خطورة عالية، عدوى خطيرة ومميتة، العلاج ليس سهلًا خصوصًا للمثبَّطة مناعتهم."),
 ("What is the biohazard symbol used for? Give three examples.", "لِمَ يُستخدم رمز الخطر الحيوي؟ أعطِ ثلاثة أمثلة.",
  "To warn people of the potential presence of dangerous biological materials: cultures of pathogens; human blood and tissue; corridors leading to the laboratories.",
  "لتحذير الأشخاص من احتمال وجود مواد بيولوجية خطرة: مزارع المُمرِضات؛ دم الإنسان وأنسجته؛ الممرات المؤدية إلى المختبرات."),
 ("List the eight laboratory safety considerations.", "عدّد اعتبارات السلامة الثمانية في المختبر.",
  "Protective clothing; avoid touching objects with gloves and never place items in the mouth; no eating/drinking and no glassware as food containers; tie long hair; no cultures out of the lab; wash hands; disinfect instruments after use; disinfect waste before discarding.",
  "الملابس الواقية؛ عدم لمس الأشياء بالقفازات وعدم وضع شيء في الفم؛ عدم الأكل والشرب؛ ربط الشعر الطويل؛ عدم إخراج المزارع؛ غسل اليدين؛ تطهير الأدوات فور الاستخدام؛ تطهير النفايات قبل التخلّص منها."),
 ("Define: sterilization, disinfection, antiseptics and decontamination.", "عرّف: التعقيم، التطهير، المطهّرات الموضعية، إزالة التلوّث.",
  "See the four definitions in the booklet (Section 5) — key words: all organisms / not bacterial spores, inanimate objects / body surfaces / mechanical removal of most microbes.",
  "راجع التعاريف الأربعة في الملزمة (القسم 5) — الكلمات المفتاحية: جميع الكائنات / ليس الأبواغ البكتيرية، الأجسام غير الحيّة / أسطح الجسم / إزالة ميكانيكية لمعظم الميكروبات."),
 ("Define: biological laboratory, bio risk and bio risk assessment.", "عرّف: المختبر البيولوجي، الخطر البيولوجي، تقييم الخطر البيولوجي.",
  "See Section 6 of the booklet — facility for collecting/handling/storing microorganisms; probability of an adverse event leading to harm; process to identify acceptable and unacceptable risks and their consequences.",
  "راجع القسم 6 من الملزمة — منشأة لجمع الكائنات الدقيقة والتعامل معها وتخزينها؛ احتمال حدث ضار يؤدي إلى الضرر؛ عملية تحديد المخاطر المقبولة وغير المقبولة وعواقبها."),
 ("Differentiate between biosafety risks and laboratory biosecurity risks.", "فرّق بين مخاطر السلامة الحيوية ومخاطر الأمن الحيوي المختبري.",
  "Biosafety risks: risks of accidental infection. Biosecurity risks: unauthorized access, loss, theft, misuse, diversion or intentional release.",
  "مخاطر السلامة الحيوية: العدوى العَرَضية. مخاطر الأمن الحيوي: الوصول غير المصرَّح به، الفقدان، السرقة، إساءة الاستخدام، التحويل أو الإطلاق المتعمَّد."),
]

# ---------------------------------------------------------------- renderers
def mcq_html(i, q):
    qe, qa, opts, _ = q
    o = "".join(f'<div class="opt"><span class="l">{l}</span>{en(e)}{ar(a) if a != e else "<p></p>"}</div>'
                for l, (e, a) in zip("abcd", opts))
    return f'<div class="q"><div class="qh"><span class="qn">Q{i}</span><div class="qt">{en(qe)}{ar(f"س{ard(i)}. " + qa)}</div></div><div class="opts">{o}</div></div>'

def tf_html(i, t):
    return (f'<div class="tf"><span class="qn">{i}</span><div class="qt">{en(t[0])}{ar(t[1])}</div>'
            f'<div class="tfbox" dir="ltr"><span><b>T</b><em>صح</em></span><span><b>F</b><em>خطأ</em></span></div></div>')

def trap_html(i, t):
    return f'<div class="q"><div class="qh"><span class="qn">{i}</span><div class="qt">{en(t[0])}{ar(t[1])}</div></div></div>'

def imp_html(i, t):
    return f'<div class="q"><div class="qh"><span class="qn">{i}</span><div class="qt">{en(t[0])}{ar(t[1])}</div></div><div class="ans-lines"></div></div>'

HDR = (f'<div class="hdr"><span class="h-en" dir="ltr">{SUBJ_EN}</span>'
       f'<span class="chip">Exam &amp; Questions · بنك الأسئلة</span>'
       f'<span class="h-ar" dir="rtl">{SUBJ_AR}</span></div>')
FL = "Lab 1 · " + TITLE_EN
FR = "المختبر ١ · " + TITLE_AR

def cover():
    return f'''<section class="page cover cv2">
<div class="cv-top">{grid(color="rgba(255,255,255,.22)", label_color="rgba(255,255,255,.6)")}</div>
<div class="cv-bot">{grid(color="rgba(156,111,179,.18)", rows=3, letters="DEF", label_color="rgba(156,111,179,.5)")}</div>
<div class="cv-logo-badge"><img src="assets/logo.png"></div>
<div class="cv-chip"><span>Lab 1</span><span class="tri"></span></div>
<div class="cv-ar" dir="rtl">بنك الأسئلة<br>والمراجعة</div>
<div class="cv-badge"><span>MCQ · True/False · Traps</span><span class="w">Answer Key</span></div>
<div class="cv-en"><small>Exam &amp; Questions</small>{TITLE_EN}</div>
<div class="cv-art">{emblem(c_ring=("#FFFFFF", "#FCFDC8", "#4C9DB0", "#6E4483"), agar="#FCFDC8", streak="#4C9DB0", colony="#C69FD5", bug="#6E4483", seed=11)}</div>
<div class="cv-info">
  <div class="cv-subj">{SUBJ_EN}</div>
  <div class="cv-subj-ar" dir="rtl">{SUBJ_AR}</div>
  <div class="cv-rows">
    <div class="cv-row"><span class="k">Stage</span><span class="v">The fourth stage</span><span class="va">المرحلة الرابعة</span></div>
    <div class="cv-row"><span class="k">Lab</span><span class="v">Lab: 1</span><span class="va">المختبر: ١</span></div>
    <div class="cv-row"><span class="k">Type</span><span class="v">Practical</span><span class="va">عملي</span></div>
  </div>
</div>
<div class="cv-foot"><span>{len(MCQ)} MCQs · {len(TF)} True/False · {len(TRAPS)} Exam Traps · {len(IMPQ)} Important Questions</span>
<span class="sw"><i style="background:#C69FD5"></i><i style="background:#FCFDC8"></i><i style="background:#FFEBAF"></i><i style="background:#4C9DB0"></i></span></div>
</section>'''

def ka(num, e, a, q=None):
    qh = f'<div class="kq2">{md(q)}</div>' if q else ""
    return f'<div class="ka"><span class="kn">{num}</span><div>{qh}{en(e)}{ar(a)}</div></div>'

def key_blocks():
    mk = '<div class="key">' + "".join(f'<div><b>{i}</b><span>{q[3].upper()}</span></div>' for i, q in enumerate(MCQ, 1)) + "</div>"
    tk = '<div class="key">' + "".join(f'<div><b>{i}</b><span>{"True" if t[2] == "T" else "False"}</span></div>' for i, t in enumerate(TF, 1)) + "</div>"
    out = [h2("MCQ Answers", "إجابات الاختيار من متعدد") + mk, h2("True / False Answers", "إجابات صح أو خطأ") + tk]
    for i, t in enumerate(TRAPS, 1):
        out.append((h2("Exam Traps Answers", "إجابات المقالب") if i == 1 else "") + ka(i, t[2], t[3]))
    for i, t in enumerate(IMPQ, 1):
        out.append((h2("Important Questions — model answers", "أهم الأسئلة — إجابات نموذجية") if i == 1 else "") + ka(i, t[2], t[3], t[0]))
    return out

def chunks(items, sizes):
    out, k = [], 0
    for s in sizes:
        out.append(items[k:k + s]); k += s
    assert k == len(items), (k, len(items))
    return out

def build(sz):
    pages = [cover()]
    n = 1
    def add(html_):
        nonlocal n
        n += 1
        pages.append(page(html_, HDR, FL, FR, n, notes=False).replace('class="page"', 'class="page exam"'))
    k = 0
    for j, ch in enumerate(chunks(MCQ, sz["mcq"])):
        head = sec("A", "Comprehensive MCQs", "أسئلة اختيار من متعدد شاملة", "📝") if j == 0 else h2("Comprehensive MCQs (continued)", "أسئلة الاختيار من متعدد (تتمة)")
        add(head + "".join(mcq_html(k + i + 1, q) for i, q in enumerate(ch))); k += len(ch)
    k = 0
    for j, ch in enumerate(chunks(TF, sz["tf"])):
        head = sec("B", "True / False", "صح أو خطأ", "✔️") if j == 0 else h2("True / False (continued)", "صح أو خطأ (تتمة)")
        add(head + "".join(tf_html(k + i + 1, t) for i, t in enumerate(ch))); k += len(ch)
    k = 0
    for j, ch in enumerate(chunks(TRAPS, sz["trap"])):
        head = (sec("C", "Exam Traps", "المقالب والأسئلة الخادعة", "⚠️")
                + box("alert", pair("Read each statement carefully — every one hides a small but important detail from the lecture.",
                                    "اقرأ كل عبارة بعناية — كل واحدة تخفي تفصيلًا صغيرًا لكنه مهم من المحاضرة."))) if j == 0 else h2("Exam Traps (continued)", "المقالب (تتمة)")
        add(head + "".join(trap_html(k + i + 1, t) for i, t in enumerate(ch))); k += len(ch)
    k = 0
    for j, ch in enumerate(chunks(IMPQ, sz["imp"])):
        head = sec("D", "Important Questions", "أهم الأسئلة للمراجعة", "⭐") if j == 0 else h2("Important Questions (continued)", "أهم الأسئلة (تتمة)")
        add(head + "".join(imp_html(k + i + 1, t) for i, t in enumerate(ch))); k += len(ch)
    # answer key (auto-packed)
    kb = key_blocks()
    k = 0
    for j, cnt in enumerate(sz["key"]):
        head = sec("✓", "Answer Key", "الحلول", "🔑") if j == 0 else h2("Answer Key (continued)", "الحلول (تتمة)")
        add(head + "".join(kb[k:k + cnt])); k += cnt
    return pages

if __name__ == "__main__":
    import json
    SIZES = json.load(open("sizes.json"))
    pages = build(SIZES)
    open("exam.html", "w").write(doc("Biosafety Exam", pages, COVER_CSS + EXAM_CSS))
    print("pages", len(pages))
