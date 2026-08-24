# harvest FREE-looking KBOs from tick2127 near*.html titles that may have YE2025
import re, csv, ssl, urllib.request
from pathlib import Path
csv.field_size_limit(10**7)
mined=set()
for path in ["docs/doge/data/entities.csv","docs/doge/data/commitments.csv","docs/doge/data/leaderboard.csv"]:
    with open(path,newline="",encoding="utf-8") as f:
        for row in csv.DictReader(f):
            blob=re.sub(r"[.\s]","", " ".join(str(v) for v in row.values()))
            for m in re.findall(r"\d{10}", blob): mined.add(m)
ctx=ssl.create_default_context(); UA={"User-Agent":"Mozilla/5.0"}
out=Path("docs/doge/data/raw/tick2168")
kbos=[]
for folder in [Path("docs/doge/data/raw/tick2127"), Path("docs/doge/data/raw/tick2126"), Path("docs/doge/data/raw/tick2058")]:
    if not folder.exists(): continue
    for p in folder.glob("*.html"):
        t=p.read_text(encoding="utf-8",errors="replace")[:8000]
        title=re.search(r"<title>([^<]+)", t)
        for m in re.findall(r"BE0?(\d{9,10})", t[:3000]):
            d=m if len(m)==10 else ("0"+m)
            if len(d)==10: kbos.append((d, p.name, (title.group(1) if title else "")[:50]))
        m2=re.search(r"(\d{10})", p.name)
        if m2: kbos.append((m2.group(1), p.name, ""))
print("harvested", len(kbos))
seen=set(); free_y5=[]
def fetch(url,p):
    try:
        req=urllib.request.Request(url,headers=UA)
        with urllib.request.urlopen(req,context=ctx,timeout=25) as r: data=r.read()
        p.write_bytes(data); return data.decode("utf-8","ignore")
    except Exception as e:
        return None
def parse(t):
    yb={}
    for y,body in re.findall(r"(20\d\d)\s*:\s*\{([^{}]+)\}", t or ""):
        def g(k,b=body):
            m=re.search(rf'{k}:\s*"([^"]*)"',b); return m.group(1) if m else None
        yb[y]={k:g(k) for k in ["omzet","winst","bruto_marge","eigen_vermogen"]}
    fte=re.search(r"([\d.,]+)\s*FTE", t or "")
    filed=re.search(r"filed on ([0-9-]{10})", t or "")
    title=re.search(r"<title>([^<]+)", t or "")
    nace87=re.findall(r"87\.\d{3}", t or "")[:4]
    nbad=re.findall(r"(?:68|55)\.\d{3}", t or "")[:3]
    return yb, fte.group(1) if fte else None, filed.group(1) if filed else None, title.group(1) if title else None, nace87, nbad
for kbo,src,_ in kbos:
    if kbo in seen: continue
    seen.add(kbo)
    if kbo in mined: continue
    t=fetch(f"https://www.companyweb.be/en/{kbo}", out/f"h_{kbo}_en.html")
    if not t: continue
    yb,fte,filed,title,n87,nbad=parse(t)
    if "Error 404" in (title or ""): continue
    y5=yb.get("2025")
    if not y5: continue
    print("FREE-Y5", kbo, (title or "")[:65], "fte", fte, "filed", filed, "nace", n87 or nbad, y5)
    if nbad and not n87: 
        print("  skip bad"); continue
    omzet=(y5.get("omzet") or "").replace(",","")
    bruto=(y5.get("bruto_marge") or "").replace(",","")
    o=int(omzet) if omzet.isdigit() else 0
    b=int(bruto) if bruto.isdigit() else 0
    if o>=100000 or b>=100000:
        free_y5.append((kbo,title,y5,fte,filed,n87)); print("  >>>")
print("count", len(free_y5))
for x in free_y5: print(x)
