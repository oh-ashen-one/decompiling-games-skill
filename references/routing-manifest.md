# Optional offline routing manifest

Read only when preparing input for `python3 -B scripts/route_tools.py <manifest.json>`. It selects a plan and executes no external tools. The input is an evidence record, not a scanner or authorization token; never fabricate facts to obtain ready status.

`schema_version=1`; `operation` is static, batch, dynamic, capture, fuzz, patch or learn. `authorization` records owned_or_authorized and permitted operations; `security_bypass=false` records the boundary. `privacy.agent` is local or cloud, with target/destination-specific binary_disclosure_authorized when cloud results are needed. `host` is linux, macos or windows.

`observed` carries format, runtime, platform, architecture and a nonempty `evidence` mapping for each. File/source inputs require `sha256` (the input or source-manifest hash); browsers require `evidence.session_identity`. Runtime enums are native, dotnet, unity-mono, unity-il2cpp, electron, javascript, browser, firmware, wasm, protocol or unknown. Unity needs `evidence.unity_runtime`; game profiles need `evidence.game_profile`. Use `not-applicable` with an explicit evidence reason for source/PCAP architecture, never for unknown native architecture. `conflicting_evidence=true` stops routing. Optional WASM `wasm_kind=core` and `goal=text-sections` select WABT; components keep wasm-tools.

Each available_tools record has id, installed, version, pinned_docs, compatible_with_target, license_reviewed and local_transport. Game profiles add a separate `specialist_workflow` with primary/fallback research repositories; they do not turn a reference project into an executable tool. These are readback facts, not defaults. The test fixtures explicitly mark synthetic tools; do not reuse their facts for real execution. Existing task authorization remains authoritative; the manifest does not request duplicate approvals.


The [decision JSON](tool-routes.json) is implementation data for the helper; do not dump it into context. The output includes only selected tools, requirements, reasons and relevant references. `ready_for_bounded_use` means recorded prerequisites passed, not compatibility tested by this repository.
