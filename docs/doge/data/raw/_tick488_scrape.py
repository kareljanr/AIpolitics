import re
import urllib.request
from pathlib import Path

url = "https://bosa.belgium.be/fr/news/comite-de-monitoring-actualisation-2026-estimation-2027-et-estimation-pluriannuelle-2028-2031"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
html = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")
pdfs = re.findall(r'href="([^"]+\.pdf[^"]*)"', html, re.I)
print("PDFS:")
for p in pdfs:
    print(p)
text = re.sub(r"<[^>]+>", " ", html)
text = re.sub(r"\s+", " ", text)
idx = text.find("Comité de monitoring")
print("TEXT:", text[idx : idx + 3500] if idx >= 0 else text[:2500])

# try known pattern paths
candidates = [
    "https://bosa.belgium.be/sites/default/files/publications/documents/260706%20Rapport%20Monitoringcomit%C3%A9.pdf",
    "https://bosa.belgium.be/sites/default/files/publications/documents/260706%20Rapport%20Monitoringcomit%C3%A9%20-%20Version%20d%C3%A9finitive.pdf",
    "https://bosa.belgium.be/sites/default/files/content/documents/260706%20Rapport%20Monitoringcomit%C3%A9.pdf",
]
for c in list(pdfs):
    if c.startswith("/"):
        candidates.append("https://bosa.belgium.be" + c)
    elif c.startswith("http"):
        candidates.append(c)

out = Path("docs/doge/data/raw/cm_jul2026.pdf")
for c in candidates:
    try:
        print("try", c[:120])
        req = urllib.request.Request(c, headers={"User-Agent": "Mozilla/5.0"})
        data = urllib.request.urlopen(req, timeout=60).read()
        if data[:4] == b"%PDF":
            out.write_bytes(data)
            print("SAVED", len(data), c)
            break
    except Exception as e:
        print("fail", type(e).__name__, e)
