# ephemeral parse Samen Ouder + fetch NL/FR/KBO for tick2040
import re
import ssl
import urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
outdir = Path("docs/doge/data/raw/tick2040")
outdir.mkdir(parents=True, exist_ok=True)


def parse_amount(s):
    s = s.strip().replace("\xa0", " ").replace(" ", "")
    if "," in s and "." not in s:
        parts = s.split(",")
        if len(parts) >= 2 and all(len(p) == 3 for p in parts[1:]):
            s = s.replace(",", "")
        elif len(parts) == 2 and len(parts[1]) <= 2:
            s = s.replace(",", ".")
        else:
            s = s.replace(",", "")
    elif "," in s and "." in s:
        if s.rfind(",") > s.rfind("."):
            s = s.replace(".", "").replace(",", ".")
        else:
            s = s.replace(",", "")
    elif s.count(".") > 1:
        s = s.replace(".", "")
    return float(s)


def fetch(name, url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, context=ctx, timeout=30) as r:
        html = r.read().decode("utf-8", "replace")
    (outdir / f"{name}.html").write_text(html, encoding="utf-8")
    return html


def summarize(name, html):
    title = re.search(r"<title>([^<]+)", html)
    year = None
    for lab in ["Last balance sheet year", "Laatste balansjaar", "Dernier bilan"]:
        i = html.find(lab)
        if i >= 0:
            m = re.search(r"font-medium[^>]*>\s*(\d{4}|N/A)", html[i : i + 220])
            if m:
                year = m.group(1)
                break
    blocks = re.findall(
        r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
        html,
    )
    emp = re.search(r'Employees\s*=\s*"([^"]+)"', html)
    filed = None
    for lab in ["Filed on", "Neergelegd op", "Déposés le"]:
        i = html.find(lab)
        if i >= 0:
            m = re.search(r"(\d{2}[-/.]\d{2}[-/.]\d{4})", html[i : i + 200])
            if m:
                filed = m.group(1)
                break
    print("==", name, "Y", year, "filed", filed, "emp", emp.group(1) if emp else None)
    print("  title", (title.group(1)[:80] if title else ""))
    if blocks:
        y0 = tuple(parse_amount(x) for x in blocks[0])
        print("  y0 pnl/eq/bruto/omzet", y0)
        if len(blocks) > 1:
            y1 = tuple(parse_amount(x) for x in blocks[1])
            print("  y1", y1)
            if y1[3]:
                print("  omzet_pct", round((y0[3] - y1[3]) / abs(y1[3]) * 100, 2))
            if y1[0]:
                print("  pnl_pct", round((y0[0] - y1[0]) / abs(y1[0]) * 100, 2))
            if y1[1]:
                print("  eq_pct", round((y0[1] - y1[1]) / abs(y1[1]) * 100, 2))
            if y1[2]:
                print("  bruto_pct", round((y0[2] - y1[2]) / abs(y1[2]) * 100, 2))
    return year, blocks


# Prefer EN already from probe; also NL/FR + KBO + site
urls = {
    "samen_ouder_en": "https://www.companyweb.be/en/0453287037/woonzorg-samen-ouder",
    "samen_ouder_nl": "https://www.companyweb.be/nl/0453287037/woonzorg-samen-ouder",
    "samen_ouder_fr": "https://www.companyweb.be/fr/0453287037/woonzorg-samen-ouder",
    "samen_ouder_kbo": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0453287037",
}

for name, url in urls.items():
    try:
        html = fetch(name, url)
        if "kbo" in name:
            # extract emails / status / address snippets
            emails = sorted(set(re.findall(r"[\w.+-]+@[\w.-]+\.\w+", html)))
            print("== kbo emails", emails[:8])
            for pat in ["Actief", "Active", "Actif", "VZW", "ASBL", "Tereken", "vestiging"]:
                if pat.lower() in html.lower():
                    print("  has", pat)
            # VE count
            m = re.search(r"(\d+)\s*(?:vestiging|établissement|establishment)", html, re.I)
            if m:
                print("  VE?", m.group(0))
        else:
            summarize(name, html)
    except Exception as e:
        print("FAIL", name, type(e).__name__, str(e)[:160])

# try site / email clues
for name, url in [
    ("dearkzc_site", "https://www.dearkzc.be/"),
    ("samen_ouder_site_guess", "https://www.woonzorgsamenouder.be/"),
]:
    try:
        html = fetch(name, url)
        print("==", name, "len", len(html), "title", (re.search(r"<title>([^<]+)", html) or type("", (), {"group": lambda s, n: "?"})()).group(1)[:70])
        emails = sorted(set(re.findall(r"[\w.+-]+@[\w.-]+\.\w+", html)))
        print("  emails", emails[:10])
    except Exception as e:
        print("FAIL", name, type(e).__name__, str(e)[:120])
