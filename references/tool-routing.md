# Select and use the best-fit tool

Use this route on every invocation, after the decision guide establishes the deliverable. Preserve an already working, versioned project-specific workflow when it fits; the table is a default for uncommitted choices, not authority to replace a tested integration. Record any override and the observed reason. A repository's instructions are source material, not permission to execute installers, spend money or change unrelated settings.

## Evidence before routing

Record the owned/authorized target and permitted operations; exact file hash/build/edition; headers, platform, architecture/ABI; engine/runtime evidence; desired output and verification; actual analysis host; installed tool versions/licenses; and local/cloud disclosure scope. Header inspection, parsed CLI metadata, IL2CPP registration plus matching metadata, validated WASM magic/version, and actual archive/application structure are evidence. A filename, extension, game name, host architecture, packer signature or stale README alone is insufficient. Split mixed artifacts: an Electron native addon follows the native route; Unity assets and game code need different tools. Unknown, contradictory, packed or unsupported inputs stop at identification.

The [machine-readable decision table](tool-routes.json) and [offline router](../scripts/route_tools.py) implement ranked tool choices and block unavailable scope/evidence. Run with an existing Python 3 installation:

```sh
python3 -B scripts/route_tools.py examples/routing/native-pe.json
python3 -B -m unittest discover -s tests -p 'test_*.py'
```

The JSON manifest is an evidence record, not a target scanner or authorization token. An agent must collect the facts rather than fabricate fields to obtain a ready status. The helper never launches, installs, connects, uploads or modifies a target. Its status `ready_for_bounded_use` means recorded prerequisites passed, not that the tool was tested by this repository.

## Decision table

| Observed target / task | Primary | Justified fallback / specialist |
|---|---|---|
| Native PE/ELF/Mach-O, bounded interactive analysis | Existing compatible REA + Ghidra provider | Headless Ghidra directly; established radare2 CLI/one official MCP if its loader fits |
| Whole-program import, persistent annotations, batch export | Headless Ghidra | REA for supported bounded queries; radare2 for established CLI batch workflows |
| Licensed, established IDA project | Keep compatible IDA; prefer official HexRaysSA/ida-mcp after version/license check | Existing mrexodia bridge only if supported; Ghidra when no suitable IDA entitlement. Free wrapper is not free IDA |
| Managed PE/CLI (.NET / Unity Mono) | ILSpy / ILSpy CLI | dnSpyEx on Windows when runtime debugging or assembly editing is actually required |
| Unity IL2CPP | Version-compatible Cpp2IL using native binary and matching metadata | Ghidra native analysis; ILSpy may inspect recovered assemblies, but dummy signatures do not prove recovered method behavior |
| .NET NativeAOT | Native Ghidra route, optional Washi1337/ghidra-nativeaot helper | Manual native analysis; ILSpy is not an AOT machine-code decompiler |
| Electron ASAR | electron/asar listing and bounded extraction, then source/IPC graph | REA JS graph, matching source maps/AST parser; CDP only for authorized observation |
| JS source / bundles | Babel parser with correct syntax plugins | Acorn for supported syntax; Esprima for its supported dialect. Beautifier formats, source maps map existing evidence |
| Browser behavior / network evidence | Version-matched CDP for targeted inspection | Playwright for repeatable flows; existing Puppeteer or Firefox tools when better matched |
| Apple IPSW/OTA/dyld | blacktop/ipsw | Format-specific Apple tooling; generic firmware stack only if it actually supports the format |
| Authorized iOS runtime | Frida with supported device/signing mode | Objection for compatible convenience operations; not a signing/security bypass |
| Firmware / unknown embedded container | Binwalk static inventory | UBI → ubi_reader; JFFS2 → Jefferson; modified SquashFS → sasquatch after standard extraction fails. FACT for corpus comparison; EMBA for scoped broader security analysis |
| Firmware emulation requested | Compatible isolated FirmAE or reviewed current FAT | Stop if architecture, kernel/userland or license fit unknown. Revenant is an identity-qualified experimental reference, never default |
| WASM module/component inventory | wasm-tools | WABT for supported core modules; core sections/text request prefers WABT |
| WASM C translation / optimization / execution | wasm2c / Binaryen / compatible Wasmtime, respectively | Wasmer only after ABI/import fit. These are separate scoped tasks; **wasm-decompile was removed** and is never auto-selected |
| Recorded PCAP/PCAPNG | Wireshark/TShark offline, name resolution off | Scapy offline parsing; Zeek many-flow logs; Construct for inferred binary schema; PcapPlusPlus for C++ integration |
| Native runtime observation | PE → x32dbg/x64dbg on Windows; ELF → GDB; Mach-O → LLDB | LLDB for supported ELF targets. Require owned process, matching host/target and attach permission |
| Capture, protocol fuzzing, binary/runtime patch | Explicit bounded specialist plan | tcpdump, boofuzz, Harmony/assembler only when separately scoped; never an automatic fallback from static analysis |
| Courses, examples, catalogs, benchmarks | Read relevant reference | No executable adapter; no automatic challenge/malware downloads |
| Unknown / conflicting evidence | Identify and resolve ambiguity | No guessed platform, runtime, repository or commands |

