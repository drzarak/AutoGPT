from autogpt_platform.backend.backend.util.request import _is_ip_blocked, validate_url

print(_is_ip_blocked("::ffff:127.0.0.1"))
try:
    print(validate_url("http://[::ffff:127.0.0.1]", []))
except Exception as e:
    print(f"Error: {e}")
