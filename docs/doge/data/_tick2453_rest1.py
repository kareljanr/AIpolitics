from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2453_stamp.txt").read_text().strip().splitlines()
EID="vzw_oko_zo_zele"
SRC_PDF="src_oko_zo_jr2025_nbb_pdf_2453"
COMM="comm_oko_zo_jr2025_statutory_bruto_914k_omzet73_empty_pnl_flip_15k"
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
"\"\"2025_bruto\"\":914033,"
"\"\"2025_pnl\"\":-15184,\"\"2025_bedrijfswinst\"\":-20522,"
"\"\"2025_equity\"\":668157,\"\"2025_assets\"\":858840,\"\"2025_debt\"\":190683,"
"\"\"2025_fte\"\":14.2,\"\"2025_kapitaalsubsidies\"\":0,\"\"2025_destin691\"\":0,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":419271,\"\"2025_geldbeleggingen\"\":0,"
"\"\"2025_personnel62\"\":925505,\"\"2025_gebouwen22\"\":121734,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":0,"
"\"\"2025_fondsen10\"\":0,\"\"2025_overgedragen14\"\":668157,"
"\"\"2025_bestemdefondsen13\"\":0,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":8924,\"\"2025_capex8169\"\":3167,"
"\"\"2024_omzet\"\":0,\"\"2024_73\"\":0,"
"\"\"2024_bruto\"\":951799,\"\"2024_pnl\"\":17773,\"\"2024_bedrijfswinst\"\":11600,"
"\"\"2024_equity\"\":683341,\"\"2024_assets\"\":895781,"
"\"\"2024_debt\"\":212441,\"\"2024_cash\"\":309603,\"\"2024_fte\"\":14.8,"
"\"\"2024_destin691\"\":0,\"\"2024_kapitaalsubsidies\"\":0,\"\"2024_76A\"\":0,"
"\"\"2024_geldbeleggingen\"\":65000}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},OKO & ZO YE2025 (bruto DROP 914k / omzet+73 empty VKT / pnl FLIP LOSS 15k / destin empty / Strong PDF),{EID},Opgroeien + leftover city_zele CIK,VZW OKO & ZO (KBO 0862.154.608; Actief; 2 VE; RSZ2025 88.911; toelating Kinderopvang Vlaamse Gemeenschap; 2/2 VE Zele),2026-06-17,2025,2025,914033,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00191153.pdf,Public CIK dual of mined city_zele,Publish Opgroeien matrix behind bruto 914k + why omzet+73 empty VKT + why pnl FLIP LOSS 15k while destin empty and cash JUMP 419k and geldbeleggingen DROP 65k and FTE DROP 14.2,{SRC_PDF},strong,Vlaanderen>Oost-Vlaanderen>Zele>OKOZO>JR2025_statutory_L5,tick2453; Strong official native PDF; leftover mined city_zele CIK; 2 VE; NOT Kloosterstraat 6 Drongen; NOT Harlekijntjes 0407.700.403 remine; NOT Hartjes Ninove remine; NOT Hartjes Tienen remine; NOT De Wissel remine; NOT Familia remine; NOT t Sloeberke YE2024; not TE-additive",
])
print("commitments ok")
