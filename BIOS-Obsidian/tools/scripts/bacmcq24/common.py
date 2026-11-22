# Shared helpers for the 2024 bacteriology MCQ file (Yassin Falah compilation) — lectures 1–11 (pages 1–24 of the file).
def S(latin):
    return "__%s__" % latin

D1 = ("1st round 2023", "الدور الأول 2023")
D2 = ("2nd round 2023", "الدور الثاني 2023")

def Q(en, ar, opts, ans, note=None, tag=None):
    if tag:                                    # past-exam marker kept from the file
        en, ar = f"{en} ({tag[0]})", f"{ar} ({tag[1]})"
    d = {"en": en, "ar": ar, "options": opts}
    if ans:
        d["answer"] = ans
    if note:
        d["note_en"], d["note_ar"] = note
    return d

def T(en, ar):
    return {"topic_en": en, "topic_ar": ar}

ALL   = ["All of the above", "جميع ما سبق"]
ALLs  = ["All of above", "جميع ما سبق"]
NONE  = ["None of the above", "لا شيء مما سبق"]
NONEb = ["None of them", "لا شيء منها"]
NOONE = ["No one of above", "لا شيء مما سبق"]
AB    = ["Both A+B", "كلاهما أ + ب"]
