import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"

# Fix loop_state notes to ASCII-safe Eveque
path = DATA / "loop_state.csv"
with open(path, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fields = reader.fieldnames
    rows = list(reader)
notes = rows[0]["notes"]
notes = re.sub(r"Fontaine-l'[^ ;,]{0,30}que", "Fontaine-l'Eveque", notes)
rows[0]["notes"] = notes
with open(path, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state:", rows[0]["notes"][:160])

# Spot-check key CSVs still have correct entity strings
for fn, key, val in [
    ("entities.csv", "entity_id", "bv_mrs_le_hanois_fontaine_leveque"),
    ("foi_queue.csv", "gap_id", "gap_le_hanois_nbb_pdf_assets_debt_omzet_empty_bellechasse_absorption_matrix_l5"),
    ("research_queue.csv", "task_id", "rq_2157"),
]:
    with open(DATA / fn, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    hit = [r for r in rows if r.get(key) == val]
    print(fn, key, val, "OK" if hit else "MISSING", hit[0].get("status", hit[0].get("name_nl", ""))[:60] if hit else "")
