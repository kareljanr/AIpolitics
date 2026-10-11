from pathlib import Path
import csv
from io import StringIO
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2495_stamp.txt").read_text().strip().splitlines()
SRC_PDF="src_trento_jr2025_nbb_pdf_2495"
EID="vzw_zorgnetwerk_trento_hamme"
GAP="gap_trento_hamme_wzc_matrix_omzet_13_43m_73_jump_3_05m_destin_jump_2_30m_cash_drop_1_92m_l5"
COMM="comm_trento_jr2025_statutory_omzet_13_43m_73_jump_3_05m_destin_jump_2_30m"
LB="lb_trento_omzet_1343m_73_jump_305m_destin_jump_230m_jr2025"

def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)

cash_json=(
"\"{\"\"2025_omzet\"\":13434174,\"\"2025_73\"\":3051871,\"\"2025_76A\"\":0,"
"\"\"2025_opbr7076A\"\":17021630,\"\"2025_bruto9900\"\":0,"
"\"\"2025_pnl\"\":362341,\"\"2025_bedrijfswinst\"\":331288,"
"\"\"2025_equity\"\":13774142,\"\"2025_assets\"\":19824343,\"\"2025_debt\"\":6050201,"
"\"\"2025_fte\"\":186.5,\"\"2025_kapitaalsubsidies\"\":534830,\"\"2025_destin691\"\":2300000,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":1921671,\"\"2025_geldbeleggingen\"\":5290614,"
"\"\"2025_personnel62\"\":12989805,\"\"2025_gebouwen22\"\":9371432,"
"\"\"2025_aanbouw27\"\":50499,\"\"2025_66A\"\":1418,\"\"2025_66B\"\":0,"
"\"\"2025_fondsen10\"\":3119608,\"\"2025_overgedragen14\"\":4161237,"
"\"\"2025_bestemdefondsen13\"\":5958466,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":900836,\"\"2025_capex\"\":328573,"
"\"\"2025_6408\"\":35371,\"\"2025_74\"\":535584,\"\"2025_9903\"\":359992,"
"\"\"2024_omzet\"\":12674723,\"\"2024_73\"\":2813385,"
"\"\"2024_opbr7076A\"\":15883901,\"\"2024_bruto9900\"\":0,\"\"2024_pnl\"\":68230,\"\"2024_bedrijfswinst\"\":16482,"
"\"\"2024_equity\"\":13556686,\"\"2024_assets\"\":20140114,"
"\"\"2024_debt\"\":6583428,\"\"2024_cash\"\":2799148,\"\"2024_fte\"\":192.3,"
"\"\"2024_destin691\"\":68230,\"\"2024_kapitaalsubsidies\"\":679715,\"\"2024_76A\"\":1000,"
"\"\"2024_geldbeleggingen\"\":4425451}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Zorgnetwerk Trento YE2025 (omzet JUMP 13.43m / 73 JUMP 3.05m / destin JUMP 2.30m / cash DROP 1.92m / Strong PDF),{EID},WZC + leftover city_hamme WZC,Zorgnetwerk Trento VZW (KBO 0455.449.048; Actief; 2 VE; zetel Hamme),2026-06-24,2025,2025,13434174,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00304248.pdf,Public WZC dual of mined city_hamme,Publish RIZIV/VL/gemeente matrix behind omzet 13.43m + 73 3.05m and why destin JUMP 2.30m while cash DROP 1.92m,{SRC_PDF},strong,Vlaanderen>Oost-Vlaanderen>Hamme>Trento>JR2025_statutory_L5,tick2495; Strong official native PDF; leftover mined city_hamme WZC; 2 VE; prior-year identical; NOT leftover city_zele; NOT De Vlietoever BV; NOT Woonzorg Samen Ouder remine; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"Trento omzet JUMP 13.43m / 73 JUMP 3.05m / destin JUMP 2.30m / cash DROP 1.92m (YE2025 leftover city_hamme WZC)",
"L5",
"wzc_vzw_statutory",
"Vlaanderen>Oost-Vlaanderen>Hamme>Trento>JR2025",
"13434174",
"13434174",
"PDF envelope 13434174 = omzet 70 material not commercial-only; 73 JUMP 3051871; 76A empty; 70/76A 17021630; bedrijfswinst JUMP 331288; pnl JUMP 362341; equity JUMP 13774142; assets DROP 19824343; debt DROP 6050201; FTE 186.5; kapitaalsubsidies DROP 534830; destin691 JUMP 2300000; cash DROP 1921671; capex 328573; leftover city_hamme WZC",
"strong",
SRC_PDF,
"WZC + leftover city_hamme WZC",
"WZC leftover city_hamme",
"13.43m omzet; 73 JUMP 3.05m; destin JUMP 2.30m; cash DROP 1.92m; leftover city_hamme WZC",
"5.60",
"5.55",
"5.15",
"5.56",
"FOI RIZIV/VL/gemeente matrix behind omzet 13.43m + 73 3.05m and why destin JUMP 2300000 after YE2024 68230 while cash DROP 1921671",
"active",
"",
"tick2495 leftover mined city_hamme WZC after leftover-type hunt; 2 VE; prior-year identical; NOT every-10 (next 2500); NOT leftover city_zele; NOT De Vlietoever BV; NOT Woonzorg Samen Ouder remine; NOT Avondzon remine; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine",
])
assert len(next(csv.reader(StringIO(row))))==21
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Hamme>Trento>WZC",
"entity_id": EID,
"what_is_missing": "RIZIV / Vlaamse overheid / zorgkas / gemeente Hamme / gemeente Zele / eigen bijdragen split behind omzet 70 13434174 + 73 3051871 (733 3025798) and why destin 691 JUMP 2300000 after YE2024 68230 while cash DROP 1921671",
"why_it_matters": "Strong official PDF leftover public WZC of mined city_hamme; VOL-VZW envelope omzet 13.43m material not commercial-only; public ROB 2 VE (Hamme + Zele); destin JUMP 2.30m; cash DROP 31.35%",
"priority": "8",
"recipient_body": "Zorgnetwerk Trento VZW / Raad van Bestuur",
"recipient_email": "info@zorgnetwerktrento.be",
"recipient_postal": "Molenstraat 11 9220 Hamme",
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
"notes": "tick2495; ready NOT sent; Strong official native NBB PDF; leftover mined city_hamme WZC after leftover-type hunt; 2 VE; prior-year identical; NOT every-10 (next 2500); off leftover city_zele; off De Vlietoever BV; off Woonzorg Samen Ouder remine; off Avondzon remine; off leftover-via-VE; off Armonea commercial; off Vulpia commercial; off Korian commercial",
}
foi_path=DATA/"foi_queue.csv"
raw=foi_path.read_bytes()
if not raw.endswith(b"\n"): raise SystemExit("foi_queue no LF")
with foi_path.open("a", newline="", encoding="utf-8") as f:
    w=csv.DictWriter(f, fieldnames=list(foi_row.keys()), extrasaction="raise", lineterminator="\n")
    w.writerow(foi_row)
print("foi_queue ok")
print("CORE2 DONE")
