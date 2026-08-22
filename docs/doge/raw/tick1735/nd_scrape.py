import urllib.request, ssl, re
from pathlib import Path

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

# Molenheide WZC Wijnegem KBO 0810.616.132
urls = [
    "https://www.northdata.com/MOLENHEIDE%20WZC,%20Wijnegem/KBO%200810.616.132",
    "https://www.northdata.com/Molenheide%20Woonzorgcentrum,%20Wijnegem/KBO%200810.616.132",
]
for url in urls:
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=60) as r:
            html = r.read().decode("utf-8", "replace")
        out = Path("docs/doge/raw/tick1735/nd_molenheide.html")
        out.write_text(html, encoding="utf-8")
        print("url", url[:70], "len", len(html))
        deps = sorted(set(re.findall(r"2026-00\d{5,6}", html)))
        print("deps", deps)
        for m in re.findall(r"publicationTitle[^,]{0,100}", html)[:20]:
            print(m)
        if deps:
            break
    except Exception as e:
        print("fail", type(e).__name__, e)

# quick NSZ CDN probe if known deposit from prior notes (2026-00394221)
for dep in ["2026-00394221", "2026-00375176"]:
    u = f"http://cdn.staatsbladmonitor.be/2026pdf/{dep}.pdf"
    try:
        req = urllib.request.Request(u, headers=ua, method="HEAD")
        with urllib.request.urlopen(req, context=ctx, timeout=20) as r:
            print("CDN", dep, r.status, r.headers.get("content-length"))
    except Exception as e:
        print("CDN", dep, type(e).__name__, getattr(e, "code", e))
