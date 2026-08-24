# -*- coding: utf-8 -*-
import re
import ssl
import urllib.request
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
            text = re.sub(r"<[^>]+>", " ", html[idx : idx + 7000])
            return re.sub(r"\s+", " ", text)[:700]
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

    try:
        html = fetch(
            "addr_mechelen",
            "https://www.companyweb.be/en/search/address?addressQuery=2800%2bMechelen%3bStationsstraat%3b102&City=Mechelen&Country=BE&Number=102&PostalCode=2800&Street=Stationsstraat",
        )
        links = re.findall(r'href="(/en/(\d{10})/[^"]+)"', html)
        names = re.findall(r'<a[^>]+href="/en/\d{10}/[^"]+"[^>]*>([^<]{2,80})</a>', html)
        print("MECHELEN STATIONSSTRAAT 102:")
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
        print("addr ERR", e)

    print("\nCANDIDATE YEARS:")
    cands = [
        "0480566704",
        "0598966387",
        "0685516024",
        "0422620585",
        "0787300696",
        "0443249616",
        "0438687654",
        "0464822341",
        "0412210456",
        "0425123789",
        "0453380125",
        "0475123890",
        "0405406887",
        "0432829147",
        "0459770496",
        "0466266429",
        "0417958152",
        "0201712587",
    ]
    for kbo in cands:
        kbo_dot = kbo[:4] + "." + kbo[4:7] + "." + kbo[7:]
        used = kbo in used_blob or kbo_dot in used_blob
        try:
            html = fetch(f"cand_{kbo}", f"https://www.companyweb.be/en/{kbo}")
            last = re.search(r"Last balance sheet year[^0-9]*(\d{4})", html)
            title = re.search(r"<title>([^<]+)", html)
            print(
                ("USED" if used else "FREE"),
                kbo_dot,
                "last",
                last.group(1) if last else "?",
                "|",
                (title.group(1)[:70] if title else ""),
            )
            if last and last.group(1) == "2025" and not used:
                print(" ", money_block(html)[:520])
                for pat in [
                    r"filed on ([0-9-]{10})",
                    r"neergelegd op ([0-9./]{8,})",
                    r"déposées le ([0-9-]{10})",
                ]:
                    m = re.search(pat, html, re.I)
                    if m:
                        print("  filed", m.group(1))
                        break
        except Exception as e:
            print(kbo, "ERR", e)


if __name__ == "__main__":
    main()
