# Choose the reconstruction goal

These terms describe different objectives. Choose before selecting tools or measuring success.

| Goal | Work product | Evidence of success | Common mistaken claim |
|---|---|---|---|
| Binary analysis | Annotated functions, types, data relationships and uncertainty | Reproducible evidence tied to a fingerprinted binary | Named functions equal recovered source |
| Matching decompilation | Source that recompiles to a specified binary target | Reproducible compiler/linker setup and explicitly defined byte or object matching | Similar output or gameplay proves a match |
| Behavioral reimplementation | New code realizing an observed contract | Controlled differential tests and stated coverage | Original source has been recovered |
| Static recompilation | Ahead-of-time translation plus supporting runtime | Correct target translation, runtime integration and behavior tests | A translator supplies a complete portable game |
| Asset extraction/conversion | Decoded or transformed data | Format correctness and controlled visual/data checks | A rendered map proves gameplay parity |

“Native” describes how a resulting program executes on its host. A new native engine and a statically recompiled native executable can have very different provenance and validation requirements.

## Target fingerprint

Keep a private target record containing title, edition, platform, region, executable hash algorithm and digest, patch/title update, file format, ISA, endianness, pointer width, ABI/calling conventions, image base and loader options. Record compiler/linker evidence if available; mark unknowns rather than guessing. Record the host and reference execution environment separately.

An address is meaningful only with its binary fingerprint and addressing convention. A model must not reuse another edition's vtables, offsets or pool layouts without evidence. Derived datasets should carry the same fingerprint so a stale database cannot silently contaminate a new analysis.

## Select a first experiment

Prefer a narrow behavior with a reliable observation path and inexpensive tests. A parser with synthetic malformed fixtures, a deterministic transform or a handle validator is easier to falsify than an entire animation or physics system. Write the expected observations and failure conditions first.

If your actual goal is a new game inspired by a reference, use an ordinary game-development workflow. If you need only modding hooks or a file converter, limit the scope accordingly. A full engine reconstruction is not an automatic prerequisite.

## Keep method and rights distinct

Reference a method without importing its implementation. If code is copied or adapted, record the exact files, upstream revision, applicable license, modifications and notices. Mixed-license repositories require file-level inspection. A root MIT or Apache badge does not establish ownership of included retail-derived material.

For a proposed clean-room process, define information flow, roles and enforcement explicitly. Two model sessions sharing the same decompiler output are not independent implementations. This guide makes no legal certification of a clean-room process.
