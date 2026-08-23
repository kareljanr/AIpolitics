# -*- coding: utf-8 -*-
"""Hunt unused YE2025 MRS/WZC via known Korian homes + CW name search fallbacks."""
import re
import ssl
import urllib.parse
import urllib.request
from html import unescape
from pathlib import Path

RAW = Path(__file__).resolve().parent
DATA = RAW.parents[1]
CTX = ssl.create_default_context()
UA = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "nl-BE,nl;q=0.9,fr;q=0.8,en;q=0.7",
}
PAT = re.compile(
    r'(20\d\d)\s*:\s*\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",'
    r'\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)"'
)

taken = (DATA / "entities.csv").read_text(encoding="utf-8", errors="replace")
taken += (DATA / "leaderboard.csv").read_text(encoding="utf-8", errors="replace")
dn = (
    "0412.640.671 0405.311.530 0443.082.637 0452.865.383 0445.175.263 "
    "0417.958.152 0466.961.859 0435.357.675 0869.769.702 0887.690.451 "
    "0893.863.017 0201.712.587 0644.638.937 0877.556.624"
)
taken += dn

# Try name-slug URLs / known search terms on companyweb
# First resolve via kbo pub or companyweb search pages for these names
names = [
    "les-sittelles",
    "la-passerinette",
    "les-charmilles",
    "le-chenoy",
    "le-colvert",
    "les-cheveux-d-argent",
    "golden-morgen",
    "heris",
    "bellevue",
    "jardins-d-astrid",
    "air-du-temps",
    "ohana",
    "clos-de-la-rivelaine",
    "parchemin",
    "domaine-des-lys",
    "residence-le-lys",
    "le-lys",
]


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=CTX, timeout=40) as resp:
        return resp.read()


def parse(html: str):
    text = unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html)))
    title = re.search(r"<title>([^<]+)</title>", html, re.I)
    lb = re.search(
        r"(?:Laatste balansjaar|Last balance sheet year|Dernier bilan)\s+(\d{4})",
        text,
        re.I,
    )
    euros = {m.group(1): m.groups()[1:] for m in PAT.finditer(html)}
    ftes = re.findall(r"([\d\.,]+)\s*FTE", text)
    neer = re.search(
        r"(?:neergelegd op|filed on|déposés le)\s+([\d\-]+)", text, re.I
    )
    kbo_m = re.search(r"BE\s*(\d{4})[.\s]?(\d{3})[.\s]?(\d{3})", html)
    kbo = (
        f"{kbo_m.group(1)}.{kbo_m.group(2)}.{kbo_m.group(3)}" if kbo_m else "?"
    )
    nace = re.findall(r"(87\.\d{3}|86\.\d{3})", text)
    return {
        "title": title.group(1)[:110] if title else "?",
        "year": lb.group(1) if lb else "?",
        "neer": neer.group(1) if neer else "?",
        "euros": euros,
        "ftes": ftes[:4],
        "kbo": kbo,
        "nace": nace[:6],
    }


# Use companyweb search
print("=== CW search for Korian-path MRS names ===")
for name in names:
    q = urllib.parse.quote(name.replace("-", " "))
    try:
        # companyweb search endpoint often /nl/search?q=
        body = fetch(f"https://www.companyweb.be/nl/search?q={q}")
        (RAW / f"search_{name}.html").write_bytes(body)
        html = body.decode("utf-8", "ignore")
        # extract company links /kbos
        kbods = re.findall(
            r'href="/(?:nl|en|fr)/(\d{10})/([^"]+)"', html
        )
        # also BE numbers
        bes = re.findall(r"BE\s*(\d{4})\.(\d{3})\.(\d{3})", html)
        print(f"\nSEARCH {name}: links={len(kbods)} bes={len(bes)}")
        seen = set()
        for digits, slug in kbods[:8]:
            if digits in seen:
                continue
            seen.add(digits)
            dotted = f"{digits[:4]}.{digits[4:7]}.{digits[7:]}"
            already = dotted in taken or digits in taken
            try:
                b2 = fetch(f"https://www.companyweb.be/nl/{digits}/{slug}")
                (RAW / f"cand_{digits}_nl.html").write_bytes(b2)
                info = parse(b2.decode("utf-8", "ignore"))
                e25 = info["euros"].get("2025")
                flag = "Y25" if info["year"] == "2025" or e25 else f"y{info['year']}"
                print(
                    f"  {flag} {'TAKEN' if already else 'FREE'} {dotted} "
                    f"{slug[:40]} e25={e25} fte={info['ftes']} "
                    f"title={info['title'][:55]}"
                )
            except Exception as e:
                print(f"  ERR {digits} {e}")
        for a, b, c in bes[:5]:
            dotted = f"{a}.{b}.{c}"
            digits = a + b + c
            if digits in seen:
                continue
            seen.add(digits)
            already = dotted in taken or digits in taken
            try:
                b2 = fetch(f"https://www.companyweb.be/nl/{digits}")
                (RAW / f"cand_{digits}_nl.html").write_bytes(b2)
                info = parse(b2.decode("utf-8", "ignore"))
                e25 = info["euros"].get("2025")
                flag = "Y25" if info["year"] == "2025" or e25 else f"y{info['year']}"
                print(
                    f"  {flag} {'TAKEN' if already else 'FREE'} {dotted} "
                    f"e25={e25} fte={info['ftes']} title={info['title'][:55]}"
                )
            except Exception as e:
                print(f"  ERR {dotted} {e}")
    except Exception as e:
        print(f"SEARCH FAIL {name} {e}")
