# BIOS — مناعة نظري المحاضرة الثالثة (Ankylosing spondylitis + Psoriatic Arthritis) — د. عبير، المرحلة الرابعة
# المصدر: Clinical Immunology - Lec 1-6.pdf (الصفحات 14–17 حتى «Lecture No. 4»؛ الملف في مجلد المحاضرة 1).
# كل جملة منقولة حرفيًا ومترجمة؛ بلا تصحيح إملائي. شكل «Main Features of Psoriatic Arthritis» نصّه صورة فنُقل جدولًا بنفس الكلمات.
import json, os, random
from collections import Counter

def C(en, ar, **k):  return dict(t="card", en=en, ar=ar, **k)
def SEC(en, ar):     return dict(t="section", en=en, ar=ar)
def H2(en, ar):      return dict(t="h2", en=en, ar=ar)
def L(en_items, ar_items, en="", ar="", **k):
    return dict(t="card", en=en, ar=ar, list_en=en_items, list_ar=ar_items, **k)
def T(head, rows, **k): return dict(t="table", head=head, rows=rows, **k)
def F(src, en, ar, **k): return dict(t="figure", src="assets/" + src, en=en, ar=ar, **k)
def TF(en, ar, a): return dict(en=en, ar=ar, answer=a)
def TR(en, ar, ae, aa): return dict(en=en, ar=ar, answer_en=ae, answer_ar=aa)
IM = TR

def split_cards(blocks, n=2):
    """Long multi-sentence cards become cards of n sentences each, so pages fill evenly (no text dropped)."""
    out = []
    for b in blocks:
        if b.get("t") == "card" and isinstance(b.get("en"), list) and len(b["en"]) > n + 1 and "list_en" not in b:
            for i in range(0, len(b["en"]), n):
                out.append(dict(t="card", en=b["en"][i:i + n], ar=b["ar"][i:i + n]))
        else:
            out.append(b)
    return out

