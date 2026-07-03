## 2024-05-24 - [SSRF Bypass using IPv4-mapped IPv6 Address]
**Vulnerability:** The URL validation logic `_is_ip_blocked` was vulnerable to Server-Side Request Forgery (SSRF) bypass through DNS rebinding using IPv4-mapped IPv6 addresses (e.g. `::ffff:127.0.0.1`). When a host was resolved to an IPv4-mapped IPv6 address, it bypassed the standard internal IPv4 checks.
**Learning:** `ipaddress.ip_address()` evaluates IPv4-mapped IPv6 strings as IPv6 addresses. Therefore, standard IPv4 blocklists fail to block these mapped addresses unless specifically accounted for.
**Prevention:** Always extract and validate the underlying mapped IPv4 address from the original IP object (via `getattr(ip_addr, 'ipv4_mapped', None)`) when attempting to prevent SSRF against internal subnets.
