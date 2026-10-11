# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/sources.csv")
rows = [
    {"source_id":"src_ovco_jr2025_nbb","title":"OVCO jaarrekening boekjaar 2025 (official NBB WVV VKT-kap deposit 2026-00287142; AV 25.06.2026)","url":"http://cdn.staatsbladmonitor.be/2026pdf/2026-00287142.pdf","publisher":"OVCO / NBB WVV deposit","accessed_date":"2026-08-19","source_class":"budget","notes":"tick1401; official NBB VKT-kap PDF 908492 bytes 30p deposit 2026-00287142 created 14.07.2026 header 10.07.2026; leftover crematorium IGS Polderbos; euros from deposit PDF; NBB consult skipped; Belscope/Companyweb not used; commissaris Callens Vandelanotte Theunissen B0003 / 0427.897.088 / Inge Nuyttens A02514 fee 5576; oordeel zonder voorbehoud assets 9368744.13 / PnL 385547.67; omzet 70 empty / 60/61 empty"},
    {"source_id":"src_ovco_site","title":"Polderbos official site (leftover crematorium IGS OVCO arrondissement Oostende)","url":"https://polderbos.be/","publisher":"OVCO / Polderbos","accessed_date":"2026-08-19","source_class":"official_register","notes":"tick1401; leftover crematorium IGS; site history names Oostende+Oudenburg+Bredene+Middelkerke; statutory 2025 balans is NBB CDN"},
    {"source_id":"src_kbo_ovco_0845064493","title":"KBO OVCO 0845.064.493","url":"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0845064493","publisher":"KBO Public Search FOD Economie","accessed_date":"2026-08-19","source_class":"official_register","notes":"tick1401; KBO 0845.064.493 Actief since 05.12.2011; Opdrachthoudende vereniging since 05.12.2011; zetel Grintweg 120 8400 Oostende since 22.09.2022; 1 VE; kapitaal 571390; jaarvergadering juni; boekjaar 31 december; NACE 96.302; voorzitter Karel Labens since 27.03.2025 (WVV 2.1); KBO dagelijks bestuur Karel Labens since 28.06.2016"},
    {"source_id":"src_ovco_foi_contact","title":"OVCO FOI channel / Polderbos contact (info@polderbos.be; Grintweg 120 Oostende)","url":"https://polderbos.be/polderbos/polderbos-is-ook-meer/","publisher":"OVCO / Polderbos","accessed_date":"2026-08-19","source_class":"official_register","notes":"tick1401; official site lists info@polderbos.be + Grintweg 120 8400 Oostende + directeur Johan Seynaeve; raad van bestuur page may lag 2025 WVV board (voorzitter Karel Labens)"},
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
