import re
import ssl
import urllib.request
from pathlib import Path
from pypdf import PdfReader

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0"}
bot = {"User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"}
out = Path("docs/doge/raw/tick1752")
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
        with urllib.request.urlopen(req, timeout=20, context=ctx) as r:
            print("CDN", name, "OK")
    except Exception as e:
        print("CDN", name, type(e).__name__, str(e)[:60])

# Justel MU subsidy PDF
mu = "https://www.ejustice.just.fgov.be/mopdf/2025/09/26_2.pdf"
try:
    req = urllib.request.Request(mu, headers=ua)
    with urllib.request.urlopen(req, timeout=60, context=ctx) as r:
        data = r.read()
    (out / "justel_mu_2025.pdf").write_bytes(data)
    print("MU pdf", len(data))
except Exception as e:
    print("MU FAIL", e)

# VBWest site + Zuid-Oost
for name, url in [
    ("vbwest", "https://vlaamsbrabantwest.be/"),
    ("vbwest2", "http://vlaamsbrabantwest.be/"),
    ("zuidoost", "https://www.brandweerzuidoost.be/"),
    ("zuidoost2", "https://zuidoost.hulpverleningszone.be/"),
    ("rand_begroting", "https://www.brandweerzonerand.be/nieuws/begroting-2026-goedgekeurd"),
]:
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, timeout=25, context=ctx) as r:
            html = r.read().decode("utf-8", "replace")
        (out / f"{name}.html").write_text(html, encoding="utf-8")
        links = [l for l in re.findall(r'href=["\']([^"\']+)["\']', html) if re.search(r"jaar|reken|begrot|2025|pdf|financ|besluit", l, re.I)]
        print(name, "links", links[:12])
    except Exception as e:
        print(name, type(e).__name__, str(e)[:80])

# Herent HVZ Oost VB file - check if JR2025
herent = "https://www.herent.be/file/download/40550/2B4AD5756AE2071CACAC8251FAFFA142"
try:
    req = urllib.request.Request(herent, headers=ua)
    with urllib.request.urlopen(req, timeout=40, context=ctx) as r:
        data = r.read()
    (out / "herent_hvzo.pdf").write_bytes(data)
    print("herent", len(data), data[:5])
    if data[:4] == b"%PDF":
        rdr = PdfReader(str(out / "herent_hvzo.pdf"))
        print("pages", len(rdr.pages))
        t0 = rdr.pages[0].extract_text() or ""
        print(t0[:1500])
except Exception as e:
    print("herent FAIL", type(e).__name__, str(e)[:100])
