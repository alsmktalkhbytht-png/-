import sys, os, json
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
WORK = "/home/claude/scratch/work"; sys.path.insert(0, WORK)
from bidi import ltr_all
import d1, d2, d3, d4

# Diagnostic Microbiology (stage 4) — «MCQ 2024» compiled file (Yassin Falah; 75 scanned pages, lectures 1–13 + 2023 exam rounds).
# User 2026-11-22: "لحد صفحه ٢٤ — محاضره ١٢ و١٣ ما اريدهن" → the file's printed pages 1–24 = lectures 1, 2, 3-4-5, 6, 7-8-9.
# Professor-file pattern: verbatim English (typos kept, noted only when they matter), every option translated, the highlighted
# answer under each question (answers_inline), no balance (file order), past-exam tags kept. Unsolved → engine flag + BIOS note.
mcq = d1.D + d2.D + d3.D + d4.D
qs = [q for q in mcq if "topic_en" not in q]
print("questions:", len(qs), "| answers:", dict(Counter(q.get("answer") for q in qs)), "| notes:", sum(1 for q in qs if "note_en" in q))

meta = {
 "subject_en": "Diagnostic Microbiology", "subject_ar": "الأحياء المجهرية التشخيصية", "short_ar": "بكتريا",
 "unit_en": "Lectures 1–9", "unit_ar": "المحاضرات 1–9", "unit_label": "LEC", "unit_no": "1-9",
 "title_en": "MCQ 2024 — Lectures 1 to 9", "title_ar": "أسئلة بكتريا 2024 — المحاضرات 1 إلى 9",
 "department": "قسم التحليلات", "stage": "The fourth stage — الرابعة",
 "kind": "Theory — نظري", "questions_kind": "MCQ — أسئلة اختيار",
 "file_name": "BIOS - بكتريا نظري - أسئلة 2024 (المحاضرات 1-9)",
}
questions = {
 "title_en": meta["title_en"], "title_ar": meta["title_ar"],
 "sub": "MCQ", "answers_inline": True, "compact": True, "mcq_per_page": 5,
 "mcq_en": "MCQ 2024 — lectures 1 to 9", "mcq_ar": "أسئلة الاختيار 2024 — المحاضرات 1 إلى 9",
 "intro_en": ["Choose the correct answer.",
              "The answer under each question is the one highlighted in the source file; questions from the 2023 exams carry their round. A BIOS note flags any question that is unsolved or whose answer is doubtful."],
 "intro_ar": ["اختر الإجابة الصحيحة.",
              "الحل تحت كل سؤال هو المظلَّل في الملف الأصلي، وأسئلة امتحانات 2023 معلَّمة بدورها. وملاحظة BIOS تنبّه على أي سؤال غير محلول أو حلّه مشكوك فيه."],
 "mcq": ltr_all(mcq),
}
out = "/home/user/-/bacteriology-mcq-2024-lec1-9/lecture.json"
os.makedirs(os.path.dirname(out), exist_ok=True)
json.dump({"meta": meta, "questions": questions}, open(out, "w"), ensure_ascii=False, indent=1)
print("wrote", out)
