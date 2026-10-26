# Runtime route

Read only this selected domain and the pinned upstream documentation needed for the current question. Follow [tool-use checks](../tool-routing.md) before invoking a tool.

| Observed target / task | Primary | Justified fallback / specialist |
|---|---|---|
| Native runtime observation | PE → x32dbg/x64dbg on Windows; ELF → GDB; Mach-O → LLDB | LLDB for supported ELF targets. Require owned process, matching host/target and attach permission |
| Capture, protocol fuzzing, binary/runtime patch | Explicit bounded specialist plan | tcpdump, boofuzz, Harmony/assembler only when separately scoped; never an automatic fallback from static analysis |

For source/license details, query `scripts/catalog_lookup.py --section <section>` for section 04, 05, 06 or 11, or use a specific tool name with `--query`. Do not load the full catalog.
