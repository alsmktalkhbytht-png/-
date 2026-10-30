---
source: BIOS-Obsidian/tools/scripts/pat/fix1.py
handouts: []
saved: 2026-10-30
tags: [bios, code]
---
# pat/fix1.py

Utility script.

```python
s=open('make12.py').read()
def rep(a,b):
    global s
    assert s.count(a)==1, (s.count(a),a[:70]); s=s.replace(a,b)
rep('h="78mm"),','h="70mm"),')
rep('''    "The latter **synthesize pulmonary surfactant** and are the main cell type involved in **repair** of alveolar epithelium after damage to type I pneumocytes.",
    "The alveolar walls''','''    "The latter **synthesize pulmonary surfactant** and are the main cell type involved in **repair** of alveolar epithelium after damage to type I pneumocytes."],
   ["تحتوي **ظهارة الأسناخ** على طبقة متصلة من نوعين رئيسين من الخلايا: **الخلايا الرئوية من النوع الأول** المسطّحة الصفيحية التي تغطي **95%** من سطح الأسناخ، و**الخلايا الرئوية من النوع الثاني** المستديرة.",
    "وهذه الأخيرة **تصنع المادة الفاعلة بالسطح الرئوية** (`surfactant`)، وهي النوع الرئيس من الخلايا المسؤول عن **إصلاح** ظهارة الأسناخ بعد تضرّر خلايا النوع الأول."]),
 C(["The alveolar walls''')
rep('''   ["تحتوي **ظهارة الأسناخ** على طبقة متصلة من نوعين رئيسين من الخلايا: **الخلايا الرئوية من النوع الأول** المسطّحة الصفيحية التي تغطي **95%** من سطح الأسناخ، و**الخلايا الرئوية من النوع الثاني** المستديرة.",
    "وهذه الأخيرة **تصنع المادة الفاعلة بالسطح الرئوية** (`surfactant`)، وهي النوع الرئيس من الخلايا المسؤول عن **إصلاح** ظهارة الأسناخ بعد تضرّر خلايا النوع الأول.",
    "وجدران''','''   ["وجدران''')
rep('''an example of **non-cardiogenic pulmonary edema**.",
    "Acute lung injury can progress''','''an example of **non-cardiogenic pulmonary edema**.",
   "لأن الارتشاحات الرئوية في إصابة الرئة الحادة تنتج عادةً عن **تضرّر الغشاء الشعري السنخي** وليس عن عجز القلب الأيسر، فإن هذه التجمّعات تمثّل مثالًا على **الوذمة الرئوية غير القلبية المنشأ**."),
 C("Acute lung injury can progress''')
rep('''   ["لأن الارتشاحات الرئوية في إصابة الرئة الحادة تنتج عادةً عن **تضرّر الغشاء الشعري السنخي** وليس عن عجز القلب الأيسر، فإن هذه التجمّعات تمثّل مثالًا على **الوذمة الرئوية غير القلبية المنشأ**.",
    "ويمكن''','''   "ويمكن''')
rep('''**متلازمة الضائقة التنفسية الحادة**."]),''','''**متلازمة الضائقة التنفسية الحادة**."),''')
rep('h="40mm", fit="cover", keep=True','h="40mm", fit="cover"')
rep('''of the initiating insult.",
    "With improvements''','''of the initiating insult.",
   "يصاب نحو **85%** من المرضى بالمتلازمة السريرية لإصابة الرئة الحادة أو `ARDS` **خلال 72 ساعة** من الأذى المُحدِث."),
 C("With improvements''')
rep('''   ["يصاب نحو **85%** من المرضى بالمتلازمة السريرية لإصابة الرئة الحادة أو `ARDS` **خلال 72 ساعة** من الأذى المُحدِث.",
    "ومع تحسّن''','''   "ومع تحسّن''')
rep('''**من 60% إلى 40%** في العقد الأخير."]),''','''**من 60% إلى 40%** في العقد الأخير."),''')
open('make12.py','w').write(s)

```
