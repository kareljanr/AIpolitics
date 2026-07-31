import re
import urllib.request
from pathlib import Path

raw = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw")

# Flanders Landbouw BBT page
u = "https://www.vlaamsparlement.be/nl/parlementaire-documenten/parlementaire-initiatieven/1959467"
req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
h = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")
ids = re.findall(r"pfile\?id=(\d+)", h)
print("pfile ids", ids[:10])
pdfs = re.findall(r'href="([^"]+\.pdf)"', h)
print("pdfs", pdfs[:10])

# try first id
if ids:
    pid = ids[0]
    url = f"https://docs.vlaamsparlement.be/pfile?id={pid}"
    print("try", url)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    d = urllib.request.urlopen(req, timeout=60).read()
    out = raw / "vl_bbt_landbouw_bo2026.pdf"
    out.write_bytes(d)
    print("dl", len(d), d[:5])

# Wallonia DO15 ARNE if exists
for name, url in [
    (
        "wal_do15_2026.pdf",
        "https://finances.wallonie.be/files/Budget%202026/Budget%202026/depenses/do15.pdf",
    ),
]:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        d = urllib.request.urlopen(req, timeout=90).read()
        (raw / name).write_bytes(d)
        print(name, len(d), d[:5])
    except Exception as e:
        print(name, e)
