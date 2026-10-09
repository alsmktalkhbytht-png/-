---
name: bios-malzama
description: Build a BIOS-style bilingual (English + Arabic) handout PDF — and its matching question-bank PDF — from a lecture or lab PDF. Use whenever the user uploads a lecture/lab PDF and asks for a ملزمة / ملازم / "طبق عليه" / "مثل هذا النمط", or wants a new handout in the same style as Lab 1 (lab1-biosafety/). This style replaces the generic .docx malzama for this repository.
---

# BIOS handout (ملزمة) — house style

## Look (agreed with the BIOS team — do not change without being asked)

- **Three colours only:** Black Bean `#2e272a`, Star White `#d7cfbb`, Egret `#efefe8`
  (plus white paper). They are the CSS variables `--dark`, `--star`, `--egret` in
  `bios-engine/style.css`; never add another colour.
- **Every page has the same header and footer** (no mirrored odd/even pages).
- **Header:** `Lab 1` pill (English only), subject in the centre (no instructor
  name — the instructor appears on the cover only), `BIOS` pill on its own.
- **Footer:** only the Telegram handle, page number always on the right.
- **Right margin:** one vertical rule carrying `BIOS · TELEGRAM · BIOS0t`; no left rule.
- No "ترجمة وتعديل الملازم" / "Lecture translation" text anywhere — BIOS also does
  explanations, exams and summaries. The cover logo is `brand/logo_mono.jpg`
  (recoloured to the palette, tagline removed).

Every handout in this repo uses one engine: `bios-engine/bios.py`. You never write HTML
or CSS for a new lecture. You only write **one JSON file** per lecture, and the engine
produces the cover, the alternating headers and footers, the EN/AR cards, figures, tables,
automatic pagination, and the question bank. The reference result is `lab1-biosafety/`.

## Pipeline

1. **Make the lecture folder** next to `lab1-biosafety/`, for example `lab2-sterilization/`,
   with an `assets/` subfolder.
2. **Read the source PDF** (Read tool; for image-only slides render pages with
   `pdftoppm -r 150 -png` and read them visually). Extract every diagram or photo into
   `assets/` (`pdfimages -j`, or `pdftoppm` and crop with PIL).
3. **Write `lecture.json`** using the schema below. Start from
   `lab1-biosafety/lecture.json` as the worked example.
4. **Build:** `python3 bios-engine/bios.py <folder>/lecture.json`
   This writes `<folder>/BIOS - <Subject> - <Unit>.pdf` (plus `... - Questions.pdf` when
   `questions` exists) and one PNG per page in `<folder>/.build/*-pages/`.
5. **Look at the page PNGs** (contact sheet with PIL) and fix anything odd: an overflow
   line in the build output, a wrongly cropped figure, a bad line break. Rebuild.
6. **Send both PDFs** with SendUserFile, then commit the folder (not `.build/`) and push.

## Content rules (non-negotiable)

- **English is copied verbatim** from the source: same words, typos, punctuation and
  capitalisation. Do not fix grammar. Text cut off in the source → end with `[[cut]]`
  in English and `[[قطع]]` in Arabic.
- **Arabic** is accurate, natural academic Arabic. In a definition, put the English term
  in backticks after the Arabic one: `**التعقيم (`Sterilization`):** …`.
- Scientific names: `__E. coli__` (bold italic). Inside Arabic wrap them in backticks:
  `` `__E. coli__` ``.
- Emphasise what an exam would ask about with `**…**` in both languages — sparingly.
- Every figure gets a bilingual caption. Figures are numbered automatically.

## Inline markup

| Markup | Result |
|---|---|
| `**text**` | burgundy bold term |
| `*text*` | italic |
| `__text__` | bold italic (species names) |
| `` `text` `` | left-to-right run inside Arabic (English terms, species) |
| `^^text^^` | bold mark (for example a `*` footnote marker in a table) |
| `[[cut]]` / `[[قطع]]` | yellow "text cut off in the original file" tag |

## lecture.json schema

```json
{
  "meta": {
    "subject_en": "Diagnostic Microbiology", "subject_ar": "الأحياء المجهرية التشخيصية",
    "instructor": "د. ذهب",
    "unit_en": "Lab 2", "unit_ar": "العملي 2", "unit_label": "LAB", "unit_no": "2",
    "title_en": "…", "title_ar": "…",
    "department": "قسم التحليلات", "stage": "The fourth stage — الرابعة",
    "kind": "Laboratories — عملي", "translator": "محمد حامد"
  },
  "blocks": [ … ],
  "questions": { … }
}
```

For a theory lecture use `"unit_en": "Lecture 3"`, `"unit_ar": "المحاضرة 3"`,
`"unit_label": "LECTURE"`, `"kind": "Theory — نظري"`. Optional meta keys (defaults in
`bios.py`): `brand`, `telegram`, `instructor_label_ar`, `questions_kind`, `file_name`.
`unit_ar` is optional and not printed (the header shows `unit_en` only).

### Blocks

| `t` | Fields | Use for |
|---|---|---|
| `section` | `en`, `ar` | slide title → numbered sage bar (auto 1, 2, 3…) |
| `h2` | `en`, `ar` | sub-heading inside a section |
| `card` | `en`, `ar`, optional `list_en`, `list_ar` | paragraph, definition, or an intro line followed by a numbered list |
| `rule` | `en`, `ar` | numbered instruction/step; numbering restarts at each section |
| `group` | `title_en`, `title_ar`, optional `sub_en`, `sub_ar`, `en`, `ar`, optional `style: "light"` | a classified item with a dark header bar (risk groups, types, stages); `light` gives a Star White bar |
| `figure` | `src` (relative to the lecture folder), `en`, `ar`, optional `h` + `fit` ("cover"/"contain") or `width` | one figure |
| `figure` | `symbols: ["biohazard", "radiation"]`, `en`, `ar` | the redrawn vector warning signs |
| `figures` | `items: [figure, figure]` | two figures side by side |
| `side` | `blocks: [card…]`, `figure` | cards with a small figure in a 34 mm column on the right |
| `table` | `head`, `rows`, optional `ar_cols`, `key_cols`, `widths`, `numbered`, `style: "summary"`, `label_en`, `label_ar` | tables; `summary` puts it in the sage box with a pill label |
| `note` | `en`, `ar`, optional `label: ["Note", "ملاحظة"]` | remark, warning, or clinical note |
| `spacer` | `h` (for example `"2mm"`) | small vertical gap |
| `pagebreak` | — | force a new page (rarely needed) |
| `html` | `html` | escape hatch for a one-off layout |

Any block can take `"keep": true` to stay on the same page as the block after it — use it
on a figure that is explained by the table or list right after it.

### Questions (optional — produces the second PDF)

```json
"questions": {
  "mcq":       [{"en": "…", "ar": "…", "options": [["en", "ar"], …4], "answer": "c"}],
  "tf":        [{"en": "…", "ar": "…", "answer": "T"}],
  "traps":     [{"en": "…", "ar": "…", "answer_en": "…", "answer_ar": "…"}],
  "important": [{"en": "…", "ar": "…", "answer_en": "…", "answer_ar": "…"}]
}
```

Write questions from the lecture content only: about 25–35 MCQs covering every section,
12–16 true/false, 6–8 traps (details students mix up), and 6–8 essay questions with
model answers. Spread the correct MCQ letters evenly across a–d.

## Requirements

Python 3, Node with the global `playwright` package (preinstalled in cloud sessions;
the engine sets `NODE_PATH` itself), and Chromium. Fonts and the BIOS logo are bundled in
`bios-engine/`.
