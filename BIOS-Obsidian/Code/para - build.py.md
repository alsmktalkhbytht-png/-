---
source: BIOS-Obsidian/tools/scripts/para/build.py
handouts: []
saved: 2026-10-31
tags: [bios, code]
---
# para/build.py

MCQ banks: cleaning, translation tables, BIOS flags, inline answers.

```python
import json, re, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ar1 import AR as A1
from ar2 import AR as A2
AR = {**A1, **{str(k) if isinstance(k, str) else k: v for k, v in A2.items()}}
Q = [x for x in json.load(open(os.path.join(os.path.dirname(__file__), 'q.json'))) if 'stem' in x]
for i, q in enumerate(Q, 1): q['id'] = i

GENUS = r"(Entamoeba|Enbtamoeba|Giardia|Naegleria|Naegeleria|Naegelria|Iodamoeba|Iodomoeba|Endolimax|Endolemax|Toxoplasma|Trichomonas|Leishmania|Dientamoeba|Balantidium|Isospora|Cryptosporidium|Trypanosoma|Plasmodium|Ascaris|Diphyllobothrium|Amoeba)"
def clean(s):
    s = s.replace('⟦*⟧', '').replace('⟦', '').replace('⟧', '')
    for a, b in [("N o", "No"), ("N ormally", "Normally"), ("N ot", "Not"), ("P aratenic", "Paratenic"), ("T etranucleated", "Tetranucleated"),
                 ("I ts", "Its"), ("can’t survive . without it", "can’t survive without it"), ("brain . tissue", "brain tissue"), ("includes :", "includes:")]:
        s = s.replace(a, b)
    s = re.sub(r"\s\.(?=[A-Za-z])", " ", s)
    s = re.sub(r"^[\s.\-–]+", "", s); s = re.sub(r"\s+\.$", "", s).strip()
    if "__" not in s:
        s = re.sub(GENUS + r"(\s+(?!spp)[a-z]+)?", lambda m: f"__{m.group(0)}__" if m.group(2) else m.group(0), s)
    return re.sub(r"\s+", " ", s).strip()

FIX = {   # id -> (options, answer) where the PDF layout garbled them
 44: (None, "B"), 60: (["Enter host indirectly", "Plasmodium spp", "__Endolemax nana__", "__Giardia lamblia__", "Enter host di [[cut]]"], "B"),
 83: (["Ciliaphora", "__Giardia lamblia__", "__Entamoeba histolytica__", "Apicomplexa", "Microsporidia"], "C"),
 89: (None, "C,D"),
 122: (["Light to dark brown", "Pale yellow", "Steatorrhea", "Dysentery", "Clay"], "A"),
 171: (["__E. histolytica__", "__E. coli__", "__E. gingivalis__", "__Dientamoeba fragilis__", "None of these"], "C"),
 181: (["Less pathogenic than __E. histolytica__", "Larger than __E. histolytica__", "Trophozoite with blood", "lives outside the body", "Enter host by penetration"], "A"),
 183: (["Cryptosporidium", "__T. vaginalis__", "__E. histolytica__", "__E. coli__", "__E. gingivalis__"], "C"),
 186: (None, "E"),
 197: (["Cytoplasm of trophozoites finely granular", "Few ingested bacteria or debris may be present", "Presence of RBCs within cytoplasm of the trophozoite is diagnostic features for identification of __E. dispar__", "Ingested RBCs are not frequently seen", "In the absence of diagnostic characteristic __E. histolytica / E. dispar__ should be reported"], "C"),
}
SPLIT152 = [
 ("152", "Formalin, characterized by…except:", ["Difficult in preparation", "10% Fixative", "Easy to prepare", "Long shelf life", "Good preservation of morphology of helminthes eggs, larvae, protozoa cyst and coccidian"], "A"),
 ("152b", "formalin, Suitable for:", ["Concentration procedure", "UV fluorescence 10% microscopy", "Suitable for acid -fast Safranin, Chromotrope stains", "Difficult in preparation", "Not suitable for some permanent smear stained with trichrome"], "D"),
 ("152c", "disadvantages of 10% Formaling including:", ["Not suitable for some permanent smear stained with trichrome", "Inadequate preservation of morphology of protozoan trophozoites", "Interfere with PCR especially after extended fixation time", "All", "No one of above"], "D"),
]
EXC = ("The stem has no \"except\", but the marked option is the only wrong statement — the question is meant as \"… except\". The answer is kept as marked.",
       "السؤال بلا كلمة «except» لكن الخيار المؤشَّر هو العبارة الخاطئة الوحيدة، أي أن المقصود «… ما عدا». أبقينا الحل كما هو.")
NOTE = {k: EXC for k in [78, 79, 82, 117, 127, 129, 132, 133, 139, 147, 148, 149, 150, 151, "152b", 157, 159, 192, 196, 197]}
NOTE.update({
 9: ("Getting rid of the plasma membrane (surface antigens) is antigenic shedding (B); antigenic variation means changing the surface antigens.",
     "التخلّص من الغشاء البلازمي (المستضدات السطحية) هو انسلاخ المستضدات (B)؛ أما التغيّر المستضدي فهو تبديل المستضدات السطحية."),
 13: ("\"Eating at the same table\" is the literal meaning of commensalism (D): com = together, mensa = table.",
      "«الأكل على المائدة نفسها» هو المعنى الحرفي للمعايشة (D): ‏com = معًا وmensa = مائدة."),
 51: ("This is the definition of a paratenic (transport) host (A), not a reservoir host.", "هذا تعريف المضيف الناقل Paratenic ‏(A)، لا المضيف الخازن."),
 56: ("Invasion of the body by a pathogenic organism is parasitic infection (D); the infective stage is the stage able to enter the host.",
      "غزو الجسم بكائن ممرض هو العدوى الطفيلية (D)؛ أما الطور المعدي فهو الطور القادر على دخول المضيف."),
 60: ("Option E is cut off in the source (\"Enter host di…\").", "الخيار E مقطوع في المصدر («Enter host di…»)."),
 77: ("Option C is missing in the source (A, B, D, E); the four options are shown here as A–D.", "الخيار C غير موجود في المصدر (A وB وD وE)؛ وعُرضت الخيارات الأربعة هنا A–D."),
 89: ("Both C and D are marked in the source; D (A and C) is the complete answer.", "الخياران C وD مؤشَّران في المصدر؛ والإجابة الكاملة هي D ‏(A وC)."),
 103: ("__E. histolytica__ does cause bloody diarrhea, so it cannot be the \"except\" answer; the other options do not — the word \"except\" seems to be a mistake.",
       "`__E. histolytica__` تسبّب الإسهال الدموي فعلًا، فلا يمكن أن تكون إجابة «ما عدا»؛ وبقية الخيارات لا تسبّبه — يبدو أن كلمة «except» خطأ."),
 121: ("Trophozoites are found mainly in liquid and soft (semi-formed) stool; formed stool usually contains cysts.",
       "توجد الأطوار النشطة أساسًا في البراز السائل والطري (شبه المتشكّل)؛ أما البراز المتشكّل فيحتوي غالبًا الأكياس."),
 124: ("Iron and bismuth intake (A, B) also make the stool dark/black; intestinal (upper GI) hemorrhage gives black tarry stool.",
       "تناول الحديد والبزموت (A وB) يجعل البراز غامقًا/أسود أيضًا؛ والنزف المعوي (العلوي) يعطي برازًا أسود قطرانيًا."),
 140: ("All of the listed specimens (A–D) are examined directly for tissue protozoa; \"No one\" contradicts them — the expected answer would be \"All\", which is not an option.",
       "كل العيّنات المذكورة (A–D) تُفحص مباشرة للأوالي النسيجية؛ و«لا شيء» يناقضها — والإجابة المتوقّعة «جميعها» وهي غير موجودة بين الخيارات."),
 168: ("__Entamoeba coli__ is a worldwide NON-pathogenic intestinal amoeba (D).", "`__Entamoeba coli__` أميبا معوية **غير ممرضة** عالمية الانتشار (D)."),
 171: ("__Dientamoeba fragilis__ (D) also has no known cyst stage, like __E. gingivalis__.", "`__Dientamoeba fragilis__` ‏(D) أيضًا ليس لها طور كيس معروف، مثل `__E. gingivalis__`."),
 186: ("The letter \"A\" is also bold in the source; the bold option text is E, so E is taken as the answer.", "الحرف «A» عريض أيضًا في المصدر؛ لكن نص الخيار العريض هو E، فاعتُمد E حلًا."),
 195: ("__E. histolytica__ and __E. dispar__ are morphologically identical, so direct microscopy cannot differentiate them; ELISA (C) is the recommended method. The marked answer fits only an \"except\" question.",
       "`__E. histolytica__` و`__E. dispar__` متطابقتان شكليًا، فلا يميّز بينهما الفحص المجهري المباشر؛ والطريقة الموصى بها ELISA ‏(C). والحل المؤشَّر يصح فقط إذا كان السؤال «ما عدا»."),
})
TOPIC = {1: ("Classification and general terms", "التصنيف والمصطلحات العامة"), 13: ("Associations: symbiosis, mutualism, commensalism, parasitism", "العلاقات: التعايش والتقايض والمعايشة والتطفّل"),
 28: ("Types of parasites", "أنواع الطفيليات"), 45: ("Host and life cycle", "المضيف ودورة الحياة"),
 61: ("Protozoa", "الأوالي"), 77: ("Stool collection and preservatives", "جمع البراز والمواد الحافظة"),
 83: ("Sarcodina: __Entamoeba histolytica__", "اللحميات: `__Entamoeba histolytica__`"), 117: ("Stool examination", "فحص البراز"),
 141: ("Preservatives, concentration and stains", "المواد الحافظة والتركيز والصبغات"), 153: ("Microscopy and other diagnostic methods", "الفحص المجهري وطرائق التشخيص الأخرى"),
 164: ("__Entamoeba coli__", "`__Entamoeba coli__`"), 171: ("__Entamoeba gingivalis__ and other nonpathogenic amoebae", "`__Entamoeba gingivalis__` والأميبات غير الممرضة الأخرى"),
 187: ("__Naegleria fowleri__", "`__Naegleria fowleri__`"), 192: ("Differentiation of __E. histolytica__ and __E. dispar__", "التمييز بين `__E. histolytica__` و`__E. dispar__`")}
WEEK = {1: ("Terms used in Parasitology", "المصطلحات المستعملة في علم الطفيليات", "الأول"), 2: ("Protozoa", "الأوالي", "الثاني"),
        3: ("Sarcodina: Entamoeba histolytica", "اللحميات: الأميبا الحالّة للنسيج", "الثالث"),
        4: ("Nonpathogenic Intestinal Amoeba", "الأميبات المعوية غير الممرضة", "الرابع"), 5: ("Pathogenic free – living Amoebae", "الأميبات حرّة المعيشة الممرضة", "الخامس")}

TR = {
 "Amastigote": "الطور عديم السوط (Amastigote)", "Promastigote": "الطور أمامي السوط (Promastigote)", "Epimastigote": "الطور فوق السوطي (Epimastigote)",
 "Trypomastigote": "الطور المثقبي السوطي (Trypomastigote)", "Amoebozoa": "الأميبيات (Amoebozoa)", "Apicomplexa": "معقّدات القمة (Apicomplexa)",
 "Cestoda": "الشريطيات (Cestoda)", "Chromista": "الكروميستا (Chromista)", "Ciliaphora": "الهدبيات (Ciliaphora)", "Ciliophora": "الهدبيات (Ciliophora)",
 "Ciliophoran": "الهدبيات (Ciliophoran)", "Cryptosporidium": "الأبواغ الخفية (Cryptosporidium)", "ELISA": "مقايسة الممتز المناعي المرتبط بالإنزيم (ELISA)",
 "Excavate": "المحفورات (Excavata)", "IFA": "التألّق المناعي غير المباشر (IFA)", "IHA": "التلازن الدموي غير المباشر (IHA)",
 "Leishmania": "الليشمانيا", "Maalox": "مالوكس (مضاد حموضة)", "Mastigophora": "السوطيات (Mastigophora)", "Microsporidia": "الأبواغ الدقيقة (Microsporidia)",
 "Opisthokonta": "خلفيات السوط (Opisthokonta)", "PeptoMismol": "بيبتو بيسمول (مركّب بزموت)", "Plasmosis": "Plasmosis (مصطلح غير معروف)",
 "Platyhelminthes": "الديدان المسطّحة (Platyhelminthes)", "SAR": "مجموعة SAR (السترامينوبيلات والحويصليات والشعاعيات)",
 "Sarcomastigophora": "اللحميات السوطية (Sarcomastigophora)", "Toxoplasma": "المقوّسة", "Trypanosoma": "المثقبية", "A++": "A++", 
}
SP = {"Amoeba proteus": "الأميبا المتقلّبة", "Ascaris lumbricoides": "الصفر الخراطيني (الأسكارس)", "Balantidium coli": "القربية القولونية",
 "Cryptosporidium parvum": "الأبواغ الخفية الصغيرة", "Dientamoeba fragilis": "الأميبا ثنائية النواة الهشّة", "Diphyllobothrium latum": "الشريطية السمكية العريضة",
 "E. coli": "الأميبا القولونية", "E. gingivalis": "الأميبا اللثوية", "E. histolytica": "الأميبا الحالّة للنسيج", "Endolemax nana": "الأميبا القزمة",
 "Endolimax nana": "الأميبا القزمة", "Entamoeba coli": "الأميبا القولونية", "Entamoeba gingivalis": "الأميبا اللثوية", "Entamoeba hartmani": "أميبا هارتمان",
 "Entamoeba hartmanii": "أميبا هارتمان", "Entamoeba hartmanni": "أميبا هارتمان", "Entamoeba histolytica": "الأميبا الحالّة للنسيج", "Entamoeba polecki": "أميبا بوليكي",
 "Giardia lamblia": "الجيارديا اللمبلية", "Iodamoeba buetschlii": "الأميبا اليودية", "Iodamoeba butschlii": "الأميبا اليودية", "Iodamoeba butschlli": "الأميبا اليودية",
 "Iodomoeba buetschlii": "الأميبا اليودية", "Isospora belli": "متساوية الأبواغ البيلية", "Leishmania donovani": "الليشمانيا الدونوفانية",
 "Naegeleria fowleri": "النيغلرية الفاولرية", "Naegleria fowleri": "النيغلرية الفاولرية", "Plasmodium vivax": "المتصوّرة النشيطة", "T. vaginalis": "المشعّرة المهبلية",
 "Toxoplasma gondii": "المقوّسة الغوندية", "Trichomonas vaginalis": "المشعّرة المهبلية", "Trypanosoma cruzi": "المثقبية الكروزية"}
def tr(e):
    if e in TR: return TR[e]
    parts = [x.strip() for x in e.split(" : ")]
    out = []
    for x in parts:
        k = x.strip("_ ")
        if k not in SP: return None
        out.append(SP[k])
    return " : ".join(out)

def mk(key, stem, opts, ans):
    sa, oa = AR[key]
    assert len(oa) == len(opts), (key, len(oa), len(opts))
    q = {"en": clean(stem), "ar": sa, "options": [[clean(o), a if a is not None and a != clean(o) else (tr(clean(o)) or clean(o))] for o, a in zip(opts, oa)], "answer": ans}
    if key in NOTE: q["note_en"], q["note_ar"] = NOTE[key]
    return q

weeks = {w: [] for w in WEEK}
for q in Q:
    i = q['id']
    if i in TOPIC: weeks[q['week']].append({"topic_en": TOPIC[i][0], "topic_ar": TOPIC[i][1]})
    if i == 152:
        for key, stem, opts, ans in SPLIT152: weeks[3].append(mk(key, stem, opts, ans))
        continue
    opts, ans = FIX.get(i, (None, None))
    weeks[q['week']].append(mk(i, q['stem'], opts or q['opts'], ans or ",".join(q['ans'])))

for w, items in weeks.items():
    t_en, t_ar, ordw = WEEK[w]
    n = sum(1 for x in items if "en" in x)
    flagged = sum(1 for x in items if x.get("note_en"))
    meta = {"subject_en": "Diagnostic Parasitology", "subject_ar": "الطفيليات التشخيصية", "instructor": "أ.د. نزار الخفاجي",
            "unit_en": f"Week {w}", "unit_ar": f"الأسبوع {w}", "unit_label": "WEEK", "unit_no": str(w), "title_en": t_en, "title_ar": t_ar,
            "department": "قسم التحليلات", "stage": "The fourth stage — الرابعة", "kind": "Theory — نظري", "questions_kind": "MCQ — أسئلة اختيار",
            "file_name": f"BIOS - طفيليات نظري الأسبوع {ordw} - الأسئلة", "short_ar": "طفيليات"}
    qs = {"title_en": t_en, "title_ar": t_ar, "sub": "MCQ", "answers_inline": True,
          "mcq_en": f"MCQ — 1st semester, week {w}", "mcq_ar": f"أسئلة الاختيار — الفصل الأول، الأسبوع {ordw}",
          "intro_en": ["Q. Select the most correct answer from the followings", "The answer under each question is the one marked in the source file, kept as it is; a BIOS note flags any answer that is unsolved, doubtful or wrong."],
          "intro_ar": ["س. اختر الإجابة الأصح مما يأتي", "الحل تحت كل سؤال هو المؤشَّر في الملف الأصلي كما هو؛ وملاحظة BIOS تنبّه على أي سؤال غير محلول أو حلّه مشكوك فيه أو خاطئ."],
          "mcq": items}
    d = f"/home/user/-/parasitology-week{w}-mcq"; os.makedirs(d, exist_ok=True)
    json.dump({"meta": meta, "questions": qs}, open(d + "/lecture.json", "w"), ensure_ascii=False, indent=1)
    print(w, n, "questions,", flagged, "flagged")

```
