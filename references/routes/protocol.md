# Protocol route

Read only this selected domain and the pinned upstream documentation needed for the current question. Follow [tool-use checks](../tool-routing.md) before invoking a tool.

| Observed target / task | Primary | Justified fallback / specialist |
|---|---|---|
| Recorded PCAP/PCAPNG | Wireshark/TShark offline, name resolution off | Scapy offline parsing; Zeek many-flow logs; Construct for inferred binary schema; PcapPlusPlus for C++ integration |

For source/license details, query `scripts/catalog_lookup.py --section <section>` for section 11, or use a specific tool name with `--query`. Do not load the full catalog.
