from pathlib import Path
import csv
from io import StringIO
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2493_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_doppa_jr2025_nbb_pdf_2493"
SRC_KBO="src_doppa_kbo_2493"
SRC_SBM="src_doppa_sbm_2493"
SRC_SITE="src_doppa_site_2493"
EID="vzw_doppa_zoersel"
GAP="gap_doppa_zoersel_vaph_matrix_bruto_2_54m_omzet73_empty_pnl_flip_loss_106k_l5"
COMM="comm_doppa_jr2025_statutory_bruto_2_54m_omzet73_empty_pnl_flip_loss_106k"
LB="lb_doppa_bruto_254m_omzet73_empty_pnl_flip_loss_106k_jr2025"
assert (ROOT/f"docs/doge/foi/drafts/{GAP}.md").is_file()

def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)

NOTS=("NOT AGB Zoersel remine; NOT WZC Joostens Zorgbedrijf Antwerpen commercial; NOT Halmolen Vulpia commercial; NOT 3Wplus Werk 0467.004.520 remine tick2492; NOT Hopperank 0434.363.921 remine tick2491; NOT Foyer De Lork remine; NOT MPI Oosterlo remine; NOT De Sperwer remine; NOT Alderande remine; NOT De Hagewinde remine; NOT AMAB remine; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine leftover-via-VE Gent")

append_lines(DATA/"sources.csv", [
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Doppa Zoersel deposit 2026-00172866,http://cdn.staatsbladmonitor.be/2026pdf/2026-00172866.pdf,NBB official WVV deposit PDF via CDN,{DAY},budget,tick2493; official native statutory PDF 50888 bytes 13p VKT-VZW 26.0.15 m04-f; header 16.06.2026; AV 08.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-06-18 22:15:57 UTC OpenPDF 1.3.26; CDN Last-Modified 22.06.2026; statutory pages native; CDN 2026-00172866 GET 200 50888 MD5 328f7082865c74385115660898ea66dc; official NBB UUID 54a001b8-6992-11f1-ba33-47adf9e6d406; VKT-VZW 6.1.1 6.3 6.5 6.6 7 8 niet dienstig; prior-year identical not restated; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Doppa Zoersel 0836.745.160,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0836745160,KBO Public Search FOD Economie,{DAY},official_register,tick2493; Actief; 1 VE leftover city_zoersel (Zandstraat 46 2980 Zoersel VE 2.204.301.838 TRAJECT since 01.12.2011); zetel Zandstraat 46 2980 Zoersel since 02.12.2024; VZW since 30.03.2011; RSZ2025 88.106; FOI info@doppa.be; leftover mined city_zoersel VAPH after leftover-type hunt; NOT AGB Zoersel remine; NOT Joostens commercial; NOT Halmolen Vulpia commercial",
f"{SRC_SBM},NBB Consult / SBM fiche Doppa 0836745160 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0836745160,NBB Consult / SBM,{DAY},official_register,tick2493; deposit-id 2026-00172866 YE 01.01.2025-31.12.2025 filing VKT-VZW Initial UUID 54a001b8-6992-11f1-ba33-47adf9e6d406; NBB published-deposits/ids + broker PDF used for deposit-id discovery; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
f"{SRC_SITE},Doppa Zoersel FOI contact leftover city_zoersel VAPH,https://doppa.be/,Doppa VZW leftover city_zoersel VAPH 1 VE,{DAY},foi_contact,tick2493; FOI info@doppa.be; zetel Zandstraat 46 2980 Zoersel; RSZ2025 88.106 Dienst Ondersteuningsplan; leftover mined city_zoersel VAPH; NOT AGB Zoersel remine; NOT Joostens commercial; NOT Halmolen Vulpia commercial; NOT 3Wplus Werk remine; NOT Hopperank remine; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},Doppa,ASBL Doppa,Doppa VZW (leftover city_zoersel VAPH),parastatal,city_zoersel,nl,https://doppa.be/,info@doppa.be,Zandstraat 46 2980 Zoersel,tick2493 YE2025 Strong official native NBB PDF deposit 2026-00172866 + Strong KBO 0836.745.160 Actief 1 VE; omzet70 empty VKT; 73 empty VKT; 76A DROP 3510; envelope bruto9900 DROP 2540982; pnl FLIP LOSS 106107; 9901 FLIP LOSS 123586; equity DROP 1531949; assets DROP 1891357; debt DROP 359408; FTE DROP 32; kapitaalsubsidies empty; destin691 empty; 791 empty; cash JUMP 88271; geldbeleggingen DROP 881350; leftover city_zoersel VAPH 1 VE; prior-year identical; {NOTS}; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_doppa_omzet_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 70 omzet YE2025 empty VKT,{SRC_PDF},strong,tick2493; PDF p5 native; YE2024 empty; 73 empty; 76A DROP 3510",
f"bud_doppa_73_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 empty VKT,{SRC_PDF},strong,tick2493; PDF p5 native; YE2024 empty; FOI VAPH/PVF matrix behind bruto",
f"bud_doppa_opbr_jr2025_statutory,{EID},2025,2540982,2540982,2540982,NBB VKT-VZW envelope bruto 9900 YE2025 DROP -4.30% (VKT because omzet empty),{SRC_PDF},strong,tick2493; PDF p5 native; YE2024 2655050; 70 empty; 73 empty; 76A DROP 3510",
f"bud_doppa_76A_jr2025_statutory,{EID},2025,3510,3510,3510,NBB VKT-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 DROP -97.67%,{SRC_PDF},strong,tick2493; PDF p5 native; YE2024 150706",
f"bud_doppa_pnl_jr2025_statutory,{EID},2025,-106107,-106107,-106107,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 FLIP LOSS (was +40968),{SRC_PDF},strong,tick2493; PDF p5 native; YE2024 40968; bedrijfswinst 9901 -123586 FLIP LOSS; destin691 empty",
f"bud_doppa_bedrijfswinst_jr2025_statutory,{EID},2025,-123586,-123586,-123586,NBB VKT-VZW code 9901 bedrijfswinst YE2025 FLIP LOSS (was +17384),{SRC_PDF},strong,tick2493; PDF p5 native; YE2024 17384; 62 2608339 JUMP; 630 36698 JUMP; 66A 2676 JUMP; 640/8 16855 DROP; 635/9 empty; 631/4 empty",
f"bud_doppa_equity_jr2025_statutory,{EID},2025,1531949,1531949,1531949,NBB VKT-VZW code 10/15 eigen vermogen YE2025 DROP -6.48%,{SRC_PDF},strong,tick2493; PDF p4 native; YE2024 1638056; kapitaalsubsidies 15 empty; overgedragen 14 936340 DROP; fondsen 10 25034 FLAT; bestemde fondsen 13 570575 FLAT",
f"bud_doppa_assets_jr2025_statutory,{EID},2025,1891357,1891357,1891357,NBB VKT-VZW code 20/58 totaal activa YE2025 DROP -7.57%,{SRC_PDF},strong,tick2493; PDF p3 native; YE2024 2046238; MVA 22/27 855294 DROP; cash 88271 JUMP; geldbeleggingen 881350 DROP; aanbouw 27 empty",
f"bud_doppa_debt_jr2025_statutory,{EID},2025,359408,359408,359408,NBB VKT-VZW code 17/49 schulden YE2025 DROP -11.95%,{SRC_PDF},strong,tick2493; PDF p4 native; YE2024 408182; 17 empty; 42/48 356156 DROP",
f"bud_doppa_cash_jr2025_statutory,{EID},2025,88271,88271,88271,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +12.79%,{SRC_PDF},strong,tick2493; PDF p3 native; YE2024 78259; geldbeleggingen 50/53 881350 DROP; capex 8169 23080",
f"bud_doppa_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty (791 empty; 13 FLAT 570575),{SRC_PDF},strong,tick2493; PDF p6 native; YE2024 destin empty; 791 empty; 14 DROP 936340; fondsen 10 25034 FLAT",
])
print("entities+budgets ok")

