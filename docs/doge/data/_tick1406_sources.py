# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/sources.csv")
rows = [
    {"source_id":"src_mlso_jr2025_nbb","title":"MLSO jaarrekening boekjaar 2025 (official NBB WVV VOL-inb deposit 2026-00247733; AV 03.06.2026)","url":"http://cdn.staatsbladmonitor.be/2026pdf/2026-00247733.pdf","publisher":"MLSO / NBB WVV deposit","accessed_date":"2026-08-19","source_class":"budget","notes":"tick1406; official NBB VOL-inb PDF 592563 bytes 61p deposit 2026-00247733 header 03.07.2026; leftover IGS haven-grond-industrialisatie Waaslandhaven; euros from deposit PDF; NBB consult skipped; Belscope/Companyweb not used; commissaris Callens Vandelanotte Theunissen BV B00003 / Philip Callens A2009 oordeel zonder voorbehoud assets 227277417 / PnL 7699101 fee 11635; omzet 24044090 / diensten 7752488 / Interwaas 3762955.84 / nrec 4415758 / debt 13594288 / pnl 7699101 / dividend 2910456"},
    {"source_id":"src_mlso_site","title":"MLSO official site / contact leftover IGS Waaslandhaven","url":"https://www.mlso.be/","publisher":"Maatschappij Linkerscheldeoever","accessed_date":"2026-08-19","source_class":"official_register","notes":"tick1406; leftover IGS of mined Waasland + Vlaams Gewest + PoAB; statutory 2025 balans is NBB CDN; contact info@mlso.be"},
    {"source_id":"src_kbo_mlso_0223944690","title":"KBO Maatschappij Linkerscheldeoever 0223.944.690","url":"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0223944690","publisher":"KBO Public Search FOD Economie","accessed_date":"2026-08-19","source_class":"official_register","notes":"tick1406; KBO 0223.944.690 Actief since 15.12.1982; Opdrachthoudende vereniging (Vlaams Gewest); zetel Sint-Paulusplein(KAL) 27 9120 Beveren-Kruibeke-Zwijndrecht; 1 VE; NACE 84.130; voorzitter Boudewijn Vlegels (WVV 2.1)"},
    {"source_id":"src_mlso_foi_contact","title":"MLSO FOI channel / official contact (info@mlso.be; Sint-Paulusplein 27 Beveren)","url":"https://www.mlso.be/","publisher":"MLSO","accessed_date":"2026-08-19","source_class":"official_register","notes":"tick1406; contact info@mlso.be; voorzitter Boudewijn Vlegels; ondervoorzitter Marc Van De Vijver"},
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
