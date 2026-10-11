from pathlib import Path
import csv
from io import StringIO
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2475_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_augustientjes_jr2025_nbb_pdf_2475"
SRC_KBO="src_augustientjes_kbo_2475"
SRC_SBM="src_augustientjes_sbm_2475"
SRC_SITE="src_augustientjes_site_2475"
EID="vzw_augustientjes_geel"
GAP="gap_augustientjes_opgroeien_matrix_bruto_1_53m_omzet73_empty_pnl_drop_202k_destin_202k_cash_jump_l5"
COMM="comm_augustientjes_jr2025_statutory_bruto_153m_omzet73_empty_pnl_drop_202k_destin_202k"
LB="lb_augustientjes_bruto_153m_omzet73_empty_pnl_drop_202k_destin_202k_cash_jump_jr2025"
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
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Kinderdagverblijf De Augustientjes deposit 2026-00320618,https://consult.cbso.nbb.be/api/external/broker/public/deposits/pdf/53298dd0-866f-11f1-9f93-0786a55f9609,NBB official WVV deposit PDF via official broker,{DAY},budget,tick2475; official native PDF 49373 bytes 14p VKT-VZW 25.0.13 m04-f; header 23.07.2026; AV 02.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-23 10:30:07 UTC OpenPDF 1.3.26; CDN Last-Modified 03.08.2026; all 14p native; official NBB broker UUID 53298dd0-866f-11f1-9f93-0786a55f9609 GET 200 49373 official NBB-generated PDF; CDN 2026-00320618 GET 200 same 49373 MD5; importFileType XBRL; VKT-VZW 6.1.1 6.3 6.5 6.6 7 8 niet dienstig; 6.1.2 6.1.3 6.2 6.4 6.7 6.8 present; prior-year identical not restated; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Kinderdagverblijf De Augustientjes 0445.602.360,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0445602360,KBO Public Search FOD Economie,{DAY},official_register,tick2475; Actief; 1 VE 2.150.820.689 Kinderdagverblijf De Augustientjes Kollegestraat 120 2440 Geel since 03.01.2006; VZW since 24.09.1991; begindatum 24.09.1991; zetel Kollegestraat 120 2440 Geel since 24.09.1991; toelating Kinderopvang VL since 01.04.2014; RSZ-werkgever since 01.01.1992; RSZ2025 88.911; FOI info@deaugustientjes.be; leftover mined city_geel CIK; NOT Hupskadee 0863.886.651 remine; NOT Hupskadee BV 0476.248.224 private; NOT Pardoes 0417.400.205 remine; NOT Bambi 0443.006.522 remine; NOT Zonneschijn 0877.850.493 remine; NOT Zusterhof 0473.762.450 remine",
f"{SRC_SBM},NBB Consult / SBM fiche De Augustientjes 0445602360 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0445602360,NBB Consult / SBM,{DAY},official_register,tick2475; deposit-id 2026-00320618 YE 01.01.2025-31.12.2025 filing 23.07.2026 published VKT-VZW Verkort model vereniging Initial; Companyweb last-balansjaar 2025 deposit-id discovery OK euros NOT OK; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},De Augustientjes FOI contact leftover city_geel CIK,https://deaugustientjes.be/,VZW Kinderdagverblijf De Augustientjes leftover city_geel CIK Opgroeien groepsopvang 1 VE,{DAY},foi_contact,tick2475; FOI info@deaugustientjes.be; zetel Kollegestraat 120 2440 Geel; 1 VE leftover mined city_geel after Hupskadee different-city skip; Opgroeien groepsopvang; Kind en Gezin-vergund; 86 plaatsen; 7 semi-verticale leefgroepen; inclusieve opvang; NOT Hupskadee remine; NOT Hupskadee BV private; NOT Pardoes remine; NOT Bambi remine; NOT Zonneschijn remine; NOT Infano remine; NOT Vijverbeek remine; NOT t Zonnetje remine; NOT Kindercentrum remine; NOT Duinhuisjes remine; NOT Mater Dei remine; NOT Savio remine; NOT Paideia remine; NOT Ooievaarsnest remine; NOT DE ZONNEKINDJES remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Kinderlach YE2024; NOT Helan; NOT De Speelboom Brussels leftover-via-VE; NOT Villa Boempatat SCAN/CDN403; NOT Elief CDN 403; NOT Hebe training; NOT Zo Groot YE2024; NOT De Bolster Zwalm not leftover mined parent; NOT GERUST zorgcentrale; NOT Vormingscentrum training; NOT Zwarte Zusters dissolved; NOT KIOS Schoten no deposits; NOT Molleke city_mol YE2024; NOT t Sas city_denderleeuw YE2024 2026-00050081; NOT Dol-Fijn Turnhout leftover-via-VE; NOT Pardoes NV bookshop; NOT Zusterhof remine; NOT Olliebollie BV private; NOT In de wolken BV private; NOT Troetelland Geel private BV; NOT De Zandkapoentjes BV private",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},Kinderdagverblijf De Augustientjes,ASBL Kinderdagverblijf De Augustientjes,Kinderdagverblijf De Augustientjes VZW (leftover city_geel CIK),parastatal,city_geel,nl,https://deaugustientjes.be/,info@deaugustientjes.be,Kollegestraat 120 2440 Geel,tick2475 YE2025 Strong official native NBB PDF deposit 2026-00320618 + Strong KBO 0445.602.360 Actief 1 VE 2.150.820.689; omzet70 empty VKT; 73 empty VKT; 76A empty; envelope bruto 9900 JUMP 1527461; bruto JUMP 1527461; pnl DROP 201944; 9901 DROP 150802; equity JUMP 2105573; assets JUMP 2540138; debt JUMP 157105; FTE DROP 21.1; kapitaalsubsidies DROP 44650; destin691 201944; 791 empty; cash JUMP 1698135; geldbeleggingen empty; leftover city_geel CIK 1 VE; NOT Hupskadee 0863.886.651 remine; NOT Hupskadee BV 0476.248.224 private BV; NOT Pardoes Mechelen 0417.400.205 remine; NOT Bambi Kalmthout 0443.006.522 remine; NOT Zonneschijn Dendermonde 0877.850.493 remine; NOT Infano Ternat 0477.578.411 remine; NOT Vijverbeek Asse 0448.164.744 remine; NOT t Zonnetje Waregem 0443.648.306 remine; NOT Kindercentrum Waregem 0408.226.775 remine; NOT Duinhuisjes 0413.323.037 remine; NOT 3Wplus Kinderopvang Asse 0893.870.539 remine; NOT Mater Dei 0431.168.859 remine; NOT WZC Mater Dei Heikruis remine; NOT Savio Dilbeek 0472.564.501 remine; NOT Dominiek Savio remine; NOT EVA Dilbeek 0477.276.325 remine; NOT Paideia 0445.129.931 remine; NOT Ooievaarsnest 0418.588.256 remine; NOT DE ZONNEKINDJES 0416.541.952 remine; NOT D'n Opvang 0676.442.465 remine; NOT CAR Overleie 0454.250.505 remine; NOT Gesticht 0410.918.031 remine; NOT HOCUS-POCUS 0466.893.167 remine; NOT VKA 0433.480.132 remine; NOT Soetkin 0443.641.970 remine; NOT t Sloeberke 0410.973.360 remine; NOT CAR Accent 0413.208.122 remine; NOT De Elfjes 0455.636.912 remine; NOT De Steijgertjes 0413.421.720 remine; NOT H.Hart WZC 0413.595.330; NOT Zo Groot 0818.420.771 leftover city_oostende YE2024; NOT De Groene Verte 0465.061.649 remine; NOT De Vleugels 0431.408.290 remine; NOT De Pallieterkes 0418.538.865 remine; NOT De Medemens KDV 0893.678.915 remine; NOT De Medemens parent 0428.692.191 remine; NOT OKO & ZO 0862.154.608 remine; NOT Harlekijntjes 0407.700.403 remine; NOT Hartjes Ninove 0446.391.327 remine; NOT Hartjes Tienen 0441.374.348 remine; NOT De Wissel 0421.913.376 remine; NOT Familia 0461.401.779; NOT Peutertuinen GO Mariakerke 0410.221.116; NOT Mini-creches GO Next 0896.468.060 leftover city_hasselt YE2024; NOT Kinderlach 0450.275.186; NOT Helan; NOT De Speelboom Brussels leftover-via-VE; NOT Villa Boempatat 0660.616.520 leftover city_gent YE2025 SCAN/CDN403 2026-00396513; NOT Elief 0451.624.377 CDN 403; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; NOT De Bolster 0861.680.989 YE2025 zetel Zwalm city_zwalm not mined; NOT GERUST 0776.808.068 zorgcentrale; NOT Jessa hospital special schema; NOT Vormingscentrum 0413.342.338 training; NOT Zwarte Zusters 0413.272.260 dissolved; NOT Ferm Kinderopvang 0416.117.627 remine; NOT ZONNESTRAAL; NOT Molleke 0448.186.520 leftover city_mol YE2024; NOT t Sas 0448.731.106 leftover city_denderleeuw YE2024 2026-00050081; NOT Dol-Fijn 0439.731.880 Turnhout zetel leftover-via-VE; NOT Pardoes NV 0867.020.840 bookshop; NOT Witte Meren remine; NOT Zusterhof 0473.762.450 remine; NOT Olliebollie BV 0805.501.361 private; NOT In de wolken BV 1006.181.196 private; NOT Troetelland Geel private BV; NOT De Zandkapoentjes BV 0507.854.980 private; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria SCAN; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Zo Groot Oostende YE2024 not taken; H.Hart Kortrijk YE2024 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_augustientjes_omzet_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 70 omzet YE2025 empty (VKT; envelope is bruto 9900),{SRC_PDF},strong,tick2475; PDF p6 native; YE2024 empty; 73 empty; 76A empty",
f"bud_augustientjes_73_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 empty (VKT),{SRC_PDF},strong,tick2475; PDF p6 native; YE2024 empty; FOI Opgroeien matrix behind envelope 1527461",
f"bud_augustientjes_opbr_jr2025_statutory,{EID},2025,1527461,1527461,1527461,NBB VKT-VZW envelope bruto 9900 YE2025 JUMP +3.68% (omzet empty so envelope is bruto 9900),{SRC_PDF},strong,tick2475; PDF p6 native; YE2024 1473282; 70 empty; 73 empty; 76A empty",
f"bud_augustientjes_bruto_jr2025_statutory,{EID},2025,1527461,1527461,1527461,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +3.68% (VKT envelope because omzet empty),{SRC_PDF},strong,tick2475; PDF p6 native; YE2024 1473282; 76A empty; 73 empty",
f"bud_augustientjes_pnl_jr2025_statutory,{EID},2025,201944,201944,201944,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 DROP -30.84% (was 292012),{SRC_PDF},strong,tick2475; PDF p6 native; YE2024 292012; bedrijfswinst 9901 150802 DROP; destin691 201944",
f"bud_augustientjes_bedrijfswinst_jr2025_statutory,{EID},2025,150802,150802,150802,NBB VKT-VZW code 9901 bedrijfswinst YE2025 DROP -35.69% (was 234505),{SRC_PDF},strong,tick2475; PDF p6 native; YE2024 234505; 62 1291269 JUMP; 630 85111 DROP; 66A 60; 640/8 219 DROP; 635/9 empty; 631/4 empty",
f"bud_augustientjes_equity_jr2025_statutory,{EID},2025,2105573,2105573,2105573,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +8.98%,{SRC_PDF},strong,tick2475; PDF p5 native; YE2024 1932022; kapitaalsubsidies DROP 44650; overgedragen 14 empty; fondsen 10 FLAT 227968; bestemde fondsen 13 JUMP 1832955",
f"bud_augustientjes_assets_jr2025_statutory,{EID},2025,2540138,2540138,2540138,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +7.65%,{SRC_PDF},strong,tick2475; PDF p4 native; YE2024 2359694; MVA 22/27 707082 DROP; cash 1698135 JUMP; geldbeleggingen empty; aanbouw 27 empty; FVA 28 1000 FLAT; LT recv 29 empty",
f"bud_augustientjes_debt_jr2025_statutory,{EID},2025,157105,157105,157105,NBB VKT-VZW code 17/49 schulden YE2025 JUMP +4.59%,{SRC_PDF},strong,tick2475; PDF p5 native; YE2024 150212; 17 empty; 42/48 157105 JUMP; 43 empty",
f"bud_augustientjes_cash_jr2025_statutory,{EID},2025,1698135,1698135,1698135,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +19.19%,{SRC_PDF},strong,tick2475; PDF p4 native; YE2024 1424775; geldbeleggingen 50/53 empty; capex 15133 gebouwen DROP 693727",
f"bud_augustientjes_destin_jr2025_statutory,{EID},2025,201944,201944,201944,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 DROP -30.84% (791 empty; 13 JUMP 1832955 = prior 1631011 + destin 201944),{SRC_PDF},strong,tick2475; PDF p7 native; YE2024 destin 292012; bestemde fondsen 13 JUMP 1832955 FOI",
])
print("entities+budgets ok")

