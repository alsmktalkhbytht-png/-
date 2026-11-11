import sys, os, shutil, re; sys.path.insert(0, "/tmp/claude-0/-home-user-kwmdkm/44452a28-19bf-5ce8-890a-f6919e775f0b/scratchpad/imm456")
from ci import *            # c helpers + B INSHORT TERMS balance save(split.fix)
sys.path.insert(0, "/tmp/claude-0/-home-user-kwmdkm/44452a28-19bf-5ce8-890a-f6919e775f0b/scratchpad"); from bidi import ltr_all; from flowfit import fit
import split; split.ABBR += ("i. e.", "e.g.,")   # "( i. e. no free – living)" is not a sentence end

# Diagnostic Parasitology (theory, stage 4, Prof. Dr. Nizar Al-Khafaji) — week 10: phylum Apicomplexa, main properties
# of the group, ultrastructure of the apical complex. Source: text pasted by the user (no figures, no questions).
# The second half of the file REPEATS the general characters and life-cycle paragraphs with small wording changes —
# kept as in the file, with a BIOS note. Ends with "First term examination". Stage 4 → wineoat + separate question file.
def _q(a):
    f = lambda x: re.sub(r"“([^”]*[A-Za-z][^”]*)”", lambda m: "`“" + m.group(1).replace("**", "") + "”`", x)
    return [f(x) for x in a] if isinstance(a, list) else f(a)
BN = lambda en, ar: N(en, _q(ar), label=["BIOS note", "ملاحظة BIOS"])
BX = lambda en, ar: N(en, ar, label=["BIOS explanation", "شرح BIOS"])
O = P
FOLDER = "parasitology-week10-theory"
SRC = "/tmp/claude-0/-home-user-kwmdkm/44452a28-19bf-5ce8-890a-f6919e775f0b/scratchpad/par10"
def G(te, ta, en, ar): return dict(t="group", title_en=te, title_ar=ta, en=en, ar=ar, style="light")
def TERMS6(terms, n=6):
    head = [B("Term", "المصطلح"), "الترجمات العربية المستعملة"]
    return [SEC("Key terms", "أهم المصطلحات")] + [T(head, [[f"**{e}**", a] for e, a in terms[i:i + n]], ar_cols=[1], widths=[36, 64])
                                                  for i in range(0, len(terms), n)]
AP = "المعقّدات القمّية"; AL = "للمعقّدات القمّية"

