import re
import urllib.request
from pathlib import Path

url = "https://ibsa.brussels/publications/publications-institutionnelles"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "ignore")
Path("docs/doge/raw/ibsa_pubs.html").write_text(html, encoding="utf-8")
print("len", len(html))
pdfs = re.findall(r"https?://[^\s\"']+\.pdf", html)
pdfs += re.findall(r"/[^\s\"']+\.pdf", html)
for p in sorted(set(pdfs)):
    print("PDF", p)

# try common paths
cands = [
    "https://ibsa.brussels/sites/default/files/publication/documents/RapportAnnuel-FR-2024-WEB.pdf",
    "https://ibsa.brussels/sites/default/files/publication/documents/RapportAnnuel-FR-2025-WEB.pdf",
    "https://ibsa.brussels/sites/default/files/publication/documents/RapportAnnuel-FR-2025.pdf",
    "https://ibsa.brussels/sites/default/files/publication/documents/Rapport-annuel-IBSA-2024.pdf",
    "https://ibsa.brussels/sites/default/files/publication/documents/RapportAnnuel-NL-2024-WEB.pdf",
]
for u in cands:
    try:
        req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}, method="HEAD")
        r = urllib.request.urlopen(req, timeout=15)
        print("OK", r.status, r.headers.get("Content-Length"), u)
    except Exception as e:
        print("no", type(e).__name__, u)
