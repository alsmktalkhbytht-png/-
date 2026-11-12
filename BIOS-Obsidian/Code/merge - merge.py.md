---
source: BIOS-Obsidian/tools/scripts/merge/merge.py
handouts: []
saved: 2026-11-12
tags: [bios, code]
---
# merge/merge.py

Utility script.

```python
"""merge — build a "دمج" copy of finished handouts: lecture + its questions in ONE pdf named
"<normal name> - <title_ar> - دمج.pdf". lecture.json and the separate files are left untouched.

    python3 merge.py <folder> [<folder> …]          (run from the repo root)

How: writes <folder>/.merge.json (meta + merge_questions + file_name; note labels cleaned of the old
bidi backticks), builds it with bios.py, deletes the temp json, prints the page count.
"""
import json, os, re, subprocess, sys

REPO = os.environ.get("BIOS_REPO", "/home/user/-")
sys.path.insert(0, os.path.join(REPO, "bios-engine"))
import bios  # noqa: E402


def clean(x):
    if isinstance(x, dict):
        return {k: ([v[0], v[1].replace("`", "")] if k == "label" and isinstance(v, list) else clean(v)) for k, v in x.items()}
    if isinstance(x, list):
        return [clean(y) for y in x]
    return x


for folder in sys.argv[1:]:
    folder = folder.rstrip("/")
    d = json.load(open(os.path.join(REPO, folder, "lecture.json")))
    bios.M.clear(); bios.M.update(bios.DEFAULTS if hasattr(bios, "DEFAULTS") else {}); bios.M.update(d["meta"])
    bios.M.setdefault("brand", "BIOS")
    base = d["meta"].get("file_name") or bios.file_name()
    d["meta"]["file_name"] = f'{base} - {d["meta"]["title_ar"]} - دمج'
    d["meta"]["merge_questions"] = True
    tmp = os.path.join(REPO, folder, ".merge.json")
    json.dump(clean(d), open(tmp, "w"), ensure_ascii=False)
    out = subprocess.run([sys.executable, os.path.join(REPO, "bios-engine", "bios.py"), tmp], capture_output=True, text=True, cwd=os.path.join(REPO, "bios-engine"))
    os.remove(tmp)
    print(folder, "|", out.stdout.strip().splitlines()[-1] if out.stdout.strip() else out.stderr[-500:])

```
