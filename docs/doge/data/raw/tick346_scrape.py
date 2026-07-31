import re
import urllib.request
from pathlib import Path

raw = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw")
h = (raw / "adeps_ra2025.html").read_text(encoding="utf-8", errors="replace")

print("=== PDF HREFS ===")
for m in re.finditer(r'href="([^"]+\.pdf)"', h, re.I):
    print(m.group(1))

print("=== FILEADMIN ===")
for m in re.finditer(r'href="([^"]*fileadmin[^"]+)"', h, re.I):
    print(m.group(1)[:250])

# also file links without pdf extension
for m in re.finditer(r'(https?://[^"\s]+(?:Rapport|rapport|audit)[^"\s]*)', h, re.I):
    print("url", m.group(1)[:250])

idx = h.find("budget relativement")
print("budget snippet:", h[idx - 100 : idx + 900] if idx > 0 else "no")

# try a propos page
url = "https://www.sport-adeps.be/a-propos/adeps-a-propos/"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
try:
    data = urllib.request.urlopen(req, timeout=30).read()
    (raw / "adeps_apropos.html").write_bytes(data)
    h2 = data.decode("utf-8", errors="replace")
    print("=== APROPOS PDFS ===")
    for m in re.finditer(r'href="([^"]+\.pdf)"', h2, re.I):
        print(m.group(1))
    for m in re.finditer(r'href="([^"]*fileadmin[^"]+)"', h2, re.I):
        print(m.group(1)[:250])
except Exception as e:
    print("apropos err", e)
