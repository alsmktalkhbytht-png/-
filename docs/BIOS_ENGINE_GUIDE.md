# دليل محرّك ملازم BIOS — التوثيق الكامل

> هذا الملف يشرح كل شيء عن نظام صنع ملازم قناة **BIOS** (تلغرام `@BIOS0t`):
> التصميم المعتمد، وبنية الكود، وطريقة العمل خطوة بخطوة، وصيغة ملف المحاضرة،
> والألوان، والغلاف، والأسئلة، وحلول كل المشاكل التي واجهتنا.
>
> المصطلحات والأوامر الإنجليزية موضوعة دائمًا داخل صناديق الكود أو الجداول
> حتى لا يختلّ اتجاه النص العربي.

---

## الفهرس

1. [الفكرة العامة](#1-الفكرة-العامة)
2. [القواعد المعتمدة من الفريق (لا تتغيّر إلا بطلب)](#2-القواعد-المعتمدة-من-الفريق)
3. [بنية المستودع](#3-بنية-المستودع)
4. [المتطلّبات والتشغيل](#4-المتطلّبات-والتشغيل)
5. [طريقة العمل الكاملة لمحاضرة جديدة](#5-طريقة-العمل-الكاملة-لمحاضرة-جديدة)
6. [ملف المحاضرة `lecture.json`](#6-ملف-المحاضرة)
7. [أنواع الكتل (Blocks)](#7-أنواع-الكتل)
8. [التنسيق داخل النص (Inline markup)](#8-التنسيق-داخل-النص)
9. [قسم الأسئلة](#9-قسم-الأسئلة)
10. [الغلاف المعتمد](#10-الغلاف-المعتمد)
11. [الألوان (Themes)](#11-الألوان)
12. [قواعد المراحل (الثالثة / الرابعة)](#12-قواعد-المراحل)
13. [تسمية الملفات](#13-تسمية-الملفات)
14. [كيف يعمل المحرّك من الداخل](#14-كيف-يعمل-المحرّك-من-الداخل)
15. [سكربت التوليد (Generator) — النمط المستخدم](#15-سكربت-التوليد)
16. [استخراج المحتوى من PDF وPPTX وDOCX](#16-استخراج-المحتوى)
17. [فحص الجودة قبل الإرسال](#17-فحص-الجودة-قبل-الإرسال)
18. [حلول المشاكل (Troubleshooting)](#18-حلول-المشاكل)
19. [الحفظ والرفع على Git](#19-الحفظ-والرفع-على-git)
20. [مرجع سريع للأوامر](#20-مرجع-سريع-للأوامر)
21. [قائمة الملازم المنجزة](#21-قائمة-الملازم-المنجزة)

---

## 1. الفكرة العامة

لكل محاضرة نكتب **ملفًا واحدًا فقط** هو `lecture.json` يحتوي:

- **المعلومات الأساسية** (المادة، التدريسي، المرحلة، رقم المحاضرة، العنوان).
- **المحتوى** على شكل كتل مرتّبة (عنوان قسم، بطاقة نص، جدول، صورة…).
- **الأسئلة** (اختيار من متعدد، صح وخطأ، مقالب، أسئلة مهمة).

ثم يتولّى المحرّك كل الباقي تلقائيًا:

```
lecture.json  ──►  bios.py  ──►  HTML  ──►  Chromium (Playwright)  ──►  PDF + صور الصفحات
```

المحرّك يبني الغلاف، والترويسة والتذييل، وبطاقات النص الإنجليزي مع ترجمته،
والصور والجداول، ويقسّم الصفحات تلقائيًا بقياس ارتفاع كل كتلة داخل المتصفّح،
ثم يبني بنك الأسئلة وجدول الحلول.

**لا نكتب HTML ولا CSS لأي محاضرة جديدة.** كل التصميم موجود في المحرّك.

---

## 2. القواعد المعتمدة من الفريق

هذه القواعد اتُّفق عليها خلال العمل، ويجب الالتزام بها في كل ملزمة:

### المحتوى

| القاعدة | التفصيل |
|---|---|
| النص الإنجليزي حرفي | يُنقل كما هو من المصدر بأخطائه الإملائية وعلاماته، ولا يُصحَّح. |
| الترجمة جملة بجملة | كل جملة إنجليزية تتبعها ترجمتها مباشرة، ثم الجملة التالية — حتى داخل النقاط الطويلة، ولا تُجمع ترجمة 3 جمل بعد الفقرة كلها. |
| ترجمة الجداول | كل خلية إنجليزية تحمل ترجمتها داخلها (`["en", "ar"]`)، وكذلك رؤوس الأعمدة؛ لا عمود «الترجمة» يلخّص الصف. |
| تنظيم للحفظ | لا يبقى كل شيء نصًا عاديًا: الفقرات المزدحمة تُدعم بجدول أو مخطط سهمي أو نقاط أو صندوق «باختصار»، مع بقاء النص الإنجليزي حرفيًا. |
| خلاصة كل موضوع | في نهاية كل موضوع (قسم) صندوق «باختصار» بنقاط ثنائية اللغة تلخّص ذلك الموضوع بتعريفاته وأرقامه وفروقه، حتى يراجعه الطالب بعد قراءته مباشرة. |
| نهاية الملزمة | جدول «أهم المصطلحات» فقط، بأكثر من ترجمة عربية لكل مصطلح؛ لا خلاصة عامة طويلة في النهاية. |
| النقاط القصيرة | الإنجليزي يسارًا والعربي يمينًا في السطر نفسه. |
| النقاط الطويلة | العربي تحت الإنجليزي. |
| حجم الخط العربي | 13pt (أصغر بدرجة من السابق). |
| النص المقطوع | يُعلَّم بـ `[[cut]]` في الإنجليزي و`[[قطع]]` في العربي. |
| المصطلح في التعريف | العربي ثم الإنجليزي بين علامتي الكود: ``**التعقيم** (`Sterilization`)`` |
| أسماء الكائنات | `__E. coli__` (عريض مائل)، وداخل العربي: `` `__E. coli__` `` |
| أخطاء الأصل | تبقى في الإنجليزي، والصحيح يُكتب في الترجمة، مع «ملاحظة بايوس» عند الحاجة. |
| أسئلة الصور | كل بنك أسئلة لمحاضرة فيها صور يحتوي قسم «أسئلة الصور». |
| المحاضرة العربية | تُبنى عربية فقط مع `"arabic_only": true`. |

### الشكل

| القاعدة | التفصيل |
|---|---|
| الترويسة | شارة الوحدة (مثل `Lab 1`) يسارًا، المادة بالوسط، شعار `BIOS` يمينًا. لا اسم تدريسي في الترويسة. |
| التذييل | معرّف التلغرام فقط، ورقم الصفحة يمينًا دائمًا. |
| الهامش الأيمن | خط عمودي عليه `BIOS · TELEGRAM · BIOS0t`. |
| الصفحات | متماثلة (لا صفحات زوجية وفردية مختلفة). |
| ممنوع | عبارة «ترجمة وتعديل الملازم»، وأي اسم شخصي لمترجم. |
| الغلاف | التصميم 1B فقط (انظر القسم 10). |
| الألوان | ثلاثة ألوان هادئة فقط. الافتراضي `wineoat`، والمرحلة الثالثة `blush`. |
| اسم الملف | عربي، وكلمة `BIOS` فقط بالإنجليزي. |
| قبل أي تصميم جديد | تُعرض خيارات على الفريق ليختار قبل التطبيق على الملازم. |

---

## 3. بنية المستودع

```
.
├── bios-engine/                 ← المحرّك
│   ├── bios.py                  ← البرنامج الرئيس (JSON → HTML → PDF)
│   ├── render.js                ← القياس والطباعة عبر Chromium/Playwright
│   ├── style.css                ← كل التصميم (بدون ألوان)
│   ├── make_theme.py            ← مولّد ألوان من ثلاثة ألوان + شعار ملوّن
│   ├── art.py                   ← رسومات متّجهة (رمز الخطر الحيوي والإشعاعي)
│   ├── themes/*.css             ← ملفات الألوان (متغيّرات CSS فقط)
│   ├── brand/                   ← الشعار الأصلي ونسخه الملوّنة
│   │   ├── logo_full.jpg        ← الشعار الأصلي
│   │   ├── logo_<theme>.jpg     ← شعار ملوّن لكل ثيم
│   │   └── logo_<theme>.png     ← شعار شفاف للغلاف
│   └── fonts/                   ← خطوط Mada وAmiri Quran وPlayfair
├── <lecture-folder>/            ← مجلد لكل محاضرة
│   ├── lecture.json             ← المحتوى (الملف الوحيد الذي نكتبه)
│   ├── assets/                  ← صور المحاضرة
│   ├── BIOS - ... .pdf          ← الناتج
│   └── .build/                  ← ملفات مؤقتة وصور الصفحات (لا تُرفع)
├── .claude/skills/bios-malzama/SKILL.md   ← تعليمات مختصرة للمساعد
├── docs/BIOS_ENGINE_GUIDE.md    ← هذا الملف
└── README.md                    ← قائمة المجلدات
```

`.gitignore` يستثني:

```
.build/
__pycache__/
```

---

## 4. المتطلّبات والتشغيل

| المتطلّب | الاستخدام |
|---|---|
| `Python 3` | تشغيل المحرّك |
| `Node.js` + حزمة `playwright` العامة | القياس والطباعة |
| `Chromium` | متصفّح Playwright |
| `pdfplumber`, `pdfimages`, `pdftoppm` | استخراج النص والصور من PDF |
| `python-pptx`, `python-docx` | قراءة PPTX وDOCX |
| `LibreOffice` (`soffice`) | تحويل PPTX إلى PDF لرؤية الشرائح |
| `Pillow`, `numpy` | قصّ الصور وتوليد الشعارات |

المحرّك يضبط مسار حزم Node بنفسه:

```python
env = dict(os.environ, NODE_PATH=subprocess.check_output(["npm", "root", "-g"]).decode().strip())
```

### أمر البناء

```bash
python3 bios-engine/bios.py <folder>/lecture.json
```

الناتج:

```
no overflow
/home/user/-/<folder>/BIOS - امراض الدم نظري المحاضرة الثانية.pdf  (17 pages + cover)
```

لبناء HTML فقط بدون PDF (للتجربة السريعة):

```bash
python3 bios-engine/bios.py <folder>/lecture.json --html-only
```

---

## 5. طريقة العمل الكاملة لمحاضرة جديدة

### الخطوة 1: جمع المعلومات

من رسالة المستخدم أو الملف نحتاج:

| المعلومة | مثال |
|---|---|
| المادة | أمراض الدم |
| النوع | نظري / عملي |
| رقم المحاضرة | 2 |
| المرحلة | الثالثة / الرابعة |
| التدريسي | د. مازن اللهيبي |

إذا كانت **المرحلة** أو **الترتيب** غير واضحين، **اسأل قبل البناء**، لأنهما يغيّران الألوان
وطريقة دمج الأسئلة واسم الملف.

### الخطوة 2: استخراج المحتوى

انظر القسم 16 للأوامر. الهدف: نص كامل وكل الصور المهمة في `assets/`.

### الخطوة 3: كتابة سكربت التوليد

نكتب سكربت `Python` صغيرًا (في مجلد مؤقت) يبني `lecture.json`، لأن كتابة JSON يدويًا
طويلة وتكثر فيها الأخطاء. انظر القسم 15.

### الخطوة 4: البناء

```bash
python3 make.py                                   # يكتب lecture.json
python3 bios-engine/bios.py <folder>/lecture.json # يبني PDF
```

### الخطوة 5: الفحص البصري

نجمع صور الصفحات في لوحة واحدة ونراجعها (القسم 17): فراغات كبيرة، صور مقصوصة،
نص معكوس الاتجاه، جداول مزدحمة.

### الخطوة 6: الإرسال والحفظ

- إرسال PDF للمستخدم.
- تحديث `README.md`.
- `git add` للمجلد (بدون `.build/`) ثم `commit` و`push`.

---

## 6. ملف المحاضرة

### الهيكل العام

```json
{
  "meta": { ... },
  "blocks": [ ... ],
  "questions": { ... }
}
```

### مفاتيح `meta`

| المفتاح | إلزامي | الوصف | مثال |
|---|---|---|---|
| `subject_en` | نعم | اسم المادة بالإنجليزي | `"Hematology"` |
| `subject_ar` | نعم | اسم المادة بالعربي | `"أمراض الدم"` |
| `short_ar` | مستحسن | الاسم المختصر لاسم الملف | `"امراض الدم"` |
| `unit_en` | نعم | يظهر في الترويسة والغلاف | `"Lecture 2"` أو `"Lab 1"` |
| `unit_ar` | نعم | يظهر في شارة الغلاف | `"المحاضرة 2"` أو `"العملي 1"` |
| `unit_label` | نعم | فوق الرقم في شريط العنوان | `"LEC"` أو `"LAB"` |
| `unit_no` | نعم | الرقم (يُحوَّل إلى «الأولى، الثانية…») | `"2"` |
| `title_en` | نعم | عنوان المحاضرة | `"Blood cell formation"` |
| `title_ar` | نعم | العنوان بالعربي | `"تكوين خلايا الدم"` |
| `kind` | نعم | يحدّد «نظري/عملي» | `"Theory — نظري"` |
| `stage` | مستحسن | المرحلة (تحدّد الألوان والدمج) | `"The third stage — الثالثة"` |
| `instructor` | اختياري | اسم التدريسي (يُخفى إن غاب) | `"د. مازن اللهيبي"` |
| `theme` | اختياري | لإجبار ثيم معيّن | `"wineoat"` |
| `merge_questions` | اختياري | دمج الأسئلة بالملزمة أو فصلها | `false` |
| `file_name` | اختياري | اسم ملف مخصّص بالكامل | `"BIOS - طفيليات ..."` |
| `arabic_only` | اختياري | محاضرة عربية بالكامل | `true` |
| `kind_ar` / `kind_en` | اختياري | نص شريحة النوع على الغلاف | `"عملي"` / `"Practical"` |
| `stage_ar` | اختياري | نص شريحة المرحلة على الغلاف | `"المرحلة الثالثة"` |

القيم الافتراضية في المحرّك:

```python
DEFAULTS = {"brand": "BIOS", "telegram": "BIOS0t", "translation": "بايوس",
            "instructor_label_ar": "تدريسية المادة", "unit_label": "LAB",
            "kind": "Laboratories — عملي", "questions_kind": "Questions — أسئلة"}
```

### مثال كامل مختصر

```json
{
 "meta": {
  "subject_en": "Hematology", "subject_ar": "أمراض الدم", "short_ar": "امراض الدم",
  "unit_en": "Lecture 4", "unit_ar": "المحاضرة 4", "unit_label": "LEC", "unit_no": "4",
  "title_en": "Hemoglobin", "title_ar": "الهيموغلوبين",
  "kind": "Theory — نظري", "stage": "The third stage — الثالثة",
  "instructor": "د. مازن اللهيبي"
 },
 "blocks": [
  {"t": "section", "en": "Hemoglobin", "ar": "الهيموغلوبين"},
  {"t": "card",
   "en": ["The main function of red cells is to carry O2 to the tissues.",
          "They contain the specialized protein called hemoglobin."],
   "ar": ["الوظيفة الرئيسة للكريات الحمر نقل الأوكسجين إلى الأنسجة.",
          "وتحتوي على بروتين متخصّص يُسمّى الهيموغلوبين."]}
 ],
 "questions": {
  "mcq": [{"en": "Hb A consists of:", "ar": "يتكوّن Hb A من:",
           "options": [["2 alpha and 2 beta chains", "سلسلتي ألفا وسلسلتي بيتا"],
                       ["2 alpha and 2 gamma chains", "سلسلتي ألفا وسلسلتي غاما"],
                       ["4 beta chains", "أربع سلاسل بيتا"],
                       ["2 alpha and 2 delta chains", "سلسلتي ألفا وسلسلتي دلتا"]],
           "answer": "a"}],
  "tf": [{"en": "Hb F contains beta chains.", "ar": "يحتوي Hb F على سلاسل بيتا.", "answer": "F"}],
  "traps": [], "important": []
 }
}
```

---

## 7. أنواع الكتل

كل كتلة لها المفتاح `t` الذي يحدّد نوعها. وأي كتلة تقبل `"keep": true` لتبقى في نفس
صفحة الكتلة التي بعدها (مفيد لصورة يشرحها جدول بعدها).

### 7.1 `section` — شريط قسم مرقّم

```json
{"t": "section", "en": "Iron Absorption", "ar": "امتصاص الحديد"}
```

يُرقَّم تلقائيًا (1، 2، 3…) ويبقى دائمًا مع الكتلة التي بعده.
ترقيم كتل `rule` يبدأ من جديد عند كل قسم.

### 7.2 `h2` — عنوان فرعي

```json
{"t": "h2", "en": "1. Erythropoiesis", "ar": "1. تكوين الكريات الحمر"}
```

### 7.3 `card` — بطاقة نص

نص واحد:

```json
{"t": "card", "en": "Text.", "ar": "نص."}
```

جمل متعدّدة (كل جملة تتبعها ترجمتها):

```json
{"t": "card", "en": ["Sentence one.", "Sentence two."], "ar": ["الجملة الأولى.", "الجملة الثانية."]}
```

بطاقة مع قائمة نقاط مرقّمة (كل نقطة مع ترجمتها):

```json
{"t": "card", "en": "Causes of anaemia:", "ar": "أسباب فقر الدم:",
 "list_en": ["Blood loss", "Impaired production"],
 "list_ar": ["فقدان الدم", "ضعف الإنتاج"]}
```

قائمة بأحرف `A, B, C` بدل الأرقام: أضف `"alpha": true`.

قائمة فقط بلا مقدّمة: اترك `en` و`ar` فارغين `""`.

> **مهم:** طول `en` و`ar` يجب أن يكون متساويًا إذا كانا قائمتين، وكذلك `list_en` و`list_ar`.

### 7.4 `rule` — خطوة مرقّمة بدائرة

```json
{"t": "rule", "en": "**Coating:** Immobilize antigen.", "ar": "**التغليف:** تثبيت المستضد."}
```

### 7.5 `group` — بطاقة بعنوان داكن

```json
{"t": "group", "title_en": "a) Direct ELISA", "title_ar": "أ) الإليزا المباشرة",
 "sub_en": "optional", "sub_ar": "اختياري",
 "en": ["Line 1.", "Line 2."], "ar": ["سطر 1.", "سطر 2."],
 "style": "light"}
```

`"style": "light"` يعطي شريط عنوان فاتحًا.

### 7.6 `figure` — صورة مرقّمة مع تعليق ثنائي اللغة

```json
{"t": "figure", "src": "assets/cell-cycle.png",
 "en": "The cell cycle", "ar": "دورة الخلية", "h": "70mm", "fit": "contain"}
```

| المفتاح | الوصف |
|---|---|
| `h` | ارتفاع الصورة (مثل `"60mm"`) |
| `fit` | `"contain"` (كاملة) أو `"cover"` (تملأ وتُقص) |
| `width` | بديل عن `h` (مثل `"100%"`) |
| `symbols` | `["biohazard", "radiation"]` لرسم رموز الخطر المتّجهة |

### 7.7 `figures` — صورتان جنبًا إلى جنب

```json
{"t": "figures", "items": [
  {"src": "assets/a.jpg", "en": "...", "ar": "...", "h": "50mm", "fit": "contain"},
  {"src": "assets/b.jpg", "en": "...", "ar": "...", "h": "50mm", "fit": "contain"}]}
```

### 7.8 `side` — نص يسارًا وصورة صغيرة يمينًا

```json
{"t": "side",
 "blocks": [{"t": "card", "en": "...", "ar": "..."}],
 "figure": {"src": "assets/x.jpg", "en": "Caption", "ar": "تعليق"}}
```

### 7.9 `table` — جدول

```json
{"t": "table", "head": ["Tube", "Additive", "الترجمة"],
 "rows": [["Purple", "EDTA", "بنفسجي — EDTA"]],
 "ar_cols": [2], "key_cols": [0], "widths": ["30mm", "", ""]}
```

| المفتاح | الوصف |
|---|---|
| `ar_cols` | أعمدة عربية (اتجاه يمين ← يسار) |
| `key_cols` | أعمدة بخط عريض (عمود المفتاح) |
| `widths` | عرض كل عمود (الفارغ = تلقائي) |
| `numbered` | العمود الأول رقم ملوّن |
| `style: "summary"` | يوضع داخل صندوق خلاصة مع شارة |
| `label_en` / `label_ar` | نص شارة الخلاصة |

### 7.10 `note` — ملاحظة مؤطّرة

```json
{"t": "note", "en": "Text.", "ar": "نص.", "label": ["Important", "مهم"]}
```

أمثلة على التسميات المستخدمة:

```
["Note", "ملاحظة"]  ["Important", "مهم"]  ["Remember", "تذكّر"]
["Key point", "نقطة مهمة"]  ["BIOS note", "ملاحظة بايوس"]  ["Rule", "قاعدة"]
```

### 7.11 `flow` — سلسلة أسهم

صف أفقي:

```json
{"t": "flow", "steps": [{"en": "Coating", "ar": "التغليف"}, {"en": "Blocking", "ar": "الحجب"}]}
```

عمودي مع شرح لكل خطوة: أضف `text_en` و`text_ar` لكل خطوة.
عنوان فوق السلسلة: `en` و`ar` على مستوى الكتلة. وتعليق تحتها: `tail_en` و`tail_ar`.
في المحاضرات العربية تتّجه الأسهم من اليمين إلى اليسار تلقائيًا.

### 7.12 `eq` — صورة معادلة (بلا ترقيم)

```json
{"t": "eq", "src": "assets/mm-equation.jpg", "h": "20mm"}
```

أو عدة صور في سطر واحد: `"src": ["assets/a.jpg", "assets/b.jpg"]`.

### 7.13 كتل أخرى

```json
{"t": "spacer", "h": "3mm"}
{"t": "pagebreak"}
{"t": "html", "html": "<div>...</div>"}
```

---

## 8. التنسيق داخل النص

| الكتابة | النتيجة |
|---|---|
| `**text**` | مصطلح عريض مسطّر بلون الثيم |
| `*text*` | مائل |
| `__text__` | عريض مائل (أسماء الكائنات) |
| `` `text` `` | مقطع إنجليزي معزول الاتجاه داخل العربي |
| `^^text^^` | علامة بارزة ملوّنة |
| `[[cut]]` / `[[قطع]]` | وسم «النص مقطوع في الملف الأصلي» |
| `\\*` | نجمة حرفية |

الكود المسؤول:

```python
def md(s):
    s = html.escape(s or "", quote=False).replace("\\*", "\x00")
    s = re.sub(r"__(.+?)__", r'<i class="sp">\1</i>', s)
    s = re.sub(r"\*\*(.+?)\*\*", r'<b class="t">\1</b>', s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", s)
    s = re.sub(r"`(.+?)`", r'<bdi dir="ltr" class="lt">\1</bdi>', s)
    s = re.sub(r"\^\^(.+?)\^\^", r'<span class="mark">\1</span>', s)
    ...
```

> **قاعدة ذهبية:** أي كلمة إنجليزية أو رقم بوحدة أو صيغة كيميائية داخل نص عربي
> تُوضع بين علامتي `` ` `` حتى لا ينقلب ترتيب الكلمات.

---

## 9. قسم الأسئلة

### الأنواع

```json
"questions": {
  "mcq": [
    {"topic_en": "Iron", "topic_ar": "الحديد"},
    {"en": "Q?", "ar": "س؟", "options": [["A","أ"],["B","ب"],["C","ج"],["D","د"]], "answer": "b"},
    {"en": "Picture Q", "ar": "سؤال صورة", "options": [...], "answer": "c",
     "img": "assets/q-microtome.jpg", "img_h": "36mm"}
  ],
  "tf":        [{"en": "...", "ar": "...", "answer": "T"}],
  "traps":     [{"en": "...", "ar": "...", "answer_en": "...", "answer_ar": "..."}],
  "important": [{"en": "...", "ar": "...", "answer_en": "...", "answer_ar": "..."}]
}
```

| العنصر | الوصف |
|---|---|
| `topic_en/topic_ar` | عنوان فرعي بين الأسئلة (لا يُحسب سؤالًا) |
| `options` | 4 أو 5 خيارات (A–E) |
| `answer` | حرف صغير `a`–`e`، أو `T`/`F` في صح وخطأ |
| `img` / `img_h` | سؤال صورة: الصورة بين السؤال والخيارات |
| `note_en/note_ar` | ملاحظة على الإجابة تظهر تحت جدول الحلول |

مفاتيح إضافية لبنك أسئلة بلا محاضرة:
`title_en`، `title_ar`، `sub`، `mcq_en`، `mcq_ar`، `intro_en`، `intro_ar`.

### المعايير

| النوع | العدد المعتاد |
|---|---|
| اختيار من متعدد | 20–38 حسب حجم المحاضرة |
| أسئلة صور | 3–6 (إن وُجدت صور) |
| صح وخطأ | 10–14 |
| مقالب | 5–7 |
| أسئلة مهمة | 5–8 مع إجابات نموذجية |

- توزيع الإجابات الصحيحة متوازن بين `a b c d` (السكربت يطبع العدّ للتأكد).
- إذا وضع التدريسي أسئلة مراجعة في نهاية المحاضرة، تصبح هي «الأسئلة المهمة» مع إجابات من نص المحاضرة.
- إذا كان في الملف أسئلة جاهزة بإجابات معلّمة بخط عريض، تُستخرج الإجابات من نوع الخط (القسم 16).
- **أسئلة الصور للأجهزة:** نقصّ اسم الجهاز المكتوب على الصورة قبل وضعها في السؤال.

### ترتيب البنك داخل الملف

```
عنوان «بنك الأسئلة» ← الاختيار ← صح وخطأ ← المقالب ← الأسئلة المهمة (مع أسطر للإجابة)
← الحلول: جدول الاختيار، ملاحظات الحلول، جدول صح وخطأ، إجابات المقالب، الإجابات النموذجية
```

---

## 10. الغلاف المعتمد

التصميم النهائي **1B** — وافق عليه الفريق ولا يُغيَّر:

```
┌───────────────────────────────┐  ← إطاران رفيعان مزدوجان
│            [ شعار BIOS ]       │
│       Hematology               │  ← المادة بالإنجليزي
│       أمراض الدم               │  ← المادة بالعربي
│      ┌──[ LAB 1 · العملي 1 ]──┐│  ← شارة الرقم فوق الصندوق
│      │   عنوان المحاضرة عربي   ││  ← صندوق داكن
│      │   Lecture title          ││
│      └──────────────────────────┘│
│   [ عملي · Practical ] [ المرحلة الثالثة ] │  ← شريحتان بيضاوان
│           ─────────              │
│     INSTRUCTOR · التدريسي        │
│        م.م. آية وسمي             │  ← اسم كبير وعريض
│      BIOS · Telegram @BIOS0t     │  ← سطر صغير في الأسفل
└───────────────────────────────┘
```

يحتوي ستة أشياء فقط: التدريسي، المادة، العنوان، النوع، الرقم، المرحلة.
إذا غاب اسم التدريسي أو المرحلة يُخفى تلقائيًا.

دوال تحويل الشرائح:

```python
def cover_kind(kind):          # "Theory — نظري" → "نظري · Theory"
def cover_stage():             # "The third stage — الثالثة" → "المرحلة الثالثة"
```

مواضع عناصر الغلاف في `style.css` (لا تُعدَّل):

```css
.cb-logo{top:26mm;width:90mm}
.cb-subj{top:106mm}
.cb-low{top:150mm}
.cb-chips{margin-top:12mm}
.cb-ins b{font-size:20pt;font-weight:900}
.cb-foot{bottom:17mm}
```

---

## 11. الألوان

### المبدأ

ملف `style.css` لا يحتوي ألوانًا مباشرة، بل متغيّرات:

| المتغيّر | الاستخدام |
|---|---|
| `--dark` | النص الرئيس، الأشرطة، التذييل |
| `--gold` / `--star` / `--red` | اللون المتوسط: الأرقام، الخطوط، الحدود |
| `--egret` | الخلفيات الفاتحة (لوحات العربي، الغلاف) |
| `--ink` | لون النص |
| `--key` | لون المصطلحات العريضة |
| `--paper` | خلفية الصفحة (أبيض) |
| `--muted` | النص الثانوي |
| `--bd` | لون الحدود |

كل ثيم ملف واحد في `bios-engine/themes/` يعيد تعريف هذه المتغيّرات.

### الثيمات المعتمدة

| الثيم | الألوان | الاستخدام |
|---|---|---|
| `wineoat` | `#4A2C34` · `#C9B4A5` · `#F7F1EE` | **الافتراضي** لكل الملازم (النموذج 10) |
| `blush` | `#f9e9ef` · `#f2808f` · `#e8d6d0` · `#eebcc2` + نص `#4a2a30` | **المرحلة الثالثة** تلقائيًا |

ثيمات تجريبية موجودة للعرض فقط:
`knight` `nightfall` `plum` `rose` `violet` `oatmeal` `sage` `mist` `sand` `seafoam` `lilac` `powder` `oceansand` `slate` `rosewood`.

### توليد ثيم جديد

```bash
python3 bios-engine/make_theme.py NAME DARK MID LIGHT "Title"
# مثال:
python3 bios-engine/make_theme.py wineoat "#4a2c34" "#c9b4a5" "#f7f1ee" "10 · Soft Wine & Oatmeal"
```

ينتج:

```
bios-engine/themes/NAME.css        ← المتغيّرات + تصحيحات التباين
bios-engine/brand/logo_NAME.jpg    ← الشعار بلونين
bios-engine/brand/logo_NAME.png    ← الشعار شفافًا للغلاف
```

المولّد يجبر النص فوق اللون المتوسط أن يكون داكنًا، والنص فوق الأشرطة أن يكون فاتحًا،
حتى لا يظهر نص باهت (انظر حلول المشاكل).

### الشعار الملوّن (الفكرة البرمجية)

```python
a = np.asarray(Image.open("brand/logo_full.jpg").convert("L")).astype(float)
lo, hi = np.percentile(a, 1), np.percentile(a, 45)
t = np.clip((a - lo) / (hi - lo), 0, 1)          # 0 = حبر، 1 = ورق
t[int(.70*900):int(.82*900), :] = 1               # حذف سطر الشعار السفلي
alpha = ((1 - t) * 255).astype("uint8")           # الشفافية
ink = np.dstack([np.full(t.shape, c, "uint8") for c in rgb(dark)] + [alpha])
Image.fromarray(ink, "RGBA").crop((90, 150, 810, 640)).save("brand/logo_NAME.png")
```

---

## 12. قواعد المراحل

القرار تلقائي داخل `build()` اعتمادًا على `meta.stage`:

```python
third = cover_stage() == "المرحلة الثالثة"
theme = M.get("theme", "blush" if third else "wineoat")
merge = M.get("merge_questions", third)
```

| المرحلة | الألوان | الأسئلة |
|---|---|---|
| الثالثة | `blush` (وردي) | **داخل الملف نفسه** بعد المحاضرة، ترقيم متصل |
| الرابعة وغيرها | `wineoat` | ملف منفصل باسم `... - الأسئلة.pdf` |

عند الدمج يحذف المحرّك تلقائيًا أي ملف أسئلة منفصل قديم.

للتجاوز (فقط بطلب صريح):

```json
"theme": "wineoat", "merge_questions": false
```

---

## 13. تسمية الملفات

الصيغة:

```
BIOS - <الاسم المختصر> <النوع> المحاضرة <الترتيب>.pdf
BIOS - <الاسم المختصر> <النوع> المحاضرة <الترتيب> - الأسئلة.pdf
```

أمثلة حقيقية:

```
BIOS - مناعة عملي المحاضرة الأولى.pdf
BIOS - امراض الدم نظري المحاضرة السابعة.pdf
BIOS - انزيمات سريرية نظري المحاضرة الثانية - الأسئلة.pdf
```

الكود:

```python
ORD_F = ["الأولى", "الثانية", "الثالثة", ...]      # للمحاضرة
ORD_M = ["الأول", "الثاني", "الثالث", ...]          # للأسبوع
def file_name():
    if M.get("file_name"): return M["file_name"]
    n = int(M["unit_no"]) if str(M["unit_no"]).isdigit() else 0
    week = M["unit_ar"].startswith("الأسبوع")
    ...
    return f'{M["brand"]} - {M.get("short_ar", M["subject_ar"])} {kind_ar} {unit}'
```

إذا كان الرقم غير عددي (مثل `1+2`) نستخدم `file_name` يدويًا:

```json
"file_name": "BIOS - أمراض نظري المحاضرة الأولى والثانية"
```

---

## 14. كيف يعمل المحرّك من الداخل

### 14.1 المسار الكامل لدالة `build()`

```
load(json) → M (meta + defaults)
    │
    ├─ اختيار الثيم والدمج حسب المرحلة
    ├─ render_block() لكل كتلة → قائمة items = [(html, keep_with_next)]
    ├─ paginate(items) → قياس في Chromium ثم توزيع على صفحات
    ├─ cover() + page() لكل صفحة
    ├─ (إن وُجدت أسئلة) question_items() → paginate → صفحات الأسئلة
    ├─ doc() → كتابة HTML في .build/
    └─ node render.js pdf → PDF + صورة لكل صفحة في .build/*-pages/
```

### 14.2 التقسيم التلقائي للصفحات

1. توضع كل الكتل في صفحة واحدة طويلة، وكل كتلة داخل `div` يحمل `data-m="رقم"`.
2. يقيس `render.js` ارتفاع كل كتلة بالملّيمتر:

```js
document.querySelectorAll('[data-m]').forEach(e => {
  o[e.dataset.m] = e.getBoundingClientRect().height * 25.4 / 96;
});
```

3. توزّع `paginate()` الكتل بحيث لا يتجاوز مجموع الصفحة `BODY_MM = 240`:

```python
for i, (h, keep) in enumerate(items):
    need = H[str(i)]
    j = i
    while keep and j + 1 < len(items):     # العنوان يُحسب مع الكتلة التي بعده
        j += 1; need += H[str(j)]
        if not items[j][1]: break
    if cur and (i in forced or h_cur + need > BODY_MM):
        pages.append(cur); cur, h_cur = [], 0.0
    cur.append(h); h_cur += H[str(i)]
```

النتيجة: لا يبقى عنوان قسم وحيدًا في أسفل الصفحة.

> **ملاحظة:** الكتلة الأطول من صفحة كاملة لا تُقسَّم؛ لذلك نقسّم البطاقات الطويلة يدويًا
> إلى بطاقات أصغر (انظر حلول المشاكل).

### 14.3 الطباعة

`render.js` بوضع `pdf`:

- ينتظر تحميل الخطوط `document.fonts.ready`.
- يتحقّق أن محتوى كل صفحة لم يفض (`no overflow` أو `page N overflows by X mm`).
- يبلّغ عن أي خط فشل تحميله `FONT LOAD ERRORS`.
- يلتقط صورة لكل صفحة ثم يطبع PDF بحجم `A4`.

### 14.4 أبعاد الصفحة

```css
@page{size:A4;margin:0}
.page{width:210mm;height:297mm}
.hdr{top:12mm;height:13mm}
.body{left:17mm;right:17mm;top:31mm;bottom:24mm}   /* ≈ 242mm ارتفاع */
.ftr{bottom:6mm;height:6mm}
.mr{right:8.5mm;top:31mm;bottom:31mm}              /* خط الهامش الأيمن */
```

### 14.5 الخطوط

| الخط | الاستخدام |
|---|---|
| `Mada` | كل النص الإنجليزي والعناوين |
| `AmiriQ` (Amiri Quran) | النص العربي في البطاقات (13pt) |
| `Playfair` مائل عريض | كلمة `BIOS` في الترويسة |

### 14.6 وضع المحاضرة العربية

مع `"arabic_only": true`:

- `<body class="ar-only">` يخفي شرائح `EN/AR`.
- الأرقام والقوائم من اليمين.
- ترقيم الأسئلة `س1، س2…`، والخيارات `أ ب ج د` (دالة `letters()`).
- الأسهم في `flow` من اليمين إلى اليسار.
- تُترك حقول `en` فارغة `""` (أو `[""]` لكل عنصر في القوائم).

---

## 15. سكربت التوليد

لا نكتب `lecture.json` بيدنا. نكتب سكربت `Python` صغيرًا بدوال مختصرة.

### ملف المساعدات المشترك `common.py`

```python
import json, os
from collections import Counter

def C(en, ar, **k):  return dict(t="card", en=en, ar=ar, **k)
def R(en, ar):       return dict(t="rule", en=en, ar=ar)
def SEC(en, ar):     return dict(t="section", en=en, ar=ar)
def H2(en, ar):      return dict(t="h2", en=en, ar=ar)
def L(en_items, ar_items, en="", ar="", **k):
    return dict(t="card", en=en, ar=ar, list_en=en_items, list_ar=ar_items, **k)
def N(en, ar, label=None):
    b = dict(t="note", en=en, ar=ar)
    if label: b["label"] = label
    return b
def FLOW(pairs, **k): return dict(t="flow", steps=[{"en": e, "ar": a} for e, a in pairs], **k)
def T(head, rows, **k): return dict(t="table", head=head, rows=rows, **k)
def F(src, en, ar, **k): return dict(t="figure", src="assets/" + src, en=en, ar=ar, **k)
def FF(*items):
    return dict(t="figures", items=[dict(src="assets/" + s, en=e, ar=a, h=h, fit="contain")
                                    for s, e, a, h in items])
def SIDE(blocks, src, en, ar):
    return dict(t="side", blocks=blocks, figure=dict(src="assets/" + src, en=en, ar=ar))

def Q(en, ar, opts, ans, **k):
    return dict(en=en, ar=ar, options=[list(o) for o in opts], answer=ans, **k)
def TF(en, ar, a): return dict(en=en, ar=ar, answer=a)
def TR(en, ar, ae, aa): return dict(en=en, ar=ar, answer_en=ae, answer_ar=aa)
IM = TR

def save(folder, meta, blocks, mcq, tf, traps, important):
    qs = [q for q in mcq if "answer" in q]
    print(folder, len(qs), dict(Counter(q["answer"] for q in qs)),
          len(tf), len(traps), len(important))          # للتأكد من توازن الإجابات
    d = "/home/user/-/" + folder
    os.makedirs(d, exist_ok=True)
    json.dump({"meta": meta, "blocks": blocks,
               "questions": {"mcq": mcq, "tf": tf, "traps": traps, "important": important}},
              open(d + "/lecture.json", "w"), ensure_ascii=False, indent=1)
```

### مثال سكربت محاضرة

```python
from common import *

blocks = [
 SEC("Anaemia", "فقر الدم"),
 C("**Definition:** It is a state of decrease hemoglobin level ...",
   "**التعريف:** حالة انخفاض مستوى الهيموغلوبين ..."),
 C("**Causes of anaemia:**", "**أسباب فقر الدم:**",
   list_en=["Blood loss", "Impaired production", "Accelerated destruction"],
   list_ar=["فقدان الدم", "ضعف الإنتاج", "تسارع التحطّم"]),
 T(["Test", "Useful in diagnosis of", "الفحص — يفيد في تشخيص"],
   [["Coombs test", "immune hemolytic anemia", "**اختبار كومبس** — فقر الدم الانحلالي المناعي"]],
   ar_cols=[2], key_cols=[0]),
]

mcq = [
 {"topic_en": "Definition", "topic_ar": "التعريف"},
 Q("Anaemia is a decrease in:", "فقر الدم انخفاض في:",
   [("WBC", "الكريات البيض"), ("Haemoglobin", "الهيموغلوبين"), ("Platelets", "الصفيحات"), ("Iron", "الحديد")], "b"),
]
tf = [TF("Anaemia is always accompanied by low PCV.", "...", "F")]
traps = [TR("Skin vs mucous membrane pallor", "...", "...", "...")]
important = [IM("Define anaemia.", "عرّف فقر الدم.", "...", "...")]

meta = dict(subject_en="Hematology", subject_ar="أمراض الدم", short_ar="امراض الدم",
            unit_en="Lecture 5", unit_ar="المحاضرة 5", unit_label="LEC", unit_no="5",
            title_en="Anaemia", title_ar="فقر الدم", kind="Theory — نظري",
            stage="The third stage — الثالثة", instructor="د. مازن اللهيبي")
save("hematology-lec5-anaemia", meta, blocks, mcq, tf, traps, important)
```

ثم:

```bash
python3 make.py && python3 bios-engine/bios.py hematology-lec5-anaemia/lecture.json
```

---

## 16. استخراج المحتوى

### 16.1 PDF — النص

```bash
python3 -I -c "
import pdfplumber
p = pdfplumber.open('src/x.pdf')
for i, pg in enumerate(p.pages):
    print('=== PAGE', i+1); print(pg.extract_text() or '')
" > x.txt
```

إذا خرج النص فارغًا أو مشوّهًا (ملف مصوّر أو خط عربي معطوب) نقرأ صور الصفحات:

```bash
pdftoppm -r 130 -png src/x.pdf pg/x
```

### 16.2 PDF — الصور

قائمة الصور:

```bash
pdfimages -list src/x.pdf
```

أفضل طريقة (تحافظ على الشكل كما يظهر في الشريحة): قصّ مواضع الصور من صورة الصفحة.

```python
import pdfplumber, glob
from PIL import Image
p = pdfplumber.open("src/x.pdf"); files = sorted(glob.glob("hi/x-*.png"))
for i, pg in enumerate(p.pages):
    im = Image.open(files[i]); s = im.size[0] / float(pg.width)
    for k, o in enumerate(pg.images):
        if o["x1"]-o["x0"] < 60: continue
        box = (int(o["x0"]*s), int(o["top"]*s), int(o["x1"]*s), int(o["bottom"]*s))
        im.crop(box).convert("RGB").save(f"crop/x{i+1:02d}_{k}.jpg", quality=90)
```

ثم نصنع لوحة مصغّرات لنختار الصور ونسمّيها أسماء واضحة في `assets/`.

### 16.3 PDF — إجابات معلّمة بالخط العريض

```python
for pg in p.pages:
    ws = pg.extract_words(extra_attrs=["fontname"])
    print([w["text"] for w in ws if "Bold" in w["fontname"]])
```

### 16.4 PPTX

```python
from pptx import Presentation
p = Presentation("src/a.pptx")
for i, s in enumerate(p.slides, 1):
    for sh in s.shapes:
        if sh.has_text_frame:
            for para in sh.text_frame.paragraphs: print(''.join(r.text for r in para.runs))
        elif getattr(sh, "has_table", False) and sh.has_table:
            for r in sh.table.rows: print(' | '.join(c.text for c in r.cells))
```

الصور: نفك الملف كأرشيف ونربط كل صورة بشريحتها:

```bash
unzip -o -q src/a.pptx 'ppt/media/*'
unzip -p src/a.pptx ppt/slides/_rels/slide5.xml.rels | grep -o 'media/[^"]*'
```

لرؤية الشرائح كما تظهر:

```bash
soffice --headless --convert-to pdf --outdir src src/a.pptx
pdftoppm -r 60 -png src/a.pdf pg/a
```

> **انتبه:** بعض الشرائح نصّها داخل صورة (جداول، رسوم توضيحية). نقرأ الصورة ونحوّلها إلى جدول مترجم.

### 16.5 DOCX

```python
import docx
d = docx.Document("src/c.docx")
for p in d.paragraphs:
    if p.text.strip(): print(p.style.name, p.text)
for t in d.tables:
    for r in t.rows: print(' | '.join(c.text for c in r.cells))
```

الصور:

```bash
unzip -o -q src/c.docx 'word/media/*'
```

### 16.6 نص ملصق في الرسالة

يُعامل كأنه المصدر. الأسهم والجداول غالبًا تضيع عند النسخ، فنعيد بناءها
(سلاسل `flow` وجداول `table`) مع الحفاظ على الكلمات حرفيًا.

### 16.7 رسم شكل غير موجود في المصدر

إذا لم يكن في المحاضرة صورة لشيء مهم (مثل أنواع الإليزا) نرسم `SVG` بسيطًا
بألوان الثيم ونكتب في التعليق أنه رُسم للملزمة من نص المحاضرة.

---

## 17. فحص الجودة قبل الإرسال

### لوحة مصغّرات لكل الصفحات

```python
from PIL import Image; import glob
fs = sorted(glob.glob("<folder>/.build/booklet-pages/*.png"))
ims = [Image.open(f) for f in fs]; w, h = ims[0].size
ims = [i.resize((300, int(h*300/w))) for i in ims]; W, H = ims[0].size
cols = 6; rows = (len(ims)+cols-1)//cols
S = Image.new("RGB", (W*cols, H*rows), "white")
for i, im in enumerate(ims): S.paste(im, ((i % cols)*W, (i//cols)*H))
S.save("contact-sheet.png")
```

### قائمة الفحص

- [ ] السطر `no overflow` ظاهر في ناتج البناء.
- [ ] لا صفحات بنصفها فارغ (إن وُجدت: قسّم البطاقات أو صغّر الصور أو اجمعها بـ `figures`).
- [ ] الغلاف: المادة، العنوان، الرقم، النوع، المرحلة، التدريسي صحيحة.
- [ ] الصور غير مقصوصة وغير مكرّرة، والتسميات مطابقة للصورة.
- [ ] لا نص عربي مقلوب الترتيب حول الأرقام والكلمات الإنجليزية.
- [ ] الألوان مناسبة للمرحلة.
- [ ] اسم الملف صحيح.
- [ ] توزيع إجابات الاختيار متوازن.

---

## 18. حلول المشاكل

| المشكلة | السبب | الحل |
|---|---|---|
| ترتيب الكلمات في سطر عربي مقلوب | كلمة إنجليزية أو رقم بوحدة داخل العربي بدون عزل | ضعها بين `` ` `` |
| صفحة نصفها فارغ | بطاقة طويلة لا تتّسع في بقية الصفحة فتنتقل كاملة | قسّم البطاقة إلى بطاقتين أو أكثر، أو صغّر الصور قبلها |
| كل قسم يأخذ صفحة كاملة | صورة كبيرة مع نص في كتلة واحدة | استخدم `side` أو `figures` لصورتين متجاورتين |
| نقاط قصيرة جدًا تأخذ صفوفًا كثيرة | استُخدمت `group` بنقاط كجمل | حوّلها إلى `card` مع `list_en/list_ar` (تصبح متجاورة) |
| `AssertionError: en/ar sentence lists differ` | عدد الجمل الإنجليزية لا يساوي العربية | وحّد عدد عناصر القائمتين |
| خطأ عند بطاقة عربية فقط بقائمة | `en` فارغ و`ar` قائمة | المحرّك يعالجها تلقائيًا (`sentences()` يملأ `[""]*len`) |
| نص باهت فوق اللون المتوسط | الثيم يكتب بلون الوسط على خلفية فاتحة | `make_theme.py` يجبر النص الداكن على هذه العناصر |
| شارة الخلاصة داكن على داكن | `.pillh` لم يكن ضمن عناصر النص الفاتح | أُضيفت إلى قائمة النص الفاتح في المولّد |
| صور صفحات قديمة تظهر في المراجعة | مجلد الصور لم يُفرّغ | المحرّك يحذف الصور القديمة قبل كل بناء |
| ملف أسئلة منفصل قديم بقي بعد الدمج | تغيّرت المرحلة إلى الثالثة | المحرّك يحذفه تلقائيًا عند الدمج |
| مدى أرقام مثل `40–65` معكوس في العربي | شرطة بين رقمين داخل نص عربي | اكتبها «40 إلى 65» أو ضعها بين `` ` `` |
| نص عربي مشوّه من PDF | خط PDF بترميز معطوب | انقل النص من صور الصفحات مباشرة |
| ملف PDF كله صور | شرائح مطبوعة كصور | اقرأ صور الصفحات بدقّة أعلى `-r 150` |
| الأسس ضاعت (`103` بدل `10³`) | استخراج النص لا يحفظ الأسس | أبقها في الإنجليزي حرفيًا، واكتب الصحيح في العربي |
| الصورة الملتقطة مقصوصة أو بإطار زائد | حدود الصورة في الشريحة | قصّ نسبي بـ `crop((w*l, h*t, w*(1-r), h*(1-b)))` |
| أسماء صور معكوسة | ترتيب الصور في الشريحة غير ترتيبها في الملف | راجع لوحة المصغّرات وبدّل الأسماء قبل البناء |
| رقم محاضرة متكرّر لنفس المادة | تعارض في المعلومات من المستخدم | اسأل المستخدم ثم أعد الترقيم وأعد تسمية المجلد |
| اسم ملف خاطئ لرقم غير عددي (`1+2`) | `unit_no` ليس رقمًا | استخدم `meta.file_name` |
| الغلاف بلون لا يناسب المرحلة | `stage` ناقص أو مكتوب بصيغة أخرى | اكتبه بالصيغة `"The third stage — الثالثة"` |
| اسم التدريسي مفقود من الغلاف | `instructor` غير موجود | أضفه وأعد البناء |
| رسالة `FONT LOAD ERRORS` | خط غير موجود في `fonts/` | تأكد من المسارات في رأس `style.css` |
| `node` لا يجد `playwright` | `NODE_PATH` غير مضبوط | المحرّك يضبطه بـ `npm root -g`؛ تأكد أن الحزمة مثبّتة عامًا |
| لا تنزّل Chromium من جديد | المتصفّح مثبّت مسبقًا في `/opt/pw-browsers` | لا تشغّل `playwright install` |
| صورة معادلة تظهر صغيرة جدًا | ارتفاع افتراضي `14mm` | مرّر `"h": "20mm"` في كتلة `eq` |
| خطأ `SyntaxError` في سكربت التوليد بعد تعديل | تحويل قائمة إلى نص أو العكس دون تعديل الأقواس | تأكد من تطابق `[` مع `]` و`(` مع `)` |

### مشاكل في التصميم مرّت سابقًا (للمعرفة)

- **الصفحات المرآة:** كانت الترويسة تختلف بين الصفحات الزوجية والفردية؛ ألغيت بطلب الفريق.
- **اسم التدريسي في الترويسة:** حُذف؛ يظهر في الغلاف فقط.
- **عبارة «ترجمة وتعديل الملازم» واسم المترجم الشخصي:** حُذفا نهائيًا.
- **الترجمة بعد كل النقاط:** صُحّح إلى ترجمة بعد **كل جملة** مباشرة.
- **الغلاف:** جُرّبت تصاميم عدّة، واعتُمد 1B نهائيًا كما في صورة الفريق.

---

## 19. الحفظ والرفع على Git

```bash
git add README.md <folder>
git commit -m "Add <Subject> lecture N

Co-Authored-By: ..."
git push -u origin <branch>
```

- لا يُرفع مجلد `.build/`.
- عند تغيير رقم محاضرة: استخدم `git mv` لإعادة تسمية المجلد، واحذف ملفات PDF القديمة، ثم أعد البناء.
- عند تعديل المحرّك أعد بناء الملازم المتأثّرة وتأكد من عدم وجود `overflow`.

---

## 20. مرجع سريع للأوامر

```bash
# بناء ملزمة
python3 bios-engine/bios.py <folder>/lecture.json

# بناء HTML فقط
python3 bios-engine/bios.py <folder>/lecture.json --html-only

# إعادة بناء كل الملازم
for f in */lecture.json; do python3 bios-engine/bios.py "$f"; done

# ثيم جديد
python3 bios-engine/make_theme.py NAME "#dark" "#mid" "#light" "Title"

# نص PDF
python3 -I -c "import pdfplumber; [print(p.extract_text()) for p in pdfplumber.open('x.pdf').pages]"

# صور صفحات PDF
pdftoppm -r 130 -png x.pdf pg/x

# PPTX → PDF
soffice --headless --convert-to pdf --outdir out x.pptx

# قائمة ملازم مرحلة معيّنة
for f in */lecture.json; do python3 -c "
import json,sys; m=json.load(open(sys.argv[1]))['meta']
if 'الثالثة' in (m.get('stage') or ''): print(m['subject_ar'], m['unit_ar'], m['title_ar'])" "$f"; done
```

---

## 21. قائمة الملازم المنجزة

### المرحلة الرابعة (ألوان `wineoat`، أسئلة في ملف منفصل)

| المجلد | المادة | المحاضرة |
|---|---|---|
| `lab1-biosafety` | بكتريا تشخيصية | عملي 1 |
| `bacteriology-lab2-specimens` | بكتريا تشخيصية | عملي 2 |
| `bacteriology-lab3-culture-media` | بكتريا تشخيصية | عملي 3 |
| `bloodbank-lec1-introduction` | نقل الدم | 1 |
| `bloodbank-lec2-donation-criteria` | نقل الدم | 2 |
| `bloodbank-lec3-services` | نقل الدم | 3 |
| `bloodbank-lec4-screening` | نقل الدم | 4 |
| `bloodbank-lec5-abo-rh` | نقل الدم | 5 |
| `clinimm-lec2-sle` | مناعة سريرية | نظري 2 — مدموجة مع الأسئلة |
| `clinimm-lec3-as-psa` | مناعة سريرية | نظري 3 — مدموجة مع الأسئلة |
| `clinimm-lec4-sjogren` | مناعة سريرية | نظري 4 |
| `clinimm-lec5-behcet` | مناعة سريرية | نظري 5 |
| `clinimm-lec6-celiac-pa-t1d` | مناعة سريرية | نظري 6 |
| `parasitology-week1-mcq` … `parasitology-week5-mcq` | طفيليات | بنوك أسئلة الأسابيع 1–5 — الحل تحت كل سؤال |
| `parasitology-lab4-solutions` | طفيليات | عملي 4 |
| `parasitology-week2-theory` … `parasitology-week5-theory` | طفيليات | نظري الأسابيع 2–5 — بدون أسئلة |
| `research-lec1-principles` | مبادئ البحث | 1 |
| `research-lec2-scientific-method` | مبادئ البحث | 2 |
| `research-lec3-research-plan` | مبادئ البحث | 3 — مدموجة مع الأسئلة |
| `enzymology-lab1-safety-tubes` | إنزيمات سريرية | عملي 1 |
| `enzymology-lec1-introduction` | إنزيمات سريرية | نظري 1 |
| `enzymology-lec2-kinetics-inhibition` | إنزيمات سريرية | نظري 2 |
| `pathology-lec1-2-atelectasis` | علم الأمراض | 1+2 |
| `pathology-lec3-chronic-bronchitis` | علم الأمراض | 3 |

### المرحلة الثالثة (ألوان `blush`، الأسئلة داخل الملزمة)

| المجلد | المادة | المحاضرة |
|---|---|---|
| `immunology-lab1-serology` | مناعة | عملي 1 |
| `advtech-lec1-elisa` | تقنيات متقدمة | نظري 1 |
| `advtech-lec3-ria` | تقنيات متقدمة | نظري 3 |
| `hematology-lab1-blood-collection` | أمراض الدم | عملي (جمع الدم) — رقمها بانتظار تأكيد |
| `hematology-practical-anticoagulants` | أمراض الدم | عملي 1 |
| `hematology-practical-normal-values` | أمراض الدم | عملي 3 |
| `hematology-practical-turbidimetry` | أمراض الدم | عملي 4 |
| `hematology-lec2…lec10-*` | أمراض الدم | نظري 2–10 |
| `genetics-lec1-cell-cycle-mitosis` | وراثة | نظري 1 |
| `immunology-lec1-introduction` | مناعة | نظري 1 |
| `immunology-lec2-cells-organs` | مناعة | نظري 2 |
| `immunology-lec3-antigens` | مناعة | نظري 3 |
| `histopathology-lab1-lab-safety` | أنسجة | عملي 1 |
| `histopathology-lab2-samples` | أنسجة | عملي 2 |
| `histopathology-lec1-acute-inflammation` | أنسجة | نظري 1 |
| `histopathology-lec2-chronic-inflammation` | أنسجة | نظري 2 |
| `histopathology-lec4-healing-regeneration` | أنسجة | نظري 4 |
| `virology-lab1-safety` | فايروسات | عملي 1 |

### بلا مرحلة

| المجلد | المادة | ملاحظة |
|---|---|---|
| `ethics-lec1-morals` | أخلاقيات المهنة | عربية فقط |
| `ethics-lec3-unethical-behavior` | أخلاقيات المهنة | محاضرة 3 — عربية فقط |