cash_json=(
"\"{\"\"2025_omzet\"\":0,\"\"2025_73\"\":0,\"\"2025_76A\"\":0,"
"\"\"2025_opbr70_76A\"\":1527461,\"\"2025_bruto\"\":1527461,"
"\"\"2025_pnl\"\":201944,\"\"2025_bedrijfswinst\"\":150802,"
"\"\"2025_equity\"\":2105573,\"\"2025_assets\"\":2540138,\"\"2025_debt\"\":157105,"
"\"\"2025_fte\"\":21.1,\"\"2025_kapitaalsubsidies\"\":44650,\"\"2025_destin691\"\":201944,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":1698135,\"\"2025_geldbeleggingen\"\":0,"
"\"\"2025_personnel62\"\":1291269,\"\"2025_gebouwen22\"\":693727,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":60,"
"\"\"2025_fondsen10\"\":227968,\"\"2025_overgedragen14\"\":0,"
"\"\"2025_bestemdefondsen13\"\":1832955,"
"\"\"2025_voorzieningen16\"\":277460,\"\"2025_630\"\":85111,\"\"2025_capex\"\":15133,"
"\"\"2025_ltrecv29\"\":0,\"\"2025_75\"\":61359,"
"\"\"2024_omzet\"\":0,\"\"2024_73\"\":0,"
"\"\"2024_opbr70_76A\"\":1473282,\"\"2024_bruto\"\":1473282,\"\"2024_pnl\"\":292012,\"\"2024_bedrijfswinst\"\":234505,"
"\"\"2024_equity\"\":1932022,\"\"2024_assets\"\":2359694,"
"\"\"2024_debt\"\":150212,\"\"2024_cash\"\":1424775,\"\"2024_fte\"\":22.1,"
"\"\"2024_destin691\"\":292012,\"\"2024_kapitaalsubsidies\"\":73043,\"\"2024_76A\"\":0,"
"\"\"2024_geldbeleggingen\"\":0}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},De Augustientjes YE2025 (bruto JUMP 1.53m / omzet+73 empty VKT / pnl DROP 202k / destin 202k / cash JUMP 1.70m / Strong PDF),{EID},Opgroeien + leftover city_geel CIK,VZW Kinderdagverblijf De Augustientjes (KBO 0445.602.360; Actief; 1 VE; zetel Geel),2026-06-02,2025,2025,1527461,{cash_json},0,active,https://consult.cbso.nbb.be/api/external/broker/public/deposits/pdf/53298dd0-866f-11f1-9f93-0786a55f9609,Public CIK dual of mined city_geel,Publish Opgroeien matrix behind envelope 1.53m + why omzet+73 empty VKT and why pnl DROP 201944 while destin 201944 and cash JUMP 1698135,{SRC_PDF},strong,Vlaanderen>Antwerpen>Geel>De Augustientjes>JR2025_statutory_L5,tick2475; Strong official native PDF; leftover mined city_geel CIK; 1 VE; prior-year identical; NOT every-10; NOT Hupskadee remine; NOT Pardoes remine; NOT Bambi remine; NOT Zonneschijn remine; NOT Infano remine; NOT Hupskadee BV private; NOT Zusterhof remine; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"De Augustientjes bruto JUMP 1.53m / omzet+73 empty VKT / pnl DROP 202k / destin 202k / cash JUMP 1.70m (YE2025 leftover city_geel CIK)",
"L5",
"cik_vzw_statutory",
"Vlaanderen>Antwerpen>Geel>De Augustientjes>JR2025",
"1527461",
"1527461",
"PDF envelope 1527461 = bruto 9900 VKT because omzet empty; 70 empty; 73 empty; 76A empty; bruto 1527461; bedrijfswinst DROP 150802; pnl DROP 201944; equity JUMP 2105573; assets JUMP 2540138; debt JUMP 157105; FTE 21.1; kapitaalsubsidies DROP 44650; destin691 201944; cash JUMP 1698135; leftover city_geel CIK",
"strong",
SRC_PDF,
"Opgroeien + leftover city_geel CIK",
"CIK / Kind en Gezin groepsopvang leftover city_geel",
"1.53m envelope; omzet+73 empty VKT; pnl DROP 201944; destin 201944; cash JUMP 1698135; leftover city_geel CIK",
"5.48",
"5.22",
"5.28",
"5.36",
"FOI Opgroeien matrix behind envelope 1.53m + why omzet+73 empty VKT and why pnl DROP 201944 while destin 201944 and cash JUMP 1698135",
"active",
"",
"tick2475 leftover mined city_geel CIK after Hupskadee lock; 1 VE; prior-year identical; NOT every-10; NOT Hupskadee remine; NOT Pardoes remine; NOT Bambi remine; NOT Zonneschijn remine; NOT Infano remine; NOT Hupskadee BV 0476.248.224 private BV; NOT Zusterhof remine; NOT KIOS Schoten no deposits; NOT Molleke city_mol YE2024; NOT t Sas city_denderleeuw YE2024 2026-00050081",
])
assert len(next(csv.reader(StringIO(row))))==21
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>Antwerpen>Geel>De Augustientjes>CIK",
"entity_id": EID,
"what_is_missing": "Opgroeien split behind envelope 1527461 (bruto 9900 VKT; omzet 70 empty + 73 empty + 76A empty) and why destin 201944 while pnl DROP 201944 and cash JUMP 1698135 and kapitaalsubsidies DROP 44650 and 62 JUMP 1291269 FTE DROP 21.1",
"why_it_matters": "Strong official PDF leftover public CIK of mined city_geel; VKT envelope bruto 1.53m because omzet empty; public Opgroeien groepsopvang 1 VE Kollegestraat 120 Geel; 86 plaatsen; destin 202k / cash JUMP 1.70m / pnl DROP 30.8%",
"priority": "8",
"recipient_body": "VZW Kinderdagverblijf De Augustientjes / Raad van Bestuur",
"recipient_email": "info@deaugustientjes.be",
"recipient_postal": "Kollegestraat 120 2440 Geel",
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
"notes": "tick2475; ready NOT sent; Strong official native NBB PDF; leftover mined city_geel CIK after Hupskadee lock; 1 VE; prior-year identical; NOT every-10; off Hupskadee remine; off Pardoes remine; off Bambi remine; off Zonneschijn remine; off Hupskadee BV private; off Zusterhof remine",
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
if rq_raw.count(b"rq_2475,")!=1: raise SystemExit(f"bad 2475 count {rq_raw.count(b'rq_2475,')}")
if b"rq_2476," in rq_raw: raise SystemExit("2476 exists")
idx=rq_raw.rfind(b"rq_2475,")
if idx<0: raise SystemExit("rq_2475 not found")
new_2475=(
"rq_2475,leftover dual Kinderdagverblijf De Augustientjes YE2025,hole_fill,8,done,L5,vzw_augustientjes_geel,"
"Took unused leftover public CIK Kinderdagverblijf De Augustientjes 0445.602.360 leftover mined city_geel. Official NBB VKT-VZW YE2025 2026-00320618 native 14p. Envelope bruto 9900 JUMP 1527461 (omzet+73 empty VKT); pnl DROP 201944; destin 201944; cash JUMP 1698135; FTE 21.1. NOT Hupskadee remine. NOT Pardoes remine. NOT Bambi remine. NOT Zonneschijn remine. NOT Hupskadee BV private. NOT Zusterhof remine.,"
f",{STAMP},{STAMP},tick2475 leftover mined city_geel CIK; Strong native PDF; 1 VE; prior-year identical; next every-10 is 2480\n"
)
new_2476=(
"rq_2476,leftover dual after De Augustientjes — hunt unused public dual,hole_fill,8,open,L5,,"
"After De Augustientjes YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf. Less-picked mined cities still with 0 leftover CIK: herentals / schoten / vilvoorde / mol (geel now has De Augustientjes; mechelen has Pardoes; kalmthout has Bambi; dendermonde has Zonneschijn; begijnendijk has Hupskadee). Molleke 0448.186.520 leftover city_mol YE2024 — take ONLY if unused + official YE2025 native PDF. t Sas 0448.731.106 leftover city_denderleeuw YE2024 only 2026-00050081 — skip unless YE2025. Villa Boempatat 0660.616.520 leftover city_gent YE2025 2026-00396513 CDN 403 / SCAN — take ONLY if unused + official native-text YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen YE2025 2026-00374905 CDN 403 — take ONLY if CDN 200 native. Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO! Next / Zo Groot Oostende still YE2024 — take ONLY if unused + official YE2025 PDF. De Bolster 0861.680.989 YE2025 zetel Zwalm (city_zwalm not mined) — take ONLY if leftover of a mined parent. Jessa leftover city_hasselt hospital YE2025 PDF — take ONLY if unused + official YE2025 euros extract. KIOS 0882.468.881 leftover city_schoten — no jaarrekening skip unless deposits appear. Dol-Fijn 0439.731.880 zetel Turnhout leftover-via-VE Herentals — not enough. NOT De Augustientjes remine. NOT Hupskadee remine. NOT Hupskadee BV 0476.248.224 private. NOT Pardoes remine. NOT Bambi remine. NOT Zonneschijn remine. NOT Infano remine. NOT Vijverbeek remine. NOT Mater Dei remine. NOT Savio remine. NOT 3Wplus remine. NOT Paideia remine. NOT Ooievaarsnest remine. NOT De Zonnekindjes remine. NOT D'n Opvang remine. NOT CAR Overleie remine. NOT Gesticht remine. NOT Grauwzusters convent. NOT Hocus-Pocus remine. NOT VKA remine. NOT Soetkin remine. NOT t Sloeberke remine. NOT CAR Accent remine. NOT De Groene Verte remine. NOT De Vleugels remine. NOT De Pallieterkes remine. NOT De Medemens remine. NOT OKO & ZO remine. NOT Harlekijntjes remine. NOT Hartjes remine. NOT De Wissel remine. NOT Familia remine. NOT t Zonnetje remine. NOT Kindercentrum remine. NOT Duinhuisjes remine. NOT Helan. NOT Hebe training. NOT WZC OLVA remine. NOT De Speelboom Brussels leftover-via-VE. NOT GERUST zorgcentrale. NOT Zo Groot remine. NOT De Elfjes remine. NOT De Steijgertjes remine. NOT Vormingscentrum training. NOT Zwarte Zusters dissolved. NOT Dominiek Savio remine. NOT EVA Dilbeek remine. NOT WZC Mater Dei Heikruis remine. NOT Ferm Kinderopvang remine. NOT Molleke YE2024 remine. NOT t Sas YE2024 remine. NOT Witte Meren remine. NOT Zusterhof remine. NOT Pardoes NV bookshop. NOT Olliebollie BV private. NOT In de wolken BV private. NOT Troetelland Geel private BV. NOT De Zandkapoentjes BV private.,"
f",{STAMP},{STAMP},spawned after tick2475; De Augustientjes taken leftover mined city_geel CIK; Hupskadee taken leftover mined city_begijnendijk CIK; Pardoes taken leftover mined city_mechelen CIK; Bambi taken leftover mined city_kalmthout CIK; Zonneschijn taken leftover mined city_dendermonde CIK; Infano taken leftover mined city_ternat CIK EVERY-10; t Sas city_denderleeuw YE2024; Molleke city_mol YE2024; KIOS Schoten no deposits; next every-10 is 2480\n"
)
if new_2475.count("\n")!=1 or new_2476.count("\n")!=1: raise SystemExit("bad rq newlines")
for label,line in [("2475",new_2475),("2476",new_2476)]:
    n=len(next(csv.reader(StringIO(line))))
    if n!=12: raise SystemExit(f"{label} fields {n} != 12")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2475.encode("utf-8"))
    f.write(new_2476.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2475", chk.count(b"rq_2475,"), "n2476", chk.count(b"rq_2476,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2475,2475,no,tick2475 leftover dual De Augustientjes 0445.602.360 Strong native PDF (omzet70 empty VKT; 73 empty VKT; 76A empty; envelope bruto 9900 JUMP 1527461; bruto JUMP 1527461; pnl DROP 201944; 9901 DROP 150802; equity JUMP 2105573; assets JUMP 2540138; debt JUMP 157105; FTE DROP 21.1; kapitaalsubsidies DROP 44650; destin691 201944; 791 empty; cash JUMP 1698135; geldbeleggingen empty; 1 VE leftover city_geel CIK); leftover mined city_geel CIK; prior-year identical; NOT Hupskadee remine; NOT Hupskadee BV 0476.248.224 private; NOT Pardoes remine; NOT Bambi remine; NOT Zonneschijn remine; NOT Infano remine; NOT Vijverbeek remine; NOT t Zonnetje remine; NOT Kindercentrum remine; NOT Duinhuisjes remine; NOT 3Wplus remine; NOT Mater Dei remine; NOT WZC Mater Dei Heikruis remine; NOT Savio remine; NOT Dominiek Savio remine; NOT EVA Dilbeek remine; NOT Paideia remine; NOT Ooievaarsnest remine; NOT DE ZONNEKINDJES remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT Grauwzusters convent; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens KDV remine; NOT De Medemens parent remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Mini-creches GO Next remine; NOT Kinderlach; NOT Zo Groot YE2024; NOT De Speelboom Brussels leftover-via-VE; NOT Elief CDN 403; NOT Villa Boempatat SCAN/CDN403; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; NOT De Bolster Zwalm not leftover mined parent; NOT GERUST zorgcentrale; NOT De Elfjes remine; NOT De Steijgertjes remine; NOT Vormingscentrum training; NOT Zwarte Zusters dissolved; NOT Ferm Kinderopvang remine; NOT KIOS Schoten no deposits; NOT Molleke city_mol YE2024; NOT t Sas city_denderleeuw YE2024 2026-00050081; NOT Dol-Fijn Turnhout leftover-via-VE; NOT Witte Meren remine; NOT Zusterhof remine; NOT Pardoes NV bookshop; NOT Olliebollie BV private; NOT In de wolken BV private; NOT Troetelland Geel private BV; NOT De Zandkapoentjes BV private; next every-10 is 2480; next rq_2476 leftover dual\n",
encoding="utf-8",
)
print("loop_state ok")

