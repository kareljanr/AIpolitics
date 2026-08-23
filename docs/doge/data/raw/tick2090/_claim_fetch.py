# -*- coding: utf-8 -*-
"""Claim rq_2090 and fetch Familiezorg WV YE2025 + stall checks."""
import csv
import re
import urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
RAW = Path("docs/doge/data/raw/tick2090")
RAW.mkdir(parents=True, exist_ok=True)
UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)
UTC = "2026-08-25T03:35:00Z"
KBO = "0405112085"

# --- claim ---
path = Path("docs/doge/data/research_queue.csv")
with path.open(encoding="utf-8-sig", newline="") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)
claimed = False
for row in rows:
    if row["task_id"] == "rq_2090":
        st = (row.get("status") or "").lower()
        if st not in ("open", "in_progress"):
            raise SystemExit(f"RACE status={row.get('status')}")
        row["status"] = "in_progress"
        row["updated_utc"] = UTC
        row["notes"] = "CLAIM tick2090 EVERY-10 + Familiezorg WV after FARO/AIESH/REW YE2024 stall"
        claimed = True
if not claimed:
    raise SystemExit("rq_2090 missing")
with path.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("claimed rq_2090")

# unused check
with open("docs/doge/data/entities.csv", encoding="utf-8-sig", newline="") as f:
    for r in csv.DictReader(f):
        blob = " ".join(str(v).lower() for v in r.values())
        if "familiezorg" in blob and ("west" in blob or "0405.112.085" in blob or KBO in blob):
            print("ENT HIT", r.get("entity_id"))
            raise SystemExit("already mined")
print("entities: unused OK")


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


# stall confirm
for name, url in [
    ("faro_nl.html", "https://www.companyweb.be/nl/0893863017/faro-vlaams-steunpunt-voor-cultureel-erfgoed"),
    ("aiesh_nl.html", "https://www.companyweb.be/nl/0201712587/aiesh"),
    ("rew_nl.html", "https://www.companyweb.be/nl/0644638937/rew"),
]:
    try:
        t = fetch(name, url)
        ye = re.search(r"kernCijfers\s*=\s*\{\s*(20\d\d)\s*:", t)
        print(" ", name, "YE", ye.group(1) if ye else "?")
    except Exception as e:
        print("FAIL", name, e)

for name, url in [
    ("fz_nl.html", f"https://www.companyweb.be/nl/{KBO}/familiezorg-west-vlaanderen"),
    ("fz_en.html", f"https://www.companyweb.be/en/{KBO}/familiezorg-west-vlaanderen"),
    ("fz_fr.html", f"https://www.companyweb.be/fr/{KBO}/familiezorg-west-vlaanderen"),
    ("kbo_fz.html", f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={KBO}"),
]:
    t = fetch(name, url)
    if name.startswith("fz_"):
        ye = re.search(r"kernCijfers\s*=\s*\{\s*(20\d\d)\s*:", t)
        print(" ", name, "YE", ye.group(1) if ye else "?")

t = (RAW / "fz_nl.html").read_text(encoding="utf-8", errors="replace")
print("TITLE", re.search(r"<title>([^<]+)</title>", t).group(1)[:140])
for ym in list(
    re.finditer(
        r'(20\d\d)\s*:\s*\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)"',
        t,
    )
)[:4]:
    print("Y", ym.group(1), "winst", ym.group(2), "equity", ym.group(3), "bruto", ym.group(4), "omzet", ym.group(5))
filed = re.search(r"neergelegd op ([0-9.\-]+)", t)
print("FILED", filed.group(0) if filed else "?")
fte = re.search(r'amountOfEmployees\s*=\s*"([^"]+)"', t)
print("FTE", fte.group(1) if fte else "?")
# also EN FTE / employees spans
ten = (RAW / "fz_en.html").read_text(encoding="utf-8", errors="replace")
for ym in list(
    re.finditer(
        r'(20\d\d)\s*:\s*\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)"',
        ten,
    )
)[:2]:
    print("EN Y", ym.group(1), "winst", ym.group(2), "equity", ym.group(3), "bruto", ym.group(4), "omzet", ym.group(5))
# employee history often in span list near Employees
emps = re.findall(r"Employees[^<]{0,40}|werknemers[^<]{0,40}|([0-9]+[.,][0-9])\s*(?:FTE|</)", ten, re.I)
print("EMP hints", emps[:10])
# try amountOfEmployees on EN
fte_en = re.search(r'amountOfEmployees\s*=\s*"([^"]+)"', ten)
print("FTE_EN", fte_en.group(1) if fte_en else "?")
# look for employee year series in JS
emp_js = re.search(r"amountOfEmployeesPerYear\s*=\s*(\[[^\]]+\])", ten)
print("FTE_YEARS", emp_js.group(1) if emp_js else "?")
emp_js2 = re.search(r"employees\s*[:=]\s*(\[[^\]]{0,200}\])", ten, re.I)
print("EMP2", emp_js2.group(1) if emp_js2 else "?")

kbo = (RAW / "kbo_fz.html").read_text(encoding="utf-8", errors="replace")
idx = kbo.find("Adres van de zetel")
print("ADDR", re.sub(r"<[^>]+>", " ", kbo[idx : idx + 500])[:300])
for pat in [
    r"pageactief\">([^<]+)",
    r"Vereniging zonder winstoogmerk",
    r"vestigingseenheden \(VE\):.*?<strong>([^<]+)",
    r"88\.\d+|87\.\d+|86\.\d+|881\d+",
    r"aanbested",
    r"Brugge|8000",
    r"Familiezorg",
]:
    m = re.search(pat, kbo, re.I | re.S)
    if m:
        print("KBO", re.sub(r"\s+", " ", m.group(0))[:160])

for name, url in [
    ("fz_site.html", "https://www.familiezorg.be/"),
    ("fz_site2.html", "https://www.familiezorg.be/west-vlaanderen"),
    ("fz_contact.html", "https://www.familiezorg.be/contact"),
]:
    try:
        text = fetch(name, url)
        emails = sorted(set(re.findall(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}", text)))
        emails = [
            e
            for e in emails
            if not any(x in e.lower() for x in ("sentry", "wix", "example", "cloudflare", "redacted", "schema"))
        ]
        print("SITE", name, emails[:12])
    except Exception as e:
        print("FAIL", name, e)
