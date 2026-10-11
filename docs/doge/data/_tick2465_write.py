from pathlib import Path
import csv
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2465_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_ooievaarsnest_jr2025_nbb_pdf_2465"
SRC_KBO="src_ooievaarsnest_kbo_2465"
SRC_SBM="src_ooievaarsnest_sbm_2465"
SRC_SITE="src_ooievaarsnest_site_2465"
EID="vzw_ooievaarsnest_tienen"
GAP="gap_ooievaarsnest_opgroeien_matrix_bruto_2_08m_omzet73_empty_pnl_drop_105k_destin_drop_105k_l5"
COMM="comm_ooievaarsnest_jr2025_statutory_bruto_2_08m_omzet73_empty_pnl_drop_105k"
LB="lb_ooievaarsnest_bruto_2_08m_omzet73_empty_pnl_drop_105k_destin_drop_105k_jr2025"
assert (ROOT/f"docs/doge/foi/drafts/{GAP}.md").is_file()

def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)

append_lines(DATA/"sources.csv", [
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Kinderdagverblijf Ooievaarsnest deposit 2026-00113832,http://cdn.staatsbladmonitor.be/2026pdf/2026-00113832.pdf,NBB official WVV deposit PDF,{DAY},budget,tick2465; official native PDF 51186 bytes 13p VKT-VZW 25.0.12 m04-f; header 13.05.2026; AV 23.04.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-05-19 12:20:52 UTC OpenPDF 1.3.26; all 13p native; CDN 2026-00113832 GET 200 Last-Modified 07.06.2026; VKT-VZW 6.1.1 6.1.3 6.5 6.6 7 8 niet dienstig; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Kinderdagverblijf Ooievaarsnest 0418.588.256,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0418588256,KBO Public Search FOD Economie,{DAY},official_register,tick2465; Actief; 1 VE 2.150.806.041 Ooievaarsnest Veldbornstraat 16 3300 Tienen since 03.01.2006; VZW since 31.08.1978; begindatum 31.08.1978; zetel Veldbornstraat 16 3300 Tienen since 23.01.1997; Werkgever RSZ since 01.01.1979; RSZ2025 88.911; toelating Kinderopvang Vlaamse Gemeenschap since 01.04.2014; FOI kdv@ooievaarsnesttienen.be; leftover mined city_tienen CIK; NOT Hartjes Tienen 0441.374.348 remine; NOT De Wissel 0421.913.376 remine; NOT DE ZONNEKINDJES 0416.541.952 remine",
f"{SRC_SBM},NBB Consult / SBM fiche Kinderdagverblijf Ooievaarsnest 0418588256 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0418588256,NBB Consult / SBM,{DAY},official_register,tick2465; deposit-id 2026-00113832 YE 01.01.2025-31.12.2025 filing 13.05.2026 published 13.05.2026 VKT-VZW Verkort Initial; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},Kinderdagverblijf Ooievaarsnest FOI contact leftover city_tienen CIK,https://wp.ooievaarsnesttienen.be/,VZW Kinderdagverblijf Ooievaarsnest leftover city_tienen CIK Opgroeien groepsopvang + BKO Klimop,{DAY},foi_contact,tick2465; FOI kdv@ooievaarsnesttienen.be / info@ooievaarsnesttienen.be; zetel + 1 VE Veldbornstraat 16 3300 Tienen; 1 VE leftover mined city_tienen after DE ZONNEKINDJES different-city skip and after Hartjes Tienen different-KBO skip; NOT Kloosterstraat 6 Drongen; NOT DE ZONNEKINDJES remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Kinderlach YE2024; NOT Helan; NOT De Speelboom Brussels; NOT Villa Boempatat SCAN/CDN403; NOT Elief CDN 403; NOT Hebe training; NOT Zo Groot YE2024; NOT De Bolster Zwalm not leftover mined parent; NOT GERUST zorgcentrale; NOT Vormingscentrum training; NOT Zwarte Zusters dissolved; NOT Paideia leftover city_brugge unused YE2025",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},Kinderdagverblijf Ooievaarsnest,ASBL Kinderdagverblijf Ooievaarsnest,Ooievaarsnest VZW (leftover city_tienen CIK),parastatal,city_tienen,nl,https://wp.ooievaarsnesttienen.be/,kdv@ooievaarsnesttienen.be,Veldbornstraat 16 3300 Tienen,tick2465 YE2025 Strong official native NBB PDF deposit 2026-00113832 + Strong KBO 0418.588.256 Actief 1 VE RSZ2025 88.911 toelating Kinderopvang Vlaamse Gemeenschap; omzet70 empty VKT; 73 empty VKT; 76A DROP 9128; bruto DROP 2078142 envelope; pnl DROP 104516; 9901 DROP 82223; equity JUMP 3244146; assets JUMP 3584716; debt JUMP 340571; FTE 32.4 JUMP; kapitaalsubsidies DROP 593048; destin691 DROP 104516 destin=pnl; 791 empty; cash DROP 221571; geldbeleggingen JUMP 1293719; leftover mined city_tienen after DE ZONNEKINDJES different-city skip; 1 VE CIK groepsopvang + BKO Klimop not private; NOT Kloosterstraat 6 Drongen; NOT DE ZONNEKINDJES 0416.541.952 remine; NOT D'n Opvang 0676.442.465 remine; NOT CAR Overleie 0454.250.505 remine; NOT Gesticht 0410.918.031 remine; NOT HOCUS-POCUS 0466.893.167 remine; NOT VKA 0433.480.132 remine; NOT Soetkin 0443.641.970 remine; NOT t Sloeberke 0410.973.360 remine; NOT CAR Accent 0413.208.122 remine; NOT De Elfjes 0455.636.912 remine; NOT De Steijgertjes 0413.421.720 remine; NOT H.Hart WZC 0413.595.330; NOT Zo Groot 0818.420.771 leftover city_oostende YE2024; NOT De Groene Verte 0465.061.649 remine; NOT De Vleugels 0431.408.290 remine; NOT De Pallieterkes 0418.538.865 remine; NOT De Medemens KDV 0893.678.915 remine; NOT De Medemens parent 0428.692.191 remine; NOT OKO & ZO 0862.154.608 remine; NOT Harlekijntjes 0407.700.403 remine; NOT Hartjes Ninove 0446.391.327 remine; NOT Hartjes Tienen 0441.374.348 remine; NOT De Wissel 0421.913.376 remine; NOT Familia 0461.401.779; NOT Peutertuinen GO Mariakerke 0410.221.116; NOT Mini-creches GO Next 0896.468.060 leftover city_hasselt YE2024; NOT Kinderlach 0450.275.186; NOT Helan; NOT De Speelboom Brussels; NOT Villa Boempatat 0660.616.520 leftover city_gent YE2025 SCAN/CDN403 2026-00396513; NOT Elief 0451.624.377 CDN 403; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; NOT De Bolster 0861.680.989 YE2025 zetel Zwalm city_zwalm not mined; NOT GERUST 0776.808.068 zorgcentrale; NOT Jessa hospital special schema; NOT Vormingscentrum 0413.342.338 training; NOT Zwarte Zusters 0413.272.260 dissolved; NOT Paideia 0445.129.931 leftover city_brugge unused YE2025 2026-00259827; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria SCAN; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Zo Groot Oostende YE2024 not taken; H.Hart Kortrijk YE2024 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_ooievaarsnest_omzet_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 70 omzet YE2025 empty (VKT; envelope is bruto 9900 because omzet empty),{SRC_PDF},strong,tick2465; PDF p5 native; YE2024 identical empty; 73 empty; 76A 9128",
f"bud_ooievaarsnest_73_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 empty (VKT),{SRC_PDF},strong,tick2465; PDF p5 native; YE2024 identical empty; FOI Opgroeien matrix behind bruto 2078142",
f"bud_ooievaarsnest_opbr_jr2025_statutory,{EID},2025,2078142,2078142,2078142,NBB VKT-VZW envelope bruto 9900 YE2025 DROP -1.69% (omzet 70 empty + 73 empty so VKT envelope is 9900; 76A 9128 present),{SRC_PDF},strong,tick2465; PDF p5 native; YE2024 identical 2113906; 70 empty; 73 empty",
f"bud_ooievaarsnest_bruto_jr2025_statutory,{EID},2025,2078142,2078142,2078142,NBB VKT-VZW code 9900 brutomarge YE2025 DROP -1.69% (VKT envelope because omzet empty),{SRC_PDF},strong,tick2465; PDF p5 native; YE2024 identical 2113906; 76A 9128 DROP; 73 empty",
f"bud_ooievaarsnest_pnl_jr2025_statutory,{EID},2025,104516,104516,104516,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 DROP -47.88% (was 200548),{SRC_PDF},strong,tick2465; PDF p5 native; YE2024 identical 200548; bedrijfswinst 9901 82223 DROP; destin691 104516 DROP destin=pnl",
f"bud_ooievaarsnest_bedrijfswinst_jr2025_statutory,{EID},2025,82223,82223,82223,NBB VKT-VZW code 9901 bedrijfswinst YE2025 DROP -58.10% (was 196229),{SRC_PDF},strong,tick2465; PDF p5 native; YE2024 identical 196229; 62 1817794 JUMP; 630 149498 DROP; 66A 5249 DROP; 640/8 23377 JUMP",
f"bud_ooievaarsnest_equity_jr2025_statutory,{EID},2025,3244146,3244146,3244146,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +2.66%,{SRC_PDF},strong,tick2465; PDF p4 native; YE2024 identical 3160230; kapitaalsubsidies 593048 DROP; overgedragen 14 442617 FLAT; fondsen 10 624314 FLAT; bestemde fondsen 13 1584166 JUMP",
f"bud_ooievaarsnest_assets_jr2025_statutory,{EID},2025,3584716,3584716,3584716,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +3.48%,{SRC_PDF},strong,tick2465; PDF p3 native; YE2024 identical 3464246; MVA 22/27 1840899 DROP; cash 221571 DROP; geldbeleggingen 1293719 JUMP; aanbouw 27 17280 JUMP",
f"bud_ooievaarsnest_debt_jr2025_statutory,{EID},2025,340571,340571,340571,NBB VKT-VZW code 17/49 schulden YE2025 JUMP +12.02%,{SRC_PDF},strong,tick2465; PDF p4 native; YE2024 identical 304016; 17 empty; 42/48 335192 JUMP",
f"bud_ooievaarsnest_cash_jr2025_statutory,{EID},2025,221571,221571,221571,NBB VKT-VZW code 54/58 liquide middelen YE2025 DROP -26.23%,{SRC_PDF},strong,tick2465; PDF p3 native; YE2024 identical 300366; geldbeleggingen 50/53 1293719 JUMP was 1090651",
f"bud_ooievaarsnest_destin_jr2025_statutory,{EID},2025,104516,104516,104516,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 DROP -47.88% (destin=pnl 104516; 13 JUMP 1584166),{SRC_PDF},strong,tick2465; PDF p6 native; YE2024 destin 200548; bestemde fondsen 13 1584166 JUMP FOI",
])
print("entities+budgets ok")

