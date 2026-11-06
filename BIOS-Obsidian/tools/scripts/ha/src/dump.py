import docx,sys
from docx.oxml.ns import qn
d=docx.Document(sys.argv[1]); rels=d.part.rels
def pics(el):
    out=[]
    for b in el.iter(qn('a:blip')):
        r=b.get(qn('r:embed')); out.append(rels[r].target_ref.split('/')[-1] if r in rels else r)
    for b in el.iter('{urn:schemas-microsoft-com:vml}imagedata'):
        r=b.get(qn('r:id')); out.append('v:'+(rels[r].target_ref.split('/')[-1] if r in rels else str(r)))
    return out
def ptxt(p): return ''.join(x.text or '' for x in p.iter(qn('w:t')))
for el in d.element.body.iterchildren():
    tag=el.tag.split('}')[1]
    if tag=='p':
        t=ptxt(el); pc=pics(el)
        if t.strip() or pc: print((str(pc)+' ' if pc else '')+t)
    elif tag=='tbl':
        print('<<TABLE')
        for r in el.findall(qn('w:tr')):
            for c in r.findall(qn('w:tc')):
                print(' --CELL', pics(c) or '')
                for p in c.iter(qn('w:p')):
                    t=ptxt(p)
                    if t.strip(): print('    ',t)
            print(' ==ROW')
        print('TABLE>>')
