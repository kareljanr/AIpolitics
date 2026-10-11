# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
def append_rows(path, new_rows):
    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        existing = {row.get(fields[0]) for row in reader}
    added = 0
    with open(path, "a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        for row in new_rows:
            if row.get(fields[0]) in existing:
                continue
            w.writerow({k: row.get(k, "") for k in fields})
            added += 1
    return added
n = append_rows(DATA/"sources.csv", [
    {"source_id":"src_diepbk_jr2025_bbc","title":"Lokaal Bestuur Diepenbeek BBC jaarrekening 2025 (PDF 122p)","url":"https://www.diepenbeek.be/file_uploads/42819.pdf?sc=F808981DD9F273563DAD49F3E75B762A","publisher":"Gemeente en OCMW Diepenbeek","accessed_date":"2026-08-17","source_class":"budget","notes":"tick1297; 7.98MB BBC PDF diepenbeek.be file_uploads/42819; GR 22.06.2026; KBO 0207.465.974/0212.246.787; assets 190.496m fin debt 13.592m IGS reval 19.425m OCMW equity -0.708m NEG AFM +5.047m avail 21.858m"},
    {"source_id":"src_diepbk_jr2025_gr","title":"Diepenbeek GR 22.06.2026 vaststelling JR2025 deel gemeente","url":"https://www.diepenbeek.be/file_uploads/42816.pdf?sc=DB6EB9B961D2402B1084C068852A8E92","publisher":"Gemeenteraad Diepenbeek","accessed_date":"2026-08-17","source_class":"official_register","notes":"tick1297; JR2025 vaststelling GR 22.06.2026 2026_GR_00085; pub 24.06.2026; unanimiteit; AD Jan Dreesen; burgemeester Rik Kriekels"},
    {"source_id":"src_kbo_diepbk_0207465974","title":"KBO Gemeente Diepenbeek 0207.465.974","url":"https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0207465974","publisher":"KBO Public Search FOD Economie","accessed_date":"2026-08-17","source_class":"official_register","notes":"tick1297; city since 01.01.1968; seat Dorpsstraat 14 3590; 14 VE; burgemeester Rik Kriekels since 01.01.2019; AD Jan Dreesen since 15.04.2024 / FD Monique Aerts; OCMW sibling 0212.246.787 (4 VE; voorzitter Kriekels); email info@diepenbeek.be; NIS 71011"},
])
print("sources", n)
