#!/usr/bin/env python3
from datetime import datetime, timezone
from pathlib import Path
NOW = datetime.now(timezone.utc)
STAMP = NOW.strftime("%Y-%m-%dT%H:%M:%SZ")
DAY = NOW.strftime("%Y-%m-%d")
Path("/workspace/AIpolitics/docs/doge/data/_tick2387_stamp.txt").write_text(STAMP + "\n" + DAY + "\n")
print(STAMP, DAY)
