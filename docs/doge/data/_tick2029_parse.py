# ephemeral parse tick2029 Karus
import re
from pathlib import Path


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


for name in ["karus_nl", "karus_en", "karus_fr", "karus_kbo", "karus_site", "agb_en", "faro_en"]:
    p = Path(f"docs/doge/data/raw/tick2029/{name}.html")
    if not p.exists():
        print("MISS", name)
        continue
    html = p.read_text(encoding="utf-8", errors="replace")
    title = re.search(r"<title>([^<]+)</title>", html)
    print("==", name, (title.group(1)[:100] if title else None))
    year = None
    for lab in ["Last balance sheet year", "Laatste balansjaar", "Dernier bilan"]:
        i = html.find(lab)
        if i >= 0:
            m = re.search(r"font-medium[^>]*>\s*(\d{4}|N/A)", html[i : i + 220])
            if m:
                year = m.group(1)
    print(" year", year)
    blocks = re.findall(
        r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
        html,
    )
    print(" n", len(blocks))
    if blocks:
        y0 = tuple(parse_amount(x) for x in blocks[0])
        y1 = tuple(parse_amount(x) for x in blocks[1]) if len(blocks) > 1 else None
        print(" y0", y0)
        if y1:
            print(" y1", y1)
            for n, i in [("winst", 0), ("equity", 1), ("bruto", 2), ("omzet", 3)]:
                a, b = y0[i], y1[i]
                pct = (a - b) / abs(b) * 100 if b else None
                if pct is not None:
                    print(f"  {n} {a:.0f} vs {b:.0f} {pct:+.2f}%")
                else:
                    print(f"  {n} {a}")
    m2 = re.search(r'Employees\s*=\s*"([^"]+)"', html)
    print(" emp", m2.group(1) if m2 else None)
    for lab in ["filed on", "neergelegd op", "déposés le"]:
        j = html.lower().find(lab.lower())
        if j >= 0:
            print(" filed", html[j : j + 55])
            break
    emails = sorted(set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", html)))
    if "kbo" in name or "site" in name:
        print(" emails", emails[:8])
        t = re.sub(r"<[^>]+>", " ", html)
        t = re.sub(r"\s+", " ", t)
        for k in ["Adres van de zetel", "Rechtsvorm", "Status", "Melle", "Gent", "Deinze", "Karus"]:
            i = t.find(k)
            if i >= 0:
                print(" ", k, t[i : i + 110])
