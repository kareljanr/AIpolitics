# -*- coding: utf-8 -*-
import re
import urllib.request
from pathlib import Path

UA = {"User-Agent": "Mozilla/5.0"}
OUT = Path(__file__).resolve().parent
OUT.mkdir(parents=True, exist_ok=True)


def fetch(url: str, dest: Path | None = None) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    data = urllib.request.urlopen(req, timeout=45).read()
    if dest:
        dest.write_bytes(data)
        print("saved", dest.name, len(data))
    return data


# NSZ retry
try:
    fetch(
        "http://cdn.staatsbladmonitor.be/2026pdf/2026-00394221.pdf",
        OUT / "nsz_retry.pdf",
    )
except Exception as e:
    print("NSZ", type(e).__name__, getattr(e, "code", e))

# Welzijnszorg SBM / companyweb / donorinfo / site
urls = [
    "https://www.staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0416426839",
    "https://www.welzijnszorg.be/",
    "https://www.welzijnszorg.be/jaarverslag",
    "https://www.absym-bvas.be/over-bvas/jaarverslag",
    "https://www.pov.be/",
    "https://www.g-o.be/",
    "https://www.donorinfo.be/nl/charity/welzijnszorg",
]
for u in urls:
    try:
        html = fetch(u).decode("utf-8", "replace")
        pdfs = sorted(
            set(
                re.findall(
                    r"https?://[^\"'\s>]+\.pdf|/[^\"'\s>]+\.pdf",
                    html,
                    re.I,
                )
            )
        )
        print("===", u[:70], "status OK pdfs", len(pdfs))
        for p in pdfs[:25]:
            print(" ", p[:120])
        # deposit ids
        deps = re.findall(r"20\d{2}-\d{8}", html)
        print(" deposits", deps[:10])
    except Exception as e:
        print("ERR", u[:70], type(e).__name__, getattr(e, "code", e))

# Blind scan recent deposits around Welzijnszorg filing ~2025-06-27
# Also try Northdata pointer pages
for u in [
    "https://www.northdata.com/Welzijnszorg%20VZW,%20Brussel/KBO%200416.426.839",
    "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=416426839",
]:
    try:
        html = fetch(u).decode("utf-8", "replace")
        deps = re.findall(r"20\d{2}-\d{8}", html)
        pdfs = re.findall(r"https?://[^\"'\s>]+\.pdf", html, re.I)
        print("===", u[:60], "deps", deps[:8], "pdfs", pdfs[:5])
    except Exception as e:
        print("ERR", u[:60], type(e).__name__, getattr(e, "code", e))
