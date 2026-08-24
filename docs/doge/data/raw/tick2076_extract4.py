import re
from pathlib import Path
t = Path(r"docs/doge/data/raw/tick2075/kuurne_en.html").read_text(encoding="utf-8", errors="replace")
idx = t.find("220.5")
print("220.5 contexts:")
while idx >= 0:
    print(re.sub(r"\s+", " ", t[max(0,idx-120):idx+120]))
    print("---")
    idx = t.find("220.5", idx+1)
    if idx > 0 and t.find("220.5", idx) > idx+50000:
        break
# also search 220,5
idx = t.find("220,5")
print("220,5 contexts:")
while idx >= 0:
    print(re.sub(r"\s+", " ", t[max(0,idx-120):idx+120]))
    print("---")
    idx = t.find("220,5", idx+1)
