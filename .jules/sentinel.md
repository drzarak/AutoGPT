## 2026-07-07 - [SSRF Bypass via IPv4-mapped IPv6 Addresses]
**Vulnerability:** The SSRF filter bypassed blocked loopback/private IPv4 networks if represented as an IPv4-mapped IPv6 address (e.g., `::ffff:127.0.0.1` or `::ffff:0.0.0.0`).
**Learning:** Python's `ipaddress` module parses these as `IPv6Address` objects, which won't match `IPv4Network` entries in the blocklist. Additionally, `IPv4Address('0.0.0.0')` is falsey in Python.
**Prevention:** Always extract `ipv4_mapped` from parsed IPs using `mapped_ip = getattr(ip_addr, 'ipv4_mapped', None)` and ensure proper `if mapped_ip is not None:` truthiness checks before applying IPv4-based filtering logic.
