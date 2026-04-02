---
name: reduce
description: |
  Removal audit for any product artifact — PRD, feature spec, user flow, copy,
  onboarding, or settings. Applies 7 reduction lenses (Rubin, Rams, Jobs, Ive,
  Strunk/White, McKeown, Graham) to answer one question: what would you remove?
  TRIGGERS: "what should we cut", "what would you remove", "reduce this", "simplify
  this PRD", "what's unnecessary here", "essentialism review", "ruthless edit",
  "what's bloat", "removal audit", "what's the minimum", "cut this down"
---

# Reduce

> "Perfection is achieved not when there is nothing more to add, but when there is nothing left to take away." — Antoine de Saint-Exupéry

This skill answers one question: **what would you remove?**

It does not suggest improvements. It does not add features. It does not propose alternatives. It removes. It produces a Removal Audit — a table of concrete, actionable cuts applied through 7 distinct intellectual lenses, each asking the same question from a different vantage point.

Use this when a PRD is getting fat, an onboarding flow has too many steps, a settings screen has become a dumping ground, or copy has stopped earning its place on screen.

---

## How to Invoke

Paste the artifact directly — a PRD section, feature list, user flow description, settings spec, onboarding copy, button labels, or any product surface. Provide context if useful (who the user is, what stage the product is at). The skill will apply all 7 lenses and produce the full Removal Audit.

**Artifacts this skill processes:**
- PRD sections (feature lists, scope definitions, requirements)
- User flows (onboarding steps, setup wizards, checkout flows)
- Settings and configuration panels
- Product copy (labels, tooltips, empty states, error messages, modal text)
- Feature specs and capability lists
- API surface area and integration lists

---

## The 7 Lenses

### 1. Rick Rubin — Serve the Work, Not the Maker

*The work has its own essence. Everything that serves the maker's ego rather than the user's need is noise.*

Rubin's question: *"Is this here because the product needs it, or because someone wanted to build it?"*

Rubin scans for features, flows, and copy that exist because of internal excitement rather than user demand. The tell: "we've always wanted to do this" language in PRD rationale sections. Features no user asked for but that the team is proud of. Clever interactions that showcase engineering craft but add cognitive load.

**Example finding:** "The animated onboarding checklist with confetti on completion — remove it. The animation is for you, not for the user. The user just wants to know what to do next."

---

### 2. Dieter Rams — Less, But Better

*Good design is as little design as possible. Everything that is not necessary weakens everything that is.*

Rams' question: *"Would removing this make the remaining product stronger?"*

Rams applies his 10th principle as a filter. He scans for: settings panels that serve edge cases, UI chrome that decorates rather than communicates, configuration choices that exist because the team couldn't commit to a good default. He is particularly intolerant of optionality as a substitute for design decisions.

**Example finding:** "'Display density: Compact / Normal / Comfortable' — remove it. It exists because no one decided what the right density is. Decide. Ship one. The options are a design failure presented as a feature."

---

### 3. Steve Jobs — Focus Is Saying No

*Saying yes to one thing means saying no to a thousand others. Most of what's in this artifact is one of those thousand.*

Jobs' question: *"If we could only ship one thing from this entire list, what would it be? What does that imply about everything else?"*

Jobs scans for scope that accumulated without someone saying no. He is not looking for bad features — he is looking for good features that aren't *the* thing. Every feature shipped must be maintained, documented, supported, and explained to new users forever. Jobs demanded everything justify that cost.

**Example finding:** "You have three onboarding paths: 'Quick Setup', 'Guided Setup', and 'Enterprise Setup'. Remove 'Guided Setup'. It's the hedge — the option you created so you didn't have to choose between fast and thorough. Choose."

---

### 4. Jony Ive — Simplicity Is Mastered Complexity

*Simplicity is not the absence of complexity. It is the result of mastering it upstream so it never reaches the user.*

Ive's question: *"Where is complexity being displayed instead of resolved?"*

Ive scans for unresolved design decisions that surfaced as user-facing options: "Advanced" tabs that exist because the core algorithm has too many knobs, power-user modes that were easier to build than remove, settings that wouldn't exist if the defaults were smarter. If a user has to make a choice, it means designers decided not to make a decision.

**Example finding:** "The 'Advanced' tab with 14 settings — remove it. These settings exist because the underlying system wasn't designed well enough to work without tuning. The solution is not a tab. The solution is resolving the design so the tab becomes unnecessary."

