
## 2024-06-30 - [SSRF Bypass via IPv4-Mapped IPv6 Addresses]
**Vulnerability:** The SSRF protection in `backend/util/request.py` blocked IPv4 loopback/private addresses but failed to handle IPv4-mapped IPv6 addresses (e.g., `::ffff:127.0.0.1`), allowing an attacker to bypass the IP filters and access internal services by resolving domains to mapped IPv6 addresses.
**Learning:** `ipaddress.ip_address` correctly parses mapped addresses into IPv6 objects, which do not inherently match IPv4 network ranges in `BLOCKED_IP_NETWORKS` unless explicitly unwrapped using the `.ipv4_mapped` property.
**Prevention:** Always check and extract the underlying IPv4 address from parsed IP addresses using `getattr(ip_addr, 'ipv4_mapped', None)` before applying blocklist/allowlist validations against IPv4 subnets.
