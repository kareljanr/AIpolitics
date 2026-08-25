from pathlib import Path
import csv
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2473_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_pardoes_jr2025_nbb_pdf_2473"
SRC_KBO="src_pardoes_kbo_2473"
SRC_SBM="src_pardoes_sbm_2473"
SRC_SITE="src_pardoes_site_2473"
EID="vzw_pardoes_mechelen"
GAP="gap_pardoes_opgroeien_matrix_opbr_2_29m_omzet_665k_73_1_62m_pnl_flip_loss_7k_destin_empty_l5"
COMM="comm_pardoes_jr2025_statutory_opbr_2_29m_omzet_665k_73_1_62m_pnl_flip_loss_7k"
LB="lb_pardoes_opbr_2_29m_omzet_665k_73_1_62m_pnl_flip_loss_7k_destin_empty_jr2025"
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
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Pardoes deposit 2026-00295237,http://cdn.staatsbladmonitor.be/2026pdf/2026-00295237.pdf,NBB official WVV deposit PDF via SBM CDN,{DAY},budget,tick2473; official native PDF 57572 bytes 16p VKT-VZW 25.0.13 m04-f; header 15.07.2026; AV 01.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-15 16:36:07 UTC OpenPDF 1.3.26; all 16p native; CDN 2026-00295237 GET 200 57572 official NBB-generated PDF Last-Modified 01.08.2026; official NBB broker UUID 3f52c368-8055-11f1-8445-8fc15c279710 HEAD 403 without SPA session; importFileType ZIP; VKT-VZW 6.1.3 6.2 6.3 6.5 6.6 7 8 niet dienstig; prior-year identical not restated; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Pardoes dienst voor onthaalouders 0417.400.205,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0417400205,KBO Public Search FOD Economie,{DAY},official_register,tick2473; Actief; 1 VE 2.232.656.423 Kinderopvangdienst Mechelen Tervuursesteenweg 48 2800 Mechelen since 01.04.2014; VZW since 07.06.1977; begindatum 07.06.1977; zetel Tervuursesteenweg 48 2800 Mechelen since 08.12.2015; toelating Kinderopvang VL since 01.04.2014; RSZ-werkgever since 01.09.1977; RSZ2025 88.911; FOI aanvraag@kinderopvangpardoes.be; leftover mined city_mechelen CIK; NOT Bambi 0443.006.522 remine; NOT Zonneschijn 0877.850.493 remine; NOT t Sas 0448.731.106 YE2024; NOT Hupskadee 0863.886.651 YE2025 unused; NOT Pardoes NV 0867.020.840 bookshop",
f"{SRC_SBM},NBB Consult / SBM fiche Pardoes 0417400205 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0417400205,NBB Consult / SBM,{DAY},official_register,tick2473; deposit-id 2026-00295237 YE 01.01.2025-31.12.2025 filing 15.07.2026 published VKT-VZW Verkort model vereniging Initial; Companyweb last-balansjaar 2025 deposit-id discovery OK euros NOT OK; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},Pardoes FOI contact leftover city_mechelen CIK,https://kinderopvangpardoes.be/,VZW Pardoes dienst voor onthaalouders leftover city_mechelen CIK Opgroeien gezinsopvang 1 VE,{DAY},foi_contact,tick2473; FOI aanvraag@kinderopvangpardoes.be; zetel Tervuursesteenweg 48 2800 Mechelen; 1 VE leftover mined city_mechelen after t Sas YE2024 skip; Opgroeien gezinsopvang / onthaalouders; Kind en Gezin-vergund; NOT Bambi remine; NOT Zonneschijn remine; NOT Infano remine; NOT Vijverbeek remine; NOT t Zonnetje remine; NOT Kindercentrum remine; NOT Duinhuisjes remine; NOT Mater Dei remine; NOT Savio remine; NOT Paideia remine; NOT Ooievaarsnest remine; NOT DE ZONNEKINDJES remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Kinderlach YE2024; NOT Helan; NOT De Speelboom Brussels; NOT Villa Boempatat SCAN/CDN403; NOT Elief CDN 403; NOT Hebe training; NOT Zo Groot YE2024; NOT De Bolster Zwalm not leftover mined parent; NOT GERUST zorgcentrale; NOT Vormingscentrum training; NOT Zwarte Zusters dissolved; NOT Hupskadee leftover city_begijnendijk YE2025 unused 2026-00374083; NOT KIOS Schoten no deposits; NOT Molleke city_mol YE2024; NOT t Sas city_denderleeuw YE2024 2026-00050081; NOT Dol-Fijn Turnhout leftover-via-VE; NOT Pardoes NV bookshop",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},Pardoes dienst voor onthaalouders,ASBL Pardoes service d'accueillantes,Pardoes VZW (leftover city_mechelen CIK onthaalouders),parastatal,city_mechelen,nl,https://kinderopvangpardoes.be/,aanvraag@kinderopvangpardoes.be,Tervuursesteenweg 48 2800 Mechelen,tick2473 YE2025 Strong official native NBB PDF deposit 2026-00295237 + Strong KBO 0417.400.205 Actief 1 VE 2.232.656.423; omzet70 DROP 664999 commercial-only vs large 73; 73 JUMP 1618539; 76A JUMP 9397; envelope 70/76A JUMP 2292935; bruto JUMP 1269497; pnl FLIP LOSS -7367; 9901 FLIP LOSS -13292; equity DROP 1094620; assets DROP 1388126; debt JUMP 293506; FTE JUMP 28.2; kapitaalsubsidies empty; destin691 empty; 791 15000 FLAT; cash DROP 427595; geldbeleggingen JUMP 646644; leftover city_mechelen CIK 1 VE; NOT Bambi Kalmthout 0443.006.522 remine; NOT Zonneschijn Dendermonde 0877.850.493 remine; NOT Infano Ternat 0477.578.411 remine; NOT Vijverbeek Asse 0448.164.744 remine; NOT t Zonnetje Waregem 0443.648.306 remine; NOT Kindercentrum Waregem 0408.226.775 remine; NOT Duinhuisjes 0413.323.037 remine; NOT 3Wplus Kinderopvang Asse 0893.870.539 remine; NOT Mater Dei 0431.168.859 remine; NOT WZC Mater Dei Heikruis remine; NOT Savio Dilbeek 0472.564.501 remine; NOT Dominiek Savio remine; NOT EVA Dilbeek 0477.276.325 remine; NOT Paideia 0445.129.931 remine; NOT Ooievaarsnest 0418.588.256 remine; NOT DE ZONNEKINDJES 0416.541.952 remine; NOT D'n Opvang 0676.442.465 remine; NOT CAR Overleie 0454.250.505 remine; NOT Gesticht 0410.918.031 remine; NOT HOCUS-POCUS 0466.893.167 remine; NOT VKA 0433.480.132 remine; NOT Soetkin 0443.641.970 remine; NOT t Sloeberke 0410.973.360 remine; NOT CAR Accent 0413.208.122 remine; NOT De Elfjes 0455.636.912 remine; NOT De Steijgertjes 0413.421.720 remine; NOT H.Hart WZC 0413.595.330; NOT Zo Groot 0818.420.771 leftover city_oostende YE2024; NOT De Groene Verte 0465.061.649 remine; NOT De Vleugels 0431.408.290 remine; NOT De Pallieterkes 0418.538.865 remine; NOT De Medemens KDV 0893.678.915 remine; NOT De Medemens parent 0428.692.191 remine; NOT OKO & ZO 0862.154.608 remine; NOT Harlekijntjes 0407.700.403 remine; NOT Hartjes Ninove 0446.391.327 remine; NOT Hartjes Tienen 0441.374.348 remine; NOT De Wissel 0421.913.376 remine; NOT Familia 0461.401.779; NOT Peutertuinen GO Mariakerke 0410.221.116; NOT Mini-creches GO Next 0896.468.060 leftover city_hasselt YE2024; NOT Kinderlach 0450.275.186; NOT Helan; NOT De Speelboom Brussels; NOT Villa Boempatat 0660.616.520 leftover city_gent YE2025 SCAN/CDN403 2026-00396513; NOT Elief 0451.624.377 CDN 403; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; NOT De Bolster 0861.680.989 YE2025 zetel Zwalm city_zwalm not mined; NOT GERUST 0776.808.068 zorgcentrale; NOT Jessa hospital special schema; NOT Vormingscentrum 0413.342.338 training; NOT Zwarte Zusters 0413.272.260 dissolved; NOT Ferm Kinderopvang 0416.117.627 remine; NOT ZONNESTRAAL; NOT Molleke 0448.186.520 leftover city_mol YE2024; NOT t Sas 0448.731.106 leftover city_denderleeuw YE2024 2026-00050081; NOT Dol-Fijn 0439.731.880 Turnhout zetel leftover-via-VE; NOT Hupskadee 0863.886.651 leftover city_begijnendijk YE2025 unused 2026-00374083; NOT KIOS 0882.468.881 leftover city_schoten no deposits; NOT Pardoes NV 0867.020.840 bookshop; NOT Witte Meren remine; NOT Zusterhof remine; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria SCAN; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Zo Groot Oostende YE2024 not taken; H.Hart Kortrijk YE2024 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_pardoes_omzet_jr2025_statutory,{EID},2025,664999,664999,664999,NBB VKT-VZW code 70 omzet YE2025 DROP -5.75% (commercial-only vs large 73),{SRC_PDF},strong,tick2473; PDF p6 native; YE2024 705573; 73 1618539; 76A 9397",
f"bud_pardoes_73_jr2025_statutory,{EID},2025,1618539,1618539,1618539,NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP +3.72%,{SRC_PDF},strong,tick2473; PDF p6 native; YE2024 1560550; FOI Opgroeien matrix behind envelope 2292935",
f"bud_pardoes_opbr_jr2025_statutory,{EID},2025,2292935,2292935,2292935,NBB VKT-VZW envelope 70/76A YE2025 JUMP +1.15% (VZW omzet commercial-only vs large 73; 70+73+76A disclosed),{SRC_PDF},strong,tick2473; PDF p6 native; YE2024 2266864; 70 664999; 73 1618539; 76A 9397; 72/74 not separately disclosed on VKT",
f"bud_pardoes_bruto_jr2025_statutory,{EID},2025,1269497,1269497,1269497,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +5.11%,{SRC_PDF},strong,tick2473; PDF p6 native; YE2024 1207782; envelope is 70/76A not bruto because omzet not empty",
f"bud_pardoes_pnl_jr2025_statutory,{EID},2025,-7367,-7367,-7367,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 FLIP to LOSS (was 97684),{SRC_PDF},strong,tick2473; PDF p6 native; YE2024 97684; bedrijfswinst 9901 -13292 FLIP; destin691 empty",
f"bud_pardoes_bedrijfswinst_jr2025_statutory,{EID},2025,-13292,-13292,-13292,NBB VKT-VZW code 9901 bedrijfswinst YE2025 FLIP to LOSS (was 96634),{SRC_PDF},strong,tick2473; PDF p6 native; YE2024 96634; 62 1236380 JUMP; 630 36143 DROP; 66A 1197; 640/8 9622 DROP; 635/9 empty; 631/4 -553",
f"bud_pardoes_equity_jr2025_statutory,{EID},2025,1094620,1094620,1094620,NBB VKT-VZW code 10/15 eigen vermogen YE2025 DROP -0.67%,{SRC_PDF},strong,tick2473; PDF p5 native; YE2024 1101987; kapitaalsubsidies empty; overgedragen 14 510512 JUMP; fondsen 10 empty; bestemde fondsen 13 584108 DROP",
f"bud_pardoes_assets_jr2025_statutory,{EID},2025,1388126,1388126,1388126,NBB VKT-VZW code 20/58 totaal activa YE2025 DROP -0.16%,{SRC_PDF},strong,tick2473; PDF p4 native; YE2024 1390349; MVA 22/27 208389 DROP; cash 427595 DROP; geldbeleggingen 646644 JUMP; aanbouw 27 empty; FVA 28 empty; LT recv 29 empty",
f"bud_pardoes_debt_jr2025_statutory,{EID},2025,293506,293506,293506,NBB VKT-VZW code 17/49 schulden YE2025 JUMP +1.78%,{SRC_PDF},strong,tick2473; PDF p5 native; YE2024 288362; 17 empty; 42/48 282297 JUMP",
f"bud_pardoes_cash_jr2025_statutory,{EID},2025,427595,427595,427595,NBB VKT-VZW code 54/58 liquide middelen YE2025 DROP -21.86%,{SRC_PDF},strong,tick2473; PDF p4 native; YE2024 547186; geldbeleggingen 50/53 646644 JUMP; capex 20675 gebouwen DROP 185733",
f"bud_pardoes_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty (791 15000 FLAT; 14 JUMP 510512 = prior 502879 + pnl -7367 + 791 15000),{SRC_PDF},strong,tick2473; PDF p7 native; YE2024 destin 53824; bestemde fondsen 13 DROP 584108 FOI",
])
print("entities+budgets ok")

