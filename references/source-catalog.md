# Source, credit and license catalog

Observed **2026-10-18, approximately 20:21–20:25 UTC**. Star counts were supplied by the research pass from live GitHub REST repository metadata (`GET https://api.github.com/repos/{owner}/{repo}`). They are a dated observation, not a quality score or a promise of current status. This is a relevance-filtered catalog, ranked within categories, not an exhaustive global leaderboard.

The 56 ranked entries cover native analysis, AI interfaces, static recompilation, game projects and comparison tooling. High-star Java/.NET tools and generic model servers were outside this native-Bully search scope. Read only the category relevant to the chosen target.

**License evidence:** a linked label points to a license/notice file inspected in the research; **API** indicates metadata identification only, requiring actual file-level review before reuse. Some API-only entries also link to a candidate license location for follow-up. GitHub GPL identifiers do not resolve “only” versus “or later.” Null/NOASSERTION does not mean unrestricted use. Root licenses do not override third-party notices or establish rights to retail-derived material.

All sources here are **methodology references or tool candidates**, not bundled dependencies or copied/adapted files. No upstream implementation, manual or skill is vendored. Our MIT license covers only our original material.

## Starting shortlist

For a PC Scholarship Edition investigation, begin with a local Ghidra project, a small validated analysis interface and, when authorized, x32dbg or controlled instrumentation. LEGO Island and DX-Ball offer useful x86/MSVC comparison methods; bully-re supplies target-specific leads. Check each against the exact executable. Adding multiple AI bridges at once makes failures and disclosure boundaries harder to diagnose.

## Native analysis and validation tools

