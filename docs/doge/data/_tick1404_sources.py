# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/sources.csv")
rows = [
    {"source_id":"src_psln_jr2025_nbb","title":"Psilon jaarrekening boekjaar 2025 (official NBB WVV VKT-inb deposit 2026-00258944; AV 17.06.2026)","url":"http://cdn.staatsbladmonitor.be/2026pdf/2026-00258944.pdf","publisher":"Psilon / NBB WVV deposit","accessed_date":"2026-08-19","source_class":"budget","notes":"tick1404; official NBB VKT-inb PDF 3254883 bytes 32p deposit 2026-00258944 header 04.07.2026 created 07.07.2026; leftover crematorium IGS Zuid-West-Vlaanderen; euros from deposit PDF; NBB consult skipped; Belscope/Companyweb not used; commissaris Boes & Verrue B00821 / Mathias Verrue A02519 fee 4000; oordeel zonder voorbehoud assets 8627376.88 / PnL 498831.95; omzet 70 empty / 60/61 empty / brutomarge 1935397 / pers 877307 / debt 2186709 / voorzieningen 327247"},
    {"source_id":"src_psln_site","title":"Psilon official site (leftover opdrachthoudende vereniging 22 West-Vlaanderen gemeenten / crematorium Uitzicht)","url":"https://psilon.be/","publisher":"Psilon","accessed_date":"2026-08-19","source_class":"official_register","notes":"tick1404; leftover crematorium IGS; site names 21-22 gemeenten Zuid- en Midden-West-Vlaanderen; statutory 2025 balans is NBB CDN"},
    {"source_id":"src_kbo_psln_0874649790","title":"KBO Intergemeentelijke Vereniging voor Crematoriumbeheer in Zuid-West-Vlaanderen / PSILON 0874.649.790","url":"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0874649790","publisher":"KBO Public Search FOD Economie","accessed_date":"2026-08-19","source_class":"official_register","notes":"tick1404; KBO 0874.649.790 Actief since 23.06.2005; Opdrachthoudende vereniging since 22.03.2005; zetel Ambassadeur Baertlaan 5 8500 Kortrijk since 01.07.2016; 1 VE; tel 056/28.29.30; e-mail tine.bloeyaert@crematoriumuitzicht.be; kapitaal KBO 450000 / WVV inbreng 2090100; NACE 96.302; voorzitter Piet Lombaerts (WVV 2.1)"},
    {"source_id":"src_psln_foi_contact","title":"Psilon FOI channel / official contact (tine.bloeyaert@crematoriumuitzicht.be; Ambassadeur Baertlaan 5 Kortrijk)","url":"https://psilon.be/","publisher":"Psilon","accessed_date":"2026-08-19","source_class":"official_register","notes":"tick1404; KBO e-mail tine.bloeyaert@crematoriumuitzicht.be; tel 056 28 29 30; info@psilon.be; voorzitter Piet Lombaerts; ondervoorzitter Greta Vandeputte"},
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
