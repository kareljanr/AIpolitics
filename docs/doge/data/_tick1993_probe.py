# ephemeral tick1993 probe — year check FARO/AIESH/REW + CHBA + fetch fresh
import re
import ssl
import urllib.request
from pathlib import Path

dst = Path("docs/doge/data/raw/tick1993")
dst.mkdir(parents=True, exist_ok=True)
ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}


def parse(path: Path):
    t = path.read_text(encoding="utf-8", errors="replace")
    years = re.findall(r'data-year="(\d{4})"', t)
    blocks = re.findall(
        r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
        t,
    )
    title = re.search(r"<title>([^<]+)</title>", t)
    print(path.name)
    print("  title", (title.group(1)[:90] if title else None))
    print("  years", years[:8])
    print("  blocks", blocks[:4])
    for lab in [
        "filed on",
        "neergelegd op",
        "déposés le",
        "Last balance sheet year",
        "Last filed accounts",
        "Employees",
    ]:
        i = t.find(lab)
        if i >= 0:
            print(" ", lab, repr(t[i : i + 140]))
    em = re.findall(r'Employees\s*=\s*"([^"]+)"', t)
    print("  Employees attr", em[:4])
    # pct deltas near chart
    for needle in ["JUMP", "DROP", "%", "2025", "2024"]:
        pass
    print()


def fetch(name, url):
    req = urllib.request.Request(url, headers=ua)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=45) as r:
            data = r.read()
        (dst / f"{name}.html").write_bytes(data)
        print("FETCH", name, "OK", len(data))
        return dst / f"{name}.html"
    except Exception as e:
        print("FETCH", name, "FAIL", e)
        return None


# Prior caches year-check
for p in [
    Path("docs/doge/data/raw/tick1980/faro_cw.html"),
    Path("docs/doge/data/raw/tick1980/aiesh_cw.html"),
    Path("docs/doge/data/raw/tick1980/rew_cw.html"),
    Path("docs/doge/data/raw/tick1990/chba_cw_en.html"),
    Path("docs/doge/data/raw/tick1990/chba_cw_nl.html"),
]:
    if p.exists():
        parse(p)

# Fresh fetches for candidates
urls = [
    ("faro_en", "https://www.companyweb.be/en/0893863017/faro-vlaams-steunpunt-voor-cultureel-erfgoed"),
    ("aiesh_en", "https://www.companyweb.be/en/0201712587"),
    ("rew_en", "https://www.companyweb.be/en/0644638937"),
    ("chba_en", "https://www.companyweb.be/en/0203980409/centre-hospitalier-bois-de-l-abbaye"),
    ("chba_nl", "https://www.companyweb.be/nl/0203980409/centre-hospitalier-bois-de-l-abbaye"),
    ("chba_fr", "https://www.companyweb.be/fr/0203980409/centre-hospitalier-bois-de-l-abbaye"),
    ("chba_kbo", "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0203980409"),
    ("chba_site", "https://www.chba.be/"),
]

# Discover correct AIESH/REW numbers from prior HTML if our guesses fail
for label, prior in [
    ("aiesh", Path("docs/doge/data/raw/tick1980/aiesh_cw.html")),
    ("rew", Path("docs/doge/data/raw/tick1980/rew_cw.html")),
]:
    t = prior.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"companyweb\.be/(?:nl|en|fr)/(\d{10})/([^\"'?]+)", t)
    print(label, "discovered", m.group(0) if m else None, m.groups() if m else None)

print("--- fetching ---")
for name, url in urls:
    p = fetch(name, url)
    if p:
        parse(p)
