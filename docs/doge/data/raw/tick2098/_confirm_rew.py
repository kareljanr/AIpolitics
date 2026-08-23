# -*- coding: utf-8 -*-
import re
import ssl
import urllib.request
from pathlib import Path

CTX = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0", "Accept-Language": "nl-BE"}
PAT = re.compile(
    r'(20\d\d)\s*:\s*\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",'
    r'\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)"'
)
url = "https://www.companyweb.be/nl/0644638937/rew"
req = urllib.request.Request(url, headers=UA)
with urllib.request.urlopen(req, context=CTX, timeout=25) as resp:
    html = resp.read().decode("utf-8", "replace")
Path("docs/doge/data/raw/tick2098/rew_nl.html").write_text(html, encoding="utf-8")
print("REW years", [y[0] for y in PAT.findall(html)[:5]])
title = re.search(r"<title>([^<]+)", html)
print("REW", title.group(1)[:90] if title else "?")
