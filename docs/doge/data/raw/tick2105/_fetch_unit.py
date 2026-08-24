# -*- coding: utf-8 -*-
import re
import ssl
import urllib.request
from html import unescape
from pathlib import Path

RAW = Path(__file__).resolve().parent
CTX = ssl.create_default_context()
UA = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "nl-BE,nl;q=0.9,en;q=0.8,fr;q=0.7",
}

cands = [
    ("0417958152", "woonzorgcentrum-sint-camillus", "camillus"),
    ("0452865383", "rusthuis-sint-jozef", "sj_ninove"),
    ("0445175263", "wzc-zilverlinde", "zilverlinde"),
    ("0479401318", "woon-en-zorgcentrum-ter-burg", "ter_burg"),
    ("0424236725", "woon-en-zorgcentrum-sint-antonius", "sint_antonius"),
    ("0810616132", "molenheide-woonzorgcentrum", "molenheide"),
    ("0893863017", "faro-vlaams-steunpunt-voor-cultureel-erfgoed", "faro"),
    ("0201712587", "association-intercommunale-d-electricite-du-sud-du-hainaut", "aiesh"),
    ("0644638937", "reseau-d-energies-de-wavre", "rew"),
]


def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=CTX, timeout=45) as resp:
        return resp.read()


def parse(html: str):
    text = unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html)))
    title_m = re.search(r"<title>([^<]+)</title>", html, re.I)
    title = title_m.group(1).strip()[:120] if title_m else "?"
    lb = re.search(r"Laatste balansjaar\s+(\d{4})", text)
    # financial table: find 2025 row numbers via embedded JSON-like pattern used by CW
    pat = re.compile(
        r'(20\d\d)\s*:\s*\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",'
        r'\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)"'
    )
    euros = {
        m.group(1): {
            "pnl": m.group(2),
            "eq": m.group(3),
            "bruto": m.group(4),
            "omzet": m.group(5),
        }
        for m in pat.finditer(html)
    }
    # FTE
    fte = re.search(r"Bedrijfsgrootte[^0-9]*([\d\.,]+)\s*FTE", text)
    if not fte:
        fte = re.search(r"Personeel\s+([\d\.,]+)", text)
    # filing
    neer = re.search(r"neergelegd op\s+([\d\-]+)", text, re.I)
    # address snippet
    addr = re.search(r"(\d{4}\s+[A-Za-zÀ-ÿ\- ]+)", text[text.find("Bedrijfsinformatie") : text.find("Bedrijfsinformatie") + 800] if "Bedrijfsinformatie" in text else text[:1500])
    return {
        "title": title,
        "year": lb.group(1) if lb else "?",
        "euros": euros,
        "fte": fte.group(1) if fte else "?",
        "neer": neer.group(1) if neer else "?",
        "text_snip": text[0:400],
    }


for kbo, slug, tag in cands:
    for lang, path_tag in [("nl", "nl"), ("en", "en"), ("fr", "fr")]:
        url = f"https://www.companyweb.be/{lang}/{kbo}/{slug}"
        try:
            body = fetch(url)
        except Exception as e:
            print(f"FAIL {tag}/{lang}: {e}")
            continue
        out = RAW / f"{tag}_{path_tag}.html"
        out.write_bytes(body)
        if lang == "nl":
            info = parse(body.decode("utf-8", "ignore"))
            e25 = info["euros"].get("2025")
            e24 = info["euros"].get("2024")
            print(
                f"{tag}|{kbo}|year={info['year']}|fte={info['fte']}|neer={info['neer']}|"
                f"e25={e25}|e24={e24}|{info['title'][:70]}"
            )

# KBO pages for top YE2025 hit
for kbo, tag in [
    ("0417958152", "camillus"),
    ("0445175263", "zilverlinde"),
    ("0479401318", "ter_burg"),
    ("0424236725", "sint_antonius"),
    ("0810616132", "molenheide"),
]:
    url = f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={kbo}"
    try:
        body = fetch(url)
        (RAW / f"{tag}_kbo.html").write_bytes(body)
        text = unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", body.decode("utf-8", "ignore"))))
        status = "Actief" if "Actief" in text or "Active" in text else "?"
        nace = re.findall(r"(87\.\d{3}|88\.\d{3}|86\.\d{3})", text)
        print(f"KBO {tag}|{kbo}|{status}|nace={nace[:6]}|len={len(body)}")
    except Exception as e:
        print(f"KBO FAIL {tag}: {e}")
