from pathlib import Path
import csv
from io import StringIO
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2491_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_hopperank_jr2025_nbb_pdf_2491"
SRC_KBO="src_hopperank_kbo_2491"
SRC_SBM="src_hopperank_sbm_2491"
SRC_SITE="src_hopperank_site_2491"
EID="vzw_hopperank_asse"
GAP="gap_hopperank_asse_vaph_matrix_bruto_1_38m_omzet_empty_73_drop_1_46m_pnl_drop_44k_l5"
COMM="comm_hopperank_jr2025_statutory_bruto_1_38m_omzet_empty_73_drop_1_46m_pnl_drop_44k"
LB="lb_hopperank_bruto_138m_omzet_empty_73_drop_146m_pnl_drop_44k_jr2025"
assert (ROOT/f"docs/doge/foi/drafts/{GAP}.md").is_file()

def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)

NOTS=("NOT De Sperwer 0415.344.892 remine tick2490; NOT Alderande 0431.893.389 remine tick2489; NOT De Hagewinde 0861.262.010 remine tick2481; NOT 3Wplus Kinderopvang remine; NOT Vijverbeek 0448.164.744 remine tick2469; NOT AMAB 0411.635.039 remine; NOT Hof ter Waarbeek 0478.728.256 remine; NOT Walfergem 0633.687.439 remine; NOT ViTeS leftover-via-VE Leuven; NOT Groep INTRO leftover-via-VE Anderlecht; NOT Mirto leftover-via-VE Gent; NOT Mivas leftover-via-VE Lier; NOT MILLE LUCI 0680.594.461 CVBA no JR; NOT Huis Coppens SENIORS CARE-ION BV commercial; NOT De Cirkel remine; NOT CAR Waas remine; NOT Ter Engelen remine; NOT De Kapoentjes remine; NOT De Zonnewende remine; NOT Huize De Veuster remine; NOT Grijkoort remine; NOT Nektari remine; NOT Reva Ter Linde remine; NOT BWP remine; NOT De Poel leftover-via-VE; NOT ASTOR bankrupt; NOT Aralea YE2024; NOT CAR Kapelhof Drongen OFF; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine leftover-via-VE Gent")

