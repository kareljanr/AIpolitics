# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/sources.csv")
rows = [
    {"source_id":"src_ptri_jr2025_nbb","title":"AGB Patri / Stadspatrimonium Sint-Truiden jaarrekening boekjaar 2025 (official NBB WVV VKT-inb deposit 2026-00258861; AV 22.06.2026)","url":"http://cdn.staatsbladmonitor.be/2026pdf/2026-00258861.pdf","publisher":"AGB Patri / NBB WVV deposit","accessed_date":"2026-08-19","source_class":"budget","notes":"tick1407; official NBB VKT-inb PDF 58813 bytes 20p deposit 2026-00258861 header 30.06.2026; leftover AGB cultuurcentra of mined city Sint-Truiden; euros from deposit PDF; NBB consult skipped; Belscope/Companyweb not used; no commissarisverslag filed (6.6 empty); omzet 70 empty / 60/61 empty / pers 62 empty / brutomarge 574007 / debt 4566935 / ST recv 1565883 / pnl 84930 / dividend 16986"},
    {"source_id":"src_ptri_site","title":"Stad Sint-Truiden / AGB Patri official contact (leftover AGB cultuurcentra)","url":"https://www.sint-truiden.be/","publisher":"Stad Sint-Truiden / AGB Patri","accessed_date":"2026-08-19","source_class":"official_register","notes":"tick1407; leftover AGB of mined city Sint-Truiden; statutory 2025 balans is NBB CDN; KBO e-mail info.boekhouding@sint-truiden.be tel 011/70 15 00"},
    {"source_id":"src_kbo_ptri_0635564190","title":"KBO Autonoom gemeentebedrijf stadspatrimonium Sint-Truiden 0635.564.190","url":"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0635564190","publisher":"KBO Public Search FOD Economie","accessed_date":"2026-08-19","source_class":"official_register","notes":"tick1407; KBO 0635.564.190 Actief since 30.03.2015; afkorting AGB Patri; Autonoom gemeentebedrijf; zetel Gazometerstraat 9 3800 Sint-Truiden since 28.04.2026; 0 VE; tel 011/70 15 00; e-mail info.boekhouding@sint-truiden.be; NACE 90.312/90.042; voorzitter Ann Ruyters (WVV 2.1)"},
    {"source_id":"src_ptri_foi_contact","title":"AGB Patri FOI channel / official contact (info.boekhouding@sint-truiden.be; Gazometerstraat 9 Sint-Truiden)","url":"https://www.sint-truiden.be/","publisher":"AGB Patri / Stad Sint-Truiden","accessed_date":"2026-08-19","source_class":"official_register","notes":"tick1407; KBO e-mail info.boekhouding@sint-truiden.be; tel 011 70 15 00; voorzitter Ann Ruyters; vennoot Stad Sint-Truiden 0207.469.934 100%"},
]
with p.open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    seen = {row[fields[0]] for row in r}
added = 0
with p.open("a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    for row in rows:
        if row[fields[0]] in seen:
            continue
        w.writerow({k: row.get(k, "") for k in fields})
        added += 1
print("sources", added)
