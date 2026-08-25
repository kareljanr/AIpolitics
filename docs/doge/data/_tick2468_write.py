from pathlib import Path
import csv
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2468_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_materdei_jr2025_nbb_pdf_2468"
SRC_KBO="src_materdei_kbo_2468"
SRC_SBM="src_materdei_sbm_2468"
SRC_SITE="src_materdei_site_2468"
EID="vzw_mater_dei_brasschaat"
GAP="gap_materdei_opgroeien_matrix_bruto_469k_omzet73_empty_pnl_drop_6k_destin_empty_l5"
COMM="comm_materdei_jr2025_statutory_bruto_469k_omzet73_empty_pnl_drop_6k"
LB="lb_materdei_bruto_469k_omzet73_empty_pnl_drop_6k_destin_empty_jr2025"
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
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Groepsopvang Mater Dei deposit 2026-00145548,http://cdn.staatsbladmonitor.be/2026pdf/2026-00145548.pdf,NBB official WVV deposit PDF,{DAY},budget,tick2468; official native PDF 47878 bytes 12p VKT-VZW 25.0.12 m04-f; header 09.06.2026; AV 04.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-06-09 07:35:12 UTC OpenPDF 1.3.26; all 12p native; CDN 2026-00145548 GET 200 Last-Modified 13.06.2026; VKT-VZW 6.1.1 6.2 6.3 6.5 6.6 7 8 niet dienstig; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Groepsopvang Mater Dei 0431.168.859,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0431168859,KBO Public Search FOD Economie,{DAY},official_register,tick2468; Actief; 1 VE 2.150.853.452 Kinderdagverblijf Mater Dei Vzw Bredabaan 479 bus a since 03.01.2006; VZW since 21.08.1985; begindatum 21.08.1985; zetel Bredabaan 479 2930 Brasschaat since 13.12.1994; FOI kinderdagverblijf@materdeibrasschaat.be; leftover mined city_brasschaat CIK; NOT WZC Mater Dei Heikruis remine; NOT Savio Dilbeek 0472.564.501 remine",
f"{SRC_SBM},NBB Consult / SBM fiche Groepsopvang Mater Dei 0431168859 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0431168859,NBB Consult / SBM,{DAY},official_register,tick2468; deposit-id 2026-00145548 YE 01.01.2025-31.12.2025 filing 09.06.2026 published 09.06.2026 VKT-VZW Verkort Initial; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},Mater Dei FOI contact leftover city_brasschaat CIK,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0431168859,VZW Groepsopvang Mater Dei leftover city_brasschaat CIK Opgroeien groepsopvang,{DAY},foi_contact,tick2468; FOI kinderdagverblijf@materdeibrasschaat.be; zetel Bredabaan 479 2930 Brasschaat; 1 VE leftover mined city_brasschaat after Savio different-city skip; NOT Savio remine; NOT WZC Mater Dei Heikruis remine; NOT Paideia remine; NOT Ooievaarsnest remine; NOT DE ZONNEKINDJES remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Kinderlach YE2024; NOT Helan; NOT De Speelboom Brussels; NOT Villa Boempatat SCAN/CDN403; NOT Elief CDN 403; NOT Hebe training; NOT Zo Groot YE2024; NOT De Bolster Zwalm not leftover mined parent; NOT GERUST zorgcentrale; NOT Vormingscentrum training; NOT Zwarte Zusters dissolved",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},Groepsopvang Mater Dei,ASBL Groepsopvang Mater Dei,Groepsopvang Mater Dei VZW (leftover city_brasschaat CIK),parastatal,city_brasschaat,nl,,kinderdagverblijf@materdeibrasschaat.be,Bredabaan 479 2930 Brasschaat,tick2468 YE2025 Strong official native NBB PDF deposit 2026-00145548 + Strong KBO 0431.168.859 Actief 1 VE 2.150.853.452; omzet70 empty VKT; 73 empty VKT; 76A empty; envelope bruto 9900 JUMP 468574; bruto JUMP 468574; pnl DROP -6395; 9901 DROP -6467; equity DROP 84354; assets DROP 128981; debt DROP 44627; FTE JUMP 7.7; kapitaalsubsidies FLAT 49579; destin691 empty; 791 empty; cash DROP 43327; geldbeleggingen empty; leftover city_brasschaat CIK; NOT WZC Mater Dei Heikruis remine; NOT Savio Dilbeek 0472.564.501 remine; NOT Dominiek Savio remine; NOT EVA Dilbeek 0477.276.325 remine; NOT Paideia 0445.129.931 remine; NOT Ooievaarsnest 0418.588.256 remine; NOT DE ZONNEKINDJES 0416.541.952 remine; NOT D'n Opvang 0676.442.465 remine; NOT CAR Overleie 0454.250.505 remine; NOT Gesticht 0410.918.031 remine; NOT HOCUS-POCUS 0466.893.167 remine; NOT VKA 0433.480.132 remine; NOT Soetkin 0443.641.970 remine; NOT t Sloeberke 0410.973.360 remine; NOT CAR Accent 0413.208.122 remine; NOT De Elfjes 0455.636.912 remine; NOT De Steijgertjes 0413.421.720 remine; NOT H.Hart WZC 0413.595.330; NOT Zo Groot 0818.420.771 leftover city_oostende YE2024; NOT De Groene Verte 0465.061.649 remine; NOT De Vleugels 0431.408.290 remine; NOT De Pallieterkes 0418.538.865 remine; NOT De Medemens KDV 0893.678.915 remine; NOT De Medemens parent 0428.692.191 remine; NOT OKO & ZO 0862.154.608 remine; NOT Harlekijntjes 0407.700.403 remine; NOT Hartjes Ninove 0446.391.327 remine; NOT Hartjes Tienen 0441.374.348 remine; NOT De Wissel 0421.913.376 remine; NOT Familia 0461.401.779; NOT Peutertuinen GO Mariakerke 0410.221.116; NOT Mini-creches GO Next 0896.468.060 leftover city_hasselt YE2024; NOT Kinderlach 0450.275.186; NOT Helan; NOT De Speelboom Brussels; NOT Villa Boempatat 0660.616.520 leftover city_gent YE2025 SCAN/CDN403 2026-00396513; NOT Elief 0451.624.377 CDN 403; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; NOT De Bolster 0861.680.989 YE2025 zetel Zwalm city_zwalm not mined; NOT GERUST 0776.808.068 zorgcentrale; NOT Jessa hospital special schema; NOT Vormingscentrum 0413.342.338 training; NOT Zwarte Zusters 0413.272.260 dissolved; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria SCAN; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Zo Groot Oostende YE2024 not taken; H.Hart Kortrijk YE2024 not taken; Vijverbeek Asse 0448.164.744 unused YE2025 not taken; Infano Ternat 0477.578.411 unused YE2025 not taken; Hupskadee 0863.886.651 leftover city_begijnendijk year TBD not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_materdei_omzet_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 70 omzet YE2025 empty (VKT; envelope is bruto 9900),{SRC_PDF},strong,tick2468; PDF p5 native; YE2024 empty; 73 empty; 76A empty",
f"bud_materdei_73_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 empty (VKT),{SRC_PDF},strong,tick2468; PDF p5 native; YE2024 empty; FOI Opgroeien matrix behind envelope 468574",
f"bud_materdei_opbr_jr2025_statutory,{EID},2025,468574,468574,468574,NBB VKT-VZW envelope bruto 9900 YE2025 JUMP +5.35% (omzet empty so envelope is bruto 9900),{SRC_PDF},strong,tick2468; PDF p5 native; YE2024 444799; 70 empty; 73 empty; 76A empty",
f"bud_materdei_bruto_jr2025_statutory,{EID},2025,468574,468574,468574,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +5.35% (VKT envelope because omzet empty),{SRC_PDF},strong,tick2468; PDF p5 native; YE2024 444799; 76A empty; 73 empty",
f"bud_materdei_pnl_jr2025_statutory,{EID},2025,-6395,-6395,-6395,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 DROP (was -3693; loss deepened),{SRC_PDF},strong,tick2468; PDF p5 native; YE2024 -3693; bedrijfswinst 9901 -6467 DROP; destin691 empty",
f"bud_materdei_bedrijfswinst_jr2025_statutory,{EID},2025,-6467,-6467,-6467,NBB VKT-VZW code 9901 bedrijfswinst YE2025 DROP (was -3826),{SRC_PDF},strong,tick2468; PDF p5 native; YE2024 -3826; 62 469464 JUMP; 630 5155 JUMP; 66A empty; 640/8 421 JUMP; 635/9 empty",
f"bud_materdei_equity_jr2025_statutory,{EID},2025,84354,84354,84354,NBB VKT-VZW code 10/15 eigen vermogen YE2025 DROP -7.05%,{SRC_PDF},strong,tick2468; PDF p4 native; YE2024 90749; kapitaalsubsidies 49579 FLAT; overgedragen 14 34775 DROP; fondsen 10 empty; bestemde fondsen 13 empty",
f"bud_materdei_assets_jr2025_statutory,{EID},2025,128981,128981,128981,NBB VKT-VZW code 20/58 totaal activa YE2025 DROP -8.77%,{SRC_PDF},strong,tick2468; PDF p3 native; YE2024 141381; MVA 22/27 18965 DROP; cash 43327 DROP; geldbeleggingen empty; aanbouw 27 empty",
f"bud_materdei_debt_jr2025_statutory,{EID},2025,44627,44627,44627,NBB VKT-VZW code 17/49 schulden YE2025 DROP -11.86%,{SRC_PDF},strong,tick2468; PDF p4 native; YE2024 50632; 17 empty; 42/48 41345 DROP",
f"bud_materdei_cash_jr2025_statutory,{EID},2025,43327,43327,43327,NBB VKT-VZW code 54/58 liquide middelen YE2025 DROP -30.24%,{SRC_PDF},strong,tick2468; PDF p3 native; YE2024 62106; geldbeleggingen 50/53 empty",
f"bud_materdei_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty (destin empty; 14 DROP 34775 = prior 41170 + pnl -6395),{SRC_PDF},strong,tick2468; PDF p6 native; YE2024 destin empty; bestemde fondsen 13 empty FOI",
])
print("entities+budgets ok")

