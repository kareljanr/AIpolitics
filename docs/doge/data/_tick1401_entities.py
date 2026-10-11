# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/entities.csv")
row = {
    "entity_id": "igs_ovco",
    "name_nl": "OVCO Opdrachthoudende Vereniging voor Crematoriumbeheer in het Arrondissement Oostende (leftover IGS crematorium Polderbos)",
    "name_fr": "OVCO association chargée de mission crematorium arrondissement Ostende (IGS residuelle)",
    "name_en": "OVCO leftover Oostende-arrondissement crematorium IGS Polderbos",
    "level": "other",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://polderbos.be/",
    "foi_email": "info@polderbos.be",
    "foi_postal": "Grintweg 120 8400 Oostende",
    "notes": "tick1401 leftover residual crematorium IGS of mined arrondissement-Oostende municipalities Oostende+Bredene+Middelkerke+Oudenburg after leftover AGB/IGS hunt; KBO 0845.064.493 Actief since 05.12.2011; official NBB WVV VKT-kap PDF downloads; sourced euros assets 9368744 brutomarge 1163024 pers 459819 debt 6313967 pnl 385548 equity 3054777 cash 83941 invest 973616 cip 975949 capsub 1743380; FOI ready omzet 70 empty / 60/61 empty / 6.31m debt / 0.98m CIP / vennoten share unpublished; distinct from already-mined HAVICREM 1393 / Westlede 1394 / Hofheide 1395 / Pontes 1396 / IGL 1400",
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
