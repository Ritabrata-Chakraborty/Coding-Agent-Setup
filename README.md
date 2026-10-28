# Coding-Agent-Setup

Personal config for [Claude Code](https://claude.com/claude-code) and Codex (Ubuntu 24.04, ROS2 Jazzy, conda/mamba).

| Path | Contents |
|------|----------|
| `.claude/CLAUDE.md` | Global instructions: profile, coding rules, skill/agent index |
| `.claude/settings.json` | Permissions, hooks, model settings |
| `.claude/agents/`, `commands/`, `scripts/` | Subagents, slash commands, helper scripts |
| `.claude/skills/` | Skills (ML/RL, data, stats, visualization, writing, docs) and coding guidelines |
| `.claude/plugins/known_marketplaces.json` | Plugin marketplace list |
| `.codex/AGENTS.md`, `config.toml` | Codex instructions and config |
| `.codex/claude-compat/` | Mapping of Claude skills for Codex |

## Install

```bash
git clone https://github.com/Ritabrata-Chakraborty/Coding-Agent-Setup.git
cp -r Coding-Agent-Setup/.claude/. ~/.claude/
cp -r Coding-Agent-Setup/.codex/. ~/.codex/
```

Back up existing `~/.claude` and `~/.codex` first. Paths in `.codex/config.toml` assume user `rc`; edit them for other machines.

Credentials, auth, memory, sessions, history and caches are deliberately excluded (see `.gitignore`).
