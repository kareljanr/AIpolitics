from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2446_stamp.txt").read_text().strip().splitlines()
EID="vzw_kinderkuren"
SRC_PDF="src_kinderkuren_jr2025_nbb_pdf_2446"
COMM="comm_kinderkuren_jr2025_statutory_bruto_4_67m_omzet73_empty_pnl_flip_loss_618k"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
cash_json=(
"\"{\"\"2025_omzet\"\":0,\"\"2025_73\"\":0,\"\"2025_76A\"\":2432,"
"\"\"2025_opbr\"\":0,\"\"2025_bruto\"\":4674661,"
"\"\"2025_pnl\"\":-617961,\"\"2025_bedrijfswinst\"\":-615411,"
"\"\"2025_equity\"\":857351,\"\"2025_assets\"\":1762362,\"\"2025_debt\"\":905011,"
"\"\"2025_fte\"\":81.6,\"\"2025_kapitaalsubsidies\"\":0,\"\"2025_destin691\"\":0,"
"\"\"2025_791\"\":680000,\"\"2025_cash\"\":1417387,\"\"2025_geldbeleggingen\"\":0,"
"\"\"2025_personnel62\"\":5127146,\"\"2025_gebouwen22\"\":1128,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":112,"
"\"\"2025_fondsen10\"\":17217,\"\"2025_overgedragen14\"\":840134,"
"\"\"2025_bestemdefondsen13\"\":0,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":29822,\"\"2025_capex8029_8169\"\":15555,"
"\"\"2024_omzet\"\":0,\"\"2024_73\"\":0,"
"\"\"2024_bruto\"\":5663317,\"\"2024_pnl\"\":837483,\"\"2024_bedrijfswinst\"\":839176,"
"\"\"2024_equity\"\":1475312,\"\"2024_assets\"\":2390826,"
"\"\"2024_debt\"\":915514,\"\"2024_cash\"\":1340576,\"\"2024_fte\"\":72.4,"
"\"\"2024_destin691\"\":680000,\"\"2024_kapitaalsubsidies\"\":0,\"\"2024_76A\"\":3022}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Kinderkuren YE2025 (bruto DROP 4.67m / omzet+73 empty VKT / pnl FLIP LOSS 618k / destin DROP 680k / Strong PDF),{EID},Opgroeien + leftover city_leuven EVA BKO,VZW Kinderkuren (KBO 0478.167.834; Actief; 37 VE; naam Kinderkuren since 18.12.2025; EVA Stad Leuven; RSZ2025 88.919; 1/37 VE Leuven),2026-06-30,2025,2025,4674661,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00321398.pdf,Public EVA dual of mined city_leuven,Publish Opgroeien/Stad Leuven matrix behind bruto 4.67m + why omzet+73 empty VKT + why pnl FLIP LOSS 618k while destin DROP 680k and FTE JUMP 81.6,{SRC_PDF},strong,Vlaanderen>VlaamsBrabant>Leuven>Kinderkuren>JR2025_statutory_L5,tick2446; Strong official native PDF; leftover mined city_leuven EVA; 37 VE; NOT Kloosterstraat 6 Drongen; NOT Wigwam 0435.015.207; NOT t Anemoontje 0413.354.612; NOT t Zonnetje 0443.648.306; NOT Kinderdagverblijven Leuven 0413.321.255 absorbed; not TE-additive",
])
print("commitments ok")
