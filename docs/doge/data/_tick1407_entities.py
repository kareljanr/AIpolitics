# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/entities.csv")
row = {
    "entity_id": "agb_ptri",
    "name_nl": "Autonoom gemeentebedrijf stadspatrimonium Sint-Truiden / AGB Patri (leftover AGB cultuurcentra van mined city Sint-Truiden)",
    "name_fr": "AGB Patri Saint-Trond (AGB residuel centres culturels)",
    "name_en": "AGB Patri leftover cultural-centres municipal company Sint-Truiden",
    "level": "other",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.sint-truiden.be/",
    "foi_email": "info.boekhouding@sint-truiden.be",
    "foi_postal": "Gazometerstraat 9 3800 Sint-Truiden",
    "notes": "tick1407 leftover residual AGB of mined city Sint-Truiden after leftover AGB hunt; KBO 0635.564.190 Actief since 30.03.2015; official NBB WVV VKT-inb PDF downloads; sourced euros assets 9688747 brutomarge 574007 debt 4566935 recv 1565883 pnl 84930 equity 5017317 cash 380295 capex 127844 dividend 16986; FOI ready omzet empty / diensten unpublished / pers empty / ST recv 1.57m / commissaris unpublished; distinct from already-mined AGOST / Trupark / AGB Tielt 1405 / MLSO 1406",
}
with p.open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    seen = {row0[fields[0]] for row0 in r}
added = 0
with p.open("a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    if row[fields[0]] not in seen:
        w.writerow({k: row.get(k, "") for k in fields})
        added = 1
print("entities", added)
