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
KBO = "0452865383"
SLUG = "rusthuis-sint-jozef"
PAT = re.compile(
    r'(20\d\d)\s*:\s*\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",'
    r'\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)"'
)


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=CTX, timeout=45) as resp:
        return resp.read()


for lang in ("nl", "en", "fr"):
    url = f"https://www.companyweb.be/{lang}/{KBO}/{SLUG}"
    body = fetch(url)
    (RAW / f"ninove_{lang}.html").write_bytes(body)
    html = body.decode("utf-8", "ignore")
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
    email = re.findall(r"[\w\.-]+@(?:[\w\-]+\.)+[\w\-]+", text)
    print(
        lang,
        title.group(1)[:90] if title else "?",
        "year",
        lb.group(1) if lb else "?",
        "ftes",
        ftes[:8],
        "neer",
        neer.group(1) if neer else "?",
        "e25",
        euros.get("2025"),
        "e24",
        euros.get("2024"),
        "deltas",
        deltas[:12],
        "email",
        email[:8],
    )

for name, url in [
    (
        "kbo",
        f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={KBO}",
    ),
    (
        "kbo_nl",
        f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={KBO}&lang=nl",
    ),
    ("nbb", f"https://consult.cbso.nbb.be/consult-enterprise/{KBO}"),
]:
    body = fetch(url)
    (RAW / f"ninove_{name}.html").write_bytes(body)
    text = unescape(
        re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", body.decode("utf-8", "ignore")))
    )
    print(name, "ok", len(body), "Actief" in text or "Active" in text or "Actif" in text)
    if "kbo" in name:
        for p in [
            r"[\w\.-]+@(?:[\w\-]+\.)+[\w\-]+",
            r"Aanbestedende overheid|Pouvoir adjudicateur",
            r"vestigingseenheden \(VE\):\s*(\d+)|Nombre d.unités[^\d]*(\d+)|"
            r"Number of establishments[^\d]*(\d+)",
            r"(87\.\d{3}|86\.\d{3}|88\.\d{3}|84\.\d{3})",
            r"Vereniging zonder winstoogmerk|Association sans but lucratif|"
            r"Besloten vennootschap|Société à responsabilité limitée|VZW|ASBL|BV|SRL",
            r"(?:Adres van de zetel|Siège|Registered office).{0,160}",
            r"https?://[\w\.-]+\.be",
            r"Ninove|9400|Oude|Kaai|Jozef|Sint",
            r"Rechtsvorm sinds .{0,80}|Legal form since .{0,80}",
            r"Status van de onderneming.{0,40}|Status of the enterprise.{0,40}",
        ]:
            ms = re.findall(p, text, re.I)
            if ms:
                print(" ", p[:70], ms[:10])

# site hunt
for name, url in [
    ("site_google", "https://www.google.com/search?q=Rusthuis+Sint+Jozef+Ninove"),
    ("site_cw_contact", f"https://www.companyweb.be/nl/{KBO}"),
]:
    try:
        body = fetch(url)
        (RAW / f"{name}.html").write_bytes(body)
        text = unescape(
            re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", body.decode("utf-8", "ignore")))
        )
        emails = re.findall(r"[\w\.-]+@(?:[\w\-]+\.)+[\w\-]+", text)
        sites = re.findall(r"https?://[\w\.-]*(?:sint|jozef|ninove|wzc|rusthuis)[\w\.-]*", text, re.I)
        print(name, "emails", emails[:8], "sites", sites[:8])
    except Exception as e:
        print(name, "ERR", e)
