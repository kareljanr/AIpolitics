# -*- coding: utf-8 -*-
import re
import ssl
import urllib.request
import pathlib
import urllib.parse

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
            text = re.sub(r"<[^>]+>", " ", html[idx : idx + 8000])
            return re.sub(r"\s+", " ", text)[:900]
    return ""


def summarize(label, html):
    last = re.search(r"Last balance sheet year[^0-9]*(\d{4})", html) or re.search(
        r"Laatste balansi?aar[^0-9]*(\d{4})", html
    )
    title = re.search(r"<title>([^<]+)", html)
    print(label, "last", last.group(1) if last else "?", "|", (title.group(1)[:80] if title else ""))
    print(" ", money_block(html)[:650])
    for pat in [r"filed on ([0-9-]{10})", r"neergelegd op ([0-9./]{8,})", r"déposées le ([0-9-]{10})"]:
        m = re.search(pat, html, re.I)
        if m:
            print("  filed", m.group(1))
            break
    # FTE / size
    for pat in [
        r"Average number of employees[^0-9]*([\d.,]+)",
        r"Gemiddeld aantal werknemers[^0-9]*([\d.,]+)",
        r"FTE[^0-9]*([\d.,]+)",
        r"Personnel[^0-9]*([\d.,]+)",
    ]:
        m = re.search(pat, html, re.I)
        if m:
            print("  fte-ish", m.group(1))
            break


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

    # Melis deep dive NL/EN/FR + KBO
    for label, url in [
        ("melis_en", "https://www.companyweb.be/en/0787300696"),
        ("melis_nl", "https://www.companyweb.be/nl/0787300696"),
        ("melis_fr", "https://www.companyweb.be/fr/0787300696"),
        ("melis_kbo", "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0787300696"),
    ]:
        try:
            html = fetch(label, url)
            summarize(label, html)
            print("---")
        except Exception as e:
            print(label, "ERR", e)

    # Find more unused YE2025 MRS via KBO phonetic / known lists
    # Probe more candidate KBOs often deferred in prior ticks
    more = [
        ("0420845678", "guess1"),  # invalid likely
        ("0400228858", "korian_be?"),
        ("0471678155", "cand"),
        ("0460123456", "bad"),
        ("0436123456", "bad"),
        ("0865123456", "bad"),
        # From tick2118/2108 candidate lists if any exist in prior raw
    ]

    # Scan prior cand html lists for KBO numbers with YE2025 unused
    prior_dirs = [
        ROOT / "docs/doge/data/raw/tick2125",
        ROOT / "docs/doge/data/raw/tick2118",
        ROOT / "docs/doge/data/raw/tick2108",
    ]
    kbos = set()
    for d in prior_dirs:
        if not d.exists():
            continue
        for p in d.glob("cand_*.html"):
            m = re.search(r"cand_(\d{10})", p.name)
            if m:
                kbos.add(m.group(1))
        for p in d.glob("*.html"):
            t = p.read_text(encoding="utf-8", errors="ignore")[:2000]
            for m in re.findall(r"BE(\d{10})", t):
                kbos.add(m)
            for m in re.findall(r"/en/(\d{10})", t):
                kbos.add(m)

    print("\nSCAN PRIOR CANDS FOR FREE YE2025:")
    interesting = []
    for kbo in sorted(kbos):
        kbo_dot = kbo[:4] + "." + kbo[4:7] + "." + kbo[7:]
        if kbo in used_blob or kbo_dot in used_blob:
            continue
        # skip already known stalls
        if kbo in ("0201712587", "0644638937", "0893863017", "0787300696"):
            continue
        try:
            html = fetch(f"scan_{kbo}", f"https://www.companyweb.be/en/{kbo}")
            last = re.search(r"Last balance sheet year[^0-9]*(\d{4})", html)
            title = re.search(r"<title>([^<]+)", html)
            year = last.group(1) if last else "?"
            tit = title.group(1)[:70] if title else ""
            if year == "2025":
                block = money_block(html)
                # prefer material turnover/gross
                interesting.append((kbo_dot, tit, block[:400]))
                print("FREE YE2025", kbo_dot, "|", tit)
                print(" ", block[:400])
        except Exception as e:
            pass

    print("\nINTERESTING COUNT", len(interesting))


if __name__ == "__main__":
    main()
