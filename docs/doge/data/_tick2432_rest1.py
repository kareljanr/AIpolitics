from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2432_stamp.txt").read_text().strip().splitlines()
EID="vzw_home_emmaus"
SRC_PDF="src_home_emmaus_jr2025_nbb_pdf_2432"
COMM="comm_home_emmaus_jr2025_statutory_opbr_2_23m_omzet_279k_73_1_95m_pnl_jump_271k"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
cash_json=(
"\"{\"\"2025_omzet\"\":279413,\"\"2025_73\"\":1951139,\"\"2025_76A\"\":0,"
"\"\"2025_opbr\"\":2230552,\"\"2025_bruto\"\":2086695,"
"\"\"2025_pnl\"\":270624,\"\"2025_bedrijfswinst\"\":193689,"
"\"\"2025_equity\"\":2562446,\"\"2025_assets\"\":2911569,\"\"2025_debt\"\":349123,"
"\"\"2025_fte\"\":26.6,\"\"2025_kapitaalsubsidies\"\":27614,\"\"2025_destin691\"\":0,"
"\"\"2025_cash\"\":736197,\"\"2025_geldbeleggingen\"\":1841875,"
"\"\"2025_personnel62\"\":1859718,\"\"2025_gebouwen22\"\":0,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_capex\"\":86283,"
"\"\"2025_fondsen10\"\":0,\"\"2025_overgedragen14\"\":2399832,"
"\"\"2025_bestemdefondsen13\"\":135000,"
"\"\"2025_66A\"\":97,\"\"2025_66B\"\":0,\"\"2025_voorzieningen16\"\":0,"
"\"\"2025_76B\"\":0,\"\"2025_630\"\":24409,"
"\"\"2024_omzet\"\":269143,\"\"2024_73\"\":1854327,"
"\"\"2024_opbr\"\":2123470,\"\"2024_bruto\"\":1988358,\"\"2024_pnl\"\":226461,\"\"2024_bedrijfswinst\"\":141307,"
"\"\"2024_equity\"\":2264207,\"\"2024_assets\"\":2578270,"
"\"\"2024_debt\"\":314063,\"\"2024_cash\"\":1017801,\"\"2024_fte\"\":27.6,"
"\"\"2024_destin691\"\":0,\"\"2024_kapitaalsubsidies\"\":0,\"\"2024_geldbeleggingen\"\":1309992}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Home Emmaus vzw YE2025 (opbr JUMP 2.23m / omzet 279k commercial-only / 73 JUMP 1.95m / pnl JUMP 271k / destin 0 / Strong PDF),{EID},VAPH + leftover city_gent VAPH,VZW Home Emmaus (KBO 0451.749.190; Actief; 1 VE Van den Heckestraat 41-43 9050 Gent; RSZ2025 88.104; VAPH-erkend),2026-06-02,2025,2025,2230552,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00339558.pdf,Public VAPH dual of mined city_gent,Publish VAPH/PVF/RTH matrix behind opbr 2.23m + why 70 commercial-only vs large 73 + why destin 0 of 271k pnl + FTE 26.6 DROP,{SRC_PDF},strong,Vlaanderen>Oost-Vlaanderen>Gent>HomeEmmaus>JR2025_statutory_L5,tick2432; Strong official native PDF; leftover mined city_gent after Witje Wiebel / Beregoed / Windekind / Elfenbankje / AGB Kunsten / AGB Erfgoed; 1 VE Gent-Ledeberg not city_aalter leftover; NOT Kloosterstraat 6 Drongen; NOT Emmaus AZ 0411.515.075; NOT Witje Wiebel 0443.654.937; NOT Beregoed 0447.515.042; NOT Windekind 0431.806.386; NOT Elfenbankje 0417.638.151; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037; NOT Knuffelboom 0478.310.859; NOT De Zeppelin 0454.001.867; not TE-additive",
])
print("commitments ok")
