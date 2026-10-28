---
name: claude-academic-paper-86ad19a
description: 12-agent academic paper writing pipeline. 10 modes (full/plan/outline/revision/revision-coach/abstract/lit-review/format-convert/citation-check/disclosure).
  6 paper types, 5 citation formats…
---

# academic-paper

Read `/home/rc/.claude/skills/academic-research-skills/skills/academic-paper/SKILL.md` and only the resources needed for the task. This is a migrated skill; use available Codex tools for its workflow intent. Treat `$ARGUMENTS` as the user's task arguments.

Source/resource paths resolve in the maintained Claude tree. Academic package references (including `${CLAUDE_PLUGIN_ROOT}`) resolve from `/home/rc/.claude/skills/academic-research-skills`; shared scripts, schemas, agents and skills live under `/home/rc/.claude`. Resolve command references such as `academic-paper/SKILL.md` from that package root. The manifest at `/home/rc/.codex/claude-compat/manifest.json` maps workflow names to adapters.

Claude models, permissions, tool names, hooks and auto-memory do not configure Codex. Use native integrations when required. Delegate only when authorized and available; disclose missing runtime capabilities or independent review. Apply current task scope and authorization. Claude usage reports describe Claude, not Codex.
