import csv
import re
from pathlib import Path

csv.field_size_limit(10**7)
with open("docs/doge/data/entities.csv", encoding="utf-8-sig") as f:
    ents = list(csv.DictReader(f))
for e in ents:
    blob = " ".join(str(v or "") for v in e.values())
    if (
        "0869769702" in blob.replace(".", "")
        or "korian belgium" in blob.lower()
        or e.get("entity_id") == "nv_korian_belgium"
    ):
        print("ENT", e.get("entity_id"), (e.get("notes") or "")[:160])

pat = re.compile(
    r'(20\d\d)\s*:\s*\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",'
    r'\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)"'
)
for p in sorted(Path("docs/doge/data/raw/tick2103").glob("korian*")):
    t = p.read_text(encoding="utf-8", errors="ignore")
    years = pat.findall(t)
    print(p.name, "n=", len(years))
    for y in years[:3]:
        print(" ", y)
    m = re.search(r"Laatste balansjaar.{0,240}(\d{4})", t, re.S)
    print(" balans", m.group(1) if m else "?")
    title = re.search(r"<title>([^<]+)", t)
    print(" title", (title.group(1)[:90] if title else "?"))
    fte = re.search(r"Personeel|Employees|werknemers.{0,80}", t, re.I)
    # FTE from company size line
    size = re.search(r"(Groot|Big|Grand)\s*([\d.,]+)\s*FTE", t, re.I)
    print(" size", size.group(0) if size else "?")
