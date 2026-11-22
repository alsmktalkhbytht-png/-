import json, os, re, difflib, copy

# User 2026-11-22: the «2024» file (76 Q, bacteriology-mcq-2024-lec1-9) vs the merged theory file (315 Q) — keep only the 2024
# questions NOT already in the 315 (text-similarity ratio < 0.8 against every one of the 315 stems → 39 Q), MCQ only (no notes),
# appended at the end of the merged file with a note. L1–L9 topic headings kept. Fixes: Q63 was unsolved → A (Enriched media);
# Q24 key D → E (All of the above: the lecture also counts environmental factors).
REPO = "/home/user/-"
clean = lambda s: " ".join(re.sub(r"[^a-z0-9 ]", " ", re.sub(r"<[^>]+>|__|`", "", s.lower())).split())
base = []
for f in ["bacteriology-lec1-mcq", "bacteriology-lec2-mcq", "bacteriology-lec3-5-mcq", "bacteriology-lec6-mcq", "bacteriology-lec7-9-mcq", "bacteriology-adnan-exams-mcq"]:
    base += [clean(q["en"]) for q in json.load(open(f"{REPO}/{f}/lecture.json"))["questions"]["mcq"] if "options" in q]
src = json.load(open(f"{REPO}/bacteriology-mcq-2024-lec1-9/lecture.json"))
out, topic, n = [], None, 0
for q in src["questions"]["mcq"]:
    if "options" not in q: topic = q; continue
    n += 1; s = clean(q["en"])
    dup = any(abs(len(s) - len(b)) <= 0.5 * max(len(s), len(b)) and difflib.SequenceMatcher(None, s, b).ratio() >= 0.8 for b in base)
    if dup: continue
    q = copy.deepcopy(q); q.pop("note_en", None); q.pop("note_ar", None)
    if n == 63: q["answer"] = "a"
    if n == 24: q["answer"] = "e"
    if topic is not None: out.append(topic); topic = None
    out.append(q)
nq = sum(1 for q in out if "options" in q)
meta = dict(src["meta"], unit_en="2024 extra", unit_ar="إضافية 2024", unit_no="24+",
            title_en="Extra Questions from the 2024 File (not repeated)", title_ar="أسئلة إضافية من ملف 2024 (غير مكرَّرة)",
            file_name="BIOS - بكتريا نظري - أسئلة إضافية من ملف 2024", instructor="د. عدنان")
Qs = {"title_en": "Extra 2024 Questions — MCQ", "title_ar": "أسئلة 2024 الإضافية — اختيار",
      "answers_inline": True, "compact": True, "mcq_per_page": 5,
      "mcq_en": "Extra questions — 2024 file", "mcq_ar": "أسئلة إضافية — ملف 2024",
      "intro_en": ["Note: these questions are from the 2024 questions file (lectures 1–9) and are NOT repeated in the previous parts of this file.",
                   "Choose the correct answer; the answer sits under each question."],
      "intro_ar": ["ملاحظة: هذه الأسئلة من ملف أسئلة 2024 (المحاضرات 1–9)، وهي غير مكرَّرة في الأجزاء السابقة من هذا الملف.",
                   "اختر الإجابة الصحيحة؛ والحل تحت كل سؤال."],
      "mcq": out, "tf": [], "traps": [], "important": []}
d = f"{REPO}/bacteriology-2024-extra-mcq"; os.makedirs(d, exist_ok=True)
json.dump({"meta": meta, "questions": Qs}, open(d + "/lecture.json", "w"), ensure_ascii=False, indent=1)
print("extra questions:", nq)
