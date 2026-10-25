# Default toolchain: REA and Ghidra

Owner decision, **2026-10-25**: for any question that depends on a shipped game binary, use **REA** ([morluto/rea](https://github.com/morluto/rea), MIT) as the agent-facing analysis interface and **Ghidra** ([NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra), Apache-2.0) as the native analysis engine. Their own skills and documentation are more detailed than this one about tool mechanics, so follow them for that. This skill still governs scope, privacy, evidence and publication.

| Question | Authority |
|---|---|
| Which REA tool to call, connection recovery, provider setup, Evidence interpretation | REA's bundled `reverse-engineer-anything` skill and [docs](https://github.com/morluto/rea/tree/main/docs) for the installed release |
| Ghidra installation, headless analysis, scripting, project format | Ghidra's official documentation for the installed release |
| Target identity, private-material boundary, validation, publication, credits | This skill |

When these conflict on scope or disclosure, the stricter rule wins.

## Use stronger upstream skills first

Owner direction, 2026-10-25: when a well-known skill covers a step better than this one, load it and follow it. This skill then adds only the game-specific scope, privacy and validation rules. Vetted on 2026-10-25 from each repository's README, skill file and license:

| Step | Skill to load | Why |
|---|---|---|
| Any REA call, tool routing, recovery | REA's `reverse-engineer-anything` (bundled with `rea-agents`; installed by `rea setup` to `~/.agents/skills/`) | Written by REA's maintainers and matched to the installed release's tools |
| Iterative Ghidra work on a game binary: annotation rounds, avoiding self-corroboration, game-specific evidence sweeps | [GeReV/ghidra-iterative-re](https://github.com/GeReV/ghidra-iterative-re) `SKILL.md`, MIT | Deepest on MSVC x86 PE and C++ class recovery, which matches PC Bully. It is explicitly work in progress, so re-read its current revision rather than caching rules. |
| Ghidra scripting, headless options, project format | Ghidra's bundled `docs/` and `support/analyzeHeadlessREADME.md` for the installed release | Authoritative and version-matched |

Not adopted as defaults: `zhaoxuya520/reverse-skill` (popular, but broad pentest-oriented routing), `EncidXVII/claude-reverse-engineering-skill` (no clear license) and GUI-bound Ghidra MCP bridges (attended only, see below). Re-vet before switching. Popularity is not correctness, and a new revision can change scope.

## Choose the tool

| Situation | Use |
|---|---|
| Targeted question about a binary: find a function, follow callers or xrefs, decompile one function, inspect strings, data types or a function dossier | **REA over MCP**, Ghidra provider. This is the default for interactive investigation. |
| First analysis of a new executable; batch exports (e.g. every Lua binding registration, every string reference to a format); persistent database edits | **Ghidra headless** (`analyzeHeadless` or PyGhidra) into a project cached by executable hash. REA's annotations are session-only and are discarded on close. |
| REA lacks a needed operation, or the owner is present and wants to inspect interactively | **Ghidra GUI**, attended only. A GUI bridge such as [LaurieWired/GhidraMCP](https://github.com/LaurieWired/GhidraMCP) opens an HTTP listener (default `127.0.0.1:8080`). Use it only with prior owner approval of that listener and never during unattended runs. |
| Question answerable from already-decompiled scripts, decoded file formats or a public project's notes | **Neither.** Use ordinary repository tools; REA's own skill says to skip it for source-level analysis. |
| Iterative Ghidra annotation discipline for MSVC x86 PE (class layouts, avoiding self-corroboration) | Read [GeReV/ghidra-iterative-re](https://github.com/GeReV/ghidra-iterative-re) (MIT, explicitly work in progress) as a method reference, not an authority. |

Pick one interface per question. Running several AI bridges against the same project at once makes failures and disclosure boundaries hard to diagnose.

## Install and connect

Install only with the owner's approval of each step. Verify current official instructions first; the versions below were checked on 2026-10-25.

1. **JDK 21+, host-native.** REA rejects a JDK running under emulation, for example x86_64 under Rosetta on Apple silicon. On macOS arm64, use an arm64 JDK 21 and select it with `JAVA_HOME`.
2. **Ghidra 12.1.x.** REA 6.7 accepts Ghidra 12.1.x only and is verified with **12.1.4 + JDK 21**. Do not move to 12.2 until the installed REA release documents support for it. Extract the official release outside any repository. The native decompiler for the host must be present in `Ghidra/Features/Decompiler/os/<platform>/` or `build/os/<platform>/`. **Official releases ship no macOS binaries.** On a Mac, build them with `cd <ghidra>/support/gradle && JAVA_HOME=<jdk21> gradle buildNatives`, which needs Gradle 8.5+ and Xcode or its Command Line Tools; this was verified on the Studio on 2026-10-25. A local build carries no quarantine attribute. REA does not change Gatekeeper quarantine; clearing it is a separate owner decision.
3. **REA, version-pinned.** Choose a `rea-agents` release published at least seven days earlier, per house supply-chain policy. For example, use 6.7.0 (2026-10-18), not 6.8.0 (published 2026-10-25). Use `npx -y rea-agents@<version>` in place of `@latest` in every command REA's skill shows.
4. **Diagnose read-only:** `npx -y rea-agents@<version> doctor --client <client> --json`. Client ids include `devin`, `claude_code`, `codex` and `cursor`.
5. **Plan, review, apply.** Run `setup --client <client> --dry-run --json`, then show the owner the exact config paths, backups and skill replacement. After approval, apply the same scope with `--yes`. Never add `--install-hopper` unless that separate install was approved.
6. **Restart the agent** and confirm that REA tools appear in the session before claiming the connection works.

REA setup never installs Java or Ghidra; install those first. Its Ghidra adapter runs locally as a stdio process. Recheck for listening ports after any upgrade anyway, because macOS firewall prompts stall unattended runs.

## Privacy boundary

The analyzer runs locally, but a cloud-hosted agent receives every tool response it reads; see [local and cloud models](local-cloud.md). Before a cloud agent queries REA or Ghidra on a retail executable, obtain the owner's permission for that target and that destination. Then:

- Keep Ghidra projects, headless exports and REA evidence in a local research directory outside every repository, for example `<research-root>/ghidra/<sha256-of-executable>/`.
- Request bounded results (one function, one xref set), not whole-program dumps.
- Publish only independently written behavior descriptions and original code. Never publish raw pseudocode, disassembly, exports or databases.

## Evidence

- Record the executable hash, Ghidra version, JDK, REA version, provider and analysis options with every finding.
- REA returns Evidence with limitations and unknowns. Carry the unknowns into the behavior contract rather than dropping them. A successful call can still be incomplete.
- For PE targets, REA reports load-image measurements with an *unsupported* attestation status. Treat those addresses as measured, not attested.
- Decompiler types and names are hypotheses until layout, call evidence or observed behavior supports them (see [validation](validation.md)).