cash_json=(
"\"{\"\"2025_omzet\"\":664999,\"\"2025_73\"\":1618539,\"\"2025_76A\"\":9397,"
"\"\"2025_opbr70_76A\"\":2292935,\"\"2025_bruto\"\":1269497,"
"\"\"2025_pnl\"\":-7367,\"\"2025_bedrijfswinst\"\":-13292,"
"\"\"2025_equity\"\":1094620,\"\"2025_assets\"\":1388126,\"\"2025_debt\"\":293506,"
"\"\"2025_fte\"\":28.2,\"\"2025_kapitaalsubsidies\"\":0,\"\"2025_destin691\"\":0,"
"\"\"2025_791\"\":15000,\"\"2025_cash\"\":427595,\"\"2025_geldbeleggingen\"\":646644,"
"\"\"2025_personnel62\"\":1236380,\"\"2025_gebouwen22\"\":185733,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":1197,"
"\"\"2025_fondsen10\"\":0,\"\"2025_overgedragen14\"\":510512,"
"\"\"2025_bestemdefondsen13\"\":584108,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":36143,\"\"2025_capex\"\":20675,"
"\"\"2024_omzet\"\":705573,\"\"2024_73\"\":1560550,"
"\"\"2024_opbr70_76A\"\":2266864,\"\"2024_bruto\"\":1207782,\"\"2024_pnl\"\":97684,\"\"2024_bedrijfswinst\"\":96634,"
"\"\"2024_equity\"\":1101987,\"\"2024_assets\"\":1390349,"
"\"\"2024_debt\"\":288362,\"\"2024_cash\"\":547186,\"\"2024_fte\"\":24.6,"
"\"\"2024_destin691\"\":53824,\"\"2024_kapitaalsubsidies\"\":0,\"\"2024_76A\"\":741,"
"\"\"2024_geldbeleggingen\"\":451839}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Pardoes YE2025 (opbr 70/76A JUMP 2.29m / omzet 665k commercial-only / 73 JUMP 1.62m / pnl FLIP LOSS 7.4k / destin empty / Strong PDF),{EID},Opgroeien + leftover city_mechelen CIK,VZW Pardoes dienst voor onthaalouders (KBO 0417.400.205; Actief; 1 VE; zetel Mechelen),2026-06-01,2025,2025,2292935,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00295237.pdf,Public CIK dual of mined city_mechelen,Publish Opgroeien matrix behind envelope 2.29m + why omzet 665k commercial-only vs 73 1.62m and why pnl FLIP LOSS -7367 while destin empty and cash DROP 427595,{SRC_PDF},strong,Vlaanderen>Antwerpen>Mechelen>Pardoes>JR2025_statutory_L5,tick2473; Strong official native PDF; leftover mined city_mechelen CIK; 1 VE; prior-year identical; NOT every-10; NOT Bambi remine; NOT Zonneschijn remine; NOT Infano remine; NOT t Sas YE2024; NOT Kinderlach YE2024; NOT Zo Groot YE2024; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"Pardoes opbr 70/76A JUMP 2.29m / omzet 665k commercial-only / 73 JUMP 1.62m / pnl FLIP LOSS 7.4k / destin empty (YE2025 leftover city_mechelen CIK)",
"L5",
"cik_vzw_statutory",
"Vlaanderen>Antwerpen>Mechelen>Pardoes>JR2025",
"2292935",
"2292935",
"PDF envelope 2292935 = 70+73+76A because VZW omzet commercial-only vs large 73; 70 664999; 73 1618539; 76A 9397; bruto 1269497; bedrijfswinst FLIP LOSS -13292; pnl FLIP LOSS -7367; equity DROP 1094620; assets DROP 1388126; debt JUMP 293506; FTE 28.2; kapitaalsubsidies empty; destin691 empty; cash DROP 427595; leftover city_mechelen CIK",
"strong",
SRC_PDF,
"Opgroeien + leftover city_mechelen CIK",
"CIK / Kind en Gezin gezinsopvang onthaalouders leftover city_mechelen",
"2.29m envelope; omzet 665k commercial-only vs 73 1.62m; pnl FLIP LOSS -7367; cash DROP 427595; destin empty; leftover city_mechelen CIK",
"5.35",
"5.20",
"5.10",
"5.24",
"FOI Opgroeien matrix behind envelope 2.29m + why omzet 665k commercial-only vs 73 1.62m and why pnl FLIP LOSS -7367 while destin empty and cash DROP 427595",
"active",
"",
"tick2473 leftover mined city_mechelen CIK after t Sas YE2024 skip; 1 VE; prior-year identical; NOT every-10; NOT Bambi remine; NOT Zonneschijn remine; NOT Infano remine; NOT Vijverbeek remine; NOT t Zonnetje remine; NOT Kindercentrum remine; NOT Duinhuisjes remine; NOT Mater Dei remine; NOT Savio remine; NOT Kinderlach YE2024; NOT Zo Groot YE2024; NOT Elief CDN 403; NOT Villa Boempatat SCAN/CDN403; NOT De Speelboom Brussels; NOT Hupskadee leftover city_begijnendijk YE2025 unused 2026-00374083; NOT KIOS Schoten no deposits; NOT Molleke city_mol YE2024; NOT t Sas city_denderleeuw YE2024 2026-00050081",
])
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>Antwerpen>Mechelen>Pardoes>CIK",
"entity_id": EID,
"what_is_missing": "Opgroeien split behind envelope 2292935 (omzet 70 664999 commercial-only + 73 1618539 + 76A 9397) and why destin empty while pnl FLIP LOSS -7367 and cash DROP 427595 and 62 JUMP 1236380 FTE JUMP 28.2",
"why_it_matters": "Strong official PDF leftover public CIK of mined city_mechelen; VZW envelope 70/76A 2.29m because omzet commercial-only vs large 73; public Opgroeien gezinsopvang 1 VE Tervuursesteenweg 48 Mechelen",
"priority": "8",
"recipient_body": "VZW Pardoes dienst voor onthaalouders / Raad van Bestuur",
"recipient_email": "aanvraag@kinderopvangpardoes.be",
"recipient_postal": "Tervuursesteenweg 48 2800 Mechelen",
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
"notes": "tick2473; ready NOT sent; Strong official native NBB PDF; leftover mined city_mechelen CIK after t Sas YE2024 skip; 1 VE; prior-year identical; NOT every-10; off Bambi remine; off Zonneschijn remine; off t Sas YE2024; off Hupskadee YE2025 unused",
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
if rq_raw.count(b"rq_2473,")!=1: raise SystemExit(f"bad 2473 count {rq_raw.count(b'rq_2473,')}")
if b"rq_2474," in rq_raw: raise SystemExit("2474 exists")
idx=rq_raw.rfind(b"rq_2473,")
if idx<0: raise SystemExit("rq_2473 not found")
new_2473=(
"rq_2473,leftover dual Pardoes YE2025,hole_fill,8,done,L5,vzw_pardoes_mechelen,"
"Took unused leftover public CIK Pardoes 0417.400.205 leftover mined city_mechelen. Official NBB VKT-VZW YE2025 2026-00295237 native 16p. Envelope 70/76A JUMP 2292935 (omzet 664999 commercial-only vs 73 1618539); pnl FLIP LOSS -7367; cash DROP 427595; destin empty; FTE 28.2. NOT Bambi remine. NOT Zonneschijn remine. NOT t Sas YE2024. NOT Hupskadee YE2025 unused.,"
f",{STAMP},{STAMP},tick2473 leftover mined city_mechelen CIK; Strong native PDF; 1 VE; prior-year identical; next every-10 is 2480\n"
)
new_2474=(
"rq_2474,leftover dual after Pardoes — hunt unused public dual,hole_fill,8,open,L5,,"
"After Pardoes YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf. Hupskadee 0863.886.651 leftover city_begijnendijk now YE2025 2026-00374083 unused — take ONLY if unused + official YE2025 native PDF. Molleke 0448.186.520 leftover city_mol YE2024 (2025-00170508) — take ONLY if unused + official YE2025 native PDF. t Sas 0448.731.106 leftover city_denderleeuw YE2024 only 2026-00050081 — skip unless YE2025. Villa Boempatat 0660.616.520 leftover city_gent YE2025 2026-00396513 CDN 403 / SCAN — take ONLY if unused + official native-text YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen YE2025 2026-00374905 CDN 403 — take ONLY if CDN 200 native. Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO! Next / Zo Groot Oostende still YE2024 — take ONLY if unused + official YE2025 PDF. De Bolster 0861.680.989 YE2025 2026-00210039 zetel Zwalm (city_zwalm not mined) — take ONLY if leftover of a mined parent. Jessa leftover city_hasselt hospital YE2025 PDF — take ONLY if unused + official YE2025 euros extract. KIOS 0882.468.881 leftover city_schoten — no jaarrekening skip unless deposits appear. Dol-Fijn 0439.731.880 zetel Turnhout leftover-via-VE Herentals — not enough. NOT Pardoes remine. NOT Bambi remine. NOT Zonneschijn remine. NOT Infano remine. NOT Vijverbeek remine. NOT Mater Dei remine. NOT Savio remine. NOT 3Wplus remine. NOT Paideia remine. NOT Ooievaarsnest remine. NOT De Zonnekindjes remine. NOT D'n Opvang remine. NOT CAR Overleie remine. NOT Gesticht remine. NOT Grauwzusters convent. NOT Hocus-Pocus remine. NOT VKA remine. NOT Soetkin remine. NOT t Sloeberke remine. NOT CAR Accent remine. NOT De Groene Verte remine. NOT De Vleugels remine. NOT De Pallieterkes remine. NOT De Medemens remine. NOT OKO & ZO remine. NOT Harlekijntjes remine. NOT Hartjes remine. NOT De Wissel remine. NOT Familia remine. NOT t Zonnetje remine. NOT Kindercentrum remine. NOT Duinhuisjes remine. NOT Helan. NOT Hebe training. NOT WZC OLVA remine. NOT De Speelboom Brussels. NOT GERUST zorgcentrale. NOT Zo Groot remine. NOT De Elfjes remine. NOT De Steijgertjes remine. NOT Vormingscentrum training. NOT Zwarte Zusters dissolved. NOT Dominiek Savio remine. NOT EVA Dilbeek remine. NOT WZC Mater Dei Heikruis remine. NOT Ferm Kinderopvang remine. NOT Molleke YE2024 remine. NOT t Sas YE2024 remine. NOT Witte Meren remine. NOT Zusterhof remine. NOT Pardoes NV bookshop.,"
f",{STAMP},{STAMP},spawned after tick2473; Pardoes taken leftover mined city_mechelen CIK; Bambi taken leftover mined city_kalmthout CIK; Zonneschijn taken leftover mined city_dendermonde CIK; Infano taken leftover mined city_ternat CIK EVERY-10; Hupskadee city_begijnendijk YE2025 unused; t Sas city_denderleeuw YE2024; Molleke city_mol YE2024; KIOS Schoten no deposits; next every-10 is 2480\n"
)
if new_2473.count("\n")!=1 or new_2474.count("\n")!=1: raise SystemExit("bad rq newlines")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2473.encode("utf-8"))
    f.write(new_2474.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2473", chk.count(b"rq_2473,"), "n2474", chk.count(b"rq_2474,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2473,2473,no,tick2473 leftover dual Pardoes 0417.400.205 Strong native PDF (omzet70 DROP 664999 commercial-only vs large 73; 73 JUMP 1618539; 76A JUMP 9397; envelope 70/76A JUMP 2292935; bruto JUMP 1269497; pnl FLIP LOSS -7367; 9901 FLIP LOSS -13292; equity DROP 1094620; assets DROP 1388126; debt JUMP 293506; FTE JUMP 28.2; kapitaalsubsidies empty; destin691 empty; 791 15000 FLAT; cash DROP 427595; geldbeleggingen JUMP 646644; 1 VE leftover city_mechelen CIK); leftover mined city_mechelen CIK; prior-year identical; NOT Bambi remine; NOT Zonneschijn remine; NOT Infano remine; NOT Vijverbeek remine; NOT t Zonnetje remine; NOT Kindercentrum remine; NOT Duinhuisjes remine; NOT 3Wplus remine; NOT Mater Dei remine; NOT WZC Mater Dei Heikruis remine; NOT Savio remine; NOT Dominiek Savio remine; NOT EVA Dilbeek remine; NOT Paideia remine; NOT Ooievaarsnest remine; NOT DE ZONNEKINDJES remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT Grauwzusters convent; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens KDV remine; NOT De Medemens parent remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Mini-creches GO Next remine; NOT Kinderlach; NOT Zo Groot YE2024; NOT De Speelboom Brussels; NOT Elief CDN 403; NOT Villa Boempatat SCAN/CDN403; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; NOT De Bolster Zwalm not leftover mined parent; NOT GERUST zorgcentrale; NOT De Elfjes remine; NOT De Steijgertjes remine; NOT Vormingscentrum training; NOT Zwarte Zusters dissolved; NOT Ferm Kinderopvang remine; NOT Hupskadee leftover city_begijnendijk YE2025 unused 2026-00374083; NOT KIOS Schoten no deposits; NOT Molleke city_mol YE2024; NOT t Sas city_denderleeuw YE2024 2026-00050081; NOT Dol-Fijn Turnhout leftover-via-VE; NOT Witte Meren remine; NOT Zusterhof remine; NOT Pardoes NV bookshop; next every-10 is 2480; next rq_2474 leftover dual\n",
encoding="utf-8",
)
print("loop_state ok")

