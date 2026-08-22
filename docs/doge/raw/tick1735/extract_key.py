import re
from pathlib import Path

t = Path("docs/doge/raw/tick1735/wzc_molenheide_extract.txt").read_text(encoding="utf-8")
parts = t.split("===== PAGE")

# pages 8-12 typically PnL
for i in range(8, 15):
    if i < len(parts):
        print("---PAGE", i)
        print(parts[i][:2200])
        print("====")

# audit opinion pages ~50-56
for i in range(50, 57):
    if i < len(parts):
        if re.search(r"oordeel|Oordeel|9904|9901|9087|subsid|Dividend|resultaat", parts[i], re.I):
            print("---PAGE", i)
            print(parts[i][:2500])
            print("====")

# VTE + 9087
for m in re.findall(r"9087.{0,80}", t):
    print("9087", m)
for m in re.findall(r"9901.{0,80}|9904.{0,80}|9903.{0,80}", t):
    print("pnl", m)
for m in re.findall(r"Dividend.{0,120}|694.{0,80}|kapitaalsubsid.{0,80}", t, re.I):
    print("div", m[:150])