blocks = [
 # ───────────────────────── 0 contents & summary
 SEC("Contents of the week", "محتويات الأسبوع"),
 C("**10th Week**", "**الأسبوع العاشر**"),
 C("**Phylum Apicomplexa; Main properties of the group; Ultrastructure of the apical complex**",
   f"**شعبة {AP} (`Apicomplexa`)؛ الصفات الرئيسية للمجموعة؛ البنية الدقيقة للمعقّد القمّي**"),
 C("Apicomplexa are characterized by their **distinctive apical complex for host cell invasion**, a **relict non- photosynthetic plastid called an apicoplast for survival**, **complex life cycles involving sexual and asexual reproduction**, and **gliding motility for movement**.",
   f"تتميّز {AP} **بمعقّدها القمّي المميّز لغزو خلية المضيف**، و**بلاستيدة أثرية غير قادرة على التمثيل الضوئي تُسمّى البلاستيدة القمّية للبقاء**، و**دورات حياة معقّدة فيها تكاثر جنسي ولا جنسي**، و**الحركة الانزلاقية للتنقّل**."),
 C("Most are **obligate parasites of animals**, **lack external locomotion like flagella or pseudopods**, and include **well- known pathogens like Plasmodium Malaria and Toxoplasma**",
   "ومعظمها **طفيليات إجبارية للحيوانات**، و**تفتقر إلى أعضاء حركة خارجية كالأسواط أو الأقدام الكاذبة**، وتضمّ **ممرضات معروفة مثل المتصوّرة (الملاريا) والمقوّسة**"),
 BN("“Plasmodium Malaria” — **Plasmodium** is the genus and **malaria** is the disease it causes: *Plasmodium* spp. (malaria) and *Toxoplasma gondii*.",
    "“Plasmodium Malaria” — **المتصوّرة (`Plasmodium`)** اسم الجنس و**الملاريا** هي المرض الذي تسبّبه: أنواع المتصوّرة (الملاريا)، والمقوّسة الغوندية (`Toxoplasma gondii`)."),

 # ───────────────────────── 1 key properties
 SEC("Key properties", "الصفات الرئيسية"),
 G("Apical complex:", "المعقّد القمّي:", "A **specialized structure at the cell's anterior end** that includes **secretory organelles (micronemes, rhoptries)** and **cytoskeletal elements**, which **secrete enzymes needed to penetrate and invade host cells**",
   "**تركيب متخصّص في النهاية الأمامية للخلية** يضمّ **عُضيّات إفرازية (الميكرونيمات والروبتريات)** و**عناصر هيكلية خلوية**، **تفرز الإنزيمات اللازمة لاختراق خلايا المضيف وغزوها**"),
 G("Apicoplast:", "البلاستيدة القمّية:", "A **relict, non- photosynthetic organelle derived from a red alga via secondary endosymbiosis**, it is **essential for the apicomplexan's survival**",
   "**عُضيّة أثرية غير قادرة على التمثيل الضوئي، مشتقّة من طحلب أحمر بالتعايش الداخلي الثانوي**، وهي **أساسية لبقاء الطفيلي القمّي**"),
 G("Gliding motility:", "الحركة الانزلاقية:", "Apicomplexan use a **unique form of locomotion called gliding motility** to **move across surfaces and locate hosts**, as they **lack flagella or pseudopods in their active stages**",
   "تستعمل {0} **شكلًا فريدًا من الحركة يُسمّى الحركة الانزلاقية** **للتنقّل على الأسطح وإيجاد المضيفات**، لأنها **تفتقر إلى الأسواط أو الأقدام الكاذبة في أطوارها النشطة**".format(AP)),
 G("Parasitism", "التطفّل", "Most apicomplexans are **obligate endoparasites of animals**, meaning they **must live inside a host to survive**.",
   f"معظم {AP} **طفيليات داخلية إجبارية للحيوانات**، أي **يجب أن تعيش داخل مضيف لتبقى حيّة**."),
 G("Complex life cycles", "دورات الحياة المعقّدة", "They often have **intricate life cycles** with different stages of **asexual (e.g., schizogony)** and **sexual reproduction (gametogony)**, as well as **spore formation (Sporogony)**.",
   "لها غالبًا **دورات حياة متشابكة** بأطوار مختلفة من **التكاثر اللاجنسي (مثل الانقسام المتعدّد)** و**التكاثر الجنسي (التكوّن العرسي)**، إضافةً إلى **تكوين الأبواغ (التبوّغ)**."),
 G("Microscopic structure", "البنية المجهرية", "Apicomplexans are **unicellular, eukaryotic organisms**", f"{AP} كائنات **وحيدة الخلية حقيقية النواة**"),
 G("Absence of motile appendages KL:", "غياب الزوائد الحركية:", "In most stages, they **do not possess external structures like cilia, or flagellum** which are **only found in certain gamete stages**",
   "في معظم الأطوار **لا تملك تراكيب خارجية مثل الأهداب أو السوط**، وهي **لا توجد إلا في أطوار عرسية معيّنة**"),
 BN(["“**KL**” after “Absence of motile appendages” is a **stray typing slip** in the file — it has no meaning here.",
     "“Apicomplexan use” = apicomplexan**s** use."],
    ["“**KL**” بعد “Absence of motile appendages” **زلّة طباعية** في الملف — لا معنى لها هنا.",
     "و“Apicomplexan use” صحيحها apicomplexan**s** use."]),
 T([B("Property", "الصفة"), B("What it means", "ما المقصود")],
   [[B("**Apical complex**", "**المعقّد القمّي**"), B("organelles at the anterior end; secrete enzymes to invade the host cell", "عُضيّات في النهاية الأمامية؛ تفرز إنزيمات لغزو خلية المضيف")],
    [B("**Apicoplast**", "**البلاستيدة القمّية**"), B("relict plastid from a red alga; no photosynthesis; essential for survival", "بلاستيدة أثرية من طحلب أحمر؛ لا تمثيل ضوئي؛ أساسية للبقاء")],
    [B("**Gliding motility**", "**الحركة الانزلاقية**"), B("unique locomotion — no flagella or pseudopods in active stages", "حركة فريدة — بلا أسواط ولا أقدام كاذبة في الأطوار النشطة")],
    [B("**Parasitism**", "**التطفّل**"), B("obligate endoparasites of animals", "طفيليات داخلية إجبارية للحيوانات")],
    [B("**Life cycle**", "**دورة الحياة**"), B("asexual (schizogony) + sexual (gametogony) + spore formation (sporogony)", "لا جنسي (انقسام متعدّد) + جنسي (تكوّن عرسي) + تبوّغ")],
    [B("**Structure**", "**البنية**"), B("unicellular eukaryotes; cilia/flagella only in certain gamete stages", "وحيدة الخلية حقيقية النواة؛ الأهداب/الأسواط في أطوار عرسية فقط")]],
   key_cols=[0], widths=[26, 74], style="summary", label_en="BIOS — key properties at a glance", label_ar="BIOS — الصفات الرئيسية بلمحة"),
 BX("The **apicoplast** no longer makes food (it lost photosynthesis) but still carries out **fatty-acid, isoprenoid and haem synthesis** — and because it came from a plant-like ancestor it is a **drug target** absent from human cells.",
    "**البلاستيدة القمّية** لم تعد تصنع الغذاء (فقدت التمثيل الضوئي) لكنها ما تزال تقوم **ببناء الأحماض الدهنية والآيزوبرينويدات والهيم** — ولأنها جاءت من سلف نباتي فهي **هدف دوائي** غير موجود في خلايا الإنسان."),
 INSHORT([("Four marks of the group: **apical complex**, **apicoplast**, **complex life cycles**, **gliding motility**.",
           f"أربع علامات للمجموعة: **المعقّد القمّي**، و**البلاستيدة القمّية**، و**دورات الحياة المعقّدة**، و**الحركة الانزلاقية**."),
          ("All are **unicellular eukaryotes** and **obligate endoparasites**; **no flagella or pseudopods**.",
           "كلّها **وحيدة الخلية حقيقية النواة** و**طفيليات داخلية إجبارية**؛ **بلا أسواط ولا أقدام كاذبة**."),
          ("Famous members: **Plasmodium** (malaria) and **Toxoplasma**.", "من أشهرها: **المتصوّرة** (الملاريا) و**المقوّسة**.")]),

 # ───────────────────────── 2 the name sporozoa
 SEC("The name Sporozoa", "اسم البوغيات"),
 C(["**Formerly the Apicomplexa were part of a group called sporozoa** and this name is **still sometimes used**.",
    "**Recently there have been some suggestions to revert back to the name sporozoa.**",
    "Apicomplexa part of a group called sporozoan."],
   [f"**كانت {AP} سابقًا جزءًا من مجموعة تُسمّى البوغيات (`Sporozoa`)**، وما زال هذا الاسم **يُستعمل أحيانًا**.",
    "**وظهرت حديثًا اقتراحات بالعودة إلى اسم البوغيات.**",
    "والمعقّدات القمّية جزء من مجموعة تُسمّى البوغيات."]),
 BN("The last line (“Apicomplexa part of a group called sporozoan”) is **incomplete** and repeats the first — it should read: Apicomplexa **were** part of a group called **sporozoa**.",
    "السطر الأخير (“Apicomplexa part of a group called sporozoan”) **ناقص** ومكرّر للأول — وصوابه: Apicomplexa **were** part of a group called **sporozoa**."),
 BX("The old name **Sporozoa** came from the **spores (oocysts)** these parasites form; the modern name **Apicomplexa** comes from the **apical complex**.",
    "جاء الاسم القديم **البوغيات** من **الأبواغ (الأكياس البيضية)** التي تكوّنها هذه الطفيليات؛ والاسم الحديث **المعقّدات القمّية** مأخوذ من **المعقّد القمّي**."),

 # ───────────────────────── 3 general characters
 SEC("General characters of Apicomplexa", f"الصفات العامة {AL}"),
 C("The Apicomplexa are a **monophyletic group** composed **almost entirely of parasitic ( i. e. no free – living) species**.",
   f"{AP} **مجموعة وحيدة النشأة (`monophyletic`)** مؤلَّفة **كلّها تقريبًا من أنواع طفيلية (أي لا توجد أنواع حرّة المعيشة)**."),
 C("The parasite belonging to this group of protozoa **don’t possess any type of locomotion organelles**, they show **slight amoeboid change of form (body flexion)**.",
   "الطفيليات التي تنتمي إلى هذه المجموعة من الأوالي **لا تملك أيّ نوع من عُضيّات الحركة**، وتُظهر **تغيّرًا أميبيًا طفيفًا في الشكل (انثناء الجسم)**."),
 BN("“monophyletic” = all the members **descend from one common ancestor**; “The parasite … don’t” = the parasite**s** … don’t.",
    "“monophyletic” أي أن كل أفراد المجموعة **تنحدر من سلف مشترك واحد**؛ و“The parasite … don’t” صحيحها parasite**s**."),
 C("**Electron microscopy revealed unique ultrastructural features** among the various sporozoan which were subsequently **used to redefine the groups**.",
   "**كشف المجهر الإلكتروني صفات بنيوية دقيقة فريدة** بين البوغيات المختلفة، واستُعملت بعد ذلك **لإعادة تعريف المجموعات**."),
 H2("Ultrastructure of the apical complex", "البنية الدقيقة للمعقّد القمّي"),
 C("**A defining characteristic of the Apicomplexa is a group of organelles found at one end – called the apical end – of the organism.**",
   f"**الصفة المميّزة {AL} مجموعة من العُضيّات توجد في طرف واحد من الكائن — يُسمّى الطرف القمّي.**"),
 C("This **apical complex** includes **secretory organelles known as micronemes and rhoptries**, **polar ring composed of microtubules**, and in some species **a conoid which lies within the polar rings**.",
   "ويضمّ هذا **المعقّد القمّي** **عُضيّات إفرازية تُعرف بالميكرونيمات والروبتريات**، و**حلقة قطبية مؤلَّفة من أنيبيبات دقيقة**، وفي بعض الأنواع **مخروطًا (`conoid`) يقع داخل الحلقات القطبية**."),
 T([B("Structure", "التركيب"), B("What it is / does", "ما هو ووظيفته")],
   [[B("**Micronemes**", "**الميكرونيمات**"), B("secretory organelles — first secretions: attachment to the host cell and gliding", "عُضيّات إفرازية — أول الإفرازات: الالتصاق بخلية المضيف والانزلاق")],
    [B("**Rhoptries**", "**الروبتريات**"), B("secretory organelles — enzymes and proteins for penetration and the parasitophorous vacuole", "عُضيّات إفرازية — إنزيمات وبروتينات للاختراق وتكوين الفجوة الطفيلية")],
    [B("**Polar ring(s)**", "**الحلقة (الحلقات) القطبية**"), B("composed of microtubules — the organizing centre of the apical cytoskeleton", "مؤلَّفة من أنيبيبات دقيقة — مركز تنظيم الهيكل الخلوي القمّي")],
    [B("**Conoid**", "**المخروط**"), B("in some species only — a cone of spiral fibres lying within the polar rings", "في بعض الأنواع فقط — مخروط من ألياف حلزونية يقع داخل الحلقات القطبية")]],
   key_cols=[0], widths=[26, 74], style="summary", label_en="BIOS — the apical complex", label_ar="BIOS — المعقّد القمّي"),
 BN("The file says “**polar ring** composed of microtubules” (singular) in one paragraph and “**polar rings**” in the other — both describe the same structure; most species have **one or two polar rings**.",
    "يقول الملف “**polar ring** composed of microtubules” بالمفرد في فقرة و“**polar rings**” بالجمع في الأخرى — وكلاهما التركيب نفسه؛ ولمعظم الأنواع **حلقة أو حلقتان قطبيتان**."),
 BX("**Toxoplasma** and the coccidia **have a conoid** (they are “conoid-bearing”), while **Plasmodium** has no conoid in its invasive blood stages — this is why the file says “**in some species**”.",
    "**المقوّسة** والأكريات **لها مخروط** (حاملة للمخروط)، أما **المتصوّرة** فلا مخروط في أطوارها الغازية الدموية — ولهذا يقول الملف “**في بعض الأنواع**”."),
 INSHORT([("Apicomplexa = **monophyletic**, almost all **parasitic** (no free-living), **no locomotion organelles** — only slight **body flexion**.",
           f"{AP} = **وحيدة النشأة**، كلّها تقريبًا **طفيلية** (لا حرّة المعيشة)، **بلا عُضيّات حركة** — فقط **انثناء الجسم** الطفيف."),
          ("**Electron microscopy** revealed the ultrastructure that redefined the groups.", "**المجهر الإلكتروني** كشف البنية الدقيقة التي أُعيد بها تعريف المجموعات."),
          ("Apical complex = **micronemes + rhoptries + polar ring(s) of microtubules** (+ a **conoid** in some species).",
           "المعقّد القمّي = **ميكرونيمات + روبتريات + حلقة (حلقات) قطبية من أنيبيبات دقيقة** (+ **مخروط** في بعض الأنواع).")]),

 # ───────────────────────── 4 life cycle
 SEC("The life cycle", "دورة الحياة"),
 C("The Apicomplexa have **complex life cycle that are characterized by three distinct processes, sporogony, merogony and gametogony (alternation of generation)**. **May be classified into two processes schizogony and gametogony**",
   f"{AL} **دورات حياة معقّدة تتميّز بثلاث عمليات متمايزة: التبوّغ (`sporogony`) والتقسّم (`merogony`) والتكوّن العرسي (`gametogony`) (تعاقب الأجيال)**. **وقد تُصنَّف إلى عمليتين: الانقسام المتعدّد (`schizogony`) والتكوّن العرسي**"),
 C("**Sporogony is an asexual reproduction that culminates in the production of sporozoites.** Sporozoites will develop into forms that undergo **another asexual replication known as merogony**. **Merogony and the resulting merozoites are known by many different names depending on the species.**",
   "**التبوّغ تكاثر لا جنسي ينتهي بإنتاج البويغات (`sporozoites`).** وتتطوّر البويغات إلى أشكال تمرّ **بتكاثر لا جنسي آخر يُعرف بالتقسّم**. **والتقسّم والأقسومات (`merozoites`) الناتجة عنه تُعرف بأسماء مختلفة كثيرة بحسب النوع.**"),
 C("Similarly, **sporogony and gametogony can involve different hosts or cell types.** **As an alternative to asexual replication merozoites can become gametes through a process variously called gametogony, or gametogenesis.**",
   "وكذلك **قد يشترك في التبوّغ والتكوّن العرسي مضيفات مختلفة أو أنواع خلايا مختلفة.** **وبدلًا من التكاثر اللاجنسي يمكن أن تتحوّل الأقسومات إلى أعراس (`gametes`) بعملية تُسمّى التكوّن العرسي أو التولّد العرسي.**"),
 C("**As in other types of sexual reproduction, the gametes fuse to form a zygote which differentiates into a form yielding sporozoites.**",
   "**وكما في أنواع التكاثر الجنسي الأخرى، تندمج الأعراس مكوّنةً لاقحة (`zygote`) تتمايز إلى شكل يُنتج البويغات.**"),
 FLOW([("Sporozoites (from sporogony)", "البويغات (من التبوّغ)"), ("Merogony → merozoites", "التقسّم ← أقسومات"),
       ("Gametogony → gametes", "التكوّن العرسي ← أعراس"), ("Fusion → zygote", "الاندماج ← لاقحة"), ("Sporogony → sporozoites again", "التبوّغ ← بويغات من جديد")],
      en="BIOS — the cycle in one line", ar="BIOS — الدورة بسطر واحد"),
 T([B("Process", "العملية"), B("Type", "النوع"), B("Product", "الناتج")],
   [[B("**Sporogony**", "**التبوّغ**"), B("asexual", "لا جنسي"), B("sporozoites", "البويغات")],
    [B("**Merogony (schizogony)**", "**التقسّم (الانقسام المتعدّد)**"), B("asexual", "لا جنسي"), B("merozoites", "الأقسومات")],
    [B("**Gametogony (gametogenesis)**", "**التكوّن العرسي**"), B("sexual", "جنسي"), B("gametes → zygote", "الأعراس ← اللاقحة")]],
   key_cols=[0], widths=[36, 24, 40], style="summary", label_en="BIOS — the three processes", label_ar="BIOS — العمليات الثلاث"),
 BX("**Merogony and schizogony are the same process** under two names (the dividing stage is the **meront** or **schizont**) — that is why the file says the cycle may be described as **three processes** (sporogony, merogony, gametogony) or as **two** (schizogony and gametogony).",
    "**التقسّم والانقسام المتعدّد عملية واحدة** باسمين (والطور المنقسم يُسمّى `meront` أو `schizont`) — ولهذا يقول الملف إن الدورة قد تُوصف **بثلاث عمليات** (التبوّغ والتقسّم والتكوّن العرسي) أو **بعمليتين** (الانقسام المتعدّد والتكوّن العرسي)."),
 BN("“complex life cycle that are” = complex life **cycles** that are; and the **two-process** classification does not contradict the **three-process** one — see the explanation above.",
    "“complex life cycle that are” صحيحها complex life **cycles**؛ وتصنيف **العمليتين** لا يناقض تصنيف **العمليات الثلاث** — انظر الشرح أعلاه."),
 INSHORT([("**Sporogony** → sporozoites (asexual) · **merogony/schizogony** → merozoites (asexual) · **gametogony** → gametes (sexual).",
           "**التبوّغ** ← بويغات (لا جنسي) · **التقسّم/الانقسام المتعدّد** ← أقسومات (لا جنسي) · **التكوّن العرسي** ← أعراس (جنسي)."),
          ("Gametes **fuse → zygote → sporozoites** again (alternation of generation); the processes may involve **different hosts or cell types**.",
           "تندمج الأعراس ← **لاقحة ← بويغات** من جديد (تعاقب الأجيال)؛ وقد تشترك في العمليات **مضيفات أو خلايا مختلفة**.")]),

 # ───────────────────────── 5 the repeated section
 SEC("Size of the group (repeated section)", "حجم المجموعة (القسم المكرّر)"),
 C("The Apicomplexa are an **extremely large and diverse group (> 5000 named species)**",
   f"{AP} **مجموعة كبيرة جدًا ومتنوّعة (أكثر من 5000 نوع مسمّى)**"),
 BN(["From here to the end, the file **repeats the paragraphs of the general characters and the life cycle** with small wording changes — they are kept as in the file.",
     "Differences in the repeat: “at one **–** end”, the unclosed quotation mark in “This ‘ apical complex”, “polar **rings**” (plural), “depending **of** the species”, “gametogony, **gametogony** or gametogenesis” (the word twice) and “differentiates into **as** form” (should be **a** form)."],
    ["من هنا إلى النهاية **يكرّر الملف فقرات الصفات العامة ودورة الحياة** بتغييرات لفظية بسيطة — وأُبقيت كما في الملف.",
     "والفروق في التكرار: “at one **–** end”، وعلامة اقتباس غير مغلقة في “This ‘ apical complex”، و“polar **rings**” بالجمع، و“depending **of** the species” (الصواب on)، و“gametogony, **gametogony** or gametogenesis” (الكلمة مرّتين)، و“differentiates into **as** form” (الصواب **a** form)."]),
 C("A defining characteristic of the Apicomplexa is a group of organelles found at one – end – called the apical end – of the organism. This ‘ apical complex includes secretory organelles known as micronemes and rhoptries, **polar rings** composed of microtubules, and in some species a conoid which lies within the polar rings.",
   f"الصفة المميّزة {AL} مجموعة من العُضيّات توجد في طرف واحد من الكائن — يُسمّى الطرف القمّي. ويضمّ هذا المعقّد القمّي عُضيّات إفرازية تُعرف بالميكرونيمات والروبتريات، و**حلقات قطبية** مؤلَّفة من أنيبيبات دقيقة، وفي بعض الأنواع مخروطًا يقع داخل الحلقات القطبية."),
 C("The Apicomplexa have complex life cycles that are characterized by three distinct processes, sporogony, merogony and gametogony (alternation of generation). **Also, may be classified into two processes schizogony and gametogony.**",
   f"{AL} دورات حياة معقّدة تتميّز بثلاث عمليات متمايزة: التبوّغ والتقسّم والتكوّن العرسي (تعاقب الأجيال). **وقد تُصنَّف أيضًا إلى عمليتين: الانقسام المتعدّد والتكوّن العرسي.**"),
 C("Sporogony is an asexual reproduction that culminates in the production of sporozoites. Sporozoites will develop into forms that undergo another asexual replication known as merogony. Merogony and the resulting merozoites are known by many different names **depending of the species**.",
   "التبوّغ تكاثر لا جنسي ينتهي بإنتاج البويغات. وتتطوّر البويغات إلى أشكال تمرّ بتكاثر لا جنسي آخر يُعرف بالتقسّم. والتقسّم والأقسومات الناتجة عنه تُعرف بأسماء مختلفة كثيرة **بحسب النوع**."),
 C("Similarly, sporogony and gametogony can involve different hosts or cell types. As an alternative to asexual replication merozoites can become gametes through a process variously called **gametogony, gametogony or gametogenesis**. As in other types of sexual reproduction, the gametes fuse to form a zygote which differentiates into **as form** yielding sporozoites.",
   "وكذلك قد يشترك في التبوّغ والتكوّن العرسي مضيفات مختلفة أو أنواع خلايا مختلفة. وبدلًا من التكاثر اللاجنسي يمكن أن تتحوّل الأقسومات إلى أعراس بعملية تُسمّى **التكوّن العرسي أو التولّد العرسي**. وكما في أنواع التكاثر الجنسي الأخرى، تندمج الأعراس مكوّنةً لاقحة تتمايز إلى **شكل** يُنتج البويغات."),
 C("**First term examination**", "**امتحان الفصل الأول**"),
 BN("The week ends with the line “**First term examination**” — the lecture material of the first term stops here.",
    "ينتهي الأسبوع بسطر “**First term examination**” أي **امتحان الفصل الأول** — فمادة الفصل الأول تقف هنا."),
 INSHORT([("The group has **more than 5000 named species**.", "في المجموعة **أكثر من 5000 نوع مسمّى**."),
          ("The last part of the file **repeats** the general characters and the life cycle, then ends with **“First term examination”**.",
           "الجزء الأخير من الملف **يكرّر** الصفات العامة ودورة الحياة، ثم ينتهي بـ**“امتحان الفصل الأول”**.")]),
] + TERMS6([
 ("Apicomplexa", "المعقّدات القمّية / القميّات المعقّدة"),
 ("Sporozoa", "البوغيات / الأوالي البوغية"),
 ("Apical complex", "المعقّد القمّي"),
 ("Apical end", "الطرف القمّي / النهاية الأمامية"),
 ("Micronemes", "الميكرونيمات / الخييطات الدقيقة"),
 ("Rhoptries", "الروبتريات / الهُرَيّات"),
 ("Polar ring", "الحلقة القطبية"),
 ("Conoid", "المخروط / الجسم المخروطي"),
 ("Microtubules", "الأنيبيبات الدقيقة"),
 ("Apicoplast", "البلاستيدة القمّية"),
 ("Secondary endosymbiosis", "التعايش الداخلي الثانوي"),
 ("Gliding motility", "الحركة الانزلاقية"),
 ("Obligate endoparasite", "طفيلي داخلي إجباري"),
 ("Monophyletic group", "مجموعة وحيدة النشأة / أحادية الأصل"),
 ("Body flexion", "انثناء الجسم"),
 ("Sporogony", "التبوّغ / التكاثر البوغي"),
 ("Sporozoite", "البويغة / الطور البوغي"),
 ("Merogony", "التقسّم"),
 ("Merozoite", "الأقسومة / القسيم"),
 ("Schizogony", "الانقسام المتعدّد / التكاثر الانشطاري"),
 ("Gametogony / gametogenesis", "التكوّن العرسي / التولّد العرسي"),
 ("Gamete", "العُرس / الخلية الجنسية"),
 ("Zygote", "اللاقحة / البيضة الملقّحة"),
 ("Alternation of generation", "تعاقب الأجيال"),
])

