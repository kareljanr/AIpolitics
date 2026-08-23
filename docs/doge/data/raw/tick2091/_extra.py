# -*- coding: utf-8 -*-
import re
import urllib.request
from pathlib import Path

RAW = Path("docs/doge/data/raw/tick2091")
UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)


def fetch(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "nl,en;q=0.8"})
    with urllib.request.urlopen(req, timeout=45) as resp:
        return resp.read()


for lang in ("en", "fr"):
    t = (RAW / f"sed_{lang}.html").read_text(encoding="utf-8", errors="replace")
    fte = re.search(r'amountOfEmployees\s*=\s*"([^"]+)"', t)
    # look for previous year FTE patterns
    for pat in [
        r"(\d{4}).{0,40}(\d+[.,]\d)\s*FTE",
        r'employees[^"]{0,40}"([^"]+)"',
        r"Personeel|Personnel|Employés",
    ]:
        ms = list(re.finditer(pat, t, re.I))
        print(lang, pat[:40], "n=", len(ms), "first=", (ms[0].group(0)[:80] if ms else None))
    print(lang, "fte", fte.group(1) if fte else None)

# site
for url in [
    "https://st-elisabethsdal.be/",
    "https://st-elisabethsdal.be/vestiging/zoutleeuw/contact/",
    "https://st-elisabethsdal.be/contact/",
]:
    try:
        data = fetch(url)
        (RAW / ("site_" + url.rstrip("/").split("/")[-1].replace(".", "_") + ".html")).write_bytes(data)
        t = data.decode("utf-8", "replace")
        emails = sorted(set(re.findall(r"[A-Za-z0-9._%+\-]+@vzwsed\.be", t, re.I)))
        print("SITE", url, "bytes", len(data), "emails", emails)
    except Exception as e:
        print("SITE FAIL", url, type(e).__name__, str(e)[:100])