---

### 5. Strunk & White — Omit Needless Words

*Every word on screen that doesn't carry weight dilutes every word around it.*

Strunk & White's question: *"What would happen if we removed this word, sentence, label, or message entirely?"*

They scan every text surface with a red pen: modal titles that restate what the modal obviously does, button labels padded with politeness, tooltips that explain what the button already says, empty states with two paragraphs of encouragement when one line would do, error messages that apologize before they explain, onboarding copy left over from the landing page.

**Example finding:** "Remove the welcome modal. 'Welcome to [Product]! We're so excited you're here. Let's get you set up so you can experience all the powerful features...' is 22 words of self-congratulation. Replace with: 'Let's set up your workspace.' Or remove it entirely."

---

### 6. Greg McKeown — The Disciplined Pursuit of Less

*The difference between the vital few and the trivial many is not obvious — the trivial many feel just as important in the moment.*

McKeown's question: *"Of everything here, what is the single highest-contribution item? What does that make everything else?"*

McKeown applies the Essentialist diagnostic to scope, integration lists, and feature sets. He scans for: features added because one loud stakeholder asked, integrations built for 2% of users, options that exist to satisfy theoretical edge cases, work that feels productive but isn't the most important thing. His cut is strategic, not aesthetic — he is asking about opportunity cost.

**Example finding:** "The Slack, Jira, Salesforce, Zapier, and CSV integrations all appear in the same priority tier. They cannot all be equal. Remove four from this release. One integration done exceptionally is more valuable than five done adequately."

---

### 7. Paul Graham — Ruthless Prioritization from First Principles

*Do the smallest version that proves the assumption. Everything beyond that is premature.*

Graham's question: *"What is the minimum version of this that would still delight the right user? What is everything else?"*

Graham scans for infrastructure built before it was needed, configurability added before users asked for it, features polished before they were validated. He asks: what assumption are you trying to prove? Have you proved it yet? If not, you don't need anything beyond the minimum that proves it.

**Example finding:** "You built a full notification preference panel with 12 toggles before shipping the first notification. Remove 11 of them. Send the one notification that matters. Add toggles only when users complain about getting too many. Right now you have zero users complaining."

---

## Output Format

### Removal Audit

| Remove | Why | Lens | Confidence | Pain Level |
|--------|-----|------|------------|------------|
| [Specific thing — feature, step, word, setting, screen] | [1-sentence rationale] | [Rubin / Rams / Jobs / Ive / S&W / McKeown / Graham] | High / Med / Low | Low / Med / High |

*Confidence* = how certain this removal improves the product.
*Pain Level* = how much team resistance to expect (Low = easy win, High = will require a fight).

---

### What Remains

After all cuts, state the irreducible essence in 1-3 sentences. This is the hardest section to write and the most valuable. If you cannot articulate what remains, you do not yet have a clear enough mental model of what the product is for.

---

### The Hardest Cut

> Name one specific thing — a feature, a step, a word, an integration, a screen — that the team would push back hardest on removing, but that would make everything sharper if they did.

This cannot be a category or a vague recommendation. Name the thing. In one sentence, explain why removing it would hurt. In one sentence, explain why removing it would be right.

**Auto-saving to** `📚 Knowledge/Growth/growth-signals-[YYYY-MM].md` — append a brief entry noting the artifact reviewed and the top 3 removals. No prompt needed.

---

## Hard Constraints

- **NEVER suggest adding features, steps, words, or options** — if an improvement requires addition, note it briefly and defer to `/critique` or `/spec`
- **NEVER soften a removal recommendation** — state it as a removal: "Remove X", not "You might consider removing X"
- **NEVER produce a "What Remains" longer than 3 sentences** — if you need more, you haven't finished reducing
- **NEVER give a vague Hardest Cut** — "simplify the onboarding" is not a Hardest Cut; "Remove the role-selection screen entirely" is
- **NEVER skip The Hardest Cut** even if everything in the artifact seems defensible — there is always a hardest cut

---

## Related Skills

- `/critique` — For adding, improving, and evaluating what's working; the counterpart to this skill
- `/product-taste-intuition` — For building the removal instinct over time; understanding *why* less is better
- `/spec` — For rewriting the artifact after cuts are applied; turning the Removal Audit into revised requirements
