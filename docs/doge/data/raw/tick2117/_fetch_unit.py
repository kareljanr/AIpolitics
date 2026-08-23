# -*- coding: utf-8 -*-
"""Fetch La Charmille Pont-à-Celles CW NL/EN/FR + KBO for tick 2117."""
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
PAT = re.compile(
    r'(20\d\d)\s*:\s*\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",'
    r'\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)"'
)
KBO = "0416116637"


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=CTX, timeout=45) as resp:
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
    deltas = re.findall(
        r"(Omzet|Turnover|Chiffre d.affaires|Brutomarge|Gross margin|"
        r"Marge brute|Winst/Verlies|Profit/Loss|Bénéfice/Perte|"
        r"Eigen vermogen|Equity|Capitaux propres|"
        r"Werknemers|Employees|Employés)"
        r"[^%]{0,80}?([+\-−]?\s*[\d\.,]+\s*%)",
        text,
        re.I,
    )
    emails = [
        e
        for e in re.findall(r"[A-Z0-9._%+\-]+@[A-Z0-9.\-]+\.[A-Z]{2,}", text, re.I)
        if "companyweb" not in e.lower() and "sentry" not in e.lower()
    ]
    form = re.search(
        r"(VZW|ASBL|NV|SA|BV|SRL|CV|SC|vereniging zonder winstoogmerk|"
        r"association sans but lucratif)",
        text,
        re.I,
    )
    return {
        "title": title.group(1)[:140] if title else "?",
        "year": lb.group(1) if lb else "?",
        "neer": neer.group(1) if neer else "?",
        "euros": euros,
        "ftes": ftes[:6],
        "deltas": deltas[:12],
        "emails": emails[:8],
        "form": form.group(1) if form else "?",
    }


for lang in ("nl", "en", "fr"):
    url = f"https://www.companyweb.be/{lang}/{KBO}"
    body = fetch(url)
    (RAW / f"la_charmille_{lang}.html").write_bytes(body)
    info = parse(body.decode("utf-8", "ignore"))
    print(f"==== {lang}")
    print(info)

# KBO
kbo_url = (
    "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?"
    f"ondernemingsnummer={KBO}&lang=nl"
)
kbo_body = fetch(kbo_url)
(RAW / "la_charmille_kbo.html").write_bytes(kbo_body)
kbo_text = unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", kbo_body.decode("utf-8", "ignore"))))
print("==== KBO snip")
for key in ("Actief", "Normale", "La Charmille", "87.301", "Pont", "VZW", "aanbestedende", "Aanbestedende"):
    if key.lower() in kbo_text.lower():
        print("HIT", key)
print(kbo_text[kbo_text.find("Ondernemingsnummer") : kbo_text.find("Ondernemingsnummer") + 700])
