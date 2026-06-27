
## 2026-06-27 - [High] SSRF Bypass via IPv4-Mapped IPv6 Addresses
**Vulnerability:** The SSRF protection wrapper (`backend.util.request._is_ip_blocked`) checked raw IP addresses against a blacklist of internal ranges. It failed to account for IPv4-mapped IPv6 addresses (e.g., `::ffff:127.0.0.1`). If a hostile actor used this format, it bypassed the IP blocklist but could still resolve to the restricted IPv4 loopback during execution, resulting in SSRF.
**Learning:** Checking IPs solely via structural containment (`ip_addr in network`) can be bypassed when the network stack natively translates an allowed IPv6 block to a restricted IPv4 destination under the hood. Python's `ipaddress` library surfaces this via the `ipv4_mapped` property.
**Prevention:** Always extract and validate the underlying `ipv4_mapped` representation when filtering IP addresses for SSRF protection to ensure parity between filtering and execution layers.
