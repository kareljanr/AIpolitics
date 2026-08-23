# -*- coding: utf-8 -*-
import re
import ssl
import urllib.request
from html import unescape
from pathlib import Path

RAW = Path(__file__).resolve().parent
RAW.mkdir(parents=True, exist_ok=True)
CTX = ssl.create_default_context()
UA = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "nl-BE,nl;q=0.9,en;q=0.8,fr;q=0.7",
}

# Prefer IDELUX Eau; fallback Camillus / Zilverlinde already fetched in tick2105
cands = [
    ("0204359994", "idelux-eau", "idelux_eau"),
    ("0204.359.994", "idelux-eau", "idelux_eau_dot"),
]


def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=CTX, timeout=45) as resp:
        return resp.read()


pat = re.compile(
    r'(20\d\d)\s*:\s*\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",'
    r'\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)"'
)

kbo = "0204359994"
for lang in ("nl", "en", "fr"):
    url = f"https://www.companyweb.be/{lang}/{kbo}/idelux-eau"
    try:
        body = fetch(url)
    except Exception as e:
        print(f"FAIL cw {lang}: {e}")
        # try alternate slug
        for slug in ("idelux", "eau", "idelux-eau-sc", "association-intercommunale"):
            try:
                url2 = f"https://www.companyweb.be/{lang}/{kbo}/{slug}"
                body = fetch(url2)
                print(f"OK alt slug {slug}/{lang}")
                break
            except Exception as e2:
                body = None
                last = e2
        if body is None:
            print(f"FAIL all {lang}: {last}")
            continue
    (RAW / f"idelux_eau_{lang}.html").write_bytes(body)
    html = body.decode("utf-8", "ignore")
    text = unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html)))
    title_m = re.search(r"<title>([^<]+)</title>", html, re.I)
    lb = re.search(r"(?:Laatste balansjaar|Last balance sheet year|Dernier bilan)\s+(\d{4})", text, re.I)
    euros = {m.group(1): m.groups()[1:] for m in pat.finditer(html)}
    fte = re.search(r"([\d\.,]+)\s*FTE", text)
    neer = re.search(r"(?:neergelegd op|filed on|déposés le)\s+([\d\-]+)", text, re.I)
    print(
        f"lang={lang}|title={(title_m.group(1)[:80] if title_m else '?')}|"
        f"year={lb.group(1) if lb else '?'}|fte={fte.group(1) if fte else '?'}|"
        f"neer={neer.group(1) if neer else '?'}|e25={euros.get('2025')}|e24={euros.get('2024')}"
    )

# KBO
url = f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={kbo}"
try:
    body = fetch(url)
    (RAW / "idelux_eau_kbo.html").write_bytes(body)
    text = unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", body.decode("utf-8", "ignore"))))
    print("KBO ok", "Actief" in text or "Active" in text, "len", len(body))
    for patn in [r"Nacebel[^\d]*(\d{2}\.\d{3})", r"(36\.\d{3}|37\.\d{3}|42\.\d{3})", r"Établissements|Vestigingseenheden[^\d]*(\d+)"]:
        ms = re.findall(patn, text, re.I)
        if ms:
            print(" ", patn, ms[:8])
except Exception as e:
    print("KBO FAIL", e)

# also contact / NBB consult pages
for name, url in [
    ("nbb", f"https://consult.cbso.nbb.be/consult-enterprise/{kbo}"),
    ("idelux_site", "https://www.idelux.be/"),
]:
    try:
        body = fetch(url)
        (RAW / f"{name}.html").write_bytes(body)
        print(name, "ok", len(body))
    except Exception as e:
        print(name, "FAIL", e)
