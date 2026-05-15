---
description: Run the COMMAND REFERENCE workflow
---
# AIPMOS Command Reference

Intent detection guide for 25 commands. Match user intent → suggest command. Suggest only when confidence >70%.

---

## Daily Operating Rhythm

### /today
Daily planning, reviewing priorities, checking blockers.
- "What should I work on today?" / "Help me prioritize" / "What's on my agenda?"
- NOT for: creating spec documents, strategic planning, long-term roadmap

### /weekly-review [--week YYYY-MM-DD] [--growth-review [--months N]]
End-of-week PM calibration: decisions, signals, OKRs, relationships, next-week priorities.
- "Weekly review" / "End of week wrap-up" / "Review this week"
- `--growth-review`: Cross-month growth signal synthesis (quarterly cadence)
- NOT for: daily planning (/today), session capture (/checkpoint)

### /granola
Extract meetings from Granola API → save as markdown, surface decisions/actions/signals.
- "Pull my meetings" / "Extract meeting notes" / "Sync Granola"
- NOT for: meeting prep (/prep), post-meeting follow-up (/follow-up)

---

## Meeting Workflow

### /prep
Pre-meeting context assembly: stakeholder read, talking points, decision framing.
- "Prep for my meeting with..." / "Get ready for..." / "Meeting prep for [name]"
- NOT for: post-meeting capture (/follow-up), writing a deck (/deck)

### /follow-up
Post-meeting execution: extract decisions, assign actions, update People/ files, draft comms.
- "Follow up on the meeting" / "What were the action items?" / "Send follow-up for..."
- NOT for: pre-meeting prep (/prep), general writing (/write)

---

## Memory & Session Management

### /memory-health [--refresh [--dry-run]]
Memory system health check + optional session state update.
- "Is my memory stale?" / "Memory health check" / "Update memory" / "Refresh memory"
- `--refresh`: runs memory_updater.py to write current session to memory.md
- NOT for: session-end capture (/checkpoint), pattern extraction (/checkpoint --capture)

### /checkpoint [--capture [type] [description]]
Session-end pipeline: summarize session, update memory.md, extract pattern candidates.
- "End of session" / "Save this session" / "Capture before clearing" / "Safe to /clear?"
- `--capture`: interactive pattern capture (decision/convention/mistake/pattern/tool) with quality gates
- NOT for: mid-session memory refresh (/memory-health --refresh)

---

## Discovery & Strategy

### /discover
Four-phase product discovery: problem → solution → risk → scope. Continuous discovery framework.
- "Discovery for..." / "Validate this problem" / "Research this opportunity" / "Customer discovery"
- NOT for: writing the spec (/spec), competitive research (/research or /industry-brief)

### /think
Strategic analysis, complex decisions, mental models, framing.
- "Help me think through..." / "Should we do X or Y?" / "Strategic analysis of..."
- Automatically applies Type 1/Type 2 classification and AI risk analysis for AI features
- NOT for: writing a spec (/spec), daily task planning (/today)

### /brainstorm
Lightweight persona-driven ideation: PM + Designer + Engineer perspectives.
- "Brainstorm ideas for..." / "What could we do about..." / "Generate options for..."
- NOT for: deep strategic analysis (/think), formal discovery (/discover)

### /align
Stakeholder alignment workflow: map influence, build persuasion arc, draft communications.
- "Get stakeholder buy-in on..." / "Align [name] on..." / "Stakeholder map for..."
- NOT for: general comms drafting (/write), post-meeting follow-up (/follow-up)

---

## Research & Intelligence

### /research
Targeted validation studies, customer research plans, evidence synthesis.
- "Research this assumption" / "Validate this idea" / "Find evidence for..." / "Customer research on..."
- NOT for: competitive analysis (/industry-brief), web scraping (/scrape)

### /industry-brief
Broad market scanning: analyst reports, earnings, job postings, adjacent market signals.
- "Market landscape for..." / "Industry brief on..." / "What's happening in [space]?"
- NOT for: customer-specific research (/research), competitor-only deep dives

### /scrape [url]
Fetch and analyze web page content.
- "Scrape this page" / "Get the content from [url]" / "Analyze this page"
- NOT for: broad research (/research), multi-source intelligence (/industry-brief)

### /signal
Capture customer signal at point of occurrence as atomic nuggets.
- "Capture this signal" / "Customer said..." / "Log this feedback" / "Note this observation"
- NOT for: signal synthesis (/weekly-review Step 2), win/loss deep dives (/win-loss)

### /win-loss [deal-name]
Structured B2B deal analysis: win/loss interview framework, signal extraction, pattern capture.
- "Win/loss on [deal]" / "Why did we lose [account]?" / "Analyze [deal] outcome"
- NOT for: general signal capture (/signal), competitive briefing

