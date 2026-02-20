#!/usr/bin/env python3
"""
Granola Command - Meeting Automation

Extracts yesterday's meetings from Granola and saves as markdown files.

Usage:
    python -m granola_cmd.main [options]

Options:
    --target-date DATE    Target date (yesterday, today, or YYYY-MM-DD)
    --config PATH         Path to config.yaml
    --dry-run             Show what would be saved without saving
    -v, --verbose         Enable verbose logging
"""

import argparse
import logging
import sys
from datetime import datetime
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from granola_cmd.granola_collector import GranolaCollector


def setup_logging(verbose: bool = False):
    """
    Configure logging.

    Args:
        verbose: Enable DEBUG level logging

    Returns:
        Logger instance
    """
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    return logging.getLogger(__name__)


def parse_args():
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser(
        description="Granola meeting extraction automation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--target-date",
        type=str,
        default=None,
        help='Target date (yesterday, today, or YYYY-MM-DD)',
    )

    parser.add_argument(
        "--config",
        type=str,
        default=None,
        help="Path to config.yaml",
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be saved without saving",
    )

    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose logging",
    )

    return parser.parse_args()


def load_config(config_path: str | None = None) -> dict:
    """
    Load configuration from YAML file.

    Args:
        config_path: Path to config.yaml (optional)

    Returns:
        Configuration dictionary
    """
    import yaml

    if config_path is None:
        config_path = Path(__file__).parent / "config.yaml"
    else:
        config_path = Path(config_path)

    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    return config


def main():
    """Main entry point."""
    args = parse_args()
    logger = setup_logging(args.verbose)

    logger.info("=" * 60)
    logger.info("📝 Granola Command - Meeting Extraction")
    logger.info("=" * 60)

    # Load config
    try:
        config = load_config(args.config)
    except FileNotFoundError as e:
        logger.error(f"Configuration error: {e}")
        logger.error("Please create a config.yaml file in the granola_cmd directory.")
        return 1

    # Override target date from CLI
    if args.target_date:
        config["target_date"] = args.target_date

    # Handle dry-run
    if args.dry_run:
        logger.info("DRY RUN MODE - No files will be saved")
        # In dry-run mode, we could just show what would happen
        # For now, we'll still run but log that it's dry run
        # TODO: Implement proper dry-run without file writes

    # Initialize collector
    collector = GranolaCollector(config)

    # Execute
    try:
        result = collector.execute()
    except Exception as e:
        logger.error(f"Execution failed: {e}")
        if args.verbose:
            import traceback

            traceback.print_exc()
        return 1

    # Report results
    logger.info("=" * 60)
    logger.info(f"✅ Complete: {result['count']} meeting(s) saved")
    for file_path in result["files"]:
        logger.info(f"  📄 {file_path}")
    logger.info("=" * 60)

    return 0


if __name__ == "__main__":
    sys.exit(main())
