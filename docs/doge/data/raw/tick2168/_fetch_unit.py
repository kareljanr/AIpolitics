# -*- coding: utf-8 -*-
import re, ssl, urllib.request
from pathlib import Path
ctx=ssl.create_default_context(); UA={"User-Agent":"Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out=Path("docs/doge/data/raw/tick2168"); kbo="0410127084"

def fetch(url,p):
    req=urllib.request.Request(url,headers=UA)
    with urllib.request.urlopen(req,context=ctx,timeout=30) as r: data=r.read()
    p.write_bytes(data); return data.decode("utf-8","ignore")

for lang in ["nl","fr","en"]:
    t=fetch(f"https://www.companyweb.be/{lang}/{kbo}", out/f"sint_lodewijk_{lang}.html")
    print(lang, len(t))
kbo_html=fetch("https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0410127084", out/"sint_lodewijk_kbo.html")
text=re.sub(r"<script[\s\S]*?</script>"," ",kbo_html,flags=re.I)
text=re.sub(r"<[^>]+>","\n",text)
lines=[re.sub(r"\s+"," ",l).strip() for l in text.splitlines() if re.sub(r"\s+"," ",l).strip()]
for i,l in enumerate(lines):
    if any(k in l.lower() for k in ["status","actief","naam","juridische","adres","telefoon","e-mail","web","vestiging","nace","begindatum","0410","sint","lodewijk","schilde"]):
        print(i, l[:140])
# site contact
for url,name in [
 ("https://www.sintlodewijk.be/","site"),
 ("https://www.zorgcentrumsintlodewijk.be/","site2"),
 ("https://www.google.com/search?q=Zorgcentrum+Sint+Lodewijk+Schilde+contact", "gsearch"),
]:
    try:
        t=fetch(url, out/f"{name}.html")
        print(name, "ok", len(t))
        emails=set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", t))
        print(" emails", list(emails)[:10])
        phones=re.findall(r"0\d[\d\s/.-]{7,}", t)
        print(" phones", phones[:5])
    except Exception as e:
        print(name, type(e).__name__, e)
# parse EN metrics again + NACE from page text
t=Path(out/"sint_lodewijk_en.html").read_text(encoding="utf-8",errors="replace")
yb={}
for y,body in re.findall(r"(20\d\d)\s*:\s*\{([^{}]+)\}", t):
    def g(k,b=body):
        m=re.search(rf'{k}:\s*"([^"]*)"',b); return m.group(1) if m else None
    yb[y]={k:g(k) for k in ["omzet","winst","bruto_marge","eigen_vermogen"]}
print("YE", {y:yb[y] for y in sorted(yb)[-2:]})
print("FTE", re.search(r"([\d.,]+)\s*FTE", t).group(1))
print("filed", re.search(r"filed on ([0-9-]{10})", t).group(1))
# NACE descriptions nearby
for m in re.finditer(r"87\.\d{3}[^<\n]{0,80}|Residential|care|RVT|ROB|nursing", t, re.I):
    print("hint", m.group(0)[:100])
    break
