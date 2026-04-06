# AI Evaluation (Evals) - All Guest Insights

*2 guests, 2 mentions*

---

## Hamel Husain & Shreya Shankar
*Hamel Husain & Shreya Shankar*

> "Both the chief product officers of Anthropic and OpenAI shared that evals are becoming the most important new skill for product builders."

**Insight:** The guests explicitly define this as a 'new skill' that is distinct from traditional software testing or general AI strategy. It involves a specific multi-step workflow (Error Analysis, Open Coding, Axial Coding, Creating Rubrics, and Scoring) that must be mastered. This is a 'core product skill' that involves manual trace analysis, writing down what's wrong, clustering failure patterns, and creating rubrics to systematically measure AI output quality.

**Tactical advice:**
- Master the full eval workflow: error analysis → open coding → axial coding → rubrics → scoring
- Do not skip manual trace analysis — you cannot write good evals without first understanding failure patterns
- Treat evals as a core PM skill, not a ML engineering task

---

## Brendan Foody
*Brendan Foody*

> "If the model is the product, then the eval is the product requirement document."

**Insight:** The guest explicitly states we are entering the 'era of evals' and describes it as a core bottleneck for AI labs. It involves creating rubrics, benchmarks, and systematic tests to measure model capabilities — not just for researchers, but as a fundamental product management activity. Evals define what success looks like in AI products.

**Tactical advice:**
- Write evals before writing prompts — they are your specification
- Use Pass/Fail rubrics, not Likert scales (1-5 scales produce meaningless averages)
- If using LLM-as-judge, validate the judge against human expert ratings first
- Run evals continuously, not just at launch
