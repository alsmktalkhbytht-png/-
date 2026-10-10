# BIOS handouts

Bilingual (English + Arabic) handouts in the BIOS style.

- `bios-engine/` — the engine (style, colour themes — wineoat (option 10) by default — fonts, logo, pagination, PDF rendering).
- `lab1-biosafety/` — Diagnostic Microbiology Lab 1, the reference handout: `lecture.json` is the content, the PDFs are the output.
- `immunology-lab1-serology/` — Practical Immunology Lab 1.
- `parasitology-week1-mcq/` — Diagnostic Parasitology MCQ bank, week 1.
- `bloodbank-lec1-introduction/` — Blood Transfusion (نقل الدم) lecture 1: Introduction to blood banking + Practical 1.
- `bloodbank-lec2-donation-criteria/` — Blood Transfusion lecture 2: Criteria of blood donation.
- `bloodbank-lec3-services/` — Blood Transfusion lecture 3: Blood bank services.
- `research-lec1-principles/` — Principles of Research (مبادئ البحث العلمي) lecture 1.
- `research-lec2-scientific-method/` — Principles of Research lecture 2: the scientific method.
- `enzymology-lab1-safety-tubes/` — Clinical Enzymology (الإنزيمات السريرية) Lab 1: lab safety and blood collecting tubes.
- `ethics-lec1-morals/` — Professional Ethics (أخلاقيات المهنة) lecture 1 — Arabic-only handout.
- `pathology-lec1-2-atelectasis/` — Pathology (علم الأمراض) lectures 1+2: atelectasis, acute lung injury/ARDS, emphysema.
- `pathology-lec3-chronic-bronchitis/` — Pathology lecture 3: chronic bronchitis and asthma.
- `enzymology-lec1-introduction/` — Clinical Enzymology lecture 1: introduction, classification, properties, units, factors.
- `enzymology-lec2-kinetics-inhibition/` — Clinical Enzymology lecture 2: Michaelis-Menten, Lineweaver-Burke, inhibition.
- `advtech-lec1-elisa/` — Advanced Techniques (التقنيات المتقدمة) lecture 1: ELISA — third stage (pink, questions inside).
- `hematology-lab1-blood-collection/` — Hematology (أمراض الدم) practical lab 1: blood collection — third stage.
- `genetics-lec1-cell-cycle-mitosis/` — Genetics (علم الوراثة) lecture 1: cell cycle and mitosis — third stage.
- `.claude/skills/bios-malzama/SKILL.md` — how to make a new handout and the full `lecture.json` format.

Build a handout:

```bash
python3 bios-engine/bios.py lab1-biosafety/lecture.json
```
