## 2025-02-17 - Fix SSRF vulnerabilities by enforcing secure request wrapper
**Vulnerability:** Several files in the codebase were directly importing the raw `requests` library, bypassing the custom `Requests` wrapper that prevents SSRF attacks.
**Learning:** The custom wrapper in `backend.util.request` is crucial for security as it blocks loopback, private IPs, and handles safe redirects. Bypassing it exposes the application to SSRF vulnerabilities.
**Prevention:** Always use the secure `Requests` wrapper (`from backend.util.request import requests`) for HTTP requests instead of the standard library directly.
