import re
import ssl
import urllib.request
from pathlib import Path
from pypdf import PdfReader

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0"}
out = Path("docs/doge/raw/tick1754")

urls = [
    (
        "jr2025",
        "https://www.maaseik.be/sites/default/files/2026-08/Rekening-2025-BWOL-boek-toezicht.pdf",
    ),
    (
        "bw2026",
        "https://www.maaseik.be/sites/default/files/2026-08/BW-1-en-2-2026-BWOL-boek-toezicht.pdf",
    ),
]

for name, url in urls:
    req = urllib.request.Request(url, headers=ua)
    with urllib.request.urlopen(req, timeout=120, context=ctx) as r:
        data = r.read()
    path = out / f"bwol_{name}.pdf"
    path.write_bytes(data)
    print(name, len(data), data[:5])
    rr = PdfReader(str(path))
    print("pages", len(rr.pages))
    # print early pages + pages with key terms
    for i, p in enumerate(rr.pages):
        t = p.extract_text() or ""
        if i < 8 or any(
            k in t.lower()
            for k in [
                "uitgaven",
                "ontvangsten",
                "personeel",
                "dotatie",
                "totaal g",
                "samenvatt",
                "resultaat",
                "gemeente",
            ]
        ):
            if i < 12 or re.search(
                r"totaal|uitgaven gewone|personeel|gemeentelijke|federale",
                t,
                re.I,
            ):
                print(f"\n==== p{i+1} ====")
                print(t[:2500])

# KBO address
kh = (out / "kbo.html").read_text(encoding="utf-8")
kt = re.sub(r"<[^>]+>", " ", kh)
kt = re.sub(r"\s+", " ", kt)
idx = kt.lower().find("adres")
print("\nKBO", kt[idx : idx + 450] if idx >= 0 else kt[:500])
