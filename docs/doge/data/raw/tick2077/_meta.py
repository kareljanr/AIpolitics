# Extract De Zwaluw entity metadata from CW + KBO HTML
import re
from pathlib import Path

RAW = Path(__file__).parent

for name in ["zwaluw_en.html", "zwaluw_nl.html", "kbo.html"]:
    t = (RAW / name).read_text(encoding="utf-8", errors="replace")
    print("====", name)
    # address-like
    for pat in [
        r'itemprop="address"[^>]*>(.*?)</',
        r'itemprop="streetAddress"[^>]*>(.*?)</',
        r'itemprop="postalCode"[^>]*>(.*?)</',
        r'itemprop="addressLocality"[^>]*>(.*?)</',
        r'mailto:([^"\'>\s]+)',
        r'tel:([^"\'>\s]+)',
        r'https?://(?!www\.companyweb)([^"\'>\s]+)',
        r"Pajottegem[^<{]{0,80}",
        r"1570[^<{]{0,80}",
        r"nursing homes[^<{]{0,80}",
        r"woon[- ]?zorg[^<{]{0,80}",
        r"rusthuis[^<{]{0,80}",
        r"Principal activity.{0,200}",
        r"Hoofdactiviteit.{0,200}",
        r"Start date.{0,120}",
        r"Oprichtingsdatum.{0,120}",
        r"filed on[^<{]{0,40}",
        r"neergelegd op[^<{]{0,40}",
    ]:
        ms = re.findall(pat, t, re.I | re.S)
        if ms:
            print(pat[:40], "=>", [re.sub(r"\s+", " ", str(m))[:120] for m in ms[:4]])

# Print address block from EN
t = (RAW / "zwaluw_en.html").read_text(encoding="utf-8", errors="replace")
idx = t.find("Pajottegem")
print("\nPajottegem ctx:", t[max(0, idx - 300) : idx + 200].replace("\n", " ")[:500])
idx = t.find("Activities of nursing")
print("\nActivity ctx:", t[max(0, idx - 100) : idx + 200].replace("\n", " ")[:400])
# employees as FTE
print("\nEmployees row again from NL")
tn = (RAW / "zwaluw_nl.html").read_text(encoding="utf-8", errors="replace")
m = re.search(
    r"Personeel|Werknemers|Employees.{0,200}?</td>\s*((?:<td[^>]*>.*?</td>\s*){1,12})",
    tn,
    re.S | re.I,
)
if m:
    cells = m.group(1)
    print(re.findall(r">\s*([0-9]+(?:[,\.][0-9]+)?)\s*<", cells)[:20])
