import re
import ssl
import urllib.request
from pathlib import Path

CTX = ssl.create_default_context()
OUT = Path("docs/doge/raw/tick2222")

# Manus VZW FR + KBO + site
extra = {
    "manus_vzw_fr": "https://www.companyweb.be/fr/0808114522/manus",
    "manus_vzw_kbo": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0808114522",
    "manus_site": "https://www.manus.tv/",
    "herop_nl2": "https://www.companyweb.be/nl/0406678141/heropbeuring",
}
for k, u in extra.items():
    try:
        req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=CTX, timeout=30) as r:
            html = r.read().decode("utf-8", "replace")
        (OUT / f"{k}.html").write_text(html, encoding="utf-8")
        print(k, "ok", len(html))
    except Exception as e:
        print(k, e)

# parse Manus VZW
for name in ["manus_bxl_nl.html", "manus_vzw_en.html", "manus_vzw_fr.html", "manus_vzw_kbo.html"]:
    p = OUT / name
    if not p.exists():
        continue
    html = p.read_text(encoding="utf-8")
    print("====", name)
    m = re.search(r"window\.cw\.kernCijfers\s*=\s*\{(.*?)\};", html, re.S)
    if m:
        print(m.group(1)[:900])
    m = re.search(r'amountOfEmployees\s*=\s*"([^"]+)"', html)
    print("emp", m.group(1) if m else None)
    for pat in [r"neergelegd op ([0-9-]+)", r"filed on ([0-9-]+)", r"déposés le ([0-9-]+)"]:
        ms = re.findall(pat, html)
        if ms:
            print(pat, ms[0])
    text = re.sub(r"<[^>]+>", " ", html)
    text = re.sub(r"\s+", " ", text)
    m = re.search(r"Aantal vestigingseenheden \(VE\):\s*(\d+)", text)
    if m:
        print("VE", m.group(1))
    m = re.search(r"Adres van de zetel:.{0,100}", text)
    if m:
        print("addr", m.group(0)[:120])
    m = re.search(r"Begindatum:.{0,60}", text)
    if m:
        print("begin", m.group(0)[:80])
    m = re.search(r"Status:\s*(\w+)", text)
    if m:
        print("status", m.group(1))
    for nace in re.findall(r"88\.\d{3}", text):
        print("nace", nace)
        break
    emails = sorted(set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", html)))
    print("emails", [e for e in emails if "sentry" not in e][:5])

# deltas
br25, br24 = 3044848, 2800796
pn25, pn24 = 600300, 495811
eq25, eq24 = 2039760, 1439460
print("bruto pct", round((br25 / br24 - 1) * 100, 2))
print("pnl pct", round((pn25 / pn24 - 1) * 100, 2))
print("equity pct", round((eq25 / eq24 - 1) * 100, 2))

# heropbeuring kern retry
html = (OUT / "heropbeuring_nl.html").read_text(encoding="utf-8")
m = re.search(r"kernCijfers\s*=\s*\{(.*?)\n\s*\};", html, re.S)
print("herop kern alt", (m.group(1)[:500] if m else "none"))
# try year markers
for y in ["2025", "2024"]:
    if f"{y}" in html and "winst" in html.lower():
        pass
ms = re.findall(r"winst:\s*\"([^\"]+)\"", html)
print("herop winsts", ms[:6])
ms = re.findall(r"bruto_marge:\s*\"([^\"]+)\"", html)
print("herop bruto", ms[:6])
ms = re.findall(r"omzet:\s*\"([^\"]*)\"", html)
print("herop omzet", ms[:6])
ms = re.findall(r"eigen_vermogen:\s*\"([^\"]+)\"", html)
print("herop eq", ms[:6])
