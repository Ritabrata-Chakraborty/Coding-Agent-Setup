# Refactor Analysis

Analyse target file(s) for refactoring opportunities and produce a written plan.
**This command does not modify any code.** It only generates a report.

## Usage

```
/refactor-analysis @path/to/file.py
/refactor-analysis src/control/cascade_pid.py
```

## Instructions

Produce a markdown report saved to `reports/refactor-analysis_<target>_<YYYY-MM-DD>.md`.

### Analysis Steps

1. **Understand current state**
   - Module purpose, entry points, dependencies
   - Lines of code, function count, max function length

2. **Identify hotspots**
   - Functions over 50 lines — candidates for extraction
   - Duplicated logic — consolidation opportunities
   - Mixed concerns — functions doing more than one thing
   - Magic numbers/strings — candidates for named constants
   - Vectorisation opportunities (loops over arrays)

3. **Assess test coverage**
   - Which functions have tests, which do not
   - Gaps that must be filled before safe refactoring

4. **Propose target architecture**
   - Suggested module split or reorganisation
   - Naming changes needed for consistency with CODING_GUIDELINES
   - Import structure improvements

5. **Risk and sequencing**
   - Order steps from lowest to highest risk
   - Note any behaviour that depends on side effects or ordering

### Report Format

```markdown
# Refactor Analysis: `<file>`
**Date**: YYYY-MM-DD

## Summary
- Lines: N  Functions: N  Max fn length: N lines
- Primary concern: [mixed concerns / duplication / over-length functions / ...]

## Hotspots

| Function | Lines | Issue | Priority |
|----------|-------|-------|----------|
| `fn_name` | 80 | Mixed concerns: X and Y | High |

## Proposed Changes

### 1. [Change description]
- **Why**: ...
- **How**: Extract `fn_a` and `fn_b` from `big_fn`
- **Risk**: Low — no side effects, covered by tests

### 2. ...

## Test Gaps
- `fn_name` — no tests; write before refactoring

## Recommended Sequence
1. Fill test gaps
2. Extract helpers (low risk)
3. Reorganise module structure (medium risk)
```
