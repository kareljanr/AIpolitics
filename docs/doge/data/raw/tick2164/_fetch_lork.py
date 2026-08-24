# -*- coding: utf-8 -*-
import json
import re
import ssl
import urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path(__file__).resolve().parent
KBO = "0755822317"


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

        yblocks[y] = {
            k: g(k) for k in ["omzet", "winst", "bruto_marge", "eigen_vermogen"]
        }
    fte = re.search(r"(\d[\d.,]*)\s*FTE", t)
    filed = re.search(r"filed on ([0-9-]{10})", t)
    title = re.search(r"<title>([^<]+)", t)
    nace = list(
        dict.fromkeys(re.findall(r"(87\.\d{3}|88\.\d{3}|86\.\d{3}|68\.\d{3})", t))
    )
    return {
        "title": title.group(1) if title else None,
        "fte": fte.group(1).replace(",", ".") if fte else None,
        "filed": filed.group(1) if filed else None,
        "years": {y: yblocks[y] for y in sorted(yblocks, reverse=True)[:4]},
        "nace": nace[:10],
    }


urls = {
    "en": f"https://www.companyweb.be/en/{KBO}",
    "nl": f"https://www.companyweb.be/nl/{KBO}/wzc-foyer-de-lork-hoeselt",
    "nl2": f"https://www.companyweb.be/nl/{KBO}",
    "fr": f"https://www.companyweb.be/fr/{KBO}",
    "kbo": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer={KBO}",
}

pages = {}
for label, url in urls.items():
    t = fetch(url, out / f"lork_{label}.html")
    if t:
        pages[label] = t

for label in ["en", "nl", "nl2", "fr"]:
    if label in pages:
        print(label, json.dumps(parse_cw(pages[label]), indent=2, ensure_ascii=False))

if "kbo" in pages:
    t = pages["kbo"]
    print("KBO Actief", "Actief" in t)
    for pat, name in [
        (r"Rechtsvorm</td>\s*<td[^>]*>.*?<[^>]+>\s*([^<\n]+)", "form"),
        (r"Adres van de zetel</td>\s*<td[^>]*>\s*([^<]+)", "addr"),
        (r"E-mailadres</td>\s*<td[^>]*>\s*([^<]+)", "email"),
        (r"Telefoonnummer</td>\s*<td[^>]*>\s*([^<]+)", "tel"),
        (r"Aantal vestigingseenheden.*?</td>\s*<td[^>]*>\s*(\d+)", "ve"),
        (r"Datum van de oprichting</td>\s*<td[^>]*>\s*([^<]+)", "start"),
        (r"Status van de entiteit</td>\s*<td[^>]*>\s*<[^>]+>\s*([^<\n]+)", "status"),
    ]:
        m = re.search(pat, t, re.I | re.S)
        if m:
            print("KBO", name, re.sub(r"\s+", " ", m.group(1))[:140])
    nace = re.findall(r"87\.\d{3}|88\.\d{3}|86\.\d{3}|68\.\d{3}", t)
    print("KBO nace", list(dict.fromkeys(nace))[:10])
    for m in re.finditer(
        r"(87\.\d{3}|88\.\d{3}|68\.\d{3})[^<]{0,5}</td>\s*<td[^>]*>\s*([^<]+)", t
    ):
        print("NACE_DESC", m.group(1), m.group(2)[:120])
    emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", t)
    print("KBO emails", emails[:5])
    # address city
    addrs = re.findall(r"\d{4}\s+[A-Za-zÀ-ÿ' \-]+", t)
    print("addrs", addrs[:8])

# Foyer De Lork parent was Geel - site contact
for label, url in [
    ("site_lork", "https://www.foyerdelork.be/"),
    ("site_lork2", "https://foyerdelork.be/"),
    ("site_hoeselt", "https://www.hoeselt.be/"),
]:
    t = fetch(url, out / f"lork_{label}.html")
    if t:
        title = re.search(r"<title>([^<]+)", t)
        print(label, "title", title.group(1)[:100] if title else "?", "len", len(t))
        emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", t)
        emails = [
            e
            for e in emails
            if not any(x in e.lower() for x in ("wix", "example", "sentry", "schema"))
        ]
        print(label, "emails", emails[:10])
        tels = re.findall(r"0\d{1,2}[./\s-]?\d{2,3}[./\s-]?\d{2}[./\s-]?\d{2}", t)
        print(label, "tels", list(dict.fromkeys(tels))[:6])
