
## 2024-05-18 - [SSRF Bypass via IPv4-mapped IPv6 Addresses]
**Vulnerability:** The SSRF protection in `backend.util.request` checked IP addresses against a blocklist, but failed to extract the underlying IPv4 address from an IPv4-mapped IPv6 address (e.g., `::ffff:127.0.0.1`). An attacker could supply this IPv6 address, bypass the IPv4 blocklist checks, and successfully target internal IPv4 networks.
**Learning:** The Python `ipaddress` module's `.ip_address` function converts mapped addresses to `IPv6Address` objects, which do not match `IPv4Network` objects in a blocklist, even if they fundamentally point to the same host in a dual-stack environment.
**Prevention:** Always check for and extract the underlying IPv4 address using `getattr(ip_addr, "ipv4_mapped", None)` before evaluating an IP address against a blocklist.
