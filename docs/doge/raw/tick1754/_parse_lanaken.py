import re
from pathlib import Path

html = Path("docs/doge/raw/tick1754/lanaken_jr.html").read_text(encoding="utf-8")
# all hrefs
hrefs = re.findall(r'href=["\']([^"\']+)["\']', html)
for h in hrefs:
    if re.search(r"pdf|download|file|reken|besluit|boek", h, re.I):
        print("H", h)

# media / attachment patterns
for pat in [
    r"/media/[^\"' ]+",
    r"/sites/default/files/[^\"' ]+",
    r"documentId=[^\"'&\s]+",
    r"/api/[^\"' ]+",
]:
    for m in re.findall(pat, html):
        print("P", m[:200])

idx = html.lower().find("rekening 2025")
print("NEAR", html[idx : idx + 1200] if idx >= 0 else "none")

# download jaarverslag 2025
import ssl
import urllib.request
from pypdf import PdfReader

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0"}
url = "https://www.bwol.be/uploads/1/2/5/4/12549797/2025_jaarverslag_def.pdf"
req = urllib.request.Request(url, headers=ua)
with urllib.request.urlopen(req, timeout=90, context=ctx) as r:
    data = r.read()
Path("docs/doge/raw/tick1754/bwol_jv2025.pdf").write_bytes(data)
print("JV", len(data), data[:5])
rr = PdfReader("docs/doge/raw/tick1754/bwol_jv2025.pdf")
print("pages", len(rr.pages))
for i, p in enumerate(rr.pages):
    t = p.extract_text() or ""
    if any(
        k in t.lower()
        for k in ["financ", "budget", "euro", "personeel", "dotatie", "uitgave", "ontvang"]
    ):
        print(f"===p{i+1}===")
        print(t[:2200])
