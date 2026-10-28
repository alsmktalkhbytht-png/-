import json, os

def C(en, ar, **k): return dict(t="card", en=en, ar=ar, **k)
def R(en, ar): return dict(t="rule", en=en, ar=ar)
def SEC(en, ar): return dict(t="section", en=en, ar=ar)
def N(en, ar, label=None):
    d = dict(t="note", en=en, ar=ar)
    if label: d["label"] = label
    return d
def S(en, ar): return {"en": en, "ar": ar}

blocks = [
 SEC("Think Before We Start", "فكّر قبل أن نبدأ"),
 C("**Can an Observation Become a Scientific Fact?**", "**هل يمكن أن تصبح الملاحظة حقيقة علمية؟**"),
 C("**Example:** “I noticed that many university students have anemia.”", "**مثال:** «لاحظتُ أن كثيرًا من طلبة الجامعة مصابون بفقر الدم.»"),
 C(["Is this enough to conclude that anemia is common among university students?", "**No. We need evidence.**"],
   ["هل هذا كافٍ لنستنتج أن فقر الدم شائع بين طلبة الجامعة؟", "**لا. نحتاج إلى دليل.**"]),

 SEC("What is Research?", "ما البحث؟"),
 C("**Research** is a **systematic investigation** used to:", "**البحث** (`Research`) هو **استقصاء منهجي** يُستعمل من أجل:",
   list_en=["Answer a question", "Solve a problem", "Discover new information"],
   list_ar=["الإجابة عن سؤال", "حلّ مشكلة", "اكتشاف معلومات جديدة"]),
 dict(t="flow", en="Simply:", ar="ببساطة:", steps=[S("Question", "سؤال"), S("Investigation", "استقصاء"), S("Data", "بيانات"), S("Analysis", "تحليل"), S("Answer", "إجابة")]),

 SEC("What is Scientific Research?", "ما البحث العلمي؟"),
 C("**Scientific research** is an **organized process** that uses scientific methods and evidence to answer questions and solve problems.",
   "**البحث العلمي** (`Scientific research`) هو **عملية منظّمة** تستعمل الطرق العلمية والأدلة للإجابة عن الأسئلة وحلّ المشكلات."),
 dict(t="flow", en="In scientific research:", ar="في البحث العلمي:", steps=[S("We ask", "نسأل"), S("We collect", "نجمع"), S("We analyze", "نحلّل"), S("We conclude", "نستنتج")]),

 SEC("Why Do We Conduct Research?", "لماذا نجري البحث؟"),
 C("**Research Helps Us To:**", "**يساعدنا البحث على:**",
   list_en=["**Describe** a health problem", "**Explore** new information", "**Compare** groups or methods", "**Identify associations** between factors",
            "**Evaluate** tests or treatments", "**Improve** healthcare practice"],
   list_ar=["**وصف** مشكلة صحية", "**استكشاف** معلومات جديدة", "**مقارنة** مجموعات أو طرق", "**تحديد الارتباطات** بين العوامل",
            "**تقييم** الفحوص أو العلاجات", "**تحسين** ممارسة الرعاية الصحية"]),
 C("**Examples:**", "**أمثلة:**",
   list_en=["How common is anemia among university students?", "What bacteria are commonly isolated from UTI patients?", "Is smoking associated with increased WBC count?"],
   list_ar=["ما مدى شيوع فقر الدم بين طلبة الجامعة؟", "ما البكتيريا التي تُعزل عادةً من مرضى التهاب المسالك البولية (`UTI`)؟", "هل يرتبط التدخين بزيادة عدد كريات الدم البيض (`WBC`)؟"]),

 SEC("Observation, Opinion, or Evidence?", "ملاحظة أم رأي أم دليل؟"),
 C("**Which One is Scientific Evidence?**", "**أيّها دليل علمي؟**", alpha=True,
   list_en=["“I think vitamin D deficiency is common among young adults.”", "“I noticed that many people have low vitamin D.”", "“Among 300 tested participants, 42% had vitamin D deficiency.”"],
   list_ar=["«أعتقد أن نقص فيتامين D شائع بين الشباب.» (رأي)", "«لاحظتُ أن كثيرًا من الناس لديهم انخفاض في فيتامين D.» (ملاحظة)", "«من بين 300 مشارك جرى فحصهم، كان لدى 42% نقص في فيتامين D.» (دليل)"]),
 N(["**Answer: C — Evidence**", "**Opinion ≠ Evidence**", "Observation can start research, but observation alone is not [[cut]]"],
   ["**الإجابة: C — دليل**", "**الرأي ≠ الدليل**", "قد تبدأ الملاحظة بحثًا، لكن الملاحظة وحدها ليست [[قطع]]"], ["Answer", "الإجابة"]),

 SEC("Basic Principles of Research", "المبادئ الأساسية للبحث"),
 R(["**Objectivity**", "Research should be based on facts, not personal opinions."], ["**الموضوعية** (`Objectivity`)", "يجب أن يُبنى البحث على الحقائق، لا على الآراء الشخصية."]),
 R(["**Systematic Approach**", "Research should follow organized and logical steps."], ["**النهج المنهجي** (`Systematic Approach`)", "يجب أن يتبع البحث خطوات منظّمة ومنطقية."]),
 R(["**Accuracy**", "Data should be collected and measured accurately."], ["**الدقة** (`Accuracy`)", "يجب جمع البيانات وقياسها بدقة."]),
 R(["**Evidence-Based**", "Conclusions should be supported by data."], ["**القائم على الدليل** (`Evidence-Based`)", "يجب أن تكون الاستنتاجات مدعومة بالبيانات."]),
 R(["**Verifiability**", "Methods and results should be open to checking."], ["**قابلية التحقق** (`Verifiability`)", "يجب أن تكون الطرق والنتائج قابلة للتدقيق."]),
 R("**Research Ethics**", "**أخلاقيات البحث** (`Research Ethics`)"),

 SEC("A Researcher Does Not Choose the Result", "الباحث لا يختار النتيجة"),
 C(["**Incorrect Approach** ✗", "“I want to prove that energy drinks cause heart palpitations.”"],
   ["**النهج الخاطئ** ✗", "«أريد أن أثبت أن مشروبات الطاقة تسبب خفقان القلب.»"]),
 C(["**Better Approach** ✓", "“Is there an association between energy drink consumption and heart palpitations among university students?”"],
   ["**النهج الأفضل** ✓", "«هل يوجد ارتباط بين تناول مشروبات الطاقة وخفقان القلب بين طلبة الجامعة؟»"]),
 N(["\\*\\*The researcher asks.", "The data answer.\\*\\*"], ["الباحث يسأل.", "والبيانات تجيب."], ["Remember", "تذكّر"]),

 SEC("From Observation to Research", "من الملاحظة إلى البحث"),
 dict(t="flow", steps=[
   dict(en="Observation", ar="الملاحظة", text_en="Many UTI samples appear to contain __E. coli__.", text_ar="يبدو أن كثيرًا من عيّنات التهاب المسالك البولية تحتوي `__E. coli__`."),
   dict(en="Research Question", ar="سؤال البحث", text_en="How common is __E. coli__ among patients with UTI?", text_ar="ما مدى شيوع `__E. coli__` بين مرضى التهاب المسالك البولية؟"),
   dict(en="Data Collection", ar="جمع البيانات", text_en="Urine samples", text_ar="عيّنات الإدرار")],
   tail_en="↓ [[cut]]", tail_ar="↓ [[قطع]]"),

 SEC("Characteristics of Good Research", "خصائص البحث الجيد"),
 C("**Good Research Should Be:**", "**يجب أن يكون البحث الجيد:**",
   list_en=["Clear", "Systematic", "Objective", "Accurate", "Feasible", "Ethical", "Relevant"],
   list_ar=["واضحًا", "منهجيًا", "موضوعيًا", "دقيقًا", "قابلًا للتنفيذ (`Feasible`)", "أخلاقيًا", "ذا صلة (مهمًا)"]),
 C(["**What Does “Feasible” Mean?**", "Can the study actually be done with the available time, participants, equipment, and resources?"],
   ["**ماذا تعني «قابلية التنفيذ»؟**", "هل يمكن إجراء الدراسة فعلًا بالوقت والمشاركين والأجهزة والموارد المتاحة؟"]),

 SEC("Research in Medical Laboratory Technology", "البحث في تقنيات المختبرات الطبية"),
 C("**Research Questions Can Come From Daily Laboratory Practice:**", "**يمكن أن تأتي أسئلة البحث من الممارسة المختبرية اليومية:**"),
 R(["**Hematology**", "How common is anemia in a specific population?"], ["**أمراض الدم** (`Hematology`)", "ما مدى شيوع فقر الدم في مجتمع معيّن؟"]),
 R(["**Microbiology**", "What are the most common bacteria isolated from UTI cases?"], ["**الأحياء المجهرية** (`Microbiology`)", "ما أكثر البكتيريا شيوعًا التي تُعزل من حالات التهاب المسالك البولية؟"]),
 R(["**Immunology**", "Are inflammatory markers elevated in a certain disease?"], ["**المناعة** (`Immunology`)", "هل ترتفع مؤشرات الالتهاب في مرض معيّن؟"]),
 R(["**Molecular Biology**", "Can PCR detect a pathogen in clinical samples?"], ["**البيولوجيا الجزيئية** (`Molecular Biology`)", "هل يستطيع `PCR` الكشف عن مُمرِض في العيّنات السريرية؟"]),

 SEC("Artificial Intelligence in Research", "الذكاء الاصطناعي في البحث"),
 C(["**Can AI Help Researchers?**", "**AI Can Assist With:**"], ["**هل يمكن للذكاء الاصطناعي مساعدة الباحثين؟**", "**يمكن للذكاء الاصطناعي (`AI`) المساعدة في:**"],
   list_en=["**Brainstorming** research ideas", "Developing research questions", "Suggesting keywords", "Organizing information", "Improving scientific language", "Explaining difficult concepts"],
   list_ar=["**العصف الذهني** لأفكار البحث", "تطوير أسئلة البحث", "اقتراح الكلمات المفتاحية", "تنظيم المعلومات", "تحسين اللغة العلمية", "شرح المفاهيم الصعبة"]),
 N("AI can make mistakes and may generate false information or references.", "قد يخطئ الذكاء الاصطناعي، وقد يولّد معلومات أو مراجع زائفة.", ["But…", "لكن…"]),

 SEC("Use AI Critically", "استعمل الذكاء الاصطناعي بعين ناقدة"),
 C(["**Poor Prompt**", "“Write a research about anemia.”"], ["**طلب (موجّه) ضعيف**", "«اكتب بحثًا عن فقر الدم.»"]),
 C("**Why is it poor?**", "**لماذا هو ضعيف؟**",
   list_en=["Too broad", "No population", "No specific question", "No clear purpose"],
   list_ar=["واسع جدًا", "لا يحدّد مجتمع الدراسة", "لا يوجد سؤال محدّد", "لا يوجد هدف واضح"]),
 C(["**Better Prompt**", "“Suggest five measurable research questions about anemia among university students. Do not assume the results.”", "Then: [[cut]]"],
   ["**طلب (موجّه) أفضل**", "«اقترح خمسة أسئلة بحثية قابلة للقياس عن فقر الدم بين طلبة الجامعة. لا تفترض النتائج.»", "ثم: [[قطع]]"]),

 SEC("AI: What Should We Never Do?", "الذكاء الاصطناعي: ما الذي لا يجب أن نفعله أبدًا؟"),
 C("**Never:**", "**لا تفعل أبدًا:**",
   list_en=["✗ Trust AI-generated references without checking them.", "✗ Allow AI to invent or modify research results.",
            "✗ Enter confidential patient information into unapproved AI tools.", "✗ Copy AI-generated text without reviewing and understanding it."],
   list_ar=["✗ الوثوق بالمراجع التي يولّدها الذكاء الاصطناعي من دون التحقق منها.", "✗ السماح للذكاء الاصطناعي باختلاق نتائج البحث أو تعديلها.",
            "✗ إدخال معلومات المرضى السرّية في أدوات ذكاء اصطناعي غير معتمدة.", "✗ نسخ النص الذي يولّده الذكاء الاصطناعي من دون مراجعته وفهمه."]),
 dict(t="flow", en="Always:", ar="دائمًا:", steps=[S("Think", "فكّر"), S("Check", "تحقّق"), S("Verify", "تأكّد")]),

 SEC("Class Activity", "نشاط صفّي"),
 C(["**Observation:**", "“Antibiotic resistance appears to be increasing among bacterial isolates in the laboratory.”"],
   ["**الملاحظة:**", "«يبدو أن مقاومة المضادات الحيوية في ازدياد بين العزلات البكتيرية في المختبر.»"]),
 C("**Discuss:**", "**ناقش:**",
   list_en=["What is the problem?", "What would you like to know?", "Write one research question.", "What data would you need?", "How could you collect these data?"],
   list_ar=["ما المشكلة؟", "ماذا تودّ أن تعرف؟", "اكتب سؤالًا بحثيًا واحدًا.", "ما البيانات التي ستحتاج إليها؟", "كيف يمكنك جمع هذه البيانات؟"]),

 SEC("The Big Picture", "الصورة الكاملة"),
 dict(t="flow", en="Research Starts With a Question", ar="البحث يبدأ بسؤال",
      steps=[S("Observation", "الملاحظة"), S("Research Problem", "مشكلة البحث"), S("Research Question", "سؤال البحث"), S("Research Plan", "خطة البحث"),
             S("Data Collection", "جمع البيانات"), S("Data Analysis", "تحليل البيانات"), S("Results", "النتائج")]),
]

