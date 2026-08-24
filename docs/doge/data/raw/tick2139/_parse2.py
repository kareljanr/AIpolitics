from pathlib import Path
import re
for name in ["denderrust_cw_en.html","denderrust_kbo.html","denderrust_site.html","0419333572_zorgcampus_denderrust.html"]:
    p=Path("docs/doge/data/raw/tick2139")/name
    if not p.exists():
        print("missing", name); continue
    t=p.read_text(encoding="utf-8", errors="replace")
    print("====", name)
    # print lines with key numbers
    for pat in ["47.586","47,586","47586","12.099","11.135","8.526","Personeel","FTE","9087","Adres","straat","Aalst","email","@","Actief","VZW","vestiging","Enterprise","Legal form","filed","03-06","neerlegging","Principal","nursing","WZC","87."]:
        if pat in t or pat.lower() in t.lower():
            pass
    # extract store/finance JSON chunks around personeel
    for m in re.finditer(r".{0,40}(personeel|fte|9087).{0,80}", t, re.I):
        s=m.group(0).replace("\n"," ")
        if any(c.isdigit() for c in s):
            print(" ", s[:140])
    # KBO specific
    if "kbo" in name:
        for m in re.finditer(r"(Status|Adres|Rechtsvorm|Naam|Vestiging|Nace|email|E-mail|Ondernemingsnummer).{0,200}", t, re.I|re.S):
            print("KBO", re.sub(r"\s+"," ", m.group(0))[:220])
    if "site" in name:
        for m in re.finditer(r"(mailto:[^\s\"'<>]+|info@[^\s\"'<>]+|contact[^\s\"'<>]{0,40}|[0-9]{2,4}[./ ][0-9. ]{5,}|Denderrust|Aalst|WZC).{0,60}", t, re.I):
            print("SITE", re.sub(r"\s+"," ", m.group(0))[:180])
# EN page finance values displayed
en=Path("docs/doge/data/raw/tick2139/denderrust_cw_en.html").read_text(encoding="utf-8", errors="replace")
# find displayed KPI numbers near labels
for label in ["Turnover","Gross margin","Profit/Loss","Equity","Personnel","employees","Last available"]:
    i=en.lower().find(label.lower())
    if i>=0:
        print("ENCTX", label, re.sub(r"\s+"," ", en[i:i+250])[:250])
