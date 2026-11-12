import sys; sys.path.insert(0, "/tmp/claude-0/-home-user-kwmdkm/a7dd109e-db53-5fd3-8234-9dab3a530e24/scratchpad/nur")
from common_nur import *     # ci helpers + B INSHORT TERMS balance save + chunk_lists

def HA(no, title_en, title_ar):
    return dict(subject_en="Health Assessment", subject_ar="تقييم صحي", short_ar="تقييم صحي", unit_label="LEC",
                kind="Theory — نظري", stage="The second stage — الثانية", department="كلية التمريض",
                instructor="د. حسن علي",
                unit_en=f"Lecture {no}", unit_ar=f"المحاضرة {no}", unit_no=str(no), title_en=title_en, title_ar=title_ar)

PH = [B("Procedure", "الإجراء"), B("Normal findings", "النتائج الطبيعية")]
def PN(rows, w=(42, 58), **k):
    """PROCEDURE | NORMAL FINDINGS table; rows = [(p_en, p_ar, n_en, n_ar), ...]"""
    return T(PH, [[B(a, b), B(c, d)] for a, b, c, d in rows], widths=list(w), **k)

def LB(*pairs):
    cells = [B(f"**{e}**", a) for e, a in pairs]
    if len(cells) % 2: cells.append(B("", ""))
    return [cells[i:i + 2] for i in range(0, len(cells), 2)]
def LBT(*pairs):
    return T([B("Label", "الكتابة"), B("Label", "الكتابة")], LB(*pairs), style="summary",
             label_en="Labels in the figure", label_ar="كتابات الشكل")
