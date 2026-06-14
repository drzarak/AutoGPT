import pytest

import socket

from backend.util.request import validate_url


def test_validate_url():
    # Rejected IP ranges
    with pytest.raises(ValueError):
        validate_url("localhost", [])

    with pytest.raises(ValueError):
        validate_url("192.168.1.1", [])

    with pytest.raises(ValueError):
        validate_url("127.0.0.1", [])

    with pytest.raises(ValueError):
        validate_url("0.0.0.0", [])

    # Normal URLs
    assert validate_url("google.com/a?b=c", []) == "http://google.com/a?b=c"
    assert validate_url("github.com?key=!@!@", []) == "http://github.com?key=!@!@"

    # Scheme Enforcement
    with pytest.raises(ValueError):
        validate_url("ftp://example.com", [])
    with pytest.raises(ValueError):
        validate_url("file://example.com", [])

    # International domain that converts to punycode - should be allowed if public
    assert validate_url("http://xn--exmple-cua.com", []) == "http://xn--exmple-cua.com"
    # If the domain fails IDNA encoding or is invalid, it should raise an error
    with pytest.raises(ValueError):
        validate_url("http://exa◌mple.com", [])

    # IPv6 Addresses
    with pytest.raises(ValueError):
        validate_url("::1", [])  # IPv6 loopback should be blocked
    with pytest.raises(ValueError):
        validate_url("http://[::1]", [])  # IPv6 loopback in URL form

    # Suspicious Characters in Hostname
    with pytest.raises(ValueError):
        validate_url("http://example_underscore.com", [])
    with pytest.raises(ValueError):
        validate_url("http://exa mple.com", [])  # Space in hostname

    # Malformed URLs
    with pytest.raises(ValueError):
        validate_url("http://", [])  # No hostname
    with pytest.raises(ValueError):
        validate_url("://missing-scheme", [])  # Missing proper scheme

    # Trusted Origins
    trusted = ["internal-api.company.com", "10.0.0.5"]
    assert (
        validate_url("internal-api.company.com", trusted)
        == "http://internal-api.company.com"
    )
    assert validate_url("10.0.0.5", ["10.0.0.5"]) == "http://10.0.0.5"

    # Special Characters in Path or Query
    assert (
        validate_url("example.com/path%20with%20spaces", [])
        == "http://example.com/path%20with%20spaces"
    )

    # Backslashes should be replaced with forward slashes
    assert (
        validate_url("http://example.com\\backslash", [])
        == "http://example.com/backslash"
    )

    # Check defaulting scheme behavior for valid domains
    assert validate_url("example.com", []) == "http://example.com"
    assert validate_url("https://secure.com", []) == "https://secure.com"

    # Non-ASCII Characters in Query/Fragment
    assert validate_url("example.com?param=äöü", []) == "http://example.com?param=äöü"


def test_validate_url_ipv4_mapped_ipv6(monkeypatch):
    """
    Test that DNS names resolving to IPv4-mapped IPv6 addresses are blocked.
    Using a monkeypatch on socket.getaddrinfo to simulate such DNS resolution.
    """
    original_getaddrinfo = socket.getaddrinfo

    def mock_getaddrinfo(host, port, *args, **kwargs):
        if host == "ssrf-mapped-loopback.example.com":
            return [(socket.AF_INET6, 0, 0, "", ("::ffff:127.0.0.1", port, 0, 0))]
        if host == "ssrf-mapped-private.example.com":
            return [(socket.AF_INET6, 0, 0, "", ("::ffff:192.168.1.1", port, 0, 0))]
        return original_getaddrinfo(host, port, *args, **kwargs)

    monkeypatch.setattr(socket, "getaddrinfo", mock_getaddrinfo)

    with pytest.raises(ValueError, match="Access to blocked or private IP"):
        validate_url("http://ssrf-mapped-loopback.example.com", [])

    with pytest.raises(ValueError, match="Access to blocked or private IP"):
        validate_url("http://ssrf-mapped-private.example.com", [])
