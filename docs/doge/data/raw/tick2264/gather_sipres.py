import re
import urllib.request
import ssl
from pathlib import Path
from html.parser import HTMLParser

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
raw = Path(__file__).resolve().parent
KBO = "0423643540"
KBO_DOT = "0423.643.540"

urls = {
    "sipres_en": f"https://www.companyweb.be/en/{KBO}",
    "sipres_nl": f"https://www.companyweb.be/nl/{KBO}",
    "sipres_fr": f"https://www.companyweb.be/fr/{KBO}",
    "kbo_toon": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={KBO}",
    "kbo_0": f"https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer={KBO}&actionLu=Zoek",
    "site": "https://www.sipres-services.be/",
    "leseta": "https://leseta.be/annuaire-eta/sipres/",
}


def clean_cells(row):
    cells = re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", row, re.S)
    cells = [re.sub(r"<[^>]+>", "", c).strip() for c in cells]
    return [re.sub(r"\s+", " ", c) for c in cells if c]


def parse_cw(name, html):
    print("====", name)
    for label, pat in [
        ("year", r"Last balance sheet year.*?<[^>]+>(\d{4}|N/A)"),
        ("year_nl", r"Laatste balansjaar.*?<[^>]+>(\d{4}|N/A)"),
        ("year_fr", r"Dernier (?:bilan|exercice).*?<[^>]+>(\d{4}|N/A)"),
        ("filed_en", r"filed on ([0-9.\-/]+)"),
        ("filed_nl", r"neergelegd op ([0-9.\-/]+)"),
        ("filed_fr", r"d[eé]pos[eé]s? le ([0-9.\-/]+)"),
        ("status", r"Status.*?<[^>]+>(Active|Actief|Actif)"),
        ("size", r"Company size.*?<[^>]+>([^<]+)"),
        ("size_nl", r"Bedrijfsgrootte.*?<[^>]+>([^<]+)"),
        ("nace", r"Principal activity.*?<[^>]+>([^<]+)"),
        ("nace_nl", r"Hoofdactiviteit.*?<[^>]+>([^<]+)"),
        ("nace_fr", r"Activité principale.*?<[^>]+>([^<]+)"),
        ("name", r"<h1[^>]*>(.*?)</h1>"),
        ("addr", r"(?:located at|zetel.*?is|siège social.*?est)\s*([^.<]+)"),
    ]:
        m = re.search(pat, html, re.S | re.I)
        if m:
            print(f"  {label}:", re.sub(r"<[^>]+>|\s+", " ", m.group(1)).strip()[:100])
    block = re.search(
        r"(?:Financial data|Financiële data|Données financières).*?</table>",
        html,
        re.I | re.S,
    )
    if block:
        rows = re.findall(r"<tr[^>]*>(.*?)</tr>", block.group(0), re.S)
        for row in rows[:10]:
            cells = clean_cells(row)
            if cells:
                print(" ", cells)
    # FTE
    for pat in [
        r"Average number of employees.*?<[^>]+>([^<]+)",
        r"Gemiddeld aantal werknemers.*?<[^>]+>([^<]+)",
        r"Nombre moyen d.employés.*?<[^>]+>([^<]+)",
        r"There are ([0-9.,]+) FTEs",
        r"Er werken ([0-9.,]+) FTE",
        r"Il y a ([0-9.,]+) employés",
    ]:
        m = re.search(pat, html, re.I | re.S)
        if m:
            print("  FTE:", re.sub(r"\s+", " ", m.group(1))[:60])


def parse_kbo(html):
    print("==== KBO")
    text = re.sub(r"<[^>]+>", " ", html)
    text = re.sub(r"\s+", " ", text)
    for needle in [
        "Actief",
        "Active",
        "Actif",
        "Normale toestand",
        "Situation normale",
        "Normal situation",
        "Vereniging zonder winstoogmerk",
        "Association sans but lucratif",
        "Non-profit",
        "88.993",
        "88.999",
        "vestigingseenheden",
        "unités d'établissement",
        "establishment units",
        "SIPRES",
        "Sipres",
        "Ghlin",
        "Mons",
        "Eva Dupont",
    ]:
        if needle.lower() in text.lower():
            idx = text.lower().find(needle.lower())
            print(" ", text[max(0, idx - 40) : idx + 80])


for name, url in urls.items():
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=30) as r:
            data = r.read()
        (raw / f"{name}.html").write_bytes(data)
        html = data.decode("utf-8", "ignore")
        print(f"FETCH OK {name} {len(data)}")
        if name.startswith("sipres_"):
            parse_cw(name, html)
        elif name.startswith("kbo"):
            parse_kbo(html)
        else:
            print("  title", re.search(r"<title[^>]*>([^<]+)", html, re.I))
            emails = set(re.findall(r"[\w.+-]+@[\w.-]+\.\w+", html))
            print("  emails", list(emails)[:8])
    except Exception as e:
        print("FAIL", name, type(e).__name__, e)
