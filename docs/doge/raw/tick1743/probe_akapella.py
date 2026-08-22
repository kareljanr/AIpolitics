import urllib.request, ssl, re
from pathlib import Path

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0"}
url = "https://www.northdata.com/Akapella%20Woonzorgcentrum%20VZW,%20Belgium/KBO%200870.764.941"
# also try from previous search page
for u in [
    "https://www.northdata.com/Akapella%20Woonzorgcentrum/KBO%200870.764.941",
    "https://www.northdata.com/search?q=0870764941",
]:
    try:
        req = urllib.request.Request(u, headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=40) as r:
            html = r.read().decode("utf-8", "replace")
        deps = sorted(set(re.findall(r"2026-00\d{5,6}", html)))
        print(u[:70], "len", len(html), "deps", deps)
        for t in re.findall(r"publicationTitle&quot; : &quot;([^&]+)", html)[:8]:
            print(" ", t)
    except Exception as e:
        print("fail", u[:50], type(e).__name__, e)

# CDN HEAD
dep = "2026-00139430"
u = f"http://cdn.staatsbladmonitor.be/2026pdf/{dep}.pdf"
try:
    req = urllib.request.Request(u, headers=ua, method="HEAD")
    with urllib.request.urlopen(req, context=ctx, timeout=20) as r:
        print("CDN", dep, r.status, r.headers.get("content-length"))
except Exception as e:
    print("CDN", dep, type(e).__name__, getattr(e, "code", e))

# also Hof ter Waarbeek
for label, kbo in [("waarbeek", "0478728256"), ("walfergem", "0633687439")]:
    url = f"https://www.northdata.com/search?q={kbo}"
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=30) as r:
            html = r.read().decode("utf-8", "replace")
        deps = sorted(set(re.findall(r"2026-00\d{5,6}", html)))
        print(label, "deps", deps[:8], "len", len(html))
    except Exception as e:
        print(label, type(e).__name__, e)
