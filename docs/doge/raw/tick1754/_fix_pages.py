from pypdf import PdfReader
from pathlib import Path

r = PdfReader("docs/doge/raw/tick1754/bwol_jr2025.pdf")
out = Path("docs/doge/raw/tick1754/_pages_text.txt")
chunks = []
for i, p in enumerate(r.pages):
    t = p.extract_text() or ""
    if len(t) > 200 and sum(c.isalnum() for c in t) > 100:
        # try reverse each line (some BBC PDFs are RTL garbled)
        lines = t.splitlines()
        rev = "\n".join(line[::-1] for line in lines)
        chunks.append(f"\n======== PAGE {i+1} raw ========\n{t[:1500]}")
        chunks.append(f"\n======== PAGE {i+1} reversed ========\n{rev[:1500]}")

out.write_text("\n".join(chunks), encoding="utf-8", errors="replace")
print("wrote", out, "chunks", len(chunks) // 2)

# also fetch lanaken 2025 bekendmaking
import ssl, urllib.request, re

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0"}
for name, url in [
    (
        "lanaken_jr",
        "https://www.lanaken.be/bekendmakingen/detail/1185/brandweerzone-oost-limburg-bwol-jaarrekening-2024",
    ),
    (
        "dilsen",
        "https://www.dilsen-stokkem.be/bekendmakingen/categorie/13/financien-beleidsrapporten",
    ),
    ("bwol_jv", "https://www.bwol.be/jaarverslagen.html"),
]:
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
            html = resp.read().decode("utf-8", "replace")
        Path(f"docs/doge/raw/tick1754/{name}.html").write_text(html, encoding="utf-8")
        pdfs = re.findall(r'href=["\']([^"\']+\.pdf[^"\']*)["\']', html, re.I)
        print(name, "pdfs", pdfs[:20])
        for m in re.finditer(
            r".{0,40}(2025|jaarrekening|rekening|euro|download).{0,80}", html, re.I
        ):
            s = re.sub(r"<[^>]+>", " ", m.group(0))
            s = re.sub(r"\s+", " ", s)
            if "2025" in s or "pdf" in s.lower() or "euro" in s.lower():
                print(" ", s[:160])
    except Exception as e:
        print(name, type(e).__name__, str(e)[:100])
