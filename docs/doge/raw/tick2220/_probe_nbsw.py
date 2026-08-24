import re
from pathlib import Path

paths = [
    Path("docs/doge/data/raw/tick2220/nbsw_nl.html"),
    Path("docs/doge/data/raw/tick2220/nbsw_en.html"),
    Path("docs/doge/data/raw/tick2220/nbsw_fr.html"),
    Path("docs/doge/data/raw/tick2220/nbsw_kbo.html"),
    Path("docs/doge/raw/tick2219/nbsw.html"),
]
for p in paths:
    if not p.exists():
        print("missing", p)
        continue
    html = p.read_text(encoding="utf-8", errors="replace")
    print("====", p, len(html))
    m = re.search(r"window\.cw\.kernCijfers\s*=\s*\{(.*?)\};", html, re.S)
    if m:
        print("kern", m.group(1)[:1000])
    m = re.search(r'amountOfEmployees\s*=\s*"([^"]+)"', html)
    print("emp", m.group(1) if m else None)
    for pat in [
        r"neergelegd op ([0-9-]+)",
        r"filed on ([0-9-]+)",
        r"déposés le ([0-9-]+)",
        r"0479\.456\.845",
        r"88\.993",
        r"info@[A-Za-z0-9.-]+",
    ]:
        ms = re.findall(pat, html)
        if ms:
            print(pat, ms[:5])
    text = re.sub(r"<[^>]+>", " ", html)
    text = re.sub(r"\s+", " ", text)
    m = re.search(r"Aantal vestigingseenheden \(VE\):\s*(\d+)", text)
    if m:
        print("VE", m.group(1))
    m = re.search(r"Adres van de zetel:.{0,120}", text)
    if m:
        print("addr", m.group(0)[:150])
    m = re.search(r"Begindatum:.{0,80}", text)
    if m:
        print("begin", m.group(0)[:100])
    m = re.search(r"Status:\s*(\w+)", text)
    if m:
        print("status", m.group(1))
    # FARO stall check
    if "faro" in p.name.lower():
        m = re.search(r"Laatste balansjaar.{0,40}(\d{4})", text)
        print("faro year hint", m.group(0) if m else None)
        m = re.search(r"window\.cw\.kernCijfers\s*=\s*\{(.*?)\};", html, re.S)
        if m:
            print("faro kern head", m.group(1)[:400])
