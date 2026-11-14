import json, os
SRC={4:("research-methods-lec4-process","Lecture 4","المحاضرة 4","4","Research Process","عملية البحث","الرابعة"),
     5:("research-methods-lec5-classification","Lecture 5","المحاضرة 5","5","Classification of Researches","تصنيف البحوث","الخامسة"),
     6:("research-methods-lec6-basic-research","Lecture 6","المحاضرة 6","6","Basic Research","البحث الأساسي (الجوهري)","السادسة")}
OUT={4:"research-methods-lec4-mcq",5:"research-methods-lec5-mcq",6:"research-methods-lec6-mcq"}
ORD={4:"الرابعة",5:"الخامسة",6:"السادسة"}
for n,(srcf,uen,uar,uno,ten,tar,ordar) in SRC.items():
    d=json.load(open(srcf+"/lecture.json")); items=d["questions"]["mcq"]
    prof=[]; after=False
    for x in items:
        if "topic_en" in x:
            if "BIOS" in x.get("topic_en",""): after=True
            continue
        if not after: prof.append(x)
    meta={"subject_en":"Research Methods","subject_ar":"طرائق البحث العلمي","short_ar":"طرائق البحث","instructor":"د. فياض",
          "unit_en":uen,"unit_ar":uar,"unit_label":"LEC","unit_no":uno,
          "title_en":ten,"title_ar":tar,"kind":"Theory — نظري","stage":"The fourth stage — الرابعة",
          "file_name":f"BIOS - طرائق البحث نظري المحاضرة {ordar} - أسئلة الأستاذ"}
    Qs={"title_en":f"{ten} (Lecture {uno}) — MCQs","title_ar":f"{tar} (المحاضرة {ordar}) — أسئلة اختيار من متعدّد",
        "sub":"MCQs","answers_inline":True,"compact":True,"mcq_per_page":3,
        "mcq_en":"Multiple-choice questions","mcq_ar":"أسئلة الاختيار من متعدّد",
        "mcq":prof,"tf":[],"traps":[],"important":[]}
    folder=OUT[n]; os.makedirs("/home/user/-/"+folder,exist_ok=True)
    json.dump({"meta":meta,"questions":Qs},open("/home/user/-/"+folder+"/lecture.json","w"),ensure_ascii=False,indent=1)
    notes=sum(1 for m in prof if m.get("note_en"))
    print(folder, len(prof),"MCQ | notes:",notes)
