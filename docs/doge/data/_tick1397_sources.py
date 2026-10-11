# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/sources.csv")
rows = [
    {"source_id":"src_ivbc_jr2025_nbb","title":"IGS IVEBICA jaarrekening boekjaar 2025 (official NBB WVV VKT-inb deposit 2026-00160301; AV 10.06.2026)","url":"http://cdn.staatsbladmonitor.be/2026pdf/2026-00160301.pdf","publisher":"IGS IVEBICA / NBB WVV deposit","accessed_date":"2026-08-19","source_class":"budget","notes":"tick1397; official NBB VKT-inb PDF 1.55MB 35p deposit 2026-00160301 created 15.06.2026; leftover IGS library/culture/academy Hemiksem+Schelle+Niel; euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; Belscope/Companyweb extracted tables not used; Staatsbladmonitor table euros not used; commissaris Clybouw Bedrijfsrevisoren BV B00162 / 0446.129.922 / Arnaud Clybouw A02273 oordeel getrouw beeld assets 919752.75 / PnL 60843.93; omzet 70 empty; 60/61 empty; only brutomarge published on form; jaarverslag publishes omzet 207858 / andere 1382095; 6.6 related empty except commissaris"},
    {"source_id":"src_ivbc_site","title":"IGS IVEBICA official site (leftover library/culture/academy IGS Hemiksem Schelle Niel)","url":"https://www.ivebica.be/over-ivebica","publisher":"IGS IVEBICA","accessed_date":"2026-08-19","source_class":"official_register","notes":"tick1397; leftover IGS of 3 Rupel municipalities Hemiksem+Schelle+Niel; site quote intergemeentelijke vereniging bibliotheek cultuurdienst academie; statutory 2025 balans is the NBB CDN deposit"},
    {"source_id":"src_kbo_ivbc_0280300997","title":"KBO IGS IVEBICA 0280.300.997","url":"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0280300997","publisher":"KBO Public Search FOD Economie","accessed_date":"2026-08-19","source_class":"official_register","notes":"tick1397; KBO 0280.300.997 Actief / normale toestand since 11.04.2003; statutaire naam Intergemeentelijke Vereniging voor Bibliotheekwerking, Cultuur en Academie voor Deeltijds Kunstonderwijs since 31.08.2017; afkorting IVEBICA since 31.08.2017; Opdrachthoudende vereniging (Vlaams Gewest) since 11.04.2003; zetel Heuvelstraat 111-117 2620 Hemiksem since 05.06.2023; 7 VE; KBO no email/web/tel; official site https://www.ivebica.be/; btw since 01.01.2026; RSZ since 01.01.2022; NACE 91.110/85.520; aanbestedende overheid since 11.04.2003; 6 bestuurders; KBO stand 18.08.2026"},
    {"source_id":"src_ivbc_foi_contact","title":"IGS IVEBICA FOI channel / klachtenprocedure (cultuur@ivebica.be; directeur Inge Cornelis)","url":"https://www.ivebica.be/klachtenprocedure","publisher":"IGS IVEBICA","accessed_date":"2026-08-19","source_class":"official_register","notes":"tick1397; site contact cultuur@ivebica.be; privacy HQ 03/218.72.09 privacy@ivebica.be; directeur Inge Cornelis (klachten 2e niveau); bibhemiksem@ivebica.be; bibniel@ivebica.be"},
]
with p.open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    ids = {row.get("source_id") for row in r}
added = 0
with p.open("a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    for row in rows:
        if row["source_id"] in ids:
            continue
        w.writerow({k: row.get(k, "") for k in fields})
        added += 1
print("sources", added)
