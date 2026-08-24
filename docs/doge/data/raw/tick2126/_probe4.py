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


def fetch(label, url):
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

    # KBO phonetic name search for Armonea-related / unused MRS
    names = [
        "PHI-BIS",
        "Happy Old People",
        "Zorghome De Fakkel",
        "Residentie Moretus",
        "Armonea Home",
        "La Salette",
        "Soprim",
        "Klein Veldekens",
        "Wommelgheem",
        "Smeedeshof",
        "Charmes en Famenne",
        "De Klinckaert",
        "De Notelaar",
        "De Hovenier",
        "Dageraad Antwerpen",
        "Home Bethanie",
        "Home Van Dievoet",
        "Les Buissonnets",
        "Les Chartriers",
        "La Visitation",
        "Seniorie de Longtain",
        "Comme Chez Soi",
        "Hof Ter Lande",
        "De Hoeksteen Diksmuide",
        "Rusthuis Stil Geluk",
        "Sint Vincentius Erpe",
        "Helianthus Melle",
    ]
    found = []
    for name in names:
        q = urllib.parse.quote(name)
        url = (
            "https://kbopub.economie.fgov.be/kbopub/zoeknaamfonetisch.html?"
            f"searchWord={q}&_ou=&filterEnkelActieve=true"
        )
        try:
            html = fetch(f"kbo_{re.sub(r'[^A-Za-z0-9]+','_',name)[:24]}", url)
            # extract enterprise numbers and names
            rows = re.findall(
                r"ondernemingsnummer=(\d+)[^>]*>.*?,</a>\s*<br\s*/?>\s*([^<]{2,80})",
                html,
                re.I | re.S,
            )
            # alternate pattern
            nums = re.findall(r"ondernemingsnummer=(\d+)", html)
            titles = re.findall(r"toonondernemingps\.html\?ondernemingsnummer=\d+[^\"]*\"[^>]*>([^<]+)", html)
            print("KBO", name, "nums", nums[:6], "titles", [t.strip()[:40] for t in titles[:6]])
            for n, t in zip(nums, titles):
                found.append((n.zfill(10), t.strip(), name))
        except Exception as e:
            print("KBO", name, "ERR", e)

    # Also try companyweb direct slug guesses
    slugs = [
        "phi-bis",
        "happy-old-people",
        "zorghome-de-fakkel",
        "residentie-moretus",
        "la-salette",
        "soprim",
        "klein-veldekens",
        "wommelgheem",
        "smeedeshof",
        "charmes-en-famenne",
        "de-klinckaert",
        "de-notelaar",
        "de-hovenier",
        "home-bethanie",
        "home-van-dievoet",
        "les-buissonnets",
        "les-chartriers",
        "la-visitation",
    ]

    print("\nCHECK FOUND KBOS:")
    seen = set()
    for kbo, title, src in found:
        if kbo in seen:
            continue
        seen.add(kbo)
        kbo_dot = kbo[:4] + "." + kbo[4:7] + "." + kbo[7:]
        used = kbo in used_blob or kbo_dot in used_blob
        try:
            html = fetch(f"ent_{kbo}", f"https://www.companyweb.be/en/{kbo}")
            last = re.search(r"Last balance sheet year[^0-9]*(\d{4})", html)
            year = last.group(1) if last else "?"
            tit = re.search(r"<title>([^<]+)", html)
            tit_s = tit.group(1)[:75] if tit else title
            flag = "USED" if used else "FREE"
            print(flag, kbo_dot, "Y", year, "|", tit_s, "| src", src)
            if year == "2025" and not used:
                print(" ", money_block(html)[:500])
                for pat in [r"filed on ([0-9-]{10})", r"neergelegd op ([0-9./]{8,})"]:
                    m = re.search(pat, html, re.I)
                    if m:
                        print("  filed", m.group(1))
                        break
        except Exception as e:
            print(kbo, title, "ERR", e)


if __name__ == "__main__":
    main()
