from pathlib import Path
import csv
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2469_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_vijverbeek_jr2025_nbb_pdf_2469"
SRC_KBO="src_vijverbeek_kbo_2469"
SRC_SBM="src_vijverbeek_sbm_2469"
SRC_SITE="src_vijverbeek_site_2469"
EID="vzw_vijverbeek_asse"
GAP="gap_vijverbeek_opgroeien_matrix_bruto_1211k_omzet73_empty_pnl_jump_100k_destin_empty_l5"
COMM="comm_vijverbeek_jr2025_statutory_bruto_1211k_omzet73_empty_pnl_jump_100k"
LB="lb_vijverbeek_bruto_1211k_omzet73_empty_pnl_jump_100k_destin_empty_jr2025"
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
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Kinderdagverblijf Vijverbeek deposit 2026-00119084,http://cdn.staatsbladmonitor.be/2026pdf/2026-00119084.pdf,NBB official WVV deposit PDF,{DAY},budget,tick2469; official native PDF 258436 bytes 15p VKT-VZW 23.0.9 m04-f; header 19.05.2026; AV 05.05.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-05-23 05:15:24 UTC OpenPDF 1.3.26; all 15p native; CDN 2026-00119084 GET 200 Last-Modified 09.06.2026; VKT-VZW 6.1.1 6.2 6.5 6.6 7 8 niet dienstig; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Kinderdagverblijf Vijverbeek 0448.164.744,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0448164744,KBO Public Search FOD Economie,{DAY},official_register,tick2469; Actief; 1 VE 2.156.481.234 KINDERDAGVERBLIJF VIJVERBEEK vzw Nieuwstraat 126 since 05.10.2006; VZW since 12.06.1992; begindatum 12.06.1992; zetel Nieuwstraat 126 1730 Asse since 01.01.2016; FOI directie@kdv-vijverbeek.be; leftover mined city_asse CIK; NOT 3Wplus Kinderopvang Asse 0893.870.539 remine; NOT Mater Dei 0431.168.859 remine",
f"{SRC_SBM},NBB Consult / SBM fiche Kinderdagverblijf Vijverbeek 0448164744 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0448164744,NBB Consult / SBM,{DAY},official_register,tick2469; deposit-id 2026-00119084 YE 01.01.2025-31.12.2025 filing 19.05.2026 published 19.05.2026 VKT-VZW Verkort Initial; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},Vijverbeek FOI contact leftover city_asse CIK,https://kdv-vijverbeek.be/,VZW Kinderdagverblijf Vijverbeek leftover city_asse CIK Opgroeien groepsopvang 66 plaatsen,{DAY},foi_contact,tick2469; FOI directie@kdv-vijverbeek.be; zetel Nieuwstraat 126 1730 Asse; Kind en Gezin sitenummer 910021814; 1 VE leftover mined city_asse after Mater Dei different-city skip; NOT 3Wplus remine; NOT Mater Dei remine; NOT Savio remine; NOT WZC Mater Dei Heikruis remine; NOT Paideia remine; NOT Ooievaarsnest remine; NOT DE ZONNEKINDJES remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Kinderlach YE2024; NOT Helan; NOT De Speelboom Brussels; NOT Villa Boempatat SCAN/CDN403; NOT Elief CDN 403; NOT Hebe training; NOT Zo Groot YE2024; NOT De Bolster Zwalm not leftover mined parent; NOT GERUST zorgcentrale; NOT Vormingscentrum training; NOT Zwarte Zusters dissolved",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},Kinderdagverblijf Vijverbeek,ASBL Kinderdagverblijf Vijverbeek,Kinderdagverblijf Vijverbeek VZW (leftover city_asse CIK),parastatal,city_asse,nl,https://kdv-vijverbeek.be/,directie@kdv-vijverbeek.be,Nieuwstraat 126 1730 Asse,tick2469 YE2025 Strong official native NBB PDF deposit 2026-00119084 + Strong KBO 0448.164.744 Actief 1 VE 2.156.481.234; omzet70 empty VKT; 73 empty VKT; 76A empty; envelope bruto 9900 JUMP 1210775; bruto JUMP 1210775; pnl JUMP 100245; 9901 JUMP 105664; equity JUMP 975164; assets JUMP 1275877; debt JUMP 300713; FTE JUMP 15.5; kapitaalsubsidies DROP 466191; destin691 empty; 791 empty; cash JUMP 250304; geldbeleggingen empty; leftover city_asse CIK 66 plaatsen; NOT 3Wplus Kinderopvang Asse 0893.870.539 remine; NOT Mater Dei 0431.168.859 remine; NOT WZC Mater Dei Heikruis remine; NOT Savio Dilbeek 0472.564.501 remine; NOT Dominiek Savio remine; NOT EVA Dilbeek 0477.276.325 remine; NOT Paideia 0445.129.931 remine; NOT Ooievaarsnest 0418.588.256 remine; NOT DE ZONNEKINDJES 0416.541.952 remine; NOT D'n Opvang 0676.442.465 remine; NOT CAR Overleie 0454.250.505 remine; NOT Gesticht 0410.918.031 remine; NOT HOCUS-POCUS 0466.893.167 remine; NOT VKA 0433.480.132 remine; NOT Soetkin 0443.641.970 remine; NOT t Sloeberke 0410.973.360 remine; NOT CAR Accent 0413.208.122 remine; NOT De Elfjes 0455.636.912 remine; NOT De Steijgertjes 0413.421.720 remine; NOT H.Hart WZC 0413.595.330; NOT Zo Groot 0818.420.771 leftover city_oostende YE2024; NOT De Groene Verte 0465.061.649 remine; NOT De Vleugels 0431.408.290 remine; NOT De Pallieterkes 0418.538.865 remine; NOT De Medemens KDV 0893.678.915 remine; NOT De Medemens parent 0428.692.191 remine; NOT OKO & ZO 0862.154.608 remine; NOT Harlekijntjes 0407.700.403 remine; NOT Hartjes Ninove 0446.391.327 remine; NOT Hartjes Tienen 0441.374.348 remine; NOT De Wissel 0421.913.376 remine; NOT Familia 0461.401.779; NOT Peutertuinen GO Mariakerke 0410.221.116; NOT Mini-creches GO Next 0896.468.060 leftover city_hasselt YE2024; NOT Kinderlach 0450.275.186; NOT Helan; NOT De Speelboom Brussels; NOT Villa Boempatat 0660.616.520 leftover city_gent YE2025 SCAN/CDN403 2026-00396513; NOT Elief 0451.624.377 CDN 403; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; NOT De Bolster 0861.680.989 YE2025 zetel Zwalm city_zwalm not mined; NOT GERUST 0776.808.068 zorgcentrale; NOT Jessa hospital special schema; NOT Vormingscentrum 0413.342.338 training; NOT Zwarte Zusters 0413.272.260 dissolved; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria SCAN; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Zo Groot Oostende YE2024 not taken; H.Hart Kortrijk YE2024 not taken; Infano Ternat 0477.578.411 unused YE2025 not taken; Hupskadee 0863.886.651 leftover city_begijnendijk year TBD not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_vijverbeek_omzet_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 70 omzet YE2025 empty (VKT; envelope is bruto 9900),{SRC_PDF},strong,tick2469; PDF p5 native; YE2024 empty; 73 empty; 76A empty",
f"bud_vijverbeek_73_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 empty (VKT),{SRC_PDF},strong,tick2469; PDF p5 native; YE2024 empty; FOI Opgroeien matrix behind envelope 1210775",
f"bud_vijverbeek_opbr_jr2025_statutory,{EID},2025,1210775,1210775,1210775,NBB VKT-VZW envelope bruto 9900 YE2025 JUMP +8.85% (omzet empty so envelope is bruto 9900),{SRC_PDF},strong,tick2469; PDF p5 native; YE2024 1112383; 70 empty; 73 empty; 76A empty",
f"bud_vijverbeek_bruto_jr2025_statutory,{EID},2025,1210775,1210775,1210775,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +8.85% (VKT envelope because omzet empty),{SRC_PDF},strong,tick2469; PDF p5 native; YE2024 1112383; 76A empty; 73 empty",
f"bud_vijverbeek_pnl_jr2025_statutory,{EID},2025,100245,100245,100245,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 JUMP +89.68% (was 52849),{SRC_PDF},strong,tick2469; PDF p5 native; YE2024 52849; bedrijfswinst 9901 105664 JUMP; destin691 empty",
f"bud_vijverbeek_bedrijfswinst_jr2025_statutory,{EID},2025,105664,105664,105664,NBB VKT-VZW code 9901 bedrijfswinst YE2025 JUMP +74.53% (was 60542),{SRC_PDF},strong,tick2469; PDF p5 native; YE2024 60542; 62 992152 JUMP; 630 106561 DROP; 66A empty; 640/8 1977 JUMP; 635/9 empty; 631/4 4421 JUMP",
f"bud_vijverbeek_equity_jr2025_statutory,{EID},2025,975164,975164,975164,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +5.13%,{SRC_PDF},strong,tick2469; PDF p4 native; YE2024 927610; kapitaalsubsidies 466191 DROP; overgedragen 14 508973 JUMP; fondsen 10 empty; bestemde fondsen 13 empty",
f"bud_vijverbeek_assets_jr2025_statutory,{EID},2025,1275877,1275877,1275877,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +4.04%,{SRC_PDF},strong,tick2469; PDF p3 native; YE2024 1226283; MVA 22/27 897058 DROP; cash 250304 JUMP; geldbeleggingen empty; aanbouw 27 empty",
f"bud_vijverbeek_debt_jr2025_statutory,{EID},2025,300713,300713,300713,NBB VKT-VZW code 17/49 schulden YE2025 JUMP +0.68%,{SRC_PDF},strong,tick2469; PDF p4 native; YE2024 298673; 17 124597 DROP; 42/48 176116 JUMP",
f"bud_vijverbeek_cash_jr2025_statutory,{EID},2025,250304,250304,250304,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +71.68%,{SRC_PDF},strong,tick2469; PDF p3 native; YE2024 145793; geldbeleggingen 50/53 empty",
f"bud_vijverbeek_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty (destin empty; 14 JUMP 508973 = prior 408728 + pnl 100245),{SRC_PDF},strong,tick2469; PDF p6 native; YE2024 destin empty; bestemde fondsen 13 empty FOI",
])
print("entities+budgets ok")