blocks = [
 SEC("Ankylosing spondylitis", "التهاب الفقار المقسِّط"),
 C(["The term spondyloarthritis (SpA) (otherwise known as spondyloarthropathy) encompasses a heterogeneous group of inflammatory diseases characterized by spinal and peripheral joint oligoarthritis, inflammation of the attachments of ligaments and tendons to bones (enthesitis) and, at times, mucocutaneous, ocular, and/or cardiac manifestations.",
    "These disorders show familial aggregation and are typically associated with genes of the major histocompatibility complex (MHC), particularly human leukocyte antigen (HLA)-B27"],
   ["يشمل مصطلح **التهاب الفقار والمفاصل** (`SpA`) (ويُعرف أيضًا باعتلال الفقار والمفاصل) مجموعة **غير متجانسة** من الأمراض الالتهابية، تتميّز بـ **التهاب قليل المفاصل** في العمود الفقري والمفاصل المحيطية، و**التهاب مواضع ارتكاز الأربطة والأوتار على العظام** (`enthesitis`)، وأحيانًا بمظاهر جلدية مخاطية أو عينية و/أو قلبية.",
    "وتُظهر هذه الاضطرابات **تجمّعًا عائليًا**، وترتبط عادةً بجينات **معقّد التوافق النسيجي الكبير** (`MHC`)، ولا سيّما **مستضدّ الكريات البيض البشري `HLA-B27`**"]),
 L(["ankylosing spondylitis (AS);",
    "reactive arthritis (ReA)— known previously as Reiter’s syndrome;",
    "psoriatic arthritis (PsA) and/or spondylitis;",
    "enteropathic arthritis and/or spondylitis associated with the inflammatory bowel diseases (IBD), ulcerative colitis (UC), or Crohn’s disease; and",
    "undifferentiated SpA, which encompasses patients expressing elements of, but failing to fulfill, accepted criteria for one of the above diseases."],
   ["**التهاب الفقار المقسِّط** (`AS`)؛",
    "**التهاب المفاصل التفاعلي** (`ReA`) — المعروف سابقًا باسم **متلازمة رايتر**؛",
    "**التهاب المفاصل الصدفي** (`PsA`) و/أو التهاب الفقار؛",
    "التهاب المفاصل و/أو الفقار **المعوي** المرتبط بأمراض الأمعاء الالتهابية (`IBD`)، أو التهاب القولون التقرّحي (`UC`)، أو داء كرون؛",
    "**التهاب الفقار والمفاصل غير المميَّز**، الذي يشمل مرضى يُظهرون عناصر أحد الأمراض السابقة دون أن يستوفوا معاييره المقبولة."],
   en="The SpA include:", ar="تشمل أمراض `SpA`:"),
 C("In addition, isolated acute anterior uveitis (AAU)1 and spondylitic heart disease (complete heart block and/or lone aortic regurgitation) associated with HLA-B27 may also be classified within the spectrum of SpA.",
   "إضافةً إلى ذلك، قد يُصنَّف **التهاب العنبية الأمامي الحادّ المعزول** (`AAU`) و**مرض القلب الفقاري** (حصار القلب التامّ و/أو قلس الأبهر المنفرد) المرتبطان بـ `HLA-B27` ضمن طيف `SpA` أيضًا."),
 C(["Ankylosing spondylitis (AS) is a chronic inflammatory condition of the spine and sacroiliac joints.",
    "It is progressive disease in which restriction of movement is associated with intervertebral ossification of the ligaments.",
    "Men, usually below the age of 40, man develop the disease three times more frequently than women.",
    "Approximately 90% of the patients are HLA-B\\*27 positive, while the prevalence of this antigen in the general population is 7%.",
    "Of all the adult HLA-B\\*27- positive individuals, 1-2% have ankylosing spondylitis."],
   ["**التهاب الفقار المقسِّط** (`AS`) حالة التهابية مزمنة تصيب **العمود الفقري والمفصلين العجزيين الحرقفيين**.",
    "وهو مرض **متقدّم** يرتبط فيه تقييد الحركة **بتعظّم الأربطة بين الفقرات**.",
    "ويُصاب الرجال، عادةً **دون سنّ الأربعين**، بالمرض **ثلاثة أضعاف** النساء.",
    "ونحو **90%** من المرضى موجبو **`HLA-B*27`**، بينما يبلغ انتشار هذا المستضدّ في عموم السكان **7%**.",
    "ومن بين جميع البالغين موجبي `HLA-B*27`، يُصاب **1–2%** بالتهاب الفقار المقسِّط."]),

 H2("Etiology of AS", "سببيات التهاب الفقار المقسِّط"),
 C(["The etiology of the disease is unknown, but persistence of specific antigens of the infecting organisms has been demonstrated in these patients.",
    "This has led to suggestion that AS is also triggered by infection (possibly in the gastrointestinal tract) in susceptible HLA-B\\*27- positive individuals.",
    "Inflammation occurs and persists in different organs and joints in Ankylosing Spondylitis.",
    "Each individual tends to have their own unique pattern of presentation and activity of the illness.",
    "The initial inflammation may be a result of an activation of body's immune system, perhaps by a preceding bacterial infection or a combination of infectious microbes.",
    "Once activated, the body's immune system becomes unable to turn itself off, even though the initial bacterial infection may have long subsided.",
    "Chronic tissue inflammation resulting from the continued activation of the body's own immune system in the absence of active infection is the hallmark of an inflammatory autoimmune disease."],
   ["سبب المرض **غير معروف**، لكن ثبت **استمرار وجود مستضدّات نوعية للكائنات المُعدية** لدى هؤلاء المرضى.",
    "وقد أدّى ذلك إلى اقتراح أن المرض **يُحفَّز بعدوى** (ربما في **القناة الهضمية**) لدى الأفراد المستعدّين موجبي `HLA-B*27`.",
    "ويحدث الالتهاب ويستمرّ في أعضاء ومفاصل مختلفة في هذا المرض.",
    "ولكل فرد **نمطه الفريد** في ظهور المرض ونشاطه.",
    "وقد يكون الالتهاب الأولي نتيجة **تنشيط الجهاز المناعي**، ربما بعدوى بكتيرية سابقة أو بمجموعة من الميكروبات المُعدية.",
    "وبعد تنشيطه، يصبح الجهاز المناعي **عاجزًا عن إيقاف نفسه**، حتى لو كانت العدوى البكتيرية الأولى قد زالت منذ زمن.",
    "و**الالتهاب النسيجي المزمن** الناتج عن استمرار تنشيط الجهاز المناعي **في غياب عدوى نشطة** هو السمة المميّزة **للمرض الالتهابي المناعي الذاتي**."]),

 H2("Clinical features", "المظاهر السريرية"),
 C(["The onset of AS tends to be insidious with a dull lumbar pain; this persists over 3 months and is accompanied by morning stiffness relieved by exercise.",
    "Arthritis of the peripheral joints is seen in one third of the patients.",
    "Amongst extrarticular manifestation, iritis is the most troublesome: it tends to be unilateral and accompanied by photophobia pain.",
    "Inflammation of the colon and ileum is frequent but usually asymptomatic."],
   ["يكون بدء المرض **خفيًّا** مع **ألم قطني كليل** يستمرّ **أكثر من 3 أشهر** ويرافقه **تيبّس صباحي يخفّ بالتمرين**.",
    "ويُرى التهاب المفاصل المحيطية لدى **ثلث** المرضى.",
    "ومن بين المظاهر خارج المفصلية يُعدّ **التهاب القزحية** الأكثر إزعاجًا: فهو يميل إلى أن يكون **أحادي الجانب** ويرافقه ألم **رهاب الضوء**.",
    "و**التهاب القولون واللفائفي** شائع لكنه عادةً **بلا أعراض**."]),

 H2("Criteria of AS Classification", "معايير تصنيف التهاب الفقار المقسِّط"),
 C("**Inflammatory Spinal Pain**: History or present symptoms of spinal pain in back, dorsal or cervical region with at least 4 of the following: **A.** Onset at age < 45 years. B. Insidious onset. **C.** Improved by exercise. **D.** Associated with morning stiffness **E.** at least for 3 months duration",
   "**ألم العمود الفقري الالتهابي:** تاريخ أو أعراض حالية لألم العمود الفقري في الظهر أو المنطقة الظهرية أو الرقبية، مع **4 على الأقل** ممّا يأتي: **أ.** البدء قبل عمر 45 سنة. ب. البدء الخفيّ. **ج.** التحسّن بالتمرين. **د.** ارتباطه بالتيبّس الصباحي **هـ.** مدّة 3 أشهر على الأقل"),
 L(["Positive family history", "Psoriasis", "Inflammatory bowel disease.", "Alternating buttock pain.", "Enthesopathy", "Acute diarrhea", "Urithritis", "Sacroiliiatis"],
   ["قصة عائلية إيجابية", "الصدفية", "مرض الأمعاء الالتهابي.", "ألم الأليتين المتناوب.", "اعتلال مواضع الارتكاز", "الإسهال الحادّ", "التهاب الإحليل (`Urithritis`)", "التهاب المفصل العجزي الحرقفي (`Sacroiliiatis`)"],
   en="**Synovitis**: Asymmetric or Predominantly in the lower limbs. and one of the followings:",
   ar="**التهاب الغشاء الزليلي:** غير متناظر أو يغلب في الطرفين السفليين، **مع واحد** ممّا يأتي:"),

 H2("The diagnosis of Ankylosing Spondylitis is based on:", "يعتمد تشخيص التهاب الفقار المقسِّط على:"),
 L(["Evaluating the patient's symptoms include pain and morning stiffness of the spine and sacral areas with or without accompanying inflammation in other joints, tendons, and organs.",
    "A physical examination: the Schober's test is a useful clinical measure of flexion of the lumbar spine performed during examination. Flexibility of the low back and/or neck can be decreased.",
    "X-ray findings",
    "Blood tests: Patients with AS tend to have elevated levels of IgA and, when the disease is active, elevated erythrocyte sedimentation rates and levels of C-reactive protein. Rheumatoid factor and antinuclear antibody are consistently negative. The clinical need to assess the HLA-B\\*27 status of a patient with symptoms and signs of AS is controversial."],
   ["تقييم أعراض المريض، وتشمل ألم العمود الفقري والمنطقة العجزية وتيبّسهما الصباحي، مع التهاب مرافق في مفاصل وأوتار وأعضاء أخرى أو بدونه.",
    "الفحص السريري: **اختبار شوبر** (`Schober's test`) مقياس سريري مفيد **لانثناء العمود الفقري القطني** يُجرى أثناء الفحص. وقد تقلّ مرونة أسفل الظهر و/أو الرقبة.",
    "نتائج **الأشعة السينية**",
    "فحوص الدم: يميل المرضى إلى **ارتفاع مستويات `IgA`**، وعند نشاط المرض **ترتفع سرعة الترسيب والبروتين المتفاعل-سي**. ويكون **العامل الروماتويدي والضدّ المضادّ للنواة سالبين دائمًا**. أمّا الحاجة السريرية لتقييم حالة `HLA-B*27` لدى مريض بأعراض المرض وعلاماته **فمثار جدل**."]),

 SEC("Psoriatic Arthritis", "التهاب المفاصل الصدفي"),
 C(["Psoriatic Arthritis (PsA) is a chronic and inflammatory arthritis in association with skin psoriasis, characterized by osteolysis and bony proliferation.",
    "PsA is classified as one of the subtypes of spondyloarthropathies.",
    "Males and females are equally affected.",
    "PsA can range from mild nondestructive disease to a severely rapid and destructive arthropathy."],
   ["**التهاب المفاصل الصدفي** (`PsA`) التهاب مفاصل مزمن **مرتبط بصدفية الجلد**، ويتميّز **بانحلال العظم وتكاثر العظم**.",
    "ويُصنَّف `PsA` بوصفه أحد الأنواع الفرعية **لاعتلالات الفقار والمفاصل**.",
    "ويُصاب **الذكور والإناث بالتساوي**.",
    "ويتراوح `PsA` بين مرض خفيف غير مدمّر واعتلال مفصلي **سريع شديد ومدمّر**."]),
 C("**Clinical manifestations** include skin and nail psoriasis, dactylitis, enthesitis, osteoperiostitis, large joint oligoarthritis, arthritis mutilans, sacroiliitis, spondylitis and distal interphalangeal arthritis.",
   "تشمل **المظاهر السريرية**: صدفية الجلد والأظافر، و**التهاب الإصبع** (`dactylitis`)، والتهاب مواضع الارتكاز، والتهاب العظم والسمحاق، والتهاب قليل المفاصل الكبيرة، و**التهاب المفاصل المشوِّه** (`arthritis mutilans`)، والتهاب المفصل العجزي الحرقفي، والتهاب الفقار، و**التهاب المفاصل بين السلاميات البعيدة**."),
 F("psa-photos.jpg", "Clinical pictures of psoriatic arthritis (hands, toes, skin psoriasis, heels)",
   "صور سريرية لالتهاب المفاصل الصدفي (اليدان، أصابع القدم، صدفية الجلد، العقبان)", h="70mm", fit="contain", nonum=True),
 L(["Ocular inflammation (Iritis/Uveitis/ Episcleritis).",
    "Irritable bowel disease (IBD).",
    "Metabolic Syndrome (Hyperlipidemia, Hypertension, Insulin resistent, Diabetes,Obesity ) lead to Higher risk of Cardiovascular disease (CVD)",
    "Psychosocial burden, Reactive depression, Higher suicidal ideation and Alcoholism."],
   ["**الالتهاب العيني** (التهاب القزحية/العنبية/الصلبة الظاهرة).",
    "مرض الأمعاء (`IBD`).",
    "**المتلازمة الأيضية** (فرط شحوم الدم، وارتفاع ضغط الدم، ومقاومة الإنسولين، والسكري، والسمنة) تؤدّي إلى **خطر أعلى لأمراض القلب والأوعية** (`CVD`)",
    "العبء النفسي الاجتماعي، والاكتئاب التفاعلي، وارتفاع الأفكار الانتحارية، والإدمان على الكحول."],
   en="**Comorbidities in PsA Patients**", ar="**الأمراض المصاحبة لدى مرضى التهاب المفاصل الصدفي**"),
 C(["Two percent of patients with psoriasis develop psoriatic arthropathy; this may affect the peripheral joints or the spine.",
    "The psoriasis generally precedes the arthritis by many years; in rare cases where the arthritis comes first, diagnosis may be difficult.",
    "A family history of psoriasis is a helpful diagnostic clue and the characteristic nail changes of psoriasis are present in 80% of patients with psoriatic arthritis.",
    "Dactylitis – inflammation of an entire digit to look like a sausage – is a distinctive feature.",
    "Usually rheumatoid factor (RF) negative and ACPA negative.",
    "Radiographic damage can be noted in up to 47% of patients at a median interval of two years despite clinical improvement with standard DMARD therapy.",
    "Treatment is similar to that for RA, including the use of anti- TNF drugs.",
    "The prognosis is usually good, although severe joint destruction can occur."],
   ["يُصاب **2%** من مرضى الصدفية باعتلال المفاصل الصدفي، وقد يصيب المفاصل المحيطية أو العمود الفقري.",
    "وعادةً **تسبق الصدفيةُ التهابَ المفاصل بسنوات كثيرة**؛ وفي الحالات النادرة التي يأتي فيها التهاب المفاصل أولًا قد يصعب التشخيص.",
    "و**القصة العائلية للصدفية** دليل تشخيصي مفيد، و**تغيّرات الأظافر** المميّزة للصدفية موجودة لدى **80%** من المرضى.",
    "و**التهاب الإصبع** — التهاب الإصبع كلّه فيبدو **كالنقانق** — سمة مميّزة.",
    "ويكون عادةً **سالب العامل الروماتويدي** (`RF`) و**سالب `ACPA`**.",
    "ويمكن ملاحظة **ضرر شعاعي لدى ما يصل إلى 47%** من المرضى بعد فترة وسطية قدرها سنتان، رغم التحسّن السريري بالعلاج القياسي بالأدوية المعدِّلة للمرض (`DMARD`).",
    "والعلاج **مشابه لعلاج التهاب المفاصل الروماتويدي**، بما في ذلك استعمال **مضادّات `TNF`**.",
    "والإنذار جيد عادةً، مع أن تدميرًا شديدًا للمفاصل قد يحدث."]),
 H2("Figure: Main Features of Psoriatic Arthritis", "الشكل: السمات الرئيسة لالتهاب المفاصل الصدفي"),
 T(["Clinical", "Laboratory", "Radiographic", "الترجمة"],
   [["Psoriasis of skin and nails", "Rheumatoid factor (RF) & Anti-citrullinated protein antibodies (ACPA) negative\\*", "Erosions and resorptions",
     "**سريري:** صدفية الجلد والأظافر — **مختبري:** سالب `RF` و`ACPA`\\* — **شعاعي:** تآكلات وارتشافات"],
    ["Peripheral arthritis", "Elevated Acute Phase\\*\\*", "Joint space narrowing or involvement of entheseal sites",
     "**سريري:** التهاب المفاصل المحيطية — **مختبري:** ارتفاع بروتينات الطور الحادّ\\*\\* — **شعاعي:** تضيّق المسافة المفصلية أو إصابة مواضع الارتكاز"],
    ["Distal interphalangeal (DIP) involvement", "", "New bone growth at the enthesis",
     "**سريري:** إصابة المفاصل بين السلاميات البعيدة (`DIP`) — **شعاعي:** نموّ عظم جديد عند موضع الارتكاز"],
    ["Dactylitis", "", "Syndesmophytes\\*\\*\\*", "**سريري:** التهاب الإصبع — **شعاعي:** النوابت العظمية الرباطية\\*\\*\\*"],
    ["Enthesopathy", "", "Sacroiliitis\\*\\*\\*", "**سريري:** اعتلال مواضع الارتكاز — **شعاعي:** التهاب المفصل العجزي الحرقفي\\*\\*\\*"]],
   ar_cols=[3], widths=["20%", "22%", "20%", "38%"]),
]
blocks = split_cards(blocks)

