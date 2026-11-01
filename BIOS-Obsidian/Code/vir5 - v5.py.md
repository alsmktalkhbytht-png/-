---
source: BIOS-Obsidian/tools/scripts/vir5/v5.py
handouts: []
saved: 2026-11-01
tags: [bios, code]
---
# vir5/v5.py

Utility script.

```python
import sys; sys.path.insert(0, "/tmp/claude-0/-home-user-kwmdkm/a0840832-519a-5a9b-84ea-294867ea1189/scratchpad/imm456")
from ci import *            # c helpers + B INSHORT TERMS balance save(split.fix)

BN = lambda en, ar: N(en, ar, label=["BIOS note", "ملاحظة BIOS"])
O = P

blocks = [
 # ───────────────────────── 1
 SEC("Complement Fixation Test", "اختبار تثبيت المتمّم"),
 C("The **complement fixation test (CFT)** is a **serological test** used to detect the presence of **specific antibodies or antigens** in a patient's serum.",
   "**اختبار تثبيت المتمّم (CFT)** **فحص مصلي** يُستعمل للكشف عن وجود **أضداد أو مستضدّات نوعية** في مصل المريض."),
 C("It is based on the principle of **complement fixation**, where complement proteins are **consumed in an antigen-antibody reaction**.",
   "ويعتمد على مبدأ **تثبيت المتمّم**، حيث **تُستهلك** بروتينات المتمّم **في تفاعل المستضدّ-الضدّ**."),
 C("This test has been widely used in the diagnosis of various viral infections, particularly those where **viral culture is difficult or unavailable**.",
   "وقد استُعمل هذا الاختبار على نطاق واسع في تشخيص إصابات فيروسية مختلفة، ولا سيّما تلك التي يكون فيها **الزرع الفيروسي صعبًا أو غير متاح**."),
 C(["**Complement** is a **protein (Globulin)** present in the **normal serum** and found in many types.", "When **Ag is complexed with Ab on the surface of cell**, complement causes **lysis of cell**."],
   ["**المتمّم** **بروتين (غلوبيولين)** موجود في **المصل الطبيعي** ويوجد بأنواع كثيرة.", "وعندما **يرتبط المستضدّ (Ag) بالضدّ (Ab) على سطح الخلية** يسبّب المتمّم **تحلّل الخلية**."]),
 C("The CFT has been used in the diagnosis of various viral infections, including: **Influenza, Measles, Mumps, Rubella, Herpes simplex virus, Cytomegalovirus**.",
   "استُعمل CFT في تشخيص إصابات فيروسية مختلفة، منها: **الإنفلونزا، والحصبة، والنكاف (أبو كعب)، والحصبة الألمانية، وفيروس الحلأ البسيط (الهربس البسيط)، والفيروس المضخّم للخلايا**."),
 INSHORT([("**CFT** = serological test for **antibodies or antigens** in serum; complement is **consumed** by Ag–Ab reaction.", "**CFT** = فحص مصلي **للأضداد أو المستضدّات** في المصل؛ والمتمّم **يُستهلك** بتفاعل المستضدّ-الضدّ."),
          ("**Complement** = serum **globulin** protein → lyses cells carrying Ag–Ab complexes.", "**المتمّم** = بروتين **غلوبيولين** مصلي ← يحلّل الخلايا الحاملة لمعقّدات المستضدّ-الضدّ."),
          ("Used for influenza, measles, mumps, rubella, HSV, CMV.", "يُستعمل للإنفلونزا والحصبة والنكاف والحصبة الألمانية والهربس البسيط وCMV.")]),

 # ───────────────────────── 2
 SEC("Procedure", "طريقة العمل"),
 R("**Serum Preparation:**", "**تحضير المصل:**"),
 L(["**Heat inactivate** the patient’s serum at **56°C for 30 minutes** to **destroy endogenous complement**."],
   ["**ثبّط** مصل المريض **بالحرارة** عند **56°م لمدة 30 دقيقة** **لتحطيم المتمّم الداخلي (الموجود أصلًا في المصل)**."]),
 R("**Primary Incubation:**", "**الحضن الأولي:**"),
 L(["Mix patient serum with **known viral antigen**.", "Add a **measured amount of complement**.", "Incubate the mixture at **37°C for 30 minutes** to allow antigen-antibody interaction and complement fixation."],
   ["امزج مصل المريض مع **مستضدّ فيروسي معروف**.", "أضف **كمية مقيسة من المتمّم**.", "احضن المزيج عند **37°م لمدة 30 دقيقة** للسماح بتفاعل المستضدّ-الضدّ وتثبيت المتمّم."]),
 R("**Indicator System Addition:**", "**إضافة النظام الدالّ (الكاشف):**"),
 L(["Add **sheep RBCs (SRBCs) sensitized with hemolysin**.", "Incubate at **37°C for another 30 minutes**."],
   ["أضف **كريات دم حمر للأغنام (SRBCs) مُحسَّسة بالهيمولايسين (الحالّ الدموي)**.", "احضن عند **37°م لمدة 30 دقيقة أخرى**."]),
 F("cft.png", "Complement fixation test. Complement-fixation stage: Antigen + Complement + Serum with antibody against antigen → Complement fixation (left); Antigen + Complement + Serum without antibody → No complement fixation (right). Indicator stage: Sheep RBC + Antibody to sheep RBC → (a) No hemolysis (complement tied up in antigen–antibody reaction); (b) Hemolysis (uncombined complement available). (a) Positive test. All available complement is fixed by the antigen–antibody reaction; no hemolysis occurs, so the test is positive for the presence of antibodies. (b) Negative test. No antigen–antibody reaction occurs. The complement remains, and the red blood cells are lysed in the indicator stage, so the test is negative.",
   "اختبار تثبيت المتمّم. مرحلة تثبيت المتمّم: مستضدّ + متمّم + مصل فيه ضدّ للمستضدّ ← تثبيت المتمّم (يسار)؛ مستضدّ + متمّم + مصل بلا ضدّ ← لا تثبيت للمتمّم (يمين). المرحلة الدالّة: كرية حمراء للأغنام + ضدّ لكريات الأغنام الحمر ← (أ) لا تحلّل دم (المتمّم مقيّد في تفاعل المستضدّ-الضدّ)؛ (ب) تحلّل دم (متمّم غير مرتبط متاح). (أ) اختبار موجب: كل المتمّم المتاح يُثبَّت بتفاعل المستضدّ-الضدّ؛ فلا يحدث تحلّل، والاختبار موجب لوجود الأضداد. (ب) اختبار سالب: لا يحدث تفاعل مستضدّ-ضدّ؛ فيبقى المتمّم وتتحلّل الكريات الحمر في المرحلة الدالّة، والاختبار سالب.", h="118mm"),
 R("**Result Interpretation:**", "**تفسير النتيجة:**"),
 L(["**Positive Test:** **No hemolysis** observed, indicating complement fixation due to antigen-antibody complex formation.",
    ["**Negative Test:** **Hemolysis** observed, indicating **free complement**, hence no antigen-antibody reaction.", "See figure above."]],
   ["**الاختبار الموجب:** **لا يُلاحظ تحلّل دم**، ممّا يدلّ على تثبيت المتمّم بسبب تكوّن معقّد المستضدّ-الضدّ.",
    ["**الاختبار السالب:** **يُلاحظ تحلّل دم**، ممّا يدلّ على **متمّم حرّ**، وبالتالي لا تفاعل بين المستضدّ والضدّ.", "انظر الشكل أعلاه."]]),
 T([B("Result", "النتيجة"), B("Hemolysis", "تحلّل الدم"), B("Complement", "المتمّم"), B("Meaning", "المعنى")],
   [[B("**Positive**", "**موجب**"), B("No", "لا"), B("fixed", "مُثبَّت"), B("Ag–Ab complex formed (antibody present)", "تكوّن معقّد مستضدّ-ضدّ (الضدّ موجود)")],
    [B("**Negative**", "**سالب**"), B("Yes", "نعم"), B("free", "حرّ"), B("no Ag–Ab reaction", "لا تفاعل مستضدّ-ضدّ")]],
   key_cols=[0], widths=[18, 18, 20, 44], style="summary", label_en="Reading the result", label_ar="قراءة النتيجة"),
 FLOW([("Heat serum 56°C, 30 min", "تسخين المصل 56°م، 30 د"), ("+ Ag + complement, 37°C 30 min", "+ مستضدّ + متمّم، 37°م 30 د"), ("+ sensitized SRBCs, 37°C 30 min", "+ كريات أغنام محسّسة، 37°م 30 د"), ("Read hemolysis", "قراءة التحلّل")], en="CFT in steps", ar="CFT بالخطوات"),
 INSHORT([("Serum **56°C / 30 min** destroys endogenous complement.", "المصل **56°م / 30 دقيقة** يحطّم المتمّم الداخلي."),
          ("Serum + **known antigen** + **measured complement** → 37°C; then **sensitized sheep RBCs** → 37°C.", "المصل + **مستضدّ معروف** + **متمّم مقيس** ← 37°م؛ ثم **كريات أغنام محسّسة** ← 37°م."),
          ("**No hemolysis = positive**; **hemolysis = negative** (free complement).", "**لا تحلّل = موجب**؛ **تحلّل = سالب** (متمّم حرّ).")]),

 # ───────────────────────── 3
 SEC("Advantages and Disadvantages", "المزايا والعيوب"),
 H2("Advantages of CFT", "مزايا CFT"),
 L(["Ability to **screen against a large number of viral and bacterial infections at the same time**.", "**Economical**."],
   ["القدرة على **الكشف عن عدد كبير من الإصابات الفيروسية والبكتيرية في الوقت نفسه**.", "**اقتصادي**."]),
 H2("Disadvantages of CFT", "عيوب CFT"),
 L(["**Not sensitive** - cannot be used for immunity screening", "**Time consuming** and **labor intensive**", "Often **non-specific** e.g. **cross-reactivity**"],
   ["**غير حسّاس** - لا يمكن استعماله لمسح المناعة", "**يستهلك الوقت** و**يحتاج جهدًا كبيرًا**", "غالبًا **غير نوعي** مثل **التفاعل المتصالب**"]),
 BN("Cross-reactivity is listed here as a disadvantage, so the answer of True/False question 10 at the end of the lab sheet (cross-reactivity as a disadvantage of CFT) should be **T**, not F; the question bank uses T.",
    "التفاعل المتصالب مذكور هنا من العيوب، لذلك سؤال الصح والخطأ رقم 10 في آخر ورقة العملي (التفاعل المتصالب من عيوب CFT) جوابه الصحيح **صح (T)**؛ واعتمدنا صح في بنك الأسئلة."),
 INSHORT([("Pros: **many infections at once**, **economical**.", "المزايا: **إصابات كثيرة دفعة واحدة**، **اقتصادي**."),
          ("Cons: **not sensitive** (no immunity screening), **slow and laborious**, **cross-reactivity**.", "العيوب: **غير حسّاس** (لا لمسح المناعة)، **بطيء ومُتعِب**، **تفاعل متصالب**.")]),

 *TERMS([("Complement fixation test (CFT)", "اختبار تثبيت المتمّم"),
         ("Complement", "المتمّم / المُكمِّل"),
         ("Serological test", "فحص مصلي"),
         ("Antigen (Ag)", "المستضدّ / الأنتيجين"),
         ("Antibody (Ab)", "الضدّ / الجسم المضاد"),
         ("Globulin", "الغلوبيولين"),
         ("Lysis", "التحلّل / الانحلال"),
         ("Heat inactivation", "التثبيط بالحرارة / التعطيل الحراري"),
         ("Endogenous complement", "المتمّم الداخلي (الذاتي)"),
         ("Indicator system", "النظام الدالّ / الكاشف"),
         ("Sheep RBCs (SRBCs)", "كريات الدم الحمر للأغنام"),
         ("Sensitized", "مُحسَّس / مُهيَّأ"),
         ("Hemolysin", "الهيمولايسين / الحالّ الدموي"),
         ("Hemolysis", "تحلّل الدم / انحلال الكريات الحمر"),
         ("Measles / Mumps / Rubella", "الحصبة / النكاف (أبو كعب) / الحصبة الألمانية"),
         ("Cytomegalovirus (CMV)", "الفيروس المضخّم للخلايا"),
         ("Immunity screening", "مسح (تحرّي) المناعة"),
         ("Cross-reactivity", "التفاعل المتصالب")]),
]
_t = blocks[-1]; _r = _t["rows"]
blocks[-1:] = [dict(_t, rows=_r[i:i + 6]) for i in range(0, len(_r), 6)]

exec(open(__file__.replace("v5.py", "v5q.py")).read())

```
