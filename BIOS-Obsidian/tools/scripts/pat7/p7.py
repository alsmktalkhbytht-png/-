import sys, re; sys.path.insert(0, "/tmp/claude-0/-home-user-kwmdkm/a7dd109e-db53-5fd3-8234-9dab3a530e24/scratchpad/imm456")
from ci import *            # c helpers + B INSHORT TERMS balance save(split.fix)
import split
split.ABBR = split.ABBR + ("Fig.",)

# Pathology — lecture 7 (stage 4) — د. حامد خليل التميمي — Oral Cavity Tumors (+ reflux esophagitis at the end of the file)

BN = lambda en, ar: N(en, ar, label=["BIOS note", "ملاحظة BIOS"])
O = P
def TERMS6(terms, n=6):
    head = [B("Term", "المصطلح"), "الترجمات العربية المستعملة"]
    return [SEC("Key terms", "أهم المصطلحات")] + [T(head, [[f"**{e}**", a] for e, a in terms[i:i + n]], ar_cols=[1], widths=[36, 64])
                                                  for i in range(0, len(terms), n)]

blocks = [
 # ───────────────────────── 1. Pleomorphic adenoma
 SEC("BENIGN TUMORS OF ORAL CAVITY — PLEOMORPHIC ADENOMA", "أورام التجويف الفموي الحميدة — الورم الغدّي متعدّد الأشكال"),
 C("**Pleomorphic adenoma** is a most common benign tumor of the salivary glands, characterized by an admixture of epithelial and stromal elements, and is also called mixed tumors.",
   "**الورم الغدّي متعدّد الأشكال** هو **أشيع ورم حميد في الغدد اللعابية**، ويتميّز **بخليط من العناصر الظهارية والسدوية (اللُحمية)**، ويسمّى أيضًا **الأورام المختلطة**."),
 FF(("pleomorphic-patient-mri.jpg", "Pleomorphic adenoma: (A) parotid swelling, (B) MRI", "الورم الغدّي متعدّد الأشكال: (A) تورّم النكفية، (B) رنين مغناطيسي", "52mm"),
    ("pleomorphic-palate.jpg", "Pleomorphic adenoma of the palate (minor salivary gland)", "ورم غدّي متعدّد الأشكال في الحنك (غدة لعابية صغيرة)", "52mm")),
 C(["In pathology, the term\"pleomorphic\" is used to indicate nuclear variation (size and shape of nuclei) in neoplasm.",
    "However, the term pleomorphic adenoma is used because of variable cell type seen in this lesion."],
   ["في علم الأمراض يُستعمل مصطلح **\"متعدّد الأشكال\"** للدلالة على **تباين الأنوية (حجمها وشكلها)** في الورم.",
    "لكن مصطلح الورم الغدّي متعدّد الأشكال يُستعمل هنا بسبب **تنوّع أنواع الخلايا** في هذه الآفة."]),
 L(["**Age:** It occurs usually during third to fifth decade of life (middle-age).", "**Sex:** It is most frequent in females."],
   ["**العمر:** يحدث عادةً **بين العقد الثالث والخامس** من العمر (منتصف العمر).", "**الجنس:** **أكثر شيوعًا في الإناث**."]),
 L(["**Major salivary gland:** Common site and constitute about 60% of tumors in the parotid. Usually arise in the superficial lobe of the parotid. Less common in the submandibular glands and very rare in the sublingual gland.",
    "**Minor salivary gland:** Its involvement is relatively rare."],
   ["**الغدد اللعابية الكبيرة:** موقع شائع ويشكّل **حوالي 60% من أورام النكفية**. وينشأ عادةً في **الفص السطحي للنكفية**. وأقل شيوعًا في **الغدد تحت الفكية**، و**نادر جدًا في الغدة تحت اللسان**.",
    "**الغدد اللعابية الصغيرة:** إصابتها **نادرة نسبيًا**."], en="**Site**", ar="**الموقع**"),
 C("**Etiology** Not known. Exposure to radiation increases the risk.", "**السببيات** **غير معروفة**. و**التعرّض للإشعاع** يزيد الخطر."),
 INSHORT([("Pleomorphic adenoma = **most common benign salivary tumor** = **mixed tumor** (epithelial + stromal).", "الورم الغدّي متعدّد الأشكال = **أشيع ورم لعابي حميد** = **ورم مختلط** (ظهاري + سدوي)."),
          ("“Pleomorphic” here = **variable cell types**, not nuclear variation.", "“متعدّد الأشكال” هنا = **تنوّع أنواع الخلايا** لا تباين الأنوية."),
          ("3rd–5th decade, **females**; **parotid ~60%** (superficial lobe); risk ↑ with **radiation**.", "العقد 3–5، **الإناث**؛ **النكفية ~60%** (الفص السطحي)؛ الخطر ↑ مع **الإشعاع**.")]),

 # ───────────────────────── 2. Warthin tumor
 SEC("WARTHIN TUMOR", "ورم وارثين"),
 C("**Warthins tumor** (papillary cystadenoma lymphomatosum , adenolymphoma) is a benign and the second most common salivary gland neoplasm.",
   "**ورم وارثين** (**الورم الغدّي الكيسي الحليمي اللمفاوي**، **الورم الغدّي اللمفاوي**) ورم **حميد** و**ثاني أشيع ورم في الغدد اللعابية**."),
 F("warthin-patient.jpg", "Warthin tumor — parotid swelling (A, B, C)", "ورم وارثين — تورّم النكفية (A، B، C)", h="50mm", fit="contain"),
 L(["**Site:** It almost exclusively arises in the parotid gland.", "**Sex:** It is the only salivary glands tumor that is more common in males than in females.",
    "**Age:** It usually occur between fifth to seventh decades of life.", "**Predisposing factor:** Smokers have eight times the risk of nonsmokers."],
   ["**الموقع:** ينشأ **حصرًا تقريبًا في الغدة النكفية**.", "**الجنس:** هو **الورم اللعابي الوحيد الأشيع في الذكور** منه في الإناث.",
    "**العمر:** يحدث عادةً **بين العقد الخامس والسابع**.", "**العامل المهيّئ:** للمدخّنين **ثمانية أضعاف** خطر غير المدخّنين."]),
 FF(("salivary-histology.jpg", "Salivary gland histology (labels on the slide: serous acini, mucous acini, intercalated ducts, myoepithelial cells, striated ducts)", "نسيج الغدة اللعابية (كتابات الشريحة: عنيبات مصلية، عنيبات مخاطية، قنوات بينية، خلايا ظهارية عضلية، قنوات مخطّطة)", "48mm"),
    ("warthin-histology.jpg", "Warthin tumor (histology)", "ورم وارثين (مقطع نسيجي)", "48mm")),
 T([B("Feature", "الصفة"), B("Pleomorphic adenoma", "الورم الغدّي متعدّد الأشكال"), B("Warthin tumor", "ورم وارثين")],
   [[B("**Rank**", "**المرتبة**"), B("most common benign", "أشيع حميد"), B("second most common", "ثاني أشيع")],
    [B("**Sex**", "**الجنس**"), B("females", "الإناث"), B("males (the only one)", "الذكور (الوحيد)")],
    [B("**Age**", "**العمر**"), B("3rd–5th decade", "العقد 3–5"), B("5th–7th decade", "العقد 5–7")],
    [B("**Site**", "**الموقع**"), B("parotid (~60%), superficial lobe", "النكفية (~60%)، الفص السطحي"), B("almost exclusively parotid", "النكفية حصرًا تقريبًا")],
    [B("**Risk**", "**الخطر**"), B("radiation", "الإشعاع"), B("smoking ×8", "التدخين ×8")]],
   key_cols=[0], widths=[18, 41, 41], style="summary", label_en="Pleomorphic adenoma vs Warthin", label_ar="متعدّد الأشكال مقابل وارثين"),
 INSHORT([("Warthin = **papillary cystadenoma lymphomatosum / adenolymphoma**; benign, **2nd most common**.", "وارثين = **الورم الغدّي الكيسي الحليمي اللمفاوي**؛ حميد، **ثاني أشيع**."),
          ("Almost only **parotid**; the only salivary tumor **commoner in males**; 5th–7th decade; **smokers ×8**.", "تقريبًا **النكفية فقط**؛ الورم اللعابي الوحيد **الأشيع في الذكور**؛ العقد 5–7؛ **المدخّنون ×8**.")]),

 # ───────────────────────── 3. Malignant: SCC
 SEC("MALIGNANT TUMORS OF ORAL CAVITY", "أورام التجويف الفموي الخبيثة"),
 C("**Oral cancer:** Majority are squamous cell carcinomas.", "**سرطان الفم:** **أغلبه كارسينومات الخلايا الحرشفية**."),
 C("Squamous cell carcinoma (SCC) of oral cavity is multifactorial disease usually seen in middle-aged men.", "كارسينوما الخلايا الحرشفية (SCC) في التجويف الفموي **مرض متعدّد العوامل** يُرى عادةً في **الرجال في منتصف العمر**."),
 H2("PATHOGENESIS", "الإمراضية"),
 C(["The development of squamous cell carcinoma is a multistep process.", "It involves sequential activation of oncogenes and inactivation of tumor suppressor genes in a clonal population of cells."],
   ["نشوء كارسينوما الخلايا الحرشفية **عملية متعدّدة الخطوات**.", "تتضمّن **تنشيطًا متسلسلًا للجينات الورمية** و**تعطيلًا للجينات الكابتة للورم** في **مجموعة خلايا نسيلية**."]),
 L(["Inactivation of the p16 gene (about 80% of the cases) .", "Mutation of the p53 tumor suppressor gene is associated with progression of hyperplasia /hyperkeratosis to dysplasia.",
    "Amplification and overexpression of the cyclin D1 gene constitutively activates cell cycle progression"],
   ["**تعطيل جين p16** (حوالي **80%** من الحالات).", "**طفرة الجين الكابت للورم p53** ترتبط **بتطوّر فرط التنسّج / فرط التقرّن إلى خلل التنسّج**.",
    "**تضخيم جين cyclin D1 وفرط التعبير عنه** ينشّط **تقدّم دورة الخلية بشكل دائم**"]),
 H2("METHODS OF SPREAD", "طرق الانتشار"),
 L(["**Local:** Tissue involved depends on the primary site.",
    ["**Lymph node:** The involved site of lymph node depends on the location of the primary tumor.", "The more anterior the tumor, more is the spread to the cervical nodes.", "Carcinomas of the base of the tongue and oropharynx metastasize to the deep retropharyngeal lymph nodes."],
    "**Blood spread:** It spreads to lungs, liver, and bones."],
   ["**الموضعي:** النسيج المصاب يعتمد على **الموقع الأولي**.",
    ["**العقد اللمفية:** موقع العقد المصابة يعتمد على مكان الورم الأولي.", "**كلما كان الورم أمامياً أكثر** زاد انتشاره إلى **العقد العنقية**.", "وكارسينومات **قاعدة اللسان والبلعوم الفموي** تنتقل إلى **العقد اللمفية خلف البلعوم العميقة**."],
    "**الانتشار الدموي:** ينتشر إلى **الرئتين والكبد والعظام**."]),
 INSHORT([("Oral cancer: **mostly SCC**; multifactorial; **middle-aged men**.", "سرطان الفم: **أغلبه SCC**؛ متعدّد العوامل؛ **رجال منتصف العمر**."),
          ("Multistep: **p16 inactivation (~80%)**, **p53** mutation (hyperplasia → dysplasia), **cyclin D1** amplification.", "متعدّد الخطوات: **تعطيل p16 (~80%)**، طفرة **p53** (فرط تنسّج ← خلل تنسّج)، تضخيم **cyclin D1**."),
          ("Spread: local; nodes (anterior → **cervical**; tongue base/oropharynx → **deep retropharyngeal**); blood → **lungs, liver, bones**.", "الانتشار: موضعي؛ عقد (أمامي ← **عنقية**؛ قاعدة اللسان/البلعوم ← **خلف البلعوم العميقة**)؛ دم ← **الرئة، الكبد، العظام**.")]),

 # ───────────────────────── 4. Mucoepidermoid carcinoma
 SEC("MUCOEPIDERMOID CARCINOMA", "الكارسينوما المخاطية البشروية"),
 C("Most common primary malignant tumor of the salivary glands.", "**أشيع ورم خبيث أولي في الغدد اللعابية**."),
 FF(("mucoepidermoid-clinical.jpg", "Intraoral examination showed swelling on right maxilla", "فحص داخل الفم أظهر تورّمًا في الفك العلوي الأيمن", "50mm"),
    ("mucoepidermoid-histology.jpg", "Mucoepidermoid carcinoma (histology)", "الكارسينوما المخاطية البشروية (مقطع نسيجي)", "50mm")),
 L(["Constitute about 15% of all salivary gland tumors.", "Occur mainly (60–70%) in the parotids.", "Account for a major fraction of the minor salivary gland tumors."],
   ["تشكّل **حوالي 15% من كل أورام الغدد اللعابية**.", "تحدث أساسًا (**60–70%**) في **النكفيتين**.", "وتشكّل **جزءًا كبيرًا من أورام الغدد اللعابية الصغيرة**."],
   en="**INCIDENCE**", ar="**الحدوث**"),
 INSHORT([("Mucoepidermoid carcinoma = **most common primary malignant salivary tumor**; **15%** of salivary tumors; **60–70% parotid**; big share of minor-gland tumors.", "الكارسينوما المخاطية البشروية = **أشيع ورم لعابي خبيث أولي**؛ **15%** من الأورام اللعابية؛ **60–70% النكفية**؛ جزء كبير من أورام الغدد الصغيرة.")]),

 # ───────────────────────── 5. Reflux esophagitis
 SEC("REFLUX ESOPHAGITIS", "التهاب المريء الارتجاعي"),
 C(["The stratified squamous epithelium of the esophagus is resistant to abrasion from foods but is sensitive to acid.",
    "The submucosal glands of the proximal and distal esophagus contribute to mucosal protection by secreting mucin and bicarbonate."],
   ["الظهارة الحرشفية المطبّقة للمريء **مقاومة لاحتكاك الطعام** لكنها **حسّاسة للحامض**.",
    "وتسهم **الغدد تحت المخاطية** في المريء القريب والبعيد في حماية المخاطية **بإفراز المخاط (الميوسين) والبيكاربونات**."]),
 C(["Reflux of gastric contents into the lower esophagus is the most frequent cause of esophagitis and the most common outpatient gastrointestinal diagnosis in the United States.",
    "The associated clinical condition is termed gastroesophageal reflux disease(GERD)."],
   ["**ارتجاع محتويات المعدة إلى أسفل المريء** هو **أشيع سبب لالتهاب المريء** و**أشيع تشخيص هضمي في العيادات الخارجية** في الولايات المتحدة.",
    "وتسمّى الحالة السريرية المرتبطة **داء الارتجاع المعدي المريئي (GERD)**."]),
 BN("Reflux esophagitis is in the same file as the oral tumors (last slides) — kept here as written.", "التهاب المريء الارتجاعي موجود في نفس الملف بعد أورام الفم (آخر الشرائح) — نُقل كما هو."),
 H2("MORPHOLOGY", "الشكل النسيجي"),
 L(["Simple hyperemia , evident to the endoscopist as redness, may be the only alteration.", "In mild GERD the mucosal histology is often unremarkable.",
    "With more significant disease, eosinophils are recruited into the squamous mucosa, followed by neutrophils, which usually are associated with more severe injury (Fig. 14–9, A).",
    "Basal zone hyperplasia exceeding 20% of the total epithelial thickness and elongation of lamina propria papillae, such that they extend into the upper third of the epithelium, also may be present."],
   ["قد يكون **احتقان بسيط** — يراه منظار الهضم **احمرارًا** — هو التغيّر الوحيد.", "في **GERD الخفيف** يكون النسيج المخاطي غالبًا **غير لافت**.",
    "ومع المرض الأشد تُستدعى **الحمضات (eosinophils)** إلى المخاطية الحرشفية، تليها **العدلات** التي ترتبط عادةً **بأذى أشد** (الشكل 14–9، A).",
    "وقد يوجد أيضًا **فرط تنسّج المنطقة القاعدية** بما يتجاوز **20% من سمك الظهارة الكلي**، و**استطالة حليمات الصفيحة المخصوصة** حتى تمتد إلى **الثلث العلوي من الظهارة**."]),
 H2("CLINICAL FEATURES", "المظاهر السريرية"),
 L(["GERD is most common in adults older than 40 years of age but also occurs in infants and children.",
    "The most frequently reported symptoms are heartburn, dysphagia, and, less often, noticeable regurgitation of sour -tasting gastric con-tents.",
    "Rarely, chronic GERD is punctuated by attacks of severe chest pain that may be mistaken for heart disease.",
    ["Treatment with proton pump inhibitors reduces gastric acidity and typically provides symptomatic relief.", "While the severity of symptoms is not closely related to the degree of histologic damage, the latter tends to increase with disease duration."],
    "Complications of reflux esophagitis include esophageal ulceration, hematemesis, melena, stricture development, and Barrett esophagus."],
   ["GERD **أشيع في البالغين فوق 40 سنة** لكنه يحدث أيضًا في **الرضّع والأطفال**.",
    "أكثر الأعراض المذكورة: **حرقة المعدة (heartburn)**، و**عسر البلع**، وبشكل أقل **ارتجاع ملحوظ لمحتويات معدية حامضة الطعم**.",
    "ونادرًا تتخلّل GERD المزمن **نوبات ألم صدري شديد** قد تُخلط **بمرض القلب**.",
    ["العلاج **بمثبّطات مضخّة البروتون** يقلّل حموضة المعدة ويخفّف الأعراض عادةً.", "ومع أن **شدّة الأعراض لا ترتبط بشدّة بدرجة الضرر النسيجي**، فإن الضرر **يميل للزيادة مع طول مدّة المرض**."],
    "**مضاعفات** التهاب المريء الارتجاعي: **تقرّح المريء**، **قيء الدم**، **التغوّط الأسود (melena)**، **التضيّق**، و**مريء باريت**."]),
 INSHORT([("Esophageal squamous epithelium resists abrasion but is **sensitive to acid**; submucosal glands secrete **mucin + bicarbonate**.", "ظهارة المريء الحرشفية تقاوم الاحتكاك لكنها **حسّاسة للحامض**؛ والغدد تحت المخاطية تفرز **مخاطًا + بيكاربونات**."),
          ("**GERD** = commonest cause of esophagitis; morphology: hyperemia → **eosinophils** → neutrophils; basal hyperplasia **> 20%**, papillae to upper third.", "**GERD** = أشيع سبب لالتهاب المريء؛ النسيج: احتقان ← **حمضات** ← عدلات؛ فرط تنسّج قاعدي **> 20%**، حليمات للثلث العلوي."),
          ("Adults **> 40**; heartburn, dysphagia, regurgitation; chest pain mimics heart disease; **PPIs**; complications: ulcer, hematemesis, melena, stricture, **Barrett**.", "البالغون **> 40**؛ حرقة، عسر بلع، ارتجاع؛ ألم صدري يشبه القلب؛ **مثبّطات مضخّة البروتون**؛ المضاعفات: قرحة، قيء دم، melena، تضيّق، **باريت**.")]),

 *TERMS6([("Salivary gland", "الغدة اللعابية"), ("Pleomorphic adenoma (mixed tumor)", "الورم الغدّي متعدّد الأشكال / الورم المختلط"), ("Stromal", "سدوي / لُحمي"),
          ("Parotid gland", "الغدة النكفية"), ("Submandibular gland", "الغدة تحت الفكية"), ("Sublingual gland", "الغدة تحت اللسان"),
          ("Warthin tumor (adenolymphoma)", "ورم وارثين / الورم الغدّي اللمفاوي"), ("Squamous cell carcinoma (SCC)", "كارسينوما الخلايا الحرشفية"), ("Oncogene", "الجين الورمي"),
          ("Tumor suppressor gene (p16, p53)", "الجين الكابت للورم"), ("Cyclin D1", "سايكلين D1"), ("Hyperkeratosis", "فرط التقرّن"),
          ("Retropharyngeal lymph nodes", "العقد اللمفية خلف البلعوم"), ("Mucoepidermoid carcinoma", "الكارسينوما المخاطية البشروية"), ("Reflux esophagitis", "التهاب المريء الارتجاعي"),
          ("GERD", "داء الارتجاع المعدي المريئي"), ("Hyperemia", "الاحتقان / فرط الدم"), ("Eosinophils", "الحمضات / الخلايا الحمضية"),
          ("Heartburn", "حرقة المعدة / الحموضة"), ("Dysphagia", "عسر البلع"), ("Proton pump inhibitors", "مثبّطات مضخّة البروتون"),
          ("Hematemesis / Melena", "قيء الدم / التغوّط الأسود"), ("Barrett esophagus", "مريء باريت")]),
]

def _chunk(blocks, n=2, minlen=4):
    out = []
    for b in blocks:
        le = b.get("list_en")
        if b.get("t") == "card" and le and len(le) >= minlen:
            st = b.get("start", 1)
            for i in range(0, len(le), n):
                d = dict(t="card", en=b["en"] if i == 0 else "", ar=b["ar"] if i == 0 else "",
                         list_en=le[i:i + n], list_ar=b["list_ar"][i:i + n])
                if st + i != 1: d["start"] = st + i
                out.append(d)
        else:
            out.append(b)
    return out
blocks = _chunk(blocks)

exec(open(__file__.replace("p7.py", "p7q.py")).read())
