import re
from pathlib import Path

dst = Path("docs/doge/data/raw/tick2018")


def parse_amount(s):
    s = s.strip().replace("\xa0", " ").replace(" ", "")
    if "," in s and "." not in s:
        parts = s.split(",")
        if len(parts) >= 2 and all(len(p) == 3 for p in parts[1:]):
            s = s.replace(",", "")
        elif len(parts) == 2 and len(parts[1]) <= 2:
            s = s.replace(",", ".")
        else:
            s = s.replace(",", "")
    elif "," in s and "." in s:
        if s.rfind(",") > s.rfind("."):
            s = s.replace(".", "").replace(",", ".")
        else:
            s = s.replace(",", "")
    elif s.count(".") > 1:
        s = s.replace(".", "")
    return float(s)


for name in [
    "faro_en",
    "noorderhart_en",
    "noorderhart_nl",
    "sfz_en",
    "jessa_en",
    "zol_en",
    "aiesh_en",
    "rew_en",
]:
    path = dst / f"{name}.html"
    if not path.exists():
        print("MISS", name)
        continue
    t = path.read_text(encoding="utf-8", errors="replace")
    title = re.search(r"<title>([^<]+)</title>", t)
    year = None
    for lab in ["Last balance sheet year", "Laatste balansjaar"]:
        i = t.find(lab)
        if i >= 0:
            m = re.search(r"font-medium[^>]*>\s*(\d{4}|N/A)", t[i : i + 220])
            if m:
                year = m.group(1)
    blocks = re.findall(
        r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
        t,
    )
    filed = None
    for lab in ["filed on", "neergelegd op"]:
        i = t.find(lab)
        if i >= 0:
            filed = t[i : i + 45]
    print("==", name, "==", (title.group(1)[:90] if title else None))
    print(" year", year, "filed", filed, "nblocks", len(blocks))
    if blocks:
        try:
            y0 = tuple(parse_amount(x) for x in blocks[0])
            print(" y0", y0)
            if len(blocks) > 1:
                y1 = tuple(parse_amount(x) for x in blocks[1])
                print(" y1", y1)
                for n, i in [("winst", 0), ("equity", 1), ("bruto", 2), ("omzet", 3)]:
                    a, b = y0[i], y1[i]
                    pct = (a - b) / abs(b) * 100 if b else None
                    print(
                        f"  {n} {a:.0f} vs {b:.0f} {pct:.2f}%"
                        if pct is not None
                        else f"  {n} {a} vs {b}"
                    )
        except Exception as e:
            print(" err", e)
    print()
