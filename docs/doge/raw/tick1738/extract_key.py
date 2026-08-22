from pathlib import Path

t = Path("docs/doge/raw/tick1738/colisee_extract.txt").read_text(encoding="utf-8")
parts = t.split("===== PAGE")
for i in range(8, 12):
    if i < len(parts):
        print("---PAGE", i)
        print(parts[i][:2500])
        print("====")
# audit opinion amount
for i in range(44, 49):
    if i < len(parts):
        print("---PAGE", i)
        print(parts[i][:2000])
        print("====")
