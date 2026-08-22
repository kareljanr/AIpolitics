import urllib.request, ssl, re
from pathlib import Path

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

# Probe several leftover candidates
candidates = [
    ("dijk92", "https://www.northdata.com/Dijk92%20vzw,%20Brugge"),
    ("akapella", "https://www.northdata.com/Akapella%20Woonzorgcentrum"),
    ("buitenhof", "https://www.northdata.com/Buitenhof%20woonzorgcentrum"),
    ("familiehof", "https://www.northdata.com/Familiehof%20woonzorg"),
    ("hofschoten", "https://www.northdata.com/Hof%20van%20Schoten"),
]

for name, url in candidates:
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=40) as r:
            html = r.read().decode("utf-8", "replace")
            final = r.geturl()
        Path(f"docs/doge/raw/tick1743/nd_{name}.html").write_text(html, encoding="utf-8")
        deps = sorted(set(re.findall(r"2026-00\d{5,6}", html)))
        kbos = re.findall(r"KBO\s+0\d{3}\.\d{3}\.\d{3}", html)
        print(name, "url", final[:80], "len", len(html), "deps", deps[:6], "kbo", kbos[:3])
    except Exception as e:
        print(name, "FAIL", type(e).__name__, e)

# CDN probe known blocked
for dep in ["2026-00394221", "2026-00375176"]:
    u = f"http://cdn.staatsbladmonitor.be/2026pdf/{dep}.pdf"
    try:
        req = urllib.request.Request(u, headers=ua, method="HEAD")
        with urllib.request.urlopen(req, context=ctx, timeout=12) as r:
            print("CDN", dep, r.status)
    except Exception as e:
        print("CDN", dep, getattr(e, "code", e))
