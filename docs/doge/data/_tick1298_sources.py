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
    {"source_id":"src_stnok_jr2025_bbc","title":"Lokaal Bestuur Steenokkerzeel BBC jaarrekening 2025 (PDF 197p)","url":"https://steenokkerzeel-echo.cipalschaubroeck.be/raadpleegomgeving/document/a0726846-bd39-4a94-8ef7-fc64cde7ffa8","publisher":"Gemeente en OCMW Steenokkerzeel","accessed_date":"2026-08-17","source_class":"budget","notes":"tick1298; 24.99MB BBC PDF steenokkerzeel-echo 197p; GR+RMW 18.06.2026; pub 22.06.2026; KBO 0206.561.993/0212.173.345; assets 95.073m fin debt 2.492m IGS reval 9.510m AFM -0.051m avail 9.977m OCMW cum -1.428m NEG"},
    {"source_id":"src_stnok_jr2025_gr","title":"Steenokkerzeel GR 18.06.2026 vaststelling JR2025 deel gemeente","url":"https://steenokkerzeel-echo.cipalschaubroeck.be/raadpleegomgeving/document/3ad72d30-4267-470b-be31-3c6e6d971b74","publisher":"Gemeenteraad Steenokkerzeel","accessed_date":"2026-08-17","source_class":"official_register","notes":"tick1298; JR2025 vaststelling GR+RMW 18.06.2026; pub 22.06.2026; 18 voor / 3 onthoudingen; AD Heidi Abeloos; burgemeester Kurt Ryon; tussenkomst 1.194900m; TAK26 herbelegging 1.027m"},
    {"source_id":"src_kbo_stnok_0206561993","title":"KBO Gemeente Steenokkerzeel 0206.561.993","url":"https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0206561993","publisher":"KBO Public Search FOD Economie","accessed_date":"2026-08-17","source_class":"official_register","notes":"tick1298; city since 23.05.1969; seat Orchideeenlaan 17 1820; 7 VE; burgemeester Kurt Ryon since 01.01.2013; AD Heidi Abeloos since 26.03.2007 / FD Luk Vandeuren; OCMW sibling 0212.173.345 (2 VE; voorzitter Ryon since 01.01.2019); email info@steenokkerzeel.be; NIS 23094"},
])
print("sources", n)
