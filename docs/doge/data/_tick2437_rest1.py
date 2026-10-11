from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2437_stamp.txt").read_text().strip().splitlines()
EID="vzw_monte_rosa"
SRC_PDF="src_monte_rosa_jr2025_nbb_pdf_2437"
COMM="comm_monte_rosa_jr2025_statutory_opbr_5_42m_73_5_32m_pnl_jump_349k"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
cash_json=(
"\"{\"\"2025_omzet\"\":0,\"\"2025_73\"\":5323280,\"\"2025_76A\"\":0,"
"\"\"2025_opbr\"\":5424143,\"\"2025_bruto\"\":0,"
"\"\"2025_pnl\"\":348642,\"\"2025_bedrijfswinst\"\":369456,"
"\"\"2025_equity\"\":5395536,\"\"2025_assets\"\":7358796,\"\"2025_debt\"\":1963260,"
"\"\"2025_fte\"\":63.0,\"\"2025_kapitaalsubsidies\"\":1749682,\"\"2025_destin691\"\":2050000,"
"\"\"2025_cash\"\":823541,\"\"2025_geldbeleggingen\"\":1662593,"
"\"\"2025_personnel62\"\":4348869,\"\"2025_gebouwen22\"\":1478450,"
"\"\"2025_aanbouw27\"\":2333389,\"\"2025_66A\"\":84,"
"\"\"2025_fondsen10\"\":294730,\"\"2025_overgedragen14\"\":223125,"
"\"\"2025_bestemdefondsen13\"\":3128000,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":84853,\"\"2025_74\"\":100863,"
"\"\"2024_omzet\"\":0,\"\"2024_73\"\":5274009,"
"\"\"2024_opbr\"\":5421846,\"\"2024_pnl\"\":213173,\"\"2024_bedrijfswinst\"\":215304,"
"\"\"2024_equity\"\":5085007,\"\"2024_assets\"\":7020817,"
"\"\"2024_debt\"\":1935811,\"\"2024_cash\"\":575837,\"\"2024_fte\"\":64.9,"
"\"\"2024_destin691\"\":176176,\"\"2024_kapitaalsubsidies\"\":1787794,\"\"2024_geldbeleggingen\"\":1604926}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Monte Rosa vzw YE2025 (opbr FLAT 5.42m / 73 JUMP 5.32m / pnl JUMP 349k / destin JUMP 2.05m / Strong PDF),{EID},Opgroeien + leftover city_leuven OVBJ,VZW Monte Rosa (KBO 0413.350.751; Actief; 4 VE zetel Heidebergstraat 249 3010 Leuven; RSZ2025 87.991; OVBJ),2026-04-23,2025,2025,5424143,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00093041.pdf,Public OVBJ dual of mined city_leuven,Publish Opgroeien matrix behind 73 5.32m + why destin 2.05m >> pnl 349k + bouwprojecten aanbouw 2.33m,{SRC_PDF},strong,Vlaanderen>Vlaams-Brabant>Leuven>MonteRosa>JR2025_statutory_L5,tick2437; Strong official native PDF; leftover mined city_leuven; also leftover mined city_herent + leftover mined city_antwerpen same KBO not city_aalter leftover; 4 VE Leuven+Herent+Deurne; NOT Kloosterstraat 6 Drongen; NOT Don Bosco 0408.666.344; NOT Ferm 0416.117.627; NOT IZW 0430.278.439; NOT Avida 0438.814.241; NOT Konekt 0524.936.680; not TE-additive",
])
print("commitments ok")
