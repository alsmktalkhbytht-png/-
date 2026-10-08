import re
import lib3
from lib3 import *
from art2 import biohazard, radiation

# bold-italic species names: __x__
_md = lib3.md
def md2(s):
    return re.sub(r"__(.+?)__", r'<i class="sp">\1</i>', _md(s))
lib3.md = md2

X = r"""
i.sp{font-weight:700;font-style:italic}
.ar i.sp{font-family:Mada;font-size:.86em}
.side{display:grid;grid-template-columns:1fr 34mm;gap:4.5mm;align-items:start}
.side figcaption{display:block;text-align:center;font-size:7.8pt;line-height:1.35}
.side figcaption span{display:block}
.sym{display:flex;justify-content:space-around;padding:1.5mm 0 .5mm}
.sym div{text-align:center}
.sym svg{width:25mm}
.sym .l1{font-weight:800;font-size:9.5pt;color:var(--burg);margin-top:1mm}
.sym .l2{font-weight:800;font-size:10.5pt;color:#222}
"""

def rgc(n, col, te, ta, e, a):
    return rg(n, col, te, ta, e, a)

COL = ["#6F8B72", "#B08A3E", "#A65A34", "#6E1F2A"]

SUM = ('<div class="sum"><span class="pillh">Summary <span dir="rtl">خلاصة الجدول</span></span>'
       '<table class="tb"><tr><th>Risk group</th><th dir="rtl">مجموعة الخطورة</th><th>Biosafety level</th><th dir="rtl">مستوى السلامة الحيوية</th></tr>'
       + "".join(f'<tr><td>{n} — {e}</td><td class="a">{n} — {a}</td><td class="k">Biosafety level {n}</td><td class="a" style="font-weight:500">المستوى {n}</td></tr>'
                 for n, e, a in [(1, "Minimal risk", "خطورة ضئيلة"), (2, "Moderate risk", "خطورة متوسطة"), (3, "High risk", "خطورة عالية"), (4, "Extreme risk", "خطورة قصوى")])
       + "</table></div>")

LABELS = [("Class I biosafety cabinet", "خزانة السلامة الحيوية من الصنف الأول", False),
          ("Mini Biosafety cabinet", "خزانة سلامة حيوية صغيرة", False),
          ("[Class] II Biosafety cabinet", "خزانة السلامة الحيوية من الصنف الثاني", True),
          ("[…] Bio Cabinet", "خزانة سلامة حيوية", True),
          ("[…]F Biosafety cabinet", "خزانة سلامة حيوية", True),
          ("Class III Biosafety Cabinet", "خزانة السلامة الحيوية من الصنف الثالث", False),
          ("Ducted and Ductless Fume Hood", "خزانة سحب الأبخرة (بمجرى هواء وبدون مجرى)", False),
          ("Laminar flow Cabinet", "خزانة التدفق الهوائي الصفائحي", False),
          ("PCR Cabinet", "خزانة PCR", False),
          ("Autoclave", "جهاز التعقيم بالبخار المضغوط (الأوتوكليف)", False),
          ("Incubator", "الحاضنة", False)]
LTAB = ('<table class="tb lab"><tr><th style="width:10mm">#</th><th style="width:72mm">Label (English)</th><th dir="rtl" style="text-align:right">التسمية بالعربية</th></tr>'
        + "".join(f'<tr><td style="text-align:center;color:var(--burg);font-weight:800">{i}</td><td class="k">{e}{" <span style=\'color:#B08A3E\'>*</span>" if s else ""}</td><td class="a" style="font-weight:500">{a}</td></tr>'
                  for i, (e, a, s) in enumerate(LABELS, 1)) + "</table>")

SYM = (f'<div class="sym"><div>{biohazard(tri="#F2C318", fill="#111", edge="#111")}<div class="l1">BIOHAZARD</div><div class="l2" dir="rtl">خطر بيولوجي</div></div>'
       f'<div>{radiation(tri="#F2C318", fill="#111", edge="#111")}<div class="l1">RADIATION HAZARD</div><div class="l2" dir="rtl">خطر إشعاعي</div></div></div>')

