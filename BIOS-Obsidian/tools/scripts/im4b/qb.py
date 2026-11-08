import sys, json, os, shutil, copy
sys.path.insert(0, "/tmp/claude-0/-home-user/ebd718de-5339-5b98-9782-8a5888247f2a/scratchpad/imm456")
from ci import *            # Q TF TR IM P balance
sys.path.insert(0, "/tmp/claude-0/-home-user/ebd718de-5339-5b98-9782-8a5888247f2a/scratchpad"); from bidi import ltr_all

# Immunology theory lecture 4 (stage 3, د. أحمد داود) — QUESTIONS ONLY, comprehensive bank (user 2026-11-08).
# The user re-sent Lec._4_immunogloblin.pptx: every word of it is already in immunology-lec4-immunoglobulins/lecture.json
# (same file) → the existing bank (51 MCQ, 16 TF, 8 traps, 8 essays) + new questions for the gaps
# (protective functions, Fc/structure details, IgA/IgD/IgE, class switching, uses of the antigenic determinants).
SRC = "/home/user/-/immunology-lec4-immunoglobulins"
FOLDER = "immunology-lec4-mcq"
O = P
old = json.load(open(SRC + "/lecture.json"))["questions"]

NEW = {
 "Definition and pathways": [
  Q("Immunoglobulins circulate in blood and body fluids to:", "تدور الغلوبيولينات المناعية في الدم وسوائل الجسم لكي:",
    O(("Recognize and neutralize bacteria, viruses and toxins", "تتعرّف على البكتيريا والفيروسات والسموم وتعادلها"), ("Carry oxygen", "تنقل الأوكسجين"), ("Clot the blood", "تخثّر الدم"), ("Digest proteins", "تهضم البروتينات")), "a"),
  Q("In T-independent activation, the first signal comes from:", "في التنشيط المستقلّ عن التائية تأتي الإشارة الأولى من:",
    O(("Th cell cytokines", "سيتوكينات التائية المساعدة"), ("Cross-linkage of multiple BCRs by repetitive epitopes", "ربط عدّة مستقبلات BCR بالحواتم المتكرّرة"), ("MHC I", "MHC I"), ("Complement C1q", "المتمّم C1q")), "b"),
  Q("The main antibody secreted in T-independent B cell activation is:", "الضدّ الرئيسي المُفرز في التنشيط المستقلّ عن التائية:",
    O(("IgE", "IgE"), ("IgD", "IgD"), ("Pentameric IgM", "IgM الخماسي"), ("Secretory IgA", "IgA الإفرازي")), "c"),
  Q("Plasma-cell antibodies clear the antigen by:", "تتخلّص أضداد خلايا البلازما من المستضد بـ:",
    O(("Phosphorylation", "الفسفرة"), ("Glycolysis", "تحلّل السكر"), ("Hemolysis only", "تحلّل الدم فقط"), ("Agglutination, precipitation or neutralization", "التلازن أو الترسيب أو المعادلة")), "d"),
 ],
 "Structure": [
  Q("The light chain of an immunoglobulin is:", "السلسلة الخفيفة في الغلوبيولين المناعي:", O(("κ or λ", "κ أو λ"), ("μ or γ", "μ أو γ"), ("α or δ", "α أو δ"), ("ε only", "ε فقط")), "a"),
  Q("Each domain of an immunoglobulin is a globular region containing:", "كل مجال في الغلوبيولين المناعي منطقة كروية تحتوي:",
    O(("A J chain", "سلسلة J"), ("An intra-chain disulfide bond", "رابطة ثنائية الكبريت داخل السلسلة"), ("A carbohydrate on every domain", "كربوهيدرات على كل مجال"), ("A secretory piece", "قطعة إفرازية")), "b"),
  Q("Ig domains were determined using:", "حُدّدت مجالات الغلوبيولين المناعي باستعمال:",
    O(("Light microscopy", "المجهر الضوئي"), ("ELISA", "الإليزا"), ("High-resolution x-ray crystallography", "علم البلورات بالأشعة السينية عالي الدقة"), ("Gel filtration only", "الترشيح الهلامي فقط")), "c"),
  Q("Framework regions (FR) are:", "مناطق الهيكل (FR) هي:",
    O(("The Fc fragment", "قطعة Fc"), ("The hinge", "المفصل"), ("The J chain", "سلسلة J"), ("The regions between the CDRs in the variable region", "المناطق بين الـ CDRs في المنطقة المتغيّرة")), "d"),
  Q("Mercaptoethanol reduction of an immunoglobulin gives:", "اختزال الغلوبيولين المناعي بالمركبتوإيثانول يعطي:",
    O(("Separate heavy and light chains", "سلاسل ثقيلة وخفيفة منفصلة"), ("Two Fab + Fc", "قطعتي Fab + Fc"), ("F(ab')2", "F(ab')2"), ("A pentamer", "خماسيًا")), "a"),
  Q("Which is a physiological effect mediated through the Fc region?", "أيّ مما يلي تأثير فسيولوجي تتوسّطه منطقة Fc؟",
    O(("Antigen recognition", "التعرّف على المستضد"), ("Degranulation of mast cells", "تحرّر حبيبات الخلايا البدينة"), ("Gene rearrangement", "إعادة ترتيب الجينات"), ("Forming the CDRs", "تكوين الـ CDRs")), "b"),
 ],
 "Genes and diversity": [
  Q("In each of the three Ig gene loci, the V gene segments are separated from the:", "في كل من مواقع جينات الغلوبيولين الثلاثة، تكون قطع الجينات V منفصلة عن:",
    O(("Promoter only", "المحفّز فقط"), ("Mitochondrial genes", "جينات المايتوكوندريا"), ("C gene segments", "قطع الجينات C"), ("MHC genes", "جينات MHC")), "c"),
  Q("L and H chains are synthesized:", "تُصنع السلاسل الخفيفة والثقيلة:",
    O(("Together on one ribosome", "معًا على رايبوسوم واحد"), ("In the nucleus", "في النواة"), ("In the Golgi", "في جهاز غولجي"), ("Separately on polysomes and assembled into H2L2", "منفصلة على متعدّدات الرايبوسوم ثم تُجمع إلى H2L2")), "d"),
 ],
 "Classes": [
  Q("IgG subclasses differ in:", "تختلف الأصناف الفرعية لـ IgG في:",
    O(("The number of disulfide bonds and length of the hinge region", "عدد الروابط ثنائية الكبريت وطول منطقة المفصل"), ("The light chain type", "نوع السلسلة الخفيفة"), ("Having a J chain", "وجود سلسلة J"), ("Being pentamers", "كونها خماسية")), "a"),
  Q("IgG is called the most versatile immunoglobulin because:", "يُسمّى IgG أكثر الغلوبيولينات تعدّدًا للوظائف لأنه:",
    O(("It is a pentamer", "خماسي"), ("It can carry out all of the functions of immunoglobulin molecules", "يستطيع أداء كل وظائف الغلوبيولينات المناعية"), ("It is only on B cells", "على الخلايا البائية فقط"), ("It binds mast cells only", "يرتبط بالخلايا البدينة فقط")), "b"),
  Q("The IgG subclasses that do NOT bind to macrophages, monocytes and PMNs are:", "الأصناف الفرعية لـ IgG التي لا ترتبط بالبلاعم والوحيدات ومتعدّدات النوى:",
    O(("IgG1 and IgG3", "IgG1 وIgG3"), ("IgG1 only", "IgG1 فقط"), ("IgG2 and IgG4", "IgG2 وIgG4"), ("IgG3 only", "IgG3 فقط")), "c"),
  Q("The half-life of IgM is about:", "العمر النصفي لـ IgM نحو:", O(("21 days", "21 يومًا"), ("1 hour", "ساعة"), ("1 year", "سنة"), ("5 days", "5 أيام")), "d"),
  Q("The complement pathway activated by IgM is the:", "مسار المتمّم الذي ينشّطه IgM:", O(("Classical pathway", "المسار الكلاسيكي"), ("Alternative pathway only", "المسار البديل فقط"), ("Lectin pathway only", "مسار اللكتين فقط"), ("None", "لا شيء")), "a"),
  Q("Serum IgA is a:", "IgA المصل:", O(("Pentamer", "خماسي"), ("Monomer", "أحادي"), ("Trimer with J chain", "ثلاثي بسلسلة J"), ("Dimer always", "ثنائي دائمًا")), "b"),
  Q("Secretory IgA protects body surfaces by:", "يحمي IgA الإفرازي أسطح الجسم بـ:",
    O(("Lysing red cells", "تحليل الكريات الحمر"), ("Binding mast cells", "الارتباط بالخلايا البدينة"), ("Blocking the attachment of bacteria and viruses to mucous membranes", "منع التصاق البكتيريا والفيروسات بالأغشية المخاطية"), ("Crossing the placenta", "عبور المشيمة")), "c"),
  Q("The role of IgD in serum is:", "دور IgD في المصل:", O(("Allergy", "التحسّس"), ("Placental transfer", "العبور المشيمي"), ("Complement fixation", "تثبيت المتمّم"), ("Uncertain", "غير مؤكّد")), "d"),
  Q("Killing of IgE-coated helminths is done by:", "قتل الديدان المغطّاة بـ IgE يتمّ بواسطة:",
    O(("Eosinophils with Fc receptors for IgE", "الحمضات ذات مستقبلات Fc لـ IgE"), ("Red blood cells", "الكريات الحمر"), ("Platelets", "الصفائح"), ("Plasma cells", "خلايا البلازما")), "a"),
  Q("The least common serum immunoglobulin is:", "أقلّ الغلوبيولينات المناعية في المصل:", O(("IgG", "IgG"), ("IgE", "IgE"), ("IgA", "IgA"), ("IgM", "IgM")), "b"),
 ],
 "Antigenic determinants and responses": [
  Q("Antibodies formed against antibodies are called:", "الأضداد المتكوّنة ضدّ الأضداد تُسمّى:",
    O(("Autoantigens", "مستضدات ذاتية"), ("Haptens", "هابتينات"), ("Anti-Ig antibodies", "أضداد مضادّة للغلوبيولين"), ("Toxoids", "ذيفانات معدّلة")), "c"),
  Q("Isotype determination is used in:", "يُستعمل تحديد الأنماط المتماثلة في:",
    O(("Paternity testing", "فحص الأبوّة"), ("Vaccine design", "تصميم اللقاحات"), ("Forensic medicine", "الطب العدلي"), ("Characterization of B cell leukemia and diagnosis of immunodeficiency", "توصيف ابيضاض الخلايا البائية وتشخيص نقص المناعة")), "d"),
  Q("Anti-idiotype antibodies are used in:", "تُستعمل الأضداد المضادّة للنمط الذاتي في:",
    O(("Vaccines and treatment of B cell tumors", "اللقاحات وعلاج أورام الخلايا البائية"), ("Blood grouping", "تحديد فصائل الدم"), ("Paternity testing", "فحص الأبوّة"), ("Measuring glucose", "قياس السكّر")), "a"),
  Q("Class switching is regulated by Th cells and cytokines such as:", "ينظّم تبديل الصنفَ الخلايا التائية المساعدة وسيتوكينات مثل:",
    O(("Insulin and glucagon", "الأنسولين والغلوكاغون"), ("IL-4, IL-5, IFN-γ and TGF-β", "IL-4 وIL-5 وIFN-γ وTGF-β"), ("Histamine", "الهستامين"), ("Erythropoietin", "الإريثروبويتين")), "b"),
  Q("Class switching occurs by a mechanism called:", "يحدث تبديل الصنف بآلية تُسمّى:",
    O(("Somatic hypermutation only", "الطفرة الجسدية المفرطة فقط"), ("Alternative splicing of light chains", "التضفير البديل للسلاسل الخفيفة"), ("Class switching recombination (CSR)", "إعادة اتحاد تبديل الصنف (CSR)"), ("Phagocytosis", "البلعمة")), "c"),
  Q("In the secondary response, the amount of IgM is:", "في الاستجابة الثانوية تكون كمّية IgM:",
    O(("Absent", "غائبة"), ("Ten times higher than IgG", "أعلى بعشر مرّات من IgG"), ("The only antibody", "الضدّ الوحيد"), ("Qualitatively similar to the first contact", "مشابهة نوعيًا للتماسّ الأول")), "d"),
 ],
 "Protective functions": [
  Q("Neutralization by antibodies means:", "المعادلة بالأضداد تعني:",
    O(("Blocking viral binding sites and coating bacterial toxins", "حجب مواقع ارتباط الفيروس وتغليف السموم البكتيرية"), ("Clumping particulate antigens", "تكتيل المستضدات الدقائقية"), ("Lysing the cell", "تحليل الخلية"), ("Precipitating soluble antigens", "ترسيب المستضدات الذائبة")), "a"),
  Q("Agglutination is the clumping of:", "التلازن هو تكتّل:", O(("Soluble antigens", "المستضدات الذائبة"), ("Particulate antigens", "المستضدات الدقائقية"), ("Antibodies alone", "الأضداد وحدها"), ("Complement proteins", "بروتينات المتمّم")), "b"),
  Q("Antibodies precipitate:", "ترسّب الأضداد:", O(("Bacteria only", "البكتيريا فقط"), ("Red cells", "الكريات الحمر"), ("Soluble antigens", "المستضدات الذائبة"), ("Mast cells", "الخلايا البدينة")), "c"),
  Q("Activation of complement by antibodies leads to:", "تنشيط المتمّم بالأضداد يؤدّي إلى:",
    O(("Gene rearrangement", "إعادة ترتيب الجينات"), ("Placental transfer", "العبور المشيمي"), ("Class switching", "تبديل الصنف"), ("Cell lysis, enhanced phagocytosis and inflammation", "تحلّل الخلايا وتعزيز البلعمة والالتهاب")), "d"),
  Q("Immune complexes activate the classical complement pathway through:", "تنشّط المعقّدات المناعية المسار الكلاسيكي للمتمّم عبر:",
    O(("C1q", "C1q"), ("The J chain", "سلسلة J"), ("MHC II", "MHC II"), ("TCR", "TCR")), "a"),
  Q("Antibodies bound to the surface of pathogens prepare them for phagocytosis; this is:", "الأضداد المرتبطة بسطح الممرضات تهيّئها للبلعمة؛ وهذا هو:",
    O(("Neutralization", "المعادلة"), ("Opsonization", "الطهي (التهيئة للبلعمة)"), ("Precipitation", "الترسيب"), ("Agglutination", "التلازن")), "b"),
  Q("Antibodies bound to target cells promote their recognition and killing by:", "الأضداد المرتبطة بالخلايا الهدف تعزّز تعرّفها وقتلها بواسطة:",
    O(("Red blood cells", "الكريات الحمر"), ("Platelets", "الصفائح"), ("NK cells", "الخلايا القاتلة الطبيعية (NK)"), ("Plasma cells", "خلايا البلازما")), "c"),
  Q("In the figure of protective functions, antibodies act as adapter molecules linking antigens to:", "في شكل الوظائف الوقائية، تعمل الأضداد جزيئات وصل تربط المستضدات بـ:",
    O(("DNA", "الدنا"), ("Hemoglobin", "الهيموغلوبين"), ("Ribosomes", "الرايبوسومات"), ("C1q and Fc receptors (FcR)", "C1q ومستقبلات Fc (FcR)")), "d", img="assets/protective-2.png", img_h="44mm"),
 ],
}
NEW_TF = [
 TF("T-independent B cell activation needs the cooperation of helper T cells.", "يحتاج التنشيط المستقلّ عن التائية تعاون الخلايا التائية المساعدة.", "F"),
 TF("Th cells secrete chemokines that activate B cells more effectively.", "تفرز الخلايا التائية المساعدة كيموكينات تنشّط الخلايا البائية بفعالية أكبر.", "T"),
 TF("The heavy chain variable region (VH) contains about 110 amino acids.", "تحتوي المنطقة المتغيّرة للسلسلة الثقيلة (VH) نحو 110 أحماض أمينية.", "T"),
 TF("Mercaptoethanol reduction separates heavy and light chains.", "الاختزال بالمركبتوإيثانول يفصل السلاسل الثقيلة عن الخفيفة.", "T"),
 TF("The κ light chain genes are on chromosome 14.", "جينات السلسلة الخفيفة κ على الكروموسوم 14.", "F"),
 TF("IgD fixes complement.", "يثبّت IgD المتمّم.", "F"),
 TF("Serum IgE levels rise in parasitic helminth infections.", "ترتفع مستويات IgE في المصل في عدوى الديدان الطفيلية.", "T"),
 TF("Idiotypes are located in the constant region of the Ig.", "تقع الأنماط الذاتية في المنطقة الثابتة للغلوبيولين.", "F"),
 TF("Antibodies can opsonize pathogens for phagocytosis.", "تستطيع الأضداد طهي الممرضات (تهيئتها) للبلعمة.", "T"),
 TF("Agglutination is the precipitation of soluble antigens.", "التلازن هو ترسيب المستضدات الذائبة.", "F"),
]
NEW_TR = [
 TR("Agglutination vs precipitation", "التلازن مقابل الترسيب", "Agglutination = clumping of PARTICULATE antigens (cells, bacteria); precipitation = of SOLUBLE antigens.",
    "التلازن = تكتّل المستضدات الدقائقية (خلايا، بكتيريا)؛ والترسيب = للمستضدات الذائبة."),
 TR("Which Ig for which complement pathway?", "أيّ ضدّ لأيّ مسار متمّم؟", "IgM (and IgG) → classical pathway via C1q; IgA → alternative pathway (fixes complement only when aggregated); IgD and IgE do not fix complement.",
    "IgM (وIgG) ← المسار الكلاسيكي عبر C1q؛ وIgA ← المسار البديل (لا يثبّت المتمّم إلا إذا تجمّع)؛ وIgD وIgE لا يثبّتان المتمّم."),
]
NEW_IM = [
 IM("List the protective functions of antibodies.", "عدّد الوظائف الوقائية للأضداد.",
    "Neutralization (blocks viral binding sites, coats bacterial toxins); agglutination of particulate antigens; precipitation of soluble antigens; activation of complement (C1q, classical pathway) leading to cell lysis, enhanced phagocytosis and inflammation; opsonization through Fc receptors; recognition and killing of antibody-coated cells by NK cells (and of worms by eosinophils); sensitization of cells through Fc receptors.",
    "المعادلة (حجب مواقع ارتباط الفيروس وتغليف السموم البكتيرية)؛ تلازن المستضدات الدقائقية؛ ترسيب المستضدات الذائبة؛ تنشيط المتمّم (C1q، المسار الكلاسيكي) فيؤدّي إلى تحلّل الخلايا وتعزيز البلعمة والالتهاب؛ الطهي عبر مستقبلات Fc؛ تعرّف الخلايا القاتلة الطبيعية على الخلايا المغطّاة بالأضداد وقتلها (والحمضات للديدان)؛ تحسيس الخلايا عبر مستقبلات Fc."),
 IM("What is class switching and how is it regulated?", "ما تبديل الصنف وكيف يُنظَّم؟",
    "A change of the antibody produced by a B cell from one class to another after the first antigen exposure (e.g. IgM to IgG). The heavy-chain constant region changes while the variable region stays the same, so antigen specificity and affinity are kept. It occurs in activated B cells, is regulated by Th cells through contact and cytokines (IL-4, IL-5, IFN-γ, TGF-β), by class switching recombination (CSR).",
    "تغيّر الضدّ الذي تنتجه الخلية البائية من صنف إلى آخر بعد التعرّض الأول للمستضد (مثل IgM إلى IgG). تتغيّر المنطقة الثابتة للسلسلة الثقيلة وتبقى المتغيّرة كما هي، فتُحفظ النوعية والألفة. ويحدث في الخلايا البائية المنشّطة، وتنظّمه الخلايا التائية المساعدة بالتماسّ والسيتوكينات (IL-4، IL-5، IFN-γ، TGF-β)، بآلية إعادة اتحاد تبديل الصنف (CSR)."),
]

