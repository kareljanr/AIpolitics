# -*- coding: utf-8 -*-
import csv
import re
import urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
RAW = Path("docs/doge/data/raw/tick2084")
RAW.mkdir(parents=True, exist_ok=True)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

blob = ""
with open("docs/doge/data/entities.csv", encoding="utf-8-sig", newline="") as f:
    blob += " ".join(str(r).lower() for r in csv.DictReader(f))
with open("docs/doge/data/research_queue.csv", encoding="utf-8-sig", newline="") as f:
    blob += " ".join(
        ((r.get("entity_id") or "") + " " + (r.get("title") or "") + " " + (r.get("notes") or "")).lower()
        for r in csv.DictReader(f)
    )
with open("docs/doge/data/leaderboard.csv", encoding="utf-8-sig", newline="") as f:
    blob += " ".join(str(r).lower() for r in csv.DictReader(f))


def mined(*terms: str) -> bool:
    return any(t.lower() in blob for t in terms)


def fetch(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "nl"})
    with urllib.request.urlopen(req, timeout=40) as resp:
        return resp.read(), resp.geturl()


CANDS = [
    ("0598966387", "de-hoeksteen-samenwerking-in-woonzorg", ["hoeksteen", "0598.966.387", "0598966387"]),
    ("0459770496", "woonzorgcentrum-sint-augustinus", ["sint-augustinus", "augustinus halle", "0459.770.496"]),
    ("0409970203", "woonzorgcentrum-sint-carolus", ["sint-carolus", "carolus ternat", "0409.970.203"]),
    ("0480566704", "hof-ter-lande-woon-en-zorgcentrum", ["hof ter lande", "0480.566.704", "0480566704"]),
    ("0443249616", "rusthuis-stil-geluk", ["stil geluk", "0443.249.616"]),
    ("0685516024", "immaculata", ["immaculata", "0685.516.024"]),
    ("0696715807", "woonzorgcentrum-crayenhof", ["crayenhof", "0696.715.807"]),
    ("0432505281", "rustoord-t-hoge", ["t hoge", "rustoord-t-hoge", "0432.505.281"]),
    ("0466266429", "helianthus", ["helianthus", "0466.266.429"]),
    ("0413055989", "woon-en-zorgcentrum-sint-jozef", ["sint jozef aarschot", "0413.055.989", "wzc sint jozef aarschot"]),
    ("0422620585", "woon-en-zorgcentrum-sint-vincentius", ["vincentius erpe", "0422.620.585"]),
    ("0478123456", "x", ["x"]),  # skip junk
    ("0869769702", "korian-belgium", ["korian", "0869.769.702"]),
    ("0887690451", "emeis-belgium", ["emeis", "0887.690.451"]),
    ("0845064196", "slg-operaties-vlaanderen", ["slg operaties", "0845.064.196"]),
    ("0405551234", "x", ["x"]),
]

# more plausible WZC KBOs from common lists
EXTRA = [
    ("0417890123", "x", ["x"]),
    ("0450123456", "x", ["x"]),
    ("0475000111", "woonzorgcentrum-het-park", ["het park"]),
    ("0418500000", "x", ["x"]),
    ("0428000000", "x", ["x"]),
    ("0439000000", "x", ["x"]),
    ("0448000000", "x", ["x"]),
    ("0468000000", "x", ["x"]),
    ("0479000000", "x", ["x"]),
    ("0481000000", "x", ["x"]),
    ("0500000000", "x", ["x"]),
    ("0550000000", "x", ["x"]),
    ("0600000000", "x", ["x"]),
    ("0650000000", "x", ["x"]),
    ("0700000000", "x", ["x"]),
    ("0750000000", "x", ["x"]),
    ("0800000000", "x", ["x"]),
    ("0820000000", "x", ["x"]),
    ("0830000000", "x", ["x"]),
    ("0850000000", "x", ["x"]),
]

# Better extras from web knowledge / plausible
EXTRA2 = [
    ("0416337262", "woon-en-zorgcentrum-home-vrijzicht-vzw", ["vrijzicht"]),  # mined
    ("0422152314", "woonzorgcentrum-sint-barbara", ["sint-barbara herselt"]),  # mined
    ("0414678562", "woon-zorgcentrum-h-vander-stokken", ["vander stokken"]),  # wrong kbo maybe
    ("0424830108", "home-stuyvenberg", ["stuyvenberg"]),  # mined
    ("0428659430", "mater-dei", ["mater dei"]),
    ("0639973732", "den-akker", ["den akker"]),
    ("0449425546", "de-wijtshage", ["wijshage"]),
    # unused prospects
    ("0408220000", "x", ["x"]),
    ("0410000000", "x", ["x"]),
    ("0411000000", "x", ["x"]),
    ("0412000000", "x", ["x"]),
    ("0414000000", "x", ["x"]),
    ("0415000000", "x", ["x"]),
    ("0416000000", "x", ["x"]),
    ("0417000000", "x", ["x"]),
    ("0418000000", "x", ["x"]),
    ("0419000000", "x", ["x"]),
]

for kbo, slug, terms in CANDS:
    if slug == "x":
        continue
    dotted = f"{kbo[:4]}.{kbo[4:7]}.{kbo[7:]}"
    if mined(*terms, kbo, dotted):
        print("SKIP mined", terms[0], kbo)
        continue
    url = f"https://www.companyweb.be/nl/{kbo}/{slug}"
    try:
        data, final = fetch(url)
        text = data.decode("utf-8", "replace")
        title = re.search(r"<title>([^<]+)</title>", text)
        ye = re.search(r"kernCijfers\s*=\s*\{\s*(20\d\d)\s*:", text)
        filed = re.search(r"neergelegd op ([0-9.\-]+)", text)
        omzet = re.search(r"omzet:\s*\"([^\"]+)\"", text)
        winst = re.search(r"winst:\s*\"([^\"]+)\"", text)
        print(
            "HIT",
            kbo,
            "YE",
            ye.group(1) if ye else "?",
            "filed",
            filed.group(1) if filed else "?",
            "omzet",
            omzet.group(1) if omzet else "?",
            "winst",
            winst.group(1) if winst else "?",
            "title",
            (title.group(1)[:70] if title else "?"),
        )
        (RAW / f"cand_{kbo}_nl.html").write_bytes(data)
        if ye and ye.group(1) == "2025":
            print("  *** YE2025 CANDIDATE ***", kbo)
    except Exception as e:
        print("FAIL", kbo, slug, type(e).__name__, str(e)[:80])
