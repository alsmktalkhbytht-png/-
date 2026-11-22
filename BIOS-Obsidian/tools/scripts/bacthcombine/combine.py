import os, json, subprocess, html
from pypdf import PdfWriter, PdfReader

# Diagnostic Microbiology THEORY (stage 4, د. عدنان) — merge the theory MCQ banks + Dr. Adnan's past exams into one PDF,
# a bookmark per part, and a first "note" page saying where each part (and Dr. Adnan's exam questions) starts.
# User 2026-11-22: "اجمعهن بملف واحد و شكد عدد الأسئلة" then "ضيف هل اسئلة مال دكتور عدنان وخلي ملاحظه بالبداية ...".
REPO = "/home/user/-"; ENGINE = os.path.join(REPO, "bios-engine")
parts = [
    ("bacteriology-lec1-mcq", "المحاضرة 1 — الغرض والفلسفة"),
    ("bacteriology-lec2-mcq", "المحاضرة 2 — السلامة المختبرية"),
    ("bacteriology-lec3-5-mcq", "المحاضرات 3–5 — اختيار العيّنات وجمعها ونقلها"),
    ("bacteriology-lec6-mcq", "المحاضرة 6 — الأوساط الزراعية"),
    ("bacteriology-lec7-9-mcq", "المحاضرات 7–9 — طرق التشخيص"),
    ("bacteriology-adnan-exams-mcq", "أسئلة امتحانات د. عدنان (2025، 2023، 2022)"),
]
info = []; cur = 2; total_q = 0   # page 1 = note page
for folder, title in parts:
    d = os.path.join(REPO, folder)
    j = json.load(open(os.path.join(d, "lecture.json")))
    nq = sum(1 for q in j["questions"]["mcq"] if "answer" in q); total_q += nq
    pdf = os.path.join(d, j["meta"]["file_name"] + ".pdf"); n = len(PdfReader(pdf).pages)
    info.append((title, nq, cur, pdf)); print(f"{title}: {nq} Q, {n} pages @ {cur}"); cur += n
adnan_page = info[-1][2]
rows = "".join(f'<tr{" class=hl" if i == len(info)-1 else ""}><td>{html.escape(t)}</td><td>{nq}</td><td>{p}</td></tr>' for i, (t, nq, p, _) in enumerate(info))
page = f"""<!DOCTYPE html><html lang=ar dir=rtl><head><meta charset=utf-8><style>
@font-face{{font-family:Mada;src:url(file://{ENGINE}/fonts/Mada-Regular.ttf);font-weight:400}}
@font-face{{font-family:Mada;src:url(file://{ENGINE}/fonts/Mada-Bold.ttf);font-weight:700}}
@page{{size:A4;margin:0}} body{{margin:0;font-family:Mada;color:#3b1f27;background:#f6f1ea}}
.p{{width:210mm;height:297mm;box-sizing:border-box;padding:28mm 22mm;display:flex;flex-direction:column;gap:9mm}}
.brand{{font-size:30pt;font-weight:700;color:#5a2333;letter-spacing:1px}} h1{{font-size:20pt;margin:0}}
.note{{background:#5a2333;color:#fff;border-radius:6mm;padding:8mm 9mm;font-size:17pt;line-height:1.7;font-weight:700}}
.note b{{color:#f2d7a6;font-size:22pt}}
table{{border-collapse:collapse;width:100%;font-size:13pt}} td,th{{border-bottom:1px solid #d9c9b8;padding:3mm 2mm;text-align:right}}
th{{color:#5a2333}} tr.hl td{{background:#efe0c8;font-weight:700}} .tot{{font-size:14pt;font-weight:700}}
.foot{{margin-top:auto;font-size:11pt;color:#7a5a63}}
</style></head><body><div class=p>
<div class=brand>BIOS</div><h1>بكتريا نظري — أسئلة MCQ (المحاضرات 1–9) + أسئلة امتحانات د. عدنان</h1>
<div class=note>ملاحظة: أسئلة امتحانات الدكتور عدنان (2025، 2/12/2023، 2022) تبدأ من الصفحة <b>{adnan_page}</b></div>
<table><tr><th>الجزء</th><th>عدد الأسئلة</th><th>يبدأ من الصفحة</th></tr>{rows}</table>
<div class=tot>المجموع الكلي: {total_q} سؤالًا</div>
<div class=foot>BIOS · Telegram @BIOS0t</div></div></body></html>"""
tmp = "/tmp/bacth_note.html"; open(tmp, "w").write(page)
env = dict(os.environ, NODE_PATH=subprocess.check_output(["npm", "root", "-g"]).decode().strip())
subprocess.check_call(["node", os.path.join(ENGINE, "render.js"), "pdf", tmp, "/tmp/bacth_note.pdf"], env=env)
writer = PdfWriter(); writer.append(PdfReader("/tmp/bacth_note.pdf")); writer.add_outline_item("ملاحظة وفهرس", 0)
for title, nq, p, pdf in info:
    writer.append(PdfReader(pdf)); writer.add_outline_item(f"{title} ({nq} سؤالًا)", p - 1)
out_dir = os.path.join(REPO, "bacteriology-theory-mcq-combined"); os.makedirs(out_dir, exist_ok=True)
for f in os.listdir(out_dir):
    if f.endswith(".pdf"): os.remove(os.path.join(out_dir, f))
out = os.path.join(out_dir, "BIOS - بكتريا نظري - أسئلة MCQ (المحاضرات 1-9 + امتحانات د. عدنان).pdf")
with open(out, "wb") as f: writer.write(f)
print("TOTAL questions:", total_q, "| pages:", cur - 1, "| Adnan starts at page", adnan_page); print(out)
