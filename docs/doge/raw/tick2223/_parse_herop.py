import re
from pathlib import Path

OUT = Path("docs/doge/raw/tick2223")
for name in ["herop_nl.html", "herop_en.html", "herop_fr.html", "vlotter_nl.html"]:
    p = OUT / name
    html = p.read_text(encoding="utf-8", errors="replace")
    print("====", name)
    # all year blocks
    for m in re.finditer(r"(20\d{2})\s*:\s*\{([^}]{0,400})\}", html):
        print("YEAR", m.group(1), m.group(2)[:300].replace("\n", " "))
    # balansjaar
    for pat in [
        r"Laatste balansjaar.*?</div>\s*<div[^>]*>\s*(\d{4})",
        r"Last financial year.*?</div>\s*<div[^>]*>\s*(\d{4})",
        r"Dernier exercice.*?</div>\s*<div[^>]*>\s*(\d{4})",
        r"balansjaar[^\d]{0,40}(\d{4})",
    ]:
        ms = re.findall(pat, html, re.I | re.S)
        if ms:
            print(pat[:40], ms[:5])
    # omzet/winst anywhere
    for key in ["omzet", "winst", "bruto_marge", "eigen_vermogen", "turnover", "profit", "equity"]:
        ms = re.findall(rf'{key}\s*[:=]\s*"([^"]*)"', html, re.I)
        if ms:
            print(key, ms[:8])
    # free pub links / deposits
    pubs = re.findall(r"/company/\d+/free-pub/(\d+)", html)
    print("free-pubs", pubs[:8])
    # size class
    text = re.sub(r"<[^>]+>", " ", html)
    text = re.sub(r"\s+", " ", text)
    for needle in ["Klein", "Groot", "Middel", "Micro", "Small", "Large", "VKT", "VOL"]:
        if needle in text:
            print("size-ish", needle)
    m = re.search(r"Aantal vestigingseenheden \(VE\):\s*(\d+)", text)
    print("VE", m.group(1) if m else None)
    m = re.search(r"NACE[^0-9]{0,20}(\d{2}\.\d{3})", text)
    print("nace", m.group(1) if m else None)
    emails = sorted(set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", html)))
    print("emails", [e for e in emails if "sentry" not in e and "companyweb" not in e][:8])
    # KBO page-ish
    for pat in [r"Status:\s*(\w+)", r"Adres van de zetel:.{0,120}", r"Begindatum:.{0,40}"]:
        m = re.search(pat, text)
        if m:
            print(m.group(0)[:140])
