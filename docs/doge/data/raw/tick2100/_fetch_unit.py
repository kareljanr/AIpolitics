# -*- coding: utf-8 -*-
"""Fetch SLG Vlaanderen VZW YE2025 full + KBO."""
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
KBO = "0410958712"
slug = "slg-vlaanderen"


def get(url, out):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=CTX, timeout=30) as resp:
        html = resp.read().decode("utf-8", "replace")
    out.write_text(html, encoding="utf-8")
    return html


def scrub(h):
    h = re.sub(r"<script[^>]*>.*?</script>", " ", h, flags=re.S | re.I)
    return re.sub(r"<style[^>]*>.*?</style>", " ", h, flags=re.S | re.I)


for lang, path in [
    ("nl", RAW / "slgv_nl.html"),
    ("en", RAW / "slgv_en.html"),
    ("fr", RAW / "slgv_fr.html"),
]:
    url = f"https://www.companyweb.be/{lang}/{KBO}/{slug}"
    print("GET", url)
    html = get(url, path)
    years = PAT.findall(html)
    print(" years", years[:3])
    nls = scrub(html)
    for label in ["Winst/Verlies", "Omzet", "Eigen vermogen", "Brutomarge", "Personeel", "Profit", "Turnover"]:
        m = re.search(rf"{label}.*?(?=</tr>|<tr)", nls, re.S | re.I)
        if m:
            cells = [c.strip() for c in re.findall(r">\s*([^<>]{1,40}?)\s*<", m.group(0)) if c.strip()]
            print(label, cells[:10])
    m = re.search(
        r"(?:neergelegd|filed|déposé|Laatste jaarrekening)[^0-9]{0,80}(\d{2}[-/.]\d{2}[-/.]\d{4})",
        nls,
        re.I,
    )
    print(" filed", m.group(1) if m else None)

kbo_url = (
    "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?"
    f"ondernemingsnummer={KBO}"
)
print("GET", kbo_url)
khtml = get(kbo_url, RAW / "slgv_kbo.html")
txt = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", scrub(khtml)))
idx = txt.find("Gegevens van de geregistreerde")
print(txt[idx : idx + 1600] if idx >= 0 else txt[500:1800])
