import json, os, subprocess, sys
from lib2 import *
from art2 import medallion, corner, divider, icon
from booklet2 import X, SUBJ_EN, SUBJ_AR, TITLE_EN, TITLE_AR, LECTURER, HDR as _H

D = json.load(open("data.json"))
MCQ, TF, TRAPS, IMPQ = D["MCQ"], D["TF"], D["TRAPS"], D["IMPQ"]

HDR = _H.replace('<span class="lab">Lab 1</span>', '<span class="lab">Exam &amp; Questions</span>').replace('العملي ١', 'بنك الأسئلة')

EX = r"""
.q{margin:0 0 2.2mm;break-inside:avoid;padding-bottom:2mm;border-bottom:.3mm solid var(--line)}
.qh{display:grid;grid-template-columns:12mm 1fr;gap:2mm;align-items:start}
.qn{font-family:Playfair;font-style:italic;font-weight:900;font-size:17pt;color:var(--gold);line-height:1.15}
.qn small{font-size:9pt;color:var(--burg);font-style:normal;font-family:Cormorant;font-weight:700;letter-spacing:.1em;display:block;line-height:1}
.qt .en{font-weight:600;line-height:1.3}
.qt .ar{line-height:1.5}
.opts{display:grid;grid-template-columns:1fr;gap:.6mm;margin:1mm 0 0 14mm}
.opt{display:grid;grid-template-columns:6.5mm 1fr 1fr;gap:3mm;align-items:center;border:.3mm solid var(--line);border-radius:5mm;padding:.15mm 3.5mm .15mm 1mm;background:#fff}
.opt .l{width:5.6mm;height:5.6mm;border-radius:50%;border:.35mm solid var(--gold);color:var(--burg);font-family:Playfair;font-style:italic;font-weight:700;font-size:10pt;display:flex;align-items:center;justify-content:center}
.opt .en{font-size:12pt;line-height:1.2}
.opt .ar{font-size:12.5pt;line-height:1.35}
.tf{display:grid;grid-template-columns:10mm 1fr auto;gap:2.5mm;align-items:start;margin:0 0 2.6mm;padding-bottom:2.2mm;border-bottom:.3mm solid var(--line);break-inside:avoid}
.tf .qt .en{font-weight:500}
.tfbox{display:flex;gap:1.5mm;margin-top:1mm}
.tfbox span{width:15mm;height:7mm;border:.35mm solid var(--gold);border-radius:4mm;display:flex;align-items:center;justify-content:center;gap:1.2mm;font-size:9.5pt;color:var(--burg);font-weight:700;background:#fff}
.tfbox b{font-family:Playfair;font-style:italic}
.ans-lines{height:24mm;margin:1.6mm 0 0 14mm;background:repeating-linear-gradient(to bottom,transparent 0,transparent 7.75mm,#DCCBAA 7.75mm,#DCCBAA 8mm)}
.key{display:grid;grid-template-columns:repeat(8,1fr);gap:1.6mm;margin-bottom:3.6mm}
.key div{border:.3mm solid var(--line);border-radius:1.6mm;background:#fff;padding:1mm 0;text-align:center;font-size:11pt}
.key div b{font-family:Playfair;font-style:italic;color:var(--gold-d);margin-right:1.2mm;font-weight:700}
.key div span{color:var(--burg);font-weight:800}
.key.tfk{grid-template-columns:repeat(6,1fr)}
.ka{margin:0 0 2.4mm;display:grid;grid-template-columns:9mm 1fr;gap:2mm;break-inside:avoid}
.ka .kn{font-family:Playfair;font-style:italic;font-weight:900;color:var(--gold);font-size:15pt;line-height:1.1;text-align:right}
.ka .en{font-size:12.5pt;line-height:1.35}.ka .ar{font-size:13pt;line-height:1.6}
.kq2{font-family:Playfair;font-weight:700;color:var(--burg);font-size:11pt}
/* exam cover: inverse */
.ecv{background:radial-gradient(110% 70% at 50% 25%,#7A2532 0,#561520 50%,#320A11 100%)}
.ecv .cv-fr{border-color:var(--gold)}.ecv .cv-fr2{border-color:rgba(217,192,142,.45)}
.ecv .lb{position:absolute;left:50%;top:14mm;transform:translateX(-50%);width:70mm;padding:3mm 5mm;background:#F7EFE2;border-radius:3mm;box-shadow:0 0 0 .8mm var(--gold)}
.ecv .lb img{width:100%;display:block}
.ecv .cv-tg{color:#F3E3C4;border-color:var(--gold);background:rgba(0,0,0,.15)}
.ecv .cv-tg i{background:var(--gold)}
.ecv .cv-ar-brand{color:#E9D3A6;top:64mm}.ecv .cv-ar-brand .d{border-color:var(--gold)}
.ecv .cv-t0{color:var(--gold-l);top:72mm}
.ecv .cv-t1{color:#F7EFE2;top:77mm}
.ecv .cv-div{top:104mm}
.ecv .cv-t2{color:#F3E3C4;top:108mm}
.ecv .cv-t3{top:128mm}.ecv .cv-t3 .ln{border-color:var(--gold)}.ecv .cv-t3 span.e{color:var(--gold-l)}
.ecv .cv-t4{color:#E9D3A6;top:135.5mm}
.ecv .cv-med{top:147mm;width:88mm;height:88mm}
.ecv .stats{position:absolute;left:15mm;right:15mm;bottom:17mm;display:grid;grid-template-columns:repeat(4,1fr);gap:3mm}
.ecv .stats div{border:.4mm solid var(--gold);border-radius:2mm;padding:2.6mm 1mm 2mm;text-align:center;background:rgba(255,255,255,.05)}
.ecv .stats b{display:block;font-family:Playfair;font-weight:900;font-style:italic;font-size:22pt;color:var(--gold-l);line-height:1}
.ecv .stats span{display:block;font-family:Cormorant;font-weight:700;font-size:10.5pt;letter-spacing:.08em;color:#F3E3C4;margin-top:1mm}
.ecv .stats i{display:block;font-style:normal;font-weight:700;font-size:10pt;color:#E9D3A6}
"""