# ───────────────────────── questions (BIOS — the file has none)
mcq = [
 {"topic_en": "Main properties of the group", "topic_ar": "الصفات الرئيسية للمجموعة"},
 Q("The defining characteristic of the phylum Apicomplexa is the:", "الصفة المميّزة لشعبة المعقّدات القمّية هي:", O(("Apical complex at one end of the organism", "المعقّد القمّي في طرف الكائن"), ("Undulating membrane", "الغشاء المتموّج"), ("Adhesive disc", "القرص اللاصق"), ("Pair of flagella", "زوج الأسواط")), "a"),
 Q("The apical complex is found at the:", "يوجد المعقّد القمّي في:", O(("Posterior end", "النهاية الخلفية"), ("Anterior (apical) end", "النهاية الأمامية (القمّية)"), ("Nucleus", "النواة"), ("Cell membrane all around", "الغشاء الخلوي كلّه")), "b"),
 Q("The secretory organelles of the apical complex are the:", "العُضيّات الإفرازية في المعقّد القمّي هي:", O(("Ribosomes and lysosomes", "الرايبوسومات والجسيمات الحالّة"), ("Mitochondria", "المتقدّرات"), ("Micronemes and rhoptries", "الميكرونيمات والروبتريات"), ("Golgi bodies", "أجسام غولجي")), "c"),
 Q("The polar ring of the apical complex is composed of:", "تتألّف الحلقة القطبية في المعقّد القمّي من:", O(("Chitin", "الكايتين"), ("Peptidoglycan", "الببتيدوغلايكان"), ("Lipid droplets", "قطرات دهنية"), ("Microtubules", "أنيبيبات دقيقة")), "d"),
 Q("The conoid of the apical complex:", "المخروط في المعقّد القمّي:", O(("Is present in some species, within the polar rings", "موجود في بعض الأنواع، داخل الحلقات القطبية"), ("Is present in all species", "موجود في كل الأنواع"), ("Lies in the posterior end", "يقع في النهاية الخلفية"), ("Is a secretory organelle", "عُضيّة إفرازية")), "a"),
 Q("The function of the apical complex is to:", "وظيفة المعقّد القمّي:", O(("Store food", "خزن الغذاء"), ("Secrete enzymes to penetrate and invade host cells", "إفراز إنزيمات لاختراق خلايا المضيف وغزوها"), ("Carry out photosynthesis", "القيام بالتمثيل الضوئي"), ("Produce flagella", "إنتاج الأسواط")), "b"),
 Q("The apicoplast is:", "البلاستيدة القمّية:", O(("A photosynthetic chloroplast", "بلاستيدة خضراء قادرة على التمثيل الضوئي"), ("A secretory organelle", "عُضيّة إفرازية"), ("A relict non-photosynthetic plastid derived from a red alga", "بلاستيدة أثرية غير قادرة على التمثيل الضوئي مشتقّة من طحلب أحمر"), ("A type of nucleus", "نوع من النوى")), "c"),
 Q("The apicoplast was acquired by:", "اكتُسبت البلاستيدة القمّية بـ:", O(("Binary fission", "الانشطار الثنائي"), ("Conjugation", "الاقتران"), ("Phagocytosis of bacteria only", "بلعمة البكتيريا فقط"), ("Secondary endosymbiosis", "التعايش الداخلي الثانوي")), "d"),
 Q("Apicomplexans move by:", "تتحرّك المعقّدات القمّية بـ:", O(("Gliding motility", "الحركة الانزلاقية"), ("Flagella", "الأسواط"), ("Pseudopods", "الأقدام الكاذبة"), ("Cilia", "الأهداب")), "a"),
 Q("Cilia or flagella in Apicomplexa are found:", "توجد الأهداب أو الأسواط في المعقّدات القمّية:", O(("In all stages", "في كل الأطوار"), ("Only in certain gamete stages", "في أطوار عرسية معيّنة فقط"), ("Only in the sporozoite", "في البويغة فقط"), ("Never at all", "أبدًا")), "b"),
 Q("Most apicomplexans are:", "معظم المعقّدات القمّية:", O(("Free-living", "حرّة المعيشة"), ("Ectoparasites", "طفيليات خارجية"), ("Obligate endoparasites of animals", "طفيليات داخلية إجبارية للحيوانات"), ("Plant parasites", "طفيليات نباتية")), "c"),
 Q("Apicomplexans are:", "المعقّدات القمّية:", O(("Multicellular prokaryotes", "متعدّدة الخلايا بدائية النواة"), ("Multicellular eukaryotes", "متعدّدة الخلايا حقيقية النواة"), ("Unicellular prokaryotes", "وحيدة الخلية بدائية النواة"), ("Unicellular eukaryotes", "وحيدة الخلية حقيقية النواة")), "d"),
 Q("Well-known pathogens of this phylum include:", "من ممرضات هذه الشعبة المعروفة:", O(("Plasmodium (malaria) and Toxoplasma", "المتصوّرة (الملاريا) والمقوّسة"), ("Giardia and Trichomonas", "الجيارديا والمشعّرة"), ("Leishmania and Trypanosoma", "الليشمانيا والمثقّبة"), ("Entamoeba and Naegleria", "المتحوّلة والنيغلرية")), "a"),
 {"topic_en": "General characters and the name", "topic_ar": "الصفات العامة والاسم"},
 Q("The former name of the Apicomplexa was:", "الاسم السابق للمعقّدات القمّية:", O(("Mastigophora", "السوطيات"), ("Sporozoa", "البوغيات"), ("Sarcodina", "اللحميات"), ("Ciliophora", "الهدبيات")), "b"),
 Q("The Apicomplexa are described as a monophyletic group, which means:", "توصف المعقّدات القمّية بأنها مجموعة وحيدة النشأة، أي:", O(("They have many different ancestors", "لها أسلاف كثيرة مختلفة"), ("They are all free-living", "كلّها حرّة المعيشة"), ("All members descend from one common ancestor", "كل أفرادها تنحدر من سلف مشترك واحد"), ("They reproduce only sexually", "تتكاثر جنسيًا فقط")), "c"),
 Q("The species of this group are:", "أنواع هذه المجموعة:", O(("Mostly free-living", "حرّة المعيشة غالبًا"), ("Half parasitic, half free-living", "نصفها طفيلي ونصفها حرّ"), ("All photosynthetic", "كلّها ذاتية التغذية ضوئيًا"), ("Almost entirely parasitic, with no free-living forms", "كلّها تقريبًا طفيلية، بلا أشكال حرّة المعيشة")), "d"),
 Q("The only movement shown by the parasites of this group (lacking locomotion organelles) is:", "الحركة الوحيدة التي تُظهرها طفيليات هذه المجموعة (لافتقارها إلى عُضيّات الحركة):", O(("Slight amoeboid change of form (body flexion)", "تغيّر أميبي طفيف في الشكل (انثناء الجسم)"), ("Falling-leaf motion", "حركة سقوط الورقة"), ("Jerky rotatory motility", "حركة متقطّعة دوّارة"), ("Swimming by cilia", "السباحة بالأهداب")), "a"),
 Q("The unique ultrastructural features used to redefine the groups were revealed by:", "كُشفت الصفات البنيوية الدقيقة الفريدة التي أُعيد بها تعريف المجموعات بوساطة:", O(("Light microscopy", "المجهر الضوئي"), ("Electron microscopy", "المجهر الإلكتروني"), ("Serology", "المصليات"), ("Culture", "الزرع")), "b"),
 Q("The Apicomplexa include approximately:", "تضمّ المعقّدات القمّية نحو:", O(("50 named species", "50 نوعًا مسمّى"), ("500 named species", "500 نوع مسمّى"), ("More than 5000 named species", "أكثر من 5000 نوع مسمّى"), ("Exactly 100 species", "100 نوع بالضبط")), "c"),
 {"topic_en": "The life cycle", "topic_ar": "دورة الحياة"},
 Q("The three distinct processes of the apicomplexan life cycle are:", "العمليات الثلاث المتمايزة في دورة حياة المعقّدات القمّية:", O(("Mitosis, meiosis and binary fission", "الانقسام الخيطي والاختزالي والانشطار الثنائي"), ("Encystation, excystation and division", "التكيّس والانفلات والانقسام"), ("Budding, conjugation and sporulation", "التبرعم والاقتران والتبوّغ"), ("Sporogony, merogony and gametogony", "التبوّغ والتقسّم والتكوّن العرسي")), "d"),
 Q("Sporogony is an asexual reproduction that culminates in the production of:", "التبوّغ تكاثر لا جنسي ينتهي بإنتاج:", O(("Sporozoites", "البويغات"), ("Merozoites", "الأقسومات"), ("Gametes", "الأعراس"), ("Zygotes", "اللواقح")), "a"),
 Q("Merogony produces:", "ينتج عن التقسّم:", O(("Sporozoites", "البويغات"), ("Merozoites", "الأقسومات"), ("Oocysts", "الأكياس البيضية"), ("Gametes", "الأعراس")), "b"),
 Q("The process by which merozoites become gametes is called:", "العملية التي تتحوّل بها الأقسومات إلى أعراس تُسمّى:", O(("Sporogony", "التبوّغ"), ("Merogony", "التقسّم"), ("Gametogony (gametogenesis)", "التكوّن العرسي (التولّد العرسي)"), ("Schizogony", "الانقسام المتعدّد")), "c"),
 Q("When the gametes fuse they form a:", "عندما تندمج الأعراس تكوّن:", O(("Merozoite", "أقسومة"), ("Sporozoite", "بويغة"), ("Trophozoite", "طورًا متغذّيًا"), ("Zygote", "لاقحة")), "d"),
 Q("The zygote differentiates into a form yielding:", "تتمايز اللاقحة إلى شكل يُنتج:", O(("Sporozoites", "البويغات"), ("Gametes", "الأعراس"), ("Cysts only", "الأكياس فقط"), ("Nothing further", "لا شيء بعد ذلك")), "a"),
 Q("When classified into two processes, the apicomplexan life cycle consists of:", "عند تصنيفها إلى عمليتين، تتكوّن دورة حياة المعقّدات القمّية من:", O(("Sporogony and merogony", "التبوّغ والتقسّم"), ("Schizogony and gametogony", "الانقسام المتعدّد والتكوّن العرسي"), ("Mitosis and meiosis", "الانقسام الخيطي والاختزالي"), ("Encystation and excystation", "التكيّس والانفلات")), "b"),
 Q("Sporogony and gametogony:", "التبوّغ والتكوّن العرسي:", O(("Always occur in the same cell", "يحدثان دائمًا في الخلية نفسها"), ("Occur only outside the host", "يحدثان خارج المضيف فقط"), ("Can involve different hosts or cell types", "قد يشترك فيهما مضيفات مختلفة أو أنواع خلايا مختلفة"), ("Are both sexual", "كلاهما جنسي")), "c"),
 Q("The alternation of asexual and sexual generations in the apicomplexan cycle is called:", "تناوب الأجيال اللاجنسية والجنسية في دورة المعقّدات القمّية يُسمّى:", O(("Binary fission", "الانشطار الثنائي"), ("Encystation", "التكيّس"), ("Conjugation", "الاقتران"), ("Alternation of generation", "تعاقب الأجيال")), "d"),
]
mcq = balance(mcq, 64)

