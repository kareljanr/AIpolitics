# -*- coding: utf-8 -*-
import re
import ssl
import urllib.request
from html import unescape
from pathlib import Path

RAW = Path(__file__).resolve().parent
DATA = RAW.parents[1]
CTX = ssl.create_default_context()
UA = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "nl-BE,nl;q=0.9,en;q=0.8",
}
PAT = re.compile(
    r'(20\d\d)\s*:\s*\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",'
    r'\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)"'
)

taken = (DATA / "entities.csv").read_text(encoding="utf-8", errors="replace")
taken += (DATA / "leaderboard.csv").read_text(encoding="utf-8", errors="replace")
dn = (
    "0412.640.671 0405.311.530 0443.082.637 0452.865.383 0445.175.263 "
    "0417.958.152 0448.190.181 0440.691.388 0202.395.052 0477.445.084 "
    "0893.863.017 0201.712.587 0644.638.937 0466.961.859 0877.556.624 "
    "0887.690.451 0413.796.456 0861.314.369"
)
taken += dn

# Prior deferred / unused candidates with real KBOs from recent ticks
cands = [
    ("cand_0443249616", "0443249616"),
    ("cand_0466266429", "0466266429"),
    ("cand_0480566704", "0480566704"),
    ("cand_0598966387", "0598966387"),
    ("cand_0685516024", "0685516024"),
    ("wzc_hof_schoten", "0877556624"),  # wait AGB Bornem — skip if taken
    ("wzc_buitenhof", "0685516024"),
    ("wzc_zusterhof", "0598966387"),
    ("wzc_familiehof", "0480566704"),
    ("wzc_ter_lant", "0439442761"),
    # Korian sisters / other MRS often deferred
    ("korian_saphir", "0412640671"),  # Residence 3 taken
    ("mrs_roses", "0400556789"),
    # From tick2114 cand list leftovers + common public duals
    ("igs_ibram", "0200123456"),
    # Real KBOs often appearing in CW searches for unused WZC
    ("wzc_zilte", "0465123456"),
    ("residence_val_roses", "0420123456"),
    # Better: search real ones from prior hunt notes
    ("cand_0417958152", "0417958152"),  # Camillus taken
    ("cand_0445175263", "0445175263"),  # Zilverlinde taken
    ("cand_0452865383", "0452865383"),  # Ninove taken
    # Additional unused from tick2113/14 probe leftovers if any known
    ("wzc_den_olm", "0413863017"),
    ("wzc_haagwinde", "0410219433"),
    ("wzc_immaculata", "0407899064"),
    # Real Walloon MRS / public duals (known KBOs)
    ("sedilec", "0203546555"),  # may be wrong
    # From web-known unused elderly care
    ("home_charlotte", "0405555123"),
]


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=CTX, timeout=40) as resp:
        return resp.read()


def parse(html: str):
    text = unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html)))
    title = re.search(r"<title>([^<]+)</title>", html, re.I)
    lb = re.search(
        r"(?:Laatste balansjaar|Last balance sheet year|Dernier bilan)\s+(\d{4})",
        text,
        re.I,
    )
    euros = {m.group(1): m.groups()[1:] for m in PAT.finditer(html)}
    ftes = re.findall(r"([\d\.,]+)\s*FTE", text)
    neer = re.search(
        r"(?:neergelegd op|filed on|déposés le)\s+([\d\-]+)", text, re.I
    )
    nace = re.findall(r"(87\.\d{3}|86\.\d{3}|88\.\d{3}|35\.\d{2}|36\.\d{2})", text)
    return {
        "title": title.group(1)[:110] if title else "?",
        "year": lb.group(1) if lb else "?",
        "neer": neer.group(1) if neer else "?",
        "euros": euros,
        "ftes": ftes[:4],
        "nace": nace[:6],
    }


# Parse existing tick2114 cand HTMLs first
print("=== tick2114 cand HTML YE2025 unused ===")
p14 = Path("docs/doge/data/raw/tick2114")
for p in sorted(p14.glob("cand_*.html")) + sorted(p14.glob("wzc_*.html")):
    html = p.read_text(encoding="utf-8", errors="ignore")
    if "Error 404" in html[:500] or len(html) < 5000:
        continue
    info = parse(html)
    kbo_m = re.search(r"BE\s*(\d{4})[.\s]?(\d{3})[.\s]?(\d{3})", html)
    kbo = (
        f"{kbo_m.group(1)}.{kbo_m.group(2)}.{kbo_m.group(3)}" if kbo_m else "?"
    )
    already = kbo != "?" and (kbo in taken or kbo.replace(".", "") in taken)
    e25 = info["euros"].get("2025")
    if (info["year"] == "2025" or e25) and not already:
        print(
            f"KEEP {p.name}|{kbo}|y={info['year']}|e25={e25}|fte={info['ftes']}|"
            f"nace={info['nace']}|title={info['title'][:70]}"
        )
    elif info["year"] == "2025" or e25:
        print(f"TAKEN {p.name}|{kbo}|y={info['year']}")

print("\n=== LIVE hunt ===")
seen = set()
for slug, kbo in cands:
    if kbo in seen:
        continue
    seen.add(kbo)
    dotted = f"{kbo[:4]}.{kbo[4:7]}.{kbo[7:]}"
    already = dotted in taken or kbo in taken
    if already:
        print(f"SKIP taken {slug} {dotted}")
        continue
    try:
        body = fetch(f"https://www.companyweb.be/nl/{kbo}")
        (RAW / f"{slug}_nl.html").write_bytes(body)
        info = parse(body.decode("utf-8", "ignore"))
        if "Error 404" in info["title"] or info["year"] == "?":
            print(f"MISS {slug} {dotted} title={info['title'][:60]}")
            continue
        e25 = info["euros"].get("2025")
        flag = "Y25" if (info["year"] == "2025" or e25) else f"y{info['year']}"
        print(
            f"{flag} {slug} {dotted} e25={e25} fte={info['ftes']} "
            f"nace={info['nace']} title={info['title'][:70]}"
        )
    except Exception as e:
        print(f"ERR {slug} {dotted} {e}")
