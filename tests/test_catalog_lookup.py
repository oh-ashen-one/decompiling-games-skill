"""Prove that selected queries return bounded relevant records, not bulk context."""

import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("catalog_lookup", ROOT / "scripts/catalog_lookup.py")
lookup = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(lookup)


class LookupTests(unittest.TestCase):
    def setUp(self):
        self.entries = json.loads(lookup.CATALOG.read_text())["entries"]

    def test_selected_domain_excludes_unrelated_entries_and_pages(self):
        first = lookup.lookup(self.entries, section="05")
        self.assertEqual(5, first["returned"])
        self.assertEqual(8, first["matches"])
        self.assertTrue(all(x["section"] == "05" for x in first["entries"]))
        second = lookup.lookup(self.entries, section="05", offset=first["next_offset"])
        self.assertEqual(3, second["returned"])
        self.assertIsNone(second["next_offset"])
        self.assertEqual(8, len({x["id"] for x in first["entries"] + second["entries"]}))

    def test_empty_selector_and_unbounded_limits_rejected(self):
        for kwargs in ({}, {"query": " "}, {"section": "99"}, {"query": "a", "limit": 114},
                       {"query": "a", "offset": -1}):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                lookup.lookup(self.entries, **kwargs)

    def test_specific_tool_query_and_unknown_name(self):
        result = lookup.lookup(self.entries, query="ILSpy", section="05")
        self.assertIn("ILSpy", [x["name"] for x in result["entries"]])
        self.assertTrue(all(x["section"] == "05" for x in result["entries"]))
        self.assertEqual([], lookup.lookup(self.entries, query="nonexistent-unique-tool")["entries"])

    def test_cli_no_filter_refuses_and_selected_output_is_small(self):
        cmd = [sys.executable, "-B", str(ROOT / "scripts/catalog_lookup.py")]
        self.assertEqual(2, subprocess.run(cmd, capture_output=True).returncode)
        proc = subprocess.run(cmd + ["--query", "ILSpy", "--section", "05"], capture_output=True)
        self.assertEqual(0, proc.returncode)
        self.assertLess(len(proc.stdout), 3000)
        self.assertNotIn(b"Revenant", proc.stdout)


if __name__ == "__main__":
    unittest.main()