tf = [
 TF("The apical complex is used for host cell invasion.", "يُستعمل المعقّد القمّي لغزو خلية المضيف.", "T"),
 TF("The apicoplast carries out photosynthesis in Apicomplexa.", "تقوم البلاستيدة القمّية بالتمثيل الضوئي في المعقّدات القمّية.", "F"),
 TF("The apicoplast is essential for the survival of the apicomplexan.", "البلاستيدة القمّية أساسية لبقاء الطفيلي القمّي.", "T"),
 TF("Apicomplexans move by pseudopods in their active stages.", "تتحرّك المعقّدات القمّية بالأقدام الكاذبة في أطوارها النشطة.", "F"),
 TF("Most apicomplexans must live inside a host to survive.", "معظم المعقّدات القمّية يجب أن تعيش داخل مضيف لتبقى حيّة.", "T"),
 TF("A conoid is present in every apicomplexan species.", "المخروط موجود في كل أنواع المعقّدات القمّية.", "F"),
 TF("The polar ring is composed of microtubules.", "تتألّف الحلقة القطبية من أنيبيبات دقيقة.", "T"),
 TF("Micronemes and rhoptries are secretory organelles.", "الميكرونيمات والروبتريات عُضيّات إفرازية.", "T"),
 TF("The name Sporozoa is no longer used by anyone.", "لم يعد أحد يستعمل اسم البوغيات.", "F"),
 TF("Electron microscopy revealed the ultrastructural features used to redefine the groups.", "كشف المجهر الإلكتروني الصفات البنيوية الدقيقة التي أُعيد بها تعريف المجموعات.", "T"),
 TF("Sporogony is a sexual process.", "التبوّغ عملية جنسية.", "F"),
 TF("Merozoites can become gametes as an alternative to asexual replication.", "يمكن أن تتحوّل الأقسومات إلى أعراس بديلًا عن التكاثر اللاجنسي.", "T"),
]

