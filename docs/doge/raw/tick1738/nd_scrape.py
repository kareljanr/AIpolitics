import urllib.request, ssl, re
from pathlib import Path

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

candidates = [
    ("colisee", "https://www.northdata.com/Colis%C3%A9e%20Belgium%20NV,%20Sint-Gillis/KBO%200723.858.144"),
    ("colisee2", "https://www.northdata.com/Colisee%20Belgium%20NV,%20Saint-Gilles/KBO%200723.858.144"),
    ("prinsenhof", "https://www.northdata.com/WZC%20PRINSENHOF,%20Beringen/KBO%200644.497.395"),
]

for name, url in candidates:
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=45) as r:
            html = r.read().decode("utf-8", "replace")
        Path(f"docs/doge/raw/tick1738/nd_{name}.html").write_text(html, encoding="utf-8")
        deps = sorted(set(re.findall(r"2026-00\d{5,6}", html)))
        titles = re.findall(r"publicationTitle&quot; : &quot;([^&]+)", html)
        print(name, "len", len(html), "deps", deps[:8])
        for t in titles[:8]:
            print(" ", t)
    except Exception as e:
        print(name, "FAIL", type(e).__name__, e)

# also direct CDN probe known Prinsenhof deposit
for dep in ["2026-00176220"]:
    u = f"http://cdn.staatsbladmonitor.be/2026pdf/{dep}.pdf"
    try:
        req = urllib.request.Request(u, headers=ua, method="HEAD")
        with urllib.request.urlopen(req, context=ctx, timeout=20) as r:
            print("CDN", dep, r.status, r.headers.get("content-length"))
    except Exception as e:
        print("CDN", dep, type(e).__name__, getattr(e, "code", e))
