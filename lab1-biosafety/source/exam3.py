import json, os, subprocess
from lib3 import *

D = json.load(open("data.json"))
MCQ, TF, TRAPS, IMPQ = D["MCQ"], D["TF"], D["TRAPS"], D["IMPQ"]
SUB = ("Exam", "الأسئلة")

EX = r"""
.qc .c-en .en{font-weight:600}.qc .c-ar .ar{line-height:1.55}.qc .c-ar{padding-top:1mm;padding-bottom:1mm}.qc .c-en{padding-top:1.8mm;padding-bottom:1.8mm}
.opts{display:grid;grid-template-columns:1fr 1fr;gap:1mm 3mm;padding:.6mm 4mm 2.4mm 4mm;background:#fff;border-top:.3mm dashed #DDD3C2}
.opts.one{grid-template-columns:1fr}
.op{display:grid;grid-template-columns:6mm 1fr 1fr;gap:3mm;align-items:center;border:.3mm solid var(--bd);border-radius:3mm;padding:0 3mm 0 1.4mm;margin-top:.9mm}
.op .l{width:5mm;height:5mm;border-radius:50%;background:var(--sage-l);color:var(--sage);font-weight:800;font-size:7.6pt;display:flex;align-items:center;justify-content:center}
.op .en{font-size:10.4pt;line-height:1.3}
.op .ar{font-size:12.5pt;line-height:1.4}
.qnum{position:absolute;right:4mm;top:3.1mm;font-size:6.4pt;font-weight:800;background:var(--burg);color:#fff;border-radius:1mm;padding:.5mm 1.4mm;line-height:1}
.c-en.q{padding-right:16mm}
.tfrow{position:absolute;left:4mm;bottom:2mm;display:flex;gap:2mm}.c-ar.tfa{padding-left:52mm}
.tfrow span{border:.35mm solid var(--sage-m);border-radius:3mm;padding:.3mm 3mm;font-size:8.6pt;font-weight:800;color:var(--sage);background:#fff}
.lines{height:24mm;margin:0 5mm 2mm;background:repeating-linear-gradient(to bottom,transparent 0,transparent 7.7mm,#D7D2C8 7.7mm,#D7D2C8 8mm)}
.akey{display:grid;grid-template-columns:repeat(8,1fr);gap:1.4mm;margin:0 0 3.6mm}
.akey div{border:.3mm solid var(--bd);border-radius:1.6mm;background:#fff;text-align:center;font-size:9.5pt;padding:1mm 0}
.akey div b{color:var(--sage);margin-right:1mm}
.akey div span{color:var(--burg);font-weight:800}
.akey.tf{grid-template-columns:repeat(6,1fr)}
"""

def mcq(i, q):
    qe, qa, opts, _ = q
    one = any(len(x) > 24 or len(y) > 24 for x, y in opts)
    o = "".join(f'<div class="op"><span class="l">{l}</span>{en(e)}{ar(a) if a != e else "<span></span>"}</div>' for l, (e, a) in zip("abcd", opts))
    return (f'<div class="card qc"><div class="c-en q"><span class="chip">EN</span><span class="qnum">Q{i}</span>{en(qe)}</div>'
            f'<div class="c-ar"><span class="chip chip-ar">AR</span>{ar(f"س{i}. " + qa)}</div>'
            f'<div class="opts{" one" if one else ""}">{o}</div></div>')

def tfq(i, t):
    return (f'<div class="card"><div class="c-en q"><span class="chip">EN</span><span class="qnum">{i}</span>{en(t[0])}</div>'
            f'<div class="c-ar tfa"><span class="chip chip-ar">AR</span><div class="tfrow" dir="ltr"><span>True · صح</span><span>False · خطأ</span></div>{ar(t[1])}</div></div>')

def trap(i, t):
    return card(t[0], t[1]).replace('<span class="chip">EN</span>', f'<span class="chip">EN</span><span class="qnum">{i}</span>', 1).replace('class="c-en"', 'class="c-en q"', 1)

def impq(i, t):
    return trap(i, t)[:-len("</div>")] + '<div class="lines" style="margin-top:2mm"></div></div>'

def ans(i, e, a, q=None):
    head = f'<div style="font-weight:800;color:var(--burg);font-size:9.5pt;margin-bottom:.6mm">{md(q)}</div>' if q else ""
    return card("", a, e_extra=head + en(e)).replace('<span class="chip">EN</span>', f'<span class="chip">EN</span><span class="qnum">{i}</span>', 1).replace('class="c-en"', 'class="c-en q"', 1)