# merge: new questions go at the end of their topic (before the next topic heading); a new topic is added before the picture questions
mcq, topic = [], None
for m in old["mcq"]:
    if "topic_en" in m:
        if topic in NEW: mcq += NEW.pop(topic)
        if m["topic_en"] == "Picture questions" and "Protective functions" in NEW:
            mcq += [{"topic_en": "Protective functions", "topic_ar": "الوظائف الوقائية"}] + NEW.pop("Protective functions")
        topic = m["topic_en"]
    mcq.append(copy.deepcopy(m))
assert not NEW, NEW.keys()
mcq = balance(mcq, 41)
tf = old["tf"] + NEW_TF
traps = old["traps"] + NEW_TR
important = old["important"] + NEW_IM

d = "/home/user/-/" + FOLDER
os.makedirs(d + "/assets", exist_ok=True)
for m in mcq:
    if m.get("img"):
        shutil.copy(os.path.join(SRC, m["img"]), os.path.join(d, m["img"]))
meta = {"subject_en": "Immunology", "subject_ar": "علم المناعة", "short_ar": "مناعة", "instructor": "د. أحمد داود",
        "unit_en": "Lecture 4", "unit_ar": "المحاضرة 4", "unit_label": "LEC", "unit_no": "4",
        "title_en": "Immunoglobulins (Ig)", "title_ar": "الغلوبيولينات المناعية (الأضداد)",
        "kind": "Theory — نظري", "stage": "The third stage — الثالثة",
        "file_name": "BIOS - مناعة نظري المحاضرة الرابعة - الأسئلة"}
Qs = {"title_en": "Immunoglobulins (Ig) — Comprehensive Questions", "title_ar": "الغلوبيولينات المناعية — أسئلة شاملة",
      "mcq": ltr_all(mcq), "tf": ltr_all(tf), "traps": ltr_all(traps), "important": ltr_all(important)}
json.dump({"meta": meta, "questions": Qs}, open(d + "/lecture.json", "w"), ensure_ascii=False, indent=1)
from collections import Counter
qs = [m for m in mcq if "answer" in m]
print(FOLDER, len(qs), dict(Counter(m["answer"] for m in qs)), len(tf), len(traps), len(important))
