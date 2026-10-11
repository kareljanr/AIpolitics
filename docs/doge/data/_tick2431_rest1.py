from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2431_stamp.txt").read_text().strip().splitlines()
EID="vzw_witje_wiebel"
SRC_PDF="src_witje_wiebel_jr2025_nbb_pdf_2431"
COMM="comm_witje_wiebel_jr2025_statutory_bruto_1_88m_omzet73_empty_pnl_jump_301k"
LB="lb_witje_wiebel_bruto_1_88m_omzet73_empty_pnl_jump_301k_destin_300k_jr2025"
GAP="gap_witje_wiebel_opgroeien_matrix_bruto_1_88m_omzet73_empty_pnl_jump_301k_destin_300k_l5"
DRAFT=f"docs/doge/foi/drafts/{GAP}.md"
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
"\"\"2025_bruto\"\":1878999,"
"\"\"2025_pnl\"\":301158,\"\"2025_bedrijfswinst\"\":304658,"
"\"\"2025_equity\"\":2307857,\"\"2025_assets\"\":2843864,\"\"2025_debt\"\":536007,"
"\"\"2025_fte\"\":25.3,\"\"2025_kapitaalsubsidies\"\":560470,\"\"2025_destin691\"\":300000,"
"\"\"2025_cash\"\":804896,\"\"2025_geldbeleggingen\"\":650000,"
"\"\"2025_personnel62\"\":1490455,\"\"2025_gebouwen22\"\":1134601,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_capex\"\":28703,"
"\"\"2025_fondsen10\"\":88712,\"\"2025_overgedragen14\"\":1059090,"
"\"\"2025_bestemdefondsen13\"\":599585,"
"\"\"2025_66A\"\":0,\"\"2025_66B\"\":0,\"\"2025_voorzieningen16\"\":0,"
"\"\"2025_76B\"\":0,\"\"2025_630\"\":80835,"
"\"\"2024_omzet\"\":0,\"\"2024_73\"\":0,"
"\"\"2024_bruto\"\":1877813,\"\"2024_pnl\"\":299585,\"\"2024_bedrijfswinst\"\":308105,"
"\"\"2024_equity\"\":2039571,\"\"2024_assets\"\":2634687,"
"\"\"2024_debt\"\":595116,\"\"2024_cash\"\":517039,\"\"2024_fte\"\":25.3,"
"\"\"2024_destin691\"\":299585,\"\"2024_kapitaalsubsidies\"\":593343,\"\"2024_geldbeleggingen\"\":650000}\""
)
print("cash_json starts", cash_json[:20])
append_lines(DATA/"commitments.csv", [
f"{COMM},Witje Wiebel vzw YE2025 (bruto FLAT 1.88m / omzet+73 empty / pnl JUMP 301k / destin 300k / Strong PDF),{EID},Opgroeien + leftover city_gent CIK,VZW KINDERDAGVERBLIJF WITJE WIEBEL (KBO 0443.654.937; Actief; 2 VE Kortrijksesteenweg 1020 9000 Gent + Smidsestraat 88 9000 Gent; RSZ2025 88.911; Kinderopvang Vlaamse Gemeenschap),2026-06-01,2025,2025,1878999,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00143338.pdf,Public CIK dual of mined city_gent,Publish Opgroeien/ouderbijdragen matrix behind bruto 1.88m + why 70+73 empty vs 2 Gent campussen + why destin 300k of 301k pnl + FTE 25.3,{SRC_PDF},strong,Vlaanderen>Oost-Vlaanderen>Gent>WitjeWiebel>JR2025_statutory_L5,tick2431; Strong official native PDF; leftover mined city_gent after Beregoed / Windekind / Elfenbankje / AGB Kunsten / AGB Erfgoed; 2 VE both Gent not city_aalter leftover; NOT Kloosterstraat 6 Drongen; NOT Beregoed 0447.515.042; NOT Windekind 0431.806.386; NOT Elfenbankje 0417.638.151; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037; NOT Duinhuisjes 0413.323.037; NOT t Bremhuisje 0445.265.533 stopgezet 1993; NOT Kinderlach 0450.275.186; NOT KISME 0894.549.440; NOT Kindercentrum 0408.226.775; not TE-additive",
])
print("commitments ok")
