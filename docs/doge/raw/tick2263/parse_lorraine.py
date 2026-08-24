import re
import urllib.request
import ssl
from pathlib import Path

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
raw = Path(__file__).resolve().parent

# also fetch KBO
kbo_url = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0412131719"
# try both KBO URL forms
alts = [
    "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer=0412131719",
    "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0412131719",
]


def fetch(url, name):
    req = urllib.request.Request(url, headers=ua)
    with urllib.request.urlopen(req, context=ctx, timeout=30) as r:
        data = r.read()
    (raw / name).write_bytes(data)
    print("OK", name, len(data), url)
    return data.decode("utf-8", "ignore")


def clean(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s)).strip()


def parse_table(html, label):
    print("====", label)
    for pat in [
        r"Financial data.*?</table>",
        r"Financiële data.*?</table>",
        r"Kerncijfers.*?</table>",
        r"Key figures.*?</table>",
        r"Chiffres clés.*?</table>",
        r"Données financières.*?</table>",
    ]:
        block = re.search(pat, html, re.I | re.S)
        if block:
            print(" matched", pat[:30])
            rows = re.findall(r"<tr[^>]*>(.*?)</tr>", block.group(0), re.S)
            for row in rows[:15]:
                cells = re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", row, re.S)
                cells = [clean(c) for c in cells]
                cells = [c for c in cells if c]
                if cells:
                    print(" ", cells)
            break
    # look for Turnover / Omzet anywhere near 2025
    for kw in [
        "Turnover",
        "Omzet",
        "Chiffre d'affaires",
        "Gross margin",
        "Brutomarge",
        "Marge brute",
        "Profit/Loss",
        "Winst/Verlies",
        "Equity",
        "Eigen vermogen",
        "Employees",
        "Werknemers",
        "filed on",
        "neergelegd",
        "dépos",
    ]:
        for m in re.finditer(re.escape(kw), html, re.I):
            snip = clean(html[m.start() : m.start() + 180])
            if snip:
                print(" SNIP", snip[:160])
                break


for lang in ("en", "nl", "fr"):
    html = (raw / f"lorraine_{lang}.html").read_text(encoding="utf-8", errors="ignore")
    parse_table(html, f"lorraine_{lang}")

# KBO
for i, url in enumerate(alts):
    try:
        html = fetch(url, f"kbo_{i}.html")
        print("==== KBO", i)
        for pat in [
            r"Status van de entiteit.*?</tr>",
            r"Toestand van de entiteit.*?</tr>",
            r"Rechtsvorm.*?</tr>",
            r"Maatschappelijke benaming.*?</tr>",
            r"Adres van de zetel.*?</tr>",
            r"Aantal vestigingseenheden.*?</tr>",
            r"E-mail.*?</tr>",
            r"Web.*?</tr>",
            r"Nace[^<]{0,200}",
            r"Begindatum.*?</tr>",
        ]:
            m = re.search(pat, html, re.I | re.S)
            if m:
                print(" ", clean(m.group(0))[:200])
        # activities
        acts = re.findall(r"(\d{2}\.\d{3})[^<]{0,80}", html)
        print(" nace codes", acts[:10])
        break
    except Exception as e:
        print("KBO fail", i, e)

# try company site / email
for url, name in [
    ("https://www.lalorraineservices.be/", "site.html"),
    ("https://www.companyweb.be/en/0412131719", "cw_en_again.html"),
]:
    try:
        html = fetch(url, name)
        emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", html)
        print(name, "emails", list(dict.fromkeys(emails))[:10])
        title = re.search(r"<title>([^<]+)", html, re.I)
        print(name, "title", title.group(1)[:100] if title else None)
    except Exception as e:
        print("site fail", name, e)
