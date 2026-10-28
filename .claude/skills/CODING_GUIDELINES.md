# Coding standards

This is the shared source of coding conventions for Claude and Codex. Update it
when a convention is agreed upon. Follow explicit project instructions and
established repository conventions first; the layout/config defaults below are
for new Python projects, not a request to migrate existing repositories.

## Structure and configuration

- Group by feature/domain and prefer flat layouts. New projects typically use
  `src/`, matching `tests/`, `docs/`, `scripts/` and `research/`. Keep the root for
  manifests, top-level configuration and primary docs. Do not restructure or
  rename existing files unless asked. Vendored `external/` is read-only unless
  explicitly authorized.
- For new Python projects, use one root `config.py` for parameters, grouped by
  purpose. Keep an existing CLI, YAML, Hydra or other configuration system when
  extending a project. Avoid adding parallel sources of truth.
- Constants use `UPPER_SNAKE_CASE`; use explicit namespaces such as
  `import config as Config`, never wildcard imports.

## Naming and style

- Prefer the shortest unambiguous names. Use `snake_case` for Python files,
  directories, functions and variables; action verbs for functions; singular
  `PascalCase` for classes. Boolean names use `is_`, `has_`, `should_` or `can_`.
  Avoid vague names for non-trivial values; `cfg` is fine in a local context.
- Standalone docs use `UPPER_SNAKE_CASE.md`. Preserve reserved/runtime names,
  including `CLAUDE.md`, `CLAUDE.local.md`, `AGENTS.md`, `SKILL.md`, and named
  command/agent files. Keep existing project memory-file names.
- Write brief, readable code with logical blank-line separation. Do not collapse
  multiple statements onto one line. Introduce a local or helper when reused,
  structurally required, or useful for clarity; avoid single-use indirection.
- Python files start with a 1–2 line module docstring. Function docstrings are
  normally 1–2 lines. Comments explain why, appear above a block, and use inline
  placement only for a non-obvious single line. Use long-dash section headers
  between substantial distinct blocks, following the existing file's style.
- Use type hints on function signatures. Python line length is 100 unless the
  project specifies otherwise. Run the configured linter; for new Python work,
  prefer Ruff (or flake8). Do not claim a clean check that was not run.
- A concept has one name and boolean polarity across the codebase. State units
  consistently; add `_m`, `_s`, `_deg` when ambiguity is possible.

## Correctness and performance

- Fix verified bugs within the requested scope and note them in the change
  summary/commit message. Ask when a fix depends on unclear intended behavior or
  research assumptions. Report unrelated issues without expanding the task.
- Check bounds, shapes/dtypes, silent failures, unexpected mutation, zero/NaN
  handling, dead branches and stale state. Do not mask a defect with compensating
  code elsewhere. Remove dead/duplicate code touched by the change rather than
  commenting it out; avoid unrelated cleanup.
- Prefer vectorized NumPy/PyTorch/Pandas operations when they preserve semantics
  and fit memory. Preallocate known-size arrays and avoid repeated expensive
  allocation/lookups. Use in-place tensor operations only when the original is
  no longer needed and autograd is unaffected. Profile before optimizing.

## Reproducible research

- Seed every random source used by training/evaluation (`random`, NumPy, PyTorch,
  CUDA as applicable). Expose the seed through the existing config/CLI and save
  it with results and checkpoints. Enable deterministic kernels when required
  by the experiment; document performance or reproducibility limits.
- Log hyperparameters, configuration, seed and software versions at run start.
  Label numeric output with metric/context and units when meaningful.
- Keep runs in the project's results area, using unique timestamped or stable
  run/seed identifiers. Preserve resumability and never overwrite prior results
  unintentionally. Keep established deterministic experiment naming/layouts.

## Tests and scripts

- Follow existing test layout; new projects use `tests/` mirroring `src/`.
  Non-trivial behavior changes need relevant deterministic tests: expected and
  edge inputs, shapes/dtypes and failure behavior. Seed stochastic tests; avoid
  flaky wall-clock assertions. Test observable behavior rather than mirroring
  implementation. Documentation-only or trivial edits need proportionate checks.
- Bash automation uses `#!/usr/bin/env bash`, a short purpose comment, quoted
  paths, repository-relative path resolution, and clearly grouped paths,
  parameters, utilities and main work. Allow parameter overrides, validate
  inputs, create required output directories and emit useful contextual logs.
  Use a `main` function when the script has enough structure to benefit from it.
