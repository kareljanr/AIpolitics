from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2450_stamp.txt").read_text().strip().splitlines()
EID="vzw_hartjes_tienen"
SRC_PDF="src_hartjes_jr2025_nbb_pdf_2450"
COMM="comm_hartjes_jr2025_statutory_opbr_1_59m_omzet_252k_73_1_34m_pnl_jump_154k"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
cash_json=(
"\"{\"\"2025_omzet\"\":251750,\"\"2025_73\"\":1342084,\"\"2025_76A\"\":0,"
"\"\"2025_opbr\"\":1593834,\"\"2025_bruto\"\":1447874,"
"\"\"2025_pnl\"\":154432,\"\"2025_bedrijfswinst\"\":147753,"
"\"\"2025_equity\"\":511958,\"\"2025_assets\"\":695457,\"\"2025_debt\"\":183499,"
"\"\"2025_fte\"\":20.6,\"\"2025_kapitaalsubsidies\"\":0,\"\"2025_destin691\"\":154432,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":174846,\"\"2025_geldbeleggingen\"\":250000,"
"\"\"2025_personnel62\"\":1277682,\"\"2025_gebouwen22\"\":87788,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":0,"
"\"\"2025_fondsen10\"\":291275,\"\"2025_overgedragen14\"\":16251,"
"\"\"2025_bestemdefondsen13\"\":204432,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":18499,\"\"2025_capex8169\"\":18339,"
"\"\"2024_omzet\"\":267256,\"\"2024_73\"\":1288700,"
"\"\"2024_opbr\"\":1559358,\"\"2024_pnl\"\":115162,\"\"2024_bedrijfswinst\"\":107446,"
"\"\"2024_equity\"\":388648,\"\"2024_assets\"\":657053,"
"\"\"2024_debt\"\":268405,\"\"2024_cash\"\":130603,\"\"2024_fte\"\":20.6,"
"\"\"2024_destin691\"\":50000,\"\"2024_kapitaalsubsidies\"\":31122,\"\"2024_76A\"\":3402,"
"\"\"2024_geldbeleggingen\"\":250000}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Groepsopvang De Hartjes YE2025 (opbr JUMP 1.59m / omzet DROP 252k commercial-only / 73 JUMP 1.34m / pnl JUMP 154k / destin JUMP 154k / Strong PDF),{EID},Opgroeien + leftover city_tienen CIK,VZW Groepsopvang De Hartjes (KBO 0441.374.348; Actief; 1 VE; RSZ2025 88.911; toelating Kinderopvang Vlaamse Gemeenschap; 1/1 VE Tienen),2026-06-10,2025,2025,1593834,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00180031.pdf,Public CIK dual of mined city_tienen,Publish Opgroeien matrix behind opbr 1.59m + why omzet 252k commercial-only vs 73 1.34m + why pnl JUMP 154k destin=pnl while cash JUMP 175k and debt DROP 183k,{SRC_PDF},strong,Vlaanderen>Vlaams-Brabant>Tienen>Hartjes>JR2025_statutory_L5,tick2450; Strong official native PDF; leftover mined city_tienen CIK; 1 VE; NOT Kloosterstraat 6 Drongen; NOT De Hartjes Ninove 0446.391.327; NOT De Wissel remine; NOT Familia remine; NOT t Sloeberke YE2024; not TE-additive",
])
print("commitments ok")
