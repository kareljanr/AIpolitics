# ephemeral fetch tick2045 — Curando YE2025
import re
import ssl
import urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
outdir = Path("docs/doge/data/raw/tick2045")
outdir.mkdir(parents=True, exist_ok=True)
KBO = "0445499422"

URLS = {
    "curando_nl": f"https://www.companyweb.be/nl/{KBO}/curando",
    "curando_en": f"https://www.companyweb.be/en/{KBO}/curando",
    "curando_fr": f"https://www.companyweb.be/fr/{KBO}/curando",
    "curando_kbo": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={KBO}",
    "curando_site": "https://www.curando.be/nl/contact",
}


def fetch(name, url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, context=ctx, timeout=35) as r:
        data = r.read()
    # try decode
    html = data.decode("utf-8", "replace")
    (outdir / f"{name}.html").write_text(html, encoding="utf-8")
    print("OK", name, len(html), url[:80])
    return html


for n, u in URLS.items():
    try:
        fetch(n, u)
    except Exception as e:
        print("FAIL", n, type(e).__name__, str(e)[:180])

# parse EN for filing / FTE / blocks
html = (outdir / "curando_en.html").read_text(encoding="utf-8")
for pat in [
    r"filed on ([0-9\-]+)",
    r"Employees\s*=\s*\"([^\"]+)\"",
    r"Last balance sheet year.{0,80}?(\d{4}|N/A)",
    r"FTEs working[^0-9]*([0-9.,]+)",
    r"total turnover of €([0-9.,]+)",
    r"Profit/Loss.{0,40}?€\s*([0-9.,\-]+)",
]:
    m = re.search(pat, html, re.I | re.S)
    print("MATCH", pat[:40], "->", (m.group(1) if m else None))

blocks = re.findall(
    r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
    html,
)
print("blocks", blocks[:3])

# KBO snippets
kbo = (outdir / "curando_kbo.html").read_text(encoding="utf-8", errors="replace")
for lab in ["Status", "Actief", "Active", "E-mail", "email", "Rechtsvorm", "Adres"]:
    i = kbo.lower().find(lab.lower())
    if i >= 0:
        snip = re.sub(r"\s+", " ", kbo[i : i + 120])
        print("KBO", snip[:110])

# site email
site = (outdir / "curando_site.html").read_text(encoding="utf-8", errors="replace")
emails = sorted(set(re.findall(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}", site)))
print("emails", emails[:10])
