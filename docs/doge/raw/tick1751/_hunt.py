import re
import ssl
import urllib.request
from pathlib import Path
from pypdf import PdfReader

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
bot = {"User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"}
out = Path("docs/doge/raw/tick1751")
out.mkdir(parents=True, exist_ok=True)

# CDN recheck
for name, dep in [
    ("nsz", "2026-00394221"),
    ("dijk92", "2026-00377886"),
    ("apefe", "2026-00375176"),
]:
    url = f"http://cdn.staatsbladmonitor.be/2026pdf/{dep}.pdf"
    try:
        req = urllib.request.Request(url, headers=bot)
        with urllib.request.urlopen(req, timeout=25, context=ctx) as r:
            data = r.read(300)
        print("CDN", name, "OK", data[:5])
    except Exception as e:
        print("CDN", name, type(e).__name__, str(e)[:80])

# Brecht Rand 2025/2026 dots
brecht_html = Path("docs/doge/raw/tick1749/brecht.html")
html = brecht_html.read_text(encoding="utf-8", errors="replace") if brecht_html.exists() else ""
for label in ["dienstjaar 2025", "dienstjaar 2026"]:
    for prefix in ["Dotatie Brandweerzone Rand - ", "Dotatie brandweerzone Rand - "]:
        i = html.find(prefix + label)
        if i >= 0:
            chunk = html[max(0, i - 600) : i + 80]
            hrefs = re.findall(r"/download-publication/[A-Za-z0-9]+/[^\"']+\.pdf", chunk)
            print(label, hrefs)

cands = [
    ("rand2025", "https://www.brecht.be/download-publication/ax5r9/Uittreksel_dotatie_brandweer.pdf"),
    ("rand2026", "https://www.brecht.be/download-publication/7gvV2/Uittreksel%20GR%2011%20december%202025%20Dotatie%20brandweer.pdf"),
]
for name, url in cands:
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, timeout=40, context=ctx) as r:
            data = r.read()
        path = out / f"{name}.pdf"
        path.write_bytes(data)
        print("DL", name, len(data), data[:5])
        if data[:4] == b"%PDF":
            rdr = PdfReader(str(path))
            print(" pages", len(rdr.pages))
            for i, p in enumerate(rdr.pages[:3]):
                print("====", name, i + 1)
                print((p.extract_text() or "")[:2200])
    except Exception as e:
        print("FAIL", name, type(e).__name__, str(e)[:100])

# Waasland zoneraad meldingslijst from prior search
waas = "https://cdn.prod.website-files.com/68b9ea0c64b4393f8cabeb7f/6a46159d1355a0703a54db57_Meldingslijst%20ZR%20-%201%20juli%202026%2009-00.pdf"
try:
    req = urllib.request.Request(waas, headers=ua)
    with urllib.request.urlopen(req, timeout=40, context=ctx) as r:
        data = r.read()
    (out / "waasland_zr.pdf").write_bytes(data)
    print("WAAS", len(data))
    rdr = PdfReader(str(out / "waasland_zr.pdf"))
    print(" pages", len(rdr.pages))
    for i, p in enumerate(rdr.pages[:2]):
        print((p.extract_text() or "")[:2000])
except Exception as e:
    print("WAAS FAIL", type(e).__name__, str(e)[:100])
