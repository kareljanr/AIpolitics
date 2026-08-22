import re
import ssl
import urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0"}
out = Path("docs/doge/raw/tick1749")

urls = {
    "gent_hvzc": "https://ebesluitvorming.gent.be/zittingen/25.0515.1368.4599/agendapunten/25.1105.0364.1021",
    "merelbeke_jrpage": "https://www.merelbeke-melle.be/jaarrekening-2025-zorgband-leie-en-schelde",
    "destelbergen_rmw": "https://www.destelbergen.be/sites/default/files/2026-06/20260618_RMW_Besluitenlijst.pdf",
}

for name, url in urls.items():
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, timeout=45, context=ctx) as r:
            data = r.read()
        if data[:4] == b"%PDF":
            (out / f"{name}.pdf").write_bytes(data)
            print("PDF", name, len(data))
            continue
        html = data.decode("utf-8", "replace")
        (out / f"{name}.html").write_text(html, encoding="utf-8")
        links = re.findall(r'href=["\']([^"\']+)["\']', html)
        pdfs = [l for l in links if re.search(r"pdf|download|document|file", l, re.I)]
        print("HTML", name, "len", len(html), "pdfish", len(pdfs))
        for p in pdfs[:20]:
            print(" ", p[:180])
        text = re.sub(r"<[^>]+>", " ", html)
        text = re.sub(r"\s+", " ", text)
        for m in re.finditer(
            r".{0,40}\d{1,3}(?:[.\s]\d{3})+(?:,\d{2})?.{0,50}", text
        ):
            s = m.group(0)
            if re.search(r"euro|dotatie|exploitat|invest|personeel|uitgave", s, re.I):
                print("EUR", s[:180])
    except Exception as e:
        print("FAIL", name, type(e).__name__, str(e)[:120])
