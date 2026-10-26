# Javascript route

Read only this selected domain and the pinned upstream documentation needed for the current question. Follow [tool-use checks](../tool-routing.md) before invoking a tool.

| Observed target / task | Primary | Justified fallback / specialist |
|---|---|---|
| Electron ASAR | electron/asar listing and bounded extraction, then source/IPC graph | REA JS graph, matching source maps/AST parser; CDP only for authorized observation |
| JS source / bundles | Babel parser with correct syntax plugins | Acorn for supported syntax; Esprima for its supported dialect. Beautifier formats, source maps map existing evidence |

For source/license details, query `scripts/catalog_lookup.py --section <section>` for section 07, or use a specific tool name with `--query`. Do not load the full catalog.
