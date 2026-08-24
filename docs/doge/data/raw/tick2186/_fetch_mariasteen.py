import os
import re
import urllib.request
import html as H

ua = {"User-Agent": "Mozilla/5.0"}
out = "docs/doge/data/raw/tick2186"
os.makedirs(out, exist_ok=True)
d = "0407079207"

urls = {
    "en": f"https://www.companyweb.be/en/{d}/mariasteen",
    "nl": f"https://www.companyweb.be/nl/{d}/mariasteen",
    "fr": f"https://www.companyweb.be/fr/{d}/mariasteen",
    "kbo": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={d}",
    "site": "https://www.mariasteen.be/",
    "contact": "https://www.mariasteen.be/contact",
}

for name, url in urls.items():
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, timeout=25) as r:
            html = r.read().decode("utf-8", "replace")
            final = r.geturl()
        open(os.path.join(out, f"mariasteen_{name}.html"), "w", encoding="utf-8").write(html)
        emails = sorted(set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", html)))
        print(name, "OK", len(html), "emails", emails[:8], "final", final)
    except Exception as e:
        print(name, type(e).__name__, e)

# parse all years from EN
html = open(os.path.join(out, "mariasteen_en.html"), encoding="utf-8").read()
for y in (2025, 2024, 2023, 2022):
    m = re.search(
        rf'{y}\s*:\s*\{{\s*winst:\s*"([^"]+)"\s*,\s*eigen_vermogen:\s*"([^"]+)"\s*,\s*bruto_marge:\s*"([^"]+)"\s*,\s*omzet:\s*"([^"]+)"',
        html,
        re.S,
    )
    print("YEAR", y, m.groups() if m else None)

# FTE series from table text
text = H.unescape(re.sub(r"<[^>]+>", " ", html))
text = re.sub(r"\s+", " ", text)
for key in [
    "Employees",
    "877",
    "Profit/Loss",
    "Turnover",
    "Equity",
    "Gross margin",
    "filed on",
    "Last balance",
    "Non-profit",
    "association",
]:
    i = text.lower().find(key.lower())
    if i >= 0:
        print("CTX", key, ":", text[max(0, i - 20) : i + 160])

# KBO
kbo = open(os.path.join(out, "mariasteen_kbo.html"), encoding="utf-8").read()
kt = H.unescape(re.sub(r"<[^>]+>", " ", kbo))
kt = re.sub(r"\s+", " ", kt)
for key in [
    "Status",
    "Rechtsvorm",
    "Vereniging zonder",
    "Adres van de zetel",
    "Aantal vestigingseenheden",
    "88.993",
    "E-mail",
    "Bestuurder",
    "0407.079.207",
]:
    j = kt.lower().find(key.lower())
    print("KBO", key, ":", kt[j : j + 200] if j >= 0 else "MISS")
