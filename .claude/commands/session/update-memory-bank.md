# Update Memory Bank

Sync `CLAUDE.md` and any `CLAUDE-*.md` memory bank files in the current repo after
a session that changed behaviour, patterns, or project structure.

## Usage

```
/update-memory-bank
```

Run at the end of a work session before closing.

## Instructions

1. **Review what changed this session**
   - New code patterns introduced
   - Architecture decisions made
   - Bugs found and fixed
   - Config variables added or renamed
   - Build/test commands that changed

2. **Update `CLAUDE.md`** in the project root
   - Reflect any new commands, patterns, or conventions
   - Remove stale information

3. **Update relevant `CLAUDE-*.md` files** (only those that exist)
   - `CLAUDE-activeContext.md` — current state, goals, what's in progress
   - `CLAUDE-patterns.md` — new code patterns or idioms established
   - `CLAUDE-decisions.md` — architecture decisions made with rationale
   - `CLAUDE-troubleshooting.md` — new known issues or fixes discovered

4. **Sync key information to auto-memory**
   - Write critical patterns and decisions to `~/.claude/projects/.../memory/`
     topic files so they survive a `CLAUDE.md` reset
   - Update `memory/MEMORY.md` index if new topic files are created

5. **Confirm**
   - Report which files were updated and what changed
   - Note anything that could not be captured
