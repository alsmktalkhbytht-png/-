---
source: BIOS-Obsidian/tools/scripts/bac/bal.py
handouts: []
saved: 2026-10-29
tags: [bios, code]
---
# bac/bal.py

balance(mcq, seed): spreads MCQ answer letters evenly.

```python
import random
def balance(mcq, seed=7):
    rnd = random.Random(seed); L = "abcde"
    qs = [q for q in mcq if "answer" in q]
    seq = []
    while len(seq) < len(qs):
        b = list("abcd"); rnd.shuffle(b); seq += b
    for q, t in zip(qs, seq):
        n = len(q["options"]); i = L.index(q["answer"]); j = min(L.index(t), n - 1)
        q["options"][i], q["options"][j] = q["options"][j], q["options"][i]
        q["answer"] = L[j]
    return mcq

```
