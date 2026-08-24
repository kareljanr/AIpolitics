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
    idx = html.find("Table Graph")
    if idx < 0:
        idx = html.find("Financial data from")
    if idx > 0:
        text = re.sub(r"<[^>]+>", " ", html[idx : idx + 9000])
        return re.sub(r"\s+", " ", text)[:1000]
    return ""


def extract_rows(html):
    out = {}
    for lab in ["Turnover", "Gross margin", "Profit/Loss", "Equity"]:
        idx = html.find(lab)
        if idx < 0:
            continue
        chunk = re.sub(r"<[^>]+>", "|", html[idx : idx + 1600])
        amounts = re.findall(r"€\s*\|\s*\|\s*([-\d,]+)", chunk)
        pcts = re.findall(r"\|\s*((?:&lt;\s*)?-?\d[\d.,]*%|&lt;\s*-1000%)", chunk)
        if amounts:
            out[lab] = {"amounts": amounts[:3], "pcts": pcts[:2], "chunk": re.sub(r"\s+", " ", chunk)[:220]}
    # FTE
    m = re.search(r"([0-9]+(?:[.,]\d+)?)\s*FTE", html)
    if m:
        out["FTE"] = m.group(1)
    m = re.search(r"filed on ([0-9-]{10})", html, re.I)
    if m:
        out["filed"] = m.group(1)
    last = re.search(r"Last balance sheet year[^0-9]*(\d{4})", html)
    if last:
        out["year"] = last.group(1)
    title = re.search(r"<title>([^<]+)", html)
    if title:
        out["title"] = title.group(1)[:80]
    return out


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

    cands = [
        ("0458352318", "orchidee"),
        ("0413550491", "restel_flats"),
        ("0865574649", "fakkel"),
        ("0874863091", "gravenkasteel"),  # likely used
        ("0821289991", "always_home"),  # used
        ("0442694142", "sebrechts"),  # used
        ("0475400760", "famifamenne"),  # used
        ("0462316153", "le_castel"),  # used
        ("0500937791", "armonea_home"),
        ("0883790853", "happy"),
        # more guesses from Armonea network
        ("0467222769", "miflo"),
        ("0641760611", "numera"),
        ("0880226993", "man_in_motion"),
        ("0650907810", "ventu"),
    ]
    for kbo, label in cands:
        kbo_dot = kbo[:4] + "." + kbo[4:7] + "." + kbo[7:]
        used = kbo in used_blob or kbo_dot in used_blob or label.replace("_", " ") in used_blob
        try:
            html = fetch(label, f"https://www.companyweb.be/en/{kbo}")
            rows = extract_rows(html)
            print(("USED" if used else "FREE"), kbo_dot, label, rows.get("year"), rows.get("title"))
            print(" ", {k: rows[k] for k in rows if k not in ("title", "chunk")})
            mb = money_block(html)
            if mb:
                print(" ", mb[:450])
            print("---")
        except Exception as e:
            print(label, "ERR", e)


if __name__ == "__main__":
    main()
