# -*- coding: utf-8 -*-
"""Fetch SLG Operaties Vlaanderen YE2025 + REW hunt + AIESH confirm."""
import re
import ssl
import urllib.request
from pathlib import Path

RAW = Path(__file__).resolve().parent
CTX = ssl.create_default_context()
UA = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "nl-BE,nl;q=0.9,en;q=0.8,fr;q=0.7",
}
PAT = re.compile(
    r'(20\d\d)\s*:\s*\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",'
    r'\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)"'
)
FTE = re.compile(
    r'(?:Personeel|Personnel|Employees|FTE|VTE)[^0-9]{0,80}([\d]+[.,]\d+|[\d]+)',
    re.I,
)
FILED = re.compile(
    r"(?:neergelegd|filed|déposé|Laatste jaarrekening)[^0-9]{0,80}(\d{2}[-/.]\d{2}[-/.]\d{4})",
    re.I,
)
NACE = re.compile(r"(?:NACE|Nace-code|Code NACE)[^0-9A-Z]{0,40}(\d{2}\.?\d{0,3})", re.I)
EMAIL = re.compile(r"mailto:([a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,})")
VE = re.compile(r"(?:vestiging|établissement|establishment)[^0-9]{0,40}(\d+)", re.I)


def get(url: str, out: Path):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=CTX, timeout=30) as resp:
        html = resp.read().decode("utf-8", "replace")
    out.write_text(html, encoding="utf-8")
    return html


def euros(s: str):
    s = s.replace(".", "").replace(",", ".").replace(" ", "").replace("\xa0", "")
    if s in ("", "-", "n.v.t.", "n/a", "N/A"):
        return None
    try:
        return float(s)
    except ValueError:
        return None


KBO = "0845064196"
slug = "slg-operaties-vlaanderen"
for lang, path in [
    ("nl", RAW / "slg_nl.html"),
    ("en", RAW / "slg_en.html"),
    ("fr", RAW / "slg_fr.html"),
]:
    url = f"https://www.companyweb.be/{lang}/{KBO}/{slug}"
    print("GET", url)
    html = get(url, path)
    years = PAT.findall(html)
    print(" LANG", lang, "years", years[:4])
    for y in years[:2]:
        print("  ", y, "->", [euros(x) for x in y[1:]])
    fm = FTE.search(html)
    print("  FTE match", fm.group(0)[:80] if fm else None)
    fd = FILED.search(html)
    print("  filed", fd.group(1) if fd else None)
    nm = NACE.search(html)
    print("  nace", nm.group(1) if nm else None)
    em = EMAIL.findall(html)
    print("  emails", em[:5])

# KBO public
kbo_url = (
    "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?"
    f"ondernemingsnummer={KBO}"
)
print("GET", kbo_url)
try:
    khtml = get(kbo_url, RAW / "slg_kbo.html")
    print(" KBO len", len(khtml))
    for pat in [
        r"Status van de entiteit</td>\s*<td[^>]*>\s*<[^>]+>([^<]+)",
        r"Rechtsvorm</td>\s*<td[^>]*>.*?>([^<]+)",
        r"Aard van de gegevens</td>",
        r"aanbestedende|pouvoir adjudicateur|contracting",
        r"Start datum</td>\s*<td[^>]*>\s*([^<]+)",
    ]:
        m = re.search(pat, khtml, re.I | re.S)
        if m:
            print(" ", pat[:40], "->", re.sub(r"\s+", " ", m.group(0 if m.lastindex is None else 1)[:120]))
except Exception as e:
    print("KBO ERR", e)

# REW hunt via companyweb search-ish known names
rew_kbos = [
    ("0203303145", "reseaux"),
    ("0203301234", "rew"),
    ("0267430123", "rew"),
    ("0201754321", "rew"),
    ("0212456789", "rew"),
    ("0201689123", "rew"),
    ("0478123456", "rew"),
    ("0201555666", "rew"),
    ("0216987654", "rew"),
    ("0220123456", "rew"),
]
# Try known: Réseau d'Electricité de Wavre / REW often KBO 0220.xxx or similar
# From prior HTML aiesh/rew in tick2096
for html_path in [
    Path("docs/doge/data/raw/tick2096/aiesh_nl.html"),
    Path("docs/doge/data/raw/tick2096/rew_nl.html"),
    Path("docs/doge/data/raw/tick2096/faro_nl.html"),
]:
    if html_path.exists():
        t = html_path.read_text(encoding="utf-8", errors="replace")
        years = PAT.findall(t)
        title = re.search(r"<title>([^<]+)", t)
        print("PRIOR", html_path.name, title.group(1)[:70] if title else "?", "yrs", [y[0] for y in years[:4]])
        # extract enterprise number
        for m in re.findall(r"BE0?(\d{3})[.\s]?(\d{3})[.\s]?(\d{3})", t)[:3]:
            print("  BE", "".join(m))

# Try Wavre REW official KBO from web knowledge: 0220.002.997? 
extra = [
    ("0220002997", "rew-wavre"),
    ("0203002997", "rew"),
    ("0215499655", "reseaux-electricite-wavre"),
    ("0200654321", "rew"),
    ("0432123456", "rew"),
    ("0201713456", "rew"),
    ("0222345678", "reseaux"),
    ("0207456789", "electricite-wavre"),
]
for kbo, slug in extra:
    url = f"https://www.companyweb.be/nl/{kbo}/{slug}"
    try:
        html = get(url, RAW / f"rewtry_{kbo}.html")
        years = PAT.findall(html)
        title = re.search(r"<title>([^<]+)", html)
        print("REWTRY", kbo, title.group(1)[:60] if title else "?", [y[0] for y in years[:3]])
    except Exception as e:
        print("REWTRY ERR", kbo, str(e)[:60])
