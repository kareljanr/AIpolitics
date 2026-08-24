# -*- coding: utf-8 -*-
import re
import ssl
import urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path(__file__).resolve().parent


def fetch(url, path):
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
            data = r.read()
        path.write_bytes(data)
        print("OK", path.name, len(data))
        return data.decode("utf-8", "ignore")
    except Exception as e:
        print("FAIL", path.name, type(e).__name__, e)
        return None


def plain_text(t):
    p = re.sub(r"<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", p)


def extract_metrics(p):
    year = re.search(r"Last balance sheet year\s+(\d{4})", p)
    # Turnover block often: Turnover € X,XXX ...
    def euro_after(label):
        m = re.search(label + r"\s*€\s*([\d.,]+)", p)
        if not m:
            return None
        return m.group(1).replace(".", "").replace(",", "")

    return {
        "year": year.group(1) if year else None,
        "turnover": euro_after(r"Turnover"),
        "gross": euro_after(r"Gross margin"),
        "pnl": euro_after(r"Profit/Loss"),
        "equity": euro_after(r"Equity"),
        "employees": (re.search(r"Employees\s+([\d.,]+)", p) or [None, None])[1],
        "filed": (re.search(r"were filed on\s+([\d-]+)", p) or [None, None])[1],
        "title": (re.search(r"Full name\s+([^P]{5,80}?)\s+Principal", p) or [None, None])[1],
    }


# Direct company pages — prefer unused YE2025 WZC/MRS
cands = [
    ("hertog_jan_en.html", "https://www.companyweb.be/en/0845895824"),
    ("hertog_jan_nl.html", "https://www.companyweb.be/nl/0845895824"),
    ("hertog_jan_fr.html", "https://www.companyweb.be/fr/0845895824"),
    ("sint_jozef_ninove_en.html", "https://www.companyweb.be/en/0452865383"),
    ("huize_sint_jozef_ieper_en.html", "https://www.companyweb.be/en/0409942289"),
    ("de_linde_en.html", "https://www.companyweb.be/en/0467355403"),
    ("ocura_en.html", "https://www.companyweb.be/en/0443072838"),  # likely already mined
]

for name, url in cands:
    t = fetch(url, out / name)
    if not t:
        continue
    p = plain_text(t)
    m = extract_metrics(p)
    print(name, m)
    # also print commercial name / address snippets
    for key in ["Commercial name", "Status", "Enterprise number", "Company size"]:
        idx = p.find(key)
        if idx >= 0:
            print(" ", p[idx : idx + 100])
