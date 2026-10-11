#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2394_stamp.txt").read_text().strip().splitlines()
EID = "vzw_zwz"
SRC_PDF = "src_zwz_jr2025_nbb_pdf_2394"
COMM = "comm_zwz_jr2025_statutory_omzet_10_69m_73_1_97m_pnl_drop"
LB = "lb_zwz_omzet_10_69m_73_1_97m_pnl_drop_destin_empty_jr2025"
GAP = "gap_zwz_zorgkas_riziv_wzc_matrix_omzet_10_69m_73_1_97m_pnl_drop_destin_empty_l5"
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
    '"{""2025_omzet"":10693272,""2025_bruto9900"":0,""2025_73"":1971245,'
    '""2025_7076A"":13006495,""2025_pnl"":45054,""2025_bedrijfswinst"":256073,'
    '""2025_equity"":12902648,""2025_assets"":33038468,""2025_debt"":20135821,'
    '""2025_fte"":120.2,""2025_kapitaalsubsidies"":5917611,""2025_destin691"":0,'
    '""2025_cash"":4229666,""2025_geldbeleggingen"":0,'
    '""2025_personnel62"":8388859,""2025_gebouwen22"":21049473,'
    '""2025_aanbouw27"":0,""2025_capex"":7363513,""2025_fondsen10"":2625000,'
    '""2025_bestemde13"":749293,""2025_overgedragen14"":3610743,'
    '""2025_76A"":83799,""2025_74"":258178,""2025_731"":0,""2025_733"":1971245,'
    '""2025_791"":0,""2024_omzet"":10175910,""2024_73"":1923731,'
    '""2024_bruto9900"":0,""2024_pnl"":783928,""2024_bedrijfswinst"":802457,'
    '""2024_equity"":13429711,""2024_assets"":27549707,""2024_debt"":14119996,'
    '""2024_kapitaalsubsidies"":6489728,""2024_cash"":4438804,""2024_fte"":114.2,'
    '""2024_destin691"":396188,""2024_geldbeleggingen"":0}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},ZWZ vzw YE2025 (omzet JUMP 10.69m / 73 1.97m / pnl DROP 45k / destin empty / Strong PDF),{EID},zorgkas + RIZIV + leftover city_zedelgem,VZW Zorg en Welzijn Zedelgem (KBO 0832.024.923; Actief; 1 VE; RSZ2025 87.101),2026-07-01,2025,2025,10693272,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00228427.pdf,Public WZC dual of mined city_zedelgem,Publish zorgkas/RIZIV/VIPA/OCMW matrix inside omzet 10.69m + 73 1.97m + pnl drop 45k + kapitaalsubsidies 5.92m + debt jump 20.14m + destin empty,{SRC_PDF},strong,Vlaanderen>West-Vlaanderen>Zedelgem>ZWZ>JR2025_statutory_L5,tick2394; Strong official native PDF; leftover city_zedelgem after Zonnebloem@2393; NOT CAR Houtland-Westkust 0408.436.019; NOT Zonnebloem 0421.039.386; NOT De Schans 0430.473.231; NOT LDSST 0410.121.344; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; NOT Kloosterstraat 6; NOT CAR De Hert; NOT CAR De Klinker; NOT Ascendere; NOT CAR Roeselare; NOT Vijvens; NOT CAR DAT; NOT H.Hart Oudenaarde; NOT Sint-Vincentius Zulte; NOT Floordam; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort; NOT CAR Overleie; NOT Leieborg; NOT Ten Anker; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},ZWZ omzet JUMP 10.69m / 73 1.97m / pnl DROP 45k / destin empty (YE2025 Zedelgem),L5,wzc_vzw_statutory,Vlaanderen>West-Vlaanderen>Zedelgem>ZWZ>JR2025,10693272,10693272,PDF omzet JUMP 10693272 WZC envelope; 73 JUMP 1971245; 70/76A JUMP 13006495; bedrijfswinst DROP 256073; pnl DROP 45054; equity DROP 12902648; assets JUMP 33038468; debt JUMP 20135821; FTE 120.2; kapitaalsubsidies DROP 5917611; destin691 empty; cash DROP 4229666; gebouwen 21049473; aanbouw 0; capex 7363513; personeel 62 8388859,strong,{SRC_PDF},elderly WZC Klaverveld Zedelgem PPS,zorgkas + leftover city_zedelgem,10.69m WZC omzet JUMP 5.1pct; 73 1.97m; pnl DROP 45k; debt JUMP 20.14m; capex 7.36m; destin empty; leftover city_zedelgem,5.8,5.7,5.6,5.72,FOI zorgkas/RIZIV/VIPA/OCMW matrix + omzet 10.69m + 73 1.97m + pnl drop 45k + kapitaalsubsidies 5.92m + debt jump 20.14m + destin empty + campus split Klaverveld,active,,tick2394; Strong official NBB native PDF + Strong KBO; leftover city_zedelgem after Zonnebloem@2393; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF Ten Anker OFF Leieborg",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>West-Vlaanderen>Zedelgem>ZWZ>zorgkas_RIZIV_VIPA,{EID},zorgkas/RIZIV/VIPA/OCMW split inside omzet 10693272 + 73 1971245; why pnl DROP 45054 (was 783928); why 691 empty while 45054 fully to overgedragen 3610743 (YE2024 691 was 396188); why kapitaalsubsidies DROP 5917611 and capex 7363513 with debt JUMP 20135821; why cash DROP 4229666 vs assets JUMP 33038468; campus split Klaverveld/CKV/DVC/Klaverhof,Strong official PDF leftover public WZC of city_zedelgem; 10.69m omzet; public PPS not private clinic; not CAR Houtland-Westkust 0408.436.019; not Zonnebloem 0421.039.386; not De Schans 0430.473.231; not LDSST 0410.121.344; not REVA Kohesi 0410.121.641; not CGG Kohesi 0472.466.907; not BW Kohesi 0451.932.995,8,Zorg en Welzijn Zedelgem VZW / Raad van Bestuur,info@zwz.be,"Fazantenlaan 89, 8210 Zedelgem",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2394; ready NOT sent; Strong official native NBB PDF; leftover city_zedelgem WZC after Zonnebloem@2393; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off Ten Anker off Leieborg; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
