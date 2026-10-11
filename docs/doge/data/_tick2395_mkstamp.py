from datetime import datetime, timezone
n = datetime.now(timezone.utc)
print(n.strftime("%Y-%m-%dT%H:%M:%SZ"))
print(n.strftime("%Y-%m-%d"))
