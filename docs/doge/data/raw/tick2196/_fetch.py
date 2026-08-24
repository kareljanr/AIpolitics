# tick2196: probe FARO/AIESH/REW; take BWZ Zottegem if stalls; fetch CW+KBO
import os
import re
import urllib.request
import html as H
from pathlib import Path

ua = {"User-Agent": "Mozilla/5.0"}
out = Path("docs/doge/data/raw/tick2196")
out.mkdir(parents=True, exist_ok=True)


def num(s):
    s = (s or "").strip().replace(" ", "").replace("\xa0", "")
    if s in ("", "-"):
        return None
    if re.search(r",\d{2}$", s) and "." in s:
        s = s.replace(".", "").replace(",", ".")
    elif s.count(",") > 1:
        s = s.replace(",", "")
    elif s.count(".") > 1:
        s = s.replace(".", "")
    elif "," in s and "." not in s:
        parts = s.split(",")
        s = (
            parts[0] + "." + parts[1]
            if len(parts) == 2 and len(parts[1]) == 2
            else s.replace(",", "")
        )
    return float(s)


def fetch(url, dest=None):
    req = urllib.request.Request(url, headers=ua)
    with urllib.request.urlopen(req, timeout=30) as r:
        html = r.read().decode("utf-8", "replace")
        final = r.geturl()
    if dest:
        Path(dest).write_text(html, encoding="utf-8")
    return html, final


def year_of(html):
    text = re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", html)))
    ym = re.search(r"Last balance sheet year (20\d\d)", text)
    return ym.group(1) if ym else "?"


def kern(html, y):
    m = re.search(
        rf'{y}\s*:\s*\{{[^}}]*?winst:\s*"([^"]+)"\s*,\s*eigen_vermogen:\s*"([^"]+)"\s*,\s*bruto_marge:\s*"([^"]+)"\s*,\s*omzet:\s*"([^"]+)"',
        html,
        re.S,
    )
    if not m:
        return None
    return {
        "pnl": num(m.group(1)),
        "equity": num(m.group(2)),
        "bruto": num(m.group(3)),
        "omzet": num(m.group(4)),
    }


def fte_of(html):
    m = re.search(r'amountOfEmployees\s*=\s*"([^"]+)"', html)
    return m.group(1) if m else None


def filing_of(html):
    text = re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", html)))
    for pat in [
        r"Date of filing[^0-9]*(\d{2}[./-]\d{2}[./-]\d{4})",
        r"Filing date[^0-9]*(\d{2}[./-]\d{2}[./-]\d{4})",
        r"neerlegging[^0-9]*(\d{2}[./-]\d{2}[./-]\d{4})",
        r"filed on[^0-9]*(\d{2}[./-]\d{2}[./-]\d{4})",
        r"Datum neerlegging[^0-9]*(\d{2}[./-]\d{2}[./-]\d{4})",
    ]:
        mm = re.search(pat, text, re.I)
        if mm:
            return mm.group(1)
    return None


print("=== preferred stalls ===")
for name, kbo in [
    ("faro", "0893863017"),
    ("aiesh", "0200724564"),
    ("rew", "0644638937"),
]:
    d = re.sub(r"\D", "", kbo)
    try:
        html, final = fetch(f"https://www.companyweb.be/en/{d}/")
        print(name, "year", year_of(html), "slug", final.rstrip("/").split("/")[-1], "k25", bool(kern(html, "2025")))
    except Exception as e:
        print(name, "ERR", type(e).__name__, str(e)[:80])

# BWZ Zottegem — primary unit
KBO = "0407657148"
SLUG = "beschermde-werkplaats-zottegem"
print("=== BWZ fetch ===")
for lang, path in [
    ("en", out / "en.html"),
    ("nl", out / "nl.html"),
    ("fr", out / "fr.html"),
]:
    html, final = fetch(f"https://www.companyweb.be/{lang}/{KBO}/{SLUG}", path)
    print(lang, "year", year_of(html), "fte", fte_of(html), "filing", filing_of(html))
    for y in ("2025", "2024"):
        k = kern(html, y)
        if k:
            print(" ", y, k)

# KBO
kbo_html, _ = fetch(
    f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={KBO}",
    out / "kbo.html",
)
text = re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", kbo_html)))
print("KBO snippet:", text[text.find("Status") : text.find("Status") + 200] if "Status" in text else text[:300])

# site / contact
for url, dest in [
    ("https://www.bwz.be/", out / "site.html"),
    ("https://www.bwz.be/contact", out / "contact.html"),
]:
    try:
        fetch(url, dest)
        print("OK", url)
    except Exception as e:
        print("site ERR", url, type(e).__name__, str(e)[:60])

# De Schakel probe as backup note
try:
    html, final = fetch("https://www.companyweb.be/en/0419461652/")
    k = kern(html, "2025")
    print("de_schakel year", year_of(html), "k25", k)
except Exception as e:
    print("de_schakel ERR", e)
