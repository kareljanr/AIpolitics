from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2441_stamp.txt").read_text().strip().splitlines()
EID="vzw_hummeltjes"
SRC_PDF="src_hummeltjes_jr2025_nbb_pdf_2441"
COMM="comm_hummeltjes_jr2025_statutory_opbr_13_11m_omzet_1_40m_73_11_28m_pnl_drop_259k_destin_drop_70k"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
cash_json=(
"\"{\"\"2025_omzet\"\":1401475,\"\"2025_73\"\":11277795,\"\"2025_76A\"\":57881,"
"\"\"2025_opbr\"\":13105742,\"\"2025_bruto\"\":0,"
"\"\"2025_pnl\"\":259329,\"\"2025_bedrijfswinst\"\":247462,"
"\"\"2025_equity\"\":5708548,\"\"2025_assets\"\":9784745,\"\"2025_debt\"\":3968488,"
"\"\"2025_fte\"\":152.9,\"\"2025_kapitaalsubsidies\"\":2662209,\"\"2025_destin691\"\":70000,"
"\"\"2025_cash\"\":2100999,\"\"2025_geldbeleggingen\"\":500000,"
"\"\"2025_personnel62\"\":10263962,\"\"2025_gebouwen22\"\":5417866,"
"\"\"2025_aanbouw27\"\":136841,\"\"2025_66A\"\":47860,"
"\"\"2025_fondsen10\"\":829074,\"\"2025_overgedragen14\"\":647265,"
"\"\"2025_bestemdefondsen13\"\":1570000,"
"\"\"2025_voorzieningen16\"\":107709,\"\"2025_630\"\":406810,\"\"2025_capex8169\"\":92968,"
"\"\"2024_omzet\"\":1286093,\"\"2024_73\"\":10790315,"
"\"\"2024_opbr\"\":12404911,\"\"2024_pnl\"\":552603,\"\"2024_bedrijfswinst\"\":544940,"
"\"\"2024_equity\"\":5585606,\"\"2024_assets\"\":9593084,"
"\"\"2024_debt\"\":3934958,\"\"2024_cash\"\":1779290,\"\"2024_fte\"\":148.7,"
"\"\"2024_destin691\"\":735647,\"\"2024_kapitaalsubsidies\"\":2798596,\"\"2024_geldbeleggingen\"\":300000}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},De Hummeltjes vzw YE2025 (opbr JUMP 13.11m / omzet JUMP 1.40m commercial-only / 73 JUMP 11.28m / pnl DROP 259k / destin DROP 70k / Strong PDF),{EID},Opgroeien + leftover city_hasselt CIK,VZW De Hummeltjes (KBO 0409.987.425; Actief; 13 VE zetel Zuster Stanislaslaan 1 3500 Hasselt; RSZ2025 88.911; CIK+BOA+CKG 450 plaatsen),2026-06-15,2025,2025,13105742,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00225380.pdf,Public CIK+BOA+CKG dual of mined city_hasselt,Publish Opgroeien matrix behind opbr 13.11m + why omzet 1.40m commercial-only vs 73 11.28m + why pnl DROP 259k and destin DROP 70k while cash JUMP 2.10m,{SRC_PDF},strong,Vlaanderen>Limburg>Hasselt>DeHummeltjes>JR2025_statutory_L5,tick2441; Strong official native PDF; leftover mined city_hasselt; 13 VE zetel Hasselt; NOT Kloosterstraat 6 Drongen; NOT De Ukkies 0412.729.654; NOT Grauwzusters 0409.771.748 convent; NOT Jessa 0821.142.117; NOT Klein Hemelrijk 0413.866.336 remine; NOT Pinnochio 0438.745.648 remine; NOT Kinderlach 0450.275.186; not TE-additive",
])
print("commitments ok")
