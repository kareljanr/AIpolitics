import re
import urllib.request
import ssl
from pathlib import Path

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
raw = Path(__file__).resolve().parent
KBO = "0407149877"
KBO_DOT = "0407.149.877"

urls = {
    "stallbois_en": f"https://www.companyweb.be/en/{KBO}",
    "stallbois_nl": f"https://www.companyweb.be/nl/{KBO}",
    "stallbois_fr": f"https://www.companyweb.be/fr/{KBO}",
    "kbo_toon": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={KBO}&lang=nl",
    "kbo_0": f"https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer={KBO}&actionLu=Zoek",
    "faro_en": "https://www.companyweb.be/en/0893863017",
    "aiesh_en": "https://www.companyweb.be/en/0201712587",
    "rew_en": "https://www.companyweb.be/en/0203541556",
    "leseta": "https://leseta.be/annuaire-eta/stallbois/",
    "site": "https://www.stallbois.be/",
}


def clean_cells(row):
    cells = re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", row, re.S)
    cells = [re.sub(r"<[^>]+>", "", c).strip() for c in cells]
    return [re.sub(r"\s+", " ", c) for c in cells if c]


def parse_cw(name, html):
    print("====", name)
    m = re.search(r"cw\.kernCijfers\s*=\s*\{(.*?)\n\s*\};", html, re.S)
    if m:
        years = re.findall(r"(20\d{2})\s*:\s*\{([^}]+)\}", m.group(1))
        for y, body in years[:4]:
            fields = dict(
                re.findall(
                    r"(winst|eigen_vermogen|bruto_marge|omzet):\s*\"([^\"]*)\"", body
                )
            )
            print(y, fields)
    for label, pat in [
        ("year", r"Last balance sheet year.*?<[^>]+>(\d{4}|N/A)"),
        ("year_nl", r"Laatste balansjaar.*?<[^>]+>(\d{4}|N/A)"),
        ("year_fr", r"Dernier (?:bilan|exercice).*?<[^>]+>(\d{4}|N/A)"),
        ("filed_en", r"filed on ([0-9.\-/]+)"),
        ("filed_nl", r"neergelegd op ([0-9.\-/]+)"),
        ("filed_fr", r"d[eé]pos[eé]s? le ([0-9.\-/]+)"),
        ("status", r"Status.*?<[^>]+>(Active|Actief|Actif)"),
        ("nace", r"Principal activity.*?<[^>]+>([^<]+)"),
        ("nace_nl", r"Hoofdactiviteit.*?<[^>]+>([^<]+)"),
        ("name", r"<h1[^>]*>(.*?)</h1>"),
    ]:
        m = re.search(pat, html, re.S | re.I)
        if m:
            print(f"  {label}:", re.sub(r"<[^>]+>|\s+", " ", m.group(1)).strip()[:120])
    for pat in [
        r"There are ([0-9.,]+) FTEs",
        r"Er werken ([0-9.,]+) FTE",
        r"Il y a ([0-9.,]+) employés",
    ]:
        m = re.search(pat, html, re.I | re.S)
        if m:
            print("  FTE:", m.group(1))
    emails = sorted(set(re.findall(r"[\w.+-]+@[\w.-]+\.\w+", html)))
    emails = [e for e in emails if "companyweb" not in e.lower() and "example" not in e]
    if emails:
        print("  emails:", emails[:10])


def parse_kbo(html):
    print("==== KBO")
    text = re.sub(r"<[^>]+>", " ", html)
    text = re.sub(r"\s+", " ", text)
    for needle in [
        "Actief",
        "Active",
        "Normale toestand",
        "Coöperatieve",
        "cooperatieve",
        "Société coopérative",
        "88.993",
        "88.999",
        "vestigingseenheden",
        "STALLBOIS",
        "Etalle",
        "Belle-Vue",
        "Belle Vue",
    ]:
        if needle.lower() in text.lower():
            idx = text.lower().find(needle.lower())
            print(" ", text[max(0, idx - 40) : idx + 90])


for name, url in urls.items():
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=45) as r:
            data = r.read()
        (raw / f"{name}.html").write_bytes(data)
        html = data.decode("utf-8", "ignore")
        print(f"FETCH OK {name} {len(data)}")
        if name.startswith("stallbois_") or name in ("faro_en", "aiesh_en", "rew_en"):
            parse_cw(name, html)
        elif name.startswith("kbo"):
            parse_kbo(html)
        else:
            title = re.search(r"<title[^>]*>([^<]+)", html, re.I)
            print("  title", title.group(1)[:80] if title else None)
            emails = sorted(set(re.findall(r"[\w.+-]+@[\w.-]+\.\w+", html)))
            emails = [
                e
                for e in emails
                if not any(x in e.lower() for x in ("example", "sentry", "wix", "google"))
            ]
            print("  emails", emails[:15])
    except Exception as e:
        print(f"FETCH FAIL {name}: {e}")
