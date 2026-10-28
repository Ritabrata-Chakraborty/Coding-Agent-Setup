---
name: claude-autoskill
description: Observe the user's screen via screenpipe, detect repeated research workflows,
  match them against existing scientific-agent-skills, and draft new skills (or composition
  recipes that chain existing…
---

# autoskill

Read `/home/rc/.claude/skills/autoskill/SKILL.md` and only the resources needed for the task. This is a migrated skill; use available Codex tools for its workflow intent. Treat `$ARGUMENTS` as the user's task arguments.

Source/resource paths resolve in the maintained Claude tree. Academic package references (including `${CLAUDE_PLUGIN_ROOT}`) resolve from `/home/rc/.claude/skills/academic-research-skills`; shared scripts, schemas, agents and skills live under `/home/rc/.claude`. Resolve command references such as `academic-paper/SKILL.md` from that package root. The manifest at `/home/rc/.codex/claude-compat/manifest.json` maps workflow names to adapters.

Claude models, permissions, tool names, hooks and auto-memory do not configure Codex. Use native integrations when required. Delegate only when authorized and available; disclose missing runtime capabilities or independent review. Apply current task scope and authorization. Claude usage reports describe Claude, not Codex.
