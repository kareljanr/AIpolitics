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

# known do-not-redo
done.update(
    {
        "0204359994",  # IDELUX Eau
        "0832382635",  # IDELUX Projets Publics
        "0258258738",  # IDELUX Finances
        "0201400209",  # BEP Env / wrong
        "0219511295",  # Intradel
        "0869769702",
        "0410958712",
        "0845064196",
        "0897436971",
        "0727639263",
        "0893863017",
        "0201712587",
        "0644638937",
        "0877556624",
    }
)


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=CTX, timeout=45) as resp:
        return resp.read()


cands = [
    # IDELUX Développement guesses + known
    ("0436152789", "idelux-developpement"),
    ("0426152789", "idelux-developpement"),
    ("0478123456", "idelux-developpement"),
    ("0206123456", "idelux"),
    ("0432382635", "idelux-developpement"),
    ("0822382635", "idelux-developpement"),
    ("0845382635", "idelux-developpement"),
    ("0866382635", "idelux-developpement"),
    ("0408382635", "idelux"),
    ("0419382635", "idelux"),
    # unused WZC YE2025 confirmed earlier
    ("0417958152", "woonzorgcentrum-sint-camillus"),
    ("0445175263", "wzc-zilverlinde"),
    ("0452865383", "rusthuis-sint-jozef"),
]

# Better: scrape IDELUX site / companyweb search via northdata-like pages
# First try open idelux group pages we have
print("done contains camillus?", "0417958152" in done)
print("done contains zilverlinde?", "0445175263" in done)

hits = []
for kbo, slug in cands:
    if kbo in done:
        print("SKIP", kbo, slug)
        continue
    url = f"https://www.companyweb.be/nl/{kbo}/{slug}"
    try:
        body = fetch(url)
    except Exception as e:
        print("FAIL", kbo, type(e).__name__)
        continue
    (RAW / f"cand_{kbo}_nl.html").write_bytes(body)
    html = body.decode("utf-8", "ignore")
    text = unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html)))
    title_m = re.search(r"<title>([^<]+)</title>", html, re.I)
    title = title_m.group(1)[:90] if title_m else slug
    lb = re.search(r"Laatste balansjaar\s+(\d{4})", text)
    year = lb.group(1) if lb else "?"
    euros = {m.group(1): m.groups()[1:] for m in pat.finditer(html)}
    print(f"{kbo}|{year}|e25={euros.get('2025')}|{title}")
    if year == "2025":
        hits.append((kbo, slug, title, euros.get("2025"), euros.get("2024")))

print("---HITS---")
for h in hits:
    print(h[0], h[2][:70], h[3])
