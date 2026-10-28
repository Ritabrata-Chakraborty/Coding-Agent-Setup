# Explain Architecture Pattern

Identify and explain architectural patterns, design patterns, and structural decisions
in the target codebase or module. Useful for understanding ROS2 package structure,
simulation architectures, control system designs, and RL experiment layouts.

## Usage

```
/explain-architecture
/explain-architecture @path/to/module
/explain-architecture src/control/
```

## Instructions

1. **Analyse project structure** — folder layout, file naming, module relationships
2. **Identify patterns** — control flow, node graphs (ROS2), state machines, RL loops,
   data pipelines, plugin systems
3. **Explain rationale** — why these patterns suit the domain
4. **Illustrate with ASCII diagrams** where relationships are non-obvious
5. **Show concrete examples** from actual code with file:line references

## Output Format

```markdown
## Architecture Analysis: [Target]

### Overview
[One-paragraph summary of the primary architectural approach]

### Patterns Identified

#### [Pattern Name]
- **Where**: `path/to/file.py:line`
- **Why**: [Rationale — domain constraint, performance, modularity]
- **Diagram** (if useful):
  ```
  [ROS node] --topic--> [ROS node]
  ```

### Data / Control Flow
[How data moves through the system end to end]

### Strengths and Trade-offs
- **Strengths**: ...
- **Trade-offs**: ...

### Recommendations
[Only if asked or clearly beneficial — scope to what was requested]
```
