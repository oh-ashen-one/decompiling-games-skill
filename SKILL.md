---
name: decompiling-games-skill
description: Plan and validate authorized game binary analysis, matching decompilation, behavioral reimplementation, and static recompilation, with evidence-driven local and cloud model workflows. Use for reverse-engineering research and narrow subsystem recovery, including Bully; not for ordinary game creation or obtaining retail files.
---

# Decompiling games

Turn a game-reconstruction request into a target-specific, testable research plan. Distinguish what the binary proves, what observations suggest, and what remains unknown. This skill supplies a method; it does not recover a complete game automatically.

## Establish the target

1. Determine the requested outcome using [the decision guide](references/decision-guide.md): analysis, matching decompilation, behavioral reimplementation, static recompilation, or asset conversion. A native executable is an output, not proof of any particular reconstruction method.
2. Record edition, platform, region, patch/title update, executable hash, architecture, endianness, pointer width, ABI and image base before using addresses or choosing a translator. Inspect headers rather than inferring the target architecture from the host computer.
3. Check the available tools and authorized input files. Preserve the original installation. Work in a task-owned directory and branch; leave other sessions, engines, terminals and model servers alone.
4. For Bully, read [the Bully workflow](references/bully-workflow.md). PC Scholarship Edition and Xbox 360 Scholarship Edition require separate analysis profiles. Do not substitute one for the other.

## Research and evidence

- Start with primary sources and pinned revisions. Use [the dated source catalog](references/source-catalog.md) for leads, then check current documentation, license files and per-file exceptions before reuse. Stars measure attention, not correctness.
- Keep proprietary binaries, assets, generated game code, raw decompiler output, database exports and memory dumps local and outside the public repository. Do not use leaked source. Credit does not confer permission to copy.
- Default toolchain: when a claim depends on a shipped binary, use REA over MCP with the Ghidra provider, plus headless Ghidra for whole-program analysis, batch exports and persistent annotation. Load stronger well-known skills where they exist: REA's bundled `reverse-engineer-anything` for REA, `ghidra-iterative-re` for iterative Ghidra annotation, and Ghidra's own docs for mechanics. This skill governs scope, privacy and validation. Read [REA and Ghidra](references/rea-and-ghidra.md) for when to use which, pinned installation, approvals and the cloud boundary. Skip both when decompiled scripts or decoded formats already answer the question.
- Analyze once and cache by target hash, tool version, loader and analysis options. Query a local index for relevant functions, callers, strings, types and data references instead of sending a whole program to a model.
- Attach provenance and uncertainty to each inference. A decompiler's inferred type or an AI-generated name is a hypothesis until supported by layout, calls or observed behavior.
- For ideas drawn from IW4L and Skate work, use [the attributed methods reference](references/creator-methods.md). Do not copy unlicensed implementations or describe procedural agent separation as guaranteed clean-room isolation.

## Recover one verifiable slice

1. Select a small behavior with observable inputs and outputs: a file-header parser, handle lookup, coordinate transform, Lua binding or bounded state transition.
2. Write its contract before implementation: widths and signedness, outputs, side effects, lifetime, state ordering, invalid-input handling, numerical rules and unresolved questions.
3. Follow [the local/cloud workflow](references/local-cloud.md). Route private binary-derived context locally by default. Cloud models receive public references, suitable independently written specifications, synthetic fixtures and original implementation. Sending private material requires specific permission for that material and destination.
4. Implement original code or reuse code under an explicitly compatible license with its notices. Keep research claims separate from implementation choices.
5. Compare controlled cases against the owned original where feasible. Align starting state, input sequence, random seed, coordinate convention and simulation steps. Record the reference environment and instrumentation effects.
6. Use semantic tests: boundaries, malformed input, signedness, state ordering and relevant numerical edge cases. A build or plausible screenshot is insufficient. Use bitwise comparison only when warranted; justify numerical tolerances before examining results.
7. If instrumentation is authorized, gate hooks on the exact binary and address validation, confirm activation, bound log volume, and provide a reversible exit. Compare uninstrumented and instrumented baselines. Stop on an unexpected target, corrupted state or unreliable evidence.

## Deliver and stop honestly

Use [validation and publication checks](references/validation.md). Report separately: analysis performed, compilation, synthetic tests, comparison against the original, rendered inspection and human gameplay review. State the tested build and coverage denominator; do not convert a function count into a gameplay-completion claim.

Deliver the narrow result, evidence summary, source/notice ledger and next uncertainty. Before publishing, inspect staged files and history for private material and licenses. Do not expand a research request into model installation, paid inference, game execution, asset extraction, deployment or unrelated project changes.
