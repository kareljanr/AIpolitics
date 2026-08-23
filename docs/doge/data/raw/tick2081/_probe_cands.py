# -*- coding: utf-8 -*-
import csv
import re
import urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
RAW = Path("docs/doge/data/raw/tick2081")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

# Build mined KBO set from entities notes + queue
mined = set()
with open("docs/doge/data/entities.csv", encoding="utf-8-sig", newline="") as f:
    for r in csv.DictReader(f):
        blob = " ".join((r.get(k) or "") for k in r)
        for m in re.findall(r"0\d{3}\.\d{3}\.\d{3}", blob):
            mined.add(m.replace(".", ""))
        for m in re.findall(r"0\d{9}", blob):
            mined.add(m)
with open("docs/doge/data/research_queue.csv", encoding="utf-8-sig", newline="") as f:
    for r in csv.DictReader(f):
        blob = " ".join((r.get(k) or "") for k in r)
        for m in re.findall(r"0\d{3}\.\d{3}\.\d{3}", blob):
            mined.add(m.replace(".", ""))

CANDS = [
    ("0449425546", "woonzorgcentrum-de-wijtshage", "De Wijtshage"),
    ("0696715807", "woonzorgcentrum-crayenhof", "Crayenhof"),  # guess from 0696.715.?
    ("0416135970", "heidehuis", "Heidehuis"),
    ("0434135970", "heidehuis", "Heidehuis vzw"),
    ("0478123456", "x", "skip"),
    # try Northdata-ish known WZCs
    ("0405567890", "x", "skip"),
    ("0425901234", "woonzorgcentrum-zonneweelde", "Zonneweelde"),
    ("0460123456", "x", "skip"),
]

# Better: fetch CoBRHA / search pages for known free names via companyweb search is blocked
# Direct known KBOs from web:
URLS = [
    "https://www.companyweb.be/nl/0449425546/rust-en-verzorgingstehuis-de-wijtshage",
    "https://www.companyweb.be/nl/0449425546/de-wijtshage",
    "https://www.companyweb.be/nl/0449425546/woonzorgcentrum-de-wijtshage",
    "https://www.companyweb.be/nl/0434135970/heidehuis",
    "https://kbopub.economie.fgov.be/kbopub/zoeknaamfonetischform.html?searchWord=Zonneweelde+woonzorg&filterEnkelActieve=true",
]


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "nl"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read(), resp.geturl()


# Resolve De Wijtshage via KBO then companyweb
for kbo in ["0449425546", "0434135970", "0425567891"]:
    print("KBO check", kbo, "mined" if kbo in mined else "FREE")

# Fetch wijtshage variants
for url in URLS[:4]:
    try:
        data, final = fetch(url)
        text = data.decode("utf-8", "replace")
        title = re.search(r"<title>([^<]+)</title>", text)
        ye = re.search(r"kernCijfers\s*=\s*\{\s*(20\d\d)\s*:", text)
        print("OK", final[:90], "title", (title.group(1)[:90] if title else None), "YE", ye.group(1) if ye else None, "bytes", len(data))
        if ye and ye.group(1) == "2025" and "404" not in (title.group(1) if title else ""):
            name = "cand_" + re.sub(r"\W+", "_", final.split("/")[-1])[:40] + ".html"
            (RAW / name).write_bytes(data)
            print("SAVED", name)
            # parse metrics
            for ym in list(
                re.finditer(
                    r"(20\d\d)\s*:\s*\{\s*winst:\s*\"([^\"]+)\",\s*eigen_vermogen:\s*\"([^\"]+)\",\s*bruto_marge:\s*\"([^\"]+)\",\s*omzet:\s*\"([^\"]+)\"",
                    text,
                )
            )[:2]:
                print(" ", ym.group(1), ym.group(2), ym.group(5))
    except Exception as e:
        print("FAIL", url[:70], e)

# KBO name search Zonneweelde
try:
    data, final = fetch(
        "https://kbopub.economie.fgov.be/kbopub/zoeknaamfonetisch.html?nieuw=1&searchWord=Zonneweelde&filterEnkelActieve=true"
    )
    text = data.decode("utf-8", "replace")
    (RAW / "kbo_search_zonne.html").write_bytes(data)
    # extract enterprise numbers
    nums = re.findall(r"ondernemingsnummer=(\d+)", text)
    names = re.findall(r"<td[^>]*>\s*([^<]{3,80})\s*</td>", text)
    print("Zonne KBO hits", nums[:10])
    for n in nums[:8]:
        print(" ", n, "mined" if n in mined else "FREE")
except Exception as e:
    print("Zonne search fail", e)

# Also search Wijtshage / Crayenhof / Meander
for term in ["Wijtshage", "Crayenhof", "Meander+woonzorg", "Zinnebinnen", "De+Klippel"]:
    try:
        url = f"https://kbopub.economie.fgov.be/kbopub/zoeknaamfonetisch.html?nieuw=1&searchWord={term}&filterEnkelActieve=true"
        data, final = fetch(url)
        text = data.decode("utf-8", "replace")
        nums = re.findall(r"ondernemingsnummer=(\d+)", text)
        print(term, "nums", nums[:6], ["FREE" if n not in mined else "HIT" for n in nums[:6]])
    except Exception as e:
        print(term, "fail", e)
