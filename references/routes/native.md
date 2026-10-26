# Native route

Read only this selected domain and the pinned upstream documentation needed for the current question. Follow [tool-use checks](../tool-routing.md) before invoking a tool.

| Observed target / task | Primary | Justified fallback / specialist |
|---|---|---|
| Native PE/ELF/Mach-O, bounded interactive analysis | Existing compatible REA + Ghidra provider | Headless Ghidra directly; established radare2 CLI/one official MCP if its loader fits |
| Whole-program import, persistent annotations, batch export | Headless Ghidra | REA for supported bounded queries; radare2 for established CLI batch workflows |
| Licensed, established IDA project | Keep compatible IDA; prefer official HexRaysSA/ida-mcp after version/license check | Existing mrexodia bridge only if supported; Ghidra when no suitable IDA entitlement. Free wrapper is not free IDA |

For source/license details, query `scripts/catalog_lookup.py --section <section>` for section 03 or 04, or use a specific tool name with `--query`. Do not load the full catalog.

When REA/Ghidra is selected, read [its pinned setup/privacy guidance](../rea-and-ghidra.md). Keep the stronger installed upstream skill for tool mechanics.
