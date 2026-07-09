## 2024-07-09 - Fix SSRF bypass via IPv4-mapped IPv6 Addresses
**Vulnerability:** The SSRF protection logic (`_is_ip_blocked`) did not adequately block requests mapped to IPv6 loopback addresses via IPv4-mapping (e.g., `::ffff:127.0.0.1`), allowing potential circumvention of the internal service filters.
**Learning:** Python's `ipaddress` module requires checking and extracting the underlying IPv4 address from an IPv6 object if it is an IPv4-mapped address, otherwise it won't match against typical IPv4 blocklists.
**Prevention:** Always extract and evaluate the underlying `.ipv4_mapped` address when validating IPs for SSRF defense, by safely querying the property (e.g., using `getattr(ip, 'ipv4_mapped', None)`).
