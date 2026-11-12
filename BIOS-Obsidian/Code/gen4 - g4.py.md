---
source: BIOS-Obsidian/tools/scripts/gen4/g4.py
handouts: [genetics-lab4-mendelian-genetics]
saved: 2026-11-12
tags: [bios, code]
---
# gen4/g4.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#genetics-lab4-mendelian-genetics|genetics-lab4-mendelian-genetics]]

```python
import sys; sys.path.insert(0, "/tmp/claude-0/-home-user-kwmdkm/a7dd109e-db53-5fd3-8234-9dab3a530e24/scratchpad/imm456")
from ci import *            # c helpers + B INSHORT TERMS balance save(split.fix)
from itertools import product
from collections import Counter

# Human genetics practical, lab 4 — source: lab_4_1_3.docx (header "Human genetic lab. 4 Noor. M. Fadhil Stage 3");
# instructor as the user gave it: د. فردوس عثمان
GL = dict(subject_en="Human Genetics", subject_ar="الوراثة البشرية", short_ar="وراثة", unit_label="LAB",
          kind="Laboratories — عملي", stage="The third stage — الثالثة", instructor="د. فردوس عثمان")
BN = lambda en, ar: N(en, ar, label=["BIOS note", "ملاحظة BIOS"])
BS = lambda en, ar: N(en, ar, label=["BIOS solution", "حل BIOS"])


# ------------------------------------------------------------------ Punnett squares
def _geno(a, b):
    """join two gametes gene by gene, dominant letter first: 'BR' + 'br' -> 'BbRr'."""
    return "".join("".join(sorted(x + y, key=lambda c: (c.islower(), c))) for x, y in zip(a, b))


def square(g1, g2, who1=("", ""), who2=("", "")):
    """Punnett square: rows = gametes of parent 1, columns = gametes of parent 2."""
    head = [B("Gametes", "الأمشاج")] + [f"**{g}**" for g in g2]
    rows = [[f"**{a}**"] + [_geno(a, b) for b in g2] for a in g1]
    w = 100 / (len(g2) + 1.4)
    return T(head, rows, key_cols=[0], widths=[round(w * 1.4)] + [round(w)] * len(g2))


def ratio(g1, g2, names, label_en="Ratio", label_ar="النسبة"):
    """phenotype classes of a cross; names: {letter: (en, ar)} for the dominant and recessive letter of each gene."""
    genos = Counter(_geno(a, b) for a in g1 for b in g2)
    total = sum(genos.values())
    cls = {}
    for g, n in genos.items():
        key = tuple(g[i] if g[i].isupper() else g[i + 1] for i in range(0, len(g), 2))   # one letter per gene
        cls.setdefault(key, []).append((g, n))
    order = sorted(cls, key=lambda k: (-sum(n for _, n in cls[k]), [c.islower() for c in k]))
    rows = []
    for k in order:
        n = sum(x for _, x in cls[k])
        en = " ".join(names[c][0] for c in k)
        ar = " و".join(names[c][1] for c in k)
        gs = ", ".join(f"{x} {g}" if x > 1 else g for g, x in sorted(cls[k], key=lambda t: (-t[1], t[0])))
        rows.append([B(f"**{en}**", f"**{ar}**"), gs, f"**{n}/{total}**"])
    return T([B("Phenotype", "المظهر"), B("Genotypes (number of boxes)", "التراكيب الوراثية (عدد المربعات)"), B("Ratio", "النسبة")],
             rows, key_cols=[0], widths=[38, 42, 20], style="summary", label_en=label_en, label_ar=label_ar)


blocks = [
 # ------------------------------------------------------------------ 1 terms
 SEC("Basic terms", "المصطلحات الأساسية"),
 H2("**Mendelian Genetics**:", "**الوراثة المندلية:**"),
 L(["**Alleles** – two genes that occupy the same position on homologous chromosomes and that cover the same trait (like ‘flavors’ of a trait).",
    "**Homozygous** – having identical genes (one from each parent) for a particular characteristic.",
    "**Heterozygous** – having two different genes for a particular characteristic.",
    "**Dominant** – the allele of a gene that masks or suppresses the expression of an alternate allele; the trait appears in the heterozygous condition.",
    "**Recessive** – an allele that is masked by a dominant allele; does not appear in the heterozygous condition, only in homozygous."],
   ["**الأليلات (`Alleles`)** – جينان يشغلان الموقع نفسه على كروموسومين متماثلين ويخصّان الصفة نفسها (مثل «نكهات» الصفة الواحدة).",
    "**متماثل الأليلات / نقي (`Homozygous`)** – يحمل جينين متطابقين (واحد من كل أب) لصفة معيّنة.",
    "**متغاير الأليلات / هجين (`Heterozygous`)** – يحمل جينين مختلفين لصفة معيّنة.",
    "**السائد (`Dominant`)** – أليل الجين الذي يحجب أو يثبّط ظهور الأليل البديل؛ فتظهر الصفة في الحالة الهجينة.",
    "**المتنحّي (`Recessive`)** – أليل يحجبه الأليل السائد؛ لا يظهر في الحالة الهجينة، بل في الحالة النقية فقط."]),
 L(["**Genotype** – the genetic makeup of an organisms .",
    "**Phenotype** – the physical appearance of an organism (Genotype + environment).",
    "**Monohybrid cross**: a genetic cross involving a single pair of genes (one trait); parents differ by a single trait."],
   ["**التركيب الوراثي / الطراز الجيني (`Genotype`)** – المكوّنات الوراثية للكائن الحي.",
    "**المظهر / الطراز المظهري (`Phenotype`)** – الشكل الظاهري للكائن الحي (التركيب الوراثي + البيئة).",
    "**التهجين الأحادي (`Monohybrid cross`):** تهجين وراثي يخصّ زوجًا واحدًا من الجينات (صفة واحدة)؛ ويختلف الأبوان بصفة واحدة."], start=6),
 L(["**P = Parental generation**", "**F1 = First filial generation; offspring from a genetic cross.**", "**F2 = Second filial generation of a genetic cross**"],
   ["**P = جيل الآباء**", "**F1 = الجيل الأول من الأبناء؛ النسل الناتج من تهجين وراثي.**", "**F2 = الجيل الثاني من الأبناء في التهجين الوراثي**"], alpha=True),
 T([B("Example", "مثال"), B("Genotype", "التركيب الوراثي"), B("Phenotype", "المظهر")],
   [[B("Homozygous dominant", "نقي سائد"), "**TT**", B("tall", "طويل")],
    [B("Heterozygous", "هجين"), "**Tt**", B("tall (T masks t)", "طويل (T يحجب t)")],
    [B("Homozygous recessive", "نقي متنحٍّ"), "**tt**", B("dwarf", "قزم")]],
   key_cols=[0], widths=[36, 24, 40], style="summary", label_en="BIOS example: one gene, three genotypes", label_ar="مثال BIOS: جين واحد وثلاثة تراكيب"),
 INSHORT([("Alleles = 2 forms of one gene at the **same position** on homologous chromosomes.", "الأليلات = شكلان لجين واحد في **الموقع نفسه** على الكروموسومين المتماثلين."),
          ("**Homozygous** = identical (TT, tt); **heterozygous** = different (Tt).", "**النقي** = متطابقان (TT، tt)؛ و**الهجين** = مختلفان (Tt)."),
          ("Dominant shows in **Tt**; recessive shows **only in tt**.", "السائد يظهر في **Tt**؛ والمتنحّي يظهر **في tt فقط**."),
          ("Phenotype = **genotype + environment**.", "المظهر = **التركيب الوراثي + البيئة**."),
          ("**P** parents → **F1** offspring → **F2** second generation.", "**P** الآباء ← **F1** الأبناء ← **F2** الجيل الثاني.")]),

 # ------------------------------------------------------------------ 2 first law
 SEC("Mendel's First Law", "قانون مندل الأول"),
 H2("**Mendel's First Law (the law of segregation;)**", "**قانون مندل الأول (قانون الانعزال)**"),
 C("during gamete formation each member of the allelic pair separates from the other member to form the genetic constitution of the gamete.",
   "أثناء تكوين الأمشاج ينفصل كل فرد من زوج الأليلات عن الفرد الآخر، ليكوّن التركيب الوراثي للمشيج."),
 FLOW([("Tt (parent)", "Tt (الأب)"), ("T and t separate", "ينفصل T عن t"), ("½ gametes T + ½ gametes t", "نصف الأمشاج T ونصفها t")],
      en="Segregation in one picture", ar="الانعزال بصورة واحدة"),
 H2("**Mendel’s peas**", "**بازلاء مندل**"),
 C("• Mendel looked at seven traits or characteristics of pea plants:", "• درس مندل سبع صفات أو خصائص في نبات البازلاء:"),
 F("pea-seven-traits.png", "7 Characteristics in Peas", "الصفات السبع في البازلاء", h="62mm"),
 T([B("Trait", "الصفة"), B("Characteristic (upper row)", "الخاصية (الصف الأعلى)"), B("Characteristic (lower row)", "الخاصية (الصف الأسفل)")],
   [[B("**Stem length**", "**طول الساق**"), B("Tall", "طويل"), B("Dwarf", "قزم")],
    [B("**Pod shape**", "**شكل القرنة**"), B("Inflated", "منتفخة"), B("Constricted", "متخصّرة (مضغوطة)")],
    [B("**Seed shape**", "**شكل البذرة**"), B("Smooth", "ملساء"), B("Wrinkled", "مجعّدة")],
    [B("**Seed color**", "**لون البذرة**"), B("Yellow", "صفراء"), B("Green", "خضراء")],
    [B("**Flower position**", "**موقع الزهرة**"), B("Lateral", "جانبي (إبطي)"), B("Terminal", "طرفي")],
    [B("**Flower color**", "**لون الزهرة**"), B("Purple", "بنفسجي"), B("White", "أبيض")],
    [B("**Pod color**", "**لون القرنة**"), B("Green", "خضراء"), B("Yellow", "صفراء")]],
   key_cols=[0], widths=[30, 35, 35], label_en="Figure text", label_ar="كتابات الشكل"),
 BN("In Mendel's results the **upper row is the dominant form** of each trait (tall, inflated, smooth, yellow seed, lateral/axial, purple, green pod) and the lower row is recessive.",
    "في نتائج مندل يكون **الصف الأعلى هو الشكل السائد** لكل صفة (طويل، منتفخة، ملساء، بذرة صفراء، جانبي/إبطي، بنفسجي، قرنة خضراء)، والصف الأسفل متنحٍّ."),
 C(["**1- Example -** Pure tall plants are homozygous and, therefore/possess genes (factors) TT; similarly dwarf possess genes tt.",
    "The tallness and dwarf are two independent but contrasting factors or determiners.",
    "Pure tall plants produce gametes all of which possess gene T and dwarf plants t type of gametes ."],
   ["**1. مثال –** النباتات الطويلة النقية متماثلة الأليلات، ولذلك تحمل الجينات (العوامل) TT؛ وبالمثل تحمل النباتات القزمة الجينات tt.",
    "والطول والقِصَر عاملان أو محدِّدان مستقلّان لكنهما متضادّان.",
    "والنباتات الطويلة النقية تنتج أمشاجًا كلها تحمل الجين T، والنباتات القزمة تنتج أمشاجًا من نوع t."]),
 BS("P: **TT × tt** → gametes T and t → F1 all **Tt (tall)**. F1 × F1 (Tt × Tt) gives the F2 below: genotypes **1 TT : 2 Tt : 1 tt**, phenotypes **3 tall : 1 dwarf**.",
    "الآباء (P): **TT × tt** ← أمشاج T وt ← الجيل F1 كله **Tt (طويل)**. وتهجين F1 × F1 (Tt × Tt) يعطي الجيل F2 في الأسفل: التراكيب **1 TT : 2 Tt : 1 tt**، والمظاهر **3 طويل : 1 قزم**."),
 square(["T", "t"], ["T", "t"], ("Tt", "Tt"), ("Tt", "Tt")),
 C(["2- Explain on the bases of genetic principle , crossing between two pea plants of hybrid smooth seeds .",
    "knowing that smooth seeds traits ( R) is dominant & wrinkled seeds traits (r) is recessive ."],
   ["2. اشرح على أساس المبدأ الوراثي التهجين بين نباتَي بازلاء هجينَي البذور الملساء.",
    "علمًا أن صفة البذور الملساء (R) سائدة، وصفة البذور المجعّدة (r) متنحّية."]),
 BS("Hybrid smooth = **Rr**. **Rr × Rr**: each parent gives ½ R and ½ r (segregation). Result: genotypes **1 RR : 2 Rr : 1 rr**; phenotypes **3 smooth : 1 wrinkled**.",
    "الهجين الأملس = **Rr**. **Rr × Rr**: كل أب يعطي ½ R و½ r (الانعزال). النتيجة: التراكيب **1 RR : 2 Rr : 1 rr**؛ والمظاهر **3 ملساء : 1 مجعّدة**."),
 square(["R", "r"], ["R", "r"], ("Rr", "Rr"), ("Rr", "Rr")),
 C("3- What is the probability of  Yy X yy producing green seeds ?", "3. ما احتمال أن ينتج التهجين Yy × yy بذورًا خضراء؟"),
 BS("Yellow (Y) is dominant, so green = **yy**. **Yy × yy** → ½ Yy (yellow) + ½ yy (green). Probability of green seeds = **1/2 = 50%**.",
    "الأصفر (Y) سائد، فالأخضر = **yy**. **Yy × yy** ← ½ Yy (أصفر) + ½ yy (أخضر). احتمال البذور الخضراء = **1/2 = 50%**."),
 square(["Y", "y"], ["y", "y"], ("Yy", "Yy"), ("yy", "yy")),
 INSHORT([("First law = **segregation**: the 2 alleles separate into different gametes.", "القانون الأول = **الانعزال**: ينفصل الأليلان إلى أمشاج مختلفة."),
          ("Mendel studied **7 pea traits**.", "درس مندل **7 صفات** في البازلاء."),
          ("**TT × tt** → F1 all Tt; **Tt × Tt** → 1:2:1 genotypes, **3:1** phenotypes.", "**TT × tt** ← F1 كله Tt؛ و**Tt × Tt** ← تراكيب 1:2:1 ومظاهر **3:1**."),
          ("Test cross **Yy × yy** → **1:1** (50% green).", "التهجين الاختباري **Yy × yy** ← **1:1** (50% خضراء).")]),

 # ------------------------------------------------------------------ 3 human traits
 SEC("Mendelian traits in humans", "الصفات المندلية في الإنسان"),
 H2("**Mendelian traits in humans**", "**الصفات المندلية في الإنسان**"),
 C("Mendelian traits in humans concerns how, in Mendelian inheritance, a child receiving a dominant allele from either parent will have the dominant form of the phenotypic trait or characteristic. "
   "Only those that received the recessive allele from both parents, known as zygosity, will have the recessive phenotype. "
   "Those that receive a dominant allele from one parent and a recessive allele from the other parent will have the dominant form of the trait. "
   "Purely Mendelian traits are a tiny minority of all traits, since most phenotypic traits exhibit incomplete dominance, codominance, and contributions from many genes.",
   "تتعلّق الصفات المندلية في الإنسان بكيف أن الطفل الذي يستلم أليلًا سائدًا من أيّ من الأبوين، في الوراثة المندلية، يحمل الشكل السائد للصفة المظهرية أو الخاصية. "
   "وفقط من استلموا الأليل المتنحّي من كلا الأبوين، وهو ما يُعرف بالتماثل الأليلي (`zygosity`)، يظهر عليهم المظهر المتنحّي. "
   "ومن يستلمون أليلًا سائدًا من أحد الأبوين وأليلًا متنحّيًا من الآخر يحملون الشكل السائد للصفة. "
   "والصفات المندلية الصرفة أقلية صغيرة جدًا من بين كل الصفات، لأن أغلب الصفات المظهرية تُظهر السيادة غير التامّة، والسيادة المشتركة، ومساهمة جينات كثيرة."),
 BN("\"known as zygosity\": the correct word for receiving the recessive allele from both parents is **homozygosity** (homozygous recessive, e.g. aa).",
    "\"known as zygosity\": الكلمة الأدقّ لاستلام الأليل المتنحّي من الأبوين هي **homozygosity (التماثل الأليلي)**، أي نقي متنحٍّ مثل aa."),
 L(["Wet (dominant) or dry (recessive) earwax – dry is found mostly in Asians and Native American", "Albinism (recessive)", "Blood type", "Cystic fibrosis",
    "six fingers", "cleft chin", "Dimples", "Sickle-cell diseas"],
   ["شمع الأذن الرطب (سائد) أو الجاف (متنحٍّ) – والجاف يوجد غالبًا عند الآسيويين والأمريكيين الأصليين", "المَهَق (متنحٍّ)", "فصيلة الدم", "التليّف الكيسي",
    "الأصابع الستّ", "الذقن المشقوقة", "الغمّازات", "فقر الدم المنجلي"],
   en="**Some example of Mendelian traits in humans:**", ar="**بعض أمثلة الصفات المندلية في الإنسان:**"),
 L(["tens, or even hundreds of genes can play a role in just one trait", "genes can block or exaggerate processes in the cell which change the visible phenotype.",
    "environmental factors such temperature, light, and nutrient levels influence the development of a phenotype."],
   ["عشرات بل مئات الجينات قد تؤدّي دورًا في صفة واحدة فقط", "قد تحجب الجينات أو تضخّم عمليات في الخلية فتغيّر المظهر المرئي.",
    "العوامل البيئية مثل الحرارة والضوء ومستويات المغذّيات تؤثّر في تكوين المظهر."],
   en="Some traits were previously believed to be Mendelian, but their inheritance is more complicated than in those listed above or those which Mendel observed in his garden.",
   ar="كان يُعتقد سابقًا أن بعض الصفات مندلية، لكن وراثتها أعقد من الصفات المذكورة أعلاه أو التي لاحظها مندل في حديقته."),
 L(["Tongue rolling", "Eye color", "Hair color", "Detached (dominant) or attached (recessive) earlobes", "Skin color ."],
   ["لفّ اللسان", "لون العين", "لون الشعر", "شحمة الأذن المنفصلة (سائدة) أو الملتصقة (متنحّية)", "لون الجلد."],
   en=["Below is a list of traits in humans involving interaction between multiple genes (probably) based on more complex genetic models, possibly involving more than one gene.", "**These include:**"],
   ar=["فيما يلي قائمة بصفات في الإنسان تتضمّن تداخلًا بين جينات متعدّدة (على الأرجح)، مبنية على نماذج وراثية أعقد، وربما تشمل أكثر من جين واحد.", "**وتشمل:**"]),
 T([B("Mendelian (one gene)", "مندلية (جين واحد)"), B("More complex (many genes / environment)", "أعقد (جينات متعدّدة / بيئة)")],
   [[B("Wet / dry earwax", "شمع الأذن رطب / جاف"), B("Tongue rolling", "لفّ اللسان")],
    [B("Albinism", "المَهَق"), B("Eye color", "لون العين")],
    [B("Blood type", "فصيلة الدم"), B("Hair color", "لون الشعر")],
    [B("Cystic fibrosis, sickle-cell disease", "التليّف الكيسي، فقر الدم المنجلي"), B("Detached / attached earlobes", "شحمة الأذن منفصلة / ملتصقة")],
    [B("Six fingers, cleft chin, dimples", "الأصابع الستّ، الذقن المشقوقة، الغمّازات"), B("Skin color", "لون الجلد")]],
   widths=[50, 50], style="summary", label_en="Two lists to memorise", label_ar="قائمتان للحفظ"),
 INSHORT([("Dominant allele from **either** parent → dominant phenotype; recessive phenotype only when **both** parents give the recessive allele.", "أليل سائد من **أيّ** أب ← مظهر سائد؛ والمتنحّي فقط إذا أعطاه **كلا** الأبوين."),
          ("Pure Mendelian traits are a **tiny minority**.", "الصفات المندلية الصرفة **أقلية صغيرة جدًا**."),
          ("Why complex: **many genes**, genes **block/exaggerate** cell processes, **environment**.", "سبب التعقيد: **جينات كثيرة**، وجينات **تحجب/تضخّم** عمليات الخلية، و**البيئة**.")]),

 # ------------------------------------------------------------------ 4 second law
 SEC("Mendel's second Law", "قانون مندل الثاني"),
 H2("**Mendel's second  Law(Law of independent assortment)**", "**قانون مندل الثاني (قانون التوزيع المستقل)**"),
 C("Genes for different traits can segregate independently during the formation of gametes.", "يمكن لجينات الصفات المختلفة أن تنعزل بصورة مستقلة أثناء تكوين الأمشاج."),
 C(["**Explanation**: The cross was made between plants having yellow and round cotyledons and plants having green and wrinkled cotyledons .", "This law can be illustrated using dihybrid crosses."],
   ["**الشرح:** أُجري التهجين بين نباتات ذات فلقات صفراء ومستديرة ونباتات ذات فلقات خضراء ومجعّدة.", "ويمكن توضيح هذا القانون باستعمال التهجينات الثنائية."]),
 F("dihybrid-punnett.png", "Punnett Square of Dihybrid Cross (F1 cross: RrYy × RrYy)", "مربع بانيت للتهجين الثنائي (تهجين F1: RrYy × RrYy)", h="60mm"),
 T([B("Figure text", "كتابات الشكل"), B("Meaning", "المعنى")],
   [[B("**Gametes from RrYy parent**", "**أمشاج الأب RrYy**"), B("RY, Ry, rY, ry — 4 kinds, ¼ each", "RY، Ry، rY، ry — 4 أنواع، ربع لكل منها")],
    [B("**round yellow**", "**مستديرة صفراء**"), B("9 boxes (R_Y_)", "9 مربعات (R_Y_)")],
    [B("**round green**", "**مستديرة خضراء**"), B("3 boxes (R_yy)", "3 مربعات (R_yy)")],
    [B("**wrinkled yellow**", "**مجعّدة صفراء**"), B("3 boxes (rrY_)", "3 مربعات (rrY_)")],
    [B("**wrinkled green**", "**مجعّدة خضراء**"), B("1 box (rryy)", "مربع واحد (rryy)")]],
   key_cols=[0], widths=[40, 60], label_en="Figure text + BIOS count", label_ar="كتابات الشكل + عدّ BIOS"),
 FLOW([("P: RRYY × rryy", "الآباء: RRYY × rryy"), ("F1: all RrYy (round yellow)", "F1: كله RrYy (مستدير أصفر)"), ("F2: 9 : 3 : 3 : 1", "الجيل F2: 9 : 3 : 3 : 1")],
      en="Dihybrid cross", ar="التهجين الثنائي"),
 C(["2- A right- handed black – haired man married a left – handed blonde – haired woman .. the children were all black – haired right – handed .",
    "when the chidren reached puberty one of them married a girl genetically similar to him .",
    "what are the genetic and phenotypic structures of the first generation and the second generation ( the trait of black – haired B , Right – handed recipe R) ."],
   ["2. تزوّج رجل أيمن أسود الشعر من امرأة عسراء شقراء الشعر.. فكان الأبناء جميعًا سود الشعر يمينيين.",
    "وعندما بلغ الأبناء سنّ البلوغ تزوّج أحدهم من فتاة مشابهة له وراثيًا.",
    "ما التراكيب الوراثية والمظهرية للجيل الأول والجيل الثاني (صفة الشعر الأسود B، وصفة استعمال اليد اليمنى R)؟"]),
 BS("All children are black-haired right-handed, so the man is pure **BBRR** and the woman **bbrr**. F1: all **BbRr** (black-haired, right-handed). F2 (BbRr × BbRr, the girl is also BbRr):",
    "كل الأبناء سود الشعر يمينيون، إذن الرجل نقي **BBRR** والمرأة **bbrr**. الجيل F1: كله **BbRr** (أسود الشعر، أيمن). الجيل F2 (BbRr × BbRr، فالفتاة أيضًا BbRr):"),
 square(["BR", "Br", "bR", "br"], ["BR", "Br", "bR", "br"], ("BbRr", "BbRr"), ("BbRr", "BbRr")),
 ratio(["BR", "Br", "bR", "br"], ["BR", "Br", "bR", "br"],
       {"B": ("black-haired", "أسود الشعر"), "b": ("blonde-haired", "أشقر الشعر"), "R": ("right-handed", "أيمن"), "r": ("left-handed", "أعسر")}, "F2 phenotypes 9:3:3:1", "مظاهر F2 9:3:3:1"),
 BN("\"recipe R\" in the question means the **trait** (character) R = right-handed.", "\"recipe R\" في السؤال تعني **الصفة** R = استعمال اليد اليمنى."),
 C("3- work out each cross showing the square , the parents genotype .and the ratios .", "3. حلّ كل تهجين مع رسم المربع، وتراكيب الآباء الوراثية، والنسب."),
 C(["1- in guinea pigs , smooth coat ( S) is dominant over rough coat (s) and black coat (B) is dominant over white coat .", "cross two parents with the genotypes SsBb X SsBb ."],
   ["1. في خنازير غينيا، الفرو الأملس (S) سائد على الفرو الخشن (s)، والفرو الأسود (B) سائد على الفرو الأبيض.", "هجّن أبوين تركيبهما الوراثي SsBb × SsBb."]),
 BS("Parents **SsBb × SsBb**; each gives 4 gametes SB, Sb, sB, sb. Genotypes 1:2:1:2:4:2:1:2:1; phenotypes **9 : 3 : 3 : 1**.",
    "الآباء **SsBb × SsBb**؛ كل منهما يعطي 4 أمشاج SB وSb وsB وsb. التراكيب 1:2:1:2:4:2:1:2:1؛ والمظاهر **9 : 3 : 3 : 1**."),
 square(["SB", "Sb", "sB", "sb"], ["SB", "Sb", "sB", "sb"], ("SsBb", "SsBb"), ("SsBb", "SsBb")),
 ratio(["SB", "Sb", "sB", "sb"], ["SB", "Sb", "sB", "sb"],
       {"S": ("smooth", "أملس"), "s": ("rough", "خشن"), "B": ("black", "أسود"), "b": ("white", "أبيض")}, "Guinea pigs 9:3:3:1", "خنازير غينيا 9:3:3:1"),
 C(["2- in tomatoes , red fruit (R) is dominat over fruit (r ) and tallness ( T) is domint over shortness ( t) .", "Apant that is RrTT is crossed with a plant that is rrTt ."],
   ["2. في الطماطم، الثمرة الحمراء (R) سائدة على الثمرة (r)، والطول (T) سائد على القِصَر (t).", "يُهجَّن نبات تركيبه RrTT مع نبات تركيبه rrTt."]),
 BS("Gametes: RrTT → **RT, rT**; rrTt → **rT, rt**. Offspring: ¼ RrTT, ¼ RrTt, ¼ rrTT, ¼ rrTt → **all tall**; **1 red : 1 non-red (r) fruit**.",
    "الأمشاج: RrTT ← **RT وrT**؛ وrrTt ← **rT وrt**. النسل: ¼ RrTT و¼ RrTt و¼ rrTT و¼ rrTt ← **كلها طويلة**؛ و**1 ثمرة حمراء : 1 ثمرة غير حمراء (r)**."),
 square(["RT", "rT"], ["rT", "rt"], ("RrTT", "RrTT"), ("rrTt", "rrTt")),
 ratio(["RT", "rT"], ["rT", "rt"], {"R": ("red", "حمراء"), "r": ("non-red (r)", "غير حمراء (r)"), "T": ("tall", "طويلة"), "t": ("short", "قصيرة")}, "Tomatoes 1:1", "الطماطم 1:1"),
 BN("The colour of the recessive fruit (r) is missing in the sheet (\"over fruit (r )\"); in tomatoes it is usually **yellow**.",
    "لون الثمرة المتنحّية (r) ناقص في الملزمة (\"over fruit (r )\")؛ وفي الطماطم يكون عادةً **أصفر**."),
 C(["3- Suppose you cross a pure – breeding , black- coated dog with curly fur to apure- breeding , yellow – coated dog with straight fur.",
    "In the F1 generation, all the puppies have straight , black coats .", "next you interbreed the F1 dogs with one anther to get an F2 generation ?"],
   ["3. لنفترض أنك هجّنت كلبًا نقي السلالة أسود الفرو مجعّده مع كلب نقي السلالة أصفر الفرو أملسه (مستقيمه).",
    "في الجيل F1 كانت كل الجراء ذات فرو مستقيم أسود.", "ثم هجّنت كلاب F1 بعضها مع بعض لتحصل على الجيل F2؟"]),
 BS("F1 is all black and straight, so **black (B)** and **straight (S)** are dominant. P: **BBss × bbSS** → F1 **BbSs**. F2 (BbSs × BbSs) = **9 : 3 : 3 : 1**.",
    "الجيل F1 كله أسود ومستقيم، إذن **الأسود (B)** و**المستقيم (S)** سائدان. الآباء (P): **BBss × bbSS** ← F1 **BbSs**. والجيل F2 (BbSs × BbSs) = **9 : 3 : 3 : 1**."),
 square(["BS", "Bs", "bS", "bs"], ["BS", "Bs", "bS", "bs"], ("BbSs", "BbSs"), ("BbSs", "BbSs")),
 ratio(["BS", "Bs", "bS", "bs"], ["BS", "Bs", "bS", "bs"],
       {"B": ("black", "أسود"), "b": ("yellow", "أصفر"), "S": ("straight", "مستقيم"), "s": ("curly", "مجعّد")}, "Dogs F2 9:3:3:1", "الكلاب F2 9:3:3:1"),
 C(["4- what are the genotype and phenotype ratios in the offspring resulting from a cross between two pea plants that are heterozygous for pod color and pod shape ?",
    "Pod shape ( smooth   N ) ( constricted   n )", "Pod color (  green   G )  ( Yellow   g ) ?"],
   ["4. ما نسب التراكيب الوراثية والمظاهر في النسل الناتج من تهجين نباتَي بازلاء هجينين للون القرنة وشكلها؟",
    "شكل القرنة (ملساء N) (متخصّرة n)", "لون القرنة (خضراء G) (صفراء g)؟"]),
 BS("Both parents **GgNn**; gametes GN, Gn, gN, gn. Genotype ratio **1 : 2 : 1 : 2 : 4 : 2 : 1 : 2 : 1** (9 genotypes); phenotype ratio **9 : 3 : 3 : 1**.",
    "الأبوان **GgNn**؛ والأمشاج GN وGn وgN وgn. نسبة التراكيب **1 : 2 : 1 : 2 : 4 : 2 : 1 : 2 : 1** (9 تراكيب)؛ ونسبة المظاهر **9 : 3 : 3 : 1**."),
 square(["GN", "Gn", "gN", "gn"], ["GN", "Gn", "gN", "gn"], ("GgNn", "GgNn"), ("GgNn", "GgNn")),
 ratio(["GN", "Gn", "gN", "gn"], ["GN", "Gn", "gN", "gn"],
       {"G": ("green", "خضراء"), "g": ("yellow", "صفراء"), "N": ("smooth", "ملساء"), "n": ("constricted", "متخصّرة")}, "Pea pods 9:3:3:1", "قرون البازلاء 9:3:3:1"),
 INSHORT([("Second law = **independent assortment**: genes of different traits separate independently.", "القانون الثاني = **التوزيع المستقل**: جينات الصفات المختلفة تنعزل باستقلال."),
          ("Dihybrid **AaBb** makes **4 gametes** (¼ each) → 16-box square.", "الهجين الثنائي **AaBb** يكوّن **4 أمشاج** (ربع لكل منها) ← مربع من 16 خانة."),
          ("AaBb × AaBb → phenotypes **9:3:3:1**, genotypes **1:2:1:2:4:2:1:2:1**.", "AaBb × AaBb ← مظاهر **9:3:3:1**، وتراكيب **1:2:1:2:4:2:1:2:1**."),
          ("All F1 show one form → that form is **dominant** and the parents were **pure**.", "إذا ظهر شكل واحد في كل F1 ← فهو **السائد** والآباء **نقية**.")]),
] + TERMS([
 ("Allele", "أليل / الشكل البديل للجين"),
 ("Homozygous", "متماثل الأليلات / نقي / أصيل"),
 ("Heterozygous", "متغاير الأليلات / هجين / خليط"),
 ("Dominant", "سائد / غالب"),
 ("Recessive", "متنحٍّ / مُستتِر / مغلوب"),
 ("Genotype", "التركيب الوراثي / الطراز الجيني / النمط الجيني"),
 ("Phenotype", "المظهر / الطراز المظهري / النمط الظاهري"),
 ("Monohybrid cross", "تهجين أحادي / تهجين أحادي الصفة"),
 ("Dihybrid cross", "تهجين ثنائي / تهجين ثنائي الصفة"),
 ("Law of segregation", "قانون الانعزال / قانون انفصال الصفات"),
 ("Law of independent assortment", "قانون التوزيع المستقل / قانون التوزيع الحر"),
 ("Gamete", "مشيج / خلية جنسية"),
 ("Punnett square", "مربع بانيت / جدول بانيت"),
 ("Filial generation (F1, F2)", "جيل الأبناء (الأول، الثاني)"),
 ("Cotyledons", "الفلقات / الأوراق البذرية"),
 ("Albinism", "المَهَق / عدم التصبّغ الخِلقي / الأمهق (للشخص)"),
 ("Earlobes", "شحمة الأذن"),
 ("Codominance", "السيادة المشتركة / المتساوية"),
 ("Incomplete dominance", "السيادة غير التامّة / الناقصة"),
])

# ------------------------------------------------------------------ questions
O = P
mcq = [
 {"topic_en": "Basic terms", "topic_ar": "المصطلحات الأساسية"},
 Q("Two genes that occupy the same position on homologous chromosomes and cover the same trait are:", "جينان يشغلان الموقع نفسه على الكروموسومين المتماثلين ويخصّان الصفة نفسها هما:",
   O(("Alleles", "أليلات"), ("Gametes", "أمشاج"), ("Chromatids", "كروماتيدات"), ("Centromeres", "سنتروميرات")), "a"),
 Q("Having identical genes for a particular characteristic is called:", "حمل جينين متطابقين لصفة معيّنة يُسمّى:",
   O(("Heterozygous", "هجين"), ("Homozygous", "نقي (متماثل الأليلات)"), ("Recessive", "متنحٍّ"), ("Monohybrid", "أحادي الهجين")), "b"),
 Q("Tt is:", "التركيب Tt:", O(("Homozygous dominant", "نقي سائد"), ("Homozygous recessive", "نقي متنحٍّ"), ("Heterozygous", "هجين"), ("A gamete", "مشيج")), "c"),
 Q("The allele that masks the expression of an alternate allele is:", "الأليل الذي يحجب ظهور الأليل البديل:",
   O(("Recessive", "المتنحّي"), ("Codominant", "المشترك السيادة"), ("Lethal", "المميت"), ("Dominant", "السائد")), "d"),
 Q("A recessive allele appears in the phenotype:", "يظهر الأليل المتنحّي في المظهر:",
   O(("Only in the homozygous condition", "في الحالة النقية فقط"), ("In the heterozygous condition", "في الحالة الهجينة"), ("Always", "دائمًا"), ("Never", "أبدًا")), "a"),
 Q("The genetic makeup of an organism is its:", "المكوّنات الوراثية للكائن هي:",
   O(("Phenotype", "المظهر"), ("Genotype", "التركيب الوراثي"), ("Karyotype", "النمط النووي"), ("Pedigree", "شجرة العائلة")), "b"),
 Q("Phenotype is:", "المظهر هو:", O(("Genotype only", "التركيب الوراثي فقط"), ("Environment only", "البيئة فقط"), ("Genotype + environment", "التركيب الوراثي + البيئة"), ("The gametes", "الأمشاج")), "c"),
 Q("A cross involving a single pair of genes (one trait) is a:", "التهجين الذي يخصّ زوجًا واحدًا من الجينات (صفة واحدة):",
   O(("Dihybrid cross", "تهجين ثنائي"), ("Back cross", "تهجين رجعي"), ("Test cross", "تهجين اختباري"), ("Monohybrid cross", "تهجين أحادي")), "d"),
 Q("F2 is:", "الجيل F2 هو:", O(("Second filial generation", "الجيل الثاني من الأبناء"), ("Parental generation", "جيل الآباء"), ("First filial generation", "الجيل الأول من الأبناء"), ("The gametes of P", "أمشاج الآباء")), "a"),
 {"topic_en": "Mendel's first law", "topic_ar": "قانون مندل الأول"},
 Q("Mendel's first law is the law of:", "قانون مندل الأول هو قانون:", O(("Independent assortment", "التوزيع المستقل"), ("Segregation", "الانعزال"), ("Dominance only", "السيادة فقط"), ("Linkage", "الارتباط")), "b"),
 Q("According to the law of segregation, during gamete formation:", "حسب قانون الانعزال، أثناء تكوين الأمشاج:",
   O(("Both alleles go to the same gamete", "يذهب الأليلان إلى المشيج نفسه"), ("Genes of different traits stay together", "تبقى جينات الصفات المختلفة معًا"), ("Each member of the allelic pair separates from the other", "ينفصل كل فرد من زوج الأليلات عن الآخر"), ("No gametes are formed", "لا تتكوّن أمشاج")), "c"),
 Q("How many traits of pea plants did Mendel look at?", "كم صفة درسها مندل في نبات البازلاء؟", O(("Two", "اثنتان"), ("Four", "أربع"), ("Five", "خمس"), ("Seven", "سبع")), "d"),
 Q("Pure tall plants possess the genes:", "تحمل النباتات الطويلة النقية الجينات:", O(("TT", "TT"), ("Tt", "Tt"), ("tt", "tt"), ("T only", "T فقط")), "a"),
 Q("Pure tall plants (TT) produce gametes:", "تنتج النباتات الطويلة النقية (TT) أمشاجًا:", O(("All t", "كلها t"), ("All T", "كلها T"), ("Half T, half t", "نصفها T ونصفها t"), ("TT", "TT")), "b"),
 Q("Crossing two hybrid smooth pea plants (Rr × Rr) gives a phenotype ratio of:", "تهجين نباتَي بازلاء هجينَي الملمس (Rr × Rr) يعطي نسبة مظاهر:",
   O(("1 : 1", "1 : 1"), ("1 : 2 : 1", "1 : 2 : 1"), ("3 smooth : 1 wrinkled", "3 ملساء : 1 مجعّدة"), ("All smooth", "كلها ملساء")), "c"),
 Q("The genotype ratio of Rr × Rr is:", "نسبة التراكيب الوراثية في Rr × Rr:", O(("3 : 1", "3 : 1"), ("9 : 3 : 3 : 1", "9 : 3 : 3 : 1"), ("1 : 1", "1 : 1"), ("1 RR : 2 Rr : 1 rr", "1 RR : 2 Rr : 1 rr")), "d"),
 Q("The probability of Yy × yy producing green (yy) seeds is:", "احتمال أن ينتج Yy × yy بذورًا خضراء (yy):", O(("1/2", "1/2"), ("1/4", "1/4"), ("3/4", "3/4"), ("0", "0")), "a"),
 {"topic_en": "Mendelian traits in humans", "topic_ar": "الصفات المندلية في الإنسان"},
 Q("A child with the recessive phenotype received the recessive allele from:", "الطفل ذو المظهر المتنحّي استلم الأليل المتنحّي من:",
   O(("The mother only", "الأم فقط"), ("Both parents", "كلا الأبوين"), ("The father only", "الأب فقط"), ("Neither parent", "لا أحد")), "b"),
 Q("Which is listed as a Mendelian trait in humans?", "أيّ مما يلي مذكور صفةً مندلية في الإنسان؟", O(("Eye color", "لون العين"), ("Skin color", "لون الجلد"), ("Albinism", "المَهَق"), ("Hair color", "لون الشعر")), "c"),
 Q("Dry earwax is:", "شمع الأذن الجاف:", O(("Dominant, found mostly in Africans", "سائد، يكثر عند الأفارقة"), ("Codominant", "مشترك السيادة"), ("Not inherited", "غير موروث"), ("Recessive, found mostly in Asians and Native American", "متنحٍّ، يكثر عند الآسيويين والأمريكيين الأصليين")), "d"),
 Q("Which trait involves interaction between multiple genes (more complex inheritance)?", "أيّ صفة تتضمّن تداخل جينات متعدّدة (وراثة أعقد)؟",
   O(("Tongue rolling", "لفّ اللسان"), ("Cystic fibrosis", "التليّف الكيسي"), ("Blood type", "فصيلة الدم"), ("Sickle-cell disease", "فقر الدم المنجلي")), "a"),
 Q("Purely Mendelian traits are:", "الصفات المندلية الصرفة:", O(("Most human traits", "أغلب صفات الإنسان"), ("A tiny minority of all traits", "أقلية صغيرة جدًا من الصفات"), ("Half of all traits", "نصف الصفات"), ("Only in plants", "في النبات فقط")), "b"),
 {"topic_en": "Mendel's second law", "topic_ar": "قانون مندل الثاني"},
 Q("Mendel's second law is the law of:", "قانون مندل الثاني هو قانون:", O(("Segregation", "الانعزال"), ("Dominance", "السيادة"), ("Independent assortment", "التوزيع المستقل"), ("Mutation", "الطفرة")), "c"),
 Q("The second law can be illustrated using:", "يمكن توضيح القانون الثاني باستعمال:", O(("Monohybrid crosses", "التهجينات الأحادية"), ("Karyotypes", "الأنماط النووية"), ("Test tubes", "أنابيب الاختبار"), ("Dihybrid crosses", "التهجينات الثنائية")), "d"),
 Q("A dihybrid AaBb individual produces how many kinds of gametes?", "كم نوعًا من الأمشاج ينتج الفرد AaBb؟", O(("4", "4"), ("2", "2"), ("8", "8"), ("16", "16")), "a"),
 Q("The F2 phenotype ratio of a dihybrid cross (AaBb × AaBb) is:", "نسبة المظاهر في F2 للتهجين الثنائي (AaBb × AaBb):", O(("3 : 1", "3 : 1"), ("9 : 3 : 3 : 1", "9 : 3 : 3 : 1"), ("1 : 2 : 1", "1 : 2 : 1"), ("1 : 1 : 1 : 1", "1 : 1 : 1 : 1")), "b"),
 Q("In RrTT × rrTt (tomatoes), the proportion of tall offspring is:", "في RrTT × rrTt (الطماطم)، نسبة النسل الطويل:", O(("1/4", "1/4"), ("1/2", "1/2"), ("All (100%)", "كله (100%)"), ("3/4", "3/4")), "c"),
 {"topic_en": "Picture questions", "topic_ar": "أسئلة الصور"},
 Q("In this figure, which stem length is in the upper (dominant) row?", "في هذا الشكل، أيّ طول ساق في الصف الأعلى (السائد)؟", O(("Dwarf", "قزم"), ("Medium", "متوسط"), ("Constricted", "متخصّر"), ("Tall", "طويل")), "d", img="assets/pea-seven-traits.png", img_h="34mm"),
 Q("In this Punnett square (RrYy × RrYy), how many boxes are wrinkled green?", "في مربع بانيت هذا (RrYy × RrYy)، كم مربعًا مجعّدًا أخضر؟", O(("1", "1"), ("3", "3"), ("9", "9"), ("4", "4")), "a", img="assets/dihybrid-punnett.png", img_h="44mm"),
]
mcq = balance(mcq, 4)
tf = [
 TF("Alleles occupy the same position on homologous chromosomes.", "تشغل الأليلات الموقع نفسه على الكروموسومين المتماثلين.", "T"),
 TF("A heterozygous individual has two identical genes for a characteristic.", "يحمل الفرد الهجين جينين متطابقين لصفة ما.", "F"),
 TF("A dominant trait appears in the heterozygous condition.", "تظهر الصفة السائدة في الحالة الهجينة.", "T"),
 TF("Phenotype depends on genotype only, not on environment.", "يعتمد المظهر على التركيب الوراثي فقط لا على البيئة.", "F"),
 TF("F1 is the first filial generation.", "الجيل F1 هو الجيل الأول من الأبناء.", "T"),
 TF("Mendel's first law is the law of independent assortment.", "قانون مندل الأول هو قانون التوزيع المستقل.", "F"),
 TF("Dwarf pea plants possess the genes tt.", "تحمل نباتات البازلاء القزمة الجينات tt.", "T"),
 TF("Crossing TT × tt gives all tall offspring in F1.", "تهجين TT × tt يعطي في F1 نسلًا كله طويل.", "T"),
 TF("Yy × yy gives 3/4 green seeds.", "التهجين Yy × yy يعطي 3/4 بذورًا خضراء.", "F"),
 TF("Albinism is a recessive Mendelian trait.", "المَهَق صفة مندلية متنحّية.", "T"),
 TF("Most phenotypic traits are purely Mendelian.", "أغلب الصفات المظهرية مندلية صرفة.", "F"),
 TF("Environmental factors such as temperature, light and nutrients can influence the phenotype.", "قد تؤثّر العوامل البيئية مثل الحرارة والضوء والمغذّيات في المظهر.", "T"),
 TF("Detached earlobes are recessive.", "شحمة الأذن المنفصلة صفة متنحّية.", "F"),
 TF("A dihybrid cross AaBb × AaBb gives a 9:3:3:1 phenotype ratio.", "التهجين الثنائي AaBb × AaBb يعطي نسبة مظاهر 9:3:3:1.", "T"),
]
traps = [
 TR("Genotype vs phenotype", "التركيب الوراثي مقابل المظهر", "Genotype = the genes (TT, Tt, tt). Phenotype = what you see (tall/dwarf) = genotype + environment.", "التركيب الوراثي = الجينات (TT، Tt، tt). والمظهر = ما تراه (طويل/قزم) = التركيب + البيئة."),
 TR("Homozygous vs heterozygous", "النقي مقابل الهجين", "Homozygous = identical (TT or tt); heterozygous = different (Tt). A 'hybrid' plant in a question = heterozygous.", "النقي = متطابقان (TT أو tt)؛ والهجين = مختلفان (Tt). وكلمة 'hybrid' في السؤال = هجين (Tt)."),
 TR("First vs second law", "القانون الأول مقابل الثاني", "First = segregation (one gene, monohybrid, 3:1). Second = independent assortment (two genes, dihybrid, 9:3:3:1).", "الأول = الانعزال (جين واحد، أحادي، 3:1). والثاني = التوزيع المستقل (جينان، ثنائي، 9:3:3:1)."),
 TR("Genotype ratio vs phenotype ratio", "نسبة التراكيب مقابل نسبة المظاهر", "Tt × Tt: genotypes 1:2:1 but phenotypes 3:1. Dihybrid: genotypes 1:2:1:2:4:2:1:2:1 but phenotypes 9:3:3:1.", "Tt × Tt: التراكيب 1:2:1 لكن المظاهر 3:1. والثنائي: التراكيب 1:2:1:2:4:2:1:2:1 لكن المظاهر 9:3:3:1."),
 TR("Yy × yy is not 3:1", "Yy × yy ليس 3:1", "Only one parent is heterozygous → 1 Yy : 1 yy = 1:1 (50% green).", "أب واحد فقط هجين ← 1 Yy : 1 yy = 1:1 (50% خضراء)."),
 TR("Earwax and earlobes", "شمع الأذن وشحمة الأذن", "Wet earwax dominant / dry recessive (Mendelian). Detached earlobes dominant / attached recessive (listed with the more complex traits).", "شمع الأذن الرطب سائد / الجاف متنحٍّ (مندلية). وشحمة الأذن المنفصلة سائدة / الملتصقة متنحّية (مذكورة مع الصفات الأعقد)."),
 TR("All F1 look alike", "كل الجيل F1 متشابه", "If all F1 show one form, that form is dominant and the parents were pure (homozygous) — e.g. BBRR × bbrr.", "إذا ظهر شكل واحد في كل F1 فهو السائد والآباء نقية — مثل BBRR × bbrr."),
]
important = [
 IM("Define: alleles, homozygous, heterozygous, dominant, recessive.", "عرّف: الأليلات، النقي، الهجين، السائد، المتنحّي.",
    "Alleles: two genes at the same position on homologous chromosomes covering the same trait. Homozygous: identical genes for a characteristic. Heterozygous: two different genes. Dominant: masks the alternate allele and appears in the heterozygous condition. Recessive: masked by the dominant allele, appears only in the homozygous condition.",
    "الأليلات: جينان في الموقع نفسه على الكروموسومين المتماثلين يخصّان الصفة نفسها. النقي: جينان متطابقان للصفة. الهجين: جينان مختلفان. السائد: يحجب الأليل البديل ويظهر في الحالة الهجينة. المتنحّي: يحجبه السائد ولا يظهر إلا في الحالة النقية."),
 IM("State Mendel's first and second laws.", "اذكر قانونَي مندل الأول والثاني.",
    "First (segregation): during gamete formation each member of the allelic pair separates from the other. Second (independent assortment): genes for different traits segregate independently during gamete formation; shown by dihybrid crosses.",
    "الأول (الانعزال): أثناء تكوين الأمشاج ينفصل كل فرد من زوج الأليلات عن الآخر. الثاني (التوزيع المستقل): جينات الصفات المختلفة تنعزل باستقلال أثناء تكوين الأمشاج؛ ويُوضَّح بالتهجين الثنائي."),
 IM("Lab sheet Q1 (law 1): explain the cross between pure tall (TT) and dwarf (tt) pea plants.", "سؤال الملزمة 1 (القانون الأول): اشرح التهجين بين نبات بازلاء طويل نقي (TT) وقزم (tt).",
    "TT gives only T gametes and tt only t → F1 all Tt (tall). Tt × Tt → F2 1 TT : 2 Tt : 1 tt = 3 tall : 1 dwarf.",
    "TT يعطي أمشاج T فقط وtt أمشاج t فقط ← F1 كله Tt (طويل). وTt × Tt ← F2 1 TT : 2 Tt : 1 tt = 3 طويل : 1 قزم."),
 IM("Lab sheet Q2 (law 1): cross two pea plants of hybrid smooth seeds (R smooth dominant, r wrinkled).", "سؤال الملزمة 2 (القانون الأول): هجّن نباتَي بازلاء هجينَي البذور الملساء (R أملس سائد، r مجعّد).",
    "Rr × Rr: gametes R and r from each parent → 1 RR : 2 Rr : 1 rr; 3 smooth : 1 wrinkled.",
    "Rr × Rr: أمشاج R وr من كل أب ← 1 RR : 2 Rr : 1 rr؛ 3 ملساء : 1 مجعّدة."),
 IM("Lab sheet Q3 (law 1): probability of Yy × yy producing green seeds?", "سؤال الملزمة 3 (القانون الأول): احتمال أن ينتج Yy × yy بذورًا خضراء؟",
    "Green = yy. Yy × yy → ½ Yy yellow : ½ yy green → probability 1/2 (50%).", "الأخضر = yy. Yy × yy ← ½ Yy أصفر : ½ yy أخضر ← الاحتمال 1/2 (50%)."),
 IM("Lab sheet Q2 (law 2): right-handed black-haired man × left-handed blonde woman; all children black-haired right-handed. Give F1 and F2.", "سؤال الملزمة 2 (القانون الثاني): رجل أيمن أسود الشعر × امرأة عسراء شقراء؛ الأبناء كلهم سود الشعر يمينيون. أعطِ F1 وF2.",
    "P: BBRR × bbrr → F1 all BbRr (black-haired, right-handed). F2 (BbRr × BbRr): 9 black right-handed : 3 black left-handed : 3 blonde right-handed : 1 blonde left-handed; genotypes 1:2:1:2:4:2:1:2:1.",
    "الآباء (P): BBRR × bbrr ← F1 كله BbRr (أسود الشعر، أيمن). وF2 (BbRr × BbRr): 9 أسود أيمن : 3 أسود أعسر : 3 أشقر أيمن : 1 أشقر أعسر؛ والتراكيب 1:2:1:2:4:2:1:2:1."),
 IM("Lab sheet Q3-1: guinea pigs SsBb × SsBb.", "سؤال الملزمة 3-1: خنازير غينيا SsBb × SsBb.",
    "Gametes SB, Sb, sB, sb from each → 16 boxes: 9 smooth black : 3 smooth white : 3 rough black : 1 rough white.",
    "الأمشاج SB وSb وsB وsb من كل أب ← 16 مربعًا: 9 أملس أسود : 3 أملس أبيض : 3 خشن أسود : 1 خشن أبيض."),
 IM("Lab sheet Q3-2: tomatoes RrTT × rrTt.", "سؤال الملزمة 3-2: الطماطم RrTT × rrTt.",
    "Gametes RT, rT × rT, rt → RrTT, RrTt, rrTT, rrTt (¼ each): all tall; 1 red : 1 non-red (r) fruit.",
    "الأمشاج RT وrT × rT وrt ← RrTT وRrTt وrrTT وrrTt (ربع لكل منها): كلها طويلة؛ 1 ثمرة حمراء : 1 غير حمراء (r)."),
 IM("Lab sheet Q3-3: pure black curly dog × pure yellow straight dog; F1 all black straight. Give F2.", "سؤال الملزمة 3-3: كلب أسود مجعّد نقي × كلب أصفر مستقيم نقي؛ F1 كله أسود مستقيم. أعطِ F2.",
    "Black (B) and straight (S) are dominant. BBss × bbSS → F1 BbSs. F2: 9 black straight : 3 black curly : 3 yellow straight : 1 yellow curly.",
    "الأسود (B) والمستقيم (S) سائدان. BBss × bbSS ← F1 BbSs. وF2: 9 أسود مستقيم : 3 أسود مجعّد : 3 أصفر مستقيم : 1 أصفر مجعّد."),
 IM("Lab sheet Q3-4: pea plants heterozygous for pod color (G green) and pod shape (N smooth): genotype and phenotype ratios?", "سؤال الملزمة 3-4: نباتا بازلاء هجينان للون القرنة (G خضراء) وشكلها (N ملساء): ما نسب التراكيب والمظاهر؟",
    "GgNn × GgNn → genotypes 1:2:1:2:4:2:1:2:1; phenotypes 9 green smooth : 3 green constricted : 3 yellow smooth : 1 yellow constricted.",
    "GgNn × GgNn ← التراكيب 1:2:1:2:4:2:1:2:1؛ والمظاهر 9 خضراء ملساء : 3 خضراء متخصّرة : 3 صفراء ملساء : 1 صفراء متخصّرة."),
]
meta = dict(GL, unit_en="Lab 4", unit_ar="العملي 4", unit_no="4", title_en="Mendelian Genetics", title_ar="الوراثة المندلية")
sys.path.insert(0, "/tmp/claude-0/-home-user-kwmdkm/a7dd109e-db53-5fd3-8234-9dab3a530e24/scratchpad"); from bidi import ltr_all   # formulas inside Arabic stay LTR
blocks, mcq, tf, traps, important = ltr_all(blocks), ltr_all(mcq), ltr_all(tf), ltr_all(traps), ltr_all(important)
save("genetics-lab4-mendelian-genetics", meta, blocks, mcq, tf, traps, important)
sys.path.insert(0, "/tmp/claude-0/-home-user-kwmdkm/a7dd109e-db53-5fd3-8234-9dab3a530e24/scratchpad"); from flowfit import fit; fit("genetics-lab4-mendelian-genetics")   # no big gaps (fill2 >= 80%)

```
