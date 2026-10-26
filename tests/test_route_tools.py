"""Observable routing decisions using invented evidence; no target/tool execution."""

import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("route_tools", ROOT / "scripts/route_tools.py")
router = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(router)
CATALOG = router.load_json(ROOT / "references/tool-routes.json")


def request(runtime="native", fmt="PE", platform="windows", host="linux", operation="static"):
    return {"schema_version": 1, "operation": operation, "host": host,
            "authorization": {"owned_or_authorized": True, "operations": [operation]},
            "security_bypass": False, "privacy": {"agent": "local"},
            "observed": {"format": fmt, "runtime": runtime, "platform": platform,
                         "architecture": "x86_64", "sha256": "0" * 64,
                         "evidence": {k: "SYNTHETIC test fixture: parsed " + k for k in
                                      ("format", "runtime", "platform", "architecture", "unity_runtime", "session_identity")}},
            "available_tools": [{"id": name, "installed": True, "version": "SYNTHETIC-test-only",
                                 "pinned_docs": "SYNTHETIC reviewed fixture; not real tool verification",
                                 "compatible_with_target": True, "license_reviewed": True,
                                 "local_transport": True} for name in CATALOG["tools"]]}


class RoutingTests(unittest.TestCase):
    def test_native_containers_have_same_interactive_default(self):
        for fmt, platform in [("PE", "windows"), ("ELF", "linux"), ("Mach-O", "macos")]:
            with self.subTest(fmt=fmt):
                result = router.route(request(fmt=fmt, platform=platform))
                self.assertEqual("ready_for_bounded_use", result["status"])
                self.assertEqual("rea", result["primary"]["id"])
                self.assertEqual("ghidra", result["fallback"]["id"])

    def test_batch_uses_persistent_native_project(self):
        result = router.route(request(operation="batch"))
        self.assertEqual("ghidra", result["primary"]["id"])

    def test_runtime_specific_routes_and_fallbacks(self):
        cases = [("dotnet", "PE", "ilspy", "dnspyex"),
                 ("unity-mono", "PE", "ilspy", "dnspyex"),
                 ("unity-il2cpp", "PE", "cpp2il", "ghidra"),
                 ("electron", "ASAR", "asar", "rea"),
                 ("javascript", "source", "babel-parser", "acorn"),
                 ("browser", "session", "cdp", "playwright"),
                 ("firmware", "container", "binwalk", None),
                 ("wasm", "WASM", "wasm-tools", "wabt"),
                 ("protocol", "PCAPNG", "wireshark", "scapy")]
        for runtime, fmt, primary, fallback in cases:
            with self.subTest(runtime=runtime):
                result = router.route(request(runtime, fmt, host="windows"))
                self.assertEqual(primary, result["primary"]["id"])
                self.assertEqual(fallback, result["fallback"]["id"] if result["fallback"] else None)

    def test_wasm_component_and_core_text_are_distinct(self):
        req = request("wasm", "WASM")
        req.update(goal="text-sections")
        req["observed"]["wasm_kind"] = "core"
        self.assertEqual("wabt", router.route(req)["primary"]["id"])
        req["observed"]["wasm_kind"] = "component"
        self.assertEqual("wasm-tools", router.route(req)["primary"]["id"])
        self.assertNotIn("wasm-decompile", CATALOG["tools"])

    def test_apple_firmware_uses_apple_specialist(self):
        result = router.route(request("firmware", "IPSW", "ios", "macos"))
        self.assertEqual("ipsw", result["primary"]["id"])

    def test_dynamic_native_routes_match_target_and_host(self):
        for fmt, platform, host, expected in [("PE", "windows", "windows", "x64dbg"),
                                             ("ELF", "linux", "linux", "gdb"),
                                             ("Mach-O", "macos", "macos", "lldb"),
                                             ("Mach-O", "ios", "macos", "frida")]:
            with self.subTest(fmt=fmt, platform=platform):
                result = router.route(request(fmt=fmt, platform=platform, host=host, operation="dynamic"))
                self.assertEqual(expected, result["primary"]["id"])
        self.assertEqual("unsupported_host", router.route(request(operation="dynamic", host="macos"))["status"])

    def test_available_fallback_wins_over_unverified_preference(self):
        req = request()
        req["available_tools"] = [x for x in req["available_tools"] if x["id"] == "ghidra"]
        result = router.route(req)
        self.assertEqual("ghidra", result["primary"]["id"])
        self.assertFalse(result["fallback"]["verified_available"])

    def test_absent_or_unreviewed_tools_do_not_become_ready(self):
        for field in ("installed", "compatible_with_target", "license_reviewed", "local_transport", "version", "pinned_docs"):
            req = request()
            for tool in req["available_tools"]:
                tool[field] = False
            with self.subTest(field=field):
                self.assertEqual("needs_tool_verification", router.route(req)["status"])

    def test_no_filename_or_unknown_architecture_guessing(self):
        req = request()
        req["filename"] = "DefinitelyWindowsGame.exe"
        req["observed"]["evidence"] = {}
        self.assertEqual("needs_identification", router.route(req)["status"])
        for value in ("unknown", "not-applicable"):
            req = request()
            req["observed"]["architecture"] = value
            self.assertIsNone(router.route(req)["primary"])
        req = request(fmt="WASM")
        self.assertIsNone(router.route(req)["primary"])
        req = request(fmt="ELF", platform="windows")
        self.assertIsNone(router.route(req)["primary"])

    def test_conflicting_runtime_and_missing_unity_evidence_stop(self):
        req = request("unity-il2cpp")
        del req["observed"]["evidence"]["unity_runtime"]
        self.assertIsNone(router.route(req)["primary"])
        req = request()
        req["observed"]["conflicting_evidence"] = True
        self.assertIsNone(router.route(req)["primary"])
        req = request("dotnet", "ELF", "linux")
        self.assertIsNone(router.route(req)["primary"])

    def test_missing_hash_or_browser_identity_stops(self):
        req = request()
        del req["observed"]["sha256"]
        self.assertIsNone(router.route(req)["primary"])
        req = request("browser", "session")
        del req["observed"]["evidence"]["session_identity"]
        self.assertIsNone(router.route(req)["primary"])

    def test_scope_and_cloud_boundary_are_not_tool_availability(self):
        req = request()
        req["authorization"]["operations"] = []
        self.assertEqual("blocked_scope", router.route(req)["status"])
        req = request()
        req["privacy"] = {"agent": "cloud"}
        self.assertEqual("blocked_disclosure", router.route(req)["status"])
        req["privacy"]["binary_disclosure_authorized"] = True
        self.assertEqual("ready_for_bounded_use", router.route(req)["status"])
        req["security_bypass"] = True
        self.assertEqual("blocked_scope", router.route(req)["status"])

    def test_active_operations_require_bounded_plan_even_when_scoped(self):
        for operation in ("capture", "fuzz", "patch"):
            req = request("protocol", "PCAP", operation=operation)
            self.assertEqual("specialized_plan_required", router.route(req)["status"])
            req["authorization"]["operations"] = ["static"]
            self.assertEqual("blocked_scope", router.route(req)["status"])

    def test_education_does_not_select_executable(self):
        result = router.route({"schema_version": 1, "operation": "learn"})
        self.assertEqual("education_only", result["status"])
        self.assertIsNone(result["primary"])
        self.assertIsNone(result["fallback"])

    def test_specialist_game_repositories_are_retained(self):
        profiles = {"bully-pc": "LiquidSnake0/bully-re", "fnv": "slaterain/nv-rs",
                    "dsr": "oh-ashen-one/dsr-mw2-crossover", "mw2-2009": "vladtrc/iw4L",
                    "ds1": "rehan-remade/universal-modder",
                    "faith-runner": "tnrjns/faith-runner",
                    "elden-ring": "Funny-Bones/ELDEN-RING-Combat-Rewrite",
                    "ps5": "boykopovar/AnyPS5"}
        for profile, repo in profiles.items():
            with self.subTest(profile=profile):
                req = request()
                if profile in {"bully-pc", "fnv", "ds1", "mw2-2009"}:
                    req["observed"]["architecture"] = "x86"
                if profile == "ps5":
                    req["observed"].update(format="ELF", platform="ps5")
                req["observed"]["game_profile"] = profile
                req["observed"]["evidence"]["game_profile"] = "SYNTHETIC exact edition fixture"
                result = router.route(req)
                self.assertEqual("https://github.com/" + repo, result["specialist_workflow"]["primary_repository"])
                self.assertIsNotNone(result["specialist_workflow"]["fallback_repository"])

    def test_bully_xbox_is_not_pc_route(self):
        req = request(fmt="XEX", platform="xbox360")
        req["observed"].update(architecture="powerpc", game_profile="bully-x360")
        req["observed"]["evidence"]["game_profile"] = "SYNTHETIC console edition fixture"
        result = router.route(req)
        self.assertEqual("xbox360-recompilation", result["route"])
        self.assertIsNone(result["primary"])
        self.assertIn("BullyRecomp", result["specialist_workflow"]["primary_repository"])

    def test_game_profile_cannot_override_conflicting_header(self):
        req = request()
        req["observed"]["game_profile"] = "ps5"
        req["observed"]["evidence"]["game_profile"] = "SYNTHETIC conflicting label"
        self.assertEqual("needs_identification", router.route(req)["status"])

    def test_ambiguous_game_and_duplicate_input_records_fail(self):
        req = request()
        req["observed"]["game_profile"] = "Dark Souls maybe Remastered"
        self.assertIsNone(router.route(req)["primary"])
        req = request()
        req["available_tools"].append(copy.deepcopy(req["available_tools"][0]))
        with self.assertRaises(ValueError):
            router.route(req)
        with self.assertRaises(ValueError):
            json.loads('{"operation":"static","operation":"dynamic"}', object_pairs_hook=router.unique_object)

    def test_catalog_coverage_and_non_executable_resources(self):
        audit = router.load_json(ROOT / "references/resource-catalog.json")["entries"]
        self.assertEqual(114, len(audit))
        self.assertEqual(114, len({x["id"] for x in audit}))
        self.assertEqual(108, len({x["canonical_url"] for x in audit if x["canonical_url"]}))
        self.assertEqual(4, sum("same_source_as" in x for x in audit))
        self.assertEqual(2, sum(x["canonical_url"] is None for x in audit))
        for entry in audit:
            self.assertTrue(entry["note"] and entry["license"] and entry["status"])
        for entry in CATALOG["routes"].values():
            for name in entry["candidates"]:
                self.assertIn(name, CATALOG["tools"])
        for name in ("wasm-decompile", "AgentRE-Bench", "SRE-Bench", "Revenant", "UMass"):
            self.assertNotIn(name, CATALOG["tools"])

    def test_cli_example_is_local_only_and_matches_route(self):
        result = subprocess.run([sys.executable, "-B", str(ROOT / "scripts/route_tools.py"),
                                 str(ROOT / "examples/routing/native-pe.json")], capture_output=True, text=True)
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual("rea", json.loads(result.stdout)["primary"]["id"])


if __name__ == "__main__":
    unittest.main()
