# Shared Claude and Codex rules

Read `~/.claude/CLAUDE.md` and `~/.claude/skills/CODING_GUIDELINES.md` at the start
of work. They are the maintained shared sources; Codex does not expand Claude's
`@` imports. Project instructions override global defaults.

`config.toml` loads project `CLAUDE.md` when no `AGENTS.md` exists. Read local
`CLAUDE.local.md` if present and existing project topic files only as needed.
Maintain shared project facts in the repository instruction file.

Use available Codex tools for Claude workflow intent. Claude model/permission
settings, tool names, auto-memory and lifecycle hooks do not configure Codex.
Prefer native Codex skills for documents, browser/computer control and connected
apps. Delegate only when authorized by the task or applicable instructions.

Migrated `$claude-*` skills read their maintained Claude sources directly;
`~/.codex/claude-compat/manifest.json` maps aliases and disabled duplicates.
Archived migration snapshots are fallbacks, not active configuration. Never
assume a copied skill grants a missing runtime, connector or credential.
