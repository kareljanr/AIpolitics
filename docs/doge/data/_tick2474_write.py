from pathlib import Path
import csv
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2474_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_hupskadee_jr2025_nbb_pdf_2474"
SRC_KBO="src_hupskadee_kbo_2474"
SRC_SBM="src_hupskadee_sbm_2474"
SRC_SITE="src_hupskadee_site_2474"
EID="vzw_hupskadee_begijnendijk"
GAP="gap_hupskadee_opgroeien_matrix_bruto_701k_omzet73_empty_pnl_flip_loss_79k_cash_drop_destin_empty_l5"
COMM="comm_hupskadee_jr2025_statutory_bruto_701k_omzet73_empty_pnl_flip_loss_79k_cash_drop"
LB="lb_hupskadee_bruto_701k_omzet73_empty_pnl_flip_loss_79k_cash_drop_destin_empty_jr2025"
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
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Kinderdagverblijf Hupskadee deposit 2026-00374083,https://consult.cbso.nbb.be/api/external/broker/public/deposits/pdf/98e94f9d-8ccc-11f1-9362-5fa85de4714b,NBB official WVV deposit PDF via official broker,{DAY},budget,tick2474; official native PDF 50198 bytes 15p VKT-VZW 26.0.15 m04-f; header 31.07.2026; AV 30.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-08-03 11:42:10 UTC OpenPDF 1.3.26; all 15p native; official NBB broker UUID 98e94f9d-8ccc-11f1-9362-5fa85de4714b GET 200 50198 official NBB-generated PDF; CDN 2026-00374083 GET 403; importFileType XBRL; VKT-VZW 6.2 6.3 6.5 8 niet dienstig; 6.1.1 6.1.2 6.1.3 6.4 6.6 6.7 7 present; prior-year identical not restated; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO KINDERDAGVERBLIJF HUPSKADEE 0863.886.651,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0863886651,KBO Public Search FOD Economie,{DAY},official_register,tick2474; Actief; 1 VE 2.160.573.842 KINDERDAGVERBLIJF HUPSKADEE vzw Kleinesteenweg 55 3130 Begijnendijk since 21.03.2007; VZW since 30.12.2003; begindatum 08.03.2004; zetel Kleinesteenweg 55 3130 Begijnendijk since 30.12.2003; toelating Kinderopvang VL since 01.04.2014; RSZ-werkgever since 01.06.2004; RSZ2025 88.911; FOI info@hupskadee.be; leftover mined city_begijnendijk CIK; NOT Hupskadee BV 0476.248.224 private BV; NOT Pardoes 0417.400.205 remine; NOT Bambi 0443.006.522 remine; NOT Zonneschijn 0877.850.493 remine",
f"{SRC_SBM},NBB Consult / SBM fiche Hupskadee 0863886651 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0863886651,NBB Consult / SBM,{DAY},official_register,tick2474; deposit-id 2026-00374083 YE 01.01.2025-31.12.2025 filing 31.07.2026 published VKT-VZW Verkort model vereniging Initial; Companyweb last-balansjaar 2025 deposit-id discovery OK euros NOT OK; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},Hupskadee FOI contact leftover city_begijnendijk CIK,https://www.hupskadee.be/,VZW KINDERDAGVERBLIJF HUPSKADEE leftover city_begijnendijk CIK Opgroeien groepsopvang 1 VE,{DAY},foi_contact,tick2474; FOI info@hupskadee.be; zetel Kleinesteenweg 55 3130 Begijnendijk; 1 VE leftover mined city_begijnendijk after Pardoes different-city skip; Opgroeien groepsopvang; Kind en Gezin-vergund; inkomenstarief IKT; 4 leefgroepen; NOT Hupskadee BV 0476.248.224 private BV; NOT Pardoes remine; NOT Bambi remine; NOT Zonneschijn remine; NOT Infano remine; NOT Vijverbeek remine; NOT t Zonnetje remine; NOT Kindercentrum remine; NOT Duinhuisjes remine; NOT Mater Dei remine; NOT Savio remine; NOT Paideia remine; NOT Ooievaarsnest remine; NOT DE ZONNEKINDJES remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Kinderlach YE2024; NOT Helan; NOT De Speelboom Brussels; NOT Villa Boempatat SCAN/CDN403; NOT Elief CDN 403; NOT Hebe training; NOT Zo Groot YE2024; NOT De Bolster Zwalm not leftover mined parent; NOT GERUST zorgcentrale; NOT Vormingscentrum training; NOT Zwarte Zusters dissolved; NOT KIOS Schoten no deposits; NOT Molleke city_mol YE2024; NOT t Sas city_denderleeuw YE2024 2026-00050081; NOT Dol-Fijn Turnhout leftover-via-VE; NOT Pardoes NV bookshop",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},KINDERDAGVERBLIJF HUPSKADEE,ASBL Kinderdagverblijf Hupskadee,Kinderdagverblijf Hupskadee VZW (leftover city_begijnendijk CIK),parastatal,city_begijnendijk,nl,https://www.hupskadee.be/,info@hupskadee.be,Kleinesteenweg 55 3130 Begijnendijk,tick2474 YE2025 Strong official native NBB PDF deposit 2026-00374083 + Strong KBO 0863.886.651 Actief 1 VE 2.160.573.842; omzet70 empty VKT; 73 empty VKT; 76A empty; envelope bruto 9900 JUMP 700865; bruto JUMP 700865; pnl FLIP LOSS -78745; 9901 FLIP LOSS -81482; equity DROP 69055; assets JUMP 276216; debt JUMP 207162; FTE JUMP 14.5; kapitaalsubsidies empty; destin691 empty; 791 78745; cash DROP 15536; geldbeleggingen empty; WCO; leftover city_begijnendijk CIK 1 VE; NOT Hupskadee BV 0476.248.224 private BV; NOT Pardoes Mechelen 0417.400.205 remine; NOT Bambi Kalmthout 0443.006.522 remine; NOT Zonneschijn Dendermonde 0877.850.493 remine; NOT Infano Ternat 0477.578.411 remine; NOT Vijverbeek Asse 0448.164.744 remine; NOT t Zonnetje Waregem 0443.648.306 remine; NOT Kindercentrum Waregem 0408.226.775 remine; NOT Duinhuisjes 0413.323.037 remine; NOT 3Wplus Kinderopvang Asse 0893.870.539 remine; NOT Mater Dei 0431.168.859 remine; NOT WZC Mater Dei Heikruis remine; NOT Savio Dilbeek 0472.564.501 remine; NOT Dominiek Savio remine; NOT EVA Dilbeek 0477.276.325 remine; NOT Paideia 0445.129.931 remine; NOT Ooievaarsnest 0418.588.256 remine; NOT DE ZONNEKINDJES 0416.541.952 remine; NOT D'n Opvang 0676.442.465 remine; NOT CAR Overleie 0454.250.505 remine; NOT Gesticht 0410.918.031 remine; NOT HOCUS-POCUS 0466.893.167 remine; NOT VKA 0433.480.132 remine; NOT Soetkin 0443.641.970 remine; NOT t Sloeberke 0410.973.360 remine; NOT CAR Accent 0413.208.122 remine; NOT De Elfjes 0455.636.912 remine; NOT De Steijgertjes 0413.421.720 remine; NOT H.Hart WZC 0413.595.330; NOT Zo Groot 0818.420.771 leftover city_oostende YE2024; NOT De Groene Verte 0465.061.649 remine; NOT De Vleugels 0431.408.290 remine; NOT De Pallieterkes 0418.538.865 remine; NOT De Medemens KDV 0893.678.915 remine; NOT De Medemens parent 0428.692.191 remine; NOT OKO & ZO 0862.154.608 remine; NOT Harlekijntjes 0407.700.403 remine; NOT Hartjes Ninove 0446.391.327 remine; NOT Hartjes Tienen 0441.374.348 remine; NOT De Wissel 0421.913.376 remine; NOT Familia 0461.401.779; NOT Peutertuinen GO Mariakerke 0410.221.116; NOT Mini-creches GO Next 0896.468.060 leftover city_hasselt YE2024; NOT Kinderlach 0450.275.186; NOT Helan; NOT De Speelboom Brussels; NOT Villa Boempatat 0660.616.520 leftover city_gent YE2025 SCAN/CDN403 2026-00396513; NOT Elief 0451.624.377 CDN 403; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; NOT De Bolster 0861.680.989 YE2025 zetel Zwalm city_zwalm not mined; NOT GERUST 0776.808.068 zorgcentrale; NOT Jessa hospital special schema; NOT Vormingscentrum 0413.342.338 training; NOT Zwarte Zusters 0413.272.260 dissolved; NOT Ferm Kinderopvang 0416.117.627 remine; NOT ZONNESTRAAL; NOT Molleke 0448.186.520 leftover city_mol YE2024; NOT t Sas 0448.731.106 leftover city_denderleeuw YE2024 2026-00050081; NOT Dol-Fijn 0439.731.880 Turnhout zetel leftover-via-VE; NOT Pardoes NV 0867.020.840 bookshop; NOT Witte Meren remine; NOT Zusterhof remine; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria SCAN; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Zo Groot Oostende YE2024 not taken; H.Hart Kortrijk YE2024 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_hupskadee_omzet_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 70 omzet YE2025 empty (VKT; envelope is bruto 9900),{SRC_PDF},strong,tick2474; PDF p5 native; YE2024 empty; 73 empty; 76A empty",
f"bud_hupskadee_73_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 empty (VKT),{SRC_PDF},strong,tick2474; PDF p5 native; YE2024 empty; FOI Opgroeien matrix behind envelope 700865",
f"bud_hupskadee_opbr_jr2025_statutory,{EID},2025,700865,700865,700865,NBB VKT-VZW envelope bruto 9900 YE2025 JUMP +2.75% (omzet empty so envelope is bruto 9900),{SRC_PDF},strong,tick2474; PDF p5 native; YE2024 682109; 70 empty; 73 empty; 76A empty",
f"bud_hupskadee_bruto_jr2025_statutory,{EID},2025,700865,700865,700865,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +2.75% (VKT envelope because omzet empty),{SRC_PDF},strong,tick2474; PDF p5 native; YE2024 682109; 76A empty; 73 empty",
f"bud_hupskadee_pnl_jr2025_statutory,{EID},2025,-78745,-78745,-78745,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 FLIP to LOSS (was 14802),{SRC_PDF},strong,tick2474; PDF p5 native; YE2024 14802; bedrijfswinst 9901 -81482 FLIP; destin691 empty",
f"bud_hupskadee_bedrijfswinst_jr2025_statutory,{EID},2025,-81482,-81482,-81482,NBB VKT-VZW code 9901 bedrijfswinst YE2025 FLIP to LOSS (was 14933),{SRC_PDF},strong,tick2474; PDF p5 native; YE2024 14933; 62 773351 JUMP; 630 8749 JUMP; 66A empty; 640/8 248 DROP; 635/9 empty; 631/4 empty",
f"bud_hupskadee_equity_jr2025_statutory,{EID},2025,69055,69055,69055,NBB VKT-VZW code 10/15 eigen vermogen YE2025 DROP -53.28%,{SRC_PDF},strong,tick2474; PDF p4 native; YE2024 147799; kapitaalsubsidies empty; overgedragen 14 empty; fondsen 10 empty; bestemde fondsen 13 DROP 69055",
f"bud_hupskadee_assets_jr2025_statutory,{EID},2025,276216,276216,276216,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +11.06%,{SRC_PDF},strong,tick2474; PDF p3 native; YE2024 248713; MVA 22/27 53543 JUMP; cash 15536 DROP; geldbeleggingen empty; aanbouw 27 empty; FVA 28 empty; LT recv 29 121766 JUMP",
f"bud_hupskadee_debt_jr2025_statutory,{EID},2025,207162,207162,207162,NBB VKT-VZW code 17/49 schulden YE2025 JUMP +105.29%,{SRC_PDF},strong,tick2474; PDF p4 native; YE2024 100914; 17 empty; 42/48 207054 JUMP; 43 37518",
f"bud_hupskadee_cash_jr2025_statutory,{EID},2025,15536,15536,15536,NBB VKT-VZW code 54/58 liquide middelen YE2025 DROP -84.52%,{SRC_PDF},strong,tick2474; PDF p3 native; YE2024 100388; geldbeleggingen 50/53 empty; capex 27180 gebouwen DROP 1749",
f"bud_hupskadee_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty (791 78745; 13 DROP 69055 approx prior 147799 - 791 78745; 1 EUR rounding),{SRC_PDF},strong,tick2474; PDF p6 native; YE2024 destin 14802; bestemde fondsen 13 DROP 69055 FOI",
])
print("entities+budgets ok")