log=ROOT/"docs/doge/loop_log.md"
log_raw=log.read_bytes()
if not log_raw.endswith(b"\n"): raise SystemExit("loop_log no LF")
entry=f"""
### {STAMP} - tick 2475 - rq_2475 Kinderdagverblijf De Augustientjes (bruto JUMP 1.53m / omzet+73 empty VKT / pnl DROP 202k / destin 202k / cash JUMP 1.70m / Strong PDF)

- Unit: **rq_2475** leftover dual after **Hupskadee@2474**. Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024** (not re-downloaded); FARO 2026-00010398 still **YE2024** (HEAD-only policy). Discovery path: less-picked mined Flanders cities with 0 leftover CIK (herentals / schoten / vilvoorde / geel / mol). Confirmed `city_herentals` / `city_schoten` / `city_vilvoorde` / `city_geel` / `city_mol` exist. Kinderdagverblijf Molleke **0448.186.520** leftover city_mol still **YE2024** — skip. KIOS leftover city_schoten — no jaarrekening — skip. t Sas leftover city_denderleeuw **YE2024** **2026-00050081** — skip. Dol-Fijn **0439.731.880** zetel Turnhout leftover-via-VE Herentals YE2025 — not enough. Witte Meren leftover city_mol already mined. Zusterhof leftover city_geel already mined. Villa Boempatat leftover city_gent **YE2025** **2026-00396513** CDN **403** / SCAN — not taken. Speelhuis Elief leftover city_antwerpen unused YE2025 **2026-00374905** CDN **403** — not taken. Kinderlach leftover city_eeklo still **YE2024**. De Linde Ronse leftover city_ronse still **YE2024**. Woon en Zorg H. Hart Kortrijk leftover city_kortrijk still **YE2024**. Jessa leftover city_hasselt hospital YE2025 PDF / hospital special schema — not taken. Mini-creches GO! Next leftover city_hasselt still **YE2024**. Zo Groot Oostende leftover city_oostende still **YE2024**. Familiehulp De Speelboom YE2025 unused Brussels zetel / Herentals VE leftover-via-VE — not taken. De Bolster 0861.680.989 YE2025 zetel Zwalm (city_zwalm not mined) — not taken. GERUST Zorgcentrale leftover city_herentals YE2025 — zorgcentrale not in dual types — not taken. Hummeltjeshof city-run Herentals — skip. CIK Geel city-run — skip. De Bengelbende city-run — skip. Vormingscentrum leftover city_gent training — skip. Helan Kinderopvang already skipped. Zwarte Zusters dissolved — skip. Private BVs (Olliebollie **0805.501.361** / In de wolken **1006.181.196** / Troetelland Geel / De Zandkapoentjes **0507.854.980** / Vlindertje Schoten / Regenboog Vilvoorde / Hupskadee BV **0476.248.224**) skipped. Hupskadee 0863.886.651 just mined — do not remine. Pardoes 0417.400.205 already mined — do not remine. Bambi 0443.006.522 already mined — do not remine. Zonneschijn 0877.850.493 already mined — do not remine. Infano 0477.578.411 already mined — do not remine. Vijverbeek already mined — do not remine. Mater Dei already mined — do not remine. Savio already mined — do not remine. t Zonnetje Waregem already mined — do not remine. First leftover unused + live official YE2025 native euros: took FREE leftover Flemish **VZW Kinderdagverblijf De Augustientjes** YE2025 (KBO **0445.602.360**; zetel Kollegestraat 120 2440 Geel; **Actief** **1 VE** **2.150.820.689** Kinderdagverblijf De Augustientjes since 03.01.2006; RSZ2025 **88.911**; leftover of mined **city_geel**; info@deaugustientjes.be; Opgroeien groepsopvang; Kind en Gezin-vergund; 86 plaatsen; 7 semi-verticale leefgroepen; inclusieve opvang). Identity trap: De Augustientjes 0445.602.360 ≠ Hupskadee **0863.886.651** leftover city_begijnendijk just mined; ≠ Hupskadee BV **0476.248.224** private BV; ≠ Pardoes **0417.400.205**; ≠ Kinderdagverblijf Bambi **0443.006.522**; ≠ Zonneschijn **0877.850.493**; ≠ INFANO **0477.578.411**; ≠ Kinderdagverblijf Vijverbeek **0448.164.744**; ≠ t Zonnetje Waregem **0443.648.306**; ≠ DE ZONNEKINDJES **0416.541.952**; ≠ ZONNESTRAAL / Zonnestraal Junior; ≠ Kindercentrum Waregem **0408.226.775**; ≠ Duinhuisjes **0413.323.037**; ≠ Groepsopvang Mater Dei **0431.168.859**; ≠ WZC Mater Dei Heikruis; ≠ Kinderdagverblijf Savio **0472.564.501**; ≠ Dominiek Savio; ≠ EVA Dilbeek **0477.276.325**; ≠ Paideia **0445.129.931**; ≠ KDV Ooievaarsnest **0418.588.256**; ≠ D'n Opvang **0676.442.465**; ≠ CAR Overleie **0454.250.505**; ≠ Gesticht **0410.918.031**; ≠ HOCUS-POCUS **0466.893.167**; ≠ VKA **0433.480.132**; ≠ Soetkin **0443.641.970**; ≠ t Sloeberke **0410.973.360**; ≠ CAR Accent **0413.208.122**; ≠ Speelhuis Elief **0451.624.377**; ≠ Villa Boempatat **0660.616.520**; ≠ De Groene Verte **0465.061.649**; ≠ De Vleugels **0431.408.290**; ≠ De Pallieterkes **0418.538.865**; ≠ De Medemens Kinderdagverblijven **0893.678.915**; ≠ De Medemens **0428.692.191**; ≠ OKO & ZO **0862.154.608**; ≠ Harlekijntjes **0407.700.403**; ≠ Hartjes Ninove **0446.391.327**; ≠ Hartjes Tienen **0441.374.348**; ≠ De Wissel **0421.913.376**; ≠ Ferm Kinderopvang **0416.117.627**; ≠ Familia **0461.401.779**; ≠ Peutertuinen GO Mariakerke **0410.221.116**; ≠ Mini-crèches GO! Next **0896.468.060**; ≠ Kinderlach **0450.275.186**; ≠ Helan 0464.151.037; ≠ Hebe **0451.789.772**; ≠ WZC OLVA **0430.977.136**; ≠ H.Hart Kortrijk **0413.595.330**; ≠ De Linde Ronse **0778.279.401**; ≠ De Bolster **0861.680.989**; ≠ GERUST **0776.808.068**; ≠ Jessa **0821.142.117**; ≠ AZ Sint-Maria **0467.967.491**; ≠ De Elfjes **0455.636.912**; ≠ De Steijgertjes **0413.421.720**; ≠ TKDV Het Veer Kloosterstraat 6; ≠ Vormingscentrum **0413.342.338** training; ≠ Zwarte Zusters **0413.272.260** dissolved; ≠ KIOS **0882.468.881**; ≠ Molleke **0448.186.520**; ≠ t Sas **0448.731.106**; ≠ Dol-Fijn **0439.731.880**; ≠ Witte Meren **0418.234.997**; ≠ Zusterhof **0473.762.450**; ≠ Pardoes NV **0867.020.840** bookshop; ≠ Olliebollie BV **0805.501.361**; ≠ In De Wolken BV **1006.181.196**; ≠ De Zandkapoentjes BV **0507.854.980**. 1 VE Geel — leftover of mined city_geel (zetel + Kollegestraat 120). Confirmed leftover public (Opgroeien CIK groepsopvang; Kind en Gezin-vergund; 86 plaatsen; 7 semi-verticale leefgroepen; inclusieve opvang) not convent / not private clinic / not school / not OVBJ / not WZC / not VAPH / not Ferm / not Hupskadee remine / not Pardoes remine / not Bambi remine / not Zonneschijn remine / not Zusterhof remine / not private BV. VKT-VZW **native text** (not scan) — 49373 B / 14p all native euros (VKT-VZW 6.1.1 / 6.3 / 6.5 / 6.6 / 7 / 8 niet dienstig; 6.1.2 / 6.1.3 / 6.2 / 6.4 / 6.7 / 6.8 present).
- Found: official NBB VKT-VZW native PDF deposit **2026-00320618** (49373 B / 14p; AV **02.06.2026**; header **23.07.2026**; official NBB broker UUID 53298dd0 GET **200** 49373 official NBB-generated OpenPDF 1.3.26 CreationDate 23.07.2026; CDN GET **200** same 49373 MD5 Last-Modified 03.08.2026; importFileType XBRL; all 14p native; prior-year identical not restated) — omzet 70 **empty** VKT; 73 **empty** VKT; 76A **empty**; envelope bruto 9900 **EUR1527461** JUMP +3.68% (VKT envelope because omzet empty; was 1473282); bruto 9900 **EUR1527461** JUMP +3.68%; 62 **EUR1291269** JUMP +12.27%; 630 **EUR85111** DROP −3.64%; 66A **EUR60**; 640/8 **EUR219** DROP; 635/9 **empty**; 631/4 **empty**; bedrijfswinst 9901 **EUR150802** DROP −35.69% (was 234505); pnl 9904 **EUR201944** DROP −30.84% (was 292012); equity **EUR2105573** JUMP +8.98%; assets **EUR2540138** JUMP +7.65%; debt **EUR157105** JUMP +4.59%; FTE **21.1** DROP −4.52% (was 22.1; 100 21.1; 105 20.8); kapitaalsubsidies **EUR44650** DROP −38.87%; destin 691 **EUR201944** DROP −30.84% (791 empty; 13 JUMP 1832955 = prior 1631011 + destin 201944); 791 **empty**; cash **EUR1698135** JUMP +19.19%; geldbeleggingen **empty**; gebouwen **EUR693727** DROP; MVA 22/27 **EUR707082** DROP; aanbouw **empty**; capex **EUR15133**; fondsen 10 **EUR227968** FLAT; overgedragen 14 **empty**; bestemde fondsen 13 **EUR1832955** JUMP; voorzieningen 16 **EUR277460** FLAT; FVA 28 **EUR1000** FLAT; LT recv 29 **empty**. Strong KBO + Strong PDF (native all pages; not SBM table; not Companyweb euros). Site: 1 VE leftover mined city_geel CIK. NOT Hupskadee remine. NOT Pardoes remine. NOT Bambi remine. NOT Zonneschijn remine. NOT Hupskadee BV private. NOT Zusterhof remine. NOT t Sas YE2024. NOT Molleke YE2024. NOT KIOS no deposits.
- Wrote: sources (+4); budgets (+11); commitments (+1); leaderboard (+1 pi 5.36); entities (+1 vzw_augustientjes_geel); foi + draft `gap_augustientjes_opgroeien_matrix_bruto_1_53m_omzet73_empty_pnl_drop_202k_destin_202k_cash_jump_l5`; rq_2475=done + rq_2476 open; loop_state ticks=2475; raw tick2475/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2480**). Next: rq_2476 unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT De Augustientjes remine / NOT Hupskadee remine / NOT Hupskadee BV private / NOT Pardoes remine / NOT Bambi remine / NOT Zonneschijn remine / NOT Infano remine / NOT Vijverbeek remine / NOT t Zonnetje remine / NOT Kindercentrum remine / NOT Duinhuisjes remine / NOT Mater Dei remine / NOT Savio remine / NOT 3Wplus remine / NOT Paideia remine / NOT Ooievaarsnest remine / NOT De Zonnekindjes remine / NOT D'n Opvang remine / NOT CAR Overleie remine / NOT Gesticht remine / NOT Grauwzusters convent / NOT HOCUS-POCUS remine / NOT VKA remine / NOT Soetkin remine / NOT t Sloeberke remine / NOT CAR Accent remine / NOT De Groene Verte remine / NOT De Vleugels remine / NOT De Pallieterkes remine / NOT De Medemens remine / NOT OKO & ZO remine / NOT Harlekijntjes remine / NOT Hartjes remine / NOT De Wissel remine / NOT Familia remine / NOT Mini-creches GO Next remine / NOT WZC OLVA remine / NOT Hebe training / NOT Quattro remine / NOT GERUST zorgcentrale / NOT Zo Groot remine / NOT De Elfjes remine / NOT De Steijgertjes remine / NOT Vormingscentrum training / NOT Zwarte Zusters dissolved / NOT Dominiek Savio remine / NOT EVA Dilbeek remine / NOT WZC Mater Dei Heikruis remine / NOT Ferm Kinderopvang remine / NOT Molleke YE2024 / NOT t Sas YE2024 / NOT Witte Meren remine / NOT Zusterhof remine / NOT Pardoes NV bookshop / NOT Olliebollie BV private / NOT In de wolken BV private / NOT Troetelland Geel private BV / NOT De Zandkapoentjes BV private). NOW leftover candidates: Molleke 0448.186.520 leftover city_mol YE2024 — take ONLY if unused + official YE2025 native PDF. t Sas 0448.731.106 leftover city_denderleeuw YE2024 only 2026-00050081 — skip unless YE2025. Villa Boempatat 0660.616.520 leftover city_gent YE2025 **2026-00396513** CDN **403** / SCAN — take ONLY if unused + official native-text YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen unused YE2025 **2026-00374905** CDN **403** — take ONLY if unused + CDN 200 native YE2025 PDF. Kinderlach leftover city_eeklo still YE2024 — take ONLY if unused + official YE2025 PDF. De Linde Ronse leftover city_ronse still YE2024 — take ONLY if unused + official YE2025 PDF. H.Hart Kortrijk leftover city_kortrijk still YE2024 — take ONLY if unused + official YE2025 PDF. Jessa leftover city_hasselt hospital YE2025 PDF — take ONLY if unused + official YE2025 euros extract. De Bolster 0861.680.989 YE2025 zetel Zwalm — leftover of mined parent only. Familiehulp De Speelboom YE2025 Brussels zetel — leftover-via-VE not enough per LOOP.md. Mini-creches GO! Next leftover city_hasselt still YE2024 — skip unless YE2025. Zo Groot Oostende leftover city_oostende still YE2024 — skip unless YE2025. KIOS leftover city_schoten no deposits — skip. Dol-Fijn leftover-via-VE not enough. Tick **2480** is next every-10.

"""
with log.open("ab") as f:
    f.write(entry.encode("utf-8"))
print("loop_log ok")
print("WRITE CORE DONE")
