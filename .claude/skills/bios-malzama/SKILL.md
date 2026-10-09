---
name: bios-malzama
description: Build a BIOS-style bilingual (English + Arabic) handout PDF — and its matching question-bank PDF — from a lecture or lab PDF. Use whenever the user uploads a lecture/lab PDF and asks for a ملزمة / ملازم / "طبق عليه" / "مثل هذا النمط", or wants a new handout in the same style as Lab 1 (lab1-biosafety/). This style replaces the generic .docx malzama for this repository.
---

# BIOS handout (ملزمة) — house style

## Look (agreed with the BIOS team — do not change without being asked)

- **Colour themes:** set `"theme"` in `meta`. Each theme is one file in
  `bios-engine/themes/` (CSS variables only) plus a recoloured cover logo
  `bios-engine/brand/logo_<theme>.jpg`. Never hard-code a colour in a lecture.
  - `knight`: navy, gold, crimson, parchment, ink.
  - `nightfall` (trial, used by `lab1-biosafety/`): Nightfall Serenity — `#444152`,
    `#8E8AA5`, `#CBCAD0`, `#E4E4E6`; key terms are underlined instead of coloured.
  - `plum` (**default for every handout**, chosen by the team): `#3F2537`, `#EFCAD0`, `#FFF1F3`;
    key terms underlined in pink.
  - Calm three-colour trials made with `bios-engine/make_theme.py` (dark text/bars, soft mid
    accent, very light panels — nothing else): `sage` (slate `#2F3E46`, sage `#A3B8A8`,
    `#F0F4F1`), `mist` (ink blue `#2B3A4A`, mist `#A9BCCF`, `#EFF3F7`), `sand` (charcoal
    `#3D3833`, sand `#C9B79C`, `#F6F2EC`). New palettes: `python3 bios-engine/make_theme.py
    NAME DARK MID LIGHT "Title"`.
  - `violet` (trial): Antique Gold `#B9A38B` + Deep Violet `#2C1F33`.
  - `oatmeal` (trial): Plum `#33022F` + Oatmeal `#D9C1A7`.
    Both are two-colour palettes; light surfaces are tints of the beige.
  - `blush` (trial, used by `immunology-lab1-serology/`): `#f9e9ef`, `#f2808f`, `#e8d6d0`,
    `#eebcc2`, plus a deep rose ink `#4a2a30` for text — the palette has no dark colour, so
    coral bars carry ink text and key terms are underlined in coral.
  - `rose` (earlier trial): Dark Raspberry `#89235B`,
    Electric Rose `#F10291`, Pastel Petal `#FFCAE4`, Snow `#FFF3F2`, Rich Mahogany `#250209`.
  To add a theme, copy a theme file, change the values, and recolour
  `brand/logo_full.jpg` the same way (dark ink → the theme's `--dark`, paper → `--egret`).
- **Cover credit:** the cover shows "Translation · ترجمة: بايوس" (meta `translation`, default
  `بايوس`). Never put a person's name as translator. `instructor` and `stage` are optional —
  leave them out when the source does not give them and the cover hides those boxes.
- **Arabic body text is 13 pt** (one step smaller than before); keep it there.
- **Sentence by sentence:** when a paragraph has more than one sentence, write `en` and
  `ar` as lists of sentences (same length). Each English sentence is then followed directly
  by its Arabic translation, and the text continues with the next sentence. Split only at
  real sentence ends — not at stray full stops inside a sentence (`patient's. particulars`)
  or abbreviations (`D.W.`, `spp.`, `e.g.`, `5 min.`). Works for `card`, `rule`, `group`
  and `note`.
- **Every listed point carries its own translation right after it** — never all English
  points followed by all Arabic points. Short pairs sit on one line (English left, Arabic
  right); long pairs stack with the Arabic underneath. MCQ options follow the same rule.
- **Every page has the same header and footer** (no mirrored odd/even pages).
- **Header:** `Lab 1` pill (English only), subject in the centre (no instructor
  name — the instructor appears on the cover only), `BIOS` pill on its own.
- **Footer:** only the Telegram handle, page number always on the right.
- **Right margin:** one vertical rule carrying `BIOS · TELEGRAM · BIOS0t`; no left rule.
- No "ترجمة وتعديل الملازم" / "Lecture translation" text anywhere — BIOS also does
  explanations, exams and summaries. The cover logo is `brand/logo_cover.jpg`
  (recoloured to the palette, tagline removed). The cover card says "Prepared by / إعداد".

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
    "instructor": "د. هبة سامي",
    "unit_en": "Lab 2", "unit_ar": "العملي 2", "unit_label": "LAB", "unit_no": "2",
    "title_en": "…", "title_ar": "…",
    "department": "قسم التحليلات", "stage": "The fourth stage — الرابعة",
    "kind": "Laboratories — عملي"
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
| `card` | `en`, `ar` (string, or list of sentences), optional `list_en`, `list_ar` (same length); leave `en` and `ar` empty for a list-only card | paragraph, definition, or an intro line followed by numbered points; point *n* of `list_en` is paired with point *n* of `list_ar` |
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

**Question bank from a professor's MCQ file** (no lecture text): leave out `blocks`; only
the question PDF is built and named after `meta.file_name`. Keep every question and option
verbatim and use the professor's marked answer (often bold/underlined — extract it with
`pdfplumber` font names). Extra keys:

- `questions.title_en/title_ar` (title band), `sub` (header pill, e.g. `"MCQ"`),
  `mcq_en/mcq_ar` (section bar), `intro_en/intro_ar` (instructions note).
- `{"topic_en": …, "topic_ar": …}` items inside `mcq` print a sub-heading between questions.
- Options can be 4 or 5 (shown A–E). If a marked answer contradicts standard references,
  keep it as the key and add `note_en/note_ar` to that question; the notes print under
  the answer key.

Write questions from the lecture content only: about 25–35 MCQs covering every section,
12–16 true/false, 6–8 traps (details students mix up), and 6–8 essay questions with
model answers. Spread the correct MCQ letters evenly across a–d.

## Requirements

Python 3, Node with the global `playwright` package (preinstalled in cloud sessions;
the engine sets `NODE_PATH` itself), and Chromium. Fonts and the BIOS logo are bundled in
`bios-engine/`.
