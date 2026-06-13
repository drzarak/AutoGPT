import pytest
from backend.util.request import _is_ip_blocked

def test_is_ip_blocked():
    # IPv4 loopback
    assert _is_ip_blocked("127.0.0.1") is True
    assert _is_ip_blocked("127.0.1.1") is True

    # IPv6 loopback
    assert _is_ip_blocked("::1") is True

    # IPv4 mapped IPv6 loopback
    assert _is_ip_blocked("::ffff:127.0.0.1") is True
    assert _is_ip_blocked("0:0:0:0:0:FFFF:127.0.0.1") is True

    # Private networks
    assert _is_ip_blocked("10.0.0.1") is True
    assert _is_ip_blocked("192.168.1.1") is True

    # Allowed IPs (e.g. public IPs like 8.8.8.8)
    assert _is_ip_blocked("8.8.8.8") is False
    assert _is_ip_blocked("1.1.1.1") is False
