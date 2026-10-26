#!/usr/bin/env python3
"""Deterministic, offline routing of recorded evidence. Never executes a tool."""

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NATIVE = {"PE", "ELF", "Mach-O"}
OPERATIONS = {"static", "batch", "dynamic", "capture", "fuzz", "patch", "learn"}
RUNTIMES = {"native", "dotnet", "unity-mono", "unity-il2cpp", "electron", "javascript", "browser", "firmware", "wasm", "protocol", "unknown"}


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key: " + key)
        result[key] = value
    return result


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"), object_pairs_hook=unique_object)


def route(request, catalog=None):
    catalog = catalog or load_json(ROOT / "references" / "tool-routes.json")
    if not isinstance(request, dict) or request.get("schema_version") != 1 or isinstance(request.get("schema_version"), bool):
        raise ValueError("schema_version must be 1")
    operation = request.get("operation")
    if operation not in OPERATIONS:
        raise ValueError("operation must be one of " + ", ".join(sorted(OPERATIONS)))
    result = {"schema_version": 1, "status": "needs_identification", "route": None,
              "primary": None, "fallback": None, "references": [], "reasons": [],
              "execution": "No tool executed; follow references/tool-routing.md before use."}
    if operation == "learn":
        result.update(status="education_only", route="education", references=["references/resource-catalog.md#education"])
        result["reasons"].append("Courses and benchmarks are references, never executable tool selections.")
        return result
    authorization = request.get("authorization", {})
    if authorization.get("owned_or_authorized") is not True or operation not in authorization.get("operations", []):
        result.update(status="blocked_scope")
        result["reasons"].append("The requested operation is not in the recorded authorized target scope.")
        return result
    if request.get("security_bypass") is not False:
        result.update(status="blocked_scope")
        result["reasons"].append("Record security_bypass=false; DRM, ownership and anti-cheat bypass are outside this skill.")
        return result
    privacy = request.get("privacy", {})
    if privacy.get("agent") not in {"local", "cloud"}:
        result.update(status="needs_privacy_scope")
        return result
    if privacy["agent"] == "cloud" and privacy.get("binary_disclosure_authorized") is not True:
        result.update(status="blocked_disclosure")
        result["reasons"].append("Keep private binary-derived tool responses local until this target and destination are authorized.")
        return result
    observed = request.get("observed", {})
    runtime = observed.get("runtime", "unknown")
    fmt = observed.get("format")
    provenance = observed.get("evidence", {})
    if runtime not in RUNTIMES:
        raise ValueError("unknown runtime enum")
    required = {"format", "runtime", "platform", "architecture"}
    if any(not isinstance(provenance.get(k), str) or not provenance[k].strip() for k in required):
        result["reasons"].append("Record header/parser/runtime evidence for format, runtime, platform and architecture; filenames are insufficient. Use 'not applicable' with reason for source/protocol targets.")
        return result
    if any(observed.get(k) in (None, "", "unknown") for k in required):
        result["reasons"].append("Resolve unknown target facts before selecting a tool.")
        return result
    if observed.get("conflicting_evidence", False):
        result["reasons"].append("Resolve conflicting runtime/header evidence; do not silently pick a platform.")
        return result
    if runtime != "browser" and not re.fullmatch(r"[0-9a-fA-F]{64}", str(observed.get("sha256", ""))):
        result["reasons"].append("Record the actual input SHA-256 (or hashed source manifest) before routing.")
        return result
    if runtime == "browser" and not provenance.get("session_identity"):
        result["reasons"].append("Record the authorized browser/session identity before selecting observation tools.")
        return result
    if observed.get("game_profile") == "bully-x360" and fmt == "XEX":
        if observed.get("platform") == "xbox360" and observed.get("architecture") == "powerpc" and provenance.get("game_profile"):
            specialist = catalog["game_profiles"]["bully-x360"]
            result.update(status="specialized_plan_required", route="xbox360-recompilation", specialist_workflow=specialist)
            result["references"].extend([specialist["reference"], "references/bully-workflow.md"])
            result["reasons"].append("XEX/PPC is the console workflow, not a PE/x86 PC substitute; verify translator metadata/runtime before execution.")
            return result
    if runtime in {"native", "dotnet", "unity-mono", "unity-il2cpp"} and fmt not in NATIVE:
        result["reasons"].append("This runtime needs a verified native container or managed PE; inspect the actual member, not an archive filename.")
        return result
    if runtime in {"native", "unity-il2cpp"}:
        if observed.get("architecture") == "not-applicable" or observed.get("platform") == "not-applicable":
            result["reasons"].append("Native code requires an actual target architecture and platform.")
            return result
        platforms = {"PE": {"windows"}, "ELF": {"linux", "android", "ps5"}, "Mach-O": {"macos", "ios"}}
        if observed.get("platform") not in platforms[fmt]:
            result["reasons"].append("Container/platform combination needs specialist identification; do not treat compatibility layers as the binary's target OS.")
            return result
    if runtime in {"dotnet", "unity-mono"} and fmt != "PE":
        result["reasons"].append("Managed CLI assemblies require validated PE/CLI metadata, not just an engine label.")
        return result
    if runtime.startswith("unity-") and not provenance.get("unity_runtime"):
        result["reasons"].append("Distinguish real CLI assemblies from IL2CPP metadata plus native registration evidence; an Assembly-CSharp filename alone is not proof.")
        return result
    if runtime == "wasm" and fmt != "WASM":
        result["reasons"].append("Require validated WebAssembly magic/version, not a .wasm suffix.")
        return result
    host = request.get("host")
    if host not in {"linux", "macos", "windows"}:
        result["reasons"].append("Record the actual analysis host OS.")
        return result
    if operation in {"capture", "fuzz", "patch"}:
        result.update(status="specialized_plan_required")
        result["reasons"].append("Scope is recorded; define target, reversibility, traffic/process limits and acceptance tests before this active operation. Static tool routing does not authorize it.")
        return result
    key = runtime
    if runtime == "firmware" and fmt in {"IPSW", "OTA", "DYLD"}:
        key = "apple-firmware"
    if runtime == "wasm" and observed.get("wasm_kind") == "core" and request.get("goal") == "text-sections":
        key = "wasm-core-text"
    if runtime == "native":
        key = "native-batch" if operation == "batch" else "native"
        if operation == "dynamic":
            key = {"PE": "debug-pe", "ELF": "debug-elf", "Mach-O": "debug-macho"}[fmt]
            if observed.get("platform") == "ios":
                key = "instrument"
    elif operation == "dynamic":
        key = {"dotnet": "debug-managed", "unity-mono": "debug-managed", "unity-il2cpp": "instrument", "electron": "browser", "javascript": "browser", "browser": "browser"}.get(runtime)
    if not key or key not in catalog["routes"]:
        result["reasons"].append("No supported automatic route; identify the target or write a bounded specialist plan.")
        return result
    profile = observed.get("game_profile")
    if profile:
        if profile not in catalog["game_profiles"] or not provenance.get("game_profile"):
            result["reasons"].append("Unknown or unevidenced game profile; preserve edition ambiguity.")
            return result
        expected = {"bully-pc": ("PE", "windows", "x86"), "fnv": ("PE", "windows", "x86"),
                    "dsr": ("PE", "windows", "x86_64"), "ds1": ("PE", "windows", "x86"),
                    "mw2-2009": ("PE", "windows", "x86"), "elden-ring": ("PE", "windows", "x86_64"),
                    "ps5": ("ELF", "ps5", "x86_64")}.get(profile)
        if expected and (fmt, observed["platform"], observed["architecture"]) != expected:
            result["reasons"].append("Game edition/profile conflicts with the recorded container/platform/architecture; resolve before routing.")
            return result
        specialist = catalog["game_profiles"][profile]
        result["references"].append(specialist["reference"])
        result["specialist_workflow"] = specialist
    choice = catalog["routes"][key]
    result.update(route=key)
    result["references"].append(choice["reference"])
    records = request.get("available_tools", [])
    if not isinstance(records, list) or any(not isinstance(x, dict) or not x.get("id") for x in records):
        raise ValueError("available_tools must be records with id")
    if len({x["id"] for x in records}) != len(records):
        raise ValueError("duplicate available tool id")
    available = {x["id"]: x for x in records}
    candidates = [t for t in choice["candidates"] if host in catalog["tools"][t]["hosts"]]
    if not candidates:
        result.update(status="unsupported_host")
        result["reasons"].append("No supported candidate on this host; do not migrate work or install a VM implicitly.")
        return result
    def verified(tool):
        rec = available.get(tool, {})
        return (rec.get("installed") is True and rec.get("compatible_with_target") is True
                and rec.get("license_reviewed") is True and rec.get("local_transport") is True
                and bool(rec.get("version")) and bool(rec.get("pinned_docs")))
    ready = [t for t in candidates if verified(t)]
    primary = ready[0] if ready else candidates[0]
    fallback = next((t for t in ready if t != primary), None)
    fallback = fallback or next((t for t in candidates if t != primary), None)
    def describe(tool):
        if not tool:
            return None
        return {"id": tool, "repository": catalog["tools"][tool]["repository"],
                "verified_available": verified(tool), "requirements": catalog["tools"][tool]["requirements"]}
    result.update(status="ready_for_bounded_use" if ready else "needs_tool_verification",
                  primary=describe(primary), fallback=describe(fallback))
    result["reasons"].extend([choice["reason"], "Prefer the highest-ranked compatible installed candidate; fallback is conditional on verification, not a second simultaneous MCP."])
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(route(load_json(args.manifest)), indent=2))
    except (ValueError, OSError, TypeError, AttributeError) as error:
        parser.exit(2, str(error) + "\n")


if __name__ == "__main__":
    main()
