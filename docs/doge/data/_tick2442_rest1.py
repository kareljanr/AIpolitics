from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2442_stamp.txt").read_text().strip().splitlines()
EID="vzw_anemoontje"
SRC_PDF="src_anemoontje_jr2025_nbb_pdf_2442"
COMM="comm_anemoontje_jr2025_statutory_opbr_835k_omzet_137k_73_698k_pnl_jump_105k_destin_jump_598k"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
cash_json=(
"\"{\"\"2025_omzet\"\":136595,\"\"2025_73\"\":698331,\"\"2025_76A\"\":0,"
"\"\"2025_opbr\"\":834926,\"\"2025_bruto\"\":759661,"
"\"\"2025_pnl\"\":105278,\"\"2025_bedrijfswinst\"\":109330,"
"\"\"2025_equity\"\":1329241,\"\"2025_assets\"\":1575233,\"\"2025_debt\"\":245992,"
"\"\"2025_fte\"\":8.1,\"\"2025_kapitaalsubsidies\"\":515543,\"\"2025_destin691\"\":598014,"
"\"\"2025_cash\"\":332675,\"\"2025_geldbeleggingen\"\":250000,"
"\"\"2025_personnel62\"\":573449,\"\"2025_gebouwen22\"\":898992,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":0,"
"\"\"2025_fondsen10\"\":12702,\"\"2025_overgedragen14\"\":202982,"
"\"\"2025_bestemdefondsen13\"\":598014,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":74800,\"\"2025_capex8169\"\":1997,"
"\"\"2024_omzet\"\":134340,\"\"2024_73\"\":629635,"
"\"\"2024_opbr\"\":763975,\"\"2024_pnl\"\":55346,\"\"2024_bedrijfswinst\"\":59669,"
"\"\"2024_equity\"\":1263408,\"\"2024_assets\"\":1521581,"
"\"\"2024_debt\"\":258172,\"\"2024_cash\"\":224895,\"\"2024_fte\"\":9.4,"
"\"\"2024_destin691\"\":0,\"\"2024_kapitaalsubsidies\"\":554988,\"\"2024_geldbeleggingen\"\":250000}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Kinderdagverblijf t Anemoontje vzw YE2025 (opbr JUMP 835k / omzet JUMP 137k commercial-only / 73 JUMP 698k / pnl JUMP 105k / destin JUMP 598k / Strong PDF),{EID},Opgroeien + leftover city_leuven CIK,VZW Kinderdagverblijf t Anemoontje (KBO 0413.354.612; Actief; 1 VE 2.150.886.809 Bosstraat 30 3012 Leuven; RSZ2025 88.911; CIK 40 plaatsen),2026-06-17,2025,2025,834926,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00213975.pdf,Public CIK dual of mined city_leuven,Publish Opgroeien matrix behind opbr 835k + why omzet 137k commercial-only vs 73 698k + why destin JUMP 598k >> pnl 105k while overgedragen DROP 203k,{SRC_PDF},strong,Vlaanderen>VlaamsBrabant>Leuven>Anemoontje>JR2025_statutory_L5,tick2442; Strong official native PDF; leftover mined city_leuven; 1 VE Leuven; NOT Kloosterstraat 6 Drongen; NOT Duinhuisjes VE t Anemoontje 2.375.207.425; NOT De Slabbertjes 0411.972.064; NOT Ferm Kinderopvang 0416.117.627; NOT Kinderlach 0450.275.186; not TE-additive",
])
print("commitments ok")
