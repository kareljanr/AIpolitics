# ephemeral refetch Ternat Sint-Carolus (not Mayerhof)
import re
import ssl
import urllib.request
from pathlib import Path

outdir = Path("docs/doge/data/raw/tick2027")
outdir.mkdir(parents=True, exist_ok=True)
ctx = ssl.create_default_context()


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


for name, url in [
    ("ternat_nl", "https://www.companyweb.be/nl/0409970203/woonzorgcentrum-sint-carolus"),
    ("ternat_en", "https://www.companyweb.be/en/0409970203/woonzorgcentrum-sint-carolus"),
    ("ternat_fr", "https://www.companyweb.be/fr/0409970203/woonzorgcentrum-sint-carolus"),
    (
        "ternat_kbo",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0409970203",
    ),
    ("ternat_site", "https://www.sintcarolus.be/"),
]:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
            html = r.read().decode("utf-8", "replace")
        (outdir / f"{name}.html").write_text(html, encoding="utf-8")
        title = re.search(r"<title>([^<]+)</title>", html)
        print("==", name, (title.group(1)[:90] if title else None))
        if "kbo" in name or "site" in name:
            emails = sorted(
                set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", html))
            )
            print(" emails", emails[:6])
            continue
        year = None
        for lab in ["Last balance sheet year", "Laatste balansjaar", "Dernier bilan"]:
            i = html.find(lab)
            if i >= 0:
                m = re.search(r"font-medium[^>]*>\s*(\d{4}|N/A)", html[i : i + 220])
                if m:
                    year = m.group(1)
        blocks = re.findall(
            r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
            html,
        )
        print(" year", year, "n", len(blocks))
        if blocks:
            y0 = tuple(parse_amount(x) for x in blocks[0])
            y1 = tuple(parse_amount(x) for x in blocks[1]) if len(blocks) > 1 else None
            print(" y0", y0)
            if y1:
                print(" y1", y1)
                for n, i in [("winst", 0), ("equity", 1), ("bruto", 2), ("omzet", 3)]:
                    a, b = y0[i], y1[i]
                    pct = (a - b) / abs(b) * 100 if b else None
                    print(f"  {n} {a:.0f} vs {b:.0f} {pct:+.2f}%")
        m2 = re.search(r'Employees\s*=\s*"([^"]+)"', html)
        print(" emp", m2.group(1) if m2 else None)
        # confirm address Ternat not Mortsel
        if "Ternat" in html or "1742" in html:
            print(" addr_ok Ternat")
        if "Mortsel" in html:
            print(" WARN Mortsel in page")
        for lab in ["filed on", "neergelegd op", "déposés le"]:
            j = html.lower().find(lab.lower())
            if j >= 0:
                print(" filed", html[j : j + 55])
                break
    except Exception as e:
        print("FAIL", name, type(e).__name__, e)