cash_json=(
"\"{\"\"2025_omzet\"\":0,\"\"2025_73\"\":0,\"\"2025_76A\"\":3510,"
"\"\"2025_opbr7076A\"\":0,\"\"2025_bruto9900\"\":2540982,"
"\"\"2025_pnl\"\":-106107,\"\"2025_bedrijfswinst\"\":-123586,"
"\"\"2025_equity\"\":1531949,\"\"2025_assets\"\":1891357,\"\"2025_debt\"\":359408,"
"\"\"2025_fte\"\":32,\"\"2025_kapitaalsubsidies\"\":0,\"\"2025_destin691\"\":0,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":88271,\"\"2025_geldbeleggingen\"\":881350,"
"\"\"2025_personnel62\"\":2608339,\"\"2025_gebouwen22\"\":832430,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":2676,\"\"2025_66B\"\":0,"
"\"\"2025_fondsen10\"\":25034,\"\"2025_overgedragen14\"\":936340,"
"\"\"2025_bestemdefondsen13\"\":570575,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":36698,\"\"2025_capex\"\":23080,"
"\"\"2025_6408\"\":16855,\"\"2025_75\"\":18435,\"\"2025_9903\"\":-106107,"
"\"\"2024_omzet\"\":0,\"\"2024_73\"\":0,"
"\"\"2024_opbr7076A\"\":0,\"\"2024_bruto9900\"\":2655050,\"\"2024_pnl\"\":40968,\"\"2024_bedrijfswinst\"\":17384,"
"\"\"2024_equity\"\":1638056,\"\"2024_assets\"\":2046238,"
"\"\"2024_debt\"\":408182,\"\"2024_cash\"\":78259,\"\"2024_fte\"\":33.6,"
"\"\"2024_destin691\"\":0,\"\"2024_kapitaalsubsidies\"\":0,\"\"2024_76A\"\":150706,"
"\"\"2024_geldbeleggingen\"\":988960}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Doppa YE2025 (bruto DROP 2.54m / omzet+73 empty VKT / pnl FLIP LOSS 106k / Strong PDF),{EID},VAPH + leftover city_zoersel VAPH,Doppa VZW (KBO 0836.745.160; Actief; 1 VE; zetel Zoersel),2026-06-08,2025,2025,2540982,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00172866.pdf,Public VAPH dual of mined city_zoersel,Publish VAPH/PVF matrix behind bruto 2.54m and why pnl FLIP LOSS 106107 after YE2024 profit 40968,{SRC_PDF},strong,Vlaanderen>Antwerpen>Zoersel>Doppa>JR2025_statutory_L5,tick2493; Strong official native PDF; leftover mined city_zoersel VAPH; 1 VE; prior-year identical; NOT AGB Zoersel remine; NOT Joostens commercial; NOT 3Wplus Werk remine; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"Doppa bruto DROP 2.54m / omzet+73 empty VKT / pnl FLIP LOSS 106k (YE2025 leftover city_zoersel VAPH)",
"L5",
"vaph_vzw_statutory",
"Vlaanderen>Antwerpen>Zoersel>Doppa>JR2025",
"2540982",
"2540982",
"PDF envelope 2540982 = bruto 9900 VKT because omzet empty; 70 empty; 73 empty; 76A DROP 3510; bedrijfswinst FLIP LOSS 123586; pnl FLIP LOSS 106107; equity DROP 1531949; assets DROP 1891357; debt DROP 359408; FTE 32; kapitaalsubsidies empty; destin691 empty; cash JUMP 88271; capex 23080; leftover city_zoersel VAPH",
"strong",
SRC_PDF,
"VAPH + leftover city_zoersel VAPH",
"VAPH leftover city_zoersel",
"2.54m bruto; omzet+73 empty VKT; pnl FLIP LOSS 106k; leftover city_zoersel VAPH",
"5.35",
"5.20",
"5.10",
"5.28",
"FOI VAPH/PVF matrix behind bruto 2.54m and why pnl FLIP LOSS 106107 after YE2024 profit 40968 while 76A DROP 3510 and FTE DROP 32",
"active",
"",
"tick2493 leftover mined city_zoersel VAPH after leftover-type hunt; 1 VE; prior-year identical; NOT every-10 (next 2500); NOT AGB Zoersel remine; NOT Joostens commercial; NOT Halmolen Vulpia commercial; NOT 3Wplus Werk remine; NOT Hopperank remine; NOT Foyer De Lork remine; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine",
])
assert len(next(csv.reader(StringIO(row))))==21
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>Antwerpen>Zoersel>Doppa>VAPH",
"entity_id": EID,
"what_is_missing": "VAPH / PVF / Vlaamse overheid / provincie Antwerpen / stad Zoersel split behind bruto 9900 2540982 (omzet 70 empty VKT; 73 empty VKT; 76A DROP 3510) and why pnl FLIP LOSS 106107 after YE2024 profit 40968 while destin 691 empty and 76A DROP 3510",
"why_it_matters": "Strong official PDF leftover public VAPH of mined city_zoersel; VKT envelope 2.54m because omzet empty; public Dienst Ondersteuningsplan 1 VE; pnl FLIP to LOSS; 76A DROP from 150706",
"priority": "8",
"recipient_body": "Doppa VZW / Raad van Bestuur",
"recipient_email": "info@doppa.be",
"recipient_postal": "Zandstraat 46 2980 Zoersel",
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
"notes": "tick2493; ready NOT sent; Strong official native NBB PDF; leftover mined city_zoersel VAPH after leftover-type hunt; 1 VE; prior-year identical; NOT every-10 (next 2500); off AGB Zoersel remine; off Joostens commercial; off Halmolen Vulpia commercial; off 3Wplus Werk remine; off Hopperank remine; off leftover-via-VE; off Armonea commercial; off Vulpia commercial; off Korian commercial",
}
foi_path=DATA/"foi_queue.csv"
raw=foi_path.read_bytes()
if not raw.endswith(b"\n"): raise SystemExit("foi_queue no LF")
with foi_path.open("a", newline="", encoding="utf-8") as f:
    w=csv.DictWriter(f, fieldnames=list(foi_row.keys()), extrasaction="raise", lineterminator="\n")
    w.writerow(foi_row)
print("foi_queue ok")
print("CORE APPEND DONE")
