---
source: BIOS-Obsidian/tools/scripts/enz3/e3.py
handouts: []
saved: 2026-11-05
tags: [bios, code]
---
# enz3/e3.py

Utility script.

```python
import sys, re; sys.path.insert(0, "/tmp/claude-0/-home-user/a0840832-519a-5a9b-84ea-294867ea1189/scratchpad/imm456")
from ci import *            # c helpers + B INSHORT TERMS balance save(split.fix)

# Clinical Enzymology — theory lecture 3 (stage 4) — Dr. Waleed Majeed — Michaelis-Menten equation: QUESTIONS
# Source: 7-page PDF; solutions of Q1, Q2, Q3, Q4 are in the file; the second Q3 and the table exercise are unsolved
# in the file and are solved here as BIOS solutions (clearly labelled).

BN = lambda en, ar: N(en, ar, label=["BIOS note", "ملاحظة BIOS"])
BS = lambda en, ar: N(en, ar, label=["BIOS solution", "حل BIOS"])
O = P
EQ = dict(t="eq", src="assets/mm-equation.png", h="15mm")
def GIVEN(rows):
    cells = [B(f"**`{e}`** — {m}", f"`{a}` — {n}") for e, a, m, n in rows]
    if len(cells) % 2: cells.append(B("", ""))
    return T([B("Given (from the slide)", "المعطيات (من الشريحة)"), B("Given", "المعطيات")], [cells[i:i + 2] for i in range(0, len(cells), 2)],
             widths=[50, 50], style="summary", label_en="Given", label_ar="المعطيات")
def STEPS(en, ar, title=("Solution", "الحل")):
    return L(en, ar, en=f"**{title[0]}**", ar=f"**{title[1]}**")
def TERMS4(terms, n=5):
    head = [B("Term", "المصطلح"), "الترجمات العربية المستعملة"]
    return [SEC("Key terms", "أهم المصطلحات")] + [T(head, [[f"**{e}**", a] for e, a in terms[i:i + n]], ar_cols=[1], widths=[36, 64])
                                                  for i in range(0, len(terms), n)]

blocks = [
 # ───────────────────────── 0. the equation
 SEC("Michaelis-Menten equation", "معادلة ميكالس-منتن"),
 C("**Michaelis-Menten equation** — Lecture : QUESTIONS (2025 - 2026)", "**معادلة ميكالس-منتن** — المحاضرة: أسئلة (2025 - 2026)"),
 EQ,
 T([B("Symbol", "الرمز"), B("Meaning", "المعنى"), B("Unit in this lecture", "الوحدة في هذه المحاضرة")],
   [[B("**v₀**", "v₀"), B("initial velocity of the reaction", "السرعة الابتدائية للتفاعل"), B("mmol/L.min⁻¹", "ملي مول/لتر.دقيقة")],
    [B("**Vmax**", "Vmax"), B("maximum velocity", "السرعة القصوى"), B("mmol/L.min⁻¹", "ملي مول/لتر.دقيقة")],
    [B("**[S]**", "[S]"), B("substrate concentration", "تركيز المادة الأساس"), B("mmol/L", "ملي مول/لتر")],
    [B("**Km**", "Km"), B("Michaelis constant = [S] that gives v₀ = Vmax/2", "ثابت ميكالس = تركيز المادة الأساس الذي يعطي نصف السرعة القصوى"), B("mmol/L", "ملي مول/لتر")]],
   key_cols=[0], widths=[16, 50, 34], style="summary", label_en="What the letters mean (BIOS)", label_ar="معنى الرموز (BIOS)"),
 T([B("To find", "المطلوب"), B("Rearranged equation", "المعادلة بعد الترتيب")],
   [[B("**Km**", "Km"), B("`Km = (Vmax × [S] / v₀) − [S]`", "`Km = (Vmax × [S] / v₀) − [S]`")],
    [B("**Vmax**", "Vmax"), B("`Vmax = v₀ × (Km + [S]) / [S]`", "`Vmax = v₀ × (Km + [S]) / [S]`")]],
   key_cols=[0], widths=[18, 82], style="summary", label_en="One equation, four forms (BIOS)", label_ar="معادلة واحدة بأربع صيغ (BIOS)"),
 T([B("To find", "المطلوب"), B("Rearranged equation", "المعادلة بعد الترتيب")],
   [[B("**[S]**", "[S]"), B("`[S] = v₀ × Km / (Vmax − v₀)`", "`[S] = v₀ × Km / (Vmax − v₀)`")],
    [B("**v₀**", "v₀"), B("`v₀ = Vmax × [S] / (Km + [S])`", "`v₀ = Vmax × [S] / (Km + [S])`")]],
   key_cols=[0], widths=[18, 82], style="summary", label_en="One equation, four forms (cont.)", label_ar="معادلة واحدة بأربع صيغ (تكملة)"),
 INSHORT([("Write the **given** values first (S1, v₀₁, Vmax, Km…), then put them in **v₀ = Vmax[S] / (Km + [S])**.", "اكتب **المعطيات** أولًا (S1، v₀₁، Vmax، Km…)، ثم عوّضها في `v₀ = Vmax[S] / (Km + [S])`."),
          ("Keep the units the same: [S] and Km in **mmol/L**, velocities in **mmol/L.min⁻¹**.", "وحّد الوحدات: [S] وKm بـ**ملي مول/لتر**، والسرع بـ**ملي مول/لتر.دقيقة**."),
          ("If **v₀ = Vmax/2** then **[S] = Km**.", "إذا كانت `v₀ = Vmax/2` فإن `[S] = Km`.")]),

 # ───────────────────────── Q1
 SEC("Q1 — Km", "س1 — حساب Km"),
 C(["**Q1-** An enzyme hydrolyzed a substrate concentration of 0.03 mmol/L ,the initial velocity was 1.5x10⁻³ mmol/L.min-1 and the maximum velocity was 4.5x10⁻³ mmol/L.min⁻¹ .",
    "Calculate the km value."],
   ["**س1-** حلمأ إنزيم مادة أساس تركيزها **0.03 ملي مول/لتر**، وكانت السرعة الابتدائية **1.5×10⁻³** ملي مول/لتر.دقيقة، والسرعة القصوى **4.5×10⁻³** ملي مول/لتر.دقيقة.",
    "احسب قيمة **Km**."]),
 GIVEN([("S1= 0.03", "S1 = 0.03", "substrate concentration (mmol/L)", "تركيز المادة الأساس (ملي مول/لتر)"),
        ("Vo1= 1.5×10-3", "Vo1 = 1.5×10⁻³", "initial velocity", "السرعة الابتدائية"),
        ("Vmax= 4.5×10-3", "Vmax = 4.5×10⁻³", "maximum velocity", "السرعة القصوى"),
        ("Km =?", "Km = ؟", "required", "المطلوب")]),
 STEPS(["`1.5×10⁻³ = 4.5×10⁻³ × 0.03 / (Km + 0.03)`", "`Km + 0.03 = 4.5×10⁻³ × 0.03 / 1.5×10⁻³`", "`Km + 0.03 = 0.135×10⁻³ / 1.5×10⁻³`",
        "`Km + 0.03 = 0.09`", "`Km = 0.06`"],
       ["نعوّض في المعادلة: `1.5×10⁻³ = 4.5×10⁻³ × 0.03 / (Km + 0.03)`", "نبادل الطرفين (ضرب تبادلي): `Km + 0.03 = 4.5×10⁻³ × 0.03 / 1.5×10⁻³`",
        "نضرب البسط: `Km + 0.03 = 0.135×10⁻³ / 1.5×10⁻³`", "نقسم: `Km + 0.03 = 0.09`", "نطرح 0.03: **`Km = 0.06`** ملي مول/لتر"]),
 INSHORT([("Answer: **Km = 0.06 mmol/L**.", "الجواب: **Km = 0.06 ملي مول/لتر**."),
          ("Quick check: v₀ / Vmax = 1.5 / 4.5 = **1/3** → [S] / (Km + [S]) = 1/3 → Km = **2 × [S]**.", "تحقّق سريع: `v₀ / Vmax = 1.5 / 4.5 = 1/3 → [S] / (Km + [S]) = 1/3 → Km = 2 × [S]`.")]),

 # ───────────────────────── Q2
 SEC("Q2 — Vmax", "س2 — حساب Vmax"),
 C(["**Q2-** Urease enzyme hydrolyzed urea at [S]= 0.03 mmol/L with a Km value of around 0.06 mmol/L.",
    "The initial velocity observed was 1.5x10⁻³mmol/L.min⁻¹ .",
    "Calculate the maximum velocity of the enzymatic reaction"],
   ["**س2-** حلمأ إنزيم **اليورييز** اليوريا عند **[S] = 0.03 ملي مول/لتر** بقيمة Km حوالي **0.06 ملي مول/لتر**.",
    "وكانت السرعة الابتدائية الملاحظة **1.5×10⁻³** ملي مول/لتر.دقيقة.",
    "احسب **السرعة القصوى** للتفاعل الإنزيمي"]),
 GIVEN([("S1= 0.03", "S1 = 0.03", "substrate concentration (mmol/L)", "تركيز المادة الأساس (ملي مول/لتر)"),
        ("Km= 0.06", "Km = 0.06", "Michaelis constant (mmol/L)", "ثابت ميكالس (ملي مول/لتر)"),
        ("Vo1= 1.5×10-3", "Vo1 = 1.5×10⁻³", "initial velocity", "السرعة الابتدائية"),
        ("Vmax=?", "Vmax = ؟", "required", "المطلوب")]),
 STEPS(["`1.5×10⁻³ = Vmax × 0.03 / (0.06 + 0.03)`", "`Vmax = 1.5×10⁻³ × 3`", "`= 4.5×10⁻³`"],
       ["نعوّض في المعادلة: `1.5×10⁻³ = Vmax × 0.03 / (0.06 + 0.03)`", "لأن `0.09 / 0.03 = 3`: `Vmax = 1.5×10⁻³ × 3`", "**`Vmax = 4.5×10⁻³`** ملي مول/لتر.دقيقة"]),
 INSHORT([("Answer: **Vmax = 4.5×10⁻³ mmol/L.min⁻¹** — the same enzyme numbers as Q1, asked the other way round.", "الجواب: **Vmax = 4.5×10⁻³ ملي مول/لتر.دقيقة** — نفس أرقام س1 لكن بالعكس.")]),

 # ───────────────────────── Q3
 SEC("Q3 — [S] for a new velocity", "س3 — تركيز المادة لسرعة جديدة"),
 C(["**Q3-** An enzyme with a Km of 0.06 mmol/L hydrolyzed a substrate of a concentration 0.03 mmol/L.",
    "The initial velocity of the reaction was 0.0015 mmol/L.min⁻¹ .",
    "Calculate the substrate concentration which gives an initial velocity of 0.003 mmol/L.min⁻¹."],
   ["**س3-** حلمأ إنزيم قيمة Km له **0.06 ملي مول/لتر** مادة أساس تركيزها **0.03 ملي مول/لتر**.",
    "وكانت السرعة الابتدائية للتفاعل **0.0015** ملي مول/لتر.دقيقة.",
    "احسب **تركيز المادة الأساس** الذي يعطي سرعة ابتدائية مقدارها **0.003** ملي مول/لتر.دقيقة."]),
 GIVEN([("S1= 0.03", "S1 = 0.03", "first substrate concentration", "التركيز الأول للمادة الأساس"),
        ("Km= 0.06", "Km = 0.06", "Michaelis constant", "ثابت ميكالس"),
        ("Vo1= 1.5×10-3", "Vo1 = 1.5×10⁻³", "first initial velocity", "السرعة الابتدائية الأولى"),
        ("Vo2= 3 ×10-3", "Vo2 = 3×10⁻³", "second (new) velocity", "السرعة الثانية (الجديدة)"),
        ("S2 =?", "S2 = ؟", "required", "المطلوب")]),
 STEPS(["`1.5×10⁻³ = Vmax × 0.03 / (0.06 + 0.03)`", "`Vmax = 1.5×10⁻³ × 3 = 4.5×10⁻³`", "`3×10⁻³ = 4.5×10⁻³ × S2 / (0.06 + S2)`", "`S2 = 0.12 mmol/L`"],
       ["أولًا نحسب Vmax: `1.5×10⁻³ = Vmax × 0.03 / (0.06 + 0.03)`", "`Vmax = 1.5×10⁻³ × 3 = 4.5×10⁻³`", "ثم نعوّض السرعة الجديدة: `3×10⁻³ = 4.5×10⁻³ × S2 / (0.06 + S2)`",
        "**`S2 = 0.12`** ملي مول/لتر"]),
 BN("Between the last two lines: 3 (0.06 + S2) = 4.5 S2 → 0.18 = 1.5 S2 → S2 = 0.12.", "بين السطرين الأخيرين: `3 (0.06 + S2) = 4.5 S2 → 0.18 = 1.5 S2 → S2 = 0.12`."),
 INSHORT([("Two steps: **find Vmax first**, then use the new v₀ to find **S2 = 0.12 mmol/L**.", "خطوتان: **احسب Vmax أولًا**، ثم استعمل السرعة الجديدة لتجد **S2 = 0.12 ملي مول/لتر**.")]),

 # ───────────────────────── Q4
 SEC("Q4 — v₀ at a new [S]", "س4 — السرعة عند تركيز جديد"),
 C(["**Q4-** Urease enzyme hydrolyzed urea at [S]= 0.03 mmol/L with a Km value of around 0.06 mmol/L.",
    "The initial velocity observed was 1.5x10⁻³ mmol/L.min⁻¹ .",
    "Calculate the initial velocity of the enzymatic reaction when using [S]= 0.12 mmol/L."],
   ["**س4-** حلمأ إنزيم **اليورييز** اليوريا عند **[S] = 0.03 ملي مول/لتر** بقيمة Km حوالي **0.06 ملي مول/لتر**.",
    "وكانت السرعة الابتدائية الملاحظة **1.5×10⁻³** ملي مول/لتر.دقيقة.",
    "احسب **السرعة الابتدائية** للتفاعل الإنزيمي عند استعمال **[S] = 0.12 ملي مول/لتر**."]),
 GIVEN([("S1= 0.03", "S1 = 0.03", "first substrate concentration", "التركيز الأول للمادة الأساس"),
        ("Km= 0.06", "Km = 0.06", "Michaelis constant", "ثابت ميكالس"),
        ("Vo1= 1.5×10-3", "Vo1 = 1.5×10⁻³", "first initial velocity", "السرعة الابتدائية الأولى"),
        ("S2=0.12", "S2 = 0.12", "new substrate concentration", "التركيز الجديد"),
        ("Vo2=?", "Vo2 = ؟", "required", "المطلوب")]),
 STEPS(["`1.5×10⁻³ = Vmax × 0.03 / (0.06 + 0.03)`", "`Vmax = 1.5×10⁻³ × 3 = 4.5×10⁻³`", "`Vo2 = 4.5×10⁻³ × 0.12 / (0.06 + 0.12)`", "`Vo2 = 3×10⁻³`"],
       ["أولًا نحسب Vmax: `1.5×10⁻³ = Vmax × 0.03 / (0.06 + 0.03)`", "`Vmax = 1.5×10⁻³ × 3 = 4.5×10⁻³`", "نعوّض التركيز الجديد: `Vo2 = 4.5×10⁻³ × 0.12 / (0.06 + 0.12)`",
        "**`Vo2 = 3×10⁻³`** ملي مول/لتر.دقيقة"]),
 INSHORT([("Q4 is **Q3 reversed**: [S] = 0.12 mmol/L gives **v₀ = 3×10⁻³** (2/3 of Vmax).", "س4 هو **س3 بالعكس**: [S] = 0.12 ملي مول/لتر يعطي **v₀ = 3×10⁻³** (ثلثا Vmax).")]),

 # ───────────────────────── Q3 (second version, unsolved in the file)
 SEC("Q3 (second slide) — [S]", "س3 (الشريحة الثانية) — التركيز"),
 C(["**Q3** An enzyme hydrolyzed a substrate concentration of 0.03 mmol/L ,the initial velocity was 1.5x10⁻³ mmol/L.min⁻¹ and the maximum velocity was 4.5x10-3 mmol/L.min⁻¹ .",
    "Calculate the substrate concentration that gives a velocity of 3x10⁻³ mmol/L.min-1 ."],
   ["**س3** حلمأ إنزيم مادة أساس تركيزها **0.03 ملي مول/لتر**، وكانت السرعة الابتدائية **1.5×10⁻³** والسرعة القصوى **4.5×10⁻³** ملي مول/لتر.دقيقة.",
    "احسب تركيز المادة الأساس الذي يعطي سرعة **3×10⁻³** ملي مول/لتر.دقيقة."]),
 GIVEN([("S1= 0.03", "S1 = 0.03", "first substrate concentration", "التركيز الأول للمادة الأساس"),
        ("Vo1= 1.5×10-3", "Vo1 = 1.5×10⁻³", "first initial velocity", "السرعة الابتدائية الأولى"),
        ("Vmax= 4.5×10-3", "Vmax = 4.5×10⁻³", "maximum velocity", "السرعة القصوى"),
        ("Vo2= 3 ×10-3", "Vo2 = 3×10⁻³", "new velocity", "السرعة الجديدة"),
        ("S2 =?", "S2 = ؟", "required", "المطلوب")]),
 BS(["The slide leaves this one unsolved; here Km is unknown, so find **Km first** (as in Q1): 1.5×10⁻³ = 4.5×10⁻³ × 0.03 / (Km + 0.03) → **Km = 0.06**.",
     "Then: 3×10⁻³ = 4.5×10⁻³ × S2 / (0.06 + S2) → 3 (0.06 + S2) = 4.5 S2 → 0.18 = 1.5 S2 → **S2 = 0.12 mmol/L**."],
    ["الشريحة تركت هذا السؤال بلا حل؛ وهنا Km مجهول فنحسب **Km أولًا** (مثل س1): `1.5×10⁻³ = 4.5×10⁻³ × 0.03 / (Km + 0.03) → Km = 0.06`.",
     "ثم: `3×10⁻³ = 4.5×10⁻³ × S2 / (0.06 + S2) → 0.18 = 1.5 S2 → S2 = 0.12 mmol/L`."]),
 INSHORT([("Same answer as the first Q3: **S2 = 0.12 mmol/L** — but here you find **Km** first, not Vmax.", "نفس جواب س3 الأول: **S2 = 0.12 ملي مول/لتر** — لكن هنا تحسب **Km** أولًا لا Vmax.")]),

 # ───────────────────────── table exercise (unsolved in the file)
 SEC("Exercise — missing [S] values", "تمرين — قيم [S] المفقودة"),
 C(["**1.** Use the Michaelis-Menton Equation to calculate the missing values of [S] given below if Vmax = 5 mmol/min.", "Plot [S] versus V .",
    "Draw line parallel to the x-axis at Vmax and extend your plotted line to show its approach to Vmax."],
   ["**1.** استعمل معادلة ميكالس-منتن لحساب قيم [S] المفقودة أدناه إذا كانت **Vmax = 5 ملي مول/دقيقة**.", "ارسم [S] مقابل V .",
    "ارسم خطًا موازيًا للمحور السيني عند Vmax ومدّ الخط المرسوم ليُظهر اقترابه من Vmax."]),
 T([B("[S] (mM)", "[S] (ملي مولار)"), B("V (mmol/min)", "V (ملي مول/دقيقة)"), B("BIOS answer", "جواب BIOS")],
   [[B("10", "10"), B("1.2", "1.2"), B("given → Km = 31.67 mM", "معطى ← Km = 31.67")],
    [B("[S]₁", "[S]₁"), B("1.7", "1.7"), B("**16.31 mM**", "**16.31**")],
    [B("[S]₂", "[S]₂"), B("2.1", "2.1"), B("**22.93 mM**", "**22.93**")],
    [B("[S]₃", "[S]₃"), B("2.2", "2.2"), B("**24.88 mM**", "**24.88**")],
    [B("[S]₄", "[S]₄"), B("2.5", "2.5"), B("**31.67 mM** (= Km, because V = Vmax/2)", "**31.67** (= Km لأن V = Vmax/2)")]],
   key_cols=[0], widths=[22, 26, 52]),
 BS("The file gives no answer; first find Km from the known row: 1.2 = 5 × 10 / (Km + 10) → Km + 10 = 41.67 → **Km = 31.67 mM**.",
    "الملف لا يعطي جوابًا؛ نحسب Km أولًا من الصف المعلوم: `1.2 = 5 × 10 / (Km + 10) → Km + 10 = 41.67 → Km = 31.67 mM`."),
 BS("Then for every V: **[S] = V × Km / (Vmax − V)**, e.g. [S]₁ = 1.7 × 31.67 / 3.3 = **16.31 mM**.",
    "ثم لكل V: `[S] = V × Km / (Vmax − V)`، مثلًا `[S]₁ = 1.7 × 31.67 / 3.3 = 16.31 mM`."),
 BN("“Michaelis-Menton” in the slide = **Michaelis-Menten**.", "“Michaelis-Menton” في الشريحة أي **Michaelis-Menten**."),
 F("mm-plot.png", "BIOS plot of the exercise: V against [S] with the dashed line at Vmax = 5 mmol/min; the curve approaches Vmax but never reaches it; at V = Vmax/2 = 2.5, [S] = Km ≈ 31.7 mM",
   "رسم BIOS للتمرين: V مقابل [S] مع الخط المتقطّع عند Vmax = 5 ملي مول/دقيقة؛ المنحني يقترب من Vmax ولا يصلها؛ وعند V = Vmax/2 = 2.5 يكون [S] = Km ≈ 31.7 ملي مولار", h="70mm", fit="contain"),
 INSHORT([("Use the **known row** to get Km, then **[S] = V·Km / (Vmax − V)** for the rest.", "استعمل **الصف المعلوم** لإيجاد Km، ثم `[S] = V·Km / (Vmax − V)` للبقية."),
          ("The curve is a **hyperbola**: it rises fast, then flattens and **approaches Vmax** without reaching it.", "المنحني **قطع زائد**: يرتفع بسرعة ثم يتسطّح و**يقترب من Vmax** دون أن يصلها."),
          ("**V = Vmax/2 ↔ [S] = Km** — the last row of the table proves it.", "`V = Vmax/2 ↔ [S] = Km` — والصف الأخير من الجدول يثبت ذلك.")]),

 *TERMS4([("Michaelis-Menten equation", "معادلة ميكالس-منتن / معادلة ميكايلس-مينتن"),
          ("Initial velocity (v₀)", "السرعة الابتدائية / سرعة التفاعل الأولية"),
          ("Maximum velocity (Vmax)", "السرعة القصوى / أقصى سرعة للتفاعل"),
          ("Michaelis constant (Km)", "ثابت ميكالس / ثابت ميكايلس"),
          ("Substrate concentration [S]", "تركيز المادة الأساس / تركيز الركيزة"),
          ("Hydrolyze", "يحلمئ / يحلّل مائيًا"),
          ("Urease", "اليورييز / إنزيم تحليل اليوريا"),
          ("mmol/L.min⁻¹", "ملي مول لكل لتر في الدقيقة"),
          ("Hyperbola", "القطع الزائد / منحني زائدي"),
          ("Enzymatic reaction", "التفاعل الإنزيمي")]),
]

exec(open(__file__.replace("e3.py", "e3q.py")).read())

```
