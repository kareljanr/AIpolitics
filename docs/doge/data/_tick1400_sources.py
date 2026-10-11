# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/sources.csv")
rows = [
    {"source_id":"src_iglg_jr2025_nbb","title":"IGL jaarrekening boekjaar 2025 (official NBB WVV VOL-inb deposit 2026-00270170; AV 25.06.2026)","url":"http://cdn.staatsbladmonitor.be/2026pdf/2026-00270170.pdf","publisher":"IGL / NBB WVV deposit","accessed_date":"2026-08-19","source_class":"budget","notes":"tick1400; official NBB VOL-inb PDF 1080297 bytes 70p deposit 2026-00270170 created 07.07.2026 header 07.07.2026; leftover zorg IGS Limburg; euros from deposit PDF; NBB consult skipped; Belscope/Companyweb not used; commissaris Foederer B00466 / 0475.170.930 / Mathieu Meers A02676 fee 11495; oordeel zonder voorbehoud assets 65298610 / PnL 2298042.92; 6.10 category filled / geo empty"},
    {"source_id":"src_iglg_site","title":"IGL official site (leftover zorg IGS Limburg municipalities + provincie)","url":"https://iglimburg.be/","publisher":"IGL","accessed_date":"2026-08-19","source_class":"official_register","notes":"tick1400; leftover zorg IGS; Ter Heide + LIV + Secretariaat; statutory 2025 balans is NBB CDN"},
    {"source_id":"src_kbo_iglg_0201310929","title":"KBO IGL 0201.310.929","url":"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0201310929","publisher":"KBO Public Search FOD Economie","accessed_date":"2026-08-19","source_class":"official_register","notes":"tick1400; KBO 0201.310.929 Actief since 06.05.1967; Opdrachthoudende vereniging since 05.09.2003; zetel Klotstraat 125 3600 Genk since 05.09.2003; 5 VE; kapitaal 500000; jaarvergadering juni; boekjaar 31 december; voorzitter Nele Beckers since 27.03.2025"},
    {"source_id":"src_iglg_foi_contact","title":"IGL FOI channel / bestuur (info@iglimburg.be; Klotstraat 125 Genk)","url":"https://iglimburg.be/over-ons/bestuur-en-regelgeving/","publisher":"IGL","accessed_date":"2026-08-19","source_class":"official_register","notes":"tick1400; official site lists info@iglimburg.be + Klotstraat 125 3600 Genk + 089 32 39 50; bestuur katrien.geukens@iglimburg.be; presentiegeld 132.12 bestuurder / 264.24 voorzitter AV 26.06.2025"},
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
