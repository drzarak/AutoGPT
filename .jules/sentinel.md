
## 2024-05-24 - SSRF Bypass using IPv4-Mapped IPv6 Addresses
**Vulnerability:** The SSRF mitigation blocklist bypassed IPv4-mapped IPv6 addresses (e.g., `::ffff:127.0.0.1`) that translated directly to blocked IPv4 addresses. Python's `ipaddress` module's blocklist checks (`ip_addr in network`) treat IPv4 and IPv6 as mutually exclusive spaces and thus failed to block the mapped IP.
**Learning:** Checking against a blocklist requires handling multiple representations of IP addresses. Specifically, IPv4 addresses mapped to IPv6 spaces (`::ffff:x.x.x.x`) bypass simple IPv4 inclusion checks.
**Prevention:** Always check and extract the underlying IPv4 address from IPv6 objects using the `.ipv4_mapped` property. Use `getattr(ip_addr, 'ipv4_mapped', None)` safely to prevent bypasses via mapped addresses before comparing against blocked networks.
