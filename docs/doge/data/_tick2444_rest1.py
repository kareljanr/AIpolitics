from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2444_stamp.txt").read_text().strip().splitlines()
EID="vzw_wigwam"
SRC_PDF="src_wigwam_jr2025_nbb_pdf_2444"
COMM="comm_wigwam_jr2025_statutory_bruto_1_07m_omzet73_empty_pnl_drop_36"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
cash_json=(
"\"{\"\"2025_omzet\"\":0,\"\"2025_73\"\":0,\"\"2025_76A\"\":22522,"
"\"\"2025_opbr\"\":0,\"\"2025_bruto\"\":1068827,"
"\"\"2025_pnl\"\":36,\"\"2025_bedrijfswinst\"\":26727,"
"\"\"2025_equity\"\":896597,\"\"2025_assets\"\":2053811,\"\"2025_debt\"\":1157214,"
"\"\"2025_fte\"\":18.6,\"\"2025_kapitaalsubsidies\"\":644459,\"\"2025_destin691\"\":149849,"
"\"\"2025_cash\"\":207008,\"\"2025_geldbeleggingen\"\":0,"
"\"\"2025_personnel62\"\":946597,\"\"2025_gebouwen22\"\":1739199,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":5113,"
"\"\"2025_fondsen10\"\":0,\"\"2025_overgedragen14\"\":0,"
"\"\"2025_bestemdefondsen13\"\":252138,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":84903,\"\"2025_capex8169\"\":4752,"
"\"\"2024_omzet\"\":0,\"\"2024_73\"\":0,"
"\"\"2024_bruto\"\":1057980,\"\"2024_pnl\"\":98132,\"\"2024_bedrijfswinst\"\":126283,"
"\"\"2024_equity\"\":931072,\"\"2024_assets\"\":2133288,"
"\"\"2024_debt\"\":1202216,\"\"2024_cash\"\":203846,\"\"2024_fte\"\":15.6,"
"\"\"2024_destin691\"\":98132,\"\"2024_kapitaalsubsidies\"\":678969,\"\"2024_76A\"\":21121}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Wigwam vzw YE2025 (bruto JUMP 1.07m / omzet+73 empty VKT / pnl DROP 36 / destin JUMP 150k / Strong PDF),{EID},Opgroeien + leftover city_leuven CIK,VZW Wigwam (KBO 0435.015.207; Actief; 1 VE 2.155.773.431 Diestsesteenweg 379/c 3010 Leuven; RSZ2025 88.911; 1/1 VE Leuven),2026-06-11,2025,2025,1068827,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00159445.pdf,Public CIK dual of mined city_leuven,Publish Opgroeien matrix behind bruto 1.07m + why omzet+73 empty VKT + why pnl DROP to 36 while destin JUMP 150k and FTE JUMP 18.6,{SRC_PDF},strong,Vlaanderen>VlaamsBrabant>Leuven>Wigwam>JR2025_statutory_L5,tick2444; Strong official native PDF; leftover mined city_leuven; 1 VE Leuven; NOT Kloosterstraat 6 Drongen; NOT t Anemoontje 0413.354.612; NOT De Slabbertjes 0411.972.064; NOT Ferm Kinderopvang 0416.117.627; NOT Jeugdhulp Don Bosco 0408.666.344; not TE-additive",
])
print("commitments ok")