# ---------------------------------------------------------------- questions (lecture content only)
LET = list("abcd") * 7
random.Random(33).shuffle(LET)
_n = [0]
def Q(en, ar, right, wrong, **k):
    ans = LET[_n[0]]; _n[0] += 1
    opts = list(wrong); opts.insert("abcd".index(ans), right)
    return dict(en=en, ar=ar, options=[list(o) for o in opts], answer=ans, **k)

mcq = [
 {"topic_en": "Spondyloarthritis and ankylosing spondylitis", "topic_ar": "التهاب الفقار والمفاصل والتهاب الفقار المقسِّط"},
 Q("Inflammation of the attachments of ligaments and tendons to bones is called:", "التهاب مواضع ارتكاز الأربطة والأوتار على العظام يُسمّى:",
   ("Enthesitis", "التهاب مواضع الارتكاز"), [("Dactylitis", "التهاب الإصبع"), ("Synovitis", "التهاب الغشاء الزليلي"), ("Iritis", "التهاب القزحية")]),
 Q("Spondyloarthritis disorders are typically associated with:", "ترتبط أمراض التهاب الفقار والمفاصل عادةً بـ:",
   ("HLA-B27", "`HLA-B27`"), [("HLA-DR4", "`HLA-DR4`"), ("HLA-DR2/DR3", "`HLA-DR2/DR3`"), ("HLA-A2", "`HLA-A2`")]),
 Q("Reactive arthritis was known previously as:", "كان التهاب المفاصل التفاعلي يُعرف سابقًا باسم:",
   ("Reiter’s syndrome", "متلازمة رايتر"), [("Sjögren’s syndrome", "متلازمة شوغرن"), ("CREST syndrome", "متلازمة `CREST`"), ("Crohn’s disease", "داء كرون")]),
 Q("Ankylosing spondylitis is a chronic inflammatory condition of:", "التهاب الفقار المقسِّط حالة التهابية مزمنة تصيب:",
   ("The spine and sacroiliac joints", "العمود الفقري والمفصلين العجزيين الحرقفيين"),
   [("Small joints of the hands only", "مفاصل اليد الصغيرة فقط"), ("The kidneys", "الكليتين"), ("Lacrimal glands", "الغدد الدمعية")]),
 Q("In AS, restriction of movement is associated with:", "في التهاب الفقار المقسِّط يرتبط تقييد الحركة بـ:",
   ("Intervertebral ossification of the ligaments", "تعظّم الأربطة بين الفقرات"),
   [("Muscle atrophy only", "ضمور العضلات فقط"), ("Skin psoriasis", "صدفية الجلد"), ("Synovial fluid glucose", "غلوكوز السائل الزليلي")]),
 Q("AS develops in men, compared with women:", "يُصاب الرجال بالتهاب الفقار المقسِّط مقارنةً بالنساء:",
   ("Three times more frequently", "ثلاثة أضعاف"), [("Equally", "بالتساوي"), ("Nine times more", "تسعة أضعاف"), ("Less frequently", "أقل")]),
 Q("Approximately what percentage of AS patients are HLA-B\\*27 positive?", "نحو أيّ نسبة من مرضى التهاب الفقار المقسِّط موجبو `HLA-B*27`؟",
   ("90%", "90%"), [("7%", "7%"), ("30%", "30%"), ("1-2%", "1–2%")]),
 Q("The prevalence of HLA-B\\*27 in the general population is:", "انتشار `HLA-B*27` في عموم السكان:",
   ("7%", "7%"), [("90%", "90%"), ("47%", "47%"), ("80%", "80%")]),
 Q("Of all adult HLA-B\\*27-positive individuals, AS develops in:", "من بين جميع البالغين موجبي `HLA-B*27` يُصاب بالمرض:",
   ("1-2%", "1–2%"), [("50%", "50%"), ("90%", "90%"), ("25%", "25%")]),
 Q("AS is suggested to be triggered by infection possibly in:", "يُقترح أن المرض يُحفَّز بعدوى ربما في:",
   ("The gastrointestinal tract", "القناة الهضمية"), [("The skin", "الجلد"), ("The urinary bladder only", "المثانة فقط"), ("The eye", "العين")]),

 {"topic_en": "Clinical features, criteria and diagnosis of AS", "topic_ar": "المظاهر والمعايير وتشخيص التهاب الفقار المقسِّط"},
 Q("In AS, morning stiffness is:", "في التهاب الفقار المقسِّط يكون التيبّس الصباحي:",
   ("Relieved by exercise", "يخفّ بالتمرين"), [("Worsened by exercise", "يزداد بالتمرين"), ("Absent", "غائبًا"), ("Relieved only by rest", "يخفّ بالراحة فقط")]),
 Q("Arthritis of peripheral joints in AS is seen in:", "يُرى التهاب المفاصل المحيطية في المرض لدى:",
   ("One third of the patients", "ثلث المرضى"), [("All patients", "كل المرضى"), ("No patients", "لا أحد"), ("90% of patients", "90% من المرضى")]),
 Q("The most troublesome extra-articular manifestation of AS is:", "أكثر المظاهر خارج المفصلية إزعاجًا في المرض:",
   ("Iritis", "التهاب القزحية"), [("Malar rash", "الطفح الوجني"), ("Dry mouth", "جفاف الفم"), ("Nail pitting", "تنقّر الأظافر")]),
 Q("Inflammatory spinal pain criteria include onset at age:", "من معايير ألم العمود الفقري الالتهابي البدء قبل عمر:",
   ("< 45 years", "45 سنة"), [("< 15 years", "15 سنة"), ("> 60 years", "بعد 60 سنة"), ("> 80 years", "بعد 80 سنة")]),
 Q("Inflammatory spinal pain criteria require at least how many of the listed features?", "تتطلّب معايير ألم العمود الفقري الالتهابي كم سمة على الأقل؟",
   ("4", "4"), [("1", "1"), ("2", "2"), ("All 8", "الثماني كلّها")]),
 Q("Schober's test measures:", "يقيس اختبار شوبر:",
   ("Flexion of the lumbar spine", "انثناء العمود الفقري القطني"), [("Grip strength", "قوة القبضة"), ("Knee reflex", "منعكس الركبة"), ("Eye pressure", "ضغط العين")]),
 Q("Patients with AS tend to have elevated levels of:", "يميل مرضى التهاب الفقار المقسِّط إلى ارتفاع مستويات:",
   ("IgA", "`IgA`"), [("IgE", "`IgE`"), ("Rheumatoid factor", "العامل الروماتويدي"), ("ANA", "`ANA`")]),
 Q("In AS, rheumatoid factor and antinuclear antibody are:", "في المرض يكون العامل الروماتويدي والضدّ المضادّ للنواة:",
   ("Consistently negative", "سالبين دائمًا"), [("Always positive", "موجبين دائمًا"), ("High titre", "بعيار عالٍ"), ("Positive in 90%", "موجبين لدى 90%")]),

 {"topic_en": "Psoriatic arthritis", "topic_ar": "التهاب المفاصل الصدفي"},
 Q("Psoriatic arthritis is characterized by:", "يتميّز التهاب المفاصل الصدفي بـ:",
   ("Osteolysis and bony proliferation", "انحلال العظم وتكاثر العظم"), [("Butterfly rash", "الطفح الفراشي"), ("Dry eyes", "جفاف العينين"), ("Anti-dsDNA", "`anti-dsDNA`")]),
 Q("In PsA, males and females are affected:", "في التهاب المفاصل الصدفي يُصاب الذكور والإناث:",
   ("Equally", "بالتساوي"), [("Females 3:1", "الإناث 3:1"), ("Males 3:1", "الذكور 3:1"), ("Females 9:1", "الإناث 9:1")]),
 Q("What percentage of patients with psoriasis develop psoriatic arthropathy?", "ما نسبة مرضى الصدفية الذين يُصابون باعتلال المفاصل الصدفي؟",
   ("2%", "2%"), [("20%", "20%"), ("47%", "47%"), ("80%", "80%")]),
 Q("Characteristic nail changes of psoriasis are present in what percentage of PsA patients?", "تغيّرات الأظافر المميّزة للصدفية موجودة لدى أيّ نسبة من مرضى `PsA`؟",
   ("80%", "80%"), [("2%", "2%"), ("10%", "10%"), ("30%", "30%")]),
 Q("Inflammation of an entire digit to look like a sausage is:", "التهاب الإصبع كلّه حتى يبدو كالنقانق هو:",
   ("Dactylitis", "التهاب الإصبع"), [("Enthesitis", "التهاب مواضع الارتكاز"), ("Arthritis mutilans", "التهاب المفاصل المشوِّه"), ("Iritis", "التهاب القزحية")]),
 Q("In PsA, rheumatoid factor and ACPA are usually:", "في `PsA` يكون العامل الروماتويدي و`ACPA` عادةً:",
   ("Negative", "سالبين"), [("Strongly positive", "موجبين بقوّة"), ("Positive in 70%", "موجبين لدى 70%"), ("Not tested", "غير مفحوصين")]),
 Q("Radiographic damage in PsA can be noted in up to:", "يمكن ملاحظة الضرر الشعاعي في `PsA` لدى ما يصل إلى:",
   ("47% of patients", "47% من المرضى"), [("2% of patients", "2% من المرضى"), ("80% of patients", "80% من المرضى"), ("100% of patients", "100% من المرضى")]),
 Q("Treatment of PsA is similar to that for RA, including:", "علاج `PsA` مشابه لعلاج `RA`، ويشمل:",
   ("Anti-TNF drugs", "مضادّات `TNF`"), [("Antibiotics only", "المضادّات الحيوية فقط"), ("Insulin", "الإنسولين"), ("Antihistamines only", "مضادّات الهستامين فقط")]),
 Q("According to the PsA features figure, “Syndesmophytes” is a:", "حسب شكل سمات `PsA`، «النوابت العظمية الرباطية» سمة:",
   ("Radiographic feature", "شعاعية"), [("Clinical feature", "سريرية"), ("Laboratory feature", "مختبرية"), ("Comorbidity", "مرض مصاحب")]),
 Q("Which is listed among the comorbidities in PsA patients?", "أيّ ممّا يأتي من الأمراض المصاحبة لدى مرضى `PsA`؟",
   ("Metabolic syndrome", "المتلازمة الأيضية"), [("Hemophilia", "الناعور"), ("Sickle cell anemia", "فقر الدم المنجلي"), ("Malaria", "الملاريا")]),
]

