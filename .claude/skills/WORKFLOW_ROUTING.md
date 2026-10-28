# Workflow routing

Read only when skill descriptions overlap; this is shared by both coding agents.

| Task | Preferred workflow |
| --- | --- |
| Standard single-agent RL/prototyping | stable-baselines3 |
| High-throughput/vectorized RL | pufferlib |
| Focused scientific draft | scientific-writing |
| Complete manuscript and revision pipeline | academic-research-skills/academic-paper or academic-pipeline |
| Targeted literature search/review | paper-lookup or literature-review, scoped to the request |
| Rigorous systematic research pipeline | academic-research-skills/deep-research |
| Publication figure | scientific-visualization; matplotlib/seaborn as needed |
| Quick statistical exploration | seaborn |
| Statistical test selection/reporting | statistical-analysis |
| Programmatic statistical models/diagnostics | statsmodels |
| Humanize using pasted writing samples | synced humanizer; Codex alias claude-humanizer-ea7730f |
| Humanize using a local corpus fingerprint | standalone humanizer, only when its indexer/fingerprint is available |

Claude synced browser, computer-use, Google Workspace and document skills are
runtime-specific. Preserve them for Claude. In Codex, use native plugins for the
corresponding capabilities; redundant adapters are disabled in config.toml.
The synced and standalone writing/research variants differ, so keep both with
distinct descriptions rather than treating them as identical copies.

Academic plugin resources use the package root
`~/.claude/skills/academic-research-skills/`. Its `skills/<name>` paths alias the
canonical top-level skill folders. Preserve these aliases when updating the
plugin. Plugin upgrades or Claude sync may recreate duplicates; review afterward.
