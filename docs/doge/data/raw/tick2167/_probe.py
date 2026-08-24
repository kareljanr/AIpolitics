# -*- coding: utf-8 -*-
import re, ssl, urllib.request, csv
from pathlib import Path
csv.field_size_limit(10**7)
ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path("docs/doge/data/raw/tick2167")
out.mkdir(parents=True, exist_ok=True)

mined = set()
for path in ["docs/doge/data/entities.csv","docs/doge/data/commitments.csv","docs/doge/data/leaderboard.csv"]:
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            blob = re.sub(r"[.\s]", "", " ".join(str(v) for v in row.values()))
            for m in re.findall(r"\d{10}", blob):
                mined.add(m)

def fetch(url, path):
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, context=ctx, timeout=30) as r:
            data = r.read()
        path.write_bytes(data)
        return data.decode("utf-8", "ignore")
    except Exception as e:
        print("FAIL", path.name, type(e).__name__, str(e)[:80])
        return None

def parse_cw(t):
    yblocks={}
    for y, body in re.findall(r"(20\d\d)\s*:\s*\{([^{}]+)\}", t or ""):
        def g(k, b=body):
            m=re.search(rf'{k}:\s*"([^"]*)"', b)
            return m.group(1) if m else None
        yblocks[y]={k:g(k) for k in ["omzet","winst","bruto_marge","eigen_vermogen"]}
    fte=re.search(r"([\d.,]+)\s*FTE", t or "")
    filed=re.search(r"filed on ([0-9-]{10})", t or "") or re.search(r"neergelegd op ([0-9-]{10})", t or "")
    title=re.search(r"<title>([^<]+)", t or "")
    return yblocks, (fte.group(1) if fte else None), (filed.group(1) if filed else None), (title.group(1) if title else None)

# prefer preferred stalls check + unit
CANDS = [
    ("0893863017","faro"),
    ("0201712587","aiesh"),
    ("0644638937","rew"),
    ("0877556624","agb_bornem"),
    ("0469969453","anima_hold"),
]
for kbo,label in CANDS:
    status = "MINED" if kbo in mined else "FREE"
    print("===", label, kbo, status)
    for lang,suf in [("en","_en"),("nl","_nl"),("fr","_fr")]:
        url = f"https://www.companyweb.be/{lang}/{kbo}" if lang!="nl" else f"https://www.companyweb.be/nl/{kbo}"
        # companyweb uses /en/ /nl/ /fr/
        url = f"https://www.companyweb.be/{lang}/{kbo}"
        t = fetch(url, out / f"{label}{suf}.html")
        if lang=="en" and t:
            yb,fte,filed,title=parse_cw(t)
            print(" ", (title or "")[:90])
            print("  fte", fte, "filed", filed)
            for y in sorted(yb, reverse=True)[:2]:
                print(" ", y, yb[y])
# KBO for anima hold
kbo_html = fetch("https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0469969453", out/"anima_hold_kbo.html")
if kbo_html:
    for pat in [r"Status</td>\s*<td[^>]*>([^<]+)", r"Rechtstoestand</td>\s*<td[^>]*>([^<]+)", r"Naam</td>\s*<td[^>]*>([^<]+)", r"Juridische vorm</td>\s*<td[^>]*>([^<]+)", r"Nace[^<]*</td>\s*<td[^>]*>([^<]+)"]:
        m=re.search(pat, kbo_html, re.I)
        if m: print("KBO", pat[:20], re.sub(r"\s+"," ",m.group(1))[:80])
    # simpler dumps
    if "Actief" in kbo_html: print("KBO has Actief")
    if "Stopgezet" in kbo_html: print("KBO has Stopgezet")
