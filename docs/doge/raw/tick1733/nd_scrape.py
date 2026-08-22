import urllib.request, ssl, re
from pathlib import Path

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
url = "https://www.northdata.com/Woonzorgcentrum%20Veilige%20Have%20VZW,%20Aalter/KBO%200449.507.205"
req = urllib.request.Request(url, headers=ua)
with urllib.request.urlopen(req, context=ctx, timeout=60) as r:
    html = r.read().decode("utf-8", "replace")
out = Path("docs/doge/raw/tick1733/nd_veilige.html")
out.write_text(html, encoding="utf-8")
print("len", len(html))
deps = sorted(set(re.findall(r"2026-00\d{5}", html)))
print("deps", deps)
cbsos = sorted(set(re.findall(r"Cbso\s+2026-00\d{5}", html, re.I)))
print("cbsos", cbsos)
for m in re.findall(r"publicationTitle[^,]{0,80}", html)[:30]:
    print(m)
