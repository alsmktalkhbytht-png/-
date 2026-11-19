import os
from pypdf import PdfWriter, PdfReader

REPO = "/home/user/dash-repo"
parts = [
    ("parasitology-week1-mcq",   "BIOS - طفيليات نظري الأسبوع الأول - الأسئلة.pdf",            "الأسبوع 1 — المصطلحات"),
    ("parasitology-week2-mcq",   "BIOS - طفيليات نظري الأسبوع الثاني - الأسئلة.pdf",           "الأسبوع 2 — الأوالي"),
    ("parasitology-week3-mcq",   "BIOS - طفيليات نظري الأسبوع الثالث - الأسئلة.pdf",           "الأسبوع 3 — الأميبا الحالّة للنسيج"),
    ("parasitology-week4-mcq",   "BIOS - طفيليات نظري الأسبوع الرابع - الأسئلة.pdf",           "الأسبوع 4 — الأميبات غير الممرضة"),
    ("parasitology-week5-mcq",   "BIOS - طفيليات نظري الأسبوع الخامس - الأسئلة.pdf",           "الأسبوع 5 — الأميبات حرّة المعيشة"),
    ("parasitology-week6-7-mcq", "BIOS - طفيليات نظري الأسبوعان السادس والسابع - الأسئلة.pdf", "الأسبوعان 6–7 — السوطيات المعوية والتناسلية"),
    ("parasitology-week8-mcq",   "BIOS - طفيليات نظري الأسبوع الثامن - الأسئلة.pdf",           "الأسبوع 8 — المثقبيات (Trypanosoma)"),
    ("parasitology-week9-mcq",   "BIOS - طفيليات نظري الأسبوع التاسع - الأسئلة.pdf",           "الأسبوع 9 — الليشمانيا (Leishmania)"),
]

writer = PdfWriter()
page_cursor = 0
for folder, fname, title in parts:
    path = os.path.join(REPO, folder, fname)
    r = PdfReader(path)
    n = len(r.pages)
    writer.append(r)
    writer.add_outline_item(title, page_cursor)   # bookmark -> this week's cover
    print(f"{title}: {n} pages @ page {page_cursor+1}")
    page_cursor += n

out_dir = os.path.join(REPO, "parasitology-mcq-combined")
os.makedirs(out_dir, exist_ok=True)
out = os.path.join(out_dir, "BIOS - طفيليات نظري - بنك الأسئلة (المحاضرات 1-9).pdf")
with open(out, "wb") as f:
    writer.write(f)
print("TOTAL pages:", page_cursor)
print("wrote", out)
