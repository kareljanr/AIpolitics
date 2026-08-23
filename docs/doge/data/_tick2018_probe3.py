# probe Bornem official + more unused hospital KBOs with omzet potential
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
    ]:
        i = t.find(lab)
        if i >= 0:
            print(" ", lab, repr(t[i : i + 140].replace("\n", " ")))
    em = re.findall(r'Employees\s*=\s*"([^"]+)"', t)
    print(" FTE", em[:2], "n_blocks", len(blocks))
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


# Bornem official
data = fetch("bornem_jr", "https://www.bornem.be/jaarrekening-gemeente-ocmw-en-agb")
if data:
    t = data.decode("utf-8", "replace")
    links = re.findall(r'href=["\']([^"\']+)["\']', t)
    for L in links:
        if any(x in L.lower() for x in ("jaar", "2025", "2024", ".pdf", "agb")):
            print(" LINK", L[:180])

targets = [
    ("az_turnhout_en", "https://www.companyweb.be/en/0897191602"),
    ("az_waregem_en", "https://www.companyweb.be/en/0405608035"),  # guess may 404
    ("az_yperman_en", "https://www.companyweb.be/en/0411989726"),
    ("az_zottegem_en", "https://www.companyweb.be/en/0405638952"),
    ("az_diest_en", "https://www.companyweb.be/en/0405633281"),
    ("az_oudenaarde_en", "https://www.companyweb.be/en/0411687705"),
    ("az_sint_lucas_brugge_en", "https://www.companyweb.be/en/0405675785"),
    ("uz_gent_en", "https://www.companyweb.be/en/0236985729"),
    ("uz_antwerpen_en", "https://www.companyweb.be/en/0416680135"),
    ("az_sint_nikolaas_en", "https://www.companyweb.be/en/0411698467"),
    # unused IGS/HVZ/water-ish not on skip list — try Fluvius Antwerpen / PBE / IWVA / Pidpa?
    ("pidpa_en", "https://www.companyweb.be/en/0204520381"),
    ("iwva_en", "https://www.companyweb.be/en/0204503501"),
    ("pbe_en", "https://www.companyweb.be/en/0204500476"),
]

for name, url in targets:
    fetch(name, url)
print("---SUM---")
for name, _ in targets:
    summarize(name)
