from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2439_stamp.txt").read_text().strip().splitlines()
EID="vzw_slabbertjes"
SRC_PDF="src_slabbertjes_jr2025_nbb_pdf_2439"
COMM="comm_slabbertjes_jr2025_statutory_bruto_520k_pnl_drop_48k_destin_jump_375k"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
cash_json=(
"\"{\"\"2025_omzet\"\":0,\"\"2025_73\"\":0,\"\"2025_76A\"\":2808,"
"\"\"2025_opbr\"\":0,\"\"2025_bruto\"\":519885,"
"\"\"2025_pnl\"\":48280,\"\"2025_bedrijfswinst\"\":47360,"
"\"\"2025_equity\"\":599876,\"\"2025_assets\"\":662430,\"\"2025_debt\"\":62554,"
"\"\"2025_fte\"\":10.6,\"\"2025_kapitaalsubsidies\"\":71963,\"\"2025_destin691\"\":375400,"
"\"\"2025_cash\"\":138351,\"\"2025_geldbeleggingen\"\":257760,"
"\"\"2025_personnel62\"\":442718,\"\"2025_gebouwen22\"\":208808,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":1326,"
"\"\"2025_fondsen10\"\":91491,\"\"2025_overgedragen14\"\":0,"
"\"\"2025_bestemdefondsen13\"\":436423,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":27786,\"\"2025_capex8169\"\":2173,"
"\"\"2024_omzet\"\":0,\"\"2024_73\"\":0,"
"\"\"2024_bruto\"\":554244,\"\"2024_pnl\"\":61023,\"\"2024_bedrijfswinst\"\":59613,"
"\"\"2024_equity\"\":560592,\"\"2024_assets\"\":644742,"
"\"\"2024_debt\"\":84150,\"\"2024_cash\"\":332128,\"\"2024_fte\"\":8.2,"
"\"\"2024_destin691\"\":61023,\"\"2024_kapitaalsubsidies\"\":80958,\"\"2024_geldbeleggingen\"\":0}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},De Slabbertjes vzw YE2025 (bruto DROP 520k / omzet+73 empty / pnl DROP 48k / destin JUMP 375k / Strong PDF),{EID},Opgroeien + leftover city_leuven CIK,VZW Kinderdagverblijf De Slabbertjes (KBO 0411.972.064; Actief; 1 VE zetel Mechelsevest 4 3000 Leuven; RSZ2025 88.911; CIK 30 plaatsen),2026-05-31,2025,2025,519885,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00138923.pdf,Public CIK dual of mined city_leuven,Publish Opgroeien matrix behind bruto 520k + why destin 375k >> pnl 48k + cash DROP while geldbeleggingen JUMP 258k,{SRC_PDF},strong,Vlaanderen>Vlaams-Brabant>Leuven>DeSlabbertjes>JR2025_statutory_L5,tick2439; Strong official native PDF; leftover mined city_leuven; 1 VE Leuven; NOT Kloosterstraat 6 Drongen; NOT Ferm 0416.117.627; NOT t Eekhoorntje 0414.453.680; NOT De Wissel 0421.913.376; NOT Monte Rosa 0413.350.751; NOT IZW 0430.278.439; NOT Grauwzusters 0409.771.748 convent; not TE-additive",
])
print("commitments ok")