cash_json=(
"\"{\"\"2025_omzet\"\":0,\"\"2025_73\"\":0,\"\"2025_76A\"\":9128,"
"\"\"2025_opbr70_76A\"\":9128,\"\"2025_bruto\"\":2078142,"
"\"\"2025_pnl\"\":104516,\"\"2025_bedrijfswinst\"\":82223,"
"\"\"2025_equity\"\":3244146,\"\"2025_assets\"\":3584716,\"\"2025_debt\"\":340571,"
"\"\"2025_fte\"\":32.4,\"\"2025_kapitaalsubsidies\"\":593048,\"\"2025_destin691\"\":104516,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":221571,\"\"2025_geldbeleggingen\"\":1293719,"
"\"\"2025_personnel62\"\":1817794,\"\"2025_gebouwen22\"\":1790389,"
"\"\"2025_aanbouw27\"\":17280,\"\"2025_66A\"\":5249,"
"\"\"2025_fondsen10\"\":624314,\"\"2025_overgedragen14\"\":442617,"
"\"\"2025_bestemdefondsen13\"\":1584166,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":149498,\"\"2025_capex\"\":119015,"
"\"\"2024_omzet\"\":0,\"\"2024_73\"\":0,"
"\"\"2024_opbr70_76A\"\":9986,\"\"2024_bruto\"\":2113906,\"\"2024_pnl\"\":200548,\"\"2024_bedrijfswinst\"\":196229,"
"\"\"2024_equity\"\":3160230,\"\"2024_assets\"\":3464246,"
"\"\"2024_debt\"\":304016,\"\"2024_cash\"\":300366,\"\"2024_fte\"\":30.3,"
"\"\"2024_destin691\"\":200548,\"\"2024_kapitaalsubsidies\"\":613648,\"\"2024_76A\"\":9986,"
"\"\"2024_geldbeleggingen\"\":1090651}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Kinderdagverblijf Ooievaarsnest YE2025 (bruto DROP 2.08m / omzet+73 empty VKT / pnl DROP 105k / destin DROP 105k / Strong PDF),{EID},Opgroeien + leftover city_tienen CIK,VZW Kinderdagverblijf Ooievaarsnest (KBO 0418.588.256; Actief; 1 VE; RSZ2025 88.911; zetel + 1/1 VE Tienen),2026-04-23,2025,2025,2078142,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00113832.pdf,Public CIK dual of mined city_tienen,Publish Opgroeien matrix behind bruto 2.08m + why omzet+73 empty and why pnl DROP 105k while destin DROP 105k destin=pnl and cash DROP 222k while geldbeleggingen JUMP 1.29m and FTE 32.4,{SRC_PDF},strong,Vlaanderen>Vlaams-Brabant>Tienen>Ooievaarsnest>JR2025_statutory_L5,tick2465; Strong official native PDF; leftover mined city_tienen CIK; 1 VE; NOT every-10; NOT Kloosterstraat 6 Drongen; NOT DE ZONNEKINDJES remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Kinderlach YE2024; NOT Zo Groot YE2024; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"Ooievaarsnest bruto DROP 2.08m / omzet+73 empty VKT / pnl DROP 105k / destin DROP 105k (YE2025 leftover city_tienen CIK)",
"L5",
"cik_vzw_statutory",
"Vlaanderen>Vlaams-Brabant>Tienen>Ooievaarsnest>JR2025",
"2078142",
"2078142",
"PDF bruto 2078142 envelope because omzet empty; 70 empty; 73 empty; 76A 9128 DROP; bedrijfswinst DROP 82223; pnl DROP 104516; equity JUMP 3244146; assets JUMP 3584716; debt JUMP 340571; FTE 32.4 JUMP; kapitaalsubsidies DROP 593048; destin691 DROP 104516 destin=pnl; cash DROP 221571; geldbeleggingen JUMP 1293719; 1 VE leftover city_tienen CIK",
"strong",
SRC_PDF,
"Opgroeien + leftover city_tienen CIK",
"CIK / Kind en Gezin groepsopvang leftover city_tienen",
"2.08m bruto envelope; omzet+73 empty VKT; pnl DROP 105k; destin DROP 105k destin=pnl; cash DROP 222k; leftover city_tienen CIK",
"5.17",
"5.16",
"5.05",
"5.15",
"FOI Opgroeien matrix behind bruto 2.08m + why omzet+73 empty and why pnl DROP 105k while destin DROP 105k destin=pnl and cash DROP 222k while geldbeleggingen JUMP 1.29m and FTE 32.4",
"active",
"",
"tick2465 leftover mined city_tienen CIK after DE ZONNEKINDJES different-city skip; 1 VE; NOT every-10; NOT DE ZONNEKINDJES remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Kinderlach YE2024; NOT Zo Groot YE2024; NOT Elief CDN 403; NOT Villa Boempatat SCAN/CDN403; NOT De Speelboom Brussels; NOT De Elfjes remine; NOT De Steijgertjes remine",
])
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>Vlaams-Brabant>Tienen>Ooievaarsnest>CIK",
"entity_id": EID,
"what_is_missing": "Opgroeien split behind envelope bruto 2078142 (omzet 70 empty VKT + 73 empty VKT + 76A 9128) and why destin DROP 104516 destin=pnl while pnl DROP 104516 and cash DROP 221571 and geldbeleggingen JUMP 1293719 and FTE 32.4",
"why_it_matters": "Strong official PDF leftover public CIK of mined city_tienen; VKT envelope bruto 9900 2.08m because omzet empty; public Opgroeien groepsopvang + BKO Klimop",
"priority": "8",
"recipient_body": "VZW Kinderdagverblijf Ooievaarsnest / Raad van Bestuur",
"recipient_email": "kdv@ooievaarsnesttienen.be",
"recipient_postal": "Veldbornstraat 16 3300 Tienen",
"draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
"status": "ready",
"date_ready": DAY,
"date_sent": "",
"date_due": "",
"date_answered": "",
"response_summary": "",
"linked_commitment_id": COMM,
"linked_leaderboard_id": LB,
"created_utc": STAMP,
"updated_utc": STAMP,
"notes": "tick2465; ready NOT sent; Strong official native NBB PDF; leftover mined city_tienen CIK after DE ZONNEKINDJES different-city skip; 1 VE; NOT every-10; off Hartjes Tienen remine; off De Wissel remine; off Zonnekindjes remine",
}
foi_path=DATA/"foi_queue.csv"
raw=foi_path.read_bytes()
if not raw.endswith(b"\n"): raise SystemExit("foi_queue no LF")
with foi_path.open("a", newline="", encoding="utf-8") as f:
    w=csv.DictWriter(f, fieldnames=list(foi_row.keys()), extrasaction="raise", lineterminator="\n")
    w.writerow(foi_row)
