# BIOS — قالب سكربت توليد lecture.json
# انسخه إلى <folder>/make.py ثم املأ blocks و الأسئلة و meta.
# القاعدة: كل جملة من المصدر تُنقل حرفيًا وتُترجم — لا حذف ولا إضافة (انظر 01 - القواعد الذهبية).
import json, os
from collections import Counter

# ---------- دوال الكتل ----------
def C(en, ar, **k):  return dict(t="card", en=en, ar=ar, **k)            # بطاقة نص (en/ar نص أو قائمة جمل)
def R(en, ar):       return dict(t="rule", en=en, ar=ar)                 # خطوة مرقّمة بدائرة
def SEC(en, ar):     return dict(t="section", en=en, ar=ar)              # شريط قسم مرقّم
def H2(en, ar):      return dict(t="h2", en=en, ar=ar)                   # عنوان فرعي
def L(en_items, ar_items, en="", ar="", **k):                            # قائمة نقاط (كل نقطة مع ترجمتها)
    return dict(t="card", en=en, ar=ar, list_en=en_items, list_ar=ar_items, **k)
def N(en, ar, label=None):                                               # ملاحظة مؤطّرة
    b = dict(t="note", en=en, ar=ar)
    if label: b["label"] = label
    return b
def G(te, ta, en, ar, **k): return dict(t="group", title_en=te, title_ar=ta, en=en, ar=ar, **k)  # بطاقة بعنوان داكن
def T(head, rows, **k): return dict(t="table", head=head, rows=rows, **k)                      # جدول
def F(src, en, ar, **k): return dict(t="figure", src="assets/" + src, en=en, ar=ar, **k)       # صورة واحدة
def FF(*items):                                                                                  # صورتان متجاورتان
    return dict(t="figures", items=[dict(src="assets/" + s, en=e, ar=a, h=h, fit="contain") for s, e, a, h in items])
def SIDE(blocks, src, en, ar):                                                                   # نص + صورة صغيرة
    return dict(t="side", blocks=blocks, figure=dict(src="assets/" + src, en=en, ar=ar))
def FLOW(pairs, **k): return dict(t="flow", steps=[{"en": e, "ar": a} for e, a in pairs], **k)  # سلسلة أسهم (فقط إن كانت في المصدر)

# ---------- دوال الأسئلة ----------
def Q(en, ar, opts, ans, **k):          # اختيار من متعدد: opts = [(en, ar), ...] 4 أو 5، ans = 'a'..'e'
    return dict(en=en, ar=ar, options=[list(o) for o in opts], answer=ans, **k)
def TF(en, ar, a): return dict(en=en, ar=ar, answer=a)                    # صح وخطأ: 'T' / 'F'
def TR(en, ar, ae, aa): return dict(en=en, ar=ar, answer_en=ae, answer_ar=aa)   # مقلب
IM = TR                                                                   # سؤال مهم بإجابة نموذجية

blocks = [
 SEC("Section title", "عنوان القسم"),
 C(["Sentence one.", "Sentence two."],
   ["الجملة الأولى.", "الجملة الثانية."]),
 # F("figure.jpg", "Caption", "التعليق", h="60mm", fit="contain"),
 # T(["Col EN", "Col EN", "الترجمة"], [["...", "...", "**...** — ..."]], ar_cols=[2], key_cols=[0]),
]

mcq = [
 {"topic_en": "Topic", "topic_ar": "الموضوع"},
 # Q("Question?", "السؤال؟", [("A", "أ"), ("B", "ب"), ("C", "ج"), ("D", "د")], "a"),
 # {"topic_en": "Picture questions", "topic_ar": "أسئلة الصور"},
 # Q("...", "...", [...], "b", img="assets/q-x.jpg", img_h="34mm"),
]
tf = []
traps = []
important = []

meta = dict(subject_en="Subject", subject_ar="المادة", short_ar="الاسم المختصر",
            unit_en="Lecture 1", unit_ar="المحاضرة 1", unit_label="LEC", unit_no="1",      # عملي: "Lab 1","العملي 1","LAB"
            title_en="Title", title_ar="العنوان",
            kind="Theory — نظري",                       # عملي: "Laboratories — عملي"
            stage="The third stage — الثالثة",          # رابعة: "The fourth stage — الرابعة"
            instructor="د. ...")

folder = "subject-lec1-topic"
qs = [q for q in mcq if "answer" in q]
print(folder, len(qs), dict(Counter(q["answer"] for q in qs)), len(tf),
      dict(Counter(t["answer"] for t in tf)), len(traps), len(important))
d = os.path.join(os.path.dirname(os.path.abspath(__file__)))
json.dump({"meta": meta, "blocks": blocks,
           "questions": {"mcq": mcq, "tf": tf, "traps": traps, "important": important}},
          open(os.path.join(d, "lecture.json"), "w"), ensure_ascii=False, indent=1)
