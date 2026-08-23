import re
import ssl
import urllib.request
from pathlib import Path

dst = Path("docs/doge/data/raw/tick2018")
ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}

urls = [
    ("pcgs_contact", "https://www.pcgs.be/nl/contact"),
    ("pcgs_contact2", "https://www.pcgs.be/contact"),
    ("pcgs_disclaimer", "https://www.pcgs.be/nl/disclaimer"),
    ("pcgs_footer", "https://www.pcgs.be/nl"),
]
for name, url in urls:
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
            data = resp.read()
        (dst / f"{name}.html").write_bytes(data)
        t = data.decode("utf-8", "replace")
        emails = sorted(
            set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", t))
        )
        print(name, len(data), emails[:15])
        for lab in ("Fratersplein", "Sleidinge", "info@", "mailto:"):
            if lab.lower() in t.lower():
                i = t.lower().find(lab.lower())
                print(" ", lab, repr(t[i : i + 120].replace("\n", " ")))
    except Exception as e:
        print("FAIL", name, e)

# KBO start date
t = (dst / "pcgs_kbo.html").read_text(encoding="utf-8", errors="replace")
for lab in ["Start van de rechtspersoon", "Maatschappelijke naam", "Status", "Actief"]:
    i = t.find(lab)
    if i >= 0:
        print("KBO", lab, repr(t[i : i + 200].replace("\n", " ").replace("\t", " ")[:180]))
