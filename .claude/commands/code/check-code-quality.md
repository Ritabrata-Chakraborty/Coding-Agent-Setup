# Check Code Quality

Review code against language best-practices, coding conventions, and the project's
CODING_GUIDELINES. Covers Python, C++, and ROS2 patterns.

## Usage

```
/check-code-quality @path/to/file.py
/check-code-quality src/control/
"Check if this follows Python best practices"
```

## Instructions

1. **Detect language and framework** — Python, C++14/17, ROS2, NumPy, PyTorch, etc.
2. **Apply relevant standards** — PEP 8, PEP 484 type hints, ROS2 naming conventions,
   CMake best-practices, NumPy vectorisation idioms
3. **Cross-check CODING_GUIDELINES** — naming, config management, seeding, logging
4. **Prioritise findings** — High (correctness/reproducibility), Medium (style/clarity),
   Low (minor nitpicks)
5. **Provide concrete examples** — show current code and suggested improvement side by side

## Domain-specific Checks

### Python / Research Code
- Type hints on all function signatures
- `ruff`/`flake8` compliance, 100-char line limit
- Vectorised ops instead of explicit loops on arrays
- Randomness seeded at top of training/eval scripts
- Logging includes units and context (not bare floats)
- Each run writes to a unique timestamped output directory

### C++ / ROS2
- `snake_case` for variables and functions, `PascalCase` for classes
- RAII for resource management
- Callback signatures match ROS2 conventions
- No raw `new`/`delete` — prefer smart pointers
- Launch files use typed parameters

### Configuration
- Constants in `UPPER_SNAKE_CASE` with unit suffix where ambiguous (`_m`, `_s`, `_deg`)
- One config file per component under `/config`
- No `from config import *`

## Output Format

```markdown
## Code Quality Review: `<file>`

### Summary
- Language/stack: [Python 3.11 / ROS2 Jazzy / ...]
- Overall: [Good / Needs attention in N areas]

### Issues

#### High Priority
1. **[Issue]**
   - Current: `<code>`
   - Recommended: `<code>`
   - Why: [reason]

#### Medium Priority
...

#### Low Priority
...

### What's Already Good
- [Practice]: [why it's correct]
```
