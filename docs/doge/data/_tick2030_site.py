import re
import ssl
import urllib.request
from pathlib import Path

html = Path("docs/doge/data/raw/tick2030/sint_jozef_aarschot_en.html").read_text(encoding="utf-8")
m = re.search(r'Employees\s*=\s*"([^"]+)"', html)
print("emp0", m.group(1) if m else None)
# second year often in same script arrays — look nearby numbers after emp
print("fte snippets", re.findall(r"(\d{2,3}[\.,]\d)", html[html.find("Employees") : html.find("Employees") + 400])[:10])

ctx = ssl.create_default_context()
req = urllib.request.Request("https://www.sintjozefrillaar.be/", headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
    h = r.read().decode("utf-8", "replace")
Path("docs/doge/data/raw/tick2030/sj_site.html").write_text(h, encoding="utf-8")
emails = sorted(set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", h)))
print("site emails", emails[:8])
t = re.sub(r"<[^>]+>", " ", Path("docs/doge/data/raw/tick2030/sj_aarschot_kbo.html").read_text(encoding="utf-8"))
t = re.sub(r"\s+", " ", t)
for k in ["Adres van de zetel", "Rechtsvorm", "Status", "Aantal vestigingseenheden"]:
    i = t.find(k)
    if i >= 0:
        print(k, t[i : i + 120])
