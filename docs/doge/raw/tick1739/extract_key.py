from pathlib import Path
import re

t = Path("docs/doge/raw/tick1739/wzc_prinsenhof_extract.txt").read_text(encoding="utf-8")
parts = t.split("===== PAGE")
print("---PAGE 5---")
print(parts[5] if len(parts) > 5 else "missing")
print("====")
for m in re.findall(r"9087.{0,100}|1003.{0,120}", t):
    print(m)
for i, block in enumerate(parts):
    if "SOCIALE BALANS" in block or ("9087" in block and "Gemiddeld" in block):
        print("---PAGE", i)
        print(block[:2000])
        print("====")
