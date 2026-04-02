# Skill Learning System

This directory is the canonical home for workspace-first skill learning.

## Purpose

The system combines:
- per-skill operational memory via sibling `LEARNED.md` files
- structured run capture from hooks and session history
- eval and candidate generation
- human-reviewed `SKILL.md` revision proposals

## Canonical Files

- `registry.yaml` - inventory of workspace-local skills and wrappers
- `learning-config.yaml` - policy, thresholds, pilot selection, and paths
- `runs.jsonl` - normalized skill run records
- `candidates.jsonl` - recurring lessons waiting for review or acceptance
- `eval-results.jsonl` - scored skill eval results
- `review-queue/` - markdown proposals for `SKILL.md` or eval changes
- `rubrics/` - family-specific evaluation dimensions and thresholds
- `evals/` - seed baseline and holdout cases

## Operating Model

- `SKILL.md` stays human-owned.
- `LEARNED.md` is compact runtime memory for a single skill.
- Broader instruction changes go to `review-queue/`, never directly to `SKILL.md`.
- Durable cross-skill conventions still belong in `🤖 AI/patterns/learned-patterns.md`.
