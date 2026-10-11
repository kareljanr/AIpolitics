# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/entities.csv")
row = {
    "entity_id": "igs_iglg",
    "name_nl": "IGL Intercommunale Vereniging voor Hulp aan Gehandicapten in Limburg (leftover IGS zorg / opdrachthoudende vereniging)",
    "name_fr": "IGL Intercommunale d aide aux personnes handicapees du Limbourg (IGS residuelle soins)",
    "name_en": "IGL leftover Limburg disability-care IGS",
    "level": "other",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://iglimburg.be/",
    "foi_email": "info@iglimburg.be",
    "foi_postal": "Klotstraat 125 3600 Genk",
    "notes": "tick1400 leftover residual zorg IGS of mined Limburg municipalities + provincie after leftover AGB hunt; KBO 0201.310.929 Actief since 06.05.1967; official NBB WVV VOL-inb PDF downloads; sourced euros assets 65298610 omzet 48156858 diensten 5366617 pers 40508243 debt 31766387 pnl 2298043 equity 33288549 cash 5894254 invest 9500000 capsub 8217525; FOI ready VL werkingsopbrengsten 40.23m / 40.51m pers / 31.77m debt / 5.37m diensten / 8.22m capsub / 9.50m deposito / vennoten unpublished; distinct from already-mined Fluvius Limburg 1388 / Nuhma stack / Otary RS 1399",
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
