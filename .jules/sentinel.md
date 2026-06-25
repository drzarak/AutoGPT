
## 2024-06-25 - Prevent SSRF bypass via IPv4-mapped IPv6 addresses
**Vulnerability:** The application's SSRF protection `_is_ip_blocked` used `ipaddress.ip_address()` to validate if an IP fell within a blocklist. However, it did not account for IPv4-mapped IPv6 addresses (e.g., `::ffff:127.0.0.1`). Attackers could map private IPv4 addresses to bypass the blocklist, allowing requests to internal resources.
**Learning:** Python's `ipaddress` library treats `::ffff:127.0.0.1` as an IPv6 object. Since the blocklist (`127.0.0.0/8`, etc.) are IPv4 networks, the `in` check will fail without unwrapping the IPv4 mapped representation.
**Prevention:** Always extract the underlying IPv4 address when using `ipaddress` to validate against an IPv4 blocklist by checking `getattr(ip_addr, 'ipv4_mapped', None)`.