def key_blocks():
    mk = '<div class="akey">' + "".join(f'<div><b>{i}</b><span>{q[3].upper()}</span></div>' for i, q in enumerate(MCQ, 1)) + "</div>"
    tk = '<div class="akey tf">' + "".join(f'<div><b>{i}</b><span>{"True" if t[2] == "T" else "False"}</span></div>' for i, t in enumerate(TF, 1)) + "</div>"
    out = [h2("MCQ Answers", "إجابات الاختيار من متعدد") + mk, h2("True / False Answers", "إجابات صح أو خطأ") + tk]
    out += [(h2("Exam Traps Answers", "إجابات المقالب") if i == 1 else "") + ans(i, t[2], t[3]) for i, t in enumerate(TRAPS, 1)]
    out += [(h2("Important Questions — Model Answers", "أهم الأسئلة — إجابات نموذجية") if i == 1 else "") + ans(i, t[2], t[3], t[0]) for i, t in enumerate(IMPQ, 1)]
    return out

SECS = [
 ("mcq", 1, "Comprehensive MCQs", "أسئلة اختيار من متعدد شاملة", lambda: [mcq(i, q) for i, q in enumerate(MCQ, 1)]),
 ("tf", 2, "True / False", "صح أو خطأ", lambda: [tfq(i, t) for i, t in enumerate(TF, 1)]),
 ("trap", 3, "Exam Traps", "المقالب والأسئلة الخادعة", lambda: [note("Read each statement carefully — every one hides a small but important detail from the lecture.",
                                                                       "اقرأ كل عبارة بعناية — كل واحدة تخفي تفصيلًا صغيرًا لكنه مهم من المحاضرة.", ("Exam Alert", "تنبيه امتحاني"))]
                                                                + [trap(i, t) for i, t in enumerate(TRAPS, 1)]),
 ("imp", 4, "Important Questions", "أهم الأسئلة للمراجعة", lambda: [impq(i, t) for i, t in enumerate(IMPQ, 1)]),
 ("key", 5, "Answer Key", "الحلول", key_blocks),
]

def items():
    out = [("title", labtitle().replace(TITLE_EN, "Exam &amp; Questions").replace(TITLE_AR, "بنك الأسئلة"), True)]
    for k, num, en_, ar_, fn in SECS:
        out.append((f"{k}_h", '<div style="height:2mm"></div>' + sec(num, en_, ar_), True))
        out += [(f"{k}_{i}", b, False) for i, b in enumerate(fn())]
    return out

COVER = lambda: cover("Lab 1 — Exam &amp; Questions", "العملي 1 — بنك الأسئلة",
                   [("Department", "القسم", "قسم التحليلات"), ("Stage", "المرحلة", "The fourth stage — الرابعة"),
                    ("Type", "النوع", "Questions — أسئلة"), ("Translated &amp; edited by", "ترجمة وتعديل", "محمد حامد")])

def build(S):
    its = items(); pages = [COVER()]; k = 0
    for n, cnt in enumerate(S, 1):
        body = "".join(f'<div data-m="{key}" style="display:flow-root">{h}</div>' for key, h, _ in its[k:k + cnt])
        pages.append(page(body, n, SUB)); k += cnt
    return pages

def measure():
    its = items()
    open("exam.html", "w").write(doc("x", build([len(its)]), EX))
    env = dict(os.environ, NODE_PATH=subprocess.check_output(["npm", "root", "-g"]).decode().strip())
    H = json.loads(subprocess.check_output(["node", "measure.js", "exam.html"], env=env))
    AV = 240.0; sizes, cur, cnt = [], 0, 0
    for idx, (key, _, keep) in enumerate(its):
        h = H[key] + (H[its[idx + 1][0]] if keep and idx + 1 < len(its) else 0)
        if cur + h > AV and cnt:
            sizes.append(cnt); cur, cnt = 0, 0
        cur += H[key]; cnt += 1
    sizes.append(cnt)
    return sizes

if __name__ == "__main__":
    S = measure(); print(S)
    open("exam.html", "w").write(doc("BIOS - Diagnostic Microbiology - Lab 1 - Exam", build(S), EX))
