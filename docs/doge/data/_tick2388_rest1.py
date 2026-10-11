#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2388_stamp.txt").read_text().strip().splitlines()
EID = "vzw_reva_kohesi"
SRC_PDF = "src_revakohesi_jr2025_nbb_pdf_2388"
COMM = "comm_revakohesi_jr2025_statutory_omzet_5_96m_73_1_86m_pnl_drop_destin_54k"
LB = "lb_revakohesi_omzet_5_96m_73_1_86m_pnl_drop_destin_54k_jr2025"
GAP = "gap_revakohesi_riziv_vl_vaph_matrix_omzet_5_96m_73_1_86m_pnl_drop_destin_54k_l5"
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
    '"{""2025_omzet"":5960431,""2025_opbr7076A"":8755588,""2025_73"":1863434,'
    '""2025_pnl"":104069,""2025_bedrijfswinst"":107392,""2025_equity"":6474902,'
    '""2025_assets"":8501347,""2025_debt"":2026445,""2025_fte"":85.2,'
    '""2025_kapitaalsubsidies"":1102703,""2025_destin691"":53728,""2025_cash"":1533265,'
    '""2025_geldbeleggingen"":0,""2025_personnel62"":7004590,'
    '""2025_gebouwen22"":3806491,""2025_aanbouw27"":0,'
    '""2025_capex"":606926,""2025_fondsen10"":78086,'
    '""2025_bestemde13"":1751148,""2025_overgedragen14"":3542964,'
    '""2025_76A"":143314,""2025_74"":788410,'
    '""2024_omzet"":6140547,""2024_opbr7076A"":8726460,'
    '""2024_73"":1879253,""2024_pnl"":356497,""2024_bedrijfswinst"":348267,'
    '""2024_equity"":6448986,""2024_assets"":8708551,""2024_debt"":2259565,'
    '""2024_kapitaalsubsidies"":1180857,""2024_cash"":1964824,""2024_fte"":81.9,'
    '""2024_destin691"":152899,""2024_geldbeleggingen"":500000}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},REVA Kohesi vzw YE2025 (omzet DROP 5.96m / 73 1.86m / pnl DROP 104k / destin 54k / Strong PDF),{EID},Departement Zorg + leftover city_hasselt,VZW REVA Kohesi (KBO 0410.121.641; Actief; 8 VE; RSZ2025 88.999),2026-06-29,2025,2025,5960431,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00244637.pdf,Public CAR/Reval dual of mined city_hasselt,Publish RIZIV/VL/VAPH/KDV matrix inside omzet 5.96m + 73 1.86m + pnl DROP 104k + destin 54k + cash 1.53m DROP + 1.10m kapitaalsubsidies DROP,{SRC_PDF},strong,Vlaanderen>Limburg>Hasselt>REVA_Kohesi>JR2025_statutory_L5,tick2388; Strong official native PDF; leftover city_hasselt after De Hert@2387; NOT CGG Kohesi 0472.466.907; NOT Kloosterstraat 6; NOT CAR De Hert; NOT CAR De Klinker; NOT Ascendere; NOT CAR Roeselare; NOT Vijvens; NOT CAR DAT; NOT H.Hart Oudenaarde; NOT Sint-Vincentius Zulte; NOT Floordam; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort; NOT CAR Overleie; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},REVA Kohesi omzet DROP 5.96m / 73 1.86m / pnl DROP 104k / destin 54k (YE2025 Hasselt),L5,car_vzw_statutory,Vlaanderen>Limburg>Hasselt>REVA_Kohesi>JR2025,5960431,5960431,PDF omzet DROP 5960431 CAR envelope; 73 DROP 1863434; 70/76A JUMP 8755588; bedrijfswinst DROP 107392; pnl DROP 104069; equity JUMP 6474902; assets DROP 8501347; debt DROP 2026445; FTE 85.2 JUMP; kapitaalsubsidies DROP 1102703; destin691 DROP 53728; cash DROP 1533265; geldbeleggingen empty; gebouwen 3806491; capex 606926; personnel 7004590,strong,{SRC_PDF},children and adults CAR/Reval Limburg + KDV Maasmechelen,Departement Zorg + leftover city_hasselt,5.96m CAR omzet DROP; 73 1.86m; pnl DROP 71pct; destin 54k DROP; cash 1.53m DROP; 1.10m kapitaalsubsidies DROP; leftover city_hasselt,5.6,5.5,5.0,5.37,FOI RIZIV/VL/VAPH/KDV matrix + 73 1.86m + pnl DROP 104k + destin 54k + cash 1.53m DROP + 1.10m kapitaalsubsidies + BTW-eenheid,active,,tick2388; Strong official NBB native PDF + Strong KBO; leftover city_hasselt after De Hert@2387; OFF Drongen OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF CGG Kohesi",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Limburg>Hasselt>REVA_Kohesi>RIZIV_VL_VAPH_CAR,{EID},RIZIV/Departement Zorg/VAPH/OPGROEIEN split inside omzet 5960431; why 73 1863434 vs omzet DROP 2.93pct; why destin 691 53728 DROP 64.86pct; why cash 1533265 DROP and 50/53 emptied; nature of kapitaalsubsidies 15 1102703 DROP; 76A meerwaarde 143314; FTE JUMP 85.2; BTW-eenheid CGG/Beschut Wonen/LDSST/De Schans,Strong official PDF leftover public CAR of city_hasselt; 5.96m omzet; public not private clinic; not CGG Kohesi 0472.466.907,8,REVA Kohesi VZW / Erik Ottenbourgs voorzitter / Johan Gommers gedelegeerd bestuurder,info@kohesi.be,"Ilgatlaan 11 bus 4, 3500 Hasselt",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2388; ready NOT sent; Strong official native NBB PDF; leftover city_hasselt CAR after De Hert@2387; off Drongen off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off CGG Kohesi; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
