# -*- coding: utf-8 -*-
import csv
import re
import ssl
import urllib.request
from html import unescape
from pathlib import Path

csv.field_size_limit(10**7)
RAW = Path(__file__).resolve().parent
RAW.mkdir(parents=True, exist_ok=True)
CTX = ssl.create_default_context()
UA = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "nl-BE,nl;q=0.9,en;q=0.8",
}
pat = re.compile(
    r'(20\d\d)\s*:\s*\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",'
    r'\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)"'
)

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

# do-not-redo from rq_2108 + recent ticks
done.update(
    {
        "0205797475",  # IDELUX Développement
        "0832382635",  # IDELUX Projets Publics
        "0204359994",  # IDELUX Eau
        "0258258738",  # IDELUX Finances
        "0219511295",  # INTRADEL
        "0869769702",  # Korian
        "0727639263",  # Comnexio
        "0897436971",  # ORES SC
        "0410958712",  # SLG Vlaanderen
        "0821289991",  # Always Home
        "0845064196",  # SLG Operaties?
    }
)


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=CTX, timeout=45) as resp:
        return resp.read()


cands = [
    # Prefer FARO / AIESH / REW if YE2025
    ("0893863017", "faro"),
    ("0201712587", "aiesh"),
    ("0644638937", "rew"),
    ("0877556624", "rew"),
    # unused WZC deferred
    ("0417958152", "woonzorgcentrum-sint-camillus"),
    ("0445175263", "wzc-zilverlinde"),
    ("0452865383", "rusthuis-sint-jozef"),
    # more unused zorg / IGS guesses from earlier notes
    ("0428620585", "wzc"),
    ("0443249616", "wzc"),
    ("0466266429", "wzc"),
    ("0480566704", "wzc"),
    ("0598966387", "wzc"),
    ("0685516024", "wzc"),
    ("0887690451", "wzc"),
]

print("camillus in done?", "0417958152" in done)
print("zilverlinde in done?", "0445175263" in done)
print("faro in done?", "0893863017" in done)
print("aiesh in done?", "0201712587" in done)

hits = []
for kbo, slug in cands:
    url = f"https://www.companyweb.be/nl/{kbo}/{slug}"
    try:
        body = fetch(url)
    except Exception as e:
        print("FAIL", kbo, slug, type(e).__name__)
        continue
    (RAW / f"cand_{kbo}_nl.html").write_bytes(body)
    html = body.decode("utf-8", "ignore")
    text = unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html)))
    title_m = re.search(r"<title>([^<]+)</title>", html, re.I)
    title = title_m.group(1)[:110] if title_m else slug
    lb = re.search(r"Laatste balansjaar\s+(\d{4})", text)
    year = lb.group(1) if lb else "?"
    euros = {m.group(1): m.groups()[1:] for m in pat.finditer(html)}
    fte = re.search(r"([\d\.,]+)\s*FTE", text)
    print(
        f"{kbo}|done={kbo in done}|year={year}|fte={fte.group(1) if fte else '?'}|"
        f"e25={euros.get('2025')}|e24={euros.get('2024')}|{title}"
    )
    if year == "2025" and kbo not in done:
        hits.append((kbo, slug, title, euros.get("2025"), euros.get("2024")))

print("---HITS YE2025 unused---")
for h in hits:
    print(h[0], h[2][:80], h[3])
