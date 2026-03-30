---
description: Query Pendo data and segments
---

# Pendo Query

Quick access to Pendo analytics and segmentation data via the Pendo CLI.

## Usage

`/pendo <action>`

## Actions

| Action | Description | Example |
|--------|-------------|---------|
| `segments` | List all segments | `/pendo segments` |
| `visitors <days>` | Query visitors from last N days | `/pendo visitors 30` |
| `accounts <days>` | Query accounts from last N days | `/pendo accounts 30` |
| `activity` | Query activity metrics | `/pendo activity` |
| `trend <feature> <days>` | Trend analysis — detect slope change, compare to prior period | `/pendo trend "dependency-view" 90` |
| `anomaly <metric> <days>` | Detect anomalous movements, surface outlier accounts | `/pendo anomaly "dau" 30` |
| `adoption <feature> <segment>` | Feature adoption rate across named segment | `/pendo adoption "capacity-planning" "enterprise"` |
| `health <account>` | Account health profile — usage trend, feature adoption breadth, active users | `/pendo health "NatWest"` |

## Examples

```
/pendo segments
# Lists all Pendo segments with IDs and names

/pendo visitors 30
# Shows visitor data from the last 30 days

/pendo accounts 7
# Shows account data from the last week

/pendo trend "dependency-view" 90
# Trend analysis for dependency view over 90 days — detects slope change vs. prior period

/pendo anomaly "dau" 30
# Surfaces anomalous DAU movements and outlier accounts in last 30 days

/pendo adoption "capacity-planning" "enterprise"
# Feature adoption rate for capacity planning across enterprise segment

/pendo health "NatWest"
# Account health profile: usage trend, feature breadth, active user count
```

## Analysis Routing

After any substantive Pendo finding, offer:
> "Want to turn this into a story for a specific audience? Run `/data-story --audience <exec|product|sales|cs> [finding]`"

When `trend` shows declining adoption: cross-reference `📚 Knowledge/Research/signals-YYYY-MM.md` for correlated `support` or `cs-escalation` signals from the same timeframe. Correlation across sources is stronger signal than either alone — and can elevate the finding from "usage metric" to "customer signal worth routing."

## Configuration

The Pendo CLI uses environment variables:
- `PENDO_SUBSCRIPTION_ID` - Your Pendo subscription ID
- `PENDO_APP_ID` - Your Pendo app ID

These are loaded from `.env` in the pendo-cli directory.
