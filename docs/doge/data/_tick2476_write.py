from pathlib import Path
import csv
from io import StringIO
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2476_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_bremdael_jr2025_nbb_pdf_2476"
SRC_KBO="src_bremdael_kbo_2476"
SRC_SBM="src_bremdael_sbm_2476"
SRC_SITE="src_bremdael_site_2476"
EID="vzw_bremdael_herentals"
GAP="gap_bremdael_wzc_matrix_bruto_4_56m_omzet73_empty_pnl_flip_loss_147k_equity_neg_754k_cash_jump_l5"
COMM="comm_bremdael_jr2025_statutory_bruto_456m_omzet73_empty_pnl_flip_loss_147k_equity_neg_754k"
LB="lb_bremdael_bruto_456m_omzet73_empty_pnl_flip_loss_147k_equity_neg_754k_cash_jump_jr2025"
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
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Bremdael deposit 2026-00202409,https://consult.cbso.nbb.be/api/external/broker/public/deposits/pdf/2af5dee7-7143-11f1-9307-cfbb4cd6ca3c,NBB official WVV deposit PDF via official broker,{DAY},budget,tick2476; official native PDF 50373 bytes 14p VKT-VZW 26.0.15 m04-f; header 26.06.2026; AV 22.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-06-26 09:43:43 UTC OpenPDF 1.3.26; CDN Last-Modified 09.07.2026; all 14p native; official NBB broker UUID 2af5dee7-7143-11f1-9307-cfbb4cd6ca3c GET 200 50373 official NBB-generated PDF; CDN 2026-00202409 GET 200 same 50373 MD5; importFileType XBRL; VKT-VZW 6.1.3 6.5 6.6 7 8 niet dienstig; 6.1.1 6.1.2 6.2 6.3 6.4 6.7 6.8 present; prior-year identical not restated; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Bremdael 0435.234.149,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0435234149,KBO Public Search FOD Economie,{DAY},official_register,tick2476; Actief; 1 VE 2.156.449.362 Bremdael Ernest Claesstraat 62 2200 Herentals since 05.10.2006; VZW since 07.05.1988; begindatum 07.05.1988; zetel Ernest Claesstraat 62 2200 Herentals since 07.12.2017; RSZ-werkgever since 01.04.1994; RSZ2025 87.101 RVT; BTW2025 87.301 ROB; FOI onthaal@bremdael.be; leftover mined city_herentals WZC; NOT De Augustientjes 0445.602.360 remine; NOT Hupskadee 0863.886.651 remine; NOT Armonea 0889.421.308 commercial; NOT Orelia 0810.196.557 commercial",
f"{SRC_SBM},NBB Consult / SBM fiche Bremdael 0435234149 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0435234149,NBB Consult / SBM,{DAY},official_register,tick2476; deposit-id 2026-00202409 YE 01.01.2025-31.12.2025 filing 26.06.2026 published VKT-VZW Verkort model vereniging Initial; Companyweb last-balansjaar 2025 deposit-id discovery OK euros NOT OK; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},Bremdael FOI contact leftover city_herentals WZC,https://bremdael.be/,VZW Bremdael leftover city_herentals WZC + GAW 1 VE,{DAY},foi_contact,tick2476; FOI onthaal@bremdael.be; tel 014/224933; zetel Ernest Claesstraat 62 2200 Herentals; 1 VE leftover mined city_herentals after De Augustientjes different-city skip; WZC + GAW Hof van Bremdael; 54+6 kamers; 60 serviceflats; Patio dementie; Paviljoen; NOT De Augustientjes remine; NOT Hupskadee remine; NOT Hupskadee BV private; NOT Pardoes remine; NOT Bambi remine; NOT Zonneschijn remine; NOT Infano remine; NOT Vijverbeek remine; NOT t Zonnetje remine; NOT Kindercentrum remine; NOT Duinhuisjes remine; NOT Mater Dei remine; NOT Savio remine; NOT Paideia remine; NOT Ooievaarsnest remine; NOT DE ZONNEKINDJES remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Kinderlach YE2024; NOT Helan; NOT De Speelboom Brussels leftover-via-VE; NOT Villa Boempatat SCAN/CDN403; NOT Elief CDN 403; NOT Hebe training; NOT Zo Groot YE2024; NOT De Bolster Zwalm not leftover mined parent; NOT GERUST zorgcentrale; NOT Vormingscentrum training; NOT Zwarte Zusters dissolved; NOT KIOS Schoten no deposits; NOT Molleke city_mol YE2024; NOT t Sas city_denderleeuw YE2024 2026-00050081; NOT Dol-Fijn Turnhout leftover-via-VE; NOT Pardoes NV bookshop; NOT Zusterhof remine; NOT Olliebollie BV private; NOT In de wolken BV private; NOT Troetelland Geel private BV; NOT De Zandkapoentjes BV private; NOT Armonea Vogelzang/Hemelrijck commercial; NOT Orelia Koningshof commercial; NOT Stijn leftover-via-VE Hasselt remine; NOT Felies leftover-via-VE Brussels; NOT 3Wplus remine; NOT Klein Hemelrijk absorbed",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},Bremdael,ASBL Bremdael,Bremdael VZW (leftover city_herentals WZC),parastatal,city_herentals,nl,https://bremdael.be/,onthaal@bremdael.be,Ernest Claesstraat 62 2200 Herentals,tick2476 YE2025 Strong official native NBB PDF deposit 2026-00202409 + Strong KBO 0435.234.149 Actief 1 VE 2.156.449.362; omzet70 empty VKT; 73 empty VKT; 76A empty; envelope bruto 9900 DROP 4557619; bruto DROP 4557619; pnl FLIP LOSS 146785; 9901 FLIP LOSS 114897; equity NEG DROP 754371; assets JUMP 1430125; debt JUMP 2184496; FTE JUMP 62.2; kapitaalsubsidies empty; destin691 empty; 791 empty; cash JUMP 105787; geldbeleggingen empty; leftover city_herentals WZC 1 VE; NOT De Augustientjes 0445.602.360 remine; NOT Hupskadee 0863.886.651 remine; NOT Hupskadee BV 0476.248.224 private BV; NOT Pardoes Mechelen 0417.400.205 remine; NOT Bambi Kalmthout 0443.006.522 remine; NOT Zonneschijn Dendermonde 0877.850.493 remine; NOT Infano Ternat 0477.578.411 remine; NOT Vijverbeek Asse 0448.164.744 remine; NOT t Zonnetje Waregem 0443.648.306 remine; NOT Kindercentrum Waregem 0408.226.775 remine; NOT Duinhuisjes 0413.323.037 remine; NOT 3Wplus Kinderopvang Asse 0893.870.539 remine; NOT Mater Dei 0431.168.859 remine; NOT WZC Mater Dei Heikruis remine; NOT Savio Dilbeek 0472.564.501 remine; NOT Dominiek Savio remine; NOT EVA Dilbeek 0477.276.325 remine; NOT Paideia 0445.129.931 remine; NOT Ooievaarsnest 0418.588.256 remine; NOT DE ZONNEKINDJES 0416.541.952 remine; NOT D'n Opvang 0676.442.465 remine; NOT CAR Overleie 0454.250.505 remine; NOT Gesticht 0410.918.031 remine; NOT HOCUS-POCUS 0466.893.167 remine; NOT VKA 0433.480.132 remine; NOT Soetkin 0443.641.970 remine; NOT t Sloeberke 0410.973.360 remine; NOT CAR Accent 0413.208.122 remine; NOT De Elfjes 0455.636.912 remine; NOT De Steijgertjes 0413.421.720 remine; NOT H.Hart WZC 0413.595.330; NOT Zo Groot 0818.420.771 leftover city_oostende YE2024; NOT De Groene Verte 0465.061.649 remine; NOT De Vleugels 0431.408.290 remine; NOT De Pallieterkes 0418.538.865 remine; NOT De Medemens KDV 0893.678.915 remine; NOT De Medemens parent 0428.692.191 remine; NOT OKO & ZO 0862.154.608 remine; NOT Harlekijntjes 0407.700.403 remine; NOT Hartjes Ninove 0446.391.327 remine; NOT Hartjes Tienen 0441.374.348 remine; NOT De Wissel 0421.913.376 remine; NOT Familia 0461.401.779; NOT Peutertuinen GO Mariakerke 0410.221.116; NOT Mini-creches GO Next 0896.468.060 leftover city_hasselt YE2024; NOT Kinderlach 0450.275.186; NOT Helan; NOT De Speelboom Brussels leftover-via-VE; NOT Villa Boempatat 0660.616.520 leftover city_gent YE2025 SCAN/CDN403 2026-00396513; NOT Elief 0451.624.377 CDN 403; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; NOT De Bolster 0861.680.989 YE2025 zetel Zwalm city_zwalm not mined; NOT GERUST 0776.808.068 zorgcentrale; NOT Jessa hospital special schema; NOT Vormingscentrum 0413.342.338 training; NOT Zwarte Zusters 0413.272.260 dissolved; NOT Ferm Kinderopvang 0416.117.627 remine; NOT ZONNESTRAAL; NOT Molleke 0448.186.520 leftover city_mol YE2024; NOT t Sas 0448.731.106 leftover city_denderleeuw YE2024 2026-00050081; NOT Dol-Fijn 0439.731.880 Turnhout zetel leftover-via-VE; NOT Pardoes NV 0867.020.840 bookshop; NOT Witte Meren remine; NOT Zusterhof 0473.762.450 remine; NOT Olliebollie BV 0805.501.361 private; NOT In de wolken BV 1006.181.196 private; NOT Troetelland Geel private BV; NOT De Zandkapoentjes BV 0507.854.980 private; NOT Armonea 0889.421.308 Vogelzang/Hemelrijck commercial; NOT Orelia 0810.196.557 Koningshof commercial; NOT Stijn 0439.452.461 leftover-via-VE Hasselt remine; NOT Felies 0420.427.890 leftover-via-VE Brussels; NOT Klein Hemelrijk absorbed; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria SCAN; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Zo Groot Oostende YE2024 not taken; H.Hart Kortrijk YE2024 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_bremdael_omzet_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 70 omzet YE2025 empty (VKT; envelope is bruto 9900),{SRC_PDF},strong,tick2476; PDF p5 native; YE2024 empty; 73 empty; 76A empty",
f"bud_bremdael_73_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 empty (VKT),{SRC_PDF},strong,tick2476; PDF p5 native; YE2024 empty; FOI Departement Zorg / RIZIV matrix behind envelope 4557619",
f"bud_bremdael_opbr_jr2025_statutory,{EID},2025,4557619,4557619,4557619,NBB VKT-VZW envelope bruto 9900 YE2025 DROP -0.77% (omzet empty so envelope is bruto 9900),{SRC_PDF},strong,tick2476; PDF p5 native; YE2024 4593068; 70 empty; 73 empty; 76A empty",
f"bud_bremdael_bruto_jr2025_statutory,{EID},2025,4557619,4557619,4557619,NBB VKT-VZW code 9900 brutomarge YE2025 DROP -0.77% (VKT envelope because omzet empty),{SRC_PDF},strong,tick2476; PDF p5 native; YE2024 4593068; 76A empty; 73 empty",
f"bud_bremdael_pnl_jr2025_statutory,{EID},2025,-146785,-146785,-146785,NBB VKT-VZW code 9904 verlies van het boekjaar YE2025 FLIP to LOSS (was +2224),{SRC_PDF},strong,tick2476; PDF p5 native; YE2024 +2224; bedrijfswinst 9901 -114897 FLIP; destin691 empty",
f"bud_bremdael_bedrijfswinst_jr2025_statutory,{EID},2025,-114897,-114897,-114897,NBB VKT-VZW code 9901 bedrijfsverlies YE2025 FLIP to LOSS (was +38325),{SRC_PDF},strong,tick2476; PDF p5 native; YE2024 +38325; 62 4545578 JUMP; 630 115263 JUMP; 66A empty; 640/8 11674 JUMP; 635/9 empty; 631/4 empty",
f"bud_bremdael_equity_jr2025_statutory,{EID},2025,-754371,-754371,-754371,NBB VKT-VZW code 10/15 eigen vermogen YE2025 NEG DROP -24.16%,{SRC_PDF},strong,tick2476; PDF p4 native; YE2024 -607585; kapitaalsubsidies empty; overgedragen 14 DROP -754371; fondsen 10 empty; bestemde fondsen 13 empty",
f"bud_bremdael_assets_jr2025_statutory,{EID},2025,1430125,1430125,1430125,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +6.80%,{SRC_PDF},strong,tick2476; PDF p3 native; YE2024 1339079; MVA 22/27 658948 DROP; cash 105787 JUMP; geldbeleggingen empty; aanbouw 27 empty; FVA 28 empty; LT recv 29 empty",
f"bud_bremdael_debt_jr2025_statutory,{EID},2025,2184496,2184496,2184496,NBB VKT-VZW code 17/49 schulden YE2025 JUMP +12.22%,{SRC_PDF},strong,tick2476; PDF p4 native; YE2024 1946664; 17 201644 DROP; 42/48 1767322 JUMP; 43 empty",
f"bud_bremdael_cash_jr2025_statutory,{EID},2025,105787,105787,105787,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +250.30%,{SRC_PDF},strong,tick2476; PDF p3 native; YE2024 30199; geldbeleggingen 50/53 empty; capex 71368 gebouwen DROP 433093",
f"bud_bremdael_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty (791 empty; 14 DROP -754371 = prior -607585 + pnl -146785),{SRC_PDF},strong,tick2476; PDF p6 native; YE2024 destin empty; bestemde fondsen 13 empty FOI",
])
print("entities+budgets ok")

