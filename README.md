# Decompiling Games Skill

An evidence-driven agent skill for game reverse engineering, with a practical **Bully: Scholarship Edition** workflow and separate local/cloud model responsibilities.

This repository contains original guidance and synthetic examples. It contains no game binaries, assets, recovered retail source, or bundled reverse-engineering tools. It is a research workflow, not a completed Bully decompilation or a promise of whole-game recovery.

## Start here

Read the compact [SKILL.md](SKILL.md), then only the matching domain/game reference. Catalogs and audit reports are optional lookups; linked files are not includes. Use the [decision guide](references/decision-guide.md) when the reconstruction type is unclear. For Bully, use the [edition-specific workflow](references/bully-workflow.md). The default example is **PC Scholarship Edition binary analysis and behavioral reimplementation**; the optional Xbox 360 static-recompilation route requires a different, compatible input.

To use with an agent, provide the repository and ask it to follow `SKILL.md`. For example:

> Use this skill to prepare an analysis-only plan for my owned PC copy of Bully: Scholarship Edition. First establish the exact executable build and a small subsystem to study. Keep binary-derived material local. Do not run the game, install tools, or start inference yet.

Follow your agent client's documented skill-folder setup if you want persistent discovery. This repository does not modify global agent rules or install anything automatically.

## What is included

| Guide | Purpose |
|---|---|
| [Automatic best-fit routing](references/tool-routing.md) | Evidence-first primary/fallback selection, offline router and actual-tool adoption checks |
| [Audited toolkit catalog](references/resource-catalog.md) | 114 named mentions across all 12 supplied sections; canonical sources, duplicates, ambiguity and license limits |
| [Game specialists](references/game-specialists.md) | Retain Bully, Unity, FNV, DS1/DSR × MW2, movement/combat and PS5 routes |
| [Decision guide](references/decision-guide.md) | Choose matching decompilation, reimplementation, static recompilation, or asset conversion |
| [Bully workflow](references/bully-workflow.md) | Fingerprint the correct edition, map engine evidence, and validate one slice |
| [REA and Ghidra](references/rea-and-ghidra.md) | Native default toolchain: when to use REA or Ghidra, pinned setup, approvals and the cloud boundary |
| [Local and cloud models](references/local-cloud.md) | Bound context, protect private inputs, and measure model usefulness |
| [Creator methods and credits](references/creator-methods.md) | Separate IW4L, Chasm, SK8 and recompilation contributions |
| [Source and license catalog](references/source-catalog.md) | Dated primary-source references, roles and reuse boundaries |
| [Validation](references/validation.md) | Differential evidence, publication review and honest progress reporting |

## Try the synthetic comparison

The offline routing example uses synthetic evidence and tool records; it does not inspect a real target, install software or execute any selected tool:

```sh
python3 -B scripts/route_tools.py examples/routing/native-pe.json
python3 -B -m unittest discover -s tests -p 'test_*.py'
```

With an existing Python 3 installation, run:

```sh
python3 scripts/compare_traces.py examples/reference.json examples/candidate.json
```

This compares two invented, schema-checked traces. It executes no external commands, contacts no service and reads no game data. The example demonstrates a validation mechanism, not Bully behavior. See [the comparison contract](references/validation.md#synthetic-comparison-contract) before using it with your own outputs.

## Credits and research scope

The October 18, 2026 research draws on the work of **vladtrc and IW4L contributors; Chasm/chasmlol; dumbad/Ethanw05 and the Skate modding community; SK8-ENGINE contributors and Hailey-Ross; mchughalex; ReXGlue/Tom Clay; Xenia contributors; XenonRecomp contributors; LiquidSnake0; and the Bully tooling community**. Individual contributions and license boundaries are recorded in the [catalog](references/source-catalog.md). No affiliation or endorsement is implied.

Chasm's IW4L/Skate/Minecraft project matches the description that prompted this research. We have not established that “Kazem” is an alias for Chasm. The guide credits documented repository identities.

## Limits, cost and license

This guide was researched and its synthetic example tested; no retail decompilation, gameplay parity test or native Bully build was performed for this release. Upstream progress reports remain upstream claims. Model and tool costs depend on your chosen services and workload; this repository initiates no inference or purchases.

Our original documentation and example code are [MIT licensed](LICENSE). That license does not cover referenced projects or retail game content. Inspect upstream license text and notices before reusing code. Ownership of a game copy alone does not settle every permission question about analysis, cloud transfer or distribution.
