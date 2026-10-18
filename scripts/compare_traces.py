#!/usr/bin/env python3
"""Compare explicitly selected numeric trace files; no game or command execution."""

import argparse
import json
import math
from pathlib import Path
import sys


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def validate(trace):
    if not isinstance(trace, dict) or set(trace) != {
        "schema_version", "scenario", "build_id", "records"
    }:
        raise ValueError("expected schema_version, scenario, build_id and records")
    if type(trace["schema_version"]) is not int or trace["schema_version"] != 1:
        raise ValueError("schema_version must be integer 1")
    for key in ("scenario", "build_id"):
        if not isinstance(trace[key], str) or not trace[key].strip():
            raise ValueError(f"{key} must be a nonempty string")
    records = trace["records"]
    if not isinstance(records, list) or not records:
        raise ValueError("records must be a nonempty list")
    previous_step = -1
    for record in records:
        if not isinstance(record, dict) or set(record) != {"step", "state"}:
            raise ValueError("each record must contain exactly step and state")
        step = record["step"]
        if type(step) is not int or step <= previous_step:
            raise ValueError("steps must be nonnegative, unique and increasing integers")
        previous_step = step
        state = record["state"]
        if not isinstance(state, dict) or not state:
            raise ValueError("state must be a nonempty numeric object")
        for key, value in state.items():
            if not isinstance(key, str) or not key.strip():
                raise ValueError("state field names must be nonempty strings")
            if type(value) not in (int, float):
                raise ValueError(f"state field {key} must be numeric, not boolean")
            if isinstance(value, float) and not math.isfinite(value):
                raise ValueError(f"state field {key} must be finite")
    return trace


def load_trace(path):
    with Path(path).open(encoding="utf-8") as stream:
        return validate(json.load(stream, object_pairs_hook=unique_object))


def compare(reference, candidate, atol=0.0):
    validate(reference)
    validate(candidate)
    if not math.isfinite(atol) or atol < 0:
        raise ValueError("atol must be finite and nonnegative")
    if reference["scenario"] != candidate["scenario"]:
        return ["scenario identifiers differ"]
    left, right = reference["records"], candidate["records"]
    if [r["step"] for r in left] != [r["step"] for r in right]:
        return ["record steps differ (missing, extra or misaligned samples)"]
    mismatches = []
    for original, rebuilt in zip(left, right):
        step = original["step"]
        expected, actual = original["state"], rebuilt["state"]
        if set(expected) != set(actual):
            mismatches.append(f"step {step}: state fields differ")
            continue
        for field in sorted(expected):
            a, b = expected[field], actual[field]
            if type(a) is not type(b):
                mismatches.append(f"step {step}, {field}: numeric types differ")
                continue
            # Integers stay exact, including values larger than float precision.
            equal = a == b if type(a) is int else math.isclose(a, b, rel_tol=0, abs_tol=atol)
            if not equal:
                mismatches.append(f"step {step}, {field}: {a!r} != {b!r}")
    return mismatches


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("reference")
    parser.add_argument("candidate")
    parser.add_argument("--atol", type=float, default=0.0,
                        help="absolute tolerance for float fields only (default: 0)")
    args = parser.parse_args(argv)
    try:
        reference = load_trace(args.reference)
        candidate = load_trace(args.candidate)
        mismatches = compare(reference, candidate, args.atol)
    except (OSError, ValueError, RecursionError) as exc:
        print(f"INVALID: {exc}", file=sys.stderr)
        return 2
    if mismatches:
        print("MISMATCH")
        for message in mismatches:
            print(message)
        return 1
    print(f"MATCH: {len(reference['records'])} samples; atol={args.atol:g}")
    print("Only the supplied numeric observations were compared; this is not whole-program parity.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
