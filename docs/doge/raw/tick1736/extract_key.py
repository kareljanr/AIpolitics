import re
from pathlib import Path

t = Path("docs/doge/raw/tick1736/wzc_gravenkasteel_extract.txt").read_text(encoding="utf-8")
parts = t.split("===== PAGE")
print("---PAGE 5 full---")
print(parts[5] if len(parts) > 5 else "missing")
print("====")
for m in re.findall(r"9087.{0,100}", t):
    print("9087", m)
for m in re.findall(r"1003.{0,120}", t):
    print("1003", m)
for m in re.findall(r"Overlopende rekeningen 6\.8 492/3[^\n]*\n[^\n]*", t):
    print("overl", m)
# social balans page
for i, block in enumerate(parts):
    if re.search(r"9087|SOCIAAL|voltijdse equivalenten \(VTE\)|1003", block, re.I):
        if "9087" in block or "1003" in block or "SOCIALE BALANS" in block:
            print("---PAGE", i, "len", len(block))
            print(block[:2200])
            print("====")
