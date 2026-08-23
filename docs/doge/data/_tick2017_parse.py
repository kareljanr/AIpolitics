import re
from pathlib import Path

t = Path("docs/doge/data/raw/tick2017/kbo.html").read_text(encoding="utf-8", errors="replace")
for lab in [
    "Juridische vorm",
    "Start van de rechtspersoon",
    "Maatschappelijke naam",
    "Ondernemingsnummer",
]:
    i = t.find(lab)
    if i >= 0:
        print(lab, repr(t[i : i + 280].replace("\t", " ").replace("\n", " ")[:240]))

tn = Path("docs/doge/data/raw/tick2017/az_rivierenland_nl.html").read_text(
    encoding="utf-8", errors="replace"
)
blocks = re.findall(
    r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
    tn,
)
print("n_blocks", len(blocks))
print("y0", blocks[0] if blocks else None)
print("y1", blocks[1] if len(blocks) > 1 else None)
print("FTE nl", re.findall(r"[Ww]erknemers\s*=\s*\"([^\"]+)\"", tn)[:2])
print("Employees", re.findall(r'Employees\s*=\s*"([^"]+)"', tn)[:2])