append_lines(DATA/"sources.csv", [
f"{SRC_PDF},NBB MIC-VZW jaarrekening 2025 Hopperank Asse deposit 2026-00126399,http://cdn.staatsbladmonitor.be/2026pdf/2026-00126399.pdf,NBB official WVV deposit PDF via CDN,{DAY},budget,tick2491; official native statutory PDF 41918 bytes 10p MIC-VZW 26.0.11 m08-f; header 29.05.2026; AV 19.05.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-05-29 23:25:51 UTC OpenPDF 1.3.26; CDN Last-Modified 10.06.2026; statutory pages native; CDN 2026-00126399 GET 200 41918 MD5 66694bdfbf5284f43cd866a1ababc3fd; official NBB UUID 7c4d8446-5b42-11f1-9d66-df103d3064ff; MIC-VZW 6.1.1 6.1.3 6.2 6.3 7 8 niet dienstig; 6.1.2 6.4 6.5 present; prior-year identical not restated; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Hopperank Asse 0434.363.921,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0434363921,KBO Public Search FOD Economie,{DAY},official_register,tick2491; Actief; 1 VE leftover city_asse (Gasthuisstraat 7 bus 7 1730 Asse VE 2.159.420.037 since 12.02.2007); zetel Gasthuisstraat 7 bus 7 1730 Asse since 01.01.1999; VZW since 19.10.1987; RSZ2025 88.106; FOI info@hopperank.be; leftover mined city_asse VAPH after 3Wplus+Vijverbeek CIK locks; NOT AMAB remine; NOT Hof ter Waarbeek remine; NOT Walfergem remine; NOT 3Wplus Kinderopvang remine; NOT Vijverbeek remine",
f"{SRC_SBM},NBB Consult / SBM fiche Hopperank 0434363921 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0434363921,NBB Consult / SBM,{DAY},official_register,tick2491; deposit-id 2026-00126399 YE 01.01.2025-31.12.2025 filing MIC-VZW micromodel vereniging Initial UUID 7c4d8446-5b42-11f1-9d66-df103d3064ff; Companyweb last-balansjaar 2025 used for deposit-id discovery via NBB OK euros NOT OK; used for deposit-id discovery only; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
f"{SRC_SITE},Hopperank Asse FOI contact leftover city_asse VAPH,https://hopperank.be/,Hopperank VZW leftover city_asse VAPH 1 VE,{DAY},foi_contact,tick2491; FOI info@hopperank.be; zetel Gasthuisstraat 7 bus 7 1730 Asse; VAPH ambulante+mobiele ondersteuning PVB+RTH regio Asse/Opwijk/Merchtem/Affligem; RSZ2025 88.106; leftover mined city_asse VAPH after CIK locks; NOT AMAB remine; NOT Hof ter Waarbeek remine; NOT Walfergem remine; NOT 3Wplus Kinderopvang remine; NOT Vijverbeek remine; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},Hopperank,ASBL Hopperank,Hopperank VZW (leftover city_asse VAPH),parastatal,city_asse,nl,https://hopperank.be/,info@hopperank.be,Gasthuisstraat 7 bus 7 1730 Asse,tick2491 YE2025 Strong official native NBB PDF deposit 2026-00126399 + Strong KBO 0434.363.921 Actief 1 VE; omzet70 empty MIC; 73 DROP 1462680; 76A empty; envelope bruto9900 DROP 1384983; pnl DROP 44365; 9901 DROP 29074; equity JUMP 1304516; assets JUMP 1515048; debt JUMP 210532; FTE JUMP 16.7; kapitaalsubsidies empty; destin691 empty; 791 empty; cash DROP 456741; geldbeleggingen JUMP 1028808; leftover city_asse VAPH 1 VE; prior-year identical; {NOTS}; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_hopperank_omzet_jr2025_statutory,{EID},2025,0,0,0,NBB MIC-VZW code 70 omzet YE2025 empty MIC,{SRC_PDF},strong,tick2491; PDF p5 native; YE2024 empty; 73 DROP 1462680; 76A empty",
f"bud_hopperank_73_jr2025_statutory,{EID},2025,1462680,1462680,1462680,NBB MIC-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 DROP -4.94%,{SRC_PDF},strong,tick2491; PDF p5 native; YE2024 1538735; FOI VAPH PVB/RTH matrix behind bruto",
f"bud_hopperank_opbr_jr2025_statutory,{EID},2025,1384983,1384983,1384983,NBB MIC-VZW envelope bruto 9900 YE2025 DROP -4.57% (MIC because omzet empty),{SRC_PDF},strong,tick2491; PDF p5 native; YE2024 1451341; 70 empty; 73 DROP 1462680; 76A empty",
f"bud_hopperank_76A_jr2025_statutory,{EID},2025,0,0,0,NBB MIC-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 empty,{SRC_PDF},strong,tick2491; PDF p5 native; YE2024 empty",
f"bud_hopperank_pnl_jr2025_statutory,{EID},2025,44365,44365,44365,NBB MIC-VZW code 9904 winst van het boekjaar YE2025 DROP -67.83%,{SRC_PDF},strong,tick2491; PDF p5 native; YE2024 137918; bedrijfswinst 9901 29074 DROP; destin691 empty",
f"bud_hopperank_bedrijfswinst_jr2025_statutory,{EID},2025,29074,29074,29074,NBB MIC-VZW code 9901 bedrijfswinst YE2025 DROP -76.58% (was 124166),{SRC_PDF},strong,tick2491; PDF p5 native; YE2024 124166; 62 1348508 JUMP; 630 7401 JUMP; 66A empty; 640/8 empty; 635/9 empty; 631/4 empty",
f"bud_hopperank_equity_jr2025_statutory,{EID},2025,1304516,1304516,1304516,NBB MIC-VZW code 10/15 eigen vermogen YE2025 JUMP +3.52%,{SRC_PDF},strong,tick2491; PDF p4 native; YE2024 1260151; kapitaalsubsidies 15 empty; overgedragen 14 1304516 JUMP; fondsen 10 empty; bestemde fondsen 13 empty",
f"bud_hopperank_assets_jr2025_statutory,{EID},2025,1515048,1515048,1515048,NBB MIC-VZW code 20/58 totaal activa YE2025 JUMP +4.84%,{SRC_PDF},strong,tick2491; PDF p3 native; YE2024 1445078; MVA 22/27 29416 DROP; cash 456741 DROP; geldbeleggingen 1028808 JUMP; aanbouw 27 empty",
f"bud_hopperank_debt_jr2025_statutory,{EID},2025,210532,210532,210532,NBB MIC-VZW code 17/49 schulden YE2025 JUMP +13.85%,{SRC_PDF},strong,tick2491; PDF p4 native; YE2024 184927; 17 empty; 42/48 210532 JUMP",
f"bud_hopperank_cash_jr2025_statutory,{EID},2025,456741,456741,456741,NBB MIC-VZW code 54/58 liquide middelen YE2025 DROP -15.60%,{SRC_PDF},strong,tick2491; PDF p3 native; YE2024 541163; geldbeleggingen 50/53 1028808 JUMP; capex 8169 4090",
f"bud_hopperank_destin_jr2025_statutory,{EID},2025,0,0,0,NBB MIC-VZW code 691 toevoeging bestemde fondsen YE2025 empty (791 empty; 13 empty),{SRC_PDF},strong,tick2491; PDF p6 native; YE2024 destin empty; 791 empty; 14 JUMP 1304516; fondsen 10 empty",
])
print("entities+budgets ok")

