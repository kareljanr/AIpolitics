import re
import ssl
import urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0"}
out = Path("docs/doge/raw/tick1752")
out.mkdir(parents=True, exist_ok=True)

urls = [
    ("rand_home", "https://www.brandweerzonerand.be/"),
    ("rand_contact", "https://www.brandweerzonerand.be/contact"),
    ("rand_over", "https://www.brandweerzonerand.be/over-ons"),
    ("rand_begroting", "https://www.brandweerzonerand.be/nieuws/begroting-2026-goedgekeurd"),
    ("kbo_rand", "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0500914730"),
]

for name, url in urls:
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, timeout=25, context=ctx) as r:
            html = r.read().decode("utf-8", "replace")
        (out / f"{name}.html").write_text(html, encoding="utf-8")
        emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", html)
        addrs = re.findall(r"\d{4}\s+[A-Za-z\- ]+", html)
        print(name, "ok", len(html), "emails", list(dict.fromkeys(emails))[:10])
        if "begroting" in name.lower() or "over" in name:
            text = re.sub(r"<[^>]+>", " ", html)
            text = re.sub(r"\s+", " ", text)
            for m in re.finditer(r".{0,80}(euro|EUR|€|begroting|budget|dotatie|jaarrekening|rekening).{0,120}", text, re.I):
                print("  snip:", m.group(0)[:200])
    except Exception as e:
        print(name, type(e).__name__, str(e)[:120])

# also extract VBWest + Zuid-Oost MU from justel
from pypdf import PdfReader

r = PdfReader(str(out / "justel_mu_2025.pdf"))
for i in range(28, 33):
    t = r.pages[i].extract_text() or ""
    for label in ["VLAAMS-BRABANT WEST", "ZUID-OOST", "ZONE RAND", "WAASLAND", "CENTRUM"]:
        if label in t.upper().replace(" ", "") or label.replace("-", " ") in t.upper():
            pass
    if "VLAAMS" in t.upper() or "ZUID" in t.upper() or "WAASLAND" in t.upper() or "CENTRUM" in t.upper():
        for line in t.splitlines():
            u = line.upper()
            if any(x in u for x in ["VLAAMS", "ZUID", "WAASLAND", "CENTRUM", "0500 9", "0500.9"]):
                print("L", i + 1, line[:120])
