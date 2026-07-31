import urllib.request
import re
import json

urls = [
    "https://raadpleeg-oost-vlaanderen.onlinesmartcities.be",
    "https://raadpleeg-oost-vlaanderen.onlinesmartcities.be/search?q=meerjarenplan",
    "https://dms.oost-vlaanderen.be",
    "https://www.oost-vlaanderen.be/zoeken?q=meerjarenplan+2026",
    "https://provincieoost-vlaanderen.beleidsportaal.be/meerjarenplan-2026-2031/programma/handleiding",
    "https://provincieoost-vlaanderen.beleidsportaal.be/meerjarenplan-2026-2031/programma/omschrijving-van-de-prioritaire-actieplannen",
    "https://www.vrt.be/vrtnws/nl/2025/12/04/oost-vlaanderen-belasting-daalt-mobiliteit-water-recreatie-moens/",
    "https://www.hln.be/gent/de-meerjarenplanning-van-de-provincie-oost-vlaanderen-onder-de-loep-van-5-3-miljoen-euro-voor-recreatiedomein-de-ster-tot-fietstunnel-in-zelzate~a33456c6/",
]

for u in urls:
    try:
        req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
        with urllib.request.urlopen(req, timeout=25) as r:
            raw = r.read()
            html = raw.decode("utf-8", "replace")
        print("OK", u[:80], "len", len(html))
        # numbers near exploitatie
        for m in re.finditer(r".{0,40}exploitatie.{0,80}", html, re.I):
            s = re.sub(r"\s+", " ", m.group(0))
            if any(c.isdigit() for c in s):
                print("  EXP:", s[:150])
        pdfs = re.findall(r"https?://[^\s\"'<>]+\.pdf", html, re.I)[:8]
        if pdfs:
            print("  pdfs:", pdfs)
        href_pdf = re.findall(r'href="([^"]+\.pdf[^"]*)"', html, re.I)[:8]
        if href_pdf:
            print("  href_pdf:", href_pdf)
        data = re.findall(r"/Data/[^\s\"'<>]+", html)[:10]
        if data:
            print("  data:", data)
        # million patterns
        mil = re.findall(r"[0-9]+[.,]?[0-9]*\s*miljoen", html, re.I)[:15]
        if mil:
            print("  miljoen:", mil)
    except Exception as e:
        print("ERR", u[:80], type(e).__name__, e)
