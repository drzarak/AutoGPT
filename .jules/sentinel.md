## 2024-06-21 - IPv4-Mapped IPv6 SSRF Bypass
**Vulnerability:** The IP blocking mechanism (`_is_ip_blocked`) did not correctly identify IPv4-mapped IPv6 addresses (e.g., `::ffff:127.0.0.1`), leading to a potential SSRF bypass for private networks.
**Learning:** Python's `ipaddress` module treats IPv4-mapped IPv6 addresses as IPv6 objects, meaning they do not automatically match IPv4 subnets in a blocklist unless explicitly converted or handled.
**Prevention:** Always check `getattr(ip_addr, "ipv4_mapped", None)` when validating IP addresses against a blocklist, extracting the underlying IPv4 address if present, to ensure mapped addresses are evaluated correctly.
