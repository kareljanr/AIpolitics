from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2451_stamp.txt").read_text().strip().splitlines()
EID="vzw_hartjes_ninove"
SRC_PDF="src_hartjes_ninove_jr2025_nbb_pdf_2451"
COMM="comm_hartjes_ninove_jr2025_statutory_bruto_484k_omzet73_empty_pnl_jump_31k"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
cash_json=(
"\"{\"\"2025_omzet\"\":0,\"\"2025_73\"\":0,\"\"2025_76A\"\":0,"
"\"\"2025_bruto\"\":483796,"
"\"\"2025_pnl\"\":31142,\"\"2025_bedrijfswinst\"\":21273,"
"\"\"2025_equity\"\":437479,\"\"2025_assets\"\":478634,\"\"2025_debt\"\":41156,"
"\"\"2025_fte\"\":8.2,\"\"2025_kapitaalsubsidies\"\":27420,\"\"2025_destin691\"\":0,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":391809,\"\"2025_geldbeleggingen\"\":0,"
"\"\"2025_personnel62\"\":441255,\"\"2025_gebouwen22\"\":53150,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":0,"
"\"\"2025_fondsen10\"\":124183,\"\"2025_overgedragen14\"\":285876,"
"\"\"2025_bestemdefondsen13\"\":0,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":20246,\"\"2025_capex8169\"\":0,"
"\"\"2024_omzet\"\":0,\"\"2024_73\"\":0,"
"\"\"2024_bruto\"\":478464,\"\"2024_pnl\"\":6066,\"\"2024_bedrijfswinst\"\":-9920,"
"\"\"2024_equity\"\":416397,\"\"2024_assets\"\":459328,"
"\"\"2024_debt\"\":42931,\"\"2024_cash\"\":350440,\"\"2024_fte\"\":9.1,"
"\"\"2024_destin691\"\":0,\"\"2024_kapitaalsubsidies\"\":37479,\"\"2024_76A\"\":0,"
"\"\"2024_geldbeleggingen\"\":0}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Kinderdagverblijf De Hartjes Ninove YE2025 (bruto JUMP 484k / omzet+73 empty VKT / pnl JUMP 31k / destin empty / Strong PDF),{EID},Opgroeien + leftover city_ninove CIK,VZW Kinderdagverblijf De Hartjes (KBO 0446.391.327; Actief; 1 VE; RSZ2025 88.911; toelating Kinderopvang Vlaamse Gemeenschap; 1/1 VE Ninove),2026-05-11,2025,2025,483796,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00170536.pdf,Public CIK dual of mined city_ninove,Publish Opgroeien matrix behind bruto 484k + why omzet+73 empty VKT + why pnl JUMP 31k destin empty while cash JUMP 392k and FTE DROP 8.2,{SRC_PDF},strong,Vlaanderen>Oost-Vlaanderen>Ninove>HartjesNinove>JR2025_statutory_L5,tick2451; Strong official native PDF; leftover mined city_ninove CIK; 1 VE; NOT Kloosterstraat 6 Drongen; NOT Groepsopvang De Hartjes Tienen 0441.374.348 remine; NOT De Wissel remine; NOT Familia remine; NOT t Sloeberke YE2024; not TE-additive",
])
print("commitments ok")
