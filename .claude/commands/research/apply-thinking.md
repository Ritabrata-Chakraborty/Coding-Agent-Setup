# Apply Thinking

Enhance a prompt or problem statement with extended reasoning frameworks so that
Claude produces deeper, more reliable analysis. Useful for complex algorithm design,
controller tuning strategies, RL reward shaping, and architecture decisions.

## Usage

```
/apply-thinking @path/to/prompt.md
/apply-thinking "Design a reward function for hover-to-waypoint navigation"
```

**Target**: `$ARGUMENTS` — a file path or inline problem statement.

## Instructions

Read the target prompt or problem, then rewrite it (or answer it) using the following
structure. The goal is to surface assumptions, enumerate alternatives, and reason
through trade-offs before committing to a solution.

### Step 1 — Problem Decomposition
- What is the exact goal?
- What are the hard constraints (physics, compute budget, API limits)?
- What are the soft constraints (maintainability, reproducibility)?
- What would a wrong answer look like?

### Step 2 — Alternative Approaches
List 2–4 plausible approaches. For each:
- Core idea in one sentence
- Key advantage
- Key risk or weakness

### Step 3 — Evaluation Against Constraints
Score each approach against the constraints identified in Step 1.
Eliminate clearly dominated options.

### Step 4 — Recommended Approach
State the chosen approach and the decisive reasons.
Note any remaining uncertainties and how to resolve them experimentally.

### Step 5 — Implementation Sketch
Outline the first concrete steps. Include code structure, key variables,
verification experiments, and expected failure modes.

## Output

If applied to a file: overwrite the file with the enhanced version.
If applied to an inline problem: respond directly with the structured analysis.
