## 2024-06-23 - [SSRF Bypass via IPv4-Mapped IPv6]
**Vulnerability:** The SSRF protection in `validate_url` (`backend/util/request.py`) blocked internal IPv4 addresses but failed to block IPv4-mapped IPv6 addresses like `::ffff:127.0.0.1`.
**Learning:** Python's `ipaddress` module parses these strictly as `IPv6Address` objects. Since internal network lists typically contain `IPv4Network` objects (like `127.0.0.0/8`), `ip in network` returns False, leading to a dangerous bypass.
**Prevention:** When evaluating IP addresses against blocklists, always check if an IPv6 object has an `.ipv4_mapped` property. If it does, extract and validate the mapped IPv4 address instead of the IPv6 container. Example: `ip_to_check = getattr(ip_addr, 'ipv4_mapped', None) or ip_addr`.
