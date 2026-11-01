---
source: BIOS-Obsidian/tools/scripts/enz3/e3q.py
handouts: [enzymology-lec3-michaelis-menten-questions]
saved: 2026-11-01
tags: [bios, code]
---
# enz3/e3q.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#enzymology-lec3-michaelis-menten-questions|enzymology-lec3-michaelis-menten-questions]]

```python
A = lambda f: "assets/" + f
mcq = [
 {"topic_en": "The equation", "topic_ar": "المعادلة"},
 Q("In the Michaelis-Menten equation, v₀ =", "في معادلة ميكالس-منتن، v₀ =", O(("Vmax[S] / (Km + [S])", "Vmax[S] / (Km + [S])"), ("Km[S] / (Vmax + [S])", "Km[S] / (Vmax + [S])"), ("Vmax / [S]", "Vmax / [S]"), ("(Km + [S]) / Vmax[S]", "(Km + [S]) / Vmax[S]")), "a"),
 Q("Km is the substrate concentration that gives:", "Km هو تركيز المادة الأساس الذي يعطي:", O(("Vmax", "Vmax"), ("Half of Vmax", "نصف Vmax"), ("Zero velocity", "سرعة صفر"), ("Twice Vmax", "ضعف Vmax")), "b"),
 Q("Km is expressed in units of:", "يُعبّر عن Km بوحدات:", O(("mmol/L.min⁻¹", "ملي مول/لتر.دقيقة"), ("min", "دقيقة"), ("mmol/L (concentration)", "ملي مول/لتر (تركيز)"), ("No units", "بلا وحدات")), "c"),
 Q("To calculate [S] when v₀, Vmax and Km are known:", "لحساب [S] عند معرفة v₀ وVmax وKm:", O(("[S] = Vmax × Km / v₀", "[S] = Vmax × Km / v₀"), ("[S] = v₀ × Vmax / Km", "[S] = v₀ × Vmax / Km"), ("[S] = Km / v₀", "[S] = Km / v₀"), ("[S] = v₀ × Km / (Vmax − v₀)", "[S] = v₀ × Km / (Vmax − v₀)")), "d"),
 Q("When [S] is much higher than Km, v₀ approaches:", "عندما يكون [S] أكبر بكثير من Km تقترب v₀ من:", O(("Vmax", "Vmax"), ("Zero", "الصفر"), ("Km", "Km"), ("Vmax/2", "Vmax/2")), "a"),
 Q("The Michaelis-Menten plot of v₀ against [S] is a:", "منحني ميكالس-منتن لـ v₀ مقابل [S] هو:", O(("Straight line", "خط مستقيم"), ("Hyperbola approaching Vmax", "قطع زائد يقترب من Vmax"), ("Bell-shaped curve", "منحني جرسي"), ("Horizontal line", "خط أفقي")), "b"),
 {"topic_en": "Q1 – Q4 of the lecture", "topic_ar": "أسئلة المحاضرة 1 – 4"},
 Q("Q1: [S] = 0.03 mmol/L, v₀ = 1.5×10⁻³, Vmax = 4.5×10⁻³. Km =", "س1: [S] = 0.03، v₀ = 1.5×10⁻³، Vmax = 4.5×10⁻³. Km =", O(("0.03 mmol/L", "0.03"), ("0.09 mmol/L", "0.09"), ("0.06 mmol/L", "0.06"), ("0.12 mmol/L", "0.12")), "c"),
 Q("In Q1, the step “Km + 0.03 = 0.09” comes from:", "في س1، الخطوة “Km + 0.03 = 0.09” تأتي من:", O(("1.5×10⁻³ / 0.03", "1.5×10⁻³ / 0.03"), ("4.5×10⁻³ − 1.5×10⁻³", "4.5×10⁻³ − 1.5×10⁻³"), ("0.03 × 3", "0.03 × 3 فقط"), ("0.135×10⁻³ / 1.5×10⁻³", "0.135×10⁻³ / 1.5×10⁻³")), "d"),
 Q("Q2: urease, [S] = 0.03, Km = 0.06, v₀ = 1.5×10⁻³. Vmax =", "س2: اليورييز، [S] = 0.03، Km = 0.06، v₀ = 1.5×10⁻³. Vmax =", O(("4.5×10⁻³ mmol/L.min⁻¹", "4.5×10⁻³"), ("3×10⁻³ mmol/L.min⁻¹", "3×10⁻³"), ("1.5×10⁻³ mmol/L.min⁻¹", "1.5×10⁻³"), ("9×10⁻³ mmol/L.min⁻¹", "9×10⁻³")), "a"),
 Q("In Q2, Vmax = v₀ × 3 because:", "في س2، Vmax = v₀ × 3 لأن:", O(("Km = 3[S]", "Km = 3[S]"), ("(Km + [S]) / [S] = 0.09 / 0.03 = 3", "(Km + [S]) / [S] = 0.09 / 0.03 = 3"), ("Vmax is always 3 v₀", "Vmax دائمًا 3 أضعاف v₀"), ("[S] = 3 Km", "[S] = 3 Km")), "b"),
 Q("Q3: Km = 0.06, [S] = 0.03, v₀ = 0.0015. The [S] that gives v₀ = 0.003 is:", "س3: Km = 0.06، [S] = 0.03، v₀ = 0.0015. التركيز الذي يعطي v₀ = 0.003:", O(("0.06 mmol/L", "0.06"), ("0.09 mmol/L", "0.09"), ("0.12 mmol/L", "0.12"), ("0.24 mmol/L", "0.24")), "c"),
 Q("In Q3, the first thing to calculate is:", "في س3، أول ما يُحسب هو:", O(("S2", "S2"), ("Km", "Km"), ("v₀₂", "v₀₂"), ("Vmax", "Vmax")), "d"),
 Q("Q4: same urease data, [S] = 0.12 mmol/L. v₀ =", "س4: نفس معطيات اليورييز، [S] = 0.12. v₀ =", O(("3×10⁻³ mmol/L.min⁻¹", "3×10⁻³"), ("4.5×10⁻³ mmol/L.min⁻¹", "4.5×10⁻³"), ("1.5×10⁻³ mmol/L.min⁻¹", "1.5×10⁻³"), ("6×10⁻³ mmol/L.min⁻¹", "6×10⁻³")), "a"),
 Q("In Q4, v₀ at [S] = 0.12 is what fraction of Vmax?", "في س4، السرعة عند [S] = 0.12 كم جزءًا من Vmax؟", O(("1/3", "الثلث"), ("2/3", "الثلثان"), ("1/2", "النصف"), ("All of it", "كلها")), "b"),
 Q("In the second Q3 (Km not given), Km is first found to be:", "في س3 الثاني (Km غير معطى)، نجد Km أولًا ويساوي:", O(("0.03 mmol/L", "0.03"), ("0.12 mmol/L", "0.12"), ("0.06 mmol/L", "0.06"), ("0.09 mmol/L", "0.09")), "c"),
 {"topic_en": "The table exercise", "topic_ar": "تمرين الجدول"},
 Q("Exercise: Vmax = 5 mmol/min and [S] = 10 mM gives V = 1.2. Km is about:", "التمرين: Vmax = 5 و[S] = 10 يعطي V = 1.2. قيمة Km تقريبًا:", O(("10 mM", "10"), ("41.7 mM", "41.7"), ("2.5 mM", "2.5"), ("31.7 mM", "31.7")), "d"),
 Q("In the exercise, [S] for V = 2.5 mmol/min equals:", "في التمرين، [S] عند V = 2.5 يساوي:", O(("Km (≈ 31.7 mM)", "Km (≈ 31.7)"), ("10 mM", "10"), ("Vmax", "Vmax"), ("Zero", "صفر")), "a"),
 Q("In the exercise, [S]₁ for V = 1.7 mmol/min is about:", "في التمرين، [S]₁ عند V = 1.7 تقريبًا:", O(("10 mM", "10"), ("16.3 mM", "16.3"), ("22.9 mM", "22.9"), ("31.7 mM", "31.7")), "b"),
 Q("The line drawn parallel to the x-axis in the exercise is at:", "الخط الموازي للمحور السيني في التمرين يكون عند:", O(("Km", "Km"), ("Vmax/2", "Vmax/2"), ("Vmax", "Vmax"), ("[S] = 10", "[S] = 10")), "c"),
 {"topic_en": "Picture questions", "topic_ar": "أسئلة الصور"},
 Q("In this equation, Km stands for:", "في هذه المعادلة، Km يعني:", O(("Maximum velocity", "السرعة القصوى"), ("Initial velocity", "السرعة الابتدائية"), ("Substrate concentration", "تركيز المادة الأساس"), ("The Michaelis constant", "ثابت ميكالس")), "d", img=A("mm-equation.png"), img_h="16mm"),
 Q("In this plot, the dashed horizontal line represents:", "في هذا الرسم، الخط الأفقي المتقطّع يمثّل:", O(("Vmax = 5 mmol/min", "Vmax = 5 ملي مول/دقيقة"), ("Km", "Km"), ("Vmax/2", "Vmax/2"), ("[S] = 10 mM", "[S] = 10")), "a", img=A("mm-plot.png"), img_h="44mm"),
]

tf = [
 TF("In Q1 the answer is Km = 0.06 mmol/L.", "في س1 الجواب Km = 0.06 ملي مول/لتر.", "T"),
 TF("When v₀ = Vmax/2, [S] = Km.", "عندما v₀ = Vmax/2 يكون [S] = Km.", "T"),
 TF("Km has the units of velocity (mmol/L.min⁻¹).", "وحدات Km هي وحدات السرعة (ملي مول/لتر.دقيقة).", "F"),
 TF("In Q2, Vmax = 4.5×10⁻³ mmol/L.min⁻¹.", "في س2، Vmax = 4.5×10⁻³ ملي مول/لتر.دقيقة.", "T"),
 TF("In Q3, Vmax must be found before S2.", "في س3 يجب حساب Vmax قبل S2.", "T"),
 TF("In Q4, the answer is v₀ = 4.5×10⁻³ mmol/L.min⁻¹.", "في س4، الجواب v₀ = 4.5×10⁻³ ملي مول/لتر.دقيقة.", "F"),
 TF("Increasing [S] from 0.03 to 0.12 mmol/L doubles v₀ in Q4.", "زيادة [S] من 0.03 إلى 0.12 في س4 تضاعف v₀.", "T"),
 TF("The Michaelis-Menten curve reaches Vmax at a finite [S].", "منحني ميكالس-منتن يصل Vmax عند تركيز محدود.", "F"),
 TF("In the exercise, Km is about 31.7 mM.", "في التمرين، Km حوالي 31.7 ملي مولار.", "T"),
 TF("In the exercise, the [S] values increase as V increases.", "في التمرين، قيم [S] تزداد بزيادة V.", "T"),
 TF("[S] = v₀ × Km / (Vmax − v₀) is a rearranged form of the Michaelis-Menten equation.", "[S] = v₀ × Km / (Vmax − v₀) صيغة مرتّبة من معادلة ميكالس-منتن.", "T"),
 TF("Q1 and Q2 use different enzyme numbers.", "س1 وس2 يستعملان أرقامًا مختلفة للإنزيم.", "F"),
]

traps = [
 TR("Km or Vmax — which is a concentration?", "Km أم Vmax — أيّهما تركيز؟",
    "Km is a concentration (mmol/L); Vmax is a velocity (mmol/L.min⁻¹).", "Km تركيز (ملي مول/لتر)؛ وVmax سرعة (ملي مول/لتر.دقيقة)."),
 TR("In Q1, is “Km + 0.03 = 0.09” the answer?", "في س1، هل “Km + 0.03 = 0.09” هو الجواب؟",
    "No — subtract [S]: Km = 0.09 − 0.03 = 0.06 mmol/L.", "لا — اطرح [S]: Km = 0.09 − 0.03 = 0.06 ملي مول/لتر."),
 TR("Q3 and the second Q3 — same first step?", "س3 وس3 الثاني — هل الخطوة الأولى نفسها؟",
    "No — in Q3 Km is given so you find Vmax first; in the second Q3 Vmax is given so you find Km first. Both give S2 = 0.12 mmol/L.", "لا — في س3 Km معطى فتحسب Vmax أولًا؛ وفي س3 الثاني Vmax معطى فتحسب Km أولًا. وكلاهما يعطي S2 = 0.12."),
 TR("Doubling v₀ from 1.5 to 3 (×10⁻³) — does [S] double?", "مضاعفة v₀ من 1.5 إلى 3 (×10⁻³) — هل يتضاعف [S]؟",
    "No — [S] goes from 0.03 to 0.12 (four times), because the curve is not a straight line.", "لا — [S] يزيد من 0.03 إلى 0.12 (أربعة أضعاف)، لأن المنحني ليس خطًا مستقيمًا."),
 TR("Exercise: is 10 mM the Km because it is the first [S]?", "التمرين: هل 10 ملي مولار هو Km لأنه أول [S]؟",
    "No — Km = 31.67 mM, the [S] at V = Vmax/2 = 2.5 (the last row).", "لا — Km = 31.67 ملي مولار، وهو [S] عند V = Vmax/2 = 2.5 (الصف الأخير)."),
]

important = [
 IM("An enzyme hydrolyzed a substrate concentration of 0.03 mmol/L, the initial velocity was 1.5×10⁻³ and the maximum velocity was 4.5×10⁻³ mmol/L.min⁻¹. Calculate Km.", "حلمأ إنزيم مادة أساس تركيزها 0.03، والسرعة الابتدائية 1.5×10⁻³ والقصوى 4.5×10⁻³. احسب Km.",
    "1.5×10⁻³ = 4.5×10⁻³ × 0.03 / (Km + 0.03) → Km + 0.03 = 0.135×10⁻³ / 1.5×10⁻³ = 0.09 → Km = 0.06 mmol/L.", "`1.5×10⁻³ = 4.5×10⁻³ × 0.03 / (Km + 0.03) → Km + 0.03 = 0.135×10⁻³ / 1.5×10⁻³ = 0.09 → Km = 0.06 mmol/L`."),
 IM("Urease hydrolyzed urea at [S] = 0.03 mmol/L, Km = 0.06 mmol/L, v₀ = 1.5×10⁻³. Calculate Vmax.", "حلمأ اليورييز اليوريا عند [S] = 0.03، Km = 0.06، v₀ = 1.5×10⁻³. احسب Vmax.",
    "1.5×10⁻³ = Vmax × 0.03 / (0.06 + 0.03) → Vmax = 1.5×10⁻³ × 3 = 4.5×10⁻³ mmol/L.min⁻¹.", "`1.5×10⁻³ = Vmax × 0.03 / (0.06 + 0.03) → Vmax = 1.5×10⁻³ × 3 = 4.5×10⁻³ mmol/L.min⁻¹`."),
 IM("Km = 0.06, [S] = 0.03 mmol/L, v₀ = 0.0015. Calculate the [S] which gives v₀ = 0.003 mmol/L.min⁻¹.", "Km = 0.06، [S] = 0.03، v₀ = 0.0015. احسب [S] الذي يعطي v₀ = 0.003.",
    "Vmax = 1.5×10⁻³ × 3 = 4.5×10⁻³; 3×10⁻³ = 4.5×10⁻³ × S2 / (0.06 + S2) → 0.18 = 1.5 S2 → S2 = 0.12 mmol/L.", "أولًا `Vmax = 1.5×10⁻³ × 3 = 4.5×10⁻³`؛ ثم `3×10⁻³ = 4.5×10⁻³ × S2 / (0.06 + S2) → 0.18 = 1.5 S2 → S2 = 0.12 mmol/L`."),
 IM("Same urease data. Calculate v₀ when [S] = 0.12 mmol/L.", "نفس معطيات اليورييز. احسب v₀ عند [S] = 0.12.",
    "Vmax = 4.5×10⁻³; v₀ = 4.5×10⁻³ × 0.12 / (0.06 + 0.12) = 3×10⁻³ mmol/L.min⁻¹.", "أولًا `Vmax = 4.5×10⁻³`؛ ثم `v₀ = 4.5×10⁻³ × 0.12 / (0.06 + 0.12) = 3×10⁻³ mmol/L.min⁻¹`."),
 IM("Vmax = 5 mmol/min; [S] = 10 mM gives V = 1.2. Find Km and the [S] values for V = 1.7, 2.1, 2.2 and 2.5.", "Vmax = 5؛ [S] = 10 يعطي V = 1.2. أوجد Km وقيم [S] عند V = 1.7 و2.1 و2.2 و2.5.",
    "Km = 10 × (5 − 1.2) / 1.2 = 31.67 mM. [S] = V × Km / (Vmax − V): 16.31, 22.93, 24.88 and 31.67 mM (the last equals Km because V = Vmax/2).", "`Km = 10 × (5 − 1.2) / 1.2 = 31.67 mM`؛ ثم `[S] = V × Km / (Vmax − V)`: 16.31 و22.93 و24.88 و31.67 ملي مولار (الأخير يساوي Km لأن `V = Vmax/2`)."),
 IM("Prove that [S] = Km when v₀ = Vmax/2.", "أثبت أن [S] = Km عندما v₀ = Vmax/2.",
    "Vmax/2 = Vmax[S] / (Km + [S]) → Km + [S] = 2[S] → Km = [S].", "`Vmax/2 = Vmax[S] / (Km + [S]) → Km + [S] = 2[S] → Km = [S]`."),
]

import re as _re
_RUN = _re.compile(r"[A-Za-z0-9\[₀-₉⁰-⁹¹²³(][A-Za-z0-9\[\]₀-₉⁰-⁹¹²³⁻×−+/=.()· ]*[A-Za-z0-9\]₀-₉⁰-⁹¹²³)=]")
def _ltr(s):
    """Put formulas inside Arabic text in LTR runs so their order is not reversed."""
    return _RUN.sub(lambda m: "`" + m.group(0) + "`" if _re.search(r"[A-Za-z=]", m.group(0)) else m.group(0), s)
for _q in mcq:
    if "ar" in _q:
        _q["ar"] = _ltr(_q["ar"]); _q["options"] = [[o[0], _ltr(o[1])] for o in _q["options"]]
for _q in tf + traps:
    _q["ar"] = _ltr(_q["ar"])

meta = {"subject_en": "Clinical Enzymology", "subject_ar": "الإنزيمات السريرية", "short_ar": "انزيمات سريرية", "instructor": "د. وليد مجيد",
        "unit_en": "Lecture 3", "unit_ar": "المحاضرة 3", "unit_label": "LEC", "unit_no": "3",
        "title_en": "Michaelis-Menten equation — Questions", "title_ar": "معادلة ميكالس-منتن — أسئلة",
        "department": "قسم التحليلات", "stage": "The fourth stage — الرابعة", "kind": "Theory — نظري"}
save("enzymology-lec3-michaelis-menten-questions", meta, blocks, balance(mcq, 3), tf, traps, important)

```
