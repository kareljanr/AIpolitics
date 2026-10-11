# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/entities.csv")
row = {
    "entity_id":"igs_ivbc",
    "name_nl":"IGS IVEBICA (Opdrachthoudende Vereniging voor Bibliotheekwerking, Cultuur en Academie; leftover IGS Hemiksem/Schelle/Niel)",
    "name_fr":"IGS IVEBICA (association missionnee bibliotheque/culture/academie Hemiksem/Schelle/Niel; IGS residuel)",
    "name_en":"IGS IVEBICA leftover IGS library culture academy Hemiksem Schelle Niel",
    "level":"other",
    "parent_id":"sec_flanders",
    "community_language":"nl",
    "website":"https://www.ivebica.be/",
    "foi_email":"cultuur@ivebica.be",
    "foi_postal":"Heuvelstraat 111-117 2620 Hemiksem",
    "notes":"tick1397 leftover residual IGS IVEBICA library/culture/academy IGS; KBO 0280.300.997 Actief since 11.04.2003; official NBB WVV VKT-inb PDF downloads; sourced euros assets 919753 omzet empty-form/207858-jv diensten empty-form/370466-jv pers 1023843 debt 338424 pnl 60844 equity 581329 capex 42867 othinc 1382095; FOI ready omzet empty / 1.38m toelagen / 1.02m pers / 137k collectie; distinct from already-mined IGS Pontes 1396 prefix pnts and IGS Hofheide 1395 prefix hofh and IGS Westlede 1394 prefix wstl and HAVICREM 1393 prefix hvic and IVLA 1392 / Fluvius stack 1382-1391",
}
with p.open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    ids = {x.get("entity_id") for x in r}
added = 0
if row["entity_id"] not in ids:
    with p.open("a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writerow({k: row.get(k, "") for k in fields})
        added = 1
print("entities", added)
