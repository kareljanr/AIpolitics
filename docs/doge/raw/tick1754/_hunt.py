import re
import ssl
import urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0"}
bot = {
    "User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
}
out = Path("docs/doge/raw/tick1754")
out.mkdir(parents=True, exist_ok=True)

for name, dep in [
    ("nsz", "2026-00394221"),
    ("dijk92", "2026-00377886"),
    ("apefe", "2026-00375176"),
]:
    url = f"http://cdn.staatsbladmonitor.be/2026pdf/{dep}.pdf"
    try:
        req = urllib.request.Request(url, headers=bot)
        with urllib.request.urlopen(req, timeout=20, context=ctx) as r:
            data = r.read(32)
            print("CDN", name, "OK", data[:8])
            if data[:4] == b"%PDF":
                full = urllib.request.urlopen(
                    urllib.request.Request(url, headers=bot), timeout=60, context=ctx
                ).read()
                (out / f"{name}.pdf").write_bytes(full)
                print("  saved", len(full))
    except Exception as e:
        print("CDN", name, type(e).__name__, str(e)[:80])

targets = [
    ("zoneoost", "https://www.zoneoost.be/"),
    ("zoneoost2", "https://oost.hulpverleningszone.be/"),
    ("hvzol", "https://www.hvzoostlimburg.be/"),
    ("hvzol2", "https://oost-limburg.hulpverleningszone.be/"),
    ("bza", "https://www.brandweerzoneantwerpen.be/"),
    ("bosgroep", "https://bosgroepen.be/"),
    ("bosgroep_fin", "https://bosgroepen.be/financiering/"),
    ("bornem_agb", "https://www.bornem.be/"),
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
            if re.search(
                r"jaar|reken|begrot|2025|2026|pdf|financ|besluit|rapport|storage",
                l,
                re.I,
            )
        ]
        print(name, "ok", len(html), "links", links[:18])
    except Exception as e:
        print(name, type(e).__name__, str(e)[:100])
