# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/entities.csv")
row = {
    "entity_id": "igs_dds",
    "name_nl": "DDS Dender Durme en Schelde (leftover IGS dienstverlenende vereniging / streekregisseurs 8 Oost-Vlaanderen gemeenten)",
    "name_fr": "DDS Dendre Durme et Escaut (IGS residuelle association de services)",
    "name_en": "DDS leftover Dender-Durme-Schelde development IGS",
    "level": "other",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://dds-streekregisseurs.be/",
    "foi_email": "info@dds-streekregisseurs.be",
    "foi_postal": "Bevrijdingslaan 201 9200 Dendermonde",
    "notes": "tick1402 leftover residual streek IGS of mined Oost-Vlaanderen municipalities Berlare+Buggenhout+Dendermonde+Hamme+Lebbeke+Wetteren+Wichelen+Zele after leftover AGB/IGS hunt; KBO 0207.087.872 Actief since 25.04.1970; official NBB WVV VOL-kap PDF downloads; sourced euros assets 48501395 omzet 1262519 othops 5219038 diensten 1359141 pers 3875923 inventory 12793375 voorzieningen 7847265 pnl -287310 equity 38109541 cash 5533236; FOI ready othops 5.22m / inventory 12.79m / voorzieningen 7.85m / commissaris fee unpublished; distinct from already-mined SOLVA / Interwaas / Veneco / IGEMO / Leiedal / WVI / IOK / Interleuven / Haviland / IGEAN",
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