log=ROOT/"docs/doge/loop_log.md"
log_raw=log.read_bytes()
if not log_raw.endswith(b"\n"): raise SystemExit("loop_log no LF")
entry=f"""
### {STAMP} - tick 2473 - rq_2473 Pardoes (opbr 70/76A JUMP 2.29m / omzet 665k commercial-only / 73 JUMP 1.62m / pnl FLIP LOSS 7.4k / destin empty / Strong PDF)

- Unit: **rq_2473** leftover dual after **Bambi@2472**. Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024** (not re-downloaded); FARO 2026-00010398 still **YE2024** (HEAD-only policy). Discovery path: FIRST t Sas 0448.731.106 leftover city_denderleeuw unused — latest deposit **2026-00050081** is **YE2024** (periodEnd 31.12.2024; filed 03.03.2026) — skip. Then less-picked mined Flanders cities with 0 leftover CIK (mechelen / herentals / schoten / vilvoorde / geel / mol). Kinderdagverblijf Molleke **0448.186.520** leftover city_mol still **YE2024** 2025-00170508 — skip. KIOS leftover city_schoten — no jaarrekening — skip. Dol-Fijn **0439.731.880** zetel Turnhout leftover-via-VE Herentals YE2025 — not enough. Witte Meren leftover city_mol already mined tick1732. Zusterhof leftover city_geel already mined tick1747. Hupskadee leftover city_begijnendijk now **YE2025** **2026-00374083** unused — not taken (Pardoes locked first). Villa Boempatat leftover city_gent **YE2025** **2026-00396513** CDN **403** / SCAN — not taken. Speelhuis Elief leftover city_antwerpen unused YE2025 **2026-00374905** CDN **403** — not taken. Kinderlach leftover city_eeklo still **YE2024**. De Linde Ronse leftover city_ronse still **YE2024**. Woon en Zorg H. Hart Kortrijk leftover city_kortrijk still **YE2024**. Jessa leftover city_hasselt hospital YE2025 PDF / hospital special schema — not taken. Mini-creches GO! Next leftover city_hasselt still **YE2024**. Zo Groot Oostende leftover city_oostende still **YE2024**. Familiehulp De Speelboom YE2025 unused Brussels zetel — not taken. De Bolster 0861.680.989 YE2025 zetel Zwalm (city_zwalm not mined) — not taken. GERUST Zorgcentrale leftover city_herentals YE2025 — zorgcentrale not in dual types — not taken. Vormingscentrum leftover city_gent training — skip. Helan Kinderopvang already skipped. Zwarte Zusters dissolved — skip. Private BVs (Ello Mechelen / Troetelland Geel / Regenboog Vilvoorde / Vlindertje Schoten) skipped. Bambi 0443.006.522 just mined — do not remine. Zonneschijn 0877.850.493 already mined — do not remine. Infano 0477.578.411 already mined — do not remine. Vijverbeek already mined — do not remine. Mater Dei already mined — do not remine. Savio already mined — do not remine. t Zonnetje Waregem already mined — do not remine. First leftover unused + live official YE2025 native euros: took FREE leftover Flemish **VZW Pardoes dienst voor onthaalouders** YE2025 (KBO **0417.400.205**; zetel Tervuursesteenweg 48 2800 Mechelen; **Actief** **1 VE** **2.232.656.423** Kinderopvangdienst Mechelen since 01.04.2014; RSZ2025 **88.911**; leftover of mined **city_mechelen**; aanvraag@kinderopvangpardoes.be; Opgroeien gezinsopvang / onthaalouders; Kind en Gezin-vergund). Identity trap: Pardoes 0417.400.205 ≠ Kinderdagverblijf Bambi **0443.006.522** leftover city_kalmthout just mined; ≠ Zonneschijn **0877.850.493** leftover city_dendermonde; ≠ INFANO **0477.578.411**; ≠ Kinderdagverblijf Vijverbeek **0448.164.744**; ≠ t Zonnetje Waregem **0443.648.306**; ≠ DE ZONNEKINDJES **0416.541.952**; ≠ ZONNESTRAAL / Zonnestraal Junior; ≠ Kindercentrum Waregem **0408.226.775**; ≠ Duinhuisjes **0413.323.037**; ≠ Groepsopvang Mater Dei **0431.168.859**; ≠ WZC Mater Dei Heikruis; ≠ Kinderdagverblijf Savio **0472.564.501**; ≠ Dominiek Savio; ≠ EVA Dilbeek **0477.276.325**; ≠ Paideia **0445.129.931**; ≠ KDV Ooievaarsnest **0418.588.256**; ≠ D'n Opvang **0676.442.465**; ≠ CAR Overleie **0454.250.505**; ≠ Gesticht **0410.918.031**; ≠ HOCUS-POCUS **0466.893.167**; ≠ VKA **0433.480.132**; ≠ Soetkin **0443.641.970**; ≠ t Sloeberke **0410.973.360**; ≠ CAR Accent **0413.208.122**; ≠ Speelhuis Elief **0451.624.377**; ≠ Villa Boempatat **0660.616.520**; ≠ De Groene Verte **0465.061.649**; ≠ De Vleugels **0431.408.290**; ≠ De Pallieterkes **0418.538.865**; ≠ De Medemens Kinderdagverblijven **0893.678.915**; ≠ De Medemens **0428.692.191**; ≠ OKO & ZO **0862.154.608**; ≠ Harlekijntjes **0407.700.403**; ≠ Hartjes Ninove **0446.391.327**; ≠ Hartjes Tienen **0441.374.348**; ≠ De Wissel **0421.913.376**; ≠ Ferm Kinderopvang **0416.117.627**; ≠ Familia **0461.401.779**; ≠ Peutertuinen GO Mariakerke **0410.221.116**; ≠ Mini-crèches GO! Next **0896.468.060**; ≠ Kinderlach **0450.275.186**; ≠ Helan 0464.151.037; ≠ Hebe **0451.789.772**; ≠ WZC OLVA **0430.977.136**; ≠ H.Hart Kortrijk **0413.595.330**; ≠ De Linde Ronse **0778.279.401**; ≠ De Bolster **0861.680.989**; ≠ GERUST **0776.808.068**; ≠ Jessa **0821.142.117**; ≠ AZ Sint-Maria **0467.967.491**; ≠ De Elfjes **0455.636.912**; ≠ De Steijgertjes **0413.421.720**; ≠ TKDV Het Veer Kloosterstraat 6; ≠ Vormingscentrum **0413.342.338** training; ≠ Zwarte Zusters **0413.272.260** dissolved; ≠ Hupskadee **0863.886.651**; ≠ KIOS **0882.468.881**; ≠ Molleke **0448.186.520**; ≠ t Sas **0448.731.106**; ≠ Dol-Fijn **0439.731.880**; ≠ Witte Meren **0418.234.997**; ≠ Zusterhof **0473.762.450**; ≠ Pardoes NV **0867.020.840** bookshop. 1 VE Mechelen — leftover of mined city_mechelen (zetel + Tervuursesteenweg 48). Confirmed leftover public (Opgroeien CIK gezinsopvang / onthaalouders; Kind en Gezin-vergund) not convent / not private clinic / not school / not OVBJ / not WZC / not VAPH / not Ferm / not Bambi remine / not Zonneschijn remine / not t Sas YE2024. VKT-VZW **native text** (not scan) — 57572 B / 16p all native euros (VKT-VZW 6.1.3 / 6.2 / 6.3 / 6.5 / 6.6 / 7 / 8 niet dienstig).
- Found: official NBB VKT-VZW native PDF deposit **2026-00295237** (57572 B / 16p; AV **01.06.2026**; header **15.07.2026**; CDN GET **200** 57572 official NBB-generated OpenPDF 1.3.26 Last-Modified 01.08.2026; official NBB broker UUID 3f52c368 HEAD **403** without SPA session; CreationDate 15.07.2026; all 16p native; prior-year identical not restated) — omzet 70 **EUR664999** DROP −5.75% (commercial-only vs large 73; was 705573); 73 **EUR1618539** JUMP +3.72% (was 1560550); 76A **EUR9397** JUMP +1168.15% (was 741); envelope 70/76A **EUR2292935** JUMP +1.15% (70+73+76A disclosed; was 2266864); bruto 9900 **EUR1269497** JUMP +5.11% (was 1207782); 62 **EUR1236380** JUMP +16.77%; 630 **EUR36143** DROP −2.84%; 66A **EUR1197**; 640/8 **EUR9622** DROP; 635/9 **empty**; 631/4 **EUR-553**; bedrijfswinst 9901 **EUR-13292** FLIP to LOSS (was 96634); pnl 9904 **EUR-7367** FLIP to LOSS (was 97684); equity **EUR1094620** DROP −0.67%; assets **EUR1388126** DROP −0.16%; debt **EUR293506** JUMP +1.78%; FTE **28.2** JUMP +14.63% (was 24.6; 100 28.2; 105 28.6); kapitaalsubsidies **empty**; destin 691 **empty** (791 15000 FLAT; 14 JUMP 510512 = prior 502879 + pnl −7367 + 791 15000); 791 **EUR15000** FLAT; cash **EUR427595** DROP −21.86%; geldbeleggingen **EUR646644** JUMP +43.11%; gebouwen **EUR185733** DROP; MVA 22/27 **EUR208389** DROP; aanbouw **empty**; capex **EUR20675**; fondsen 10 **empty**; overgedragen 14 **EUR510512** JUMP; bestemde fondsen 13 **EUR584108** DROP; voorzieningen 16 **empty**; FVA 28 **empty**; LT recv 29 **empty**. Strong KBO + Strong PDF (native all pages; not SBM table; not Companyweb euros). Site: 1 VE leftover mined city_mechelen CIK. NOT Bambi remine. NOT Zonneschijn remine. NOT t Sas YE2024. NOT Hupskadee YE2025 unused. NOT Molleke YE2024. NOT KIOS no deposits.
- Wrote: sources (+4); budgets (+11); commitments (+1); leaderboard (+1 pi 5.24); entities (+1 vzw_pardoes_mechelen); foi + draft `gap_pardoes_opgroeien_matrix_opbr_2_29m_omzet_665k_73_1_62m_pnl_flip_loss_7k_destin_empty_l5`; rq_2473=done + rq_2474 open; loop_state ticks=2473; raw tick2473/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2480**). Next: rq_2474 unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Pardoes remine / NOT Bambi remine / NOT Zonneschijn remine / NOT Infano remine / NOT Vijverbeek remine / NOT t Zonnetje remine / NOT Kindercentrum remine / NOT Duinhuisjes remine / NOT Mater Dei remine / NOT Savio remine / NOT 3Wplus remine / NOT Paideia remine / NOT Ooievaarsnest remine / NOT De Zonnekindjes remine / NOT D'n Opvang remine / NOT CAR Overleie remine / NOT Gesticht remine / NOT Grauwzusters convent / NOT HOCUS-POCUS remine / NOT VKA remine / NOT Soetkin remine / NOT t Sloeberke remine / NOT CAR Accent remine / NOT De Groene Verte remine / NOT De Vleugels remine / NOT De Pallieterkes remine / NOT De Medemens remine / NOT OKO & ZO remine / NOT Harlekijntjes remine / NOT Hartjes remine / NOT De Wissel remine / NOT Familia remine / NOT Mini-creches GO Next remine / NOT WZC OLVA remine / NOT Hebe training / NOT Quattro remine / NOT GERUST zorgcentrale / NOT Zo Groot remine / NOT De Elfjes remine / NOT De Steijgertjes remine / NOT Vormingscentrum training / NOT Zwarte Zusters dissolved / NOT Dominiek Savio remine / NOT EVA Dilbeek remine / NOT WZC Mater Dei Heikruis remine / NOT Ferm Kinderopvang remine / NOT Molleke YE2024 / NOT t Sas YE2024 / NOT Witte Meren remine / NOT Zusterhof remine / NOT Pardoes NV bookshop). NOW leftover candidate: Hupskadee 0863.886.651 leftover city_begijnendijk YE2025 **2026-00374083** unused — take ONLY if unused + official YE2025 native PDF. Molleke 0448.186.520 leftover city_mol YE2024 — take ONLY if unused + official YE2025 native PDF. t Sas 0448.731.106 leftover city_denderleeuw YE2024 only 2026-00050081 — skip unless YE2025. Villa Boempatat 0660.616.520 leftover city_gent YE2025 **2026-00396513** CDN **403** / SCAN — take ONLY if unused + official native-text YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen unused YE2025 **2026-00374905** CDN **403** — take ONLY if unused + CDN 200 native YE2025 PDF. Kinderlach leftover city_eeklo still YE2024 — take ONLY if unused + official YE2025 PDF. De Linde Ronse leftover city_ronse still YE2024 — take ONLY if unused + official YE2025 PDF. H.Hart Kortrijk leftover city_kortrijk still YE2024 — take ONLY if unused + official YE2025 PDF. Jessa leftover city_hasselt hospital YE2025 PDF — take ONLY if unused + official YE2025 euros extract. De Bolster 0861.680.989 YE2025 zetel Zwalm — leftover of mined parent only. Familiehulp De Speelboom YE2025 Brussels zetel — leftover-via-VE not enough per LOOP.md. Mini-creches GO! Next leftover city_hasselt still YE2024 — skip unless YE2025. Zo Groot Oostende leftover city_oostende still YE2024 — skip unless YE2025. KIOS leftover city_schoten no deposits — skip. Dol-Fijn leftover-via-VE not enough. Tick **2480** is next every-10.

"""
with log.open("ab") as f:
    f.write(entry.encode("utf-8"))
print("loop_log ok")
print("WRITE CORE DONE")
