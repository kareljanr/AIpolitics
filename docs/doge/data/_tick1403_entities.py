# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/entities.csv")
row = {
    "entity_id": "igs_vrko",
    "name_nl": "VERKO Verenigde Kompostbedrijven (leftover IGS opdrachthoudende vereniging / waste inzameling + compostering + recyclageparken 9 Oost-Vlaanderen gemeenten)",
    "name_fr": "VERKO Verenigde Kompostbedrijven (IGS residuelle association chargee de mission dechets)",
    "name_en": "VERKO leftover Dender-Durme waste IGS",
    "level": "other",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://dds-verko.be/",
    "foi_email": "boekhouding@dds-verko.be",
    "foi_postal": "Bevrijdingslaan 201 9200 Dendermonde",
    "notes": "tick1403 leftover residual waste IGS of mined Oost-Vlaanderen municipalities Berlare+Buggenhout+Dendermonde+Hamme+Laarne+Lebbeke+Melle+Wetteren+Wichelen after leftover AGB hunt; KBO 0218.426.974 Actief since 08.06.1978; official NBB WVV VOL-kap PDF downloads; sourced euros assets 38416495 omzet 26146600 diensten 12448633 pers 11760008 debt 28727165 voorzieningen 5233600 pnl 6578 equity 4455729 cash 3529851 capex 2165409; FOI ready diensten 12.45m / pers 11.76m / debt 28.73m / commissaris fee unpublished; distinct from already-mined DDS 1402 / IDM / IVM / ILvA / IVLA / IVVO / IVIO / IVBO / IMOG / IVAGO / MIWA / IVOO / EcoWerf / Limburg.net",
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
