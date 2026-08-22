import re
import ssl
import urllib.request
from pathlib import Path
from pypdf import PdfReader

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0"}
out = Path("docs/doge/raw/tick1753")

candidates = [
    ("b2026", "https://www.zonezuidoost.be/s/HVZ-ZUID-OOST-B-2026.pdf"),
    ("jr2025", "https://www.zonezuidoost.be/s/HVZ-ZUID-OOST-JR-2025.pdf"),
    ("jr2025b", "https://www.zonezuidoost.be/s/HVZ-ZUID-OOST-JAARREKENING-2025.pdf"),
    ("jr2025c", "https://www.zonezuidoost.be/s/Jaarrekening-2025.pdf"),
    ("r2025", "https://www.zonezuidoost.be/s/HVZ-ZUID-OOST-R-2025.pdf"),
    ("av2025", "https://www.zonezuidoost.be/s/HVZ-ZUID-OOST-AV-2025.pdf"),
]

# scrape beg2026 page + zoneraad pages for /s/ pdfs
for htmlname in ["zzo_beg2026.html", "zzo_zoneraad.html", "zzo_zr_college.html", "zzo_tag2026.html"]:
    p = out / htmlname
    if not p.exists():
        continue
    html = p.read_text(encoding="utf-8")
    for m in re.findall(r'(/s/[^"\'\s>]+\.pdf)', html, re.I):
        print("found", htmlname, m)
        candidates.append((re.sub(r"[^a-zA-Z0-9]+", "_", m)[:50], "https://www.zonezuidoost.be" + m))
    for m in re.findall(r'(https?://[^"\'\s>]+\.pdf)', html, re.I):
        print("found abs", htmlname, m)

seen = set()
for name, url in candidates:
    if url in seen:
        continue
    seen.add(url)
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, timeout=40, context=ctx) as r:
            data = r.read()
        print(name, url, "len", len(data), "head", data[:8])
        if data[:4] == b"%PDF":
            path = out / f"zzo_{name}.pdf"
            path.write_bytes(data)
            rr = PdfReader(str(path))
            print("  pages", len(rr.pages))
            full = []
            for i, p in enumerate(rr.pages):
                t = p.extract_text() or ""
                full.append(t)
                if i < 5 or any(
                    k in t.lower()
                    for k in ["uitgaven", "ontvangsten", "personeel", "dotatie", "totaal", "2025"]
                ):
                    print(f"  ===p{i+1}===")
                    print(t[:2200])
            text = "\n".join(full)
            amts = re.findall(
                r"(\d{1,3}(?:\.\d{3})+(?:,\d{2})?)", text
            )
            print("  amounts sample", amts[:50])
    except Exception as e:
        print(name, "FAIL", type(e).__name__, str(e)[:100])

# NorthData deposit hunt
nd = (out / "nd_zzo.html").read_text(encoding="utf-8", errors="replace")
for m in re.finditer(r".{0,40}(2026-\d+|jaarrekening|deposit|neerlegg).{0,80}", nd, re.I):
    print("ND", m.group(0)[:140])
