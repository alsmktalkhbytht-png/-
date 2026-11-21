import os, json
from pypdf import PdfWriter, PdfReader

# Professional Ethics (stage 4, د. نور) — merge the five comprehensive MCQ banks into one PDF, a bookmark per lecture
# (each keeps its own cover and numbering; no rebuild). User 2026-11-21: "اجمعهنن بملف واحد واطيني العدد النهائي".
REPO = "/home/user/-"
parts = [
    ("ethics-lec1-mcq", "المحاضرة 1 — الأخلاق والقيم الأخلاقية"),
    ("ethics-lec2-mcq", "المحاضرة 2 — أخلاقيات العمل في المختبرات الطبية"),
    ("ethics-lec3-mcq", "المحاضرة 3 — أنماط السلوك غير الأخلاقي"),
    ("ethics-lec4-mcq", "المحاضرة 4 — الغش في العمل المختبري"),
    ("ethics-lec5-mcq", "المحاضرة 5 — ترسيخ قيم أخلاقيات المهنة"),
]
writer = PdfWriter(); cur = 0; total_q = 0
for folder, title in parts:
    d = os.path.join(REPO, folder)
    j = json.load(open(os.path.join(d, "lecture.json")))
    nq = sum(1 for q in j["questions"]["mcq"] if "answer" in q); total_q += nq
    r = PdfReader(os.path.join(d, j["meta"]["file_name"] + ".pdf"))
    writer.append(r); writer.add_outline_item(f"{title} ({nq} سؤالًا)", cur)
    print(f"{title}: {nq} Q, {len(r.pages)} pages @ {cur+1}"); cur += len(r.pages)
out_dir = os.path.join(REPO, "ethics-mcq-combined"); os.makedirs(out_dir, exist_ok=True)
out = os.path.join(out_dir, "BIOS - أخلاقيات المهنة نظري - بنك الأسئلة الشامل (المحاضرات 1-5).pdf")
with open(out, "wb") as f: writer.write(f)
print("TOTAL questions:", total_q, "| pages:", cur); print(out)
