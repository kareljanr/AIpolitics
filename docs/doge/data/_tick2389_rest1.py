#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2389_stamp.txt").read_text().strip().splitlines()
EID = "vzw_bw_kohesi"
SRC_PDF = "src_bwkohesi_jr2025_nbb_pdf_2389"
COMM = "comm_bwkohesi_jr2025_statutory_omzet_1_29m_73_488k_pnl_jump_destin_empty"
LB = "lb_bwkohesi_omzet_1_29m_73_488k_pnl_jump_destin_empty_jr2025"
GAP = "gap_bwkohesi_riziv_vl_ibw_matrix_omzet_1_29m_73_488k_pnl_jump_destin_empty_l5"
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
    '"{""2025_omzet"":1294776,""2025_bruto9900"":1243451,""2025_73"":487682,'
    '""2025_pnl"":18602,""2025_bedrijfswinst"":18146,""2025_equity"":615414,'
    '""2025_assets"":1101290,""2025_debt"":485876,""2025_fte"":15.2,'
    '""2025_kapitaalsubsidies"":0,""2025_destin691"":0,""2025_cash"":645903,'
    '""2025_geldbeleggingen"":0,""2025_personnel62"":1217122,'
    '""2025_gebouwen22"":0,""2025_aanbouw27"":0,'
    '""2025_capex"":14094,""2025_fondsen10"":21533,'
    '""2025_bestemde13"":304281,""2025_overgedragen14"":289600,'
    '""2025_76A"":0,""2025_791"":4046,'
    '""2024_omzet"":1256608,""2024_bruto9900"":1269419,'
    '""2024_73"":501440,""2024_pnl"":11017,""2024_bedrijfswinst"":9962,'
    '""2024_equity"":596811,""2024_assets"":1070944,""2024_debt"":474132,'
    '""2024_kapitaalsubsidies"":0,""2024_cash"":734043,""2024_fte"":15.1,'
    '""2024_destin691"":11017,""2024_geldbeleggingen"":0}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},Beschut Wonen Kohesi vzw YE2025 (omzet JUMP 1.29m / 73 488k / pnl JUMP 19k / destin empty / Strong PDF),{EID},Departement Zorg + leftover city_heusden_zolder,VZW Beschut Wonen Kohesi (KBO 0451.932.995; Actief; 2 VE; RSZ2025 87.205),2026-06-29,2025,2025,1294776,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00243983.pdf,Public IBW dual of mined city_heusden_zolder,Publish RIZIV/VL/IBW matrix inside omzet 1.29m + 73 488k + pnl JUMP 19k + destin empty + cash 646k DROP,{SRC_PDF},strong,Vlaanderen>Limburg>Heusden-Zolder>BW_Kohesi>JR2025_statutory_L5,tick2389; Strong official native PDF; leftover city_heusden_zolder after REVA@2388; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT Kloosterstraat 6; NOT CAR De Hert; NOT CAR De Klinker; NOT Ascendere; NOT CAR Roeselare; NOT Vijvens; NOT CAR DAT; NOT H.Hart Oudenaarde; NOT Sint-Vincentius Zulte; NOT Floordam; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort; NOT CAR Overleie; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},Beschut Wonen Kohesi omzet JUMP 1.29m / 73 488k / pnl JUMP 19k / destin empty (YE2025 Heusden-Zolder),L5,beschut_wonen_vzw_statutory,Vlaanderen>Limburg>Heusden-Zolder>BW_Kohesi>JR2025,1294776,1294776,PDF omzet JUMP 1294776 IBW envelope; 73 DROP 487682; bruto DROP 1243451; bedrijfswinst JUMP 18146; pnl JUMP 18602; equity JUMP 615414; assets JUMP 1101290; debt JUMP 485876; FTE 15.2 JUMP; kapitaalsubsidies empty; destin691 empty; cash DROP 645903; geldbeleggingen empty; gebouwen empty; capex 14094; personnel 1217122,strong,{SRC_PDF},adults psychiatric supported housing West-Limburg,Departement Zorg + leftover city_heusden_zolder,1.29m IBW omzet JUMP; 73 488k; pnl JUMP 69pct; destin empty; cash 646k DROP; leftover city_heusden_zolder + city_beringen,5.3,4.8,4.9,5.00,FOI RIZIV/VL/IBW matrix + 73 488k + pnl JUMP 19k + destin empty + cash 646k DROP + BTW-eenheid,active,,tick2389; Strong official NBB native PDF + Strong KBO; leftover city_heusden_zolder after REVA@2388; OFF Drongen OFF REVA Kohesi OFF CGG Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Limburg>Heusden-Zolder>BW_Kohesi>RIZIV_VL_IBW,{EID},RIZIV/Departement Zorg IBW split inside omzet 1294776; why 73 487682 vs omzet JUMP 3.04pct; why destin 691 empty (was 11017) and 791 4046; why cash 645903 DROP; nature of handelsvorderingen JUMP 245173; FTE JUMP 15.2; BTW-eenheid REVA/CGG/LDSST/De Schans,Strong official PDF leftover public IBW of city_heusden_zolder; 1.29m omzet; public not private clinic; not REVA Kohesi 0410.121.641; not CGG Kohesi 0472.466.907,8,Beschut Wonen Kohesi VZW / Erik Ottenbourgs voorzitter / Johan Gommers dagelijks bestuur,info@kohesi.be,"Pastoor Paquaylaan 123 bus 1, 3550 Heusden-Zolder",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2389; ready NOT sent; Strong official native NBB PDF; leftover city_heusden_zolder IBW after REVA@2388; off Drongen off REVA Kohesi off CGG Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
