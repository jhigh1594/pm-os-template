# Writing Guide: Customer Audience

**Who this is for:** External customers — end users, champions, economic buyers, admins — receiving product communications, release notes, announcements, or change notices.

---

## Opening Logic

**Lead with the pain being resolved OR the outcome the customer gains. Never the feature.**

Sentence 1 must contain: what changes for them — what they can now do, avoid, or stop struggling with.

> ✅ "Your teams can now plan dependencies across portfolios without switching tools."
> ✅ "Forecasting accuracy is getting significantly better — here's what changed."
> ❌ "We're excited to announce the release of Ensemble Custom Views in [Product Name]."
> ❌ "Today we're shipping a new feature called Dependency Visualization."

**Why this works:** Customers don't care about features. They care about their job getting easier, their team complaining less, or their executive asking fewer hard questions. Lead with that.

---

## Evidence Hierarchy

Order evidence from most to least persuasive for this audience:

1. **Before/after — how their experience changes** — what did they have to do before? What do they do now?
2. **Outcome for their team or role** — what result does this create for them specifically?
3. **Social proof** — other teams/customers using it (with their permission), or volume of customer requests this solves
4. **How to get started** — direct path to value, minimal friction
5. **Technical details** — footnote-level; only if they need it to adopt or configure

---

## Structure Template

```
[Outcome they gain OR pain they no longer have — 1 sentence]

[Before/after: what changes — 2-3 sentences. Describe the old frustration, then the new reality]

[What's specifically available now — 2-3 bullets. Feature name → outcome it creates]
• [Feature/change] → [what this means for them]
• [Feature/change] → [what this means for them]

[How to get started — 1-3 steps. Make it obvious]
1. [Action]
2. [Action]

[Optional: where to get help — link or contact]
```

---

## Tone Markers

- **Second-person throughout.** "You can now..." not "customers will be able to..."
- **Concrete and specific.** "Reduce weekly planning meetings by eliminating the sync-up for dependency updates" not "improve planning efficiency"
- **Action-oriented.** End with a clear next step — try it, set it up, read the doc
- **Warm but not hollow.** Avoid "exciting," "delighted," "thrilled." Use specifics instead of enthusiasm
- **No internal jargon.** Feature code names, team names, sprint numbers don't belong here

---

## Anti-Patterns

| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| "We're excited to announce Feature X" | Feature-first, company-centric | Lead with the customer outcome |
| "As part of our Q2 roadmap..." | Internal framing — they don't care | Remove; start with the benefit |
| Bullet list of capabilities without outcomes | Reads like a spec, not a benefit | Each bullet: [capability] → [what it means for them] |
| "Please reach out if you have questions" | Passive — feels like a wall | "Try it now at [link]" or "Book a quick setup call" |
| Release notes that list what changed, not why | Customers have to translate code changes to value | Always include "what this means for you" |

---

## Context-Specific Variants

### Champion Communications
When writing to a customer champion (someone advocating internally for your product):
- Equip them to tell the story internally — give them language they can use with their own executives
- Include the "so what" their boss will ask
- See `📚 Knowledge/People/[champion].md` for their specific framing needs

### Release Notes
- Lead with the top 1-2 changes by customer impact, not by engineering work completed
- Group by workflow or persona, not by component or team
- Include "not changed / coming soon" only if customers are actively asking

### Change/Downtime Notices
- Lead with impact ("This affects X") and duration
- Never bury the action they need to take
- Send before + reminder, not just one notice

---

## Integration Notes

- Loaded by `/write --type announcement`, `/write --type release-notes`, or when `--to` indicates external customer
- Pairs with: `/signal` for capturing customer reaction, `/prep` for champion-briefing variant
- For customer-facing sales materials: see `sales-se.md`
