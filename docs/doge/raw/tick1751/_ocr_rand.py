import re
import ssl
import urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0"}
out = Path("docs/doge/raw/tick1751")

# Zone sites
for name, url in [
    ("rand_home", "https://www.brandweerzonerand.be/"),
    ("rand_nieuws", "https://www.brandweerzonerand.be/nieuws"),
    ("waas_home", "https://www.hvzwaasland.be/"),
    ("waas_beleidsplan", "https://www.hvzwaasland.be/beleidsplan-investeren-in-toekomstbestendige-hulpverlening"),
]:
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, timeout=30, context=ctx) as r:
            html = r.read().decode("utf-8", "replace")
        (out / f"{name}.html").write_text(html, encoding="utf-8")
        links = re.findall(r'href=["\']([^"\']+)["\']', html)
        hits = [l for l in links if re.search(r"jaar|reken|begrot|2025|pdf|financ|besluit|dotatie", l, re.I)]
        print(name, "hits", len(hits))
        for h in hits[:20]:
            print(" ", h[:160])
    except Exception as e:
        print(name, type(e).__name__, str(e)[:100])

# OCR Rand PDFs via pypdfium2 or PIL+pymupdf
pdf_path = out / "rand2025.pdf"
try:
    import pypdfium2 as pdfium

    pdf = pdfium.PdfDocument(str(pdf_path))
    import pytesseract
    from PIL import Image

    for i in range(len(pdf)):
        page = pdf[i]
        bitmap = page.render(scale=2)
        pil = bitmap.to_pil()
        text = pytesseract.image_to_string(pil, lang="nld+eng")
        print("==== OCR page", i + 1)
        print(text[:2500])
except Exception as e:
    print("OCR fail", type(e).__name__, e)
    try:
        import fitz  # pymupdf

        doc = fitz.open(str(pdf_path))
        for i, page in enumerate(doc):
            text = page.get_text()
            print("==== pymupdf", i + 1, "len", len(text))
            print(text[:2000])
            # also try OCR if empty
            if len(text.strip()) < 50:
                pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
                img_path = out / f"rand2025_p{i+1}.png"
                pix.save(str(img_path))
                import pytesseract
                from PIL import Image

                text = pytesseract.image_to_string(Image.open(img_path), lang="nld+eng")
                print("OCR", text[:2500])
    except Exception as e2:
        print("pymupdf fail", type(e2).__name__, e2)
