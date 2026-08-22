from pathlib import Path
import re

t = Path("docs/doge/raw/tick1741/vivalto_extract.txt").read_text(encoding="utf-8")
parts = t.split("===== PAGE")
for i in range(8, 12):
    if i < len(parts):
        print("---PAGE", i)
        print(parts[i][:2200])
        print("====")
for m in re.findall(r"9087.{0,80}|9901.{0,80}|9904.{0,80}|9903.{0,80}", t):
    print(m)
