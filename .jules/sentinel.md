
## 2024-05-24 - IPv4-mapped IPv6 Address SSRF Bypass
**Vulnerability:** The SSRF protection in `backend.util.request.requests` failed to check if an IPv6 address was an IPv4-mapped address (e.g., `::ffff:127.0.0.1`), allowing an attacker to bypass the IPv4 local loopback blocklist (`127.0.0.0/8`).
**Learning:** `ipaddress.ip_address` objects for IPv6 include an `.ipv4_mapped` property. If the IPv6 address is mapped to IPv4, this returns the underlying IPv4 address object, otherwise it returns `None`. Without checking this property, an IPv4-mapped IPv6 address will fail the `in` operator check against IPv4 networks, resulting in an SSRF bypass.
**Prevention:** When evaluating IP addresses against a blocklist or allowlist using the `ipaddress` module, always inspect and convert mapped addresses using the `.ipv4_mapped` property before comparison.
