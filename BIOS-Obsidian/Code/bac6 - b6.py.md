---
source: BIOS-Obsidian/tools/scripts/bac6/b6.py
handouts: []
saved: 2026-11-11
tags: [bios, code]
---
# bac6/b6.py

Utility script.

```python
import sys, re; sys.path.insert(0, "/tmp/claude-0/-home-user-kwmdkm/44452a28-19bf-5ce8-890a-f6919e775f0b/scratchpad/imm456")
from ci import *            # c helpers + B INSHORT TERMS balance save(split.fix)
import split
split.ABBR = split.ABBR + ("spp.)", "agar).")

# Diagnostic Microbiology — theory lecture 6 (stage 4) — instructor written as د. عدنان on the user's request
# (the sheet says أ.م.د أحمد سالم محمد) — Cultivation and Isolation of Viable Pathogen (culture media).

BN = lambda en, ar: N(en, ar, label=["BIOS note", "ملاحظة BIOS"])
O = P
def TERMS5(terms, n=4):
    head = [B("Term", "المصطلح"), "الترجمات العربية المستعملة"]
    return [SEC("Key terms", "أهم المصطلحات")] + [T(head, [[f"**{e}**", a] for e, a in terms[i:i + n]], ar_cols=[1], widths=[36, 64])
                                                  for i in range(0, len(terms), n)]

blocks = [
 # ───────────────────────── 1. Laboratory media + constituents
 SEC("Laboratory media", "الأوساط المختبرية"),
 C("Culture media are required to isolate the bacteria from the clinical specimens; following which the appropriate biochemical tests can be performed to identify the causative agent.",
   "**الأوساط الزرعية** مطلوبة **لعزل البكتيريا من العيّنات السريرية**؛ وبعدها يمكن إجراء **الفحوص الكيموحيوية** المناسبة لتشخيص **العامل المسبّب**."),
 H2("Constituents of culture media:", "مكوّنات الأوساط الزرعية:"),
 C("The basic constituents of culture media are:", "المكوّنات الأساسية للأوساط الزرعية هي:"),
 L(["**Water:** Distilled water or potable water with low mineral content is suitable for culture media preparation.",
    "**Electrolyte:** Sodium chloride or other electrolytes."],
   ["**الماء:** الماء المقطّر أو ماء الشرب **قليل المعادن** مناسب لتحضير الأوساط الزرعية.",
    "**الإلكتروليت:** كلوريد الصوديوم أو إلكتروليتات أخرى."]),
 L(["**Peptone:** It is a complex mixture of partially digested proteins."],
   ["**الببتون:** خليط معقّد من **بروتينات مهضومة جزئيًا**."], start=3),
 L(['**Source:** It is obtained from lean meat or other protein material, such as heart muscle, casein or fibrin, or soya flour usually by digestion with proteolytic enzymes, such as pepsin'], ['**المصدر:** يُحصل عليه من **اللحم الأحمر الخالي من الدهن** أو مواد بروتينية أخرى مثل عضلة القلب أو الكازين أو الفايبرين أو طحين الصويا، عادةً **بالهضم بإنزيمات محلّلة للبروتين** مثل **البيبسين**'], en="**Peptone —**", ar="**الببتون —**"),
 L(['**Constituents:** 1t contains proteoses, aminoacids, inorganic salts (phosphates, potassium and magnesium), accessory growth factors like nicotinic acid and riboflavin.'], ['**المكوّنات:** يحتوي البروتيوزات والأحماض الأمينية والأملاح غير العضوية (الفوسفات والبوتاسيوم والمغنيسيوم) و**عوامل النمو المساعدة** مثل حامض النيكوتينيك والرايبوفلافين.'], start=2),
 C(["**Agar:** It is used for solidifying the culture media.", "It is commercially available in powder form; melts in water after boiling and jellifies after cooling also called 'agar-agar' is prepared from the cell wall of variety of seaweeds (red algae of species __Gelidium__ and __Gracilaria__)"],
   ["**الأكار:** يُستعمل **لتصليب الأوساط الزرعية**.", "يتوفّر تجاريًا بشكل مسحوق؛ **يذوب في الماء بعد الغليان ويتهلّم بعد التبريد**، ويسمّى أيضًا 'أكار-أكار'، ويُحضَّر من **جدار خلايا أنواع من الأعشاب البحرية** (الطحالب الحمراء من نوعي `Gelidium` و`Gracilaria`)"]),
 C(["**Preparation of agar media:** The appropriate amount of agar powder is added to water and the mixture is dissolved and then sterilized by placing it in an autoclave.",
    "When the temperature of the molten agar comes down to 45°C, it is poured to the Petri dishes and then allowed to set for 20 minutes."],
   ["**تحضير أوساط الأكار:** تُضاف الكمية المناسبة من مسحوق الأكار إلى الماء ويُذاب الخليط، ثم يُعقَّم **بوضعه في المؤصدة (autoclave)**.",
    "وعندما تنخفض درجة حرارة الأكار المنصهر إلى **45°م** يُصبّ في **أطباق بتري** ثم يُترك **ليتصلّب 20 دقيقة**."]),
 FLOW([("agar powder + water", "مسحوق أكار + ماء"), ("dissolve", "إذابة"), ("autoclave", "المؤصدة"), ("cool to 45°C", "تبريد إلى 45°م"), ("pour into Petri dishes", "صبّ في أطباق بتري"), ("set 20 min", "تصلّب 20 دقيقة")]),
 C("**Meat extract:** It is a commercial preparation of highly concentrated meat stock, usually made from beef. It contains protein degradation products, inorganic salts, carbohydrates and growth factors.",
   "**مستخلص اللحم:** مستحضر تجاري من **مرق لحم عالي التركيز**، عادةً من **لحم البقر**. ويحتوي نواتج تحلّل البروتين والأملاح غير العضوية والكاربوهيدرات وعوامل النمو."),
 C(["**Yeast extract:** Itis prepared commercially from washed cells of Baker's yeast.", "It contains amino acids, inorgani c salts (potassium and phosphates) and carbohydrates. (Figure-1)"],
   ["**مستخلص الخميرة:** يُحضَّر تجاريًا من **خلايا خميرة الخبّاز المغسولة**.", "ويحتوي الأحماض الأمينية والأملاح غير العضوية (البوتاسيوم والفوسفات) والكاربوهيدرات. (الشكل 1)"]),
 F("media-fig1.png", "Figure (1): A. Peptone water; B. Nutrient agar; C. Blood agar; D. Chocolate agar.",
   "الشكل (1): A. ماء الببتون؛ B. الأكار المغذّي؛ C. أكار الدم؛ D. أكار الشوكولاتة.", h="46mm", fit="contain"),
 C("**Malt extract:** It consists of maltose (about 50%), starch, dextrin, glucose and 5% protein products.",
   "**مستخلص الشعير (المولت):** يتكوّن من **المالتوز (حوالي 50%)** والنشا والدكسترين والغلوكوز و**5% منتجات بروتينية**."),
 C(["**Blood and serum:** They are important components of enriched media and provide extra nutrition to fastidious bacteria.", "Usually 5- % of sheep blood is used.", "Horse, ox or human blood can also be used."],
   ["**الدم والمصل:** مكوّنان مهمّان في **الأوساط المُغناة** ويوفّران **تغذية إضافية للبكتيريا صعبة النمو**.", "عادةً يُستعمل **5- % من دم الأغنام**.", "ويمكن استعمال دم الحصان أو الثور أو الإنسان أيضًا."]),
 BN("“5- %” — the second number is missing in the sheet (usually **5–10%** sheep blood); “1t” = It, “Itis” = It is, “inorgani c” = inorganic.",
    "“5- %” — الرقم الثاني ناقص في الورقة (عادةً **5–10%** من دم الأغنام)؛ و“1t” أي It، و“Itis” أي It is، و“inorgani c” أي inorganic."),
 T([B("Constituent", "المكوّن"), B("Role / what it is", "الدور / ما هو")],
   [[B("**Water**", "**الماء**"), B("distilled / low-mineral water", "مقطّر / قليل المعادن")],
    [B("**Electrolyte**", "**الإلكتروليت**"), B("NaCl", "كلوريد الصوديوم")],
    [B("**Peptone**", "**الببتون**"), B("partially digested proteins (pepsin)", "بروتينات مهضومة جزئيًا (بيبسين)")]],
   key_cols=[0], widths=[34, 66], style="summary", label_en="Constituents at a glance", label_ar="المكوّنات بنظرة"),
 T([B("Constituent", "المكوّن"), B("Role / what it is", "الدور / ما هو")],
   [[B("**Agar**", "**الأكار**"), B("solidifying agent from red algae", "عامل تصليب من الطحالب الحمراء")],
    [B("**Meat / yeast / malt extract**", "**مستخلص اللحم / الخميرة / الشعير**"), B("nutrients and growth factors", "مغذّيات وعوامل نمو")],
    [B("**Blood and serum**", "**الدم والمصل**"), B("enrichment for fastidious bacteria", "إغناء للبكتيريا صعبة النمو")]],
   key_cols=[0], widths=[34, 66], style="summary", label_en="Constituents (cont.)", label_ar="المكوّنات (تكملة)"),
 INSHORT([("Media isolate bacteria from specimens → then **biochemical tests** identify them.", "الأوساط تعزل البكتيريا من العيّنات ← ثم **الفحوص الكيموحيوية** تشخّصها."),
          ("Peptone = **partially digested proteins** (pepsin); agar from **red algae**, melts on boiling, gels on cooling.", "الببتون = **بروتينات مهضومة جزئيًا** (بيبسين)؛ الأكار من **الطحالب الحمراء**، يذوب بالغليان ويتهلّم بالتبريد."),
          ("Agar plates: autoclave → cool to **45°C** → pour → set **20 min**.", "أطباق الأكار: المؤصدة ← تبريد إلى **45°م** ← صبّ ← تصلّب **20 دقيقة**."),
          ("Malt extract ≈ **50% maltose**; blood (usually **sheep**) for **fastidious** bacteria.", "مستخلص الشعير ≈ **50% مالتوز**؛ الدم (عادةً **أغنام**) للبكتيريا **صعبة النمو**.")]),

 # ───────────────────────── 2. Types of culture media
 SEC("Types of culture media", "أنواع الأوساط الزرعية"),
 L(["Liquid media (or broth)", "Semisolid media", "Solid media"], ["أوساط سائلة (أو مرق)", "أوساط شبه صلبة", "أوساط صلبة"],
   en="Bacteriological culture media can be classified in two ways: **A. Based on consistency,** culture media are grouped into:",
   ar="يمكن تصنيف الأوساط الزرعية البكتيرية بطريقتين: **أ. حسب القوام** تُجمع الأوساط في:"),
 L(["**Routine laboratory media:** They are prepared from nutrients, such as aqueous extract of meat, peptone, etc. They can further be classified into various types based on functional use or application, as Simple/basal media; Enriched media; Enrichment broth; Selective media; Differential media; Transport media; Anaerobic media.",
    "**Defined or synthetic media:** They are prepared from pure chemical substances and the exact composition of the media is known, Simple synthetic media and Complex synthetic media."],
   ["**الأوساط المختبرية الروتينية:** تُحضَّر من مغذّيات مثل **المستخلص المائي للحم** والببتون وغيرها. ويمكن تصنيفها أيضًا حسب الاستعمال إلى: الأوساط البسيطة/الأساسية؛ والمُغناة؛ ومرق الإغناء؛ والانتقائية؛ والتفريقية؛ وأوساط النقل؛ والأوساط اللاهوائية.",
    "**الأوساط المحدّدة أو الصناعية:** تُحضَّر من **مواد كيميائية نقية** ويكون **تركيبها الدقيق معروفًا**، وهي أوساط صناعية بسيطة وأوساط صناعية معقّدة."],
   en="**B. Based on the growth requirements,** culture media are classified as:", ar="**ب. حسب متطلّبات النمو** تُصنَّف الأوساط إلى:"),
 H2("Simple media", "الأوساط البسيطة"),
 C("Many bacteria will grow in or on simple media such as nutrient broth/nutrient agar that contains ‘peptone’ (polypeptides and amino acids from the enzymatic digestion of meat) and ‘meat extract’(water-soluble components of meat containing mineral salts and vitamins).",
   "تنمو بكتيريا كثيرة في أو على **الأوساط البسيطة** مثل **المرق المغذّي/الأكار المغذّي** الذي يحتوي ‘الببتون’ (متعدّدات ببتيد وأحماض أمينية من **الهضم الإنزيمي للحم**) و‘مستخلص اللحم’ (المكوّنات الذائبة في الماء من اللحم وفيها أملاح معدنية وفيتامينات)."),
 H2("Enriched media", "الأوساط المُغناة"),
 C("These contain additional nutrients for the isolation of more fastidious bacteria that require special conditions for growth like agar containing whole blood (blood agar) or agar containing lysed blood (chocolate agar). (Figure-2)",
   "تحتوي **مغذّيات إضافية** لعزل **البكتيريا الأكثر صعوبة في النمو** التي تتطلّب ظروفًا خاصة، مثل الأكار الذي يحتوي **دمًا كاملًا (أكار الدم)** أو الأكار الذي يحتوي **دمًا متحلّلًا (أكار الشوكولاتة)** (الشكل 2)."),
 F("media-fig2.png", "Figure (2): A. Brain-heart infusion broth; B. Biphasic medium (Brain-heart infusion broth/agar); C. Robertson's cooked meat medium; D. Thioglycollate broth — labels in the picture: Monophasic medium (A), Biphasic medium (B)",
   "الشكل (2): A. مرق منقوع الدماغ والقلب؛ B. وسط ثنائي الطور (مرق/أكار منقوع الدماغ والقلب)؛ C. وسط روبرتسون للحم المطبوخ؛ D. مرق الثايوغلايكوليت — كتابات الصورة: وسط أحادي الطور (A)، وسط ثنائي الطور (B)", h="96mm", fit="contain"),
 INSHORT([("By **consistency**: liquid (broth), semisolid, solid.", "حسب **القوام**: سائل (مرق)، شبه صلب، صلب."),
          ("By **growth requirements**: routine media (simple, enriched, enrichment broth, selective, differential, transport, anaerobic) and **defined/synthetic** media (pure chemicals, exact composition).", "حسب **متطلّبات النمو**: أوساط روتينية (بسيطة، مُغناة، مرق إغناء، انتقائية، تفريقية، نقل، لاهوائية) وأوساط **محدّدة/صناعية** (مواد نقية وتركيب دقيق)."),
          ("Simple = **nutrient broth/agar**; enriched = **blood agar** (whole blood) and **chocolate agar** (lysed blood).", "البسيط = **المرق/الأكار المغذّي**؛ المُغنى = **أكار الدم** (دم كامل) و**أكار الشوكولاتة** (دم متحلّل).")]),

 # ───────────────────────── 3. Selective and indicator media
 SEC("Selective media", "الأوساط الانتقائية"),
 L(["**Mannitol salt agar** which contains increased NaCl (salt) concentration for the recovery of staphylococci;",
    "**MacConkey agar,** which contains bile salts and allows the growth of bile-tolerant bacteria only; and",
    "**Antibiotics,** which are frequently added to media to allow only certain bacteria to grow while suppressing or killing others."],
   ["**أكار الملح والمانيتول** الذي يحتوي **تركيزًا عاليًا من NaCl (الملح)** لاستعادة **المكوّرات العنقودية**؛",
    "**أكار ماكونكي** الذي يحتوي **أملاح الصفراء** ويسمح بنمو **البكتيريا المتحمّلة للصفراء** فقط؛ و",
    "**المضادات الحيوية** التي تُضاف كثيرًا للأوساط للسماح لبكتيريا معيّنة فقط بالنمو مع تثبيط الأخرى أو قتلها."],
   en="These are designed to facilitate growth of some bacteria, while suppressing the growth of others, and include:",
   ar="صُمّمت **لتسهيل نمو بعض البكتيريا مع تثبيط نمو غيرها**، وتشمل:"),
 H2("Indicator media", "الأوساط الدالّة"),
 C(["These are designed to aid the detection and recognition of particular pathogens.",
    "They are often based on sugar fermentation reactions that result in production of acid and the subsequent colour change of a pH indicator, such as MacConkey agar contains lactose and a pH indicator (neutral red); lactose-fermenting bacteria (__Escherichia coli__) produce acid and form pink colonies, whereas non-lactose fermenting bacteria (__Salmonella spp.__) do not produce acid and form pale yellow colonies."],
   ["صُمّمت للمساعدة في **كشف وتمييز ممرضات معيّنة**.",
    "وغالبًا تعتمد على **تفاعلات تخمّر السكر** التي تنتج **حامضًا** يتبعه **تغيّر لون دليل pH**؛ مثل أكار ماكونكي الذي يحتوي **اللاكتوز** ودليل pH (**الأحمر المتعادل**)؛ فالبكتيريا **المخمّرة للاكتوز** (`Escherichia coli`) تنتج حامضًا وتكوّن **مستعمرات وردية**، بينما البكتيريا **غير المخمّرة للاكتوز** (`Salmonella spp.`) لا تنتج حامضًا وتكوّن **مستعمرات صفراء شاحبة**."]),
 C(["This property facilitates the recognition of possible Salmonella colonies among normal bowel flora.",
    "Note that indicator media may also contain selective agents including antibiotics or substances such as bile salts and crystal violet to suppress growth of most Gram- positive microorganisms.",
    "MacConkey agar is therefore both a selective medium and an indicator medium."],
   ["وتسهّل هذه الخاصية **تمييز مستعمرات السالمونيلا المحتملة** بين **فلورا الأمعاء الطبيعية**.",
    "ولاحظ أن الأوساط الدالّة قد تحتوي أيضًا **عوامل انتقائية** منها المضادات الحيوية أو مواد مثل **أملاح الصفراء والبنفسجي البلّوري** **لتثبيط نمو معظم الأحياء الموجبة لغرام**.",
    "لذا فإن **أكار ماكونكي وسط انتقائي ودالّ معًا**."]),
 T([B("Feature", "الصفة"), B("Lactose fermenter", "مخمّر اللاكتوز"), B("Non-lactose fermenter", "غير مخمّر اللاكتوز")],
   [[B("**Example**", "**مثال**"), B("Escherichia coli", "الإشريكية القولونية"), B("Salmonella spp.", "أنواع السالمونيلا")],
    [B("**Acid**", "**الحامض**"), B("produced", "يُنتج"), B("not produced", "لا يُنتج")],
    [B("**Colonies on MacConkey**", "**المستعمرات على ماكونكي**"), B("pink", "وردية"), B("pale yellow", "صفراء شاحبة")]],
   key_cols=[0], widths=[30, 35, 35], style="summary", label_en="MacConkey agar", label_ar="أكار ماكونكي"),
 INSHORT([("Selective: **mannitol salt agar** (high NaCl → staphylococci), **MacConkey** (bile salts → bile-tolerant), **antibiotics**.", "الانتقائية: **أكار الملح والمانيتول** (ملح عالٍ ← العنقودية)، **ماكونكي** (أملاح صفراء ← المتحمّلة للصفراء)، **المضادات الحيوية**.")]),
 INSHORT([
          ("Indicator: sugar fermentation → acid → **pH indicator colour change**; MacConkey: lactose + **neutral red**.", "الدالّة: تخمّر السكر ← حامض ← **تغيّر لون دليل pH**؛ ماكونكي: لاكتوز + **الأحمر المتعادل**."),
          ("**E. coli → pink**, **Salmonella → pale yellow**; MacConkey is **selective + indicator**.", "**الإشريكية ← وردية**، **السالمونيلا ← صفراء شاحبة**؛ وماكونكي **انتقائي + دالّ**.")], en="In short (cont.)", ar="باختصار (تكملة)"),

 # ───────────────────────── 4. Pretest / posttest
 SEC("Pretest and posttest", "الاختبار القبلي والبعدي"),
 L(["Pretest: -How u can cultivate the bacteria in Lab. ?", "Posttest 1- Constituents of culture media are ---------,-----------", "Posttest 2- Which are common pathogenic bacteria isolated form urinary tract?"],
   ["الاختبار القبلي: كيف يمكنك زرع البكتيريا في المختبر؟", "الاختبار البعدي 1- مكوّنات الأوساط الزرعية هي ---------، -----------", "الاختبار البعدي 2- ما البكتيريا الممرضة الشائعة المعزولة من المجاري البولية؟"]),
 BN(["The scientific content listed in the sheet: Laboratory media; Constituents of culture media; Types of culture media.", "The model answers of these questions are in the question file (important questions)."],
    ["المحتوى العلمي المذكور في الورقة: الأوساط المختبرية؛ مكوّنات الأوساط الزرعية؛ أنواع الأوساط الزرعية.", "والإجابات النموذجية لهذه الأسئلة في ملف الأسئلة (الأسئلة المهمة)."]),

 *TERMS5([("Culture medium", "الوسط الزرعي / المزرعة / البيئة الزرعية"), ("Peptone", "الببتون / البروتين المهضوم جزئيًا"), ("Agar", "الأكار / الآجار"),
          ("Autoclave", "المؤصدة / جهاز التعقيم بالبخار المضغوط"), ("Petri dish", "طبق بتري"), ("Fastidious bacteria", "البكتيريا صعبة النمو / المتطلّبة"),
          ("Broth", "المرق / الوسط السائل"), ("Enriched medium", "الوسط المُغنى / الوسط المدعَّم"), ("Selective medium", "الوسط الانتقائي"),
          ("Indicator (differential) medium", "الوسط الدالّ / الوسط التفريقي"), ("Blood agar", "أكار الدم"), ("Chocolate agar", "أكار الشوكولاتة / أكار الدم المسخّن"),
          ("MacConkey agar", "أكار ماكونكي"), ("Mannitol salt agar", "أكار الملح والمانيتول"), ("Lactose fermenter", "مخمّر اللاكتوز"),
          ("Neutral red", "الأحمر المتعادل"), ("Bile salts", "أملاح الصفراء"), ("Biphasic medium", "الوسط ثنائي الطور"),
          ("Robertson's cooked meat medium", "وسط روبرتسون للحم المطبوخ"), ("Thioglycollate broth", "مرق الثايوغلايكوليت")]),
]

SPECIES = re.compile(r"\b(?:Escherichia coli|Salmonella spp\.|E\. coli)")
def ital(s):
    out, i = [], 0
    for m in SPECIES.finditer(s):
        if s[:m.start()].endswith("__") or s[:m.start()].count("**") % 2: continue
        out.append(s[i:m.start()]); out.append(f"__{m.group(0)}__"); i = m.end()
    out.append(s[i:]); return "".join(out)
for b in blocks:
    if b.get("t") == "table":
        b["rows"] = [[[ital(c[0]), c[1]] if isinstance(c, list) else c for c in r] for r in b["rows"]]

exec(open(__file__.replace("b6.py", "b6q.py")).read())

```
