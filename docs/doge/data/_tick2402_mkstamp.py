from datetime import datetime, timezone
from pathlib import Path
now = datetime.now(timezone.utc).replace(microsecond=0)
stamp = now.strftime("%Y-%m-%dT%H:%M:%SZ")
day = now.strftime("%Y-%m-%d")
p = Path("/workspace/AIpolitics/docs/doge/data/_tick2402_stamp.txt")
p.write_text(stamp + "\n" + day + "\n", encoding="utf-8")
print(stamp)
print(day)
