# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/sources.csv")
rows = [
    {"source_id":"src_dds_jr2025_nbb","title":"DDS jaarrekening boekjaar 2025 (official NBB WVV VOL-kap deposit 2026-00188846; AV 09.06.2026)","url":"http://cdn.staatsbladmonitor.be/2026pdf/2026-00188846.pdf","publisher":"DDS / NBB WVV deposit","accessed_date":"2026-08-19","source_class":"budget","notes":"tick1402; official NBB VOL-kap PDF 2117343 bytes 45p deposit 2026-00188846 created 23.06.2026 header 23.06.2026; leftover streek IGS Dender-Durme-Schelde; euros from deposit PDF; NBB consult skipped; Belscope/Companyweb not used; commissaris Dominique Vaes A01898; commissarisverslag pp.39-41 image-only / fee unpublished; omzet 1262519 / othops 5219038 / diensten 1359141 / pers 3875923 / inventory 12793375 / voorzieningen 7847265"},
    {"source_id":"src_dds_site","title":"DDS Streekregisseurs official site (leftover dienstverlenende vereniging 8 Oost-Vlaanderen gemeenten)","url":"https://dds-streekregisseurs.be/","publisher":"DDS Streekregisseurs","accessed_date":"2026-08-19","source_class":"official_register","notes":"tick1402; leftover streek IGS; site names Berlare+Buggenhout+Dendermonde+Hamme+Lebbeke+Wetteren+Wichelen+Zele; statutory 2025 balans is NBB CDN"},
    {"source_id":"src_kbo_dds_0207087872","title":"KBO Dender Durme en Schelde / DDS 0207.087.872","url":"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0207087872","publisher":"KBO Public Search FOD Economie","accessed_date":"2026-08-19","source_class":"official_register","notes":"tick1402; KBO 0207.087.872 Actief since 25.04.1970; Dienstverlenende vereniging since 25.11.2003; zetel Bevrijdingslaan 201 9200 Dendermonde since 07.02.1991; 1 VE; kapitaal 125000 (WVV geplaatst 870050); jaarvergadering juni; boekjaar 31 december; NACE 68.310/84.119; voorzitter Hans Knop (WVV 2.1 + site)"},
    {"source_id":"src_dds_foi_contact","title":"DDS FOI channel / official contact (info@dds-streekregisseurs.be; Bevrijdingslaan 201 Dendermonde)","url":"https://dds-streekregisseurs.be/contact/","publisher":"DDS Streekregisseurs","accessed_date":"2026-08-19","source_class":"official_register","notes":"tick1402; official site lists info@dds-streekregisseurs.be + Bevrijdingslaan 201 9200 Dendermonde + tel +32 52 21 39 91; WVV e-mail boekhouding@dds-verko.be; algemeen directeur Kris Dooms"},
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
