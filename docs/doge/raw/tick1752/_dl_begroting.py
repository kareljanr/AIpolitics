import ssl
import urllib.request
from pathlib import Path
from pypdf import PdfReader

out = Path("docs/doge/raw/tick1752")
ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0"}

ids = [
    ("begroting2026", "10WJjEkF4C-al4sC-Y7u0VExmJj0Kwdmc"),
    ("motivatienota", "1DH7sjg1L-dzJ_yvo50dbdJPKZ5zFbHqT"),
]

for name, fid in ids:
    urls = [
        f"https://drive.google.com/uc?export=download&id={fid}",
        f"https://drive.google.com/uc?export=download&confirm=t&id={fid}",
        f"https://www.googleapis.com/drive/v3/files/{fid}?alt=media",
    ]
    for url in urls:
        try:
            req = urllib.request.Request(url, headers=ua)
            with urllib.request.urlopen(req, timeout=60, context=ctx) as r:
                data = r.read()
                ctype = r.headers.get("Content-Type", "")
            print(name, url[:60], "len", len(data), "ctype", ctype, "head", data[:8])
            if data[:4] == b"%PDF":
                path = out / f"rand_{name}.pdf"
                path.write_bytes(data)
                rr = PdfReader(str(path))
                print("  pages", len(rr.pages))
                for i, p in enumerate(rr.pages[:6]):
                    t = p.extract_text() or ""
                    print(f"  ---p{i+1}---")
                    print(t[:2000])
                # search all for key euros
                full = "\n".join((p.extract_text() or "") for p in rr.pages)
                for kw in ["uitgaven", "ontvangsten", "personeel", "dotatie", "gemeente", "2025", "totaal", "budget"]:
                    if kw.lower() in full.lower():
                        pass
                import re

                amounts = re.findall(r"(?:€\s*)?(\d{1,3}(?:[.\s]\d{3})+(?:,\d{2})?|\d+,\d{2})", full)
                print("  amount samples", amounts[:40])
                break
            else:
                # maybe HTML confirm page
                (out / f"rand_{name}_dl.html").write_bytes(data[:50000])
                print("  not pdf, saved html snippet")
        except Exception as e:
            print(name, "FAIL", url[:50], type(e).__name__, str(e)[:100])
