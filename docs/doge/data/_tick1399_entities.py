# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/entities.csv")
row = {
    "entity_id": "nv_otar",
    "name_nl": "Otary RS NV (Publiek recht; leftover Nuhma-adjacent offshore-wind NV / Rentel Seastar Mermaid)",
    "name_fr": "Otary RS SA (droit public; NV residuelle offshore Nuhma-adjacente / Rentel Seastar Mermaid)",
    "name_en": "Otary RS leftover Nuhma-adjacent public-law NV offshore wind holding",
    "level": "other",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.otary.be/",
    "foi_email": "administration@otary.be",
    "foi_postal": "Buskruitstraat 3 8400 Oostende",
    "notes": "tick1399 leftover residual Nuhma-adjacent public-law NV after leftover AGB/IGS hunt; KBO 0833.507.538 Actief since 21.01.2011; official NBB WVV VOL-kap PDF downloads; sourced euros assets 95625285 omzet 12426978 diensten 10235828 debt 14121330 pnl 17237470 equity 81503955 div 14471000 fva 82864237 cash 10999623; FOI ready omzet-geo-empty / 10.24m diensten / 14.47m dividend / 82.86m FVA / 11.00m achtergesteld; distinct from already-mined ECO2050 cv 1360 prefix e50 (books 11m Otary subordinated) and Nuhma cv 1356; 8x12.5pct aandeelhouders incl Z-Kracht Herkenrodesingel",
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
