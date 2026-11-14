---
source: BIOS-Obsidian/tools/scripts/research-mcq1/q.py
handouts: [research-lec1-principles-mcq]
saved: 2026-11-14
tags: [bios, code]
---
# research-mcq1/q.py

```python
import sys, json, os, random
sys.path.insert(0, "/tmp/claude-0/-home-user/bbbdedfa-3c9f-5150-ab3b-e66c0ade12b5/scratchpad/work/imm456")
from ci import *            # Q P IM
sys.path.insert(0, "/tmp/claude-0/-home-user/bbbdedfa-3c9f-5150-ab3b-e66c0ade12b5/scratchpad/work"); from bidi import ltr_all

# Principles of Research — Lecture 1 "Principles of Research" (stage 4, ليندا منجد هادي).
# Source: the professor's own MCQ file (3 pages, 19 Q, correct answer highlighted/bold). QUESTIONS ONLY —
# the professor's exact MCQs arranged BIOS-style: every option translated, answer under each (answers_inline),
# 4 questions per page (meta questions.mcq_per_page). No invented SA — faithful to the professor's file.
O = P
FOLDER = "research-lec1-principles-mcq"
W = lambda q, en, ar: dict(q, note_en=en, note_ar=ar)

def balance5(mcq, seed=7):               # like balance() but distributes the answer across all 5 letters a–e
    rnd = random.Random(seed); L = "abcde"
    qs = [q for q in mcq if "answer" in q]
    seq = []
    while len(seq) < len(qs):
        b = list("abcde"); rnd.shuffle(b); seq += b
    for q, t in zip(qs, seq):
        n = len(q["options"]); i = L.index(q["answer"]); j = min(L.index(t), n - 1)
        q["options"][i], q["options"][j] = q["options"][j], q["options"][i]
        q["answer"] = L[j]
    return mcq

mcq = [
 Q("Which is research:", "أيّها يمثّل البحث:",
   O(("A systematic investigation to answer questions, solve problems, or discover information", "تحرٍّ منهجي للإجابة عن الأسئلة أو حلّ المشكلات أو اكتشاف المعلومات"),
     ("A personal belief about a topic", "اعتقاد شخصي حول موضوع"),
     ("A collection of unrelated facts", "مجموعة حقائق غير مترابطة"),
     ("A way to confirm what the researcher already thinks", "طريقة لتأكيد ما يظنّه الباحث مسبقًا"),
     ("A discussion without collecting data", "نقاش دون جمع بيانات")), "a"),
 Q("What is the sequence of research steps:", "ما تسلسل خطوات البحث:",
   O(("Question → Investigation → Data → Analysis → Answer", "السؤال ← التحرّي ← البيانات ← التحليل ← الإجابة"),
     ("Answer → Question → Data → Investigation → Analysis", "الإجابة ← السؤال ← البيانات ← التحرّي ← التحليل"),
     ("Data → Opinion → Answer → Question", "البيانات ← الرأي ← الإجابة ← السؤال"),
     ("Observation → Conclusion → Data → Question", "الملاحظة ← الاستنتاج ← البيانات ← السؤال"),
     ("Analysis → Investigation → Question → Answer", "التحليل ← التحرّي ← السؤال ← الإجابة")), "a"),
 Q("Scientific research is :", "البحث العلمي هو:",
   O(("Scientific methods and evidence", "المناهج العلمية والأدلّة"),
     ("Personal experience alone", "الخبرة الشخصية وحدها"),
     ("Popular opinions and assumptions", "الآراء الشائعة والافتراضات"),
     ("AI-generated conclusions", "استنتاجات مولّدة بالذكاء الاصطناعي"),
     ("Unverified observations", "ملاحظات غير محقَّقة")), "a"),
 Q("Which is a valid reason to conduct research:", "أيّها سبب وجيه لإجراء البحث:",
   O(("To compare groups or methods", "لمقارنة المجموعات أو الطرائق"),
     ("To ensure a preferred treatment appears effective", "لضمان أن يبدو علاج مفضَّل فعّالًا"),
     ("To avoid collecting data", "لتجنّب جمع البيانات"),
     ("To replace evidence with experience", "لاستبدال الأدلّة بالخبرة"),
     ("To prove an assumption", "لإثبات افتراض مسبق")), "a"),
 Q("A researcher notices anemia among several students. What is needed before concluding it is common among university students:", "لاحظ باحث فقر دم بين عدّة طلاب. ما المطلوب قبل استنتاج أنه شائع بين طلبة الجامعة:",
   O(("Evidence collected through an appropriate investigation", "أدلّة مجموعة عبر تحرٍّ مناسب"),
     ("stronger personal opinion", "رأي شخصي أقوى"),
     ("A more confident statement", "عبارة أكثر ثقة"),
     ("An AI-generated explanation", "تفسير مولّد بالذكاء الاصطناعي"),
     ("A single additional observation", "ملاحظة إضافية واحدة")), "a"),
 Q("Which research principle means conclusions should rely on facts rather than personal opinions:", "أيّ مبدأ بحثي يعني أن تعتمد الاستنتاجات على الحقائق لا على الآراء الشخصية:",
   O(("Objectivity", "الموضوعية"),
     ("Feasibility", "الجدوى"),
     ("Relevance", "الصلة (الملاءمة)"),
     ("Verifiability", "القابلية للتحقّق"),
     ("Accuracy", "الدقّة")), "a"),
 Q("Following organized and logical steps demonstrates which principle:", "اتّباع خطوات منظّمة ومنطقية يجسّد أيّ مبدأ:",
   O(("Systematic approach", "المنهج المنظّم (المنهجية)"),
     ("Research ethics", "أخلاقيات البحث"),
     ("Feasibility", "الجدوى"),
     ("Objectivity", "الموضوعية"),
     ("Relevance", "الصلة (الملاءمة)")), "a"),
 Q("What does verification require:", "ما الذي يتطلّبه التحقّق:",
   O(("Methods and results that can be checked", "طرائق ونتائج يمكن فحصها"),
     ("A result that agrees with the hypothesis", "نتيجة تتّفق مع الفرضية"),
     ("Data collected from only one source", "بيانات مجموعة من مصدر واحد فقط"),
     ("The researcher to select the outcome", "أن يختار الباحث المحصّلة"),
     ("AI to confirm all findings", "أن يؤكّد الذكاء الاصطناعي كل النتائج")), "a"),
 Q("Which action is part of research ethics:", "أيّ إجراء جزء من أخلاقيات البحث:",
   O(("Protecting participants' rights, privacy, and safety", "حماية حقوق المشاركين وخصوصيتهم وسلامتهم"),
     ("Sharing participant identities to improve transparency", "مشاركة هويات المشاركين لتحسين الشفافية"),
     ("Avoiding consent to save time", "تجنّب أخذ الموافقة لتوفير الوقت"),
     ("Changing results to protect participants", "تغيير النتائج لحماية المشاركين"),
     ("Entering identifiable patient information into any AI tool", "إدخال معلومات مريض قابلة للتعريف في أيّ أداة ذكاء اصطناعي")), "a"),
 Q("The researcher asks; for the data answer because:", "يسأل الباحث؛ لتأتي الإجابة من البيانات، لأنّ:",
   O(("Conclusions should follow the evidence rather than a desired result", "الاستنتاجات يجب أن تتبع الأدلّة لا نتيجةً مرغوبة"),
     ("Researchers should decide the outcome before data collection", "على الباحثين تحديد المحصّلة قبل جمع البيانات"),
     ("Data are unnecessary when a question is clear", "البيانات غير ضرورية عندما يكون السؤال واضحًا"),
     ("Researchers should avoid asking focused questions", "على الباحثين تجنّب طرح أسئلة مركّزة"),
     ("The answer should be chosen to match the hypothesis", "يجب اختيار الجواب ليطابق الفرضية")), "a"),
 Q("What is meant by a feasible study:", "ما المقصود بالدراسة القابلة للتنفيذ (الجدوى):",
   O(("A study that can be done with available time, participants, equipment, and resources", "دراسة يمكن إنجازها بالوقت والمشاركين والمعدّات والموارد المتاحة"),
     ("A study guaranteed to produce significant results", "دراسة مضمونة إنتاج نتائج ذات دلالة"),
     ("A study that avoids ethical review", "دراسة تتجنّب المراجعة الأخلاقية"),
     ("A study that requires no planning", "دراسة لا تتطلّب تخطيطًا"),
     ("A study using only large samples", "دراسة تستعمل عيّنات كبيرة فقط")), "a"),
 Q("Which is the correct sequence of research pathway:", "ما التسلسل الصحيح لمسار البحث:",
   O(("Observation → Research problem → Research question → Research plan → Data collection → Data analysis → Results → Discussion → Conclusion", "الملاحظة ← مشكلة البحث ← سؤال البحث ← خطة البحث ← جمع البيانات ← تحليل البيانات ← النتائج ← المناقشة ← الاستنتاج"),
     ("Research plan → Conclusion → Observation → Results → Question", "خطة البحث ← الاستنتاج ← الملاحظة ← النتائج ← السؤال"),
     ("Data analysis → Question → Research problem → Observation → Conclusion", "تحليل البيانات ← السؤال ← مشكلة البحث ← الملاحظة ← الاستنتاج"),
     ("Observation → Results → Data collection → Question → Discussion", "الملاحظة ← النتائج ← جمع البيانات ← السؤال ← المناقشة"),
     ("Research question → Conclusion → Data collection → Research plan → Results", "سؤال البحث ← الاستنتاج ← جمع البيانات ← خطة البحث ← النتائج")), "a"),
 Q("What is the proposed laboratory investigation for finding the causal bacteria:", "ما التحرّي المختبري المقترح لإيجاد البكتيريا المسبِّبة:",
   O(("Culture and identification", "الزرع والتشخيص (التعريف)"),
     ("Blood pressure measurement", "قياس ضغط الدم"),
     ("Questionnaire scoring", "تسجيل درجات الاستبيان"),
     ("PCR only", "PCR فقط"),
     ("Microscopic cell counting only", "عدّ الخلايا مجهريًا فقط")), "a"),
 Q("Which is an example of a research question from hematology:", "أيّها مثال على سؤال بحثي من أمراض الدم:",
   O(("How common is anemia in a specific population?", "ما مدى شيوع فقر الدم في مجتمع محدّد؟"),
     ("Can PCR detect a pathogen in clinical samples?", "هل يستطيع PCR كشف ممرض في العيّنات السريرية؟"),
     ("Are inflammatory markers elevated in a certain disease?", "هل ترتفع الواسمات الالتهابية في مرض معيّن؟"),
     ("What are the most common bacteria isolated from UTI cases?", "ما أكثر البكتيريا شيوعًا المعزولة من حالات التهاب المسالك البولية (UTI)؟"),
     ("Which treatment do patients prefer?", "أيّ علاج يفضّله المرضى؟")), "a"),
 Q("What should a researcher do with AI-generated references:", "ماذا يجب أن يفعل الباحث بالمراجع المولّدة بالذكاء الاصطناعي:",
   O(("Check and verify them", "فحصها والتحقّق منها"),
     ("Trust them if they look complete", "الوثوق بها إذا بدت كاملة"),
     ("Use them only when the AI is confident", "استعمالها فقط حين يكون الذكاء الاصطناعي واثقًا"),
     ("Assume they are accurate when cited", "افتراض أنها دقيقة ما دامت مُستشهَدًا بها"),
     ("Avoid reviewing them", "تجنّب مراجعتها")), "a"),
 Q("Which information should never be entered into unapproved AI tools:", "أيّ معلومات يجب ألّا تُدخَل أبدًا في أدوات ذكاء اصطناعي غير معتمدة:",
   O(("Confidential patient information", "معلومات المريض السرّية"),
     ("Publicly available keywords", "كلمات مفتاحية متاحة للعموم"),
     ("A general research topic", "موضوع بحثي عام"),
     ("A broad concept for explanation", "مفهوم عام للتوضيح"),
     ("A draft research question without personal data", "مسودّة سؤال بحثي دون بيانات شخصية")), "a"),
 Q("What is the recommended way to handle AI output:", "ما الطريقة المُوصى بها للتعامل مع مُخرَجات الذكاء الاصطناعي:",
   O(("AI Output → Critical Thinking → Verification", "مُخرَج الذكاء الاصطناعي ← التفكير النقدي ← التحقّق"),
     ("AI Output → Copy → Submit", "مُخرَج الذكاء الاصطناعي ← نسخ ← تسليم"),
     ("AI Output → Conclusion → Publication", "مُخرَج الذكاء الاصطناعي ← استنتاج ← نشر"),
     ("AI Output → Trust → Citation", "مُخرَج الذكاء الاصطناعي ← ثقة ← استشهاد"),
     ("AI Output → Replace Data → Report", "مُخرَج الذكاء الاصطناعي ← استبدال البيانات ← تقرير")), "a"),
 W(Q("The medical laboratory practice help to evaluate:", "تساعد الممارسة المختبرية الطبية على تقييم:",
   O(("Tests or treatments", "الفحوص أو العلاجات"),
     ("Only student opinions", "آراء الطلاب فقط"),
     ("Only laboratory equipment prices", "أسعار معدّات المختبر فقط"),
     ("Personal preferences without evidence", "التفضيلات الشخصية دون أدلّة"),
     ("Unrelated social trends", "اتجاهات اجتماعية غير ذات صلة")), "a"),
   "Source typo: in the professor's file option B was mistyped “A. Only student opinions” (stray “A.”). The stem also reads “practice help” — kept verbatim; the intended wording is “laboratory practice helps to evaluate”.",
   "خطأ مطبعي في الأصل: في ملف الدكتور كُتب الخيار B خطأً «A. Only student opinions» (بزيادة «A.»). كما ورد في السؤال «practice help» — أُبقي حرفيًا، والمقصود «laboratory practice helps to evaluate»."),
 Q("In antibiotic resistance, what is a suitable next step after noticing the observation:", "في مقاومة المضادات الحيوية، ما الخطوة التالية المناسبة بعد ملاحظة المشاهدة:",
   O(("Formulate a research question and identify the data needed", "صياغة سؤال بحثي وتحديد البيانات اللازمة"),
     ("Declare resistance is increasing everywhere", "إعلان أن المقاومة تتزايد في كل مكان"),
     ("Ask AI to invent a conclusion", "الطلب من الذكاء الاصطناعي اختلاق استنتاج"),
     ("Change the laboratory results", "تغيير نتائج المختبر"),
     ("Ignore the observation because it is not proof", "تجاهل المشاهدة لأنها ليست دليلًا")), "a"),
]
mcq = balance5(mcq, 111)

meta = {"subject_en": "Principles of Research", "subject_ar": "مبادئ البحث العلمي", "short_ar": "مبادئ البحث", "instructor": "ليندا منجد هادي",
        "unit_en": "Lecture 1", "unit_ar": "المحاضرة 1", "unit_label": "LEC", "unit_no": "1",
        "title_en": "Principles of Research", "title_ar": "مبادئ البحث",
        "kind": "Theory — نظري", "stage": "The fourth stage — الرابعة",
        "file_name": "BIOS - مبادئ البحث نظري المحاضرة الأولى - الأسئلة"}

Qs = {"title_en": "Principles of Research (Lecture 1) — MCQs", "title_ar": "مبادئ البحث (المحاضرة الأولى) — أسئلة اختيار من متعدّد",
      "sub": "MCQs", "answers_inline": True, "mcq_per_page": 4, "compact": True,
      "mcq_en": "Multiple-choice questions", "mcq_ar": "أسئلة الاختيار من متعدّد",
      "mcq": ltr_all(mcq), "tf": [], "traps": [], "important": []}
d = "/home/user/-/" + FOLDER
os.makedirs(d, exist_ok=True)
json.dump({"meta": meta, "questions": Qs}, open(d + "/lecture.json", "w"), ensure_ascii=False, indent=1)
from collections import Counter
qs = [m for m in mcq if "answer" in m]
print(FOLDER, len(qs), "MCQ", dict(sorted(Counter(m["answer"] for m in qs).items())), "| notes:", sum(1 for m in qs if m.get("note_en")))

```
