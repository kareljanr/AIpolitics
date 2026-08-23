# ephemeral tick2000 — fetch Z.org KU Leuven NL/FR/KBO/site + parse
import re
import ssl
import urllib.request
from pathlib import Path

dst = Path("docs/doge/data/raw/tick2000")
dst.mkdir(parents=True, exist_ok=True)
ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}


def fetch(name, url):
    req = urllib.request.Request(url, headers=ua)
    with urllib.request.urlopen(req, context=ctx, timeout=45) as resp:
        data = resp.read()
    (dst / f"{name}.html").write_bytes(data)
    print("FETCH", name, len(data), url)


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
    t = path.read_text(encoding="utf-8", errors="replace")
    title = re.search(r"<title>([^<]+)</title>", t)
    blocks = re.findall(
        r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
        t,
    )
    print("==", name, "==")
    print(" title", (title.group(1)[:120] if title else None))
    print(" blocks", blocks[:3])
    for lab in ["Last balance sheet year", "filed on", "neergelegd op", "déposés le", "Laatste balansjaar"]:
        i = t.find(lab)
        if i >= 0:
            print(" ", lab, repr(t[i : i + 180].replace("\n", " ")))
    em = re.findall(r'Employees\s*=\s*"([^"]+)"', t)
    print(" FTE", em[:3])
    if blocks:
        y0 = tuple(parse_amount(x) for x in blocks[0])
        y1 = tuple(parse_amount(x) for x in blocks[1]) if len(blocks) > 1 else None
        print(" y0", y0)
        print(" y1", y1)
        if y1:
            for n, i in [("winst", 0), ("equity", 1), ("bruto", 2), ("omzet", 3)]:
                a, b = y0[i], y1[i]
                pct = (a - b) / abs(b) * 100 if b else None
                print(f"  {n} {a:.0f} vs {b:.0f} {pct:.2f}%" if pct is not None else f"  {n} {a} vs {b}")
    print()


urls = [
    ("zorg_kul_nl", "https://www.companyweb.be/nl/0558906971/z-org-ku-leuven"),
    ("zorg_kul_fr", "https://www.companyweb.be/fr/0558906971/z-org-ku-leuven"),
    ("zorg_kul_en", "https://www.companyweb.be/en/0558906971/z-org-ku-leuven"),
    ("zorg_kul_kbo", "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0558906971"),
    ("zorg_kul_site", "https://www.uzleuven.be/nl/zorg-ku-leuven"),
    ("uzleuven_site", "https://www.uzleuven.be/"),
]

for name, url in urls:
    try:
        fetch(name, url)
    except Exception as e:
        print("FAIL", name, e)

for name in ["zorg_kul_nl", "zorg_kul_fr", "zorg_kul_en"]:
    summarize(name)

kbo = (dst / "zorg_kul_kbo.html").read_text(encoding="utf-8", errors="replace")
clean = re.sub(r"<[^>]+>", " ", kbo)
clean = re.sub(r"\s+", " ", clean)
for needle in ["Actief", "Rechtsvorm", "E-mail", "Webadres", "Aanbested", "Herestraat", "vestiging", "psychiatr"]:
    i = clean.lower().find(needle.lower())
    if i >= 0:
        print("KBO", needle, repr(clean[max(0, i - 40) : i + 140]))

for site_name in ["zorg_kul_site", "uzleuven_site"]:
    p = dst / f"{site_name}.html"
    if p.exists():
        site = p.read_text(encoding="utf-8", errors="replace")
        emails = sorted(set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", site)))
        print(site_name, "emails", [e for e in emails if not any(x in e.lower() for x in ["sentry", "wix", "example", "schema"])][:20])
        print(site_name, "title", re.search(r"<title>([^<]+)</title>", site).group(1)[:100] if re.search(r"<title>", site) else None)
