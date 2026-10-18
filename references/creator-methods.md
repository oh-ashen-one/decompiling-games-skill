# Attributed methods from IW4L and Skate research

This reference synthesizes methods in original language. It contains no upstream source code or copied skill instructions. Research snapshot: 2026-10-18 UTC.

## Identity and distinct contributions

The strongest match to the description “IW4 and Skate 3” is **Chasm / chasmlol**: [2010-rust-rewrite-mashup](https://github.com/chasmlol/2010-rust-rewrite-mashup) combines IW4L, Skate 3 and Minecraft. Its [NOTICE](https://github.com/chasmlol/2010-rust-rewrite-mashup/blob/f608f85e407ff1b7689d54a9aafdd16e95711ac4/NOTICE) credits chasmlol's fork and vladtrc's original IW4L work. No primary source in this research establishes “Kazem” as Chasm's name or alias.

Credit these contributions separately:

- **vladtrc and IW4L contributors:** the original Rust/Bevy/wgpu MW2 runtime and its supporting research.
- **chasmlol / Chasm:** the mashup and separate Skate reconstruction/preservation projects.
- **dumbad / Ethanw05 and the Skate modding community:** underlying format, mesh, map, collision, animation and interaction research acknowledged in [SK8's history](https://github.com/SK8-ENGINE/skate-3-rust-engine/blob/2e16697797c8358d16f747a8259354ff2921041a/README.md).
- **SK8-ENGINE contributors and Hailey-Ross:** Rust engine development, research hooks and tracing documentation.
- **mchughalex, ReXGlue/Tom Clay, Xenia and XenonRecomp contributors:** distinct static-recompilation and runtime work. Do not merge these into a single author's contribution.
- **LiquidSnake0 and Bully tooling authors:** Bully-specific format and binary research.

## Reimplementation with subsystem boundaries

[IW4L's README](https://github.com/vladtrc/iw4L/blob/acc57a5c9dd027db8eb5ef17c792fa69f059daa1/README.md) describes asset readers, an intermediate representation, shader translation and a shared simulation step. Its account of LLM-written code does not establish matching decompilation or complete gameplay.

The mashup's [Skate guide](https://github.com/chasmlol/2010-rust-rewrite-mashup/blob/f608f85e407ff1b7689d54a9aafdd16e95711ac4/docs/SKATE.md) describes a pinned SK8 component, a separately bounded skating simulation, collision transfer, derived grind rails and skeleton retargeting. The reusable lesson is to define explicit data and simulation interfaces before joining systems. Reusing an interface idea is distinct from importing its licensed implementation.

For Bully, apply that lesson to a narrowly scoped loader, animation interface or state machine. First define coordinate systems, ownership, event order and error behavior. A visually convincing integration still needs behavioral tests.

## Research before implementation

The [SK8 research skill](https://github.com/SK8-ENGINE/skate-3-rust-engine/blob/2e16697797c8358d16f747a8259354ff2921041a/tools/claude-skills/recomp-research/SKILL.md) motivates a useful evidence cycle: locate the relevant behavior, verify the feature exists, instrument only the necessary path, capture controlled observations, formulate a contract, then test a new implementation against it.

For a new workflow, make the observations auditable. Confirm hook activation; identify build and schema versions; limit logging; distinguish measured values from inferred types; and keep uncertainty attached to each claim. [SK8's trace documentation](https://github.com/SK8-ENGINE/skate-3-rust-engine/blob/2e16697797c8358d16f747a8259354ff2921041a/tools/recomp-trace/README.md) notes that recompilation changes timing/threading. A logic trace therefore cannot automatically certify original-console timing.

## Paired observations

The unlicensed skate3clone [dual-oracle discussion](https://github.com/chasmlol/skate3clone/blob/32ba20633f445eacc65aa32459c18efbdc03c91b/parity/DUAL_ORACLE.md) is a methodological reference for checking readiness, applying equivalent inputs and comparing aligned states on controlled geometry. This repository cites the concept and supplies its own synthetic comparison example; it does not reuse that project's implementation or prose.

When designing your own comparison, establish both systems' readiness, normalize simulation steps and coordinate conventions, record initial conditions, and retain the exact input sequence. Define tolerances before seeing a mismatch. If equivalent states cannot be established, report an inconclusive comparison instead of forcing a parity score.

## Provenance is part of correctness

[IW4L's movement provenance note](https://github.com/vladtrc/iw4L/blob/acc57a5c9dd027db8eb5ef17c792fa69f059daa1/docs/provenance/movement-iw4.md) describes replacing a solver of uncertain provenance using a new behavioral contract and independent geometric tests. It separates procedural isolation from an enforced sandbox, and analytic tests from retail comparison.

Use the same clarity in reporting your own process. Record which materials each implementation stage received and which tests ran. Do not promise legal clean-room status because a different model generated the replacement. Independent synthetic tests establish their tested properties, not full retail parity.

The [catalog](source-catalog.md) records license observations. In particular, skate3clone explicitly grants no software license, and missing licenses elsewhere are not permission to reuse code.
