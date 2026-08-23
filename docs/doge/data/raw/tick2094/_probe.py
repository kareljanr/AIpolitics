# -*- coding: utf-8 -*-
"""Probe prefer-path + Sint-Lucia for tick 2094."""
import re
import ssl
import urllib.request
from pathlib import Path

OUT = Path(__file__).resolve().parent
UA = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "nl-BE,nl;q=0.9,en;q=0.8",
}
CTX = ssl.create_default_context()

TARGETS = [
    ("agb_bornem_site", "https://www.bornem.be/bestuur/jaarrekening"),
    ("agb_bornem_jr", "https://www.bornem.be/bestuur-en-beleid/jaarrekening-gemeente-ocmw-en-agb"),
    ("faro_nl", "https://www.companyweb.be/nl/0893863017/faro-vlaams-steunpunt-voor-cultureel-erfgoed"),
    ("aiesh_nl", "https://www.companyweb.be/nl/0201712587/a-i-e-s-h"),
    ("rew_nl", "https://www.companyweb.be/nl/0644638937/rew"),
    ("lucia_nl", "https://www.companyweb.be/nl/0410151137/sint-lucia"),
    ("lucia_en", "https://www.companyweb.be/en/0410151137/sint-lucia"),
    ("lucia_fr", "https://www.companyweb.be/fr/0410151137/sint-lucia"),
    ("lucia_kbo", "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0410151137"),
]


def fetch(name, url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=CTX, timeout=60) as r:
        data = r.read()
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        text = data.decode("latin-1", errors="replace")
    path = OUT / f"{name}.html"
    path.write_text(text, encoding="utf-8")
    return text


def summarize_cw(name, html):
    title = re.search(r"<title[^>]*>(.*?)</title>", html, re.I | re.S)
    title_s = re.sub(r"\s+", " ", title.group(1)).strip() if title else "?"
    # boekjaar / latest filing year patterns used on CW
    boek = re.findall(r"Boekjaar[^0-9]{0,30}(202[0-9])", html, re.I)
    neer = re.findall(r"Neergelegd[^0-9]{0,40}([0-9]{2}[./-][0-9]{2}[./-][0-9]{4})", html, re.I)
    years_near = re.findall(
        r"(?:jaar|year|boekjaar|periode|exercise)[^0-9]{0,25}(202[3-6])", html, re.I
    )
    # KPI cards often have aria or nearby year
    metrics = {}
    for label in [
        "Omzet",
        "Turnover",
        "Chiffre d'affaires",
        "Brutomarge",
        "Gross margin",
        "Marge brute",
        "Winst/Verlies",
        "Profit/Loss",
        "Bénéfice/Perte",
        "Eigen vermogen",
        "Equity",
        "Capitaux propres",
        "Personeelsbestand",
        "Workforce",
        "Effectif",
    ]:
        # find label then next euro-like number within 400 chars
        for m in re.finditer(re.escape(label), html, re.I):
            window = html[m.end() : m.end() + 500]
            num = re.search(
                r"(?:€|EUR|&euro;)?\s*([+-]?\s*[0-9]{1,3}(?:[.\s][0-9]{3})*(?:,[0-9]+)?|[+-]?\s*[0-9]+(?:,[0-9]+)?)",
                window,
            )
            if num:
                metrics[label] = re.sub(r"\s+", "", num.group(1))
                break
    # trend badges JUMP/DROP often near year
    trends = re.findall(r"(JUMP|DROP|FLIP|N/A|n\.v\.t\.)", html)
    print(f"=== {name}")
    print(" title:", title_s[:140])
    print(" boekjaar hits:", boek[:8])
    print(" neergelegd:", neer[:6])
    print(" year ctx:", sorted(set(years_near))[:10])
    print(" metrics:", metrics)
    print(" trends sample:", trends[:12], "count", len(trends))
    # explicit latest year from CW schema.org or JSON
    for m in re.finditer(r'"fiscalYear"\s*:\s*"?(202[0-9])', html):
        print(" fiscalYear", m.group(1))
    for m in re.finditer(r'data-year="(202[0-9])"', html):
        print(" data-year", m.group(1))
    # look for 'Laatste jaarrekening' block
    for m in re.finditer(r"Laatste jaarrekening.{0,200}", html, re.I | re.S):
        s = re.sub(r"<[^>]+>", " ", m.group(0))
        s = re.sub(r"\s+", " ", s).strip()
        print(" laatste:", s[:180])
        break


def summarize_bornem(html):
    print("=== bornem")
    links = []
    for m in re.finditer(r'href="([^"]+)"[^>]*>([^<]{0,120})', html, re.I):
        href, txt = m.group(1), m.group(2)
        blob = (href + " " + txt).lower()
        if any(k in blob for k in ["jaarrekening", "agb", "2025", "2024", "pdf"]):
            links.append((re.sub(r"\s+", " ", txt).strip()[:80], href[:160]))
    for t, h in links[:25]:
        print(" ", t, "->", h)


def main():
    for name, url in TARGETS:
        try:
            html = fetch(name, url)
            print(f"FETCH OK {name} {len(html)} {url}")
            if "bornem" in name:
                summarize_bornem(html)
            elif "kbo" in name:
                print("=== kbo lucia")
                for pat in [
                    r"Actief|Stopzetting|Rechtstoestand",
                    r"VZW|NV|CV",
                    r"NACE[^<]{0,80}",
                    r"email|@|Tel",
                    r"Turnhout|Lucia",
                ]:
                    ms = re.findall(pat, html, re.I)
                    if ms:
                        print(" ", pat[:30], ms[:5])
            else:
                summarize_cw(name, html)
        except Exception as e:
            print(f"FETCH FAIL {name}: {e}")
        print()


if __name__ == "__main__":
    main()
