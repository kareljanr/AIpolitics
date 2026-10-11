from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2448_stamp.txt").read_text().strip().splitlines()
EID="vzw_peutertuinen_go_mariakerke"
SRC_PDF="src_peutertuinen_jr2025_nbb_pdf_2448"
COMM="comm_peutertuinen_jr2025_statutory_bruto_872k_omzet73_empty_pnl_jump_115k"
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
"\"\"2025_opbr\"\":0,\"\"2025_bruto\"\":872268,"
"\"\"2025_pnl\"\":115219,\"\"2025_bedrijfswinst\"\":126095,"
"\"\"2025_equity\"\":1316171,\"\"2025_assets\"\":1658146,\"\"2025_debt\"\":341975,"
"\"\"2025_fte\"\":13.7,\"\"2025_kapitaalsubsidies\"\":491875,\"\"2025_destin691\"\":0,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":550474,\"\"2025_geldbeleggingen\"\":0,"
"\"\"2025_personnel62\"\":784405,\"\"2025_gebouwen22\"\":373129,"
"\"\"2025_aanbouw27\"\":627877,\"\"2025_66A\"\":53048,"
"\"\"2025_fondsen10\"\":0,\"\"2025_overgedragen14\"\":824297,"
"\"\"2025_bestemdefondsen13\"\":0,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":27380,\"\"2025_capex8029_8169\"\":559640,"
"\"\"2024_omzet\"\":0,\"\"2024_73\"\":0,"
"\"\"2024_bruto\"\":933927,\"\"2024_pnl\"\":72573,\"\"2024_bedrijfswinst\"\":72986,"
"\"\"2024_equity\"\":982265,\"\"2024_assets\"\":1260098,"
"\"\"2024_debt\"\":157833,\"\"2024_cash\"\":667369,\"\"2024_fte\"\":14.6,"
"\"\"2024_destin691\"\":0,\"\"2024_kapitaalsubsidies\"\":273188,\"\"2024_76A\"\":1351}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Peutertuinen GO Mariakerke YE2025 (bruto DROP 872k / omzet+73 empty VKT / pnl JUMP 115k / destin empty / Strong PDF),{EID},Opgroeien + leftover city_gent CIK,VZW Peutertuinen GO Mariakerke (KBO 0410.221.116; Actief; 2 VE; RSZ2025 88.911; toelating Kinderopvang Vlaamse Gemeenschap; 2/2 VE Gent-Mariakerke),2026-06-10,2025,2025,872268,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00288310.pdf,Public CIK dual of mined city_gent,Publish Opgroeien matrix behind bruto 872k + why omzet+73 empty VKT + why pnl JUMP 115k while destin empty and aanbouw JUMP 628k,{SRC_PDF},strong,Vlaanderen>OostVlaanderen>Gent>PeutertuinenGOMariakerke>JR2025_statutory_L5,tick2448; Strong official native PDF; leftover mined city_gent CIK; 2 VE; NOT Kloosterstraat 6 Drongen; NOT Mini-creches GO Next 0896.468.060; NOT Stad Gent peutertuinen; NOT Villa Boempatat 0660.616.520; NOT COB Annuntiaten 0447.017.570; not TE-additive",
])
print("commitments ok")
