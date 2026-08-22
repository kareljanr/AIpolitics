import urllib.request, ssl, re
from pathlib import Path

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
url = "https://www.northdata.com/Woon-%20en%20Zorgcentrum%20Sint-Jozef%20VZW,%20Rumst/KBO%200448.190.181"
req = urllib.request.Request(url, headers=ua)
with urllib.request.urlopen(req, context=ctx, timeout=60) as r:
    html = r.read().decode("utf-8", "replace")
out = Path("docs/doge/raw/tick1734/nd_sintjozef.html")
out.write_text(html, encoding="utf-8")
print("len", len(html))
deps = sorted(set(re.findall(r"2026-00\d{5}", html)))
print("deps", deps)
cbsos = sorted(set(re.findall(r"Cbso\s+2026-00\d{5}", html, re.I)))
print("cbsos", cbsos)
for m in re.findall(r"publicationTitle[^,]{0,100}", html)[:40]:
    print(m)
# also try alternate URL forms
for alt in [
    "https://www.northdata.com/WOON-%20EN%20ZORGCENTRUM%20SINT-JOZEF%20VZW,%20Rumst/KBO%200448.190.181",
    "https://www.northdata.com/search?q=0448190181",
]:
    try:
        req2 = urllib.request.Request(alt, headers=ua)
        with urllib.request.urlopen(req2, context=ctx, timeout=30) as r2:
            h2 = r2.read().decode("utf-8", "replace")
        d2 = sorted(set(re.findall(r"2026-00\d{5}", h2)))
        print("ALT", alt[:60], "len", len(h2), "deps", d2[:10])
    except Exception as e:
        print("ALT fail", alt[:60], type(e).__name__, e)
