"""BIOS handout engine — turns one lecture.json into the BIOS-styled booklet PDF
(and, when the JSON has a "questions" section, the matching question-bank PDF).

usage:  python3 bios-engine/bios.py path/to/lecture.json [--html-only]

Pagination is automatic: every block is measured in Chromium, then packed onto
A4 pages; section and sub-heading bars always stay with the block after them.
"""
import html, json, os, random, re, subprocess, sys

ENGINE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ENGINE)
from art import biohazard, radiation  # noqa: E402

BODY_MM = 240.0                                   # usable height of .body
M = {}                                            # lecture meta, set by load()


# ------------------------------------------------------------------ inline markup
def md(s):
    """**bold**  *italic*  __bold italic species__  `LTR run inside Arabic`
    ^^mark^^  [[cut]] / [[قطع]] = text cut off in the original file."""
    s = html.escape(s or "", quote=False)
    s = re.sub(r"__(.+?)__", r'<i class="sp">\1</i>', s)
    s = re.sub(r"\*\*(.+?)\*\*", r'<b class="t">\1</b>', s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", s)
    s = re.sub(r"`(.+?)`", r'<bdi dir="ltr" class="lt">\1</bdi>', s)
    s = re.sub(r"\^\^(.+?)\^\^", r'<span class="mark">\1</span>', s)
    s = s.replace("[[cut]]", '<span class="cut" dir="ltr">[text cut off in the original file]</span>')
    s = s.replace("[[قطع]]", '<span class="cut" dir="rtl">[النص مقطوع في الملف الأصلي]</span>')
    return s


def en(s): return f'<p class="en" dir="ltr">{md(s)}</p>'
def ar(s): return f'<p class="ar" dir="rtl">{md(s)}</p>'


# ------------------------------------------------------------------ components
def card(e, a, e_extra="", a_extra="", cls=""):
    return (f'<div class="card {cls}"><div class="c-en"><span class="chip">EN</span>{en(e) if e else ""}{e_extra}</div>'
            f'<div class="c-ar"><span class="chip chip-ar">AR</span>{ar(a) if a else ""}{a_extra}</div></div>')


SHORT = 38   # an EN/AR pair this short sits on one line; longer pairs stack (Arabic under English)


def is_short(e, a, limit=SHORT):
    plain = lambda x: re.sub(r"[*_`^\[\]]", "", x or "")
    le, la = len(plain(e)), len(plain(a))
    return le + la <= 2 * limit and max(le, la) <= 1.3 * limit


def pair(e, a, limit=SHORT):
    """English with its Arabic translation: side by side when short, Arabic underneath when long."""
    lay = "inline" if is_short(e, a, limit) else "stack"
    return f'<div class="pr {lay}">{en(e)}{ar(a) if a and a != e else ""}</div>'


def plist(items_en, items_ar):
    """Numbered points, each followed immediately by its own translation."""
    rows = "".join(f'<li><span class="nb">{i}</span>{pair(e, a)}</li>'
                   for i, (e, a) in enumerate(zip(items_en, items_ar), 1))
    return f'<ol class="pl">{rows}</ol>'


def sec(n, e, a):
    return f'<div class="sec"><span class="sn">{n}</span><div class="sb"><span dir="ltr">{md(e)}</span><span dir="rtl">{md(a)}</span></div></div>'


def h2(e, a): return f'<div class="h2"><span dir="ltr">{md(e)}</span><span dir="rtl">{md(a)}</span></div>'


def unit_title(e, a):
    return (f'<div class="lt-band"><div class="lt-box"><small>{M["unit_label"]}</small><b>{M["unit_no"]}</b></div>'
            f'<span class="lt-en" dir="ltr">{md(e)}</span><span class="lt-ar" dir="rtl">{md(a)}</span></div>')


def rule(n, e, a): return f'<div class="rule"><span class="rn">{n}</span>{card(e, a)}</div>'


def group(b, alt=False):
    sub = ""
    if b.get("sub_en") or b.get("sub_ar"):
        sub = f'<div class="rg-s"><span dir="ltr">{md(b.get("sub_en", ""))}</span><span dir="rtl">{md(b.get("sub_ar", ""))}</span></div>'
    return (f'<div class="rg card"><div class="rg-h{' alt' if alt else ''}"><span dir="ltr">{md(b["title_en"])}</span>'
            f'<span dir="rtl">{md(b["title_ar"])}</span></div>{sub}'
            f'<div class="c-en"><span class="chip">EN</span>{en(b["en"])}</div>'
            f'<div class="c-ar"><span class="chip chip-ar">AR</span>{ar(b["ar"])}</div></div>')


def note(e, a, label=("Note", "ملاحظة")):
    return f'<div class="note"><span class="np">{label[0]} &nbsp; <span dir="rtl">{label[1]}</span></span>{en(e)}{ar(a)}</div>'


FIG = {"n": 0}


def fig(f, base):
    FIG["n"] += 1
    n = FIG["n"]
    if f.get("symbols"):
        art = {"biohazard": (biohazard, "BIOHAZARD", "خطر بيولوجي"), "radiation": (radiation, "RADIATION HAZARD", "خطر إشعاعي")}
        body = '<div class="sym">' + "".join(
            f'<div>{art[k][0](tri="#d9b45a", fill="#1e1b1c", edge="#1e1b1c")}<div class="l1">{art[k][1]}</div><div class="l2" dir="rtl">{art[k][2]}</div></div>'
            for k in f["symbols"]) + "</div>"
    else:
        src = os.path.join(base, f["src"])
        if f.get("width"):
            st = f'width:{f["width"]};display:block;margin:0 auto'
        elif f.get("h"):
            st = f'height:{f["h"]};object-fit:{f.get("fit", "contain")};object-position:center 40%;width:100%'
        else:
            st = "width:100%"
        body = f'<img src="{src}" style="{st}">'
    return (f'<figure class="fig"><div class="fig-c">{body}</div><figcaption><span dir="ltr"><b>Figure {n}.</b> {md(f.get("en", ""))}</span>'
            f'<span dir="rtl"><b>الشكل {n}.</b> {md(f.get("ar", ""))}</span></figcaption></figure>')


def table(b):
    ar_cols, key_cols = set(b.get("ar_cols", [])), set(b.get("key_cols", []))
    w = b.get("widths", [])
    th = "".join(f'<th{" dir=rtl" if i in ar_cols else ""}{f" style=width:{w[i]}" if i < len(w) and w[i] else ""}>{md(h)}</th>'
                 for i, h in enumerate(b["head"]))
    rows = ""
    for r in b["rows"]:
        tds = ""
        for i, c in enumerate(r):
            cls = "a" if i in ar_cols else ("k" if i in key_cols else "")
            if b.get("numbered") and i == 0:
                tds += f'<td style="text-align:center;color:var(--red);font-weight:800">{md(c)}</td>'
            else:
                tds += f'<td class="{cls}">{md(c)}</td>'
        rows += f"<tr>{tds}</tr>"
    t = f'<table class="tb">{"<tr>" + th + "</tr>"}{rows}</table>'
    if b.get("style") == "summary":
        return (f'<div class="sum"><span class="pillh">{md(b.get("label_en", "Summary"))} '
                f'<span dir="rtl">{md(b.get("label_ar", "خلاصة الجدول"))}</span></span>{t}</div>')
    return t


# ------------------------------------------------------------------ blocks → html
def render_block(b, st, base):
    """Return (html, keep_with_next)."""
    t = b["t"]
    if t == "section":
        st["sec"] += 1
        st["rule"] = 0
        top = '<div style="height:2mm"></div>' if st["sec"] > 1 else ""
        return top + sec(st["sec"], b["en"], b["ar"]), True
    if t == "h2":
        return h2(b["en"], b["ar"]), True
    if t == "card":
        if not b.get("en") and not b.get("ar"):     # list-only card
            return f'<div class="card"><div class="c-list" style="border-top:0">{plist(b["list_en"], b.get("list_ar", []))}</div></div>', False
        c = card(b["en"], b["ar"])
        if b.get("list_en"):
            c = c[:-len("</div>")] + f'<div class="c-list">{plist(b["list_en"], b.get("list_ar", []))}</div></div>'
        return c, False
    if t == "rule":
        st["rule"] += 1
        return rule(st["rule"], b["en"], b["ar"]), False
    if t == "group":
        st["grp"] += 1
        return group(b, b.get("style") == "light"), False
    if t == "figure":
        return fig(b, base), False
    if t == "figures":
        return '<div class="fig2">' + "".join(fig(f, base) for f in b["items"]) + "</div>", False
    if t == "side":
        inner = "".join(render_block(x, st, base)[0] for x in b["blocks"])
        return f'<div class="side"><div>{inner}</div>{fig(b["figure"], base)}</div>', False
    if t == "table":
        return table(b) + '<div style="height:3.4mm"></div>', False
    if t == "note":
        return note(b["en"], b["ar"], tuple(b.get("label", ("Note", "ملاحظة")))), False
    if t == "spacer":
        return f'<div style="height:{b.get("h", "3mm")}"></div>', False
    if t == "html":
        return b["html"], False
    raise ValueError(f"unknown block type: {t}")


# ------------------------------------------------------------------ page chrome
def margin_rule():
    return (f'<div class="mr"><i class="t"></i><i class="b"></i>'
            f'<span>{M["brand"]} <em>·</em> TELEGRAM <em>·</em> {M["telegram"]}</span></div>')


def header(sub):
    return (f'<div class="hdr"><div class="hp lab"><span>{sub}</span></div>'
            f'<span class="hl" style="left:25%;width:8%"></span>'
            f'<div class="hc"><div class="e">{M["subject_en"]}</div><div class="a" dir="rtl">{M["subject_ar"]}</div></div>'
            f'<span class="hl" style="right:25%;width:8%"></span>'
            f'<div class="hp bios"><span class="bw">{M["brand"]}</span></div></div>')


def footer(n):
    return (f'<div class="ftr"><div class="fx"><span>Telegram</span><b>@{M["telegram"]}</b></div></div>'
            f'<div class="tab">{n}</div>')


def page(content, n, sub):
    return (f'<section class="page" data-num="{n}">{margin_rule()}{header(sub)}'
            f'<div class="body"><div class="content">{content}</div></div>{footer(n)}</section>')


def cover(pill_l, pill_r, kind):
    cards = [("Department", "القسم", M["department"]), ("Stage", "المرحلة", M["stage"]),
             ("Type", "النوع", kind), ("Prepared by", "إعداد", M["translator"])]
    cc = "".join(f'<div class="cv-card"><span class="k">{k}<small dir="rtl">{ka}</small></span><span class="v" dir="rtl">{v}</span></div>'
                 for k, ka, v in cards)
    return f'''<section class="page cover">
<div class="cv-c1"></div><div class="cv-c2"></div><div class="cv-b1"></div><div class="cv-b2"></div>
<div class="cv-logo"><img src="{M["_logo"]}"></div>
<div class="cv-r" style="top:130mm"></div>
<div class="cv-t1">{M["subject_en"]}</div>
<div class="cv-t2" dir="rtl">{M["subject_ar"]}</div>
<div class="cv-pill"><span dir="ltr">{pill_l}</span><span dir="rtl">{pill_r}</span></div>
<div class="cv-r" style="top:181mm"></div>
<div class="cv-cards">{cc}</div>
<div class="cv-ins"><span class="k">Instructor<br><span dir="rtl">{M["instructor_label_ar"]}</span></span><span class="v" dir="rtl">{M["instructor"]}</span></div>
<span class="cv-st" style="top:221.2mm">✦ ✦ ✦</span><span class="cv-st" style="top:238.6mm;letter-spacing:0;padding:0 3mm">✦</span>
<div class="cv-band"></div>
<div class="cv-foot"><div class="l"><b>{M["brand"]}</b></div><div class="r">Telegram &nbsp;<b>@{M["telegram"]}</b></div></div>
</section>'''


def doc(title, pages):
    return (f'<!doctype html><html><head><meta charset="utf-8"><title>{title}</title>'
            f'<link rel="stylesheet" href="{M["_css"]}"><link rel="stylesheet" href="{M["_theme"]}"></head><body>{"".join(pages)}</body></html>')


# ------------------------------------------------------------------ questions
def mcq(i, q):
    one = not all(is_short(e, a, 22) for e, a in q["options"])
    o = "".join(f'<div class="op"><span class="l">{l}</span>{pair(e, a, 22 if not one else 44)}</div>'
                for l, (e, a) in zip("abcdef", q["options"]))
    return (f'<div class="card qc"><div class="c-en q"><span class="chip">EN</span><span class="qnum">Q{i}</span>{en(q["en"])}</div>'
            f'<div class="c-ar"><span class="chip chip-ar">AR</span>{ar(f"س{i}. " + q["ar"])}</div>'
            f'<div class="opts{" one" if one else ""}">{o}</div></div>')


def tfq(i, t):
    return (f'<div class="card"><div class="c-en q"><span class="chip">EN</span><span class="qnum">{i}</span>{en(t["en"])}</div>'
            f'<div class="c-ar tfa"><span class="chip chip-ar">AR</span><div class="tfrow" dir="ltr"><span>True · صح</span>'
            f'<span>False · خطأ</span></div>{ar(t["ar"])}</div></div>')


def numbered(i, e, a, lines=False):
    c = card(e, a).replace('<span class="chip">EN</span>', f'<span class="chip">EN</span><span class="qnum">{i}</span>', 1)
    c = c.replace('class="c-en"', 'class="c-en q"', 1)
    return c[:-len("</div>")] + '<div class="lines" style="margin-top:2mm"></div></div>' if lines else c


def model_answer(i, e, a, q=None):
    head = f'<div style="font-weight:800;color:var(--burg);font-size:9.5pt;margin-bottom:.6mm">{md(q)}</div>' if q else ""
    c = card("", a, e_extra=head + en(e))
    c = c.replace('<span class="chip">EN</span>', f'<span class="chip">EN</span><span class="qnum">{i}</span>', 1)
    return c.replace('class="c-en"', 'class="c-en q"', 1)


def question_items(Q):
    out = [(unit_title("Exam & Questions", "بنك الأسئلة"), True)]
    n = 0

    def head(e, a):
        nonlocal n
        n += 1
        out.append(('<div style="height:2mm"></div>' + sec(n, e, a), True))

    if Q.get("mcq"):
        head("Comprehensive MCQs", "أسئلة اختيار من متعدد شاملة")
        out += [(mcq(i, q), False) for i, q in enumerate(Q["mcq"], 1)]
    if Q.get("tf"):
        head("True / False", "صح أو خطأ")
        out += [(tfq(i, t), False) for i, t in enumerate(Q["tf"], 1)]
    if Q.get("traps"):
        head("Exam Traps", "المقالب والأسئلة الخادعة")
        out.append((note("Read each statement carefully — every one hides a small but important detail from the lecture.",
                         "اقرأ كل عبارة بعناية — كل واحدة تخفي تفصيلًا صغيرًا لكنه مهم من المحاضرة.", ("Exam Alert", "تنبيه امتحاني")), False))
        out += [(numbered(i, t["en"], t["ar"]), False) for i, t in enumerate(Q["traps"], 1)]
    if Q.get("important"):
        head("Important Questions", "أهم الأسئلة للمراجعة")
        out += [(numbered(i, t["en"], t["ar"], lines=True), False) for i, t in enumerate(Q["important"], 1)]
    head("Answer Key", "الحلول")
    if Q.get("mcq"):
        out.append((h2("MCQ Answers", "إجابات الاختيار من متعدد"), True))
        out.append(('<div class="akey">' + "".join(f'<div><b>{i}</b><span>{q["answer"].upper()}</span></div>'
                                                   for i, q in enumerate(Q["mcq"], 1)) + "</div>", False))
    if Q.get("tf"):
        out.append((h2("True / False Answers", "إجابات صح أو خطأ"), True))
        out.append(('<div class="akey tf">' + "".join(f'<div><b>{i}</b><span>{"True" if t["answer"] == "T" else "False"}</span></div>'
                                                      for i, t in enumerate(Q["tf"], 1)) + "</div>", False))
    for i, t in enumerate(Q.get("traps", []), 1):
        if i == 1:
            out.append((h2("Exam Traps Answers", "إجابات المقالب"), True))
        out.append((model_answer(i, t["answer_en"], t["answer_ar"]), False))
    for i, t in enumerate(Q.get("important", []), 1):
        if i == 1:
            out.append((h2("Important Questions — Model Answers", "أهم الأسئلة — إجابات نموذجية"), True))
        out.append((model_answer(i, t["answer_en"], t["answer_ar"], t["en"]), False))
    return out


# ------------------------------------------------------------------ pagination
def node(*args):
    env = dict(os.environ, NODE_PATH=subprocess.check_output(["npm", "root", "-g"]).decode().strip())
    return subprocess.check_output(["node", os.path.join(ENGINE, "render.js"), *args], env=env).decode()


def paginate(items, html_path, sub, forced):
    """items: [(html, keep_with_next)]; forced: indexes that must start a new page."""
    probe = "".join(f'<div data-m="{i}" style="display:flow-root">{h}</div>' for i, (h, _) in enumerate(items))
    open(html_path, "w").write(doc("measure", [page(probe, 1, sub)]))
    H = json.loads(node("measure", html_path))
    pages, cur, h_cur = [], [], 0.0
    for i, (h, keep) in enumerate(items):
        need = H[str(i)]
        j = i
        while keep and j + 1 < len(items):          # heading chain + first real block
            j += 1
            need += H[str(j)]
            if not items[j][1]:
                break
        if cur and (i in forced or h_cur + need > BODY_MM):
            pages.append(cur)
            cur, h_cur = [], 0.0
        cur.append(h)
        h_cur += H[str(i)]
    if cur:
        pages.append(cur)
    return pages


# ------------------------------------------------------------------ main
DEFAULTS = {"brand": "BIOS", "telegram": "BIOS0t", "instructor_label_ar": "تدريسية المادة", "unit_label": "LAB", "kind": "Laboratories — عملي",
            "questions_kind": "Questions — أسئلة"}


def load(path):
    data = json.load(open(path))
    M.clear()
    M.update(DEFAULTS)
    M.update(data["meta"])
    return data


def build(path, html_only=False):
    data = load(path)
    base_dir = os.path.dirname(os.path.abspath(path))
    out_dir = os.path.join(base_dir, ".build")
    os.makedirs(out_dir, exist_ok=True)
    rel = lambda p: os.path.relpath(p, out_dir)
    M["_css"] = rel(os.path.join(ENGINE, "style.css"))
    theme = M.get("theme", "knight")
    M["_theme"] = rel(os.path.join(ENGINE, "themes", theme + ".css"))
    M["_logo"] = rel(os.path.join(ENGINE, "brand", f"logo_{theme}.jpg"))
    asset_base = rel(base_dir)
    sub = M["unit_en"]
    name = M.get("file_name") or f'{M["brand"]} - {M["subject_en"]} - {M["unit_en"]}'
    outputs = []

    # booklet
    FIG["n"] = 0
    st = {"sec": 0, "rule": 0, "grp": 0}
    items, forced = [(unit_title(M["title_en"], M["title_ar"]), True)], set()
    for b in data["blocks"]:
        if b["t"] == "pagebreak":
            forced.add(len(items))
            continue
        h, keep = render_block(b, st, asset_base)
        items.append((h, keep or b.get("keep", False)))
    tmp = os.path.join(out_dir, "booklet.html")
    pages = paginate(items, tmp, sub, forced)
    FIG["n"] = 0  # numbering already baked into items
    html_pages = [cover(f'{M["unit_en"]} — {M["title_en"]}', M["title_ar"], M["kind"])]
    html_pages += [page("".join(p), n, sub) for n, p in enumerate(pages, 1)]
    open(tmp, "w").write(doc(name, html_pages))
    outputs.append((tmp, os.path.join(base_dir, name + ".pdf"), len(pages)))

    # question bank
    if data.get("questions"):
        qsub = f'{M["unit_en"]} · Exam'
        tmpq = os.path.join(out_dir, "questions.html")
        qpages = paginate(question_items(data["questions"]), tmpq, qsub, set())
        hp = [cover(f'{M["unit_en"]} — Exam &amp; Questions', "بنك الأسئلة", M["questions_kind"])]
        hp += [page("".join(p), n, qsub) for n, p in enumerate(qpages, 1)]
        open(tmpq, "w").write(doc(name + " - Questions", hp))
        outputs.append((tmpq, os.path.join(base_dir, name + " - Questions.pdf"), len(qpages)))

    for h, pdf, n in outputs:
        if not html_only:
            shots = os.path.join(out_dir, os.path.splitext(os.path.basename(h))[0] + "-pages")
            os.makedirs(shots, exist_ok=True)
            for old in os.listdir(shots):
                os.remove(os.path.join(shots, old))
            print(node("pdf", h, pdf, shots))
        print(f"{pdf}  ({n} pages + cover)")


if __name__ == "__main__":
    build(sys.argv[1], "--html-only" in sys.argv)
