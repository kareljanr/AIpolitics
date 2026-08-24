# -*- coding: utf-8 -*-
import json
import re
import ssl
import urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path(__file__).resolve().parent
KBO = "0432582485"


def fetch(url, path):
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
            data = r.read()
        path.write_bytes(data)
        print("OK", path.name, len(data), url)
        return data.decode("utf-8", "ignore")
    except Exception as e:
        print("FAIL", path.name, type(e).__name__, str(e)[:100])
        return None


def parse_cw(t):
    yblocks = {}
    for y, body in re.findall(r"(20\d\d)\s*:\s*\{([^{}]+)\}", t):

        def g(k, b=body):
            m = re.search(rf'{k}:\s*"([^"]*)"', b)
            return m.group(1) if m else None

        yblocks[y] = {k: g(k) for k in ["omzet", "winst", "bruto_marge", "eigen_vermogen"]}
    fte = re.search(r"(\d[\d.,]*)\s*FTE", t)
    filed = re.search(r"filed on ([0-9-]{10})", t)
    title = re.search(r"<title>([^<]+)", t)
    return {
        "title": title.group(1) if title else None,
        "fte": fte.group(1).replace(",", ".") if fte else None,
        "filed": filed.group(1) if filed else None,
        "years": yblocks,
    }


urls = {
    "en": f"https://www.companyweb.be/en/{KBO}",
    "nl": f"https://www.companyweb.be/nl/{KBO}/woonzorgcentrum-sint-bernardus-vzw",
    "fr": f"https://www.companyweb.be/fr/{KBO}",
    "kbo": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer={KBO}",
    "site": "https://www.wzc-sintbernardus.be/",
    "site2": "https://www.sintbernardus.be/",
    "site3": "https://www.wzcsintbernardus.be/",
}

pages = {}
for label, url in urls.items():
    t = fetch(url, out / f"bernardus_{label}.html")
    if t:
        pages[label] = t

if "en" in pages:
    info = parse_cw(pages["en"])
    print(json.dumps(info, indent=2))

if "kbo" in pages:
    t = pages["kbo"]
    for pat in [
        r"Status van de entiteit</td>\s*<td[^>]*>\s*<[^>]+>\s*([^<\n]+)",
        r"Rechtsvorm</td>\s*<td[^>]*>.*?>([^<\n]+)",
        r"Adres van de zetel</td>\s*<td[^>]*>\s*([^<]+)",
        r"E-mailadres</td>\s*<td[^>]*>\s*([^<]+)",
        r"Nummer van de vestigingseenheid</td>",
        r"87\.\d{3}",
        r"Aantal vestigingseenheden.*?</td>\s*<td[^>]*>\s*(\d+)",
    ]:
        m = re.search(pat, t, re.I | re.S)
        if m:
            print("KBO", pat[:40], "->", re.sub(r"\s+", " ", m.group(0 if m.lastindex is None else 1))[:120])
    # simpler extracts
    if "Actief" in t:
        print("KBO status Actief present")
    ve = re.findall(r"vestigingseenheid", t, re.I)
    print("VE mentions", len(ve))
    emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", t)
    print("KBO emails", emails[:5])
    addrs = re.findall(r"\d{4}\s+[A-Za-zÀ-ÿ' \-]+", t)
    print("addrs sample", addrs[:8])

for label in ["site", "site2", "site3"]:
    if label in pages:
        t = pages[label]
        emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", t)
        emails = [e for e in emails if "wix" not in e.lower() and "example" not in e.lower()]
        print(label, "emails", emails[:8], "len", len(t))
        tels = re.findall(r"0\d{1,2}[./\s-]?\d{2,3}[./\s-]?\d{2}[./\s-]?\d{2}", t)
        print(label, "tels", tels[:5])
