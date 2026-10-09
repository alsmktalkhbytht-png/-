# BIOS handouts

Bilingual (English + Arabic) handouts in the BIOS style.

- `bios-engine/` — the engine (style, fonts, logo, pagination, PDF rendering).
- `lab1-biosafety/` — Diagnostic Microbiology Lab 1 (knight theme), the reference handout: `lecture.json` is the content, the PDFs are the output.
- `immunology-lab1-serology/` — Practical Immunology Lab 1 (rose theme).
- `.claude/skills/bios-malzama/SKILL.md` — how to make a new handout and the full `lecture.json` format.

Build a handout:

```bash
python3 bios-engine/bios.py lab1-biosafety/lecture.json
```
