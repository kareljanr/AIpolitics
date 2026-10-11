from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2447_stamp.txt").read_text().strip().splitlines()
EID="vzw_cob_annuntiaten_heverlee"
SRC_PDF="src_cobah_jr2025_nbb_pdf_2447"
COMM="comm_cobah_jr2025_statutory_bruto_2_46m_omzet73_empty_pnl_drop_199k"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
cash_json=(
"\"{\"\"2025_omzet\"\":0,\"\"2025_73\"\":0,\"\"2025_76A\"\":3698,"
"\"\"2025_opbr\"\":0,\"\"2025_bruto\"\":2462444,"
"\"\"2025_pnl\"\":8845,\"\"2025_bedrijfswinst\"\":12020,"
"\"\"2025_equity\"\":2993102,\"\"2025_assets\"\":4525424,\"\"2025_debt\"\":1532322,"
"\"\"2025_fte\"\":43.5,\"\"2025_kapitaalsubsidies\"\":1792722,\"\"2025_destin691\"\":0,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":433864,\"\"2025_geldbeleggingen\"\":0,"
"\"\"2025_personnel62\"\":2246000,\"\"2025_gebouwen22\"\":3539290,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":0,"
"\"\"2025_fondsen10\"\":370618,\"\"2025_overgedragen14\"\":329763,"
"\"\"2025_bestemdefondsen13\"\":500000,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":198320,\"\"2025_capex8029_8169\"\":56022,"
"\"\"2024_omzet\"\":0,\"\"2024_73\"\":0,"
"\"\"2024_bruto\"\":2492228,\"\"2024_pnl\"\":207684,\"\"2024_bedrijfswinst\"\":209533,"
"\"\"2024_equity\"\":3006278,\"\"2024_assets\"\":4498862,"
"\"\"2024_debt\"\":1492584,\"\"2024_cash\"\":208643,\"\"2024_fte\"\":39.5,"
"\"\"2024_destin691\"\":0,\"\"2024_kapitaalsubsidies\"\":1814742,\"\"2024_76A\"\":559}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},COB Annuntiaten Heverlee YE2025 (bruto DROP 2.46m / omzet+73 empty VKT / pnl DROP 199k / destin empty / Strong PDF),{EID},Opgroeien + leftover city_leuven CIK,VZW COBAH (KBO 0447.017.570; Actief; 4 VE; RSZ2025 88.911; toelating Kinderopvang Vlaamse Gemeenschap; 2/4 VE Leuven),2026-06-23,2025,2025,2462444,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00216711.pdf,Public CIK dual of mined city_leuven,Publish Opgroeien matrix behind bruto 2.46m + why omzet+73 empty VKT + why pnl DROP 199k while destin empty and FTE JUMP 43.5,{SRC_PDF},strong,Vlaanderen>VlaamsBrabant>Leuven>COBAnnuntiatenHeverlee>JR2025_statutory_L5,tick2447; Strong official native PDF; leftover mined city_leuven CIK; 4 VE; NOT Kloosterstraat 6 Drongen; NOT WZC Annuntiaten 0895.366.220; NOT Kinderkuren 0478.167.834; NOT Kinderdagverblijven Leuven 0413.321.255 absorbed; not TE-additive",
])
print("commitments ok")
