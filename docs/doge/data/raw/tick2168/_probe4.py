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
    nace_bad=re.findall(r"(?:68|55)\.\d{3}", t or "")[:4]
    return yb, fte.group(1) if fte else None, filed.group(1) if filed else None, title.group(1) if title else None, nace87, nace_bad

CANDS=[
("0416337262","vrijzicht_ieper"),
("0418016550","st_vincentius_antwerpen"),
("0449425546","wijtshage_rumst"),
("0448190181","sint_jozef_rumst"),
("0463758978","huize_vincent_temse"),
("0787300696","melis_home"),
("0450755634","oudenburg_skip"),
# more Walloon MRS / leftover names from historical
("0408.123.456","x"),
("0425.861.473","le_castel_guess"),
("0438.521.679","bethanie_guess"),
("0441.258.963","passerinette_guess"),
("0452.187.639","seigneurie_guess"),
("0462.871.549","ry_chevreuil"),
("0471.852.036","seniservices"),
("0482.156.739","progres"),
("0405.218.763","cfs"),
("0412.587.639","elisabeth"),
("0423.156.879","near"),
("0435.218.769","chateau_vert_huy_mined_check"),
("0448.033.201","chateau_vert"),
("0409.587.123","slgw"),
("0413.796.456","cand_from2144"),
("0416.528.391","prestige_mined"),
("0479.984.011","peupliers_mined"),
# open_page names: Home Vrijzicht etc already above
("0428.571.639","extra_a"),
("0437.852.169","extra_b"),
("0446.258.739","extra_c"),
("0457.821.639","extra_d"),
("0468.257.139","extra_e"),
("0475.821.639","extra_f"),
("0486.257.139","extra_g"),
("0867.521.439","extra_h"),
("0825.671.439","extra_i"),
("0756.821.439","extra_j"),
("0697.521.439","extra_k"),
("0546.821.439","extra_l"),
("0501.258.739","extra_m"),
("0402.158.739","extra_n"),
("0415.287.639","extra_o"),
("0426.158.739","extra_p"),
("0438.257.169","extra_q"),
("0449.158.739","extra_r"),
("0451.287.639","extra_s"),
("0463.158.739","extra_t"),
("0474.287.639","extra_u"),
("0485.158.739","extra_v"),
]
for kbo,label in CANDS:
    kbo=re.sub(r"\D","",kbo)
    if len(kbo)!=10: continue
    st="MINED" if kbo in mined else "FREE"
    t=fetch(f"https://www.companyweb.be/en/{kbo}", out/f"{label}_{kbo}_en.html")
    if not t: continue
    yb,fte,filed,title,n87,nbad=parse(t)
    if "Error 404" in (title or ""):
        print(st,kbo,label,"404"); continue
    y5=yb.get("2025",{})
    print(st,kbo,(title or "")[:70],"fte",fte,"filed",filed,"nace", (n87 or nbad)[:2], "Y5", y5 if y5 else "NO")
    if st=="FREE" and y5 and not (nbad and not n87):
        omzet=(y5.get("omzet") or "").replace(",","")
        bruto=(y5.get("bruto_marge") or "").replace(",","")
        o=int(omzet) if omzet.isdigit() else 0
        b=int(bruto) if bruto.isdigit() else 0
        w=re.sub(r"[^\d-]","", y5.get("winst") or "0")
        wi=int(w) if w not in ("","-") else 0
        if o>=150000 or b>=150000 or abs(wi)>=50000:
            print("  >>> TAKE THIS")
