from pathlib import Path
import re
for name in ["aiesh_cw_en.html","rew_cw_en.html","faro_cw_en.html"]:
    t=Path("docs/doge/data/raw/tick2139")/name
    if not t.exists():
        print(name,"missing"); continue
    txt=t.read_text(encoding="utf-8",errors="replace")
    m=re.search(r"2025\s*:\s*\{", txt)
    m4=re.search(r"2024\s*:\s*\{[^}]{0,200}\}", txt)
    filed=re.search(r"filed on [0-9-]+", txt, re.I)
    # enterprise name
    title=re.search(r"<title>([^<]+)", txt)
    print(name, "has2025", bool(m), "filed", filed.group(0) if filed else None, "y2024", (m4.group(0)[:120] if m4 else None), "title", title.group(1)[:60] if title else None)
