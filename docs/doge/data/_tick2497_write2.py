from pathlib import Path
import csv
from io import StringIO
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2497_stamp.txt").read_text().strip().splitlines()
SRC_PDF="src_pegode_jr2025_nbb_pdf_2497"
EID="vzw_pegode_kontich"
GAP="gap_pegode_kontich_vaph_matrix_70_76A_18_11m_omzet_commercial_73_jump_15_32m_pnl_jump_630k_cash_jump_1_50m_l5"
COMM="comm_pegode_jr2025_statutory_70_76A_18_11m_73_jump_15_32m_pnl_jump_630k"
LB="lb_pegode_7076A_1811m_73_jump_1532m_pnl_jump_630k_jr2025"

def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)

cash_json=(
"\"{\"\"2025_omzet\"\":1914328,\"\"2025_73\"\":15317093,\"\"2025_76A\"\":741511,"
"\"\"2025_opbr7076A\"\":18110069,\"\"2025_bruto9900\"\":0,"
"\"\"2025_pnl\"\":629938,\"\"2025_bedrijfswinst\"\":610467,"
"\"\"2025_equity\"\":4856573,\"\"2025_assets\"\":8551945,\"\"2025_debt\"\":3480999,"
"\"\"2025_fte\"\":174.6,\"\"2025_kapitaalsubsidies\"\":285334,\"\"2025_destin691\"\":370649,"
"\"\"2025_791\"\":92286,\"\"2025_cash\"\":1497839,\"\"2025_geldbeleggingen\"\":1240218,"
"\"\"2025_personnel62\"\":14055244,\"\"2025_gebouwen22\"\":3635080,"
"\"\"2025_aanbouw27\"\":124098,\"\"2025_66A\"\":10235,\"\"2025_66B\"\":0,"
"\"\"2025_fondsen10\"\":1493063,\"\"2025_overgedragen14\"\":1880102,"
"\"\"2025_bestemdefondsen13\"\":1198073,"
"\"\"2025_voorzieningen16\"\":214373,\"\"2025_630\"\":441185,\"\"2025_capex\"\":739991,"
"\"\"2025_6408\"\":97415,\"\"2025_74\"\":137137,\"\"2025_9903\"\":629938,"
"\"\"2024_omzet\"\":1772665,\"\"2024_73\"\":14168896,"
"\"\"2024_opbr7076A\"\":16608499,\"\"2024_bruto9900\"\":0,\"\"2024_pnl\"\":101408,\"\"2024_bedrijfswinst\"\":36620,"
"\"\"2024_equity\"\":4221951,\"\"2024_assets\"\":8369495,"
"\"\"2024_debt\"\":4047469,\"\"2024_cash\"\":779025,\"\"2024_fte\"\":173.8,"
"\"\"2024_destin691\"\":317923,\"\"2024_kapitaalsubsidies\"\":280650,\"\"2024_76A\"\":345722,"
"\"\"2024_geldbeleggingen\"\":2308632}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Pegode YE2025 (70/76A JUMP 18.11m / 73 JUMP 15.32m / pnl JUMP 630k / cash JUMP 1.50m / Strong PDF),{EID},VAPH + leftover city_kontich VAPH,Pegode VZW (KBO 0420.281.501; Actief; 19 VE; official zetel Kontich),2026-06-18,2025,2025,18110069,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00293740.pdf,Public VAPH dual of mined city_kontich,Publish VAPH/VL/PVB/RTH/gemeente matrix behind 70/76A 18.11m + 73 15.32m and why pnl JUMP 630k while cash JUMP 1.50m,{SRC_PDF},strong,Vlaanderen>Antwerpen>Kontich>Pegode>JR2025_statutory_L5,tick2497; Strong official native PDF; leftover mined city_kontich VAPH; 19 VE; prior-year identical; NOT leftover city_niel; NOT leftover city_schilde; NOT Iris remine; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"Pegode 70/76A JUMP 18.11m / 73 JUMP 15.32m / pnl JUMP 630k / cash JUMP 1.50m (YE2025 leftover city_kontich VAPH)",
"L5",
"vaph_vzw_statutory",
"Vlaanderen>Antwerpen>Kontich>Pegode>JR2025",
"18110069",
"18110069",
"PDF envelope 18110069 = 70/76A VZW because omzet commercial-only vs large 73; omzet 1914328; 73 JUMP 15317093; 76A JUMP 741511; bedrijfswinst JUMP 610467; pnl JUMP 629938; equity JUMP 4856573; assets JUMP 8551945; debt DROP 3480999; FTE 174.6; kapitaalsubsidies JUMP 285334; destin691 JUMP 370649; cash JUMP 1497839; capex 739991; leftover city_kontich VAPH",
"strong",
SRC_PDF,
"VAPH + leftover city_kontich VAPH",
"VAPH leftover city_kontich",
"18.11m 70/76A; 73 JUMP 15.32m; pnl JUMP 630k; cash JUMP 1.50m; leftover city_kontich VAPH",
"5.68",
"5.58",
"5.18",
"5.64",
"FOI VAPH/VL/PVB/RTH/gemeente matrix behind 70/76A 18.11m + 73 15.32m and why pnl JUMP 629938 while cash JUMP 1497839 and 76A JUMP 741511",
"active",
"",
"tick2497 leftover mined city_kontich VAPH after leftover-type hunt; 19 VE; prior-year identical; NOT every-10 (next 2500); NOT leftover city_niel; NOT leftover city_schilde; NOT Iris remine; NOT De Dageraad remine; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine",
])
assert len(next(csv.reader(StringIO(row))))==21
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>Antwerpen>Kontich>Pegode>VAPH",
"entity_id": EID,
"what_is_missing": "VAPH / Vlaamse overheid / PVB / RTH / MFC / gemeente Kontich / gemeente Niel / andere VE-gemeenten / eigen bijdragen split behind omzet 70 1914328 + 73 15317093 (733 14997731) and why pnl JUMP 629938 while cash JUMP 1497839 and 76A JUMP 741511",
"why_it_matters": "Strong official PDF leftover public VAPH of mined city_kontich; VOL-VZW envelope 70/76A 18.11m because omzet commercial-only vs large 73; public VAPH 19 VE (official zetel Kontich; Niel is VE only); pnl JUMP 630k; cash JUMP 1.50m",
"priority": "8",
"recipient_body": "PEGODE VZW / Raad van Bestuur",
"recipient_email": "info@pegode.be",
"recipient_postal": "Antwerpsesteenweg 62 2550 Kontich",
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
"notes": "tick2497; ready NOT sent; Strong official native NBB PDF; leftover mined city_kontich VAPH after leftover-type hunt; 19 VE; prior-year identical; NOT every-10 (next 2500); off leftover city_niel; off leftover city_schilde; off Iris remine; off De Dageraad remine; off leftover-via-VE; off Armonea commercial; off Vulpia commercial; off Korian commercial",
}
foi_path=DATA/"foi_queue.csv"
raw=foi_path.read_bytes()
if not raw.endswith(b"\n"): raise SystemExit("foi_queue no LF")
with foi_path.open("a", newline="", encoding="utf-8") as f:
    w=csv.DictWriter(f, fieldnames=list(foi_row.keys()), extrasaction="raise", lineterminator="\n")
    w.writerow(foi_row)
print("foi_queue ok")
print("CORE2 DONE")