cash_json=(
"\"{\"\"2025_omzet\"\":0,\"\"2025_73\"\":0,\"\"2025_76A\"\":0,"
"\"\"2025_opbr70_76A\"\":1210775,\"\"2025_bruto\"\":1210775,"
"\"\"2025_pnl\"\":100245,\"\"2025_bedrijfswinst\"\":105664,"
"\"\"2025_equity\"\":975164,\"\"2025_assets\"\":1275877,\"\"2025_debt\"\":300713,"
"\"\"2025_fte\"\":15.5,\"\"2025_kapitaalsubsidies\"\":466191,\"\"2025_destin691\"\":0,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":250304,\"\"2025_geldbeleggingen\"\":0,"
"\"\"2025_personnel62\"\":992152,\"\"2025_gebouwen22\"\":853311,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":0,"
"\"\"2025_fondsen10\"\":0,\"\"2025_overgedragen14\"\":508973,"
"\"\"2025_bestemdefondsen13\"\":0,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":106561,\"\"2025_capex\"\":12968,"
"\"\"2024_omzet\"\":0,\"\"2024_73\"\":0,"
"\"\"2024_opbr70_76A\"\":1112383,\"\"2024_bruto\"\":1112383,\"\"2024_pnl\"\":52849,\"\"2024_bedrijfswinst\"\":60542,"
"\"\"2024_equity\"\":927610,\"\"2024_assets\"\":1226283,"
"\"\"2024_debt\"\":298673,\"\"2024_cash\"\":145793,\"\"2024_fte\"\":14.2,"
"\"\"2024_destin691\"\":0,\"\"2024_kapitaalsubsidies\"\":518882,\"\"2024_76A\"\":0,"
"\"\"2024_geldbeleggingen\"\":0}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Kinderdagverblijf Vijverbeek YE2025 (bruto JUMP 1.21m / omzet+73 empty VKT / pnl JUMP 100k / destin empty / Strong PDF),{EID},Opgroeien + leftover city_asse CIK,VZW Kinderdagverblijf Vijverbeek (KBO 0448.164.744; Actief; 1 VE 2.156.481.234; zetel Asse),2026-05-05,2025,2025,1210775,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00119084.pdf,Public CIK dual of mined city_asse,Publish Opgroeien matrix behind envelope 1.21m + why omzet+73 empty VKT and why pnl JUMP 100245 while destin empty and cash JUMP 250304,{SRC_PDF},strong,Vlaanderen>Vlaams-Brabant>Asse>Kinderdagverblijf Vijverbeek>JR2025_statutory_L5,tick2469; Strong official native PDF; leftover mined city_asse CIK; 1 VE; prior-year identical; NOT every-10; NOT 3Wplus remine; NOT Mater Dei remine; NOT WZC Mater Dei Heikruis remine; NOT Savio remine; NOT Dominiek Savio remine; NOT EVA Dilbeek remine; NOT Paideia remine; NOT Ooievaarsnest remine; NOT DE ZONNEKINDJES remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Kinderlach YE2024; NOT Zo Groot YE2024; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"Kinderdagverblijf Vijverbeek bruto JUMP 1.21m / omzet+73 empty VKT / pnl JUMP 100k / destin empty (YE2025 leftover city_asse CIK)",
"L5",
"cik_vzw_statutory",
"Vlaanderen>Vlaams-Brabant>Asse>Kinderdagverblijf Vijverbeek>JR2025",
"1210775",
"1210775",
"PDF envelope 1210775 = bruto 9900 VKT because omzet empty; 70 empty; 73 empty; 76A empty; bruto 1210775; bedrijfswinst JUMP 105664; pnl JUMP 100245; equity JUMP 975164; assets JUMP 1275877; debt JUMP 300713; FTE 15.5; kapitaalsubsidies 466191 DROP; destin691 empty; cash JUMP 250304; leftover city_asse CIK",
"strong",
SRC_PDF,
"Opgroeien + leftover city_asse CIK",
"CIK / Kind en Gezin groepsopvang leftover city_asse",
"1.21m envelope; omzet+73 empty VKT; pnl JUMP 100245; destin empty; leftover city_asse CIK",
"5.16",
"5.00",
"5.08",
"5.12",
"FOI Opgroeien matrix behind envelope 1.21m + why omzet+73 empty VKT and why pnl JUMP 100245 while destin empty and cash JUMP 250304",
"active",
"",
"tick2469 leftover mined city_asse CIK after Mater Dei different-city skip; 1 VE; prior-year identical; NOT every-10; NOT 3Wplus remine; NOT Mater Dei remine; NOT WZC Mater Dei Heikruis remine; NOT Savio remine; NOT Dominiek Savio remine; NOT EVA Dilbeek remine; NOT Paideia remine; NOT Ooievaarsnest remine; NOT DE ZONNEKINDJES remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Kinderlach YE2024; NOT Zo Groot YE2024; NOT Elief CDN 403; NOT Villa Boempatat SCAN/CDN403; NOT De Speelboom Brussels; NOT De Elfjes remine; NOT De Steijgertjes remine",
])
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>Vlaams-Brabant>Asse>Kinderdagverblijf Vijverbeek>CIK",
"entity_id": EID,
"what_is_missing": "Opgroeien split behind envelope 1210775 (omzet 70 empty + 73 empty + 76A empty; VKT bruto 9900) and why destin empty while pnl JUMP 100245 and cash JUMP 250304",
"why_it_matters": "Strong official PDF leftover public CIK of mined city_asse; VKT envelope bruto 1.21m because omzet empty; public Opgroeien groepsopvang 66 plaatsen Nieuwstraat 126",
"priority": "8",
"recipient_body": "VZW Kinderdagverblijf Vijverbeek / Raad van Bestuur",
"recipient_email": "directie@kdv-vijverbeek.be",
"recipient_postal": "Nieuwstraat 126 1730 Asse",
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
"notes": "tick2469; ready NOT sent; Strong official native NBB PDF; leftover mined city_asse CIK after Mater Dei different-city skip; 1 VE; prior-year identical; NOT every-10; off 3Wplus remine; off Mater Dei remine",
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
if rq_raw.count(b"rq_2469,")!=1: raise SystemExit(f"bad 2469 count {rq_raw.count(b'rq_2469,')}")
if b"rq_2470," in rq_raw: raise SystemExit("2470 exists")
idx=rq_raw.rfind(b"rq_2469,")
if idx<0: raise SystemExit("rq_2469 not found")
new_2469=(
"rq_2469,leftover dual Kinderdagverblijf Vijverbeek YE2025,hole_fill,8,done,L5,vzw_vijverbeek_asse,"
"Took unused leftover public CIK Kinderdagverblijf Vijverbeek 0448.164.744 leftover mined city_asse. Official NBB VKT-VZW YE2025 2026-00119084 native 15p. Envelope bruto 9900 JUMP 1210775 (omzet+73 empty VKT); pnl JUMP 100245; destin empty; FTE 15.5. NOT 3Wplus remine. NOT Mater Dei remine. NOT Kinderlach YE2024.,"
f",{STAMP},{STAMP},tick2469 leftover mined city_asse CIK; Strong native PDF; 1 VE; prior-year identical; next every-10 is 2470\n"
)
new_2470=(
"rq_2470,leftover dual after Kinderdagverblijf Vijverbeek — hunt unused public dual + every-10,hole_fill,8,open,L5,,"
"EVERY-10 tick after Kinderdagverblijf Vijverbeek YE2025. Refresh progress_every_10_ticks.md + doge_waste_top10_current.md. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf. Infano 0477.578.411 leftover city_ternat YE2025 2026-00205409 — take ONLY if unused + official native-text YE2025 PDF. Hupskadee 0863.886.651 leftover city_begijnendijk 2026 deposits — take ONLY if unused + official YE2025 native PDF. Villa Boempatat 0660.616.520 leftover city_gent YE2025 2026-00396513 CDN 403 / SCAN — take ONLY if unused + official native-text YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen YE2025 2026-00374905 CDN 403 — take ONLY if CDN 200 native. Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO! Next / Zo Groot Oostende still YE2024 — take ONLY if unused + official YE2025 PDF. De Bolster 0861.680.989 YE2025 2026-00210039 zetel Zwalm (city_zwalm not mined) — take ONLY if leftover of a mined parent. Jessa leftover city_hasselt hospital YE2025 PDF — take ONLY if unused + official YE2025 euros extract. NOT Vijverbeek remine. NOT Mater Dei remine. NOT Savio remine. NOT 3Wplus remine. NOT Paideia remine. NOT Ooievaarsnest remine. NOT De Zonnekindjes remine. NOT D'n Opvang remine. NOT CAR Overleie remine. NOT Gesticht remine. NOT Grauwzusters convent. NOT Hocus-Pocus remine. NOT VKA remine. NOT Soetkin remine. NOT t Sloeberke remine. NOT CAR Accent remine. NOT De Groene Verte remine. NOT De Vleugels remine. NOT De Pallieterkes remine. NOT De Medemens remine. NOT OKO & ZO remine. NOT Harlekijntjes remine. NOT Hartjes remine. NOT De Wissel remine. NOT Familia remine. NOT Helan. NOT Hebe training. NOT WZC OLVA remine. NOT De Speelboom Brussels. NOT GERUST zorgcentrale. NOT Zo Groot remine. NOT De Elfjes remine. NOT De Steijgertjes remine. NOT Vormingscentrum training. NOT Zwarte Zusters dissolved. NOT Dominiek Savio remine. NOT EVA Dilbeek remine. NOT WZC Mater Dei Heikruis remine.,"
f",{STAMP},{STAMP},spawned after tick2469; Vijverbeek taken leftover mined city_asse CIK; Mater Dei taken leftover mined city_brasschaat CIK; Savio taken leftover mined city_dilbeek CIK; Paideia taken leftover mined city_brugge CIK; Ooievaarsnest taken leftover mined city_tienen CIK; Zonnekindjes taken leftover mined city_diepenbeek CIK; D'n Opvang taken leftover mined city_oostende CIK; CAR Overleie taken leftover mined city_kortrijk CAR; Gesticht taken leftover mined city_ieper CIK convent-class check PASSED; Hocus-Pocus taken leftover mined city_roeselare CIK; VKA taken leftover mined city_antwerpen CIK; Soetkin taken leftover mined city_kortrijk CIK; t Sloeberke taken leftover mined city_kortrijk CIK; De Groene Verte taken leftover mined city_houthulst WZC; THIS TICK IS EVERY-10\n"
)
if new_2469.count("\n")!=1 or new_2470.count("\n")!=1: raise SystemExit("bad rq newlines")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2469.encode("utf-8"))
    f.write(new_2470.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2469", chk.count(b"rq_2469,"), "n2470", chk.count(b"rq_2470,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2469,2469,no,tick2469 leftover dual Kinderdagverblijf Vijverbeek 0448.164.744 Strong native PDF (omzet70 empty VKT; 73 empty VKT; 76A empty; envelope bruto 9900 JUMP 1210775; bruto JUMP 1210775; pnl JUMP 100245; 9901 JUMP 105664; equity JUMP 975164; assets JUMP 1275877; debt JUMP 300713; FTE JUMP 15.5; kapitaalsubsidies DROP 466191; destin691 empty; 791 empty; cash JUMP 250304; geldbeleggingen empty; 1 VE leftover city_asse CIK); leftover mined city_asse CIK; prior-year identical; NOT 3Wplus remine; NOT Mater Dei remine; NOT WZC Mater Dei Heikruis remine; NOT Savio remine; NOT Dominiek Savio remine; NOT EVA Dilbeek remine; NOT Paideia remine; NOT Ooievaarsnest remine; NOT DE ZONNEKINDJES remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT Grauwzusters convent; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens KDV remine; NOT De Medemens parent remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Mini-creches GO Next remine; NOT Kinderlach; NOT Zo Groot YE2024; NOT De Speelboom Brussels; NOT Elief CDN 403; NOT Villa Boempatat SCAN/CDN403; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; NOT De Bolster Zwalm not leftover mined parent; NOT GERUST zorgcentrale; NOT De Elfjes remine; NOT De Steijgertjes remine; NOT Vormingscentrum training; NOT Zwarte Zusters dissolved; next every-10 is 2470; next rq_2470 leftover dual + every-10\n",
encoding="utf-8",
)
print("loop_state ok")

