## 2024-07-10 - SSRF IPv4-mapped IPv6 Bypass
**Vulnerability:** The custom HTTP requests wrapper (`backend.util.request.Requests`) intended to block SSRF was vulnerable to bypassing via IPv4-mapped IPv6 addresses (e.g., `::ffff:127.0.0.1`). The `ipaddress` module's containment checks don't automatically check the mapped IPv4 address against IPv4 networks.
**Learning:** Security validations on IP addresses must explicitly handle the `ipv4_mapped` property of IPv6 addresses when using Python's `ipaddress` module, otherwise private network restrictions can be bypassed.
**Prevention:** Always extract and validate the mapped IPv4 address (`getattr(ip_addr, 'ipv4_mapped', None)`) before performing containment checks against a blocklist of IPv4 networks.
