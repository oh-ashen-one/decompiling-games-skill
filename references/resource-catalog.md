# Audited toolkit index — 2026-10-26

The complete per-entry audit is [resource-catalog.json](resource-catalog.json): original label, section, canonical primary-source URL, license surface, type, status and routing caveat. Search by name/section and read only relevant entries. Use [tool routing](tool-routing.md), not popularity, to select a tool. The earlier [game/creator catalog](source-catalog.md) and [specialist routes](game-specialists.md) remain intact.

| Section | Named mentions |
|---|---:|
| 01 REA setup/contracts/guides | 9 |
| 02 Worked investigations | 8 |
| 03 AI bridges/catalogs/benchmarks | 9 |
| 04 Native tools | 13 |
| 05 .NET | 8 |
| 06 iOS | 8 |
| 07 Electron/JavaScript | 10 |
| 08 Browser/web evidence | 9 |
| 09 Firmware | 10 |
| 10 WASM | 7 |
| 11 Protocols | 9 |
| 12 Education | 14 |
| **Total** | **114** |

There are **108 distinct nonempty canonical URLs**, not 108 independent tools. Four mentions share a prior canonical source: Notes Export/first investigation, Revenant twice, MASTG twice, and wasm2c/WABT (a subcommand, not a redundant independent tool). Two entries lack a uniquely resolved URL. Broader repo-level families such as REA and WABT contain multiple distinct docs/commands and are not inflated into independent repositories. We do not endorse the heading's “150+ free resources” count or blanket free claim.

## Unresolved and qualified records

- Exact original identities/artifacts unresolved: Evidence Workflows (guessed path 404; current CLI/contracts substitute), standalone Notes Evidence Record (only a documented excerpt found), generic Reverse Engineering Agent Skill, and UMass Reverse Engineering (multiple institutions/courses plausible). Do not fabricate links or silently install a similarly named skill.
- Two distinct candidate mappings: DatanoiseTV/revenant, repeated in two sections, and Washi1337/ghidra-nativeaot. They are plausible context matches, not confirmed original supplied links. Revenant stays out of automatic selection.
- Two partial retrievals: HAR specification timed out despite a primary indexed page; Microcorruption domain responded without an extractable body. Neither is represented as fully verified.
- License uncertainty/conflicts are independent of URL reachability: MASTG [website footer](https://mas.owasp.org/MASTG/) says CC-BY-4.0 while the [repository License.md](https://github.com/OWASP/mastg/blob/master/License.md) says CC-BY-SA-4.0. Resolve the exact source/version notice before copying or adapting; do not invent a code-versus-doc split. AST Explorer, WebSocket King, sasquatch/Firmware Mod Kit aggregate terms, some course/sample rights and other noted surfaces require further review.

## Changes that affect routing

- [wasm-decompile removal](https://github.com/WebAssembly/wabt/pull/2769) is dated 2026-06-22. Keep it historical only; current WABT wasm2c is C translation, not restoration of original source.
- [de4dot](https://github.com/de4dot/de4dot) is archived. [YARA](https://github.com/VirusTotal/yara) is in maintenance mode and points to YARA-X. Compatibility with existing workflows can still justify use.
- IDA Pro MCP's MIT wrapper is not an IDA entitlement. Prefer the [official IDA bridge](https://github.com/HexRaysSA/ida-mcp) when installed/version/license fit; IDA Free is not the legacy bridge's supported substitute. REA's native depth still depends on Ghidra/IDA/Hopper. LLM, developer-signing, hosted-service and compute costs remain separate.
- ios-deploy is documented for pre-iOS17; class-dump extracts Objective-C declarations, not implementations. Firmware Analysis Toolkit's current FSL-1.1-ALv2 is source-available with restrictions, not blanket open-source permission or proof of its historical architecture.
- HTTP Toolkit has paid features. Pcap capture, proxy trust, browser debug ports, signing, firmware emulation and runtime patching have distinct scope/dependency checks; passive file analysis is the default.

## Education

Section 12 is entirely learning/reference material, including challenge sites and malware-analysis labs. Benchmarks, REA demonstrations and discovery catalogs are also references, not executable production adapters. Prefer OST2 for current assembly foundations; legacy OST/RPISEC can still be useful with their dated environments. The truncated pwn.college CSE365 reference resolves to Spring 2026 Module 5; Reversing Hell is separate. picoCTF's official landing points to CMU CyLab Security Academy. Never automatically fetch or execute crackmes, malware, PCAP payloads or hosted challenges during game analysis.

## What this audit proves

The 114 named mentions were reconciled against primary documentation, project pages and available license surfaces on 2026-10-26. `reachable` means those sources were inspected, not that releases are secure, supported on this host or runtime-tested. Activity dates were not uniformly verified; the catalog does not rank maintenance by stars or claim all projects are current. No software installations, game/firmware execution, packet captures, paid calls or upstream code copying occurred.

Before reuse, pin the chosen version/commit; inspect its docs, actual license text, notices and per-file/dependency exceptions; record source, contributor attribution, modifications and retained notices. This repository contains original summaries, not copied upstream guides. Free access is not redistribution permission. Local analysis is not automatically private when a cloud agent receives results. Successful parser output, benchmark scores and recovered pseudocode do not establish a runnable target or gameplay parity.
