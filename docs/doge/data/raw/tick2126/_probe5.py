# -*- coding: utf-8 -*-
import re
import ssl
import urllib.request
import urllib.parse
import pathlib

ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
ROOT = pathlib.Path(r"C:\Users\karel\dev\AIpolitics")
OUT = pathlib.Path(__file__).resolve().parent


def fetch(label, url, data=None):
    if data is not None:
        req = urllib.request.Request(url, data=data, headers={**UA, "Content-Type": "application/x-www-form-urlencoded"})
    else:
        req = urllib.request.Request(url, headers=UA)
    html = urllib.request.urlopen(req, timeout=45, context=ctx).read().decode("utf-8", "replace")
    (OUT / f"{label}.html").write_text(html, encoding="utf-8")
    return html


def money_block(html):
    for key in ["Financial data", "Financiële gegevens", "Données financières"]:
        idx = html.find(key)
        if idx > 0:
            text = re.sub(r"<[^>]+>", " ", html[idx : idx + 9000])
            return re.sub(r"\s+", " ", text)[:900]
    return ""


def kbo_name_search(name):
    # POST phonetic search
    payload = urllib.parse.urlencode(
        {
            "searchWord": name,
            "_ou": "",
            "filterEnkelActieve": "true",
            "actionLucene": "Zoeken",
        }
    ).encode()
    # try several endpoints
    for endpoint in [
        "https://kbopub.economie.fgov.be/kbopub/zoeknaamfonetisch.html",
        "https://kbopub.economie.fgov.be/kbopub/zoeknaamfonetischform.html",
        "https://kbopub.economie.fgov.be/kbopub/zoeknaamexact.html",
    ]:
        try:
            html = fetch(f"kbo_{re.sub(r'[^A-Za-z0-9]+','_',name)[:20]}", endpoint, data=payload)
            nums = re.findall(r"ondernemingsnummer=(\d+)", html)
            titles = re.findall(
                r"toonondernemingps\.html\?ondernemingsnummer=\d+[^\"]*\"[^>]*>([^<]+)", html
            )
            if nums:
                return nums, titles, endpoint
        except Exception as e:
            last = e
            continue
    raise last


