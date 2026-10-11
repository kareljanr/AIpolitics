#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2387_stamp.txt").read_text().strip().splitlines()
EID = "vzw_car_de_hert"
SRC_PDF = "src_dehert_jr2025_nbb_pdf_2387"
COMM = "comm_dehert_jr2025_statutory_omzet_1_87m_73_634k_pnl_jump_destin_empty"
LB = "lb_dehert_omzet_1_87m_73_634k_pnl_jump_destin_empty_jr2025"
GAP = "gap_dehert_riziv_vl_vaph_matrix_omzet_1_87m_73_634k_pnl_jump_destin_empty_l5"
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
    '"{""2025_omzet"":1869719,""2025_bruto"":2409407,""2025_73"":634363,'
    '""2025_pnl"":31450,""2025_bedrijfswinst"":31824,""2025_equity"":2657601,'
    '""2025_assets"":3220530,""2025_debt"":562928,""2025_fte"":27,'
    '""2025_kapitaalsubsidies"":1066108,""2025_destin691"":0,""2025_cash"":924004,'
    '""2025_geldbeleggingen"":0,""2025_personnel62"":2217469,'
    '""2025_gebouwen22"":2182790,""2025_aanbouw27"":0,'
    '""2025_capex8169"":1185,""2025_fondsen10"":232865,'
    '""2025_bestemde13"":0,""2025_overgedragen14"":1358628,'
    '""2025_76A"":17014,'
    '""2024_omzet"":1822944,""2024_bruto"":2251797,'
    '""2024_73"":538499,""2024_pnl"":2939,""2024_bedrijfswinst"":3683,'
    '""2024_equity"":2674611,""2024_assets"":3195892,""2024_debt"":521280,'
    '""2024_kapitaalsubsidies"":1114568,""2024_cash"":676724,""2024_fte"":24.7,'
    '""2024_destin691"":0,""2024_geldbeleggingen"":0}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},CAR De Hert Aalst vzw YE2025 (omzet 1.87m / 73 634k / pnl JUMP 31k / destin empty / Strong PDF),{EID},Departement Zorg + VAPH + leftover city_aalst,VZW CAR De Hert (KBO 0409.371.672; Actief; 1 VE 2.153.754.445; RSZ2025 86.959),2026-06-19,2025,2025,1869719,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00174560.pdf,Public CAR dual of mined city_aalst,Publish RIZIV/VL/VAPH matrix inside omzet 1.87m + 73 JUMP 634k + pnl JUMP 31k + destin empty + cash 924k JUMP + 1.07m kapitaalsubsidies DROP,{SRC_PDF},strong,Vlaanderen>Oost-Vlaanderen>Aalst>CAR_De_Hert>JR2025_statutory_L5,tick2387; Strong official native PDF; leftover city_aalst after De Klinker@2386; NOT CGG Kohesi; NOT REVA Kohesi; NOT Kloosterstraat 6; NOT CAR De Klinker; NOT Ascendere; NOT CAR Roeselare; NOT Vijvens; NOT CAR DAT; NOT H.Hart Oudenaarde; NOT Sint-Vincentius Zulte; NOT Floordam; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort; NOT CAR Overleie; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},CAR De Hert Aalst omzet 1.87m / 73 634k / pnl JUMP 31k / destin empty (YE2025 Aalst),L5,car_vzw_statutory,Vlaanderen>Oost-Vlaanderen>Aalst>CAR_De_Hert>JR2025,1869719,1869719,PDF omzet JUMP 1869719 CAR envelope; 73 JUMP 634363; bruto JUMP 2409407; bedrijfswinst JUMP 31824; pnl JUMP 31450; equity DROP 2657601; assets JUMP 3220530; debt JUMP 562928; FTE 27 JUMP; kapitaalsubsidies DROP 1066108; destin691 empty; cash JUMP 924004; geldbeleggingen empty; gebouwen 2182790; capex 1185; personnel 2217469,strong,{SRC_PDF},children with developmental difficulties Aalst,Departement Zorg + VAPH + leftover city_aalst,1.87m CAR omzet; 73 JUMP 634k; pnl JUMP 970pct; destin empty; cash 924k JUMP; 1.07m kapitaalsubsidies DROP; leftover city_aalst,5.4,5.0,5.0,5.13,FOI RIZIV/VL/VAPH matrix + 73 JUMP 634k + pnl JUMP 31k + destin empty + cash 924k JUMP + 1.07m kapitaalsubsidies,active,,tick2387; Strong official NBB native PDF + Strong KBO; leftover city_aalst after De Klinker@2386; OFF Drongen OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Oost-Vlaanderen>Aalst>CAR_De_Hert>RIZIV_VL_VAPH_CAR,{EID},RIZIV/Departement Zorg/VAPH split inside omzet 1869719; why 73 634363 JUMP +17.80pct vs omzet +2.57pct; why destin 691 empty while overgedragen 14 1358628; why cash 924004 JUMP; nature of kapitaalsubsidies 15 1066108 DROP; FTE JUMP 27,Strong official PDF leftover public CAR of city_aalst; 1.87m omzet; public not private clinic; not CGG/REVA Kohesi,8,CAR De Hert VZW / Kristof Vandenbogaerde voorzitter / Marie-Therese De Wael secretaris,info@cardehert.be,"Rozendreef 250, 9300 Aalst",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2387; ready NOT sent; Strong official native NBB PDF; leftover city_aalst CAR after De Klinker@2386; off Drongen off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
