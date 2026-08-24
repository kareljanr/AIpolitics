# -*- coding: utf-8 -*-
import urllib.request, re, ssl
from pathlib import Path
ctx=ssl.create_default_context()
ua={"User-Agent":"Mozilla/5.0"}
def get(url):
    req=urllib.request.Request(url, headers=ua)
    with urllib.request.urlopen(req, context=ctx, timeout=35) as r:
        return r.read().decode("utf-8","replace")
text=Path("docs/doge/data/entities.csv").read_text(encoding="utf-8",errors="replace").lower()
lb=Path("docs/doge/data/leaderboard.csv").read_text(encoding="utf-8",errors="replace").lower()
blob=text+lb
cands=[
 ("huize_sion","0430737705","https://www.companyweb.be/en/0430737705/huize-sion"),
 ("emeis_belgium","0887690451","https://www.companyweb.be/en/0887690451/emeis-belgium"),
 ("seniors_care_ion","0422923859","https://www.companyweb.be/en/0422923859/seniors-care-ion"),
 ("zusters_berlaar","0417703081","https://www.companyweb.be/en/0417703081/zorggroep-zusters-van-berlaar"),
 ("veilige_have","0449507205","https://www.companyweb.be/en/0449507205/woonzorgcentrum-veilige-have"),
 ("christine","0421903676","https://www.companyweb.be/en/0421903676/woonzorgcentrum-christine"),
 ("zilverbos","0644984078","https://www.companyweb.be/en/0644984078/woonzorgcentrum-zilverbos"),
 ("residence_du_heysel","0401968196","https://www.companyweb.be/en/0401968196/residence-du-heysel"),
 # more from web-like names
 ("kalvermarkt","0441313178","https://www.companyweb.be/en/0441313178/kalvermarkt"),
]
for name,digits,url in cands:
    dotted=digits[:4]+"."+digits[4:7]+"."+digits[7:]
    mined = digits in blob or dotted in blob or name.replace("_"," ") in blob
    try:
        h=get(url)
        title=re.search(r"<title>([^<]+)", h)
        years=re.findall(r"\n(202[0-9])\s*:", h)
        m=re.search(r"Last balance sheet year[^0-9]*([0-9]{4})", h, re.I)
        print("===", name, "mined", mined, "years", years[:5], "last", m.group(1) if m else None)
        print("   ", (title.group(1) if title else "")[:90])
        if years and years[0]=="2025":
            mm=re.search(r"2025\s*:\s*\{([^}]+)\}", h)
            print("    2025", re.sub(r"\s+"," ", mm.group(1))[:300] if mm else None)
            mm=re.search(r"2024\s*:\s*\{([^}]+)\}", h)
            print("    2024", re.sub(r"\s+"," ", mm.group(1))[:300] if mm else None)
            fte=re.search(r'Employees\s*=\s*"([^"]+)"', h)
            filed=re.search(r"filed on ([0-9\-]+)", h, re.I)
            print("    fte", fte.group(1) if fte else None, "filed", filed.group(1) if filed else None)
    except Exception as e:
        print(name, "ERR", e)
