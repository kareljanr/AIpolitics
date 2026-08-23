# -*- coding: utf-8 -*-
import re
import glob
from pathlib import Path

PAT = re.compile(
    r'(20\d\d)\s*:\s*\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)"'
)
OLD = Path(__file__).resolve().parent.parent / "tick2095"
for p in sorted(OLD.glob("*.html")):
    t = p.read_text(encoding="utf-8", errors="ignore")
    ye = re.search(r"kernCijfers\s*=\s*\{\s*(20\d\d)", t)
    first = PAT.search(t)
    title = re.search(r"<title>([^<]+)</title>", t)
    fte = re.search(r'amountOfEmployees\s*=\s*"([^"]+)"', t)
    tit = (re.sub(r"\s+", " ", title.group(1)).strip() if title else "?")[:70]
    y = ye.group(1) if ye else None
    print(p.name, "YE", y, tit)
    if first:
        print(" ", first.groups(), "fte", fte.group(1) if fte else None)
