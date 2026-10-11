# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/entities.csv")
row = {
    "entity_id": "igs_mlso",
    "name_nl": "Maatschappij Linkerscheldeoever (leftover IGS opdrachthoudende vereniging / haven-grond-industrialisatie Waaslandhaven)",
    "name_fr": "MLSO (IGS residuel port-sol-industrialisation rive gauche de l'Escaut)",
    "name_en": "MLSO leftover Waaslandhaven land and industrialisation IGS",
    "level": "other",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.mlso.be/",
    "foi_email": "info@mlso.be",
    "foi_postal": "Sint-Paulusplein 27 9120 Beveren-Kruibeke-Zwijndrecht",
    "notes": "tick1406 leftover residual IGS of mined Waasland + Vlaams Gewest + PoAB after leftover AGB hunt; KBO 0223.944.690 Actief since 15.12.1982; official NBB WVV VOL-inb PDF downloads; sourced euros assets 227277417 omzet 24044090 diensten 7752488 interwaas 3762955.84 nrec 4415758 debt 13594288 pnl 7699101 equity 213683129 cash 24924839 capex 259767 dividend 2910456; FOI ready diensten split / Interwaas 3.76m / nrec 4.42m / vennoten unpublished; distinct from already-mined Interwaas / IDM / Water-Link / Farys / Port of Antwerp-Bruges",
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
