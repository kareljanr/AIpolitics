# -*- coding: utf-8 -*-
"""Fetch Charmilles Sambreville CW NL/EN/FR + KBO for tick 2116."""
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
KBO = "0457649265"
SLUG = "charmilles"
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
    # NACE near activity labels
    nace_hits = re.findall(
        r"(?:NACE|Activiteit|Activity|Activité)[^0-9]{0,40}(\d{2}\.\d{3})",
        text,
        re.I,
    )
    emails = [
        e
        for e in re.findall(r"[A-Z0-9._%+\-]+@[A-Z0-9.\-]+\.[A-Z]{2,}", text, re.I)
        if "companyweb" not in e.lower() and "sentry" not in e.lower()
    ]
    addr = re.search(
        r"(?:Maatschappelijke zetel|Registered office|Siège social)\s*"
        r"(.{10,120}?\d{4}\s+[A-Za-zÀ-ÿ\- ]+)",
        text,
        re.I,
    )
    print(f"=== {lang} ===")
    print("title:", title.group(1)[:140] if title else "?")
    print("year:", lb.group(1) if lb else "?", "neer:", neer.group(1) if neer else "?")
    print("e25:", euros.get("2025"), "e24:", euros.get("2024"))
    print("fte:", ftes[:4], "nace:", nace_hits[:8], "deltas:", deltas[:12])
    print("emails:", emails[:8])
    print("addr:", addr.group(1)[:120] if addr else "?")
    # also dump a few key phrases around Korian / bestuurder
    for kw in ("Korian", "bestuurder", "director", "administrateur", "NACE", "87."):
        idx = text.lower().find(kw.lower())
        if idx >= 0:
            print(f"ctx[{kw}]:", text[max(0, idx - 40) : idx + 120])


for lang in ("nl", "en", "fr"):
    url = f"https://www.companyweb.be/{lang}/{KBO}"
    body = fetch(url)
    (RAW / f"{SLUG}_{lang}.html").write_bytes(body)
    parse(body.decode("utf-8", "ignore"), lang)

# KBO official
kbo_url = (
    "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
    f"?ondernemingsnummer={KBO}"
)
try:
    body = fetch(kbo_url)
    (RAW / f"{SLUG}_kbo.html").write_bytes(body)
    text = unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", body.decode("utf-8", "ignore"))))
    print("=== KBO ===")
    print(text[:2500])
except Exception as e:
    print("KBO ERR", e)
