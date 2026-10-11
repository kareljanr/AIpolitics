from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2436_stamp.txt").read_text().strip().splitlines()
EID="vzw_avida"
SRC_PDF="src_avida_jr2025_nbb_pdf_2436"
COMM="comm_avida_jr2025_statutory_omzet_42_86m_73_11_55m_pnl_drop_784k"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
cash_json=(
"\"{\"\"2025_omzet\"\":42857494,\"\"2025_73\"\":11552982,\"\"2025_76A\"\":37803,"
"\"\"2025_opbr\"\":55138086,\"\"2025_bruto\"\":0,"
"\"\"2025_pnl\"\":-784162,\"\"2025_bedrijfswinst\"\":-484969,"
"\"\"2025_equity\"\":32531263,\"\"2025_assets\"\":67049389,\"\"2025_debt\"\":34448367,"
"\"\"2025_fte\"\":624.2,\"\"2025_kapitaalsubsidies\"\":10271770,\"\"2025_destin691\"\":0,"
"\"\"2025_cash\"\":6847926,\"\"2025_geldbeleggingen\"\":0,"
"\"\"2025_personnel62\"\":40657596,\"\"2025_gebouwen22\"\":43981165,"
"\"\"2025_aanbouw27\"\":1256730,\"\"2025_66A\"\":85058,"
"\"\"2025_fondsen10\"\":12928239,\"\"2025_overgedragen14\"\":8676365,"
"\"\"2025_bestemdefondsen13\"\":654148,"
"\"\"2025_voorzieningen16\"\":69759,\"\"2025_630\"\":3074601,"
"\"\"2024_omzet\"\":19520867,\"\"2024_73\"\":7771490,"
"\"\"2024_opbr\"\":27968542,\"\"2024_pnl\"\":-415792,\"\"2024_bedrijfswinst\"\":-253696,"
"\"\"2024_equity\"\":13497519,\"\"2024_assets\"\":31401611,"
"\"\"2024_debt\"\":17828901,\"\"2024_cash\"\":1993021,\"\"2024_fte\"\":302.7,"
"\"\"2024_destin691\"\":0,\"\"2024_kapitaalsubsidies\"\":2747291,\"\"2024_geldbeleggingen\"\":4000000}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Avida vzw YE2025 (omzet JUMP 42.86m / 73 JUMP 11.55m / pnl DROP 784k / destin 0 / Strong PDF),{EID},Departement Zorg + leftover city_gent WZC,VZW Avida (KBO 0438.814.241; Actief; 7 VE zetel Molenaarsstraat 34 9000 Gent; RSZ2025 87.101; RVT),2026-06-18,2025,2025,42857494,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00206951.pdf,Public WZC dual of mined city_gent,Publish Zorg/RIZIV/steden matrix behind omzet 42.86m + 73 11.55m + why consecutive losses 784k + why destin empty + Conecto merger opening,{SRC_PDF},strong,Vlaanderen>Oost-Vlaanderen>Gent>Avida>JR2025_statutory_L5,tick2436; Strong official native PDF; leftover mined city_gent; 7 VE Gent+Lochristi+Damme+Beveren same KBO not city_aalter leftover; Conecto 0433.961.964 absorbed 01.01.2025; NOT Kloosterstraat 6 Drongen; NOT WZC Sint-Coleta Gent 0448.294.507; NOT Home Emmaus 0451.749.190; NOT De Foyer 0413.796.456; NOT IZW 0430.278.439; NOT Ferm Kinderopvang 0416.117.627; NOT Witje Wiebel 0443.654.937; NOT Beregoed 0447.515.042; NOT Windekind 0431.806.386; not TE-additive",
])
print("commitments ok")
