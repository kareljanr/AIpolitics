# -*- coding: utf-8 -*-
import json
import re
import ssl
import urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path(__file__).resolve().parent
KBO = "0450755634"


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
    nace = list(dict.fromkeys(re.findall(r"(87\.\d{3}|88\.\d{3}|86\.\d{3}|68\.\d{3}|55\.\d{3}|41\.\d{3})", t)))
    # activities text
    act = re.search(r"Activities[^<]{0,40}</[^>]+>\s*<[^>]+>([^<]{10,200})", t, re.I)
    slug = re.search(r'canonical" href="https://www\.companyweb\.be/[^"]+/(\d+)/([^"]+)"', t)
    return {
        "title": title.group(1) if title else None,
        "fte": fte.group(1).replace(",", ".") if fte else None,
        "filed": filed.group(1) if filed else None,
        "years": yblocks,
        "nace": nace[:10],
        "act": act.group(1).strip() if act else None,
        "slug": slug.group(2) if slug else None,
    }


urls = {
    "en": f"https://www.companyweb.be/en/{KBO}",
    "nl": f"https://www.companyweb.be/nl/{KBO}",
    "fr": f"https://www.companyweb.be/fr/{KBO}",
    "kbo": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer={KBO}",
}

pages = {}
for label, url in urls.items():
    t = fetch(url, out / f"oudenburg_{label}.html")
    if t:
        pages[label] = t

if "en" in pages:
    info = parse_cw(pages["en"])
    print(json.dumps(info, indent=2, ensure_ascii=False))
    # try find NL slug for nicer URL
    t = pages["en"]
    for m in re.findall(r"https://www\.companyweb\.be/nl/\d+/[a-z0-9\-]+", t):
        print("NL_URL", m)
        break
    for m in re.findall(r"https://www\.companyweb\.be/(?:nl|en|fr)/\d+/[a-z0-9\-]+", t)[:5]:
        print("CW_URL", m)

if "nl" in pages:
    info_nl = parse_cw(pages["nl"])
    print("NL", json.dumps(info_nl, indent=2, ensure_ascii=False))
    # redirect / actual title path
    t = pages["nl"]
    if "Error 404" in t or "404" in (re.search(r"<title>([^<]+)", t).group(1) if re.search(r"<title>", t) else ""):
        print("NL 404 — need slug")
    emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", t)
    emails = [e for e in emails if "companyweb" not in e.lower()]
    print("NL emails", emails[:8])

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
    ]:
        m = re.search(pat, t, re.I | re.S)
        if m:
            print("KBO", name, re.sub(r"\s+", " ", m.group(1))[:120])
    nace = re.findall(r"87\.\d{3}|88\.\d{3}|86\.\d{3}|68\.\d{3}|55\.\d{3}", t)
    print("KBO nace", list(dict.fromkeys(nace))[:10])
    # activity descriptions near NACE
    for m in re.finditer(r"(87\.\d{3}|88\.\d{3}|68\.\d{3}|55\.\d{3})[^<]{0,5}</td>\s*<td[^>]*>\s*([^<]+)", t):
        print("NACE_DESC", m.group(1), m.group(2)[:100])
    emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", t)
    print("KBO emails", emails[:5])
    # website
    webs = re.findall(r"https?://[^\s\"'<>]+", t)
    webs = [w for w in webs if "economie" not in w and "kbopub" not in w]
    print("webs", webs[:8])

# also try known care site names
for label, url in [
    ("site1", "https://www.residentieoudenburg.be/"),
    ("site2", "https://residentie-oudenburg.be/"),
    ("site3", "https://www.oudenburg.be/"),
]:
    t = fetch(url, out / f"oudenburg_{label}.html")
    if t and "404" not in (re.search(r"<title>([^<]+)", t).group(1) if re.search(r"<title>", t) else ""):
        emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", t)
        emails = [e for e in emails if "wix" not in e.lower() and "example" not in e.lower() and "sentry" not in e.lower()]
        print(label, "emails", emails[:8], "len", len(t))
        tels = re.findall(r"0\d{1,2}[./\s-]?\d{2,3}[./\s-]?\d{2}[./\s-]?\d{2}", t)
        print(label, "tels", tels[:5])
        title = re.search(r"<title>([^<]+)", t)
        print(label, "title", title.group(1)[:100] if title else "?")
