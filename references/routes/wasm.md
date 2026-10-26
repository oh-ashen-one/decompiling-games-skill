# Wasm route

Read only this selected domain and the pinned upstream documentation needed for the current question. Follow [tool-use checks](../tool-routing.md) before invoking a tool.

| Observed target / task | Primary | Justified fallback / specialist |
|---|---|---|
| WASM module/component inventory | wasm-tools | WABT for supported core modules; core sections/text request prefers WABT |
| WASM C translation / optimization / execution | wasm2c / Binaryen / compatible Wasmtime, respectively | Wasmer only after ABI/import fit. These are separate scoped tasks; **wasm-decompile was removed** and is never auto-selected |

For source/license details, query `scripts/catalog_lookup.py --section <section>` for section 10, or use a specific tool name with `--query`. Do not load the full catalog.
