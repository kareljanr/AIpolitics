# -*- coding: utf-8 -*-
import re
import ssl
import urllib.request
import pathlib

ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
OUT = pathlib.Path(__file__).resolve().parent
ROOT = pathlib.Path(r"C:\Users\karel\dev\AIpolitics")


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

    url = (
        "https://www.companyweb.be/en/search/address?addressQuery="
        "2800%2bMechelen%3bStationsstraat%3b102&City=Mechelen&Country=BE"
        "&Number=102&PostalCode=2800&Street=Stationsstraat"
    )
    try:
        html = fetch("addr_mechelen2", url)
        links = re.findall(r'href="(/en/(\d{10})/[^"]+)"', html)
        names = re.findall(r'<a[^>]+href="/en/\d{10}/[^"]+"[^>]*>([^<]{2,80})</a>', html)
        print("mechelen len", len(html), "links", len(links))
        seen = set()
        for n, pair in zip(names, links):
            kbo = pair[1]
            if kbo in seen:
                continue
            seen.add(kbo)
            kbo_dot = kbo[:4] + "." + kbo[4:7] + "." + kbo[7:]
            used = kbo in used_blob or kbo_dot in used_blob
            print(("USED" if used else "FREE"), kbo_dot, n.strip()[:55])
    except Exception as e:
        print("mechelen ERR", e)

    # Remy Yves / Armonea path known KBOs + Home Sebrechts sister candidates
    cands = [
        ("0883790853", "happy_old_people"),  # fusion absorption
        ("0500937791", "armonea_at_home"),
        ("0723858144", "remy_mgmt_co"),  # bestuurder BV?
        ("0446793678", "y_remy"),
        ("0889421308", "armonea_nv"),  # already mined
        ("0432829147", "cand_0432829147"),
        ("0405406887", "cand_0405406887"),
        ("0459770496", "sint_augustinus"),  # used
        # Home Bethanie Genval - guess via common KBOs searched later
        ("0420845123", "bad"),
        ("0465123456", "bad"),
    ]

    # Also try pappers.be search pages if any
    for kbo, label in cands:
        kbo_dot = kbo[:4] + "." + kbo[4:7] + "." + kbo[7:]
        used = kbo in used_blob or kbo_dot in used_blob
        try:
            html = fetch(label, f"https://www.companyweb.be/en/{kbo}")
            last = re.search(r"Last balance sheet year[^0-9]*(\d{4})", html)
            year = last.group(1) if last else "?"
            tit = re.search(r"<title>([^<]+)", html)
            tit_s = tit.group(1)[:75] if tit else "?"
            print(("USED" if used else "FREE"), kbo_dot, "Y", year, "|", tit_s, "|", label)
            if year == "2025":
                print(" ", money_block(html)[:500])
                for pat in [r"filed on ([0-9-]{10})", r"neergelegd op ([0-9./]{8,})"]:
                    m = re.search(pat, html, re.I)
                    if m:
                        print("  filed", m.group(1))
                        break
        except Exception as e:
            print(label, kbo, "ERR", e)

    # Northdata / open pages for Remy mandates - try companyweb related companies on Armonea page
    try:
        html = fetch("armonea_page", "https://www.companyweb.be/en/0889421308/armonea")
        # look for related company links
        rels = re.findall(r'href="(/en/(\d{10})/[^"]+)"[^>]*>([^<]{2,80})', html)
        print("armonea related sample", len(rels))
        for href, kbo, name in rels[:40]:
            print(" ", kbo, name.strip()[:50])
    except Exception as e:
        print("armonea_page ERR", e)

    # Try Home Bethanie via companyweb numeric unknown - search northdata-style via google cached KBO
    # Probe common Bethanie KBOs from web: try 0432.829.147 already, try address Bois Pirart
    try:
        html = fetch(
            "bethanie_addr",
            "https://www.companyweb.be/en/search/address?addressQuery="
            "1332%2bGenval%3bRue%20Bois%20Pirart%3b127&City=Genval&Country=BE"
            "&Number=127&PostalCode=1332&Street=Rue%20Bois%20Pirart",
        )
        links = re.findall(r'href="(/en/(\d{10})/[^"]+)"', html)
        names = re.findall(r'<a[^>]+href="/en/\d{10}/[^"]+"[^>]*>([^<]{2,80})</a>', html)
        print("bethanie addr", len(html), len(links))
        for n, pair in list(dict.fromkeys(zip(names, links)))[:15]:
            print(" ", pair[1], n.strip()[:55])
    except Exception as e:
        print("bethanie addr ERR", e)

    # Wommelgheem address? unknown — try Smeedeshof again with + encoding like mechelen
    try:
        html = fetch(
            "smeede_addr",
            "https://www.companyweb.be/en/search/address?addressQuery="
            "2360%2bOud-Turnhout%3bOude%20Arendonksebaan%3b38&City=Oud-Turnhout&Country=BE"
            "&Number=38&PostalCode=2360&Street=Oude%20Arendonksebaan",
        )
        links = re.findall(r'href="(/en/(\d{10})/[^"]+)"', html)
        names = re.findall(r'<a[^>]+href="/en/\d{10}/[^"]+"[^>]*>([^<]{2,80})</a>', html)
        print("smeede addr", len(html), len(links))
        for n, pair in list(dict.fromkeys(zip(names, links)))[:15]:
            print(" ", pair[1], n.strip()[:55])
    except Exception as e:
        print("smeede ERR", e)


if __name__ == "__main__":
    main()
