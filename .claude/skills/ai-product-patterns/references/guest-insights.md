# AI-Native Product Building - All Guest Insights

*1 guest, 4 mentions*

---

## Kevin Weil
*Kevin Weil (CPO, OpenAI)*

> "The AI model you're using today is the worst AI model you will ever use for the rest of your life. What computers can do changes every two months."

**Insight:** AI capabilities are on an exponential curve, not a linear one. Product decisions made today that treat current model limitations as permanent constraints will be wrong within months. The correct planning horizon is "what does this look like when the model is 10x better?"

**Tactical advice:**
- Don't design UI or product flows that assume current failure modes are permanent
- Build interfaces that scale with model improvements — avoid hardcoded fallbacks that limit the model
- Ship at the edge of current capability; in two months that edge becomes the baseline

---

> "At OpenAI, evals are the product spec. If you can define what good looks like in test cases, you've defined the product."

**Insight:** For AI products, traditional PRD-style requirements are insufficient — they describe intent but not measurability. An eval (test case with input, expected output, and quality bar) is more precise than a written requirement and forces PMs to define success concretely before building.

**Tactical advice:**
- Write evals before prompts — the eval is the specification
- Define success cases AND failure cases as runnable tests
- Track eval scores across model versions to detect regressions automatically

---

> "Don't make everything AI. Use AI where it shines, traditional code where it's reliable."

**Insight:** Hybrid architectures consistently outperform pure-AI approaches for production products. AI excels at pattern matching, intent understanding, and generation. Deterministic code excels at math, validation, access control, and critical execution paths. The design decision is where the boundary sits.

**Tactical advice:**
- Use AI for intent understanding, code for deterministic execution
- Apply rule-based preprocessing before AI calls to reduce cost and latency
- Build confidence scoring into AI decisions; route low-confidence cases to fallbacks or humans

---

> "If you're building and the product is right on the edge of what's possible, keep going. In two months, there's going to be a better model."

**Insight:** The primary reason to avoid building at the capability frontier — "the AI isn't good enough yet" — is self-defeating. The correct response to an AI capability gap is to design for the capability you want and ship as the models improve, rather than shipping a degraded version designed around current limits.

**Tactical advice:**
- When the AI falls short, ask: "would a better model fix this?" If yes, build the full experience
- Avoid UX that teaches users the current model's limitations — it will confuse them when the model improves
- Use progressive enhancement: start with what works today, unlock more as capabilities improve
