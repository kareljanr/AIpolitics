# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/entities.csv")
row = {
    "entity_id": "agb_tlt",
    "name_nl": "Autonoom Gemeentebedrijf Tielt (leftover AGB sportaccommodaties + monumenten van mined city Tielt)",
    "name_fr": "AGB Tielt (AGB residuel sport et monuments)",
    "name_en": "AGB Tielt leftover sport+monuments municipal company",
    "level": "other",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.tielt.be/",
    "foi_email": "agb@tielt.be",
    "foi_postal": "Markt 13 8700 Tielt",
    "notes": "tick1405 leftover residual AGB of mined city Tielt after leftover AGB hunt; KBO 0841.231.312 Actief since 01.09.2011; official NBB WVV VKT-kap PDF downloads; sourced euros assets 19953810 brutomarge 679356 debt 11899035 lease 9303045 pnl 321320 equity 5586840 cash 1132461 capex 388010 dividend 160660; FOI ready omzet empty / diensten unpublished / pers empty / lease 9.30m / commissaris unpublished; distinct from already-mined WAGSO Waregem / AGB Oostkamp / AGB Sport Hulshout",
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
