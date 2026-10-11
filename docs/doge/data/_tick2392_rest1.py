#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2392_stamp.txt").read_text().strip().splitlines()
EID = "vzw_car_houtland"
SRC_PDF = "src_houtland_jr2025_nbb_pdf_2392"
COMM = "comm_houtland_jr2025_statutory_omzet_4_93m_73_1_06m_pnl_flip"
LB = "lb_houtland_omzet_4_93m_73_1_06m_pnl_flip_destin_empty_jr2025"
GAP = "gap_houtland_riziv_vl_vaph_matrix_omzet_4_93m_73_1_06m_pnl_flip_destin_empty_l5"
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
    '"{""2025_omzet"":4926107,""2025_bruto9900"":0,""2025_73"":1056007,'
    '""2025_7076A"":6109882,""2025_pnl"":34332,""2025_bedrijfswinst"":19339,'
    '""2025_equity"":3945582,""2025_assets"":6149424,""2025_debt"":2103842,'
    '""2025_fte"":63,""2025_kapitaalsubsidies"":1231624,""2025_destin691"":0,'
    '""2025_cash"":837963,""2025_geldbeleggingen"":999454,'
    '""2025_personnel62"":5429501,""2025_gebouwen22"":3531617,'
    '""2025_aanbouw27"":136226,""2025_capex"":256888,""2025_fondsen10"":900747,'
    '""2025_bestemde13"":1486530,""2025_overgedragen14"":326681,'
    '""2025_76A"":109313,""2025_74"":18455,""2025_731"":9514,""2025_733"":1046493,'
    '""2025_791"":0,""2024_omzet"":4805460,""2024_73"":945586,'
    '""2024_7076A"":5978212,""2024_pnl"":-86910,""2024_bedrijfswinst"":-90942,'
    '""2024_equity"":3727458,""2024_assets"":6154150,""2024_debt"":2326692,'
    '""2024_kapitaalsubsidies"":1047832,""2024_cash"":1094248,""2024_fte"":63.3,'
    '""2024_destin691"":0,""2024_geldbeleggingen"":890998}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},CAR Houtland-Westkust vzw YE2025 (omzet JUMP 4.93m / 73 1.06m / pnl PROFIT FLIP 34k / destin empty / Strong PDF),{EID},Departement Zorg + leftover city_zedelgem + leftover city_nieuwpoort,VZW CAR Houtland-Westkust (KBO 0408.436.019; Actief; 2 VE; RSZ2025 86.959),2026-05-20,2025,2025,4926107,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00115391.pdf,Public CAR dual of mined city_zedelgem + city_nieuwpoort,Publish RIZIV/VL/VAPH matrix inside omzet 4.93m + 73 1.06m + pnl flip 34k + kapitaalsubsidies 1.23m + destin empty,{SRC_PDF},strong,Vlaanderen>West-Vlaanderen>Zedelgem>CARHoutland>JR2025_statutory_L5,tick2392; Strong official native PDF; leftover city_zedelgem + leftover city_nieuwpoort after De Schans@2391; NOT De Schans 0430.473.231; NOT LDSST 0410.121.344; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; NOT Kloosterstraat 6; NOT CAR De Hert; NOT CAR De Klinker; NOT Ascendere; NOT CAR Roeselare; NOT Vijvens; NOT CAR DAT; NOT H.Hart Oudenaarde; NOT Sint-Vincentius Zulte; NOT Floordam; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort; NOT CAR Overleie; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},CAR Houtland-Westkust omzet JUMP 4.93m / 73 1.06m / pnl PROFIT FLIP 34k / destin empty (YE2025 Zedelgem),L5,car_vzw_statutory,Vlaanderen>West-Vlaanderen>Zedelgem>CARHoutland>JR2025,4926107,4926107,PDF omzet JUMP 4926107 CAR envelope; 73 JUMP 1056007; 70/76A JUMP 6109882; bedrijfswinst PROFIT FLIP 19339; pnl PROFIT FLIP 34332; equity JUMP 3945582; assets DROP 6149424; debt DROP 2103842; FTE 63; kapitaalsubsidies JUMP 1231624; destin691 empty; cash DROP 837963; geldbeleggingen 999454; gebouwen 3531617; aanbouw 136226; capex 256888; personeel 62 5429501,strong,{SRC_PDF},children developmental CAR Zedelgem + Nieuwpoort,Departement Zorg + leftover city_zedelgem + leftover city_nieuwpoort,4.93m CAR omzet JUMP 2.5pct; 73 1.06m JUMP; pnl PROFIT FLIP 34k; kapitaalsubsidies 1.23m JUMP; destin empty; leftover city_zedelgem,5.6,5.5,5.3,5.52,FOI RIZIV/VL/VAPH matrix + omzet 4.93m + 73 1.06m + pnl flip 34k + kapitaalsubsidies 1.23m + destin empty + campus split t Veld/Elora,active,,tick2392; Strong official NBB native PDF + Strong KBO; leftover city_zedelgem + leftover city_nieuwpoort after De Schans@2391; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>West-Vlaanderen>Zedelgem>CARHoutland>RIZIV_VL_VAPH,{EID},RIZIV/Zorg/VAPH split inside omzet 4926107 vs 73 1056007; why pnl PROFIT FLIP 34332 (was -86910); why 691 empty while 34332 fully to overgedragen 326681; why kapitaalsubsidies JUMP 1231624 and aanbouw 136226; why cash DROP 837963 vs geldbeleggingen JUMP 999454; campus split t Veld/Elora; BTW 35.140,Strong official PDF leftover public CAR of city_zedelgem + city_nieuwpoort; 4.93m omzet; public not private clinic; not De Schans 0430.473.231; not LDSST 0410.121.344; not REVA Kohesi 0410.121.641; not CGG Kohesi 0472.466.907; not BW Kohesi 0451.932.995,8,CAR Houtland-Westkust VZW / Raad van Bestuur,info@carelora.be,"Ichtegemsestraat 32, 8211 Zedelgem",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2392; ready NOT sent; Strong official native NBB PDF; leftover city_zedelgem CAR after De Schans@2391; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