cash_json=(
"\"{\"\"2025_omzet\"\":0,\"\"2025_73\"\":0,\"\"2025_76A\"\":0,"
"\"\"2025_opbr70_76A\"\":468574,\"\"2025_bruto\"\":468574,"
"\"\"2025_pnl\"\":-6395,\"\"2025_bedrijfswinst\"\":-6467,"
"\"\"2025_equity\"\":84354,\"\"2025_assets\"\":128981,\"\"2025_debt\"\":44627,"
"\"\"2025_fte\"\":7.7,\"\"2025_kapitaalsubsidies\"\":49579,\"\"2025_destin691\"\":0,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":43327,\"\"2025_geldbeleggingen\"\":0,"
"\"\"2025_personnel62\"\":469464,\"\"2025_gebouwen22\"\":13992,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":0,"
"\"\"2025_fondsen10\"\":0,\"\"2025_overgedragen14\"\":34775,"
"\"\"2025_bestemdefondsen13\"\":0,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":5155,\"\"2025_capex\"\":1658,"
"\"\"2024_omzet\"\":0,\"\"2024_73\"\":0,"
"\"\"2024_opbr70_76A\"\":444799,\"\"2024_bruto\"\":444799,\"\"2024_pnl\"\":-3693,\"\"2024_bedrijfswinst\"\":-3826,"
"\"\"2024_equity\"\":90749,\"\"2024_assets\"\":141381,"
"\"\"2024_debt\"\":50632,\"\"2024_cash\"\":62106,\"\"2024_fte\"\":7.2,"
"\"\"2024_destin691\"\":0,\"\"2024_kapitaalsubsidies\"\":49579,\"\"2024_76A\"\":0,"
"\"\"2024_geldbeleggingen\"\":0}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Groepsopvang Mater Dei YE2025 (bruto JUMP 469k / omzet+73 empty VKT / pnl DROP 6.4k / destin empty / Strong PDF),{EID},Opgroeien + leftover city_brasschaat CIK,VZW Groepsopvang Mater Dei (KBO 0431.168.859; Actief; 1 VE 2.150.853.452; zetel Brasschaat),2026-06-04,2025,2025,468574,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00145548.pdf,Public CIK dual of mined city_brasschaat,Publish Opgroeien matrix behind envelope 469k + why omzet+73 empty VKT and why pnl DROP -6395 while destin empty and cash DROP 43327,{SRC_PDF},strong,Vlaanderen>Antwerpen>Brasschaat>Groepsopvang Mater Dei>JR2025_statutory_L5,tick2468; Strong official native PDF; leftover mined city_brasschaat CIK; 1 VE; prior-year identical; NOT every-10; NOT Savio remine; NOT WZC Mater Dei Heikruis remine; NOT Dominiek Savio remine; NOT EVA Dilbeek remine; NOT Paideia remine; NOT Ooievaarsnest remine; NOT DE ZONNEKINDJES remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Kinderlach YE2024; NOT Zo Groot YE2024; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"Groepsopvang Mater Dei bruto JUMP 469k / omzet+73 empty VKT / pnl DROP 6.4k / destin empty (YE2025 leftover city_brasschaat CIK)",
"L5",
"cik_vzw_statutory",
"Vlaanderen>Antwerpen>Brasschaat>Groepsopvang Mater Dei>JR2025",
"468574",
"468574",
"PDF envelope 468574 = bruto 9900 VKT because omzet empty; 70 empty; 73 empty; 76A empty; bruto 468574; bedrijfswinst DROP -6467; pnl DROP -6395; equity DROP 84354; assets DROP 128981; debt DROP 44627; FTE 7.7; kapitaalsubsidies 49579 FLAT; destin691 empty; cash DROP 43327; leftover city_brasschaat CIK",
"strong",
SRC_PDF,
"Opgroeien + leftover city_brasschaat CIK",
"CIK / Kind en Gezin groepsopvang leftover city_brasschaat",
"469k envelope; omzet+73 empty VKT; pnl DROP -6395; destin empty; leftover city_brasschaat CIK",
"5.08",
"4.94",
"5.02",
"5.04",
"FOI Opgroeien matrix behind envelope 469k + why omzet+73 empty VKT and why pnl DROP -6395 while destin empty and cash DROP 43327",
"active",
"",
"tick2468 leftover mined city_brasschaat CIK after Savio different-city skip; 1 VE; prior-year identical; NOT every-10; NOT Savio remine; NOT WZC Mater Dei Heikruis remine; NOT Dominiek Savio remine; NOT EVA Dilbeek remine; NOT Paideia remine; NOT Ooievaarsnest remine; NOT DE ZONNEKINDJES remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Kinderlach YE2024; NOT Zo Groot YE2024; NOT Elief CDN 403; NOT Villa Boempatat SCAN/CDN403; NOT De Speelboom Brussels; NOT De Elfjes remine; NOT De Steijgertjes remine",
])
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>Antwerpen>Brasschaat>Groepsopvang Mater Dei>CIK",
"entity_id": EID,
"what_is_missing": "Opgroeien split behind envelope 468574 (omzet 70 empty + 73 empty + 76A empty; VKT bruto 9900) and why destin empty while pnl DROP -6395 and cash DROP 43327",
"why_it_matters": "Strong official PDF leftover public CIK of mined city_brasschaat; VKT envelope bruto 469k because omzet empty; public Opgroeien groepsopvang Bredabaan 479",
"priority": "8",
"recipient_body": "VZW Groepsopvang Mater Dei / Raad van Bestuur",
"recipient_email": "kinderdagverblijf@materdeibrasschaat.be",
"recipient_postal": "Bredabaan 479 2930 Brasschaat",
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
"notes": "tick2468; ready NOT sent; Strong official native NBB PDF; leftover mined city_brasschaat CIK after Savio different-city skip; 1 VE; prior-year identical; NOT every-10; off Savio remine; off WZC Mater Dei Heikruis remine",
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
if rq_raw.count(b"rq_2468,")!=1: raise SystemExit(f"bad 2468 count {rq_raw.count(b'rq_2468,')}")
if b"rq_2469," in rq_raw: raise SystemExit("2469 exists")
idx=rq_raw.rfind(b"rq_2468,")
if idx<0: raise SystemExit("rq_2468 not found")
new_2468=(
"rq_2468,leftover dual Groepsopvang Mater Dei YE2025,hole_fill,8,done,L5,vzw_mater_dei_brasschaat,"
"Took unused leftover public CIK Groepsopvang Mater Dei 0431.168.859 leftover mined city_brasschaat. Official NBB VKT-VZW YE2025 2026-00145548 native 12p. Envelope bruto 9900 JUMP 468574 (omzet+73 empty VKT); pnl DROP -6395; destin empty; FTE 7.7. NOT Savio remine. NOT WZC Mater Dei Heikruis remine. NOT Kinderlach YE2024.,"
f",{STAMP},{STAMP},tick2468 leftover mined city_brasschaat CIK; Strong native PDF; 1 VE; prior-year identical; next every-10 is 2470\n"
)
new_2469=(
"rq_2469,leftover dual after Groepsopvang Mater Dei — hunt unused public dual,hole_fill,8,open,L5,,"
"After Groepsopvang Mater Dei YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf. KDV Vijverbeek 0448.164.744 leftover city_asse YE2025 2026-00119084 — take ONLY if unused + official native-text YE2025 PDF. Infano 0477.578.411 leftover city_ternat YE2025 2026-00205409 — take ONLY if unused + official native-text YE2025 PDF. Hupskadee 0863.886.651 leftover city_begijnendijk 2026 deposits — take ONLY if unused + official YE2025 native PDF. Villa Boempatat 0660.616.520 leftover city_gent YE2025 2026-00396513 CDN 403 / SCAN — take ONLY if unused + official native-text YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen YE2025 2026-00374905 CDN 403 — take ONLY if CDN 200 native. Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO! Next / Zo Groot Oostende still YE2024 — take ONLY if unused + official YE2025 PDF. De Bolster 0861.680.989 YE2025 2026-00210039 zetel Zwalm (city_zwalm not mined) — take ONLY if leftover of a mined parent. Jessa leftover city_hasselt hospital YE2025 PDF — take ONLY if unused + official YE2025 euros extract. NOT Mater Dei remine. NOT Savio remine. NOT Paideia remine. NOT Ooievaarsnest remine. NOT De Zonnekindjes remine. NOT D'n Opvang remine. NOT CAR Overleie remine. NOT Gesticht remine. NOT Grauwzusters convent. NOT Hocus-Pocus remine. NOT VKA remine. NOT Soetkin remine. NOT t Sloeberke remine. NOT CAR Accent remine. NOT De Groene Verte remine. NOT De Vleugels remine. NOT De Pallieterkes remine. NOT De Medemens remine. NOT OKO & ZO remine. NOT Harlekijntjes remine. NOT Hartjes remine. NOT De Wissel remine. NOT Familia remine. NOT Helan. NOT Hebe training. NOT WZC OLVA remine. NOT De Speelboom Brussels. NOT GERUST zorgcentrale. NOT Zo Groot remine. NOT De Elfjes remine. NOT De Steijgertjes remine. NOT Vormingscentrum training. NOT Zwarte Zusters dissolved. NOT Dominiek Savio remine. NOT EVA Dilbeek remine. NOT WZC Mater Dei Heikruis remine.,"
f",{STAMP},{STAMP},spawned after tick2468; Mater Dei taken leftover mined city_brasschaat CIK; Savio taken leftover mined city_dilbeek CIK; Paideia taken leftover mined city_brugge CIK; Ooievaarsnest taken leftover mined city_tienen CIK; Zonnekindjes taken leftover mined city_diepenbeek CIK; D'n Opvang taken leftover mined city_oostende CIK; CAR Overleie taken leftover mined city_kortrijk CAR; Gesticht taken leftover mined city_ieper CIK convent-class check PASSED; Hocus-Pocus taken leftover mined city_roeselare CIK; VKA taken leftover mined city_antwerpen CIK; Soetkin taken leftover mined city_kortrijk CIK; t Sloeberke taken leftover mined city_kortrijk CIK; De Groene Verte taken leftover mined city_houthulst WZC; next every-10 is 2470\n"
)
if new_2468.count("\n")!=1 or new_2469.count("\n")!=1: raise SystemExit("bad rq newlines")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2468.encode("utf-8"))
    f.write(new_2469.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2468", chk.count(b"rq_2468,"), "n2469", chk.count(b"rq_2469,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2468,2468,no,tick2468 leftover dual Groepsopvang Mater Dei 0431.168.859 Strong native PDF (omzet70 empty VKT; 73 empty VKT; 76A empty; envelope bruto 9900 JUMP 468574; bruto JUMP 468574; pnl DROP -6395; 9901 DROP -6467; equity DROP 84354; assets DROP 128981; debt DROP 44627; FTE JUMP 7.7; kapitaalsubsidies FLAT 49579; destin691 empty; 791 empty; cash DROP 43327; geldbeleggingen empty; 1 VE leftover city_brasschaat CIK); leftover mined city_brasschaat CIK; prior-year identical; NOT Savio remine; NOT WZC Mater Dei Heikruis remine; NOT Dominiek Savio remine; NOT EVA Dilbeek remine; NOT Paideia remine; NOT Ooievaarsnest remine; NOT DE ZONNEKINDJES remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT Grauwzusters convent; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens KDV remine; NOT De Medemens parent remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Mini-creches GO Next remine; NOT Kinderlach; NOT Zo Groot YE2024; NOT De Speelboom Brussels; NOT Elief CDN 403; NOT Villa Boempatat SCAN/CDN403; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; NOT De Bolster Zwalm not leftover mined parent; NOT GERUST zorgcentrale; NOT De Elfjes remine; NOT De Steijgertjes remine; NOT Vormingscentrum training; NOT Zwarte Zusters dissolved; next every-10 is 2470; next rq_2469 leftover dual\n",
encoding="utf-8",
)
print("loop_state ok")

