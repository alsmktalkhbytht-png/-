import sys; sys.path.insert(0, "/tmp/claude-0/-home-user--/8f878068-bae9-502b-96f7-788f221c7cb0/scratchpad/imm456")
from ci import *            # c helpers + B INSHORT TERMS balance save(split.fix)

ORD = {1: "الأولى", 2: "الثانية", 3: "الثالثة", 4: "الرابعة"}
def NUR(no, title_en, title_ar):
    return dict(subject_en="Pediatric Nursing", subject_ar="تمريض الأطفال", short_ar="تمريض أطفال", unit_label="LEC",
                kind="Theory — نظري", stage="The third stage — الثالثة", department="كلية التمريض",
                unit_en=f"Lecture {no}", unit_ar=f"المحاضرة {no}", unit_no=str(no), title_en=title_en, title_ar=title_ar)
BN = lambda en, ar: N(en, ar, label=["BIOS note", "ملاحظة BIOS"])
