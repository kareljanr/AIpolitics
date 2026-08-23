# ephemeral fetch tick2039 — C.W.Z.C. Zonhoven NL/EN/FR + KBO + site
import re
import ssl
import urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
outdir = Path("docs/doge/data/raw/tick2039")
outdir.mkdir(parents=True, exist_ok=True)

KBO = "0413203073"
urls = {
    "cwzc_nl": f"https://www.companyweb.be/nl/{KBO}/christelijke-woon-en-zorgcentra",
    "cwzc_en": f"https://www.companyweb.be/en/{KBO}/christelijke-woon-en-zorgcentra",
    "cwzc_fr": f"https://www.companyweb.be/fr/{KBO}/christelijke-woon-en-zorgcentra",
    "cwzc_kbo": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={KBO}",
}


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
        data = r.read()
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        text = data.decode("latin-1", "replace")
    (outdir / f"{name}.html").write_text(text, encoding="utf-8")
    print("saved", name, len(text))
    return text


for name, url in urls.items():
    try:
        fetch(name, url)
    except Exception as e:
        print("FAIL", name, type(e).__name__, str(e)[:140])

# site candidates
for name, url in [
    ("cwzc_site", "https://www.cwzc.be/"),
    ("cwzc_site2", "https://www.christelijkewoonenzorgcentra.be/"),
]:
    try:
        fetch(name, url)
    except Exception as e:
        print("FAIL", name, type(e).__name__, str(e)[:140])

html = (outdir / "cwzc_en.html").read_text(encoding="utf-8")
blocks = re.findall(
    r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
    html,
)
emp = re.search(r'Employees\s*=\s*"([^"]+)"', html)
filed = re.search(r"filed on\s*([0-9\-]+)", html, re.I) or re.search(
    r"neergelegd op\s*([0-9\.\-]+)", html, re.I
)
print("emp", emp.group(1) if emp else None)
print("filed", filed.group(1) if filed else None)
for i, b in enumerate(blocks[:3]):
    vals = tuple(parse_amount(x) for x in b)
    print(f"y{i}", vals)

# KBO extract
kbo = (outdir / "cwzc_kbo.html").read_text(encoding="utf-8", errors="replace")
for pat in [
    r"Status van de entiteit</td>\s*<td[^>]*>\s*([^<]+)",
    r"Rechtsvorm</td>\s*<td[^>]*>.*?>([^<]+)",
    r"Adres van de zetel</td>\s*<td[^>]*>\s*([^<]+(?:<br/?>[^<]+)*)",
    r"E-mailadres</td>\s*<td[^>]*>\s*([^<]+)",
    r"Aantal vestigingseenheden</td>\s*<td[^>]*>\s*([^<]+)",
]:
    m = re.search(pat, kbo, re.I | re.S)
    if m:
        print("KBO", re.sub(r"<[^>]+>", " ", m.group(1)).strip()[:120])
