from datetime import datetime, timezone
from pathlib import Path
n = datetime.now(timezone.utc)
stamp = n.strftime("%Y-%m-%dT%H:%M:%SZ")
day = n.strftime("%Y-%m-%d")
p = Path("/workspace/AIpolitics/docs/doge/data/_tick2429_stamp.txt")
p.write_text(stamp + "\n" + day + "\n")
print(stamp)
print(day)