cash_json=(
"\"{\"\"2025_omzet\"\":0,\"\"2025_73\"\":0,\"\"2025_76A\"\":0,"
"\"\"2025_opbr70_76A\"\":700865,\"\"2025_bruto\"\":700865,"
"\"\"2025_pnl\"\":-78745,\"\"2025_bedrijfswinst\"\":-81482,"
"\"\"2025_equity\"\":69055,\"\"2025_assets\"\":276216,\"\"2025_debt\"\":207162,"
"\"\"2025_fte\"\":14.5,\"\"2025_kapitaalsubsidies\"\":0,\"\"2025_destin691\"\":0,"
"\"\"2025_791\"\":78745,\"\"2025_cash\"\":15536,\"\"2025_geldbeleggingen\"\":0,"
"\"\"2025_personnel62\"\":773351,\"\"2025_gebouwen22\"\":1749,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":0,"
"\"\"2025_fondsen10\"\":0,\"\"2025_overgedragen14\"\":0,"
"\"\"2025_bestemdefondsen13\"\":69055,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":8749,\"\"2025_capex\"\":27180,"
"\"\"2025_ltrecv29\"\":121766,\"\"2025_related9500\"\":53706,"
"\"\"2024_omzet\"\":0,\"\"2024_73\"\":0,"
"\"\"2024_opbr70_76A\"\":682109,\"\"2024_bruto\"\":682109,\"\"2024_pnl\"\":14802,\"\"2024_bedrijfswinst\"\":14933,"
"\"\"2024_equity\"\":147799,\"\"2024_assets\"\":248713,"
"\"\"2024_debt\"\":100914,\"\"2024_cash\"\":100388,\"\"2024_fte\"\":12.6,"
"\"\"2024_destin691\"\":14802,\"\"2024_kapitaalsubsidies\"\":0,\"\"2024_76A\"\":0,"
"\"\"2024_geldbeleggingen\"\":0}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Hupskadee YE2025 (bruto JUMP 701k / omzet+73 empty VKT / pnl FLIP LOSS 79k / cash DROP / destin empty / Strong PDF),{EID},Opgroeien + leftover city_begijnendijk CIK,VZW KINDERDAGVERBLIJF HUPSKADEE (KBO 0863.886.651; Actief; 1 VE; zetel Begijnendijk),2026-06-30,2025,2025,700865,{cash_json},0,active,https://consult.cbso.nbb.be/api/external/broker/public/deposits/pdf/98e94f9d-8ccc-11f1-9362-5fa85de4714b,Public CIK dual of mined city_begijnendijk,Publish Opgroeien matrix behind envelope 701k + why omzet+73 empty VKT and why pnl FLIP LOSS -78745 while destin empty and cash DROP 15536 and WCO,{SRC_PDF},strong,Vlaanderen>Vlaams-Brabant>Begijnendijk>Hupskadee>JR2025_statutory_L5,tick2474; Strong official native PDF; leftover mined city_begijnendijk CIK; 1 VE; prior-year identical; NOT every-10; NOT Pardoes remine; NOT Bambi remine; NOT Zonneschijn remine; NOT Infano remine; NOT Hupskadee BV private; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"Hupskadee bruto JUMP 701k / omzet+73 empty VKT / pnl FLIP LOSS 79k / cash DROP / destin empty (YE2025 leftover city_begijnendijk CIK)",
"L5",
"cik_vzw_statutory",
"Vlaanderen>Vlaams-Brabant>Begijnendijk>Hupskadee>JR2025",
"700865",
"700865",
"PDF envelope 700865 = bruto 9900 VKT because omzet empty; 70 empty; 73 empty; 76A empty; bruto 700865; bedrijfswinst FLIP LOSS -81482; pnl FLIP LOSS -78745; equity DROP 69055; assets JUMP 276216; debt JUMP 207162; FTE 14.5; kapitaalsubsidies empty; destin691 empty; cash DROP 15536; WCO; leftover city_begijnendijk CIK",
"strong",
SRC_PDF,
"Opgroeien + leftover city_begijnendijk CIK",
"CIK / Kind en Gezin groepsopvang leftover city_begijnendijk",
"701k envelope; omzet+73 empty VKT; pnl FLIP LOSS -78745; cash DROP 15536; destin empty; WCO; leftover city_begijnendijk CIK",
"5.45",
"5.15",
"5.20",
"5.30",
"FOI Opgroeien matrix behind envelope 701k + why omzet+73 empty VKT and why pnl FLIP LOSS -78745 while destin empty and cash DROP 15536 and WCO / related-party 53706",
"active",
"",
"tick2474 leftover mined city_begijnendijk CIK after Pardoes lock; 1 VE; prior-year identical; NOT every-10; NOT Pardoes remine; NOT Bambi remine; NOT Zonneschijn remine; NOT Infano remine; NOT Vijverbeek remine; NOT t Zonnetje remine; NOT Kindercentrum remine; NOT Duinhuisjes remine; NOT Mater Dei remine; NOT Savio remine; NOT Kinderlach YE2024; NOT Zo Groot YE2024; NOT Elief CDN 403; NOT Villa Boempatat SCAN/CDN403; NOT De Speelboom Brussels; NOT Hupskadee BV 0476.248.224 private BV; NOT KIOS Schoten no deposits; NOT Molleke city_mol YE2024; NOT t Sas city_denderleeuw YE2024 2026-00050081",
])
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>Vlaams-Brabant>Begijnendijk>Hupskadee>CIK",
"entity_id": EID,
"what_is_missing": "Opgroeien split behind envelope 700865 (bruto 9900 VKT; omzet 70 empty + 73 empty + 76A empty) and why destin empty while pnl FLIP LOSS -78745 and cash DROP 15536 and debt JUMP 207162 and WCO / related-party 9500 53706 / LT recv 121766 / 62 JUMP 773351 FTE JUMP 14.5",
"why_it_matters": "Strong official PDF leftover public CIK of mined city_begijnendijk; VKT envelope bruto 701k because omzet empty; public Opgroeien groepsopvang 1 VE Kleinesteenweg 55 Begijnendijk; WCO / cash DROP 84.5% / equity DROP 53%",
"priority": "8",
"recipient_body": "VZW KINDERDAGVERBLIJF HUPSKADEE / Raad van Bestuur",
"recipient_email": "info@hupskadee.be",
"recipient_postal": "Kleinesteenweg 55 3130 Begijnendijk",
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
"notes": "tick2474; ready NOT sent; Strong official native NBB PDF; leftover mined city_begijnendijk CIK after Pardoes lock; 1 VE; prior-year identical; NOT every-10; off Pardoes remine; off Bambi remine; off Zonneschijn remine; off Hupskadee BV private",
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
if rq_raw.count(b"rq_2474,")!=1: raise SystemExit(f"bad 2474 count {rq_raw.count(b'rq_2474,')}")
if b"rq_2475," in rq_raw: raise SystemExit("2475 exists")
idx=rq_raw.rfind(b"rq_2474,")
if idx<0: raise SystemExit("rq_2474 not found")
new_2474=(
"rq_2474,leftover dual Kinderdagverblijf Hupskadee YE2025,hole_fill,8,done,L5,vzw_hupskadee_begijnendijk,"
"Took unused leftover public CIK Kinderdagverblijf Hupskadee 0863.886.651 leftover mined city_begijnendijk. Official NBB VKT-VZW YE2025 2026-00374083 native 15p. Envelope bruto 9900 JUMP 700865 (omzet+73 empty VKT); pnl FLIP LOSS -78745; cash DROP 15536; destin empty; FTE 14.5; WCO. NOT Pardoes remine. NOT Bambi remine. NOT Zonneschijn remine. NOT Hupskadee BV private.,"
f",{STAMP},{STAMP},tick2474 leftover mined city_begijnendijk CIK; Strong native PDF; 1 VE; prior-year identical; next every-10 is 2480\n"
)
new_2475=(
"rq_2475,leftover dual after Hupskadee — hunt unused public dual,hole_fill,8,open,L5,,"
"After Hupskadee YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf. Less-picked mined cities still with 0 leftover CIK: herentals / schoten / vilvoorde / geel / mol (mechelen now has Pardoes; kalmthout has Bambi; dendermonde has Zonneschijn; begijnendijk now has Hupskadee). Molleke 0448.186.520 leftover city_mol YE2024 (2025-00170508) — take ONLY if unused + official YE2025 native PDF. t Sas 0448.731.106 leftover city_denderleeuw YE2024 only 2026-00050081 — skip unless YE2025. Villa Boempatat 0660.616.520 leftover city_gent YE2025 2026-00396513 CDN 403 / SCAN — take ONLY if unused + official native-text YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen YE2025 2026-00374905 CDN 403 — take ONLY if CDN 200 native. Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO! Next / Zo Groot Oostende still YE2024 — take ONLY if unused + official YE2025 PDF. De Bolster 0861.680.989 YE2025 2026-00210039 zetel Zwalm (city_zwalm not mined) — take ONLY if leftover of a mined parent. Jessa leftover city_hasselt hospital YE2025 PDF — take ONLY if unused + official YE2025 euros extract. KIOS 0882.468.881 leftover city_schoten — no jaarrekening skip unless deposits appear. Dol-Fijn 0439.731.880 zetel Turnhout leftover-via-VE Herentals — not enough. NOT Hupskadee remine. NOT Hupskadee BV 0476.248.224 private. NOT Pardoes remine. NOT Bambi remine. NOT Zonneschijn remine. NOT Infano remine. NOT Vijverbeek remine. NOT Mater Dei remine. NOT Savio remine. NOT 3Wplus remine. NOT Paideia remine. NOT Ooievaarsnest remine. NOT De Zonnekindjes remine. NOT D'n Opvang remine. NOT CAR Overleie remine. NOT Gesticht remine. NOT Grauwzusters convent. NOT Hocus-Pocus remine. NOT VKA remine. NOT Soetkin remine. NOT t Sloeberke remine. NOT CAR Accent remine. NOT De Groene Verte remine. NOT De Vleugels remine. NOT De Pallieterkes remine. NOT De Medemens remine. NOT OKO & ZO remine. NOT Harlekijntjes remine. NOT Hartjes remine. NOT De Wissel remine. NOT Familia remine. NOT t Zonnetje remine. NOT Kindercentrum remine. NOT Duinhuisjes remine. NOT Helan. NOT Hebe training. NOT WZC OLVA remine. NOT De Speelboom Brussels. NOT GERUST zorgcentrale. NOT Zo Groot remine. NOT De Elfjes remine. NOT De Steijgertjes remine. NOT Vormingscentrum training. NOT Zwarte Zusters dissolved. NOT Dominiek Savio remine. NOT EVA Dilbeek remine. NOT WZC Mater Dei Heikruis remine. NOT Ferm Kinderopvang remine. NOT Molleke YE2024 remine. NOT t Sas YE2024 remine. NOT Witte Meren remine. NOT Zusterhof remine. NOT Pardoes NV bookshop.,"
f",{STAMP},{STAMP},spawned after tick2474; Hupskadee taken leftover mined city_begijnendijk CIK; Pardoes taken leftover mined city_mechelen CIK; Bambi taken leftover mined city_kalmthout CIK; Zonneschijn taken leftover mined city_dendermonde CIK; Infano taken leftover mined city_ternat CIK EVERY-10; t Sas city_denderleeuw YE2024; Molleke city_mol YE2024; KIOS Schoten no deposits; next every-10 is 2480\n"
)
if new_2474.count("\n")!=1 or new_2475.count("\n")!=1: raise SystemExit("bad rq newlines")
# verify field counts (no extra commas in unquoted fields)
import csv as _csv
from io import StringIO
for label,line in [("2474",new_2474),("2475",new_2475)]:
    n=len(next(_csv.reader(StringIO(line))))
    if n!=12: raise SystemExit(f"{label} fields {n} != 12")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2474.encode("utf-8"))
    f.write(new_2475.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2474", chk.count(b"rq_2474,"), "n2475", chk.count(b"rq_2475,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2474,2474,no,tick2474 leftover dual Hupskadee 0863.886.651 Strong native PDF (omzet70 empty VKT; 73 empty VKT; 76A empty; envelope bruto 9900 JUMP 700865; bruto JUMP 700865; pnl FLIP LOSS -78745; 9901 FLIP LOSS -81482; equity DROP 69055; assets JUMP 276216; debt JUMP 207162; FTE JUMP 14.5; kapitaalsubsidies empty; destin691 empty; 791 78745; cash DROP 15536; geldbeleggingen empty; WCO; 1 VE leftover city_begijnendijk CIK); leftover mined city_begijnendijk CIK; prior-year identical; NOT Pardoes remine; NOT Bambi remine; NOT Zonneschijn remine; NOT Infano remine; NOT Vijverbeek remine; NOT t Zonnetje remine; NOT Kindercentrum remine; NOT Duinhuisjes remine; NOT 3Wplus remine; NOT Mater Dei remine; NOT WZC Mater Dei Heikruis remine; NOT Savio remine; NOT Dominiek Savio remine; NOT EVA Dilbeek remine; NOT Paideia remine; NOT Ooievaarsnest remine; NOT DE ZONNEKINDJES remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT Grauwzusters convent; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens KDV remine; NOT De Medemens parent remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Mini-creches GO Next remine; NOT Kinderlach; NOT Zo Groot YE2024; NOT De Speelboom Brussels; NOT Elief CDN 403; NOT Villa Boempatat SCAN/CDN403; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; NOT De Bolster Zwalm not leftover mined parent; NOT GERUST zorgcentrale; NOT De Elfjes remine; NOT De Steijgertjes remine; NOT Vormingscentrum training; NOT Zwarte Zusters dissolved; NOT Ferm Kinderopvang remine; NOT Hupskadee BV 0476.248.224 private; NOT KIOS Schoten no deposits; NOT Molleke city_mol YE2024; NOT t Sas city_denderleeuw YE2024 2026-00050081; NOT Dol-Fijn Turnhout leftover-via-VE; NOT Witte Meren remine; NOT Zusterhof remine; NOT Pardoes NV bookshop; next every-10 is 2480; next rq_2475 leftover dual\n",
encoding="utf-8",
)
print("loop_state ok")

