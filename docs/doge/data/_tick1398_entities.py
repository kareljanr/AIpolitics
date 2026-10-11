# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/entities.csv")
row = {
    "entity_id": "igs_ibeg",
    "name_nl": "IGS IBEG (Intercommunale van Brabant voor Elektriciteit en Gas; leftover IGS energy holding HV)",
    "name_fr": "IGS IBEG (intercommunale Brabant electricite et gaz; IGS residuel holding energie HV)",
    "name_en": "IGS IBEG leftover IGS energy holding Halle-Vilvoorde 5 municipalities",
    "level": "other",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://ibeg.be/",
    "foi_email": "info@ibeg.be",
    "foi_postal": "Laurent Benoit Dewezplein 6 1800 Vilvoorde",
    "notes": "tick1398 leftover residual IGS IBEG energy holding IGS; KBO 0202.082.078 Actief since 01.01.1968; official NBB WVV VOL-inb PDF downloads; sourced euros assets 100488193 omzet empty diensten 809703 debt 1450184 pnl 1283311 equity 99038008 div 3500000 fva 96372430; FOI ready omzet empty / 3.50m dividend / 96.37m FVA / 9.00m Fluvius HV loan; distinct from already-mined Fluvius Halle-Vilvoorde 1387 prefix flhv (IBEG is 21.48pct holding) and IGS IVEBICA 1397 / Pontes 1396 / Fluvius stack 1382-1391",
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
