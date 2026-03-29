#!/usr/bin/env python3
"""
Create a ready-to-edit ICP brief markdown file.

This script is intentionally simple: it scaffolds structure and placeholders,
but it does not attempt to infer strategy or auto-generate insights.
"""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


def build_brief(product: str, segment: str) -> str:
    title_product = product or "[Product]"
    title_segment = segment or "[Segment]"
    today = date.today().isoformat()

    return f"""# ICP Brief: {title_product}

Date: {today}
Segment: {title_segment}

## Decision To Support
- [What decision is this brief meant to support?]

## ICP Hypothesis
- Company size or stage:
- Role or champion:
- Painful workflow:
- Tech environment:
- Trigger event:

## Not For
- 
- 
- 

## Champion
- Feels the pain first:
- Makes the shortlist:
- Can carry the deal internally:

## Alternatives
- Status quo:
- Internal workaround:
- Direct competitor:
- Adjacent tool:

## Signal Assessment
### Strong Evidence
- 
- 
- 

### Weak Or Noisy Evidence
- 
- 
- 

### What Still Needs Validation
- 
- 
- 

## Differentiated Value
- Capability:
  - So what:
  - So what:
  - Buyer-valued outcome:

- Capability:
  - So what:
  - So what:
  - Buyer-valued outcome:

## Positioning Draft
- For [target customer] who [problem], {title_product} is a [category] that [value]. Unlike [alternative], it [differentiator].

## Discovery Or Qualification Follow-Ups
- 
- 
- 
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Scaffold an ICP brief markdown file.")
    parser.add_argument("--product", default="", help="Product name to prefill.")
    parser.add_argument("--segment", default="", help="Segment name to prefill.")
    parser.add_argument(
        "--output",
        default="icp-brief.md",
        help="Path to write the markdown file.",
    )
    args = parser.parse_args()

    output_path = Path(args.output).expanduser().resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(build_brief(args.product, args.segment), encoding="utf-8")
    print(f"Wrote ICP brief scaffold to {output_path}")


if __name__ == "__main__":
    main()
