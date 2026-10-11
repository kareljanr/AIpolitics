import re
from pathlib import Path
OUT=Path("/workspace/AIpolitics/docs/doge/raw/tick2473")
for name in ["pardoes_kbo.html","pardoes_kbo_ve.html"]:
    html=(OUT/name).read_text(encoding="utf-8", errors="replace")
    text=re.sub(r"<script[\s\S]*?</script>"," ",html,flags=re.I)
    text=re.sub(r"<[^>]+>"," ",text)
    text=re.sub(r"&nbsp;"," ",text)
    text=re.sub(r"[ \t]+"," ",text)
    text=re.sub(r"\n\s*\n","\n",text)
    (OUT/name.replace(".html",".txt")).write_text(text)
    print("====", name)
    for line in text.splitlines():
        l=line.strip()
        if l and len(l)<220:
            if any(k in l.lower() for k in ["status","actief","adres","zetel","vestig","naam","rechtsvorm","e-mail","mail","telefoon","rsz","nace","toelating","kinder","begindatum","datum","2800","mechelen","tervuur","aantal","eenheid","2.","website","webadres"]):
                print(l)
