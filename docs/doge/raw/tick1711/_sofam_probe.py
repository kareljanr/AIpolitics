# -*- coding: utf-8 -*-
import re
import urllib.request
from pathlib import Path

UA = {"User-Agent": "Mozilla/5.0"}
OUT = Path(__file__).resolve().parent

req = urllib.request.Request("https://www.sofam.be/nl/138/Jaarverslagen", headers=UA)
html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")
links = re.findall(r'href="([^"]+)"', html)
for l in links:
    if any(
        k in l.lower()
        for k in ["2025", "jaar", "transp", "download", ".pdf", ".docx", "file"]
    ):
        print(l)
print("---sample---")
for l in links[:50]:
    print(l[:140])