print("foi_queue ok")

rq_path=DATA/"research_queue.csv"
rq_raw=rq_path.read_bytes()
if not rq_raw.endswith(b"\n"): raise SystemExit("rq no LF")
if b"\r\n" in rq_raw: raise SystemExit("CRLF")
if rq_raw.count(b"rq_2465,")!=1: raise SystemExit(f"bad 2465 count {rq_raw.count(b'rq_2465,')}")
if b"rq_2466," in rq_raw: raise SystemExit("2466 exists")
idx=rq_raw.rfind(b"rq_2465,")
if idx<0: raise SystemExit("rq_2465 not found")
new_2465=(
"rq_2465,leftover dual KDV Ooievaarsnest YE2025,hole_fill,8,done,L5,vzw_ooievaarsnest_tienen,"
"Took unused leftover public CIK Kinderdagverblijf Ooievaarsnest 0418.588.256 leftover mined city_tienen. Official NBB VKT-VZW YE2025 2026-00113832 native 13p. Envelope bruto 9900 DROP 2078142 (omzet+73 empty VKT; 76A 9128); pnl DROP 104516; destin DROP 104516 destin=pnl; cash DROP 221571. NOT DE ZONNEKINDJES remine. NOT Hartjes Tienen remine. NOT De Wissel remine. NOT Kinderlach YE2024.,"
f",{STAMP},{STAMP},tick2465 leftover mined city_tienen CIK; Strong native PDF; 1 VE; next every-10 is 2470\n"
)
new_2466=(
"rq_2466,leftover dual after KDV Ooievaarsnest — hunt unused public dual,hole_fill,8,open,L5,,"
"After KDV Ooievaarsnest YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf. Paideia 0445.129.931 leftover city_brugge YE2025 2026-00259827 CDN 200 54kB — take ONLY if unused + official native-text YE2025 PDF. Villa Boempatat 0660.616.520 leftover city_gent YE2025 2026-00396513 CDN 403 / SCAN — take ONLY if unused + official native-text YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen YE2025 2026-00374905 CDN 403 — take ONLY if CDN 200 native. Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO! Next / Zo Groot Oostende still YE2024 — take ONLY if unused + official YE2025 PDF. De Bolster 0861.680.989 YE2025 2026-00210039 zetel Zwalm (city_zwalm not mined) — take ONLY if leftover of a mined parent. Jessa leftover city_hasselt hospital YE2025 PDF — take ONLY if unused + official YE2025 euros extract. NOT Ooievaarsnest remine. NOT De Zonnekindjes remine. NOT D'n Opvang remine. NOT CAR Overleie remine. NOT Gesticht remine. NOT Grauwzusters convent. NOT Hocus-Pocus remine. NOT VKA remine. NOT Soetkin remine. NOT t Sloeberke remine. NOT CAR Accent remine. NOT De Groene Verte remine. NOT De Vleugels remine. NOT De Pallieterkes remine. NOT De Medemens remine. NOT OKO & ZO remine. NOT Harlekijntjes remine. NOT Hartjes remine. NOT De Wissel remine. NOT Familia remine. NOT Helan. NOT Hebe training. NOT WZC OLVA remine. NOT De Speelboom Brussels. NOT GERUST zorgcentrale. NOT Zo Groot remine. NOT De Elfjes remine. NOT De Steijgertjes remine. NOT Vormingscentrum training. NOT Zwarte Zusters dissolved.,"
f",{STAMP},{STAMP},spawned after tick2465; Ooievaarsnest taken leftover mined city_tienen CIK; Zonnekindjes taken leftover mined city_diepenbeek CIK; D'n Opvang taken leftover mined city_oostende CIK; CAR Overleie taken leftover mined city_kortrijk CAR; Gesticht taken leftover mined city_ieper CIK convent-class check PASSED; Hocus-Pocus taken leftover mined city_roeselare CIK; VKA taken leftover mined city_antwerpen CIK; Soetkin taken leftover mined city_kortrijk CIK; t Sloeberke taken leftover mined city_kortrijk CIK; De Groene Verte taken leftover mined city_houthulst WZC; next every-10 is 2470\n"
)
if new_2465.count("\n")!=1 or new_2466.count("\n")!=1: raise SystemExit("bad rq newlines")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2465.encode("utf-8"))
    f.write(new_2466.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2465", chk.count(b"rq_2465,"), "n2466", chk.count(b"rq_2466,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2465,2465,no,tick2465 leftover dual KDV Ooievaarsnest 0418.588.256 Strong native PDF (omzet70 empty VKT; 73 empty VKT; 76A DROP 9128; envelope bruto 9900 DROP 2078142; pnl DROP 104516; 9901 DROP 82223; equity JUMP 3244146; assets JUMP 3584716; debt JUMP 340571; FTE 32.4 JUMP; kapitaalsubsidies DROP 593048; destin691 DROP 104516 destin=pnl; 791 empty; cash DROP 221571; geldbeleggingen JUMP 1293719; 1 VE leftover city_tienen CIK); leftover mined city_tienen CIK; NOT DE ZONNEKINDJES remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT Grauwzusters convent; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens KDV remine; NOT De Medemens parent remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Mini-creches GO Next remine; NOT Kinderlach; NOT Zo Groot YE2024; NOT De Speelboom Brussels; NOT Elief CDN 403; NOT Villa Boempatat SCAN/CDN403; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; NOT De Bolster Zwalm not leftover mined parent; NOT GERUST zorgcentrale; NOT De Elfjes remine; NOT De Steijgertjes remine; NOT Vormingscentrum training; NOT Zwarte Zusters dissolved; next every-10 is 2470; next rq_2466 leftover dual\n",
encoding="utf-8",
)
print("loop_state ok")

