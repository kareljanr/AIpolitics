import re
import ssl
import urllib.request

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"}

cands = [
    ("rivierenland", "https://www.brandweerrivierenland.be/"),
    ("rivierenland2", "https://rivierenland.hulpverleningszone.be/"),
    ("rand", "https://www.zone-rand.be/"),
    ("rand2", "https://rand.hulpverleningszone.be/"),
    ("waasland", "https://www.brandweerwaasland.be/"),
    ("waasland2", "https://waasland.hulpverleningszone.be/"),
    ("centrum", "https://www.brandweerzonecentrum.be/"),
    ("vbwest", "https://www.hvzvlbw.be/"),
    ("zuidlimburg", "https://www.brandweerzuidlimburg.be/"),
    ("oostlimburg", "https://www.brandweeroostlimburg.be/"),
    ("zuidoost", "https://www.brandweerzuidoost.be/"),
    ("antwerpen", "https://www.brandweerzone-antwerpen.be/"),
]

for name, url in cands:
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, timeout=25, context=ctx) as r:
            html = r.read().decode("utf-8", "replace")
        pdfs = re.findall(r'href=["\']([^"\']+\.pdf)["\']', html, flags=re.I)
        hits = [p for p in pdfs if re.search(r"jaar|reken|2025|begrot|budget", p, re.I)]
        print(name, "hits", hits[:10], "npdfs", len(pdfs), "len", len(html))
    except Exception as e:
        print(name, type(e).__name__, str(e)[:120])