tf = [
 TF("Spondyloarthritis disorders show familial aggregation.", "تُظهر أمراض التهاب الفقار والمفاصل تجمّعًا عائليًا.", "T"),
 TF("Enteropathic arthritis is associated with inflammatory bowel diseases.", "التهاب المفاصل المعوي يرتبط بأمراض الأمعاء الالتهابية.", "T"),
 TF("AS usually affects men above the age of 60.", "يصيب التهاب الفقار المقسِّط عادةً الرجال فوق 60 سنة.", "F"),
 TF("All HLA-B\\*27-positive individuals develop AS.", "كل موجبي `HLA-B*27` يُصابون بالمرض.", "F"),
 TF("In AS the immune system may stay active even after the initial infection has subsided.", "في المرض قد يبقى الجهاز المناعي نشطًا حتى بعد زوال العدوى الأولى.", "T"),
 TF("The onset of AS is usually sudden and acute.", "بدء التهاب الفقار المقسِّط عادةً مفاجئ وحادّ.", "F"),
 TF("Iritis in AS tends to be unilateral.", "التهاب القزحية في المرض يميل إلى أن يكون أحادي الجانب.", "T"),
 TF("Inflammation of the colon and ileum in AS is rare.", "التهاب القولون واللفائفي في المرض نادر.", "F"),
 TF("Rheumatoid factor is usually positive in AS.", "العامل الروماتويدي موجب عادةً في المرض.", "F"),
 TF("Assessing HLA-B\\*27 status in AS is controversial.", "تقييم حالة `HLA-B*27` في المرض مثار جدل.", "T"),
 TF("PsA is classified as one of the subtypes of spondyloarthropathies.", "يُصنَّف `PsA` ضمن اعتلالات الفقار والمفاصل.", "T"),
 TF("In PsA the arthritis usually precedes the psoriasis by many years.", "في `PsA` يسبق التهاب المفاصل الصدفيةَ عادةً بسنوات.", "F"),
 TF("Severe joint destruction can never occur in PsA.", "لا يمكن أن يحدث تدمير شديد للمفاصل في `PsA`.", "F"),
 TF("Elevated acute phase is a laboratory feature of PsA.", "ارتفاع الطور الحادّ سمة مختبرية لـ `PsA`.", "T"),
]

