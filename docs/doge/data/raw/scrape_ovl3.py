import urllib.request
import re
import json

# Try smartcities API / listing endpoints
candidates = [
    "https://raadpleeg-oost-vlaanderen.onlinesmartcities.be/api/search?q=meerjarenplan",
    "https://raadpleeg-oost-vlaanderen.onlinesmartcities.be/api/zittingen",
    "https://raadpleeg-oost-vlaanderen.onlinesmartcities.be/zittingen",
    "https://raadpleeg-oost-vlaanderen.onlinesmartcities.be/documenten",
    "https://raadpleeg-oost-vlaanderen.onlinesmartcities.be/search",
    "https://dms.oost-vlaanderen.be/search?q=meerjarenplan+2026",
    "https://dms.oost-vlaanderen.be/search?query=meerjarenplan",
    # known Data folder siblings
    "https://provincieoost-vlaanderen.beleidsportaal.be/Data/c66a5628-79bb-4bfa-a5e1-669708b8200e/Public/",
    "https://provincieoost-vlaanderen.beleidsportaal.be/Data/c66a5628-79bb-4bfa-a5e1-669708b8200e/",
]

names = [
    "meerjarenplan-2026-2031 - financiele-nota.pdf",
    "meerjarenplan-2026-2031 - financiele-nota-en-toelichting.pdf",
    "meerjarenplan-2026-2031 - documentatie.pdf",
    "meerjarenplan-2026-2031 - schema-m2.pdf",
    "meerjarenplan-2026-2031 - schema-t2.pdf",
    "meerjarenplan-2026-2031 - boekdeel-2.pdf",
    "meerjarenplan-2026-2031 - financieel.pdf",
    "meerjarenplan-2026-2031 - staat-van-het-financieel-evenwicht.pdf",
    "MJP-2026-2031-fin-nota.pdf",
    "MJP_ORIGINEEL_BEGINKREDIET_2026.pdf",
]

base = "https://provincieoost-vlaanderen.beleidsportaal.be/Data/c66a5628-79bb-4bfa-a5e1-669708b8200e/Public/"

for n in names:
    u = base + urllib.request.quote(n)
    try:
        req = urllib.request.Request(u, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as r:
            print("FOUND", r.status, u, r.headers.get("Content-Type"), r.headers.get("Content-Length"))
    except Exception as e:
        code = getattr(e, "code", None)
        print("miss", code, n)

print("--- endpoints ---")
for u in candidates:
    try:
        req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=20) as r:
            html = r.read().decode("utf-8", "replace")
        print("OK", r.status, u[:90], "len", len(html))
        # sample interesting bits
        if "meerjaren" in html.lower() or "M2" in html or ".pdf" in html.lower():
            hits = re.findall(r".{0,30}meerjaren.{0,40}", html, re.I)[:5]
            pdfs = re.findall(r'href="([^"]+\.pdf[^"]*)"', html, re.I)[:8]
            print("  hits:", hits)
            print("  pdfs:", pdfs)
    except Exception as e:
        print("ERR", type(e).__name__, getattr(e, "code", ""), u[:90])
