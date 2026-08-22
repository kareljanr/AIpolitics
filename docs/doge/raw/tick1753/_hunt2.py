import re
import ssl
import urllib.request
from pathlib import Path
from pypdf import PdfReader

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0"}
out = Path("docs/doge/raw/tick1753")
out.mkdir(parents=True, exist_ok=True)

urls = [
    ("zzo", "https://www.zonezuidoost.be/"),
    ("zzo_nieuws", "https://www.zonezuidoost.be/nieuws"),
    ("zzo_invest", "https://www.zonezuidoost.be/nieuws/investeren-in-veiligheid-modernisering-en-financieel-evenwicht"),
    ("zzo_over", "https://www.zonezuidoost.be/over-ons"),
    ("zzo_contact", "https://www.zonezuidoost.be/contact"),
    ("bza_fin", "https://www.brandweerzoneantwerpen.be/over-ons"),
    ("bza_bestuur", "https://www.brandweerzoneantwerpen.be/bestuur"),
    ("zoneoost", "https://www.zoneoost.be/"),
    ("aalst", "https://www.aalst.be/"),
]

for name, url in urls:
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, timeout=30, context=ctx) as r:
            html = r.read().decode("utf-8", "replace")
        (out / f"{name}.html").write_text(html, encoding="utf-8")
        links = [
            l
            for l in re.findall(r'href=["\']([^"\']+)["\']', html)
            if re.search(
                r"jaar|reken|begrot|2025|2026|pdf|financ|besluit|budget|dotatie|rapport|storage|drive",
                l,
                re.I,
            )
        ]
        emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", html)
        print(name, "ok", len(html), "links", links[:20])
        print("  emails", list(dict.fromkeys(emails))[:8])
        if "invest" in name or "zzo" == name:
            text = re.sub(r"<[^>]+>", " ", html)
            text = re.sub(r"\s+", " ", text)
            for m in re.finditer(
                r".{0,60}(euro|EUR|€|\d{1,3}(?:\.\d{3})+).{0,80}", text, re.I
            ):
                s = m.group(0)
                if re.search(r"\d", s):
                    print("  snip:", s[:160])
    except Exception as e:
        print(name, type(e).__name__, str(e)[:120])

# NorthData / KBO for Zuid-Oost
kbo_urls = [
    (
        "kbo_zzo",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0500928586",
    ),
    (
        "nd_zzo",
        "https://www.northdata.com/Hulpverleningszone%20Zuid-Oost,%20Aalst/0500%20928%20586",
    ),
]
for name, url in kbo_urls:
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, timeout=25, context=ctx) as r:
            html = r.read().decode("utf-8", "replace")
        (out / f"{name}.html").write_text(html, encoding="utf-8")
        print(name, "ok", len(html))
    except Exception as e:
        print(name, type(e).__name__, str(e)[:100])
