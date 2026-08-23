# ephemeral tick1993 — deep parse CHBA + KBO + site
import re
from pathlib import Path

dst = Path("docs/doge/data/raw/tick1993")


def num_eu(s):
    s = s.replace("\xa0", "").replace(" ", "").replace(".", "").replace(",", ".")
    # EN uses comma as thousands: 1,441,066
    return s


def parse_amount(s):
    s = s.strip().replace("\xa0", " ").replace(" ", "")
    if "," in s and "." in s:
        # ambiguous
        if s.rfind(",") > s.rfind("."):
            s = s.replace(".", "").replace(",", ".")
        else:
            s = s.replace(",", "")
    elif "," in s:
        parts = s.split(",")
        if len(parts) == 2 and len(parts[1]) <= 2:
            s = s.replace(",", ".")
        else:
            s = s.replace(",", "")
    elif s.count(".") > 1:
        s = s.replace(".", "")
    return float(s)


for label in ["chba_en", "chba_nl"]:
    t = (dst / f"{label}.html").read_text(encoding="utf-8", errors="replace")
    blocks = re.findall(
        r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
        t,
    )
    print(label, "raw blocks", blocks[:3])
    parsed = [(parse_amount(a), parse_amount(b), parse_amount(c), parse_amount(d)) for a, b, c, d in blocks[:2]]
    print(label, "parsed winst,equity,bruto,omzet", parsed)
    if len(parsed) >= 2:
        y25, y24 = parsed[0], parsed[1]
        for name, i in [("winst", 0), ("equity", 1), ("bruto", 2), ("omzet", 3)]:
            a, b = y25[i], y24[i]
            if b != 0:
                pct = (a - b) / abs(b) * 100
            else:
                pct = None
            print(f"  {name}: {a:.0f} vs {b:.0f} -> {pct:.2f}%" if pct is not None else f"  {name}: {a} vs {b}")
    em = re.findall(r'Employees\s*=\s*"([^"]+)"', t)
    print("  FTE", em)
    for lab in ["filed on", "neergelegd op", "Last balance sheet year"]:
        i = t.find(lab)
        if i >= 0:
            print(" ", lab, repr(t[i : i + 160]))

# KBO
kbo = (dst / "chba_kbo.html").read_text(encoding="utf-8", errors="replace")
clean = re.sub(r"<[^>]+>", " ", kbo)
clean = re.sub(r"\s+", " ", clean)
for needle in [
    "Actief",
    "Rechtsvorm",
    "E-mail",
    "Webadres",
    "Aanbested",
    "Seraing",
    "Société",
    "cooperative",
    "cooperatieve",
    "CV",
    "SC",
    "Adresse",
    "Adres",
    "Beginn",
    "Datum van",
    "onderneming",
    "Entiteit",
]:
    i = clean.lower().find(needle.lower())
    if i >= 0:
        print("KBO", needle, repr(clean[max(0, i - 40) : i + 120]))

# site emails
site = (dst / "chba_site.html").read_text(encoding="utf-8", errors="replace")
emails = sorted(set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", site)))
print("site emails", emails[:25])
clean_s = re.sub(r"<[^>]+>", " ", site)
clean_s = re.sub(r"\s+", " ", clean_s)
for needle in ["contact", "info@", "communication", "Seraing", "Avenue", "Rue"]:
    i = clean_s.lower().find(needle.lower())
    if i >= 0:
        print("SITE", needle, repr(clean_s[max(0, i - 40) : i + 100]))
