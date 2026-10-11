from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2445_stamp.txt").read_text().strip().splitlines()
EID="vzw_t_zonnetje"
SRC_PDF="src_zonnetje_jr2025_nbb_pdf_2445"
COMM="comm_zonnetje_jr2025_statutory_bruto_2_11m_omzet73_empty_pnl_drop_176k"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
cash_json=(
"\"{\"\"2025_omzet\"\":0,\"\"2025_73\"\":0,\"\"2025_76A\"\":10445,"
"\"\"2025_opbr\"\":0,\"\"2025_bruto\"\":2113971,"
"\"\"2025_pnl\"\":175969,\"\"2025_bedrijfswinst\"\":158114,"
"\"\"2025_equity\"\":1652293,\"\"2025_assets\"\":2101178,\"\"2025_debt\"\":448885,"
"\"\"2025_fte\"\":30.5,\"\"2025_kapitaalsubsidies\"\":213065,\"\"2025_destin691\"\":0,"
"\"\"2025_cash\"\":279435,\"\"2025_geldbeleggingen\"\":900000,"
"\"\"2025_personnel62\"\":1848937,\"\"2025_gebouwen22\"\":0,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":453,"
"\"\"2025_fondsen10\"\":47700,\"\"2025_overgedragen14\"\":1391528,"
"\"\"2025_bestemdefondsen13\"\":0,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":104433,\"\"2025_capex8169\"\":251244,"
"\"\"2024_omzet\"\":0,\"\"2024_73\"\":0,"
"\"\"2024_bruto\"\":2074478,\"\"2024_pnl\"\":299368,\"\"2024_bedrijfswinst\"\":280456,"
"\"\"2024_equity\"\":1510639,\"\"2024_assets\"\":1855217,"
"\"\"2024_debt\"\":344578,\"\"2024_cash\"\":612863,\"\"2024_fte\"\":29.4,"
"\"\"2024_destin691\"\":0,\"\"2024_kapitaalsubsidies\"\":247380,\"\"2024_76A\"\":9478}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},t Zonnetje kinderdagverblijven YE2025 (bruto JUMP 2.11m / omzet+73 empty VKT / pnl DROP 176k / destin empty / Strong PDF),{EID},Opgroeien + leftover city_waregem + leftover city_kruisem CIK,VZW t Zonnetje kinderdagverblijven (KBO 0443.648.306; Actief; 3 VE 2.154.838.667 Nazareth-De Pinte + 2.218.012.589 Kruisem + 2.218.012.886 Waregem; RSZ2025 88.911; 1/3 VE Waregem + 1/3 VE Kruisem),2026-06-04,2025,2025,2113971,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00162372.pdf,Public CIK dual of mined city_waregem + leftover city_kruisem,Publish Opgroeien matrix behind bruto 2.11m + why omzet+73 empty VKT + why pnl DROP 176k while destin empty and cash DROP 54pct while beleggingen JUMP 900k,{SRC_PDF},strong,Vlaanderen>OostVlaanderen>Waregem>tZonnetje>JR2025_statutory_L5,tick2445; Strong official native PDF; leftover mined city_waregem + leftover mined city_kruisem; 3 VE; NOT Kloosterstraat 6 Drongen; NOT Kindercentrum 0408.226.775; NOT KINDEROPVANG ZONNESTRAAL 0413.351.642; NOT Zonnestraal Junior 0866.116.859; NOT KDV De Regenboog 0671.670.560 BV; NOT Wigwam 0435.015.207; not TE-additive",
])
print("commitments ok")