P = []
# ---------------- page 1
P.append(labtitle()
  + sec(1, "Biosafety Levels", "مستويات السلامة الحيوية")
  + '<div class="side"><div>'
  + card("**Biosafety levels:** They are principles and application used to protect laboratory workers and the surrounding environment from exposure to danger while working with living organisms.",
         "**مستويات السلامة الحيوية (`Biosafety levels`):** هي مبادئ وتطبيقات تُستخدم لحماية العاملين في المختبر والبيئة المحيطة من التعرض للخطر في أثناء العمل مع الكائنات الحية.")
  + card("**It aims to:** provide the highest level of protection and the lowest range of exposure.",
         "**وتهدف إلى:** توفير أعلى مستوى من الحماية وأدنى حدٍّ من التعرض.")
  + '</div>' + fig("assets/labsafety.jpg", "Lab safety", "سلامة المختبر") + '</div>'
  + '<div style="height:3mm"></div>'
  + sec(2, "Risk Groups", "مجموعات الخطورة")
  + card("**Risk groups:** are used to assess risk, determine its source and how to deal with it, includes 4 groups:",
         "**مجموعات الخطورة (`Risk groups`):** تُستخدم لتقييم الخطر وتحديد مصدره وكيفية التعامل معه، وتشمل 4 مجموعات:")
  + rgc(1, COL[0], "Risk group 1 — (Minimal risk)", "مجموعة الخطورة 1 — (خطورة ضئيلة)",
        "**Non-pathogenic** factors in healthy people and adults (with little or no risk). __E. coli__, __Bacillus subtilis__",
        "عوامل **غير ممرضة** للأشخاص الأصحاء والبالغين (خطورتها قليلة أو معدومة). `__E. coli__`، `__Bacillus subtilis__`"))
# ---------------- page 2
P.append(
    rgc(2, COL[1], "Risk group 2 — (Moderate risk)", "مجموعة الخطورة 2 — (خطورة متوسطة)",
        "Factors related to **human infection** and **treatment is possible** in this case (moderate risk and **limited** risk of spread). __E. coli__ pathogenic strain, __Brucella__ spp., __Salmonella__ spp.",
        "عوامل ترتبط **بإصابة الإنسان بالعدوى**، و**علاجها ممكن** في هذه الحالة (خطورة متوسطة وخطر انتشار **محدود**). السلالة الممرضة من `__E. coli__`، وأنواع `__Brucella spp.__`، وأنواع `__Salmonella spp.__`")
  + rgc(3, COL[2], "Risk group 3 — (High risk)", "مجموعة الخطورة 3 — (خطورة عالية)",
        "Factors that cause serious and fatal infections to humans and their **treatment is not easy**, specially for immunosuppressed persons (with a high risk for individuals). __Salmonella typhi__. __Mycobacterium tuberculosis__.",
        "عوامل تسبب للإنسان أنواع عدوى خطيرة ومميتة، و**علاجها ليس سهلًا**، ولا سيما لدى الأشخاص المثبَّطين مناعيًا (خطورة عالية على الأفراد). `__Salmonella typhi__`. `__Mycobacterium tuberculosis__`.")
  + rgc(4, COL[3], "Risk group 4 — (Extreme risk)", "مجموعة الخطورة 4 — (خطورة قصوى)",
        "Factor that are fatal to humans are easily transmitted from … [[cut]]",
        "عوامل مميتة للإنسان وتنتقل بسهولة من … [[قطع]]")
  + '<div style="height:2mm"></div>' + SUM)
