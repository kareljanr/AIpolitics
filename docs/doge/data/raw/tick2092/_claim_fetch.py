# -*- coding: utf-8 -*-
import csv
import re
import urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
RAW = Path("docs/doge/data/raw/tick2092")
RAW.mkdir(parents=True, exist_ok=True)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

path = Path("docs/doge/data/research_queue.csv")
with path.open(encoding="utf-8-sig", newline="") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)
for row in rows:
    if row["task_id"] == "rq_2092":
        st = (row.get("status") or "").lower()
        if st not in ("open", "in_progress"):
            raise SystemExit(f"RACE status={row.get('status')}")
        row["status"] = "in_progress"
        row["updated_utc"] = "2026-08-25T04:05:00Z"
        row["notes"] = "CLAIM tick2092 probing AGB/FARO/AIESH/REW then Lidwina"
with path.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("claimed rq_2092")

with open("docs/doge/data/entities.csv", encoding="utf-8-sig", newline="") as f:
    for r in csv.DictReader(f):
        if "lidwina" in str(r).lower() or "0407.601.720" in str(r) or "0407601720" in str(r):
            print("ENT HIT", r.get("entity_id"))
            raise SystemExit("already mined")


def fetch(name, url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "nl,en;q=0.8"})
    with urllib.request.urlopen(req, timeout=45) as resp:
        data = resp.read()
        print("OK", name, len(data), resp.geturl())
    text = data.decode("utf-8", "replace")
    text = re.sub(r"pk\.[A-Za-z0-9._\-]+", "pk.REDACTED", text)
    text = re.sub(r"sk\.[A-Za-z0-9._\-]+", "sk.REDACTED", text)
    (RAW / name).write_text(text, encoding="utf-8")
    return text


for name, url in [
    ("faro_nl.html", "https://www.companyweb.be/nl/0893863017/faro-vlaams-steunpunt-voor-cultureel-erfgoed"),
    ("aiesh_nl.html", "https://www.companyweb.be/nl/0201712587/aiesh"),
    ("rew_nl.html", "https://www.companyweb.be/nl/0644638937/rew"),
    ("lidwina_nl.html", "https://www.companyweb.be/nl/0407601720/lidwina-vzw"),
    ("lidwina_en.html", "https://www.companyweb.be/en/0407601720/lidwina-vzw"),
    ("lidwina_fr.html", "https://www.companyweb.be/fr/0407601720/lidwina-vzw"),
    ("kbo_lidwina.html", "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0407601720"),
]:
    try:
        t = fetch(name, url)
        ye = re.search(r"kernCijfers\s*=\s*\{\s*(20\d\d)\s*:", t)
        if ye:
            print(" ", name, "YE", ye.group(1))
    except Exception as e:
        print("FAIL", name, e)

t = (RAW / "lidwina_nl.html").read_text(encoding="utf-8", errors="replace")
print("TITLE", re.search(r"<title>([^<]+)</title>", t).group(1)[:140])
for ym in list(
    re.finditer(
        r"(20\d\d)\s*:\s*\{\s*winst:\s*\"([^\"]+)\",\s*eigen_vermogen:\s*\"([^\"]+)\",\s*bruto_marge:\s*\"([^\"]+)\",\s*omzet:\s*\"([^\"]+)\"",
        t,
    )
)[:3]:
    print("Y", ym.group(1), "winst", ym.group(2), "equity", ym.group(3), "bruto", ym.group(4), "omzet", ym.group(5))
print("FILED", re.search(r"neergelegd op ([0-9\-]+)", t).group(0))
print("FTE", re.search(r'amountOfEmployees\s*=\s*"([^"]+)"', t).group(1))
print("spans", re.findall(r"<span>([\d.,]+)</span>", t)[:6])

kbo = (RAW / "kbo_lidwina.html").read_text(encoding="utf-8", errors="replace")
idx = kbo.find("Adres van de zetel")
print("ADDR", re.sub(r"<[^>]+>", " ", kbo[idx : idx + 400]))
for pat in [
    r"pageactief\">([^<]+)",
    r"Vereniging zonder winstoogmerk",
    r"vestigingseenheden \(VE\):.*?<strong>([^<]+)",
    r"88\.\d+|87\.\d+|86\.\d+",
    r"aanbested",
    r"Mol|2400|Postelarenweg",
]:
    m = re.search(pat, kbo, re.I | re.S)
    if m:
        print("KBO", re.sub(r"\s+", " ", m.group(0))[:140])

for name, url in [
    ("lidwina_site.html", "https://www.lidwina.be/"),
    ("lidwina_site2.html", "https://lidwina.be/"),
    ("lidwina_contact.html", "https://www.lidwina.be/contact"),
]:
    try:
        text = fetch(name, url)
        emails = sorted(set(re.findall(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}", text)))
        emails = [
            e
            for e in emails
            if not any(x in e.lower() for x in ("sentry", "wix", "example", "cloudflare", "redacted"))
        ]
        print("SITE", name, emails[:8])
    except Exception as e:
        print("FAIL", name, e)