log=ROOT/"docs/doge/loop_log.md"
log_raw=log.read_bytes()
if not log_raw.endswith(b"\n"): raise SystemExit("loop_log no LF")
entry=f"""
### {STAMP} - tick 2474 - rq_2474 Kinderdagverblijf Hupskadee (bruto JUMP 701k / omzet+73 empty VKT / pnl FLIP LOSS 79k / cash DROP / destin empty / Strong PDF)

- Unit: **rq_2474** leftover dual after **Pardoes@2473**. Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024** (not re-downloaded); FARO 2026-00010398 still **YE2024** (HEAD-only policy). Discovery path: FIRST Hupskadee 0863.886.651 leftover city_begijnendijk unused — latest deposit **2026-00374083** is **YE2025** (period 01.01.2025–31.12.2025; filed 31.07.2026; AV 30.06.2026) — LOCKED (0 real entity hits; leftover of mined city_begijnendijk; official NBB broker PDF GET 200 50198 native 15p; CDN **403**). Then less-picked mined Flanders cities with 0 leftover CIK (herentals / schoten / vilvoorde / geel / mol). Kinderdagverblijf Molleke **0448.186.520** leftover city_mol still **YE2024** — skip. KIOS leftover city_schoten — no jaarrekening — skip. Dol-Fijn **0439.731.880** zetel Turnhout leftover-via-VE Herentals YE2025 — not enough. Witte Meren leftover city_mol already mined. Zusterhof leftover city_geel already mined. t Sas leftover city_denderleeuw **YE2024** **2026-00050081** — skip. Villa Boempatat leftover city_gent **YE2025** **2026-00396513** CDN **403** / SCAN — not taken. Speelhuis Elief leftover city_antwerpen unused YE2025 **2026-00374905** CDN **403** — not taken. Kinderlach leftover city_eeklo still **YE2024**. De Linde Ronse leftover city_ronse still **YE2024**. Woon en Zorg H. Hart Kortrijk leftover city_kortrijk still **YE2024**. Jessa leftover city_hasselt hospital YE2025 PDF / hospital special schema — not taken. Mini-creches GO! Next leftover city_hasselt still **YE2024**. Zo Groot Oostende leftover city_oostende still **YE2024**. Familiehulp De Speelboom YE2025 unused Brussels zetel — not taken. De Bolster 0861.680.989 YE2025 zetel Zwalm (city_zwalm not mined) — not taken. GERUST Zorgcentrale leftover city_herentals YE2025 — zorgcentrale not in dual types — not taken. Vormingscentrum leftover city_gent training — skip. Helan Kinderopvang already skipped. Zwarte Zusters dissolved — skip. Private BVs (Hupskadee BV **0476.248.224** same zetel NACE 68.203 / Ello Mechelen / Troetelland Geel / Regenboog Vilvoorde / Vlindertje Schoten) skipped. Pardoes 0417.400.205 just mined — do not remine. Bambi 0443.006.522 already mined — do not remine. Zonneschijn 0877.850.493 already mined — do not remine. Infano 0477.578.411 already mined — do not remine. Vijverbeek already mined — do not remine. Mater Dei already mined — do not remine. Savio already mined — do not remine. t Zonnetje Waregem already mined — do not remine. First leftover unused + live official YE2025 native euros: took FREE leftover Flemish **VZW KINDERDAGVERBLIJF HUPSKADEE** YE2025 (KBO **0863.886.651**; zetel Kleinesteenweg 55 3130 Begijnendijk; **Actief** **1 VE** **2.160.573.842** KINDERDAGVERBLIJF HUPSKADEE vzw since 21.03.2007; RSZ2025 **88.911**; leftover of mined **city_begijnendijk**; info@hupskadee.be; Opgroeien groepsopvang; Kind en Gezin-vergund; inkomenstarief IKT; 4 leefgroepen). Identity trap: Hupskadee 0863.886.651 ≠ Hupskadee BV **0476.248.224** private BV same zetel; ≠ Pardoes **0417.400.205** leftover city_mechelen just mined; ≠ Kinderdagverblijf Bambi **0443.006.522**; ≠ Zonneschijn **0877.850.493**; ≠ INFANO **0477.578.411**; ≠ Kinderdagverblijf Vijverbeek **0448.164.744**; ≠ t Zonnetje Waregem **0443.648.306**; ≠ DE ZONNEKINDJES **0416.541.952**; ≠ ZONNESTRAAL / Zonnestraal Junior; ≠ Kindercentrum Waregem **0408.226.775**; ≠ Duinhuisjes **0413.323.037**; ≠ Groepsopvang Mater Dei **0431.168.859**; ≠ WZC Mater Dei Heikruis; ≠ Kinderdagverblijf Savio **0472.564.501**; ≠ Dominiek Savio; ≠ EVA Dilbeek **0477.276.325**; ≠ Paideia **0445.129.931**; ≠ KDV Ooievaarsnest **0418.588.256**; ≠ D'n Opvang **0676.442.465**; ≠ CAR Overleie **0454.250.505**; ≠ Gesticht **0410.918.031**; ≠ HOCUS-POCUS **0466.893.167**; ≠ VKA **0433.480.132**; ≠ Soetkin **0443.641.970**; ≠ t Sloeberke **0410.973.360**; ≠ CAR Accent **0413.208.122**; ≠ Speelhuis Elief **0451.624.377**; ≠ Villa Boempatat **0660.616.520**; ≠ De Groene Verte **0465.061.649**; ≠ De Vleugels **0431.408.290**; ≠ De Pallieterkes **0418.538.865**; ≠ De Medemens Kinderdagverblijven **0893.678.915**; ≠ De Medemens **0428.692.191**; ≠ OKO & ZO **0862.154.608**; ≠ Harlekijntjes **0407.700.403**; ≠ Hartjes Ninove **0446.391.327**; ≠ Hartjes Tienen **0441.374.348**; ≠ De Wissel **0421.913.376**; ≠ Ferm Kinderopvang **0416.117.627**; ≠ Familia **0461.401.779**; ≠ Peutertuinen GO Mariakerke **0410.221.116**; ≠ Mini-crèches GO! Next **0896.468.060**; ≠ Kinderlach **0450.275.186**; ≠ Helan 0464.151.037; ≠ Hebe **0451.789.772**; ≠ WZC OLVA **0430.977.136**; ≠ H.Hart Kortrijk **0413.595.330**; ≠ De Linde Ronse **0778.279.401**; ≠ De Bolster **0861.680.989**; ≠ GERUST **0776.808.068**; ≠ Jessa **0821.142.117**; ≠ AZ Sint-Maria **0467.967.491**; ≠ De Elfjes **0455.636.912**; ≠ De Steijgertjes **0413.421.720**; ≠ TKDV Het Veer Kloosterstraat 6; ≠ Vormingscentrum **0413.342.338** training; ≠ Zwarte Zusters **0413.272.260** dissolved; ≠ KIOS **0882.468.881**; ≠ Molleke **0448.186.520**; ≠ t Sas **0448.731.106**; ≠ Dol-Fijn **0439.731.880**; ≠ Witte Meren **0418.234.997**; ≠ Zusterhof **0473.762.450**; ≠ Pardoes NV **0867.020.840** bookshop. 1 VE Begijnendijk — leftover of mined city_begijnendijk (zetel + Kleinesteenweg 55). Confirmed leftover public (Opgroeien CIK groepsopvang; Kind en Gezin-vergund; inkomenstarief IKT) not convent / not private clinic / not school / not OVBJ / not WZC / not VAPH / not Ferm / not Pardoes remine / not Bambi remine / not Zonneschijn remine / not Hupskadee BV private. VKT-VZW **native text** (not scan) — 50198 B / 15p all native euros (VKT-VZW 6.2 / 6.3 / 6.5 / 8 niet dienstig).
- Found: official NBB VKT-VZW native PDF deposit **2026-00374083** (50198 B / 15p; AV **30.06.2026**; header **31.07.2026**; official NBB broker UUID 98e94f9d GET **200** 50198 official NBB-generated OpenPDF 1.3.26 CreationDate 03.08.2026; CDN GET **403**; importFileType XBRL; all 15p native; prior-year identical not restated) — omzet 70 **empty** VKT; 73 **empty** VKT; 76A **empty**; envelope bruto 9900 **EUR700865** JUMP +2.75% (VKT envelope because omzet empty; was 682109); bruto 9900 **EUR700865** JUMP +2.75%; 62 **EUR773351** JUMP +17.09%; 630 **EUR8749** JUMP +130.48%; 66A **empty**; 640/8 **EUR248** DROP −91.44%; 635/9 **empty**; 631/4 **empty**; bedrijfswinst 9901 **EUR-81482** FLIP to LOSS (was 14933); pnl 9904 **EUR-78745** FLIP to LOSS (was 14802); equity **EUR69055** DROP −53.28%; assets **EUR276216** JUMP +11.06%; debt **EUR207162** JUMP +105.29%; FTE **14.5** JUMP +15.08% (was 12.6; 100 14.5; 105 16); kapitaalsubsidies **empty**; destin 691 **empty** (791 78745; 13 DROP 69055 ≈ prior 147799 − 791 78745; 1 EUR rounding); 791 **EUR78745**; cash **EUR15536** DROP −84.52%; geldbeleggingen **empty**; gebouwen **EUR1749** DROP; MVA 22/27 **EUR53543** JUMP; aanbouw **empty**; capex **EUR27180**; fondsen 10 **empty**; overgedragen 14 **empty**; bestemde fondsen 13 **EUR69055** DROP; voorzieningen 16 **empty**; FVA 28 **empty**; LT recv 29 **EUR121766** JUMP; related-party 9500 **EUR53706**; 43 **EUR37518**; WCO / gerechtelijke reorganisatie in jaarverslag. Strong KBO + Strong PDF (native all pages; not SBM table; not Companyweb euros). Site: 1 VE leftover mined city_begijnendijk CIK. NOT Pardoes remine. NOT Bambi remine. NOT Zonneschijn remine. NOT Hupskadee BV private. NOT t Sas YE2024. NOT Molleke YE2024. NOT KIOS no deposits.
- Wrote: sources (+4); budgets (+11); commitments (+1); leaderboard (+1 pi 5.30); entities (+1 vzw_hupskadee_begijnendijk); foi + draft `gap_hupskadee_opgroeien_matrix_bruto_701k_omzet73_empty_pnl_flip_loss_79k_cash_drop_destin_empty_l5`; rq_2474=done + rq_2475 open; loop_state ticks=2474; raw tick2474/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2480**). Next: rq_2475 unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Hupskadee remine / NOT Hupskadee BV private / NOT Pardoes remine / NOT Bambi remine / NOT Zonneschijn remine / NOT Infano remine / NOT Vijverbeek remine / NOT t Zonnetje remine / NOT Kindercentrum remine / NOT Duinhuisjes remine / NOT Mater Dei remine / NOT Savio remine / NOT 3Wplus remine / NOT Paideia remine / NOT Ooievaarsnest remine / NOT De Zonnekindjes remine / NOT D'n Opvang remine / NOT CAR Overleie remine / NOT Gesticht remine / NOT Grauwzusters convent / NOT HOCUS-POCUS remine / NOT VKA remine / NOT Soetkin remine / NOT t Sloeberke remine / NOT CAR Accent remine / NOT De Groene Verte remine / NOT De Vleugels remine / NOT De Pallieterkes remine / NOT De Medemens remine / NOT OKO & ZO remine / NOT Harlekijntjes remine / NOT Hartjes remine / NOT De Wissel remine / NOT Familia remine / NOT Mini-creches GO Next remine / NOT WZC OLVA remine / NOT Hebe training / NOT Quattro remine / NOT GERUST zorgcentrale / NOT Zo Groot remine / NOT De Elfjes remine / NOT De Steijgertjes remine / NOT Vormingscentrum training / NOT Zwarte Zusters dissolved / NOT Dominiek Savio remine / NOT EVA Dilbeek remine / NOT WZC Mater Dei Heikruis remine / NOT Ferm Kinderopvang remine / NOT Molleke YE2024 / NOT t Sas YE2024 / NOT Witte Meren remine / NOT Zusterhof remine / NOT Pardoes NV bookshop). NOW leftover candidates: Molleke 0448.186.520 leftover city_mol YE2024 — take ONLY if unused + official YE2025 native PDF. t Sas 0448.731.106 leftover city_denderleeuw YE2024 only 2026-00050081 — skip unless YE2025. Villa Boempatat 0660.616.520 leftover city_gent YE2025 **2026-00396513** CDN **403** / SCAN — take ONLY if unused + official native-text YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen unused YE2025 **2026-00374905** CDN **403** — take ONLY if unused + CDN 200 native YE2025 PDF. Kinderlach leftover city_eeklo still YE2024 — take ONLY if unused + official YE2025 PDF. De Linde Ronse leftover city_ronse still YE2024 — take ONLY if unused + official YE2025 PDF. H.Hart Kortrijk leftover city_kortrijk still YE2024 — take ONLY if unused + official YE2025 PDF. Jessa leftover city_hasselt hospital YE2025 PDF — take ONLY if unused + official YE2025 euros extract. De Bolster 0861.680.989 YE2025 zetel Zwalm — leftover of mined parent only. Familiehulp De Speelboom YE2025 Brussels zetel — leftover-via-VE not enough per LOOP.md. Mini-creches GO! Next leftover city_hasselt still YE2024 — skip unless YE2025. Zo Groot Oostende leftover city_oostende still YE2024 — skip unless YE2025. KIOS leftover city_schoten no deposits — skip. Dol-Fijn leftover-via-VE not enough. Tick **2480** is next every-10.

"""
with log.open("ab") as f:
    f.write(entry.encode("utf-8"))
print("loop_log ok")
print("WRITE CORE DONE")