cash_json=(
"\"{\"\"2025_omzet\"\":0,\"\"2025_73\"\":1462680,\"\"2025_76A\"\":0,"
"\"\"2025_opbr7076A\"\":0,\"\"2025_bruto9900\"\":1384983,"
"\"\"2025_pnl\"\":44365,\"\"2025_bedrijfswinst\"\":29074,"
"\"\"2025_equity\"\":1304516,\"\"2025_assets\"\":1515048,\"\"2025_debt\"\":210532,"
"\"\"2025_fte\"\":16.7,\"\"2025_kapitaalsubsidies\"\":0,\"\"2025_destin691\"\":0,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":456741,\"\"2025_geldbeleggingen\"\":1028808,"
"\"\"2025_personnel62\"\":1348508,\"\"2025_gebouwen22\"\":0,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":0,\"\"2025_66B\"\":0,"
"\"\"2025_fondsen10\"\":0,\"\"2025_overgedragen14\"\":1304516,"
"\"\"2025_bestemdefondsen13\"\":0,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":7401,\"\"2025_capex\"\":4090,"
"\"\"2025_75\"\":23518,\"\"2025_9903\"\":52154,"
"\"\"2024_omzet\"\":0,\"\"2024_73\"\":1538735,"
"\"\"2024_opbr7076A\"\":0,\"\"2024_bruto9900\"\":1451341,\"\"2024_pnl\"\":137918,\"\"2024_bedrijfswinst\"\":124166,"
"\"\"2024_equity\"\":1260151,\"\"2024_assets\"\":1445078,"
"\"\"2024_debt\"\":184927,\"\"2024_cash\"\":541163,\"\"2024_fte\"\":16.3,"
"\"\"2024_destin691\"\":0,\"\"2024_kapitaalsubsidies\"\":0,\"\"2024_76A\"\":0,"
"\"\"2024_geldbeleggingen\"\":867234}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Hopperank YE2025 (bruto DROP 1.38m / omzet empty MIC / 73 DROP 1.46m / pnl DROP 44k / Strong PDF),{EID},VAPH + leftover city_asse VAPH,Hopperank VZW (KBO 0434.363.921; Actief; 1 VE; zetel Asse),2026-05-19,2025,2025,1384983,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00126399.pdf,Public VAPH dual of mined city_asse,Publish VAPH PVB/RTH matrix behind bruto 1.38m and why pnl DROP 44365 after YE2024 137918,{SRC_PDF},strong,Vlaanderen>Vlaams-Brabant>Asse>Hopperank>JR2025_statutory_L5,tick2491; Strong official native PDF; leftover mined city_asse VAPH; 1 VE; prior-year identical; NOT De Sperwer remine; NOT AMAB remine; NOT Hof ter Waarbeek remine; NOT Walfergem remine; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"Hopperank bruto DROP 1.38m / omzet empty MIC / 73 DROP 1.46m / pnl DROP 44k (YE2025 leftover city_asse VAPH)",
"L5",
"vaph_vzw_statutory",
"Vlaanderen>Vlaams-Brabant>Asse>Hopperank>JR2025",
"1384983",
"1384983",
"PDF envelope 1384983 = bruto 9900 MIC because omzet empty; 70 empty; 73 DROP 1462680; 76A empty; bedrijfswinst DROP 29074; pnl DROP 44365; equity JUMP 1304516; assets JUMP 1515048; debt JUMP 210532; FTE 16.7; kapitaalsubsidies empty; destin691 empty; cash DROP 456741; capex 4090; leftover city_asse VAPH",
"strong",
SRC_PDF,
"VAPH + leftover city_asse VAPH",
"VAPH leftover city_asse",
"1.38m bruto; omzet empty MIC; 73 DROP 1.46m; pnl DROP 44k; leftover city_asse VAPH",
"5.40",
"5.18",
"5.12",
"5.23",
"FOI VAPH PVB/RTH matrix behind bruto 1.38m and why pnl DROP 44365 after YE2024 137918 while 62 JUMP 1348508 and FTE JUMP 16.7 and 73 DROP 1462680",
"active",
"",
"tick2491 leftover mined city_asse VAPH after 3Wplus+Vijverbeek CIK locks; 1 VE; prior-year identical; NOT every-10 (next 2500); NOT De Sperwer remine tick2490; NOT Alderande remine; NOT De Hagewinde remine; NOT AMAB remine; NOT Hof ter Waarbeek remine; NOT Walfergem remine; NOT 3Wplus Kinderopvang remine; NOT Vijverbeek remine; NOT ViTeS leftover-via-VE; NOT Groep INTRO leftover-via-VE; NOT Mirto leftover-via-VE; NOT Mivas leftover-via-VE; NOT MILLE LUCI CVBA no JR; NOT Huis Coppens commercial; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine",
])
assert len(next(csv.reader(StringIO(row))))==21
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>Vlaams-Brabant>Asse>Hopperank>VAPH",
"entity_id": EID,
"what_is_missing": "VAPH PVB/RTH / stad Asse split behind bruto 9900 1384983 (omzet 70 empty MIC; 73 DROP 1462680) and why pnl DROP 44365 after YE2024 137918 while destin 691 empty and 62 JUMP 1348508",
"why_it_matters": "Strong official PDF leftover public VAPH of mined city_asse; MIC envelope 1.38m because omzet empty; public ambulante+mobiele 1 VE; pnl DROP 94k / 73 DROP 76k / cash DROP 84k",
"priority": "8",
"recipient_body": "HOPPERANK VZW / Raad van Bestuur",
"recipient_email": "info@hopperank.be",
"recipient_postal": "Gasthuisstraat 7 bus 7 1730 Asse",
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
"notes": "tick2491; ready NOT sent; Strong official native NBB PDF; leftover mined city_asse VAPH after 3Wplus+Vijverbeek CIK locks; 1 VE; prior-year identical; NOT every-10 (next 2500); off De Sperwer remine; off AMAB remine; off Hof ter Waarbeek remine; off Walfergem remine; off 3Wplus Kinderopvang remine; off Vijverbeek remine; off leftover-via-VE; off Armonea commercial; off Vulpia commercial; off Korian commercial",
}
foi_path=DATA/"foi_queue.csv"
raw=foi_path.read_bytes()
if not raw.endswith(b"\n"): raise SystemExit("foi_queue no LF")
with foi_path.open("a", newline="", encoding="utf-8") as f:
    w=csv.DictWriter(f, fieldnames=list(foi_row.keys()), extrasaction="raise", lineterminator="\n")
    w.writerow(foi_row)
print("foi_queue ok")
print("CORE APPEND DONE")
