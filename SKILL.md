---
name: decompiling-games-skill
description: Plan and validate authorized game binary analysis, matching decompilation, behavioral reimplementation, and static recompilation, with evidence-driven local and cloud model workflows. Use for reverse-engineering research and narrow subsystem recovery, including Bully; not for ordinary game creation or obtaining retail files.
---

# Decompiling games

Use this for authorized analysis or reconstruction of an existing game, not ordinary game creation. Preserve working project-specific SDK/loader workflows and other sessions' files, engines and jobs.

## Load only what this task needs

This is the entrypoint, not a request to read the library. **Do not preload catalogs, audit reports, the JSON decision table or every linked file.** A link is a lookup destination, not an include. Select one relevant domain below, then read only its needed upstream docs. Retain already-read guidance within the task; do not reread unchanged files each turn.

1. Establish the requested output, exact edition/build/hash, parsed format/platform/architecture and engine/runtime evidence, actual host, available tools/licenses, authorized operations and disclosure scope. Never infer platform from filename or host. Stop at conflicting/unknown evidence.
2. Preserve a suitable established project workflow. Otherwise select one primary and a justified fallback from the relevant route below. Before using it, inspect version-matched upstream docs/license/dependencies and invoke the installed supported tool for the smallest authorized question. Missing prerequisites do not authorize installs. Keep one MCP/interface by default.
3. Use the optional offline `scripts/route_tools.py <manifest.json>` for a deterministic check; it prints only the selected route. Its JSON table is read by Python, not pasted into model context. Read [manifest instructions](references/routing-manifest.md) only when preparing that input.

| Target/task evidence | Read only this route |
|---|---|
| Native PE/ELF/Mach-O | [Native](references/routes/native.md) |
| .NET, Unity Mono/IL2CPP or NativeAOT | [Managed/native runtime distinction](references/routes/managed.md) |
| Electron or JavaScript source | [JavaScript](references/routes/javascript.md) |
| Browser behavior | [Browser](references/routes/browser.md) |
| Firmware or Apple/mobile artifacts | [Firmware/mobile](references/routes/firmware.md) |
| WebAssembly | [WASM](references/routes/wasm.md) |
| Recorded traffic or binary protocols | [Protocols](references/routes/protocol.md) |
| Runtime observation, patching, capture or fuzzing | [Runtime scope](references/routes/runtime.md) |
| Learning only | [Education](references/routes/education.md) |
| Bully/FNV/DS1/DSR/MW2, movement/combat or PS5 | [Game index](references/game-specialists.md), then only the matching game |

## Look up sources when needed

For a tool/license/source question, run `python3 -B scripts/catalog_lookup.py --query ILSpy` or `--section 05`. Output is filtered and capped; refine the query or page deliberately. The [114-entry catalog and audit](references/resource-catalog.md) and [historical game/creator catalog](references/source-catalog.md) are optional lookups, not required reading. Courses/benchmarks are references, never executable adapters.

## Evidence and completion

For substantive research or implementation, load [the reconstruction workflow](references/reconstruction-workflow.md). Use [the decision guide](references/decision-guide.md) when the requested reconstruction type is unclear; [validation](references/validation.md) before claiming results or publishing. Keep target hashes, observations, hypotheses, failures and unknowns separate. A build, pseudocode or screenshot does not prove original source recovery or gameplay parity.

Default to read-only work. Keep private binaries, assets, dumps and decompiler output local; cloud disclosure requires authority for that material and destination ([local/cloud guidance](references/local-cloud.md) when relevant). Runtime actions need their actual operation/target in scope. No DRM/ownership/anti-cheat bypass, unrelated installation or paid calls. Clean-room records do not establish reuse rights; inspect licenses/notices before reuse or publication.
