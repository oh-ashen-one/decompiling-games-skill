# Firmware route

Read only this selected domain and the pinned upstream documentation needed for the current question. Follow [tool-use checks](../tool-routing.md) before invoking a tool.

| Observed target / task | Primary | Justified fallback / specialist |
|---|---|---|
| Apple IPSW/OTA/dyld | blacktop/ipsw | Format-specific Apple tooling; generic firmware stack only if it actually supports the format |
| Authorized iOS runtime | Frida with supported device/signing mode | Objection for compatible convenience operations; not a signing/security bypass |
| Firmware / unknown embedded container | Binwalk static inventory | UBI → ubi_reader; JFFS2 → Jefferson; modified SquashFS → sasquatch after standard extraction fails. FACT for corpus comparison; EMBA for scoped broader security analysis |
| Firmware emulation requested | Compatible isolated FirmAE or reviewed current FAT | Stop if architecture, kernel/userland or license fit unknown. Revenant is an identity-qualified experimental reference, never default |

For source/license details, query `scripts/catalog_lookup.py --section <section>` for section 06 or 09, or use a specific tool name with `--query`. Do not load the full catalog.
