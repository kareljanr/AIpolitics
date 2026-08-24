# -*- coding: utf-8 -*-
import csv, re, ssl, urllib.request
from pathlib import Path
csv.field_size_limit(10**7)
ctx=ssl.create_default_context(); UA={"User-Agent":"Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out=Path("docs/doge/data/raw/tick2168")
mined=set()
for path in ["docs/doge/data/entities.csv","docs/doge/data/commitments.csv","docs/doge/data/leaderboard.csv"]:
    with open(path,newline="",encoding="utf-8") as f:
        for row in csv.DictReader(f):
            blob=re.sub(r"[.\s]","", " ".join(str(v) for v in row.values()))
            for m in re.findall(r"\d{10}", blob): mined.add(m)

def fetch(url,p):
    try:
        req=urllib.request.Request(url,headers=UA)
        with urllib.request.urlopen(req,context=ctx,timeout=30) as r: data=r.read()
        p.write_bytes(data); return data.decode("utf-8","ignore")
    except Exception as e:
        print("FAIL",p.name,type(e).__name__); return None

def parse(t):
    yb={}
    for y,body in re.findall(r"(20\d\d)\s*:\s*\{([^{}]+)\}", t or ""):
        def g(k,b=body):
            m=re.search(rf'{k}:\s*"([^"]*)"',b); return m.group(1) if m else None
        yb[y]={k:g(k) for k in ["omzet","winst","bruto_marge","eigen_vermogen"]}
    fte=re.search(r"([\d.,]+)\s*FTE", t or "")
    filed=re.search(r"filed on ([0-9-]{10})", t or "")
    title=re.search(r"<title>([^<]+)", t or "")
    nace87=re.findall(r"87\.\d{3}", t or "")[:5]
    nbad=re.findall(r"(?:68|55|64|70)\.\d{3}", t or "")[:4]
    # also try description
    return yb, fte.group(1) if fte else None, filed.group(1) if filed else None, title.group(1) if title else None, nace87, nbad

CANDS=[
("0411600692","maria_rustoord_moorslede"),
("0453287037","samen_ouder_sint_niklaas"),
("0410127084","sint_lodewijk_schilde"),
("0454090355","zusters_sint_vincentius_deinze"),
("0644843825","sint_vincentius_aaigem"),
("0641760611","numera_services"),
("0650907810","ventu"),
("0400371161","abdij_affligem"),
("0787300696","melis_home"),
]
for kbo,label in CANDS:
    st="MINED" if kbo in mined else "FREE"
    t=fetch(f"https://www.companyweb.be/en/{kbo}", out/f"{label}_{kbo}_en.html")
    if not t:
        print(st,kbo,"fail"); continue
    # also NL+FR+KBO for winners later
    yb,fte,filed,title,n87,nbad=parse(t)
    if "Error 404" in (title or ""):
        print(st,kbo,"404"); continue
    y5=yb.get("2025",{}); y4=yb.get("2024",{})
    print(st,kbo,(title or "")[:70])
    print("  fte",fte,"filed",filed,"nace87",n87[:3],"other",nbad[:3])
    print("  2025",y5)
    print("  2024",y4)
    if st=="FREE" and y5:
        omzet=(y5.get("omzet") or "").replace(",","")
        bruto=(y5.get("bruto_marge") or "").replace(",","")
        o=int(omzet) if omzet.isdigit() else 0
        b=int(bruto) if bruto.isdigit() else 0
        if (o>=200000 or b>=200000) and not (nbad and not n87 and "vincentius" not in label and "maria" not in label and "samen" not in label and "lodewijk" not in label and "aaigem" not in label):
            print("  >>> STRONG CANDIDATE")
