from pathlib import Path
import csv
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2471_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_zonneschijn_jr2025_nbb_pdf_2471"
SRC_KBO="src_zonneschijn_kbo_2471"
SRC_SBM="src_zonneschijn_sbm_2471"
SRC_SITE="src_zonneschijn_site_2471"
EID="vzw_zonneschijn_dendermonde"
GAP="gap_zonneschijn_opgroeien_matrix_bruto_1245k_omzet73_empty_pnl_jump_135k_destin_empty_l5"
COMM="comm_zonneschijn_jr2025_statutory_bruto_1245k_omzet73_empty_pnl_jump_135k"
LB="lb_zonneschijn_bruto_1245k_omzet73_empty_pnl_jump_135k_destin_empty_jr2025"
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
f"{SRC_PDF},NBB MIC-VZW jaarrekening 2025 Zonneschijn deposit 2026-00406573,https://consult.cbso.nbb.be/api/external/broker/public/deposits/pdf/f47d9558-971e-11f1-9362-4d4aa53229b0,NBB official WVV deposit PDF,{DAY},budget,tick2471; official native PDF 44253 bytes 11p MIC-VZW 26.0.15 m08-f; header 17.08.2026; AV 28.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-08-19 12:57:45 UTC OpenPDF 1.3.26; all 11p native; official NBB broker GET 200 44253; CDN 2026-00406573 HEAD 403 SBM not yet mirrored (deposit filed 17.08.2026); MIC-VZW 6.1.1 6.2 6.3 7 8 niet dienstig; prior-year identical not restated; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Zonneschijn 0877.850.493,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0877850493,KBO Public Search FOD Economie,{DAY},official_register,tick2471; Actief; 3 VE 2.200.716.006 zonneschijn vzw Sas (DEN) 36b since 26.07.2011 + 2.325.867.582 Zonneschijn 2.0 Begijnhoflaan (DEN) 2 since 10.01.2022 + 2.374.150.125 Kinderdagverblijf Appelrosje Heidestraat (APP) 69A-B since 04.06.2025; VZW since 07.12.2005; begindatum 12.12.2005; zetel Sas (DEN) 36B 9200 Dendermonde since 01.01.2013; FOI info@kdvzonneschijn.be; leftover mined city_dendermonde CIK; NOT Infano 0477.578.411 remine; NOT Vijverbeek 0448.164.744 remine; NOT t Zonnetje 0443.648.306 remine",
f"{SRC_SBM},NBB Consult / SBM fiche Zonneschijn 0877850493 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0877850493,NBB Consult / SBM,{DAY},official_register,tick2471; deposit-id 2026-00406573 YE 01.01.2025-31.12.2025 filing 17.08.2026 published 17.08.2026 MIC-VZW Microschema Initial; used for deposit-id discovery only; euros NOT taken from SBM HTML table; Companyweb last-balansjaar 2025 deposit-id discovery OK euros NOT OK",
f"{SRC_SITE},Zonneschijn FOI contact leftover city_dendermonde CIK,https://www.kdvzonneschijn.be/,VZW Zonneschijn leftover city_dendermonde CIK Opgroeien groepsopvang 3 VE,{DAY},foi_contact,tick2471; FOI info@kdvzonneschijn.be; zetel Sas (DEN) 36B 9200 Dendermonde; 3 VE leftover mined city_dendermonde after Infano different-city skip; NOT Infano remine; NOT Vijverbeek remine; NOT t Zonnetje remine; NOT Kindercentrum remine; NOT Duinhuisjes remine; NOT Mater Dei remine; NOT Savio remine; NOT Paideia remine; NOT Ooievaarsnest remine; NOT DE ZONNEKINDJES remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Kinderlach YE2024; NOT Helan; NOT De Speelboom Brussels; NOT Villa Boempatat SCAN/CDN403; NOT Elief CDN 403; NOT Hebe training; NOT Zo Groot YE2024; NOT De Bolster Zwalm not leftover mined parent; NOT GERUST zorgcentrale; NOT Vormingscentrum training; NOT Zwarte Zusters dissolved; NOT Hupskadee YE2024; NOT KIOS Schoten no deposits; NOT Pardoes Mechelen YE2024",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},Zonneschijn,ASBL Zonneschijn,Zonneschijn VZW (leftover city_dendermonde CIK),parastatal,city_dendermonde,nl,https://www.kdvzonneschijn.be/,info@kdvzonneschijn.be,Sas (DEN) 36B 9200 Dendermonde,tick2471 YE2025 Strong official native NBB PDF deposit 2026-00406573 + Strong KBO 0877.850.493 Actief 3 VE 2.200.716.006 + 2.325.867.582 + 2.374.150.125; omzet70 empty MIC; 73 empty MIC; 76A empty; envelope bruto 9900 JUMP 1245059; bruto JUMP 1245059; pnl JUMP 134975; 9901 JUMP 134802; equity JUMP 404510; assets JUMP 592650; debt JUMP 188140; FTE JUMP 18.9; kapitaalsubsidies empty; destin691 empty; 791 empty; cash JUMP 259913; geldbeleggingen empty; leftover city_dendermonde CIK 3 VE; NOT Infano Ternat 0477.578.411 remine; NOT Vijverbeek Asse 0448.164.744 remine; NOT t Zonnetje Waregem 0443.648.306 remine; NOT Kindercentrum Waregem 0408.226.775 remine; NOT Duinhuisjes 0413.323.037 remine; NOT 3Wplus Kinderopvang Asse 0893.870.539 remine; NOT Mater Dei 0431.168.859 remine; NOT WZC Mater Dei Heikruis remine; NOT Savio Dilbeek 0472.564.501 remine; NOT Dominiek Savio remine; NOT EVA Dilbeek 0477.276.325 remine; NOT Paideia 0445.129.931 remine; NOT Ooievaarsnest 0418.588.256 remine; NOT DE ZONNEKINDJES 0416.541.952 remine; NOT D'n Opvang 0676.442.465 remine; NOT CAR Overleie 0454.250.505 remine; NOT Gesticht 0410.918.031 remine; NOT HOCUS-POCUS 0466.893.167 remine; NOT VKA 0433.480.132 remine; NOT Soetkin 0443.641.970 remine; NOT t Sloeberke 0410.973.360 remine; NOT CAR Accent 0413.208.122 remine; NOT De Elfjes 0455.636.912 remine; NOT De Steijgertjes 0413.421.720 remine; NOT H.Hart WZC 0413.595.330; NOT Zo Groot 0818.420.771 leftover city_oostende YE2024; NOT De Groene Verte 0465.061.649 remine; NOT De Vleugels 0431.408.290 remine; NOT De Pallieterkes 0418.538.865 remine; NOT De Medemens KDV 0893.678.915 remine; NOT De Medemens parent 0428.692.191 remine; NOT OKO & ZO 0862.154.608 remine; NOT Harlekijntjes 0407.700.403 remine; NOT Hartjes Ninove 0446.391.327 remine; NOT Hartjes Tienen 0441.374.348 remine; NOT De Wissel 0421.913.376 remine; NOT Familia 0461.401.779; NOT Peutertuinen GO Mariakerke 0410.221.116; NOT Mini-creches GO Next 0896.468.060 leftover city_hasselt YE2024; NOT Kinderlach 0450.275.186; NOT Helan; NOT De Speelboom Brussels; NOT Villa Boempatat 0660.616.520 leftover city_gent YE2025 SCAN/CDN403 2026-00396513; NOT Elief 0451.624.377 CDN 403; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; NOT De Bolster 0861.680.989 YE2025 zetel Zwalm city_zwalm not mined; NOT GERUST 0776.808.068 zorgcentrale; NOT Jessa hospital special schema; NOT Vormingscentrum 0413.342.338 training; NOT Zwarte Zusters 0413.272.260 dissolved; NOT Ferm Kinderopvang 0416.117.627 remine; NOT ZONNESTRAAL; Hupskadee 0863.886.651 leftover city_begijnendijk YE2024 2026-00053030 not taken; KIOS 0882.468.881 leftover city_schoten no deposits not taken; Pardoes 0417.400.205 leftover city_mechelen YE2024 not taken; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria SCAN; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Zo Groot Oostende YE2024 not taken; H.Hart Kortrijk YE2024 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_zonneschijn_omzet_jr2025_statutory,{EID},2025,0,0,0,NBB MIC-VZW code 70 omzet YE2025 empty (MIC; envelope is bruto 9900),{SRC_PDF},strong,tick2471; PDF p5 native; YE2024 empty; 73 empty; 76A empty",
f"bud_zonneschijn_73_jr2025_statutory,{EID},2025,0,0,0,NBB MIC-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 empty (MIC),{SRC_PDF},strong,tick2471; PDF p5 native; YE2024 empty; FOI Opgroeien matrix behind envelope 1245059",
f"bud_zonneschijn_opbr_jr2025_statutory,{EID},2025,1245059,1245059,1245059,NBB MIC-VZW envelope bruto 9900 YE2025 JUMP +40.07% (omzet empty so envelope is bruto 9900),{SRC_PDF},strong,tick2471; PDF p5 native; YE2024 888899; 70 empty; 73 empty; 76A empty",
f"bud_zonneschijn_bruto_jr2025_statutory,{EID},2025,1245059,1245059,1245059,NBB MIC-VZW code 9900 brutomarge YE2025 JUMP +40.07% (MIC envelope because omzet empty),{SRC_PDF},strong,tick2471; PDF p5 native; YE2024 888899; 76A empty; 73 empty",
f"bud_zonneschijn_pnl_jr2025_statutory,{EID},2025,134975,134975,134975,NBB MIC-VZW code 9904 winst van het boekjaar YE2025 JUMP +842.86% (was 14315),{SRC_PDF},strong,tick2471; PDF p5 native; YE2024 14315; bedrijfswinst 9901 134802 JUMP; destin691 empty",
f"bud_zonneschijn_bedrijfswinst_jr2025_statutory,{EID},2025,134802,134802,134802,NBB MIC-VZW code 9901 bedrijfswinst YE2025 JUMP +850.65% (was 14180),{SRC_PDF},strong,tick2471; PDF p5 native; YE2024 14180; 62 1083489 JUMP; 630 14092 DROP; 66A 7566; 640/8 5110 JUMP; 635/9 empty; 631/4 empty",
f"bud_zonneschijn_equity_jr2025_statutory,{EID},2025,404510,404510,404510,NBB MIC-VZW code 10/15 eigen vermogen YE2025 JUMP +50.08%,{SRC_PDF},strong,tick2471; PDF p4 native; YE2024 269535; kapitaalsubsidies empty; overgedragen 14 303703 JUMP; fondsen 10 100807 FLAT; bestemde fondsen 13 empty",
f"bud_zonneschijn_assets_jr2025_statutory,{EID},2025,592650,592650,592650,NBB MIC-VZW code 20/58 totaal activa YE2025 JUMP +42.02%,{SRC_PDF},strong,tick2471; PDF p3 native; YE2024 417300; MVA 22/27 84573 JUMP; cash 259913 JUMP; geldbeleggingen empty; aanbouw 27 empty; FVA 28 3923; LT recv 29 244221 JUMP",
f"bud_zonneschijn_debt_jr2025_statutory,{EID},2025,188140,188140,188140,NBB MIC-VZW code 17/49 schulden YE2025 JUMP +27.32%,{SRC_PDF},strong,tick2471; PDF p4 native; YE2024 147765; 17 empty; 42/48 179743 JUMP",
f"bud_zonneschijn_cash_jr2025_statutory,{EID},2025,259913,259913,259913,NBB MIC-VZW code 54/58 liquide middelen YE2025 JUMP +15.60%,{SRC_PDF},strong,tick2471; PDF p3 native; YE2024 224847; geldbeleggingen 50/53 empty",
f"bud_zonneschijn_destin_jr2025_statutory,{EID},2025,0,0,0,NBB MIC-VZW code 691 toevoeging bestemde fondsen YE2025 empty (destin empty; 14 JUMP 303703 = prior 168728 + pnl 134975),{SRC_PDF},strong,tick2471; PDF p6 native; YE2024 destin empty; bestemde fondsen 13 empty FOI",
])
print("entities+budgets ok")

