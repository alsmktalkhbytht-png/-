import os, json
from pypdf import PdfWriter, PdfReader

# Diagnostic Microbiology THEORY (stage 4, د. عدنان) — merge the theory MCQ banks (MCQ only, no explanations) into one PDF,
# a bookmark per part (each keeps its own cover and numbering). User 2026-11-22: "اجمعهن بملف واحد و شكد عدد الأسئلة".
REPO = "/home/user/-"
parts = [
    ("bacteriology-lec1-mcq", "المحاضرة 1 — الغرض والفلسفة"),
    ("bacteriology-lec2-mcq", "المحاضرة 2 — السلامة المختبرية"),
    ("bacteriology-lec3-5-mcq", "المحاضرات 3–5 — اختيار العيّنات وجمعها ونقلها"),
    ("bacteriology-lec6-mcq", "المحاضرة 6 — الأوساط الزراعية"),
    ("bacteriology-lec7-9-mcq", "المحاضرات 7–9 — طرق التشخيص"),
]
writer = PdfWriter(); cur = 0; total_q = 0
for folder, title in parts:
    d = os.path.join(REPO, folder)
    j = json.load(open(os.path.join(d, "lecture.json")))
    nq = sum(1 for q in j["questions"]["mcq"] if "answer" in q); total_q += nq
    r = PdfReader(os.path.join(d, j["meta"]["file_name"] + ".pdf"))
    writer.append(r); writer.add_outline_item(f"{title} ({nq} سؤالًا)", cur)
    print(f"{title}: {nq} Q, {len(r.pages)} pages @ {cur+1}"); cur += len(r.pages)
out_dir = os.path.join(REPO, "bacteriology-theory-mcq-combined"); os.makedirs(out_dir, exist_ok=True)
out = os.path.join(out_dir, "BIOS - بكتريا نظري - أسئلة MCQ (المحاضرات 1-9).pdf")
with open(out, "wb") as f: writer.write(f)
print("TOTAL questions:", total_q, "| pages:", cur); print(out)
