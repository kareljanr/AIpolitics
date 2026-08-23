import re
import ssl
import urllib.request
from pathlib import Path

dst = Path("docs/doge/data/raw/tick2015")
dst.mkdir(parents=True, exist_ok=True)
ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}


def fetch(name, url):
    req = urllib.request.Request(url, headers=ua)
    with urllib.request.urlopen(req, context=ctx, timeout=45) as resp:
        data = resp.read()
    (dst / f"{name}.html").write_bytes(data)
    print("FETCH", name, len(data))


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
    t = (dst / f"{name}.html").read_text(encoding="utf-8", errors="replace")
    title = re.search(r"<title>([^<]+)</title>", t)
    blocks = re.findall(
        r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
        t,
    )
    # also kernCijfers year keys
    years = re.findall(r"kernCijfers\s*=\s*\{\s*(\d{4})\s*:", t)
    print("==", name, "==", (title.group(1)[:100] if title else None), "years", years[:4])
    for lab in ["Last balance sheet year", "filed on", "neergelegd op", "Laatste balansjaar"]:
        i = t.find(lab)
        if i >= 0:
            print(" ", lab, repr(re.sub(r"\s+", " ", t[i : i + 120])[:140]))
    em = re.findall(r'Employees\s*=\s*"([^"]+)"', t)
    print(" FTE", em[:2], "blocks", len(blocks))
    if blocks:
        y0 = tuple(parse_amount(x) for x in blocks[0])
        print(" y0", y0)
        if len(blocks) > 1:
            y1 = tuple(parse_amount(x) for x in blocks[1])
            print(" y1", y1)
            for n, i in [("winst", 0), ("equity", 1), ("bruto", 2), ("omzet", 3)]:
                a, b = y0[i], y1[i]
                pct = (a - b) / abs(b) * 100 if b else None
                print(f"  {n} {a:.0f} vs {b:.0f} {pct:.2f}%" if pct is not None else f"  {n} {a} vs {b}")
    ems = set(
        re.findall(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            t,
        )
    )
    ems = {
        e
        for e in ems
        if not any(
            x in e.lower()
            for x in ["example", "sentry", "schema", "w3.org", "companyweb", "fontawesome"]
        )
    }
    if ems:
        print(" emails", sorted(ems)[:8])
    print()


urls = [
    ("hhtienen_en", "https://www.companyweb.be/en/0408228557/regionaal-ziekenhuis-heilig-hart-tienen"),
    ("hhtienen_nl", "https://www.companyweb.be/nl/0408228557/regionaal-ziekenhuis-heilig-hart-tienen"),
    ("hhtienen_fr", "https://www.companyweb.be/fr/0408228557/regionaal-ziekenhuis-heilig-hart-tienen"),
    ("hhtienen_kbo", "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0408228557"),
    ("hhtienen_site", "https://www.hhtienen.be/"),
]
for name, url in urls:
    try:
        fetch(name, url)
    except Exception as e:
        print("FAIL", name, e)

for name, _ in urls:
    if (dst / f"{name}.html").exists():
        summarize(name)
