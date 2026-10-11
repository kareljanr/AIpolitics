# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/sources.csv")
rows = [
    {"source_id":"src_ibeg_jr2025_nbb","title":"IGS IBEG jaarrekening boekjaar 2025 (official NBB WVV VOL-inb deposit 2026-00238388; AV 23.06.2026)","url":"http://cdn.staatsbladmonitor.be/2026pdf/2026-00238388.pdf","publisher":"IGS IBEG / NBB WVV deposit","accessed_date":"2026-08-19","source_class":"budget","notes":"tick1398; official NBB VOL-inb PDF 1.93MB 40p deposit 2026-00238388 created 02.07.2026 header 30.06.2026; leftover IGS energy holding 5 HV municipalities; euros from deposit PDF; NBB consult 403; Belscope/Companyweb not used; commissaris EY 8233+1671; 6:116 only; omzet 70 empty"},
    {"source_id":"src_ibeg_site","title":"IGS IBEG official site (leftover energy holding IGS 5 HV municipalities)","url":"https://ibeg.be/","publisher":"IGS IBEG","accessed_date":"2026-08-19","source_class":"official_register","notes":"tick1398; leftover IGS Grimbergen+Machelen+Meise+Vilvoorde+Wemmel; statutory 2025 balans is NBB CDN"},
    {"source_id":"src_kbo_ibeg_0202082078","title":"KBO IGS IBEG 0202.082.078","url":"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0202082078","publisher":"KBO Public Search FOD Economie","accessed_date":"2026-08-19","source_class":"official_register","notes":"tick1398; KBO 0202.082.078 Actief since 01.01.1968; OV since 01.04.2019; zetel Grote Markt z/n 1800 Vilvoorde; 0 VE; 15 bestuurders; KBO stand 18.08.2026"},
    {"source_id":"src_ibeg_foi_contact","title":"IGS IBEG FOI channel / secretariaat (info@ibeg.be; Dewezplein 6 Vilvoorde)","url":"https://ibeg.be/contact/","publisher":"IGS IBEG","accessed_date":"2026-08-19","source_class":"official_register","notes":"tick1398; secretariaat Laurent Benoit Dewezplein 6 1800 Vilvoorde; info@ibeg.be; voorzitter Jean-Pierre De Groef"},
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
