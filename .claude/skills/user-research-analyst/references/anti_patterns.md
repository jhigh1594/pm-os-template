# Anti-Patterns: What 10X Researchers Actively Avoid

These are the specific behaviors and habits that separate mediocre research from research that drives decisions. Each is paired with the failure it causes and what to do instead.

---

## Asking about the product instead of the customer's life

**What it looks like:** "What do you think of this feature?" "Would you use X?" "How important is Y to you?"

**Why it fails:** Produces compliments, hypothetical fluff, and wishlists (Fitzpatrick). None of these map to actual behavior. None predict whether someone will buy, adopt, or stay.

**What to do instead:** Ask about the last time they dealt with the problem. Ask what they did. Ask what they use now. Ask about the day they decided to look for something different.

---

## Recruiting only warm intros and happy-path users

**What it looks like:** Interviewing your most engaged customers, your champions, your warm referrals.

**Why it fails:** Selection bias toward people who already believe in you. It confirms what you already know and hides the reasons people don't adopt or churn.

**What to do instead:** Recruit churned users, non-adopters, and power users of your competitors. These are the people who understand your failure modes. After 3–4 interviews confirming a pattern, specifically recruit someone who doesn't fit it.

---

## Clustering themes by topic instead of underlying need

**What it looks like:** Affinity map organized around "onboarding," "pricing," "performance," "support."

**Why it fails:** Topics are categories, not insights. "Onboarding" contains at least five completely different user needs. Topic clusters summarize data; they don't produce design implications.

**What to do instead:** Cluster by underlying need or behavior pattern: "Users need to feel progress in the first week," "Enterprise buyers need IT sign-off before committing." Ask "what is the user trying to do?" and "what's getting in the way?" — not "what subject is this about?"

---

## Analysis theater: findings without an interpretive position

**What it looks like:** A summary of what was said across participants, presented neutrally without a recommendation.

**Why it fails:** Stakeholders can't act on neutral summaries. They can act on positions. A 40-page research report with no recommendation is the world's most expensive delay tactic.

**What to do instead:** Take a position. State what the data means and what you recommend. If no one could reasonably disagree with your output, you haven't done the synthesis work. At least one statement in every brief should be worth debating.

---

## Confusing stated preference with past behavior

**What it looks like:** "Eight of ten participants said they would want a screen." "Users said real-time data was very important."

**Why it fails:** What people say they want and what they do are systematically different. Stated preference is cheap to give and unreliable to act on. Past behavior is the only reliable predictor of future behavior.

**What to do instead:** Ask about what they've *done*, not what they *would* do. "Have you ever paid for a service to solve this problem?" "What did you actually do the last time this happened?" Preference questions are hypothetical; behavior questions are empirical.

---

## Letting LLMs flatten contradictions into false consensus

**What it looks like:** AI produces clean, coherent themes that neatly summarize the data. Every theme is presented with equal confidence.

**Why it fails:** LLMs are trained to produce coherent, helpful outputs — not to flag their own uncertainty or surface contradictions. A dataset with three people who loved a feature and four people who hated it will often produce a "mixed reception" theme that buries the signal.

**What to do instead:** Explicitly instruct the model to look for contradictions (see `analysis_workflow.md` Verification Pass). Segment by participant type before synthesizing. Look at the distribution, not just the theme.

---

## Rushing to solutions before mapping the opportunity space

**What it looks like:** Interview sessions that end with "so, what feature would help you?" Product backlog items that appear before 6+ customers have been interviewed.

**Why it fails:** Feature-first thinking produces features for the solutions customers describe, not the underlying jobs they're trying to do. Customers are experts in their problems; they are not product designers.

**What to do instead:** Map the opportunity (the underlying need, pain, or desired outcome) before generating solutions. A customer who says "I want a screen" is describing a solution. The opportunity is "I need activity-awareness during workouts." Multiple solutions address that opportunity — screen is one of them.

---

## Outsourcing analysis to one person

**What it looks like:** The PM watches the interview recordings alone and writes up findings. Or the researcher does all synthesis and presents conclusions.

**Why it fails:** Different people hear different things in the same interview. A PM hears business implications; a designer hears interaction patterns; an engineer hears feasibility constraints. Mono-perspective analysis has systematic blind spots.

**What to do instead:** Product trio (PM + designer + engineer) observes interviews together. Everyone writes down observations independently before the debrief. The first person to speak in a debrief anchors the group — avoid this by collecting written observations first. Synthesis is a team activity.

---

## Treating AI output as final on first pass

**What it looks like:** Running transcript analysis, getting clean themes, putting them directly into the deck.

**Why it fails:** The first AI pass is always a hypothesis. It contains fabricated quotes, generic themes, and undetected contradictions. Without a verification step, you have no way to know what's wrong until a stakeholder asks a question you can't answer.

**What to do instead:** Treat the first pass as a draft. Run the Quote Verification prompt. Run the Verification Pass. A few extra minutes of verification is the difference between AI output you'll always second-guess and insights you can stand behind.

---

## Reporting on past research as if it answers the current question

**What it looks like:** "We did research on this topic 18 months ago — here's what we found." The decision is made based on that research without checking whether the context has changed.

**Why it fails:** User research has a shelf life. Market conditions change, competitive dynamics shift, the product evolves. Research from before a major product change or competitive entry is not reliable evidence for a current decision.

**What to do instead:** Check whether the research question and participant profile still match the current decision. If the decision has changed, or if significant time has passed, plan new touchpoints rather than recycling old findings.

---

## Presenting insights without disconfirming evidence

**What it looks like:** A brief with three supporting insights and no counterevidence.

**Why it fails:** If the synthesis only shows support, either you didn't look hard enough for contrary evidence, or you found it and buried it. Either way, a stakeholder will find it — and your credibility suffers more for not having surfaced it yourself.

**What to do instead:** Every decision brief must include at least one disconfirming finding. "Here's what we found, and here's what cuts against it, and here's how we weighed it" is the most defensible research position. It signals rigor, not weakness.