cash_json=(
"\"{\"\"2025_omzet\"\":0,\"\"2025_73\"\":0,\"\"2025_76A\"\":0,"
"\"\"2025_opbr70_76A\"\":1245059,\"\"2025_bruto\"\":1245059,"
"\"\"2025_pnl\"\":134975,\"\"2025_bedrijfswinst\"\":134802,"
"\"\"2025_equity\"\":404510,\"\"2025_assets\"\":592650,\"\"2025_debt\"\":188140,"
"\"\"2025_fte\"\":18.9,\"\"2025_kapitaalsubsidies\"\":0,\"\"2025_destin691\"\":0,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":259913,\"\"2025_geldbeleggingen\"\":0,"
"\"\"2025_personnel62\"\":1083489,\"\"2025_gebouwen22\"\":0,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":7566,"
"\"\"2025_fondsen10\"\":100807,\"\"2025_overgedragen14\"\":303703,"
"\"\"2025_bestemdefondsen13\"\":0,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":14092,\"\"2025_capex\"\":17040,"
"\"\"2024_omzet\"\":0,\"\"2024_73\"\":0,"
"\"\"2024_opbr70_76A\"\":888899,\"\"2024_bruto\"\":888899,\"\"2024_pnl\"\":14315,\"\"2024_bedrijfswinst\"\":14180,"
"\"\"2024_equity\"\":269535,\"\"2024_assets\"\":417300,"
"\"\"2024_debt\"\":147765,\"\"2024_cash\"\":224847,\"\"2024_fte\"\":15.8,"
"\"\"2024_destin691\"\":0,\"\"2024_kapitaalsubsidies\"\":0,\"\"2024_76A\"\":0,"
"\"\"2024_geldbeleggingen\"\":0}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Zonneschijn YE2025 (bruto JUMP 1.25m / omzet+73 empty MIC / pnl JUMP 135k / destin empty / Strong PDF),{EID},Opgroeien + leftover city_dendermonde CIK,VZW Zonneschijn (KBO 0877.850.493; Actief; 3 VE; zetel Dendermonde),2026-06-28,2025,2025,1245059,{cash_json},0,active,https://consult.cbso.nbb.be/api/external/broker/public/deposits/pdf/f47d9558-971e-11f1-9362-4d4aa53229b0,Public CIK dual of mined city_dendermonde,Publish Opgroeien matrix behind envelope 1.25m + why omzet+73 empty MIC and why pnl JUMP 134975 while destin empty and cash JUMP 259913,{SRC_PDF},strong,Vlaanderen>Oost-Vlaanderen>Dendermonde>Zonneschijn>JR2025_statutory_L5,tick2471; Strong official native PDF; leftover mined city_dendermonde CIK; 3 VE; prior-year identical; NOT every-10; NOT Infano remine; NOT Vijverbeek remine; NOT t Zonnetje remine; NOT Kindercentrum remine; NOT Duinhuisjes remine; NOT Mater Dei remine; NOT Savio remine; NOT Kinderlach YE2024; NOT Zo Groot YE2024; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"Zonneschijn bruto JUMP 1.25m / omzet+73 empty MIC / pnl JUMP 135k / destin empty (YE2025 leftover city_dendermonde CIK)",
"L5",
"cik_vzw_statutory",
"Vlaanderen>Oost-Vlaanderen>Dendermonde>Zonneschijn>JR2025",
"1245059",
"1245059",
"PDF envelope 1245059 = bruto 9900 MIC because omzet empty; 70 empty; 73 empty; 76A empty; bruto 1245059; bedrijfswinst JUMP 134802; pnl JUMP 134975; equity JUMP 404510; assets JUMP 592650; debt JUMP 188140; FTE 18.9; kapitaalsubsidies empty; destin691 empty; cash JUMP 259913; leftover city_dendermonde CIK",
"strong",
SRC_PDF,
"Opgroeien + leftover city_dendermonde CIK",
"CIK / Kind en Gezin groepsopvang leftover city_dendermonde",
"1.25m envelope; omzet+73 empty MIC; pnl JUMP 134975; destin empty; leftover city_dendermonde CIK",
"5.30",
"5.05",
"5.08",
"5.20",
"FOI Opgroeien matrix behind envelope 1.25m + why omzet+73 empty MIC and why pnl JUMP 134975 while destin empty and cash JUMP 259913",
"active",
"",
"tick2471 leftover mined city_dendermonde CIK after Infano different-city skip; 3 VE; prior-year identical; NOT every-10; NOT Infano remine; NOT Vijverbeek remine; NOT t Zonnetje remine; NOT Kindercentrum remine; NOT Duinhuisjes remine; NOT Mater Dei remine; NOT Savio remine; NOT Kinderlach YE2024; NOT Zo Groot YE2024; NOT Elief CDN 403; NOT Villa Boempatat SCAN/CDN403; NOT De Speelboom Brussels; NOT Hupskadee YE2024; NOT KIOS Schoten no deposits; NOT Pardoes Mechelen YE2024",
])
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Dendermonde>Zonneschijn>CIK",
"entity_id": EID,
"what_is_missing": "Opgroeien split behind envelope 1245059 (omzet 70 empty + 73 empty + 76A empty; MIC bruto 9900) and why destin empty while pnl JUMP 134975 and cash JUMP 259913 and new VE Appelrosje since 04.06.2025",
"why_it_matters": "Strong official PDF leftover public CIK of mined city_dendermonde; MIC envelope bruto 1.25m because omzet empty; public Opgroeien groepsopvang 3 VE Sas 36B Dendermonde",
"priority": "8",
"recipient_body": "VZW Zonneschijn / Raad van Bestuur",
"recipient_email": "info@kdvzonneschijn.be",
"recipient_postal": "Sas (DEN) 36B 9200 Dendermonde",
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
"notes": "tick2471; ready NOT sent; Strong official native NBB PDF; leftover mined city_dendermonde CIK after Infano different-city skip; 3 VE; prior-year identical; NOT every-10; off Infano remine; off Vijverbeek remine; off t Zonnetje remine",
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
if rq_raw.count(b"rq_2471,")!=1: raise SystemExit(f"bad 2471 count {rq_raw.count(b'rq_2471,')}")
if b"rq_2472," in rq_raw: raise SystemExit("2472 exists")
idx=rq_raw.rfind(b"rq_2471,")
if idx<0: raise SystemExit("rq_2471 not found")
new_2471=(
"rq_2471,leftover dual Zonneschijn YE2025,hole_fill,8,done,L5,vzw_zonneschijn_dendermonde,"
"Took unused leftover public CIK Zonneschijn 0877.850.493 leftover mined city_dendermonde. Official NBB MIC-VZW YE2025 2026-00406573 native 11p. Envelope bruto 9900 JUMP 1245059 (omzet+73 empty MIC); pnl JUMP 134975; destin empty; FTE 18.9. NOT Infano remine. NOT Vijverbeek remine. NOT t Zonnetje remine. NOT Hupskadee YE2024.,"
f",{STAMP},{STAMP},tick2471 leftover mined city_dendermonde CIK; Strong native PDF; 3 VE; prior-year identical; next every-10 is 2480\n"
)
new_2472=(
"rq_2472,leftover dual after Zonneschijn — hunt unused public dual,hole_fill,8,open,L5,,"
"After Zonneschijn YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf. Hupskadee 0863.886.651 leftover city_begijnendijk YE2024 2026-00053030 — take ONLY if unused + official YE2025 native PDF (later 2026 deposit). Villa Boempatat 0660.616.520 leftover city_gent YE2025 2026-00396513 CDN 403 / SCAN — take ONLY if unused + official native-text YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen YE2025 2026-00374905 CDN 403 — take ONLY if CDN 200 native. Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO! Next / Zo Groot Oostende still YE2024 — take ONLY if unused + official YE2025 PDF. De Bolster 0861.680.989 YE2025 2026-00210039 zetel Zwalm (city_zwalm not mined) — take ONLY if leftover of a mined parent. Jessa leftover city_hasselt hospital YE2025 PDF — take ONLY if unused + official YE2025 euros extract. KIOS 0882.468.881 leftover city_schoten — no jaarrekening skip unless deposits appear. Pardoes 0417.400.205 leftover city_mechelen — YE2024 skip unless YE2025. NOT Zonneschijn remine. NOT Infano remine. NOT Vijverbeek remine. NOT Mater Dei remine. NOT Savio remine. NOT 3Wplus remine. NOT Paideia remine. NOT Ooievaarsnest remine. NOT De Zonnekindjes remine. NOT D'n Opvang remine. NOT CAR Overleie remine. NOT Gesticht remine. NOT Grauwzusters convent. NOT Hocus-Pocus remine. NOT VKA remine. NOT Soetkin remine. NOT t Sloeberke remine. NOT CAR Accent remine. NOT De Groene Verte remine. NOT De Vleugels remine. NOT De Pallieterkes remine. NOT De Medemens remine. NOT OKO & ZO remine. NOT Harlekijntjes remine. NOT Hartjes remine. NOT De Wissel remine. NOT Familia remine. NOT t Zonnetje remine. NOT Kindercentrum remine. NOT Duinhuisjes remine. NOT Helan. NOT Hebe training. NOT WZC OLVA remine. NOT De Speelboom Brussels. NOT GERUST zorgcentrale. NOT Zo Groot remine. NOT De Elfjes remine. NOT De Steijgertjes remine. NOT Vormingscentrum training. NOT Zwarte Zusters dissolved. NOT Dominiek Savio remine. NOT EVA Dilbeek remine. NOT WZC Mater Dei Heikruis remine. NOT Ferm Kinderopvang remine.,"
f",{STAMP},{STAMP},spawned after tick2471; Zonneschijn taken leftover mined city_dendermonde CIK; Infano taken leftover mined city_ternat CIK EVERY-10; Vijverbeek taken leftover mined city_asse CIK; Mater Dei taken leftover mined city_brasschaat CIK; Savio taken leftover mined city_dilbeek CIK; Paideia taken leftover mined city_brugge CIK; Ooievaarsnest taken leftover mined city_tienen CIK; Zonnekindjes taken leftover mined city_diepenbeek CIK; D'n Opvang taken leftover mined city_oostende CIK; CAR Overleie taken leftover mined city_kortrijk CAR; Gesticht taken leftover mined city_ieper CIK convent-class check PASSED; Hocus-Pocus taken leftover mined city_roeselare CIK; VKA taken leftover mined city_antwerpen CIK; Soetkin taken leftover mined city_kortrijk CIK; t Sloeberke taken leftover mined city_kortrijk CIK; De Groene Verte taken leftover mined city_houthulst WZC; t Zonnetje taken leftover mined city_waregem CIK; Kindercentrum taken leftover mined city_waregem CIK; Duinhuisjes taken leftover mined city_knokke_heist CIK; KIOS Schoten no deposits; Pardoes Mechelen YE2024; next every-10 is 2480\n"
)
if new_2471.count("\n")!=1 or new_2472.count("\n")!=1: raise SystemExit("bad rq newlines")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2471.encode("utf-8"))
    f.write(new_2472.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2471", chk.count(b"rq_2471,"), "n2472", chk.count(b"rq_2472,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2471,2471,no,tick2471 leftover dual Zonneschijn 0877.850.493 Strong native PDF (omzet70 empty MIC; 73 empty MIC; 76A empty; envelope bruto 9900 JUMP 1245059; bruto JUMP 1245059; pnl JUMP 134975; 9901 JUMP 134802; equity JUMP 404510; assets JUMP 592650; debt JUMP 188140; FTE JUMP 18.9; kapitaalsubsidies empty; destin691 empty; 791 empty; cash JUMP 259913; geldbeleggingen empty; 3 VE leftover city_dendermonde CIK); leftover mined city_dendermonde CIK; prior-year identical; NOT Infano remine; NOT Vijverbeek remine; NOT t Zonnetje remine; NOT Kindercentrum remine; NOT Duinhuisjes remine; NOT 3Wplus remine; NOT Mater Dei remine; NOT WZC Mater Dei Heikruis remine; NOT Savio remine; NOT Dominiek Savio remine; NOT EVA Dilbeek remine; NOT Paideia remine; NOT Ooievaarsnest remine; NOT DE ZONNEKINDJES remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT Grauwzusters convent; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens KDV remine; NOT De Medemens parent remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Mini-creches GO Next remine; NOT Kinderlach; NOT Zo Groot YE2024; NOT De Speelboom Brussels; NOT Elief CDN 403; NOT Villa Boempatat SCAN/CDN403; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; NOT De Bolster Zwalm not leftover mined parent; NOT GERUST zorgcentrale; NOT De Elfjes remine; NOT De Steijgertjes remine; NOT Vormingscentrum training; NOT Zwarte Zusters dissolved; NOT Ferm Kinderopvang remine; NOT Hupskadee YE2024; NOT KIOS Schoten no deposits; NOT Pardoes Mechelen YE2024; next every-10 is 2480; next rq_2472 leftover dual\n",
encoding="utf-8",
)
print("loop_state ok")

