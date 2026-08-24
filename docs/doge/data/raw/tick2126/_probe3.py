# -*- coding: utf-8 -*-
import re
import ssl
import urllib.request
import pathlib
import csv

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
            return re.sub(r"\s+", " ", text)[:1000]
    return ""


def parse_table_metrics(html):
    """Extract year-row metrics from Companyweb EN financial table heuristically."""
    # Prefer EN labels
    out = {}
    # Look for Turnover row with euro amounts
    patterns = {
        "turnover": r"Turnover[^€]*€\s*([-\d,]+)\s*([-\d.,%]*)\s*€\s*([-\d,]+)",
        "gross": r"Gross margin[^€]*€\s*([-\d,]+)\s*([-\d.,%]*)\s*€\s*([-\d,]+)",
        "pnl": r"Profit/Loss[^€]*€\s*([-\d,]+)\s*([-\d.,%]*)\s*€\s*([-\d,]+)",
        "equity": r"Equity[^€]*€\s*([-\d,]+)\s*([-\d.,%]*)\s*€\s*([-\d,]+)",
    }
    text = money_block(html)
    for k, pat in patterns.items():
        m = re.search(pat, text, re.I)
        if m:
            out[k] = (m.group(1), m.group(2), m.group(3))
    # FTE often in workforce section
    m = re.search(r"(?:Average number of employees|Workforce)[^0-9]{0,40}([\d]+(?:[.,]\d+)?)", html, re.I)
    if m:
        out["fte"] = m.group(1)
    # also try Personnel costs context
    m2 = re.search(r">([\d]+(?:[.,]\d+)?)\s*</[^>]*>\s*(?:FTE|VTE|werknemers)", html, re.I)
    if m2:
        out["fte2"] = m2.group(1)
    return out, text


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

    # Melis detail
    html = (OUT / "melis_en.html").read_text(encoding="utf-8", errors="ignore")
    metrics, text = parse_table_metrics(html)
    print("MELIS METRICS", metrics)
    print("MELIS TEXT", text[:800])

    # Extract establishment / NACE / VE from KBO
    kbo_html = (OUT / "melis_kbo.html").read_text(encoding="utf-8", errors="ignore")
    print("KBO snippet:")
    textk = re.sub(r"<[^>]+>", " ", kbo_html)
    textk = re.sub(r"\s+", " ", textk)
    for needle in ["Rechtsvorm", "Status", "Adres", "Nace", "Vestiging", "Bestuur", "Melis"]:
        idx = textk.lower().find(needle.lower())
        if idx >= 0:
            print(textk[idx : idx + 200])

    # Broader candidate hunt: Armonea related KBOs from pappers / companyweb search
    searches = [
        ("search_armonea_mrs", "https://www.companyweb.be/en/search?query=armonea"),
        ("search_woonzorg", "https://www.companyweb.be/en/search?query=woonzorgcentrum"),
        ("search_maison_repos", "https://www.companyweb.be/en/search?query=maison+de+repos"),
        ("search_residence_senior", "https://www.companyweb.be/en/search?query=residence+senior"),
        # Jolimont unused homes
        ("search_buissonnets", "https://www.companyweb.be/en/search?query=les+buissonnets"),
        ("search_chartriers", "https://www.companyweb.be/en/search?query=les+chartriers"),
        ("search_visitation", "https://www.companyweb.be/en/search?query=la+visitation+lobbes"),
        ("search_longtain", "https://www.companyweb.be/en/search?query=seniorie+longtain"),
        ("search_fontaine", "https://www.companyweb.be/en/search?query=notre-dame+de+la+fontaine"),
        ("search_comme_chez", "https://www.companyweb.be/en/search?query=comme+chez+soi+ecaussinnes"),
    ]
    found_kbos = []
    for label, url in searches:
        try:
            h = fetch(label, url)
            links = re.findall(r'href="(/en/(\d{10})/[^"]*)"', h)
            names = re.findall(r'<a[^>]+href="/en/\d{10}/[^"]*"[^>]*>([^<]{2,90})</a>', h)
            print(label, "hits", len(links))
            seen = set()
            for n, pair in zip(names, links):
                kbo = pair[1]
                if kbo in seen:
                    continue
                seen.add(kbo)
                print(" ", kbo, n.strip()[:60])
                found_kbos.append((kbo, n.strip()))
        except Exception as e:
            print(label, "ERR", e)

    print("\nCHECKING FOUND FOR FREE YE2025:")
    for kbo, name in found_kbos[:40]:
        kbo_dot = kbo[:4] + "." + kbo[4:7] + "." + kbo[7:]
        if kbo in used_blob or kbo_dot in used_blob:
            print("USED", kbo_dot, name[:40])
            continue
        try:
            h = fetch(f"hit_{kbo}", f"https://www.companyweb.be/en/{kbo}")
            last = re.search(r"Last balance sheet year[^0-9]*(\d{4})", h)
            year = last.group(1) if last else "?"
            title = re.search(r"<title>([^<]+)", h)
            tit = title.group(1)[:70] if title else name
            if year == "2025":
                metrics, text = parse_table_metrics(h)
                print("FREE YE2025", kbo_dot, "|", tit)
                print(" ", metrics)
                print(" ", text[:350])
            else:
                print("skip", kbo_dot, "year", year, tit[:40])
        except Exception as e:
            print(kbo, "ERR", e)


if __name__ == "__main__":
    main()
