#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2386_stamp.txt").read_text().strip().splitlines()
EID = "vzw_car_deklinker"
SRC_PDF = "src_deklinker_jr2025_nbb_pdf_2386"
COMM = "comm_deklinker_jr2025_statutory_bruto_1_62m_omzet73_empty_destin_179k"
LB = "lb_deklinker_bruto_1_62m_omzet73_empty_destin_179k_jr2025"
GAP = "gap_deklinker_riziv_vl_vaph_matrix_bruto_1_62m_omzet73_empty_destin_179k_l5"
DRAFT = f"docs/doge/foi/drafts/{GAP}.md"

def append_lines(path: Path, lines):
    raw = path.read_bytes()
    if not raw.endswith(b"\n"):
        raise SystemExit(f"{path} does not end with LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"):
                line = line + "\n"
            f.write(line.encode("utf-8"))
    print("appended", len(lines), "->", path.name)

cash_json = (
    '"{""2025_omzet"":null,""2025_bruto"":1615845,""2025_73"":null,'
    '""2025_pnl"":68250,""2025_bedrijfswinst"":68351,""2025_equity"":421965,'
    '""2025_assets"":835288,""2025_debt"":413323,""2025_fte"":18.6,'
    '""2025_kapitaalsubsidies"":127157,""2025_destin691"":179028,""2025_cash"":268878,'
    '""2025_geldbeleggingen"":0,""2025_personnel62"":1517396,'
    '""2025_gebouwen22"":393505,""2025_aanbouw27"":0,'
    '""2025_capex8169"":16945,""2025_fondsen10"":115780,'
    '""2025_bestemde13"":179028,""2025_overgedragen14"":0,'
    '""2025_fin_opbr75"":1992,'
    '""2024_omzet"":null,""2024_bruto"":1481932,'
    '""2024_73"":null,""2024_pnl"":63931,""2024_bedrijfswinst"":61257,'
    '""2024_equity"":363391,""2024_assets"":748693,""2024_debt"":385302,'
    '""2024_kapitaalsubsidies"":136832,""2024_cash"":218697,""2024_fte"":16.6,'
    '""2024_destin691"":0,""2024_geldbeleggingen"":0}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},CAR De Klinker Ieper vzw YE2025 (bruto 1.62m / omzet+73 empty / destin 179k / Strong PDF),{EID},RIZIV + Departement Zorg + VAPH + leftover city_ieper,VZW CAR De Klinker (KBO 0430.535.290; Actief; 1 VE 2.154.433.940; RSZ2025 86.959),2026-07-02,2025,2025,1615845,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00241698.pdf,Public CAR dual of mined city_ieper,Publish RIZIV/VL/VAPH matrix inside bruto 1.62m + explain empty omzet70/73 on VKT + destin 179k full allocation + cash 269k JUMP + 127k kapitaalsubsidies DROP,{SRC_PDF},strong,Vlaanderen>West-Vlaanderen>Ieper>CAR_De_Klinker>JR2025_statutory_L5,tick2386; Strong official native PDF; leftover city_ieper after Ascendere@2385; NOT school Rotselaar; NOT Kloosterstraat 6; NOT Ascendere; NOT CAR Roeselare; NOT Vijvens; NOT CAR DAT; NOT H.Hart Oudenaarde; NOT Sint-Vincentius Zulte; NOT Floordam; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort; NOT CAR Overleie; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},CAR De Klinker Ieper bruto 1.62m / omzet+73 empty / destin 179k (YE2025 Ieper),L5,car_vzw_statutory,Vlaanderen>West-Vlaanderen>Ieper>CAR_De_Klinker>JR2025,1615845,1615845,PDF bruto JUMP 1615845 VKT envelope; omzet70 empty; 73 empty; bedrijfswinst JUMP 68351; pnl JUMP 68250; equity JUMP 421965; assets JUMP 835288; debt JUMP 413323; FTE 18.6 JUMP; kapitaalsubsidies DROP 127157; destin691 JUMP 179028; cash JUMP 268878; geldbeleggingen empty; gebouwen 393505; capex 16945; personnel 1517396,strong,{SRC_PDF},children with language/speech/motor/development/hearing difficulties Ieper,RIZIV + Departement Zorg + VAPH + leftover city_ieper,1.62m CAR bruto; omzet+73 empty on VKT; destin 179k full allocation; cash 269k JUMP; 127k kapitaalsubsidies DROP; leftover city_ieper,5.3,4.9,5.0,5.07,FOI RIZIV/VL/VAPH matrix + empty omzet70/73 + destin 179k + cash 269k JUMP + 127k kapitaalsubsidies,active,,tick2386; Strong official NBB native PDF + Strong KBO; leftover city_ieper after Ascendere@2385; OFF Drongen OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>West-Vlaanderen>Ieper>CAR_De_Klinker>RIZIV_VL_VAPH_CAR,{EID},RIZIV/Departement Zorg/VAPH split inside bruto 1615845; why omzet70 and 73 empty on VKT; why destin 691 179028 full allocation (overgedragen emptied); why cash 268878 JUMP; nature of kapitaalsubsidies 15 127157 DROP; FTE JUMP 18.6,Strong official PDF leftover public CAR of city_ieper; 1.62m bruto; public not private clinic; not school Rotselaar,8,CAR De Klinker VZW / Luc Colman voorzitter / Johan Messely gedelegeerd bestuurder,info@cardeklinker.be,"Cartonstraat 53, 8900 Ieper",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2386; ready NOT sent; Strong official native NBB PDF; leftover city_ieper CAR after Ascendere@2385; off Drongen off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
