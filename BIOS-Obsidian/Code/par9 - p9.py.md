---
source: BIOS-Obsidian/tools/scripts/par9/p9.py
handouts: [parasitology-week9-theory]
saved: 2026-11-12
tags: [bios, code]
---
# par9/p9.py

Generator script — writes the handout's `lecture.json`.

Handouts: [[06 فهرس الملازم#parasitology-week9-theory|parasitology-week9-theory]]

```python
import sys, os, shutil, re; sys.path.insert(0, "/tmp/claude-0/-home-user-kwmdkm/a7dd109e-db53-5fd3-8234-9dab3a530e24/scratchpad/imm456")
from ci import *            # c helpers + B INSHORT TERMS balance save(split.fix)
sys.path.insert(0, "/tmp/claude-0/-home-user-kwmdkm/a7dd109e-db53-5fd3-8234-9dab3a530e24/scratchpad"); from bidi import ltr_all; from flowfit import fit
import split; split.ABBR += ("L.", "spp.")   # "the L. major homologue" is not a sentence end

# Diagnostic Parasitology (theory, stage 4, Prof. Dr. Nizar Al-Khafaji) — week 9: genus Leishmania, properties of ideal
# vaccines, Leishmania vaccine in trial. Source: text pasted by the user (no figures and no questions in it).
# The title promises "Properties of ideal vaccines" but the text never lists them → BIOS explanation box.
# Stage 4 → wineoat + separate question file.
def _q(a):
    f = lambda x: re.sub(r"“([^”]*[A-Za-z][^”]*)”", lambda m: "`“" + m.group(1).replace("**", "") + "”`", x)
    return [f(x) for x in a] if isinstance(a, list) else f(a)
BN = lambda en, ar: N(en, _q(ar), label=["BIOS note", "ملاحظة BIOS"])
BX = lambda en, ar: N(en, ar, label=["BIOS explanation", "شرح BIOS"])
O = P
FOLDER = "parasitology-week9-theory"
SRC = "/tmp/claude-0/-home-user-kwmdkm/a7dd109e-db53-5fd3-8234-9dab3a530e24/scratchpad/par9"
def G(te, ta, en, ar): return dict(t="group", title_en=te, title_ar=ta, en=en, ar=ar, style="light")
def TERMS6(terms, n=6):
    head = [B("Term", "المصطلح"), "الترجمات العربية المستعملة"]
    return [SEC("Key terms", "أهم المصطلحات")] + [T(head, [[f"**{e}**", a] for e, a in terms[i:i + n]], ar_cols=[1], widths=[36, 64])
                                                  for i in range(0, len(terms), n)]

blocks = [
 # ───────────────────────── 0 contents
 SEC("Contents of the week", "محتويات الأسبوع"),
 C("**9th Week**", "**الأسبوع التاسع**"),
 C("**Genus Leishmania; Properties of ideal vaccines; Leishmania vaccine in trial**",
   "**جنس الليشمانيا؛ صفات اللقاح المثالي؛ لقاح الليشمانيا قيد التجربة**"),
 C("**Properties of ideal vaccine as Leishmania Vaccine in trial**", "**صفات اللقاح المثالي ولقاح الليشمانيا قيد التجربة**"),
 BX(["The heading promises **properties of an ideal vaccine**, but the text of the week does not list them — it is all about the **Leishmania vaccine in trial**. The properties are therefore given here as a **BIOS explanation** (not the lecturer's text), because the heading asks for them.",
     "An **ideal vaccine** should be: **safe** (no disease, no serious side effects), **effective** (strong protection in most people), **long-lasting** (memory, few or no boosters), **broadly protective** (covers the species/strains in the area), **stable and cheap** (easy transport and storage, suitable for poor endemic areas), **easy to give** (few doses, simple route) and **easy to distinguish from infection** in the laboratory."],
    ["العنوان يَعِد **بصفات اللقاح المثالي**، لكن نصّ الأسبوع لا يعدّدها — فكلّه عن **لقاح الليشمانيا قيد التجربة**. ولذلك كُتبت الصفات هنا **شرحًا من BIOS** (لا من نصّ المحاضر)، لأن العنوان يطلبها.",
     "**اللقاح المثالي** يجب أن يكون: **آمنًا** (لا يسبّب المرض ولا آثارًا جانبية خطيرة)، و**فعّالًا** (حماية قوية لمعظم الناس)، و**طويل الأمد** (ذاكرة مناعية، بجرعات معزّزة قليلة أو بلا)، و**واسع الحماية** (يغطّي الأنواع والسلالات الموجودة في المنطقة)، و**ثابتًا ورخيصًا** (سهل النقل والخزن، مناسبًا للمناطق الفقيرة المتوطّنة)، و**سهل الإعطاء** (جرعات قليلة وطريق بسيط)، و**يسهل تمييزه عن العدوى** في المختبر."]),
 T([B("Property", "الصفة"), B("What it means", "ما المقصود")],
   [[B("**Safe**", "**آمن**"), B("does not cause the disease or serious side effects", "لا يسبّب المرض ولا آثارًا جانبية خطيرة")],
    [B("**Effective (immunogenic)**", "**فعّال (محفّز للمناعة)**"), B("gives strong protection in most vaccinated people", "يعطي حماية قوية لمعظم الملقَّحين")],
    [B("**Long-lasting**", "**طويل الأمد**"), B("immunological memory; few or no boosters", "ذاكرة مناعية؛ جرعات معزّزة قليلة أو بلا")],
    [B("**Broadly protective**", "**واسع الحماية**"), B("covers the species and strains of the area", "يغطّي أنواع المنطقة وسلالاتها")],
    [B("**Stable and cheap**", "**ثابت ورخيص**"), B("easy transport and storage in poor endemic areas", "سهل النقل والخزن في المناطق المتوطّنة الفقيرة")],
    [B("**Easy to give**", "**سهل الإعطاء**"), B("few doses, simple route of administration", "جرعات قليلة وطريق إعطاء بسيط")]],
   key_cols=[0], widths=[32, 68], style="summary", label_en="BIOS — properties of an ideal vaccine", label_ar="BIOS — صفات اللقاح المثالي"),

 # ───────────────────────── 1 why a vaccine is feasible
 SEC("Why a vaccine is feasible", "لماذا اللقاح ممكن"),
 C("**Leishmaniasis** is a disease that is **most likely to be controlled by a successful vaccination program**.",
   "**داء الليشمانيات** مرض **يُرجَّح جدًا السيطرة عليه ببرنامج تلقيح ناجح**."),
 C("The relatively **uncomplicated leishmanial life cycle** and the fact that **recovery from a primary infection renders the host resistant to subsequent infections** indicate that **vaccine is feasible**.",
   "إن **دورة حياة الليشمانيا غير المعقّدة** نسبيًا، وكون **الشفاء من العدوى الأولية يجعل المضيف مقاومًا للإصابات اللاحقة**، يدلّان على أن **اللقاح ممكن**."),
 C("Evidence from studies in **animal models, mainly mice**, indicates that **protection can be achieved** upon immunization with various vaccine formulations, however, **to date such vaccines have been disappointing when tested in the field**.",
   "تدلّ أدلّة الدراسات في **النماذج الحيوانية، وأساسًا الفئران**، على أنه **يمكن تحقيق الحماية** بالتمنيع بتركيبات لقاحية مختلفة، **لكن هذه اللقاحات كانت حتى الآن مخيّبة للآمال عند اختبارها ميدانيًا**."),
 C("Leishmania vaccine development has proven to be a **difficult and challenging task**, which is mostly hampered by **inadequate knowledge of parasite pathogenesis** and the **complexity of immune responses needed for protection**.",
   "أثبت تطوير لقاح الليشمانيا أنه **مهمّة صعبة ومليئة بالتحدّيات**، يعوقها أساسًا **عدم كفاية المعرفة بإمراضية الطفيلي** و**تعقّد الاستجابات المناعية اللازمة للحماية**."),
 BX("**Why recovery protects:** healing of a cutaneous lesion leaves a strong **cell-mediated (Th1) immunity** — this is also the idea behind the old practice of **leishmanization** (deliberate inoculation of live parasites in a hidden site to produce one controlled lesion and lifelong immunity).",
    "**لماذا يحمي الشفاء:** شفاء الآفة الجلدية يترك **مناعة خلوية قوية (`Th1`)** — وهذه أيضًا فكرة الممارسة القديمة **التلقيح بالليشمانيا (`leishmanization`)**: حقن طفيليات حيّة عمدًا في موضع مستور لإحداث آفة واحدة مضبوطة ومناعة مدى الحياة."),
 INSHORT([("Leishmaniasis is a **good candidate** for a vaccine: **simple life cycle** + **recovery gives resistance** to later infections.",
           "داء الليشمانيات **مرشّح جيد** للّقاح: **دورة حياة بسيطة** + **الشفاء يعطي مقاومة** للإصابات اللاحقة."),
          ("In **mice** many formulations protect, but **in the field they have been disappointing**.",
           "في **الفئران** تحمي تركيبات كثيرة، لكنها **كانت مخيّبة ميدانيًا**."),
          ("Obstacles: poor knowledge of **pathogenesis** + **complex immune responses** needed.",
           "العوائق: ضعف معرفة **الإمراضية** + **تعقّد الاستجابات المناعية** المطلوبة.")]),

 # ───────────────────────── 2 one antigen is not enough
 SEC("Combination vaccines", "اللقاحات المركّبة"),
 C("It is **highly unlikely** a successful antileishmanial vaccine will be based on a **single antigen**.",
   "**من المستبعد جدًا** أن يقوم لقاح ناجح مضادّ لليشمانيا على **مستضد واحد**."),
 C("**Combination vaccines** composed of **multiple antigens** and **well- developed adjuvants**, such as **Leish 111f and MPL –SE** , have the **best chances to succussed**.",
   "**اللقاحات المركّبة** المؤلَّفة من **مستضدات متعدّدة** و**مواد مساعدة جيدة التطوير**، مثل **`Leish-111f`** و**`MPL–SE`**، لها **أفضل فرص النجاح**."),
 BN(["“succussed” = **succeed**.",
     "**`MPL–SE`** is the **adjuvant** (monophosphoryl lipid A in a stable emulsion), not a second antigen: `Leish-111f` is the antigen and `MPL–SE` is given with it to strengthen the immune response."],
    ["“succussed” صحيحها **succeed** أي تنجح.",
     "**`MPL–SE`** هو **المادة المساعدة** (أحادي فوسفوريل الدهن `A` في مستحلب ثابت)، لا مستضد ثانٍ: فـ`Leish-111f` هو المستضد، و`MPL–SE` يُعطى معه لتقوية الاستجابة المناعية."]),
 BX("An **adjuvant** is a substance added to a vaccine to **make the immune response stronger and longer** without being the antigen itself (e.g. alum, `MPL–SE`).",
    "**المادة المساعدة (`adjuvant`)** مادة تُضاف إلى اللقاح **لتقوية الاستجابة المناعية وإطالتها** دون أن تكون هي المستضد (مثل الشبّة و`MPL–SE`)."),
 C("**Majority of experimental vaccines** were tested against the **cutaneous form** of the disease in the **mouse model**.",
   "**اختُبرت أغلب اللقاحات التجريبية** ضدّ **الشكل الجلدي** من المرض في **نموذج الفأر**."),
 C("Although the demands for a **VL vaccine** are **more complex** than for a **CL vaccine**, it is believed that **human VL trials will follow any successful CL immunization program**.",
   "ومع أن متطلّبات **لقاح الليشمانيا الحشوية (`VL`)** **أعقد** من متطلّبات **لقاح الليشمانيا الجلدية (`CL`)**، يُعتقد أن **تجارب الليشمانيا الحشوية في الإنسان ستتبع أيّ برنامج تمنيع ناجح للشكل الجلدي**."),
 BN("The file uses **`CL`** and **`VL`** without defining them: `CL` = **cutaneous leishmaniasis** (the skin form), `VL` = **visceral leishmaniasis** (kala-azar — liver, spleen, bone marrow; fatal if untreated).",
    "يستعمل الملف **`CL`** و**`VL`** دون تعريفهما: `CL` = **الليشمانيا الجلدية** (الشكل الجلدي)، و`VL` = **الليشمانيا الحشوية** (الكالا آزار — الكبد والطحال ونقي العظم؛ مميتة إن لم تُعالَج)."),
 T([B("", ""), B("CL — cutaneous", "الجلدية `CL`"), B("VL — visceral", "الحشوية `VL`")],
   [[B("**Site**", "**الموضع**"), B("skin (ulcer at the bite site)", "الجلد (قرحة في موضع اللدغة)"), B("liver, spleen, bone marrow", "الكبد والطحال ونقي العظم")],
    [B("**Severity**", "**الشدّة**"), B("usually self-healing, leaves a scar", "تُشفى ذاتيًا غالبًا وتترك ندبة"), B("fatal if untreated (kala-azar)", "مميتة إن لم تُعالَج (الكالا آزار)")],
    [B("**Vaccine work**", "**العمل اللقاحي**"), B("most experimental vaccines, mouse model", "أغلب اللقاحات التجريبية، نموذج الفأر"), B("demands are more complex; trials follow CL success", "متطلّباتها أعقد؛ وتجاربها تتبع نجاح الجلدية")]],
   key_cols=[0], widths=[20, 40, 40], style="summary", label_en="BIOS — CL vs VL", label_ar="BIOS — الجلدية مقابل الحشوية"),
 INSHORT([("A successful vaccine will **not** be based on a **single antigen** — **multiple antigens + good adjuvant** (`Leish-111f` with `MPL–SE`).",
           "اللقاح الناجح **لن** يقوم على **مستضد واحد** — بل **مستضدات متعدّدة + مادة مساعدة جيدة** (`Leish-111f` مع `MPL–SE`)."),
          ("Most experimental vaccines were tested against **CL in mice**; **VL** is more demanding and follows **CL** success.",
           "أغلب اللقاحات التجريبية اختُبرت ضدّ **الجلدية في الفئران**؛ و**الحشوية** أصعب وتتبع نجاح **الجلدية**.")]),

 # ───────────────────────── 3 generations of vaccines
 SEC("Approaches to the vaccine", "مناهج تطوير اللقاح"),
 C("To date, **several different approaches** to antileishmanial vaccine have been tested.",
   "جُرّبت حتى الآن **عدّة مناهج مختلفة** للّقاح المضادّ لليشمانيا."),
 H2("First generation vaccines", "لقاحات الجيل الأول"),
 C("**First generation vaccines** composed of **whole killed parasites** have been proposed as both **prophylactic and therapeutic** vaccines.",
   "**لقاحات الجيل الأول** المؤلَّفة من **طفيليات كاملة مقتولة** اقتُرحت لقاحات **وقائية وعلاجية** معًا."),
 C("In general, the **whole – cell, killed vaccines** have been **rather poorly defined and variable in potency**, hence they have **rendered inconclusive results**.",
   "وعمومًا كانت **لقاحات الخلايا الكاملة المقتولة** **غير محدّدة التركيب جيدًا ومتفاوتة الفاعلية**، ولذلك **أعطت نتائج غير حاسمة**."),
 BX("**Prophylactic** = given to a healthy person **to prevent** the disease; **therapeutic** = given to a patient **as part of treatment** (immunotherapy, often with the drug).",
    "**الوقائي** = يُعطى للشخص السليم **لمنع** المرض؛ و**العلاجي** = يُعطى للمريض **ضمن العلاج** (مناعي علاجي، وغالبًا مع الدواء)."),
 H2("Second generation vaccines", "لقاحات الجيل الثاني"),
 C("**Most of the vaccine studies concentrate on the second-generation vaccines** consisting of **recombinant proteins, poly- proteins, DNA vaccines** or **dendritic cells loaded with peptides** derived from leishmanial antigens.",
   "**تتركّز معظم دراسات اللقاح على لقاحات الجيل الثاني** المؤلَّفة من **بروتينات مأشوبة، وبروتينات متعدّدة، ولقاحات الدنا**، أو **خلايا تغصّنية محمّلة ببيبتيدات** مشتقّة من مستضدات الليشمانيا."),
 C("To date, **only one second generation vaccine, Leish -111f, has been assessed in clinical trials**.",
   "وحتى الآن **لم يُقيَّم في التجارب السريرية إلا لقاح واحد من الجيل الثاني هو `Leish-111f`**."),
 T([B("Generation", "الجيل"), B("What it is made of", "ممّ يتكوّن"), B("Result", "النتيجة")],
   [[B("**First generation**", "**الجيل الأول**"), B("whole killed parasites (prophylactic + therapeutic)", "طفيليات كاملة مقتولة (وقائي + علاجي)"), B("poorly defined, variable potency → inconclusive", "غير محدّد جيدًا، فاعلية متفاوتة ← نتائج غير حاسمة")],
    [B("**Second generation**", "**الجيل الثاني**"), B("recombinant proteins, poly-proteins, DNA vaccines, dendritic cells with peptides", "بروتينات مأشوبة، بروتينات متعدّدة، لقاحات دنا، خلايا تغصّنية ببيبتيدات"), B("most studies; only `Leish-111f` reached clinical trials", "معظم الدراسات؛ و`Leish-111f` وحده وصل التجارب السريرية")],
    [B("**Live attenuated**", "**الحيّ الموهَن**"), B("avirulent parasites made by a defined genetic alteration", "طفيليات غير ضارية تُنتَج بتغيير وراثي محدّد"), B("an alternative — mimics the natural infection", "بديل — يحاكي العدوى الطبيعية")]],
   key_cols=[0], widths=[22, 48, 30], style="summary", label_en="BIOS — the vaccine approaches", label_ar="BIOS — مناهج اللقاح"),
 INSHORT([("**First generation** = whole **killed** parasites: poorly defined, variable potency → **inconclusive**.",
           "**الجيل الأول** = طفيليات **مقتولة** كاملة: غير محدّدة، فاعلية متفاوتة ← **نتائج غير حاسمة**."),
          ("**Second generation** = recombinant proteins, poly-proteins, **DNA vaccines**, dendritic cells with peptides — most of the studies.",
           "**الجيل الثاني** = بروتينات مأشوبة، بروتينات متعدّدة، **لقاحات دنا**، خلايا تغصّنية ببيبتيدات — وهي معظم الدراسات."),
          ("Only **`Leish-111f`** has been assessed in **clinical trials**.", "و**`Leish-111f`** وحده قُيّم في **التجارب السريرية**.")]),

 # ───────────────────────── 4 Leish-111f
 SEC("Leish-111f", "لقاح `Leish-111f`"),
 C("**Leish- 111f** is a **single poly protein** composed of **three molecules fused**; the **L. major homologue of eukaryotic thiol- specific antioxidant (TSA)**, the **L. major stress- inducible protein -1(LmST11)**and the **L. braziliensis elongation and initiation factor (LeIF)**.",
   "**`Leish-111f`** **بروتين متعدّد واحد** مؤلَّف من **ثلاثة جزيئات مندمجة**: **نظير الليشمانيا الكبرى لمضادّ الأكسدة النوعي للثايول في حقيقيات النوى (`TSA`)**، و**بروتين الليشمانيا الكبرى المستحثّ بالإجهاد 1 (`LmSTI1`)**، و**عامل الاستطالة والبدء من الليشمانيا البرازيلية (`LeIF`)**."),
 BN(["“**LmST11**” (with two ones) is written in the literature **`LmSTI1`** — Leishmania major **S**tress-**I**nducible protein **1**.",
     "The name is written three ways in the file (“Leish 111f”, “Leish -111f”, “Leish- 111f”) — all are the same vaccine, **`Leish-111f`**."],
    ["“**LmST11**” (بواحدَين) تُكتب في المراجع **`LmSTI1`** — بروتين الليشمانيا الكبرى المستحثّ بالإجهاد 1.",
     "والاسم مكتوب بثلاث صور في الملف (“Leish 111f”، “Leish -111f”، “Leish- 111f”) — وكلّها اللقاح نفسه **`Leish-111f`**."]),
 T([B("Molecule in the fusion", "الجزيء في الاندماج"), B("Origin", "المصدر")],
   [[B("**TSA** — thiol-specific antioxidant homologue", "**`TSA`** — نظير مضادّ الأكسدة النوعي للثايول"), B("L. major", "الليشمانيا الكبرى")],
    [B("**LmSTI1** — stress-inducible protein 1", "**`LmSTI1`** — البروتين المستحثّ بالإجهاد 1"), B("L. major", "الليشمانيا الكبرى")],
    [B("**LeIF** — elongation and initiation factor", "**`LeIF`** — عامل الاستطالة والبدء"), B("L. braziliensis", "الليشمانيا البرازيلية")]],
   key_cols=[0], widths=[64, 36], style="summary", label_en="BIOS — the three fused molecules of Leish-111f", label_ar="BIOS — جزيئات Leish-111f الثلاثة المندمجة"),
 BX("A **poly-protein** is one protein made by **fusing several antigens into a single chain**, so one molecule carries several targets — and `Leish-111f` is given with the adjuvant `MPL–SE`.",
    "**البروتين المتعدّد** بروتين واحد يُصنع **بدمج عدّة مستضدات في سلسلة واحدة**، فيحمل الجزيء الواحد عدّة أهداف — ويُعطى `Leish-111f` مع المادة المساعدة `MPL–SE`."),
 INSHORT([("**`Leish-111f`** = a **single poly-protein** of **three fused molecules**: **`TSA`** and **`LmSTI1`** (L. major) + **`LeIF`** (L. braziliensis).",
           "**`Leish-111f`** = **بروتين متعدّد واحد** من **ثلاثة جزيئات مندمجة**: **`TSA`** و**`LmSTI1`** (الكبرى) + **`LeIF`** (البرازيلية)."),
          ("It is the **only second-generation vaccine** assessed in clinical trials, given with **`MPL–SE`**.",
           "وهو **اللقاح الوحيد من الجيل الثاني** المقيَّم في التجارب السريرية، ويُعطى مع **`MPL–SE`**.")]),

 # ───────────────────────── 5 sand fly saliva
 SEC("Sand fly saliva", "لعاب ذبابة الرمل"),
 C("**Sand fly saliva** contains an **array of molecules able to interfere with the host immune response**, therefore, **immunity against saliva components may indirectly enhance-anti- leishmanial immunity**.",
   "يحتوي **لعاب ذبابة الرمل** على **مجموعة من الجزيئات القادرة على التداخل مع استجابة المضيف المناعية**، ولذلك فإن **المناعة ضدّ مكوّنات اللعاب قد تعزّز بصورة غير مباشرة المناعة المضادّة لليشمانيا**."),
 C("**More recently**, it has been shown that **vector salivary proteins**, in particular **LJM19**, **protect hamster from VL**.",
   "و**حديثًا** تبيّن أن **بروتينات لعاب الناقل**، ولا سيّما **`LJM19`**، **تحمي الهامستر من الليشمانيا الحشوية**."),
 BX("The parasite is injected **together with the saliva**; the saliva's molecules **suppress the local immune response** and help the parasite establish. If the host is **already immune to the saliva**, an inflammatory reaction at the bite site **makes the environment hostile to the parasite** — this is the idea of a **saliva-based (vector) vaccine**.",
    "يُحقن الطفيلي **مع اللعاب**؛ وجزيئات اللعاب **تكبح الاستجابة المناعية الموضعية** وتساعد الطفيلي على التوطّن. وإذا كان المضيف **ممنّعًا أصلًا ضدّ اللعاب** فإن تفاعلًا التهابيًا في موضع اللدغة **يجعل البيئة معادية للطفيلي** — وهذه فكرة **اللقاح المعتمد على اللعاب (لقاح الناقل)**."),
 BN("“enhance-anti- leishmanial” is written with stray hyphens in the file — it means **enhance anti-leishmanial immunity**; “protect hamster” = protect **hamsters**.",
    "“enhance-anti- leishmanial” مكتوبة بشُرَط زائدة في الملف — ومعناها **تعزّز المناعة المضادّة لليشمانيا**؛ و“protect hamster” أي تحمي **الهامستر** (الجمع)."),
 INSHORT([("Sand fly **saliva** interferes with the host immune response and helps the parasite.", "**لعاب** ذبابة الرمل يتداخل مع مناعة المضيف ويساعد الطفيلي."),
          ("Immunity **against the saliva** may indirectly protect; **`LJM19`** protected **hamsters from VL**.",
           "والمناعة **ضدّ اللعاب** قد تحمي بصورة غير مباشرة؛ و**`LJM19`** حمى **الهامستر من الحشوية**.")]),

 # ───────────────────────── 6 live attenuated
 SEC("Live attenuated Leishmania", "الليشمانيا الحيّة الموهَنة"),
 C("**Live – attenuated Leishmania** as an **alternative for vaccine development**.", "**الليشمانيا الحيّة الموهَنة** **بديلًا لتطوير اللقاح**."),
 C("By **mimicking the natural infection**, live – attenuated parasites can **deliver a complete spectrum of antigens to the antigens presenting cells**, in principle leading to a **better immune response** that results in a **better protective outcome** than that observed following immunization with a **subunit vaccine**.",
   "إن الطفيليات الحيّة الموهَنة، **بمحاكاتها العدوى الطبيعية**، تستطيع **إيصال طيف كامل من المستضدات إلى الخلايا العارضة للمستضد**، ممّا يؤدّي مبدئيًا إلى **استجابة مناعية أفضل** تُعطي **نتيجة وقائية أفضل** من الملاحَظة بعد التمنيع بـ**لقاح الوحدات الفرعية**."),
 C("**Avirulent microorganisms** can be generated by a **defined genetic alteration**, **eliminating the risk of parasite reversion to the virulent phenotype**.",
   "ويمكن توليد **أحياء مجهرية غير ضارية** **بتغيير وراثي محدّد**، ممّا **يزيل خطر رجوع الطفيلي إلى النمط الظاهري الضاري**."),
 BN("“the antigens presenting cells” = the **antigen-presenting cells (APCs)** — macrophages and dendritic cells.",
    "“the antigens presenting cells” صحيحها **الخلايا العارضة للمستضد (`APCs`)** — البلاعم والخلايا التغصّنية."),
 BX(["A **subunit vaccine** contains only **part of the parasite** (one or a few antigens), so it shows the immune system **few targets**; a **live attenuated** parasite shows it **the whole spectrum**, as in a natural infection.",
     "**Attenuated** = weakened so that it **cannot cause disease** but is still alive. The danger of older attenuated strains was **reversion** to a virulent form; a **defined genetic alteration** (deleting a known essential gene) removes that risk."],
    ["**لقاح الوحدات الفرعية** يحتوي **جزءًا من الطفيلي** فقط (مستضدًا أو بضعة مستضدات)، فيعرض على الجهاز المناعي **أهدافًا قليلة**؛ أما الطفيلي **الحيّ الموهَن** فيعرض عليه **الطيف كلّه** كما في العدوى الطبيعية.",
     "**الموهَن** = مُضعَّف بحيث **لا يستطيع إحداث المرض** لكنه ما يزال حيًّا. وخطر السلالات الموهَنة القديمة كان **الرجوع** إلى شكل ضارٍ؛ و**التغيير الوراثي المحدّد** (حذف جين أساسي معروف) يزيل هذا الخطر."]),
 T([B("", ""), B("Subunit vaccine", "لقاح الوحدات الفرعية"), B("Live attenuated", "الحيّ الموهَن")],
   [[B("**Contains**", "**يحتوي**"), B("one or a few antigens", "مستضدًا أو بضعة مستضدات"), B("the whole living (weakened) parasite", "الطفيلي الحيّ (المضعَّف) كلّه")],
    [B("**Antigens shown to APCs**", "**المستضدات المعروضة**"), B("few", "قليلة"), B("a complete spectrum", "طيف كامل")],
    [B("**Immune response**", "**الاستجابة المناعية**"), B("weaker", "أضعف"), B("better — mimics natural infection", "أفضل — تحاكي العدوى الطبيعية")],
    [B("**Main risk**", "**الخطر الرئيسي**"), B("not enough protection", "حماية غير كافية"), B("reversion to virulence — removed by a defined genetic alteration", "الرجوع إلى الضراوة — يُزال بتغيير وراثي محدّد")]],
   key_cols=[0], widths=[26, 37, 37], style="summary", label_en="BIOS — subunit vs live attenuated", label_ar="BIOS — الوحدات الفرعية مقابل الحيّ الموهَن"),
 INSHORT([("**Live attenuated** parasites **mimic the natural infection** and deliver a **complete spectrum of antigens** to the **APCs**.",
           "الطفيليات **الحيّة الموهَنة** **تحاكي العدوى الطبيعية** وتوصل **طيفًا كاملًا من المستضدات** إلى **الخلايا العارضة**."),
          ("Better protection than a **subunit** vaccine; **defined genetic alteration** removes the risk of **reversion to virulence**.",
           "حماية أفضل من **لقاح الوحدات الفرعية**؛ و**التغيير الوراثي المحدّد** يزيل خطر **الرجوع إلى الضراوة**.")]),
] + TERMS6([
 ("Leishmaniasis", "داء الليشمانيات / اللشمانيا"),
 ("Cutaneous leishmaniasis (CL)", "الليشمانيا الجلدية / حبّة بغداد"),
 ("Visceral leishmaniasis (VL)", "الليشمانيا الحشوية / الكالا آزار"),
 ("Vaccine", "اللقاح / التطعيم / المطعوم"),
 ("Immunization", "التمنيع / التلقيح"),
 ("Prophylactic", "وقائي"),
 ("Therapeutic", "علاجي"),
 ("Antigen", "المستضد"),
 ("Adjuvant", "المادة المساعدة / المعزّز المناعي"),
 ("Recombinant protein", "البروتين المأشوب / المهندَس وراثيًا"),
 ("Poly-protein", "البروتين المتعدّد / المندمج"),
 ("DNA vaccine", "لقاح الدنا / اللقاح الجيني"),
 ("Dendritic cell", "الخلية التغصّنية / المتغصّنة"),
 ("Antigen-presenting cell (APC)", "الخلية العارضة للمستضد"),
 ("Subunit vaccine", "لقاح الوحدات الفرعية"),
 ("Live attenuated", "حيّ موهَن / مضعَّف"),
 ("Avirulent", "غير ضارٍ / عديم الضراوة"),
 ("Virulent phenotype", "النمط الظاهري الضاري"),
 ("Reversion", "الرجوع / الارتداد إلى الضراوة"),
 ("Potency", "الفاعلية / القوّة"),
 ("Pathogenesis", "الإمراضية / آلية إحداث المرض"),
 ("Sand fly (Phlebotomus)", "ذبابة الرمل / الفاصدة"),
 ("Salivary protein", "البروتين اللعابي"),
 ("Clinical trial", "التجربة السريرية"),
])

# ───────────────────────── questions (BIOS — the file has none)
mcq = [
 {"topic_en": "Why a vaccine is feasible", "topic_ar": "لماذا اللقاح ممكن"},
 Q("Leishmaniasis is considered a good candidate for a vaccination program because:", "يُعدّ داء الليشمانيات مرشّحًا جيدًا لبرنامج التلقيح لأن:", O(("Its life cycle is relatively uncomplicated and recovery gives resistance", "دورة حياته غير معقّدة نسبيًا والشفاء يعطي مقاومة"), ("It has no animal reservoir", "ليس له مستودع حيواني"), ("It is not transmitted by a vector", "لا ينتقل بناقل"), ("It is always fatal", "مميت دائمًا")), "a"),
 Q("Recovery from a primary leishmanial infection makes the host:", "الشفاء من العدوى الليشمانية الأولية يجعل المضيف:", O(("More susceptible", "أكثر قابلية للإصابة"), ("Resistant to subsequent infections", "مقاومًا للإصابات اللاحقة"), ("A permanent carrier", "حاملًا دائمًا"), ("Unable to make antibodies", "غير قادر على تكوين الأضداد")), "b"),
 Q("The main animal model used in leishmanial vaccine studies is the:", "النموذج الحيواني الرئيسي في دراسات لقاح الليشمانيا:", O(("Rabbit", "الأرنب"), ("Dog", "الكلب"), ("Mouse", "الفأر"), ("Monkey", "القرد")), "c"),
 Q("Experimental leishmanial vaccines that protect in animals have, in the field, been:", "اللقاحات الليشمانية التجريبية التي تحمي في الحيوانات كانت ميدانيًا:", O(("Highly successful", "ناجحة جدًا"), ("Never tested", "لم تُختبر أبدًا"), ("Better than in animals", "أفضل منها في الحيوانات"), ("Disappointing", "مخيّبة للآمال")), "d"),
 Q("Leishmania vaccine development is mostly hampered by:", "يعوق تطوير لقاح الليشمانيا أساسًا:", O(("Inadequate knowledge of pathogenesis and complex immune responses", "عدم كفاية معرفة الإمراضية وتعقّد الاستجابات المناعية"), ("The high cost of mice", "ارتفاع كلفة الفئران"), ("Absence of any antigen", "عدم وجود أيّ مستضد"), ("Lack of patients", "قلّة المرضى")), "a"),
 {"topic_en": "Combination vaccines, CL and VL", "topic_ar": "اللقاحات المركّبة والجلدية والحشوية"},
 Q("A successful antileishmanial vaccine is highly unlikely to be based on:", "من المستبعد جدًا أن يقوم اللقاح الناجح المضادّ لليشمانيا على:", O(("Multiple antigens", "مستضدات متعدّدة"), ("A single antigen", "مستضد واحد"), ("An adjuvant", "مادة مساعدة"), ("A poly-protein", "بروتين متعدّد")), "b"),
 Q("In the combination “Leish-111f and MPL–SE”, MPL–SE is the:", "في التركيب “`Leish-111f` و`MPL–SE`” يكون `MPL–SE`:", O(("Second antigen", "المستضد الثاني"), ("Parasite strain", "سلالة الطفيلي"), ("Adjuvant", "المادة المساعدة"), ("Diluent only", "مجرّد مُذيب")), "c"),
 Q("An adjuvant is a substance that:", "المادة المساعدة مادة:", O(("Replaces the antigen", "تحلّ محلّ المستضد"), ("Kills the parasite in the host", "تقتل الطفيلي في المضيف"), ("Preserves the vaccine only", "تحفظ اللقاح فقط"), ("Strengthens and prolongs the immune response", "تقوّي الاستجابة المناعية وتطيلها")), "d"),
 Q("The majority of experimental vaccines were tested against:", "اختُبرت أغلب اللقاحات التجريبية ضدّ:", O(("The cutaneous form in the mouse model", "الشكل الجلدي في نموذج الفأر"), ("The visceral form in dogs", "الشكل الحشوي في الكلاب"), ("Mucocutaneous disease in man", "الداء الجلدي المخاطي في الإنسان"), ("Trypanosomiasis", "داء المثقّبيات")), "a"),
 Q("Compared with a CL vaccine, the demands for a VL vaccine are:", "مقارنةً بلقاح الجلدية، فإن متطلّبات لقاح الحشوية:", O(("Identical", "متطابقة"), ("More complex", "أعقد"), ("Much simpler", "أبسط بكثير"), ("Not studied at all", "غير مدروسة إطلاقًا")), "b"),
 Q("It is believed that human VL trials will:", "يُعتقد أن تجارب الحشوية في الإنسان:", O(("Replace CL studies", "ستحلّ محلّ دراسات الجلدية"), ("Never be done", "لن تُجرى أبدًا"), ("Follow any successful CL immunization program", "ستتبع أيّ برنامج تمنيع ناجح للجلدية"), ("Precede all animal work", "ستسبق كل العمل الحيواني")), "c"),
 {"topic_en": "Generations of vaccines", "topic_ar": "أجيال اللقاحات"},
 Q("First generation leishmanial vaccines are composed of:", "تتكوّن لقاحات الجيل الأول لليشمانيا من:", O(("Recombinant proteins", "بروتينات مأشوبة"), ("DNA plasmids", "بلازميدات دنا"), ("Dendritic cells", "خلايا تغصّنية"), ("Whole killed parasites", "طفيليات كاملة مقتولة")), "d"),
 Q("First generation vaccines were proposed as:", "اقتُرحت لقاحات الجيل الأول بوصفها:", O(("Both prophylactic and therapeutic vaccines", "لقاحات وقائية وعلاجية معًا"), ("Prophylactic only", "وقائية فقط"), ("Therapeutic only", "علاجية فقط"), ("Diagnostic reagents", "كواشف تشخيصية")), "a"),
 Q("The results of whole-cell killed vaccines have been:", "كانت نتائج لقاحات الخلايا الكاملة المقتولة:", O(("Completely protective", "واقية تمامًا"), ("Inconclusive, with variable potency", "غير حاسمة، وفاعليتها متفاوتة"), ("Better than all others", "أفضل من كل غيرها"), ("Never published", "لم تُنشر أبدًا")), "b"),
 Q("Which is NOT a second generation vaccine component?", "أيّ مما يأتي ليس من مكوّنات لقاحات الجيل الثاني؟", O(("Recombinant proteins", "البروتينات المأشوبة"), ("DNA vaccines", "لقاحات الدنا"), ("Whole killed parasites", "الطفيليات الكاملة المقتولة"), ("Dendritic cells loaded with peptides", "خلايا تغصّنية محمّلة ببيبتيدات")), "c"),
 Q("The only second generation vaccine assessed in clinical trials is:", "اللقاح الوحيد من الجيل الثاني المقيَّم في التجارب السريرية:", O(("MPL–SE", "`MPL–SE`"), ("LJM19", "`LJM19`"), ("LeIF alone", "`LeIF` وحده"), ("Leish-111f", "`Leish-111f`")), "d",),
 {"topic_en": "Leish-111f and sand fly saliva", "topic_ar": "لقاح Leish-111f ولعاب ذبابة الرمل"},
 Q("Leish-111f is:", "لقاح `Leish-111f`:", O(("A single poly-protein of three fused molecules", "بروتين متعدّد واحد من ثلاثة جزيئات مندمجة"), ("A killed whole parasite", "طفيلي كامل مقتول"), ("A live attenuated strain", "سلالة حيّة موهَنة"), ("A salivary protein", "بروتين لعابي")), "a"),
 Q("Which molecule of Leish-111f comes from L. braziliensis?", "أيّ جزيء من `Leish-111f` مصدره الليشمانيا البرازيلية؟", O(("TSA", "`TSA`"), ("LeIF", "`LeIF`"), ("LmSTI1", "`LmSTI1`"), ("LJM19", "`LJM19`")), "b"),
 Q("TSA in Leish-111f stands for:", "يرمز `TSA` في `Leish-111f` إلى:", O(("Thiol-specific antibody", "ضدّ نوعي للثايول"), ("Total soluble antigen", "مستضد ذائب كلّي"), ("Thiol-specific antioxidant", "مضادّ أكسدة نوعي للثايول"), ("Trypanosoma surface antigen", "مستضد سطحي للمثقّبة")), "c"),
 Q("Sand fly saliva contains molecules that:", "يحتوي لعاب ذبابة الرمل جزيئات:", O(("Kill the parasite", "تقتل الطفيلي"), ("Have no effect on immunity", "لا تؤثّر في المناعة"), ("Replace the antigen", "تحلّ محلّ المستضد"), ("Interfere with the host immune response", "تتداخل مع استجابة المضيف المناعية")), "d"),
 Q("The salivary protein shown to protect hamsters from visceral leishmaniasis is:", "البروتين اللعابي الذي ثبت أنه يحمي الهامستر من الليشمانيا الحشوية:", O(("LJM19", "`LJM19`"), ("LmSTI1", "`LmSTI1`"), ("TSA", "`TSA`"), ("MPL–SE", "`MPL–SE`")), "a"),
 Q("Immunity against sand fly saliva components may:", "المناعة ضدّ مكوّنات لعاب ذبابة الرمل قد:", O(("Prevent the fly from biting", "تمنع الذبابة من اللدغ"), ("Indirectly enhance anti-leishmanial immunity", "تعزّز بصورة غير مباشرة المناعة المضادّة لليشمانيا"), ("Cause the disease", "تسبّب المرض"), ("Abolish all immunity", "تلغي كل مناعة")), "b"),
 {"topic_en": "Live attenuated vaccines", "topic_ar": "اللقاحات الحيّة الموهَنة"},
 Q("Live attenuated parasites are advantageous because they:", "تمتاز الطفيليات الحيّة الموهَنة لأنها:", O(("Are cheaper to store", "أرخص في الخزن"), ("Need no adjuvant at all", "لا تحتاج مادة مساعدة إطلاقًا"), ("Mimic the natural infection and deliver a complete spectrum of antigens", "تحاكي العدوى الطبيعية وتوصل طيفًا كاملًا من المستضدات"), ("Contain only one antigen", "تحتوي مستضدًا واحدًا فقط")), "c"),
 Q("Live attenuated parasites deliver antigens to the:", "توصل الطفيليات الحيّة الموهَنة المستضدات إلى:", O(("Red blood cells", "كريات الدم الحمر"), ("Platelets", "الصفيحات"), ("Hepatocytes only", "خلايا الكبد فقط"), ("Antigen-presenting cells", "الخلايا العارضة للمستضد")), "d"),
 Q("Compared with a subunit vaccine, a live attenuated vaccine in principle gives:", "مقارنةً بلقاح الوحدات الفرعية، يعطي اللقاح الحيّ الموهَن مبدئيًا:", O(("A better immune response and better protection", "استجابة مناعية أفضل وحماية أفضل"), ("A weaker response", "استجابة أضعف"), ("No response", "لا استجابة"), ("Only antibody responses", "استجابات ضدّية فقط")), "a"),
 Q("Avirulent organisms generated by a defined genetic alteration have the advantage of:", "الأحياء غير الضارية المولَّدة بتغيير وراثي محدّد تمتاز بـ:", O(("Being cheaper", "كونها أرخص"), ("Eliminating the risk of reversion to the virulent phenotype", "إزالة خطر الرجوع إلى النمط الظاهري الضاري"), ("Needing no cold chain", "عدم حاجتها إلى سلسلة التبريد"), ("Working without the immune system", "عملها دون الجهاز المناعي")), "b"),
]
mcq = balance(mcq, 42)

tf = [
 TF("The leishmanial life cycle is relatively uncomplicated.", "دورة حياة الليشمانيا غير معقّدة نسبيًا.", "T"),
 TF("Recovery from a primary leishmanial infection leaves the host more susceptible to later infections.", "الشفاء من العدوى الليشمانية الأولية يترك المضيف أكثر قابلية للإصابات اللاحقة.", "F"),
 TF("Vaccines that protected mice have also performed well in field trials.", "اللقاحات التي حمت الفئران أدّت أداءً جيدًا في التجارب الميدانية أيضًا.", "F"),
 TF("A successful antileishmanial vaccine is likely to need more than one antigen.", "يُرجَّح أن يحتاج اللقاح الناجح المضادّ لليشمانيا إلى أكثر من مستضد واحد.", "T"),
 TF("MPL–SE is an antigen of the Leishmania parasite.", "`MPL–SE` مستضد من طفيلي الليشمانيا.", "F"),
 TF("Most experimental vaccines were tested against the cutaneous form in mice.", "اختُبرت أغلب اللقاحات التجريبية ضدّ الشكل الجلدي في الفئران.", "T"),
 TF("First generation vaccines are made of whole killed parasites.", "لقاحات الجيل الأول مصنوعة من طفيليات كاملة مقتولة.", "T"),
 TF("Whole-cell killed vaccines gave clear and conclusive results.", "أعطت لقاحات الخلايا الكاملة المقتولة نتائج واضحة وحاسمة.", "F"),
 TF("Several second generation vaccines have reached clinical trials.", "وصلت عدّة لقاحات من الجيل الثاني إلى التجارب السريرية.", "F"),
 TF("Leish-111f contains molecules from both L. major and L. braziliensis.", "يحتوي `Leish-111f` جزيئات من الليشمانيا الكبرى والبرازيلية معًا.", "T"),
 TF("Sand fly salivary molecules can interfere with the host immune response.", "يمكن لجزيئات لعاب ذبابة الرمل أن تتداخل مع استجابة المضيف المناعية.", "T"),
 TF("A defined genetic alteration increases the risk of reversion to virulence.", "التغيير الوراثي المحدّد يزيد خطر الرجوع إلى الضراوة.", "F"),
]

traps = [
 TR("Leish-111f vs MPL–SE", "`Leish-111f` مقابل `MPL–SE`",
    "Leish-111f is the ANTIGEN (a poly-protein of three fused molecules); MPL–SE is the ADJUVANT given with it — not a second vaccine or antigen.",
    "`Leish-111f` هو **المستضد** (بروتين متعدّد من ثلاثة جزيئات مندمجة)؛ و`MPL–SE` هو **المادة المساعدة** التي تُعطى معه — لا لقاح ثانٍ ولا مستضد."),
 TR("Three molecules, two species", "ثلاثة جزيئات ونوعان",
    "In Leish-111f, TSA and LmSTI1 come from L. major, but LeIF comes from L. braziliensis — do not put all three under one species.",
    "في `Leish-111f` جاء `TSA` و`LmSTI1` من **الليشمانيا الكبرى**، أما `LeIF` فمن **البرازيلية** — لا تنسب الثلاثة إلى نوع واحد."),
 TR("Killed vs attenuated", "المقتول مقابل الموهَن",
    "First generation = whole KILLED parasites (dead). Live attenuated = the parasite is ALIVE but weakened — they are different approaches.",
    "الجيل الأول = طفيليات كاملة **مقتولة** (ميتة). والحيّ الموهَن = الطفيلي **حيّ** لكنه مضعَّف — وهما منهجان مختلفان."),
 TR("CL and VL", "الجلدية والحشوية",
    "CL = cutaneous (skin); VL = visceral (kala-azar). The VL vaccine is the MORE demanding one, and its human trials follow CL success — not the reverse.",
    "`CL` = الجلدية؛ و`VL` = الحشوية (الكالا آزار). ولقاح **الحشوية** هو **الأصعب**، وتجاربه البشرية تتبع نجاح الجلدية — لا العكس."),
 TR("Saliva immunity is indirect", "مناعة اللعاب غير مباشرة",
    "Immunity against sand fly saliva does not attack the parasite itself; it INDIRECTLY enhances anti-leishmanial immunity at the bite site.",
    "المناعة ضدّ لعاب ذبابة الرمل لا تهاجم الطفيلي نفسه؛ بل تعزّز **بصورة غير مباشرة** المناعة المضادّة لليشمانيا في موضع اللدغة."),
 TR("Subunit ≠ better", "الوحدات الفرعية ليست الأفضل",
    "A subunit vaccine shows the immune system FEW antigens; the live attenuated parasite gives a COMPLETE spectrum and, in principle, better protection.",
    "لقاح الوحدات الفرعية يعرض على الجهاز المناعي **مستضدات قليلة**؛ أما الطفيلي الحيّ الموهَن فيعطي **طيفًا كاملًا** وحماية أفضل مبدئيًا."),
]

important = [
 IM("Why is leishmaniasis considered a disease that can be controlled by vaccination?", "لماذا يُعدّ داء الليشمانيات مرضًا يمكن السيطرة عليه بالتلقيح؟",
    "Because the leishmanial life cycle is relatively uncomplicated, and because recovery from a primary infection renders the host resistant to subsequent infections — both indicate that a vaccine is feasible. Studies in animal models (mainly mice) show that protection can be achieved with various formulations, although field results have so far been disappointing.",
    "لأن دورة حياة الليشمانيا غير معقّدة نسبيًا، ولأن الشفاء من العدوى الأولية يجعل المضيف مقاومًا للإصابات اللاحقة — وكلاهما يدلّ على أن اللقاح ممكن. وتُظهر الدراسات في النماذج الحيوانية (وأساسًا الفئران) أنه يمكن تحقيق الحماية بتركيبات مختلفة، مع أن النتائج الميدانية كانت حتى الآن مخيّبة."),
 IM("What hampers the development of a Leishmania vaccine?", "ما الذي يعوق تطوير لقاح الليشمانيا؟",
    "Mainly inadequate knowledge of the parasite's pathogenesis and the complexity of the immune responses needed for protection; in addition, a single antigen is highly unlikely to be enough, and the whole-cell killed vaccines were poorly defined and variable in potency.",
    "أساسًا عدم كفاية المعرفة بإمراضية الطفيلي وتعقّد الاستجابات المناعية اللازمة للحماية؛ وإضافةً إلى ذلك من المستبعد جدًا أن يكفي مستضد واحد، كما أن لقاحات الخلايا الكاملة المقتولة كانت غير محدّدة التركيب ومتفاوتة الفاعلية."),
 IM("Compare first generation and second generation antileishmanial vaccines.", "قارن بين لقاحات الجيل الأول والثاني المضادّة لليشمانيا.",
    "First generation: whole killed parasites, proposed as both prophylactic and therapeutic vaccines; poorly defined and variable in potency, so the results were inconclusive. Second generation: recombinant proteins, poly-proteins, DNA vaccines or dendritic cells loaded with peptides derived from leishmanial antigens; most vaccine studies concentrate on them, but to date only Leish-111f has been assessed in clinical trials.",
    "الجيل الأول: طفيليات كاملة مقتولة، اقتُرحت لقاحات وقائية وعلاجية معًا؛ وكانت غير محدّدة التركيب ومتفاوتة الفاعلية فجاءت النتائج غير حاسمة. الجيل الثاني: بروتينات مأشوبة وبروتينات متعدّدة ولقاحات دنا أو خلايا تغصّنية محمّلة ببيبتيدات مشتقّة من مستضدات الليشمانيا؛ وتتركّز عليه معظم الدراسات، لكن `Leish-111f` وحده قُيّم حتى الآن في التجارب السريرية."),
 IM("Describe the composition of Leish-111f.", "صف تركيب لقاح `Leish-111f`.",
    "It is a single poly-protein composed of three fused molecules: the L. major homologue of the eukaryotic thiol-specific antioxidant (TSA), the L. major stress-inducible protein 1 (LmSTI1) and the L. braziliensis elongation and initiation factor (LeIF). It is used with a well-developed adjuvant (MPL–SE).",
    "هو بروتين متعدّد واحد مؤلَّف من ثلاثة جزيئات مندمجة: نظير الليشمانيا الكبرى لمضادّ الأكسدة النوعي للثايول (`TSA`)، وبروتين الليشمانيا الكبرى المستحثّ بالإجهاد 1 (`LmSTI1`)، وعامل الاستطالة والبدء من الليشمانيا البرازيلية (`LeIF`). ويُستعمل مع مادة مساعدة جيدة التطوير (`MPL–SE`)."),
 IM("What is the role of sand fly saliva in leishmanial vaccination?", "ما دور لعاب ذبابة الرمل في التلقيح ضدّ الليشمانيا؟",
    "Sand fly saliva contains an array of molecules able to interfere with the host immune response (helping the parasite establish); therefore immunity against saliva components may indirectly enhance anti-leishmanial immunity. Recently, vector salivary proteins, in particular LJM19, were shown to protect hamsters from visceral leishmaniasis.",
    "يحتوي لعاب ذبابة الرمل مجموعة من الجزيئات القادرة على التداخل مع استجابة المضيف المناعية (فتساعد الطفيلي على التوطّن)؛ ولذلك قد تعزّز المناعة ضدّ مكوّنات اللعاب بصورة غير مباشرة المناعة المضادّة لليشمانيا. وحديثًا تبيّن أن بروتينات لعاب الناقل، ولا سيّما `LJM19`، تحمي الهامستر من الليشمانيا الحشوية."),
 IM("Why are live attenuated Leishmania considered an alternative for vaccine development?", "لماذا تُعدّ الليشمانيا الحيّة الموهَنة بديلًا لتطوير اللقاح؟",
    "Because by mimicking the natural infection they deliver a complete spectrum of antigens to the antigen-presenting cells, which in principle leads to a better immune response and better protection than a subunit vaccine. Avirulent organisms can be generated by a defined genetic alteration, which eliminates the risk of the parasite reverting to the virulent phenotype.",
    "لأنها بمحاكاتها العدوى الطبيعية توصل طيفًا كاملًا من المستضدات إلى الخلايا العارضة للمستضد، ممّا يؤدّي مبدئيًا إلى استجابة مناعية أفضل وحماية أفضل من لقاح الوحدات الفرعية. ويمكن توليد أحياء غير ضارية بتغيير وراثي محدّد يزيل خطر رجوع الطفيلي إلى النمط الظاهري الضاري."),
 IM("List the properties of an ideal vaccine.", "عدّد صفات اللقاح المثالي.",
    "BIOS answer (the week's text does not list them): safe — does not cause the disease or serious side effects; effective (immunogenic) — strong protection in most vaccinated people; long-lasting — immunological memory with few or no boosters; broadly protective — covers the species and strains of the area; stable and cheap — easy transport and storage in poor endemic areas; easy to give — few doses and a simple route; and easy to distinguish from natural infection in the laboratory.",
    "جواب BIOS (نصّ الأسبوع لا يعدّدها): آمن — لا يسبّب المرض ولا آثارًا جانبية خطيرة؛ وفعّال (محفّز للمناعة) — حماية قوية لمعظم الملقَّحين؛ وطويل الأمد — ذاكرة مناعية بجرعات معزّزة قليلة أو بلا؛ وواسع الحماية — يغطّي أنواع المنطقة وسلالاتها؛ وثابت ورخيص — سهل النقل والخزن في المناطق المتوطّنة الفقيرة؛ وسهل الإعطاء — جرعات قليلة وطريق بسيط؛ ويسهل تمييزه عن العدوى الطبيعية في المختبر."),
]

meta = dict(subject_en="Diagnostic Parasitology", subject_ar="الطفيليات التشخيصية", short_ar="طفيليات", instructor="أ.د. نزار الخفاجي",
            unit_en="Week 9", unit_ar="الأسبوع 9", unit_label="WEEK", unit_no="9",
            title_en="Genus Leishmania: Properties of ideal vaccines & Leishmania vaccine in trial",
            title_ar="جنس الليشمانيا: صفات اللقاح المثالي ولقاح الليشمانيا قيد التجربة",
            department="قسم التحليلات", stage="The fourth stage — الرابعة", kind="Theory — نظري")
os.makedirs(f"/home/user/-/{FOLDER}", exist_ok=True)
shutil.copy(f"{SRC}/source-transcript.txt", f"/home/user/-/{FOLDER}/source-transcript.txt")
blocks, mcq, tf, traps, important = ltr_all(blocks), ltr_all(mcq), ltr_all(tf), ltr_all(traps), ltr_all(important)
save(FOLDER, meta, blocks, mcq, tf, traps, important)
fit(FOLDER, min_gap=0.08)

```
