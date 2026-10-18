# Validation and publication

## State the claim being tested

Keep these outcomes separate in every report:

| Evidence | What it establishes | What it does not establish |
|---|---|---|
| Static analysis | Observed instructions/data and explicitly marked inferences | Executed behavior or recovered original source |
| Successful compilation | A particular toolchain accepted the candidate | Correct semantics, portability or binary matching |
| Synthetic tests | The tested contract on the supplied cases | Original-game behavior or untested cases |
| Differential observations | Agreement for aligned observed states | Whole-program equivalence or identical hidden state |
| Reproducible binary/object comparison | The exact comparison criterion for a pinned build | Legal provenance or unmeasured runtime behavior |
| Rendered inspection / human gameplay review | The inspected scenes and interactions | Complete gameplay coverage or a timing guarantee |

Record target/build identity, tool versions, test cases, seeds, environment, expected/actual outputs and unresolved cases. Coverage must state its denominator and counting rule. An address mentioned in source is not necessarily an implemented function.

## Matching is a reproducible experiment

Pin compiler/linker versions, flags, headers, runtime libraries, object order and build scripts. Obtain historical toolchains through authorized channels; a repository download link is not redistribution permission. Separate a convenient development build from a reproducible reference build.

[LEGO Island](https://github.com/isledecomp/isle/blob/master/README.md) supplies a target-specific cold-rebuild example. [DX-Ball](https://github.com/N0zoM1z0/dx-ball/blob/main/docs/MATCHING.md) documents full-function comparisons with explicit COFF relocation mapping. Apply the ideas to a verified target; do not assume Bully uses the same compiler or inputs.

For x86, evaluate [reccmp](https://github.com/isledecomp/reccmp) against the identified compiler/debug metadata. [objdiff](https://github.com/encounter/objdiff) supports x86/x86_64 but requires suitable relocatable objects. A stripped linked PE does not automatically provide them. Establish reference extraction/mapping before selecting a comparator. Never silently discard significant operands to improve a similarity score.

## Behavioral comparisons

Use the same input sequence and an equivalent starting state. Account for random seeds, fixed-step count, coordinate convention, precision, imports, external state and memory side effects. Restore memory between isolated cases. Preserve failing cases, including boundary values, sign extension, overflow and invalid input where relevant.

Have the original execution or an independently justified specification supply expected outputs. Asking the same model to invent both implementation and oracle is not independent validation. Sanitizers, fuzzing and emulation are useful but prove only their tested properties and modeled environment.

Instrumentation should be exact-build-gated, reversible and bounded. Confirm that the hook is active and that it observes the intended path. Measure observer effects against an uninstrumented baseline. Do not equate timing from a recompiled or compatibility-layer execution with timing on the original platform.

## Synthetic comparison contract

`scripts/compare_traces.py` is an original standard-library-only Python 3 example. It compares two **already captured** files and never starts either program. The fixtures are invented values with no retail content. A trace has exactly:

- `schema_version`: integer `1`.
- `scenario`: a nonempty identifier for the exact controlled input/initial-state contract. The helper checks identifier equality, not the truth of that contract.
- `build_id`: a nonempty identifier for the producer; different builds are expected. The helper does not verify this identifier cryptographically. A real workflow should bind it to its private build manifest/hash.
- `records`: a nonempty ordered list of `{ "step": integer, "state": { "field": number } }` records. Steps are nonnegative and strictly increasing; state is a nonempty flat numeric object.

Both traces must have identical step sequences and state-field sets at each corresponding step. Integer fields compare exactly, including values above floating-point precision. Float fields use absolute tolerance `--atol`, default zero, with no relative tolerance. Numeric type changes fail. Booleans, nonfinite floats, duplicate JSON keys and unknown schema fields are rejected.

```sh
python3 scripts/compare_traces.py examples/reference.json examples/candidate.json
python3 -B -m unittest discover -s tests -v
```

Exit codes are `0` for matching supplied observations, `1` for a difference, and `2` for invalid input/options. A successful result is never a claim of whole-program parity. Identical fixtures demonstrate the interface; the tests additionally exercise differences, invalid schema, missing samples, tolerance and large integers.

This small helper does not compare nested memory, pointers, raw float bits, NaN payloads, strings or hidden state. In particular it treats positive/negative floating zero as numerically equal. If those distinctions matter, extend the schema and comparison deliberately with independent tests. Do not use a wide global tolerance to conceal a mismatch; a real heterogeneous trace may need per-field units and tolerances defined in its contract.

## Before public publication

Inspect every staged path and text diff; inspect reachable history too if the branch contains earlier work. Publish only original documentation/code, suitable schemas, synthetic fixtures, source links and compatible third-party notices. Keep retail assets/binaries, generated game code, decompiler exports, memory captures, private model logs, credentials, private paths and proprietary toolchain packages out of both files and history.

An ignore file is a convenience, not an authorization or content scanner. Review new files explicitly before staging. If sensitive material reached history, stop publication and handle it through an authorized remediation process rather than simply deleting the current file.

Verify local links, attribution, license labels and time-sensitive claims. Explain which statements are upstream reports and which tests were actually performed. Check that model/provider recommendations do not promise unsupported quality, hardware requirements or privacy.

For each reused file, retain an exact source/revision, applicable license, modifications and required notices. This release has no copied/adapted upstream implementation files. The MIT grant applies to this repository's original work only.
