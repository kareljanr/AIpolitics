from pathlib import Path
import csv
from io import StringIO
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2494_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_avondzon_jr2025_nbb_pdf_2494"
SRC_KBO="src_avondzon_kbo_2494"
SRC_SBM="src_avondzon_sbm_2494"
SRC_SITE="src_avondzon_site_2494"
EID="vzw_avondzon_erpe_mere"
GAP="gap_avondzon_erpe_mere_wzc_matrix_omzet_11_74m_73_drop_2_19m_pnl_flip_loss_54k_l5"
COMM="comm_avondzon_jr2025_statutory_omzet_11_74m_73_drop_2_19m_pnl_flip_loss_54k"
LB="lb_avondzon_omzet_1174m_73_drop_219m_pnl_flip_loss_54k_jr2025"
assert (ROOT/f"docs/doge/foi/drafts/{GAP}.md").is_file()

def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)

NOTS=("NOT WZC Sint-Vincentius Erpe-Mere 0422.620.585 YE2024; NOT De Zonnewende 0735.627.214 remine; NOT Doppa remine; NOT Zorgbedrijf Vilvoorde OCMW; NOT Sint-Anna Herentals OCMW; NOT An for All CommV commercial; NOT ZENITH BV commercial; NOT Studijo Bos CV no YE2025; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine leftover-via-VE Gent")

append_lines(DATA/"sources.csv", [
f"{SRC_PDF},NBB VOL-VZW jaarrekening 2025 Avondzon Erpe-Mere deposit 2026-00283016,http://cdn.staatsbladmonitor.be/2026pdf/2026-00283016.pdf,NBB official WVV deposit PDF via CDN,{DAY},budget,tick2494; official native statutory PDF 3089772 bytes 44p VOL-VZW 26.0.15 m05-f; header 10.07.2026; AV 24.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-13 07:04:10 UTC OpenPDF 1.3.26; CDN Last-Modified 30.07.2026; statutory pages native; CDN 2026-00283016 GET 200 3089772 MD5 dcc85424deb07dcadc5364b2a186b781; official NBB UUID b1f510be-7c58-11f1-80db-a734674e7150; VOL-VZW 6.1 6.2.1 6.2.3 6.2.4 6.4.1-3 6.5.1-3 6.14 6.16 niet dienstig; prior-year identical not restated; commissaris NV Callens Vandelanotte / Roef Mathias; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Avondzon Erpe 0419.044.057,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0419044057,KBO Public Search FOD Economie,{DAY},official_register,tick2494; Actief; 1 VE leftover city_erpe_mere (zetel Botermelkstraat 12 9420 Erpe-Mere since 23.03.1996); VZW since 28.10.1978; RSZ2025 87.101; FOI info@avondzon.be; leftover mined city_erpe_mere WZC after leftover-type hunt; NOT WZC Sint-Vincentius Erpe-Mere YE2024; NOT De Zonnewende remine",
f"{SRC_SBM},NBB Consult / SBM fiche Avondzon 0419044057 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0419044057,NBB Consult / SBM,{DAY},official_register,tick2494; deposit-id 2026-00283016 YE 01.01.2025-31.12.2025 filing VOL-VZW Initial UUID b1f510be-7c58-11f1-80db-a734674e7150; NBB published-deposits/ids + broker PDF used for deposit-id discovery; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
f"{SRC_SITE},Avondzon Erpe-Mere FOI contact leftover city_erpe_mere WZC,https://avondzon.be/,Avondzon VZW leftover city_erpe_mere WZC 1 VE,{DAY},foi_contact,tick2494; FOI info@avondzon.be; PDF kt@avondzon.be; zetel Botermelkstraat 12 9420 Erpe-Mere; RSZ2025 87.101 WZC/RVT; leftover mined city_erpe_mere WZC; NOT WZC Sint-Vincentius Erpe-Mere YE2024; NOT De Zonnewende remine; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},Avondzon Erpe,ASBL Avondzon Erpe,Avondzon VZW (leftover city_erpe_mere WZC),parastatal,city_erpe_mere,nl,https://avondzon.be/,info@avondzon.be,Botermelkstraat 12 9420 Erpe-Mere,tick2494 YE2025 Strong official native NBB PDF deposit 2026-00283016 + Strong KBO 0419.044.057 Actief 1 VE; omzet70 JUMP 11741711 material not commercial-only; 73 DROP 2192121; 76A DROP 76278; envelope omzet70 JUMP 11741711; pnl FLIP LOSS 54204; 9901 DROP 127652; equity DROP 9411942; assets DROP 24696447; debt DROP 15284505; FTE DROP 141.3; kapitaalsubsidies DROP 50886; destin691 empty; 791 empty; cash DROP 547038; geldbeleggingen JUMP 941385; leftover city_erpe_mere WZC 1 VE; prior-year identical; {NOTS}; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_avondzon_omzet_jr2025_statutory,{EID},2025,11741711,11741711,11741711,NBB VOL-VZW code 70 omzet YE2025 JUMP +0.69% (material not commercial-only),{SRC_PDF},strong,tick2494; PDF p6 native; YE2024 11661740; 6.9 WZC+DVC 9171930 / AW 2569780",
f"bud_avondzon_73_jr2025_statutory,{EID},2025,2192121,2192121,2192121,NBB VOL-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 DROP -1.49%,{SRC_PDF},strong,tick2494; PDF p6 native; YE2024 2229265; 733 2192121; FOI RIZIV/VL matrix behind omzet+73",
f"bud_avondzon_opbr_jr2025_statutory,{EID},2025,11741711,11741711,11741711,NBB VOL-VZW envelope omzet 70 YE2025 JUMP +0.69% (VZW because omzet material not commercial-only),{SRC_PDF},strong,tick2494; PDF p6 native; YE2024 11661740; 70/76A 14259492 JUMP; 76A DROP 76278",
f"bud_avondzon_76A_jr2025_statutory,{EID},2025,76278,76278,76278,NBB VOL-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 DROP -27.19%,{SRC_PDF},strong,tick2494; PDF p6 native; YE2024 104759",
f"bud_avondzon_pnl_jr2025_statutory,{EID},2025,-54204,-54204,-54204,NBB VOL-VZW code 9904 winst van het boekjaar YE2025 FLIP LOSS (was +540121),{SRC_PDF},strong,tick2494; PDF p7 native; YE2024 540121; bedrijfswinst 9901 127652 DROP; destin691 empty",
f"bud_avondzon_bedrijfswinst_jr2025_statutory,{EID},2025,127652,127652,127652,NBB VOL-VZW code 9901 bedrijfswinst YE2025 DROP -83.10%,{SRC_PDF},strong,tick2494; PDF p6 native; YE2024 755117; 62 8783930 JUMP; 630 1606910 JUMP; 66A 38009 JUMP; 640/8 107368 DROP; 635/9 empty; 631/4 10815 DROP",
f"bud_avondzon_equity_jr2025_statutory,{EID},2025,9411942,9411942,9411942,NBB VOL-VZW code 10/15 eigen vermogen YE2025 DROP -0.72%,{SRC_PDF},strong,tick2494; PDF p5 native; YE2024 9480521; kapitaalsubsidies 15 50886 DROP; overgedragen 14 6269616 DROP; fondsen 10 31641 FLAT; bestemde fondsen 13 3059799 FLAT",
f"bud_avondzon_assets_jr2025_statutory,{EID},2025,24696447,24696447,24696447,NBB VOL-VZW code 20/58 totaal activa YE2025 DROP -4.67%,{SRC_PDF},strong,tick2494; PDF p4 native; YE2024 25907826; MVA 22/27 21519498 DROP; cash 547038 DROP; geldbeleggingen 941385 JUMP; aanbouw 27 6542 JUMP",
f"bud_avondzon_debt_jr2025_statutory,{EID},2025,15284505,15284505,15284505,NBB VOL-VZW code 17/49 schulden YE2025 DROP -6.95%,{SRC_PDF},strong,tick2494; PDF p5 native; YE2024 16427306; 17 11822926 DROP; 42/48 3448894 JUMP",
f"bud_avondzon_cash_jr2025_statutory,{EID},2025,547038,547038,547038,NBB VOL-VZW code 54/58 liquide middelen YE2025 DROP -19.92%,{SRC_PDF},strong,tick2494; PDF p4 native; YE2024 683131; geldbeleggingen 50/53 941385 JUMP; capex 360865",
f"bud_avondzon_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VOL-VZW code 691 toevoeging bestemde fondsen YE2025 empty (791 empty; 13 FLAT 3059799),{SRC_PDF},strong,tick2494; PDF p8 native; YE2024 destin empty; 791 empty; 14 DROP 6269616; fondsen 10 31641 FLAT",
])
print("entities+budgets ok")

