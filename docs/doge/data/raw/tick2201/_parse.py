import re
import html as H
from pathlib import Path

out = Path("docs/doge/data/raw/tick2201")
html = (out / "mwp_en.html").read_text(encoding="utf-8", errors="replace")
text = re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", html)))
print("TITLE", re.search(r"<title>([^<]+)", html).group(1))
print("YEAR", re.search(r"Last balance sheet year (20\d\d)", text).group(1))

pat = (
    r"20(25|24)\s*:\s*\{\s*winst:\s*\"([^\"]+)\"\s*,\s*eigen_vermogen:\s*\"([^\"]+)\""
    r"\s*,\s*bruto_marge:\s*\"([^\"]+)\"\s*,\s*omzet:\s*\"([^\"]+)\""
)
for m in re.finditer(pat, html, re.S):
    print("KERN", m.group(1), m.groups()[1:])

fte = re.search(r'amountOfEmployees\s*=\s*"([^"]+)"', html)
print("FTE", fte.group(1) if fte else None)

for p in [
    r"filed on ([0-9\-]+)",
    r"neergelegd op ([0-9\-]+)",
    r"The most recent financial statements.*?filed on ([0-9\-]+)",
    r"neerlegging.*?([0-9]{2}[./\-][0-9]{2}[./\-][0-9]{4})",
]:
    mm = re.search(p, text, re.I)
    if mm:
        print("FILING", p[:30], mm.group(1))

emails = set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", html))
print("EMAILS", emails)

idx = text.find("Financial data")
print("FIN", text[idx : idx + 900] if idx >= 0 else "none")

# NL for filing
nl = (out / "mwp_nl.html").read_text(encoding="utf-8", errors="replace")
nlt = re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", nl)))
for p in [
    r"neergelegd op ([0-9\-]+)",
    r"De meest recente jaarrekening.*?neergelegd op ([0-9\-]+)",
    r"neerlegging.*?([0-9]{2}[./\-][0-9]{2}[./\-][0-9]{4})",
]:
    mm = re.search(p, nlt, re.I)
    if mm:
        print("NL_FILING", p[:40], mm.group(1))

kbo = (out / "kbo.html").read_text(encoding="utf-8", errors="replace")
kt = re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", kbo)))
start = kt.find("Ondernemingsnummer")
print("KBO", kt[start : start + 1500])
