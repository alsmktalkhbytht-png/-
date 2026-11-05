import sys; sys.path.insert(0, "/tmp/claude-0/-home-user--/8f878068-bae9-502b-96f7-788f221c7cb0/scratchpad/imm456")
from ci import *            # c helpers + B INSHORT TERMS balance save(split.fix)

ORD = {1: "الأولى", 2: "الثانية", 3: "الثالثة", 4: "الرابعة"}
def NUR(no, title_en, title_ar):
    return dict(subject_en="Pediatric Nursing", subject_ar="تمريض الأطفال", short_ar="تمريض أطفال", unit_label="LEC",
                kind="Theory — نظري", stage="The third stage — الثالثة", department="كلية التمريض",
                unit_en=f"Lecture {no}", unit_ar=f"المحاضرة {no}", unit_no=str(no), title_en=title_en, title_ar=title_ar)
BN = lambda en, ar: N(en, ar, label=["BIOS note", "ملاحظة BIOS"])

def chunk_lists(blocks, size=8):
    """Split long point lists into several cards so no card is taller than a page."""
    out = []
    for b in blocks:
        le, la = b.get("list_en"), b.get("list_ar")
        if b.get("t") == "card" and le and len(le) > size + 1:
            for i in range(0, len(le), size):
                nb = dict(b, list_en=le[i:i + size], list_ar=la[i:i + size], start=b.get("start", 1) + i)
                if i:
                    nb["en"] = (b.get("en") or "") and b["en"].rstrip(":*") + " (continued)**" if b.get("en", "").startswith("**") else b.get("en", "")
                    nb["ar"] = (b.get("ar") or "") and b["ar"].rstrip(":*") + " (تكملة)**" if b.get("ar", "").startswith("**") else b.get("ar", "")
                out.append(nb)
        else:
            out.append(b)
    return out
