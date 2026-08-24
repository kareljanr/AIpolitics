import re
from pathlib import Path
t=Path("docs/doge/data/raw/tick2166/anima_hold_en.html").read_text(encoding="utf-8",errors="replace")
title=re.search(r"<title>([^<]+)",t)
print("title", title.group(1) if title else None)
yblocks={}
for y, body in re.findall(r"(20\d\d)\s*:\s*\{([^{}]+)\}", t):
    def g(k, b=body):
        m=re.search(rf'{k}:\s*"([^"]*)"', b)
        return m.group(1) if m else None
    yblocks[y]={k:g(k) for k in ["omzet","winst","bruto_marge","eigen_vermogen"]}
print("years", sorted(yblocks))
for y in sorted(yblocks, reverse=True)[:3]:
    print(y, yblocks[y])
fte=re.search(r"([\d.,]+)\s*FTE", t)
filed=re.search(r"filed on ([0-9-]{10})", t)
print("fte", fte.group(1) if fte else None, "filed", filed.group(1) if filed else None)
h1=re.search(r"<h1[^>]*>([^<]+)",t)
print("h1", h1.group(1) if h1 else None)
for label in ["faro","aiesh","rew","lork_hoeselt","anima_hold"]:
    t2=Path(f"docs/doge/data/raw/tick2166/{label}_en.html").read_text(encoding="utf-8",errors="replace")
    yb={}
    for y, body in re.findall(r"(20\d\d)\s*:\s*\{([^{}]+)\}", t2):
        def g(k, b=body):
            m=re.search(rf'{k}:\s*"([^"]*)"', b)
            return m.group(1) if m else None
        yb[y]={k:g(k) for k in ["omzet","winst","bruto_marge","eigen_vermogen"]}
    filed=re.search(r"filed on ([0-9-]{10})", t2)
    print(label, "filed", filed.group(1) if filed else None)
    for y in sorted(yb, reverse=True)[:2]:
        print(" ",y,yb[y])
