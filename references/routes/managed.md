# Managed route

Read only this selected domain and the pinned upstream documentation needed for the current question. Follow [tool-use checks](../tool-routing.md) before invoking a tool.

| Observed target / task | Primary | Justified fallback / specialist |
|---|---|---|
| Managed PE/CLI (.NET / Unity Mono) | ILSpy / ILSpy CLI | dnSpyEx on Windows when runtime debugging or assembly editing is actually required |
| Unity IL2CPP | Version-compatible Cpp2IL using native binary and matching metadata | Ghidra native analysis; ILSpy may inspect recovered assemblies, but dummy signatures do not prove recovered method behavior |
| .NET NativeAOT | Native Ghidra route, optional Washi1337/ghidra-nativeaot helper | Manual native analysis; ILSpy is not an AOT machine-code decompiler |

For source/license details, query `scripts/catalog_lookup.py --section <section>` for section 05, or use a specific tool name with `--query`. Do not load the full catalog.

For Unity, read [the Unity profile](../games/unity.md). NativeAOT follows native analysis plus a version-compatible helper, not ordinary managed-DLL decompilation.
