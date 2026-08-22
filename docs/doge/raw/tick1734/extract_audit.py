from pathlib import Path

t = Path("docs/doge/raw/tick1734/wzc_sintjozef_extract.txt").read_text(encoding="utf-8")
parts = t.split("===== PAGE")
for i in range(45, min(50, len(parts))):
    print("---PAGE", i)
    print(parts[i][:4000])
    print("====")
