#!/usr/bin/env python3
"""Return a bounded subset of the audit catalog; never fetch or execute anything."""

import argparse
import json
from pathlib import Path

CATALOG = Path(__file__).resolve().parents[1] / "references/resource-catalog.json"


def lookup(entries, query=None, section=None, limit=5, offset=0):
    query = (query or "").strip().casefold()
    if not query and section is None:
        raise ValueError("Choose --query or --section; bulk output is not a default.")
    if section is not None and section not in {f"{n:02}" for n in range(1, 13)}:
        raise ValueError("section must be 01 through 12")
    if type(limit) is not int or not 1 <= limit <= 8 or type(offset) is not int or offset < 0:
        raise ValueError("limit must be 1..8 and offset a nonnegative integer")
    matches = [entry for entry in entries
               if (section is None or entry["section"] == section)
               and (not query or query in " ".join(str(entry.get(k) or "") for k in
                    ("name", "canonical_url", "note", "status")).casefold())]
    selected = matches[offset:offset + limit]
    return {"matches": len(matches), "returned": len(selected),
            "next_offset": offset + limit if offset + limit < len(matches) else None,
            "entries": selected}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--query")
    parser.add_argument("--section")
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--offset", type=int, default=0)
    args = parser.parse_args()
    try:
        entries = json.loads(CATALOG.read_text(encoding="utf-8"))["entries"]
        result = lookup(entries, args.query, args.section, args.limit, args.offset)
        print(json.dumps(result, indent=2))
    except (OSError, ValueError) as error:
        parser.exit(2, str(error) + "\n")


if __name__ == "__main__":
    main()