cash_json=(
"\"{\"\"2025_omzet\"\":11741711,\"\"2025_73\"\":2192121,\"\"2025_76A\"\":76278,"
"\"\"2025_opbr7076A\"\":14259492,\"\"2025_bruto9900\"\":0,"
"\"\"2025_pnl\"\":-54204,\"\"2025_bedrijfswinst\"\":127652,"
"\"\"2025_equity\"\":9411942,\"\"2025_assets\"\":24696447,\"\"2025_debt\"\":15284505,"
"\"\"2025_fte\"\":141.3,\"\"2025_kapitaalsubsidies\"\":50886,\"\"2025_destin691\"\":0,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":547038,\"\"2025_geldbeleggingen\"\":941385,"
"\"\"2025_personnel62\"\":8783930,\"\"2025_gebouwen22\"\":12848600,"
"\"\"2025_aanbouw27\"\":6542,\"\"2025_66A\"\":38009,\"\"2025_66B\"\":0,"
"\"\"2025_fondsen10\"\":31641,\"\"2025_overgedragen14\"\":6269616,"
"\"\"2025_bestemdefondsen13\"\":3059799,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":1606910,\"\"2025_capex\"\":360865,"
"\"\"2025_6408\"\":107368,\"\"2025_74\"\":249382,\"\"2025_9903\"\":-54204,"
"\"\"2024_omzet\"\":11661740,\"\"2024_73\"\":2229265,"
"\"\"2024_opbr7076A\"\":14190587,\"\"2024_bruto9900\"\":0,\"\"2024_pnl\"\":540121,\"\"2024_bedrijfswinst\"\":755117,"
"\"\"2024_equity\"\":9480521,\"\"2024_assets\"\":25907826,"
"\"\"2024_debt\"\":16427306,\"\"2024_cash\"\":683131,\"\"2024_fte\"\":141.9,"
"\"\"2024_destin691\"\":0,\"\"2024_kapitaalsubsidies\"\":65261,\"\"2024_76A\"\":104759,"
"\"\"2024_geldbeleggingen\"\":929251}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Avondzon Erpe YE2025 (omzet JUMP 11.74m / 73 DROP 2.19m / pnl FLIP LOSS 54k / Strong PDF),{EID},WZC + leftover city_erpe_mere WZC,Avondzon VZW (KBO 0419.044.057; Actief; 1 VE; zetel Erpe-Mere),2026-06-24,2025,2025,11741711,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00283016.pdf,Public WZC dual of mined city_erpe_mere,Publish RIZIV/VL/gemeente matrix behind omzet 11.74m + 73 2.19m and why pnl FLIP LOSS 54204 after YE2024 profit 540121,{SRC_PDF},strong,Vlaanderen>Oost-Vlaanderen>Erpe-Mere>Avondzon>JR2025_statutory_L5,tick2494; Strong official native PDF; leftover mined city_erpe_mere WZC; 1 VE; prior-year identical; NOT WZC Sint-Vincentius Erpe-Mere YE2024; NOT De Zonnewende remine; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"Avondzon omzet JUMP 11.74m / 73 DROP 2.19m / pnl FLIP LOSS 54k (YE2025 leftover city_erpe_mere WZC)",
"L5",
"wzc_vzw_statutory",
"Vlaanderen>Oost-Vlaanderen>Erpe-Mere>Avondzon>JR2025",
"11741711",
"11741711",
"PDF envelope 11741711 = omzet 70 material not commercial-only; 73 DROP 2192121; 76A DROP 76278; 70/76A 14259492; bedrijfswinst DROP 127652; pnl FLIP LOSS 54204; equity DROP 9411942; assets DROP 24696447; debt DROP 15284505; FTE 141.3; kapitaalsubsidies DROP 50886; destin691 empty; cash DROP 547038; capex 360865; leftover city_erpe_mere WZC",
"strong",
SRC_PDF,
"WZC + leftover city_erpe_mere WZC",
"WZC leftover city_erpe_mere",
"11.74m omzet; 73 DROP 2.19m; pnl FLIP LOSS 54k; leftover city_erpe_mere WZC",
"5.60",
"5.50",
"5.10",
"5.54",
"FOI RIZIV/VL/gemeente matrix behind omzet 11.74m + 73 2.19m and why pnl FLIP LOSS 54204 after YE2024 profit 540121 while destin empty and cash DROP 547038",
"active",
"",
"tick2494 leftover mined city_erpe_mere WZC after leftover-type hunt; 1 VE; prior-year identical; NOT every-10 (next 2500); NOT WZC Sint-Vincentius Erpe-Mere YE2024; NOT De Zonnewende remine; NOT Doppa remine; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine",
])
assert len(next(csv.reader(StringIO(row))))==21
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Erpe-Mere>Avondzon>WZC",
"entity_id": EID,
"what_is_missing": "RIZIV / Vlaamse overheid / zorgkas / gemeente Erpe-Mere / eigen bijdragen split behind omzet 70 11741711 (6.9 WZC+DVC 9171930 / AW 2569780) + 73 2192121 and why pnl FLIP LOSS 54204 after YE2024 profit 540121 while destin 691 empty and cash DROP 547038",
"why_it_matters": "Strong official PDF leftover public WZC of mined city_erpe_mere; VOL-VZW envelope omzet 11.74m material not commercial-only; public RVT 1 VE; pnl FLIP to LOSS after 540k profit; cash DROP 19.92%",
"priority": "8",
"recipient_body": "Avondzon Erpe VZW / Raad van Bestuur",
"recipient_email": "info@avondzon.be",
"recipient_postal": "Botermelkstraat 12 9420 Erpe-Mere",
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
"notes": "tick2494; ready NOT sent; Strong official native NBB PDF; leftover mined city_erpe_mere WZC after leftover-type hunt; 1 VE; prior-year identical; NOT every-10 (next 2500); off WZC Sint-Vincentius Erpe-Mere YE2024; off De Zonnewende remine; off Doppa remine; off leftover-via-VE; off Armonea commercial; off Vulpia commercial; off Korian commercial",
}
foi_path=DATA/"foi_queue.csv"
raw=foi_path.read_bytes()
if not raw.endswith(b"\n"): raise SystemExit("foi_queue no LF")
with foi_path.open("a", newline="", encoding="utf-8") as f:
    w=csv.DictWriter(f, fieldnames=list(foi_row.keys()), extrasaction="raise", lineterminator="\n")
    w.writerow(foi_row)
print("foi_queue ok")
print("CORE APPEND DONE")
