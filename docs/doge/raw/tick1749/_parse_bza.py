import re
import ssl
import urllib.request
from pathlib import Path

html = Path("docs/doge/raw/tick1749/antwerpen_bza.html").read_text(encoding="utf-8", errors="replace")
print("len", len(html))
for pat in ["Begrotingsrekening", "Jaarrekening", "Afkondiging", "assets.antwerpen", "download"]:
    print(pat, html.count(pat))

ids = re.findall(
    r"assets\.antwerpen\.be/srv/assets/api/download/([a-f0-9-]{36})/([^\"'?]+)",
    html,
)
print("downloads", len(ids))
seen = set()
for i, n in ids:
    key = (i, n)
    if key in seen:
        continue
    seen.add(key)
    print(i, n)

for m in re.finditer(r".{0,60}(Jaarrekening|Begrotingsrekening).{0,200}", html, re.I):
    print("CTX:", re.sub(r"\s+", " ", m.group(0))[:280])

# Download afkondiging + try common patterns from search snippet filenames
ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0"}
out = Path("docs/doge/raw/tick1749")
known = [
    ("afkondiging", "https://assets.antwerpen.be/srv/assets/api/download/e3030011-a6a5-443f-be63-1a937acce0d9/JR%202025%20Afkondiging.pdf"),
]
for name, url in known:
    req = urllib.request.Request(url, headers=ua)
    with urllib.request.urlopen(req, timeout=60, context=ctx) as r:
        data = r.read()
    (out / f"bza_{name}.pdf").write_bytes(data)
    print("saved", name, len(data))
