## 2024-05-24 - Unencrypted API Keys Over HTTP
**Vulnerability:** OpenWeatherMap API keys were being transmitted over unencrypted `http://` connections.
**Learning:** Even well-known external APIs might accept HTTP requests, allowing developers to inadvertently expose credentials over the network if not careful to use `https://`.
**Prevention:** Always default to HTTPS for any external request and audit code for `http://` patterns, especially when appending parameters like `appid` or `api_key`.
