# tick 2258 helpers — refine Val du Geer filing date + equity field + Nekto collision check
import re
from pathlib import Path

RAW = Path(__file__).resolve().parent / "raw" / "tick2257"
html = (RAW / "valdugeer_en.html").read_text(encoding="utf-8", errors="replace")
for key in ["omzet", "bruto_marge", "winst", "eigen_vermogen", "fte", "personeelsbestand"]:
    ms = re.findall(key + r'\s*:\s*"([^"]+)"', html)
    print(key, ms[:6])

text = re.sub(r"<[^>]+>", " ", html)
text = re.sub(r"\s+", " ", text)
for lab in ["Filing date", "filed", "Publication", "17-03-2026", "neerlegging", "deposit"]:
    i = text.lower().find(lab.lower())
    if i >= 0:
        print("near", lab, text[i : i + 220])

# publications block
m = re.search(r"Publications from Val Du Geer(.{0,500})", text, re.I)
if m:
    print("PUBS", m.group(1)[:400])

kbo = (RAW / "valdugeer_kbo.html").read_text(encoding="utf-8", errors="replace")
kt = re.sub(r"<[^>]+>", " ", kbo)
kt = re.sub(r"\s+", " ", kt)
# NACE adapted work
for m in re.finditer(r"88\.\d+|Adapted|beschut|travail adapt|sociale werkplaats", kt, re.I):
    print("NACE-ish", kt[m.start() : m.start() + 120])
