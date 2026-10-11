# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/sources.csv")
rows = [
    {"source_id":"src_tlt_jr2025_nbb","title":"AGB Tielt jaarrekening boekjaar 2025 (official NBB WVV VKT-kap deposit 2026-00316168; AV 02.07.2026)","url":"http://cdn.staatsbladmonitor.be/2026pdf/2026-00316168.pdf","publisher":"AGB Tielt / NBB WVV deposit","accessed_date":"2026-08-19","source_class":"budget","notes":"tick1405; official NBB VKT-kap PDF 61089 bytes 19p deposit 2026-00316168 created 22.07.2026; leftover AGB sport+monumenten of mined city Tielt; euros from deposit PDF; NBB consult skipped; Belscope/Companyweb not used; no commissarisverslag filed (VKT-kap 8 not deposited); omzet 70 empty / 60/61 empty / pers 62 empty / brutomarge 679356 / debt 11899035 / lease 9303045 / pnl 321320 / dividend 160660"},
    {"source_id":"src_tlt_site","title":"Stad Tielt / AGB Tielt official contact (leftover AGB sport+monumenten)","url":"https://www.tielt.be/","publisher":"Stad Tielt / AGB Tielt","accessed_date":"2026-08-19","source_class":"official_register","notes":"tick1405; leftover AGB of mined city Tielt; statutory 2025 balans is NBB CDN; KBO e-mail agb@tielt.be tel 051/42.81.72"},
    {"source_id":"src_kbo_tlt_0841231312","title":"KBO Autonoom Gemeentebedrijf Tielt 0841.231.312","url":"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0841231312","publisher":"KBO Public Search FOD Economie","accessed_date":"2026-08-19","source_class":"official_register","notes":"tick1405; KBO 0841.231.312 Actief since 01.09.2011; Autonoom gemeentebedrijf; zetel Markt 13 8700 Tielt; 1 VE; tel 051/42.81.72; e-mail agb@tielt.be; NACE 93.110/91.220; voorzitter Luc Vannieuwenhuyze (WVV 2.1)"},
    {"source_id":"src_tlt_foi_contact","title":"AGB Tielt FOI channel / official contact (agb@tielt.be; Markt 13 Tielt)","url":"https://www.tielt.be/","publisher":"AGB Tielt / Stad Tielt","accessed_date":"2026-08-19","source_class":"official_register","notes":"tick1405; KBO e-mail agb@tielt.be; tel 051 42 81 72; voorzitter Luc Vannieuwenhuyze; ondervoorzitter Lieve Germonprez"},
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
