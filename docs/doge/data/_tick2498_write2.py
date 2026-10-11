from pathlib import Path
import csv
from io import StringIO
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2498_stamp.txt").read_text().strip().splitlines()
SRC_PDF="src_meredal_jr2025_nbb_pdf_2498"
EID="vzw_meredal_erpe_mere"
GAP="gap_meredal_erpe_mere_wzc_matrix_omzet_8_22m_73_drop_1_09m_pnl_drop_185k_cash_drop_1_32m_l5"
COMM="comm_meredal_jr2025_statutory_omzet_8_22m_73_drop_1_09m_pnl_drop_185k"
LB="lb_meredal_omzet_822m_73_drop_109m_pnl_drop_185k_cash_drop_132m_jr2025"

def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)

cash_json=(
"\"{\"\"2025_omzet\"\":8224110,\"\"2025_73\"\":1091421,\"\"2025_76A\"\":10,"
"\"\"2025_opbr7076A\"\":9464409,\"\"2025_bruto9900\"\":0,"
"\"\"2025_pnl\"\":185241,\"\"2025_bedrijfswinst\"\":374227,"
"\"\"2025_equity\"\":10586696,\"\"2025_assets\"\":20590835,\"\"2025_debt\"\":9571459,"
"\"\"2025_fte\"\":92.4,\"\"2025_kapitaalsubsidies\"\":0,\"\"2025_destin691\"\":185241,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":1316785,\"\"2025_geldbeleggingen\"\":4081030,"
"\"\"2025_personnel62\"\":6737249,\"\"2025_gebouwen22\"\":14399163,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":867,\"\"2025_66B\"\":0,"
"\"\"2025_fondsen10\"\":2905934,\"\"2025_overgedragen14\"\":0,"
"\"\"2025_bestemdefondsen13\"\":7680762,"
"\"\"2025_voorzieningen16\"\":432680,\"\"2025_630\"\":715291,\"\"2025_capex\"\":63438,"
"\"\"2025_6408\"\":5815,\"\"2025_74\"\":148869,\"\"2025_9903\"\":214719,"
"\"\"2024_omzet\"\":7969825,\"\"2024_73\"\":1185364,"
"\"\"2024_opbr7076A\"\":9388410,\"\"2024_bruto9900\"\":0,\"\"2024_pnl\"\":766756,\"\"2024_bedrijfswinst\"\":946927,"
"\"\"2024_equity\"\":10402887,\"\"2024_assets\"\":21266694,"
"\"\"2024_debt\"\":10431127,\"\"2024_cash\"\":2945791,\"\"2024_fte\"\":89.3,"
"\"\"2024_destin691\"\":766756,\"\"2024_kapitaalsubsidies\"\":1432,\"\"2024_76A\"\":54715,"
"\"\"2024_geldbeleggingen\"\":2499170}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Meredal YE2025 (omzet JUMP 8.22m / 73 DROP 1.09m / pnl DROP 185k / cash DROP 1.32m / Strong PDF),{EID},WZC + leftover city_erpe_mere WZC,Meredal VZW (KBO 0419.333.671; Actief; 1 VE; official zetel Erpe-Mere),2026-04-29,2025,2025,8224110,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00108199.pdf,Public WZC dual of mined city_erpe_mere,Publish RIZIV/VL/zorgkas/gemeente matrix behind omzet 8.22m + 73 1.09m and why pnl DROP 185k while cash DROP 1.32m,{SRC_PDF},strong,Vlaanderen>Oost-Vlaanderen>Erpe-Mere>Meredal>JR2025_statutory_L5,tick2498; Strong official native PDF; leftover mined city_erpe_mere WZC; 1 VE; prior-year identical; NOT Avondzon remine; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"Meredal omzet JUMP 8.22m / 73 DROP 1.09m / pnl DROP 185k / cash DROP 1.32m (YE2025 leftover city_erpe_mere WZC)",
"L5",
"wzc_vzw_statutory",
"Vlaanderen>Oost-Vlaanderen>Erpe-Mere>Meredal>JR2025",
"8224110",
"8224110",
"PDF envelope 8224110 = omzet 70 material not commercial-only; 73 DROP 1091421; 76A DROP 10; 70/76A 9464409; bedrijfswinst DROP 374227; pnl DROP 185241; equity JUMP 10586696; assets DROP 20590835; debt DROP 9571459; FTE 92.4; kapitaalsubsidies DROP 0; destin691 DROP 185241; cash DROP 1316785; capex 63438; leftover city_erpe_mere WZC",
"strong",
SRC_PDF,
"WZC + leftover city_erpe_mere WZC",
"WZC leftover city_erpe_mere",
"8.22m omzet; 73 DROP 1.09m; pnl DROP 185k; cash DROP 1.32m; leftover city_erpe_mere WZC",
"5.50",
"5.40",
"5.10",
"5.44",
"FOI RIZIV/VL/zorgkas/gemeente matrix behind omzet 8.22m + 73 1.09m and why pnl DROP 185241 after YE2024 profit 766756 while cash DROP 1316785 and geldbeleggingen JUMP 4081030",
"active",
"",
"tick2498 leftover mined city_erpe_mere WZC after leftover-type hunt; 1 VE; prior-year identical; NOT every-10 (next 2500); NOT Avondzon remine; NOT WZC Sint-Vincentius Erpe-Mere YE2024; NOT Maria Boodschap absorbed; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine",
])
assert len(next(csv.reader(StringIO(row))))==21
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Erpe-Mere>Meredal>WZC",
"entity_id": EID,
"what_is_missing": "RIZIV / Vlaamse overheid / zorgkas / gemeente Erpe-Mere / eigen bijdragen / assistentiewoningen De Merelaar+De Valeriaan split behind omzet 70 8224110 + 73 1091421 (733 1091371) and why pnl DROP 185241 while cash DROP 1316785 and geldbeleggingen JUMP 4081030",
"why_it_matters": "Strong official PDF leftover public WZC of mined city_erpe_mere; VOL-VZW envelope omzet 70 8.22m because omzet material not commercial-only; public WZC 1 VE (official zetel Erpe-Mere); pnl DROP 185k; cash DROP 1.32m",
"priority": "8",
"recipient_body": "MEREDAL VZW / Raad van Bestuur",
"recipient_email": "administratie@wzcmeredal.be",
"recipient_postal": "Vijverstraat 38 9420 Erpe-Mere",
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
"notes": "tick2498; ready NOT sent; Strong official native NBB PDF; leftover mined city_erpe_mere WZC after leftover-type hunt; 1 VE; prior-year identical; NOT every-10 (next 2500); off Avondzon remine; off WZC Sint-Vincentius YE2024; off Maria Boodschap absorbed; off leftover-via-VE; off Armonea commercial; off Vulpia commercial; off Korian commercial",
}
foi_path=DATA/"foi_queue.csv"
raw=foi_path.read_bytes()
if not raw.endswith(b"\n"): raise SystemExit("foi_queue no LF")
with foi_path.open("a", newline="", encoding="utf-8") as f:
    w=csv.DictWriter(f, fieldnames=list(foi_row.keys()), extrasaction="raise", lineterminator="\n")
    w.writerow(foi_row)
print("foi_queue ok")
print("CORE2 DONE")
