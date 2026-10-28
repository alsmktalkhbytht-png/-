import json, re
r = json.load(open('paras.json'))[:223]
# merge page-break continuations
items = []
for x in r:
    t = x['text']
    if items and re.match(r'^(\.?[A-E]\s*[.\-]|[a-z]|\.|quantity|Multiple fission|amniotic)', t) and not re.search(r'week', t):
        items[-1]['text'] += ' ' + t; continue
    items.append(dict(x))
def norm(t):
    t = re.sub(r'(\s)\.([A-E])\.', r'\1\2.', t)                      # ".D." -> "D."
    t = re.sub(r'(\s)([B-E])(\s)(?=[A-Z⟦_])', r'\1\2.\3', t)          # "B Toxoplasmosis" -> "B. "
    t = re.sub(r'([A-E])\s*⟦\s*([.\-])\s*', r'\1\2 ⟦', t)        # "B ⟦. X" -> "B. ⟦X"
    t = re.sub(r'⟦\s*([A-E])\s*⟧\s*([.\-])', r'\1\2 ⟦⟧', t)      # bold letter only
    t = re.sub(r'⟦\s*⟧', '⟦*⟧', t)
    return t
OPT = re.compile(r'(?:(?<=\s)|^|(?<=⟦))([A-E])\s*[.\-]\s*')
out, week = [], 1
for it in items:
    t = it['text'].strip()
    m = re.search(r'(\d)\s*(?:st|nd|rd|th)\s*week', re.sub('[⟦⟧]', '', t))
    if m: week = int(m.group(1)); out.append({'week': week, 'heading': 'WEEK'}); continue
    if not re.search(r'\bA\s*⟦?\s*[.\-]', t) and not re.search(r'⟦A⟧\s*-', t):
        out.append({'week': week, 'heading': re.sub('[⟦⟧]', '', t).strip()}); continue
    t = norm(t)
    pos, start = [], 0
    for L in 'ABCDE':
        mm = None
        for cand in OPT.finditer(t, start):
            if cand.group(1) == L: mm = cand; break
            if cand.group(1) > L: break
        if not mm: continue
        pos.append((L, mm.start(), mm.end())); start = mm.end()
    stem = t[:pos[0][1]].strip() if pos else t
    opts, labels = [], []
    for k, (L, s0, e0) in enumerate(pos):
        end = pos[k + 1][1] if k + 1 < len(pos) else len(t)
        opts.append(t[e0:end].strip()); labels.append(L)
    for k in range(len(opts) - 1):                                  # a bold run opened just before the next letter
        if opts[k].endswith('⟦'):
            opts[k] = opts[k][:-1].strip(); opts[k + 1] = '⟦' + opts[k + 1]
    bold = lambda o: ''.join(re.findall(r'⟦(.*?)⟧', o))
    ans = [labels[k] for k, o in enumerate(opts) if len(re.sub(r'[\W_]', '', bold(o))) >= 1]
    out.append({'week': week, 'page': it['page'], 'stem': stem, 'opts': opts, 'labels': ''.join(labels), 'ans': ans, 'n': len(opts)})
json.dump(out, open('q.json', 'w'), ensure_ascii=False, indent=1)
from collections import Counter
qs = [q for q in out if 'stem' in q]
print('questions', len(qs), Counter(q['week'] for q in qs))
print('opt counts', Counter(q['n'] for q in qs))
print('answers', Counter(len(q['ans']) for q in qs))
for q in qs:
    if q['labels'] != 'ABCDE' or len(q['ans']) != 1:
        print('--', q['week'], q['page'], q['n'], q['ans'], q['stem'][:80], '|', ' | '.join(o[:30] for o in q['opts']))
print([ (h['week'],h['heading']) for h in out if 'heading' in h])
