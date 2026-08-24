# -*- coding: utf-8 -*-
import csv, re, ssl, urllib.request, urllib.parse
from pathlib import Path
csv.field_size_limit(10**7)
ctx=ssl.create_default_context()
UA={"User-Agent":"Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out=Path("docs/doge/data/raw/tick2168"); out.mkdir(parents=True, exist_ok=True)
mined=set()
for path in ["docs/doge/data/entities.csv","docs/doge/data/commitments.csv","docs/doge/data/leaderboard.csv"]:
    with open(path,newline="",encoding="utf-8") as f:
        for row in csv.DictReader(f):
            blob=re.sub(r"[.\s]"," "," ".join(str(v) for v in row.values()))
            for m in re.findall(r"\d{10}", re.sub(r"\D","",blob) if False else re.sub(r"[.\s]","", " ".join(str(v) for v in row.values()))):
                mined.add(m)

def fetch(url, path):
    try:
        req=urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, context=ctx, timeout=30) as r:
            data=r.read()
        path.write_bytes(data)
        return data.decode("utf-8","ignore")
    except Exception as e:
        print("FAIL", path.name, e.__class__.__name__, str(e)[:80])
        return None

def parse(t):
    yblocks={}
    for y, body in re.findall(r"(20\d\d)\s*:\s*\{([^{}]+)\}", t or ""):
        def g(k,b=body):
            m=re.search(rf'{k}:\s*"([^"]*)"',b)
            return m.group(1) if m else None
        yblocks[y]={k:g(k) for k in ["omzet","winst","bruto_marge","eigen_vermogen"]}
    fte=re.search(r"([\d.,]+)\s*FTE", t or "")
    filed=re.search(r"filed on ([0-9-]{10})", t or "")
    title=re.search(r"<title>([^<]+)", t or "")
    nace87=re.findall(r"87\.\d{3}", t or "")[:5]
    nace_bad=re.findall(r"(?:68|55)\.\d{3}", t or "")[:4]
    return yblocks, fte.group(1) if fte else None, filed.group(1) if filed else None, title.group(1) if title else None, nace87, nace_bad

# Northdata / CW name search via duck-like: try companyweb search pages
queries=[
 "https://www.companyweb.be/nl/search?q=woonzorgcentrum",
 "https://www.northdata.com/search?q=woonzorgcentrum+Belgium+2025",
]
# Better: try known Anima Care homes from site + common FREE lists from tick notes
NAMES_KBO = [
    # from anima group public list / common leftover
    ("0472.615.953","huize_van_niel"), # guess may 404
    ("0465.723.491","residentie_ter_linde"),
    ("0438.687.654","bad"),
    ("0425.123.789","bad2"),
    ("0405.406.887","bad3"),
    ("0865.574.649","fakkel_mined_check"),
    ("0827.850.260","care_support_mined"),
    ("0413.550.491","restel_mined"),
    ("0458.352.318","orchidee_mined"),
    ("0446.222.962","olv_armen_mined"),
    ("0414.747.056","cigb_mined"),
    ("0454.712.838","comte_mined"),
    ("0479.984.011","peupliers_mined"),
    ("0409.232.013","esplanade_mined"),
    ("0440.737.514","corolles_mined"),
    ("0416.528.391","prestige_mined"),
    ("0466.114.791","en_famille_mined"),
    ("0419.333.572","denderrust_campus"),
    ("0409.698.009","denderrust_dg_mined"),
    ("0422.923.859","care_ion_mined"),
    ("0420.607.638","zonnelied_mined"),
    ("0895.366.220","annuntiaten_mined"),
    ("0409.583.092","sint_felix_mined"),
    ("0861.157.387","eycken_mined"),
    ("0421.479.153","hanois_mined"),
    ("0452.587.548","parc_forest_mined"),
    ("0447.771.695","epinette_mined"),
    ("0435.015.702","lindeboom_mined"),
    ("0845.895.824","hertog_jan_mined"),
    ("0446.022.331","lork_geel_mined"),
    ("0433.440.342","olv_kempen_mined"),
    ("0500.952.540","wznd_mined"),
    ("0412.886.636","boterlaar_mined"),
    ("0423.571.581","salvator_mined"),
    ("0473.694.748","ruggeveld_mined"),
    ("0432.582.485","bernardus_mined"),
    # new guesses / adjacent
    ("0478.350.612","guess1"),
    ("0430.215.789","guess2"),
    ("0461.852.347","guess3"),
    ("0417.958.152","sint_camillus_mined_check"),
    ("0445.175.263","zilverlinde_check"),
    ("0452.865.383","sint_jozef_ninove_check"),
    ("0787.300.696","melis_home"),
    ("0410.219.433","haagwinde"),
    ("0480.566.704","hof_ter_lande"),
    ("0443.249.616","stil_geluk"),
    ("0466.266.429","helianthus"),
    ("0422.620.585","sint_vincentius_erpe"),
    ("0441.675.147","wsr_bruxelles"),
    ("0685.516.024","woonzorgnetwerk_edegem"),
    ("0598.966.387","hoeksteen"),
]

