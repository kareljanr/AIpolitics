import re
from pathlib import Path

base = Path(__file__).resolve().parent.parent / "tick2155"
for name in ["aiesh_en.html", "rew_en.html", "faro_en.html"]:
    t = (base / name).read_text(encoding="utf-8", errors="replace")
    be = re.search(r"BE\s*0?\d{3}[\.\s]?\d{3}[\.\s]?\d{3}", t)
    yr = re.search(
        r"Last balance sheet year.*?font-medium[^>]*>\s*(\d{4})", t, re.S | re.I
    )
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", t, re.S | re.I)
    print(
        name,
        be.group(0) if be else None,
        "year",
        yr.group(1) if yr else None,
        re.sub(r"<[^>]+>", "", h1.group(1)).strip()[:60] if h1 else None,
    )
