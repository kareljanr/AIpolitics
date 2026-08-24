import re, csv
from pathlib import Path
csv.field_size_limit(10**7)
# is there dedicated anima hold entity?
with open("docs/doge/data/entities.csv", encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        eid=row.get("entity_id","")
        blob=" ".join((v or "") for v in row.values())
        if "0469.969.453" in blob or "0469969453" in blob or eid.startswith("nv_anima") or "anima hold" in blob.lower() or eid=="anima":
            print("ENT", eid, (row.get("notes") or "")[:160])
with open("docs/doge/data/leaderboard.csv", encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        if "0469969453" in " ".join(row.values()) or "anima hold" in " ".join(row.values()).lower() or "lb_anima_hold" in (row.get("item_id") or ""):
            print("LB", row.get("item_id"))
# parse KBO html
t=Path("docs/doge/data/raw/tick2167/anima_hold_kbo.html").read_text(encoding="utf-8",errors="replace")
print("kbo len", len(t))
# strip tags roughly for key lines
text=re.sub(r"<script[\s\S]*?</script>"," ",t,flags=re.I)
text=re.sub(r"<style[\s\S]*?</style>"," ",text,flags=re.I)
text=re.sub(r"<[^>]+>","\n",text)
lines=[re.sub(r"\s+"," ",l).strip() for l in text.splitlines()]
lines=[l for l in lines if l]
for i,l in enumerate(lines):
    if any(k in l.lower() for k in ["status","actief","anima","juridische","nace","adres","zetel","begindatum","e-mail","telefoon","vestiging","ondernemingsnummer","0469"]):
        print(i, l[:120])
# CW EN more detail - name slug / address / nace from html
t2=Path("docs/doge/data/raw/tick2167/anima_hold_en.html").read_text(encoding="utf-8",errors="replace")
for pat in [r"company_name[^']*'([^']+)'", r"street[^']*'([^']+)'", r"city[^']*'([^']+)'", r"nace_code[^']*'([^']+)'", r"nace_description[^']*'([^']+)'", r"number_of_establishments[^']*'([^']+)'", r"legal_form[^']*'([^']+)'", r"email[^']*'([^']+)'", r"phone[^']*'([^']+)'", r"website[^']*'([^']+)'"]:
    m=re.search(pat,t2,re.I)
    if m: print("CW", pat.split("[")[0], m.group(1)[:100])
# also try JSON-ish
for pat in [r'"name"\s*:\s*"([^"]+)"', r'"vat"\s*:\s*"([^"]+)"']:
    ms=re.findall(pat,t2)[:3]
    if ms: print(pat, ms)
