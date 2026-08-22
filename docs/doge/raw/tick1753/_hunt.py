import re
import ssl
import urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0"}
bot = {
    "User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
}
out = Path("docs/doge/raw/tick1753")
out.mkdir(parents=True, exist_ok=True)

# CDN recheck preferred
for name, dep in [
    ("nsz", "2026-00394221"),
    ("dijk92", "2026-00377886"),
    ("apefe", "2026-00375176"),
]:
    url = f"http://cdn.staatsbladmonitor.be/2026pdf/{dep}.pdf"
    try:
        req = urllib.request.Request(url, headers=bot)
        with urllib.request.urlopen(req, timeout=20, context=ctx) as r:
            data = r.read(20)
            print("CDN", name, "OK", data[:5])
    except Exception as e:
        print("CDN", name, type(e).__name__, str(e)[:80])

# HVZ portals
targets = [
    ("zuidoost", "https://www.brandweerzuidoost.be/"),
    ("zuidoost2", "https://zuidoost.hulpverleningszone.be/"),
    ("zuidoost3", "https://www.hvzzuidoost.be/"),
    ("vbwest", "https://vlaamsbrabantwest.be/"),
    ("vbwest_besl", "https://vlaamsbrabantwest.be/over-ons/besluitvorming"),
    ("bza", "https://www.brandweerzoneantwerpen.be/"),
    ("bza2", "https://antwerpen.hulpverleningszone.be/"),
    ("bosgroep", "https://www.bosgroepen.be/"),
    ("faro", "https://faro.be/"),
]

for name, url in targets:
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, timeout=25, context=ctx) as r:
            html = r.read().decode("utf-8", "replace")
        (out / f"{name}.html").write_text(html, encoding="utf-8")
        links = [
            l
            for l in re.findall(r'href=["\']([^"\']+)["\']', html)
            if re.search(r"jaar|reken|begrot|2025|pdf|financ|besluit|rapport", l, re.I)
        ]
        print(name, "ok", len(html), "links", links[:15])
    except Exception as e:
        print(name, type(e).__name__, str(e)[:100])
