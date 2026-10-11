# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/sources.csv")
rows = [
    {"source_id":"src_vrko_jr2025_nbb","title":"VERKO jaarrekening boekjaar 2025 (official NBB WVV VOL-kap deposit 2026-00195553; AV 09.06.2026)","url":"http://cdn.staatsbladmonitor.be/2026pdf/2026-00195553.pdf","publisher":"VERKO / NBB WVV deposit","accessed_date":"2026-08-19","source_class":"budget","notes":"tick1403; official NBB VOL-kap PDF 2087128 bytes 48p deposit 2026-00195553 header 23.06.2026; leftover waste IGS Dender-Durme; euros from deposit PDF; NBB consult skipped; Belscope/Companyweb not used; commissaris Dominique Vaes A01898; commissarisverslag pp.41-44 image-only / fee unpublished; omzet 26146600 / diensten 12448633 / pers 11760008 / debt 28727165 / voorzieningen 5233600"},
    {"source_id":"src_vrko_site","title":"VERKO official site (leftover opdrachthoudende vereniging 9 Oost-Vlaanderen gemeenten)","url":"https://dds-verko.be/","publisher":"VERKO Verenigde Kompostbedrijven","accessed_date":"2026-08-19","source_class":"official_register","notes":"tick1403; leftover waste IGS; site names Berlare+Buggenhout+Dendermonde+Hamme+Laarne+Lebbeke+Melle+Wetteren+Wichelen; statutory 2025 balans is NBB CDN"},
    {"source_id":"src_kbo_vrko_0218426974","title":"KBO Verenigde Kompostbedrijven / VERKO 0218.426.974","url":"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0218426974","publisher":"KBO Public Search FOD Economie","accessed_date":"2026-08-19","source_class":"official_register","notes":"tick1403; KBO 0218.426.974 Actief since 08.06.1978; Opdrachthoudende vereniging since 01.01.2004; zetel Bevrijdingslaan 201 9200 Dendermonde since 28.02.1991; 11 VE; kapitaal WVV geplaatst 850450; jaarvergadering mei; boekjaar 31 december; NACE 38.110/38.330; voorzitter Raf De Wolf (WVV 2.1 + jaarverslag)"},
    {"source_id":"src_vrko_foi_contact","title":"VERKO FOI channel / official contact (boekhouding@dds-verko.be; Bevrijdingslaan 201 Dendermonde)","url":"https://dds-verko.be/","publisher":"VERKO Verenigde Kompostbedrijven","accessed_date":"2026-08-19","source_class":"official_register","notes":"tick1403; WVV e-mail boekhouding@dds-verko.be; ombud 0800 92 992; algemeen directeur Peter De Leeuw; voorzitter Raf De Wolf"},
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
