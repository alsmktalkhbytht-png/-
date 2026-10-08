import json, subprocess, os, exam
from exam import *
from lib import doc, CSS
from booklet import COVER_CSS
# blocks to measure
blocks = {}
heads = {
 "mcq0": sec("A", "Comprehensive MCQs", "أسئلة اختيار من متعدد شاملة", "📝"),
 "h2": h2("Comprehensive MCQs (continued)", "أسئلة الاختيار من متعدد (تتمة)"),
 "tf0": sec("B", "True / False", "صح أو خطأ", "✔️"),
 "trap0": sec("C", "Exam Traps", "المقالب والأسئلة الخادعة", "⚠️") + box("alert", pair("Read each statement carefully — every one hides a small but important detail from the lecture.", "اقرأ كل عبارة بعناية — كل واحدة تخفي تفصيلًا صغيرًا لكنه مهم من المحاضرة.")),
 "imp0": sec("D", "Important Questions", "أهم الأسئلة للمراجعة", "⭐"),
}
blocks.update(heads)
for i,q in enumerate(MCQ): blocks[f"mcq{i+1}_"]=mcq_html(i+1,q)
for i,t in enumerate(TF): blocks[f"tf{i+1}_"]=tf_html(i+1,t)
for i,t in enumerate(TRAPS): blocks[f"trap{i+1}_"]=trap_html(i+1,t)
for i,t in enumerate(IMPQ): blocks[f"imp{i+1}_"]=imp_html(i+1,t)
for i,b in enumerate(key_blocks()): blocks[f"key{i+1}_"]=b
blocks["key0"]=sec("✓", "Answer Key", "الحلول", "🔑")
# wrap each in flow-root so margins count
html = "".join(f'<div class="page exam" style="height:auto;display:block"><div class="body" style="display:block"><div data-m="{k}" style="display:flow-root">{v}</div></div></div>' for k,v in blocks.items())
open("measure.html","w").write(doc("m",[html],COVER_CSS+exam.EXAM_CSS))
H=json.loads(subprocess.check_output(["node","measure.js","measure.html"],env=dict(os.environ,NODE_PATH=subprocess.check_output(["npm","root","-g"]).decode().strip())))
AVAIL=240.0
def pack(prefix,n,head0):
    sizes=[];cur=H[head0];cnt=0
    for i in range(1,n+1):
        h=H[f"{prefix}{i}_"]
        if cur+h>AVAIL and cnt: sizes.append(cnt);cur=H["h2"];cnt=0
        cur+=h;cnt+=1
    sizes.append(cnt);return sizes
S=dict(mcq=pack("mcq",len(MCQ),"mcq0"),tf=pack("tf",len(TF),"tf0"),trap=pack("trap",len(TRAPS),"trap0"),imp=pack("imp",len(IMPQ),"imp0"))
S["key"]=pack("key",len(key_blocks()),"key0"); print(json.dumps(S)); open("sizes.json","w").write(json.dumps(S))