def main():
    used_blob = ""
    for rel in [
        "docs/doge/data/entities.csv",
        "docs/doge/data/leaderboard.csv",
        "docs/doge/data/research_queue.csv",
        "docs/doge/data/budgets.csv",
    ]:
        p = ROOT / rel
        if p.exists():
            used_blob += p.read_text(encoding="utf-8", errors="ignore").lower()

    # Address searches on KBO and Companyweb
    addr_tests = [
        (
            "addr_tchaurnia",
            "https://kbopub.economie.fgov.be/kbopub/zoekadres.html?"
            + urllib.parse.urlencode(
                {
                    "postcode": "5560",
                    "straat": "Tchaurnia",
                    "huisnummer": "32",
                    "filterEnkelActieve": "true",
                }
            ),
        ),
        (
            "cw_addr_tchaurnia",
            "https://www.companyweb.be/en/search/address?addressQuery="
            + urllib.parse.quote("5560 Houyet;Rue du Tchaurnia;32")
            + "&City=Houyet&Country=BE&Number=32&PostalCode=5560&Street=Rue%20du%20Tchaurnia",
        ),
        (
            "cw_addr_smeedeshof",
            "https://www.companyweb.be/en/search/address?addressQuery="
            + urllib.parse.quote("2360 Oud-Turnhout;Oude Arendonksebaan;38")
            + "&City=Oud-Turnhout&Country=BE&Number=38&PostalCode=2360&Street=Oude%20Arendonksebaan",
        ),
        (
            "cw_addr_klinckaert",
            "https://www.companyweb.be/en/search/address?addressQuery="
            + urllib.parse.quote("3150 Haacht;Rijmenamsesteenweg;71")
            + "&City=Haacht&Country=BE&Number=71&PostalCode=3150&Street=Rijmenamsesteenweg",
        ),
        (
            "cw_addr_notelaar",
            "https://www.companyweb.be/en/search/address?addressQuery="
            + urllib.parse.quote("2250 Olen;Notelaar;1a")
            + "&City=Olen&Country=BE&Number=1a&PostalCode=2250&Street=Notelaar",
        ),
        (
            "cw_addr_hovenier",
            "https://www.companyweb.be/en/search/address?addressQuery="
            + urllib.parse.quote("8800 Roeselare;Hoveniersstraat;15")
            + "&City=Roeselare&Country=BE&Number=15&PostalCode=8800&Street=Hoveniersstraat",
        ),
        (
            "cw_addr_dageraad",
            "https://www.companyweb.be/en/search/address?addressQuery="
            + urllib.parse.quote("2018 Antwerpen;Wipstraat;24")
            + "&City=Antwerpen&Country=BE&Number=24&PostalCode=2018&Street=Wipstraat",
        ),
        (
            "cw_addr_ham",
            "https://www.companyweb.be/en/search/address?addressQuery="
            + urllib.parse.quote("6120 Ham-sur-Heure;Allee des Ecureuils;60")
            + "&City=Ham-sur-Heure&Country=BE&Number=60&PostalCode=6120&Street=Allee%20des%20Ecureuils",
        ),
    ]

    found_kbos = []
    for label, url in addr_tests:
        try:
            html = fetch(label, url)
            nums = re.findall(r"(?:ondernemingsnummer=|/en/)(\d{9,10})", html)
            names = re.findall(r'<a[^>]+href="[^"]*(?:ondernemingsnummer=\d+|/en/\d{10}/)[^"]*"[^>]*>([^<]{2,80})</a>', html)
            print(label, "len", len(html), "nums", nums[:10], "names", [n.strip()[:40] for n in names[:8]])
            for n in nums:
                found_kbos.append(n.zfill(10))
        except Exception as e:
            print(label, "ERR", e)

    # POST name searches
    for name in [
        "Charmes en Famenne",
        "PHI-BIS",
        "Happy Old People",
        "Klein Veldekens",
        "Wommelgheem",
        "Smeedeshof",
        "De Klinckaert",
        "De Notelaar",
        "De Hovenier",
        "Dageraad",
        "Home Bethanie",
        "Les Buissonnets",
        "Les Chartriers",
        "La Visitation",
        "Zorghome De Fakkel",
        "Residentie Moretus",
    ]:
        try:
            nums, titles, ep = kbo_name_search(name)
            print("NAME", name, "via", ep[-30:], "nums", nums[:5], [t.strip()[:35] for t in titles[:5]])
            for n in nums[:5]:
                found_kbos.append(n.zfill(10))
        except Exception as e:
            print("NAME", name, "ERR", e)

    print("\nYE CHECK:")
    seen = set()
    for kbo in found_kbos:
        if kbo in seen:
            continue
        seen.add(kbo)
        kbo_dot = kbo[:4] + "." + kbo[4:7] + "." + kbo[7:]
        used = kbo in used_blob or kbo_dot in used_blob
        try:
            html = fetch(f"ye_{kbo}", f"https://www.companyweb.be/en/{kbo}")
            last = re.search(r"Last balance sheet year[^0-9]*(\d{4})", html)
            year = last.group(1) if last else "?"
            tit = re.search(r"<title>([^<]+)", html)
            tit_s = tit.group(1)[:75] if tit else "?"
            print(("USED" if used else "FREE"), kbo_dot, "Y", year, "|", tit_s)
            if year == "2025" and not used:
                print(" ", money_block(html)[:520])
                for pat in [r"filed on ([0-9-]{10})", r"neergelegd op ([0-9./]{8,})"]:
                    m = re.search(pat, html, re.I)
                    if m:
                        print("  filed", m.group(1))
                        break
        except Exception as e:
            print(kbo, "ERR", e)


if __name__ == "__main__":
    main()