log=ROOT/"docs/doge/loop_log.md"
log_raw=log.read_bytes()
if not log_raw.endswith(b"\n"): raise SystemExit("loop_log no LF")
entry=f"""
### {STAMP} - tick 2468 - rq_2468 Groepsopvang Mater Dei (bruto JUMP 469k / omzet+73 empty VKT / pnl DROP 6.4k / destin empty / Strong PDF)

- Unit: **rq_2468** leftover dual after **Savio@2467**. Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024** (not re-downloaded); FARO 2026-00010398 still **YE2024** (HEAD-only policy Last-Modified 21.01.2026; not re-downloaded); AIESH/Gandae/Aralea/Manupal/Vlotter still **YE2024**. Zeepreventorium still **YE2024**. Drongen named+unnamed CARs **exhausted** — De Elfjes Kloosterstraat 6 already mined. Kohesi family **exhausted**. Quattro WZC members **exhausted** except already-in-entities St Jozef Zonnebeke / Sint-Vincentius Avelgem. CAR Antenne 3000 leftover city_leuven CDN still **403**. AZ Sint-Maria leftover city_halle YE2025 SCAN — not taken. CAR Noorderkempen leftover city_wuustwezel still SCAN. De Linde Ronse leftover city_ronse still **YE2024**. Kinderlach leftover city_eeklo still **YE2024**. Villa Boempatat leftover city_gent **YE2025** **2026-00396513** CDN **403** / SCAN no extractable euros — not taken. Woon en Zorg H. Hart Kortrijk leftover city_kortrijk still **YE2024**. Jessa leftover city_hasselt hospital YE2025 PDF / hospital special schema — not taken. Mini-creches GO! Next leftover city_hasselt still **YE2024**. Zo Groot Oostende leftover city_oostende still **YE2024** (2026-00055086 is YE2024; second 2026 deposit is YE2023 restatement). Familiehulp De Speelboom YE2025 unused Brussels zetel — not taken. Speelhuis Elief leftover city_antwerpen unused YE2025 **2026-00374905** CDN **403** — not taken. Hebe Kenniscentrum leftover city_antwerpen training — skip. WZC OLVA leftover city_antwerpen already in entities — do not remine. De Bolster 0861.680.989 YE2025 zetel Zwalm (city_zwalm not mined) — not taken. GERUST Zorgcentrale leftover city_herentals YE2025 — zorgcentrale not in dual types — not taken. Vormingscentrum 0413.342.338 leftover city_gent training — skip. Helan Kinderopvang 0464.151.037 already skipped. Zwarte Zusters 0413.272.260 dissolved — skip. Savio 0472.564.501 just mined — do not remine. Paideia 0445.129.931 just mined — do not remine. Ooievaarsnest 0418.588.256 just mined — do not remine. DE ZONNEKINDJES 0416.541.952 just mined — do not remine. D'n Opvang 0676.442.465 just mined — do not remine. CAR Overleie just mined — do not remine. Gesticht just mined — do not remine. HOCUS-POCUS just mined — do not remine. VKA just mined — do not remine. Soetkin just mined — do not remine. t Sloeberke just mined — do not remine. De Groene Verte just mined — do not remine. De Vleugels already mined — do not remine. De Pallieterkes just mined — do not remine. De Medemens Kinderdagverblijven just mined — do not remine. De Medemens parent already mined — do not remine. CAR Accent already mined — do not remine. De Elfjes 0455.636.912 already mined — do not remine. De Steijgertjes 0413.421.720 already mined — do not remine. Hartjes Tienen 0441.374.348 already mined — do not remine. De Wissel 0421.913.376 already mined — do not remine. Grauwzusters Franciscanessen Hasselt 0409.771.748 leftover city_hasselt convent skip. EVA-vzw Gemeentelijke Kinderopvang Dilbeek 0477.276.325 already mined — do not remine. Dominiek Savio Hooglede VAPH already mined — do not remine. First leftover unused + live official YE2025 native euros: took FREE leftover Flemish **VZW Groepsopvang Mater Dei** YE2025 (KBO **0431.168.859**; zetel Bredabaan 479 2930 Brasschaat; **Actief** **1 VE** **2.150.853.452** Kinderdagverblijf Mater Dei Vzw Bredabaan 479 bus a since 03.01.2006; RSZ2025 **88.911**; leftover of mined **city_brasschaat**; kinderdagverblijf@materdeibrasschaat.be; Opgroeien groepsopvang). Identity trap: Groepsopvang Mater Dei 0431.168.859 ≠ WZC Mater Dei Heikruis Pepingen already in entities; ≠ Kinderdagverblijf Savio **0472.564.501** leftover city_dilbeek just mined; ≠ Dominiek Savio VZW Hooglede-Gits VAPH already mined; ≠ EVA-vzw Gemeentelijke Kinderopvang Dilbeek **0477.276.325** leftover city_dilbeek already mined; ≠ Paideia **0445.129.931** leftover city_brugge just mined; ≠ KDV Ooievaarsnest **0418.588.256** leftover city_tienen just mined; ≠ DE ZONNEKINDJES **0416.541.952** leftover city_diepenbeek just mined; ≠ D'n Opvang **0676.442.465** leftover city_oostende just mined; ≠ De Elfjes **0455.636.912** already mined; ≠ De Steijgertjes **0413.421.720** already mined; ≠ CAR Overleie **0454.250.505**; ≠ Gesticht **0410.918.031**; ≠ HOCUS-POCUS **0466.893.167**; ≠ VKA **0433.480.132**; ≠ Soetkin **0443.641.970**; ≠ t Sloeberke **0410.973.360**; ≠ CAR Accent **0413.208.122**; ≠ Speelhuis Elief **0451.624.377**; ≠ Villa Boempatat **0660.616.520**; ≠ De Groene Verte **0465.061.649**; ≠ De Vleugels **0431.408.290**; ≠ De Pallieterkes **0418.538.865**; ≠ De Medemens Kinderdagverblijven **0893.678.915**; ≠ De Medemens **0428.692.191**; ≠ OKO & ZO **0862.154.608**; ≠ Harlekijntjes **0407.700.403**; ≠ Hartjes Ninove **0446.391.327**; ≠ Hartjes Tienen **0441.374.348**; ≠ De Wissel **0421.913.376**; ≠ Ferm Kinderopvang **0416.117.627**; ≠ Familia **0461.401.779**; ≠ Peutertuinen GO Mariakerke **0410.221.116**; ≠ Mini-crèches GO! Next **0896.468.060**; ≠ Kinderlach **0450.275.186**; ≠ Helan 0464.151.037; ≠ Hebe **0451.789.772**; ≠ WZC OLVA **0430.977.136**; ≠ H.Hart Kortrijk **0413.595.330**; ≠ De Linde Ronse **0778.279.401**; ≠ De Bolster **0861.680.989**; ≠ GERUST **0776.808.068**; ≠ Jessa **0821.142.117**; ≠ AZ Sint-Maria **0467.967.491**; ≠ TKDV Het Veer Kloosterstraat 6; ≠ Vormingscentrum **0413.342.338** training; ≠ Zwarte Zusters **0413.272.260** dissolved; ≠ KDV Vijverbeek **0448.164.744** leftover city_asse unused YE2025; ≠ Infano **0477.578.411** leftover city_ternat unused YE2025. 1 VE Brasschaat — leftover of mined city_brasschaat (zetel + 1/1 VE Bredabaan 479). Confirmed leftover public (Opgroeien CIK groepsopvang; Kind en Gezin-vergund) not convent / not private clinic / not school / not OVBJ / not WZC / not VAPH / not Ferm / not Savio remine / not WZC Mater Dei Heikruis remine. VKT-VZW **native text** (not scan) — 47878 B / 12p all native euros (VKT-VZW 6.1.1 / 6.2 / 6.3 / 6.5 / 6.6 / 7 / 8 niet dienstig).
- Found: official NBB VKT-VZW native PDF deposit **2026-00145548** (47878 B / 12p; AV **04.06.2026**; header **09.06.2026**; CDN Last-Modified **13.06.2026**; CreationDate 09.06.2026 OpenPDF 1.3.26; all 12p native; prior-year identical not restated) — omzet 70 **empty** VKT; 73 **empty** VKT; 76A **empty**; envelope bruto 9900 **EUR468574** JUMP +5.35% (VKT envelope because omzet empty; was 444799); bruto 9900 **EUR468574** JUMP +5.35%; 62 **EUR469464** JUMP +5.67%; 630 **EUR5155** JUMP +19.66%; 66A **empty**; 640/8 **EUR421** JUMP (was 23); 635/9 **empty**; bedrijfswinst 9901 **EUR-6467** DROP (was −3826); pnl 9904 **EUR-6395** DROP (was −3693); equity **EUR84354** DROP −7.05%; assets **EUR128981** DROP −8.77%; debt **EUR44627** DROP −11.86%; FTE **7.7** JUMP +6.94% (was 7.2; 100 7.7; 105 7; 9087 7.7); kapitaalsubsidies **EUR49579** FLAT; destin 691 **empty** (791 empty; 14 DROP 34775 = prior 41170 + pnl −6395); 791 **empty**; cash **EUR43327** DROP −30.24%; geldbeleggingen **empty**; gebouwen **EUR13992** DROP; MVA 22/27 **EUR18965** DROP; aanbouw **empty**; capex **EUR1658**; fondsen 10 **empty**; overgedragen 14 **EUR34775** DROP; bestemde fondsen 13 **empty**; voorzieningen 16 **empty**. Strong KBO + Strong PDF (native all pages; not SBM table; not Companyweb euros). Site: 1 VE leftover mined city_brasschaat CIK. NOT Savio remine. NOT WZC Mater Dei Heikruis remine. NOT Dominiek Savio remine. NOT EVA Dilbeek remine. NOT Paideia remine. NOT Ooievaarsnest remine. NOT DE ZONNEKINDJES remine. NOT D'n Opvang remine. NOT CAR Overleie remine. NOT Gesticht remine. NOT Grauwzusters convent. NOT HOCUS-POCUS remine. NOT VKA remine. NOT Soetkin remine. NOT t Sloeberke remine. NOT CAR Accent remine. NOT De Groene Verte remine. NOT De Vleugels remine. NOT De Pallieterkes remine. NOT De Medemens remine. NOT OKO & ZO remine. NOT Harlekijntjes remine. NOT Hartjes remine. NOT De Wissel remine. NOT Familia remine. NOT Mini-creches GO Next Hasselt. NOT Kinderlach. NOT Helan. NOT De Speelboom Brussels. NOT Elief CDN 403. NOT Villa Boempatat SCAN/CDN403. NOT Hebe training. NOT WZC OLVA remine. NOT Zo Groot YE2024. NOT De Bolster Zwalm. NOT GERUST zorgcentrale. NOT Vormingscentrum training. NOT Zwarte Zusters dissolved.
- Wrote: sources (+4); budgets (+11); commitments (+1); leaderboard (+1 pi 5.04); entities (+1 vzw_mater_dei_brasschaat); foi + draft `gap_materdei_opgroeien_matrix_bruto_469k_omzet73_empty_pnl_drop_6k_destin_empty_l5`; rq_2468=done + rq_2469 open; loop_state ticks=2468; raw tick2468/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2470**). Next: rq_2469 unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Mater Dei remine / NOT Savio remine / NOT Paideia remine / NOT Ooievaarsnest remine / NOT De Zonnekindjes remine / NOT D'n Opvang remine / NOT CAR Overleie remine / NOT Gesticht remine / NOT Grauwzusters convent / NOT HOCUS-POCUS remine / NOT VKA remine / NOT Soetkin remine / NOT t Sloeberke remine / NOT CAR Accent remine / NOT De Groene Verte remine / NOT De Vleugels remine / NOT De Pallieterkes remine / NOT De Medemens Kinderdagverblijven remine / NOT De Medemens parent remine / NOT OKO & ZO remine / NOT Harlekijntjes remine / NOT Hartjes remine / NOT De Wissel remine / NOT Familia remine / NOT BKO GENK-OOST remine / NOT Peutertuinen GO Mariakerke remine / NOT Mini-creches GO Next remine / NOT WZC OLVA remine / NOT Hebe training / NOT Quattro remine / NOT GERUST zorgcentrale / NOT Zo Groot remine / NOT De Elfjes remine / NOT De Steijgertjes remine / NOT Vormingscentrum training / NOT Zwarte Zusters dissolved / NOT Dominiek Savio remine / NOT EVA Dilbeek remine / NOT WZC Mater Dei Heikruis remine). NOW leftover candidate: KDV Vijverbeek 0448.164.744 leftover city_asse unused YE2025 **2026-00119084** CDN **200** 258kB — take ONLY if unused + official native-text YE2025 PDF. Infano 0477.578.411 leftover city_ternat unused YE2025 **2026-00205409** CDN **200** 559kB — take ONLY if unused + official native-text YE2025 PDF. Hupskadee 0863.886.651 leftover city_begijnendijk 2026 deposits — take ONLY if unused + official YE2025 native PDF. Villa Boempatat 0660.616.520 leftover city_gent YE2025 **2026-00396513** CDN **403** / SCAN — take ONLY if unused + official native-text YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen unused YE2025 **2026-00374905** CDN **403** — take ONLY if unused + CDN 200 native YE2025 PDF. Kinderlach leftover city_eeklo still YE2024 — take ONLY if unused + official YE2025 PDF. De Linde Ronse leftover city_ronse still YE2024 — take ONLY if unused + official YE2025 PDF. H.Hart Kortrijk leftover city_kortrijk still YE2024 — take ONLY if unused + official YE2025 PDF. Jessa leftover city_hasselt hospital YE2025 PDF — take ONLY if unused + official YE2025 euros extract. De Bolster 0861.680.989 YE2025 zetel Zwalm — leftover of mined parent only. Familiehulp De Speelboom YE2025 Brussels zetel — leftover-via-VE not enough per LOOP.md. Mini-creches GO! Next leftover city_hasselt still YE2024 — skip unless YE2025. Zo Groot Oostende leftover city_oostende still YE2024 — skip unless YE2025. Vormingscentrum leftover city_gent training — skip. VBJK leftover city_gent training — skip. Helan Kinderopvang Helan-HH-adjacent — skip. Hebe Kenniscentrum training — skip. Tick **2470** is next every-10.
"""
with log.open("ab") as f:
    f.write(entry.encode("utf-8"))
print("loop_log ok")
print("WRITE CORE DONE")
