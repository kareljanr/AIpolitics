import os
import re
import urllib.request
import html as H

ua = {"User-Agent": "Mozilla/5.0"}
out = "docs/doge/data/raw/tick2187"
d = "0407656257"

urls = {
    "en": f"https://www.companyweb.be/en/{d}/mirto",
    "nl": f"https://www.companyweb.be/nl/{d}/mirto",
    "fr": f"https://www.companyweb.be/fr/{d}/mirto",
    "kbo": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={d}",
    "site": "https://www.mirto.be/",
    "site2": "https://mirto.be/",
}

for name, url in urls.items():
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, timeout=25) as r:
            html = r.read().decode("utf-8", "replace")
            final = r.geturl()
        open(os.path.join(out, f"mirto_{name}.html"), "w", encoding="utf-8").write(html)
        emails = sorted(set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", html)))
        print(name, "OK", len(html), "emails", [e for e in emails if "sentry" not in e][:8], "final", final)
    except Exception as e:
        print(name, type(e).__name__, e)

html = open(os.path.join(out, "mirto_en.html"), encoding="utf-8").read()
for y in (2025, 2024, 2023, 2022):
    m = re.search(
        rf'{y}\s*:\s*\{{\s*winst:\s*"([^"]+)"\s*,\s*eigen_vermogen:\s*"([^"]+)"\s*,\s*bruto_marge:\s*"([^"]+)"\s*,\s*omzet:\s*"([^"]+)"',
        html,
        re.S,
    )
    print("YEAR", y, m.groups() if m else None)

text = re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", html)))
for key in ["Employees", "Profit/Loss", "Turnover", "Equity", "Gross margin", "filed on", "Last balance", "317"]:
    i = text.lower().find(key.lower())
    if i >= 0:
        print("CTX", key, ":", text[max(0, i - 20) : i + 180])

kbo = open(os.path.join(out, "mirto_kbo.html"), encoding="utf-8").read()
kt = re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", kbo)))
for key in [
    "Status",
    "Rechtsvorm",
    "Vereniging zonder",
    "Adres van de zetel",
    "Aantal vestigingseenheden",
    "88.993",
    "0407.656.257",
    "Bestuurder",
]:
    j = kt.lower().find(key.lower())
    print("KBO", key, ":", kt[j : j + 220] if j >= 0 else "MISS")
