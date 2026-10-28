# ccusage Daily Report

Summarise daily Claude Code token usage and costs using the `ccusage` CLI.

## Usage

```
/ccusage-daily
```

## Instructions

1. Run `bunx ccusage claude daily` via Bash
2. If `ccusage` is not installed, report that and stop
3. Parse output and produce the report below

## Report Format

```markdown
## Claude Code Usage — Daily Summary

### Executive Summary
- Period: YYYY-MM-DD to YYYY-MM-DD  (N days)
- Total cost: $X.XX
- Average daily cost: $X.XX
- Peak day: YYYY-MM-DD ($X.XX)
- Cache efficiency: X%

### Token Totals by Model

| Model | Total tokens | Input | Output | Cache read | Total cost | Avg/day |
|-------|-------------|-------|--------|------------|------------|---------|

### Top 15 Days by Cost

| Date | Model | Input (M) | Output (M) | Cache read (M) | Cost |
|------|-------|-----------|------------|----------------|------|

### Insights
- High-cost days (>$20): N
- Cache effectiveness: [good / moderate / low] — X% of input from cache
- Primary model: [sonnet / opus]
- Notable patterns: [any trends in usage]

### Recommendations
[1–3 concrete suggestions based on the data]
```

Report token counts in millions (e.g. 1,234,567 → 1.23 M). Limit the daily table
to the top 15 highest-cost days.

---

## Command Reference

```bash
bunx ccusage claude daily  # Default daily report
bunx ccusage claude daily --json  # JSON output for parsing
bunx ccusage claude weekly  # Weekly breakdown
bunx ccusage claude monthly  # Monthly breakdown
bunx ccusage claude daily --since YYYY-MM-DD --until YYYY-MM-DD  # Custom date range
bunx ccusage claude daily --timezone UTC  # Specify timezone
bunx ccusage claude daily --instances  # Group by project/instance
bunx ccusage --compact  # Force compact table mode
```
