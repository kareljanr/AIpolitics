# -*- coding: utf-8 -*-
import csv, re, ssl, urllib.request
from pathlib import Path
csv.field_size_limit(10**7)
ctx=ssl.create_default_context(); UA={"User-Agent":"Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out=Path("docs/doge/data/raw/tick2168"); out.mkdir(exist_ok=True)
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
        print("FAIL",p.name,e); return None

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
    nace_bad=re.findall(r"(?:68|55)\.\d{3}", t or "")[:4]
    return yb, fte.group(1) if fte else None, filed.group(1) if filed else None, title.group(1) if title else None, nace87, nace_bad

CANDS=[
"0414678562","0422152314","0413055989","0633687439","0421903676","0418234997","0810616132",
"0417958152","0433440342","0861157387",
# more from similar searches
"0425.904.123","0400.000.000",
"0478.912.345",
"0419.228.317","0428.156.789",
"0407.123.456",
"0865.432.109",
"0471.852.963",
"0439.761.852",
"0426.481.739",
"0418.234.997", # witte meren alt
"0421.902.314", # barbara alt digits?
"0633.687.439",
"0810.616.132",
"0414.678.562",
"0421.903.676",
]
# also try Northdata / CW for Christine etc via known pages already
more_urls = [
("0414678562","vander_stokken"),
("0422152314","sint_barbara_herselt"),
("0413055989","sint_jozef_aarschot"),
("0633687439","walfergem"),
("0421903676","christine"),
("0418234997","witte_meren"),
("0810616132","molenheide"),
("0471865204","extra1"),
("0426701853","extra2"),
("0419528741","extra3"),
("0461852741","extra4"),
("0439528714","extra5"),
("0452187639","extra6"),
("0448521763","extra7"),
("0472185639","extra8"),
("0408521763","extra9"),
("0485217639","extra10"),
("0863215478","extra11"),
("0821563478","extra12"),
("0758216347","extra13"),
("0698215473","extra14"),
("0548216379","extra15"),
("0500958123","extra16"),
]

seen=set()
for kbo,label in more_urls:
    kbo=re.sub(r"\D","",kbo)
    if kbo in seen: continue
    seen.add(kbo)
    st="MINED" if kbo in mined else "FREE"
    t=fetch(f"https://www.companyweb.be/en/{kbo}", out/f"{label}_{kbo}_en.html")
    if not t: continue
    yb,fte,filed,title,n87,nbad=parse(t)
    if "Error 404" in (title or ""):
        print(st,kbo,label,"404"); continue
    y5=yb.get("2025",{})
    print(st,kbo,(title or "")[:65],"fte",fte,"filed",filed,"nace",n87[:2] or nbad[:2],"Y5",y5 if y5 else "NO")
    if st=="FREE" and y5 and not (nbad and not n87):
        omzet=(y5.get("omzet") or "").replace(",","")
        bruto=(y5.get("bruto_marge") or "").replace(",","")
        o=int(omzet) if omzet.isdigit() else 0
        b=int(bruto) if bruto.isdigit() else 0
        if o>=200000 or b>=200000:
            print("  >>> TAKE")
