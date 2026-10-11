import re, json, datetime
from pathlib import Path
from uuid import UUID
OUT=Path("/workspace/AIpolitics/docs/doge/raw/tick2473")

def uuid_time(u):
    try:
        x=UUID(u)
        if x.version!=1:
            return f"v{x.version}"
        ts = (x.time - 0x01b21dd213814000) / 1e7
        return datetime.datetime.utcfromtimestamp(ts).isoformat()+"Z"
    except Exception as e:
        return str(e)

ids=json.loads((OUT/"tsas_ids.json").read_text())
print("UUID times:")
for x in ids:
    print(x["id"], x["importFileType"], "mig", x["migration"], "->", uuid_time(x["id"]))

# KBO parse
kbo=(OUT/"tsas_kbo.html").read_text(encoding="utf-8", errors="replace")
print("\n==== KBO snippets ====")
# strip tags lightly
text=re.sub(r"<script[\s\S]*?</script>"," ",kbo,flags=re.I)
text=re.sub(r"<style[\s\S]*?</style>"," ",text,flags=re.I)
text=re.sub(r"<[^>]+>"," ",text)
text=re.sub(r"[ \t]+"," ",text)
text=re.sub(r"\n\s*\n","\n",text)
(OUT/"tsas_kbo.txt").write_text(text)
# print useful lines
for line in text.splitlines():
    l=line.strip()
    if not l: continue
    if any(k in l.lower() for k in ["status","actief","adres","zetel","vestig","naam","rechtsvorm","e-mail","mail","telefoon","rsz","nace","toelating","kinder","begindatum","datum","9470","dender","nayer","aantal","eenheid"]):
        print(l[:200])

print("\n==== SBM snippets ====")
sbm=(OUT/"tsas_sbm.html").read_text(encoding="latin-1", errors="replace")
text=re.sub(r"<script[\s\S]*?</script>"," ",sbm,flags=re.I)
text=re.sub(r"<[^>]+>"," ",text)
text=re.sub(r"[ \t]+"," ",text)
(OUT/"tsas_sbm.txt").write_text(text)
refs=re.findall(r"20[12][0-9]-[0-9]{8}", sbm)
print("refs", refs)
for line in text.splitlines():
    l=line.strip()
    if not l: continue
    if any(k in l.lower() for k in ["2024","2025","2026","jaarrekening","neerlegg","boekjaar","model","vkt","vol","pdf"]):
        if len(l)<240:
            print(l)
