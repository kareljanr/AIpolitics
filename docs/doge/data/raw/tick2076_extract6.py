from pathlib import Path
import re
t = Path(r"docs/doge/data/raw/tick2075/kuurne_en.html").read_text(encoding="utf-8", errors="replace")
idx = t.find("Average number of staff")
print(t[idx:idx+1200])