traps = [
 TR("Apicoplast ≠ chloroplast", "البلاستيدة القمّية ليست خضراء",
    "The apicoplast came from a red alga and is a PLASTID, but it is a RELICT: it does NOT photosynthesize. It is kept because it is essential for survival (and is a drug target).",
    "البلاستيدة القمّية جاءت من طحلب أحمر وهي **بلاستيدة**، لكنها **أثرية**: **لا** تقوم بالتمثيل الضوئي. وتبقى لأنها أساسية للبقاء (وهي هدف دوائي)."),
 TR("No flagella — except gametes", "بلا أسواط — إلّا الأعراس",
    "Apicomplexa lack flagella and pseudopods and move by gliding, BUT cilia/flagella are found in certain gamete stages (e.g. the male gamete of Plasmodium).",
    "المعقّدات القمّية بلا أسواط ولا أقدام كاذبة وتتحرّك بالانزلاق، **لكن** الأهداب/الأسواط توجد في أطوار عرسية معيّنة (مثل العُرس الذكري للمتصوّرة)."),
 TR("Merogony = schizogony", "التقسّم = الانقسام المتعدّد",
    "They are two names for the SAME asexual process — that is why the cycle is described as three processes (sporogony, merogony, gametogony) or as two (schizogony and gametogony).",
    "اسمان **للعملية اللاجنسية نفسها** — ولهذا تُوصف الدورة بثلاث عمليات (التبوّغ والتقسّم والتكوّن العرسي) أو بعمليتين (الانقسام المتعدّد والتكوّن العرسي)."),
 TR("Sporozoite vs merozoite", "البويغة مقابل الأقسومة",
    "Sporogony → SPOROZOITES; merogony → MEROZOITES. Sporozoites develop into the forms that then undergo merogony — do not swap the two.",
    "التبوّغ ← **البويغات**؛ والتقسّم ← **الأقسومات**. والبويغات تتطوّر إلى الأشكال التي تمرّ بعدها بالتقسّم — لا تبدّل بينهما."),
 TR("Apical complex ≠ apicoplast", "المعقّد القمّي ليس البلاستيدة القمّية",
    "The apical COMPLEX is the invasion machinery (micronemes, rhoptries, polar rings, conoid); the apicoPLAST is the relict plastid — different structures with similar names.",
    "**المعقّد القمّي** جهاز الغزو (ميكرونيمات، روبتريات، حلقات قطبية، مخروط)؛ أما **البلاستيدة القمّية** فهي البلاستيدة الأثرية — تركيبان مختلفان باسمين متشابهين."),
 TR("Plasmodium is not “Malaria”", "المتصوّرة ليست “الملاريا”",
    "The file writes “Plasmodium Malaria”: Plasmodium is the genus (P. falciparum, P. vivax …) and malaria is the disease — the genus is not called Malaria.",
    "الملف يكتب “Plasmodium Malaria”: فالمتصوّرة اسم الجنس (المنجلية، النشيطة…) والملاريا هي المرض — واسم الجنس ليس Malaria."),
]

