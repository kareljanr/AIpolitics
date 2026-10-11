# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
DATA = Path("/workspace/AIpolitics/docs/doge/data")
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
n = append_rows(DATA/"entities.csv", [
    {"entity_id":"city_kortenaken","name_nl":"Gemeente Kortenaken","name_fr":"Commune de Kortenaken","name_en":"Municipality of Kortenaken","level":"municipality","parent_id":"vlaanderen_gov","community_language":"nl","website":"https://www.kortenaken.be","foi_email":"financien@kortenaken.be","foi_postal":"Dorpsplein 35 3470 Kortenaken","notes":"tick1299 parent stub for AGB; KBO 0207.520.711 / OCMW 0212.189.379 (kortenaken.be contact); NIS 24054; city+OCMW JR2025 BBC now published 22.06.2026 left unmined for later GE unit"},
    {"entity_id":"agb_kortenaken","name_nl":"Autonoom Gemeentebedrijf Kortenaken","name_fr":"Regie communale autonome Kortenaken","name_en":"Autonomous municipal company Kortenaken","level":"municipal_agency","parent_id":"city_kortenaken","community_language":"nl","website":"https://www.kortenaken.be/bestuur-organisatie/beleidsdocumenten/jaarrekening/agb","foi_email":"financien@kortenaken.be","foi_postal":"Dorpsplein 35 3470 Kortenaken","notes":"tick1299 JR2025 Entity II residual; KBO 0535.811.469; 1 VE; no FVA; assets 3.479m fin debt 3.281m leasing 3.216m city prijssub 0.157m gecorr AFM -0.209m avail 0.095m; FOI ready"},
])
print("entities", n)