log=ROOT/"docs/doge/loop_log.md"
log_raw=log.read_bytes()
if not log_raw.endswith(b"\n"): raise SystemExit("loop_log no LF")
entry=f"""
### {STAMP} - tick 2469 - rq_2469 Kinderdagverblijf Vijverbeek (bruto JUMP 1.21m / omzet+73 empty VKT / pnl JUMP 100k / destin empty / Strong PDF)

- Unit: **rq_2469** leftover dual after **Mater Dei@2468**. Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024** (not re-downloaded); FARO 2026-00010398 still **YE2024** (HEAD-only policy Last-Modified 21.01.2026; not re-downloaded); AIESH/Gandae/Aralea/Manupal/Vlotter still **YE2024**. Zeepreventorium still **YE2024**. Drongen named+unnamed CARs **exhausted** — De Elfjes Kloosterstraat 6 already mined. Kohesi family **exhausted**. Quattro WZC members **exhausted** except already-in-entities St Jozef Zonnebeke / Sint-Vincentius Avelgem. CAR Antenne 3000 leftover city_leuven CDN still **403**. AZ Sint-Maria leftover city_halle YE2025 SCAN — not taken. CAR Noorderkempen leftover city_wuustwezel still SCAN. De Linde Ronse leftover city_ronse still **YE2024**. Kinderlach leftover city_eeklo still **YE2024**. Villa Boempatat leftover city_gent **YE2025** **2026-00396513** CDN **403** / SCAN no extractable euros — not taken. Woon en Zorg H. Hart Kortrijk leftover city_kortrijk still **YE2024**. Jessa leftover city_hasselt hospital YE2025 PDF / hospital special schema — not taken. Mini-creches GO! Next leftover city_hasselt still **YE2024**. Zo Groot Oostende leftover city_oostende still **YE2024** (2026-00055086 is YE2024; second 2026 deposit is YE2023 restatement). Familiehulp De Speelboom YE2025 unused Brussels zetel — not taken. Speelhuis Elief leftover city_antwerpen unused YE2025 **2026-00374905** CDN **403** — not taken. Hebe Kenniscentrum leftover city_antwerpen training — skip. WZC OLVA leftover city_antwerpen already in entities — do not remine. De Bolster 0861.680.989 YE2025 zetel Zwalm (city_zwalm not mined) — not taken. GERUST Zorgcentrale leftover city_herentals YE2025 — zorgcentrale not in dual types — not taken. Vormingscentrum 0413.342.338 leftover city_gent training — skip. Helan Kinderopvang 0464.151.037 already skipped. Zwarte Zusters 0413.272.260 dissolved — skip. Mater Dei 0431.168.859 just mined — do not remine. Savio 0472.564.501 already mined — do not remine. Paideia 0445.129.931 already mined — do not remine. Ooievaarsnest 0418.588.256 already mined — do not remine. DE ZONNEKINDJES 0416.541.952 already mined — do not remine. D'n Opvang 0676.442.465 already mined — do not remine. CAR Overleie already mined — do not remine. Gesticht already mined — do not remine. HOCUS-POCUS already mined — do not remine. VKA already mined — do not remine. Soetkin already mined — do not remine. t Sloeberke already mined — do not remine. De Groene Verte already mined — do not remine. De Vleugels already mined — do not remine. De Pallieterkes already mined — do not remine. De Medemens Kinderdagverblijven already mined — do not remine. De Medemens parent already mined — do not remine. CAR Accent already mined — do not remine. De Elfjes 0455.636.912 already mined — do not remine. De Steijgertjes 0413.421.720 already mined — do not remine. Hartjes Tienen 0441.374.348 already mined — do not remine. De Wissel 0421.913.376 already mined — do not remine. Grauwzusters Franciscanessen Hasselt 0409.771.748 leftover city_hasselt convent skip. EVA-vzw Gemeentelijke Kinderopvang Dilbeek 0477.276.325 already mined — do not remine. Dominiek Savio Hooglede VAPH already mined — do not remine. 3Wplus Kinderopvang Asse 0893.870.539 already mined — do not remine. First leftover unused + live official YE2025 native euros: took FREE leftover Flemish **VZW Kinderdagverblijf Vijverbeek** YE2025 (KBO **0448.164.744**; zetel Nieuwstraat 126 1730 Asse; **Actief** **1 VE** **2.156.481.234** KINDERDAGVERBLIJF VIJVERBEEK vzw Nieuwstraat 126 since 05.10.2006; RSZ2025 **88.911**; leftover of mined **city_asse**; directie@kdv-vijverbeek.be; Opgroeien groepsopvang **66 plaatsen**; Kind en Gezin sitenummer **910021814**). Identity trap: Kinderdagverblijf Vijverbeek 0448.164.744 ≠ 3Wplus Kinderopvang VZW Asse **0893.870.539** leftover city_asse already mined; ≠ Groepsopvang Mater Dei **0431.168.859** leftover city_brasschaat just mined; ≠ WZC Mater Dei Heikruis Pepingen already in entities; ≠ Kinderdagverblijf Savio **0472.564.501** leftover city_dilbeek already mined; ≠ Dominiek Savio VZW Hooglede-Gits VAPH already mined; ≠ EVA-vzw Gemeentelijke Kinderopvang Dilbeek **0477.276.325** leftover city_dilbeek already mined; ≠ Paideia **0445.129.931** leftover city_brugge already mined; ≠ KDV Ooievaarsnest **0418.588.256** leftover city_tienen already mined; ≠ DE ZONNEKINDJES **0416.541.952** leftover city_diepenbeek already mined; ≠ D'n Opvang **0676.442.465** leftover city_oostende already mined; ≠ De Elfjes **0455.636.912** already mined; ≠ De Steijgertjes **0413.421.720** already mined; ≠ CAR Overleie **0454.250.505**; ≠ Gesticht **0410.918.031**; ≠ HOCUS-POCUS **0466.893.167**; ≠ VKA **0433.480.132**; ≠ Soetkin **0443.641.970**; ≠ t Sloeberke **0410.973.360**; ≠ CAR Accent **0413.208.122**; ≠ Speelhuis Elief **0451.624.377**; ≠ Villa Boempatat **0660.616.520**; ≠ De Groene Verte **0465.061.649**; ≠ De Vleugels **0431.408.290**; ≠ De Pallieterkes **0418.538.865**; ≠ De Medemens Kinderdagverblijven **0893.678.915**; ≠ De Medemens **0428.692.191**; ≠ OKO & ZO **0862.154.608**; ≠ Harlekijntjes **0407.700.403**; ≠ Hartjes Ninove **0446.391.327**; ≠ Hartjes Tienen **0441.374.348**; ≠ De Wissel **0421.913.376**; ≠ Ferm Kinderopvang **0416.117.627**; ≠ Familia **0461.401.779**; ≠ Peutertuinen GO Mariakerke **0410.221.116**; ≠ Mini-crèches GO! Next **0896.468.060**; ≠ Kinderlach **0450.275.186**; ≠ Helan 0464.151.037; ≠ Hebe **0451.789.772**; ≠ WZC OLVA **0430.977.136**; ≠ H.Hart Kortrijk **0413.595.330**; ≠ De Linde Ronse **0778.279.401**; ≠ De Bolster **0861.680.989**; ≠ GERUST **0776.808.068**; ≠ Jessa **0821.142.117**; ≠ AZ Sint-Maria **0467.967.491**; ≠ TKDV Het Veer Kloosterstraat 6; ≠ Vormingscentrum **0413.342.338** training; ≠ Zwarte Zusters **0413.272.260** dissolved; ≠ Infano **0477.578.411** leftover city_ternat unused YE2025; ≠ Hupskadee **0863.886.651**. 1 VE Asse — leftover of mined city_asse (zetel + 1/1 VE Nieuwstraat 126). Confirmed leftover public (Opgroeien CIK groepsopvang 66 plaatsen; Kind en Gezin-vergund sitenummer 910021814) not convent / not private clinic / not school / not OVBJ / not WZC / not VAPH / not Ferm / not 3Wplus remine / not Mater Dei remine. VKT-VZW **native text** (not scan) — 258436 B / 15p all native euros (VKT-VZW 6.1.1 / 6.2 / 6.5 / 6.6 / 7 / 8 niet dienstig).
- Found: official NBB VKT-VZW native PDF deposit **2026-00119084** (258436 B / 15p; AV **05.05.2026**; header **19.05.2026**; CDN Last-Modified **09.06.2026**; CreationDate 23.05.2026 OpenPDF 1.3.26; all 15p native; prior-year identical not restated) — omzet 70 **empty** VKT; 73 **empty** VKT; 76A **empty**; envelope bruto 9900 **EUR1210775** JUMP +8.85% (VKT envelope because omzet empty; was 1112383); bruto 9900 **EUR1210775** JUMP +8.85%; 62 **EUR992152** JUMP +5.67%; 630 **EUR106561** DROP −4.03%; 66A **empty**; 640/8 **EUR1977** JUMP +3.35%; 635/9 **empty**; 631/4 **EUR4421** JUMP (was empty); bedrijfswinst 9901 **EUR105664** JUMP +74.53%; pnl 9904 **EUR100245** JUMP +89.68%; equity **EUR975164** JUMP +5.13%; assets **EUR1275877** JUMP +4.04%; debt **EUR300713** JUMP +0.68%; FTE **15.5** JUMP +9.15% (was 14.2; 100 15.5; 105 16.3; 9087 15.5); kapitaalsubsidies **EUR466191** DROP −10.16%; destin 691 **empty** (791 empty; 14 JUMP 508973 = prior 408728 + pnl 100245); 791 **empty**; cash **EUR250304** JUMP +71.68%; geldbeleggingen **empty**; gebouwen **EUR853311** DROP; MVA 22/27 **EUR897058** DROP; aanbouw **empty**; capex **EUR12968**; fondsen 10 **empty**; overgedragen 14 **EUR508973** JUMP; bestemde fondsen 13 **empty**; voorzieningen 16 **empty**. Strong KBO + Strong PDF (native all pages; not SBM table; not Companyweb euros). Site: 1 VE leftover mined city_asse CIK. NOT 3Wplus remine. NOT Mater Dei remine. NOT WZC Mater Dei Heikruis remine. NOT Savio remine. NOT Dominiek Savio remine. NOT EVA Dilbeek remine. NOT Paideia remine. NOT Ooievaarsnest remine. NOT DE ZONNEKINDJES remine. NOT D'n Opvang remine. NOT CAR Overleie remine. NOT Gesticht remine. NOT Grauwzusters convent. NOT HOCUS-POCUS remine. NOT VKA remine. NOT Soetkin remine. NOT t Sloeberke remine. NOT CAR Accent remine. NOT De Groene Verte remine. NOT De Vleugels remine. NOT De Pallieterkes remine. NOT De Medemens remine. NOT OKO & ZO remine. NOT Harlekijntjes remine. NOT Hartjes remine. NOT De Wissel remine. NOT Familia remine. NOT Mini-creches GO Next Hasselt. NOT Kinderlach. NOT Helan. NOT De Speelboom Brussels. NOT Elief CDN 403. NOT Villa Boempatat SCAN/CDN403. NOT Hebe training. NOT WZC OLVA remine. NOT Zo Groot YE2024. NOT De Bolster Zwalm. NOT GERUST zorgcentrale. NOT Vormingscentrum training. NOT Zwarte Zusters dissolved.
- Wrote: sources (+4); budgets (+11); commitments (+1); leaderboard (+1 pi 5.12); entities (+1 vzw_vijverbeek_asse); foi + draft `gap_vijverbeek_opgroeien_matrix_bruto_1211k_omzet73_empty_pnl_jump_100k_destin_empty_l5`; rq_2469=done + rq_2470 open; loop_state ticks=2469; raw tick2469/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2470** IS every-10). Next: rq_2470 unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere + every-10 progress (NOT Vijverbeek remine / NOT Mater Dei remine / NOT Savio remine / NOT 3Wplus remine / NOT Paideia remine / NOT Ooievaarsnest remine / NOT De Zonnekindjes remine / NOT D'n Opvang remine / NOT CAR Overleie remine / NOT Gesticht remine / NOT Grauwzusters convent / NOT HOCUS-POCUS remine / NOT VKA remine / NOT Soetkin remine / NOT t Sloeberke remine / NOT CAR Accent remine / NOT De Groene Verte remine / NOT De Vleugels remine / NOT De Pallieterkes remine / NOT De Medemens Kinderdagverblijven remine / NOT De Medemens parent remine / NOT OKO & ZO remine / NOT Harlekijntjes remine / NOT Hartjes remine / NOT De Wissel remine / NOT Familia remine / NOT BKO GENK-OOST remine / NOT Peutertuinen GO Mariakerke remine / NOT Mini-creches GO Next remine / NOT WZC OLVA remine / NOT Hebe training / NOT Quattro remine / NOT GERUST zorgcentrale / NOT Zo Groot remine / NOT De Elfjes remine / NOT De Steijgertjes remine / NOT Vormingscentrum training / NOT Zwarte Zusters dissolved / NOT Dominiek Savio remine / NOT EVA Dilbeek remine / NOT WZC Mater Dei Heikruis remine). NOW leftover candidate: Infano 0477.578.411 leftover city_ternat unused YE2025 **2026-00205409** CDN **200** 559kB — take ONLY if unused + official native-text YE2025 PDF. Hupskadee 0863.886.651 leftover city_begijnendijk 2026 deposits — take ONLY if unused + official YE2025 native PDF. Villa Boempatat 0660.616.520 leftover city_gent YE2025 **2026-00396513** CDN **403** / SCAN — take ONLY if unused + official native-text YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen unused YE2025 **2026-00374905** CDN **403** — take ONLY if unused + CDN 200 native YE2025 PDF. Kinderlach leftover city_eeklo still YE2024 — take ONLY if unused + official YE2025 PDF. De Linde Ronse leftover city_ronse still YE2024 — take ONLY if unused + official YE2025 PDF. H.Hart Kortrijk leftover city_kortrijk still YE2024 — take ONLY if unused + official YE2025 PDF. Jessa leftover city_hasselt hospital YE2025 PDF — take ONLY if unused + official YE2025 euros extract. De Bolster 0861.680.989 YE2025 zetel Zwalm — leftover of mined parent only. Familiehulp De Speelboom YE2025 Brussels zetel — leftover-via-VE not enough per LOOP.md. Mini-creches GO! Next leftover city_hasselt still YE2024 — skip unless YE2025. Zo Groot Oostende leftover city_oostende still YE2024 — skip unless YE2025. Vormingscentrum leftover city_gent training — skip. VBJK leftover city_gent training — skip. Helan Kinderopvang Helan-HH-adjacent — skip. Hebe Kenniscentrum training — skip. Tick **2470** IS every-10.

"""
with log.open("ab") as f:
    f.write(entry.encode("utf-8"))
print("loop_log ok")
print("WRITE CORE DONE")
