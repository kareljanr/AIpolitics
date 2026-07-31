import urllib.request
import re

urls = [
    "https://provincieoost-vlaanderen.beleidsportaal.be/meerjarenplan-2026-2031",
    "https://provincieoost-vlaanderen.beleidsportaal.be/meerjarenplan-2026-2031/programma/beleidsverklaring",
    "https://www.oost-vlaanderen.be",
    "https://www.oost-vlaanderen.be/over-oost-vlaanderen/bestuur-en-beleid/meerjarenplan-en-budget",
    "https://www.oost-vlaanderen.be/over-oost-vlaanderen/bestuur-en-beleid",
]

for u in urls:
    try:
        req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=25) as r:
            html = r.read().decode("utf-8", "replace")
        print("URL", u, "len", len(html), "status ok")
        pdfs = re.findall(r"https?://[^\s\"'<>]+\.pdf", html, re.I)
        data = re.findall(r"/Data/[^\s\"'<>]+", html)
        href_pdf = re.findall(r'href="([^"]+\.pdf[^"]*)"', html, re.I)
        mjp = re.findall(r'href="([^"]*meerjaren[^"]*)"', html, re.I)
        print("  pdfs:", pdfs[:12])
        print("  data:", data[:12])
        print("  href_pdf:", href_pdf[:12])
        print("  mjp:", mjp[:12])
    except Exception as e:
        print("ERR", u, type(e).__name__, e)
