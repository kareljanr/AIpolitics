from pathlib import Path
txt=Path("/workspace/AIpolitics/docs/doge/raw/tick2473/pardoes-2026-00295237.txt").read_text()
pages=txt.split("\f")
print("NPAGES", len(pages))
for i,p in enumerate(pages,1):
    head=p.strip().splitlines()[0][:80] if p.strip() else ""
    print(f"--- p{i} {len(p)} {head}")

# dump pages that likely have numbers: typically 3-8
for i in [3,4,5,6,7,8,9]:
    if i<=len(pages):
        print(f"\n========== PAGE {i} ==========")
        print(pages[i-1])
