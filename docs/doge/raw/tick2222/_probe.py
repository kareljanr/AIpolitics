import re
import ssl
import urllib.request
from pathlib import Path

CTX = ssl.create_default_context()
OUT = Path("docs/doge/raw/tick2222")

cands = {
    "heropbeuring_nl": "https://www.companyweb.be/nl/0406678141/heropbeuring",
    "heropbeuring_en": "https://www.companyweb.be/en/0406678141/heropbeuring",
    "manus_bxl_nl": "https://www.companyweb.be/nl/0808114522/manus",
    "manus_vzw_en": "https://www.companyweb.be/en/0808114522/manus",
    "vlotter_nl": "https://www.companyweb.be/nl/0841843796/vlotter-maatwerk-vzw",
    "vlotter_en": "https://www.companyweb.be/en/0841843796/vlotter-maatwerk-vzw",
    "bornem": "https://www.bornem.be/jaarrekening-gemeente-ocmw-en-agb",
    "kzov_nl": "https://www.companyweb.be/nl/0422152313/katholieke-zorg-oost-vlaanderen",
}

for k, u in cands.items():
    try:
        req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=CTX, timeout=30) as r:
            html = r.read().decode("utf-8", "replace")
        (OUT / f"{k}.html").write_text(html, encoding="utf-8")
        print("====", k, "len", len(html), "url", r.geturl())
        m = re.search(r"window\.cw\.kernCijfers\s*=\s*\{(.*?)\};", html, re.S)
        if m:
            print("kern head", m.group(1)[:700])
        m = re.search(r'amountOfEmployees\s*=\s*"([^"]+)"', html)
        print("emp", m.group(1) if m else None)
        for pat in [
            r"neergelegd op ([0-9-]+)",
            r"filed on ([0-9-]+)",
            r"Laatste balansjaar\s*</div>\s*<div[^>]*>\s*(\d{4})",
            r"Last financial year\s*</div>\s*<div[^>]*>\s*(\d{4})",
        ]:
            ms = re.findall(pat, html, re.I)
            if ms:
                print(pat[:30], ms[:3])
        if "bornem" in k:
            print("has 2025 pdf?", bool(re.search(r"[Jj]aarrekening 2025", html)))
            print("has 2024 pdf?", bool(re.search(r"[Jj]aarrekening 2024", html)))
    except Exception as e:
        print("====", k, type(e).__name__, e)