def mcq_html(i, q):
    qe, qa, opts, _ = q
    o = "".join(f'<div class="opt"><span class="l">{l}</span>{en(e)}{ar(a) if a != e else "<p></p>"}</div>' for l, (e, a) in zip("abcd", opts))
    return f'<div class="q"><div class="qh"><span class="qn"><small>Q</small>{i}</span><div class="qt">{en(qe)}{ar(f"س{ard(i)}. " + qa)}</div></div><div class="opts">{o}</div></div>'

def tf_html(i, t):
    return (f'<div class="tf"><span class="qn">{i}</span><div class="qt">{en(t[0])}{ar(t[1])}</div>'
            f'<div class="tfbox" dir="ltr"><span><b>T</b>صح</span><span><b>F</b>خطأ</span></div></div>')

def trap_html(i, t):
    return f'<div class="q"><div class="qh"><span class="qn">{i}</span><div class="qt">{en(t[0])}{ar(t[1])}</div></div></div>'

def imp_html(i, t):
    return f'<div class="q"><div class="qh"><span class="qn">{i}</span><div class="qt">{en(t[0])}{ar(t[1])}</div></div><div class="ans-lines"></div></div>'

def ka(num, e, a, q=None):
    qh = f'<div class="kq2">{md(q)}</div>' if q else ""
    return f'<div class="ka"><span class="kn">{num}</span><div>{qh}{en(e)}{ar(a)}</div></div>'

def key_blocks():
    mk = '<div class="key">' + "".join(f'<div><b>{i}</b><span>{q[3].upper()}</span></div>' for i, q in enumerate(MCQ, 1)) + "</div>"
    tk = '<div class="key tfk">' + "".join(f'<div><b>{i}</b><span>{"True" if t[2] == "T" else "False"}</span></div>' for i, t in enumerate(TF, 1)) + "</div>"
    out = [h2("MCQ Answers", "إجابات الاختيار من متعدد") + mk, h2("True / False Answers", "إجابات صح أو خطأ") + tk]
    for i, t in enumerate(TRAPS, 1):
        out.append((h2("Exam Traps Answers", "إجابات المقالب") if i == 1 else "") + ka(i, t[2], t[3]))
    for i, t in enumerate(IMPQ, 1):
        out.append((h2("Important Questions — model answers", "أهم الأسئلة — إجابات نموذجية") if i == 1 else "") + ka(i, t[2], t[3], t[0]))
    return out

HEADS = {
 "mcq": (sec("★", "Comprehensive MCQs", "أسئلة اختيار من متعدد شاملة", "check", ("PART A", "الجزء أ")), h2("Comprehensive MCQs (continued)", "أسئلة الاختيار من متعدد (تتمة)")),
 "tf": (sec("★", "True / False", "صح أو خطأ", "scale", ("PART B", "الجزء ب")), h2("True / False (continued)", "صح أو خطأ (تتمة)")),
 "trap": (sec("★", "Exam Traps", "المقالب والأسئلة الخادعة", "alert", ("PART C", "الجزء ج"))
          + box("alert", pair("Read each statement carefully — every one hides a small but important detail from the lecture.",
                              "اقرأ كل عبارة بعناية — كل واحدة تخفي تفصيلًا صغيرًا لكنه مهم من المحاضرة.")), h2("Exam Traps (continued)", "المقالب (تتمة)")),
 "imp": (sec("★", "Important Questions", "أهم الأسئلة للمراجعة", "star", ("PART D", "الجزء د")), h2("Important Questions (continued)", "أهم الأسئلة (تتمة)")),
 "key": (sec("★", "Answer Key", "الحلول", "key", ("ANSWERS", "الإجابات")), h2("Answer Key (continued)", "الحلول (تتمة)")),
}

