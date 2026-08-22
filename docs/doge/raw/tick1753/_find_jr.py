import re
from pathlib import Path

out = Path("docs/doge/raw/tick1753")
for fn in [
    "zzo_zoneraad.html",
    "zzo_zr_college.html",
    "zzo_tag2026.html",
    "zzo_beg2026.html",
]:
    html = (out / fn).read_text(encoding="utf-8")
    hrefs = re.findall(r'href=["\']([^"\']+)["\']', html)
    for h in hrefs:
        if re.search(r"jaar|reken|2025|begrot|/s/|februari|27", h, re.I):
            print("H", fn, h[:200])
    # collection items titles
    for m in re.finditer(
        r"(Jaarrekening[^<]{0,80}|Begroting[^<]{0,80}|Lijst zoneraad[^<]{0,80})",
        html,
        re.I,
    ):
        print("T", fn, re.sub(r"\s+", " ", m.group(0))[:160])