| Rank | Repository | Stars | License evidence | Role and limitation |
|---:|---|---:|---|---|
| 1 | [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) | 90,802 | [Apache-2.0](https://github.com/NationalSecurityAgency/ghidra/blob/master/LICENSE) | Disassembly, decompilation and headless analysis; pseudo-C is inferred evidence. |
| 2 | [x64dbg/x64dbg](https://github.com/x64dbg/x64dbg) | 49,938 | [Modified GPLv3, plugin exception; API NOASSERTION](https://github.com/x64dbg/x64dbg/blob/development/LICENSE) | Use x32dbg for a verified 32-bit Windows target. |
| 3 | [radareorg/radare2](https://github.com/radareorg/radare2) | 25,085 | [Mainly LGPLv3; mixed components](https://github.com/radareorg/radare2/blob/master/COPYING.md) | Scriptable analysis; inspect component obligations. |
| 4 | [frida/frida](https://github.com/frida/frida) | 22,360 | [wxWindows Library Licence 3.1](https://github.com/frida/frida/blob/main/COPYING) | Dynamic observation, not source recovery. |
| 5 | [rizinorg/cutter](https://github.com/rizinorg/cutter) | 20,053 | [GPL-3.0](https://github.com/rizinorg/cutter/blob/dev/COPYING) | Rizin-based graphical analysis environment. |
| 6 | [unicorn-engine/unicorn](https://github.com/unicorn-engine/unicorn) | 9,466 | [GPL-2.0 with component exceptions](https://github.com/unicorn-engine/unicorn/blob/master/COPYING) | Isolated CPU tests; not a complete game/OS runtime. |
| 7 | [angr/angr](https://github.com/angr/angr) | 9,214 | [BSD-2-Clause](https://github.com/angr/angr/blob/master/LICENSE) | Bounded symbolic questions with explicit environment models. |
| 8 | [capstone-engine/capstone](https://github.com/capstone-engine/capstone) | 9,114 | [BSD-3-Clause core; additional notices](https://github.com/capstone-engine/capstone/blob/next/LICENSES/LICENSE.TXT) | Instruction extraction; current license path is under LICENSES. |
| 9 | [avast/retdec](https://github.com/avast/retdec) | 8,650 | [MIT core; third-party licenses](https://github.com/avast/retdec/blob/master/LICENSE) | Alternative x86/PE decompiler; limited maintenance reported. |
| 10 | [microsoft/Detours](https://github.com/microsoft/Detours) | 6,409 | [MIT (API)](https://github.com/microsoft/Detours/blob/main/LICENSE.md) | Windows instrumentation support. |
| 11 | [lief-project/LIEF](https://github.com/lief-project/LIEF) | 5,596 | [Apache-2.0](https://github.com/lief-project/LIEF/blob/main/LICENSE) | Deterministic PE/ELF/Mach-O inventory and manipulation. |
| 12 | [uxmal/reko](https://github.com/uxmal/reko) | 2,621 | GPL-2.0 (API) | Alternative native decompiler; evaluate exact-target suitability. |

## AI interfaces, research models and workflow routers

| Rank | Repository | Stars | License evidence | Role and limitation |
|---:|---|---:|---|---|
| 1 | [morluto/rea](https://github.com/morluto/rea) | 320,610 | [MIT](https://github.com/morluto/rea/blob/main/LICENSE) | Analysis-engine wrapper/evidence system; cloud tool results can leave the host. |
| 2 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | 42,550 | [MIT (API)](https://github.com/zhaoxuya520/reverse-skill/blob/main/LICENSE) | Broad routing reference; do not inherit unrelated pentest/bootstrap scope. |
| 3 | [mrexodia/ida-pro-mcp](https://github.com/mrexodia/ida-pro-mcp) | 12,997 | [MIT (API)](https://github.com/mrexodia/ida-pro-mcp/blob/main/LICENSE) | README recommends HexRaysSA/ida-mcp; legacy documented route excludes IDA Free. |
| 4 | [LaurieWired/GhidraMCP](https://github.com/LaurieWired/GhidraMCP) | 11,384 | [Apache-2.0 (API)](https://github.com/LaurieWired/GhidraMCP/blob/main/LICENSE) | Focused bridge; check current Ghidra/headless/transport compatibility. |
| 5 | [albertan017/LLM4Decompile](https://github.com/albertan017/LLM4Decompile) | 7,143 | [MIT repository (API)](https://github.com/albertan017/LLM4Decompile/blob/main/LICENSE) | Linux x86_64/GCC benchmarks do not validate Windows x86/MSVC Bully. Check model licenses separately. |
| 6 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | 5,763 | Apache-2.0 (API) | Larger automation surface; feature count does not establish reliability. |
| 7 | [LING71671/open-reverselab](https://github.com/LING71671/open-reverselab) | 1,278 | GPL-3.0 (API) | Multi-tool platform; broader than a small first slice needs. |
| 8 | [HexRaysSA/ida-mcp](https://github.com/HexRaysSA/ida-mcp) | 1,269 | [MIT](https://github.com/HexRaysSA/ida-mcp/blob/main/LICENSE) | Official IDA bridge; README specifies IDA 9.4+, idalib, Python 3.11+, Git and uv. IDA licensing is separate. |
| 9 | [cyberkaida/reverse-engineering-assistant](https://github.com/cyberkaida/reverse-engineering-assistant) | 877 | Apache-2.0 (API) | Alternative Ghidra assistant. |
| 10 | [symgraph/GhidrAssistMCP](https://github.com/symgraph/GhidrAssistMCP) | 777 | MIT (API) | Native Ghidra MCP extension. |
| 11 | [symgraph/GhidrAssist](https://github.com/symgraph/GhidrAssist) | 764 | MIT (API) | Local and cloud backend options; inspect actual endpoint configuration. |
| 12 | [mahaloz/DAILA](https://github.com/mahaloz/DAILA) | 711 | [BSD-2-Clause](https://github.com/mahaloz/DAILA/blob/main/LICENSE) | DecLib/LiteLLM interface with local and remote options. |
| 13 | [radareorg/r2ai](https://github.com/radareorg/r2ai) | 489 | [MIT](https://github.com/radareorg/r2ai/blob/master/LICENSE) | radare2 language-model plugins. |
| 14 | [clearbluejar/pyghidra-mcp](https://github.com/clearbluejar/pyghidra-mcp) | 446 | Apache-2.0 (API) | Python/headless Ghidra interface. |

REA's exceptional count was checked twice by the research pass: 320,603 initially and 320,610 at approximately 20:22:41 UTC. It is retained as observed, not interpreted as independent validation. Its [CLI](https://github.com/morluto/rea/blob/main/docs/cli.md), [native-analysis](https://github.com/morluto/rea/blob/main/docs/native-investigation.md) and [security](https://github.com/morluto/rea/blob/main/SECURITY.md) documentation distinguish observations/inferences, incomplete results and analyzer security boundaries. A zero exit status can still contain unresolved evidence; the analyzer is not a sandbox.

## Static recompilers and concrete ports

| Rank | Repository | Stars | License evidence | Role and limitation |
|---:|---|---:|---|---|
| 1 | [N64Recomp/N64Recomp](https://github.com/N64Recomp/N64Recomp) | 8,265 | [MIT](https://github.com/N64Recomp/N64Recomp/blob/main/LICENSE) | N64 MIPS-to-C tool; requires runtime/metadata, not a PC/PS2 Bully translator. |
| 2 | [Zelda64Recomp/Zelda64Recomp](https://github.com/Zelda64Recomp/Zelda64Recomp) | 7,464 | GPL-3.0 (API) | Concrete Majora's Mask port and integration example. |
| 3 | [hedge-dev/XenonRecomp](https://github.com/hedge-dev/XenonRecomp) | 6,571 | [MIT](https://github.com/hedge-dev/XenonRecomp/blob/main/LICENSE.md) | Xbox 360 PPC-to-C++; no complete runtime supplied. |
| 4 | [hedge-dev/UnleashedRecomp](https://github.com/hedge-dev/UnleashedRecomp) | 5,219 | GPL-3.0 (API) | Sonic Unleashed integration; target-specific configuration. |
| 5 | [ran-j/PS2Recomp](https://github.com/ran-j/PS2Recomp) | 3,577 | [GPL-3.0](https://github.com/ran-j/PS2Recomp/blob/main/LICENSE) | Experimental R5900 translation/runtime; stripped targets need verified function maps. |
| 6 | [rexdex/recompiler](https://github.com/rexdex/recompiler) | 1,755 | MIT (API) | Historical Xbox 360-to-Windows converter; recorded latest push 2022-02-12. |
| 7 | [rexglue/rexglue-sdk](https://github.com/rexglue/rexglue-sdk) | 1,108 | [BSD-3-Clause text; API NOASSERTION](https://github.com/rexglue/rexglue-sdk/blob/main/LICENSE) | Xbox 360 runtime/toolkit with Xenia attribution. |

Translation, runtime services, graphics, audio, synchronization, saves and input require separate acceptance tests. A generated C++ file is not a playable port.

## Game reconstructions, reimplementations and ports

| Rank | Repository | Stars | License evidence | Role and limitation |
|---:|---|---:|---|---|
| 1 | [OpenRCT2/OpenRCT2](https://github.com/OpenRCT2/OpenRCT2) | 16,453 | GPL-3.0 (API) | Long-lived engine reimplementation; not a general decompiler. |
| 2 | [diasurgical/DevilutionX](https://github.com/diasurgical/DevilutionX) | 9,895 | [Sustainable Use License 1.0](https://github.com/diasurgical/DevilutionX/blob/master/LICENSE.md) | Modernized Diablo-derived port; source-available with restrictions. |
| 3 | [diasurgical/devilution](https://github.com/diasurgical/devilution) | 9,006 | [Sustainable Use License 1.0](https://github.com/diasurgical/devilution/blob/master/LICENSE.md) | Historical reconstruction/compiler lessons; not permissively reusable. |
| 4 | [n64decomp/sm64](https://github.com/n64decomp/sm64) | 8,895 | [CC0-1.0](https://github.com/n64decomp/sm64/blob/master/LICENSE.md) | Matching listed N64 targets with hashes; users provide game assets. |
| 5 | [OpenMW/openmw](https://github.com/OpenMW/openmw) | 6,645 | GPL-3.0 (API) | Compatible Morrowind engine; GitHub points to GitLab as main project. |
| 6 | [zeldaret/oot](https://github.com/zeldaret/oot) | 5,601 | No root license detected; API null | Match-oriented work in progress; not a PC port or evidence all versions are complete. |
| 7 | [k4zmu2a/SpaceCadetPinball](https://github.com/k4zmu2a/SpaceCadetPinball) | 4,713 | MIT (API) | Native-PC source-port reference; requires original resources. No whole-binary match inferred. |
| 8 | [pret/pokeemerald](https://github.com/pret/pokeemerald) | 3,607 | No root license detected; API null | GBA matching-project organization; different compiler/architecture. |
| 9 | [open-goal/jak-project](https://github.com/open-goal/jak-project) | 3,587 | [ISC](https://github.com/open-goal/jak-project/blob/master/LICENSE) | GOAL-specific recovery/compiler/runtime, not a generic PS2 C++ converter. |
| 10 | [isledecomp/isle](https://github.com/isledecomp/isle) | 3,494 | [LGPL-3.0](https://github.com/isledecomp/isle/blob/master/LICENSE) | English 1.1 LEGO Island x86/VC4.2 matching and cold-rebuild reports. |
| 11 | [scummvm/scummvm](https://github.com/scummvm/scummvm) | 2,860 | GPL-3.0 (API) | Many engine reimplementations/interpreters; architecture reference. |
| 12 | [OpenDriver2/REDRIVER2](https://github.com/OpenDriver2/REDRIVER2) | 1,414 | [MIT](https://github.com/OpenDriver2/REDRIVER2/blob/master/LICENSE) | Driver 2 port with intentional fixes/enhancements. |
| 13 | [gta-reversed/gta-reversed](https://github.com/gta-reversed/gta-reversed) | 1,090 | No root license detected; API null | Incremental GTA:SA replacement DLL; not complete standalone engine or portable Bully layouts. |
| 14 | [N0zoM1z0/dx-ball](https://github.com/N0zoM1z0/dx-ball) | 66 | MIT (API) | Small AI-assisted x86/MSVC comparison case study, still in progress. |
| 15 | [LiquidSnake0/bully-re](https://github.com/LiquidSnake0/bully-re) | 3 | [GPL-3.0](https://github.com/LiquidSnake0/bully-re/blob/main/LICENSE) | PC Scholarship Edition leads; address-reference coverage is not implementation parity. |

OpenGOAL's documented status distinguishes Jak 1 completion, Jak 2 beta and unfinished Jak 3. These are upstream labels, not results reproduced here. Likewise, LEGO Island's matching outcome applies to its documented target/toolchain, not Bully.

## Matching and project support

| Rank | Repository | Stars | License evidence | Role and limitation |
|---:|---|---:|---|---|
| 1 | [decompiler-explorer/decompiler-explorer](https://github.com/decompiler-explorer/decompiler-explorer) | 2,717 | MIT (API) | Compare analyzer outputs; use a suitable local deployment for private inputs. |
| 2 | [SubmitGame/awesome-decomp-games](https://github.com/SubmitGame/awesome-decomp-games) | 1,722 | CC0-1.0 (API) | Discovery list; verify the classification at each primary repository. |
| 3 | [decompme/decomp.me](https://github.com/decompme/decomp.me) | 633 | [MIT](https://github.com/decompme/decomp.me/blob/main/LICENSE) | Compiler/diff workbench; a public scratch discloses its content. |
| 4 | [encounter/objdiff](https://github.com/encounter/objdiff) | 600 | [MIT OR Apache-2.0](https://github.com/encounter/objdiff/blob/main/LICENSE-MIT) | Includes x86/x86_64 support but needs suitable relocatable objects. |
| 5 | [ethteck/splat](https://github.com/ethteck/splat) | 370 | [MIT](https://github.com/ethteck/splat/blob/main/LICENSE) | Binary splitting/scaffolding; check target format support. |
| 6 | [simonlindholm/decomp-permuter](https://github.com/simonlindholm/decomp-permuter) | 234 | [MIT](https://github.com/simonlindholm/decomp-permuter/blob/main/LICENSE) | MIPS/PPC/ARM32 source permutation per README; not an x86/MSVC Bully default. |
| 7 | [simonlindholm/asm-differ](https://github.com/simonlindholm/asm-differ) | 178 | Unlicense (API) | Assembly comparison; check target/configuration support. |
| 8 | [isledecomp/reccmp](https://github.com/isledecomp/reccmp) | 159 | [AGPL-3.0 (API)](https://github.com/isledecomp/reccmp/blob/master/COPYING) | Older-MSVC x86 comparison, including vtables/stack/exports; evaluate newer-toolchain support. |

Useful worked sources: [DX-Ball evidence loop](https://github.com/N0zoM1z0/dx-ball/blob/main/docs/REA.md), [DX-Ball relocation-aware matching](https://github.com/N0zoM1z0/dx-ball/blob/main/docs/MATCHING.md), [LEGO Island reproducible builds](https://github.com/isledecomp/isle/blob/master/README.md), and [reccmp](https://github.com/isledecomp/reccmp/blob/master/README.md). See [validation](validation.md) for how to apply the ideas without overstating a result.

## Additional Bully and creator-lineage sources

These supplement the ranked categories; they are not a combined leaderboard.

| Source | Stars | Observed license | Credit and use boundary |
|---|---:|---|---|
| [chasmlol/2010-rust-rewrite-mashup](https://github.com/chasmlol/2010-rust-rewrite-mashup) | 898 | Apache-2.0 root, inspect notices/dependencies | Chasm's integration work; derived from vladtrc's IW4L with a pinned SK8 component. |
| [vladtrc/iw4L](https://github.com/vladtrc/iw4L) | 1,089 | Apache-2.0 | vladtrc and contributors' original Rust MW2 runtime; behavioral reimplementation. |
| [chasmlol/iw4L](https://github.com/chasmlol/iw4L) | 17 | Apache-2.0 | Fork; preserve original-author attribution. |
| [chasmlol/skate3clone](https://github.com/chasmlol/skate3clone) | 32 | Explicitly no software license granted | Methodology citation only; no code/prose reuse. |
| [chasmlol/skate-3-trick-toolkit](https://github.com/chasmlol/skate-3-trick-toolkit) | 2 | No root license detected | Research reference pending permission for reuse. |
| [SK8-ENGINE/skate-3-rust-engine](https://github.com/SK8-ENGINE/skate-3-rust-engine) | 761 | GPL-3.0-only per README; exceptions | Credit SK8/Hailey-Ross, dumbad/Ethanw05 and the Skate community distinctly. |
| [mchughalex/skate3recomp](https://github.com/mchughalex/skate3recomp) | 1,669 | No root license detected | Static recompilation case study, no code reuse assumed. |
| [coole42-pixel/BullyRecomp](https://github.com/coole42-pixel/BullyRecomp) | 15 | MIT original work; BSD-3-Clause SDK patches | Xbox 360 case study; retail-derived code excluded. |
| [Razcoina/Bully-SE-scripts](https://github.com/Razcoina/Bully-SE-scripts) | 17 | Advertises MIT | Retail-derived Lua; uploader's license does not establish retail-script reuse rights. No scripts bundled. |
| [marcdred/bully-mact-tool](https://github.com/marcdred/bully-mact-tool) | 5 | GPL-3.0 | Bully CAT-tooling research reference. |

## Revision pins for the detailed case studies

The broader catalog contains dated metadata and moving primary-document links. The detailed method references use these observed revisions. Neither kind is a dependency lockfile; refresh evidence before implementation or reuse.

| Repository | Observed revision |
|---|---|
| chasmlol/2010-rust-rewrite-mashup | `f608f85e407ff1b7689d54a9aafdd16e95711ac4` |
| vladtrc/iw4L | `acc57a5c9dd027db8eb5ef17c792fa69f059daa1` |
| chasmlol/skate3clone | `32ba20633f445eacc65aa32459c18efbdc03c91b` |
| SK8-ENGINE/skate-3-rust-engine | `2e16697797c8358d16f747a8259354ff2921041a` |
| LiquidSnake0/bully-re | `dce485bf29117edca4d04b802a169f0a909da432` |
| coole42-pixel/BullyRecomp | `856b4cd98fb591a67b7a312c6c6b6b90da12a66e` |
| hedge-dev/XenonRecomp | `ddd128bcca99fe8bfbb99bea583c972351fa6ace` |

## Maintain the credit ledger

For each new source, record repository and exact revision, author/contributors, license file and relevant exceptions, role (reference/dependency/copied file), any modifications and retained notices. If actual implementation reuse is proposed, review it separately before adding files. Document source-available, unlicensed and retail-derived material as such; do not collapse them into an “open-source” badge.

When refreshing stars, store the observation time and API response source. When a license changes, inspect the revision actually being used. Do not silently replace a historical observation with today's value or infer permissions from a project's popularity.
