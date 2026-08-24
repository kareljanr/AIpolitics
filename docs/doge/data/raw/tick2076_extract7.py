from pathlib import Path
t = Path(r"docs/doge/data/raw/tick2075/kuurne_en.html").read_text(encoding="utf-8", errors="replace")
idx = t.find("Average number of staff")
print(t[idx-1500:idx+200])
