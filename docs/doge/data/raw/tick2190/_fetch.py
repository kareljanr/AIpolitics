import os
import re
import urllib.request
import html as H
import csv

ua = {"User-Agent": "Mozilla/5.0"}
out = "docs/doge/data/raw/tick2190"
os.makedirs(out, exist_ok=True)

csv.field_size_limit(10**7)

# inventory counts
for fname in [
    "budgets.csv",
    "commitments.csv",
    "leaderboard.csv",
    "entities.csv",
    "sources.csv",
    "foi_queue.csv",
]:
    with open(f"docs/doge/data/{fname}", newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if fname == "foi_queue.csv":
        from collections import Counter

        c = Counter((r.get("status") or "").strip() for r in rows)
        print("foi", len(rows), dict(c))
    else:
        print(fname, len(rows))

used = (
    open("docs/doge/data/entities.csv", encoding="utf-8").read()
    + open("docs/doge/data/commitments.csv", encoding="utf-8").read()
).replace(".", "")

cands = [
    ("de_wroeter", "0433138454", "de-wroeter-maatwerkbedrijf"),
    ("demival", "0407409007", "demival-werkplaats-voor-aangepaste-arbeid-te-deinze"),
    ("mivas", "0407597958", "mivas"),
]

picked = None
for name, kbo, slug in cands:
    d = re.sub(r"\D", "", kbo)
    if d in used:
        print("USED", name)
        continue
    print("FREE", name, kbo)
    if picked is None:
        picked = (name, d, slug)
        break

if not picked:
    raise SystemExit("no free")

name, d, slug = picked
print("PICK", name, d)

urls = {
    "en": f"https://www.companyweb.be/en/{d}/{slug}",
    "nl": f"https://www.companyweb.be/nl/{d}/{slug}",
    "fr": f"https://www.companyweb.be/fr/{d}/{slug}",
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

# site for De Wroeter
for sname, surl in [
    ("site", "https://www.dewroeter.be/"),
    ("site2", "https://dewroeter.be/"),
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
    "0433.138.454",
    "Naam:",
]:
    j = kt.lower().find(key.lower())
    print("KBO", key, ":", kt[j : j + 220] if j >= 0 else "MISS")

# top10 recheck from leaderboard
with open("docs/doge/data/leaderboard.csv", newline="", encoding="utf-8") as f:
    lbs = list(csv.DictReader(f))


def pi(r):
    try:
        return float(r.get("priority_index") or 0)
    except Exception:
        return 0


# filter stocks / corrupt
STOCK_HINTS = (
    "snowball",
    "stock",
    "eoy2083",
    "metro3",
    "hedera",
    "debt stock",
    "principal",
    "safe loan",
)
scored = []
for r in lbs:
    p = pi(r)
    if p > 10:
        continue
    blob = ((r.get("name") or "") + " " + (r.get("notes") or "") + " " + (r.get("tco_notes") or "")).lower()
    if any(h in blob for h in STOCK_HINTS) and p < 9:
        # soft filter already-known stocks by id
        pass
    if (r.get("item_id") or "").startswith("lb_metro3") or "owv_snowball" in (r.get("item_id") or ""):
        continue
    scored.append(r)
scored.sort(key=lambda r: (-pi(r), -float(r.get("annual_cost_eur") or 0)))
print("TOP10 candidates:")
for i, r in enumerate(scored[:12], 1):
    print(i, r.get("item_id"), r.get("priority_index"), (r.get("name") or "")[:70], r.get("annual_cost_eur"))
