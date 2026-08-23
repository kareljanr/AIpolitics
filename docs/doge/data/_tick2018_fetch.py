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
    ("molenheide_nl", "https://www.companyweb.be/nl/0810616132/molenheide-woonzorgcentrum"),
    ("molenheide_en", "https://www.companyweb.be/en/0810616132/molenheide-woonzorgcentrum"),
    ("molenheide_fr", "https://www.companyweb.be/fr/0810616132/molenheide-woonzorgcentrum"),
    (
        "molenheide_kbo",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0810616132",
    ),
]:
    t = fetch(name, url)
    if "kbo" in name:
        text = re.sub(r"<[^>]+>", " ", t)
        text = re.sub(r"\s+", " ", text)
        for kw in ["Status", "Actief", "0810", "Wijnegem", "vestiging", "Rechtsvorm", "Begin", "E-mail"]:
            i = text.lower().find(kw.lower())
            if i >= 0:
                print(kw, ":", text[max(0, i - 10) : i + 110])
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
        print(name, "year", year, "FTE", em[:1], "blocks", blocks[:2])
        if blocks:
            y0 = tuple(parse_amount(x) for x in blocks[0])
            y1 = tuple(parse_amount(x) for x in blocks[1]) if len(blocks) > 1 else None
            print(" y0", y0)
            if y1:
                print(" y1", y1)