cash_json=(
"\"{\"\"2025_omzet\"\":0,\"\"2025_73\"\":0,\"\"2025_76A\"\":0,"
"\"\"2025_opbr70_76A\"\":4557619,\"\"2025_bruto\"\":4557619,"
"\"\"2025_pnl\"\":-146785,\"\"2025_bedrijfswinst\"\":-114897,"
"\"\"2025_equity\"\":-754371,\"\"2025_assets\"\":1430125,\"\"2025_debt\"\":2184496,"
"\"\"2025_fte\"\":62.2,\"\"2025_kapitaalsubsidies\"\":0,\"\"2025_destin691\"\":0,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":105787,\"\"2025_geldbeleggingen\"\":0,"
"\"\"2025_personnel62\"\":4545578,\"\"2025_gebouwen22\"\":433093,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":0,"
"\"\"2025_fondsen10\"\":0,\"\"2025_overgedragen14\"\":-754371,"
"\"\"2025_bestemdefondsen13\"\":0,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":115263,\"\"2025_capex\"\":71368,"
"\"\"2025_ltrecv29\"\":0,\"\"2025_75\"\":229,"
"\"\"2024_omzet\"\":0,\"\"2024_73\"\":0,"
"\"\"2024_opbr70_76A\"\":4593068,\"\"2024_bruto\"\":4593068,\"\"2024_pnl\"\":2224,\"\"2024_bedrijfswinst\"\":38325,"
"\"\"2024_equity\"\":-607585,\"\"2024_assets\"\":1339079,"
"\"\"2024_debt\"\":1946664,\"\"2024_cash\"\":30199,\"\"2024_fte\"\":61.9,"
"\"\"2024_destin691\"\":0,\"\"2024_kapitaalsubsidies\"\":0,\"\"2024_76A\"\":0,"
"\"\"2024_geldbeleggingen\"\":0}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Bremdael YE2025 (bruto DROP 4.56m / omzet+73 empty VKT / pnl FLIP LOSS 147k / equity NEG 754k / cash JUMP 106k / Strong PDF),{EID},Departement Zorg + leftover city_herentals WZC,VZW Bremdael (KBO 0435.234.149; Actief; 1 VE; zetel Herentals),2026-06-22,2025,2025,4557619,{cash_json},0,active,https://consult.cbso.nbb.be/api/external/broker/public/deposits/pdf/2af5dee7-7143-11f1-9307-cfbb4cd6ca3c,Public WZC dual of mined city_herentals,Publish Departement Zorg / RIZIV matrix behind envelope 4.56m + why omzet+73 empty VKT and why pnl FLIP LOSS 146785 while equity NEG 754371 and cash JUMP 105787,{SRC_PDF},strong,Vlaanderen>Antwerpen>Herentals>Bremdael>JR2025_statutory_L5,tick2476; Strong official native PDF; leftover mined city_herentals WZC; 1 VE; prior-year identical; NOT every-10; NOT De Augustientjes remine; NOT Hupskadee remine; NOT Pardoes remine; NOT Bambi remine; NOT Zonneschijn remine; NOT Infano remine; NOT Hupskadee BV private; NOT Armonea commercial; NOT Orelia commercial; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"Bremdael bruto DROP 4.56m / omzet+73 empty VKT / pnl FLIP LOSS 147k / equity NEG 754k / cash JUMP 106k (YE2025 leftover city_herentals WZC)",
"L5",
"wzc_vzw_statutory",
"Vlaanderen>Antwerpen>Herentals>Bremdael>JR2025",
"4557619",
"4557619",
"PDF envelope 4557619 = bruto 9900 VKT because omzet empty; 70 empty; 73 empty; 76A empty; bruto 4557619; bedrijfswinst FLIP LOSS 114897; pnl FLIP LOSS 146785; equity NEG DROP 754371; assets JUMP 1430125; debt JUMP 2184496; FTE 62.2; kapitaalsubsidies empty; destin691 empty; cash JUMP 105787; leftover city_herentals WZC",
"strong",
SRC_PDF,
"Departement Zorg + leftover city_herentals WZC",
"WZC / RVT leftover city_herentals",
"4.56m envelope; omzet+73 empty VKT; pnl FLIP LOSS 146785; equity NEG 754371; cash JUMP 105787; leftover city_herentals WZC",
"5.55",
"5.40",
"5.32",
"5.48",
"FOI Departement Zorg / RIZIV matrix behind envelope 4.56m + why omzet+73 empty VKT and why pnl FLIP LOSS 146785 while equity NEG 754371 and cash JUMP 105787",
"active",
"",
"tick2476 leftover mined city_herentals WZC after De Augustientjes lock; 1 VE; prior-year identical; NOT every-10; NOT De Augustientjes remine; NOT Hupskadee remine; NOT Pardoes remine; NOT Bambi remine; NOT Zonneschijn remine; NOT Infano remine; NOT Hupskadee BV 0476.248.224 private BV; NOT Armonea commercial; NOT Orelia commercial; NOT KIOS Schoten no deposits; NOT Molleke city_mol YE2024; NOT t Sas city_denderleeuw YE2024 2026-00050081",
])
assert len(next(csv.reader(StringIO(row))))==21
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>Antwerpen>Herentals>Bremdael>WZC",
"entity_id": EID,
"what_is_missing": "Departement Zorg / RIZIV split behind envelope 4557619 (bruto 9900 VKT; omzet 70 empty + 73 empty + 76A empty) and why destin empty while pnl FLIP LOSS 146785 and equity NEG DROP 754371 and cash JUMP 105787 and debt JUMP 2184496 and 62 JUMP 4545578 FTE 62.2 plus continuity restructuring",
"why_it_matters": "Strong official PDF leftover public WZC of mined city_herentals; VKT envelope bruto 4.56m because omzet empty; public WZC + GAW 1 VE Ernest Claesstraat 62 Herentals; 54+6 kamers; 60 serviceflats; equity NEG 754k / cash JUMP 106k / pnl FLIP LOSS 147k / continuity herstructurering",
"priority": "8",
"recipient_body": "VZW Bremdael / Raad van Bestuur",
"recipient_email": "onthaal@bremdael.be",
"recipient_postal": "Ernest Claesstraat 62 2200 Herentals",
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
"notes": "tick2476; ready NOT sent; Strong official native NBB PDF; leftover mined city_herentals WZC after De Augustientjes lock; 1 VE; prior-year identical; NOT every-10; off De Augustientjes remine; off Hupskadee remine; off Pardoes remine; off Bambi remine; off Zonneschijn remine; off Hupskadee BV private; off Armonea commercial; off Orelia commercial",
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
if rq_raw.count(b"rq_2476,")!=1: raise SystemExit(f"bad 2476 count {rq_raw.count(b'rq_2476,')}")
if b"rq_2477," in rq_raw: raise SystemExit("2477 exists")
idx=rq_raw.rfind(b"rq_2476,")
if idx<0: raise SystemExit("rq_2476 not found")
new_2476=(
"rq_2476,leftover dual Bremdael YE2025,hole_fill,8,done,L5,vzw_bremdael_herentals,"
"Took unused leftover public WZC Bremdael 0435.234.149 leftover mined city_herentals. Official NBB VKT-VZW YE2025 2026-00202409 native 14p. Envelope bruto 9900 DROP 4557619 (omzet+73 empty VKT); pnl FLIP LOSS 146785; equity NEG 754371; cash JUMP 105787; FTE 62.2. NOT De Augustientjes remine. NOT Hupskadee remine. NOT Pardoes remine. NOT Bambi remine. NOT Zonneschijn remine. NOT Hupskadee BV private. NOT Armonea commercial. NOT Orelia commercial.,"
f",{STAMP},{STAMP},tick2476 leftover mined city_herentals WZC; Strong native PDF; 1 VE; prior-year identical; next every-10 is 2480\n"
)
new_2477=(
"rq_2477,leftover dual after Bremdael — hunt unused public dual,hole_fill,8,open,L5,,"
"After Bremdael YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf. Less-picked mined cities still with 0 leftover CIK: schoten / vilvoorde / mol (herentals now has Bremdael WZC; geel has De Augustientjes; mechelen has Pardoes; kalmthout has Bambi; dendermonde has Zonneschijn; begijnendijk has Hupskadee). Molleke 0448.186.520 leftover city_mol YE2024 — take ONLY if unused + official YE2025 native PDF. t Sas 0448.731.106 leftover city_denderleeuw YE2024 only 2026-00050081 — skip unless YE2025. Villa Boempatat 0660.616.520 leftover city_gent YE2025 2026-00396513 CDN 403 / SCAN — take ONLY if unused + official native-text YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen YE2025 2026-00374905 CDN 403 — take ONLY if CDN 200 native. Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO! Next / Zo Groot Oostende still YE2024 — take ONLY if unused + official YE2025 PDF. De Bolster 0861.680.989 YE2025 zetel Zwalm (city_zwalm not mined) — take ONLY if leftover of a mined parent. Jessa leftover city_hasselt hospital YE2025 PDF — take ONLY if unused + official YE2025 euros extract. KIOS 0882.468.881 leftover city_schoten — no jaarrekening skip unless deposits appear. Dol-Fijn 0439.731.880 zetel Turnhout leftover-via-VE Herentals — not enough. NOT Bremdael remine. NOT De Augustientjes remine. NOT Hupskadee remine. NOT Hupskadee BV 0476.248.224 private. NOT Pardoes remine. NOT Bambi remine. NOT Zonneschijn remine. NOT Infano remine. NOT Vijverbeek remine. NOT Mater Dei remine. NOT Savio remine. NOT 3Wplus remine. NOT Paideia remine. NOT Ooievaarsnest remine. NOT De Zonnekindjes remine. NOT D'n Opvang remine. NOT CAR Overleie remine. NOT Gesticht remine. NOT Grauwzusters convent. NOT Hocus-Pocus remine. NOT VKA remine. NOT Soetkin remine. NOT t Sloeberke remine. NOT CAR Accent remine. NOT De Groene Verte remine. NOT De Vleugels remine. NOT De Pallieterkes remine. NOT De Medemens remine. NOT OKO & ZO remine. NOT Harlekijntjes remine. NOT Hartjes remine. NOT De Wissel remine. NOT Familia remine. NOT t Zonnetje remine. NOT Kindercentrum remine. NOT Duinhuisjes remine. NOT Helan. NOT Hebe training. NOT WZC OLVA remine. NOT De Speelboom Brussels leftover-via-VE. NOT GERUST zorgcentrale. NOT Zo Groot remine. NOT De Elfjes remine. NOT De Steijgertjes remine. NOT Vormingscentrum training. NOT Zwarte Zusters dissolved. NOT Dominiek Savio remine. NOT EVA Dilbeek remine. NOT WZC Mater Dei Heikruis remine. NOT Ferm Kinderopvang remine. NOT Molleke YE2024 remine. NOT t Sas YE2024 remine. NOT Witte Meren remine. NOT Zusterhof remine. NOT Pardoes NV bookshop. NOT Olliebollie BV private. NOT In de wolken BV private. NOT Troetelland Geel private BV. NOT De Zandkapoentjes BV private. NOT Armonea Vogelzang/Hemelrijck commercial. NOT Orelia Koningshof commercial. NOT Stijn leftover-via-VE Hasselt remine. NOT Felies leftover-via-VE Brussels. NOT Klein Hemelrijk absorbed.,"
f",{STAMP},{STAMP},spawned after tick2476; Bremdael taken leftover mined city_herentals WZC; De Augustientjes taken leftover mined city_geel CIK; Hupskadee taken leftover mined city_begijnendijk CIK; Pardoes taken leftover mined city_mechelen CIK; Bambi taken leftover mined city_kalmthout CIK; Zonneschijn taken leftover mined city_dendermonde CIK; Infano taken leftover mined city_ternat CIK EVERY-10; t Sas city_denderleeuw YE2024; Molleke city_mol YE2024; KIOS Schoten no deposits; next every-10 is 2480\n"
)
if new_2476.count("\n")!=1 or new_2477.count("\n")!=1: raise SystemExit("bad rq newlines")
for label,line in [("2476",new_2476),("2477",new_2477)]:
    n=len(next(csv.reader(StringIO(line))))
    if n!=12: raise SystemExit(f"{label} fields {n} != 12")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2476.encode("utf-8"))
    f.write(new_2477.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2476", chk.count(b"rq_2476,"), "n2477", chk.count(b"rq_2477,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2476,2476,no,tick2476 leftover dual Bremdael 0435.234.149 Strong native PDF (omzet70 empty VKT; 73 empty VKT; 76A empty; envelope bruto 9900 DROP 4557619; bruto DROP 4557619; pnl FLIP LOSS 146785; 9901 FLIP LOSS 114897; equity NEG DROP 754371; assets JUMP 1430125; debt JUMP 2184496; FTE JUMP 62.2; kapitaalsubsidies empty; destin691 empty; 791 empty; cash JUMP 105787; geldbeleggingen empty; 1 VE leftover city_herentals WZC); leftover mined city_herentals WZC; prior-year identical; NOT De Augustientjes remine; NOT Hupskadee remine; NOT Hupskadee BV 0476.248.224 private; NOT Pardoes remine; NOT Bambi remine; NOT Zonneschijn remine; NOT Infano remine; NOT Vijverbeek remine; NOT t Zonnetje remine; NOT Kindercentrum remine; NOT Duinhuisjes remine; NOT 3Wplus remine; NOT Mater Dei remine; NOT WZC Mater Dei Heikruis remine; NOT Savio remine; NOT Dominiek Savio remine; NOT EVA Dilbeek remine; NOT Paideia remine; NOT Ooievaarsnest remine; NOT DE ZONNEKINDJES remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT Grauwzusters convent; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens KDV remine; NOT De Medemens parent remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Mini-creches GO Next remine; NOT Kinderlach; NOT Zo Groot YE2024; NOT De Speelboom Brussels leftover-via-VE; NOT Elief CDN 403; NOT Villa Boempatat SCAN/CDN403; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; NOT De Bolster Zwalm not leftover mined parent; NOT GERUST zorgcentrale; NOT De Elfjes remine; NOT De Steijgertjes remine; NOT Vormingscentrum training; NOT Zwarte Zusters dissolved; NOT Ferm Kinderopvang remine; NOT KIOS Schoten no deposits; NOT Molleke city_mol YE2024; NOT t Sas city_denderleeuw YE2024 2026-00050081; NOT Dol-Fijn Turnhout leftover-via-VE; NOT Witte Meren remine; NOT Zusterhof remine; NOT Pardoes NV bookshop; NOT Olliebollie BV private; NOT In de wolken BV private; NOT Troetelland Geel private BV; NOT De Zandkapoentjes BV private; NOT Armonea Vogelzang/Hemelrijck commercial; NOT Orelia Koningshof commercial; NOT Stijn leftover-via-VE Hasselt remine; NOT Felies leftover-via-VE Brussels; NOT Klein Hemelrijk absorbed; next every-10 is 2480; next rq_2477 leftover dual\n",
encoding="utf-8",
)
print("loop_state ok")

