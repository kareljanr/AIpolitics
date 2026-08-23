from pathlib import Path
import re

t = Path("docs/doge/data/raw/tick2008/azo_kbo.html").read_text(encoding="utf-8", errors="replace")
text = re.sub(r"<[^>]+>", " ", t)
text = re.sub(r"\s+", " ", text)
for kw in [
    "E-mail",
    "Status",
    "Actief",
    "0800",
    "Oostende",
    "Aanbested",
    "vestiging",
    "Rechtsvorm",
    "Web",
    "Begin",
]:
    i = text.lower().find(kw.lower())
    if i >= 0:
        print(kw, ":", text[max(0, i - 30) : i + 140])

t2 = Path("docs/doge/data/raw/tick2008/azo_nl.html").read_text(encoding="utf-8", errors="replace")
blocks = re.findall(
    r'winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)"',
    t2,
)
print("nl blocks", blocks[:2])
site = Path("docs/doge/data/raw/tick2008/azo_site.html").read_text(encoding="utf-8", errors="replace")
emails = sorted(set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", site)))
print("site emails", emails[:15])
print("azoostende" in site.lower(), "azo.be" in site.lower())
