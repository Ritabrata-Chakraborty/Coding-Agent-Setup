# Cleanup Context

Consolidate and trim bloated `CLAUDE-*.md` memory bank files in the current repo.
Removes duplicate content, obsolete entries, and verbose descriptions that waste
context window space.

## Usage

```
/cleanup-context
```

## Instructions

### 1. Audit current state

```bash
find . -name "CLAUDE-*.md" -exec wc -c {} \;
```

List files with size. Flag any over 20 KB as primary targets.

### 2. Identify waste

- Content duplicated across multiple files — consolidate into one
- Entries explicitly marked REMOVED, DEPRECATED, or RESOLVED — delete them
- Verbose setup/architecture descriptions that duplicate what code already shows
- Outdated code examples that no longer match the codebase

### 3. Consolidate

For files covering the same topic area:
- Merge into a single comprehensive file
- Preserve all technical detail, implementation examples, and troubleshooting notes
- Preserve all todo lists, planned work, and decision rationales — never delete these
- Remove the originals and update `CLAUDE.md` references

### 4. Streamline `CLAUDE.md`

- Replace verbose inline descriptions with a one-line summary + pointer to the CLAUDE-*.md file
- Remove instructions that duplicate global `~/.claude/CLAUDE.md` rules

### 5. Archive resolved content

If historically useful but no longer active:
- Move to `archive/` subdirectory
- Add an index entry in `archive/README.md`
- Update `CLAUDE.md` with archive pointer

### 6. Report

State: files changed, KB saved, what was preserved, what was removed and why.

## Preservation rules

Always keep:
- Todo lists and planned features
- Architecture decisions with rationale
- Troubleshooting guides and known-issue fixes
- Session achievement logs

Only remove:
- Confirmed duplicates
- Explicitly obsolete/deprecated content
- Auto-generated reports that are no longer current
