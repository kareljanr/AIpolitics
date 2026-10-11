from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2454_stamp.txt").read_text().strip().splitlines()
EID="vzw_medemens_kdv_antwerpen"
SRC_PDF="src_medemens_kdv_jr2025_nbb_pdf_2454"
COMM="comm_medemens_kdv_jr2025_statutory_opbr_9_55m_omzet_1_76m_73_7_57m_pnl_drop_500k"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
cash_json=(
"\"{\"\"2025_omzet\"\":1762950,\"\"2025_73\"\":7571818,\"\"2025_76A\"\":100810,"
"\"\"2025_envelope70_76A\"\":9548863,\"\"2025_bruto\"\":0,"
"\"\"2025_pnl\"\":500404,\"\"2025_bedrijfswinst\"\":501545,"
"\"\"2025_equity\"\":14533752,\"\"2025_assets\"\":16808555,\"\"2025_debt\"\":2186496,"
"\"\"2025_fte\"\":123.7,\"\"2025_kapitaalsubsidies\"\":3503975,\"\"2025_destin691\"\":5672853,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":3019243,\"\"2025_geldbeleggingen\"\":500000,"
"\"\"2025_personnel62\"\":6768393,\"\"2025_gebouwen22\"\":8823127,"
"\"\"2025_aanbouw27\"\":31224,\"\"2025_66A\"\":49142,"
"\"\"2025_fondsen10\"\":1475810,\"\"2025_overgedragen14\"\":0,"
"\"\"2025_bestemdefondsen13\"\":9553967,"
"\"\"2025_voorzieningen16\"\":88307,\"\"2025_630\"\":454052,\"\"2025_capex8161_6\"\":989105,"
"\"\"2024_omzet\"\":1471486,\"\"2024_73\"\":7043292,"
"\"\"2024_envelope70_76A\"\":8706655,\"\"2024_pnl\"\":848906,\"\"2024_bedrijfswinst\"\":842210,"
"\"\"2024_equity\"\":13244296,\"\"2024_assets\"\":15376491,"
"\"\"2024_debt\"\":2132195,\"\"2024_cash\"\":2253921,\"\"2024_fte\"\":111,"
"\"\"2024_destin691\"\":848906,\"\"2024_kapitaalsubsidies\"\":3514922,\"\"2024_76A\"\":78999,"
"\"\"2024_geldbeleggingen\"\":500000}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},De Medemens Kinderdagverblijven YE2025 (opbr JUMP 9.55m / omzet JUMP 1.76m commercial-only / 73 JUMP 7.57m / pnl DROP 500k / destin JUMP 5.67m / Strong PDF),{EID},Opgroeien + leftover city_antwerpen CIK,VZW De Medemens Kinderdagverblijven (KBO 0893.678.915; Actief; 9 VE; RSZ2025 88.911; toelating Kinderopvang Vlaamse Gemeenschap; aanbestedende overheid; zetel Antwerpen),2026-06-17,2025,2025,9548863,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00206605.pdf,Public CIK dual of mined city_antwerpen,Publish Opgroeien matrix behind opbr 9.55m + why omzet 1.76m commercial-only vs 73 7.57m + why pnl DROP 500k while destin JUMP 5.67m and cash JUMP 3.02m and FTE JUMP 123.7,{SRC_PDF},strong,Vlaanderen>Antwerpen>Antwerpen>MedemensKDV>JR2025_statutory_L5,tick2454; Strong official native PDF; leftover mined city_antwerpen CIK; 9 VE; NOT Kloosterstraat 6 Drongen; NOT De Medemens 0428.692.191 remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes Ninove remine; NOT Hartjes Tienen remine; NOT Familia remine; NOT t Sloeberke YE2024; not TE-additive",
])
print("commitments ok")
