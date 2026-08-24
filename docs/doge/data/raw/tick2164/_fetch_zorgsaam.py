# -*- coding: utf-8 -*-
import json
import re
import ssl
import urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path(__file__).resolve().parent
KBO = "0470673890"


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
    filed = re.search(r"filed on ([0-9-]{10})", t) or re.search(
        r"neergelegd op ([0-9-]{10})", t
    )
    title = re.search(r"<title>([^<]+)", t)
    nace = list(
        dict.fromkeys(re.findall(r"(87\.\d{3}|88\.\d{3}|86\.\d{3}|84\.\d{3})", t))
    )
    slug = None
    m = re.search(r"companyweb\.be/nl/\d+/([a-z0-9\-]+)", t)
    if m:
        slug = m.group(1)
    return {
        "title": title.group(1) if title else None,
        "fte": fte.group(1) if fte else None,
        "filed": filed.group(1) if filed else None,
        "years": {y: yblocks[y] for y in sorted(yblocks, reverse=True)[:3]},
        "nace": nace[:12],
        "slug": slug,
    }


urls = {
    "en": f"https://www.companyweb.be/en/{KBO}",
    "nl": f"https://www.companyweb.be/nl/{KBO}",
    "fr": f"https://www.companyweb.be/fr/{KBO}",
    "kbo": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer={KBO}",
}

pages = {}
for label, url in urls.items():
    t = fetch(url, out / f"zorgsaam_{label}.html")
    if t:
        pages[label] = t

for label in ["en", "nl", "fr"]:
    if label in pages:
        print(label, json.dumps(parse_cw(pages[label]), indent=2, ensure_ascii=False))

if "kbo" in pages:
    t = pages["kbo"]
    print("KBO Actief", "Actief" in t)
    for pat, name in [
        (r"Rechtsvorm:\s*</td><td[^>]*>\s*([^<]+)", "form"),
        (
            r"Adres van de zetel:</td><td[^>]*>\s*(.*?)</td>",
            "addr",
        ),
        (r"Aantal vestigingseenheden \(VE\):\s*</td><td[^>]*>.*?<strong>(\d+)</strong>", "ve"),
        (r"Datum van de oprichting:</td><td[^>]*>\s*([^<]+)", "start"),
        (r"E-mail:\s*</td><td[^>]*>\s*([^<]+)", "email"),
        (r"Telefoonnummer:\s*</td><td[^>]*>\s*([^<]+)", "tel"),
        (r"Webadres:\s*</td><td[^>]*>\s*([^<]+)", "web"),
        (r"aanbestedende overheid", "aanbestedende"),
    ]:
        m = re.search(pat, t, re.I | re.S)
        if m:
            val = re.sub(r"<[^>]+>", " ", m.group(1) if m.lastindex else m.group(0))
            print("KBO", name, re.sub(r"\s+", " ", val)[:160])
    nace = re.findall(r"87\.\d{3}|88\.\d{3}|86\.\d{3}", t)
    print("KBO nace", list(dict.fromkeys(nace))[:15])
    for m in re.finditer(
        r"nace\.code=(\d+)[^>]*>\s*([\d.]+)</a>\s*&nbsp;-&nbsp;\s*([^<]+)", t
    ):
        print("NACE_DESC", m.group(2), m.group(3)[:100])
    emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", t)
    print("KBO emails", emails[:5])
    if "aanbestedende overheid" in t.lower():
        print("KBO has aanbestedende overheid")

# sites
for label, url in [
    ("site1", "https://www.zorg-saam.be/"),
    ("site2", "https://zorg-saam.be/"),
    ("site3", "https://www.zorgsaam.be/"),
    ("site4", "https://www.zusterskindsheidjesu.be/"),
]:
    t = fetch(url, out / f"zorgsaam_{label}.html")
    if t:
        title = re.search(r"<title>([^<]+)", t)
        print(label, "title", title.group(1)[:100] if title else "?", "len", len(t))
        emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", t)
        emails = [
            e
            for e in emails
            if not any(
                x in e.lower()
                for x in ("wix", "example", "sentry", "schema", "cloudflare")
            )
        ]
        print(label, "emails", list(dict.fromkeys(emails))[:10])
        tels = re.findall(r"0\d{1,2}[./\s-]?\d{2,3}[./\s-]?\d{2}[./\s-]?\d{2}", t)
        print(label, "tels", list(dict.fromkeys(tels))[:6])
