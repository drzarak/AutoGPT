
## 2024-05-20 - SSRF Bypass via IPv4-Mapped IPv6
**Vulnerability:** A mechanism used to block SSRF requests to localhost and internal IPv4 addresses was bypassed by supplying IPv4-Mapped IPv6 addresses (e.g. `::ffff:127.0.0.1`), which would result in `_is_ip_blocked` returning False because the IPv6 object didn't match the blocked IPv4 networks.
**Learning:** `ipaddress.IPv6Address` network checks don't automatically extract mapped IPv4 components. This is a common and subtle pitfall when creating IP blocklists.
**Prevention:** Always check `getattr(ip_addr, 'ipv4_mapped', None)` when using the `ipaddress` module to process user-supplied IPs to safely normalize mapped IPv6-to-IPv4 structures before evaluating against access control lists.
