import re
import ssl
import urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
out = Path("docs/doge/raw/tick1749")

urls = [
    "https://ebesluit.antwerpen.be/zittingen/kalender",
    "https://ebesluit.antwerpen.be/zoeken?q=jaarrekening+2025+brandweer",
    "https://ebesluit.antwerpen.be/zoeken?query=Brandweer%20Zone%20Antwerpen%20jaarrekening%202025",
    "https://www.antwerpen.be/nl/overzicht/brandweer/over-de-brandweer/zoneraad",
    "https://ebesluit.antwerpen.be/document/699eb362a60702536ead1eac",
]

for url in urls:
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, timeout=35, context=ctx) as r:
            data = r.read()
        name = re.sub(r"[^a-z0-9]+", "_", url.lower())[-80:]
        if data[:4] == b"%PDF":
            path = out / f"{name}.pdf"
            path.write_bytes(data)
            print("PDF", url[:70], len(data))
        else:
            html = data.decode("utf-8", "replace")
            path = out / f"{name}.html"
            path.write_text(html, encoding="utf-8")
            links = re.findall(r'href=["\']([^"\']+)["\']', html)
            hits = [l for l in links if re.search(r"2025|jaar|reken|pdf|download|document|zitting", l, re.I)]
            print("HTML", url[:70], "hits", len(hits), "len", len(html))
            for h in hits[:20]:
                print(" ", h[:160])
    except Exception as e:
        print("FAIL", url[:70], type(e).__name__, str(e)[:100])
