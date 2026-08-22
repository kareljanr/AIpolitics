import re
import ssl
import urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
out = Path("docs/doge/raw/tick1748")

for name in ["riv_page.html", "rumst.html"]:
    html = (out / name).read_text(encoding="utf-8", errors="replace")
    links = re.findall(r'href=["\']([^"\']+)["\']', html)
    print("====", name)
    for l in links:
        if re.search(r"pdf|download|jaar|reken|brand|file", l, re.I):
            print(l)

# try known willebroek sibling files
cands = [
    "https://www.willebroek.be/sites/default/files/public/Brandweer/Vereenvoudigde%20voorstelling%20rekening%202025.pdf",
    "https://www.willebroek.be/sites/default/files/public/Brandweer/Bekendmaking%20rekening%202025.pdf",
    "https://www.willebroek.be/sites/default/files/public/Brandweer/vereenvoudigde_voorstelling_rekening_2025.pdf",
]
for url in cands:
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, timeout=40, context=ctx) as r:
            data = r.read()
        fn = url.split("/")[-1].replace("%20", "_")
        if not fn.endswith(".pdf"):
            fn += ".pdf"
        (out / fn).write_bytes(data)
        print("OK", fn, len(data), data[:8])
    except Exception as e:
        print("FAIL", url[-60:], type(e).__name__, str(e)[:100])
