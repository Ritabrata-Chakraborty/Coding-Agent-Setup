# Applied Claude and Codex cleanup — 2026-10-28

Shared global context plus coding standards shrank from 21,995 to 7,754 bytes (65% smaller). This measures text size, not a model-specific token count. Claude imports the standards via `@skills/CODING_GUIDELINES.md`; Codex explicitly reads the same two files.

## Changes

- Removed duplicated global rule/catalog tables, retaining task scope, source verification, profile and project context. Moved workflow disambiguation to `~/.claude/skills/WORKFLOW_ROUTING.md`, read on demand.
- Resolved bug rules: fix verified implementation bugs within scope; ask when intended behavior/research assumptions are unclear. Existing repo instructions, layout, config systems and test conventions take precedence; new-project defaults remain explicit.
- Condensed coding examples into concrete rules while preserving seeding, experiment integrity, naming, comments, linting, performance and tests. Deterministic run/seed names and resumability are supported alongside timestamped runs.
- Claude permissions: 867 accumulated approvals -> 9 retained rules (eight existing codegraph inspection tools and WebSearch). Common read-only shell commands already have Claude's built-in handling. Historical installation, mutation, publish, sudo and arbitrary Python approvals were removed, not converted to Codex permissions. No new deny rules or approval-mode changes were introduced.
- Extra directories: 25 -> 3 (`/tmp`, `~/.claude`, `~/.tweakidea`). Old project-specific paths, `.ssh`, broad home reads and session scratch entries are no longer permanently preapproved. Routine edits/tests remain governed by each runtime and project settings; an old one-off command may prompt again.
- Replaced two repeated PreToolUse reminders with one short conditional SessionStart hook. It emits context only if an existing graph and the Graphify CLI are present; it does not build graphs or execute Graphify. No automatic graph generation on entering new repos.
- Four exact duplicate academic skill directory trees are archived and replaced with relative symlinks to their canonical siblings. Both public path layouts still work. Different synced Claude runtime variants remain untouched.
- 23 curated Claude skill/agent descriptions were shortened. Fixed the code-searcher agent's invalid YAML description. Unrelated vendor workflow bodies and synced content remain unchanged.
- All 121 Codex adapters now read the maintained Claude source directly, avoiding stale snapshot workflows. Their descriptions are compact and their runtime notes remain explicit. 101 remain enabled; 20 redundant/unavailable runtime entries are disabled with `[[skills.config]]`. Files and discovery links are preserved.
- Existing native Codex plugins, MCP server configuration, models, visual preferences and trust/approval settings are preserved. No project source files were changed.

## Disabled Codex adapters

- `claude-academic-paper-86ad19a`: Identical academic plugin entry; canonical un-suffixed adapter remains enabled.
- `claude-academic-paper-reviewer-e15cd08`: Identical academic plugin entry; canonical un-suffixed adapter remains enabled.
- `claude-academic-pipeline-183820f`: Identical academic plugin entry; canonical un-suffixed adapter remains enabled.
- `claude-deep-research-e195c69`: Identical academic plugin entry; canonical un-suffixed adapter remains enabled.
- `claude-docx`: Use native Codex document, browser, connected-app, memory or skill-authoring capability; Claude runtime variant retained.
- `claude-pdf`: Use native Codex document, browser, connected-app, memory or skill-authoring capability; Claude runtime variant retained.
- `claude-pptx`: Use native Codex document, browser, connected-app, memory or skill-authoring capability; Claude runtime variant retained.
- `claude-built-in-browser`: Use native Codex document, browser, connected-app, memory or skill-authoring capability; Claude runtime variant retained.
- `claude-chrome-browser`: Use native Codex document, browser, connected-app, memory or skill-authoring capability; Claude runtime variant retained.
- `claude-computer-use`: Use native Codex document, browser, connected-app, memory or skill-authoring capability; Claude runtime variant retained.
- `claude-docs`: Use native Codex document, browser, connected-app, memory or skill-authoring capability; Claude runtime variant retained.
- `claude-docx-97af66e`: Use native Codex document, browser, connected-app, memory or skill-authoring capability; Claude runtime variant retained.
- `claude-google-workspace`: Use native Codex document, browser, connected-app, memory or skill-authoring capability; Claude runtime variant retained.
- `claude-import-memory`: Use native Codex document, browser, connected-app, memory or skill-authoring capability; Claude runtime variant retained.
- `claude-morning`: Use native Codex document, browser, connected-app, memory or skill-authoring capability; Claude runtime variant retained.
- `claude-pdf-4cc22f1`: Use native Codex document, browser, connected-app, memory or skill-authoring capability; Claude runtime variant retained.
- `claude-pptx-2b58404`: Use native Codex document, browser, connected-app, memory or skill-authoring capability; Claude runtime variant retained.
- `claude-skill-creator`: Use native Codex document, browser, connected-app, memory or skill-authoring capability; Claude runtime variant retained.
- `claude-xlsx`: Use native Codex document, browser, connected-app, memory or skill-authoring capability; Claude runtime variant retained.
- `claude-xlsx-f7e7ac6`: Use native Codex document, browser, connected-app, memory or skill-authoring capability; Claude runtime variant retained.

## Dependencies and maintenance

Restart both apps to load the configuration. Format, paths, hook behavior and unchanged native plugin/MCP settings are checked locally; external connector/model workflows were not executed.

The standalone humanizer references `voice-indexer.py` and `~/.claude/voice-fingerprint.json`, neither of which exists in this installation. Its dependency is now visible in its description. Use the separate synced/sample-based humanizer when no fingerprint is available; no substitute profile was invented.

Claude skill edits are consumed by Codex on next skill use. Discovery descriptions and adapter inventory do not automatically refresh when skills are renamed or added; update the corresponding adapter/manifest for those changes. Claude sync or academic plugin upgrades can recreate vendor duplicates, so review after updates. Archived `source/` workflows are historical fallbacks; the rules snapshots were refreshed.

Backups are in the sibling `backups/cleanup-*` directory. It contains every overwritten file, the four original duplicate directory trees and a rollback script. The installer checks hashes to avoid overwriting concurrent edits. Rollback restores the state immediately before this cleanup, while retaining the initial Codex migration.

Official format references: [Codex skills](https://learn.chatgpt.com/docs/build-skills), [Claude settings](https://code.claude.com/docs/en/settings), [Claude hooks](https://code.claude.com/docs/en/hooks), [Claude memory imports](https://code.claude.com/docs/en/memory), [Claude permissions](https://code.claude.com/docs/en/permissions).
