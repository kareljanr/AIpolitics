# -*- coding: utf-8 -*-
import re
import urllib.request
from pathlib import Path

UA = {"User-Agent": "Mozilla/5.0"}
OUT = Path(__file__).resolve().parent


def get(url: str, dest: Path | None = None) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    data = urllib.request.urlopen(req, timeout=60).read()
    if dest:
        dest.write_bytes(data)
        print("saved", dest.name, len(data))
    return data


urls = [
    "https://www.playright.be/",
    "https://playright.be/",
    "https://www.simim.be/",
    "https://www.simim.be/bedrijf/",
    "https://playright.be/dit-was-de-algemene-vergadering-van-playright-2025/",
]
for base in urls:
    try:
        html = get(base).decode("utf-8", "replace")
        pdfs = sorted(
            set(
                re.findall(
                    r"https?://[^\"'\s>]+\.pdf|/[a-zA-Z0-9_./%-]+\.pdf",
                    html,
                    re.I,
                )
            )
        )
        print("===", base, "pdfs", len(pdfs))
        for p in pdfs[:50]:
            print(p)
    except Exception as e:
        print("ERR", base, type(e).__name__, e)

# download known live PDFs
known = [
    (
        "https://playright.be/wp-content/uploads/2025/05/PlayRight-commissarisverslag-NL.pdf",
        "playright_commissaris_2024.pdf",
    ),
    (
        "https://www.simim.be/bedrijf/Rapport_De_Gestion_SIMIM_2024.pdf",
        "simim_rapport_gestion_2024.pdf",
    ),
]
for url, name in known:
    try:
        get(url, OUT / name)
    except Exception as e:
        print("DL ERR", name, e)
