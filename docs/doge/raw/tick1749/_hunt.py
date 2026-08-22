import re
import ssl
import urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
out = Path("docs/doge/raw/tick1749")
out.mkdir(parents=True, exist_ok=True)

pages = [
    ("merelbeke", "https://www.merelbeke-melle.be/documenten-andere-entiteiten"),
    ("brecht", "https://www.brecht.be/over-brecht/beleid/beleids-en-beheercyclus-bbc"),
    ("zwl", "https://zuidwestlimburg.be/hulpverleningszone-zwl/jaarverslagen"),
    ("vbw", "http://vlaamsbrabantwest.be/"),
    ("centrum", "https://www.brandweerzonecentrum.be/"),
    ("waas", "https://waasland.hulpverleningszone.be/"),
    ("sintniklaas", "https://www.sint-niklaas.be/"),
]

for name, url in pages:
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, timeout=30, context=ctx) as r:
            html = r.read().decode("utf-8", "replace")
        (out / f"{name}.html").write_text(html, encoding="utf-8")
        links = re.findall(r'href=["\']([^"\']+)["\']', html)
        hits = [
            l
            for l in links
            if re.search(r"jaar|reken|2025|brand|zone|pdf|download|file", l, re.I)
        ]
        print(name, "hits", len(hits))
        for h in hits[:25]:
            print(" ", h[:160])
    except Exception as e:
        print(name, type(e).__name__, str(e)[:120])

# also probe NSZ/Dijk92/APEFE CDN again
for name, dep in [
    ("nsz", "2026-00394221"),
    ("dijk92", "2026-00377886"),
    ("apefe", "2026-00375176"),
]:
    url = f"http://cdn.staatsbladmonitor.be/2026pdf/{dep}.pdf"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"})
        with urllib.request.urlopen(req, timeout=30, context=ctx) as r:
            data = r.read(200)
        print("CDN", name, "OK", data[:5])
    except Exception as e:
        print("CDN", name, type(e).__name__, str(e)[:80])