important = [
 IM("What are the main properties that characterize the phylum Apicomplexa?", "ما الصفات الرئيسية التي تميّز شعبة المعقّدات القمّية؟",
    "A distinctive apical complex for host cell invasion; a relict non-photosynthetic plastid (the apicoplast) essential for survival; complex life cycles involving sexual and asexual reproduction; and gliding motility. Most are obligate endoparasites of animals, they are unicellular eukaryotes, and they lack external locomotion organelles (flagella or pseudopods), cilia and flagella being found only in certain gamete stages. Well-known members are Plasmodium (malaria) and Toxoplasma.",
    "معقّد قمّي مميّز لغزو خلية المضيف؛ وبلاستيدة أثرية غير قادرة على التمثيل الضوئي (البلاستيدة القمّية) أساسية للبقاء؛ ودورات حياة معقّدة فيها تكاثر جنسي ولا جنسي؛ والحركة الانزلاقية. ومعظمها طفيليات داخلية إجبارية للحيوانات، وكائنات وحيدة الخلية حقيقية النواة، وتفتقر إلى عُضيّات الحركة الخارجية (الأسواط أو الأقدام الكاذبة)، ولا توجد الأهداب والأسواط إلّا في أطوار عرسية معيّنة. ومن أشهر أفرادها المتصوّرة (الملاريا) والمقوّسة."),
 IM("Describe the ultrastructure of the apical complex.", "صف البنية الدقيقة للمعقّد القمّي.",
    "It is a group of organelles found at one end of the organism — the apical end. It includes the secretory organelles known as micronemes and rhoptries, a polar ring (or rings) composed of microtubules, and in some species a conoid which lies within the polar rings. These structures secrete the enzymes needed to penetrate and invade host cells.",
    "هو مجموعة من العُضيّات توجد في طرف واحد من الكائن يُسمّى الطرف القمّي. ويضمّ العُضيّات الإفرازية المعروفة بالميكرونيمات والروبتريات، وحلقة (أو حلقات) قطبية مؤلَّفة من أنيبيبات دقيقة، وفي بعض الأنواع مخروطًا يقع داخل الحلقات القطبية. وهذه التراكيب تفرز الإنزيمات اللازمة لاختراق خلايا المضيف وغزوها."),
 IM("What is the apicoplast and why is it important?", "ما البلاستيدة القمّية ولماذا هي مهمّة؟",
    "It is a relict, non-photosynthetic organelle (plastid) derived from a red alga via secondary endosymbiosis. Although it no longer carries out photosynthesis, it is essential for the survival of the apicomplexan — and because it is of plant origin and absent from human cells it is an attractive drug target.",
    "عُضيّة (بلاستيدة) أثرية غير قادرة على التمثيل الضوئي، مشتقّة من طحلب أحمر بالتعايش الداخلي الثانوي. ومع أنها لم تعد تقوم بالتمثيل الضوئي فهي أساسية لبقاء الطفيلي القمّي — ولأنها من أصل نباتي وغير موجودة في خلايا الإنسان فهي هدف دوائي مهمّ."),
 IM("Why are Apicomplexa sometimes still called Sporozoa?", "لماذا ما زالت المعقّدات القمّية تُسمّى أحيانًا البوغيات؟",
    "Formerly the Apicomplexa were part of a group called Sporozoa, and this name is still sometimes used; recently there have been some suggestions to revert back to the name Sporozoa. The old name came from the spores (oocysts) these parasites form, while Apicomplexa is taken from the apical complex.",
    "لأن المعقّدات القمّية كانت سابقًا جزءًا من مجموعة تُسمّى البوغيات، وما زال هذا الاسم يُستعمل أحيانًا؛ وظهرت حديثًا اقتراحات بالعودة إليه. وجاء الاسم القديم من الأبواغ (الأكياس البيضية) التي تكوّنها هذه الطفيليات، أما اسم المعقّدات القمّية فمأخوذ من المعقّد القمّي."),
 IM("Give the general characters of the Apicomplexa.", "اذكر الصفات العامة للمعقّدات القمّية.",
    "A monophyletic group composed almost entirely of parasitic species (no free-living forms); an extremely large and diverse group of more than 5000 named species; the parasites possess no locomotion organelles and show only a slight amoeboid change of form (body flexion); electron microscopy revealed their unique ultrastructural features, which were then used to redefine the groups; and their defining characteristic is the apical complex.",
    "مجموعة وحيدة النشأة مؤلَّفة كلّها تقريبًا من أنواع طفيلية (بلا أشكال حرّة المعيشة)؛ وهي مجموعة كبيرة جدًا ومتنوّعة فيها أكثر من 5000 نوع مسمّى؛ ولا تملك طفيلياتها عُضيّات حركة، وتُظهر تغيّرًا أميبيًا طفيفًا في الشكل (انثناء الجسم) فقط؛ وكشف المجهر الإلكتروني صفاتها البنيوية الدقيقة الفريدة التي استُعملت بعد ذلك لإعادة تعريف المجموعات؛ وصفتها المميّزة هي المعقّد القمّي."),
 IM("Describe the three processes of the apicomplexan life cycle.", "صف العمليات الثلاث في دورة حياة المعقّدات القمّية.",
    "Sporogony: an asexual reproduction that culminates in the production of sporozoites. Merogony: the sporozoites develop into forms that undergo another asexual replication, producing merozoites (merogony and its merozoites are known by many different names depending on the species). Gametogony (gametogenesis): as an alternative to asexual replication, merozoites can become gametes; the gametes fuse to form a zygote which differentiates into a form yielding sporozoites — an alternation of generation. The cycle may also be classified into two processes: schizogony and gametogony.",
    "التبوّغ: تكاثر لا جنسي ينتهي بإنتاج البويغات. والتقسّم: تتطوّر البويغات إلى أشكال تمرّ بتكاثر لا جنسي آخر فتنتج الأقسومات (ويُعرف التقسّم وأقسوماته بأسماء مختلفة كثيرة بحسب النوع). والتكوّن العرسي: بدلًا من التكاثر اللاجنسي يمكن أن تتحوّل الأقسومات إلى أعراس؛ فتندمج الأعراس مكوّنةً لاقحة تتمايز إلى شكل يُنتج البويغات — وهذا تعاقب الأجيال. وقد تُصنَّف الدورة أيضًا إلى عمليتين: الانقسام المتعدّد والتكوّن العرسي."),
]

meta = dict(subject_en="Diagnostic Parasitology", subject_ar="الطفيليات التشخيصية", short_ar="طفيليات", instructor="أ.د. نزار الخفاجي",
            unit_en="Week 10", unit_ar="الأسبوع 10", unit_label="WEEK", unit_no="10",
            title_en="Phylum Apicomplexa: main properties and ultrastructure of the apical complex",
            title_ar="شعبة المعقّدات القمّية: الصفات الرئيسية والبنية الدقيقة للمعقّد القمّي",
            department="قسم التحليلات", stage="The fourth stage — الرابعة", kind="Theory — نظري")
os.makedirs(f"/home/user/-/{FOLDER}", exist_ok=True)
shutil.copy(f"{SRC}/source-transcript.txt", f"/home/user/-/{FOLDER}/source-transcript.txt")
blocks, mcq, tf, traps, important = ltr_all(blocks), ltr_all(mcq), ltr_all(tf), ltr_all(traps), ltr_all(important)
save(FOLDER, meta, blocks, mcq, tf, traps, important)
fit(FOLDER, min_gap=0.08)