traps = [
 TR("HLA-B\\*27 is diagnostic of AS because 90% of patients carry it.", "`HLA-B*27` تشخيصي للمرض لأن 90% من المرضى يحملونه.",
    "No — it is also present in 7% of the general population and only 1-2% of positive adults have AS; assessing it is controversial.",
    "لا — يوجد أيضًا لدى 7% من عموم السكان، ولا يُصاب إلا 1–2% من البالغين الموجبين؛ وتقييمه مثار جدل."),
 TR("Morning stiffness in AS is relieved by rest.", "التيبّس الصباحي في المرض يخفّ بالراحة.",
    "No — it is relieved by exercise (and inflammatory spinal pain is improved by exercise).",
    "لا — يخفّ بالتمرين (وألم العمود الفقري الالتهابي يتحسّن بالتمرين)."),
 TR("AS patients have elevated IgG and positive ANA.", "مرضى التهاب الفقار المقسِّط لديهم `IgG` مرتفع و`ANA` موجبة.",
    "No — they tend to have elevated IgA; RF and ANA are consistently negative.",
    "لا — يميلون إلى ارتفاع `IgA`؛ و`RF` و`ANA` سالبان دائمًا."),
 TR("PsA, like RA, affects women more than men.", "`PsA` كالتهاب المفاصل الروماتويدي يصيب النساء أكثر.",
    "No — in PsA males and females are equally affected.",
    "لا — في `PsA` يُصاب الذكور والإناث بالتساوي."),
 TR("Dactylitis and enthesitis are the same thing.", "التهاب الإصبع والتهاب مواضع الارتكاز شيء واحد.",
    "No — dactylitis is inflammation of an entire digit (sausage digit); enthesitis is inflammation of the attachments of ligaments and tendons to bones.",
    "لا — التهاب الإصبع التهاب الإصبع كلّه (إصبع النقانق)؛ والتهاب مواضع الارتكاز التهاب ارتكاز الأربطة والأوتار على العظام."),
 TR("Clinical improvement on DMARDs means no radiographic damage in PsA.", "التحسّن السريري بالأدوية المعدِّلة يعني عدم وجود ضرر شعاعي في `PsA`.",
    "No — radiographic damage can be noted in up to 47% of patients at a median of two years despite clinical improvement.",
    "لا — يمكن ملاحظة ضرر شعاعي لدى ما يصل إلى 47% بعد سنتين وسطيًا رغم التحسّن السريري."),
]

