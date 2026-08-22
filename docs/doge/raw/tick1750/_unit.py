import re
import ssl
import urllib.request
from pathlib import Path
from pypdf import PdfReader

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0"}
out = Path("docs/doge/raw/tick1750")
out.mkdir(parents=True, exist_ok=True)

# Brecht Rand 2025 dotatie
brecht = Path("docs/doge/raw/tick1749/brecht.html")
html = brecht.read_text(encoding="utf-8", errors="replace") if brecht.exists() else ""
# find download id near 'dienstjaar 2025'
for label in ["dienstjaar 2025", "dienstjaar 2026"]:
    i = html.find(f"Dotatie Brandweerzone Rand - {label}")
    if i < 0:
        i = html.find(f"Dotatie brandweerzone Rand - {label}")
    print("label", label, "idx", i)
    if i >= 0:
        chunk = html[max(0, i - 500) : i + 50]
        hrefs = re.findall(r"/download-publication/[A-Za-z0-9]+/[^\"']+", chunk)
        print(" hrefs", hrefs)

# Direct known from prior hunt text: ax5r9 for 2025
cands = [
    "https://www.brecht.be/download-publication/ax5r9/Uittreksel_dotatie_brandweer.pdf",
    "https://www.brecht.be/download-publication/7gvV2/Uittreksel%20GR%2011%20december%202025%20Dotatie%20brandweer.pdf",
]
for url in cands:
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, timeout=40, context=ctx) as r:
            data = r.read()
        fn = url.split("/")[-2] + "_" + url.split("/")[-1].replace("%20", "_")
        if not fn.endswith(".pdf"):
            fn += ".pdf"
        (out / fn).write_bytes(data)
        print("OK", fn, len(data), data[:5])
        if data[:4] == b"%PDF":
            rdr = PdfReader(str(out / fn))
            print(" pages", len(rdr.pages))
            for i, p in enumerate(rdr.pages[:4]):
                print("====", i + 1)
                print((p.extract_text() or "")[:2000])
    except Exception as e:
        print("FAIL", url[-50:], type(e).__name__, str(e)[:100])

# Also try Sint-Niklaas / Waasland known CDN website-files from search
waas = "https://cdn.prod.website-files.com/68b9ea0c64b4393f8cabeb7f/6a46159d1355a0703a54db57_Meldingslijst%20ZR%20-%201%20juli%202026%2009-00.pdf"
try:
    req = urllib.request.Request(waas, headers=ua)
    with urllib.request.urlopen(req, timeout=40, context=ctx) as r:
        data = r.read()
    (out / "waasland_zr_meldingslijst.pdf").write_bytes(data)
    print("WAAS", len(data))
    rdr = PdfReader(str(out / "waasland_zr_meldingslijst.pdf"))
    print(" pages", len(rdr.pages))
    print(rdr.pages[0].extract_text() or "")
except Exception as e:
    print("WAAS FAIL", type(e).__name__, str(e)[:100])