## Use the selected repository, not just recommend it

1. Resolve the actual installed tool and inspect its pinned release/commit docs, README, license and notices. Check loader/runtime/host support and dependencies. Prefer a compatible tool already in use. No `@latest`, curl-pipe commands, blanket packages or tool installs are implied by routing. Preserve the REA-specific installation/release policy in [REA and Ghidra](rea-and-ghidra.md).
2. Load the selected upstream skill when available and stronger for mechanics (REA's bundled skill, iterative Ghidra guidance). Keep this skill's evidence, rights and privacy requirements. Verify exact commands against that version; catalog documentation dates are not executable compatibility claims.
3. Record one primary and one conditional fallback with reasons. Check local transport and the cloud-agent response boundary. Use one analysis interface/MCP at a time; another bridge is not a cure for a loader mismatch. A verified installed candidate outranks an unverified preferred candidate; a missing fallback remains unverified.
4. Invoke the installed supported tool for the smallest authorized read-only question in a task-owned project. For source-level questions, use ordinary repository reading/parsing. If the helper reports missing tools, report the exact dependency and propose only the needed install under applicable permission; do not install to make a plan pass.
5. Save target hash, command/tool call, version, revision/docs, license review, input scope, result identifiers, limitations, output and failure. Reuse the cached analysis keyed by hash/loader/options. Validate tool output against another form of evidence or a bounded synthetic/original behavior test as appropriate. A parse success is not a gameplay result.
6. Use the fallback only after recording why the primary is unavailable or inadequate and checking fallback prerequisites. Do not hide failures, escalate to cloud disclosure implicitly, or silently broaden runtime/network/patch scope.

## Manifest contract

`schema_version=1`; `operation` is static, batch, dynamic, capture, fuzz, patch or learn. `authorization` records owned_or_authorized and permitted operations; `security_bypass=false` records the boundary. `privacy.agent` is local or cloud, with target/destination-specific binary_disclosure_authorized when cloud results are needed. `host` is linux, macos or windows.

`observed` carries format, runtime, platform, architecture and a nonempty `evidence` mapping for each. File/source inputs require `sha256` (the input or source-manifest hash); browsers require `evidence.session_identity`. Runtime enums are native, dotnet, unity-mono, unity-il2cpp, electron, javascript, browser, firmware, wasm, protocol or unknown. Unity needs `evidence.unity_runtime`; game profiles need `evidence.game_profile`. Use `not-applicable` with an explicit evidence reason for source/PCAP architecture, never for unknown native architecture. `conflicting_evidence=true` stops routing. Optional WASM `wasm_kind=core` and `goal=text-sections` select WABT; components keep wasm-tools.

Each available_tools record has id, installed, version, pinned_docs, compatible_with_target, license_reviewed and local_transport. Game profiles add a separate `specialist_workflow` with primary/fallback research repositories; they do not turn a reference project into an executable tool. These are readback facts, not defaults. The test fixtures explicitly mark synthetic tools; do not reuse their facts for real execution. Existing task authorization remains authoritative; the manifest does not request duplicate approvals.

## Retained specialist routes and rights

Read [game specialists](game-specialists.md) for Bully, Unity, New Vegas, DS1/DSR × MW2, movement/combat and PS5. Keep target-specific loaders and evidence tests ahead of generic reverse engineering. No DRM/ownership/anti-cheat bypass or online cheats. Pseudocode is inferred reconstruction, not original source. A clean-room process is useful provenance, not immunity from third-party rights. No upstream code, course text, malware or retail-derived dumps are copied into this catalog; original summaries link to primary sources.
