# Interview Design: JTBD and Mom Test Principles

## The Fundamental Error in Most Interviews

Average interviewers ask about the product:
- "What do you think of feature X?"
- "Would you use Y if we built it?"
- "How satisfied are you with Z?"

These questions produce three types of bad data (Rob Fitzpatrick, *The Mom Test*):
1. **Compliments** — "It's great, I love it"
2. **Hypothetical fluff** — "I would definitely use that"
3. **Wishlists** — "You should add X, Y, Z"

None of these map to actual behavior. None of them tell you whether something is worth building.

**Elite interviewers ask about the customer's life, not your product.**

---

## The Mom Test

The Mom Test: if your most defensive, protective mother could give you a dishonest answer to your question without lying, rewrite the question.

**Questions that fail the Mom Test:**
- "Do you think this is a good idea?"
- "Would you pay for something like this?"
- "Can you see yourself using this regularly?"
- "How often would you use [feature]?"

**Questions that pass:**
- "Tell me about the last time you dealt with [problem]."
- "What did you do when that happened?"
- "What are you using now to solve this?"
- "How much does your current solution cost you — time and money?"
- "Walk me through the day you decided to start looking for something different."

**The test:** Could the answer validate your idea without being true? If yes, rewrite the question.

---

## JTBD Switch Interview Structure

The Switch Interview (Bob Moesta and Chris Spiek) focuses entirely on the moment of purchase or adoption — reconstructing the customer's timeline of events, thoughts, and emotions that led to the switch.

The interviewer is not asking about the product. They are reconstructing the customer's causal story.

### Timeline Reconstruction Questions

Work through these chronologically — the goal is a narrative, not a checklist:

**First thought:**
- "Tell me about the first time you thought about solving this problem."
- "What was happening in your life or work that made you start thinking about this?"
- "How long had the problem been bothering you before you did anything about it?"

**Passive looking:**
- "What did you do first when you started looking into options?"
- "Who did you talk to? What did you read?"
- "What alternatives did you consider?"

**Active looking:**
- "What triggered you to get serious about finding a solution?"
- "Was there a specific event or day that pushed you from 'I should fix this' to 'I'm fixing this today'?"

**Decision day:**
- "Walk me through the day you actually made the switch."
- "What almost stopped you?"
- "What were you worried about?"

**Consumption:**
- "What happened the first time you used it?"
- "When did you know it was working? Or when did you know it wasn't?"

### The 4 Forces of Progress

Every switch (purchase, adoption, churn) is governed by four forces. Map where each customer sits on each:

| Force | Direction | Probe |
|---|---|---|
| **Push** (frustration) | Enables switch | "What was so frustrating that you finally had to do something?" |
| **Pull** (attraction) | Enables switch | "What did the new solution make possible that the old one didn't?" |
| **Anxiety** (concern) | Blocks switch | "What worried you about making the change?" "What almost stopped you?" |
| **Inertia/Habit** | Blocks switch | "What was hard to leave behind?" "What did you have to give up?" |

A switch only happens when Push + Pull outweigh Anxiety + Habit.

**The insight:** Most customers who didn't convert had high Anxiety or Inertia — not weak Pull. If you're trying to drive adoption, you're often fighting habits and fears more than you're lacking features.

**For churn interviews:** Run the forces in reverse. What pushed them out? What pulled them elsewhere? What anxiety or inertia almost kept them?

---

## Probing Techniques (Steve Portigal)

### Silence as a probe
After the participant finishes speaking, wait 5–10 seconds before responding. Novice interviewers fill silence. Elite interviewers sit in it.

Participants fill silence with the thing they almost didn't say — often the most revealing content in the interview.

### Concrete instance probe
"Can you walk me through the last specific time that happened?"

Moves from generalization to specific event. Real data lives in specific events, not general patterns. "It's usually pretty frustrating" tells you nothing. "Last Tuesday at 4pm, I was trying to get the report out before the board call and the system timed out for the third time" tells you everything.

### Exception probe
"Was there ever a time when it worked differently?"
"Can you think of an instance where you handled it differently than usual?"

Exceptions reveal the boundaries of behavior patterns and frequently surface the hidden job. If someone always uses workaround X except on Fridays, Friday is where the real behavior lives.

### Comparison probe
"How is this different from the way you used to do it?"
"How does this compare to how [colleague / competitor / old tool] handles it?"

Comparison surfaces mental models. The gap between how things are and how they were (or how a competitor handles it) is often where the pain lives.

### Laddering (from Values Laddering)
For any attribute the user mentions, probe upward to find the consequence, then probe again to find the value:

- User: "It has to be fast."
- Probe: "Why does speed matter to you?"
- User: "Because I don't have to think about it."
- Probe: "What does that give you?"
- User: "I stay in flow — my work is better."
- Probe: "And why does that matter?"
- User: "That's how I justify my value to my team."

Most product teams live at the attribute level ("fast"). Elite researchers ladder to the value level ("justifies their professional standing"). The value level is where positioning lives.

---

## Reading Non-Obvious Signals

Non-obvious insights appear most often when:

1. **Participant hesitates** before answering — they're censoring something. Probe: "You paused — what were you thinking?"
2. **Words and tone diverge** — "It's fine, I guess..." with flat affect. Probe: "That sounded uncertain — what's the 'I guess' about?"
3. **Stated preference contradicts described behavior** — They say they want X but describe always doing Y. Flag this explicitly in your notes.
4. **They use language you've never heard internally** — This is commercially important. Write it down verbatim.

---

## Recruiting for Disconfirmation

Average researchers recruit happy, engaged users. This is selection bias. It produces insights that confirm your existing beliefs.

Elite researchers specifically recruit:
- **Churned users** — people who left understand the failure modes
- **Non-adopters** — people who evaluated and chose not to buy reveal anxiety and inertia
- **Power users of competitors** — people who chose someone else articulate what your product is missing or what their alternative does better
- **Outliers within your user base** — the 10% who use the product very differently from the majority often hold the hidden job

After 3–4 interviews that seem to confirm a pattern, recruit specifically for people who don't fit the pattern. Ask: who would this be wrong about? Go find them.

---

## Interview Guide Checklist

Before running any interview, verify:

- [ ] No hypothetical future questions ("would you use...")
- [ ] No product opinion questions ("what do you think of...")
- [ ] No leading questions that embed the answer ("don't you find it frustrating that...")
- [ ] At least 3 timeline reconstruction questions (first thought, active search, decision day)
- [ ] At least 1 "what almost stopped you" probe
- [ ] At least 1 exception probe
- [ ] Forces of Progress mapped in the guide (push, pull, anxiety, inertia)
- [ ] Silence is planned — guide has open sections, not back-to-back questions

**Session structure (45–60 min):**
1. Warm-up and rapport (5 min) — "Tell me a bit about your role and how you spend your time"
2. Timeline reconstruction (30 min) — walk through the switch story from first thought to today
3. Probing loops (10 min) — silence, concrete instances, exceptions, comparisons
4. Wrap (5 min) — "Is there anything important I didn't ask about?"

Do not pitch or explain your product during the interview. This contaminates the data.
