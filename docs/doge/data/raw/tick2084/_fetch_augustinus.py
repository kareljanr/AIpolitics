# -*- coding: utf-8 -*-
import json
import re
import urllib.request
from pathlib import Path

RAW = Path("docs/doge/data/raw/tick2084")
RAW.mkdir(parents=True, exist_ok=True)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
KBO = "0459770496"
SLUG = "woonzorgcentrum-sint-augustinus"


def fetch(url: str, out: Path):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "nl,en,fr"})
    with urllib.request.urlopen(req, timeout=45) as resp:
        data = resp.read()
        final = resp.geturl()
    out.write_bytes(data)
    return data.decode("utf-8", "replace"), final


def parse_cw(text: str):
    ye_m = re.search(r"kernCijfers\s*=\s*\{\s*(20\d\d)\s*:", text)
    ye = ye_m.group(1) if ye_m else None
    # extract block for YE
    block = None
    if ye:
        m = re.search(rf"{ye}\s*:\s*\{{(.*?)\n\s*\}}", text, re.S)
        if m:
            block = m.group(1)
    fields = {}
    if block:
        for key in [
            "winst",
            "eigen_vermogen",
            "bruto_marge",
            "omzet",
            "bedrijfsopbrengsten",
            "totale_activa",
            "totale_schulden",
            "aantal_werknemers",
            "cash",
            "ebitda",
        ]:
            m = re.search(rf'{key}:\s*"([^"]*)"', block)
            if m:
                fields[key] = m.group(1)
    # also prior year
    prior = {}
    if ye:
        py = str(int(ye) - 1)
        m = re.search(rf"{py}\s*:\s*\{{(.*?)\n\s*\}}", text, re.S)
        if m:
            b = m.group(1)
            for key in ["winst", "eigen_vermogen", "bruto_marge", "omzet", "aantal_werknemers", "totale_activa", "totale_schulden"]:
                mm = re.search(rf'{key}:\s*"([^"]*)"', b)
                if mm:
                    prior[key] = mm.group(1)
    filed = re.search(r"neergelegd op ([0-9.\-]+)", text)
    email = re.search(r"mailto:([a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,})", text)
    addr = re.search(r"zetel[^<]{0,40}|social[^<]{0,40}", text, re.I)
    # address often in structured place
    street = re.search(r'(?:straat|laan|weg|plein|dreef)[^,<\n]{0,40},\s*\d{4}\s+[A-Za-z\- ]+', text, re.I)
    # try JSON-LD
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', text, re.S):
        try:
            jd = json.loads(m.group(1))
            print("LD", jd if not isinstance(jd, dict) else {k: jd.get(k) for k in list(jd)[:12]})
        except Exception:
            pass
    return {
        "ye": ye,
        "fields": fields,
        "prior": prior,
        "filed": filed.group(1) if filed else None,
        "email": email.group(1) if email else None,
        "street_hint": street.group(0)[:120] if street else None,
    }


for lang in ("nl", "en", "fr"):
    url = f"https://www.companyweb.be/{lang}/{KBO}/{SLUG}"
    text, final = fetch(url, RAW / f"aug_{lang}.html")
    info = parse_cw(text)
    print("===", lang, final)
    print(info)

# KBO
kbo_url = f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={KBO}"
try:
    text, final = fetch(kbo_url, RAW / "kbo_aug.html")
    print("=== KBO", final, "len", len(text))
    # status / form / email
    for pat in [
        r"Status van de entiteit</td>\s*<td[^>]*>\s*<span[^>]*>([^<]+)",
        r"Rechtsvorm</td>\s*<td[^>]*>.*?>([^<]+)",
        r"E-mail:\s*</td>\s*<td[^>]*>\s*([^<]+)",
        r"Adres van de zetel</td>\s*<td[^>]*>\s*(.*?)</td>",
        r"Aantal bijkantoren",
        r"aanbestedende overheid",
        r"Datum van einde rechtspersonen",
    ]:
        m = re.search(pat, text, re.S | re.I)
        if m:
            print(pat[:40], "->", re.sub(r"\s+", " ", m.group(0 if m.lastindex is None else 1))[:200])
except Exception as e:
    print("KBO FAIL", e)

# site search hints
for url in [
    "https://www.google.com/search?q=WZC+Sint-Augustinus+Halle",
    "https://www.woonzorghalle.be/",
    "https://www.ocmwhalle.be/",
]:
    pass
