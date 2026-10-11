from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2452_stamp.txt").read_text().strip().splitlines()
EID="vzw_harlekijntjes_tielt"
SRC_PDF="src_harlekijntjes_jr2025_nbb_pdf_2452"
COMM="comm_harlekijntjes_jr2025_statutory_bruto_1_90m_omzet73_empty_pnl_drop_144k"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
cash_json=(
"\"{\"\"2025_omzet\"\":0,\"\"2025_73\"\":0,\"\"2025_76A\"\":1700,"
"\"\"2025_bruto\"\":1896924,"
"\"\"2025_pnl\"\":144205,\"\"2025_bedrijfswinst\"\":136158,"
"\"\"2025_equity\"\":1405811,\"\"2025_assets\"\":1693592,\"\"2025_debt\"\":287780,"
"\"\"2025_fte\"\":27,\"\"2025_kapitaalsubsidies\"\":203433,\"\"2025_destin691\"\":661844,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":141324,\"\"2025_geldbeleggingen\"\":847580,"
"\"\"2025_personnel62\"\":1705156,\"\"2025_gebouwen22\"\":423141,"
"\"\"2025_aanbouw27\"\":2040,\"\"2025_66A\"\":10248,"
"\"\"2025_fondsen10\"\":375073,\"\"2025_overgedragen14\"\":165461,"
"\"\"2025_bestemdefondsen13\"\":661844,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":44081,\"\"2025_capex8169\"\":21840,"
"\"\"2024_omzet\"\":0,\"\"2024_73\"\":0,"
"\"\"2024_bruto\"\":1866805,\"\"2024_pnl\"\":176554,\"\"2024_bedrijfswinst\"\":141180,"
"\"\"2024_equity\"\":1276125,\"\"2024_assets\"\":1569532,"
"\"\"2024_debt\"\":293407,\"\"2024_cash\"\":705796,\"\"2024_fte\"\":28,"
"\"\"2024_destin691\"\":0,\"\"2024_kapitaalsubsidies\"\":217952,\"\"2024_76A\"\":0,"
"\"\"2024_geldbeleggingen\"\":198668}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},KINDEROPVANG De Harlekijntjes YE2025 (bruto JUMP 1.90m / omzet+73 empty VKT / pnl DROP 144k / destin JUMP 662k / Strong PDF),{EID},Opgroeien + leftover city_tielt CIK,VZW KINDEROPVANG De Harlekijntjes (KBO 0407.700.403; Actief; 1 VE; RSZ2025 88.911; toelating Kinderopvang Vlaamse Gemeenschap; 1/1 VE Tielt),2026-06-02,2025,2025,1896924,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00161949.pdf,Public CIK dual of mined city_tielt,Publish Opgroeien matrix behind bruto 1.90m + why omzet+73 empty VKT + why destin JUMP 662k while cash DROP 141k and geldbeleggingen JUMP 848k and FTE DROP 27,{SRC_PDF},strong,Vlaanderen>West-Vlaanderen>Tielt>Harlekijntjes>JR2025_statutory_L5,tick2452; Strong official native PDF; leftover mined city_tielt CIK; 1 VE; NOT Kloosterstraat 6 Drongen; NOT Hartjes Ninove 0446.391.327 remine; NOT Hartjes Tienen remine; NOT De Wissel remine; NOT Familia remine; NOT t Sloeberke YE2024; not TE-additive",
])
print("commitments ok")
