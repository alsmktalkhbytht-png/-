"""review — final check of a BIOS handout BEFORE sending it (user rule 2026-11-06: every handout is re-checked
for mistakes and missing content after it is built, then sent).

    python3 review.py <folder> <source.txt>      # source.txt = the professor's text (pdftotext -layout / docx XML)

Prints a report; "REVIEW OK" only when nothing needs a look. Checks:
  1  source coverage  every source line/sentence (4+ words) must appear verbatim in the English of lecture.json
  2  words            every source word (6+ letters) appears somewhere
  3  translation      every en has an ar; no Arabic field left in English; sentence lists the same length
  4  figures          every assets/ file is used, every used file exists
  5  questions        MCQ: answer letter valid, 4-5 options, no duplicate options, letters balanced;
                      TF answers T/F; traps/important have answers; no repeated question
  6  pages            overflow + fill2 (lecture pages >= 80%) — run after bios.py
Then READ the flagged items and the page images yourself: numbers, units, names, answer keys, the cover.
"""
import json, os, re, subprocess, sys, glob
from collections import Counter

folder, src_path = sys.argv[1].rstrip("/"), sys.argv[2]
data = json.load(open(os.path.join(folder, "lecture.json")))
issues = []


def norm(s, lower=True):
    s = re.sub(r"[\ue000-\uf8ff\u200b-\u200f\u00a0\ufeff]", " ", s)          # Word bullets, invisible marks
    s = re.sub(r"\[\[[^\]]*\]\]|\*\*|__|`|\^\^|\\", "", s)
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("&amp;", "&")
    s = re.sub(r"^[\s•\-–·]*(\(?\d{1,2}[-.)]\)?)?\s*", "", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s.lower() if lower else s


def strings(x, keys=("en",), out=None, key=None):
    out = [] if out is None else out
    if isinstance(x, str):
        if key in keys:
            out.append(x)
    elif isinstance(x, list):
        if len(x) == 2 and all(isinstance(y, str) for y in x) and key not in ("list_en", "list_ar", "en", "ar"):
            if "en" in keys: out.append(x[0])          # bilingual cell / option
            if "ar" in keys: out.append(x[1])
        else:
            for y in x:
                strings(y, keys, out, key)
    elif isinstance(x, dict):
        for k, v in x.items():
            kk = {"list_en": "en", "list_ar": "ar", "answer_en": "en", "answer_ar": "ar", "text_en": "en", "text_ar": "ar",
                  "title_en": "en", "title_ar": "ar", "label_en": "en", "label_ar": "ar"}.get(k, k)
            if k in ("head", "rows", "options", "items", "steps", "blocks", "figure"):
                kk = key if k in ("items", "steps", "blocks", "figure") else "cell"
                if kk == "cell":
                    for y in (v if isinstance(v, list) else [v]):
                        _cells(y, keys, out)
                    continue
            strings(v, keys, out, kk)
    return out


def _cells(x, keys, out):
    if isinstance(x, str):
        if "en" in keys: out.append(x)
    elif isinstance(x, list):
        if len(x) == 2 and all(isinstance(y, str) for y in x):
            if "en" in keys: out.append(x[0])
            if "ar" in keys: out.append(x[1])
        else:
            for y in x: _cells(y, keys, out)


EN = norm(" \n ".join(strings(data.get("blocks") or [], ("en",)) + strings(data.get("questions") or {}, ("en",))))
src = open(src_path).read()

# 1 coverage: rejoin wrapped lines into paragraphs, then check sentence by sentence and option by option
def paragraphs(text):
    text = text.replace("**", "").replace("\f", "\n")
    text = re.sub(r"-\n\s*", "-", text)                                   # "antigen-\nantibody"
    out, cur = [], []
    for line in text.splitlines():
        t = re.sub(r"[\ue000-\uf8ff]", " ", line).strip()
        starts = re.match(r"^(\d{1,2}[.)-]|[a-z][.)]?\s|[•oO▪§\-–]\s|[A-Z][a-z]+( [a-z]+)*:$)", t)
        short_prev = cur and len(cur[-1].split()) <= 5 and not re.search(r"[.,;:?]$", cur[-1])   # a title line
        if not t or re.fullmatch(r"\d{1,3}", t) or (starts and cur) or short_prev:
            if cur: out.append(" ".join(cur)); cur = []
            if not t or re.fullmatch(r"\d{1,3}", t): continue
        cur.append(re.sub(r"^([•oO▪§\-–]|[a-z][.)]?)\s+", "", t))
    if cur: out.append(" ".join(cur))
    return out
miss = []
for para in paragraphs(src):
    for sent in re.split(r"(?<=[.?!:])\s+(?=[A-Z(])|(?<=[a-z] [.?!])(?=[A-Z][a-z])|(?<=[a-z][.?!])(?=[A-Z][a-z])|\s+(?=[A-Ea-e]\.\s)|\s+(?=\(\d{1,2}\)\s)", para):
        sent = re.sub(r"^([A-Ea-e]\.|\(\d{1,2}\))\s+", "", sent)
        sent = re.sub(r"\s+[a-e]\.?$", "", sent)                         # trailing list letter of the next item
        n = norm(sent)
        n2 = re.sub(r"\s+[tf]$", "", n)                                   # TF key letter after the statement
        heading = len(n.split()) <= 6 and not re.search(r"[.?]", n)          # titles are rewritten as section bars
        if len(n.split()) >= 4 and not heading and n not in EN and n2 not in EN:
            miss.append(sent.strip())
if miss:
    issues.append(("source sentences not found verbatim", miss))

# 2 words
words = {w.lower() for w in re.findall(r"[A-Za-z][A-Za-z\-]{5,}", src)}
allj = json.dumps(data, ensure_ascii=False).lower()
lost = sorted(w for w in words if w not in allj)
if lost:
    issues.append(("source words missing", lost))

# 3 translation
bad = []
def walk(b, where=""):
    if isinstance(b, dict):
        t = b.get("t", "")
        for ek, ak in (("en", "ar"), ("list_en", "list_ar"), ("answer_en", "answer_ar")):
            e, a = b.get(ek), b.get(ak)
            if e and not a and not data["meta"].get("arabic_only"):
                bad.append(f"{t} {ek} has no {ak}: {str(e)[:60]}")
            if isinstance(e, list) and isinstance(a, list) and len(e) != len(a):
                bad.append(f"{t} {ek}/{ak} lengths {len(e)}/{len(a)}: {str(e)[:60]}")
        for v in b.values():
            walk(v, where)
    elif isinstance(b, list):
        for v in b:
            walk(v, where)
walk(data)
for a in strings(data, ("ar",)):
    plain = re.sub(r"`[^`]*`", "", a)
    lat, arb = len(re.findall(r"[A-Za-z]", plain)), len(re.findall(r"[؀-ۿ]", plain))
    if lat > 25 and lat > arb:
        bad.append("Arabic field mostly English: " + a[:70])
if bad:
    issues.append(("translation", bad))

# 4 figures
used = set(re.findall(r'"(assets/[^"]+)"', json.dumps(data, ensure_ascii=False)))
have = {os.path.relpath(p, folder) for p in glob.glob(os.path.join(folder, "assets", "*"))}
if used - have: issues.append(("figures used but missing", sorted(used - have)))
if have - used: issues.append(("assets not used in the handout (every image of the file must go in)", sorted(have - used)))

# 5 questions
Q = data.get("questions") or {}
qi = []
mcq = [q for q in Q.get("mcq", []) if "options" in q]
for i, q in enumerate(mcq, 1):
    n = len(q["options"])
    if not 4 <= n <= 5: qi.append(f"MCQ {i}: {n} options")
    if q.get("answer") not in "abcde"[:n] or not q.get("answer"): qi.append(f"MCQ {i}: answer {q.get('answer')!r}")
    if len({norm(o[0], lower=False) for o in q["options"]}) < n: qi.append(f"MCQ {i}: duplicate options")
cnt = Counter(q.get("answer") for q in mcq)
if mcq and max(cnt.values()) - min(cnt.values()) > 2:
    qi.append(f"MCQ letters unbalanced {dict(cnt)} — OK only if the professor's own questions keep their keys")
for i, q in enumerate(Q.get("tf", []), 1):
    if q.get("answer") not in ("T", "F"): qi.append(f"TF {i}: answer {q.get('answer')!r}")
for k in ("traps", "important"):
    for i, q in enumerate(Q.get(k, []), 1):
        if not q.get("answer_en") or not q.get("answer_ar"): qi.append(f"{k} {i}: no answer")
stems = Counter(norm(q.get("en", "")) for q in mcq + Q.get("tf", []))
qi += [f"repeated question: {s[:60]}" for s, c in stems.items() if c > 1 and s]
if qi: issues.append(("questions", qi))
print(f"questions: {len(mcq)} MCQ {dict(sorted(cnt.items()))}, {len(Q.get('tf', []))} TF, {len(Q.get('traps', []))} traps, {len(Q.get('important', []))} important")

# 6 pages
here = os.path.dirname(os.path.abspath(__file__))
if os.path.exists(os.path.join(folder, ".build", "booklet.html")):
    r = subprocess.run([sys.executable, "-W", "ignore", os.path.join(here, "fill2.py"), folder], capture_output=True, text=True).stdout.split()
    if len(r) > 2: issues.append(("pages under 80% (fill2)", r[2:]))
else:
    issues.append(("pages", ["not built yet — run bios.py, then review again"]))

for title, items in issues:
    print(f"\n## {title} ({len(items)})")
    for x in items[:40]:
        print("  -", x)
print("\nREVIEW OK" if not issues else f"\nREVIEW: {len(issues)} group(s) to look at")
