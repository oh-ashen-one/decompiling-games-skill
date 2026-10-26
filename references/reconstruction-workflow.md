# Research and reconstruction workflow

Load this when beginning substantive investigation or implementing a recovered slice, not merely selecting a tool. This preserves the detailed evidence and validation guidance. Read only relevant linked references.

## Research and evidence

- Start with primary sources and pinned revisions. Use [the audited 114-mention toolkit catalog](resource-catalog.md) and [the retained game/creator source catalog](source-catalog.md) for leads, then check current documentation, license files and per-file exceptions before reuse. Ambiguous, removed, legacy and partial-fetch records stay explicit. Courses, demonstrations and benchmarks are references, not executable tools. Stars measure attention, not correctness.
- Keep proprietary binaries, assets, generated game code, raw decompiler output, database exports and memory dumps local and outside the public repository. Do not use leaked source. Credit does not confer permission to copy.
- Native default retained: for compatible native binary questions, use REA over MCP with the Ghidra provider, plus headless Ghidra for whole-program analysis, batch exports and persistent annotation. The 2026-10-26 best-fit routing request specializes this default: managed .NET/Unity Mono, IL2CPP, JS/Electron, browser, firmware, WASM and protocols use their matching routes. Load stronger well-known skills where they exist: REA's bundled `reverse-engineer-anything` for REA, `ghidra-iterative-re` for iterative Ghidra annotation, and Ghidra's own docs for mechanics. Read [REA and Ghidra](rea-and-ghidra.md) for pinned setup and privacy. Keep one interface/MCP by default; skip native decompilers when source or decoded formats already answer the question.
- Analyze once and cache by target hash, tool version, loader and analysis options. Query a local index for relevant functions, callers, strings, types and data references instead of sending a whole program to a model.
- Attach provenance and uncertainty to each inference. A decompiler's inferred type or an AI-generated name is a hypothesis until supported by layout, calls or observed behavior.
- For ideas drawn from IW4L and Skate work, use [the attributed methods reference](creator-methods.md). Do not copy unlicensed implementations or describe procedural agent separation as guaranteed clean-room isolation.

## Recover one verifiable slice

1. Select a small behavior with observable inputs and outputs: a file-header parser, handle lookup, coordinate transform, Lua binding or bounded state transition.
2. Write its contract before implementation: widths and signedness, outputs, side effects, lifetime, state ordering, invalid-input handling, numerical rules and unresolved questions.
3. Follow [the local/cloud workflow](local-cloud.md). Route private binary-derived context locally by default. Cloud models receive public references, suitable independently written specifications, synthetic fixtures and original implementation. Sending private material requires specific permission for that material and destination.
4. Implement original code or reuse code under an explicitly compatible license with its notices. Keep research claims separate from implementation choices.
5. Compare controlled cases against the owned original where feasible. Align starting state, input sequence, random seed, coordinate convention and simulation steps. Record the reference environment and instrumentation effects.
6. Use semantic tests: boundaries, malformed input, signedness, state ordering and relevant numerical edge cases. A build or plausible screenshot is insufficient. Use bitwise comparison only when warranted; justify numerical tolerances before examining results.
7. If instrumentation is authorized, gate hooks on the exact binary and address validation, confirm activation, bound log volume, and provide a reversible exit. Compare uninstrumented and instrumented baselines. Stop on an unexpected target, corrupted state or unreliable evidence.

## Deliver and stop honestly

Use [validation and publication checks](validation.md). Report separately: analysis performed, compilation, synthetic tests, comparison against the original, rendered inspection and human gameplay review. State the tested build and coverage denominator; do not convert a function count into a gameplay-completion claim.

Deliver the narrow result, evidence summary, source/notice ledger and next uncertainty. Before publishing, inspect staged files and history for private material and licenses. Do not expand a research request into model installation, paid inference, game execution, asset extraction, deployment or unrelated project changes.

Read-only reconnaissance is the default. Runtime patching, fuzzing, capture, replay and device/process instrumentation need their actual target and operation in scope. Do not bypass DRM, ownership checks, anti-cheat or security controls. Recovered pseudocode is not original source; clean-room records do not establish blanket reuse rights. Preserve unknowns and require runnable-target/differential/gameplay evidence before claiming those outcomes.
