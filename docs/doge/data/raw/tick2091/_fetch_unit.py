# -*- coding: utf-8 -*-
import re
import urllib.request
from pathlib import Path

RAW = Path("docs/doge/data/raw/tick2091")
UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)
KBO = "0413653827"
SLUG = "sint-elisabeth-s-dal"


def fetch(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "nl,en;q=0.8"})
    with urllib.request.urlopen(req, timeout=45) as resp:
        return resp.read(), resp.geturl()


for lang in ("nl", "en", "fr"):
    url = f"https://www.companyweb.be/{lang}/{KBO}/{SLUG}"
    data, final = fetch(url)
    (RAW / f"sed_{lang}.html").write_bytes(data)
    print(lang, len(data), final)

kbo_url = f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={KBO}"
data, final = fetch(kbo_url)
(RAW / "kbo_sed.html").write_bytes(data)
print("kbo", len(data), final)

t = (RAW / "sed_nl.html").read_text(encoding="utf-8", errors="replace")
# dump all year blocks
for m in re.finditer(
    r'(20\d\d)\s*:\s*\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)"',
    t,
):
    print("YR", m.group(1), "winst", m.group(2), "eq", m.group(3), "bruto", m.group(4), "omzet", m.group(5))
for pat in [
    r'amountOfEmployees\s*=\s*"([^"]+)"',
    r"neergelegd op ([0-9.\-]+)",
    r"Laatste balansjaar</[^>]*>\s*<[^>]*>\s*(\d{4})",
    r'NACE[^<]*</[^>]*>\s*<[^>]*>\s*([^<]+)',
    r'email[^>]*>\s*([^<]+@[^<]+)',
    r'itemprop="email"[^>]*content="([^"]+)"',
    r'https?://[a-zA-Z0-9./\-]+elisabeth[a-zA-Z0-9./\-]*',
    r'adres[^>]*>\s*([^<]{10,80})',
]:
    m = re.search(pat, t, re.I)
    if m:
        print("MATCH", pat[:40], "->", m.group(1)[:120] if m.lastindex else m.group(0)[:120])

# KBO bits
kt = (RAW / "kbo_sed.html").read_text(encoding="utf-8", errors="replace")
for pat in [
    r"Status:\s*</[^>]*>\s*<[^>]*>\s*<[^>]*>\s*([^<]+)",
    r"Ondernemingsnummer:\s*</[^>]*>\s*<[^>]*>\s*([\d.]+)",
    r"Vereniging zonder winstoogmerk|Association sans but lucratif",
    r"(\d+)\s*vestiging",
    r"Aanbestedende overheid",
    r"([A-Z][a-z]+straat[^<]{0,60}|Grote Markt[^<]{0,40}|Kerkstraat[^<]{0,40})",
]:
    m = re.search(pat, kt, re.I)
    if m:
        print("KBO", pat[:50], "->", (m.group(1) if m.lastindex else m.group(0))[:120])
