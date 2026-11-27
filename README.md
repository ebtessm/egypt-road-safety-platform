# منصة وطنية للسلامة على الطرق ونقل المواد الخطرة
# National Road Safety & Hazardous-Materials Transport Platform (Egypt)

> مشروع مفتوح المصدر، نقطة بداية للتطوير. ليس مشروعًا حكوميًا رسميًا، وهو مفتوح لكل من يريد المساهمة.
> An open-source starting point. Not an official government project. Anyone may contribute.

## المقدمة

رحم الله ضحايا حادث الوراق، وربط على قلوب أسرهم، وشفى المصابين 💔

لكن وسط الحزن، لازم نسأل نفسنا…
ماذا يمكن أن نفعل حتى لا تتكرر هذه المأساة؟

أنا مؤمنة إننا محتاجين ننتقل من رد الفعل إلى التفكير الاستباقي، ومن التعامل مع الحوادث بعد وقوعها إلى بناء منظومة تمنعها قدر الإمكان.

لدينا عقول وخبرات وتكنولوجيا وإمكانيات، ويمكننا توظيف الذكاء الاصطناعي، وقواعد البيانات، وأنظمة التتبع الذكي، وتحليل المخاطر، لبناء منظومة وطنية متكاملة للسلامة على الطرق ونقل المواد الخطرة.

مشروع يربط الجهات المعنية في منصة واحدة، ويتابع الناقلات لحظيًا، ويرصد المخاطر، ويساعد على التدخل السريع قبل تحول الخطأ إلى كارثة.

الأوطان لا تتقدم بالأفكار وحدها، ولكن بتحويل الأفكار إلى خطط، والخطط إلى تنفيذ، والتنفيذ إلى نتائج تحمي حياة الإنسان.

يارب قدرنا نكون جزءًا من التغيير اللي بنحلم نشوفه في مصر. 🇪🇬

## الفكرة في نقاط

1. **منصة واحدة** تربط الجهات المعنية (المرور، الإسعاف، الحماية المدنية، شركات النقل، المصانع والموانئ، الجهات الرقابية).
2. **تتبع لحظي** للناقلات (خصوصًا ناقلات المواد الخطرة) عبر أجهزة GPS.
3. **رصد المخاطر**: سرعة زائدة، خروج عن المسار، توقف غير معتاد، سائق مرهق، مركبة منتهية الفحص، طقس سيئ.
4. **تنبيه وتدخل سريع** قبل أن يتحول الخطأ إلى كارثة.
5. **تحليل بيانات وذكاء اصطناعي** لاكتشاف النقاط السوداء على الطرق والتنبؤ بالمخاطر.

## ما الموجود الآن في هذا المستودع

| المجلد | المحتوى |
|---|---|
| `docs/ARCHITECTURE.md` | تصور البنية العامة للمنظومة |
| `docs/DATA_MODEL.md` | نموذج البيانات المقترح |
| `docs/ROADMAP.md` | خطة المراحل والمهام المفتوحة |
| `docs/CONTRIBUTING.md` | كيف تشارك |
| `src/roadsafety/` | نموذج أولي بسيط بلغة Python: حساب درجة الخطر وتوليد التنبيهات |
| `tests/` | اختبارات للنموذج الأولي |
| `examples/` | بيانات تجريبية مصنوعة (وليست بيانات حقيقية) |

**مهم:** النموذج الأولي تجريبي لإثبات الفكرة فقط. الأوزان والحدود في الكود أمثلة، وتحتاج مراجعة خبراء السلامة والجهات المختصة قبل أي استخدام فعلي.

## تشغيل النموذج الأولي

```bash
python run_demo.py
python -m unittest discover tests
```

لا يحتاج أي مكتبات خارجية، فقط Python 3.9 أو أحدث.

## English summary

A single platform linking road-safety authorities, tracking hazardous-materials carriers in real time, scoring risk (speed, route deviation, abnormal stops, driver fatigue, vehicle inspection status, weather) and raising early alerts so that interventions happen before an error becomes a disaster. This repo holds the vision, architecture, data model, roadmap and a small dependency-free Python prototype of the risk engine. All sample data is synthetic.

## الترخيص / License

MIT. See `LICENSE`.

## Related project / مشروع مرتبط

[SCaaS: Software Components as a Service](https://github.com/ebtessm/scaas): a research idea for a national-cloud platform where reusable components (such as this project's risk scoring) could be shared. Idea stage only.

[SCaaS](https://github.com/ebtessm/scaas): فكرة بحثية لمنصة على سحابة وطنية تُشارَك فيها المكوّنات القابلة لإعادة الاستخدام (مثل تقييم المخاطر هنا). مرحلة فكرة فقط.
