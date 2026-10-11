from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2449_stamp.txt").read_text().strip().splitlines()
EID="vzw_familia_genk"
SRC_PDF="src_familia_jr2025_nbb_pdf_2449"
COMM="comm_familia_jr2025_statutory_opbr_7_57m_omzet_1_25m_73_6_23m_pnl_jump_645k"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
cash_json=(
"\"{\"\"2025_omzet\"\":1249649,\"\"2025_73\"\":6232638,\"\"2025_76A\"\":26485,"
"\"\"2025_opbr\"\":7571995,\"\"2025_bruto\"\":0,"
"\"\"2025_pnl\"\":645105,\"\"2025_bedrijfswinst\"\":642132,"
"\"\"2025_equity\"\":4554709,\"\"2025_assets\"\":5674553,\"\"2025_debt\"\":1065188,"
"\"\"2025_fte\"\":103.5,\"\"2025_kapitaalsubsidies\"\":1169221,\"\"2025_destin691\"\":462255,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":256788,\"\"2025_geldbeleggingen\"\":1334280,"
"\"\"2025_personnel62\"\":5952762,\"\"2025_gebouwen22\"\":2224617,"
"\"\"2025_aanbouw27\"\":604487,\"\"2025_66A\"\":1915,"
"\"\"2025_fondsen10\"\":454161,\"\"2025_overgedragen14\"\":358479,"
"\"\"2025_bestemdefondsen13\"\":2572848,"
"\"\"2025_voorzieningen16\"\":54656,\"\"2025_630\"\":220335,\"\"2025_capex8161_8166\"\":199810,"
"\"\"2024_omzet\"\":1208052,\"\"2024_73\"\":5748993,"
"\"\"2024_opbr\"\":7051844,\"\"2024_pnl\"\":610700,\"\"2024_bedrijfswinst\"\":610849,"
"\"\"2024_equity\"\":3978358,\"\"2024_assets\"\":5246173,"
"\"\"2024_debt\"\":1222982,\"\"2024_cash\"\":301202,\"\"2024_fte\"\":99,"
"\"\"2024_destin691\"\":460535,\"\"2024_kapitaalsubsidies\"\":1237975,\"\"2024_76A\"\":49379,"
"\"\"2024_geldbeleggingen\"\":934618}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Kinderdagverblijf Familia YE2025 (opbr JUMP 7.57m / omzet JUMP 1.25m commercial-only / 73 JUMP 6.23m / pnl JUMP 645k / destin JUMP 462k / Strong PDF),{EID},Opgroeien + leftover city_genk CIK,VZW Kinderdagverblijf Familia (KBO 0461.401.779; Actief; 1 VE; RSZ2025 88.911; toelating Kinderopvang Vlaamse Gemeenschap; 1/1 VE Genk),2026-06-15,2025,2025,7571995,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00272867.pdf,Public CIK dual of mined city_genk,Publish Opgroeien matrix behind opbr 7.57m + why omzet 1.25m commercial-only vs 73 6.23m + why pnl JUMP 645k while destin JUMP 462k and geldbeleggingen JUMP 1.33m,{SRC_PDF},strong,Vlaanderen>Limburg>Genk>Familia>JR2025_statutory_L5,tick2449; Strong official native PDF; leftover mined city_genk CIK; 1 VE; NOT Kloosterstraat 6 Drongen; NOT BKO GENK-OOST 0475.432.830 remine; NOT Peutertuinen GO Mariakerke 0410.221.116; NOT t Sloeberke 0410.973.360; not TE-additive",
])
print("commitments ok")
