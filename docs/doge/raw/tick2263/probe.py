import re
import urllib.request
import ssl
from pathlib import Path

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
raw = Path(__file__).resolve().parent
raw.mkdir(parents=True, exist_ok=True)

targets = {
    "faro_en": "https://www.companyweb.be/en/0893863017",
    "aiesh_en": "https://www.companyweb.be/en/0201712587",
    "rew_en": "https://www.companyweb.be/en/0644638937",
    "lorraine_en": "https://www.companyweb.be/en/0412131719",
    "lorraine_nl": "https://www.companyweb.be/nl/0412131719",
    "lorraine_fr": "https://www.companyweb.be/fr/0412131719",
    "agb_bornem": "https://www.bornem.be/bestuur/financien/jaarrekening",
}


def clean_cells(row):
    cells = re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", row, re.S)
    cells = [re.sub(r"<[^>]+>", "", c).strip() for c in cells]
    return [re.sub(r"\s+", " ", c) for c in cells if c]


def parse_cw(name, html):
    print("====", name)
    y = re.search(r"Last balance sheet year.*?<[^>]+>(\d{4})", html, re.S | re.I)
    y2 = re.search(r"Laatste balansjaar.*?<[^>]+>(\d{4})", html, re.S | re.I)
    y3 = re.search(r"Dernier exercice.*?<[^>]+>(\d{4})", html, re.S | re.I)
    print(
        " year EN/NL/FR",
        y.group(1) if y else None,
        y2.group(1) if y2 else None,
        y3.group(1) if y3 else None,
    )
    filed = re.search(r"filed on ([0-9.\-/]+)", html, re.I)
    filed2 = re.search(r"neergelegd op ([0-9.\-/]+)", html, re.I)
    filed3 = re.search(r"d[eé]pos[eé]s? le ([0-9.\-/]+)", html, re.I)
    f = filed or filed2 or filed3
    print(" filed", f.group(1) if f else None)
    block = re.search(r"Financial data.*?</table>", html, re.I | re.S)
    if not block:
        block = re.search(r"Financiële data.*?</table>", html, re.I | re.S)
    if not block:
        block = re.search(r"Données financières.*?</table>", html, re.I | re.S)
    if block:
        rows = re.findall(r"<tr[^>]*>(.*?)</tr>", block.group(0), re.S)
        for row in rows[:12]:
            cells = clean_cells(row)
            if cells:
                print(" ", cells)
    else:
        print("  NO financial table")
    for pat in [
        r"Average number of employees.*?<[^>]+>([^<]+)",
        r"Gemiddeld aantal werknemers.*?<[^>]+>([^<]+)",
        r"Nombre moyen d.employés.*?<[^>]+>([^<]+)",
    ]:
        m = re.search(pat, html, re.I | re.S)
        if m:
            print(" FTE-ish", re.sub(r"\s+", " ", m.group(1))[:60])


for name, url in targets.items():
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=30) as r:
            data = r.read()
        (raw / f"{name}.html").write_bytes(data)
        html = data.decode("utf-8", "ignore")
        print(f"FETCH OK {name} {len(data)}")
        if "bornem" in name:
            print(
                "  2025",
                html.count("2025"),
                "2024",
                html.count("2024"),
            )
            pdfs = re.findall(r'href="([^"]+\.pdf)"', html, re.I)
            print("  pdfs", pdfs[:8])
            for y in ("Jaarrekening 2025", "jaarrekening-2025", "JR2025", "2025"):
                if y.lower() in html.lower():
                    print("  hit", y)
        else:
            parse_cw(name, html)
    except Exception as e:
        print("FAIL", name, type(e).__name__, e)
