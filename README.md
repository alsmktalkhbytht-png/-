# BIOS handouts

Bilingual (English + Arabic) handouts in the BIOS style.

- `bios-engine/` — the engine (style, colour themes — wineoat (option 10) by default — fonts, logo, pagination, PDF rendering).
- `lab1-biosafety/` — Diagnostic Microbiology Lab 1, the reference handout: `lecture.json` is the content, the PDFs are the output.
- `immunology-lec1-introduction/` — Immunology theory lecture 1: Introduction to Human Immunology (د. أحمد داود) — third stage.
- `immunology-lec2-cells-organs/` — Immunology theory lecture 2: Cells, Organs, and Defense (د. أحمد داود) — third stage.
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
- `advtech-lec3-ria/` — Advanced Techniques lecture 3: Radioimmunoassay (RIA) — third stage.
- `hematology-lab1-blood-collection/` — Hematology (أمراض الدم) practical lab 1: blood collection — third stage.
- `genetics-lec1-cell-cycle-mitosis/` — Genetics (علم الوراثة) lecture 1: cell cycle and mitosis — third stage.
- `hematology-lec2…lec7-*/` — Hematology theory (د. مازن اللهيبي) lectures 2–7: blood cell formation, blood elements, hemoglobin, anaemia, iron deficiency, chronic/sideroblastic — third stage.
- `histopathology-lab1-lab-safety/`, `histopathology-lab2-samples/` — Histopathology (علم الأمراض النسيجية) practical labs 1–2 — third stage.
- `hematology-practical-anticoagulants/` (lab 1), `hematology-practical-normal-values/` (lab 2) — Hematology practical (ليندا منجد هادي) — third stage.
- `histopathology-lec1-acute-inflammation/` — Histopathology theory lecture 1 (د. حامد خليل التميمي) — third stage.
- `histopathology-lec2-chronic-inflammation/` — Histopathology theory lecture 2 (د. حامد خليل التميمي) — third stage.
- `histopathology-lec4-healing-regeneration/` — Histopathology theory lecture 4 (د. حامد خليل التميمي) — third stage.
- `virology-lab1-safety/` — Medical Virology practical lab 1: safety and aseptic techniques — third stage.
- `bacteriology-lab2-specimens/`, `bacteriology-lab3-culture-media/` — Diagnostic Microbiology practical labs 2 and 3 (د. هبة سامي) — fourth stage.
- `docs/BIOS_ENGINE_GUIDE.md` — full documentation (Arabic): design, workflow, code, troubleshooting.
- `.claude/skills/bios-malzama/SKILL.md` — how to make a new handout and the full `lecture.json` format.

Build a handout:

```bash
python3 bios-engine/bios.py lab1-biosafety/lecture.json
```
