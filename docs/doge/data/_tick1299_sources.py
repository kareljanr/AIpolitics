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
    {"source_id":"src_agbktn_jr2025_bbc","title":"AGB Kortenaken BBC jaarrekening 2025 (PDF 71p)","url":"https://www.kortenaken.be/sites/default/files/2026-05/20260528_VASTSTELLING-BBC-JAARREKENING-AGB.pdf","publisher":"Autonoom Gemeentebedrijf Kortenaken","accessed_date":"2026-08-17","source_class":"budget","notes":"tick1299; 2.83MB BBC PDF kortenaken.be 71p; RVB 28.05.2026; pub 29.05.2026; KBO 0535.811.469; assets 3.479m fin debt 3.281m leasing 3.216m city prijssub 0.157m gecorr AFM -0.209m"},
    {"source_id":"src_agbktn_jr2025_rvb","title":"AGB Kortenaken RVB 28.05.2026 vaststelling JR2025","url":"https://www.kortenaken.be/sites/default/files/2026-05/20260528_VASTSTELLING-BBC-JAARREKENING-AGB_RVB.pdf","publisher":"Raad van bestuur AGB Kortenaken","accessed_date":"2026-08-17","source_class":"official_register","notes":"tick1299; JR2025 vaststelling RVB 28.05.2026 pub 29.05.2026; AFM 9171 / BBR 9171 / avail 94988 / PnL 15431 / winstuitkering 10000; voorzitter Niels Willems; city GE JR2025 also live left for later unit"},
    {"source_id":"src_kbo_agbktn_0535811469","title":"KBO Autonoom Gemeentebedrijf Kortenaken 0535.811.469","url":"https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0535811469","publisher":"KBO Public Search FOD Economie","accessed_date":"2026-08-17","source_class":"official_register","notes":"tick1299; AGB KBO 0535.811.469; seat Dorpsplein 35 3470; 1 VE; voorzitter Niels Willems / AD Dominique Hayen / FD Eddy Jacobs; city sibling 0207.520.711 / OCMW 0212.189.379 (kortenaken.be contact)"},
])
print("sources", n)
