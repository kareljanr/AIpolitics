#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2393_stamp.txt").read_text().strip().splitlines()
EID = "vzw_zonnebloem"
SRC_PDF = "src_zonnebloem_jr2025_nbb_pdf_2393"
COMM = "comm_zonnebloem_jr2025_statutory_bruto_4_58m_omzet73_empty_pnl_drop"
LB = "lb_zonnebloem_bruto_4_58m_omzet73_empty_pnl_drop_destin_empty_jr2025"
GAP = "gap_zonnebloem_vaph_mfc_matrix_bruto_4_58m_omzet73_empty_pnl_drop_destin_empty_l5"
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
    '"{""2025_omzet"":0,""2025_bruto9900"":4579601,""2025_73"":0,'
    '""2025_7076A"":0,""2025_pnl"":182958,""2025_bedrijfswinst"":176097,'
    '""2025_equity"":2994675,""2025_assets"":3793570,""2025_debt"":798895,'
    '""2025_fte"":60.8,""2025_kapitaalsubsidies"":711539,""2025_destin691"":0,'
    '""2025_cash"":983179,""2025_geldbeleggingen"":0,'
    '""2025_personnel62"":4162454,""2025_gebouwen22"":2380480,'
    '""2025_aanbouw27"":0,""2025_capex"":133836,""2025_fondsen10"":24167,'
    '""2025_bestemde13"":1190161,""2025_overgedragen14"":1068808,'
    '""2025_76A"":0,""2025_74"":0,""2025_731"":0,""2025_733"":0,'
    '""2025_791"":0,""2024_omzet"":0,""2024_73"":0,'
    '""2024_bruto9900"":4318309,""2024_pnl"":226641,""2024_bedrijfswinst"":212692,'
    '""2024_equity"":2845599,""2024_assets"":3697414,""2024_debt"":851815,'
    '""2024_kapitaalsubsidies"":745421,""2024_cash"":875660,""2024_fte"":59.3,'
    '""2024_destin691"":0,""2024_geldbeleggingen"":0}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},Zonnebloem vzw YE2025 (bruto JUMP 4.58m / omzet+73 empty / pnl DROP 183k / destin empty / Strong PDF),{EID},VAPH + leftover city_kortrijk,VZW Zonnebloem (KBO 0421.039.386; Actief; 2 VE; RSZ2025 87.201),2026-07-06,2025,2025,4579601,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00254348.pdf,Public VAPH MFC dual of mined city_kortrijk,Publish VAPH/KgG matrix inside bruto 4.58m + omzet73 empty + pnl drop 183k + kapitaalsubsidies 712k + destin empty,{SRC_PDF},strong,Vlaanderen>West-Vlaanderen>Kortrijk>Zonnebloem>JR2025_statutory_L5,tick2393; Strong official native PDF; leftover city_kortrijk after Houtland@2392; NOT CAR Houtland-Westkust 0408.436.019; NOT De Schans 0430.473.231; NOT LDSST 0410.121.344; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; NOT Kloosterstraat 6; NOT CAR De Hert; NOT CAR De Klinker; NOT Ascendere; NOT CAR Roeselare; NOT Vijvens; NOT CAR DAT; NOT H.Hart Oudenaarde; NOT Sint-Vincentius Zulte; NOT Floordam; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort; NOT CAR Overleie; NOT Leieborg; NOT Ten Anker; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},Zonnebloem bruto JUMP 4.58m / omzet+73 empty / pnl DROP 183k / destin empty (YE2025 Kortrijk),L5,vaph_vzw_statutory,Vlaanderen>West-Vlaanderen>Kortrijk>Zonnebloem>JR2025,4579601,4579601,PDF bruto JUMP 4579601 VAPH envelope; omzet70 empty; 73 empty; bedrijfswinst DROP 176097; pnl DROP 182958; equity JUMP 2994675; assets JUMP 3793570; debt DROP 798895; FTE 60.8; kapitaalsubsidies DROP 711539; destin691 empty; cash JUMP 983179; gebouwen 2380480; aanbouw empty; capex 133836; personeel 62 4162454,strong,{SRC_PDF},children youth disability VAPH MFC Kortrijk + KDV Madelief,VAPH + leftover city_kortrijk,4.58m VAPH bruto JUMP 6.1pct; omzet73 empty VKT; pnl DROP 183k; kapitaalsubsidies 712k DROP; destin empty; leftover city_kortrijk,5.4,5.3,5.2,5.38,FOI VAPH/KgG matrix + bruto 4.58m + omzet73 empty + pnl drop 183k + kapitaalsubsidies 712k + destin empty + campus split MFC/Madelief,active,,tick2393; Strong official NBB native PDF + Strong KBO; leftover city_kortrijk after Houtland@2392; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Ten Anker OFF Leieborg",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>West-Vlaanderen>Kortrijk>Zonnebloem>VAPH_KgG,{EID},VAPH/KgG/stad split inside bruto 4579601 vs empty omzet70/73; why pnl DROP 182958 (was 226641); why 691 empty while 182958 fully to overgedragen 1068808; why kapitaalsubsidies DROP 711539 and capex 133836; why cash JUMP 983179 vs debt DROP 798895; campus split MFC/Madelief,Strong official PDF leftover public VAPH MFC of city_kortrijk; 4.58m bruto; public not private clinic; not CAR Houtland-Westkust 0408.436.019; not De Schans 0430.473.231; not LDSST 0410.121.344; not REVA Kohesi 0410.121.641; not CGG Kohesi 0472.466.907; not BW Kohesi 0451.932.995,8,Zonnebloem VZW / Raad van Bestuur,algemeen@zonnebloemvzw.be,"Steenstraat 14, 8501 Kortrijk",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2393; ready NOT sent; Strong official native NBB PDF; leftover city_kortrijk VAPH after Houtland@2392; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Ten Anker off Leieborg; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
