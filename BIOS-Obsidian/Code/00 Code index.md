# Code — كل الكودات

## Helpers

- [[Code/bac - bal.py|bac/bal.py]] — balance(mcq, seed): spreads MCQ answer letters evenly.
- [[Code/hem3 - common.py|hem3/common.py]] — Base helpers used by c.py.
- [[Code/imm456 - ci.py|imm456/ci.py]] — Clinical-immunology meta, B() bilingual cell, END() summary+glossary, INSHORT() per-topic box, TERMS() glossary, save() with split.fix.
- [[Code/imm456 - split.py|imm456/split.py]] — Sentence splitter + checker: every English sentence must get its own Arabic sentence.
- [[Code/n7 - c.py|n7/c.py]] — Short block builders (C, R, SEC, H2, L, N, FLOW, T, Q, TF, TR, IM, F, FF, SIDE) and save().
- [[Code/par2 - pz.py|par2/pz.py]] — Parasitology theory meta + SAVE() for handouts without questions.
- [[Code/para - build.py|para/build.py]] — MCQ banks: cleaning, translation tables, BIOS flags, inline answers.
- [[Code/para - parse.py|para/parse.py]] — PDF → paragraphs with ⟦bold⟧ and __italic__ markers (pdfplumber).
- [[Code/para - qparse.py|para/qparse.py]] — Paragraphs → MCQs (stem, options A–E, bold = answer).

## Generators (one per handout)

- [[Code/bac - lab2.py|bac/lab2.py]] → bacteriology-lab2-specimens
- [[Code/bac - lab3.py|bac/lab3.py]] → bacteriology-lab3-culture-media
- [[Code/bb - make.py|bb/make.py]] → bloodbank-lec1-introduction
- [[Code/bt - make2.py|bt/make2.py]] → bloodbank-lec2-donation-criteria
- [[Code/bt - make3.py|bt/make3.py]] → bloodbank-lec3-services
- [[Code/chr - l2.py|chr/l2.py]] → histopathology-lec2-chronic-inflammation
- [[Code/eth - make.py|eth/make.py]] → ethics-lec1-morals
- [[Code/heal - l4.py|heal/l4.py]] → histopathology-lec4-healing-regeneration
- [[Code/hem - make.py|hem/make.py]] → enzymology-lab1-safety-tubes
- [[Code/hem3 - l2.py|hem3/l2.py]] → hematology-lec2-blood-cell-formation
- [[Code/hem3 - l3.py|hem3/l3.py]] → hematology-lec3-blood-elements
- [[Code/hem3 - l4.py|hem3/l4.py]] → hematology-lec4-hemoglobin
- [[Code/hem3 - l5.py|hem3/l5.py]] → hematology-lec5-anaemia
- [[Code/hem3 - l6.py|hem3/l6.py]] → hematology-lec6-iron-deficiency
- [[Code/hem3 - l7.py|hem3/l7.py]] → hematology-lec7-chronic-sideroblastic
- [[Code/his - l1.py|his/l1.py]] → histopathology-lab1-lab-safety
- [[Code/his - l2.py|his/l2.py]] → histopathology-lab2-samples
- [[Code/im2 - l2.py|im2/l2.py]] → immunology-lec2-cells-organs
- [[Code/im3 - l3.py|im3/l3.py]] → immunology-lec3-antigens
- [[Code/imm456 - bb4.py|imm456/bb4.py]] → bloodbank-lec4-screening
- [[Code/imm456 - bb5.py|imm456/bb5.py]] → bloodbank-lec5-abo-rh
- [[Code/imm456 - ci2.py|imm456/ci2.py]] → clinimm-lec2-sle
- [[Code/imm456 - ci3.py|imm456/ci3.py]] → clinimm-lec3-as-psa
- [[Code/imm456 - ci4.py|imm456/ci4.py]] → clinimm-lec4-sjogren
- [[Code/imm456 - ci5.py|imm456/ci5.py]] → clinimm-lec5-behcet
- [[Code/imm456 - ci6.py|imm456/ci6.py]] → clinimm-lec6-celiac-pa-t1d
- [[Code/imm456 - eth3.py|imm456/eth3.py]] → ethics-lec3-unethical-behavior
- [[Code/imm456 - rs3.py|imm456/rs3.py]] → research-lec3-research-plan
- [[Code/imt - l1.py|imt/l1.py]] → immunology-lec1-introduction
- [[Code/inf - l1.py|inf/l1.py]] → histopathology-lec1-acute-inflammation
- [[Code/n2 - make1.py|n2/make1.py]] → enzymology-lec1-introduction
- [[Code/n2 - make2.py|n2/make2.py]] → enzymology-lec2-kinetics-inhibition
- [[Code/n3 - make.py|n3/make.py]] → research-lec2-scientific-method
- [[Code/n4 - make.py|n4/make.py]] → advtech-lec1-elisa
- [[Code/n4 - svg.py|n4/svg.py]] → advtech-lec1-elisa
- [[Code/n5 - make.py|n5/make.py]] → hematology-lab1-blood-collection
- [[Code/n6 - make.py|n6/make.py]] → genetics-lec1-cell-cycle-mitosis
- [[Code/n7 - anti.py|n7/anti.py]] → hematology-practical-anticoagulants
- [[Code/n7 - norm.py|n7/norm.py]] → hematology-practical-normal-values
- [[Code/n7 - vir.py|n7/vir.py]] → virology-lab1-safety
- [[Code/par - make.py|par/make.py]] → parasitology-week1-mcq
- [[Code/pat - make12.py|pat/make12.py]] → pathology-lec1-2-atelectasis
- [[Code/pat - make3.py|pat/make3.py]] → pathology-lec3-chronic-bronchitis
- [[Code/picq.py|picq.py]] → bloodbank-lec1-introduction, immunology-lab1-serology, lab1-biosafety
- [[Code/res - make.py|res/make.py]] → research-lec1-principles
- [[Code/ria - l3.py|ria/l3.py]] → advtech-lec3-ria
- [[Code/sol - l4.py|sol/l4.py]] → parasitology-lab4-solutions

## Other utilities

- [[Code/bac - sheet.py|bac/sheet.py]]
- [[Code/bios_dbg.py|bios_dbg.py]]
- [[Code/covers - make.py|covers/make.py]]
- [[Code/covers - make2.py|covers/make2.py]]
- [[Code/imm456 - ci5_blocks.py|imm456/ci5_blocks.py]]
- [[Code/imm456 - ci6_ar.py|imm456/ci6_ar.py]]
- [[Code/par2 - ps2.py|par2/ps2.py]]
- [[Code/par2 - ps3.py|par2/ps3.py]]
- [[Code/par2 - ps4.py|par2/ps4.py]]
- [[Code/par2 - ps5.py|par2/ps5.py]]
- [[Code/para - ar1.py|para/ar1.py]]
- [[Code/para - ar2.py|para/ar2.py]]
- [[Code/pat - fix1.py|pat/fix1.py]]
- [[Code/restyle.py|restyle.py]]

## Engine snapshot

- [[Code/engine - bios.py]]
- [[Code/engine - style.css]]
- [[Code/engine - make_theme.py]]
