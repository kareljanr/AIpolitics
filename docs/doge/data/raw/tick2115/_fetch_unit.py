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
KBO = "0451031489"
SLUG = "les-sittelles"
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
    nace = re.findall(r"(87\.\d{3}|86\.\d{3})", text)
    emails = [
        e
        for e in re.findall(r"[A-Z0-9._%+\-]+@[A-Z0-9.\-]+\.[A-Z]{2,}", text, re.I)
        if "companyweb" not in e.lower() and "sentry" not in e.lower()
    ]
    rv = re.search(
        r"(BV|NV|SA|SRL|VZW|ASBL|CV|SC)",
        title.group(1) if title else "",
    )
    print(f"=== {lang} ===")
    print("title:", title.group(1)[:110] if title else None)
    print("year:", lb.group(1) if lb else None, "neer:", neer.group(1) if neer else None)
    print("euros:", {k: euros[k] for k in sorted(euros)})
    print("fte:", ftes[:4], "nace:", nace[:6], "rv:", rv.group(1) if rv else None)
    print("deltas:", deltas[:10])
    print("emails:", emails[:6])
    for pat in [
        r"(?:Maatschappelijke zetel|Registered office|Siège social)\s+(.{10,120})",
        r"(?:Adres|Address|Adresse)\s+(.{10,120})",
    ]:
        m = re.search(pat, text, re.I)
        if m:
            print("addr:", m.group(1)[:120])
            break
    # bestuurders mention
    for kw in ("Korian", "bestuurder", "Director", "Administrateur", "SL Finance"):
        if kw.lower() in text.lower():
            idx = text.lower().find(kw.lower())
            print("ctx:", text[max(0, idx - 40) : idx + 80].replace("\n", " "))


# KBO public
try:
    kbo_url = (
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
        f"?ondernemingsnummer={KBO}&lang=nl"
    )
    body = fetch(kbo_url)
    (RAW / "sittelles_kbo_nl.html").write_bytes(body)
    t = body.decode("utf-8", "ignore")
    text = unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", t)))
    print("=== KBO ===")
    for pat in [
        r"Status:\s*(\w+)",
        r"Rechtsvorm:\s*([^0-9]{5,80})",
        r"Adres van de zetel:\s*(.{10,120})",
        r"Aantal vestigingseenheden[^:]*:\s*(\d+)",
        r"E-mail:\s*(\S+)",
        r"Webadres:\s*(\S+)",
        r"Nacebel[^\d]*(\d{2}\.\d{3}[^\n]{0,80})",
        r"Aanbestedende overheid",
        r"87\.\d{3}",
    ]:
        m = re.search(pat, text, re.I)
        if m:
            print(pat, "->", m.group(0)[:120] if m.lastindex is None else m.group(1)[:120])
    # print NACE hits
    print("nace hits:", re.findall(r"87\.\d{3}[^\n]{0,60}", text)[:6])
    print("email hits:", re.findall(r"[A-Z0-9._%+\-]+@[A-Z0-9.\-]+\.[A-Z]{2,}", text, re.I)[:6])
except Exception as e:
    print("KBO ERR", e)

for lang in ("nl", "en", "fr"):
    url = f"https://www.companyweb.be/{lang}/{KBO}/{SLUG}"
    body = fetch(url)
    (RAW / f"sittelles_{lang}.html").write_bytes(body)
    parse(body.decode("utf-8", "ignore"), lang)