# ---------------- page 3
P.append(
    sec(3, "Biohazard Symbol", "رمز الخطر البيولوجي")
  + card("**Biohazard symbol:** it used to warn people of the potential for the presence dangerous biological materials such as:",
         "**رمز الخطر البيولوجي (`Biohazard symbol`):** يُستخدم لتحذير الأشخاص من احتمال وجود مواد بيولوجية خطرة، مثل:",
         e_extra=nlist(["Cultures of pathogens.", "Human Blood and Tissue.", "Corridors leading to the laboratories."]),
         a_extra=nlist(["مزارع الأحياء الممرضة (`Cultures of pathogens`).", "دم الإنسان وأنسجته.", "الممرات المؤدية إلى المختبرات."], rtl=True))
  + fig(None, "Warning symbols (redrawn in high resolution)", "رموز التحذير (أُعيد رسمها بدقة عالية)", inner=SYM)
  + sec(4, "Laboratory Safety Considerations", "اعتبارات السلامة في المختبر")
  + rule(1, "Wear protective clothing (clean lab. coat – **gloves** – **mask** – safety **glasses**).",
            "ارتدِ الملابس الواقية (صدرية مختبر نظيفة – **قفازات** – **كمّامة** – **نظارات** السلامة).")
  + fig("assets/ppe.jpg", "Personal protective equipment", "معدات الحماية الشخصية", h="27mm", fit="cover"))
# ---------------- page 4
P.append(
    rule(2, "Avoid touching objects (pencils, cell phones, door handles, e.g.) while wearing gloves. And pencils, labels, or any other materials should never be placed in your mouth.",
            "تجنّب لمس الأشياء (مثل الأقلام والهواتف المحمولة ومقابض الأبواب) في أثناء ارتداء القفازات. ولا يجوز أبدًا وضع الأقلام أو الملصقات أو أي مواد أخرى في فمك.")
  + rule(3, "Do not eat food or drink water in the lab. Do not use lab glassware as food or water containers.",
            "لا تتناول الطعام ولا تشرب الماء في المختبر. ولا تستخدم الأواني الزجاجية المختبرية أوعيةً للطعام أو الماء.")
  + rule(4, "Long hair must be tied back or covered to minimize fire hazard or contamination of experiment.",
            "يجب ربط الشعر الطويل إلى الخلف أو تغطيته لتقليل خطر الحريق أو تلوث التجربة.")
  + rule(5, "Do not take any cultures out of the lab for any reason, all cultures should be handled as potentially pathogenic.",
            "لا تُخرج أي مزرعة من المختبر لأي سبب كان، ويجب التعامل مع جميع المزارع على أنها ممرضة محتملة.")
  + '<div class="fig2">' + fig("assets/nofood.jpg", "No food or drink", "ممنوع الطعام والشراب", h="44mm", fit="cover")
  + fig("assets/cultures.jpg", "Bacterial cultures", "مزارع بكتيرية", h="44mm", fit="cover") + '</div>')
# ---------------- page 5
P.append(
    rule(6, "Wash hands after working with infectious materials.", "اغسل يديك بعد العمل مع المواد المُعدية.")
  + rule(7, "Disinfect all instruments immediately after use.", "طهّر جميع الأدوات فور الانتهاء من استخدامها.")
  + rule(8, "Disinfect all contaminated waste before discarding.", "طهّر جميع النفايات الملوثة قبل التخلص منها.")
  + '<div class="fig2">' + fig("assets/handwash.jpg", "Hand washing", "غسل اليدين", h="44mm", fit="cover")
  + fig("assets/disinfect.jpg", "Disinfecting instruments and surfaces", "تطهير الأدوات والأسطح", h="44mm", fit="cover") + '</div>'
  + sec(5, "Important Definitions", "تعريفات مهمة")
  + card("**Sterilization:** is the complete killing or removal of all living organism such as cell spore, viruses, fungi, ….",
         "**التعقيم (`Sterilization`):** هو القتل أو الإزالة الكاملة لجميع الكائنات الحية، مثل الأبواغ (`Spores`) والفيروسات والفطريات، ….")
  + card("**Disinfection:** the destruction or removal of pathogens **but not bacterial spores**, usually used only on inanimate object.",
         "**التطهير (`Disinfection`):** إتلاف الأحياء الممرضة أو إزالتها **ولكن ليس الأبواغ البكتيرية**، ويُستخدم عادةً على الأجسام غير الحية فقط."))
