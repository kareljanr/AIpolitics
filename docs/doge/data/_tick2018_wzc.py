import re
import ssl
import urllib.request
from pathlib import Path

dst = Path("docs/doge/data/raw/tick2018")
ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}


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


def fetch(name, url):
    req = urllib.request.Request(url, headers=ua)
    with urllib.request.urlopen(req, context=ctx, timeout=45) as resp:
        data = resp.read()
    (dst / f"{name}.html").write_bytes(data)
    print("FETCH", name, len(data))
    return data.decode("utf-8", "replace")


for name, url in [
    ("barbara_nl", "https://www.companyweb.be/nl/0422152314/woonzorgcentrum-sint-barbara"),
    ("barbara_en", "https://www.companyweb.be/en/0422152314/woonzorgcentrum-sint-barbara"),
    ("barbara_fr", "https://www.companyweb.be/fr/0422152314/woonzorgcentrum-sint-barbara"),
    (
        "barbara_kbo",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0422152314",
    ),
]:
    t = fetch(name, url)
    if "kbo" in name:
        text = re.sub(r"<[^>]+>", " ", t)
        text = re.sub(r"\s+", " ", text)
        for kw in [
            "Status",
            "Actief",
            "0422",
            "Herselt",
            "vestiging",
            "Rechtsvorm",
            "Begin",
            "E-mail",
            "Web",
            "Aanbested",
        ]:
            i = text.lower().find(kw.lower())
            if i >= 0:
                print(kw, ":", text[max(0, i - 10) : i + 120])
    else:
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
        em = re.findall(r'Employees\s*=\s*"([^"]+)"', t)
        filed = None
        for lab in ["filed on", "neergelegd op"]:
            i = t.find(lab)
            if i >= 0:
                filed = t[i : i + 40]
        print(name, "year", year, "filed", filed, "FTE", em[:1])
        if blocks:
            y0 = tuple(parse_amount(x) for x in blocks[0])
            y1 = tuple(parse_amount(x) for x in blocks[1]) if len(blocks) > 1 else None
            print(" y0", y0)
            if y1:
                print(" y1", y1)
                for n, i in [("winst", 0), ("equity", 1), ("bruto", 2), ("omzet", 3)]:
                    a, b = y0[i], y1[i]
                    pct = (a - b) / abs(b) * 100 if b else None
                    print(
                        f"  {n} {a:.0f} vs {b:.0f} {pct:.2f}%"
                        if pct is not None
                        else f"  {n} {a} vs {b}"
                    )
