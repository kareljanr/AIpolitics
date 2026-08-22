import re
from pathlib import Path

html = Path("docs/doge/raw/tick1754/bwol_contact.html").read_text(encoding="utf-8")
for m in re.finditer(r'data-cfemail=["\']([0-9a-fA-F]+)["\']', html):
    enc = m.group(1)
    r = int(enc[:2], 16)
    email = "".join(chr(int(enc[i : i + 2], 16) ^ r) for i in range(2, len(enc), 2))
    print("cfemail", email)
print("mailto", re.findall(r"mailto:([^\"' ]+)", html)[:10])
idx = html.find("cfemail")
print(html[idx - 80 : idx + 220] if idx >= 0 else "no cf")
