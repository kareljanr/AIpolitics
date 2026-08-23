# -*- coding: utf-8 -*-
"""Probe FARO/AIESH/REW + unused WZC for YE2025."""
import csv
import re
import ssl
import urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
RAW = Path(__file__).resolve().parent
CTX = ssl.create_default_context()
UA = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "nl-BE,nl;q=0.9",
}
PAT = re.compile(
    r'(20\d\d)\s*:\s*\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",'
    r'\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)"'
)
PAT2 = re.compile(r"Laatste balansjaar\s*</[^>]+>\s*(\d{4})", re.I)
FTE_PAT = re.compile(r"Personeel</td>\s*<td[^>]*>\s*([\d.,]+)")

done = set()
for path in [
    Path("docs/doge/data/entities.csv"),
    Path("docs/doge/data/commitments.csv"),
    Path("docs/doge/data/leaderboard.csv"),
]:
    with path.open(encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh):
            blob = " ".join(str(v or "") for v in row.values())
            for m in re.findall(r"0\d{9}|\d{4}\.\d{3}\.\d{3}", blob):
                done.add(re.sub(r"\D", "", m))

# known REW/AIESH from notes
with Path("docs/doge/data/entities.csv").open(encoding="utf-8-sig", newline="") as fh:
    for row in csv.DictReader(fh):
        eid = (row.get("entity_id") or "").lower()
        name = (row.get("name_nl") or "") + (row.get("notes") or "")
        if eid in ("aiesh", "igs_aiesh", "rew", "igs_rew") or "AIESH" in name or re.search(
            r"\bREW\b", name
        ):
            print("ENT", row.get("entity_id"), (row.get("name_nl") or "")[:70])
            print("  ", (row.get("notes") or "")[:180])

prefer = [
    ("0893863017", "faro"),
    ("0201712587", "aiesh"),
    ("0877556624", "agb-bornem"),
]
# REW KBO candidates often paired with AIESH in prior ticks — try common
rew_guesses = [
    ("0201726507", "rew"),
    ("0203006297", "rew2"),
    ("0215499804", "rew3"),
    ("0200758537", "rew4"),
]

cands = [
    ("0696715807", "crayenhof"),
    ("0432505281", "rustoord-t-hoge"),
    ("0422620585", "wzc-sv"),
    ("0425728191", "ter-lammeken"),
    ("0406687990", "huis-perrekes"),
    ("0475345821", "avondvrede"),
    ("0409705825", "de-mijlpaal"),
    ("0432161685", "ter-linden"),
    ("0405308859", "bethanie"),
    ("0418176295", "magnolia"),
    ("0421974538", "onderdale"),
    ("0438562119", "de-bijster"),
    ("0427819403", "zonnig-huis"),
    ("0419447286", "gielsbos"),
    ("0406912358", "philippus"),
    ("0462914805", "de-meander"),
    ("0473105916", "sint-anna"),
    ("0484216027", "sint-rochus"),
    ("0407890112", "den-houtmolen"),
    ("0413901223", "huize-van-waas"),
    ("0426531872", "sint-jozef-herent"),
    ("0448753094", "witte-meersen"),
    ("0459864105", "centrum-gheel"),
    ("0460975216", "pc-gheel"),
    ("0471086327", "olivetenhof"),
    ("0471977452", "cand0471"),
    ("0441313178", "cand0441"),
    ("0443249616", "cand0443"),
    ("0466266429", "cand0466"),
    ("0480566704", "cand0480"),
    ("0598966387", "cand0598"),
    ("0685516024", "cand0685"),
    ("0795384162", "cand0795"),
    ("0845064196", "cand0845"),
    ("0408223456", "cand0408"),
    ("0414693113", "groep-zorg-h-familie"),
    ("0417798001", "cand0417"),
    ("0417850640", "zilverbos-alt"),
]


def fetch(kbo: str, slug: str):
    url = f"https://www.companyweb.be/nl/{kbo}/{slug}"
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, context=CTX, timeout=25) as resp:
            html = resp.read().decode("utf-8", "replace")
    except Exception as exc:  # noqa: BLE001
        return None, str(exc)
    (RAW / f"{slug}_{kbo}_nl.html").write_text(html, encoding="utf-8")
    years = PAT.findall(html)
    m2 = PAT2.search(html)
    last = m2.group(1) if m2 else None
    title = re.search(r"<title>([^<]+)", html)
    name = title.group(1).split("|")[0].strip() if title else slug
    fm = FTE_PAT.search(html)
    fte = fm.group(1) if fm else None
    # status Actief?
    actief = "Actief" in html[:5000]
    return {
        "kbo": kbo,
        "name": name,
        "last": last,
        "years": years,
        "fte": fte,
        "url": url,
        "done": kbo in done,
        "actief": actief,
    }, None


allc = prefer + rew_guesses + cands
hits = []
for kbo, slug in allc:
    info, err = fetch(kbo, slug)
    if err:
        print("ERR", kbo, slug, err[:100])
        continue
    ys = [y[0] for y in info["years"]]
    has25 = "2025" in ys or info["last"] == "2025"
    if info["done"]:
        flag = "DONE"
    elif has25:
        flag = "YE2025"
    else:
        flag = f"YE{info['last']}"
    print(
        flag,
        kbo,
        info["name"][:55],
        "last",
        info["last"],
        "yrs",
        ys[:4],
        "fte",
        info["fte"],
    )
    if has25 and not info["done"]:
        hits.append(info)

print("--- HITS ---", len(hits))
for h in hits:
    y = h["years"][0] if h["years"] else None
    print("HIT", h["kbo"], h["name"][:60], y, "url", h["url"])
