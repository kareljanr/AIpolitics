# -*- coding: utf-8 -*-
import re
import ssl
import urllib.request
from pathlib import Path

out = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2218")
out.mkdir(parents=True, exist_ok=True)
ctx = ssl.create_default_context()
UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)
cands = [
    ("faro", "0893863017", "faro"),
    ("aiesh", "0201712587", "aiesh"),
    ("rew", "0644638937", "rew"),
    ("veerkracht4", "0452454124", "veerkracht-4"),
    ("opnieuw", "0466209120", "opnieuw-co"),
    ("nbsw", "0479456845", "natuur-en-boomgaarden-sociale-werkplaats"),
]


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en"})
    with urllib.request.urlopen(req, context=ctx, timeout=45) as r:
        return r.read()


for key, num, slug in cands:
    url = f"https://www.companyweb.be/en/{num}/{slug}"
    try:
        data = fetch(url)
    except Exception as e:
        print(key, "FAIL", e)
        continue
    path = out / f"{key}_en.html"
    path.write_bytes(data)
    t = data.decode("utf-8", "ignore")
    y = re.search(
        r"Last balance sheet year\s*</div>\s*<div[^>]*>\s*(20\d{2})", t, re.I
    )
    filed = re.search(r"filed on ([0-9\-]{8,10})", t, re.I)
    bal = re.findall(r"(20(?:24|25))\s*:\s*\{", t)
    nums = {}
    for lab in [
        "Turnover",
        "Gross margin",
        "Profit/Loss",
        "Equity",
        "Employees",
        "Total assets",
    ]:
        m = re.search(lab + r".{0,220}?([\d][\d\s]*(?:[.,]\d+)?)", t, re.S)
        nums[lab] = m.group(1).replace(" ", "").replace("\xa0", "") if m else None
    print("===", key, "bytes", len(data))
    print(
        " year_div",
        y.group(1) if y else None,
        "bal_keys",
        bal[:6],
        "filed",
        filed.group(1) if filed else None,
    )
    print(" nums", nums)
