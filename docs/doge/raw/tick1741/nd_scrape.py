import urllib.request, ssl, re
from pathlib import Path

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

candidates = [
    ("vivalto", "https://www.northdata.com/VIVALTO%20HOME%20BELGIUM%20NV,%20Vorst/KBO%200820.420.456"),
    ("vivalto2", "https://www.northdata.com/Vivalto%20Home%20Belgium%20NV,%20Forest/KBO%200820.420.456"),
    ("verlosser", "https://www.northdata.com/Woonzorgcentrum%20De%20Verlosser%20VZW,%20Dilbeek/KBO%200446.340.946"),
    ("verlosser2", "https://www.northdata.com/WZC%20DV%20VZW,%20Dilbeek/KBO%200446.340.946"),
]

for name, url in candidates:
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=45) as r:
            html = r.read().decode("utf-8", "replace")
        Path(f"docs/doge/raw/tick1741/nd_{name}.html").write_text(html, encoding="utf-8")
        deps = sorted(set(re.findall(r"2026-00\d{5,6}", html)))
        titles = re.findall(r"publicationTitle&quot; : &quot;([^&]+)", html)
        print(name, "len", len(html), "deps", deps[:10])
        for t in titles[:6]:
            print(" ", t)
    except Exception as e:
        print(name, "FAIL", type(e).__name__, e)

# NSZ/APEFE quick CDN re-probe
for dep in ["2026-00394221", "2026-00375176"]:
    u = f"http://cdn.staatsbladmonitor.be/2026pdf/{dep}.pdf"
    try:
        req = urllib.request.Request(u, headers=ua, method="HEAD")
        with urllib.request.urlopen(req, context=ctx, timeout=15) as r:
            print("CDN", dep, r.status)
    except Exception as e:
        print("CDN", dep, type(e).__name__, getattr(e, "code", e))
