from pathlib import Path
import re
t = Path(r"docs/doge/data/raw/tick2075/kuurne_en.html").read_text(encoding="utf-8", errors="replace")
idx = t.find("220.5")
print(t[idx-800:idx+400])
# also check for personnel by year
for m in re.finditer(r"220\.5|215[,.]9|personeelsbestand|Average number", t, re.I):
    print("at", m.start(), re.sub(r"\s+"," ", t[m.start()-60:m.start()+80])[:160])