def blocks():
    return {"mcq": [mcq_html(i, q) for i, q in enumerate(MCQ, 1)], "tf": [tf_html(i, t) for i, t in enumerate(TF, 1)],
            "trap": [trap_html(i, t) for i, t in enumerate(TRAPS, 1)], "imp": [imp_html(i, t) for i, t in enumerate(IMPQ, 1)],
            "key": key_blocks()}

def measure(S):
    open("exam.html", "w").write(doc("Biosafety Exam", build(S), X + EX))
    env = dict(os.environ, NODE_PATH=subprocess.check_output(["npm", "root", "-g"]).decode().strip())
    H = json.loads(subprocess.check_output(["node", "measure.js", "exam.html"], env=env))
    B = blocks(); AVAIL = 234.0; S2 = {}
    for k in HEADS:
        h0 = H.get(f"{k}_h0"); h1 = H.get(f"{k}_h1", 12.5)
        sizes, cur, cnt = [], h0, 0
        for i in range(len(B[k])):
            h = H[f"{k}_{i}"]
            if cur + h > AVAIL and cnt:
                sizes.append(cnt); cur, cnt = h1, 0
            cur += h; cnt += 1
        sizes.append(cnt)
        while len(sizes) > 1 and sizes[-1] < 2 and sizes[-2] > 2:
            sizes[-2] -= 1; sizes[-1] += 1
        S2[k] = sizes
    return S2

def cover():
    corners = (f'<div class="cv-cn" style="left:4mm;top:4mm">{corner(24)}</div><div class="cv-cn" style="right:4mm;top:4mm">{corner(24, rot=90)}</div>'
               f'<div class="cv-cn" style="right:4mm;bottom:4mm">{corner(24, rot=180)}</div><div class="cv-cn" style="left:4mm;bottom:4mm">{corner(24, rot=270)}</div>')
    stats = "".join(f'<div><b>{n}</b><span>{e}</span><i>{a}</i></div>' for n, e, a in
                    [(len(MCQ), "MCQs", "اختيار من متعدد"), (len(TF), "True / False", "صح أو خطأ"), (len(TRAPS), "Exam Traps", "مقالب"), (len(IMPQ), "Key Questions", "أسئلة مهمة")])
    return f'''<section class="page cover ecv"><div class="cv-fr"></div><div class="cv-fr2"></div>{corners}
<div class="lb"><img src="assets/logo.png"></div>
<div class="cv-tg" style="top:17mm"><i><span style="width:4.2mm;height:4.2mm;display:flex">{icon("plane", "#4A131B", "100%", 1.8)}</span></i>t.me/BIOS0t</div>
<div class="cv-ar-brand"><span class="d"></span><span>بنك الأسئلة &nbsp;|&nbsp; {LECTURER}</span><span class="d"></span></div>
<div class="cv-t0">EXAM &amp; QUESTIONS</div>
<div class="cv-t1">MICROBIOLOGY</div>
<div class="cv-div">{divider("70mm", "#D9C08E")}</div>
<div class="cv-t2" dir="rtl">{SUBJ_AR}</div>
<div class="cv-t3"><span class="ln"></span><span class="e">LAB 1 · {TITLE_EN.upper()}</span><span class="ln"></span></div>
<div class="cv-t4" dir="rtl">العملي ١ — {TITLE_AR} · المرحلة الرابعة</div>
<div class="cv-med">{medallion(seed=8, uid="ecm")}</div>
<div class="stats">{stats}</div>
</section>'''

def build(S):
    B = blocks(); pages = [cover()]; n = 1
    for k in ["mcq", "tf", "trap", "imp", "key"]:
        i = 0
        for j, cnt in enumerate(S[k]):
            n += 1
            hd = f'<div data-m="{k}_h{0 if j == 0 else 1}" style="display:flow-root">{HEADS[k][0 if j == 0 else 1]}</div>'
            bl = "".join(f'<div data-m="{k}_{i + t}" style="display:flow-root">{b}</div>' for t, b in enumerate(B[k][i:i + cnt]))
            pages.append(page(hd + bl, HDR, n, notes=False))
            i += cnt
    return pages

if __name__ == "__main__":
    B = blocks(); S = {k: [1] * len(B[k]) for k in HEADS}
    S = measure(S); print(S)
    pages = build(S)
    open("exam.html", "w").write(doc("Biosafety Exam", pages, X + EX))
    print("pages", len(pages))
