
## 2024-06-24 - [IPv4-mapped IPv6 SSRF Bypass]
**Vulnerability:** The custom HTTP request wrapper used to prevent Server-Side Request Forgery (SSRF) failed to explicitly unwrap IPv4-mapped IPv6 addresses (e.g. `::ffff:127.0.0.1`).
**Learning:** Python's `ipaddress` module parses `::ffff:127.0.0.1` as a valid IPv6 address, and when checked against blocked IPv4 networks using `in`, it evaluates to `False`. Attackers could exploit this behavior to bypass network blocklists.
**Prevention:** Always extract the underlying IPv4 address from parsed IP addresses using the `.ipv4_mapped` property (safely, via `getattr` to handle pure IPv4 addresses) before evaluating them against blocklists.
