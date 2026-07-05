## 2024-07-05 - [SSRF bypass via IPv4-mapped IPv6]
**Vulnerability:** A vulnerability was found in the `validate_url` function logic preventing Server-Side Request Forgery (SSRF). Attackers could use IPv4-mapped IPv6 addresses (e.g., `::ffff:127.0.0.1`) to bypass security filters that only check against standard IPv4 blocklists.
**Learning:** Python's `ipaddress` library handles `IPv4Address` and `IPv6Address` natively. However, to compare `IPv4-mapped IPv6 addresses` properly against IPv4 subnets, we need to extract the underlying IPv4 address manually.
**Prevention:** Always check and extract the underlying IPv4 address from IPv6 objects using the `.ipv4_mapped` property. Utilize `getattr(ip_addr, 'ipv4_mapped', None)` safely, as the property does not exist on IPv4 objects natively.
