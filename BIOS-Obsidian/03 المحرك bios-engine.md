---
tags: [bios, engine]
---
# 03 المحرك bios-engine

كل ملزمة تُبنى من ملف واحد هو
`lecture.json`
والمحرك يصنع الغلاف والصفحات والجداول والأسئلة وملف
PDF
وصور الصفحات. الكود الكامل في [[Code/engine - bios.py]].

## البناء

```bash
cd bios-engine
python3 bios.py ../<folder>/lecture.json
# → <folder>/BIOS - ….pdf  (+ "… - الأسئلة.pdf" or merged)
# → <folder>/.build/booklet-pages/p00.png …   and   .build/questions-pages/
# prints "page N overflows by X mm" when a block is taller than the page (BODY_MM = 240)
```

## شكل الملف

```json
{
  "meta": {
    "subject_en": "Clinical Immunology", "subject_ar": "المناعة السريرية", "short_ar": "مناعة سريرية",
    "unit_en": "Lecture 6", "unit_ar": "المحاضرة 6", "unit_label": "LEC", "unit_no": "6",
    "title_en": "…", "title_ar": "…",
    "kind": "Theory — نظري", "stage": "The fourth stage — الرابعة", "instructor": "د. عبير",
    "department": "قسم التحليلات",
    "merge_questions": true,            // optional: questions inside the same PDF
    "file_name": "BIOS - … - دمج",      // optional: overrides the automatic Arabic name
    "arabic_only": true,                // optional: Arabic-only lectures (ethics)
    "theme": "wineoat"                  // optional: stage 3 → blush automatically
  },
  "blocks": [ … ],
  "questions": { "mcq": [], "tf": [], "traps": [], "important": [], "answers_inline": false }
}
```

## أنواع الكتل

```text
section  {en, ar}                         numbered bar
h2       {en, ar}                         sub-heading
card     {en, ar}  (string or sentence list) + optional list_en/list_ar, alpha
rule     {en, ar}                         numbered step (restarts per section)
note     {en, ar, label:[en, ar]}         remark / BIOS note / "In short" box
group    {title_en, title_ar, en, ar}     classified item with a dark bar
figure   {src, en, ar, h, fit}            numbered figure with bilingual caption
figures  {items:[figure, figure]}         two side by side
side     {blocks:[…], figure}             cards + small figure column
table    {head, rows, ar_cols, key_cols, widths, style:"summary", label_en, label_ar}
         cell = "text"  or  ["en", "ar"]   (bilingual cell, Arabic under English)
flow     {steps:[{en, ar}], en, ar}       arrow chain (row) or stacked (long steps)
eq, spacer, pagebreak, html
```

## العلامات داخل النص

```text
**bold term**      *italic*      __Species name__ (bold italic)
`LTR run`          inside Arabic keeps English left-to-right
^^mark^^           [[cut]] / [[قطع]]
```

## إضافات هذه المحادثة على المحرك

```text
2026-10  table cells and headers accept ["en", "ar"]          → cell()
2026-10  list points accept sentence lists                    → pairs()  (.prs wrapper)
2026-10  questions.answers_inline: answer line under each MCQ → inline_answer()
         + "⚠ Not solved in the source file" when answer is empty
         + BIOS note (note_en/note_ar) under the answer
         + Arabic side shows "B — النص العربي" (bdi-isolated)
CSS      .tc-ar  .prs  .qans  .qflag
```
