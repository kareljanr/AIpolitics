# ephemeral tick1998 — fetch ZAS YE2025 + KBO + site
import re
import ssl
import urllib.request
from pathlib import Path

dst = Path("docs/doge/data/raw/tick1998")
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
    path = dst / f"{name}.html"
    if not path.exists():
        print("MISSING", name)
        return
    t = path.read_text(encoding="utf-8", errors="replace")
    title = re.search(r"<title>([^<]+)</title>", t)
    blocks = re.findall(
        r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
        t,
    )
    print("==", name, "==")
    print(" title", (title.group(1)[:130] if title else None))
    print(" blocks", blocks[:3])
    for lab in ["Last balance sheet year", "filed on", "neergelegd op", "déposés le"]:
        i = t.find(lab)
        if i >= 0:
            print(" ", lab, repr(t[i : i + 140]))
    em = re.findall(r'Employees\s*=\s*"([^"]+)"', t)
    print(" FTE", em[:3])
    if blocks:
        y0 = tuple(parse_amount(x) for x in blocks[0])
        print(" y0 winst,equity,bruto,omzet", y0)
        if len(blocks) > 1:
            y1 = tuple(parse_amount(x) for x in blocks[1])
            print(" y1", y1)
            for n, i in [("winst", 0), ("equity", 1), ("bruto", 2), ("omzet", 3)]:
                a, b = y0[i], y1[i]
                pct = (a - b) / abs(b) * 100 if b else None
                print(f"  {n} {a:.0f} vs {b:.0f} {pct:.2f}%" if pct is not None else f"  {n} {a} vs {b}")
    print()


urls = [
    ("zas_en", "https://www.companyweb.be/en/0862382656/ziekenhuis-aan-de-stroom"),
    ("zas_nl", "https://www.companyweb.be/nl/0862382656/ziekenhuis-aan-de-stroom"),
    ("zas_fr", "https://www.companyweb.be/fr/0862382656/ziekenhuis-aan-de-stroom"),
    ("zas_kbo", "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0862382656"),
    ("zas_site", "https://www.zas.be/"),
    ("azjp_en", "https://www.companyweb.be/en/0262926616"),
    ("azjp_nl", "https://www.companyweb.be/nl/0262926616"),
]
for name, url in urls:
    try:
        fetch(name, url)
    except Exception as e:
        print("FAIL", name, e)

for name in ["zas_en", "zas_nl", "zas_fr", "azjp_en"]:
    summarize(name)

kbo = (dst / "zas_kbo.html").read_text(encoding="utf-8", errors="replace")
clean = re.sub(r"<[^>]+>", " ", kbo)
clean = re.sub(r"\s+", " ", clean)
for needle in [
    "Actief",
    "Rechtsvorm",
    "E-mail",
    "Webadres",
    "Aanbested",
    "Ziekenhuis",
    "Stroom",
    "vestiging",
    "Begin datum",
]:
    i = clean.find(needle)
    if i >= 0:
        print("KBO", needle, clean[i : i + 180])

site = (dst / "zas_site.html").read_text(encoding="utf-8", errors="replace")
emails = sorted(set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", site)))
print("site emails", emails[:20])
print("site title", re.search(r"<title>([^<]+)</title>", site).group(1)[:100] if re.search(r"<title>", site) else None)
