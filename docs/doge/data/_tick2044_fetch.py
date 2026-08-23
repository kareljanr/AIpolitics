# fetch AGB Bornem JR2024 PDFs + REW CW + unused WZC candidates
import re
import ssl
import urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
outdir = Path("docs/doge/data/raw/tick2044")
outdir.mkdir(parents=True, exist_ok=True)


def fetch(name, url, binary=False):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=60) as r:
            data = r.read()
            final = r.geturl()
        path = outdir / name
        path.write_bytes(data)
        print("OK", name, len(data), final[:100])
        return data
    except Exception as e:
        print("FAIL", name, type(e).__name__, str(e)[:160])
        return None


# From bornem.be search / common patterns — try media library search
page = (outdir / "bornem_jr_page.html").read_text(encoding="utf-8", errors="ignore")
# Drupal sometimes embeds file ids
for pat in [
    r"/system/files/[^\s\"']+",
    r"/media/[^\s\"']+",
    r"/sites/default/files/[^\s\"']+",
    r"file/[^\"']+",
    r"document/[^\s\"']+",
]:
    hits = re.findall(pat, page)
    if hits:
        print("pat", pat, "n", len(hits))
        for h in hits[:15]:
            print(" ", h[:180])

# Try known filenames from web search titles
candidates = [
    (
        "agb_bornem_jr2024_statutair.pdf",
        "https://www.bornem.be/sites/default/files/2025-10/Jaarrekening%202024%20AGB%20Bornem%20%28Statutair%29%201.pdf",
    ),
    (
        "agb_bornem_jr2024_bbc.pdf",
        "https://www.bornem.be/sites/default/files/2025-10/Jaarrekening%202024%20AGB%20Bornem%20%28BBC%20%28incl.%20bijlagen%29%29%201.pdf",
    ),
    (
        "agb_bornem_jr2024_rvb.pdf",
        "https://www.bornem.be/sites/default/files/2025-10/Vaststelling%20RVB%20Jaarrekening%202024%20-%20AGB%20Bornem.pdf",
    ),
]

# Also probe Drupal JSON API / search for attachments in HTML data attributes
attrs = re.findall(r'data-[a-z-]+=\"([^\"]+)\"', page)
for a in attrs:
    if "pdf" in a.lower() or "jaar" in a.lower():
        print("attr", a[:160])

# REW CW
fetch("rew_en.html", "https://www.companyweb.be/en/0644638937/reseau-d-energies-de-wavre")
fetch("rew_nl.html", "https://www.companyweb.be/nl/0644638937/reseau-d-energies-de-wavre")
fetch("rew_fr.html", "https://www.companyweb.be/fr/0644638937/reseau-d-energies-de-wavre")

# Try unused WZC candidates (not in do-not-redo)
unused = [
    ("wzc_ter_linde_hooglede", "https://www.companyweb.be/en/search?q=Ter+Linde+Hooglede"),
    ("wzc_curando", "https://www.companyweb.be/en/0423540123/curando"),
    ("wzc_gvo", "https://www.companyweb.be/nl/search?q=GVO+woonzorg"),
    ("wzc_zonnebloem", "https://www.companyweb.be/nl/search?q=WZC+Zonnebloem"),
    ("wzc_sint_anna", "https://www.companyweb.be/nl/search?q=WZC+Sint-Anna+VZW+2025"),
    ("wzc_olvv", "https://www.companyweb.be/en/0412123456/olvv"),
]

# Better: known unused from prior notes — probe a few YE2025 WZC with omzet
unused2 = [
    ("wzc_arculus", "https://www.companyweb.be/en/0412345678/x"),  # placeholder skip
]

# Parse AGB Bornem NL page for visible euros without blocks
html = (outdir / "agb_bornem_nl.html").read_text(encoding="utf-8", errors="ignore")
# table rows often as <td>...€ X...</td>
euros = re.findall(r"€\s*([\d.]+(?:,\d+)?)", html)
print("euro samples", euros[:40])
# Look for JSON financeData
for key in ["finance", "winst", "omzet", "bruto", "activa", "equity"]:
    i = html.lower().find(key)
    if i >= 0:
        snip = re.sub(r"\s+", " ", html[max(0, i - 40) : i + 120])[:160]
        print(key, ":", snip)

# Download candidate PDFs
for name, url in candidates:
    fetch(name, url, binary=True)
