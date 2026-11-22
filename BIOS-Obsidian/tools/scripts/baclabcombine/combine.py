import os, json
from pypdf import PdfWriter, PdfReader

# Diagnostic Microbiology practical (stage 4, د. هبة سامي) — merge the six comprehensive lab MCQ banks into one PDF,
# a bookmark per lab (each keeps its own cover and numbering; no rebuild). User 2026-11-22: "ادمجهن ملفات العملي وكل شكد مجموع الاسئله".
REPO = "/home/user/-"
parts = [
    ("bacteriology-lab1-mcq", "العملي 1 — القواعد ومستويات السلامة الحيوية"),
    ("bacteriology-lab2-mcq", "العملي 2 — اختيار العيّنات وجمعها ونقلها"),
    ("bacteriology-lab3-mcq", "العملي 3 — الأوساط الزرعية"),
    ("bacteriology-lab4-mcq", "العملي 4 — الطرق الميكروبيولوجية للتشخيص"),
    ("bacteriology-lab5-mcq", "العملي 5 — معالجة العيّنات والتصبيغ"),
    ("bacteriology-lab6-mcq", "العملي 6 — الفحوص الكيميائية الحيوية"),
]
writer = PdfWriter(); cur = 0; total_q = 0; total_img = 0
for folder, title in parts:
    d = os.path.join(REPO, folder)
    j = json.load(open(os.path.join(d, "lecture.json")))
    qs = [q for q in j["questions"]["mcq"] if "answer" in q]
    nq = len(qs); ni = sum(1 for q in qs if q.get("img")); total_q += nq; total_img += ni
    r = PdfReader(os.path.join(d, j["meta"]["file_name"] + ".pdf"))
    writer.append(r); writer.add_outline_item(f"{title} ({nq} سؤالًا)", cur)
    print(f"{title}: {nq} Q ({ni} pictures), {len(r.pages)} pages @ {cur+1}"); cur += len(r.pages)
out_dir = os.path.join(REPO, "bacteriology-lab-mcq-combined"); os.makedirs(out_dir, exist_ok=True)
out = os.path.join(out_dir, "BIOS - بكتريا عملي - بنك الأسئلة الشامل بالصور (العملي 1-6).pdf")
with open(out, "wb") as f: writer.write(f)
print("TOTAL questions:", total_q, "| picture questions:", total_img, "| pages:", cur); print(out)
