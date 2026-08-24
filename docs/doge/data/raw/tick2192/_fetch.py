import os
import re
import urllib.request
import html as H

ua = {"User-Agent": "Mozilla/5.0"}
out = "docs/doge/data/raw/tick2192"
os.makedirs(out, exist_ok=True)

used = (
    open("docs/doge/data/entities.csv", encoding="utf-8").read()
    + open("docs/doge/data/commitments.csv", encoding="utf-8").read()
).replace(".", "")

d = "0407597958"
assert d not in used, "Mivas already used"
print("FREE mivas", d)

urls = {
    "en": f"https://www.companyweb.be/en/{d}/mivas",
    "nl": f"https://www.companyweb.be/nl/{d}/mivas",
    "fr": f"https://www.companyweb.be/fr/{d}/mivas",
    "kbo": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={d}",
    "faro_en": "https://www.companyweb.be/en/0893863017/faro",
}
for key, url in urls.items():
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, timeout=25) as r:
            html = r.read().decode("utf-8", "replace")
            final = r.geturl()
        open(os.path.join(out, f"{key}.html"), "w", encoding="utf-8").write(html)
        print(key, "OK", len(html), final)
    except Exception as e:
        print(key, type(e).__name__, e)

for sname, surl in [
    ("site", "https://www.mivas.be/"),
    ("site2", "https://mivas.be/"),
    ("contact", "https://www.mivas.be/contact"),
]:
    try:
        req = urllib.request.Request(surl, headers=ua)
        with urllib.request.urlopen(req, timeout=20) as r:
            html = r.read().decode("utf-8", "replace")
            final = r.geturl()
        open(os.path.join(out, f"{sname}.html"), "w", encoding="utf-8").write(html)
        emails = sorted(
            e
            for e in set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", html))
            if "sentry" not in e and "voorbeeld" not in e
        )
        print(sname, "OK", emails[:8], final)
    except Exception as e:
        print(sname, type(e).__name__, e)

faro = open(os.path.join(out, "faro_en.html"), encoding="utf-8").read()
ft = re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", faro)))
ym = re.search(r"Last balance sheet year (20\d\d)", ft)
print("FARO year", ym.group(1) if ym else "?")

html = open(os.path.join(out, "en.html"), encoding="utf-8").read()
for y in (2025, 2024, 2023, 2022):
    m = re.search(
        rf'{y}\s*:\s*\{{\s*winst:\s*"([^"]+)"\s*,\s*eigen_vermogen:\s*"([^"]+)"\s*,\s*bruto_marge:\s*"([^"]+)"\s*,\s*omzet:\s*"([^"]+)"',
        html,
        re.S,
    )
    print("YEAR", y, m.groups() if m else None)

text = re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", html)))
for key in ["Employees", "Profit/Loss", "Turnover", "Equity", "Gross margin", "filed on", "Last balance"]:
    i = text.lower().find(key.lower())
    if i >= 0:
        print("CTX", key, ":", text[max(0, i - 10) : i + 170])

kbo = open(os.path.join(out, "kbo.html"), encoding="utf-8").read()
kt = re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", kbo)))
for key in [
    "Status",
    "Rechtsvorm",
    "Vereniging zonder",
    "Adres van de zetel",
    "Aantal vestigingseenheden",
    "88.993",
    "0407.597.958",
    "Naam:",
]:
    j = kt.lower().find(key.lower())
    print("KBO", key, ":", kt[j : j + 220] if j >= 0 else "MISS")