# Also scrape anima.be homes if possible
anima=fetch("https://animagroup.be/", out/"anima_home.html")
if anima:
    for m in re.findall(r"0\d{3}[.\s]?\d{3}[.\s]?\d{3}", anima):
        d=re.sub(r"\D","",m)
        if len(d)==10:
            NAMES_KBO.append((f"{d[:4]}.{d[4:7]}.{d[7:]}", "anima_site"))
    print("anima site kbOs found", len(re.findall(r"0\d{3}", anima)))

# Companyweb search pages (NL)
for q in ["woonzorgcentrum","rusthuis","maison de repos","MRS"]:
    url=f"https://www.companyweb.be/nl/search?q={urllib.parse.quote(q)}"
    t=fetch(url, out/f"cw_search_{q.replace(' ','_')}.html")
    if t:
        found=re.findall(r"/nl/(0\d{9})/", t)
        print("search", q, "hits", len(set(found)), list(set(found))[:15])
        for d in set(found):
            NAMES_KBO.append((f"{d[:4]}.{d[4:7]}.{d[7:]}", f"search_{q[:8]}"))

seen=set(); strong=[]
for kbo_dot,label in NAMES_KBO:
    kbo=re.sub(r"\D","",kbo_dot)
    if len(kbo)!=10 or kbo in seen: continue
    seen.add(kbo)
    status="MINED" if kbo in mined else "FREE"
    t=fetch(f"https://www.companyweb.be/en/{kbo}", out/f"p_{kbo}_en.html")
    if not t: continue
    yb,fte,filed,title,nace87,nace_bad=parse(t)
    if "Error 404" in (title or ""):
        continue
    y5=yb.get("2025",{})
    if not y5: 
        if status=="FREE":
            print("FREE-noY5", kbo, (title or "")[:55], "filed", filed)
        continue
    print(status, kbo, (title or "")[:60], "fte", fte, "filed", filed, "nace", nace87[:2] or nace_bad[:2], y5)
    if status!="FREE":
        continue
    if nace_bad and not nace87:
        print("  skip bad nace")
        continue
    omzet=(y5.get("omzet") or "").replace(",","")
    bruto=(y5.get("bruto_marge") or "").replace(",","")
    w=re.sub(r"[^\d-]","", y5.get("winst") or "0")
    o=int(omzet) if omzet.isdigit() else 0
    b=int(bruto) if bruto.isdigit() else 0
    wi=int(w) if w not in ("","-") else 0
    if o>=150000 or b>=150000 or abs(wi)>=40000:
        strong.append((kbo,title,y5,fte,filed,nace87))
        print("  >>> CAND")
print("STRONG", len(strong))
for s in strong:
    print(s)
