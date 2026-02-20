#!/usr/bin/env python3
"""
/today Command - Daily Planning Automation

Generates and delivers a prioritized daily plan based on:
- AgilePlace tasks and cards

Usage:
    python -m today_cmd.main [options]

Options:
    --config PATH    Path to config.yaml (default: today_cmd/config.yaml)
    --dry-run        Generate plan but don't write files
    --skip-storage   Skip writing to /tasks/ directory
    -v, --verbose    Enable verbose logging
    --version        Show version and exit
"""

import argparse
import asyncio
import logging
import os
import sys
from datetime import datetime
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from today_cmd.today_orchestrator import TodayOrchestrator


def capture_command_usage() -> None:
    """Capture command usage for analytics (optional).

    Gracefully degrades if observer system is unavailable.
    This is Phase 1 Memory System tracking for usage analytics.
    """
    try:
        from observers.observer_manager import ObserverManager

        async def _capture():
            manager = ObserverManager()
            await manager.initialize(Path.cwd())
            observer = manager.get_observer("command_usage")
            if observer:
                await observer.capture_command("/today")

        asyncio.run(_capture())
    except Exception:
        # Graceful degradation - analytics is optional
        pass


def setup_logging(verbose: bool = False):
    """Configure logging based on verbosity level."""
    level = logging.DEBUG if verbose else logging.INFO

    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    logger = logging.getLogger(__name__)
    logger.setLevel(level)

    return logger


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Daily planning automation with PM Operating Principles',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python -m today_cmd.main                    # Run with default config
    python -m today_cmd.main --dry-run          # Generate without writing files
    python -m today_cmd.main --skip-storage     # Skip writing to /tasks/ directory
    python -m today_cmd.main -v                 # Verbose logging
    python -m today_cmd.main --config custom.yaml
        """
    )

    parser.add_argument(
        '--config',
        type=str,
        default=None,
        help='Path to config.yaml (default: today_cmd/config.yaml)'
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Generate plan but don\'t write files'
    )

    parser.add_argument(
        '--skip-storage',
        action='store_true',
        help='Skip writing to /tasks/ directory'
    )

    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose logging'
    )

    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s 1.0.0'
    )

    return parser.parse_args()


def load_env_vars():
    """Load environment variables from .env file."""
    # .env is in automation/ directory (two levels up from today_cmd/)
    env_file = Path(__file__).parent.parent / '.env'

    if env_file.exists():
        # Try python-dotenv first
        try:
            from dotenv import load_dotenv
            load_dotenv(env_file)
            logging.getLogger(__name__).debug(f"Loaded .env from {env_file}")
            return
        except ImportError:
            pass

        # Fall back to manual parsing
        with open(env_file) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ.setdefault(key.strip(), value.strip())

        logging.getLogger(__name__).debug(f"Loaded .env from {env_file}")


async def main():
    """Main entry point for /today command."""
    # Parse arguments
    args = parse_args()

    # Setup logging
    logger = setup_logging(args.verbose)
    logger.info("=" * 60)
    logger.info("📅 /today Command - Daily Planning Automation")
    logger.info("=" * 60)

    # Capture command usage (optional analytics)
    capture_command_usage()

    # Load environment variables
    load_env_vars()

    # Check for Google API key
    if not os.getenv('GOOGLE_API_KEY'):
        logger.warning("GOOGLE_API_KEY not set - AI agents will fail")
        logger.warning("Set GOOGLE_API_KEY in .env file or environment")

    try:
        # Initialize orchestrator
        config_path = args.config
        orchestrator = TodayOrchestrator(config_path=config_path)

        # Apply command line overrides
        if args.dry_run:
            logger.info("DRY RUN: Skipping file writes")
            orchestrator.task_writer = None

        if args.skip_storage:
            logger.info("Skipping file writes")
            orchestrator.task_writer = None

        # Execute workflow
        logger.info(f"Starting workflow for {datetime.now().strftime('%Y-%m-%d')}")

        result = await orchestrator.execute()

        # Report results
        if result:
            today_count = result.get('tasks_due_today_count', 0)
            overdue_count = result.get('overdue_count', 0)
            confidence = result.get('confidence_score', 0.0)

            logger.info("")
            logger.info("=" * 60)
            logger.info("✅ TASK FILES GENERATED")
            logger.info("=" * 60)
            logger.info(f"Tasks Due Today: {today_count}")
            logger.info(f"Overdue: {overdue_count}")

            today_path = result.get('today_path')
            if today_path:
                logger.info(f"today.md: {today_path}")

            this_week_path = result.get('this_week_path')
            if this_week_path:
                logger.info(f"this-week.md: {this_week_path}")

            next_week_path = result.get('next_week_path')
            if next_week_path:
                logger.info(f"next-week.md: {next_week_path}")

            logger.info("")
            logger.info("Run '/today' in Claude Code to analyze and prioritize.")

            logger.info("=" * 60)

            return 0
        else:
            logger.error("")
            logger.error("=" * 60)
            logger.error("❌ WORKFLOW FAILED")
            logger.error("=" * 60)
            logger.error("Check logs above for errors")

            return 1

    except KeyboardInterrupt:
        logger.info("\nInterrupted by user")
        return 130

    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
        return 1


if __name__ == '__main__':
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
