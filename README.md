# BIOS handouts

Bilingual (English + Arabic) handouts in the BIOS style.

- `bios-engine/` — the engine (style, fonts, logo, pagination, PDF rendering).
- `lab1-biosafety/` — Lab 1, the reference handout: `lecture.json` is the content, the PDFs are the output.
- `.claude/skills/bios-malzama/SKILL.md` — how to make a new handout and the full `lecture.json` format.

Build a handout:

```bash
python3 bios-engine/bios.py lab1-biosafety/lecture.json
```
