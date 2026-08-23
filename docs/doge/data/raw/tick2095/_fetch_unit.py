# -*- coding: utf-8 -*-
"""Claim rq_2095 + fetch Begralim YE2025 + stall confirm FARO/AIESH/REW."""
import csv
import re
import urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
RAW = Path(__file__).resolve().parent
ROOT = RAW.parents[1]
UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)
UTC = "2026-08-25T04:50:00Z"
KBO = "0428374764"
SLUG = "bejaardenzorg-grauwzusters-limburg"


def fetch(name: str, url: str) -> str:
    req = urllib.request.Request(
        url, headers={"User-Agent": UA, "Accept-Language": "nl-BE,nl;q=0.9,en;q=0.8"}
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = resp.read()
        print("OK", name, len(data), resp.geturl())
    text = data.decode("utf-8", "replace")
    text = re.sub(r"pk\.[A-Za-z0-9._\-]+", "pk.REDACTED", text)
    text = re.sub(r"sk\.[A-Za-z0-9._\-]+", "sk.REDACTED", text)
    (RAW / name).write_text(text, encoding="utf-8")
    return text


# claim
path = ROOT / "research_queue.csv"
with path.open(encoding="utf-8-sig", newline="") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)
claimed = False
for row in rows:
    if row["task_id"] == "rq_2095":
        st = (row.get("status") or "").lower()
        if st not in ("open", "in_progress"):
            raise SystemExit(f"RACE status={row.get('status')}")
        row["status"] = "in_progress"
        row["updated_utc"] = UTC
        row["notes"] = (
            "CLAIM tick2095 Begralim after FARO/AIESH/REW YE2024 stall; "
            "unused WZC Grauwzusters Limburg YE2025"
        )
        claimed = True
if not claimed:
    raise SystemExit("rq_2095 missing")
with path.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("claimed rq_2095")

# unused check
with open(ROOT / "entities.csv", encoding="utf-8-sig", newline="") as f:
    for r in csv.DictReader(f):
        blob = " ".join(str(v).lower() for v in r.values())
        if any(
            x in blob
            for x in (
                "begralim",
                "grauwzusters",
                "0428.374.764",
                "0428374764",
            )
        ):
            print("ENT HIT", r.get("entity_id"))
            raise SystemExit("already mined")
print("entities: unused OK")

# stall + unit
PAGES = [
    ("faro_nl.html", "https://www.companyweb.be/nl/0893863017/faro-vlaams-steunpunt-voor-cultureel-erfgoed"),
    ("aiesh_nl.html", "https://www.companyweb.be/nl/0201712587/a-i-e-s-h"),
    ("rew_nl.html", "https://www.companyweb.be/nl/0644638937/rew"),
    ("begralim_nl.html", f"https://www.companyweb.be/nl/{KBO}/{SLUG}"),
    ("begralim_en.html", f"https://www.companyweb.be/en/{KBO}/{SLUG}"),
    ("begralim_fr.html", f"https://www.companyweb.be/fr/{KBO}/{SLUG}"),
    (
        "kbo_begralim.html",
        f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={KBO}",
    ),
]

for name, url in PAGES:
    try:
        t = fetch(name, url)
        ye = re.search(r"kernCijfers\s*=\s*\{\s*(20\d\d)\s*:", t)
        first = re.search(
            r'(20\d\d)\s*:\s*\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",'
            r'\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)"',
            t,
        )
        # also capture YoY from second year block if present
        years = list(
            re.finditer(
                r'(20\d\d)\s*:\s*\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",'
                r'\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)"',
                t,
            )
        )
        fte = re.search(r'amountOfEmployees\s*=\s*"([^"]+)"', t)
        filed = re.search(r"neergelegd op ([0-9.\-]+)", t, re.I)
        title = re.search(r"<title>([^<]+)</title>", t)
        print(
            "SUM",
            name,
            "YE",
            ye.group(1) if ye else "?",
            "filed",
            filed.group(1) if filed else "?",
            "fte",
            fte.group(1) if fte else "?",
        )
        for m in years[:2]:
            print(
                " ",
                m.group(1),
                "pnl",
                m.group(2),
                "eq",
                m.group(3),
                "bruto",
                m.group(4),
                "omzet",
                m.group(5),
            )
        if title:
            print(" ", title.group(1)[:100])
        if "kbo" in name:
            for pat in [
                r"Actief",
                r"Vereniging zonder winstoogmerk",
                r"aanbestedende overheid",
                r"Nacebel[^<]{0,120}",
                r"[@][A-Za-z0-9._\-]+",
                r"Hasselt|Limburg",
                r"vestigingseenheid|VE",
            ]:
                ms = re.findall(pat, t, re.I)
                if ms:
                    print(" ", pat[:40], ms[:6])
    except Exception as e:
        print("FAIL", name, type(e).__name__, str(e)[:150])
