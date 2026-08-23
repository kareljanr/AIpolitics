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
    "Accept-Language": "nl-BE,nl;q=0.9,fr;q=0.8,en;q=0.7",
}
KBO = "0466961859"
SLUG = "residence-les-buissons"
PAT = re.compile(
    r'(20\d\d)\s*:\s*\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",'
    r'\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)"'
)


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=CTX, timeout=45) as resp:
        return resp.read()


def parse(html: str, lang: str):
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
    deltas = re.findall(
        r"(Omzet|Turnover|Chiffre d.affaires|Brutomarge|Gross margin|"
        r"Marge brute|Winst/Verlies|Profit/Loss|Bénéfice/Perte|"
        r"Eigen vermogen|Equity|Capitaux propres|"
        r"Werknemers|Employees|Employés)"
        r"[^%]{0,80}?([+\-−]?\s*[\d\.,]+\s*%)",
        text,
        re.I,
    )
    # NACE
    nace = re.findall(r"(87\.\d{3})", text)
    # email
    emails = re.findall(
        r"[A-Z0-9._%+\-]+@[A-Z0-9.\-]+\.[A-Z]{2,}", text, re.I
    )
    emails = [e for e in emails if "companyweb" not in e.lower() and "example" not in e.lower()]
    # rechtsvorm
    rv = re.search(
        r"(BV|NV|SA|SRL|VZW|ASBL|CV|SC|CVBA|Comm\.?V)",
        title.group(1) if title else "",
    )
    print(f"=== {lang} ===")
    print("title:", title.group(1)[:110] if title else None)
    print("year:", lb.group(1) if lb else None, "neer:", neer.group(1) if neer else None)
    print("euros:", {k: euros[k] for k in sorted(euros)})
    print("fte:", ftes[:4], "nace:", nace[:6], "rv:", rv.group(1) if rv else None)
    print("deltas:", deltas[:10])
    print("emails:", emails[:6])
    # address block
    for pat in [
        r"(?:Maatschappelijke zetel|Registered office|Siège social)\s+(.{10,100})",
        r"(?:Adres|Address|Adresse)\s+(.{10,100})",
    ]:
        m = re.search(pat, text, re.I)
        if m:
            print("addr:", m.group(1)[:100])
            break
    return euros


# also check De Foyer quickly
print("=== quick De Foyer check ===")
try:
    body = fetch("https://www.companyweb.be/nl/0413796456")
    (RAW / "de_foyer_nl.html").write_bytes(body)
    t = body.decode("utf-8", "ignore")
    text = unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", t)))
    lb = re.search(r"Laatste balansjaar\s+(\d{4})", text)
    title = re.search(r"<title>([^<]+)", t)
    print("De Foyer", title.group(1)[:80] if title else "?", "y=", lb.group(1) if lb else "?")
except Exception as e:
    print("De Foyer ERR", e)

for lang in ("nl", "en", "fr"):
    url = f"https://www.companyweb.be/{lang}/{KBO}/{SLUG}"
    body = fetch(url)
    (RAW / f"buissons_{lang}.html").write_bytes(body)
    parse(body.decode("utf-8", "ignore"), lang)

# KBO public search
kbo_url = (
    "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?"
    f"ondernemingsnummer={KBO}&lang=nl"
)
try:
    body = fetch(kbo_url)
    (RAW / "buissons_kbo_nl.html").write_bytes(body)
    text = unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", body.decode("utf-8", "ignore"))))
    print("=== KBO ===")
    print(text[:1500])
except Exception as e:
    print("KBO ERR", e)
