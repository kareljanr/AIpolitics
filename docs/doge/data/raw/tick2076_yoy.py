from pathlib import Path
import re
t = Path(r"docs/doge/data/raw/tick2076/agb_bornem_check.html").read_text(encoding="utf-8", errors="replace")
m = re.search(r"window\.cw\.kernCijfers = \{(.{0,120})", t, re.S)
print("kern", m.group(1)[:100] if m else "no")
filed = re.search(r"filed on ([0-9-]+)", t)
print("filed", filed.group(1) if filed else None)
print("len", len(t))
# FARO/AIESH/REW already confirmed YE2024
print("YoY checks:")
omzet25, omzet24 = 16399438, 15801877
pnl25, pnl24 = -179732, -165145
eq25, eq24 = 14293709, 14515487
br25, br24 = 15744392, 15252404
fte25, fte24 = 215.9, 219.1
def yoy(a,b):
    return (a-b)/abs(b)*100
print("omzet", f"{yoy(omzet25,omzet24):+.2f}%")
print("pnl deeper", f"{yoy(abs(pnl25),abs(pnl24)):+.2f}% magnitude")
print("equity", f"{yoy(eq25,eq24):+.2f}%")
print("bruto", f"{yoy(br25,br24):+.2f}%")
print("fte", f"{yoy(fte25,fte24):+.2f}%")
