import re
import ssl
import urllib.request
from pathlib import Path
from urllib.parse import urljoin

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
out = Path("docs/doge/raw/tick1749")
out.mkdir(parents=True, exist_ok=True)

url = "https://www.antwerpen.be/info/52d5052639d8a6ec798b4b4a/besluitvorming"
req = urllib.request.Request(url, headers=ua)
with urllib.request.urlopen(req, timeout=45, context=ctx) as r:
    html = r.read().decode("utf-8", "replace")
(out / "antwerpen_bza.html").write_text(html, encoding="utf-8")

# find pdf / media links mentioning 2025 / jaarrekening / begrotingsrekening
links = re.findall(r'href=["\']([^"\']+)["\']', html)
print("total links", len(links))
for l in links:
    if re.search(r"2025|jaar|reken|begrot|pdf|media|download|file|document", l, re.I):
        print(l[:200])

# also search for media IDs / filenames in text
for m in re.finditer(r".{0,40}(Jaarrekening 2025|Begrotingsrekening 2025|Afkondiging jaarrekening).{0,200}", html, re.I):
    print("CTX:", re.sub(r"\s+", " ", m.group(0))[:240])
