# Bully: target-specific workflow

Research snapshot: **2026-10-18 UTC**. This is a proposed workflow, not a report of experiments performed with retail files. Read [the source catalog](source-catalog.md) for revision pins and licenses.

## 1. Keep the editions separate

| Target | Suitable research direction | Required checks |
|---|---|---|
| PC Scholarship Edition | PE binary analysis and incremental behavioral/native-engine reimplementation | Confirm expected x86-32 headers, exact patch/hash, imports, calling conventions, pointer width and image base |
| Xbox 360 Scholarship Edition | PowerPC/XEX analysis and separately scoped static recompilation | Compatible owned dump, region/media/title-update identity, big-endian memory, runtime and graphics integration |
| PS2, Wii, Anniversary/mobile | Separate target-specific investigation | Their own binary formats, ABIs, asset variants and tooling; no offset portability assumed |

PC Scholarship Edition is the starting profile in this guide. Apple Silicon may host analysis tools or new code; it does not make a PC source executable ARM. CrossOver or another compatibility layer also changes the reference environment, particularly timing.

Do not feed a PC `bully.exe` to an Xbox 360 translator. Do not replace an existing engine or asset-import project merely because a different reconstruction route exists.

## 2. Establish a read-only baseline

With authorization for local analysis, inventory the specific executable and input assets. Record the [target fingerprint](decision-guide.md#target-fingerprint), tool availability and a task-owned output directory. Keep the retail installation unmodified; private evidence and build products belong outside the public skill checkout.

Record what the user wants to recover: analysis only, a compatible subsystem, a new engine, a binary match, or static translation. “Decompile Bully” is not sufficiently precise to select a success metric.

## 3. Use PC research as leads, not universal layouts

[LiquidSnake0/bully-re](https://github.com/LiquidSnake0/bully-re/tree/dce485bf29117edca4d04b802a169f0a909da432) is an early GPL-3.0 PC Scholarship Edition reimplementation. Its README describes a v1.0 analysis with RTTI, vtables and Lua bindings, plus Ghidra export tools and a local SQLite analysis index. This makes it a useful map of research questions. It does not prove that another executable revision has the same addresses or structures.

Its documentation suggests these concrete checks:

- Check Lua **5.0/5.0.2** behavior and binary interfaces instead of assuming Lua 5.1 compatibility. Verify bindings, stack conventions, ownership and error paths individually. [Lua notes](https://github.com/LiquidSnake0/bully-re/blob/dce485bf29117edca4d04b802a169f0a909da432/docs/lua.md).
- Investigate Gamebryo 2.3/NIF 20.3.0.9 as reported for the analyzed material; do not import GTA RenderWare assumptions. Some PC-set NIF files reportedly use big-endian encoding, so inspect each format header. [NIF notes](https://github.com/LiquidSnake0/bully-re/blob/dce485bf29117edca4d04b802a169f0a909da432/docs/nif.md).
- Verify pool handles, packing, invalid values, object lifetime and generation behavior from evidence. Superficial similarity to a GTA structure is insufficient. [World notes](https://github.com/LiquidSnake0/bully-re/blob/dce485bf29117edca4d04b802a169f0a909da432/docs/world.md).
- Check RTTI relationships, vtable ordering, call signatures and initialization order on the exact build. [Entry-point mapping](https://github.com/LiquidSnake0/bully-re/blob/dce485bf29117edca4d04b802a169f0a909da432/docs/points-entree.md).

### Interpret upstream progress carefully

The October 18 coverage report lists 345 functions, 1.7% of the function count and 2.5% of code bytes. However, [its counting script](https://github.com/LiquidSnake0/bully-re/blob/dce485bf29117edca4d04b802a169f0a909da432/tools/avancement.py) counts addresses referenced in `src/`, excluding generated skeletons; a reference can include code that merely calls a named function. Treat these as **address-reference coverage metrics**, not verified implementation, byte matching or gameplay completion. The [report](https://github.com/LiquidSnake0/bully-re/blob/dce485bf29117edca4d04b802a169f0a909da432/docs/avancement.md) and README's early visual/Lua-harness claims were not independently reproduced for this guide.

## 4. Analyze once, then ask narrow questions

Use an existing authorized Ghidra installation or another suitable analyzer. Save its project locally and key exports to the executable hash, tool version and analysis options. An index should let you retrieve a function and relevant callers, strings, types and data references without dumping the whole executable into a model.

Default to the [REA and Ghidra toolchain](rea-and-ghidra.md):
- Run one headless Ghidra analysis of the fingerprinted executable into a project keyed by its hash.
- Then ask narrow questions through REA's Ghidra provider.

For a project like bully-remake, prefer the decompiled mission scripts and decoded formats first. Reach for the binary when engine behavior is not in the scripts. Examples: a text-table key hash, minigame timing and scoring, ped schedule or authority (prefect) logic, and ambient speech triggers.

Begin with known anchors: imports, distinctive strings, RTTI, vtables, Lua registration tables and initialization paths. For each hypothesis record the target-relative location, observation, inference, confidence and disconfirming test. Keep inferred names distinguishable from names actually found in the binary.

Do not publish raw analysis exports as a convenience cache. A public description can summarize a finding while the underlying binary-derived evidence remains local.

## 5. Work through a bounded slice

A useful progression is a small format loader, then a deterministic handle/transform operation, then one Lua binding and one state transition. Advance only when each step has observable validation; this ordering is a suggestion, not a claim that these components are already reconstructed.

For the selected slice:

1. Define inputs, outputs, invalid cases, memory ownership, side effects and sequence requirements.
2. Create invented fixtures for parsing and edge-case tests. Do not include extracted game files in the public test suite.
3. Implement original code or plan compatible upstream reuse explicitly. If using GPL implementation code, resolve its distribution requirements before incorporating it into a differently licensed project.
4. Compare the same controlled scenario with the original where feasible. Report the edition/hash, environment, initial state, steps and tolerances with each result.
5. Keep separate results for synthetic conformance, original-game observations, visuals and human play. A campus renderer or a Lua harness with stubs cannot establish complete engine behavior.

## 6. Optional Xbox 360 case study

[coole42-pixel/BullyRecomp](https://github.com/coole42-pixel/BullyRecomp/tree/856b4cd98fb591a67b7a312c6c6b6b90da12a66e) targets Scholarship Edition NTSC-U, title `5454081A`, media `0867AD86`, using ReXGlue. The maintainer reports reaching the title menu and tutorial yard, approximately 60 FPS on one laptop configuration and a ten-minute unattended test. Town, missions and interiors remain largely untested. These are bounded upstream reports, not independently measured results or a portability guarantee.

The project documents fixes for function boundaries, static initializers and jump tables. Its [AI notice](https://github.com/coole42-pixel/BullyRecomp/blob/856b4cd98fb591a67b7a312c6c6b6b90da12a66e/AI_USAGE.md) describes AI assistance and limited review/testing. Its [notices](https://github.com/coole42-pixel/BullyRecomp/blob/856b4cd98fb591a67b7a312c6c6b6b90da12a66e/THIRD_PARTY_NOTICES.md) distinguish MIT original work, BSD SDK patches and excluded retail code.

[XenonRecomp](https://github.com/hedge-dev/XenonRecomp/tree/ddd128bcca99fe8bfbb99bea583c972351fa6ace) translates Xbox 360 PowerPC instructions to C++; it does not supply a runtime. Memory endianness, indirect calls, jump tables, exceptions, OS services and graphics need appropriate handling. Generated retail-derived code remains local. A compatible Xbox 360 input is a separate prerequisite, never an implicit substitution for an owned PC copy.

## 7. Keep existing project provenance explicit

The public [bully-remake project](https://github.com/oh-ashen-one/bully-remake/tree/92163805ea0d49596138330da758344f227d8b7f) is a separate PC Scholarship Edition reimplementation/import pipeline. The research audit found independent importers citing bully-re format/behavior findings, rather than a bully-re submodule or compiled dependency. For example, see the [NIF importer](https://github.com/oh-ashen-one/bully-remake/blob/92163805ea0d49596138330da758344f227d8b7f/tools/importers/nif.py).

Its [opening-slice notes](https://github.com/oh-ashen-one/bully-remake/blob/92163805ea0d49596138330da758344f227d8b7f/docs/re-notes/opening-slice-recon.md) use Bully-SE-scripts as research for an original mission representation. Its [locomotion notes](https://github.com/oh-ashen-one/bully-remake/blob/92163805ea0d49596138330da758344f227d8b7f/docs/re-notes/locomotion-spec.md) document external use of bully-mact-tool's CAT_TO_MACT utility to inspect action-tree parameters and clip selection. No BullyRecomp integration was identified in that audit. These are distinct kinds of use: cited research, an external analysis tool, and a runtime dependency should not be conflated.

An older no-license characterization of bully-re in that project's notes is stale relative to the GPL-3.0 license observed in this research. This guide neither modifies that project nor certifies its legal provenance. Any future implementation reuse needs a separate file-level license review.

## 8. A useful first deliverable

Deliver a verified target record, a reproducible local analysis recipe, one narrowly defined behavior contract, synthetic tests, any authorized differential observations, and a short list of unresolved questions. Identify which actions have actually run. Do not label a research plan a completed native port.
