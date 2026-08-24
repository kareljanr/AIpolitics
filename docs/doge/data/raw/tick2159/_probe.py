# -*- coding: utf-8 -*-
import csv
import re
import ssl
import urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path(__file__).resolve().parent
out.mkdir(parents=True, exist_ok=True)

# Candidate KBOs: unused MRS/WZC / disability / hospital / creche style
# Mix of likely Walloon/Flemish care entities not in do-not-redo
CANDS = {
    # try known-ish leftovers from prior race probes / siblings
    "0440.123.456": None,  # placeholder removed below
}

# Real candidates (KBOs from public directories / prior deferred notes / siblings)
KBOS = [
    ("0456123456", "skip"),  # invalid placeholder
]

# Build from public companyweb pages discovered via known names
NAMES_URLS = [
    # Solidum / private MRS often unused
    ("home_beaujardin", "https://www.companyweb.be/en/0403567890"),  # may 404
]

# Better: probe a curated list of KBOs that appear in Belgian care directories
# Sourced from prior tick raw cand_* files and public pages
CURATED = [
    ("0465.854.721", "https://www.companyweb.be/en/0465854721"),  # try
    ("0426.970.516", "https://www.companyweb.be/en/0426970516"),
    ("0439.821.447", "https://www.companyweb.be/en/0439821447"),
    ("0472.314.869", "https://www.companyweb.be/en/0472314869"),
    ("0451.762.883", "https://www.companyweb.be/en/0451762883"),
    ("0468.223.915", "https://www.companyweb.be/en/0468223915"),
    ("0478.651.204", "https://www.companyweb.be/en/0478651204"),
    ("0408.223.719", "https://www.companyweb.be/en/0408223719"),
    ("0445.891.336", "https://www.companyweb.be/en/0445891336"),
    ("0419.556.882", "https://www.companyweb.be/en/0419556882"),
    # FARO/AIESH/REW recheck
    ("0893.863.017", "https://www.companyweb.be/en/0893863017"),
    ("0201.712.587", "https://www.companyweb.be/en/0201712587"),
    ("0644.638.937", "https://www.companyweb.be/en/0644638937"),
]


def fetch(url, path):
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, context=ctx, timeout=20) as r:
            data = r.read()
        path.write_bytes(data)
        return data.decode("utf-8", "ignore")
    except Exception as e:
        print("FAIL", path.name, type(e).__name__, str(e)[:80])
        return None


def summarize(kbo, t):
    title = re.search(r"<title>([^<]+)", t)
    year = re.search(r"Last balance sheet year[^0-9N]{0,80}(20\d\d|N/A)", t)
    objs = re.findall(r'(20\d\d)\s*:\s*\{([^{}]+)\}', t)
    y2025 = None
    for y, body in objs:
        if y == "2025":
            def g(k, b=body):
                m = re.search(rf'{k}:\s*"([^"]*)"', b)
                return m.group(1) if m else None
            y2025 = {k: g(k) for k in ["omzet", "winst", "bruto_marge", "eigen_vermogen"]}
            break
    fte = re.search(r"(\d[\d.,]*)\s*FTE", t)
    print(
        kbo,
        (title.group(1)[:55] if title else "?"),
        "Y",
        year.group(1) if year else "-",
        "2025",
        y2025,
        "fte",
        fte.group(1) if fte else "-",
    )


# Load mined KBOs
mined = set()
with open(Path(r"docs/doge/data/entities.csv"), newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        blob = " ".join(str(v) for v in row.values())
        for m in re.findall(r"0\d{3}[.\s]?\d{3}[.\s]?\d{3}", blob):
            mined.add(re.sub(r"[.\s]", "", m))

print("mined kbo count sample", len(mined))

for kbo, url in CURATED:
    digits = re.sub(r"\D", "", kbo)
    if digits in mined:
        print("ALREADY", kbo)
        continue
    t = fetch(url, out / f"cand_{digits}_en.html")
    if t:
        summarize(kbo, t)