log=ROOT/"docs/doge/loop_log.md"
log_raw=log.read_bytes()
if not log_raw.endswith(b"\n"): raise SystemExit("loop_log no LF")
entry=f"""
### {STAMP} - tick 2476 - rq_2476 Bremdael (bruto DROP 4.56m / omzet+73 empty VKT / pnl FLIP LOSS 147k / equity NEG 754k / cash JUMP 106k / Strong PDF)

- Unit: **rq_2476** leftover dual after **De Augustientjes@2475**. Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024** (not re-downloaded); FARO 2026-00010398 still **YE2024** (HEAD-only policy). Discovery path: less-picked mined Flanders cities with 0 leftover CIK (herentals / schoten / vilvoorde / mol). Confirmed `city_herentals` / `city_schoten` / `city_vilvoorde` / `city_mol` exist. Public Opgroeien/Cobrha groepsopvang lists: Herentals CIK leftover exhausted (Hummeltjeshof city-run; Speelboom Familiehulp leftover-via-VE Brussels; Dol-Fijn leftover-via-VE Turnhout; Zandkapoentjes BV private; Snuffel 3 BV). Schoten CIK leftover exhausted (De Koekoek / 't Beertje / Zazou city 0212.168.001; Elfenland / Villa Valentijn / PIMPERNEL / Vlindertje / Eigenwijs / Happy Hearts private BVs; Helan remine; KIOS no JR). Vilvoorde CIK leftover exhausted (KaDeeke city-run; Regenboog / Kinderhoeve / Kabouterland / bosvriendjes private BVs; Zonnetje Infano remine leftover-via-VE; Regenboogjes Felies 0420.427.890 leftover-via-VE Brussels; Villadroom 3Wplus remine; Ark van Noah Helan remine). Mol CIK leftover exhausted (Molleke YE2024; Polderke GCV private; Ukkepuk BV; Tingelientje BV; Troetelland Mol BV; Ferm 't Kleine Wolkje + Ka-Baaltjes remine; Meneer Miel = Stijn 0439.452.461 leftover-via-VE Hasselt already mined tick2179; Koning Leeuw / Jef Giraf BV). After 8 failed CIK candidates took leftover WZC of less-picked mined city_herentals. Kinderdagverblijf Molleke **0448.186.520** leftover city_mol still **YE2024** — skip. KIOS leftover city_schoten — no jaarrekening — skip. t Sas leftover city_denderleeuw **YE2024** **2026-00050081** — skip. Dol-Fijn **0439.731.880** zetel Turnhout leftover-via-VE Herentals YE2025 — not enough. Witte Meren leftover city_mol already mined. Zusterhof leftover city_geel already mined. Villa Boempatat leftover city_gent **YE2025** **2026-00396513** CDN **403** / SCAN — not taken. Speelhuis Elief leftover city_antwerpen unused YE2025 **2026-00374905** CDN **403** — not taken. Kinderlach leftover city_eeklo still **YE2024**. De Linde Ronse leftover city_ronse still **YE2024**. Woon en Zorg H. Hart Kortrijk leftover city_kortrijk still **YE2024**. Jessa leftover city_hasselt hospital YE2025 PDF / hospital special schema — not taken. Mini-creches GO! Next leftover city_hasselt still **YE2024**. Zo Groot Oostende leftover city_oostende still **YE2024**. Familiehulp De Speelboom YE2025 unused Brussels zetel leftover-via-VE — not taken. De Bolster 0861.680.989 YE2025 zetel Zwalm (city_zwalm not mined) — not taken. GERUST Zorgcentrale leftover city_herentals YE2025 — zorgcentrale not in dual types — not taken. Armonea WZC Vogelzang Herentals / Hemelrijck Mol commercial NV — skip. Orelia Residentie Koningshof Schoten commercial NV — skip. Hummeltjeshof city-run Herentals — skip. Vormingscentrum leftover city_gent training — skip. Helan Kinderopvang already skipped. Zwarte Zusters dissolved — skip. Private BVs (Olliebollie **0805.501.361** / In de wolken **1006.181.196** / Troetelland Geel / De Zandkapoentjes **0507.854.980** / Vlindertje Schoten / Regenboog Vilvoorde / Hupskadee BV **0476.248.224**) skipped. De Augustientjes 0445.602.360 just mined — do not remine. Hupskadee 0863.886.651 already mined — do not remine. Pardoes 0417.400.205 already mined — do not remine. Bambi 0443.006.522 already mined — do not remine. Zonneschijn 0877.850.493 already mined — do not remine. Infano 0477.578.411 already mined — do not remine. Vijverbeek already mined — do not remine. Mater Dei already mined — do not remine. Savio already mined — do not remine. t Zonnetje Waregem already mined — do not remine. First leftover unused + live official YE2025 native euros: took FREE leftover Flemish **VZW Bremdael** YE2025 (KBO **0435.234.149**; zetel Ernest Claesstraat 62 2200 Herentals; **Actief** **1 VE** **2.156.449.362** Bremdael since 05.10.2006; RSZ2025 **87.101** RVT; leftover of mined **city_herentals**; onthaal@bremdael.be; WZC + GAW Hof van Bremdael; 54 éénpersoonskamers + 6 tweepersoonskamers; 60 serviceflats; Patio dementie + Paviljoen). Identity trap: Bremdael 0435.234.149 ≠ De Augustientjes **0445.602.360** leftover city_geel just mined; ≠ Hupskadee **0863.886.651**; ≠ Hupskadee BV **0476.248.224** private BV; ≠ Pardoes **0417.400.205**; ≠ Kinderdagverblijf Bambi **0443.006.522**; ≠ Zonneschijn **0877.850.493**; ≠ INFANO **0477.578.411**; ≠ Kinderdagverblijf Vijverbeek **0448.164.744**; ≠ t Zonnetje Waregem **0443.648.306**; ≠ DE ZONNEKINDJES **0416.541.952**; ≠ ZONNESTRAAL / Zonnestraal Junior; ≠ Kindercentrum Waregem **0408.226.775**; ≠ Duinhuisjes **0413.323.037**; ≠ Groepsopvang Mater Dei **0431.168.859**; ≠ WZC Mater Dei Heikruis; ≠ Kinderdagverblijf Savio **0472.564.501**; ≠ Dominiek Savio; ≠ EVA Dilbeek **0477.276.325**; ≠ Paideia **0445.129.931**; ≠ KDV Ooievaarsnest **0418.588.256**; ≠ D'n Opvang **0676.442.465**; ≠ CAR Overleie **0454.250.505**; ≠ Gesticht **0410.918.031**; ≠ HOCUS-POCUS **0466.893.167**; ≠ VKA **0433.480.132**; ≠ Soetkin **0443.641.970**; ≠ t Sloeberke **0410.973.360**; ≠ CAR Accent **0413.208.122**; ≠ Speelhuis Elief **0451.624.377**; ≠ Villa Boempatat **0660.616.520**; ≠ De Groene Verte **0465.061.649**; ≠ De Vleugels **0431.408.290**; ≠ De Pallieterkes **0418.538.865**; ≠ De Medemens Kinderdagverblijven **0893.678.915**; ≠ De Medemens **0428.692.191**; ≠ OKO & ZO **0862.154.608**; ≠ Harlekijntjes **0407.700.403**; ≠ Hartjes Ninove **0446.391.327**; ≠ Hartjes Tienen **0441.374.348**; ≠ De Wissel **0421.913.376**; ≠ Ferm Kinderopvang **0416.117.627**; ≠ Familia **0461.401.779**; ≠ Peutertuinen GO Mariakerke **0410.221.116**; ≠ Mini-crèches GO! Next **0896.468.060**; ≠ Kinderlach **0450.275.186**; ≠ Helan 0464.151.037; ≠ Hebe **0451.789.772**; ≠ WZC OLVA **0430.977.136**; ≠ H.Hart Kortrijk **0413.595.330**; ≠ De Linde Ronse **0778.279.401**; ≠ De Bolster **0861.680.989**; ≠ GERUST **0776.808.068**; ≠ Jessa **0821.142.117**; ≠ AZ Sint-Maria **0467.967.491**; ≠ De Elfjes **0455.636.912**; ≠ De Steijgertjes **0413.421.720**; ≠ TKDV Het Veer Kloosterstraat 6; ≠ Vormingscentrum **0413.342.338** training; ≠ Zwarte Zusters **0413.272.260** dissolved; ≠ KIOS **0882.468.881**; ≠ Molleke **0448.186.520**; ≠ t Sas **0448.731.106**; ≠ Dol-Fijn **0439.731.880**; ≠ Witte Meren **0418.234.997**; ≠ Zusterhof **0473.762.450**; ≠ Pardoes NV **0867.020.840** bookshop; ≠ Olliebollie BV **0805.501.361**; ≠ In De Wolken BV **1006.181.196**; ≠ De Zandkapoentjes BV **0507.854.980**; ≠ Armonea NV **0889.421.308** Vogelzang/Hemelrijck commercial; ≠ Orelia Zorg NV **0810.196.557** Koningshof commercial; ≠ Stijn VZW **0439.452.461** leftover-via-VE Hasselt remine; ≠ Felies **0420.427.890** leftover-via-VE Brussels; ≠ Klein Hemelrijk absorbed. 1 VE Herentals — leftover of mined city_herentals (zetel + Ernest Claesstraat 62). Confirmed leftover public (WZC + GAW; RVT 87.101 / ROB 87.301; 54+6 kamers; 60 serviceflats) not convent / not private clinic / not school / not OVBJ / not CIK / not VAPH / not Ferm / not De Augustientjes remine / not Armonea commercial / not private BV. VKT-VZW **native text** (not scan) — 50373 B / 14p all native euros (VKT-VZW 6.1.3 / 6.5 / 6.6 / 7 / 8 niet dienstig; 6.1.1 / 6.1.2 / 6.2 / 6.3 / 6.4 / 6.7 / 6.8 present).
- Found: official NBB VKT-VZW native PDF deposit **2026-00202409** (50373 B / 14p; AV **22.06.2026**; header **26.06.2026**; official NBB broker UUID 2af5dee7 GET **200** 50373 official NBB-generated OpenPDF 1.3.26 CreationDate 26.06.2026; CDN GET **200** same 50373 MD5 Last-Modified 09.07.2026; importFileType XBRL; all 14p native; prior-year identical not restated) — omzet 70 **empty** VKT; 73 **empty** VKT; 76A **empty**; envelope bruto 9900 **EUR4557619** DROP −0.77% (VKT envelope because omzet empty; was 4593068); bruto 9900 **EUR4557619** DROP −0.77%; 62 **EUR4545578** JUMP +2.24%; 630 **EUR115263** JUMP +15.31%; 66A **empty**; 640/8 **EUR11674** JUMP +32.93%; 635/9 **empty**; 631/4 **empty**; bedrijfswinst 9901 **EUR-114897** FLIP to LOSS (was 38325); pnl 9904 **EUR-146785** FLIP to LOSS (was 2224); equity **EUR-754371** DROP −24.16%; assets **EUR1430125** JUMP +6.80%; debt **EUR2184496** JUMP +12.22%; FTE **62.2** JUMP +0.48% (was 61.9; 100 62.2; 105 61.6); kapitaalsubsidies **empty**; destin 691 **empty** (791 empty; 14 DROP −754371 = prior −607585 + pnl −146785); 791 **empty**; cash **EUR105787** JUMP +250.30%; geldbeleggingen **empty**; gebouwen **EUR433093** DROP; MVA 22/27 **EUR658948** DROP; aanbouw **empty**; capex **EUR71368**; fondsen 10 **empty**; overgedragen 14 **EUR-754371** DROP; bestemde fondsen 13 **empty**; voorzieningen 16 **empty**; FVA 28 **empty**; LT recv 29 **empty**. Continuity p14: overgedragen verlies 754370.72; verlies 146785.49 door herstructurering / tijdelijke dubbele personeelskosten. Strong KBO + Strong PDF (native all pages; not SBM table; not Companyweb euros). Site: 1 VE leftover mined city_herentals WZC. NOT De Augustientjes remine. NOT Hupskadee remine. NOT Pardoes remine. NOT Bambi remine. NOT Zonneschijn remine. NOT Hupskadee BV private. NOT Armonea commercial. NOT Orelia commercial. NOT t Sas YE2024. NOT Molleke YE2024. NOT KIOS no deposits.
- Wrote: sources (+4); budgets (+11); commitments (+1); leaderboard (+1 pi 5.48); entities (+1 vzw_bremdael_herentals); foi + draft `gap_bremdael_wzc_matrix_bruto_4_56m_omzet73_empty_pnl_flip_loss_147k_equity_neg_754k_cash_jump_l5`; rq_2476=done + rq_2477 open; loop_state ticks=2476; raw tick2476/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2480**). Next: rq_2477 unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Bremdael remine / NOT De Augustientjes remine / NOT Hupskadee remine / NOT Hupskadee BV private / NOT Pardoes remine / NOT Bambi remine / NOT Zonneschijn remine / NOT Infano remine / NOT Vijverbeek remine / NOT t Zonnetje remine / NOT Kindercentrum remine / NOT Duinhuisjes remine / NOT Mater Dei remine / NOT Savio remine / NOT 3Wplus remine / NOT Paideia remine / NOT Ooievaarsnest remine / NOT De Zonnekindjes remine / NOT D'n Opvang remine / NOT CAR Overleie remine / NOT Gesticht remine / NOT Grauwzusters convent / NOT HOCUS-POCUS remine / NOT VKA remine / NOT Soetkin remine / NOT t Sloeberke remine / NOT CAR Accent remine / NOT De Groene Verte remine / NOT De Vleugels remine / NOT De Pallieterkes remine / NOT De Medemens remine / NOT OKO & ZO remine / NOT Harlekijntjes remine / NOT Hartjes remine / NOT De Wissel remine / NOT Familia remine / NOT Mini-creches GO Next remine / NOT WZC OLVA remine / NOT Hebe training / NOT Quattro remine / NOT GERUST zorgcentrale / NOT Zo Groot remine / NOT De Elfjes remine / NOT De Steijgertjes remine / NOT Vormingscentrum training / NOT Zwarte Zusters dissolved / NOT Dominiek Savio remine / NOT EVA Dilbeek remine / NOT WZC Mater Dei Heikruis remine / NOT Ferm Kinderopvang remine / NOT Molleke YE2024 / NOT t Sas YE2024 / NOT Witte Meren remine / NOT Zusterhof remine / NOT Pardoes NV bookshop / NOT Olliebollie BV private / NOT In de wolken BV private / NOT Troetelland Geel private BV / NOT De Zandkapoentjes BV private / NOT Armonea commercial / NOT Orelia commercial / NOT Stijn leftover-via-VE Hasselt remine / NOT Felies leftover-via-VE Brussels / NOT Klein Hemelrijk absorbed). NOW leftover candidates: Molleke 0448.186.520 leftover city_mol YE2024 — take ONLY if unused + official YE2025 native PDF. t Sas 0448.731.106 leftover city_denderleeuw YE2024 only 2026-00050081 — skip unless YE2025. Villa Boempatat 0660.616.520 leftover city_gent YE2025 **2026-00396513** CDN **403** / SCAN — take ONLY if unused + official native-text YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen unused YE2025 **2026-00374905** CDN **403** — take ONLY if unused + CDN 200 native YE2025 PDF. Kinderlach leftover city_eeklo still YE2024 — take ONLY if unused + official YE2025 PDF. De Linde Ronse leftover city_ronse still YE2024 — take ONLY if unused + official YE2025 PDF. H.Hart Kortrijk leftover city_kortrijk still YE2024 — take ONLY if unused + official YE2025 PDF. Jessa leftover city_hasselt hospital YE2025 PDF — take ONLY if unused + official YE2025 euros extract. De Bolster 0861.680.989 YE2025 zetel Zwalm — leftover of mined parent only. Familiehulp De Speelboom YE2025 Brussels zetel — leftover-via-VE not enough per LOOP.md. Mini-creches GO! Next leftover city_hasselt still YE2024 — skip unless YE2025. Zo Groot Oostende leftover city_oostende still YE2024 — skip unless YE2025. KIOS leftover city_schoten no deposits — skip. Dol-Fijn leftover-via-VE not enough. Tick **2480** is next every-10.

"""
with log.open("ab") as f:
    f.write(entry.encode("utf-8"))
print("loop_log ok")
print("WRITE CORE DONE")
