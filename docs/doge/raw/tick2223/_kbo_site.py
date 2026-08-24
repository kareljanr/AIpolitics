import re
import ssl
import urllib.request
from pathlib import Path

CTX = ssl.create_default_context()
OUT = Path("docs/doge/raw/tick2223")

urls = {
    "kw_maasland_kbo": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0417701992",
    "kw_maasland_site": "https://www.dekringwinkel.be/maasland",
    "kw_maasland_contact": "https://www.dekringwinkel.be/maasland/contact",
}

for k, u in urls.items():
    try:
        req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=CTX, timeout=30) as r:
            html = r.read().decode("utf-8", "replace")
            final = r.geturl()
        (OUT / f"{k}.html").write_text(html, encoding="utf-8")
        print(k, "ok", len(html), final)
    except Exception as e:
        print(k, type(e).__name__, e)

html = (OUT / "kw_maasland_nl.html").read_text(encoding="utf-8")
m = re.search(r'amountOfEmployees\s*=\s*"([^"]+)"', html)
print("emp", m.group(1) if m else None)
# prior FTE if any table
for pat in [r"(\d+[.,]\d)\s*FTE", r"FTE.{0,40}?(\d+[.,]\d+)"]:
    print(pat, re.findall(pat, html)[:8])

om25, om24 = 3184457, 3018677
br25, br24 = 5753438, 5181229
pn25, pn24 = 227945, 302701
eq25, eq24 = 5956845, 5746500
print("omzet pct", round((om25 / om24 - 1) * 100, 2))
print("bruto pct", round((br25 / br24 - 1) * 100, 2))
print("pnl pct", round((pn25 / pn24 - 1) * 100, 2))
print("equity pct", round((eq25 / eq24 - 1) * 100, 2))
print("bruto/omzet", round(br25 / om25, 2))

emails = sorted(set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", html)))
print("cw emails", [e for e in emails if "sentry" not in e and "companyweb" not in e][:10])

kbo = (OUT / "kw_maasland_kbo.html").read_text(encoding="utf-8", errors="replace")
text = re.sub(r"<[^>]+>", " ", kbo)
text = re.sub(r"\s+", " ", text)
for pat in [
    r"Status:\s*(\w+)",
    r"Aantal vestigingseenheden \(VE\):\s*(\d+)",
    r"Adres van de zetel:.{0,120}",
    r"Begindatum:.{0,60}",
    r"Rechtsvorm:.{0,80}",
]:
    m = re.search(pat, text)
    if m:
        print(m.group(0)[:140])
for nace in re.findall(r"(?:88|47|87)\.\d{3}", text)[:8]:
    print("nace", nace)

for site_name in ["kw_maasland_site.html", "kw_maasland_contact.html"]:
    p = OUT / site_name
    if not p.exists():
        continue
    shtml = p.read_text(encoding="utf-8", errors="replace")
    semails = sorted(set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", shtml)))
    print(site_name, "emails", [e for e in semails if "example" not in e][:8])
    print(site_name, "title", (re.search(r"<title>([^<]+)", shtml) or type("", (), {"group": lambda *_: "?"})()).group(1)[:100])
