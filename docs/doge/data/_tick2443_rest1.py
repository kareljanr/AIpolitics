from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2443_stamp.txt").read_text().strip().splitlines()
EID="vzw_jeugdhulp_don_bosco"
SRC_PDF="src_jdbv_jr2025_nbb_pdf_2443"
COMM="comm_jdbv_jr2025_statutory_opbr_29_16m_omzet_208k_73_27_79m_pnl_drop_830k"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
cash_json=(
"\"{\"\"2025_omzet\"\":207924,\"\"2025_73\"\":27785881,\"\"2025_76A\"\":671098,"
"\"\"2025_opbr\"\":29159144,\"\"2025_bruto\"\":0,"
"\"\"2025_pnl\"\":830135,\"\"2025_bedrijfswinst\"\":821772,"
"\"\"2025_equity\"\":24731057,\"\"2025_assets\"\":33372760,\"\"2025_debt\"\":8641703,"
"\"\"2025_fte\"\":342,\"\"2025_kapitaalsubsidies\"\":7796340,\"\"2025_destin691\"\":830135,"
"\"\"2025_cash\"\":3303716,\"\"2025_geldbeleggingen\"\":12671844,"
"\"\"2025_personnel62\"\":24343059,\"\"2025_gebouwen22\"\":7430623,"
"\"\"2025_aanbouw27\"\":559962,\"\"2025_66A\"\":306436,"
"\"\"2025_fondsen10\"\":4283735,\"\"2025_overgedragen14\"\":0,"
"\"\"2025_bestemdefondsen13\"\":12650983,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":696488,\"\"2025_capex8161_66\"\":699886,"
"\"\"2025_731\"\":218010,\"\"2025_733\"\":27567872,"
"\"\"2024_omzet\"\":193581,\"\"2024_73\"\":26595033,"
"\"\"2024_opbr\"\":27265839,\"\"2024_pnl\"\":1310352,\"\"2024_bedrijfswinst\"\":961016,"
"\"\"2024_equity\"\":23820622,\"\"2024_assets\"\":32273917,"
"\"\"2024_debt\"\":8453295,\"\"2024_cash\"\":2993936,\"\"2024_fte\"\":337.3,"
"\"\"2024_destin691\"\":6557130,\"\"2024_kapitaalsubsidies\"\":7866039,\"\"2024_geldbeleggingen\"\":11019628}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Jeugdhulp Don Bosco Vlaanderen vzw YE2025 (opbr JUMP 29.16m / omzet JUMP 208k commercial-only / 73 JUMP 27.79m / pnl DROP 830k / destin DROP 6.56m / Strong PDF),{EID},Opgroeien + leftover city_eeklo jeugdhulp,VZW Jeugdhulp Don Bosco Vlaanderen (KBO 0408.666.344; Actief; 17 VE zetel Waaistraat 6 9900 Eeklo; RSZ2025 87.991; 2/17 VE Eeklo),2026-06-18,2025,2025,29159144,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00259885.pdf,Public jeugdhulp dual of mined city_eeklo,Publish Opgroeien matrix behind opbr 29.16m + why omzet 208k commercial-only vs 73 27.79m + why destin DROP 6.56m to 830k = pnl + commissaris voorbehoud 2017-inbreng MVA,{SRC_PDF},strong,Vlaanderen>OostVlaanderen>Eeklo>JeugdhulpDonBosco>JR2025_statutory_L5,tick2443; Strong official native PDF; leftover mined city_eeklo; 17 VE 2/17 Eeklo; NOT Kloosterstraat 6 Drongen; NOT VIA Don Bosco vzw_via; NOT Kinderlach 0450.275.186; NOT m-accent 0465.841.411; NOT t Anemoontje 0413.354.612; not TE-additive",
])
print("commitments ok")
