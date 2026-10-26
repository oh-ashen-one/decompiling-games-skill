# Keep the game-specific route

The general catalog supplements these workflows; it does not flatten every task into a generic decompiler. Read the current project's instructions, handoff, exact-build checks, loader support and tests first. A source audit or saved reference does not resume a paused project. Never touch another session's installation, saves, engines or render jobs.

## Bully

Keep [the Bully workflow](bully-workflow.md), [creator methods](creator-methods.md) and [existing source catalog](source-catalog.md). Verified PC Scholarship Edition → `LiquidSnake0/bully-re` for build-specific leads and REA/Ghidra for native evidence; the reference project's GPL obligations remain separate. Xbox 360 Scholarship Edition → the distinct `coole42-pixel/BullyRecomp`, `hedge-dev/XenonRecomp` and `rexglue/rexglue-sdk` research route after XEX/PPC/build/metadata verification. Neither translates a PC executable automatically. Retain N64/PS2 recompilation and matching-tool references for their supported targets, not as Bully-PC fallbacks.

## Unity

Verified CLI/IL assemblies in a Unity Mono build → [ILSpy](https://github.com/icsharpcode/ILSpy); Windows runtime debugging → [dnSpyEx](https://github.com/dnSpyEx/dnSpy). Verify the assembly contents, not just `Assembly-CSharp.dll` names. IL2CPP-generated dummy assemblies are not proof of Mono.

Verified IL2CPP native binary plus matching global metadata/registration/version evidence → [SamboyCoding/Cpp2IL](https://github.com/SamboyCoding/Cpp2IL) (MIT license inspected 2026-10-26). It is work in progress; metadata recovery, method signatures and partially recovered IL are distinct outcomes. Use Ghidra for unresolved native semantics, optionally ILSpy for recovered assembly inspection. Keep existing import/build/asset pipelines and tests. Harmony is a managed-runtime patching library, not a universal IL2CPP hook.

## New Vegas

For an engine-reimplementation question, first inspect [slaterain/nv-rs](https://github.com/slaterain/nv-rs), exact target/version, `LEGAL.md`, project handoff and behavioral/oracle tests. For a supported native mod, prefer the project's verified SDK/loader path instead. Native unknowns still use REA/Ghidra.

The 2026-10-26 README and root LICENSE show GPLv3; older listings described MIT/Apache. Verify the exact revision and license before reusing anything. It is experimental: partial playable reports, translation/function counts and claimed parity are upstream reports, not this skill's test evidence. It is not a drop-in engine for another game, and original save/NVSE compatibility must be independently established.

## DS1, DSR and MW2

Keep original Dark Souls separate from Dark Souls Remastered, and MW2 (2009) separate from later titles. The known [oh-ashen-one/dsr-mw2-crossover](https://github.com/oh-ashen-one/dsr-mw2-crossover) is the specific DSR/MW2 source-release reference. Its audited default branch is `release/v0.2.0`; README directs to `AGENTS.md`, `SKILL.md`, `HANDOFF.md`, `docs/SETUP.md` and `docs/STATUS.md`. Its root LICENSE is GPLv3; inspect per-file and dependency notices. The documented M3 Ultra/macOS/CrossOver setup and exact native hashes are not generic DS1/native-Windows support. Read current owner tests and unresolved issues before repeating claims. No project files or game targets were changed by this catalog update.

For a new mashup architecture, read [universal-modder's mashup workflow](https://github.com/rehan-remade/universal-modder/blob/main/skills/mashup-mods/SKILL.md) and its linked route/prior-project/bridge-contract/loader references. The repository advertises MIT; dependency and asset rights remain separate. Reuse guidance selectively; do not inherit paid fal generation, API-key setup, automatic publishing or tool installation. An installed supported modding SDK/loader should precede new reverse engineering.

Distinguish content port, state exchange between two runtimes, composited render output, embedded rebuilt runtime and native behavior mod. Record input/camera/collision/damage/inventory ownership, units/axes/time, versioned channels, stale-message handling and restart semantics. Prove original games and loader baselines, then one input-to-gameplay loop. Test equip/unequip, reload/damage, death/respawn, save/load, both-process disconnect/restart and rollback. Capture actual native input and gameplay evidence; launcher success and a screenshot do not prove mechanics.

For MW2 runtime-reimplementation lineage keep [vladtrc/iw4L](https://github.com/vladtrc/iw4L) and Chasm's integration references from the existing catalog. Preserve original-author attribution and the distinction between Apache-licensed code, GPL components and unlicensed/retail-derived materials.

## Movement and combat

[tnrjns/faith-runner](https://github.com/tnrjns/faith-runner) (MIT license inspected) is a Mirror's Edge-style movement reference with a separate controller crate. [Funny-Bones/ELDEN-RING-Combat-Rewrite](https://github.com/Funny-Bones/ELDEN-RING-Combat-Rewrite) is a Bevy player-movement/combat sandbox using data derived locally from an owned game. Its `LICENSE.md` was inspected and states MIT; the extensionless `LICENSE` path is absent. Preserve notices and inspect the chosen revision before code reuse. Neither proves integration into a different native host. Use exact-state behavioral tests, collision/timing tests and real in-game evidence, not only a sandbox recording.

## PS5

[boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) and [ymatrix1/PortPS5](https://github.com/ymatrix1/PortPS5) are GPL-2.0-only according to their inspected READMEs. They are distinct interoperability research paths; PortPS5 is Windows-focused, while an AnyPS5 relinker building on macOS does not establish macOS gameplay. Check title-specific reports, architecture/graphics dependencies and lawful input provenance. Already-decrypted lawful inputs do not authorize decryption, DRM/security bypass, key acquisition or firmware distribution. No universal AAA-port or successful-gameplay claim follows from relinking.

## Supplemental source audit boundary

These preserve specialized prior guidance and are separate from the 114 user-toolkit mentions. Primary repository identity/README and the license surfaces noted above were checked 2026-10-26. No upstream implementation or skill text was vendored; these are original summaries and links. No referenced game build, hook, translation or gameplay result was executed or independently reproduced in this documentation update.
