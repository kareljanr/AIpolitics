import re
import ssl
import urllib.request
from pathlib import Path
from pypdf import PdfReader

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0"}
out = Path("docs/doge/raw/tick1753")
out.mkdir(parents=True, exist_ok=True)

pdfs = [
    (
        "zzo_zr_agenda",
        "https://zuid-oost.hulpverleningszone.be/storage/xQZ0zbruOBA5b0yJigUWepXH56w7Xq1GBaTROQyW.pdf",
    ),
    (
        "zzo_zr_besluit",
        "https://zuid-oost.hulpverleningszone.be/storage/nhlfkU3xAHZ7lTQejk44R8EfofQiQDwkpii4kU9m.pdf",
    ),
]

# also crawl zoneraad listing pages for more PDF links
pages = [
    ("zzo_zoneraad", "https://www.zonezuidoost.be/zoneraad"),
    (
        "zzo_zr_college",
        "https://www.zonezuidoost.be/zoneraad-zonecollege",
    ),
    (
        "zzo_beg2026",
        "https://www.zonezuidoost.be/zoneraad/agenda-zoneraad-23-februari-2024-fpjkp-6am9x-zyeff-2aw5c-gykxr-a35kj-na69j-3fhrt-msf2p-e586f-cezk2-jrhde-cstbf-7da7z-5b2dn-sxyjn-afmfx-mcf92-34mxr-d98te-2tt56-z3pmt-7wdls-m9d9a-59d3x-pxcgr",
    ),
    (
        "zzo_tag2026",
        "https://www.zonezuidoost.be/zoneraad/tag/2026",
    ),
]

for name, url in pages:
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, timeout=30, context=ctx) as r:
            html = r.read().decode("utf-8", "replace")
        (out / f"{name}.html").write_text(html, encoding="utf-8")
        links = re.findall(r'href=["\']([^"\']+)["\']', html)
        pdf_like = [
            l
            for l in links
            if re.search(r"pdf|storage|jaar|reken|begrot|besluit|notul", l, re.I)
        ]
        print(name, "ok", len(html), "pdfish", pdf_like[:25])
        # squarespace sometimes embeds static CDN
        static = re.findall(
            r"https?://[^\"'\s]+\.pdf", html
        ) + re.findall(r"https?://[^\"'\s]+storage/[^\"'\s]+", html)
        print("  static", static[:15])
    except Exception as e:
        print(name, type(e).__name__, str(e)[:120])

for name, url in pdfs:
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, timeout=40, context=ctx) as r:
            data = r.read()
        path = out / f"{name}.pdf"
        path.write_bytes(data)
        print(name, "DL", len(data), data[:5])
        if data[:4] == b"%PDF":
            rr = PdfReader(str(path))
            print("  pages", len(rr.pages))
            for i, p in enumerate(rr.pages[:8]):
                t = p.extract_text() or ""
                print(f"  ---p{i+1}---")
                print(t[:2500])
    except Exception as e:
        print(name, "FAIL", type(e).__name__, str(e)[:120])

# KBO address extract
kh = (out / "kbo_zzo.html").read_text(encoding="utf-8")
kt = re.sub(r"<[^>]+>", " ", kh)
kt = re.sub(r"\s+", " ", kt)
idx = kt.lower().find("adres")
print("KBO", kt[idx : idx + 500] if idx >= 0 else kt[:600])