---

## Product Artifacts

### /spec [--type full|light|one-pager|context-doc] [--skip-discovery] [--save] [--review path] [--eng-brief prd-path]
Write PRDs with decision-focused structure and quality gates. Review existing PRDs.
- "Write a spec for..." / "PRD for..." / "Document this feature" / "Review this PRD"
- `--eng-brief <path>`: generate SPEC_BRIEF.md engineering handoff from approved PRD
- `--review <path>`: review existing PRD for decision quality (no auto-edits)
- NOT for: strategic framing before spec (/think), story breakdown after (/story)

### /roadmap [--format now-next-later|themes|quarterly]
Quarterly roadmap with themes, now/next/later, explicit exclusions.
- "Create the roadmap" / "Roadmap for Q[N]" / "Roadmap update"
- NOT for: individual feature spec (/spec), backlog prioritization (use `prioritization-craft` skill)

### /story [--prd path] [--dry-run]
Generate Epic → Feature → Story hierarchy from approved PRD.
- "Break this PRD into stories" / "Create backlog from spec" / "Story breakdown for..."
- NOT for: writing the PRD (/spec), roadmap-level planning (/roadmap)

---

## Output & Delivery

### /demo-prep [customer] [product-area]
Customer-ready demo guide: story arc, feature spotlights, discovery questions.
- "Prep a demo for [customer]" / "Demo script for [feature]" / "Get ready to demo..."
- NOT for: pre-meeting stakeholder prep (/prep), general presentation (/deck)

### /data-story [--audience exec|product|sales|cs]
Package analysis into audience-specific narrative: exec BLUF, product, sales, CS.
- "Turn this data into a story" / "Exec-ready summary of..." / "Package this for sales"
- NOT for: full deck creation (/deck), raw data analysis

### /mockup [description]
Generate HTML/CSS UI mockups for prototyping and stakeholder alignment.
- "Mockup for..." / "Show me what this could look like" / "Prototype UI for..."
- NOT for: full deck (/deck), PRD writing (/spec)

### /deck [--format pptx|html]
Create presentation: routes to PPTX (corporate template) or hosted HTML deck.
- "I need a deck" / "Build slides for..." / "PowerPoint for..." / "Hosted deck for..."
- NOT for: demo-specific guides (/demo-prep), single-page mockups (/mockup)

### /write [--type memo|email|brief|one-pager] [audience]
PM communication with audience-aware routing and structure.
- "Write a memo to..." / "Draft an email to [stakeholder]" / "Write this up for exec"
- NOT for: full spec documents (/spec), slide decks (/deck)

---

## UI & Code

### /ui-refine [url-or-description]
Iterative UI refinement loop with scoring until ≥9.3/10.
- "Refine this UI" / "Improve this design" / "Iterate on this until it's good"
- NOT for: mockup generation (/mockup), full design brief

---

## Quick Reference Table

| Need | Command |
|------|---------|
| Plan my day | /today |
| End of week | /weekly-review |
| Pull meeting notes | /granola |
| Pre-meeting prep | /prep |
| Post-meeting actions | /follow-up |
| Memory health | /memory-health |
| End of session | /checkpoint |
| Discovery work | /discover |
| Strategic thinking | /think |
| Brainstorm options | /brainstorm |
| Stakeholder alignment | /align |
| Research/validate | /research |
| Market landscape | /industry-brief |
| Scrape a page | /scrape |
| Log customer signal | /signal |
| Win/loss analysis | /win-loss |
| Write PRD | /spec |
| Engineering handoff | /spec --eng-brief |
| Quarterly roadmap | /roadmap |
| Story breakdown | /story |
| Demo guide | /demo-prep |
| Audience-ready data | /data-story |
| UI prototype | /mockup |
| Presentation/deck | /deck |
| PM communication | /write |
| Refine UI | /ui-refine |

---

## Commands Removed (now handled by skills)

These were deleted. Use the corresponding skill directly:
- `/biz-case` → `business-reasoning` skill
- `/compete` → `competitive-analysis` skill
- `/critique` → `product-critique` skill
- `/experiment` → `exp-driven-dev` skill
- `/jtbd` → `jtbd-building` skill
- `/launch`, `/ship` → `launch-execution` skill
- `/measure` → `metrics-frameworks` skill
- `/narrative` → `strategic-storytelling` skill
- `/ost` → `opportunity-solution-tree` skill
- `/prioritize` → `prioritization-craft` skill
- `/product-depth` → `product-operational-intelligence` skill
- `/reduce` → `reduce` skill
- `/search` → `qmd` skill
- `/strategic-build` → `strategic-build` skill
- `/think` → also `reason` skill for heavy reasoning
