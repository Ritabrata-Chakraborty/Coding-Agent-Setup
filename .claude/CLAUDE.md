# Shared working context

Solo robotics and AI researcher on Ubuntu 24.04, ROS2 Jazzy, Python 3.11 and
PyTorch, using miniforge3 (conda/mamba). Work spans deep RL, UAV simulation,
SLAM, path planning and academic writing.

Coding standards: @skills/CODING_GUIDELINES.md

## Scope and evidence

- Read relevant source and usages before making claims. State uncertainty and
  how to verify it; do not invent APIs, paths or results.
- Carry out action requests within scope. For ambiguous research questions,
  investigate and recommend before editing. Avoid adjacent refactors and new
  files unless the task needs them.
- Do not restructure directories, rename files or modify vendored `external/`
  code unless explicitly authorized.
- Fix verified implementation bugs within scope and describe the fix. Ask when
  intended behavior or research assumptions are ambiguous; report unrelated bugs.
- Ask before destructive or hard-to-reverse actions unless already authorized.
- Verify requirements and run checks appropriate to the change. Report what was
  checked, results and any limits. Parallelize independent tool calls.

## Project context

Project instructions and established conventions take precedence over these
defaults. Read project `CLAUDE.md` or `AGENTS.md` and local overrides when present.
Keep behavior, environment, exact run/test commands and non-obvious constraints
in the project's shared instruction file. Update it when those facts change.
Create a concise project context file when durable facts need recording, rather
than adding an empty template during read-only work.

Read existing `CLAUDE-*.md` topic files on demand. Keep shared facts in repository
context; native auto-memory is specific to the agent runtime.

## Discovery and workflows

Use `rg` / `fd` for direct file and text lookup. When an existing
`graphify-out/graph.json` and the Graphify CLI are available, use scoped
`graphify query`, `path` or `explain` for architectural relationships; verify
details in source before editing or debugging. Use the wiki index for broad
navigation; load the full graph report only when needed. Update an existing graph
after relevant code/context changes when the configured update is local and
available. Do not build a graph merely because a repository lacks one; graph
creation is a separate task that can involve external services and cost.

Select skills from their metadata. For overlapping research, plotting, RL or
writing workflows, consult `~/.claude/skills/WORKFLOW_ROUTING.md` only as needed.
Commands and agents remain under `~/.claude/commands/` and `~/.claude/agents/`;
load them when their workflow is useful, without delegating routine lookups.
Claude has one conditional Graphify SessionStart reminder in `settings.json`.
Codex uses these shared instructions instead of a Claude lifecycle hook.
