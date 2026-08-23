# ephemeral probe tick2072 — claim + stalls + unused WZC candidates
import csv
import re
import ssl
import sys
import urllib.request
from pathlib import Path

csv.field_size_limit(sys.maxsize)
ctx = ssl.create_default_context()
outdir = Path("docs/doge/data/raw/tick2072")
outdir.mkdir(parents=True, exist_ok=True)
UTC = "2026-08-24T23:05:00Z"


def load(path):
    with Path(path).open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
        for row in rows:
            for k in list(row):
                if k.startswith("\ufeff"):
                    row[k.lstrip("\ufeff")] = row.pop(k)
        return rows


def year_of(html):
    for lab in ["Last balance sheet year", "Laatste balansjaar", "Dernier bilan"]:
        i = html.find(lab)
        if i >= 0:
            m = re.search(r"font-medium[^>]*>\s*(\d{4}|N/A)", html[i : i + 220])
            if m:
                return m.group(1)
    return None


def parse_blocks(html):
    return re.findall(
        r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
        html,
    )


def fetch(name, url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, context=ctx, timeout=35) as resp:
        html = resp.read().decode("utf-8", "replace")
    (outdir / f"{name}_en.html").write_text(html, encoding="utf-8")
    emp = re.search(r'Employees\s*=\s*"([^"]+)"', html)
    filed = re.search(r"filed on ([0-9\-]+)", html, re.I)
    title = re.search(r"<title>([^<]+)", html)
    print(
        "FETCH",
        name,
        "Y",
        year_of(html),
        "emp",
        emp.group(1) if emp else None,
        "filed",
        filed.group(1) if filed else None,
        (title.group(1)[:55] if title else ""),
        "blocks",
        parse_blocks(html)[:2],
    )
    return html, year_of(html), parse_blocks(html)


qrows = load("docs/doge/data/research_queue.csv")
r = next(x for x in qrows if x.get("task_id") == "rq_2072")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))
if st == "open":
    fields = list(qrows[0].keys())
    r["status"] = "in_progress"
    r["updated_utc"] = UTC
    with open("docs/doge/data/research_queue.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(qrows)
    print("CLAIMED rq_2072")
else:
    print("ALREADY", st)

stalls = [
    ("agb_bornem", "https://www.companyweb.be/en/0877556624/autonoom-gemeentebedrijf-bornem"),
    ("faro", "https://www.companyweb.be/en/0893863017/faro-vlaams-steunpunt-voor-cultureel-erfgoed"),
    ("aiesh", "https://www.companyweb.be/en/0201712587/aiesh"),
    ("rew", "https://www.companyweb.be/en/0644638937/reseau-d-energies-de-wavre"),
]
for name, url in stalls:
    try:
        fetch(name, url)
    except Exception as e:
        print("FAIL", name, type(e).__name__, str(e)[:160])

# Candidate unused WZC / zorg / MSW — avoid already-mined names
candidates = [
    ("zonnige_ruste", "https://www.companyweb.be/en/0407591018"),  # guess may 404
    ("huis_perrekes", "https://www.companyweb.be/en/0411783981"),
    ("de_bijster", "https://www.companyweb.be/en/0415592495"),
    ("rusthuis_ten_bos", "https://www.companyweb.be/en/"),
]

# Search companyweb via known Flemish WZC KBOs from prior deferrals / common list
# Pull candidates from recent tick notes / google-ish list we know unused
more = [
    # Always Home skipped (Armonea). Try other public-ish WZC VZWs with YE2025
    ("ocmw_linked_skip", None),
]

ents = load("docs/doge/data/entities.csv")
ent_blob = " ".join(
    ((e.get("entity_id") or "") + " " + (e.get("name_nl") or "") + " " + (e.get("notes") or "")).lower()
    for e in ents
)

# Probe a shortlist of plausible unused WZC/zorg VZWs (KBOs from prior inventory scripts if present)
shortlist = [
    ("vzw_denolf", "https://www.companyweb.be/en/0404457905"),  # may be wrong
    ("wzc_de_witte_meren", "https://www.companyweb.be/en/"),  # already mined
]

# Read tick2070 inventory for deferred candidates
inv = Path("docs/doge/data/_tick2070_inventory.py")
if inv.exists():
    print("INV exists", inv.stat().st_size)

# Known deferred / unused from recent logs and probes in raw/
probe_urls = [
    ("always_home", "https://www.companyweb.be/en/0475190847"),  # Armonea path — skip if confirms
    ("zonnebloem", "https://www.companyweb.be/en/0407157828"),
    ("magnolia", "https://www.companyweb.be/en/0465490920"),
    ("loof", "https://www.companyweb.be/en/0473251302"),
    ("ortelius", "https://www.companyweb.be/en/0426626494"),
    ("zilverlinde", "https://www.companyweb.be/en/0430707647"),
    ("immanuela", "https://www.companyweb.be/en/0412277526"),
    ("bethanie", "https://www.companyweb.be/en/0406362158"),
    ("sint_anna_wz", "https://www.companyweb.be/en/0414817220"),
    ("de_wijk", "https://www.companyweb.be/en/0425794117"),
    ("huize_ter_linden", "https://www.companyweb.be/en/0407659157"),
    ("ooghe", "https://www.companyweb.be/en/0441662881"),
    ("mse_kortrijk", "https://www.companyweb.be/en/0405481039"),  # MSW?
    ("msw_cm", "https://www.companyweb.be/en/0404456241"),
]

print("--- probing shortlist ---")
for name, url in probe_urls:
    try:
        html, y, blocks = fetch(name, url)
        title = re.search(r"<title>([^<]+)", html)
        t = (title.group(1) if title else "").lower()
        mined = any(
            k in ent_blob
            for k in [
                name.replace("_", " "),
                re.sub(r"\D", "", url.split("/en/")[-1][:10]) if "/en/" in url else "xxx",
            ]
        )
        # also check KBO digits in entities
        kbo = re.search(r"/en/(\d{10})", url)
        kbo_hit = False
        if kbo:
            digits = kbo.group(1)
            dotted = f"{digits[:4]}.{digits[4:7]}.{digits[7:]}"
            kbo_hit = digits in ent_blob or dotted in ent_blob
        print("  mined?", mined or kbo_hit, "title", (title.group(1)[:70] if title else ""))
    except Exception as e:
        print("FAIL", name, type(e).__name__, str(e)[:120])
