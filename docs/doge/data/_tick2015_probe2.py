import re
import ssl
import urllib.request
from pathlib import Path

dst = Path("docs/doge/data/raw/tick2015")
dst.mkdir(parents=True, exist_ok=True)
ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}

urls = [
    ("vesalius_cw", "https://www.companyweb.be/nl/0426380543"),
    ("jessa_cw", "https://www.companyweb.be/nl/0411977647"),
    ("zol_cw", "https://www.companyweb.be/nl/0413507053"),
    ("azvesalius_site", "https://www.azvesalius.be/administratieve-gegevens"),
    ("azzeno_contact", "https://www.azzeno.be/nl/contact"),
]
for name, url in urls:
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=45) as resp:
            data = resp.read()
        (dst / f"{name}.html").write_bytes(data)
        t = data.decode("utf-8", "replace")
        title = re.search(r"<title>([^<]+)</title>", t)
        year = None
        for lab in ["Last balance sheet year", "Laatste balansjaar"]:
            i = t.find(lab)
            if i >= 0:
                m = re.search(r"font-medium[^>]*>\s*(\d{4}|N/A)", t[i : i + 220])
                if m:
                    year = m.group(1)
        blocks = re.findall(
            r'omzet:\s*"([^"]+)"',
            t,
        )
        # also look for BE numbers on site
        bes = re.findall(r"BE\s?0?\d{3}[\.\s]?\d{3}[\.\s]?\d{3}", t)
        print(
            "OK",
            name,
            (title.group(1)[:80] if title else None),
            "year",
            year,
            "omzet",
            blocks[:1],
            "BE",
            bes[:3],
        )
    except Exception as e:
        print("FAIL", name, e)
