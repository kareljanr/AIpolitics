import os
import re
import urllib.request
import html as H

ua = {"User-Agent": "Mozilla/5.0"}
out = "docs/doge/data/raw/tick2193"
os.makedirs(out, exist_ok=True)

d = "0465707391"
assert d not in (
    open("docs/doge/data/entities.csv", encoding="utf-8").read()
    + open("docs/doge/data/commitments.csv", encoding="utf-8").read()
).replace(".", ""), "already used"

urls = {
    "en": f"https://www.companyweb.be/en/{d}/sociale-werkplaatsen-web",
    "nl": f"https://www.companyweb.be/nl/{d}/sociale-werkplaatsen-web",
    "fr": f"https://www.companyweb.be/fr/{d}/sociale-werkplaatsen-web",
    "kbo": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={d}",
    "rew_en": "https://www.companyweb.be/en/0644638937/reseau-d-energies-de-wavre",
    "rew_nl": "https://www.companyweb.be/nl/0644638937/reseau-d-energies-de-wavre",
    "bwz_fr": "https://www.companyweb.be/fr/0407657148/beschermde-werkplaats-zottegem",
    "schakel_fr": "https://www.companyweb.be/fr/0419461652/de-schakel",
}


def get(key, url):
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, timeout=25) as r:
            html = r.read().decode("utf-8", "replace")
            final = r.geturl()
        open(os.path.join(out, f"{key}.html"), "w", encoding="utf-8").write(html)
        text = re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", html)))
        ym = (
            re.search(r"Last balance sheet year (20\d\d)", text)
            or re.search(r"Laatste balansjaar\s*(20\d\d)", text)
            or re.search(r"Dernier bilan\s*(20\d\d)", text)
        )
        print(key, "OK", len(html), "year", ym.group(1) if ym else "?", final[:100])
        for y in (2025, 2024, 2023):
            m = re.search(
                rf'{y}\s*:\s*\{{\s*winst:\s*"([^"]+)"\s*,\s*eigen_vermogen:\s*"([^"]+)"\s*,\s*bruto_marge:\s*"([^"]+)"\s*,\s*omzet:\s*"([^"]+)"',
                html,
                re.S,
            )
            if m:
                print(" ", y, m.groups())
        for label in ["filed on", "Employees", "Turnover", "Profit/Loss", "Equity", "Gross margin", "Last balance"]:
            i = text.lower().find(label.lower())
            if i >= 0:
                print("  CTX", label, ":", text[max(0, i - 5) : i + 140])
        return html, text
    except Exception as e:
        print(key, type(e).__name__, e)
        return None, None


for k, u in urls.items():
    get(k, u)

for sname, surl in [
    ("site", "https://www.sw-web.be/"),
    ("site2", "https://sw-web.be/"),
    ("contact", "https://www.sw-web.be/contact"),
    ("site3", "https://www.sociale-werkplaatsen-web.be/"),
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
            if "sentry" not in e and "voorbeeld" not in e and "wixpress" not in e
        )
        print(sname, "OK", emails[:10], final)
    except Exception as e:
        print(sname, type(e).__name__, e)

kbo = open(os.path.join(out, "kbo.html"), encoding="utf-8").read()
kt = re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", kbo)))
for key in [
    "Status",
    "Rechtsvorm",
    "Vereniging zonder",
    "Adres van de zetel",
    "Aantal vestigingseenheden",
    "88.993",
    "0465.707.391",
    "Naam:",
    "E-mail",
    "Webadres",
    "Afkorting",
]:
    j = kt.lower().find(key.lower())
    print("KBO", key, ":", kt[j : j + 240] if j >= 0 else "MISS")