log=ROOT/"docs/doge/loop_log.md"
log_raw=log.read_bytes()
if not log_raw.endswith(b"\n"): raise SystemExit("loop_log no LF")
entry=f"""
### {STAMP} - tick 2471 - rq_2471 Zonneschijn (bruto JUMP 1.25m / omzet+73 empty MIC / pnl JUMP 135k / destin empty / Strong PDF)

- Unit: **rq_2471** leftover dual after **INFANO@2470**. Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024** (not re-downloaded); FARO 2026-00010398 still **YE2024** (HEAD-only policy Last-Modified 21.01.2026; not re-downloaded); AIESH/Gandae/Aralea/Manupal/Vlotter still **YE2024**. Zeepreventorium still **YE2024**. Drongen named+unnamed CARs **exhausted**. Kohesi family **exhausted**. Quattro WZC members **exhausted**. CAR Antenne 3000 leftover city_leuven CDN still **403**. AZ Sint-Maria leftover city_halle YE2025 SCAN — not taken. CAR Noorderkempen leftover city_wuustwezel still SCAN. De Linde Ronse leftover city_ronse still **YE2024**. Kinderlach leftover city_eeklo still **YE2024**. Villa Boempatat leftover city_gent **YE2025** **2026-00396513** CDN **403** / SCAN no extractable euros — not taken. Woon en Zorg H. Hart Kortrijk leftover city_kortrijk still **YE2024**. Jessa leftover city_hasselt hospital YE2025 PDF / hospital special schema — not taken. Mini-creches GO! Next leftover city_hasselt still **YE2024**. Zo Groot Oostende leftover city_oostende still **YE2024**. Familiehulp De Speelboom YE2025 unused Brussels zetel — not taken. Speelhuis Elief leftover city_antwerpen unused YE2025 **2026-00374905** CDN **403** — not taken. Hebe Kenniscentrum leftover city_antwerpen training — skip. WZC OLVA leftover city_antwerpen already in entities — do not remine. De Bolster 0861.680.989 YE2025 zetel Zwalm (city_zwalm not mined) — not taken. GERUST Zorgcentrale leftover city_herentals YE2025 — zorgcentrale not in dual types — not taken. Vormingscentrum 0413.342.338 leftover city_gent training — skip. Helan Kinderopvang 0464.151.037 already skipped. Zwarte Zusters 0413.272.260 dissolved — skip. Hupskadee 0863.886.651 leftover city_begijnendijk YE2024 only (2026-00053030 already on disk) — not taken. KIOS 0882.468.881 leftover city_schoten — no jaarrekening — skip. Pardoes 0417.400.205 leftover city_mechelen — last deposit YE2024 — skip. Infano 0477.578.411 just mined — do not remine. Vijverbeek 0448.164.744 already mined — do not remine. Mater Dei 0431.168.859 already mined — do not remine. Savio 0472.564.501 already mined — do not remine. t Zonnetje Waregem already mined — do not remine. Kindercentrum Waregem already mined — do not remine. Duinhuisjes already mined — do not remine. First leftover unused + live official YE2025 native euros: took FREE leftover Flemish **VZW Zonneschijn** YE2025 (KBO **0877.850.493**; zetel Sas (DEN) 36B 9200 Dendermonde; **Actief** **3 VE** **2.200.716.006** + **2.325.867.582** + **2.374.150.125** Appelrosje since 04.06.2025; RSZ2025 **88.911**; leftover of mined **city_dendermonde**; info@kdvzonneschijn.be; Opgroeien groepsopvang; Kind en Gezin-vergund). Identity trap: Zonneschijn 0877.850.493 ≠ INFANO **0477.578.411** leftover city_ternat just mined; ≠ Kinderdagverblijf Vijverbeek **0448.164.744**; ≠ t Zonnetje Waregem **0443.648.306**; ≠ DE ZONNEKINDJES **0416.541.952**; ≠ ZONNESTRAAL / Zonnestraal Junior; ≠ Kindercentrum Waregem **0408.226.775**; ≠ Duinhuisjes **0413.323.037**; ≠ Groepsopvang Mater Dei **0431.168.859**; ≠ WZC Mater Dei Heikruis; ≠ Kinderdagverblijf Savio **0472.564.501**; ≠ Dominiek Savio; ≠ EVA Dilbeek **0477.276.325**; ≠ Paideia **0445.129.931**; ≠ KDV Ooievaarsnest **0418.588.256**; ≠ D'n Opvang **0676.442.465**; ≠ CAR Overleie **0454.250.505**; ≠ Gesticht **0410.918.031**; ≠ HOCUS-POCUS **0466.893.167**; ≠ VKA **0433.480.132**; ≠ Soetkin **0443.641.970**; ≠ t Sloeberke **0410.973.360**; ≠ CAR Accent **0413.208.122**; ≠ Speelhuis Elief **0451.624.377**; ≠ Villa Boempatat **0660.616.520**; ≠ De Groene Verte **0465.061.649**; ≠ De Vleugels **0431.408.290**; ≠ De Pallieterkes **0418.538.865**; ≠ De Medemens Kinderdagverblijven **0893.678.915**; ≠ De Medemens **0428.692.191**; ≠ OKO & ZO **0862.154.608**; ≠ Harlekijntjes **0407.700.403**; ≠ Hartjes Ninove **0446.391.327**; ≠ Hartjes Tienen **0441.374.348**; ≠ De Wissel **0421.913.376**; ≠ Ferm Kinderopvang **0416.117.627**; ≠ Familia **0461.401.779**; ≠ Peutertuinen GO Mariakerke **0410.221.116**; ≠ Mini-crèches GO! Next **0896.468.060**; ≠ Kinderlach **0450.275.186**; ≠ Helan 0464.151.037; ≠ Hebe **0451.789.772**; ≠ WZC OLVA **0430.977.136**; ≠ H.Hart Kortrijk **0413.595.330**; ≠ De Linde Ronse **0778.279.401**; ≠ De Bolster **0861.680.989**; ≠ GERUST **0776.808.068**; ≠ Jessa **0821.142.117**; ≠ AZ Sint-Maria **0467.967.491**; ≠ De Elfjes **0455.636.912**; ≠ De Steijgertjes **0413.421.720**; ≠ TKDV Het Veer Kloosterstraat 6; ≠ Vormingscentrum **0413.342.338** training; ≠ Zwarte Zusters **0413.272.260** dissolved; ≠ Hupskadee **0863.886.651**; ≠ KIOS **0882.468.881**; ≠ Pardoes **0417.400.205**. 3 VE Dendermonde — leftover of mined city_dendermonde (zetel + Sas 36b + Begijnhoflaan 2 + Appelrosje Heidestraat 69A-B). Confirmed leftover public (Opgroeien CIK groepsopvang; Kind en Gezin-vergund) not convent / not private clinic / not school / not OVBJ / not WZC / not VAPH / not Ferm / not Infano remine / not Vijverbeek remine / not t Zonnetje remine. MIC-VZW **native text** (not scan) — 44253 B / 11p all native euros (MIC-VZW 6.1.1 / 6.2 / 6.3 / 7 / 8 niet dienstig).
- Found: official NBB MIC-VZW native PDF deposit **2026-00406573** (44253 B / 11p; AV **28.06.2026**; header **17.08.2026**; official NBB broker GET 200; CDN HEAD **403** SBM not yet mirrored; CreationDate 19.08.2026 OpenPDF 1.3.26; all 11p native; prior-year identical not restated) — omzet 70 **empty** MIC; 73 **empty** MIC; 76A **empty**; envelope bruto 9900 **EUR1245059** JUMP +40.07% (MIC envelope because omzet empty; was 888899); bruto 9900 **EUR1245059** JUMP +40.07%; 62 **EUR1083489** JUMP +27.02%; 630 **EUR14092** DROP −22.64%; 66A **EUR7566**; 640/8 **EUR5110** JUMP +47.22%; 635/9 **empty**; 631/4 **empty**; bedrijfswinst 9901 **EUR134802** JUMP +850.65%; pnl 9904 **EUR134975** JUMP +842.86%; equity **EUR404510** JUMP +50.08%; assets **EUR592650** JUMP +42.02%; debt **EUR188140** JUMP +27.32%; FTE **18.9** JUMP +19.62% (was 15.8; 100 18.9; 105 22.3); kapitaalsubsidies **empty**; destin 691 **empty** (791 empty; 14 JUMP 303703 = prior 168728 + pnl 134975); 791 **empty**; cash **EUR259913** JUMP +15.60%; geldbeleggingen **empty**; gebouwen **empty**; MVA 22/27 **EUR84573** JUMP; aanbouw **empty**; capex **EUR17040**; fondsen 10 **EUR100807** FLAT; overgedragen 14 **EUR303703** JUMP; bestemde fondsen 13 **empty**; voorzieningen 16 **empty**; FVA 28 **EUR3923**; LT recv 29 **EUR244221** JUMP. Strong KBO + Strong PDF (native all pages; not SBM table; not Companyweb euros). Site: 3 VE leftover mined city_dendermonde CIK. NOT Infano remine. NOT Vijverbeek remine. NOT t Zonnetje remine. NOT Kindercentrum remine. NOT Duinhuisjes remine. NOT Mater Dei remine. NOT Savio remine. NOT Hupskadee YE2024. NOT KIOS no deposits. NOT Pardoes YE2024.
- Wrote: sources (+4); budgets (+11); commitments (+1); leaderboard (+1 pi 5.20); entities (+1 vzw_zonneschijn_dendermonde); foi + draft `gap_zonneschijn_opgroeien_matrix_bruto_1245k_omzet73_empty_pnl_jump_135k_destin_empty_l5`; rq_2471=done + rq_2472 open; loop_state ticks=2471; raw tick2471/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2480**). Next: rq_2472 unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Zonneschijn remine / NOT Infano remine / NOT Vijverbeek remine / NOT t Zonnetje remine / NOT Kindercentrum remine / NOT Duinhuisjes remine / NOT Mater Dei remine / NOT Savio remine / NOT 3Wplus remine / NOT Paideia remine / NOT Ooievaarsnest remine / NOT De Zonnekindjes remine / NOT D'n Opvang remine / NOT CAR Overleie remine / NOT Gesticht remine / NOT Grauwzusters convent / NOT HOCUS-POCUS remine / NOT VKA remine / NOT Soetkin remine / NOT t Sloeberke remine / NOT CAR Accent remine / NOT De Groene Verte remine / NOT De Vleugels remine / NOT De Pallieterkes remine / NOT De Medemens remine / NOT OKO & ZO remine / NOT Harlekijntjes remine / NOT Hartjes remine / NOT De Wissel remine / NOT Familia remine / NOT Mini-creches GO Next remine / NOT WZC OLVA remine / NOT Hebe training / NOT Quattro remine / NOT GERUST zorgcentrale / NOT Zo Groot remine / NOT De Elfjes remine / NOT De Steijgertjes remine / NOT Vormingscentrum training / NOT Zwarte Zusters dissolved / NOT Dominiek Savio remine / NOT EVA Dilbeek remine / NOT WZC Mater Dei Heikruis remine / NOT Ferm Kinderopvang remine). NOW leftover candidate: Hupskadee 0863.886.651 leftover city_begijnendijk YE2024 2026-00053030 — take ONLY if unused + official YE2025 native PDF. Villa Boempatat 0660.616.520 leftover city_gent YE2025 **2026-00396513** CDN **403** / SCAN — take ONLY if unused + official native-text YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen unused YE2025 **2026-00374905** CDN **403** — take ONLY if unused + CDN 200 native YE2025 PDF. Kinderlach leftover city_eeklo still YE2024 — take ONLY if unused + official YE2025 PDF. De Linde Ronse leftover city_ronse still YE2024 — take ONLY if unused + official YE2025 PDF. H.Hart Kortrijk leftover city_kortrijk still YE2024 — take ONLY if unused + official YE2025 PDF. Jessa leftover city_hasselt hospital YE2025 PDF — take ONLY if unused + official YE2025 euros extract. De Bolster 0861.680.989 YE2025 zetel Zwalm — leftover of mined parent only. Familiehulp De Speelboom YE2025 Brussels zetel — leftover-via-VE not enough per LOOP.md. Mini-creches GO! Next leftover city_hasselt still YE2024 — skip unless YE2025. Zo Groot Oostende leftover city_oostende still YE2024 — skip unless YE2025. KIOS leftover city_schoten no deposits — skip. Pardoes leftover city_mechelen YE2024 — skip unless YE2025. Tick **2480** is next every-10.

"""
with log.open("ab") as f:
    f.write(entry.encode("utf-8"))
print("loop_log ok")
print("WRITE CORE DONE")
