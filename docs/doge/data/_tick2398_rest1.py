#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2398_stamp.txt").read_text().strip().splitlines()
EID = "vzw_car_halle_asse"
SRC_PDF = "src_halleasse_jr2025_nbb_pdf_2398"
COMM = "comm_halleasse_jr2025_statutory_bruto_2_34m_omzet73_empty_pnl_jump"
LB = "lb_halleasse_bruto_2_34m_omzet73_empty_pnl_jump_256k_jr2025"
GAP = "gap_halleasse_riziv_vl_vaph_matrix_bruto_2_34m_omzet73_empty_pnl_jump_destin_505k_l5"
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
    '"{""2025_omzet"":0,""2025_bruto9900"":2343257,""2025_73"":0,'
    '""2025_7076A"":848,""2025_pnl"":255548,""2025_bedrijfswinst"":256459,'
    '""2025_equity"":2180458,""2025_assets"":3012006,""2025_debt"":831548,'
    '""2025_fte"":28,""2025_kapitaalsubsidies"":725722,""2025_destin691"":505074,'
    '""2025_cash"":1268818,""2025_geldbeleggingen"":0,'
    '""2025_personnel62"":2007104,""2025_gebouwen22"":1540395,'
    '""2025_aanbouw27"":0,""2025_capex"":35384,""2025_fondsen10"":3545,'
    '""2025_bestemde13"":1451192,""2025_overgedragen14"":0,'
    '""2025_76A"":848,""2025_66A"":1987,""2025_76B"":0,'
    '""2025_791"":0,""2024_omzet"":0,""2024_73"":0,'
    '""2024_bruto9900"":2148623,""2024_pnl"":219167,""2024_bedrijfswinst"":226071,'
    '""2024_equity"":1952822,""2024_assets"":2801331,""2024_debt"":848508,'
    '""2024_kapitaalsubsidies"":753634,""2024_cash"":1130222,""2024_fte"":26.3,'
    '""2024_destin691"":219167,""2024_geldbeleggingen"":0}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},CAR Halle Asse vzw YE2025 (bruto JUMP 2.34m / omzet+73 empty / pnl JUMP 256k / destin 505k / Strong PDF),{EID},RIZIV + VAZG + leftover city_halle + leftover city_asse,VZW CAR Land van Halle en Asse (KBO 0425.788.230; Actief; 1 VE; RSZ2025 86.959),2026-07-31,2025,2025,2343257,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00364866.pdf,Public CAR dual of mined city_halle + leftover city_asse,Publish RIZIV/VAPH/VAZG/stad matrix behind bruto 2.34m + empty 70/73 + pnl jump 256k + destin bouwfonds 505k + cash 1.27m,{SRC_PDF},strong,Vlaanderen>Vlaams-Brabant>Halle>CAR Halle Asse>JR2025_statutory_L5,tick2398; Strong official native PDF; leftover city_halle after Waas@2397; NOT Waas 0415.472.279; NOT CAR Accent 0413.208.122; NOT CAR Horizon 0418.529.759; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; NOT CAR Houtland-Westkust 0408.436.019; NOT De Schans 0430.473.231; NOT LDSST 0410.121.344; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; NOT Kloosterstraat 6; NOT CAR De Hert; NOT CAR De Klinker; NOT Ascendere; NOT CAR Roeselare; NOT Vijvens; NOT CAR DAT; NOT H.Hart Oudenaarde; NOT Sint-Vincentius Zulte; NOT Floordam; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort; NOT CAR Overleie; NOT Leieborg; NOT Ten Anker; NOT m-accent Eeklo 0465.841.411; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},CAR Halle Asse bruto JUMP 2.34m / omzet+73 empty / pnl JUMP 256k / destin 505k (YE2025 Halle),L5,car_vzw_statutory,Vlaanderen>Vlaams-Brabant>Halle>CAR Halle Asse>JR2025,2343257,2343257,PDF bruto JUMP 2343257 CAR envelope; omzet70 empty; 73 empty; 76A 848; bedrijfswinst JUMP 256459; pnl JUMP 255548; equity JUMP 2180458; assets JUMP 3012006; debt DROP 831548; FTE 28; kapitaalsubsidies DROP 725722; destin691 JUMP 505074 bouwfonds; cash JUMP 1268818; geldbeleggingen empty; gebouwen 1540395; aanbouw 0; capex 35384; personeel 62 2007104,strong,{SRC_PDF},children CAR Halle Asse ambulante revalidatie,RIZIV + VAZG + leftover city_halle + leftover city_asse,2.34m CAR bruto JUMP 9.06pct; omzet+73 empty; pnl JUMP 256k; destin bouwfonds JUMP 505k; cash JUMP 1.27m; leftover city_halle + leftover city_asse,5.3,5.2,5.1,5.20,FOI RIZIV/VAPH/VAZG/stad matrix behind bruto 2.34m + empty 70/73 + pnl jump 256k + destin bouwfonds 505k + cash 1.27m,active,,tick2398; Strong official NBB native PDF + Strong KBO; leftover city_halle after Waas@2397; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Ten Anker OFF Leieborg OFF m-accent Eeklo",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Vlaams-Brabant>Halle>CAR Halle Asse>RIZIV_VAPH_VAZG,{EID},RIZIV/VAPH/VAZG/stad split behind bruto 2343257; why 70 and 73 empty on recognized CAR; why pnl JUMP 255548 (was 219167) and 9901 JUMP 256459; why 691 JUMP 505074 bouwfonds while 14 drops to 0 and bestemde 13 JUMP 1451192; why cash JUMP 1268818 vs schulden DROP 831548; why kapitaalsubsidies DROP 725722 with capex 35384,Strong official PDF leftover public CAR of city_halle + leftover city_asse; 2.34m bruto; public CAR not private clinic; not Waas 0415.472.279; not CAR Accent 0413.208.122; not CAR Horizon 0418.529.759; not ZWZ 0832.024.923; not Zonnebloem 0421.039.386; not CAR Houtland-Westkust 0408.436.019; not De Schans 0430.473.231; not LDSST 0410.121.344; not REVA Kohesi 0410.121.641; not CGG Kohesi 0472.466.907; not BW Kohesi 0451.932.995; not m-accent Eeklo 0465.841.411,8,CAR Land van Halle en Asse VZW / Raad van Bestuur,halle@car-halle-asse.be,"Ziekenhuislaan 35, 1500 Halle",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2398; ready NOT sent; Strong official native NBB PDF; leftover city_halle CAR after Waas@2397; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Ten Anker off Leieborg off m-accent Eeklo; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
