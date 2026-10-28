"""Build an Obsidian vault (Markdown notes) with every rule, decision, handout and generator script of the BIOS work."""
import os, re, json, glob, subprocess, datetime

import shutil
REPO = os.environ.get("BIOS_REPO", "/home/user/-")
V = os.path.join(REPO, "BIOS-Obsidian")
KEEP = os.path.join(V, "tools", "scripts")          # permanent copy of every generator script
SCR = os.environ.get("BIOS_SCRATCH", "")             # optional: a session scratchpad with newer scripts
if SCR and os.path.isdir(SCR):                       # refresh the permanent copy from the scratchpad
    for f in glob.glob(SCR + "/**/*.py", recursive=True):
        if os.path.basename(f) == "vault.py": continue
        dst = os.path.join(KEEP, os.path.relpath(f, SCR)); os.makedirs(os.path.dirname(dst), exist_ok=True); shutil.copy2(f, dst)
SCR = KEEP
os.makedirs(os.path.join(V, "Code"), exist_ok=True)
TODAY = datetime.date.today().isoformat()

def w(rel, text):
    p = os.path.join(V, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w").write(text.strip() + "\n")

def pages(pdf):
    try:
        out = subprocess.check_output(["pdfinfo", pdf], stderr=subprocess.DEVNULL).decode()
        return int(re.search(r"Pages:\s+(\d+)", out).group(1))
    except Exception:
        return None

# ------------------------------------------------------------------ scripts -> code notes
SCRIPTS = {}   # script rel path -> handout folders
for f in sorted(glob.glob(SCR + "/**/*.py", recursive=True)):
    rel = os.path.relpath(f, SCR)
    src = open(f).read()
    folders = sorted(set(re.findall(r"\b((?:[a-z]+-(?:lec|lab|week|practical)[a-z0-9-]*)|lab1-biosafety)\b", src)))
    folders = [x for x in folders if os.path.isdir(os.path.join(REPO, x))]
    SCRIPTS[rel] = folders
HELPERS = {"n7/c.py": "Short block builders (C, R, SEC, H2, L, N, FLOW, T, Q, TF, TR, IM, F, FF, SIDE) and save().",
           "hem3/common.py": "Base helpers used by c.py.",
           "bac/bal.py": "balance(mcq, seed): spreads MCQ answer letters evenly.",
           "imm456/ci.py": "Clinical-immunology meta, B() bilingual cell, END() summary+glossary, INSHORT() per-topic box, TERMS() glossary, save() with split.fix.",
           "imm456/split.py": "Sentence splitter + checker: every English sentence must get its own Arabic sentence.",
           "par2/pz.py": "Parasitology theory meta + SAVE() for handouts without questions.",
           "para/parse.py": "PDF → paragraphs with ⟦bold⟧ and __italic__ markers (pdfplumber).",
           "para/qparse.py": "Paragraphs → MCQs (stem, options A–E, bold = answer).",
           "para/build.py": "MCQ banks: cleaning, translation tables, BIOS flags, inline answers."}
code_links = []
for rel, folders in SCRIPTS.items():
    name = rel.replace("/", " - ")
    note = f"Code/{name}.md"
    fm = "---\n" + f"source: BIOS-Obsidian/tools/scripts/{rel}\n" + f"handouts: [{', '.join(folders)}]\n" + f"saved: {TODAY}\n" + "tags: [bios, code]\n---\n"
    desc = HELPERS.get(rel, "Generator script — writes the handout's `lecture.json`." if folders else "Utility script.")
    links = " · ".join(f"[[06 فهرس الملازم#{x}|{x}]]" for x in folders)
    body = f"# {rel}\n\n{desc}\n\n" + (f"Handouts: {links}\n\n" if links else "") + "```python\n" + open(os.path.join(SCR, rel)).read() + "\n```\n"
    w(note, fm + body)
    code_links.append((rel, folders, name))
# engine snapshot
for rel in ["bios-engine/bios.py", "bios-engine/style.css", "bios-engine/make_theme.py"]:
    p = os.path.join(REPO, rel)
    if os.path.exists(p):
        lang = "css" if rel.endswith(".css") else "python"
        w(f"Code/engine - {os.path.basename(rel)}.md",
          f"---\nsource: {rel}\nsaved: {TODAY}\ntags: [bios, code, engine]\n---\n# {rel} (snapshot {TODAY})\n\n"
          f"The live file is in the repository; this note is a copy for reading in Obsidian.\n\n```{lang}\n" + open(p).read() + "\n```\n")

# ------------------------------------------------------------------ catalog
rows = []
for lj in sorted(glob.glob(REPO + "/*/lecture.json")):
    d = os.path.basename(os.path.dirname(lj))
    j = json.load(open(lj)); m = j.get("meta", {})
    pdfs = sorted(glob.glob(os.path.join(REPO, d, "*.pdf")))
    pdf_txt = "<br>".join(f"{os.path.basename(p)} — {pages(p)} p" for p in pdfs)
    scripts = [f"[[Code/{n}|{r}]]" for r, fs, n in code_links if d in fs]
    stage = (m.get("stage") or "—").split("—")[-1].strip()
    q = j.get("questions") or {}
    kind = "MCQ bank" if not j.get("blocks") else ("merged" if m.get("merge_questions") or stage == "الثالثة" else "handout")
    rows.append((d, m.get("subject_en", ""), m.get("unit_en", ""), m.get("title_en", ""), stage, m.get("instructor", "—"), kind, pdf_txt, " ".join(scripts) or "—"))
cat = ["# 06 فهرس الملازم", "", f"تحديث تلقائي: {TODAY}", "",
       "| Folder | Subject | Unit | Title | Stage | Instructor | Type | PDFs (pages incl. cover) | Script |",
       "|---|---|---|---|---|---|---|---|---|"]
for r in rows:
    cat.append("| " + " | ".join(str(x).replace("|", "\\|") for x in r) + " |")
cat += ["", "## Per folder", ""]
for r in rows:
    cat += [f"### {r[0]}", f"- {r[1]} · {r[2]} · {r[3]}", f"- Stage: {r[4]} · Instructor: {r[5]} · Type: {r[6]}", f"- Script: {r[8]}", ""]
w("06 فهرس الملازم.md", "\n".join(cat))

# ------------------------------------------------------------------ code index
ci = ["# Code — كل الكودات", "", "## Helpers", ""]
for r, fs, n in code_links:
    if r in HELPERS: ci.append(f"- [[Code/{n}|{r}]] — {HELPERS[r]}")
ci += ["", "## Generators (one per handout)", ""]
for r, fs, n in code_links:
    if r not in HELPERS and fs: ci.append(f"- [[Code/{n}|{r}]] → {', '.join(fs)}")
ci += ["", "## Other utilities", ""]
for r, fs, n in code_links:
    if r not in HELPERS and not fs: ci.append(f"- [[Code/{n}|{r}]]")
ci += ["", "## Engine snapshot", "", "- [[Code/engine - bios.py]]", "- [[Code/engine - style.css]]", "- [[Code/engine - make_theme.py]]"]
w("Code/00 Code index.md", "\n".join(ci))
print("notes:", len(code_links), "scripts,", len(rows), "handouts")
