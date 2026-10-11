# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/sources.csv")
rows = [
    {"source_id":"src_otar_jr2025_nbb","title":"Otary RS jaarrekening boekjaar 2025 (official NBB WVV VOL-kap deposit 2026-00254280; AV 15.05.2026)","url":"http://cdn.staatsbladmonitor.be/2026pdf/2026-00254280.pdf","publisher":"Otary RS NV / NBB WVV deposit","accessed_date":"2026-08-19","source_class":"budget","notes":"tick1399; official NBB VOL-kap PDF 589485 bytes 47p deposit 2026-00254280 created 06.07.2026 header 06.07.2026; leftover Nuhma-adjacent public-law NV; euros from deposit PDF; NBB consult skipped; Belscope/Companyweb not used; commissaris Deloitte B00025 / 0429.053.863 / Gert Vanhees A01724 fee 16609 + extra 6598; 6.10 omzet category/geo empty"},
    {"source_id":"src_otar_site","title":"Otary RS official site (leftover public-law NV offshore wind Rentel Seastar Mermaid)","url":"https://www.otary.be/","publisher":"Otary RS NV","accessed_date":"2026-08-19","source_class":"official_register","notes":"tick1399; leftover Nuhma-adjacent public-law NV; 800 MW Rentel/Seastar/Mermaid; statutory 2025 balans is NBB CDN"},
    {"source_id":"src_kbo_otar_0833507538","title":"KBO Otary RS 0833.507.538","url":"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0833507538","publisher":"KBO Public Search FOD Economie","accessed_date":"2026-08-19","source_class":"official_register","notes":"tick1399; KBO 0833.507.538 Actief since 21.01.2011; NV Publiek recht; zetel Buskruitstraat 3 8400 Oostende since 04.04.2017; 1 VE; kapitaal 72310606.48; jaarvergadering mei; boekjaar 31 december"},
    {"source_id":"src_otar_foi_contact","title":"Otary RS FOI channel / disclaimer (administration@otary.be; Buskruitstraat 3 Oostende)","url":"https://www.otary.be/nl/disclaimer","publisher":"Otary RS NV","accessed_date":"2026-08-19","source_class":"official_register","notes":"tick1399; official disclaimer lists administration@otary.be + Buskruitstraat 3 B-8400 Oostende + 059 40 10 00; privacy@otary.be for AVG only"},
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
