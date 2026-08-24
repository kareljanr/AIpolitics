# -*- coding: utf-8 -*-
import re
import ssl
import urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
OUT = Path(__file__).resolve().parent
KBO = "0865574649"


def fetch(label, url):
    req = urllib.request.Request(url, headers=UA)
    html = urllib.request.urlopen(req, timeout=45, context=ctx).read().decode("utf-8", "replace")
    (OUT / f"{label}.html").write_text(html, encoding="utf-8")
    return html


def extract(html, lab):
    idx = html.find(lab)
    if idx < 0:
        return None
    chunk = re.sub(r"<[^>]+>", "|", html[idx : idx + 2000])
    amounts = re.findall(r"€\s*\|\s*\|\s*([-\d,]+)", chunk)
    pcts = re.findall(r"\|\s*((?:&lt;\s*)?-?\d[\d.,]*%|&lt;\s*-1000%)", chunk)
    # also personnel row may not have euro
    if lab in ("Employees", "Personnel", "Personeel"):
        nums = re.findall(r"\|\s*\|\s*([\d]+(?:[.,]\d+)?)\s*\|", chunk)
        return {"nums": nums[:4], "chunk": re.sub(r"\s+", " ", chunk)[:300]}
    return {"amounts": amounts[:4], "pcts": pcts[:3], "chunk": re.sub(r"\s+", " ", chunk)[:300]}


def main():
    pages = {
        "fakkel_en": f"https://www.companyweb.be/en/{KBO}/zorghome-de-fakkel",
        "fakkel_nl": f"https://www.companyweb.be/nl/{KBO}/zorghome-de-fakkel",
        "fakkel_fr": f"https://www.companyweb.be/fr/{KBO}/zorghome-de-fakkel",
        "fakkel_kbo": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={KBO}",
    }
    for label, url in pages.items():
        try:
            html = fetch(label, url)
            print("OK", label, len(html))
        except Exception as e:
            # try without slug
            try:
                html = fetch(label, url.rsplit("/", 1)[0] if "zorghome" in url else url)
                print("OK fallback", label, len(html))
            except Exception as e2:
                print(label, e, e2)
                continue

    html = (OUT / "fakkel_en.html").read_text(encoding="utf-8", errors="ignore")
    for lab in [
        "Turnover",
        "Gross margin",
        "Profit/Loss",
        "Equity",
        "Employees",
        "Personnel",
    ]:
        print(lab, extract(html, lab))
    for pat in [r"filed on ([0-9-]{10})", r"([0-9]+(?:[.,]\d+)?)\s*FTE", r"Last balance sheet year[^0-9]*(\d{4})"]:
        print(pat, re.findall(pat, html)[:3])

    # prior year FTE from Employees row
    idx = html.find("Employees")
    if idx < 0:
        idx = html.find("Personnel")
    if idx > 0:
        chunk = re.sub(r"<[^>]+>", " ", html[idx : idx + 2500])
        print("EMP CHUNK", re.sub(r"\s+", " ", chunk)[:500])

    # Gross margin prior
    idx = html.find("Gross margin")
    chunk = re.sub(r"<[^>]+>", "|", html[idx : idx + 2500])
    print("GROSS amounts", re.findall(r"€\s*\|\s*\|\s*([-\d,]+)", chunk)[:5])
    print("GROSS pcts", re.findall(r"\|\s*((?:&lt;\s*)?-?\d[\d.,]*%|&lt;\s*-1000%)", chunk)[:4])

    # Equity prior
    idx = html.find('Equity of the financial year') if 'Equity of' in html else html.find(">Equity<")
    if idx < 0:
        idx = html.find("Equity")
    # find the financial table Equity row more carefully - look after Table Graph
    idx = html.find("Table Graph")
    text = re.sub(r"<[^>]+>", " ", html[idx : idx + 8000]) if idx > 0 else ""
    print("TABLE", re.sub(r"\s+", " ", text)[:1200])

    kbo = (OUT / "fakkel_kbo.html").read_text(encoding="utf-8", errors="ignore")
    text = re.sub(r"<[^>]+>", " ", kbo)
    text = re.sub(r"\s+", " ", text)
    for needle in [
        "Rechtsvorm",
        "Status",
        "Adres",
        "Nace",
        "vestigingseenheden",
        "Bestuur",
        "Kapitaal",
        "E-mail",
        "Webadres",
        "Armonea",
        "Fakkel",
    ]:
        i = text.lower().find(needle.lower())
        if i >= 0:
            print(text[i : i + 240])


if __name__ == "__main__":
    main()
