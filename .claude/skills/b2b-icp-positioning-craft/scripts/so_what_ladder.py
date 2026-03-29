#!/usr/bin/env python3
"""
Build a markdown "so what?" worksheet from a list of capabilities.

Read capabilities from a text file or stdin, one capability per line.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def read_capabilities(input_path: str | None) -> list[str]:
    if input_path:
        content = Path(input_path).expanduser().read_text(encoding="utf-8")
    else:
        content = sys.stdin.read()
    return [line.strip("- ").strip() for line in content.splitlines() if line.strip()]


def build_output(capabilities: list[str]) -> str:
    if not capabilities:
        return "# So What? Worksheet\n\n- No capabilities provided.\n"

    sections = ["# So What? Worksheet", ""]
    for capability in capabilities:
        sections.extend(
            [
                f"## Capability: {capability}",
                "",
                "### Immediate Consequence",
                "- ",
                "",
                "### Buyer Impact",
                "- ",
                "",
                "### Business Outcome",
                "- ",
                "",
                "### Risk Of Over-Abstracting",
                "- [What generic claim should be avoided here?]",
                "",
            ]
        )
    return "\n".join(sections).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description='Generate a "so what?" markdown worksheet.')
    parser.add_argument(
        "--input",
        help="Text file containing one capability per line. If omitted, read from stdin.",
    )
    parser.add_argument(
        "--output",
        default="so-what-worksheet.md",
        help="Path to write the markdown worksheet.",
    )
    args = parser.parse_args()

    capabilities = read_capabilities(args.input)
    output_path = Path(args.output).expanduser().resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(build_output(capabilities), encoding="utf-8")
    print(f'Wrote "so what?" worksheet to {output_path}')


if __name__ == "__main__":
    main()
