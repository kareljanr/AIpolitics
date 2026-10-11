from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2435_stamp.txt").read_text().strip().splitlines()
EID="vzw_izw_leuven"
SRC_PDF="src_izw_jr2025_nbb_pdf_2435"
COMM="comm_izw_jr2025_statutory_opbr_1_33m_omzet_530k_73_803k_pnl_drop_10k"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
cash_json=(
"\"{\"\"2025_omzet\"\":530078,\"\"2025_73\"\":802987,\"\"2025_76A\"\":163,"
"\"\"2025_opbr\"\":1333228,\"\"2025_bruto\"\":815478,"
"\"\"2025_pnl\"\":10323,\"\"2025_bedrijfswinst\"\":5047,"
"\"\"2025_equity\"\":867134,\"\"2025_assets\"\":1468447,\"\"2025_debt\"\":601313,"
"\"\"2025_fte\"\":17.3,\"\"2025_kapitaalsubsidies\"\":0,\"\"2025_destin691\"\":35000,"
"\"\"2025_cash\"\":1444638,\"\"2025_geldbeleggingen\"\":0,"
"\"\"2025_personnel62\"\":742756,\"\"2025_gebouwen22\"\":0,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":62904,"
"\"\"2025_fondsen10\"\":120143,\"\"2025_overgedragen14\"\":561991,"
"\"\"2025_bestemdefondsen13\"\":185000,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":0,"
"\"\"2024_omzet\"\":505113,\"\"2024_73\"\":841458,"
"\"\"2024_opbr\"\":1346571,\"\"2024_bruto\"\":936197,\"\"2024_pnl\"\":188046,\"\"2024_bedrijfswinst\"\":184611,"
"\"\"2024_equity\"\":856811,\"\"2024_assets\"\":1595128,"
"\"\"2024_debt\"\":738316,\"\"2024_cash\"\":1486891,\"\"2024_fte\"\":16.4,"
"\"\"2024_destin691\"\":0,\"\"2024_kapitaalsubsidies\"\":0,\"\"2024_geldbeleggingen\"\":0}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},IZW vzw YE2025 (opbr DROP 1.33m / omzet JUMP 530k commercial-only / 73 DROP 803k / pnl DROP 10k / destin 35k / Strong PDF),{EID},VAPH + leftover city_leuven VAPH,VZW IZW (KBO 0430.278.439; Actief; 3 VE zetel Riddersstraat 60 bus 02 3000 Leuven; RSZ2025 88.999; VAPH),2026-06-11,2025,2025,1333228,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00262459.pdf,Public VAPH dual of mined city_leuven,Publish VAPH/Vlaams/Leuven/Grimbergen matrix behind opbr 1.33m + why 70 commercial-only vs large 73 + why destin 35k of 10k pnl + why 66A 63k vakantiegeld,{SRC_PDF},strong,Vlaanderen>Vlaams-Brabant>Leuven>IZW>JR2025_statutory_L5,tick2435; Strong official native PDF; leftover mined city_leuven; 3 VE Leuven+Grimbergen same KBO not city_aalter leftover; NOT Kloosterstraat 6 Drongen; NOT Ferm Kinderopvang 0416.117.627; NOT Alvinnenberg 0434.390.150; NOT Hejmen 0426.383.987; NOT Staf 0431.333.660; NOT Grimbergen VAPH Zonnestraal; NOT WZC Sint-Coleta Gent 0448.294.507; NOT Home Emmaus 0451.749.190; NOT Witje Wiebel 0443.654.937; NOT Beregoed 0447.515.042; NOT Windekind 0431.806.386; not TE-additive",
])
print("commitments ok")
