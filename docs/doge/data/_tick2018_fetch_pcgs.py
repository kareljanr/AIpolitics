# fetch PCGS NL/EN/FR + KBO + site + a few more unused with correct KBOs
import re
import ssl
import urllib.request
from pathlib import Path

dst = Path("docs/doge/data/raw/tick2018")
dst.mkdir(parents=True, exist_ok=True)
ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}


def fetch(name, url):
    req = urllib.request.Request(url, headers=ua)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=45) as resp:
            data = resp.read()
        (dst / f"{name}.html").write_bytes(data)
        print("FETCH", name, len(data), url)
        return data
    except Exception as e:
        print("FAIL", name, e, url)
        return None


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


def summarize(name):
    path = dst / f"{name}.html"
    if not path.exists():
        return
    t = path.read_text(encoding="utf-8", errors="replace")
    title = re.search(r"<title>([^<]+)</title>", t)
    blocks = re.findall(
        r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
        t,
    )
    print("==", name, "==", (title.group(1)[:120] if title else None))
    for lab in [
        "Last balance sheet year",
        "filed on",
        "neergelegd op",
        "Laatste balansjaar",
        "Adres van de zetel",
        "Aantal vestigingseenheden",
        "Start van de rechtspersoon",
        "Juridische vorm",
    ]:
        i = t.find(lab)
        if i >= 0:
            print(" ", lab, repr(t[i : i + 180].replace("\n", " ").replace("\t", " ")[:160]))
    em = re.findall(r'Employees\s*=\s*"([^"]+)"', t)
    print(" FTE", em[:2], "n_blocks", len(blocks))
    emails = sorted(set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", t)))
    print(" emails", [e for e in emails if "sentry" not in e.lower()][:8])
    if blocks:
        try:
            y0 = tuple(parse_amount(x) for x in blocks[0])
            print(" y0 winst/equity/bruto/omzet", y0)
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
            print(" parse err", e)


targets = [
    ("pcgs_en", "https://www.companyweb.be/en/0837845517"),
    ("pcgs_nl", "https://www.companyweb.be/nl/0837845517"),
    ("pcgs_fr", "https://www.companyweb.be/fr/0837845517"),
    (
        "pcgs_kbo",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0837845517",
    ),
    ("pcgs_site", "https://www.pcgs.be/"),
    # alternates if PCGS fails
    ("uz_gent_en", "https://www.companyweb.be/en/0232987862"),
    ("az_oudenaarde_en", "https://www.companyweb.be/en/0870757023"),
    ("maria_middelares_en", "https://www.companyweb.be/en/0410214186"),
    ("az_sint_lucas_gent_en", "https://www.companyweb.be/en/0406477468"),
]

for name, url in targets:
    fetch(name, url)
print("---SUM---")
for name, _ in targets:
    summarize(name)

# Bornem page text snippet
bp = dst / "bornem_jr.html"
if bp.exists():
    t = bp.read_text(encoding="utf-8", errors="replace")
    for yr in ("2025", "2024"):
        print("bornem mentions", yr, t.count(yr))
