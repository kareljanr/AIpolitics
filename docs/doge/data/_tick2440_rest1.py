from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2440_stamp.txt").read_text().strip().splitlines()
EID="vzw_ukkies"
SRC_PDF="src_ukkies_jr2025_nbb_pdf_2440"
COMM="comm_ukkies_jr2025_statutory_bruto_5_13m_pnl_flat_309k_destin_flat_309k"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
cash_json=(
"\"{\"\"2025_omzet\"\":0,\"\"2025_73\"\":0,\"\"2025_76A\"\":42695,"
"\"\"2025_opbr\"\":0,\"\"2025_bruto\"\":5126812,"
"\"\"2025_pnl\"\":308628,\"\"2025_bedrijfswinst\"\":300046,"
"\"\"2025_equity\"\":3995693,\"\"2025_assets\"\":4695584,\"\"2025_debt\"\":699892,"
"\"\"2025_fte\"\":79.3,\"\"2025_kapitaalsubsidies\"\":705041,\"\"2025_destin691\"\":308628,"
"\"\"2025_cash\"\":1065696,\"\"2025_geldbeleggingen\"\":1287959,"
"\"\"2025_personnel62\"\":4620455,\"\"2025_gebouwen22\"\":1766727,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":3736,"
"\"\"2025_fondsen10\"\":1187923,\"\"2025_overgedragen14\"\":1484169,"
"\"\"2025_bestemdefondsen13\"\":618560,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":190242,\"\"2025_capex8169\"\":103512,"
"\"\"2024_omzet\"\":0,\"\"2024_73\"\":0,"
"\"\"2024_bruto\"\":5061722,\"\"2024_pnl\"\":309932,\"\"2024_bedrijfswinst\"\":273579,"
"\"\"2024_equity\"\":3736723,\"\"2024_assets\"\":4709533,"
"\"\"2024_debt\"\":972810,\"\"2024_cash\"\":746188,\"\"2024_fte\"\":79.4,"
"\"\"2024_destin691\"\":309932,\"\"2024_kapitaalsubsidies\"\":754700,\"\"2024_geldbeleggingen\"\":1231052}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},De Ukkies vzw YE2025 (bruto JUMP 5.13m / omzet+73 empty / pnl FLAT 309k / destin FLAT 309k / Strong PDF),{EID},Opgroeien + leftover city_hasselt CIK,VZW De Ukkies (KBO 0412.729.654; Actief; 3 VE zetel Erasmuslaan 14 3500 Hasselt; RSZ2025 88.911; CIK 212 plaatsen + 5 BOA),2026-05-27,2025,2025,5126812,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00164180.pdf,Public CIK+BOA dual of mined city_hasselt,Publish Opgroeien matrix behind bruto 5.13m + why 70+73 empty at 462 plaatsen + why destin 309k = pnl while cash JUMP 1.07m,{SRC_PDF},strong,Vlaanderen>Limburg>Hasselt>DeUkkies>JR2025_statutory_L5,tick2440; Strong official native PDF; leftover mined city_hasselt; 3 VE Hasselt; NOT Kloosterstraat 6 Drongen; NOT De Slabbertjes 0411.972.064; NOT Ferm 0416.117.627; NOT Grauwzusters 0409.771.748 convent; NOT Jessa 0821.142.117; NOT Kinderlach 0450.275.186; not TE-additive",
])
print("commitments ok")
