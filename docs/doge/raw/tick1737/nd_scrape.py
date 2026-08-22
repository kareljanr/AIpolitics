import urllib.request, ssl, re
from pathlib import Path

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
url = "https://www.northdata.com/ARMONEA%20NV,%20Mechelen/KBO%200889.421.308"
req = urllib.request.Request(url, headers=ua)
with urllib.request.urlopen(req, context=ctx, timeout=60) as r:
    html = r.read().decode("utf-8", "replace")
Path("docs/doge/raw/tick1737/nd_armonea.html").write_text(html, encoding="utf-8")
print("len", len(html))
deps = sorted(set(re.findall(r"2026-00\d{5,6}", html)))
print("deps", deps)
for m in re.findall(r"publicationTitle[^,]{0,120}", html)[:20]:
    print(m)
