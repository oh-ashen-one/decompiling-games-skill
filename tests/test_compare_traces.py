"""Public-safe behavioral tests for the numeric comparison helper."""

import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "compare_traces.py"
SPEC = importlib.util.spec_from_file_location("compare_traces", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ComparisonTests(unittest.TestCase):
    def setUp(self):
        self.reference = MODULE.load_trace(ROOT / "examples" / "reference.json")
        self.candidate = copy.deepcopy(self.reference)
        self.candidate["build_id"] = "independent-candidate"

    def test_different_builds_can_have_identical_observations(self):
        self.assertEqual([], MODULE.compare(self.reference, self.candidate))

    def test_float_tolerance_is_explicit(self):
        self.candidate["records"][1]["state"]["position"] += 0.0001
        self.assertTrue(MODULE.compare(self.reference, self.candidate))
        self.assertEqual([], MODULE.compare(self.reference, self.candidate, 0.001))

    def test_large_integer_differences_are_never_rounded_away(self):
        self.reference["records"][0]["state"]["counter"] = 2**60
        self.candidate["records"][0]["state"]["counter"] = 2**60 + 1
        self.assertTrue(MODULE.compare(self.reference, self.candidate, 10.0))

    def test_missing_samples_and_fields_fail(self):
        self.candidate["records"].pop()
        self.assertTrue(MODULE.compare(self.reference, self.candidate))
        self.candidate = copy.deepcopy(self.reference)
        del self.candidate["records"][0]["state"]["counter"]
        self.assertTrue(MODULE.compare(self.reference, self.candidate))

    def test_incompatible_scenarios_and_numeric_types_fail(self):
        self.candidate["scenario"] = "different-input-sequence"
        self.assertTrue(MODULE.compare(self.reference, self.candidate))
        self.candidate = copy.deepcopy(self.reference)
        self.candidate["records"][0]["state"]["counter"] = 0.0
        self.assertTrue(MODULE.compare(self.reference, self.candidate))

    def test_nonfinite_boolean_and_unknown_schema_rejected(self):
        for invalid in (float("nan"), float("inf"), True, "0"):
            with self.subTest(value=invalid):
                candidate = copy.deepcopy(self.reference)
                candidate["records"][0]["state"]["position"] = invalid
                with self.assertRaises(ValueError):
                    MODULE.validate(candidate)
        self.candidate["schema_version"] = True
        with self.assertRaises(ValueError):
            MODULE.validate(self.candidate)
        self.candidate = copy.deepcopy(self.reference)
        self.candidate["unknown"] = "not silently ignored"
        with self.assertRaises(ValueError):
            MODULE.validate(self.candidate)

    def test_duplicate_keys_empty_trace_and_bad_steps_rejected(self):
        with self.assertRaises(ValueError):
            json.loads('{"step": 1, "step": 2}', object_pairs_hook=MODULE.unique_object)
        for records in ([], [{"step": -1, "state": {"x": 1}}],
                        [{"step": 0, "state": {"x": 1}}] * 2):
            with self.subTest(records=records):
                self.candidate["records"] = records
                with self.assertRaises(ValueError):
                    MODULE.validate(self.candidate)

    def test_invalid_tolerances_rejected(self):
        for value in (-1.0, float("inf"), float("nan")):
            with self.assertRaises(ValueError):
                MODULE.compare(self.reference, self.candidate, value)

    def test_cli_exit_codes(self):
        with tempfile.TemporaryDirectory() as directory:
            candidate_path = Path(directory) / "candidate.json"
            command = [sys.executable, str(SCRIPT),
                       str(ROOT / "examples" / "reference.json"), str(candidate_path)]
            candidate_path.write_text(json.dumps(self.candidate), encoding="utf-8")
            self.assertEqual(0, subprocess.run(command, capture_output=True).returncode)
            self.candidate["records"][0]["state"]["counter"] = 9
            candidate_path.write_text(json.dumps(self.candidate), encoding="utf-8")
            self.assertEqual(1, subprocess.run(command, capture_output=True).returncode)
            candidate_path.write_text("not json", encoding="utf-8")
            self.assertEqual(2, subprocess.run(command, capture_output=True).returncode)


if __name__ == "__main__":
    unittest.main()
