import re
import ssl
import urllib.request
from pathlib import Path
from pypdf import PdfReader

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0"}
out = Path("docs/doge/raw/tick1754")
out.mkdir(parents=True, exist_ok=True)

pages = [
    (
        "maaseik_bwol",
        "https://www.maaseik.be/nl/stad-bestuur/bestuur/beleidsdocumenten/brandweerzone-oost-limburg-bwol",
    ),
    ("bwol_home", "https://www.bwol.be/"),
    (
        "bwol_besluit",
        "https://www.bwol.be/uploads/1/2/5/4/12549797/besluitenlijst_zoneraad_26_juni_2026.pdf",
    ),
    (
        "kbo",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0500907802",
    ),
]

for name, url in pages:
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, timeout=40, context=ctx) as r:
            data = r.read()
        if data[:4] == b"%PDF":
            (out / f"{name}.pdf").write_bytes(data)
            print(name, "PDF", len(data))
            rr = PdfReader(str(out / f"{name}.pdf"))
            print("  pages", len(rr.pages))
            for i, p in enumerate(rr.pages[:6]):
                print(f"  ---p{i+1}---")
                print((p.extract_text() or "")[:2000])
        else:
            html = data.decode("utf-8", "replace")
            (out / f"{name}.html").write_text(html, encoding="utf-8")
            links = re.findall(r'href=["\']([^"\']+)["\']', html)
            pdfs = [
                l
                for l in links
                if re.search(r"pdf|jaar|reken|begrot|download|file", l, re.I)
            ]
            print(name, "HTML", len(html), "pdfish", pdfs[:25])
            emails = re.findall(
                r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", html
            )
            print("  emails", list(dict.fromkeys(emails))[:8])
    except Exception as e:
        print(name, type(e).__name__, str(e)[:120])