important = [
 IM("Define spondyloarthritis and list its diseases.", "عرّف التهاب الفقار والمفاصل وعدّد أمراضه.",
    "A heterogeneous group of inflammatory diseases with spinal and peripheral joint oligoarthritis, enthesitis and at times mucocutaneous, ocular and/or cardiac manifestations, associated with HLA-B27. Includes AS, reactive arthritis (Reiter’s syndrome), psoriatic arthritis, enteropathic arthritis (IBD, UC, Crohn’s) and undifferentiated SpA.",
    "مجموعة غير متجانسة من الأمراض الالتهابية فيها التهاب قليل المفاصل الفقري والمحيطي، والتهاب مواضع الارتكاز، وأحيانًا مظاهر جلدية مخاطية أو عينية أو قلبية، وترتبط بـ `HLA-B27`. وتشمل: التهاب الفقار المقسِّط، والتهاب المفاصل التفاعلي (متلازمة رايتر)، والتهاب المفاصل الصدفي، والتهاب المفاصل المعوي (`IBD`، `UC`، كرون)، و`SpA` غير المميَّز."),
 IM("Define ankylosing spondylitis and mention its relation to HLA-B\\*27.", "عرّف التهاب الفقار المقسِّط واذكر علاقته بـ `HLA-B*27`.",
    "A chronic progressive inflammatory condition of the spine and sacroiliac joints with intervertebral ossification of ligaments; men below 40, 3 times more than women. About 90% of patients are HLA-B\\*27 positive (7% of general population); 1-2% of positive adults have AS.",
    "حالة التهابية مزمنة متقدّمة للعمود الفقري والمفصلين العجزيين الحرقفيين مع تعظّم الأربطة بين الفقرات؛ تصيب الرجال دون 40 ثلاثة أضعاف النساء. نحو 90% من المرضى موجبو `HLA-B*27` (7% من السكان)؛ و1–2% من البالغين الموجبين مصابون."),
 IM("Mention the criteria of inflammatory spinal pain in AS classification.", "اذكر معايير ألم العمود الفقري الالتهابي في تصنيف المرض.",
    "Spinal pain in back, dorsal or cervical region with at least 4 of: onset < 45 years; insidious onset; improved by exercise; associated with morning stiffness; at least 3 months duration.",
    "ألم في الظهر أو المنطقة الظهرية أو الرقبية مع 4 على الأقل من: البدء قبل 45 سنة؛ البدء الخفيّ؛ التحسّن بالتمرين؛ ارتباطه بالتيبّس الصباحي؛ مدّة 3 أشهر على الأقل."),
 IM("On what is the diagnosis of AS based?", "على ماذا يعتمد تشخيص التهاب الفقار المقسِّط؟",
    "Evaluating symptoms (pain and morning stiffness of the spine and sacral areas); physical examination (Schober's test); X-ray findings; blood tests (elevated IgA, ESR and CRP when active; RF and ANA consistently negative).",
    "تقييم الأعراض (ألم وتيبّس صباحي في العمود الفقري والمنطقة العجزية)؛ الفحص السريري (اختبار شوبر)؛ نتائج الأشعة؛ فحوص الدم (ارتفاع `IgA`، و`ESR` و`CRP` عند النشاط؛ `RF` و`ANA` سالبان دائمًا)."),
 IM("Define psoriatic arthritis and list its clinical manifestations.", "عرّف التهاب المفاصل الصدفي وعدّد مظاهره السريرية.",
    "A chronic inflammatory arthritis associated with skin psoriasis, characterized by osteolysis and bony proliferation. Manifestations: skin and nail psoriasis, dactylitis, enthesitis, osteoperiostitis, large joint oligoarthritis, arthritis mutilans, sacroiliitis, spondylitis and DIP arthritis.",
    "التهاب مفاصل التهابي مزمن مرتبط بصدفية الجلد، يتميّز بانحلال العظم وتكاثره. مظاهره: صدفية الجلد والأظافر، التهاب الإصبع، التهاب مواضع الارتكاز، التهاب العظم والسمحاق، التهاب قليل المفاصل الكبيرة، التهاب المفاصل المشوِّه، التهاب المفصل العجزي الحرقفي، التهاب الفقار، والتهاب المفاصل بين السلاميات البعيدة."),
 IM("List the comorbidities in PsA patients.", "عدّد الأمراض المصاحبة لدى مرضى التهاب المفاصل الصدفي.",
    "Ocular inflammation (iritis/uveitis/episcleritis); IBD; metabolic syndrome (hyperlipidemia, hypertension, insulin resistance, diabetes, obesity) with higher CVD risk; psychosocial burden, reactive depression, higher suicidal ideation and alcoholism.",
    "الالتهاب العيني (القزحية/العنبية/الصلبة الظاهرة)؛ مرض الأمعاء؛ المتلازمة الأيضية (فرط الشحوم، ارتفاع الضغط، مقاومة الإنسولين، السكري، السمنة) مع خطر أعلى لأمراض القلب والأوعية؛ العبء النفسي الاجتماعي، والاكتئاب التفاعلي، وارتفاع الأفكار الانتحارية، والإدمان على الكحول."),
]

meta = dict(subject_en="Clinical Immunology", subject_ar="المناعة السريرية", short_ar="مناعة",
            unit_en="Lecture 3", unit_ar="المحاضرة 3", unit_label="LEC", unit_no="3",
            title_en="Ankylosing spondylitis and Psoriatic Arthritis", title_ar="التهاب الفقار المقسِّط والتهاب المفاصل الصدفي",
            kind="Theory — نظري", stage="The fourth stage — الرابعة", instructor="د. عبير",
            file_name="مناعة نظري المحاضرة الثالثة", questions_suffix=" اسئلة")

folder = "immunology4-lec3-spondyloarthritis"
qs = [q for q in mcq if "answer" in q]
print(folder, len(qs), dict(Counter(q["answer"] for q in qs)), len(tf),
      dict(Counter(t["answer"] for t in tf)), len(traps), len(important))
d = os.path.dirname(os.path.abspath(__file__))
json.dump({"meta": meta, "blocks": blocks,
           "questions": {"mcq": mcq, "tf": tf, "traps": traps, "important": important}},
          open(os.path.join(d, "lecture.json"), "w"), ensure_ascii=False, indent=1)
