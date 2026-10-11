from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2433_stamp.txt").read_text().strip().splitlines()
EID="vzw_wzc_sint_coleta_gent"
SRC_PDF="src_sint_coleta_jr2025_nbb_pdf_2433"
COMM="comm_sint_coleta_jr2025_statutory_omzet_5_61m_73_983k_pnl_drop_75k"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
cash_json=(
"\"{\"\"2025_omzet\"\":5614657,\"\"2025_73\"\":982687,\"\"2025_76A\"\":70552,"
"\"\"2025_opbr\"\":6796611,\"\"2025_bruto\"\":0,"
"\"\"2025_pnl\"\":75406,\"\"2025_bedrijfswinst\"\":69308,"
"\"\"2025_equity\"\":2789036,\"\"2025_assets\"\":4673967,\"\"2025_debt\"\":1884932,"
"\"\"2025_fte\"\":66.8,\"\"2025_kapitaalsubsidies\"\":173334,\"\"2025_destin691\"\":0,"
"\"\"2025_cash\"\":478451,\"\"2025_geldbeleggingen\"\":650876,"
"\"\"2025_personnel62\"\":4729997,\"\"2025_gebouwen22\"\":2042258,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_capex\"\":136286,"
"\"\"2025_fondsen10\"\":299608,\"\"2025_overgedragen14\"\":1890348,"
"\"\"2025_bestemdefondsen13\"\":425746,"
"\"\"2025_66A\"\":6424,\"\"2025_66B\"\":0,\"\"2025_voorzieningen16\"\":0,"
"\"\"2025_76B\"\":0,\"\"2025_630\"\":271762,\"\"2025_733\"\":956206,"
"\"\"2024_omzet\"\":5095783,\"\"2024_73\"\":1073507,"
"\"\"2024_opbr\"\":6281450,\"\"2024_bruto\"\":0,\"\"2024_pnl\"\":194096,\"\"2024_bedrijfswinst\"\":192776,"
"\"\"2024_equity\"\":2738152,\"\"2024_assets\"\":4735989,"
"\"\"2024_debt\"\":1997837,\"\"2024_cash\"\":451304,\"\"2024_fte\"\":64.4,"
"\"\"2024_destin691\"\":0,\"\"2024_kapitaalsubsidies\"\":197856,\"\"2024_geldbeleggingen\"\":309210}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},WZC Sint-Coleta Gent vzw YE2025 (omzet JUMP 5.61m / 73 DROP 983k / pnl DROP 75k / destin 0 / Strong PDF),{EID},Departement Zorg + leftover city_gent WZC,VZW Woon- en Zorgcentrum Sint-Coleta Gent (KBO 0448.294.507; Actief; 1 VE Sint-Coletastraat 4 9000 Gent; RSZ2025 87.101; RVT),2026-06-18,2025,2025,5614657,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00192499.pdf,Public WZC dual of mined city_gent,Publish RIZIV/Vlaams/stad Gent/VIPA matrix behind omzet 5.61m + why 73 DROP 983k + why destin 0 of 75k pnl + FTE 66.8 JUMP,{SRC_PDF},strong,Vlaanderen>Oost-Vlaanderen>Gent>WZCSintColeta>JR2025_statutory_L5,tick2433; Strong official native PDF; leftover mined city_gent after Home Emmaus / Witje Wiebel / Beregoed / Windekind / Elfenbankje / AGB Kunsten / AGB Erfgoed; 1 VE Gent not city_aalter leftover; NOT Kloosterstraat 6 Drongen; NOT Home Emmaus 0451.749.190; NOT De Foyer 0413.796.456; NOT Emmaus AZ 0411.515.075; NOT Witje Wiebel 0443.654.937; NOT Beregoed 0447.515.042; NOT Windekind 0431.806.386; NOT Elfenbankje 0417.638.151; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037; NOT Knuffelboom 0478.310.859; NOT De Zeppelin 0454.001.867; not TE-additive",
])
print("commitments ok")
