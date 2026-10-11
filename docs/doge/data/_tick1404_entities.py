# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/entities.csv")
row = {
    "entity_id": "igs_psln",
    "name_nl": "Psilon Intergemeentelijke Vereniging voor Crematoriumbeheer in Zuid-West-Vlaanderen (leftover IGS opdrachthoudende vereniging / crematorium Uitzicht 22 West-Vlaanderen gemeenten)",
    "name_fr": "Psilon (IGS residuelle association chargee de mission crematorium Uitzicht)",
    "name_en": "Psilon leftover South-West Flanders crematorium IGS",
    "level": "other",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://psilon.be/",
    "foi_email": "tine.bloeyaert@crematoriumuitzicht.be",
    "foi_postal": "Ambassadeur Baertlaan 5 8500 Kortrijk",
    "notes": "tick1404 leftover residual crematorium IGS of 22 mined West-Vlaanderen municipalities after leftover AGB hunt; KBO 0874.649.790 Actief since 23.06.2005; official NBB WVV VKT-inb PDF downloads; sourced euros assets 8627377 brutomarge 1935397 pers 877307 debt 2186709 pnl 498832 equity 6113421 cash 776217 capex 170092; FOI ready omzet empty / diensten unpublished / debt 2.19m / vennoten 6.20m guarantee; distinct from already-mined HAVICREM 1393 / Westlede 1394 / Hofheide 1395 / Pontes 1396 / OVCO 1401",
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