# ---------------- page 6
P.append(
    card("**Antiseptics:** chemicals applied to **body surfaces** to destroy or inhibit pathogens.",
         "**المطهرات الموضعية (`Antiseptics`):** مواد كيميائية توضع على **سطوح الجسم** لإتلاف الأحياء الممرضة أو تثبيطها.")
  + card("**Decontamination:** the mechanical removal of most microbes by using washing, heat or disinfectants.",
         "**إزالة التلوث (`Decontamination`):** الإزالة الميكانيكية لمعظم الميكروبات باستخدام الغسل أو الحرارة أو المطهرات.")
  + card("**Biological laboratory:** A facility within which microorganisms, their components or their derivatives are collected, handled and/or stored.",
         "**المختبر البيولوجي (`Biological laboratory`):** منشأة تُجمع فيها الأحياء المجهرية أو مكوّناتها أو مشتقاتها، ويُتعامل معها و/أو تُخزَّن.")
  + card("**Bio risk:** The probability or chance that a particular adverse event (accidental infection or loss, theft, misuse, diversion or intentional release), possibly leading to harm.",
         "**الخطر البيولوجي (`Bio risk`):** احتمال أو فرصة وقوع حدث ضار معيّن (عدوى عَرَضية، أو فقدان، أو سرقة، أو إساءة استخدام، أو تحويل عن الغرض، أو إطلاق متعمَّد)، قد يؤدي إلى الأذى.")
  + card("**Bio risk assessment:** The process to identify acceptable and unacceptable risks (embracing biosafety risks (risks of accidental infection) and laboratory biosecurity risks (risks of unauthorized access, loss, theft, misuse, diversion or intentional release)) and their potential consequences.",
         "**تقييم الخطر البيولوجي (`Bio risk assessment`):** عملية تحديد المخاطر المقبولة وغير المقبولة (وتشمل مخاطر السلامة الحيوية (مخاطر العدوى العَرَضية)، ومخاطر الأمن البيولوجي المختبري (مخاطر الوصول غير المصرَّح به، أو الفقدان، أو السرقة، أو إساءة الاستخدام، أو التحويل عن الغرض، أو الإطلاق المتعمَّد))، وعواقبها المحتملة."))
# ---------------- page 7
P.append(
    sec(6, "Biosafety Cabinet", "خزانة السلامة الحيوية")
  + fig(None, "Biosafety cabinets and laboratory equipment", "خزانات السلامة الحيوية وأجهزة مختبرية",
        inner='<img src="assets/cabinets.jpg" style="width:118mm;display:block;margin:0 auto">')
  + h2("Labels in the figure", "تسميات الشكل") + LTAB + '<div style="height:3.4mm"></div>'
  + note("* Labels 3–5 are partly hidden by a watermark in the original image; only the readable parts are shown.",
         "* التسميات 3–5 مغطّاة جزئيًا بعلامة مائية في الصورة الأصلية، لذلك كُتب الجزء المقروء منها فقط."))

def build():
    pages = [cover("Lab 1 — Rules and Biosafety Levels", "العملي 1 — القواعد ومستويات السلامة الحيوية",
                   [("Department", "القسم", "قسم التحليلات"), ("Stage", "المرحلة", "The fourth stage — الرابعة"),
                    ("Type", "النوع", "Laboratories — عملي"), ("Translated &amp; edited by", "ترجمة وتعديل", "محمد حامد")])]
    pages += [page(c, i) for i, c in enumerate(P, 1)]
    return pages

if __name__ == "__main__":
    open("booklet.html", "w").write(doc("BIOS - Diagnostic Microbiology - Lab 1", build(), X))
    print("ok")
