## 2023-10-27 - SSRF Bypass via IPv4-mapped IPv6 Addresses
**Vulnerability:** A Server-Side Request Forgery (SSRF) blocklist bypass existed in `backend/util/request.py`. The `_is_ip_blocked` function used `ipaddress.ip_address` to parse IPs but failed to check for IPv4-mapped IPv6 addresses (e.g., `::ffff:127.0.0.1`).
**Learning:** Python's `ipaddress` module parses `::ffff:127.0.0.1` as a valid IPv6 address, which then fails to match IPv4 network blocklists (like `127.0.0.0/8`), allowing an attacker to request private network resources.
**Prevention:** When validating IP addresses against blocklists, always extract the underlying IPv4 address from IPv6 objects using the `.ipv4_mapped` property before performing network containment checks.
