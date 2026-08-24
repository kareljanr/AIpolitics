# -*- coding: utf-8 -*-
import urllib.request, re, ssl
from pathlib import Path
ctx=ssl.create_default_context()
ua={"User-Agent":"Mozilla/5.0"}
dst=Path("docs/doge/data/raw/tick2143")
dst.mkdir(parents=True, exist_ok=True)
urls={
 "careion_cw_en.html":"https://www.companyweb.be/en/0422923859/seniors-care-ion",
 "careion_cw_nl.html":"https://www.companyweb.be/nl/0422923859/seniors-care-ion",
 "careion_cw_fr.html":"https://www.companyweb.be/fr/0422923859/seniors-care-ion",
 "careion_kbo.html":"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0422923859",
 "bornem_en.html":"https://www.companyweb.be/en/0877556624",
 "faro_en.html":"https://www.companyweb.be/en/0893863017",
 "aiesh_en.html":"https://www.companyweb.be/en/0201712587",
}
for name,url in urls.items():
    try:
        req=urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=40) as r:
            data=r.read()
        (dst/name).write_bytes(data)
        print("OK", name, len(data))
    except Exception as e:
        print("FAIL", name, e)

en=(dst/"careion_cw_en.html").read_text(encoding="utf-8", errors="replace")
print("title", re.search(r"<title>([^<]+)", en).group(1)[:110])
for y in ["2025","2024"]:
    mm=re.search(rf"{y}\s*:\s*\{{([^}}]+)}}", en)
    print(y, re.sub(r"\s+"," ", mm.group(1)) if mm else None)
print("fte", re.search(r'Employees\s*=\s*"([^"]+)"', en).group(1))
print("filed", re.search(r"filed on ([0-9\-]+)", en, re.I).group(1))
# EN field names sometimes differ
for key in ["Turnover","Gross margin","Profit","Equity","Employees","Principal activity","Company size","Established"]:
    m=re.search(rf"{key}[^<]{{0,40}}", en)
    # better parse JSON-ish
print("--- preferred years ---")
for name in ["bornem_en.html","faro_en.html","aiesh_en.html"]:
    t=(dst/name).read_text(encoding="utf-8", errors="replace")
    years=re.findall(r"\n(202[0-9])\s*:", t)
    m=re.search(r"Last balance sheet year[^0-9]*([0-9]{4})", t, re.I)
    print(name, years[:4], "last", m.group(1) if m else None)
# KBO status
kbo=(dst/"careion_kbo.html").read_text(encoding="utf-8", errors="replace")
for pat in [r"Status</td>\s*<td[^>]*>([^<]+)", r"Rechtsvorm</td>\s*<td[^>]*>([^<]+)", r"Adres</td>\s*<td[^>]*>(.*?)</td>", r"aanbestedende overheid", r"Aantal vestigingseenheden[^0-9]*([0-9]+)", r"Ondernemingsnummer[^0-9]*([0-9.\s]+)"]:
    m=re.search(pat, kbo, re.I|re.S)
    print("kbo", pat[:40], "=>", (re.sub(r"\s+"," ", m.group(0 if m.lastindex is None else 1))[:160] if m else None))
