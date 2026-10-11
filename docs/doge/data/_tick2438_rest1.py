from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2438_stamp.txt").read_text().strip().splitlines()
EID="vzw_de_wissel"
SRC_PDF="src_de_wissel_jr2025_nbb_pdf_2438"
COMM="comm_de_wissel_jr2025_statutory_opbr_8_58m_73_8_10m_pnl_jump_102k"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
cash_json=(
"\"{\"\"2025_omzet\"\":0,\"\"2025_73\"\":8101474,\"\"2025_76A\"\":200,"
"\"\"2025_opbr\"\":8576450,\"\"2025_bruto\"\":0,"
"\"\"2025_pnl\"\":101865,\"\"2025_bedrijfswinst\"\":109342,"
"\"\"2025_equity\"\":3645083,\"\"2025_assets\"\":6189923,\"\"2025_debt\"\":2466620,"
"\"\"2025_fte\"\":82.7,\"\"2025_kapitaalsubsidies\"\":1651366,\"\"2025_destin691\"\":200000,"
"\"\"2025_cash\"\":656811,\"\"2025_geldbeleggingen\"\":0,"
"\"\"2025_personnel62\"\":6477401,\"\"2025_gebouwen22\"\":3467123,"
"\"\"2025_aanbouw27\"\":366190,\"\"2025_66B\"\":23222,"
"\"\"2025_fondsen10\"\":850000,\"\"2025_overgedragen14\"\":9337,"
"\"\"2025_bestemdefondsen13\"\":1134379,"
"\"\"2025_voorzieningen16\"\":78220,\"\"2025_630\"\":182536,\"\"2025_74\"\":474775,"
"\"\"2024_omzet\"\":20,\"\"2024_73\"\":7585632,"
"\"\"2024_opbr\"\":7900651,\"\"2024_pnl\"\":-97512,\"\"2024_bedrijfswinst\"\":-125021,"
"\"\"2024_equity\"\":2057619,\"\"2024_assets\"\":4578283,"
"\"\"2024_debt\"\":2432922,\"\"2024_cash\"\":326708,\"\"2024_fte\"\":80.7,"
"\"\"2024_destin691\"\":0,\"\"2024_kapitaalsubsidies\"\":1015768,\"\"2024_geldbeleggingen\"\":750000}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},De Wissel vzw YE2025 (opbr JUMP 8.58m / 73 JUMP 8.10m / pnl JUMP 102k / destin JUMP 200k / Strong PDF),{EID},Opgroeien + leftover city_leuven OVBJ,VZW De Wissel (KBO 0421.913.376; Actief; 1 VE zetel Parkstraat 64 3000 Leuven; RSZ2025 87.991; CANO/OVBJ),2026-06-24,2025,2025,8576450,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00213923.pdf,Public OVBJ dual of mined city_leuven,Publish Opgroeien matrix behind 73 8.10m + why destin 200k > pnl 102k + bouwprojecten gebouwen JUMP 3.47m,{SRC_PDF},strong,Vlaanderen>Vlaams-Brabant>Leuven>DeWissel>JR2025_statutory_L5,tick2438; Strong official native PDF; leftover mined city_leuven; 1 VE Leuven not city_rotselaar leftover same KBO; NOT Kloosterstraat 6 Drongen; NOT Monte Rosa 0413.350.751; NOT MFC Combo; NOT Don Bosco 0408.666.344; NOT Ferm 0416.117.627; NOT IZW 0430.278.439; NOT Avida 0438.814.241; not TE-additive",
])
print("commitments ok")