def M(en, ar, o, a): return {"en": en, "ar": ar, "options": o, "answer": a}
mcq = [
 M("Research is defined as a:", "يُعرَّف البحث بأنه:", [["Personal opinion", "رأي شخصي"], ["Systematic investigation", "استقصاء منهجي"], ["Single observation", "ملاحظة واحدة"], ["Random guess", "تخمين عشوائي"]], "b"),
 M("Which of the following is NOT a purpose of research as stated in the lecture?", "أيٌّ مما يأتي ليس من أهداف البحث المذكورة في المحاضرة؟", [["Answer a question", "الإجابة عن سؤال"], ["Solve a problem", "حلّ مشكلة"], ["Prove a result chosen in advance", "إثبات نتيجة مختارة مسبقًا"], ["Discover new information", "اكتشاف معلومات جديدة"]], "c"),
 M("The correct order of the research process is:", "الترتيب الصحيح لعملية البحث هو:", [["Question → Investigation → Data → Analysis → Answer", "سؤال ← استقصاء ← بيانات ← تحليل ← إجابة"], ["Answer → Data → Question → Analysis", "إجابة ← بيانات ← سؤال ← تحليل"], ["Data → Answer → Question → Investigation", "بيانات ← إجابة ← سؤال ← استقصاء"], ["Analysis → Question → Answer → Data", "تحليل ← سؤال ← إجابة ← بيانات"]], "a"),
 M("Scientific research uses ___ to answer questions and solve problems.", "يستعمل البحث العلمي ___ للإجابة عن الأسئلة وحلّ المشكلات.", [["Personal opinions", "الآراء الشخصية"], ["Rumours", "الشائعات"], ["Assumed results", "النتائج المفترضة"], ["Scientific methods and evidence", "الطرق العلمية والأدلة"]], "d"),
 M("In scientific research, the steps are:", "في البحث العلمي، الخطوات هي:", [["We conclude → we ask → we collect", "نستنتج ← نسأل ← نجمع"], ["We ask → we collect → we analyze → we conclude", "نسأل ← نجمع ← نحلّل ← نستنتج"], ["We collect → we conclude → we ask", "نجمع ← نستنتج ← نسأل"], ["We analyze → we ask → we conclude", "نحلّل ← نسأل ← نستنتج"]], "b"),
 M("“I noticed that many university students have anemia.” This statement is:", "«لاحظتُ أن كثيرًا من طلبة الجامعة مصابون بفقر الدم.» هذه العبارة:", [["Enough to prove anemia is common", "كافية لإثبات أن فقر الدم شائع"], ["Scientific evidence", "دليل علمي"], ["An observation that needs evidence", "ملاحظة تحتاج إلى دليل"], ["A research result", "نتيجة بحث"]], "c"),
 M("Which statement is scientific evidence?", "أيّ عبارة تُعدّ دليلًا علميًا؟", [["“I think vitamin D deficiency is common among young adults.”", "«أعتقد أن نقص فيتامين D شائع بين الشباب.»"], ["“I noticed that many people have low vitamin D.”", "«لاحظتُ أن كثيرًا من الناس لديهم انخفاض في فيتامين D.»"], ["“Among 300 tested participants, 42% had vitamin D deficiency.”", "«من بين 300 مشارك جرى فحصهم، كان لدى 42% نقص في فيتامين D.»"], ["“Everyone says vitamin D is low.”", "«الجميع يقول إن فيتامين D منخفض.»"]], "c"),
 M("“I think vitamin D deficiency is common among young adults” is an example of:", "«أعتقد أن نقص فيتامين D شائع بين الشباب» مثال على:", [["Opinion", "رأي"], ["Evidence", "دليل"], ["Data analysis", "تحليل بيانات"], ["Research result", "نتيجة بحث"]], "a"),
 M("The principle stating that research should be based on facts, not personal opinions, is:", "المبدأ الذي ينصّ على أن البحث يُبنى على الحقائق لا على الآراء الشخصية هو:", [["Accuracy", "الدقة"], ["Verifiability", "قابلية التحقق"], ["Objectivity", "الموضوعية"], ["Feasibility", "قابلية التنفيذ"]], "c"),
 M("“Research should follow organized and logical steps” describes:", "«يجب أن يتبع البحث خطوات منظّمة ومنطقية» يصف:", [["Systematic approach", "النهج المنهجي"], ["Research ethics", "أخلاقيات البحث"], ["Relevance", "الصلة"], ["Objectivity", "الموضوعية"]], "a"),
 M("“Methods and results should be open to checking” describes:", "«يجب أن تكون الطرق والنتائج قابلة للتدقيق» يصف:", [["Accuracy", "الدقة"], ["Evidence-based", "القائم على الدليل"], ["Clarity", "الوضوح"], ["Verifiability", "قابلية التحقق"]], "d"),
 M("“Conclusions should be supported by data” describes the principle of being:", "«يجب أن تكون الاستنتاجات مدعومة بالبيانات» يصف مبدأ:", [["Feasible", "قابلية التنفيذ"], ["Evidence-based", "القائم على الدليل"], ["Ethical", "الأخلاقية"], ["Relevant", "الصلة"]], "b"),
 M("Which research approach is correct?", "أيّ نهج بحثي صحيح؟", [["“I want to prove that energy drinks cause heart palpitations.”", "«أريد أن أثبت أن مشروبات الطاقة تسبب خفقان القلب.»"], ["“Is there an association between energy drink consumption and heart palpitations among university students?”", "«هل يوجد ارتباط بين تناول مشروبات الطاقة وخفقان القلب بين طلبة الجامعة؟»"], ["“Energy drinks are harmful, so the data must show it.”", "«مشروبات الطاقة ضارة، لذا يجب أن تُظهر البيانات ذلك.»"], ["“I will choose the result first.”", "«سأختار النتيجة أولًا.»"]], "b"),
 M("According to the lecture: the researcher ___, the data ___.", "وفق المحاضرة: الباحث ___، والبيانات ___.", [["answers / ask", "يجيب / تسأل"], ["chooses / confirm", "يختار / تؤكّد"], ["asks / answer", "يسأل / تجيب"], ["proves / follow", "يثبت / تتبع"]], "c"),
 M("In the UTI example, after the research question comes:", "في مثال التهاب المسالك البولية، بعد سؤال البحث تأتي:", [["Observation", "الملاحظة"], ["Data collection (urine samples)", "جمع البيانات (عيّنات الإدرار)"], ["Conclusion", "الاستنتاج"], ["Publication", "النشر"]], "b"),
 M("“Feasible” research means:", "البحث «القابل للتنفيذ» يعني:", [["It can actually be done with the available time, participants, equipment, and resources", "يمكن إجراؤه فعلًا بالوقت والمشاركين والأجهزة والموارد المتاحة"], ["It is very expensive", "أنه مكلف جدًا"], ["It has no ethical approval", "أنه بلا موافقة أخلاقية"], ["It uses only AI", "أنه يستعمل الذكاء الاصطناعي فقط"]], "a"),
 M("Which is NOT listed as a characteristic of good research?", "أيٌّ مما يأتي ليس من خصائص البحث الجيد المذكورة؟", [["Clear", "واضح"], ["Ethical", "أخلاقي"], ["Feasible", "قابل للتنفيذ"], ["Biased", "متحيّز"]], "d"),
 M("“Can PCR detect a pathogen in clinical samples?” is a research question from:", "«هل يستطيع PCR الكشف عن مُمرِض في العيّنات السريرية؟» سؤال بحثي من مجال:", [["Hematology", "أمراض الدم"], ["Immunology", "المناعة"], ["Molecular Biology", "البيولوجيا الجزيئية"], ["Microbiology", "الأحياء المجهرية"]], "c"),
 M("“Are inflammatory markers elevated in a certain disease?” belongs to:", "«هل ترتفع مؤشرات الالتهاب في مرض معيّن؟» ينتمي إلى:", [["Immunology", "المناعة"], ["Hematology", "أمراض الدم"], ["Molecular Biology", "البيولوجيا الجزيئية"], ["Microbiology", "الأحياء المجهرية"]], "a"),
 M("AI can assist researchers with all of the following EXCEPT:", "يمكن للذكاء الاصطناعي مساعدة الباحثين في كل ما يأتي ما عدا:", [["Brainstorming research ideas", "العصف الذهني لأفكار البحث"], ["Suggesting keywords", "اقتراح الكلمات المفتاحية"], ["Inventing research results", "اختلاق نتائج البحث"], ["Explaining difficult concepts", "شرح المفاهيم الصعبة"]], "c"),
 M("“Write a research about anemia.” is a poor prompt because it is:", "«اكتب بحثًا عن فقر الدم.» طلب ضعيف لأنه:", [["Too specific", "محدّد جدًا"], ["Too broad, with no population, question or purpose", "واسع جدًا، بلا مجتمع دراسة ولا سؤال ولا هدف"], ["Measurable", "قابل للقياس"], ["About university students", "عن طلبة الجامعة"]], "b"),
 M("A better AI prompt should:", "الطلب الأفضل للذكاء الاصطناعي يجب أن:", [["Ask AI to write the whole research", "يطلب منه كتابة البحث كله"], ["Assume the results", "يفترض النتائج"], ["Include patient names", "يتضمن أسماء المرضى"], ["Ask for measurable research questions and not assume the results", "يطلب أسئلة بحثية قابلة للقياس ولا يفترض النتائج"]], "d"),
 M("Which of the following should we NEVER do with AI?", "أيٌّ مما يأتي لا يجب أن نفعله أبدًا مع الذكاء الاصطناعي؟", [["Check its references", "التحقق من مراجعه"], ["Review its text before use", "مراجعة نصّه قبل استعماله"], ["Enter confidential patient information into unapproved AI tools", "إدخال معلومات المرضى السرّية في أدوات غير معتمدة"], ["Use it to organize information", "استعماله لتنظيم المعلومات"]], "c"),
 M("When using AI, we should always:", "عند استعمال الذكاء الاصطناعي يجب دائمًا:", [["Think → Check → Verify", "التفكير ← التحقق ← التأكد"], ["Copy → Paste → Submit", "النسخ ← اللصق ← التسليم"], ["Trust → Accept → Publish", "الثقة ← القبول ← النشر"], ["Ask → Copy → Share", "السؤال ← النسخ ← المشاركة"]], "a"),
 M("In “The Big Picture”, what comes directly after Research Question?", "في «الصورة الكاملة»، ماذا يأتي مباشرة بعد سؤال البحث؟", [["Data Analysis", "تحليل البيانات"], ["Research Plan", "خطة البحث"], ["Observation", "الملاحظة"], ["Results", "النتائج"]], "b"),
 M("Research starts with:", "يبدأ البحث بـ:", [["A result", "نتيجة"], ["An opinion", "رأي"], ["A conclusion", "استنتاج"], ["A question", "سؤال"]], "d"),
]
tf = [
 {"en": "An observation alone is enough to conclude a scientific fact.", "ar": "الملاحظة وحدها كافية لاستنتاج حقيقة علمية.", "answer": "F"},
 {"en": "Research is a systematic investigation.", "ar": "البحث استقصاء منهجي.", "answer": "T"},
 {"en": "Opinion equals evidence.", "ar": "الرأي يساوي الدليل.", "answer": "F"},
 {"en": "Observation can start research.", "ar": "يمكن للملاحظة أن تبدأ بحثًا.", "answer": "T"},
 {"en": "A researcher should decide the result before collecting data.", "ar": "يجب أن يحدّد الباحث النتيجة قبل جمع البيانات.", "answer": "F"},
 {"en": "Data should be collected and measured accurately.", "ar": "يجب جمع البيانات وقياسها بدقة.", "answer": "T"},
 {"en": "Research ethics is one of the basic principles of research.", "ar": "أخلاقيات البحث من المبادئ الأساسية للبحث.", "answer": "T"},
 {"en": "A feasible study is one that cannot be done with the available resources.", "ar": "الدراسة القابلة للتنفيذ هي التي لا يمكن إجراؤها بالموارد المتاحة.", "answer": "F"},
 {"en": "Research questions can come from daily laboratory practice.", "ar": "يمكن أن تأتي أسئلة البحث من الممارسة المختبرية اليومية.", "answer": "T"},
 {"en": "AI never makes mistakes in references.", "ar": "الذكاء الاصطناعي لا يخطئ أبدًا في المراجع.", "answer": "F"},
 {"en": "We may allow AI to modify research results if they look better.", "ar": "يمكننا السماح للذكاء الاصطناعي بتعديل نتائج البحث إذا بدت أفضل.", "answer": "F"},
 {"en": "AI-generated text should be reviewed and understood before use.", "ar": "يجب مراجعة النص الذي يولّده الذكاء الاصطناعي وفهمه قبل استعماله.", "answer": "T"},
 {"en": "In the big picture, data analysis comes before data collection.", "ar": "في الصورة الكاملة، يأتي تحليل البيانات قبل جمعها.", "answer": "F"},
]
traps = [
 {"en": "“I noticed that many people have low vitamin D” is scientific evidence. Correct?", "ar": "«لاحظتُ أن كثيرًا من الناس لديهم انخفاض في فيتامين D» دليل علمي. هل هذا صحيح؟", "answer_en": "No. It is an **observation**. Evidence is measured data: “Among 300 tested participants, 42% had vitamin D deficiency.”", "answer_ar": "لا. إنها **ملاحظة**. الدليل هو بيانات مقيسة: «من بين 300 مشارك جرى فحصهم، كان لدى 42% نقص في فيتامين D.»"},
 {"en": "“I want to prove that energy drinks cause heart palpitations” is a good research approach. Correct?", "ar": "«أريد أن أثبت أن مشروبات الطاقة تسبب خفقان القلب» نهج بحثي جيد. هل هذا صحيح؟", "answer_en": "No. The researcher does not choose the result; ask a neutral question about an **association**.", "answer_ar": "لا. الباحث لا يختار النتيجة؛ بل يطرح سؤالًا محايدًا عن **الارتباط**."},
 {"en": "Objectivity means data are measured accurately. Correct?", "ar": "الموضوعية تعني قياس البيانات بدقة. هل هذا صحيح؟", "answer_en": "No. Objectivity = based on facts, not personal opinions; **accuracy** = data collected and measured accurately.", "answer_ar": "لا. الموضوعية = البناء على الحقائق لا الآراء الشخصية؛ أما **الدقة** فهي جمع البيانات وقياسها بدقة."},
 {"en": "Feasible means the research is important to society. Correct?", "ar": "قابلية التنفيذ تعني أن البحث مهم للمجتمع. هل هذا صحيح؟", "answer_en": "No. Feasible = can actually be done with the available time, participants, equipment and resources; importance is **relevance**.", "answer_ar": "لا. قابلية التنفيذ = إمكان إجرائه فعلًا بالوقت والمشاركين والأجهزة والموارد المتاحة؛ أما الأهمية فهي **الصلة**."},
 {"en": "AI-generated references can be used directly because AI is accurate. Correct?", "ar": "يمكن استعمال المراجع التي يولّدها الذكاء الاصطناعي مباشرة لأنه دقيق. هل هذا صحيح؟", "answer_en": "No. AI may generate false information or references — never trust them without checking.", "answer_ar": "لا. قد يولّد الذكاء الاصطناعي معلومات أو مراجع زائفة — لا تثق بها أبدًا من دون تحقق."},
 {"en": "Research starts with data collection. Correct?", "ar": "يبدأ البحث بجمع البيانات. هل هذا صحيح؟", "answer_en": "No. Research starts with a question: Observation → Research Problem → Research Question → Research Plan → Data Collection → Data Analysis → Results.", "answer_ar": "لا. يبدأ البحث بسؤال: الملاحظة ← مشكلة البحث ← سؤال البحث ← خطة البحث ← جمع البيانات ← تحليل البيانات ← النتائج."},
]
important = [
 {"en": "Define research and scientific research.", "ar": "عرّف البحث والبحث العلمي.", "answer_en": "Research: a systematic investigation used to answer a question, solve a problem or discover new information. Scientific research: an organized process that uses scientific methods and evidence to answer questions and solve problems.", "answer_ar": "البحث: استقصاء منهجي للإجابة عن سؤال أو حلّ مشكلة أو اكتشاف معلومات جديدة. البحث العلمي: عملية منظّمة تستعمل الطرق العلمية والأدلة للإجابة عن الأسئلة وحلّ المشكلات."},
 {"en": "Why do we conduct research?", "ar": "لماذا نجري البحث؟", "answer_en": "To describe a health problem, explore new information, compare groups or methods, identify associations between factors, evaluate tests or treatments, and improve healthcare practice.", "answer_ar": "لوصف مشكلة صحية، واستكشاف معلومات جديدة، ومقارنة مجموعات أو طرق، وتحديد الارتباطات بين العوامل، وتقييم الفحوص أو العلاجات، وتحسين ممارسة الرعاية الصحية."},
 {"en": "Differentiate between observation, opinion and evidence, with an example of each.", "ar": "فرّق بين الملاحظة والرأي والدليل، مع مثال لكل منها.", "answer_en": "Opinion: “I think vitamin D deficiency is common among young adults.” Observation: “I noticed that many people have low vitamin D.” Evidence: “Among 300 tested participants, 42% had vitamin D deficiency.”", "answer_ar": "الرأي: «أعتقد أن نقص فيتامين D شائع بين الشباب.» الملاحظة: «لاحظتُ أن كثيرًا من الناس لديهم انخفاض في فيتامين D.» الدليل: «من بين 300 مشارك جرى فحصهم، كان لدى 42% نقص في فيتامين D.»"},
 {"en": "List the basic principles of research.", "ar": "عدّد المبادئ الأساسية للبحث.", "answer_en": "Objectivity, systematic approach, accuracy, evidence-based, verifiability, research ethics.", "answer_ar": "الموضوعية، النهج المنهجي، الدقة، القائم على الدليل، قابلية التحقق، أخلاقيات البحث."},
 {"en": "List the characteristics of good research and explain “feasible”.", "ar": "عدّد خصائص البحث الجيد واشرح «قابلية التنفيذ».", "answer_en": "Clear, systematic, objective, accurate, feasible, ethical, relevant. Feasible: the study can actually be done with the available time, participants, equipment and resources.", "answer_ar": "واضح، منهجي، موضوعي، دقيق، قابل للتنفيذ، أخلاقي، ذو صلة. قابل للتنفيذ: يمكن إجراء الدراسة فعلًا بالوقت والمشاركين والأجهزة والموارد المتاحة."},
 {"en": "How can AI help researchers, and what should we never do with it?", "ar": "كيف يساعد الذكاء الاصطناعي الباحثين، وما الذي لا يجب فعله معه أبدًا؟", "answer_en": "Help: brainstorming ideas, developing questions, suggesting keywords, organizing information, improving language, explaining concepts. Never: trust unchecked references, let it invent or modify results, enter confidential patient data into unapproved tools, copy its text without review. Always: Think → Check → Verify.", "answer_ar": "يساعد في: العصف الذهني، وتطوير الأسئلة، واقتراح الكلمات المفتاحية، وتنظيم المعلومات، وتحسين اللغة، وشرح المفاهيم. لا تفعل أبدًا: الوثوق بمراجع غير متحقَّق منها، أو السماح له باختلاق النتائج أو تعديلها، أو إدخال بيانات المرضى السرّية في أدوات غير معتمدة، أو نسخ نصّه من دون مراجعة. دائمًا: فكّر ← تحقّق ← تأكّد."},
]

data = {"meta": {
  "subject_en": "Principles of Research", "subject_ar": "مبادئ البحث العلمي", "short_ar": "مبادئ البحث",
  "unit_en": "Lecture 1", "unit_ar": "المحاضرة 1", "unit_label": "LEC", "unit_no": "1",
  "title_en": "Research Starts With a Question", "title_ar": "البحث يبدأ بسؤال",
  "kind": "Theory — نظري", "stage": "The fourth stage — الرابعة", "instructor": "ليندا منجد هادي"},
 "blocks": blocks, "questions": {"mcq": mcq, "tf": tf, "traps": traps, "important": important}}
from collections import Counter
print(len(mcq), Counter(q["answer"] for q in mcq))
os.makedirs("/home/user/-/research-lec1-principles", exist_ok=True)
json.dump(data, open("/home/user/-/research-lec1-principles/lecture.json", "w"), ensure_ascii=False, indent=1)
