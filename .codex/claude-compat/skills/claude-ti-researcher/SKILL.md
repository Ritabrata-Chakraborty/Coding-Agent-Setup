---
name: claude-ti-researcher
description: Gathers competitor landscape, market data, and user evidence from web
  sources for startup idea evaluation. Spawned by /tweak:evaluate before dimension
  evaluation.
---

# ti-researcher

Read `/home/rc/.claude/agents/ti-researcher.md` and only the resources needed for the task. This is a migrated agent; use available Codex tools for its workflow intent. Treat `$ARGUMENTS` as the user's task arguments.

Source/resource paths resolve in the maintained Claude tree. Academic package references (including `${CLAUDE_PLUGIN_ROOT}`) resolve from `/home/rc/.claude/skills/academic-research-skills`; shared scripts, schemas, agents and skills live under `/home/rc/.claude`. Resolve command references such as `academic-paper/SKILL.md` from that package root. The manifest at `/home/rc/.codex/claude-compat/manifest.json` maps workflow names to adapters.

Claude models, permissions, tool names, hooks and auto-memory do not configure Codex. Use native integrations when required. Delegate only when authorized and available; disclose missing runtime capabilities or independent review. Apply current task scope and authorization. Claude usage reports describe Claude, not Codex.
