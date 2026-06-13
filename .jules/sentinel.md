## 2024-06-13 - SSRF Bypass via IPv4-mapped IPv6 Addresses
**Vulnerability:** The SSRF protection mechanism `_is_ip_blocked` in `autogpt_platform/backend/backend/util/request.py` failed to block IPv4-mapped IPv6 addresses (e.g. `::ffff:127.0.0.1`), allowing an attacker to bypass the blocklist and hit internal IPv4 networks.
**Learning:** Python's `ipaddress` module parses `::ffff:127.0.0.1` as an `IPv6Address` which does not match IPv4 networks in a blocklist, creating a gap between the application's blocklist check and the underlying socket or OS behavior which will treat it as an IPv4 loopback connection.
**Prevention:** Always check and extract `.ipv4_mapped` when handling generic `ipaddress` objects for filtering.
