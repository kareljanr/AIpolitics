import re
import urllib.request
from pathlib import Path

url = "https://vliz.be/en/publications/annual-report/annual-report-2025"
html = urllib.request.urlopen(url, timeout=45).read().decode("utf-8", "ignore")
Path("docs/doge/raw/vliz_ar2025_page.html").write_text(html, encoding="utf-8")
print("html_len", len(html))

pdfs = re.findall(r"https?://[^\s\"']+\.pdf", html)
pdfs += re.findall(r"/[^\s\"']+\.pdf", html)
print("pdfs:")
for p in sorted(set(pdfs))[:30]:
    print(" ", p)

# also try NL page
url2 = "https://www.vliz.be/nl/publicaties/jaarboek/jaarboek-2024"
try:
    html2 = urllib.request.urlopen(url2, timeout=30).read().decode("utf-8", "ignore")
    pdfs2 = re.findall(r"https?://[^\s\"']+\.pdf", html2)
    print("jaarboek2024 pdfs:")
    for p in sorted(set(pdfs2))[:20]:
        print(" ", p)
except Exception as e:
    print("nl fail", e)

# try imis search
for q in [
    "https://www.vliz.be/en/imis?module=ref&refid=420765",
    "https://www.vliz.be/imis?module=ref&refid=420676",
]:
    try:
        h = urllib.request.urlopen(q, timeout=20).read().decode("utf-8", "ignore")
        pdfs = re.findall(r"https?://[^\s\"']+\.pdf", h)
        print(q, "pdfs", pdfs[:10])
    except Exception as e:
        print(q, e)
