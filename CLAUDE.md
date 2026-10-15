# BIOS handouts — read this first

This repository builds BIOS (Telegram @BIOS0t) bilingual English/Arabic lecture handouts (ملازم).

## Trigger

Whenever the user writes «ترجم المحاضرة» or «ترجم الملزمة» (or «سوّي ملزمة», «طبق عليه», ملزمة/ملازم),
or uploads a lecture file (PDF / PPTX / DOCX), **before doing anything else** read the Obsidian memory vault
`obsidian-memory/` in this order and apply it exactly:

1. `obsidian-memory/00 - ابدأ هنا.md` (index)
2. `obsidian-memory/01 - القواعد الذهبية.md` — scientific content is untouchable: copy every sentence verbatim,
   translate every sentence; never shorten, never add content, tables, diagrams or explanations that are not in the source.
3. `obsidian-memory/02 - الألوان والمراحل.md` — third stage → `blush` (questions inside); fourth stage → `wineoat`
   = «النموذج العاشر» (questions in a separate file). Decided by `meta.stage`.
4. Then 03–12 (naming, workflow, generator template, extraction, questions, QA, subjects/instructors, log, engine, reply style).

Then also follow `.claude/skills/bios-malzama/SKILL.md` and `docs/BIOS_ENGINE_GUIDE.md`.

## After each handout

Update `obsidian-memory/10 - سجل الملازم المنجزة.md` (and `09` if a new subject/instructor appears),
save the generator as `<folder>/make.py`, update `README.md`, commit and push.

## Replies

Reply in Arabic; put every English word on its own line (user preference).
