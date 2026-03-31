---
description: Run the memory audit workflow
---
Run a health audit of the workspace memory system. Check for TTL violations, stale memory files, line count warnings, and structural issues.

## Steps

1. Run the memory maintainer audit:
   ```bash
   cd "/Users/jhigh/workspace/🔧 Automation/scripts" && python memory_maintainer.py --audit --workspace "/Users/jhigh/workspace"
   ```

2. Display the health report output to the user.

3. Based on the report, offer specific follow-up actions:
   - If TTL violations: "I can update the `review_by` dates in the affected files"
   - If memory.md near limit: "I can trim memory.md to remove outdated sections"
   - If learned-patterns review overdue: "I can run a pattern review against recent sessions"
   - If no issues: "Memory system is healthy. No action needed."

4. If the user wants to act on any recommendation, proceed with the specific fix.
