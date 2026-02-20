#!/usr/bin/env python3
"""Launcher for /today command that resolves workspace paths dynamically.

This script is called by the Claude Code /today command and handles:
- Workspace discovery via AIPMOSConfig
- Path resolution to run main.py
- Argument parsing and forwarding
"""

import os
import sys
import subprocess
from pathlib import Path

# Find workspace root by searching upward for .aipmos directory
_current_dir = Path(__file__).resolve().parent
while _current_dir != _current_dir.parent:  # Not at filesystem root
    if (_current_dir / ".aipmos").exists():
        _workspace_root = _current_dir
        break
    _current_dir = _current_dir.parent
else:
    # Fallback: use directory structure heuristics
    _workspace_root = Path(__file__).parent.parent.parent.parent

# Add scripts directory to path for imports
_scripts_dir = _workspace_root / "🔧 Automation" / "scripts"
sys.path.insert(0, str(_scripts_dir))

from shared.aipmos_config import AIPMOSConfig


def main():
    """Launch the today workflow with resolved paths."""
    try:
        # Discover workspace and resolve paths
        config = AIPMOSConfig()
        scripts_dir = config.paths.get("scripts")

        # Fallback if scripts path not in config
        if not scripts_dir:
            scripts_dir = config.workspace_root / "🔧 Automation" / "scripts"

        main_py_path = scripts_dir / "today_cmd" / "main.py"

        # Verify script exists
        if not main_py_path.exists():
            print(f"Error: Script not found: {main_py_path}", file=sys.stderr)
            sys.exit(1)

        # Build command with Python
        cmd = [sys.executable, str(main_py_path)] + sys.argv[1:]

        # Forward all arguments to main.py
        result = subprocess.run(
            cmd,
            check=False,
            cwd=config.workspace_root,
        )

        sys.exit(result.returncode)

    except RuntimeError as e:
        # Workspace not found or other config error
        print(f"Error: {e}", file=sys.stderr)
        print("\nHint: Run 'aipmos init' to initialize this workspace.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