log=ROOT/"docs/doge/loop_log.md"
log_raw=log.read_bytes()
if not log_raw.endswith(b"\n"): raise SystemExit("loop_log no LF")
entry=f"""
### {STAMP} - tick 2465 - rq_2465 KDV Ooievaarsnest (bruto DROP 2.08m / omzet+73 empty VKT / pnl DROP 105k / destin DROP 105k / Strong PDF)

- Unit: **rq_2465** leftover dual after **DE ZONNEKINDJES@2464**. Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024** (not re-downloaded); FARO 2026-00010398 still **YE2024** (HEAD-only policy Last-Modified 21.01.2026; not re-downloaded); AIESH/Gandae/Aralea/Manupal/Vlotter still **YE2024**. Zeepreventorium still **YE2024**. Drongen named+unnamed CARs **exhausted** — De Elfjes Kloosterstraat 6 already mined. Kohesi family **exhausted**. Quattro WZC members **exhausted** except already-in-entities St Jozef Zonnebeke / Sint-Vincentius Avelgem. CAR Antenne 3000 leftover city_leuven CDN still **403**. AZ Sint-Maria leftover city_halle YE2025 SCAN — not taken. CAR Noorderkempen leftover city_wuustwezel still SCAN. De Linde Ronse leftover city_ronse still **YE2024**. Kinderlach leftover city_eeklo still **YE2024**. Villa Boempatat leftover city_gent **YE2025** **2026-00396513** CDN **403** / SCAN no extractable euros — not taken. Woon en Zorg H. Hart Kortrijk leftover city_kortrijk still **YE2024**. Jessa leftover city_hasselt hospital YE2025 PDF / hospital special schema — not taken. Mini-creches GO! Next leftover city_hasselt still **YE2024**. Zo Groot Oostende leftover city_oostende still **YE2024** (2026-00055086 is YE2024; second 2026 deposit is YE2023 restatement). Familiehulp De Speelboom YE2025 unused Brussels zetel — not taken. Speelhuis Elief leftover city_antwerpen unused YE2025 **2026-00374905** CDN **403** — not taken. Hebe Kenniscentrum leftover city_antwerpen training — skip. WZC OLVA leftover city_antwerpen already in entities — do not remine. De Bolster 0861.680.989 YE2025 zetel Zwalm (city_zwalm not mined) — not taken. GERUST Zorgcentrale leftover city_herentals YE2025 — zorgcentrale not in dual types — not taken. Vormingscentrum 0413.342.338 leftover city_gent training — skip. Helan Kinderopvang 0464.151.037 already skipped. Zwarte Zusters 0413.272.260 dissolved — skip. DE ZONNEKINDJES 0416.541.952 just mined — do not remine. D'n Opvang 0676.442.465 just mined — do not remine. CAR Overleie just mined — do not remine. Gesticht just mined — do not remine. HOCUS-POCUS just mined — do not remine. VKA just mined — do not remine. Soetkin just mined — do not remine. t Sloeberke just mined — do not remine. De Groene Verte just mined — do not remine. De Vleugels already mined — do not remine. De Pallieterkes just mined — do not remine. De Medemens Kinderdagverblijven just mined — do not remine. De Medemens parent already mined — do not remine. CAR Accent already mined — do not remine. De Elfjes 0455.636.912 already mined — do not remine. De Steijgertjes 0413.421.720 already mined — do not remine. Hartjes Tienen 0441.374.348 already mined — do not remine. De Wissel 0421.913.376 already mined — do not remine. Grauwzusters Franciscanessen Hasselt 0409.771.748 leftover city_hasselt convent skip. First leftover unused + live official YE2025 native euros: took FREE leftover Flemish **VZW Kinderdagverblijf Ooievaarsnest** YE2025 (KBO **0418.588.256**; zetel Veldbornstraat 16 3300 Tienen; **Actief** **1 VE** **2.150.806.041** Ooievaarsnest Veldbornstraat 16 since 03.01.2006; RSZ2025 **88.911**; Kinderopvang Vlaamse Gemeenschap since 01.04.2014; leftover of mined **city_tienen**; kdv@ooievaarsnesttienen.be). Identity trap: KDV Ooievaarsnest 0418.588.256 ≠ Groepsopvang De Hartjes Tienen **0441.374.348** leftover city_tienen already mined; ≠ De Wissel **0421.913.376** already mined Tienen-site; ≠ DE ZONNEKINDJES **0416.541.952** leftover city_diepenbeek just mined; ≠ D'n Opvang **0676.442.465** leftover city_oostende just mined; ≠ De Elfjes **0455.636.912** already mined; ≠ De Steijgertjes **0413.421.720** already mined; ≠ CAR Overleie **0454.250.505**; ≠ Gesticht **0410.918.031**; ≠ HOCUS-POCUS **0466.893.167**; ≠ VKA **0433.480.132**; ≠ Soetkin **0443.641.970**; ≠ t Sloeberke **0410.973.360**; ≠ CAR Accent **0413.208.122**; ≠ Speelhuis Elief **0451.624.377**; ≠ Villa Boempatat **0660.616.520**; ≠ De Groene Verte **0465.061.649**; ≠ De Vleugels **0431.408.290**; ≠ De Pallieterkes **0418.538.865**; ≠ De Medemens Kinderdagverblijven **0893.678.915**; ≠ De Medemens **0428.692.191**; ≠ OKO & ZO **0862.154.608**; ≠ Harlekijntjes **0407.700.403**; ≠ Hartjes Ninove **0446.391.327**; ≠ Ferm Kinderopvang **0416.117.627**; ≠ Familia **0461.401.779**; ≠ Peutertuinen GO Mariakerke **0410.221.116**; ≠ Mini-crèches GO! Next **0896.468.060**; ≠ Kinderlach **0450.275.186**; ≠ Helan 0464.151.037; ≠ Hebe **0451.789.772**; ≠ WZC OLVA **0430.977.136**; ≠ H.Hart Kortrijk **0413.595.330**; ≠ De Linde Ronse **0778.279.401**; ≠ De Bolster **0861.680.989**; ≠ GERUST **0776.808.068**; ≠ Jessa **0821.142.117**; ≠ AZ Sint-Maria **0467.967.491**; ≠ Paideia **0445.129.931** leftover city_brugge unused YE2025; ≠ TKDV Het Veer Kloosterstraat 6; ≠ Vormingscentrum **0413.342.338** training; ≠ Zwarte Zusters **0413.272.260** dissolved. 1 VE Tienen — leftover of mined city_tienen (zetel + 1/1 VE). Confirmed leftover public (Opgroeien CIK groepsopvang + BKO Klimop; Kind en Gezin-vergund) not convent / not private clinic / not school / not OVBJ / not WZC / not VAPH / not Ferm / not Hartjes Tienen remine / not De Wissel remine / not Zonnekindjes remine. VKT-VZW **native text** (not scan) — 51186 B / 13p all native euros (VKT-VZW 6.1.1 / 6.1.3 / 6.5 / 6.6 / 7 / 8 niet dienstig).
- Found: official NBB VKT-VZW native PDF deposit **2026-00113832** (51186 B / 13p; AV **23.04.2026**; header **13.05.2026**; CDN Last-Modified **07.06.2026**; CreationDate 19.05.2026 OpenPDF 1.3.26; all 13p native; prior-year identical not restated) — omzet 70 **empty** VKT; 73 **empty** VKT; 76A **EUR9128** DROP −8.59% (was 9986); envelope bruto 9900 **EUR2078142** DROP −1.69% (VKT envelope because omzet empty; was 2113906); bruto 9900 **EUR2078142** DROP −1.69%; 62 **EUR1817794** JUMP +4.39%; 630 **EUR149498** DROP −5.56%; 66A **EUR5249** DROP −66.02%; 640/8 **EUR23377** JUMP +803.63%; 635/9 **empty**; bedrijfswinst 9901 **EUR82223** DROP −58.10%; pnl 9904 **EUR104516** DROP −47.88%; equity **EUR3244146** JUMP +2.66%; assets **EUR3584716** JUMP +3.48%; debt **EUR340571** JUMP +12.02%; FTE **32.4** JUMP +6.93% (was 30.3; 100 32.4; 105 32.9; 9087 32.4); kapitaalsubsidies **EUR593048** DROP −3.36%; destin 691 **EUR104516** DROP −47.88% (destin=pnl 104516; 791 empty; 13 JUMP 1584166); 791 **empty**; cash **EUR221571** DROP −26.23%; geldbeleggingen **EUR1293719** JUMP +18.62% (was 1090651); gebouwen **EUR1790389** DROP; MVA 22/27 **EUR1840899** DROP; aanbouw **EUR17280** JUMP; capex **EUR119015**; fondsen 10 **EUR624314** FLAT; overgedragen 14 **EUR442617** FLAT; bestemde fondsen 13 **EUR1584166** JUMP; voorzieningen 16 **empty**. Strong KBO + Strong PDF (native all pages; not SBM table; not Companyweb euros). Site: 1 VE leftover mined city_tienen CIK. NOT Kloosterstraat 6 Drongen De Elfjes remine. NOT DE ZONNEKINDJES remine. NOT D'n Opvang remine. NOT CAR Overleie remine. NOT Gesticht remine. NOT Grauwzusters convent. NOT HOCUS-POCUS remine. NOT VKA remine. NOT Soetkin remine. NOT t Sloeberke remine. NOT CAR Accent remine. NOT De Groene Verte remine. NOT De Vleugels remine. NOT De Pallieterkes remine. NOT De Medemens remine. NOT OKO & ZO remine. NOT Harlekijntjes remine. NOT Hartjes remine. NOT De Wissel remine. NOT Familia remine. NOT Mini-creches GO Next Hasselt. NOT Kinderlach. NOT Helan. NOT De Speelboom Brussels. NOT Elief CDN 403. NOT Villa Boempatat SCAN/CDN403. NOT Hebe training. NOT WZC OLVA remine. NOT Zo Groot YE2024. NOT De Bolster Zwalm. NOT GERUST zorgcentrale. NOT Vormingscentrum training. NOT Zwarte Zusters dissolved.
- Wrote: sources (+4); budgets (+11); commitments (+1); leaderboard (+1 pi 5.15); entities (+1 vzw_ooievaarsnest_tienen); foi + draft `gap_ooievaarsnest_opgroeien_matrix_bruto_2_08m_omzet73_empty_pnl_drop_105k_destin_drop_105k_l5`; rq_2465=done + rq_2466 open; loop_state ticks=2465; raw tick2465/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2470**). Next: rq_2466 unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Ooievaarsnest remine / NOT De Zonnekindjes remine / NOT D'n Opvang remine / NOT CAR Overleie remine / NOT Gesticht remine / NOT Grauwzusters convent / NOT HOCUS-POCUS remine / NOT VKA remine / NOT Soetkin remine / NOT t Sloeberke remine / NOT CAR Accent remine / NOT De Groene Verte remine / NOT De Vleugels remine / NOT De Pallieterkes remine / NOT De Medemens Kinderdagverblijven remine / NOT De Medemens parent remine / NOT OKO & ZO remine / NOT Harlekijntjes remine / NOT Hartjes remine / NOT De Wissel remine / NOT Familia remine / NOT BKO GENK-OOST remine / NOT Peutertuinen GO Mariakerke remine / NOT Mini-creches GO Next remine / NOT WZC OLVA remine / NOT Hebe training / NOT Quattro remine / NOT GERUST zorgcentrale / NOT Zo Groot remine / NOT De Elfjes remine / NOT De Steijgertjes remine / NOT Vormingscentrum training / NOT Zwarte Zusters dissolved). NOW leftover candidate: Paideia 0445.129.931 leftover city_brugge unused YE2025 **2026-00259827** CDN **200** 54kB — take ONLY if unused + official native-text YE2025 PDF. Villa Boempatat 0660.616.520 leftover city_gent YE2025 **2026-00396513** CDN **403** / SCAN — take ONLY if unused + official native-text YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen unused YE2025 **2026-00374905** CDN **403** — take ONLY if unused + CDN 200 native YE2025 PDF. Kinderlach leftover city_eeklo still YE2024 — take ONLY if unused + official YE2025 PDF. De Linde Ronse leftover city_ronse still YE2024 — take ONLY if unused + official YE2025 PDF. H.Hart Kortrijk leftover city_kortrijk still YE2024 — take ONLY if unused + official YE2025 PDF. Jessa leftover city_hasselt hospital YE2025 PDF — take ONLY if unused + official YE2025 euros extract. De Bolster 0861.680.989 YE2025 zetel Zwalm — leftover of mined parent only. Familiehulp De Speelboom YE2025 Brussels zetel — leftover-via-VE not enough per LOOP.md. Mini-creches GO! Next leftover city_hasselt still YE2024 — skip unless YE2025. Zo Groot Oostende leftover city_oostende still YE2024 — skip unless YE2025. Vormingscentrum leftover city_gent training — skip. VBJK leftover city_gent training — skip. Helan Kinderopvang Helan-HH-adjacent — skip. Hebe Kenniscentrum training — skip. Tick **2470** is next every-10.
"""
with log.open("ab") as f:
    f.write(entry.encode("utf-8"))
print("loop_log ok")
print("WRITE CORE DONE")
