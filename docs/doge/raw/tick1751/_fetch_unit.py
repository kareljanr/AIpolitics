import re
import ssl
import urllib.request
from pathlib import Path
from pypdf import PdfReader

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0"}
out = Path("docs/doge/raw/tick1751")

urls = {
    "rand_cijfers": "https://www.brandweerzonerand.be/nieuws/brandweer-zone-rand-in-cijfergegevens-2025",
    "waas_besluit": "https://www.hvzwaasland.be/over-ons/besluitvorming",
    "schoten_mjp": "https://www.schoten.be/sites/default/files/2025-12/Meerjarenplan_finaal-LR.pdf",
}

for name, url in urls.items():
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, timeout=60, context=ctx) as r:
            data = r.read()
        if data[:4] == b"%PDF":
            path = out / f"{name}.pdf"
            path.write_bytes(data)
            print("PDF", name, len(data))
            rdr = PdfReader(str(path))
            print(" pages", len(rdr.pages))
            # search pages mentioning brandweer / Rand / 2025 euros
            for i, p in enumerate(rdr.pages):
                t = p.extract_text() or ""
                if re.search(r"Brandweer|Rand|1[\.\s]?\d{3}[\.\s]?\d{3}", t, re.I):
                    if "Rand" in t or "brandweer" in t.lower():
                        print("====", name, "p", i + 1)
                        print(t[:2000])
                        print()
            continue
        html = data.decode("utf-8", "replace")
        (out / f"{name}.html").write_text(html, encoding="utf-8")
        print("HTML", name, len(html))
        text = re.sub(r"<[^>]+>", " ", html)
        text = re.sub(r"\s+", " ", text)
        print(text[:3000])
        print("---")
        links = re.findall(r'href=["\']([^"\']+)["\']', html)
        for l in links:
            if re.search(r"pdf|download|jaar|reken|cijfer|2025", l, re.I):
                print("LINK", l[:180])
    except Exception as e:
        print("FAIL", name, type(e).__name__, str(e)[:120])
